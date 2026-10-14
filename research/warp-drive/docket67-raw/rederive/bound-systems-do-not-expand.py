#!/usr/bin/env python3
"""DOCKET 67 -- audit: bound-systems-do-not-expand (permute.py:60-66, 243-245, 425-426, 534-536).

Re-derives, with sympy, what the tree hardcodes as bohr_radius_contains_a() = False:
  A. the tidal (geodesic-deviation) acceleration of flat FLRW in a comoving orthonormal
     frame -- the only way expansion reaches a local system at Newtonian order;
  B. the classical circular-orbit shift it causes (Coulomb and Kepler);
  C. the quantum first-order shift of <r> in hydrogen 1s (Dalgarno-Lewis, exact);
  D. the numbers today and at recombination (Planck 2018 H0, Omega_Lambda; CODATA a0, alpha);
  E. the same for the Earth's orbit and for galaxy/cluster-mass systems, plus the
     Schwarzschild-de Sitter force-balance radius that limits 'bound';
  F. sensitivity of the tree's ratio 1090.92 to a variation of m_e or alpha;
  G. a tree-internal check: permute.ratio_from_temperature is 1+z by construction.
Exit 0 iff every assertion holds.  stdlib + sympy only.
"""
import sympy as sp, math, sys

ok = True
def check(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + detail) if detail else ""))

# ---------------------------------------------------------------- A. FLRW tidal tensor
t, x, y, z = sp.symbols('t x y z', real=True)
a = sp.Function('a')(t)
X = [t, x, y, z]
g = sp.diag(-1, a**2, a**2, a**2)
gi = g.inv()
Gam = [[[sum(gi[l, m]*(sp.diff(g[m, i], X[j]) + sp.diff(g[m, j], X[i]) - sp.diff(g[i, j], X[m]))
             for m in range(4))/2 for j in range(4)] for i in range(4)] for l in range(4)]
def Riem(r, s, m, n):   # R^r_{s m n}
    e = sp.diff(Gam[r][n][s], X[m]) - sp.diff(Gam[r][m][s], X[n])
    e += sum(Gam[r][m][l]*Gam[l][n][s] - Gam[r][n][l]*Gam[l][m][s] for l in range(4))
    return sp.simplify(e)
# geodesic deviation for comoving observer u = d/dt:  D^2 xi^i/dtau^2 = -R^i_{t j t} xi^j
tidal = sp.Matrix(3, 3, lambda i, j: sp.simplify(-Riem(i+1, 0, j+1, 0)))
# convert coordinate xi^j to physical (orthonormal) components: xi_hat = a xi  -> same matrix (diagonal)
addot_over_a = sp.diff(a, t, 2)/a
check("A1 tidal matrix = (a''/a) * identity (orthonormal comoving frame)",
      sp.simplify(tidal - addot_over_a*sp.eye(3)) == sp.zeros(3, 3), "d2xi/dtau2 = (a''/a) xi")
# does it depend on a or a' separately?  substitute a -> lam*a (a rescaling of a): invariant
lam = sp.symbols('lam', positive=True)
check("A2 tidal term invariant under a -> lam*a (it carries no scale factor, only a''/a)",
      sp.simplify(addot_over_a.subs(a, lam*a).doit() - addot_over_a) == 0)
# a de Sitter a = exp(H t) gives a''/a = H^2 constant in time
H = sp.symbols('H', positive=True)
check("A3 de Sitter: a''/a = H^2, time independent",
      sp.simplify(addot_over_a.subs(a, sp.exp(H*t)).doit()) == H**2)
# matter-dominated a = t^(2/3): a''/a = -2/(9 t^2) = -H^2/2 (deceleration)
check("A4 matter era: a''/a = -H^2/2 (H = 2/(3t))",
      sp.simplify(addot_over_a.subs(a, t**sp.Rational(2, 3)).doit() + (sp.Rational(2, 3)/t)**2/2) == 0)

# ---------------------------------------------------------------- B. classical circular orbit
r, L, m, K, q, d = sp.symbols('r L m K q delta', real=True)
# radial force balance at fixed angular momentum L:  L^2/(m r^3) = K/r^2 - m q r ,  q = a''/a
r0 = L**2/(m*K)
eq = sp.expand((L**2/(m*r**3) - K/r**2 + m*q*r).subs(r, r0*(1 + d)))
d1 = sp.solve(sp.series(eq, d, 0, 2).removeO().subs(q, q), d)[0]
d1 = sp.simplify(sp.series(d1, q, 0, 2).removeO())
check("B1 first-order shift delta = m q r0^3 / K (outward for q>0)",
      sp.simplify(d1 - m*q*r0**3/K) == 0, "delta = %s" % sp.simplify(d1.subs(L**2, m*K*r)))

