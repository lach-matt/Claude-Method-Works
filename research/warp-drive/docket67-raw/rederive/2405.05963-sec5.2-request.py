#!/usr/bin/env python3
"""DOCKET 67 audit: Kontou 2024 (arXiv:2405.05963) Sec. 5.2 -- the request to test HPS
(gr-qc/9701064) with the non-minimal QEIs [17,30], and the throat-size remark
'of Planck length or up to the order 10^2 l_pl'.

What is finite/closed-form here and checked:
 C1  the tree's parse of the request's citation list -> (17, 30); FS not among the tree's names
     (CIRCULAR: checks the tree's own ref map, not Kontou's bibliography -- flagged)
 C2  HPS quartic (8) at f(0)=f''(0)=1, r''(0)=0, ln f(0)=0: r(0)=sqrt(K^-2/4)=sqrt(1440 pi)=67.26 l_P
     (HPS text: 'r(0) ~ 67 l_P')
 C3  HPS data class (9): quartic (8) with f''=r''=0 gives r(0)^2 = -16 K^2 ln f(0), i.e. eq.(9)'s r(0);
     at ln f(0) = -2/3: r0 = 1/sqrt(540 pi) = 0.02428 l_P (HPS text: 'r(0) ~ 0.02 l_P');
     over -1 <= ln f(0) < 0: r0 in (0, 1/sqrt(360 pi)] = (0, 0.02974] l_P
 C4  decades: log10 r0 for 0.0243, 67.26, 200, 300 against Kontou's range [~1, ~10^2] l_P
 C5  orthonormal Riemann of metric (2) at l=0 with f'=r'=0, by sympy from the metric:
     |R_tltl| = |f''/(2f)|, |R_lthlth| = |r''/r|, |R_thphthph| = 1/r^2 -> curvature in Planck units
     for the (9) class (1/r0^2 = 540 pi) and for the 67 l_P case (f''/2f = 1/2: Planckian)
 C6  Kretschmann at the (9)-class throat = 4/r0^4 -> radius r0/sqrt(2)
Not checkable here: HPS's 200-300 l_P 'local solutions' (data not printed; 'separate publication').
"""
import math, re, sys
import sympy as sp

ok = True
def check(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + detail if detail else ""))

# C1
REQ = ("However, it would be of interest to examine that wormhole solution using "
       "one of the QEIs for the nonminimally coupled fields derived in [17,30] to "
       "determine its exact validity.")
refs = tuple(int(x) for x in re.search(r"\[([\d,]+)\]", REQ).group(1).split(","))
TREE_NAMES = {17: "Fliss-Freivogel-Kontou-Pardo Santos 2309.10848",
              30: "Fewster-Osterbrink 0708.2450"}
fs = any("0702056" in TREE_NAMES.get(k, "") or "Fewster-Smith" in TREE_NAMES.get(k, "") for k in refs)
check("C1 refs parsed = (17,30); FS not named (tree's map; circular)", refs == (17, 30) and not fs, str(refs))

# C2, C3: quartic (8)
r, lnf, fpp, rpp, f0 = sp.symbols("r lnf fpp rpp f0", real=True)
K2 = sp.Rational(1, 5760) / sp.pi
quartic = (-4 * (fpp / f0) ** 2 * (1 + lnf) * r ** 4
           + 32 * (fpp * rpp / f0) * (1 + lnf / 2) * r ** 3
           + (1 / K2 - 16 * rpp ** 2 * lnf) * r ** 2 + 16 * lnf)
q67 = quartic.subs({f0: 1, fpp: 1, rpp: 0, lnf: 0})
sols = [s for s in sp.solve(sp.Eq(q67, 0), r) if s.is_positive]
r67 = sols[0]
check("C2 quartic(8) at f=f''=1, r''=0 -> r0 = sqrt(1440 pi)", sp.simplify(r67 - sp.sqrt(1440 * sp.pi)) == 0,
      "r0 = %s = %.4f l_P (HPS: ~67)" % (r67, float(r67)))

q9 = quartic.subs({fpp: 0, rpp: 0})
sol9 = [s for s in sp.solve(sp.Eq(q9, 0), r)]
r9 = sp.sqrt(-16 * K2 * lnf)
check("C3a quartic(8) with f''=r''=0 reproduces eq.(9) r(0)=sqrt(-16K^2 ln f0)",
      any(sp.simplify(s - r9) == 0 for s in sol9))
r_plot = r9.subs(lnf, sp.Rational(-2, 3))
check("C3b ln f0 = -2/3 -> r0 = 1/sqrt(540 pi)", sp.simplify(r_plot - 1 / sp.sqrt(540 * sp.pi)) == 0,
      "%.6f l_P (HPS: ~0.02)" % float(r_plot))
