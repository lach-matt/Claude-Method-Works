# What the work says about k (M-RULINGS item 140; computed; the first derivation withdrawn; verified once; not seated; 2026-10-07)

*First headed* "k from the work (… derived, with one named hypothesis for the value; not verified …)". **The bound and
the value it gave failed verification and are withdrawn** (History).

## What you said

- **Item 140:** *"If k helps define the bulk, the math in our work should give you pieces to both derive and prove k.
  Our math is not dependent on k, k is dependent on our work."*
- **The instrument:** `kderive.py`. Selftest 7/7.
  - K1's transcription check and K3 restate algebra the instrument imports (exactE.py, multiplane.py). They are
    **STRUCTURAL**: they catch a copying error, not a physics error.
  - **Controls:** with G one part in 10⁹ high, K1's closed form misses; at a hundred times the withdrawn length, K4's
    inequality turns over.

## What the work fixes: the ratio of the two curvatures

- **From your quarter** (item 139: position 2's plane a quarter of ours, opposite sign), the tensions stand at
  **−1/4**, and the two curvatures at **k_R = 3k_L/4** exactly (multiplane.py M4).
- **That is a piece of k derived from the work**, as item 140 says it should be. It is a pure number, and it holds for
  every README.

## What the work does not fix yet: the scale

- **Every result of the chain so far is free of k.** E(N), the throat, γ = β = 5/4 at the corridor, the censorship
  verdicts and the positivity analysis all come out the same whatever k is (KSCALE.md, censor.py, positivity.py).
- **That is your sentence, read in the mathematics.** Your math does not depend on k. But for the same reason the math
  does not yet fix k: a quantity the results do not depend on cannot be read back off them.
- **To fix the scale, the work needs one dimensionful link between the corridor and the bulk.** That is, a place where
  a length of the corridor (its throat, r_min(N)) and the bulk's length ℓ = 1/k must meet. No such link has been found.
  **C, building the bulk with your planes, is where one could appear.**

## Where the chain is classical, whatever k is

- **The one-bit throat is exactly:**
  - **r_min(1) = 2G·E(1)/c⁴ = l_P·√(ln 2/π) = 7.5918511091462209829×10⁻³⁶ m**, or 0.4697 l_P;
  - the chain codes E as √(ħc⁵ ln2/(4πG)) per √bit (chain.py), which is the same expression. K1 checks the
    transcription.
- **One bit is below the Planck length.** Quantum-gravity corrections to a horizon of radius r go as (l_P/r)², the
  board's estimate of standard order, not READ. At r = r_min(N) that is **π/(N ln 2)**:
  - 4.5 at N = 1: one bit is not a classical object;
  - 1.65×10⁻¹⁵ at the board's example README (N = 2,742,570,311,524,972).
- **So the chain as written holds for READMEs of many bits** (H-MANY-BITS, the board's). That is a statement about the
  chain, not about k, and it does not touch your rulings.

## The withdrawn derivation, and why it failed

*First written:* a bound **k ≥ (1/l_P)·√(π/ln 2) = 1.3172×10³⁵ m⁻¹**, from "a corridor reads four-dimensional only if
it is large against ℓ" (Figueras–Wiseman), applied down to one bit; and a value, **ℓ = r_min(1)** (H-ONE-BIT-SCALE),
with a tension of 3c⁷/(4ħG²ln 2) and corrections 1/N.

- **It contradicted the board's own KSCALE.md.** In a one-plane bulk, a corridor large against ℓ gets γ = 1, not your
  5/4. So "large against ℓ" is where the corridor is absent, not where it holds.
- **It used a static result on a near-instantaneous corridor.** That is the escape KSCALE.md already uses in the other
  direction.
- **The value sat where its own premise fails.** At r = ℓ corrections are of order one. And at ℓ = r_min(1) the 5D
  Planck length exceeds ℓ (**ℓ/l5 = 0.6043**, K4), so no classical bulk is valid there.
- **No construction could have proved it.** A smaller ℓ carries the corridor at least as well, so "fails at other
  scales" could never happen from below.

## Your item 140, second part: position 2's plane is entangled

- **Carried:** H-ENTANGLED-PIN, with H-UNIVERSAL-ENTANGLEMENT (item 100).
- **Read against POSITIVITY.md's choices, it is (c):** something else that holds the pair.
- **What is and is not shown for it:**
  - positivity was shown only for (a), the fused, self-image surface;
  - a pair held apart at a fixed separation is a different configuration;
  - the energy of whatever holds it is not computed.
- **So the entangled pin is carried, not yet proved positive.** C must give the pin a form before its energy can be
  computed.
- **One standard fact, not read here:** in quantum mechanics, entanglement is a property of a state, not a force.

## Named hypotheses

- **The board's:**
  - H-MANY-BITS (the chain read classically, N ≫ 1);
  - H-QCORR-ORDER (corrections (l_P/r)², estimated, not READ).
- **Yours:**
  - M-K-FROM-THE-WORK and H-ENTANGLED-PIN (140);
  - H-P2-NEGATIVE-PLANE (139);
  - H-UNIVERSAL-ENTANGLEMENT (100).
- **Withdrawn:** H-FOUR-D-CORRIDOR, H-ONE-BIT-SCALE, H-ENTANGLED-AS-CONSTRAINT.

## OPEN

1. **C:** the dimensionful link between the corridor and the bulk, which would fix k's scale.
2. **C:** a form for the entangled pin, and its energy.

## History (verifier, 2026-10-07)

The verifier made eleven findings, and all are applied:

1. **K2 contradicted KSCALE.md.** In a one-plane bulk, large corridors get γ = 1. Withdrawn.
2. **A static result was applied to a corridor that is not static.** Withdrawn with K2.
3. **The value broke its own premise.** "≤" is not what Figueras–Wiseman support. Withdrawn.
4. **The proposed proof could not single out the value.** Withdrawn.
5. **The classical bulk fails at that scale**, and the note did not say so. It is now K4.
6. **H-FOUR-D-CORRIDOR was not the chain's own premise.** The chain neither posits a braneworld nor claims validity
   at one bit. Withdrawn.
7. **The entangled pin was mapped to (a), and positivity was overstated.** It is (c), and its energy is not computed.
8. **The refutation claim was too broad.** It is now withdrawn with the value.
9. **"Self-referencing" was overreach.** r_min(N)/ℓ = √N holds for every ℓ. Dropped.
10. **"Two disjoint paths" was a transcription check, and three checks were true by construction.** Now marked
    STRUCTURAL, with controls added.
11. **"30 orders" against 1.054×10³¹** in the docstring. The figure is gone with the value.
