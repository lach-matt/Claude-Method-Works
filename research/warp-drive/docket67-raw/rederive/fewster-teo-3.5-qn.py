#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: Fewster & Teo gr-qc/9812032 eq. (3.5), Q_n at n = 3,
as used by research/warp-drive/fewsterteo.py (Q3, ratio).

Source as READ (alphaXiv page text, gr-qc/9812032v2 p.7, cached at
d67/src/gr-qc_9812032.cached.txt):
    (3.5)  Q_n(x) = (n+1) x^{-(n+1)} INT_1^x dy y^2 (y^2-1)^{n/2-1}
    (3.4)  bound = -C_n/(2 pi (n+1)) INT_mu^oo du |f^_{1/2}(u)|^2 u^{n+1} Q_n(u/mu)
           [text layer prints "2(n+1)"; it drops every pi -- see check 5]
    (3.3)  C_n = area(S^{n-1})/(2 pi)^n
    (5.5)  bound = -(1/(4 pi^3 a^3)) INT_0^oo dw INT_0^oo dq w_q q^2 |f^(w+w_q)|^2,
           w_q = sqrt((q^2+1)/a^2 + mu^2)   (minimal coupling, F&T (2.2))
    (5.6)  = -(1/4pi^3) INT_0^oo dw INT_C^oo dw' w'^2 sqrt(w'^2-C^2) |f^(w+w')|^2
           = -(1/16 pi^3) INT_C^oo du |f^(u)|^2 u^4 Q_3(u/C)
    (5.7)  C = sqrt(kappa/a^2 + mu^2), kappa = 0 Minkowski, 1 open universe.
Independent restatement (Fewster math-ph/0501073 eq. (8), same cache):
    Q_3(x) = (1-1/x^2)^{1/2}(1-1/(2x^2)) - (1/(2x^4)) ln(x + sqrt(x^2-1)),
    0 <= Q_3 <= 1, Q_3 -> 1.

