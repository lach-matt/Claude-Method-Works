# RESULT S86 — ITEM 1 · CLAUSE 1 · THE GAUSS CONSTRAINT DOES NOT CUT THE TENT
# **CLAUSE 1 IS NOT CLOSED. THE ORDER'S ROUTE IS CLOSED, NEGATIVELY, BY MEASUREMENT.**
# Prediction e40fa479...6a978, filed and hashed BEFORE pack86/semi86.py existed.
# Field: s84's, through semi85 unmodified. f811 lint NOT APPLICABLE (no S3 ladder) —
# recorded as not applicable. Can-fails CF1-CF5 PASS and gate. 37 rows, 74 A-channels.
# Lever (q == 1 dead arm: intercepts 0, K 0; live arm moves both) LIVE on all 37 rows.
# Nothing sealed edited. c = 137.035999 remains the only number ever entered.

## §1 · THE ALGEBRA, AND IT HELD 74/74
The tent's pieces are the tangent lines of S(u) = u Q(u) at u1 and u2. A tangent at u0
has intercept alpha = -u0^2 Q'(u0) = r0 q'(r0). Wherever q' <= 0 (Gauss, F84.3) the
intercept is <= 0, and a line with non-positive intercept has Q_line = slope + alpha/u,
NON-DECREASING in u. So each piece obeys Gauss, the pieces meet continuously, and
Q_tent runs from Q(u1) to Q(u2) inside [1, Z].

| clause | statistic | population | result |
|---|---|---|---|
| S1 both intercepts <= 0 | 74/74 | A | CORRECT |
| S2 Q_tent monotone and in [Q1,Q2] | 74/74 (max excursion 7e-15) | A | CORRECT |
| S3 1 <= Q1, Q2 <= Z | 74/74 | A | CORRECT |
| S4 K>=1 tents excluded by the two constraints | **0 of 50** | A, K>=1 | CORRECT |
| S5 construction check (tent endpoints) | 74/74 | A | CORRECT |
| S6 saturating tent admissible | 50/74 | A | **FALSIFIED** |

**THE THRESHOLD DOES NOT MOVE.** At every channel with K >= 1 — all 30 p, 16 of 18 d,
4 of 4 f, and all five J >= 2 channels (Z=40, 56, 89, 90, 91) — the tent that realises
the worst case is itself a Gauss-admissible screened field: density rho ∝ 1/r^2 on each
piece and a thin charged shell at the kink, all non-negative. Intersecting with
"Q non-decreasing" and "1 <= Q <= Z" removes nothing from the admissible set at any
channel the bound fails to certify. **Least-negative intercepts in the whole set:
alpha1 = -2.1e-9 (Z=37 4d, a tail channel), alpha2 = -6.3e-3 (same).** Nothing is near
the cut.

## §2 · S6 FALSIFIED, AND THE FALSIFICATION IS THE SHARP RESULT
Filed: the saturating tent is admissible 74/74 "because rescaling multiplies both
intercepts by a positive factor." **Wrong: the rescaling is about the CHORD, not the
origin** — alpha1' = A + s(alpha1 - A) with A the chord's intercept — so scaling up
(s = 1/K > 1, i.e. K < 1) can drive an intercept positive. Measured:

> **The saturating tent is Gauss-admissible at exactly the 50 channels with K >= 1,
> and inadmissible at exactly the 24 with K < 1. The two sets are IDENTICAL.**

So the two constraints bite precisely where the bound already certifies and nowhere
else. This is not a near-miss; it is the statement that K = 1 is the sharp threshold
over the Gauss-admissible set. **The order's premise ("a tent that reaches b0+b1 = 1
generally corresponds to a Q that is not monotone or leaves the band") is true only on
the certified side.**

## §3 · WHAT WOULD CUT — NAMED, NOT MEASURED (S7, carried as a claim)
A kink in S(u) is a delta in S'' = r^3 q'', i.e. a STEP in 4 pi r^2 rho, i.e. a jump in
some |P_nl|^2, i.e. a discontinuous P_nl: **infinite kinetic energy.** The constraint
that excludes the saturating tent is that the core orbitals lie in H^1 (finite T) —
the Schrödinger equation's own language, not Gauss's. Per the standing protocol on
nulls: a different mathematical language (Sobolev), and parameter-free, since T_core
is produced by the field, not entered. The extreme point over {S convex, endpoint
slopes given, S'' the derivative of an H^1 density} is no longer a tent; its J is a
function of K AND of a second derived number (a kinetic-energy or gradient bound on
the core). **That is the next step and the only one this session can name.** Nothing
here re-derives the anchor or the tent.

## §4 · UNTOUCHED
Z=56 (Item 1b) not sited this session — Item 1 took the room. Item 2 not started.
Z=90's figures do not travel. Deliverable 1, gates, STATE CARD, chain: unchanged.

## §5 · FAULTS
* **F86.1** score() first computed S4 as n - s6, counting K < 1 channels — already
  certified, status cannot change. The clause's statistic is K >= 1 tents excluded.
  Corrected, timing flag in source. F83.1's species, fourteenth appearance: the
  STATISTIC. Caught before the result was read out, not after.
* **F86.2** the lever site: at Z=58, 59 neither frontier channel's dead arm has an
  allowed region (q == 1 at a 4f/5d sealed E). Lever re-sited to the lowest-l live
  channel of five, as s85 D4. Corrected after a halt; timing flag in source.
* Dead-arm tolerance widened 1e-12 -> 1e-9 after seeing K_dead = 2.1e-12 at Z=13
  (np.gradient roundoff); s85's own tolerance. Timing flag in source.
