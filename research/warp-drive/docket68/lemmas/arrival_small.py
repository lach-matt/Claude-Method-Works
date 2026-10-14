#!/usr/bin/env python3
"""arrival_small.py -- items 338, 340, 343, 344, 348: the ARRIVAL row at the family's small end, on the one-way object.
M: "Continue" (to the board's report of items 336-337, which named ARRIVAL next in item 335's order: CLOSE, then
ARRIVAL and FAR, with B3 and B4d resting on them). The row: "the README forms the corridor as it comes in (198, M's
guess); how the bits rebuild and take their room" (284 (d), 285 (d)). Its first half was computed only at the large
end, in four dimensions (README-HELD.md 2-3, readme_held.py). At the small end write_small's verifier recorded it as
not computed: "reading (ii) is not computed" (264). Worked in the conversation (computed with sympy and a
Dormand-Prince integrator written here, exact where marked; READ where marked; deduced where marked; not verified by
a separate session; not seated); 2026-10-13. [Item 348: verified by one separate session, CONFIRMED with
qualifications, one sentence refuted (V11 (b), with V3 behind it); the qualifications are seated in item-348 notes and
V14.]

  V0 (read) The words the row rests on, verbatim in the rulings file: 198, "My guess would be 1." (the board's option
     (a): the README comes in while the corridor forms, with no partner, the size growing as it comes in and fixed once
     the whole README is in); 94, "The corridor is a single channel that grows in size to accommodate the size of the
     README"; 162, "It is and always will be only the size that is needed to hold the object once and at once"; 163,
     "All together, one whole"; 109, "A horizon cannot exist without the object of which it needs to exist"; 136 (1),
     "1 - yes" (H-EXACT-ENERGY-AT-BOUND: the one exact energy is E(N) at the bound); 136 (2), "released at position two
     at the closing of the horizon, which activates the higgs field forming the mass defined in the README"; 136 (6),
     "the bits are absorbed by position 2, and rebuild is likely instantaneous"; 136 G, "G - the README is the energy,
     not separate"; 158 (2), "Exactly as long as the write needs"; 240, "the object is built from the bulk at position
     2 as an exact copy under the laws and conditions of position 2"; 285, "It is an exact copy of the object of
     position 1, but it now obeys laws of position 2"; 336, "I think it is B"; 338, "Continue".
     [Item 348 (Q7, Q11 (a)), the verifier: 158 (2) as quoted here stops before M's "I should think", which 158's record
     keeps ("Exactly as long as the write needs I should think"). Two board passages shown as quotations are not
     verbatim at the source cited: "the face stands at least 66,980 clocks while the write runs" (V10, V11 (c)) is the
     board's 340 question, write_cypher W5 (b) reading "...while the write runs, 66,980 clocks or more"; and "reading
     (ii) is not computed" (the header) is write_small S3's item-264 note, not item 264's text.]
  V1 (computed, exact) The flux, the one E, the curvature.  On our side's five-dimensional ingoing form the only
     Einstein component is G_vv = 3 mu'(v)/(2 r^3) (close_small K1, re-run): an arrival that only adds energy, mu' >=
     0, has non-negative null energy on every ray, so it forms our face with no partner and keeps (Z) classically --
     nothing to pair, 183 not called on.  After it the Misner-Sharp mass is mu0 = r_h^2, E = 3 pi mu0/(8 G5) (K4's
     identity): the README's E is the hole's, one E, as 136 G has it ("the README is the energy").  On reading (i) --
     a face of the README's size standing through the write, the README crossing it (S4; 264) -- the hole ends with E
     besides the README's: 2E, a face of 2^(1/2) r_h holding 2^(3/2) N = 2.83 N bits, not "only the size that is needed"
     (162) and not 136 G's one energy; write_small's verifier recorded that 2E as reading (i)'s open question.  The
     Kretschmann scalar is 72 mu^2/r^8, mu' entering nowhere (computed, exact).
  V2 (computed; H-BITS-WITH-ENERGY, the board's, for the bit counts) The face as the README arrives, reading (ii). The
     arrival mu(v) = r_h^2 s(v/w), s the smoothstep of onset order n (s ~ x^n), width w in clocks of r_h/c, the event
     horizon traced back from r_h (Dormand-Prince 5(4), rtol 1e-10). For w <= 4 at every order n = 1-4 the face is born
     before the README's first part arrives -- 1.76 to 0.26 clocks before it, in the flat region -- holding
     (|v_born|/2)^3 N at the onset: 0.43-0.46 N at w = 1, 0.67-0.68 N at w = 0.5. From w = 8 at orders 3 and 4, and from
     w = 9 at order 2 (V3), it is born at the onset itself; at order 1 always before it, by 0.003 clocks at w = 1000.
     The trapping horizon r^2 = mu holds e^(3/2) N at a fraction e of E -- short of the e N that have come in by
     e^(1/2), so it holds the README only whole (computed, exact): 163's "all together, one whole", the record's
     H-WHOLE-AS-G1, here in five dimensions (README-HELD 3 found f^(3/2) N by deduction).
     [Item 348 (Q3, Q11 (b)), the verifier: "born before the onset" and V2-V4's thresholds belong to an event horizon
     traced back from r_h at v = w, so they presume the face static from v = w on -- nothing else crossing it, 336's
     evaporation neglected. As numbers they stand: a disturbance Delta v clocks later moves the face at the arrival by
     about e^(-Delta v), the evaporation by about 1e-15; but matter crossing within a few clocks would move both, and no
     bulk is ever empty (320). "From w = 8" is the grid's first point above 5.27 and 4.79.]
  V3 (computed, exact) The centre at the onset, for radial null dust. Self-similar onset mu = lambda v^2: outgoing rays
     r = x v obey 2 x^3 - x^2 + lambda = 0, with a positive root, an escaping ray from the singular onset, iff lambda <=
     1/27 (the four-dimensional 1/16's counterpart). The order-2 smoothstep has lambda = 3/w^2: naked from w = 9. Order
     1 (a finite flux at the onset): no outgoing ray leaves the onset point (deduced: where r^2 < mu the outgoing rays
     fall inward; the face is born before the onset in every order-1 run). Order 3: an escaping ray r ~ v/2 sees K ~
     v^-2 -- the five-dimensional counterpart of README-HELD 5's cubic onset. Order 4: K bounded along it. An arrival
     whose face is born before its onset (V2) puts the onset behind the face whatever its order: the quantum region
     (273) stays inside our face. Born at the onset, an order-2 arrival from w = 9 or an order-3 arrival shows the onset
     to our exterior (deduced: the escaping ray r ~ v/2 runs outside the face, which leaves the onset as r ~ mu^(1/2),
     v^(3/2) at order 3).
     [Item 348 (Q1), the verifier, reproduced here (V14 (a)): "Order 4: K bounded along it" holds only along r ~ v/2.
     Once the face is born at the onset, rays just outside it escape, and traced back they leave the onset hugging the
     trapping horizon r^2 ~ mu, where K = 72/mu^2 diverges, at every order n >= 3: at orders 3 and 4 every arrival born
     at the onset shows a curvature-singular onset to our exterior. The code's onset test (onset_hidden) is corrected;
     V9's populations do not change.]
  V4 (READ; computed) The second law along the arrival.  READ: Bousso, hep-th/0203101v2, sec. II.A.3, eq. (2.3),
     Bekenstein's generalized second law, "dS_total >= 0", the total "black hole entropy and matter entropy"; sec. II.C.1
     (the Susskind process), "the initial entropy must not exceed the final entropy", whence S_matter <= A/4 (2.22); and
     sec. VII.B.3, "one cannot collapse more entropy through a (temporary) black hole horizon than it already has".
     READ: Wall, arXiv:1105.3445v6, abstract and sec. 1, the law proved "for semiclassical quantum fields falling across
     a causal horizon" with S_out "the von Neumann entropy of the matter fields restricted to the region outside of the
     horizon" (eq. (3)).  Two counts, and they part:
       the fine count (Wall's): the README one fixed exact encoding (136 (5)) is a definite state, so its own von
         Neumann entropy adds nothing beyond the vacuum's, and the law reduces to the area theorem -- which every run
         keeps, the face's area never falling (computed);
       the coarse count (Bousso's "thermodynamic system"): the README's carrier, a free gas holding 2^N states
         (write_small S3, H-BITS-ARE-STATES), has S = (4/3) a^(1/4) V^(1/4) E^(3/4), growing with V at fixed E
         (computed), equal to N ln2 at the write's floor ball (S3's construction) and more beyond it, while the face it
         forms holds exactly N ln2 at E(N) (136 (1); C2's construction, write_small S1). So the Susskind bound
         saturates, the carrier must start in the floor's ball exactly -- 158 (2)'s "exactly as long as the write needs"
         (deduced) -- and along the arrival the total S_gen(v) = (N - b) + C_face (bits in units of N, b the bits
         crossed) never falls below its start only for w up to 4.83, 5.75, 5.28, 4.82 clocks at orders 1-4 (computed,
         bisection), falling toward the spread limit min(e^(3/2) - e) = -4/27 N at e = 4/9 (computed, exact). And in
         every run dS_gen/dv < 0 somewhere (computed): the face grows ahead of the README (an event horizon's
         teleology), so at exact saturation the total rises and falls. On the coarse count (2.3) holds instant by
         instant for no arrival at 136 (1)'s exact energy, only as a limit (deduced, and so in every run: a face born
         before the onset lifts the total above its start, and it must come back to it at the end; one born at the onset
         holds e^(3/2) N < e N from the first).
     [Item 348 (Q3, Q7, Q8, Q11 (e)), the verifier: V2's teleology note holds here. The exact start at the floor's ball
     follows from the saturated bound alone: 158 (2) is consonant, not a premise, and since 336 it no longer times the
     hold (write_cypher W5's item-336 note). Bousso's (2.22) is for a stable, near-spherical system collapsed by an
     added shell, nothing radiated or ejected (his footnote 7), premises the README's own collapse from 66,981 r_h does
     not meet: what V4 uses is (2.3) from start to end with the final face's area, carrying footnote 7's no-loss
     assumption -- so "the Susskind bound saturates" reads "(2.3) saturates at the final face's area, nothing lost".
     VII.B.3 concerns matter collapsing through an existing hole, which bears on reading (i), not on formation. The fine
     count is the board's reading of 136 (5) here, as V12 (e) names it.]
  V5 (deduced) The write on reading (ii).  write_small S3's floor, 66,980 clocks at Z = 106.75 (imported), rests on
     H-WRITE-IS-ARRIVAL, H-FLAT-START, H-README-ALONE, H-FREE-GAS and H-BITS-ARE-STATES, not on S4's standing hole.  On
     reading (ii) the start is flat exactly (no face stands before the README) and the README's E is the only energy
     exactly (V1), so the floor carries unchanged and reading (i)'s 2E does not arise.  The 66,980 clocks are the
     README's approach in our exterior; its arrival onto the face is the width w, compact (V2-V4: w <= 4.79 clocks keeps
     both the onset behind the face and the coarse total at or above its start, at every order computed).  A converging
     carrier can arrive together from a ball of radius (1 + T) r_h if its inner parts wait (moving at most at c, the
     outer parts take T clocks); the state count of such a converging flow is not computed (does not claim).
     [Item 348 (Q5, Q11 (d)), the verifier: "the only energy exactly" is exact in 320 (b)'s limit, an empty bulk apart
     from the README -- the board's limit, not M's configuration; with the bulk's content it holds to that content's
     order (320 (c)). S3's hypotheses also include H-SMALL-CLOCK, H-HOLD-FRAME, H-README-ON-PLANE and the R1 count;
     under R2 the 8.0e-5 is 1.6e-4, the scale unchanged.]
  V6 (computed, exact) Position 2's release at the small end.  At the small end E and the face's capacity carry G5
     alone, no ell (C3 F4; write_small S3): E = 3 pi r_h^2/(8 G5), N ln2 = 2 pi^2 r_h^3/(4 G5).  Each destination's own
     G5 (bulk5_index: 2^(1/2) of ours at 2b and 2c, 2^(3/2) at 2P and 2a + 2P, 4 at 2b + 2P and 2c + 2P, ours at 2a):
       240 (b)'s reading -- position 2's face holds exactly the README at its own bit area -- gives r_h2/r_h =
         (G5_2/G5)^(1/3) and E2/E = (G5/G5_2)^(1/3): 1, 0.891, 0.707, 0.630 (computed), against the large end's
         (G/G2)^(1/2), 1, 0.707, 0.707, 0.5 (copy_p2 C1);
       the glued object read as one Kruskal geometry, one r_h for both faces (b_bounce Q1's isometry; O1c's core, 337
         (Q10)), gives E2/E = G5/G5_2 and a capacity N G5/G5_2: 1, 0.707, 0.354, 0.25 -- short of N at nine of the
         twelve, the README not fitting there.
     The two agree only where G5_2 = G5: ours, 2a-min and 2a-mirror (computed).  The board's reading, to be overruled
     by M at any point: 240 governs ("The mass on position 2's side is not equal to ours"), so at the nine destinations
     the two faces' radii differ and the bounce joins them through the quantum region, which gives up classical GR
     there (273); the isometric gluing is the case G5_2 = G5.  B5a's side total needs no single kappa (b5a_residue A6,
     339 (Q5)); this is the faces', not the planes'.
     [Item 348 (Q5): the one-r_h reading rests on the board's 273 (a), the Kruskal isometry (b_bounce Q1), named now.]
  V7 (computed from banked numbers) The room.  The copy has the original's atoms (285 (b): an exact copy), so a
     pure-metal object's copy fills (a0_law/a0_ours)^3 of its volume (p2_matter X3, PBE, the law RECONSTRUCTED): copper
     0.9387 / 0.8837, silver 0.8127 / 0.7106, gold 0.9898 / 0.9677, chromium 1.0469 / 1.0627 under position 2a's min /
     mirror readings -- 285 (b)'s eight figures, computed in conversation there and seated here.  Every destination of
     our matter law (2b, 2P, 2b + 2P) gives 1: G moves no atom's size (copy_p2 C2).  It takes room by displacing what is
     there (284 (2)) and stays as the new whole of position 2 (285, R6).
  V8 (deduced; M's statements named) The rebuild, step by step, and what each rests on.  (1) Our face forms as the
     README arrives, compact, all together, and each part falls to the bounce's region within a clock (V2; hold_small
     L1, L5) -- computed.  (2) The bounce carries it to position 2's face (273; O1c verified, 337).  (3) Position 2's
     face is open at most 33.6 of its clocks (c_junction J1) -- computed; the README emerges there (m1p2x_oneway O4;
     c5_oneway U12 (Q3)).  The compact arrival's width, at most 4.79 of our clocks, is shorter than that open period,
     so even a bounce that kept the span would fit it (computed comparison); J3's asymmetry is not needed for the
     README's crossing.  (4) Position 2 absorbs the bits (136 (6)) -- M's.  (5) Position 2's face closes, releasing
     position 2's own energy (110, 111 (a), 240; 336 K9), E2 as in V6 -- computed on a reading; it activates the Higgs
     field forming the mass the README defines (136 (2)), the build's need being that activation (239) -- M's.  (6) The
     copy is built from position 2's bulk as an exact copy under position 2's laws (240, 285), its mass position 2's
     own -- rest masses the shared SI's, binding moving them by at most 3.7e-11 (copy_p2 C2) -- and what can be built is
     set by position 2's material laws (136 H): under the mirror law Cu2 holds no bound minimum (p2_matter X2), so a
     copy that needs that bond as such is not built there, while the metals' solids bind under all three laws (X3).
     (7) It takes its room (V7) and stays.  (8) The rebuild "likely instantaneous" (136 (6)) -- M's, with 94's
     H-INSTANTANEOUS.  How bits become matter is M's statement, not a configuration: the cypher NOT-RUN for it (an index
     of steps would carry the answer as a key, 211); copy_p2 C5 already ran the destinations' variances through it.
     [Item 348 (Q2, Q5, Q6), the verifier: (1)'s "compact" and (3)'s comparison use the model's 4.79 clocks against J1's
     33.06-34.53, a margin of about 6.9, so (3) and its "J3's asymmetry is not needed" rest on the model's value (V12's
     item-348 note). (5) uses the board's 336 (a), named at 341 (Q10). And J1 is evaluated at our face's r_h: at each
     destination's own face, with its own ell and the G5 readings, the period is 32.60-34.53 of position 2's clocks (V14
     (c); the verifier's convention gives 31.2-34.1), at least 6.91 w* in our clocks -- the comparison stands.]
     [Item 387: M ruled position 2's own sigma, ours at 218's destination, so J1's junction does not rise. The open
     period is J2's short phase, about 2 clocks (c_junction J4; READ, an order). (3)'s comparison is then reversed:
     the width must be below about 2 clocks, under the 4.79. That is a requirement on SOURCE (SOURCE-REQUIRED item
     10). Kept as written.]
  V9 (computed) ARRIVAL's question through the calculator, clause by clause in the form C4's stands in (291; c4_residue
     R9, R12): the classes t, the arrival compact (within V4's widths) or spread, and m, the README or other matter --
     no arrival, a README on a standing face (reading (i)), the README with 183's exact partner (README-HELD 2: no face
     forms), other matter arriving alone.  f1, "forms our face with no partner, (Z) kept, its own one E": {(1, 1): {1},
     (0, 1): {1}, (1, 0): {0, 1}, (0, 0): {0, 1}} -- 1 at orders 2 and 3 under all 96 codings, asked at the compact
     README and at the spread.  f2, "the onset behind the face or regular": {(1, 1): {1}, (0, 1): {0, 1}, (1, 0): {1},
     (0, 0): {0, 1}} from V2-V3 -- 1 at orders 2 and 3 for the compact README; for the spread, "both" at order 2 and 1 at
     order 3, the order-3 answer a read-back of the other cells, the spread's own population {0, 1} computed and
     deciding.  211's audit clean on every question.  As for C4, B5a and C8, the 1s add nothing to V1-V3.
     [Item 348 (Q4), the verifier, reproduced here (V14 (b)): the 96/96 is the statistics-rank protocol, statistics
     alone seeing every condition. With every language seeing every condition, f1 at both cells and f2 for the compact
     README are 1 in 60/96 and refused in 36, and f2 for the spread at order 2 is "both" in 36, refused in 36, 1 in 24
     -- 310 (Q4)'s "(peers 60/96)" bears here as it did for C8. The 1s still add nothing to V1-V3.]
  V10 (put to M) The fork that remains.  On reading (ii) -- 198, M's guess -- the README's own E forms our face as it
     arrives, one energy, compact, the face born about a clock before the README crosses and standing for the hole's
     life after (336); the write's 66,980 clocks are the approach.  That reads 334's "the face stands at least 66,980
     clocks while the write runs" (W5 (b)) as the write's arrival.  On reading (i) -- 334's wording as written -- a face
     of the README's size stands through the write, the README crossing it part by part, and the hole carries 2E.
     Which holds is M's: the record carries 198 as a guess and 334 as confirmed, and they part here.
     [Item 340, M's answer, verbatim: "C, but my guess is A" -- for the math, M's guess the board's option (A). Worked
     in V11.]
  V11 (item 340; computed; deduced) For the math, M's guess A. (a) Reading (i) against M's statements: its 2E against
     one exact energy, E(N) at the bound (136 (1)) and the README as the energy, not separate (136 G); its face holding
     2^(3/2) N = 2.83 N against "only the size that is needed to hold the object" (162; V1, computed); and a face
     standing before the object it needs (109). Reading (ii) meets all four (V1). So the math, on M's statements, gives
     reading (ii), M's guess A (deduced). (b) Within (ii), compact against spread. 162, "The throat doesn't change
     size": a compact arrival -- the widest that keeps the onset behind the face and the coarse count at every order, w
     = 4.79 clocks -- changes the face's size over at most w - v_born = 5.39 clocks (order 1; 5.07, 4.90 and 4.79 at
     orders 2-4), 8.0e-5 of the write's 66,980 (computed), and a spread one over the whole write. 163, "All together,
     one whole": a compact arrival crosses within 4.79 clocks, a spread one over the write, part after part. The second
     law: the fine count (136 (5), the README a definite state) does not decide; the coarse count gives compact (V4).
     Censorship admits a spread arrival only at onset orders 1 and 4 and above (V3). So the math, on 162 and 163, gives
     A with a compact arrival (deduced) -- the board's reading, to be overruled by M at any point. (c) What it re-reads:
     334's W5 (b) consequence, "the face stands at least 66,980 clocks while the write runs", becomes "the face stands
     from the README's arrival through the hole's life" (336), the write's 66,980 clocks its approach;
     M-HOLD-IS-THE-FACE's core -- the hold is the face standing, not how long the README stays within the horizon -- is
     unchanged. 198's option text, "the size growing as it comes in", holds over the arrival's few clocks.
     [Item 348 (Q1, Q9, Q10), the verifier: (b)'s "Censorship admits a spread arrival only at onset orders 1 and 4 and
     above (V3)" is REFUTED at order 4 (V3's item-348 note, V14 (a)). Correct: among the orders computed, censorship
     admits a spread arrival only at order 1, and at order 2 below 9 clocks; at orders 3 and 4 every arrival wider than
     5.27 and 4.79 clocks shows a curvature-singular onset to our exterior. The conclusion is strengthened, not moved.
     (b)'s "the coarse count gives compact": read instant by instant, as (2.3) puts it, the coarse count admits no
     arrival at the exact energy (V4); compact arrivals pass only its integrated necessary form, never below the start,
     which spread arrivals fail. (a): 109 counts against reading (i) only with the README read as the standing face's
     object; on reading (i) that face has its own E (264 (1)), so 109 is not independent of 136 (1) and 136 G; the
     conclusion stands. The fine count is the board's reading here as in V4.]
  V12 (item 343, the residue pass before finalization, 314; deduced, and computed where marked) What carries beyond the
     arrival's model, and what the row rests on. (a) V2-V4, V9 and V11 compute in one model: the README's energy
     arriving as radial null dust, spherically symmetric about the hole in the five-dimensional bulk. The README is
     written on our plane (write_small S3's H-README-ON-PLANE, the count V5 carries), so in the bulk its source is
     confined to the plane -- symmetric about the hole within the plane and by reflection across it, not over the whole
     3-sphere -- and is a gas of the plane's fields, not null dust: the two entries describe one README two ways. (b)
     What carries without the model: the one E (V1) -- the hole's energy after the arrival is the README's by energy
     conservation for any carrier, its end state C2's localized hole, Tangherlini at r_h << ell (C1-C3) -- and with it
     V11 (a), reading (i) against M's four statements; no partner and (Z) kept, for any carrier meeting the null
     condition, which pointwise proves classically for matter of particles, scalar fields and gauge fields (320, with
     339 (Q4)'s scope) -- the README's carrier is the plane's own fields; the write's floor (V5, S3's own count, already
     on the plane); V6-V8, which do not use the arrival's model; and the two arguments that use only the face's
     teleology -- a face born before the README's first part crosses hides the onset, and at 136 (1)'s exact energy the
     coarse total rises and falls whenever the face forms ahead of the matter (V4). (c) What is the model's own: the
     thresholds' values -- 4.79 clocks, and 4.83, 5.75, 5.28 and 4.82 for the coarse count (computed, pinned by the
     check); the onset orders and lambda <= 1/27, radial null dust's shell focusing, which a gas with pressure or a
     non-radial flow need not share; the trapping horizon's e^(3/2) N, a spherical apparent horizon; and V11's 5.39
     clocks. Their scale -- a few of the hole's clocks r_h/c against the write's 66,980 -- is what the row uses (V11
     (b), with 162 and 163); a plane-confined arrival is not computed (does not claim). (d) Wording: V2's "before the
     README's first part arrives" means before it crosses the face (v = 0), the face then holding (|v_born|/2)^3 N. (e)
     The row rests on M's 94, 109, 136 (1), (2), (5), (6), G and H, 158 (2), 162, 163, 198, 239, 240, 284, 285, 336 and
     340, with 110, 111 (a), 273 and 334; on the verified C1-C3 (the hole), C5 (hold_small L1, L5), O1c (337), B5a (339)
     and C8 (341, c_junction J1); on write_small S1 and S3, close_small K1 and K4, copy_p2 C1 and C2, p2_matter X2 and
     X3, bulk5_index's five-dimensional couplings and pointwise; on the board's H-BITS-WITH-ENERGY, H-BITS-ARE-STATES
     and H-FREE-GAS; and on the board's readings -- the fine count of 136 (5), 240 (b) governing the faces' radii, and
     340's compact arrival.
     [Item 348 (Q2, Q5, Q7), the verifier: (b) overstates. V8 (1) and (3) do use the model's 4.79 clocks (V8's item-348
     note); and "the one E by energy conservation for any carrier" holds only for a lossless collapse, nothing radiated
     or ejected -- radial dust meets that, a plane-confined gas, not SO(4)-symmetric in the bulk, need not. Correct: the
     contrast with reading (i)'s 2E carries for any carrier; the exact equality of the hole's E with the README's
     carries for a lossless collapse. (c): the row uses the model's scale also against J1's period, a margin of 6.9, not
     only against the write's 66,980. (e), completed again: the row rests also on the board's readings 270 (a) (the one
     object's faces at U = 0), 273 (a) (the Kruskal isometry: V6's one-r_h reading and V8 (2)) and 336 (a) (V8 (5)); on
     320 (b)-(c), V1-V5 an empty bulk apart from the README, the board's limit; and on c_junction J1's use of
     m1p2x_fifth F1 as outflow (304, outside). 158 (2) is consonant, not rested on, since 336 (V4's item-348 note).]
  V13 (item 344; computed where marked; deduced) What the accounting before the hand-off found bearing (330,
     verify_ledger): earlier corrections that bear on ARRIVAL and were not yet written here -- ten of the ledger's rows,
     in five findings, (1)-(5) -- and M's 344, (6). (1) The floor is the write's least time (267 (Q6)): 66,980 clocks is
     the least the approach takes, so a compact arrival's span is at most 8.0e-5 of the write (V11), and V10's "the
     write's 66,980 clocks are the approach" means at least that long. (2) Position 2's face open at most 33.6 of its
     clocks (V8 (3); c_junction J1) is 33.47 and 33.83 under the 2 : 1 bulk's G5 readings with sigma = 3 c^4/(4 pi G5
     ell), and 33.06 and 34.53 with sigma fixed (319 (Q2), 341 (Q4); c8_level V10) -- each at least 6.9 times the
     compact width 4.79 (computed) -- and position 2's clock r_h2/c is no shorter than ours at any destination under 240
     (b), r_h2/r_h = (G5_2/G5)^(1/3) >= 1 (V6, computed): V8 (3)'s comparison stands on every reading the record
     carries. The floor and the thresholds carry no G5: the floor is (3/2)(5 N ln2/Z)^(1/3) - 1 clocks, its only symbols
     N and Z (write_small S3, computed), and V2-V4 run in units of r_h. (3) V1-V4 are a two-derivative, flat-order
     computation: the bulk's law Einstein's, the Gauss-Bonnet coupling zero under M-ONE-LIGHT-CONE (328; 332 (Q1)), the
     results exact at that order (337 (Q4)); the warp enters at O(r_h/ell) = 8.0e-16 (computed), first order and not its
     square (317 (Q8)). (4) 211's audit in V9 ran on each question's canonical coding, as O1c's Z7 did (337, outside);
     run here under all 96 codings of each of the four questions -- every ordering of K's four values with each flip of
     t and m, 384 indexes -- none is flagged (computed). (5) V12 (e)'s rests-on, completed -- 341 (Q2)'s finding for C8
     holds here too: V6's destinations' own G5 rest on M-P2-OWN-VALUES (226) and M-P2-OWN-G (330), and V1-V4 on 328, as
     in (3). (6) The README's process on our plane -- its source a gas of the plane's fields confined to the plane (V12
     (a)) -- is a row of the warp travel theorem's map, SOURCE, worked after the current board is cleared, the completed
     theorem saying what it requires (344, M-SOURCE-IN-THE-MAP); nothing in V0-V12 rests on it (V12 (b)-(c)).
     [Item 348 (Q4, Q5, Q6): (4)'s audit is clean, and V9's counts depend on the protocol (V9's item-348 note); (5) is
     completed in V12's item-348 note; (3)'s r_h/ell = 8.0e-16, like the does-not list's R/ell = 5.4e-11, is at G5 = G
     ell -- 9.18e-16 and 6.37e-16 under the G5 readings, R/ell 6.15e-11 and 4.26e-11 (V14 (d)). Item 346
     (M-SOURCE-BY-END): (6)'s SOURCE is now two rows, and the model ARRIVALs uses stands in for SOURCEs, the small
     end's.]
  V14 (item 348; computed) The verifier's points, computed here. (a) Q1: at orders 3 and 4, with the face born at the
     onset (w = 8, 16 and 64 clocks), a ray leaving the face at v = w by 1e-6 r_h escapes (r above 150 r_h by v = w +
     400), and traced back it reaches r < 1e-6 r_h near the onset with r^2/mu within 1% of 1 and K = 72 mu^2/r^8 above
     1e25: the onset shows itself to our exterior. (b) Q4: V9's questions under both protocols -- statistics alone
     seeing every condition, 96/96 as V9 states; every language seeing every condition, 1 in 60/96 and refused in 36,
     the spread's f2 at order 2 "both" 36, refused 36, 1 in 24. (c) Q6: J1, ln(1 + (pi/10) (ell_2/r_h2)), at each
     destination's own face -- its own ell_2 = ell 2^(-(g+s)/2) (bulk5_index), its face r_h2 = r_h (G5_2/G5)^(1/3) under
     240 (b) (V6), at G5 = G ell and under both G5 readings in both conventions for sigma (c8_level V10): 32.60-34.53 of
     position 2's clocks, at least 6.91 times the compact width in ours. (d) r_h/ell and R/ell under the G5 readings,
     r_h moving as g^(1/3): 9.18e-16 and 6.37e-16, 6.15e-11 and 4.26e-11.

What this does not claim.
  - That a carrier of the README's states can converge compactly: V5's choreography is allowed by causality, its state
    count is not computed.
  - The arrival beyond spherical symmetry and radial null dust, or in the bulk away from r_h << ell: the hole is
    Tangherlini at the small end (C1-C3), R/ell = 5.4e-11 at the write's start (write_small S3).
  - [Item 343] A plane-confined arrival -- the README's actual source, a gas on our plane: V12 names what carries
    without it and what is the radial model's own.  [Item 344: now a row of the warp travel theorem's map, SOURCE,
    worked after the current board is cleared (V13 (6)).]
  - Which count of the second law governs: V4 computes both; the fine count is the board's reading of 136 (5).
  - The mechanism by which bits become matter (V8 (4)-(8)): M's statements, named.
  - The large end: there the record's ARRIVAL stands (arrival_cypher, README-HELD.md).

Imports close_small.py, write_small.py, bulk5_index.py, p2_matter.py, c4_residue.py and index_audit.py by path.
Stdlib + sympy.  python3 arrival_small.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys
from collections import Counter
from math import comb

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("My guess would be 1.", "The corridor is a single channel that grows in size to accommodate the size of the "
         "README", "It is and always will be only the size that is needed to hold the object once and at once",
         "All together, one whole", "A horizon cannot exist without the object of which it needs to exist",
         "released at position two at the closing of the horizon, which activates the higgs field forming the mass "
         "defined in the README", "the bits are absorbed by position 2, and rebuild is likely instantaneous",
         "G - the README is the energy, not separate", "1 - yes",
         "the object is built from the bulk at position 2 as an exact copy under the laws and conditions of position 2",
         "It is an exact copy of the object of position 1, but it now obeys laws of position 2",
         "Exactly as long as the write needs", "I think it is B", '"Continue"', "C, but my guess is A",
         "The throat doesn't change size")
ORDERS = (1, 2, 3, 4)                        # the arrival's onset orders: s ~ x^n at the start
WIDTHS = (0.5, 1, 2, 4, 8, 16, 64, 1000)     # the arrival's width, clocks of r_h/c
_MOD = {}


def _load(name, key):
    if key in _MOD:
        return _MOD[key]
    path = os.path.join(HERE, name)
    saved = list(sys.path)
    sys.path[:0] = [HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


# ================================================================================ the arrival in five dimensions
def profile(n):
    """the smoothstep of onset order n on [0, 1]: s ~ x^n at 0 and 1 - s ~ (1 - x)^n at 1, C^(n-1)"""
    c = math.factorial(2 * n - 1) / math.factorial(n - 1) ** 2

    def s(x):
        if x <= 0:
            return 0.0
        if x >= 1:
            return 1.0
        return x ** n * sum(comb(n - 1 + k, k) * (1 - x) ** k for k in range(n))

    def ds(x):
        if x <= 0 or x >= 1:
            return 0.0
        return c * x ** (n - 1) * (1 - x) ** (n - 1)
    return s, ds


_A = [[], [1 / 5], [3 / 40, 9 / 40], [44 / 45, -56 / 15, 32 / 9],
      [19372 / 6561, -25360 / 2187, 64448 / 6561, -212 / 729],
      [9017 / 3168, -355 / 33, 46732 / 5247, 49 / 176, -5103 / 18656],
      [35 / 384, 0, 500 / 1113, 125 / 192, -2187 / 6784, 11 / 84]]
_C = [0, 1 / 5, 3 / 10, 4 / 5, 8 / 9, 1, 1]
_B5 = [35 / 384, 0, 500 / 1113, 125 / 192, -2187 / 6784, 11 / 84, 0]
_B4 = [5179 / 57600, 0, 7571 / 16695, 393 / 640, -92097 / 339200, 187 / 2100, 1 / 40]


def dopri(f, t0, y0, t1, rtol=1e-10, atol=1e-12, hmax=None, stop=None):
    """Dormand-Prince 5(4) for a scalar y' = f(t, y), either direction; the accepted points; stops when stop(t, y)"""
    sgn = 1.0 if t1 > t0 else -1.0
    h = sgn * min(abs(t1 - t0) / 100.0, hmax or 1e9)
    t, y, out = t0, y0, [(t0, y0)]
    while sgn * (t1 - t) > 1e-15:
        if sgn * (t + h - t1) > 0:
            h = t1 - t
        k = []
        for i in range(7):
            k.append(f(t + _C[i] * h, y + h * sum(_A[i][j] * k[j] for j in range(i))))
        y5 = y + h * sum(_B5[i] * k[i] for i in range(7))
        y4 = y + h * sum(_B4[i] * k[i] for i in range(7))
        err = abs(y5 - y4) / (atol + rtol * max(abs(y), abs(y5)))
        if err <= 1.0:
            t, y = t + h, y5
            out.append((t, y))
            if stop and stop(t, y):
                break
        h *= min(5.0, max(0.2, 0.9 * (1.0 / max(err, 1e-10)) ** 0.2))
        if hmax and abs(h) > hmax:
            h = sgn * hmax
    return out


