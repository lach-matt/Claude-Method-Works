# DOCKET 66 · A3-qet: H-QET-EXOTIC — does information arriving where it was absent make exotic matter?

**Status: a docket work item, wave 1, 2026-10-04, corrected at D66-fix the same day. Nothing is seated.** `ledger.py`, `index3.py`, `specthm.py`,
`LEDGER.md`, `paper/` and `docket68/` are untouched. The instrument is `qet.py`, beside this file.

`PYTHONDONTWRITEBYTECODE=1 python3 qet.py --selftest` runs **47 counted checks and passes all 47** in about 48 s.
Most of that time is specthm's z3 derivation. **10 of the checks are controls**: cases built to fail, which must fail
(wave 1: 45 checks, 9 controls).
**2 items cannot fail.** They are printed STRUCTURAL and not counted: the grade text is built from imported figures, and
R-LIT's SILENT is assigned. `python3 qet.py` prints the report and `--json` prints its numbers.

**Board figures are imported, never retyped:**
- `achievable.duration_bound`, `FEWSTER_C`, `HBAR`, `C_SI`
- `wormhole.throat_mass`, `G`
- `geometry.r_quantum` (D68 R-QUANTUM)
- `measure.H`, `LN2`, `landauer_j`, `bekenstein_floor_j`
- `massform.PAYLOAD_KG`
- `phase1.L_PROXIMA`
- `transit.BEATS_LIGHT`
- `specthm.build` / `derive` (z3, at run time)
- `ledger.RULED_BY_M` (M-D65-1, read as text)

## D66-fix: what the three verifier reports found here, and what was done

Each item was applied or answered with a computed or READ reason. Wave 1's words are kept in `qet.HISTORY`.

| verifier item | wave 1 first said | now |
|---|---|---|
| V66-0 #6 | item 3: under R-QET the result is "genuine negative energy density ... 'exotic matter' in the standard sense" | **a local negative energy density (pointwise WEC violation), which the review calls a pathway to exotic matter (p.26).** FMM's abstract says "violate energy conditions and have negative local stress-energy densities", not "exotic matter"; the negative density is offset by positive energy elsewhere (FMM p.3); the protocol obeys the quantum energy inequalities (check C6; FMM p.11); it is not the averaged (ANEC) violation a throat needs (GJW p.2), so O-HOLD stays LEFT-IF at 2.08e-68. R-QET's TRUE-IF stands |
| V66-0 #7 | O-HOLD "OPEN on the ξ > 0 branch via N_QET-NMC" | **N_XI and N_QEIC are the board's R-QUANTUM pathways, present with or without QET; QET's own OPEN pathway is N_QETHAD.** H-QET-HADAMARD is a short check, not a hard open question: the post-protocol state is a finite mixture of finite superpositions of Weyl-displaced vacua with smooth smearings, whose two-point function is, by the standard argument, the vacuum's plus a finite sum of products of smooth classical solutions. That check is **not run here, so OPEN** |
| V66-1 #7 | R-LIT labelled "M's sentence alone" | **R-LIT is the question's parenthetical read as arrival alone** ("information arriving at the destination creates ..."). M's words are "the introduction of information into a space that never previously contained it": "introduction" is an act, and A3 itself says what the destination never contained was the classical record. M's sentence read operationally is **R-QET, TRUE-IF {H-GROUND, H-CORR, H-ACT, H-INSTANT}**. No verdict word changes |
| V66-2 #4 | t* = 0.1450/k at (1.5, 1) and 0.1855/k at (1, 1) | **0.1449/k and 0.1854/k** (bisection: t* k = 0.144942 and 0.185375; V66-2's independent bisection: 0.144941 and 0.185373). Wave 1 printed the first grid point at or above zero; there ⟨H_B + V⟩ is 1.1e-4, not 0 (check A15c, control) |
| V66-2 #5 | E_B = 0.1425 h, E_A = 1.2481 h, 0.494 h per nat, 0.2036 h per bit, E_B = −0.079 h | **the raw model values at (h, k) = (1.5, 1)**: E_B = 0.14252 (E_B/h = 0.0950), E_A = h²/√(h²+k²) = 1.2481 (E_A/h = 0.832); the per-nat and per-bit figures are in the same raw unit. The numbers were right; the unit word was not |
| V66-2 #6 | Hotta 1002.0200v2: "even before the start" p.3, eq.(8) p.7 | **printed p.2 and p.8** (re-read at D66-fix). This file now cites 1002.0200v2 by printed page numbers throughout: eqs (1)-(3) p.3, (4) and (5) p.5, (8) p.8, (9) p.11, (10) p.10, (12) p.12, (15) p.14 |

