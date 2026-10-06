# The trajectories' share of the corridor (M-RULINGS item 113, first of three; deduced and computed; not verified; not seated; 2026-10-06)

## What M said

- **Item 101.6:** *"The 12 trajectories also contributed to the size of the corridor depending on ranked dependency
  for each trajectory."*
- **Item 104(c):** *"They were proposed by Gemini in the taxonomy paper … 12 was proposed by Gemini, however, there can
  certainly be more ... Consider that anything I can observe can be used as a trajectory, for example my universe or
  rather my spacetime contains religious ideals and I may want to travel to a universe where religion was never
  invented...."*
- **Item 23:** *"the math for the corridor is formed by the 12 trajectories of navigation … entanglement at 12
  criteria"*.
- The twelve are the 12-vector the board carries in `settle.H12`, from multiverse_12_vector_taxonomy_v2.pdf:
  **V = [M, R, K, T, CP, α_s, Z0, Λ, G, G_F, G_θ, v]**.

Every number is printed by `trajectories.py`.
- **Selftest:** 6/6 checks, 2 genuine controls, with 3 STRUCTURAL lines printed and not counted.
- **Imported, not rebuilt:** `chain.py` (the floor), `settle.py` (the twelve) and `cosmo.py` (H0).

**The board's reading (R-CHAIN-RULE, ungraded).** A trajectory adds the information it carries beyond the trajectories
ranked above it.
- Each added bit enlarges the corridor's least area by 7.24277891×10⁻⁷⁰ m² (chain.py, under H-STRONG-BOUND and
  H-HORIZON-HOLDS).
- With n trajectory bits beside an N-bit README, the trajectories' share of the area is n/(N + n), and the energy
  grows by a factor √(1 + n/N).

## What follows the work

- **1. Ranking decides each trajectory's share, not the total.**
  - The chain rule gives the same total information in every ranking. Computed exactly on a small example
    distribution (H-TOY): 3.331914641898 bits in all three orders.
  - What moves is who carries it:

    | ranking | Z0 | v | R | G_F |
    |---|---|---|---|---|
    | parents first (Z0, v, R, G_F) | 1.8464 | 1.4855 | **0** | **0** |
    | readouts first (R, G_F, Z0, v) | 0.8755 | 0 | 0.9710 | 1.4855 |

  - So your "ranked dependency" decides which trajectory pays, not how much the corridor grows.
  - Control: if R and G_F were independent, they would add their own information even when ranked last.
- **2. Three of your twelve add nothing once their parents are ranked above them.**
  - `settle.H12` records:
    - M and R as readouts of α (M also of mₑ and v);
    - G_F as 1/(√2 v²) at tree level;
    - Z0 as α itself (*"Z0 = 2 alpha h/e^2"*).
  - With Z0 and v ranked above them, R and G_F add 0 bits, and M adds only mₑ's information (H-TREE-LEVEL for G_F).
  - K and T are material properties, so they belong to the object or the site rather than to the universe.
  - Seven are universe-level, and the taxonomy records them as independent: CP, α_s, Z0, Λ, G, G_θ and v.
  - Control: the classification rule reads the taxonomy's own text. Remove R's "readout of" and R becomes independent.
- **3. Constants specified to measurable precision are a negligible share.**
  - The trajectory bits must reach the README's own size (2.74257×10¹⁵ bits for the core) before they double the area.
  - As an illustration only (H-ILLUSTRATIVE), 12 trajectories × 64 bits gives an area share of 2.8×10⁻¹³ and an energy
    factor of 1 + 1.4×10⁻¹³.
  - The precision and range each trajectory actually needs is OPEN (H-UNIFORM-RANGE: bits = log₂(range/precision)).
- **4. A whole counterfactual universe has a ceiling: the Hubble horizon.**
  - The most any specification of a universe like ours can carry is its horizon's Bekenstein–Hawking count:
    **N_H = πc⁵/(ħ G H0² ln2) = 3.272×10¹²² bits** (H0 = 67.36 km/s/Mpc, cosmo.py; relative uncertainty 1.6×10⁻²).
  - A corridor sized for it has radius **c/H0 = 1.3733×10²⁶ m** and least energy **c⁵/(2 G H0) = 8.3103×10⁶⁹ J**: a
    corridor the size of the observable universe (H-HOLOGRAPHIC-CEILING).
  - *"A universe where religion was never invented"* lies between points 3 and 4.
    - With your own universe ranked first (H-REFERENCE-UNIVERSE), it adds only what distinguishes the destination from
      yours.
    - How much that is, is OPEN.

## The wall, as this changes it

- **Wall 9, the coupling.** The README's share of the size is the floor.
- The trajectories' share is n/(N + n) of the area, set by the ranked conditional information:
  - zero for the three readouts once their parents are ranked above them;
  - negligible for constants at measurable precision;
  - up to the Hubble horizon for a whole counterfactual universe.

## Named hypotheses

- **Yours:** H-TWELVE-TRAJECTORIES (101.6), H-TRAJECTORIES-OPEN (104c), H-12Q (item 24).
- **The board's:** R-CHAIN-RULE; H-TOY; H-TREE-LEVEL; H-ILLUSTRATIVE; H-HOLOGRAPHIC-CEILING; H-REFERENCE-UNIVERSE;
  H-UNIFORM-RANGE; and chain.py's H-STRONG-BOUND and H-HORIZON-HOLDS.

## OPEN

1. The precision and range each trajectory needs, and so its bits.
2. How much a destination defined by one observable feature (*"religion was never invented"*) adds, given your own
   universe.
3. Whether the twelve "quantum-correlated" criteria (H-12Q) are counted in ebits (ENTANGLE.md) or in bits. Under
   H-HOLD-IS-ENTANGLE the two are the same count.
