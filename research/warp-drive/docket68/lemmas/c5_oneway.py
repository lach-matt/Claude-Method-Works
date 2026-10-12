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
     [Item 311 (U9): "as long again" holds through c4_residue R6's core with the Killing energy kept -- the continuation
     past the bounce is the incoming half's image under (T, t) -> (-T, 2 t_0 - t), an isometry; the face, for the
     README's parts on reading (i), joins the quantum region's form.]
  U2 (computed, exact; kept, hold_small L2) The capture radius for the plane's fields: photon sphere at sqrt2 r_h,
     critical impact parameter 2 r_h, cross-section 4 pi r_h^2 -- outside the hole, unchanged.
  U3 (estimate, kept; hold_small L3/L5 with the C5 verifier's figures) The hole radiates mainly into the plane's own
     fields, greybody 0.93, the bulk graviton 0.6% of the power; its life 3.2e-14 s, 8.57e14 clocks.  On the one-way
     object this emission is negative energy going in at our face and positive energy leaving from outside it --
     nothing exits the face (item 277's check), so it is not a reverse passage.
  U4 (computed; kept, hold_small L4 against write_small S3) The hold is the write: the hole outlives the write's floor,
     66,980 clocks, 1.28e10-fold (i_oneway I5: 3.9e-11 of E lost over the floor), on reading (i) of items 264 and 267.
     [Item 312 (U10): on the object M's 162, 163, 273 and 282 (2) describe -- the README all in when the faces begin, at
     the fixed size -- this comparison stands with the hole's E the README's, not 2E: 1.28e10.  On reading (ii), which
     162 excludes, the binding margin would be the growing hole's 4.8 at the Planck-size seed (estimate).]
  U5 (deduced) The C5 verifier's qualification (5), "the most serious" -- the lifetime is an evaporating,
     collapse-formed hole's with no second exterior, while the eternal hole carrying the bridge loses no mass, so L1's
     bridge and L3/L4's life described different spacetimes -- resolves on the one-way object: it opens (270 (c)), so
     it is formed and evaporates, and the same formed hole carries the passage, through its interior and the bounce,
     with no second exterior of the eternal kind.  The lifetime and the passage now describe one spacetime.
     [Item 311 (U9): one spacetime stands for formation and evaporation; on reading (i) the passage of the README's
     parts through position 2's face is conditional on the quantum region reversing their Killing energy.]
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
     E~ != 0, and for the README on b_bounce Q5's reading, it is the core's scale, not computed.  The check pins it.]
     [Item 311 (U9), computed: in the core Tdot^2 = 1 + E~^2/G + L^2/R^2 >= 1 (G > 0), so no timelike route crosses
     it in more proper time than the E~ = 0 observer -- 1.6e-7 per half bounds them all.]
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
     [Item 311 (U9): leaving as its own image is the README on reading (ii), one whole body that collapses and
     bounces; on reading (i), where U4's margin holds, its parts are bodies crossing the core of a hole already
     standing, and through a t-independent core they leave toward the far side.]
     (6) The bounce as constructed: R6's metric, NEC negative at the bounce, paired per ray by the README (b_bounce
     Q5, 183), its T-lines geodesics -- C4's residue (6), read here, not rebuilt.
  U9 (item 311; computed where marked, deduced where marked) C5 against C4's verification (item 310), each finding put
     to U0-U8 because M asked that C5 be shown unchanged.
     Unchanged (deduced): (3) C5 reads no mass of position 2's; (4) U7 is the entered rows read back, as its (i) says;
     (5) and (8) bear on clauses C5 does not carry (the vacuum, the brane's analyticity); (6) U2-U4's inner horizon 0
     holds for spin as for charge, a Myers-Perry exterior being vacuum but not Tangherlini; (7) C5 uses no tau; (9) the
     scalar's greybody 1.003 lifts the all-species maximum to 1.000112 (each factor at the larger of 1 and its own), so
     U8 (3)'s 1.19e10 is 1.1890e10 against 1.1891e10, a change of 0.01% (computed); the two core-scale estimates both
     pair the README (U1's pairing; b_bounce Q5's note).
     Closed further (computed): (2) the core's crossing for every timelike route -- with p_t = -E~ and the angular
     momentum L conserved, Tdot^2 = 1 + E~^2/G + L^2/R^2 >= 1 where G > 0, so U8 (1)'s 1.6e-7 per half bounds every
     route, not the E~ = 0 one alone; and the half past the bounce is the incoming half's image under (T, t) -> (-T,
     2 t_0 - t), so "as long again" holds with the Killing energy kept (deduced from the isometry and uniqueness).
     Outside C4's claim (computed): G5 under the 2 : 1 bulk leaves every clock figure of C5 unchanged -- r_h is fixed by
     the README's bits in units of l5 (r_h/l5 = 72,762), so the life in clocks, 8.573e14, and its margin over the
     write's floor, 1.28e10, are functions of N alone; only the SI figures move, r_h and the life by (G5/G ell)^(1/3)
     and E by its inverse (1.282e-20 m, 3.667e-14 s, 1.119e9 J at (3/2) G ell; 8.89e-21 m, 2.542e-14 s, 1.614e9 J at
     G ell/2).
     Changed (deduced): item 310's (1) with the critic's scope.  U1, U4 and U5 hold the README as parts crossing a hole
     that stands open through the write -- each part in at most two clocks while the face is open at least 66,980
     (i_oneway I2, I5) -- on reading (i), the hole standing at its size through the write, the one reading U4's margin
     is verified on (264 (1)).  Those parts are bodies crossing the core of a hole already standing, which (1) is about.
     The critic's scope -- the README as the matter that collapses and bounces, leaving as its own image (b_bounce Q5,
     d_evap D1) -- is reading (ii)'s, where the README is one whole body (163) and the hold runs from formation to the
     bounce, so U4's verified comparison is not the one that applies (264 (1); b_bounce's "does not show").  So the face
     the record names and the margin U4 verifies rest on different readings.  Through R6's t-independent core each
     part on reading (i) keeps its Killing energy and moves past the bounce toward the far side of the white-hole
     interior, where t runs to -infinity (c4_residue R13: under Q1 the image of the second exterior's side) -- away
     from position 2's face as named.  On the one-way object, whose faces begin at the opening (270 (c)) and which has
     no eternal second exterior (282), that side is Q1's image of what opened the hole, not an exterior.  A part
     reaches position 2's face only if the quantum region reverses its Killing energy against the continued d_t,
     as Haggard and Rovelli's region does for the collapsing matter; for matter crossing a hole already standing nothing
     in the record, or in the literature read here, constructs that.  So U1's "as long again" stands, and its face, for
     the README's parts on reading (i), joins the quantum region's form among what the board cannot close; U5's one
     spacetime stands for formation and evaporation, the parts' passage conditional in the same way.  The cypher on it,
     stated: over (the part forms the hole, the core reverses the Killing energy) the answer is the second coordinate
     itself -- index_audit flags the pair one-hot -- so 211 voids any verdict, and none is taken.
     So C5 has changed in one place: on reading (i), where U4's margin holds, the face by which the README's parts
     emerge is conditional on the quantum region's form; on reading (ii), where the README leaves as its own image by
     the face named, U4's verified comparison does not apply.  Every figure and U7's result stand.
     [Item 312 (U10): the change found here is reading (i)'s, a hole standing before the README is in, which M's 273
     ("README only") and 282 (2) ("no horizons" before the opening) exclude; reading (ii), the hole growing as the README
     comes in, M's 162 excludes ("the throat doesn't change size").  On the object those rulings leave -- the README all
     in when the faces begin, at the fixed size -- nothing of the README crosses a hole already standing, and C5 stands
     on C4's condition alone (U10).]
  U10 (item 312; computed where marked, deduced where marked, estimates marked) U9's change worked against M's rulings.
     The readings of where the write sits (o3_write W4): (i) inside a static hold -- a hole of E standing while the
     README of E arrives (264 (1)'s open 2E question); (ii) the write is the opening -- the README forms the hole as it
     arrives, the size growing (ingoing Vaidya; 198, M's guess: "the size growing as it comes in ... and fixed once the
     whole README is in").  Against M's rulings (deduced): 273 chose the object whose option text reads "README only",
     and 282 (2) chose "Before the opening the positions are joined through the bulk with no horizons; the corridor's
     faces begin at the opening" -- so no hole stands before the README is in, and none of E that is not the README's:
     reading (i) is excluded, its 2E question answered against it.  162 rules "The throat doesn't change size because
     the whole chain object only every takes on the size that contains the README upon opening" (H-FIXED-SIZE; the
     record's reading there, "any ramp of m(v) give[s] way") -- so reading (ii)'s growing hole is excluded too, 198
     being a guess.  What the rulings leave, the board's reading: the README carried in by the inflow (115 (c)) with no horizon, and the faces beginning
     at the opening at the size that holds it, the README within -- held "once and at once", as one whole (162, 163).
     The face (computed; the board's reading where marked).  On that object the README is the whole of the hole's
     collapsing matter, enclosed at the opening, and in Haggard and Rovelli's construction the collapse is glued to its
     image: each part of the README, entering our face at V = V0 > 0, leaves as its own image, which under b_bounce
     Q1's map is V' = -V0 and meets U' = 0 at V' < 0 -- position 2's face as named, onto Q1's image of our exterior --
     for every V0.  They construct it for a thin null shell (b_interior B4, READ); carried to the README as a whole,
     the board's reading.  Nothing of the README crosses a hole already standing, so item 310's (1) bears on nothing of
     it; the face rests on a quantum region of that kind -- C4's condition (c4_residue R13) -- and on nothing further.
     The hold (U4).  The hole's E is the README's (273), so U4's comparison stands as verified, with E and not 2E: the
     hole, open at its size from the opening, outlives the write's floor 1.28e10-fold; each part of the README crosses
     in at most two of its own clocks while the face stands open (i_oneway I2, I5), the parts entering together.
     Reading (ii) for the record, M's guess against M's ruling (computed; estimates marked).  Were the hole to grow as
     the write feeds it, at E/t_w, evaporating at P(E)/f with the fraction f of E (5D: E ~ r_h^2, P ~ r_h^-2; species
     and greybody as hold_small's; P(E) = E/(2 life)), the feed would outrun the evaporation above f* = t_w/(2 life) =
     3.91e-11 (t_w the floor).  The smallest semiclassical hole, r_h = l5, holds f_P = (l5/r_h)^2 = 1.89e-10 -- 4.8 f* --
     so the hole would only grow from there, the margin rising to 2.6e10 at full size, the README radiating f*
     ln(1/f_P) = 8.7e-10 of E over the write (estimates: a uniform feed; g* = 106.75 and greybody 0.93 held at the
     seed's 2.0e8 GeV, 72,762 times the completed hole's temperature); the margin would close for a write past 4.8
     floors or species at 2.0e8 GeV above 4.8 times the Standard Model's (H-SPECIES-FINITE).
     So C5, on the object M's rulings describe, has not changed beyond C4's own condition: the face rests on a quantum
     region of Haggard and Rovelli's kind, as C4's does, the hold's margin is U4's 1.28e10, and every figure and U7's
     result stand.  U9's change belongs to reading (i), which the rulings exclude.  The cypher NOT-RUN on the choice
     of reading, stated: M's 162, 273 and 282 (2) decide it, read and deduced, not a configuration among others.

What this does not show.
  - The quantum region's duration and the order-one coefficient of any bounce time (b_bounce Q3 is the two-way
    object's; item 277).  [item 309: U8 (1) gives the core's crossing on c4_residue R6's effective metric, 1.6e-7 of a
    clock, an estimate; its order-one coefficient and the region's quantum-gravitational form stay open.]
  - That a small brane hole at r_h/l = 8e-16 exists as a static solution: the literature's (item 261), as for C4.
  - Verification: U7-U8 wait for M's finalization and a verifier after C4's (249).
  - [Item 310, outside the C4 claim, its verifier's] G5 under the 2 : 1 bulk (tau_share T4's note): G5 = (3/2) G ell
    over both sides, or G ell/2 over ours alone, not G ell -- an O(1) change in r_h and in the life and margins here.
    [Item 311: computed in U9 -- the clock figures and the margins are unchanged; only r_h, the life in seconds and E
    move, by (G5/G ell)^(+-1/3).]
  - [Item 311] Which face the README's parts emerge by on reading (i), where U4's margin holds (U9): the quantum
    region's form.  [Item 312: reading (i) is excluded by M's 273 and 282 (2) (U10).]
  - [Item 312] Haggard and Rovelli's gluing for the README as a whole rather than a thin shell (U10, the board's
    reading); the reading of where the write sits, read from M's 162, 163, 273 and 282 (2), the board's (U10).
  - Species beyond the Standard Model (H-SPECIES-FINITE), as in hold_small.

Imports hold_small.py, i_oneway.py, c1_oneway.py, c4_oneway.py, c4_residue.py, calculator.py, b_interior.py,
index_audit.py and hlaw.py by path.  Stdlib + sympy.  python3 c5_oneway.py [--selftest |
--mutants]
"""
import contextlib
import importlib.util
import itertools
import math
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
C5VALS = {"U1": {"singular": 0, "inner": 0, "quantum": 1, "shell": 1},     # the route to position 2 (c1_oneway K34)
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


def against_c4():
    """U9 (item 311): C5 put against C4's verification (item 310)"""
    H = _load("hold_small.py", "c5o_hs3")
    PG = _load("p2_gravity.py", "c5o_pg")
    WS = _load("write_small.py", "c5o_ws")
    l5c = H.l5_checks()
    gam, bulk = l5c["gamma_eff"], l5c["bulk"]
    G, c, hb, kB, sSB = PG.G, PG.C, PG.HBAR, 1.380649e-23, 5.670374419e-8
    wc = WS.head_clocks()
    g5, rh0 = {}, None
    for g in (1, 1.5, 0.5):              # G5 over G ell: ours; both sides of the 2 : 1 bulk; our side alone (item 310)
        G5 = g * G * PG.ELL_MAX
        l5 = (hb * G5 / c ** 3) ** (1 / 3)
        rh = (2 * H.N_EX * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
        if MUT.get("u9_rh_in_metres"):
            rh0 = rh0 or rh
            rh = rh0                     # the mutant: r_h held in metres, not fixed by the README's bits
        E = 3 * math.pi * c ** 4 * rh ** 2 / (8 * G5)
        T = hb * c / (2 * math.pi * kB * rh)
        P = (H.G_STAR / 2) * sSB * 4 * (4 * math.pi * rh ** 2) * T ** 4
        life = E / (2 * P) / (gam * (1 + bulk))
        g5[g] = dict(rh=rh, E=E, life=life, clocks=life / (rh / c), over=life / (wc * rh / c), rl5=rh / l5)
    Gs, Rs, Es, Ls, X = sp.symbols("G R E L X", positive=True)
    td2 = sp.solve(sp.Eq(-X + Gs * (Es / Gs) ** 2 + Rs ** 2 * (Ls / Rs ** 2) ** 2, -1), X)[0]
    bound = sp.simplify(td2 - 1 - Es ** 2 / Gs - Ls ** 2 / Rs ** 2) == 0     # Tdot^2 - 1 = E~^2/G + L^2/R^2 >= 0
    r13 = _load("c4_residue.py", "c5o_cr3").r13()
    later = r13["Q1"]["exit"]            # a part crossing R6's t-independent core: toward the image of 'III''s side
    forming = r13["Q1"]["mirror_exit"]   # the part that forms the hole, leaving as its own image: the image of ours
    if MUT.get("u9_parts_as_image"):
        later = forming                  # the mutant: the critic's scope stretched to every part
    au = _load("index_audit.py", "c5o_ia3").audit_index(["forms", "reverses", "named_face"],
                                                         [(f, r, r) for f in (0, 1) for r in (0, 1)])
    return dict(g5=g5, bound=bound, later=later, forming=forming, audit=au)


def reading_two():
    """U10 (item 312): the README's image on the object M's rulings leave; reading (ii)'s growing hole, for the record"""
    H = _load("hold_small.py", "c5o_hs4")
    WS = _load("write_small.py", "c5o_ws2")
    l5c = H.l5_checks()
    life, tw = l5c["life_clocks"], WS.head_clocks()
    if MUT.get("u10_slow_write"):
        tw = 10 * tw                     # the mutant: a write ten floors long
    fstar = tw / (2 * life)              # the feed E/t_w meets the evaporation P(E)/f, P(E) = E/(2 life), at f*
    rl5 = (2 * H.N_EX * math.log(2) / math.pi ** 2) ** (1 / 3)
    fP = rl5 ** -2                       # the smallest semiclassical hole, r_h = l5
    # each ingoing shell V = V0 > 0 of the README, near our face (U = eps), and its image under the gluing map
    V0, eps = sp.symbols("V0 eps", positive=True)
    m = (lambda u, v: (-v, -u)) if MUT.get("u10_time_reflection") else (lambda u, v: (-u, -v))
    a, b = m(eps, V0)
    face = None
    if sp.limit(a, eps, 0) == 0 and bool(b < 0):
        face = "U'=0, V'<0"              # position 2's face as named, onto Q1's image of our exterior
    elif sp.limit(b, eps, 0) == 0 and bool(a < 0):
        face = "V'=0, U'<0"
    return dict(fstar=fstar, fP=fP, ratio=fP / fstar, full=1 / fstar, radiated=fstar * math.log(1 / fP),
                seed_T=rl5, longest=fP / fstar, face=face)


def compute():
    h = hold()
    return dict(h=h, x=crossing_agrees(h), rt=route(), cq=calc_question(), rs=residue(), ag=against_c4(),
                r2=reading_two())


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
    _report_u9(o)
    _report_u10(o)
    rs = o["rs"]
    print("U8 the core crossed in %.2g clocks; the passage at most %.7f clocks; the hold over the floor %.3g-fold -- "
          "%.3g with every greybody 1; species could multiply %.3g-fold before the floor is reached" % (
              rs["core"], rs["passage_max"], rs["over"], rs["greybody_over"], rs["species_factor"]))


def _report_u9(o):
    ag = o["ag"]
    for g, v in ag["g5"].items():
        print("U9 G5 = %.1f G ell: r_h %.4g m, E %.4g J, life %.4g s = %.4g clocks, over the floor %.3g, r_h/l5 %.0f" % (
            g, v["rh"], v["E"], v["life"], v["clocks"], v["over"], v["rl5"]))
    print("U9 Tdot^2 = 1 + E~^2/G + L^2/R^2 in the core: %s; a later part through R6's core leaves toward the image of "
          "%s, the README as its own image (reading (ii)) onto the image of %s; audit %s" % (ag["bound"], ag["later"],
                                                                                   ag["forming"], ag["audit"]))


def _report_u10(o):
    r2 = o["r2"]
    print("U10 the README's image leaves by %s; reading (ii) for the record: the feed outruns the evaporation above "
          "f* = %.3g of E; the smallest semiclassical hole holds %.3g, %.2f f*; %.2g at full size; %.2g of E radiated "
          "over the write; the seed %.0f times the completed hole's temperature" % (
              r2["face"], r2["fstar"], r2["fP"], r2["ratio"], r2["full"], r2["radiated"], r2["seed_T"]))


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
    ag = o["ag"]
    g5 = ag["g5"]
    ok = all("%.4g" % v["clocks"] == "8.573e+14" and "%.3g" % v["over"] == "1.28e+10" and "%.0f" % v["rl5"] == "72762"
             for v in g5.values())
    ok &= abs(g5[1.5]["rh"] / g5[1]["rh"] - 1.5 ** (1 / 3)) < 1e-12
    ok &= abs(g5[0.5]["E"] / g5[1]["E"] - 2 ** (1 / 3)) < 1e-12
    ok &= ag["bound"] and ag["later"] == "III" and ag["forming"] == "I"
    ok &= ("reverses", "named_face") in ag["audit"]["onehot"]
    add("U9 C5 against C4's verification (item 311): the clock figures unchanged under the 2 : 1 bulk's G5, the SI ones "
        "moving by the cube root; every timelike route crosses the core within the E~ = 0 time; a part crossing a "
        "standing hole leaves R6's core toward the far side, the README as its own image by position 2's face; the "
        "face a function of the core's form alone (one-hot, 211)", ok)
    r2 = o["r2"]
    add("U10 on the object M's rulings leave every part of the README leaves as its own image by U' = 0, V' < 0; and on "
        "reading (ii), for the record, the feed would outrun the evaporation from the smallest semiclassical hole by "
        "4.8 (f* 3.91e-11, f_P 1.89e-10), 2.6e10 at full size, 8.7e-10 of E radiated (item 312)",
        r2["face"] == "U'=0, V'<0" and "%.3g" % r2["fstar"] == "3.91e-11" and "%.3g" % r2["fP"] == "1.89e-10"
        and "%.2g" % r2["ratio"] == "4.8" and r2["ratio"] > 1 and "%.2g" % r2["full"] == "2.6e+10"
        and "%.2g" % r2["radiated"] == "8.7e-10")
    return res


MUTANTS = {"eternal": "the hole read as eternal, losing no mass",
           "slice_passage": "the passage restored to the slice's join of the exteriors",
           "u7_no_population": "C5's question without tension and matter, the continuation alone (U7)",
           "u7_inner_outside_kept": "the inner horizon's exterior read as Tangherlini (U7)",
           "u8_no_margin": "a hold shorter than the write's floor (U8)",
           "u9_rh_in_metres": "r_h held in metres while G5 changes, not fixed by the README's bits (U9)",
           "u9_parts_as_image": "every part of the README read as leaving by its own image through R6's core (U9)",
           "u10_slow_write": "a write ten floors long (U10)",
           "u10_time_reflection": "the README's image taken under the time reflection, not Q1 (U10)"}


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
