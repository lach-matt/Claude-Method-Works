---

# PART V — PAST, PRESENT, FUTURE

## 23. The balance, and where it holds

§10.2 reads the constraint tree as *past — change — future*, left to right: the source end (n, ℓ, k, 2S), the transfer q, the target end (e, f, g). The three-part reading is the book's; what follows is its arithmetic.

**The three parts do not add up as three free things.**

$$|A| \cdot |Q| \cdot |B| = 33 \cdot 4 \cdot 17 = 2{,}244 \qquad \text{against} \qquad |\Lambda| = 976$$

A defect of **1,268** — the three parts overcount by 130% when treated as independent. Conditioned on the transfer they separate exactly: Σ_q |A(q)|·|B(q)| = 976, defect zero.

**And the balance is not special to the transfer.** Tested at every cut of the constraint tree, four of the eight coordinates split it in two — ℓ, q, f and g — and **all four give defect zero.** §12.6.1 presents the q-factorisation as though the transfer were doing the work; the computation says the **tree** is doing it, and q is distinguished only by *which* two things it separates.

**The shape is a path, not a triangle.** Reading the three parts off the constraint tree gives edges past ↔ present and present ↔ future, and **no past–future edge**. Two edges, treewidth 1. That is not decoration: §18.4.1's criterion is that treewidth 1 closes exactly and treewidth 2 gives an envelope, so **Λ's exactness is a proof that the three parts are not a triangle.** A triangle would be the three-body shape, and register 316 states its price.

## 24. The future is a bracket, and the past does not enter

Two questions with computable answers: is the future a function of past and present, and does the past enter at all?

| | |
|---|---|
| (past, present) pairs | 97 |
| futures per pair | min 5 · median 10 · max 17 |
| **pairs determining a single future** | **0 of 97** |

**Not one pair determines a future.** That is §20.1's bracket arriving at the level of the transition itself, and §13.4's line computed — structure does not choose, and 1,113,045,672 maximal chains satisfy every constraint in the book while it chooses none of them.

**And for each value of the present, all pasts give the same future set.**

| present q | distinct pasts | distinct future sets | \|future\| |
|---|---|---|---|
| 0 | 33 | **1** | 5 |
| 1 | 33 | **1** | 10 |
| 2 | 23 | **1** | 15 |
| 3 | 8 | **1** | 17 |

> **The future is conditionally independent of the past given the present.** A Markov property, exact at every value.

That is the arithmetic behind §23's balance: the factorisation *is* the conditional independence, and the 1,268 is what treating the three parts as free costs. The past constrains only which presents are reachable — q ≤ k — and having spent that, it has spent everything.

**The dependence is monotone and opposed.** The future set is **nested increasing** in the present — 5 ⊂ 10 ⊂ 15 ⊂ 17, each containing the last — while the past set is **nested decreasing** — 33 ⊇ 33 ⊇ 23 ⊇ 8. §12.8.1's Pareto frontier, and the same shape as dw/dh > 0 with dV/dh < 0.

**And the bracket is saturated.** At every value of the present the admissible future set is the *full* interval of the target lattice between its own extremes, [(1,0,0), (3,1,q)] — nothing inside is missing. E(X) = 0 read on the target end.

## 25. The tick, decomposed

The clock is occupancy and the tick is k − g. Over the 1,169 composable cells of Λ₉:

| tick | cells | share |
|---|---|---|
| 0 — reversible | 389 | 33.3% |
| 1 | 540 | 46.2% |
| 2 | 240 | 20.5% |

**The tick has two sources and they are exactly balanced.** k − g = (k − q) + (q − g): something not removed, and something removed but not placed.

| | cells | share |
|---|---|---|
| something not removed, k > q | **430** | 36.8% |
| something removed and not placed, q > g | **430** | 36.8% |

Not approximately — 430 against 430, with the split table its own transpose: (0,1) = 270 against (1,0) = 270, and (0,2) = 80 against (2,0) = 80. **Irreversibility has two independent sources contributing identically.** One is a choice not taken; the other is a capacity that could not receive.

**And Pauli is a minority partner in the tick.** g's ceiling is fixed by counting in 60.2% of composable cells, tied in 29.5%, and by the shell capacity in **10.3%** — with only 6.2% where Pauli holds g down and the transfer would have allowed more. **The arrow of time in this object is overwhelmingly a counting phenomenon**, which §12.9 states in advance: the coupling g ≤ q binds 35.6% of intervals and g ≤ 4f+2 binds 4.9%.

---

# PART VI — WHAT CANNOT BE REMOVED

