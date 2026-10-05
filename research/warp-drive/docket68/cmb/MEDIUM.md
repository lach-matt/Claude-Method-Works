# H-CMB-CORRIDOR, reading 2: the cosmic background as medium or carrier, with H-CONTRACT (verified once and corrected; SEATED in ledger.py section 8g on M's "3, then 2, then 1 please", item 54; 2026-10-05)

*First headed* "(verified once and corrected; not seated; 2026-10-05)".

## M's words and how they are carried

**M's words**, verbatim from the rulings file:
- Item 45: *"Seat it, then medium"*.
- Item 46: *"Now what happens if we consider that the universe not only expands, but it contracts as well?"*
- Item 47: *"2, then 1"*. The contraction status is read at source first, then folded into this reading.

**Carried as M's hypotheses, never as results:** H-CMB-CORRIDOR, H-CMB-UNIVERSAL (item 41) and H-CONTRACT (item 46).
H-UNOBSERVED-MEDIUM (item 48) and H-TWO-OBSERVERS (item 49) are taken up in their own reading (`unobserved.py`).

Every number is printed by `medium.py`. It loads `cmbframe.py` and `step1c/demand.py` by path and imports `nopath.py`,
`seat.py` and `cosmo.py`. Its selftest runs 18/18 checks, 3 of them controls, with 3 STRUCTURAL lines printed. One
verifier checked it in both directions. Every finding is applied, and the first-written claims are kept in the file's
HISTORY and below.

## Five meanings of "medium", each priced

### (A) What is there to use

At T₀ = 2.72548 K the background holds:
- 410.7 photons per cm³ and 4.175×10⁻¹⁴ J/m³;
- an entropy of 2.134×10⁹ bits/m³, which is 5.20 bits per photon;
- a mean photon energy of 0.634 meV and a thermal length of 0.840 mm.

A 1 m² tube from Earth to Proxima holds 8.6×10²⁵ bits of background entropy.

### (B) A medium in the acoustic sense

**Today: no.**
- The photon–photon mean free path, averaged over the spectrum and computed exactly, is **10⁵³ Hubble lengths**.
- The exact average weights each pair by its centre-of-mass energy (H-OMEGA-CM): ω² = E₁E₂(1 − cos θ)/2 per photon, with
  the flux factor (1 − cos θ). The cross-section is King & Heinzl 1510.08456v1 p.3.
- Even a photon far out in the spectrum's tail (x = 30) travels 10⁵⁰ Hubble lengths between collisions.
- The gas is collisionless and carries no collective mode.

**Before decoupling: yes.** The background was then the photon–baryon fluid.
- Its sound speed was c_s = c/√(3(1+R)) (Hu & Sugiyama eq. 6). At R* = 0.60 (Hu & Dodelson p.26) that is 0.456 c.
- Decoupling happened at T₀(1+z*) = 2,973 K.

### (C) A passive carrier

Conservation of radiance (étendue) caps the background photons that any passive device can send from A into B at
(n c/4π) A_A A_B/L². Against the species count over a year, 3.0×10²⁰ bits/s:

| apertures at A and B | background photons per second from A into B, at most | bits each photon would have to carry |
|---|---|---|
| 1 m² each | 6.1×10⁻¹⁸ | 5×10³⁷ |
| 1 km² each | 6.1×10⁻⁶ | 5×10²⁵ |

The contrast a passive modulator can work with depends on its kind (H-PASSIVE):
- a lossless redirector, or an absorber in equilibrium at T₀: 9.9×10⁻³, from the dipole;
- a shutter colder than T₀, which must be refrigerated: up to 1.

The photon budget above binds either way.

### (D) Noise and heat sink

**Where the background is the noise.**
- It is the dominant noise at and below its own peak. Its occupation is 0.063 at the peak, exceeds 1 below
  **39.4 GHz**, and is 56 at 1 GHz.
- At the board's floor quantum (263 keV) its occupation is 10^(−4.9×10⁸). It plays no part in that link.

**The coldest heat sink the board holds.**
- *Erasing* a bit at T₀ costs at least 2.6×10⁻²³ J (Landauer prices irreversible erasure only). Erasing the whole
  species count costs at least 2.5×10⁵ J.
- The board's 1-year channel floor is 5.6×10⁸ times larger. The cost of sending the information is set by the channel,
  not by thermodynamics.