# ---------------------------------------------------------------- C. quantum 1s, Dalgarno-Lewis (atomic units)
rr = sp.symbols('r', positive=True)
psi0 = sp.exp(-rr)/sp.sqrt(sp.pi)
def expv(f):  # <1s| f(r) |1s>
    return sp.integrate(4*sp.pi*rr**2*psi0**2*f, (rr, 0, sp.oo))
r2 = expv(rr**2); rm = expv(rr)
check("C0 <r^2>_1s = 3 a0^2, <r>_1s = 3/2 a0", r2 == 3 and rm == sp.Rational(3, 2))
# perturbation V = lam * r^2 (lam = -m q /2 in physical units). Solve (H0-E0) (F psi0) = -(V-<V>) psi0
A_, B_, C_ = sp.symbols('A B C')
F = A_*rr**3 + B_*rr**2 + C_*rr
# (H0-E0)(F psi0) = -(1/2)(F'' + 2F'/r) psi0 - F' psi0' ; psi0'=-psi0
lhs = -sp.Rational(1, 2)*(sp.diff(F, rr, 2) + 2*sp.diff(F, rr)/rr) + sp.diff(F, rr)
sol = sp.solve(sp.Poly(sp.expand(rr*(lhs + (rr**2 - r2))), rr).coeffs(), [A_, B_, C_], dict=True)[0]
Fs = F.subs(sol)
# orthogonalise psi1 = (F - <F>) psi0 ; delta<r> = 2 <(F-<F>) r>
dr_per_lam = sp.simplify(2*(expv(Fs*rr) - expv(Fs)*rm))
print("     Dalgarno-Lewis F(r) =", sp.expand(Fs), " ; d<r>/d(lam) =", dr_per_lam, "a0 per (E_h/a0^2)")
# physical: lam = -m q/2 in units E_h/a0^2 ->  lam_au = -(1/2) q a0^2 * m / (E_h) ... E_h = m alpha^2 c^2
# so lam_au = -(1/2) q a0^2/(alpha^2 c^2) and delta<r>/<r> = dr_per_lam*lam_au/(3/2)
coef_q = sp.simplify(dr_per_lam*(-sp.Rational(1, 2))/sp.Rational(3, 2))
print("     => delta<r>/<r> = %s * (a''/a) a0^2/(alpha c)^2" % coef_q)
check("C1 quantum shift has the classical sign (outward for a''/a > 0) and order-unity coefficient",
      coef_q > 0 and 1 <= coef_q <= 10, "coefficient %s" % coef_q)

# ---------------------------------------------------------------- D. numbers
c = 299792458.0; hbar = 1.054571817e-34; kB = 1.380649e-23
a0 = 5.29177210544e-11           # CODATA 2022 (sibling audit codata-2018-constants.json)
alpha = 7.2973525643e-3          # CODATA 2022
Mpc = 3.0856775814913673e22
T0 = 2.7255                      # permute.py:178 (Fixsen 2009)
zrec = 1089.92                   # permute.py:179 (Planck 2018)
G = 6.67430e-11
cases = {"Planck2018 TT,TE,EE+lowE+lensing": (67.36, 0.6847),
         "Planck2018 +BAO": (67.66, 0.6889),
         "local-ladder-like H0 = 73 (illustrative, NOT READ)": (73.0, 0.6847)}
rho_g = (math.pi**2/15)*(kB*T0)**4/(hbar*c)**3/c**2          # kg/m^3 photons
Neff = 3.046
rho_r = rho_g*(1 + Neff*(7/8)*(4/11)**(4/3))
qcoef = float(coef_q)
res = {}
for name, (h0, OL) in cases.items():
    H0 = h0*1e3/Mpc
    rho_c = 3*H0**2/(8*math.pi*G)
    Or = rho_r/rho_c; Om = 1 - OL - Or
    qa_now = H0**2*(OL - Om/2 - Or)
    zz = 1 + zrec
    qa_rec = H0**2*(OL - Om*zz**3/2 - Or*zz**4)
    d_now = qcoef*qa_now*a0**2/(alpha*c)**2
    d_rec = qcoef*qa_rec*a0**2/(alpha*c)**2
    res[name] = (d_now, d_rec)
    print("     %-48s a''/a now %.3e s^-2, at z_rec %.3e s^-2; delta a_B/a_B now %.2e, at rec %.2e"
          % (name, qa_now, qa_rec, d_now, d_rec))