## 26. Pushback

For a cell x, count the pairs of *other* cells that produce it — J(x) joining to x, M(x) meeting at x. Remove x and that is exactly how many pairs of survivors fail.

| | |
|---|---|
| minimum over all 976 cells | **16** |
| median | 506 |
| maximum | 5,091 |
| mean | 739 |
| **cells removable with no failing pair** | **0** |

**No cell of Λ₈ can be removed without the remainder contradicting the removal.** The weakest is implied back sixteen ways.

**The formula is exact rather than fitted.** J(x) recomputed using only the cells at or below x agrees with the global count on 930 of 930 cells checked; M(x) inside [x, ⊤] on 934 of 934. So J(x) is the number of ways x's own down-set is covered by two proper down-subsets, and M(x) the dual: **pushback is a property of the interval and of nothing outside it.**

Which is why statistics fail — corr(pushback, cells below) = +0.425, cells above +0.454, their product +0.117. §16.8.4 found precisely this for insertion: four statistical measures of a constraint all failed and only a measure of the *tree* succeeded. Same shape, second operation.

**J(x) = 0 exactly on the join-irreducibles and M(x) = 0 exactly on the meet-irreducibles**, both exactly, 17 each with ⊥ and ⊤ excluded — reproducing §8.3's count by a route with nothing to do with Birkhoff.

**And the distribution is U-shaped in rank.** Median pushback runs 3,234 at rank 3, down to 335 at rank 10, back up to 1,555 at rank 20. **An index's resistance to deletion is weakest where it is widest** — rank 11 holds 122 cells and defends each of them least — which is the opposite of the intuition that more neighbours means more redundancy.

## 27. The step law

A single cell cannot leave. The minimum that can is derived rather than measured.

*Derivation.* Let R = [a,b] and suppose z ∈ R with z = x∨y and x, y ∉ R. Since x, y ≤ z ≤ b, being outside R means x ≱ a and y ≱ a, while a ≤ x∨y. In a distributive lattice every join-irreducible is join-**prime**, so a ≤ x∨y forces a ≤ x or a ≤ y — contradiction. Conversely if a is join-reducible, a = u∨v with u, v < a, both under b and neither above a, so u, v ∉ R while u∨v = a ∈ R. Dually for meets and b. ∎

> **X ∖ [a,b] is a sublattice if and only if a is join-prime and b is meet-prime.**
>
> **step(X) = min { |[a,b]| : a join-prime, b meet-prime, a ≤ b, 1 < |[a,b]| < |X| }**

**Corrected by its own test.** The first statement of the criterion used *irreducible* rather than *prime* and disagreed with the truth on **35 of 116,138 intervals** — exactly 17 + 17 + 1, being the intervals [⊥, b] with b meet-irreducible, [a, ⊤] with a join-irreducible, and the whole lattice. Convention excludes ⊥ from the join-irreducibles; the property the proof uses is primeness, which ⊥ satisfies trivially. **With *prime*: 0 disagreements in 116,138 intervals**, exhaustive.

| caps | \|Λ\| | \|J\| = \|M\| | doubly irreducible | **step** |
|---|---|---|---|---|
| (3,3,1,3) | 976 | 17 | **0** | 4 |
| (3,3,1,4) | 1,636 | 21 | **0** | 4 |
| (4,4,1,3) | 1,968 | 19 | **0** | 9 |
| (4,4,1,4) | 3,363 | 23 | **0** | 9 |
| (5,5,1,3) | 3,304 | 21 | **0** | 16 |

At the book's caps the step is a coordinate box free in exactly two coordinates — **n and e, the two shell coordinates, the two ends of the caterpillar** — running from (2,1,3,3,2,1,3,0) to (3,1,3,3,3,1,3,0), and removing it leaves 972 cells with **0 join/meet failures across all 471,906 surviving pairs**.

The step is (n_max − 1)(e_max − 1) at all five settings. That is a pattern across five points and it is **not promoted**: §20.1.2 forbids taking the next term from the pattern the terms make. What is derived is the criterion; a closed form for the minimum over primes is not.

## 28. No cell is doubly irreducible

The two results of §26 and §27 are one fact seen twice.

|[a,a]| = 1 requires a cell that is both join-prime and meet-prime. **Λ has none, at every cap tested** — 17 join-irreducibles, 17 meet-irreducibles, intersection empty. So the pushback floor of 16 and the step of 4 are the same statement: there is no cell whose removal the rest of the index does not contradict, because there is no cell that is irreducible on both sides.

