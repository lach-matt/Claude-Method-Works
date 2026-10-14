#!/usr/bin/env python3
"""b4_regular.py -- Warp Theorem lemma B4, step 4: is the bulk regular where the hold can reach?

Item 152 (2): B4 as a brief forward evolution, "an option ... check it".  b4_global.py settled the topology (one end, CGS
Thm 3.5's deformation, fixed before the opening) and the far boundary (untouched Randall-Sundrum II, 3/R).  What is left
of B4 is W2: the bulk stays regular -- globally hyperbolic -- through the hold.  This is what the board can say about it.

  R1 THE CURVATURE TEST (computed, with controls).  The Kretschmann scalar of ds^2 = -A dt^2 + B dr^2 + C dOmega^2 + dy^2,
      A, B, C functions of (r, y), is built symbolically (~3 s).  Checked (i) on the black string, A = e^{-2y/ell}(1-2m/r),
      B = e^{-2y/ell}/(1-2m/r), C = e^{-2y/ell} r^2: it gives 48 m^2 e^{4y/ell}/r^6 + 40/ell^4 exactly, and m = 0 gives
      AdS5's 40/ell^4; and (ii) on a generic metric, where A_y/A, B_y/B, C_y/C all differ (the black string has them
      equal), against an independent full contraction R_abcd R^abcd with no symmetry shortcut, at a point
  R2 WHAT THE HOLD REQUIRES: A NECESSARY CONDITION AT A FINITE DEPTH (deduced, within a locally analytic class; standard,
      not READ).  During the hold the plane carries eq. (17), static.  Where the bulk is analytic -- the class in which
      localbulk L4 makes the local bulk unique (B2) -- the plane's data over the hold fix the bulk in that time-slab's
      double cone (Cauchy-Kovalevskaya; Holmgren-John uniqueness is for linear analytic problems, and outside the
      analytic class unique continuation across a timelike surface can fail, Alinhac-Baouendi), and there it is the
      static local bulk.  The class can only be local: a bulk analytic everywhere and static over a slab would be static
      for ever, with no opening or closing.  The hold was taken as 28.4777 clocks of far (Killing) time -- O3's per-bit
      figure, since withdrawn (b4_static.py S4); the figures below are at that withdrawn hold -- and the depth the
      double cone reaches is set by the bulk's lapse sqrt(A), which at the plane is sqrt(F) -- 0.156 at r = 2.05m and 0
      at the throat: the depth D(r) solves  integral_0^D dy / sqrt(A(r, y)) = t_h / 2.  With the black-string lapse
      sqrt(F) e^{-y/ell}, D = ell ln(1 + sqrt(F) t_h/(2 ell)) (sqrt(F) t_h/2 as ell >> r0); with the series' own A it is
      read off the banked coefficients.  So the requirement is weakest at the throat (D -> 0 as r -> 2m, the extremal
      horizon's redshift) and grows outward:
          ell >> r0: about 1.9-2.2m at r = 2.05m, 4.7m at r = 2.25m, 8.2m at r = 3m;
          ell = r0:  about 1.2-1.5m at r = 2.05m.
      Necessary, not sufficient.  Sufficiency also needs: the non-static opening and closing, which static data do not
      fix; W1's pointwise null-energy thickening (B5); W3 for all time (b4_global.py B4c, with H-WEAK-RADIATION); no
      excised region inside T (b4_global.py B4a's control); and initial data beyond the double cone joined regularly to
      the exterior (H-GLUING, the board's -- gluing theorems exist for data with no plane; none was READ for a bulk with
      one)
  R3 WHAT THE STATIC SERIES SHOWS (computed from banked coefficients, b4_series.json, checked at selftest against a
      fresh low-order solve; --regenerate rebuilds it, about 110 min).  K is evaluated from the metric's own Taylor
      polynomials at three orders; a depth is "series-stable" where the top two orders agree within 1%.  This is a
      convergence test, not a certificate: within the convergent region, with A, B, C > 0, K is finite automatically,
      and agreement of two orders is a heuristic (at r = 2.25m it fails at 1.8-1.9m and returns at 2.0m).
      ell >> r0 -- the regime above r0; measurement bounds ell only from above, at tens of micrometres, so ell < r0 is
      not excluded, and it is not computed (BULKSERIES OPEN 2): at r = 2.05m series-stable to 1.5m (marginal: orders 10
      and 12 differ by 0.9% there, 8 and 10 by 8%), K rising gently 1.04 -> 3.79, A, B, C positive -- against 1.9-2.2m
      needed.  At r = 3m series-stable to 2.25m against 8.2m needed.  NOT DECIDED, at every r tested.
      ell = r0: at r = 2.05m series-stable to 0.65m; beyond, the truncations diverge near the series' radius (BULKSERIES
      B5: about 1.29m), where g_tt and g_rr fall toward zero together.  A curvature singularity and a bulk horizon (where
      K stays finite) are NOT distinguished.  Needed: 1.2-1.5m.  NOT SHOWN
  R4 B4 IS NOT FREE OF k's SCALE (deduced).  The required depth and the evidence both depend on ell (2.2m against 1.5m at
      r = 2.05m), and so does the far boundary (b4_global.py B4c: ell > 2 R_reach).  So b6_k.py's "every clause free of
      k's scale" holds for the clauses it checks, not for B4; the theorem's B6 says so
Stdlib + sympy (+ numpy for evaluation).  python3 b4_regular.py [--selftest] [--regenerate]
"""
import json
import math
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
BANK = os.path.join(HERE, "b4_series.json")
HOLD = 2 * math.pi**2 / math.log(2)                      # the withdrawn per-bit hold, 28.4777 clocks (b4_static.py S4)


