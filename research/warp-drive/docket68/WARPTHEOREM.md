# The Warp Theorem (M-RULINGS items 150, 151; one statement built from the pieces; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft counted its lemmas wrongly, read the energy
ledger's remainder from item 139 alone, and left out four lemmas. All are corrected after the reassessment's verifier
(History).

## What you said

- **Item 150:** *"The approach needs to be to stop piecing together theorems to fit my theory, instead we need to
  consider one single theorem built from the pieces that defines the warp theory as a single statement"*.
- **So the board's separate results are now lemmas of one theorem.** What is not yet proved is a named lemma of it, not
  a separate question.
- **The instrument:** `warptheorem.py`. It imports exactE.py, coin.py, passage5d.py, localbulk.py and stability.py by
  path. Selftest 8/8; the eighth check runs every lemma instrument's own selftest.
  - **Genuine checks:** six.
  - **Control:** one.
  - **Marked STRUCTURAL:** one.

## The theorem

> **For an object whose README — its one fixed exact encoding, labels and values, written in what every universe
> shares — has N bits, there is exactly one corridor, fixed by N alone, and through it the README becomes, one way and
> exactly, the object at position 2.**

The corridor is the following, clause by clause.

- **(G) Geometry.**
  - It is Bronnikov–Kim's eq. (17) at r₀ = 2m on the plane.
  - **E = √(N h c⁵ ln2 / (8π²G)) = 459,404,002.42 J × √N.**
  - **m = GE/c⁴.**
  - **r₀ = 2m = √(N h G ln2 / (2π²c³)).**
- **(H) Holding.**
  - The throat holds exactly the README: **4πr₀² = N × 2hG ln2/(πc³)**, which is 4 ln2 Planck areas per bit.
  - The horizons hold it too.
- **(O) One way.**
  - The passage runs from position 1 to position 2 through an extremal horizon, with surface gravity 0.
  - It is nonsingular and complete, never runs back, and survives its hold.
- **(Z) Null energy never violated.**
  - Along the passage, a null geodesic of the five-dimensional geometry, the null energy is zero.
  - The plane's apparent deficit is exactly the bulk's pull.
- **(B) Bulk.**
  - A vacuum five-dimensional bulk carries the corridor. The plane is free of matter, at the Randall–Sundrum tension.
  - The plane's two ends are one end of the bulk.
  - The energy is positive at every point.
  - The bulk's scale k is fixed by the work.
  - The corridor opens and closes between static planes.
- **(I) Information.** The passage is N bits of entanglement, and it carries the N-bit README within the capacity
  bound.
- **(E) Energy.**
  - One exact energy E is carried from position 1 through three holds.
  - It is released into position 2 at the closing, and the build uses exactly it, with every joule accounted for.
- **(R) Reconstruction.**
  - The corridor takes the README at its opening.
  - Position 2's matter rearranges to the README exactly, with no tolerance, by a field reaction the README triggers.
    After that, position 2's laws govern.
  - The corridor's length is set by the trajectories, the difference between the two positions.

## Its lemmas

The theorem is proved exactly when no lemma below is OPEN.

