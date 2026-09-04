# RESULT S85 — ITEM 1 · CLAUSE 1 · THE VARIABLE-q BOUND
# **CLAUSE 1 IS NOT CLOSED.** A BOUND IS DERIVED AND VERIFIED; IT IS TOO WEAK TO FORCE
# J < 2 ANYWHERE ABOVE l = 0, AND WIDENING FALSIFIED THE ORDER'S OWN THIRD PREMISE.
# Prediction d5d40ca1...5f5ba166, filed and hashed BEFORE the instrument was written.
# Instrument pack85/semi85.py. f811 lint: **NOT APPLICABLE** (no S3 ladder) — recorded
# as not applicable, NOT as a pass. Can-fails PASS and gate. 37 rows, 185 channels.
# Nothing sealed edited. c = 137.035999 remains the only number ever entered.

## §1 · THE BOUND — DERIVED, AND THE THRESHOLD IS EXACT

In u = 1/r, with S(u) := q(r)/r = -V(r) and [u1,u2] the outer allowed region:

    f - g = 2[S - CHORD],   g := L^2 (u-u1)(u2-u)

where g is the UNIQUE constant-charge parabola through the same two turning points and
int du/sqrt(g) = pi/L is s84's anchor. Hence, with a := u2-u1 and t := (u-u1)/a,

    J = (1/pi) int_0^1 dt / sqrt( t(1-t) - delta(t) ),  delta := 2[CHORD-S]/(L^2 a^2)

**delta >= 0 exactly when S is convex in u, i.e. when q'' >= 0, i.e. where the radial
core density 4 pi r^2 rho is falling.** J is a CONVEX functional of delta and delta is
AFFINE in S, so J is maximised at an extreme point of the admissible set of S; those
extreme points are one-kink TENTS, and each tent piece leaves the radicand QUADRATIC,
so the maximum is closed-form:

    J_tent(b0,b1) = 1 + (2/pi)[ asin sqrt(tk/(1-b0)) - asin sqrt((tk-b1)/(1-b1)) ]

**J_tent = 2 EXACTLY on b0 + b1 = 1, for EVERY split** (checked at four splits, max
deviation 9.2e-7). Therefore, with V+ the positive variation of w := q - r q' across
the orbit's own turning points,

> **K := 2 V+ / (L^2 a)  <  1   ==>   J < 2   ==>   dg/dl > 0   ==>   G-WITHIN.**

**S1 CORRECT: ZERO violations over all 185 measured channels.** The bound is a theorem
and it survives contact with the real field.

## §2 · AND IT IS TOO WEAK. THE MEASURED SEPARATION IS BY l, NOT BY J = 2

Population A = the width-2 frontier (nu_rank 0,1), 74 channels over 37 rows.

| l | n | K median | K max | K >= 1 | J median | J max |
|---|---|---|---|---|---|---|
| 0 s | 22 | 0.9898 | 0.9978 | **0 of 22** | 1.2214 | 1.2336 |
| 1 p | 30 | 1.1028 | 1.2066 | **30 of 30** | 1.6132 | 1.8653 |
| 2 d | 18 | 1.2392 | 1.3471 | 16 of 18 | 1.7953 | 2.4407 |
| 3 f | 4 | 1.4031 | 1.4210 | 4 of 4 | 2.0006 | 2.1018 |

**THE BOUND CERTIFIES l = 0 AND NOTHING ELSE.** It is informative at 24 of 74 frontier
channels, and all 24 are s. **S3 FALSIFIED** (30 l<=1 frontier channels have K >= 1);
**S4 FALSIFIED** in consequence; **S8 FALSIFIED** badly (50 channels with K >= 1, filed
at most 8).

**IT DOES MEET THE ORDER'S l = 1 / l = 3 TEST, AND CLEANLY.** K rises monotonically
in l and the l=1 and l=3 ranges DO NOT OVERLAP: max K(l=1) = 1.2066 < min K(l=3) =
1.3847. **The bound distinguishes p from f. Its threshold simply does not sit where
J = 2 sits.** K = 1 separates s from everything; J = 2 separates five channels from
the rest; the two cuts are not the same cut.

**K_end = K AND conv_frac = 1.000 AT EVERY ONE OF THE 74.** The frozen core's w is
monotone across every orbit measured, so the positive-variation refinement (D3), built
because real cores have shell structure, is IDLE on this population. It is correct and
it was not needed. CF5 sites the case where it would bite; no real row did.

## §3 · **WIDENING FALSIFIED THE ORDER'S THIRD PREMISE. SIX ROWS WAS SIX ROWS.**

The order gave three things the measurement already had, the third being that J crosses
2 ONLY at 6d/Z=89 and 5f/Z=90. Over 37 rows, **J >= 2 at FIVE width-2 frontier
channels**:

| Z | channel | rank | J | K | sealed entrant |
|---|---|---|---|---|---|
| 40 | 4d | 0 | **2.0763** | 1.3471 | 4d |
| 56 | 5d | 1 | **2.4407** | 1.2950 | 6s |
| 89 | 6d | 0 | 2.0201 | 1.2103 | 6d |
| 90 | 5f | 1 | 2.1018 | 1.3986 | 6d |
| 91 | 5f | 0 | 2.0456 | 1.3847 | 5f |

