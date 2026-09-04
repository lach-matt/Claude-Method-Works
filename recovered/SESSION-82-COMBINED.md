# SESSION 82 — COMBINED HANDOFF
# Open Session 83 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-82 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108. Any claim of 119 is a boundary violation.

## §0 · OPEN
`bash pack58/open58.sh` passed: s81 seal **1354/1354 root MATCH**, canary CLEAN, STATE
CARD CLEAN. M ruled the sequence at open: **item 5, then item 4, then item 1, then 2+3.**
**ITEMS 5 AND 4 CLOSED. ITEMS 1, 2 AND 3 NOT STARTED — clause 1 is untouched and remains
the last open deliverable.** M issued **TWO RULINGS**, R82.1 and R82.2, both binding.

## §1 · ITEM 5 — R81.7 DISCHARGED. **F81.1 COST A WORD AND NOTHING ELSE.**
pack82/RESULT-S82-ITEM5-F811-PROPAGATION.md. Prediction sha 9efc9285...13c4a58d filed first.
`f811.py`, 486 .py files scanned, structural detector (re-seed + energy accumulation),
never lexical. **THE TWO CLAUSES THAT DECIDE IT BOTH RETURNED ZERO:**
**X2 one-sided termination tests = 0** tree-wide — every stationarity test reads
`abs(E2−E) < ESTAT`. On a RISING ladder a signed test would never fire or fire at pass 1,
and 7p rises; none exists. **X4 external consumers of the signed quantity = 0** — nothing
reads `drop_mHa`. **NO NUMBER ANYWHERE WAS COMPUTED FROM A MIS-SIGNED INPUT.**
**FOUR SENSES OF "LADDER", 19 FILES SAY IT, 3 MEAN IT:** S1 nlguard rung ladder · S2
nlchain restart-mode walk · **S3 restart-to-stationarity, F81.1's only object** · S4 a
radial quadrature grid in corepol, pre-s80, found by the scan.
**CORRECTED VOCABULARY, NOW LAW IN PRACTICE:** the quantity is the **RESTART OFFSET**,
SIGNED; its magnitude is a **RESOLUTION**; it is not a drop, not a descent, not a distance
to a basin floor. Demonstrated: `perturb82_vocab.py` is perturb81 with exactly the 9
flagged sites corrected, lints rc=0 where the sealed original lints rc=1.
**FORWARD GATE: `f811.py lint PATH` binds every instrument from s82 onward.**
Scored: X1 X2 X3 X4 X6 X7 correct, **X5 SPLIT** (17 sites, above my 4–12 band — I counted
code and forgot docstrings, and the docstrings are where the fault lived).
**X6 was filed as the clause I expected to lose and it held. Third session running.**

## §2 · ITEM 4 — R81.6 **NOT DISCHARGED, AND RETURNED TO M WITH THE REASON.**
pack82/RESULT-S82-ITEM4-CONVERGED-FIELD.md. Prediction sha c25baba9...9d6daf11 filed first.
`conf82.py` IMPORTS pack81/fixed81.py unmodified. Z=89 cfg88+6d converged and restarted to
stationarity (R81.2), 12 passes, E = −25694.541665071.
**A FREE DETERMINISM RECEIPT: the restart offset came back −0.034493 mHa, reproducing
F80.2's figure to six decimals in a different instrument in a different session.**
**Y1 CONTROL EXACT:** census zero = SCF's own eps(6d) = −0.176896095, **diff 0.000000 mHa**.
**THE NODE CENSUS — MONOTONE, NOTHING SKIPPED, nd CLIMBS 3 → 16.** The 4-node region spans
86 scan points and the 5-node region 66. **THE STATES ARE THERE. THE ZEROS ARE NOT.**
| ch | target nd | pts at target | zeros |
|---|---|---|---|
| 6d (control) | 3 | 372 | **1, exact** |
| 7d | 4 | **86** | **0** |
| 8d | 5 | **66** | **0** |
**ALL THREE FILED EXPLANATIONS KILLED BY MEASUREMENT.** H1 tail not −1/r: **DEAD**,
q_eff = −r·V = **1.000000** from 20 to 298 a₀. H2 grid too small: **DEAD**, r_max = **300 a₀**,
npts 4000, 6d identically zero at the edge. H3 physics terminates the ladder: **IMPOSSIBLE**,
H1 forecloses it. Scored: Y1 Y2 Y5 correct, Y6 correct in verdict/wrong in mechanism,
**Y3 and Y4 FALSIFIED — and Y4 was the clause I filed as the one with the content.**

