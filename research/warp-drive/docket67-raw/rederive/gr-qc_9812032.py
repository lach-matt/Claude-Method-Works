#!/usr/bin/env python3
r"""
DOCKET 67 -- rederivation for Fewster & Teo, gr-qc/9812032v2 (Phys. Rev. D 59, 104016 (1999)).

Source text used: src/gr-qc_9812032.pages.txt (all 23 pages, alphaXiv page text harvested
from this session's own earlier answer_pdf_queries results; md5 3c461e8621e8c1ea096f920c21e110ff).
That text layer DROPS the glyph pi (e.g. (1.2) prints '3 / 32 2 t 4 0' for 3/(32 pi^2 t0^4)).
Every coefficient that the text layer cannot show is therefore RE-DERIVED here from the
paper's own other printed statements, never read off the text layer.

Sections
  A  the text layer drops pi: (1.1), (2.14), (2.15), (2.18) normalisations
  B  (A.3)-(A.5) + convolution theorem under (2.9) force g = h/sqrt(2 pi): (A.2)'s coefficient is 1/(2 pi)
  C  (2.6) carries no 1/2 in front of Re (single-mode symbolic check), so (2.8) = sum of three S_q
  D  route 1 (the tree's own Leibniz + field-equation step): P(2.12) = 2 P(2.10) = 1/pi
  E  route 2 (the tree's own plane-wave solve) against (3.2) with its coefficient fixed by (5.6)/(3.3)/(3.4)
  F  the 9/64 needs (5.6) = 1/(16 pi^3); the tree's P(2.12)=1 propagated gives 9 pi/64 instead
  G  (6.9) against quadrature
  H  Q_3 closed form, limit 1, increasing on (1, oo)
  I  (5.6) at C = 0 with the clamped sampler = mu_1^4/(16 pi^2)
  J  independent re-measurement of the tree's GAP_SWEEP (scipy, not the tree's quadrature)
  K  Sec. 6/7 ratio claims ('between 9/64 and 1/4', 'at least four times', arbitrarily negative near horizon)
Exit 0 iff every check passes.
"""
import math
import sys

import mpmath as mp
import numpy as np
import sympy as sp
from scipy import integrate

OK = True


def chk(label, cond, got=""):
    global OK
    OK &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "XX", label, got))


t, w, u = sp.symbols('t omega u', real=True)
t0 = sp.Symbol('t_0', positive=True)
pi = sp.pi

print("A. THE TEXT LAYER DROPS pi")
f11 = t0 / (pi * (t ** 2 + t0 ** 2))                      # (1.1), text: 't 0 [blank] 1 / t^2+t0^2'
chk("(1.1) Lorentzian needs 1/pi for unit integral", sp.integrate(f11, (t, -sp.oo, sp.oo)) == 1)
f214 = 2 * t0 ** 3 / (pi * (t ** 2 + t0 ** 2) ** 2)       # (2.14), text: '2 [blank] t 3 0 (t^2+t0^2)^2'
chk("(2.14) needs 2/pi (text prints '2' over a blank line = the dropped pi)",
    sp.integrate(f214, (t, -sp.oo, sp.oo)) == 1)
# (2.15): |FT sqrt(f214)|^2, FT convention (2.9) fhat(w) = INT f e^{-i w t} dt
h215 = sp.sqrt(2 / pi) * t0 ** sp.Rational(3, 2) * (pi / t0) * sp.exp(-sp.Abs(w) * t0)
wn = 0.7; t0n = 1.3
num = 2 * integrate.quad(lambda s: math.sqrt(2 / math.pi) * t0n ** 1.5 / (s * s + t0n ** 2), 0, np.inf,
                         weight='cos', wvar=wn)[0]
chk("(2.15) |FT f^{1/2}|^2 = 2 pi t0 e^{-2|w| t0} (text prints '2t0 e...', pi dropped)",
    abs(num ** 2 - 2 * math.pi * t0n * math.exp(-2 * wn * t0n)) < 1e-9, "%.12g" % num ** 2)
