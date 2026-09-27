#!/usr/bin/env python3
"""D67 re-derivation: modified spherical Bessel functions of the second kind k_l.

Tree's form (excite.py:709-724):  k_l(x) = e^{-x} p_l(1/x),
    p_l(y) = sum_{j=0}^{l} (l+j)!/(j!(l-j)!) (y/2)^j * y
Source form (DLMF 10.49.12, restated in Stoutemyer arXiv:2207.00707 Table 6 in
MathWorld normalisation): k_n^{DLMF}(x) = (pi/2) e^{-x} sum_k a_k(n+1/2) x^{-k-1},
    a_k(n+1/2) = (n+k)!/(2^k k! (n-k)!),  k_n^{DLMF} = sqrt(pi/(2x)) K_{n+1/2}(x).

Checks:
 C1  ALL l (symbolic in l): the tree's coefficients satisfy the two-term recurrence
     that is equivalent to R'' + 2R'/x - l(l+1)R/x^2 - R = 0, and the series
     terminates at j = l.  (Derivation of the recurrence re-checked by sympy on a
     single term e^{-x} x^{-n}.)
 C2  l = 0..12 exact residual by direct sympy differentiation (the tree does 0..5).
 C3  normalisation: (2/pi) sqrt(pi/(2x)) K_{l+1/2}(x) == tree k_l(x), mpmath 40 digits,
     l = 0..12 at several x; and sympy expand_func(besselk) where available.
 C4  Stoutemyer Table 6 rows n = 0..4 reproduced coefficient by coefficient.
 C5  rate: -R'/R = 1 + y + (l(l+1)/2) y^2 + O(y^3); limit 1 for every l (symbolic
     for general l to second order); the tree's datum 'within 1e-5 of 1 at x = 1e6'.
 C6  CONTROL: l^2 in place of l(l+1) leaves a nonzero residual (l = 1..5).
 C7  tail linearisation: (1/2) f (f+1)(f+2) = f + (3/2) f^2 + (1/2) f^3, so the
     linear operator of the tree's reduced equation is exactly (lap - 1).
 C8  dimension: in d dims the radial operator is f'' + (d-1)f'/x - l(l+d-2)f/x^2 - f;
     the tree's k_l solves it only for d = 3 (shown: residual nonzero for d = 2,4,5
     with l >= 1 or l = 0 as applicable), while x^{1-d/2} K_{l+d/2-1}(x) solves it
     for all d (numeric) and its log-derivative rate still -> 1.
 C9  domination: k_l(x) e^{x} x is decreasing in x (positive coefficients in 1/x),
     so for x >= X the multipole series is dominated termwise -- the interchange
     that carries 'rate -> 1' from each l to a convergent sum.  Checked for l<=12.
"""
import sympy as sp
import mpmath as mp
from fractions import Fraction
from math import factorial

