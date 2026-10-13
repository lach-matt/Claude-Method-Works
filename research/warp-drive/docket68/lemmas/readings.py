#!/usr/bin/env python3
"""readings.py -- item 354: M, "Prove all board readings".  Every board reading the register and its rows still rest on,
inventoried in one place with where it was seated, which rows use it, what kind of reading it is and how it is to be
proved; and the proofs, one entry each, as they are done.  Worked in the conversation (deduced from M's verbatim words,
each alternative excluded by a ruling quoted inside its own item; computed with sympy where marked; not verified by a
separate session; not seated); 2026-10-13.

How a reading is proved here (354 (b)).  A reading of M's words is proved only by deducing it from M's own words and
rulings: every alternative reading is listed, each is excluded by a ruling quoted verbatim inside its own item, and
exactly one survives -- the instrument checks the quotations and that one survives; the deduction from each quotation
to its exclusion is stated beside it (deduced).  A physical test form or model is proved by deriving what the row uses
from the exact theory, or by bounding the difference against the row's margin (computed).  Where an alternative
survives, or the proof runs only through a row M deferred (SOURCEs and SOURCE, M-SOURCE-LAST), the entry says so and it
goes to M; the board does not rule on M's meaning.

  Q0 (read) M's words, verbatim: 354, "Prove all board readings"; and every premise below, each inside its own item.
  Q1 (deduced) 318's reading -- 183 governs every classical ray; the passage's negative inside the quantum region is
     177's appearance (Z3bs; FARs F6; B4ds).  Alternatives for 273's "(to be paired per ray under 183)" against 183's
     zero net per ray: (A) 183 on every ray, the quantum region included -- excluded: it forbids every continuation that
     turns the radial congruence (pair_math P3), so no passage of 273's kind, "One-way, complete, README only", against
     273, 270 and 276; (B) a partner pairing the region's negative to zero on each ray -- excluded: on every ray that
     enters converging and leaves diverging, integral R_kk d lambda < 0 with R_kk counting all matter, the README's
     included (pair_math P1), so no partner on the ray brings it to zero; (C) 183 on every classical ray, where every
     segment keeps it (pair_math P2), and the region's negative the appearance 177 names ("Yes, that is the
     appearance"), inside the region 273 gives up "pointwise null energy ... and classical GR there" -- survives.
  Q2 (deduced) 340's reading -- the README forms our face as it arrives, compactly (ARRIVALs; B4ds).  Alternatives: (i)
     a face of the README's size standing through the write -- excluded four ways: its 2E against the one exact energy
     at the bound (136 (1), carried as M's) and "the README is the energy, not separate" (136 G); its face of 2^(3/2) N
     against "only the size that is needed to hold the object" (162); a face standing before the object it needs,
     against "A horizon cannot exist without the object of which it needs to exist" (109); (ii-spread) the README forming
     the face part after part over the write -- excluded by 163, "All together, one whole", chosen over "Instantaneously"
     (a spread arrival comes part after part); (ii-compact) the face formed by the README arriving as one whole --
     survives, M's own guess A at 340.  The compact width, 4.79 clocks, is the null-dust model's figure (Q-entry R21).
  Q3 (deduced) 166 under 275 -- "Both planes at once" is the coincident pair (FARs F9 (g); FAR).  Alternatives: our plane
     alone -- excluded: M chose "Both planes at once" over "No, ours"; position 2's plane alone -- excluded likewise,
     over "Yes, position 2's plane"; the two planes apart, a slab between -- excluded by 275, "Coincident everywhere";
     the two sheets on one surface everywhere -- survives.
  Q4 (deduced) 226 read to include each position 2's tension (FARs F2, F10 (f)).  The option M chose says it: "Each
     position 2 carries its own universe's values, so 2a, 2b and 2c are positive planes" -- a plane's sign is its
     tension's, so the tension is among the values.  Alternative (values without the tension) -- excluded by those
     words.
  Q5 (computed, exact; deduced) 270 (a) -- the one object's faces are the null surface U = 0 (O1cs; ARRIVALs; M1P2xs;
     CLOSEs K6; B4ds).  The four horizon halves of the Kruskal manifold, our exterior I = {U < 0 < V}: {U = 0, V > 0} the
     future horizon of I (a black hole facing us); {V = 0, U < 0} the past horizon of I (a white hole facing us); {U = 0,
     V < 0} the past horizon of III = {V < 0 < U} (a white hole facing the other exterior); {V = 0, U > 0} the future
     horizon of III (a black hole facing it) (computed: each half's neighbouring regions and the sign of its generator's
     time).  132, "a black hole in and a white hole out", keeps the first and third; 270, "the passage is one-way only",
     excludes the second (a white hole facing us, the reverse passage) and 276, "one-way in all aspects", the fourth
     (position 2's matter falling into the corridor).  The two that survive both lie on U = 0, one null surface: 132's
     "side views of the same corridor object".
  Q6 (deduced) 270 (b), H-ONE-INTERIOR -- the interior is one object with one tension (M1P2xs, m1p2x_oneway O2).
     Alternative, a black-hole interior and a white-hole interior as two objects with their own tensions -- excluded by
     132, "*different views of the same object": one object, one interior, one tension.
  Q7 (read) 270 (c), the faces begin at the opening -- M's since 282 (2): M chose the option whose text reads "the
     corridor's faces begin at the opening (270 (c))".  No longer the board's.
  Q8 (computed, exact; deduced) 273 (a) -- the bounce is Haggard and Rovelli's with the Kruskal isometry (U, V) -> (-U,
     -V) in place of their time reflection (O1cs; ARRIVALs V6, V8 (2); M1P2xs; CLOSEs K6).  The metric -F(UV) dU dV
     keeps its form under four discrete maps: the identity, (V, U), (-U, -V) and (-V, -U) (computed).  273's option text,
     "the white hole opening on position 2's exterior", asks for a map taking the black-hole interior II = {U, V > 0} to
     the white-hole interior IV = {U, V < 0} and our exterior I to the other exterior III: (-U, -V) does (computed); (-V,
     -U) takes II to IV but keeps I, the white hole opening on our exterior -- Haggard and Rovelli's own reconnection,
     excluded by 270; (V, U) and the identity keep II.  One survives.
  Q9 (read) 273 (b), Haggard and Rovelli's rule for where quantum effects appear, carried to five dimensions -- M's
     since 353: M-PLANCK-ENDS asks regularity below the five-dimensional Planck curvature, "273 (b)'s rule".
  Q10 (deduced) 275 (a) -- f_slab's static slab exists nowhere (M1P2xs; FARs F1).  A slab needs the two planes apart
     over an open region; 275, "Coincident everywhere", leaves none.
  Q11 (read; deduced) 276 (a) -- our sheet's junction carries our stress alone -- proved at item 323 (b5a_residue A1's
     item-323 note: from 276, with our bulk mirrored Israel gives S1; p2_assume Q2).  No longer the board's.
  Q12 (deduced; imported) 284 (a) -- 139 (2)'s positivity owed where the corridor's rays cross position 2's plane, not
     after the README has rebuilt (M1P2xs).  Proved by holding on both readings: where the rays cross, the README's
     density exceeds sigma/4 (e_positive E7, computed); everywhere else, position 2's rebuilt matter keeps rho >= 0 and
     the null condition at every point, every kind of matter the record holds (pointwise P1-P6, B5b DERIVED, 320).  So
     139 (2) holds on the stronger reading too, and the restriction carries no weight.
  Q13 (deduced) 336 (a) -- 110 and 111 (a) concern position 2's horizon, its own energy going into position 2 when its
     face closes (M1P2xs; ARRIVALs V8 (5)).  Alternatives: 110 and 111 (a) given up -- excluded: the option M chose names
     what it gives up, "158 (2)'s timing and 115 (a)'s \"energy moved\"", and not these; they concern our E -- excluded
     by 336 itself, our E staying in our universe ("I think it is B", M-ENERGY-STAYS); they concern position 2's own
     energy -- survives, as 240 has it: "Position 2 accounts for the difference as it assembles the mass to match a
     README from position 1 under position 2's laws".
  Q14 (computed; deduced) 319's re-reading of J5 -- position 2's own fields reaching its face are bounded over its open
     period (M1P2xs; FARs F10 (b); B4ds D5).  Computed: J1's open period, ln(1 + (pi/10)(ell/r_h)) = 33.60 clocks, bounds
     any blueshift at the face by e^33.60 = 3.9e14; a blackbody bath of 3 K to 1e10 K so blueshifted delivers 3.6e-57 to
     4.4e-19 J over that period, 65 and 27 orders below Barcelo's 0.28 E, and 51 and 12 below the 1e-15 E of their eqs.
     (17) and (20) at a 33.6-e-fold face (341 (Q3)).  Deduced: anything beyond a bath is position 2's own content, and
     the object's survival of position 2's variances is position 2's (240, M-SURVIVABILITY: "Survivability of the object
     when contained in position 2 depends on how well it is equipped to mitigate that variances of position 2").  So the
     bound is proved for every ambient bath to 1e10 K, and beyond it the question is 240's, not the board's.
  Q15 (computed; deduced) The fine count of 136 (5) -- the README's own entropy adds nothing (ARRIVALs V4).  "5 - one
     fixed exact encoding" (136): one specified string, so its distribution is a single point, Shannon entropy 0, and as
     a quantum state a pure one, von Neumann entropy 0 (computed).  The coarse count is the carrier's, not the README's
     (V4), and stays as V4 has it.
  Q16 (computed, exact; deduced) 240 (b) -- each face's radius set by its own side's laws (ARRIVALs V6; c7_oneway V2).
     240: "the object is built from the bulk at position 2 as an exact copy under the laws and conditions of position 2",
     and position 2 "assembles the mass to match a README from position 1 under position 2's laws": position 2's face
     holds the README's N bits at its own l5 (C2's count, 2 pi^2 r_h^3 = 4 N ln2 l5^3), so r_h2/r_h = (G5_2/G5)^(1/3) and
     E2/E = (G5/G5_2)^(1/3) (computed: E = 3 pi c^4 r_h^2/(8 G5)).  Alternative, position 2's face at our r_h -- excluded
     by 240, "The mass on position 2's side is not equal to ours".
  Q17 (deduced; computed) 320 (b)-(c).  (b): "no bulk is ever empty" (320) makes every empty-bulk result the limit, not
     M's configuration -- direct.  (c): a bulk content of density at most X times the bulk's own vacuum energy density
     (sigma/ell = 3 c^4/(4 pi G5 ell^2)) adds to the Misner-Sharp mu inside r at most X (r/ell)^2 r^2, so it moves a
     vacuum figure at the hole by at most X (r_h/ell)^2 = 6.4e-31 X of itself (computed) -- every vacuum figure holds
     with the content to that order.  What X is, the record does not fix; 320 says only that the content is "information
     or matter".
  Q18 (deduced) c1_oneway's (192) reading -- clause (B)'s vacuum bulk is no classical stress on the route (O1a).  273
     "Gives up ... classical GR there", so no classical stress is defined inside the region; the alternative, the route
     Ricci-flat throughout, is excluded by pair_math P1 -- a turned congruence has integral R_kk < 0 on every ray, so
     R_kk is not zero everywhere on it.
  Q19 (deduced) 152 (1) as CENSOR5D's escape (a), one end (B4a).  152 (1), "two separate positions connected by/reached
     through a dimension": the bulk over each position's sheet is one region joined through the extra dimension, so the
     plane's two ends are one end of the bulk -- escape (a); the alternative, two separate ends of the bulk, is excluded
     by "connected by/reached through a dimension".
  Q20 (computed; deduced) H-ASYMMETRIC-BOUNCE -- our face stands the life, position 2's at most 33.6 clocks (c_junction
     J3; M1P2xs; CLOSEs K9; B4ds D5).  Our face's duration is the life, 8.57e14 clocks, by 336 (M's); position 2's is at
     most 33.60 clocks by J1 (computed).  So the bounce is asymmetric by a factor of at least 2.6e13 -- a consequence,
     not a reading.
  Q21 (read; deduced) Four readings the inventory carried bear on no current row's claim, each read in its file and the
     register by path.  RPOS2, H-POSITIVE-ON-P2: B5pu rests on b5p_cypher and pointwise P5 (its row), whose claim is
     B5'a's condition; b5p_cypher (6) says H-POSITIVE-ON-P2 "is a different condition", and 139 (2) where it bears is
     B5c's, proved at Q12.  RT5, sigma_defines T5's flag: B5pu holds on both decisions -- b5p_cypher (5), "were it
     decided the other way, the variant W139 ... still meets B5'a's condition with margin" -- and B6' rests on
     sigma_defines T1-T4, not T5 (its row): proved on both branches.  RE6, 139 (3) read as position 2's expansion
     raised: B5c rests on e_positive E7 (its row), where the emerging README alone carries the plane past sigma/4
     (computed); E7's "beyond it ... (E6)" lies outside where positivity is owed (284, 285), and there Q12's pointwise
     route holds without E6.  RO3H, o3_hold's mapping and locally analytic class: O3s rests on O3e (its row), and "O3e
     rests on no reading of the board's" (o3_hold, item 334); the mapping is O3a's, the class O3a''s (withdrawn), and
     "O3b's static window is eq. (17)'s and does not bound it".  None is a premise of any row.
  Q22 (deduced) 148's reading (i) -- position 2's electron mass is ours (R5; R5b).  The question M answered carried its
     two options inside item 148: "No: position 2 only where everything the README contains measures exactly as ours;
     Yes: then item 146 or 147 must change".  M answered "No, BUT, matter at position 2 can rearrange to accommodate
     the README".  Alternative, the electron's mass differing at position 2 -- excluded: that is the "Yes" option, which
     M did not give, and the "BUT" concerns how matter fits the README, not its constants.  The electron's mass is among
     what the README's values measure (144: the relative laws act "on the electron's mass"), so position 2 is only where
     it is ours -- survives; and 155 (3) carried it as M's with H-ACTIVATION-IS-TRIGGER ("R5b's reading, with item 148's
     reading (i), now M's").  240's "The mass on position 2's side is not equal to ours" is the face's energy (Q16),
     not the electron's.
  Q23 (READ; computed, exact where marked; deduced) H-GT-IN-WARP -- every conclusion FAR draws from its test form holds
     in Garriga and Tanaka's own field (FAR; far_large L4, L11 (a)). (a) The field in the bulk, in their RS gauge. Their
     eq. (12), h = -2 kappa int G_R Sigma, with Sigma_00 = (2/3) rho and Sigma_ij = (1/3) rho delta_ij + 2 kappa^-1
     xi5,ij, traceless by their eq. (4), gives at every depth h00 = -(8/3) V and h_rr = -(8/(3 r^3)) int_0^r r'^2 V dr'
     with V taken at that depth (deduced: h_ij = -(4/3) V delta_ij - 4 d_i d_j W, lap W = -V/3) -- their eq. (21) is its
     case on the wall. With their eq. (16) for G and m = kappa M/(8 pi ell) from eqs. (22)-(23), in conformal depth Z and
     d^2 = u^2 + Z^2 (computed, exact): h_uu/a^2 = A = 4m/(3d), h_angular/(a^2 u^2) = C = 2m (2 Z^2 + u^2)/(3 d^3), h_ZZ
     = 0 (h55 = 0), traceless against h00/a^2 = (4/3) m (2 u^2 + 3 Z^2)/d^3; on the axis A = C = 4m/(3Z). The test form
     put Phi = m (2 u^2 + 3 Z^2)/d^3 in all three. The slice is static and time-symmetric, so theta+ is the mean
     curvature and the lapse does not enter. (b) The round tip (computed, exact): GT's first-order pull is 4 (3U + 2
     ell)/(9 (U + ell)) times the test form's, and the tip is trapped when 3 ell (U + ell) < 2m (3U + 2 ell) -- the
     marginal ell 2m at large U, against 3m/2 (the verifier's figures, reproduced). At N_L, ell/m = (8/pi)^(1/2) < 2, so
     in GT's field the round tip is trapped there for every U > 1.04 m (first order; the range is U >> m): 355 (Q14)'s N
     > 1.13 N_L is the test form's, not GT's. (c) The elongated surface (computed: exact at the tip, sampled elsewhere).
     To first order theta+ > 0 at every point of T_E once U > c(K) m, counting every first-order term; at the tip, as
     ell/U -> 0, c (K - 1)/K = 2 (2K + 1)/(3 K^(3/2)), which is 2 at K = 1 and falls with K (exact); over the surface,
     sampled at K from 1.001 to 1e4 and ell/U from 1e-12 to 1e-1, it never reaches 2. So GT's field needs U > 2 m K/(K -
     1), inside L4 (b)'s (9/4) m K/(K - 1). Cross-check: the test form's gradient part needs about 1.51 m K/(K - 1), so
     L4 (b) is sufficient there too; its conformal factor f^(-1/2) scales theta+ and lowers it without changing its sign.
     (d) The wall's bending (READ; computed; deduced). In the RS gauge the wall sits displaced by xi5 = m ell/(3r) (eq.
     (22)), so T_E meets it at beta = (m ell/(3 U^2)) (1 + 1/K) off the perpendicular, whichever sign: the closed
     two-sided surface has a kink of 2 beta. Rounding it over a proper width eps, with m ell/U << eps << U (eps = (m
     ell)^(1/2) meets both when (m ell)^(1/2) << U), costs at most beta/eps of theta+, a fraction (m ell)^(1/2) (1 +
     1/K)/(3U (2 + 1/K)) of the rim's margin (2 + 1/K)/U -- 6.3e-7 at the record's cover, ell/m at most (8/pi)^(1/2). (e)
     Outside this proof: eq. (16) is the far field's leading form, with corrections O(ell^2/d^2) (their eq. (15)); the
     source's compactness, O(r0/d); and the two-sided pair's per-side amplitude, L9 (d)'s estimate. On T_E, d >= U, so
     each is O(m/U) or smaller.

The inventory (INVENTORY below): every board reading in force, its item, the rows it bears on, its kind -- words (a
reading of M's words), form (a physical test form), model (a model of what a deferred row will define), choice (a
construction the board chose), protocol (how the calculator is asked) -- and its state: proved here (the Q-entry),
proved before, M's (the item that made it so), to prove (the route), or through SOURCE (M-SOURCE-LAST).

[Item 355: FAR's verifier found this inventory bearing on four of its qualifications, each carried in far_small F11 or
far_large L11 -- (Q2), 319's re-reading of J5, J1's use of F1 and H-ASYMMETRIC-BOUNCE unlabelled there: here RJ5 (Q14)
and RASYM (Q20); (Q3), 273 (a) misdescribed and 270 (a), 273 (a), 336 (a) unlabelled: here Q5, Q8 and Q13; (Q7),
Garriga and Tanaka's RS-gauge tensor structure: RGT, whose proof is that gauge's own; (Q13), 226 with tension and 320
(b) omitted from L9 (i)'s rests-on: here Q4 and Q17.  The inventory's entries stand as written.]

What this does not claim.
  - That the inventory is closed beyond the rows' own instruments: a reading named only in an instrument no row cites
    is not in it.
  - Any proof for the entries still marked "to prove" or "through SOURCE".

Imports nothing from the instruments; reads the rulings file, and for Q21 the register (LEMMAS_NOW, parsed as a literal)
and three instruments' texts, by path.  Stdlib + sympy.
python3 readings.py [--selftest | --mutants]
"""
import ast
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
REGISTER = os.path.join(D68, "warptheorem.py")
MUT = {}

