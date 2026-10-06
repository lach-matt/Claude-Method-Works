# Everything entangled with everything (M-RULINGS item 100; deduced, computed and READ; verified once; not seated; 2026-10-06)

*First headed* "(M-RULINGS item 100; deduced, computed and READ; not verified; not seated; 2026-10-06)".

## What M said

- **Item 100:** *"Consider that until refuted everything is entangled to everything, however, the entanglements can
  range/differ in characterization."*
- Carried as **H-UNIVERSAL-ENTANGLEMENT**: every system is entangled with every other, until a refutation, and the
  entanglements range or differ in character. "In degree and in kind" is the board's gloss on your words.
- You gave it in answer to "which walls first", so it is taken as the thing to consider first.

Every number is printed by `entangle.py`.
- **Selftest:** 11/11 checks, 3 genuine controls and 1 contrast, with 7 STRUCTURAL lines printed and not counted.
  *First written* "10/10 checks, 3 genuine controls"; two of those controls could not fail (History).
- **Imported, not rebuilt:** `chain.py` and `vacuum.py`.

## What follows the work

- **1. Your second clause follows from your first, and both have read support.**
  - **Monogamy.** Horodecki et al., READ: *"no system can be EPR correlated with two systems at the same time"*
    (p.8; §XVI p.72).
    - If everything is entangled with everything, the entanglements cannot all be strong.
    - So they must range, as you said.
  - **Kinds differ.** *"there is free entanglement that can be distilled and the bound one"*, and *"inequivalent types
    of multipartite entanglement have been identified"* (p.6, READ).
  - **For field regions the vacuum supplies it at every separation** (vacuum.py: *"arbitrarily far-apart regions"*).
    - At a fixed probe window the degree falls faster than any power of the distance:

      | β = L/cT | strength (negativity per λ²) |
      |---|---|
      | 2 | 2.451×10⁻³ (communication not excluded) |
      | 4 | 5.615×10⁻⁷ (communication not excluded) |
      | 7 | 4.004×10⁻¹⁵ |
      | 10 | 8.201×10⁻²⁷ |
      | 14 | 3.066×10⁻⁴⁸ |

    - With a window scaled to the distance it does not fall. In vacuum.py's words, *"a fixed negativity at any L needs
      a window T proportional to L"*. So Proxima-distance entanglement is not intrinsically weak.
  - *First written:* "Your 'differ in characterization' is the fall with distance, computed". That dropped vacuum.py's
    window qualifier, the kinds, and monogamy.
- **2. The prior connection is the universe's**, if pre-shared entanglement counts as one.
  - That identification is named H-ENTANGLEMENT-IS-SETUP; it is item 99's R-ENTANGLED-SETUP.
  - It clears chain.py's finite-propagation clause by the encoding, so it is STRUCTURAL.
  - **What z3 shows:** under item 100, a made corridor is consistent where the entanglement already there reaches the
    README's size N. With half of it, making by local action is inconsistent. **So under item 100, "made" and "found"
    meet.**
  - Control: with no prior connection from any source, the made corridor is inconsistent. Your hypothesis is one source
    of that connection; H-PRIOR-SETUP is another.
- **3. The corridor's neck has the area of N ebits. This is one formula, not two routes.**
  - **The Ryu–Takayanagi area law**, READ: eq. 1.5, p.1, *"we propose the following 'area law'"*.
    - Its normalization *"is fixed from Eq. (1.1)"*, Bekenstein–Hawking, p.4.
    - Its two-sided case is *"the AdS black hole can be dual to an entanglement of two different CFTs"*, p.4.
  - It gives N ebits a least area of **2 h G ln2/(π c³) × N = 7.24277891×10⁻⁷⁰ m² × N**.
  - That is chain.py's neck, and necessarily so: Bekenstein's bound saturated at the Schwarzschild radius *is* the
    Bekenstein–Hawking area law.
  - With ER=EPR and **H-HOLD-IS-ENTANGLE** (the bits a neck holds are counted as the ebits it carries), the neck that
    holds an N-bit README has the area of N ebits.
  - *First written:* "That is exactly the neck chain.py found by another route … The selftest checks the two against
    each other". It was the same formula, checked against itself.
