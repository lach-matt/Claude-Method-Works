# H-CMB-CORRIDOR, reading 2: the cosmic background as medium or carrier, with H-CONTRACT (not verified, not seated; 2026-10-05)

## M's words and how they are carried

**M's words**, verbatim from the rulings file:
- Item 45: *"Seat it, then medium"*.
- Item 46: *"Now what happens if we consider that the universe not only expands, but it contracts as well?"*
- Item 47: *"2, then 1"*. The contraction status is read at source first, then folded into this reading.

**Carried as M's hypotheses, never as results:** H-CMB-CORRIDOR, H-CMB-UNIVERSAL (item 41) and H-CONTRACT (item 46).

Every number is printed by `medium.py`. It loads `cmbframe.py` and `step1c/demand.py` by path and imports `nopath.py`,
`seat.py` and `cosmo.py`. Its selftest runs 18/18 checks, 3 of them controls, with 3 STRUCTURAL lines printed and not
counted.

## Five meanings of "medium", each priced

The reading takes "medium" in five senses. None is dismissed, and each says what would change it.

### (A) What is there to use

At T₀ = 2.72548 K (Fixsen) the background holds:
- 410.7 photons per cm³ and 4.175×10⁻¹⁴ J/m³;
- an entropy of 2.134×10⁹ bits/m³, which is 5.20 bits per photon;
- a mean photon energy of 0.634 meV and a thermal length of 0.840 mm.

These densities come from integrating the Planck distribution numerically and are checked against the closed forms.
A 1 m² tube from Earth to Proxima holds **8.6×10²⁵ bits** of background entropy.

### (B) A medium in the acoustic sense

**Today: no.**
- A medium carries a collective mode, such as sound, only if its constituents interact.
- An upper bound on the photon–photon scattering rate gives a mean free path of at least **1.2×10⁷⁸ m**. That is
  **52 orders beyond the Hubble length**, so the gas is collisionless.
- The bound uses the low-energy light-by-light cross-section, σ = (973/10125π) α⁴ (ω/m)⁶ ƛ_e² (King & Heinzl
  1510.08456v1 p.3), averaged over the thermal spectrum.

**Before decoupling: yes.**
- The background was then the photon–baryon fluid. Its sound speed was c_s = c/√(3(1+R)) (Hu & Sugiyama
  astro-ph/9407093v1 eq. 6).
- At the observed R* = 0.60 ± 0.06 (Hu & Dodelson astro-ph/0110414v1 p.26), that is **0.456 c**.
- Decoupling happened at T₀(1+z*) = **2,973 K**, with z* = 1089.92 from Planck 2018 VI Table 2.

### (C) A passive carrier

This sense means using background photons that are already heading from A toward B, by redirecting or modulating
them at A. The demand is the species count, 9.5×10²⁷ bits, which is 3.0×10²⁰ bits/s over a year.

| apertures at A and B | background photons per second from A into B | bits each photon would have to carry |
|---|---|---|
| 1 m² each | 6.1×10⁻¹⁸ | 5×10³⁷ |
| 1 km² each | 6.1×10⁻⁶ | 5×10²⁵ |

A passive modulator also has almost nothing to modulate with. Its contrast is bounded by the background's own
anisotropy: the dipole gives 9.9×10⁻³, comparing the apex patch with the anti-apex.

### (D) Noise and heat sink

**Not the noise at the board's quantum.**
- At the board's floor quantum (263 keV), the background's mean occupation is 10^(−4.9×10⁸). It does not limit that
  link at all.
- It is the noise only near its own peak, where the occupation is 0.063.

**The coldest heat sink the board holds.**
- Handling one bit at T₀ costs at least 2.6×10⁻²³ J (Landauer). Handling the whole species count costs at least
  **2.5×10⁵ J**.
- The board's 1-year channel floor is **5.6×10⁸ times larger**.
- So the cost of sending the information is set by the channel, not by thermodynamics. Thermodynamically, at the
  background's temperature, the information is nearly free.

### (E) A shared resource between the ends

