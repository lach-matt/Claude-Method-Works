# The Screening Bracket
## A testable protocol for the cold fusion question — test annex to *Cold Fusion Under a Closed Index*

**Matthew Lach** — draft v0.1, 31 July 2026, prepared with the computing collaborator
*Protocols per* The Method v1.2, Appendix B. *Every number computed before its sentence; flags carried inline.*

---

## 0. What is under test

Not "cold fusion occurs" — the lattice cannot emit that and this protocol does not smuggle it. Under test is the **conditional machine** of the companion paper, instantiated at the cell the index orders first:

> If any condensed-matter environment supplies screening at effective coordinate ≳ 10 mₑ (the Koonin–Nauenberg threshold, verified against the source), then p + d → ³He + γ proceeds at detectable rate, and every event announces itself as a 5.49 MeV monoenergetic gamma with **no neutrons**.

Both halves are measurable. The antecedent is one number per material. The consequent is one spectral line. Every outcome — including every null — is a bound (B.2.15).

## 1. Why this cell

Read off the index, nothing invented: reactant cells (1,0) and (1,1) occupied; product cell ³He (2,1) occupied and stable; Q = 5.493 MeV *(recalled; flag)*; the lowest Coulomb barrier on the chart; no particle exit channel, so the entire signature is electromagnetic — which converts the experiment from calorimetry-limited to gamma-spectroscopy-limited. The stable/fast opposition of the companion paper's §4 is paid here in rate (the γ exit is slow relative to particle exits), and bought back in sensitivity:

| quantity | value | provenance |
|---|---|---|
| events (= 5.49 MeV γ)/s per watt | 1.136 × 10¹² | computed from Q |
| ³He accumulation | 1.63 × 10⁻⁷ mol per W·day | computed |
| detection floor (0.1 γ/s detected, ε = 10⁻²) | **P_min ≈ 8.8 × 10⁻¹² W** | computed; ε nominal |
| sensitivity vs 1 mW calorimetry | 8.1 orders deeper | computed |
| screened molecular p–d baseline | ~10⁻⁵⁵ s⁻¹ per pair | KN-adjacent (*recalled; flag*) |
| enhancement required at the detection floor | **32.5 orders** (d–d needed 41.0) | computed |
| enhancement required at watt scale | 43.6 orders (d–d: 51.5) | computed |
| p + d advantage at the floor | 8.5 orders | computed |

## 2. The two routes (B.2.8 — no shared step)

**Route 1 — the line.** HPGe/scintillator spectroscopy at 5.49 MeV, a region with essentially no natural background line. Calibration chain: gamma sources only.
**Route 2 — the inventory.** ³He accumulation by mass spectrometry (and calorimetry if power reaches its floor). Calibration chain: gas standards only.
The routes share no instrument, standard, or analysis step. Agreement through Q is the claim; disagreement is a refusal (B.2.9), never a partial positive.

**Controls, built into the chemistry.** Same cell, three fills, schedule fixed in advance:
- **H₂ only** — no deuterium: predicts *no line* at any screening. The apparatus blank.
- **H₂ + D₂ (HD-forming)** — the test fill: predicts the 5.49 MeV line if and only if the antecedent holds.
- **D₂ only** — the crossover control: predicts *no 5.49 line*, and instead the d–d signature set (2.45 MeV neutrons / tritium / 23.85 MeV γ) at the d–d rate — 8.5 orders harder to reach. A 5.49 line in the D₂ fill, or d–d products in the HD fill at non-commensurate rates, is contamination or artefact, and the run is refused by pre-stated rule.

## 3. The committed-prediction sheet (B.2.13 — signed before power)

> **Run [ID] — date — signature.**
> 1. Material, loading, temperature: ____ / ____ / ____. Fill (H₂ | HD | D₂): ____.
> 2. Measured or literature screening coordinate for this material, entered **before** the run: U_e = ____ eV (source: ____), predicted rate band: ____ /s.
> 3. Predicted 5.49 MeV line intensity: ____ γ/s (or: **null predicted** — the default at every currently measured screening value).
> 4. Admissibility: line accepted only at ≥ 5σ above the fitted continuum in the 5.3–5.7 MeV window, threshold from blank series [IDs] (B.2.2).
> 5. Mandatory correlates if the line appears: ³He at 1.63 × 10⁻⁷ mol/W·day-equivalent; **zero** excess neutrons above blank; H₂ fill dark.
> 6. Disposal of every outcome, pre-stated: line + correlates → claim, submitted with raw spectra; line without correlates → route disagreement, refused, registered; null → converted to a bound per §4 and **published with sensitivity** (B.2.6).

## 4. The screening-axis program — nulls as the product

The bracket's measured anchors: mₑ (rate 3 × 10⁻⁶⁴ s⁻¹, d–d, verified to source), ~10 mₑ (the watt-scale threshold, per Koonin–Nauenberg's own statement, verified), 207 mₑ (muonic, ~10¹² s⁻¹, measured). The program fills the axis between the first two:

For each cell of the grid (material × loading × T): measure the screening potential U_e by low-energy accelerator yield — an established technique; literature values for metals run ~10²–10³ eV against ~10¹ eV atomic (*recalled; flag*) — convert to an effective coordinate and a predicted ambient rate band, run the three fills, and enter the result. A null at sensitivity s excludes enhancement η > s/r₀ **at that cell**: *attempted — condition c; excludes — η(c) above the stated ceiling; kind — upper bound.* The deliverable is the measured function η(c) over the grid — an enhancement-ceiling map where thirty-seven years have anecdotes — publishable at every cell regardless of outcome, which is the property that dissolves the stalemate ARPA-E diagnosed.

## 5. The decision table — every exit pre-stated

| observation | verdict |
|---|---|
| no line, all cells, ceilings mapped | the conditional's antecedent bounded: no tested environment reaches the coordinate; the map is the result |
| U_e measurements approach the KN threshold in some material | the antecedent becomes live for that cell; rerun with route-2 emphasis; still no occurrence claim until the line |
| 5.49 MeV line, both routes commensurate, controls clean, replicated on demand | the cell is occupied; the prediction machine fired; **this and only this** converts predicted → true |
| line without correlates, or products in the wrong fill | refusal; artefact hunt; registered |
| d–d signatures at claimed watt scale anywhere | evaluate under the companion paper §5.2 equalities — the 10¹² n/s test |

## 6. Flags (B.2.11)

Q(p,d) = 5.493 MeV and the p–d molecular baseline ~10⁻⁵⁵ s⁻¹ are recalled, unfetched; detector efficiency 10⁻² and floor 0.1 γ/s are nominal design values, to be replaced by the instrument's measured numbers on the sheet; metal screening-potential ranges recalled. None is load-bearing for the protocol's structure; all are load-bearing for its absolute sensitivities and must be pinned before run 1.

---

*The protocol predicts nothing. It is a machine that converts one measured number per material into a rate bound, and one spectral line — if the world ever supplies it — into an occupied cell. Until then its product is the map of ceilings, and a bounded silence is the first new kind of result available to this question in thirty-seven years.*
