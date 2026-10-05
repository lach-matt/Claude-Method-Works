# Leaving, stasis in the corridor, arriving (O6, BULK-O2; by deduction; not verified; not seated; 2026-10-05)

## What M asked

- **Item 59:** *"4, then 3 please."* The pairing shape (done, seated), then entering and leaving the corridor.
- **Item 61:** *"Fold into O6 (Recommended)"*. H-DETACH and H-CORRIDOR-STASIS are modelled as three states, with what must
  cross at each.
- **Item 64:** *"1, but I want you to consider using deduction and first principle as we continue forward in to the
  unobserved. Such will be the best method to both determine and fill our gaps"* (M-DEDUCE).
- **Item 66:** *"Premises of O6 (Recommended)"*. H-INFO-RELATIVE-SPEED and H-TWO-PERSPECTIVE-TENSION are premises.

All of M's hypotheses are carried as hypotheses, never as results. O9 stays OPEN.

**How this file is built.** Every statement is one of two kinds.
- A **premise**: READ at source, computed by a board owner, or a named hypothesis.
- A **deduction**, labelled DEDUCED, with the premises it uses.

What no deduction closes is OPEN. The geometry is Randall–Sundrum's two planes as `bulk.py` seats them (H-RS1).

Every number is printed by `crossing.py`.
- **Selftest:** 6/6 checks, 3 of them controls, with 4 STRUCTURAL lines printed and not counted.
- **Owners it asks:** `bulk.py`, `searches.py`, `measure.py` and `transit.py`.

## The premises

| | premise | status |
|---|---|---|
| P-CONF | Each plane carries its own fields; the bulk carries only gravity (RS eq. 4, p.2; "two three-branes, one of which contains the Standard Model fields", abstract). | READ. Named **H-CONFINED**, because RS variants exist with matter in the bulk (CMS p.3). |
| P-KK | One term couples the bulk's modes to our matter: the zero mode at gravitational strength, each massive mode at Energy/TeV (RS p.6; DHR eq. 10). | READ |
| P-TENS | V_hid = −V_vis = 24M³k and Λ = −24M³k² (RS eq. 11, p.3), "required in order to obtain a solution that respects four-dimensional Poincare invariance" (p.4). | READ; re-derived here from RS eqs. 7–9 (check 1) |
| P-SCALE | A visible mass is e^(−kr_cπ)m₀ "when measured with the metric ḡ", since "all operators get rescaled according to their four-dimensional conformal weight" (RS pp.5–6). | READ |
| P-VIEW | The TeV scale may equally be regarded as fundamental, "the one naturally taken by a four-dimensional observer residing on the visible brane" (RS p.6). | READ |
| P-MPL | M̄_Pl² = (M³/k)(1 − e^(−2kr_cπ)) (RS eq. 16). | READ; re-derived here (check 2) |
| P-JUMP | The jump reads 3.29×10⁻²⁸ s on our clock and 3.29×10⁻¹³ s on a hidden clock built to the same physics. | COMPUTED (`bulk.py`, seated 8i) |
| P-ML | At most 2E/h orthogonal states per unit time (Margolus & Levitin eq. 2, p.3). Reaching one orthogonal state takes at least h/4E (eq. 4; check 3). "E t … tells us the number of distinct states that a system with energy E can pass through in time t" (p.10). Useful dynamics are counted in the rest frame, where E·t is invariant (p.9). | READ. The bound counts states, not bits, so one orthogonal step per bit is named **H-ONE-STEP-PER-BIT**. |
| P-BITS | The information defining a 70 kg body is 9.5×10²⁷ to 1.1×10²⁹ bits under named counts. Bekenstein's floor and Landauer's cost are the owner's. | COMPUTED (`measure.py`) |
| P-MOVE | Teleporting an unknown quantum state is a move, not a copy; no-cloning is enforced. | COMPUTED (`transit.py`) |

## The three states, deduced

### Leaving

- **D1. What crosses is not the matter.** [P-CONF] A field on a plane has its action only on that plane, so a body made of
  such fields cannot enter the bulk. What crosses is an excitation of a bulk field carrying the body's defining
  information. *This is H-DETACH's physical reading: the information leaves, and the matter stays.*
- **D2. The carrier is gravitational.** [P-CONF, P-KK] In Randall–Sundrum the bulk holds only gravity. The carrier is a
  gravitational mode (a massive graviton, or the radion), loaded through the one coupling term.
- **D3. What happens to the original.** [D1, P-MOVE, P-BITS] The matter at the departure point keeps its pattern unless
  something removes it.
  - If the defining information is classical, it can be copied. The original is then left intact, a duplicate rather
    than a departure, unless it is erased at Landauer's price.
  - If it is quantum, no-cloning forces the original's state to be given up in the transfer, a move.
  - Either way, leaving is a separation of information from matter, and for a quantum pattern a forced one. *Your "let
    go" has this exact counterpart.* Whether the defining information is classical or quantum is OPEN (S1B-O1).

### Stasis in the corridor

- **D4. The information has no matter form in the bulk.** [D1, D2] While it is there, no plane's fields hold it; it exists
  only as a gravitational excitation. *This is H-CORRIDOR-STASIS's physical reading: "cannot take physical form".*
