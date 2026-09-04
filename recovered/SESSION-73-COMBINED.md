# SESSION 73 — COMBINED HANDOFF
# Open Session 74 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-73 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108. Any claim of 119 is a boundary violation.

## §0 · FIRST ACTION IN SESSION 74
**THE FIRST ACTION IS THE OPEN, NOT THE WORK.** `bash pack58/open58.sh`.
A ruling taken before the STATE CARD is read has no standing (§H.0): recollection has no
standing, the card does. Only after seal / runtime / canary report CLEAN does work begin.
**THE SECOND ACTION IS §5, M'S OPEN RULINGS.**

## §1 · WHAT s73 DID
Opened CLEAN (files 1169/1169, root MATCH, prime CLEAN, canary CLEAN). Took three rulings
from M. Closed the CI-2x2 object: CI-2, CI-6 and CI-7 are now MEASURED, and with CI-1, CI-3,
CI-4, CI-5 from s71 **every clause of PREDICTION-CI2x2 has been scored.** Ran a fresh,
hashed, out-of-scope probe at Z=111 which FAILED its own calibration clause and was withheld
from scoring by that clause. Registered four faults, one of them the assistant's own
reporting failure. **No physics claim in any deliverable changed. Deliverable 1 is untouched.**

## §2 · M'S RULINGS, TAKEN AND FILED (pack73/RULINGS-S73.md)
**R-A** A1 KEEPS [SECONDARY]; an annotation line is added beneath it; no new label is created
and the ledger's one-label taxonomy (§H.6) is NOT modified. Applied at T4 from
pack73/AMEND-A1-LEDGER.md. The sealed ledger was not edited.
**R-B** The second Löwdin excerpt is cited to the paper WITHOUT a page. Scerri prints 334;
that is not carried. Reopens only if the 1969 original is obtained.
**R-C** CI-6 run as (a), determinant-level. (b) term-coupled was NOT authorised.

## §3 · THE RESULT WORTH THE SESSION
**CONFIGURATION MIXING IS RIGOROUSLY FORBIDDEN AT EVERY COINAGE METAL.**
At Cu 29, Ag 47, Au 79 the observed configuration d10 s1 is a closed d shell plus one s
electron, hence PURE 2S; the Madelung configuration d9 s2 has d9, which carries only 2D.
H is a scalar, so <2S|H|2D> = 0 EXACTLY. Measured at 4e-19 Ha on both fields at all three
rows, and the shared (M_L,M_S) sector is only 2 pairs wide, so there is nowhere for a nonzero
to hide. **Derived at Cu BEFORE any number (pack73/DERIVATION-CI6-SECTOR §3a), then found to
hold at Ag and Au, which that derivation did not cover.**
The ten s<->d anomalies therefore PARTITION BY ANGULAR MOMENTUM ALONE:
    ZERO      Cu 29, Ag 47, Au 79            -- forbidden, not small
    ALIVE     Cr 8.14, Nb 18.85, Mo 17.75, Ru 15.82, Rh 14.97, Pd 9.94, Pt 12.87  (mHa)
**Cu, Ag and Au are UNREACHABLE by the 2x2. That closes one candidate mechanism for three of
the Challenge's exceptions BY DERIVATION, not by bound.** Per DERIVATION §3b the same holds
at Cr for a different reason: 7S has no same-(L,S) partner in 3d4 4s2.

## §4 · SCORING — PREDICTION-CI2x2 IS NOW FULLY SCORED
  CI-1 HELD (s71) · CI-3 HELD (s71) · CI-4 HELD (s71, refined by F73.1) · CI-5 HELD (s71)
  **CI-2 HELD.** Spectator spherically averaged -> V machine zero at every row (worst
       1.7e-15 mHa). **SPEC §2(iii) SURVIVES. THE DESIGN IS NOT WITHDRAWN.** Open since s71.
  **CI-6 FAILED AS FILED** (conjunctive over Cr and Cu; Cu is zero). Clears at 7 of 10 rows.
  **CI-7 HELD** at all ten. S = I as derived, so the 2x2 is ordinary symmetric.
Instruments: pack73/ci2.py (single pair), pack73/ci2b.py (enumerates EVERY valid pair, so no
representative is chosen by hand). They agree at Cr. Can-fail passed in both directions at
both, and CAUGHT A REAL ERROR: a mis-ordered Condon-Shortley exchange factor, fixed before
any row was read.
**WHAT THIS BUYS FOR THE CRITERIA, STATED AT PROPER STRENGTH:** criterion 7 is NARROWED, not
met -- one mechanism eliminated at three exceptions is an elimination, not an explanation.
Criterion 6 is DEFENDED, not advanced: the single-determinant objection to Deliverable 1 is
answered by derivation, since V is zero at every first-entry row (occupancy) and every d<->f
tie-break row (parity). Criteria 1, 3, 5 UNTOUCHED.

## §5 · RULINGS OPEN AT THE CLOSE OF s73 — PUT THESE TO M AFTER THE OPEN
**R-D · THE ground_occ AUDIT (F73.3).** One pass classifying every ground_occ call site as
SCORE or CONSTRUCT. Bounded, finite, mechanical. Confirmed already: nlchain.py does NOT
consume it. Suspected construct-side: hfterm.py, pb4_terms.py. Run it, or defer it.
**R-E · CI-8, THE TERM-RESOLVED 2x2 (F73.2).** Diagonal and off-diagonal at the SAME
resolution on one orbital set. NOT covered by any clause of PREDICTION-CI2x2. Needs a FRESH
hashed prediction. NOT STARTED, NOT AUTHORISED.
**R-F · SCOPE, AND IT IS A SCOPE RULING NOT A PHYSICS ONE.** Clause 2 is closed: the
derivation governs the DIFFERENTIATING ELECTRON, not the total configuration. Cu/Ag/Au are
total-configuration rows and have never been inside the object being derived. s73 shows the
total-configuration object resists repair at Cu by two independent routes. **That either
vindicates the scope decision or looks like the exceptions were defined out of scope.** Both
readings fit the evidence. M rules; the assistant does not.
**R-G · CLAUSE 1.** The reverse chain from the many-electron Schrödinger equation to the field
solved. **THE ONE GENUINELY OPEN DELIVERABLE.** Nothing at s73 moved it.