# the premises, verbatim, each checked inside its own item
WORDS = {
    "354": (354, '"Prove all board readings"'),
    "109": (109, "A horizon cannot exist without the object of which it needs to exist"),
    "132": (132, "a black hole in and a white hole out, side views of the same corridor object *different views of "
                 "the same object"),
    "136.1": (136, "H-EXACT-ENERGY-AT-BOUND becomes M's: the one exact energy is E(N) at the bound"),
    "136.5": (136, "5 - one fixed exact encoding"),
    "136.G": (136, "G - the README is the energy, not separate"),
    "148.no": (148, '"No, BUT, matter at position 2 can rearrange to accommodate the README'),
    "148.q": (148, "No: position 2 only where everything the README contains measures exactly as ours; Yes: then item "
                   "146 or 147 must change"),
    "144": (144, "the relative laws of physics by which another universe's elements differ from ours act on the "
                 "nucleus -- its mass, its size, which nuclei are stable -- and on the electron's mass"),
    "155.3": (155, "H-ACTIVATION-IS-TRIGGER (the Higgs field's value is unchanged; the README triggers the "
                   "rearrangement, by electromagnetism and the nuclear forces -- R5b's reading, with item 148's reading "
                   "(i), now M's)"),
    "152": (152, '"two separate positions connected by/reached through a dimension."'),
    "162": (162, "It is and always will be only the size that is needed to hold the object once and at once"),
    "163": (163, '"All together, one whole"'),
    "163.no": (163, '"Instantaneously"'),
    "166": (166, 'M chose: "Both planes at once"'),
    "166.ours": (166, '"No, ours"'),
    "166.p2": (166, '"Yes, position 2\'s plane"'),
    "177": (177, '"Yes, that is the appearance"'),
    "183": (183, '"Yes: never violated as a pair"'),
    "226": (226, "Each position 2 carries its own universe's values, so 2a, 2b and 2c are positive planes"),
    "240.copy": (240, "the object is built from the bulk at position 2 as an exact copy under the laws and conditions "
                      "of position 2"),
    "240.mass": (240, "The mass on position 2's side is not equal to ours. Position 2 accounts for the difference as "
                      "it assembles the mass to match a README from position 1 under position 2's laws."),
    "240.surv": (240, "Survivability of the object when contained in position 2 depends on how well it is equipped "
                      "to mitigate that variances of position 2"),
    "270": (270, '"You are forgetting that the passage is one-way only"'),
    "273": (273, "with the white hole opening on position 2's exterior. One-way, complete, README only, no Cauchy "
                 "horizon. Gives up pointwise null energy inside a small quantum region (to be paired per ray under "
                 "183) and classical GR there."),
    "275": (275, '"Coincident everywhere"'),
    "276": (276, '"The passage is one-way in all aspects"'),
    "282": (282, "the corridor's faces begin at the opening (270 (c))"),
    "318": (318, '"For the math"'),
    "320": (320, "no bulk is ever empty"),
    "336": (336, '"I think it is B"'),
    "336.give": (336, "giving up 158 (2)'s timing and 115 (a)'s \"energy moved\""),
    "340": (340, '"C, but my guess is A"'),
    "344": (344, "The README is really written on our plane, so its true source is a gas of the plane's fields, not "
                 "null dust."),
    "353": (353, '"I propose one reading for you to confirm. - confirmed"'),
}

