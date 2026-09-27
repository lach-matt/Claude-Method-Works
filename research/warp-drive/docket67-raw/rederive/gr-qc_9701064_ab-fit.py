#!/usr/bin/env python3
"""DOCKET 67 -- audit of gr-qc/9701064#ab-fit: HPS's far-zone law
sqrt F = a ln l - b, a = 5.3, b = 25.5 (hpscentre.py:245, "HPS p.8").

The source could NOT be read this run (alphaXiv quota exhausted; arxiv.org and
every mirror EGRESS_BLOCKED), so (5.3, 25.5) and "F", "l", the length unit are
taken AS THE TREE READS THEM, and every conclusion below is conditional on
that reading.  Nothing here is written into research/warp-drive: the tree's
hpscentre.py / throatmass.py are imported from a COPY in _hps_tree/ (md5
recorded), the tree dir is only APPENDED to sys.path for their seated imports,
and bytecode writing is disabled.

PART A  (sympy, closed form -- independent of the integrations)
  A1  a is invariant under a change of length unit; b is not:
      l -> lam l  sends (a, b) -> (a, b + a ln lam).  So b = 25.5 is a number
      only together with HPS's unit of l.  Computes b in K units if HPS's l
      were in l_P (K = l_P/sqrt(5760 pi), the tree's K_in_planck()).
  A2  the law's own zero l0 = exp(b/a): the law cannot hold at l ~ l0, so it is
      a far-zone law for l >> l0 only (a hypothesis HPS's use needs).
  A3  a two-parameter log fit to a function whose log-slope drifts returns a
      window-dependent a: exact least-squares on g = A ln x - B + C ln ln x
      (continuous, log-uniform weight) -- a_fit = A + C * <1/ln x>-type term,
      shown symbolically to depend on the window unless C = 0.

PART B  (numeric -- the tree's own integrations, re-run from the copy)
  B1  both readings (printed M1, conserved) of HPS eq. (9), ln f(0) = -2/3,
      integrated to X = 1e5 K; the tree's window sweep (FAR_ZONE_WINDOWS +
      FULL) re-fitted; attribution() re-run.
  B2  the LOCAL slope a_loc(l) = d sqrt f / d ln l (ripple-averaged over one
      decade-fraction) at l = 500 ... 1e5: does a converge?
  B3  a fine scan of windows [lo, hi] (lo, hi on a log grid in [500, 1e5]):
      in how many does each system match (5.3, 25.5) within 5 %?  Does any
      window give b near the l_P-unit value from A1?
Exit 0 always; the verdicts are printed, not asserted, except the sympy
identities (A1-A3), which are asserted.
"""
import math
import os
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
COPY = os.path.join(HERE, "_hps_tree")
REAL = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, COPY)
sys.path.append(REAL)          # achievable, foliation -- read only

import sympy as sp

FAIL = []


def chk(name, ok):
    print(("  PASS " if ok else "  FAIL ") + name)
    if not ok:
        FAIL.append(name)


A_P, B_P = 5.3, 25.5
TOL = 0.05

print("PART A -- closed form (sympy)")
a, b, lam, l, x = sp.symbols("a b lam l x", positive=True)
# A1: sqrt F = a ln(l) - b with l = lam * l'
lp = sp.symbols("lp", positive=True)
expr = sp.expand_log(a*sp.log(lam*lp) - b, force=True)
a_new = sp.simplify(sp.diff(expr, lp)*lp)             # coefficient of ln l'
b_new = sp.simplify(-(expr - a_new*sp.log(lp)))       # minus the constant
chk("A1 a invariant under l -> lam l", sp.simplify(a_new - a) == 0)
chk("A1 b -> b - a ln lam  (l = lam l')", sp.simplify(b_new - (b - a*sp.log(lam))) == 0)
K_lP = 1/sp.sqrt(5760*sp.pi)          # K in l_P (hpscentre.K_in_planck)
# if HPS's l is in l_P: x_P = l/l_P = x_K * K/l_P  -> l(in l_P) = (K/l_P) * x_K, lam = K/l_P
b_K_if_lP = B_P - A_P*float(sp.log(K_lP))
print("     K = %.6f l_P;  ln(l_P/K) = %.4f" % (float(K_lP), float(-sp.log(K_lP))))
print("     b in K units IF HPS's l were in l_P: %.3f  (vs 25.5 if l is in K)" % b_K_if_lP)
print("     b/a = %.4f  vs  ln(l_P/K) = %.4f  (ratio %.4f) -- recorded, not interpreted"
      % (B_P/A_P, float(-sp.log(K_lP)), (B_P/A_P)/float(-sp.log(K_lP))))
