# Your corridor in Bronnikov–Kim's family (M-RULINGS items 101–111; deduced, computed and READ; verified three times; SEATED (ledger.py section 8o); 2026-10-06)

*Seated in ledger.py section 8o on M's order of work (item 113); until then headed "… not seated …".*

*First headed* "(M-RULINGS items 101 and 102; … not verified …)", then "(… items 101, 102 and 104 …; verified once …)",
then "(… 101, 102, 104 and 106; first form verified once, the item-104 rework not yet …)".

## What M said (verbatim in the rulings file)

- **101.11:** *"total our plane can read"*.
- **104(b)**, choosing the pull: *"observers at position 1 can only see the mouth at position 1. The corridor interior and
  position 2 are not observable until the horizon of the corridor is crossed, at which point position is no longer
  observable... Horizons have 2 sides"*.
- **106:**
  - *"Horizon; reciprocal"*.
  - *"Three distinct holds in one fluid wave motion, horizon position 1 only as the corridor opens, when the corridor is
    fully realized the bits are held on both horizons simultaneously because the corridor builds position 2 with the
    bits in mind, upon the corridor closing the bits are then held only at the horizon of position 2."*
  - *"Yes, it ends at P2"*.
- **107:** *"The information in transit is still the definition of the geometric object, just absent the actual physical
  mass, which makes it appear to be negative mass"*.
- **108:** *"Yes, that's it"*; *"Whatever is needed"*.
- **109:** *"The horizon of position ends as well. A horizon cannot exist without the object of which it needs to
  exist"*.
- **110:** *"Into position 2"*.
- **111:** *"that and only that which is provided by the closing of the horizon."*; *"one energy read from two sides
  because both positions are currently entangled as a singular state"*.

Every number is printed by `plane.py`.
- **Selftest:** 13/13 checks, 2 genuine controls and 1 contrast, with 9 STRUCTURAL lines printed and not counted.
  *First written* "11/11", then "12/12", then "15/15"; restatements had been counted, and the thermofield check
  held by construction (History).
- **Imported, not rebuilt:**
  - `chain.py`: the floor and constants;
  - `bulk/escape.py`: R = 0;
  - `pair.py`: the Hawking temperature;
  - `higgs.py`: the Higgs mass;
  - `geometry.py`: the thermofield double;
  - `stockdest.py`: the 70 kg payload.

**The geometry, READ.** Bronnikov & Kim, gr-qc/0212112v1, eq. (17), p.4.
- *"a symmetric wormhole geometry for any r0 > 2m ≥ 0, or for any r0 > 0 in case m < 0"*.
- For η = r₀ − 3m/2 > 0, framed near Schwarzschild after Casadio and others, *"a nonsingular black hole with a wormhole
  throat at r = r0 inside the horizon, in other words, a non-traversable wormhole"*.
- Eq. (18) gives the density.
- The full window r₀/2 < m < 2r₀/3 is the board's extension, computed.
- *First written* "citing Casadio … for 3m/2 < r₀ < 2m", which attributed the window to them; and "p.6" (rulings item
  105).

## What follows the work

- **1. Your corridor is in the family, and its horizon is crossed one way, from position 1 to position 2.**
  - The members with a horizon outside the throat and no singularity are exactly **r₀/2 < m < 2r₀/3**. This is checked
    numerically, with a control (no horizon) and a contrast (a singularity outside the throat).
  - Rewrite eq. (17) in Bronnikov–Kim's coordinate x, with r = r₀ + x² (computed). The clock-rate factor
    g_tt = (x² + r₀ − 2m)/(r₀ + x²) vanishes at x = ±√(2m − r₀): **a horizon on each side**.
  - Between the two horizons, the dx² coefficient changes sign: −10.8 at x = 0, for m = 1, r₀ = 1.8. **x is a time
    direction there.**
    - The throat is a moment, not a place.
    - Every forward-in-time path that enters position 1's horizon crosses the throat and leaves through position 2's
      horizon, which is a white-hole horizon on that side.
    - Control: an ordinary throat (r₀ > 2m) keeps x as a space direction, coefficient +8.0.
  - **That is your description, computed.** Position 2 is unseen until position 1's horizon is crossed, and then
    position 1 is unseen (H-CORRIDOR-HORIZON, H-ONE-MOUTH-SEEN, H-TWO-SIDED-HORIZON).
  - Bronnikov–Kim's "non-traversable" means not two-way. One-way passage is what the geometry gives.
  - **A published analogue** (Simpson & Visser, 1812.07114v3, READ by a verifier):
    - p.3: for a < 2m, *"a one-way spacelike throat … a bounce into a future incarnation of the universe"*.
    - pp.4–5: *"a bounce into a separate copy of our own universe"*. That sits beside your H-SEPARATE-UNIVERSES.
  - Whether every path through the geometry is complete is not computed: OPEN.
  - *First written* (as the boundary): "Crossing to position 2's exterior: the horizon members are non-traversable".
    That was wrong.
