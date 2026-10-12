#!/usr/bin/env python3
"""c1_oneway.py -- item 282: claim C1 re-posed on the glued one-way object.  M: "Re-pose them one-way (Recommended)"
-- "their outside-the-hole figures are kept; the slice crossing, the bifurcation sphere, the past interior and the
throat-as-narrowest-sphere are dropped".  C1 as verified (localized_hole.py, items 252, 254) is kept as written with
its item-281 note; this is its one-way form.  Worked in the conversation (computed with sympy, exact where marked;
deduced where marked; not verified by a separate session; not seated); 2026-10-12.

  K0 (read) M's item-282 words, verbatim in the rulings file.
  K1 (computed, exact; imported from localized_hole) Kept, outside the hole: the bulk is five-dimensional
     Schwarzschild-Tangherlini, f = 1 - r_h^2/r^2, Ricci-flat (clause (B)), Kretschmann 72 r_h^4/r^8 (H1); our plane is
     the equator, totally geodesic, no matter stress at flat order, its own four-dimensional reading the bulk's
     traceless Weyl term (H2 with the verifier's qualification (1)); the plane reads -f dt^2 + dr^2/f + r^2 dOmega^2,
     Ricci scalar 0, a 1/r^2 pull for r_h << r << ell (H3 with qualification (2)); the horizon's chart -- surface
     gravity 1/r_h, Kruskal F = r_h^2 (r + r_h)^2 e^(-2r/r_h)/r^2 finite and positive at r_h, pulling back to the static
     metric (H4's first half); the example (H6) and the kink at order r_h/ell (H7).
  K2 (computed, exact) The faces, not the bridge.  Our black-hole face is U = 0 from the opening, V >= V_open > 0
     (270 (c): the faces begin at the opening); position 2's white-hole face is U = 0 from V_s < 0 to its closing,
     V_close = V_s e^(-Delta tau_2) with Delta tau_2 <= 33.6 clocks at the small-end example (c_junction J1; ln(1 +
     (pi/10)(ell/r_h)), finite at every r_h, which is all K2 needs), so V_close = V_s e^(-33.6) < 0.
     V = 0 -- the bifurcation sphere U = V = 0 and the reverse passage -- lies on neither face.  Our plane, the
     equator, is untouched by the chart, so it runs on our side up to our face and, the same surface, on position 2's
     side from its face: not "through the bifurcation sphere".
  K3 (computed; j_readings J1, i_oneway I2) The README's route.  Our exterior reaches position 2's exterior only
     through our future interior, the bounce (H-BOUNCE-TO-P2) and position 2's past interior; no chart of the object
     joins the two exteriors directly -- the eternal solution's t = 0 slice, which did, is not a part of it.  The README
     crosses along that route, each part in at most one of its own clocks to the quantum region and as long again out
     -- one way, the information it carries (251) crossing with it -- not along a slice no causal curve follows.
  K4 (computed, exact) Regularity on the object: Kretschmann 72 r_h^4/r^8 falls with r, so it is finite on both
     exteriors and both faces (r >= r_h), at most 72/r_h^4 at the faces, and tends to 0 far away.  Its divergence at
     r = 0 lies in the interiors, where the bounce's quantum region stands (b_bounce Q4: the classical equations do not
     hold there) -- the singularity C1 left in the future and past interiors is replaced, not crossed.
  K5 (deduced) The ledger.  Kept: H1, H2, H3, H4's horizon chart, H5's curvature outside, H6, H7, and the verifier's
     qualifications (1) and (2).  Dropped (282): H4's continuation through the bifurcation sphere, the t = 0 slice and
     its minimal sphere at r_h, the second exterior as the eternal solution's, "the bridge is not traversable ... only
     the README crosses, as information" (replaced by K3's one-way route), and H5's regularity of the bridge's slice
     and of a past interior on our side.  The verifier's qualification (3) -- the minimal sphere pinching off, the
     second exterior only in the eternal solution -- is moot: what it qualified is dropped.
  K6 (computed; the cypher, roster 1173, audited; item 283) The passage's causal order as an index.  Its seven
     regions in the order the passage runs -- our exterior, our face, our future interior, the quantum region, position
     2's past interior, position 2's face, position 2's exterior -- from j_readings J1's chart graph, each face inserted
     where its chart edge crosses U = 0 and the quantum region on the bounce.  The reachable pairs (from, to) are 28,
     exactly those with from <= to in the passage's order, none the other way; but a two-coordinate index is
     degenerate -- statistics is silent, "needs more than 2 coordinates at order 2 (reg 1175)", 6 of 10 pairs -- so the
     cypher runs on the order's routes: each cell a triple (from, through, to), "through" reachable from "from" and
     "to" from "through" -- 84 cells, exactly from <= through <= to.  The five operator-bearing languages agree at E = 0
     (10 of 10 pairs), the run is not degenerate, K.langclose holds and index_audit is clean: the one-way order, and
     every route through it, is a closed index in every language.  A two-way passage would hold the whole box of 343,
     which is closed too: the cypher's agreement certifies the order as an index, not its direction -- the direction is
     the held set itself, the 84 forward routes and none back (K3, and this check).
     (First written as NOT-RUN, a construction with no cells; M, item 283: "Run the cypher on it".)
     [Item 298, the board's audit: the one verifier sent on C1 under 283 was stopped mid-run, when M interrupted the
     board's question that followed ("Put the question to me again"), and returned no verdict -- C1 one-way is not
     verified.  And K6 is the index reading item 286 set aside: C1's question is owed through the calculator, as C4's
     was (c4_oneway P8-P13).]
  K7 (computed; calculator.py, items 286-302; the encoding the board's, 192, in the form C4's question settled,
     c4_oneway P13-P20) C1's question through the calculator: does C1 hold on the one-way object as built -- the
     quantum bounce, P2 at -sigma/4, the README where it lands?  Clause by clause (291's form), the clauses of C1 that
     vary across the configurations: (B) the bulk vacuum (b_interior B5; C4's (a), kept from C1), K2 the one-way faces
     -- the interior opening into position 2 (b_interior's one_way) -- and K3-K4 a complete, regular route (B6; C4's
     (b)/(e)).  The rest (H2-H7, outside the hole) hold in every configuration and vary with none.  The conditions: the
     continuation by its own two clauses, NEC holding and README-only, all four interiors entered (c4_oneway P20); P2's
     tension and matter in every clause, read at statistics' rank (P13), over the population (295) -- C1's clauses
     depend on neither, so every (tension, matter) class carries each interior's own answers.  By interior, (B, K2,
     K3-K4): the singular (1, 0, 0), the inner horizon (1, 1, 0), the quantum bounce (1, 1, 1), the shell (0, 1, 1).
     Orders 2 and 3: each clause 1, lawful, and logic joins 1 -- C1 holds.  Under all 24 codes order 3 decides 1, 1, 1
     in every one and order 2 in 22 (the other 2 put the quantum bounce and the shell on a diagonal, leaving K3-K4
     open).  Order 4: the operator refuses all three, each a binary communication (302) -- (B) carried by README-only
     (the shell its neighbour), K2 and K3-K4 by NEC (the singular interior its neighbour); under the channel reading
     (c4_oneway P20) 1, 1, 1 in every code, and each interior entered as the question returns its own three clauses.
     The continuation alone, without tension and matter, refuses all three at orders 1 and 2: the quantum bounce's
     clauses do not follow from the other three interiors' -- what decides them is the quantum bounce's own other
     configurations, which the population of tensions and matters supplies (293: they stay in the question).  So the
     cypher agrees, in C4's form, at every lawful order -- the condition 283 set for the verifier.

What this does not show.
  - The bounce's quantum region as a metric (b_bounce's "does not show"); K3 uses its join, not its interior.
  - Where our face's opening V_open sits in our time, and position 2's V_s in its (joined only through the quantum
    region, c_junction J3).
  - C4, C5 and C7 re-posed: the next instruments, in that order (282 (b)).

Imports localized_hole.py, j_readings.py, c_junction.py, i_oneway.py, and for K7 c4_oneway.py, calculator.py,
b_interior.py and research/warp-drive/hlaw.py, by path.  Stdlib + sympy.
python3 c1_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
from collections import Counter
import itertools
import io
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
REGIONS = ["our exterior", "our face", "our future interior", "the quantum region", "position 2's past interior",
           "position 2's face", "position 2's exterior"]
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


def kept():
    """K1: C1's outside-the-hole figures, from localized_hole itself"""
    LH = _load("localized_hole.py", "c1o_lh")
    o = LH.compute()
    res = {n.split()[0]: ok for n, ok in LH.checks(o)}
    br = o["bridge"]
    rh = LH.rh
    r = sp.Symbol("r", positive=True)
    K = o["bulk"]["K"]
    Kr = K.subs(LH.r, r) if hasattr(LH, "r") else K
    return dict(checks={k: res[k] for k in ("H1", "H2", "H3", "H6")}, kappa_ok=sp.simplify(br["kappa"] - 1 / rh) == 0,
                F_pos=br["finite_positive"], pullback=br["pullback"], K=Kr, rh=rh, r=r)


