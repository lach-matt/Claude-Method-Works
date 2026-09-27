#!/usr/bin/env python3
"""DOCKET 67 / hawking-unruh-analogue -- re-derivation of what is finite or closed-form behind
achievable.py:34 'HAWKING / UNRUH flux  analogue-measured; same family.'

C1  acoustic metric (de Oliveira et al. 2106.03960 eq. B1, 1+1 part) ds^2 = W(x)^2[-(c^2-v^2)dt^2 - 2v dt dx + dx^2]:
    surface gravity of the Killing field d/dt at the sonic horizon c=v is |d(c-v)/dx| and does not depend on a
    regular conformal factor W  -> T_H = hbar*kappa/(2 pi k_B) is fixed by the flow profile (the quantity the analogue
    experiments test).
C2  Hawking area theorem hypothesis: A = 16 pi G^2 M^2/c^4 ; evaporation dM/dt<0 => dA/dt<0, which the area theorem
    forbids under the NEC -> the gravitational Hawking process REQUIRES an NEC-violating <T_ab> (the 'same family').
C3  Poincare invariance: the only symmetric T_ab invariant under all boosts and rotations is lambda*eta_ab.  With the
    flat-space vacuum renormalised to <T_ab>=0, every observer -- uniformly accelerated ones included -- measures
    T_ab u^a u^b = 0 in the Minkowski vacuum: the (eternal) Unruh effect carries no negative energy density.
C4  numbers: T_H(M_sun), T_Unruh(g), and the acceleration giving 1 K -- why neither gravitational case is measured.
"""
import sympy as sp, math, sys
ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name); ok = ok and bool(cond)

