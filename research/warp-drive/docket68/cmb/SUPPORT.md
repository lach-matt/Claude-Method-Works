# How observation extends the clock's support (M-SUPPORT's dynamics; verified once; SEATED in ledger.py section 8h on M's "Seat both", item 55; 2026-10-05)

*First headed* "(M-SUPPORT's dynamics; verified once; not seated; 2026-10-05)".

## What M asked, and how it is carried

- **The order.** M's order (rulings item 54) was *"3, then 2, then 1 please"*: M-SUPPORT's dynamics first.
- **What M-SUPPORT is.** It is M's stronger reading of item 48 (*"The decoupling only exists upon observation of a
  universe?"*) as a computable rule. The clock's support is the coupled epochs, and observation extends it through
  records. It is built in `unobserved.py`.
- **The open question.** How does the support grow? That was OPEN 1 in UNOBSERVED.md.
- **M's answer.** Item 52 (H-LOCAL-CLOCK) is carried as M's answer to that question: *"The clock is relative to the
  matter-based observation."*
- **The warrant for matter as observer.** M's item 49 (H-TWO-OBSERVERS) warrants treating matter as an observer:
  *"matter itself is capable of observation"*.

Everything here is carried as M's hypotheses, never as results.

Every number below is printed by `support.py`.
- **Selftest:** 9/9 checks, 5 of them controls, with 3 STRUCTURAL lines printed and not counted.
- **Inputs:** it asks `unobserved.py` (and through it `medium.py`, `cmbframe.py`, `cosmo.py` and `seat.py`) and
  `arrival.py` for its inputs.
- **Verification:** it was verified once, and its findings are applied. The first-written claims are kept under History.

## The reading (H-SUPPORT-IS-RECORDS, a hypothesis)

**On this hypothesis,** matter observes the photons by scattering them, and each Thomson scattering is a record.
- **The rate.** Matter then records a given photon at the rate Γ = n_e σ_T c, which is **Γ/H records per photon per
  e-fold of expansion**. That is the support's growth law:

  > d(support)/d ln a = Γ/H

- **Where a record lasts is itself a hypothesis (H-RECORD-DURABLE).** An electron's momentum is re-thermalised at once
  by Coulomb collisions and by about 10⁹ photons per baryon. In decoherence physics, the durable record of a scattering
  sits in the outgoing photon (NAMED-NOT-READ).

Two supports follow. Both are standard cosmology under a new name:

- **ALL-RECORDS.** Every epoch at which matter recorded the photons, weighted by the Thomson optical depth dτ.
- **LAST-RECORD.** The epoch at which today's photon was *last* recorded by matter. This is the **visibility
  function**, g(z) = e^(−τ) dτ/dz.

**On this hypothesis, M's item 48 becomes a statement about records.** Decoupling is the edge of matter's observation of
the light: the point where matter stops recording the photons faster than the universe expands, and where the last
record peaks. The mapping is a named hypothesis. The physics under it is not.

## Sources READ (2026-10-05, via alphaXiv; "verifier-READ" marks text the verifier read at source)

- **Recombination.** Seager, Sasselov & Scott, astro-ph/9909275v2 (RECFAST): eq. 1 (p.3), eq. 3, and the constants on
  p.4 (Λ_2s = 8.22458 s⁻¹, λ_Lyα = 121.5682 nm, a, b, c, d, F = 1.14). He I at 24.6 eV is on p.3.
- **Cosmological parameters.** Planck 2018 VI, 1807.06209v4: Table 1 (p.15), Table 2 (p.16) and Y_P = 0.2454 from
  Table 2's caption.
- **Reionisation.** Planck XLVII, 1605.03507v3: the tanh model (eq. 2, p.5), δz = 0.5, and helium's second ionisation
  at z = 3.5 (p.5).
  - **Discrepancy 1, the sign:** the printed eq. 2 reads tanh((y − y_re)/δy), which would ionise the *early* universe.
    - The same page describes the transition as running "from an essentially vanishing ionized fraction x_e at early
      times, to a value of unity at low redshifts".
    - CAMB's code uses the opposite sign (verifier-READ).
    - So the sign is a misprint or extraction artefact in the paper, and (y_re − y) is used.
  - **Discrepancy 2, the width:** the paper evaluates δy at z. The code, like CAMB, evaluates it at z_re. This changes τ
    from 0.05414 to 0.05426 (verifier-computed).