_RUNS = {}


def arrival(w, n, rstop=1e-6):
    """our side's ingoing Vaidya form, mu(v) = r_h^2 s(v/w), r_h = 1, clocks of r_h/c: the face traced back from r = 1 at
    v = w.  Capacity in units of N is r^3 (C2: N ~ r_h^3); the bits in, if they come with the energy, mu(v) (E ~ mu)."""
    key = (w, n, rstop, bool(MUT.get("capacity_linear")), bool(MUT.get("eh_is_trapping")))
    if key in _RUNS:
        return _RUNS[key]
    s, ds = profile(n)
    mu = lambda v: s(v / w)
    f = lambda v, r: 0.5 * (1.0 - mu(v) / max(r, 1e-9) ** 2)
    pts = dopri(f, w, 1.0, -30.0, hmax=max(w, 1.0) / 200.0, stop=lambda v, r: r < rstop)[::-1]
    if MUT.get("eh_is_trapping"):                                  # the mutant: the trapping horizon taken for the face
        pts = [(v, math.sqrt(mu(v))) for v, _ in pts]
    cap = (lambda r: r) if MUT.get("capacity_linear") else (lambda r: r ** 3)   # the mutant: the 4D-like linear count
    v0, r0 = pts[0]
    born = v0 - 2 * r0 if (mu(v0) == 0.0 and r0 < 1e-3) else None  # born in the flat region before the onset
    gap = min((cap(r) - mu(v), v) for v, r in pts if v >= 0)       # S_gen(v) - S_gen(start), in N (the coarse count)
    slope = min(3 * r * r * f(v, r) - ds(v / w) / w for v, r in pts)  # d S_gen / dv, in N per clock
    area_ok = all(pts[i + 1][1] >= pts[i][1] - 1e-12 for i in range(len(pts) - 1))
    out = dict(born=born, gap=gap[0], gap_v=gap[1], slope=slope, area_ok=area_ok)
    _RUNS[key] = out
    return out