**Z=40 (Zr) AND Z=56 (Ba) ARE NOT ACTINIDE OPENINGS AND THEIR ROWS ARE CLEAN AT
WIDTH 2.** The largest J in the entire set is Z=56's 5d at 2.4407 — larger than
Thorium's. **dg/dl < 0 at a frontier channel therefore does NOT imply the row fails at
width 2**, and any route that treats J >= 2 as the failure itself is reading a
sufficient condition as a definition.

**S7 CORRECT.** Z=91's 5f has K = 1.3847 and J = 2.0456: the actinide breach is not
Thorium's alone, which is the second data point the order asked for.

## §4 · s84's S7 RE-SCORED ON THE WIDENED SET — **35 OF 37, AND Z=56 IS THE FAULT SITE**

Sign of dg/dl at the rank-2 channel against sign of the banked g-difference, s84's own
rule on s84's own population, now over 37 rows: **AGREE 35, DISAGREE 2.**
* **Z=37** banked = -0.001. The sign of a vanishing quantity; a null row, not a miss.
* **Z=56** dg/dl(5d) = -0.441 against banked = +0.363. **A genuine disagreement, and it
  is the same row that carries the largest J in the set.** The criterion calls G-within
  broken at Barium and the sealed ladder says it is not.

**Z=56 IS THE NEW SITE.** It was outside s84's six rows.

## §5 · WHAT WAS LOST, AND WHERE THE ROUTE NOW GOES

**S5 AND S10 FALSIFIED TOGETHER, AND THE CAUSE IS ONE ALGEBRA STEP.** Filed step (v)
rewrote K as V+ / (c* sqrt(1-(L/nu*)^2)) using u1*u2 = -2E/L^2. **That follows from
f(u1)=f(u2)=0 only when q is CONSTANT**; for a varying q the product of the turning
points is not fixed by E. Measured discrepancy up to 0.787 in K. **THE BOUND ITSELF
NEVER USED (v)** — K := 2V+/(L^2 a) throughout — so what is lost is the interpretation,
not the theorem. The exact replacement is Gamma := L^2 a / 2, with eps_exact := Gamma/c*
reducing to the Coulomb eccentricity when q is constant. **And eps_exact does exactly
what the filed eps was supposed to do and could not**: median 0.9990 (s), 0.9773 (p),
0.8739 (d), **0.6711 (f)**, with Z=90's 5f at 0.8281. The filed eps, built on the bad
step, read 0.999 for everything and discriminated nothing.

**S6 FALSIFIED ON MONOTONICITY ONLY.** K at A's s channels stayed in
[0.9559, 0.9978] and never reached 1, as filed. It is not monotone in Z, and the breaks
are structural rather than noise: K(s) DROPS at Z = 20, 38, 56 — **exactly the rows
where the entrant is the second s electron.** **S9 FALSIFIED ON THE BAND ONLY**: no
l<=1 frontier channel anywhere has J >= 2 (the substantive clause, now over 37 rows
rather than 6), but two p channels sit at 1.409 and 1.441, below the filed 1.45.

**SCORE: S1, S2, S7 CORRECT. S3, S4, S5, S6, S8, S9, S10 FALSIFIED — three of ten.**

**THE ROUTE, AND IT IS ONE STEP.** The tent is the extreme point over convex S with
given endpoint slopes, and it uses NOTHING ELSE about q. But the real q obeys two
constraints the saturating tent violates: **Q(u) = q(1/u) is NON-DECREASING in u and
lies in [1, Z]** — Gauss's law, already the ruling of F84.3. A tent that reaches
b0+b1 = 1 generally corresponds to a Q that is not monotone or leaves the band.
**Re-taking the extreme point over the admissible set INTERSECTED with those two
constraints must raise the threshold above K = 1**, and the p channels sit at K ~ 1.10
with J ~ 1.61 — a long way inside a threshold that has room to move.

## §6 · FAULTS REGISTERED

* **F85.1** the can-fail accumulator was written `ok &= g`. Where a clause returns a
  truthy NON-BOOLEAN — `g3 = (viol==0) and lo_side and hi_side` returns the int 2 —
  `True & 2` is 0 and **the gate reported FAIL while every clause printed PASS**. With
  the int 3 it would have reported PASS while a clause failed. **A bitwise operator
  standing in for a logical one, in the gate itself.** Repaired with bool(); the
  failure direction was safe this time and is not guaranteed to be.
* **F85.2** scoring s84's S7 on the widened set, I first computed a SECOND difference
  of dg/dl between the two frontier channels and read 17 disagreements of 37 — an
  apparent collapse of s84's headline result. s84's clause is a FIRST difference: the
  sign of dg/dl AT the rank-2 channel. Re-scored correctly it is 35 of 37. **I nearly
  filed a false falsification of the previous session under the previous session's own
  clause name.** Same species as F83.1 — a claim whose statistic was not stated — but
  about the STATISTIC rather than the population. Caught by re-reading s84's table.
* **CF4 and CF8 were both corrected AFTER failing** and both timing flags are written
  into the instrument's source (R1449). CF4 was a badly SITED probe — one named core
  at l=1 giving K=0.9806, while the same core at l=2,3 gives K>1 — and the substance
  (two-sidedness) had already passed at CF3 before the revision. CF8 was a REAL
  failure and is the falsification of S10, recorded as such and not repaired away.