- The sink is usable in practice. Erasing the count at 2T₀ over a year needs about 0.016 W. A sky-facing radiator of
  **335 m²** dumps that heat, since the sky's own flux is σT₀⁴ = 3.1×10⁻⁶ W/m².

### (E) A shared resource between the ends

**Negligible field correlation across the span.**
- The trace of the field's coherence tensor, averaged over the Planck spectrum, has an exact closed form:
  15/(π⁴ρ⁴) − (15/πρ) csch²(πρ) coth(πρ), with ρ = r·kT/(ħc).
- The longitudinal component falls more slowly, as 45/(2π³ρ³).
- Across Earth–Proxima: the trace is **3×10⁻⁸⁰** and the longitudinal component **7×10⁻⁶⁰**. Both are negligible.

**A shared map of the sky.**
- The two ends see the same sky, to a parallax below 2.9×10⁻¹⁰ rad.
- The larger difference is aberration from Proxima's 32 km/s motion: 1.1×10⁻⁴ rad, about 9 % of the finest scale
  Planck maps. Reading 1's frame corrects it.
- The sky holds **6,295,077** independent modes (Planck to ℓ = 2508). This is shared classical randomness. By
  no-signalling it carries no message: it is a common reference, not a channel.

## (H) H-CONTRACT: the status as read, and what contraction does

**The status, read at source** (`CONTRACT_READ` holds the full citations):

- **The expansion is accelerating now.** Riess 1998 finds q₀ < 0 at 2.8–3.9σ. DESI DR1 finds acceleration required at
  z < 0.7.
- **Evolving dark energy is preferred, but weakly.** DESI DR2 prefers it at 2.8–4.2σ (frequentist).
  - After the DES-Dovekie recalibration this falls to 3.2σ, "only a weak preference".
  - Ong, Yallup and Handley find no Bayesian evidence.
- **A recollapse appears only in fits with a negative vacuum or potential.**
  - Luu, Qiu and Tye's best fit turns around in about 11 Gyr and has a 33.3 Gyr lifespan, ending at a → 0. It uses the
    pre-recalibration DES data, lies outside 1σ of its own mean, and Ω_Λ = 0 is consistent with the data.
  - Andrei, Ijjas and Steinhardt find the expansion ends no sooner than 0.27/H₀ for m_Pl/m = 10, sooner for steeper
    potentials.
  - Gialamas et al. prefer a negative vacuum at 93.8 %, also on pre-recalibration data.
- **Bounces can be nonsingular or singular.**
  - Loop quantum cosmology keeps the volume above zero in every state, and so does Ijjas and Steinhardt's classical
    bounce.
  - The original ekpyrotic model (4d frame) and Luu, Qiu and Tye's crunch both reach a = 0.
- **What happens to radiation through a bounce depends on the model.**
  - LQC: *printed*. Radiation keeps ρ ∝ a⁻⁴ through the bounce, and its temperature peaks there, finite (Ashtekar &
    Singh §VII.D pp.113–114).
  - Ijjas and Steinhardt: radiation is regenerated each cycle, with "the entropy observed within the Hubble radius … the
    same from cycle to cycle".
  - Steinhardt and Turok: radiation is generated at the bounce.

**Verdict:** H-CONTRACT is carried. It is not shown and not excluded.

**What contraction does, computed:**

1. **Loop-freedom.** `frame.py`'s z3 lemma needs only a > 0. It was asked at run time, with its vacuity and drift guards
   asserted.
   - A nonsingular bounce keeps a corridor network keyed to cosmic time loop-free.
   - A crunch to a = 0 breaks the premise. The lemma's own control, run with a = 0 allowed, shows the claim failing.
2. **The temperature label.**
   - T ∝ 1/a holds both ways, so every temperature below the bounce's occurs twice per cycle.
   - LQC's bounce caps the photon temperature near 1.26×10³² K. That is 0.888 of the Planck temperature, a ratio fixed by
     the 0.41 for any constants.
   - a_bounce/a_now is about 2×10⁻³² counting photons alone, about three times that once the changing number of
     particle species is counted (g*s).
