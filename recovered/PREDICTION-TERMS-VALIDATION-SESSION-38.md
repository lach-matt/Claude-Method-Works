# PREDICTION-TERMS-VALIDATION (s38, item 1) — WRITTEN BEFORE ANY CODE READ, CHANGE OR RUN (R 1449).
Successor to PREDICTION-TERMS (s37), which stated the mechanism and PT-1..5. This file states the DESIGN DECISIONS (i)(ii)(iii) as DETERMINED BY THE ROWS
(M's ruling, s38: "these can be determined by studying the other rows; each row has its own definable characteristics") and the tests that determine them.

## 0 · Row classes — read from ground.expand / t5_scf.ground_occ, s38, no measured input
A  Sc(21) Y(39) La(57) Lu(71) Ac(89)   neutral d^1 s^2 ; d-removed ion CLOSED (no open shell) ; s-removed ion d^1 s^1
B  Hf(72) Th(90) Rf(104)               neutral d^2 s^2 ; d-removed ion d^1 ; s-removed ion d^2 s^1
C  Ce(58) Gd(64) Pa(91) U(92) Cm(96)   neutral f^n d^1 s^2 ; d-removed ion f^n ; s-removed ion f^n d^1 s^1
FORCED (zero arrangement freedom): all of A (closed / two singly-occupied shells), Ce f^1, Gd f^7 and Cm f^7 (half-filled, ^8S), every d^1 ion.
FREE: Hf Th Rf (d^2), Pa (f^2), U (f^3).
STRUCTURAL POINT: Th is class B and Ac is class A. The d-side term is present at Th by configuration and EXACTLY ZERO at Ac by configuration.
This is the only row-differential object on the pair and it is not fitted.

## 1 · Design decisions, determined not chosen
(i)   Ground arrangement COMPUTED by the Slater-Condon machinery on all 13 rows. The record's term label is a COMPARISON COLUMN, RECALLED-NOT-ENTERED,
      never an input. Validation set = the FORCED rows, where the record cannot be anything else.
(ii)  FROZEN average-of-configuration SR HF orbitals (nlwalk_hf field) for the term integrals; frozen-minus-relaxed MEASURED on all rows carrying a term
      and tested for class-flatness with the s37 seam instrument. The test adopts or rejects the convention; it is not asserted.
(iii) LS terms only in the term column; zeta computed PER ROW as a SEPARATE column (t7c_so machinery) in the same session, so that SO is measured rather
      than assumed away. SO is itself row-differential (grows with Z) and therefore a live competitor for the Th/Ac residual until separated.

## 2 · Predictions (falsifiable; failure is logged, not suppressed)
PV-1 (i, machinery validation). On the FORCED rows the computed lowest arrangement reproduces the record's ground term on 9 of 9. A miss at ANY forced row is
     a MACHINERY FAULT, not physics: the run HALTS, the fault is registered, and NO Th/Ac number is read from that state.
PV-2 (ii, the zero rows). Frozen term energy of the d-removed ion on class A = 0 exactly. |T| > 1e-6 Ha there is a machinery fault (closed shell has no
     open-shell integral). Frozen and relaxed must agree identically on those five d-side removals.
PV-3 (ii, flatness). Frozen-minus-relaxed term difference is CLASS-FLAT: spread <= 0.005 Ha across the 8 rows carrying a term, <= 0.002 Ha within class B.
     If flat -> frozen adopted, difference registered as a seam with a stated bound. IF ITS ROW-DEPENDENCE EXCEEDS THE Th/Ac SPLIT (0.016 Ha) the relaxation
     object competes with terms and the residual DOES NOT CLOSE this session — a real outcome, not a design failure.
PV-4 (the object; PT-1 restated on the class reading). Th: d^2 Hund-I term lost on d removal, 0.020-0.040 Ha; gap moves from +0.008 to <= -0.010 (s-first, HELD).
     Ac: d-side term exactly 0; only the s-removed ion (d^1 s^1 triplet) gains a term <= 0.010 Ha; gap moves +0.003..+0.008, STAYS d-first.
     Term-induced Th/Ac split >= 0.020 Ha against the 0.016 Ha residual to be explained.
PV-5 (iii, SO separation). zeta(6d) at Ac and Th differ by < 10% (adjacent Z, same channel), so SO contributes < 0.003 Ha of row-differential across the pair —
     an order below the residual. IF SO REACHES THE RESIDUAL, terms are not the mechanism and the attribution reopens.
PV-6 (whole table; PT-4 restated). On HF+terms (no corr) the boundary sits at 0 within +-0.010 on >= 12/13 rows. Hf is the row at risk (PT-3): +0.028 minus a
     d^2 term of 0.02-0.035 lands within +-0.01 of zero. Rf stays d-first. Pa/U decrease by <= 0.02, stay d-first. Cm stays d-first. Y unchanged (no term).
PV-7 (row-differentiality, the claim being tested). The term correction is NOT class-flat — range 0.00 (class A d-side) to 0.04 (class B) — and would be the
     FIRST row-differential term measured on the pair. A class-flat outcome falsifies terms as the residual's home.

## 3 · Held / not in this run
No correlation in the term column (PT-5: corr x terms is item 2, comparison decides after). No constant beyond c. No scans. No threshold chosen.
SUBCELL=1; HF maxit 100; grid/tolerance as inherited (CHOSEN, §H.6). T4 LAST.
