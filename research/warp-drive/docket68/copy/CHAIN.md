# The whole chain under M's theory (M-RULINGS item 96; deduced, computed and READ; verified once; not seated; 2026-10-06)

*First headed* "(M-RULINGS item 96; deduced, computed and READ; not verified; not seated; 2026-10-06)".

## What M asked

- **Item 96:** *"Instead of trying to prove my theory of warp travel wrong. We need to focus on proving it right. Assume
  that my theory is the only one in which warp travel is actually realizable. The whole chain of warp travel should be
  entirely derivable from first principles and provable with math. Rerun the whole chain and reassess the
  walls/obstructions/gaps. Those will be our focus."*
- Carried as H-M-THEORY: your items 86–98 are the working premises, and the board's other routes are the boundary.
- Also carried: H-CMB-FRAME (item 96), H-COSMIC-BEAT (item 97), and M-COEFF (item 98: every coefficient evaluated).

**How it was done.**
- Four readers re-ran every station over the board's owners. `chain.py` assembles them and machine-checks the chain's
  logic with z3.
- **Selftest:** 17/17 checks, 5 genuine controls and 2 contrasts, with 6 STRUCTURAL lines printed and not counted.
  *First written* "13/13 checks, 2 genuine controls and 2 contrasts"; the verifier found clauses stronger than their
  sources (History).
- **Every coefficient** is printed as an exact closed form in the constants, then as its value. h, c and k_B enter
  exactly; G and H0 carry their named uncertainties.
- **The rule:** a link is **proved** only from named premises. A **wall** blocks a link even under your premises. A
  **route** is a named premise under which the wall does not bind.

## The chain under your theory

ADDRESS → READ → README → MAKE (one corridor containing position 2: two places made one) → KEY (joined at the same
instant of the CMB clock) → HOLD → CROSS (the README is present at position 2) → BUILD (position 2 builds from its own
stock) → COPY → REPEAT.

## What follows the work

