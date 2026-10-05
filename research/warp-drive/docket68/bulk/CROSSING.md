# Leaving, stasis in the corridor, arriving (O6, BULK-O2; by deduction; verified once; not seated; 2026-10-05)

*First headed* "(O6, BULK-O2; by deduction; not verified; not seated; 2026-10-05)".

## What M asked

- **Item 59:** *"4, then 3 please."*
- **Item 61:** *"Fold into O6 (Recommended)"*. H-DETACH and H-CORRIDOR-STASIS are modelled as three states, with what must
  cross at each.
- **Item 64:** *"1, but I want you to consider using deduction and first principle as we continue forward in to the
  unobserved. Such will be the best method to both determine and fill our gaps"* (M-DEDUCE).
- **Item 66:** *"Premises of O6 (Recommended)"*.
- **Item 67:** speed is *"relative not to the information traveling but to the two positions observing from two
  perspectives at the same time"*. This corrects item 65's carrying (H-INFO-RELATIVE-SPEED) to
  **H-POSITION-RELATIVE-SPEED**.

All of M's hypotheses are carried as hypotheses, never as results. O9 stays OPEN.

**How this file is built.** Every statement is a premise (READ at source, computed by a board owner, or a named
hypothesis) or a deduction listing its premises. What no deduction closes is OPEN.

**Scope.** Every deduction rests on Randall–Sundrum's two planes as `bulk.py` seats them (H-RS1), except D3's and D6's
information floors.

Every number is printed by `crossing.py`.
- **Selftest:** 9/9 checks, 4 of them controls, with 5 STRUCTURAL lines printed and not counted.
- **Verification:** verified once, with its findings applied (History).

## The premises

| | premise | status |
|---|---|---|
| P-CONF | Each plane carries its own fields; the bulk, as written, only gravity (RS eq. 4, p.2). The modulus is "not yet solved" (p.4), and stabilisation adds a bulk scalar (DHR p.2). | READ. **H-CONFINED** and **H-UNSTABILISED** are named. |
| P-KK | One term couples the graviton tower to our plane: the massless zero mode at gravitational strength, each massive mode at 1/Λ_π (DHR eq. 10). The radion is not in it. | READ |
| P-KKPROF | How each massive mode is spread across the bulk (DHR eqs. 6–8). | READ |
| P-TENS | V_hid = −V_vis = 24M³k (RS eq. 11), "required in order to obtain a solution that respects four-dimensional Poincare invariance". The separation r_c "is effectively an arbitrary integration constant" (p.4). | READ; matched from eqs. 7–10 (check 1) |
| P-SCALE | Visible masses are e^(−kr_cπ)m₀ "when measured with the metric ḡ" (RS pp.5–6). | READ |
| P-VIEW | The TeV scale is "the one naturally taken by a four-dimensional observer residing on the visible brane" (RS p.6). | READ |
| P-JUMP | The jump reads 3.29×10⁻²⁸ s on our clock and 3.29×10⁻¹³ s on a hidden clock built to the same physics. | COMPUTED (`bulk.py`) |
| P-ML | At most 2E/h orthogonal states per unit time (eq. 2), and at least h/4E to reach one (eq. 4). Rates of separate subsystems add (p.8). The bounds count states, not bits (p.2). | READ. **H-ONE-STEP-PER-BIT** is named. |
| P-BITS | The information defining a 70 kg body, 9.5×10²⁷ to 1.1×10²⁹ bits under named counts; Bekenstein's floor and Landauer's cost. | COMPUTED (`measure.py`) |
| P-MOVE | Teleportation arrives at fidelity 1 on all four outcomes, and B holds a featureless state without the classical bits. No-cloning: A cannot also keep an unknown state. | COMPUTED (`transit.py`). No-cloning is named (**H-UNKNOWN-STATE**). |

## The three states, deduced

### Leaving

- **D1. What crosses is not the matter.** [P-CONF, H-CONFINED] A body made of fields confined to a plane cannot enter
  the bulk. What crosses is a bulk excitation carrying the defining information. *H-DETACH has a physical counterpart
  here, which follows from H-CONFINED: the information leaves, and the matter stays.*
- **D2. The carriers.** [P-CONF as written, H-GRAVITATIONAL-CARRIER] In RS1 as written there are three:
  - the massive gravitons, loaded through the one coupling term;
  - the massless zero mode, through the same term at gravitational strength. It is stable.
  - the radion, which has a separate coupling.

  With Goldberger–Wise stabilisation, a bulk scalar's modes are candidates too (OPEN).
