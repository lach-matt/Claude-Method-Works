# DOCKET 66 · A2-throatbits: H-THROAT-BITS made quantitative

**Seated since (R-apply note, 2026-10-04).** DOCKET 66 wave 1 has been seated at D66-seat: `ledger.py` section 8 and O9's DOCKET 66 answer, `LEDGER.md` regenerated, a comment in `index3.py` and no index3 row. The status line below was written at D66-fix, when nothing here was seated and `ledger.py`, `index3.py`, `specthm.py`, `LEDGER.md`, `paper/` and `docket68/` were untouched; it is kept as written, as history.

**Status: a docket work item, wave 1, step 1 (one hypothesis on its own) and step 2 (the literature read at source),
2026-10-04, corrected at D66-fix the same day. Nothing is seated.** `ledger.py`, `index3.py`, `specthm.py`, `LEDGER.md`, `paper/` and `docket68/` are
untouched. The instrument is `throatbits.py`, beside this file.

`PYTHONDONTWRITEBYTECODE=1 python3 throatbits.py --selftest` runs **51 counted checks and passes all 51** in about 43 s,
most of it specthm's z3 derivation. **12 of the checks are controls**, cases built to fail that must fail. **4 checks
cannot fail and are printed STRUCTURAL, not counted:** the seat-condition text is built from specthm's verdicts; A1 and
A2 compare an owner with its own printed report; and F5 and F6 restate the authored grades. Wave 1 ran 41 checks with 9
controls.

## D66-fix: what the three verifier reports found here, and what was done

Each item was applied or answered with a computed or READ reason. Wave 1's words are kept in `throatbits.HISTORY`.

| verifier item | wave 1 first said | now | ground |
|---|---|---|---|
| V66-0 #1 (grade-moving) | R-TELEPORT O-HOLD **REMOVED-IF** {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED} in GJW's setting | **LEFT-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED} for a hold on GJW alone.** GJW's bridge becomes "slightly traversable" (p.12), "only open for a small proper time" (p.13), opening ΔV ~ h G_N/R^(D−2) (eq.(5.1)); in the teleportation reading the window is "just enough to let the single qubit Q pass through" (p.15). An opening is not a hold, as A1 grades FGM's. A **held** throat is taken from Maldacena & Qi 1804.00491 (READ): REMOVED-IF {H-GJW-COUNTERPART, H-MQ-NADS2, H-MQ-ETERNAL-COUPLING, H-MQ-LARGE-N} in nearly-AdS2, outside the board's one-space setting | GJW pp.12-15 and MQ pp.1-4, 6, 8, 18-20, 52-53 READ at D66-fix (alphaXiv) |
| V66-1 #2 (grade-moving) | N_GJW-AMBIENT: GJW p.14's one-space version, "stated, not computed" | **What Maldacena-Milekhin-Popov 1807.04726 shows (READ):** a long traversable wormhole in one asymptotically flat 4D space, no causality violation, the mouth coupling "generated automatically by the exchange of massless fields in the bulk", SM-embeddable at sub-electroweak size: REMOVED-IF {H-GJW-COUNTERPART, H-MMP, H-SM-FIELDS} at that scale, outside the board's setting by scale. **For a throat that admits the payload: LEFT-IF {H-MMP, H-SM-FIELDS}** -- MMP's binding energy equals the payload's rest energy only at r_e = 6.6e-47 m, below l_P; at r_fit a throat needs N_f ≥ 1.8e14 massless charged species (the SM has 54) and mouths ≥ 6.4e-12 m apart, 3.2e7 × 1/TeV. Outside that family: **OPEN via N_GJW-PAYLOAD** | `mmp_scales` from MMP eqs.(2.3), (5.31), (5.49), (6.50)-(6.52), (7.58), p.18, p.26; checks B10-B16 with two controls |
| V66-1 #1 (applied consistently) | R-TELEPORT O-MAKE-TOPO: NOT-BOUND-IF {H-ER=EPR} only | and **without ITE, OPEN via specthm W-create-ncc**: M's ruling M-S1A-P3 places the pathology at the throat and keeps the throat-creation classes OPEN | the ledger row |
| V66-0 #4 | R-HOLO "gives M's mechanism a precise size"; R-ISLAND "a precise sense in which geometry is compressed to binary information" | **r_fit is the radius at which the A/4 ceiling equals the payload's count, IF {H-CAP-AT-THROAT, H-NECK-DOGMA, H-COUNT-IS-ENTROPY}; no mechanism that compresses or encodes at that density is constructed or READ.** The island area term counts fine-grained entropy, not a state or an encoding (2006.06872 p.38) | wording (answer items 1 and 7; `what_it_does`) |
| V66-0 #5 | "A singular throat is a standard object in GR, so M's ruling costs GR nothing" | **Under H-SINGULAR-IS-THINSHELL** a singular throat is a standard distributional object (PV p.1), so admitting it costs GR no new structure; it still needs σ₀ < 0 (computed): the deficit is concentrated, not removed. Under H-SINGULAR-IS-PINCH: not modelled | wording |
| V66-1 #6 | the payload is 2.3e22-2.7e23 × the board's 300 l_P throat | that figure stands for the board's throat; **beside it, MMP's SM-embedded throat** (r_e ≲ 3.8e-26 m on V66-1's estimate, 2.5e19 bits) puts the payload at **~4e8-4e9 ×**; with MMP's normalisation and N_f = 54 explicitly carried, r_e ≲ 2.3-2.6e-26 m and 1e9-1.2e10 × | `mmp_scales`, `capacity_table()["mmp_SM_throat"]`; order of magnitude (H-MMP-OOM) |
| V66-1 #8 | "member-attributed removals by H-THROAT-BITS: none ... credited to the premise set, not to H-THROAT-BITS" | **none in the board's setting** (no leading REMOVED-IF in any reading, F4); **inside MQ's and MMP's settings H-GJW-COUNTERPART, M's reading, is load-bearing** in each REMOVED-IF clause, and each clause names its setting (F4b; a planted untagged clause is caught, F4c) | `setting_removals` |


