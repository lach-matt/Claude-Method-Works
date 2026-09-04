# PREDICTION S92 ITEM 2 -- SPLIT THE RELAXATION: WHICH RESPONSE CARRIES THE 0.88
# Filed before any solve. Instrument pack92/relax92.py. Rows 38,56,58,90,91; 10 channels as items 1/s91.
# c the only number. Every piece is a solve in the field's own potentials; nothing fitted.

## Definitions
 G = converged sealed state (Z*, cfg(Z*-1)+ch), orbitals P_G.  H = converged (Z*-1, cfg(Z*-2)+ch), orbitals P_H.
 e(ch | V) = eigenvalue of ch re-solved (one solve_one, non-self-consistent) in the FROZEN potential V of all other electrons.
 For S (entrant +1 electron, on G):
   S1c = first-order change of <ch|h|ch>, frozen, INCLUDING the frozen change of the SIC-correlation potential V_c
         (item 1's S1 omitted the V_c change; S_c := S1c - S1 is reported as its own piece).
   S_self = [e(ch | with entrant) - e(ch | without entrant)] - S1c        (ch's own orbital response)
   S_oth  = S - S1c - S_self                                              (everyone else's response, incl. total-energy vs eigenvalue)
 For P (proton +1, on H):  P1 = -<1/r>_ch (item 1);
   P_self = [e(ch | Z*, others frozen) - e(ch | Z*-1, others frozen)] - P1
   P_oth  = P - P1 - P_self
 rho2 = (S1c + S_self) / |P1 + P_self|   -- the channel's own self-consistent ratio, nothing else relaxed.

## Predictions
 Q1 SIGN   S_self <= 0 on 10/10 (variational: the re-solved orbital can only lower e).
 Q2 SIGN   P_self <= 0 on 10/10 (same).
 Q3 VALUE  at 90 5f, |P_self| / |P| > 0.50: the f collapse is the channel's OWN response, not the core's.
 Q4 SIGN   P_oth > 0 on 10/10 (the core contracts under the proton and screens ch more).
 Q5 SIGN   S_oth has the sign of S - S1 on >= 8/10: the l_ent-signed relaxation found in item 1 lives in the others.
 Q6 VALUE  |S_c| < 0.02 Ha on 10/10 (the correlation-potential piece is small).
 Q7 PLATEAU rho2(own) on the 5 own rows: spread <= 0.06 AND mean in 0.84..0.92.
          If Q7 holds the plateau is the channel's self-consistent own-screening; R_S,R_P collapse to S_oth,P_oth.
          If Q7 fails the plateau needs the others' response and the residue is S_oth/P_oth (named, field-computed).
 Q8 REPRO  e(ch | unperturbed G) = G.eps[ch] to 1e-5 on 10/10 (the frozen eigen-solve reproduces the SCF eigenvalue).

## Can-fails (non-vacuous)
 A  lever dead: dq=0 -> S1c = S_self = 0 -> rc=4.
 B  control validity: Q8 perturbed by +0.01 must be caught -> rc=4.
 Z=90 STOP rule stands.
