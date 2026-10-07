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
| O | O3 the corridor survives its hold: 2π²/ln2 = 28.4777 clocks for every N; growth ≤ 20.8 | **reading**, o3_hold.py: H-ONE-STEP-PER-BIT, H-HOLD-AT-BOUND; the hold exceeds the local bulk's span, so it also leans on B4 |
| Z | Z1 5D null energy zero along the passage; deficit = bulk pull | **proved**, passage5d.py P2 |
| Z | Z2 the integral equals the plane's reading on both legs | **proved**, passage5d.py P3, coin.py |
| Z | Z3 null energy never violated | **derived**, axioms.py: bulk R(k,k) = 0, passage 0 (Z1), composite ≥ 0 (B5a, so it inherits B5's reading) |
| B | B1 plane matter-free; Gauss and Codazzi met | **proved**, localbulk.py |
| B | B2 a local vacuum bulk exists, unique among analytic ones | **proved**, localbulk.py |
| B | **B3 a complete bulk exists, under closed-index criteria** | **OPEN**, equivalent to B4a with B4b and B4c |
| B | B4a the global bulk's shape: two separate positions reached through a dimension (152 (1)) are one end of the bulk; CGS Thm 3.5's deformation; topology fixed before the opening | **proved** (STRUCTURAL), given W2 inside T, b4_global.py |
| B | B4c the far boundary untrapped, uniformly in time | **reading**, b4_global.py: in the board's model T exists beyond the hold's reach iff ℓ > 2R_reach (≈ 57 m, corridor units); H-WEAK-RADIATION, H-NEAR-ZONE |
| B | **B4b the bulk regular through the hold (152 (2), a brief evolution)** | **OPEN**, b4_regular.py: necessary, the static local bulk regular within the hold's double cone, ~1.9–2.2 m deep at r = 2.05m and ~8.2 m at r = 3m (ℓ ≫ r₀); series-stable to 1.5 m and 2.25 m |
| B | B5 positivity for the entangled pin, at every point | **reading**, b5_positive.py: H-SHARED-PROFILE, H-PIN-IS-COINCIDENCE |
| B | B6 k's ratio fixed by the work, k_R = 3k_L/4; every clause b6_k.py checks free of k's scale — **not B4**, whose depth and far boundary depend on ℓ | **proved**, b6_k.py, kderive.py K3 — narrowed twice |
| B | B6′ k's scale | **nature**, item 136 answer 8 |
| B | B7 formation: the widening of a preexisting bridge, consistent and safe; 5D evolution with B4 | **reading**, b7_formation.py: H-BRIDGE-PREEXISTS; Maldacena–Susskind p.17 READ |
| I | I1 the passage is N bits of entanglement | **derived**, axioms.py: Maldacena–Susskind p.5 READ; extremal case H-EXTREMAL-ENTROPY, READ for a class (Strominger–Vafa) and carried to the corridor by the board |
| I | I2 the README within the capacity bound as READ | **proved**, i2_capacity.py |
| E | E1 E carried through three holds into position 2 | **derived**, axioms.py: 115 (c), 136 G, O1, 136 answer 3, 109, conservation (z3, with controls) |
| E | E2 released at position 2 at the closing | **derived**, axioms.py: 106, 109, 115 (b) |
| E | E3 the ledger closes | **reading**, ledger.py: reading (a) (see below) |
| E | E4 the field energy outside the neck, E/4: the bulk's Weyl field read on the plane, positive | **proved**, ledger.py; Maartens–Koyama eq. 143 |
| R | R0 the read: the corridor takes the README at its opening; N read from the object | **definition**, items 70, 101 answer 8, 115 (c), 130 (2); consistent with I2b |
| R | R1 exact reconstruction, no tolerance | **definition**, items 145, 146; consistent with R3, R5c |
| R | R2 position 2 rearranges to the README; then its laws govern | **definition**, item 148; consistent with rearrange.py, E3 |
| R | R3 exactness at the instant over the mass window | **proved**, exactcopy.py, rearrange.py |
| R | R4 the corridor's length as the trajectory difference, given a measure (not a distance) | **reading**, r4_length.py: H-LENGTH-AS-DIFFERENCE |
| R | R5 the build's mechanism | **reading**, r5_build.py: the mechanism yours; the fields the board's reading of 148 under 149 |

- **The count:** 33 lemmas. **14 proved, 6 derived, 3 definitions, 7 on the board's readings, 1 a measurement, 2 OPEN**
  (B3 and B4b, one lemma in effect). warptheorem.py prints it from its list; selftest 8/8.
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

- **Open:** B4b, the bulk regular through the hold. It carries B3, closes formation and the address with B4a and B4c,
  and bears on the hold (O3d). See lemmas/B4.md.
- **On the board's readings, each labelled and withdrawn if you correct it:** O3, B5 (and Z3 through it), B7, B4c, E3,
  R4, R5.
- **Caveats the board can clear:** I1's extremal step, READ for a class only; the duration quantum inequality (old wall
  D7), not yet re-run against Z3.
- **A measurement, by your ruling:** B6′, k's scale.
- **Verification:** none of the nine lemma instruments, axioms.py or warptheorem.py has had a verifier.
- The chain map (chainmap.html, published as the Warp Chain Map) shows which station each lemma decides.

## Named hypotheses

- **Yours:** M-ONE-THEOREM (150), M-PROVE-EVERY-LEMMA (151), and the rulings each derived lemma is derived from.
- **The board's:**
  - reading your item 152 (1) as CENSOR5D's escape (a), encoded as one end (B4a);
  - H-FAR-MODEL, H-WEAK-RADIATION, H-NEAR-ZONE (B4c); H-GLUING (B4b's sufficiency);
  - reading (a) for E3;
  - H-ONE-STEP-PER-BIT, H-HOLD-AT-BOUND (O3); H-SHARED-PROFILE, H-PIN-IS-COINCIDENCE (B5); H-BRIDGE-PREEXISTS (B7);
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

