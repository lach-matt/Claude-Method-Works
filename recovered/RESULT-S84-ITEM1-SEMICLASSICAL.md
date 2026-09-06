# RESULT S84 — ITEM 1 · CLAUSE 1 · THE SEMICLASSICAL HALF, STARTED
# **CLAUSE 1 IS NOT CLOSED.** An EXACT ANCHOR is derived and a CRITERION is measured.
# Prediction 2857b8f5...9bd33c41, filed and hashed BEFORE the instrument was written.
# Instrument pack84/semi84.py, f811 lint rc=0, can-fails PASS and gate.
# Nothing sealed edited. c = 137.035999 remains the only number ever entered.

## §1 · THE ANCHOR THEOREM — EXACT, AND IT IS THE RESULT

With q(r) := -r V(r), E the channel's energy and L := l + 1/2:

    p = sqrt(2E + 2q(r)/r - L^2/r^2),   Phi = int p dr,   pi*delta = Phi - Phi_Coulomb
    dPhi/dL^2 = -(1/2) I,              I(L) := int dr/(r^2 p)

**In u = 1/r the radicand is a QUADRATIC whenever q is constant, and the integral of an
inverse square root of a quadratic between its own roots is pi/sqrt(coefficient).
Hence I = pi/L EXACTLY, for ANY constant charge and ANY bound E.** Verified to
**max |J-1| = 7.5e-12** over 60 (q0, l, E) cases with q0 in {1, 2, 89, 90}, and the
allowed/forbidden split agrees with the closed form 2E + q0^2/L^2 > 0 at 60/60.

Therefore, exactly:

> **dg/dl = 2 - J,   J := I/I_C = (L/pi) I.   G-within (dg/dl > 0)  <=>  J < 2.**

**THE CONTENT IS THE CHARGE-BLINDNESS.** A bare nucleus of charge 90 and a hydrogen
atom contribute IDENTICALLY to I. **The entire l-dependence of the quantum defect —
the whole threat to Madelung's tie-break — therefore lives in the region where q(r)
is VARYING, and nowhere else.** That is a property of F_core, derived rather than
fitted, and it is the first thing this project has said about F_core itself rather
than about the ladder F_core produces.

**IT IS NOT YET A PROOF OF CLAUSE 1. No bound on the variable-q contribution is
derived.** What is earned is that the target is now a bound on ONE integral over ONE
region, with the rest cancelling identically.

## §2 · THE MEASUREMENT — SIX ROWS, THE WIDTH-2 FRONTIER AND ITS NEIGHBOURS

Field: fixed81's frozen N-1 core, one SCF per Z, entrant occupancy reduced by one.
Currency: **the sealed relaxed D, never an eigenvalue (F79.2 avoided by construction).**
q(r) is the DIRECT core field; every channel reports q_tail, and all thirty read
**1.000000**, reproducing s82's q_eff independently.

| Z | rank 1 | J | dg/dl | rank 2 | J | dg/dl | banked dg/dl | sign |
|---|---|---|---|---|---|---|---|---|
| 20 | 4s | 1.196 | +0.804 | 4p | 1.727 | +0.273 | +0.653 | agree |
| 38 | 5s | 1.200 | +0.800 | 5p | 1.730 | +0.270 | +0.636 | agree |
| 57 | 5d | 1.985 | +0.015 | 6p | 1.586 | +0.414 | +0.343 | agree |
| 88 | 7s | 1.190 | +0.810 | 7p | 1.681 | +0.319 | +0.553 | agree |
| 89 | 6d | **2.020** | **-0.020** | 7p | 1.612 | +0.388 | +0.217 | agree |
| 90 | 6d | 1.906 | +0.094 | 5f | **2.102** | **-0.102** | **-0.293** | **agree** |

"banked dg/dl" is (g(rank2) - g(rank1))/(l2 - l1) from the sealed g-ladder.

**S7 HOLDS AT 6 OF 6, INCLUDING THE SIGN REVERSAL AT THORIUM.** The criterion built
from the radial potential alone reproduces the sign of the banked g-difference at
every tested row, and the one row where the banked difference is NEGATIVE — Z=90, the
sole width-2 failure in the whole 107-row walk — is the one row where the criterion
also goes negative. Magnitudes agree to about 0.15 g-units at five rows; at Z=90 the
predicted -0.004 is far smaller than the measured -0.293, so **the SIGN is the claim
and the magnitude is not.**

## §3 · SCORING — **THREE CLAUSES LOST, AND ONE OF THEM INVERTS THE MECHANISM**

**S1, S2 CORRECT.** The anchor, at 7.5e-12, and its charge-blindness.