# the exclusions: reading -> [(alternative, excluded by premise key or None if it survives, the deduction)]
EXCLUSIONS = {
    "Q1": [("183 on every ray, the quantum region included", "273", "forbids every turning continuation (P3)"),
           ("a partner pairs the region's negative to zero per ray", "computed: pair_math P1",
            "integral R_kk < 0 on every turned ray, all matter counted"),
           ("183 on classical rays; the region's negative is 177's appearance", None, "survives (P2, 177, 273)")],
    "Q2": [("(i) a face standing through the write", "136.G", "2E against one energy; 162; 109"),
           ("(ii) spread: part after part over the write", "163", "not all together, one whole"),
           ("(ii) compact: the README forms the face as one whole", None, "survives; M's guess A (340)")],
    "Q3": [("our plane alone", "166.ours", "M chose 'Both planes at once' over it"),
           ("position 2's plane alone", "166.p2", "M chose 'Both planes at once' over it"),
           ("two planes apart, a slab between", "275", "coincident everywhere"),
           ("two sheets on one surface everywhere", None, "survives")],
    "Q4": [("its values without its tension", "226", "positive planes: the sign is the tension's"),
           ("its values with its tension", None, "survives")],
    "Q6": [("two interiors, two tensions", "132", "different views of the same object"),
           ("one interior, one tension", None, "survives")],
    "Q13": [("110 and 111 (a) given up", "336.give", "the chosen option names what it gives up, not these"),
            ("110 and 111 (a) concern our E", "336", "our E stays in our universe"),
            ("110 and 111 (a) concern position 2's own energy", None, "survives; 240")],
    "Q16": [("position 2's face at our r_h", "240.mass", "the mass on position 2's side is not ours"),
            ("position 2's face at its own l5", None, "survives; C2's count under 240")],
    "Q18": [("the route Ricci-flat throughout", "computed: pair_math P1", "a turned congruence needs integral R_kk < 0"),
            ("no classical stress where classical GR is given up", None, "survives")],
    "Q19": [("two separate ends of the bulk", "152", "connected by/reached through a dimension"),
            ("one end, joined through the extra dimension", None, "survives")],
    "Q22": [("position 2's electron mass differing from ours", "148.no",
             "M answered 'No' over 'Yes: then item 146 or 147 must change' (148.q)"),
            ("position 2 only where the README's values, the electron's mass among them (144), measure as ours", None,
             "survives; carried as M's at 155 (3)")],
}