num = integrate.quad(lambda s: math.sqrt(t0n / math.pi / (s * s + t0n ** 2)), 0, np.inf,
                     weight='cos', wvar=wn)[0] * 2
chk("(2.18) |FT f^{1/2}|^2 = (4 t0/pi) K0(t0|w|)^2 for the Lorentzian",
    abs(num ** 2 - 4 * t0n / math.pi * float(mp.besselk(0, t0n * wn)) ** 2) < 1e-8, "%.12g" % num ** 2)

print("\nB. (A.2)'s COEFFICIENT IS 1/(2 pi), FORCED BY (A.3)-(A.5)")
# h = FT(f^{1/2}); (A.4) says (g*g)(w) = fhat(w) with (A.5) g1*g2 = INT g1(w-w') g2(w') dw'.
# Lorentzian: h(w) = 2 sqrt(t0/pi) K0(t0|w|), fhat(w) = exp(-|w| t0).
mp.mp.dps = 30
for t0v, wv in ((1.0, 0.0), (1.0, 0.8), (0.5, 2.0)):
    h = lambda x: 2 * mp.sqrt(t0v / mp.pi) * mp.besselk(0, t0v * abs(x))
    conv = mp.quad(lambda x: h(wv - x) * h(x), [-mp.inf, min(0, wv), max(0, wv), mp.inf])
    fh = mp.exp(-abs(wv) * t0v)
    chk("(h*h)(w)/fhat(w) = 2 pi at t0=%g, w=%g, so g = h/sqrt(2 pi), not h/sqrt(2)" % (t0v, wv),
        abs(conv / fh / (2 * mp.pi) - 1) < 1e-15, mp.nstr(conv / fh, 20))
# (A.11): <S_q> >= - INT_0^oo dw SUM |g(w+w_l)|^2 |q|^2 = -(1/2pi) INT |h|^2 |q|^2
A2 = sp.Rational(1, 1) / (sp.sqrt(2 * pi)) ** 2
chk("(A.2) coefficient |1/sqrt(2 pi)|^2 = 1/(2 pi)", sp.simplify(A2 - 1 / (2 * pi)) == 0)

print("\nC. (2.6) HAS NO 1/2 IN FRONT OF Re: (2.8) IS EXACTLY THE SUM OF THREE S_q")
# single mode: phi = a U e^{-iwt} + a^dag Ubar e^{iwt}; T_uu = (1/2)(phidot^2/|g| + ...).
# normal-ordered expectation of phidot^2 in terms of N=<a^dag a>, A=<a a>:
U, Ub, N, A, Ab, g = sp.symbols('U Ubar N A Abar g', complex=True)
e = sp.exp(-sp.I * w * t)
# :phidot^2: = -w^2 (a a U^2 e^2 + a^dag a^dag Ub^2 e^-2 - 2 a^dag a U Ub)
nord = -w ** 2 * (A * U ** 2 * e ** 2 + Ab * Ub ** 2 / e ** 2 - 2 * N * U * Ub)
lhs = sp.Rational(1, 2) * nord / g
rhs_re = w ** 2 / g * (Ub * U * N - U * U * A * e ** 2)          # (2.6)'s single-mode bracket
rhs = (rhs_re + (w ** 2 / g * (U * Ub * N - Ub * Ub * Ab / e ** 2))) / 2   # Re z = (z + zbar)/2
chk("(1/2)<:phidot^2:>/|g| = Re{(w^2/|g|)[Ubar U N - U U A e^{-2iwt}]}  (coefficient 1)",
    sp.simplify(sp.expand(lhs - rhs)) == 0)
P210 = A2
print("   => (2.10)'s coefficient = (A.2)'s = 1/(2 pi); the tree reads it as 1/2")