- **1. Two ways through the formation walls, and both are yours.** This is machine-checked over the board's reading of
  each theorem.

  | how the corridor comes to be | consistent? | causal safety proved? | singularity? |
  |---|---|---|---|
  | **found and widened** (your answer 3) | **yes** | **yes** | no |
  | **made, with its making begun at or below light speed before the joining** (H-PRIOR-SETUP), degenerate joining | **yes** | **yes** | no |
  | made, with a light-time setup, non-compact joining | yes | yes | yes (Tipler), not disqualified by the board's ruling M-S1A-P3 |
  | made at the joining instant from nothing (smooth, compact, CMB clock) | no | — | — |
  | made at the instant, degenerate or non-compact | no (finite propagation) | — | — |
  | made in an information layer (charter's reading, no source) | no | — | — |

  - **Your "made" is not ruled out.** The finite-propagation wall bars only a corridor made at the joining instant from
    nothing.
  - A made corridor whose making begins beforehand, within light speed, with a degenerate joining, is consistent and
    loop-free. That is D23's first trip, and in its corrected form it needs only a common causal past.
  - Found-and-widened needs no setup at all.
  - Controls:
    - with no theorems, the made corridor is consistent, so the inconsistency comes from the theorems;
    - a pinched throat is inconsistent;
    - removing the keyed-corridor proof removes safety;
    - removing the prior setup removes the made route.
  - *First written:* "Your own answer 3 is the route the theorems leave open … the only one that clears both walls".
    That rested on a well-posedness clause stronger than its sources, and a partly invented quantum clause.
- **2. Computed here, and carried from the readers.**
  - **Computed:**
    - keyed corridors close no loop;
    - frame.py's z3 lemma shows the geometry picks the cosmic beat;
    - widening is not a change of topology;
    - nothing is shipped (k\* = 0);
    - stock passes on quantity at a primitive body.
  - **Carried from the readers, not recomputed here:**
    - D13 satisfied with a zero bound once two places are one;
    - D1–D4 and D8–D12 exclude a throat by their own scope;
    - zero-curvature throats need no plane matter — locally, under H-RS1 (section 8m), with the global case open (W8).
- **3. One corridor's energy has a lower bound that grows as the square root of the README.**
  - At a throat of radius r, the Misner–Sharp energy is r c⁴/(2G) = **6.05127782×10⁴³ J/m × r** (sympy). The matter
    outside the neck can add up to the opposite sign (H-NECK-ENERGY).
  - Bekenstein's bound (eq. 1, READ in measure.py) gives E·r ≥ N h c ln2/(4π²) = **3.48772679×10⁻²⁷ J·m × N**.
  - Both are met at the least radius:
    - **E_min = √(N h c⁵ ln2/(8π²G)) = 4.59404002×10⁸ J × √N**;
    - **r_min = √(N h G ln2/(2π²c³)) = 7.59185111×10⁻³⁶ m × √N**.
    - Both carry a relative uncertainty of 1.1×10⁻⁵, from G.
  - **At that floor the neck sits at its own Schwarzschild radius, and its area is exactly 4 ln2 Planck areas per bit**
    (nopath.holographic_bits, computed). The floor is the holographic bound, the strong-gravity form of Bekenstein
    (H-STRONG-BOUND, Bousso's extrapolation).

  | README | least neck | least energy | trips whose energy lies above the floor |
  |---|---|---|---|
  | identity core (2.74257×10¹⁵ bits) | 3.97581866×10⁻²⁸ m | **2.40587833×10¹⁶ J** | 0.1 c (3.169×10¹⁶ J), 0.2 c, 0.8 c; not 0.01 c (3.146×10¹⁴ J) |
  | largest snapshot (1.088×10²⁹ bits) | 2.504×10⁻²¹ m | 1.515×10²³ J | none |

  - **One corridor's least energy grows as the square root of the file.** This is a floor, not the cost, and it rests
    on H-NECK-HOLDS, H-NECK-ENERGY and H-STRONG-BOUND.
  - If the cost were the total our plane reads, the floor would vanish. Which energy you mean is OPEN.
  - *First written:* "one corridor costs in proportion to the square root of the file", a floor stated as a cost, and
    "0.235 × E_Planck × √N", corrected on your item 98.
- **4. The cosmic beat (item 97).**
  - The CMB temperature falls with the expansion: dT/T = −H0·dt, with H0 = 2.182989×10⁻¹⁸ s⁻¹ (Planck 2018, relative
    uncertainty 8.0×10⁻³).
  - The measured T₀ = 2.72548 ± 0.00057 K (Fixsen 2009) fixes cosmic time locally to **9.58×10¹³ s (3.0 Myr)**.
  - So the beat cannot be read to useful precision today. For a found throat it need not be read: the throat keys the
    joining (H-FOUND-KEYED).

## The walls, ranked: the focus

| # | wall | what would remove it |
|---|---|---|
| 1 | **Formation**: a smooth compact making is topology change, and Geroch–Borde then force a closed loop, which the CMB clock excludes (D24) | found and widened; or made with a light-time setup and a degenerate (READ Horowitz 1991) or non-compact joining |
| 2 | **Reaching position 2**: finite propagation (the board's reading, ungraded) bars a corridor made at the joining instant with no prior connection | a throat that already reaches position 2; or a making begun beforehand (H-PRIOR-SETUP) |
| 3 | **Throat existence** (found route): throats keyed at the cosmic beat, common enough that one joins the two places | READ the searches and the throat literature; compute the abundance needed (a foam origin would be quantum and need its own safety proof) |
| 4 | **The corridor's energy**: point 3's floor at position 1 | the plane-total reading (OPEN: which energy you mean) |
| 5 | **The builder at position 2**: no READ or computed mechanism makes a position execute a specification (STOCKDEST OPEN 6, COPY-O2) | READ constructor theory (Deutsch–Marletto) as the frame for your H-POSITION-BUILDS; or the README carries the recipe |
| 6 | **Energy at position 2**: the build's energy is computed nowhere; the README's information buys at most 2.96667818×10⁻²¹ J × N at 310 K (8.14×10⁻⁶ J for the core) | the stock's own free energy, or energy through the corridor |
| 7 | **The destination's composition**: Proxima b and d unmeasured (COPY-O4); what a site adds to the README (COPY-O5) | a transit, a spectrum, direct imaging |
| 8 | **The global bulk** for the zero-curvature throats, with both mouths in one universe (BULK5-O1) | construct it, or READ Vollick and Bronnikov–Kim's references |
| 9 | **The coupling**: what at position 1 widens or makes the corridor (O6) | a Lagrangian for the device's input |
| 10 | **Address precision**: the radial error at Proxima is 2.6101×10¹² m, 359 times Proxima b's orbit (under the found route this sits below wall 3) | micro-arcsecond astrometry; the address carries its frame |
| 11 | **The read**: non-destructive at synapse resolution (COPY-O3) | a non-destructive read, or H-RETIRE-A (left open) |
| 12 | **Identity completeness** (COPY-O1) | a whole-brain synapse total; a tolerance |
| 13 | **The split**: on which side the README's record ends (H-SPLIT-RULE) | a rule, derived or yours |

*First written* with eleven walls. The corridor's own energy (4) and the destination's composition (7) were missing, and
wall 6 carried "3.6×10¹⁰ J of chemistry", a figure with no owner.

## Named hypotheses

- **Yours (items 86–98):** H-M-THEORY, H-ADDRESS-INPUT, H-TRIANGULATED-ACTION, H-README, H-COST-IN-README,
  H-STOCK-IS-STOCK, H-POSITION-BUILDS, H-CORRIDOR-CONTAINS-P2, H-IDENTIFY, H-MADE, H-COMMON-THROATS, H-CMB-FRAME,
  H-COSMIC-BEAT, H-BRIEF-HOLD, H-READING-ONLY, H-SEEN-BY-INTERACTION, H-CORRIDOR-SINGLE-USE, H-DEVICE-REUSABLE,
  H-CORRIDOR-REPEATABLE, H-SINGLE-CHANNEL-GROWS, H-README-IN-HOLD, H-NO-MOVEMENT, H-INSTANTANEOUS,
  H-UNIDENTIFIED-CARRIER, H-RETIRE-A (open); M-COEFF.
- **The board's:**
  - H-ENCODING, with the z3 clauses printed beside their sources and grades;
  - H-WELL-POSED: finite propagation, ungraded, NOT READ;
  - H-PRIOR-SETUP, H-NO-PINCH, H-FOUND-KEYED, H-CORRIDOR-MODEL, H-FRW-EXACT, H-NOT-DE-SITTER;
  - H-NECK-HOLDS, H-NECK-ENERGY, H-STRONG-BOUND;
  - H-SPLIT-RULE, H-RS1, H-REGENERABLE, H-WIRING-SUFFICES, H-IDENTITY-IN-DYNAMICS.

## Sources

- **Nothing new READ in this file.** Every theorem comes through an owner with its grade:
  - Geroch–Borde and topology change: GRADES.tsv (NARROWED, READ-VIA-RESTATEMENT).
  - Tipler: GRADES.tsv, NOT READ at source.
  - Bekenstein eq. 1: measure.py (READ).
  - The holographic bound and Bousso's extrapolation: nopath.py's DOCKET 67 correction.
  - Liberati–Sonego–Visser: causal.py (READ).
  - Planck 2018, Fixsen 2009 and Gaia DR3: cmbframe.py.
  - Faria 2022: seat.py.
- **The readers' unseated computations** are not used here. These include the throat whose total our plane reads as
  zero, or negative, at m = −2r₀, the address ellipsoid, and the wider K2.

## OPEN

1. Each wall above.
2. Which energy a corridor costs.
3. Whether a corridor's making may begin before its joining instant (H-PRIOR-SETUP).
4. Whether the cosmic beat keys found throats too (H-FOUND-KEYED).

## History (verifier, 2026-10-06)

- **Finite propagation** was encoded as a bar on any made corridor and sourced to BULK5-O6 and D23. It is now the
  board's ungraded reading, barring a corridor made at the instant with no prior connection. The light-time-setup routes
  were added.
- **The quantum clause** asserted more than its source. It is now the charter's reading, and that route is relabelled.
- **Geroch–Borde** merged two clauses. The pinch, Tipler, and "a closed loop is unsafe" are now encoded.
- **Bekenstein at the Schwarzschild scale** is now named (H-STRONG-BOUND) and checked as the holographic bound.
- **A floor** had been called a cost. Carried results had been listed as computed. An unowned figure has been removed.
  Two definitional checks are now STRUCTURAL.
