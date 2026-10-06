# The whole chain under M's theory (M-RULINGS item 96; deduced, computed and READ; not verified; not seated; 2026-10-06)

## What M asked

- **Item 96:** *"Instead of trying to prove my theory of warp travel wrong. We need to focus on proving it right. Assume
  that my theory is the only one in which warp travel is actually realizable. The whole chain of warp travel should be
  entirely derivable from first principles and provable with math. Rerun the whole chain and reassess the
  walls/obstructions/gaps. Those will be our focus."*
- Carried as H-M-THEORY: your items 86–97 are the working premises, and the board's other routes are the boundary
  (item 82).
- *"My CMB preferred frame is cosmic background radiation"* is carried as H-CMB-FRAME. Item 97, the cosmic beat, is
  H-COSMIC-BEAT.

**How it was done.**
- Four readers re-ran every station over the board's owners: the read, README and build; making the corridor; holding
  it and its energy; and the address, key, crossing and repetition.
- `chain.py` assembles them. Every number is computed now from the owners, and the chain's logic is machine-checked
  with z3.
- **Selftest:** 15/15 checks, 2 genuine controls and 2 contrasts, with 4 STRUCTURAL lines printed and not counted.
  *First written* "13/13"; the two added checks confirm that the evaluated coefficients reproduce the computed floor.
- **Every coefficient is evaluated (your item 98, M-COEFF):** printed as an exact closed form in the constants, then as
  its value. h, c and k_B enter exactly; G and H0 carry their named uncertainties.
- **The rule:** a link is **proved** only from named premises. A **wall** blocks a link even under your premises. A
  **route** is a named premise under which the wall does not bind. A **gap** is what nothing on the board reaches.

## The chain under your theory

ADDRESS (position 2 is the device's input) → READ (the object at position 1) → README (the classical specification) →
MAKE (one corridor containing position 2: two places made one) → KEY (joined at the same instant of the CMB clock) →
HOLD (brief, appearing to contain negative energy without containing it) → CROSS (the README is present at position 2)
→ BUILD (position 2 builds from its own stock) → COPY (the faithful copy) → REPEAT.

## What follows the work

- **1. Your own answer 3 is the route the theorems leave open.** This is machine-checked over the board's reading of
  each theorem (z3).

  | how the corridor comes to be | consistent with the theorems? | causal safety proved? |
  |---|---|---|
  | **made**, as stated (smooth metric, compact, CMB clock, well-posed physics) | no: blocked by Geroch–Borde and by well-posedness | — |
  | **found and widened** (your answer 3: *"if found and widened … common and regular occurrences"*) | **yes** | **yes** |
  | made, with a degenerate metric | no: clears Geroch, but not well-posedness | — |
  | made, non-compact | no: the same | — |
  | made by quantum topology change | yes | no: the safety proof is lost |

  - Widening a throat is not a change of topology, so Geroch–Borde say nothing about it.
  - A throat that already exists already reaches position 2. The act at position 1 widens it, so nothing has to reach
    position 2 faster than light.
  - The CMB clock stays a true global clock, so every repetition stays loop-free.
  - **Of the five routes tested, found-and-widened is the only one that clears both walls and keeps causal safety.**
  - Controls: with the theorems removed, the "made" set becomes consistent, so the inconsistency comes from the
    theorems. Dropping well-posedness alone lets the degenerate-metric route through, so that is the clause it cannot
    clear.
- **2. Proved under your premises.**
  - **Causal safety, however often corridors are made:** keyed corridors close no loop, and frame.py's z3 lemma shows
    the geometry picks the cosmic beat.
  - **The crossing:** D13 is satisfied with a bound of zero once two places are one, so the carrier question dissolves
    for the crossing.
  - **The contraction rows go silent:** D1–D4 and D8–D12 exclude a throat by their own scope.
  - **The negative energy is an appearance:** throats with zero curvature scalar need no matter on our plane (section
    8m). That is your H-READING-ONLY in the board's own terms.
  - **Widening is not topology change.**
  - **Nothing is shipped**, so k\* = 0.
  - **Stock passes on quantity.**
  - **The README is classical**, and its size sets the corridor's size (Bekenstein).
- **3. The corridor's energy has a first-principles floor, and it grows as the square root of the README.**
  - A throat's neck of radius r carries energy E_neck = r c⁴/(2G) = **6.05127782×10⁴³ J/m × r** (Misner–Sharp mass
    r/2, derived with sympy).
  - Bekenstein's bound (eq. 1, READ in measure.py) says a region of radius r holding N bits needs
    E·r ≥ N h c ln2/(4π²) = **3.48772679×10⁻²⁷ J·m × N**.
  - Both are met at the least r:
    - **E_min = √(N h c⁵ ln2/(8π²G)) = 4.59404002×10⁸ J × √N**;
    - **r_min = √(N h G ln2/(2π²c³)) = 7.59185111×10⁻³⁶ m × √N**.
  - h and c enter exactly (SI definitions). G is measured (CODATA 2018, relative uncertainty 2.2×10⁻⁵), so both
    coefficients carry 1.1×10⁻⁵. *First written* "E_min = 0.235 × E_Planck × √N", corrected on your item 98.

  | README | least neck | least energy | the trips it beats |
  |---|---|---|---|
  | identity core (2.74257×10¹⁵ bits) | 3.97581866×10⁻²⁸ m | **2.40587833×10¹⁶ J** | 0.1 c (3.169×10¹⁶ J), 0.2 c, 0.8 c; not 0.01 c (3.146×10¹⁴ J) |
  | largest snapshot (1.088×10²⁹ bits) | 2.504×10⁻²¹ m | 1.515×10²³ J | none |

  - Your *"The cost is in how much information is transferred as a README (how big the file is)"* (item 89) gets an
    exact form: **one corridor costs in proportion to the square root of the file.**
  - Your item 94 fits too: one channel that grows with the README. The neck's size grows with the file.
  - **Premises:** the README sits in the neck region (H-NECK-HOLDS), and the corridor's cost is the neck's energy
    (H-NECK-ENERGY).
  - If the cost were instead the total our plane reads, which can be zero for these throats, the floor would vanish.
    Which energy you mean is OPEN.
