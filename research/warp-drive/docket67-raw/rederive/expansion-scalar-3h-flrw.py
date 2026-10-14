#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for key expansion-scalar-3h-flrw.

Source (READ, page text): Ellis & van Elst, "Cosmological models", Cargese
lectures 1998, arXiv:gr-qc/9812046v5, eq.(11) Theta = tilde-nabla_a u^a "the
rate of volume expansion scalar of the fluid (with H = Theta/3 the Hubble
scalar)"; eq.(25) Sdot/S = Theta/3, "so the volume of a fluid element varies as
S^3"; eq.(104) FLRW metric in matter-comoving coordinates, u^a = delta^a_0,
Sdot/S = Theta/3.

Checks
  A  Theta = nabla_mu u^mu = 3 adot/a for u = d/dt in FLRW, k = +1, 0, -1.
  B  full 1+3 split of nabla_mu u_nu: acceleration, shear, vorticity vanish;
     trace = 3H (so Theta is the whole kinematics of the comoving flow).
  C  coordinate invariance: the same Theta in (i) conformal time, (ii) proper
     radius R = a r, (iii) a generic nonlinear coordinate map (numeric).
  D  Theta = d ln(volume)/dt along the flow; Theta = 0 <=> volume-preserving.
  E  CONGRUENCE DEPENDENCE (the hypothesis the tree must carry): de Sitter is
     flat FLRW with a = e^{Ht}; its static-patch Killing congruence has
     Theta = 0 exactly at the same events where the comoving one has 3H; a
     tilted congruence in matter-FLRW has Theta != 3H.  Changing u is a change
     of physical observer family, NOT a relabelling: Theta is a scalar of the
     pair (g, u).
  F  "three, exactly": in n spatial dimensions Theta = n H.
  G  numbers: 3 H0 for Planck 2018, Planck+BAO, DESI DR2+BBN, SH0ES R22.