- **D3. What happens to the original.** [D1, P-MOVE] It depends on the kind of information.
  - A classical pattern is copied, not separated, unless the original is erased (at Landauer's price).
  - An unknown quantum pattern is forcibly separated: a move. *Your "let go" has its counterpart in the quantum case.*
  - Which kind the defining information is remains OPEN.

### Stasis in the corridor

- **D4. No ordinary-matter form in the bulk.** [D1, D2] No plane's matter fields hold the information there; it is a
  gravitational excitation. (Our plane would see that as a massive spin-2 particle.) *This is H-CORRIDOR-STASIS's
  "cannot take physical form", read as no ordinary-matter form.*
- **D5. How long stasis lasts.** [P-KK, P-KKPROF, H-STATIC-COUPLING, an open decay channel]
  - **A carrier loaded at A returns to A within its decay time there,** however it couples at B.
  - **Loading and unloading go together.** One coupling term does both, so at A a longer stay means a slower loading.
  - **Measured in jump times,** the stay depends only on the coupling:

    | where | stay ÷ jump time |
    |---|---|
    | where the massive graviton is a resonance at all (coupling ≲ 0.3) | at least 2 |
    | CMS's edge (lasts 9.7×10⁻²⁷ s) | 18 |
    | coupling 0.01 at warp 10¹⁵ (lasts 4.9×10⁻²³ s) | 1,800 |
    | `bulk.py`'s point (outside the width law's validity) | 0.27 |

  - **The massive modes couple 2.5×10⁻³⁰ as strongly at the hidden plane** (deduced from DHR eqs. 6–8), so they return to
    ours.
  - **A lasting stasis needs one of two things:** a carrier that cannot decay, such as the massless zero mode, which loads
    only at gravitational strength; or a coupling switched after loading. That is OPEN, and it is a device question.

### Arriving

