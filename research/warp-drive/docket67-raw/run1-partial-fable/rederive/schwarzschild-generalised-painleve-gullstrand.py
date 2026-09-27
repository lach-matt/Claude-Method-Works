#!/usr/bin/env python3
"""DOCKET 67 rederivation, result 12/286: Schwarzschild in the generalised
Painleve-Gullstrand chart with constant energy E, as foliation.py section 4
uses it (research/warp-drive/foliation.py:182-205, verify() V7-V12,
d3_table :537-541, shapiro :568-574).

Source read at alphaXiv: Martel & Poisson gr-qc/0001069v4, eqs (3.1)-(3.6),
footnote [15].  Their chart, with p = 1/Etilde^2 in (0, 1]:

    ds^2 = -(1/p) dT^2 + p (dr + (1/p) sqrt(1 - p f) dT)^2 + r^2 dOmega^2   (3.6)

The owner's chart (foliation.py:184):

    ds^2 = -dtau^2 + (dR + sqrt(2M/R + 2E) dtau)^2 / (1+2E) + R^2 dOmega^2

Checks, all independent of the owner's own verify():
  C1  the owner's chart IS (3.6) under p = 1/(1+2E), T = sqrt(p) tau  (identity)
  C2  (3.6) IS Schwarzschild (1.1) under dt = dT - f^{-1} sqrt(1-pf) dr  (identity)
  C3  Ricci of the owner's chart = 0, computed by an independent route
      (sympy, full Riemann via a different code path than the owner's)
  C4  g^{RR} = 1 - 2M/R  =>  Misner-Sharp m = M
  C5  Gamma = sqrt(1+2E) on tau = const;  U = sqrt(2M/R+2E);  Gamma^2 - U^2 = 1 - 2M/R
  C6  STATICITY, which the owner asserts and does not verify: xi = d/dtau is
      Killing (components tau-independent), timelike for R > 2M, and
      hypersurface-orthogonal (Frobenius xi_[a d_b xi_c] = 0), i.e. STATIC.
  C7  E < 0 (p > 1): M&P footnote [15] -- the chart does not reach infinity;
      sqrt(2M/R + 2E) is real only for R <= -M/E.  Owner :199 names E < 0 as a
      member "giving Gamma < 1" without this domain restriction.
  C8  d3_table fixtures (foliation.py:960-962) recomputed with an independent
      integrator (mpmath quad, not the owner's trapezoid loop).
  C9  Shapiro excess 2M ln((R2-2M)/(R1-2M)) at M=1, 10->100 = 5.011.
Exit 1 on any failure.
"""
import sys
import sympy as sp

fails = []


def chk(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)


tau, R, th, ph, M, E = sp.symbols("tau R theta phi M E", positive=True)

# Zero test.  sympy's simplify leaves sqrt(a)*sqrt(b) - sqrt(a*b) uncombined
# (found on the first run: residual sqrt(2E+1)sqrt(ER+M) - sqrt((2E+1)(ER+M))),
# so combine radicals first (powsimp force=True); if that still does not
# close, evaluate EXACTLY at rational points and say so in the output.
ROUTE = {}
_PTS = [{M: sp.Rational(1), R: sp.Rational(7, 2), E: sp.Rational(3, 5), th: sp.Rational(1, 3)},
        {M: sp.Rational(2, 3), R: sp.Rational(11), E: sp.Rational(1, 7), th: sp.Rational(2, 5)},
        {M: sp.Rational(5, 4), R: sp.Rational(9, 4), E: sp.Rational(4, 9), th: sp.Rational(7, 6)}]
def iszero(e, tag=""):
    e1 = sp.simplify(sp.powsimp(sp.expand(e), force=True))
    if e1 == 0:
        ROUTE[tag] = "symbolic"
        return True
    e2 = sp.simplify(sp.powdenest(sp.radsimp(e1), force=True))
    if e2 == 0:
        ROUTE[tag] = "symbolic"
        return True
    ok = all(sp.simplify(e1.subs(pt)) == 0 for pt in _PTS)
    ROUTE[tag] = "exact-rational-points(3)" if ok else "NONZERO: %s" % e1
    return ok

p = 1 / (1 + 2 * E)                      # Martel-Poisson parameter
f = 1 - 2 * M / R
v = sp.sqrt(2 * M / R + 2 * E)

