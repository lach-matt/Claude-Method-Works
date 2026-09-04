# RESULT S82 — ITEM 5. R81.7: F81.1 PROPAGATED.
# **F81.1 IS A NAMING FAULT AND NOT A NUMERICAL ONE. ZERO ONE-SIDED TERMINATION TESTS
# EXIST ANYWHERE IN THE TREE, AND NO NUMBER ANYWHERE WAS COMPUTED FROM A MIS-SIGNED
# INPUT.** The word travelled; the arithmetic did not.
# Prediction sha256 9efc9285133a9e5a5d3e31c47fd6338b091903bd0f7744297f68677c13c4a58d, filed first.
# Instrument pack82/f811.py. 486 .py files scanned. NO SEALED FILE EDITED.

## THE CAN-FAILS, RUN FIRST AND GATING — FIVE, ALL PASSED, TWO WRITTEN AFTER A FAILURE
| id | synthetic input | required verdict | got |
|---|---|---|---|
| CF1 | one-sided break, `float(E2) - E < eps` | S3, 1 offence | PASS |
| CF2 | magnitude break, `abs(E2 - E) < eps` | S3, 0 offences | PASS |
| CF4 | reversed operands, `E - float(E2) > -eps` | S3, 1 offence | PASS |
| CF5 | tuple-target re-seed as the SOLE re-seed | S3 detected | PASS |
| CF3 | the WORD only, sense S1 rung ladder | NOT S3 | PASS |
**CF1 FAILED ON ITS FIRST FIRING AND HALTED THE RUN AT rc=4. CF4 FALSIFIED THE REPAIR
THAT FOLLOWED. See F82.1.**

## THE FOUR SENSES — THE WORD TRAVELLED FURTHER THAN THE OBJECT
Scope was decided STRUCTURALLY (re-seed from own orbitals + accumulation of successive
total energies), never lexically. The word was measured separately, and that measurement
is the finding:
| sense | object | files |
|---|---|---|
| **S1** | `nlguard.LADDER` — the convergence RUNG ladder (β, maxit) | nlguard, nlchain, gate90, f543, tbstep, l2fin, de80, de81 |
| **S2** | `nlchain restart` — walk reference = OBSERVED cfg(Z−1) | cinf, cinf2, gate87 |
| **S3** | **restart-to-stationarity — F81.1's ONLY object** | **perturb80, perturb81, fixed81** |
| **S4** | a coarse **r_e quadrature grid** | corepol (pack29 and rt) |
**19 FILES SAY "LADDER". THREE MEAN F81.1's LADDER. THE OVER-MATCH IS 16.** S4 is
pre-s80 and was found by the scan, not by recollection.

## THE SCORED SCAN
| clause | measured |
|---|---|
| **X1** S3 files, tree-wide | **3** — perturb80, perturb81, fixed81. **pre-s80: ZERO** |
| **X2** one-sided termination tests | **0** tree-wide |
| **X3** naive `ladder` files / over-match | **19 / 16** |
| **X4** external consumers of the signed quantity | **0** |
| **X5** naming sites inside the 3 S3 files | **17** (perturb81 9 · fixed81 5 · perturb80 3) |
| **X6** a fourth sense in pack5..pack74 | **YES — S4, corepol, pack29** |
| **X7** lint fails sealed / passes corrected | **rc=1 (9 sites) / rc=0** |

## WHAT THIS SETTLES, AND IT IS THE POINT OF THE ITEM
**X2 IS THE CLAUSE WITH TEETH AND IT RETURNED ZERO.** Every stationarity test in the
project reads `abs(E2 − E) < ESTAT`. A one-sided test would either never fire or fire at
pass 1 on a RISING ladder, and 7p rises — so had one existed, F80.2's number, F80.3's
floor and every re-label built on them would have been computed on a truncated ladder.
None exists.
**X4 RETURNED ZERO CONSUMERS.** The signed quantity `drop_mHa` is written to receipts by
the three S3 files and read by nothing. **No downstream number was computed from it.**
**THEREFORE: F81.1 COST A WORD AND NOTHING ELSE.** That is the fullest statement the
evidence supports, and it is a weaker fault than F79.2 (units) or F80.1 (which zero).
It is not thereby harmless: the word "basin floor" was carried into F80.2's conclusion
and would have been carried into Deliverable 1's language had s81 not measured 7p.