**No quantum correlation across the span.**
- The field's degree of coherence between two points falls off as 15/(π⁴ρ⁴), with ρ = r·kT/(ħc).
- This is the sin(kr)/kr kernel (Henkel et al. physics/0008028v1 p.4) averaged over the Planck spectrum. The fall-off
  formula matches the integral to 10⁻⁶.

| separation | degree of coherence |
|---|---|
| 1 mm | 0.068 |
| 1 cm | 7.7×10⁻⁶ |
| Earth–Proxima | **3×10⁻⁸⁰** |

The background holds no correlation, quantum or classical, between the corridor's ends at the field level.

**A shared map of the sky.**
- Both ends see the same sky: the parallax between their views is below 2.9×10⁻¹⁰ rad.
- That sky has **6,295,077** independent modes up to ℓ = 2508 (Planck 2018 V).
- This is shared classical randomness. By no-signalling it carries no message: it is a common reference, not a
  channel.

## (H) H-CONTRACT: the status as read, and what contraction does

**The status, read at source** (`CONTRACT_READ` holds the full citations):

- **The expansion is accelerating now.** Riess 1998 finds q₀ < 0 at 2.8–3.9σ. DESI DR1 finds acceleration required at
  z < 0.7.
- **Evolving dark energy is preferred, but weakly.** DESI DR2 prefers w₀ > −1, wa < 0 at 2.8–4.2σ (frequentist).
  - The DES-Dovekie recalibration brings this to 3.2σ, "only a weak preference" in Bayesian terms.
  - Ong, Yallup and Handley find no Bayesian evidence with Dovekie.
- **A recollapse appears only in fits with a negative vacuum or potential.**
  - Luu, Qiu and Tye's best fit turns around in about 11 Gyr and crunches at a lifespan of 33.3 Gyr. That best fit lies
    outside 1σ of their mean, and Ω_Λ = 0 is consistent with the data.
  - Andrei, Ijjas and Steinhardt find the expansion ends no sooner than 0.27/H₀, which is **3.9 Gyr** with the board's
    Hubble time of 14.5 Gyr.
  - Gialamas et al. prefer a negative vacuum at 93.8 %, using the pre-recalibration DES supernovae.
- **Bounces can be nonsingular or singular.**
  - Loop quantum cosmology keeps the volume above zero in every state (Ashtekar & Singh eq. 3.23), and so does Ijjas and
    Steinhardt's classical bounce.
  - The original ekpyrotic model reaches a = 0 in the 4d frame (Steinhardt & Turok p.7).
- **What happens to radiation through a bounce depends on the model.**
  - Ijjas and Steinhardt: radiation is regenerated each cycle and the old is diluted, with "the entropy observed within
    the Hubble radius … the same from cycle to cycle".
  - Steinhardt and Turok: radiation is generated at the bounce.
  - LQC: the conservation law is unchanged, so radiation would pass through. This is the reader's inference, not
    printed in the source.

**Verdict:** H-CONTRACT is carried. It is not shown and not excluded.

**What contraction does, computed:**

1. **Loop-freedom.** `frame.py`'s z3 lemma needs only a > 0, and that was asked of `frame.py` at run time.
   - A nonsingular bounce keeps a corridor network keyed to cosmic time loop-free, through the bounce
     (H-EFFECTIVE-METRIC).
   - A crunch to a = 0 breaks the premise. The lemma's own control, run with a = 0 allowed, shows the claim failing
     there.
2. **The temperature label.**
   - T ∝ 1/a holds both ways (Novello & Perez Bergliaffa p.86, T³a³ = const).
   - Below the bounce temperature, every temperature therefore occurs twice, so temperature stops being a unique label
     for a slice. Cosmic time itself remains a label.
   - In LQC the bounce caps the background near 1.3×10³² K, just under the Planck temperature (1.42×10³² K). That figure
     assumes radiation held the whole density.