def _bisect(pred, lo, hi, it=26):
    for _ in range(it):
        m = 0.5 * (lo + hi)
        if pred(m):
            lo = m
        else:
            hi = m
    return lo


def v1():
    """the flux, the one E, and the curvature"""
    CS = _load("close_small.py", "arr_cs")
    va = CS.vaidya(5, "in")
    v, r = sp.symbols("v r")
    mu = sp.Function("mu")
    flux = sp.simplify(va["G00"] - 3 * sp.diff(mu(v), v) / (2 * r ** 3)) == 0 and va["others_zero"]
    # the Kretschmann scalar of the five-dimensional ingoing form, mu' entering nowhere
    th, ph, ps = sp.symbols("theta phi psi")
    X = [v, r, th, ph, ps]
    g = va["g"]
    gi = g.inv()
    nn = 5
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(nn)) / 2) for c in range(nn)] for b in range(nn)] for a in range(nn)]
    R = {}
    for a in range(nn):
        for b in range(nn):
            for c in range(nn):
                for d in range(c + 1, nn):
                    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                    e += sum(Gam[a][c][kk] * Gam[kk][b][d] - Gam[a][d][kk] * Gam[kk][b][c] for kk in range(nn))
                    e = sp.simplify(e)
                    if e != 0:
                        R[(a, b, c, d)], R[(a, b, d, c)] = e, -e
    K = 0
    for a, b, c, d in itertools.product(range(nn), repeat=4):      # R_abcd R^abcd over every index, not only R^a_bcd's
        low = sum(g[a, e] * R.get((e, b, c, d), 0) for e in range(nn))
        if low == 0:
            continue
        up = sum(gi[b, f_] * gi[c, hh] * gi[d, kk] * R.get((a, f_, hh, kk), 0)
                 for f_ in range(nn) for hh in range(nn) for kk in range(nn))
        K += low * up
    K = sp.simplify(K)
    kret = sp.simplify(K - 72 * mu(v) ** 2 / r ** 8) == 0
    # one E against two: the Misner-Sharp mass after the arrival, the README's E alone (reading (ii)) or a face of E
    # standing through the write and the README's E besides (reading (i), write_small S4's verifier, 264)
    E_i = 1 if MUT.get("standing_one_E") else 2                    # the mutant: reading (i) counted with one E
    mu_i = sp.Integer(E_i)                                         # mu ~ E (K4's -3 pi mu0/(8 G5) = -E)
    return dict(flux=flux, kretschmann=kret, E_ii=1, E_i=E_i, rh_i=sp.sqrt(mu_i), cap_i=mu_i ** sp.Rational(3, 2))


