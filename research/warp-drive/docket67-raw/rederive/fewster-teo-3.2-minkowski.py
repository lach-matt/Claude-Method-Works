#!/usr/bin/env python3
"""DOCKET 67 -- audit of Fewster & Teo gr-qc/9812032 eq. (3.2), the Minkowski form,
as fewsterteo.py (route 2 of section 1(a)) uses it.  sympy + mpmath.  READ-ONLY on the tree.

Published (3.2), pi glyphs restored (the alphaXiv text layer drops every pi:
'(2)^n' for (2 pi)^n on the same line):
  rho >= -(1/(2 pi)) INT_0^oo dw INT d^n k/(2 pi)^n w_k |(f^1/2)^(w + w_k)|^2
       = -(C_n/(2 pi)) INT_0^oo dw INT_mu^oo dw' w'^2 (w'^2-mu^2)^(n/2-1) |(f^1/2)^(w+w')|^2
The tree (fewsterteo.py:465) reads it as  -(1/2) INT d^n k/(2 pi)^n w_k S_k.
Checks:
 T1  the tree's route 2 reproduced: P = 1 against -(1/2); control norm=1 -> 1/2
 T2  the same solve against the pi-restored -(1/(2 pi)): P = 1/pi (the literal printed
     prefactor of (2.12)); route 1 with (2.10) read as -(1/(2 pi)) also gives 1/pi;
     so the tree's P is pi x the literal prefactor on BOTH routes (a common factor)
 T3  (3.2)'s second equality: the radial reduction with C_n of (3.3), n = 1..6
 T4  (3.4)/(3.5): the change of variables u = w + w', v = w', numerically (n=3, mu=1)
 T5  (2.18) re-derived: |(f^1/2)^|^2 = (4 t0/pi) K0(t0|w|)^2 for the Lorentzian (1.1)
 T6  THE DISCRIMINATOR: F&T's printed '9/64 of Ford and Roman' (p.7, legible) holds
     with (3.2)'s leading factor A = 1/(2 pi) and FAILS (9 pi/64) with A = 1/2
 T7  the tree's own (b) expression 1/(16 pi^3) = C_3/(2 pi (n+1)) carries the pi
"""
import sys
import sympy as sp
import mpmath as mp

res = []
def rec(name, ok, detail):
    res.append((name, bool(ok), detail))
    print("[%s] %s: %s" % ("PASS" if ok else "FAIL", name, detail))

# ---------- T1/T2: route 2, literally as fewsterteo.prefactor_route2 does it
W2, M2, LAP = sp.symbols('W2 M2 LAP')
b212 = W2 * M2 + LAP / 4
def route2(A, norm=2):
    n = sp.Symbol('n', positive=True, integer=True)
    P, w, S = sp.symbols('P omega_k S', positive=True)
    X = sp.symbols('x1:4', real=True); K = sp.symbols('k1:4', real=True)
    U = sp.exp(sp.I * sum(k * x for k, x in zip(K, X))) / sp.sqrt((2 * sp.pi) ** n * norm * w)
    mod2 = sp.simplify(sp.expand(U * sp.conjugate(U)))
    lap = sp.simplify(sum(sp.diff(mod2, x, 2) for x in X))
    lhs = -P * b212.subs({W2: w ** 2, M2: mod2, LAP: lap}) * S
    rhs = -A * w / (2 * sp.pi) ** n * S
    sol = sp.solve(sp.Eq(lhs, rhs), P)
    assert len(sol) == 1
    return sp.simplify(sol[0]), sp.simplify(lap)

