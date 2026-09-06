# BRIDGE — LOWDIN SESSION 51 · THE WALK PASSES THE BOUNDARY, AND THE COLLAPSE CONDITION ARRIVES

Open Session 52 with **`bash open49.sh`** and nothing else. Still unchanged, still needs no
successor. The only number ever entered into this chain remains **c = 137.035999**. The
−1/(2n²) introduced this session is a **denominator, not a parameter** — the Coulomb eigenvalue
at Z_eff = 1.

---

## §1 · WHAT SESSION 51 DID

Walked **Z = 109 → 120** as output beyond the evidentiary boundary, twelve steps, all six
prediction clauses held. Then, from an unsought result in those rows, **stated the collapse
condition from the field** and closed most of the one open physics object s50 left.

    DERIVATION, UNCHANGED    107 rows, Z=2..108    STEP 96/107    CONFIG 73/107
    OUTPUT, NEW              12 rows,  Z=109..120  no score, no denominator
    ORDERING CLAUSE          0 failures in 119 steps

---

## §2 · THE BEYOND-BOUNDARY WALK — SIX OF SIX

`OUTPUT-BEYOND-109-120.md`. 6d takes 109–112 and closes at 6d10; 7p takes 113–118 and closes the
period at Og; 8s opens period 8 at 119 and pairs at 120. **PB-1 through PB-6 all held with no
correction.** 5g never wins a step and never comes within 0.16 Ha of doing so.

**And the margin's mechanism got an independent confirmation.** s50 corrected s49's claim that
the margin widens with Z. It collapses from 0.26417 to **0.05809 at 113** — the step where the
competing pair changes from 6d/7p to 7p/8s — then recovers to 0.21015 by 118 and falls again at
the 8s opening. Every discontinuity is a change of adjacent pair. **The margin is a property of
which two channels compete, not of Z.** s50 read this from one event; there are now four.

---

## §3 · THE COLLAPSE CONDITION — DELIVERABLE 3

`DELIVERABLE-3-COLLAPSE-CONDITION.md`, scored against `PREDICTION-COLLAPSE-KAPPA.md`
(sha256 1c0a7d28…, filed 22:55:46Z before any κ was read).

**The unsought result.** Every g channel is pinned to exactly −1/(2n²) and does not move with Z
— 5g at 65 atoms spanning Z = 20..120, 6g at 70, 7g at 57, 8g at 28, each with total spread at
or below 1e-5. Every s, p, d and f channel in the same rows moves. **A channel that does not
respond to the nucleus is not in the field.** So:

    κ(n,ℓ,Z) = D_field / (−1/(2n²))      n* = 1/√(−2D)      uncollapsed ⟺ dn*/dZ = 0

**The field says why there is no g block.** No g channel collapses anywhere in Z ≤ 120. They are
admissible at every step and win none.

**PK-1 and PK-2 were both FALSIFIED in half, and the falsification is the finding.** Both assumed
the three tie-break failures were one phenomenon. They are two:

- **Ac(89) is the plateau case** — 5f genuinely uncollapsed, dn*/dZ = −0.0095, not in the field.
- **La(57) and Th(90) are the transit case** — n* falls 1.82 and 2.08 **in a single proton**;
  the channel is in the field but not yet at its depth.

**PK-3 held and is the load-bearing half.** The tie-break is exercised and obeyed at **94 of 107**
steps; the winning lower-n entrant has κ from 2.33 to 39.73 and **none below 2.0**. PK-4 held:
collapse is sharp, plateau spread 0.0057 (4f) and 0.0115 (5f) against a transit near 2.

**What this closes.** The tie-break clause now has a **stated, field-computed domain**: lower n
first among equal n+ℓ, *over channels whose collapse is complete*. The three failures are the
only three steps in the table where a tie-break pair becomes testable before the lower-n channel
has finished collapsing. No s, p or d pair is ever affected — only f openings have a plateau to
leave.

---

## §4 · WHAT IS STILL OWED, NAMED AND NOT GLOSSED

**κ does not separate the three failures from the 94 holds by threshold, and no claim is made
that it does.** La sits at 3.38 and Th at 6.84, both inside the holds' range. Only Ac at 1.57
falls below every hold. The separation is by **regime** — plateau, transit, complete — read from
the derivative. A cut on a value would be a fitted constant and is refused.

