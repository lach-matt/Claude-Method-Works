"""DOCKET 67 audit: Pitre, Schneider & Poisson, arXiv:2604.05980v1 (7 Apr 2026),
"Self-gravitating thin shells are dynamically unstable on all angular scales".

Independent re-derivation of the NEWTONIAN non-radial normal modes of a static,
self-gravitating, infinitesimally thin, barotropic perfect-fluid shell (vacuum inside
and outside), the model of their Sec. X.  Units G = M = R = 1 (rates in sqrt(GM/R^3)).

Derivation (this file, not copied): Lagrangian displacement xi = R h Y r_hat + R grad(j Y)
(even parity).  Continuity: Delta sigma/sigma = -(2h - l(l+1) j) Y.  Barotropic:
Delta p = Gamma p Delta sigma/sigma.  Equilibrium p = G M sigma/(4R) (their (10.15)).
Extrinsic-curvature perturbation Delta K / K = (l-1)(l+2) h Y / 2 (their (10.23)).
Membrane force per area: + p K n - grad_s p, n = r_hat - grad_Omega(h Y).
Self-gravity: multipoles of the displaced shell, field AVERAGED over the two faces
(the theta-hat component of the field is discontinuous across a tilted surface).

Checks against the PRINTED paper (pages read: 1-4, 6-7, 9, 23, 37, 41, 47 of v1):
  (a) l = 0 : lambda = Gamma - 3/2                         (Sec. X H, p.41)
  (b) l = 1 : lambda_+ = (3 Gamma - 4)/2, lambda_- = 0, zero mode j = h   (10.57)
  (c) the h-row combination (2l+1)(Gamma - w^2) - (2l^3 - l^2 + 9l + 6)/4  (10.52b)
  (d) the denominator (2l+1) Gamma - 2(l+1)                                (10.52b)
  (e) the mass-multipole coefficient 2(l+2)Gamma - 4 w^2 - (l^2+l+6)       (10.54)
Then:
  (f) PROOF (sympy + z3) that for EVERY real l >= 2 and EVERY Gamma > 0 one eigenvalue
      of the restoring matrix is negative -> exponentially growing mode (Newtonian).
  (g) the growth rate kappa_l(Gamma): depends on Gamma (so on beta^2) and GROWS with l,
      kappa_l ~ l/2 as l -> infinity (unbounded for an infinitely thin shell).
  (h) wall.py's density-ceiling numbers recomputed with k = 0.6 (tree), with the
      Newtonian l = 2 value, and with higher l.
Exits 1 on any failure.
"""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp

FAIL = []
def ok(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)

l, G = sp.symbols('ell Gamma', positive=True)
h, j, lam = sp.symbols('h j lam')

sig0 = 1 / (4 * sp.pi)          # M/(4 pi R^2)
p_over_sig = sp.Rational(1, 4)  # G M/(4R)
K0 = 2                          # 2/R
# perturbed potential coefficients at r = R (exterior A, interior B)
A = -4 * sp.pi * sig0 * (l * (l + 1) * j + l * h) / (2 * l + 1)
B = -4 * sp.pi * sig0 * (l * (l + 1) * j - (l + 1) * h) / (2 * l + 1)
ok("potential continuous across displaced surface: B - A = G M h / R", sp.simplify(B - A - h) == 0)

dsig = -(2 * h - l * (l + 1) * j)                     # Delta sigma / sigma
# radial acceleration (per unit mass, coefficient of Y)
g_r = sp.Rational(1, 2) * (2 * h + (l + 1) * A - l * B)
memb_r = p_over_sig * K0 * ((G - 1) * dsig + sp.Rational(1, 2) * (l - 1) * (l + 2) * h)
hdd = g_r + memb_r
# tangential acceleration (coefficient of grad_Omega Y)
g_t = -(A + B) / 2
memb_t = p_over_sig * (-K0 * h - G * dsig)
jdd = g_t + memb_t

Lm = -sp.Matrix([[sp.diff(hdd, h), sp.diff(hdd, j)], [sp.diff(jdd, h), sp.diff(jdd, j)]])
Lm = sp.simplify(Lm)
print("restoring matrix L (x'' = -L x, x = (h, j)):")
sp.pprint(Lm)
cp = sp.factor((Lm - lam * sp.eye(2)).det())
tr = sp.factor(Lm.trace()); dt = sp.factor(Lm.det())
print("trace =", tr); print("det   =", dt)

