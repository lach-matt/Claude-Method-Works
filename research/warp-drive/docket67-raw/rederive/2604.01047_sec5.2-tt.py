#!/usr/bin/env python3
"""DOCKET 67 re-derivation: GMMPS (arXiv 2604.01047v1) sec. 5.2, TT sector, AS linstab.py USES IT.

What the tree uses (linstab.py:147-150, 170-179, 453-455; bracket 747-777, 981-990):
  "5.2 (TT, alpha~^TT_1 = 0, b_0 = 0): 'One of the zeros, say gamma_0, is, however, always
   negative ... the magnitude of gamma_0 can be made as small as we want by choosing larger and
   larger positive b_2' (p. 62)."
  and, resting on it: the TT growing root near g* = -b_1/b_2 has a scale set by the FREE constant
  (alpha~^TT_4, through b_2): "Planckian for O(1) values only" (WITHDRAWN entry, linstab.py:453-455;
  LITERATURE_SPLIT_IS_ONE_CONSTANT scoping, 344-349).

SOURCE NOT READ THIS SESSION (alphaXiv quota exceeded on every call; arxiv.org / alphaxiv.org
egress-blocked).  The TT dispersion function is taken from the TREE's transcription of (5.4)
(linstab.py:750, 763-764): F_TT(g) = g (a - g)^2 J(g) - g (b_1 + b_2 g), a = 4 m^2, b_1 = 60/kappa,
b_0 = 0, and J = the Stieltjes transform of rho (4.5) (READ at source by the sibling audit
2604.01047_spectral-j).  Nothing is imported from the tree.  Units m = 1.

 T1  F_TT(0) = 0 identically: g = 0 is a root for every constant (b_0 = 0).               sympy
 T2  G(g) := F_TT(g)/g = (4 - g)^2 J(g) - b_1 - b_2 g;  G(0) = 1/(6 pi^2) - 60/kappa,
     negative iff kappa m^2 < 360 pi^2 (always, for m << M_P).                             sympy
 T3  z3: for M >= 4, g < 0 the integrand (4-g)^2/(M-g) is strictly decreasing in g, so with
     rho >= 0 (rho > 0 on M > 4) (4-g)^2 J(g) is strictly decreasing on g < 0.
     Vacuity guard (hypotheses sat) + control (the claim fails for g in (0,4) somewhere: sat).  z3
 T4  hence for b_2 >= 0, G is strictly decreasing on g < 0 and G -> +inf as g -> -inf
     (b_2 > 0 trivially; b_2 = 0 via (4-g)^2 J ~ |g| ln|g| /(16 pi^2)): EXACTLY ONE negative
     zero gamma_0.  J-DROPPED: b_1 g + b_2 g^2 = 0 gives gamma_0 = -b_1/b_2 < 0 iff b_2 > 0.  sympy+mpmath
 T5  d gamma_0 / d b_2 = gamma_0 / G'(gamma_0) > 0 (both negative): |gamma_0| strictly
     decreasing in b_2, and gamma_0 -> 0- as b_2 -> +inf, with J kept.  Numeric at GMMPS's
     matched eps = kappa m^2 = (m/M_P)^2.                                                  sympy+mpmath
 T6  b_2 < 0: J-dropped has NO negative zero; J-kept STILL has one (G(0) < 0, G -> +inf by the
     log), at |g| ~ exp(16 pi^2 |b_2|) b_1-scale -- super-Planckian.  Recorded as a scope fact:
     'b_2 > 0' is needed for the J-dropped statement, not for existence with J kept.       mpmath
 T7  scale: at b_2 = O(1) the J-kept zero is Planckian (|gamma_0| ~ b_1/(b_2 + ln/(16pi^2)));
     J is NOT negligible there (J-dropped -b_1/b_2 is off by ~ x1.9 at b_2 = 1).  gamma_0 lies
     in (-4 m^2, 0) (the range the tree states for Thm 4.16) iff G(-4) > 0 iff
     b_2 > (b_1 - 64 J(-4))/4 ~ 15/eps.  So 'Planckian for O(1)' roots are OUTSIDE that range.  mpmath
 T8  the tree's bracket at b_2 = +1e100 (TT): exact zero located and compared with -b_1/b_2.   mpmath
Exit 0 iff every assertion passes.
"""
import sys
import sympy as sp
import mpmath as mp
import z3

