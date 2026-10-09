# Item 178: positive and negative null energy, and the definable null (the board's answer; computed, READ and deduced; verified once, findings applied; not seated; 2026-10-09)

*First headed* "Item 178 … (the board's answer; verified once, findings applied; not seated)". The computations are
scratch runs, reproduced by both verifiers. They are not yet an owned instrument; they go into `sim2_passage.py`
X10 (e) in the E-PASS fix round.

## What you said

- **Item 178** (verbatim in the rulings file): *"If the is a positive null energy, why not a negative null energy?
  We have positive and negative tension, charge, etc... I would imagine the very same principles apply to null
  energy. Remember that a null is according to my original work in the book the method, a null is a computational
  nothing, but a true nothing by definition implies a lack of existence, so that 'nothing' is something definable."*

## Plain words first

1. **Negative null energy exists** in established physics. It always comes with positive energy, but the pairing is
   lopsided, not a mirror.
2. **Your tension analogy holds across a sheet, not along it.**
   - A light ray crossing a thin sheet sees null energy with the sign of the sheet's energy density. For a pure
     tension, that is the tension's sign.
   - Along the sheet, a pure tension of either sign has exactly zero null energy.
   - Null energy is not a conserved, charge-like quantity.
3. **"Null" means two different things here.** In physics, "null energy" is energy along a light ray. In your book, a
   null is a definable nothing. The corpus uses both senses and never joins them.
4. **For E-PASS (X10 (e)):**
   - At exact coincidence, position 2's piece has zero null energy along the plane.
   - Across the plane, only the pair's sum is physical, and it is exactly zero.
   - Your 177's "appearance" is the plane's four-dimensional reading, the board's standing axiom Z3. So it does not
     reach the README's negative density inside one universe, and nothing needs to be put to you.

## The answer, labelled

**1. Negative null energy exists (READ).**
- **Examples, each READ on the page that names it:**
  - Casimir plates: Kontou–Sanders 2003.01815 p.34.
  - Squeezed light: Ford–Roman gr-qc/9901074 p.2.
  - The Hawking flux: through Fewster–Roman p.13; Hawking 1975 is NOT READ.
- **One caveat (Ford–Roman p.2):** Casimir energy densities "have not been directly measured". The corpus's
  Transitions.md:486-488 ("Casimir energy is measured") goes beyond that source.

**2. Across a sheet, null energy carries the energy density's sign (computed, exact).**
- **The formula.** A thin sheet with surface stress diag(−ρ, p, p, p), crossed by a 5D null ray with k_∥ along the
  sheet and k_y across it, has null energy T(k,k) = [(ρ+p)k_∥² + ρk_y²]δ(y). So:
  - along the sheet, only ρ+p enters;
  - across it, ρ enters.
- **Consequence.** At a thin sheet, the 5D NEC is the sheet's WEC.
- **Negative tension in brane models (READ, Barcelo–Visser hep-th/0004022).**
  - Negative tension, with the null vector "even slightly orthogonal to the brane", gives T k k < 0 (p.2).
  - In brane models, "there is no longer any particular barrier to negative brane tension — in fact negative brane
    tensions are ubiquitous" (p.4), and "in the brane picture there is nothing wrong with the notion of a negative
    brane tension" (p.16).
- **Along a sheet (computed, exact).** A stress has zero null energy for every null direction along the sheet exactly
  when it is a pure tension, S ∝ δ, of either sign.
  - The control fails as it must: three directions leave seven parameters free; twelve leave none.

**3. Null energy is not charge-like (READ, computed).**
- **Not conserved, and it depends on direction.** Between Casimir plates it is −4C cos²θ/L⁴ (computed): negative
  along the normal, zero along the plates.