P_tree, lap = route2(sp.Rational(1, 2))
rec("T1a tree route 2 against -(1/2): P", P_tree == 1, "P = %s; grad^2|U_k|^2 = %s (computed)" % (P_tree, lap))
P_ctl, _ = route2(sp.Rational(1, 2), norm=1)
rec("T1b tree control (norm 1)", P_ctl == sp.Rational(1, 2), "P = %s" % P_ctl)
P_pub, _ = route2(1 / (2 * sp.pi))
rec("T2a same solve against pi-restored -(1/(2 pi)): P", sp.simplify(P_pub - 1 / sp.pi) == 0, "P = %s" % P_pub)
MU2 = sp.Symbol('MU2')
b210 = sp.expand(W2 * M2 + (LAP / 2 + (W2 - MU2) * M2) + MU2 * M2)   # tree's route-1 on-shell form
P_r1_tree = sp.Rational(1, 2) * sp.simplify(b210 / b212)
P_r1_pub = (1 / (2 * sp.pi)) * sp.simplify(b210 / b212)
rec("T2b route 1: (2.10) read -(1/2) -> 1; read -(1/(2 pi)) -> 1/pi",
    P_r1_tree == 1 and sp.simplify(P_r1_pub - 1 / sp.pi) == 0,
    "tree %s, pi-restored %s" % (P_r1_tree, sp.simplify(P_r1_pub)))
rec("T2c tree P / literal P is the same factor on both routes (common pi)",
    sp.simplify(P_tree / P_pub - P_r1_tree / P_r1_pub) == 0, "ratio = %s on both" % sp.simplify(P_tree / P_pub))

# ---------- T3: radial reduction, C_n of (3.3)
kk, wp, mu = sp.symbols('k omega_p mu', positive=True)
okall = True; det = []
for n in range(1, 7):
    Cn = 1 / (2 ** (n - 1) * sp.pi ** sp.Rational(n, 2) * sp.gamma(sp.Rational(n, 2)))
    area = 2 * sp.pi ** sp.Rational(n, 2) / sp.gamma(sp.Rational(n, 2))
    ok1 = sp.simplify(Cn - area / (2 * sp.pi) ** n) == 0
    # INT d^n k/(2pi)^n w_k F(w_k) = area/(2pi)^n INT k^(n-1) w_k F dk ; k = sqrt(w'^2-mu^2), dk = w'/k dw'
    integrand_k = area / (2 * sp.pi) ** n * kk ** (n - 1) * sp.sqrt(kk ** 2 + mu ** 2)
    sub = sp.simplify(integrand_k.subs(kk, sp.sqrt(wp ** 2 - mu ** 2)) * wp / sp.sqrt(wp ** 2 - mu ** 2))
    target = Cn * wp ** 2 * (wp ** 2 - mu ** 2) ** (sp.Rational(n, 2) - 1)
    ok2 = sp.simplify(sp.powsimp(sub / target, force=True)) == 1
    okall &= ok1 and ok2; det.append("n=%d:%s" % (n, ok1 and ok2))
rec("T3 (3.2) second equality and (3.3) C_n", okall, " ".join(det))

# ---------- T4: (3.4)/(3.5) numerically, n=3, mu=1, F(u)=exp(-u)
mp.mp.dps = 30
n, m = 3, mp.mpf(1)
F = lambda u: mp.e ** (-u)
lhs = mp.quad(lambda w: mp.quad(lambda v: v ** 2 * (v ** 2 - m ** 2) ** (mp.mpf(n) / 2 - 1) * F(w + v), [m, mp.inf]), [0, mp.inf])
Qn = lambda x: (n + 1) * x ** (-(n + 1)) * mp.quad(lambda y: y ** 2 * (y ** 2 - 1) ** (mp.mpf(n) / 2 - 1), [1, x])
rhs = mp.quad(lambda u: F(u) * u ** (n + 1) * Qn(u / m), [m, mp.inf]) / (n + 1)
rec("T4 (3.4)/(3.5) change of variables", abs(lhs - rhs) / abs(rhs) < mp.mpf(10) ** -20, "lhs %s rhs %s" % (mp.nstr(lhs, 15), mp.nstr(rhs, 15)))

# ---------- T5: (2.18) for the Lorentzian (1.1), t0 = 1
t0 = mp.mpf(1)
worst = 0
for om in (mp.mpf('0.3'), mp.mpf(1), mp.mpf('2.5')):
    ft = 2 * mp.quadosc(lambda t: mp.sqrt(t0 / mp.pi / (t ** 2 + t0 ** 2)) * mp.cos(om * t), [0, mp.inf], omega=om)
    want = 4 * t0 / mp.pi * mp.besselk(0, t0 * om) ** 2
    worst = max(worst, abs(ft ** 2 - want) / want)
