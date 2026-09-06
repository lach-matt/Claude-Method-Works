# FINDING-CHAIN-4p (s43, item 1) — THE ROW GOES 8/8, AND argmin n FAILS AT TWO NEW ELEMENTS

## 0 · THE ROW

    Z    ent  rec   ok      D_ent     margin
    31   4p   4p   True   -0.20007   0.10012
    32   4p   4p   True   -0.25262   0.14409
    33   4p   4p   True   -0.30706   0.19108
    34   4p   4p   True   -0.36398   0.24134
    35   4p   4p   True   -0.42367   0.29494
    36   4p   4p   True   -0.48627   0.35190
    37   5s   5s   True   -0.13964   0.07991
    38   5s   5s   True   -0.17457   0.05639

**Chain 29 -> 37 steps. Chained score 27/29 -> 35/37. FIRST DIVERGENCE unchanged at 25.**
Eight steps, eight agreements with the record, no new divergence.

## 1 · THE RE-DERIVATION REPRODUCES THE DISCARDED NUMBERS EXACTLY

Z=31, 32, 33 come back at **-0.20007, -0.25262, -0.30706** — identical to the values
carried by the store discarded under M's ruling 1.

**This does not retroactively legitimate the discarded work; it is the reason the rule
exists.** It is R 1645's Lu I case exactly: the quarantined table matched the served one
234/234 and stayed in quarantine, because PROVENANCE, NOT ACCURACY, IS WHAT THE GATE
PROTECTS. A match on one re-derived row establishes nothing about the next unattested
one. The row now in the bank was walked from the sealed 29-step state, and that is why
it is in the bank.

## 2 · SCORING — 7 HELD, 1 CONSISTENT-BY-FLAG, 0 FAILED

**PC4P-1 HELD.** 4p is the entrant at all six of Z=31..36. The n+l=5 tie-break that held
10/10 across the 3d row holds 6/6 here on a DIFFERENT PAIR (4p/5s, not 4s/3d). The clause
is not a property of the pair it was found on.

**PC4P-2 HELD at 34,35,36 · CONSISTENT at 31,32,33 (timing flag).** Monotone deepening
throughout, no reversal.

**PC4P-3 HELD.** Per-proton steps: -0.05255, -0.05444, -0.05692, -0.05969, -0.06260.
Second differences -0.00189, -0.00248, -0.00277, -0.00291 — smooth and gently
accelerating, an order of magnitude inside the 0.02 bound. **Contrast with the 3d row's
+0.1285 swing in one proton against a +0.0047 drift.** No shell opens inside a p
subshell and the field says so.

**PC4P-4 HELD.** The entrant switches at exactly Z=37. Pauli-forced, as filed — this
scores the occupancy bookkeeping, not the field, and it was the weakest claim on purpose.

**PC4P-5 HELD, WITH THE STRONGER READING IN §3.** The margin collapses 0.35190 -> 0.07991
across 36 -> 37, one crossover, no other sign change in the row.

**PC4P-6 HELD EXACTLY.** 8/8 configuration, 35/37 chained, FIRST DIVERGENCE 25.

**PC4P-7 HELD.** `ok` and the configuration agree at all 8 steps. The 3d row's 4-of-10
disagreement does not recur where no element is anomalous — which localises that fault to
`rectag`'s occupancy-increase counting, exactly as s41 finding 5 said. **s42 §4(3) stays
OWED, not blocking.**

**PC4P-8 HELD.** PD-6's exception set is still **EMPTY** with the eight new steps in:
argmax|Delta| never disagrees with the entrant. Delta remains a scored column. PC3D-10's
expected first break at Z=39..41 has NOT arrived early. PD-5's 4f trace extends across
Z=31..38 at |Delta| ~ 1e-5, still HELD.

## 3 · THE ROW'S REAL RESULT — argmin n IS NOW WRONG AT FOUR ELEMENTS

`delta.py` PD-6 reports the entrant is not argmin n at **Z = [19, 20, 37, 38]**.
Z=37 and 38 are NEW, added by this row.

At Rb and Sr the field picks **5s** while the smallest available n is **4** (4d).
n+l separates them: 5s has n+l = 5, 4d has n+l = 6. **So n alone picks WRONG at Rb and
Sr and n+l picks RIGHT**, on the same field, at consecutive elements — the same shape as
the Lu finding of s35, where 5d/6s ordering was decided by relaxation and not by n.

**Four elements now carry it: K, Ca, Rb, Sr — two from each of two different rows.**
This is the walk producing direct evidence for the ORDERING VARIABLE rather than for a
particular crossover, and it is the first time the evidence has come from more than one
row. It is not yet a mechanism.

## 4 · THE NEXT ROW IS ALREADY VISIBLE IN THE MARGIN

The margin NARROWS from **0.07991 (Z=37) to 0.05639 (Z=38)** — the only place in this row
where the margin moves against the trend. The 4p row's margins widen monotonically
(0.10012 -> 0.35190); the 5s pair's narrow. **That is the 4d competition tightening as
Z=39 approaches**, where s42 measured 4d converging cleanly and unblocked (D = -0.195614).
Recorded here as a MEASURED APPROACH, not a prediction — Z=39 is not opened by this file.

## 5 · NOT DONE HERE

Z=39..48 (the 4d row, where PC3D-10 expects Delta's first break). PV-3. The nlchain
configuration column. Anything at Z >= 39.
