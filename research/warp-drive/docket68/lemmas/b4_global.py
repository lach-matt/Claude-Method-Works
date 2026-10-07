#!/usr/bin/env python3
"""b4_global.py -- Warp Theorem lemma B4, steps 1-3: the global bulk's topology, its persistence, and the far boundary.

M, item 152 (1): "two separate positions connected by/reached through a dimension."  Item 152 (2): B4 as a brief forward
evolution of the bulk, "an option ... check it" (H-BRIEF-EVOLUTION, an option, not a ruling).

CENSOR5D.md's Theorem W (CGS Thm 3.1, READ) bars two distinct untrapped ends; escape (a) is one end, and then CGS Thm 3.5
(READ, p.5) requires "any causal curve included within <<T>> with end points on T can be deformed, keeping end points
fixed, to a curve included in T".  This instrument does what the board can do about that without solving the bulk.

  B4a ONE END, AND THE DEFORMATION EXISTS IF THE INSIDE OF T IS REGULAR (STRUCTURAL; conditional on W2 inside T).  Near
      the corridor a time slice of the mirror-doubled bulk is (u, w) x S^2: u the plane's coordinate through the throat
      (r = 2m + u^2, C2), w the doubled depth, the plane at w = 0.  Item 152 (1) is encoded as H-SEPARATE-JOINED-THROUGH-
      DIMENSION: the bulk over position 1's sheet and over position 2's sheet is one region, joined through w; that this
      is CENSOR5D's escape (a) is the board's reading, as item 152 records.  Then the far region outside the disc
      u^2 + w^2 <= R^2 is one connected set holding both positions' far sheets (one end), and the passage (w = 0, u from
      -R to R) deforms, ends fixed, onto the arc of T = {u^2 + w^2 = R^2} x S^2 through the bulk -- CGS Thm 3.5's
      deformation, "reached through a dimension" as a curve.  In this model both are true by construction (the region is
      all of the plane and the disc convex), so the check is STRUCTURAL; what it shows is the controls.  Controls: the
      plane alone (four dimensions) has two ends; a bulk joined through w only at the throat -- the other reading of
      "connected by a dimension", under which CGS Thm 3.1 forbids the corridor -- has two ends; and one end with a
      mirrored pair of excised regions inside T has one far component and T one arc, yet NO deformation: so B4a's
      deformation needs the bulk inside T regular, which is W2 (b4_regular.py).  The S^2 plays no part even if it caps
      off regularly: it is simply connected, and only regularity matters
  B4b' THE TOPOLOGY IS FIXED BEFORE THE OPENING (READ + deduced; conditional on W2 for the whole spacetime).  Ake Hau,
      Flores and Sanchez, arXiv:1808.04412, abstract: "the splitting of any globally hyperbolic (M-bar, g) as an
      orthogonal product R x Sigma-bar with Cauchy slices with boundary {t} x Sigma-bar is proved".  So every slice has
      the same topology: the one end is present before the opening, as B7's preexisting bridge joined through the bulk --
      and, by the same splitting, at every earlier time too.  The widening changes the bridge's size, not its topology
  B4c THE FAR BOUNDARY: UNTRAPPED ONLY INSIDE HALF THE CURVATURE LENGTH (computed in the board's model, H-FAR-MODEL).
      CENSOR5D C1's sphere (an S^3 centred on one plane in pure RS II) is not B4a's T, which is S^1 x S^2 and crosses the
      deep bulk over the throat.  So theta+- is computed for T itself, in a labelled model -- not a solution: the
      Randall-Sundrum II conformal form with the plane's spheres given a throat, g = (ell/z)^2 (-dt^2 + du^2 + dw^2 +
      rho(u)^2 dOmega^2), z = ell + |w|, rho^2 = u^2 + a^2.  On T, at angle alpha from the plane,
          +-theta+- = (3 R^2 ell cos^2 alpha - 2 R a^2 sin alpha + a^2 ell) / (R ell (R^2 cos^2 alpha + a^2)).
      Control: a -> 0 gives C1's 3/R exactly.  Over the throat (alpha = pi/2) its sign is that of ell - 2R: T is strictly
      untrapped iff R < ell/2.  T must also lie beyond the opening's reach, so the model needs ell > 2 R_reach.  The
      reach (Randall-Sundrum estimate, from eq. (17)'s plane: 1 - F H = x (4x - 3)^2/(2 - 3x) with x = m/r, so the
      coordinate speed dr/dt = sqrt(F H) < 1 and Delta r <= Delta t) is at most 13.0 m over the longest hold the bulk
      admits (O3's window, b4_static.py; first written 28.48 m, O3's withdrawn per-bit hold) -- an estimate, since
      the lapse near the core is not shown to be RS's; under W2 the influenced set is compact whatever the core does
      (J+(K) n J-(Sigma) compact; standard, not READ, and with timelike boundary resting on Ake Hau-Flores-Sanchez-type
      structure).  So in the model: ell > ~26 m (corridor units; ~57 m under the withdrawn hold) -- met by orders of
      magnitude if ell is anywhere near
      its measured bound, and impossible at ell = r0, where no such T exists and escape (a) is not shown.  "Uniformly in
      time" (CGS p.9) holds in the model before the opening and through the hold; after the closing (E2) outgoing
      radiation reaches any fixed T, and that it leaves T untrapped is H-WEAK-RADIATION, the board's.  Scoping eq. (17)
      to inside the reach -- which is what keeps its 1/r tail (GLOBALBULK G2) off T -- is GLOBALBULK OPEN 5's weaker
      form, a hypothesis (H-NEAR-ZONE), not a result
  NOT HERE: W1 (pointwise null energy) inherits B5's reading; W2 (the bulk regular through the hold) is b4_regular.py
      and b4_static.py
Imports lemmas/o3_hold.py by path.  Stdlib + sympy.  python3 b4_global.py [--selftest]
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
    if model == "CONTROL one end, a mirrored pair of excised regions inside T":
        return u * u + (w - 8) ** 2 > 9 and u * u + (w + 8) ** 2 > 9
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
    """Straight-line homotopy from the passage (w = 0, u from -R to R) onto T's upper or lower arc, ends fixed: does
    either stay in the closed disc (convexity) and in the allowed set?"""
    return _homotopy(model, ns, nl, 1) or _homotopy(model, ns, nl, -1)


def _homotopy(model, ns, nl, side):
    for i in range(ns):
        s = i / (ns - 1)
        p0 = (-R + 2 * R * s, 0.0)
        p1 = (-R * math.cos(math.pi * s), side * R * math.sin(math.pi * s))
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
          "CONTROL bulk walled at u = 0 (sheets' bulks meet only at the throat)",
          "CONTROL one end, a mirrored pair of excised regions inside T"]


# ---- B4c: light speed on the plane, the reach, the far boundary --------------------------------------------------
def plane_light_speed():
    x = sp.Symbol("x", positive=True)                     # x = m/r, in (0, 1/2] for r >= 2m
    F = 1 - 2 * x
    H = (1 - 2 * x) ** 2 / (1 - sp.Rational(3, 2) * x)
    gap = sp.factor(sp.together(1 - F * H))
    closed = x * (4 * x - 3) ** 2 / (2 - 3 * x)
    return {"one_minus_FH": gap, "closed": closed, "identity": sp.simplify(gap - closed) == 0,
            "zero_at": sp.solve(sp.Eq(4 * x - 3, 0), x)}


def far_boundary():
    """theta+ of T = {u^2 + w^2 = R^2} x S^2 in the board's model (H-FAR-MODEL), side w > 0; static, so
    theta+- = +-(div n - a_n) (CENSOR5D's derivation), div over sqrt|g| with the lapse."""
    u, w = sp.symbols("u w", real=True)
    ell, Rr, a = sp.symbols("ell R a", positive=True)
    al = sp.Symbol("alpha")
    z = ell + w
    lapse = ell / z
    rho = sp.sqrt(u**2 + a**2)
    sqrtg = (ell / z) ** 5 * rho**2
    rr = sp.sqrt(u**2 + w**2)
    n = [z / ell * u / rr, z / ell * w / rr]
    X = [u, w]
    div = sum(sp.diff(sqrtg * n[i], X[i]) for i in range(2)) / sqrtg
    an = sum(n[i] * sp.diff(sp.log(lapse), X[i]) for i in range(2))
    on = sp.simplify((div - an).subs({u: Rr * sp.cos(al), w: Rr * sp.sin(al)}))
    want = ((3 * Rr**2 * ell * sp.cos(al) ** 2 - 2 * Rr * a**2 * sp.sin(al) + a**2 * ell)
            / (Rr * ell * (Rr**2 * sp.cos(al) ** 2 + a**2)))
    top = sp.simplify(on.subs(al, sp.pi / 2))
    f = sp.lambdify((al, ell, Rr, a), on)
    grid = [k * math.pi / 400 for k in range(0, 401)]
    def min_theta(L_, R_, a_):
        return min(f(x, L_, R_, a_) for x in grid)
    return {"theta": on, "closed_form": sp.simplify(on - want) == 0, "a0": sp.simplify(on.subs(a, 0)), "top": top,
            "min": min_theta, "symbols": (ell, Rr, a)}


def compute():
    topo = {m: {"far": far_components(m), "T": t_arcs(m), "homotopy": homotopy_ok(m)} for m in MODELS}
    ls = plane_light_speed()
    o3 = _load(os.path.join(HERE, "o3_hold.py"), "b4_o3")
    hold = float(o3.compute()["v"])
    fb = far_boundary()
    return {"topo": topo, "ls": ls, "hold": hold, "reach_plane": hold, "fb": fb,
            "min_ok": fb["min"](10 * hold, 1.2 * hold, 1.0), "min_bad": fb["min"](2.0, 1.2 * hold, 1.0)}


def report(d):
    print("b4_global.py -- Warp Theorem lemma B4: B4a, B4b', B4c\n")
    for m, t in d["topo"].items():
        print("  %-66s far components %d (positions in one: %s); T arcs %d (joins the ends: %s); deformation: %s"
              % (m, t["far"]["n"], t["far"]["same_end"], t["T"]["n"], t["T"]["joins_ends"], t["homotopy"]))
    ls, fb = d["ls"], d["fb"]
    print("\nB4c plane: 1 - F H = %s (identity: %s), so dr/dt < 1; reach over the longest admissible hold %.4f m (RS estimate)"
          % (ls["closed"], ls["identity"], d["hold"]))
    print("    theta+ on T = %s" % fb["theta"])
    print("    a -> 0: %s (C1); over the throat: %s -- untrapped iff R < ell/2" % (fb["a0"], fb["top"]))
    print("    min theta, R = 1.2 x reach: ell = 10 x reach %.3g; ell = r0 %.3g" % (d["min_ok"], d["min_bad"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    j = d["topo"][MODELS[0]]
    chk("B4a (STRUCTURAL): joined through the bulk (item 152's encoding), one end holding both positions, and the passage "
        "deforms, ends fixed, onto T", j["far"]["n"] == 1 and j["far"]["same_end"] and j["homotopy"]
        and j["T"]["n"] == 1 and j["T"]["joins_ends"])
    p = d["topo"][MODELS[1]]
    wl = d["topo"][MODELS[2]]
    chk("B4a controls: the plane alone, and the bulk joined only at the throat, each have two ends and no deformation",
        p["far"]["n"] == 2 and not p["far"]["same_end"] and wl["far"]["n"] == 2 and not wl["far"]["same_end"]
        and not wl["homotopy"] and not wl["T"]["joins_ends"] and not p["homotopy"])
    h = d["topo"][MODELS[3]]
    chk("B4a control: one end with excised regions inside T -- one far component, T one arc, yet no deformation "
        "(so B4a needs W2 inside T)", h["far"]["n"] == 1 and h["T"]["joins_ends"] and not h["homotopy"])
    ls = d["ls"]
    chk("B4c: on the plane 1 - F H = x(4x - 3)^2/(2 - 3x) > 0 for r > 2m (zero only at r = 4m/3), so dr/dt < 1",
        ls["identity"] and ls["zero_at"] == [sp.Rational(3, 4)] and abs(d["hold"] - 13.0) < 0.1)
    fb = d["fb"]
    ell, Rr, a = fb["symbols"]
    chk("B4c: theta+ of T in the model, closed form; control a -> 0 gives C1's 3/R",
        fb["closed_form"] and sp.simplify(fb["a0"] - 3 / Rr) == 0)
    chk("B4c: over the throat theta+ has the sign of ell - 2R; with T beyond the reach, untrapped at ell = 10 x reach, "
        "trapped somewhere at ell = r0", sp.simplify(fb["top"] - a**2 * (ell - 2 * Rr) / (Rr * ell * a**2)) == 0
        and d["min_ok"] > 0 and d["min_bad"] < 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