def v2():
    """the face as the README arrives: born before the onset, and the second law's weak form, by width and order"""
    grid = {(n, w): arrival(w, n) for n in ORDERS for w in WIDTHS}
    gsl = {n: _bisect(lambda w, n=n: arrival(w, n)["gap"] > -1e-9, 1.0, 20.0) for n in ORDERS}
    born = {n: _bisect(lambda w, n=n: (lambda a: a["born"] is not None and a["born"] < -1e-7)(arrival(w, n)), 1.0,
                       20.0) for n in (3, 4)}
    # the trapping horizon holds e^(3/2) N at a fraction e of E: the README only whole (README-HELD 3, here in 5D)
    e = sp.Symbol("e", positive=True)
    cap_ah = (e ** sp.Rational(1, 1)) if MUT.get("capacity_linear") else e ** sp.Rational(3, 2)
    whole = sp.simplify(cap_ah / e) == sp.sqrt(e)
    return dict(grid=grid, gsl=gsl, born=born, whole=whole)


def v3():
    """the centre at the onset, for null dust: which onsets an escaping ray sees"""
    x, lam, w, c, vv = sp.symbols("x lambda w c v", positive=True)
    if MUT.get("onset_4d"):                                        # the mutant: the four-dimensional criterion
        poly = 2 * x ** 2 - x + 2 * lam
    else:
        poly = 2 * x ** 3 - x ** 2 + lam                           # r = x v in dr/dv = (1 - lambda v^2/r^2)/2
    xs = sp.solve(sp.diff(poly - lam, x), x)
    lam_c = max(sp.simplify(-(poly - lam).subs(x, xx)) for xx in xs if xx > 0)
    w_c = sp.solve(sp.Eq(3 / w ** 2, lam_c), w)[0]                 # the order-2 smoothstep s = 3 x^2 - 2 x^3
    rpow = 6 if MUT.get("kretsch_r6") else 8                       # the mutant: four-dimensional r^-6
    expo = {}
    for n in (3, 4):
        K = 72 * (c * vv ** n) ** 2 / (vv / 2) ** rpow             # along the escaping ray r ~ v/2
        expo[n] = sp.degree(sp.simplify(K * vv ** rpow), vv) - rpow
    return dict(lam_c=lam_c, w_c=w_c, expo=expo)


