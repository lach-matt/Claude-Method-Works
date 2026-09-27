#!/usr/bin/env python3
"""DOCKET 67 re-derivation: anderson-molina-paris-mottola-kontou-validity.

Tree use (throatmass.py:68-72): 'If Flanagan-Wald, Anderson-Molina-Paris-Mottola
and Kontou are right that eps ~ 1 lies outside semiclassical gravity's domain,
the corridor is ... placed beyond the theory's jurisdiction.'

What is checked here (finite / closed form only):
 A. the tree's eps: h = 2(M/b)/(a/b) at the core surface, from achievable.py
    constants imported READ-ONLY -> 1/2 exactly.
 B. the domain boundary the sources STATE is a length-scale one:
    AMM gr-qc/0209075 p.7 'length scales l much greater than the Planck length',
    p.13 '4 G_N |k^2| << O(1)'; Kontou-Sanders 2003.01815 p.35 'Planck scale
    ... probably lie outside the range of validity of the semiclassical Einstein
    equation'; Kontou 2405.05963 p.19 HPS throat 'of Planck length or up to the
    order 10^2 l_pl, so it is doubtful that it can be considered in the regime
    of the semiclassical approximation'.
    Compute AMM's 4 G|k^2| ~ 4 (l_P/L)^2 at the corridor scales and at HPS scales.
 C. Schwarzschild: derive the Kretschmann scalar from the metric (sympy),
    K = 48 M^2/r^6 = 12 h^2 / r^4 with h = 2M/r.  So at FIXED h (eps) the
    curvature in Planck units is 12 h^2 (l_P/r)^4 -- set by scale, not by h.
    h = 1 at the horizon r = 2M: AMM p.14 name Schwarzschild horizons and the
    Hartle-Hawking static self-consistent solution as applications of their
    criterion, i.e. an h = 1 geometry treated INSIDE the framework.
 D. z3: logical independence of 'eps ~ 1' and 'Planckian curvature' under the
    dimensional estimate l_P^2 |Riem| ~ h (l_P/L)^2 -- all four quadrants SAT;
    and the universal statement: for all h in (0,1], L >= 1e3 l_P,
    12 h^2 (l_P/L)^4 <= 1.2e-11  (UNSAT of its negation).
    (First run used < 1e-11, which is FALSE at h=1, L=1e3 l_P: 1.2e-11 -- z3 caught it; kept on record.)
Exit 0 iff every check passes.
"""
import sys, math
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import sympy as sp

fails = 0
def chk(name, ok, detail=""):
    global fails
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        fails += 1

# ---------------- A. tree's eps
import achievable  # read-only import of constants
Mb = sp.nsimplify(achievable.M_OVER_B); ab = sp.nsimplify(achievable.A_OVER_B)
h = sp.simplify(2 * Mb / ab)
chk("A1 h_core = 2(M/b)/(a/b) = 1/2 exactly", h == sp.Rational(1, 2), "M/b=%s a/b=%s h=%s" % (Mb, ab, h))
lP = achievable.L_PLANCK
chk("A2 l_P from achievable.py = CODATA 1.616255e-35 m", abs(lP - 1.616255e-35) < 1e-41)
# cross-check l_P from CODATA 2018/2022 hbar, G, c
hbar = 1.054571817e-34; G = 6.67430e-11; c = 299792458.0
lP_c = math.sqrt(hbar * G / c**3)
chk("A3 sqrt(hbar G/c^3) = l_P (CODATA 2018 = 2022 values)", abs(lP_c / lP - 1) < 1e-6, "%.7e" % lP_c)

# ---------------- B. AMM's length-scale condition at the corridor and at HPS
def amm_x(L):  # 4 G |k^2| with k ~ 1/L, G = l_P^2 in hbar=c=1
    return 4.0 * (lP / L) ** 2
rows = []
for label, a in [("corridor core a = 1 m (b = 50 m)", 1.0),
                 ("corridor core a = 1 cm", 1e-2),
                 ("achievable.py dimensional-identity crossing a = 4.09 l_P", 4.09 * lP),
                 ("HPS throat ~ 1 l_P (Kontou 2405.05963 p.19 lower end)", 1.0 * lP),
                 ("HPS throat ~ 1e2 l_P (Kontou p.19 upper end)", 1e2 * lP)]:
    x = amm_x(a)
    rows.append((label, a, x))
    print("     %-60s a/l_P = %.3e   4G|k^2| ~ %.3e" % (label, a / lP, x))
chk("B1 corridor at a = 1 m: 4G|k^2| << 1 (AMM p.13 condition met)", amm_x(1.0) < 1e-60, "%.3e" % amm_x(1.0))
chk("B2 AMM condition fails (x >= O(0.1)) only at a ~ few l_P", amm_x(4.09 * lP) > 0.1 and amm_x(1e2 * lP) < 1e-3,
    "x(4.09 l_P)=%.3f, x(100 l_P)=%.1e" % (amm_x(4.09 * lP), amm_x(1e2 * lP)))
chk("B3 AMM's condition contains no metric-amplitude (h/eps) variable",
    sp.Symbol('h') not in (4 * sp.Symbol('lP')**2 / sp.Symbol('L')**2).free_symbols)