- **The established pairing is lopsided.**
  - **Quantum interest (Ford–Roman):** the positive part must repay the negative "with an 'interest'". This is proven
    for delta-function pulse pairs of massless scalar fields in flat 2D and 4D spacetime.
  - **Gao–Jafferis–Wall (1608.05687, pp.2, 4; now READ, NOT READ in item 176):** with the two boundaries decoupled,
    the null energy cancels exactly between U > 0 and U < 0, a mirror at linear order. Coupling them breaks the
    cancellation, and the coupling's sign chooses the sign.
- **"Opposites attract":**
  - **The sign of energy.** For the sign of energy itself, a positive/negative mass pair runs away together (Bondi
    1957, standard-not-READ).
  - **Maldacena–Milekhin (2008.06618, READ).** Oppositely charged black holes thread closed magnetic field lines
    through the wormhole, and the Casimir energy on those lines is negative (p.4). Their attraction is a problem the
    construction must counter: "Naively, they would attract and coalesce" (p.3); they are made to orbit (p.6).

**4. The two senses of "null" (READ).**
- **In physics,** "null" means lightlike: a non-zero vector of zero length (Carroll gr-qc/9712019 pp.15-16). The sign
  belongs to the energy, not to the null.
- **In your book,** a null is the empty index: "every closure test in this book passes on nothing at all"
  (The_Method_1_6-2.md:2995-2996, §12.11.0.11). The book also keeps a null protocol:
  - "every null is a mathematical gap" (Register 1663);
  - "a finding, not a value" (Register 1681);
  - a null response proving non-existence (Register 1704).
- **The corpus uses both senses,** sometimes in the same table (Transitions, "null case" beside "local null surface"),
  and never links them. Its one deliberate bridge, Register 1472 (the null bound on smeared null energy, computed at
  your instruction), is about method.
- **Attribution.** "Computational nothing" is your phrase in 178; it has no hits in the corpus. "Nothing is something
  definable" heads a note from the collaborator in your book (The_Method_1_6-2.md:17); the book's author is you (line
  7), and the note credits that reframing to "a second party" (lines 51-58).
- **The board's reading, not an identity.** The objects with exactly zero null energy along a sheet are the pure
  tensions and vacua of either sign (computed: T_kk = 0). They carry energy, so they are not a nothing in your book's
  sense, and the board draws no identity between them. Telling a zero of absence (the empty index) from a zero of
  cancellation (a pair summing to zero) is the board's reading too (H-TWO-ZEROS); the corpus contains both kinds and
  does not set them against each other.
