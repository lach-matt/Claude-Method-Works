# DOCKET 66 · A2-throatbits: H-THROAT-BITS made quantitative

**Status: a docket work item, wave 1, step 1 (one hypothesis on its own) and step 2 (the literature read at source),
2026-10-04. Nothing is seated.** `ledger.py`, `index3.py`, `specthm.py`, `LEDGER.md`, `paper/` and `docket68/` are
untouched. The instrument is `throatbits.py`, beside this file.

`PYTHONDONTWRITEBYTECODE=1 python3 throatbits.py --selftest` runs **41 counted checks and passes all 41** in about 45 s,
most of it specthm's z3 derivation. **9 of the checks are controls**, cases built to fail that must fail. **4 checks
cannot fail and are printed STRUCTURAL, not counted:** the seat-condition text is built from specthm's verdicts; A1 and
A2 compare an owner with its own printed report; and F5 and F6 restate the authored grades.

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

1. **"Compressed to binary information" has precise counterparts, read at source, and the payload gets a definite
   size in them.** The information that defines the 70 kg payload is between 9.5e27 and 1.1e29 bits. The spread is
   H-ALT made visible (measure.py). At the holographic density, A/(4 l_P² ln 2) bits, that count fits a throat sphere
   of radius **r_fit = 7.40e-22 m to 2.50e-21 m**, which is 4.6e13 to 1.5e14 Planck lengths. Three READ statements
   give the sense in which geometry is information:
   - S_gen = Area/(4ħG_N) + S_outside (2006.06872 eq. (2.4), p.5);
   - the central dogma (p.13), which the review itself calls an unproven assumption (p.14);
   - Wheeler's bag of gold (pp.33-34): a neck whose area sets the exterior's fine-grained entropy. This is the
     nearest READ statement of information "compressed at a throat".

2. **A singular throat is a standard object in GR, so M's ruling costs GR nothing.** Poisson-Visser's thin-shell
   wormhole has a throat where the Einstein tensor "is formally singular", "a Dirac distribution". Yet the manifold "is
   geodesically complete" (gr-qc/9506083v1 p.1).

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

6. **"Then push to the seat" also has a precise counterpart, and in it O-BITS stands.** The counterpart is
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

7. **H-THROAT-BITS removes no obstruction by itself, in any reading.** The selftest (F4) checks this, and a planted
   member removal is caught (F3). Its contributions are these:
   - it gives sizes to M's mechanism (r_fit, M_sat, the QNEC price);
   - it fixes where D68's ITB non-bindings sit (at the throat);
   - in the teleportation reading, O-HOLD is REMOVED-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED}. That removal is
     credited to the premise set, holds in GJW's AdS setting only, and rests on the coupling, which is O-BITS's
     channel.

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
  The payload is **2.3e22 to 2.7e23** times that (B9).
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
| **R-TELEPORT**: GJW / MSY (H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED) | LEFT: GJW p.4 and p.14; MSY (2.21), (2.25) | NOT-BOUND-IF {H-ER=EPR}, which is D68's ITE grade carried in, not added | LEFT-IF {H-GJW-COUNTERPART, MS sec. 3.2}: the bridge is prior entanglement | REMOVED-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED}, in AdS only. Credited to the premise set, not to H-THROAT-BITS, and resting on O-BITS's channel. For one space: OPEN via N_GJW-AMBIENT (GJW p.14, not computed) | OPEN via N_S5; B-RECV as H-INFO-SHAPE has it | SILENT (GJW p.13: no CTC) |
| **R-ISLAND**: area term and island (H-ISLAND-COUNTERPART, H-NECK-DOGMA) | LEFT-IF {H-ISLAND-COUNTERPART}: entropy, not state (p.38); decoding roughly exponential (p.33) | SILENT: replica wormholes are Euclidean saddles (p.37) | SILENT | SILENT | OPEN via N_S5 | SILENT |
| **R-ITB**: the literal reading under D68's ITB (H-ITB, N_QTOPO) | LEFT (D68 ITB) | NOT-BOUND-IF {N_QTOPO}, H-IT's | LEFT (D68 ITB) | NOT-BOUND-IF {N_QTOPO}, geometric form; the layer's own cost OPEN | OPEN via N_S5 | NOT-BOUND-IF {N_QTOPO}, for corridors |

**Member-attributed removals by H-THROAT-BITS: none** (F4). Every NOT-BOUND-IF above belongs to D68's H-IT, ITE or
ITB, and is imported as geometry.GRADES' own text (F7). Every REMOVED-IF is credited to a premise set.

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

All four were read on 2026-10-04 with alphaXiv `answer_pdf_queries`, which returns open arXiv full text tagged by
page. No paywall, login wall or 403 was met, and Firecrawl was not needed.

| source | read | used for |
|---|---|---|
| Poisson & Visser, gr-qc/9506083v1 (board: STANDS, D67) | all 4 pages | the singular throat: p.1 (Dirac distribution, geodesically complete); eqs (11)-(13), (18)-(19), (29), (33)-(36); p.3-4 caveats |
| Gao, Jafferis & Wall, 1608.05687v3 | pp.1-5, 10, 12-15 | traversability needs the coupling (p.4); ANEC < 0 (p.10); ΔV (5.1); no CTC (p.13); fn.8 (an information limit presumed, not derived); no faster than light (p.14); teleportation reading (pp.14-15) |
| Maldacena, Stanford & Yang, 1704.05333v1 | pp.1-4, 12-14, 22-24, 36-37, 47-49 | (2.21), (2.25): information sent ≲ bits exchanged, parametric; teleportation (pp.22-23); (D.92): slightly more than 2 classical bits per qubit in classical-information Hayden-Preskill |
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
| N_GJW-AMBIENT | OPEN pathway: GJW p.14's same-space version, stated and not computed |
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
- GJW's same-space version (N_GJW-AMBIENT). Stated, not computed: OPEN.
- H-SINGULAR-IS-PINCH (the curvature-singular reading). Not modelled.
- **Step 3 candidates** (combinations, not screened here):
  - H-THROAT-BITS (R-TELEPORT) × D68's H-SETTLE W2 × H-FRAME F1, where O-BITS is D68's one member-attributed removal,
    conditionally. Here O-BITS is what R-TELEPORT leaves.
  - R-ITB × D68's H-IT (ITB), which this work only locates.
  - R-TELEPORT × H-QET-EXOTIC (A3's), on whether the arriving information's negative energy can be the throat's
    ANEC deficit.
