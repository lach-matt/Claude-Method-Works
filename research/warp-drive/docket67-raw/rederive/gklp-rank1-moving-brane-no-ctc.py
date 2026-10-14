#!/usr/bin/env python3
"""
DOCKET 67 -- independent re-derivation for key gklp-rank1-moving-brane-no-ctc.

Source read at alphaXiv: Greene, Kabat, Levin, Porrati, "Back to the Future:
Causality on a Moving Braneworld", arXiv:2208.09014v3 (PRD 107, 025016, 2023),
and its predecessor Greene, Kabat, Levin, Menon arXiv:2206.13590v2 (PRD 106,
085001, 2022).  Does NOT import the owner (latticectc.py); recomputes from the
papers' own equations.

  A. identification vector (GKLP eq. 6/8, eq. 10) is spacelike, norm (2 pi R)^2,
     for every |beta| < 1 and every observer boost B (sympy); owner's
     parametrisation xi = (-3/4, 0, 0, 5/4), |xi|^2 = 1 at beta = 3/5 (exact).
  B. GKLP algebra: eq. 17 sin^2 alpha, tan alpha = Gamma gamma beta, eq. 20 = eq. 22
     at cos(theta)=1 (eqs. 23-24), eq. 28 v_eff = gamma (1 + Gamma^2 B^2 beta^2),
     eq. 32 around-the-brane-circle time (sympy).
  C. v and w (eqs. 20, 25) re-derived INDEPENDENTLY from the bulk quotient
     geometry: earliest arrival on the brane axis = min over winding of
     n xi_t + |X - n xi_s| (numeric, continuous-winding asymptote).
  D. Round trip T > 0 for every integer winding pair, every D, every B including
     supercritical (exact-ish numeric over integer windings) -- and the general
     reason, machine-checked in z3: n xi_t + |n| |xi_s| > 0 for n != 0 when xi is
     spacelike (triangle inequality closes the argument).
  E. Rank-1 statement itself: m^2 |xi|^2 > 0, no nonzero causal multiple (z3),
     and a K-leg future-causal chain summing to m xi is impossible (z3 per m at
     K=1,2; every K via Lagrange identity (sympy) + scalar lemma (z3)).
  F. GKLP's rank-2 example (eq. 29, brane circle L') is the owner's spacelike-span
     rank-2 case: Gram positive definite (sympy).
  G. Cross-check: Polychronakos 2210.11497 eq. 2.4 periodicity vector has norm R^2.
"""
import math
from fractions import Fraction as Fr
import sympy as sp
import z3

ok_all = True
def chk(label, got, want):
    global ok_all
    good = (got == want)
    ok_all &= good
    print(("  [ok] " if good else "  [FAIL] ") + label + " -> " + str(got))

def nrm(v):  # signature (-,+,+,...)
    return -v[0] ** 2 + sum(c ** 2 for c in v[1:])

print("A. IDENTIFICATION VECTOR")
b, B, L, Lp = sp.symbols('beta B L Lp', real=True)
g = 1 / sp.sqrt(1 - b ** 2); G = 1 / sp.sqrt(1 - B ** 2)
xi_brane = (-g * b * L, 0, g * L)                    # eq. 6/8, (t', x', z')
xi_obs = (-G * g * b * L, G * B * g * b * L, g * L)  # eq. 10, (t'', x'', z'')
chk("eq. 8 |xi|^2 == L^2 (all |beta|<1)", sp.simplify(nrm(xi_brane) - L ** 2), 0)
chk("eq. 10 |xi''|^2 == L^2 (all |beta|,|B|<1)", sp.simplify(nrm(xi_obs) - L ** 2), 0)
beta = Fr(3, 5); gam = Fr(5, 4)
xi_owner = (-gam * beta, Fr(0), Fr(0), gam)
chk("owner xi at beta=3/5, 2piR=1 == (-3/4,0,0,5/4)", xi_owner, (Fr(-3, 4), 0, 0, Fr(5, 4)))
chk("owner |xi|^2 == 1 exactly", nrm(xi_owner), 1)
chk("gamma^2 == 1/(1-beta^2) at 3/5", gam ** 2 == 1 / (1 - beta ** 2), True)

print("B. GKLP ALGEBRA (sympy, on 0<beta<1, 0<B<1)")
bp, Bp = sp.symbols('b Bb', positive=True)
gp = 1 / sp.sqrt(1 - bp ** 2); Gp = 1 / sp.sqrt(1 - Bp ** 2)
tan_theta = Gp * Bp * bp                                    # eq. 14
tan_alpha = Gp * gp * bp                                    # stated after eq. 18
sin2_alpha_17 = bp ** 2 / (1 - Bp ** 2 + bp ** 2 * Bp ** 2)  # eq. 17
chk("eq. 17 consistent with tan(alpha) = Gamma gamma beta",
    sp.simplify(tan_alpha ** 2 / (1 + tan_alpha ** 2) - sin2_alpha_17), 0)