ok = True


def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


mp.mp.dps = 80

# ---------------------------------------------------------------- J from (4.5) / (4.17), m = 1
def J(g):
    """INT_4^inf rho(M)/(M-g) dM, rho = sqrt(1-4/M)/(16 pi^2 M) (4.5)."""
    g = mp.mpf(g)
    # substitution M = 4 e^t (t >= 0): integrand sqrt(1-e^-t)/(16 pi^2) / (4 e^t - g), smooth,
    # a plateau up to t ~ ln(|g|/4) then exponential decay -- breakpoints there
    with mp.workdps(160):      # quadrature needs the extra digits at |g| >~ 1e80 (checked)
        g = mp.mpf(g)
        h = lambda t: mp.sqrt(-mp.expm1(-t)) / (16 * mp.pi ** 2) / (4 * mp.exp(t) - g)
        L = mp.log(max(abs(g), 4) / 4)
        pts = [mp.mpf(0), mp.mpf('1e-6'), mp.mpf('1e-3'), mp.mpf(1)] + \
              [L * k / 64 for k in range(1, 65)] + [L + 2, L + 5, L + 10, L + 40, mp.inf]
        pts = sorted(set(pts[:-1])) + [mp.inf]
        v = mp.quad(h, pts)
    return +v


def J_closed(g):
    """(4.17), principal branches (verified against the integral by the sibling audit)."""
    g = mp.mpc(g)
    return ((1 / (8 * mp.pi ** 2)) * (1 / g - mp.sqrt(4 - g) * mp.acsc(2 / mp.sqrt(g)) / g ** mp.mpf(1.5))).real


J0 = 1 / (96 * mp.pi ** 2)
chk("J(0) integral = 1/(96 pi^2)", abs(J(0) - J0) < mp.mpf(10) ** -60)
for gg in (-1, -100, -1e6, -1e40, -1e120):
    chk("J closed (4.17) = integral at g = %g" % gg, abs(J_closed(gg) / J(gg) - 1) < mp.mpf(10) ** -30)

# ---------------------------------------------------------------- T1, T2 (sympy, symbolic)
g, kap, b2, Js, Jp = sp.symbols('gamma kappa b_2 J0 Jp', real=True)
Jf = sp.Function('J')
a, b1 = 4, 60 / kap
FTT = g * (a - g) ** 2 * Jf(g) - g * (b1 + b2 * g)          # (5.4) as linstab.py:764 transcribes it
chk("T1 F_TT(0) = 0 identically (b_0 = 0): gamma = 0 always a root", sp.simplify(FTT.subs(g, 0)) == 0)
G = sp.simplify(sp.expand(FTT / g))
chk("T1 F_TT = gamma * G with G = (4-g)^2 J - b_1 - b_2 g",
    sp.simplify(G - ((a - g) ** 2 * Jf(g) - b1 - b2 * g)) == 0)
G0 = G.subs(g, 0).subs(Jf(0), sp.Rational(1, 96) / sp.pi ** 2)
chk("T2 G(0) = 1/(6 pi^2) - 60/kappa", sp.simplify(G0 - (1 / (6 * sp.pi ** 2) - 60 / kap)) == 0)
kc = sp.solve(sp.Eq(G0, 0), kap)
chk("T2 G(0) < 0 iff kappa m^2 < 360 pi^2 (the only sign change)", kc == [360 * sp.pi ** 2])

# ---------------------------------------------------------------- T3 z3
M, x = z3.Reals('M x')
d_integrand = (4 - x) * (4 + x - 2 * M)            # numerator of d/dg [(4-g)^2/(M-g)], denom (M-g)^2 > 0
Msp, gsp = sp.symbols('M g', real=True)
chk("T3 sympy: d/dg[(4-g)^2/(M-g)] = (4-g)(4+g-2M)/(M-g)^2",
    sp.simplify(sp.diff((4 - gsp) ** 2 / (Msp - gsp), gsp) - (4 - gsp) * (4 + gsp - 2 * Msp) / (Msp - gsp) ** 2) == 0)
