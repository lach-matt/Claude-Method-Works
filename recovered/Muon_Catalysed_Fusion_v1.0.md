# Muon-Catalysed Fusion: Definition, Procedure, and Two Gaps

**Matthew Lach** — Independent researcher
*Draft v1.0, 1 August 2026. Prepared with a computing collaborator under the protocols of* The Method v1.2-8.
*Supersedes the exploratory drafts v0.1–v0.14 of* Cold Fusion Under a Closed Index.

---

## Abstract

Cold fusion is defined here as a nuclear fusion event in which the approach to nuclear separation is supplied by molecular binding geometry rather than kinetic energy. On that definition it is neither speculative nor unachieved: it has been performed routinely since 1957, and this paper states the procedure. Seven necessary conditions are given; applied to the closed index of charged particles they admit exactly one solution, μ⁻ + (d,t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV, because a structural window on the binder mass — bounded below by fusion geometry and above by molecular-index survival — contains one leptonic occupant. The procedure is then given in full: target requirements, the cycle with pinned rates, the exit branching, the two observables, and the failure signatures. The accelerator is treated as structure rather than preamble, since it is the only element the reaction cannot self-supply and the only one it destroys. Two quantitative gaps separate the demonstrated reaction from useful power, and they are independent. The **energy gap**: cycles per muon are capped at 1/ω_s because driving the formation resonance moves the bottleneck to muon transfer at (2.7 ± 0.9) × 10⁸ s⁻¹, so λ_c saturates near 2.6 × 10⁸ s⁻¹ and breakeven requires ω_s ≤ 0.202–0.292% against 0.45–0.56% measured; dual polarisation alone (0.34%) is insufficient at any density, while polarisation combined with a J = 1 state mixture (0.234%) clears at φ ≥ 2. The **flux gap**: 1 MW of fusion at 300 cycles per muon requires 1.2 × 10¹⁵ μ/s against ~10¹⁰ /s at the best planned source, so energy-positivity is necessary and not sufficient. Ambient electron-screened fusion is excluded separately and by conservation: at thermal energies the adiabaticity ratio is 10⁻³, where static screening is exact, and a static screening energy is bounded by the site's own electronic inventory at ~30 eV against a requirement of 88 eV.

---

## 1. Definition

> A **cold fusion reaction** is a nuclear fusion event in which the approach to nuclear separation is supplied by *molecular binding geometry* rather than by kinetic energy.

Temperature does not appear. "Cold" is a consequence — when geometry supplies the approach, kinetic energy is unnecessary — and the name has misdirected the field for decades. The operative property is *molecular access at nuclear separations*.

Seven conditions are necessary:

1. **A binder** — negatively charged, leptonic (a hadron is absorbed before it can catalyse), mass within the structural window of §2, lifetime × cycle rate ≫ 1, producible.
2. **A molecular index** with at least two bound states, so that an *edge cell* exists near the binding threshold.
3. **A formation channel** — that edge cell reachable by the host medium's smallest exchangeable quantum.
4. **Nuclear overlap** — internuclear separation small enough that fusion outruns formation.
5. **An open exit** — the compound system must have a particle channel available.
6. **Binder release** — the recoil velocity must exceed the binder's orbital velocity sufficiently that sticking is small.
7. **Conservation closure** — one heavy ash nucleus per event, energy accounted through Q.

Conditions 1–5 suffice for the reaction to *occur*; 6–7 govern whether it is sustainable and verifiable.

---

## 2. The unique realisation

The binder's mass sets the molecule's size, and therefore everything. Mass substitution moves the internuclear separation from 74,100 fm (electron) to ~280 fm (muon) — a factor buying ~91 orders of magnitude in tunnelling rate, against ~33 orders available from any perturbation of the potential at fixed geometry. **Geometry is the mechanism; screening is a correction to it.**

Two structural requirements bound the mass axis. **Fusion geometry**: the separation must bring the nuclei close enough for fusion to outrun the cycle, giving m > 119 mₑ. **Index survival**: the number of molecular bound states scales as √(M_nuclear/m_binder), and at least two are needed so an edge cell exists, giving m < 918 mₑ.

> **The structural window is [119, 918] mₑ.**

The electron fails below it (geometry), the tau above it (the molecular index degenerates to a single state). Inside it sit the muon (207 mₑ) and the pion (273 mₑ); a second filter — interaction type — removes the pion, which is absorbed by the nucleus before catalysis. **Exactly one occupant remains**, interior to the window by 1.74× and 4.44×, so the conclusion survives reasonable movement of either criterion.

Hence the reaction is fully specified rather than schematic:

> **μ⁻ + (d,t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV**

The exit channel is fixed by nuclear structure, not chosen: ⁵He is unbound, so the compound system has no bound configuration to occupy and separates as ⁴He + n. The formation channel is fixed by a near-coincidence: the dtμ (J = 1, v = 1) state is bound by only 0.66 eV, within a factor of 1.8 of the D₂ vibrational quantum (0.365 eV), and resonant transfer of that binding into host rovibrational excitation is what makes formation fast. The muonic molecule's ground state, 319 eV deep, is unreachable by the host — **the resonance uses the last bound state, and there is no second option.**

The channel is also optimal and not merely available. Sticking is governed by the ratio of recoil velocity to binder orbital velocity: 2.97 for d + t giving ~1% sticking, 1.66 for d + d giving ~15%. d + t is the unique light channel where the overlap is small.

---

## 3. The procedure

### 3.1 Stage A — the binder factory

See §4. Produce μ⁻ and stop them within the fuel volume.

### 3.2 Stage B — the target

**Purity.** Hydrogen isotopes only. Elements with Z > 1 capture muons preferentially and terminate the chain; ppm-level purity is a requirement, not a refinement.

**Tritium fraction.** Not critical. The transfer step auto-optimises the population, which is why the measured record spans c_t = 2–95% without a sharp optimum.

**Density.** φ as high as the cryogenics permit, in units of liquid hydrogen density (4.25 × 10²² atoms/cm³). The record covers 0.01–1.5 LHD.

**Temperature.** High, not low. λ_dtμ rises resonantly by roughly two orders of magnitude from low temperature to 800 K. This is the single point at which the phrase "cold fusion" misleads the operator.

### 3.3 Stage C — the cycle

Per catalytic turn, at φ = 1.2:

| step | rate (s⁻¹) | time | note |
|---|---|---|---|
| muon stops by ionisation | 10⁹ | 1 ns | once only |
| capture into a high-n muonic orbit | 10¹² | 1 ps | |
| cascade to 1s | 10¹² | 1 ps | |
| transfer μd → μt (48 eV more bound) | **(2.7 ± 0.9) × 10⁸** | 3.7 ns | **the cap** |
| dtμ formation, Vesman resonant | 10⁸ → 1.5 × 10¹⁰ | 10 ns → 0.07 ns | temperature-dependent |
| Auger de-excitation to the fusing state | 10¹¹ | 10 ps | |
| **d + t fusion at ~280 fm** | 10¹² | 1 ps | |

The cycle is a harmonic sum, so **the bottleneck moves**. At low temperature, formation is rate-determining and the cycle takes 13.6 ns (λ_c ≈ 7.3 × 10⁷ s⁻¹). Driving the resonance transfers the bottleneck to muon transfer, after which **λ_c saturates near 2.6 × 10⁸ s⁻¹** — temperature buys a factor of ~3.6 and then stops.

### 3.4 Stage D — the exit

Per fusion: **99.14%** the muon is released and re-enters Stage C; **0.86%** it remains bound to the ⁴He as (μ⁴He)⁺ recoiling at 0.043c. Of those, roughly half are collisionally stripped and rejoin the cycle, giving a net loss near 0.45% per fusion and a sticking ceiling of ~222 turns. The chain terminates when the muon decays (τ = 2.197 μs; bound-muon disappearance 4.665 × 10⁵ s⁻¹) or remains stuck.

### 3.5 Stage E — observables

**Neutrons.** 14.1 MeV, one per fusion, timed from each muon stop. The decay slope gives Λ = λ₀ + ω_s·φλ_c; the yield per muon gives N.

**X-rays.** The (μ⁴He)⁺ K_α line at 8.2 keV counts stuck muons directly, on a route sharing no instrument or calibration with the neutron measurement. These two methods disagreed historically; running them simultaneously on one target is what resolves the disagreement, and a disagreement is a refusal rather than an average.

### 3.6 Stage F — failure modes

| symptom | cause |
|---|---|
| yield far below expectation | Z > 1 contamination capturing muons |
| Λ near the free-muon 4.665 × 10⁵ s⁻¹ | muons not stopping in the fuel |
| yield falling over hours | helium ash accumulating — circulate the target |
| low λ_c at low temperature | resonance mismatch — *raise* the temperature |
| neutron and X-ray sticking disagree | refusal; resolve before any claim |

**Minimal demonstration.** Pure D₂ requires no tritium licence and yields ~4 fusions per muon, giving ~2 × 10⁴ neutrons/s at 10⁴ μ/s stopping — an unambiguous signal within minutes.

---

## 4. The binder factory

The accelerator is not preamble. It is **the sole source of the one element the reaction cannot self-supply, and the only element the reaction destroys.** Fuel, geometry, resonance and exit channel are supplied by nature or purchased once; the binder is purchased continuously.

**Chain.** A1 proton driver above the 300 MeV pion threshold; A2 production target, p + N → π⁻ + X; A3 capture (magnetic horn or solenoid — the largest single loss); A4 decay channel; A5 transport; A6 stopping within the fuel volume.

**Floor plan.** Two decay lengths set the machine's geometry: a 200 MeV/c pion travels 11.2 m before decaying, while a 100 MeV/c muon travels 624 m. The decay channel must therefore be ~11 m, and muon transport over tens of metres is nearly lossless. The 56× ratio between those lengths is what makes the machine possible.

**Energy budget.** The kinematic floor at perfect collection is 0.30 GeV per muon; the achieved figure is 5 GeV — an inefficiency of 16.7×, distributed across pion yield, capture solid angle, decay acceptance, transport and stopping fraction. None of it is forbidden, which makes E_μ the most tractable free parameter.

**Flow, not batch.** A chemical catalyst is recovered at cycle's end; the muon decays regardless of what it is doing. The accelerator must therefore run continuously at the muon loss rate, and the fuel must circulate to clear helium ash. No steady state conserves binder inventory.

---

## 5. The two gaps

### 5.1 The energy gap

Cycles per muon follow N = φλ_c/(λ₀ + ω_s·φλ_c), which saturates at 1/ω_s once λ_c is driven up. With λ_c capped at 2.6 × 10⁸ s⁻¹ by transfer, and scientific breakeven at 284 fusions per muon against a 5 GeV muon:

| ω_s | φ = 1.2 | φ = 2.0 | φ = 3.0 |
|---|---|---|---|
| 0.56% (PSI, measured) | 0.50 | 0.54 | 0.57 |
| 0.45% (SIN, measured) | 0.59 | 0.65 | 0.69 |
| 0.34% (dual polarisation) | 0.72 | 0.82 | 0.88 |
| 0.31% (J = 1 state mixture) | 0.77 | 0.88 | 0.95 |
| **0.234% (both together)** | 0.93 | **1.10** | **1.21** |

Breakeven requires ω_s ≤ 0.202% at φ = 1.2, ≤ 0.262% at φ = 2.0, ≤ 0.292% at φ = 3.0. **Two sticking levers are required; neither suffices alone.** The initial sticking ω_s⁰ is a quantum overlap fixed by the channel (0.90% from the S state, 0.31% from J = 1, v = 0), leaving reactivation and polarisation as the adjustable quantities; external-field stripping is constrained by a space–time overlap factor that renders a focused-beam approach ineffective by ~6 orders.

Measured sticking carries an interval, not a point: 0.45 ± 0.05% and 0.56 ± 0.04%, both reported below theoretical prediction. That tension is on the binding parameter and runs in the favourable direction.

### 5.2 The flux gap

| fusion power | muon rate (N = 300) | accelerator power |
|---|---|---|
| 1 kW | 1.2 × 10¹² /s | ~1 kW |
| 1 MW | **1.2 × 10¹⁵ /s** | ~0.95 MW |
| 1 GW | 1.2 × 10¹⁸ /s | ~950 MW |

Against ~10⁸ μ/s at present facilities and ~10¹⁰ /s planned. **One megawatt of fusion requires ~10⁵ times the best planned muon source.** The two gaps are independent, and the second is the harder: it is not a parameter to optimise but a machine that does not exist.

---

## 6. What the definition excludes

| excluded | grounds |
|---|---|
| electron-bound systems (ambient "cold fusion") | geometry: 74,100 fm separation, ~91 orders short |
| tau and heavier binders | the molecular index degenerates; no edge cell |
| π⁻, K⁻, p̄, Σ⁻ | nuclear absorption preempts catalysis |
| enhanced ambient screening | conservation (§6.1) |
| excess heat without commensurate ash | baryon number: any d–d branching deposits 3.76 × 10⁻⁸ – 2.74 × 10⁻⁷ mol of heavy ash per watt-day, a window 7.29× wide whose ends are the extremal channels |
| d + d with γ-dominant branching | selection rule: s-wave d + d is 0⁺ → 0⁺, which emits no single photon |
| thermal and inertial fusion | by definition — approach supplied by kinetic energy |

### 6.1 The ambient exclusion

Enhanced electron screening in metals has been proposed as an ambient route. It is excluded by conservation on two independent grounds.

**Adiabaticity.** At thermal energies the ratio of deuteron to electron velocity is 1.0 × 10⁻³ — deeply adiabatic, where static screening is not an approximation but exact. Beam measurements sit at 0.63, some 620× faster and squarely non-adiabatic, where a fitted screening parameter absorbs stopping-power and straggling effects that have no ambient counterpart. The measured enhancement belongs to a different regime.

**Energy audit.** A static screening energy is bounded by what the electron system can donate. The complete site inventory is: Thomas–Fermi 29 eV, plasmon ~9, Fermi 5–10, cohesive 4–8, zero-point 0.1, kT 0.026. The ceiling is ~30 eV against a requirement of 88 eV for a detectable p + d rate — a factor 2.9 in energy, 27 orders in rate.

The bound is conservation-grade and admits no mitigation by vacuum, geometry, cooling, or channel choice. Independently, the historical absence of neutrons from palladium deuteride excludes a static reading of the beam anomaly by ~16 orders.

---

## 7. Provenance

Verified against primary or surveyed literature: the transfer rate (2.7 ± 0.9) × 10⁸ s⁻¹; λ_dtμ > 10⁸ s⁻¹ rising to (100–150) × 10⁸ at 800 K; bound-muon disappearance 4.665 × 10⁵ s⁻¹; LHD 4.25 × 10²² atoms/cm³; dtμ separation ~280 fm; dtμ (J=1,v=1) binding 0.66 eV; sticking 0.90% (S state) and 0.31% (J=1,v=0) by variational three-body calculation, measured 0.45 ± 0.05% (SIN) and 0.56 ± 0.04% (PSI); ~150 cycles and Q ≈ 0.53 at Los Alamos; scientific breakeven at 284 fusions per muon; E_μ ≈ 5 GeV at PSI and J-PARC MUSE; dual-polarisation estimates ω_s 0.45 → 0.34%, λ_c +30–50%, cycles 148 → 193; scanned ranges PSI 0.01–1.5 LHD at c_t 2–95% and T 13–300 K, JINR 0.2–1.2 LHD at T 20–800 K; the screened molecular D₂ rate 3 × 10⁻⁶⁴ s⁻¹; sticking ~1% for dtμ against ~15% for ddμ; the external-field reactivation criterion ω_S^eff = ω_S⁰(1−R_col)(1−R_X).

Computed for this paper: the structural window [119, 918] mₑ; λ_c saturation at 2.6 × 10⁸ s⁻¹ from the harmonic sum; breakeven sticking thresholds 0.202/0.262/0.292%; decay lengths 11.2 m and 624 m; the 0.30 GeV kinematic floor and 16.7× inefficiency; flux requirements 1.2 × 10¹²/10¹⁵/10¹⁸ s⁻¹; the ash bracket 3.76 × 10⁻⁸ – 2.74 × 10⁻⁷ mol per watt-day at width 7.29; the adiabaticity ratios 1.0 × 10⁻³ and 0.63; the ~30 eV static screening ceiling against an 88 eV requirement; the muonic ⁴He 1s binding 10.9 keV and 1s→2p resonance 8.20 keV.

Carried with reservation: step rates other than transfer are order-of-magnitude; the internuclear separation from a hydrogenic estimate was 28% high before correction; whether the 0.31% figure is initial or post-reactivation sticking is not resolved by its source; the muonic-molecule state table is recalled; the window edges depend on the two criteria stated in §2, though the muon is interior to any reasonable choice.

Corrections made during preparation are recorded in the working drafts and are not reproduced here. Two are material to the results above and are stated for the reader's benefit: an earlier claim that fusion is confined to the molecular ground state was withdrawn against the variational result for J = 1; and an earlier framing treating energy-positivity as the sole remaining requirement was corrected by the flux gap of §5.2.

---

## References

1. M. Lach, *The Method* v1.2-8 — *The Lach Cylinder: an index of transitions*.
2. μCF cycle parameters: transfer, formation, disappearance rates; LHD; scanned density, concentration and temperature ranges (PSI, JINR, TRIUMF programmes).
3. Variational three-body calculation of μ–α sticking, S state and J = 1, v = 0 (Phys. Rev. A **34**, 2536, 1986).
4. Measured final sticking: SIN 0.45 ± 0.05%, PSI 0.56 ± 0.04% (direct observation, ionisation chamber).
5. μCF energy balance: ⟨E_μ⟩ ≈ 5 GeV; ~150 cycles at Los Alamos; Q ≈ 0.53; breakeven ≈ 284 fusions per muon.
6. Dual polarisation of fuel nuclei and muon beam: ω_s and λ_c estimates (2026 μCF review).
7. External-field-assisted muon reactivation: rate-network criterion and no-go condition (2026).
8. S.E. Koonin and M. Nauenberg, *Nature* **339**, 690 (1989) — screened fusion rates in isotopic hydrogen molecules.
9. Accelerator screening-potential measurements in deuterated metals; temperature dependence (Raiola et al., 2004–2005).
10. Baluev et al., d + d → ⁴He + γ branch limit from the ddμ system.