tp = (tan_theta + tan_alpha) / (1 - tan_theta * tan_alpha)
tm = (tan_theta - tan_alpha) / (1 + tan_theta * tan_alpha)
v20 = gp * (1 + Gp ** 2 * Bp ** 2 * bp ** 2) / (1 - Gp ** 2 * Bp * gp * bp ** 2)
w25 = -gp * (1 + Gp ** 2 * Bp ** 2 * bp ** 2) / (1 + Gp ** 2 * Bp * gp * bp ** 2)
chk("eq. 20: tan(theta+alpha)/(Gamma beta) - B == v", sp.simplify(tp / (Gp * bp) - Bp - v20), 0)
chk("eq. 25: tan(theta-alpha)/(Gamma beta) - B == w", sp.simplify(tm / (Gp * bp) - Bp - w25), 0)
v22 = (gp - Bp) / (1 - Bp * gp)                             # eq. 22 at cos=1
chk("eq. 22 (cos=1) == eq. 20 (eqs. 23-24)", sp.simplify(v22 - v20), 0)
veff = 2 / (1 / v20 - 1 / w25)
chk("eq. 28 v_eff == gamma(1+Gamma^2 B^2 beta^2)",
    sp.simplify(veff - gp * (1 + Gp ** 2 * Bp ** 2 * bp ** 2)), 0)
Lq = sp.symbols('Lq', positive=True)
t32 = Gp * Bp * Lq + Gp * Lq / v20
chk("eq. 32 total time == Gamma L'/gamma (1+B/gamma)/(1+Gamma^2B^2beta^2)",
    sp.simplify(t32 - Gp * Lq / gp * (1 + Bp / gp) / (1 + Gp ** 2 * Bp ** 2 * bp ** 2)), 0)
Bc = sp.nsolve(sp.Subs(Gp ** 2 * Bp - 1 / (gp * bp ** 2), bp, sp.Rational(3, 5)).doit(), Bp, 0.8)
chk("B_critical at beta=0.6 == 0.8 (GKLP Fig. 3 caption uses B=0.8)", round(float(Bc), 12), 0.8)

print("C. v, w RE-DERIVED FROM THE BULK QUOTIENT (independent of the envelope picture)")
def arrival_slope(bv, Bv, sign):
    """lim_{D->inf} t(D)/D with t(D) = min_n [n a + sqrt((sign*D - n bx)^2 + (n c)^2)],
    continuous winding s = n/D; minimised on a fine grid + golden refinement."""
    gv = 1 / math.sqrt(1 - bv * bv); Gv = 1 / math.sqrt(1 - Bv * Bv)
    a, bx, c = -Gv * gv * bv, Gv * Bv * gv * bv, gv
    f = lambda s: s * a + math.hypot(sign - s * bx, s * c)
    grid = [i / 2000.0 for i in range(-40000, 40001)]
    s0 = min(grid, key=f)
    lo, hi = s0 - 1e-3, s0 + 1e-3
    for _ in range(200):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if f(m1) < f(m2): hi = m2
        else: lo = m1
    return f((lo + hi) / 2)
for Bv in (0.0, 0.4, 0.7, 0.9):
    bv = 0.6
    gv = 1 / math.sqrt(1 - bv * bv); Gv = 1 / math.sqrt(1 - Bv * Bv)
    v = gv * (1 + Gv ** 2 * Bv ** 2 * bv ** 2) / (1 - Gv ** 2 * Bv * gv * bv ** 2)
    w = -gv * (1 + Gv ** 2 * Bv ** 2 * bv ** 2) / (1 + Gv ** 2 * Bv * gv * bv ** 2)
    kp, km = arrival_slope(bv, Bv, +1), arrival_slope(bv, Bv, -1)
    chk("B=%.1f: bulk forward slope %.9f == 1/v %.9f" % (Bv, kp, 1 / v), abs(kp - 1 / v) < 1e-7, True)
    chk("B=%.1f: bulk backward slope %.9f == -1/w %.9f" % (Bv, km, -1 / w), abs(km + 1 / w) < 1e-7, True)
    chk("B=%.1f: round-trip slope %.9f == 2/v_eff > 0" % (Bv, kp + km),
        abs(kp + km - 2 / (gv * (1 + Gv ** 2 * Bv ** 2 * bv ** 2))) < 1e-7 and kp + km > 0, True)

print("D. ROUND TRIP T > 0 OVER INTEGER WINDINGS, SUB- AND SUPERCRITICAL")
def T_round(D, bv, Bv, N=4000):
    gv = 1 / math.sqrt(1 - bv * bv); Gv = 1 / math.sqrt(1 - Bv * Bv)
    a, bx, c = -Gv * gv * bv, Gv * Bv * gv * bv, gv
    out = min(n * a + math.hypot(D - n * bx, n * c) for n in range(-N, N + 1))
    back = min(n * a + math.hypot(-D - n * bx, n * c) for n in range(-N, N + 1))
    return out, back