def faces():
    """K2: both faces bounded away from V = 0"""
    CJ = _load("c_junction.py", "c1o_cj")
    t_full = CJ.compute()["ex"]["t_full"]
    if MUT.get("white_open_long"):
        t_full = float("inf")                              # the mutant keeps position 2's face open for ever
    V_open, V_s = sp.Rational(1, 10), -sp.Integer(1)       # any V_open > 0 and V_s < 0; the signs are what count
    if MUT.get("opens_at_bifurcation"):
        V_open = sp.Integer(0)                             # the mutant opens our face at U = V = 0
    V_close = V_s * sp.exp(-t_full) if t_full != float("inf") else sp.Integer(0)
    return dict(t_full=t_full, ours=bool(V_open > 0), theirs=bool(V_close < 0), V_close=V_close)


def route():
    """K3: the README's route, from j_readings' chart graph; the crossing time from i_oneway"""
    JR = _load("j_readings.py", "c1o_jr")
    c = JR.causal()
    edges = set(c["edges"])
    if MUT.get("slice_route"):
        edges.add(("our exterior", "position 2's exterior"))   # the mutant restores the eternal slice's join
    direct = ("our exterior", "position 2's exterior") in edges or ("position 2's exterior", "our exterior") in edges
    chain = [("our exterior", "our future interior"), ("our future interior", "position 2's past interior"),
             ("position 2's past interior", "position 2's exterior")]
    IO = _load("i_oneway.py", "c1o_io")
    cr = IO.crossing()
    return dict(edges=sorted(edges), direct=direct, chain=all(e in edges for e in chain),
                p2_back=c["reach_p2"], crossing=cr["closed"] and cr["max_one"])


