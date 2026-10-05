# Step 1b — the balanced equation (first pass, 2026-10-05)

Instrument: `step1b/balance.py` (`--selftest`: 33/33 pass, 5 of them controls, 1 STRUCTURAL item printed and not
counted). It reads the research tree and writes nothing. Every figure is imported from its owner: `measure.py`,
`seat.py`, `transit.py`, `massform.py`, `stock.py`, `nopath.py`.

## M's definition (docket68/M-RULINGS-2026-10-03.md, items 29–30, verbatim)

> Balanced means that the value of the object at first position must equal the value of the object at the second
> position. And any variable input must be accounted for in output

On what the value is, M: "Information only".

So: **I(A, before) = I(B, after)**. Every matter and energy term is an input or an output, and every input must be
accounted for by some output.

## What it computes

**The value.** I is counted four ways, under the hypotheses `measure.py` names. M's words do not fix which count is the
object's information (H-WHICH-COUNT), so all four are carried: species sequence 9.509e27 bits, 1 Å grid 4.142e28,
0.1 Å grid 1.088e29, thermal entropy 2.84e28.

**Does the value balance?** Two readings are carried.
- R-QUANTUM (teleportation, `transit.teleport`, over 400 random states):
  - With the two bits sent, B's least fidelity is 1.000000000000.
  - A's four outcomes are equiprobable for every state, with largest deviation 2.2e-16. The record alone holds no I.
  - With the bits withheld, B's fidelity is 0.5 for every state, because B holds I/2. Without the channel the value
    does not balance.
- R-CLASSICAL: I bits are sent. A classical record can be copied, so I(A) does not fall to zero by sending it.

**A finding that holds on both readings.** Teleportation moves state, not species (`transit.CARRIES_SUBSTANCE =
False`). So the classical part of I, the species sequence, is still present at A after the transfer. The object at A
leaves only through an output term: OUT-A-RESIDUE, A's 70 kg retired as stock at A. If that term is left out, the
balance holds and the object is at both positions. M's condition, "either at the beginning or end position, never in
between", therefore needs that output term. The value equation does not supply it.

**Conserved quantities.** These are a consistency column, not the value. The object has 6.712e27 atoms,
2.313e28 electrons (Z read via `massform.Z_OF`), mass number ~4.215e28 (H-BARYON-BY-MASS) and charge 0. The column
closes site by site, and **the transfer of every conserved quantity from A to B is 0**: only I crosses. At B the closure
is D25's stock gate. The CI-chondrite feedstock is 749.1 kg, with phosphorus (P) as the binder and a residue of
679.1 kg. P is measured nowhere in the Proxima system (`seat.P_MEASURED_IN_PROXIMA_SYSTEM = False`), so the closure at
B is OPEN there. This column closes by construction, so it is printed as STRUCTURAL and not counted.

**The equation's terms.** For every count and reading, every input is accounted for by an output (checked). Two
controls guard the check: dropping the ebit output leaves IN-EBITS unaccounted and is caught, and filling the OPEN
energy terms with 0 makes the total computable.

**Not totalled.** Two energy terms are OPEN: reading I at A (IN-A-READ) and assembling at B (IN-B-ASSEMBLE, E_rec,
already OPEN in `seat.py`). The energy to retire A's instance is OPEN inside OUT-A-RESIDUE. No energy total is printed,
and none may be quoted. The channel is priced per schedule only (`seat.channel_floor`). Species-sequence count, 1D
one-polarisation floor:

| reading | in 1 yr | in 100 yr |
|---|---|---|
| R-CLASSICAL | 1.39e14 J | 1.39e12 J |
| R-QUANTUM | 5.55e14 J | 5.55e12 J |

There is no floor independent of the schedule. Erasure terms are floors that apply only if a record is erased; a kept
record is itself the output. These floors are B's register reset at 2.725 K (≥ 2.48e5 J, under H-RESET) and A's
record or copy at 310 K (≥ 2.82e7 J for I bits).

## Named hypotheses

H-WHICH-COUNT, H-INFO-SHAPE (M, items 1 and 5), H-SAME-COMPOSITION, H-SAME-ISOTOPES (a mass-energy difference, not
computed), H-BARYON-BY-MASS, H-RESET, H-ERASE-RECORD, and H-ONE-POSITION. H-ONE-POSITION is M's: "The two positions
technically exist as one". The board's channel reading, `transit.BEATS_LIGHT = False`, is recorded beside it and not
graded, because M has said "speed is not a question in my work".

## OPEN

1. Which count is the object's definable condition information (H-WHICH-COUNT).
2. Energy to read I at A, to retire A's instance, and to assemble at B (E_rec).
3. The D25 gate at Proxima: P is unmeasured.
4. Isotope ratios between A's object and B's stock (H-SAME-ISOTOPES).

## History

- First written expecting B's fidelity with the bits withheld to be 2/3. That is the best measure-and-prepare fidelity,
  a different quantity. The check failed, and the value is 1/2 for every state, since B holds I/2.