## §3 · F82.1 AND F82.2 — TWO FAULTS, AND THEY ARE THE SAME FAULT TWICE
**F82.1 THE FAULT DETECTOR COULD NOT SEE THE FAULT. THREE DRAFTS.** Draft 1 (paren) caught
by a can-fail at rc=4. Draft 2 (claimed both operand orders, had tested one) caught by a
can-fail written to attack my own repair. **DRAFT 3 CAUGHT BY NO GATE AT ALL**: `\.P0\s*=`
cannot see a tuple-target re-seed, so perturb80 was scored as carrying no ladder while
perturb81 and fixed81 were caught INCIDENTALLY by an unrelated `.P0 = None`. **X1 read 2
instead of 3 and X4 read 1 instead of 0 — the headline wrong in both directions at once.
All five synthetic can-fails passed.** REPAIRED, and the repair is R82.1.
**F82.2 THE MATCHING CRITERION CANNOT SEE A RYDBERG CHANNEL.** f = log(nrm) crosses zero
**exactly once** in the whole l=2 channel — at 6d — and is positive and RISING at every
energy above it, +3.15 → +8.49. **Every channel shallower than the valence eigenvalue is
invisible BY CONSTRUCTION. s81's 80x widening could never have worked.** Unseen for three
sessions **because the control always passed, and the control was 6d — sited in the one
region where the instrument works.**
**SEVERITY BOUNDED AND ARGUED: no ordering, no entrant, no sealed row moves.** The hidden
channels are the LEAST bound in their ℓ; the currency is total-energy dE; a least-bound
channel cannot be an entrant at any Z. **THE FAULT HIDES EXACTLY THE STATES THAT CAN NEVER
WIN.** M's R81.6 ruling is what kept it out of the record, made before it was known.
**NINTH APPEARANCE IN FIVE SESSIONS.**

## §4 · M's TWO RULINGS — BINDING
**R82.1 · THE POSITIVE CONTROL.** Any detector that scans the corpus must include among its
can-fails at least one REAL file from the corpus whose verdict is established by inspection
and written down BEFORE the detector runs, in BOTH directions, and it GATES.
**f811 retrofitted immediately; PC1 is the very file draft 3 missed; nothing scored moved.**
**R82.2 · THE DOUBT-SITED CONTROL.** A control must be sited where the instrument is
DOUBTED, not where it is TRUSTED. Declare the domain (trusted/doubted), site a control in
the doubted region, file its expectation first, and **HALT at rc=5 if no such control can
be built — the impossibility is the finding.** A doubt-sited control MAY FAIL; that
restricts the claim rather than voiding it. **Only not looking is forbidden.**
**HARNESS `pack82/doubt82.py` BUILT AND SELF-TESTED IN FOUR DIRECTIONS, INCLUDING THE
F82.2 CASE (trusted-only → rc=5). NOT YET EXERCISED ON A PHYSICAL INSTRUMENT — s83.**

## §5 · UNCHANGED
Deliverable 1, the gates, the STATE CARD, the chain and every sealed row are untouched.
**NO PROPERTY OF F_core HAS BEEN DERIVED. CLAUSE 1 IS THE LAST OPEN DELIVERABLE AND WAS
NOT REACHED THIS SESSION.** T4 unblocked, last by practice. THE ALPHA THREAD REMAINS
CLOSED. Z=111 WITHHELD. F67.1–F67.6 remain UNVERIFIABLE. O-C1 open, floor ~0.0015 mHa.
