# PREDICTION S87 — ITEM 1b · CLAUSE 1 · THE FLOOR ON S''
# Filed and hashed BEFORE pack87/floor87.py exists. TIMING FLAG: this design follows the
# s87 Item 1 result (S7 falsified: tau3 is NOT small, the core's S'' is spread across the
# orbit). Same field, same 37 rows, same population A.

## THE DERIVATION
sigma~(t) := d^2 S~/dt^2 = 2 S''(u)/L^2 >= 0 on the orbit (Gauss). Let
    m~ := 2 S''_min / L^2,   S''_min := min over r in [r_in, r_out] of r^2 rho_r   (DERIVED, the field's own)
Then sigma~ = m~ + sigma', sigma' >= 0 with mass K' = K - m~ and first moment pinned by the
chord. By s85's theorem (J convex in delta, delta affine in S) the extreme point of the
sigma' set is a single delta: the tent of mass K'. The floor alone gives
S~_floor = -(m~/2) t (1-t) and contributes slope -+ m~/2 at each end, so

    J_max(K, m~) = J_tent(b0 - m~/2, b1 - m~/2; rescaled) / sqrt(1 - m~/2),
    radicand = (1 - m~/2) t(1-t) + S~_tent(b0', b1'),   b' = b - m~/2.

Certification: J_max < 2. A uniform floor alone RAISES J (it is convexity), so the
threshold is NOT simply K < 1 + m~/2; it is J_tent(b0', b1') < 2 sqrt(1 - m~/2),
computed numerically per channel. Lever: m~ -> 0 returns the tent (dead arm); the
measured m~ must change J_max (live arm), on every row, at the lowest-l live channel
with finite tent or on the radicand at the kink centre otherwise (F87.3 form).

## CLAUSES (population A = nu_rank 0,1, 74 channels; K>=1 subset, 50)
F1 [A,74]  closed form == direct quadrature of the composite profile at every channel
           (|diff| < 1e-5 where finite). Filed: 0 violations.
F2 [A,74]  J_max(K, m~) >= J(measured) wherever finite. Filed: 0 violations (the bound
           must hold on the real field: it is a theorem).
F3 [A,K>=1,50]  CERTIFIED by the floor (J_max < 2): filed AT LEAST 15 of 50.
F4 [A,K>=1,50]  by l: p >= 10 of 30;  d >= 3 of 16;  f >= 1 of 4 (4f orbits lie
           inside the core where r^2 rho_r is large). Filed as three sub-clauses.
F5 [A,K>=1,50]  The five J>=2 channels (Z=40 4d, 56 5d, 89 6d, 90 5f, 91 5f) are NOT
           certified (the bound cannot certify what is false). Filed: 0 of 5.
F6 [A,74]  m~ is not small: median m~ over A >= 0.05. Filed.

## CAN-FAILS
CF1 synthetic K=1.10 symmetric, m~ = 0.30: composite profile is finite and J < 2
    (certifies); m~ = 0: inf. CF2 closed form vs quadrature on the synthetic, 1e-5.
CF3 the floor moves J: m~ = 0.30 vs 0.15 differ. CF4 at K=1.40, m~=0.30 NOT certified.
