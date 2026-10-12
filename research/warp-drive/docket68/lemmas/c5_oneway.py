#!/usr/bin/env python3
"""c5_oneway.py -- item 282: claim C5 (O1b/O1c at the small end, and the hold against the hole's temperature)
re-posed on the glued one-way object.  C5 as verified (hold_small.py, items 262, 267) is kept as written with its
item-281 note; this is its one-way form, after C1's and C4's.  Worked in the conversation (computed with sympy, exact
where marked; READ where marked through the instruments imported; deduced where marked; not verified by a separate
session; not seated); 2026-10-12.

  U0 (read) M's item-282 words, verbatim in the rulings file.
  U1 (computed, exact; hold_small L5, i_oneway I2) L1 re-posed: the passage is the README's route on the object --
     our black-hole face, our future interior, the bounce, position 2's past interior and white-hole face
     (c1_oneway K3) -- not a crossing "as information across the bridge's slice".  Any radial fall from the horizon
     reaches the quantum region in r_h/(c (1 + E~)) of proper time, E~ the specific energy -- at most one clock --
     hold_small's own tau and i_oneway's closed form agreeing; the README emerges through position 2's interior in as
     long again.  The interior's r = 0, admitted by item 259 as the classical interior outside the passage, is where
     the bounce's quantum region stands (273): the passage runs through it, paired per ray by the README (b_bounce Q5).
  U2 (computed, exact; kept, hold_small L2) The capture radius for the plane's fields: photon sphere at sqrt2 r_h,
     critical impact parameter 2 r_h, cross-section 4 pi r_h^2 -- outside the hole, unchanged.
  U3 (estimate, kept; hold_small L3/L5 with the C5 verifier's figures) The hole radiates mainly into the plane's own
     fields, greybody 0.93, the bulk graviton 0.6% of the power; its life 3.2e-14 s, 8.57e14 clocks.  On the one-way
     object this emission is negative energy going in at our face and positive energy leaving from outside it --
     nothing exits the face (item 277's check), so it is not a reverse passage.
  U4 (computed; kept, hold_small L4 against write_small S3) The hold is the write: the hole outlives the write's floor,
     66,980 clocks, 1.28e10-fold (i_oneway I5: 3.9e-11 of E lost over the floor), on reading (i) of items 264 and 267.
  U5 (deduced) The C5 verifier's qualification (5), "the most serious" -- the lifetime is an evaporating,
     collapse-formed hole's with no second exterior, while the eternal hole carrying the bridge loses no mass, so L1's
     bridge and L3/L4's life described different spacetimes -- resolves on the one-way object: it opens (270 (c)), so
     it is formed and evaporates, and the same formed hole carries the passage, through its interior and the bounce,
     with no second exterior of the eternal kind.  The lifetime and the passage now describe one spacetime.
  U6 (the cypher NOT-RUN, stated) U1-U5 re-post a construction and its figures; the object's causal order is
     c1_oneway K6's run.  [item 309: U7 puts C5's question through the calculator; U6 stands for U1-U5 as built.]
  U7 (computed; item 309) C5's question through the calculator, in the form C4's question stands in (c4_residue
     R12): clause by clause, one condition over the four interiors, tension and matter at statistics' rank over the
     population (F18; 292, 295), the question cell the quantum bounce's row at C4's (t, m).  The clauses' rows are
     read from b_interior's cells, not set by hand: U1 (the route through to position 2) and U5 (one spacetime --
     formed, evaporating, passing) are B6's complete, regular route, c1_oneway K34's row (singular 0, inner 0,
     quantum 1, shell 1); U2-U4 (capture, emission and life, that life against the floor) are computed outside the
     hole and hold where the exterior is Tangherlini -- every interior but the inner horizon, whose charge or spin
     (B3) changes it (the C1 verifier's qualification (5)): singular 1, inner 0, quantum 1, shell 1.  Result: each of
     U1-U5 is 1 at orders 2 and 3, the lawful orders, under all 96 codings (24 orderings x 4 orientations); 211's audit
     flags no key and no one-hot on any clause.  Control: the continuation alone, without tension and matter, is
     refused on every clause at both orders, and the audit flags every clause -- the population is what the admission
     rests on, as in C4.  Two qualifications, stated: (i) the answer is read back from the quantum bounce's own rows
     at the other tensions and matters -- the calculator says C5's clauses do not turn on tension or matter once the
     interior is fixed, which is the content; (ii) the answer at the bounce does not depend on the inner horizon's
     row -- the mutant that reads the inner horizon's exterior as Tangherlini returns the same 96/96, and is caught
     only by the rows' read from b_interior.  The five clauses carry two distinct rows (U1 = U5, U2 = U3 = U4).
     U7 rests on R12's form; the verdict of C4's verifier on that form carries to U7.
     [Item 310: it did -- by the C4 verifier's (4), in R12's form each clause is the entered value read back, the
     agreement adding nothing to its inputs; here those are b_interior's rows and the population's constancy, as (i)
     and (ii) say.]
  U8 (computed, with the estimates marked; item 309) C5's residue, listed and closed as C4's was.
     (1) The core: c4_residue R6's effective bounce metric, ds^2 = -dT^2 + (r_h^2/R^2 - 1) dt^2 + R(T)^2 dOmega_3^2,
     vacuum where R'^2 = r_h^2/R^2 - 1, the core at (r_h l5^2)^(1/3) (estimate) -- crossed in 1.6e-7 of a clock along
     the T-geodesics, so the passage takes at most 2 clocks plus that, 2.0000002: in, through, out.  The order-one
     coefficient of the core's size is not shown.
     [Item 310, the C4 verifier's (2): the T-geodesics are the E~ = 0 family, from bifurcation sphere to bifurcation
     sphere (282 drops it); 1.6e-7 is that observer's proper time over Tangherlini's r_q to 0, r_q an estimate.  For
     E~ != 0, and for the README on b_bounce Q5's reading, it is the core's scale, not computed.  The check now pins it.]
     (2) Species: the life goes as 1/(degrees of freedom), so the hold's 1.28e10 margin over the write's floor admits a
     1.28e10-fold multiplication of the radiated species before the floor is reached (estimate; H-SPECIES-FINITE).
     (3) Greybody: with every greybody factor set to 1, the most the hole can radiate, the margin is 1.19e10.
     [Item 310, the C4 verifier's (9): greybody 1 is not strictly the most -- the scalar's factor is 1.003 -- a change
     under 1%; the margin stands at 1.19e10 to that.]
     (4) The inner horizon: U2-U4's figures hold for the singular interior, the bounce and the shell, not the inner
     horizon (U7's rows) -- the C1 verifier's (5), carried.
     (5) The crossing: the passage is the README's route through the interior and the bounce (U1), not information
     across the bridge's slice; the slice's join is the mutant slice_passage.
     [Item 310 (c4_residue R13): a body crossing a t-independent core leaves the white hole opposite the gluing map's
     image of our face; the README, on b_bounce Q5's reading the matter that bounces, leaves as its own image by
     position 2's face as named, through a quantum region of Haggard and Rovelli's kind, not modeled here.]
     (6) The bounce as constructed: R6's metric, NEC negative at the bounce, paired per ray by the README (b_bounce
     Q5, 183), its T-lines geodesics -- C4's residue (6), read here, not rebuilt.

What this does not show.
  - The quantum region's duration and the order-one coefficient of any bounce time (b_bounce Q3 is the two-way
    object's; item 277).  [item 309: U8 (1) gives the core's crossing on c4_residue R6's effective metric, 1.6e-7 of a
    clock, an estimate; its order-one coefficient and the region's quantum-gravitational form stay open.]
  - That a small brane hole at r_h/l = 8e-16 exists as a static solution: the literature's (item 261), as for C4.
  - Verification: U7-U8 wait for M's finalization and a verifier after C4's (249).
  - [Item 310, outside the C4 claim, its verifier's] G5 under the 2 : 1 bulk (tau_share T4's note): G5 = (3/2) G ell
    over both sides, or G ell/2 over ours alone, not G ell -- an O(1) change in r_h and in the life and margins here.
  - Species beyond the Standard Model (H-SPECIES-FINITE), as in hold_small.

Imports hold_small.py, i_oneway.py, c1_oneway.py, c4_oneway.py, c4_residue.py, calculator.py, b_interior.py,
index_audit.py and hlaw.py by path.  Stdlib + sympy.  python3 c5_oneway.py [--selftest |
--mutants]
"""
import contextlib
import importlib.util
import itertools
from collections import Counter
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
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