s = z3.Solver(); s.add(M >= 4, x < 0)
chk("T3 vacuity guard: {M >= 4, g < 0} satisfiable", s.check() == z3.sat)
s = z3.Solver(); s.add(M >= 4, x < 0, z3.Not(d_integrand < 0))
chk("T3 z3: M >= 4, g < 0 => d/dg integrand < 0 (negation unsat)", s.check() == z3.unsat)
s = z3.Solver(); s.add(M >= 4, x < 4, z3.Not(d_integrand < 0))
chk("T3 z3 (stronger): the sign holds for every g < 4 = 4m^2, not only g < 0 (negation unsat)", s.check() == z3.unsat)
s = z3.Solver(); s.add(M > 0, x < 0, d_integrand >= 0)
chk("T3 control: without the threshold M >= 4 (rho's support) the sign can fail (sat)", s.check() == z3.sat)
H = lambda gg: (4 - mp.mpf(gg)) ** 2 * (J0 if gg == 0 else J_closed(gg))   # (4.17), checked = integral above and below
vals = [H(-t) for t in (0, 1e-6, 1, 10, 1e3, 1e6, 1e12)]
chk("T3 numeric: (4-g)^2 J(g) strictly increasing as g -> -inf", all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)))
big = mp.mpf(10) ** 40
chk("T4 asymptotic: (4-g)^2 J(g) / (|g| ln|g| /(16 pi^2)) -> 1 (ratio at |g| = 1e40 within 5%)",
    abs(H(-big) / (big * mp.log(big) / (16 * mp.pi ** 2)) - 1) < 0.05)

# ---------------------------------------------------------------- the point: GMMPS's matched eps
# eps = (m/M_P)^2 at m = 7.885e-3 eV (sibling audit 2604.01047_sec5.3-mass), reduced M_P = 2.435323e27 eV
eps = (mp.mpf('7.885e-3') / mp.mpf('2.435323e27')) ** 2
B1 = 60 / eps
print("   eps = kappa m^2 = %s ; b_1 = 60/eps = %s m^2" % (mp.nstr(eps, 4), mp.nstr(B1, 4)))


def Gn(gg, bb):
    return H(gg) - B1 - mp.mpf(bb) * mp.mpf(gg)


def root(bb):
    """unique negative zero of G for b_2 >= 0 (G decreasing); bisection in log|g|."""
    lo, hi = mp.mpf(-1) * mp.mpf(10) ** -300, None
    t = mp.mpf(10) ** -300
    while Gn(-t, bb) < 0:
        t *= 10
        if t > mp.mpf(10) ** 400:
            return None
    hi_t, lo_t = t, t / 10
    for _ in range(400):
        mid = mp.sqrt(hi_t * lo_t)
        if Gn(-mid, bb) < 0:
            lo_t = mid
        else:
            hi_t = mid
        if hi_t / lo_t - 1 < mp.mpf(10) ** -40:
            break
    return -mp.sqrt(hi_t * lo_t)


chk("T2 at GMMPS's eps, G(0) < 0", Gn(0, 0) < 0)
roots = {}
for bb in (0, 1, 10, 1e3, 1e10, 1e30, 1e60, 1e100):
    r = root(bb)
    roots[bb] = r
    ratio = (r / (-B1 / bb)) if bb else None
    print("   b_2 = %-6g : gamma_0 = %s m^2   gamma_0/(-b_1/b_2) = %s   in (-4,0): %s" % (
        bb, mp.nstr(r, 6), mp.nstr(ratio, 8) if ratio is not None else "n/a (J-dropped has no root)",
        -4 < r < 0))
    # T4 uniqueness numerically: G decreasing at samples around the root
    chk("T4 b_2 = %g: exactly one sign change of G on a log grid of g < 0" % bb,
        sum(1 for k in range(-300, 200, 2) if (Gn(-mp.mpf(10) ** k, bb) < 0) != (Gn(-mp.mpf(10) ** (k + 2), bb) < 0)) == 1)
