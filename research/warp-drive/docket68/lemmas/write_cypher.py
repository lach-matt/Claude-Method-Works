#!/usr/bin/env python3
"""write_cypher.py -- the chain input WRITE ("the static bulk held through the whole write, >= 2.0e5 clocks (OPEN;
R1-COVER pending)") and row O3 ("the corridor survives its hold, which lasts exactly as long as the write needs
(158 (2))"), put to the cypher (items 196, 158 (2)).  Computed and deduced from instruments already run; the cypher
CLASSIFIES, it derives nothing.  Not verified by a separate session; not seated; 2026-10-10.  Restated once on a
critic's finding: the negative-tension plane's keeps_Z had been entered 1 with no source; p2_full.py TS gives 0 by this
file's own coding rule, and statistics' refusal of WRITE moves from order 4 to order 3 (WZ, C1-C4 below).

WHAT IS ASKED.  Among the holds and bulks the board has computed, is there a bulk held through the whole write -- one
that carries the corridor, stands static, stays regular on the crossing's causal past for >= 2.0e5 clocks, keeps
seated clause (Z), in a configuration M's words leave standing -- or does any language admit one?  And for O3, the
same with the corridor's own linear survival over that hold in place of "static".

M'S WORDS (verbatim, rulings file; never paraphrased as M's).
  149 "I have given you everything I can. You have to work the math now"
  158 (2) "Exactly as long as the write needs  I should think" (typing kept; H-HOLD-AT-BOUND); 158 (3) "This question
      needs the math worked to answer it."
  160 "the corridor and the opening are the same object"
  161 "my inclination is yes" (an inclination, not a ruling: H-CORRIDOR-HOLDS)
  162 (excerpt) "The throat doesn't change size"
  163 M chose "All together, one whole"; the option's text, the board's, reads in part "the write lasts at least
      ~200,000 clocks; B4d must keep the fixed-size corridor regular for that long"
  166 M chose "Both planes at once" over "Yes, position 2's plane" and "No, ours" (to "Is the corridor's eq. (17) on
      position 2's plane?")
  172 (1) M chose "Yes, it may" (position 2's piece may carry the README's stress; the board's question said "stress
      that obeys the NEC")
  183 M chose "Yes: never violated as a pair"; 187 (3) M chose "Seat both": clause (Z) is seated in the board's
      wording, "\\"null energy never violated\\" holds net along each light ray (183)"
  184 "There are no matter free planes"
  195 "The README is not a pair"
  196 "All questions get works through the cypher" (excerpt, typing kept)
  198 "My guess would be 1." (a guess, not a ruling: the README forms the corridor as it comes in, size growing)
  200 (1) "1 - Once: k_R = k_L/2"
  203 "yes" (twice: the corridor is where the two planes' bulks meet; its energy is the README's E)

THE CELLS (every value from an instrument or note already run; U = not computed, a distinct code, never guessed).
  Coordinates: corridor (1 carries the corridor's crossable extremal throat; 0 not), static (1 held static through its
  hold; 0 changes), lasts (1 regular on the crossing's past for >= the write's floor; 0 not; U undecided or not
  computed), keeps_Z (1 no negative null energy on its rays -- a vacuum bulk whose planes carry no negative stress, or
  the NEC kept at every settled node; 0 broken pointwise -- at a settled node, or on every ray crossing a plane of
  negative pure tension (WZ) -- with net per light ray NOT computed (F5); U not computed), survives (1 linear
  survival of the horizon certified over its own hold; 0 a computed linear instability; U not certified / not
  computed), stands (1 no word of M's sets the configuration aside; 0 set aside, quoted), ell (0: ell <= 2m; 1: ell >=
  4m and the flat limit; a cell not computed at either is entered at both).
  No per-cell key coordinate (forming_rim.py F7: a key makes statistics return the table itself).

  W0 (computed, imported) the write's floor: o3_write.py W3, t_min(3) at the example README (Z = 108.75), 1.997e5
     clocks; sim2_passage.write_floor() gives the same.
  W1 (computed, imported; one figure READ from an owner's note) eq. (17)'s static bulk on one plane does not last:
     verified to 11.28 clocks, K >= 100 from 14.88 (b4_static.py S3, compute(live=False)), singular by ~18 (B4.md, the
     verifier's figure, o3_write.SINGULAR_CLOCKS); at ell = 2m ... m/4 its cone holds K >= 1e4 within 8-16 clocks
     (b4d_stage5.py check "F2/F3", READ from B4D-STAGE5.md F2's table: the instrument takes ~5 min and is not re-run);
     with no second sheet every layer to 1e10 K_bs is in J^-(P_c) within 389.3 clocks (sim2_passage.py X7, check C8,
     recomputed here by layer()).  Every one is below the floor by > 500x: lasts 0.
  W2 (computed, imported from the full run's pins) R1-COVER: every two-order hold is <= 88.74 clocks (r1_cover R2,
     max of hold2 over PIN_COLUMNS, at 100|1/2), floor/hold >= 2250 -- so R1's verdicts are verdicts for the whole
     write.  From PIN_VERDICTS and PIN_NECROWS through r1_cover's own nec_along/nec_code: the crossable rows that HOLD
     (lasts 1) are 12, all at ell >= 4m (the level surface at y* and at the band's midpoint, smooth near at y*), and
     EVERY one breaks the NEC pointwise at a settled node (keeps_Z 0); the 13 crossable rows that keep the NEC at every
     settled node (keeps_Z 1) never HOLD (12 UNDECIDED, among them the best member at 0.1 y_s at all nine ell; 1 FAILS).
  W3 (computed, imported; READ) the localized 5D hole is not the corridor: no 1/r tail, surface gravity 1/r_h (not
     extremal), r_h = 582 m against r0 = 2 m (b4d_stage1.py D2, tangherlini_slice, hole_radius); linearly stable
     against all tensorial types (Ishibashi-Kodama, READ in B4D-STAGE1.md): lasts 1, survives 1, corridor 0.
  W4 (computed, imported) Wall E over the write (bulk/stability.py's transport, D_derivatives, r_second, white_hole):
     the horizon is extremal (D' = 0); S4's exact rate changes the second derivative by T/4 = 4.99e4 natural sizes over
     the write and S5b's blueshift reaches (1 + T/8)^2 = 6.23e8; inside the static window (11.28 clocks) 2.82 and 5.8,
     o3_hold O3c's PROVED survival.  Over the write linear survival is not certified (o3_write W5): survives U.
  WZ (computed, imported p2_full.py TS; ITEM178-NULL-PAIRS.md 2, computed there, exact, READ here) "A light ray
     crossing a thin sheet sees null energy with the sign of the sheet's energy density. For a pure tension, that is the
     tension's sign."  thin_shell run here at J3's -1/3 (only the sign enters): sigma sin a < 0 at every crossing angle
     a = 0.5 ... 0.001, control +1/3 positive; far_cypher.py F8 and b5p_cypher.py use the same rule.  So the lone
     negative-tension plane (matter-free, clause (B); vacuum bulk) breaks the NEC pointwise on every ray that crosses
     it, and net per ray is computed nowhere (no partner on its rays is computed; far_cypher's H-NEG-PLANE-UNPAIRED is
     a reading and is not used): keeps_Z 0 by the coding rule, as R1's y*-pieces are coded -- not 1 (it had been
     entered 1, citing only F6's regularity, J3 and 166, none of which bears on (Z)) and not U (the pointwise sign is
     computed).
  Other cells (each cited in cells()): the window hold (o3_hold O3b/O3c), the closing plane (b4d_stage1 D3, b4d_stage5
     F5, b4d_stage6 J4: real matter with rho + p_r < 0), the negative-tension plane (b4d_stage5 F6: regular on the
     evidence, lasts 1; keeps_Z 0 by WZ), both planes (b4d_stage7 K4: every small-separation branch decays, singular),
     stage 7's named escapes, 203's meeting and 198 (a)'s forming phase (nothing computed through the write), the black
     string (o3_readings R3: Gregory-Laflamme, >= 9.2e3 e-folds) and the slab string (b4d_stage1 D4).
  A FINDING RECORDED, NOT REPAIRED (outside this restatement): the both-planes cell's keeps_Z 1 faces WZ's question too
     -- every K4 branch has position 2's plane at negative tension (-1/3 or -1/6 against ours +4/3; far_cypher F6), and
     K2 says that plane must curve or carry matter, which far_cypher codes (Z) U.  It is left as entered.  Read 0 or U
     it moves no statistics verdict on either target (C4, checked): its lasts is 0, and (corridor, keeps_Z, stands) is
     met by R1's NEC-keeping pieces as well.
  The board's readings that set "stands" (decided under 149, labelled; none is M's):
     H-166-ONE-PLANE-SET-ASIDE: M chose "Both planes at once" over "No, ours" and "Yes, position 2's plane", so every
       single-plane placement of eq. (17) -- b4_static's, stage 5's F2 and F6, the route with no second sheet -- is
       set aside as the corridor's configuration (stands 0).  Two-plane cells (closing plane, stage 7, R1's P1 + P2) stand.
     H-WINDOW-SET-ASIDE: 158 (2) with 163's floor sets aside a hold inside the static window as O3's hold (stands 0).
     H-160-RECORD: the record of 160 (the board's) takes the quasi-static black string off as the opening's model.
     H-R1-AS-COMPUTED: R1's cells are entered as computed (H-Z2-PIECES, H-POINTWISE-NEC-ON-P2); 200 (1)'s "no mirror
       image" re-reads P2's Israel stress, not its shape, so it can move keeps_Z, not lasts -- run as variant V200.
     H-SURVIVES-IS-O3C: O3's "survives" read as o3_hold O3c's linear survival over the hold.
  184's "There are no matter free planes" makes every eq. (17)-on-P1 cell a matter-free LIMIT (clause (B) in full on
  P1), as sim2_passage and r1_cover carry it; it applies to every corridor cell alike and is not a discriminator here.

THE CYPHER (roster 1173's five operator-bearing languages; tools/cypher.py imported by path).
  T_WRITE = (corridor 1, static 1, lasts 1, keeps_Z 1, stands 1); T_O3 = (corridor 1, lasts 1, keeps_Z 1, survives 1,
  stands 1).  No computed cell is either target.
  C1 (cypher) statistics refuses T_WRITE from order 3 (3 to 6) and admits it only at order 2: an over-reach assembled
     from pairs (no pair blocks).  The one blocking triple is (corridor, lasts, keeps_Z), and the blocking 4-tuples are
     exactly the two that contain it, (corridor, lasts, keeps_Z, stands) and (corridor, static, lasts, keeps_Z).  No
     computed cell carries the corridor, lasts the write and keeps (Z): lasting and keeping (Z) meet in one cell only,
     the localized hole -- not the corridor.  Of the four triples of (corridor, lasts, keeps_Z, stands), three are met:
     (lasts, keeps_Z, stands) by the localized hole alone; (corridor, lasts, stands) by R1's pieces at y* and at the
     band's midpoint for ell >= 4m alone -- breaking the NEC pointwise, net per ray not computed (F5); (corridor,
     keeps_Z, stands) by several, stage 7's both planes and R1's NEC-keeping pieces, none of which lasts.  The
     negative-tension plane, which met (corridor, lasts, keeps_Z) while its keeps_Z stood at 1, breaks the NEC on every
     crossing ray (WZ) and meets it no longer; put back to 1, the refusal returns to order 4 (C4).
  C2 (cypher) T_O3 is refused by statistics from order 3; the blocking triples are (corridor, lasts, keeps_Z) --
     WRITE's own -- (corridor, lasts, survives) and (corridor, survives, stands): certified survival belongs only to
     holds inside the static window (set aside as O3's hold) and to the localized hole (not the corridor).  Granting F5
     leaves it refused, by the two survival triples alone; certifying survival too for the F5 cells admits it
     (control).  So O3 is blocked twice, by WRITE and independently by linear survival.
  C3 (cypher; codings; deduced) order, algebra and geometry admit both targets in EVERY coding tried -- the 81
     placements of the unknown code on its four axes (0 < 1 kept), every value order of each axis singly, and 200
     seeded joint permutations of all seven (311 in all).  For order and geometry that is by construction (deduced,
     checked at the base coding): a pair of values seen together in a cell meets each staircase inequality and lies in
     its shadow's hull, so both contain statistics' order-2 support, and statistics at order 2 over-reaches here.  Their
     YES is a stable over-reach, not a reading (no cell is the target).  Information's verdict MOVES with the coding:
     YES under every placement of the unknown code, NO for T_O3 under 7 of the 30 single-axis orders, and NO under 85
     (T_WRITE) and 128 (T_O3) of the 200 joint permutations -- an artefact of ordering nominal axes, not a reading.
     Statistics' verdict, taken at order 3 for both targets, is the same in every coding (coding-independent, checked).
  C4 (controls, variants) F5 granted on R1's pointwise breaks: T_WRITE is admitted by all five (statistics at every
     order), the decisive cells being R1's 12 y* and band-midpoint pieces at ell >= 4m; one cell alone
     (r1:0|y_star|level made keeps_Z 1, which makes it the target) flips statistics at every order.  166 decided away
     (the negative plane standing): REFUSED from order 3, as in the main run -- standing, the plane still breaks (Z)
     on its crossing rays; admitted only when its crossing rays are read net-kept as well (control: the cell is then
     the target).  The old entry (the negative plane's keeps_Z 1, 166 standing): admitted at 3, refused from 4 with
     the one blocking 4-tuple (corridor, lasts, keeps_Z, stands) -- that one cell sets order 3 against order 4.  V200
     (R1's keeps_Z read unknown under 200 (1)): refused from order 3, as in the main run.  The recorded finding (both
     planes' keeps_Z read 0 or U): no statistics verdict moves.
THE BOARD'S READING (H-WRITE-NEEDS-ONE-OF-TWO, not M's): WRITE stays OPEN, neither met nor refuted.  On the computed
cells, carrying the corridor, lasting the write and keeping (Z) never occur together -- already as a triple, before
standing under M's words is asked -- and the blocking triple names what would close it: F5 (a pairing that makes the
y*-pieces' pointwise breaks net-kept at ell >= 4m -- on 195 and 198 that pairing would make the README's stress on P2 a
member of a pair, the compatibility rim_readme R9 left open), or R1-COVER's OPEN items on the NEC-keeping pieces (their
UNDECIDED decided over the far field, or a piece of the classes shaped otherwise beyond 3m that keeps the NEC and does
not close onto P1).  166 is not a third door: the lone negative-tension plane lasts but breaks (Z) on its crossing
rays (WZ), so reading it as standing admits nothing unless a partner on those rays is computed too.  O3 needs more
than WRITE: linear survival over 2.0e5 clocks, which W4 does not certify.
On M's guess 198 (option 1) the write is the forming phase, not static (the size grows as the README comes in), so
WRITE as worded is the fixed-size way's input (162, 163); the forming cell enters with lasts, keeps_Z, survives U:
nothing about the forming phase's bulk through the write is computed (179).  Caveats: H-HOLD-FRAME's two glosses
(advanced time: O3-WRITE, sim2_passage X8, R1; far time: B4D-STAGE5) are not reconciled (OPEN, sim2_passage X8) --
every "lasts 0" here is a factor > 500 short in its own owner's frame; R1's cells rest on F1 carried as M1 (OPEN), on
H-PROFILE-CONTINUED and on a finite sample (R1-COVER: NOT SHOWN, OPEN), so its UNDECIDED rows are entered U, never 0;
the cells are an enumeration of what the board computed, not a classification of every bulk.  No question for M:
whether a partner for the README's stress squares with 195 is not needed for this verdict, since no pairing is
computed.
Imports o3_write.py, b4_static.py, r1_cover.py (and through it sim2_passage.py), b4d_stage1.py, p2_full.py,
bulk/stability.py and tools/cypher.py by path.  Stdlib + sympy (+ mpmath, through p2_full.py).  ~30 s.
python3 write_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
ROOT = os.path.dirname(os.path.dirname(WD))
MUT = {}
U = 2                                             # the unknown code: a value nobody has computed, never guessed
LANGS = ("order", "algebra", "geometry", "information", "statistics")
C = ["corridor", "static", "lasts", "keeps_Z", "survives", "stands", "ell"]
IX = {n: i for i, n in enumerate(C)}
WITH_U = ("lasts", "keeps_Z", "survives", "stands")      # axes whose unknown code has no natural place in an order
BASE = {n: ([0, 1, U] if n in WITH_U else [0, 1]) for n in C}
T_WRITE = {"corridor": 1, "static": 1, "lasts": 1, "keeps_Z": 1, "stands": 1}
T_O3 = {"corridor": 1, "lasts": 1, "keeps_Z": 1, "survives": 1, "stands": 1}
# B4D-STAGE5.md F2's table (computed by b4d_stage5.py, check "F2/F3"; READ here from the owner's note, not re-run: the
# instrument takes ~5 min): the hold whose cone reaches K >= 1e4 at ell = 2m, m, m/2, m/4.
STAGE5_HOLDS = {"2m": 16.0, "m": 13.0, "m/2": 10.9, "m/4": 7.8}


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


_SRC = {}


def sources():
    """Every number the cells rest on, from its owner instrument (imported by path, never copied).  Cached: the
    mutants change how cells are made from these numbers, not the owners' numbers."""
    if _SRC:
        return _SRC
    ow = _load(os.path.join(HERE, "o3_write.py"), "wc_o3write")
    floor = float(ow._num(ow.t_min(3)))                                   # W0: o3_write W3 at the example README
    cone = _load(os.path.join(HERE, "b4_static.py"), "wc_b4static").compute(live=False)["cone"]   # W1: S3's cone
    r1 = _load(os.path.join(HERE, "r1_cover.py"), "wc_r1cover")
    P = r1.P                                                              # sim2_passage.py, as r1_cover loads it
    x7 = max(P.layer(e, 1e10)["upper"] for e in (Fr(0), Fr(1, 8), Fr(1)))   # W1: sim2_passage X7 / C8's claimed rows
    cols = {k: dict(v, nec={}) for k, v in r1.pinned_columns().items()}  # W2: the full run's pins, NEC per PIN_NECROWS
    holds = [(h, k) for k, c in cols.items()
             for h in (r1.hold2(c["hold_vtop"]), r1.hold2(c["hold_ys90"]) if c["hold_ys90"] else None) if h is not None]
    mem = {r1.mname(m): m for m in r1.MEMBERS}
    rows = []
    for key, v in sorted(r1.PIN_VERDICTS.items()):
        e, dk, mn = key.split("|")
        rows.append({"key": key, "e": Fr(e), "depth": dk, "member": mn, "crossable": mn in r1.CROSSABLE,
                     "verdict": v[0], "nec": r1.nec_code(r1.nec_along(cols, Fr(e), mem[mn], dk))})
    b1 = _load(os.path.join(HERE, "b4d_stage1.py"), "wc_b4dstage1")
    tang = b1.tangherlini_slice()                                         # W3: D2's slice of the 5D hole
    rh = b1.hole_radius(2 * (floor + 2))                                  # W3: D1's ell > 2 R_reach, D2's r_h
    st = _load(os.path.join(D68, "bulk", "stability.py"), "wc_stability")
    m = st.m
    tr = st.transport()                                                   # W4: S4's identities, derived by the owner
    d1, d2 = st.D_derivatives(2 * m, 2 * m)
    d2s, r0s, r2s = tr["syms"]
    cH0 = sp.simplify(tr["second"][0].coeff(sp.Derivative(tr["psi"], tr["rho"])).subs({d2s: d2}))
    wh = st.white_hole()                                                  # W4: S5b's ray law
    p2 = _load(os.path.join(HERE, "p2_full.py"), "wc_p2full")             # WZ: TS's crossing integral, a pure tension
    ts_neg = p2.thin_shell(0.0, rho=-1 / 3)                               # J3's -1/3 (only the sign enters)
    ts_pos = p2.thin_shell(0.0, rho=1 / 3)                                # control: a positive tension
    a, v = sp.Symbol("a", positive=True), sp.Symbol("v", positive=True)
    _SRC.update({"floor": floor, "floor_p": float(P.write_floor()), "window": float(cone["t_cert"]),
                 "k100": float(cone["t_fail_2"]), "sing": float(ow.SINGULAR_CLOCKS), "x7": float(x7),
                 "r1_hold": max(holds), "r1_rows": rows, "tang": tang, "rh": rh, "D1": d1, "cH0": cH0,
                 "s4": lambda T: float(abs(cH0 * (T * m) * m)),          # natural sizes H0/m over v = T m
                 "s5b": lambda T: float(sp.simplify((1 / wh["spacing"]).subs({a: m, v: T * m}))),   # a ray m off
                 "ts_neg": ts_neg, "ts_pos": ts_pos, "m": m})
    return _SRC