# ---- C1: owner's chart == M&P (3.6) under T = sqrt(p) tau ------------------
dtau, dR = sp.symbols("dtau dR")
owner = -dtau**2 + (dR + v * dtau)**2 / (1 + 2 * E)
dT = sp.sqrt(p) * dtau
mp36 = -(1 / p) * dT**2 + p * (dR + (1 / p) * sp.sqrt(1 - p * f) * dT)**2
chk("C1 owner chart == Martel-Poisson (3.6) with p=1/(1+2E), T=sqrt(p)tau",
    iszero(owner - mp36, "C1"))

# ---- C2: M&P (3.6) == Schwarzschild (1.1) under dt = dT - sqrt(1-pf)/f dR ----
dTs = sp.symbols("dT")
dt = dTs - sp.sqrt(1 - p * f) / f * dR
schw = -f * dt**2 + dR**2 / f
mp36T = -(1 / p) * dTs**2 + p * (dR + (1 / p) * sp.sqrt(1 - p * f) * dTs)**2
chk("C2 (3.6) == Schwarzschild curvature form under M&P's dt(dT,dr)",
    iszero(schw - mp36T, "C2"))

# ---- C3: Ricci = 0 for the owner's chart, independent code path -------------
x = [tau, R, th, ph]
g = sp.zeros(4, 4)
g[0, 0] = -1 + v**2 / (1 + 2 * E)
g[0, 1] = g[1, 0] = v / (1 + 2 * E)
g[1, 1] = 1 / (1 + 2 * E)
g[2, 2] = R**2
g[3, 3] = R**2 * sp.sin(th)**2
ginv = g.inv()
n = 4
# Christoffel of the second kind, Gamma^a_{bc}
Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                       - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
         for c in range(n)] for b in range(n)] for a in range(n)]
# Riemann R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce} Gam^e_{db} - Gam^a_{de} Gam^e_{cb}
def riem(a, b, c, d):
    e = sp.diff(Gam[a][d][b], x[c]) - sp.diff(Gam[a][c][b], x[d])
    for k in range(n):
        e += Gam[a][c][k] * Gam[k][d][b] - Gam[a][d][k] * Gam[k][c][b]
    return sp.simplify(e)
Ric = sp.zeros(4, 4)
for b in range(n):
    for d in range(n):
        Ric[b, d] = sum(riem(a, b, a, d) for a in range(n))
chk("C3 Ricci_ab == 0 (all 16, via Riemann contraction)",
    all(iszero(Ric[i, j], "C3[%d,%d]" % (i, j)) for i in range(n) for j in range(n)))
# Kretschmann as a positive check that the curvature is Schwarzschild's, not
# flat.  Contracted EXACTLY at rational points (the symbolic 4^8 contraction of
# unsimplified components did not finish in 10 min on the first attempt).
RIEM = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                RIEM[(a, b, c, d)] = riem(a, b, c, d)
k_ok = True
for pt in _PTS:
    gp = g.subs(pt); gip = ginv.subs(pt)
    Rn = {k: sp.nsimplify(sp.simplify(val.subs(pt))) for k, val in RIEM.items()}
    Rdn = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    Rdn[(a, b, c, d)] = sum(gp[a, e] * Rn[(e, b, c, d)] for e in range(n))
    Rup = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    Rup[(a, b, c, d)] = sum(gip[a, e] * gip[b, f_] * gip[c, h_] * gip[d, i_] * Rdn[(e, f_, h_, i_)]
                                            for e in range(n) for f_ in range(n) for h_ in range(n) for i_ in range(n)
                                            if gip[a, e] != 0 and gip[b, f_] != 0 and gip[c, h_] != 0 and gip[d, i_] != 0)
    Kp = sp.simplify(sum(Rdn[k] * Rup[k] for k in Rdn))
    target = (48 * M**2 / R**6).subs(pt)
    print("   Kretschmann at", {kk: vv for kk, vv in pt.items() if kk != th}, "=", Kp, " target 48M^2/R^6 =", target)
    if sp.simplify(Kp - target) != 0:
        k_ok = False
ROUTE["C3b"] = "exact-rational-points(3)"
chk("C3b Kretschmann == 48 M^2 / R^6 at 3 exact rational points (Schwarzschild, not flat, E-independent)", k_ok)

