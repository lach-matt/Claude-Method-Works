# PREDICTION-S103-ITEM1 -- analytic rot_k law, row 58, scored at the four <=1e-10 shells (5s, 5p, 5d, 6s).
# Filed and hashed BEFORE any arithmetic. c the only number. Core shells gated behind F102.3 (not scored).

LAW (derived, S103 open):
  Efun/pot are pairwise-symmetric in orbitals => the exact functional gradient is
      dE/dP_k = 2 q_k F_k P_k,   F_k P == (T - Z/r) P + (Vloc_k + Z/r) P - X_k(P)
  with (Vloc_k, X_k) = pot(hybrid, k) -- the SAME operator as the sealed eigen-relation.
  w102b's rot is the symmetrized two-endpoint form; the quadratic Taylor term cancels exactly
  between the Pm-forward and Pp-backward expansions. Hence, analytically:

      rot_k^AN = (q_k / dq2) * sum_{k' same l, k' != k} s_kk' * [ F(m)_{k'k} + F(p)_{k'k} ]

      F(pm)_{k'k} = <P_k'(h5) | F_k(hybrid_pm) | P_k^pm>,  hybrid_pm = h5 with shell k's orbital
      replaced by P_k^pm (occupancies fixed at h5's Q); T P_k^pm taken exactly from the h_pm
      eigen-relation (valid at valence shells; that is the <=1e-10 gate).
  Overlaps s_kk' are the sealed w102b receipt values (chord projections onto same-l h5 partners).
  Factor bookkeeping: 2 q_k F * (1/2 endpoint avg) / dq2 = (q_k/dq2)[F(m)+F(p)].

P103.1 (value-exact AND sign-exact; instrument value-exact):
  |rot_k^AN - rot_k^w102b| <= 2e-6  for k in {5s, 6s}   (cubic remainder + Hessian dq-drift bound)
  |rot_k^AN - rot_k^w102b| <= 1e-7  for k in {5p, 5d}
  sign(rot_k^AN) == sign(rot_k^w102b) at all four. Inequality direction: differences BELOW bound.

P103.2 (sign-exact): for each of the four shells, sign(rot_k^w102b) equals the sign of the single
  term s_kk' [F(m)+F(p)] belonging to the largest-|s| partner (6s->5s, 5s->6s, 5p->4p, 5d->4d).

CAN-FAIL (non-vacuous): --canfail adds +1e-5 to F(m)_{5s,6s} and F(p)_{5s,6s} (the 6s shell's
  dominant element). P103.1 at 6s must then MISS (|d| > 2e-6) -> rc=4 BREAK OK; else rc=5 VACUOUS.

Score against sealed pack102/w102b-58.json rot values only. No sealed file edited.