"""
import sympy as sp
import math, random

ok_all = True
def rep(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print("  %-70s %s" % (label, "ok" if cond else "FAIL"))

t, chi, th, ph, c = sp.symbols('t chi theta phi c', positive=True)
a = sp.Function('a')(t)

def christoffel(g, X):
    n = len(X); gi = g.inv()
    return [[[sp.simplify(sum(gi[l, m]*(sp.diff(g[m, i], X[j]) + sp.diff(g[m, j], X[i])
              - sp.diff(g[i, j], X[m])) for m in range(n))/2) for j in range(n)]
             for i in range(n)] for l in range(n)]

def divergence(g, X, u):
    sg = sp.sqrt(-g.det())
    return sp.simplify(sum(sp.diff(sg*u[m], X[m]) for m in range(len(X)))/sg)

H = sp.diff(a, t)/a
print("A. Theta = 3H for the comoving congruence, k = +1, 0, -1")
for k, f in ((1, sp.sin(chi)), (0, chi), (-1, sp.sinh(chi))):
    X = [t, chi, th, ph]
    g = sp.diag(-c**2, a**2, a**2*f**2, a**2*f**2*sp.sin(th)**2)
    u = [1, 0, 0, 0]                                     # u.u = -c^2, t proper time
    Th = divergence(g, X, u)
    rep("k=%+d: nabla_mu u^mu - 3 adot/a = 0" % k, sp.simplify(Th - 3*H) == 0)

print("B. 1+3 split of nabla_mu u_nu (flat and closed)")
for k, f in ((0, chi), (1, sp.sin(chi))):
    X = [t, chi, th, ph]
    g = sp.diag(-c**2, a**2, a**2*f**2, a**2*f**2*sp.sin(th)**2)
    G = christoffel(g, X)
    uU = sp.Matrix([1, 0, 0, 0]); uL = g*uU
    Du = sp.Matrix(4, 4, lambda m, n_: sp.diff(uL[n_], X[m]) - sum(G[l][m][n_]*uL[l] for l in range(4)))
    acc = sp.simplify((uU.T*Du).T)                       # u^m nabla_m u_n
    hL = g + uL*uL.T/c**2
    hU = g.inv() + uU*uU.T/c**2
    tr = sp.simplify(sum(hU[m, n_]*Du[m, n_] for m in range(4) for n_ in range(4)))
    sym = sp.simplify((Du + Du.T)/2 + (uL*acc.T + acc*uL.T)/(2*c**2))
    shear = sp.simplify(sym - tr*hL/3)
    vort = sp.simplify((Du - Du.T)/2 + (uL*acc.T - acc*uL.T)/(2*c**2))
    rep("k=%+d: acceleration = 0" % k, acc == sp.zeros(4, 1))
    rep("k=%+d: shear = 0" % k, shear == sp.zeros(4, 4))
    rep("k=%+d: vorticity = 0" % k, vort == sp.zeros(4, 4))
    rep("k=%+d: trace h^mn nabla_m u_n = 3H" % k, sp.simplify(tr - 3*H) == 0)

print("C. coordinate invariance")
# (i) conformal time eta: dt = a d eta, u^eta = 1/a
eta = sp.symbols('eta', positive=True); b = sp.Function('b')(eta)   # b(eta) = a(t(eta))
X = [eta, chi, th, ph]
g = sp.diag(-c**2*b**2, b**2, b**2*chi**2, b**2*chi**2*sp.sin(th)**2)
Th = divergence(g, X, [1/b, 0, 0, 0])
rep("(i) conformal time: Theta = 3 b'/b^2 = 3 (da/dt)/a", sp.simplify(Th - 3*sp.diff(b, eta)/b**2) == 0)
# (ii) proper radius R = a(t) chi, flat
R = sp.symbols('R', positive=True)
X = [t, R, th, ph]
Hs = sp.Function('Hs')(t)            # H(t)
# chi = R/a -> d chi = dR/a - R H dt/a ; g = -c^2dt^2 + (dR - R H dt)^2 + R^2 dOmega^2
g = sp.Matrix([[-c**2 + R**2*Hs**2, -R*Hs, 0, 0], [-R*Hs, 1, 0, 0],
               [0, 0, R**2, 0], [0, 0, 0, R**2*sp.sin(th)**2]])
Th = divergence(g, X, [1, Hs*R, 0, 0])    # comoving observers: dR/dt = H R
rep("(ii) proper-radius coordinates: Theta = 3H", sp.simplify(Th - 3*Hs) == 0)
# (iii) generic nonlinear map (radial sector, angles untouched), a = t^(2/3)
tau, rho, eps = sp.symbols('tau rho epsilon', positive=True)
tt = tau + eps*rho**2*sp.cos(tau); rr = rho + eps*tau*rho**2
aa = lambda x: x**sp.Rational(2, 3)
J = sp.Matrix([[sp.diff(tt, tau), sp.diff(tt, rho)], [sp.diff(rr, tau), sp.diff(rr, rho)]])
g2 = sp.diag(-c**2, aa(tt)**2)
gp = sp.simplify(J.T*g2*J)
g4 = sp.diag(1, 1, aa(tt)**2*rr**2, aa(tt)**2*rr**2*sp.sin(th)**2)
g4[0:2, 0:2] = gp
up = J.inv()*sp.Matrix([1, 0])
Thp = divergence(g4, [tau, rho, th, ph], [up[0], up[1], 0, 0])
worst = 0.0
random.seed(67)
for _ in range(6):
    vals = {tau: random.uniform(1.0, 3.0), rho: random.uniform(0.1, 0.6), eps: 0.07,
            c: 1.0, th: 1.1}
    lhs = float(Thp.subs(vals)); tv = float(tt.subs(vals))
    worst = max(worst, abs(lhs - 3*(2/3)/tv)/(2/tv))
rep("(iii) nonlinear (t,r) -> (tau,rho): Theta' = 3H(t(tau,rho)), max rel err %.1e" % worst, worst < 1e-10)

print("D. Theta = d ln V/dt; zero iff volume-preserving")
f = chi
sqrt_h = a**3*f**2*sp.sin(th)
rep("(1/sqrt h) d sqrt(h)/dt = 3H  (volume of a fluid element ~ a^3)", sp.simplify(sp.diff(sqrt_h, t)/sqrt_h - 3*H) == 0)

print("E. congruence dependence -- the hypothesis the tree must name")
Hc = sp.symbols('H', positive=True); r = sp.symbols('r', positive=True)
# de Sitter as flat FLRW: a = exp(H t); static coordinates R = a r, T = t - ln(1 - H^2R^2/c^2)/(2H)
Rf = sp.exp(Hc*t)*r
Tf = t - sp.log(1 - Hc**2*Rf**2/c**2)/(2*Hc)
Jds = sp.Matrix([[sp.diff(Tf, t), sp.diff(Tf, r)], [sp.diff(Rf, t), sp.diff(Rf, r)]])
F = 1 - Hc**2*Rf**2/c**2
gstat = sp.diag(-F*c**2, 1/F)
pull = sp.simplify(Jds.T*gstat*Jds)
rep("static patch pulls back to -c^2dt^2 + e^{2Ht} dr^2 (same spacetime)",
    sp.simplify(pull - sp.diag(-c**2, sp.exp(2*Hc*t))) == sp.zeros(2, 2))
T_, R_ = sp.symbols('T R_', positive=True)
Fs = 1 - Hc**2*R_**2/c**2
gS = sp.diag(-Fs*c**2, 1/Fs, R_**2, R_**2*sp.sin(th)**2)
Th_K = divergence(gS, [T_, R_, th, ph], [1/sp.sqrt(Fs), 0, 0, 0])
rep("Killing (static) congruence in de Sitter: Theta = 0 exactly", sp.simplify(Th_K) == 0)
gdS = sp.diag(-c**2, sp.exp(2*Hc*t), sp.exp(2*Hc*t)*r**2, sp.exp(2*Hc*t)*r**2*sp.sin(th)**2)
Th_c = divergence(gdS, [t, r, th, ph], [1, 0, 0, 0])
rep("comoving congruence in the same de Sitter: Theta = 3H", sp.simplify(Th_c - 3*Hc) == 0)
# the Killing observer in FLRW coords: u = (dt/dT, dr/dT)/sqrt(F); compute its divergence in FLRW coords
Jinv = sp.simplify(Jds.inv())
uK = sp.simplify(Jinv*sp.Matrix([1/sp.sqrt(F), 0]))
Th_K2 = divergence(gdS, [t, r, th, ph], [uK[0], uK[1], 0, 0])
rep("same Killing congruence, evaluated in FLRW coordinates: Theta = 0", sp.simplify(Th_K2) == 0)
# tilted congruence in matter FLRW, a = t^(2/3): radial peculiar velocity v = V0 chi (proper), gamma
V0 = sp.symbols('V0', positive=True)
am = t**sp.Rational(2, 3)
gm = sp.diag(-c**2, am**2, am**2*chi**2, am**2*chi**2*sp.sin(th)**2)
v = V0*chi
gam = 1/sp.sqrt(1 - v**2/c**2)
Th_tilt = divergence(gm, [t, chi, th, ph], [gam, gam*v/am, 0, 0])
diff_at = sp.simplify(Th_tilt - 3*sp.Rational(2, 3)/t).subs({t: 2, chi: sp.Rational(1, 3), V0: sp.Rational(1, 10), c: 1})
rep("tilted congruence in matter FLRW: Theta - 3H != 0 (= %.4g at a test event)" % float(diff_at), abs(float(diff_at)) > 1e-3)

print("F. 'three, exactly': Theta = n H in n spatial dimensions")
for n in range(1, 6):
    xs = sp.symbols('x1:%d' % (n+1))
    X = [t] + list(xs)
    g = sp.diag(*([-c**2] + [a**2]*n))
    rep("n=%d: Theta = %d H" % (n, n), sp.simplify(divergence(g, X, [1] + [0]*n) - n*H) == 0)

print("G. numbers (km/s/Mpc -> 1/s, MPC as in cosmo.py)")
MPC = 3.0856775814913673e22
rows = (("Planck 2018 TT,TE,EE+lowE+lensing (tree's value)", 67.36, 0.54),
        ("Planck 2018 + BAO", 67.66, 0.42),
        ("DESI DR2 BAO + BBN", 68.51, 0.58),
        ("SH0ES R22", 73.04, 1.04))
for lab, h, s in rows:
    th3 = 3*h*1e3/MPC
    print("   %-52s theta = %.4e /s  (H0/sigma = %.0f)" % (lab, th3, h/s))
th_tree = 3*67.36e3/MPC
rep("tree's printed 6.549e-18 /s reproduced (%.6e)" % th_tree, abs(th_tree - 6.549e-18) < 5e-22)
rep("theta != 0 under every quoted H0 (min H0/sigma > 60)", min(h/s for _, h, s in rows) > 60)
spread = (3*73.04e3/MPC - th_tree)/th_tree
print("   printed value moves by %.1f%% across the Hubble tension; the sign/zero test does not" % (100*spread))

print("\nALL CHECKS %s" % ("PASS" if ok_all else "FAIL"))
raise SystemExit(0 if ok_all else 1)
