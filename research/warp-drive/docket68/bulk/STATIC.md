# Static planes, moving surfaces (M-RULINGS item 141; READ and computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft reported your item 139 order met; that was
an over-read and is corrected (History).

## What you said

- **Item 141:** *"If planes are constantly in motion around each other, a stable throat cannot form. I suggest the
  planes are static, but their surfaces contain their own movements from within their own contained dimensions.
  Imagine two rubiks cubes solving so that their facing sides match"*.
- **Carried:**
  - H-STATIC-PLANES;
  - H-INTERNAL-MOTION;
  - H-FACING-MATCH.
- **What it answers:** it gives item 140's entangled pin its form. The pin holds the separation fixed.
- **The instrument:** `static.py`. Selftest 19/19.
  - **Controls (seven):** S1, S2, S2b, S3, S5, and two in S7 (unmirrored moves, a middle slice).
  - **Marked READ or STRUCTURAL:** five checks restate a source or the instrument's own construction (S1, S2's split,
    S5's E(N), and two in S7).
- **Units:** wherever a number is given for the coinciding planes, M = k_L = 1 and k_R = 3/4.

## What passes

### 1. Static planes are a solution, at any separation (S1, READ)

- **The tensions do not depend on the separation r** (Pilo–Rattazzi–Zaffaroni, "PRZ", p.3). No force moves the planes,
  so a static configuration exists at every r, the coinciding one included.
- **The separation is still physical.** The 4D Planck mass depends on it, so "static" is a real condition.
- **Control:** with k_R = k_L that dependence vanishes, as it must.

### 2. Static and face to face, your two planes are one Randall–Sundrum plane (S2, S2b)

- **The force law on our plane splits exactly into two parts.** PRZ state it themselves (p.10), and the instrument
  re-derives it from their eqs. 3.3–3.4:
  - **a massless graviton**, (P2 − P0)/(8M̂²);
  - **the radion**, P0/C_r: the one mode that moves the planes apart or together.
- **Remove the radion, as static planes do, and the force law is Einstein's: γ = 1.**
  - The instrument reads γ off the split, rather than assuming it.
  - **Scope:** this holds in PRZ's long-range (zero-mode) part. Their eq. 3.5 adds a massive tower, which is not read.
- **At the coinciding planes, with the radion removed, the pair *is* one Randall–Sundrum plane of curvature k_R.**
  - The 4D Planck mass becomes M³/k_R, the one-plane value, and k_L drops out.
  - **Control:** with the planes apart, k_L enters.
- **This is POSITIVITY.md's fused case (a), reached by another road.** Your entangled pin was read as (c), "something
  else that holds the pair". Once the pin holds the planes static and face to face, (c) cannot be told apart from (a)
  by anything at long range.

### 3. In that form the energy is positive (S4)

- **Background:** the summed surface's null energy is λ·k_y², never negative (positivity.py Q3). That rests on reading
  the two sheets as one surface (H-COMPOSITE-SURFACE). Position 2's sheet alone reads −(1/3)·λ·k_y².
- **Dynamical:** the one remaining long-range mode, the graviton, has positive norm (coefficient 3/32 > 0).
- **There is one known way to remove the separation as a variable: a surface that is its own mirror image** (PRZ p.3,
  where the displacement is "projected out"). At the coinciding planes that is exactly the one plane above.

### 4. The surfaces can move without changing the plane's energy (S5)

- **The chain's energy reads the README's bit count, not its arrangement.** E = √N × the per-bit constant (exactE.py).
  That check is STRUCTURAL: it restates the chain's defining relation.
- **A reorganization of the README is a permutation of its states, and a permutation keeps the entropy exactly.** So
  the Landauer lower bound for it is zero. The check uses a non-uniform distribution, so it can fail.
  - **Control:** erasing one bit lowers the entropy, and that costs at least kT ln 2.
