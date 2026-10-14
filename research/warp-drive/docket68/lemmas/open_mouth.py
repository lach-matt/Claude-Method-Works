#!/usr/bin/env python3
"""open_mouth.py -- the rim as an open mouth (item 210: "The rim is a coupling interaction between the mouth and our
plane. My guess is it looks like a singularity on paper, but is an open mouth."): our plane turning smoothly into the
corridor, in the flat-limit bank.  What the joint carries in each of the two orientations a smooth turn allows, and
which of them keeps the seated corridor.  Items 210, 211; computed and deduced where marked; checked by an adversarial
verifier in the item-210 critic pass (its F1, F2, F5, F6, F9 and F11 (i) survived; the analyst's F4, F10, F11 (ii)
and answer were refuted for working one orientation without stating it as a choice); seated under 206; 2026-10-10.

  O1 (computed) our plane in the bank: at y = 0, A = 1 - 2m/r, B = r(2r - 3m)/(2(r - 2m)^2), C = r^2, and A, B, C are
     even in y.  So the plane's extrinsic curvature vanishes at flat order (K_ab = 0); B is not Schwarzschild's g_rr
  O2 (deduced by hand, computed check) a sheet leaving the plane at proper angle t (tan t = |Y'|/sqrt B) has, as
     y -> 0 and in corridor_shape's orientation, k_t = -sqrt2 m sin t / (r^1.5 sqrt(2r - 3m)) and
     k_theta = (r - 2m) k_t / m.  So the marginal corridor (k_r = k_t) carries at its rim EXACTLY
     rho_rim = sqrt2 sin t sqrt(2 r_rim - 3m) / r_rim^1.5 (in 2/kappa5^2 per m), and every seated member reproduces
     it to 3e-3 (the march stops at y = 0.01): ring_consistent's tau = rho_rim ell/(3m) is an exact function of
     (r_rim, t), not a free coefficient.  The
     tangential null energy there is sqrt2 sin t (r - 3m) / (r^1.5 sqrt(2r - 3m)): it changes sign at r = 3m EXACTLY,
     the photon sphere (d(A/C)/dr = 0).  rim_profile P2's 'r_b ~ 3.01m' is its 0.01m grid step
  O3 (computed, sympy) Y'' enters k_r only, affinely, with dk_r/dY'' > 0.  So a smooth fold of a gravitating Z2 sheet,
     whose stress is fixed by its curvature, carries a Nambu-Goto line: across a fold of turning angle t the energy
     and the radial null energy each integrate to -t or +t (2/kappa5^2), and the tangential to 0.  The sign is set by
     which side is kept.  ring_cypher R2 ('a thin pure-tension sheet carries NO line tension at a fold') holds for a
     test membrane, not for such a sheet (a scope correction, recorded and not repaired)
  O4 (deduced from O2, O3; computed check) 'our plane turns smoothly into the corridor' fixes the surface, not the
     side kept.  D+ keeps corridor_shape's normal (into the slab): what B becomes when our plane inside the rim is
     removed.  Reflected y -> -y (the bank is even in y) it is the shoot analyst's S, whose dome lies in the
     analytically continued region beyond our plane.  D- (the shoot's D) keeps the other side, where every flat-limit
     stress changes sign.  Read in D-, every seated member has negative tangential null energy along its whole length
     (the warp adds none to it), so by TS grazing rays break (Z) unless a second source lies on them; it also has
     negative energy at flat order.  So D+ is the only orientation in which the seated corridor is the open mouth's
     body (rim_profile P4, P4b: radial null energy 0, tangential and energy positive, joined to the throat).  The warp
     part, +sigma cos t (1 + sin^2 t/3) on a dome whose kept bulk lies above it, has the same sign in both orientations
     and puts no line at the fold
  O5 (computed, D+) the joint is a concave fold carrying a NEGATIVE Nambu-Goto line, lambda = -(2/kappa5^2) t.
     It is a line in compression with negative energy at the line: the strut's sign (ring_consistent C3), but the
     fold's own value, and it needs no balance.  A radial null ray in the sheet gains
     int (rho + p_r) ds / sqrt(A) = -t / sqrt(1 - 2m/r_rim) across it (-0.14 to -0.33 over the members), and the
     marginal corridor adds exactly 0.  So (Z) net per ray (183) fails on those rays unless something positive lies on
     the same rays: TS's own exception, a second source on the same rays (P2-FULL).  That is where 177's appearance
     and 210's coupling enter.  The tangential null energy is kept (r_rim > 3m, O2)
  O6 (computed, D-) the joint is a convex fold carrying a POSITIVE Nambu-Goto line, lambda = +(2/kappa5^2) t, with
     its tangential null energy kept for r_rim < 3m and lost for r_rim > 3m (O2; at 3m the first order vanishes and
     the next decides -- the item-210 shoot critic).  No D- body has been computed (O4: the seated family fails there)
  O7 (cypher, 196; audited per 211) the computed rim carriers, on exact values over (lam, rho, inside, body): B's
     strut read Nambu-Goto, B's strut read with energy >= 0 (added matter), the D+ open mouth, the D- open mouth
     (body not computed: U), and the ringless members past 45 deg.  The refuted positive ring is left out, since its
     premise was refuted (item 208).  M's sentence entered as a cell -- a line (lam != 0), an open mouth (inside 0,
     body 1), a coupling (negative energy at the line that something on the same rays must pair: rho 0) -- IS the D+
     cell, so every language admits it by construction, and the cypher adds nothing to O4-O5.  The D- open mouth with
     a body splits the languages: order, algebra and information admit it, geometry and statistics refuse it, and
     statistics' refusal (blocked by (lam, body)) is forced, since lam = +1 is held by one cell only (208).  The index
     has no key and no one-hot code (index_audit).  So the cypher does not decide whether D- has a body
So the open mouth that keeps the seated corridor is D+.  On paper it is a line in compression, so 210's board reading
stands, and the analyst's correction of it does not.  Its negative null energy per ray asks (Z) for a partner on the
same rays: the coupling.  What pairs it is OPEN.  Under TS (deduced from P2-FULL's wording) only a second source at
the same place can pair it for bulk rays: a ray grazing the sheet where its tangent null energy is negative gains
S(k0, k0)/alpha -> -infinity, which the sheet's own shape elsewhere cannot offset.  So the partner sits at the rim, as
M's 'coupling interaction between the mouth and our plane' places it.  The corridor's own shape pairs in-sheet rays
only.  In the item-210 pass (scratch, its critic re-ran it on two banks; broad, one member of a free family, not re-run
here) a prescribed D+ path that dives to a depth of about m near the throat, plateaus, and rises to a tangential joint
keeps every in-sheet ray class computed non-negative, though its own radial pattern (-, +, -, +, -) leaves TS's grazing
bulk rays unpaired.  Its radial affine net is +0.27 to +0.29 (a 1.6% difference of terms near +-16.7 at
r - 2m < 1e-3), it has no horizon boundary term, and its energy is positive only with sigma counted, for
ell/m <= about 28.9.  The half-ray positives of the shallow 'throat lever' were refuted: they were the boundary term
where the ray is cut at the horizon, and on mirror-completed rays the net is 2L < 0.  The board's reading H-OPEN-MOUTH-DPLUS (M's open mouth is D+,
because it keeps the seated corridor) goes to M with the report; D- is kept on record.
What this does not show: (i) the flat limit, eq. (17)'s static bulk by Pade continuation; the fold integrals use the
bank within 0.01m of y = 0, where O1 is exact to 1e-13; (ii) thin sheets; (iii) the folds are smooth at width
w = 0.002m, so the limit w -> 0 is taken numerically; (iv) what lies on the same rays; (v) both orientations keep eq.
(17)'s deep static bulk under the throat, b4_static S2's singular surface (y = 2.49-2.50m at r = 2.15m, numerical
evidence) included (deduced; the item-210 shoot critic), so what is shown is a sheet and its joint, bounding a bulk that
is singular on that evidence, not yet an open mouth in a regular bulk; (vi) the bank's near-throat interpolation
(corridor_shape S0's note) moves the members' rims by about 1%, which no check here turns on.
Imports rim_profile.py (and through it corridor_shape.py), index_audit.py and tools/cypher.py by path.  Stdlib + sympy
(+ mpmath through corridor_shape).  python3 open_mouth.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}
_C = {}
WIDE = ((1.5, 0.0), (1.9, 0.0), (2.0, 1.0))                     # ring_consistent's wider members
FOLDS = ((0.25, 0.0), (0.5, 1.0), (1.0, 3.0))                   # the fold cases (rims 3.39, 4.15, 5.28m)
W = 0.002
M210 = ("The rim is a coupling interaction between the mouth and our plane. My guess is it looks like a singularity "
        "on paper, but is an open mouth.")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), os.path.dirname(os.path.dirname(path))]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def shape():
    if "rp" not in _C:
        rp = _load(os.path.join(HERE, "rim_profile.py"), "om_rim_profile")
        _C["rp"] = rp
        _C["cs"], _C["ks"], _C["bulk"] = rp.shape()
    return _C["cs"], _C["ks"], _C["bulk"]


def stress(r, Y, Y1, Y2, side=+1):
    """rho, rho + p_r, rho + p_theta at (r, Y) for slope Y1 and curvature Y2; side +1 is corridor_shape's orientation
    (D+), -1 the other (D-)"""
    cs, ks, bulk = shape()
    if MUT.get("orient_flip"):
        side = -side
    return tuple(side * v for v in cs.stresses(ks, bulk.at(r, Y), Y1, 0.0 if MUT.get("no_fold_curvature") else Y2))


Bf = lambda r: r * (2 * r - 3) / (2 * (r - 2) ** 2)              # m = 1 throughout


# ================================================================================================================ O1
def o1():
    cs, ks, bulk = shape()
    dev, sch = 0.0, 0.0
    for i, r in enumerate(bulk.rv):
        c = bulk.col(i, 0.0)
        dev = max(dev, abs(c["A"][0] / (1 - 2 / r) - 1), abs(c["B"][0] / Bf(r) - 1), abs(c["C"][0] / r ** 2 - 1),
                  abs(c["A"][1]), abs(c["B"][1]), abs(c["C"][1]))
        sch = max(sch, abs(c["B"][0] * (1 - 2 / r) - 1))
    return {"dev": dev, "sch": sch, "ncol": len(bulk.rv)}


# ================================================================================================================ O2
def kt_closed(r, t):
    return -math.sqrt(2) * math.sin(t) / (r ** 1.5 * math.sqrt(2 * r - 3))


def rho_rim_closed(r, t):
    return math.sqrt(2) * math.sin(t) * math.sqrt(2 * r - 3) / r ** 1.5


def tan_closed(r, t):
    return math.sqrt(2) * math.sin(t) * (r - 3) / (r ** 1.5 * math.sqrt(2 * r - 3))


def member(d, s):
    cs, ks, bulk = shape()
    R = cs.marginal(ks, bulk, d, 0.0, s, rmax=12.0)
    rows = R["rows"]
    r, Y, Y1, rho, rad, tan = rows[-1][:6]
    t = math.atan(abs(Y1) / math.sqrt(bulk.at(r, max(Y, 1e-6))["B"][0]))
    return {"rim": R["rim"], "r": r, "Y1": Y1, "theta": t, "rho_rim": rho, "tan_rim": tan,
            "min_rho": min(x[3] for x in rows), "min_tan": min(x[5] for x in rows),
            "max_rho_dminus": max(-x[3] for x in rows), "max_tan_dminus": max(-x[5] for x in rows)}


def rb_bisect(Yv=1e-4, dY=1e-4):
    """where the tangential null energy's slope coefficient b changes sign, at depth Yv (b ~ (3m - r) sin t)"""
    cs, ks, bulk = shape()
    f = lambda r: (cs.stresses(ks, bulk.at(r, Yv), dY, 0.0)[2] - cs.stresses(ks, bulk.at(r, Yv), -dY, 0.0)[2]) / (2 * dY)
    if MUT.get("grid_rb"):
        r = 2.4
        while f(r + 0.01) > 0:
            r += 0.01
        return r + 0.01
    lo, hi = 2.99, 3.02
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    return 0.5 * (lo + hi)