# ---------------- C1 acoustic surface gravity ----------------
t, x = sp.symbols('t x', real=True)
c = sp.Function('c')(x); v = sp.Function('v')(x); W = sp.Function('W')(x)
g = W**2*sp.Matrix([[-(c**2 - v**2), -v], [-v, 1]])
ginv = sp.simplify(g.inv())
X = [t, x]
def christ(g, ginv):
    G = [[[0]*2 for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for b in range(2):
            for d in range(2):
                G[a][b][d] = sp.simplify(sum(ginv[a, e]*(sp.diff(g[e, b], X[d]) + sp.diff(g[e, d], X[b]) - sp.diff(g[b, d], X[e]))
                                             for e in range(2))/2)
    return G
Gm = christ(g, ginv)
xi_up = [1, 0]
xi_dn = [sum(g[a, b]*xi_up[b] for b in range(2)) for a in range(2)]
# nabla_a xi_b = d_a xi_b - Gamma^e_{ab} xi_e
Dxi = sp.Matrix(2, 2, lambda a, b: sp.diff(xi_dn[b], X[a]) - sum(Gm[e][a][b]*xi_dn[e] for e in range(2)))
kappa2 = sp.simplify(-sp.Rational(1, 2)*sum(Dxi[a, b]*sum(ginv[a, cc]*ginv[b, dd]*Dxi[cc, dd] for cc in range(2) for dd in range(2))
                                           for a in range(2) for b in range(2)))
# evaluate at horizon: v = c there (substitute v -> c, keep derivatives distinct)
c0, v0, c1, v1, W0, W1 = sp.symbols('c0 v0 c1 v1 W0 W1', real=True)
subsd = {sp.Derivative(c, x): c1, sp.Derivative(v, x): v1, sp.Derivative(W, x): W1}
k2 = kappa2.subs(subsd).subs({c: c0, v: v0, W: W0})
k2h = sp.simplify(k2.subs(v0, c0))
print("kappa^2 at horizon (W regular):", sp.factor(k2h))
# Killing normalisation: xi^2 -> -W0^2 c0^2 ... at infinity; normalise by requiring kappa for flat-far-field W->1, c->c_inf.
# kappa computed w.r.t. lab time t; expected kappa^2 = (c1 - v1)^2 (units 1/s^2) independent of W0, W1.
chk("C1 kappa^2 = (dc/dx - dv/dx)^2 at c=v, independent of W and W'", sp.simplify(k2h - (c1 - v1)**2) == 0)

# vacuity guard: off the horizon the same expression is NOT (c1-v1)^2, so the pass above is not an identity
chk("C1 guard: off-horizon kappa^2 differs from (c1-v1)^2", sp.simplify(k2.subs({c0: 2, v0: 1}) - (c1 - v1)**2) != 0)
# ---------------- C2 area theorem ----------------
G_, M, cc_ = sp.symbols('G M c', positive=True)
Mt = sp.Function('M')(t)
A = 16*sp.pi*G_**2*Mt**2/cc_**4
dA = sp.diff(A, t)
chk("C2 dA/dt = 32 pi G^2 M dM/dt / c^4 (sign of dM/dt)", sp.simplify(dA - 32*sp.pi*G_**2*Mt*sp.diff(Mt, t)/cc_**4) == 0)
chk("C2 evaporation (dM/dt<0, M>0) => dA/dt<0 => area theorem's NEC hypothesis must fail",
    sp.simplify((32*sp.pi*G_**2*M*(-1)/cc_**4)) < 0)

# ---------------- C3 Poincare-invariant symmetric tensors ----------------
eta = sp.diag(-1, 1, 1, 1)
Ts = sp.symbols('T0:10')
T = sp.Matrix([[Ts[0], Ts[1], Ts[2], Ts[3]], [Ts[1], Ts[4], Ts[5], Ts[6]], [Ts[2], Ts[5], Ts[7], Ts[8]], [Ts[3], Ts[6], Ts[8], Ts[9]]])
gens = []
for i in range(1, 4):  # boosts K_i
    K = sp.zeros(4); K[0, i] = 1; K[i, 0] = 1; gens.append(K)
for (i, j) in [(1, 2), (1, 3), (2, 3)]:  # rotations
    J = sp.zeros(4); J[i, j] = -1; J[j, i] = 1; gens.append(J)
# infinitesimal invariance of covariant T_ab: L^T T + T L = 0 with L = generator acting on vectors; for lower indices use
# omega_a^c : (Lambda^{-1})^T T Lambda^{-1}; infinitesimally  -(L^T T + T L) = 0
eqs = []
for L in gens:
    Ll = eta*L*eta  # generator acting on covectors (lower indices) is -(eta L eta)^T; symmetric form below
    Lc = -(eta*L*eta.inv()).T
    eqs += list(Lc.T*T + T*Lc)
sol = sp.solve(eqs, Ts, dict=True)
Tsol = T.subs(sol[0])
lam = sp.Symbol('lam')
free = sorted(Tsol.free_symbols, key=str)
print("invariant symmetric tensors:", Tsol, "free:", free)
chk("C3 only lambda*eta_ab is boost+rotation invariant", len(free) == 1 and sp.simplify(Tsol - Tsol[1, 1]*eta) == sp.zeros(4))
# accelerated observer 4-velocity in Rindler: u = (cosh(a tau), sinh(a tau), 0, 0)
a, tau = sp.symbols('a tau', real=True)
u = sp.Matrix([sp.cosh(a*tau), sp.sinh(a*tau), 0, 0])
rho_obs = sp.simplify((u.T*(Tsol[1, 1]*eta)*u)[0])
print("rho seen by accelerated observer in invariant state:", rho_obs)
chk("C3 rho_accelerated = -lambda (the inertial value) ; lambda=0 (renormalised flat vacuum) => 0", sp.simplify(rho_obs + Tsol[1, 1]) == 0)

# ---------------- C4 numbers ----------------
hbar = 1.054571817e-34; kB = 1.380649e-23; cl = 299792458.0   # exact SI (2019) / derived
G = 6.67430e-11                                          # CODATA 2018 = CODATA 2022 value
GMsun = 1.32712440018e20                                 # IAU nominal heliocentric GM (m^3 s^-2)
Msun = GMsun/G
TH = hbar*cl**3/(8*math.pi*G*Msun*kB)
TU_g = hbar*9.80665/(2*math.pi*cl*kB)
a1K = 2*math.pi*cl*kB/hbar
print("T_H(M_sun) = %.4e K ; T_Unruh(g_n) = %.4e K ; a for T_U = 1 K : %.4e m/s^2" % (TH, TU_g, a1K))
chk("C4 T_H(M_sun) ~ 6.17e-8 K (<< CMB 2.7255 K: a solar-mass hole absorbs more than it emits)", abs(TH - 6.17e-8)/6.17e-8 < 0.01)
chk("C4 T_Unruh(g) ~ 3.97e-20 K", abs(TU_g - 3.97e-20)/3.97e-20 < 0.01)
# sensitivity: G's CODATA uncertainty (2.2e-5 rel) moves T_H by the same relative amount -- conclusion unaffected
G2 = G*(1+2.2e-5); TH2 = hbar*cl**3/(8*math.pi*G2*(GMsun/G2)*kB)
chk("C4 T_H(M_sun) depends on GM only (G cancels when M is fixed by GM)", abs(TH2 - TH)/TH < 1e-12)
print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
