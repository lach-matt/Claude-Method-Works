# Your answers to walls A and B, followed through (M-RULINGS item 143; READ, deduced and computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft said a different nucleus cannot be seen in a
spectrum, and that chemistry is then the same in every universe. Both were wrong (History).

## What you said

- **Item 143:** *"A - the only thing that can cross is that which can cross the horizon of a black hole. B - light
  likely doesn't vary"*.
- **Carried:** H-HORIZON-CARRIER and H-LIGHT-INVARIANT.
- **The board's reading of B (H-ALPHA-IS-LIGHT):** the Löwdin walk's one entered constant, c = 137.035999, is the same
  in every universe. That constant is 1/α in atomic units.
  - The seated member `method/members/THE-LOWDIN-SOLUTION-2.md` l.35: *"with c = 137.035999 the only entered
    constant"*.
  - If you meant the speed of light alone, α could still differ through the electron's charge or Planck's constant.
- **The instrument:** `samelight.py`. Selftest 5/5, in 50-digit arithmetic.
  - **Genuine checks:** two.
  - **Marked STRUCTURAL:** three.

## What follows

### 1. A different nucleus *can* be seen in a spectrum, so your search has a target (L3)

- **Ordinary electronic lines do not see the nucleus's mass, to first order. Some lines do.**
- **Hydrogen's 21 cm hyperfine line scales with the electron-to-proton mass ratio.** Change the proton's mass by a part
  in 10⁴ and:
  - every electronic line ratio stays exactly where it was;
  - the 21 cm line against Lyman-α moves by 1.0 part in 10⁴.
  - The formula is standard, not READ here.
- **Isotope shifts and molecular lines do the same.** That is how astronomers measure the proton-to-electron mass ratio
  in distant gas, against its redshift.
- **So an element whose electronic lines match ours, but whose nucleus differs, would show it** in those lines. That
  is a concrete target for your item 142, for elements that exist in both universes.

### 2. With α the same, the electrons' structure is the same (L1)

- **The board checked what α does on the one atom solvable exactly,** hydrogen-like with Dirac's levels.
  - Change α by a part in 10⁴, and the 2p fine-structure interval against Lyman-α moves by **2.000** parts in 10⁴.
  - Hα against Lyman-α moves by −2.4×10⁻⁹.
  - **The shift differs from line to line, so a different α would be visible against a redshift.**
  - With α held, every ratio is identical (STRUCTURAL).
- **The Löwdin walk under the board's readings** (H-ALPHA-IS-LIGHT and H-SAME-HAMILTONIAN) returns the same table in
  every universe:
  - the same 107 entrants;
  - the same three exceptions;
  - the same twelve unwitnessed rows.
- **So item 138's "measure exactly as are ours do" holds for the electrons' structure**, under those readings and your
  "likely".
- **The walk's nucleus is a point charge of infinite mass** (*"their attraction −Z/r to the nucleus"*, l.72). So the
  table is silent on any nuclear difference.
- **The table changes only for large changes of α.** At c → ∞ eleven elements move. For small differences, section 1's
  line ratios carry the weight, not the table.

### 3. What stays hidden: uniform scalings (L2, STRUCTURAL)

- **A redshift scales every line by the same factor.** So does the electron's mass with α held, and so does the
  nucleus's mass to first order.
- **Those cannot be told from each other.** Section 1's lines are what break the tie.

### 4. What could differ between universes, under your B

- **Not the electrons' structure.**
- **But these could:**
  - the electron's mass, which sets the scale of every line;
  - the nucleus's mass;
  - its size;
  - which nuclei are stable.
- **Each changes material properties.** Heavy water, whose nucleus differs, melts at 3.8 °C. And if a universe's stable
  nuclei differ, its set of elements differs.
- **So your "laws … that govern those elements' material properties" (item 138) have room to act,** in the nucleus and
  the electron's mass, even with light the same.

### 5. What crosses (L4)

- **Every causal signal crosses a horizon inward: matter, light and gravitational waves alike.**
  - **So your A restricts the direction of crossing, not the kind.**
  - That matches your corridor, whose horizon is crossed one way, 1 → 2 (plane.py P1, seated).
- **It also goes past the brane models that set up wall A.** In those, matter and light stay on their plane and only
  gravity crosses. Your A admits light.
- **On item 90 ("not by light", for the README):** the board reads 90 as what the README uses, and 143 as what can cross,
  so it reads both as standing. Whether they meet is yours to say.

## For your search (item 142)

- **Our own background radiation cannot carry the signature you want, for a physical reason.**
  - It left the gas at z ≈ 1089, when only hydrogen, helium and trace lithium existed.
  - Nuclei at Z ≥ 119 have never been made, and their heavier neighbours live for milliseconds at best.
  - That answers item 142 without any reading of A.
- **Where a crossing would show is the board's deduction, not your A.**
  - If every crossing between universes is a corridor, another universe's element reaches ours by crossing a horizon
    into it, with ours at the corridor's position 2.
  - That is the reverse of the board's usual frame, where ours is position 1.
  - **Other imprints of other universes have been sought in the background radiation, but they are not element
    crossings:** bubble collisions (Feeney, Johnson, Mortlock and Peiris, PRL 107, 071301, 2011; not READ here).
- **For a known element with a different nucleus:** section 1's lines are the target.
- **For an element we lack (Z ≥ 119):** the index writes 119 and 120 as hydrogen-like (cmbindex.py), so it cannot
  template them.
  - The walk computes their configurations, 8s¹ and 8s².
  - But a frozen field's orbital energies are not transition energies, so even its code (*"PENDING BANK"*) would be a
    start, not a template.

## Named hypotheses

- **Yours:**
  - H-HORIZON-CARRIER, H-LIGHT-INVARIANT (143);
  - M-CMB-ELEMENT-SEARCH (142);
  - H-ELEMENTS-PER-UNIVERSE (138);
  - H-UNIDENTIFIED-CARRIER (90).
- **The board's:**
  - H-ALPHA-IS-LIGHT (reading B as α held);
  - H-SAME-HAMILTONIAN (the walk's equation is the same in every universe);
  - H-CROSSING-IS-CORRIDOR (every crossing between universes is a corridor; used only in the deduction above).

## OPEN

1. Whether item 138's "relative laws" act on the nucleus and the electron's mass.
2. A template for Z = 119–120's lines.
3. What a crossing into our universe at a position 2 would show.

## History (verifier, 2026-10-07)

Ten findings, all applied:

1. **"1.97 parts in 10⁴" was float cancellation.** The value is 2.000, now in 50-digit arithmetic. Hα's shift is
   −2.4×10⁻⁹.
2. **"A different nuclear mass scales every line by the same factor … no spectrum can tell" was false beyond first
   order.** The 21 cm line, isotope shifts and molecular lines see the nucleus. This is now section 1, and the lead.
3. **"Every universe's atoms give the same spectrum" and "chemistry is the same" contradicted section 2.** Narrowed to
   the electrons' structure.
4. **L3 rested on two board readings and a walk blind to the nucleus.** Both are now stated, and "likely" is kept.
5. **"Not where your A says to look"** put a location into your answer. It is now the board's deduction, with
   H-CROSSING-IS-CORRIDOR named and the reversed frame flagged.
6. **The physical reason the background radiation cannot carry the signature** is now stated.
7. **The electron's mass** is added to what could differ.
8. **A restricts direction, not kind.** The tension with the brane models, and the reading of item 90, are now drawn
   out.
9. **"Can find only Z ≥ 119"** held only for electronic lines. "Its channel energies would give a real template" was
   over-reach.
10. **The Löwdin quotes** now cite the seated member, not the recovered draft.
