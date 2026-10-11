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

- **(G) Geometry** (seated as re-worded, item 187).
  - The corridor sits in the bulk, on neither plane; it only bridges them (179/180).
  - Bronnikov–Kim's eq. (17) at r₀ = 2m is kept only as a plane's possible reading of the corridor's mouth
    (H-PLANE-READS-MOUTH, the board's; OPEN).
  - **E = √(N h c⁵ ln2 / (8π²G)) = 459,404,002.42 J × √N.**
  - **m = GE/c⁴.**
  - **r₀ = 2m = √(N h G ln2 / (2π²c³)).**
- **(H) Holding.**
  - The throat holds exactly the README: **4πr₀² = N × 2hG ln2/(πc³)**, which is 4 ln2 Planck areas per bit.
  - The horizons hold it too.
- **(O) One way.**
  - The passage runs from position 1 to position 2 through an extremal horizon, with surface gravity 0.
  - It is nonsingular and complete, never runs back, and survives its hold.
- **(Z) Null energy never violated** (seated as re-worded, item 187).
  - "Never violated" holds net along each light ray (183): a negative member paired along the same light rays is the
    appearance (117/120).
  - Along the passage, a null geodesic of the five-dimensional geometry, the null energy is zero, and the plane's
    apparent deficit is exactly the bulk's pull (Z1, Z2: computed with eq. (17) as the plane's own metric, the board's
    configuration, and re-read under 179).
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
| B | **B4d the opening and closing evolve regularly in five dimensions; data beyond the cone join the exterior** | **OPEN**: a nonlinear 5D problem through a write of ≥ 2.0×10⁵ clocks at fixed size (162, 163). Stage 5 (verified once): with eq. (17) on a plane, a side where the warp decays is singular within 8–16 clocks, a side where it grows is regular on the evidence. Stage 6 (verified once): every positive-tension plane has a decaying side, so ours (139, clause (B)) cannot carry eq. (17) regularly; position 2's plane can, at its own ℓ₂ = 3ℓ (138), carrying exactly 139's −1/3 with both sides growing. Stage 7 (verified once, item 166): across both planes every small-separation branch has a decaying outer bulk, so singular. Simulation phase 1 (sim1_transition.py, verified once): eq. (17) is no 4D null-energy end state; the bulk must supply its anisotropic Weyl stress. Phase 2 (sim2_facing.py, verified and re-verified; item 168): two matter-free pieces of our plane cannot face each other across a static bulk (a facing piece would read tension <= -1, another universe's); with the README's NEC-obeying stress on position 2's piece (H-README-ON-P2, put to you), facing only near the object's throat on the verified map. Still open within one universe: the passage through the horizon (next), a changing bulk, motion inside the planes |
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

## History (2026-10-08, item 166 and B4d stage 7)

- **Item 166:** *"Both planes at once"*.
- **Stage 7** (`b4d_stage7.py`, verified once).
  - **No parallel, matter-free position-2 plane exists** at a nonzero tension.
  - **The slab** between the planes is itself stage 5's singular case.
  - **Every small-separation branch has a decaying outer bulk,** whichever ℓ is the unit and whichever count of 139's
    −1/3. That holds with eq. (17) on either plane. Our side is then singular directly, position 2's by continuity.
  - **Recorded:** 139's −1/3 counts position 2's plane twice. One sheet is −1/6, and with that the equations reproduce
    M4 exactly.
- **Still open:** separations near the slab's own singular surface, data that differ by direction, curved planes, and
  outer bulks that are not anti-de Sitter.


## History (2026-10-08/09, items 167–170, simulation phase 1, your PDF)

- **Item 167:** run B4d as a simulation, in phases. **Item 168:** in your sense: first the corridor between two
  positions within one universe, then between universes. The hierarchy is your law and history trajectories.
- **Phase 1** (`sim1_transition.py`, verified once by three verifiers). A four-dimensional Einstein–scalar evolution. It
  stands as the validated tool; its 4D reading of your words is withdrawn by item 168.
  - **Matter in, evenly spread:** a README written evenly over the write disperses.
  - **Fixed size:** a horizon that keeps its size absorbs nothing (Raychaudhuri).
  - **Eq. (17):** not a 4D null-energy end state. Its Weyl fluid is anisotropic, so the bulk must supply it.
- **Item 169** (a thought, offered for discussion). No travel through time alone; a time-only target lands in a separate
  spacetime. The board reads chronology protection within one universe as following from your 117/120 (Hawking 1992,
  not READ).
- **Item 170:** the world arrived in runs on position 2's clock; the object keeps position 1's time, like an astronaut.
  - **The board's reading** (destination's frame sets "now"): a return between positions approaching each other would
    arrive before the departure, by ~2.8 h for Proxima.
  - **Item 169 sends that return to a separate spacetime,** so the two together keep one universe free of loops.
- **Your PDF** (`lemmas/M-PDF-ASTRO.md`): it answers no open question and is set aside. Four filings from its sources:
  - one universe is a global condition of topology;
  - the vacuum bridge lives 6.3 clocks against the write's 2.0×10⁵;
  - Eardley's white hole;
  - Hochberg & Visser's null-energy theorem, which excludes horizon throats, the corridor's kind.
- **Phase 2 is being designed** in your sense (item 168).
- **No status moves.** The count stays at 14 proved, 11 derived, 2 readings, 3 definitions, 1 measurement, 3 open.

## History (2026-10-09, simulation phase 2: two positions, one universe)

- **Phase 2** (`lemmas/sim2_facing.py`, selftest 16/16; verified by three verifiers and an adjudication, then
  re-verified by two more; `SIM2-FACING.md`).
- **Decided by deduction, for one member.** Two matter-free pieces of our plane, at our tension, cannot face each other
  across a static bulk. A Raychaudhuri trap keeps the warp falling away from our plane, so a facing piece would read a
  tension of −1 or below: the negative plane of your 139, another universe's. The member is refuted on its stated
  conjunction (H-Z2-PIECES, H-NEAREST-APPROACH, static, vacuum, clause (B) on both pieces).
- **Computed, only on H-README-ON-P2** (position 2's piece carries the README's stress, obeying the NEC). This is put to
  you: it sits against your 129 (1), 130 (1) and 136 (2) as worded, and would relax clause (B) on position 2's piece.
  - **On the verified map,** facing is allowed only near the object's throat.
  - **For a reached nearest point:** a band of depths y\* to y_s. Positive energy needs ℓ ≥ 49.86m.
  - **Approached down the throat:** no lower edge in the approach, so your 127's coincidence is allowed by the NEC
    there. Positive energy needs ℓ > 27.07m.
  - **Within one universe only on H-SPLIT-AT-OUR-TENSION;** on H-LAW-READ-BY-TRACE it is phase 3.