def o2():
    cs, ks, bulk = shape()
    worst = {"kt": 0.0, "kth": 0.0, "tan": 0.0}
    for r in (2.05, 2.4, 2.9, 3.6, 5.0, 9.0):
        for Z in (0.02, 0.7, 2.0, 9.0):
            t = math.atan(Z / math.sqrt(Bf(r)))
            g = bulk.at(r, 1e-9)
            a = (g["A"][0], g["B"][0], g["C"][0], g["A"][1], g["B"][1], g["C"][1], g["A"][2], g["B"][2], g["C"][2], -Z, 0.0)
            kt, kth = ks["kt"](*a), ks["kth"](*a)
            tan = cs.stresses(ks, g, -Z, 0.0)[2]
            worst["kt"] = max(worst["kt"], abs(kt / kt_closed(r, t) - 1))
            worst["kth"] = max(worst["kth"], abs(kth / ((r - 2) * kt_closed(r, t)) - 1))
            worst["tan"] = max(worst["tan"], abs(tan - tan_closed(r, t)) / abs(kt_closed(r, t)))
    fam = {k: member(*k) for k in list(_C["rp"].FAMILY) + list(WIDE)}
    rel = {k: abs(v["rho_rim"] / rho_rim_closed(v["r"], v["theta"]) - 1) for k, v in fam.items()}
    rp = _C["rp"]
    return {"worst": worst, "fam": fam, "rel": rel, "rb": rb_bisect(), "rb_grid": rp.p2(rs=(2.5,))["rb"]}


