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
  Q24 (computed, exact where marked; READ; deduced) H-HOLE-IN-WARP -- every conclusion FARs draws from its test form
     holds in the exact linear field of the README's mass on the warped bulk, near zone and far (FARs; far_small F4, F5).
     (a) Exact: Tangherlini's static slice is conformally flat, dr^2/(1 - mu/r^2) + r^2 dOmega_3^2 = psi^2 (d rho^2 +
     rho^2 dOmega_3^2) with r = rho psi, psi = 1 + mu/(4 rho^2) (computed) -- the test form is that slice under the warp,
     (ell/Z)^2 psi^2 delta. (b) The exact linear field, every zone. Garriga and Tanaka's eq. (11), static and mode by
     mode e^(ik.x), is Bessel's equation of order 2 in Z on each side, and their junction fixes the decaying solution:
     G_k(Z) = -K_2(kZ)/(2k K_1(k ell)) (computed, exact), so G = -(1/(4 pi^2 r)) int_0^oo sin(kr) K_2(kZ)/K_1(k ell) dk;
     its small-k limit is 2 ell/Z^2, eq. (16)'s zero mode. With eq. (12) at every depth (Q23 (a)) and m ell = (3 pi/8) mu
     (F5 (c)) this is the hole's linear field in the RS gauge at every distance (computed by quadrature): near the hole
     h00 = (mu/rho^2)(1 + O(rho/ell)) -- Tangherlini's, the brane's tension entering at first order in rho/ell, the
     coefficient about 2.7 -- and far away Q23's closed forms, matched to 1e-3. (c) theta+ on T_E in that field, to first
     order (computed, sampled at U/ell from 1e-3 to 1e3, W/U = 1, 1.5^(1/2), 3^(1/2), w >= 0.02 U and u >= 1e-3 U, the
     rim by continuity): its relative lowering never exceeds 5 mu/min(U, ell)^2. In the near zone it is about 0.7 mu/U^2,
     the test form's own figure 0.75 to 0.89; far out the elongated surface's falls as m/U and the round tip's tends to
     2m/ell, Q23 (b)'s. (d) At every README of the small end the parameter is max((r_h/U)^2, (r_h/ell)^2): 5.05e-11 at
     the example, so theta+ moves by at most 2.5e-10 of itself, and 0.012 at N = 1e3 (U = 9.0 r_h), at most 0.06.
     Position 2's side, with its own face's mu up to 4^(2/3) r_h^2 (V6), scales by at most 2.52. Smaller READMEs, with U
     near r_h, are outside linear theory; there F5 (a)'s exact spherical result holds (a round sphere untrapped exactly
     while mu < r^2), with corrections O(U/ell) from the warp. (e) The wall's bending: xi5 = m ell/(3r) = (pi/8) mu/r
     (eq. (22)), so beta = (pi/8)(mu/U^2)(1 + 1/K), and rounding the kink over eps = U beta^(1/2) costs at most
     beta^(1/2)/(2 + 1/K) of the rim's margin -- 2.2e-6 at the example (Q23 (d)'s argument). So the test form carries no
     weight of its own: any field of the size (b) computes gives FARs's conclusions, nine orders inside the margin at the
     example.  The field is the Z2-symmetric wall's; on the two-sided pair each side's differs by a factor of order one
     (far_large L9 (d)'s estimate), which those nine orders absorb.
  Q25 (deduced; computed) RCOVER -- the record's cover U = 1.05 R_reach carries no weight: FARs and FAR hold on every far
     surface enclosing the write's reach (FARs F4; FAR L5, L9).  (a) What the cover must do is causal: T_E keeps
     coordinate distance at least U from the origin, and no signal from the corridor or the README's own matter -- inside
     R_core + T when the write began, spreading at most T further by the closing -- reaches it before the closing once U
     >= R_reach = R_core + 2T (b4c_far's reach, the model's cones), R_core = r_h at the small end and 2m at the large;
     the factor 1.05 is the record's margin on that, not a requirement.  (b) The small end: F3 is exact at every U, F4's
     round margin mu/(4U^2) + mu/(2U ell) < 1 holds at every U > r_h, and Q24's bound 5 mu/min(U, ell)^2 falls as U grows
     -- at the reach itself, U = 133,961 r_h at the example, mu/U^2 = 5.57e-11 and theta+ moves by at most 2.8e-10 of
     itself, against 5.05e-11 and 2.5e-10 at the cover (computed).  (c) The large end: at every U past the reach an
     elongation serves -- Q23's bound in Garriga and Tanaka's field needs K > U/(U - 2m), L4 (b)'s in the test form K >=
     4U/(4U - 9m) -- and at the reach itself, U = 399,406.38 m, these are K - 1 > 5.0e-6 and 5.6e-6, against 4.8e-6 and
     5.4e-6 at the cover (computed).  Each bound loosens as U grows (computed), so any U >= R_reach serves, the cover
     among them; the round surface's failure at the large end does not depend on the cover either, its threshold U > 2
     ell (ell + 3m)/(3m - 2 ell) lying far inside R_reach.
  Q26 (deduced; computed where marked) write_small S3's five mappings, on which the write's floor of 66,980 clocks rests
     (WRITEs, O3s, FARs's reach).  (a) H-WRITE-IS-ARRIVAL -- the write is done when the README has crossed onto the
     horizon.  The option M chose at 163 says what the write is: "the README carried in by the inflow, 115 (c), and held
     as a single whole, not bit by bit, at the fixed size".  Alternatives: the write done before the README arrives, a
     transport after it -- excluded: the write is the carrying in; the write still running after the README is in, part
     by part -- excluded by "held as a single whole, not bit by bit"; the write is done when the README is in --
     survives, and on 340's compact arrival (Q2) being in is the arrival that forms the face.  (b) H-SMALL-CLOCK -- the
     clock r_h/c.  A unit: every comparison a row draws is a ratio in one clock, the life 1.28e10 floors in any
     (computed); in seconds the floor is 2.5e-24 s at the example.  (c) H-HOLD-FRAME -- advanced time.  M's since 334:
     M-HOLD-IS-THE-FACE seats the hold as "our face open, in advanced time, through the write".  (d) H-FLAT-START -- the
     plane and the bulk flat at the write's start.  On 340's reading (ii) no hole stands during the approach -- the
     README forms the face as it arrives -- so the only fields are the README's own: (r_h/R)^2 = 2.2e-10 at the start and
     R/ell = 5.4e-11 (computed), reaching order one only within the arrival's last 4.79 clocks (Q2's width), 7.2e-5 of
     the floor (computed).  (e) H-README-ALONE -- the gas carries only the README's E.  Alternative, a carrier with more
     energy than E, up to the collapse ('t Hooft's eq. (8), S3 V4) -- excluded by 136 G, "the README is the energy, not
     separate", and 136 (1), the one exact energy E(N): the carrier's energy is the README's, E.  So the floor rests on
     M's rulings, Q2 and two computed bounds; S3's own derivation is C6's, verified (264).
  Q27 (READ; computed) H-SPECIES-FINITE -- finitely many species above the Standard Model (WRITEs, O3s, B4ds) -- is
     replaced by a bound the hole sets itself.  READ, as C5 U11 (8) reads them (verified with C5, 317): Dvali and Redi,
     "black-holes smaller than Lambda_G^{-1} are already no longer semi-classical", and in D dimensions "M_D^{D-2} >~ N
     Lambda^{D-2}"; so a five-dimensional hole of radius r_h is semiclassical, as every figure here assumes, only for at
     most (r_h/l5)^3 = 3.85e14 species (computed).  What the rows draw on, at every count up to that cap (computed; the
     life as 1/Z, the floor's 1 + T as Z^(-1/3)): the hole's life against the write's floor -- 238 clocks against 4.37 at
     the cap, 54 times, the conclusions failing only past 1.55e17 species; the life against the README's three-clock stay
     -- 79 times at the cap, failing only past 3.05e16; and B4ds D6's place -- the curvature Planckian at 2.91 l5 with
     176 bits, which no count moves, the time left there 2.2e-3 clocks at 106.75 and shorter as 1/Z.  So no row's
     conclusion needs the species finite beyond what its own hole imposes.  One number does move: WRITEs' "66,980 clocks"
     is the floor at the Standard Model's 106.75, the species lighter than the gas's 5.6 TeV (write_small S3), and it
     falls to 4.37 clocks at the cap -- the row's figure is the Standard Model's, its claim (the bulk held through the
     write) holds at every count.  Recorded for the row, not repaired here.
  Q28 (read; deduced) RCALC -- c4_oneway's calculator protocols, P13 (the form of C4's question), P17 (the continuation
     as one condition), P18 (the README's density scaling with position 2's tension) and P20 (the channel reading of a
     binary communication) -- carry no weight on M1s.  M1s's claim is P6's: "So M1 holds at the small end on the one-way
     object on (a)-(f) at flat order in classical GR", concluded from P1-P5 -- the Komar mass (P1, m1_small N1, verified
     269), the totally geodesic equator in every chart (P2, exact), clause (e) on both faces (P3), clause (f) between
     universes (P4, e_positive E7 and P19's tau_share, exact), and the state (P5).  None of P1-P6 cites P13, P17 or P20;
     P18 appears once, beside P4's own reading of position 2's tension, which the verifier's (7) found positive a
     fortiori on the side total (read in the file, checked).  The protocols decide how the calculator is asked (P7-P20);
     its agreement is the standing check beside the proof -- every question through the calculator or stated NOT-RUN --
     not a premise of it.  The register's M1s row rests on m1_small and c4_oneway, both verified (269, 310).
  Q29 (computed, exact; READ; deduced) RSHELL -- the README as Haggard and Rovelli's thin null shell (O1cs, O1bs) --
     carries no weight beyond RDUST, the README as radial null dust: the thin shell is that model's step profile, and
     O1c's conclusions hold on every profile. Computed, on the ingoing Vaidya form -(1 - mu(v)/r^2) dv^2 + 2 dv dr + r^2
     dOmega_3^2 with mu(v) arbitrary: the Ricci tensor is R_vv = (3/2) mu'/r^3 alone, so R = R_ab R^ab = 0, and the
     Kretschmann scalar is exactly 72 mu^2/r^8, with no term in mu'. The README's energy is positive (ARRIVALs V1), so
     mu' >= 0 and mu <= r_h^2: every profile's curvature is at most the finished hole's at the same r, and reaches the
     five-dimensional Planck scale only at r_c = 72^(1/8) (r_h l5)^(1/2) = 7.09e-23 m, where 273's region begins (B4ds
     D4). Deduced: the geodesic equations' coefficients are bounded away from r = 0 for bounded mu and mu' -- a step, the
     thin shell, is crossed with the metric continuous (Barrabes and Israel, as o1c_oneway Z2b READs them) -- so a causal
     geodesic can end only by reaching r_c, the quantum region, complete by 273. And Z2b's causal argument -- v never
     decreasing along a future causal curve, the region the README has not yet swept the undisturbed bulk -- holds for
     any converging matter, as o1c_oneway's item-337 note records (Z8 (Q2), (Q7), (Q8)): "Z2b's causal argument needs
     neither". So the shell carries nothing RDUST does not; the README's true form, a gas of our plane's fields (344), is
     SOURCEs's to define, and RSHELL goes through SOURCE with RDUST (M-SOURCE-LAST).
  Q30 (computed, exact; deduced; estimate where marked) FARs rests on neither of the two readings the inventory listed
     for it that go through SOURCE.  (a) RGAS, the carrier a free gas, enters FARs only through the write's floor T,
     which sets the reach the cover must enclose; FARs holds at every U past the reach whatever T is (Q25).  (b) RDUST,
     the README as radial null dust, enters through F5 (a), and F5 (a) does not need it: on every spherically symmetric
     metric, -e^(2 Phi)(1 - mu/r^2) dt^2 + dr^2/(1 - mu/r^2) + r^2 dOmega_3^2 with mu and Phi functions of t and r, g^ab
     d_a r d_b r = 1 - mu/r^2 and G^t_t = -(3/(2 r^3)) d_r mu (computed, exact), so the README's positive energy gives
     d_r mu = (2 kappa/3) r^3 rho >= 0 and mu <= r_h^2 outside the face, its E the only energy (Q26 (e)) -- every round
     sphere outside r_h untrapped at every stage, for every spherical README, null dust or a gas or anything else.  A
     README that is not spherical -- written on our plane, SO(3) -- is F5 (b)'s: inside the reach, it lies at least U -
     (1 + T) r_h = 0.52 U from T_E at the write's start and only further after, so its field there is at most 3.64 times
     the centred field's scale (computed), and by Q24's bound it moves theta+ by about 10 mu/U^2 x 3.64, 2e-9 at the
     example (estimate: the constant for an off-centre source taken as twice the centred one's).  So every reading FARs
     rests on is proved or M's.
  Q31 (item 356; deduced; READ; computed) RGAS -- H-BITS-ARE-STATES and H-FREE-GAS, the carrier of write_small S3
     (WRITEs, O3s, ARRIVALs) -- proved.  (a) H-BITS-ARE-STATES, N bits need e^S >= 2^N.  Every README of N bits carries
     the one energy E(N) (136 (1), a function of N alone), and the rebuild has "no tolerance at all" (146): each of the
     2^N READMEs must be told from every other with zero error.  Two pure states are told apart with zero error only if
     they are orthogonal -- the least error at equal priors is (1 - (1 - |<psi|phi>|^2)^(1/2))/2, zero only at overlap
     zero (computed, exact) -- and 2^N mutually orthogonal states need a space of dimension 2^N (computed).  So the
     carrier's states at energy E in the volume it fills number at least 2^N: e^S(E, V) >= 2^N, S the microcanonical
     entropy.  (b) H-FREE-GAS, those states at most the free gas's.  The carrier is M's since 344: "its true source is a
     gas of the plane's fields".  At the gas's temperature, 5.6 TeV (S3), every Standard Model species is relativistic,
     and the free massless gas has S = (4/3) a^(1/4) V^(1/4) E^(3/4).  Interactions shift it.  READ: Kajantie, Laine,
     Rummukainen and Schroder (hep-ph/0211321) eqs. (6.4)-(6.7), p_QCD = (8 pi^2/45) T^4 [sum p_i (alpha_s/pi)^(i/2)]
     with p0 = 1 + 21 N_f/32 and p2 = -(15/4)(1 + 5 N_f/12), the first correction negative -- with their caution that the
     series "could well converge only very slowly, requiring perhaps something like T >> TeV" -- and Borsanyi et al.
     (1309.5258) find the continuum pressure below "the Stefan-Boltzmann value of 5.209" at every temperature they reach.
     Whatever the sign beyond leading order, a shift delta in the pressure moves the ball's radius, and so the floor, by
     (1 + delta)^(-1/3) exactly (computed): by at most 6% and 8% for |delta| <= 0.2.  So the free gas bounds the carrier
     to leading order and the floor of 66,980 clocks stands within that band; the number of species it uses is the
     Standard Model's (Q27).

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
and three instruments' texts, by path.  Stdlib + sympy; numpy and scipy for Q24's quadratures.
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
    "163.opt": (163, "the README carried in by the inflow, 115 (c), and held as a single whole, not bit by bit, at the "
                     "fixed size"),
    "334.frame": (334, "our face open, in advanced time, through the write"),
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
    "Q26a": [("the write done before the README arrives, a transport after it", "163.opt",
              "the write is the carrying in"),
             ("the write running on after the README is in, part by part", "163.opt",
              "held as a single whole, not bit by bit"),
             ("the write done when the README is in", None, "survives; on 340's compact arrival (Q2), the arrival")],
    "Q26e": [("a carrier with more energy than E, up to the collapse (S3 V4)", "136.G",
              "the README is the energy, not separate; one exact energy, 136 (1)"),
             ("the carrier's energy the README's, E", None, "survives")],
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
    ("RDUST", 338, "the README arriving as radial null dust", "ARRIVALs B4ds", "model",              # [Q30] not FARs
     "through SOURCE (M-SOURCE-LAST): SOURCEs replaces it"),
    ("RBITS", 338, "H-BITS-WITH-ENERGY: the bits come in with the energy", "ARRIVALs", "model",
     "through SOURCE (M-SOURCE-LAST)"),
    ("RSHELL", 337, "the README as Haggard and Rovelli's thin null shell", "O1cs O1bs", "model",
     "no weight beyond RDUST (Q29); through SOURCE with it (M-SOURCE-LAST)"),
    ("RHOLE", 349, "H-HOLE-IN-WARP: the hole's isotropic factor under the warp", "FARs", "form",
     "proved here (Q24)"),
    ("RGT", 350, "H-GT-IN-WARP: Garriga-Tanaka's far field under the warp", "FAR", "form", "proved here (Q23)"),
    ("RCOVER", 349, "the record's cover U = 1.05 R_reach", "FARs FAR", "choice", "proved here (Q25)"),
    ("RONPLANE", 264, "H-README-ON-PLANE: the README written in our plane's fields", "WRITEs O3s FARs ARRIVALs",
     "model", "M's since 344 (\"The README is really written on our plane\")"),
    ("RGAS", 264, "H-FREE-GAS, H-BITS-ARE-STATES: the carrier a free gas holding 2^N states",
     "WRITEs O3s ARRIVALs", "model",                                                                 # [Q30] not FARs
     "proved here (Q31; item 356)"),
    # [Q26] write_small's mappings, once one entry (RMAP), each its own
    ("RWIA", 264, "H-WRITE-IS-ARRIVAL: the write done when the README is in", "WRITEs O3s FARs", "choice",
     "proved here (Q26 (a))"),
    ("RCLOCK", 264, "H-SMALL-CLOCK: the clock r_h/c", "WRITEs O3s FARs", "choice", "a unit; proved here (Q26 (b))"),
    ("RFRAME", 264, "H-HOLD-FRAME: the write in advanced time", "WRITEs O3s FARs", "choice",
     "M's since 334, M-HOLD-IS-THE-FACE (Q26 (c))"),
    ("RFLAT", 264, "H-FLAT-START: the plane and the bulk flat at the write's start", "WRITEs O3s FARs", "model",
     "proved here (Q26 (d))"),
    ("RALONE", 264, "H-README-ALONE: the gas carries only the README's E", "WRITEs O3s FARs", "model",
     "proved here (Q26 (e))"),
    ("RSPEC", 264, "H-SPECIES-FINITE: finitely many species above the Standard Model", "WRITEs O3s B4ds", "model",
     "replaced by a READ bound; proved here (Q27)"),
    ("RCALC", 310, "c4_oneway's calculator protocols (P13, P17, P18, P20)", "M1s", "protocol",
     "bears on no row's claim (Q28)"),
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


# ---------------------------------------------------------------------------------- Q24 the hole's exact linear field
def _rs_field(r, Z, flat=False):
    """the exact linear RS field of a brane point mass at (r, Z), mu = ell = 1: A, C, A_r, A_Z, C_r, C_Z, v"""
    import numpy as np
    from scipy import integrate, special
    w = Z - 1.0
    if flat:                                                           # the mutant: flat five-dimensional space
        f = lambda k: math.exp(-k * w)
        fZ = lambda k: -k * math.exp(-k * w)
    else:
        f = lambda k: special.kve(2, k * Z) / special.kve(1, k) * math.exp(-k * w)
        fZ = lambda k: (k * (-special.kve(1, k * Z) - 2 / (k * Z) * special.kve(2, k * Z)) / special.kve(1, k)
                        * math.exp(-k * w))

    def s_(k):
        x = k * r
        return k * r ** 3 / 3 * (1 - x * x / 10) if x < 1e-3 else (math.sin(x) - x * math.cos(x)) / k ** 2
    a = 40.0 / max(r, w)
    q = lambda g: integrate.quad(g, 0, a, limit=800, epsabs=0, epsrel=1e-10)[0]
    qf = lambda g, kind: integrate.quad(g, a, np.inf, weight=kind, wvar=r, limlst=400)[0]
    J0 = q(lambda k: f(k) * math.sin(k * r)) + qf(f, "sin")
    J1 = q(lambda k: k * f(k) * math.cos(k * r)) + qf(lambda k: k * f(k), "cos")
    Jz = q(lambda k: fZ(k) * math.sin(k * r)) + qf(fZ, "sin")
    I0 = q(lambda k: f(k) * s_(k)) + qf(lambda k: f(k) / k ** 2, "sin") - r * qf(lambda k: f(k) / k, "cos")
    Iz = q(lambda k: fZ(k) * s_(k)) + qf(lambda k: fZ(k) / k ** 2, "sin") - r * qf(lambda k: fZ(k) / k, "cos")
    c = -3 / 8                                                         # V/a^2 = -(m ell/pi) Z^2 J0/r, m ell = 3 pi/8
    v, v_r, v_Z = c * Z ** 2 * J0 / r, c * Z ** 2 * (J1 / r - J0 / r ** 2), c * (2 * Z * J0 + Z ** 2 * Jz) / r
    I, I_r, I_Z = c * Z ** 2 * I0, r ** 2 * v, c * (2 * Z * I0 + Z ** 2 * Iz)
    A, A_r, A_Z = -8 * I / (3 * r ** 3), -8 * I_r / (3 * r ** 3) + 8 * I / r ** 4, -8 * I_Z / (3 * r ** 3)
    C = -4 / 3 * v + 4 * I / (3 * r ** 3)
    C_r = -4 / 3 * v_r + 4 * I_r / (3 * r ** 3) - 4 * I / r ** 4
    C_Z = -4 / 3 * v_Z + 4 * I_Z / (3 * r ** 3)
    return A, C, A_r, A_Z, C_r, C_Z, v


def q24():
    rho, mu, k, Zs, ell = sp.symbols("rho mu k Z ell", positive=True)
    psi = 1 + mu / (4 * rho ** 2)
    rr = rho * psi
    slice_ok = sp.simplify(sp.diff(rr, rho) ** 2 / (1 - mu / rr ** 2) - psi ** 2) == 0
    G = sp.besselk(2, k * Zs)
    mode_ok = sp.simplify(Zs ** 2 * sp.diff(G, Zs, 2) + Zs * sp.diff(G, Zs) - k ** 2 * Zs ** 2 * G - 4 * G) == 0
    jump = 2 * sp.diff(G, Zs).subs(Zs, ell) + 4 * G.subs(Zs, ell) / ell + 2 * k * sp.besselk(1, k * ell)
    jump_ok = abs(sp.N(jump.subs({k: 0.9, ell: 1.7}))) < 1e-12 and abs(sp.N(jump.subs({k: 3.1, ell: 0.4}))) < 1e-12
    zero_mode = sp.limit(sp.besselk(2, k * Zs) / sp.besselk(1, k * ell) * k, k, 0) == 2 * ell / Zs ** 2
    flat = bool(MUT.get("flat_green"))
    # the field: near the hole against Tangherlini's h00, far away against Q23's closed forms
    v = _rs_field(1e-3, 1.001, flat)[6]
    near = -8 / 3 * v * 2e-6                                           # h00 rho^2/mu at rho^2 = 2e-6 ell^2
    m = 3 * math.pi / 8
    A, C = _rs_field(1000.0, 400.0, flat)[:2]
    d = math.hypot(1000.0, 400.0)
    far = max(abs(A / (4 * m / (3 * d)) - 1), abs(C / (2 * m * (2 * 400.0 ** 2 + 1e6) / (3 * d ** 3)) - 1))
    # theta+ on T_E: the generic first-order H with A, h_ZZ = 0, C and their first derivatives (ell = 1)
    u, w, U, W, eps = sp.symbols("u w U W epsilon", positive=True)
    sy = sp.symbols("a0 c0 au aw cu cw")
    Af, Cf = sp.Function("A")(u, w), sp.Function("C")(u, w)
    Om2 = (1 / (1 + w)) ** 2
    guu, gww, goo = Om2 * (1 + eps * Af), Om2, Om2 * u ** 2 * (1 + eps * Cf)
    F = u ** 2 / U ** 2 + w ** 2 / W ** 2
    Fu, Fw = sp.diff(F, u), sp.diff(F, w)
    nrm = sp.sqrt(Fu ** 2 / guu + Fw ** 2 / gww)
    sq = sp.sqrt(guu * gww) * goo
    H = (sp.diff(sq * Fu / guu / nrm, u) + sp.diff(sq * Fw / gww / nrm, w)) / sq
    H0 = H.subs(eps, 0).doit()
    H1 = sp.diff(H, eps).subs(eps, 0).doit().subs({sp.Derivative(Af, u): sy[2], sp.Derivative(Af, w): sy[3],
                                                    sp.Derivative(Cf, u): sy[4], sp.Derivative(Cf, w): sy[5]})
    H1 = H1.subs({Af: sy[0], Cf: sy[1]})
    f0 = sp.lambdify((u, w, U, W), H0, "math")
    f1 = sp.lambdify((u, w, U, W) + sy, H1, "math")
    table = {}
    for Uv in (1e-3, 0.1, 1.0, 10.0, 1e3):
        for Kv in (1.0, 1.5, 3.0):
            Wv, worst = math.sqrt(Kv) * Uv, 0.0
            for i in range(41):
                t = (math.pi / 2) * i / 40
                uu, ww = max(Uv * math.sin(t), 1e-3 * Uv), max(Wv * math.cos(t), 0.02 * Uv)
                A, C, Ar, AZ, Cr, CZ, v = _rs_field(uu, 1.0 + ww, flat)
                worst = max(worst, -f1(uu, ww, Uv, Wv, A, C, Ar, AZ, Cr, CZ) / f0(uu, ww, Uv, Wv))
            table[(Uv, Kv)] = worst * min(Uv, 1.0) ** 2                # in units of mu/min(U, ell)^2
    beta_ex = (math.pi / 8) * 5.05e-11 * (1 + 1 / 1.5)
    return dict(slice_ok=slice_ok, mode_ok=mode_ok, jump_ok=jump_ok, zero_mode=zero_mode, near=near, far=far,
                table=table, smax=max(table.values()), example=5 * 5.05e-11, bend=math.sqrt(beta_ex) / (2 + 1 / 1.5))


# ---------------------------------------------------------------------------------- Q25 every cover past the reach
def q25():
    T_s, T_l = 66980, 199702.19                                         # the writes' floors (write_small S3, o3_write)
    small = {}
    for lab, U in (("reach", 1 + 2 * T_s), ("cover", 1.05 * (1 + 2 * T_s))):
        small[lab] = dict(U=U, mu_U2=1 / U ** 2, bound=5 / U ** 2,     # Q24's bound, mu/min(U, ell)^2 with U << ell
                          round_ok=1 / (4 * U ** 2) + 1 / (2 * U * 1.25e15) < 1)     # F4's round margin, ell/r_h
    large = {}
    for lab, U in (("reach", 2 + 2 * T_l), ("cover", 1.05 * (2 + 2 * T_l))):
        Ug = U if not MUT.get("cover_needed") else 1.0                  # the mutant: the cover read as the reach itself
        large[lab] = dict(U=U, k_gt=2 / (Ug - 2), k_test=9 / (4 * Ug - 9))     # K - 1 above which each bound holds
    # each bound loosens as U grows: d/dU of mu/U^2, 2/(U - 2) and 9/(4U - 9) all negative
    Us = sp.Symbol("U", positive=True)
    monotone = all(sp.simplify(sp.diff(e, Us)).subs(Us, 10) < 0 for e in (1 / Us ** 2, 2 / (Us - 2), 9 / (4 * Us - 9)))
    return dict(small=small, large=large, monotone=monotone)


# ---------------------------------------------------------------------------------- Q26 write_small's five mappings
def q26():
    floor, life, arrival = 66980.0, 8.573276e14, 4.79                   # clocks of r_h/c (S3; C5 U4; Q2's width)
    clock_s = 1.12008e-20 / 299792458.0                                 # r_h/c at the example, s
    # H-SMALL-CLOCK: the comparison is a ratio, the same in every clock; in seconds the floor is 2.5e-24 s
    ratio, ratio_s = life / floor, (life * clock_s) / (floor * clock_s)
    if MUT.get("clock_weighs"):
        ratio_s = (life * clock_s) / floor                              # the mutant: two clocks mixed
    # H-FLAT-START: the README's own gravity at the start, and the warp; at most the arrival's width against the floor
    R = (1 + floor)                                                     # the ball's radius at the start, r_h
    return dict(ratio=ratio, ratio_same=abs(ratio_s / ratio - 1) < 1e-12, floor_s=floor * clock_s,
                selfgrav=1 / R ** 2, warp=R * 8.02117e-16, shift=arrival / floor)


# ---------------------------------------------------------------------------------- Q27 species bounded by the hole
def q27():
    N, rh, l5, Z0, life0 = 2742570311524972, 1.12008e-20, 1.53937e-25, 106.75, 8.573276e14
    cap = (rh / l5) ** 3                                                # Dvali-Redi: N_species <~ (r_h/l5)^3 in 5D
    life = lambda Z: life0 * Z0 / Z                                     # the life as 1/Z (hold_small)
    head = lambda Z: 1.5 * (5 * N * math.log(2) / Z) ** (1 / 3)         # 1 + T, write_small S3's head
    if MUT.get("floor_fixed"):
        head = lambda Z: 1.5 * (5 * N * math.log(2) / Z0) ** (1 / 3)    # the mutant: the floor held at the SM's count
    fail_stay = life0 * Z0 / 3                                          # the life down to the three-clock stay
    fail_floor = (life0 * Z0 / (1.5 * (5 * N * math.log(2)) ** (1 / 3))) ** 1.5    # the life down to the floor
    return dict(cap=cap, life_cap=life(cap), head_cap=head(cap), head_sm=head(Z0), ratio=life(cap) / head(cap),
                stay_ratio=life(cap) / 3, fail_stay=fail_stay, fail_floor=fail_floor, d6_left=2.2e-3 * Z0 / cap)


# ---------------------------------------------------------------------------------- Q28 the protocols carry no weight
def q28():
    src = open(os.path.join(HERE, "c4_oneway.py"), encoding="utf-8").read()
    doc = src.split('"""')[1]
    end = "\n  P14 " if MUT.get("calc_premise") else "\n  P7 "        # the mutant: the calculator's runs as premises
    block = " ".join(doc[doc.index("\n  P1 "):doc.index(end)].split())
    proto = {t: len(re.findall(r"\b%s\b" % t, block)) for t in ("P13", "P17", "P18", "P20")}
    p18_beside = "while P4 and P18 read P2's tension for (f) as 139 (1)'s own -sigma/4" in block
    concl = "So M1 holds at the small end on the one-way object on (a)-(f) at flat order in classical GR" in block
    row = _register_rows().get("M1s", "")
    return dict(proto=proto, p18_beside=p18_beside, concl=concl,
                row_ok="lemmas/m1_small.py (C4 verified, 269); lemmas/c4_oneway.py (C4 one-way verified, 310)" in row)


# ---------------------------------------------------------------------------------- Q29 every null-dust profile
def q29():
    v, r, a, b, c = sp.symbols("v r theta1 theta2 theta3", positive=True)
    mu = sp.Function("mu")(v, r) if MUT.get("mass_in_r") else sp.Function("mu")(v)    # the mutant: mu depends on r
    X, n = [v, r, a, b, c], 5
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -(1 - mu / r ** 2), 1, 1
    g[2, 2], g[3, 3], g[4, 4] = r ** 2, r ** 2 * sp.sin(a) ** 2, r ** 2 * sp.sin(a) ** 2 * sp.sin(b) ** 2
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                             for l in range(n)) / 2) for k in range(n)] for j in range(n)] for i in range(n)]

    def riem(i, j, k, l):                                              # R^i_jkl
        e = sp.diff(Gam[i][j][l], X[k]) - sp.diff(Gam[i][j][k], X[l])
        return sp.simplify(e + sum(Gam[i][k][m] * Gam[m][j][l] - Gam[i][l][m] * Gam[m][j][k] for m in range(n)))
    R = [[[[riem(i, j, k, l) for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.Matrix(n, n, lambda j, l: sp.simplify(sum(R[i][j][i][l] for i in range(n))))
    Rs = sp.simplify(sum(gi[j, l] * Ric[j, l] for j in range(n) for l in range(n)))
    RR = sp.simplify(sum(Ric[i, j] * gi[i, p] * gi[j, q] * Ric[p, q] for i in range(n) for j in range(n)
                         for p in range(n) for q in range(n)))
    Rl = [[[[sp.simplify(sum(g[i, m] * R[m][j][k][l] for m in range(n))) for l in range(n)] for k in range(n)]
           for j in range(n)] for i in range(n)]
    nz = [(i, j, k, l) for i in range(n) for j in range(n) for k in range(n) for l in range(n) if Rl[i][j][k][l] != 0]
    K = sp.simplify(sum(Rl[i][j][k][l] * sum(gi[i, p] * gi[j, q] * gi[k, s_] * gi[l, t] * Rl[p][q][s_][t]
                                             for p, q, s_, t in nz) for i, j, k, l in nz))
    others = [(i, j) for i in range(n) for j in range(n) if (i, j) != (0, 0) and Ric[i, j] != 0]
    ricci_ok = not others and sp.simplify(Ric[0, 0] - sp.Rational(3, 2) * sp.diff(mu, v) / r ** 3) == 0
    rc = 72 ** 0.125 * math.sqrt(1.12008e-20 * 1.53937e-25)           # where 72 mu^2/r^8 = l5^-4 at mu = r_h^2
    z2b = "Z2b's causal argument needs neither" in _flat(os.path.join(HERE, "o1c_oneway.py"))
    return dict(ricci_ok=ricci_ok, R0=Rs == 0 and RR == 0, K_ok=sp.simplify(K - 72 * mu ** 2 / r ** 8) == 0, rc=rc,
                z2b=z2b)


# ---------------------------------------------------------------------------------- Q30 FARs rests on no SOURCE reading
def q30():
    t, r, a, b, c = sp.symbols("t r theta1 theta2 theta3", positive=True)
    mu, Ph = sp.Function("mu")(t, r), sp.Function("Phi")(t, r)
    X, n = [t, r, a, b, c], 5
    f = 1 - mu / r ** 2
    g = sp.diag(-sp.exp(2 * Ph) * f, 1 / f, r ** 2, r ** 2 * sp.sin(a) ** 2, r ** 2 * sp.sin(a) ** 2 * sp.sin(b) ** 2)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                             for l in range(n)) / 2) for k in range(n)] for j in range(n)] for i in range(n)]

    def ric(j, l):
        e = sum(sp.diff(Gam[i][j][l], X[i]) - sp.diff(Gam[i][j][i], X[l]) for i in range(n))
        e += sum(Gam[i][i][m] * Gam[m][j][l] - Gam[i][l][m] * Gam[m][j][i] for i in range(n) for m in range(n))
        return sp.simplify(e)
    Ric = sp.Matrix(n, n, lambda j, l: ric(j, l))
    Rs = sp.simplify(sum(gi[j, l] * Ric[j, l] for j in range(n) for l in range(n)))
    Gtt = sp.simplify((gi * (Ric - Rs * g / 2))[0, 0])                 # G^t_t
    k_ms = sp.Rational(1, 2) if MUT.get("ms_4d") else sp.Rational(3, 2)  # the mutant: the four-dimensional coefficient
    ms_ok = sp.simplify(Gtt + k_ms * sp.diff(mu, r) / r ** 3) == 0
    gab_rr = sp.simplify(gi[1, 1]) == sp.simplify(f)                  # g^ab d_a r d_b r = 1 - mu/r^2
    # a README off the centre: T_E at U = 1.05 (1 + 2T) r_h, the README within (1 + T) r_h at the write's start
    T = 66980
    U, R0 = 1.05 * (1 + 2 * T), 1 + T
    near = (U / (U - R0)) ** 2                                          # its field's scale at T_E against the centre's
    return dict(ms_ok=ms_ok, gab_rr=gab_rr, near=near, offc=10 * near / U ** 2)


