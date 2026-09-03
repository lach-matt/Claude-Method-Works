# The Λ audit — every reconstructible claim, and the three that do not reproduce

```sh
python3 tools/audit_lambda.py          # the full pass, a few minutes
python3 tools/audit_lambda.py --fast   # skips the interval census and the 842,206 triples
```

Sixty-one recorded claims about Λ are checked against the volumes: **59 PASS, 2 FAIL.**

There are **three findings**, not two. The third does not show as a FAIL because the program runs
that check on the population that makes it pass and annotates the discrepancy instead — the claim
is right, the box named beside it is not. All three sit in two places, §8.4's rank entries and
§11's marginal exclusion table, and none touches a cell count, a closure defect, or a structural
result.

The program adjudicates nothing. It prints the claim and the measurement side by side.

## What reproduces

Λ at 976 cells in a 6,912 box, `E = 0` in all five operator-bearing languages with all ten pairs
agreeing. Zero join and zero meet failures over all 475,800 unordered pairs. The rank sequence
`1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1`, log-concave at every
interior rank. `F(1) = 976`, `F(−1) = 2`, mean rank `11.0666`. The largest antichain at 122, and
`976 = 8 × 122`. Seventeen join-irreducibles. **1,113,045,672 maximal chains.** 115,162 comparable
intervals of which 31,604 are boxes, 116,138 distinct meet-join boxes, binding rates 30.0 / 28.0 /
1.9 %. The 319-cell seven-coordinate projection with `Σ (k+1) = 976`. `A_q(1) = 33, 33, 23, 8` and
`B_q(1) = 5, 10, 15, 17`. The triangle at 911 cells, and 280 / 240 / 40 on the stated box. The
tower at 1,654, 1,561 and 2,535. Λ₉'s 41,682 composable pairs, closed, and 842,206 associative
triples with no failure. Λ₁₀'s 485 non-composing cells, every one at `g = 0`. All eight marginal
exclusions.

## FINDING 1 — the rank skew is mislabelled, and read as a skew its sign is inverted

**§8.4, The rank skew.** Prints *"centre of mass 11.0666 vs midpoint 11.5, skew −0.43"*, and
attributes it: *"Prior art: the third standardised moment of a rank distribution. Gauss (1809)."*

The rank sequence reproduces exactly, and the third standardised moment of that sequence is
**+0.14**, not −0.43.

The printed −0.43 is `11.0666 − 11.5 = −0.4334` — the displacement of the centre of mass from the
midpoint. That is a real quantity, correctly computed, and it is the number the same sentence
derives two clauses earlier. It is not the statistic the prior-art note names.

The consequence is not cosmetic. The two quantities carry **opposite signs**, so a reader taking
"skew −0.43" at its attribution concludes Λ's rank distribution is left-skewed. It is not: the
right tail is the longer one, nine steps from the peak at rank 11 down to rank 20, against eight
from the peak down to rank 3.

Either the number wants a different name — *the centre-of-mass displacement*, with the Gauss
attribution dropped — or the third standardised moment wants computing and printing at +0.14.
The measurement does not choose.

## FINDING 2 — two sections disagree about the same eight cells

**§8.4, The rank skew:** *"only 8 of 976 cells **fixed** by x ↦ max − x"*

**§8.4, The Sperner property:** *"NOT self-dual: 8 of 976 cells **survive** x ↦ max − x against the
box maxima (3,1,3,3,3,1,3,3), **none fixed**"*

Measured: **8 survive, 0 are fixed.** The Sperner entry is right in both halves; the rank-skew
entry's "fixed" is wrong for a set of eight cells it otherwise counts correctly.

A fixed point of `x ↦ max − x` would need every coordinate at half its maximum, and the box maxima
`(3,1,3,3,3,1,3,3)` include odd values, so no cell can be fixed — the count is not merely wrong,
it is unreachable.

## FINDING 3 — the marginal exclusion table and the box printed beside it are different boxes

**§11.** The eight bounds ranked by marginal exclusion — `g ≤ q` 673, `q ≤ k` 575, `k ≤ 4ℓ+2` 564,
`ℓ ≤ n−1` 308, `2S ≤ k` 300, `f ≤ e−1` 200, `k ≥ 1` 25, `g ≤ 4f+2` 24 — are described as *"measured
on the rebuilt Λ₈ at the caps of §7.4"*, beside an ambient box quoted at **6,912**.

All eight reproduce exactly, but only on a **9,216**-cell box whose `k` runs from 0. On the
6,912-cell box, `k` runs from 1, so `k ≥ 1` cannot fail on any cell and its marginal exclusion is
**0**, not 25. The other seven are unchanged between the two boxes.

Both boxes are legitimate — 6,912 is the ambient after the `k ≥ 1` floor is applied, 9,216 before —
and the table is right on its own population. What is wrong is that the population is not the one
named next to it. Naming the pre-floor box, or dropping the `k ≥ 1` row from a table measured
post-floor, resolves it.

## Five false alarms, and what they show

Five checks failed during construction and every one was the audit's fault, not the book's. They
are recorded because the pattern is the point.

| the check | why it failed | what reconciled it |
| --- | --- | --- |
| comparable intervals | counted the 976 singletons | `116,138 − 976 = 115,162`, exactly |
| of which are boxes | same | `32,580 − 976 = 31,604`, exactly |
| binding rates | wrong population and wrong criterion | the book states both: `y_u > φ(x_v)` over the 475,800 pairs |
| join-irreducibles | counted the bottom element | Birkhoff excludes it: `18 − 1 = 17` |
| Λ₉′ | took the tighter bound alone instead of conjoined | the 93 cut cells came out at `(f=0, g=2, 2S′=2)`, as recorded |

In each case the index supplied its own reconciliation, and the offset was exact rather than
approximate — 976, 976, 1, 93. A closed index defends itself: a wrong reconstruction of it does not
land near the recorded figure, it lands a nameable distance away, and the distance names the error.
That is why a FAIL here is worth reading twice before it is believed.