`throatbits.py` imports what it uses and copies nothing:

- `docket68/measure.py`: `price_table` and `bekenstein_floor_j`.
- `docket68/geometry.py`: `qnec_price` and `r_quantum`, which take nullinfo.py's expression; `shape_checks`; and the
  D68 `GRADES` rows for ITE and ITB, quoted as their own text.
- `nopath.py`: `holographic_bits`, `bekenstein_bits` and the constants.
- `wormhole.throat_mass`, `throatmass.LARGEST_THROAT_M`, and `massform.PAYLOAD_KG` / `rest_energy_j`.
- `specthm.build` / `derive`, so the class verdicts are derived by z3 at run time.
- `ledger.RULED_BY_M`, from which M-S1A-P3's text is read and checked.

M's hypothesis itself is read from `CHARTER.md`.

## M's words, verbatim

From the ledger (M-S1A-P3, M's clarification): *"My ruling refers to the seat/destination. Singular occurs in the throat
where the geometry is compressed to binary information, and then push to the seat"*.

Carried as **H-THROAT-BITS**, a hypothesis and never a result. M's ruling is **applied**: a singular throat is not
disqualified, because the closed-causal-curve / Borde disqualifier binds at the seat only. The selftest checks that the
ledger carries the sentence (E1), that the charter carries the hypothesis (E2), and that M-S1A-P3 is ruled (E4).

## The answer, first

1. **"Compressed to binary information" has counterparts, read at source, under named readings.** The information
   that defines the 70 kg payload is between 9.5e27 and 1.1e29 bits. The spread is H-ALT made visible (measure.py).
   **r_fit = 7.40e-22 m to 2.50e-21 m** (4.6e13 to 1.5e14 Planck lengths) is the radius at which the A/(4 l_P² ln 2)
   ceiling equals that count, IF {H-CAP-AT-THROAT, H-NECK-DOGMA, H-COUNT-IS-ENTROPY}; no mechanism that compresses or
   encodes at that density is constructed or READ. *Wave 1 first said "the payload gets a definite size".* Three READ
   statements give the sense in which geometry is tied to information:
   - S_gen = Area/(4ħG_N) + S_outside (2006.06872 eq. (2.4), p.5);
   - the central dogma (p.13), which the review itself calls an unproven assumption (p.14);
   - Wheeler's bag of gold (pp.33-34): a neck whose area sets the exterior's fine-grained entropy. This is the
     nearest READ statement of information "compressed at a throat".

2. **Under H-SINGULAR-IS-THINSHELL, a singular throat is a standard distributional object, so admitting it costs GR no
   new structure -- it still needs σ₀ < 0, so the deficit is concentrated, not removed (item 3).** Poisson-Visser's
   thin-shell wormhole has a throat where the Einstein tensor "is formally singular", "a Dirac distribution". Yet the
   manifold "is geodesically complete" (gr-qc/9506083v1 p.1). Under H-SINGULAR-IS-PINCH: not modelled. *Wave 1 first
   said "M's ruling costs GR nothing".*

3. **That throat does not hold itself open.** Computed from PV's equations:
   - σ₀ < 0 for every a₀ > 2M;
   - σ₀ + p₀ = (3M/a₀ − 1)/(4πa₀√(1−2M/a₀)), so the shell's NEC fails for a₀ > 3M;
   - for every sound-speed parameter 0 < β₀² ≤ 1, no radius is stable (PV p.3, reproduced on a grid);
   - the shell's mass at M = 0 is −2a c²/G, which is **−16π × wormhole.throat_mass(a)** and −4 × M_sat; at r_fit that
     is −1.99e6 kg.

   The singular throat **concentrates** the deficit; it does not remove it. **O-HOLD is LEFT-IF
   {H-SINGULAR-IS-THINSHELL, H-PV-STATIC}.**

4. **Compression has a price in mass, given as a floor.** At the payload's own Mc², Bekenstein's bound admits the count
   only at **R ≥ 5.27e-18 m to 6.03e-17 m**. That bound is in scope there, since R_Bek exceeds the payload's
   Schwarzschild radius by more than 10⁶. To hold the count at r_fit, the least energy Bekenstein allows equals
   **exactly r_fit c⁴/(2G)**, a Schwarzschild energy (sympy identity, plus a numeric check on the owner's function).
   So **M_sat = 4.98e5 kg to 1.69e6 kg, which is 7,100× to 24,000× the payload.** This is where the two bounds meet,
   which is the board's own correction in `nopath.bekenstein_bits`. It is a floor, not a price paid, and not
   Bekenstein in scope (H-BEK-SCOPE).

5. **The QNEC price of the throat, in bits, is half the count it holds.** geometry.qnec_price gives
   |ΔS| = (1 − b′)/2 × A/(4 l_P² ln 2) over the throat sphere. For b′ = 0 that is **0.500 of the payload's count at
   r_fit**, independent of the radius. This holds under H-QNEC-OUT-OF-SCOPE and H-CONST, and it is a requirement, not a
   supply. R-QUANTUM covers **3.8e-26 to 3.3e-27** of the deficit at r_fit, under {H_flat, H-PATH, H-MIN-SCALAR}.

6. **"Then push to the seat" also has a READ counterpart under H-GJW-COUNTERPART, and in it O-BITS stands.** *(D66-repro
   residual of V66-0 #4: this heading first read "also has a precise counterpart"; "precise" dropped.)* The counterpart is
   traversable-wormhole teleportation:
   - Gao-Jafferis-Wall: a boundary coupling makes the Einstein-Rosen bridge traversable, and the qubit is sent "via the
     entanglement".
   - Maldacena-Stanford-Yang: the teleportee feels nothing special as it passes through.

   This is the nearest READ realisation of M's whole sentence. It pays with **a prior bridge plus bits pushed outside
   at ≤ c**:
   - with decoupled boundaries, no signal crosses the bulk (GJW p.4);
   - such wormholes "do not enable one to travel faster than light over long distances" (GJW p.14);
   - N_send ≲ g ≲ N_bits, a parametric bound (MSY (2.21), (2.25)).

   For the payload, under H-FAITHFUL, that means **≥ 1.9e28 to 2.2e29 classical bits**. MSY's bound does not itself
   give the factor 2; MSY p.13 says they "would like to reproduce" it.

7. **H-THROAT-BITS removes no obstruction in the board's setting, in any reading.** The selftest (F4) checks this, and
   a planted member removal is caught (F3). Its contributions are these:
   - it gives the radius and the mass at which the capacity ceiling would meet the payload's count (r_fit, M_sat, the
     QNEC price), each under its named hypotheses; no encoding at that density is shown;
   - it fixes where D68's ITB non-bindings sit (at the throat);
   - in the teleportation reading, **GJW alone gives an opening, not a hold: O-HOLD LEFT-IF {H-GJW-COUNTERPART,
     H-ADS-TFD, H-COUPLED}** (*wave 1 first said REMOVED-IF*). Held throats are READ in Maldacena & Qi (nearly-AdS2)
     and Maldacena-Milekhin-Popov (one space, sub-electroweak); each is REMOVED-IF its own premises **outside the
     board's setting**, and in each H-GJW-COUNTERPART, M's reading, is load-bearing there (F4b). Each rests on the
     coupling, which is O-BITS's channel. For a throat that admits the payload in one space: LEFT-IF {H-MMP,
     H-SM-FIELDS}, OPEN via N_GJW-PAYLOAD outside that family (`mmp_scales`).

   O-SEAT stays OPEN via N_S5, so no grade moves.

**Over-representation, both ways.** Against M, this work does not say the mechanism is impossible: a held throat of
radius r_fit is not refused by anything computed here. What is refused, in each named reading, is that the throat
removes O-BITS or O-HOLD by itself. For M, it does not say the mechanism is realised: a capacity is a ceiling, and
nothing here shows the payload can be encoded at that density (H-COUNT-IS-ENTROPY).

## (A) The payload's information (imported, measure.py)

| count (named hypotheses) | bits | classical bits if teleported as qubits (H-FAITHFUL) |
|---|---|---|
| species sequence (H-LISTED) | 9.509e27 | 1.90e28 |
| grid at 1 Å (H-GRID, H-RHO) | 4.142e28 | 8.28e28 |
| grid at 0.1 Å (H-GRID, H-RHO) | 1.088e29 | 2.18e29 |
| thermal entropy (H-THERMO, CONDITIONAL) | 2.840e28 | 5.68e28 |

A1 and A2 reproduce A3-measure.md's printed 9.509e27 and 1.088e29, read from that file. Control A3: a value off by 1 %
is not accepted.

## (B) Capacity, fit radius and the mass of compression

| count | r_fit (m) | r_fit / l_P | R_Bek at Mc² (m) | R_Bek / r_fit = M_sat / M | M_sat (kg) |
|---|---|---|---|---|---|
| species | 7.403e-22 | 4.581e13 | 5.272e-18 | 7,121 | 4.985e5 |
| grid 1 Å | 1.545e-21 | 9.559e13 | 2.296e-17 | 14,860 | 1.040e6 |
| grid 0.1 Å | 2.504e-21 | 1.549e14 | 6.031e-17 | 24,080 | 1.686e6 |
| thermal | 1.279e-21 | 7.916e13 | 1.575e-17 | 12,310 | 8.614e5 |

How these figures were obtained:

- **r_fit** is found by bisection on `nopath.holographic_bits`. It agrees with the closed form l_P √(I ln2/π) to 1e-9
  (B1). Control B2: the capacity counted in nats misses r_fit.
- **The saturation identity** is a sympy identity (B4), and it fails with the capacity in nats (control B5). Two
  further checks confirm it: `measure.bekenstein_floor_j` at r_fit equals r_fit c⁴/(2G) (B6), and R_Bek/r_fit equals
  M_sat/M (B7).
- **The density** is 1/(4 ln 2) = 0.3607 bits per Planck area.
- **The board's largest surveyed self-consistent throat** (throatmass, 300 l_P = 4.85e-33 m) holds **4.08e5 bits**.
  The payload is **2.3e22 to 2.7e23** times that (B9). The board's D67 audit marks that throat as contested by MMP, so
  **MMP's SM-embedded throat is set beside it** (D66-fix, V66-1 #6; `mmp_scales`, H-MMP-OOM):

  | MMP throat, SM-embedded (d_min(r_e) = 1/TeV) | r_e max | capacity (bits) | payload ÷ capacity |
  |---|---|---|---|
  | V66-1's estimate: g = 0.36, eq.(6.52) as printed, N_f = 1 | 3.83e-26 m (2.4e9 l_P) | 2.55e19 | 3.7e8 - 4.3e9 |
  | g′ = 0.36, MMP's normalisation g = g′/6, N_f = 54, eqs.(6.50)-(6.51)-(7.58) | 2.31e-26 m | 9.2e18 | 1.0e9 - 1.2e10 |
  | g′ = 0.46, the same | 2.55e-26 m | 1.1e19 | 8.5e8 - 9.7e9 |

  At r_fit the mouths would need d ≫ 2.7e-12 to 2.1e-11 m on V66-1's estimate (6.4e-12 to 4.9e-11 m with N_f = 54
  carried): 1e7 to 2.5e8 × the electroweak length, so beyond the SM's massless fields. And MMP p.18: an energy above
  the throat's binding energy makes a near-extremal black hole ("not safe for human travelers"); the binding energy
  ħc g² N_f²/(256π r_e) (eqs.(5.31), (7.58), the two printed forms agree, B12) equals the payload's rest energy only at
  r_e ≈ 1e-46 to 1e-48 m, far below l_P (B14). A 1 eV wave is below the binding of the SM-bound throat (B15, control).
