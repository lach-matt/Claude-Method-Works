# SESSION 85 — COMBINED HANDOFF
# Open Session 86 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-85 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108.

## §0 · OPEN
`bash pack58/open58.sh` passed: s84 seal **1400/1400 root MATCH**, STATE CARD CLEAN,
canary CLEAN, ledger 0 jobs. **ITEM 1 TOOK THE SESSION, AS ORDERED. ITEM 2 NOT STARTED
AND NOT TOUCHED — it derives nothing and was not allowed to displace Item 1.**

## §1 · ITEM 1 — **A BOUND IS DERIVED AND VERIFIED. IT IS TOO WEAK. CLAUSE 1 IS OPEN.**
pack85/RESULT-S85-ITEM1-THE-BOUND.md. Prediction d5d40ca1...5f5ba166 filed and hashed
before pack85/semi85.py existed. Instrument imports s84's field unmodified (CF6: q grid
identical to semi84's qfun at 0.00e+00). **f811 lint NOT APPLICABLE — no S3 ladder —
recorded as not applicable, not as a pass.** Can-fails PASS and gate. 37 rows.

**THE BOUND.** f - g = 2[S - CHORD] with g the constant-charge parabola through the
same turning points, so J = (1/pi) int dt/sqrt(t(1-t) - delta). J is CONVEX in delta,
delta AFFINE in S, so the maximiser is a one-kink TENT whose pieces leave the radicand
quadratic. **J_tent = 2 EXACTLY on b0+b1 = 1, every split.** Hence

> **K := 2 V+ / (L^2 a) < 1  ==>  J < 2  ==>  G-within**, V+ = positive variation of
> w := q - r q' across the orbit's own turning points.

**S1 CORRECT: zero violations over 185 real channels.**

**AND IT CERTIFIES l = 0 ONLY.** Over the width-2 frontier: K >= 1 at 0/22 s, **30/30
p**, 16/18 d, 4/4 f. Informative at 24 of 74. **S3, S4, S8 FALSIFIED.** K does separate
l=1 from l=3 with no overlap (max K(p) = 1.2066 < min K(f) = 1.3847) — it meets the
order's test — **but K = 1 separates s from everything, and J = 2 separates five
channels from everything. The two cuts are not the same cut.**

**WIDENING FALSIFIED THE ORDER'S THIRD PREMISE.** J >= 2 at **FIVE** frontier channels,
not two: **Z=40 4d (2.076), Z=56 5d (2.441)**, Z=89 6d (2.020), Z=90 5f (2.102),
Z=91 5f (2.046). Zr and Ba are not actinide openings and their rows are CLEAN at width
2 — **so dg/dl < 0 at a frontier channel does not imply the row fails.** The largest J
in the set is Barium's, not Thorium's. **S7 CORRECT**: Z=91 breaches too, so the
actinide breach is not Z=90's alone.

**s84's S7 RE-SCORED, s84's own rule, 37 rows: AGREE 35, DISAGREE 2.** Z=37 is a null
row (banked -0.001). **Z=56 is a genuine disagreement — dg/dl(5d) = -0.441 against
banked +0.363 — and it is the same row carrying the largest J. Z=56 IS THE NEW SITE.**

**S5 AND S10 FALSIFIED BY ONE ALGEBRA STEP.** Filed step (v) used u1*u2 = -2E/L^2,
true only for CONSTANT q. **The bound never used it**; the interpretation is lost, not
the theorem. Exact replacement Gamma := L^2 a/2, and eps_exact := Gamma/c* does what
the filed eps could not: 0.9990 s, 0.9773 p, 0.8739 d, **0.6711 f**, Z=90 5f 0.8281.
**S6 FALSIFIED on monotonicity only** — K(s) stayed in [0.9559,0.9978] and never
reached 1, and its breaks sit at Z = 20, 38, 56, exactly the second-s-electron rows.
**S9 FALSIFIED on the band only** — no l<=1 frontier channel has J >= 2 anywhere in 37
rows; two p channels sit just under the filed floor.
**SCORE: S1, S2, S7 CORRECT. S3, S4, S5, S6, S8, S9, S10 FALSIFIED. Three of ten.**

**V+ WAS IDLE.** K_end = K and conv_frac = 1.000 at all 74 frontier channels: the
frozen core's w is monotone across every orbit measured. The refinement is correct and
no real row exercised it.

## §2 · FAULTS REGISTERED THIS SESSION
* **F85.1** `ok &= g` in the CAN-FAIL GATE ITSELF. A truthy non-boolean clause result
  (`int 2`) made `True & 2` = 0: the gate printed FAIL while every clause printed PASS.
  With `int 3` it would have printed PASS over a failing clause. **A bitwise operator
  standing in for a logical one, inside the thing that gates every run.** Repaired.
* **F85.2** I first re-scored s84's S7 with a SECOND difference and read 17/37
  disagreements — an apparent collapse of s84's headline. s84's clause is a FIRST
  difference; correctly scored it is 35/37. **A false falsification of the previous
  session, under that session's own clause name, caught only by re-reading its table.**
  F83.1's species, thirteenth appearance, this time about the STATISTIC not the
  population.
* **CF4** corrected after failing: a badly SITED probe, substance already passed at CF3.
  **CF8** corrected after failing: a REAL failure, and it is S10's falsification.
  Both timing flags written into the source (R1449).

## §3 · WHERE CLAUSE 1 GOES — ONE STEP, NAMED
The tent uses only the endpoint slopes and nothing else about q. The real q obeys two
constraints the saturating tent violates: **Q(u) non-decreasing and 1 <= Q <= Z**
(Gauss, already F84.3's ruling). Re-taking the extreme point over the admissible set
INTERSECTED with those must raise the threshold above K = 1. The p channels sit at
K ~ 1.10 with J ~ 1.61: there is a long way inside for the threshold to move.

## §4 · UNCHANGED
Deliverable 1, the gates, the STATE CARD, the chain and every sealed row untouched.
**CLAUSE 1 REMAINS THE LAST OPEN DELIVERABLE.** T4 unblocked, last by practice.
ALPHA THREAD CLOSED. Z=111 WITHHELD. F54.1, F67.1-F67.6 UNVERIFIABLE, O-C1 open,
Rung B not built, F82.2 open and bounded, F84.1 detector sealed.