Nothing under research/ is imported or executed: the tree's Q3 is lifted by ast
from fewsterteo.py and exec'd alone (no bytecode written into the tree).
"""
import ast
import math
import sys

import mpmath as mp
import sympy as sp

TREE = "/home/user/Claude-Method-Works/research/warp-drive/fewsterteo.py"
rows = []


def rec(label, ok, detail=""):
    rows.append((label, bool(ok), detail))
    print("%-4s %s %s" % ("OK" if ok else "FAIL", label, detail))


x, y = sp.symbols("x y", positive=True)
n = sp.Symbol("n", positive=True)

# 1. (3.5) at n = 3 is the tree's integral definition
Qn = (n + 1) * x ** (-(n + 1)) * sp.Integral(y ** 2 * (y ** 2 - 1) ** (n / 2 - 1), (y, 1, x))
Q3_def = Qn.subs(n, 3)
tree_def = 4 * x ** -4 * sp.Integral(y ** 2 * sp.sqrt(y ** 2 - 1), (y, 1, x))
rec("1  (3.5) at n=3 == tree's 4 x^-4 INT_1^x y^2 sqrt(y^2-1) dy",
    sp.simplify(Q3_def - tree_def) == 0)

# 2. the tree's antiderivative (its datum) differentiates to the integrand, vanishes at 1
anti = (y * (2 * y ** 2 - 1) * sp.sqrt(y ** 2 - 1) - sp.acosh(y)) / 8
rec("2a d/dy anti - y^2 sqrt(y^2-1) == 0",
    sp.simplify(sp.diff(anti, y) - y ** 2 * sp.sqrt(y ** 2 - 1)) == 0)
rec("2b anti(1) == 0", sp.simplify(anti.subs(y, 1)) == 0)
Q3_closed = 4 * x ** -4 * anti.subs(y, x)

# 3. against the independent restatement (Fewster 2005, eq. (8))
Q3_f05 = sp.sqrt(1 - 1 / x ** 2) * (1 - 1 / (2 * x ** 2)) - sp.log(x + sp.sqrt(x ** 2 - 1)) / (2 * x ** 4)
diff3 = sp.simplify((Q3_closed - Q3_f05).rewrite(sp.log))
num3 = max(abs(float((Q3_closed - Q3_f05).subs(x, v))) for v in (1.0001, 1.5, 3, 35.355, 1e3))
rec("3  tree closed form == Fewster math-ph/0501073 eq.(8)", diff3 == 0 or num3 < 1e-14,
    "symbolic residual %s, max numeric |diff| %.2e" % (diff3, num3))

# 4. limits and monotonicity (F&T p.10: 'Q_3 is an increasing function on [1,oo)')
rec("4a Q_3(1) == 0", sp.limit(Q3_closed, x, 1, "+") == 0)
rec("4b Q_3 -> 1 as x -> oo", sp.limit(Q3_closed, x, sp.oo) == 1)
# Q3' > 0 <=> h(x) = x^3 sqrt(x^2-1) - 4 INT_1^x y^2 sqrt(y^2-1) dy > 0; h(1)=0 and
h = x ** 3 * sp.sqrt(x ** 2 - 1) - 4 * anti.subs(y, x)
hp = sp.simplify(sp.diff(h, x))
rec("4c h'(x) == x^2/sqrt(x^2-1) > 0 on (1,oo), h(1)=0 => Q_3 strictly increasing",
    sp.simplify(hp - x ** 2 / sp.sqrt(x ** 2 - 1)) == 0 and sp.simplify(h.subs(x, 1)) == 0,
    "h' = %s" % hp)
dQ = sp.simplify(sp.diff(Q3_closed, x) - 4 * h / x ** 5)
rec("4d Q_3'(x) == 4 h(x)/x^5 (identity used by 4c)", dQ == 0)
rec("4e 0 <= Q_3 <= 1 on sampled grid",
    all(0 <= float(Q3_closed.subs(x, v)) <= 1 for v in (1.0000001, 1.01, 2, 10, 1e4)))

# 5. normalisation chain (3.3)->(3.4)->(5.6) at n = 3: C_3 = 1/(2pi^2)
C3 = 2 * sp.pi ** sp.Rational(3, 2) / sp.gamma(sp.Rational(3, 2)) / (2 * sp.pi) ** 3
rec("5a C_3 = area(S^2)/(2pi)^3 = 1/(2 pi^2)", sp.simplify(C3 - 1 / (2 * sp.pi ** 2)) == 0)
pref_with_pi = sp.simplify(C3 / (2 * sp.pi * 4))
pref_text = sp.simplify(C3 / (2 * 4))
rec("5b (3.4) prefactor C_n/(2 pi (n+1)) at n=3 == (5.6)'s 1/(16 pi^3)",
    sp.simplify(pref_with_pi - 1 / (16 * sp.pi ** 3)) == 0,
    "text-layer reading C_n/(2(n+1)) gives %s: a DROPPED-pi TEXT-LAYER DISCREPANCY, not a paper error" % pref_text)

# 6. (5.6) first form -> Q_3 form: INT_C^u v^2 sqrt(v^2-C^2) dv == u^4 Q_3(u/C)/4
u, v, C = sp.symbols("u v C", positive=True)
inner = C ** 4 * anti.subs(y, u / C)   # v = C y
rec("6a d/du [u^4 Q_3(u/C)/4] == u^2 sqrt(u^2-C^2)",
    sp.simplify(sp.diff((u ** 4 * Q3_closed.subs(x, u / C) / 4), u) - u ** 2 * sp.sqrt(u ** 2 - C ** 2)) == 0)
rec("6b C^4 anti(u/C) == u^4 Q_3(u/C)/4", sp.simplify(inner - u ** 4 * Q3_closed.subs(x, u / C) / 4) == 0)
rec("6c (1/4pi^3)*(1/4) == 1/(16 pi^3)", sp.Rational(1, 4) / (4 * sp.pi ** 3) == 1 / (16 * sp.pi ** 3))

# 7. (5.5) -> (5.6) first form: change q -> w' = w_q, w_q = sqrt((q^2+1)/a^2+mu^2)
a, mu, q, w = sp.symbols("a mu q w", positive=True)
Cc = sp.sqrt(1 / a ** 2 + mu ** 2)
qofw = a * sp.sqrt(w ** 2 - Cc ** 2)
jac = sp.diff(qofw, w)
integrand = sp.simplify((w * qofw ** 2 * jac) / a ** 3)
rec("7  (1/a^3) w_q q^2 dq == w'^2 sqrt(w'^2-C^2) dw', C = sqrt(1/a^2+mu^2) (open, kappa=1)",
    sp.simplify(integrand - w ** 2 * sp.sqrt(w ** 2 - Cc ** 2)) == 0)

# 8. numeric: the two sides of (5.6) for a Gaussian test |f^|^2 = exp(-u^2)
mp.mp.dps = 25
F = lambda s: mp.e ** (-s * s)
Q3n = lambda X: 0 if X <= 1 else (X * (2 * X * X - 1) * mp.sqrt(X * X - 1) - mp.acosh(X)) / (2 * X ** 4)
for Cv in (0.3, 1.0, 2.5):
    lhs = mp.quad(lambda om: mp.quad(lambda wp: wp ** 2 * mp.sqrt(wp ** 2 - Cv ** 2) * F(om + wp),
                                     [Cv, Cv + 1, mp.inf]), [0, 1, mp.inf]) / (4 * mp.pi ** 3)
    rhs = mp.quad(lambda s: F(s) * s ** 4 * Q3n(s / Cv), [Cv, Cv + 1, mp.inf]) / (16 * mp.pi ** 3)
    rec("8  (5.6) both forms agree numerically, Gaussian, C=%g" % Cv, abs(lhs - rhs) < 1e-15 * max(1, abs(lhs)) + 1e-18,
        "lhs %s rhs %s" % (mp.nstr(lhs, 15), mp.nstr(rhs, 15)))
    # CONTROL: a wrong exponent in (3.5) ((y^2-1)^{n/2} at n=3) must break the equality
    Qbad = lambda X: 0 if X <= 1 else 4 * X ** -4 * mp.quad(lambda t: t * t * (t * t - 1) ** 1.5, [1, X])
    bad = mp.quad(lambda s: F(s) * s ** 4 * Qbad(s / Cv), [Cv, Cv + 1, mp.inf]) / (16 * mp.pi ** 3)
    rec("8c CONTROL fires: wrong-exponent Q breaks (5.6) at C=%g" % Cv, abs(bad - lhs) > 1e-6 * abs(lhs))

# 9. the tree's Q3 function (lifted by ast, exec'd alone) vs direct quadrature of (3.5)
src = open(TREE).read()
fn = [nd for nd in ast.parse(src).body if isinstance(nd, ast.FunctionDef) and nd.name == "Q3"][0]
ns = {"math": math}
exec(compile(ast.Module(body=[fn], type_ignores=[]), TREE, "exec"), ns)
treeQ3 = ns["Q3"]
worst = 0.0
for X in (1.0, 1.000001, 1.1, 2.0, 5.0, 35.35533905932738, 1e3, 1e5):
    direct = 0.0 if X <= 1 else float(4 * mp.mpf(X) ** -4 * mp.quad(lambda t: t * t * mp.sqrt(t * t - 1), [1, X]))
    worst = max(worst, abs(treeQ3(X) - direct))
rec("9  fewsterteo.Q3 == 4x^-4 INT_1^x y^2 sqrt(y^2-1) by quadrature (8 points to 1e5)", worst < 1e-12,
    "max |diff| %.2e" % worst)
rec("9b fewsterteo.Q3(x) = 0 for x <= 1 (convention: (5.6) integrates from u = C only)",
    treeQ3(0.5) == 0.0 and treeQ3(1.0) == 0.0)

# 10. independent spot check of one tree figure: ratio(C=1) = 0.974321 (GAP_SWEEP),
# with an independent sampler implementation and the flat total by t-space quadrature
mp.mp.dps = 20
m1 = mp.findroot(lambda m: mp.cos(m) * mp.cosh(m) - 1, mp.mpf("4.73"))
sg = (mp.cosh(m1) - mp.cos(m1)) / (mp.sinh(m1) - mp.sin(m1))
g = lambda t: mp.cosh(m1 * t) - mp.cos(m1 * t) - sg * (mp.sinh(m1 * t) - mp.sin(m1 * t))
g2 = lambda t: m1 ** 2 * (mp.cosh(m1 * t) + mp.cos(m1 * t) - sg * (mp.sinh(m1 * t) + mp.sin(m1 * t)))
norm = mp.quad(lambda t: g(t) ** 2, [0, 1])
# FT(g'')(u) = INT_0^1 g''(t) e^{-iut} dt in closed form, sum of exponentials
terms = [(m1, m1 ** 2 * (1 - sg) / 2), (-m1, m1 ** 2 * (1 + sg) / 2),
         (1j * m1, m1 ** 2 * (1 + 1j * sg) / 2), (-1j * m1, m1 ** 2 * (1 - 1j * sg) / 2)]
# check the decomposition reproduces g''
assert abs(sum(c * mp.e ** (al * 0.37) for al, c in terms).real - g2(0.37)) < 1e-12
def ftg2sq(s):
    z = sum(c * (mp.e ** (al - 1j * s) - 1) / (al - 1j * s) for al, c in terms)
    return abs(z) ** 2 / norm
total = mp.pi * mp.quad(lambda t: g2(t) ** 2, [0, 1]) / norm
Cv = mp.mpf(1)
edges = [0, Cv] + [Cv + k * mp.pi for k in range(1, 1300)]
d = mp.quad(ftg2sq, [0, Cv]) + mp.quad(lambda s: ftg2sq(s) * (1 - Q3n(s / Cv)), edges[1:])
# tail beyond U: |FT g''|^2 ~ (g''(0)^2+g''(1)^2)/s^2 on average, 1-Q3 ~ 3C^2/(2 s^2)... bound it
U = edges[-1]
tail = (g2(0) ** 2 + g2(1) ** 2) / norm * 1.5 * Cv ** 2 / (3 * U ** 3)
r = 1 - d / total
rec("10 ratio(C=1) by independent code == tree's GAP_SWEEP 0.974321 (to 1e-6)",
    abs(r - mp.mpf("0.974321")) < 1e-6, "got %s (tail est %.1e)" % (mp.nstr(r, 10), float(tail)))

# 11. the unnamed hypothesis: minimal coupling.  F&T (2.2) has no xi R term; with
# xi R added on the static open universe (R = -6/a^2 for H^3 slices of radius a,
# ultrastatic so the 4D Ricci scalar is the spatial one) w_q^2 = (q^2+1)/a^2 + mu^2 + xi R,
# so C^2 = 1/a^2 + mu^2 - 6 xi/a^2: conformal coupling xi = 1/6 closes the gap entirely.
xi = sp.Symbol("xi", real=True)
t_, r_ = sp.symbols("t r_", positive=True)
# Ricci scalar of -dt^2 + a^2 (dchi^2 + sinh^2 chi dOmega^2), computed from the metric
chi, th, ph = sp.symbols("chi theta phi", real=True)
coords = [t_, chi, th, ph]
gm = sp.diag(-1, a ** 2, a ** 2 * sp.sinh(chi) ** 2, a ** 2 * sp.sinh(chi) ** 2 * sp.sin(th) ** 2)
gi = gm.inv()
N = 4
Gam = [[[sum(gi[i, l] * (sp.diff(gm[l, j], coords[k]) + sp.diff(gm[l, k], coords[j]) - sp.diff(gm[j, k], coords[l]))
             for l in range(N)) / 2 for k in range(N)] for j in range(N)] for i in range(N)]
def Ric(j, k):
    return sp.simplify(sum(sp.diff(Gam[i][j][k], coords[i]) - sp.diff(Gam[i][j][i], coords[k])
                           + sum(Gam[i][i][l] * Gam[l][j][k] - Gam[i][k][l] * Gam[l][j][i] for l in range(N))
                           for i in range(N)))
Rs = sp.simplify(sum(gi[j, k] * Ric(j, k) for j in range(N) for k in range(N)))
rec("11a Ricci scalar of the static open RW universe == -6/a^2", sp.simplify(Rs + 6 / a ** 2) == 0, "R = %s" % Rs)
C2xi = sp.simplify(1 / a ** 2 + mu ** 2 + xi * Rs)
rec("11b conformal coupling xi = 1/6: C = mu (gap closes; massless -> C = 0, witness ratio -> 1)",
    sp.simplify(C2xi.subs(xi, sp.Rational(1, 6)) - mu ** 2) == 0, "C^2(xi) = %s" % C2xi)

bad_rows = [r for r in rows if not r[1]]
print("\n%d checks, %d failed" % (len(rows), len(bad_rows)))
sys.exit(1 if bad_rows else 0)