- **Named limit, H-CAP-AT-THROAT.** Bousso's covariant bound (board: NARROWED) caps a light-sheet, meaning expansion
  ≤ 0. geometry.shape_checks computes that a flare-out throat has θ = 0 at r₀ and θ > 0 on both sides (C5), against a
  Minkowski control where θ < 0 (C6). So no light-sheet leaves the throat sphere, and Bousso gives no cap there. The
  READ route to a cap at a neck is the central dogma applied to Wheeler's bag of gold (H-NECK-DOGMA). That reading
  covers a neck that evolves into a black hole, not a throat held open.

## (C) The QNEC price, and R-QUANTUM, at r_fit

| count | \|ΔS\| over the throat sphere (bits) | ÷ count | R-QUANTUM fraction covered |
|---|---|---|---|
| species | 4.755e27 | 0.500 | 3.80e-26 |
| grid 1 Å | 2.071e28 | 0.500 | 8.72e-27 |
| grid 0.1 Å | 5.439e28 | 0.500 | 3.32e-27 |
| thermal | 1.420e28 | 0.500 | 1.27e-26 |

- The ratio is 1/4 at b′ = 1/2 (C2), and zero at b′ = 1, where the throat does not flare out (control C3).
- The R-QUANTUM fraction scales as r⁻² (C4).
- Both figures carry geometry.py's named hypotheses: H-QNEC-OUT-OF-SCOPE and H-CONST for the QNEC price, and H_flat,
  H-PATH and H-MIN-SCALAR for R-QUANTUM.

