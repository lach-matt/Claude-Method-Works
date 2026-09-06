# PREDICTION S87 — ITEM 1 · CLAUSE 1 · THE KINETIC CAP ON S''
# Filed and hashed BEFORE pack87/semi87.py exists. Field: s84's through semi85 unmodified.
# c = 137.035999 remains the only number ever entered. Nothing sealed is edited.

## THE DERIVATION (what the instrument will measure, stated before it runs)

In u = 1/r, S(u) = u Q(u), S'(u) = w = q - r q', and for the direct frozen-core field
(Gauss, F84.3):  q'' = 4 pi r rho, hence

    S''(u) = r^3 q'' = 4 pi r^4 rho(r) = r^2 * rho_r(r),   rho_r := 4 pi r^2 rho = sum_i occ_i P_i^2.

**Correction to s86 §3, entered here:** a kink in S is a DELTA in S'', i.e. a delta-shell
in rho, not a step in rho_r. A step in rho_r is a kink in S', which is a jump in S'' —
admissible to a sup-bound. The excluding language for the kink is therefore any
bound on sup S''; H^1 supplies one, and it is derived as follows.

For each core orbital, P(0) = 0 and P in L^2 with ||P||_2 = 1, so for every r
    P(r)^2 = int_0^r 2 P P' <= 2 ||P||_{[0,r]} ||P'||_{[0,r]},
    P(r)^2 = -int_r^inf 2 P P' <= 2 ||P||_{[r,inf)} ||P'||_{[r,inf)},
and adding, by Cauchy-Schwarz on the two halves,  **sup P^2 <= ||P'||_2 = sqrt(2 T_i^rad)**,
where T_i^rad = (1/2) int P'^2 dr <= T_i (the centrifugal term is dropped). Therefore

    M_r2 := sum_i occ_i sqrt(2 T_i)                 (per-orbital gradient norms)
    M_r1 := sqrt(2 N_core T_core)  >= M_r2          (Cauchy-Schwarz again; one number)
    sup_r rho_r <= M_r2 <= M_r1.

On the orbit r in [r_in, r_out],  S'' <= r^2 rho_r <= r_out^2 M_r  =: M_u.  Three caps,
nested, all produced by the field and none entered:
    M_u1 = r_out^2 M_r1   (total core kinetic energy, one number)
    M_u2 = r_out^2 M_r2   (per-orbital gradient norms)
    M_u3 = sup_{orbit} r^2 rho_r   — NOT a bound from T but the CEILING of the
                                     sup-language: the best any sup-type cap can do.
The admissible set becomes {S convex, 0 <= S'' <= M, endpoint slopes and chord given}.
With the cap, the extreme point is no longer a tent: with sigma = S'' in [0, M] and the
two linear constraints (mass V+ = int sigma, chord = first moment), the extreme sigma are
bang-bang. The candidate extreme is the single RAMP sigma = M on an interval of width
Delta_u = V+/M whose position is pinned by the chord. Dimensionless: tau := Delta_u/a
= K L^2 / (2 M_u). As M -> inf, tau -> 0 and the ramp -> the tent. J_max(K, M) is J
of the ramp profile, computed by quadrature of 1/sqrt(t(1-t) - delta_ramp(t)); it is
finite wherever the radicand stays positive, and it CERTIFIES a channel when J_max < 2.
The single-ramp extremal claim is checked (not proved) against random bang-bang
profiles at CF5; if any random profile beats the ramp, S2-S6 are scored on the
max over profiles and the ramp claim is registered as a fault.

## POPULATION (F83.1, fifteenth appearance): A = width-2 frontier, 74 channels, 37 rows,
## the rows of semi86-out.json. K >= 1 subset: 50 channels.

## CLAUSES

S1  [A, 74]  THEOREM CHECK. sup_{orbit} S'' <= M_u2 <= M_u1 at every channel.
    Statistic: violations. Filed: 0 of 74.
S2  [A, 74]  NESTING. J_max(K,M_u1) >= J_max(K,M_u2) >= J_max(K,M_u3) >= J(measured)
    at every channel where J_max is finite; and J_max(K, M=inf) = J_tent to 1e-6.
    Filed: 0 violations.
S3  [A, K>=1, 50]  THE BOUND FROM T CERTIFIES ALMOST NOTHING. Channels with
    J_max(K, M_u2) < 2. Filed: at most 2 of 50. Expected 0. Mechanism: tau is of order
    1e-3 — the cap is a global sup over r <= r_out while the orbit lives where the core
    density is small; the ramp is indistinguishable from the tent.
S4  [A, K>=1, 50]  THE CEILING OF THE SUP-LANGUAGE. Channels with J_max(K, M_u3) < 2.
    Filed: at most 5 of 50, all of them p channels with K < 1.10. Expected ~0-3.
S5  [A, K>=1, 50]  No d or f channel (K >= 1.20) is certified even by M_u3: 0 of 22.
S6  [A, 74]  WHERE THE LOSS IS. median(M_u2 / M_u3) > 10 and median(M_u1 / M_u2) < 3:
    the loss is in the LOCALISATION (a global sup against an orbit-local one), not in
    the inequality sup P^2 <= ||P'||.
S7  [A, 74]  The measured concentration tau_3 = K L^2 / (2 M_u3) is below 0.10 at
    every channel: the real core's S'' on the orbit is already far from a delta, so
    the kink is excluded by a wide margin — and J still reaches 2. Filed: max tau_3 < 0.10.

## CAN-FAILS (must pass and gate; a failure halts)
CF1 smooth synthetic core (hydrogenic 1s,2s,2p, Z=10): sup rho_r <= M_r2 — ADMITTED.
CF2 step core (P with a jump): discretised ||P'||^2 grows by >= x4 when the grid is
    refined x4 — it has NO finite M and is EXCLUDED from the H^1 set (the step is
    not a member; the cap cannot be formed for it).
CF3 delta-shell core (narrow Gaussian, width eps): sup rho_r > M_r2 of the SAME
    mass smooth core by >= x10 — the shell is what the cap excludes.
CF4 ramp limits: J_max -> J_tent as M -> inf (|diff| < 1e-6 at M = 1e9) and -> 1 as V+ -> 0.
CF5 extremality: on a synthetic channel with K = 1.1, tau = 0.05, 200 random
    bang-bang sigma (1-3 intervals, same mass and chord) never exceed J_ramp.
CF6 lever: on the synthetic channel, halving M strictly lowers J_max; M -> inf returns the
    tent. On every real row, the lever is M_u2 -> inf (dead arm = tent) against M_u2
    (live arm); the live arm must differ from the dead arm at the lowest-l live
    channel — the F86.2 siting. Halt rc=4 otherwise.
CF0 orbital normalisation: every frozen P_nl has int P^2 dr = 1 to 1e-6, and
    sum cQ = Z - 1.

## SCORING. Statistic and population stated per clause (F86.1). Timing flags in source.
