## The string partition function

**The generating function of string state degeneracies, read as an index with multiplicity.** Where Λ's cells are present or absent, this index's cells carry a count — the number of string states at each level. §31.2.3.

| coordinate | values | bound |
|---|---|---|
| mode occupation | ℤ₊ per oscillator (n, i), n ≥ 1, i ∈ 1…24 | independent |
| level | N = Σ n · occ(n, i) | the graded total |

**E = 0**, because the modes are independent. The partition function ∏ₙ (1 − qⁿ)⁻²⁴ = Σ d(N) qᴺ counts the states at level N as the 24-coloured partitions of N — a part of size n available in each of the 24 transverse dimensions — giving d(1) = 24, d(2) = 324, d(3) = 3,200, and d(14) = 156,883,829,400. The admissible set of occupation vectors is a full product, each oscillator's occupancy free of every other's, and a product closes trivially: ℛ adds nothing, so E = 0. It closes for the reason dual to Λ's — Λ's coordinates couple along a tree and close in one pass; the string's modes do not couple at all, which is the degenerate case of the three closure conditions where independence stands in for the tree. The two are the same theorem at its two ends: an index closes when its coordinates are free, and it closes when they couple only along a tree, and nothing between.