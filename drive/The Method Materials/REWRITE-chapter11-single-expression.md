# Rewrite — Chapter 11 "The single expression" (prose revision; numbering left at source values)

**Placement:** Part I — The Lattice. The mathematical high point of the part: Λ written in seven languages and as one generating function. **Numbering left at source values** (old Ch 11 → new Ch 9; §12.11→§10.11 etc. resolve in the final renumber pass). Per standing treatment: every result kept; self-audit and self-reconciliation cut (the "binary belongs, the admission test settles it / §17 condition" adjudication; the "One cost, stated" Appendix-D trade; the "P20 already said this / §32.4.1 says it from a third side"; the §11.8 "these three separately-reported facts are one thing" reconciliation). Proofs pointed to the Mathematical Compendium via [MC-NN]. The seven-languages / P21 material is kept as content, with the "P21 requires" self-citation trimmed to plain statement.

---

## 11. The single expression

Every cell of Λ can be written in one expression — and the reason one exists is worth more than the expression itself.

### 11.1 In six languages, and a seventh
Λ is a single object, and it can be stated in each of the standard mathematical languages, with every statement naming the same 976 cells:

| language | the expression | \|Λ\| |
|---|---|---|
| order | the fixed point of ℛ — the least set closed under ∨ and ∧ satisfying its own recovered bounds | 976 |
| algebra | ℤ⁸ ∩ {x : Ax ≤ b}, with A a 7×8 matrix, two non-zeros per row | 976 |
| geometry | the lattice points of a polytope whose constraint graph is a tree; the count factorises | 976 |
| analysis | F(1, …, 1) for the multivariate generating function | 976 |
| information | the set whose description length, given its closure, is zero bits | 976 |
| logic | {x ∈ ℤ⁸ : χ(x) = 1}, with χ a product of seven Heaviside steps | 976 |

All six agree exactly. That a definition holds in every language, and in their combinations, is one of the book's standing requirements, and Λ is where it is met most completely.

### 11.1.1 A seventh, in binary
There is a seventh statement, in binary, and it earns its place by distinguishing something the other six do not:

> **binary** — Λ is the set of 976 words in {0,1}¹⁷ that are down-sets of the seventeen-generator poset; **join is bitwise OR and meet is bitwise AND**, with zero failures over all 475,800 pairs. The map cell ↦ word is a bijection.

The seventeen bits are the seventeen generators of §8.3. A bit is a generator: bit *i* is set in a cell's word exactly when generator *i* lies beneath that cell — one yes-or-no question, *is this generator under you?* — and a cell is the set of its answers, nothing more. This is Birkhoff's correspondence in the language a machine reads: not new mathematics, but the one statement that says the cells **are** bit-vectors, which makes join and meet machine primitives rather than definitions.

And in this language the thesis of Chapter 16 becomes a number:

| | |
|---|---|
| bits carried per cell | 17 |
| bits needed to index 976 cells | 9.93 |
| **surplus** | **7.07 bits per cell** |

**The bits are not free of one another.** The twenty covering relations of the generator poset are twenty implications between bit positions: if generator *j* covers generator *i*, then bit *j* set forces bit *i* set. Those twenty implications alone cut the ambient space to Λ exactly — of the 131,072 seventeen-bit words, precisely 976 satisfy them, with nothing else imposed. So the surplus is not spare capacity, and no bit is removable; the seven surplus bits live in the twenty implications, which is where redundancy lives in a closed index. [MC-12]

**In that language Λ is a circuit.** The seventeen generators are input lines, the twenty implications are gates, join is OR and meet is AND. The twenty gates accept 976 words of the 131,072 available — exactly Λ — at depth five. Available: AND, OR, implication. Absent: NOT, feedback, memory.

> **Λ₈ is a monotone boolean circuit. It decides membership; it does not compute a function of successive inputs.**

And the ninth axis is where that changes. Λ₉ is closed under composition — 41,682 pairs, associative — so it has states, transitions, and a composition law: **Λ₈ is a circuit; Λ₉ is an automaton**, still negation-free and so still not general, but no longer a thing that answers once. The tower's first step is the step from a decider to a machine, and it was taken to carry seniority.

Written out, the logic and algebra statements are:

**logic:**

      χ(x) = H(n−1−ℓ) H(4ℓ+2−k) H(k−q) H(k−2S) H(e−1−f) H(4f+2−g) H(q−g)

**algebra**, the seven rows of A: ℓ − n ≤ −1 · k − 4ℓ ≤ 2 · q − k ≤ 0 · 2S − k ≤ 0 · f − e ≤ −1 · g − 4f ≤ 2 · g − q ≤ 0. **Every row has exactly two non-zero entries**, and that single property is what makes the constraint graph a tree.

**analysis**, the rank polynomial:

      F(z) = z³(z¹⁷ + 4z¹⁶ + 10z¹⁵ + … + 122z⁸ + 121z⁷ + … + 5z + 1)

with F(1) = 976, F′(1)/F(1) = 11.0666, and F(−1) = 2 — the asymmetry of §8.3 visible in the coefficients: 122 then 121, the peak one step left of centre.

### 11.2 And in their combinations
The combinations name real objects, not analogies — ten were tested and ten hold:

| combination | statement |
|---|---|
| order + algebra | gcd(N(a), N(b)) = N(a∧b), and lcm = N(a∨b) |
| order + analysis | F′(1)/F(1) = the mean rank, 11.0666 |
| order + geometry | box − Λ = the void, 6,912 − 976 = 5,936 |
| geometry + analysis | F is not palindromic ⟺ the poset is not self-dual |
| order + information | E_bits = log₂ C(\|ℛ(X)\|, E) = 0 |
| algebra + information | the description is seven rows of two non-zeros — the whole index |
| logic + algebra | χ as a product of Heaviside steps selects exactly 976 |
| logic + analysis | the coefficient function of F is χ |
| analysis + information | log₂ F(1) = 9.93 bits to name one cell |
| algebra + geometry | the integer points of the polytope are the lattice, exactly |

The last makes "single expression" literal: the coefficient of z₁ⁿ…z₈^{2S} in F is 1 if the cell exists and 0 if it does not. F and χ are the same function written twice. [MC-13]

### 11.3 The expression
      F = Σₙ z₁ⁿ Σ_{ℓ≤n−1} z₂^ℓ Σ_{k≤4ℓ+2} z₃^k · [Σ_{S≤k} z₈^S] · Σ_{q≤k} z₄^q Σₑ z₅^e
          Σ_{f<e} z₆^f Σ_{g≤min(q,4f+2)} z₇^g

Set every z = 1 and it gives the count. Set every z equal and it gives the rank polynomial. The coefficient of z₁ⁿ…z₈^{2S} is 1 if the cell exists and 0 if it does not.

> The coefficient function of F is χ. F is one expression containing every cell of the lattice and nothing else.

![Figure 11.1](figures/figure-11.1.png)

*Figure 11.1. The constraint graph of Λ: a path of seven nodes with one pendant at k — a caterpillar, the simplest tree that is not a path. That shape is why a single left-to-right nesting exists with one bracketed factor. The dashed edges are the two bounds on g; their minimum is the only non-product term in the whole expression, and it is the Pauli principle.*

### 11.4 The shape of the tree
      n — ℓ — k — q — g — f — e, with 2S pendant at k

Not a generic tree but a **caterpillar** — a path of seven nodes with one pendant, the simplest tree that is not a path. That is why a linear nesting exists with a single bracketed factor. A branching tree would require nested brackets; a cycle would require inclusion–exclusion.

### 11.5 The one coupling, and it is the Pauli principle
Every bound is a single inequality except one: g ≤ min(q, 4f+2). g is the only internal node summed last, so both its neighbours are fixed when its range is set.

**Remove the coupling and 976 becomes 1,000.** The excluded 24 cells all have f = 0 and g = 3 — three electrons in an s orbital.

> Every other bound in this lattice is a counting or ordering fact. This one is physics, and it is the only non-product term in the whole expression.

And it is recovered, not assumed: ℛ(Λ) = Λ rebuilds all 976 cells from the cells alone, so a reader given only the cell list would deduce g ≤ 2(2f+1) without being told it.

### 11.6 The detachable factor
2S is a leaf, so its sum closes geometrically and multiplies out:

      [Σ_{S≤k} z₈^S] = (1 − z₈^{k+1})/(1 − z₈)

**Spin multiplicity is algebraically inert here.** It scales every cell count by (k+1) and changes no structure — which is why removing it leaves E(X) = 0 unchanged: Λ has 976 cells and E = 0; with 2S removed it has 319 cells and E = 0; and every seven-coordinate cell carries exactly k+1 spin values. The count is verified; the reason is that 2S is a leaf. [MC-14]

### 11.7 Why a closed expression exists at all
Three structural facts combine:

| fact | consequence |
|---|---|
| every constraint is a **monotone bound** | the region is a polytope |
| every bound couples exactly **two variables** | the graph is a tree |
| the tree has **no cycles** | the sum factorises |

Remove any one and no such expression exists. A sum bound breaks the first — 89,864 join failures were measured when one was tried. A three-variable constraint breaks the second. A cycle breaks the third, and 2^d inclusion–exclusion terms return. [MC-15]

> "All the information in one expression" is not a curiosity. It is what closure buys, and it is the strongest available statement of what E(X) = 0 means: the expression is the index, and the cells are its coefficients.

![Figure 11.2](figures/figure-11.2.png)

*Figure 11.2. The rank polynomial F(z), read forwards as bars and backwards as the dashed line. They part at rank 1 — 5 against 4 — and never rejoin. A rank polynomial is palindromic exactly when the poset is self-dual, so this one picture carries both facts of §8.3: the asymmetric rank sequence, and the 8 of 976 cells that survive reflection.*

### 11.8 The rank polynomial and the asymmetry
A rank polynomial is palindromic if and only if the poset is self-dual. Λ's is not:

      forwards:  1, 5, 15, 34, 59, 87
      backwards: 1, 4, 10, 21, 37, 57

The two part company at rank 1 — 5 against 4 — and never rejoin. The asymmetry that §8.3 measures two ways (only 8 of 976 cells survive x → max − x; the rank sequence is skewed) is this one fact, and F(−1) = 2 is a third measurement of it.

**F(−1) = 2 has a cause.** A self-dual graded poset gives F(−1) = 0; Λ gives 2, and the reason is the tree. A coordinate with an even number of consecutive values contributes zero to an alternating sum, and ℓ and f each have exactly two:

| factor at z = −1 | value |
|---|---|
| Σ(−1)ⁿ, n = 1…3 | −1 |
| Σ(−1)^ℓ, ℓ = 0…1 | 0 |
| Σ(−1)^e, e = 1…3 | −1 |
| Σ(−1)^f, f = 0…1 | 0 |

If the coordinates were free, the alternating sum would vanish — F_box(−1) = 0 exactly. But the constraints couple ℓ to n and f to e, so the vanishing factors never appear free, and a residue of 2 survives. F(−1) = 2 measures the tree's asymmetry by a third route. [MC-16]