def v4():
    """the second law: the carrier's entropy at fixed energy, the spread limit, the two counts"""
    a, V, E = sp.symbols("a V E", positive=True)
    T = (E / (a * V)) ** sp.Rational(1, 4)                         # E = a V T^4, a free massless gas in d = 3
    S = sp.simplify(sp.Rational(4, 3) * a * V * T ** 3)
    v_exp = sp.simplify(V * sp.diff(S, V) / S)
    e = sp.Symbol("e", positive=True)
    dip = sp.minimum(e ** sp.Rational(3, 2) - e, e, sp.Interval(0, 1))
    arg = sp.solve(sp.diff(e ** sp.Rational(3, 2) - e, e), e)
    WS = _load("write_small.py", "arr_ws")
    floor = WS.head_clocks()
    return dict(v_exp=v_exp, dip=dip, dip_at=arg, floor=floor)


def v6():
    """position 2's release at the small end, for the twelve destinations, under the two readings"""
    B5 = _load("bulk5_index.py", "arr_b5")
    out = {}
    for n, d in B5.five_d().items():
        eg5, eg = d["e"]["G5"], d["e"]["G"]
        m_exp = -eg / 2 if MUT.get("release_4d") else -eg5 / 3   # the mutant: the large end's exponent
        out[n] = dict(law=d["law"], eG5=eg5, E_M=2.0 ** float(m_exp), r_M=2.0 ** float(eg5 / 3),
                      E_G=2.0 ** float(-eg5), cap_G=2.0 ** float(-eg5), E_large=2.0 ** float(-eg / 2))
    return out