# ---------------- C. Schwarzschild Kretschmann from the metric
t, r, th, ph, M = sp.symbols('t r theta phi M', positive=True)
x = [t, r, th, ph]
f = 1 - 2 * M / r
g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[cc]) + sp.diff(g[d, cc], x[b]) - sp.diff(g[b, cc], x[d]))
          for d in range(n)) / 2) for cc in range(n)] for b in range(n)] for a in range(n)]
def Riem(a, b, cc, d):  # R^a_{bcd}
    e = sp.diff(Gam[a][b][d], x[cc]) - sp.diff(Gam[a][b][cc], x[d])
    e += sum(Gam[a][cc][k] * Gam[k][b][d] - Gam[a][d][k] * Gam[k][b][cc] for k in range(n))
    return sp.simplify(e)
R = {}
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(cc + 1, n):
                v = Riem(a, b, cc, d)
                if v != 0:
                    R[(a, b, cc, d)] = v; R[(a, b, d, cc)] = -v
# lower first index, raise others (diagonal metric)
K = 0
for (a, b, cc, d), v in R.items():
    low = g[a, a] * v
    up = v * gi[b, b] * gi[cc, cc] * gi[d, d]
    K += low * up
K = sp.simplify(K)
chk("C1 Kretschmann(Schwarzschild) = 48 M^2/r^6 (derived from metric)", sp.simplify(K - 48 * M**2 / r**6) == 0, str(K))
hs = sp.Symbol('h', positive=True)
K_h = sp.simplify(K.subs(M, hs * r / 2))
chk("C2 in terms of h = 2M/r: K = 12 h^2 / r^4", sp.simplify(K_h - 12 * hs**2 / r**4) == 0, str(K_h))
chk("C3 h = 1 exactly at the horizon r = 2M (g_tt = 0)", sp.simplify((2 * M / r).subs(r, 2 * M)) == 1 and sp.simplify(f.subs(r, 2 * M)) == 0)
for L in [1.0, 1e3 * lP, 4.09 * lP]:
    val = 12 * 0.25 * (lP / L)**4
    print("     h = 1/2, r = %.3e m: l_P^4 K = %.3e" % (L, val))
chk("C4 h = 1/2 at r = 1 m: l_P^4 K = 3 (l_P/r)^4 ~ 2e-139 (sub-Planckian by 139 decades)",
    12 * 0.25 * lP**4 < 1e-138)

# ---------------- D. z3: independence of eps~1 and Planckian curvature
try:
    import z3
except ImportError:
    z3 = None
if z3 is None:
    chk("D0 z3 available", False)
else:
    H, Lr = z3.Reals('H Lr')   # Lr = L / l_P
    curv = H / (Lr * Lr)        # l_P^2 |Riem| ~ h (l_P/L)^2 (dimensional estimate)
    quad = {
        "eps~1 & sub-Planckian": [H >= z3.RealVal("0.5"), H <= 1, Lr > 0, curv < z3.RealVal("1e-60")],
        "eps~1 & Planckian":     [H >= z3.RealVal("0.5"), H <= 1, Lr > 0, curv >= 1],
        "eps<<1 & sub-Planckian":[H > 0, H <= z3.RealVal("1e-10"), Lr > 0, curv < z3.RealVal("1e-60")],
        "eps<<1 & Planckian":    [H > 0, H <= z3.RealVal("1e-10"), Lr > 0, curv >= 1],
    }
    allsat = True
    for k, cs in quad.items():
        s = z3.Solver(); s.add(*cs); res = s.check()
        print("     z3 quadrant %-24s %s" % (k, res))
        allsat &= (res == z3.sat)
    chk("D1 all four (eps, curvature) quadrants satisfiable: 'eps ~ 1' is not the Planck criterion", allsat)
    # universal: forall h in (0,1], Lr >= 1e3: 12 h^2 / Lr^4 < 1e-11  (Schwarzschild, exact form C2)
    s = z3.Solver()
    s.add(H > 0, H <= 1, Lr >= 1000, 12 * H * H > z3.RealVal("1.2e-11") * Lr * Lr * Lr * Lr)
    res = s.check()
    chk("D2 forall h in (0,1], r >= 1e3 l_P: l_P^4 K = 12 h^2 (l_P/r)^4 <= 1.2e-11 (negation UNSAT)", res == z3.unsat, str(res))
    # vacuity guard: the hypotheses alone are satisfiable
    s2 = z3.Solver(); s2.add(H > 0, H <= 1, Lr >= 1000)
    chk("D3 vacuity guard: hypotheses of D2 satisfiable", s2.check() == z3.sat)
    # encoding-drift guard: D2's bound is tight at h=1, Lr=1e3: bound is attained at h=1, Lr=1e3, so any smaller threshold fails
    s3 = z3.Solver(); s3.add(H > 0, H <= 1, Lr >= 1000, 12 * H * H > z3.RealVal("1.1e-11") * Lr**4)
    chk("D4 encoding guard: a tighter threshold 1.1e-11 is violated (SAT) -- the check can fail", s3.check() == z3.sat)

print("\n%d failure(s)" % fails)
sys.exit(1 if fails else 0)