def cells(src):
    """(id, tuple over C, source).  Values as named in the docstring; U = not computed."""
    floor = src["floor"] if not MUT.get("short_floor") else 0.05          # mutant: O3a's 1/(2 xi) in place of the floor
    lasts = lambda hold: 1 if hold >= floor else 0
    surv = lambda hold: 1 if (hold <= src["window"] or MUT.get("survival_any")) else U
    tang = dict(src["tang"])
    if MUT.get("hole_tail"):
        tang["one_over_r"] = tang["ctl"]                                  # mutant: the hole given 4D Schwarzschild's tail
    out = []
    add = lambda i, t, s: out.append((i, tuple(t), s))
    # (corridor, static, lasts, keeps_Z, survives, stands, ell)
    add("eq17-static-flat", (1, 1, lasts(src["sing"]), 1, surv(floor), 0, 1),
        "b4_static.py S3: cone verified to 11.28 clocks, K >= 100 from 14.88; B4.md: singular by ~18.  Keeps Z: vacuum "
        "bulk, warptheorem Z1 (passage5d P2) 'plane deficit = bulk pull'.  Stands 0: one plane, H-166-ONE-PLANE-SET-ASIDE")
    add("window-hold", (1, 1, lasts(src["window"]), 1, surv(src["window"]), 0, 1),
        "o3_hold.py O3b/O3c: a hold inside the static window, survival PROVED there; set aside as O3's hold by 158 (2) "
        "with 163 (H-WINDOW-SET-ASIDE)")
    add("eq17-static-finite", (1, 1, lasts(max(STAGE5_HOLDS.values())), 1, surv(floor), 0, 0),
        "b4d_stage5.py F2/F3 (READ from B4D-STAGE5.md F2): K >= 1e4 within 8-16 clocks at ell = 2m ... m/4; one plane")
    for e in (0, 1):
        add("cone-no-second-sheet", (1, 1, lasts(src["x7"]), 1, surv(floor), 0, e),
            "sim2_passage.py X7/X8, C8: every layer to 1e10 K_bs in J^-(P_c) within 389.3 clocks at the nine ell; the "
            "route with no second sheet is one plane")
        add("closing-plane", (1, 1, U, 0, U, 1, e),
            "b4d_stage1.py D3 (STRUCTURAL at small y_w, flat), b4d_stage5.py F5, b4d_stage6.py J4: rho + p_r = "
            "R4_kk (y_w + 3 y_w^2/ell) < 0, real matter; its hold through the write not computed")
        add("both-planes-escapes", (1, 1, U, U, U, 1, e),
            "B4D-STAGE7.md 'still open' 1-4 (d near the slab's singular surface, direction-dependent data, curved "
            "planes, non-AdS outer bulks): not computed")
        add("meeting-203", (1, 1, U, U, U, 1, e),
            "203 (M's): the corridor as the surface where the two planes' bulks meet; no bulk computed through the "
            "write (forming_rim.py F0: its arrangements are force diagrams, not spacetimes)")
        add("forming-198a", (1, 0, U, U, U, 1, e),
            "198 (M's guess, option 1): the README forms the corridor, size growing; README-HELD.md; chain_cypher "
            "ARRIVAL: formation in the bulk OPEN (179)")
    # keeps_Z by the coding rule (WZ): a lone plane of negative pure tension (clause (B), matter-free) in a vacuum bulk;
    # a ray crossing it sees null energy with the tension's sign at every crossing angle (p2_full.py TS, imported and
    # run in sources(); ITEM178-NULL-PAIRS.md 2, computed, exact; far_cypher.py F8) -- broken pointwise, on every
    # crossing ray -- and net per ray is computed nowhere (no partner on its rays is computed; far_cypher's
    # H-NEG-PLANE-UNPAIRED is a reading and is not used here).  So 0, coded as R1's y*-pieces are, not 1 and not U.
    zneg = 0 if any(x < 0 for _, x in src["ts_neg"]) else 1
    if MUT.get("neg_keeps_z1"):
        zneg = 1                                                          # mutant: the cell back to keeps_Z 1
    add("negative-plane", (1, 1, 1, zneg, U, 0 if not MUT.get("decide_166") else 1, 0),
        "b4d_stage5.py F6 (check 'F6', ell = 2m, m, m/2): regular on the evidence, static; b4d_stage6.py J3; one plane: "
        "set aside by 166 (M chose 'Both planes at once', not 'Yes, position 2's plane').  Keeps Z 0: a negative pure "
        "tension, crossed at any angle, gives negative null energy (p2_full.py TS; ITEM178 2; far_cypher.py F8); net "
        "per ray not computed")
    add("both-planes", (1, 1, 0, 1, U, 1, 0),
        "b4d_stage7.py K4: every small-separation branch has a decaying outer bulk, singular (stage 5 F2; H-F2-STABLE)")
    hole_is_corridor = int(not (tang["one_over_r"] == 0 and tang["kappa"] != 0 and src["rh"] > 2))
    add("localized-hole", (hole_is_corridor, 1, 1, 1, 1, 1, 1),
        "b4d_stage1.py D2: no 1/r tail, kappa = 1/r_h, r_h ~ 582 m >> 2 m; Ishibashi-Kodama (READ): linearly stable")
    add("black-string", (0, 0, 0, 1, 0, 0, 1),
        "o3_readings.py R3 (check 'R3 (ii)'): Gregory-Laflamme, >= 9.2e3 e-folds over the write; ends in "
        "Schwarzschild, not the corridor; H-160-RECORD")
    add("slab-string", (0, 0, U, 1, U, 0, 1),
        "b4d_stage1.py D4, o3_readings.py R4 (b): H-SLAB-PHASES open, not shown; its end is a uniform string")
    for r in src["r1_rows"]:
        L = {"HOLDS": 1, "FAILS": 0, "UNDECIDED": U}[r["verdict"]]
        Z = {2: 1, 0: 0, 1: U}[r["nec"]]
        if MUT.get("f5_granted") and Z == 0:
            Z = 1                                                         # mutant: F5's pairing decided in code
        add("r1:" + r["key"], (int(r["crossable"]), 1, L, Z, U, 1, 1 if r["e"] <= Fr(1, 4) else 0),
            "r1_cover.py PIN_VERDICTS / PIN_NECROWS through nec_along, nec_code (H-R1-AS-COMPUTED)")
    if MUT.get("survival_any"):                                           # mutant: W5 ignored for every static corridor
        out = [(i, (c[:4] + (1,) + c[5:]) if c[0] == 1 and c[1] == 1 and c[4] == U else c, s) for i, c, s in out]
    if MUT.get("u_as_one"):
        out = [(i, tuple(1 if x == U else x for x in c), s) for i, c, s in out]   # mutant: the unknown guessed
    if MUT.get("seat_write"):
        add("seated", (1, 1, 1, 1, U, 1, 1), "a bulk held through the write, seated as data")
    return out


