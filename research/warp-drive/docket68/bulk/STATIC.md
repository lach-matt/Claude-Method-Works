# Static planes, moving surfaces (M-RULINGS item 141; READ and computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you said

- **Item 141:** *"If planes are constantly in motion around each other, a stable throat cannot form. I suggest the
  planes are static, but their surfaces contain their own movements from within their own contained dimensions.
  Imagine two rubiks cubes solving so that their facing sides match"*.
- **Carried:**
  - H-STATIC-PLANES;
  - H-INTERNAL-MOTION;
  - H-FACING-MATCH.
- **What it answers:** this gives item 140's entangled pin its form. The pin holds the separation fixed.
- **The instrument:** `static.py`. Selftest 17/17, with six controls.

## What passes

### 1. Static planes are a solution, at any separation (S1)

- **The tensions do not depend on the separation r.** In the Lykken–Randall bulk (Pilo–Rattazzi–Zaffaroni, eqs.
  2.16–2.17, READ), no force moves the planes, so a static configuration exists at every r, the coinciding one
  included.
- **The separation is still physical.** The 4D Planck mass depends on it. So "static" is a real condition, not a choice
  of coordinates.
- **Control:** with k_R = k_L that dependence vanishes, as it must.

### 2. With the planes static, the energy is positive (S2–S4): your item 139 order, met in what the board can compute

- **The force law on our plane splits exactly into two parts** (PRZ eq. 3.3, by their identity 3.4):
  - **a massless graviton**, (P2 − P0)/(8M̂²);
  - **the radion**, P0/C_r: the mode that moves the planes apart or together.
- **The split was checked against a control.** With the radion's coefficient doubled, it leaves a residue.
- **The radion is the only part with negative energy.** Its coefficient is C_r = −96 at the coinciding planes
  (positivity.py).
- **Static planes have no radion: the separation is not free to change.** What remains is positive in both senses:
  - **background:** the summed surface's null energy is λ·k_y², never negative (positivity.py Q3);
  - **dynamical:** the one remaining long-range mode, the graviton, has positive norm (coefficient 3/32 > 0 at the
    coinciding planes).

### 3. The surfaces can move without moving anything the bulk sees (S5)

- **The chain's energy reads the README's bit count, not its arrangement.** E = √N × the per-bit constant
  (exactE.py). The check that E depends on N alone is STRUCTURAL: it restates the chain's defining relation.
- **A reorganization of the README is a permutation of its states, and a permutation keeps the entropy exactly.**
  Landauer's erasure cost is therefore zero.
  - **Control:** erasing one bit lowers the entropy by one bit, which costs kT ln 2.
- **So motion on a surface that only reorganizes its content leaves the plane's energy, and its junction with the
  bulk, unchanged.** The plane stays static while its content moves.
- That is your H-REORGANIZATION (item 137), *"neither created nor destroyed, only reorganized"*, read on the surface.

### 4. A match is made, not found (S6)

- **Two surfaces whose N-bit arrangements match share exactly N bits of information.** Unmatched, independent ones
  share none. N bits is your passage, H-PASSAGE-IS-N (item 137).
- **Arrangements that match by chance do so with probability 2⁻ᴺ.** At the board's example README that is
  10^(−8.26×10¹⁴).
- **So the facing sides are matched by solving, as your image says.** Waiting for a chance match would never produce
  one.

### 5. Your image, run: two Rubik's cubes face to face (S7)

- **Face turns never move a centre.** The frame is static and the content moves: that is your planes.
  - **Control:** a middle-slice turn does move centres. So the frame is static under face turns specifically.
- **Every turn keeps each colour's count** (reorganization), and every quarter turn undone by three more (reversible).
- **Matching is mirror synchronization.** Cube A starts as the mirror image of cube B through the plane between them.
  - If A makes the mirror of each of B's moves, their facing sides stay matched through a 40-move scramble.
  - The mirror of a move: a turn about the axis between the cubes goes to the opposite layer, same sense; a turn about
    either other axis keeps its layer and reverses its sense.
  - **Control:** the same moves made unmirrored break the match.