`signed.py` is not used. QET's negative quantity is an energy density, not a probability weight. A3-measure already
keeps the two apart (H-NEGWEIGHT-NEC: "a negative weight is not a negative T_ab k^a k^b").

## M's words, and what was tested

M (ledger M-D65-1, verbatim): *"consider the idea that the introduction of information into a space that never
previously contained it would be considered exotic matter"*. This is carried as **H-QET-EXOTIC**, a hypothesis.

The ledger records that the question's parenthetical was only the question's description as put to M, NOT READ. The
parenthetical reads: "information arriving at the destination creates a local negative-energy region there". It is
tested here against the sources.

Two readings are graded:
- **R-QET**, the operational reading. A bit from Alice's measurement arrives at the destination. A local operation
  there, conditioned on that bit, acts in an entangled ground state. The question is whether this leaves a local
  negative-energy region.
- **R-LIT**, the question's parenthetical read as arrival alone. Information arrives, with no conditioned operation and
  no prior correlation. *Wave 1 labelled this "M's sentence read alone". M's sentence names an act ("introduction"),
  and read operationally it is R-QET (V66-1 #7).*

## The answer, first

1. **The arrival of information creates no negative energy by itself.** In Hotta's minimal model, take the state after
   Alice's measurement with the bit delivered. Before Bob acts, the local energy at the destination is **0** (|.| <
   1e-12, check A10). Hotta finds the same in the field: the state around Bob is a "local vacuum" right before his step
   (0803.2272v3 p.14).
   - The negative region is made by **Bob's operation conditioned on the bit**. It exists only when four conditions hold
     together:
     - the shared state is a ground state (H-GROUND);
     - it is entangled across the two sites (H-CORR);
     - Bob acts (H-ACT);
     - he acts fast against the system's own dynamics (H-INSTANT).
   - So the parenthetical as put to M is **inexact**. R-QET is **TRUE-IF {H-GROUND, H-CORR, H-ACT, H-INSTANT}**.
2. **R-LIT is FALSE-IF {H-MINIMAL or H-1+1 as the test models, linear QM}.** Three counterexamples are computed:
   - the bit arrives and nothing is done: the local energy is 0 (A10);
   - the bit arrives with no ground-state correlation (k = 0): the best conditioned operation extracts 0 (A11);
   - the bit is uncorrelated with B (a channel at ε = ½): E_B = 0 (B2), and a fixed operation then costs energy (B3).

   The same one bit also yields **3×** the energy when (h, k) is tripled (B5). **Information fixes no amount of energy,
   of either sign.** What the destination "never previously contained" was the classical record. The correlation was
   already there: Hotta places the extracted energy at B "even before the start" (1002.0200v2 p.2). This grades the
   parenthetical's arrival-alone reading, not M's sentence, which read operationally is R-QET (item 1).