**The residue is therefore the TRANSIT WIDTH**: why the lag is one proton at 4f and two at 5f.
That is the gap between a condition that *identifies* the domain boundary, which this is, and
one that *derives* it, which this is not. **Strictly smaller than s50's residue, and named.**

---

## §5 · FAULTS

**F51.1 — A STRAY GATE RUN CONTAMINATED THE REPLAY LOG.** A malformed path in a pack-assembly
command re-ran gate 1 and appended it to the open log: 288 lines and 72 rc=0 against the correct
283 and 71. **Caught by diffing the log against the sealed reference before sealing, not after.**
Remedy: the contaminated log was **deleted, not truncated** — truncating a log is editing
evidence — and the full 1..71 replay re-run clean. Result 283 lines, 71 rc=0, **diff to zero
lines** against `pack50/GATES-50-OPEN.log`. Sealed as `pack51/GATES-51-OPEN.log`.

*Class: the fault is mine and it is the F43.1 class reaching the log rather than the tree — an
artefact that looked right and was not. The instrument that caught it is the pre-seal diff.*

**Two tool-call timeouts, zero rows lost, zero recomputation.** Both jobs were detached; the
receipts were read and the walk resumed at the next unreceipted unit. **Third and fourth
confirmations that the F49.2 remedy works as an instrument.** No fault registered — the directive
covered both exactly as written.

---

## §6 · GATES

Gates 1..71 replayed from a fresh extract, **diff to ZERO lines**, all rc=0, gate 6 `sec`
excluded. Six smoke gates PASS. Gate 83 PASS at its terminal restatement — cfg (73,107),
ok (96,107), cfg_first 24, ok_first 25, `str_mismatch []`. Gate 84 PASS.

**Gate 85 is NEW and locks Deliverable 3.** Twenty clauses: the four g channels' row counts,
spreads and hydrogenic identity; both f plateaus' spreads; the transit steps as exactly [57, 90];
the tie-break obeyed count 94 and failed set [57, 89, 90]; no obeyed step below κ = 2; ordering
failures empty over all 119 rows; 119 rows walked. **Can-failed in both directions** — once by
perturbing 5f at Th (transit moved to 91, gate FAILED) and once by planting a wrong expectation
— and `nlchain.jsonl` confirmed byte-identical after. `verify51.sh` Half B also can-failed.

**Three of gate 85's expectations were wrong on first write and the gate caught them.** 7g varies
in the fifth decimal, and both f plateaus sit at 3.99 not 4.00 at their last step. The
**expectations were corrected, never the data**, and the deliverable's draft phrase "flat to four
decimals" was an overclaim, corrected in place to the measured spreads.

---

## §7 · SEAL

`LOWDIN-HANDOFF-51.tar.gz`, `verify51.sh`, `MANIFEST-HANDOFF-51.txt`.
**ok=1034 bad=0 extra=0**, both halves, from a fresh extract.

pack51 ships: `gate85.py`, `nlchain.jsonl` (119 rows), `gates_run51.sh`,
`GATES-51-OPEN.log`, and the four documents of this session.

---

## §8 · ORDERED WORK LIST FOR SESSION 52

1. **`bash open49.sh`.** Expect gate 83 at (73,107)/(96,107) and **gate 85 PASS**. Add gate 85 to
   the smoke list in the next open script if one is ever written; do not rewrite `open49.sh`
   merely to add it.
2. **THE TRANSIT WIDTH — the one remaining open object on the n+ℓ path.** Why one proton at 4f
   and two at 5f. The instruments now exist: n*(Z) per channel is computable from the sealed
   chain with no new field runs, and the transit is visible as a two-regime structure. Attack it
   from the sealed data first; run new field points only if the sealed rows cannot resolve it.
3. **The g result deserves its own statement.** "No g block below Z=121 because no g channel
   collapses" is a Löwdin-relevant claim about the *shape* of the table, adjacent to
   Deliverable 2's period lengths, and it is presently buried inside Deliverable 3. Consider
   whether it is a fourth deliverable or a section of the second.
4. Deferred, and not on the n+ℓ path per M's ruling: the −8.021 mHa residue at Z=59, the coupled
   4f2·5d SO check, the promotion operator as an object. All three are the Cr(24) class.
5. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s51.