3. **The medium returns.** Contracting back to a = 9.2×10⁻⁴ heats the background to **2,973 K**, where it re-couples to
   matter and becomes the photon–baryon fluid again, with sound speed about 0.46 c.
   - From Luu, Qiu and Tye's best-fit turnaround (a_max 1.69, where the background would be 1.61 K), that is a
     contraction by a factor of 1,844.
   - **Under H-CONTRACT, then, the background as a medium is not impossible. It is a phase of the cycle, the hot one.**
4. **Timescales.** Today the background's temperature changes by 6.9×10⁻⁹ of itself over a century. Any contraction
   lies at least about 4 Gyr away, so it does not touch any corridor on the board's schedules (a day to a century).

## For M

**On H-CMB-UNIVERSAL.** In the two cyclic models read, the background is not carried from one cycle to the next. It is
regenerated each cycle, with the same entropy per Hubble radius. That makes the background a recurring feature of the
cosmos, the same in kind each cycle but not the same photons. This is the closest the sources read come to M's
"constant". In LQC's bounce the same background would pass through, but that rests on the reader's inference.

**On H-CMB-CORRIDOR as medium.**
- Today the background is collisionless, holds no correlation across the span, and is too sparse along the line from
  A to B to carry the object's information.
- It does three things well:
  - it names the frame (reading 1);
  - it is the coldest heat sink, making the thermodynamic cost of the information negligible;
  - it gives both ends a shared reference of six million modes.
- In a contracting universe's hot phase it becomes a true medium again.

**O9 stays OPEN.**

## Named hypotheses

H-CMB-BLACKBODY, H-OMEGA-CM, H-ALPHA, H-ISOTROPIC-FLUX, H-APERTURES, H-PASSIVE, H-SCALAR-COHERENCE, H-LSS-DISTANCE,
H-MODES, H-CONTRACT, H-EFFECTIVE-METRIC, H-RADIATION-AT-BOUNCE and H-T-SCALES, plus `cmbframe.py`'s and `demand.py`'s.

## OPEN

1. The register reading (the background's entropy as where information sits) and the carrier reading (the coupling's
   carrier).
2. Whether radiation passes through a bounce, by model. The LQC case is an inference.
3. Whether the universe will contract: the evidence is weak and contested.
4. H-CMB-UNIVERSAL's multi-spacetime clause.

## Sources (READ 2026-10-05, alphaXiv; no 403 met)

**Physics of the background:**
- King & Heinzl 1510.08456v1, p.3.
- Hu & Sugiyama astro-ph/9407093v1, pp.4–5.
- Hu & Dodelson astro-ph/0110414v1, p.26.
- Planck 2018 VI, 1807.06209v4, Table 2 p.16.
- Planck 2018 V, 1907.12875v2, Table 23 p.88.
- Henkel et al. physics/0008028v1, pp.1, 4, 6.
- Mohanty cond-mat/0005233v1, eq. 8.

**Contraction status:**
- Riess 1998, astro-ph/9805201v1.
- DESI DR1, 2404.03002v3; DESI DR2, 2503.14738v3.
- DES-Dovekie, 2511.07517v3; Unite, 2609.05053v2.
- Efstathiou 2408.07175v3; Vincenzi 2501.06664v1.
- Huang, Cai & Wang 2502.04212v5; Wang & Mota 2504.15222v2; Wang 2504.15635v3.
- Ong, Yallup & Handley 2511.10631v3.
- Luu, Qiu & Tye 2506.24011v2; Andrei, Ijjas & Steinhardt 2201.07704v2; Gialamas et al. 2506.21542v2.

**Bounce models:**
- Ashtekar & Singh 1108.0893v2.
- Ijjas & Steinhardt 1803.01961v1 and 1904.08022v1.
- Steinhardt & Turok hep-th/0111098v2.
- Novello & Perez Bergliaffa 0802.1634v1.

**NOT READ:** Berestetskii–Lifshitz–Pitaevskii; Mehta & Wolf 1964; Tolman 1934; Luu–Qiu–Tye 2503.18120; DESI
2503.14743; Herold & Karwal 2506.12004; Ijjas 1710.05990; and the others listed by the readers.