def hit(h, tgt):
    return all(h[IX[k]] == v for k, v in tgt.items())


_CY = []


def _cy():
    if not _CY:
        _CY.append(_load(os.path.join(ROOT, "tools", "cypher.py"), "wc_cypher"))
    return _CY[0]


def admitted(cs, lang, opts=None, coding=None):
    """The decoded admitted cells (None if the language is silent).  coding: a value order per axis (default BASE)."""
    cy = _cy()
    tup = sorted({c for _, c, _ in cs})
    vo = {}
    for n in C:
        present = {t[IX[n]] for t in tup}
        vo[n] = [x for x in (coding or BASE).get(n, BASE[n]) if x in present]
    ix = cy.Index("write", C, [list(t) for t in tup], value_order=vo)
    out, _ = cy.ADMISSION[lang][0](ix, opts or {})
    if out is None:
        return None
    return {tuple(ix.decode[i][x[i]] for i in range(len(C))) for x in out}


def answer(cs, tgt, lang, opts=None, coding=None):
    a = admitted(cs, lang, opts, coding)
    return None if a is None else any(hit(h, tgt) for h in a)


def stat_profile(cs, tgt):
    return {k: answer(cs, tgt, "statistics", {"statistics_order": k}) for k in range(2, 7)}


def blocking(cs, tgt, k):
    """k-sets of the target's fixed axes whose target values occur together in no cell."""
    want = {IX[n]: v for n, v in tgt.items()}
    return sorted(tuple(C[i] for i in S) for S in itertools.combinations(sorted(want), k)
                  if not any(all(c[i] == want[i] for i in S) for _, c, _ in cs))