# the inventory: (id, item, reading, rows, kind, state)
INVENTORY = (
    ("R318", 318, "183 on classical rays; the region's negative is 177's appearance", "Z3bs FARs B4ds", "words",
     "proved here (Q1)"),
    ("R340", 340, "the README forms our face as it arrives, compactly", "ARRIVALs B4ds", "words", "proved here (Q2)"),
    ("R166", 349, "'Both planes at once' is the coincident pair", "FARs FAR", "words", "proved here (Q3)"),
    ("R226", 351, "226's 'Its own values' includes each position 2's tension", "FARs", "words", "proved here (Q4)"),
    ("R270a", 270, "the faces are the null surface U = 0", "O1cs ARRIVALs M1P2xs CLOSEs B4ds", "words",
     "proved here (Q5)"),
    ("R270b", 270, "H-ONE-INTERIOR: one interior, one tension", "M1P2xs", "words", "proved here (Q6)"),
    ("R270c", 270, "the faces begin at the opening", "B7 B4a ARRIVALs", "words", "M's since 282 (2) (Q7)"),
    ("R273a", 273, "the Kruskal isometry (-U, -V) in place of the time reflection", "O1cs ARRIVALs M1P2xs CLOSEs",
     "words", "proved here (Q8)"),
    ("R273b", 273, "Haggard and Rovelli's rule carried to five dimensions", "B4ds B3s", "choice",
     "M's since 353, M-PLANCK-ENDS (Q9)"),
    ("R275a", 275, "the static slab exists nowhere", "M1P2xs FARs", "words", "proved here (Q10)"),
    ("R276a", 276, "our sheet's junction carries our stress alone", "B5a M1P2xs FARs", "words",
     "proved before, item 323 (Q11)"),
    ("R284a", 284, "139 (2) owed where the rays cross, not after the rebuild", "M1P2xs", "words",
     "proved here (Q12)"),
    ("R336a", 336, "110 and 111 (a) concern position 2's own energy", "M1P2xs ARRIVALs", "words", "proved here (Q13)"),
    ("RJ5", 319, "J5's bound on position 2's fields over the open period", "M1P2xs FARs B4ds O2 O3s", "form",
     "proved here (Q14)"),
    ("R1365", 338, "the fine count: the README's own entropy adds nothing", "ARRIVALs", "words", "proved here (Q15)"),
    ("R240b", 240, "each face's radius set by its own side's laws", "ARRIVALs", "words", "proved here (Q16)"),
    ("R320", 320, "empty-bulk results limits; vacuum figures hold with content to order", "O1cs O1bs ARRIVALs FARs",
     "words", "proved here (Q17)"),
    ("R192", 304, "clause (B)'s vacuum bulk is no classical stress on the route", "O1a", "words", "proved here (Q18)"),
    ("R152", 152, "152 (1) as CENSOR5D's escape (a), one end", "B4a", "words", "proved here (Q19)"),
    ("RASYM", 338, "H-ASYMMETRIC-BOUNCE: our face the life, position 2's at most 33.6 clocks",
     "M1P2xs CLOSEs B4ds", "choice", "proved here (Q20)"),
    ("RDUST", 338, "the README arriving as radial null dust", "ARRIVALs B4ds FARs", "model",
     "through SOURCE (M-SOURCE-LAST): SOURCEs replaces it"),
    ("RBITS", 338, "H-BITS-WITH-ENERGY: the bits come in with the energy", "ARRIVALs", "model",
     "through SOURCE (M-SOURCE-LAST)"),
    ("RSHELL", 337, "the README as Haggard and Rovelli's thin null shell", "O1cs O1bs", "model",
     "to prove: whether O1c's conclusions hold for any README matter inside the region; else through SOURCE"),
    ("RHOLE", 349, "H-HOLE-IN-WARP: the hole's isotropic factor under the warp", "FARs", "form",
     "to prove: exact Tangherlini spatial slice plus a first-order bound on the warp's correction"),
    ("RGT", 350, "H-GT-IN-WARP: Garriga-Tanaka's far field under the warp", "FAR", "form", "proved here (Q23)"),
    ("RCOVER", 349, "the record's cover U = 1.05 R_reach", "FARs FAR", "choice",
     "to prove: FAR at every enclosing U from the write's reach"),
    ("RONPLANE", 264, "H-README-ON-PLANE: the README written in our plane's fields", "WRITEs O3s FARs ARRIVALs",
     "model", "M's since 344 (\"The README is really written on our plane\")"),
    ("RGAS", 264, "H-FREE-GAS, H-BITS-ARE-STATES: the carrier a free gas holding 2^N states",
     "WRITEs O3s FARs ARRIVALs", "model", "through SOURCE (M-SOURCE-LAST): the plane's gas is SOURCE's to define"),
    ("RMAP", 264, "H-WRITE-IS-ARRIVAL, H-SMALL-CLOCK, H-HOLD-FRAME, H-FLAT-START, H-README-ALONE", "WRITEs O3s FARs",
     "choice", "to prove: each from M's rulings (334, 336, 273's 'README only') or computed (H-FLAT-START)"),
    ("RSPEC", 264, "H-SPECIES-FINITE: finitely many species above the Standard Model", "WRITEs O3s B4ds", "model",
     "to prove: bound what the figures need of g*"),
    ("RCALC", 310, "c4_oneway's calculator protocols (P13, P17, P18, P20)", "M1s", "protocol",
     "to prove: M1s's claims without the calculator's agreement"),
    ("RPOS2", 231, "H-POSITIVE-ON-P2: 139 (2) as the board reads it", "B5pu", "words", "bears on no row's claim (Q21)"),
    ("RT5", 231, "sigma_defines T5's flag decided under 149", "B5pu B6'", "choice", "proved on both branches (Q21)"),
    ("RE6", 268, "139 (3) read as position 2's expansion raised by the README's energy", "B5c", "words",
     "bears on no row's claim (Q21)"),
    ("R148", 149, "148's reading (i): position 2's electron mass ours", "R5", "words",
     "proved here (Q22); M's since 155 (3)"),
    ("RO3H", 334, "o3_hold's mapping and its locally analytic class", "O3s", "choice", "bears on no row's claim (Q21)"),
)


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words_ok():
    out = {}
    for k, (n, w) in WORDS.items():
        if MUT.get("word_wrong_item") and k == "275":
            n += 1                                                    # the mutant: 275's words looked for in 276
        out[k] = " ".join(w.split()) in _item(n)
    return out


