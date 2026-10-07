#!/usr/bin/env python3
"""b4_global.py -- Warp Theorem lemma B4, steps 1-3: the global bulk's topology, its persistence, and the far boundary.

M, item 152 (1): "two separate positions connected by/reached through a dimension."  Item 152 (2): B4 as a brief forward
evolution of the bulk, "an option ... check it" (H-BRIEF-EVOLUTION, an option, not a ruling).

CENSOR5D.md's Theorem W (CGS Thm 3.1, READ) bars two distinct untrapped ends; escape (a) is one end, and then CGS Thm 3.5
(READ, p.5) requires "any causal curve included within <<T>> with end points on T can be deformed, keeping end points
fixed, to a curve included in T".  This instrument does what the board can do about that without solving the bulk.

  B4a ONE END, AND THE DEFORMATION EXISTS (computed; the encoding of item 152 is STRUCTURAL).  Near the corridor a time
      slice of the mirror-doubled bulk is (u, w) x S^2: u the plane's coordinate through the throat (r = 2m + u^2, C2),
      w the doubled depth, the plane at w = 0.  Item 152 is encoded as: the bulk over position 1's sheet and over
      position 2's sheet is one region, joined through w.  Then the far region outside any disc u^2 + w^2 <= R^2 is ONE
      connected set holding both positions' far sheets: one end.  The passage (the segment w = 0 from u = -R to u = R)
      deforms, ends fixed, by the straight-line homotopy onto the arc of T = {u^2 + w^2 = R^2} through the bulk, never
      leaving the disc.  That is CGS Thm 3.5's deformation, and it is "reached through a dimension" as a curve.
      Controls: the plane alone (four dimensions) has two far components, one per position; a bulk walled at u = 0, the
      two sheets' bulks meeting only through the throat, has two, T falls into two arcs, and the homotopy hits the wall.
      The S^2 factor is a product and plays no part, given that the sphere does not shrink in the region (C > 0, as the
      series has it near the plane)
  B4b THE TOPOLOGY IS FIXED BEFORE THE OPENING (READ + deduced).  Ake Hau, Flores and Sanchez, arXiv:1808.04412,
      abstract: "the splitting of any globally hyperbolic (M-bar, g) as an orthogonal product R x Sigma-bar with Cauchy
      slices with boundary {t} x Sigma-bar is proved".  So under W2 every slice has the same topology: the one end of B4a
      is present before the opening, as B7's preexisting bridge joined through the bulk, and the widening changes its
      size, not its topology.  B7 and item 152 describe one initial state
  B4c THE FAR BOUNDARY IS IN UNTOUCHED BULK (computed + standard).  On the plane eq. (17)'s radial light speed in far
      time is sqrt(F H), and 1 - F H = x (4x - 3)^2 / (2 - 3x) exactly, with x = m/r in (0, 1/2]: positive, since
      2 - 3x > 0 and 4x - 3 vanishes only at r = 4m/3, inside the throat.  So F H < 1 for every r > 2m, and F < 1:
      on the plane no signal outruns light in flat space.  Over the
      hold, 28.4777 clocks (O3), the opening's reach on the plane is at most 28.4777 m in r; into a Randall-Sundrum
      exterior it is a proper depth ell ln(1 + 28.4777 m/ell): 5.45 m at ell = r0, 28.48 m as ell >> r0.  Whatever the
      core does, under W2 the set it can influence by the hold's end is compact (J+(K) n J-(Sigma) compact for compact K
      and a Cauchy surface Sigma -- standard, not READ).  So T can be placed in bulk the opening never reached, where the
      preexisting Randall-Sundrum II geometry holds and CENSOR5D C1 gives +-theta+- = 3/R exactly (imported, with its
      control).  This also removes GLOBALBULK G2 for a brief hold: eq. (17)'s 1/r tail never reaches the far boundary
  NOT HERE: W1 (pointwise null energy) inherits B5's reading; W2 (global hyperbolicity: the bulk's evolution regular
      through the hold, inside the reach) is step 4, b4_regular.py, and is where B4 still stands open
Imports bulk/censor5d.py and lemmas/o3_hold.py by path.  Stdlib + sympy.  python3 b4_global.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


# ---- B4a: the (u, w) slice, three models -------------------------------------------------------------------------
L, R, STEP = 40, 20, 1          # grid half-width, the far boundary's radius, spacing (units of m; only topology matters)


def allowed(model, u, w):
    if model == "bulk joined through w (item 152)":
        return True
    if model == "CONTROL the plane alone, four dimensions":
        return w == 0
    if model == "CONTROL bulk walled at u = 0 (sheets' bulks meet only at the throat)":
        return w == 0 or u != 0
    raise ValueError(model)


def far_components(model):
    pts = [(u, w) for u in range(-L, L + 1, STEP) for w in range(-L, L + 1, STEP)
           if u * u + w * w > R * R and allowed(model, u, w)]
    parent = {p: p for p in pts}

    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p
    for (u, w) in pts:
        for q in ((u + STEP, w), (u, w + STEP)):
            if q in parent:
                parent[find((u, w))] = find(q)
    roots = {find(p) for p in pts}
    pos1, pos2 = find((L, 0)), find((-L, 0))
    return {"n": len(roots), "same_end": pos1 == pos2}


def t_arcs(model, n=3600):
    """Components of T = {u^2 + w^2 = R^2} inside the allowed set, sampled; and whether one holds both passage ends."""
    pts = []
    for k in range(n):
        a = 2 * math.pi * k / n
        u, w = R * math.cos(a), R * math.sin(a)
        ui = 0 if abs(u) < 1e-9 else u
        wi = 0 if abs(w) < 1e-9 else w
        pts.append(allowed(model, ui, wi))
    runs, cur = [], []
    for k, ok in enumerate(pts):
        if ok:
            cur.append(k)
        elif cur:
            runs.append(cur)
            cur = []
    if cur:
        if runs and runs[0][0] == 0:
            runs[0] = cur + runs[0]
        else:
            runs.append(cur)
    if all(pts):
        return {"n": 1, "joins_ends": True}
    end1, end2 = 0, n // 2                      # (R, 0) and (-R, 0)
    joins = any(end1 in r and end2 in r for r in runs)
    return {"n": len(runs), "joins_ends": joins}


def homotopy_ok(model, ns=201, nl=101):
    """Straight-line homotopy from the passage (w = 0, u from -R to R) to T's upper arc, ends fixed: stays in the closed
    disc (convexity) and in the allowed set?"""
    for i in range(ns):
        s = i / (ns - 1)
        p0 = (-R + 2 * R * s, 0.0)
        p1 = (-R * math.cos(math.pi * s), R * math.sin(math.pi * s))
        for j in range(nl):
            lam = j / (nl - 1)
            u = (1 - lam) * p0[0] + lam * p1[0]
            w = (1 - lam) * p0[1] + lam * p1[1]
            if u * u + w * w > R * R * (1 + 1e-12):
                return False
            ui = 0 if abs(u) < 1e-9 else u
            wi = 0 if abs(w) < 1e-9 else w
            if not allowed(model, ui, wi):
                return False
    return True


MODELS = ["bulk joined through w (item 152)", "CONTROL the plane alone, four dimensions",
          "CONTROL bulk walled at u = 0 (sheets' bulks meet only at the throat)"]


# ---- B4c: light speed on the plane, the reach, the far boundary --------------------------------------------------
def plane_light_speed():
    x = sp.Symbol("x", positive=True)                     # x = m/r, in (0, 1/2] for r >= 2m
    F = 1 - 2 * x
    H = (1 - 2 * x) ** 2 / (1 - sp.Rational(3, 2) * x)
    gap = sp.factor(sp.together(1 - F * H))
    closed = x * (4 * x - 3) ** 2 / (2 - 3 * x)
    return {"one_minus_FH": gap, "closed": closed, "identity": sp.simplify(gap - closed) == 0,
            "zero_at": sp.solve(sp.Eq(4 * x - 3, 0), x)}


def compute():
    topo = {m: {"far": far_components(m), "T": t_arcs(m), "homotopy": homotopy_ok(m)} for m in MODELS}
    ls = plane_light_speed()
    o3 = _load(os.path.join(HERE, "o3_hold.py"), "b4_o3")
    hold = float(o3.compute()["v"])
    c5 = _load(os.path.join(D68, "bulk", "censor5d.py"), "b4_censor5d").compute()
    ell_r0 = 2.0                                           # ell = r0 = 2m, units of m
    return {"topo": topo, "ls": ls, "hold": hold, "reach_plane": hold,
            "depth_ell_r0": ell_r0 * math.log(1 + hold / ell_r0), "depth_flat": hold,
            "theta_brane": c5["theta_brane"], "theta_bdry": c5["theta_bdry"], "R": c5["R"]}


def report(d):
    print("b4_global.py -- Warp Theorem lemma B4, steps 1-3\n")
    for m, t in d["topo"].items():
        print("  %-70s far components %d (positions in one: %s); T arcs %d (one joins the ends: %s); homotopy: %s"
              % (m, t["far"]["n"], t["far"]["same_end"], t["T"]["n"], t["T"]["joins_ends"], t["homotopy"]))
    ls = d["ls"]
    print("\nB4c 1 - F H = %s = %s (identity: %s); zero only at x = %s, r = 4m/3: F H < 1 for r > 2m"
          % (ls["one_minus_FH"], ls["closed"], ls["identity"], ls["zero_at"]))
    print("    hold %.4f clocks: reach on the plane <= %.4f m; RS depth %.3f m at ell = r0, %.3f m as ell >> r0"
          % (d["hold"], d["reach_plane"], d["depth_ell_r0"], d["depth_flat"]))
    print("    far boundary in untouched RS II: theta = %s; control (centred on the AdS boundary): %s"
          % (d["theta_brane"], d["theta_bdry"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    j = d["topo"][MODELS[0]]
    chk("B4a: joined through the bulk (item 152, encoding STRUCTURAL), the far region is one end holding both positions",
        j["far"]["n"] == 1 and j["far"]["same_end"])
    chk("B4a: the passage deforms, ends fixed, onto T through the bulk (CGS Thm 3.5's deformation); T is one arc",
        j["homotopy"] and j["T"]["n"] == 1 and j["T"]["joins_ends"])
    p = d["topo"][MODELS[1]]
    wl = d["topo"][MODELS[2]]
    chk("B4a controls: the plane alone and the walled bulk each have two ends, T in two arcs, no deformation",
        p["far"]["n"] == 2 and not p["far"]["same_end"] and wl["far"]["n"] == 2 and not wl["far"]["same_end"]
        and not wl["homotopy"] and not wl["T"]["joins_ends"] and not p["homotopy"])
    ls = d["ls"]
    chk("B4c: on the plane 1 - F H = x(4x - 3)^2/(2 - 3x) > 0 for every r > 2m (its only zero, r = 4m/3, is inside)",
        ls["identity"] and ls["zero_at"] == [sp.Rational(3, 4)])
    chk("B4c: the hold's reach -- 28.4777 m on the plane, 5.45 m deep at ell = r0, 28.48 m as ell >> r0",
        abs(d["hold"] - 28.4777) < 1e-3 and abs(d["depth_ell_r0"] - 5.448) < 1e-3)
    R = d["R"]
    chk("B4c: the far boundary in untouched Randall-Sundrum II is strictly untrapped, 3/R (CENSOR5D C1); control 0",
        sp.simplify(d["theta_brane"] - 3 / R) == 0 and sp.simplify(d["theta_bdry"]) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