## (D) The singular throat in GR: Poisson-Visser, READ and reproduced

| check | result |
|---|---|
| D1: (13), energy conservation, re-derived from (11)-(12) with a(τ) (sympy) | holds. Control D2: with the M/a sign flipped it fails |
| D3: σ₀ < 0 for every sampled a₀ > 2M | true (PV p.3 calls σ₀ "negative", the matter "exotic") |
| D4-D5: σ₀ + p₀ in closed form; sign by a₀/M | > 0 at 2.0001, 2.5, 2.9; = 0 at 3; < 0 at 3.1 up to 10⁶ |
| D6: stability (29), 0 < β₀² ≤ 1, a₀/M in (2, 10⁴] | no stable radius (PV p.3 reproduced). Control D7: β₀² = −1 is stable for a₀/M from 5.31 up to the grid's edge; β₀² = 4 is stable for 2.19-2.59 |
| D8-D10: roots (34) and the discriminant | the transcribed roots are zeros of (29); the band lies inside them; the discriminant is real only outside (3/2 − √3, 3/2 + √3) |
| D11: shell mass at M = 0 | −2a c²/G = −16π × wormhole.throat_mass = −4 × M_sat, at three radii |

PV p.4's own caveat is carried as they state it. β₀ need not be a sound speed without a microphysical model, so
"|β₀²| > 1 should not be ruled out a priori". Stability inside PV's regions I and II is therefore **OPEN within PV's
caveat**, not refused. The other GR reading of "singular" is **H-SINGULAR-IS-PINCH**: a curvature singularity with
incomplete geodesics, the Einstein-Rosen bridge pinching off. In that reading nothing crosses the throat as matter. It
is not modelled here, and under M's ruling it is not disqualified either.