def regular(k):
    r, rh, K = k["r"], k["rh"], k["K"]
    at_face = sp.simplify(K.subs(r, rh))
    falls = sp.simplify(sp.diff(K, r)).is_negative
    far = sp.limit(K, r, sp.oo)
    return dict(at_face=at_face, falls=bool(falls) if falls is not None else bool(sp.simplify(sp.diff(K, r) < 0)),
                far=far)


def order_index(rt):
    """K6: the seven regions' reachability, from the chart graph; the cypher on the (from, to) pairs"""
    face = {("our exterior", "our future interior"): "our face",
            ("position 2's past interior", "position 2's exterior"): "position 2's face"}
    edges = set()
    for a, b in rt["edges"]:
        mid = face.get((a, b)) or ("the quantum region" if (a, b) == ("our future interior",
                                                                      "position 2's past interior") else None)
        if mid:
            edges |= {(a, mid), (mid, b)}
        else:
            edges.add((a, b))
    if MUT.get("reverse_edge"):
        edges.add(("position 2's exterior", "our exterior"))   # the mutant puts a way back
    reach = {x: {x} for x in REGIONS}
    changed = True
    while changed:
        changed = False
        for a, b in edges:
            for x in REGIONS:
                if a in reach[x] and b not in reach[x]:
                    reach[x].add(b)
                    changed = True
    idx = {x: i for i, x in enumerate(REGIONS)}
    pairs = sorted((idx[x], idx[y]) for x in REGIONS for y in reach[x])
    held = sorted((idx[x], idx[y], idx[z]) for x in REGIONS for y in reach[x] for z in reach[y])
    cy = _load_path(os.path.join(ROOT, "tools", "cypher.py"), "c1o_cy")
    ia = _load("index_audit.py", "c1o_ia")
    coords = ["from", "through", "to"]
    runs = {}
    for tag, cells, cs in (("pairs", pairs, ["from", "to"]), ("routes", held, coords)):
        ix = cy.Index("c1_oneway_" + tag, cs, [list(c) for c in cells], value_order={c: list(range(7)) for c in cs})
        runs[tag] = cy.run(ix, "1173", dict(OPTS))
    run = runs["routes"]
    return dict(pairs=pairs, held=held,
                upper=pairs == sorted(c for c in itertools.product(range(7), repeat=2) if c[0] <= c[1]),
                chains=held == sorted(c for c in itertools.product(range(7), repeat=3) if c[0] <= c[1] <= c[2]),
                pairs_degenerate=runs["pairs"]["degenerate"], degenerate=run["degenerate"],
                E={v["language"]: v["E"] for v in run["verdicts"]}, langclose=run["langclose_holds"],
                agreeing=run["pairs_agreeing"], audit=ia.audit_index(coords, held))


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


