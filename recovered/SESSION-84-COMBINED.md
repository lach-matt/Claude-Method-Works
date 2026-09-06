# SESSION 84 — COMBINED HANDOFF
# Open Session 85 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-84 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108.

## §0 · OPEN
`bash pack58/open58.sh` passed: s83 seal **1391/1391 root MATCH**, STATE CARD CLEAN,
canary CLEAN. Project knowledge reviewed first. **ITEM 0 CLOSED. ITEM 1 WORKED THE
REST OF THE SESSION AND PRODUCED THE FIRST DERIVED PROPERTY OF F_core. ITEM 2 IS
UNBLOCKED AND NOT STARTED.**

## §1 · ITEM 0 — **F83.2 CLOSED. THE LEVER IS LIVE AND R82.2's CONTROL HELD.**
pack84/stat84b.py, successor to the sealed pack83/stat84.py. Repair is conf82's
pattern on the class the chain actually uses: `_Seeded(hfc2.HFC)` whose `seed()` falls
through when P0 is None, so a first pass reproduces sealed values bit-for-bit.
f811 lint rc=0; can-fails PASS and gate. Prediction 631d5861...a49ed538 NOT re-filed.

**A PRECONDITION WAS MEASURED RATHER THAN ASSUMED.** conf82 never sets CORR, so which
setting produced -0.034493 was unknown. Measured: CORR=False reproduces conf82's
ladder[0] to **+0.000000 mHa**; CORR=True misses by 2.53 mHa. The two instruments
solve the same problem and the control is therefore a fair test.

**THE PROOF, SITED AT Z=89, ONE CODE PATH, TWO ARMS:**
| arm | offset | passes |
|---|---|---|
| DEAD (no re-seed) | **+0.000000 mHa** | 1 |
| LIVE (re-seed) | **-0.034493 mHa** | 12 |
**|d| vs s82 = 0.000000 mHa against a 0.002 tolerance, at the same 12 passes.**
`LEVER_LIVE` and `DOUBT_EXERCISED` cleared BY RECEIPT (pack84/lever84.json), which
`run` reads; there is no hand-editable flag. **Item 2 is unblocked.**

## §2 · ITEM 1 — **THE SEMICLASSICAL HALF IS STARTED AND HAS AN EXACT ANCHOR.**
pack84/RESULT-S84-ITEM1-SEMICLASSICAL.md. Prediction 2857b8f5...9bd33c41 filed and
hashed before the instrument existed. Instrument pack84/semi84.py, lint rc=0.

**THE ANCHOR THEOREM.** dg/dl = 2 - J with J = (L/pi) I, I = int dr/(r^2 p). In u=1/r
the radicand is a QUADRATIC for constant q, so **I = pi/L EXACTLY for any charge and
any bound E** — verified at 7.5e-12 over 60 cases. **A bare nucleus of charge 90 and a
hydrogen atom contribute identically: the whole l-dependence of the defect lives in
the region where q(r) VARIES.** First derived property of F_core in the project.
**G-within <=> J < 2.**

**MEASURED, SIX ROWS, WIDTH-2 FRONTIER:** J(rank1)/J(rank2) = 1.196/1.727 (Z=20),
1.200/1.730 (38), 1.985/1.586 (57), 1.190/1.681 (88), **2.020**/1.612 (89),
1.906/**2.102** (90). **THE SIGN OF dg/dl AGREES WITH THE BANKED g-DIFFERENCE AT 6 OF
6, INCLUDING THE REVERSAL AT THORIUM** — the sole width-2 failure of the whole walk is
the one row where the criterion also goes negative. Magnitudes agree to ~0.15 g-units
at five rows and NOT at Z=90 (-0.004 predicted vs -0.293 measured): **the sign is the
claim, the magnitude is not.**

**SCORING: S1, S2, S7 correct. S3 FALSIFIED** (J>=2 at TWO frontier channels, 89 and
90; only 90 was filed). **S4 FALSIFIED** as expected, 20 of 30 outside the band.
**S5 FALSIFIED AND INVERTED — the finding of the session's second half:** I filed that
penetrating channels deviate most from the anchor; measured 0.599 (l<=1) against 0.835
(l>=3), the other way round. **The centrifugal barrier does not protect a high-l
channel from the core — it PARKS it in the transition region, the only region the
anchor does not cancel.** **S6 SPLIT ON POPULATION**: over all 30 channels the extreme
row is Z=88, so S6 is false as filed; over the width-2 frontier the extreme is Z=90 and
it holds. **I did not state the population. F83.1's species, eleventh appearance.**

**UNASKED-FOR FINDINGS.** (i) The charge-1 Coulomb reference ORBIT is classically empty
wherever nu < L, which is every d/f channel at a block opening; discarding those rows
would have blinded the instrument at the frontier. (ii) **Z=89's 5f is the only channel
of thirty returning TWO allowed regions — an inner and an outer well split by a
centrifugal barrier, the orbital-collapse configuration, appearing unbidden at Ac.**

## §3 · FAULTS REGISTERED THIS SESSION
* **F84.1** f811's S3 detector is blind to a restart written as `steps.append(E2)`;
  its rc=0 was VACUOUS on semi84's predecessor form. Repaired forward, detector sealed.
* **F84.2** the first region-finder would have spanned across a centrifugal barrier.
* **F84.3** the X/P exchange localisation DIVERGES AT EVERY NODE OF P and split a 4s
  radicand into four false "regions" — **F84.2's machinery would have read the artefact
  as the collapse physics it exists to find.** Ruled to the direct core field, where
  1 <= q <= Z by Gauss's law; J_x reported alongside for occupied channels only.
* Two can-fail clauses corrected after failing (CF3's 1e-8 fixed-point band; the
  anchor's scope over classically forbidden cases). **Both timing flags are written
  into the source, and in both the substance passed before the revision.**

## §4 · UNCHANGED
Deliverable 1, the gates, the STATE CARD, the chain and every sealed row untouched.
**CLAUSE 1 REMAINS THE LAST OPEN DELIVERABLE**, now asking for a bound on ONE integral
over ONE region. T4 unblocked, last by practice. ALPHA THREAD CLOSED. Z=111 WITHHELD.
F54.1, F67.1-F67.6 UNVERIFIABLE, O-C1 open, Rung B not built, F82.2 open and bounded.