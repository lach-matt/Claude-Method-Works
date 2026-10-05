# The unobserved universe, two kinds of observer, conscious selection, many perspectives (rebuilt after one verification; not seated; 2026-10-05)

## M's words and how they are carried

M's words, verbatim from the rulings file:

- **Item 48:** *"what if this is the ground state without first principles/without observation? The decoupling only
  exists upon observation of a universe? And this would be why it is a constant"*.
- **Item 49:** *"matter itself is capable of observation, however, it is not conscious conversation, which requires
  sentience . A different type of observation..."*.
- **Item 50:** *"Matter based observation is natural and always occurring, with all probabilities available, until
  conscious observation occurs. Consciousness observation forces a specific and measurable behavior from the object
  being observed"*.
- **Item 51:** *"consider multiple sentient/conscious observers. Each observation is a different and relative
  perspective of the same object, thus each observation is inhomogeneous when compared to the others"*.

These are carried as M's hypotheses, never as results: H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS and
H-MANY-PERSPECTIVES.

M's order was to read the literature first, then build a model, then price what would distinguish the hypotheses.

Every number below is printed by `unobserved.py`. Its selftest runs 15/15 checks, 3 of them controls, with 2 STRUCTURAL
lines printed and not counted. It asks `medium.py`, `cmbframe.py` and `nosig.py` for its inputs.

A first build was verified, and its main comparison turned out to be an artefact; that is withdrawn (see the History
section). This version is the rebuild.

## What the literature says (READ 2026-10-05; routes in the instrument)

### Relational time

- **A static global state.** In Page–Wootters, Ĵ|Ψ⟩ = 0, and the physical states are "static" objects. Conditional
  states obey Schrödinger's equation relative to a clock (Giovannetti, Lloyd & Maccone, 1504.04215v3 p.2).
- **The unobserved view.** The external view is the static global state itself, and the external observer is "a
  hypothetical entity" (GLM p.7).
- **Wheeler, quoted there:** "the past has no existence except as it is recorded in the present".
- **Zurek and Landsman, quoted by Schlosshauer (p.8):**
  - Zurek: "Our experience of the classical reality does not apply to the universe as a whole, seen from the outside,
    but to the systems within it".
  - Landsman: "A world without parts … is a world without facts".
- **Status.** This is a standard proposal with live objections: Kuchař and Unruh–Wald, as GLM p.7 restates them. It has
  "never been developed beyond the toy-model stage" (Marletto & Vedral p.3).
- **Hartle–Hawking.** They call their state the "'ground state' or state of minimum excitation" (APS abstract). Its de
  Sitter limit is scoped to a minisuperspace model.

### The classical CMB

- **Standard account.** Squeezing and decoherence make the perturbations classical, with no observer invoked.
- **The critical school.** Perez, Sahlmann & Sudarsky argue against observation as the trigger, and propose objective
  collapse instead.
- **Scope of both.** Both concern *inflationary perturbations*, not photon–baryon decoupling. The CSL tests against the
  CMB are scoped the same way: one CSL version is ruled out, others remain compatible.

### Two kinds of observation

- **Matter's.** Records made by matter are standard physics: Zurek's einselection and redundancy.
- **Records don't pick an outcome.** "Does decoherence solve the measurement problem? Clearly not" (Joos).
- **Eraser experiments.**
  - A which-path record held *only in matter* removes the fringes.
  - Erasing it restores them only in conditioned subsets.
  - The authors give awareness no role: "regardless of whether or not an observer accesses this information" (Ma et al.
    p.2).
- **Consciousness-collapse models.**
  - Chalmers–McQueen and Okon–Sebastián both reproduce the Born rule.
  - Chalmers–McQueen (p.43) float a biased variant: collapses "might be biased", "current evidence leaves room open for
    it", and "We do not find this picture especially attractive".
- **Conscious-observer studies.**
  - They measure interference visibility, never outcome bias.
  - Every pre-registered or confirmatory arm read is null, and an open-data re-analysis finds the claimed shifts not
    significant after correction.
  - Radin's group disputes this. It is recorded, not adjudicated.