- **Still open within one universe:** the passage through the horizon (`sim2_passage`, next), a bulk that changes
  during the hold (152 (2)), motion inside the planes (141), and nearest approaches far out.
- **No status moves.** The count stays at 14 proved, 11 derived, 2 readings, 3 definitions, 1 measurement, 3 open.

## History (2026-10-09, items 171–185: E-PASS, the corridor in the bulk, pairs, matter)

- **Items 171–177.**
  - **171:** a question about space-only teleportation. The board's answer, offered for discussion: on your rulings the
    corridor within one universe already is that.
  - **172:** position 2's piece may carry the README's stress (H-README-ON-P2), and coinciding is the endless approach
    down the throat (H-COINCIDE-DOWN-THE-THROAT).
  - **173:** E-PASS next.
  - **174:** three questions left "For the math", each decided by the board under 149.
  - **175–177:** entanglement. You chose "Yes, that is the appearance", so escape E-Q (coupling the entangled ends) is
    open as a route for B4d.
- **E-PASS** (`lemmas/sim2_passage.py`, X1–X10). Verified by five verifiers, each finding put to skeptics
  (`lemmas/EPASS-VERIFY-RECOVERED.md`).
  - Its key overclaims are confirmed: X7–X8 put a singular layer in the crossing's past beyond what is computed; X9 cuts
    the slab; X10 (c)'s perturbed run breaks the bulk constraint; two controls cannot fail; and "end 2 is our own
    plane's far end" is a global identification no instrument computes.
  - The design for X11–X25 (`lemmas/EPASS-DESIGN-SPEC.md`) adds Lemma S: a horizon that keeps its size and stays still
    takes no net null flux, so the README can cross only with an exact negative partner along the same light rays.
  - The fix round is running.
- **Item 178** (pairs; a null is a definable nothing). Answered in `lemmas/ITEM178-NULL-PAIRS.md`, then re-read under
  183.
