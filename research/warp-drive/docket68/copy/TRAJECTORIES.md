# The trajectories' share of the corridor (M-RULINGS item 113, first of three; deduced and computed; verified once; SEATED (ledger.py section 8o); 2026-10-06)

*Seated in ledger.py section 8o on M's order of work (item 113); until then headed "… not seated …".*

*First headed* "(…; not verified; not seated; 2026-10-06)".

## What M said (verbatim in the rulings file)

- **101.6:** *"The 12 trajectories also contributed to the size of the corridor depending on ranked dependency for each
  trajectory."*
- **104(c):** *"They were proposed by Gemini in the taxonomy paper in the warp folder of Google drive. They are based on
  quantum physics forces that help define the geometric shape iof any object. 12 was proposed by Gemini, however, there
  can certainly be more ... Consider that anything I can observe can be used as a trajectory …"*
- **23:** *"… Each one is a physics condition that governs an aspect of the reconstruction at seating. These 12 allow for
  the predetermination of seat compatibility based on the starting state - entanglement at 12 criteria."*
- **24:** *"The 12 conditions only need to supply enough for the object to reconstruct in the new environment"*.
- **25:** *"… the magnitude of probabilities (negative and positive), and complex binary come into play. The stronger
  negative magnitudes will automatically triangulate the stronger positive magnitudes which rank the probability of
  seating"*.
- The twelve are settle.H12's 12-vector: **V = [M, R, K, T, CP, α_s, Z0, Λ, G, G_F, G_θ, v]**. Only H12's first column
  comes from the taxonomy; its class and carrier columns are the board's.

Every number is printed by `trajectories.py`.
- **Selftest:** 8/8 checks, 3 genuine controls, with 7 STRUCTURAL lines printed and not counted.
- *First written* "6/6 checks, 2 genuine controls". One of those checks was an identity, and one control used a
  hand-made row.

## Your answers (item 114), and what they settle

- *"The trajectory is determined by the initial definition of the object transporting, and its input as a user
  defining the counterfactual requirements as position 2. The trajectory is the difference between position 1 and
  position 2"* (H-TRAJECTORY-IS-DIFFERENCE).
- *"The principle or mechanism that determines such properties is the trajectory"* (H-TRAJECTORY-IS-MECHANISM).
- Whose limits: *"Both"* (H-BOTH-LIMITS).
- On the ranking, *"Read my last input"*. The board reads that as your trajectory-as-difference answer.

**What follows (the board's reading, ungraded):**
- **A trajectory's bits are the information in the difference between position 1 and position 2 that the object's
  definition depends on.** You tie the trajectory to *"the initial definition of the object transporting"*.
  - Counting it as H(P2 | P1) would need a probability distribution over destinations. None is named.
  - For a single destination it is the conditional description length (H-CLASSICAL-SHANNON, or its single-case form).
  - *First written:* "what position 2's specification adds given position 1's, H(P2 | P1)".
- **A destination with the same laws as the start differs in none of the twelve.** Proxima, in our universe, is one,
  so the twelve add 0 bits for it.
  - Position 2 still has to be specified. chain.py's wall 10 measures the address error at Proxima as more than 100
    times Proxima b's orbit.
  - Your item 101.7 says the device never sees the distance. It does not say the address carries no bits.
  - The address's bits are OPEN, and whether location counts as a trajectory is asked.
  - *First written:* "Its trajectories add 0 bits, and the corridor is the README's alone".
- **A counterfactual destination adds the information in your requirements,** given the starting state.
- **The ranking orders the differences,** and a difference fixed by higher-ranked ones adds nothing (points 1 and 3
  below).
- **K and T:** the trajectory is the mechanism (the Kondo exchange mechanism; the phonon anharmonicity), not the
  material's value.
  - Those mechanisms follow from quantum mechanics and electromagnetism (α, mₑ) applied to a material. So, like M and
    R, they are readouts of other laws.
  - Under H-TRAJECTORY-IS-MECHANISM they join the dependent class: they add at most H(mechanism | α, mₑ, …), which is
    OPEN.
  - Point 3's count (taken from H12's own text) is unchanged. Point 4's illustration would count 7 trajectories, not 9.
  - *First written:* "trajectories of the object or the site", then "So they are laws, and universe-level after all".
