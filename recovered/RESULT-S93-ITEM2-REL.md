# RESULT S93 ITEM 2 -- THE SCREENING-SIDE RELAXATION IS THE OWN-SHELL PARTNER'S RESPONSE (87-113%, 5/5); KOOPMANS IS EXACT IN THE FIELD
# prediction pack93/PREDICTION-S93-ITEM2-REL.md sha256 0840ff03 (hashed before any solve). ruling: Go (M).
# can-fails (row 38): A lever-dead (single-shell loop returns frozen P) -> Rel_c=0 -> rc=4 PASS; B control (E_frozen+1e-4) -> Koopmans check -> rc=4 PASS.
# instrument pack93/rel93.py: 6 SCF solves per row (30 total, rung 0 x30), Drep 5/5; frozen-orbital functional E[Q';P]; single-shell
# relaxation loops (all converged, dmax<2e-6). CORR=False asserted in-instrument.

## Table (Ha). Systems A=(Z*-1,cfg2) B=(Z*,cfg2) C=(Z*,cfg1); Rel = E_frozen - E_SCF; Rel_b = single-responder relaxation of shell b.
 Z* own  S-dN'    P-dZ'    Rel_c(C) Rel_c(B) Relc_diff  R1    R2     R3    R4    top(A,B,C)  Rel(A)   Rel(B)   Rel(C)   remainder
 38 5s  +0.00579 +0.00050  0.00639  0        +0.00639  1.103 -0.058 0.957 0.086  4p,4p,5s   0.00038  0.00088  0.00667  +0.00059
 56 6s  +0.00488 +0.00055  0.00551  0        +0.00551  1.131 -0.078 0.943 0.113  5p,5p,6s   0.00042  0.00097  0.00585  +0.00064
 58 5d  +0.01066 -0.00267  0.00925  0        +0.00925  0.867 +0.577 0.245 0.251  6s,6s,6s   0.02981  0.02714  0.03780  -0.00141
 90 6d  +0.00768 -0.00064  0.00853  0        +0.00853  1.111 +0.376 0.324 0.083  7s,7s,7s   0.01928  0.01864  0.02631  +0.00085
 91 6d  +0.00821 -0.00291  0.01443  0.00607  +0.00836  1.018 +0.441 0.457 0.355  7s,7s,7s   0.02631  0.02340  0.03161  +0.00015
 (R1 = Relc_diff/(S-dN'); R2 = sum_{b!=c}[Rel_b(C)-Rel_b(B)]/(S-dN'); R3 = Rel_c(C)/Rel(C); R4 = |P-dZ'|/(S-dN'); remainder = Relc_diff-(S-dN'))
## Scoring
R0 HELD 15/15: Koopmans defect K = 0 to 1e-8 on every system (the field's functional, ceff=Q-1, is exactly Koopmans); E_frozen - E_SCF
   reproduces Rel of item 1 to 1e-6 15/15; Rel >= 0 15/15; functional reproduces its own SCF E (Erep_err ~1e-8).
R1 HELD 5/5: the own-shell partner's single-responder relaxation carries 87-113% of S-dN'.
R2 FALSIFIED 4/5 (fails at 58: +0.58; 90: +0.38, 91: +0.44 are within bound, s rows ~ -0.07). At d rows the outer ns^2 response also
   grows with the partner present (6s: 0.0209 -> 0.0284 at 58). Single-shell Rel_b are NOT additive at d rows (sum 0.049 vs Rel 0.038 at 58 C).
R3 HELD 2/2 at s rows (0.96, 0.94). d rows reported: 0.25, 0.32, 0.46 -- the TOP responder at every d-row system (A, B, C) is the outermost
   s shell (6s at 58; 7s at 90, 91), 9/9, not the d partner. At s rows the top responder of A,B is the outer p shell (4p, 5p).
R4 magnitude FALSIFIED 1/5 (91: 0.355 > 0.3; others 0.08..0.25). Same top responder at A and B HELD 5/5.
R5 HELD: all single-shell loops converged; rung 0 x30; Drep 5/5.

## What is derived
 (i) Koopmans is EXACT in the sealed functional: D(c;Z,core) = eps_c[core+c] + Rel(Z,core), Rel = E[core; P_{core+c}] - E_SCF(core) >= 0,
     with no other term. Hence, exactly: S = dN' + [Rel(Z*,cfg1) - Rel(Z*,cfg2)],  P = dZ' + [Rel(Z*,cfg2) - Rel(Z*-1,cfg2)].
     The 0.88 = S/|P| is an eigenvalue ratio corrected by two relaxation-energy differences, all four terms field outputs, c the only number.
 (ii) S-dN' > 0 is the relaxation of one NAMED electron: the partner in the own shell (absent from cfg2 at 38,56,58,90; one 6d at 91).
     Its single-responder relaxation reproduces S-dN' to -13%..+13% (5/5). Remainder = non-additivity of responders (partner x outer s),
     +0.0006, +0.0006, -0.0014, +0.0009, +0.0002 Ha: <= 0.5% of S.
 (iii) P-dZ': responder set unchanged under the proton (same top responder 5/5); magnitude 8-36% of S-dN', i.e. <= 1% of |P|. Its l-sign
     (+ at s rows, - at d rows) is NOT derived (F93.2 stands). Observed: at s rows Rel grows with Z (0.0004 -> 0.0009), at d rows it
     shrinks (0.0298 -> 0.0271): the proton tightens the ns^2 pair under the d hole more than it tightens the d hole's own response.
## Residue after this item (named, Rule A): (a) non-additive responder coupling, 5 numbers |.| <= 0.0014 Ha; (b) P-dZ' sign mechanism,
##   5 numbers |.| <= 0.003 Ha. Both field-computed, both < 1% of the sealed S, P. NOT discharged.
## Faults
F93.3 SEVERITY: instrument (caught before any row was scored; no result depends on it). First build of rel93.py evaluated the single-shell
   relaxed energy with the FROZEN orbital's one-electron integral I_b, producing Rel_b < 0 (E above the frozen energy) on row 38 -- a
   variational impossibility that the R0 structural check did not cover (R0 tested the frozen functional only). Fixed: I_b recomputed from the
   re-solved orbital's eigenvalue. Species: reading a label (I_b) for a different object (the new orbital). Row 38 re-run; can-fails re-run.
F93.2 carried (sign of P-dZ' still underived). F93.1 carried.
## Z=90 STOP: sealed reproduction 6d. No STOP.