- **D6. Arriving.** [P-CONF at B, P-BITS, H-NO-MATERIALISATION]
  - **A bulk mode that decays at B makes particles there.** Building the pattern into a body still needs matter at B
    (Step 1b's B stock), unless the decay can supply at least mc² together with the conserved particle numbers
    (H-NO-MATERIALISATION).
  - **Bekenstein's floor for a 1 m holder is 33 J.** That does not bind: any 70 kg stock carries about 6×10¹⁸ J.
  - **Resetting a stock that is not blank costs at least 2.8×10⁷ J** at 310 K (Landauer).
  - If B is on the hidden plane, both figures are in B's own units, which is ×10¹⁵ in ours.

## Your two premises

### D7. The rate is relative to the two positions

[P-SCALE, P-JUMP, P-ML, dimensional analysis]

- **The count is shared.** Both ends count the same information. A bit count, like E·t/h, is dimensionless and not
  rescaled.
- **No rate is shared.** The two clocks read the same crossing as **3.29×10⁻²⁸ s** and **3.29×10⁻¹³ s**, so no rate is
  common to both ends' clocks.
- **The factor of 10¹⁵ belongs to the positions, not to the information.** It is the ratio between the two clocks, and it
  applies to every process. *This is H-POSITION-RELATIVE-SPEED, as you corrected it: relative to the two positions
  observing at the same time.*
- **What it costs.** Suppose every bit is written within one jump time (H-WRITE-IN-JUMP), one step per bit
  (H-ONE-STEP-PER-BIT).
  - E·t is at least 1.6×10⁻⁶ J·s if the writes run in parallel, and 3.2×10⁻⁶ J·s if sequential.
  - At our jump time that means E ≥ **4.8×10²¹ J**, about 760 times the body's mc².
  - This is one requirement read in each end's units, and E is energy held during the write, not spent.
  - A single collective transition would need only h/4t, so H-ONE-STEP-PER-BIT is what carries this figure.

### D8. The tensions from two positions

[P-TENS, P-SCALE, P-MPL, H-SAME-LAGRANGIAN]

- **Each plane reads its own vacuum energy at the same size,** each in its own units: **±(4.88 TeV)⁴**, equal and opposite.
- **Each reads the other's as 10⁶⁰ off.** Ours reads theirs as +5.7×10⁷⁴ GeV⁴; theirs reads ours as −5.7×10⁻⁴⁶ of its
  own GeV⁴.
- **So the inhomogeneity is between the two perspectives at the same time, not between the planes** (check 4).
- **What the pair does and does not do.** It is required for each plane to be flat and static. It does not fix the
  distance between them, which Randall and Sundrum leave unstabilised.
- *This is a CANDIDATE for H-TWO-PERSPECTIVE-TENSION, not shown to be it.* "At the same time" is well defined here,
  because static Randall–Sundrum has a global time.

## For M

- **Leaving.** Your detachment has a physical counterpart once matter is confined to its plane: only the information can
  cross. For an unknown quantum pattern, no-cloning forces the original to let go of it. A classical pattern would
  instead be copied, unless the original is erased.
- **Stasis.** In the corridor the information is a gravitational excitation, not ordinary matter. The massive carriers
  come back to the plane that loaded them: 2 to 18 jump times where the theory treats them as particles, and longer at
  weaker coupling. One carrier never decays, the massless graviton mode, and it is the natural candidate for a lasting
  stasis. A coupling switched after loading is the other route; that is a device question.
- **Arriving.** The destination must already hold matter to build the pattern into, unless the corridor's energy can be
  materialised there.
- **Speed.** As you said: what both ends share is how much information crossed. How fast it crossed belongs to the two
  positions. Their clocks read the same crossing 10¹⁵ apart, at the same moment.
- **Tension.** Each plane reads its own vacuum energy at the same natural size, equal and opposite. Each reads the
  other's as 10⁶⁰ off. That inhomogeneity exists only between the two perspectives at the same time, which is very close
  to your words. It is a candidate, not yet shown to be your tension.

## Named hypotheses

- **Named here:**
  - H-CONFINED: matter is confined to its plane.
  - H-UNSTABILISED: the modulus is left as Randall and Sundrum leave it.
  - H-STATIC-COUPLING: couplings do not change after loading.
  - H-ONE-STEP-PER-BIT: one orthogonal step per bit written.
  - H-WRITE-IN-JUMP: every bit is written within one jump time.
  - H-UNKNOWN-STATE: no-cloning, for an unknown quantum state.
  - H-NO-MATERIALISATION: the carrier delivers the pattern, not the matter.
  - H-RESET-STOCK: a stock that is not blank must be reset.
- **Carried from searches.py:** H-WIDTH-LAW.
- **Carried from bulk.py:** H-GRAVITATIONAL-CARRIER, H-RS1, H-RS1-WARP, H-K-PLANCK, H-SAME-LAGRANGIAN, H-OBSERVED-FRAME and
  H-STATIC-SLICING.
- **Carried from measure.py:** its counting hypotheses and H-TBODY.
- **M's:** H-DETACH, H-CORRIDOR-STASIS, H-POSITION-RELATIVE-SPEED, H-TWO-PERSPECTIVE-TENSION, H-NO-SPEED,
  H-HIGHER-CORRIDOR and H-UNOBSERVED-UNBUILT.

## OPEN

1. Whether the defining information is classical or quantum (related to S1B-O1). It decides between a copy and a move.
2. A carrier for a lasting stasis. M ruled (item 68) *"the first"*: the massless zero mode, which is loaded at
   gravitational strength. M set aside the switched coupling as *"impossible but to the very definition of the
   transition... There is no in-between..."*. That is M's ruling under H-HIGHER-CORRIDOR, not a refutation computed by
   the board.
3. The bulk scalar that stabilisation adds, as a further carrier.
4. Whether the inhomogeneous pair of tensions is M's tension (H-TWO-PERSPECTIVE-TENSION), and what observable would tell.
5. D1–D8 in a geometry whose bulk carries matter fields.

## History (verifier, 2026-10-05; first-written claims kept)

- **The tensions first compared two unit conventions.** D8 first said the hidden plane *"reads +5.7×10⁷⁴ GeV⁴; ours
  reads −(4.88 TeV)⁴: opposite in sign and 10⁶⁰ apart"*, both "in its own plane's units". The hidden figure was in our
  units. In each plane's own units the two are equal and opposite, and the 10⁶⁰ lies between the perspectives.
- **"P-TENS says that pair is what holds the two planes in a static, flat relation" and "It is what holds them in
  place."** Randall and Sundrum leave the separation unstabilised.
- **"A lasting stasis needs a carrier coupled unequally to the two planes, and that is where your inhomogeneity would
  have to live."** That contradicted D5's own bound. The asymmetry is now deduced (about 10⁻³⁰), and the real escapes are
  named.
- **"It decays back within about 10⁻²⁸ to 10⁻²⁶ s"** compared lifetimes with a jump taken at a different parameter point.
  The stay is now given in jump times, per coupling.
- **"(a massive graviton, or the radion), loaded through the one coupling term."** The radion is not in that term, the
  zero mode is, and stabilisation adds a scalar.
- **"Either way, leaving is a separation of information from matter"**, which pointed at S1B-O1. A classical copy
  separates nothing, and S1B-O1 is a different question.
- **"Which the bulk cannot supply."** Decays do make particles at the destination; H-NO-MATERIALISATION is now named.
- **The energy figure.** It was E·t ≥ hI/2 only, with the energy tabled as "9.6×10²¹ J (ours) against 9.6×10⁶ J
  (hidden)", as if those were different needs. Parallel writing halves the figure, and the two numbers are one
  requirement in two unit systems.
- **H-INFO-RELATIVE-SPEED.** D7 was first carried under this name (*"relative to the information and to the position
  reading it"*). M corrected it (item 67) to H-POSITION-RELATIVE-SPEED.
- **"Your detachment follows from first principles" and "'cannot take physical form' also follows"** overclaimed.
  H-DETACH includes consciousness. These are physical counterparts that follow from H-CONFINED.
- **P-MOVE was printed from a declared flag.** It now shows transit.py's computed fidelity.
- **Check 1's control was near-tautological.** It is now the orbifold doubling dropped.
- **Item 68 (M's ruling).** OPEN 2 first read *"A carrier for a lasting stasis: the zero mode, loaded at gravitational
  strength, or a coupling switched after loading."* M chose the zero mode and set the switched coupling aside.