def kretschmann():
    t, r, th, ph, y = sp.symbols("t r theta phi y")
    A, B, C = [sp.Function(n)(r, y) for n in "ABC"]
    X = [t, r, th, ph, y]
    g = sp.diag(-A, B, C, C * sp.sin(th) ** 2, 1)
    gi = sp.diag(-1 / A, 1 / B, 1 / C, 1 / (C * sp.sin(th) ** 2), 1)
    n = 5
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]

    def riem(a, b, c, d):
        return (sp.diff(Gam[a][d][b], X[c]) - sp.diff(Gam[a][c][b], X[d])
                + sum(Gam[a][c][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][c][b] for e in range(n)))
    K = 0
    dg = [g[i, i] for i in range(n)]
    di = [gi[i, i] for i in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(c + 1, n):
                    Rv = sp.simplify(riem(a, b, c, d))
                    if Rv != 0:
                        K += 2 * dg[a] * Rv * di[b] * di[c] * di[d] * Rv
    K = K.subs(th, sp.pi / 3)                              # spherical symmetry: independent of theta
    syms = {}
    for F, nm in ((A, "A"), (B, "B"), (C, "C")):
        for i in range(3):
            for j in range(3 - i):
                if i + j:
                    syms[sp.Derivative(F, *([r] * i + [y] * j))] = sp.Symbol(nm + "_" + "r" * i + "y" * j)
        syms[F] = sp.Symbol(nm)
    return sp.simplify(K.subs(syms)), (r, y)


def black_string_check(K, ry):
    r, y = ry
    m, ell = sp.symbols("m ell", positive=True)
    w = sp.exp(-2 * y / ell)
    funcs = {"A": w * (1 - 2 * m / r), "B": w / (1 - 2 * m / r), "C": w * r**2}
    env = {}
    for nm, f in funcs.items():
        for i in range(3):
            for j in range(3 - i):
                e = f
                if i:
                    e = sp.diff(e, r, i)
                if j:
                    e = sp.diff(e, y, j)
                env[sp.Symbol(nm + ("_" + "r" * i + "y" * j if i + j else ""))] = e
    val = sp.simplify(K.subs(env))
    want = 48 * m**2 * sp.exp(4 * y / ell) / r**6 + 40 / ell**4
    return sp.simplify(val - want) == 0, sp.simplify(val.subs(m, 0) - 40 / ell**4) == 0


def depth_blackstring(F, ell):
    """D with the black-string lapse sqrt(F) e^{-y/ell}; ell None is the flat limit."""
    return math.sqrt(F) * HOLD / 2 if ell is None else ell * math.log(1 + math.sqrt(F) * HOLD / (2 * ell))


def depth_series(bank, setname, rkey, ymax=3.0, n=30001):
    """D from the series' own A: integral_0^D dy/sqrt(A) = t_h/2.  None if A vanishes first (a bulk horizon in the
    truncation) or D lies beyond ymax."""
    A = np.polynomial.Polynomial(bank["sets"][setname]["r"][rkey]["A_0"])
    ys = np.linspace(0, ymax, n)
    av = A(ys)
    if (av <= 0).any():
        cut = int(np.argmax(av <= 0))
        ys, av = ys[:cut], av[:cut]
    f = 1 / np.sqrt(av)
    T = np.concatenate([[0.0], np.cumsum((f[1:] + f[:-1]) / 2 * np.diff(ys))])
    i = int(np.searchsorted(T, HOLD / 2))
    return float(ys[i]) if i < len(ys) else None


def k_profile(K, bank, setname, rkey, ys):
    names = sorted(K.free_symbols, key=str)
    Kf = sp.lambdify(names, K, "numpy")
    S = bank["sets"][setname]
    top = S["order"]
    orders = [top - 4, top - 2, top]
    e = S["r"][rkey]
    out = []
    for yv in ys:
        vals = []
        for o in orders:
            env = {}
            for X in "ABC":
                for i in range(3):
                    p = np.polynomial.Polynomial(e["%s_%d" % (X, i)][:o + 1])
                    for j in range(3 - i):
                        q = p.deriv(j) if j else p
                        env[X + ("_" + "r" * i + "y" * j if i + j else "")] = q(yv)
            vals.append(float(Kf(*[env[str(s)] for s in names])))
        abc = [float(np.polynomial.Polynomial(e["%s_0" % X])(yv)) for X in "ABC"]
        out.append({"y": yv, "K": vals, "ABC": abc, "agree": abs(vals[2] - vals[1]) <= 0.01 * abs(vals[2])})
    shown = 0.0
    for row in out:
        if not row["agree"]:
            break
        shown = row["y"]
    return {"orders": orders, "rows": out, "shown_to": shown}


YS = [round(0.05 * i, 2) for i in range(0, 61)]
SETS = ["flat (ell >> r0), order 12", "ell = r0, order 11"]


def generic_check(K):
    """K by the formula against an independent full contraction, on a metric with unequal A_y/A, B_y/B, C_y/C."""
    t, r, th, ph, y = sp.symbols("t r theta phi y")
    funcs = {"A": (1 + r * y / 3 + y**2) / r, "B": sp.exp(y / 2) * (1 + 1 / r), "C": r**2 * (1 + y + y**3 / 5)}
    X = [t, r, th, ph, y]
    g = sp.diag(-funcs["A"], funcs["B"], funcs["C"], funcs["C"] * sp.sin(th) ** 2, 1)
    gi = g.inv()
    n = 5
    G = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(n)) / 2
           for c in range(n)] for b in range(n)] for a in range(n)]
    pt = {r: sp.Rational(5, 2), y: sp.Rational(3, 10), th: sp.pi / 3}
    Rup = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = (sp.diff(G[a][d][b], X[c]) - sp.diff(G[a][c][b], X[d])
                         + sum(G[a][c][e2] * G[e2][d][b] - G[a][d][e2] * G[e2][c][b] for e2 in range(n)))
                    Rup[a, b, c, d] = sp.N(e.subs(pt), 30)
    gn = g.subs(pt).evalf(30)
    gin = gi.subs(pt).evalf(30)
    low = {(a, b, c, d): sum(gn[a, e2] * Rup[e2, b, c, d] for e2 in range(n))
           for a in range(n) for b in range(n) for c in range(n) for d in range(n)}
    full = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if low[a, b, c, d] == 0:
                        continue
                    up = gin[b, b] * gin[c, c] * gin[d, d] * Rup[a, b, c, d]   # diagonal metric
                    full += low[a, b, c, d] * up
    env = {}
    for nm, f in funcs.items():
        for i in range(3):
            for j in range(3 - i):
                e = f
                if i:
                    e = sp.diff(e, r, i)
                if j:
                    e = sp.diff(e, y, j)
                env[sp.Symbol(nm + ("_" + "r" * i + "y" * j if i + j else ""))] = e.subs(pt)
    formula = sp.N(K.subs(env), 30)
    return float(full), float(formula)