- **4. What widening needs (z3), with the source's own qualifier.**
  - Entanglement *"can not be increased on average when systems are not in direct contact but distributed in spatially
    separated regions"* (Horodecki, p.4, READ).

  | how a bridge of N/2 is brought to N | z3 |
  |---|---|
  | found already at N, device local | consistent |
  | local action, every time (deterministic) | **inconsistent** (contrast) |
  | local action, heralded, succeeding half the time | consistent: at most E_exist/N = 1/2 |
  | local action, heralded, succeeding 60% of the time | inconsistent |
  | a quantum carrier with N/2 qubits | consistent |
  | a quantum carrier with N/4 qubits | inconsistent: one qubit adds at most one ebit |
  | your unidentified carrier | consistent (carried with no bound) |

  - The per-qubit bound: Horodecki §XV.J asks *"How much can entanglement increase under communication of one qubit?"*.
    Chen and Yang's title answers *"at most"* one ebit (quant-ph/0006051). The title is READ; the proof is not.
  - Controls: dropping the on-average clause, or the per-qubit bound, makes the inconsistent rows consistent.
  - *First written:* "Widening a thinner bridge by local action alone is inconsistent". That was single-run, where the
    source says "on average". The table also once read "nothing bounds" a quantum carrier.
- **5. Only the crossing needs your carrier.**
  - Widening across the cut can be ordinary physics done before the joining: a quantum carrier at or below light
    speed, or entanglement swapping through the entanglement already everywhere.
  - Its lead time is at least L/c, and it is consistent with H-PRIOR-SETUP and your H-INSTANTANEOUS.
  - What your H-UNIDENTIFIED-CARRIER must do is the README's crossing at trip time.
  - ER=EPR's bridges are non-traversable (Maldacena–Susskind fn.1). Your corridor, *"two places made one"*
    (H-IDENTIFY), is not claimed to be one of them. The step from bridge to your corridor is wall 9, OPEN.
  - Candidate reading, not done: Gao–Jafferis–Wall (1608.05687) and Maldacena–Stanford–Yang (1704.05333), on bridges
    made traversable by a coupling.
  - *First written:* "The two remaining needs land on one hypothesis of yours" and "an ER=EPR bridge … so the README's
    presence at position 2 needs a carrier". That bent your corridor into an ER=EPR bridge.

## What is ruled out, as the boundary

- **Deterministic local widening** of a bridge thinner than the README, and heralded local widening above E_exist/N.
- **Weak entanglement as classical geometry.** Pair bridges are *"Planckian"* and *"probably"* not classical
  (Maldacena–Susskind p.17). Geometry likely fails *"before the entanglement is strictly zero"* (Van Raamsdonk fn.1).
  Both are READ in geometry.py. Whether a found throat is classical is OPEN, and it is wall 3's quantity.
  *First written:* "Your found throats … are the bridges of the entanglement already there".
- **If near-maximal pairs were needed** (H-NEARMAX) rather than entropy, concentrating the entanglement needs one
  classical message after the window: L/c = 1.340081×10⁸ s for Proxima. That is prior setup, not a delay in the
  teleport.
- **Operations at position 2.** Using entanglement there needs operations there (H-POSITION-OPERATES, the board's
  extension of your H-POSITION-BUILDS). *First written:* "No probe crosses … (H-POSITION-BUILDS)", unnamed.

## The walls, as this changes them

| wall (chain.py) | under H-UNIVERSAL-ENTANGLEMENT |
|---|---|
| 1 formation | made meets found (point 2): every corridor is a widening of a bridge already there, and widening is not topology change (create.py). This holds only if that bridge is classical geometry, which is OPEN |
| 2 reaching position 2 | met as to the prior connection, under H-ENTANGLEMENT-IS-SETUP. Whether enough entanglement is there (N ebits) is wall 3 |
| 3 throat existence | becomes **how much**, and **whether classical**: how many ebits already join the two places across the cut the device triangulates. OPEN. Monogamy bounds it: an N-ebit bridge excludes its degrees of freedom from other strong entanglement |
| 4 the corridor's energy | the same number, by construction (point 3). Its cost is now your item 101 (PLANE.md) |
| 9 the coupling | sharpened: no deterministic local widening (point 4). Widening by ordinary means beforehand is allowed (point 5). The step from bridge to your corridor is OPEN |
| the README's crossing | your carrier (point 5) |