## (E) Grades of H-THROAT-BITS, in docket68/B-combine.md's vocabulary

A theorem that does not bind gives NOT-BOUND-IF, never REMOVED. Each cell below is condensed from `grades()`; the
instrument holds the full text.

| reading (premises) | O-BITS | O-MAKE-TOPO | O-MAKE-DIST | O-HOLD | O-SEAT | O-LOOP |
|---|---|---|---|---|---|---|
| **R-HOLO**: geometry at A/4 density (H-CAP-AT-THROAT, H-NECK-DOGMA, H-COUNT-IS-ENTROPY, H-ALT, H-BEK-SCOPE) | LEFT: a capacity is not a channel | OPEN via specthm W-create-ncc (OPEN). Tipler and Borde still bind; the pathology they force sits at the throat, which M-S1A-P3 (i) does not disqualify. Admitted by ruling, not shown realisable | SILENT | LEFT-IF {H-SINGULAR-IS-THINSHELL, H-PV-STATIC}, plus the QNEC price (half the count) | OPEN via N_S5 (unchanged) | SILENT |
| **R-THINSHELL**: PV's distributional throat (H-SINGULAR-IS-THINSHELL, H-PV-STATIC) | LEFT | OPEN via W-create-ncc. Cut-and-paste gives a spacetime; it does not make one | SILENT | LEFT-IF {H-SINGULAR-IS-THINSHELL, H-PV-STATIC}: σ₀ < 0, the NEC fails for a₀ > 3M, unstable for 0 < β₀² ≤ 1 | OPEN via N_S5 | SILENT |
| **R-TELEPORT**: GJW / MSY (H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED) | LEFT: GJW p.4 and p.14; MSY (2.21), (2.25) | NOT-BOUND-IF {H-ER=EPR}, which is D68's ITE grade carried in, not added; without ITE OPEN via W-create-ncc (M-S1A-P3 applied) | LEFT-IF {H-GJW-COUNTERPART, MS sec. 3.2}: the bridge is prior entanglement | **LEFT-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED} for a hold on GJW alone** (an opening, ΔV ~ h G_N/R^(D−2)). Held throats: MQ REMOVED-IF {H-GJW-COUNTERPART, H-MQ-NADS2, H-MQ-ETERNAL-COUPLING, H-MQ-LARGE-N} in nearly-AdS2; MMP REMOVED-IF {H-GJW-COUNTERPART, H-MMP, H-SM-FIELDS} at sub-electroweak scale -- both outside the board's setting, M's reading load-bearing in each. A payload-admitting one-space throat: LEFT-IF {H-MMP, H-SM-FIELDS}; outside it OPEN via N_GJW-PAYLOAD. *Wave 1: REMOVED-IF on GJW alone; N_GJW-AMBIENT* | OPEN via N_S5; B-RECV as H-INFO-SHAPE has it | SILENT (GJW p.13: no CTC) |
| **R-ISLAND**: area term and island (H-ISLAND-COUNTERPART, H-NECK-DOGMA) | LEFT-IF {H-ISLAND-COUNTERPART}: entropy, not state (p.38); decoding roughly exponential (p.33) | SILENT: replica wormholes are Euclidean saddles (p.37) | SILENT | SILENT | OPEN via N_S5 | SILENT |
| **R-ITB**: the literal reading under D68's ITB (H-ITB, N_QTOPO) | LEFT (D68 ITB) | NOT-BOUND-IF {N_QTOPO}, H-IT's | LEFT (D68 ITB) | NOT-BOUND-IF {N_QTOPO}, geometric form; the layer's own cost OPEN | OPEN via N_S5 | NOT-BOUND-IF {N_QTOPO}, for corridors |

