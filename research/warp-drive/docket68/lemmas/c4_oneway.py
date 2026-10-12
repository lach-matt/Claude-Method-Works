#!/usr/bin/env python3
"""c4_oneway.py -- item 282: claim C4 (M1, the plane's reading of the corridor's mouth, at the small end) re-posed on
the glued one-way object.  C4 as verified (m1_small.py, items 262, 269) is kept as written with its item-281 note;
this is its one-way form, after C1's (c1_oneway.py).  Worked in the conversation (computed with sympy, exact where
marked; estimates marked; deduced where marked; not verified by a separate session; not seated); 2026-10-12.

  P0 (read) M's item-282 words, verbatim in the rulings file.
  P1 (computed, exact; imported from m1_small) 203, kept: the hole's Komar mass over the 3-sphere in our exterior is
     3 pi r_h^2/(8 G5), independent of r at flat order (N1), with the verifier's qualifications as seated (the AdS
     term at warp order, the hemisphere's first law, N4).  Position 2 reads the same mass from its own exterior because
     the bounce's map (U, V) -> (-U, -V) is an isometry of the form (b_bounce Q1) -- position 2's reading of its side,
     nothing passing back; the eternal solution's two isometric exteriors are no longer the reason.
  P2 (computed, exact) The plane on the object.  In the Kruskal form -F(UV) dU dV + r(UV)^2 (dchi^2 + sin^2 chi dOmega_2)
     the equator chi = pi/2 has extrinsic curvature 0 for any F and r -- computed for that general form -- so it is
     totally geodesic in every chart of the object: our exterior, our face, our future interior, position 2's past
     interior, position 2's face and exterior.  Clause (b) re-posed: the corridor is in the bulk, bridging P1 (the
     equator on our side, up to our black-hole face) and P2 (the same surface on position 2's side, from its white-hole
     face), joined through the interiors and the bounce (c1_oneway K2-K3) -- not through the eternal hole's second
     exterior; "exclusive to the bulk" holds for stress, the horizon cutting P1 (the C4 verifier's note, kept).
     (a), (c), (d) are C1's, kept (c1_oneway K1): the bulk Ricci-flat at flat order, P1 reading the equator for r_h <<
     r << ell, no matter stress on P1.
  P3 (computed; c1_oneway K4, b_bounce Q4-Q5) Clause (e) re-posed: regular on both exteriors and both faces, a smooth
     horizon at each face (curvature at most 72/r_h^4).  The interiors' r = 0 is where the bounce's quantum region
     stands (273): there the classical equations and pointwise null energy give way, every ray through it carrying net
     negative null energy, paired by the README crossing it (183).  Item 259's admission of the singularity was the
     classical interior's; on the bounce it is replaced.
  P4 (computed; e_positive E7, item 284) Clause (f) re-posed: P2 carries 139 (1)'s tension -sigma/4 and its own matter
     (268), positive where the README lands -- the README's density above sigma/4 within 2.0e-15 m = 1.8e5 r_h of the
     face (E7) -- which is where the corridor's rays cross P2 (284).  A ray crossing P2 there at angle a picks up e sin a
     + (e + P) cos^2 a / sin a >= 0 for e > 0 and e + P >= 0 (m1p2x_sixth W1, a direction-neutral share).  The
     earlier (f) -- the same positive tension, within one universe (L7) -- is set aside: between universes 139 (1)
     puts -sigma/4 on P2.
  P5 (estimate) The state.  The one-way object opens -- it is formed, not eternal -- so its quantum state is the
     collapse-formed one, outgoing Hawking flux without the Hartle-Hawking bath's ingoing half; m1_small N4's bath
     (rho/sigma = 0.305, bending P1 0.92 as much as the tension) is the eternal manifold's and is dropped.  The outgoing
     flux keeps the order: with the hole's luminosity P = E/(2 life) from hold_small L5 (greybody included), the flux's
     energy density on P1 at r = r_h, P/(4 pi r_h^2 c), is 0.29 sigma -- the same order as the bath.  C4's
     qualification (5), "C4 is classical", stands on the one-way object: near the hole the plane's quantum load is of
     the order of its tension.
  P6 (deduced) The ledger.  Kept: N1 (203, with its qualifications), (a), (c), (d), the kink at warp order (KTN,
     READ by the C1 verifier; through the faces deduced, KTN computing only outside the horizon).  Re-posed: (b) through
     the bounce, (e) with the quantum region, (f) between universes, the state.  Dropped (282): P2 on the eternal hole's
     second exterior, the bridge's slice in (e), the Hartle-Hawking bath.  So M1 holds at the small end on the one-way
     object on (a)-(f) at flat order in classical GR, with the quantum flux of P5 near the hole.
  P7 (computed; the cypher, roster 1173, audited) C4's construction choices as an index: the interior's continuation
     -- b_interior B6's own one-way cells, those exiting into position 2 (inner horizon, quantum bounce, classical
     shell) -- x P2's tension (139 (1)'s -sigma/4, or +sigma) x P2's own matter (none, or the README where it lands): 12
     rows, each with complete (no singularity on the route, B6), readme_only (B6), keeps139 and p2pos (clause (f),
     positive where relevant, 285).  The all-four cell is reached by one row only: the quantum bounce, P2 at -sigma/4,
     the README where it lands -- C4's one-way form (273, 139 (1), 284).  The languages split: geometry, information
     and statistics admit exactly the nine held cells (E = 0); order and algebra add three (E = 3) -- for each
     continuation the cell with P2 neither keeping 139 (1) nor positive, which the index cannot hold, its only other
     tension being +sigma, positive always; K.langclose holds (4 of 10 pairs agreeing), audit clean.  Not widened to
     make it agree.  The object's causal order is c1_oneway K6's run, which agreed.  (First written NOT-RUN.)
     [M, item 286: the cypher is a calculator, not an index tool -- P7 reads the languages' agreement on E, the index
     reading; kept as its record.  P8 is the question through the calculator.]
  P8 (computed; calculator.py, items 286-287; the encoding the board's, 192) C4's question in binary form: does M1
     hold?  Its coordinates are the clauses of M1 that vary across P7's twelve configurations -- (a) vacuum (the
     classical shell carries stress in the bulk, b_interior B5), (b)/(e) a complete route (B6), (f) P2 positive where
     relevant (285) -- and the answer M1, computed for the other eleven; C4's configuration enters with its answer
     open.  Analysis carries (f)'s continuous law, the README's density at the face over sigma/4, (R/r_h)^3 = 5.9e15
     against 1 (e_positive E7), giving both binaries (288): 1 at +15.8 decades, 0 at -15.8.  Broadest first, order,
     algebra, geometry, information and statistics each leave 0 and 1 open -- logic returns both, undecided, by
     statistics; analysis's magnitudes rank 1 over 0 (288 (c)).  The hierarchy law's seven containments hold on the run.
     Control (named): with 139 (1) entered as a fourth coordinate -- a ruling M1's clauses do not contain -- statistics
     admits only 0 and logic returns 0, because no other configuration keeps 139 (1) and holds M1: the AND limit
     (calculator C6).  [First run on the item-287 build, analysis returning one binary and narrowing to it: logic 1,
     the control refused -- M, item 288: "you built the calculator wrong".  Rerun on the rebuilt calculator.]
  P9 (computed; calculator.py, item 289; deduced where marked) Widening, checked before it is done (289's reading).
     The board's coordinates are binary, so every cell that could be added is one of the sixteen in {0,1}^3 x {0,1};
     the eleven known configurations occupy six, and the 2^10 = 1024 supersets of them are every widening there is,
     computed configurations or not.  On all 1024, at every admissible statistics order -- 1, 2 and 3; order 4 is
     refused, the order needing fewer coordinates than the index has (reg 1175) -- order, algebra, geometry,
     information and statistics each admit both 0 and 1 at C4's cell, so logic returns both on every widening.  Each
     language is monotone on all 1024 (its admitted set over the known cells lies inside its set over every widening):
     added cells only widen.  Why both are open already: 1 by extensivity -- C4's attributes (1, 1, 1) are a known
     cell with M1 holding, the quantum bounce with P2 at +sigma, with and without the README; 0 because each clause is
     seen failing alone -- (0, 1, 1) the classical shell, (1, 0, 1) the inner horizon, (1, 1, 0) the quantum bounce at
     -sigma/4 without the README -- so every projection of (1, 1, 1, 0) of order 3 or less is seen (with the shell's
     cells removed, order 3 excludes 0: the fails_alone_dropped mutant).  Deduced, in general: at any order below the
     coordinate count, each projection of a conjunction's corner with answer 0 leaves out a coordinate, and is seen in
     the cell where that clause fails alone, or, on the attributes alone, in the question's own cell -- so statistics
     admits 0 at the corner of any conjunction whose clauses have each been seen failing alone, and so do order,
     algebra and geometry, which contain it (hlaw.py's LAWFUL); only information, which does not contain it, could
     exclude 0, and on C4's index it does not on any widening.  The cells that show each clause matters are the cells
     that keep 0 open.  So adding cells (289) cannot decide C4's question in this encoding.  Under P8's control every
     language admits 0 now, so it stays admitted under any widening (deduced: the languages are closure operators,
     monotone in their cells, as measured here on the board's index): the control gives 0 or both, never 1.

What this does not show.
  - The kink through the faces and the interiors (deduced from KTN's exterior, not computed).
  - The flux's back-reaction on P1 (P5 is the load's size, not the bending computed).

Imports m1_small.py, c1_oneway.py, e_positive.py and hold_small.py by path.  Stdlib + sympy.
python3 c4_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
MUT = {}
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
FIVE = ["order", "algebra", "geometry", "information", "statistics"]
PROPS = ["complete", "readme_only", "keeps139", "p2pos"]
M282 = "Re-pose them one-way (Recommended)"


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [HERE]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def komar():
    MS = _load("m1_small.py", "c4o_ms")
    o = MS.compute()
    res = {n.split()[0]: ok for n, ok in MS.checks(o)}
    return dict(N1=res.get("N1", False), N4=res.get("N4", False), r_free=o["k5"]["r_free"])


def equator():
    """P2: the equator's extrinsic curvature in the Kruskal form, F and r arbitrary functions of U V"""
    U, V, chi, th, ph = sp.symbols("U V chi theta phi", real=True)
    F = sp.Function("F")(U * V)
    R = sp.Function("R")(U * V)
    g = sp.zeros(5, 5)
    g[0, 1] = g[1, 0] = -F / 2
    ang = [1, sp.sin(chi) ** 2, sp.sin(chi) ** 2 * sp.sin(th) ** 2]
    if MUT.get("bent_equator"):
        ang = [1, sp.sin(chi) ** 2 * (1 + sp.cos(chi)), sp.sin(chi) ** 2 * sp.sin(th) ** 2]   # breaks chi -> pi - chi
    for i, a in enumerate(ang):
        g[2 + i, 2 + i] = R ** 2 * a
    # unit normal along chi: n^chi = 1/R; K_ab = (1/2) n^chi d_chi g_ab on the surface's tangent directions
    K = [sp.simplify((sp.diff(g[i, i], chi) / (2 * R)).subs(chi, sp.pi / 2)) for i in (3, 4)]
    K_tu = [sp.simplify((sp.diff(g[0, 1], chi) / (2 * R)).subs(chi, sp.pi / 2))]
    return dict(K=K + K_tu, zero=all(k == 0 for k in K + K_tu))