def witnesses(cs, tgt, k):
    want = {IX[n]: v for n, v in tgt.items()}
    return {tuple(C[i] for i in S): sorted({i_ for i_, c, _ in cs if all(c[j] == want[j] for j in S)})
            for S in itertools.combinations(sorted(want), k)}


def kind(cid):
    """the cell's family: R1 cells by member and depth row, others by id"""
    if not cid.startswith("r1:"):
        return cid
    _, dk, mn = cid[3:].split("|")
    return "r1 %s @ %s" % (mn, dk)


def codings(n_random=200, seed=196):
    """(family, coding): the 81 placements of U on its four axes (0 < 1 kept); every value order of each axis singly;
    and seeded joint permutations of all seven axes."""
    out = []
    for p in itertools.product(range(3), repeat=len(WITH_U)):
        cd = {n: list(BASE[n]) for n in C}
        for n, pos in zip(WITH_U, p):
            cd[n] = [0, 1]
            cd[n].insert(pos, U)
        out.append(("placement", cd))
    for n in C:
        for perm in itertools.permutations(BASE[n]):
            cd = {k: list(BASE[k]) for k in C}
            cd[n] = list(perm)
            out.append(("single", cd))
    rng = random.Random(seed)
    for _ in range(n_random):
        cd = {}
        for n in C:
            vals = list(BASE[n])
            rng.shuffle(vals)
            cd[n] = vals
        out.append(("joint", cd))
    return out