rec("T5 (2.18) |(f^1/2)^|^2 = (4 t0/pi) K0^2 re-derived", worst < mp.mpf(10) ** -15, "worst rel %s" % mp.nstr(worst, 3))

# ---------- T6: the discriminator, massless n = 3, Lorentzian sampler
t = sp.Symbol('t_0', positive=True)
C3 = 1 / (2 ** 2 * sp.pi ** sp.Rational(3, 2) * sp.gamma(sp.Rational(3, 2)))
I4 = 2 ** 2 * sp.gamma(sp.Rational(5, 2)) ** 4 / sp.gamma(5)        # INT x^4 K0^2, F&T (6.9) at alpha=5/2
I4num = mp.quad(lambda x: x ** 4 * mp.besselk(0, x) ** 2, [0, 1, 10, 100, mp.inf])
FR = sp.Rational(3, 32) / (sp.pi ** 2 * t ** 4)                  # Ford-Roman (1.2)
def bound(A):  # (3.4) massless: Q_3 -> 1; A = leading factor of (3.2)
    return A * C3 / 4 * (4 * t / sp.pi) * I4 / t ** 5
r_pub = sp.nsimplify(sp.simplify(bound(1 / (2 * sp.pi)) / FR))
r_tree = sp.nsimplify(sp.simplify(bound(sp.Rational(1, 2)) / FR))
rec("T6a INT x^4 K0^2 = 27 pi^2/512 (quadrature)", abs(I4num - mp.mpf(27) * mp.pi ** 2 / 512) < mp.mpf(10) ** -20, mp.nstr(I4num, 20))
rec("T6b A = 1/(2 pi): ratio to Ford-Roman = printed 9/64", r_pub == sp.Rational(9, 64), "ratio = %s" % r_pub)
rec("T6c A = 1/2 (the tree's quotation) would give 9 pi/64, NOT the printed 9/64",
    sp.simplify(r_tree - 9 * sp.pi / 64) == 0, "ratio = %s = %.6f" % (r_tree, float(r_tree)))

# ---------- T7: the tree's own (b) prefactor
rec("T7 tree (b)'s 1/(16 pi^3) = C_3/(2 pi (n+1)) -- the pi-bearing form",
    sp.simplify(C3 / (2 * sp.pi * 4) - 1 / (16 * sp.pi ** 3)) == 0, "C_3 = %s" % sp.simplify(C3))

# ---------- T8: later restatements. Fewster math-ph/0501073 eq.(7) and Fewster-Smith
# gr-qc/0702056 eq.(88) print -(1/16 pi^3) INT u^4 |g^(u)|^2 du (massless); Kontou-Sanders
# 2003.01815 eq.(61) prints -(1/16 pi^2) INT |g''|^2 dt.  Consistent iff INT_0^oo u^4|g^|^2 du
# = pi INT g''^2 dt (Parseval, real g).  Checked on a Gaussian g = exp(-t^2).
g2 = mp.quad(lambda tt: mp.diff(lambda s: mp.e ** (-s ** 2), tt, 2) ** 2, [-mp.inf, mp.inf])
ghat = lambda u: mp.sqrt(mp.pi) * mp.e ** (-u ** 2 / 4)
lhs8 = mp.quad(lambda u: u ** 4 * ghat(u) ** 2, [0, mp.inf])
rec("T8 later restatements agree: (1/16pi^3) INT_0^oo u^4|g^|^2 = (1/16pi^2) INT g''^2",
    abs(lhs8 / (16 * mp.pi ** 3) - g2 / (16 * mp.pi ** 2)) < mp.mpf(10) ** -20,
    "%s vs %s" % (mp.nstr(lhs8 / (16 * mp.pi ** 3), 15), mp.nstr(g2 / (16 * mp.pi ** 2), 15)))

npass = sum(ok for _, ok, _ in res)
print("\n%d/%d PASS" % (npass, len(res)))
sys.exit(0 if npass == len(res) else 1)