- **Pairs in the corpus (READ facts; their bearing on null energy is the board's deduction).** The book finds pairs at
  its core:
  - closure by two-fold projections;
  - seven binary bounds;
  - (source, target) cells.
  It also names one thing pairs cannot carry, the ternary bracket (The_Method_1_6-2.md:5692-5696). The board reads
  this as a limit on pairwise structure, not as a law against it.

**5. What 178 does to E-PASS, X10 (e).**
- **Along the plane (computed, exact).**
  - **The pure tensions.** At coincidence, position 2's whole piece (S = +σ_RS δ) and the README's share on
    H-SPLIT-AT-OUR-TENSION (S_m = +2σ_RS δ) are pure negative tensions, so their null energy along the plane is exactly
    0. This holds under any linear junction map.
  - **The approach.** On the NEC profiles the zero is approached from above: radial +5.4×10⁻⁸ and angular
    +9.4×10⁻⁷ σ_RS at λ = 0.4, x = 10⁻¹⁴, ℓ = 32m (numerical).
  - **So** "obeys the NEC only marginally" means exactly zero along the plane, not negative.
- **Across the plane (deduced).** At exact coincidence the slab pinches (X9). No 5D null ray crosses position 2's
  sheet without crossing ours; B5a says the same of coincident sheets: the junction "sees only the sheets' summed
  surface stress".
  - The physical 5D null energy there is the sum, which is exactly 0, so Z3 is met marginally.
  - The per-sheet values (−σ_RS k_y² for position 2's piece, +σ_RS k_y² for ours) are bookkeeping.
  - Their sign follows the owner's orientation (the normal into the bulk; T5c). With the normal flipped it reverses
    (computed).
- **Decided under 149 (the board's, not yours).**
  - Item 177's appearance is the plane's four-dimensional reading, the projected bulk Weyl term (X10 (a)-(b)). This
    rests on two sources:
    - the board's axiom Z3 (axioms.py): "null energy is never violated, in five dimensions … The plane's
      four-dimensional reading of a violation is the bulk's pull (Z1) — the appearance items 117 and 120 describe";
    - Maldacena–Milekhin p.11 (READ): "what looks like a quantum Casimir energy in four dimensions is actually a
      classical effect in five dimensions … So in five dimensions the topological censorship should work".
  - So X10 (e)'s "as worded it does not reach this negative density" **stands** for the README's share inside one
    universe.
  - Its "put to M" is withdrawn: the rulings (117/120, through Z3) decide it.
- **H-POSITIVE-ON-P2 stands** (the board's reading of your 139 (2)).
  - Inside one universe the pieces stop at d₊ (0.8395m at ℓ = 32m; only for ℓ > 27.07m).
  - There, in the x → 0 limit and on the NEC-obeying profiles, position 2 carries no negative null energy: along the
    sheet radial 0, angular +4.91σ_RS; across +σ_RS k_y², since ρ = +σ_RS.
  - At finite x a level sheet below y* carries a small negative radial null energy (−3.97×10⁻⁴ σ_RS at x = 10⁻⁴), and
    the owner's NEC excludes that sheet.
- **Not to be confused (computed).** X10 (b)'s negative integrated null energy on our plane (−1.652872 = −Q for both
  legs × 8π) is eq. (17)'s induced Weyl fluid, the projected bulk term. It is not our plane's surface stress, whose
  null energy along the plane is exactly 0 at every r.

**6. OPEN.**
- **Between universes (phase 3).** Whether a per-sheet negative across-plane value can be read as an appearance at
  all, given Z3/Z1's definition, is open. Your 139 (2) still requires positivity in position 2's own frame there
  (item 176), so no appearance is established.
- **Item 179.** It changes where the corridor sits. These readings are of the board's SIM2 setup and are re-read with
  179's results.

## History

- **2026-10-09, workflow `item178-reading`.** Five readers ran (the corpus on nulls, the corpus on pairs, the work's
  structure, the physics, and the coincident-pair computation), followed by a synthesis and two verifiers (refute,
  overclaim). Both verifiers reproduced every number.
- **Both found the synthesis's central decision wrong (blocker).** It had read 177's appearance as 5D null energy
  across position 2's sheet (H-177-MEANS-5D) and withdrawn X10 (e)'s "does not reach". Z3 and Maldacena–Milekhin p.11
  point the other way: 5D null energy is never violated, and the appearance is the 4D reading. H-177-MEANS-5D is
  withdrawn. X10 (e)'s "does not reach" stands; its question to M is decided by the rulings.
- **Also corrected:**
  - A phrase quoted as M's that M never wrote ("+/- … summing to nothing") is removed.
  - "Your conclusion holds" / "your analogy is exact" was invented agreement; the answer now gives the split.
  - Register 1491 was misused as evidence that the corpus keeps the two nulls apart; it is dropped.
  - "Physics' own nothing" / "physical twin" is struck: vacua and tensions carry energy, and the analogy is the
    board's reading.
  - Maldacena–Milekhin's mechanism is restated: the attraction is an obstacle, not the driver; "the one place" is
    dropped.
  - Barcelo–Visser's "energetically disfavoured" is limited to point-particle field theories, with their brane-model
    statement added.
  - Quantum interest is given its proven scope.
  - The "between universes" exemption from 139 (2) is removed (176 still requires positivity in position 2's frame).
  - The x → 0 and NEC-profile qualifiers are restored.
  - Each example is re-cited to its page.
  - The across-plane sign is tied to the orientation, not to selftest C17.
