#!/usr/bin/env python3
"""b4_regular.py -- Warp Theorem lemma B4, step 4: is the bulk regular where the hold can reach?

Item 152 (2): B4 as a brief forward evolution, "an option ... check it".  b4_global.py settled the topology (one end, CGS
Thm 3.5's deformation, fixed before the opening) and the far boundary (untouched Randall-Sundrum II, 3/R).  What is left
of B4 is W2: the bulk stays regular -- globally hyperbolic -- through the hold.  This is what the board can say about it.

  R1 THE CURVATURE TEST (computed, with control).  The Kretschmann scalar of ds^2 = -A dt^2 + B dr^2 + C dOmega^2 + dy^2,
      A, B, C functions of (r, y), is built symbolically (~3 s) and checked on the black string, A = e^{-2y/ell}(1-2m/r),
      B = e^{-2y/ell}/(1-2m/r), C = e^{-2y/ell} r^2: it gives 48 m^2 e^{4y/ell}/r^6 + 40/ell^4 exactly.  Control: m = 0
      gives AdS5's 40/ell^4
  R2 WHAT THE HOLD REQUIRES: A NECESSARY CONDITION AT A FINITE DEPTH (deduced; standard, not READ).  During the hold the
      plane carries eq. (17), static.  In the analytic class -- where localbulk L4 makes the local bulk unique (B2) --
      static plane data give the static local bulk, and the plane's data over a hold of length t_h fix the bulk within
      the double cone of that time-slab (Cauchy-Kovalevskaya with Holmgren-John uniqueness; standard, not READ): to a
      depth of half the light-reach, D = ell ln(1 + t_h/(2 ell)) in the Randall-Sundrum depth, t_h/2 as ell >> r0.  With
      t_h = 28.4777 clocks (O3): D = 4.189 m at ell = r0, 14.24 m as ell >> r0.  So B4 under item 152 (2) REQUIRES the
      static local bulk of eq. (17) to be regular to depth D at the throat.  It is necessary, not sufficient: sufficiency
      also needs initial data beyond that region joined regularly to the untouched exterior (H-GLUING, the board's;
      gluing theorems exist for asymptotically flat and hyperbolic data without a plane, none was READ for a bulk with one)
  R3 WHAT THE STATIC SERIES SHOWS (computed from banked coefficients, b4_series.json; regenerate with --regenerate, about
      90 min).  K is evaluated from the metric's own Taylor polynomials at three orders, and a depth counts as shown only
      where the top two orders agree within 1%.
      ell >> r0 (the regime measurement leaves: ell is bounded above at tens of micrometres, r0 is 4e-28 m at the example
      README): at r = 2.05m, K is shown to 1.5m deep, rising gently (1.04 -> 3.79); A, B, C stay positive.  1.5m of the
      14.24m needed: NOT DECIDED.
      ell = r0: at r = 2.05m, K is shown only to about 0.6m; beyond, the orders climb apart (to ~2e4 at 1.2m) and A and B
      fall toward zero together near 1.28m, short of the 4.19m needed: NOT SHOWN, and leaning singular.
      Control: away from the throat, at r = 3m, the flat limit is shown to 2m with K nearly flat (0.062 -> 0.075), and
      ell = r0 is shown twice as deep as at the throat (1.2m against 0.65m), K bounded (~4.6): the trouble is the throat's
  R4 B4 IS NOT FREE OF k's SCALE (computed).  D and the evidence both depend on ell.  So b6_k.py's "every clause free of
      k's scale" holds for the clauses it lists, not for B4 -- reported, not hidden
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
HOLD = 2 * math.pi**2 / math.log(2)                      # O3's 28.4777 clocks, exact form


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


def required_depth(ell):
    return HOLD / 2 if ell is None else ell * math.log(1 + HOLD / (2 * ell))


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


YS = [round(0.05 * i, 2) for i in range(0, 41)]
SETS = ["flat (ell >> r0), order 12", "ell = r0, order 11"]


def compute():
    K, ry = kretschmann()
    bs_ok, ads_ok = black_string_check(K, ry)
    bank = json.load(open(BANK))
    prof = {(s, rk): k_profile(K, bank, s, rk, YS) for s in SETS for rk in ("41/20", "3")}
    return {"bs_ok": bs_ok, "ads_ok": ads_ok, "D_r0": required_depth(2.0), "D_flat": required_depth(None),
            "prof": prof}


def report(d):
    print("b4_regular.py -- Warp Theorem lemma B4, step 4\n")
    print("R1 Kretschmann formula reproduces the black string: %s; AdS5 control: %s" % (d["bs_ok"], d["ads_ok"]))
    print("R2 required regular depth at the throat: %.3f m at ell = r0, %.3f m as ell >> r0" % (d["D_r0"], d["D_flat"]))
    for (s, rk), p in d["prof"].items():
        last = [row for row in p["rows"] if row["y"] == p["shown_to"]][0]
        far = [row for row in p["rows"] if abs(row["y"] - 1.2) < 1e-9][0]
        print("R3 %-28s r = %-5s orders %s: shown to y = %.2f m (K = %.4g); at 1.2 m K = %s; A,B,C there %s"
              % (s, rk, p["orders"], p["shown_to"], last["K"][2], ", ".join("%.4g" % v for v in far["K"]),
                 ", ".join("%.3g" % v for v in far["ABC"])))


def regenerate():
    """Rebuild b4_series.json from bulk/bulkseries.py (about 30 min flat at order 12, 80 min at ell = r0 order 11)."""
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
    chk("R1 control: m = 0 gives AdS5's 40/ell^4", d["ads_ok"])
    chk("R2: the hold requires regularity to 4.189 m (ell = r0) and 14.24 m (ell >> r0) at the throat",
        abs(d["D_r0"] - 4.189) < 1e-3 and abs(d["D_flat"] - 14.239) < 1e-3)
    pf = d["prof"][(SETS[0], "41/20")]
    pr = d["prof"][(SETS[1], "41/20")]
    k12 = [row for row in pf["rows"] if row["y"] == 1.2][0]
    kr12 = [row for row in pr["rows"] if row["y"] == 1.2][0]
    chk("R3 ell >> r0: K shown to 1.5m at r = 2.05m, gently (K < 2 at 1.2m), A, B, C positive -- short of 14.24m",
        1.5 <= pf["shown_to"] < d["D_flat"] and k12["K"][2] < 2 and min(k12["ABC"]) > 0)
    chk("R3 ell = r0: K shown only to < 0.8m at r = 2.05m, the orders climbing past 1e4 by 1.2m -- short of 4.19m",
        pr["shown_to"] < 0.8 and kr12["K"][0] < kr12["K"][1] < kr12["K"][2] and kr12["K"][2] > 1e4)
    c1 = d["prof"][(SETS[0], "3")]
    c2 = d["prof"][(SETS[1], "3")]
    k3 = [row for row in c2["rows"] if row["y"] == c2["shown_to"]][0]
    chk("R3 control: away from the throat (r = 3m) the flat limit is shown to 2m, and ell = r0 farther than at the "
        "throat with K bounded", c1["shown_to"] >= 2.0 and c2["shown_to"] > 1.5 * pr["shown_to"] and k3["K"][2] < 10)
    chk("R4: the required depth depends on ell, so B4 is not free of k's scale", abs(d["D_r0"] - d["D_flat"]) > 1)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--regenerate" in sys.argv:
        regenerate()
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        report(compute())
