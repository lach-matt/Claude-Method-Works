# PREDICTION-S104-ITEM1 -- rot restated in the core-projected basis, row 58. Filed and hashed
# BEFORE any arithmetic. c the only number. Branch A of the S104 §6 fork; branch B (de-symmetrized
# M, repaired T-action) runs ONLY if PA.3 misses -- comparison then decides. If PA.3 hits there is
# no competing method and branch B is undeclared spend (prime directive).

RESTATEMENT (branch A, instrument w104.py = w102b twin):
  Basis per shell k: {P_k^-, P_k^+} UNION same-l occupied partners k' WITHIN the <=1e-10 set
  {5s, 5p, 5d, 6s} only. Core shells are excluded from BOTH the projection sum Dr and the I-matrix
  basis, so the symmetrized-M transpose halves <Pm|T|P_core> (F102.3 species, D1 mechanism) cannot
  enter F(). Everything else identical to sealed w102b: same solves (q = 0.4/0.5/0.6), same
  Taction from the eigen-relation, same four evaluation points, same rot/perp split.
  Consequence by construction (declared, NOT scored): 5p and 5d have no valence same-l partner,
  so Dr_val = 0 and rot_val = 0 exactly there; the non-vacuous content of this item is 5s and 6s.

RULE B LINE: PA.2 sign-exact; PA.3 value-exact; inequality direction: differences BELOW bound.

PA.1 (reproducibility, value-exact): retained overlaps s_kk' computed fresh must match the sealed
  w102b-58.json values |ds| <= 1e-9:  s_5s(6s) = +2.4053e-03, s_6s(5s) = -2.4032e-03.
  Chord(F) per shell must reproduce sealed chord |d| <= 1e-8 (F changes only through the basis of
  the I-quadratic; the endpoint evaluations use the same span -- m,p coords suffice for Pm, Pp).

PA.2 (sign-exact): sign(rot_val(6s)) = +, sign(rot_val(5s)) = -, matching the sealed valence law
  terms from w103a-58.json: +4.0626e-06 (6s<-5s) and -7.8432e-06 (5s<-6s). This flips the 5s sign
  relative to sealed rot_w102b(5s) = +8.019e-05 -- the D1 mechanism made falsifiable.

PA.3 (value-exact, the filed law re-scored where D1 says it holds):
  |rot_val(6s) - (+4.0626e-06)| <= 2e-6
  |rot_val(5s) - (-7.8432e-06)| <= 2e-6
  Grounds: S103-open derivation (quadratic Taylor term cancels in the symmetrized two-endpoint
  form; cubic remainder + Hessian dq-drift <= 2e-6) plus D1 valence-channel linear ratios
  0.98/1.00. The eps-nonlinearity S(1)/S(1e-3) = 0.49 observed at 6s is predicted to be core-M
  instrument content that the projection removes; if it is physical, PA.3 MISSES and branch B
  runs -- comparison decides.

PA.4 (identity, value-exact): rot_val + perp_val - chord = 0 to <= 1e-12 per shell (construction
  check on the twin's bookkeeping, 4/4).

CAN-FAIL (non-vacuous, exercises the computation path): --canfail adds 1e-5 * P_5s to Dr_val at
  the 6s shell BEFORE the four F evaluations. PA.3 at 6s must then MISS (|d| > 2e-6) -> rc=4
  BREAK OK; else rc=5 VACUOUS.

Scored against sealed pack102/w102b-58.json (chord, s) and pack103/w103a-58.json (law terms)
only. No sealed file edited. All work in pack104/.