def bank_check(bank):
    """A fresh solve through y^3 at r = 41/20, both regimes, against the bank."""
    import contextlib
    import importlib.util
    import io
    spec = importlib.util.spec_from_file_location("b4r_bs_chk", os.path.join(D68, "bulk", "bulkseries.py"))
    bs = importlib.util.module_from_spec(spec)
    saved = list(sys.argv)
    sys.argv = ["x"]
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(bs)
    sys.argv = saved
    r = bs.r
    F = 1 - 2 / r
    H = (1 - 2 / r) ** 2 / (1 - sp.Rational(3, 2) / r)
    worst = 0.0
    for name, k in [(SETS[0], sp.Integer(0)), (SETS[1], sp.Rational(1, 2))]:
        co = bs.solve(F, H, 3, k)
        e = bank["sets"][name]["r"]["41/20"]
        for X in "ABC":
            for i in range(3):
                fresh = [float((sp.diff(sp.sympify(c), r, i) if i else sp.sympify(c)).subs(r, sp.Rational(41, 20)))
                         for c in co[X][:4]]
                for a_, b_ in zip(fresh, e["%s_%d" % (X, i)][:4]):
                    worst = max(worst, abs(a_ - b_) / max(1e-12, abs(a_)))
    return worst


def compute():
    K, ry = kretschmann()
    bs_ok, ads_ok = black_string_check(K, ry)
    bank = json.load(open(BANK))
    prof = {(s_, rk): k_profile(K, bank, s_, rk, YS) for s_ in SETS for rk in ("41/20", "9/4", "3")}
    F = {rk: 1 - 2 / float(sp.Rational(rk)) for rk in ("41/20", "9/4", "3")}
    need = {(s_, rk): {"bs": depth_blackstring(F[rk], None if s_ == SETS[0] else 2.0),
                      "series": depth_series(bank, s_, rk)} for s_ in SETS for rk in F}
    full, formula = generic_check(K)
    return {"bs_ok": bs_ok, "ads_ok": ads_ok, "prof": prof, "need": need, "generic": (full, formula),
            "bank_err": bank_check(bank)}