x, y = sp.symbols('x y', positive=True)
l, k, n = sp.symbols('l k n', integer=True, nonnegative=True)
ok = True
def row(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

def a_tree(L, j):
    return sp.Rational(factorial(L + j), factorial(j) * factorial(L - j) * 2 ** j)

def k_tree(L):
    return sp.exp(-x) * sum(a_tree(L, j) * x ** (-(j + 1)) for j in range(L + 1))

# C1: single-term operator
LL = sp.Symbol('LL')
term = sp.exp(-x) * x ** (-n)
op = sp.diff(term, x, 2) + 2 * sp.diff(term, x) / x - LL * term / x ** 2 - term
expected = sp.exp(-x) * (2 * (n - 1) * x ** (-n - 1) + (n * (n - 1) - LL) * x ** (-n - 2))
row("C1a single-term operator e^{-x}x^{-n} -> 2(n-1)x^{-n-1} + (n(n-1)-L)x^{-n-2}",
    sp.simplify(op - expected) == 0)
# with n = j+1 the coefficient of x^{-k-2} is 2k a_k + (k(k-1) - l(l+1)) a_{k-1}
a = lambda kk: sp.factorial(l + kk) / (sp.factorial(kk) * sp.factorial(l - kk) * 2 ** kk)
ratio = sp.gammasimp(a(k) / a(k - 1))
need = (l * (l + 1) - k * (k - 1)) / (2 * k)
row("C1b general l: a_k/a_{k-1} = (l(l+1)-k(k-1))/(2k)  [symbolic in l,k]",
    sp.simplify(ratio - need) == 0)
row("C1c termination: l(l+1) - (l+1)l = 0, so a_{l+1} coefficient closes",
    sp.expand(l * (l + 1) - (l + 1) * l) == 0)

# C2 exact residual l = 0..12
res_ok = True
for L in range(13):
    R = k_tree(L)
    r = sp.simplify(sp.diff(R, x, 2) + 2 * sp.diff(R, x) / x - L * (L + 1) * R / x ** 2 - R)
    res_ok &= (r == 0)
row("C2 exact radial residual 0 for l = 0..12", res_ok)

# C3 normalisation against K_{l+1/2}
mp.mp.dps = 40
norm_ok = True
worst = mp.mpf(0)
for L in range(13):
    f = sp.lambdify(x, k_tree(L), 'mpmath')
    for xv in (mp.mpf('0.3'), mp.mpf(1), mp.mpf('7.5'), mp.mpf(40)):
        ref = (2 / mp.pi) * mp.sqrt(mp.pi / (2 * xv)) * mp.besselk(L + mp.mpf(1) / 2, xv)
        rel = abs(f(xv) / ref - 1)
        worst = max(worst, rel)
        norm_ok &= rel < mp.mpf(10) ** -30
row("C3 tree k_l == (2/pi) * DLMF k_l = (2/pi) sqrt(pi/2x) K_{l+1/2}, l<=12 (worst rel %s)"
    % mp.nstr(worst, 3), norm_ok)
try:
    s_ok = all(sp.simplify(sp.expand_func(sp.besselk(sp.Rational(2 * L + 1, 2), x))
                           * sp.sqrt(sp.pi / (2 * x)) * 2 / sp.pi - k_tree(L)) == 0
               for L in range(6))
    row("C3b sympy expand_func(besselk half-integer) agrees symbolically, l<=5", s_ok)
except Exception as e:
    print("SKIP C3b sympy besselk expand: %s" % e)

# C4 Stoutemyer Table 6 (MathWorld normalisation), coefficients of x^{-1..-(n+1)}
table6 = {0: [1], 1: [1, 1], 2: [1, 3, 3], 3: [1, 6, 15, 15], 4: [1, 10, 45, 105, 105]}
t_ok = all([a_tree(N, j) for j in range(N + 1)] == [sp.Integer(c) for c in table6[N]]
           for N in table6)
row("C4 Stoutemyer 2022 Table 6 rows n=0..4 reproduced exactly", t_ok)

# C5 rate
rate_ok = True
for L in range(13):
    R = k_tree(L)
    rate = sp.simplify(-sp.diff(R, x) / R)
    rate_ok &= sp.limit(rate, x, sp.oo) == 1
    ser = sp.series(rate.subs(x, 1 / y), y, 0, 3).removeO()
    rate_ok &= sp.simplify(ser - (1 + y + sp.Rational(L * (L + 1), 2) * y ** 2)) == 0
row("C5a -R'/R = 1 + 1/x + l(l+1)/(2x^2) + O(x^-3), limit 1, l = 0..12", rate_ok)
worst6 = max(abs(sp.N((-sp.diff(k_tree(L), x) / k_tree(L)).subs(x, 10 ** 6), 30) - 1)
             for L in range(6))
row("C5b tree datum: at x = 1e6, |rate - 1| < 1e-5 for l = 0..5 (max %s)" % sp.N(worst6, 8),
    worst6 < sp.Rational(1, 10 ** 5))

# C6 control
c_ok = all(sp.simplify(sp.diff(k_tree(L), x, 2) + 2 * sp.diff(k_tree(L), x) / x
                       - L * L * k_tree(L) / x ** 2 - k_tree(L)) != 0 for L in range(1, 6))
row("C6 CONTROL l^2 for l(l+1) leaves nonzero residual, l = 1..5", c_ok)

# C7 linearisation
f = sp.Symbol('f')
row("C7 (1/2)f(f+1)(f+2) = f + (3/2)f^2 + (1/2)f^3  (linear coefficient 1 = m^2 in x units)",
    sp.expand(sp.Rational(1, 2) * f * (f + 1) * (f + 2) - (f + sp.Rational(3, 2) * f ** 2
                                                           + f ** 3 / 2)) == 0)

# C8 dimension
def dres(R, L, d):
    return sp.simplify(sp.diff(R, x, 2) + (d - 1) * sp.diff(R, x) / x
                       - L * (L + d - 2) * R / x ** 2 - R)
d3 = all(dres(k_tree(L), L, 3) == 0 for L in range(4))
dn = all(dres(k_tree(L), L, d) != 0 for L in range(4) for d in (2, 4, 5))
row("C8a tree k_l solves the d-dim radial equation for d = 3 and NOT for d = 2,4,5 (l<=3)",
    d3 and dn)
gen_ok = True
for d in (2, 4, 5):
    for L in range(4):
        nu = L + mp.mpf(d) / 2 - 1
        g = lambda t: t ** (1 - mp.mpf(d) / 2) * mp.besselk(nu, t)
        for xv in (mp.mpf(1), mp.mpf(5)):
            r = (mp.diff(g, xv, 2) + (d - 1) * mp.diff(g, xv) / xv
                 - L * (L + d - 2) * g(xv) / xv ** 2 - g(xv))
            gen_ok &= abs(r / g(xv)) < mp.mpf(10) ** -20
        rate_big = -mp.diff(g, mp.mpf(10) ** 6) / g(mp.mpf(10) ** 6)
        gen_ok &= abs(rate_big - 1) < mp.mpf(10) ** -5
row("C8b x^{1-d/2} K_{l+d/2-1}(x) solves it for d = 2,4,5 and its rate -> 1 (x=1e6)", gen_ok)

# C9 monotone domination
dom_ok = True
for L in range(13):
    g = sp.expand(k_tree(L) * sp.exp(x) * x)
    dom_ok &= all(c > 0 for c in sp.Poly(g.subs(x, 1 / y), y).all_coeffs())
    dom_ok &= sp.limit(g, x, sp.oo) == 1
row("C9 k_l(x) e^x x = 1 + positive terms in 1/x: decreasing to 1, dominated for x >= X", dom_ok)

print("\nOVERALL: %s" % ("ALL PASS" if ok else "SOME FAIL"))
raise SystemExit(0 if ok else 1)