### Many observers

- **Relational and QBist accounts.** In relational QM and QBism, different observers give "two distinct correct
  descriptions".
- **No-go theorems.** Brukner, Frauchiger–Renner and Local Friendliness show that absolute observed events conflict with
  other basic assumptions. The experiments so far used photons as the "friends".
- **Routes back to agreement:** cross-perspective links (Adlam–Rovelli), redundant records (Zurek), and communication
  (QBism).
- **The CMB.** Each observer sees a different CMB sky, and a Lorentz boost recovers one from another (Planck 2013
  XXVII).

## The model, computed (an illustration of mechanisms, not evidence about the universe)

### The set-up

- **The clock.** A clock register labels the cooling.
- **The medium.** A photon–matter pair exchanges an excitation while ionised, and the coupling steps off at
  T_dec = 2,973 K.
- **Decoupling.** The pair is *detuned*, so decoupling changes the medium's eigenbasis
  (‖[H_hot, H_cold]‖ = 0.21). The freeze after decoupling is built into the toy by construction.
- **The whole.** The whole system is given a history-state (Feynman–Kitaev) Hamiltonian.

### 1. A universe constant as a whole

- The numerical ground state *is* the history state: overlap 1 to 12 places, energy 10⁻¹⁶.
- Its gap equals the construction's exact value, 1 − cos(π/2N).
- Conditioning that ground state on each clock reading gives ordinary evolution exactly, with uniform clock weights.
- **What "ground" means here.** It is a property of the construction. The construction gives M's "ground state" a
  literal realisation, mapped as H-CONSTANT-IS-STATIONARY.

### 2. "Unobserved", read three ways, none preferred

- **STATIC.** The global state itself, which is constant. This is M's "constant without observation", per GLM p.7.
- **TRACED.** The medium with the clock traced out: a mixture of the whole history, weighted by a clock weighting that
  GLM call "completely arbitrary".
- **M-SUPPORT.** M's stronger version as a computable rule: only the coupled epochs, with observation extending the
  support through records.

TRACED and M-SUPPORT differ by trace distance **0.24 / 0.33 / 0.42** for uniform-tick / conformal / cosmic-time
weighting. That is, the coupled epochs make up 50 %, 33 % and 20 % of the history under the three weightings. The control: with no
decoupling in range the two readings coincide exactly, so the difference measures decoupling.

### 3. Matter observation by records of tunable quality

- The records' states overlap as exp(−γ|Δk|), the form Marletto–Vedral give for a cosmological clock.
- The medium conditioned on a record's outcome has purity **0.60** with no record and **0.78 / 0.94 / 1.00** as the
  records sharpen (γ = 0.05, 0.2, ≥ 5).
- This sweep stands in for Marletto–Vedral's candidate observable, which "might have observable consequences even at the
  present epoch".

### 4. Conscious selection (H-CONSCIOUS-SELECTS)

- **Matter observation keeps every outcome available.** After matter observation, every outcome remains present, which
  is M's first clause.
- **Reading (a).** A conscious selection with Born weights reproduces the decohered weights exactly. It is empirically
  identical to the standard account.
- **Reading (b).** Biased selection; see section 6.

### 5. Many perspectives (H-MANY-PERSPECTIVES)

- **Disagreement depends on the angle between perspectives.** Two conscious observers disagree with probability
  **sin²(θ/2)**, where θ is the angle between their pointer observables. This holds whatever the state:
  - 0 when they look the same way;
  - 0.067 at 30°;
  - 0.25 at 60°;
  - 0.5 at 90°.
- **Agreement returns** with probability 1 when one reads the other's record (a cross-perspective link), or when both
  read redundant copies of one record.
- **At the corridor's ends.** Earth and Proxima see CMB skies that differ by a **0.294 mK** dipole: they move at
  32.4 km/s relative to each other, against Earth's own dipole of 3.362 mK. Each sky recovers the CMB frame exactly.