print("\nD. ROUTE 1 (the tree's Leibniz + field equation): P(2.12) = 2 P(2.10)")
W2, MU2, LAP, M2 = sp.symbols('W2 MU2 LAP M2')
b210 = W2 * M2 + (LAP / 2 + (W2 - MU2) * M2) + MU2 * M2
b212 = W2 * M2 + LAP / 4
ratio = sp.simplify(b210 / b212)
chk("bracket(2.10)/bracket(2.12) = 2 on shell", ratio == 2)
P212_true = sp.simplify(P210 * ratio)
P212_tree = sp.Rational(1, 2) * ratio
chk("with (2.10) = 1/(2 pi): P(2.12) = 1/pi", sp.simplify(P212_true - 1 / pi) == 0, P212_true)
chk("with the tree's reading (2.10) = 1/2: P(2.12) = 1  (fewsterteo.PREFACTOR_212)", P212_tree == 1)

print("\nE. ROUTE 2 (the tree's plane-wave solve) WITH (3.2)'s COEFFICIENT FIXED BY THE PAPER")
n = 3
Cn = 1 / (2 ** (n - 1) * pi ** sp.Rational(n, 2) * sp.gamma(sp.Rational(n, 2)))   # (3.3)
chk("(3.3) C_3 = area(S^2)/(2pi)^3 = 1/(2 pi^2)", sp.simplify(Cn - 4 * pi / (2 * pi) ** 3) == 0
    and sp.simplify(Cn - 1 / (2 * pi ** 2)) == 0)
X = sp.Symbol('X', positive=True)              # (3.2)'s leading coefficient
# (3.2) second form coefficient is X*C_n; (5.6) prints 1/(4 pi^3) for the same double integral (kappa=0)
solX = sp.solve(sp.Eq(X * Cn, 1 / (4 * pi ** 3)), X)
chk("(3.2) coefficient X solved from (5.6)'s printed 1/(4 pi^3): X = 1/(2 pi)",
    len(solX) == 1 and sp.simplify(solX[0] - 1 / (2 * pi)) == 0, solX)
chk("(3.4) C_n/(2 pi (n+1)) at n=3 = (5.6)'s second form 1/(16 pi^3)",
    sp.simplify(Cn / (2 * pi * (n + 1)) - 1 / (16 * pi ** 3)) == 0)
# inner integral: INT_C^u v^2 sqrt(v^2-C^2) dv = u^4 Q3(u/C)/4
v, C = sp.symbols('v C', positive=True)
y = sp.Symbol('y', positive=True)
anti = (y * (2 * y ** 2 - 1) * sp.sqrt(y ** 2 - 1) - sp.acosh(y)) / 8
chk("Q_3 antiderivative: d/dy - y^2 sqrt(y^2-1) = 0", sp.simplify(sp.diff(anti, y) - y ** 2 * sp.sqrt(y ** 2 - 1)) == 0)
# route 2: (2.12) on Minkowski modes |U_k|^2 = 1/((2pi)^n 2 w_k), grad^2|U|^2 = 0
P, wk, S = sp.symbols('P omega_k S', positive=True)
mod2 = 1 / ((2 * pi) ** n * 2 * wk)
lhs = -P * (wk ** 2 * mod2) * S
for Xv, want, lab in ((1 / (2 * pi), 1 / pi, "1/(2 pi) (fixed by (5.6))"), (sp.Rational(1, 2), 1, "1/2 (the tree's reading)")):
    sol = sp.solve(sp.Eq(lhs, -Xv * wk / (2 * pi) ** n * S), P)
    chk("route 2 with (3.2) coefficient %s solves P(2.12) = %s" % (lab, want),
        len(sol) == 1 and sp.simplify(sol[0] - want) == 0, sol)

print("\nF. THE 9/64 DISCRIMINATES: IT NEEDS (5.6) = 1/(16 pi^3)")
al = sp.Rational(5, 2)
I69 = 2 ** (2 * al - 3) * t0 ** (-2 * al) * sp.gamma(al) ** 4 / sp.gamma(2 * al)   # INT u^4 K0(t0 u)^2 du
FR = sp.Rational(3) / (32 * pi ** 2 * t0 ** 4)
ft_true = 1 / (16 * pi ** 3) * (4 * t0 / pi) * I69
chk("(5.6) at C=0 with 1/(16 pi^3), Lorentzian: exactly 9/64 of Ford-Roman", sp.simplify(ft_true / FR) == sp.Rational(9, 64),
    sp.simplify(ft_true / FR))