def recode(cs, cid, **vals):
    """cs with the named cell's coordinates replaced (a variant, run beside the main cells, never in place of them)"""
    return [(i, tuple(vals.get(C[j], x) for j, x in enumerate(c)) if i == cid else c, s) for i, c, s in cs]


def compute(sweep=True):
    src = sources()
    cs = cells(src)
    d = {"src": src, "cells": cs}
    d["in_cells_write"] = sorted(i for i, c, _ in cs if hit(c, T_WRITE))
    d["in_cells_o3"] = sorted(i for i, c, _ in cs if hit(c, T_O3))
    d["stat_write"] = stat_profile(cs, T_WRITE)
    d["stat_o3"] = stat_profile(cs, T_O3)
    d["block_write"] = {k: blocking(cs, T_WRITE, k) for k in (2, 3, 4)}
    d["block_o3"] = {k: blocking(cs, T_O3, k) for k in (2, 3)}
    core = {k: T_WRITE[k] for k in ("corridor", "lasts", "keeps_Z", "stands")}
    d["wit3"] = {S: sorted({kind(i) for i in v}) for S, v in witnesses(cs, core, 3).items()}
    d["wit2_lz"] = sorted({kind(i) for i in witnesses(cs, core, 2)[("lasts", "keeps_Z")]})
    st3 = {"statistics_order": 3}                                         # statistics' lowest refusing order, both
    d["base"] = {lang: (answer(cs, T_WRITE, lang, st3 if lang == "statistics" else None),
                        answer(cs, T_O3, lang, st3 if lang == "statistics" else None)) for lang in LANGS}
    if sweep:
        by = {lang: {"write": set(), "o3": set()} for lang in LANGS}
        cnt = {lang: {"write": 0, "o3": 0} for lang in LANGS}                # codings in which the language refuses
        fam = {}                                                          # the same counts, by coding family
        cds = codings()
        for f, cd in cds:
            fam.setdefault(f, {"n": 0, **{lang: [0, 0] for lang in LANGS}})["n"] += 1
            for lang in LANGS:
                a = admitted(cs, lang, st3 if lang == "statistics" else None, cd)
                aw = None if a is None else any(hit(h, T_WRITE) for h in a)
                ao = None if a is None else any(hit(h, T_O3) for h in a)
                by[lang]["write"].add(aw)
                by[lang]["o3"].add(ao)
                cnt[lang]["write"] += aw is False
                cnt[lang]["o3"] += ao is False
                fam[f][lang][0] += aw is False
                fam[f][lang][1] += ao is False
        d["by_coding"], d["n_codings"], d["refusals"], d["by_family"] = by, len(cds), cnt, fam
    st2 = admitted(cs, "statistics", {"statistics_order": 2})
    d["contain_stat2"] = {lang: st2 <= admitted(cs, lang) for lang in ("order", "geometry")}
    # controls and variants
    f5 = [(i, (c[:3] + (1,) + c[4:]) if i.startswith("r1:") and c[IX["keeps_Z"]] == 0 else c, s) for i, c, s in cs]
    d["f5_cells"] = sorted(i for i, c, _ in f5 if hit(c, T_WRITE))
    d["f5_write"] = {lang: answer(f5, T_WRITE, lang, {"statistics_order": 6} if lang == "statistics" else None)
                     for lang in LANGS}
    d["f5_stat"] = stat_profile(f5, T_WRITE)
    d["f5_o3"] = stat_profile(f5, T_O3)
    d["f5_block_o3"] = blocking(f5, T_O3, 3)
    f5v = [(i, (c[:4] + (1,) + c[5:]) if i in d["f5_cells"] else c, s) for i, c, s in f5]
    d["f5v_o3"] = {lang: answer(f5v, T_O3, lang, {"statistics_order": 6} if lang == "statistics" else None)
                   for lang in LANGS}
    one = [(i, (c[:3] + (1,) + c[4:]) if i == "r1:0|y_star|level" else c, s) for i, c, s in cs]
    d["one_cell"] = stat_profile(one, T_WRITE)
    v200 = [(i, (c[:3] + (U,) + c[4:]) if i.startswith("r1:") else c, s) for i, c, s in cs]
    d["v200_write"] = stat_profile(v200, T_WRITE)
    d["v166_write"] = stat_profile(recode(cs, "negative-plane", stands=1), T_WRITE)          # 166 decided away
    d["v166z_write"] = stat_profile(recode(cs, "negative-plane", stands=1, keeps_Z=1), T_WRITE)   # and net-kept
    vz = recode(cs, "negative-plane", keeps_Z=1)                          # the old entry, 166 standing
    d["vzneg_write"], d["vzneg_block"] = stat_profile(vz, T_WRITE), {k: blocking(vz, T_WRITE, k) for k in (3, 4)}
    d["vbp"] = {z: (stat_profile(recode(cs, "both-planes", keeps_Z=z), T_WRITE),          # the recorded finding
                    stat_profile(recode(cs, "both-planes", keeps_Z=z), T_O3)) for z in (0, U)}
    return d


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    s = d["src"]
    cs = {i: c for i, c, _ in d["cells"]}
    T = s["floor"]
    add("W0 the write's floor is 1.997e5 clocks (o3_write t_min(3), example README, Z = 108.75); sim2_passage's "
        "write_floor agrees", 1.996e5 < T < 1.998e5 and abs(s["floor_p"] / T - 1) < 1e-9)
    add("W1 eq. (17)'s static bulk on one plane: verified edge 11.28, K >= 100 at 14.88, singular ~18 clocks; stage 5's "
        "8-16; the no-second-sheet budget 389.3 -- every one below the floor by > 500x, and every such cell lasts 0",
        abs(s["window"] - 11.277) < 0.01 and abs(s["k100"] - 14.884) < 0.01 and s["sing"] == 18
        and abs(s["x7"] - 389.27) < 0.05 and max(s["x7"], s["sing"], max(STAGE5_HOLDS.values())) * 500 < T
        and all(cs[i][IX["lasts"]] == 0 for i in ("eq17-static-flat", "eq17-static-finite", "window-hold")))
    rows = s["r1_rows"]
    hold_x = [r for r in rows if r["crossable"] and r["verdict"] == "HOLDS"]
    keep_x = [r for r in rows if r["crossable"] and r["nec"] == 2]
    add("W2 R1's two-order holds are at most 88.74 clocks (100|1/2), floor/hold >= 2250: its verdicts are verdicts for "
        "the whole write", abs(s["r1_hold"][0] - 88.7418) < 1e-3 and s["r1_hold"][1] == "100|1/2"
        and T / s["r1_hold"][0] >= 2250)
    add("W2 the crossable rows that HOLD are 12, all at ell >= 4m, all at y* or the band's midpoint, and every one breaks "
        "the NEC pointwise at a settled node; the 13 that keep it at every settled node never HOLD (12 UNDECIDED, 1 FAILS)",
        len(hold_x) == 12 and all(r["e"] <= Fr(1, 4) and r["depth"] in ("y_star", "band_mid") and r["nec"] == 0
                                  for r in hold_x)
        and len(keep_x) == 13 and sorted(r["verdict"] for r in keep_x) == ["FAILS"] + ["UNDECIDED"] * 12
        and sum(r["member"] == "smooth near" and r["depth"] == "tenth" and r["verdict"] == "UNDECIDED"
                and r["nec"] == 2 for r in rows) == 9)
    t = s["tang"]
    m, rh = sp.Symbol("m", positive=True), sp.Symbol("r_h", positive=True)
    add("W3 the localized hole: no 1/r tail (4D Schwarzschild's -2m the control), surface gravity 1/r_h, r_h = 582 m >> "
        "r0 = 2 m -- not the corridor", t["one_over_r"] == 0 and sp.simplify(t["ctl"] + 2 * m) == 0
        and sp.simplify(t["kappa"] - 1 / rh) == 0 and 575 < s["rh"] < 590 and cs["localized-hole"][IX["corridor"]] == 0)
    add("W4 Wall E: the horizon is extremal (D' = 0); over the write T/4 = 4.99e4 natural sizes and (1 + T/8)^2 = "
        "6.23e8; at the window's top 2.82 and 5.8 (O3c's bound 6.5): survival certified in the window only",
        s["D1"] == 0 and abs(s["s4"](T) - T / 4) < 1e-6 * T and 4.98e4 < s["s4"](T) < 5.0e4
        and 6.22e8 < s["s5b"](T) < 6.24e8 and abs(s["s4"](s["window"]) - 2.819) < 0.01
        and abs(s["s5b"](s["window"]) - 5.80) < 0.01 and s["s5b"](s["window"]) < 6.5
        and cs["window-hold"][IX["survives"]] == 1 and cs["eq17-static-flat"][IX["survives"]] == U)
    neg, pos = s["ts_neg"], s["ts_pos"]
    add("WZ p2_full TS (imported): a negative pure tension crossed at angle a gives sigma sin a < 0 at every angle "
        "(control: a positive tension gives > 0) -- broken pointwise on every crossing ray, net per ray not computed: "
        "the negative plane's keeps_Z is 0 by the coding rule",
        all(x < 0 and abs(x - (-1 / 3) * math.sin(a_)) < 1e-12 for a_, x in neg) and all(x > 0 for _, x in pos)
        and cs["negative-plane"][IX["keeps_Z"]] == 0)
    add("C1 no computed cell is T_WRITE or T_O3", d["in_cells_write"] == [] and d["in_cells_o3"] == [])
    add("C1 statistics refuses T_WRITE at orders 3-6 and admits it only at 2 (an over-reach from pairs); no pair blocks; "
        "the one blocking triple is (corridor, lasts, keeps_Z), and the blocking 4-tuples are the two that contain it, "
        "(corridor, lasts, keeps_Z, stands) and (corridor, static, lasts, keeps_Z)",
        d["stat_write"] == {2: True, 3: False, 4: False, 5: False, 6: False}
        and d["block_write"] == {2: [], 3: [("corridor", "lasts", "keeps_Z")],
                                 4: [("corridor", "lasts", "keeps_Z", "stands"),
                                     ("corridor", "static", "lasts", "keeps_Z")]})
    w = d["wit3"]
    add("C1 of the four triples of (corridor, lasts, keeps_Z, stands): (corridor, lasts, keeps_Z) is met by no cell; "
        "(lasts, keeps_Z, stands) by the localized hole alone (not the corridor); (corridor, lasts, stands) by R1's pieces "
        "at y* / the band's midpoint alone (NEC broken pointwise); (corridor, keeps_Z, stands) by both planes and R1's "
        "NEC-keeping pieces, none lasting; and lasting with keeping (Z) meet in the localized hole alone",
        w[("corridor", "lasts", "keeps_Z")] == []
        and w[("lasts", "keeps_Z", "stands")] == ["localized-hole"]
        and w[("corridor", "lasts", "stands")] == ["r1 level @ band_mid", "r1 level @ y_star", "r1 smooth near @ y_star"]
        and w[("corridor", "keeps_Z", "stands")] == ["both-planes", "r1 smooth adj @ tenth", "r1 smooth near @ tenth",
                                                     "r1 smooth near @ zero"]
        and d["wit2_lz"] == ["localized-hole"])
    add("C2 statistics refuses T_O3 from order 3; blocking triples (corridor, lasts, keeps_Z) -- WRITE's -- (corridor, "
        "lasts, survives) and (corridor, survives, stands); with F5 granted still refused, by the two survival triples "
        "alone; with survival certified for the F5 cells too, all five admit (control)",
        d["stat_o3"] == {2: True, 3: False, 4: False, 5: False, 6: False}
        and d["block_o3"] == {2: [], 3: [("corridor", "lasts", "keeps_Z"), ("corridor", "lasts", "survives"),
                                         ("corridor", "survives", "stands")]}
        and d["f5_o3"][3] is False
        and d["f5_block_o3"] == [("corridor", "lasts", "survives"), ("corridor", "survives", "stands")]
        and all(d["f5v_o3"][l] for l in LANGS))
    if "by_coding" in d:
        by, fm = d["by_coding"], d["by_family"]
        info = {f: tuple(fm[f]["information"]) for f in fm}
        add("C3 over %d codings, statistics at order 3: statistics refuses both targets in every one (coding-"
            "independent); order, algebra, geometry admit both in every one (a stable over-reach); information's verdict "
            "moves with the coding -- refusing (T_WRITE, T_O3) in %s of the 81 placements of U, %s of the 30 single-axis "
            "orders, %s of the 200 joint permutations: an artefact" % (d["n_codings"], info["placement"], info["single"],
                                                                      info["joint"]),
            d["n_codings"] == 311 and {f: fm[f]["n"] for f in fm} == {"placement": 81, "single": 30, "joint": 200}
            and by["statistics"]["write"] == {False} and by["statistics"]["o3"] == {False}
            and all(by[l]["write"] == {True} and by[l]["o3"] == {True} for l in ("order", "algebra", "geometry"))
            and info == {"placement": (0, 0), "single": (0, 7), "joint": (85, 128)})
    add("C3 (deduced, checked at the base coding) order and geometry contain statistics' order-2 support",
        all(d["contain_stat2"].values()))
    add("C4 control (the decisive cells): F5 granted on R1's pointwise breaks -> T_WRITE admitted by all five, statistics "
        "at every order; the cells are R1's y* / band-midpoint pieces at ell >= 4m; one cell alone (made the target) "
        "flips every order",
        all(d["f5_write"][l] for l in LANGS) and all(d["f5_stat"].values()) and len(d["f5_cells"]) == 12
        and all(i.startswith("r1:") for i in d["f5_cells"]) and all(d["one_cell"].values()))
    add("C4 variants: 166 decided away (the negative plane standing) -> refused from order 3, as in the main run; "
        "admitted when its crossing rays are also read net-kept (control: the cell is then the target); V200 (R1's "
        "keeps_Z unknown) -> refused from order 3, as in the main run",
        d["v166_write"] == d["stat_write"] and all(d["v166z_write"].values()) and d["v200_write"] == d["stat_write"])
    add("C4 the old entry (the negative plane's keeps_Z 1, 166 standing) gives the old profile -- admitted at 3, refused "
        "from 4, the one blocking 4-tuple (corridor, lasts, keeps_Z, stands): that cell alone sets order 3 against 4",
        d["vzneg_write"] == {2: True, 3: True, 4: False, 5: False, 6: False}
        and d["vzneg_block"] == {3: [], 4: [("corridor", "lasts", "keeps_Z", "stands")]})
    add("C4 the recorded finding: both planes' keeps_Z read 0 or U moves no statistics verdict on either target",
        all(d["vbp"][z] == (d["stat_write"], d["stat_o3"]) for z in (0, U)))
    return res