- **2. The pull, and the floor.**
  - The pull our plane reads is m. That is the Komar mass at infinity, read from the static region outside r = 2m, which
    reaches flat space.
  - It equals the horizon's area-mass, √(A/16π) = m (sympy).
  - The horizon's own Komar charge is smaller: κA/4π = 2m√(1 − r₀/2m), which is 0.63 m at r₀ = 1.8 m. The rest of the
    pull comes from the tidal stress outside the horizon.
  - Under H-HORIZON-HOLDS and H-STRONG-BOUND, the least horizon that holds N bits has radius r_min(N). So the least pull
    is **√(N h c⁵ ln2/(8π² G)) = 4.59404002×10⁸ J × √N**, or 2.405878326×10¹⁶ J for the core.
  - This is the floor's number, unchanged. chain.py's floor was a throat's area-mass, reread here as a horizon's; both
    are r/2.
  - At that m the throat lies behind the horizon, at r₀ between 0.75 and 1 times r_min. The plane's total (ADM) reads
    between 1 and 5/4 of the floor.
  - *First written:* "The pull is the horizon's own mass" (it is the area-mass), and "the floor was always a horizon"
    (it was a throat, reread).
- **3. Superseded.** "If the throat holds it instead, the pull lies between the floor and 4/3 of it." Item 106 puts the
  bits on horizons, and in a horizon member the throat is a moment (point 1). Kept as history.
- **4. The Penrose inequality coincides, in this family, with the regularity condition.**
  - The total exceeds the horizon's area-mass exactly when r₀ > 3m/2. That is the same as positive density, and the
    same as no singularity.
  - The premises:
    - the constant-time slice of the static exterior is time-symmetric;
    - its curvature is 16πρ, with ρ from eq. (18);
    - r = 2m is its outermost minimal surface.
  - Source: Bray, math/9911173v1, eq. 6 p.4 and Thm 1 p.8, READ by a verifier.
  - *First written:* "is the family's regularity condition", with its premises unnamed.
- **5. Item 102: your answer, "Horizon; reciprocal".**
  - The board's reading (R-RECIPROCAL-AS-PRODUCT, ungraded): at the floor,
    **E × r = N h c ln2/(4π²) = 3.48772679×10⁻²⁷ J·m × N**. This holds by construction: Bekenstein's bound saturated.
  - Along horizons, mass grows with size. The two relations meet only at the floor.
  - The negative-mass member (m = −2r₀, total zero, density negative everywhere, no horizon) is the boundary.
  - *First written:* "The reciprocal holds exactly … the mass is the inverse of the size". That was the board's gloss,
    stated as yours (rulings item 112).
- **6. The three holds and one energy (items 106, 109–111).**

  | hold | where the bits are | what the planes read |
  |---|---|---|
  | opening | position 1's horizon | plane 1's reading rises to the floor (H-QUASISTATIC; opening.py O4) |
  | fully realized | both horizons: one entangled state | **one energy, read from two sides** |
  | closing | position 2's horizon, which ends with the corridor (109) | the energy goes into position 2 (110) and the build uses exactly it (111) |

  - **The trip carries one E_min(N)**, with N including the trajectory bits (TRAJECTORIES.md point 6). For the core
    README that is 2.406×10¹⁶ J.
    - That the energy comes from the device is the board's step.
    - That it is one energy and not two is your accounting (H-ONE-ENERGY-TWO-SIDES), carried as given, not computed.
  - **What the thermofield double shows: the two readings agree, perfectly correlated.**
    - The thermofield double is the entangled state of two copies of a system that Van Raamsdonk's eq. (1), p.2, uses
      (READ in geometry.py; asymptotically AdS: H-TFD-MODEL). It is imported as `geometry.tfd`.
    - In it, the two sides' energies always agree: each side's varies (1.40), but their difference has zero variance.
    - **That holds by construction, and it does not need entanglement.** A mixture with no entanglement, with the same
      matched levels, also gives zero.
    - **It does not give one energy in the budget sense.** In this state the two sides' energies add to twice one
      side's.
    - So "one energy" stays your hypothesis.
    - An unentangled state with the same one-sided statistics gives independent readings (variance 2.81).
    - Both lines are STRUCTURAL.
    - *First written:* "In it, the difference … has zero variance" (counted as a check), and "the state ER=EPR pairs
      with a two-sided black hole".
  - The opening and closing holds have no static member. They need dynamics, and a Komar "pull" needs a static
    geometry to be defined (H-QUASISTATIC): OPEN.