# ================================================================================================================ O3
def o3():
    import sympy as sp
    cs, ks, bulk = shape()
    Y2 = [s for s in ks["kr_expr"].free_symbols if s.name == "Y2"][0]
    free = Y2 not in ks["kt_expr"].free_symbols and Y2 not in ks["kth_expr"].free_symbols
    affine = sp.simplify(sp.diff(ks["kr_expr"], Y2, 2)) == 0
    d = sp.lambdify(sorted(ks["kr_expr"].free_symbols, key=lambda s: s.name), -sp.diff(ks["kr_expr"], Y2), "math")
    syms = sorted(ks["kr_expr"].free_symbols, key=lambda s: s.name)
    pos = True
    for r, Y, Y1 in ((2.1, 0.3, -0.2), (3.5, 0.1, -0.4), (2.5, 0.6, 0.5), (4.2, 0.005, -2.0)):
        g = bulk.at(r, Y)
        val = {"A": g["A"][0], "B": g["B"][0], "C": g["C"][0], "Ay": g["A"][1], "By": g["B"][1], "Cy": g["C"][1],
               "Ar": g["A"][2], "Br": g["B"][2], "Cr": g["C"][2], "Y1": Y1, "Y2": 0.0}
        pos = pos and d(*[val[s.name] for s in syms]) > 0
    return {"free": free, "affine": affine, "positive": pos}