negs = 0; mins = []
for Bv in (0.0, 0.4, 0.8, 0.9, 0.99):
    for D in (0.01, 0.3, 1.0, 7.0, 50.0, 400.0):
        o, bk = T_round(D, 0.6, Bv)
        mins.append((Bv, D, o, bk, o + bk))
        negs += (o + bk <= 0)
chk("no (B, D) with T <= 0 (30 cases, B up to 0.99, supercritical above 0.8)", negs, 0)
chk("supercritical B=0.9, D=400: one-way leg is negative (signal to the past)",
    [r for r in mins if r[0] == 0.9 and r[1] == 400.0][0][2] < 0, True)
# general reason in z3: a spacelike xi = (xt, xs) with |xs| > |xt|;
# any closed round trip has total n xi_t + |sum of spatial legs| >= n xi_t + |n||xi_s|.
xt, xs, n, s = z3.Reals('xt xs n s')
S = z3.Solver()
S.add(xs >= 0, xs * xs > xt * xt, n != 0, s >= 0, s * s == n * n * xs * xs, n * xt + s <= 0)
chk("z3: spacelike xi => n xi_t + |n||xi_s| > 0 for n != 0 (negation unsat)", str(S.check()), "unsat")

print("E. RANK-1 STATEMENT AS THE OWNER USES IT")
m = z3.Real('m'); a0, a1, a2, a3 = z3.Reals('a0 a1 a2 a3')
S = z3.Solver()
S.add(-a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3 > 0, m != 0,
      -(m * a0) ** 2 + (m * a1) ** 2 + (m * a2) ** 2 + (m * a3) ** 2 <= 0)
chk("z3: spacelike xi has no nonzero causal real multiple (unsat)", str(S.check()), "unsat")
for K in (1, 2):
    res = set()
    for mv in [x for x in range(-6, 7) if x != 0]:
        S = z3.Solver()
        legs = [[z3.Real('l%d_%d' % (k, i)) for i in range(4)] for k in range(K)]
        for lg in legs:
            S.add(lg[0] > 0, -lg[0] * lg[0] + lg[1] ** 2 + lg[2] ** 2 + lg[3] ** 2 <= 0)
        for i in range(4):
            S.add(sum(lg[i] for lg in legs) == z3.RealVal(str(mv * xi_owner[i])))
        res.add(str(S.check()))
    chk("z3: K=%d future-causal legs summing to m xi_owner, each 0<|m|<=6 (all unsat)" % K,
        sorted(res), ["unsat"])

# every K: the future causal cone is closed under addition.  Route: Lagrange
# identity (sympy) gives Cauchy-Schwarz x.y <= |x||y| in R^3; then a scalar lemma (z3).
X = sp.symbols('x1:4', real=True); Y = sp.symbols('y1:4', real=True)
lag = (sum(c * c for c in X) * sum(c * c for c in Y) - sum(a * b for a, b in zip(X, Y)) ** 2
       - sum((X[i] * Y[j] - X[j] * Y[i]) ** 2 for i in range(3) for j in range(i + 1, 3)))
chk("sympy: Lagrange identity |x|^2|y|^2 - (x.y)^2 = sum of squares", sp.expand(lag), 0)
t1, t2, p, q, d, s_ = z3.Reals('t1 t2 p q d s_')
S = z3.Solver()
S.add(t1 > 0, t2 > 0, p >= 0, q >= 0, p <= t1, q <= t2, d <= p * q, s_ >= 0,
      s_ * s_ == p * p + q * q + 2 * d, s_ > t1 + t2)
chk("z3 scalar lemma: two future-causal legs sum to a future-causal vector (negation unsat); "
    "induction gives every K", str(S.check()), "unsat")

print("F. GKLP eq. 29 (brane circle) = owner's rank-2 SPACELIKE span")
eta = (0, Lp, 0)
A = nrm(xi_brane); C = nrm(eta)
H = -xi_brane[0] * eta[0] + xi_brane[1] * eta[1] + xi_brane[2] * eta[2]
chk("Gram: A = L^2, C = L'^2, H = 0, AC - H^2 = L^2 L'^2 > 0",
    (sp.simplify(A), sp.simplify(C), sp.simplify(H)), (L ** 2, Lp ** 2, 0))

print("G. POLYCHRONAKOS 2210.11497 eq. 2.4 (tilted + boosted brane)")
th, vv, R = sp.symbols('theta v R', real=True)
gv_ = 1 / sp.sqrt(1 - vv ** 2)
a_vec = (-gv_ * vv * sp.cos(th) * R, sp.sin(th) * R, 0, gv_ * sp.cos(th) * R)  # (t,x,y,z)
chk("|a|^2 == R^2 for every tilt and boost", sp.simplify(nrm(a_vec) - R ** 2), 0)

print("\nALL CHECKS OK" if ok_all else "\nSOME CHECK FAILED")
raise SystemExit(0 if ok_all else 1)
