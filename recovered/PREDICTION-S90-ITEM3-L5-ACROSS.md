# PREDICTION S90 ITEM 3 (L5 read) -- s-below-d across the d collapse. NO NEW RUNS: sealed ladder only.
# Filing line (Rule B): establishes eps(ns) < eps((n-1)d), i.e. nu_d - nu_s > 0 (upper bound on
# g(d)-g(s) via identity g(d)-g(s) = 1 - (nu_d - nu_s)); VALUE-exact (eigenvalues from disk).
Series: (5s,4d) Z=33..40 and (6s,5d) Z=51..58, from rt/nlchain.jsonl 'order' D values.
P1 The d channel shows a D3-type collapse: |dn*/dZ| < 0.05 on a plateau for >= 2 rows before a
   single-proton transit with |dn*/dZ| > 0.8, at 37->38 (4d) and 55->56 (5d).
P2 The s channel has NO transit: |dn*_s/dZ| < 0.3 at every step in both series.
P3 nu_d - nu_s > 0 at every Z in both series where both are bound (the across clause holds
   throughout, not only at the frontier rows). Minimum margin is at Z=56 and is 0.274.
P4 MECHANISM: the collapse of the d moves nu_d DOWN toward nu_s, and the margin after the
   transit is set by the s's own penetration: at the post-transit row, n*_s < n*_d - 0.2.
   CAN-FAIL: a row in either series where nu_d - nu_s < 0 (s above d) -- the clause would be
   violated by the field and D1 would already carry it; or P1 with no transit found.