# A2
l0 = math.exp(B_P/A_P)
print("A2   zero of the law: l0 = exp(b/a) = %.2f (HPS's unit of l)" % l0)
for L in (500, 2000, 1e4, 1e5):
    print("     sqrt F(%g) = %.3f   F = %.2f" % (L, A_P*math.log(L) - B_P, (A_P*math.log(L) - B_P)**2))
chk("A2 l0 lies below every tree window's lower edge (500 K)", l0 < 500)
# A3: continuous least squares of g(u) = A u - B + C ln u  (u = ln x) on u in [u1, u2]
A, B, C, u, u1, u2 = sp.symbols("A B C u u1 u2", positive=True)
s1, s0 = sp.symbols("s1 s0")
g = A*u - B + C*sp.log(u)
E = sp.integrate((g - (s1*u - s0))**2, (u, u1, u2))
sol = sp.solve([sp.diff(E, s1), sp.diff(E, s0)], [s1, s0], dict=True)[0]
s1f = sp.simplify(sol[s1])
dep = sp.simplify(sp.diff(s1f, u2))
num1 = float(s1f.subs({A: 1, C: 1, u1: math.log(500), u2: math.log(2000)}))
num2 = float(s1f.subs({A: 1, C: 1, u1: math.log(5000), u2: math.log(1e4)}))
chk("A3 fitted slope = A exactly when C = 0 (window-free)", sp.simplify(s1f.subs(C, 0) - A) == 0)
chk("A3 fitted slope depends on the window when C != 0 (d s1/d u2 != 0)",
    sp.simplify(dep.subs({A: 1, C: 1, u1: 6, u2: 8})) != 0)
print("     toy A = C = 1: slope over [500,2000] = %.4f, over [5000,1e4] = %.4f" % (num1, num2))

print("\nPART B -- the tree's integrations, re-run from the copy")
import hashlib
for fn in ("hpscentre.py", "throatmass.py"):
    print("     %s md5 %s" % (fn, hashlib.md5(open(os.path.join(COPY, fn), "rb").read()).hexdigest()))
import numpy as np
import hpscentre as H

X = float(os.environ.get("HPS_X", "100000"))
t0 = time.time()
L0 = sp.Rational(*H.HPS_LNF0_RUN)
r0 = float(sp.sqrt(-16*L0))
y0 = [math.exp(float(L0)), 0, 0, 0, r0, 0, 0, 0]
runs = {}
for name, reading in (("printed", H.PRINTED_M1), ("conserved", H.CONSERVED)):
    num = H.numeric_system(sp, reading)
    res = H.integrate(num, y0, 0, X, rtol=1e-10)
    runs[name] = res
    print("     %-9s status %s end x = %.1f K  (%.0f s)" % (name, res.status, res.t[-1], time.time() - t0))

wins = H.FAR_ZONE_WINDOWS + (H.FAR_ZONE_WINDOWS_FULL if X >= 1e5 else ())
sweep = {nm: {w: H.far_zone_fit(runs[nm], *w) for w in wins} for nm in runs}
print("B1   window sweep (a, b) -- HPS print (5.3, 25.5):")
for w in wins:
    print("     %-24s printed %-20s conserved %s" % (w, H._fmt_fit(sweep['printed'][w]),
                                                    H._fmt_fit(sweep['conserved'][w])))
one = {nm: {H.WITHDRAWN_ATTRIBUTION_WINDOW: sweep[nm][H.WITHDRAWN_ATTRIBUTION_WINDOW]} for nm in runs}
print("     attribution, withdrawn window alone: %s" % H.attribution(one))
print("     attribution, every window:           %s  (tree flag %r)"
      % (H.attribution(sweep), H.HPS_INTEGRATED_THE_PRINTED_SYSTEM))