# (a) l = 0: only the radial row, j absent
lam0 = sp.simplify(Lm[0, 0].subs(l, 0))
ok("(a) l=0 radial eigenvalue = Gamma - 3/2 (paper p.41)", sp.simplify(lam0 - (G - sp.Rational(3, 2))) == 0)
# (b) l = 1
ev1 = sp.solve(cp.subs(l, 1), lam)
ok("(b) l=1 eigenvalues {0, (3Gamma-4)/2} (10.57)",
   set(sp.simplify(e) for e in ev1) == {0, sp.simplify((3 * G - 4) / 2)})
ok("(b) l=1 zero mode is j = h (translation, paper p.41)",
   sp.simplify((Lm.subs(l, 1) * sp.Matrix([1, 1])).norm()) == 0)
# (c) h-row: (2l+1)(L11 - lam) == (2l+1)(Gamma - lam) - (2l^3 - l^2 + 9l + 6)/4
ok("(c) (10.52b) combination reproduced",
   sp.simplify((2 * l + 1) * (Lm[0, 0] - lam) - ((2 * l + 1) * (G - lam) - (2 * l**3 - l**2 + 9 * l + 6) / 4)) == 0)
# (d) denominator
ok("(d) (10.52b) denominator (2l+1)Gamma - 2(l+1) = -2(2l+1) L12/(l(l+1))",
   sp.simplify(-2 * (2 * l + 1) * Lm[0, 1] / (l * (l + 1)) - ((2 * l + 1) * G - 2 * (l + 1))) == 0)
# (e) mass multipole of an eigenvector (h, j) ~ (-L12, L11 - lam): q ~ l h + l(l+1) j
q = -l * Lm[0, 1] + l * (l + 1) * (Lm[0, 0] - lam)
target = l * (l + 1) / (2 * l + 1) * (2 * l + 1) / 4 * (2 * (l + 2) * G - 4 * lam - (l**2 + l + 6))
ok("(e) (10.54) mass-multipole coefficient reproduced", sp.simplify(q - target) == 0)

# (f) instability for all l >= 2, Gamma > 0: stable requires det > 0 AND trace > 0
detpoly = sp.factor(dt * 16 * (2 * l + 1))
print("16(2l+1) det =", detpoly)
try:
    import z3
    Lz, Gz = z3.Reals('l G')
    trz = (Gz * Lz**2 + Gz * Lz + 4 * Gz - Lz**2 - Lz - 6) / 4
    detz = -Lz * (Lz - 1) * (Lz + 1) * (2 * Gz * Lz**2 + Gz * Lz - 6 * Gz - 4 * Lz + 8)
    ok("trace matches z3 encoding", sp.simplify(tr - (G * l**2 + G * l + 4 * G - l**2 - l - 6) / 4) == 0)
    ok("det matches z3 encoding", sp.simplify(detpoly - (-l * (l - 1) * (l + 1) * (2 * G * l**2 + G * l - 6 * G - 4 * l + 8))) == 0)
    s = z3.Solver()
    s.add(Lz >= 2, Gz > 0, detz >= 0, trz >= 0)   # both eigenvalues >= 0 (no growing mode)
    r = s.check()
    ok("(f) z3: NO (l >= 2 real, Gamma > 0) with both eigenvalues >= 0  [%s]" % r, r == z3.unsat)
    # vacuity guard: the encoding is satisfiable at l = 1 (stable-or-marginal exists)
    s2 = z3.Solver(); s2.add(Lz == 1, Gz == 2, detz >= 0, trz >= 0)
    ok("(f) vacuity guard: l = 1, Gamma = 2 admits no growing mode (sat)", s2.check() == z3.sat)
    s3 = z3.Solver(); s3.add(Lz == 0, Gz == 2, detz >= 0, trz >= 0)
    ok("(f) vacuity guard: encoding not trivially unsat (l=0, Gamma=2: det=0, trace=1/2, sat)", s3.check() == z3.sat)
except ImportError:
    ok("z3 available", False)

# (g) growth rates
def kappa(ll, g):
    ev = [complex(sp.N(e)) for e in Lm.subs({l: ll, G: g}).eigenvals()]
    neg = [e.real for e in ev if e.real < 0]
    return math.sqrt(-min(neg)) if neg else 0.0
