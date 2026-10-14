# Is the energy positive on the coinciding planes? (M-RULINGS item 139; READ and computed; verified once; not seated; 2026-10-07)

*First headed* "The energy is positive: a proof for the coinciding planes (… not verified …)". **That proof failed
verification and is withdrawn** (History).

## What you said

- **Item 139, answer 1:** position 2's plane is the negative-tension one, a quarter of ours, and ours is positive.
- **Answer 2:** *"positive, and you have to prove it."*
- **The instrument:** `positivity.py`. Selftest 8/8.
- **Two kinds of positivity, kept apart:**
  - **background:** the stress of the surfaces and the bulk as they sit;
  - **dynamical:** no mode with negative kinetic energy.

## What holds: the background is positive

- **The coinciding sheets act as one surface** (Israel's condition is linear in the stress, LOOSE.md L4).
  - Our tension is +4/3, position 2's −1/3, summed **+1** times the one-plane value.
  - On that surface the null energy is λ·k_y², **never negative for every null vector** (Q3).
  - A pure positive tension also satisfies the stronger dominant energy condition.
- **The bulk's null energy is 0** (censor.py C1).
- **So the five-dimensional stress, as it sits, keeps the null energy condition.**
  - Position 2's sheets taken alone would read −(1/3)·λ·k_y²; summed with ours they never do.
  - That is an illustration of your coin (item 117), under the board's reading H-COMPOSITE-SURFACE. Your item 120 calls
    the coin a metaphor.

## What does not hold: the mode that moves position 2's plane carries negative energy

- **In the two-plane bulk the board uses (Lykken–Randall), position 2's plane is a mirror pair:** a sheet at +r and its
  image at −r.
  - Moving both by f keeps the mirror symmetry for every f (Q2). **So the mode survives**, including from the
    coinciding endpoint r = 0.
  - Pilo–Rattazzi–Zaffaroni p.4 (READ) say it for this plane: *"the translational degrees of freedom of this brane are
    not projected out."*
- **Its kinetic coefficient is negative.** C_r = −72e − 24 apart, and −96 at r = 0 (units M = k_L = 1; k_R = 3k_L/4).
  It is a ghost at the coinciding planes too (Q1).
- **The −1/3 is the pair, sheet plus image.** PRZ's jump rule gives one sheet −1/6, and only the pair closes the sum
  rule (Q3). So "a quarter of ours" is the pair's total against ours.
- **The plane's own reading is also negative:** the averaged null energy along the passage is −0.826436 E/m per leg
  (Q4, coin.py). That is the four-dimensional appearance your item 117 described.
- **So, as you specified the configuration, the energy is not dynamically positive.** The computation shows the
  opposite, a ghost, and that is what the literature computes for a free negative-tension plane (PRZ p.11). The board
  cannot prove it positive. That is a finding, not a gap.

## The one configuration that is positive, and what it costs

- **If position 2's sheets are fused with ours into one surface that is its own mirror image**, a displacement is
  identified with its negative and must vanish (Q2 control). There is no radion, and the energy is positive in both
  senses.
- **But that surface is one Randall–Sundrum plane under another name.**
  - Its total tension is +1, and nothing distinguishes the +4/3 and −1/3 inside it.
  - The quarter was chosen to give γ = 5/4 through the radion. With the radion gone, nothing fixes it.
  - A lasting source there has γ = 1 (Q5). Your near-instantaneous corridor does not need a lasting field.
- **Your coinciding planes exist only "while the corridor exists"** (item 127), and the corridor is near-instantaneous.
  So for almost all the time position 2's plane is apart, and forming or dissolving the coincidence passes through
  r > 0, where the ghost is live (Q1).

## What this does and does not show

- **It shows:**
  - the background stress keeps the null energy condition;
  - the free pair's radion is a ghost at every separation, the coinciding one included;
  - only a fused, self-image surface removes it.
- **It does not settle:**
  - **a positive-energy theorem** for anti-de Sitter with branes, not read;
  - **the radion's endpoint dynamics:** whether a source pushes the pair apart or holds it at r = 0;
  - **the corridor's own geometry during the hold;**
  - **matter on position 2's sheets** (your item 139's absorption of the README);
  - **the massive graviton tower**, not read;
  - **the vacuum-hair route.** A healthy scalar with a charge of the opposite sign could give γ > 1 without a ghost, but
    that needs position 2's plane positive, against your answer 1.

## Named hypotheses

- **The board's:**
  - H-COMPOSITE-SURFACE (background only);
  - H-LR-PAIR (position 2's plane as LR's mirror pair);
  - H-FUSED (the alternative: one self-image surface).
- **Yours:** H-P2-NEGATIVE-PLANE, M-PROVE-POSITIVE (139); H-PLANES-COINCIDE (127); items 117, 120.

## OPEN

1. **Your ruling:**
   - (a) position 2's sheets fused with ours (positive; the negative tension becomes inner structure with no motion of
     its own);
   - (b) a free pair (a ghost, computed);
   - (c) something else that pins the pair.
2. A positive-energy theorem for the configuration you choose.

## History (verifier, 2026-10-07)

- **The first draft's step 1** said the coinciding planes carry no radion because a sheet at the mirror plane cannot
  move. That holds for one sheet that is its own image, not for LR's mirror pair, whose mode survives to r = 0.
  Withdrawn.
- **Its Q1 showed the ghost only apart.** At r = 0 it is negative too.
- **"Positive in every part the board can compute"** left out the plane's computed −0.826436.
- **PRZ's footnote 6** keeps a radion on a composite at a fixed point; it was cited as support. Corrected.
- **The coin mapping** is now an illustration.
- **"Exclude each other" is scoped**, and the vacuum-hair route is named.
- **Tautological checks were replaced.** Q2 now tests the pair against a self-image sheet.
- **The −1/3 is the pair, not one sheet.**
