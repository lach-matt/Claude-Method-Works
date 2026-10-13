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
QUEUED_FILES = {"O1c": ("o1c_oneway.py",), "B5a": ("b5a_residue.py", "b5a_oneway.py"), "C8": ("c8_level.py", "m1p2x_oneway.py")}
HEADERS = {254: "254. **Claim C1 verified", 258: "258. **Claim C2 verified", 261: "261. **Claim C3 verified",
           264: "264. **Claim C6 verified", 267: "267. **Claim C5 verified", 269: "269. **Claim C4 verified",
           271: "271. **Claim C7 verified", 281: "281. **The audit before 270", 304: "304. **C1 one-way verified",
           310: "310. **C4 one-way verified", 317: "317. **C5 one-way verified", 319: "319. **C7 one-way verified",
           332: "332. **C9 verified", 337: "337. **O1c one-way verified", 339: "339. **B5a one-way verified"}
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
     N("C8's (b) takes the confinement, not the name")),
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
]
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
    for rep, q, gist, seats, *bear in rows:
        for f, n in seats:
            item = n if not MUT.get("wrong_item") else n + 1000
            seated.append(((rep, q), f, item, has_item(os.path.join(HERE, f), item)))
        for obj, b in zip(QUEUED, bear):
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
    return dict(stale=stale, reg_now=max(nums) if nums else None, current=current, brought=brought,
                reg_last=max(int(x) for x in reg_hist) if reg_hist else None, rows=rows, seated=seated,
                carried=carried, outstanding=outstanding, outside=outside,
                words=all(w in rul for w in WORDS), headers={k: v in rul for k, v in HEADERS.items()})


def report(o):
    print("verify_ledger.py -- every verification accounted against the queued objects (item 330)\n")
    print("%-5s %-16s %-6s %-6s %-6s  %s" % ("item", "qualification", "O1c", "B5a", "C8", "gist"))
    for rep, q, gist, seats, *bear in o["rows"]:
        tag = lambda b: "carry" if b[0] == "carried" else "-" if b[0] == NA else "OUT"
        print("%-5d %-16s %-6s %-6s %-6s  %s" % (rep, q, tag(bear[0]), tag(bear[1]), tag(bear[2]), gist[:70]))
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
    print("L5 C9 verified, item 332; O1c verified, item 337; B5a verified, item 339 -- their rows above, carried where "
          "they bear; C8 next")


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("L0 M's item-330 words and the fifteen reports' headers verbatim in the rulings file",
        o["words"] and all(o["headers"].values()))
    add("L1 every seated correction's marker is found in its file", all(s[3] for s in o["seated"]))
    add("L2 every correction a queued object carries is found in its instrument", all(c[4] for c in o["carried"]))
    add("L3 no queued object (O1c, B5a, C8) has an outstanding row", not o["outstanding"])
    add("L4 the outstanding rows outside the queue are each marked in their own instruments",
        all(ok for _, _, seats in o["outside"] for _, _, ok in seats))
    add("L4 (item 331) the Warp Theorem's register brought current: its history reaches item 331 or later, its current "
        "statement (LEMMAS_NOW, the current head and table) present beside the record's stale rows, kept as the record",
        o["reg_now"] is not None and o["reg_now"] >= 331 and all(ok for _, _, ok in o["current"])
        and all(ok for _, _, ok in o["stale"]))
    add("L4 (item 331) the three rows outstanding outside the queue each brought current, marked in their instruments",
        all(b[3] for b in o["brought"]) and {b[0] for b in o["brought"]} == {lab for lab, _, _ in OUTSIDE_QUEUE})
    reps = {r[0] for r in o["rows"]}
    add("L4 every report of the fifteen has its rows in the ledger", reps == set(HEADERS))
    return res


MUTANTS = {"c8_stale": "C8 carrying the refuted blueshift closure instead of 319 (Q1)'s bound (L2)",
           "outstanding": "an uncarried correction left for a queued object (L3)",
           "wrong_item": "a seated correction looked for under the wrong item (L1)",
           "register_stale": "the register's 248-333 history withheld (L4; item 331)"}


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
