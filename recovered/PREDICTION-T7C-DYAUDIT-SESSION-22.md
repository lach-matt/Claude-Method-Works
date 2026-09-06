# PREDICTION — T7c-DYAUDIT (bridge-20 s3(4), ruled s22 "do first"). Written BEFORE any run.
Audit read (no run): the Hund-II bookkeeping in t7c_mult.py is internally consistent — minority channel loses the half electron
(split(): Dy 7up/2.5dn), holes (4,5)/(2,3)/(1,2)/(0,1) match 4f10/12/13/14 minority counts, particle-hole CI symmetry audited s20,
sign corr = pol + stab_n - stab_i correct, Lande level term uses J=L+S of both inverted multiplets. Only bookkeeping choice found that
is NOT forced: ONE set of F^k (from the TS half-occupied minority orbital) is used for BOTH stab_n and stab_i. The established
bookkeeping (Slater 1960; Condon-Shortley) evaluates each configuration's multiplet splitting with that configuration's own orbital.
Test: F^k from the neutral-ground 4f orbital -> stab_n; F^k from the ion (4f^{n-1}) orbital -> stab_i; TS row reproduced as gate.
Predictions (thresholds chosen before run):
 PY1  F^k ordering ion > TS > neutral on every row, spread ion/neutral 3-8 % (contraction on removal).
 PY2  Dy corr moves SHALLOWER (toward meas) by 0.004-0.012 Ha; Dy remains over-bound (|residual| > 0.005).
 PY3  Er and Tm move SHALLOWER (away from meas) by 0.002-0.008; Yb unchanged (0). Net: the change is not Dy-specific -> this
      bookkeeping is NOT the Dy anomaly; expected outcome is a bound, not a closure.
 PY4  Gate: TS-orbital F^k reproduce banked t7c_mult rows to 1e-4.
No constant, no measured input; meas rows comparison only.