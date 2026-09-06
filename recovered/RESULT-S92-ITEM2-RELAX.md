# RESULT S92 ITEM 2 -- RELAXATION SPLIT: A 0.59 PLATEAU UNDER THE 0.88; THE LIFT IS THE CORE'S RESPONSE TO THE PROTON
# prediction pack92/PREDICTION-S92-ITEM2-RELAX.md sha256 5b216d5d (hashed first). can-fails A (dq=0) rc=4 PASS, B (+0.01 on e_rep) rc=4 PASS.
# instrument pack92/relax92.py. 20 SCF solves rung 0; frozen-field eigen-solves reproduce SCF eps to 1e-5 10/10.

## Table (Ha).  S = S1c + S_self + S_oth ;  P = P1 + P_self + P_oth ;  rho2 = (S1c+S_self)/|P1+P_self|
 Z*  ch  own   S        S1c      S_self    S_oth    |  P        P1        P_self    P_oth    | rho_sealed rho2
 38  4d   -   0.21484  0.19712  -0.00549  +0.02320 | -0.25169 -0.14093  -0.16216  +0.05141 |  0.854   0.632
 38  5s  own  0.20914  0.19798  -0.00041  +0.01157 | -0.24407 -0.22156  -0.10417  +0.08166 |  0.857   0.607
 56  5d   -   0.19615  0.18385  -0.00607  +0.01837 | -0.24960 -0.17249  -0.13639  +0.05928 |  0.786   0.576
 56  6s  own  0.18687  0.17767  -0.00099  +0.01019 | -0.21640 -0.20019  -0.08950  +0.07329 |  0.864   0.610
 58  4f   -   0.33652  0.40899  -0.00553  -0.06695 | -0.59796 -1.07826  -0.25680  +0.73710 |  0.563   0.302
 58  5d  own  0.29658  0.33977  -0.00838  -0.03481 | -0.33658 -0.44703  -0.13166  +0.24211 |  0.881   0.573
 90  6d  own  0.26025  0.28524  -0.00780  -0.01719 | -0.29357 -0.36694  -0.11509  +0.18847 |  0.887   0.576
 90  5f   -   0.28817  0.32967  -0.00919  -0.03232 | -0.39360 -0.06373  -0.25098  -0.07889 |  0.732   1.018
 91  5f   -   0.30362  0.36871  -0.00685  -0.05824 | -0.47208 -0.81046  -0.19512  +0.53351 |  0.643   0.360
 91  6d  own  0.27440  0.31150  -0.00822  -0.02888 | -0.30686 -0.41314  -0.12026  +0.22654 |  0.894   0.569
 S_c = 0 identically: the sealed field runs CORR=False (nlchain.py:17, nlguard.py:48). Item 1's S1 = S1c exactly.

## Scoring
Q1 HELD 10/10  S_self <= 0, and small: -0.0004..-0.009. The channel barely responds to the entrant.
Q2 HELD 10/10  P_self <= 0.
Q3 HELD        90 5f: |P_self|/|P| = 0.64 > 0.50. The f collapse at the opening is the channel's own wavefunction (D3).
Q4 FALSIFIED 9/10  P_oth > 0 except 90 5f (-0.079): at the collapse point the rest of the atom deepens the swing, it does not screen it.
Q5 HELD 10/10  sign(S_oth) = sign(S - S1): the l_ent-signed relaxation of item 1 is entirely the others' response.
Q6 HELD-VACUOUS  S_c = 0 by construction -> F92.3.
Q7 spread HELD (0.041 <= 0.06); mean FALSIFIED (0.587, predicted 0.84..0.92).
   rho2(own) = 0.607, 0.610, 0.573, 0.576, 0.569: a SECOND PLATEAU at 0.59, s and d alike, with only the channel relaxed.
Q8 HELD 10/10.

## What is derived
 (i) With only the channel self-consistent, one own-shell electron undoes 0.59 of a proton on the 5 own rows (spread 0.041).
 (ii) The lift 0.59 -> 0.88 is P_oth(own): the core contracts under the proton and returns 33% (38), 34% (56), 72% (58), 64% (90), 74% (91)
      of the channel's own collapse. S_oth(own) is small (+0.01 at s rows, -0.02..-0.03 at d rows).
 (iii) Two row-dependent pieces (0.59 flat; P_oth 33-74%) combine into a flat 0.88 (spread 0.037). That is a compensation the field enforces.
 Residue after s92: R = P_oth(own), 5 numbers, field-computed, not closed. rho(own) = (d eps/dN_own)/(-d eps/dZ) at full self-consistency:
 the field's own Slater-type screening constant, c the only input. NOT discharged.

## Faults
F92.3 Q6 filed as a test that could not fail (sealed field is CORR=False; should have been read before filing). SR 7b violation. Severity: hygiene; no result depends on it.
F92.1, F92.2 carried from item 1.
## Z=90 STOP: sealed reproduction 6d. No STOP.