# ---- C4: Misner-Sharp mass --------------------------------------------------
chk("C4 g^{RR} = 1 - 2M/R  =>  m = M", sp.simplify(ginv[1, 1] - f) == 0
    and sp.simplify(R * (1 - ginv[1, 1]) / 2 - M) == 0)

# ---- C5: Gamma, U, invariant ------------------------------------------------
Gamma = 1 / sp.sqrt(g[1, 1])                    # dR/dl on tau = const
chk("C5a Gamma = sqrt(1+2E), R-independent", sp.simplify(Gamma - sp.sqrt(1 + 2 * E)) == 0)
u = sp.Matrix([1, -v, 0, 0])                   # unit normal to tau = const
chk("C5b unit normal u = (1,-v,0,0): u.u = -1", sp.simplify((u.T * g * u)[0, 0] + 1) == 0)
# U = u^a d_a R = -v ; Gamma^2 - U^2 = 1 - 2M/R
chk("C5c Gamma^2 - U^2 = 1 - 2M/R", sp.simplify(Gamma**2 - v**2 - f) == 0)
chk("C5d E = 0 gives Gamma = 1;  E > 0 gives Gamma > 1;  E < 0 gives Gamma < 1",
    sp.simplify(Gamma.subs(E, 0)) == 1
    and bool(sp.simplify(Gamma.subs(E, sp.Rational(1, 2))) > 1)
    and bool(sp.sqrt(1 + 2 * sp.Rational(-1, 4)) < 1))

# ---- C6: staticity (owner asserts :186, :48; verify() has no Killing check) --
xi_up = sp.Matrix([1, 0, 0, 0])
chk("C6a metric components tau-independent => xi = d/dtau is Killing",
    all(sp.diff(g[i, j], tau) == 0 for i in range(n) for j in range(n)))
# Killing equation explicitly: nabla_a xi_b + nabla_b xi_a = 0
xi_dn = g * xi_up
def cov_d(a, b):  # nabla_a xi_b
    return sp.diff(xi_dn[b], x[a]) - sum(Gam[c][a][b] * xi_dn[c] for c in range(n))
chk("C6b Killing equation nabla_(a xi_b) = 0 (all 16)",
    all(iszero(cov_d(a, b) + cov_d(b, a), "C6b[%d,%d]" % (a, b)) for a in range(n) for b in range(n)))
norm = sp.simplify((xi_up.T * g * xi_up)[0, 0])
chk("C6c xi.xi = -(1-2M/R)/(1+2E): timelike for R > 2M, null at 2M",
    sp.simplify(norm + f / (1 + 2 * E)) == 0)
# Frobenius: xi_[a d_b xi_c] = 0  (partial derivatives suffice for the 3-form)
def dxi(b, c):
    return sp.diff(xi_dn[c], x[b]) - sp.diff(xi_dn[b], x[c])
frob_ok = True
import itertools
for a, b, c in itertools.permutations(range(n), 3):
    val = xi_dn[a] * dxi(b, c) + xi_dn[b] * dxi(c, a) + xi_dn[c] * dxi(a, b)
    if not iszero(val, "C6d"):
        frob_ok = False
chk("C6d Frobenius xi ^ d xi = 0 => hypersurface-orthogonal => STATIC", frob_ok)
chk("C6e tau = const slices are NOT Killing-orthogonal: xi_R = v/(1+2E) != 0",
    sp.simplify(xi_dn[1]) != 0)

# ---- C7: E < 0 domain (M&P footnote [15]) -----------------------------------
Eneg = sp.symbols("Eneg", negative=True)
rmax = sp.solve(sp.Eq(2 * M / R + 2 * Eneg, 0), R)[0]
chk("C7a for E < 0 the shift sqrt(2M/R+2E) is real only for R <= -M/E",
    sp.simplify(rmax + M / Eneg) == 0)
chk("C7b M&P r_max: f(r_max) = Etilde^2 = 1+2E  <=>  r_max = -M/E",
    sp.simplify(sp.solve(sp.Eq(1 - 2 * M / R, 1 + 2 * Eneg), R)[0] + M / Eneg) == 0)
# numeric witness: E = -0.25, M = 1 -> r_max = 4;  at R = 10 the chart is complex
val = (2 * 1 / 10 + 2 * (-0.25))
chk("C7c witness E=-1/4, M=1: 2M/R+2E at R=10 is %.2f < 0 (chart absent there)" % val, val < 0)

