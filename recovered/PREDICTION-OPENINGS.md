# PREDICTION-OPENINGS (s47) — FILED BEFORE nlchain IS POINTED AT Z=57

Binding under PARTS-OF-THE-LAW §4(b) and R 1449. Owed since s45. Nothing below is read from
any run past Z=56. Every figure is DERIVED from sealed `nlchain.jsonl` (55 rows,
md5 97ac1c0d67c0) or RECALLED-NOT-ENTERED from the record and flagged as such.

Distinct from PREDICTION-4f-COLLAPSE, which predicts the 4f CHANNEL's behaviour. This file
predicts THE OPENINGS — Part 3 of the law, the order itself where a block opens. The two
files can fail independently and are scored separately.

## 0 · WHAT PART 3 IS, AND WHY IT IS NOT A SUBCASE

Falsified by: **the rule naming the wrong channel for the entrant at a block boundary.**
Read from the record's 19 subshell openings, 17 agree and two do not — **La(57) opens 5d
where n+ℓ says 4f; Ac(89) opens 6d where n+ℓ says 5f** (RECALLED-NOT-ENTERED).

At Cr(24) the rule names the right channel and the wrong atom: part 2, and part 1 passes.
At La(57) the rule names the **wrong channel**. Part 1 is what fails there, so part 1 cannot
absorb it, and no already-placed electron moves, so part 2 cannot. **La and Ac are the only
two elements in the table where the step column can fail for a reason that is not a
promotion.** That is why this file exists and why it is filed before the run.

## 1 · THE INSTRUMENT THIS IS PREDICTED ON — STATED, BECAUSE IT CHANGED TODAY

Z=57 will be run through the **guard** (nlguard.py, gate 84, adopted this session). Rung 0 is
the ruling field unchanged (β=0.4, maxit=100) and is tried first, so a converging channel
returns exactly what the unguarded instrument would have returned. Two consequences are
declared BEFORE the run rather than explained after it:

(i) A channel that cycles at rung 0 will now be **repaired at rung 1**, not silently returned.
    If any Z=57 channel takes rung 1, its D carries F47.3's ~1e-5 mixed-rung uncertainty in
    the last stored digit. **This cannot change an ordering** — margins here are 1e-2 to 1e-1,
    four orders larger — and if it ever appeared to, that is a finding against the guard.
(ii) A channel that cycles at EVERY rung returns **no number** and joins `fail`. It is then
    absent from `order`, exactly as a node-count failure is. **A channel absent from the
    ordering has not been shown to be unbound**; it has been shown to be unsolved. No claim
    below may be scored off an absence.

## 2 · THE BASELINE, DERIVED FROM SEALED ROWS

The two contenders at Z=57 carry n+ℓ = 7 together with 6p. Their sealed track:

    Z    4f        5d        6p        6s
    52   -0.03128  -0.06111  -0.07617  -0.11309
    53   -0.03128  -0.06233  -0.07922  -0.11833
    54   -0.03128  -0.06350  (+0.11105 -> -0.08192 repaired, F46.1)  -0.12321
    55   -0.03127  -0.06473  (FAIL: nodes 3)  -0.12779
    56   -0.03136  -0.11818  -0.10907  -0.15732

**5d nearly doubled in depth across one proton at Ba(56)** — a drop of 0.053 Ha where the
preceding step gave 0.001. That is s46's finding (4), and it was RE-TESTED this session and
survives: −0.11818 at both β=0.4 (35 it) and β=0.2 (74 it), identical to five decimals. It is
not an instrument artefact. **4f meanwhile moved 1.4e-3 across 55→56 — small absolutely, but
4.5× the largest step in the sixteen-element flat baseline. The flatness ends at Ba.**

## 3 · THE CLAIMS