*First written* without wall 1, with row 2 "met by the existing connection", and with row 9 "local action cannot
widen".

## Named hypotheses

- **Yours:** H-UNIVERSAL-ENTANGLEMENT (100); H-UNIDENTIFIED-CARRIER (90); H-COMMON-THROATS, H-MADE (86.3);
  H-SINGLE-CHANNEL-GROWS (94); H-POSITION-BUILDS (91); H-IDENTIFY (95); H-INSTANTANEOUS (94).
- **The board's:**
  - H-ER=EPR: Maldacena–Susskind's conjecture, which they introduce as speculation.
  - H-RT-HERE: the area law, proposed for anti-de Sitter space, applied here.
  - H-SI-RESTORE: the area law with SI units restored.
  - H-HOLD-IS-ENTANGLE: bits held are counted as ebits. Entanglement *"does not carry information itself"*
    (Horodecki p.4).
  - H-ENTROPY-COUNTS: pure-state entanglement entropy is the measure. Its alternative is H-NEARMAX.
  - H-ENTANGLEMENT-IS-SETUP; H-CUT; H-LOCC; H-POSITION-OPERATES; H-SUBADD (the per-qubit bound).
  - From chain.py: H-NECK-HOLDS, H-STRONG-BOUND.
  - From vacuum.py: H-UDW, H-PERTURB, H-MINK-VAC, H-SPACELIKE.

## Sources READ

| source | route | used |
|---|---|---|
| Ryu & Takayanagi, hep-th/0603001v2 | Firecrawl and alphaXiv, pp.1–5 | eq. 1.5 p.1; eq. 1.1; p.2 *"saturates the bound"*; p.4 normalization from eq. 1.1; p.4 two CFTs |
| Horodecki ×4, quant-ph/0702225v2 | Firecrawl and alphaXiv | p.4 *"can not be increased on average …"*, *"does not carry information itself"*; p.6 *"cannot bring in entanglement for free"*, free versus bound, multipartite types; p.8 and §XVI p.72 monogamy; §XV.J heading; Chen–Yang title (reference list) |
| Maldacena & Susskind; Van Raamsdonk; Reznik and others | geometry.py, vacuum.py (READ there) | ER=EPR, non-traversability, p.17 Planckian; fn.1; the vacuum's entanglement |

## OPEN

1. How many ebits, and of which kind, already join the Sun and Proxima across the cut a device would triangulate.
2. Whether weak entanglement's bridges are classical geometry (Maldacena–Susskind p.17, Van Raamsdonk fn.1).
3. The step from an ER=EPR bridge to your corridor (H-IDENTIFY), which is wall 9.
4. Whether the area law holds outside anti-de Sitter space (H-RT-HERE).
5. A refutation of H-UNIVERSAL-ENTANGLEMENT, which your "until refuted" invites. A candidate, NOT READ: highly mixed
   pairs are separable (Życzkowski–Horodecki–Sanpera–Lewenstein, quant-ph/9804024, a ball of separable states around
   the maximally mixed state). *First written* "None is held."

## History (verifier, 2026-10-06)

Twenty-five findings were applied. The main ones:

- E3 was not an independent agreement.
- The per-nat and without-UE controls could not fail.
- E2 was definitional.
- LOCC monotonicity holds on average, not in a single run.
- A quantum carrier is bounded per qubit.
- HOLDS is one-way, and H-HOLD-IS-ENTANGLE is now named.
- Only the crossing needs your carrier.
- Found throats are classical only above a threshold, which is OPEN.
- The β = 2 and 4 rows lie outside the no-signalling scope.
- The window qualifier, the kinds and monogamy were added.
- Wall 1 was added.
- The exact form had printed "0".
