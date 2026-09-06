# The Screening Bracket — Computation Annex
## Everything computable, computed: only the outcome remains

**Matthew Lach** — draft v0.1, 31 July 2026, prepared with the computing collaborator
*Annex to* The Screening Bracket *protocol and* Cold Fusion Under a Closed Index. *Calculator: `bracket_calculator.py`. Instrument: Figure 4.*

---

## 0. The claim of this annex

Every conversion, threshold, target coordinate, exposure time, and verdict boundary of the protocol is computed here, in advance, from the anchors and the model stated below. After this annex, no interpretive step remains between a laboratory measurement and its verdict: the inputs the bench can produce map mechanically to one of five pre-stated outcomes. The only unfixed symbol in the system is what the cell does — **reaction, partial reaction, or non-reaction** — which is exactly the condition the question asked for. The residue, per B.2.16.3, is stated in §6: the map carries one contested physics assumption, and the annex converts that assumption from a hidden premise into the first thing the experiment falsifies.

## 1. The instrument, calibrated

**Model.** λ(m) = C · exp(−2G₀/√m): molecular-barrier WKB, with the internuclear scale ∝ 1/m and the Gamow exponent ∝ √(μ_nuc/m). One shape parameter (2G₀), one prefactor per reaction, pinned at m = 1.

**Calibration — the committed test, passed.** 2G₀(d–d) was fit twice, from two anchors sharing no step: the Koonin–Nauenberg watt-scale threshold (m ≈ 10) gives **176.2**; the measured muonic rate (m = 207, ~10⁹ s⁻¹) gives **179.5**. Agreement within 2% across seventy-two orders of magnitude of rate; adopted **2G₀ = 177.8 ± 1.6** (B.2.8 satisfied at the instrument level). Cross-checks the model was not fit to: at m = 207 it returns 2.2 × 10⁸ s⁻¹ against the measured ~10⁹ (factor ~5 over the full span), and it reproduces the KN "ten electron masses" watt-scale statement at m\* = 9.6–10.5. p–d scaling: 2G₀ × √(μ_pd/μ_dd) = **145.2 ± 1.3**, prefactor pinned at λ_pd(1) = 10⁻⁵⁵ s⁻¹ *(recalled; flag)*.

## 2. The target coordinates — where the line lives

Computed by inverting the instrument (envelope from the ±1.6 calibration spread):

| target | m\* (envelope) | U_e by the flagged linear map (U₁ = 27 eV) |
|---|---|---|
| **p + d detectable** (10 γ/s, mole-scale) | **4.26** (4.18–4.35) | ≈ 115 eV |
| d + d detectable | 4.55 (4.46–4.65) | ≈ 123 eV |
| p + d watt scale | 10.5 | ≈ 283 eV |
| d + d watt scale | 9.6 | ≈ 260 eV |

The envelope on m\* is under ±2% — the exponential that makes the rate uncertain by orders makes the *coordinate* precise, which is why the bracket is the right instrument: the experiment measures a coordinate, not a rate.

## 3. The falsifiable fork — the annex's sharpest product

Beam-measured screening potentials in metals run ~100–800 eV *(recalled; flag)*. Under the linear map those values straddle and exceed m\*_det = 4.26. Therefore, **taken at face value, the static map predicts the 5.49 MeV line is already reachable in several metals** — and thirty-seven years of its absence is itself data. The fork, pre-stated:

- **Line appears** at the coordinate the material's measured U_e predicts → the map holds, the machine fired, proceed to the verdict table.
- **Line absent** at sensitivity across materials whose beam-U_e exceeds 115 eV → **the linear/static map is falsified**: beam-energy screening does not translate to ambient tunnelling (the dynamic-screening resolution), and the null run measures the translation deficit as a bound: the ambient coordinate of material c satisfies m_amb(c) < m(s) — a number, per material, where the field has had an ambiguity.

Either branch produces new content. There is no uninformative outcome.

## 4. The verdict machine — exhaustive, pre-stated

Inputs the bench produces: **B** blanks clean (H₂ fill dark, D₂ fill shows no 5.49 line)? **F** fill-pattern correct? **L** line ≥ 5σ (criterion: r_det·t ≥ 5√(b·t))? **N** neutrons above blank? **H** ³He commensurate within factor 3 — or below its floor for the exposure (floor from §5)? Rules, applied in order, cover all 2⁵-adjacent combinations:

| rule (first match) | verdict |
|---|---|
| B = no or F = no | **REFUSED — artefact**; register; repair; rerun |
| L = no | **NON-REACTION** at sensitivity s → bound entered: η_max(c) = s/(λ₀·N_pairs); fork §3 branch 2 evaluated |
| N = yes | **REFUSED — contamination/artefact hunt** (p + d predicts zero neutrons; a neutron excess is the d–d signature in the wrong fill) |
| H = commensurate | **REACTION** — the cell occupied; claim submitted with raw spectra; replication-on-demand clock starts |
| H = below floor for this exposure | **PARTIAL REACTION** — line real, inventory not yet measurable; verdict deferred by the exposure table, not by judgment: extend t or raise P until the ³He row of §5 is crossed; a partial that never converts within its computed exposure becomes REFUSED — route disagreement |
| H = measurable and non-commensurate | **REFUSED — route disagreement** (B.2.9): not weak evidence, a measured contradiction |

Every terminal is one of: reaction, partial (with its mandatory conversion deadline computed), non-reaction (with its bound), or refusal (with its cause). Nothing is left to interpret.

## 5. Exposure arithmetic — the partial-reaction band, bounded

Gamma: ε = 10⁻², continuum b = 0.05 c/s in the 5.3–5.7 MeV window *(nominal; replace with instrument values on the sheet)*. ³He: mass-spec floor 10⁻¹² mol *(nominal)*.

| P (W-equiv) | detected γ/day | 5σ live-time | days to ³He floor |
|---|---|---|---|
| 10⁻¹¹ | 9.8 × 10³ | ~97 s | 6.1 × 10⁵ |
| 10⁻⁹ | 9.8 × 10⁵ | < 1 s | 6.1 × 10³ |
| 10⁻⁷ | 9.8 × 10⁷ | ≪ 1 s | **61** |
| 10⁻⁵ | 9.8 × 10⁹ | ≪ 1 s | 0.6 |

The **partial-reaction band is therefore computed, not judged**: any true rate between ~10⁻¹¹ and ~10⁻⁷ W-equivalent yields a decisive line within minutes while the inventory route needs months-to-centuries — the exact regime the PARTIAL verdict exists for, with its conversion exposure read off this table. Above 10⁻⁷ W both routes close within a campaign; below 10⁻¹¹ W the line itself is the floor.

## 6. Flags and residue (B.2.11, B.2.16.3)

Load-bearing and flagged: λ_pd(1) = 10⁻⁵⁵ *(recalled)*; U₁ = 27 eV and the **linearity** of U_e ↔ m *(modelling commitment — the contested step, promoted by §3 into the first falsifiable claim rather than a buried premise)*; metal U_e range *(recalled)*; ε, b, ³He floor *(nominal, instrument-replaceable)*; muonic anchor ~10⁹ *(recalled; the calibration survives its removal — the KN anchor alone shifts m\*_det by < 2%)*. Verified: the d–d anchor 3 × 10⁻⁶⁴ (to source), the KN threshold statement (to source), Q-values (companion paper, audit 18). The residue in one sentence: this annex makes the question decidable at every coordinate the lab can reach and supplies the coordinate map, *and* the map's one assumption is the first thing the data will test — which is where a pre-computation should leave a question: with nothing between the world and the verdict but the world.
