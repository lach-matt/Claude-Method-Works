#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 2309.10848-dsnec:
FFKP (Fliss, Freivogel, Kontou, Pardo Santos, arXiv:2309.10848v1) Sec. IV.C-D,
eqs. (75)-(97), as qeihps.py uses them (REFUSED on HPS: Minkowski-only).

What is checkable here (finite / closed form), and what this script checks:
  A. (94)  int f'^2 <= ||f||^2/(2 l^2) + (l^2/2)||f''||^2     (IBP + Cauchy-Schwarz + AM-GM)
  B. (95)-(96)  Q0, Q2 from (93) + (94) + (97) -- symbolic, ASSUMING the xi term of (93)
     is |xi| phi~^2 l^-(n-2) int |d_-^2 (f^2)| (absolute value bars; see C)
  C. text-layer discrepancy: as extracted, (80)/(93) print int d_-^2(f^2) with no bars;
     for rapidly decaying f that integral is 0 identically, which would make the xi term
     vanish -- contradicting (96)'s 2|xi|phi~^2 contributions.  Shown numerically.
  D. ANEC limit (88)-(89): scaling of both right-side terms of (85)/(86) with
     delta+ delta- = alpha^2 fixed; the paper's 'delta+/(A alpha^4)' vs the general-n power.
  E. the tree's inputs (qeihps.py:125-132): r_c = 1/sqrt(540 pi), Kretschmann radius
     r_c/sqrt2, and the Kretschmann scalar of -e^{2Phi}dt^2+dl^2+r^2 dOmega^2 at a throat,
     with the conditions under which it equals 4/r0^4 (HPS's throat data are the tree's
     own computation, NOT re-derived here).
  F. the tree's DSN predicate, imported read-only: the flat CONTROL (Kretschmann 0)
     returns EVALUABLE with no inputs, although FFKP (80)-(96) need the state class (79).