def report(d):
    print("b4_regular.py -- Warp Theorem lemma B4b, the bulk regular through the hold\n")
    print("R1 Kretschmann formula: black string %s; AdS5 control %s; generic metric, formula %.12g against full "
          "contraction %.12g" % (d["bs_ok"], d["ads_ok"], d["generic"][1], d["generic"][0]))
    print("   bank against a fresh solve through y^3: worst relative difference %.1e" % d["bank_err"])
    for (s_, rk), p in d["prof"].items():
        nd = d["need"][(s_, rk)]
        last = [row for row in p["rows"] if row["y"] == p["shown_to"]][0]
        print("R2/R3 %-28s r = %-5s needed: %.2f m (black-string lapse), %s (series lapse); series-stable to %.2f m "
              "(K = %.4g)" % (s_, rk, nd["bs"], "%.2f m" % nd["series"] if nd["series"] is not None else "beyond the "
                              "series' range", p["shown_to"], last["K"][2]))


def regenerate():
    """Rebuild b4_series.json from bulk/bulkseries.py (about 30 min flat at order 12, 80 min at ell = r0 order 11:
    about 110 min)."""
    import contextlib
    import importlib.util
    import io
    spec = importlib.util.spec_from_file_location("b4r_bs", os.path.join(D68, "bulk", "bulkseries.py"))
    bs = importlib.util.module_from_spec(spec)
    saved = list(sys.argv)
    sys.argv = ["x"]
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(bs)
    sys.argv = saved
    r = bs.r
    F = 1 - 2 / r
    H = (1 - 2 / r) ** 2 / (1 - sp.Rational(3, 2) / r)
    out = {"note": "Taylor coefficients in y of A, B, C and their first two r-derivatives at fixed r, units m = 1; "
                   "from bulk/bulkseries.py solve(F, H, order, k) with eq. (17)'s F, H; generated by lemmas/"
                   "b4_regular.py --regenerate", "sets": {}}
    for name, k, order in [(SETS[0], sp.Integer(0), 12), (SETS[1], sp.Rational(1, 2), 11)]:
        co = bs.solve(F, H, order, k)
        dset = {"k": str(k), "order": order, "r": {}}
        for rv in ["41/20", "21/10", "9/4", "3"]:
            R = sp.Rational(rv)
            e = {}
            for X in "ABC":
                for i in range(3):
                    e["%s_%d" % (X, i)] = [float(sp.N((sp.diff(sp.sympify(c), r, i) if i else sp.sympify(c)).subs(r, R),
                                                      20)) for c in co[X]]
            dset["r"][rv] = e
        out["sets"][name] = dset
    json.dump(out, open(BANK, "w"), indent=0)


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("R1: the Kretschmann formula gives the black string's 48 m^2 e^{4y/ell}/r^6 + 40/ell^4 exactly", d["bs_ok"])
    chk("R1 controls: m = 0 gives AdS5's 40/ell^4; on a generic metric the formula equals a full contraction",
        d["ads_ok"] and abs(d["generic"][0] - d["generic"][1]) < 1e-9 * abs(d["generic"][0]))
    chk("R3: the banked coefficients agree with a fresh solve through y^3", d["bank_err"] < 1e-12)
    nf = d["need"][(SETS[0], "41/20")]
    nr = d["need"][(SETS[1], "41/20")]
    chk("R2: the double cone's depth at r = 2.05m: ~2.2m (black-string lapse) / ~1.9m (series) for ell >> r0, "
        "~1.5m / ~1.2m at ell = r0", abs(nf["bs"] - 2.223) < 0.01 and nf["series"] is not None
        and 1.8 < nf["series"] < 2.0 and abs(nr["bs"] - 1.494) < 0.01 and nr["series"] is not None
        and 1.1 < nr["series"] < 1.3)
    pf = d["prof"][(SETS[0], "41/20")]
    k12 = [row for row in pf["rows"] if row["y"] == 1.2][0]
    chk("R3 ell >> r0: series-stable to 1.5m at r = 2.05m, K gentle, A, B, C positive -- short of the ~1.9m needed",
        1.5 <= pf["shown_to"] < nf["series"] and k12["K"][2] < 2 and min(k12["ABC"]) > 0)
    pr = d["prof"][(SETS[1], "41/20")]
    chk("R3 ell = r0: series-stable only to < 0.8m at r = 2.05m -- short of the ~1.2m needed",
        pr["shown_to"] < 0.8 and pr["shown_to"] < nr["series"])
    p3 = d["prof"][(SETS[0], "3")]
    n3 = d["need"][(SETS[0], "3")]
    chk("R2/R3 ell >> r0 away from the throat (r = 3m): stable deeper (>= 2m) but more is needed (~8.2m) -- not decided",
        p3["shown_to"] >= 2.0 and abs(n3["bs"] - 8.22) < 0.05 and p3["shown_to"] < n3["bs"])
    chk("R4 (deduced): the required depth depends on ell (2.2m against 1.5m at r = 2.05m)", abs(nf["bs"] - nr["bs"]) > 0.5)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--regenerate" in sys.argv:
        regenerate()
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        report(compute())
