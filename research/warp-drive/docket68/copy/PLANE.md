# The cost as the pull, the corridor's two-sided horizon, the inverse of a mass (M-RULINGS items 101, 102 and 104; deduced, computed and READ; first form verified once, the item-104 rework not yet; not seated; 2026-10-06)

*First headed* "(M-RULINGS items 101 and 102; deduced, computed and READ; not verified; not seated; 2026-10-06)".

## What M said

- **Item 101:** your answers 1–11 to the walls, and the plain definition, carried verbatim in the rulings file.
- **Item 102:** *"What if a information definition of a physical/geometric object is negative mass, because it is the
  inverse definition of a positive mass?"*
- **Item 104:**
  - (a) *"I and leaning towards 1, but it could be 2"*: the negative, but possibly the reciprocal.
  - (b) You chose the pull: *"observers at position 1 can only see the mouth at position 1. The corridor interior and
    position 2 are not observable until the horizon of the corridor is crossed, at which point position is no longer
    observable... Horizons have 2 sides"*.
  - (c) The twelve trajectories (below).

Every number is printed by `plane.py`.
- **Selftest:** 11/11 checks, 1 genuine control and 1 contrast, with 5 STRUCTURAL lines printed and not counted.
- *First written* "11/11 checks", of which four restated others and two were one-line algebra (History).
- **Imported, not rebuilt:** `chain.py` (the floor, its constants, the trip energies) and `bulk/escape.py`
  (Bronnikov–Kim's R = 0).

**The geometry, READ.** Bronnikov & Kim, gr-qc/0212112v1, eq. (17), p.4.
- *"a symmetric wormhole geometry for any r0 > 2m ≥ 0, or for any r0 > 0 in case m < 0"*.
- For 3m/2 < r₀ < 2m, citing Casadio and others, it is *"a nonsingular black hole with a wormhole throat at r = r0
  inside the horizon, in other words, a non-traversable wormhole"* (p.4).
- Eq. (18), p.4, gives the density.
- *First written* "p.6", following escape.py. That is corrected in rulings item 105.

## What follows the work

- **1. Your corridor, as you describe it, is in this family.**
  - The members with a horizon outside the throat and no singularity are exactly **r₀/2 < m < 2r₀/3**. The horizon is
    at 2m > r₀; the singular radius 3m/2 lies inside the throat.
  - Checked numerically at m = 0.6 r₀. Control: m = 0.4 r₀ has no horizon. Contrast: m = 0.7 r₀ brings the
    singularity outside the throat.
  - The geometry is symmetric, so there is **a horizon on each side**. An observer at position 1 sees only the mouth on
    that side, and the interior lies behind the horizon.
  - Bronnikov and Kim call it non-traversable. Crossing in leaves position 1 unobservable from inside.
  - That is your H-ONE-MOUTH-SEEN, H-CORRIDOR-HORIZON and H-TWO-SIDED-HORIZON: *"Horizons have 2 sides"*.
- **2. The pull is the horizon's own mass, and its floor is the √N floor.**
  - The pull our plane reads (Komar, from the clock rate far away) is m. The mass at the horizon r = 2m (Misner–Sharp)
    is also m (sympy). Both agree with Bronnikov–Kim's printed density: dMS/dr = r²ρ/2, residual 0.
  - Suppose the README is held at the horizon, the surface position 1 sees (H-HORIZON-HOLDS). The least horizon then
    has radius r_min(N), so the least pull is
    **E_pull = r_min c⁴/(2G) = √(N h c⁵ ln2/(8π² G)) = 4.59404002×10⁸ J × √N**, exactly chain.py's floor.
  - The floor was always a horizon: the neck sat *"at its own Schwarzschild radius"*. For the core README this is
    2.405878326×10¹⁶ J.
  - Bekenstein's bound, with E = the pull and R = the horizon, is then met with equality (H-STRONG-BOUND).
- **3. If the throat holds the README instead, the pull is pinned between the floor and 4/3 of it.**
  - With r₀ = r_min (H-NECK-HOLDS), the window gives
    **4.59404002×10⁸ J × √N < E_pull < 6.12538669×10⁸ J × √N**. Exact form: between 1 and 4/3 times
    √(N h c⁵ ln2/(8π² G)).
  - For the core: 2.405878326×10¹⁶ J to 3.207837767×10¹⁶ J. **The 0.1c trip (3.169434×10¹⁶ J) lies inside that
    window.**
  - The ends are r_min/2 and 2r_min/3 times c⁴/G = 1.21025556×10⁴⁴ J/m (relative uncertainty 2.2×10⁻⁵, from G).
- **4. The Penrose inequality is the family's own regularity condition.**
  - The plane's total energy (ADM, m/4 + r₀/2) exceeds the horizon's mass exactly when r₀ > 3m/2 (sympy). That is
    Bronnikov–Kim's condition for no singularity.
  - The Riemannian Penrose inequality says the total is at least the horizon's area-mass when the density is
    non-negative, with equality only for Schwarzschild (Bray, math/9911173v1, eq. 6 p.4 and Thm 1 p.8, READ by the
    verifier). It holds here with room to spare.
- **5. Item 102: both readings are exact, but in different members of the family.**
  - **The reciprocal (your option 2) holds exactly in your horizon corridor.**
    - At the floor, energy and size are reciprocal, with the README's size as the constant:
      **E_pull × r_horizon = N h c ln2/(4π²) = 3.48772679×10⁻²⁷ J·m × N**. This is Bekenstein's product, saturated.
    - The information definition fixes the product, so the mass is the inverse of the size.
  - **The negative (your option 1, the one you lean to) holds exactly only in the member with no horizon,
    m = −2r₀.**
    - There the total energy is zero.
    - With the Misner–Sharp split (H-MS-SPLIT, the board's choice of quasi-local mass), the energy outside the throat
      is −r₀c⁴/(2G), the negative of the throat's area-mass. That restates the zero total; it is not a second result.
    - Every direct reading is negative there:
      - the pull, −2r₀c⁴/G (−9.623513×10¹⁶ J for the core);
      - light bending, −r₀c⁴/G (−4.811757×10¹⁶ J).
      That is your *"must appear to contain"* (item 86.1).
    - But that member has no horizon, and the density is negative everywhere (eq. 18). So it is not the corridor your
      item 104(b) describes.
  - **Your two answers point at different members.** Which you mean is asked.
- **6. The twelve trajectories (item 104c).**
  - They are the 12-vector of multiverse_12_vector_taxonomy_v2.pdf, which the board already carries (CHARTER, item 23;
    settle.H12): V = [M, R, K, T, CP, α_s, Z0, Λ, G, G_F, G_θ, v].
  - You add that there can be more, and that anything observable can serve as a trajectory (H-TRAJECTORIES-OPEN). A
    destination universe can be chosen by any observable feature: *"a universe where religion was never invented"*.
  - **The board's reading of "ranked dependency" (R-CHAIN-RULE, ungraded):**
    - Each trajectory adds the information it carries given the ones ranked above it.
    - Under the floor's own rule, that is 7.24277891×10⁻⁷⁰ m² per bit added to the corridor's least area.
    - settle.H12 already records dependencies: R and Z0 are readouts of α, M of α, mₑ and v, and G_F is 1/(√2 v²) at
      tree level.
    - On this reading, a trajectory fixed by those ranked above it adds nothing.
  - How many bits a destination's trajectories carry is not computed: OPEN.
  - *First written:* "the device sizes the neck to the floor … 'No more, no less' is that bound met with equality".
    That dropped your trajectories' share: the floor is the README's share of the necessary size.
- **7. Your other answers (item 101), carried and placed.**
  - **Distance (answer 7):** eq. (17) has no separation parameter, and the floor takes none. That is consistent with
    H-DISTANCE-IRRELEVANT, not evidence for it.
  - **Separate universes (answer 5):** eq. (17) joins two asymptotic regions and does not make them one universe;
    BULK5-O1's one-universe clause is dropped.
    - Your *"transit phase through a dimension"* is a bulk throat, and eq. (17) is a 4D throat in the plane. That
      mismatch is named under H-BK-CORRIDOR.
  - **Your plain definition** (two universes, entangled, with the corridor as their Internet) is close to the two-sided
    picture READ by the board: an AdS black hole that *"can be dual to an entanglement of two different CFTs"*
    (Ryu–Takayanagi p.4).
    - But those bridges are non-traversable (Maldacena–Susskind fn.1), and an Internet needs traffic. The step from
      bridge to your corridor is wall 9, OPEN.
  - **Answers 3 & 4:** information is a form of energy, and newly introduced energy triggers a field reaction that
    allows matter assembly.
    - *The board's reading:* the README is the trigger, and the build's energy is the position's own (H-STOCK-IS-STOCK,
      H-FIELD-REACTION).
    - The README's own information is worth at most k_B · 310 K · ln2 = 2.96667818×10⁻²¹ J per bit, 8.14×10⁻⁶ J for the
      core. That rests on H-ERASE, chain.py.
    - The Higgs field was tested on the board as a source of energy-condition violation and closed for a classical,
      minimally coupled, canonical scalar (ledger D17). Any static Higgs displacement is ultralocal and returns at the
      rate m_h (D15, D16), and holding one costs energy (D20). These bound any "however slightly" reaction.
    - No assembly energy is computed: OPEN.
    - *First written:* "tested … as a supply of negative energy, and failed", the wording D17 corrects; and "untested".
  - **Answer 8:** position 2's read is an autodetection. The closed index takes the README, **verifies it**, and
    incorporates it (H-CLOSED-INDEX, H-AUTODETECT). The verification bears on completeness (answer 9). The scan at
    position 1 (COPY-O3) is unchanged.
  - **Answer 9:** completeness is relative, and position 2 knows only what the README holds (H-COMPLETENESS-IN-README).
  - **Answer 10:** read first, then execute, at position 2. *The board's reading:* this is the split rule wall 13 asked
    for, which is on which side the record ends. Please confirm it.

## What is ruled out, as the boundary

- **A positive-density member with a total below the horizon's or throat's area-mass.** The Riemannian positive-mass
  and Penrose inequalities rule it out (Bray, pp.2–4 and 8). A zero total needs negative density everywhere.
- **A horizon member with m ≥ 2r₀/3**, which brings the singularity outside the throat (the contrast).
- **Crossing to position 2's exterior.** The horizon members are non-traversable (Bronnikov–Kim p.4). The README's
  presence at position 2 needs the step from bridge to your corridor, which is OPEN.
- **The throat's size.** Bronnikov and Kim warn that *"a restriction can quite probably appear from 5-dimensional
  geometry"* (p.2). r_min for the core is 4.0×10⁻²⁸ m. BULK5-O1, OPEN.
- **Widening as a process.** A static family in r₀ is not a widening process; no dynamics are computed
  (H-QUASISTATIC).

## The walls, now

| wall | under your answers |
|---|---|
| 4 the corridor's energy | **the pull: at least the floor, 4.59404002×10⁸ J × √N (horizon holds), or between 1 and 4/3 of it (throat holds)** |
| 6 energy at position 2 | the README triggers, and the energy is the position's own. Bounded by D15, D16 and D20, not computed: OPEN |
| 8 the global bulk | the one-universe clause is dropped. The 5D completion is OPEN, and may restrict the throat's size (BK p.2) |
| 9 the coupling | the README's share of the size is the floor; the trajectories' share is OPEN. Traversability is OPEN |
| 10 address precision | no separation enters eq. (17) |
| 11 the read | position 2 autodetects and verifies. The scan at position 1 is unchanged |
| 12 identity completeness | relative, and defined by the README |
| 13 the split | read first, then execute, at position 2 (to confirm) |

*First written* with wall 4 "zero by your measure", under the ADM reading. You then chose the pull.

## Named hypotheses

- **Yours:** H-PULL-IS-COST, H-ONE-MOUTH-SEEN, H-CORRIDOR-HORIZON, H-TWO-SIDED-HORIZON (104b);
  H-INFORMATION-IS-INVERSE-MASS (102, 104a); H-TRAJECTORIES-OPEN (104c); H-READING-ONLY (86.1); and from item 101:
  H-MADE-AS-WIDENED, H-ENTANGLEMENT-IS-IT, H-INFORMATION-IS-ENERGY, H-FIELD-REACTION, H-SEPARATE-UNIVERSES,
  H-DEVICE-SIZES, H-TWELVE-TRAJECTORIES, H-DISTANCE-IRRELEVANT, H-CLOSED-INDEX, H-AUTODETECT, H-COMPLETENESS-IN-README,
  H-READ-THEN-EXECUTE, H-PROMPT-ANALOGY.
- **The board's:**
  - H-BK-CORRIDOR: eq. (17), a static 4D metric in the plane.
  - H-HORIZON-HOLDS / H-NECK-HOLDS: where the README's bits sit.
  - H-STRONG-BOUND; H-NECK-ENERGY.
  - H-MS-SPLIT; H-TOTAL-IS-ADM (now the boundary); R-CHAIN-RULE.
  - H-QUASISTATIC; H-RS1; H-ERASE.

## Sources READ

| source | route | used |
|---|---|---|
| Bronnikov & Kim, gr-qc/0212112v1 | Firecrawl; alphaXiv (verifier) | eq. 13 p.3; eq. 17, its range, the horizon case and eq. 18, p.4; p.2 the 5D restriction; p.6 *"a complete model …"* |
| Bray, math/9911173v1 | alphaXiv (verifier) | the Riemannian positive-mass theorem and Penrose inequality, eq. 5–6 p.4, Thm 1 p.8; ADM mass definition, Def. 21 p.54 |
| Ryu & Takayanagi, hep-th/0603001v2 | ENTANGLE.md | p.4 two CFTs |
| NOT READ | — | Bondi 1957 (negative mass); Schoen–Yau 1979, Witten 1981 (positive mass); Huisken–Ilmanen; Casadio–Fabbri–Mazzacurati (BK's [33]) |

## OPEN

1. Item 102: which member is your corridor. The horizon member makes the reciprocal exact; the negative is exact only
   without a horizon.
2. Where the README's bits sit: at the horizon (cost = the floor) or at the throat (cost between 1 and 4/3 of it).
3. The bits a destination's trajectories carry (R-CHAIN-RULE).
4. The step from a non-traversable bridge to your corridor (wall 9).
5. The 5D completion, and its restriction on the throat's size.
6. Wall 13: is "read first, then execute" the split rule?

## History (verifier, 2026-10-06; first-written claims kept above, each where it stood)

- **The headline** was "By your measure, a corridor can cost nothing, at any README size". That was the ADM reading,
  unnamed; every direct reading (the pull, light bending) is negative there. You then chose the pull.
- **"The corridor contains positive energy at its neck":** eq. (18) gives negative density everywhere at m = −2r₀.
  The throat's r₀/2 is its area-mass.
- **"Your item 102 has an exact counterpart: the negative part is the neck's inverse":** it restated the zero total,
  depended on the Misner–Sharp split, and put the bits on the positive member while you called the information
  definition the negative one.
- **The Bekenstein tension** at zero total was unstated (H-NECK-ENERGY). Under your pull answer it dissolves: the pull
  is positive and saturates the bound at the horizon.
- **The z3 checks** were one line of algebra each, and four checks restated others.
- **The control's m = 0.6 r₀** was called "inside the range". It is Bronnikov–Kim's horizon case, which is now your
  corridor.
- **Pages:** eq. 17 is p.4, not p.6.
- **Also corrected:**
  - "No matter on either plane" lacked the 5D caveat.
  - "Making is enlarging … safe" lacked H-QUASISTATIC.
  - "Distance … holds in every formula" over-read.
  - The two-sided picture needs traversability.
  - The Higgs wording.
  - "Verify it" was dropped from answer 8.
  - Answer 10's reading is the board's.