def hold():
    H = _load("hold_small.py", "c5o_hold")
    o = H.compute()
    res = {n.split()[0]: ok for n, ok in H.checks(o)}
    l5 = H.l5_checks()
    tau = l5["tau"]
    rh, Et = sorted(tau.free_symbols, key=str)[::-1] if len(tau.free_symbols) == 2 else (None, None)
    life_clocks = l5["life_clocks"]
    if MUT.get("eternal"):
        life_clocks = float("inf")                         # the mutant reads the hole as eternal, losing no mass
    return dict(checks=res, tau=tau, life=l5["life"], life_clocks=life_clocks, over=life_clocks / 66980)


def crossing_agrees(h):
    IO = _load("i_oneway.py", "c5o_io")
    cr = IO.crossing()
    syms = {s.name: s for s in h["tau"].free_symbols}
    rh, Et = syms.get("r_h"), syms.get("E_t")
    eps = sp.Symbol("epsilon", nonnegative=True)
    rh2 = sp.Symbol("r_h", positive=True)
    same = sp.simplify(h["tau"].subs({rh: rh2, Et: eps}) - rh2 / (1 + eps)) == 0 if rh is not None else False
    return dict(same=same, closed=cr["closed"])


def route():
    C1 = _load("c1_oneway.py", "c5o_c1")
    if MUT.get("slice_passage"):
        C1.MUT["slice_route"] = True                       # the mutant restores the slice's join of the exteriors
    res = {n.split()[0]: ok for n, ok in C1.checks(C1.compute(light=True))}
    C1.MUT.clear()
    return dict(K3=res["K3"], K4=res["K4"])