- **7. The README against the object it defines (items 107, 108).**
  - **Apparent mass = carried − defined.** The core README carries 0.2676901 kg against the 70 kg it defines, so it
    appears as **−69.7323 kg**: negative, as you said. Position 2's stock fills the deficit.
  - It appears negative while N < **N\* = 8π² G M²/(h c ln2) = 3.827306673×10¹⁶ bits/kg² × M²**, which is
    **1.875380270×10²⁰ bits** for 70 kg. Both carry a relative uncertainty of 2.2×10⁻⁵, from G; the floor's
    coefficient 4.59404002×10⁸ J carries 1.1×10⁻⁵.
    - Checked: the bisected floor at N\* equals Mc² = 6.291286×10¹⁸ J.
  - The largest snapshot (1.088×10²⁹ bits) would carry 1.6858×10⁶ kg, more than it defines.
  - **With item 111, the README and the build are one number.** A README of N bits delivers E_min(N) to the build, the
    direction you gave. Equivalently, N = 8π² G E²/(h c⁵ ln2).
    - Sizing a README by an energy the build needs would be the board's reading, not yours.
    - How E_min for the core (2.4×10¹⁶ J) compares with any energy needed to assemble 70 kg from stock is not computed
      anywhere on the board: OPEN.
  - *First written:* "A build needing energy E needs a README of N = …".

## What is ruled out, as the boundary

- **A closing hold that persists** (H-HOLD-PERSISTS, withdrawn by your item 109 and kept as the boundary). It would be
  a hole of 0.2677 kg for the core.
  - Its temperature would be at most 4.583×10²³ K. That is the Schwarzschild value; for a Bronnikov–Kim member it is
    smaller by 2√(1 − r₀/2m), computed from eq. (17)'s surface gravity. Simpson–Visser p.11 eq. 6.5 is the analogue.
  - It would be gone in **at most about 7.8×10⁻²¹ s** (H-SM-ONLY: any further species would shorten it), radiating all
    Standard Model species (Carr–Kohri–Sendouda–Yokoyama,
    2002.12778v2, p.10 eq. 14, READ by a verifier).
  - The photon-only 1.6×10⁻¹⁸ s overestimates that by about 200.
  - *First written* as "What the closing hold implies", the main line, with the lifetime NOT READ.
- **Two-way traversal** (Bronnikov–Kim p.4).
- **A positive-density member with a total below its horizon's area-mass** (Bray).
- **A horizon member with m ≥ 2r₀/3** (the contrast).
- **Per-universe bookkeeping, if each universe is flat far away with its own conserved mass** (H-ASYMPTOTIC-FLAT-ENDS).
  - Plane 2's rise from 0 to the floor would then need an energy flux that only the tidal stress could carry, by
    violating the energy conditions. Bronnikov–Kim p.1: *"E_μν does not necessarily satisfy the energy conditions"*.
  - Source for the conserved mass: Mädler–Winicour 1609.01731v3 p.16 eq. 61, READ by a verifier.
  - Your H-ONE-ENERGY-TWO-SIDES (one entangled state) is a different accounting. Which applies is OPEN.
- **The throat's size.** Bronnikov and Kim warn *"a restriction can quite probably appear from 5-dimensional
  geometry"* (p.2). r_min for the core is 4.0×10⁻²⁸ m. BULK5-O1, OPEN.

## The walls, now

| wall | under your answers |
|---|---|
| 1 formation | the corridor is a member of a known family (H-BK-CORRIDOR). Opening and closing are modelled in opening.py; the joins are OPEN (opening.py O3) |
| 4 the corridor's energy | **one E_min(N) = 4.59404002×10⁸ J × √N per trip**, N including the trajectory bits (H-PULL-IS-COST, H-ONE-ENERGY-TWO-SIDES, H-DEVICE-SIZES, H-HORIZON-HOLDS, H-STRONG-BOUND; items 106, 110, 111). The cost of the opening and closing dynamics is OPEN |
| 6 energy at position 2 | **the closing energy, delivered into position 2 and used exactly by the build** (items 110, 111: yours, carried) |
| 7 composition | position 2's stock fills the README's deficit (item 108) |
| 8 the global bulk | the one-universe clause is dropped; the 5D completion is OPEN |
| 9 the coupling | the passage is one-way 1 → 2 (computed). How the device opens it is OPEN |
| 13 the split | answered by your rule, H-SPLIT-AT-P2: the record ends at position 2. *The board's reading:* it is read during the closing hold while the horizon shrinks, its capacity (1 − φ)² N (opening.py O7). Nothing else is computed |

*First written* with wall 4 "zero by your measure" (the ADM reading), then "at least the floor, or 1 to 4/3 of it"; and
wall 13 "closed by your rule".

