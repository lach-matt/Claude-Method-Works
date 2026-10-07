# The Warp Theorem (M-RULINGS item 150; one statement built from the pieces; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you said

- **Item 150:** *"The approach needs to be to stop piecing together theorems to fit my theory, instead we need to
  consider one single theorem built from the pieces that defines the warp theory as a single statement"*.
- **So the board's separate results are now lemmas of one theorem.** What is not yet proved is a named lemma of it, not
  a separate question.
- **The instrument:** `warptheorem.py`. It imports exactE.py, coin.py, passage5d.py, localbulk.py and stability.py by
  path. Selftest 7/7, about 70 s.
  - **Genuine checks:** six.
  - **Control:** one.
  - **Marked STRUCTURAL:** one.

## The theorem

> **For an object whose README — its one fixed exact encoding, labels and values, written in what every universe
> shares — has N bits, there is exactly one corridor, fixed by N alone, and through it the README becomes, one way and
> exactly, the object at position 2.**

The corridor is the following, clause by clause.

- **(G) Geometry.**
  - It is Bronnikov–Kim's eq. (17) at r₀ = 2m on the plane.
  - **E = √(N h c⁵ ln2 / (8π²G)) = 459,404,002.42 J × √N.**
  - **m = GE/c⁴.**
  - **r₀ = 2m = √(N h G ln2 / (2π²c³)).**
- **(H) Holding.**
  - The throat holds exactly the README: **4πr₀² = N × 2hG ln2/(πc³)**, which is 4 ln2 Planck areas per bit.
  - The horizons hold it too.
- **(O) One way.**
  - The passage runs from position 1 to position 2 through an extremal horizon, with surface gravity 0.
  - It is nonsingular and complete, and it never runs back.
- **(Z) Null energy never violated.**
  - Along the passage the five-dimensional null energy is zero.
  - The plane's apparent deficit is exactly the bulk's pull. Its integral is
    **8/(3m) − (4/(3√3·m))·artanh(√3/2) per unit E.**
- **(B) Bulk.**
  - A vacuum five-dimensional bulk carries the corridor. The plane is free of matter, at the Randall–Sundrum tension.
  - The plane's two ends are one end of the bulk.
  - The energy is positive at every point.
  - The bulk's scale k is fixed by the work.
- **(I) Information.** The passage is N bits of entanglement, and it carries the N-bit README.
- **(E) Energy.**
  - One exact energy E is carried from position 1 through three holds.
  - It is released into position 2 at the closing, with every joule accounted for.
- **(R) Reconstruction.**
  - Position 2's matter rearranges to the README exactly, with no tolerance. After that, position 2's laws govern.
  - The corridor's length is set by the trajectories, the difference between the two positions.

## Its lemmas

The theorem is proved exactly when no lemma below is OPEN.

| clause | lemma | status |
|---|---|---|
| G | G1 one exact energy, at the bound | **yours**, items 133, 136 answer 1 |
| G | G2 E(N) computed and machine-checked | **proved**, exactE.py (seated) |
| G | G3 both holds at least size give r₀ = 2m | **proved**, exactE.py |
| H | H1 4πr₀² = N·A_bit | **proved**, exactE.py |
| H | H2 the horizons hold the README too | **yours**, items 106, 132 |
| O | O1 one way, 1 → 2, nonsingular | **proved**, plane.py P1 (seated); exactE.py |
| O | O2 extremal horizon | **proved**, stability.py S1 |
| Z | Z1 5D null energy zero along the passage; deficit = bulk pull | **proved**, passage5d.py P2 |
| Z | Z2 the integral equals the plane's reading on both legs | **proved**, passage5d.py P3, coin.py |
| Z | Z3 null energy never violated | **yours**, items 117, 120, 123 |
| B | B1 plane matter-free; Gauss and Codazzi met | **proved**, localbulk.py |
| B | B2 a local vacuum bulk exists, unique among analytic ones | **proved**, localbulk.py |
| B | B3 a complete bulk exists, under closed-index criteria | **yours**, items 120, 121 |
| B | **B4 the global bulk: the plane's two ends one end of the bulk, with CGS Thm 3.5's deformation** | **OPEN** |
| B | **B5 positivity at every point** | **OPEN** (your order, item 139 (2)) |
| B | **B6 k fixed by the work** | **OPEN** (your order, item 140) |
| B | **B7 formation: opening and closing between static planes** | **OPEN** |
| I | I1 the passage is N bits of entanglement | **yours**, item 137 |
| I | **I2 N bits carried by N bits of entanglement meets the capacity bound** | **OPEN** (to compute) |
| E | E1 E carried through three holds into position 2 | **yours**, items 106, 110, 111, 115 |
| E | E2 released at position 2 at the closing | **yours**, item 136 answer 2 |
| E | **E3 where the remainder goes, shown to close the ledger** | **OPEN** |
| R | R1 exact reconstruction, no tolerance | **yours**, items 145, 146 |
| R | R2 position 2 rearranges to the README; then its laws govern | **yours**, item 148 |
| R | R3 exactness at the instant over the mass window | **proved**, exactcopy.py, rearrange.py (not re-run here) |
| R | **R4 the corridor's length, given a measure** | **OPEN** |

- **The count:** 11 lemmas are yours, 9 are proved, and **7 are OPEN**.
- **T2 (STRUCTURAL)** confirms that the theorem follows from all its lemmas, and that dropping any OPEN lemma loses it. So
  these seven are exactly what stands between the statement and a proof.

## What the theorem found that the pieces did not: the energy ledger (T3)

- **Built as one statement, the energy clause can be checked for consistency with the reconstruction clause.**
  - At the board's example README, E = 2.405878×10¹⁶ J.
  - The copy's composition is exact (146) and its matter is reorganized (137). So the copy can absorb at most the
    assembly energy, 1.1947×10¹⁰ J.
- **z3 finds your rulings inconsistent, unless the remainder has somewhere to go.**
  - With no sink: unsatisfiable.
  - With your item 139's expansion of position 2's universe as the sink: satisfiable.
  - **Control:** at N = 600 bits, E is 1.1253×10¹⁰ J, below the ceiling, and consistent with no sink.
- **So lemma E3 is not optional.** On your rulings, item 139's *"Absorbing of the README into position 2 is an expansion
  of that universe"* is where the remainder goes.
  - Reading it that way is the board's reading.
  - Showing that this closes the ledger is lemma E3's work.

## The work left, as the theorem's lemmas

- **B4 and B7 together:** the corridor's five-dimensional form, made and closed between static planes, with the two
  ends one end of the bulk (your items 126, 127, read by the board).
- **E3:** the ledger, closed through the expansion.
- **B5:** positivity at every point.
- **B6:** k from the work.
- **I2:** the capacity bound, met with equality.
- **R4:** the length, given a measure.

None needs a ruling from you (item 149).

## Named hypotheses

- **Yours:** every lemma marked "yours", and M-ONE-THEOREM (150).
- **The board's:**
  - reading B4 as your items 126–127;
  - reading E3 as item 139's expansion;
  - H-COMPOSITE-SURFACE, H-THICK-COMPOSITE, H-BK-CORRIDOR.