r_max = r9.subs(lnf, -1)
check("C3c class (9) max r0 at ln f0 = -1 is 1/sqrt(360 pi)", sp.simplify(r_max - 1 / sp.sqrt(360 * sp.pi)) == 0,
      "%.6f l_P: EVERY (9)-class throat is sub-Planckian" % float(r_max))

# C4 decades
for name, val in [("plotted (9)", float(r_plot)), ("(9) max", float(r_max)), ("quartic 67", float(r67)),
                  ("local 200", 200.0), ("local 300", 300.0)]:
    print("     log10 r0 [%s] = %+.3f" % (name, math.log10(val)))
check("C4a plotted throat is ~1.6 decades BELOW 'Planck length' (Kontou's lower end)",
      math.log10(float(r_plot)) < -1.5)
check("C4b 67 and 300 l_P round to order 10^2 (log10 in [1.5, 2.5))",
      all(1.5 <= math.log10(v) < 2.5 for v in (float(r67), 300.0)))

# C5 Riemann at the throat, from metric (2)
l = sp.symbols("l", real=True)
th, ph, t = sp.symbols("theta phi t", real=True)
F = sp.Function("f")(l); Rr = sp.Function("r")(l)
x = [t, l, th, ph]
g = sp.diag(-F, 1, Rr ** 2, Rr ** 2 * sp.sin(th) ** 2)
ginv = g.inv()
n = 4
Gam = [[[sum(ginv[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
             for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
def Riem(a, b, c, d):  # R^a_{bcd}
    e = sp.diff(Gam[a][b][d], x[c]) - sp.diff(Gam[a][b][c], x[d])
    e += sum(Gam[a][c][k] * Gam[k][b][d] - Gam[a][d][k] * Gam[k][b][c] for k in range(n))
    return sp.simplify(e)
def Rlow(a, b, c, d):
    return sp.simplify(sum(g[a, k] * Riem(k, b, c, d) for k in range(n)))
norm = [sp.sqrt(F), 1, Rr, Rr * sp.sin(th)]
def Rhat(a, b, c, d):
    return sp.simplify(Rlow(a, b, c, d) / (norm[a] * norm[b] * norm[c] * norm[d]))
throat = lambda e: sp.simplify(e.subs(sp.Derivative(F, l), 0).subs(sp.Derivative(Rr, l), 0)) \
    if False else e
f0s, f2s, r0s, r2s = sp.symbols("f0 f2 r0 r2", positive=False, real=True)
def at_throat(e):
    e = e.subs({sp.Derivative(F, (l, 2)): f2s, sp.Derivative(Rr, (l, 2)): r2s})
    e = e.subs({sp.Derivative(F, l): 0, sp.Derivative(Rr, l): 0})
    return sp.simplify(e.subs({F: f0s, Rr: r0s}))
Rtltl = at_throat(Rhat(0, 1, 0, 1)); Rlhlh = at_throat(Rhat(1, 2, 1, 2)); Rhphp = at_throat(Rhat(2, 3, 2, 3))
Rtqtq = at_throat(Rhat(0, 2, 0, 2))
print("     throat R_tltl =", Rtltl, "; R_l th l th =", Rlhlh, "; R_th ph th ph =", Rhphp, "; R_t th t th =", Rtqtq)
check("C5a |R_tltl| = |f''/(2f)|, |R_lthlth| = |r''/r|, R_thphthph = 1/r^2, R_tthtth = 0",
      sp.simplify(sp.Abs(Rtltl) - sp.Abs(f2s / (2 * f0s))) == 0 and sp.simplify(sp.Abs(Rlhlh) - sp.Abs(r2s / r0s)) == 0
      and sp.simplify(Rhphp - 1 / r0s ** 2) == 0 and Rtqtq == 0)
c9 = Rhphp.subs(r0s, r_plot)
check("C5b (9)-class plotted throat: l_P^2 |Riem|max = 540 pi = %.0f >> 1" % float(c9),
      sp.simplify(c9 - 540 * sp.pi) == 0)
c67 = [abs(float(Rtltl.subs({f2s: 1, f0s: 1}))), abs(float(Rhphp.subs(r0s, r67)))]
check("C5c 67 l_P case: |R_tltl| = 1/2 l_P^-2 (Planckian, radius %.3f l_P) though 1/r0^2 = %.2e"
      % (c67[0] ** -0.5, c67[1]), abs(c67[0] - 0.5) < 1e-12)

# C6 Kretschmann for (9) class at the throat
Kr = 4 / r0s ** 4  # only R_thphthph and permutations nonzero when f''=r''=0: 4 * (1/r0^2)^2
kr_rad = (Kr.subs(r0s, r_plot)) ** sp.Rational(-1, 4)
check("C6 Kretschmann radius = r0/sqrt2 = %.5f l_P" % float(kr_rad),
      sp.simplify(kr_rad - r_plot / sp.sqrt(2)) == 0)

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
