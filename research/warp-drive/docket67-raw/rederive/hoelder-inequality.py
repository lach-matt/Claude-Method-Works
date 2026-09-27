#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: 'hoelder-inequality' as used at noise.py:115-128, 654-655, 716-727.
Independent of noise.py (nothing imported from the tree).  Checks:
 H1  continuous autocorrelation identity  h(0) - h(u) = (1/2) INT (f(t) - f(t+u))^2 dt  (sympy, Gaussian f
     and an asymmetric f), hence |h(u)| <= h(0) = ||f||_2^2 for every real f in L^2.
 H2  discrete analogue, exact polynomial identity (zero-padded sequences, n = 6, every lag).
 H3  z3: the finite L^inf x L^1 Hoelder step  sum h_i w_i <= H sum w_i  given |h_i| <= H, w_i >= 0 (n = 8),
     plus vacuity guard (hypotheses satisfiable) and a mutation (w_i unrestricted in sign -> NOT provable).
 H4  convolution vs autocorrelation: for a NON-even real f, (f*f)(0) < ||f||_2^2 and its sup is not at 0
     (the tree writes 'h = f*f'; the claim ||h||_inf = h(0) is true for the autocorrelation, and for f*f only
     when f is even -- the Gaussian sampler is even, so the tree's number is unaffected).
 H5  thermal kernel: rho = g(0) = pi^2/30 (beta = 1), sympy limit.
 H6  ||g^2||_1 = 180 (zeta6 - zeta7)/pi^3: series (sympy) AND direct position-space quadrature (mpmath),
     the latter independent of the Parseval route the tree uses.
 H7  coefficient: (2/3) h(0) ||g^2||_1 / rho^2 * tau sqrt(2 pi) pi^7 / (zeta6 - zeta7) = 108000; zeta6 = pi^6/945.
 H8  the inequality on the tree's own case: Delta'_f(tau) = (2/3) INT h g^2 / rho^2 vs the bound, tau in
     {0.1, 0.5, 1, 3, 10}; bound at tau = 1 below 1/2; T1 crossing reproduces 1/2 above the bound's own reach.
 H9  z3: bound(tau=1) < 1/2 from rational enclosures of pi, zeta(7), sqrt(2 pi) (own enclosures, not the tree's).
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  :: " + str(detail)) if detail != "" else ""))
    if not ok:
        fails.append(name)

t, u, x = sp.symbols('t u x', real=True)
tau = sp.symbols('tau', positive=True)

# ---------------- H1 continuous autocorrelation identity
for label, f in [("Gaussian sampler (unit integral, width tau)", sp.exp(-t**2 / tau**2) / (tau * sp.sqrt(sp.pi))),
                 ("asymmetric f = t^2 e^{-t} on t>0 (via Heaviside-free form on (0,oo))", None)]:
    if f is not None:
        h = sp.simplify(sp.integrate(f * f.subs(t, t + u), (t, -sp.oo, sp.oo)))
        n2 = sp.simplify(sp.integrate(f**2, (t, -sp.oo, sp.oo)))
        half = sp.simplify(sp.integrate((f - f.subs(t, t + u))**2, (t, -sp.oo, sp.oo)) / 2)
        chk("H1 %s: h(0) = ||f||_2^2 = 1/(tau sqrt(2 pi))" % label,
            sp.simplify(h.subs(u, 0) - n2) == 0 and sp.simplify(n2 - 1 / (tau * sp.sqrt(2 * sp.pi))) == 0, n2)
        chk("H1 %s: h(0) - h(u) = (1/2)||f - f(.+u)||^2" % label, sp.simplify(n2 - h - half) == 0, sp.simplify(h))
        chk("H1 h(u) is the tree's Gaussian h(x) = exp(-x^2/(2 tau^2))/(tau sqrt(2 pi))",
            sp.simplify(h - sp.exp(-u**2 / (2 * tau**2)) / (tau * sp.sqrt(2 * sp.pi))) == 0)
    else:
        up = sp.symbols('up', positive=True)
        fa = lambda s: s**2 * sp.exp(-s)          # supported on s > 0
        # autocorrelation for lag up > 0: INT_0^oo f(s) f(s+up) ds
        h = sp.simplify(sp.integrate(fa(t) * fa(t + up), (t, 0, sp.oo)))
        n2 = sp.integrate(fa(t)**2, (t, 0, sp.oo))
        # (1/2)||f - f(.+up)||^2 over R: f(s+up) supported on s > -up
        half = sp.simplify((sp.integrate(fa(t + up)**2, (t, -up, 0))
                            + sp.integrate((fa(t) - fa(t + up))**2, (t, 0, sp.oo))) / 2)
        chk("H1 asymmetric f: h(0) - h(u) = (1/2)||f - f(.+u)||^2 (u > 0)", sp.simplify(n2 - h - half) == 0,
            "h(u) = %s, ||f||^2 = %s" % (h, n2))
        hmax = max(float(h.subs(up, v)) for v in [0.01, 0.1, 0.5, 1, 2, 5])
        chk("H1 asymmetric f: h(u) < h(0) at sampled u > 0", hmax < float(n2), (hmax, float(n2)))

# ---------------- H2 discrete identity
n = 6
fs = sp.symbols('f0:%d' % n, real=True)
F = lambda i: fs[i] if 0 <= i < n else 0
ok = True
for k in range(1, n):
    lhs = sum(F(i)**2 for i in range(n)) - sum(F(i) * F(i + k) for i in range(-n, 2 * n))
    rhs = sp.Rational(1, 2) * sum((F(i) - F(i + k))**2 for i in range(-n, 2 * n))
    ok &= sp.expand(lhs - rhs) == 0
chk("H2 discrete: ||f||^2 - h_k = (1/2) sum (f_i - f_{i+k})^2 exactly, n = 6, k = 1..5", ok)

# ---------------- H3 z3 finite Hoelder L^inf x L^1
try:
    import z3
    N = 8
    hh = z3.Reals(' '.join('h%d' % i for i in range(N)))
    ww = z3.Reals(' '.join('w%d' % i for i in range(N)))
    H = z3.Real('H')
    hyps = [z3.And(hi <= H, -H <= hi) for hi in hh] + [wi >= 0 for wi in ww]
    goal = z3.Sum([a * b for a, b in zip(hh, ww)]) <= H * z3.Sum(ww)
    s = z3.Solver(); s.add(*hyps); s.add(z3.Not(goal)); r1 = s.check()
    s2 = z3.Solver(); s2.add(*hyps); r2 = s2.check()
    s3 = z3.Solver(); s3.add(*[z3.And(hi <= H, -H <= hi) for hi in hh]); s3.add(z3.Not(goal)); r3 = s3.check()
    chk("H3 z3: sum h_i w_i <= H sum w_i under |h_i|<=H, w_i>=0 (n=8) PROVED", r1 == z3.unsat, r1)
    chk("H3 vacuity guard: hypotheses satisfiable", r2 == z3.sat, r2)
    chk("H3 mutation: drop w_i >= 0 (g^2 >= 0 is load-bearing) -> NOT provable", r3 == z3.sat, r3)
    HAVE_Z3 = True
except ImportError:
    HAVE_Z3 = False
    chk("H3 z3 available", False, "pip install z3-solver")

# ---------------- H4 convolution vs autocorrelation for non-even f
fa = lambda s: s**2 * mp.exp(-s) if s > 0 else mp.mpf(0)
n2 = mp.quad(lambda s: fa(s)**2, [0, mp.inf])
conv = lambda v: mp.quad(lambda s: fa(s) * fa(v - s), [0, max(v, 0) if v > 0 else 0, mp.inf]) if v > 0 else mp.mpf(0)
c0 = conv(mp.mpf(0))
csup = max(conv(mp.mpf(v)) for v in [1, 2, 3, 4, 5, 6, 7, 8])
chk("H4 non-even f: (f*f)(0) = %s < ||f||_2^2 = %s (f*f(0) is NOT the norm)" % (mp.nstr(c0, 6), mp.nstr(n2, 6)),
    c0 < n2)
chk("H4 non-even f: sup(f*f) = %s is <= ||f||_2^2 (Young 2,2,inf / Cauchy-Schwarz) but attained away from 0"
    % mp.nstr(csup, 6), csup <= n2 and csup > c0)

# ---------------- H5-H7 thermal kernel, g^2 norm, coefficient
us = sp.symbols('us', positive=True)
base = sp.pi / 2 * sp.coth(sp.pi * us) - 1 / (2 * us)
g = -sp.diff(base, us, 3) / (2 * sp.pi**2)
rho = sp.limit(g, us, 0)
chk("H5 rho = g(0) = pi^2/30 (Stefan-Boltzmann, beta = 1)", sp.simplify(rho - sp.pi**2 / 30) == 0, rho)
tail = sp.limit(g * us**4, us, sp.oo)
chk("H5 g ~ -3/(2 pi^2 u^4) at infinity (so g^2 in L^1)", sp.simplify(tail + sp.Rational(3, 2) / sp.pi**2) == 0, tail)
k = sp.symbols('k', integer=True, positive=True)
series = sp.summation((k - 1) * sp.factorial(6) / k**7, (k, 1, sp.oo)) / (4 * sp.pi**3)
closed = 180 * (sp.zeta(6) - sp.zeta(7)) / sp.pi**3
chk("H6 series = 180 (zeta6 - zeta7)/pi^3", sp.simplify(series - closed) == 0)
gf = sp.lambdify(us, g, 'mpmath')
def gnum(v):
    v = mp.mpf(v)
    if v < mp.mpf('1e-3'):   # series near 0 to avoid cancellation
        return mp.mpf(str(sp.N(sp.series(g, us, 0, 8).removeO().subs(us, sp.Rational(str(v))), 40)))
    return gf(v)
mp.mp.dps = 40
direct = 2 * mp.quad(lambda v: gnum(v)**2, [0, mp.mpf('1e-3'), 0.5, 2, 10, mp.inf])
cl = mp.mpf(str(sp.N(closed, 45)))
chk("H6 position-space quadrature 2 INT_0^oo g^2 = closed form (independent of Parseval)",
    abs(direct / cl - 1) < mp.mpf('1e-15'), "%s vs %s" % (mp.nstr(direct, 20), mp.nstr(cl, 20)))
B = sp.Rational(2, 3) / (tau * sp.sqrt(2 * sp.pi)) * closed / rho**2
coef = sp.simplify(B * tau * sp.sqrt(2 * sp.pi) * sp.pi**7 / (sp.zeta(6) - sp.zeta(7)))
chk("H7 coefficient = 108000", coef == 108000, coef)
chk("H7 zeta(6) = pi^6/945", sp.simplify(sp.zeta(6) - sp.pi**6 / 945) == 0)

# ---------------- H8 the inequality on the tree's own case
rhon = mp.mpf(str(sp.N(rho, 45)))
rows = []
for tv in ['0.1', '0.5', '1', '3', '10']:
    tv = mp.mpf(tv)
    hG = lambda v: mp.exp(-v**2 / (2 * tv**2)) / (tv * mp.sqrt(2 * mp.pi))
    dprime = mp.mpf(2) / 3 * 2 * mp.quad(lambda v: hG(v) * gnum(v)**2, [0, mp.mpf('1e-3'), tv, 10 * tv + 10, mp.inf]) / rhon**2
    bound = mp.mpf(2) / 3 * hG(0) * cl / rhon**2
    rows.append((tv, dprime, bound))
    print("     tau/beta = %-5s  Delta'_f = %-22s  Hoelder bound = %-22s  ratio = %s"
          % (mp.nstr(tv, 3), mp.nstr(dprime, 12), mp.nstr(bound, 12), mp.nstr(dprime / bound, 8)))
chk("H8 Delta'_f <= Hoelder bound at all five tau", all(d <= b for _, d, b in rows))
d1 = [r for r in rows if r[0] == 1][0]
chk("H8 tau = beta: Delta'_f = %s (tree states 0.1186), bound = %s < 1/2" % (mp.nstr(d1[1], 6), mp.nstr(d1[2], 6)),
    abs(d1[1] - mp.mpf('0.1186')) < mp.mpf('5e-5') and d1[2] < 0.5)
chk("H8 bound -> Delta'_f ratio -> 1 as tau/beta grows (bound asymptotically sharp for Gaussian h)",
    rows[-1][1] / rows[-1][2] > rows[0][1] / rows[0][2] and rows[-1][1] / rows[-1][2] > 0.9)
chk("H8 tau = 0.1 beta: bound = %s exceeds 1/2 -- Hoelder alone cannot decide there (tree's vacuity guard)"
    % mp.nstr(rows[0][2], 6), rows[0][2] > 0.5)

# ---------------- H9 z3 with own enclosures
if HAVE_Z3:
    from fractions import Fraction as Fr
    p, z7, r = z3.Reals('p z7 r')
    lo7 = sum(Fr(1, m**7) for m in range(1, 21)); hi7 = lo7 + Fr(1, 6 * 20**6)
    Hy = [p > z3.RealVal("3141592/1000000"), p < z3.RealVal("3141593/1000000"),
          z7 >= z3.RealVal(str(lo7)), z7 <= z3.RealVal(str(hi7)), r > 0, r * r == 2 * p]
    goal = 2 * 108000 * (p**6 / 945 - z7) < r * p**7
    s = z3.Solver(); s.add(*Hy); s.add(z3.Not(goal)); rr = s.check()
    s2 = z3.Solver(); s2.add(*Hy); rs = s2.check()
    goal10 = 2 * 108000 * (p**6 / 945 - z7) < z3.RealVal("1/10") * r * p**7
    s3 = z3.Solver(); s3.add(*Hy); s3.add(z3.Not(goal10)); r10 = s3.check()
    chk("H9 z3: 108000 (zeta6 - zeta7)/(sqrt(2pi) pi^7) < 1/2 at tau = beta PROVED (own enclosures)", rr == z3.unsat, rr)
    chk("H9 vacuity guard satisfiable", rs == z3.sat, rs)
    chk("H9 same query at tau = beta/10 NOT provable", r10 == z3.sat, r10)

print("\n%d FAIL" % len(fails) if fails else "\nALL PASS")
sys.exit(1 if fails else 0)