- **Items 179/180** (the corridor exclusive to the bulk) are answered in `lemmas/ITEM179-BULK-CORRIDOR.md`.
  - Eq. (17) is demoted from input to candidate output: at most a plane's reading of the corridor's mouth
    (H-PLANE-READS-MOUTH, the board's).
  - k's scale still has no value. Every corridor length grows as √N, so any equality ℓ = c × (corridor length) would
    give a different k for every README, against the board's reading of your 127 (2) and 138.
- **Items 181/182** (the bulk balance, your guess C) are in `lemmas/BULK-BALANCE.md`.
  - Matter-free planes beside a bulk corridor cannot rest.
  - With matter, a flat plane can rest, but its matter breaks the null energy condition at each point.
- **Item 183** ("Yes: never violated as a pair"). Axiom Z3 is re-read as net per light ray, and E-PASS's stationary
  crossing is OPEN through 177, not refuted.
- **Item 184** ("There are no matter free planes"). Every matter-free result is a limit.
- **Item 185** (the matter round) is running.
- **Clauses to be re-worded** (the board's proposals, put to you; not seated):
  - **(G):** the corridor is in the bulk and sits on neither plane (179/180). Eq. (17) at r₀ = 2m is kept as a
    plane's possible reading of its mouth, OPEN.
  - **(B):** "The plane is free of matter" gives way to 184: each plane carries its own universe's matter, the corridor
    adds none, and the matter-free plane is a limit.
  - **(Z) and (B)'s positivity:** "never violated" holds net per light ray (183). Positivity stays your 139 (2), a
    separate ruling.
- **No status moves.** The count stays at 14 proved, 11 derived, 2 readings, 3 definitions, 1 measurement, 3 open.

## History (2026-10-09, items 186 and 187)

- **Item 186:** you asked whether k differing for each corridor solves any questions, and proposed working from that
  assumption if the evidence leans that way (H-K-PER-CORRIDOR, yours, conditional). The board's assessment is running
  (`lemmas/ITEM186-K-PER-CORRIDOR.md`, to come).
- **Item 187:** clauses **(G) and (Z) are seated** as re-worded above, on your "Seat both". The lemmas under them keep
  their own statuses: Z1 and Z2 were computed with eq. (17) as the plane's own metric, the board's configuration, and
  are re-read under 179. What k varies with, and whether each universe has its own strength of gravity, you left "For
  the math": the board decides both in the item-186 note. Clause (B) is re-worded after it.
- **No lemma status moves.** The count stays at 14 proved, 11 derived, 2 readings, 3 definitions, 1 measurement, 3 open.

## History (2026-10-10, items 204–206: the cycle through the cypher; the chain seated)

- **Item 206** ("Seat the corrections after this pass ..."): the lemma table in `warptheorem.py` is now the chain the
  board has been running through the cypher. It was `lemmas/chain_cypher.py`'s proposal (the green-the-chain round:
  B1-MATTER, F1-AUDIT, ITEM197, CLOSE-FLUX, items 200 and 201, `o1c_complete.py`), with item 204's two splits and pass
  2's corrections. Each row is seated with its owner and the status that owner earned; `RESTS_ON` names the inputs a
  status is conditional on; the six inputs are rows of their own (clause N, OPEN). `chain_cypher.py` now reads its rows
  from here, so the chain and the theorem cannot drift apart.
- **Seated from the 204 splits:** B5′p → **B5pu** (within one universe, DERIVED: 202 makes position 2's matter ours,
  `b5p_cypher.py`) and **B5px** (between universes, OPEN); H2t → **H2tu** (within one universe, DERIVED on M1,
  `m1p2_cypher.py`) and **H2tx** (between universes, DERIVED on M1 and M1P2x, `g2_between.py`).
- **Seated from pass 2:**
  - **Z3b: OPEN → DERIVED** on M1, FAR, WRITE, ARRIVAL, CLOSE (`z3b_cypher.py`): every static ray class keeps (Z),
    and the dynamic phases are exactly its inputs.
  - **M1 re-worded** (`corridor_shape.py` S0, `rim_profile.py`, `forming_rim.py`): the rim closes in the static bulk.
    Pass 3 found the bank's interpolation 8% wrong in g_rr near the throat (S0: now within 10⁻⁴ of exact columns).
    Corrected, the plain marginal corridor (radial held at zero) meets our plane at 3.1–5.3m, beyond r_b = 3.01m, with
    tangential null energy and energy positive all the way. Traced inward on exact near-horizon columns, it flattens
    into the throat's constant-depth corridor. A ring of 0.013–0.10 aσ balances the rim. The earlier "tangential gap"
    (S3, S5) was the interpolation's. Still open: the ring's nature and Wall C's bridge.
  - **CLOSE re-worded** (`close_object.py`): within one universe the closing needs no negative flux. Position 1's
    horizon ends (your 115 (a)), and it is extremal, so no outer-horizon area law binds it. What remains is the joint
    ending of the (+E, −E) mouths keeping (Z) (the wormhole mouth-mass rule, READ secondary). Between universes the
    negative-flux demand stands.
  - **M1P2 → M1P2x re-worded** (`g2_between.py`): between universes position 2 reads its own eq. (17), at
    m2 = (G2/G) m = 2m on 200 (1)'s count. Within one universe M1P2 reduces to M1.
- **The count:** 47 lemmas and 6 inputs. **21 green** under the strict rule (25 counting definitions). M1 alone would
  green 31; all six inputs, 36. The other 11 are 7 rows non-green by their own status (O3, B3, B4c, B4b, B4d, B5px,
  B5b) and 4 definitions under the strict rule.
- **The selftest** now also runs the seated owners' own selftests: about 10 minutes in place of 2.

## History (2026-10-10, item 207: the ring through the cypher)

- **Item 207** ("Ask the cypher"): M1 within one universe is met on every clause but (d), no added matter
  (`lemmas/m1_cypher.py`). The rim balances only with a ring of positive tension, 0.013–0.10 aσ, and the board read
  that tension as the fold's own (H-RING-IS-THE-FOLD). Put to the cypher (`lemmas/ring_cypher.py`):
  - **The cypher refuses the ring's nature.** Beside the carriers M has ruled (129's matter, 130's mouth, 201–202's
    tension and offset, the fold, the corridor), the ring as computed — a line, its tension solved from the rim's
    balance — is refused by geometry, information and statistics under every coding (order and algebra are
    coding-dependent). No ruled carrier is a line, and none has a tension solved from a balance.
  - **The reading is refuted as stated.** A thin pure-tension sheet carries no line tension at a fold: rounding a fold
    changes its line energy by σw(θ − 2 tan(θ/2)), negative, and zero in the thin limit. So the plane as modelled
    (201: a tension and an offset) gives its fold zero tension, never the ring's positive one. Entered as the fold, the
    ring is "not matter" at every order — but that is the reading restated.
  - **What physics records (READ):** Csáki and Shirman (hep-th/9908186) — a brane junction is static only when the
    branes' forces cancel, with no junction tension; a tension on the intersection is a separate parameter.
    Carroll, Hellerman and Trodden (hep-th/9905217) — a domain-wall junction's "hub" has energy of its own, fixed by the
    walls' own field. Entered as a line tension fixed by the plane's structure, the ring is "own structure" by that hub
    alone, and refused on M's carriers.
  - **What would decide it:** whether a plane has structure beyond its tension and offset that gives a junction a
    tension of its own (a stiffness or a thickness, as a domain wall's field does); or a rim that closes with no ring
    (the Plateau angle, 120°, which the family's 5–16° does not reach); or the ring being something M's model already
    holds.
- **No rim without the ring** (R8): with the README all in, the ring can be dropped only at a tangential meeting or
  at 120°. A corridor keeping its radial null energy cannot meet the plane tangentially (Grönwall on the radial bound:
  its slope at the rim keeps at least 89% of its earlier value), and at 120° it would leave the rim heading away from
  the throat. So the static rim needs the ring, and M1's static rim turns on what the ring is.
- **The count is unchanged:** M1 stays OPEN, on (d). The proposed split into M1u and M1x moves no row, so it is not
  seated. 21 green under the strict rule (25 counting definitions).

## History (2026-10-10, items 208–209: too much in the cypher; exact values)

- **Item 208** ("We have too much information in the cypher. Something doesn't belong. Ask the cypher what the ring is
  supposed to be, and what in the current theorem doesn't belong or what is missing") and **item 209** ("Normalizing
  suggests that we are allow for broad coefficients instead of exact evaluated values"). Every count below is the
  cypher's exact E. A first leave-one-out measured as a normalized ratio was withdrawn on 209. Two independent analysts
  and two adversarial verifiers checked every claim; only what survived is recorded here.
- **The ring: the cypher is silent, because the index held too much.** The ring's index had three carriers M has ruled
  on (matter 129; tension and offset 201–202; mouth and corridor 130/203) and five coordinates. One coordinate,
  fixed_by, is a key. Three others, with_corridor, pure_tension and matter, are a one-hot code of a single three-way
  choice. No cell of any kind can close that index, and any lone junction entered with its nature unknown gets the
  ring's refusal. So ring_cypher's R4 and R6 refusals measure a value no ruled carrier has, not the ring. The only cell
  that closes the index, (sheet, README-fixed, not matter), depends on the board's own fold cell, and it is not a ring.
- **What the ring is supposed to be, on consistent physics: not a positive ring.** forming_rim F3b's ring is positive
  only because the corridor is given −σ at the rim. That is rim_readme R5's coincidence law for facing sheets, but the
  meeting angle comes from the tilted marginal corridor, so two corridors' inputs are mixed. With the marginal
  corridor's own tension (ρ_rim > 0, ρ + p_r = 0, τ = ρ_rim ℓ/(3m)), the balance asks λ/(aσ) = −cos 2θ − τ cos θ. That
  is −0.60 to −1.16 at ℓ/m = 8.54 for every admissible member: a junction in compression. A rim needing no junction sits
  past 45° (47–51°), which no admissible member reaches (`lemmas/ring_consistent.py`). The ring's coefficient was in any
  case broad by 209: a free family of launches, a Padé flat-limit bulk, quoted as a range.
- **Seated (206):**
  - **Z3b DERIVED → OPEN.** Its across-the-ring class assumed the positive, NEC-keeping ring. What the junction carries,
    and its NEC, are not computed (`z3b_cypher.py` Z4).
  - **M1's record corrected.**
  - **Correction notes, with the computations kept as they were:** forming_rim F3b, rim_profile P5 and ring_cypher R1/R8
    rest on R5's −σ; corridor_shape S2's "at most 0.76 (m/ℓ)E" is stale (q = 0.67–5.66 on the corrected bank).
  - **The count:** 21 green (strict) and 25 (audit), unchanged. Eight rows are now non-green by their own status. The
    smallest input set is {M1, M1P2x, WRITE, ARRIVAL, CLOSE}, since FAR entered only through Z3b. All six inputs would
    green 35.
- **The theorem through the cypher** (`lemmas/belongs_cypher.py`): 53 rows, 20 distinct cells.
  - **E:** 748/748/114/312/52 as asked; 748/748/90/312/40 after Z3b's correction. The correction itself moved the
    theorem toward closure.
  - **Does not belong:** no single row closes it. B4c falls most, then B4b, then E1x/E2x. B4b and B4c are READINGs
    calibrated to a hold of ~11.3 clocks, against the real hold of ≥ 2.0×10⁵ (O3, item 160), and both say "re-read
    with B4d". Together they lower E with no language rising on every coding the critics tried, but six other pairs do
    too, so it is not decided. B4d's record carries a range as well.
  - **Missing:** nothing survives a change of coding.
  - **M1:** it holds content beyond the mouth — the rim, the ring and Wall C's bridge. 14 of the 15 rows resting on M1
    use only its reading of the mouth.

## History (2026-10-10, item 210: B4b and B4c superseded; the rim is a coupling)

- **Item 210 (1), M: "Yes: superseded by B4d".**
  - B4b (the static bulk regular within the hold's double cone) and B4c (the far boundary untrapped) are set aside.
    Both were READINGs calibrated to a hold of about 11.3 clocks; the real hold is at least 2.0×10⁵ clocks (O3, item
    160). They are kept on record in `warptheorem.py`'s `SUPERSEDED` list, with the statuses and records they were
    seated with, and are not deleted.
  - B4d now carries their questions over the real hold, and rests on FAR through B4c.
  - The chain is now 45 lemmas and 6 inputs. Green is unchanged at 21 (strict) and 25 (audit rule). Six rows are
    non-green by their own status: O3, Z3b, B3, B4d, B5px and B5b. M1 alone would green 31; all six inputs, 35.
  - Through the cypher (`lemmas/belongs_cypher.py`), the theorem's exact E falls from 1938 to 693 (order 247, algebra
    247, geometry 39, information 143, statistics 17); it was 1974 when item 208 was asked.
  - Z3b and B4d now index alike: both OPEN on M1, FAR, WRITE, ARRIVAL and CLOSE. These are the rim's junction and the
    5D evolution, the two rows the ring and the write leave open.
- **Item 210 (2), M: "The rim is a coupling interaction between the mouth and our plane. My guess is it looks like a
  singularity on paper, but is an open mouth."**
  - Carried as M's: the rim is a coupling between the mouth and our plane.
  - Carried as M's guess: on paper it looks like a singularity, but it is an open mouth.
  - The board's reading: the rim stays in M1, since a coupling between the mouth and our plane is part of the plane's
    reading of the corridor's mouth, so M1 is not split. The junction the thin-sheet balance asks for (a line in
    compression) is what the open mouth looks like on paper, as 130's black hole "is what the mouth at position 1 looks
    like". On that guess it is not added matter, so clause (d) is met.
  - What the open mouth carries, and whether it keeps (Z), stay to be computed.

## History (2026-10-10, item 211: the open questions through the cypher, first part)

- **M, item 211: "Keep moving the open questions through the cypher please".**
- **The indexes audited first (`lemmas/index_audit.py`).** Each open row's cypher index was checked for what item 208
  found in the ring's index.
  - **Keys:** z3b_cypher, far_cypher, g2_between, corridor_shape S6 and rim_readme each have a coordinate that
    individuates every cell, so any verdict that turns on such a value is forced.
  - **Redundant groups:** eleven indexes carry one distinction over several coordinates.
  - **Clean:** arrival, write, close_object and b5b.
  - No seated status rests on a forced verdict alone. Each forced verdict is marked void as evidence in its own
    instrument, and no status moves.
- **The open mouth (`lemmas/open_mouth.py`).** This is M's guess in item 210: our plane turning smoothly into the
  corridor. It was computed in the flat-limit bank, and an adversarial verifier checked it.
  - **Two orientations.** A smooth turn fixes the surface but not which side is kept.
    - D+ keeps corridor_shape's own normal. It is what B becomes when our plane inside the rim is removed.
    - D− keeps the other side. There every seated stress changes sign, so the seated family has negative energy along
      its whole length and no D− body has been computed.
    - D+ is therefore the only orientation in which the seated corridor (rim_profile P4, P4b) is the open mouth's body.
  - **The joint in D+.** It is the plane's own concave fold. It carries a negative Nambu–Goto line,
    λ = −(2/κ₅²)·t, where t is the meeting angle. On paper that is a line in compression, as item 210's board reading
    had it, and it needs no balance.
    - A radial null ray in the sheet gains −t/√(1 − 2m/r_rim) across the joint (−0.14 to −0.33 over the members), and
      the marginal corridor adds exactly 0.
    - So (Z), net per ray (183), asks for a partner on the same rays. That is TS's own exception (P2-FULL) and where
      177's appearance and 210's coupling enter.
    - What pairs it is OPEN.
  - **The joint in D−.** It is a convex fold carrying a positive line, with its tangential null energy kept only if
    r_rim ≤ 3m.
  - **Exact values.**
    - The marginal corridor's energy at its rim is ρ_rim = √2 sin t √(2r_rim − 3m)/r_rim^1.5, so ring_consistent's τ
      is an exact function of (r_rim, t), not a free coefficient.
    - The tangential bound is the photon sphere, r = 3m exactly. rim_profile P2's "~3.01m" is the grid step.
    - A gravitating sheet's fold carries a Nambu–Goto line. ring_cypher R2 ("no line tension at a fold") holds for a
      test membrane only.
  - **The cypher (O7).** M's sentence entered as a cell is the D+ cell, so every language admits it by construction;
    the cypher adds nothing beyond the computation. Whether D− has a body splits the languages, and statistics'
    refusal is forced, so the cypher does not decide it.
  - **The board's reading, H-OPEN-MOUTH-DPLUS, to be overruled by M at any point:** M's open mouth is D+, because it
    keeps the seated corridor. D− is kept on record.
  - **Corrections seated (206), notes only:** M1's and Z3b's records; rim_profile P2 (r_b = 3m); ring_cypher R2
    (scope); ring_consistent C2 (τ exact). No status moves.
  - **Refuted and kept on record (the item-210 critic):**
    - the analyst's claim that the open mouth needs no appeal to 177 or 183, which holds in D− only;
    - its correction of item 210's board reading, which holds in D− only;
    - its cypher's "one missing cell", an artefact of an omitted carrier.
- **The hold's records, corrected (206; checked against the sources).**
  - **B3** rests on B4d's inputs. B3 is "equivalent to B4", and since item 210 B4 is B4a (PROVED) plus B4d, so CLOSE
    is added, which B3 lacked ever since B4d first rested on it. The theorem's exact E falls from 693 to 616
    (220/220/39/120/17) with no language rising, the same as leaving B3 out. B3, Z3b and B4d are now one cell
    (belongs_cypher B9). Statistics stays at 17, so it is the records that move B3, not the count. B3 stays OPEN.
  - **B4d's stage-5 range.** "Within 8–16 clocks at every finite ℓ tested" becomes the four measured holds: 16.0,
    13.0, 10.9 and 7.8 clocks at ℓ = 2m, m, m/2 and m/4. ℓ = m/4 was added after the verifier, and its 7.8 lies
    outside the old range.
  - **WRITE's floor, exactly.** (9/2)(5N ln2/Z)^(1/3) − 2 = 199,702.19 clocks at the example README, with Z = 108.75
    (its lower bound). "≥ 2.0e5" rounds a floor up, and the floor falls as Z^(−1/3).
- **The shoot critic's findings, seated (206).**
  - **The ring's balance counts the corridor's warp part** (ring_consistent C5; the critic's F13, re-derived by hand).
    A sheet facing its plane across the slab carries ρ_w = −σ cos t (1 + sin²t/3) and p_r = +σ cos t. So
    λ/(aσ) = sin²t − τ cos t.
    - At ℓ/m = 8.5415 every admissible member is still in compression, at −0.10 to −0.27 aσ. Item 208's −0.60 to
      −1.16 dropped the warp part: the sign survives, the values do not.
    - A balance with no junction needs ℓ/m = 0.63–7.14, below the window.
    - The 45° threshold belonged to the dropped term.
    - M1's record now carries this.
  - **The bank's near-throat derivatives** (corridor_shape S0 and rim_profile P4b, notes only). The y-derivatives are
    interpolated linearly in ln(r − 2m). Near the throat that puts the radial null energy off between columns by up to
    +220%.
    - The marginal rims move by about 1%: 3.430704m exact against 3.390m from the bank (the rim figure checked here).
    - P4b is not re-run on exact columns.
    - Recorded, not repaired.
  - **The open mouth's record** (open_mouth.py, docstring).
    - D+ is the shoot analyst's S, reflected.
    - D− is excluded through TS on grazing rays, not on a pointwise reading alone.
    - The tangential bound in D− is strict.
    - Both orientations keep b4_static S2's singular surface under the throat, so what is shown is a sheet and its
      joint, not yet an open mouth in a regular bulk.
    - One dive near the throat keeps every ray class computed non-negative: the corridor's own shape is a candidate
      for what pairs the joint. It is broad and was computed in scratch, not re-run here.
  - **Refuted and kept on record:**
    - the "throat lever", whose half-ray positive was the boundary term where the ray is cut at the horizon (on
      mirror-completed rays the net is 2L < 0);
    - "every shallow mouth fails (Z)", which holds for complete mirrored rays only;
    - "N_D = −N_S exactly", which holds at flat order only, since the warp's radial part does not flip;
    - "iff r_rim ≥ 3m", where the exact condition is r_rim > 3m.
- **Formation and closing (ARRIVAL, CLOSE), through the cypher and its critic.** Both stay OPEN, and the critic
  reproduced every count independently.
  - **The refusals are fully forced.** At the orders used, statistics refuses nearly every novel cell: ARRIVAL at order
    3 refuses 146 of 147, and at order 4 it refuses all of them. So those refusals are the record's gap, not findings.
  - **ARRIVAL's record.** Its in-bulk refusal is undecided. Its (Z) half shares its deciding carrier with the open mouth
    (open_mouth O5) and the corridor's surface (203). README-HELD's 4D model ends in Schwarzschild, not the corridor.
    arrival_cypher A6 and A7 are noted: the ring rows' U now stands as "(Z) pending an OPEN partner".
  - **CLOSE's record.**
    - The (+E, −E) mouths were H-MOUTH-FLUX, which is withdrawn as a reading. It came from a secondary source and is
      additive bookkeeping, against 111 (b). It is scoped, not "refuted": the same 4D local bookkeeping fails M's
      one-energy accounting too. So CLOSE's (Z) is a 5D question.
    - **Within one universe** the plane's net negative influx is the appearance only if it is paired on the same rays,
      through B4d's 5D ending. That pairing is not computed.
    - **Between universes** the 4D area theorem binds only if R4(k,k) ≥ 0, which (Z) does not assert. The 5D theorem
      binds if the corridor's horizon is a bulk event horizon. That is not computed.
  - **E1u** now reads "no area-law obstruction" in place of "no negative-flux demand", and stays DERIVED.
  - **Not seated:**
    - the analyst's CLOSE recode, which is close_object O4 (ii)'s own cell and isolates nothing new;
    - "refuted" for H-MOUTH-FLUX.
- **Correction to the dive note above (deduced from TS's wording, P2-FULL).** The dive keeps every *in-sheet* ray
  class non-negative. A bulk ray grazing the sheet where its tangent null energy is negative gains
  S(k₀,k₀)/α → −∞, and the sheet's shape elsewhere cannot offset it. Only a second source at the same place can: TS's
  own exception. So the partner of the open mouth's joint sits at the rim, which is where M's "coupling interaction
  between the mouth and our plane" places it. The corridor's own shape pairs in-sheet rays only.
- **The hold (FAR, WRITE, O3, B4d), through its critic.** Every count reproduced independently, and no status moves.
  - **FAR (`lemmas/far_bridge.py`, new, in closed form).** Model C's bridge with position 2's plane on the growing side
    fails the surface WEC for every matter content: at k = 1, ρ ≥ 0 and ρ + p ≥ 0 force μ ≤ 0; at k = 0, ρ + p < 0.
    - Its matter-free member BRIDGE-NEG breaks (Z) on every ray meeting the plane, so its (Z) is 0 (deduced).
    - SLAB fails only on a board reading. FAR needs every ray across position 2's plane paired on that ray (177's
      coupling the obvious candidate), or that plane meeting the WEC in total.
  - **WRITE.**
    - Every computed hold that ends is shorter than the floor for Z < 1.4456e10.
    - Its cypher bracket is now exact about orders. Order 3 is informative. Under 200 (1) it gains a second triple,
      (corridor, keeps_Z, stands). Order 2 admits from pairs. Orders 4 and above are forced.
  - **O3.**
    - It carries the exact floor and the spread at T_min.
    - The perturbation's amplifications are exact: T/4 = 4.99255e4 and (1 + T/8)² = 6.23190e8.
    - No survival threshold is recorded, because none is sourced (refuted: the analyst's cut at 1).
    - Its order-2 admission rests on the window-hold cell alone.
    - Whether O3 rests on B4d's inputs is left as a record question, and is not decided by the count.
  - **B4d** carries the exact floor in place of "≥ 2.0e5".
- **Between universes (M1P2x, H2tx, B5px, B5b), through its critic.** No status moves.
  - **M1P2x (`lemmas/m1p2_junction.py`, new).** Where position 2's bulk meets ours at the corridor (203), the near-horizon
    AdS2 and S2 radii must agree from both sides. The Ricci-flat equations reduce to (c b')' = −c/2 and (b c')' = 2b,
    which make their ratio strictly monotone in depth (proved; the ODE matches the bank to 1e-5).
    - So, with position 2's side the same family scaled by m2 (H-OWN-BULK-SAME-FASHION), m2 = m. Every other mass
      ratio is excluded in the flat-limit static class, 2m included.
    - That refutes a conjunction of readings: H-ONE-G5's per-sheet G2 = 2G1 read as position 2's G, H-PULL-PER-SIDE,
      203's one E, and H-OWN-BULK-SAME-FASHION. **Which one gives way is the board's call and has not been made.**
    - H2tx's per-sheet capacity of 2N stands on that conjunction. Its arithmetic is unaffected, and its status is not
      moved on this alone.
    - Not seated:
      - "M1P2x reduces to M1": position 2's tension still acts on crossing rays and in the rim's balance;
      - the misreading of COUNT-CYPHER's sentence.
  - **B5px** under 183 is (Z) net per ray at the pin.
    - Normal rays need (3/4)σ + δσ₂ + ρ₁ + ρ₂ ≥ 0, which no ruling gives (OPEN).
    - Grazing rays need Σ(ρ + p) ≥ 0. This follows from TS on position 2's plane if its matter is the same at the pin.
    - The cypher's refusal is the X cell restated, so it is void.
  - **B5b** under 183 is B5'a on crossing rays plus each component's ρ + p ≥ 0 along the wall.
    - The pointwise demand asks more than (Z), and rests on item 154's reading, which 183 superseded.
    - No localised matter wall exists in the separable warped class.
    - Asked of belongs_cypher, leaving B5b out *raises* the exact E by 4. So the count does not say it does not belong.

## History (2026-10-10, item 212: the bulk is everything; the negative as the reflection's appearance)

- **M, item 212:** "the bulk is everything everywhere all at once. Our universe is a cell in the bulk index." On the
  partner: "what is it's just Z's reflection creating the appearance of negative null energy."
- **Worked in the conversation (`lemmas/two_sided.py`).** A workflow was started and stopped at M's question. Each
  result is exact and is checked a second way inside the file.
  - **One bulk, smooth across the sheet.** For any static metric, the curvature seen from one side is minus that seen
    from the other, so the two-sided stress vanishes identically, including the fold's line. The negative line at the
    rim exists only in the one-sided construction, which copies one side by reflection. So M's guess holds exactly at
    flat order: the negative is the reflection's appearance, and (Z) needs no partner.
  - **Two bulks meeting as flat-order mirror images** (203's own bulks with 202's same values). The two sides add, the
    stress is exactly the one-sided reading, and the joint's negative line is real.
  - **A sheet mirrored only at warp order**, which is how our plane sits (smooth at flat order, kinked in the warp, as
    item 197's mirror lemma forces). It carries ρ = σ cos t (1 + sin²t/3) > 0 with ρ + p_r = σ cos t sin²t/3 ≥ 0 and
    ρ + p_θ = 0, and no line at a fold. Its reflection is real but creates no negative null energy.
  - **The cypher** adds nothing. M's cell is exactly that last configuration, and its index has two redundant pairs,
    so its verdicts are forced.
- **The board's reading H-CORRIDOR-IS-OUR-BRANE**, to be overruled by M at any point: the corridor's sheet is our
  plane's kind of sheet. On it, 212 and 203 hold together: one bulk at flat order, (Z) kept at the rim with no partner,
  and the corridor's positive energy is its warp-order tension.
- **Not computed:** a bulk in which the warp's kink follows our plane into the corridor (the bank puts it at y = 0),
  and 203's equality of the corridor's energy with E. **No status moves.**

## History (2026-10-10, item 213: not mirror images; the object at position 1, not at position 2)

- **M, item 213:** "they are not mirror images of each other. The whole need for warp travel is that position 1
  contains a geometric object that is not contained at position 2. We want position 2 to contain the geometric object
  after the corridor is closed".
- **`lemmas/asym_junction.py` (worked in the conversation; two independent routes).**
  - **Route 1, the lapse.** Along every seated corridor the lapse runs from below 1e-5 at the throat to 1 − 2m/r_rim at
    the rim, a factor above 4×10⁴. A static sheet needs the lapse to agree from both sides up to one constant. A side
    without the object has no horizon, so its lapse cannot follow ours, and no static sheet joins the two.
  - **Route 2, the near-horizon radii** (m1p2_junction J5). Only equal masses match, and a side with no object has no
    horizon to match at all.
- **So, reading "contains" as the object's field on that side, the corridor cannot be static while position 2 lacks
  the object: it is the transfer itself.** That fits o3_write W4 (ii) (the write is the opening), 160 and 198.
- **On the other reading** (the field reaches position 2's side during the hold, as 132's black-hole and white-hole
  side views), a static sheet needs equal fields. Mirror images being excluded, that is one smooth bulk, and 213's
  asymmetry then lives in time, which no static field carries either. Either way, the transfer is dynamic.
- **Narrowed, no status moves.**
  - two_sided T3 is set aside by M's words.
  - The static rim readings (the joint, the ring, H-CORRIDOR-IS-OUR-BRANE) describe same-field corridors.
  - In M1P2x's conjunction, the member that gives way is the static class.
  - WRITE's "static bulk through the write" cannot hold on reading (b).
- **Next:** (Z) in the dynamic transfer. The object's positive E moves from position 1's side to position 2's side, and
  each position's own reading of its mass change is to be computed against 183, 177 and 212.

## History (2026-10-10, item 214: each sees its own reflection, not mirror images of each other)

- **M, item 214:** "They see their own reflections but are not mirror images of each other".
- **The board's reading (asym_junction A4).** Each bulk closes on its own mirror image at the corridor, the one-sided
  junction that item 197's mirror lemma forces locally. So the one-sided readings computed so far are each position's
  own view of the sheet:
  - the seated corridor's stresses are position 1's view;
  - 212's negative line at the joint is the appearance in that view;
  - the two views differ because the bulks' contents differ (213), not because one reflects the other.
- **What it leaves standing.** Israel's first condition compares only the sheet's intrinsic geometry, and one corridor
  seen from both sides (132) has one intrinsic lapse. So the item-213 finding stands: while position 2 lacks the
  object, no static sheet carries both views, and the transfer is dynamic.
- No status moves.

## History (2026-10-10, item 215: they exist within the everything bulk index)

- **M, item 215:** "they exist within the everything bulk index."
- **What it withdraws, as statements about M's configuration.** The two bulks are cells of the everything bulk index,
  related by their place in it, not glued to each other along a shared sheet. So Israel's first condition is not
  imposed between them, and two board results that glued them stand as computed for glued bulks only:
  - asym_junction A2–A4 (item 213: no static corridor);
  - m1p2_junction J5 (item 211: m2 = m).
- **What follows from that.** WRITE's static bulk is no longer excluded, and M1P2x's per-sheet conjunction is no longer
  refuted, in M's configuration.
- **What stands:**
  - each position's own view (214): the one-sided readings, with the joint's negative line as the appearance in
    position 1's view (212);
  - two_sided T1–T4 and asym_junction A1, as computed.
- **What is next:** what relates the two cells in the index — where they meet (203) and how the object comes to be
  contained at position 2 (213) — put through the cypher. No status moves.

## History (2026-10-10, item 216: the index questions through the cypher)

- **M, item 216:** "I agree. Run those questions through the cypher here please".
- **`lemmas/bulk_index.py`, worked in the conversation.** The index is M's own account of the transfer:
  - before (213);
  - the three holds (106 (b)): position 1's horizon only, then both horizons at once, then position 2's only;
  - after (213, 136 (2), 110).

  Its coordinates are where the object is held and which horizons stand (115). It has no key and no redundant group.
  A first design carried (Z) and dropped it, because it duplicated position 2's horizon exactly.
- **Where the two cells meet.** Only in the realized stage, where both positions hold the object. Leave that stage out
  and statistics admits no cell with the object at both positions.
- **How the object comes to be at position 2.**
  - The index never admits the object held nowhere.
  - The after state cannot be assembled from the transit stages, so the release at position 2 (its horizon ending,
    the object kept) is a step of its own.
- **(Z)** is unknown exactly where position 2's horizon stands, which is the hold and the closing (Z3b and CLOSE).
- **What it adds.** Every verdict is forced by a named unseen projection, since there are five cells (211). The cypher
  adds that each step is irreducible, that pairs alone over-reach (order 2 admits both-held states with fewer
  horizons; order 3 is closed), and where (Z) is still to be computed. No status moves.

## History (2026-10-11, item 217: a missing piece; the method equation; a three-body problem)

- **M, item 217:** "pairs alone over-reach: - we are missing a piece of the puzzle. Position 2. It could be the method
  equation itself that connects position 1 to position 2. It could be that the everything bulk contributes something
  we cannot see making this a 3 body problem." M pointed to M's paper "The Three Body Problem for Unknown Masses"
  (Drive, Prints & Proofs; read in full from the mirror).
- **`lemmas/three_body_index.py`, against the paper's Law 3.** Law 3 (verbatim): "Every coupling coordinate's exact
  physical bound requires either two parents or a congruence, and a tree carries only one … Three bodies form K₃,
  treewidth 2, requiring strong 3-consistency (Freuder 1982) where the closure operator ℛ delivers 2."
  - **The bulk index fits that mechanism.** Its pairwise constraints form a tree, yet pairs over-reach and order 3
    closes. The binding bound — both horizons stand exactly when both positions hold the object — has two parents.
  - **No hidden two-valued coordinate closes it pairwise. Exactly one three-valued coordinate does,** up to
    relabelling, with no key and no redundant group: where the object belongs — position 1, both at once, position 2.
    These are M's three holds (106 (b)), and the middle value, the corridor holding the object across, is the piece
    the index left implicit.
  - **With it, statistics closes** at orders 2 and 3, while the four lattice languages close under none of the 96
    codings. The exact region is not a lattice.
  - **So the method equation's ordinal half (ℛ) gives only the envelope.** If the equation connects position 1 to
    position 2, it does so through its metric half — a closed form on the index's coordinates (register 1206) — which
    needs the positions' values (E: 203, 110, 111).
- **On M's guesses:** H-BULK-THIRD-BODY is supported in the cypher's sense; H-METHOD-EQUATION-CONNECTS is open, on its
  metric half. No status moves.

## History (2026-10-11, item 218: the one-hour experiment)

- **M, item 218:** "let's treat this as a simple time travel experiment. I want to move an hour in the future. The warp
  corridor will put me in a universe identical to this one with a singular exception, that that universe is 1 hour
  ahead of ours."
- **`lemmas/one_hour.py`.** Position 2's values come from the record's Planck 2018 inputs (cosmo.py) and 201's
  constant offset.
  - **Unchanged:** σ, the offset, G, ℓ, and the README's mass and horizon. So for the experiment G2 = G, m2 = m, and the
    capacity is N; the per-sheet G2 = 2G1 is set aside for it on M's word.
  - **Advanced by one hour of expansion:** H₀Δt = 7.858760e-15.
    - The scale factor rises by 7.858760e-15.
    - The Hubble rate changes by −3.718052e-15.
    - Matter density changes by −2.357628e-14 and radiation by −3.143504e-14.
    - The CMB temperature changes by −2.141905e-14 K.
    - The critical density changes by −7.436105e-15, and Ω_Λ by +7.436105e-15.
    - Dark energy is unchanged exactly.
  - **In the bulk index:** by 201's two coordinates the two positions are the same cell. Cosmic time is the coordinate
    that tells them apart, and they differ by 3600 s in it alone.
- **Noted, not resolved:** 139 (1) has position 2's plane negative, a quarter of ours. An identical universe's plane
  carries our positive σ, and for this experiment the board reads 218 as governing the destination. No status moves.

## History (2026-10-11, item 219: a universe without the Madelung exceptions)

- **M, item 219:** "Let's consider position 2 universe where the madelung exceptions didn't exist. That is the
  principle difference between ours and theirs, all other differences are built from that condition. My Löwdin
  challenge work may be very helpful here"
- **`lemmas/no_madelung.py`.** Inputs: register 1306's observed ground configurations (`LW1-ground.py`), the Register's
  118-cell lattice (registers 11, 49, 66, 67), M's Löwdin solution, and the cypher. All are read-only.
- **Three readings of "the exceptions", all measured on register 1306's data:**
  - **Configurations:** 20 elements.
  - **First openings:** 2 of 19, La and Ac (register 1307).
  - **The differentiating electron:** exactly 3, La, Ac and Th. This is M's paper's own count.
  - The primary rule holds at every element in all three readings.
- **Position 2's table is the Madelung table.** M's chain, run with no exception, gives the aufbau table exactly.
  - The periodic table itself is unchanged: the same period lengths and the same period × group cells. The cypher's
    periodic-table index (E = 36) is one cell for both universes.
- **On the Method's lattice, both universes hold the same 118 cells.** These are 118 of 630.
  - The cypher gives identical E in every language.
  - What differs is which element sits in which cell:

    | Table | Inversions | τ |
    |---|---|---|
    | Register 49's (ours; the table is reconstructed from its count) | 28, reproduced exactly | 6847/6903 |
    | M's chain | 42 | 2273/2301 |
    | Position 2 | 0 | 1 |

  - The labelling as a cypher index closes only for position 2 (E = 0). For ours, information's E equals the
    inversion count.
- **On the observed configurations, the cypher separates the two universes.**

  | Observed configurations | Ours | Position 2 |
  |---|---|---|
  | Cells | 98 | 108 |
  | Order ideal | No (197 violations) | Yes |
  | Statistics(2) over-reach | 8 | 0 (closes) |

- **Built from that condition.** M's chain is causal in Z.
  - With and without the three exceptions, it differs at exactly 29 elements: Z = 57–70 and 89–103.
  - It meets again at Lu and at Rf, and nothing below La changes.
  - So "every other difference built from that condition" fits the differentiating-electron reading. There the one
    condition is the paper's own mechanism: orbital collapse at the first f openings.
  - The board's configuration reading is kept and computed. Under it, the condition becomes twenty conditions, eight of
    them below La.
- **For the corridor:** the condition touches no defining value (σ, the offset, G, ℓ, m), so G2 = G and m2 = m. In
  the bulk index the two positions are the same cell, and the labelling is the coordinate that tells them apart.
- **Not computed:** which physical difference makes the collapse come first.
  - M's paper reads that with c → ∞ eleven entrants change, but La, Ac and Th do not.
  - The chain data are pending bank.

## History (2026-10-11, item 220: the Löwdin bank is in the repository; no constant of the atom removes the exceptions)

- **M, item 220:** "That and all the lowdin Handoff and chat transcipts are all in the repo"
- **The chain, rebuilt (`lemmas/lowdin_replay.py`).**
  - The Löwdin walk is `nlchain.py` on the ruling scalar-relativistic HF field, with the session-48 convergence guard.
  - It is rebuilt by replaying every file operation in the 105 Löwdin chats.
  - `t7b_hf.py` reproduces the sha256 the chat printed in session 28.
  - The rebuilt step reproduces the record's rows exactly: Sc, Ac and Th at our c, and Th, La and Ac at c = 10⁶.
- **The one constant M's field enters, c = 1/α (`lemmas/madelung_field.py`).**

  | d − f gap (Ha) | c = 115 | 137.036 (ours) | 200 | 300 | 10⁶ |
  |---|---|---|---|---|---|
  | La 5d/4f | 0.139 | 0.100 | 0.049 | 0.024 | 0.003 |
  | Ac 6d/5f | 0.096 | 0.126 | 0.094 | 0.055 | 0.022 |
  | Th 6d/5f | 0.125 | 0.054 | −0.041 | −0.090 | −0.129 |

  - La and Ac stay d-elements at every scanned c (115 to 10⁶). La's gap falls nearly linearly in 1/c² (concave) to
    +2.9 mHa at c = 10⁶; Ac's falls from c = 137 upward to +22 mHa. Below c = 200 Ac's 5f is the uncollapsed
    outer-well state, so its two lowest-c gaps are a different quantity.
  - Th's restart competition flips above c ≈ 164, bracketed by computed rows at c = 160 and 170. Each c row is one step
    from the c = 137 chain's reference, not a walk at that c.
  - Below c = 115 nothing was computed.
- **No other single change in the atom does it.**
  - Local exchange (the record's own `hfs` switch) keeps Th as 6d.
  - Scaling the electron–electron coupling destroys neutrality.
  - The non-relativistic equation has no constant at all.
  - So no change of c alone, within 115 ≤ c ≤ 10⁶, does it on the mean-field chain. That does not make position 2's
    condition a different law (item 222, the board's correction). Whether the exact equation at α → 0 keeps La's
    exception is not decided: La's margin there is 2.9 mHa, and physics outside the field moves La's gap by about
    31 mHa toward 4f already at c = 137.
  - Spin-orbit, even at the paper's worst case, does not reopen it for c ≥ 137.
- **A finding about M's paper, recorded and not repaired.** The paper's relativistic clause (eleven elements
  "misplaced" with c → ∞; Figure 5) is drawn from `rt/cinf.jsonl`.
  - The record voided that walk itself, at F54.2 and F59.3: it ran at c = 137.036.
  - Its eleven are session 53's restart-versus-chained differences, borne by the reference configuration.
  - The record's live-lever walks (sessions 54 and 60) and this board's runs change one entrant: Th's.
  - The same claim stands in the live corpus, for R3 under the chat-67 hold: Register 1706, Chapter 35 of the main
    volume, and the Physics Compendium's "The twin operator, c → ∞".
- **For the corridor:** none of σ, the offset, G, ℓ or m moves. Position 2 differs in the law that sets its element
  table, which the bulk index needs as a coordinate.