dmax = max(abs(v) for pair in res.values() for v in pair)
check("D1 |delta a_B / a_B| < 1e-55 at every epoch and every H0 used", dmax < 1e-55, "max %.2e" % dmax)
drift = max(abs(dn - dr) for dn, dr in res.values())
ratio_err = drift*(1 + zrec)
check("D2 the atomic-scale drift since recombination moves the tree's 1090.92 by < 1e-50",
      ratio_err < 1e-50, "absolute shift in the ratio %.2e" % ratio_err)

# ---------------------------------------------------------------- E. gravitating systems
Msun = 1.98847e30; AU = 1.495978707e11; kpc = Mpc/1e3
H0 = 67.36e3/Mpc; OL = 0.6847
qa_now = H0**2*(OL - (1 - OL)/2)
Lam = 3*OL*H0**2/c**2
systems = [("Earth orbit", Msun, AU),
           ("galaxy-mass 1e12 Msun at 100 kpc (ILLUSTRATIVE mass/radius, not READ)", 1e12*Msun, 100*kpc),
           ("cluster-mass 1e15 Msun at 2 Mpc (ILLUSTRATIVE mass/radius, not READ)", 1e15*Msun, 2*Mpc)]
for name, M, R in systems:
    dd = qa_now*R**3/(G*M)
    rL = (3*G*M/(Lam*c**2))**(1/3)
    print("     %-72s delta R/R = %.2e ; SdS force-balance radius (3GM/Lambda c^2)^(1/3) = %.3g Mpc (R/r_L = %.3g)"
          % (name, dd, rL/Mpc, R/rL))
dE = qa_now*AU**3/(G*Msun)
check("E1 Earth orbit shift < 1e-20", dE < 1e-20, "%.2e" % dE)
dC = qa_now*(2*Mpc)**3/(G*1e15*Msun)
check("E2 at cluster scale the shift is small but NOT negligible to 1e-6 -- the qualifier 'bound' does work",
      1e-4 < dC < 1e-1, "%.2e" % dC)

# ---------------------------------------------------------------- F. varying constants
dm, da = sp.symbols('dm da')

ratio_rec_to_now = (1 + sp.Symbol('z'))*(1/(1 + dm))*(1/(1 + da))   # a_B ~ 1/(m_e alpha)
lin = sp.series(sp.series(ratio_rec_to_now, dm, 0, 2).removeO(), da, 0, 2).removeO()
print("     cosmic/atomic ratio growth with a_B,rec/a_B,0 = 1/((1+dm)(1+da)):", sp.simplify(lin))
for frac in (0.01, 0.10):
    val = (1 + zrec)/(1 + frac)
    print("     a %2.0f%% larger m_e*alpha at recombination -> growth %.1f instead of %.2f" % (100*frac, val, 1 + zrec))
check("F1 the ratio stays O(10^3) for any |d(m_e alpha)/(m_e alpha)| <= 10%",
      (1 + zrec)/1.1 > 900 and (1 + zrec)/0.9 < 1300)

# ---------------------------------------------------------------- G. tree-internal: tautology
zs, T0s = sp.symbols('z T0', positive=True)
temperature_at = T0s*(1 + zs)                       # permute.py:234-235
ratio_from_temperature = temperature_at/T0s         # permute.py:238-240
check("G1 permute.ratio_from_temperature == 1+z identically (not an independent measurement)",
      sp.simplify(ratio_from_temperature - (1 + zs)) == 0,
      "T_rec = %.1f K is computed from Z_REC, not measured" % (T0*(1 + zrec)))

# ---------------------------------------------------------------- H. metastability of the inverted term
qa = H0**2*OL
rb = (a0**3/((qcoef/qcoef)*qa*a0**2/(alpha*c)**2))**(1/3)   # K/r^2 = m q r  -> r^3 = K/(m q) = a0^3/(q a0^2/(alpha c)^2)
print("     Coulomb = tidal balance radius for hydrogen under de Sitter asymptote: %.2e m (%.1e a0)" % (rb, rb/a0))
check("H1 the barrier sits > 1e20 a0 out: tunnelling through it is irrelevant", rb/a0 > 1e20)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
