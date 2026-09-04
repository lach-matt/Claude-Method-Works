# PREDICTION-S104-ITEM3 -- perp_k by exact quartic decomposition along Dp, row 58, valence
# basis, all four <=1e-10 shells. Filed and hashed BEFORE arithmetic. c the only number.
# The ONE ruled evaluation (RULING at S104 "Continue up to T4"): closes Item 3 and, per
# SWEEP-S104-CARRIED-FAULTS, discharges F101.5.

OBJECT: Dp = D - Dr (chord component orthogonal to occupied same-l partners; Dp lies in
span{m, p, partners}, so the sealed machinery applies verbatim). Same three standard solves
(state reconstruction). Exact quartic coefficients along Dp at both endpoints, t in
{0, +-1/2, +-1}:  perp = [ (c1m+c1p)/2 + (c2m-c2p)/2 + (c3m+c3p)/2 + (c4m-c4p)/2 ] / dq2.
T1p = gradient content along the orthogonal complement -- the perturbed-HF first-order object
(Gerratt-Mills 1968 line); T2p = endpoint-Hessian difference; T3p+T4p = exact remainder.

RULE B LINE: PP.1/PP.2 value-exact at stated floating-point floors (R7); PP.3/PP.4
value-exact fractional; direction: BELOW bound (PP.4: ABOVE its floor fraction).

R7 FLOOR STATEMENT: |Efun| ~ 8.8e3 Ha; per-evaluation floor ~ 1e-12; quartic extraction
amplification ~ several x -> decomposition floor class 1e-11.

PP.1 (identity): rot + perp = chord to <= 1e-12 at all four shells (rot from the same run's
  Dr split; construction check).
PP.2 (decomposition): |total - perp| <= 2e-11 at all four shells (floor-compliant bound).
PP.3 (remainder): |T3p + T4p| <= 0.1 |perp| at all four shells -- the quartic tail is below
  10% (|Dp| exceeds |Dr|, so the 1e-7-class absolute bounds of the rot case are NOT filed;
  fractional bound only, falsifiable).
PP.4 (first-order dominance, the CPHF claim): |T1p| >= 0.8 |perp| AND sign(T1p) = sign(perp)
  at all four shells.
PP.5 (F101.5 discharge clause): PP.1 AND PP.2 holding at all four shells constitutes the
  commensurate-gauge closure -- chord = rot(derived) + perp(exactly decomposed, every term a
  stated closed-form object); the located gap of F101.5 is then the incommensurate-gauge
  artifact S102 named, and F101.5 is DISCHARGED-AS-DERIVED (ledger status on this score).

CAN-FAIL (non-vacuous): --canfail adds 1e-6 to c1m at 6s after extraction; PP.2 at 6s must
  then MISS (>2e-11) -> rc=4 BREAK OK; else rc=5 VACUOUS. Runs AFTER the primary scores HIT
  (S103 deferral precedent if primary misses).

Scored against sealed w104-58.json (chord, rot_val, perp_val) and in-run reconstruction.
No sealed file edited. All work in pack104/.
