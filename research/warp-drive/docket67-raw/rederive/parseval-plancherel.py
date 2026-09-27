#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of 'parseval-plancherel' as the warp board uses it.

Independent of noise.py / fewsterteo.py: nothing is imported from the tree.
Two uses are checked, each by a route the tree itself does NOT run.

(A) noise.py:117-118, 581-586.  ||g^2||_1 = INT_{-oo}^{oo} g(u)^2 du for the
    thermal (beta = 1) normal-ordered phidot kernel
        g(u) = -(1/2pi^2) d^3/du^3 [ (pi/2) coth(pi u) - 1/(2u) ]
    claimed = 180 (zeta6 - zeta7)/pi^3 "(Parseval, exact)".
    The tree's selftest (noise.py:1043) checks only  series == closed form,
    i.e. SUM (n-1) 6!/n^7 /(4 pi^3) = 180(zeta6-zeta7)/pi^3.  It does not check
    the Parseval step INT g^2 du = pi INT_0^oo S(k)^2 dk itself.  Here:
      A1  sympy: 1/(e^x-1)^2 = SUM (n-1) e^{-nx} (x > 0), INT x^6 e^{-nx} = 720/n^7,
          SUM -> 720 (zeta6 - zeta7).
      A2  sympy: -d^3/du^3 sin(ku) = k^3 cos(ku), so g(u) = INT_0^oo S(k) cos(ku) dk
          with S(k) = k^3 n(k)/(2 pi^2)  (one-sided cosine transform).
      A3  mpmath: position-space INT_{-oo}^{oo} g(u)^2 du, directly from the closed form
          -- the Parseval step checked by quadrature, not assumed.
      A4  mpmath: pi INT_0^oo S(k)^2 dk (the spectral side) -- must agree with A3.
      A5  sympy: beta scaling g_beta(u) = beta^-4 g_1(u/beta) gives beta^-7.
      A6  g(0) = pi^2/30 and g -> -3/(2 pi^2 u^4) (so g in L^2 and L^1).
