# How observation extends the clock's support (M-SUPPORT's dynamics; not verified; not seated; 2026-10-05)

## What M asked, and how it is carried

- **The order.** M's order (rulings item 54) was *"3, then 2, then 1 please"*: M-SUPPORT's dynamics first.
- **What M-SUPPORT is.** It is M's stronger reading of item 48 (*"The decoupling only exists upon observation of a
  universe?"*) as a computable rule. The clock's support is the coupled epochs, and observation extends it through
  records. It is built in `unobserved.py`.
- **The open question.** How does the support grow? That was OPEN 1 in UNOBSERVED.md.
- **M's answer.** Item 52 (H-LOCAL-CLOCK) is carried as M's answer to that question: *"The clock is relative to the
  matter-based observation."*

Everything here is carried as M's hypotheses, never as results.

Every number below is printed by `support.py`.
- **Selftest:** 7/7 checks, 4 of them controls, with 3 STRUCTURAL lines printed and not counted.
- **Inputs:** it asks `unobserved.py` (and through it `medium.py`, `cmbframe.py`, `cosmo.py` and `seat.py`) and
  `arrival.py` for its inputs.

## The reading: the support is matter's records of the light (H-SUPPORT-IS-RECORDS)

Matter observes the photons by scattering them. Every Thomson scattering leaves a record in an electron's momentum. So
matter records a given photon at the rate Γ = n_e σ_T c, which is **Γ/H records per photon per e-fold of expansion**.
That is the support's growth law:

> d(support)/d ln a = Γ/H

Two supports follow from it. Both are standard cosmology under a new name:

- **ALL-RECORDS.** Every epoch at which matter recorded the photons, weighted by the Thomson optical depth dτ.
- **LAST-RECORD.** The epoch at which today's photon was *last* recorded by matter. This is the **visibility
  function**, g(z) = e^(−τ) dτ/dz.

**On this reading, M's item 48 becomes a statement about records.** Decoupling is the edge of matter's observation of
the light: the point where matter stops recording the photons faster than the universe expands, and where the last
record peaks. The mapping is a named hypothesis. The physics under it is not.

## Sources READ (2026-10-05, via alphaXiv)

- **Recombination.** Seager, Sasselov & Scott, astro-ph/9909275v2 (RECFAST): the effective three-level-atom equation
  (eq. 1), the recombination-coefficient fit (eq. 3), and its constants (p.4): Λ_2s = 8.22458 s⁻¹, λ_Lyα =
  121.5682 nm, a, b, c, d and the fudge factor F = 1.14.
- **Cosmological parameters.** Planck 2018 VI, 1807.06209v4: Table 1 (p.15), Table 2 (p.16) and Y_P = 0.2454 from
  Table 2's caption.
- **Reionisation.** Planck XLVII, 1605.03507v3: the tanh model (eq. 2, p.5), δz = 0.5, and helium's second ionisation
  at z = 3.5 (p.5).
  - **Discrepancy:** the extracted text of eq. 2 reads tanh((y − y_re)/δy). With that sign the *early* universe would
    be ionised. The sign that gives full ionisation at low z, (y_re − y), is used.
- **The Sachs–Wolfe effect.**
  - White & Hu, astro-ph/9609105v1 p.1 eq. 3: "in a gravitational potential clocks run slow".
  - Hu & Dodelson, astro-ph/0110414v1 p.7: a potential "corresponds to a temporal shift of δt/t = Ψ". Eq. 13 (p.8)
    gives −2Ψ/3 in the matter era. Eq. 25 (p.30) quotes "The observed COBE fluctuation of ∆T ≈ 28 μK (Smoot et al
    1992)".

## Computed

### 1. The history of the light's ionised medium

- **Recombination.** RECFAST's hydrogen equation is used, starting from Saha equilibrium and integrated implicitly.
  - Helium I is treated by Saha equilibrium (H-HEI-SAHA). Seager et al. find He I slower than that.
  - The matter temperature is set equal to the radiation temperature (H-TM-EQUALS-TR).