**S3 FALSIFIED AS FILED.** I filed J < 2 at every width-2 frontier channel "except
possibly Z=90". Measured: **two of twelve exceed 2 — Z=89 6d (2.0201) and Z=90 5f
(2.1018).** Z=89 was not filed as an exception. Both are actinide-opening channels.

**S4 FALSIFIED, AS EXPECTED.** Filed 0.6..1.4; **20 of 30 channels sit outside**, J
running to 2.62. It was a guess at the size of a term I had not bounded and it is
recorded as lost.

**S5 FALSIFIED, AND THE INVERSION IS THE FINDING.** I filed that the deviation
|J - 1| would be LARGER for penetrating channels (l <= 1) than for l >= 3, by at least
2x in the median. **Measured: 0.599 for l <= 1 against 0.835 for l >= 3 — the
inequality runs the OTHER WAY.** The s channels sit CLOSEST to the anchor (J ~ 1.20),
and it is the l = 1, 2, 3 channels that sit furthest from it.
**AND THE ANCHOR THEOREM EXPLAINS ITS OWN FALSIFICATION.** An s orbit spends its phase
where the field is Coulombic at BOTH ends — charge Z deep in, charge 1 far out — and
the anchor cannot tell those apart. **The centrifugal barrier does not protect a
high-l channel from the core; it PARKS the channel exactly in the transition region
where q(r) varies, which is the only region the anchor does not cancel.** My filed
reasoning had the geometry right and the consequence backwards.

**S6 SPLIT, AND THE SPLIT IS F83.1's SPECIES AGAIN.** Over all thirty channels the
extreme row is **Z=88 (-0.620 at 6d), not Z=90**, so S6 as filed is FALSE. Restricted
to the width-2 frontier — the population the order names, and the population the
clause was about — the minimum dg/dl is **Z=90 (-0.102)**, then Z=89 (-0.020), then
Z=57 (+0.015), and S6 holds. **I did not state the population in the clause. That is
the eleventh appearance of the species and it is registered, not argued around.**

## §4 · TWO THINGS THE INSTRUMENT FOUND THAT WERE NOT ASKED FOR

**THE COULOMB REFERENCE ORBIT DOES NOT ALWAYS EXIST.** I_C = pi/L is analytic, but the
charge-1 reference is classically empty wherever nu < L. Every d and f channel at a
block opening is in that condition — 3d at Z=20 has nu = 2.265 against L = 2.5. **A
channel can be bound more deeply than ANY charge-1 Coulomb orbit of its own L**, and
the first draft of the instrument discarded exactly those rows as "no allowed region",
which would have blinded it at the frontier. Recorded per row as `coulomb_ref`.

**Z=89's 5f CHANNEL RETURNS TWO ALLOWED REGIONS.** An inner well and an outer well
separated by a centrifugal barrier — **the orbital-collapse configuration, appearing
unbidden at Ac, which is one of the three elements this project already names as a
collapse site (La/57, Ac/89, Th/90).** It is the only channel of the thirty that does.
Its J = 1.029 describes the OUTER well alone and must be read that way.

## §5 · FAULTS REGISTERED

* **F84.1** f811's S3 detector keys on the literal `.append(float(E...))`; written as
  `steps.append(E2)` the same restart is invisible and its rc=0 is VACUOUS. Repaired
  forward by writing the accumulation in the readable form; the detector is unrepaired
  and sealed.
* **F84.2** the first region-finder took the outermost bracket of p > 0 and would have
  spanned straight across a centrifugal barrier — i.e. across the collapse structure.
  Repaired to return every interval.
* **F84.3** the exchange localisation X/P **diverges at every node of P**, splitting a
  4s radicand into four spurious "regions". **The multi-region machinery of F84.2 would
  have read that artefact as the collapse physics it exists to find.** Repaired by
  ruling the DIRECT core field, where 1 <= q <= Z holds by Gauss's law, and reporting
  the localised-exchange J_x alongside for occupied channels only.
* **CF3 and the anchor scope were both corrected AFTER failing**, and both timing
  flags are written into the instrument's source (R1449). In each case the substance
  passed before the revision.

## §6 · WHAT CLAUSE 1 ASKS FOR NOW

Unchanged in target, sharper in shape:

> **Derive a bound on the variable-q contribution to I forcing J < 2 at the width-2
> frontier, and account for Z=90 — where the measured J of the 5f channel is 2.10.**

**THE ROUTE IS NO LONGER OPEN-ENDED.** Everything outside the transition region
cancels exactly. What is missing is one inequality about one integral over the region
where the core's charge is being screened away.