| clause | lemma | status |
|---|---|---|
| G | G1 one exact energy, at the bound: E(N) | **derived**, axioms.py: 101 answer 6, 132, 131/133, the holographic bit area |
| G | G2 E(N) computed and machine-checked | **proved**, exactE.py (seated) |
| G | G3 both holds at least size give r₀ = 2m | **proved**, exactE.py |
| H | H1 4πr₀² = N·A_bit | **proved**, exactE.py |
| H | H2 the horizons hold the README too | **derived**, axioms.py: the horizon at r = 2m sits on the throat (G3) and holds N·A_bit (H1) |
| O | O1 one way, 1 → 2, nonsingular | **proved**, plane.py P1 (seated); exactE.py |
| O | O2 extremal horizon | **proved**, stability.py S1 |
| O | **O3 the corridor survives its hold, which lasts exactly as long as the write needs (158 (2)); the corridor and the opening are the same object (160)** | **OPEN**, B4d's. The hold is the corridor through the write, ≥ 2.0×10⁵ clocks (o3_write.py); item 163 keeps that ("at once" is all together, one whole). The write's energy is settled (o3_ground.py, item 164, verified once): the held README is an exact energy state at E, and the write needs a spread of 5.2×10⁻²⁰ of E. What stays open is the bulk (B4d) |
| Z | Z1 5D null energy zero along the passage; deficit = bulk pull | **proved**, passage5d.py P2 |
| Z | Z2 the integral equals the plane's reading on both legs | **proved**, passage5d.py P3, coin.py |
| Z | Z3 null energy never violated | **derived**, axioms.py: bulk R(k,k) = 0, passage 0 (Z1), composite ≥ 0 (B5a: your 117/120, shown consistent) |
| B | B1 plane matter-free; Gauss and Codazzi met | **proved**, localbulk.py |
| B | B2 a local vacuum bulk exists, unique among analytic ones | **proved**, localbulk.py |
| B | **B3 a complete bulk exists, under closed-index criteria** | **OPEN**, equivalent to B4a–B4d |
| B | B4a the global bulk's shape: two separate positions reached through a dimension (152 (1)) are one end of the bulk; CGS Thm 3.5's deformation; topology fixed before the opening | **proved** (STRUCTURAL), given W2 inside T, b4_global.py |
| B | B4c the far boundary untrapped, uniformly in time | **reading**, b4_global.py: H-FAR-MODEL. A round T exists beyond the hold's reach only if ℓ > 2R_reach; a tipped T is untrapped at any ℓ (computed: at ℓ = 0.11m, min θ+ = +0.07, B4D-STAGE2.md). Radiation after the closing cannot trap it (Raychaudhuri, margin ~4.5), and eq. (17) holds only within the reach (causality); both derived. Open: whether the model holds deep in the bulk, where a tipped T goes |
| B | B4b the bulk regular within every admissible hold's double cone: the static bulk, forced there with eq. (17) on the plane, is regular and Padé-stable for holds below ~11.3 clocks; longer holds reach the surface above the throat where its curvature diverges (y_b = 2.49–2.50m at r = 2.15m, K ∝ (y_b − y)^−p, p ≈ 2.5–3) | **reading** (computed: exact order-60/80 series, Padé continuation, the full double cone converged; flat limit; the board's locally analytic class), b4_static.py |
| B | **B4d the opening and closing evolve regularly in five dimensions; data beyond the cone join the exterior** | **OPEN**: a nonlinear 5D problem through a write of ≥ 2.0×10⁵ clocks at fixed size (162, 163). Stage 5 (verified once): with eq. (17) on a plane, a side where the warp decays is singular within 8–16 clocks, a side where it grows is regular on the evidence. Stage 6 (verified once): every positive-tension plane has a decaying side, so ours (139, clause (B)) cannot carry eq. (17) regularly; position 2's plane can, at its own ℓ₂ = 3ℓ (138), carrying exactly 139's −1/3 with both sides growing. The live route, put to you: eq. (17) on position 2's plane |
| B | B5 positivity for the entangled pin, at every point | **derived**, b5_positive.py: null energy at every point is your 117/120, shown consistent (summed tension +λ_RS at one place, 127; a smooth wall keeping it exists); no radion, the separation held at zero (127, 141) |
| B | B6 k's ratio fixed by the work, k_R = 3k_L/4; every clause b6_k.py checks free of k's scale — **not B4**, whose depth and far boundary depend on ℓ | **proved**, b6_k.py, kderive.py K3 — narrowed twice |
| B | B6′ k's scale | **nature**, item 136 answer 8 |
| B | B7 formation: the widening of the bridge already there, consistent and safe; 5D evolution with B4d | **derived**, b7_formation.py: 100, 140, 122 (4), 101 answer 1; Maldacena–Susskind p.17 READ |
| I | I1 the passage is N bits of entanglement | **derived**, axioms.py: your 137 (1) with H1; Maldacena–Susskind p.5 and Strominger–Vafa (READ) agree |
| I | I2 the README within the capacity bound as READ | **proved**, i2_capacity.py |
| E | E1 E carried through three holds into position 2 | **derived**, axioms.py: 115 (c), 136 G, O1, 136 answer 3, 109, conservation (z3, with controls) |
| E | E2 released at position 2 at the closing | **derived**, axioms.py: 106, 109, 115 (b) |
| E | E3 the ledger closes | **derived**, ledger.py: reading (a), confirmed by you (item 155: E's remainder is position 2's expansion, part of the build) |
| E | E4 the field energy outside the neck, E/4: the bulk's Weyl field read on the plane, positive | **proved**, ledger.py; Maartens–Koyama eq. 143 |
| R | R0 the read: the corridor takes the README at its opening; N read from the object | **definition**, items 70, 101 answer 8, 115 (c), 130 (2); consistent with I2b |
| R | R1 exact reconstruction, no tolerance | **definition**, items 145, 146; consistent with R3, R5c |
| R | R2 position 2 rearranges to the README; then its laws govern | **definition**, item 148; consistent with rearrange.py, E3 |
| R | R3 exactness at the instant over the mass window | **proved**, exactcopy.py, rearrange.py |
| R | R4 the corridor's length as the trajectory difference, in bits (not a distance) | **derived**, r4_length.py: the measure confirmed by you (item 155) |
| R | R5 the build's mechanism | **derived**, r5_build.py: the mechanism yours; the trigger reading confirmed by you (item 155) |