**Removals credited to H-THROAT-BITS in the board's setting: none** (F4). Every NOT-BOUND-IF above belongs to D68's
H-IT, ITE or ITB, and is imported as geometry.GRADES' own text (F7). Every REMOVED-IF clause is a held throat outside
the board's setting (MQ: nearly-AdS2; MMP: sub-electroweak scale), and in each, H-GJW-COUNTERPART -- M's reading -- is
load-bearing in that setting (F4b, `setting_removals`).

**Seat conditions, the same in every reading.**

- **specthm's seating classes are not moved** (z3, run time): S-1 NONEMPTY, S-2 OPEN, S-3 OPEN, Rec OPEN.
- **The throat classes are not moved either:** W-create-cc, W-create-ncc and W-enlarge are all OPEN.
- **The Sturm condition is untouched.** It is sufficient, and it is stated on T_kk along a chord; H-THROAT-BITS
  supplies no T_kk at the seat.
- **M-S1A-P3 (i): the seat must be free of a CTC or Borde pathology.**
  - In R-HOLO and R-THINSHELL it is SATISFIED-IF {H-SEAT-OFF-THROAT}. PV's shell is the singular support, and the rest
    of the manifold is complete.
  - R-TELEPORT adds GJW p.13: the coupling fixes the relative time, so there is no CTC.

