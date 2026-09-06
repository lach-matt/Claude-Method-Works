# FINDING — first-order spin-orbit level term: Lr I order reached, 5d edge reduced (session 19, bridge-18 s3(2), smallest scale)
Bank restore-point-2_13 (R 1700) unchanged. Findings only. Instrument t7c_so.py; gates and rows in RUN-T7C-SO-SESSION-19.txt.
## Object
zeta_nl from the converged self-consistent potential of the SR-pol TS SCF over the derived orbital, first order; level shifts +zeta*l/2 (j=l+1/2), -zeta*(l+1)/2 (j=l-1/2).
Chosen over a two-component kernel because (1') left Lr I at 0.010 Ha, and a first-order term is derivable at that scale. Predictions PL1/PL2 stated first.
## Result
Lr I: +0.010 (scalar TS) -> -0.008 with 7p1/2 (-0.035) and 6d3/2 (-0.017): PL1 HOLDS. The 7p<6d ground order of Lr I follows from the one-electron TFD-seeded
  self-consistent object with c as the only physical constant. R 1578-class boundary from session 18 is no longer a boundary; the remaining item is magnitude
  (Lr I 7p-6d gap: no measured spectrum -- Sato 2015 is IP only; null-as-gap).
5d edge: shifts -0.005/-0.007/-0.008 La/Gd/Lu (growing, toward), dev +13/13/15 % -> +11/10/11 %: PL2 HOLDS (La borderline on magnitude). NOT closed.
## Reading (after the run, flagged)
1. Every relativistic residue in the corridor now has a derived owner: 4f offset (SR), Ra II (SC-SR + TS), Lr I order (SR + TS + first-order SO).
2. The one open shell-systematic is the 5d edge, ~0.025 Ha shallow, uniform La->Lu, sign unchanged by exchange (T7b), SIC, relativity, TS or SO. It is now
   the single named obstruction to a closure statement on the corridor observables. Candidates (none opened; M ruling): (a) 5d meas is level-to-level with a
   6s^2 relaxation the neutral TS does not carry (T7b dSCF within 1.2 % of TS argues against); (b) the tail convention -q/r at charge 1 for the TS system.
3. First-order SO on the 4f rows (3b) was not run: PM1 held without it. It is the remaining derivable term for the Dy 0.017 Ha.
## Files: t7c_so.py t7c_so.jsonl RUN-T7C-SO-SESSION-19.txt FINDING-T7C-SO-SESSION-19.md