- **The count:** 34 lemmas. **14 proved, 11 derived, 3 definitions, 2 on the board's readings, 1 a measurement, 3 OPEN**
  (O3, B3 and B4d; all three wait on B4d). warptheorem.py prints it from its list; selftest 8/8.
- **T2 (STRUCTURAL)** confirms that the theorem follows from all its lemmas, and that dropping any OPEN lemma loses it.

## The energy ledger: the one place your rulings pull against each other (T3)

- **What you ruled:**
  - E goes into position 2 (110);
  - the build uses *"that and only that which is provided by the closing"* (111 (a));
  - it is released at the closing and forms the mass the README defines (136 answer 2);
  - the README is the energy (136 G);
  - item 108's accounting: the README carries E/c², and the stock fills the rest.
- **Also yours:** matter is reorganized, not created (137); and the copy is exact, with no tolerance (146).
- **What z3 finds at the board's example README.**
  - E = 2.405878×10¹⁶ J.
  - An exact copy made of reorganized matter can itself absorb at most the assembly energy, 1.1947×10¹⁰ J.
  - So "the build uses all of E" is unsatisfiable unless the build includes something besides the copy that absorbs
    the rest. With such an absorber it is satisfiable.
  - **Control:** at N = 600 bits, E is 1.1253×10¹⁰ J, below the ceiling, and needs none.
- **The exact README is far larger than the example.**
  - Item 108's full snapshot is 1.088×10²⁹ bits. There E = 1.515×10²³ J, and E/c² is about 1.7×10⁶ kg, far above the
    body's mass.
  - At that size the tension is about seven orders of magnitude larger, and item 108's deficit accounting no longer
    applies.
- **The board's reading (a), adopted under item 149, labelled, and withdrawn if you correct it.**
  - The copy's matter is the stock's (137, 148).
  - E is absorbed as the expansion of position 2's universe that the README's absorption is:
    - 136 G: the README is the energy;
    - 136 answer 6: the bits are absorbed by position 2;
    - 139 (3): *"Absorbing of the README into position 2 is an expansion of that universe"*.
  - That expansion counts as part of the build, which keeps 111 (a).
  - Item 108's E/c² is then the appearance accounting of item 107, the definition read against the object, not added
    matter.
  - **What it keeps:** 110, 111, 136 (2) with "forming the mass" read as triggering the stock's rearrangement into it
    (110: *"the energy that triggers"*), 137, 146 and 148.
  - **What it reads differently:** item 108's literal "stock fills the deficit".
- **If you mean 108 literally instead,** E/c² becomes part of the copy's mass. Then 137 or 146 must give way for that
  part. That would be your call, not the board's.

## The work left, as the theorem's lemmas

- **Open:** B4d, the opening and closing as a five-dimensional evolution, now through a write of at least
  ~2×10⁵ clocks at the example README (lemmas/O3-WRITE.md). It carries B3, and with B4a–B4c closes formation and the
  address. O3 now waits on it too.
- **On the board's readings:** B4c (H-FAR-MODEL), B4b (the locally analytic class and Padé continuation, computed).
  Both were calibrated to the static window's ~11.3-clock reach, which the write exceeds, so both are re-read with B4d.
  B5, B7 and I1 left the list under item 154; E3, R4 and R5 when you confirmed them (item 155). O3 left it for OPEN
  under item 158 (O3-WRITE.md).
- **Caveats the board can clear:** I1's extremal step, READ for a class only; the duration quantum inequality (old wall
  D7), not yet re-run against Z3.