**And the E1 puncture is placed by it.** §12.11.6 removes the one cell nature forbids from the E1 selection rule and reports closure failing by exactly four meets, all four producing the removed cell. Recomputed at cap 20: **0 join failures, 4 meet failures, all four producing (0,0).** Four is not typical — it is near the floor. **The forbidden cell is among the least-defended its index has, and the index still refuses to lose it.**

---

# PART VII — THE ONE COUPLING

## 29. The cut law

Opposed monotonicity — two quantities moving oppositely under one free parameter — appears at least nine times in *The Method 1.3* and this session, and is never grouped: §12.8.1's Pareto frontier, §21.5.2's dw/dh against dV/dh, §12.11.1's *tree or tightness*, §12.11.0.1's fill against surplus, §6.3's calendar, §17.4's coverage against order, §21.10.3's precision against robustness, §29.3.3's Hodge slice, §30.4.1's paradox-freedom against expressive power, and §24 above.

The lattice-internal instances are derivable.

> **At a cut of the constraint graph on coordinate v, each surviving component shrinks if it contains a parent of v, grows if it contains a child of v, and is flat if it contains neither.** Raising v raises the floor on its parents and the ceiling on its children.

**Tested across all seven stages of the tower and every cut: 89 component tests, one violation.** And the violation is at **Λ₉′**, whose constraint graph is the only one in the tower carrying a cycle — f–g–2S′, the tightening §12.11.1 prices at 93 cells and calls *the tree or the tightness*. The law is a theorem about trees and fails at exactly the stage that stopped being one.

**A prior version of this claim was wrong and is withdrawn.** It read *opposition fails at two-parent coordinates*, which holds at Λ₈ and nowhere above. The cause is not two parents: at Λ₈ the coordinate g has two parents **and no child**, so every component holds a parent and every one shrinks. From Λ₉ onward g has the child 2S′ and opposition returns.

## 30. The two-parent coordinate at every stage of the tower

§11.5 names g ≤ min(q, 4f+2) *the one coupling, and it is the Pauli principle* — the only non-product term in the whole expression. The tower confirms it is the only one anywhere.

| stage | \|X\| | two-parent coordinates | cut behaviour at g |
|---|---|---|---|
| Λ₈ | 976 | **g** | all components shrink |
| Λ₉ | 1,654 | g | opposed |
| Λ₉′ | 1,561 | g **and 2S′** | the one law violation |
| Λ₁₀ | 2,535 | g | opposed |
| Λ₁₁ | 13,585 | g | opposed |
| Λ₁₂ | 70,905 | g | opposed |
| Λ₁₃ | 199,130 | g | opposed |

**g is the unique two-parent bound in the entire tower as built.** Every coordinate from the ninth axis to the thirteenth enters with exactly one parent, which is why closure survives thirteen dimensions and forty-seven million ambient cells.

**And the two places a second could have entered are the two places the book records a price.** Λ₉′ makes 2S′ two-parent — 93 cells bought, the tree lost, and the only violation of the cut law in the run. Λ₁₂'s law for K is 2K ≤ 2J_c + 2f with the cell's own f, and §12.11.3.1 records the book substituting f_max to keep one parent and the cylinder.

## 31. Every second bridge, at the top of the tower

§17's twenty candidates at Λ₈ are repeated at Λ₁₃ with sixty-four.

**As built the factorisation over q is exact at Λ₁₃ — defect 0 on 199,130 cells**, with sections 11,470 · 45,880 · 89,700 · 52,080 reproducing §12.11.5's printed table to the cell.

**Fifty-eight of sixty-four second bridges destroy it**, defects from 1,794 to 82,680. The six that do not are the six that reduce the object to a remnant — k ≤ g at 27.1% of the cells, down to k ≤ f at 2.5%. Register 333's caution: a set cut hard enough factorises trivially.

> **The bridge is one-dimensional not because the index has one dimension available, but because the physics supplies one demand and the construction refuses the second.**

Structurally a second bridge is always admissible — closure survives all sixty-four, as §14.4 guarantees for monotone single-coordinate bounds. Physically the tower offers exactly one: **2K ≤ 2J_c + 2f**, core angular momentum to target orbital momentum. Dimensions 1–10 are single-parent laws, dimension 11 takes its bound from k alone, dimension 13 from K alone.

**And q is the unique cut vertex separating the two ends.** The path from g to K runs **g — q — k — 2J_c — K**, and removing q disconnects them; the cycle the tight K would create is **K — 2J_c — k — q — g — f — K**, length six. The forbidden bridge does not add a new connection between the ends. It adds a *second* one, which is what a tree forbids.