# ---- C8: d3 table fixtures, independent integrator --------------------------
import math
try:
    import mpmath as mp
    have_mp = True
except ImportError:
    have_mp = False

def profile(Rr, R1, R2):
    xx = (Rr - R1) / (R2 - R1)
    return math.tanh(xx * (R2 - R1)) * math.tanh((1.0 - xx) * (R2 - R1))

def integrand(Rr, Mm, R1, R2, A):
    ff = 1.0 - 2.0 * Mm / Rr
    return 1.0 / (math.sqrt(ff) * math.cosh(A * profile(Rr, R1, R2)))

def simpson(fn, a, b, n=200000):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = fn(a) + fn(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * fn(a + i * h)
    return s * h / 3

Mm, R1, R2 = 1.0, 10.0, 100.0
fixtures = {0.0: 1.027240534, 1.0: 0.673057927, 80.0: 4.64434e-4}
owner_table = {0.0: 1.027241, 1.0: 0.673058, 2.0: 0.285058, 5.0: 0.021733,
               20.0: 0.001868, 80.0: 0.000464}
owner_gamma = {0.0: 0.989949, 1.0: 1.526650, 2.0: 3.721930, 5.0: 73.411700,
               20.0: 2.39954e+08, 80.0: 2.74007e+34}
print("   A      L/gap (Simpson n=2e5)   owner :270-275   fixture")
for A in (0.0, 1.0, 2.0, 5.0, 20.0, 80.0):
    L = simpson(lambda r: integrand(r, Mm, R1, R2, A), R1, R2)
    rat = L / (R2 - R1)
    line = "  %5.1f   %.9f            %.6f" % (A, rat, owner_table[A])
    if A in fixtures:
        line += "        %.9g" % fixtures[A]
        chk("C8 A=%g L/gap = %.9f vs fixture %.9g (rel %.1e)" % (A, rat, fixtures[A], abs(rat / fixtures[A] - 1)),
            abs(rat / fixtures[A] - 1) < 2e-5)
    chk("C8 A=%g L/gap vs owner table %.6f" % (A, owner_table[A]), abs(rat - owner_table[A]) < 1.5e-6 * max(1, 1 / owner_table[A]) or abs(rat - owner_table[A]) < 6e-7)
    # max Gamma = sqrt(f) cosh(A * profile), scanned finely
    gmax = max(math.sqrt(1 - 2 * Mm / r) * math.cosh(A * profile(r, R1, R2))
               for r in (R1 + i * (R2 - R1) / 20000 for i in range(20001)))
    chk("C8 A=%g max Gamma %.6g vs owner %.6g" % (A, gmax, owner_gamma[A]),
        abs(gmax / owner_gamma[A] - 1) < 2e-5)
    print(line)
chk("C8 static slice A=0: L/gap = int dR/sqrt(f) / 90 -> closed form",
    abs(simpson(lambda r: integrand(r, Mm, R1, R2, 0.0), R1, R2)
        - (lambda a, b: (math.sqrt(b * (b - 2)) + 2 * math.log(math.sqrt(b) + math.sqrt(b - 2)))
           - (math.sqrt(a * (a - 2)) + 2 * math.log(math.sqrt(a) + math.sqrt(a - 2))))(R1, R2)) < 1e-9)
# Discrepancy (recorded, not repaired): foliation.py:512 docstring says "Simpson"
# but the loop at :519-521 uses trapezoid weights (1 interior, 1/2 ends).
# Also :964 checks anchoring on _bump, while d3_table runs flat_top=True.
chk("C8 flat_top profile vanishes at both mouths (the profile actually run)",
    profile(R1, R1, R2) == 0.0 and abs(profile(R2, R1, R2)) < 1e-15)

# ---- C9: Shapiro -------------------------------------------------------------
excess = 2 * Mm * math.log((R2 - 2 * Mm) / (R1 - 2 * Mm))
chk("C9 Shapiro excess over areal gap = %.4f M (owner :72 says 5.011)" % excess,
    abs(excess - 5.011) < 5e-4)

print()
print("zero-test routes used:")
for k in sorted(ROUTE):
    if ROUTE[k] != "symbolic":
        print("  %s -> %s" % (k, ROUTE[k]))
print("  (all others closed symbolically)")
print("FAILURES: %d" % len(fails))
for fl in fails:
    print("  " + fl)
sys.exit(1 if fails else 0)