- **Both limits:** a corridor's horizon must fit under both ends' cosmological ceilings, 1/√Λ at each.
  - Ours is 0.698 c/H0, conditional on Ω_Λ (NOT READ).
  - The core's horizon, 4.0×10⁻²⁸ m, sits 2.4×10⁵³ times below it (printed by trajectories.py). The order of
    magnitude is robust to Ω_Λ.
  - The README's N must also fit under both ends' holographic counts.

## The board's reading, and where it differs from your sentence

**R-CHAIN-RULE, ungraded, under ordinary (classical) information counting.**
- A trajectory adds the information it carries given those ranked above it.
- Suppose n trajectory bits are held with an N-bit README (H-TRAJECTORIES-IN-README):
  - each bit adds **2hG ln2/(πc³) = 7.24277891×10⁻⁷⁰ m²** to the corridor's least area;
  - the least energy becomes **√(ħc⁵ ln2/(4πG)) × √(N + n) = 4.59404002×10⁸ J × √(N + n)**;
  - the trajectories' share is n/(N + n) of the area and about n/(2N) of the energy.

**Under this reading the total does not depend on the ranking, but your sentence says the size does.** Two readings of
your own words would make it depend:
- Ranking by signed or complex magnitudes (item 25, H-SEATRANK).
- A stopping rule: trajectories taken in rank order until there is "only … enough" (item 24, H-STOP-WHEN-ENOUGH).

This was asked. Item 114's answer, read as "the difference between position 1 and position 2", still leaves the total
independent of the ranking, classically and for quantum states. So the tension with your item 101.6 persists, and it
is asked again.

## What follows the work

- **1. Classically, ranking moves who carries the information.**
  - On a small example (H-TOY), trajectories that follow from others add 0 when ranked after them.
  - Ranked first, they carry information instead, and the ones they follow from carry less.
  - The total, 3.331914641898 bits, is the same in every order. That is an identity, so it is STRUCTURAL.
  - Control: independent trajectories add their own information even ranked last.
- **2. Quantum-correlated trajectories can subtract (your item 24, H-12Q).**
  - If the twelve are literally quantum-correlated, each term is a quantum conditional entropy, and those can be
    negative.
  - For a maximally entangled pair, the second member adds **−1 bit** (computed). A trajectory ranked after its
    entangled partner lowers the count.
  - Control: an unentangled pair gives ≥ 0.
  - This is a candidate meaning of your "negative magnitudes" (item 25); the reading is the board's.
- **3. Two of the twelve add nothing once their parents are ranked above them, and one adds at most a little.**
  - R adds 0: it is a readout of α, and Z0 is α (*"Z0 = 2 alpha h/e^2"*).
  - G_F adds 0: it is 1/(√2 v²) at tree level (H-TREE-LEVEL).
  - M adds at most H(mₑ | α, v), and mₑ is not one of the twelve. How much is OPEN.
  - K and T are material properties in H12's text. Under item 114 (H-TRAJECTORY-IS-MECHANISM) they are mechanisms that
    follow from other laws (see above). Their bits are OPEN.
  - Seven have no dependence recorded in H12 (H-NO-RECORDED-DEPENDENCE): CP, α_s, Z0, Λ, G, G_θ and v.
    - That does not show they are independent. H12 ties CP to the Higgs–Yukawa sector, which is v's field.
    - Under your H-UNIVERSAL-ENTANGLEMENT, the information they share is presumed non-zero until refuted.
  - Control: strip the real H12 row for R of its "readout of α", and R leaves the dependent set.
  - *First written:* "Three of your twelve add nothing … M adds only mₑ's information", which contradicted itself; and
    "Seven are universe-level, and the taxonomy records them as independent".