def c1_parts():
    C1 = _load("c1_oneway.py", "c4o_c1")
    res = {n.split()[0]: ok for n, ok in C1.checks(C1.compute())}
    return {k: res[k] for k in ("K1", "K2", "K3", "K4")}


def positive():
    EP = _load("e_positive.py", "c4o_ep")
    x = EP.example()
    e, sn = sp.symbols("e s", positive=True)                 # s = sin a in (0, 1], a ray's angle to the plane
    P, cs2 = sp.symbols("P c2", nonnegative=True)            # c2 = cos^2 a; P with e + P >= 0
    share = e * sn + (e + P) * cs2 / sn
    return dict(R=x["R"], R_rh=x["R_rh"], share_pos=bool(share.is_positive))


def state():
    """P5: the collapse-formed state's outgoing flux on P1 at r = r_h, against sigma"""
    H = _load("hold_small.py", "c4o_hold")
    life = H.l5_checks()["life"]
    PG = _load("p2_gravity.py", "c4o_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    N = 2742570311524972
    rh = (2 * N * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    E = 3 * math.pi * PG.C ** 4 * rh ** 2 / (8 * PG.G * PG.ELL_MAX)
    sigma = 3 * PG.C ** 4 / (4 * math.pi * PG.G * PG.ELL_MAX ** 2)
    P = E / (2 * life)
    if MUT.get("bath_kept"):
        P = 2 * P                                          # the mutant keeps the bath's ingoing half too
    rho = P / (4 * math.pi * rh ** 2 * PG.C)
    return dict(P=P, ratio=rho / sigma, life=life)


def choices():
    """P7: b_interior's one-way continuations x P2's tension x P2's matter; the cypher"""
    BI = _load("b_interior.py", "c4o_bi")
    cells = {k: v for k, v in BI.cells().items() if k[2] == "pos2"}
    rows = {}
    for (inner, bounce, _), p in cells.items():
        for t, m in itertools.product(("-sigma/4", "+sigma"), (0, 1)):
            pos = int(m == 1 or t == "+sigma")
            if MUT.get("p2_free_positive") and t == "-sigma/4":
                pos = 1                                    # the mutant takes P2 positive without the README
            rows[(inner, bounce, t, m)] = dict(complete=p["complete"], readme_only=p["readme_only"],
                                               keeps139=int(t == "-sigma/4"), p2pos=pos)
    held = sorted({tuple(p[c] for c in PROPS) for p in rows.values()})
    cy = _load_path(os.path.join(ROOT, "tools", "cypher.py"), "c4o_cy")
    ia = _load("index_audit.py", "c4o_ia")
    run = cy.run(cy.Index("c4_oneway", PROPS, [list(c) for c in held], value_order={c: [0, 1] for c in PROPS}), "1173",
                 dict(OPTS))
    return dict(n=len(rows), held=held, E={v["language"]: v["E"] for v in run["verdicts"]},
                langclose=run["langclose_holds"], agreeing=run["pairs_agreeing"], audit=ia.audit_index(PROPS, held),
                holders=sorted(k for k, p in rows.items() if tuple(p[c] for c in PROPS) == (1, 1, 1, 1)))


def _load_path(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def calc():
    """P8: C4's question through the calculator, the board's encoding and the named control"""
    CA = _load("calculator.py", "c4o_calc")
    BI = _load("b_interior.py", "c4o_bi2")
    EP = _load("e_positive.py", "c4o_ep2")
    ratio = EP.example()["R_rh"] ** 3
    if MUT.get("readme_thin"):
        ratio = 0.5                                        # the mutant puts the README's density below sigma/4
    cells = {k: v for k, v in BI.cells().items() if k[2] == "pos2"}
    rows = {}
    for (inner, bounce, _), p in cells.items():
        vac = int(bounce != "shell")
        for t, m in itertools.product(("-sigma/4", "+sigma"), (0, 1)):
            pos = int(m == 1 or t == "+sigma")
            rows[(inner, bounce, t, m)] = dict(vac=vac, complete=p["complete"], p2pos=pos, keeps=int(t == "-sigma/4"),
                                               m1=int(vac and p["complete"] and pos))
    q = (0, "quantum", "-sigma/4", 1)
    out = {}
    for tag, coords in (("board", ["vac", "complete", "p2pos"]), ("with139", ["vac", "complete", "p2pos", "keeps"])):
        known = [tuple(r[c] for c in coords) + (r["m1"],) for k, r in rows.items() if k != q]
        attrs = tuple(rows[q][c] for c in coords)
        r = CA.ask(coords + ["m1"], known, attrs,
                   analysis={"witness": "e_positive E7: (R/r_h)^3", "magnitude": ratio, "threshold": 1.0},
                   citations=["273", "139 (1)", "268", "276", "282", "284", "285"])
        r["lawful"] = CA.controls(coords + ["m1"], known, attrs)["lawful"]
        out[tag] = r
    return dict(ratio=ratio, **out)


_P9 = {}


def widen():
    """P9: every widening of the known cells in the board's encoding, at every admissible statistics order"""
    CA = _load("calculator.py", "c4o_calc")
    BI = _load("b_interior.py", "c4o_bi3")
    cells = {k: v for k, v in BI.cells().items() if k[2] == "pos2"}
    rows = {}
    for (inner, bounce, _), p in cells.items():
        vac = int(bounce != "shell")
        for t, m in itertools.product(("-sigma/4", "+sigma"), (0, 1)):
            pos = int(m == 1 or t == "+sigma")
            hold = int(vac or p["complete"] or pos) if MUT.get("m1_or") else int(vac and p["complete"] and pos)
            rows[(inner, bounce, t, m)] = dict(attrs=(vac, p["complete"], pos), m1=hold)
    q = (0, "quantum", "-sigma/4", 1)
    attrs = rows[q]["attrs"]
    known = {k: r for k, r in rows.items() if k != q}
    if MUT.get("fails_alone_dropped"):
        known = {k: r for k, r in known.items() if r["attrs"] != (0, 1, 1)}   # the mutant: vac never fails alone
    base = sorted({r["attrs"] + (r["m1"],) for r in known.values()})
    coords = ["vac", "complete", "p2pos", "m1"]
    key = (tuple(base), attrs)
    if key not in _P9:
        amb = [a + (m,) for a in itertools.product((0, 1), repeat=3) for m in (0, 1)]
        extra = [c for c in amb if c not in base]
        qc = attrs + (CA.U,)
        langs = [(L, 2) for L in ("order", "algebra", "geometry", "information")] + [("statistics", k) for k in (1, 2, 3)]
        said = lambda cl: sorted(a for a in (0, 1) if cl is not None and attrs + (a,) in cl)
        at_base = {lk: CA.closure(coords, base + [qc], *lk) for lk in langs}
        n, both, mono = 0, True, True
        for r_ in range(len(extra) + 1):
            for add in itertools.combinations(extra, r_):
                cs = base + list(add) + [qc]
                for lk in langs:
                    cl = CA.closure(coords, cs, *lk)
                    both &= said(cl) == [0, 1]
                    mono &= cl is not None and at_base[lk] <= cl
                n += 1
                if not (both and mono):
                    break
            if not (both and mono):
                break
        k4 = CA.ask(coords, base, attrs, k=4)
        _P9[key] = dict(n=n, extra=len(extra), both=both, mono=mono,
                        k4=dict((t[0], t[1]) for t in k4["trace"])["statistics"], k4_answer=k4["answer"])
    o = dict(_P9[key])
    o["positives"] = sorted(k for k, r in known.items() if r["attrs"] == attrs and r["m1"] == 1)
    o["alone"] = [any(r["attrs"] == tuple(int(i != j) for i in range(3)) and r["m1"] == 0 for r in known.values())
                  for j in range(3)]
    return o


def compute():
    return dict(k=komar(), eq=equator(), c1=c1_parts(), pos=positive(), st=state(), ch=choices(), ca=calc(),
                wd=widen())


def report(o):
    print("c4_oneway.py -- claim C4 re-posed on the one-way object (item 282)\n")
    print("P1 m1_small N1 %s, N4 %s; Komar mass free of r: %s" % (o["k"]["N1"], o["k"]["N4"], o["k"]["r_free"]))
    print("P2 the equator's extrinsic curvature in the Kruskal form, any F(UV), r(UV): %s -- zero: %s; c1_oneway %s" % (
        o["eq"]["K"], o["eq"]["zero"], o["c1"]))
    p = o["pos"]
    print("P4 the README carries P2 past sigma/4 within %.3g m = %.3g r_h; the crossing share positive: %s" % (
        p["R"], p["R_rh"], p["share_pos"]))
    s = o["st"]
    print("P5 luminosity %.3g W (life %.3g s); outgoing flux on P1 at r_h: %.2g sigma (m1_small N4's bath: 0.305)" % (
        s["P"], s["life"], s["ratio"]))
    ca = o["ca"]
    for tag in ("board", "with139"):
        print("P8 %s: answer %s by %s, ranked %s, magnitudes %s; %s; lawful %s" % (
            tag, ca[tag]["answer"], ca[tag]["by"], ca[tag]["ranked"], ca[tag]["magnitudes"],
            "; ".join("%s %s" % (t[0], t[1]) for t in ca[tag]["trace"] if t[0] != "documentary"), ca[tag]["lawful"]))
    w = o["wd"]
    print("P9 widenings %d of 2^%d: both at every language and statistics order 1-3 %s, monotone %s; order 4: %s; "
          "C4's attributes known with M1 by %s; each clause seen failing alone %s" % (
              w["n"], w["extra"], w["both"], w["mono"], w["k4"], w["positives"], w["alone"]))
    ch = o["ch"]
    print("P7 %d rows; held %s; all four by %s; E %s; langclose %s, %d of 10 pairs agreeing; audit keys %s one-hot %s" % (
        ch["n"], ch["held"], ch["holders"], ch["E"], ch["langclose"], ch["agreeing"], ch["audit"]["keys"],
        ch["audit"]["onehot"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("P0 M's item-282 words verbatim in the rulings file", M282 in rul)
    add("P1 203 kept: the Komar mass 3 pi r_h^2/(8 G5), free of r at flat order (m1_small N1, N4)",
        o["k"]["N1"] and o["k"]["N4"] and o["k"]["r_free"])
    add("P2 the equator is totally geodesic in the Kruskal form for any F(UV), r(UV) -- every chart of the object; "
        "C1's (a), (c), (d) and the faces and route hold (c1_oneway K1-K3)", o["eq"]["zero"] and o["c1"]["K1"] and
        o["c1"]["K2"] and o["c1"]["K3"])
    add("P3 regular on both exteriors and faces (c1_oneway K4)", o["c1"]["K4"])
    p = o["pos"]
    add("P4 P2 positive where the README lands: above sigma/4 within 2.0e-15 m = 1.8e5 r_h; the crossing share positive",
        "%.2g" % p["R"] == "2e-15" and "%.2g" % p["R_rh"] == "1.8e+05" and p["share_pos"])
    s = o["st"]
    add("P5 the collapse-formed state's outgoing flux on P1 at r_h is 0.29 sigma, the order of N4's bath",
        "%.2f" % s["ratio"] == "0.29")
    ch = o["ch"]
    ok = ch["n"] == 12 and len(ch["held"]) == 9 and ch["holders"] == [(0, "quantum", "-sigma/4", 1)]
    ok &= [ch["E"][L] for L in FIVE] == [3, 3, 0, 0, 0] and ch["langclose"] and ch["agreeing"] == 4
    ok &= not ch["audit"]["keys"] and not ch["audit"]["onehot"]
    add("P7 the all-four cell only by the quantum bounce with P2 at -sigma/4 and the README where it lands; E 3, 3, 0, "
        "0, 0, langclose holds, audit clean", ok)
    ca = o["ca"]
    tb = dict((t[0], t[1]) for t in ca["board"]["trace"])
    ok = ca["board"]["answer"] == "both" and ca["board"]["by"] == "statistics" and ca["board"]["ranked"] == 1
    ok &= all(tb[L] == [0, 1] for L in ("order", "algebra", "geometry", "information", "statistics"))
    ok &= tb["analysis"] == "both" and "%.3g" % ca["board"]["magnitudes"][1] == "15.8" and ca["board"]["lawful"]
    ok &= ca["with139"]["answer"] == 0 and ca["with139"]["lawful"] and "%.2g" % ca["ratio"] == "5.9e+15"
    add("P8 through the calculator, broadest first: logic returns both (undecided), by statistics, analysis ranking 1 "
        "at +15.8 decades over 0; the control with 139 (1) as a coordinate 0 (the AND limit); the law's containments "
        "hold", ok)
    w = o["wd"]
    ok = w["n"] == 1024 and w["extra"] == 10 and w["both"] and w["mono"] and w["k4"] == "silent"
    ok &= w["positives"] == [(0, "quantum", "+sigma", 0), (0, "quantum", "+sigma", 1)] and all(w["alone"])
    add("P9 every widening of the known cells (1024, the encoding's whole ambient) leaves both answers open in every "
        "closure language at statistics orders 1-3, each monotone; order 4 refused (reg 1175); 1 open by extensivity "
        "(the quantum bounce at +sigma), 0 because each clause is seen failing alone", ok)
    return res


MUTANTS = {"bent_equator": "the reflection chi -> pi - chi broken in the angular metric",
           "p2_free_positive": "P2 taken positive at -sigma/4 without the README",
           "readme_thin": "the README's density at the face put below sigma/4",
           "bath_kept": "the Hartle-Hawking bath's ingoing half kept",
           "fails_alone_dropped": "the known cells where (a) alone fails removed (P9)",
           "m1_or": "M1 read as any one clause holding, not all (P9)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-14s %-58s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
