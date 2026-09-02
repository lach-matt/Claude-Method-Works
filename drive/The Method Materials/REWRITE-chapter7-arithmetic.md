# Rewrite — Chapter 7 (was Chapter 9), "The arithmetic encoding"

**Placement:** Part I — The Lattice, fourth chapter. Turns Λ into arithmetic. Old Ch 9 → 7; §9.x → §7.x; Figure 9.1 → 7.1. Per standing treatment: every result kept; self-audit cut (the §9.2 "the book states this three times / Register 438" self-reconciliation); proofs pointed to the Mathematical Compendium via [MC-NN] tokens keyed to OWED-EXPANSIONS.md. Cross-refs to chapters not yet reached carry their new numbers (§12.11 → §10.11; §22.1, §27, §14.3, §18.x resolved at their own passes).

---

## 7. The arithmetic encoding

Assign the *i*-th coordinate the *i*-th prime, and read a cell as a single integer:

      N(x) = ∏ᵢ pᵢ^{xᵢ}

The lattice becomes arithmetic — not by analogy, but exactly:

| lattice | arithmetic |
|---|---|
| x ≤ y | N(x) divides N(y) |
| x ∨ y | least common multiple |
| x ∧ y | greatest common divisor |
| rank, Σ xᵢ | Ω(N), prime factors counted with multiplicity |

**Λ is a sublattice of the divisor lattice of a single integer.** Every order relation, join, and meet in the whole object is a fact about divisibility, and can be computed by multiplying and factoring integers.

### 7.1 Two classical functions appear as lattice quantities
The rank of a cell is the number of prime factors of its integer, counted with multiplicity:

      rank(x) = Ω(N(x)) — verified on all 976 cells.

And the number of *distinct* primes is bounded by the order dimension, tightly:

      ω(N(x)) ≤ dim(Λ)

because N(x) uses at most one prime per coordinate, so its distinct-prime count cannot exceed the number of coordinates. The two classical prime-counting functions of analytic number theory — Ω, counting with multiplicity, and ω, counting distinctly — turn out to be Λ's rank and a bound on its dimension. Neither was placed there. [MC-07]

### 7.2 The occupancy measure
Between any two cells, whether or not either order relates them, there is an interval — the cells lying between their meet and their join — and the method returns its size:

      d(x, y) = τ( lcm(N(x), N(y)) / gcd(N(x), N(y)) )

with τ the divisor-counting function. This is the quantity the object uses in place of a distance, and it works exactly where an ordinary distance fails. The coordinate orders are partial and share only 0.3% of pairs, so for most pairs no single order relates x to y at all. But *every* pair has a meet and a join, so every pair has an interval — the interval is total where the order is partial. **That is why d(x, y) is defined for pairs the order cannot compare.**

**d(x, x) = 1**, because τ(1) = 1 — and that is not a convention. A point has no volume, but it is one point and it counts itself; the measure counts occupied cells, and a cell is occupied.

The measure has five equivalent forms, verified 500/500 and 2,000/2,000:

| | form | |
|---|---|---|
| 1 | \|[x∧y, x∨y]\| | the interval count itself |
| 2 | ∏ᵢ(\|xᵢ − yᵢ\| + 1) | coordinate form |
| 3 | τ(N(x)N(y)/gcd²) | two integers |
| 4 | τ(a·b), where N(x)/N(y) = a/b in lowest terms | one rational input |
| 5 | ∏_p(\|v_p(ρ)\| + 1) | p-adic |

Its properties make log d an ordinary metric: symmetric; d ≥ 1 with equality only when x = y; a multiplicative triangle inequality d(x, z) ≤ d(x, y)·d(y, z), holding on all 4,000 tested triples; so that log d is an ℓ¹ metric. The balls are hyperbolic — a ball's boundary satisfies (1 + Δ₁)(1 + Δ₂) = D — and each axis is a log-distorted chain, its first step log 2 and its tenth step log(11/10). The equivalence of the five forms and the metric properties are established in the Mathematical Compendium [MC-08].

![Figure 7.1](figures/figure-7.1.png)

*Figure 7.1. The occupancy measure. d(x, y) counts the cells in the interval between two points, and equals τ(lcm/gcd) of their prime encodings. Balls are hyperbolic; log d is an ordinary ℓ¹ metric; and d(x, x) = 1 because a point counts itself.*

The measure is what lets the object speak about pairs its orders cannot compare: between any two cells there is an interval, and the interval — not a single number relating them — is what the method returns. An interval carries less than the coordinates do, not more, which is why this is a bound on where something already is, never a proposal of an unlisted cell.

### 7.3 The Möbius function in closed form
Because Λ is the down-set lattice of a seventeen-element poset P, its Möbius function is read directly off P rather than computed by recursion:

      μ(x, y) = (−1)^{|y∖x|}  if y∖x is an antichain in P, and 0 otherwise.

Verified against the recursive definition on 47 comparable pairs, with values only in {−1, 0, +1}. No recursion is needed for a 976-cell lattice; the answer comes from a seventeen-element poset. [MC-09]

And there is an exact transfer condition to the arithmetic side: the lattice Möbius value and the arithmetic (divisor-lattice) Möbius value agree **if and only if** the interval is a void-free unit hypercube — 60 void-free pairs all agree, 56 void-bearing pairs all disagree, no mixed case, decidable in seven comparisons. The void that makes the two disagree is the subject of the next chapter.