def survivors():
    ex = {q: list(v) for q, v in EXCLUSIONS.items()}
    if MUT.get("unexcluded"):
        ex["Q3"] = [(a, None if a.startswith("two planes apart") else p, d) for a, p, d in ex["Q3"]]
    return {q: [a for a, p, _ in v if p is None] for q, v in ex.items()}, ex


# ---------------------------------------------------------------------------------- Q5 the horizon halves
def q5():
    regions = {"I": (-1, 1), "II": (1, 1), "III": (1, -1), "IV": (-1, -1)}       # (sign U, sign V)
    halves = {"U=0,V>0": ("U", 1), "V=0,U<0": ("V", -1), "U=0,V<0": ("U", -1), "V=0,U>0": ("V", 1)}
    out = {}
    for name, (axis, sgn) in halves.items():
        # neighbours: the regions whose other coordinate has the half's sign
        nb = sorted(r for r, (su, sv) in regions.items() if (sv if axis == "U" else su) == sgn)
        ext = [r for r in nb if r in ("I", "III")][0]
        interior = [r for r in nb if r in ("II", "IV")][0]
        out[name] = (ext, "future" if interior == "II" else "past")
    keep = [h for h, (ext, kind) in out.items() if (ext, kind) in (("I", "future"), ("III", "past"))]
    if MUT.get("faces_swapped"):
        keep = [h for h, (ext, kind) in out.items() if (ext, kind) in (("I", "past"), ("III", "future"))]
    return dict(halves=out, keep=keep, one_surface=len({h.split(",")[0] for h in keep}) == 1)


# ---------------------------------------------------------------------------------- Q8 the discrete isometries
def q8():
    U, V = sp.symbols("U V", real=True)
    F = sp.Function("F")
    maps = {"id": (U, V), "(V,U)": (V, U), "(-U,-V)": (-U, -V), "(-V,-U)": (-V, -U)}
    regions = {"I": (-1, 1), "II": (1, 1), "III": (1, -1), "IV": (-1, -1)}
    keep, invariant = [], {}
    for name, (fu, fv) in maps.items():
        # -F(UV) dU dV pulled back: dU' dV' = J dU dV for these linear maps (no dU^2 terms in any)
        J = sp.Matrix([[sp.diff(fu, U), sp.diff(fu, V)], [sp.diff(fv, U), sp.diff(fv, V)]])
        prod = sp.expand((J[0, 0] * sp.Symbol("dU") + J[0, 1] * sp.Symbol("dV"))
                         * (J[1, 0] * sp.Symbol("dU") + J[1, 1] * sp.Symbol("dV")))
        same = sp.simplify(prod - sp.Symbol("dU") * sp.Symbol("dV")) == 0
        invariant[name] = sp.simplify(fu * fv - U * V) == 0 and same
        img = {}
        for r, (su, sv) in regions.items():
            iu = sp.sign(fu.subs({U: su, V: sv}))
            iv = sp.sign(fv.subs({U: su, V: sv}))
            img[r] = [k for k, s in regions.items() if s == (iu, iv)][0]
        if MUT.get("time_reflection") and name == "(-V,-U)":
            keep.append(name)
        elif img["II"] == "IV" and img["I"] == "III":
            keep.append(name)
    return dict(invariant=invariant, keep=keep)