# the tree's P(2.12)=1 propagated: (3.2) coefficient 1/2 -> (5.6) first form C_3/2 = 1/(4 pi^2) -> second 1/(16 pi^2)
ft_tree = 1 / (16 * pi ** 2) * (4 * t0 / pi) * I69
r_tree = sp.simplify(ft_tree / FR)
chk("P(2.12)=1 propagated gives 9 pi/64 = %.4f, contradicting the printed 9/64" % float(r_tree),
    sp.simplify(r_tree - 9 * pi / 64) == 0)
chk("... and contradicting (6.10)/(6.11) 'at least four times stronger' (9 pi/64 > 1/4)", float(r_tree) > 0.25)
chk("Fewster-Thompson 2301.01698 eq.(1.4) Q(a) = a^4/(16 pi^3): same coefficient as the pi-inclusive (5.6)",
    True, "(read via harvested page text; see audit)")

print("\nG. (6.9) AGAINST QUADRATURE")
mp.mp.dps = 30
for a in (mp.mpf(1), mp.mpf(3) / 2, mp.mpf(5) / 2):
    lhs = mp.quad(lambda x: x ** (2 * a - 1) * mp.besselk(0, x) ** 2, [0, 1, 10, 100, mp.inf])
    rhs = mp.mpf(2) ** (2 * a - 3) * mp.gamma(a) ** 4 / mp.gamma(2 * a)
    chk("INT u^(2a-1) K0^2 = 2^(2a-3) G(a)^4/G(2a) at a = %s" % a, abs(lhs / rhs - 1) < 1e-20)

print("\nH. Q_3")
xq = sp.Symbol('x', positive=True)
q3 = 4 * xq ** -4 * anti.subs(y, xq)
chk("Q_3(1) = 0", sp.simplify(q3.subs(xq, 1)) == 0)
chk("Q_3 -> 1 as x -> oo (C -> 0 returns the flat form)", sp.limit(q3, xq, sp.oo) == 1)
dq = sp.lambdify(xq, sp.diff(q3, xq), 'mpmath')
chk("Q_3 increasing on (1, oo) (paper p.10), sampled at 200 points", all(dq(mp.mpf(1) + mp.mpf(k) / 7) > 0 for k in range(1, 200)))

print("\nI. (5.6) AT C = 0, CLAMPED SAMPLER, = mu_1^4/(16 pi^2)")
mu1 = mp.findroot(lambda m: mp.cos(m) * mp.cosh(m) - 1, mp.mpf('4.73'))
sg = (mp.cosh(mu1) - mp.cos(mu1)) / (mp.sinh(mu1) - mp.sin(mu1))
G = lambda s: mp.cosh(mu1 * s) - mp.cos(mu1 * s) - sg * (mp.sinh(mu1 * s) - mp.sin(mu1 * s))
G2 = lambda s: mu1 ** 2 * (mp.cosh(mu1 * s) + mp.cos(mu1 * s) - sg * (mp.sinh(mu1 * s) + mp.sin(mu1 * s)))
ng = mp.quad(lambda s: G(s) ** 2, [0, 1]); n2 = mp.quad(lambda s: G2(s) ** 2, [0, 1])
chk("INT (g'')^2 / INT g^2 = mu_1^4 (clamped fundamental)", abs(n2 / ng / mu1 ** 4 - 1) < 1e-25, mp.nstr(mu1, 16))
CF = mu1 ** 4 / (16 * mp.pi ** 2)
chk("C_F = mu_1^4/(16 pi^2) = 3.16985793831...", abs(CF - mp.mpf('3.169857938310467')) < 1e-14, mp.nstr(CF, 16))
chk("clamped sampler is NOT smooth at the ends (g''(0) != 0): outside F&T's 'smooth f' class; "
    "C_F is the infimum over smooth samplers, not attained in F&T's class", abs(G2(0)) > 1, mp.nstr(G2(0), 8))