# ---------------------------------------------------------------------------------- Q31 the carrier's states
def q31():
    # (a) zero error between two pure states needs them orthogonal: the least error, equal priors (Helstrom)
    c = sp.Symbol("c", nonnegative=True)                               # |<psi|phi>|
    perr = (1 - sp.sqrt(1 - c ** 2)) / 2
    zero_only_orth = sp.solve(sp.Eq(perr, 0), c) == [0]
    if MUT.get("tolerance"):
        zero_only_orth = sp.solve(sp.Eq(perr, sp.Rational(1, 100)), c) == [0]   # the mutant: an error allowed
    # 2^N mutually orthogonal states need dimension 2^N: the Gram matrix of orthonormal vectors has full rank
    rank_ok = all(sp.eye(2 ** n).rank() == 2 ** n for n in range(1, 5))
    # (b) the free gas at fixed E, V and the floor's response to an interaction shift delta in the pressure
    a, V, E, N, d = sp.symbols("a V E N delta", positive=True)
    S = sp.Rational(4, 3) * a ** sp.Rational(1, 4) * V ** sp.Rational(1, 4) * E ** sp.Rational(3, 4)
    Vmin = sp.solve(sp.Eq(S, N * sp.log(2)), V)[0]
    R_ratio = sp.simplify((Vmin.subs(a, a * (1 + d)) / Vmin) ** sp.Rational(1, 3))    # the ball's radius, so the floor
    exact = sp.simplify(R_ratio - (1 + d) ** sp.Rational(-1, 3)) == 0
    nf = 6                                                              # every quark below 5.6 TeV
    p0, p2 = 1 + sp.Rational(21, 32) * nf, -sp.Rational(15, 4) * (1 + sp.Rational(5, 12) * nf)   # KLRS eqs. (6.5), (6.7)
    return dict(zero_only_orth=zero_only_orth, rank_ok=rank_ok, exact=exact,
                band=[float(R_ratio.subs(d, x)) for x in (-0.2, 0.2)], p0=p0, p2=p2)