- **4. The cosmic beat (item 97).** The CMB temperature falls in step with the expansion: dT/T = −H0·dt, with
  H0 = 2.182989×10⁻¹⁸ s⁻¹ (Planck 2018, relative uncertainty 8.0×10⁻³). So reading equal cosmic time to 1 s would take
  a precision of 2.183×10⁻¹⁸. Under found-and-widened the geometry keys the joining, and no reading is
  needed.

## The walls, ranked: the focus

| # | wall | what would remove it |
|---|---|---|
| 1 | **Formation**: making the identification is topology change, which Geroch–Borde forbid with the CMB clock as time (D24) | **found and widened** (your answer 3); otherwise a degenerate metric (READ Horowitz 1991), non-compact (READ Tipler), or a folded brane reconnecting through the bulk (PROPOSED) |
| 2 | **Reaching position 2**: in well-posed physics an act at position 1 cannot make position 2 part of a corridor at the same instant (D23; BULK5-O6) | a throat that already reaches position 2 (found and widened) |
| 3 | **Throat existence**: found-and-widened needs microscopic throats, common enough that one joins the two places | READ the searches (Ellis-throat nulls) and the foam literature (Wheeler; Visser); compute the abundance needed |
| 4 | **The builder at position 2**: nothing says how a position builds from a README; a 10¹⁵-bit README needs a builder that knows the recipe, and a bare position knows only physics | READ constructor theory (Deutsch–Marletto) as the frame for "a position that builds"; or the README carries the recipe (its size rises toward the snapshot's) |
| 5 | **Energy at position 2**: the build's energy is computed nowhere; the README's information buys at most N k_B T ln2 = 2.96667818×10⁻²¹ J × N at 310 K (8.14×10⁻⁶ J for the core) | the stock's own free energy, or energy through the corridor (priced by point 3's floor) |
| 6 | **The global bulk**: the zero-curvature throats work locally; a whole bulk with both mouths in one universe is BULK5-O1 | construct it, or READ Vollick and Bronnikov–Kim's references |
| 7 | **The coupling**: what at position 1 widens the throat and writes the address (O6 moved) | a Lagrangian for the device's input, or the stabilisation scalar (BULK3-O3) |
| 8 | **Address precision**: Gaia DR3's radial error at Proxima is 2.6×10¹² m, 359 times Proxima b's orbit; nothing is sent there, so the address is worked out from light received | micro-arcsecond astrometry or a longer baseline; the address carries its frame (the CMB slice) |
| 9 | **The read**: the only read at synapse resolution destroys the tissue (COPY-O3) | a non-destructive read; or H-RETIRE-A, which you left open |
| 10 | **Identity completeness**: H-WIRING-SUFFICES unproved (COPY-O1); no fidelity criterion | a READ whole-brain synapse total; a tolerance |
| 11 | **The split**: when the corridor closes, on which side the README's record ends | a rule, derived or yours |

## Named hypotheses

- **Yours (items 86–97):** H-M-THEORY, H-ADDRESS-INPUT, H-TRIANGULATED-ACTION, H-README, H-COST-IN-README,
  H-STOCK-IS-STOCK, H-POSITION-BUILDS, H-CORRIDOR-CONTAINS-P2, H-IDENTIFY, H-MADE, H-COMMON-THROATS, H-CMB-FRAME,
  H-COSMIC-BEAT, H-BRIEF-HOLD, H-READING-ONLY, H-SEEN-BY-INTERACTION, H-CORRIDOR-SINGLE-USE, H-DEVICE-REUSABLE,
  H-CORRIDOR-REPEATABLE, H-SINGLE-CHANNEL-GROWS, H-README-IN-HOLD, H-NO-MOVEMENT, H-INSTANTANEOUS,
  H-UNIDENTIFIED-CARRIER, H-RETIRE-A (open).
- **The board's:**
  - H-ENCODING: the z3 clauses are the board's reading of each theorem, printed beside its source and grade;
  - H-NO-PINCH: a widened throat keeps r > 0, so its closing is not a change of topology;
  - H-WELL-POSED, H-CORRIDOR-MODEL, H-FRW-EXACT, H-NOT-DE-SITTER;
  - H-NECK-HOLDS, H-NECK-ENERGY;
  - H-RS1, H-REGENERABLE, H-WIRING-SUFFICES, H-IDENTITY-IN-DYNAMICS.

## Sources

- **Nothing new READ in this file.** Every theorem comes through an owner with its grade: Geroch–Borde, Tipler and
  topology change in docket67-raw/GRADES.tsv (NARROWED, READ-VIA-RESTATEMENT); Bekenstein eq. 1 in measure.py (READ);
  Liberati–Sonego–Visser in causal.py (READ); Planck 2018 and Gaia DR3 in cmbframe.py; Faria 2022 in seat.py.
- The readers' scratch computations (the zero-energy throat at m = −2r₀, the address ellipsoid, the wider K2) are not
  seated here. Where this file uses a figure, it recomputes it from an owner.

## OPEN

1. Each wall above.
2. Which energy the corridor costs: the neck's energy, or the total our plane reads.
3. Geroch, Tipler and Borde READ at source; Horowitz 1991; the throat searches.