- **A measurement, by your ruling:** B6′, k's scale.
- **Verification:** b4_global.py, b4_regular.py, b4_static.py (with o3_hold.py's window) and o3_write.py have had
  one verifier each; the other nine lemma instruments, axioms.py and warptheorem.py have not.
- The chain map (chainmap.html, published as the Warp Chain Map) shows which station each lemma decides.

## Named hypotheses

- **Yours:** M-ONE-THEOREM (150), M-PROVE-EVERY-LEMMA (151), and the rulings each derived lemma is derived from.
- **The board's:**
  - reading your item 152 (1) as CENSOR5D's escape (a), encoded as one end (B4a);
  - H-FAR-MODEL (B4c); the locally analytic class near the hold and Padé continuation (B4b); for O3's write
    (O3-WRITE.md) H-WRITE-IS-ARRIVAL, H-FREE-GAS, H-BITS-ARE-STATES, H-SPECIES-FINITE, H-FLAT-START, H-README-ALONE,
    H-HOLD-FRAME, H-NO-SHORTCUT, and reading (i)'s H-WRITE-IN-STATIC-HOLD; H-HOLD-IN-WINDOW, refuted on reading (i);
    H-EVOLUTION and H-GLUING (B4d);
  - reading (a) for E3;
  - H-SHARED-PROFILE, H-PIN-IS-COINCIDENCE (B5); H-BRIDGE-PREEXISTS (B7);
    H-LENGTH-AS-DIFFERENCE (R4); H-EXTREMAL-ENTROPY (I1);
  - H-COMPOSITE-SURFACE, H-THICK-COMPOSITE, H-BK-CORRIDOR.

## History (from the reassessment's verifier, 2026-10-07)

- **The count was wrong.** It was "11 yours, 9 proved, 7 open"; the true count was 9, 10, 7. The instrument now prints
  the count from the list.
- **E3 read the remainder from item 139 alone, as a sink outside the build.** 139's words concern the trigger, and a
  sink outside the build runs against 111 (a). It is now reading (a), with its chain of rulings stated and the conflict
  named.
- **Four lemmas were missing:**
  - O3, the hold's length. "A few clocks" was the board's assumption, not a ruling.
  - E4, the field energy outside the neck.
  - R0, the read, from your items 70, 101 answer 8, 115 (c) and 130 (2).
  - R5, the build's mechanism.
- **Three lemmas were corrected.**
  - B5's positivity is the board's composite reading of your "entangled" (140), not "fused".
  - B4 now names separate universes, no loop and the infinitely many planes.
  - I2 now states the capacity bound as READ: information is capped by what is sent to set up the interaction (MSY
    p.4), not by an entanglement count.
- **Z1's ray is a null geodesic of the five-dimensional geometry, not light** (item 90).

## History (2026-10-07, after items 150 and 151)

- **The table above was stale.** It still read "30 lemmas, 10 yours, 10 proved, 10 OPEN" after O3, I2, E3, E4, R4, B5,
  B6, R5 and B7 had each been worked in lemmas/, and after your ten lemmas (item 151's "Are my 10 lemmas proved?") were
  split by axioms.py into six derived, three definitions and one equivalent to B4. It now reads from warptheorem.py's list.
- **B6 is narrowed, not proved as first written.** The work fixes k's ratio, and no clause depends on k's scale, so the
  scale cannot be read back off the theorem: it is B6′, by measurement (136 answer 8).
- **I1's extremal step is READ for a class.** Strominger–Vafa (hep-th/9601029, abstract) derive S = A/4 for a class of
  five-dimensional extremal black holes by counting ground states. The corridor is not shown to be in that class.
- **B4's curvature test, to order 11 in y, does not decide.** At ℓ = r₀ the Kretschmann series near the throat has
  every coefficient positive and a radius of about 0.9m (r = 2.05m) to 1.07m (r = 2.25m), with a real Padé pole there;
  at r = 3m there is none within 1.7m, and the flat limit shows none within 1.6m. Evaluated from the metric itself, K
  is finite but rising steeply (235 at y = 1.0m, about 2×10⁴ at 1.2m, r = 2.05m), and orders 7, 9 and 11 disagree past
  y ≈ 0.8m, where g_tt and g_rr fall toward zero together (y ≈ 1.28m). The series cannot tell a curvature singularity
  from the bulk's horizon. B4 stays OPEN; the next step is a method beyond the Taylor series. Scratch runs, not seated.
- **B4 worked in order, after item 152 (lemmas/B4.md, verified once).** B4 is now three lemmas.
  - **B4a, PROVED (STRUCTURAL), given W2 inside T.** Your "two separate positions connected by/reached through a
    dimension" is one end of the bulk, and the passage deforms through it.
  - **B4c, READING.** The far boundary is untrapped only if ℓ > 2R_reach in the board's model.
  - **B4b, OPEN.** The bulk must be regular within the hold's double cone: about 2m deep near the throat, about 8m at
    r = 3m. The series is stable to 1.5m and 2.25m there.
  - **The entry above** "orders 7, 9 and 11 disagree past y ≈ 0.8m" was a visual reading. By the 1% criterion they part
    at 0.65m.
  - **B6 is narrowed again:** B4 depends on k's scale.
- **B4 finished, as far as the board's tools reach (item 153; lemmas/B4.md step 5, not yet verified).**
  - **The static bulk taken past its series.**
    - An exact two-variable series to order 60–80, checked against bulkseries.py, with Padé continuation and the full
      double cone.
    - It carries a curvature singularity above the throat: y_b ≈ 2.50m at r = 2.15m, K ∝ (y_b − y)⁻³.
  - **B4b, PROVED.** Every hold below 13.0 clocks keeps its double cone in verified, regular bulk.
  - **O3, PROVED as a window.** O3's 28.48 clocks reaches K = 2.3×10⁴ and the singular surface. So H-ONE-STEP-PER-BIT
    and H-HOLD-AT-BOUND are withdrawn, and O3 is now the window from the READ bounds up to 13.0 clocks.
  - **B4d, OPEN.** The opening and closing as a five-dimensional evolution.
- **The readings worked, item 154.**
  - **B5 is derived.** Null energy at every point is your 117/120, shown consistent. That replaces H-SHARED-PROFILE.
    No radion is your 127 with 141, which replaces H-PIN-IS-COINCIDENCE. Z3's composite step follows.
  - **B7 is derived.** It follows from 100, 140, 122 (4) and 101 answer 1, with Maldacena–Susskind p.17 READ.
  - **I1 is derived** from your 137 (1). H-EXTREMAL-ENTROPY is no longer needed.
  - **B4c is down to one reading.** Its radiation step (Raychaudhuri) and its near-zone step (causality) are derived;
    the far model, H-FAR-MODEL, stays the board's.
  - **Still readings:** B4c, E3, R4 and R5, each for the reason its row gives.
- **You confirmed the three readings only you could settle (item 155).**
  - E3: E's remainder is position 2's expansion, part of the build.
  - R4: the length is in bits.
  - R5: activation is a trigger.

  All three are derived from your rulings now. One lemma rests on the board's reading, B4c's far model; one is open,
  B4d.
- **Step 5's verifier (lemmas/B4.md History).**
  - **The hold's cutoff.** The refined, converged double cone puts it at ~11.3 clocks, not 13.0. Edge columns
    r = 2.005–2.01 and 10–32m are added.
  - **B4b and O3 are READINGS (computed), not PROVED.**
    - B4b rests on the locally analytic class, on agreement between Padé orders, and on the flat limit.
    - O3's hold lying in the window is a requirement on the write, H-HOLD-IN-WINDOW.
  - **The count:** 14 proved, 11 derived, 3 definitions, 3 readings, 1 measurement, 2 open.

## History (2026-10-07, item 158)

- **Your item 158 made the hold the write.** You said the hold lasts *"exactly as long as the write needs"*, and left
  the write's mode, the bulk's stillness and the energy's place to the math. lemmas/o3_write.py and O3-WRITE.md
  compute the write's least time.
- **The rate bounds don't decide it.** Bekenstein–Schiffer's information-rate bounds (quant-ph/0311050, eqs. (86),
  (97), (112), (115), READ) each give a fixed number of clocks for every N: 2, 79.5, 113.9, and 113.9/log₂ of the
  channel count.
- **The room the README needs does.** The README is the inflow (115 (c)), so it starts within light-reach of the
  throat. Until it collapses it can hold no more states than a free gas there ('t Hooft, gr-qc/9310026, pp.4–5,
  READ). So the write needs at least (3645 ln2·N/(8Z))^(1/3) − 2 clocks: 2.0×10⁵ at the example README, where the
  gas's own temperature puts every Standard Model particle in Z. That is 1.3×10⁻³¹ s.
- **One verifier.** The bound stood in every variant: through the extra dimension, without H-README-ALONE (630
  clocks), and with prior entanglement. The draft's conclusion did not. It needed an unnamed reading, that the write
  sits inside the static hold. Under your 115 (c) the write may instead be the opening itself, which is already
  non-static.
- **Where it stands.** On either reading the bulk is not still through the write; that answers 158 (3). O3 goes from
  READING to OPEN and waits on B4d. H-HOLD-IN-WINDOW is refuted only if the write sits in the static hold.
  158 (1) and (4) stay open.
- **The count:** 14 proved, 11 derived, 3 definitions, 2 readings, 1 measurement, 3 open.

## History (2026-10-08, items 159 and B4d stage 1)

- **Item 159, both readings tested** (lemmas/o3_readings.py, O3-READINGS.md, verified once).
  - **Reading (i), a hold after the corridor stands.** As first tested it contradicted 115 (c): a standing corridor
    means the README has arrived. Its coherent form (i′) is a write after arrival, and it keeps O3's static window.
  - **Reading (ii), the write as the opening.** It is refuted in the board's quasi-static model: the black string
    around the opening is Gregory–Laflamme unstable for ≥ 9.2×10³ e-folds. The dispersion relation is computed from
    GL's equation, which now matches Emparan–Suzuki–Tanabe term by term.
  - **The nearby-wall escape is closed.** Every mode crosses the unstable band as the mass rises from zero.
- **B4d stage 1** (lemmas/b4d_stage1.py, B4D-STAGE1.md, verified once).
  - **Regime.** Through the opening, B4c's far model forces the flat limit (ℓ > 4×10⁵ m).
  - **What stands.** The only bulk the board can show standing is a localized 5D hole, and it is not the corridor: no
    1/r tail, not extremal, r_h ~ 580 m.
  - **Closing the static bulk.** A plane closing eq. (17)'s static bulk would carry matter breaking the NEC. At small
    heights this is structural: ρ + p_r = y_w·R⁽⁴⁾_kk, eq. (17)'s own radial null combination. That matters only on
    the withdrawn reading (i).
- **The count** is unchanged: O3 stays OPEN until the reading is fixed.

## History (2026-10-08, item 160)

- **You said the corridor and the opening are the same object.** That settles item 159.
  - The hold "after the corridor stands", reading (i) and its form (i′), dissolves: there is no corridor before or
    after the opening.
  - Reading (ii) stands, with the opening being the corridor itself.
- **Two board readings give way:**
  - opening.py's Vaidya model as the form of the opening. It ends in Schwarzschild, not the corridor, so the
    Gregory–Laflamme refutation built on it (o3_readings.py R3) no longer bears on the corridor;
  - H-PULL-IS-COST, where it was read as "the corridor does not exist until the README has arrived".
- **What remains is one question: the corridor itself, through the write.** Held static on eq. (17), its own bulk
  reaches the singular surface by about 18 clocks. The write needs at least 2.0×10⁵. So the corridor must change while
  the README passes through it.
- **O3 is B4d's.**

## History (2026-10-08, items 161–164 and B4d stage 5)

- **Item 161:** your inclination that the corridor stays regular through the write.
- **Items 162–163:** one object of fixed size, holding the README all together, as one whole. The instant reading of
  "at once" is set aside, so `O3-ATONCE.md`'s instant route and B4d stages 3–4 become conditional on that withdrawn
  reading.
- **Item 164:** a ground state oscillates. `o3_ground.py` (verified once) answers it.
  - The phase turns, and position and the kinetic and potential energies fluctuate.
  - The total energy does not.
  - Under 163 the held README is an exact energy state, and the write's spread is 5.2×10⁻²⁰ of E. That answers all
    three of the board's objections to achievability.
- **B4d stage 5** (`b4d_stage5.py`, verified once).
  - **Positive-tension side:** with eq. (17) there, the bulk is singular within 8–16 clocks at every finite ℓ tested.
  - **A closing plane** would carry matter that breaks the NEC.
  - **Negative-tension side (your 139):** the bulk is regular on the evidence. That is the live route for 161. Its open
    costs are data at the bulk's edge and localized gravity.
- **No status moves.** The count stays at 14 proved, 11 derived, 2 readings, 3 definitions, 1 nature, 3 open.

## History (2026-10-08, item 165 and B4d stage 6)

- **Item 165:** *"Of course. Continue"*, to putting the two planes together.
- **Stage 6** (`b4d_stage6.py`, verified once).
  - **Our plane cannot carry eq. (17) regularly.** Every positive-tension plane has a side where the warp decays, and
    stage 5 makes that side singular. Ours is positive by your 139 and at the Randall–Sundrum tension by clause (B).
  - **Position 2's plane can.** At its own ℓ₂ = 3ℓ (your 138), both its sides grow at exactly your 139's −1/3.
  - **A mirrored closing plane** would break the NEC at every separation.
- **Put to you:** whether the corridor's eq. (17) sits on position 2's plane. If it does, clause (B)'s "at the
  Randall–Sundrum tension" would not apply to the corridor's plane.