_K7 = {}
CLAUSES1 = ("B", "K2", "K34")
INTERIORS = ["singular", "inner", "quantum", "shell"]


def calc_question():
    """K7: C1's question through the calculator, in the form C4's question settled (c4_oneway P13-P20)"""
    key = tuple(sorted(k for k in MUT if k.startswith("k7_")))
    if key in _K7:
        return _K7[key]
    C4 = _load("c4_oneway.py", "c1o_c4")
    if MUT.get("k7_channel_off"):
        C4.MUT["channel_off"] = True                        # the mutant: continuation bits held to the one-flip rule
    CA = _load("calculator.py", "c1o_calc")
    HL = _load_path(os.path.join(os.path.dirname(D68), "hlaw.py"), "c1o_hl")
    BI = _load("b_interior.py", "c1o_bi")
    cells = BI.cells()
    inter = {"singular": cells[(0, "none", "ours")], "inner": cells[(1, "none", "pos2")],
             "quantum": cells[(0, "quantum", "pos2")], "shell": cells[(0, "shell", "pos2")]}
    vals = {"B": {k: int(k != "shell") for k in INTERIORS},         # the bulk vacuum (b_interior B5; C4's (a))
            "K2": {k: inter[k]["one_way"] for k in INTERIORS},       # the interior opens into position 2
            "K34": {k: inter[k]["complete"] for k in INTERIORS}}     # a complete, regular route (B6; C4's (b)/(e))
    if MUT.get("k7_singular_opens"):
        vals["K2"]["singular"] = 1                          # the mutant: the singular interior given a face in position 2
    own = {k: (inter[k]["nec"], inter[k]["readme_only"]) for k in INTERIORS}
    pop = not MUT.get("k7_no_population")
    views = dict(order=(0, 1), algebra=(0, 1), geometry=(0, 1), information=(0, 1),
                 statistics=(0, 1, 2, 3) if pop else (0, 1))

    def known(cl, cm, q):
        rows = []
        for kk in INTERIORS:
            for t, m in (itertools.product((0, 1), repeat=2) if pop else [(1, 1)]):
                if (kk, t, m) == q:
                    continue
                rows.append(cm[kk] + ((t, m) if pop else ()) + (vals[cl][kk],))
        return rows

    def run(code, k, q="quantum", rule=False):
        cm = dict(zip(INTERIORS, code))
        at = cm[q] + ((1, 1) if pop else ())
        names = ["c1", "c2", "t", "m"] if pop else ["c1", "c2"]
        if rule:
            return tuple(C4._channel_rule(known(cl, cm, (q, 1, 1)), at) for cl in CLAUSES1), True
        rs = [C4._staged(CA, HL, names + [cl], known(cl, cm, (q, 1, 1)), at, views, k) for cl in CLAUSES1]
        return tuple(r["answer"] for r in rs), all(r["lawful"] for r in rs)

    ownc = tuple(own[k] for k in INTERIORS)
    codes = list(itertools.permutations([(0, 0), (0, 1), (1, 0), (1, 1)], 4))
    out = dict(vals=vals, own=own, ownrun={k: run(ownc, k) for k in (1, 2, 3, 4)},
               all={k: Counter(run(c, k)[0] for c in codes) for k in (2, 3, 4)},
               rule=run(ownc, 4, rule=True)[0], allrule=Counter(run(c, 4, rule=True)[0] for c in codes),
               control={q: (run(ownc, 4, q=q, rule=True)[0], tuple(vals[cl][q] for cl in CLAUSES1)) for q in INTERIORS})
    C4.MUT.clear()
    # the continuation alone, no tension or matter: what the cypher can say of the quantum bounce from the other three
    v3 = dict(order=(0, 1), algebra=(0, 1), geometry=(0, 1), information=(0, 1), statistics=(0, 1))
    cm = dict(zip(INTERIORS, ownc))
    out["alone"] = {k: tuple(C4._staged(CA, HL, ["c1", "c2", cl], [cm[kk] + (vals[cl][kk],) for kk in INTERIORS
                                                                   if kk != "quantum"], cm["quantum"], v3, k)["answer"]
                             for cl in CLAUSES1) for k in (1, 2)}
    _K7[key] = out
    return out


