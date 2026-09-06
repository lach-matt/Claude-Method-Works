# The Tantalum Test
## Exact laboratory reconstruction — the Screening Bracket instantiated at Ta, Pd, Au

**Matthew Lach** — draft v0.1, 31 July 2026, prepared with the computing collaborator
*Instantiates* The Screening Bracket *protocol v0.2 and its Computation Annex at the named metals. All numbers computed or carried with provenance; verdicts inherited unchanged.*

---

## 0. Object of the test

This experiment measures **C0** — whether the screening these metals show a keV deuteron beam (Ta: U_e = 309 ± 12 eV, verified and independently confirmed) is also shown to a *thermal, bound* deuteron. Nothing else is under test. All engineerable conditions (C1–C4) are set to their best values so that the outcome, whatever it is, is a statement about C0 alone. The unconditional deliverable is a coordinate per cell; the conditional deliverables are, on the null branch, the ambient screening ceiling per metal (a 1-day null already yields U_e,amb < 117 eV against tantalum's 309 eV beam value — a ≥ 3× translation deficit, ≥ 10¹³ in rate), and on the positive branch, the fully pre-described reaction of the companion paper §6.6.

## 1. Apparatus

1. **Cryostat**: closed-cycle, sample stage 4–340 K, optical/thin-wall window toward the detector; temperature logged continuously (C1 is a measured axis, not a setting).
2. **γ spectrometer**: HPGe (≥ 40% relative efficiency) with plastic-scintillator cosmic veto; region of interest **5.3–5.7 MeV** — above the 2.615 MeV endpoint of natural radioactivity, so the continuum there is cosmogenic and veto-reducible. Absolute efficiency at 5.5 MeV calibrated with an Am–Be source (4.438 MeV line) plus simulated extrapolation; the nominal ε_total = 10⁻² and window continuum b = 0.05 c/s used below are **replaced by the measured values on the sheet before Run 0 ends**.
3. **Second γ position**: the detector (or a second detector) at two angles to the sample normal, ~90° and ~30°, for the E1 test (§5.3).
4. **Neutron counter**: ³He proportional counter, moderated; the d–d discriminator channel.
5. **Loading**: Pd — electrochemical (0.1 M LiOH/LiOD in H₂O/D₂O mix), loading tracked by resistivity ratio; Ta — gas-phase charging (H₂/HD/D₂ at elevated T, then sealed and cooled), loading tracked gravimetrically. Loading is *measured and logged*, never assumed (C2).
6. **Ash assay**: sample dissolution + noble-gas mass spectrometry for ³He after each run block; tritium by liquid scintillation of the electrolyte/gas.
7. **Calorimetry**: secondary, isothermal, μW-class — present for the verdict machine's H-row, not as the discovery channel.
8. **Blank materials**: Au foil (verified no-enhancement class, with Cu as alternate), and one insulator coupon (verified small-effect class) — the periodic table's own null row (C4).

## 2. Materials matrix

| sample | class | beam U_e | naive coordinate | role |
|---|---|---|---|---|
| **Ta** (99.95%, annealed foil, 10 g) | large-effect metal | **309 ± 12 eV, verified** | 11.4 | primary — no ambient-null archive exists |
| **Pd** (99.95%, foil, 10 g; one coupon vacancy-engineered by cold-work + anneal cycling) | large-effect metal | ~800 eV *(recalled; flag)* | ~30 | secondary — probes the 4.26–6.2 band beneath its own calorimetric history |
| **Au** | no-effect noble metal, verified | small | ~1 | Run 0 blank |
| insulator coupon (e.g. Si) | small-effect class, verified | ~gaseous | ~1 | pattern control |

Purity certificates on file; boron and light-element (p,γ) contaminants assayed before loading (C4). The vacancy-engineered Pd coupon addresses C3 (pair confinement toward molecular range via vacancy–hydrogen clusters — *recalled; flag*); its comparison against as-annealed Pd is itself a row.

## 3. Conditions ladder

Temperature points: **295 K → 77 K → 20 K → (4 K if signal)**, held ≥ 24 h each, same sample, same fill. Under the verified Debye T-dependence, any genuine C0 effect must **grow on cooling** — and not gently: if the room-temperature coordinate is even 4.5, Debye scaling predicts the 77 K rate is ~10⁸× larger (computed). The cooldown is therefore a self-contained verdict: signal detonates, or the classical map is dead at that coordinate. An effect that shrinks or holds flat on cooling is not this effect.

## 4. Fills and the run matrix

Three fills per metal, schedule fixed before Run 0 (B.2.9 — no post-hoc selection):

| fill | Ta / Pd prediction | Au / insulator prediction |
|---|---|---|
| **H₂ only** | dark everywhere | dark |
| **HD (test)** | 5.49 MeV line iff C0; zero neutrons; ³He ash | dark |
| **D₂ (crossover)** | no 5.49 line; d–d set (2.45 MeV n, t) at the d–d coordinate; γ at ≤ 8 × 10⁻⁷ per fusion (measured limit, paper ref. 11) | dark |

A 5.49 line in a D₂ fill, any line in Au, or neutrons in an HD fill = artefact/contamination, refused by pre-stated rule. The periodic-table on/off pattern across the four materials is a signature no mundane artefact reproduces.

## 5. Signatures and thresholds

**5.1 The line.** Admissible at ≥ 5σ above the fitted continuum in 5.3–5.7 MeV, threshold from the Run 0 blank series, criterion r_det·t ≥ 5√(b·t).

**5.2 Sensitivity ladder (computed; nominal ε, b — to be replaced by measured):**

| exposure | 5σ source floor | W-equivalent | null ⇒ m_amb < | null ⇒ U_e,amb < |
|---|---|---|---|---|
| 1 d | 0.38 γ/s | 3.3 × 10⁻¹³ | 4.34 | 117 eV |
| 7 d | 0.14 γ/s | 1.3 × 10⁻¹³ | 4.22 | 114 eV |
| 30 d | 0.069 γ/s | 6.1 × 10⁻¹⁴ | 4.14 | 112 eV |
| 90 d | 0.040 γ/s | 3.5 × 10⁻¹⁴ | 4.08 | 110 eV |

(Nominal 0.01 mol effective p–d pairs; the sheet computes the sample's true N_pairs from measured loading. The exponential makes the coordinate bound nearly exposure-independent: **the first day decides**; long exposure buys precision on the ceiling, not reach.)

**5.3 E1 character.** p + d capture at low energy is E1; the s-wave pattern goes as ~sin²θ about the beamless symmetry axis *(recalled; flag — pin to the measured p–d capture literature before Run 0)*: ideal N(90°)/N(30°) = 4.0, corrected for geometry on the sheet. A candidate line failing the ratio is refused by selection rule.

**5.4 Neutron channel.** ³He counter live throughout; HD fills predict **zero** above blank; D₂ fills predict the d–d rate at whatever coordinate the line (if any) implies — a cross-consistency equation, not a free parameter.

**5.5 Ash.** ³He assay per run block; any claimed power must land its ash in the 7.29× bracket (3.76 × 10⁻⁸ – 2.74 × 10⁻⁷ mol per W·day). Tritium assay guards the contamination row.

## 6. Run schedule (fixed now)

**Run 0** — Au, all three fills, full T-ladder, ≥ 7 d each: measures ε, b, blank rates; freezes thresholds.
**Run 1** — **Ta**, fills H₂ → HD → D₂, T-ladder per fill, 30 d HD at 295 K then cooldown steps.
**Run 2** — **Pd** (as-annealed), same; **Run 2b** — Pd (vacancy-engineered), HD only.
**Run 3** — insulator coupon, HD, 7 d: pattern control.
Interleaved 24 h Au re-blanks between runs. Every run appears in the record with outcome and sensitivity (B.2.6); rejection causes pre-listed: loading loss below threshold, cryostat excursion, veto failure, assay contamination.

## 7. Verdict machine (inherited, instantiated)

Rules in order, per run: blanks/fills wrong → REFUSED-artefact. No line → NON-REACTION: enter U_e,amb ceiling for that metal and T (the §5.2 column), and the beam-to-ambient translation deficit (Ta: deficit ≥ 3× in U_e on day one). Neutrons in HD → REFUSED-contamination. Line + E1 pass + T-trend rising + ash commensurate → REACTION; replication-on-demand clock starts; the reaction observed must match the companion paper's §6.6 description in every particular, because nothing else is admissible as this reaction. Line + any correlate failing → route disagreement or PARTIAL per the exposure table, with its conversion deadline computed, not judged.

## 8. Pre-filled committed-prediction sheets

> **Run 0 (Au blank).** Predicted: dark, all fills, all T. Any line = apparatus artefact; thresholds frozen from this run. Signature: ____
>
> **Run 1 (Ta, HD, 295 K → 4 K).** Predicted: **null** (the grade that has never hit); printed alternative if C0 holds at face value (m = 11.4): line at ~10¹² γ/s-scale — i.e., *unmissable within seconds*, rising ~10⁸× by 77 K; zero neutrons; ³He at bracket rate. Null deliverable: U_e,amb(Ta) < 117 eV (day 1), < 112 eV (30 d) — the first ambient number tantalum will ever have. Signature: ____
>
> **Run 2/2b (Pd).** Predicted: **null**; window under test 4.26 ≤ m ≤ 6.2 — beneath the μW calorimetric history, uninspected on this observable in 37 years. Vacancy coupon tests C3 at fixed C0. Signature: ____

## 9. Flags and residue (B.2.11, B.2.16.3)

Flagged: Pd ~800 eV (survey value unverified this pass); interstitial spacing 2.9 Å and vacancy–cluster confinement (recalled); E1 angular form (pin to measured p–d capture data); ε, b, N_pairs nominal until Run 0 measures them; the classical-Debye T-scaling is part of the contested C0, so the §3 ladder is a prediction *of the map under test*, not of the experiment. Verified and carried: Ta 309 ± 12 eV; Q(p,d) = 5.493 MeV; the noble-metal null row; the T-dependence's existence; the ddμ γ-limit. The residue in one sentence: this document sets every condition a catalog can supply and instruments the one it cannot — and its expected result, stated at the grade that has never missed, is a coordinate for tantalum where none has ever been measured, with the reaction's exact face on file should the other grade finally hit.
