# B4d stage 2: the regime window (computed, READ and deduced; verified once; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage2.py`, selftest 4/4.

The first draft concluded that B4c's far model must give way, and proposed B4b and B4c as OPEN. Its verifier showed
that conclusion rests on a *round* far surface. Using the board's own expansion formula, a tipped surface is untrapped
where a round one is not. The draft also treated one member of an inconsistent set as forced to give way, and misread
KSCALE. All corrected below (History). **No B4 status moves on this stage's account.**

## What you said

- **2026-10-08:** *"Continue B4d as well please"*; *"Continue"*.
- **Item 133:** one exact energy.
- **Item 136, answer 8:** k's scale, *"leave it to measurement"*.
- **Items 160–162:**
  - the corridor is the opening;
  - one object, of fixed size;
  - it holds the README at once.

## What stands

**S1. The README's energy as plane matter** (deduced from READ normalisation).
- **The step this needs, now named:** H-BRANE-MATTER. The README's energy has to gravitate as matter on a single
  Randall–Sundrum plane, statically. The first draft left this unnamed.
- **What follows.** A 5D hole of radius r_h² = (8/3π)·m·ℓ. The coupling is G₅ = Gℓ (Maartens–Koyama eqs. (3) and (27))
  and the hole is Ishibashi–Kodama's eq. (2.3); this result does not depend on the factor-of-2 convention.
- **A consistency check, not an independent control.** Maartens–Koyama's tidal form scales the same way. Both rest on
  the same equation, MK eq. (40).

**S2. Where the 4D readings hold** (deduced, order of magnitude).
- **The rule.** Figueras–Wiseman's corrections go as O(ℓ²/r₀²) (READ p.4), so r₀ ≳ ℓ.
- **A rough figure.** For a 10% correction that is about ℓ ≲ 0.6 m, with no READ threshold.

**S3. What B4c asks depends on the far surface's shape** (computed, `b4_global.py`).
- **A round surface** needs ℓ > 2·R_reach.
- **A tipped surface does not.** Take w = W(1 − u²/U²) at ℓ = 0.11 m, enclosing the reach. It is untrapped, with
  minimum θ+ = +0.07, where a round surface of the same reach is trapped.
- **Why.** A sharp tip is untrapped at any depth, and the condition there is κ > 3/(ℓ + W).
- **B4c's text is corrected to match.** Its "iff" and "no such T exists" applied only to a round T.

**S4. The window is empty only for a round surface.**
- **With a round T,** the window is empty for every hold, even a zero hold, and the conflict predates item 158.
- **Even then nothing is forced to give way.** The inconsistent set is:
  - round-T H-FAR-MODEL;
  - H-RS2-ONE-PLANE;
  - H-STATIC;
  - H-BRANE-MATTER;
  - the board's four-dimensional readings (H-EXACT-ENERGY-AT-BOUND, H-PULL-IS-COST, the 4D bit area).

  Which member gives way is a choice. G3 and H1 are definitions, so they cannot be what gives.

**S5. In physical units.**
- **The corridor's mass length.** At the example README, m = 2.0×10⁻²⁸ m.
- **The four-dimensional bound.** ℓ ≲ 0.6m is about 1.2×10⁻²⁸ m.
- **What a round far surface would need.** ℓ > 7.9×10⁻²³ m through the old opening, or 4.5×10⁻²⁷ m through the old
  window.
- **What measurement says.** The table-top bound, ℓ ≲ 10⁻⁴ m, is an upper bound only.

## Verdict

- **The window is not shown empty.** Its upper side is a statement about round far surfaces only.
- **What actually constrains the corridor is KSCALE, read correctly.** It already closes a *static* corridor on *one*
  Randall–Sundrum plane at every ℓ: such a corridor would have γ = 1 when r₀ ≫ ℓ, and would be five-dimensional when
  r₀ ≪ ℓ.
- **Where the pressure falls.** On H-RS2-ONE-PLANE and H-STATIC-CORRIDOR, not on the far model.
- **KSCALE's own way out is a corridor that is not static, and items 160–162 supply exactly that.** The corridor exists
  only for a hold of h/(4E) (`o3_atonce.py`).
- **No B4 status moves on this stage's account.**

## Knock-on effects

- **Stage 1's D1** said the write forces the flat limit. That holds only for a round far surface; it is now flagged in
  `B4D-STAGE1.md`.
- **Stage 1's D2** gave the localized hole as ~580 m. That figure used the same round-surface ℓ; it is now flagged too.
- **B4a is unaffected.** Its deformation holds for any convex T, tipped ones included.

## History (verifier, 2026-10-08)

**What the verifier confirmed.** It ran the selftest (6/6), READ MK, IK and FW, confirmed the normalisation G₅ = Gℓ and
its convention-independence, and confirmed the physical figures.

**Its findings, all applied:**

**MUST-FIX**
1. **S3, the verdict and B4c all assumed a round T.** The tipped counterexample is now computed in `b4_global.py` and
   checked in both instruments. B4c's docstring and theorem row are corrected, and the stage-3 sentence is withdrawn.
2. **S2 used MK's tidal form outside its domain.** It is now FW's O(ℓ²/r₀²), an order of magnitude.
3. **The verdict picked which hypothesis gives way when none is forced.** The inconsistent set is now named,
   H-BRANE-MATTER included, and G3 and H1 are noted as definitions.
4. **KSCALE was misread.** It closes a static single-plane corridor at every ℓ. Its way out (a), a non-static corridor,
   is now cited, together with items 160–162.

**SHOULD-FIX**
5. **Two reach conventions were mixed.** There is now one, R_reach = (2 + hold)·m.
6. **Labels.** The tidal check is now a consistency check, the ℓ → 0 limit is STRUCTURAL, S1 is "deduced", the window
   is imported, and the round-versus-tipped control can fail.
8. **The note predated items 160–162.** It has been updated.

**NOTE**
7. **The normalisation is right** and convention-independent; MK's stronger, conjectural bound ℓ ≲ 10⁻² mm is noted.
9. **B4c has finite ℓ.** It is B4b that assumes the flat limit.
10. **Knock-on effects** are listed above.