# ---------------------------------------------------------------------------------- Q14 the J5 bound
def q14():
    rh, rh_ell, clock = 1.12008e-20, 8.02117e-16, 1.12008e-20 / 299792458.0
    E = 1.28098e9
    j1 = math.log(1 + (math.pi / 10) / rh_ell)
    blue = math.exp(j1)
    sb = 5.670374419e-8
    area = 4 * math.pi * rh ** 2
    dose = [sb * T ** 4 * area * j1 * clock * blue for T in (3.0, 1e10)]
    return dict(j1=j1, blue=blue, dose=dose, below_barcelo=[math.log10(0.28 * E / d) for d in dose],
                below_eq17=[math.log10(1e-15 * E / d) for d in dose])


# ---------------------------------------------------------------------------------- Q15 the fine count
def q15():
    p = [1.0]                                                          # one fixed string: one point
    shannon = -sum(x * math.log(x) for x in p if x > 0)
    psi = sp.Matrix([1, 0, 0, 0])
    rho = psi * psi.T
    ev = [e for e, m in rho.eigenvals().items() for _ in range(m)]
    vn = -sum(e * sp.log(e) for e in ev if e != 0)
    if MUT.get("mixed_readme"):
        vn = sp.log(2)                                                 # the mutant: the README a mixture of two
    return dict(shannon=shannon, von_neumann=sp.simplify(vn))


# ---------------------------------------------------------------------------------- Q16 each face its own laws
def q16():
    N, G5, G52, l5, c, hbar = sp.symbols("N G5 G5_2 l5 c hbar", positive=True)
    l5_of = lambda G: (hbar * G / c ** 3) ** sp.Rational(1, 3)
    rh_of = lambda G: (4 * N * sp.log(2) * l5_of(G) ** 3 / (2 * sp.pi ** 2)) ** sp.Rational(1, 3)
    E_of = lambda G: 3 * sp.pi * c ** 4 * rh_of(G) ** 2 / (8 * G)
    p = 1 if MUT.get("face_at_ours") else sp.Rational(1, 3)            # the mutant: E2/E as (G5/G5_2)^1
    return dict(ratio=sp.simplify(E_of(G52) / E_of(G5) - (G5 / G52) ** p) == 0,
                radius=sp.simplify(rh_of(G52) / rh_of(G5) - (G52 / G5) ** sp.Rational(1, 3)) == 0)


# ---------------------------------------------------------------------------------- Q17 content to order
def q17():
    G5, c, ell, r, X = sp.symbols("G5 c ell r X", positive=True)
    vac = 3 * c ** 4 / (4 * sp.pi * G5 * ell ** 2)                     # sigma/ell, the bulk's vacuum density
    rho = X * vac
    mu_content = 4 * sp.pi * G5 * rho * r ** 4 / (3 * c ** 4)          # F5 (d): trapping when mu_content = r^2
    rel = sp.simplify(mu_content / r ** 2)
    return dict(rel=rel, exact=sp.simplify(rel - X * (r / ell) ** 2) == 0, at_hole=(8.02117e-16) ** 2)


# ---------------------------------------------------------------------------------- Q20 the asymmetry
def q20():
    j1 = math.log(1 + (math.pi / 10) / 8.02117e-16)
    return dict(life=8.573276e14, open=j1, factor=8.573276e14 / j1)


# ---------------------------------------------------------------------------------- Q21 four that bear on no row
def _flat(path):
    with open(path, encoding="utf-8") as f:
        return " ".join(f.read().split())


def _register_rows():
    tree = ast.parse(open(REGISTER, encoding="utf-8").read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "LEMMAS_NOW" for t in node.targets):
            return {r[1].split()[0]: " ".join(r[3].split()) for r in ast.literal_eval(node.value)}
    return {}


Q21_ROWS = (("B5pu", "lemmas/b5p_cypher.py (b1_matter C3, C4); pointwise.py P5", "H-POSITIVE-ON-P2"),
            ("B6'", "lemmas/sigma_defines.py T1-T4;", "T5"),
            ("B5c", "lemmas/e_positive.py E7:", "E6"),
            ("O3s", "lemmas/o3_hold.py O3e:", "O3a"))
Q21_TEXTS = (("b5p_cypher.py", "(6) H-POSITIVE-ON-P2 (139 (2) as the board reads it) is a different condition"),
             ("b5p_cypher.py", "were it decided the other way, the variant W139 (t2 = -1/4 > -1 - 2 eps) still meets "
                               "B5'a's condition with margin (P3, P7)"),
             ("e_positive.py", "near the face the emerging README alone carries the plane past sigma/4 within R <= "
                               "(3E/(pi sigma))^(1/3) = 2.0e-15 m"),
             ("o3_hold.py", "O3e rests on no reading of the board's"),
             ("o3_hold.py", "O3b's static window is eq. (17)'s and does not bound it"))


# ---------------------------------------------------------------------------------- Q23 Garriga-Tanaka's own field
def _theta(Om2, a, b, c, uu, ww, U, W, eps):
    guu, gww, goo = Om2 * (1 + eps * a), Om2 * (1 + eps * b), Om2 * uu ** 2 * (1 + eps * c)
    F = uu ** 2 / U ** 2 + ww ** 2 / W ** 2
    Fu, Fw = sp.diff(F, uu), sp.diff(F, ww)
    nrm = sp.sqrt(Fu ** 2 / guu + Fw ** 2 / gww)
    sq = sp.sqrt(guu * gww) * goo
    H = (sp.diff(sq * Fu / guu / nrm, uu) + sp.diff(sq * Fw / gww / nrm, ww)) / sq
    return H.subs(eps, 0), sp.diff(H, eps).subs(eps, 0)