3. **A hot, coupled phase recurs in every model read, by different routes.**
   - **By compression** (LQC, LQT): the background heats to **2,973 K** at a = 9.2×10⁻⁴ and re-couples to matter. From
     LQT's turnaround (a_max 1.69, where it would be 1.61 K) that is a contraction by a factor of 1,844.
   - **By regeneration** (Ijjas–Steinhardt): slow contraction shrinks a only about 17-fold, even as H rises to the Planck
     rate, so the old background reaches only about 45 K. The hot phase there is regenerated at the bounce, by reheating
     above the electroweak scale.
   - Not computed: if the intergalactic gas stays diffuse and ionised (H-IONISED-IGM), the background would couple much
     earlier. The verifier estimates about 110–140 K, with sound at about 0.15 c. That is OPEN. Luu, Qiu and Tye expect
     collapse into black holes instead.
4. **Timescales.** Today the background's temperature changes by 6.9×10⁻⁹ of itself per century. The corridor's
   schedules, a day to a century, are untouched unless a contraction began within one. No source read predicts that,
   though AIS's steepest-potential times are only in a figure and stay OPEN.

## For M

**On H-CMB-UNIVERSAL.** Read across the bounce models, the background is "constant" in one of two ways:
- **the same in kind each cycle** (Ijjas–Steinhardt: regenerated, with the same entropy per Hubble radius); or
- **the same radiation carried through** (LQC: printed).

Either way, a hot, coupled photon–baryon medium recurs every cycle.

**On H-CMB-CORRIDOR as medium.**
- Today the background is collisionless, holds negligible correlation across the span, and is photon-starved along the
  line from A to B.
- It does three things well:
  - it names the frame (reading 1);
  - it is the coldest heat sink, making the erasure cost of the information negligible, with a radiator of a few hundred
    m²;
  - it gives both ends a shared reference of six million modes, brought into registry by reading 1's frame.

**O9 stays OPEN.**

## Named hypotheses

H-CMB-BLACKBODY, H-OMEGA-CM, H-ALPHA, H-ISOTROPIC-FLUX, H-APERTURES, H-PASSIVE, H-SCALAR-COHERENCE, H-LSS-DISTANCE,
H-MODES, H-CONTRACT, H-EFFECTIVE-METRIC, H-RADIATION-AT-BOUNCE, H-T-SCALES and H-IONISED-IGM, plus `cmbframe.py`'s and
`demand.py`'s.

## OPEN

1. The register reading (the background's entropy as where information sits) and the carrier reading (the coupling's
   carrier).
2. Whether radiation passes through a bounce in the regenerative and ekpyrotic models.
3. Whether the universe will contract, and AIS's steep-potential times.
4. The ionised-IGM coupling on contraction.
5. H-CMB-UNIVERSAL's multi-spacetime clause.

## History (verifier, 2026-10-05; first-written claims kept)

- **The collision bound.**
  - First said: "ω taken as the lab energy (the CM energy is never larger)".
  - What was wrong: this is false photon by photon. The figure survives only as an upper bound on the mean rate.
  - Corrected: the exact mean is 10⁵³ Hubble lengths, where 10⁵² was first printed.
- **The noise.**
  - First said: "the noise only near its own peak".
  - Corrected: the background is the dominant noise at and below its peak.
- **The coherence tensor.**
  - First said: tensor components differ "but not in their power-law fall-off".
  - Corrected: the longitudinal component falls as ρ⁻³.
- **The timescale.**
  - First said: "any contraction lies at least about 4 Gyr away".
  - Corrected: 0.27/H₀ holds for m_Pl/m = 10 only.
- **The hot phase.**
  - First said: "the medium returns … the hot one", stated for every model.
  - Corrected: split by model (compression or regeneration). The hot phase recurs in all of them.
- **LQC radiation through the bounce.**
  - First said: "the reader's INFERENCE".
  - Corrected: it is printed (pp.113–114).
- **Passive contrast and the shared sky.** The contrast bound held only for a lossless or T₀ absorber. Aberration, not
  parallax, is the larger difference between the two skies.
- **Vacuous checks.** Four checks are replaced by pins and real controls. "Handling" the bits now reads "erasing".

## Sources (READ 2026-10-05, alphaXiv; the verifier re-read seven; no 403 met)

As in reading 2's first build, plus Ashtekar & Singh 1108.0893v2 §VII.D pp.113–114 and eq. 3.26 p.40 (verifier),
Andrei, Ijjas & Steinhardt 2201.07704v2 pp.5 and 9 (verifier), and Luu, Qiu & Tye 2506.24011v2 pp.3 and 12 (verifier).