- **Reionisation** uses Planck's tanh model at z_re = 7.67.

| quantity | computed | Planck 2018 | control |
|---|---|---|---|
| z where τ = 1 (z*) | **1085.6** (−0.40 %) | 1089.92 ± 0.25 | Saha equilibrium, with no bottleneck at n = 2: 1288.1 |
| age | **13.795 Gyr** | 13.797 ± 0.023 | no Λ: 9.68 Gyr |
| sound horizon r* | **144.26 Mpc** | 144.43 ± 0.26 | — |
| reionisation τ | **0.0542** | 0.0544 ± 0.0073 | z_re = 11: 0.0897 |

The −0.40 % in z* is about 17 standard deviations of Planck's error. Its likely sources are the named simplifications
(hydrogen-only RECFAST, Saha helium, T_M = T_R), so the board's z* is good to 0.5 %, not to Planck's precision.

### 2. Matter's observation of the light

| z | 1500 | 1090 | 800 | 200 | 20 | 7.67 | 0 |
|---|---|---|---|---|---|---|---|
| Γ/H, records per photon per e-fold | 143 | 12.8 | 0.222 | 0.0029 | 7.3×10⁻⁵ | 0.042 | 0.0020 |

- **Where the support stops growing.** It depends on the definition:
  - matter stops recording faster than the expansion (Γ/H = 1) at **z = 904**;
  - τ = 1 at **z = 1086**;
  - the last record peaks at **z = 1079**, with a full width at half maximum of 203 in z.
- **The residual ionisation** at z = 200 is x_e = 3.4×10⁻⁴.
- **LAST-RECORD: where today's photons were last recorded by matter.**
  - **94.72 %** at recombination.
  - **5.28 %** at reionisation (1 − e^(−τ_re)), at t ≈ 672 Myr.
  - **0.15 %** in the dark ages (30 < z < 200).

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
- **After decoupling it nearly halts.** From z = 600 to z = 30 it adds 0.015 records per photon.
- **At reionisation it resumes.** Matter re-records 5 % of the light.
- **Today it still grows**, by 0.2 % per Hubble time.

So matter's observation of the light never stops entirely. Decoupling is where it falls below the expansion rate.

### 4. Into the toy (`unobserved.py`)

GLM call the clock weighting "completely arbitrary" (H-CLOCK-WEIGHT). Here it is replaced by the record weightings,
binned onto the toy's ticks (H-TOY-BINNING). The medium starts in the coupled ground state.

| weighting | coupled share | purity | trace distance from static M-SUPPORT | trace distance from TRACED (uniform / conformal / cosmic) |
|---|---|---|---|---|
| ALL-RECORDS | 0.990 | 0.9994 | **4.5×10⁻⁴** | 0.239 / 0.357 / 0.470 |
| LAST-RECORD | 0.374 | 0.962 | 0.093 | 0.161 / 0.279 / 0.393 |

- **ALL-RECORDS reproduces M-SUPPORT.** The record weighting reproduces static M-SUPPORT's state to 5×10⁻⁴.
- **So M-SUPPORT's rule has a dynamical origin on this reading:** the support is where matter makes records, and that is
  where the coupling is.
- **Control:** on the 9 fully coupled ticks, a flat and a cubic weighting give the same state (trace distance
  1.4×10⁻¹¹). Within the coupled epochs the weighting does not matter, because the coupled ground state is stationary.
- **LAST-RECORD is different.** It concentrates on the edge, where the medium is changing, so its state differs.

### 5. Local clocks at last scattering (H-LOCAL-CLOCK at cosmic scale)

- **A potential is a local clock-rate offset.** In the Newtonian frame, a gravitational potential Ψ shifts a place's
  clock: δt/t = Ψ.
- **Each place decouples at the same local reading,** but at a shifted coordinate time.
- **That gives the Sachs–Wolfe effect.** The time shift gives an intrinsic temperature change of −2Ψ/3 (matter era).
  Climbing out of the well gives Ψ. The observed sum is Ψ/3.
