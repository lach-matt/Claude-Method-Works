# RESULT S88 — ITEM 1 · CLAUSE 1 · THE DERIVED LOWER PROFILE phi(t)
# **CLAUSE 1 IS NOT CLOSED. THE PROFILE ROUTE CERTIFIES 31 OF 50 AS FILED (P2), 43 OF 50
# AT THE DEEPEST ACCEPTED RUNG; THE SEVEN LEFT ARE THE FIVE J >= 2 CHANNELS (FORCED BY
# THE THEOREM), Z=19 4p (PREFACTOR) AND Z=57 5d (J=1.985 vs J_max=2.004). THE PROFILE'S
# OWN CONVEXITY COSTS A MEDIAN 0.52 IN J OVER THE BARE REMAINDER TENT.**
# Prediction b23277e2...0363, hashed before pack88/prof88.py existed. Field: s84's through
# floor87 unmodified. Can-fails CF1, CF1b, CF2-CF5 gate. 37 rows, 74 A-channels, 50 K >= 1.
# Lever live on all 37 (kink-centre radicand, scale 0 / 1/2 / 1). Nothing sealed edited.
# c = 137.035999 remains the only number ever entered.

## §1 · THE INSTRUMENT (derived; every object is produced by the walk)
Sub-core c = a subset of the frozen N-1 core's shells. q_c = -sum_c occ Y0_c (the walk's own
Y0, no nucleus, no exchange). Phi = the sub-core's S~ on the channel's ruling orbit, by the
SAME geometry() that measures b0, b1. Remainder R = S~ - Phi; the hypothesis sigma~ >= phi
is TESTED as convexity of R on the orbit (w-grid, conv >= 0.999) and REFUSED otherwise.
Extreme point (s85's theorem on R): S~_max = Phi + tent(b0-beta0, b1-beta1); J_max by
quadrature. P1 = innermost shell; P2 = core minus outermost shell; ladder P_k, k=1..nsh-1.

## §2 · SCORE
| clause | filed | measured |
|---|---|---|
| T1 J_max >= J, P1 and P2 | 0 viol | **0 / 0 (theorem holds, 74+61)** |
| T2 lever live, 37 rows | all | **37** |
| T3 refusals P1 / P2 | <=2 / <=6 | **0 / 13 FALSIFIED (P2)** |
| T4 P1 certified | <=3 of 50 | **0** |
| T5 P2 certified | >=30 of 50 | **31** |
| T6 P2 by l: p / d / f | >=22/30, >=10/16, <=2/4 | **29 / 1 FALSIFIED / 1** |
| T7 J>=2 certified | 0 of 5 | **0** |
| T8 ladder monotone | >=45 of 50 | **37 FALSIFIED** |
| T9 median K' P2 / P1 | <0.15 / >0.80 | **0.059 / 1.07** |
| T10 median J_max - J (P2) | <0.10 | **0.023** |

**All 13 P2 refusals are one species:** the channel is OCCUPIED in the frozen core
(3d Z=24-30, 4d Z=40-47, 5d Z=58-59, 4f Z=59, 6d Z=90-91). Its q carries the E7
same-shell exchange multipole, which lowers S'' below r^2 rho; the shell's own direct
density then exceeds the channel's true sigma~ (Z=24 3d: K_c=1.2585 > K=1.2544) and the
instrument refuses, as designed. The rung below (core minus outermost AND minus the
channel's own shell) is accepted everywhere. **Deepest accepted rung: 43 of 50; by l:
p 29/30, d 12/16, f 2/4.** (Post-hoc read of the filed ladder; commentary, timing flag.)

**T8: the ladder is not monotone** because each added shell moves the remainder tent's
kink and the profile's convexity raises the radicand's floor: median J_max - J_tent(rem)
= 0.52 under P2. The prefactor is large; it is the price of the profile's shape.

**P1 certifies nothing**: the innermost shell's density is dead on every frontier orbit
(median K' = 1.07, i.e. K_c ~ 0). The profile that cuts is the one that lies ON the orbit.

## §3 · WHAT IT SAYS
Clause 1's sufficient condition is now: **sigma~ >= phi_c on the orbit and
K - int phi_c small enough that phi_c + tent < 2 in J** — with phi_c the direct field of
the walk's own sub-core. With P2 the remainder is a median 0.06 of K: the bound is one
shell short of the measurement itself, and it is informative at 31 (43) of 50 precisely
because J < 2 there. It does not cut the five J >= 2 channels and cannot (T1). **The route
is exhausted at this language: no profile drawn from the walk's own shells certifies a
channel whose measured J >= 2, and clause 1 needs the ORDER, not J < 2, at those five.**

## §4 · ITEM 1b · Z=56 SITED: 5d CONFIRMED, 4d CORRECTED
Both wells reported (semi84 I_inner). Z=55 5d: n_regions=2, outer J=1.0358 (B1 outer
CORRECT), **inner J=1.8605 (B1 inner >2 FALSIFIED)**; Z=56 5d: one region, J=2.4407 (B2
CORRECT). **The jump to J=2.44 is the MERGE of the two wells, not the inner well.**
Z=38 4d: **n_regions=1, J=2.2337, K=1.381 (B3 FALSIFIED)**; Z=39 4d: one region, J=2.2731
(B4 CORRECT on region, J>=2). **The 4d collapse is between Z=37 and 38, not 39/40.** Z=40
was the first row where 4d ENTERED population A, not the first post-collapse row; J(4d)
runs 2.234 (38), 2.273 (39), 2.076 (40), 1.873 (42). For 5d the note stands: collapse
55->56, J peaks at 56. Z=56 CONFIRMED AND CLOSED as a region-switch site; the note's 4d
sentence is corrected, not confirmed.

## §5 · FAULTS
* **F88.1** CF5 filed at Z=24 3d where P2 is refused; re-sited to Z=24 4p after seeing it
  (species F87.2). CF1 compared inf==inf (vacuous); CF1b added at a finite tent, tolerance
  1e-5 (4.9e-6 measured, quadrature vs closed form, s87 F1). Timing flags in source.
* **F88.2** filed lever criterion 'rc(1/2) between rc(0), rc(1)' over-specified: the kink
  centre moves with the scale, rc is not monotone (Z=13 4s). Relaxed to three distinct
  values; the lever moved on every row. Timing flag in source.
* T3(P2), T6(d), T8, B1(inner), B3 FALSIFIED: entered as such, mechanisms above.
* Item 2 not started. Z=90 figures do not travel.