**PO-1 — THE FIELD OPENS 5d AT La(57). ent = 5d, ok(57) = True.**
Basis: 5d enters Z=57 at −0.11818 against 4f's −0.03136, a gap of **0.087 Ha**, and 5d is
deepening while 4f is nearly flat. For 4f to take the step it must close 0.087 Ha in one
proton having moved 1.4e-3 in the last one. Predicted **D_5d(57) in [−0.20, −0.12]** — deeper
than Ba's, and the band is set wide-below because the Ba step was itself discontinuous and a
second discontinuous step cannot be excluded. **This band is a genuine prediction and can be
wrong on its own while PO-1's clause holds; score clause and band separately** (s46 logged
PC4F-3's band wrong ahead of its step and that discipline is kept here).

**PO-2 — THE n+ℓ RULE NAMES 4f AT La(57) AND IS THEREFORE WRONG THERE.**
4f and 5d both carry n+ℓ = 7; clause 2 (smaller n first) names 4f; the record opens 5d.
**Predicted: rule WRONG, field RIGHT, at the same step.** This is Part 3's first and sharpest
test and the first of the record's two disagreeing openings.

**PO-3 — 6p DOES NOT TAKE THE STEP AND DOES NOT DISPLACE 5d.**
6p also carries n+ℓ = 7 and F46.1 made it a live candidate. Now closed: repaired to −0.08192
at 54 and converged at −0.10907 at 56, both above 5d's −0.11818. Predicted D_6p(57) in
**[−0.16, −0.10]**, and predicted **not** the entrant. Falsified if 6p wins the ordering.

**PO-4 — THE OPENING IS NOT REPRODUCED BY A GRADUAL 4f DESCENT.**
Predicted D_4f(57) in **[−0.045, −0.031]** — 4f moves, but stays above 5d by a wide margin.
Falsified if 4f arrives within 0.02 Ha of 5d at 57, which would make La a near-tie the field
wins narrowly rather than a channel the field never considered.

**PO-5 — THE MECHANISM IS COLLAPSE, AND IT IS ALREADY LOCATED ON 5d, NOT ON 4f.**
The Janet boundary at Z = 21, 57, 89 is not sharp; collapse is rapid, not instantaneous.
Sourced: Goeppert-Mayer, Phys. Rev. 60 (1941) 184–187; Griffin, Andrew & Cowan, Phys. Rev.
177 (1969) 62–71. Already in the chain, not imported for this. **Predicted: the discontinuity
that opens the 5d block is the one ALREADY OBSERVED at Ba(56), one step early — so the
opening at La is the completion of a transfer that began at 56, not an event at 57.**
Falsified if 5d's 56→57 step returns to the ~0.001/proton régime, which would make Ba's jump
an isolated excursion rather than the onset of a transfer.

**PO-6 — DERIVED, NOT FITTED (§4a).** No correction is applied at 57 because 57 is where the
rule breaks. Nothing in §3 introduces a constant, a threshold, or a placement sweep. The only
number entered anywhere in this chain remains **c = 137.035999**. Falsified by any clause
above requiring a parameter chosen at or near Z=57.

## 4 · WHAT IS NOT PREDICTED, DECLARED

Whether cfg_ok holds at 57 (the record carries 5d1 6s2 and a walk with no promotion operator
may or may not reproduce it — that is part 2's business). Which channels fail to converge or
fail on node count at 57. Iteration counts, rungs, `sec`. The exact D of any channel outside
the stated bands. **Whether the merge of parts 2 and 3 is decided by this step — it is not;
that needs Ac(89).**

## 5 · THE SCORING RULE, FIXED IN ADVANCE

PO-1's clause, PO-2, PO-3's clause and PO-5 are scored on Z=57 alone. PO-1's band, PO-3's band
and PO-4's band are scored separately and a band failing does not carry its clause down.
A channel that returns no number is scored NEITHER pass NOR fail: it is recorded as unsolved,
per §1(ii). **PREDICTION-OPENINGS must be filed again before Z=89, and this file does not
cover Ac.**