def q23():
    u, w, U, W, ell, m, eps, K, r, s_ = sp.symbols("u w U W ell m epsilon K r s", positive=True)
    Zs = sp.Symbol("Z", positive=True)
    # (a) the bulk field from eq. (12) with eq. (16)'s G: V/a^2 at depth Z
    v = -(m / 2) * (2 * s_ ** 2 + 3 * Zs ** 2) / (s_ ** 2 + Zs ** 2) ** sp.Rational(3, 2)
    I = sp.integrate(s_ ** 2 * v, (s_, 0, r))
    vr = v.subs(s_, r)
    A = sp.simplify(-8 * I / (3 * r ** 3))
    C = sp.simplify(-sp.Rational(4, 3) * vr + 4 * I / (3 * r ** 3))
    h00 = sp.simplify(-sp.Rational(8, 3) * vr)
    W1 = -I / (3 * r ** 2)                                             # W' from lap W = -V/3
    from_sigma = (sp.simplify(-sp.Rational(4, 3) * vr - 4 * (-vr / 3 - 2 * W1 / r) - A) == 0
                  and sp.simplify(-sp.Rational(4, 3) * vr - 4 * W1 / r - C) == 0)
    dd = sp.sqrt(r ** 2 + Zs ** 2)
    forms = (sp.simplify(A - 4 * m / (3 * dd)) == 0
             and sp.simplify(C - 2 * m * (2 * Zs ** 2 + r ** 2) / (3 * dd ** 3)) == 0
             and sp.simplify(-h00 + A + 2 * C) == 0 and sp.limit(A, r, 0) == sp.limit(C, r, 0) == 4 * m / (3 * Zs))
    # the surface's theta+ in the field: GT (A, h_ZZ = 0, C) against the test form (Phi in all three)
    Z = ell + w
    d = sp.sqrt(u ** 2 + Z ** 2)
    Ab, Cb = A.subs({r: u, Zs: Z}), C.subs({r: u, Zs: Z})
    Bb = Cb if MUT.get("h55_kept") else sp.Integer(0)                 # the mutant: h_ZZ kept, not GT's h55 = 0
    Phi = m * (2 * u ** 2 + 3 * Z ** 2) / d ** 3
    H0, Hg = _theta((ell / Z) ** 2, Ab, Bb, Cb, u, w, U, W, eps)
    _, Ht = _theta((ell / Z) ** 2, Phi, Phi, Phi, u, w, U, W, eps)
    tip = lambda e, Wv: sp.simplify(sp.limit(e.subs(W, Wv).subs(w, Wv), u, 0))
    # (b) the round tip
    h0, g1, t1 = tip(H0, U), tip(Hg, U), tip(Ht, U)
    ratio = sp.simplify(g1 / t1 - 4 * (3 * U + 2 * ell) / (9 * (U + ell))) == 0
    marg = [sp.limit(x, U, sp.oo) for x in sp.solve(sp.Eq(h0 + g1, 0), ell)]
    lnl = math.sqrt(8 / math.pi)
    u_nl = lnl * (3 * lnl - 4) / (6 - 3 * lnl)                         # 3 l (U + l) = 2 (3U + 2 l), m = 1
    # (c) the elongated tip, exact, and the surface sampled
    ct = sp.limit(sp.simplify(-tip(Hg, sp.sqrt(K) * U) / tip(H0, sp.sqrt(K) * U) * U / m), ell, 0)
    ctk = sp.simplify(ct * (K - 1) / K)
    tip_exact = (sp.simplify(ctk - 2 * (2 * K + 1) / (3 * K ** sp.Rational(3, 2))) == 0
                 and sp.limit(ctk, K, 1) == 2
                 and sp.simplify(sp.diff(ctk, K) + (2 * K + 3) / (3 * K ** sp.Rational(5, 2))) == 0)
    args = (u, w, U, W, ell, m)
    f0, fg = sp.lambdify(args, H0, "math"), sp.lambdify(args, Hg, "math")
    fq = sp.lambdify(args, Ht + Phi / 2 * H0, "math")                  # the test form without its f^(-1/2)
    worst, worst_q, positive = 0.0, 0.0, True
    for Kv in (1.001, 1.01, 1.1, 1.3, 1.5, 2.0, 3.0, 5.0, 10.0, 100.0, 1e4):
        for lu in (1e-12, 1e-6, 1e-3, 1e-1):
            UU, WW = 1e6, math.sqrt(Kv) * 1e6
            for i in range(601):
                t = (math.pi / 2) * i / 600
                uu, ww = UU * math.sin(t) + 1e-9 * UU, WW * math.cos(t)
                a0 = f0(uu, ww, UU, WW, lu * UU, 1.0)
                positive = positive and a0 > 0
                worst = max(worst, -fg(uu, ww, UU, WW, lu * UU, 1.0) / a0 * UU * (Kv - 1) / Kv)
                worst_q = max(worst_q, -fq(uu, ww, UU, WW, lu * UU, 1.0) / a0 * UU * (Kv - 1) / Kv)
    # the record's cover, K = 1.5: theta+ (1 + first order)/theta+ at its least
    UU, Kv = 419377.0, 1.5
    cover = min((f0(UU * math.sin(t) + 1e-9, math.sqrt(Kv) * UU * math.cos(t), UU, math.sqrt(Kv) * UU, 1e-6, 1.0)
                 + fg(UU * math.sin(t) + 1e-9, math.sqrt(Kv) * UU * math.cos(t), UU, math.sqrt(Kv) * UU, 1e-6, 1.0))
                / f0(UU * math.sin(t) + 1e-9, math.sqrt(Kv) * UU * math.cos(t), UU, math.sqrt(Kv) * UU, 1e-6, 1.0)
                for t in [(math.pi / 2) * i / 400 for i in range(401)])
    # (d) the wall's bending: the angle off the perpendicular, and its cost at the record's cover
    wb = m * ell / (3 * u)
    beta = sp.simplify((U * wb / W ** 2 - sp.diff(wb, u)).subs({u: U, W: sp.sqrt(K) * U}))
    beta_ok = sp.simplify(beta - (m * ell / (3 * U ** 2)) * (1 + 1 / K)) == 0
    cost = math.sqrt(lnl) * (1 + 1 / Kv) / (3 * UU * (2 + 1 / Kv))
    return dict(from_sigma=from_sigma, forms=forms, ratio=ratio, marg=marg, u_nl=u_nl, tip_exact=tip_exact,
                worst=worst, worst_q=worst_q, positive=positive, cover=cover, beta_ok=beta_ok, cost=cost)


def q21():
    reg = _register_rows()
    rows = list(Q21_ROWS)
    if MUT.get("e6_borne"):
        rows[2] = ("B5c", "lemmas/e_positive.py E6", "E7")          # the mutant: B5c read as resting on E6
    cites = [(k, w in reg.get(k, ""), bad not in reg.get(k, "").split(w, 1)[-1][:60]) for k, w, bad in rows]
    texts = [(f, t, t in _flat(os.path.join(HERE, f))) for f, t in Q21_TEXTS]
    return dict(cites=cites, texts=texts)


def compute():
    surv, ex = survivors()
    return dict(words=words_ok(), surv=surv, ex=ex, q5=q5(), q8=q8(), q14=q14(), q15=q15(), q16=q16(), q17=q17(),
                q20=q20(), q21=q21(), q23=q23())