- **That is your H-REORGANIZATION (item 137), read on the surface.**
- **Whether the bulk then sees nothing is a further step: H-ENERGY-BLIND (the board's).** It says the plane's stress
  reads how much content there is, not how it is arranged. Landauer bounds erasure only. It says nothing of the
  motion's own kinetic energy or dissipation.

### 5. A match is made, not found (S6)

- **Two surfaces whose N-bit arrangements match share exactly N bits of information.** Independent ones share none. N
  bits is your passage, H-PASSAGE-IS-N (item 137).
  - Both figures assume a uniform prior over arrangements. For one fixed, known encoding, the information needs a
    distribution to be defined at all.
- **Counted as possibilities, a chance match has probability 2⁻ᴺ.** At the board's example README that is
  10^(−8.26×10¹⁴).
- **So the facing sides are matched by solving, as your image says.**

### 6. Your image, run: two Rubik's cubes face to face (S7, an illustration)

- **Face turns never move a centre.** The frame stays static and the content moves.
  - **Control:** a middle-slice turn does move centres.
- **Every turn keeps each colour's count, and four quarter turns return the cube** (reorganization, reversible).
- **Matching is mirror synchronization.**
  - Cube A starts as the mirror image of cube B through the plane between them.
  - If A makes the mirror of each of B's moves, their facing sides stay matched through a 40-move scramble.
  - The mirror of a move:
    - a turn about the axis between the cubes goes to the opposite layer, same sense;
    - a turn about either other axis keeps its layer and reverses its sense.
  - **Control:** the same moves made unmirrored break the match.
- **Tracking move for move needs the shared mirror colour scheme.** A cube can be reoriented to bring one face into
  line and solve that face. But only the mirror twin can follow the other cube turn by turn.
- **The board maps that to your one fixed exact encoding** (item 136, answer 5). The mapping is the board's.
- **Reaching a match from a mismatch is solving a cube.** A standard result, not READ: any state solves in at most 20
  moves when half turns count as one move, 26 when only quarter turns are allowed.

## What it costs, and what it does not settle

- **Positive only in the one-plane form.** For a negative-tension sheet held at a fixed place by anything else, PRZ p.2
  (READ): *"the kinetic coefficient of the radion is proportional to the brane tension, which is negative. This fact
  makes the issue of radion stabilization very unclear and probably not even well posed."*
- **A restoring force does not cure it** (S3).
  - With C_r = −96, a radion held by any restoring potential runs away exponentially, and its energy is unbounded
    below.
  - **Control:** with C_r = +96 the same potential gives an oscillation.
  - This is PRZ p.9, READ: *"giving a mass to a field with negative kinetic term clearly does not remove the
    associated instability."*
- **And once matter sits on a sheet, the radion is sourced** (PRZ p.8). Holding that sheet in place then needs a bulk
  field, and that field's energy is not computed.
- **So M-PROVE-POSITIVE is met in one form and open in all others:**
  - **met:** the coinciding sheets as one self-image surface, which is what static, face to face, reduces to;
  - **open:** any form in which position 2's sheet keeps a place of its own.
- **In the one-plane form, your quarter is invisible to every long-range observable.** k_L drops out, so the +4/3 and
  −1/3 are inner structure. The quarter stands as your ruling (H-P2-NEGATIVE-PLANE, item 139), and k_R = 3k_L/4 still
  follows from it (kderive.py K3). No long-range measurement would see it.
- **With the radion gone, the long-range field is Einstein's (γ = 1), not eq. (17)'s 5/4.** Whether the corridor needs
  a lasting field with 5/4 is OPEN. C must compute the corridor's field during the hold, made by its surfaces matching.
  - The board's way out (a) in MULTIPLANE.md, that a near-instantaneous corridor forms no lasting field, stays a board
    hypothesis (H-NO-LASTING-FIELD), not a result.
- **Not computed:**
  - the massive graviton tower and a positive-energy theorem for anti-de Sitter with branes (not read);
  - matter on the sheets (here, matter on one Randall–Sundrum plane);
  - the surfaces' own contained dimensions.
- **k:** static planes add no length, so k's scale stays unfixed. If the surfaces' contained dimensions have a size,
  that is a candidate for the link between corridor and bulk. That is open, for C.

## How the board reads the configuration

- **Your item 127 has the planes coinciding "while the corridor exists". Your item 141 has them static.** Static at all
  times, and coinciding whenever the corridor exists, means they coincide always. Any change of separation would be
  motion.
  - This is the board's derivation (H-FACE-TO-FACE), and it fits your two cubes touching.
  - It replaces POSITIVITY.md's earlier reading, that position 2's plane is apart for almost all the time.
- **The corridor is not formed by the planes coming together.** It forms when their facing surfaces match.
- **The cost of the derivation is section 2's:** the pair is then one Randall–Sundrum plane at long range.

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES, H-INTERNAL-MOTION, H-FACING-MATCH (141);
  - H-ENTANGLED-PIN (140);
  - H-P2-NEGATIVE-PLANE, M-PROVE-POSITIVE (139);
  - H-PASSAGE-IS-N, H-REORGANIZATION (137);
  - H-FIXED-ENCODING, H-FORMATION-IS-SYNCHRONIZATION (136);
  - H-PLANES-COINCIDE (127).
- **The board's:**
  - H-FACE-TO-FACE (derived from 127 and 141);
  - H-COMPOSITE-SURFACE (positivity.py);
  - H-ENERGY-BLIND;
  - H-NO-LASTING-FIELD (MULTIPLANE.md's way out (a));
  - H-LR-ZERO-MODE (multiplane.py), used here with the radion removed rather than unstabilized.

## OPEN

1. **C:** the corridor's field during the hold, in a static bulk, made by its surfaces matching.
2. **C:** whether the surfaces' contained dimensions supply the length that fixes k's scale.
3. Positivity for any form in which position 2's sheet keeps a place of its own (PRZ p.2: probably not well posed).
4. The massive tower and a positive-energy theorem, still to be read.

## History (verifier, 2026-10-07)

The verifier made twelve findings, and all are applied:

1. **"Positive … your order met" was over-claimed.** It rested on a constraint that PRZ p.2 calls probably not well
   posed for a negative-tension sheet, and the energy of whatever holds the sheet was dropped. It is now "met in the
   one-plane form, open otherwise".
2. **The main under-claim:** static and face to face, the pair *is* one Randall–Sundrum plane (S2b, added). k_L and the
   quarter are invisible at long range.
3. **S2 is PRZ's own split** (p.10), so it is marked READ. Its scope, the zero modes only, is stated.
4. **S3 was mislabelled.** The motion is a runaway, not an oscillating "massive ghost". It is now checked as such, with
   a real control, and PRZ p.9 is cited.
5. **Checks true by construction are marked.** γ = 1 is now read off the split, and the permutation check uses a
   non-uniform distribution.
6. **"A frame not shared can never match"** holds for face turns with orientation held. Qualified. The mapping to item
   136 is labelled the board's. "20 moves" now gives its metric.
7. **H-FACE-TO-FACE now carries its derivation** from items 127 and 141.
8. **S5's claim was conditional.** H-ENERGY-BLIND is now named there, and Landauer is read as a lower bound.
9. **"A field that lasts only for the hold does not reach far"** was not computed. It is now OPEN, with way out (a) as
   a named board hypothesis.
10. **H-COMPOSITE-SURFACE** is listed. Matter on the sheets is restored to "not computed".
11. **S6's uniform prior** is stated.
12. **Units** are stated.