def compute(light=False):
    k = kept()
    rt = route()
    o = dict(k=k, f=faces(), rt=rt, rg=regular(k), oi=order_index(rt))
    if not light:
        o["cq"] = calc_question()                           # instruments that cite K1-K4 alone may skip it
    return o


def report(o):
    print("c1_oneway.py -- claim C1 re-posed on the one-way object (item 282)\n")
    k = o["k"]
    print("K1 localized_hole's own checks H1 %s, H2 %s, H3 %s, H6 %s; kappa = 1/r_h %s; F finite positive at r_h %s; "
          "pullback %s" % (k["checks"]["H1"], k["checks"]["H2"], k["checks"]["H3"], k["checks"]["H6"], k["kappa_ok"],
                           k["F_pos"], k["pullback"]))
    f = o["f"]
    print("K2 our face from V_open > 0: %s; position 2's face closes at V_s e^(-%.1f) < 0: %s -- V = 0 on neither" % (
        f["ours"], f["t_full"], f["theirs"]))
    rt = o["rt"]
    print("K3 edges %s; a direct join of the exteriors: %s; the route through the bounce: %s; from position 2's "
          "exterior: %s; crossing r_h/(1 + eps): %s" % (rt["edges"], rt["direct"], rt["chain"], rt["p2_back"],
                                                       rt["crossing"]))
    rg = o["rg"]
    print("K4 Kretschmann at the faces %s, falling with r: %s, far away %s" % (rg["at_face"], rg["falls"], rg["far"]))
    oi = o["oi"]
    print("K6 %d reachable pairs of 49, the upper triangle: %s (degenerate as an index: %s); %d routes of 343, from <= "
          "through <= to: %s" % (len(oi["pairs"]), oi["upper"], oi["pairs_degenerate"], len(oi["held"]), oi["chains"]))
    print("   E %s; degenerate %s; langclose %s, %d of 10 pairs agreeing; audit keys %s one-hot %s" % (
        oi["E"], oi["degenerate"], oi["langclose"], oi["agreeing"], oi["audit"]["keys"], oi["audit"]["onehot"]))
    if "cq" in o:
        cq = o["cq"]
        print("K7 C1's varying clauses by interior: %s; the continuation's own clauses (NEC holds, README-only): %s" % (
            cq["vals"], cq["own"]))
        for k in (1, 2, 3, 4):
            print("K7 order %d, own code: %s (lawful %s)%s" % (k, cq["ownrun"][k][0], cq["ownrun"][k][1],
                                                            "; all 24 codes %s" % dict(cq["all"][k]) if k > 1 else ""))
        print("K7 the channel reading at order 4: own %s; all 24 %s; control %s" % (cq["rule"], dict(cq["allrule"]),
                                                                                  cq["control"]))
        print("K7 the continuation alone, orders 1-2: %s" % cq["alone"])


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("K0 M's item-282 words verbatim in the rulings file", M282 in rul)
    k = o["k"]
    add("K1 C1's outside-the-hole figures hold (localized_hole H1, H2, H3, H6; the horizon's chart: kappa = 1/r_h, F "
        "finite and positive, the pullback)", all(k["checks"].values()) and k["kappa_ok"] and k["F_pos"] and k["pullback"])
    f = o["f"]
    add("K2 our face begins at V_open > 0 and position 2's closes at V_s e^(-33.6) < 0: V = 0 is on neither face",
        f["ours"] and f["theirs"] and "%.1f" % f["t_full"] == "33.6")
    rt = o["rt"]
    add("K3 no chart joins the exteriors; the README's route runs through the bounce; nothing returns from position 2's "
        "exterior; each part crosses in at most a clock", not rt["direct"] and rt["chain"] and
        rt["p2_back"] == ["position 2's exterior"] and rt["crossing"])
    rg = o["rg"]
    ok = sp.simplify(rg["at_face"] - 72 / k["rh"] ** 4) == 0 and rg["falls"] and rg["far"] == 0
    add("K4 curvature finite on both exteriors and faces (72/r_h^4 at most, at the faces), its divergence only inside, "
        "where the quantum region stands", ok)
    oi = o["oi"]
    ok = oi["upper"] and len(oi["pairs"]) == 28 and oi["pairs_degenerate"] and oi["chains"] and len(oi["held"]) == 84
    ok &= [oi["E"][L] for L in FIVE] == [0] * 5 and oi["langclose"] and oi["agreeing"] == 10 and not oi["degenerate"]
    ok &= not oi["audit"]["keys"] and not oi["audit"]["onehot"]
    add("K6 the passage's causal order is the 28 pairs from <= to, none back; its 84 routes from <= through <= to; the "
        "five languages agree at E = 0, not degenerate, langclose holds, audit clean", ok)
    if "cq" not in o:
        return res
    cq = o["cq"]
    ok = cq["vals"] == {"B": {"singular": 1, "inner": 1, "quantum": 1, "shell": 0},
                        "K2": {"singular": 0, "inner": 1, "quantum": 1, "shell": 1},
                        "K34": {"singular": 0, "inner": 0, "quantum": 1, "shell": 1}}
    ok &= cq["ownrun"][2] == ((1, 1, 1), True) and cq["ownrun"][3] == ((1, 1, 1), True)
    ok &= cq["all"][3] == Counter({(1, 1, 1): 24}) and cq["all"][2] == Counter({(1, 1, 1): 22, (1, 1, "both"): 2})
    ok &= cq["alone"][1] == cq["alone"][2] == ("refused",) * 3
    add("K7 C1's question through the calculator, clause by clause in C4's settled form: (B), K2 and K3-K4 each 1 at "
        "orders 2 and 3, logic joining 1 -- C1 holds; lawful; the continuation alone refuses -- the quantum bounce's "
        "own other configurations decide", ok)
    ok = cq["ownrun"][4] == (("refused",) * 3, True) and cq["rule"] == (1, 1, 1)
    ok &= cq["allrule"] == Counter({(1, 1, 1): 24}) and all(g == t for g, t in cq["control"].values())
    add("K7 at order 4 the operator refuses all three, each a binary communication; the channel reading (302) gives 1, "
        "1, 1 under every code, and each interior as the question returns its own clauses", ok)
    return res


MUTANTS = {"opens_at_bifurcation": "our face opened at U = V = 0",
           "white_open_long": "position 2's face kept open for ever",
           "slice_route": "the eternal slice's join of the exteriors restored",
           "reverse_edge": "a way back from position 2's exterior to ours",
           "k7_no_population": "C1's question without tension and matter, the continuation alone (K7)",
           "k7_singular_opens": "the singular interior given a face in position 2 (K7)",
           "k7_channel_off": "the continuation bits held to the one-flip rule (K7)"}


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
        print("  mutant %-20s %-50s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
