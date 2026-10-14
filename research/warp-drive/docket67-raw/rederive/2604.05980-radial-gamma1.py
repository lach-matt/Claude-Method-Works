"""DOCKET 67 audit: Pitre, Schneider & Poisson arXiv:2604.05980v1, Eqs (2.6),(2.7),(3.11)-(3.18), (10.16)-(10.17).
Re-derives, symbolically, (a) the statics, (b) the three forms of Gamma_1, (c) the turning-point criterion
dM/dsigma >= 0 <=> Gamma >= Gamma_1 from (3.13), (d) an INDEPENDENT dynamical criterion V''(R0) > 0 from the
junction condition with p = p(mu), converted by Eq (2.7), (e) the series (3.17), (f) the inversion (3.18),
(g) the Newtonian 3/2, (h) wall.py's two functions, imported read-only (no bytecode written).
Exits 1 on any failure."""
import sys, os, math
sys.dont_write_bytecode = True
import sympy as sp

FAIL = []
def ok(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAIL.append(name)

s, R, Gam, b2 = sp.symbols('s R Gamma beta2', positive=True)   # s = sqrt(F) = sqrt(1-2M/R), 0<s<1
C = (1 - s**2) / 2                                              # C = M/R
M = C * R
F = s**2

# (a) statics, Eqs (3.11),(3.12) vs wall.py statics (x = 2C, s = sqrt(1-x))
mu = (1 - sp.sqrt(F)) / (4 * sp.pi * R)
p = (sp.sqrt(F) - 1 + (M / R) / sp.sqrt(F)) / (8 * sp.pi * R)
mu_tree = (1 - s) / (4 * sp.pi * R)
p_tree = (1 - s)**2 / (16 * sp.pi * R * s)
ok("(3.11) mu == wall.statics sigma", sp.simplify(mu - mu_tree) == 0)
ok("(3.12) p == wall.statics p", sp.simplify(p - p_tree) == 0)
# Newtonian limits quoted under (3.12)
eps = sp.symbols('epsilon', positive=True)
ok("(3.12) Newtonian mu ~ M/(4 pi R^2)", sp.limit((mu / (M / (4*sp.pi*R**2))).subs(s, sp.sqrt(1-eps)), eps, 0) == 1)
ok("(3.12) Newtonian p ~ M^2/(16 pi R^3)", sp.limit((p / (M**2 / (16*sp.pi*R**3))).subs(s, sp.sqrt(1-eps)), eps, 0) == 1)

# (b) three forms of Gamma_1
q = sp.simplify(p / mu)
G1a = sp.Rational(3, 2) + 4*q + 4*q**2
G1b = (1 + 2*sp.sqrt(F) + 3*F) / (4*F)
Cs = sp.symbols('C', positive=True)
G1c_C = (4 - 6*Cs + 2*sp.sqrt(1 - 2*Cs)) / (4*(1 - 2*Cs))
G1c = G1c_C.subs(Cs, C)
ok("(3.16a) == (3.16b)", sp.simplify(G1a - G1b) == 0)
ok("(3.16b) == (3.16c)", sp.simplify(sp.powsimp(G1b - G1c, force=True).subs(sp.sqrt(s**2), s)) == 0)

# (3.13) inversion
mm, pp = sp.symbols('mu p', positive=True)
M13 = 4*pp**2/(sp.pi*mm**3) * (1 + 2*pp/mm) / (1 + 4*pp/mm)**3
R13 = pp/(sp.pi*mm**2) / (1 + 4*pp/mm)
ok("(3.13) M(mu,p) reproduces M", sp.simplify(M13.subs({mm: mu, pp: p}) - M) == 0)
ok("(3.13) R(mu,p) reproduces R", sp.simplify(R13.subs({mm: mu, pp: p}) - R) == 0)

# (c) turning point: dM/dsigma with dp = Gamma p/sigma dsigma, dmu = (mu+p)/sigma dsigma (Eqs 2.5, 2.6)
sig = sp.symbols('sigma', positive=True)
dMds = sp.diff(M13, pp) * Gam * pp / sig + sp.diff(M13, mm) * (mm + pp) / sig
Gzero = sp.solve(sp.Eq(dMds, 0), Gam)
qq = sp.symbols('q', positive=True)
ok("turning point: unique root in Gamma", len(Gzero) == 1)
Groot = sp.simplify(Gzero[0].subs(pp, qq*mm))
ok("turning point root == 3/2 + 4q + 4q^2  (3.16a)", sp.simplify(Groot - (sp.Rational(3,2) + 4*qq + 4*qq**2)) == 0)
coefG = sp.simplify(sp.diff(dMds, Gam).subs(pp, qq*mm))
ok("dM/dsigma increasing in Gamma (so >= 0 iff Gamma >= Gamma_1)", sp.simplify(coefG).is_positive is True
   or all(float(coefG.subs({qq: v, mm: 1.3, sig: 0.7})) > 0 for v in (1e-3, 0.1, 1, 10, 100)))

# (d) INDEPENDENT dynamical criterion.  sqrt(1+Rd^2) - sqrt(f+Rd^2) = 4 pi r mu(r), f = 1-2M/r (Israel, Minkowski in).
# => Rd^2 + V(r) = 0, V = 1 - (k/2 + M/(r k))^2, k = 4 pi r mu.  Conservation: mu' = -(2/r)(mu + p), p' = beta2 mu'.
r = sp.symbols('r', positive=True)
muf = sp.Function('mu')(r)
pf = sp.Function('P')(r)
k = 4*sp.pi*r*muf
V = 1 - (k/2 + M/(r*k))**2
d_mu = -(2/r)*(muf + pf)
d_p = b2 * d_mu
def D(expr):
    e = sp.diff(expr, r)
    return e.subs({sp.Derivative(muf, r): d_mu, sp.Derivative(pf, r): d_p})
V1 = D(V); V2 = D(V1)
at = {muf: mu, pf: p}
V0v = sp.simplify(V.subs(at).subs(r, R))
V1v = sp.simplify(V1.subs(at).subs(r, R))
ok("V(R0) = 0 at the static solution", sp.simplify(V0v) == 0)
ok("V'(R0) = 0 at the static solution", sp.simplify(V1v) == 0)
V2v = sp.simplify(V2.subs(at).subs(r, R))
b2sol = sp.solve(sp.Eq(V2v, 0), b2)
ok("V''(R0) linear in beta2 with one root", len(b2sol) == 1)
b2c = sp.simplify(b2sol[0])
b2_tree = (1 - s)*(3*s**2 + 2*s + 1) / (4*s**2*(1 + 3*s))
ok("independent beta2_crit == wall.beta2_crit (1-s)(3s^2+2s+1)/(4s^2(1+3s))", sp.simplify(b2c - b2_tree) == 0)
dV2 = sp.simplify(sp.diff(V2v, b2))
print("     dV''/dbeta2 at R0 =", sp.factor(dV2), "(positive => stable iff beta2 > beta2_crit)")
ok("dV''/dbeta2 > 0 for 0<s<1", all(float(dV2.subs({s: v, R: 1})) > 0 for v in (1e-3, .1, .5, .9, .999)))
# convert via Eq (2.7): Gamma = beta2 (mu+p)/p
Gdyn = sp.simplify(b2c * (mu + p) / p)
ok("Eq (2.7)-converted dynamical threshold == Gamma_1 identically in s  (not just at 6 points)",
   sp.simplify(Gdyn - G1b) == 0)
# LeMaitre-Poisson convention d ln p/d ln mu = beta2 mu/p  (their Eq 34 NOT READ; value printed only)
GLP = sp.factor(sp.simplify(b2c * mu / p))
print("     threshold in d ln p/d ln mu convention (footnote 1's Ref.[34] convention):", GLP)
print("       Newtonian limit of that:", sp.limit(GLP.subs(s, sp.sqrt(1-eps)), eps, 0))

# (e) series (3.17)
ser = sp.series(G1c_C, Cs, 0, 3).removeO()
ok("(3.17) Gamma_1 = 3/2 + C + 7/4 C^2 + O(C^3)", sp.simplify(ser - (sp.Rational(3,2) + Cs + sp.Rational(7,4)*Cs**2)) == 0)

# (f) inversion (3.18): F_min = ((1 + sqrt(4 G1 - 2))/(4 G1 - 3))^2
Fmin = ((1 + sp.sqrt(4*G1b - 2)) / (4*G1b - 3))**2
ok("(3.18) inverts (3.16b) on 0<s<1 (numeric, 9 points)",
   all(abs(float(Fmin.subs(s, v)) - v**2) < 1e-12 for v in (0.05, .1, .2, .3, .5, .7, .9, .95, .999)))

# (g) Newtonian (10.16)/(10.17): M = 4p^2/(pi G^2 sigma^3), R = p/(pi G sigma^2)
Gn = sp.symbols('G', positive=True)
Mn = 4*pp**2/(sp.pi*Gn**2*sig**3)
dMn = sp.diff(Mn, pp)*Gam*pp/sig + sp.diff(Mn, sig)
ok("Newtonian turning point at Gamma = 3/2", sp.solve(sp.Eq(dMn, 0), Gam) == [sp.Rational(3, 2)])

# (i) cross-check of the V'' side against a third, older published number: Brady-Louko-Poisson 1991 (NAMED-NOT-READ
# here; restated by Ishak & Lake gr-qc/0108058 as R/m+ ~ 2.37 at P'/sigma' = 1 with m- -> 0, per the sibling audit
# dust-shell-radial-instability-textbook.json).  beta2_crit = 1 <=> 15 s^3 + 3 s^2 - s - 1 = 0.
ok("beta2_crit = 1 <=> 15s^3+3s^2-s-1 = 0", sp.simplify(sp.numer(sp.together(b2_tree - 1)) + (15*s**3 + 3*s**2 - s - 1)) == 0
   or sp.simplify(sp.numer(sp.together(b2_tree - 1)) - (15*s**3 + 3*s**2 - s - 1)) == 0
   or sp.simplify(sp.factor(sp.numer(sp.together(b2_tree - 1))) / (15*s**3 + 3*s**2 - s - 1)).is_constant())
sr = [z for z in sp.Poly(15*s**3 + 3*s**2 - s - 1, s).nroots() if z.is_real and 0 < z < 1][0]
RM = 2 / (1 - sr**2)
print("     R/M at beta2_crit = 1: %.6f  (BLP 1991 via Ishak-Lake: ~2.37)" % RM)
ok("R/M at the causal boundary rounds to 2.37", abs(float(RM) - 2.37) < 0.005)

# (h) wall.py, imported read-only
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import importlib.util
spec = importlib.util.spec_from_file_location("wall_ro", "/home/user/Claude-Method-Works/research/warp-drive/wall.py")
w = importlib.util.module_from_spec(spec); spec.loader.exec_module(w)
import mpmath
mpmath.mp.dps = 40
def G1_exact(x):
    x = mpmath.mpf(x); Cc = x/2
    return (4 - 6*Cc + 2*mpmath.sqrt(1 - 2*Cc)) / (4*(1 - 2*Cc))
worst_pub = worst_crit = worst_pair = 0.0
grid = [10**(-6 + (6 + math.log10(0.8))*i/400) for i in range(401)] + [0.05, .2, .3, .5, .8] + [0.8*i/400 for i in range(1, 401)]
for x in grid:
    e = G1_exact(x)
    a = w.gamma1_published(x); b = w.gamma_crit(x)
    worst_pub = max(worst_pub, float(abs(a - e)/e))
    worst_crit = max(worst_crit, float(abs(b - e)/e))
    worst_pair = max(worst_pair, abs(a - b)/a)
print("     wall.gamma1_published vs 40-digit (3.16c): max rel err %.2e over %d x in [1e-6, 0.8]" % (worst_pub, len(grid)))
print("     wall.gamma_crit       vs 40-digit (3.16c): max rel err %.2e" % worst_crit)
print("     wall pair |pub - crit|/pub:               max %.2e  (wall.py:113 claims 1e-15)" % worst_pair)
ok("wall.gamma1_published is (3.16c) with C = x/2 to < 1e-13", worst_pub < 1e-13)
# The tree's SENTENCE (wall.py:113) says "agree to 1e-15 at every x from 1e-6 to 0.8".  The identity is exact
# (sympy above); the double-precision gamma_crit is not, because wall.statics forms (1 - s) naively -- the
# cancellation wall.one_minus_s exists to avoid.  Recorded as a DISCREPANCY in the tree's numeric sentence, not a
# fault in the source and not a failure of the criterion.
print("     DISCREPANCY (tree sentence, not source): gamma_crit float error reaches %.1e at small x, not 1e-15" % worst_crit)
def gamma_crit_stable(x):
    s_ = math.sqrt(1.0 - x); oms = w.one_minus_s(x)
    sg = oms / (4*math.pi); pp_ = oms**2 / (16*math.pi*s_)
    return w.beta2_crit(x) * (sg + pp_) / pp_
worst_st = max(float(abs(gamma_crit_stable(x) - G1_exact(x))/G1_exact(x)) for x in grid)
print("     same conversion with (1-s) formed as x/(1+s): max rel err %.2e" % worst_st)
ok("cause identified: the loss is the naive (1-s) in wall.statics (stable form < 1e-14)", worst_st < 1e-14)
ok("tree's own selftest tolerance 1e-9 at its six points is met", all(abs(w.gamma_crit(x) - w.gamma1_published(x)) < 1e-9 for x in (1e-6, .05, .2, .3, .5, .8)))
ok("tree's Newtonian check gamma_crit(1e-9) = 1.5 within 1e-6 is met", abs(w.gamma_crit(1e-9) - 1.5) < 1e-6)
print("     observed: gamma_crit(1e-12) = %.12f (naive-(1-s) error %.1e); gamma1_published(1e-12) = %.15f"
      % (w.gamma_crit(1e-12), abs(w.gamma_crit(1e-12) - 1.5)/1.5, w.gamma1_published(1e-12)))
print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS")
sys.exit(1 if FAIL else 0)