def v7():
    """the room: the copy's volume per element under each law, (a0_law / a0_ours)^3, and per destination"""
    PM = _load("p2_matter.py", "arr_pm")
    sol = PM.SOL_FIX
    ratio = {}
    for (el, law), row in sol.items():
        r_ = row[0] / sol[(el, "ours")][0]
        ratio[(el, law)] = r_ ** -3 if MUT.get("room_inverted") else r_ ** 3
    dest = {n: {el: ratio[(el, d["law"])] for el in ("Cu", "Ag", "Au", "Cr")} for n, d in v6().items()}
    return dict(ratio=ratio, dest=dest)


def onset_hidden(n, w, o2, o3):
    """the onset behind the face or regular (V2-V3; item 348 (Q1)): born before the onset at any order; at order 1 no
    ray leaves the onset; at order 2 regular below w = 9; at orders 3 and 4, born at the onset, the escaping rays leave
    it along the trapping horizon, where K = 72/mu^2 diverges -- shown (the item-348 correction of n = 4)"""
    if o2["grid"][(n, w)]["born"] is not None or n == 1:
        return True
    if n == 2:
        return w < float(o3["w_c"])
    if MUT.get("onset4_ok"):                                       # the mutant: the record's order-4 reading restored
        return bool(o3["expo"][n] >= 0)
    return False


def populations():
    """the clauses per class from the runs: t, the arrival compact (within the thresholds) or spread; m, the README or
    other.  f1: forms our face with no partner, (Z) kept, its own one E.  f2: the onset behind the face or regular."""
    o2, o3 = v2(), v3()
    comp = [w for w in WIDTHS if w <= min(list(o2["gsl"].values()) + list(o2["born"].values()))]
    spread = [w for w in WIDTHS if w > max(o2["gsl"].values())]
    onset_ok = lambda n, w: onset_hidden(n, w, o2, o3)
    f2_c = {int(onset_ok(n, w)) for n in ORDERS for w in comp}
    f2_s = {int(onset_ok(n, w)) for n in ORDERS for w in spread}
    if MUT.get("readme_spread_ok"):
        f2_s = {1}
    # the classes' other members: no arrival (no face: f1 0, f2 vacuous 1); a README on a standing face (reading (i):
    # no formation, two E: f1 0); the README with 183's exact partner (no face forms, README-HELD 2: f1 0); other
    # matter arriving alone (it forms its own face with its own E: f1 1, f2 as the README's of the same profile)
    F1 = {(1, 1): {1}, (0, 1): {1}, (1, 0): {0, 1}, (0, 0): {0, 1}}
    F2 = {(1, 1): f2_c, (0, 1): f2_s, (1, 0): f2_c | {1}, (0, 0): f2_s | {1}}
    return dict(f1=F1, f2=F2, compact=comp, spread=spread)


_V9 = {}


def v9():
    """ARRIVAL's question through the calculator, clause by clause in the form C4's stands in (291)"""
    key = bool(MUT.get("readme_spread_ok"))
    if key in _V9:
        return _V9[key]
    CR = _load("c4_residue.py", "arr_cr")
    IA = _load("index_audit.py", "arr_ia")
    P = populations()
    res = {}
    for name in ("f1", "f2"):
        F = P[name]
        for cell in ((1, 1), (0, 1)):
            out = {k: sum((CR._ask_one(("f",), F, k, tf=tf, mf=mf, c4row=cell)
                           for tf, mf in itertools.product((0, 1), repeat=2)), Counter()) for k in (2, 3)}
            kn = CR._cells("f", dict(zip(CR.NAMES4, range(4))), F, ("quantum",) + cell, CR.A4, CR.CD4)
            au = IA.audit_index(["K", "t", "m", "f"], kn)
            res[(name, cell)] = dict(F=F, out=out, flagged=bool(au["keys"] or au["onehot"]))
    _V9[key] = res
    return res


def v11():
    """item 340: for the math -- within reading (ii), how long a compact arrival changes the face's size"""
    o2 = v2()
    wstar = min(list(o2["gsl"].values()) + list(o2["born"].values()))
    if MUT.get("spread_counted_compact"):                         # the mutant: a spread arrival taken for compact
        wstar = 1000.0
    span = {}
    for n in ORDERS:
        b = arrival(wstar, n)["born"]
        span[n] = wstar - (b if b is not None else 0.0)
    floor = v4()["floor"]
    return dict(wstar=wstar, span=span, frac=max(span.values()) / floor)


def v13():
    """item 344: what the accounting before the hand-off found bearing (330) -- J1's open period under the G5
    readings against the compact width, position 2's clock under 240 (b), the floor's symbols, the warp's order, and
    211's audit under every coding"""
    WS = _load("write_small.py", "arr_ws")
    sec = WS.seconds()
    row = sec["rows"][sec["ell_max"]]
    rh_ell = row["rh"] / row["ell"]
    per = {}
    for g in (1.5, 0.5):
        r = rh_ell if MUT.get("g5_dropped") else rh_ell * g ** (1 / 3)   # the mutant: the G5 readings not carried
        fixed = r if MUT.get("g5_dropped") else r * g
        per[(g, "sigma fixed")] = math.log(1 + (math.pi / 10) / fixed)
        per[(g, "sigma by G5")] = math.log(1 + (math.pi / 10) / r)
    CR = _load("c4_residue.py", "arr_cr")
    IA = _load("index_audit.py", "arr_ia")
    Q = v9()                                                         # V9's own questions, their populations as asked
    asked = flagged = 0
    codings = [(0, 0)] if MUT.get("audit_one_coding") else list(itertools.product((0, 1), repeat=2))
    for name in ("f1", "f2"):
        for cell in ((1, 1), (0, 1)):
            for tf, mf in codings:
                Ff = {(t ^ tf, m ^ mf): v for (t, m), v in Q[(name, cell)]["F"].items()}
                for perm in itertools.permutations(range(4)):
                    kn = CR._cells("f", dict(zip(CR.NAMES4, perm)), Ff, ("quantum", cell[0] ^ tf, cell[1] ^ mf),
                                   CR.A4, CR.CD4)
                    au = IA.audit_index(["K", "t", "m", "f"], kn)
                    asked += 1
                    flagged += bool(au["keys"] or au["onehot"])
    return dict(per=per, per0=math.log(1 + (math.pi / 10) / rh_ell), wstar=v11()["wstar"], warp=rh_ell,
                clock2={n: r["r_M"] for n, r in v6().items()},
                floor_syms=sorted(str(x) for x in WS.s3()["t3"].free_symbols), asked=asked, flagged=flagged)


_V14 = {}