## Named hypotheses

- **Yours:** H-PULL-IS-COST, H-ONE-MOUTH-SEEN, H-CORRIDOR-HORIZON, H-TWO-SIDED-HORIZON (104); H-RECIPROCAL,
  H-THREE-HOLDS, H-SPLIT-AT-P2 (106); H-DEFINITION-MINUS-MASS (107, 108); H-README-AS-NEEDED (108);
  H-HORIZON-NEEDS-OBJECT (109); H-ENERGY-INTO-P2 (110); H-BUILD-IS-CLOSING-ENERGY, H-ONE-ENERGY-TWO-SIDES (111);
  H-SEPARATE-UNIVERSES and the rest of item 101; H-READING-ONLY (86.1).
- **The board's:**
  - H-BK-CORRIDOR: a static 4D brane metric. Your "transit phase through a dimension" is a bulk throat, which this is
    not.
  - H-HORIZON-HOLDS, H-STRONG-BOUND; R-RECIPROCAL-AS-PRODUCT; H-QUASISTATIC; H-TFD-MODEL.
  - H-ASYMPTOTIC-FLAT-ENDS, H-SCHWARZSCHILD-REMNANT, H-SM-ONLY (the boundary).
  - H-RS1.

## Sources READ

| source | route | used |
|---|---|---|
| Bronnikov & Kim, gr-qc/0212112v1 | Firecrawl; alphaXiv (verifiers) | eq. 13 p.3; eq. 17, its range, the horizon case and eq. 18, p.4; p.1 energy conditions; p.2 the 5D restriction; p.6 |
| Simpson & Visser, 1812.07114v3 | alphaXiv (a verifier) | p.3 one-way spacelike throat; pp.4–5 separate copy; p.11 eq. 6.5 |
| Carr, Kohri, Sendouda, Yokoyama, 2002.12778v2 | a verifier | p.9 eqs. 11–12; p.10 f = 15.35, eq. 14 |
| Mädler & Winicour, 1609.01731v3 | a verifier | p.16 eq. 61 |
| Bray, math/9911173v1 | a verifier | eqs. 5–6 p.4; Thm 1 p.8; Def. 21 p.54 |
| NOT READ | — | Bondi 1957; Schoen–Yau; Witten; Huisken–Ilmanen; Casadio–Fabbri–Mazzacurati; the area theorem; the Page curve |

## OPEN

1. The opening and closing holds' dynamics: how the corridor opens and closes (walls 1 and 9).
2. The accounting across your two universes. On your path the one-entangled-state accounting is carried (items 111,
   115). Per-universe conserved masses are the boundary.
7. What becomes of the closing hold's bits when position 2's horizon ends (item 109).
8. How the floor's energy compares with any energy needed to assemble 70 kg from position 2's stock.
3. Whether every path through the corridor is complete.
4. The 5D completion, and its restriction on the throat's size.
5. If the bits are quantum (H-ENTANGLEMENT-IS-IT), whether holding them on both horizons at once is a copy. It is one
   entangled state on your reading (item 111), and no-cloning bears on it.
6. The bits a destination's trajectories carry (R-CHAIN-RULE).

## History (verifiers, 2026-10-06)

- **First pass:**
  - Bronnikov–Kim pages;
  - "positive energy at its neck";
  - an exact-inverse claim that restated the zero total;
  - the ADM reading unnamed;
  - the z3 checks were one line of algebra each;
  - restatements counted;
  - a mislabelled control;
  - the 5D caveat;
  - H-QUASISTATIC;
  - the trajectories' share;
  - traversability;
  - the Higgs wording.
- **Second pass:**
  - two tautological checks;
  - "the horizon's own mass";
  - the throat's range and the ADM range omitted;
  - "the floor was always a horizon";
  - the Penrose premises;
  - **the one-way passage, which had been listed as ruled out**;
  - the window's attribution;
  - the Schwarzschild temperature assumed;
  - the lifetime, now READ;
  - P3 superseded;
  - the reciprocal gloss;
  - item 106 not quoted in full;
  - wall 13 overstated;
  - the bookkeeping omitted;
  - one digit.
- **Third pass (items 107–115):**
  - The thermofield check held by construction, and showed correlation rather than one energy. It is now STRUCTURAL.
  - Its source is Van Raamsdonk eq. 1, asymptotically AdS.
  - The build's direction runs from N to E.
  - Uncertainties added.
  - The opening row now rises to the floor.
  - The device as the source is the board's step; N includes the trajectory bits.
  - The premises for wall 4 are named.
  - Wall 13's reading is the board's.
  - The accounting on your path is yours.
  - The Bronnikov–Kim temperature factor is computed.
  - The lifetime is at most 7.8×10⁻²¹ s.