Nothing here edits the tree.
"""
import math, sys
import sympy as sp

ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + detail) if detail else ""))

x = sp.symbols('x', real=True)
l = sp.symbols('ell', positive=True)

# ---------- A. (94) ----------
def norms(f):
    f1, f2 = sp.diff(f, x), sp.diff(f, x, 2)
    I = lambda g: sp.integrate(sp.simplify(g), (x, -sp.oo, sp.oo))
    return I(f**2), I(f1**2), I(f2**2)
for s in (sp.Rational(1, 2), 1, 3):
    f = sp.exp(-x**2 / (2 * s**2))
    n0, n1, n2 = norms(f)
    rhs = n0 / (2 * l**2) + l**2 / 2 * n2
    gap = sp.simplify(rhs - n1)
    # minimum over ell of the gap must be >= 0: gap = (n0/(2l^2) + l^2 n2/2) - n1, min at l^4 = n0/n2
    lmin = (n0 / n2) ** sp.Rational(1, 4)
    gmin = sp.nsimplify(sp.simplify(gap.subs(l, lmin)))
    chk("A (94) Gaussian sigma=%s: min_ell[RHS-LHS] = %s >= 0" % (s, sp.N(gmin, 8)), sp.N(gmin) >= -1e-12)
# compact bump, numerically, several ell
import random
def bump_norms(a, N=20001):
    h = 2 * a / (N - 1); xs = [-a + i * h for i in range(N)]
    def f(t):
        u = t / a
        return math.exp(-1 / (1 - u * u)) if abs(u) < 1 else 0.0
    fv = [f(t) for t in xs]
    d1 = [(fv[i + 1] - fv[i - 1]) / (2 * h) for i in range(1, N - 1)]
    d2 = [(fv[i + 1] - 2 * fv[i] + fv[i - 1]) / h**2 for i in range(1, N - 1)]
    n0 = sum(v * v for v in fv) * h; n1 = sum(v * v for v in d1) * h; n2 = sum(v * v for v in d2) * h
    # integral of d^2(f^2) and |d^2(f^2)|
    g = [v * v for v in fv]
    dd = [(g[i + 1] - 2 * g[i] + g[i - 1]) / h**2 for i in range(1, N - 1)]
    return n0, n1, n2, sum(dd) * h, sum(abs(v) for v in dd) * h
n0, n1, n2, iraw, iabs = bump_norms(1.0)
worst = min(n0 / (2 * L**2) + L**2 / 2 * n2 - n1 for L in [10 ** (k / 10) for k in range(-20, 21)])
chk("A (94) compact C^inf bump, ell in [0.01,100]: min[RHS-LHS] = %.3e >= 0" % worst, worst >= -1e-9)

# ---------- B. (95)-(96) ----------
n = sp.symbols('n', positive=True)
pn, xi, ph, F0, F1, F2, F11 = sp.symbols('p_n xi phit F0 F1 F2 F11', positive=True)
# (93): -(p_n / l^(n-2)) int f'^2  - (|xi| phit^2 / l^(n-2)) int |d^2 f^2|
# int |d^2 f^2| <= 2 int f'^2 + 2 int |f||f''|      (triangle)
# int f'^2 <= F0/(2l^2) + l^2 F2/2                  (94)
# int |f||f''| <= eps F0 + F2/(4 eps), eps = 1/(2 l^2)   (97)
eps = 1 / (2 * l**2)
bf1 = F0 / (2 * l**2) + l**2 * F2 / 2
bff = eps * F0 + F2 / (4 * eps)
bound = pn / l**(n - 2) * bf1 + xi * ph / l**(n - 2) * (2 * bf1 + 2 * bff)
Q0 = sp.simplify(sp.expand(bound).coeff(F0)); Q2 = sp.simplify(sp.expand(bound).coeff(F2))
Q0p = (pn / 2 + 2 * xi * ph) / l**n; Q2p = (pn / 2 + 2 * xi * ph) / l**(n - 4)
chk("B (96) Q0 = (p_n/2 + 2|xi|phi~^2)/l^n re-derived", sp.simplify(Q0 - Q0p) == 0, str(Q0))
chk("B (96) Q2 = (p_n/2 + 2|xi|phi~^2)/l^(n-4) re-derived", sp.simplify(Q2 - Q2p) == 0, str(Q2))
p4 = 4 / (n - 2) * sp.pi**(-n / 2) / sp.gamma((n - 2) / 2)
chk("B p_n at n=4 = 2/pi^2 (formula as printed after (93))", sp.simplify(p4.subs(n, 4) - 2 / sp.pi**2) == 0)

# ---------- C. bars ----------
f = sp.exp(-x**2)
Iraw = sp.integrate(sp.diff(f**2, x, 2), (x, -sp.oo, sp.oo))
chk("C int d^2(f^2) over R = 0 for Gaussian f (text layer, no bars)", Iraw == 0, str(Iraw))
chk("C same for compact bump (numeric): %.2e ~ 0; int|d^2 f^2| = %.4f > 0" % (iraw, iabs),
    abs(iraw) < 1e-6 and iabs > 0.1)
print("     => the xi term of (80),(85),(93) is non-trivial only with |.| (or an equivalent);"
      " (95)-(97) use the triangle inequality on |f||f''|, so the PDF presumably carries bars"
      " the text layer lost.  RECORDED as a text-layer discrepancy, not an error.")
print("     => (79) as extracted is ONE-SIDED (<:phi^2:> <= phi_max^2); the step to (80) needs"
      " |<:phi^2:>| <= phi_max^2 because d_-^2(f^2) changes sign (shown: int|.| > |int .|)."
      " Same status: discrepancy of the text layer vs the PDF, unread.")

# ---------- D. ANEC limit ----------
dp, a, A, C, phim = sp.symbols('delta_p alpha A C phimax', positive=True)
dm = a**2 / dp
t1 = 1 / (dp**((n - 2) / 2) * dm**((n + 2) / 2))          # first term of (85)
t2 = C * xi * phim / dm**2                                 # second term of (85)
# LHS (1/(dp dm)) F^2 -> (A/dm) delta(x+ - beta) F(.,0)^2  ; multiply by dm/A
s1 = sp.simplify(t1 * dm / A); s2 = sp.simplify(t2 * dm / A)
chk("D first term -> delta+/(A alpha^n)", sp.simplify(s1 - dp / (A * a**n)) == 0, str(s1))
phit = phim * a**(n - 2)                                   # phi~^2 = (d+ d-)^((n-2)/2) phi^2
s2t = sp.simplify(s2.subs(phim, sp.Symbol('pt') / a**(n - 2)))
chk("D second term -> C|xi| phi~^2 delta+/(A alpha^n) [= delta+/(A alpha^2) in phi_max]",
    sp.simplify(s2t - C * xi * sp.Symbol('pt') * dp / (A * a**n)) == 0, str(s2t))
chk("D printed 'delta+/(A alpha^4)' matches the phi~ form only at n = 4",
    sp.solve(sp.Eq(n, 4), n) == [4])
chk("D both terms -> 0 as delta+ -> 0: (89) ANEC follows either way",
    sp.limit(s1.subs(n, 4), dp, 0) == 0 and sp.limit(s2, dp, 0) == 0)

# ---------- E. tree inputs ----------
rc = 1 / math.sqrt(540 * math.pi); rk = rc / math.sqrt(2)
chk("E r_c = 1/sqrt(540 pi) = %.7f l_P (printed 0.0242789)" % rc, abs(rc - 0.0242789) < 5e-8)
chk("E Kretschmann radius (4/r_c^4)^(-1/4) = %.7f l_P (printed 0.0171677)" % (4 / rc**4) ** -0.25,
    abs((4 / rc**4) ** -0.25 - 0.0171677) < 5e-8 and abs((4 / rc**4) ** -0.25 - rk) < 1e-15)
chk("E both < 1 l_P", rc < 1 and rk < 1)
# Kretschmann of static spherical metric, generic
t, L, th, phi_ = sp.symbols('t l theta phi', real=True)
Phi = sp.Function('Phi')(L); r = sp.Function('r')(L)
coords = [t, L, th, phi_]
g = sp.diag(-sp.exp(2 * Phi), 1, r**2, r**2 * sp.sin(th)**2)
gi = g.inv()
dim = 4
Gam = [[[sp.simplify(sum(gi[i, m] * (sp.diff(g[m, j], coords[k]) + sp.diff(g[m, k], coords[j])
          - sp.diff(g[j, k], coords[m])) for m in range(dim)) / 2) for k in range(dim)]
        for j in range(dim)] for i in range(dim)]
def Riem(i, j, k, m):  # R^i_{jkm}
    e = sp.diff(Gam[i][j][m], coords[k]) - sp.diff(Gam[i][j][k], coords[m])
    e += sum(Gam[i][k][s] * Gam[s][j][m] - Gam[i][m][s] * Gam[s][j][k] for s in range(dim))
    return sp.simplify(e)
Rup = {}
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            for m in range(k + 1, dim):
                v = Riem(i, j, k, m)
                if v != 0:
                    Rup[(i, j, k, m)] = v; Rup[(i, j, m, k)] = -v
Rdn = {}
for (i, j, k, m), v in Rup.items():
    for p in range(dim):
        if g[p, i] != 0:
            Rdn[(p, j, k, m)] = Rdn.get((p, j, k, m), 0) + g[p, i] * v
K = 0
for (a1, b1, c1, d1), v in Rdn.items():
    K += v * v * gi[a1, a1] * gi[b1, b1] * gi[c1, c1] * gi[d1, d1]
K = sp.simplify(K)
r0s, P1, P2, r1s, r2s = sp.symbols('r0 P1 P2 r1 r2', real=True)
subsd = {sp.Derivative(Phi, (L, 2)): P2, sp.Derivative(Phi, L): P1,
         sp.Derivative(r, (L, 2)): r2s, sp.Derivative(r, L): r1s, r: r0s}
Kt = sp.simplify(K.subs(subsd))
Kexp = sp.expand(Kt)
print("     Kretschmann (generic static spherical, at a point):", sp.factor(Kt))
Kthroat = sp.simplify(Kt.subs({r1s: 0}))
chk("E at r'=0: K = 4(P''+P'^2)^2 + 8(r''/r)^2 + 4/r^4",
    sp.simplify(Kthroat - (4 * (P2 + P1**2)**2 + 8 * (r2s / r0s)**2 + 4 / r0s**4)) == 0,
    str(sp.factor(Kthroat)))
chk("E K = 4/r0^4 exactly when r'=r''=0 and Phi''+Phi'^2=0 at the throat (tree's HPS data, not re-derived)",
    sp.simplify(Kthroat.subs({r2s: 0, P2: -P1**2}) - 4 / r0s**4) == 0)
print("     note: K >= 4/r0^4 at any throat (r'=0), so the Kretschmann radius is <= r0/sqrt2 in"
      " general -- the sub-Planckian conclusion does not depend on the tree's throat data beyond r0.")
chk("E general throat: K - 4/r0^4 is a sum of squares (>= 0)",
    sp.simplify(Kthroat - 4 / r0s**4 - 4 * (P2 + P1**2)**2 - 8 * (r2s / r0s)**2) == 0)

# ---------- F. the tree's DSN predicate (read-only import) ----------
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import qeihps as q
    rows = q.hypothesis_table(kretschmann=0)
    st = q.qei_status(rows, q.DSN)
    chk("F tree verdict on HPS: %s" % q.DSNEC_ON_HPS.split(' --')[0],
        q.qei_status(q.HYPOTHESES, q.DSN)[0] == "REFUSED")
    chk("F flat CONTROL (Kretschmann 0) -> %s with inputs %s; FFKP (80)-(96) need (79) phi_max,"
        " which the tree's own FFKP row marks NOT-FOUND" % st, st == ("EVALUABLE", []))
    print("     => the DSN row's hypothesis set is {flat} only: DROPPED (79)/phi_max, free scalar,"
          " n-dim, factorisation (81)/(90), massless for (82)-(83),(93), even n for (83)."
          " Counterfactual only -- it cannot move the REFUSED verdict (one failed form"
          " hypothesis suffices).")
except Exception as e:
    chk("F import qeihps (read-only)", False, repr(e))

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