print("B2   local slope a_loc(l) = d sqrt f/d ln l, averaged over [l/1.25, l*1.25]:")
aloc = {}
for nm, res in runs.items():
    row = []
    for L in (500, 1000, 2000, 5000, 1e4, 2e4, 5e4, 8e4):
        if L*1.25 > res.t[-1]:
            continue
        xs = np.geomspace(L/1.25, L*1.25, 20001)
        s = np.sqrt(res.sol(xs)[0])
        slope, icpt = np.polyfit(np.log(xs), s, 1)
        row.append((L, float(slope), float(-icpt)))
    aloc[nm] = row
    print("     %-9s " % nm + "  ".join("%g:%.3f" % (L, s) for L, s, _ in row))
    # convergence test: increment of a_loc per unit ln l between successive points
    inc = ["%.3f" % ((row[k+1][1]-row[k][1])/math.log(row[k+1][0]/row[k][0])) for k in range(len(row)-1)]
    print("     %-9s d a_loc / d ln l between successive points: %s" % (nm, " ".join(inc)))

print("B4   does a_loc approach a constant?  fit a_loc(l) = a_inf - c l^(-q) to the points l >= 2000")
from scipy.optimize import curve_fit
for nm, row in aloc.items():
    Ls = np.array([r[0] for r in row if r[0] >= 2000]); As = np.array([r[1] for r in row if r[0] >= 2000])
    try:
        (ainf, c, q), _ = curve_fit(lambda L, ai, c, q: ai - c*L**(-q), Ls, As, p0=(As[-1] + 0.2, 10.0, 0.5), maxfev=20000)
        resid = float(np.max(np.abs(As - (ainf - c*Ls**(-q)))))
        print("     %-9s a_inf = %.3f  c = %.3g  q = %.3f  (max resid %.1e) -- EXTRAPOLATION, not a measurement;"
              " a_inf/5.3 - 1 = %+.1f %%" % (nm, ainf, c, q, resid, 100*(ainf/A_P - 1)))
    except Exception as e:
        print("     %-9s fit failed: %s" % (nm, e))
    # alternative: a_loc linear in 1/ln l
    X1 = 1/np.log(Ls); co = np.polyfit(X1, As, 1)
    print("     %-9s alt. model a_loc = a_inf + k/ln l: a_inf = %.3f (max resid %.1e)"
          % (nm, co[1], float(np.max(np.abs(As - np.polyval(co, X1))))))

print("B3   fine window scan: lo, hi on a 25-point log grid in [500, X], hi/lo >= 2, lin sampling")
grid = np.geomspace(500, X, 25)
count = {nm: [0, 0] for nm in runs}
both_hit = []
bmax = {nm: -1e9 for nm in runs}
amatch = {nm: [] for nm in runs}
for i, lo in enumerate(grid):
    for hi in grid[i+1:]:
        if hi/lo < 2:
            continue
        hit = []
        for nm, res in runs.items():
            ab = H.far_zone_fit(res, float(lo), float(hi), "lin", n=20001)
            if ab is None:
                continue
            count[nm][1] += 1
            bmax[nm] = max(bmax[nm], ab[1])
            if H.matches_hps(ab):
                count[nm][0] += 1
                amatch[nm].append((round(float(lo)), round(float(hi)), round(ab[0], 3), round(ab[1], 3)))
                hit.append(nm)
        if len(hit) == 2:
            both_hit.append((round(float(lo)), round(float(hi))))
for nm in runs:
    print("     %-9s matches (5.3, 25.5) within 5%% in %d of %d windows; max b over scan %.2f"
          % (nm, count[nm][0], count[nm][1], bmax[nm]))
    for m in amatch[nm][:12]:
        print("        match window %s" % (m,))
print("     windows where BOTH systems match: %d %s" % (len(both_hit), both_hit[:10]))
print("     b in K units if HPS's l were l_P = %.2f: reached by any scanned window? %s"
      % (b_K_if_lP, any(bmax[nm] >= b_K_if_lP*(1 - TOL) for nm in runs)))
print("\nsympy identities: %s" % ("ALL PASS" if not FAIL else "FAIL: %s" % FAIL))
print("elapsed %.0f s" % (time.time() - t0))
