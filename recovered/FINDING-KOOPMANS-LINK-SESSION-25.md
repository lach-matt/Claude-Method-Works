# FINDING — item (1)(c), ruling (c), s25: piecewise-linearity / Koopmans condition as next link. Derivability rule applied.
Test stated first: a link is admissible iff fixed by the functional and the state alone, computed not read, no chosen constant.
Predictions (PREDICTION-KOOPMANS-LINK-SESSION-25.md) written before the numbers.
## Result on Cs and Sc (from s24 t7c_ownshell.jsonl test D grid, same f^(1/3) interpolation as janak_table.py):
KI (Dabo et al. PRB 82, 115121 (2010), unscreened): Pi_i(f) = -int_0^f eps_i + f * int_0^1 eps_i.  E_KI(f) = E(f) + Pi(f) is linear in f
with slope DE_J and E_KI(0)=E(0), E_KI(1)=E(1).  Hence eps_KI(f) = DE_J for all f.
  Cs: DE_J -0.1450, eps_KI(f)-DE_J max|dev| 2e-16, eps_KI(1) -0.1450.   Sc: DE_J -0.3381, max|dev| 9e-16, eps_KI(1) -0.3381.
PK1 HELD (identity). PK2 HELD: resid_KI == resid_J (Cs -0.0019, Sc -0.0435); KI adds NO independent number beyond column J of
TABLE-CHAIN-15-BOTH. PK3 (structural, no run): the non-degenerate variant (KIPZ / screened alpha, Borghi et al. 2014) needs alpha; a chosen
alpha is inadmissible under the derivability rule; a linear-response alpha is the relaxed-vs-frozen split, which is item (2).
## Ruling (c) outcome: KI ADMISSIBLE under derivability, DEGENERATE with ruling (b)'s J column -> NOT a new link. FOLDED INTO item (2).
Observation only (not a prediction, not entered): bare functional's PWL deviation max|E(f) - f DE_J| = 0.0023 (Cs), 0.0090 (Sc);
Cs equals eps(1/2)-DE_J (+0.0022) as a linear eps(f) would give; Sc's eps(f) is non-linear (0.0090 vs mask 0.0170).
No constant, no measured input. Cs meas 0.14310 RECALLED-NOT-ENTERED (comparison only, unchanged from s24).