INTERIORS = ("singular", "inner", "quantum", "shell")
# C5's clauses that vary across the configurations, by interior (b_interior's cells; the inner horizon's charge or spin,
# B3, changes the exterior every outside figure of C5 is computed for -- the C1 verifier's qualification (5))
C5VALS = {"U1": {"singular": 0, "inner": 0, "quantum": 1, "shell": 1},     # the route through to position 2 (c1_oneway K34)
          "U2": {"singular": 1, "inner": 0, "quantum": 1, "shell": 1},     # capture: Tangherlini's photon sphere
          "U3": {"singular": 1, "inner": 0, "quantum": 1, "shell": 1},     # emission and life of a neutral 5D hole
          "U4": {"singular": 1, "inner": 0, "quantum": 1, "shell": 1},     # that life against the write's floor
          "U5": {"singular": 0, "inner": 0, "quantum": 1, "shell": 1}}     # one spacetime: formed, evaporating, passing
F18 = {(1, 1): {1}, (1, 0): {0, 1}, (0, 1): {1}, (0, 0): {0, 1}}
_U7 = {}


def calc_question():
    """U7: C5's question through the calculator, in the form C4's question stands in (c4_residue R12)"""
    key = tuple(sorted(k for k in MUT if k.startswith("u7_")))
    if key in _U7:
        return _U7[key]
    C4 = _load("c4_oneway.py", "c5o_c4")
    CA = _load("calculator.py", "c5o_calc")
    HL = C4._load_path(os.path.join(os.path.dirname(D68), "hlaw.py"), "c5o_hl")
    IA = _load("index_audit.py", "c5o_ia")
    BI = _load("b_interior.py", "c5o_bi")
    cells = BI.cells()
    keys = {"singular": (0, "none", "ours"), "inner": (1, "none", "pos2"), "quantum": (0, "quantum", "pos2"),
            "shell": (0, "shell", "pos2")}
    route_ = {k: cells[keys[k]]["complete"] for k in INTERIORS}          # B6: a complete, regular route (c1_oneway K34)
    outside = {k: 1 - keys[k][0] for k in INTERIORS}                     # B3: no inner horizon, the exterior Tangherlini
    vals = {"U1": dict(route_), "U2": dict(outside), "U3": dict(outside), "U4": dict(outside), "U5": dict(route_)}
    if MUT.get("u7_inner_outside_kept"):
        for c in ("U2", "U3", "U4"):
            vals[c]["inner"] = 1                           # the mutant: the inner horizon's exterior read as Tangherlini
    pop = not MUT.get("u7_no_population")
    out, audit = {}, {}
    for k in (2, 3):
        res = Counter()
        for perm in itertools.permutations(range(4)):
            kmap = dict(zip(INTERIORS, perm))
            for tf, mf in itertools.product((0, 1), repeat=2):
                tq, mq = 1 ^ tf, 1 ^ mf
                at = (kmap["quantum"], tq, mq) if pop else (kmap["quantum"],)
                names = ["K", "t", "m"] if pop else ["K"]
                views = dict(order=(0,), algebra=(0,), geometry=(0,), information=(0,),
                             statistics=(0, 1, 2) if pop else (0,))
                ans = []
                for cl in C5VALS:
                    kn = []
                    for kk in INTERIORS:
                        for (t, m) in (F18 if pop else [(1, 1)]):
                            tt, mm = t ^ tf, m ^ mf
                            if (kk, tt, mm) == ("quantum", tq, mq):
                                continue
                            kn.append(((kmap[kk], tt, mm) if pop else (kmap[kk],)) + (vals[cl][kk],))
                    ans.append(C4._staged(CA, HL, names + [cl], kn, at, views, k)["answer"])
                    if k == 2 and perm == (0, 1, 2, 3) and (tf, mf) == (0, 0):
                        a = IA.audit_index(names + [cl], kn)
                        audit[cl] = bool(a["keys"] or a["onehot"])
                res[tuple(ans)] += 1
        out[k] = res
    _U7[key] = dict(out=out, audit=audit, vals=vals)
    return _U7[key]