- **The Sachs–Wolfe effect.**
  - White & Hu, astro-ph/9609105v1, p.1 eq. 3: "in a gravitational potential clocks run slow". On the same page:
    "proper time coincides with coordinate time", and "The intrinsic term is negligible" in the fluid's rest frame.
    Their Φ has the opposite sign to Hu & Dodelson's Ψ.
  - Hu & Dodelson, astro-ph/0110414v1 (journal page numbers): a potential "corresponds to a temporal shift of δt/t = Ψ"
    (p.14). Eq. 13 (p.15) gives −2Ψ/3 in the matter era. Eq. 25 (p.30) quotes "The observed COBE fluctuation of
    ∆T ≈ 28 μK (Smoot et al 1992)".
- **z\*'s definition.** CAMB computes z* with reionisation left out of τ (`results.f90`, verifier-READ).

## Computed

### 1. The history of the light's ionised medium

- **Recombination.** RECFAST's hydrogen equation is used, starting from Saha equilibrium and integrated implicitly.
  - Helium I is treated by Saha equilibrium (H-HEI-SAHA).
  - The matter temperature is set equal to the radiation temperature (H-TM-EQUALS-TR).
- **Reionisation** uses Planck's tanh model at z_re = 7.67.

| quantity | computed | Planck 2018 | control |
|---|---|---|---|
| z* (τ = 1, reionisation left out, as Planck defines it) | **1090.28** (+0.03 %, 1.4σ) | 1089.92 ± 0.25 | Saha equilibrium, with no bottleneck at n = 2: 1291.2 |
| age | **13.795 Gyr** | 13.797 ± 0.023 | no Λ: 9.68 Gyr (trivially different) |
| sound horizon r*, at Planck's z* | **144.26 Mpc** | 144.43 ± 0.26 | — |
| reionisation τ | **0.0542** | 0.0544 ± 0.0073 | z_re = 11: 0.0897 |

- **The z\* agreement may be partly fortuitous,** given the Saha treatment of helium and T_M = T_R.
- **The age and r\* rows test the board's integrator and its baryon loading** on Planck's own parameters. They do not
  test the recombination.
- **For comparison:** with reionisation counted in τ, τ reaches 1 at z = 1085.6.

### 2. Matter's observation of the light

| z | 1500 | 1090 | 800 | 200 | 20 | 7.67 | 0 |
|---|---|---|---|---|---|---|---|
| Γ/H, records per photon per e-fold | 143 | 12.8 | 0.222 | 0.0029 | 7.3×10⁻⁵ | 0.042 | 0.0020 |

- **Where the support stops growing.** It depends on the definition:
  - matter stops recording faster than the expansion (Γ/H = 1) at **z = 904**;
  - τ = 1 at **z = 1090**;
  - the last record peaks at **z = 1079**, with a full width at half maximum of 203 in z.
- **LAST-RECORD: where today's photons were last recorded by matter.**
  - **94.57 %** at z > 200.
  - **0.15 %** at 30 < z < 200.
  - **5.28 %** since reionisation (z < 30). Reionisation's midpoint is at t = 672 Myr, but these last records spread
    toward today: the median is z = 4.57 (t = 1.3 Gyr), and the 10–90 % range is z 7.1–1.4 (t 0.74–4.5 Gyr).
- **The last-scattering surface is observer-relative by construction.** It uses τ integrated from the observing event.
  But for an observer at any z_now from 0 to 900, its peak stays at z = 1079. That cuts both ways: it is relative to the
  observer, and it is the same epoch for every observer computed.

### 3. The dynamics: the support as it stands at each moment

The table counts records per photon from z = 2500, so its absolute numbers depend on that starting point.

| present z_now | records per photon laid down since z = 2500 | growth per e-fold at z_now |
|---|---|---|
| 1500 | 109.34 | 143 |
| 1090 | 131.14 | 12.8 |
| 900 | 132.04 | 0.93 |
| 600 | 132.12 | 0.040 |
| 30 | 132.13 | 0.00013 |
| 7.67 | 132.13 | 0.042 |
| 0 | 132.19 | 0.0020 |

