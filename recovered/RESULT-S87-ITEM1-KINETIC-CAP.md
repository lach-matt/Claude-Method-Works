# RESULT S87 — ITEM 1 · CLAUSE 1 · THE KINETIC CAP, AND THE FLOOR
# **CLAUSE 1 IS NOT CLOSED. THE ORDER'S ROUTE (a cap on S'' from the core's kinetic
# energy) IS CLOSED NEGATIVELY, BY MEASUREMENT. A SECOND LANGUAGE, THE FLOOR, IS THE
# FIRST TO CERTIFY ANY CHANNEL ABOVE l = 0: 5 OF 50.**
# Predictions: de84bae1...7151 (cap) and 208058e2...5ac0 (floor), both hashed before
# their instruments existed. Field: s84's through semi85 unmodified. Can-fails gate
# (CF0-CF6 cap; CF1-CF4 floor). 37 rows, 74 A-channels, 50 with K >= 1. Lever live on
# every row (cap: radicand at the kink centre, raised by exactly K tau/8, verified to
# 1e-3 on all 37; floor: same quantity, m~ and m~/2). Nothing sealed edited.
# c = 137.035999 remains the only number ever entered.

## §1 · THE DERIVATION
S''(u) = r^3 q'' = r^2 rho_r(r) for the direct core field (Gauss). **Correction to s86
§3, entered: a kink in S is a DELTA-SHELL in rho, not a step in 4 pi r^2 rho.**
sup P^2 <= ||P'||_2 = sqrt(2 T_i) (P(0)=0, two-sided Cauchy-Schwarz), so
M_u1 = r_out^2 sqrt(2 N T) >= M_u2 = r_out^2 sum occ sqrt(2 T_i) >= M_u3 = sup_orbit r^2 rho_r
(M_u3 is the CEILING of the sup-language, not a bound from T). With sigma~ = S~'' <= M~
and mass K, the extreme point is a RAMP of width tau = K L^2/(2 M_u), centred at the
tent's kink; J_max(K, M) by quadrature; tent recovered as M -> inf (CF4).

## §2 · THE CAP: S1-S6 CORRECT, S7 FALSIFIED — AND S7 IS THE RESULT
| clause | population | filed | measured |
|---|---|---|---|
| S1 sup S'' <= M_u2 <= M_u1 | A 74 | 0 viol | **0** |
| S2 Jtent >= Jmax1 >= Jmax2 >= Jmax3 >= J | A 74 | 0 viol | **0** |
| S3 certified by M_u2 (from T) | A K>=1, 50 | <= 2 | **0** |
| S4 certified by M_u3 (ceiling) | A K>=1, 50 | <= 5 | **0** |
| S5 d/f (K>=1.20) certified by M_u3 | 18 | 0 | **0** |
| S6 median M_u2/M_u3 > 10; M_u1/M_u2 < 3 | A 74 | | **433.4; 1.28** |
| S7 max tau3 < 0.10 | A 74 | | **0.544 FALSIFIED** |

**A sup-cap certifies only when S'' is spread over >= tau*(K) of the orbit**, measured
(symmetric ramp): tau* = 0.070 (K=1.02), 0.168 (1.05), 0.317 (1.10), 0.564 (1.20),
0.756 (1.30), 0.901 (1.40). The real core sits at tau3 median 0.104 (p, K~1.10), 0.228
(d, K~1.24), 0.473 (f, K~1.40): **a factor 2-3 short at every l.** The kinetic cap from
T is 433x weaker still. **No bound on sup S'', however sharp, cuts K = 1.** Closed.

## §3 · THE FLOOR: F1, F2, F5 CORRECT; F3, F4(p), F4(f), F6 FALSIFIED
m~ := 2 S''_min/L^2 (the core density's MINIMUM on the orbit, derived). Remainder mass
K - m~ concentrates as a tent (s85's theorem), floor contributes -(m~/2) t(1-t):
J_max = J_tent(b0', b1'; rescaled by 1-m~/2) / sqrt(1 - m~/2), b' = b - m~/2.
Closed form == quadrature 74/74 (F1). J_max >= J measured 74/74 (F2: theorem holds).
**Certified: 5 of 50** — Z=18 3p (K 1.046), Z=24,26,29,30 3d (K 1.18-1.25, m~ 0.51-0.64).
Filed >= 15: FALSIFIED. p: 1 of 30 (m~ median 0.054 — the p orbit's r_out lies where
the core density has died). f: 0 of 4 despite m~ = 0.80: **the floor is itself
convexity and raises J by 1/sqrt(1-m~/2)**; the effective test is
(K - m~)/(1 - m~/2) < ~0.97, and 4f's 0.617/0.60 = 1.03 fails. The five J >= 2 channels
are not certified (F5, 0 of 5). median m~ = 0.0487 against 0.05 filed (F6, a miss).

## §4 · WHAT THE TWO LANGUAGES SAY TOGETHER
The cap (upper) cannot cut; the floor (lower) cuts only where the orbit lies INSIDE the
core (3d). Both are SINGLE NUMBERS over the orbit. The real S'' profile is large on the
inner part of the orbit and dies on the outer; a single floor is the minimum, a single
cap the maximum, and neither is the shape. **The next step is a derived lower PROFILE
sigma~(t) >= phi(t), not a constant** — e.g. the field of the innermost shells alone,
which is produced by the walk and never entered. Named, not measured.

## §5 · FAULTS
* **F87.1** CF3 threshold x10 mis-filed; held at x7. Substance (shell outside the cap)
  intact. Timing flag in source.
* **F87.2** CF5/CF6 sited at K=1.1, tau=0.05: VACUOUS (all inf). Re-sited; tau*(K)
  measured, not guessed (second guess also failed). Timing flags in source. s85 CF4 species.
* **F87.3** lever mis-sited twice: J at s channels responds to the cap below quadrature
  resolution (~1e-8); the global radicand minimum is trivially ~0 at the turning point.
  Closed on the KINK-CENTRE radicand, raised by exactly K tau/8 — analytic, no grid.
  Also: rows rounded to 1e-10 before the check (0.2% of the step at 8s); rounded at 1e-14.
* **F87.4** the M_u1/M_u2 ramps (tau ~ 1e-6) were SUB-GRID (theta spacing 8e-6) in the
  first 33 rows: the 'live' lever read there was grid noise. Quadrature refined inside
  the ramp and the tent's kink; **all 37 rows re-run under the final instrument.**
* Z=89 first halted because the lowest-l live channel is 8s with K = 1.0001 — an s
  channel at K >= 1, the first seen (Z=88-91, nu_rank >= 2, outside A). Recorded.
* Item 1b of the ORDER (Z=56 site) NOT touched. Item 2 not started.