# ============================================================================================================ O5, O6
def fold(r_rim, Z, side, w=W, n=4000):
    """a smooth fold from the corridor (slope Y' = -Z, meeting the plane at r_rim) onto our plane (Y = 0, r > r_rim + w),
    the slope blended by a cubic smoothstep over [r_rim, r_rim + w]; integrals over the fold in proper length s"""
    shape()
    bulk = _C["bulk"]
    r1 = r_rim
    u = lambda r: (r - r1) / w
    Y1f = lambda r: -Z * (1 - (3 * u(r) ** 2 - 2 * u(r) ** 3))
    Y2f = lambda r: Z * (6 * u(r) - 6 * u(r) ** 2) / w
    rs = [r1 + w * i / n for i in range(n + 1)]
    Ys = [0.0] * (n + 1)
    for i in range(n - 1, -1, -1):
        rm = 0.5 * (rs[i] + rs[i + 1])
        Ys[i] = Ys[i + 1] - Y1f(rm) * (rs[i + 1] - rs[i])
    I = {"rho": 0.0, "rad": 0.0, "tan": 0.0, "rad_aff": 0.0}
    for i in range(n):
        rm = 0.5 * (rs[i] + rs[i + 1])
        Ym = max(0.5 * (Ys[i] + Ys[i + 1]), 1e-12)
        rho, rad, tan = stress(rm, Ym, Y1f(rm), Y2f(rm), side)
        g = bulk.at(rm, Ym)
        ds = math.sqrt(g["B"][0] + Y1f(rm) ** 2) * (rs[i + 1] - rs[i])
        I["rho"] += rho * ds
        I["rad"] += rad * ds
        I["tan"] += tan * ds
        I["rad_aff"] += rad * ds / math.sqrt(g["A"][0])
    I["theta"] = math.atan(Z / math.sqrt(bulk.at(r1, 0.0)["B"][0]))
    I["r_rim"] = r_rim
    return I


def o56(fam):
    out = {}
    for k in FOLDS:
        v = fam[k]
        Z = -v["Y1"]
        out[k] = {"plus": fold(v["r"], Z, +1), "minus": fold(v["r"], Z, -1)}
    # D-'s tangential at the joint, either side of 3m (a corridor meeting the plane at 0.5 rad)
    cs, ks, bulk = shape()
    dm = {}
    for r in (2.6, 2.9, 3.1, 3.4):
        Z = math.tan(0.5) * math.sqrt(Bf(r))
        dm[r] = stress(r, 1e-9, -Z, 0.0, -1)[2]
    return {"folds": out, "dminus_tan": dm}