## §6 · FAULTS RAISED AT s73
**F73.1 SEVERITY: RESOLUTION.** s71 scored Cu NONZERO at SHELL level; at DETERMINANT level it
  is exactly zero. A shell flag is an UPPER BOUND on where coupling can live, never a
  demonstration that it does. **STANDING: the parity rule l_A+l_B even is NECESSARY, NOT
  SUFFICIENT.** ci2a output must read PERMITTED, not NONZERO. CI-4 is NOT falsified.
**F73.2 SEVERITY: LIMIT. TOUCHES NO SCORED ROW.** The s73 2x2 has a determinant-level
  off-diagonal and an average-of-configuration diagonal. The root-shift table (and its
  apparent strong-mixing flag at Mo 42) is INDICATIVE ONLY and IS NOT SCORED. Raised BEFORE
  the table was interpreted. Requires CI-8.
**F73.3 SEVERITY: HYGIENE. TOUCHES NO SCORED ROW.** ci2b.py and rg.py called the observed
  table while CONSTRUCTING configuration A, not only while scoring. Confined to those two
  s73 files. **nlchain.py builds ref_cfg from cfg_prev and does NOT consume it. Deliverable 1
  is unaffected.** The s73 results are re-derivable from the Madelung side (B = the Madelung
  configuration, A = B with one electron promoted s->d) but were not derived that way.
**F73.4 SEVERITY: REPORTING. THE ASSISTANT'S FAULT, NOT THE PROJECT'S.** F73.3 was reported
  at foundational volume with no severity marker, and M reasonably read a code-path exposure
  as a threat to the derivation. **BINDING FROM s74: every fault carries a SEVERITY line as
  its FIRST line, and any fault not touching a scored row says so in its first sentence.**

## §7 · Z=111 — RUN, AND WITHHELD BY ITS OWN CLAUSE
PREDICTION-RG111 (sha256 20ffe3c7...d23c1a) filed and hashed before rg.py existed.
**RG-1 CALIBRATION FAILED:** the instrument gets Ag (-142.00 mHa) and Au (-68.73) right and
Cu (+2.23) WRONG. Two of three is a fail. **RG-2 LEVER PASSED** (c moved the gap 300.67 mHa).
**RG-3 and RG-4 NOT SCORED** -- withheld by RG-1's blocking clause, which was written before
any number was read precisely so this outcome could not be talked around.
**THE UNSCORED NUMBERS, RECORDED SO THEY CANNOT BE REDISCOVERED AS THOUGH EARNED:**
    Z=111  c=137.035999  E(d10s1)-E(d9s2) = +71.38 mHa   lower = d9 s2
    Z=111  c=1e6         E(d10s1)-E(d9s2) = -229.30 mHa  lower = d10 s1
They point exactly where the prediction guessed. **THAT IS NOT A RESULT.** No claim is made
that relativity breaks the group-11 pattern at Rg. **NO BULK OR CONDUCTIVITY CLAIM WAS MADE
OR MAY BE MADE:** there is no lattice, no band structure and no conductivity operator in this
project. Re-running requires an instrument that first passes RG-1 at all three rows.
**BOUNDARY, OBSERVED NOT ASSERTED:** ground_occ() is a TABLE and raises KeyError at Z=111.
The Z=2..108 seal boundary is enforced by the runtime itself.

## §8 · Cu 29 — WHY IT IS THE SHARP ROW (pack73/NOTE-WHY-COPPER.md)
MEASURED on our own field, only c entered:
    Z    el   <r_d>    <r_s>   ratio   d nodes
    29   Cu   0.9974   3.2623  0.3057     0        <- 3d is NODELESS, n-l-1 = 0
    47   Ag   1.3852   3.4530  0.4012     1
    79   Au   1.5820   3.0658  0.5160     2
   111   Rg   1.8272   2.6052  0.7014     3
**Cu is NOT unique in kind. It is the unique INTERSECTION of two conditions:** group 11
(d10 s1, giving the exact 2S/2D block) and the 3d series (nodeless, maximally compact d,
giving the largest d-d repulsion relative to the competing s). It is the only element in
either set that is in both -- and it is the only row where BOTH s73 instruments fail, and
they fail consistently (the 2.23 mHa gap matches E_B-E_A at Cu in the CI table exactly).
**A READING, NOT SCORED:** the Cu failure is most likely a MISSING-CORRELATION failure --
d10 has more d-d pairs than d9, so differential correlation favours d10 by tens of mHa,
ample to cover 2.23 mHa. **Candidate mechanism only.** Under the standing law it earns no
place in the derivation until it changes an ordering the walk gets wrong.

## §9 · CARRIED FORWARD, UNCHANGED
**pack67 and pack68 still do not exist**; F67.1-F67.6 remain UNVERIFIABLE and must not be
scored either way until s67's handoff is located. F71.1 and F72.1/F72.2 stand as recorded.
**THE ALPHA THREAD REMAINS CLOSED** (s70 §5). Not to be reopened without M's ruling.
Deliverable 1 unchanged. Gates unchanged. STATE CARD unchanged: derivation = 107 rows,
Z=2..108. **T4 (R 1701-1966) IS LAST**, and only after criterion 5 closes.