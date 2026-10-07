# A bulk of more than one plane, against the corridor's far field (M-RULINGS item 138; READ and computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you said

- **Item 138:** *"the problem is that you assume the bulk is contained to a single plain. It is not. I keep saying, it
  is multi-universal."*
- **The question:** does a bulk of more than one plane give the corridor's far field, γ = β = 5/4?
- **The instrument:** `multiplane.py`. Selftest 13/13, with controls.

## What passes: with a second plane, the corridor's γ = 5/4 is reached

- **The source.** In the Lykken–Randall two-plane bulk (Pilo–Rattazzi–Zaffaroni, hep-th/0004028v2, READ), gravity on
  our plane is a tensor–scalar theory, from their eq. (3.3).
  - Its post-Newtonian γ works out to **γ = (3 + X)/(3 − X)**, with X = e^{−2k_L·r}(k_L − k_R)/k_R.
  - Here k_L is the bulk's curvature between the planes, k_R beyond the second plane, and r their separation.
  - The transcription checks itself: their own identity, eq. (3.4), holds exactly from their eqs. (2.16) and (2.17).
- **γ = 5/4 exactly when X = 1/3.** That needs k_R < k_L: the second plane has **negative tension**.
  - **Control:** a positive-tension second plane gives γ < 1.
  - **Control:** taking the planes far apart recovers one plane's γ = 1.
- **With the planes coinciding, as your item 127 has them (r = 0):**
  - **γ = 5/4 at k_R = 3k_L/4.**
  - Our plane's tension is then **+4/3** of the one-plane value, and the second plane's **−1/3**.
  - The two sum to exactly the one-plane value, which is the coinciding-junction sum rule computed earlier (LOOSE.md L4).
  - In this reading **your plane is the positive-tension one** (question 2). Position 2's is negative, with a quarter of
    ours in magnitude.
- **So your multi-universal bulk does what one plane cannot.** And the condition depends on neither N nor m, so it
  holds for every README: γ = 5/4 is independent of the corridor's size.
- **The shadow-matter fingerprint carries too.** In Garriga–Tanaka's bulk, matter on another plane gravitates on ours
  with γ = 1/2, bending light 3/4 as much for the same pull. That is their published result, re-derived here; it needs
  an unstabilized radion.

## What it costs

- **The negative-tension plane is free to move, so the mode that moves it (the radion) carries negative energy.**
  - Pilo–Rattazzi–Zaffaroni, abstract: *"The model violates positivity of energy due to a negative tension brane, which
    induces a negative kinetic term for the radion."*
  - p.11: *"the need for a non-decoupling massless and ghost-like radion is always associated with the presence of a
    brane of negative tension."*
  - At r = 0 the radion's coefficient is C_r = −96M³/k_L, negative.
- **So in five dimensions the null energy condition fails on the second plane.** That is against *"An NEC is never
  violated"*, unless it is read as your *"appears to"*.
- **Read on our plane, γ = 5/4 already breaks the null energy condition in the far field, whatever builds it.**
  - At large r, ρ + p_r = (1 − γ)·m/(4πr³), which is negative when γ > 1. That is the verifier's arithmetic, checked by
    the board.
  - The board has held this as an appearance since your item 117 (opening.py O3). The second plane is where the
    appearance would come from.
- **Three cautions:**
  - **Analogy, not derivation.** Lykken–Randall's γ is for matter on our plane, at linear order and long range. The
    corridor is a plane with no matter whose far field comes from the bulk. Making the comparison exact needs a bulk
    matched to eq. (17)'s two far-field coefficients.
  - **r = 0 extends their model** to coinciding planes. That is the board's extension.
  - **The radion is left unstabilized.** Stabilizing it changes the long-range answer (PRZ p.10).

## What changed from the first draft

- *First written:* "more planes do not give γ = 5/4 … the remaining way out is (a)".
  - That held only for Garriga–Tanaka's orbifold bulk, where the negative plane sits at a fixed point and its moving
    mode is projected out (PRZ p.3). There γ < 1 always: 1 − γ₊ = 2/(3e^{2x} + 1) and 1 − γ₋ = 2e^{2x}/(e^{2x} + 3).
  - With the negative plane free to move, γ > 1 is reached. The verifier found this; the board re-derived it.
- *First written:* "the dividing line is negative energy". The dividing line is a negative-tension plane free to move,
  which gives a ghost radion (PRZ).
- **Way out (a), a corridor that exists only for the hold, stays open beside this.** If the hold is shorter than the
  light-crossing time, no far field forms. But then eq. (17), a static metric, is not the geometry during the hold
  either, and C must build a bulk that changes in time.

## Named hypotheses

- **The board's:**
  - H-LR-ZERO-MODE (Lykken–Randall at linear order, zero modes only, radion unstabilized);
  - H-COINCIDE-LIMIT (r = 0);
  - H-VACUUM-AS-SOURCE (the corridor's far field compared with a matter-sourced one).
- **Yours:** H-MULTIVERSAL-BULK, H-ELEMENTS-PER-UNIVERSE (138); H-PLANES-COINCIDE (127); items 117, 120.

## OPEN

1. **Is position 2's plane the negative-tension plane, a quarter of ours, and our plane the positive one?**
2. **Is the negative energy its radion carries an appearance (your item 120), or does it break "never violated"?**
3. **Static, or only for the hold?** If static, this bulk is the candidate C builds; if only for the hold, C builds one
   that changes in time.
4. **The exact match:** a bulk carrying eq. (17)'s own far field on coinciding planes (C).

## History (verifier, 2026-10-07)

Seven findings were applied:

- **The Lykken–Randall model** reaches γ = 5/4, overturning the first conclusion. Its mapping was re-derived and checked
  against PRZ's eq. (3.4).
- **The dividing line is a negative-tension plane free to move**, not negative energy as such.
- **The vacuum corridor against a matter-sourced field** is now labelled analogy.
- **Way out (a) is narrowed**, and (c) is kept.
- **The shadow-matter fingerprint** is GT's own result, and needs an unstabilized radion.
- **The γ < 1 forms are now exact.** By-construction checks were replaced with derived ones.
- **Cross-references.** SIGNDIM.md and MANYPLANES.md already read Garriga–Tanaka and the many sheets.