# ================================================================================================================ O7
def o7():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "om_cypher")
    ia = _load(os.path.join(HERE, "index_audit.py"), "om_index_audit")
    U = "U"
    coords = ["lam", "rho", "inside", "body"]
    cells = {"S_NG": (-1, 0, 1, 1), "S_pos": (-1, 1, 1, 1), "D+": (-1, 0, 0, 1),
             "D-": (1, 1, 0, U if not MUT.get("dminus_body") else 1), "C4": (0, 1, 1, 0)}
    m210 = (-1, 0, 0, 1)                                          # a line, an open mouth with its body, paired at the line
    dminus_with_body = (1, 1, 0, 1)
    cl = sorted(set(cells.values()), key=str)
    vo = {"lam": [-1, 0, 1], "rho": [0, 1], "inside": [0, 1], "body": [x for x in (0, U, 1) if x in {c[3] for c in cl}]}
    ix = cy.Index("open_mouth", coords, [list(c) for c in cl], value_order=vo)
    inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(coords))]
    res = {}
    for lang in ("order", "algebra", "geometry", "information"):
        out, _ = cy.ADMISSION[lang][0](ix, {})
        dec = set() if out is None else {tuple(inv[i][c[i]] for i in range(len(coords))) for c in out}
        res[lang] = (m210 in dec, dminus_with_body in dec)
    out, _ = cy.op_statistics(ix, {"statistics_order": 2})
    dec = {tuple(inv[i][c[i]] for i in range(len(coords))) for c in out}
    res["statistics"] = (m210 in dec, dminus_with_body in dec)
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    seen = {p: {(c[p[0]], c[p[1]]) for c in cl} for p in pairs}
    block = [(coords[i], coords[j]) for (i, j) in pairs if (dminus_with_body[i], dminus_with_body[j]) not in seen[(i, j)]]
    singleton = sum(c[0] == 1 for c in cl) == 1
    audit = ia.audit_index(coords, [tuple(c) for c in cl])
    return {"m210_is_dplus": m210 == cells["D+"], "res": res, "block": block, "lam1_singleton": singleton,
            "audit": audit, "box": ix.box}