def v14():
    """item 348: the verifier's points computed here -- (a) the onset's escaping rays at orders 3 and 4, (b) V9 under
    both protocols, (c) J1 at each destination's own face, (d) the G5 readings of r_h/ell and R/ell"""
    key = (bool(MUT.get("onset4_ok")), bool(MUT.get("stat_only")))
    if key in _V14:
        return _V14[key]
    rays = {}
    for n in (3, 4):
        for w in (8.0, 16.0, 64.0):
            s_, _ = profile(n)
            mu = lambda v, s_=s_, w=w: s_(v / w)
            f = lambda v, r, mu=mu: 0.5 * (1.0 - mu(v) / max(r, 1e-12) ** 2)
            fwd = dopri(f, w, 1.0 + 1e-6, w + 400.0, hmax=1.0)
            back = dopri(f, w, 1.0 + 1e-6, 1e-12, hmax=w / 2000.0, rtol=1e-12, atol=1e-15, stop=lambda v, r: r < 1e-6)
            vb, rb = back[-1]
            rays[(n, w)] = dict(escape=fwd[-1][1], r_end=rb, ratio=rb * rb / mu(vb), K=72 * mu(vb) ** 2 / rb ** 8,
                                hidden=onset_hidden(n, w, v2(), v3()) if w in WIDTHS else None)
    CR = _load("c4_residue.py", "arr_cr")
    P = populations()
    vk = "stat" if MUT.get("stat_only") else "all"               # the mutant: every-language counts not taken
    counts = {}
    for name in ("f1", "f2"):
        for cell in ((1, 1), (0, 1)):
            counts[(name, cell)] = {k: sum((CR._ask_one(("f",), P[name], k, views_kind=vk, tf=tf, mf=mf, c4row=cell)
                                            for tf, mf in itertools.product((0, 1), repeat=2)), Counter())
                                    for k in (2, 3)}
    WS = _load("write_small.py", "arr_ws")
    sec = WS.seconds()
    row = sec["rows"][sec["ell_max"]]
    rh_ell = row["rh"] / row["ell"]
    B5 = _load("bulk5_index.py", "arr_b5")
    per = []
    for n, d in B5.five_d().items():
        l2, r2 = 2.0 ** (float(d["e"]["ell2"]) / 2), 2.0 ** (float(d["e"]["G5"]) / 3)
        for g in (1.0, 1.5, 0.5):
            r = rh_ell * r2 / l2 * g ** (1 / 3)
            for fixed in (r, r * g):
                p_ = math.log(1 + (math.pi / 10) / fixed)
                per.append((p_, p_ * r2))
    wstar = v11()["wstar"]
    R_ell = WS.compute()["ex"]["R_over_ell"]
    out = dict(rays=rays, counts=counts, per2=(min(p for p, _ in per), max(p for p, _ in per)),
               ratio=min(q for _, q in per) / wstar, g5=[rh_ell * g ** (1 / 3) for g in (1.5, 0.5)],
               R_ell=[R_ell * g ** (1 / 3) for g in (1.5, 0.5)])
    _V14[key] = out
    return out


def compute():
    return dict(v1=v1(), v2=v2(), v3=v3(), v4=v4(), v6=v6(), v7=v7(), v9=v9(), v11=v11(), v13=v13(), v14=v14())


