# RESULT S92 ITEM 1 -- S/|P| FROM THE FIELD: FIRST ORDER CARRIES THE DIRECTION, RELAXATION CARRIES THE PLATEAU
# prediction pack92/PREDICTION-S92-ITEM1-SP.md sha256 967fdfab (hashed before any solve). ruling Y (M, s92 open).
# can-fails: A lever-dead (dq=0) -> rc=4 PASS; B control-validity (D repro perturbed 0.01) -> rc=4 PASS. Both non-vacuous.
# instrument pack92/sp92.py; 4 solves per channel; rung 0 on all 40 solves; sealed D(Z*) AND D(Z*-1) reproduced 10/10 to 5 dp.

## Table. S1 = frozen-orbital Slater screening (F0 - exchange), P1 = -<1/r>_ch bare proton, frozen. (Ha)
 Z*  ch  own   S1       F0      X       S(s91)   rel      P1        P(s91)   rho_sealed rho1   rho0
 38  4d   -   0.19712  0.20527 0.00815  0.21484  -0.082  -0.14093  -0.25169   0.854    0.783  1.399
 38  5s  own  0.19798  0.19798 0.0      0.20914  -0.053  -0.22156  -0.24407   0.857    0.811  0.894
 56  5d   -   0.18385  0.19072 0.00687  0.19615  -0.063  -0.17249  -0.24960   0.786    0.737  1.066
 56  6s  own  0.17767  0.17767 0.0      0.18687  -0.049  -0.20019  -0.21640   0.864    0.821  0.888
 58  4f   -   0.40899  0.41278 0.00378  0.33652  +0.215  -1.07826  -0.59796   0.563    0.684  0.379
 58  5d  own  0.33977  0.34925 0.00948  0.29658  +0.146  -0.44703  -0.33658   0.881    1.009  0.760
 90  6d  own  0.28524  0.29327 0.00804  0.26025  +0.096  -0.36694  -0.29357   0.887    0.972  0.777
 90  5f   -   0.32967  0.33543 0.00575  0.28817  +0.144  -0.06373  -0.39360   0.732    0.838  5.173
 91  5f   -   0.36871  0.37411 0.00540  0.30362  +0.214  -0.81046  -0.47208   0.643    0.781  0.455
 91  6d  own  0.31150  0.32036 0.00886  0.27440  +0.135  -0.41314  -0.30686   0.894    1.015  0.754
 (rel = (S1-S)/S; rho1 = S1/|P|; rho0 = S1/|P1|)

## Scoring
P1 HELD 10/10: S1 > 0.
P2 HELD 5/5: rho1(own) > rho1(other) at every row (38: 0.811 > 0.783 -- the 0.003 sealed gap widens to 0.028 at first order).
P3 FALSIFIED 6/10: S1 > S only for d entrants (58,90,91). For s entrants (38,56) S1 < S: relaxation ADDS screening.
   Relaxation S - S1 is signed by the entrant's l: s entrant -> +0.009..+0.018; d entrant -> -0.025..-0.072.
P4 HELD 10/10: |rel| <= 0.215 < 0.25. The first-order term carries 78-108% of S.
P5 PLATEAU: spread FALSIFIED (0.204 > 0.05): rho1(own) splits into s-own 0.811/0.821 and d-own 0.972/1.009/1.015.
   mean 0.926 in 0.80..0.96 HELD. The sealed plateau (0.857..0.894, spread 0.037) is TIGHTER than the frozen one:
   relaxation is what makes the plateau a plateau. Value is not first order.
P6 FALSIFIED 5/10 for |P1| > |P| (held only at 58 4f, 58 5d, 90 6d, 91 5f, 91 6d). |P1_f| > |P1_d| 2/3 (fails at 90).
   Z=90 5f: P1 = -0.064 vs P = -0.394: the bare proton on the PRE-COLLAPSE 5f gives 16% of the swing; the other 84%
   is the orbital's own response -- the collapse itself. P is not first order at the f opening. (Consistent with D3.)
P7 FALSIFIED 2/5 for rho0 direction (P1 is not the carrier of P, so rho0 has no standing as a ratio);
   rho0(own) in [0.70,1.00] HELD 5/5 (0.754..0.894).
P8 HELD 10/10 rung 0, 5 dp.

## What is derived (Clause-1 residue, after this item)
 S = S1 + R_S,  S1 = F0(ch,ent) - exchange, Slater integrals of the field's own orbitals, c the only number. CLOSED FORM in the orbitals.
 The inequality S/|P|(own) > S/|P|(other) is carried by S1 alone at 5/5 rows: DIRECTION derived.
 The VALUE 0.88 is NOT carried by S1 (s-own 0.81, d-own ~1.0). It is set by R_S (orbital relaxation, signed by l_ent)
 and by the non-first-order part of P (orbital response to the proton, dominant at the f opening).
 Residue after s92: R_S = S - S1 (10 numbers, -0.072..+0.018) and R_P = P - P1 (10 numbers). Both field-computed, neither closed.
 NOT discharged. Exchange is small throughout (X/F0 <= 4%): the carrier is the direct Coulomb overlap F0.

## Faults
F92.1 detached run of row 90 died with its shell (0-byte log, no process). No data lost; rows 90, 91 re-run foreground. F53.3 recurrence.
F92.2 prediction file P5 contains a mid-line self-correction ("4 rows -- wait ... = 5"); scored on 5 own rows as the line concludes. Filed as written, hash unchanged.

## Z=90 STOP rule: sealed reproduction selected 6d (D 6d -0.19094 < 5f -0.13689). No STOP.