3. **What M's reading gets right**, stated with equal weight:
   - Under R-QET the result is a **local negative energy density** (a pointwise WEC violation), which the review calls
     a pathway to exotic matter (2505.04689v3 p.26; FMM's abstract: "violate energy conditions and have negative local
     stress-energy densities"). It is offset by positive energy elsewhere (FMM p.3), it obeys the quantum energy
     inequalities (C6; FMM p.11), and it is not the averaged (ANEC) violation a throat requires (GJW p.2) -- so O-HOLD
     stays LEFT-IF (item 7). *Wave 1 first called it "'exotic matter' in the standard sense" (V66-0 #6).*
   - **It needs the information.** Without the bit no operation at B extracts anything (Hotta eq.(5); check A6, minimum
     change ≥ 0).
   - **It grows with the information.** Through a noisy channel E_B rises monotonically with the mutual information
     I(μ; μ′), and is 0 at I = 0 (B1, B2).
   - The sources read QET as the operational route that **saturates** the quantum-interest scaling (FMM p.11). The
     scaling law is reproduced exactly (C8, C10).
4. **Magnitude.** Every bound computed or READ holds:
   - The negative energy is bounded by the energy Alice injected: E_B ≤ E_A (Hotta 1002.0200v2 p.2; review p.6). In the
     minimal model **E_B/E_A < 1/4** for every k/h; the ratio approaches 1/4 as k/h → ∞ (A13).
   - It is bounded by the entanglement consumed, Hotta's eqs (12) and (15) (A18).
   - In the field it is bounded by the quantum energy inequality. The computed 1+1 QET flux reaches **0.071** of
     Flanagan's bound (C6). The same test fails at **496×** the bound when the QET term is inflated ×10 (C7).
5. **Duration.**
   - Minimal model: after Bob's step the destination's local energy stays negative for **t\* = 0.1449/k** at (h, k) =
     (1.5, 1), and **0.1854/k** at (1, 1), by bisection (A15, A15b). Then Alice's energy arrives through the coupling.
     *Wave 1 printed the grid values 0.1450 and 0.1855.*
   - 1+1 field: the well travels at c just behind Alice's positive pulse. A fixed observer sees it for its width. At a
     smearing width of 1 m that is **1.42 ns**, carrying **−2.57e-28 J** (H-1+1, H-GAUSS).
6. **Timing against light.** QET needs the bit, so Bob's step at the destination comes after the light time:
   - B's reduced state is unchanged by Alice's measurement (no-signalling, 1.4e-17, A8);
   - FMM's Bob "only receives the information ... when he enters the lightcone of Alice" (p.3);
   - Hotta's Bob acts only after Alice's wavepackets have passed him (0803.2272v3 p.11);
   - at Proxima that is ≥ **4.2465 yr** (`phase1.L_PROXIMA`), and `transit.BEATS_LIGHT` is False (D3).

   QET's speed advantage in the literature is over the slow *internal* energy diffusion of a non-relativistic medium
   (1/k; Ikeda p.2, p.4). It is not an advantage over light.
7. **O-HOLD (the 1 m throat).** **LEFT-IF {H_flat, H-PATH, H-MIN-SCALAR, H-QET-HADAMARD}.**
   - The states QET makes are states of the free field, so the duration bound binds them as it binds any state.
   - The fraction of the 1 m throat's deficit (4.8155e42 J) that the bound can cover is **2.08e-68**
     (`geometry.r_quantum`), and **QET does not move it**.
   - QET's own OPEN pathway is **N_QETHAD**: H-QET-HADAMARD unchecked -- a short check by the displaced-vacuum
     argument, not run here. The ξ > 0 and curved-space branches are the **board's** R-QUANTUM pathways (N_XI, N_QEIC),
     present with or without QET, not QET's. *Wave 1 first said "OPEN on the ξ > 0 branch via N_QET-NMC".*
   - Under ITB the geometric form is NOT-BOUND-IF {N_QTOPO}. That is the board's grade; QET adds nothing to it.
   - **QET removes nothing.**
8. **O-SEAT.** **LEFT-IF {H-QET-BUDGET, H-MINIMAL for the ratio}**, as a supply route.
   - QET relocates at most the energy injected at the source, gated by a bit travelling at ≤ c, and it forms no
     substance.
   - A 70 kg payload's rest energy (6.2913e18 J) would need more than 2.52e19 J injected at the source under H-MINIMAL.
   - Read with M's "from the seat", Hotta's location of the energy fits: it comes out of the seat's own zero-point
     fluctuation. But it is borrowed. The seat is left at −E_B until Alice's positive energy arrives.
   - **The board's O-SEAT stays OPEN via N_S5. No grade moves.**

## (A) Hotta's minimal model, computed

The model is Hotta 1002.0200v2 eqs (1)-(3), the same as Ikeda 2301.02666v5 eqs (1)-(3):

H = hσ_z^A + hσ_z^B + 2kσ_x^Aσ_x^B, plus constants chosen so that the ground state has zero mean energy in every term
(A1).

The protocol has three steps:
1. Alice measures σ_x^A.
2. The bit μ is sent.
3. Bob applies R_Y(2μφ), with cos 2φ = (h²+2k²)/R and sin 2φ = hk/R (Ikeda eqs (10)-(12)).

| (h, k) | E_A | ⟨V⟩ | ⟨H_B⟩ | local energy at B = −E_B | E_B / E_A |
|---|---|---|---|---|---|
| (1, 0.1) | 0.9950 | −0.0193 | 0.0145 | −0.0049 | 0.0049 |
| (1, 0.2) | 0.9806 | −0.0701 | 0.0521 | −0.0180 | 0.0184 |
| (1, 0.5) | 0.8944 | −0.2599 | 0.1873 | −0.0726 | 0.0811 |
| (1, 1) | 0.7071 | −0.3746 | 0.2599 | −0.1147 | 0.1623 |
| (1.5, 1) | 1.2481 | −0.4906 | 0.3481 | −0.1425 | 0.1142 |

**Against Ikeda's tables.** All 20 of Ikeda's analytic Table II values (p.11) are reproduced within one unit of the last
printed digit (A2). They are not reproduced to 4-decimal rounding, for two reasons:
- the table truncates in places (for example ⟨V⟩(1, 0.5) = −0.259893 is printed −0.2598);
- its (1.5, 1) ⟨V⟩ = −0.4905 equals its own printed E_1 − H_1, against −0.490600 computed.

This is a reading note on the fixture, not a finding against Ikeda.

**Against Hotta's eq.(8).** E_B with Ikeda's φ equals Hotta's eq.(8) (A4). A numeric maximum over **every**
μ-dependent SU(2) operation on B, from 12 BFGS starts, equals eq.(8) to 1e-7 (A5). Ikeda's rotation is therefore the
optimum.

**The entanglement exchange.** Alice's POVM is Π(μ) = ½(1 + μrσ_x).
- At projective r = 1, ΔS_AB = 0.28837 nats and E_B = 0.14252 (raw, at (h, k) = (1.5, 1)), which is **0.494 per nat
  consumed** in the same raw unit (0.329 h per nat). *Wave 1 wrote these with the unit "h".*
- At r = 0.05 the ratio is 0.00037 / 0.00055.
- Both of Hotta's inequalities hold on the whole family (A16-A18). Eq.(12) with its coefficient ×1.5 fails at small r,
  where it is tight (A19, control).

## (B) The information-to-energy exchange rate

Alice's bit is sent through a binary symmetric channel with flip probability ε, at (h, k) = (1.5, 1). Bob re-optimises
φ. The numeric E_B equals Hotta's eq.(8) with q/p = 1 − 2ε at every ε (B1):

| ε | I(μ; μ′) bits | E_B (raw, at (h, k) = (1.5, 1); wave 1 headed this column "E_B / h") |
|---|---|---|
| 0 | 1.0000 | 0.14252 |
| 0.11 | 0.5001 | 0.08770 |
| 0.30 | 0.1187 | 0.02338 |
| 0.45 | 0.0072 | 0.00147 |
| 0.50 | 0 | 0 |

Two rates follow:
- **dE_B/dI at I → 0 = ln 2 · h²k² / ((h²+2k²)√(h²+k²)) = 0.2036 per bit** (raw; 0.1357 h per bit). The closed form
  was derived here and is checked numerically at ε = 0.4999 (B4).
- **At I = 1 bit, E_B = 0.1425** (raw; E_B/h = 0.0950).

**The rate has no universal value in joules.** It carries the system's energy scale h (B5). One bit is neither
kT ln 2 nor the Bekenstein floor of anything.
- The board's figures for one bit are context only, with no theorem relating them to E_B: `measure.landauer_j(1, T_CMB)`
  = 2.61e-23 J and `measure.bekenstein_floor_j(1, 1 m)` = 3.49e-27 J.
- **A noisy bit used as if clean costs energy.** With φ not re-optimised, ε = 0.4 gives E_B = −0.079 (raw; B3, control).
  Information that is wrong is worse than none.

## (C) The field: 1+1 QET, computed

The energy density is the review's eq.(116) (2505.04689v3 p.21), which restates FMM's eq.(11) and eq.(7).
- It is computed with Gaussian smearings: FMM's case 2, H-GAUSS.
- The principal-value integral is in closed form through Dawson's function, checked against Cauchy quadrature (C1).
- Alice's width is 1. Bob's smearing has width 0.1, centred on Alice's outgoing pulse at T = 10.
- Causality is checked on a 4-width effective support (C5, H-EFF-SUPPORT).
- Bob's coupling is optimised for the deepest well.

**Results** (ħ = c = 1, unit = Alice's width; H-1+1):
- Well depth −0.02927, at the pulse centre (C2).
- Integrated negative energy −0.00812.
- Width 0.427.
- Total field energy +0.2174 ≥ 0 (C4).
- **Erase Alice's information (⟨σ_y⟩ = 0) and the density is ≥ 0 everywhere** (C3, control). This is the field version
  of "the bit is necessary".
- **Flanagan's 1+1 QEI**, right-moving sector (gr-qc/9706006v2 eq.(2.5) p.2: ∫f T_vv ≥ −(1/48π)∫f′²/f). It holds on every
  Gaussian sampler tried, at most **0.0713** of the bound, at width 0.224 (C6; H-SAMPLER: a pass is necessary, not
  sufficient). The cross-term inflated ×10 violates it at 496× (C7). The test can fail, and the real state does not.
- **FMM's scaling law (34)-(36), n = 2.**
  - ρ_Υ(x) = Υ²ρ_1(Υx) holds to 5e-15 at Υ = 2 and 3 (C8). The wrong amplitude exponent breaks it (C9, control).
  - Under Υ = 2 the integrated negative energy doubles and the width halves, so E × width is invariant (C10).
  - That is FMM's Δx ∝ 1/ΔE (p.11): **arbitrarily large negative energy only in an arbitrarily thin, short region.**

**In SI**, at a 1 m smearing width: −2.57e-28 J, seen at a point for 1.42 ns.

**Context, not a bound (H-1+1-TO-3+1):** −2.57e-28 J is **5.3e-71** of the 1 m throat's 4.8155e42 J. The bound that
grades O-HOLD is the 3+1 duration bound in (E), not this ratio.

## (D)-(E) Board figures imported

| figure | value | owner |
|---|---|---|
| 1 m throat deficit | 4.8155e42 J | `wormhole.throat_mass(1)·c²` (D1) |
| fraction covered by the duration bound at T = r0/c | 2.081e-68 | `geometry.r_quantum` (D2) |
| required / allowed density | 4.8155e42 Pa / 1.002e-25 Pa | `geometry.r_quantum` |
| light time to Proxima | 4.2465 yr | `phase1.L_PROXIMA` (D3) |
| BEATS_LIGHT | False | `transit` (D3) |
| 70 kg rest energy | 6.2913e18 J | `massform.PAYLOAD_KG` |

## Grades (B-combine vocabulary; a theorem that does not bind gives NOT-BOUND-IF, never REMOVED)

| reading | O-BITS | O-MAKE-TOPO | O-MAKE-DIST | O-HOLD | O-SEAT | O-LOOP |
|---|---|---|---|---|---|---|
| **R-QET** (TRUE-IF {H-GROUND, H-CORR, H-ACT, H-INSTANT}); M's sentence read operationally | **LEFT**: the bit is required (A6, A8, C3) | **SILENT** | **SILENT**: consumes existing correlation (ΔS_AB > 0) and distributes none | **LEFT-IF** {H_flat, H-PATH, H-MIN-SCALAR, H-QET-HADAMARD}, ≤ 2.08e-68 of the 1 m deficit; QET's own **OPEN** pathway N_QETHAD (H-QET-HADAMARD unchecked, a short check); N_XI / N_QEIC are the board's R-QUANTUM pathways, not QET's; NOT-BOUND-IF {N_QTOPO} under ITB (board's, unchanged) | **LEFT-IF** {H-QET-BUDGET} as a supply route; the board's OPEN via N_S5 unchanged | **SILENT**: causal, closes no loop |
| **R-LIT**, the parenthetical's arrival-alone reading (FALSE-IF {test models, linear QM}) | SILENT (its operative content is R-QET's) | SILENT | SILENT | SILENT | SILENT | SILENT |

**Nothing is REMOVED and nothing reads NOT-BOUND-IF as QET's own** (check E7).

**Seat conditions**, the same in both readings:
- **specthm's seat classes are not moved** (z3, run time): S-1 NONEMPTY, S-2 OPEN, S-3 OPEN, Rec OPEN.
- **The Sturm condition is untouched.** It is sufficient and needs T_kk large and *positive* along a chord. QET supplies
  *negative* T_kk, so it can only lower the left-hand side. It certifies no seating and refuses none.
- **M-S1A-P3 (i): SATISFIED-IF {H-FLAT-QFT}.** QET is a protocol of Minkowski QFT whose step at the seat follows the bit,
  so it introduces no closed causal curve and no Borde pathology there.

**Combination, named and not screened** (charter step 3 belongs to the combine stage):
- **R-QET × H-THROAT-BITS / H-INFO-SHAPE**: bits pushed to the seat and used there for QET extraction.
- This needs the seat's vacuum to be correlated with the source measurement (H-CORR). It would supply at most E_A, and
  the bit still travels at ≤ c.
- Status: OPEN, not computed.

## The literature, READ at source (route: alphaXiv `answer_pdf_queries`, open arXiv PDFs, 2026-10-04; no paywall, no login wall, no 403)

| source | version read | what was taken (page) |
|---|---|---|
| Hotta, *Quantum Measurement Information as a key to Energy Extraction from Local Vacuums* (= PRD 78 045006; the "Hotta 2008" named to M) | arXiv:0803.2272**v3**, 16 Jul 2008 | 1+1 scalar protocol; Bob acts after Alice's wavepackets pass (p.11); ⟨H_B⟩ = −η²/2ξ eq.(25) (p.14); local vacuum before Bob's step (p.14); eq.(10) (p.9); classical channel bounded by light (p.2). Hotta's spin-chain paper arXiv:0803.0348 is cited there and **not READ** |
| Hotta, *Energy Entanglement Relation for QET* (the minimal model) | arXiv:1002.0200**v2**, 25 Jun 2010 (printed page numbers; re-read at D66-fix) | eqs (1)-(3) p.3, (4) p.5, (5) p.5, (8) p.8, (9)-(10) pp.10-11, (12) p.12, (15) p.14; E_B bounded by E_A (p.2); energy "at B even before the start" (p.2). *Wave 1 cited (4) p.4, (8) p.7 and "even before the start" p.3* |
| Funai & Martín-Martínez, *Engineering negative stress-energy densities with QET* | arXiv:1701.03805**v2**, 19 Mar 2025 | couplings eqs (1)-(2) p.2-3; eq.(7) p.3; light-cone condition p.3; well between positive peaks, none ahead for a massless field (p.7); scaling (34)-(36) and quantum interest (p.11) |
| Ikeda, *Demonstration of QET on Superconducting Quantum Hardware* | arXiv:2301.02666**v5**, 22 Aug 2023 | minimal model eqs (1)-(14) p.2-3; Table I p.6, Table II p.11 (fixtures); eqs (A7), (A9), (A10)-(A12) p.10; timescales p.2, p.4 |
| Ragula & Martín-Martínez, review | arXiv:2505.04689**v3**, 11 Jul 2025 | minimal QET p.4-6 (E_B ≤ injected energy, p.6); eq.(116) p.21 (the density computed here); scaling (135)-(137) p.26; QET as an "operational pathway" to exotic matter (p.26) |
| Zachary, *Entangled Quantum Negative Energy Teleportation as a Probe of Semiclassical Gravity* | arXiv:2506.19878**v1**, 23 Jun 2025 | eq.(3) p.5 is a Gaussian *model*, not derived from a protocol; App. B.4 p.25 "We assume a fiducial energy scale"; eqs (A.3) p.23 and (B.2) p.25 carry opposite signs; QIX-C "do not enable superluminal travel" (p.20) |
| Flanagan, *Quantum inequalities in two dimensional Minkowski spacetime* (read to grade the field state) | arXiv:gr-qc/9706006**v2**, 16 Jul 1997 | eq.(1.8) p.2; right-moving eq.(2.5) p.2; minimiser a squeezed vacuum (p.4) |

**A computed finding about 2506.19878** (check D4):
- Its own eq.(B.3) with c restored, 8πGε/c⁴ at ε = 1e-11 J/m³, gives **2.08e-54 m⁻²**.
- It prints δR_peak ~ 1e-36 m⁻², which is **4.8e17×** larger. Dropping one c² gives 1.87e-37 s⁻², which is the wrong
  unit.
- The paper states no unit convention for App. B (H-UNITS-2506), so this is recorded as a non-reproduction, not as a
  ruling on the paper.
- Its numbers are assumed rather than derived from a QET protocol, so **no grade here rests on 2506.19878**.

## Named hypotheses

H-MINIMAL, H-PROJ, H-INSTANT, H-GROUND, H-ACT, H-CORR, H-1+1, H-GAUSS, H-EFF-SUPPORT, H-DELTA-SWITCH, H-SAMPLER,
H-QET-HADAMARD, H_flat, H-PATH, H-MIN-SCALAR (D68 R-QUANTUM's), H-QET-BUDGET, H-1+1-TO-3+1, H-FLAT-QFT, H-UNITS-2506.

QET's OPEN pathway is N_QETHAD (B-combine66's name; H-QET-HADAMARD unchecked). Wave 1's N_QET-NMC is the board's
R-QUANTUM pathway N_XI. N_QTOPO and ITB are D68's. Each is defined in `qet.py`'s header.

## OPEN, unchecked

- **QET in 3+1.** FMM eq.(23) is READ and not computed. The 3+1 duration bound is applied through `geometry.r_quantum`,
  on H-QET-HADAMARD.
- **H-QET-HADAMARD itself (N_QETHAD).** A short check, not a hard open question: finite mixtures of finite
  superpositions of Weyl-displaced vacua with smooth smearings have two-point functions equal to the vacuum's plus a
  finite sum of products of smooth classical solutions. Not run here, so OPEN.
- **QET with a nonminimally coupled field.** That branch, and the curved-space one, are the board's R-QUANTUM pathways
  (N_XI, N_QEIC), present with or without QET; wave 1 listed it as QET's "only OPEN branch" (N_QET-NMC).
- **Field QET at interstellar separation.** In Hotta's 1+1 eq.(37), E_B depends on null separations (x − y ± T). The
  dependence on distance in 3+1 is not computed.
- **The combinations with H-THROAT-BITS and H-INFO-SHAPE**, which belong to the combine stage.
- **Hotta arXiv:0803.0348** (spin-chain QET), cited, not READ.

## Adversarial notes (both directions, for the verifiers)

- **Against M, possibly over-stated here:** "R-LIT FALSE" rests on the two test models (minimal, 1+1 Gaussian) and on
  linear QM. A different formalism of "information in a space" is not excluded. That is why the grade is FALSE-IF, not
  FALSE.
- **For M, possibly under-stated here:**
  - QET really is the cleanest operational route to WEC-violating states in these sources, and the information really
    is necessary and really scales the yield. The grades say so (R-QET TRUE-IF; LEFT, not refuted, on O-HOLD).
  - M's own sentence names an act ("introduction"); read that way it is R-QET, and TRUE-IF. The FALSE-IF belongs to the
    parenthetical's arrival-alone reading (D66-fix, V66-1 #7).
  - The fraction 2.08e-68 is the board's bound under named flat-space, minimal-scalar hypotheses, not a measurement of
    QET.
