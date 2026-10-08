# B4d stage 2: the regime window (computed, READ and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage2.py`, selftest 6/6.

## What you said

- **2026-10-08:** *"Continue B4d as well please"*; *"Continue"*.
- **Item 133:** there is only one exact energy for any given README.
- **Item 136, answer 8:** k's scale, *"leave it to measurement"*.
- **Item 159:** *"test both options"*.

## The question

- **The corridor's own relations.** G1, G3 and H1 use Newton's G at the throat. They put the README's horizon at
  r₀ = 2m, with m = GE/c⁴.
- **B4c's far model.** H-FAR-MODEL, the board's reading, needs ℓ > 2·R_reach.
- **Can both hold at once?**

## S1. The horizon the README's energy makes (computed from READ)

- **The five-dimensional coupling.** Maartens–Koyama (1004.3962, p.29, eq. (164)): for r ≪ ℓ, V ≈ GℓM/r² = G₅M/r². So
  G₅ = Gℓ, and a small hole *"is approximately a 5D Schwarzschild (static) solution"*.
- **Two independent forms, both READ.**
  - From Ishibashi–Kodama's eq. (2.3), the 5D Schwarzschild form: r_h² = (8/3π)·m·ℓ.
  - From Maartens–Koyama's tidal-charge horizon, eq. (163): r_h = m·(1 + √(1 + 4ℓ/m)). This grows as 2√(mℓ) when
    ℓ ≫ m.
- **Controls.** The two forms scale the same way, within a factor of 2.17. As ℓ → 0 the tidal form gives the 4D
  Schwarzschild value, 2m.

## S2. Where the four-dimensional relations hold (computed)

- **The condition.** The README's horizon sits within 10% of 2m only for **ℓ < 0.11 m**, with m the corridor's mass
  length.
- **Why.** That is Figueras–Wiseman's *"large ones recover 4d behaviour"* (READ). For ℓ ≫ m the horizon is about
  2√(mℓ), far larger than 2m: a five-dimensional hole.

## S3. What B4c asks (imported)

| hold | B4c needs |
|---|---|
| the static window (~11.3 clocks, the hold before item 158) | ℓ > 23 m |
| the opening (≥ 2.0×10⁵ clocks, `o3_write.py`) | ℓ > 4.0×10⁵ m |

## S4. The window is empty (computed)

- **What both together need.** ℓ < 0.11 m and ℓ > 2·R_reach together need R_reach < 0.055 m. That is a hold of
  under about **0.055 clocks**.
- **How far short each hold falls:**
  - the window hold, by a factor of about **200**;
  - the opening, by a factor of about **3.6×10⁶**.
- **At the opening's ℓ** the README's 5D horizon is about 580 m, against r₀ = 2 m.
- **The conflict predates item 158.** The board's B4b and B4c were computed in the flat limit (ℓ ≫ r₀), while G1, G3
  and H1 use 4D G at the throat. KSCALE.md already found the same from the far field: *"Only r₀ ~ ℓ is open"*. The long
  opening widens the gap; it did not create it.

## S5. In physical units (computed)

- **The corridor's mass length.** At the example README, m = GE/c⁴ = **2.0×10⁻²⁸ m**.
- **The two requirements:**
  - The 4D window needs ℓ < 2×10⁻²⁹ m, about 1.4 million Planck lengths.
  - B4c's far model needs ℓ > 8×10⁻²³ m (4.5×10⁻²⁷ m for the window hold).
- **What measurement says.** The table-top bound, ℓ ≲ 10⁻⁴ m (Maartens–Koyama p.11, READ), is an upper bound only. So
  measurement (B6′, your 136 answer 8) can still put ℓ on either side.

## Verdict

- **The board's reading gives way, not your rulings.** H-FAR-MODEL — a single Randall–Sundrum plane whose far surface
  reaches into the bulk — cannot hold together with the corridor's four-dimensional relations at the corridor's own
  scale, for any hold longer than about 0.055 clocks. Your rulings and the proved lemmas stand.
- **What has to be rebuilt.** Either B4c's far model is rebuilt for ℓ ≲ r₀, or the bulk carries more than one plane
  (KSCALE's route (b), your 138).
- **Not decided here: a far surface for ℓ ≲ r₀** (stage 3). In this model any surface reaching more than ℓ/2 into the
  bulk is trapped over the throat. So it would have to hug the plane, and whether one exists is open.
- **What this means for B4b and B4c.**
  - B4b's static bulk was computed in the flat limit, the regime this rules out for the corridor's relations, so B4b's
    reading must be recomputed at ℓ ≲ r₀.
  - B4c's reading, H-FAR-MODEL, is refuted against the rest of the chain.
  - Both are proposed to become **OPEN** once this is verified.

## Named hypotheses

- **Yours:** 133, 136 (8), 159.
- **The board's:**
  - H-FAR-MODEL (tested here);
  - H-PULL-IS-COST (m = GE/c⁴);
  - the RS 1-brane normalisation G₅ = Gℓ (MK eq. (164));
  - a 10% tolerance for "four-dimensional at the throat".