print("\nkappa_l(Gamma) in sqrt(GM/R^3), Newtonian:")
print("  l   G=1.5    G=1.8    G=2.0    G=2.4    G=3.0    G=10")
tab = {}
for ll in (2, 3, 4, 5, 10, 20, 100):
    row = [kappa(ll, sp.nsimplify(g)) for g in (1.5, 1.8, 2.0, 2.4, 3.0, 10)]
    tab[ll] = row
    print("  %-3d " % ll + " ".join("%8.4f" % v for v in row))
k22 = kappa(2, 2)
ok("(g) l=2, Gamma=2 Newtonian rate = %.4f (paper Fig.1 left axis spans 0.52-0.66 over M/R in [0,0.3])" % k22,
   0.5 < k22 < 0.53)
ok("(g) rate depends on Gamma: kappa_2(1.8) != kappa_2(2.4)", abs(kappa(2, sp.Rational(9, 5)) - kappa(2, sp.Rational(12, 5))) > 0.05)
ok("(g) rate grows with l: kappa_3 > 2 kappa_2 at Gamma=2", kappa(3, 2) > 2 * k22)
lamm = sp.solve(cp, lam)
asym = [sp.simplify(sp.limit(e / l**2, l, sp.oo).subs(sp.sqrt(G**2 + 2*G + 1), G + 1)) for e in lamm]
print("  lambda_+-/l^2 as l -> oo:", asym)
ok("(g) eikonal: lambda_- ~ -l^2/4, kappa ~ l/2 (pressure-driven buckling, Gamma-free at leading order)",
   sp.Rational(-1, 4) in [sp.simplify(a) for a in asym])

# Gamma -> infinity (infinitely stiff matter): the l >= 2 growing mode survives with a finite rate
lam_inf = sp.limit(dt / tr, G, sp.oo)   # smaller root ~ det/trace when trace -> oo
print("  lambda_-(Gamma -> oo) =", sp.factor(lam_inf))
k2inf = math.sqrt(-float(lam_inf.subs(l, 2)))
ok("(g) stiff limit Gamma -> oo: l=2 rate -> %.4f > 0 (stiffening slows, never removes)" % k2inf,
   abs(k2inf - math.sqrt(0.12)) < 1e-12)
ok("(g) lambda_-(Gamma -> oo) < 0 for l = 2..50", all(lam_inf.subs(l, n) < 0 for n in range(2, 51)))

# (h) wall.py numbers
c = 299792458.0; Gsi = 6.67430e-11; a = 9.80665; de = 0.2
def rho_ceiling(k): return 3 * a**2 / (4 * math.pi * Gsi * (k * c * de)**2)
def rmin(Mkg, k, n=1.0): return (Gsi * Mkg * (k * c * de / (n * a))**2) ** (1 / 3)
r06 = rho_ceiling(0.6)
ok("(h) tree's ceiling 2.658e-4 kg/m^3 reproduced with k=0.6 (%.4e)" % r06, abs(r06 - 2.658e-4) / 2.658e-4 < 1e-3)
ok("(h) tree's R > 965 m (1000 t, N<1) with k=0.6 (%.1f m)" % rmin(1e6, 0.6), abs(rmin(1e6, 0.6) - 965) < 1)
ok("(h) tree's R > 4.48 km (N<0.1) with k=0.6 (%.1f m)" % rmin(1e6, 0.6, 0.1), abs(rmin(1e6, 0.6, 0.1) - 4480) < 5)
print("\n  k used                 rho_ceiling(kg/m^3)  R_min(1000 t, N<1)")
for lab, k in (("tree 0.6", 0.6), ("Newt l=2 G=2", k22), ("Newt l=3 G=2", kappa(3, 2)),
               ("Newt l=10 G=2", kappa(10, 2)), ("Newt l=100 G=2", kappa(100, 2))):
    print("  %-22s %.4e          %.1f m" % (lab, rho_ceiling(k), rmin(1e6, k)))
print("  ceiling scales as 1/k_max^2; with an infinitely thin shell k_max ~ l_max/2 is unbounded,")
print("  so the ceiling is set by whatever cuts off l (thickness, rigidity) -- not in the paper.")

print("\nRESULT:", "ALL PASS" if not FAIL else "FAILURES: %s" % FAIL)
sys.exit(1 if FAIL else 0)