MUTANTS = {"seat_write": "a bulk held through the write seated as data",
           "short_floor": "O3a's 1/(2 xi) = 0.05 clocks in place of the write's floor",
           "decide_166": "the lone negative-tension plane read as standing (166 decided away in code)",
           "f5_granted": "F5's pairing decided in code (R1's pointwise breaks read net-kept)",
           "survival_any": "linear survival read as certified over any hold (W5 ignored)",
           "hole_tail": "the localized hole given 4D Schwarzschild's 1/r tail (read as the corridor)",
           "u_as_one": "every uncomputed value guessed favourable",
           "neg_keeps_z1": "the negative-tension plane's keeps_Z set back to 1 (TS ignored)"}


def selftest():
    t0 = time.time()
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d  (%.0f s)" % (k, len(r), time.time() - t0))
    return k == len(r)


def mutants():
    caught = 0
    sources()
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute(sweep=False)) if not ok]
        except Exception as ex:                                           # a crash is reported, never counted as caught
            failed, crashed = [], "%s: %s" % (type(ex).__name__, ex)
        else:
            crashed = None
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-13s %-62s %s" % (k, desc, "CRASHED " + crashed if crashed else
                                            ("caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT")))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    s = d["src"]
    print("write_cypher.py -- WRITE and O3 through the cypher\n")
    print("W0 floor %.4g clocks;  W1 static bulk: %.2f / %.2f / %g clocks, stage 5 <= %g, no second sheet %.1f"
          % (s["floor"], s["window"], s["k100"], s["sing"], max(STAGE5_HOLDS.values()), s["x7"]))
    print("W2 R1 cone: max two-order hold %.2f at %s (floor/hold %.0f)" % (s["r1_hold"][0], s["r1_hold"][1],
                                                                          s["floor"] / s["r1_hold"][0]))
    print("W3 localized hole: r_h = %.0f m; W4 over the write S4 %.3g, S5b %.3g; in the window %.2f, %.2f"
          % (s["rh"], s["s4"](s["floor"]), s["s5b"](s["floor"]), s["s4"](s["window"]), s["s5b"](s["window"])))
    print("WZ TS, a pure tension -1/3 crossed at angles %s: %s (control +1/3: %s)"
          % ([a_ for a_, _ in s["ts_neg"]], ["%.3g" % x for _, x in s["ts_neg"]], ["%.3g" % x for _, x in s["ts_pos"]]))
    print("\ncells (distinct tuples over %s; U = %d):" % (C, U))
    seen = {}
    for i, c, _ in d["cells"]:
        seen.setdefault(c, set()).add(kind(i))
    for c, ks in sorted(seen.items()):
        print("  %s  %s" % (c, ", ".join(sorted(ks))))
    print("\nT_WRITE in cells: %s;  T_O3 in cells: %s" % (d["in_cells_write"], d["in_cells_o3"]))
    print("statistics on T_WRITE by order:", d["stat_write"], " blocking:", d["block_write"])
    print("statistics on T_O3 by order:", d["stat_o3"], " blocking:", d["block_o3"])
    print("triple witnesses (corridor, lasts, keeps_Z, stands):")
    for S, v in d["wit3"].items():
        print("  %-36s %s" % (", ".join(S), "(no cell)" if not v else ", ".join(v) if len(v) < 6 else
                              "%d kinds" % len(v)))
    print("pair witnesses (lasts, keeps_Z):", ", ".join(d["wit2_lz"]))
    print("languages at the base coding (T_WRITE, T_O3):", d["base"])
    if "by_coding" in d:
        print("over %d codings (statistics at order 3), the codings in which each language refuses (T_WRITE, T_O3):"
              % d["n_codings"], {l: (x["write"], x["o3"]) for l, x in d["refusals"].items()})
        for f, x in d["by_family"].items():
            print("  %-9s (%3d): %s" % (f, x["n"], {l: tuple(x[l]) for l in LANGS}))
    print("order and geometry contain statistics' order-2 support (base coding):", d["contain_stat2"])
    print("control F5 granted: T_WRITE", d["f5_write"], "statistics", d["f5_stat"], "; T_O3 statistics", d["f5_o3"])
    print("control F5 granted: T_O3 blocking triples", d["f5_block_o3"])
    print("control F5 + survival certified: T_O3", d["f5v_o3"])
    print("one cell (r1:0|y_star|level keeps_Z 1):", d["one_cell"])
    print("variant 166 decided away:", d["v166_write"], " and net-kept too:", d["v166z_write"])
    print("variant V200:", d["v200_write"])
    print("the old entry (negative plane keeps_Z 1):", d["vzneg_write"], " blocking:", d["vzneg_block"])
    print("recorded finding, both planes' keeps_Z read 0 / U (T_WRITE, T_O3):", d["vbp"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
