#!/usr/bin/env python3
"""verify_ledger.py -- item 330: "before anything enters verification, the previous verification results need to be
full accounted so the next object being verified is not left stale by outstanding corrections" (M-ACCOUNT-BEFORE-
VERIFY). The ledger of every verification so far -- the verifiers' reports of items 254, 258, 261, 264, 267, 269, 271,
304, 310, 317, 319 and 332 [item 332 added], and the auditing agent's of 281 -- one row per accepted qualification and
per note outside a claim: where it is seated, and for each object still queued for verification (O1c, B5a, C8; 329-330)
whether it is carried there, does not bear (with the reason), or is outstanding. What is outstanding for rows outside
the queue is listed, not repaired. The gate for every hand-off from now on: run it before each verifier is sent; a
queued object with an outstanding row does not go. Worked in the conversation (the dispositions deduced from the rulings
file's reports and the instruments' notes, each marker checked against its file; not verified by a separate session);
2026-10-12.

  L0 (read) M's item-330 words, verbatim in the rulings file, and each report's header there.
  L1 (computed) Every seated correction's marker is found in the file the report names.
  L2 (computed) Every correction the ledger says a queued object carries is found in that object's instrument.
  L3 (computed) No queued object has an outstanding row: O1c, B5a and C8 are not stale against any verification so far.
  L4 (read; computed) What stays outstanding outside the queue, for the rows it names: the rows that rested on kappa =
     0 (271 (3): stability S5b, o3_hold O3c and write_cypher W4, marked at 281, not repaired); T3's and E3's flip at
     the small end (271 (8), 319 (Q4)); the WRITE row's 158 (2) against 163 within a horizon (317, outside (c)); and
     the Warp Theorem's register itself -- warptheorem.py and WARPTHEOREM.md carry no history after item 247, so their
     O2 row ("the horizon is extremal (surface gravity 0)", PROVED, which T1 re-runs), their O1c row (o1c_complete)
     and their B5a row (the composite reading) predate 270-330 and carry no mark (found by this ledger, checked live:
     the row flips when the register is updated).  Each is accounted for the queue -- none bears on O1c, B5a or C8,
     whose own instruments carry the corrections -- and owed to its own row, the register's after the queued
     verifications, before that row is verified.
  L5 (stated) C9 (items 325-327) is at its verifier; its verdict is accounted here on return, before O1c goes (330
     (a)).
     [Item 332: returned, CONFIRMED with qualifications; its nine rows are entered above, carried by O1c, B5a and C8
     where they bear (Q1; B5a also Q5), and the ledger is clean for O1c.]
  [Item 331 (M-UPDATE-STALE-NOW): L4's three rows outside the queue are brought current -- stability S6, o3_hold O3e
     and write_cypher W5 (the corridor's own non-extremal horizon), ledger E3s and warptheorem T3s (the small end's
     ledger), write_cypher W5 (b) (158 (2) against 163, H-HOLD-IS-THE-FACE, put to M) -- and the register with them:
     warptheorem.py's LEMMAS_NOW and WARPTHEOREM.md's current head and its history through item 333, the item-247
     rows kept beside them as the record.  L4 now checks the register current, not stale.]
  [Item 334: the reading put to M is confirmed -- M-HOLD-IS-THE-FACE -- and 317 (c) is answered on M's ruling.]
  [Item 339: B5a one-way returned, CONFIRMED with qualifications; its nine rows and its note outside B5a are entered
  above, carried by C8 where they bear ((Q4)-(Q8)), and the ledger is clean for C8. The note outside B5a found QUEUED
  mapping B5a to b5a_residue alone, so a correction carried in b5a_oneway escaped L2's check: QUEUED_FILES now names
  each object's files, and L2 requires the marker in one of them.]
  [Item 341: C8 one-way returned, CONFIRMED with qualifications; its ten rows and its notes outside C8 are entered
  above, every one seated in c8_level (V10 a new entry with a check) or outside it, and the 1.9e-69 figure 339 (Q7)
  carried into three notes is corrected there. O1c, B5a and C8 are verified (337, 339, 341): the queue of 329-330 is
  empty, and this gate stands for the next object sent.]
  [Item 344: M finalized ARRIVAL at the small end ("ARRIVAL is ready for the verifier"), and it is queued. Its column
  (ARRIVAL_BEAR) accounts it against every row of the sixteen reports, beside the record's three: 26 carried, each
  marker found in arrival_small, and 69 not bearing, each with its reason (the two-way rows among them). Ten of the
  carried rows, in five findings, were not yet written there when the gate first ran -- 267 (Q6), the floor a least
  time; 310 (outside G5), 319 (Q2) and 341 (Q4), J1's open period under the G5 readings; 332 (Q1), 337 (Q3, Q4) and 317
  (Q8), the coupling zero under 328, exactness at the two-derivative order and the warp's first order; 337 (outside),
  the audit on one coding; 341 (Q2) and (Q10), the rests-on incomplete (226, 330) -- and are carried by arrival_small
  V13 (item 344), with a check and two mutants, before the verifier starts. L6 checks the column complete.]
  [Item 348: ARRIVAL returned, CONFIRMED with qualifications, one sentence refuted. Its report's rows are entered above,
  each carried in arrival_small (item-348 notes and V14) and, where it bears, in c8_level (Q6) and README-HELD.md
  (outside). Six of ARRIVAL's own bearings are corrected: (339, Q8) and (304, outside) bear, and are carried; (310,
  Q2)'s reason is restated; (337, Q5/Q6), (341, Q10) and (310, outside G5) were carried through markers belonging to
  other points, and are re-pointed. The verifier's note stands as this gate's limit: L2 finds a correction's marker in
  the object, not whether the text there carries its substance -- that is a critic's reading, and a verifier's. The
  queue is empty.]
  [Item 351: M finalized FAR at both ends ("FAR both ends is now ready for the verifier."), FARs (far_small F0-F9) and
  FAR (far_large L0-L9) as one object, and it is queued. Its column (FAR_BEAR) accounts it against every row of the
  seventeen reports: 42 carried, each marker found in far_small or far_large, and 62 not bearing, each with its reason
  (the two-way rows among them). Fourteen of the carried rows were not yet written there when the gate first ran --
  261 (Q1)-(Q2), the large end's start a convention; 267 (Q6), the floor a least time; 271 (Q3), 319 (Q1) and 341 (Q3),
  position 2's white-hole face and J5's bound; 304 (outside), the potential's fall-off; 310 (Q3), position 2 reading
  its own mass; 317 (Q8), warp order at first order; 332 (Q8), 226 read to include tension; 337 (Q3)-(Q4), the
  two-derivative order; 337 (Q9), the options M chose; 341 (Q4), both conventions for sigma; 348 (Q2), a lossy
  collapse; 341 (Q2) and 348 (Q5), the rests-on -- and are carried by far_small F10 and far_large L10 (item 351), each
  with a check and a mutant, before the verifier starts. L7 checks the column complete.]

What this does not claim.
  - That the dispositions are complete beyond the reports' own texts: a qualification is what a report lists and the
    critic accepted; the bearing judgements are the board's, each with its reason.
  - Anything about verifications before item 254 (the earlier waves' "verified once" instruments): no queued object
    rests on them except through the claims listed.

Imports nothing.  Stdlib only.  python3 verify_ledger.py [--selftest | --mutants]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("Remember, before anything enters verification, the previous verification results need to be full accounted "
         "so the next object being verified is not left stale by outstanding corrections",)
QUEUED = {"O1c": "o1c_oneway.py", "B5a": "b5a_residue.py", "C8": "c8_level.py"}
# [item 339, the B5a verifier's note outside B5a: QUEUED maps B5a to b5a_residue alone, so b5a_oneway escaped L2] the
# files each queued object's carried corrections may sit in
QUEUED_FILES = {"O1c": ("o1c_oneway.py",), "B5a": ("b5a_residue.py", "b5a_oneway.py"),
                "C8": ("c8_level.py", "m1p2x_oneway.py")}
HEADERS = {254: "254. **Claim C1 verified", 258: "258. **Claim C2 verified", 261: "261. **Claim C3 verified",
           264: "264. **Claim C6 verified", 267: "267. **Claim C5 verified", 269: "269. **Claim C4 verified",
           271: "271. **Claim C7 verified", 281: "281. **The audit before 270", 304: "304. **C1 one-way verified",
           310: "310. **C4 one-way verified", 317: "317. **C5 one-way verified", 319: "319. **C7 one-way verified",
           332: "332. **C9 verified", 337: "337. **O1c one-way verified",
           339: "339. **B5a one-way verified",
           341: "341. **C8 one-way verified",
           348: "348. **ARRIVAL at the small end verified"}
NA = "n/a"


def C(f, m):
    return ("carried", f, m)


def N(reason):
    return (NA, reason)


O, B, E = "o1c_oneway.py", "b5a_residue.py", "c8_level.py"
NO_O, NO_B, NO_E = N("not used by O1c"), N("not used by B5a"), N("not used by C8")
TWO_WAY = N("the two-way claim, superseded by its one-way re-posing and that verification (282; 304-319)")
# report, label, gist, seated [(file, item)], bearings
ROWS = [
    (254, "Q1", "null energy zero for matter; the plane's tangential reading is the bulk's Weyl term",
     [("localized_hole.py", 254)], NO_O, N("B5a reads surface stress, not the plane's 4D reading of the Weyl term"),
     N("z_net is the surface stress's share")),
    (254, "Q2", "the 1/r^2 pull only for r_h << r << ell", [("localized_hole.py", 254)], NO_O, NO_B, NO_E),
    (254, "Q3", "the bridge's minimal sphere is no static throat; a second exterior only in the eternal solution",
     [("localized_hole.py", 254)], C(O, "Dropped, as 270 and 282 require"), NO_B,
     C(E, "No slice crossing, bifurcation sphere")),
    (258, "Q1", "E's closed form needs c^6 (the code was right)", [("area_law5.py", 258)], NO_O, NO_B,
     N("C8 uses the computed E")),
    (258, "Q2", "the black string is a leading-order proxy for the large hole", [("area_law5.py", 258)], NO_O, NO_B,
     N("the small end only; the large end not claimed")),
    (261, "Q1-Q2", "the two-end construct's jump at the crossover; the switch a convention",
     [("corridor_family.py", 261)], NO_O, NO_B, N("the small end only")),
    (261, "Q3", "the large end: 4D Schwarzschild on the plane, kappa = 1/(4M), non-extremal",
     [("corridor_family.py", 261)], C(O, "261 (3)"), NO_B, N("the large end not claimed")),
    (264, "Q1", "S4 holds on reading (i) only, the hole standing through the write", [("write_small.py", 264)], NO_O,
     NO_B, C(E, "264 (1)")),
    (264, "Q2,Q5", "the variants fit at every Z only within H-SPECIES-FINITE", [("write_small.py", 264),
                                                                               ("hold_small.py", 264)],
     NO_O, NO_B, C(E, "317 (Q2)")),
    (264, "Q3,Q4,Q6", "the clock convention; one side's modes; item 262's range text", [("write_small.py", 264)], NO_O,
     NO_B, N("C8 uses the floor 66,980 at R1, not the variants")),
    (267, "Q1", "L1's integral; the radial fall r_h/(c(1 + E~))", [("hold_small.py", 267)], C(O, "r_h/(1 + E~)"), NO_B,
     NO_E),
    (267, "Q2-Q4", "greybody 0.93; brane dominance; life 8.57e14, 1.28e10 times the floor", [("hold_small.py", 267)],
     NO_O, NO_B, C(E, "1.28e10 times longer")),
    (267, "Q5", "eternal versus evaporating: the life is a collapse-formed hole's", [("d_evap.py", 267),
                                                                                    ("m1p2x_oneway.py", 267)],
     NO_O, NO_B, C(E, "i_oneway I5")),
    (267, "Q6", "the floor a lower bound: outliving it necessary, not sufficient", [("hold_small.py", 267)], NO_O, NO_B,
     C(E, "267 (6)")),
    (269, "Q1-Q5,Q8", "C4 two-way's flat-order and warp-order qualifications", [("m1_small.py", 269)], TWO_WAY, TWO_WAY,
     TWO_WAY),
    (269, "Q6", "(e)'s completeness is M's 259, not computed", [("m1_small.py", 269)],
     C(O, "Completeness there is M's ruling"), NO_B, NO_E),
    (269, "Q7", "(f) within one universe; the null energy +sigma sin a on crossing rays", [("m1_small.py", 269)], NO_O,
     C(B, "j_readings J2's sin a form"), NO_E),
    (269, "Q9", "N2 cited, not computed", [("m1_small.py", 269)], TWO_WAY, TWO_WAY, TWO_WAY),
    (271, "Q1,Q2,Q4-Q7,Q9", "C7 two-way's row qualifications", [("rows_small.py", 271)], TWO_WAY, TWO_WAY, TWO_WAY),
    (271, "Q3", "O2 false at both ends; the white-hole blueshift returns at kappa = c^2/r_h", [("rows_small.py", 271),
                                                                                              ("c_junction.py", 271)],
     N("O1c uses the face's causal reach for the reverse passage only"), NO_B, C(E, "319 (Q1)")),
    (271, "Q8", "G1s's value flips T3 and E3 at the small end", [("rows_small.py", 271)], NO_O, NO_B, NO_E),
    (281, "#6", "o1c_complete: completeness through the maximal extension (the reverse passage)",
     [("o1c_complete.py", 281)], C(O, "re-posed on the glued one-way object"), NO_B, NO_E),
    (281, "#7", "b5_positive B5a: the composite junction, position 2's tension in ours", [("b5_positive.py", 281)], NO_O,
     C(B, "One way, our side carries ours alone"), NO_E),
    (281, "marks", "m1p2x marks omit elements: m1p2x_sixth W2's \"falls through\"", [("m1p2x_sixth.py", 281)], NO_O,
     NO_B,
     C("m1p2x_oneway.py", "m1p2x_sixth W2's \"falls through\" is excluded")),
    (281, "outside", "e_positive: the static slab (E6, W5) and the summed-stress junction (W4)",
     [("e_positive.py", 281)],
     NO_O, C(B, "the summed stress S1 + S2"), C(E, "e_positive's row (+1, -1, 2, 2)")),
    (304, "Q1", "H7's continuation through the bridge is H4's dropped one", [("c1_oneway.py", 304)], NO_O, NO_B, NO_E),
    (304, "Q2", "two example holes for one README; 33.6 clocks at the small end's r_h", [("c1_oneway.py", 304)], NO_O,
     NO_B, C(E, "33.6 of its clocks")),
    (304, "Q3,Q4,Q6", "K7's overclaim; its read-back; the singular interior decides nothing",
     [("c1_oneway.py", 304), ("c4_oneway.py", 304)],
     C(O, "the quantum bounce's own row read back"), C(B, "the population's read-back"),
     C(E, "the populations read back at M's class")),
    (304, "Q5", "(B) at the bounce a reading; the inner horizon changes the exterior", [("c1_oneway.py", 304)], NO_O,
     NO_B, NO_E),
    (304, "Q7", "\"only through our future interior\" holds by construction", [("c1_oneway.py", 304)], NO_O, NO_B, NO_E),
    (304, "Q8", "the crossing below r_h/c; \"as long again out\" only if the bounce returns the Killing energy",
     [("c1_oneway.py", 304)], C(O, "finite affine parameter"), NO_B, NO_E),
    (304, "Q9", "K2 a deduction from c_junction J1", [("c1_oneway.py", 304)], NO_O, NO_B, C(E, "c_junction J4")),
    (304, "outside", "c_junction J1 uses m1p2x_fifth F1, let stand as outflow", [("c1_oneway.py", 304)], NO_O, NO_B,
     C(E, "m1p2x_fifth F1 as outflow")),
    (310, "Q1+critic", "the face a route leaves by; the README by position 2's face, on a quantum region of that kind",
     [("c4_residue.py", 310), ("c4_oneway.py", 310)], C(O, "c4_residue R13"), NO_B, C(E, "310 (ii)")),
    (310, "Q2", "R6 constructs less than the two-exterior bounce", [("c4_residue.py", 310)],
     C(O, "it does not model the README's route"), NO_B, NO_E),
    (310, "Q3", "position 2 reads its own mass (240); a common r_h assumed", [("c4_oneway.py", 310)],
     C(O, "under position 2's own laws Z2's bounds hold with its own r_h"), NO_B,
     C(E, "each plane reads its own horizon")),
    (310, "Q4", "R12's agreement is the entered value read back", [("c4_residue.py", 310)],
     C(O, "the quantum bounce's own row read back"), C(B, "the population's read-back"),
     C(E, "the populations read back at M's class")),
    (310, "Q5,Q6", "R4 (v) against R6; R5's inner horizon for charge only", [("c4_residue.py", 310)], NO_O, NO_B, NO_E),
    (310, "Q7", "the junction fixes position 2's side total S1 + 2 S2, not tau", [("tau_share.py", 310)],
     NO_O, C(B, "310 (7)"), C(E, "310 (7)")),
    (310, "Q8", "DeTurck-Kazdan is interior regularity; analyticity up to the brane cited, not checked",
     [("c4_oneway.py", 310)], NO_O, C(B, "deduced, for analytic data"), NO_E),
    (310, "Q9", "P18's normalization; R9's witnesses corrected", [("c4_residue.py", 310)], NO_O, NO_B,
     C(E, "c4_residue's F18")),
    (310, "Q10", "mutants not caught; checks tightened", [("c4_residue.py", 310)], NO_O, NO_B, NO_E),
    (310, "outside G5", "G5 under the 2 : 1 bulk is (3/2) G ell or G ell/2, not G ell",
     [("c7_oneway.py", 315)], C(O, "Item 330, accounting before verification"),
     N("B5a's figures are sigma's, independent of G5; E7's distance enters only as 'exceeds sigma/4'"),
     C(E, "2 : 1 bulk's G5 readings")),
    (310, "outside metric", "one surface carries one induced metric; T4's two Hubble rates forbidden",
     [("b5a_residue.py", 310)], NO_O, C(B, "one induced metric (310's note)"), C(E, "j_readings J1")),
    (310, "outside map", "b_bounce Q1's map fixes only U = V = 0 pointwise", [("b_bounce.py", 310)],
     C(O, "a board reading"), NO_B, C(E, "the gluing map forced on the one chart")),
    (317, "Q1", "the pairing withdrawn: Raychaudhuri makes every turned ray net negative", [("c5_oneway.py", 317),
                                                                                           ("i_oneway.py", 317)],
     C(O, "pair_math P2, P4"), NO_B, C(E, "pair_math P1-P4")),
    (317, "Q2", "the species cap is parametric", [("c5_oneway.py", 317)], NO_O, NO_B, C(E, "317 (Q2)")),
    (317, "Q3", "the README leaving as its own image is the construction's time symmetry", [("c5_oneway.py", 317)],
     C(O, "U12 (Q3)"), NO_B, C(E, "c5_oneway U12 (Q3)")),
    (317, "Q4", "the placements: the README within for at most its stay", [("c5_oneway.py", 317)], C(O, "U12 (Q4)"),
     NO_B, NO_E),
    (317, "Q5", "E~ >= 1 assumed; for E~ < 1 the advanced time grows as ln(1/E~)", [("c5_oneway.py", 317)],
     C(O, "Those entering by our face have E~ > 0"), NO_B, NO_E),
    (317, "Q6,Q9,Q10", "U7's read-back; the seed; the words under 198", [("c5_oneway.py", 317)], NO_O, NO_B, NO_E),
    (317, "Q7", "the gluing map forced on 270 (a)'s single chart", [("c5_oneway.py", 317)], C(O, "U12 (Q7)"), NO_B,
     C(E, "Q7: the gluing map")),
    (317, "Q8", "warp order enters at O(r_h/ell) = 8.0e-16", [("c5_oneway.py", 317)], C(O, "U12 (Q8)"), NO_B,
     C(E, "O(r_h/ell) = 8.0e-16")),
    (317, "outside", "the pairing's reach; C7's carry; 158 (2) against 163; the one-way test by region",
     [("c5_oneway.py", 317), ("b_bounce.py", 317)], NO_O, NO_B,
     N("(c) is the WRITE row's: C8's (d) compares the life with the floor, not the hold with the stay")),
    (319, "Q1", "the blueshift closure refuted; bounded over the face's open period (J5), under 240",
     [("c7_oneway.py", 319)], C(O, "c7_oneway V12 (Q1)"), NO_B, C(E, "319 (Q1)")),
    (319, "Q2", "the G5 readings: 33.47 and 33.83 clocks; the 4D-G readings as g^(2/3)", [("c7_oneway.py", 319)],
     C(O, "Item 330, accounting before verification"), NO_B, C(E, "319 (Q2)")),
    (319, "Q3", "position-2 statements are the construction's single chart", [("c7_oneway.py", 319)],
     C(O, "Item 319 (c7_oneway V12 (Q3))"), NO_B, C(E, "319 (Q3)")),
    (319, "Q4", "the T3/E3 flip asserted and disclaimed", [("c7_oneway.py", 319)], NO_O, NO_B, NO_E),
    (319, "Q5-Q7", "the matter-free equator a limit; the closing line; small corrections", [("c7_oneway.py", 319)],
     NO_O, NO_B, NO_E),
    (319, "outside", "pair_math: P0's attributions, P1's example, P2's 'keeps 183', P3 conditional, P4's name",
     [("pair_math.py", 319)], N("O1c takes P2 and P4's confinement, not P4's name"), NO_B,
     N("C8's (b) takes the confinement, not the name -- and P2's uncorrected wording, carried at 341 (Q9)")),
    # item 332: the C9 verifier's report (items 325-327)
    (332, "Q1", "alpha = 0 under M-ONE-LIGHT-CONE (328), not U6 alone; C0 and S0 splice U6",
     [("gb_cone.py", 332), ("relativity.py", 332), ("gb_alpha.py", 332), ("sgb_cone.py", 332),
      ("../bulk/bulkwarp.py", 332), ("p2_offset.py", 332)],
     C(O, "alpha = 0 stands under M-ONE-LIGHT-CONE (328)"), C(B, "alpha = 0 under M-ONE-LIGHT-CONE (328), so x+"),
     C(E, "alpha = 0 under M-ONE-LIGHT-CONE (328) (Q1)")),
    (332, "Q2", "CEMZ only for alpha >> l_P5^2, at tree level", [("gb_cone.py", 332)],
     N("O1c rests on C7 under 328, not on C6"), N("B5a rests on C7, not on C6"), N("C8 rests on C7, not on C6")),
    (332, "Q3", "C5's divisor zero at U4's endpoint; positive on the open range (C10)", [("gb_cone.py", 332)],
     NO_O, NO_B, NO_E),
    (332, "Q4", "the split on the families computed, generic per RTW", [("gb_cone.py", 332), ("relativity.py", 332),
                                                                       ("gb_alpha.py", 332)],
     C(O, "332 (Q4) does bear, on Z2b's item-328 counterfactual"), NO_B, NO_E),   # [item 337 (Q11)]
    (332, "Q5", "sgb: every f' != 0 where V(phi_0) = V'(phi_0) = 0", [("sgb_cone.py", 332), ("../../currency.py", 332),
                                                                     ("../../doors.py", 332)],
     NO_O, C(B, "sgb's potential condition (Q5) concerns the coupled scalar"), NO_E),
    (332, "Q6-Q7", "S3's sign a reflection; S1's cosmology blind to the Weyl part", [("sgb_cone.py", 332)],
     NO_O, N("B5a uses S2's minimal coupling, not S3 or S1's check"), NO_E),
    (332, "Q8", "gb_alpha B2-B5 an evaluation of definitions; B0's gloss of 226; B5 vacuous", [("gb_alpha.py", 332)],
     N("O1c takes alpha from C7"), N("B5a takes alpha from C7"), N("C8 takes alpha from C7")),
    (332, "Q9", "minor: C8's crossing remark, RTW section 3.1, the symmetry of omega", [("gb_cone.py", 332),
                                                                                       ("sgb_cone.py", 332)],
     NO_O, NO_B, NO_E),
    # item 337: the O1c verifier's report
    (337, "Q1", "the faces' own generators not covered: listed as not claimed; CLOSEs and c1_oneway K2 end them",
     [("o1c_oneway.py", 337)], C(O, "The faces' own null generators (E~ = 0, on U = 0 and U' = 0)"),
     N("B5a does not use the faces' generators"), N("C8 does not use the faces' generators")),
    (337, "Q2, Q7, Q8", "Z2b's READs two-way, the shell a reading, the shell's own generators", [("o1c_oneway.py", 337)],
     C(O, "Item 337 (Z8 (Q2), (Q7), (Q8))"), NO_B, NO_E),
    (337, "Q3, Q4", "classical GR given up inside the region; exact at the two-derivative order",
     [("o1c_oneway.py", 337), ("b5a_residue.py", 337), ("c8_level.py", 337)], C(O, "Item 337 (Z8 (Q3), (Q4))"),
     C(B, "the O1c verifier's (Q4), accounted before the next verification"),
     C(E, "the O1c verifier's (Q4), accounted before the next verification")),
    (337, "Q5, Q6", "the 320 note overstated; Z6's readings named", [("o1c_oneway.py", 337)],
     C(O, "Item 337 (Z8 (Q5))"), N("B5a's 320 reading is b5a_residue A3's, not O1c's note"), NO_E),
    (337, "Q9-Q11", "Z0's attribution; R6's one r_h; 332 (Q4) on Z2b", [("o1c_oneway.py", 337)],
     C(O, "Item 337 (Z8 (Q10))"), NO_B, NO_E),
    (337, "outside", "c4_residue R6's sample point; Z7's audit on one coding; 336 bears on (Q1)",
     [("o1c_oneway.py", 337)], C(O, "Item 337 (outside)"), NO_B, NO_E),
    # item 339: the B5a verifier's report
    (339, "Q1", "the crossing share's citation: m1p2x_sixth W1 and c4_oneway P4, not j_readings J2",
     [("b5a_residue.py", 339), ("b5a_oneway.py", 339)], N("O1c verified at 337; it uses no crossing share"),
     C(B, "(Q1) \"j_readings J2's sin a form\" is a wrong citation"),
     N("C8 cites m1p2x_index Y1 and b5a_residue A1, not J2's form")),
    (339, "Q2", "A1's 'part only in how position 2's matter is counted' false as worded", [("b5a_residue.py", 339)],
     NO_O, C(B, "Item 339 (the B5a verifier's (Q2))"),
     N("C8 uses A1's side total on tensions alone, where the readings agree")),
    (339, "Q3", "-sigma/6 the strictest of the four bounds, not the weakest", [("b5a_residue.py", 339)], NO_O,
     C(B, "(Q3) -sigma/6 is the strictest of the four bounds"), NO_E),
    (339, "Q4", "rho >= 0 relative to the offset inside its vacuum's basin; classical, quantum read under 120",
     [("b5a_residue.py", 339), ("pointwise.py", 339), ("c8_level.py", 339)],
     N("O1c verified at 337; its 320 note corrected there (Q5)"),
     C(B, "(Q4) \"Both are proved ... rho >= 0 above the vacuum\" claims more than pointwise proves"),
     C(E, "Item 339 (the B5a verifier's (Q4), (Q6), accounted before the next verification, 330)")),
    (339, "Q5", "A5's dependencies unnamed (residue, 314); one kappa unstated -- A6: none needed",
     [("b5a_residue.py", 339), ("c8_level.py", 339), ("p2_offset.py", 339)], N("O1c verified at 337; no junction"),
     C(B, "A6 (item 339 (Q5); computed, exact"),
     C(E, "Item 339 (the B5a verifier's (Q5)): the side total S1 + 2 S2 needs no single five-dimensional coupling")),
    (339, "Q6", "E7's wording stale under 336; its figure under the G5 readings",
     [("b5a_residue.py", 339), ("b5a_oneway.py", 339), ("c8_level.py", 339)], N("O1c verified at 337; E7 not used"),
     C("b5a_oneway.py", "(Q6) Since item 336 (M-ENERGY-STAYS)"), C(E, "so \"the README supplies it\" is stale wording")),
    (339, "Q7", "x+ the quadratic's root, its series truncated; 'exactly' on Lovelock's premises",
     [("b5a_residue.py", 339), ("p2_offset.py", 339), ("c8_level.py", 339)], NO_O,
     C(B, "(Q7) x+ is the root of the quadratic"), C(E, "Item 339 (the B5a verifier's (Q7) and its note outside B5a)")),
    (339, "Q8", "'read-back at M's class' imprecise: 1 in 60/96, refused in 36/96 with every language",
     [("b5a_residue.py", 339), ("c8_level.py", 339)], NO_O, C(B, "Item 339 (the B5a verifier's (Q8))"),
     C(E, "Item 339 (the B5a verifier's (Q8), carried since V8 uses the same words)")),
    (339, "Q9", "record pointers: b5a_oneway's notes; 'direction-neutral' the board's own; a does-not superseded",
     [("b5a_residue.py", 339), ("b5a_oneway.py", 339)], NO_O,
     C("b5a_oneway.py", "(Q9) B3's \"direction-neutral (the auditing agent's note)\""), NO_E),
    (339, "outside", "p2_assume Q5 / p2_offset V5: C1's constancy omits the bulk's normal stress; QUEUED's scope",
     [("p2_assume.py", 339), ("p2_offset.py", 339), ("verify_ledger.py", 339)], NO_O,
     N("B5a's A3 computes C2 - C1 and names the non-vacuum case; it does not take C1 constant"),
     C(E, "p2_assume Q5's \"C1 is constant\" omits")),
    # item 341: the C8 verifier's report
    (341, "Q1", "V5 (d)'s reading-(i) condition dropped in V9; (d) on reading (ii) since 340", [("c8_level.py", 341)],
     NO_O, NO_B, C(E, "(Q1) \"every owed item closed one-way (V5)\" drops (d)'s condition")),
    (341, "Q2", "V9's rests-on incomplete (residue, 314)", [("c8_level.py", 341)], NO_O, NO_B,
     C(E, "(Q2) The row rests also on 226 with M-P2-OWN-G (330)")),
    (341, "Q3", "V5 (a) on J5 and J2, marked two-way at 277, re-admitted at 319; Barcelo's threshold at the face",
     [("c8_level.py", 341), ("c_junction.py", 341)], N("O1c verified at 337; it uses no white-hole bound"), NO_B,
     C(E, "(a) (Q3): its bound comes from c_junction J5")),
    (341, "Q4", "the G5-reading figures under two conventions for sigma", [("c8_level.py", 341), ("c7_oneway.py", 341)],
     NO_O, N("B5a's E7 figures are V1's sigma-fixed convention, consistent"), C(E, "V10 (item 341; computed)")),
    (341, "Q5", "V8's item-339 note: for z_net the read-back is the m = 1 column", [("c8_level.py", 341)], NO_O,
     N("B5a's A4 population is fixed by its t = 1 row, so its item-339 note stands"),
     C(E, "Item 341 (Q5): the item-339 note's")),
    (341, "Q6", "the quadratic's root: d1/2 - 2.79e-72 J/m^3, not 1.9e-69",
     [("c8_level.py", 341), ("b5a_residue.py", 341), ("p2_offset.py", 341)], NO_O,
     C(B, "Item 341 (the C8 verifier's (Q6), outside C8)"), C(E, "Item 341 (Q6): the item-339 note's")),
    (341, "Q7", "V4's 'no past interior' overstated: none facing us", [("c8_level.py", 341)], NO_O, NO_B,
     C(E, "Item 341 (Q7)")),
    (341, "Q8", "stale wording in V5 (e) and V9 since 336", [("c8_level.py", 341)], NO_O, NO_B,
     C(E, "(Q8) \"the README ... carrying it past sigma/4\" is stale since 336")),
    (341, "Q9", "V5 (b)'s 'every classical ray keeping 183', pair_math P2's uncorrected wording", [("c8_level.py", 341)],
     N("O1c takes P2 and P4's confinement"), NO_B, C(E, "(b) (Q9): \"every classical ray keeping 183\"")),
    (341, "Q10", "minor pointers: 319 (Q2), 240, 336 (a), V7's pointwise scope, H-ASYMMETRIC-BOUNCE",
     [("c8_level.py", 341)], NO_O, NO_B, C(E, "Item 341 (Q10): \"each plane reads its own horizon\"")),
    (341, "outside", "338 and 340 on V5 (d); the G5 convention in c7_oneway; 1.9e-69 in three notes; the owed notes",
     [("c7_oneway.py", 341), ("p2_offset.py", 341), ("b5a_residue.py", 341), ("c_junction.py", 338),
      ("write_small.py", 338), ("hold_small.py", 338)], NO_O, C(B, "Item 341 (the C8 verifier's (Q6), outside C8)"),
     C(E, "(d) (Q1): closed on reading (i), as stated; and since item 340")),
    # item 348: the ARRIVAL verifier's report
    (348, "Q1", "V11 (b)'s censorship refuted at order 4: the onset's rays escape along the trapping horizon",
     [("arrival_small.py", 348)], NO_O, NO_B, NO_E),
    (348, "Q2", "V12 (b)-(c): V8 (1), (3) use the model's 4.79; the one E only for a lossless collapse",
     [("arrival_small.py", 348)], NO_O, NO_B, NO_E),
    (348, "Q3", "V2-V4's figures belong to an event horizon presumed static from v = w", [("arrival_small.py", 348)],
     NO_O, NO_B, NO_E),
    (348, "Q4", "V9's 96/96 the statistics-rank protocol; with every language 1 in 60/96, refused 36",
     [("arrival_small.py", 348), ("verify_ledger.py", 348)], NO_O, NO_B,
     C(E, "and z_net each come back 1 in 60 of 96 codings and refused in 36")),
    (348, "Q5", "the rests-on: 270 (a), 273 (a), 336 (a), 320 (b)-(c), J1's use of F1; two ledger markers",
     [("arrival_small.py", 348), ("verify_ledger.py", 348)], NO_O, NO_B, C(E, "m1p2x_fifth F1 as outflow")),
    (348, "Q6", "J1 at our face's r_h, not each destination's; the G5 readings of r_h/ell and R/ell",
     [("arrival_small.py", 348), ("c8_level.py", 348)], NO_O, NO_B, C(E, "Item 348 (Q6), outside C8")),
    (348, "Q7-Q10", "158 (2) consonant; Bousso's (2.22) premises; the coarse count's integrated form; 109",
     [("arrival_small.py", 348)], NO_O, NO_B, NO_E),
    (348, "Q11", "minor: two board passages as quotations; w = 8; the (310, Q2) reason; S3's list; the fine count",
     [("arrival_small.py", 348), ("verify_ledger.py", 348)], NO_O, NO_B, NO_E),
    (348, "outside", "README-HELD's profile artefact; the item-346 note; L2 tests a marker, not its substance",
     [("README-HELD.md", 348), ("arrival_small.py", 346), ("verify_ledger.py", 348)], NO_O, NO_B, NO_E),
]
# [Item 344] ARRIVAL queued -- M: "ARRIVAL is ready for the verifier" -- and accounted against every row, beside the
# record's three columns (O1c, B5a and C8, verified at 337, 339 and 341): carried, with its marker in arrival_small, or
# not bearing, with the reason
A = "arrival_small.py"
NO_A = N("not used by ARRIVAL")
QUEUED_FILES["ARRIVAL"] = (A,)
ARRIVAL_BEAR = {
    (254, "Q1"): N("ARRIVAL computes the bulk's G_vv about the hole (V1), not the plane's tangential reading"),
    (254, "Q2"): N("ARRIVAL works at r ~ r_h, the Tangherlini region, and uses no 1/r^2 pull"),
    (254, "Q3"): N("ARRIVAL's hole is formed by the arrival (V1-V2): no bridge, no second exterior; the passage is the "
                   "bounce's (273; O1c, 337)"),
    (258, "Q1"): N("ARRIVAL takes E from close_small K4's identity (V1)"),
    (258, "Q2"): N("the small end only"),
    (261, "Q1-Q2"): N("the small end only"),
    (261, "Q3"): N("the large end not claimed"),
    (264, "Q1"): C(A, "the README crossing it (S4; 264)"),
    (264, "Q2,Q5"): N("ARRIVAL carries S3's floor at Z = 106.75, not the variants"),
    (264, "Q3,Q4,Q6"): N("ARRIVAL counts in clocks of r_h/c and takes S3's floor at R1 (C2's count, named in S3), as C8 "
                         "does -- not the variants, not the large end's m/c"),
    (267, "Q1"): N("ARRIVAL takes the fall within a clock (hold_small L1), which r_h/(c(1 + E~)) meets for every "
                   "E~ >= 0"),
    (267, "Q2-Q4"): N("ARRIVAL uses no greybody factor and no life figure"),
    (267, "Q5"): N("ARRIVAL's hole is collapse-formed by construction: the arrival forms it (V1-V2)"),
    (267, "Q6"): C(A, "The floor is the write's least time (267 (Q6))"),
    (269, "Q1-Q5,Q8"): TWO_WAY,
    (269, "Q6"): N("ARRIVAL claims no completeness; it rests on O1c's (337)"),
    (269, "Q7"): N("ARRIVAL's null energy is the bulk's G_vv about the hole, not a plane-crossing ray's"),
    (269, "Q9"): TWO_WAY,
    (271, "Q1,Q2,Q4-Q7,Q9"): TWO_WAY,
    (271, "Q3"): N("ARRIVAL takes J1's open period, computed on kappa = c^2/r_h, and no blueshift bound"),
    (271, "Q8"): N("ARRIVAL uses neither T3 nor E3"),
    (281, "#6"): N("ARRIVAL rests on O1c one-way (337), not o1c_complete"),
    (281, "#7"): N("ARRIVAL rests on B5a one-way (339), its side total by A6"),
    (281, "marks"): N("ARRIVAL cites m1p2x_oneway O4, which excludes m1p2x_sixth W2's \"falls through\""),
    (281, "outside"): N("ARRIVAL uses no slab and no junction stress"),
    (304, "Q1"): N("ARRIVAL uses no continuation through a bridge"),
    (304, "Q2"): C(A, "33.6 of its clocks"),
    (304, "Q3,Q4,Q6"): C(A, "the 1s add nothing to V1-V3"),
    (304, "Q5"): N("ARRIVAL uses neither (B) at the bounce nor an inner horizon"),
    (304, "Q7"): N("ARRIVAL makes no \"only through our future interior\" claim"),
    (304, "Q8"): C(A, "even a bounce that kept the span would fit it"),
    (304, "Q9"): N("ARRIVAL cites c_junction J1 directly, not K2"),
    (304, "outside"): C(A, "c_junction J1's use of m1p2x_fifth F1 as outflow (304, outside)"),   # [item 348 (Q5)]
    (310, "Q1+critic"): N("ARRIVAL takes the README's route from O1c and C8 (337, 341), which carry 310 (Q1)"),
    (310, "Q2"): N("V6 cites 337 (Q10), R6's one r_h, for its one-r_h reading; R6 constructing less than the "
                   "two-exterior bounce moves no ARRIVAL figure (item 348 (Q11))"),
    (310, "Q3"): C(A, "240 governs"),
    (310, "Q4"): C(A, "the 1s add nothing to V1-V3"),
    (310, "Q5,Q6"): N("ARRIVAL uses neither R4 nor R5"),
    (310, "Q7"): N("ARRIVAL uses no tau"),
    (310, "Q8"): N("ARRIVAL cites no DeTurck-Kazdan step"),
    (310, "Q9"): N("ARRIVAL calls c4_residue's calculator, corrected there"),
    (310, "Q10"): N("c4_residue's mutants, tightened there"),
    (310, "outside G5"): C(A, "9.18e-16 and 6.37e-16 under the G5 readings"),          # [item 348 (Q6)]
    (310, "outside metric"): N("ARRIVAL uses no plane's induced metric"),
    (310, "outside map"): C(A, "the glued object read as one Kruskal geometry"),
    (317, "Q1"): N("ARRIVAL has no pairing: mu' >= 0, nothing to pair (V1)"),
    (317, "Q2"): N("ARRIVAL quotes the floor at Z = 106.75 and uses no species cap"),
    (317, "Q3"): C(A, "c5_oneway U12 (Q3)"),
    (317, "Q4"): N("ARRIVAL places nothing within the horizon beyond its fall, within a clock (V8 (1))"),
    (317, "Q5"): N("ARRIVAL uses no advanced time; its fall is hold_small L1's, at most r_h/c for every E~ >= 0"),
    (317, "Q6,Q9,Q10"): C(A, "\"My guess would be 1.\" (the board's option (a)"),
    (317, "Q7"): C(A, "the isometric gluing is the case G5_2 = G5"),
    (317, "Q8"): C(A, "first order and not its square (317 (Q8))"),
    (317, "outside"): C(A, "M-HOLD-IS-THE-FACE's core"),
    (319, "Q1"): N("ARRIVAL uses no white-hole blueshift bound"),
    (319, "Q2"): C(A, "(319 (Q2), 341 (Q4); c8_level V10)"),
    (319, "Q3"): C(A, "one r_h for both faces"),
    (319, "Q4"): N("ARRIVAL uses neither T3 nor E3"),
    (319, "Q5-Q7"): N("ARRIVAL uses no matter-free equator and no C7 closing line"),
    (319, "outside"): N("ARRIVAL uses no pair_math attribution or example: no pairing (V1)"),
    (332, "Q1"): C(A, "zero under M-ONE-LIGHT-CONE (328; 332 (Q1))"),
    (332, "Q2"): N("ARRIVAL rests on 328 (V13 (3)), not on C6"),
    (332, "Q3"): NO_A,
    (332, "Q4"): NO_A,
    (332, "Q5"): N("ARRIVAL has no coupled scalar"),
    (332, "Q6-Q7"): NO_A,
    (332, "Q8"): N("ARRIVAL takes the coupling zero from 328, not from gb_alpha"),
    (332, "Q9"): NO_A,
    (337, "Q1"): N("ARRIVAL traces the face's generators itself (V2), not through O1c's completeness"),
    (337, "Q2, Q7, Q8"): N("ARRIVAL uses no Z2b READ and no shell"),
    (337, "Q3, Q4"): C(A, "the results exact at that order (337 (Q4))"),
    (337, "Q5, Q6"): C(A, "V1-V5 an empty bulk apart from the README, the board's limit"),   # [item 348 (Q5)]
    (337, "Q9-Q11"): C(A, "337 (Q10)"),
    (337, "outside"): C(A, "as O1c's Z7 did (337, outside)"),
    (339, "Q1"): N("ARRIVAL uses no crossing share"),
    (339, "Q2"): N("ARRIVAL cites A6, not A1's wording"),
    (339, "Q3"): NO_A,
    (339, "Q4"): C(A, "339 (Q4)'s scope"),
    (339, "Q5"): C(A, "(b5a_residue A6, 339 (Q5))"),
    (339, "Q6"): N("ARRIVAL uses no E7"),
    (339, "Q7"): N("ARRIVAL uses no x+"),
    (339, "Q8"): C(A, "f2 for the compact README are 1 in 60/96 and refused in 36"),         # [item 348 (Q4)]
    (339, "Q9"): NO_A,
    (339, "outside"): N("ARRIVAL takes no constancy of C1"),
    (341, "Q1"): N("ARRIVAL is where 340 is worked (V11); C8's V5 (d) carries it"),
    (341, "Q2"): C(A, "341 (Q2)'s finding for C8 holds here too"),
    (341, "Q3"): N("ARRIVAL uses J1 only, not J5 or J2"),
    (341, "Q4"): C(A, "33.06 and 34.53 with sigma fixed"),
    (341, "Q5"): NO_A,
    (341, "Q6"): N("ARRIVAL uses no x+"),
    (341, "Q7"): N("ARRIVAL makes no past-interior claim"),
    (341, "Q8"): N("ARRIVAL carries no \"past sigma/4\" wording"),
    (341, "Q9"): N("ARRIVAL calls on no 183 pairing: nothing to pair (V1)"),
    (341, "Q10"): C(A, "(5) uses the board's 336 (a), named at 341 (Q10)"),                    # [item 348 (Q5)]
    (341, "outside"): N("the notes owed to ARRIVAL since 338 are seated outside it (c_junction J3, write_small S4, "
                        "hold_small L4); the G5 convention is carried at (Q4)"),
    # [item 348] ARRIVAL's own report, each carried in arrival_small
    (348, "Q1"): C(A, "is REFUTED at order 4"),
    (348, "Q2"): C(A, "carries for a lossless collapse"),
    (348, "Q3"): C(A, "presume the face static from v = w on"),
    (348, "Q4"): C(A, "the 96/96 is the statistics-rank protocol"),
    (348, "Q5"): C(A, "the row rests also on the board's readings 270 (a)"),
    (348, "Q6"): C(A, "32.60-34.53 of position 2's clocks"),
    (348, "Q7-Q10"): C(A, "158 (2) is consonant, not a premise"),
    (348, "Q11"): C(A, "is the grid's first point above 5.27 and 4.79"),
    (348, "outside"): C(A, "the model ARRIVALs uses stands in for SOURCEs"),
}
# [Item 351] FAR at both ends queued -- M: "FAR both ends is now ready for the verifier." -- and accounted against every
# row: carried, with its marker in far_small or far_large, or not bearing, with the reason
FS_, FL_ = "far_small.py", "far_large.py"
NO_F = N("not used by FAR")
QUEUED_FILES["FAR"] = (FS_, FL_)
FAR_BEAR = {
    (254, "Q1"): N("FAR's (Z) is each side's R(k, k) = 0 and the crossing ray's surface stress (F6), not the plane's 4D "
                   "reading of the Weyl term"),
    (254, "Q2"): C(FS_, "Q2: the 1/r^2 pull for r_h << r << ell"),
    (254, "Q3"): N("FAR's hole is the glued one-way object's, its faces each side's own (F4, F10 (k)): no static "
                   "throat, no eternal second exterior"),
    (258, "Q1"): N("FAR takes r_h from C2's count and m from the identity (3 pi/8)(r_h/ell) r_h (F5 (c)), no closed "
                   "form of E"),
    (258, "Q2"): C(FL_, "the horizon is pancake-like"),
    (261, "Q1-Q2"): C(FL_, "is the two-end construct's switch, a convention"),
    (261, "Q3"): C(FL_, "C3 F5, verified 261"),
    (264, "Q1"): N("FAR takes write_small S3's floor and weak field, not S4"),
    (264, "Q2,Q5"): N("FAR takes S3's head floor at Z = 106.75 for its cover, not the variants"),
    (264, "Q3,Q4,Q6"): N("FAR counts its cover in clocks of r_h/c with S3's floor at R1 (F4, F9 (c)), the large end's "
                         "in clocks of m/c (o3_write), and uses neither one side's modes nor 262's range"),
    (267, "Q1"): N("FAR uses no fall time"),
    (267, "Q2-Q4"): C(FS_, "(267's brane dominance)"),
    (267, "Q5"): C(FS_, "ingoing (the arrival, arrival_small V1) or outgoing (the emission, 336)"),
    (267, "Q6"): C(FS_, "267 (Q6): the floor is the write's least time"),
    (269, "Q1-Q5,Q8"): TWO_WAY,
    (269, "Q6"): N("FAR claims no completeness"),
    (269, "Q7"): N("FAR takes the crossing ray's null energy from b5a_residue A2 (B5a verified, 339), not m1_small "
                   "(f)'s one-universe form"),
    (269, "Q9"): TWO_WAY,
    (271, "Q1,Q2,Q4-Q7,Q9"): TWO_WAY,
    (271, "Q3"): C(FS_, "position 2's face is a white-hole face with kappa = c^2/r_h"),
    (271, "Q8"): N("FAR uses neither T3 nor E3"),
    (281, "#6"): N("FAR does not rest on o1c_complete"),
    (281, "#7"): C(FS_, "our side Sigma^- = S1, position 2's Sigma^+ = S1 + 2 S2"),
    (281, "marks"): N("FAR cites no m1p2x instrument"),
    (281, "outside"): C(FS_, "the slab exists nowhere (275 (a))"),
    (304, "Q1"): N("FAR uses no continuation through a bridge"),
    (304, "Q2"): N("FAR uses one hole, C2's R1 r_h (F4: U = 140,660 r_h = 1.58e-15 m), not H6's"),
    (304, "Q3,Q4,Q6"): C(FS_, "The calculator classifies, it does not derive"),
    (304, "Q5"): N("FAR uses neither (B) at the bounce nor an inner horizon"),
    (304, "Q7"): N("FAR makes no \"only through our future interior\" claim"),
    (304, "Q8"): N("FAR uses no crossing time"),
    (304, "Q9"): N("FAR cites no K2"),
    (304, "outside"): C(FS_, "names the potential's fall-off"),
    (310, "Q1+critic"): N("FAR traces no route through the faces; T_E lies outside both"),
    (310, "Q2"): N("FAR uses no R6"),
    (310, "Q3"): C(FS_, "position 2 reads its own mass (240)"),
    (310, "Q4"): C(FS_, "so the 1 is forced and void as evidence"),
    (310, "Q5,Q6"): N("FAR uses neither R4 nor R5"),
    (310, "Q7"): C(FS_, "position 2's Sigma^+ = S1 + 2 S2"),
    (310, "Q8"): N("FAR cites no DeTurck-Kazdan step"),
    (310, "Q9"): N("FAR uses no P18 density and no R9 witness"),
    (310, "Q10"): N("FAR calls c4_residue's calculator, its mutants tightened there"),
    (310, "outside G5"): C(FS_, "U/ell moves as g^(1/3), to 1.29e-10 and 8.95e-11"),
    (310, "outside metric"): C(FS_, "the pair is curved (B5a's offset)"),
    (310, "outside map"): N("FAR uses no gluing map: its two sides are the coincident pair's (275)"),
    (317, "Q1"): N("FAR uses no pairing; a ray meeting the corridor is Z3bs's reading of 318 (F6)"),
    (317, "Q2"): N("FAR uses no species cap and no life figure"),
    (317, "Q3"): C(FS_, "neither is spherical"),
    (317, "Q4"): C(FS_, "so mu <= r_h^2 at every stage"),
    (317, "Q5"): N("FAR uses no advanced time"),
    (317, "Q6,Q9,Q10"): N("FAR quotes no 198 option text and uses no U7 or U10; its own read-back is F7's f2, flagged "
                          "void"),
    (317, "Q7"): N("FAR uses no gluing map; its position-2 mu is arrival_small V6's readings (verified, 348)"),
    (317, "Q8"): C(FS_, "warp order enters the hole's near field at first order in rho/ell"),
    (317, "outside"): N("(c) is the WRITE row's; FAR uses no pairing and no one-way test by point"),
    (319, "Q1"): C(FS_, "bounded over the face's open period by c_junction J5"),
    (319, "Q2"): C(FS_, "the G5 readings move it by a factor of order one"),
    (319, "Q3"): C(FS_, "within V6's readings r_h^2 to 4^(2/3)"),
    (319, "Q4"): N("FAR uses neither T3 nor E3"),
    (319, "Q5-Q7"): C(FS_, "the sheets carry our plane's dark energy beside the tension"),
    (319, "outside"): N("FAR uses no pair_math"),
    (332, "Q1"): C(FS_, "328 and B8 (each side Einstein, the Gauss-Bonnet coupling zero)"),
    (332, "Q2"): N("FAR rests on B8 under 328 (C7, C10), not on C6"),
    (332, "Q3"): NO_F,
    (332, "Q4"): NO_F,
    (332, "Q5"): N("FAR has no coupled scalar"),
    (332, "Q6-Q7"): NO_F,
    (332, "Q8"): C(FS_, "is the board's reading of M's words, as gb_alpha B0's was"),
    (332, "Q9"): NO_F,
    (337, "Q1"): N("FAR's surfaces lie outside both faces, whose generators are CLOSE's and position 2's (337 (Q1))"),
    (337, "Q2, Q7, Q8"): N("FAR uses no Z2b READ and no shell; its arrival is arrival_small V1's model, its "
                           "non-spherical part F5 (b)'s"),
    (337, "Q3, Q4"): C(FS_, "holds on Lovelock's premises, at the two-derivative order"),
    (337, "Q5, Q6"): C(FS_, "with the bulk's content F5 (d)'s criterion governs"),
    (337, "Q9-Q11"): C(FS_, "F0's 273 and 275 are the options M chose"),
    (337, "outside"): C(FS_, "its index flagged under all 96 codings"),
    (339, "Q1"): N("FAR uses no crossing share"),
    (339, "Q2"): N("FAR uses A1's side totals on tensions (F2), where the readings agree, and A2's summed stress for "
                   "matter (F6)"),
    (339, "Q3"): N("FAR uses no bound list"),
    (339, "Q4"): C(FS_, "the quantum case read under 120 (339 (Q4))"),
    (339, "Q5"): C(FS_, "kappa+ its own coupling (b5a_residue A6)"),
    (339, "Q6"): N("FAR uses no E7"),
    (339, "Q7"): N("FAR uses no x+"),
    (339, "Q8"): C(FS_, "with every language seeing every condition (348 (Q4))"),
    (339, "Q9"): NO_F,
    (339, "outside"): N("FAR takes no constancy of C1"),
    (341, "Q1"): N("FAR uses no V5 (d)"),
    (341, "Q2"): C(FS_, "M-P2-OWN-G (330) with 226"),
    (341, "Q3"): C(FS_, "Barcelo's threshold read at the face (341 (Q3))"),
    (341, "Q4"): C(FS_, "hold under both conventions for sigma"),
    (341, "Q5"): N("FAR's f1 and f2 populations are F7's own, not V8's columns"),
    (341, "Q6"): N("FAR uses no x+"),
    (341, "Q7"): N("FAR makes no past-interior claim"),
    (341, "Q8"): N("FAR was written after 336 and carries its wording (F1, F5 (a))"),
    (341, "Q9"): N("FAR says a corridor-meeting ray keeps (Z) on Z3bs's reading of 318 (F6), not pair_math P2's "
                   "\"keeps 183\""),
    (341, "Q10"): C(FS_, "336 (a) (position 2's energy its own)"),
    (341, "outside"): N("the notes owed since 338 sit outside FAR; the G5 convention is carried at (Q4)"),
    (348, "Q1"): N("FAR claims no censorship (F9 (k)); the onset's rays escape at r^2 ~ mu, inside every T_E, and F5 "
                   "(a)'s mu <= r_h^2 bounds T_E through it"),
    (348, "Q2"): C(FS_, "arrival_small's one E holds for a lossless collapse"),
    (348, "Q3"): N("FAR takes arrival_small V1 and V6, not V2-V4's figures"),
    (348, "Q4"): C(FS_, "Those counts are the statistics-rank protocol"),
    (348, "Q5"): C(FS_, "270 (a) (the one object's two faces"),
    (348, "Q6"): C(FS_, "Position 2's side carries its own face's mu"),
    (348, "Q7-Q10"): N("FAR uses no 158 (2), no Bousso bound, no coarse count and no 109"),
    (348, "Q11"): C(FS_, "F0's words are checked inside the item each is cited to"),
    (348, "outside"): N("FAR uses no README-HELD profile; the ledger's limit, a marker and not its substance, "
                        "stands for this gate too"),
}
OUTSIDE_QUEUE = [
    ("271 (3)", "the rows resting on kappa = 0: stability S5b, o3_hold O3c, write_cypher W4",
     [("o3_hold.py", 281), ("write_cypher.py", 281)]),
    ("271 (8), 319 (Q4)", "T3's and E3's flip at the small end", [("rows_small.py", 271)]),
    ("317 outside (c)", "the WRITE row: 158 (2) against 163 within a horizon", [("c5_oneway.py", 317)]),
]
# [Item 331] each brought current: (label, what, [(file, item)] where the current statement is written)
BROUGHT_CURRENT = [
    ("271 (3)", "stability S6, o3_hold O3e, write_cypher W5: the corridor's own non-extremal horizon",
     [("../bulk/stability.py", 331), ("o3_hold.py", 331), ("write_cypher.py", 331), ("close_object.py", 331)]),
    ("271 (8), 319 (Q4)", "ledger E3s, warptheorem T3s: the small end's ledger",
     [("ledger.py", 331), ("../warptheorem.py", 331)]),
    ("317 outside (c)", "write_cypher W5 (b): H-HOLD-IS-THE-FACE, put to M; confirmed, M-HOLD-IS-THE-FACE (334)",
     [("write_cypher.py", 331), ("write_cypher.py", 334)]),
]
STALE_REGISTER = [            # unmarked, found by this ledger: (file, stale text still present)
    (os.path.join(D68, "warptheorem.py"), "O2 the horizon is extremal (surface gravity 0)"),
    (os.path.join(D68, "WARPTHEOREM.md"), "O2 the horizon is extremal (surface gravity 0)"),
    (os.path.join(D68, "WARPTHEOREM.md"), "O1c geodesic completeness | proved | M1 | o1c_complete.py"),
]
# [Item 331] the stale texts stay as the record (LEMMAS, the item-247 head); the register's current statement must be
# present beside them
CURRENT_REGISTER = [
    (os.path.join(D68, "warptheorem.py"), "LEMMAS_NOW = ["),
    (os.path.join(D68, "warptheorem.py"), "O2 the horizon is not extremal: surface gravity c^2/r_h at the small end"),
    (os.path.join(D68, "WARPTHEOREM.md"), "## The register as it stands (item 331)"),
    (os.path.join(D68, "WARPTHEOREM.md"), "| O | O2 the horizon is not extremal: surface gravity c^2/r_h at the small"),
    (os.path.join(D68, "WARPTHEOREM.md"), "| O | O1cs every causal route of the passage complete at the small end |"),
]


def has_item(path, n):
    txt = open(path, encoding="utf-8").read()
    return re.search(r"[Ii]tem[- ]%d\b" % n, txt) is not None


def has_text(path, s):
    norm = lambda x: " ".join(x.split())
    return norm(s) in norm(open(path, encoding="utf-8").read())


def compute():
    rows = list(ROWS)
    if MUT.get("c8_stale"):
        rows = [r if not (r[0] == 319 and r[1] == "Q1") else r[:6] + (C(E, "the blueshift excluded by causal reach"),)
                for r in rows]
    if MUT.get("outstanding"):
        rows = rows + [(319, "Qx", "an uncarried correction", [("c7_oneway.py", 319)], NO_O, NO_B,
                        ("outstanding", "not carried"))]
    seated, carried, outstanding = [], [], []
    abear = dict(ARRIVAL_BEAR)                                      # [item 344] the queued ARRIVAL's column
    if MUT.get("arrival_stale"):
        abear[(341, "Q4")] = C(A, "33.6 clocks on every reading")          # the mutant: the G5 readings not carried
    if MUT.get("arrival_unaccounted"):
        del abear[(267, "Q6")]                                             # the mutant: a row left unaccounted
    fbear = dict(FAR_BEAR)                                          # [item 351] the queued FAR's column
    if MUT.get("far_stale"):
        fbear[(341, "Q4")] = C(FS_, "under one convention for sigma only")  # the mutant: 341 (Q4) not carried
    if MUT.get("far_unaccounted"):
        del fbear[(271, "Q3")]                                             # the mutant: a row left unaccounted
    for rep, q, gist, seats, *bear in rows:
        for f, n in seats:
            item = n if not MUT.get("wrong_item") else n + 1000
            seated.append(((rep, q), f, item, has_item(os.path.join(HERE, f), item)))
        for obj, b in list(zip(QUEUED, bear)) + [("ARRIVAL", abear.get((rep, q), ("outstanding", "not accounted"))),
                                                  ("FAR", fbear.get((rep, q), ("outstanding", "not accounted")))]:
            if b[0] == "carried":
                # [item 339] the marker must sit in one of the object's own files (QUEUED_FILES)
                carried.append(((rep, q), obj, b[1], b[2], has_text(os.path.join(HERE, b[1]), b[2])
                                and b[1] in QUEUED_FILES[obj]))
            elif b[0] == "outstanding":
                outstanding.append(((rep, q), obj, b[1]))
    outside = [(lab, what, [(f, n, has_item(os.path.join(HERE, f), n)) for f, n in seats])
               for lab, what, seats in OUTSIDE_QUEUE]
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    wt = open(os.path.join(D68, "WARPTHEOREM.md"), encoding="utf-8").read()
    reg_hist = re.findall(r"^## History \(.*?items? (\d+)", wt, re.M)
    stale = [(os.path.basename(f), s, has_text(f, s)) for f, s in STALE_REGISTER]
    # [item 331] the last item any History heading names, ranges included (three-digit item numbers)
    heads = re.findall(r"^## History \((.*?)\)?$", wt, re.M)
    if MUT.get("register_stale"):
        heads = [h for h in heads if "248" not in h]                      # the mutant: the 248-333 history withheld
    nums = [int(x) for h in heads for x in re.findall(r"(?<!\d)(\d{3})(?!\d)", h)]
    current = [(os.path.basename(f), s, has_text(f, s)) for f, s in CURRENT_REGISTER]
    brought = [(lab, f, n, has_item(os.path.join(HERE, f), n)) for lab, _, seats in BROUGHT_CURRENT for f, n in seats]
    arr_rows = {(r[0], r[1]) for r in rows} == set(abear)
    far_rows = {(r[0], r[1]) for r in rows} == set(fbear)
    return dict(stale=stale, reg_now=max(nums) if nums else None, current=current, brought=brought, arr_rows=arr_rows,
                abear=abear, far_rows=far_rows, fbear=fbear,
                reg_last=max(int(x) for x in reg_hist) if reg_hist else None, rows=rows, seated=seated,
                carried=carried, outstanding=outstanding, outside=outside,
                words=all(w in rul for w in WORDS), headers={k: v in rul for k, v in HEADERS.items()})


def report(o):
    print("verify_ledger.py -- every verification accounted against the queued objects (item 330)\n")
    print("%-5s %-16s %-6s %-6s %-6s %-7s %-6s %s" % ("item", "qualification", "O1c", "B5a", "C8", "ARRIVAL", "FAR",
                                                      "gist"))
    for rep, q, gist, seats, *bear in o["rows"]:
        tag = lambda b: "carry" if b[0] == "carried" else "-" if b[0] == NA else "OUT"
        ab = o["abear"].get((rep, q), ("outstanding",))
        fb = o["fbear"].get((rep, q), ("outstanding",))
        print("%-5d %-16s %-6s %-6s %-6s %-7s %-6s %s" % (rep, q, tag(bear[0]), tag(bear[1]), tag(bear[2]), tag(ab),
                                                         tag(fb), gist[:56]))
    bad_s = [s for s in o["seated"] if not s[3]]
    bad_c = [c for c in o["carried"] if not c[4]]
    print("\nL1 seated markers found: %d of %d%s" % (len(o["seated"]) - len(bad_s), len(o["seated"]),
                                                  "" if not bad_s else "; missing %s" % bad_s))
    print("L2 carried corrections found in the queued objects: %d of %d%s" % (
        len(o["carried"]) - len(bad_c), len(o["carried"]), "" if not bad_c else "; missing %s" % bad_c))
    print("L3 outstanding for a queued object: %s" % (o["outstanding"] or "none"))
    print("L4 outstanding outside the queue, owed to its own row (as found at item 330; brought current, item 331):")
    for lab, what, seats in o["outside"]:
        print("   %-18s %s (marked: %s)" % (lab, what, ", ".join("%s %s" % (f, ok) for f, n, ok in seats)))
    print("   the Warp Theorem's register: last history at item %s; stale rows still present: %s" % (
        o["reg_last"], [(f, s[:44], ok) for f, s, ok in o["stale"]]))
    print("   [item 331] brought current: %s; the register's history now reaches item %s; its current statement "
          "present: %s" % (", ".join("%s %s %s" % (lab, f, ok) for lab, f, n, ok in o["brought"]), o["reg_now"],
                           all(ok for _, _, ok in o["current"])))
    print("L5 C9 verified, item 332; O1c, item 337; B5a, item 339; C8, item 341; ARRIVAL, item 348 -- their rows "
          "above, carried where they bear; the queue holds FAR at both ends (item 351)")
    print("L6 (item 344) ARRIVAL (verified, item 348): every row accounted for it: %s; carried %d, not bearing %d" % (
        o["arr_rows"], sum(b[0] == "carried" for b in o["abear"].values()),
        sum(b[0] == NA for b in o["abear"].values())))
    print("L7 (item 351) FAR at both ends (queued): every row accounted for it: %s; carried %d, not bearing %d" % (
        o["far_rows"], sum(b[0] == "carried" for b in o["fbear"].values()),
        sum(b[0] == NA for b in o["fbear"].values())))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("L0 M's item-330 words and the seventeen reports' headers verbatim in the rulings file",
        o["words"] and all(o["headers"].values()))
    add("L1 every seated correction's marker is found in its file", all(s[3] for s in o["seated"]))
    add("L2 every correction a queued object carries is found in its instrument", all(c[4] for c in o["carried"]))
    add("L3 no queued object (O1c, B5a, C8; ARRIVAL, item 344; FAR, item 351) has an outstanding row",
        not o["outstanding"])
    add("L4 the outstanding rows outside the queue are each marked in their own instruments",
        all(ok for _, _, seats in o["outside"] for _, _, ok in seats))
    add("L4 (item 331) the Warp Theorem's register brought current: its history reaches item 331 or later, its current "
        "statement (LEMMAS_NOW, the current head and table) present beside the record's stale rows, kept as the record",
        o["reg_now"] is not None and o["reg_now"] >= 331 and all(ok for _, _, ok in o["current"])
        and all(ok for _, _, ok in o["stale"]))
    add("L4 (item 331) the three rows outstanding outside the queue each brought current, marked in their instruments",
        all(b[3] for b in o["brought"]) and {b[0] for b in o["brought"]} == {lab for lab, _, _ in OUTSIDE_QUEUE})
    reps = {r[0] for r in o["rows"]}
    add("L4 every report of the seventeen has its rows in the ledger", reps == set(HEADERS))
    add("L6 (item 344) ARRIVAL accounted against every row of the seventeen reports, each carried in "
        "arrival_small or not bearing with its reason", o["arr_rows"])
    add("L7 (item 351) FAR at both ends accounted against every row of the seventeen reports, each carried in far_small "
        "or far_large or not bearing with its reason", o["far_rows"])
    return res


MUTANTS = {"c8_stale": "C8 carrying the refuted blueshift closure instead of 319 (Q1)'s bound (L2)",
           "outstanding": "an uncarried correction left for a queued object (L3)",
           "wrong_item": "a seated correction looked for under the wrong item (L1)",
           "register_stale": "the register's 248-333 history withheld (L4; item 331)",
           "arrival_stale": "ARRIVAL carrying 33.6 clocks on every reading, not the G5 readings (L2; item 344)",
           "arrival_unaccounted": "a row left unaccounted for ARRIVAL (L3, L6; item 344)",
           "far_stale": "FAR carrying one sigma convention, not 341 (Q4)'s two (L2; item 351)",
           "far_unaccounted": "a row left unaccounted for FAR (L3, L7; item 351)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    kk = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (kk, len(r_)))
    return kk == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-72s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