## Outside sources READ this pass (route recorded; short phrases, with pages)

All were read on 2026-10-04 with alphaXiv `answer_pdf_queries`, which returns open arXiv full text tagged by page; the
last two rows and GJW pp.12-15 were read at D66-fix. No paywall, login wall or 403 was met, and Firecrawl was not
needed.

| source | read | used for |
|---|---|---|
| Poisson & Visser, gr-qc/9506083v1 (board: STANDS, D67) | all 4 pages | the singular throat: p.1 (Dirac distribution, geodesically complete); eqs (11)-(13), (18)-(19), (29), (33)-(36); p.3-4 caveats |
| Gao, Jafferis & Wall, 1608.05687v3 | pp.1-5, 10, 12-15 | traversability needs the coupling (p.4); ANEC < 0 (p.10); ΔV (5.1); no CTC (p.13); fn.8 (an information limit presumed, not derived); no faster than light (p.14); teleportation reading (pp.14-15) |
| Maldacena, Stanford & Yang, 1704.05333v1 | pp.1-4, 12-14, 22-24, 36-37, 47-49 | (2.21), (2.25): information sent ≲ bits exchanged, parametric; teleportation (pp.22-23); (D.92): slightly more than 2 classical bits per qubit in classical-information Hayden-Preskill |
| Maldacena & Qi, 1804.00491v3 (D66-fix; printed page numbers) | pp.1-4, 6, 8, 18-20, 23-25, 27-28, 52-53 | an eternal (held) traversable wormhole in nearly-AdS2 with a time-independent two-boundary coupling and many bulk fields; p.19 Δ < 1/2 with alternate boundary conditions for few fields; p.52 no causality violation; Fig.23 one-space sketch and its challenges |
| Maldacena, Milekhin & Popov, 1807.04726v3 (D66-fix; READ by the board's D67 audits; printed page numbers) | pp.1-2, 4-7, 13, 16-29 | one asymptotically flat 4D space, no causality violation (abstract); coupling generated by massless bulk fields (p.4); eqs.(2.3), (5.31), (5.49), (6.50)-(6.52), (7.58); not safe for travelers (p.18); πℓ > d (p.19); SM N_f = 54 (p.26); metastable (p.27) |
| Almheiri, Hartman, Maldacena, Shaghoulian & Tajdini, 2006.06872v1 | pp.1-5, 13-14, 21-34, 37-39, 41-42 | S_gen (2.4); central dogma (p.13, an assumption, p.14); island formula (8.2); entropy, not state (p.38); decoding complexity (p.33); bag of gold (pp.33-34); replica wormholes (p.37) |

Board readings used and not re-read: Bousso hep-th/9905177 (NARROWED), the QNEC 1509.02542 (NARROWED; geometry.py),
BSST quant-ph/9904023 p.3 (measure.py H-FAITHFUL), Maldacena-Susskind 1306.0533v2 (geometry.GRADES ITE; M-RULINGS item
14), and Bekenstein quant-ph/0404042 (measure.py; NARROWED).

## Named hypotheses

| name | content |
|---|---|
| H-ALT, H-LISTED, H-GRID, H-RHO, H-THERMO, H-FAITHFUL | measure.py's, carried with each count |
| H-CAP-AT-THROAT | the A/4 capacity applies at a throat sphere. Bousso does not supply this: no light-sheet leaves a flare-out throat (computed) |
| H-NECK-DOGMA | the central dogma applied to a neck (bag of gold). READ for a neck that becomes a black hole, and "an unproven assumption" (2006.06872 p.14) |
| H-COUNT-IS-ENTROPY | the payload's defining count is what an entropy bound constrains. A capacity is a ceiling, not an encoding |
| H-BEK-SCOPE | Bekenstein holds for complete, weakly self-gravitating systems. At r_fit the holder is not such a system, so the identity marks where two bounds meet |
| H-QNEC-OUT-OF-SCOPE, H-CONST | geometry.qnec_price's |
| H_flat, H-PATH, H-MIN-SCALAR | geometry.r_quantum's (D68 R-QUANTUM) |
| H-SINGULAR-IS-THINSHELL / H-SINGULAR-IS-PINCH | the two GR readings of a singular throat: distributional and complete / curvature-singular and incomplete |
| H-PV-STATIC | PV's linear radial stability about an assumed static solution, with equal M on both sides |
| H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED | M's sentence read as traversable-wormhole teleportation; GJW's and MSY's AdS / thermofield-double setting; the coupling switched on, which is a channel between the sides |
| H-MQ-NADS2, H-MQ-ETERNAL-COUPLING, H-MQ-LARGE-N | Maldacena-Qi's premises: nearly-AdS2 (JT) gravity; the coupling on for all time; many bulk fields in the coupling (or Δ < 1/2 with alternate boundary conditions for a few) |
| H-MMP, H-SM-FIELDS, H-MMP-G, H-MMP-OOM | MMP's construction (near-extremal magnetic black-hole pair, massless charged fermions, rotation-held mouths, d_min (6.52) ≪ d ≪ q^(5/2) l_p); the SM's fields (N_f = 54, d ≪ 1/TeV); the hypercharge coupling 0.36-0.46 (MMP's normalisation g = g′/6); the order-of-magnitude reading of (6.51)-(6.52) |
| N_GJW-PAYLOAD | OPEN pathway (D66-fix): a one-space traversable throat that admits the payload, outside MMP's family with the SM's fields. *Wave 1 carried N_GJW-AMBIENT, "stated, not computed"* |
| H-ISLAND-COUNTERPART | M's sentence read as the island formula's area term |
| H-ITB, N_QTOPO | D68's |
| H-SEAT-OFF-THROAT | the throat's singular support and the seat are disjoint |
| H-INFO-SHAPE, N_S5, H-SEAT-S5 | D68's, by M's rulings items 1, 5 and 7 |

## Findings (recorded, not repaired)

1. **The thin-shell classic the task names is PV 1995, a stability paper, and not Visser's original construction.**
   PV's sec. II restates the construction, and that restatement is what is used here. Visser's own 1989 papers (PRD 39,
   3182; NPB 328, 203) are PV's refs [1] and [2], and they are NAMED-NOT-READ here: neither is on arXiv, and neither
   was sought behind a paywall. No figure here rests on them.
2. **GJW fn.8 and MSY section 2.5 give no sharp bound on the information that passes a traversable throat.** GJW
   presumes one; MSY's is parametric. A number for "bits per throat" therefore rests on the capacity reading
   (H-CAP-AT-THROAT / H-NECK-DOGMA), not on a READ traversal bound. This is OPEN.
3. **The QNEC price of a throat is a fixed fraction of its own A/4 capacity, (1 − b′)/2, at every radius.** This
   follows by algebra from nullinfo.py's expression under H-CONST. If both apply, a throat sized to hold I bits must
   carry a null entropy variation of order I. That is a coincidence of two A/4G quantities, recorded as computed and
   not read as a mechanism.

## Open

- Whether any construction holds a throat at r_fit, which would need a microphysics for β₀ (PV p.4). OPEN.
- An information bound for a traversable throat, which GJW fn.8 and MSY sec. 2.5 leave parametric. OPEN.
- A one-space traversable throat that admits the payload, outside MMP's SM-field family (N_GJW-PAYLOAD): OPEN.
  *Wave 1 listed GJW's same-space version as "stated, not computed"; MMP realises it at sub-electroweak scale.*
- H-SINGULAR-IS-PINCH (the curvature-singular reading). Not modelled.
- **Step 3 candidates** (combinations, not screened here):
  - H-THROAT-BITS (R-TELEPORT) × D68's H-SETTLE W2 × H-FRAME F1, where O-BITS is D68's one member-attributed removal,
    conditionally. Here O-BITS is what R-TELEPORT leaves.
  - R-ITB × D68's H-IT (ITB), which this work only locates.
  - R-TELEPORT × H-QET-EXOTIC (A3's), on whether the arriving information's negative energy can be the throat's
    ANEC deficit.