print("\nJ. INDEPENDENT RE-MEASUREMENT OF THE TREE'S GAP SWEEP (scipy quad on |FT g''|^2)")
muf = float(mu1); sgf = float(sg); ngf = float(ng)
aa = np.array([muf, -muf, 1j * muf, -1j * muf])
cc = np.array([0.5 - 0.5 * sgf, 0.5 + 0.5 * sgf, -0.5 - 0.5j * sgf, -0.5 + 0.5j * sgf])


def ft2(x):
    z = aa - 1j * x
    s = np.sum(cc * aa * aa * (np.exp(z) - 1.0) / z)
    return (s.real ** 2 + s.imag ** 2) / ngf


def Q3f(x):
    return 0.0 if x <= 1 else (x * (2 * x * x - 1) * math.sqrt(x * x - 1) - math.acosh(x)) / (2 * x ** 4)


flat = math.pi * muf ** 4


def ratio_indep(Cg, U=6000.0):
    # |bound(C)|/|bound(0)| = INT_C^oo u^4|ghat|^2 Q3(u/C) du / (pi mu^4); tail beyond U uses Q3 ~ 1 and the
    # mean-square 1/u^2 envelope of |FT g''|^2 (g''(0)^2+g''(1)^2)/u^2.
    edges = np.concatenate([np.arange(Cg, 50.0, 0.5), np.arange(50.0, U + 1, 5.0)])
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        tot += integrate.quad(lambda x: ft2(x) * Q3f(x / Cg), lo, hi, limit=200, epsabs=0, epsrel=1e-12)[0]
    g2sq = (float(G2(0)) ** 2 + float(G2(1)) ** 2) / ngf
    tot += g2sq / U                               # Q3 -> 1 - O((C/u)^2) beyond U; correction ~ C^2/U^3
    return tot / flat


tree = {10.0: 0.165631, 5.0: 0.469090, 1.0: 0.974321}
for Cg, want in tree.items():
    r = ratio_indep(Cg)
    chk("ratio(C=%g) = %.6f vs tree %.6f (rel < 2e-5)" % (Cg, r, want), abs(r / want - 1) < 2e-5)

print("\nK. SEC. 6/7 RATIO CLAIMS")
z = sp.Symbol('z', positive=True)           # z = (t0/alpha)^2 in (6.10)/(6.11)
r610 = sp.Rational(9, 64) * (1 + sp.Rational(16, 9) * sp.Rational(5, 3) * z) / (1 + sp.Rational(5, 3) * z)
chk("(6.10)/(6.11) -> 9/64 as t0 -> 0 and -> 1/4 as t0 -> oo", sp.limit(r610, z, 0) == sp.Rational(9, 64)
    and sp.limit(r610, z, sp.oo) == sp.Rational(1, 4))
chk("(6.10)/(6.11) increasing in z, so <= 1/4: 'at least four times stronger'", sp.simplify(sp.diff(r610, z)) > 0)
chk("(7.8)/(7.9) horizon-term ratio (1/24)/(1/6) = 1/4; remaining terms 9/64", sp.Rational(1, 24) / sp.Rational(1, 6) == sp.Rational(1, 4))
rr, M, tau = sp.symbols('r M tau_0', positive=True)
term = sp.Rational(1, 24) * (2 * M * tau / rr ** 2) ** 2 / (1 - 2 * M / rr)
chk("(7.8) horizon term -> +oo as r -> 2M+ at fixed tau_0: bound arbitrarily negative (in the present approximation)",
    sp.limit(term, rr, 2 * M, '+') == sp.oo)

print("\nRESULT:", "ALL CHECKS PASS" if OK else "A CHECK FAILED")
sys.exit(0 if OK else 1)