- **A frame that is not shared can never be matched.** Centres never move, so if the two facing centres differ, no
  sequence of turns brings the facing sides together.
  - That is your one fixed exact encoding (item 136, answer 5): the frame must be shared before any solving.
- **This is an illustration of your image, not physics.** S7 shows a match kept under mirrored moves. Reaching a match
  from a mismatch is solving a cube; a standard result (not READ) is that any cube state solves in at most 20 face
  turns.

## What it costs, and what it does not settle

- **With the radion gone, the long-range field is Einstein's: γ = 1, not 5/4** (S2).
  - The 5/4 came entirely from the radion. That is exact: it is the only term beyond the graviton.
  - So static planes cannot give eq. (17)'s γ = 5/4 as a lasting far field.
  - **Your corridor is near-instantaneous** (items 86, 94, 136 E). A field that lasts only for the hold does not reach
    far, so a lasting far field is not required.
  - **But it moves the question.** The corridor's own field during the hold must come from the corridor and its
    surfaces, not from the planes moving. That is C.
- **The quarter is now your ruling alone.** It was first chosen because the radion then gives 5/4. With the radion
  gone, nothing in the bulk requires it.
  - It stands as H-P2-NEGATIVE-PLANE (item 139), and k_R = 3k_L/4 still follows from it (kderive.py K3).
- **"Static" must be a constraint, not a restoring force** (S3).
  - If the planes were held at their separation by a restoring force, the mode would still have negative energy: a
    massive ghost. At C_r = −96 its energy at rest position and unit speed is −48, for every strength of the force.
  - Only a constraint removes it: the separation not a variable at all.
  - The board reads your "static" that way (H-STATIC-AS-CONSTRAINT). A constraint holding a static system does no work,
    so it adds no energy. That is standard mechanics, carried as an idealization into the bulk.
- **The board's reading of the moving content: the plane's stress sees how much content there is, not how it is
  arranged** (H-ENERGY-BLIND). Without it, content moving in place would make the stress vary from point to point, and
  the plane would not be static locally.
- **Not computed:**
  - the massive graviton tower (not read);
  - a positive-energy theorem for anti-de Sitter with branes (not read);
  - the surfaces' own contained dimensions.
- **k:** static planes add no length, so k's scale stays unfixed. If the surfaces' contained dimensions have a size,
  that would be a candidate for the link between corridor and bulk. That is open, for C.

## How the board now reads the configuration

- **The planes sit face to face, coinciding in the extra dimension (item 127), and never move.** This is the board's
  reading (H-FACE-TO-FACE), from your two cubes touching.
- **The corridor is not formed by the planes coming together.** It forms when their facing surfaces match.
- **The positivity concern about the planes passing through a separated state** (POSITIVITY.md) therefore does not
  arise: they never separate.

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES, H-INTERNAL-MOTION, H-FACING-MATCH (141);
  - H-ENTANGLED-PIN (140);
  - H-P2-NEGATIVE-PLANE, M-PROVE-POSITIVE (139);
  - H-PASSAGE-IS-N, H-REORGANIZATION (137);
  - H-FIXED-ENCODING, H-FORMATION-IS-SYNCHRONIZATION (136);
  - H-PLANES-COINCIDE (127).
- **The board's:**
  - H-STATIC-AS-CONSTRAINT;
  - H-ENERGY-BLIND;
  - H-FACE-TO-FACE;
  - H-LR-ZERO-MODE (multiplane.py).

## OPEN

1. **C:** the corridor's field during the hold, in a static bulk, made by its surfaces matching.
2. **C:** whether the surfaces' contained dimensions supply the length that fixes k's scale.
3. The massive tower and a positive-energy theorem, still to be read.
