# PREDICTION S92 ITEM 1 -- DERIVE S/|P| FROM THE FIELD (ruling Y: residue = not finished)
# Filed before any solve. Instrument pack92/sp92.py. Rows 38,56,58,90,91; channels as s91 (10).
# c = 137.035999 the only number. No fitted quantity anywhere.

## Definitions (frozen-orbital, first order, built exactly as run2 builds Vloc and X)
 Orbitals: converged rung-0 solve of the SEALED state Z*, cfg(Z*-1)+ch  (has both ch and entrant).
 S1(ch;Z*)  = change of the ch one-electron energy when ONE electron is added to the entrant shell, orbitals frozen:
   ch != ent : S1 = F0(ch,ent) - 1/2 sum_k c3j0sq(l,k,l_e) G^k(ch,ent)
   ch == ent : S1 = F0(ch,ch)  - (2l+1)/(4l+1) sum_{k=2,4..2l} c3j0sq(l,k,l) F^k(ch,ch)
   (for Z*=91 the entrant occupancy step is 1->2; S1 is still the one-electron increment)
 P1(ch;Z*)  = -<1/r>_ch  on the D(Z*-1) state (Z*-1, cfg(Z*-2)+ch): one bare proton, everything frozen.
 rho1 = S1/|P|   (P sealed from pack91),   rho0 = S1/|P1|   (pure field: no computed D anywhere in it).

## Predictions (HELD/FALSIFIED each, counts out of the stated denominator)
 P1  SIGN-exact   S1 > 0 on all 10 (row,ch).
 P2  DIRECTION    rho1(own) > rho1(other) on 5/5 rows. Risk flagged: sealed gap at 38 is 0.003.
 P3  DIRECTION    S1 > S (sealed) on 10/10: frozen orbitals overestimate the screening; relaxation gives some back.
 P4  VALUE        |S1 - S| / S <= 0.25 on 10/10.
 P5  PLATEAU      rho1(own), 4 rows (38:5s, 56:6s, 90:6d, 91:6d) -- wait: own rows are 38:5s 56:6s 58:5d 90:6d 91:6d = 5.
                  rho1(own) spread (max-min) <= 0.05 over the 5 own rows; mean within 0.88 +/- 0.08.
 P6  PROTON       |P1| > |P| on 10/10 (core relaxation gives part of the bare-proton collapse back);
                  |P1_f| > |P1_d| at 58, 90, 91 (3/3).
 P7  PURE FIELD   rho0(own) > rho0(other) on 5/5 rows; rho0(own) in [0.70, 1.00] on 5/5.
 P8  REPRO        the instrument's own rung-0 solve of Z*,cfg(Z*-1)+ch reproduces sealed D(Z*) to 5 dp, 10/10.

## Can-fails (non-vacuous; F91.1 rule: no telescoping identities)
 A  lever dead: entrant increment forced to 0 -> S1 must be 0 -> rc=4.
 B  control validity: the reference solve must reproduce sealed D(Z*) to 5 dp; if it does not, rc=4.
    (B is not an identity: it compares a fresh solve against a sealed number.)

## What discharges the residue
 If P2, P5, P7 hold: the 0.88 plateau and the own>other inequality are FIELD quantities (Slater integrals of the
 field's own orbitals, c the only number). The remaining gap S - S1 is orbital relaxation, itself field-computed.
 If P4 fails (relaxation > 25%): the first-order term is not the carrier; the residue moves to relaxation and
 S92 item 2 must compute it (second solve with ent added, orbitals of ch frozen).
 Z=90 STOP rule stands: if any Z=90 solve selects 5f, stop and report.