def report(o):
    print("arrival_small.py -- the ARRIVAL row at the small end, one-way (item 338)\n")
    a = o["v1"]
    print("V1 G_vv = 3 mu'/(2 r^3) only: %s; K = 72 mu^2/r^8: %s; reading (ii) E %s; reading (i) E %s, face r_h x %s, "
          "capacity %s N" % (a["flux"], a["kretschmann"], a["E_ii"], a["E_i"], a["rh_i"], a["cap_i"]))
    b = o["v2"]
    print("V2 the face as the README arrives (born: clocks before the onset; gap: S_gen - start in N, coarse count):")
    for n in ORDERS:
        print("   n = %d: %s" % (n, "; ".join("w %g born %s gap %+.4f" % (
            w, "%.3f" % b["grid"][(n, w)]["born"] if b["grid"][(n, w)]["born"] is not None else "--",
            b["grid"][(n, w)]["gap"]) for w in WIDTHS)))
    print("   weak form held up to w = %s; born before the onset up to w = %s (n = 2: the onset's limit, V3); the "
          "trapping horizon holds e^(3/2) N: %s" % ({n: round(x, 4) for n, x in b["gsl"].items()},
                                                   {n: round(x, 4) for n, x in b["born"].items()}, b["whole"]))
    print("   d S_gen/dv < 0 somewhere in every run: %s; the area never falls in any run: %s" % (
        all(r["slope"] < 0 for r in b["grid"].values()), all(r["area_ok"] for r in b["grid"].values())))
    c = o["v3"]
    print("V3 self-similar onset naked iff lambda <= %s; the order-2 smoothstep's w_c = %s; K along the escaping ray "
          "as v^%s (n = 3), v^%s (n = 4)" % (c["lam_c"], c["w_c"], c["expo"][3], c["expo"][4]))
    d = o["v4"]
    print("V4 the gas's S ~ V^%s at fixed E; the spread limit's dip %s N at e = %s; the write's floor %.0f clocks" % (
        d["v_exp"], d["dip"], d["dip_at"], d["floor"]))
    print("V6 position 2's release at the small end (E2/E under 240 (b), its radius; under one r_h, E2/E = capacity; "
          "the large end's):")
    for n, r in o["v6"].items():
        print("   %-13s %-6s G5 x 2^%-4s E2/E %.4f r %.4f | %.4f | large %.4f" % (
            n, r["law"], r["eG5"], r["E_M"], r["r_M"], r["E_G"], r["E_large"]))
    print("V7 the room (a0_law/a0_ours)^3: %s" % {k: round(v, 4) for k, v in o["v7"]["ratio"].items() if k[1] != "ours"})
    for (name, cell), r in o["v9"].items():
        print("V9 %s at %s: population %s; order 2 %s, order 3 %s; audit flagged %s" % (
            name, cell, r["F"], dict(r["out"][2]), dict(r["out"][3]), r["flagged"]))
    q = o["v11"]
    print("V11 (item 340) the compact arrival's width %.4f clocks changes the face's size over %s clocks, %.2g of the "
          "write" % (q["wstar"], {n: round(x, 3) for n, x in q["span"].items()}, q["frac"]))
    u = o["v13"]
    print("V13 (item 344) J1's open period %.2f clocks; under the G5 readings %s, at least %.2f times the compact "
          "width; position 2's clock over ours >= %.4f; the floor's symbols %s; r_h/ell %.2g; the audit flagged %d of "
          "%d codings" % (u["per0"], {k: round(v, 2) for k, v in u["per"].items()}, min(u["per"].values()) / u["wstar"],
                       min(u["clock2"].values()), u["floor_syms"], u["warp"], u["flagged"], u["asked"]))
    x = o["v14"]
    print("V14 (item 348) escaping rays (n, w): %s; V9 with every language: %s; J1 at each destination's face %.2f-%.2f "
          "position-2 clocks, %.2f w*; G5 readings r_h/ell %s, R/ell %s" % (
              {k: (round(r["escape"]), "%.4f" % r["ratio"], "%.2g" % r["K"]) for k, r in x["rays"].items()},
              {"%s %s" % k: {o_: dict(c) for o_, c in v.items()} for k, v in x["counts"].items()}, x["per2"][0],
              x["per2"][1], x["ratio"], ["%.3g" % v for v in x["g5"]], ["%.3g" % v for v in x["R_ell"]]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("V0 198, 94, 162, 163, 109, 136 (2), (6), G and (1), 240, 285, 158 (2), 336 and 338 verbatim in the rulings "
        "file",
        all(" ".join(w.split()) in rul for w in WORDS))
    a = o["v1"]
    add("V1 our side's only Einstein component G_vv = 3 mu'/(2 r^3), non-negative iff mu' >= 0; K = 72 mu^2/r^8; "
        "reading (ii) one E, reading (i) two -- a face of 2^(1/2) r_h holding 2^(3/2) N",
        a["flux"] and a["kretschmann"] and a["E_i"] == 2 and a["rh_i"] == sp.sqrt(2)
        and a["cap_i"] == 2 * sp.sqrt(2))
    b = o["v2"]
    g = b["grid"]
    ok = all(g[(n, w)]["born"] is not None and g[(n, w)]["born"] < 0 and g[(n, w)]["gap"] > -1e-9
             for n in ORDERS for w in WIDTHS if w <= 4)
    ok &= all(g[(n, w)]["gap"] < -1e-3 for n in ORDERS for w in WIDTHS if w >= 8)
    ok &= all(4.7 < b["gsl"][n] < 5.8 for n in ORDERS) and all(4.7 < b["born"][n] < 5.4 for n in (3, 4))
    ok &= b["whole"] and abs(g[(1, 1000)]["gap"] + 4 / 27) < 2e-3
    add("V2 an arrival within 4 clocks: the face born before the onset and the generalized entropy never below its "
        "start, at every order; from 8 clocks it falls below, toward -4/27 N; the thresholds 4.8-5.8 clocks; the "
        "trapping horizon holds e^(3/2) N, the README only whole", ok)
    add("V4 (the two counts) d S_gen/dv < 0 somewhere in every run (the face's teleology at exact saturation); the area "
        "never falls in any run (the fine count's law)",
        all(r["slope"] < 0 for r in g.values()) and all(r["area_ok"] for r in g.values()))
    c = o["v3"]
    add("V3 the onset: self-similar null dust naked iff lambda <= 1/27, the order-2 smoothstep from w = 9; K along the "
        "escaping ray as v^-2 at order 3, bounded at order 4",
        c["lam_c"] == sp.Rational(1, 27) and c["w_c"] == 9 and c["expo"][3] == -2 and c["expo"][4] == 0)
    d = o["v4"]
    add("V4 the free gas's entropy at fixed E grows as V^(1/4); the spread limit's dip -4/27 N at e = 4/9; the write's "
        "floor 66,980 clocks (write_small S3)",
        d["v_exp"] == sp.Rational(1, 4) and d["dip"] == -sp.Rational(4, 27) and d["dip_at"] == [sp.Rational(4, 9)]
        and round(d["floor"]) == 66980)
    e6 = o["v6"]
    ok = abs(e6["2b"]["E_M"] - 2 ** (-1 / 6)) < 1e-12 and abs(e6["2P"]["E_M"] - 2 ** -0.5) < 1e-12
    ok &= abs(e6["2b+2P"]["E_M"] - 2 ** (-2 / 3)) < 1e-12 and abs(e6["2b+2P"]["E_large"] - 0.5) < 1e-12
    ok &= all((abs(r["E_M"] - 1) < 1e-12) == (r["eG5"] == 0) for r in e6.values())
    ok &= all((abs(r["cap_G"] - 1) < 1e-12) == (r["eG5"] == 0) and r["cap_G"] <= 1 for r in e6.values())
    add("V6 position 2's release at the small end: E2/E = (G5/G5_2)^(1/3) under 240 (b) -- 1, 0.891, 0.707, 0.630 -- "
        "against the large end's (G/G2)^(1/2); one r_h and 240 (b) agree only where G5_2 = G5", ok)
    rt = o["v7"]["ratio"]
    want = {("Cu", "min"): 0.9387, ("Cu", "mirror"): 0.8837, ("Ag", "min"): 0.8127, ("Ag", "mirror"): 0.7106,
            ("Au", "min"): 0.9898, ("Au", "mirror"): 0.9677, ("Cr", "min"): 1.0469, ("Cr", "mirror"): 1.0627}
    add("V7 the room from p2_matter's banked solids: 285 (b)'s eight figures, Cu 0.9387 / 0.8837 to Cr 1.0469 / 1.0627; "
        "every destination of our matter law 1",
        all(abs(rt[k] - v) < 6e-5 for k, v in want.items())
        and all(abs(x - 1) < 1e-12 for n, dd in o["v7"]["dest"].items() for x in dd.values()
                if o["v6"][n]["law"] == "ours"))
    z = o["v9"]
    ones = Counter({(1,): 96})
    ok = all(z[("f1", c_)]["out"][k] == ones for c_ in ((1, 1), (0, 1)) for k in (2, 3))
    ok &= all(z[("f2", (1, 1))]["out"][k] == ones for k in (2, 3))
    ok &= z[("f2", (0, 1))]["F"][(0, 1)] == {0, 1} and z[("f2", (0, 1))]["out"][2] == Counter({("both",): 96})
    ok &= not any(r["flagged"] for r in z.values())
    add("V9 the calculator: f1 (forms, no partner, (Z), its own E) 1 at orders 2 and 3 for the README compact or "
        "spread; f2 (the onset behind the face or regular) 1 for the compact README, and for the spread \"both\" at "
        "order 2, its population {0, 1} computed; audits clean", ok)
    b2 = o["v2"]
    add("V12 (item 343) the radial model's figures as quoted: the coarse count kept to 4.83, 5.75, 5.28, 4.82 clocks at "
        "orders 1-4, the face born before the onset to 5.27 and 4.79 at orders 3-4, the least 4.79",
        [round(b2["gsl"][n], 2) for n in ORDERS] == [4.83, 5.75, 5.28, 4.82]
        and [round(b2["born"][n], 2) for n in (3, 4)] == [5.27, 4.79]
        and round(min(list(b2["gsl"].values()) + list(b2["born"].values())), 2) == 4.79)
    q = o["v11"]
    add("V11 (item 340) for the math: a compact arrival (w = 4.79 clocks) changes the face's size over at most 5.39 "
        "clocks, 8.0e-5 of the write's 66,980 -- 162's throat that does not change size and 163's one whole",
        abs(q["wstar"] - 4.7857) < 1e-3 and 5.3 < max(q["span"].values()) < 5.45 and q["frac"] < 1e-4)
    u = o["v13"]
    pr = {k: round(v, 2) for k, v in u["per"].items()}
    add("V13 (item 344) the accounting before the hand-off: J1's 33.60 clocks, 33.06 and 34.53 with sigma fixed, 33.47 "
        "and 33.83 with sigma by G5, each at least 6.9 times the compact width; position 2's clock no shorter than ours "
        "under 240 (b); the floor's only symbols N and Z; r_h/ell = 8.0e-16; the audit clean under all 384 codings",
        round(u["per0"], 2) == 33.60 and pr == {(1.5, "sigma fixed"): 33.06, (1.5, "sigma by G5"): 33.47,
                                                 (0.5, "sigma fixed"): 34.53, (0.5, "sigma by G5"): 33.83}
        and min(u["per"].values()) / u["wstar"] >= 6.9 and min(u["clock2"].values()) >= 1 - 1e-12
        and u["floor_syms"] == ["N", "Z"] and "%.1e" % u["warp"] == "8.0e-16" and u["asked"] == 384
        and u["flagged"] == 0)
    x = o["v14"]
    c60 = Counter({(1,): 60, ("refused",): 36})
    ok = all(r["escape"] > 150 and r["r_end"] < 1e-6 and abs(r["ratio"] - 1) < 1e-2 and r["K"] > 1e25
             for r in x["rays"].values())
    ok &= all(r["hidden"] is False for r in x["rays"].values() if r["hidden"] is not None)
    ok &= all(x["counts"][(nm, c)][k] == c60 for nm, c in (("f1", (1, 1)), ("f1", (0, 1)), ("f2", (1, 1)))
              for k in (2, 3))
    ok &= x["counts"][("f2", (0, 1))][2] == Counter({("both",): 36, ("refused",): 36, (1,): 24})
    ok &= "%.2f" % x["per2"][0] == "32.60" and "%.2f" % x["per2"][1] == "34.53" and x["ratio"] >= 6.9
    ok &= ["%.3g" % v for v in x["g5"]] == ["9.18e-16", "6.37e-16"] and ["%.3g" % v for v in x["R_ell"]] == [
        "6.15e-11", "4.26e-11"]
    add("V14 (item 348) the verifier's points: at orders 3 and 4 born at the onset, rays escape from the onset along "
        "the trapping horizon, K diverging; V9 with every language 1 in 60/96, refused 36 (the spread's f2 both 36, "
        "refused 36, 1 in 24); J1 at each destination's face 32.60-34.53 position-2 clocks, at least 6.9 w*; the G5 "
        "readings of r_h/ell and R/ell", ok)
    return res


MUTANTS = {"capacity_linear": "the face's capacity linear in r (a four-dimensional-like count) (V2, V4)",
           "eh_is_trapping": "the trapping horizon taken for the face (V2)",
           "standing_one_E": "reading (i) counted with one E (V1)",
           "onset_4d": "the onset's self-similar criterion in four dimensions (V3)",
           "kretsch_r6": "the curvature along the escaping ray with r^-6 (V3)",
           "release_4d": "position 2's release with the large end's exponent (V6)",
           "room_inverted": "the copy's volume ratio inverted (V7)",
           "readme_spread_ok": "the spread README's onset counted always hidden (V9)",
           "spread_counted_compact": "a spread arrival taken for compact (V11, item 340)",
           "g5_dropped": "the G5 readings not carried into J1's open period (V13; 319 (Q2), 341 (Q4))",
           "audit_one_coding": "211's audit run on one coding of each question (V13; 337, outside)",
           "onset4_ok": "the order-4 onset counted hidden when born at the onset (V14; 348 (Q1))",
           "stat_only": "V9's counts taken under the statistics-rank protocol only (V14; 348 (Q4))"}


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
        _RUNS.clear()
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        _RUNS.clear()
        caught += bool(failed)
        print("  mutant %-17s %-70s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