- **While coupled, the support grows fast.**
- **After decoupling it nearly halts.**
- **At reionisation it resumes.**
- **Today, 0.2 % of the photons are scattered per Hubble time.**

### 4. Into the toy (`unobserved.py`)

GLM call the clock weighting "completely arbitrary" (H-CLOCK-WEIGHT). Here it is replaced by the record weightings,
binned onto the toy's ticks (H-TOY-BINNING). The medium starts in the coupled ground state.

| weighting | coupled share | purity | trace distance from static M-SUPPORT |
|---|---|---|---|
| ALL-RECORDS | 0.990 | 0.9994 | 4.5×10⁻⁴ |
| LAST-RECORD | 0.374 | 0.962 | 0.093 |
| record-free T⁸ (a comparison) | — | — | 3.9×10⁻⁴ |
| Thomson weight with no recombination (x_e = 1) | — | — | **0.111** |
| M-SUPPORT's own reweighting ambiguity (flat vs cubic above T_dec) | — | — | 2.3×10⁻³ |

- **What the agreement does not show.** ALL-RECORDS lies within M-SUPPORT's own reweighting ambiguity, but so does a
  record-free weighting. The agreement is largely by construction:
  - the toy's T_dec is the τ = 1 temperature;
  - any weighting with nearly all its weight above T_dec gives nearly the same state, because the coupled ground state
    is stationary there. The control shows a trace distance of 1.4×10⁻¹¹ on the 9 fully coupled ticks.
- **What it does show.** Thomson records stop where the coupling stops. Without recombination, the Thomson weight moves
  the state by 0.111, more than ten times the ambiguity.
- **So this is consistency, not a dynamical origin.** On H-SUPPORT-IS-RECORDS, records and coupling share their edge.
- **LAST-RECORD is different.** It concentrates on the edge, where the medium is changing.

### 5. Local clocks at last scattering (H-LOCAL-CLOCK at cosmic scale)

- **The frame-invariant part.** Decoupling is a surface of constant *local* temperature, i.e. of constant local matter
  state. In the fluid's own rest frame, the proper times on it agree. So when decoupling happens is defined by the local
  matter, not by a global clock, and that holds in every frame. This is the part of M's *"The clock is relative to the
  matter-based observation"* that the physics carries without condition.
- **The Newtonian-frame description.** This uses H-MATTER-ERA and H-SW-ONLY.
  - A potential Ψ is a clock-rate offset, δt/t = Ψ. Each place reaches the same local reading at a shifted coordinate
    time.
  - That gives an intrinsic temperature change of −2Ψ/3; climbing out of the well gives Ψ; the observed sum is Ψ/3.
  - **The size, from COBE's 28 μK** (an rms amplitude): ΔT/T = 1.03×10⁻⁵, so |Ψ| = 3.08×10⁻⁵. With t\* = 371,202 yr,
    the **rms offset of local decoupling is about 11 years in this frame**.
  - At z\*, radiation is still a quarter of matter (w_eff = 0.081), so the intrinsic factor is 0.617 rather than 2/3.
- **Only Ψ/3 is measured.** The offset itself is this frame's description. In the fluid's rest frame "The intrinsic
  term is negligible", and the observed Ψ/3 is the same in both frames (STRUCTURAL).

### 6. Today's telescope (STRUCTURAL)

- **A detection today is one more matter record.** Its clock reading is T0 = 2.7255 K, and its content is the photon's
  state since its last record.
- **A conscious reading of it is a perception of that record.** This follows Page; see `localclock.py`.

## For M

- **On H-SUPPORT-IS-RECORDS, your M-SUPPORT rule has a growth law** from standard physics: Γ/H records per photon per
  e-fold.
  - It is fast while the medium is coupled.
  - It falls below the expansion rate at z ≈ 904, and the last record peaks at z ≈ 1079.
  - It resumes at reionisation.
  - Today, 0.2 % of photons are scattered per Hubble time.
- **"Decoupling only exists upon observation" reads, on this mapping, as decoupling being the edge of matter's
  observation of the light.** The records thin out exactly where the coupling ends; without recombination they would
  not.
  - In the toy, weighting by records reproduces your M-SUPPORT state, but so would any weighting concentrated on the
    coupled epochs. That agreement is consistency, not proof.