- **D5. Stasis does not hold itself.** [P-KK] The same coupling term that writes the information into a massive mode also
  decays it back into our plane's matter, and both rates scale alike.
  - So, at one plane, a longer stasis costs a slower loading. An indefinite stasis needs a carrier that does not couple
    back, and then it cannot be loaded there either.
  - **Computed lifetimes of the first massive graviton.** At CMS's edge (coupling 0.1, 4.78 TeV, width 1.42 %, READ) it
    lives 9.7×10⁻²⁷ s. At `bulk.py`'s point it lives 8.8×10⁻²⁹ s; that width (97 %) comes from ATLAS's law applied outside
    its range (H-WIDTH-LAW). Both are against a jump of 3.29×10⁻²⁸ s on our clock.
  - **A way out** would be a carrier that couples differently at the two planes. How strongly the hidden plane couples to
    the massive modes is not READ (OPEN).

### Arriving

- **D6. Arriving needs matter already waiting.** [P-CONF at the destination, P-BITS] The information must be written into
  the destination plane's own fields, which the bulk cannot supply. The destination must hold the stock (Step 1b's B
  stock).
  - For 9.5×10²⁷ bits, a 1 m holder needs at least **33 J** of total energy (Bekenstein's floor).
  - Preparing a stock that is not blank costs at least **2.8×10⁷ J** at 310 K (Landauer, H-RESET-STOCK).

## Your two premises

### D7. Speed relative to the information: the count is shared, the rate is not

[P-SCALE, P-JUMP, P-ML]

- **The count is shared.** A count of bits is dimensionless, so it is not rescaled between the planes. Both ends count the
  same information, and the same number of orthogonal steps N = 2Et/h.
- **The duration is not.** The two clocks read the same crossing as **3.29×10⁻²⁸ s** and **3.29×10⁻¹³ s**.
- **So the rate differs.** Information per own second differs by **10¹⁵** between the two ends, at the same moment.
- *This is the computed counterpart of H-INFO-RELATIVE-SPEED.* A rate exists, relative to the information and to the
  position reading it. There is never a single speed.
- **The shared quantity is the action per bit.** Under H-ONE-STEP-PER-BIT, E·t ≥ hI/2 = **3.15×10⁻⁶ J·s** from both ends.
  The energy each end needs depends on the duration it reads:

  | crossing time read | energy needed |
  |---|---|
  | our clock's jump, 3.29×10⁻²⁸ s | at least **9.6×10²¹ J**, about 1,500 times the body's mc² |
  | the hidden clock's jump, in its own units | 9.6×10⁶ J |
  | 1 s | 3.2×10⁻⁶ J |

### D8. The inhomogeneous tension: a candidate

[P-TENS, P-SCALE, P-MPL]

- **Each plane carries a vacuum energy.** In the 5D frame the two are equal and opposite, ±24M³k.
- **Read in each plane's own units** (vacuum energy has conformal weight 4), they are no longer equal and opposite:
  - the hidden plane reads **+5.7×10⁷⁴ GeV⁴**;
  - ours reads **−(4.88 TeV)⁴**.
- **The pair is inhomogeneous:** opposite in sign and **10⁶⁰** apart in magnitude. P-TENS says that pair is what holds the
  two planes in a static, flat relation.
- **"At the same time" is well defined here,** because static Randall–Sundrum has a global time.
- *This is a CANDIDATE for H-TWO-PERSPECTIVE-TENSION.* An inhomogeneous pair exists and holds the planes in place; that it
  is your tension is not shown.

## For M

- **Leaving.** Your detachment follows from first principles once matter is confined to its plane. What crosses can only
  be the information. For a quantum pattern, no-cloning forces the original to let go of it; that is a move, not a copy.
- **Stasis.** Your "cannot take physical form" also follows: in the corridor the information is a gravitational
  excitation, not matter. But this carrier does not hold still. It decays back within about 10⁻²⁸ to 10⁻²⁶ s, because the
  same coupling that loads it unloads it. A lasting stasis needs a carrier coupled unequally to the two planes, and that is
  where your inhomogeneity would have to live.
- **Arriving.** The destination must already hold matter to write into. The corridor carries the pattern, not the
  substance.
- **Speed.** You were right that it isn't the conventional speed. What both ends agree on is how much information
  crossed. How fast it crossed depends on which end reads it, and the two readings differ by 10¹⁵ at the same moment.
- **Tension.** Randall–Sundrum's two planes carry exactly such an inhomogeneous pair: opposite in sign and 10⁶⁰ apart as
  each plane reads its own. It is what holds them in place. Whether it is your tension is the next thing to test.

## Named hypotheses

- **H-CONFINED:** matter is confined to its plane.
- **H-ONE-STEP-PER-BIT:** one orthogonal step per bit written.
- **H-RESET-STOCK:** a non-blank stock must be reset.
- **H-WIDTH-LAW:** ATLAS's width law used outside its range.
- **Carried from `bulk.py`:** H-RS1, H-K-PLANCK, H-SAME-LAGRANGIAN and H-STATIC-SLICING.
- **Carried from `measure.py`:** its counting hypotheses.
- **M's:** H-DETACH, H-CORRIDOR-STASIS, H-INFO-RELATIVE-SPEED, H-TWO-PERSPECTIVE-TENSION, H-NO-SPEED, H-HIGHER-CORRIDOR and
  H-UNOBSERVED-UNBUILT.

## OPEN

1. Whether the defining information is classical or quantum (S1B-O1). This decides whether leaving is a copy or a move.
2. How strongly the hidden plane couples to the massive modes. This decides whether an asymmetric carrier can hold
   stasis.
3. Whether the two planes' inhomogeneous tensions are M's tension (H-TWO-PERSPECTIVE-TENSION), and what observable would
   tell.
4. The same deductions in a geometry whose bulk carries matter fields, where D1–D4 change.