- **So "inhomogeneous" is literally true** of different perspectives of the same object, and it is recoverable under
  stated conditions.

### 6. O9 (`nosig.py` asked)

- **Under reading (a)**, Alice's conscious selection leaves Bob's statistics unchanged for every setting: the spread is
  10⁻¹⁶. There is no channel.
- **Under reading (b)**, moving Alice's outcome probability from ½ to (1 ± ε)/2 shifts Bob's marginal by (ε/2)·E(a,b).
  That makes a channel of 1 − H((1 − ε)/2) bits per pair:

| bias ε | bits per entangled pair | pairs needed for the species count (9.5×10²⁷ bits) |
|---|---|---|
| 10⁻⁵ | 7.2×10⁻¹¹ | 1.3×10³⁸ |
| 10⁻³ | 7.2×10⁻⁷ | 1.3×10³⁴ |
| 10⁻² | 7.2×10⁻⁵ | 1.3×10³² |
| 10⁻¹ | 7.2×10⁻³ | 1.3×10³⁰ |

Reading (b) is the board's beyond-linear branch, H-SETTLE. No outcome bias has been measured. The contested 10⁻⁵-level
claims concern interference visibility, so carrying their size over to ε is a named hypothesis, H-EFFECT-TRANSFER.

## For M

- **What the physics read supports.** It supports a universe that is constant as a whole, with change, decoupling and
  facts existing only relative to observers and their records.
- **The candidate rule for the stronger version.** It is computable: the coupled epochs alone, with records extending the
  support.
- **Matter's observation keeps every probability.** That is standard physics.
- **Sentient selection as a different type** has two serious models. Both obey the Born rule, and none has been tested.
- **Perspectives differ** by an exact, computable amount, and agree again when records are shared.
- **What decides the corridor** is whether conscious selection is Born-like or biased:
  - Born-like gives no channel.
  - Biased gives a channel at the rates above, which is the only route here that touches O9.

**O9 stays OPEN.**

## Named hypotheses

H-CLOCK-IS-COOLING, H-TOY-MEDIUM, H-TOY-SAHA, H-HISTORY-STATE, H-CONSTANT-IS-STATIONARY, H-UNOBSERVED-IS-STATIC,
H-UNOBSERVED-IS-TRACED, H-M-SUPPORT, H-CLOCK-WEIGHT, H-RECORD-QUALITY, H-BORN-SELECTION, H-BIASED-SELECTION,
H-POINTER-ANGLE and H-EFFECT-TRANSFER, with M's H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS and
H-MANY-PERSPECTIVES.

## OPEN

1. How observation extends the clock's support (M-SUPPORT's dynamics).
2. Any measurement of the cosmological clock's record quality (Marletto–Vedral).
3. Any experiment separating sentient from physical observation: Q-shape interferometry, Wigner's-friend tests with AI
   friends, or Yu–Nikolić's untested prediction 3.
4. Any measured outcome bias from conscious observation.
5. Page & Wootters 1983 and the full Hartle & Hawking 1983 text: NAMED-NOT-READ.

## History (verifier, 2026-10-05; first-written claims kept)

- **Withdrawn.**
  - The first build's trace distance of **0.549** and its conclusion "'unobserved' is not 'coupled'" were an artefact.
    The toy's Hamiltonians commuted, and the distance stayed between 0.5 and 0.707 whatever happened: 0.501 with no
    decoupling, 0 for a medium started in its coupled eigenstate.
  - "Half in coupled epochs" was a choice.
- **Shown tautologically, now rebuilt.**
  - The conditional-state check was true by construction.
  - The record check was true by construction.
- **Scope.** Perez–Sahlmann–Sudarsky were applied to decoupling, which is out of their scope.
- **Wording.** "Established physics" now reads "a standard proposal".
- **Undersold, now carried.** GLM's static external view; Wheeler; Zurek and Landsman; and Marletto–Vedral's observable.
