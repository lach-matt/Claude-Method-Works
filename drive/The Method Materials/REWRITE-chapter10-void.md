# Rewrite — Chapter 10 "The void" (prose revision; numbering left at source values)

**Placement:** Part I — The Lattice. Follows "The arithmetic encoding." **Numbering:** per the working rule, chapter/section/figure numbers and all cross-references are LEFT AT CURRENT SOURCE VALUES; the whole book is renumbered in one dedicated pass after the prose is finished. (This chapter is old Ch 10 → new Ch 8, and its refs to Ch 12/§12.11 etc. resolve then.) Per standing treatment: every result kept; self-correction cut (the "construction said seven and needed eight / register 301" audit); the time paragraph kept as subject matter; §10.2's correlation given its correct shared-coordinate explanation (not "two origins," which collided with Chapter 5's four physical origins and mis-stated the cause), with the full correlation analysis pointed to the Mathematical Compendium.

---

## 10. The void

Between two cells sits a box — the product of the coordinate ranges they span. Not all of that box is Λ. The cells of the box that are *not* in Λ are its **void**:

      void(x, y) = ∏ᵢ(|Δᵢ| + 1) − |[x∧y, x∨y] ∩ Λ|

### 10.1 What the void is made of
The excluded cells are exactly those a physical law forbids: barred by Pauli (k > 2(2ℓ+1), or g over its cap), by the hydrogenic bound (ℓ ≥ n, or f ≥ e), or by counting (q > k, or g > q). Nothing else is missing, and nothing forbidden survives.

      The void is the shadow of the exclusion principle.

### 10.2 Its size, and its stability
The void-free fraction — the share of boxes that lie entirely inside Λ — is **27.7–30.1% across 776 million pairs** and a seventeenfold range in cell count. It is stable, with no trend: the object's density does not drift as the caps grow.

**The constraints are correlated, and the correlation has a structural cause rather than a coincidental one.** Taken one at a time, the seven constraints are satisfied 67–94% of the time. If they were independent, the chance of a box satisfying all seven would be their product — 20.19%. The measured figure is **30.13%**, a factor of **1.49** higher. The constraints are not independent because they **share coordinates**: the same coordinate appears in two neighbouring constraints — q in both q ≤ k and g ≤ q, k in both k ≤ 2(2ℓ+1) and q ≤ k — so satisfying one constraint makes its neighbour more likely to hold. This is a fact about the constraint *graph* — the tree of Chapter 5, in which each coordinate is tied to the next — and not about the four physical origins. The origins say where each constraint comes from; the sharing of coordinates along the tree says why the constraints move together. The full correlation analysis, with the 1.49 factor derived from the tree's overlap structure, is carried in the Mathematical Compendium [MC-10].

**And Λ carries time, in the only form a transition can carry it.** The source end of a transition is a *before*, the target end an *after*, and q — the transfer — is the amount that changed between them. The constraint tree, read from one end to the other, *is* past — change — future. A date would add nothing, because a transition is a type and types are not dated; what a transition can have is a predecessor and a successor, and §12.11.0 shows Λ₉ has both. This is the composition reading of Chapter 6, seen along the tree: time enters as an order between cells, not as a stamp on one.

**There is also an eighth condition, and it is of a different kind — a definition, not a bound.** The seven constraints are limits on how far one coordinate may reach given another. The eighth, k ≥ 1, says only that a source subshell must hold at least one electron. Without it the tree collapses — with k = 0 the quantities 2S, q and g are all forced to zero, and twenty-five cells survive that are not transitions at all, but states. The cells of Λ are transitions, not states (§13.2), and k ≥ 1 is that fact written as a condition. With it, the count is 976 and the bounding box 6,912.

![Figure 10.1](figures/figure-10.1.png)

*Figure 10.1. The void-free fraction across a seventeenfold range in cell count, computed exhaustively over 776 million pairs. Stable at 27.7–30.1%, with no trend — the object's density does not drift as the caps grow.*

### 10.3 Containment in seven comparisons
A whole box lies inside Λ exactly when hi_i ≤ φ(lo_j) holds for each of the seven constraints — seven comparisons, independent of how many cells the box contains. Verified against direct enumeration on 3,168 pairs. This is the O(1) membership test the retrieval chapters rely on.

### 10.4 The count, with no sieve
Because the constraint graph is a tree, the number of Λ-cells in a box factorises — it can be summed coordinate by coordinate, with no correction term:

      |box ∩ Λ| = Σ over n, ℓ, k, q, e, f of
                  [ℓ ≤ n−1][1 ≤ k ≤ 2(2ℓ+1)][q ≤ k][f ≤ e−1] · #{2S ≤ k} · #{g ≤ min(q, 2(2f+1))}

with the two leaves in closed form:

      #{2S} = max(0, min(hi₇, k) − lo₇ + 1)
      #{g}  = max(0, min(hi₆, q, 2(2f+1)) − lo₆ + 1)

Verified against direct enumeration on eight random intervals. **No Möbius function, no 2⁷-term inclusion–exclusion** — a tree has no cycles for a sieve to correct. And that is a general statement about indices, not a special feature of this one:

      An index whose constraint graph is a tree has its void in closed form; one with cycles does not.

The full factorisation, and the proof that treeness is exactly the condition for a sieve-free count, are carried in the Mathematical Compendium [MC-11].