def compute():
    surv, ex = survivors()
    return dict(words=words_ok(), surv=surv, ex=ex, q5=q5(), q8=q8(), q14=q14(), q15=q15(), q16=q16(), q17=q17(),
                q20=q20(), q21=q21(), q23=q23(), q24=q24(), q25=q25(), q26=q26(), q27=q27(), q28=q28(), q29=q29(),
                q30=q30(), q31=q31())


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
    h = o["q24"]
    print("Q24 Tangherlini's slice conformally flat: %s; the mode K_2(kZ)/(2k K_1(k ell)): %s, junction %s, zero mode "
          "%s; near zone h00 rho^2/mu = %.4f; far zone off Q23 by %.1e; lowering on T_E at most %.2f mu/min(U, ell)^2 "
          "(%s); at the example at most %.1e; bending %.1e of the rim's margin"
          % (h["slice_ok"], h["mode_ok"], h["jump_ok"], h["zero_mode"], h["near"], h["far"], h["smax"],
             ", ".join("%g/%g %.3f" % (a, b, c) for (a, b), c in sorted(h["table"].items())), h["example"], h["bend"]))
    c = o["q25"]
    print("Q25 small end: mu/U^2 %.3e at the reach, %.3e at the cover, Q24's bound %.2e and %.2e; large end: K - 1 "
          "above %.3e (GT) and %.3e (test form) at the reach, %.3e and %.3e at the cover; each loosens with U: %s"
          % (c["small"]["reach"]["mu_U2"], c["small"]["cover"]["mu_U2"], c["small"]["reach"]["bound"],
             c["small"]["cover"]["bound"], c["large"]["reach"]["k_gt"], c["large"]["reach"]["k_test"],
             c["large"]["cover"]["k_gt"], c["large"]["cover"]["k_test"], c["monotone"]))
    e = o["q26"]
    print("Q26 the life over the floor %.3g in every clock (%s), the floor %.2g s; at the write's start (r_h/R)^2 = "
          "%.2g, R/ell = %.2g; the arrival's width %.1e of the floor" % (e["ratio"], e["ratio_same"], e["floor_s"],
                                                                  e["selfgrav"], e["warp"], e["shift"]))
    g = o["q27"]
    print("Q27 species cap (r_h/l5)^3 = %.3g; there the life %.0f clocks, the floor's 1 + T %.2f (%.0f at the SM's "
          "106.75), ratio %.1f, %.0f stays; the conclusions fail only past %.3g and %.3g species"
          % (g["cap"], g["life_cap"], g["head_cap"], g["head_sm"], g["ratio"], g["stay_ratio"], g["fail_stay"],
             g["fail_floor"]))
    k = o["q28"]
    print("Q28 c4_oneway P1-P6 against the protocols: %s (P18 only beside P4's own reading: %s); P6's conclusion "
          "found: %s; M1s's row on m1_small and c4_oneway: %s" % (k["proto"], k["p18_beside"], k["concl"], k["row_ok"]))
    q = o["q29"]
    print("Q29 ingoing Vaidya, any mu(v): Ricci only R_vv = (3/2) mu'/r^3: %s; R = R_ab R^ab = 0: %s; K = 72 mu^2/r^8: "
          "%s; Planckian at r_c = %.3g m for every profile" % (q["ricci_ok"], q["R0"], q["K_ok"], q["rc"]))
    x = o["q30"]
    print("Q30 G^t_t = -(3/(2 r^3)) d_r mu for every spherical metric: %s; g^ab d r d r = 1 - mu/r^2: %s; a README "
          "off the centre at T_E: %.2f times the centre's scale, at most about %.1e of theta+"
          % (x["ms_ok"], x["gab_rr"], x["near"], x["offc"]))
    y = o["q31"]
    print("Q31 zero error only between orthogonal states: %s; 2^N orthonormal states need dimension 2^N: %s; the floor "
          "moves as (1 + delta)^(-1/3): %s, %.3f to %.3f for delta from -0.2 to 0.2; KLRS at N_f = 6: p0 = %s, p2 = %s"
          % (y["zero_only_orth"], y["rank_ok"], y["exact"], y["band"][0], y["band"][1], y["p0"], y["p2"]))
    print("\nthe inventory: %d readings" % len(INVENTORY))
    for rid, item, text, rows, kind, state in INVENTORY:
        print("  %-8s %-4d %-8s %-58s %s" % (rid, item, kind, text[:58], state))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Q0 354's words and every premise verbatim, each inside its own item", all(o["words"].values()))
    add("Q1-Q4, Q6, Q13, Q16, Q18, Q19, Q22, Q26 exactly one alternative survives each, every exclusion a quoted "
        "premise or a named computation",
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
    h = o["q24"]
    add("Q24 H-HOLE-IN-WARP: Tangherlini's slice conformally flat; the exact linear field from eqs. (11)-(12), "
        "Tangherlini's near the hole and Garriga-Tanaka's far away; theta+ on T_E lowered by at most 5 "
        "mu/min(U, ell)^2, the round tip far out by 2m/ell; at the example 2.5e-10",
        h["slice_ok"] and h["mode_ok"] and h["jump_ok"] and h["zero_mode"] and abs(h["near"] - 1) < 0.01
        and h["far"] < 1e-3 and h["smax"] < 5 and abs(h["table"][(1e3, 1.0)] / (3 * math.pi / 4) - 1) < 0.01
        and h["table"][(1e-3, 1.0)] < 0.75 and "%.1e" % h["example"] == "2.5e-10" and "%.1e" % h["bend"] == "2.2e-06")
    c = o["q25"]
    add("Q25 the cover's 1.05 carries no weight: at the reach itself the small end's hole moves theta+ by at most "
        "2.8e-10 (mu/U^2 = 5.57e-11) and the large end needs only K > 1 + 5.0e-6 (GT) or 1 + 5.6e-6 (test form); "
        "every bound loosens as U grows",
        ["%.3g" % c["small"][x]["mu_U2"] for x in ("reach", "cover")] == ["5.57e-11", "5.05e-11"]
        and "%.2g" % c["small"]["reach"]["bound"] == "2.8e-10" and c["small"]["reach"]["round_ok"]
        and ["%.2g" % c["large"]["reach"][x] for x in ("k_gt", "k_test")] == ["5e-06", "5.6e-06"]
        and "%.2g" % c["large"]["cover"]["k_test"] == "5.4e-06" and c["monotone"])
    e = o["q26"]
    add("Q26 write_small's five mappings: the write ends at the arrival (163, Q2); the clock a unit, the life 1.28e10 "
        "floors in every clock; advanced time M's (334); the start flat to 2.2e-10 and 5.4e-11, the arrival's 4.79 "
        "clocks 7.2e-5 of the floor; the README alone (136 G, 136 (1))",
        "%.3g" % e["ratio"] == "1.28e+10" and e["ratio_same"] and "%.2g" % e["floor_s"] == "2.5e-24"
        and "%.2g" % e["selfgrav"] == "2.2e-10" and "%.2g" % e["warp"] == "5.4e-11" and "%.2g" % e["shift"] == "7.2e-05")
    g = o["q27"]
    add("Q27 H-SPECIES-FINITE replaced by the hole's own semiclassicality: at most 3.85e14 species, where the life is "
        "238 clocks, 54 times the floor and 79 stays; failure only past 3.05e16 and 1.55e17; the floor's 66,980 the "
        "Standard Model's, 4.37 at the cap",
        "%.3g" % g["cap"] == "3.85e+14" and round(g["life_cap"]) == 238 and "%.2f" % g["head_cap"] == "4.37"
        and round(g["ratio"]) == 54 and round(g["stay_ratio"]) == 79 and "%.3g" % g["fail_stay"] == "3.05e+16"
        and "%.3g" % g["fail_floor"] == "1.55e+17" and round(g["head_sm"] - 1) == 66980)
    k = o["q28"]
    add("Q28 c4_oneway's calculator protocols carry no weight on M1s: P1-P6 cite none of P13, P17, P20, and P18 only "
        "beside P4's own reading; P6 concludes M1 from P1-P5",
        k["proto"]["P13"] == k["proto"]["P17"] == k["proto"]["P20"] == 0 and k["proto"]["P18"] == 1
        and k["p18_beside"] and k["concl"] and k["row_ok"])
    q = o["q29"]
    add("Q29 RSHELL: on every radial null-dust profile mu(v) -- the thin shell one of them -- the Ricci tensor is "
        "R_vv = (3/2) mu'/r^3 alone, its invariants zero, and K = 72 mu^2/r^8, Planckian only at r_c = 7.09e-23 m",
        q["ricci_ok"] and q["R0"] and q["K_ok"] and "%.3g" % q["rc"] == "7.09e-23" and q["z2b"])
    x = o["q30"]
    add("Q30 FARs rests on neither RDUST nor RGAS: F5 (a) holds for every spherical README by the Misner-Sharp "
        "identity, d_r mu = (2 kappa/3) r^3 rho >= 0; a README off the centre moves theta+ by about 1e-9; the floor "
        "carries no weight (Q25)", x["ms_ok"] and x["gab_rr"] and "%.2f" % x["near"] == "3.64"
        and "%.0e" % x["offc"] == "2e-09")
    y = o["q31"]
    add("Q31 RGAS: N bits with no tolerance need 2^N orthogonal states at one E (zero error only for orthogonal "
        "states; rank 2^N); the plane's gas within the free gas's states up to its interactions, the floor moving as "
        "(1 + delta)^(-1/3), 1.077 to 0.941 for |delta| <= 0.2; QCD's first correction negative",
        y["zero_only_orth"] and y["rank_ok"] and y["exact"] and ["%.3f" % x for x in y["band"]] == ["1.077", "0.941"]
        and y["p2"] < 0 and y["p0"] == sp.Rational(79, 16))
    add("the inventory: every reading with an item, rows, a kind and a state; the proved ones point at their entry",
        all(len(r) == 6 and r[4] in ("words", "form", "model", "choice", "protocol") for r in INVENTORY)
        and all(("Q" in r[5]) for r in INVENTORY if r[5].startswith("proved here")))
    add("the inventory closed: no reading left to prove -- each proved, M's, bearing on no row's claim, or through "
        "SOURCE (M-SOURCE-LAST)", all(not r[5].startswith("to prove") for r in INVENTORY)
        and all(("Q" in r[5]) or "SOURCE" in r[5] or r[5].startswith("M's") for r in INVENTORY))
    return res


MUTANTS = {"word_wrong_item": "275's words looked for in item 276 (Q0)",
           "unexcluded": "the slab left unexcluded in Q3, two readings surviving (Q1-Q19)",
           "faces_swapped": "the faces taken as the past of I and the future of III (Q5)",
           "time_reflection": "Haggard and Rovelli's time reflection kept beside (-U, -V) (Q8)",
           "mixed_readme": "the README taken as a mixture of two strings (Q15)",
           "face_at_ours": "position 2's energy taken as (G5/G5_2)^1, one r_h (Q16)",
           "e6_borne": "B5c read as resting on e_positive E6, not E7 (Q21)",
           "h55_kept": "Garriga-Tanaka's h_ZZ kept equal to the angular part, not their h55 = 0 (Q23)",
           "flat_green": "the hole's field taken in flat five-dimensional space, no warp (Q24)",
           "cover_needed": "the large end's bound evaluated at U = m, as if the cover were not past the reach (Q25)",
           "clock_weighs": "the life in seconds set against the floor in clocks (Q26)",
           "floor_fixed": "the write's floor held at the Standard Model's species while the life falls (Q27)",
           "calc_premise": "c4_oneway's calculator runs P7-P13 read among M1s's premises (Q28)",
           "mass_in_r": "the Vaidya mass taken to depend on r as well as v (Q29)",
           "ms_4d": "the Misner-Sharp coefficient taken as four-dimensional, 1/2 not 3/2 (Q30)",
           "tolerance": "an error of 1% allowed in telling READMEs apart, against 146's no tolerance (Q31)"}


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