- **4. Below a computed threshold, the trajectories are a negligible share.**
  - The area share stays below 10⁻⁶ while n < 10⁻⁶ N, which is 2.742570×10⁹ bits for the core README.
  - Illustration only (H-ILLUSTRATIVE): the nine trajectories point 3 does not set to zero, at 64 bits each, give an
    area share of 2.1×10⁻¹³ and an energy share of 1.05×10⁻¹³.
  - *First written* with 12 × 64 bits, which counted the trajectories that add nothing.
- **5. The whole-universe figure is a boundary, not a corridor.**
  - The Hubble sphere's Bekenstein–Hawking count is **N_H = πc⁵/(ħGH0² ln2) = 3.272224×10¹²² bits** (relative
    uncertainty 1.6×10⁻²).
  - Sized by the flat-space floor, it gives:
    - **r = c/H0 = 1.373312×10²⁶ m**, the Hubble radius;
    - **E = c⁵/(2GH0) = 8.310292×10⁶⁹ J**, each with relative uncertainty 8.0×10⁻³.
  - That energy is exactly the critical-density mass-energy of the Hubble sphere (an identity).
  - **The caveats:**
    - c/H0 is the apparent horizon only in a flat expanding universe.
    - With Λ > 0, the asymptotic de Sitter count is larger: 4.779×10¹²² bits (Ω_Λ NOT READ).
    - The board grades Bousso's covariant bound NARROWED: it is a conjecture, and it does not cover matter that violates
      the null energy condition, which the corridor reads as.
    - **With our Λ, no black-hole horizon is larger than 0.698 c/H0** (Schwarzschild–de Sitter, computed; Nariai NOT
      READ). So a corridor of that size cannot exist here.
    - A counterfactual universe has its own H0 and Λ.
    - A larger H0 (SH0ES, NOT READ) would move N_H by about 15%.
  - *"A universe where religion was never invented"* lies between point 4 and point 5. With your universe as the
    starting state (item 23), it adds only what distinguishes the destination from yours. How much is OPEN.
  - *First written:* "a corridor the size of the observable universe". That is the Hubble radius, and the figure is a
    boundary, not a corridor.
- **6. The trajectories ride with the README.**
  - Under H-TRAJECTORIES-IN-README, they cross with it through your three holds (item 106).
  - The trip is then one E_min(N + n), delivered into position 2's build (items 110 and 111).
  - Monogamy (Horodecki p.8), under H-12Q and H-HOLD-IS-ENTANGLE: degrees of freedom already maximally entangled as the
    README's bridge cannot also carry the twelve criteria's correlations. So n adds to N rather than sharing it.

## Named hypotheses

- **Yours:** H-TWELVE-TRAJECTORIES (101.6), H-TRAJECTORIES-OPEN (104c), H-12Q (24), H-SEATRANK (25),
  H-UNIVERSAL-ENTANGLEMENT (100), H-REFERENCE-UNIVERSE (23).
- **The board's:**
  - R-CHAIN-RULE, H-CLASSICAL-SHANNON, H-STOP-WHEN-ENOUGH (a reading of item 24);
  - H-TOY, H-TREE-LEVEL, H-NO-RECORDED-DEPENDENCE, H-ILLUSTRATIVE, H-TRAJECTORIES-IN-README;
  - H-FLAT-FRW-APPARENT-HORIZON, H-BOUSSO-CONJECTURE, H-ASYMPTOTICALLY-FLAT, H-SAME-H0, H-PLANCK-H0, H-UNIFORM-RANGE;
  - from chain.py: H-STRONG-BOUND, H-HORIZON-HOLDS.

## OPEN

1. Which ranking you mean. *Read, item 114: the ranking orders the differences between position 1 and position 2.*
2. The precision and range each trajectory needs, and so its bits; and K's and T's bits per object and site.
3. How much a destination defined by one observable feature adds, given your universe.
4. Whether the seven trajectories with no recorded dependence share information (presumed yes under item 100).
5. A counterfactual destination's own H0 and Λ, which set its boundary.