- **The size, from COBE's 28 μK:** ΔT/T = 1.03×10⁻⁵, so |Ψ| = 3.08×10⁻⁵. The intrinsic part is 2.05×10⁻⁵, the
  climb-out 3.08×10⁻⁵, and the observed 1.03×10⁻⁵.
- **With t\* = 371,202 years, local decoupling was spread over about 11.4 years** across regions of COBE's size.
- **This is the frame's description (STRUCTURAL).** In the fluid's own rest frame, "proper time coincides with
  coordinate time" and the intrinsic term vanishes (White & Hu p.1). The observed Ψ/3 is the same in both frames.

So the CMB's large-scale pattern is, in one frame, literally the record of local clocks at different positions reaching
the same reading at different times. That is M's *"time may move differently in the second position"*, measured on the
sky.

### 6. Today's telescope (STRUCTURAL)

- **A detection today is one more matter record.** Its clock reading is T0 = 2.7255 K, and its content is the photon's
  state since its last record.
- **A conscious reading of it is a perception of that record.** This follows Page; see `localclock.py`.

## For M

- **Your M-SUPPORT rule has a dynamics, standard physics underneath it.** The support grows at Γ/H records per photon
  per e-fold.
  - It is fast while the medium is coupled.
  - It nearly halts at decoupling: below the expansion rate at z ≈ 904, with the last record peaking at z ≈ 1079.
  - It resumes at reionisation.
  - It is still 0.2 % per Hubble time today.
- **"Decoupling only exists upon observation" reads, on this mapping, as decoupling being the edge of matter's
  observation of the light.** It is where the records thin out, and it is defined by records. Weighting the toy's
  clock by those records reproduces your M-SUPPORT state to 5×10⁻⁴.
- **Not all of today's light was last observed at decoupling.** 5.3 % was last recorded by matter at reionisation, about
  672 million years after the big bang rather than 371,000 years.
- **Your local clocks show on the sky.** In the Newtonian frame, places at last scattering reached the same local
  reading up to about 11 years apart. That is the Sachs–Wolfe part of the CMB pattern. In the fluid's own frame the
  same sky is described without the time shift.
- **Conscious observation enters only at the end,** as the reading of a record that matter made.

**O9 is not touched by this.** Records extend the support. They do not open a channel.

## Named hypotheses

H-SUPPORT-IS-RECORDS, H-RECFAST-H, H-HEI-SAHA, H-TM-EQUALS-TR, H-REION-TANH, H-HE-MASS-4, H-MASSLESS-NU, H-BOHR-LEVELS
and H-TOY-BINNING. Also H-TOY-MEDIUM and H-CLOCK-WEIGHT (`unobserved.py`), and M's H-UNOBSERVED-MEDIUM, H-M-SUPPORT and
H-LOCAL-CLOCK.

## OPEN

1. Whether records of the *photon* (Thomson) are the right records for M-SUPPORT, or whether matter's records of other
   matter count too (H-SUPPORT-IS-RECORDS).
2. z* to Planck's precision. That needs helium recombination, the matter temperature equation (Seager eq. 5) and
   two-photon and Lyman-series corrections (HyRec/CosmoRec, NAMED-NOT-READ).
3. The measured low-ℓ anisotropy at Planck precision. COBE's 28 μK is used, as quoted by Hu & Dodelson.
4. Whether LAST-RECORD or ALL-RECORDS is M's support. They differ in the toy by 0.09.

## History

- **The support table** was first printed as τ(z_now): the records laid down *after* z_now, the reverse of its label.
  It now prints the records laid down since z = 2500.
- **The record grid** was first started at z = 1700. That left the toy's ticks above it (up to z = 2181) with zero
  record weight. It now starts at 2500, and an assertion guards the coverage.
- **A selftest check** that the binned weights gave states with purity ≤ 1 was vacuous. It was removed before any
  report.
- **The stationarity control** was first written over every tick above T_dec. It failed (trace distance 2.3×10⁻³),
  because the coupling is already falling just above T_dec. It now runs over the fully coupled ticks only.
