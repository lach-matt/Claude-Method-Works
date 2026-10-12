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
  P10 (computed; calculator.py, items 290-291; the encoding the board's, 192) C4's question clause by clause (291).
     Each clause of M1 that varies is its own question -- (a) vacuum (b_interior B5), (b)/(e) a complete route (B6),
     (f) P2 positive where relevant (285) -- over the construction's choices: the continuation (inner horizon, quantum
     bounce, classical shell), P2's tension, P2's matter.  The eleven other configurations are known with each clause's
     answer; C4's (the quantum bounce, -sigma/4, the README) enters with it open.  The board's coding: the continuation
     by b_interior's own properties nec and classical (inner horizon 11, quantum bounce 00, classical shell 01), the
     tension by keeps 139 (1) and the matter by the README, 1 where present -- P7's coding, fixed before this run.
     Broadest first, each clause comes back 1 by statistics: (a) and (b)/(e) with order and algebra leaving both open
     and geometry, information and statistics 1; (f) 1 in every closure language; analysis both binaries, (f) at +15.8
     decades for 1 (E7), (a) and (b)/(e) declaring no law.  Logic joins (1, 1, 1) by M1's own conjunction (291 (a)):
     M1 holds.  Extensive both ways, the hierarchy law's containments holding, no key or one-hot (211).  What the answer
     depends on, run under every coding (291 (b)):
       - the continuation's code: not at all -- all 24 two-bit codes give 1, 1, 1 under the board's coding;
       - the orientation of the tension and matter coordinates: over all 96 codings 54 give 1, 1, 1 and 42 are refused
         on all three, exactly where C4's row is not the join of the known rows below it -- information's regrowth,
         a join, cannot reach it.  In the board's coding C4's row is the join of the quantum bounce keeping 139 (1)
         without the README and the quantum bounce carrying the README at +sigma: C4's configuration is those two
         choices combined.  Statistics and geometry, which a coordinate's orientation does not change, give 1 alone on
         every clause in every coding;
       - the statistics order: orders 1 and 2 (2 the cypher's default and register 1174's order on Lambda) give 1, 1,
         1 in all 24 codes; order 3 refuses (f) in 16 and gives 1, 1, 1 in 8; order 4 refuses all three, a new
         configuration's every 4-projection not having been seen.
     In no coding and at no order is any clause 0 or undecided: the alternative to 1 is refusal.  P8 and P9 stand as
     the record of the conjunction's form (290).
  P11 (computed; calculator.py, item 292, reading (c)) P2's tension and matter at three places among M1's clauses,
     under all 96 codings and statistics orders 1-4, beside P10's place (peers: each clause over all three choices).
     Own rank: (a) and (b)/(e) over the continuation alone, (f) over tension and matter alone.  First: (f) over
     tension and matter, then (a) and (b)/(e) over the continuation and (f)'s answer.  Last: (a) and (b)/(e) over the
     continuation, then (f) over tension, matter and their answers.  Peers: decided 1, 1, 1 in 54, 54, 22 and 0
     codings at orders 1-4.  Own rank and first: 1, 1, 1 in every coding at every order (on the own rank statistics
     is silent at orders 3-4, its three coordinates too few, and information answers).  Last: 1, 1, 1 at orders 1-3,
     (f) refused at order 4.  Never 0 or undecided.  So the coding's dependence comes from tension and matter sitting
     beside the continuation in the questions of (a) and (b)/(e).
     [M, item 293: "I did not say to remove them, I said place them elsewhere in the conditions of the question" --
     all three places take tension and matter out of the questions of (a) and (b)/(e).  P11 is kept as the record of
     that reading; it does not answer 292.]
  P12 (computed; calculator.py's protocol with each language's conditions named, items 293-294) Tension and matter
     kept in every clause's question (293), placed three ways (294), beside P10's placement (peers: every closure
     language sees the continuation, tension and matter), all 96 codings, statistics orders 1-4, logic joining:
       - at statistics' rank: order, algebra, geometry and information see the continuation, statistics all three.
         Order 2: 1, 1, 1 in all 96 codings -- (a) and (b)/(e) decided by geometry, (f) by statistics alone.  Order 1:
         (f) undecided in all 96.  Order 3: (f) refused in 64, 1, 1, 1 in 32.  Order 4: all refused;
       - at the broad ranks: the reverse.  Order 2: 1, 1, 1 in all 96 -- (f) decided from order on, (a) and (b)/(e)
         by statistics alone.  Order 1: (a) and (b)/(e) undecided in all 96.  Orders 3 and 4 as at statistics' rank;
       - as the question's given: each clause asked among the configurations with C4's tension and matter, which are
         two -- the inner horizon and the classical shell at -sigma/4 with the README, neither with C4's continuation.
         Refused in 88 of 96 codings at orders 1-2 (at order 2 the other 8 decide (f) alone) and in all 96 at orders
         3-4;
       - peers (P10): 54, 54, 22 and 0 codings deciding 1, 1, 1 at orders 1-4.
     The hierarchy law's containments, checked on each admitted set lifted to all four conditions (294 (c)), hold at
     orders 2-4 in every placement and fail at order 1 in every placement, P10's included: statistics at order 1
     admits more than order, algebra and geometry, which the law puts above it (G.3 and section 6d are statements
     about order 2 and above).  So the order-1 runs here, in P10 and in P9 are outside the law.  No clause is 0 in any
     placement, coding or order.  Information shown tension and matter at statistics' rank brings P10's dependence back
     (the info_sees_all mutant): the refusals of P10 were information's, seeing all three at once.
  P13 (computed; deduced where marked; item 298) The form of C4's question, settled by the cypher.  Why information
     refused (deduced; P10's reach test, 96 of 96): information admits C4's cell with an answer only as the join of
     known cells below it -- its regrowth is the join-closure of the join-irreducibles, and the question's own cell
     carries the open answer, the top.  Among the eleven, C4's continuation is seen (three quantum-bounce
     configurations) and its P2 state is seen (the inner horizon and the classical shell at -sigma/4 with the README),
     but never the two together: C4 is the one configuration combining them.  Whether that combination is a join
     depends on which tension and which matter count as "more" -- with keeps 139 (1) = 1 and README = 1 it is the join
     of the quantum bounce at -sigma/4 without the README and at +sigma with it; flipped, it can fail.  P2's tension read
     relative to ours and its matter across infinite universes (295) supply no such order, so information's verdict on
     them is the coding's, not the configurations'.  Statistics reads co-occurrence, unchanged by relabelling a
     condition's values: the combination's plausibility from its parts (292).  And the continuation (the hole's
     interior) and P2's state (the plane's tension and matter) are independent choices, which is order-2 max-entropy's
     own assumption, no interaction above pairs.  So tension and matter stay in every clause (293), read at
     statistics' rank (292).  Computed: the cypher agrees -- 1, 1, 1 in all 96 codings at the protocol's order, (a) and
     (b)/(e) decided by geometry from the continuation, (f) by statistics -- and logic joins them: M1 holds.  The
     deduction tested where it could fail: with geometry also reading tension and matter, or every language but
     information, the cypher agrees in all 96; with information reading them it refuses in P10's 42.  Information's
     reading alone carried the refusals.
     [Item 299, P17: the order-2 agreement is the finite index's -- with 295's population, where a relative tension can
     outweigh the README, order 2 leaves (f) open, and the cypher agrees at order 3.]
  P14 (computed, exact where marked; estimate where marked) The outgoing flux's back-reaction on P1, owed since P5.
     The flux is a null fluid on the plane, S_ab = rho k_a k_b, traceless (exact).  Israel on P1 (m1_small N4's
     method), K_ab = -(kappa^2/2)(S_ab - S h_ab/3): the flux puts (kappa^2/2) rho into K_tt in the hole's static frame
     against the tension's (kappa^2/6) sigma = 1/ell -- 3 rho/sigma (exact), 0.86 at r = r_h on P5's rho = 0.29 sigma
     (estimate): K r_h = 6.9e-16 against the tension's 8.0e-16, falling as (r_h/r)^2, 0.0086 at 10 r_h.  Warp order:
     P1 stays the equator to a part in 10^15, the flux bending it as much as the tension's own kink does near the hole
     and falling away across clause (c)'s window r_h << r << ell.  The flux's K lies along its null direction, so
     K_ab K^ab vanishes and 0.86 is the static frame's component, the frame P5's rho is defined in; the formed hole's
     ingoing negative flux at the face (c5_oneway U3) is of the same size (estimate).  C4's qualification (5), "C4 is
     classical", stands as the verifier seated it, its bending now sized.
  P15 (computed, exact; deduced where marked) The kink through the faces, owed since P6.  KTN solve the brane condition
     outside the horizon only.  The horizon is non-extremal (kappa = 1/r_h at flat order; at warp order
     Schwarzschild-AdS5's root is simple, f' > 0 there), and U V = -e^{2 kappa r*} = -e^{2 r/r_h} (r - r_h)/(r + r_h)
     has d(UV)/dr = -e^2/(2 r_h), not zero, at r_h: r is an analytic function of U V across U = 0 and V = 0.  Deduced:
     a static brane profile psi(r) analytic at the horizon is an analytic function of U V; the brane condition's
     coefficients are analytic in (U, V), so psi(r(UV)) satisfies it wherever it did outside and continues through our
     black-hole face and position 2's white-hole face into both interiors (the identity theorem), until r reaches the
     quantum region (273).  The bounce's map (U, V) -> (-U, -V) keeps U V, so position 2's side carries the same
     profile, position 2 reading its own side (b_bounce Q1).  Conditional on KTN's exterior profile being analytic at
     the horizon; their solution is numerical and disputed (item 261), as the C1 and C4 verifiers recorded.
  P16 (deduced) C4's case, by the record.  The form of its question settled by the cypher (P13, under 291-298): clause
     by clause, tension and matter in every clause and read at statistics' rank, 1, 1, 1 under every coding at the
     protocol's order, logic joining -- M1 holds; P8-P12 the record of the forms before it.  The items 297 listed against
     readiness: the form (P13); the kink through the faces derived (P15, conditional on analyticity at the horizon);
     the flux's back-reaction sized (P14, warp order); C4 classical carried as the verifier's qualification (5), with
     its size.  So C4 is ready for M's finalization (249) and one verifier.
     [Item 299, P17: the order at which the cypher agrees is 3, with the population of tensions and matters entered and
     the continuation one condition -- not the protocol's 2, at which (f) is open once the population is entered.]
     [Item 300, P18: with survivability built in the cypher agrees at orders 2 and 3, every lawful order the question
     has.]
  P17 (computed, exact where marked; deduced where marked; item 299) The higher orders, solved.
     The top order (deduced; checked exactly, 36 of 36): on d coordinates statistics' highest order is d - 1, and a
     cell is admitted there iff each of its (d-1)-projections is seen.  Leaving out the answer gives C4's conditions,
     seen in the question's own cell; leaving out condition i asks for a known configuration that differs from C4 in i
     alone and carries the answer.  So at the top order C4's answer a is admitted iff every condition, changed alone,
     can keep a, and a clause that hinges at C4 on a binary coordinate is refused there -- its one change flips the
     answer.
     Less information.  P12's order 4 existed because the continuation, one condition with three values, was entered
     as two coordinates, and changing one bit reaches one other code: one continuation, or none.  For (a) both of the
     quantum bounce's one-bit neighbours would have to be vacuum, for (b)/(e) both complete -- the shell one bit from it
     in both bits at once -- so order 4 refuses them in every code (computed: 24 of 24; (f) in the 16 where the unused
     code is a neighbour).  Entered as one condition, the continuation changes to either other continuation, d = 4,
     and the top order is 3; order 4 is silent ("needs more than 4 coordinates", reg 1175).  The fourth order was the
     code's.
     More information.  With infinite relative tensions and matter (295), (f)'s law, f = [tau + rho/sigma > 0],
     realizes over the classes t (139 (1)'s tau = -1/4, or any other) and m (the README's rho = R sigma/4, R = 5.9e15,
     or any other matter) (computed, exact; a witness inside each class for each answer): (-1/4, the README) 1 only;
     every other class both -- the quantum bounce at -sigma/4 holds other matter above sigma/4 (1) and below it (0), and
     the README meets relative tensions below -R/4 = -1.5e15 (0).  The finite index has none of these, which is why
     order 3 refused (f): it asked for the quantum bounce at -sigma/4 holding (f) without the README.
     Solved, the continuation one condition and the population entered: at order 3, (a), (b)/(e) and (f) each 1 under
     all 6 orderings of the continuation's values -- and, as two bits, all 24 codes -- and logic joins 1: M1 holds.  The
     hierarchy law's containments hold at orders 2-4; extensive.  Order 2 leaves (f) open: its law is the sign of
     tension plus matter, a three-way interaction of (t, m, f), which pairwise marginals cannot hold once both range
     freely.  So order 3 is at once (f)'s own order and the question's top order, and there the cypher agrees.  The
     continuation as one condition with three values is the board's reading of 286's "binary form" -- the question and
     its answer binary, a condition one coordinate -- named as such (192).
     [M, item 300: survivability is built in -- the (the README, f = 0) cells at relative tensions below -R/4 entered
     the object unadapted.  P18 corrects them, and order 2 agrees as well.]
  P18 (computed, exact where marked; deduced where marked; item 300) Survivability built in.  P17 entered the README as
     position 1's object carried unchanged into every position 2, so a relative tension below -R/4 outweighed it and
     (the README, f = 0) was realized -- the error M named.  The object is built from the bulk at position 2 as an exact
     copy under that position's laws (240, 285), and its survival there is built in (300).  Deduced (the board's
     reading 300 (b)): built under a position's laws, its density at the face scales with that position's own tension,
     rho = (R/4)|tau| sigma, so where it lands P2's total is tau + (R/4)|tau| -- positive for tau > 0 and, R being
     above 4, for tau < 0 (computed, exact); at tau = 0 P2 carries no tension and the total is the object's own
     density, positive.  So the class (any other relative tension, the object) realizes 1 only.  With it, the
     continuation one condition and the population of other matter (295), the cypher agrees at orders 2 and 3 -- 1, 1,
     1 under all 6 orderings, and as two bits under all 24 codes -- and logic joins 1: M1 holds at every order the law
     admits (order 1 is outside it, P12).  P13's order-2 agreement stands again, the population entered.  The refusals
     that came from position 2's conditions are admitted.  Those left are the two-bit code's at order 4 -- (a) and
     (b)/(e) in every code, (f) in the 16 where the unused code neighbours the quantum bounce -- each a one-bit change
     reaching a continuation with another answer, or a code no continuation has: the route and the bulk, not the
     object.  Survivability is a condition on the object in position 2 (240 (c)) and does not reach them; with the
     continuation one condition there is no order 4 (P17).
     Contrast (computed): entered instead as a varying condition -- the object so built, or not so equipped (241's
     means of mitigation) -- survivability gives the question a fourth condition and a top order 4, where the cypher
     agrees (1, 1, 1, all 6 orderings) as it does at order 3; but order 2 reopens (f), whose law turns three-way in (the
     object, survivability, the answer).  Built in, survivability is not a variable, and every lawful order from 2
     agrees.
     [M, item 302: the order-4 refusals are not the code's artefacts -- a one-bit change landing on a continuation with
     another answer is a binary communication, and a code no continuation holds means more continuation clauses.  P20.]
  P19 (computed, exact; item 301) tau, calculated before the verifier (tau_share.py).  The coincidence fixes only the
     summed stress at the one junction (275), and our side carries ours alone (chi = 0, 276), so position 2 receives
     tau = 1 + lambda_2/lambda_1 = 3/4 of our tension -- exactly the summed tension, lambda_RS -- and its side carries
     sigma/2 = 2/3 lambda_RS, positive.  P4's crossing share is positive at tau = 3/4 (tau_share T5; it was for every
     tau in [0, 1]).  With matter on position 2's plane, what it receives is the summed stress itself (T3).
  P20 (computed; the board's reading where marked; item 302) More continuation clauses; binary communication.  The
     continuation's two bits are its own clauses, b_interior's binary properties that separate the interiors: NEC
     holding (no bounce) and README-only (nothing else carried inside).  The three interiors that open into position 2
     hold three of the four codes -- the inner horizon (1, 0), the quantum bounce (0, 1), the classical shell (0, 0) --
     and the code none held, (1, 1), is b_interior's fourth interior: no inner horizon and no bounce, the classical
     singular one (B1), whose route ends inside (vacuum 1, complete 0; nothing exits it, so it carries no reverse
     passage; (f) read from P2's state, as for the inner horizon).  Entered, with the population and survivability
     built in (P17-P18), orders 2 and 3 give 1, 1, 1.  At order 4 (f) is admitted -- its refusal was the missing
     continuation -- and (a) and (b)/(e) are refused, each carried by one continuation clause: (b)/(e) is exactly "a
     bounce" (NEC failing), so the quantum bounce's NEC neighbour, the singular interior, is incomplete; (a) at the
     quantum bounce follows README-only, its neighbour there the shell, which carries matter in the bulk.  Each is a
     binary communication (302): the bit's change carries the answer with it.  Under all 24 codes: order 3 gives 1, 1,
     1 in every one; order 2 in 22 (the other 2 put the quantum bounce and the shell on a diagonal, where no single
     clause separates the complete interiors); order 4 refuses (b)/(e) in all and (a) in 16.
     The board's reading of 302 (b): at the top order a continuation bit is a channel -- its neighbour's answer, the
     same or the other, is consistent with C4's so long as the neighbour exists -- while position 2's conditions
     constrain as before.  Under it the top order gives 1, 1, 1 in every code.  Control: each of the four interiors
     entered as the question returns its own answers (the singular interior and the inner horizon 1, 0, 1, the shell
     0, 1, 1, the quantum bounce 1, 1, 1), so the reading decides from what the cells hold, not toward 1.  The operator's
     own order-4 verdict stays beside it, unrepaired.
     [Item 304 (the C1 verifier's qualification (4), checked here by the critic): on 211's audit of the known cells,
     (b)/(e) under the two clauses is the complement of NEC in every interior -- index_audit flags (c1, be), b_interior
     B6's Penrose flag -- so (b)/(e)'s verdict here is that row read back, void as evidence; under P17's one-condition
     coding nothing is flagged.  And the 1, 1, 1 at the other (tension, matter) classes is the quantum bounce's own row:
     the form agreeing, not a further computation.]
  P21 (deduced; item 303) The residue, from the record.
     (1) C1 first: C4's P2 and P3 rest on c1_oneway K1-K4, and C1 one-way is not verified -- its verifier was stopped
         (298's audit) -- and its question is owed through the calculator; 282 (b) puts C1 before C4.
     (2) Conditional: the kink through the faces, on KTN's profile being analytic at the horizon (P15); tau = 3/4
         where the sheets coincide, not at the corridor, and no single number with matter on position 2's plane (P19).
     (3) Estimates: the outgoing flux, 0.29 sigma at r_h (P5); its bending, 0.86 of the tension's, a static-frame
         junction component, not the plane's solved shape (P14).
     (4) The board's readings, M's to overrule, on which the cypher's agreement rests: tension and matter read at
         statistics' rank (P13); the continuation as one condition (P17) or as its own two clauses (P20); the object's
         density scaling with position 2's own tension (P18); the channel reading of a binary communication (P20).
         The operator alone still refuses (a) and (b)/(e) at order 4 under the two clauses, and 2 of the 24 codes
         leave (b)/(e) open at order 2 (P20).
     (5) Not computed: the quantum region's duration (b_bounce Q3 is the two-way object's, 277); KTN's profile; the
         plane's shape under the flux.
     (6) Standing qualification: C4 is classical -- near the hole the plane's quantum load is of the tension's order
         (P5, P14).
     (7) Nothing in P1-P20 is verified by a separate session.
     [Item 304: (1) is closed -- C1 one-way is CONFIRMED with qualifications.  Added by the C1 verifier's (4): under
     P20's two clauses (b)/(e) is the complement of NEC in every known cell (211), void as evidence there; and in every
     form the quantum bounce's clauses at the other (tension, matter) classes are its own row read back.  And (B) / (a)
     is read as no classical stress on the route; read as Ricci-flat on the whole route, the bounce's is 0.]

What this does not show.
  - KTN's profile itself: P15 continues it through the faces, conditional on its analyticity at the horizon.
  - The plane's solved shape under the flux: P14 is the junction's static-frame component.
  - The quantum region's duration (b_bounce Q3 is the two-way object's; item 277), as c5_oneway.

Imports m1_small.py, c1_oneway.py, e_positive.py, hold_small.py, p2_gravity.py, b_interior.py, index_audit.py,
calculator.py, tau_share.py, research/warp-drive/hlaw.py and tools/cypher.py by path.  Stdlib + sympy.
python3 c4_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
from collections import Counter
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
    res = {n.split()[0]: ok for n, ok in C1.checks(C1.compute(light=True))}
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


_P10 = {}
CONTS = [(1, "none"), (0, "quantum"), (0, "shell")]          # the inner horizon, the quantum bounce, the classical shell
NAMED = {(1, "none"): (1, 1), (0, "quantum"): (0, 0), (0, "shell"): (0, 1)}   # b_interior's nec, classical
CLAUSES = (("a", "vacuum (b_interior B5)", ["b_interior B5", "273"]),
           ("be", "a complete route (b_interior B6)", ["b_interior B6", "273", "c1_oneway K3"]),
           ("f", "P2 positive where relevant (285)", ["139 (1)", "268", "284", "285", "e_positive E7"]))


def clauses():
    """P10 (item 291): C4's question clause by clause, the construction's choices as attributes, logic joining"""
    key = tuple(sorted(k for k in MUT if k in ("readme_thin", "no_readme_coordinate", "shell_continuation")))
    if key in _P10:
        return _P10[key]
    CA = _load("calculator.py", "c4o_calc")
    IA = _load("index_audit.py", "c4o_ia2")
    BI = _load("b_interior.py", "c4o_bi4")
    EP = _load("e_positive.py", "c4o_ep3")
    ratio = 0.5 if MUT.get("readme_thin") else EP.example()["R_rh"] ** 3
    cells = {k: v for k, v in BI.cells().items() if k[2] == "pos2"}
    cfg = {}
    for (inner, bounce, _), p in cells.items():
        for t, m in itertools.product(("-sigma/4", "+sigma"), (0, 1)):
            cfg[((inner, bounce), t, m)] = dict(a=int(bounce != "shell"), be=p["complete"], f=int(m == 1 or t == "+sigma"))
    q = ((0, "shell") if MUT.get("shell_continuation") else (0, "quantum"), "-sigma/4", 1)
    attrs_names = ["c1", "c2", "t"] if MUT.get("no_readme_coordinate") else ["c1", "c2", "t", "m"]

    def run(cm, tf, mf, full=False, k=2):
        def enc(k):
            row = cm[k[0]] + (int(k[1] == "-sigma/4") ^ tf, k[2] ^ mf)
            return row[:len(attrs_names)]
        at = enc(q)
        out = {}
        for cl, desc, cites in CLAUSES:
            known = [enc(k) + (r[cl],) for k, r in cfg.items() if k != q]
            an = {"witness": "e_positive E7: (R/r_h)^3", "magnitude": ratio, "threshold": 1.0} if cl == "f" else None
            r = CA.ask(attrs_names + [cl], known, at, analysis=an, citations=cites, k=k)
            aud = IA.audit_index(attrs_names + [cl], known + [at + (CA.U,)])
            r["void"] = bool(aud["keys"] or aud["onehot"])
            if full:
                ctl = CA.controls(attrs_names + [cl], known, at)
                r["extensive"], r["lawful"] = ctl["extensive"], ctl["lawful"]
            out[cl] = r
        ans = [out[cl]["answer"] for cl, _, _ in CLAUSES]
        join = 1 if all(a == 1 for a in ans) else 0 if 0 in ans and "refused" not in ans else "not binary"
        rows = [enc(k) for k in cfg if k != q]
        below = [x for x in rows if all(a <= b for a, b in zip(x, at))]
        reach = bool(below) and tuple(map(max, *below)) == at if len(below) > 1 else below == [at]
        return dict(out=out, ans=tuple(ans), join=join, reach=reach)

    named = run(NAMED, 0, 0, full=True)
    sweep = {}
    for code in itertools.permutations([(0, 0), (0, 1), (1, 0), (1, 1)], 3):
        for tf, mf in itertools.product((0, 1), repeat=2):
            sweep[(code, tf, mf)] = run(dict(zip(CONTS, code)), tf, mf)
    orders = {k: [run(dict(zip(CONTS, code)), 0, 0, k=k)["ans"]
                  for code in itertools.permutations([(0, 0), (0, 1), (1, 0), (1, 1)], 3)] for k in (1, 3, 4)}
    orders[2] = [v["ans"] for (cd, tf, mf), v in sweep.items() if (tf, mf) == (0, 0)]
    _P10[key] = dict(named=named, sweep=sweep, ratio=ratio, orders=orders)
    return _P10[key]


_P11 = {}
PLACES = ("peers", "own", "first", "last")


def ranks():
    """P11 (item 292): the cypher with P2's tension and matter at each place among M1's clauses"""
    key = tuple(sorted(k for k in MUT if k in ("tm_with_continuation", "c4_without_readme")))
    if key in _P11:
        return _P11[key]
    CA = _load("calculator.py", "c4o_calc")
    BI = _load("b_interior.py", "c4o_bi5")
    cells = {k: v for k, v in BI.cells().items() if k[2] == "pos2"}
    cfg = {}
    for (inner, bounce, _), p in cells.items():
        for t, m in itertools.product(("-sigma/4", "+sigma"), (0, 1)):
            cfg[((inner, bounce), t, m)] = dict(a=int(bounce != "shell"), be=p["complete"], f=int(m == 1 or t == "+sigma"))
    q = ((0, "quantum"), "-sigma/4", 1)
    others = [x for x in cfg if x != q]
    q_read = ((0, "quantum"), "-sigma/4", 0) if MUT.get("c4_without_readme") else q   # the mutant drops the README
    out = {pl: {} for pl in PLACES}
    by = {pl: {} for pl in PLACES}
    for code in itertools.permutations([(0, 0), (0, 1), (1, 0), (1, 1)], 3):
        cm = dict(zip(CONTS, code))
        for tf, mf in itertools.product((0, 1), repeat=2):
            C = lambda x: cm[x[0]]
            TM = lambda x: (int(x[1] == "-sigma/4") ^ tf, x[2] ^ mf)
            for k in (1, 2, 3, 4):
                seen = {pl: [] for pl in PLACES}

                def one(pl, names, rows, at):
                    r = CA.ask(names, rows, at, k=k)
                    seen[pl].append(r["by"])
                    return r["answer"]

                def joined(ans):
                    return 1 if all(a == 1 for a in ans) else 0 if 0 in ans and "refused" not in ans else "not binary"

                # peers: each clause over all three choices, as P10
                pe = tuple(one("peers", ["c1", "c2", "t", "m", cl], [C(x) + TM(x) + (cfg[x][cl],) for x in others],
                               C(q_read) + TM(q_read)) for cl in ("a", "be", "f"))
                # own: each clause over the choices it depends on -- the continuation for (a) and (b)/(e), P2's
                # tension and matter for (f); the mutant puts tension and matter back beside the continuation
                cont = (lambda x: C(x) + TM(x)) if MUT.get("tm_with_continuation") else C
                cn = ["c1", "c2", "t", "m"] if MUT.get("tm_with_continuation") else ["c1", "c2"]
                a = one("own", cn + ["a"], [cont(x) + (cfg[x]["a"],) for x in others], cont(q_read))
                b = one("own", cn + ["be"], [cont(x) + (cfg[x]["be"],) for x in others], cont(q_read))
                f = one("own", ["t", "m", "f"], [TM(x) + (cfg[x]["f"],) for x in others], TM(q_read))
                ow = (a, b, f)
                # first: (f) over tension and matter, then (a) and (b)/(e) over the continuation and (f)'s answer
                if f in (0, 1):
                    fi = (one("first", ["c1", "c2", "fv", "a"], [C(x) + (cfg[x]["f"], cfg[x]["a"]) for x in others],
                              C(q_read) + (f,)),
                          one("first", ["c1", "c2", "fv", "be"], [C(x) + (cfg[x]["f"], cfg[x]["be"]) for x in others],
                              C(q_read) + (f,)), f)
                else:
                    fi = ("after (f)", "after (f)", f)
                # last: (a) and (b)/(e) over the continuation, then (f) over tension, matter and their answers
                if a in (0, 1) and b in (0, 1):
                    la = (a, b, one("last", ["t", "m", "av", "bv", "f"],
                                    [TM(x) + (cfg[x]["a"], cfg[x]["be"], cfg[x]["f"]) for x in others],
                                    TM(q_read) + (a, b)))
                else:
                    la = (a, b, "after (a), (b)/(e)")
                for pl, ans in (("peers", pe), ("own", ow), ("first", fi), ("last", la)):
                    out[pl][(code, tf, mf, k)] = (ans, joined(ans))
                    by[pl][(code, tf, mf, k)] = tuple(seen[pl])
    _P11[key] = dict(out=out, by=by)
    return _P11[key]


_P12 = {}
SCEN = ("peers", "statistics' rank", "broad ranks", "given")


def _staged(CA, HL, names, known, attrs, views, k, analysis=None, citations=()):
    """calculator.ask's protocol -- roster 1173's order, narrowing, analysis both binaries, documentary citations,
    logic taking the last closure language -- with each closure language seeing the conditions views[lang] names
    (indices into attrs) and the answer; the law's containments checked on the admitted sets lifted to all
    conditions, a language admitting every value of a condition it does not see"""
    cells = list(known) + [tuple(attrs) + (CA.U,)]
    open_, last, trace, lifted, mags = {0, 1}, None, [], {}, {0: None, 1: None}
    for lang in CA.ORDER:
        if lang == "documentary":
            trace.append((lang, "citations", list(citations)))
            continue
        if lang == "analysis":
            if analysis is not None:
                L = math.log10(analysis["magnitude"] / analysis["threshold"])
                mags = {1: L, 0: -L}
            trace.append((lang, "both", "open after it: %s" % sorted(open_)))
            continue
        v = views[lang]
        cl = CA.closure([names[i] for i in v] + [names[-1]], [tuple(c[i] for i in v) + (c[-1],) for c in cells], lang, k)
        if cl is None:
            trace.append((lang, "silent", ""))
            lifted[lang] = None
            continue
        said = {a for a in (0, 1) if tuple(attrs[i] for i in v) + (a,) in cl}
        open_ &= said
        trace.append((lang, sorted(open_), "of %s admitted" % sorted(said)))
        last, lifted[lang] = lang, (v, cl)
    ans = {(0,): 0, (1,): 1, (0, 1): "both", (): "refused"}[tuple(sorted(open_))]
    vals = [sorted({c[i] for c in cells}) for i in range(len(attrs) + 1)]
    amb = list(itertools.product(*vals))
    up = {lang: None if lifted[lang] is None else
          {x for x in amb if tuple(x[i] for i in lifted[lang][0]) + (x[-1],) in lifted[lang][1]} for lang in lifted}
    lawful = all(up[a] is None or up[b] is None or up[a] <= up[b] for a, b in HL.LAWFUL)
    return dict(answer=ans, by=last, trace=trace, magnitudes=mags, lawful=lawful)


def placements():
    """P12 (items 293-294): tension and matter kept in every clause's question, placed at statistics' rank, as the
    question's given, or at the broad ranks; beside P10's placement, every coding, statistics orders 1-4"""
    key = tuple(sorted(k for k in MUT if k in ("info_sees_all", "given_by_tension")))
    if key in _P12:
        return _P12[key]
    CA = _load("calculator.py", "c4o_calc")
    HL = _load_path(os.path.join(os.path.dirname(D68), "hlaw.py"), "c4o_hl")
    BI = _load("b_interior.py", "c4o_bi6")
    EP = _load("e_positive.py", "c4o_ep4")
    ratio = EP.example()["R_rh"] ** 3
    cells = {k: v for k, v in BI.cells().items() if k[2] == "pos2"}
    cfg = {}
    for (inner, bounce, _), p in cells.items():
        for t, m in itertools.product(("-sigma/4", "+sigma"), (0, 1)):
            cfg[((inner, bounce), t, m)] = dict(a=int(bounce != "shell"), be=p["complete"], f=int(m == 1 or t == "+sigma"))
    q = ((0, "quantum"), "-sigma/4", 1)
    others = [x for x in cfg if x != q]
    broad = ("order", "algebra", "geometry", "information")
    every = (0, 1, 2, 3)                                    # c1, c2 (the continuation), t, m
    views = {"peers": {L: every for L in broad + ("statistics",)},
             "statistics' rank": dict({L: (0, 1) for L in broad}, statistics=every),
             "broad ranks": dict({L: (2, 3) for L in broad}, statistics=every)}
    if MUT.get("info_sees_all"):
        views["statistics' rank"]["information"] = every   # the mutant lets information see tension and matter
    views["given"] = views["peers"]
    out = {s: {} for s in SCEN}
    for code in itertools.permutations([(0, 0), (0, 1), (1, 0), (1, 1)], 3):
        cm = dict(zip(CONTS, code))
        for tf, mf in itertools.product((0, 1), repeat=2):
            enc = lambda x: cm[x[0]] + (int(x[1] == "-sigma/4") ^ tf, x[2] ^ mf)
            at = enc(q)
            fixed = (lambda x: enc(x)[2] == at[2]) if MUT.get("given_by_tension") else (lambda x: enc(x)[2:] == at[2:])
            for k in (1, 2, 3, 4):
                for s in SCEN:
                    rows = [x for x in others if fixed(x)] if s == "given" else others
                    res = []
                    for cl, desc, cites in CLAUSES:
                        an = {"witness": "e_positive E7: (R/r_h)^3", "magnitude": ratio, "threshold": 1.0} \
                            if cl == "f" else None
                        res.append(_staged(CA, HL, ["c1", "c2", "t", "m", cl], [enc(x) + (cfg[x][cl],) for x in rows],
                                           at, views[s], k, analysis=an, citations=cites))
                    ans = tuple(r["answer"] for r in res)
                    join = 1 if all(a == 1 for a in ans) else 0 if 0 in ans and "refused" not in ans else "not binary"
                    out[s][(code, tf, mf, k)] = dict(ans=ans, join=join, lawful=all(r["lawful"] for r in res),
                                                     by=tuple(r["by"] for r in res),
                                                     known=len(rows), mag=res[2]["magnitudes"][1])
    _P12[key] = out
    return out


_P13 = {}


def form():
    """P13 (item 298): which language's reading of tension and matter carries the refusals -- the form of C4's
    question settled by the cypher's agreement, at the protocol's order (2)"""
    key = tuple(sorted(k for k in MUT if k in ("info_reads_order",)))
    if key in _P13:
        return _P13[key]
    CA = _load("calculator.py", "c4o_calc")
    HL = _load_path(os.path.join(os.path.dirname(D68), "hlaw.py"), "c4o_hl")
    BI = _load("b_interior.py", "c4o_bi7")
    cells = {k: v for k, v in BI.cells().items() if k[2] == "pos2"}
    cfg = {}
    for (inner, bounce, _), p in cells.items():
        for t, m in itertools.product(("-sigma/4", "+sigma"), (0, 1)):
            cfg[((inner, bounce), t, m)] = dict(a=int(bounce != "shell"), be=p["complete"], f=int(m == 1 or t == "+sigma"))
    q = ((0, "quantum"), "-sigma/4", 1)
    others = [x for x in cfg if x != q]
    every, cont = (0, 1, 2, 3), (0, 1)
    tests = {"form": dict(order=cont, algebra=cont, geometry=cont, information=cont, statistics=every),
             "geometry too": dict(order=cont, algebra=cont, geometry=every, information=cont, statistics=every),
             "all but information": dict(order=every, algebra=every, geometry=every, information=cont,
                                         statistics=every),
             "information too": dict(order=cont, algebra=cont, geometry=cont, information=every, statistics=every)}
    if MUT.get("info_reads_order"):
        tests["form"]["information"] = every               # the mutant lets information read tension and matter
    out = {t: Counter() for t in tests}
    seen = {"cont": True, "pstate": True, "combo": False}
    for code in itertools.permutations([(0, 0), (0, 1), (1, 0), (1, 1)], 3):
        cm = dict(zip(CONTS, code))
        for tf, mf in itertools.product((0, 1), repeat=2):
            enc = lambda x: cm[x[0]] + (int(x[1] == "-sigma/4") ^ tf, x[2] ^ mf)
            for t, v in tests.items():
                out[t][tuple(_staged(CA, HL, ["c1", "c2", "t", "m", cl], [enc(x) + (cfg[x][cl],) for x in others],
                                     enc(q), v, 2)["answer"] for cl, _, _ in CLAUSES)] += 1
    # what is seen of C4: its continuation alone, its P2 state alone, and the combination
    seen["cont"] = any(x[0] == q[0] for x in others)
    seen["pstate"] = any(x[1:] == q[1:] for x in others)
    seen["combo"] = any(x == q for x in others)
    _P13[key] = dict(out=out, seen=seen)
    return _P13[key]


def flux_bend():
    """P14: the outgoing flux's bending of P1 at r = r_h against the tension's, by Israel (m1_small N4's method)"""
    s = state()
    PG = _load("p2_gravity.py", "c4o_pg2")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rh = (2 * 2742570311524972 * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    k2, sig, rho = sp.symbols("kappa2 sigma rho", positive=True)
    h = sp.diag(-1, 1, 1, 1)
    kv = sp.Matrix([1, 1, 0, 0])                            # outgoing radial null, static orthonormal frame
    S_flux = rho * kv * kv.T                                 # S_ab = rho k_a k_b (lowered: k_t = -1 -> same outer product)
    S_flux[0, 1] = S_flux[1, 0] = -rho
    trace = sum(h[i, i] * S_flux[i, i] for i in range(4))
    fac = sp.Rational(1, 2) if not MUT.get("flux_as_tension") else sp.Rational(1, 6)
    K_flux_tt = sp.simplify(fac * k2 * (S_flux[0, 0] - trace * h[0, 0] / 3))
    K_tens = sp.simplify(sp.Rational(1, 2) * k2 * ((-sig * h)[1, 1] - (-4 * sig) * h[1, 1] / 3))
    ratio_sym = sp.simplify(K_flux_tt / K_tens)              # 3 rho / sigma
    ratio = float(ratio_sym.subs({rho: s["ratio"], sig: 1}))
    return dict(traceless=trace == 0, ratio_sym=ratio_sym, ratio=ratio, K_flux=ratio * rh / PG.ELL_MAX,
                K_tension=rh / PG.ELL_MAX, at10=ratio / 100)


def faces():
    """P15: r as a function of U V across a non-extremal horizon; the bounce's map keeps U V"""
    r, rh, ell, U, V = sp.symbols("r r_h ell U V", positive=True)
    f = 1 - rh ** 2 / r ** 2
    if MUT.get("extremal"):
        f = (1 - rh ** 2 / r ** 2) ** 2                    # the mutant: a double root, kappa = 0
    kappa = sp.simplify(sp.diff(f, r).subs(r, rh) / 2)
    rstar = r + rh / 2 * sp.log((r - rh) / (r + rh))         # int dr / f for 1 - r_h^2/r^2
    ok_rstar = sp.simplify(sp.diff(rstar, r) - 1 / (1 - rh ** 2 / r ** 2)) == 0
    if kappa == 0:
        return dict(kappa=kappa, dUV=0, analytic=False, ok_rstar=ok_rstar, sads_simple=False, bounce_keeps=True)
    UV = -sp.exp(2 * kappa * r) * (r - rh) / (r + rh)        # -e^{2 kappa r*}
    ok_uv = sp.simplify(UV + sp.exp(2 * kappa * rstar)) == 0
    dUV = sp.simplify(sp.diff(UV, r).subs(r, rh))
    fa = 1 - rh ** 2 / r ** 2 + r ** 2 / ell ** 2            # warp order: Schwarzschild-AdS5
    return dict(kappa=kappa, dUV=dUV, analytic=bool(dUV != 0) and ok_uv, ok_rstar=ok_rstar,
                sads_simple=bool(sp.diff(fa, r).is_positive), bounce_keeps=sp.expand((-U) * (-V) - U * V) == 0)


_P17 = {}
NAMES3 = ["inner", "quantum", "shell"]


def population(R):
    """P17: the support of (f)'s law, f = [tau + rho/sigma > 0], over the classes t (1: 139 (1)'s tau = -1/4, 0: any
    other relative tension) and m (1: the README, rho = R sigma/4, 0: any other matter, rho >= 0) -- the answers each
    class realizes, exact, by witnesses inside the class; with infinite relative tensions and matter (295)"""
    tau, rho = sp.symbols("tau rho", real=True)
    law = lambda T, P: bool(T + P > 0)
    rR = sp.Rational(1, 4) * R
    lo = -R if not MUT.get("bounded_tension") else sp.Integer(-1)   # the mutant keeps tension within [-1, 1]
    wit = {(1, 1): [(-sp.Rational(1, 4), rR)],
           (1, 0): [(-sp.Rational(1, 4), 0), (-sp.Rational(1, 4), 1)],
           (0, 1): [(0, rR), (lo, rR)],
           (0, 0): [(0, 0), (1, 0)]}
    out, inside = {}, True
    for (t, m), ws in wit.items():
        for T, P in ws:
            inside &= (T == -sp.Rational(1, 4)) == bool(t) and (P == rR) == bool(m) and P >= 0
        out[(t, m)] = {int(law(T, P)) for T, P in ws}
    return out, inside


def relative(R):
    """P18 (item 300): the object built under each position 2's laws -- its density at the face scales with that
    position's own tension, rho = (R/4) |tau| sigma, so where it lands P2's total is tau + (R/4)|tau| (in sigma)"""
    tau = sp.Symbol("tau", real=True)
    scale = (lambda T: R / 4 * abs(T)) if not MUT.get("absolute_readme") else (lambda T: R / 4)
    tot = tau + R / 4 * sp.Abs(tau)
    pos_side = sp.simplify(tot.subs(tau, sp.Symbol("u", positive=True))).is_positive
    neg_side = sp.simplify(tot.subs(tau, -sp.Symbol("u", positive=True))).is_positive
    # the class (any other relative tension, the object): every tau realizes 1; and 0 only if some tau fails
    witnesses = [sp.Integer(1), -sp.Rational(1, 4) * 3, -R, -R ** 2, sp.Integer(10) ** 30]
    realized = {int(bool(T + scale(T) > 0)) for T in witnesses}
    # tau = 0: P2 carries no tension and its total is the object's own density, which is matter -- positive
    rho0 = sp.Symbol("rho_obj", positive=True)
    zero = bool((0 + rho0).is_positive)
    realized |= {int(zero)}
    return dict(pos_side=bool(pos_side), neg_side=bool(neg_side), zero=zero, realized=realized)


def higher(survive=False):
    """P17 (item 299): the higher statistics orders solved -- the one-flip rule at the top order, the population of
    tensions and matters (more information), the continuation as one condition (less information).  P18 (item 300):
    survive=True enters the object built under each position 2's laws, its survival there built in"""
    key = tuple(sorted(k for k in MUT if k in ("bounded_tension", "finite_grid", "two_bits", "absolute_readme"))) + (
        survive,)
    if key in _P17:
        return _P17[key]
    CA = _load("calculator.py", "c4o_calc")
    HL = _load_path(os.path.join(os.path.dirname(D68), "hlaw.py"), "c4o_hl")
    EP = _load("e_positive.py", "c4o_ep5")
    R = sp.Float(EP.example()["R_rh"] ** 3, 20)
    F, inside = population(R)
    if survive:
        rel = relative(R)
        F = dict(F)
        F[(0, 1)] = rel["realized"]                       # the object at any other relative tension
    if MUT.get("finite_grid"):
        F = {(t, m): {int(m == 1 or t == 0)} for t in (0, 1) for m in (0, 1)}   # the index's four cells only
    A = {"inner": 1, "quantum": 1, "shell": 0}
    BE = {"inner": 0, "quantum": 1, "shell": 1}

    def known(cl, enc):
        rows = []
        for k in NAMES3:
            for t, m in itertools.product((0, 1), repeat=2):
                if (k, t, m) == ("quantum", 1, 1):
                    continue
                for v in ({A[k]} if cl == "a" else {BE[k]} if cl == "be" else F[(t, m)]):
                    rows.append(enc(k) + (t, m, v))
        return rows

    one, bits = {}, {}
    flip_ok, flip_n, lawful, extensive = True, 0, {}, True
    for k in (1, 2, 3, 4):
        res, law_k = Counter(), True
        for perm in itertools.permutations(range(3)):
            kmap = dict(zip(NAMES3, perm))
            if MUT.get("two_bits"):
                cm = dict(zip(NAMES3, [(1, 1), (0, 0), (0, 1)]))
                enc, names = (lambda kk: cm[kk]), ["c1", "c2", "t", "m"]
                views = dict(order=(0, 1), algebra=(0, 1), geometry=(0, 1), information=(0, 1), statistics=(0, 1, 2, 3))
            else:
                enc, names = (lambda kk: (kmap[kk],)), ["K", "t", "m"]
                views = dict(order=(0,), algebra=(0,), geometry=(0,), information=(0,), statistics=(0, 1, 2))
            at = enc("quantum") + (1, 1)
            ans = []
            for cl, _, _ in CLAUSES:
                kn = known(cl, enc)
                r = _staged(CA, HL, names + [cl], kn, at, views, k)
                ans.append(r["answer"])
                law_k &= r["lawful"]
                if k == 3 and not MUT.get("two_bits"):
                    st = CA.closure(names + [cl], kn + [at + (CA.U,)], "statistics", 3)
                    for a in (0, 1):     # the one-flip rule: admitted at the top order iff every condition alone
                        rule = all(any(all(x[j] == at[j] for j in range(3) if j != i) and x[i] != at[i] and x[3] == a
                                       for x in kn) for i in range(3))   # can change, the answer kept at a
                        flip_ok &= ((at + (a,)) in st) == rule
                        flip_n += 1
                        stx = CA.closure(names + [cl], kn + [at + (a,)], "statistics", 3)
                        extensive &= (at + (a,)) in stx
            res[tuple(ans)] += 1
        one[k], lawful[k] = res, law_k
    for k in (2, 3, 4):
        res = Counter()
        for code in itertools.permutations([(0, 0), (0, 1), (1, 0), (1, 1)], 3):
            cm = dict(zip(NAMES3, code))
            at = cm["quantum"] + (1, 1)
            views = dict(order=(0, 1), algebra=(0, 1), geometry=(0, 1), information=(0, 1), statistics=(0, 1, 2, 3))
            res[tuple(_staged(CA, HL, ["c1", "c2", "t", "m", cl], known(cl, lambda kk: cm[kk]), at, views, k)["answer"]
                      for cl, _, _ in CLAUSES)] += 1
        bits[k] = res
    silent4 = CA.closure(["K", "t", "m", "f"], known("f", lambda kk: (NAMES3.index(kk),)) +
                         [(1, 1, 1, CA.U)], "statistics", 4) is None
    _P17[key] = dict(F=F, inside=inside, one=one, bits=bits, flip_ok=flip_ok, flip_n=flip_n, lawful=lawful,
                     extensive=extensive, silent4=silent4)
    return _P17[key]


_P18 = {}


def as_condition():
    """P18's contrast: survivability entered as a varying condition s (the object built under position 2's laws, 1, or
    not so equipped, 0 -- item 241's means of mitigation), read at statistics' rank with tension and matter"""
    key = tuple(sorted(k for k in MUT if k in ("absolute_readme",)))
    if key in _P18:
        return _P18[key]
    CA = _load("calculator.py", "c4o_calc")
    HL = _load_path(os.path.join(os.path.dirname(D68), "hlaw.py"), "c4o_hl")
    EP = _load("e_positive.py", "c4o_ep7")
    R = sp.Float(EP.example()["R_rh"] ** 3, 20)
    F, _ = population(R)                                    # s = 0: the object as P17 entered it
    rel = relative(R)["realized"]                           # s = 1: built in
    F3 = {}
    for (t, m), v in F.items():
        F3[(t, m, 0)] = v
        F3[(t, m, 1)] = (rel if t == 0 else {1}) if m == 1 else v
    A = {"inner": 1, "quantum": 1, "shell": 0}
    BE = {"inner": 0, "quantum": 1, "shell": 1}
    out, law = {}, {}
    for k in (2, 3, 4):
        res, lk = Counter(), True
        for perm in itertools.permutations(range(3)):
            kmap = dict(zip(NAMES3, perm))
            at = (kmap["quantum"], 1, 1, 1)
            views = dict(order=(0,), algebra=(0,), geometry=(0,), information=(0,), statistics=(0, 1, 2, 3))
            ans = []
            for cl, _, _ in CLAUSES:
                kn = []
                for kk in NAMES3:
                    for t, m, sv in itertools.product((0, 1), repeat=3):
                        if (kk, t, m, sv) == ("quantum", 1, 1, 1):
                            continue
                        for v in ({A[kk]} if cl == "a" else {BE[kk]} if cl == "be" else F3[(t, m, sv)]):
                            kn.append((kmap[kk], t, m, sv, v))
                r = _staged(CA, HL, ["K", "t", "m", "s", cl], kn, at, views, k)
                ans.append(r["answer"])
                lk &= r["lawful"]
            res[tuple(ans)] += 1
        out[k], law[k] = res, lk
    _P18[key] = dict(out=out, lawful=law)
    return _P18[key]


def tau_check():
    """P19 (item 301): tau, calculated (tau_share.py)"""
    TS = _load("tau_share.py", "c4o_ts")
    if MUT.get("tau_two_way"):
        TS.MUT["two_way"] = True                            # the mutant: one junction both sheets act on
    try:
        o = TS.compute()
        res = {n.split()[0]: ok for n, ok in TS.checks(o)}
    finally:
        TS.MUT.clear()
    return dict(tau=o["tv"]["tau"], side2=o["cq"].get("side2"), checks=res)


_P20 = {}
NAMES4 = ["singular", "inner", "quantum", "shell"]


def _channel_rule(kn, at, cont=(0, 1)):
    """P20, the board's reading of 302 (b): at the top order a continuation bit is a channel -- its neighbour, if one
    exists, is consistent with C4's answer whatever its own; the other conditions keep the one-flip rule"""
    out = set()
    for a in (0, 1):
        ok = True
        for i in range(len(at)):
            nb = {x[-1] for x in kn if all(x[j] == at[j] for j in range(len(at)) if j != i) and x[i] != at[i]}
            if MUT.get("channel_biased"):
                nb = nb | {1}                               # the mutant: every neighbour taken as agreeing with 1
            ok &= (len(nb) > 0) if (i in cont and not MUT.get("channel_off")) else (a in nb)
        if ok:
            out.add(a)
    return {(0,): 0, (1,): 1, (0, 1): "both", (): "refused"}[tuple(sorted(out))]


def more_continuations():
    """P20 (item 302): the continuation's own two clauses, the fourth interior entered; the top order under the
    operator and under the channel reading; each interior as the question for control"""
    key = tuple(sorted(k for k in MUT if k in ("three_continuations", "channel_off", "channel_biased")))
    if key in _P20:
        return _P20[key]
    CA = _load("calculator.py", "c4o_calc")
    HL = _load_path(os.path.join(os.path.dirname(D68), "hlaw.py"), "c4o_hl")
    BI = _load("b_interior.py", "c4o_bi8")
    cells = BI.cells()
    inter = {"singular": cells[(0, "none", "ours")], "inner": cells[(1, "none", "pos2")],
             "quantum": cells[(0, "quantum", "pos2")], "shell": cells[(0, "shell", "pos2")]}
    names = [n for n in NAMES4 if not (MUT.get("three_continuations") and n == "singular")]
    own = {k: (inter[k]["nec"], inter[k]["readme_only"]) for k in NAMES4}
    A = {k: int(k != "shell") for k in NAMES4}
    BE = {k: inter[k]["complete"] for k in NAMES4}
    F = {(1, 1): {1}, (1, 0): {0, 1}, (0, 1): {1}, (0, 0): {0, 1}}     # P18's population, survivability built in
    views = dict(order=(0, 1), algebra=(0, 1), geometry=(0, 1), information=(0, 1), statistics=(0, 1, 2, 3))

    def known(cl, cm, q):
        rows = []
        for kk in names:
            for t, m in itertools.product((0, 1), repeat=2):
                if (kk, t, m) == q:
                    continue
                for v in ({A[kk]} if cl == "a" else {BE[kk]} if cl == "be" else F[(t, m)]):
                    rows.append(cm[kk] + (t, m, v))
        return rows

    def run(code, k, q="quantum", rule=False):
        cm = dict(zip(NAMES4, code))
        at = cm[q] + (1, 1)
        if rule:
            return tuple(_channel_rule(known(cl, cm, (q, 1, 1)), at) for cl, _, _ in CLAUSES)
        return tuple(_staged(CA, HL, ["c1", "c2", "t", "m", cl], known(cl, cm, (q, 1, 1)), at, views, k)["answer"]
                     for cl, _, _ in CLAUSES)

    ownc = tuple(own[k] for k in NAMES4)
    codes = list(itertools.permutations([(0, 0), (0, 1), (1, 0), (1, 1)], 4))
    out = dict(own=own, ownrun={k: run(ownc, k) for k in (2, 3, 4)}, ownrule=run(ownc, 4, rule=True),
               all={k: Counter(run(c, k) for c in codes) for k in (2, 3, 4)},
               allrule=Counter(run(c, 4, rule=True) for c in codes),
               control={q: (run(ownc, 4, q=q, rule=True), (A[q], BE[q], 1)) for q in NAMES4 if q in names})
    _P20[key] = out
    return out


def compute():
    return dict(k=komar(), eq=equator(), c1=c1_parts(), pos=positive(), st=state(), ch=choices(), ca=calc(),
                wd=widen(), cl=clauses(), rk=ranks(), pl=placements(), fm=form(), fb=flux_bend(), fc=faces(),
                hi=higher(), sv=higher(survive=True), rl=relative(sp.Float(_load("e_positive.py", "c4o_ep6").example()[
                    "R_rh"] ** 3, 20)), ac=as_condition(), tc=tau_check(),
                mc=more_continuations())


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
    c = o["cl"]
    for cl, desc, _ in CLAUSES:
        r = c["named"]["out"][cl]
        print("P10 %s %s: answer %s by %s; %s; magnitudes %s; extensive %s, lawful %s, void %s" % (
            cl, desc, r["answer"], r["by"], "; ".join("%s %s" % (t[0], t[1]) for t in r["trace"] if t[0] != "documentary"),
            r["magnitudes"], r["extensive"], r["lawful"], r["void"]))
    print("P10 logic joins %s -> %s" % (c["named"]["ans"], c["named"]["join"]))
    for tf, mf in itertools.product((0, 1), repeat=2):
        print("P10 tension coded %s, matter coded %s, 24 continuation codes: %s" % (
            "+sigma = 1" if tf else "keeps 139 (1) = 1", "none = 1" if mf else "README = 1",
            dict(Counter(v["ans"] for (cd, a, b), v in c["sweep"].items() if (a, b) == (tf, mf)))))
    for k in (1, 2, 3, 4):
        print("P10 statistics order %d, the board's coding, 24 continuation codes: %s" % (
            k, dict(Counter(c["orders"][k]))))
    pl_ = o["pl"]
    for sc in SCEN:
        for k in (1, 2, 3, 4):
            v = [x for kk, x in pl_[sc].items() if kk[3] == k]
            print("P12 %-16s order %d, 96 codings: %s; lawful %d of 96; known configurations %s" % (
                sc, k, dict(Counter((x["ans"], x["join"]) for x in v)), sum(x["lawful"] for x in v),
                sorted({x["known"] for x in v})))
    fm = o["fm"]
    for t, c_ in fm["out"].items():
        print("P13 tension and matter read by %-20s 96 codings at order 2: %s" % (t + ":", dict(c_)))
    print("P13 seen among the eleven: C4's continuation %s, C4's P2 state %s, the combination %s" % (
        fm["seen"]["cont"], fm["seen"]["pstate"], fm["seen"]["combo"]))
    fb = o["fb"]
    print("P14 the flux's bending against the tension's: %s = %.3g at r_h (K r_h %.2g against %.2g), %.2g at 10 r_h" % (
        fb["ratio_sym"], fb["ratio"], fb["K_flux"], fb["K_tension"], fb["at10"]))
    fc = o["fc"]
    print("P15 kappa %s; d(UV)/dr at r_h %s (r analytic in UV across the faces: %s); SAdS root simple %s; the bounce "
          "keeps UV %s" % (fc["kappa"], fc["dUV"], fc["analytic"], fc["sads_simple"], fc["bounce_keeps"]))
    hi = o["hi"]
    print("P17 the population's (f) over (t, m): %s (witnesses inside their classes: %s)" % (hi["F"], hi["inside"]))
    for k in (1, 2, 3, 4):
        print("P17 the continuation one condition, order %d, its 6 orderings: %s; lawful %s%s" % (
            k, dict(hi["one"][k]), hi["lawful"][k], "; statistics silent" if k == 4 and hi["silent4"] else ""))
    for k in (2, 3, 4):
        print("P17 the continuation as two bits, order %d, 24 codes: %s" % (k, dict(hi["bits"][k])))
    print("P17 the one-flip rule at the top order: %s on %d cases; extensive %s" % (hi["flip_ok"], hi["flip_n"],
                                                                                  hi["extensive"]))
    rl, sv, ac = o["rl"], o["sv"], o["ac"]
    print("P18 the object built under each position 2's laws: P2's total tau + (R/4)|tau| positive for tau > 0 %s and "
          "tau < 0 %s; at any other relative tension it realizes %s" % (rl["pos_side"], rl["neg_side"], rl["realized"]))
    for k in (2, 3, 4):
        print("P18 survivability built in, order %d: one condition %s%s; two bits %s" % (
            k, dict(sv["one"][k]), " (statistics silent)" if k == 4 and sv["silent4"] else "", dict(sv["bits"][k])))
    for k in (2, 3, 4):
        print("P18 contrast, survivability a varying condition, order %d: %s; lawful %s" % (k, dict(ac["out"][k]),
                                                                                         ac["lawful"][k]))
    mc = o["mc"]
    print("P20 the continuation's own clauses (NEC holds, README-only): %s" % mc["own"])
    for k in (2, 3, 4):
        print("P20 four interiors, order %d: own code %s; all 24 codes %s" % (k, mc["ownrun"][k], dict(mc["all"][k])))
    print("P20 the channel reading at the top order: own code %s; all 24 codes %s" % (mc["ownrule"],
                                                                                   dict(mc["allrule"])))
    print("P20 control, each interior as the question: %s" % mc["control"])
    tc = o["tc"]
    print("P19 tau = %s (tau_share.py); position 2's side carries %s lambda_RS; tau_share's checks %s" % (
        tc["tau"], tc["side2"], tc["checks"]))
    rk = o["rk"]
    for pl in PLACES:
        for k in (1, 2, 3, 4):
            cells_ = {kk: v for kk, v in rk["out"][pl].items() if kk[3] == k}
            bys = Counter(b for kk, v in rk["by"][pl].items() if kk[3] == k for b in v)
            print("P11 %-5s order %d, 96 codings: %s; answered by %s" % (
                pl, k, dict(Counter(v[1] for v in cells_.values())), dict(bys)))
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
    c = o["cl"]
    nm = c["named"]
    ok = nm["ans"] == (1, 1, 1) and nm["join"] == 1
    for cl, _, _ in CLAUSES:
        r = nm["out"][cl]
        tr = dict((t[0], t[1]) for t in r["trace"])
        ok &= r["by"] == "statistics" and tr["statistics"] == [1] and tr["geometry"] == [1] and tr["analysis"] == "both"
        ok &= r["extensive"] and r["lawful"] and not r["void"] and tr["documentary"] == "citations"
    ok &= "%.3g" % nm["out"]["f"]["magnitudes"][1] == "15.8" and nm["out"]["a"]["magnitudes"][1] is None
    add("P10 clause by clause, b_interior's code, keeps 139 (1) = 1, README = 1: (a), (b)/(e) and (f) each 1 by "
        "statistics, geometry 1 alone, (f) at +15.8 decades; logic joins 1 -- M1 holds; extensive, lawful, no key or "
        "one-hot", ok)
    sw = c["sweep"].values()
    conv = [v for (cd, tf, mf), v in c["sweep"].items() if (tf, mf) == (0, 0)]
    ok = len(conv) == 24 and all(v["ans"] == (1, 1, 1) for v in conv)
    ok &= sum(v["ans"] == (1, 1, 1) for v in sw) == 54 and sum(v["ans"] == ("refused",) * 3 for v in sw) == 42
    ok &= all(v["reach"] == (v["ans"] == (1, 1, 1)) for v in sw) and not any(r["void"] for v in sw
                                                                             for r in v["out"].values())
    ok &= not any(a in (0, "both") for v in sw for a in v["ans"])
    add("P10 every code: with the board's coding all 24 continuation codes give 1, 1, 1; over all 96 codings 54 give "
        "1, 1, 1 and 42 are refused, exactly where C4's row is not a join of the rows below it (information); no clause "
        "is ever 0 or undecided; none voided", ok)
    od = c["orders"]
    ok = all(a == (1, 1, 1) for k in (1, 2) for a in od[k]) and all(a == ("refused",) * 3 for a in od[4])
    ok &= sum(a == (1, 1, "refused") for a in od[3]) == 16 and sum(a == (1, 1, 1) for a in od[3]) == 8
    ok &= not any(x in (0, "both") for k in od for a in od[k] for x in a)
    add("P10 by statistics order, the board's coding: orders 1 and 2 give 1, 1, 1 in all 24 codes; order 3 refuses (f) "
        "in 16 and gives 1, 1, 1 in 8; order 4 refuses all three; never 0 or undecided", ok)
    rk = o["rk"]["out"]
    at = lambda pl, k: [v for kk, v in rk[pl].items() if kk[3] == k]
    n1 = lambda pl, k: sum(v[1] == 1 for v in at(pl, k))
    ok = [n1("peers", k) for k in (1, 2, 3, 4)] == [54, 54, 22, 0]
    ok &= all(n1(pl, k) == 96 for pl in ("own", "first") for k in (1, 2, 3, 4))
    ok &= [n1("last", k) for k in (1, 2, 3, 4)] == [96, 96, 96, 0]
    ok &= all(v[0] == (1, 1, "refused") for v in at("last", 4))
    ok &= not any(a in (0, "both") for pl in PLACES for v in rk[pl].values() for a in v[0])
    add("P11 with P2's tension and matter at each place among M1's clauses, 96 codings x orders 1-4: beside the "
        "continuation (P10) 54, 54, 22, 0 decided; on (f)'s own rank, or ranked first, 1, 1, 1 in every coding at every "
        "order; ranked last, 1, 1, 1 at orders 1-3 and (f) refused at order 4; never 0 or undecided", ok)
    pl_ = o["pl"]
    tally = lambda sc, k: Counter((x["ans"], x["join"]) for kk, x in pl_[sc].items() if kk[3] == k)
    R3, B2 = ("refused",) * 3, ("both", "both", 1)
    ok = [tally("peers", k)[((1, 1, 1), 1)] for k in (1, 2, 3, 4)] == [54, 54, 22, 0]
    for sc, first in (("statistics' rank", (1, 1, "both")), ("broad ranks", B2)):
        ok &= tally(sc, 1) == Counter({(first, "not binary"): 96}) and tally(sc, 2) == Counter({((1, 1, 1), 1): 96})
        ok &= tally(sc, 3) == Counter({((1, 1, "refused"), "not binary"): 64, ((1, 1, 1), 1): 32})
        ok &= tally(sc, 4) == Counter({(R3, "not binary"): 96})
    ok &= tally("given", 1) == Counter({(R3, "not binary"): 88, ((1, 1, 1), 1): 8})
    ok &= tally("given", 2) == Counter({(R3, "not binary"): 88, (("refused", "refused", 1), "not binary"): 8})
    ok &= all(tally("given", k) == Counter({(R3, "not binary"): 96}) for k in (3, 4))
    ok &= all(x["known"] == 2 for kk, x in pl_["given"].items())
    ok &= all(x["lawful"] == (kk[3] != 1) for sc in SCEN for kk, x in pl_[sc].items())
    ok &= not any(0 in x["ans"] for sc in SCEN for x in pl_[sc].values())
    ok &= all("%.3g" % x["mag"] == "15.8" for sc in SCEN for x in pl_[sc].values())
    add("P12 tension and matter kept in every clause, 96 codings x orders 1-4: at statistics' rank or at the broad ranks "
        "1, 1, 1 in every coding at order 2, undecided on the clause whose conditions enter only at statistics at order "
        "1, (f) refused in 64 at order 3, all refused at order 4; as the given (2 configurations) refused but for 8 "
        "codings at orders 1-2; P10's placement 54, 54, 22, 0; the law's containments hold at orders 2-4 and fail at "
        "order 1 in every placement; never 0", ok)
    fm = o["fm"]["out"]
    ok = fm["form"] == Counter({(1, 1, 1): 96}) and fm["geometry too"] == fm["form"]
    ok &= fm["all but information"] == fm["form"]
    ok &= fm["information too"] == Counter({(1, 1, 1): 54, ("refused",) * 3: 42})
    ok &= o["fm"]["seen"] == {"cont": True, "pstate": True, "combo": False}
    add("P13 the form: tension and matter in every clause, read at statistics' rank -- the cypher agrees, 1, 1, 1 in all "
        "96 codings at order 2; it agrees too with geometry or every language but information reading them, and refuses "
        "in 42 whenever information does; C4's continuation and its P2 state are each seen, their combination not", ok)
    fb = o["fb"]
    add("P14 the outgoing flux is traceless; by Israel it bends P1 3 rho/sigma = 0.86 as much as the tension at r_h "
        "(K r_h 6.9e-16 against 8.0e-16), falling as (r_h/r)^2", fb["traceless"] and str(fb["ratio_sym"]) == "3*rho/sigma"
        and "%.2f" % fb["ratio"] == "0.86" and "%.2g" % fb["K_flux"] == "6.9e-16" and "%.2g" % fb["K_tension"] == "8e-16")
    fc = o["fc"]
    add("P15 the horizon is non-extremal (kappa = 1/r_h; SAdS's root simple), d(UV)/dr = -e^2/(2 r_h) at r_h: r is "
        "analytic in UV across both faces; the bounce's map keeps UV", fc["analytic"] and fc["ok_rstar"]
        and fc["sads_simple"] and fc["bounce_keeps"] and str(fc["kappa"]) == "1/r_h")
    hi = o["hi"]
    ok = hi["F"] == {(1, 1): {1}, (1, 0): {0, 1}, (0, 1): {0, 1}, (0, 0): {0, 1}} and hi["inside"]
    ok &= hi["one"][3] == Counter({(1, 1, 1): 6}) and hi["one"][2] == Counter({(1, 1, "both"): 6})
    ok &= hi["one"][4] == Counter({(1, 1, "both"): 6}) and hi["silent4"]
    ok &= hi["bits"][3] == Counter({(1, 1, 1): 24}) and hi["bits"][2] == Counter({(1, 1, "both"): 24})
    ok &= hi["bits"][4] == Counter({("refused",) * 3: 16, ("refused", "refused", 1): 8})
    ok &= hi["flip_ok"] and hi["flip_n"] == 36 and hi["extensive"] and all(hi["lawful"][k] for k in (2, 3, 4))
    add("P17 the higher orders: with the population of tensions and matters (295) the cypher agrees at order 3, 1, 1, 1, "
        "under every ordering and every two-bit code; order 2 leaves (f) open, its law three-way; with the continuation "
        "one condition the top order is 3, order 4 silent; as two bits order 4 refuses, by the one-flip rule (exact on "
        "36 cases); lawful at 2-4", ok)
    rl, sv, ac = o["rl"], o["sv"], o["ac"]
    ok = rl["pos_side"] and rl["neg_side"] and rl["zero"] and rl["realized"] == {1}
    ok &= sv["F"] == {(1, 1): {1}, (1, 0): {0, 1}, (0, 1): {1}, (0, 0): {0, 1}}
    ok &= all(sv["one"][k] == Counter({(1, 1, 1): 6}) for k in (2, 3)) and sv["silent4"]
    ok &= all(sv["bits"][k] == Counter({(1, 1, 1): 24}) for k in (2, 3))
    ok &= sv["bits"][4] == Counter({("refused",) * 3: 16, ("refused", "refused", 1): 8})
    ok &= sv["flip_ok"] and sv["extensive"] and all(sv["lawful"][k] for k in (2, 3, 4))
    add("P18 survivability built in (300): the object's total positive at every relative tension, exact; the cypher "
        "agrees at orders 2 and 3, 1, 1, 1, under every ordering and every two-bit code; the order-4 refusals left are the "
        "two-bit code's alone; lawful, extensive", ok)
    ok = all(ac["out"][k] == Counter({(1, 1, 1): 6}) for k in (3, 4)) and ac["out"][2] == Counter({(1, 1, "both"): 6})
    ok &= all(ac["lawful"][k] for k in (2, 3, 4))
    add("P18 contrast: survivability a varying condition gives a fourth order that agrees, with order 3, and reopens (f) "
        "at order 2", ok)
    tc = o["tc"]
    add("P19 tau calculated before the verifier (tau_share.py): 3/4, position 2 receiving the summed tension lambda_RS; "
        "P4's crossing share positive at it (T5)", tc["tau"] == sp.Rational(3, 4) and tc["side2"] == sp.Rational(2, 3)
        and all(tc["checks"].values()))
    mc = o["mc"]
    ok = mc["own"] == {"singular": (1, 1), "inner": (1, 0), "quantum": (0, 1), "shell": (0, 0)}
    ok &= mc["ownrun"][2] == mc["ownrun"][3] == (1, 1, 1) and mc["ownrun"][4] == ("refused", "refused", 1)
    ok &= mc["all"][3] == Counter({(1, 1, 1): 24}) and mc["all"][2] == Counter({(1, 1, 1): 22, (1, "both", 1): 2})
    ok &= mc["all"][4] == Counter({("refused", "refused", 1): 16, (1, "refused", 1): 8})
    add("P20 the fourth interior entered (b_interior's singular, the code none held): orders 2 and 3 1, 1, 1; at order 4 "
        "(f) admitted, (a) and (b)/(e) refused, each carried by one continuation clause -- binary communications", ok)
    ok = mc["ownrule"] == (1, 1, 1) and mc["allrule"] == Counter({(1, 1, 1): 24}) and len(mc["control"]) == 4
    ok &= all(g == t for g, t in mc["control"].values())
    add("P20 the channel reading (302 (b)): the top order 1, 1, 1 under every code; each interior as the question returns "
        "its own answers", ok)
    return res


MUTANTS = {"bent_equator": "the reflection chi -> pi - chi broken in the angular metric",
           "p2_free_positive": "P2 taken positive at -sigma/4 without the README",
           "readme_thin": "the README's density at the face put below sigma/4",
           "bath_kept": "the Hartle-Hawking bath's ingoing half kept",
           "fails_alone_dropped": "the known cells where (a) alone fails removed (P9)",
           "m1_or": "M1 read as any one clause holding, not all (P9)",
           "no_readme_coordinate": "P2's matter dropped from the attributes (P10)",
           "shell_continuation": "C4's continuation read as the classical shell (P10)",
           "tm_with_continuation": "tension and matter put back beside the continuation on its own rank (P11)",
           "c4_without_readme": "C4's configuration read without the README (P11)",
           "info_sees_all": "information shown tension and matter at statistics' rank (P12)",
           "given_by_tension": "the given fixed by the tension alone, the matter varying (P12)",
           "info_reads_order": "information let read tension and matter in the form (P13)",
           "flux_as_tension": "the flux's Israel term taken with the tension's factor (P14)",
           "extremal": "the horizon taken extremal, a double root (P15)",
           "bounded_tension": "relative tension kept within [-1, 1], no tension outweighing the README (P17)",
           "finite_grid": "the index's four (t, m) cells, not the population (P17)",
           "two_bits": "the continuation entered as two bits in the solved form (P17)",
           "absolute_readme": "the object's density kept at ours in every position 2, not scaled (P18)",
           "tau_two_way": "tau read from one junction both sheets act on (through tau_share) (P19)",
           "three_continuations": "the fourth interior left out (P20)",
           "channel_off": "the continuation bits held to the one-flip rule (P20)",
           "channel_biased": "every neighbour taken as agreeing with 1 (P20)"}


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