(B) fewsterteo.py:46-54, 301-303, 575-580.  For the clamped-beam fundamental on
    [0,1] (normalised INT g^2 = 1, extended by zero):
        INT_0^oo u^4 |ghat(u)|^2 du = pi INT (g'')^2 = pi mu_1^4.
      B1  mpmath: mu_1 from cos mu cosh mu = 1; g = g' = 0 at both ends.
      B2  mpmath: INT (g'')^2 / INT g^2 = mu_1^4 (the clamping identity).
      B3  mpmath: INT_0^oo |FT g''|^2 du by quadrature to U, PLUS the exact tail
          of the asymptotic form INCLUDING the oscillating cross term (the tree
          averages it away), PLUS a residual bounded numerically.
      B4  prefactor: (1/16 pi^3) pi mu^4 = mu^4/(16 pi^2) = 3.16985793831...
          matches Fewster 1208.5399 eq (1)->(3) at m = 0.
      B5  HYPOTHESIS GUARDS (the vacuity/encoding-drift guards):
          (i) drop clamping (g' != 0 at the ends: g = sin(pi t)) -> u^4|ghat|^2
              tends to a nonzero constant, INT_0^U grows linearly in U: the
              identity FAILS -- clamping is load-bearing, not decorative;
          (ii) drop reality (g -> g e^{i w t}) -> INT_0^oo != pi INT |g''|^2,
              while INT_{-oo}^{oo} = 2 pi INT |g''|^2 still holds: the one-sided
              factor pi rests on 'real g';
          (iii) convention: e^{+iut} (Fewster) vs e^{-iut} (tree) give the same
              |ghat|^2 for real g.
Exit 0 iff every check passes.
"""
import sys
import sympy as sp
import mpmath as mp

FAIL = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------------ (A)
print("=== (A) noise.py: ||g^2||_1 for the thermal phidot kernel ===")
x = sp.symbols('x', positive=True)
n = sp.symbols('n', integer=True, positive=True)
N = sp.symbols('N', integer=True, positive=True)
# A1: geometric series squared, termwise on x > 0
rr = sp.symbols('r', positive=True)
gen = rr ** 2 / (1 - rr) ** 2          # SUM_{n>=1} (n-1) r^n for 0 < r < 1
coeffs_ok = all(sp.series(gen, rr, 0, 40).removeO().coeff(rr, m) == m - 1 for m in range(1, 40))
chk("A1a' r^2/(1-r)^2 = SUM_{n>=1} (n-1) r^n (coefficients 1..39)", coeffs_ok)
chk("A1a  with r = e^{-x} (x > 0, so 0 < r < 1): r^2/(1-r)^2 = 1/(e^x-1)^2",
    sp.simplify(gen.subs(rr, sp.exp(-x)) - 1 / (sp.exp(x) - 1) ** 2) == 0)
chk("A1b INT_0^oo x^6 e^{-nx} dx = 720/n^7",
    sp.simplify(sp.integrate(x ** 6 * sp.exp(-n * x), (x, 0, sp.oo)) - 720 / n ** 7) == 0)
ser = sp.summation((n - 1) * 720 / n ** 7, (n, 1, sp.oo))
chk("A1c SUM (n-1) 720/n^7 = 720 (zeta6 - zeta7)",
    sp.simplify(ser - 720 * (sp.zeta(6) - sp.zeta(7))) == 0, str(ser))
closed = 180 * (sp.zeta(6) - sp.zeta(7)) / sp.pi ** 3
chk("A1d (1/4pi^3) * 720(zeta6-zeta7) = 180(zeta6-zeta7)/pi^3",
    sp.simplify(ser / (4 * sp.pi ** 3) - closed) == 0)

# A2: the kernel is the one-sided cosine transform of S(k) = k^3 n(k)/(2 pi^2)
u, k = sp.symbols('u k', positive=True)
chk("A2a -d^3/du^3 sin(ku) = k^3 cos(ku)",
    sp.simplify(-sp.diff(sp.sin(k * u), u, 3) - k ** 3 * sp.cos(k * u)) == 0)
base = sp.pi / 2 * sp.coth(sp.pi * u) - 1 / (2 * u)
g_sym = -sp.diff(base, u, 3) / (2 * sp.pi ** 2)
# spot-check the base integral INT_0^oo sin(ku)/(e^k-1) dk = base numerically
mp.mp.dps = 30
for uu in (mp.mpf('0.3'), mp.mpf('1.7')):
    lhsn = mp.quad(lambda kk: mp.sin(kk * uu) / mp.expm1(kk), [0, 1, 10, 60, mp.inf])
    rhsn = mp.pi / 2 * mp.coth(mp.pi * uu) - 1 / (2 * uu)
    chk("A2b INT_0^oo sin(ku)/(e^k-1) dk = (pi/2)coth(pi u) - 1/(2u) at u=%s" % mp.nstr(uu, 3),
        abs(lhsn - rhsn) < mp.mpf('1e-20'), mp.nstr(lhsn - rhsn, 3))

# A6: g(0), large-u tail
g0 = sp.limit(g_sym, u, 0)
chk("A6a g(0) = pi^2/30", sp.simplify(g0 - sp.pi ** 2 / 30) == 0, str(g0))
tail = sp.limit(g_sym * u ** 4, u, sp.oo)
chk("A6b u^4 g(u) -> -3/(2 pi^2)", sp.simplify(tail + sp.Rational(3, 2) / sp.pi ** 2) == 0, str(tail))

# A3: position side, direct quadrature of INT_{-oo}^{oo} g^2 (g even)
mp.mp.dps = 60
g_mp = sp.lambdify(u, g_sym, 'mpmath')
gser = sp.lambdify(u, sp.series(g_sym, u, 0, 24).removeO(), 'mpmath')


def gnum(t):
    t = abs(t)
    return gser(t) if t < mp.mpf('0.05') else g_mp(t)


pos = 2 * mp.quad(lambda t: gnum(t) ** 2, [0, mp.mpf('0.05'), 0.5, 1, 2, 5, 20, 100, mp.inf])
mp.mp.dps = 40
closed_n = mp.mpf(180) * (mp.zeta(6) - mp.zeta(7)) / mp.pi ** 3
# A4: spectral side, pi INT_0^oo S(k)^2 dk, S = k^3/(e^k-1)/(2pi^2)
spec = mp.pi * mp.quad(lambda kk: (kk ** 3 / mp.expm1(kk) / (2 * mp.pi ** 2)) ** 2,
                       [0, 1, 5, 20, 80, mp.inf])
print("    position INT g^2  =", mp.nstr(pos, 25))
print("    spectral pi INT S^2=", mp.nstr(spec, 25))
print("    180(z6-z7)/pi^3    =", mp.nstr(closed_n, 25))
chk("A3 position-space INT_{-oo}^{oo} g^2 du = 180(zeta6-zeta7)/pi^3 (Parseval step, by quadrature)",
    abs(pos - closed_n) / closed_n < mp.mpf('1e-20'), "rel " + mp.nstr(abs(pos - closed_n) / closed_n, 3))
chk("A4 spectral side pi INT_0^oo S^2 dk = closed form",
    abs(spec - closed_n) / closed_n < mp.mpf('1e-25'), "rel " + mp.nstr(abs(spec - closed_n) / closed_n, 3))
# control: the HALF-line integral is half -- an encoding drift a reader could make
chk("A3-control INT_0^oo g^2 alone is HALF the claimed value (whole line is what noise.py uses: Y = 2 INT_0^oo)",
    abs(pos / 2 - closed_n / 2) / closed_n < mp.mpf('1e-20') and abs(pos / 2 - closed_n) > closed_n / 3)

# A5: beta scaling
b = sp.symbols('beta', positive=True)
g_beta = (g_sym.subs(u, u / b) / b ** 4)
g_beta_direct = -sp.diff((sp.pi / (2 * b)) * sp.coth(sp.pi * u / b) - 1 / (2 * u), u, 3) / (2 * sp.pi ** 2)
chk("A5a g_beta(u) = beta^-4 g_1(u/beta) (from (pi/2beta) coth(pi u/beta) - 1/(2u))",
    sp.simplify(g_beta - g_beta_direct) == 0)
chk("A5b INT g_beta^2 du = beta^-7 INT g_1^2 (change of variable u = beta v): exponent 2*(-4)+1 = -7",
    2 * (-4) + 1 == -7)

# ------------------------------------------------------------------ (B)
print("\n=== (B) fewsterteo.py: INT_0^oo u^4|ghat|^2 du = pi INT (g'')^2 = pi mu_1^4 ===")
mp.mp.dps = 30
mu = mp.findroot(lambda m: mp.cos(m) * mp.cosh(m) - 1, mp.mpf('4.73'))
chk("B1a mu_1 = 4.730040744862704 (cos mu cosh mu = 1)", abs(mu - mp.mpf('4.730040744862704')) < 1e-14,
    mp.nstr(mu, 20))
sg = (mp.cosh(mu) - mp.cos(mu)) / (mp.sinh(mu) - mp.sin(mu))
G = lambda t: mp.cosh(mu * t) - mp.cos(mu * t) - sg * (mp.sinh(mu * t) - mp.sin(mu * t))
G1 = lambda t: mu * (mp.sinh(mu * t) + mp.sin(mu * t) - sg * (mp.cosh(mu * t) - mp.cos(mu * t)))
G2 = lambda t: mu ** 2 * (mp.cosh(mu * t) + mp.cos(mu * t) - sg * (mp.sinh(mu * t) + mp.sin(mu * t)))
bnd = max(abs(v) for v in (G(0), G1(0), G(1), G1(1)))
chk("B1b clamped: g = g' = 0 at t = 0, 1", bnd < mp.mpf('1e-20'), mp.nstr(bnd, 3))
chk("B1c g'' does NOT vanish at the ends (so FT(g'') ~ 1/u and the tail is real)",
    abs(G2(0)) > 1 and abs(G2(1)) > 1, "g''(0)=%s g''(1)=%s" % (mp.nstr(G2(0), 8), mp.nstr(G2(1), 8)))
Ng = mp.quad(lambda t: G(t) ** 2, [0, 0.5, 1])
Ng2 = mp.quad(lambda t: G2(t) ** 2, [0, 0.5, 1])
chk("B2 INT (g'')^2 = mu^4 INT g^2 (clamping identity)", abs(Ng2 / Ng - mu ** 4) < mp.mpf('1e-20'),
    mp.nstr(Ng2 / Ng - mu ** 4, 3))

# closed-form FT of g'' on [0,1]: g'' = mu^2 (cosh + cos - sg(sinh + sin))
aa = [mu, -mu, 1j * mu, -1j * mu]
cc = [(1 - sg) / 2, (1 + sg) / 2, (1 + 1j * sg) / 2, (1 - 1j * sg) / 2]   # g''/mu^2 = SUM cc e^{aa t}
for t0 in (mp.mpf('0.2'), mp.mpf('0.77')):
    v = sum(c * mp.exp(a * t0) for a, c in zip(aa, cc)) * mu ** 2
    assert abs(v - G2(t0)) < 1e-20, "g'' exponential form"


def FT2(uu, sign=-1):
    """INT_0^1 g''(t) e^{sign*i u t} dt / sqrt(INT g^2)."""
    s = 0
    for a, c in zip(aa, cc):
        z = a + sign * 1j * uu
        s += c * (mp.exp(z) - 1) / z
    return s * mu ** 2 / mp.sqrt(Ng)


A0, A1v = G2(0) / mp.sqrt(Ng), G2(1) / mp.sqrt(Ng)
U = mp.mpf(4000)
f = lambda uu: abs(FT2(uu)) ** 2
nodes = [mp.mpf(0)] + [mp.pi * j for j in range(1, int(U / mp.pi) + 1)] + [U]
part = mp.fsum(mp.quad(f, [nodes[i], nodes[i + 1]]) for i in range(len(nodes) - 1))
# exact tail of the asymptotic form |(g''(1) e^{-iu} - g''(0))/(-iu)|^2
#   = (A1^2 + A0^2 - 2 A0 A1 cos u)/u^2 ;  INT_U^oo cos u/u^2 du = cos U/U - (pi/2 - Si(U))
cos_tail = mp.cos(U) / U - (mp.pi / 2 - mp.si(U))
tail_avg = (A0 ** 2 + A1v ** 2) / U
tail_exact = tail_avg - 2 * A0 * A1v * cos_tail
# residual INT_U^oo (|F|^2 - |F_as|^2): sample its size at U..10U
Fas = lambda uu: abs((A1v * mp.exp(-1j * uu) - A0) / (-1j * uu)) ** 2
res_bound = max(abs(f(uu) - Fas(uu)) for uu in (U, 2 * U, 5 * U, 10 * U)) * U
total = part + tail_exact
target = mp.pi * mu ** 4
print("    INT_0^U |FT g''|^2 =", mp.nstr(part, 20), " tail(exact asympt) =", mp.nstr(tail_exact, 12),
      " tail(avg, tree's) =", mp.nstr(tail_avg, 12))
print("    total =", mp.nstr(total, 20), "  pi mu^4 =", mp.nstr(target, 20),
      "  rel =", mp.nstr(abs(total - target) / target, 3), "  residual bound ~", mp.nstr(res_bound, 3))
chk("B3 INT_0^oo |FT g''|^2 du = pi mu_1^4 (quadrature + exact tail)",
    abs(total - target) / target < mp.mpf('1e-9'))
chk("B3b the tree's averaged tail differs from the exact one only at O(1/U^2)",
    abs(tail_exact - tail_avg) < 4 * abs(A0 * A1v) / U ** 2)
chk("B4 (1/16pi^3) pi mu^4 = mu^4/(16 pi^2) = 3.169857938310467",
    abs(mu ** 4 / (16 * mp.pi ** 2) - mp.mpf('3.169857938310467')) < 1e-13, mp.nstr(mu ** 4 / (16 * mp.pi ** 2), 18))

# B5 guards
print("\n--- B5 hypothesis guards ---")
# (i) unclamped: g = sin(pi t) on [0,1]: g(0)=g(1)=0, g'(0)=pi, g'(1)=-pi
def ghat_sin(uu):
    # INT_0^1 sin(pi t) e^{-iut} dt, closed form
    return mp.pi * (1 + mp.exp(-1j * uu)) / (mp.pi ** 2 - uu ** 2)
# period-averaged: INT_U^{U+2pi} u^4|ghat|^2 du -> 4 pi^3 (a constant), so INT_0^U grows ~ 2 pi^2 U
per = [mp.quad(lambda uu: uu ** 4 * abs(ghat_sin(uu)) ** 2, [U0, U0 + 2 * mp.pi])
       for U0 in (mp.mpf(1e2), mp.mpf(1e3), mp.mpf(1e4))]
chk("B5i unclamped (g' != 0 at ends): INT over one period of u^4|ghat|^2 -> 4 pi^3 (does not decay); INT_0^oo diverges",
    all(abs(v / (4 * mp.pi ** 3) - 1) < 1e-2 for v in per), ", ".join(mp.nstr(v, 8) for v in per) + " vs 4pi^3=" + mp.nstr(4 * mp.pi ** 3, 8))
gpp_sin = mp.pi ** 4 / 2       # INT_0^1 (pi^2 sin pi t)^2 dt
chk("B5i' while pi INT_0^1 (g'')^2 is finite (= pi^5/2): identity FAILS without clamping",
    mp.isfinite(mp.pi * gpp_sin))
# (ii) complex g: g_w(t) = g(t) e^{i w t}; ghat_w(u) = ghat(u - w) (e^{-iut} convention)
c0 = [(1 - sg) / 2, (1 + sg) / 2, (-1 - 1j * sg) / 2, (-1 + 1j * sg) / 2]   # g = SUM c0 e^{aa t}
def ghat(v):
    s_ = 0
    for a, c in zip(aa, c0):
        z = a - 1j * v
        s_ += c * (mp.exp(z) - 1) / z
    return s_ / mp.sqrt(Ng)
chk("B5ii-pre ghat closed form: v^2 ghat(v) = -FT(g'')(v) at v = 2.5, 40",
    all(abs(-v ** 2 * ghat(v) - FT2(v)) < 1e-15 for v in (mp.mpf('2.5'), mp.mpf(40))))
w = mp.mpf(3)
G1n = lambda t: G1(t) / mp.sqrt(Ng)
Gn = lambda t: G(t) / mp.sqrt(Ng)
G2n = lambda t: G2(t) / mp.sqrt(Ng)
# g_w'' = (g'' + 2iw g' - w^2 g) e^{iwt}
gw2 = mp.quad(lambda t: (G2n(t) - w ** 2 * Gn(t)) ** 2 + (2 * w * G1n(t)) ** 2, [0, 0.5, 1])
fw = lambda uu: uu ** 4 * abs(ghat(uu - w)) ** 2
Lw = 400
pos_side = mp.fsum(mp.quad(fw, [a_, a_ + 1]) for a_ in range(0, Lw))
neg_side = mp.fsum(mp.quad(fw, [-a_ - 1, -a_]) for a_ in range(0, Lw))
tailw = (A0 ** 2 + A1v ** 2) / Lw          # |g_w''| at the ends = |g''| at the ends
pos_tot, neg_tot = pos_side + tailw, neg_side + tailw
print("    complex g_w (w=3): INT_0^oo ~ %s  INT_-oo^0 ~ %s  pi INT|g_w''|^2 = %s" % (
    mp.nstr(pos_tot, 10), mp.nstr(neg_tot, 10), mp.nstr(mp.pi * gw2, 10)))
chk("B5ii complex g: one-sided INT_0^oo != pi INT|g''|^2 (asymmetric halves)",
    abs(pos_tot - mp.pi * gw2) / (mp.pi * gw2) > 1e-2 and abs(pos_tot - neg_tot) / (mp.pi * gw2) > 1e-2)
chk("B5ii' but the two-sided Plancherel INT_R = 2 pi INT|g_w''|^2 still holds (to O(1/L^2))",
    abs(pos_tot + neg_tot - 2 * mp.pi * gw2) / (2 * mp.pi * gw2) < 1e-4,
    "rel " + mp.nstr(abs(pos_tot + neg_tot - 2 * mp.pi * gw2) / (2 * mp.pi * gw2), 3))
# (iii) convention: e^{+iut} vs e^{-iut}, real g
chk("B5iii |FT_{+}(g'')(u)| = |FT_{-}(g'')(u)| for real g (Fewster's e^{+iut} vs tree's e^{-iut})",
    all(abs(abs(FT2(uu, +1)) - abs(FT2(uu, -1))) < 1e-20 for uu in (mp.mpf('0.7'), mp.mpf(13), mp.mpf(250))))

print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS")
sys.exit(1 if FAIL else 0)