ordered = [abs(roots[b]) for b in (0, 1, 10, 1e3, 1e10, 1e30, 1e60, 1e100)]
chk("T5 |gamma_0| strictly decreasing in b_2 (J kept)", all(ordered[i] > ordered[i + 1] for i in range(len(ordered) - 1)))
chk("T5 gamma_0 -> 0-: |gamma_0| at b_2 = 1e100 < 1e-38 m^2", ordered[-1] < mp.mpf(10) ** -38)
chk("T5 large b_2: gamma_0 / (-b_1/b_2) -> 1 (within 1e-30 at b_2 = 1e100)",
    abs(roots[1e100] / (-B1 / mp.mpf(1e100)) - 1) < mp.mpf(10) ** -30)
# symbolic implicit derivative
gam0 = sp.Symbol('g0', negative=True)
Gp = sp.Symbol('Gp', negative=True)          # G'(gamma_0) < 0 by T3 and b_2 >= 0
dg_db2 = -sp.diff(-b2 * g, b2).subs(g, gam0) / Gp
chk("T5 sympy: d gamma_0/d b_2 = gamma_0/G'(gamma_0) > 0", sp.simplify(dg_db2 - gam0 / Gp) == 0 and dg_db2.is_positive)

# ---------------------------------------------------------------- T6 b_2 < 0 (J kept vs J dropped)
for bb in (-mp.mpf('0.05'), -mp.mpf('0.2')):
    # search for a sign change of G on g < 0 far out
    ks = [k for k in range(-10, 400)
          if (Gn(-mp.mpf(10) ** k, bb) < 0) != (Gn(-mp.mpf(10) ** (k + 1), bb) < 0)]
    print("   b_2 = %s : J-kept sign change(s) of G at |g| ~ 10^%s m^2 (M_P^2 = 10^%s m^2); J-dropped: -b_1/b_2 = %s > 0 (no negative zero)"
          % (mp.nstr(bb, 3), [k for k in ks], mp.nstr(mp.log10(1 / eps), 4), mp.nstr(-B1 / bb, 3)))
    chk("T6 b_2 = %s: J-kept G has a negative zero (odd # sign changes), beyond M_P^2" % mp.nstr(bb, 3),
        len(ks) % 2 == 1 and min(ks) > mp.log10(1 / eps))

# ---------------------------------------------------------------- T7 scale at O(1) b_2 and Thm 4.16 range
r1 = roots[1]
chk("T7 b_2 = 1: |gamma_0| Planckian (between 1 and 100 x M_P^2, reduced M_P, m = 1 units)",
    1 / eps < abs(r1) < 100 / eps)
chk("T7 b_2 = 1: J NOT negligible -- J-dropped -b_1/b_2 overstates |gamma_0| by > x1.5",
    (-B1) / r1 > 1.5)
print("   b_2 = 1: gamma_0/(-b_1) = %s ; |gamma_0| eps = %s (units of M_P^2)" % (mp.nstr(r1 / -B1, 5), mp.nstr(abs(r1) * eps, 5)))
b2_edge = (B1 - H(-4)) / 4
print("   gamma_0 in (-4 m^2, 0) iff b_2 > (b_1 - 64 J(-4))/4 = %s ( = %s / eps )" % (mp.nstr(b2_edge, 6), mp.nstr(b2_edge * eps, 8)))
chk("T7 edge b_2 = (b_1 - 64 J(-4))/4 ~ 15/eps", abs(b2_edge * eps / 15 - 1) < mp.mpf(10) ** -50)
chk("T7 b_2 = O(1) (0..1e3) roots OUTSIDE (-4 m^2, 0); b_2 = 1e100 root INSIDE",
    all(not (-4 < roots[b] < 0) for b in (0, 1, 10, 1e3)) and (-4 < roots[1e100] < 0))
chk("T7 at the edge the zero sits at -4 (G(-4) = 0 up to rounding)", abs(Gn(-4, b2_edge)) < mp.mpf(10) ** -50 * B1)

# ---------------------------------------------------------------- T8 the tree's TT bracket at b_2 = +1e100
gs = -abs(B1 / mp.mpf(1e100))
chk("T8 tree's TT bracket: exact zero inside (2 g*, g*/2)", 2 * gs < roots[1e100] < gs / 2)
print("   b_2 = 1e100: g* = %s, exact gamma_0 = %s" % (mp.nstr(gs, 8), mp.nstr(roots[1e100], 8)))

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