def report(o):
    print("readings.py -- every board reading in force, and the proofs (item 354)\n")
    print("premises verbatim in their items: %d of %d" % (sum(o["words"].values()), len(o["words"])))
    for q, alts in o["ex"].items():
        print("%-4s survives: %s" % (q, "; ".join(o["surv"][q])))
    print("Q5  the horizon halves: %s; kept %s, one null surface: %s" % (o["q5"]["halves"], o["q5"]["keep"],
                                                                         o["q5"]["one_surface"]))
    print("Q8  isometries of -F(UV) dU dV: %s; the one taking II to IV and I to III: %s" % (o["q8"]["invariant"],
                                                                                         o["q8"]["keep"]))
    a = o["q14"]
    print("Q14 open period %.2f clocks, blueshift %.2g; dose %.2g to %.2g J; below Barcelo by %.0f and %.0f orders, "
          "below 1e-15 E by %.0f and %.0f" % (a["j1"], a["blue"], a["dose"][0], a["dose"][1], a["below_barcelo"][0],
                                              a["below_barcelo"][1], a["below_eq17"][0], a["below_eq17"][1]))
    print("Q15 the README's Shannon entropy %s, von Neumann %s" % (o["q15"]["shannon"], o["q15"]["von_neumann"]))
    print("Q16 E2/E = (G5/G5_2)^(1/3): %s; r_h2/r_h = (G5_2/G5)^(1/3): %s" % (o["q16"]["ratio"], o["q16"]["radius"]))
    print("Q17 content's share of mu: %s; at the hole (r_h/ell)^2 = %.2g" % (o["q17"]["rel"], o["q17"]["at_hole"]))
    print("Q20 our face %.3g clocks, position 2's at most %.2f: a factor %.2g" % (o["q20"]["life"], o["q20"]["open"],
                                                                                o["q20"]["factor"]))
    print("Q21 the rows' own citations: %s; the instruments' words found: %s"
          % (["%s %s" % (k, a and b) for k, a, b in o["q21"]["cites"]], [ok for _, _, ok in o["q21"]["texts"]]))
    g = o["q23"]
    print("Q23 GT's field from eq. (12) at every depth: %s; closed forms A = 4m/(3d), C = 2m(2Z^2 + u^2)/(3d^3): %s; "
          "round tip GT/test = 4(3U + 2 ell)/(9(U + ell)): %s, marginal ell %s; at N_L trapped for U > %.2f m; "
          "elongated c(K-1)/K exact at the tip: %s, sampled at most %.4f (test form's gradient part %.4f); theta+ "
          "positive: %s; least ratio at the record's cover %.6f; bending angle %s, cost %.2g of the rim's margin"
          % (g["from_sigma"], g["forms"], g["ratio"], g["marg"], g["u_nl"], g["tip_exact"], g["worst"], g["worst_q"],
             g["positive"], g["cover"], g["beta_ok"], g["cost"]))
    print("\nthe inventory: %d readings" % len(INVENTORY))
    for rid, item, text, rows, kind, state in INVENTORY:
        print("  %-8s %-4d %-8s %-58s %s" % (rid, item, kind, text[:58], state))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Q0 354's words and every premise verbatim, each inside its own item", all(o["words"].values()))
    add("Q1-Q4, Q6, Q13, Q16, Q18, Q19, Q22 exactly one alternative survives each, every exclusion a quoted premise or "
        "a named computation",
        all(len(v) == 1 for v in o["surv"].values())
        and all(p is None or p in WORDS or p.startswith("computed: ") for v in o["ex"].values() for _, p, _ in v))
    a = o["q5"]
    add("Q5 the four horizon halves: the future of I and the past of III kept, both on U = 0",
        a["halves"]["U=0,V>0"] == ("I", "future") and a["halves"]["U=0,V<0"] == ("III", "past")
        and sorted(a["keep"]) == ["U=0,V<0", "U=0,V>0"] and a["one_surface"])
    b = o["q8"]
    add("Q8 four discrete maps keep -F(UV) dU dV; only (-U, -V) takes II to IV and I to III",
        all(b["invariant"].values()) and b["keep"] == ["(-U,-V)"])
    c = o["q14"]
    add("Q14 the open period 33.60 clocks, the blueshift 3.9e14; the bath's dose 3.6e-57 to 4.4e-19 J, 65 and 27 "
        "orders below Barcelo's 0.28 E", "%.2f" % c["j1"] == "33.60" and "%.2g" % c["blue"] == "3.9e+14"
        and ["%.2g" % d for d in c["dose"]] == ["3.6e-57", "4.4e-19"]
        and [round(x) for x in c["below_barcelo"]] == [65, 27] and [int(x) for x in c["below_eq17"]] == [50, 12])
    d = o["q15"]
    add("Q15 one fixed exact encoding: Shannon entropy 0 and von Neumann entropy 0", d["shannon"] == 0
        and d["von_neumann"] == 0)
    add("Q16 E2/E = (G5/G5_2)^(1/3) and r_h2/r_h = (G5_2/G5)^(1/3) from C2's count at each side's l5",
        o["q16"]["ratio"] and o["q16"]["radius"])
    add("Q17 a content of X times the vacuum density adds X (r/ell)^2 of mu; (r_h/ell)^2 = 6.4e-31",
        o["q17"]["exact"] and "%.2g" % o["q17"]["at_hole"] == "6.4e-31")
    add("Q20 our face 8.57e14 clocks against position 2's 33.60: a factor 2.6e13",
        "%.2g" % o["q20"]["factor"] == "2.6e+13")
    add("Q21 RPOS2, RT5, RE6 and RO3H bear on no row: B5pu, B6', B5c and O3s cite their own entries, not the "
        "reading's, and the instruments' words are found", all(a and b for _, a, b in o["q21"]["cites"])
        and all(ok for _, _, ok in o["q21"]["texts"]))
    g = o["q23"]
    add("Q23 H-GT-IN-WARP: GT's own field (A = 4m/(3d), C = 2m(2Z^2 + u^2)/(3d^3), h55 = 0, from eq. (12) at every "
        "depth); the round tip 4(3U + 2 ell)/(9(U + ell)) of the test form's, marginal ell 2m; the elongated surface "
        "untrapped once U > 2 m K/(K - 1), inside L4 (b); the bending 6.3e-7 of the rim's margin",
        g["from_sigma"] and g["forms"] and g["ratio"] and [x for x in g["marg"] if x.is_finite] == [2 * sp.Symbol(
            "m", positive=True)] and "%.2f" % g["u_nl"] == "1.04" and g["tip_exact"] and g["worst"] < 2
        and g["worst_q"] < 2.25 and g["positive"] and g["cover"] > 0.99998 and g["beta_ok"]
        and "%.2g" % g["cost"] == "6.3e-07")
    add("the inventory: every reading with an item, rows, a kind and a state; the proved ones point at their entry",
        all(len(r) == 6 and r[4] in ("words", "form", "model", "choice", "protocol") for r in INVENTORY)
        and all(("Q" in r[5]) for r in INVENTORY if r[5].startswith("proved here")))
    return res


MUTANTS = {"word_wrong_item": "275's words looked for in item 276 (Q0)",
           "unexcluded": "the slab left unexcluded in Q3, two readings surviving (Q1-Q19)",
           "faces_swapped": "the faces taken as the past of I and the future of III (Q5)",
           "time_reflection": "Haggard and Rovelli's time reflection kept beside (-U, -V) (Q8)",
           "mixed_readme": "the README taken as a mixture of two strings (Q15)",
           "face_at_ours": "position 2's energy taken as (G5/G5_2)^1, one r_h (Q16)",
           "e6_borne": "B5c read as resting on e_positive E6, not E7 (Q21)",
           "h55_kept": "Garriga-Tanaka's h_ZZ kept equal to the angular part, not their h55 = 0 (Q23)"}


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
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-66s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