## THE CORRECTED VOCABULARY — THIS IS THE REPAIR R81.7 ASKS FOR
> The quantity is the **RESTART OFFSET**, and it is **SIGNED**.
> Its **magnitude** is a **RESOLUTION**.
> It is **not** a drop, **not** a descent, and **not** a distance to a basin floor.
Demonstrated, not asserted: `pack82/perturb82_vocab.py` is perturb81 with the vocabulary
corrected — **9 lines changed, exactly the 9 flagged sites** — and it lints rc=0 where
the sealed original lints rc=1.

## THE FORWARD GATE
`python3 pack82/f811.py lint PATH` halts (rc=1) on any file that BOTH carries an S3
ladder AND either tests stationarity one-sidedly or names the signed offset as a
direction. **EVERY INSTRUMENT WRITTEN FROM s82 ONWARD IS LINTED BEFORE IT IS RUN.**
This is what makes R81.7's "no instrument may assume a sign" enforceable rather than
remembered.

## PREDICTION SCORED — X1 X2 X3 X4 X6 X7 CORRECT, **X5 SPLIT**
  X1 exactly three, none pre-s80 . . **CORRECT.** The named risk — eigen_fix, rung597,
     early hfc2 — did not materialise; none re-seeds from its own converged orbitals.
     **Correct only after two repairs to the detector (F82.1).**
  X2 zero one-sided tests . . **CORRECT**, and it is the clause that mattered.
  X3 naive over-match ≥ 5 files . . **CORRECT**, 16.
  X4 zero external consumers; naming only . . **CORRECT.**
  X5 four to twelve naming sites . . **SPLIT. The floor holds and the BAND IS WRONG:
     17, above the predicted ceiling.** The filed estimate counted the code sites and
     not the docstrings, and the docstrings are where "still-descending" and "basin
     floor" actually live — which is precisely where F81.1 did its damage. **I
     under-counted the surface of the fault I was measuring.**
  X6 a fourth sense exists . . **CORRECT — filed as the clause I expected to lose.**
     `corepol`'s r_e quadrature ladder, pre-s80. **THIRD SESSION RUNNING THAT THE
     LEAST-TRUSTED CLAUSE SURVIVED.** That pattern is now itself worth registering.
  X7 both lint directions . . **CORRECT**, demonstrated.

## RECORDED AGAINST THIS RESULT, NOT BURIED
1. **THE DETECTOR WAS WRONG TWICE AND THE SECOND TIME NO GATE CAUGHT IT.** See F82.1.
   The can-fail suite as first written would have accepted a scan that missed
   perturb80 entirely and mislabelled it an external consumer.
2. **A STRUCTURAL DETECTOR IS STILL A PATTERN.** X1's "zero pre-s80" is a statement
   about files matching `.P0`-style re-seed plus energy accumulation. An early instrument
   that restarts a solve by an entirely different mechanism is outside this scan by
   construction. **The claim is "none found by this detector", not "none exists."**
3. **THE SEALED FILES ARE UNCHANGED.** perturb80, perturb81 and fixed81 still carry all
   17 naming sites. They are RECORDED here, not patched. Any future reader of those
   receipts must read `drop_mHa` as a SIGNED OFFSET.
4. **THIS DERIVES NOTHING.** It repairs a vocabulary and installs a gate. Clause 1 is
   untouched by it, and O-C1, F54.1 and F67.1-F67.6 are untouched by it.
5. **F81.1 IS NOW DISCHARGED BY PROPAGATION**, on the evidence above, and the discharge
   rests on X2 and X4 both returning zero. If either is later shown non-zero by a better
   detector, the discharge is withdrawn.
