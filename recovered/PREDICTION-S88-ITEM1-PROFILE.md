# PREDICTION S88 — ITEM 1 · CLAUSE 1 · THE DERIVED LOWER PROFILE phi(t)
# Filed and hashed BEFORE pack88/prof88.py exists. Field: s84's through floor87 unmodified.
# Population: the 37 s87 rows, A = nu_rank 0,1 (74 channels), 50 with K >= 1.

## DESIGN PROBES RUN BEFORE THIS FILE (declared, s85 R1449 timing discipline)
D1 Z=24: int_0^1 sigma~ dt vs K: 4p 1.13267/1.13266, 5s exact, 3d 1.2641/1.2544 (0.8%,
   t-grid interpolation of r^2 rho). => the profile is built from a SUB-CORE's q(r) by the
   SAME geometry() the measurement uses, never from a re-interpolated density.
D2 Z=24,56: q_native(unoccupied channel) = Z - direct screening(all core shells) to 1.2e-4
   (3.2e-4 at 56). Occupied l>=1 channels carry a same-shell exchange multipole (E7) of
   size 0.07 (Z=24 3d) .. 0.28 (Z=56 3d/4p) in q. So S''=r^2 rho is not exact there and the
   refusal is stated on the REMAINDER: R := S~ - Phi must be convex on the orbit
   (s85's w-grid conv_frac >= 0.999); otherwise that (channel, profile) is REFUSED.

## THE INSTRUMENT
Sub-core c: a subset of the frozen N-1 core's shells. q_c(r) = -sum_c occ Y0_c(r) (the
walk's own Y0; NO nuclear term, NO exchange). Phi(t) = 2(S_c - chord_c)/(L^2 a^2) on the
channel's ruling orbit [r_in, r_out]; beta0, beta1 its end slopes by geometry() (same call
as b0, b1). Remainder mass K' = K - (beta0+beta1), slopes b0' = b0-beta0, b1' = b1-beta1.
Extreme point: S~_max = Phi + tent(b0', b1') (s85 theorem on the remainder, convex set,
J convex in S~). J_max = J_profile(S~_max) by quadrature (s87 grid + kink refinement).
Profiles scored: P1 = innermost shell only (smallest <r>); P2 = core minus its outermost
shell (largest <r>). Ladder P_k (k innermost shells, k=1..nshell-1) reported as commentary.
Lever: scale s in phi -> s*phi: s=0 must return J_tent(b0,b1) to 1e-6 and rc_tent; the
kink-centre radicand rc(s=1) != rc(0), rc(1/2) strictly between. rc=4 if dead, every row.
Can-fails (before any row): CF1 s=0 returns tent; CF2 a phi scaled to exceed sigma~ (s=1.3
on P2) is REFUSED (remainder non-convex) at a real row; CF3 a synthetic phi that certifies
(K=1.10, phi = constant 0.30 -> equals floor87 closed form to 1e-5, NON-VACUOUS: finite,<2);
CF4 a synthetic phi that does NOT certify (K=1.40, phi const 0.30, J_max >= 2 or inf);
CF5 the prefactor is real: J_max(P2) > J_tent(b0',b1') at Z=24 3d (profile convexity costs).

## FILED PREDICTIONS
T1 theorem: J_max >= J at every non-refused (channel, profile) in A: 0 violations.
T2 lever live on all 37 rows (rc=4 never fires).
T3 refusals: P1 <= 2 of 74; P2 <= 6 of 74 (same-shell exchange rows).
T4 P1 (innermost shell): certified (K>=1, J_max<2) <= 3 of 50.
T5 P2 (core minus outermost): certified >= 30 of 50.
T6 P2 by l: p >= 22 of 30; d >= 10 of 16; f <= 2 of 4.
T7 the five J >= 2 channels: 0 of 5 certified by any profile (forced by T1).
T8 ladder monotone in k (J_max non-increasing) at >= 45 of 50 K>=1 channels.
T9 median remainder mass K' under P2 < 0.15; under P1 > 0.80.
T10 prefactor: median (J_max(P2) - J) < 0.10.

## ITEM 1b (cheap probe, both wells via semi84 I_inner)
B1 Z=55 5d: n_regions=2, outer J in [1.03,1.04], inner J > 2. B2 Z=56 5d: n_regions=1, J in
[2.43,2.45]. B3 Z=38 4d: n_regions=2, outer J in [1.00,1.02]. B4 Z=39 4d: n_regions=1 (the
4d barrier vanishes between 38 and 39, Y opens 4d at 39), J >= 2.0.