def residue():
    """U8: C5's residue -- the passage's time through the core, the species and greybody margins of the hold"""
    H = _load("hold_small.py", "c5o_hs2")
    l5 = H.l5_checks()
    CR = _load("c4_residue.py", "c5o_cr")
    core = CR.r6()["core_clocks"]
    over = l5["over_floor"]
    g = l5["gamma_eff"]
    if MUT.get("u8_no_margin"):
        over = 0.5                                          # the mutant: a hold shorter than the floor
    return dict(core=core, passage_max=2 + core, over=over, species_factor=over, greybody_over=over * g,
                gamma=g, dof=l5["dof"])


def compute():
    h = hold()
    return dict(h=h, x=crossing_agrees(h), rt=route(), cq=calc_question(), rs=residue())


def report(o):
    h = o["h"]
    print("c5_oneway.py -- claim C5 re-posed on the one-way object (item 282)\n")
    print("U1 hold_small's tau %s agrees with i_oneway's r_h/(1 + eps): %s; the route (c1_oneway K3): %s" % (
        h["tau"], o["x"]["same"], o["rt"]["K3"]))
    print("U2-U4 hold_small's own checks %s" % h["checks"])
    print("U3/U4 life %.3g s = %.3g clocks; the write's floor outlived %.3g-fold" % (h["life"], h["life_clocks"],
                                                                                    h["over"]))
    cq = o["cq"]
    print("U7 C5's clauses by interior %s" % C5VALS)
    for k in (2, 3):
        print("U7 order %d over 96 codings (24 orderings x 4 orientations): %s" % (k, dict(cq["out"][k])))
    print("U7 211's audit (keys or one-hot) per clause: %s" % cq["audit"])
    rs = o["rs"]
    print("U8 the core crossed in %.2g clocks; the passage at most %.7f clocks; the hold over the floor %.3g-fold -- "
          "%.3g with every greybody 1; species could multiply %.3g-fold before the floor is reached" % (
              rs["core"], rs["passage_max"], rs["over"], rs["greybody_over"], rs["species_factor"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("U0 M's item-282 words verbatim in the rulings file", M282 in rul)
    h = o["h"]
    add("U1 the fall to the quantum region takes r_h/(c (1 + E~)), hold_small and i_oneway agreeing; the passage is the "
        "route through the bounce (c1_oneway K3)", o["x"]["same"] and o["x"]["closed"] and o["rt"]["K3"])
    add("U2 the capture cross-section 4 pi r_h^2 (hold_small L2)", h["checks"].get("L2", False))
    ok = h["checks"].get("L3/L4", False) and h["checks"].get("L5", False) and "%.3g" % h["life_clocks"] == "8.57e+14"
    add("U3 the life 3.2e-14 s, 8.57e14 clocks, greybody 0.93, bulk 0.6% (hold_small L3/L5)", ok)
    add("U4 the hole outlives the write's floor 1.28e10-fold (hold_small L4)",
        h["checks"].get("L3/L4", False) and "%.3g" % h["over"] == "1.28e+10")
    add("U5 the object's regularity outside, where the life is computed (c1_oneway K4)", o["rt"]["K4"])
    cq = o["cq"]
    add("U7 C5's question through the calculator, clause by clause in C4's settled form: the clauses' rows read from "
        "b_interior's cells; U1-U5 each 1 at orders 2 and 3 under all 96 codings; no key or one-hot",
        cq["vals"] == C5VALS and all(cq["out"][k] == Counter({(1,) * 5: 96}) for k in (2, 3))
        and not any(cq["audit"].values()))
    rs = o["rs"]
    add("U8 the residue: the core crossed in 1.6e-7 of a clock (pinned, item 310), the passage under 2 clocks and that; "
        "the hold over the floor 1.28e10-fold, above 1.1e10 with every greybody 1", "%.2g" % rs["core"] == "1.6e-07"
        and rs["passage_max"] < 2.000001
        and "%.3g" % rs["over"] == "1.28e+10" and rs["greybody_over"] > 1.1e10 and rs["gamma"] < 1)
    return res


MUTANTS = {"eternal": "the hole read as eternal, losing no mass",
           "slice_passage": "the passage restored to the slice's join of the exteriors",
           "u7_no_population": "C5's question without tension and matter, the continuation alone (U7)",
           "u7_inner_outside_kept": "the inner horizon's exterior read as Tangherlini (U7)",
           "u8_no_margin": "a hold shorter than the write's floor (U8)"}


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
        print("  mutant %-14s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
