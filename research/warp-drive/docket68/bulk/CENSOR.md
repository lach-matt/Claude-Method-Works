# The censorship theorems against your plane's bulk (M-RULINGS items 136-137, wall D; computed and READ; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you asked

- **Item 136, wall D:** *"yes, or prove that a censorship theorem does not apply"*.
- **The instrument:** `censor.py` takes seven censorship and time-delay theorems, five READ in step 2 and two after the
  verifier. It checks each premise against the board's bulk:
  - vacuum AdS₅ off the plane;
  - the plane a matter-free umbilic brane carrying the corridor;
  - the two sides mirror images.
  - Each verdict is derived from the premises' statuses: a premise that robustly FAILS (backed by a computed check), one
    that fails only under a named choice (DEPENDS), or OPEN.
  - Selftest: 15/15.

## What passes

- **The theorem on the plane itself does not apply.** Friedman–Schleich–Witt (gr-qc/9305017v2 p.3) needs the averaged
  null energy condition in the focusing form its proof uses. The plane reads it negative along the passage, −0.826436
  E/m per leg (coin.py).
  - The plane's own matter keeps it trivially, since there is none.
  - What breaks it is the bulk's Weyl part projected onto the plane (E_kk = −G_kk, umbilic.py). The plane does not obey
    4D Einstein equations.
- **The finite-boundary theorems do not apply** (Chruściel–Galloway–Solis, arXiv:0808.3233v2, READ).
  - Their Thms 3.1 and 3.5 need the boundary's time slices to be compact. An infinite plane's are not.
  - Their Thms 5.2 and 5.3 need a compact internal space. **Your answer 9 makes the extra dimension unbounded, and that
    is what keeps them from applying.**
  - **Control:** in a compact bulk (a Randall–Sundrum I interval), with the null energy condition, Thm 5.2 would apply.
    It would forbid any causal curve from one end of the corridor to the other: *"J⁺(M_ext^λ1) ∩ J⁻(M_ext^λ2) = ∅"*
    (p.10).

## What does not close: the bulk theorems depend on two choices, one of them yours

- **Gao–Wald Thms 1 and 2, and Galloway–Schleich–Witt–Woolgar's two theorems, DEPEND on named choices:**

| theorem | the choice it depends on |
|---|---|
| Gao–Wald Thm 1 | the sign of your plane's tension (the null energy condition); the bulk ending at the Poincaré horizon (completeness). Its generic condition plausibly holds with the corridor present, and its smoothness premise is a technicality: a thick plane keeps the null energy condition |
| Gao–Wald Thm 2; GSWW Thm 2.1; GSWW Thm 1 | the bulk ending at the Poincaré horizon. Inside that patch there is no boundary where Ω = 0; continued past it, global AdS has one |

- **First choice: the sign of your plane's tension (H-OUR-TENSION).**
  - On the plane the null energy is S_AB·k^A·k^B = λ·k_y², for every null vector.
  - With positive tension, the null energy condition holds everywhere in five dimensions, and your *"An NEC is never
    violated"* holds in the model.
  - With negative tension it fails on the plane. The board's earlier reading of Randall–Sundrum I (H-RS1, SIGNDIM.md)
    put our matter on the negative-tension plane.
  - The mirror symmetry alone does not fix the sign: K = −k·g gives λ > 0, K = +k·g gives λ < 0.
  - **So "never violated" is consistent with a positive-tension plane, and only that.** It also rests on a bulk carrying
    eq. (17) existing at all (C).
- **Second choice: where the bulk ends (H-POINCARE-PATCH).** This is decided by building the bulk (C).
- **If those theorems do apply, what would they forbid?** Gao–Wald Thm 1 is a time-delay theorem: the fastest
  connections between distant points avoid a compact region. The corridor is not a shortcut through space, since its
  two positions coincide (item 127). How such a theorem bears on it is open.

## The checks

- **C1.** S_kk = λ·k_y² on the plane; 0 in the bulk.
- **C2.** E_kk = −G_kk (umbilic.py, cited).
- **C3.** Pure AdS₅ fails the generic condition everywhere: exact maximal symmetry, residual 0.
  - **Control:** a non-radial Schwarzschild ray gives 20.25.
  - **Contrast:** a radial one gives 0, along a principal null direction.
- **C4.** Ω = k·z ≥ 1 inside the Poincaré patch.
- **C5.** The Poincaré horizon is at affine parameter 1/(k·ε·sin θ).
- **C6.** −0.826436 E/m per leg.
- **C7.** [K] ≠ 0 across a thin plane.
- **C8.** The plane's time slices are ℝ³.
- **C9.** The extra dimension is unbounded (your answer 9).

## What this does and does not show

- **It shows** that the plane's own censorship theorem and the finite-boundary ones do not apply. The second rests on
  your unbounded extra dimension.
- **It does not show** that the bulk theorems do not apply. They depend on the tension's sign and on where the bulk
  ends.
- **A theorem that does not apply also permits nothing.**
- **Not read:** Galloway's "finite infinity" theorem (CQG 13, 1996), which Chruściel–Galloway–Solis generalise.

## Named hypotheses

- **The board's:**
  - H-Z2;
  - H-VACUUM-PLANE;
  - H-VACUUM-BULK;
  - H-POINCARE-PATCH;
  - H-OUR-TENSION (positive), against the earlier H-RS1 (negative).
- **Yours:** items 117, 120, 122, 136 (answer 9; wall D).

## OPEN

1. **The sign of your plane's tension.** Yours to say.
2. Where the bulk ends (C).
3. Galloway's variant ("no null line") and global hyperbolicity: not checked.

## History (verifier, 2026-10-07)

Fourteen findings were applied:

- **The generic condition was judged on pure AdS, without the corridor.** It is now OPEN, plausibly holding.
- **The smoothness and completeness failures were fragile.** Smoothness is now a technicality, and completeness depends
  on the Poincaré patch.
- **Positive tension is H-OUR-TENSION, not H-Z2.** It conflicts with the board's H-RS1.
- **Two theorems were missing** (Chruściel–Galloway–Solis). They are now READ and checked.
- **Step 2's reading was wrong.** It said every theorem needs a boundary at infinity; Gao–Wald Thm 1 needs completeness
  instead. Corrected here.
- **Verdicts are now derived from premise statuses**, and each FAILS must be backed by a check that passed.
- **FSW's ANEC is stated in its focusing form.**
- **Premise lists are completed.**
- *First written:* "None of the five theorems applies", and "Your *An NEC is never violated* … is a result of this
  model". Both withdrawn as stated.