- **The last-scattering surface is defined from the observer.** For every observer computed, it is the same epoch.
- **Not all of today's light was last observed at decoupling.** 5.3 % was last recorded by matter after reionisation,
  most of it within a few billion years.
- **When decoupling happens is set by the local matter, in every frame.** That is your "clock relative to the
  matter-based observation", without condition. In the Newtonian frame the same physics reads as places reaching the
  same local reading about 11 years apart (rms). Only the resulting Ψ/3 is measured.
- **Conscious observation enters only at the end,** as the reading of a record that matter made.

**O9 is not touched by this.** Records extend the support. They do not open a channel.

## Named hypotheses

- H-SUPPORT-IS-RECORDS.
- H-RECORD-DURABLE.
- H-RECFAST-H, H-HEI-SAHA, H-TM-EQUALS-TR and H-REION-TANH.
- H-HE-MASS-4.
- H-MASSLESS-NU. Planck's Ω_m includes one 0.06 eV neutrino (Table 1 caption).
- H-BOHR-LEVELS and H-TOY-BINNING.
- H-MATTER-ERA and H-SW-ONLY.
- From `unobserved.py`: H-TOY-MEDIUM and H-CLOCK-WEIGHT.
- M's: H-UNOBSERVED-MEDIUM, H-M-SUPPORT, H-TWO-OBSERVERS and H-LOCAL-CLOCK.

## OPEN

1. Whether records of the *photon* are the right records for M-SUPPORT, and where a record lasts (H-RECORD-DURABLE).
   That needs decoherence sources READ (Joos–Zeh, Zurek; relational QM, quant-ph/9609002).
2. z\* beyond its +0.03 % agreement. That needs helium recombination, the matter temperature equation (Seager eq. 5),
   and HyRec or CosmoRec (NAMED-NOT-READ).
3. The low-ℓ anisotropy at Planck precision, including the integrated Sachs–Wolfe term (H-SW-ONLY). COBE's 28 μK is
   used, as quoted by Hu & Dodelson.
4. Whether LAST-RECORD or ALL-RECORDS is M's support. They differ in the toy by 0.09.

## History (first-written claims kept)

### Before any report

- **The support table** first printed the records laid down *after* z_now.
- **The record grid** first started at z = 1700, which gave zero weight to the toy's ticks above it.
- **A vacuous purity check** was removed.
- **The stationarity control** first ran over every tick above T_dec.

### Verifier, 2026-10-05

- **z\*.** First written as τ = 1 *with* reionisation counted: *"1085.6 (−0.40 %) … about 17 standard deviations … its
  likely sources are the named simplifications … good to 0.5 %"*. That was a definition mismatch, not physics. Like for
  like the figure is 1090.28 (+0.03 %, 1.4σ), and the check is now 0.1 %.
- **The toy.** It said: *"ALL-RECORDS reproduces M-SUPPORT … to 5×10⁻⁴. So M-SUPPORT's rule has a dynamical origin."*
  That is mostly true by construction. A record-free weighting does as well, and the precision is below M-SUPPORT's own
  reweighting ambiguity.
- **The LAST-RECORD shares.** *"94.72 % at recombination"* counted the dark ages twice; the shares summed to 100.15 %.
  The *"5.28 % at reionisation, at t ≈ 672 Myr"* put a midpoint where a spread belongs.
- **The local clocks.** It said *"local decoupling was spread over about 11.4 years"* and *"literally the record of local
  clocks … measured on the sky"*. The figure is an rms offset in one frame, and only Ψ/3 is measured. White & Hu say
  "negligible", not "vanishes".
- **Flat assertions** of H-SUPPORT-IS-RECORDS now carry the hypothesis's name. H-RECORD-DURABLE, H-MATTER-ERA and
  H-SW-ONLY are now named.
- **Tolerances.** The τ check allowed 1σ for a 0.0002 match; it is now 0.001.
- **Undersold, now carried:**
  - the frame-invariant local-matter definition of decoupling;
  - the observer-relative construction of the last-scattering surface;
  - M's item 49 as the warrant for matter as an observer.
