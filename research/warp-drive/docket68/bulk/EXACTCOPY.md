# No tolerance, and an encoding in what every universe shares (M-RULINGS item 146; deduced and computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft claimed a molecule's equilibrium geometry
as an exactly realizable invariant, and offered no-cloning as support for "only one"; both were wrong (History).

## What you said

- **Item 146:** *"1 - no tolerance at all. 2 - yes"*.
- **Carried:**
  - H-NO-TOLERANCE: a complete reconstruction is exact;
  - H-INVARIANT-ENCODING: the one fixed exact encoding is written in what every universe shares, *"such as element
    identity and electron configuration"*. This was the board's offer; it is now yours.
- **The instrument:** `exactcopy.py`. Selftest 4/4.
  - **Genuine checks:** three.
  - **Control:** one.
  - **Marked STRUCTURAL:** one.

## What passes

### 1. Under no tolerance, what an encoding can carry exactly is discrete labels

- **Labels survive exactly:**
  - an element's identity, Z;
  - its electron configuration;
  - a molecule's vibrational and rotational quantum numbers.
- **Continuous values do not:** a bond's mean length, a frequency. They depend on the nuclear-to-electron mass ratio.
  - Beyond the simplest picture they also depend on nuclear size and on small corrections of order mₑ/M.
  - Your item 144 lets those differ.
- **So the board reads your encoding as an encoding in labels.** That is the board's reading of "what every universe
  shares". It adds the molecular quantum numbers to your examples.

### 2. A label holds exactly across a finite range of mass ratio (X3)

- **On a hydrogen-molecule model** (a Morse oscillator with standard constants, not READ here):
  - it holds 17 bound vibrational levels, v = 0 to 16;
  - **that label set is exactly the same for every reduced mass from 0.898 to 1.010 of ours** (−10.2% to +1.03%).
    Outside that window a level appears or vanishes.
- **Control:** just outside each edge of the window, the count changes, from 16 to 17 and from 17 to 18.
- **So an encoding in labels meets "no tolerance at all" exactly, across a finite window of the laws you allow to
  differ.** It does not need position 2's masses to match ours exactly.
- **A condition beside it:** each label must exist at position 2.
  - Each named element must have a nucleus that exists there (item 144, as the board reads it).
  - Each named level must be bound there. That is the window above.

### 3. What labels cannot fix: the values (X1, X2)

- **A molecule never sits at its equilibrium shape.** Zero-point motion sets its mean bond length 3.1% above
  equilibrium in the model.
  - The closed form agrees with direct numerical integration to a part in 10⁶.
  - Real H₂ is about 3.4%, the verifier's figure, not READ; the model runs about 10% low.
- **Change the reduced mass by a part in 10⁷, and the mean bond length shortens by 1.6 parts in 10⁹.** That scaling
  is STRUCTURAL.
- **The equilibrium shape is a parameter of the equations, not a state a copy can be in.** It does not count as an
  exactly realizable invariant.

## What this does to the question of the copy's motion

- **Question (a) or (b) narrows to this: is the README the labels, or the values?**
  - **(b) the labels.** The copy is exact in every label it names. Its mean lengths and frequencies are what position
    2's laws make of those labels.
    - This is the board's H-COPY-TAKES-P2-LAWS (nucleus.py), now restricted to values.
    - It meets "no tolerance at all" if exactness is measured against the README, in the README's own atomic units.
  - **(a) the values.** The copy is exact only where position 2's mass ratio, nuclear size and the small corrections
    all match ours exactly. That would withdraw H-COPY-TAKES-P2-LAWS.
    - Item 138's *"measure exactly as are ours do"* bears on it.
- **Your answers so far point to (b):** item 146 places the encoding in what every universe shares, and values are not
  shared. That reading is the board's.

## On "only one"

- **Item 146 settles your "only one" as exactness, not as a count of copies.**
- **A README of labels is a known, classical specification.** The no-cloning theorem (Wootters and Zurek 1982;
  standard, not READ here) covers only unknown quantum states, so it does not bear on the README.
- **It fits elsewhere:** your item 136, answer 4 (the original is irrelevant) is consistent with no-cloning and with
  teleportation, where the original state is consumed.

## Named hypotheses

- **Yours:**
  - H-NO-TOLERANCE, H-INVARIANT-ENCODING (146);
  - H-ONE-RECONSTRUCTION, H-TWO-WITNESSES (145);
  - H-LAWS-ON-NUCLEUS (144);
  - H-LIGHT-INVARIANT (143);
  - H-ELEMENTS-PER-UNIVERSE (138);
  - H-ORIGINAL-IRRELEVANT (136, answer 4);
  - item 136 H.
- **The board's:**
  - H-ALPHA-IS-LIGHT, H-SAME-HAMILTONIAN;
  - H-COPY-TAKES-P2-LAWS (now restricted to values);
  - H-LABEL-ENCODING (the encoding as discrete labels, including molecular quantum numbers);
  - H-MORSE-MODEL.

## OPEN

1. **(b) or (a): is the README the labels or the values?** The board reads your answers as (b). Yours to confirm or
   correct.

## History (verifier, 2026-10-07)

Ten findings, all applied:

1. **The equilibrium geometry is a parameter, not a state,** and its invariance fails beyond the simplest picture. It is
   withdrawn as an exact invariant. Discrete labels replace it.
2. **"Your two answers fit each other"** held only under (b). Now stated as the board's reading, with the condition.
3. **The no-cloning paragraph misread item 146** and misapplied the theorem to a known specification. Moved out of
   "What passes" and corrected.
4. **(b) is the board's H-COPY-TAKES-P2-LAWS** and (a) would withdraw it. Now said; item 138 is cited.
5. **"The copy's own motion" overstated.** Quantum numbers are labels and can be carried. The bound-level window is
   now computed.
6. **The geometry and "which nuclei are stable"** were the board's additions. Now labelled.
7. **(a) is stated once,** in atomic units: the mass ratio, nuclear size and corrections.
8. **The selftest** now checks the closed form by quadrature. The structural check is marked, and the hard-coded
   "r_e changes by 0.0" is removed.
9. **The Morse model's limits** are stated: about 10% low against ab initio H₂, and 17 levels against real H₂'s 15.
10. **The sign of the shift** (the bond shortens) is stated.