def compute():
    a = o1()
    b = o2()
    return {"o1": a, "o2": b, "o3": o3(), "o56": o56(b["fam"]), "o7": o7()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rulings = open(os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md")).read()
    add("O0 M's 210 verbatim in the rulings file", M210 in rulings.replace("\n    ", " "))
    o = d["o1"]
    add("O1 our plane in the bank: A = 1 - 2m/r, B = r(2r - 3m)/(2(r - 2m)^2), C = r^2 at y = 0 and even in y (every "
        "column, to 1e-12): K_ab = 0 on the plane at flat order; B is not Schwarzschild's g_rr",
        o["dev"] < 1e-12 and o["sch"] > 1 and o["ncol"] >= 30)
    o = d["o2"]
    adm = {k: v for k, v in o["fam"].items() if v["rim"] and v["min_rho"] > 0 and v["min_tan"] > 0}
    add("O2 k_t = -sqrt2 m sin t/(r^1.5 sqrt(2r - 3m)) and k_theta = (r - 2m) k_t/m as y -> 0; the marginal corridor's "
        "rho_rim = sqrt2 sin t sqrt(2r - 3m)/r^1.5 exactly, every member to 3e-3 (tau exact in (r_rim, t)); the "
        "tangential changes sign at r = 3m exactly (r_b = 3m to 1e-6; P2's 3.01 is its grid)",
        o["worst"]["kt"] < 1e-3 and o["worst"]["kth"] < 1e-3 and o["worst"]["tan"] < 5e-3 and len(adm) >= 7
        and all(o["rel"][k] < 3e-3 for k in adm)
        and abs(o["rb"] - 3.0) < 1e-6 and abs(o["rb_grid"] - 3.01) < 1e-9)
    o = d["o3"]
    add("O3 Y'' enters k_r only, affinely, dk_r/dY'' > 0: a fold of a gravitating Z2 sheet carries a Nambu-Goto line "
        "(ring_cypher R2 holds for a test membrane only)", o["free"] and o["affine"] and o["positive"])
    fam = d["o2"]["fam"]
    add("O4 read in D-, every seated member has negative energy and negative tangential null energy along its whole "
        "length (every flat-limit stress changes sign): D+ is the only orientation in which the seated corridor is the "
        "body", all(v["max_rho_dminus"] < 0 and v["max_tan_dminus"] < 0 for v in adm.values()))
    F = d["o56"]["folds"]
    ok5 = all(abs(f["plus"]["rho"] + f["plus"]["theta"]) < 0.01 * f["plus"]["theta"]
              and abs(f["plus"]["rad"] + f["plus"]["theta"]) < 0.01 * f["plus"]["theta"]
              and abs(f["plus"]["rad_aff"] + f["plus"]["theta"] / math.sqrt(1 - 2 / f["plus"]["r_rim"]))
              < 0.01 * f["plus"]["theta"] and abs(f["plus"]["tan"]) < 0.05 * f["plus"]["theta"] for f in F.values())
    aff = [f["plus"]["rad_aff"] for f in F.values()]
    add("O5 D+: a concave fold, a NEGATIVE Nambu-Goto line (int rho ds = -t, 1%); a radial ray in the sheet gains "
        "-t/sqrt(1 - 2m/r_rim) (-0.14 to -0.33) and the marginal corridor adds 0: (Z) per ray asks for a partner on the "
        "same rays", ok5 and -0.35 < min(aff) and max(aff) < -0.13)
    dm = d["o56"]["dminus_tan"]
    ok6 = all(abs(f["minus"]["rho"] - f["minus"]["theta"]) < 0.01 * f["minus"]["theta"] for f in F.values())
    add("O6 D-: a convex fold, a POSITIVE Nambu-Goto line (int rho ds = +t, 1%); its tangential null energy at the "
        "joint kept iff r_rim <= 3m", ok6 and dm[2.6] > 0 and dm[2.9] > 0 and dm[3.1] < 0 and dm[3.4] < 0)
    o = d["o7"]
    add("O7 cypher: M's 210 cell is the D+ cell, admitted by every language by construction; the D- open mouth with a "
        "body splits them (order, algebra, information admit; geometry, statistics refuse), statistics blocked by "
        "(lam, body), forced -- lam = +1 is held by one cell only; no key, no one-hot code",
        o["m210_is_dplus"] and all(v[0] for v in o["res"].values()) and not o["res"]["statistics"][1]
        and not o["res"]["geometry"][1] and all(o["res"][l][1] for l in ("order", "algebra", "information"))
        and ("lam", "body") in o["block"] and o["lam1_singleton"] and not o["audit"]["keys"] and not o["audit"]["onehot"])
    return res


MUTANTS = {"orient_flip": "D+ computed in the other orientation",
           "no_fold_curvature": "the fold's Y'' left out of the stress",
           "grid_rb": "r_b located on a 0.01m grid",
           "dminus_body": "the D- open mouth entered with a body"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-18s %-42s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("open_mouth.py -- the rim as an open mouth, in both orientations (item 210)\n")
    print("O1 plane data at y = 0: max deviation %.1e over %d columns; B against Schwarzschild g_rr off by up to %.0f"
          % (d["o1"]["dev"], d["o1"]["ncol"], d["o1"]["sch"]))
    o = d["o2"]
    print("O2 closed forms at y -> 0, worst relative deviation:", {k: "%.1e" % v for k, v in o["worst"].items()})
    for k, v in sorted(o["fam"].items()):
        print("   member %s rim %.3f t %5.2f deg rho_rim %.5f closed %.5f (rel %.1e) tangential at rim %+.4f"
              % (k, v["r"], math.degrees(v["theta"]), v["rho_rim"], rho_rim_closed(v["r"], v["theta"]), o["rel"][k], v["tan_rim"]))
    print("   r_b = %.9f (bisection at y = 1e-4); rim_profile's grid gives %.2f" % (o["rb"], o["rb_grid"]))
    print("O3", d["o3"])
    for k, f in d["o56"]["folds"].items():
        p, m = f["plus"], f["minus"]
        print("O5/O6 member %s rim %.3f t %.5f: D+ int rho %+.5f, rad %+.5f, affine %+.5f (-t/sqrt(1-2m/r) %+.5f), tan %+.1e;"
              " D- int rho %+.5f" % (k, p["r_rim"], p["theta"], p["rho"], p["rad"], p["rad_aff"],
                                     -p["theta"] / math.sqrt(1 - 2 / p["r_rim"]), p["tan"], m["rho"]))
    print("O6 D- tangential at the joint (t = 0.5 rad):", {r: "%+.4f" % v for r, v in d["o56"]["dminus_tan"].items()})
    o = d["o7"]
    print("O7 admitted (M's 210 cell, D- with a body):", o["res"], " statistics blocks D- with a body by", o["block"],
          " audit:", {k: o["audit"][k] for k in ("keys", "onehot")})


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