## 32. The tight K, and a discrepancy

§12.11.5 states that the tight two-parent K breaks the factorisation by **2,475 cells, 3.5% of the product**. Recomputed here by four disjoint routes:

| route | Λ₁₂ | Λ₁₃ |
|---|---|---|
| cells cut by restoring the law | **15,150** | **45,450** |
| factorisation defect once restored | **15,150** | **45,450** |
| per-section defect, summed | — | 2,934 + 11,736 + 22,140 + 8,640 = **45,450** |
| three alternative A/B splits | — | 113,325 · 405,715 · 428,340 |

Four routes agree; **none produces 2,475**. What does is arithmetic on the stated percentage: 3.5% × 70,905 = **2,482**. So the two figures printed side by side appear to be one measurement written twice, which is §2.8's vacuous identity — computed along one path, it cannot disagree with itself.

**The rebuild is cleared under §4.1.** It reproduces all seven tower cell counts, the four-cap sweep, the composition closure at 41,682 pairs, and §12.11.5's own four sections exactly.

**The true fraction is 21.4% at Λ₁₂ and 22.8% at Λ₁₃** — and it is not constant: at f_max = 2 the cost rises to **35.3%**. The price of keeping the tree grows with the shell the index carries, which is §12.11.1's density behaviour in a second guise and which neither the book nor this session had before.

Two possibilities remain and the triangulation does not settle between them: 3.5% may measure something narrower than *the product* that this rebuild has not reconstructed, or the cylinder costs six times what the section states. Recorded as a discrepancy to localise rather than a correction to claim.

---

# PART VIII — TWO INDICES

## 33. The reversal

Reversing time is not a sign change. Extending k, q and g below zero was tested at three settings — k ≥ 0, then all three to −1, then to −2 — and the object stays closed (0 join/meet failures) while **0 cells have g > k and 0 steps raise occupancy**, the lattice growing from 976 to 2,691. Neither §7.3's closure proof nor the occupancy law uses positivity. **A negative occupancy is not a reversed one; it is a lower one.**

The reversal is a different object. Exchange the two ends of Λ₉ — (n,ℓ,k,2S) ↔ (e,f,g,2S′), transfer unchanged:

| | |
|---|---|
| \|Λ₉\| | 1,654 |
| \|rev(Λ₉)\| | 1,654 |
| reverse(Λ₉) closed | **yes**, 0 failures |
| **\|Λ₉ ∩ rev(Λ₉)\|** | **389** |

**The reversed index is a lawful closed index of the same size and it is not Λ₉.** That is §8.4's failure of self-duality read temporally: the two are both lawful and simply not the same object.

## 34. The intersection is a groupoid

Every cell of the intersection satisfies **g = q = k** — total transfer, nothing left behind — and the intersection is the reversible region twice over: it is exactly the 389 morphisms carrying a reverse.

| position | cells | join fail | meet fail | E(X) |
|---|---|---|---|---|
| Λ₉ forward | 1,654 | 0 | 0 | **0** |
| rev(Λ₉) backward | 1,654 | 0 | 0 | **0** |
| **Λ₉ ∩ rev(Λ₉)** | **389** | **0** | **0** | **0** |

**And it is a groupoid, entire.** 4,887 composable pairs with zero closure failures; **all 33 objects carry a genuine identity; all 389 morphisms have a two-sided inverse.** Λ₉ is a category and a groupoid only at its top; the intersection *is* the groupoid.

It carries its own transfer and factorises exactly — Σ_q |A(q)|·|B(q)| = 389 against 389, defect zero — so the whole construction reproduces one level down.

> **The second present definable from the forward and backward indices is the region in which time has no direction, and it is 23.5% of Λ₉.**

This unifies two results reported separately. §7's cycles were confined to level sets of occupancy with every step conservative; conservative is g = q and the level-set condition is k = g. **The intersection is that condition stated as an object rather than as a property of paths.**

## 35. The union does not exist

| position | cells | join fail | meet fail | E(X) |
|---|---|---|---|---|
| Λ₉ ∪ rev(Λ₉) | 2,919 | **360,000** | **470,625** | **2,857** |

Three of the four positions exist and the fourth does not. **The top is missing.** A present is definable from the past and future indices; the thing containing both is not.

That is not a technicality. §17's E1 admits cells when their joins and meets fall back inside; here **2,857 further cells** would have to be admitted, and §16.8.4's amplification is exactly that cost. **A structure containing both directions of time is not available at any price the index recognises** — only a structure containing their agreement.
