# Rewrite — "The shape — a cylinder over the transfer" (source §12.1–§12.10.2; prose revision, numbering left at source)

**Placement:** Part I — The Lattice. **First of three reader chapters split from source Chapter 12** (the shape; the tower; time). This is the shape. **Numbering left at source values** (renumber-last). Per standing treatment: every result kept; self-audit/self-cross-reference cut (the §12.8.1 "the book presents as a fact about brackets," the §12.9 "reports both without connecting them," the §12.10.2 "untested when written / since answered / recorded in Q"). Proofs pointed to the Mathematical Compendium via [MC-NN]. Void↔transition watch: §12.10's ninth axis emerges from fibre asymmetry (a coordinate added by observation) — noted, not a grounding hit.

---

## 12. The shape — a cylinder over the transfer

Λ has a shape, and it can be computed rather than drawn. This chapter finds it: a cylinder over the transfer coordinate, whose every cross-section is itself a closed lattice, and whose asymmetry reveals a coordinate the index had not been carrying.

### 12.1 A cylinder, not a Möbius band
Λ's derived quantities fall into two classes, exchanged under the map ν ↦ ν⁻³:

| ascending — rise up a series | descending — fall up a series |
|---|---|
| e, ν, V | T, r, δ, spacing, w |

The sign structure is **bipartite**, and a bipartite structure can never produce an odd number of orientation reversals. Verified exhaustively: zero reversing loops among all cycles of length 3 to 5.

> Λ is orientable. It is a cylinder.

And that is a reason, not an absence of evidence. Both routes to a Möbius band are closed: a non-monotone quantity has *undefined* edges rather than reversing ones, and a quantity independent of ν has *no* edge. There is no third option. [MC-17]

![Figure 12.1](figures/figure-12.1.png)

*Figure 12.1. The object. Ascending quantities rise up a series, descending ones fall, and the two are exchanged under ν ↦ ν⁻³. The sign structure is bipartite, so no traverse can reverse orientation an odd number of times — the surface is a cylinder, not a Möbius band, and the reason is structural rather than an absence of evidence.*

### 12.2 "Over ν," not "graded by ν"
ν grades every chain of Λ, but it grades Λ itself nowhere — 24 of 70 comparable pairs have ν decreasing. That near-miss is the structure in a sentence: the bracket of Part V operates along chains *because that is exactly where ν is a grading*.

The name follows: **the Lach Cylinder — a hydrogenic cylinder over ν, and over the transfer.** Not *graded by*. *Over.*

### 12.3 One scale, and one exception
Height goes as ν⁻², the metric as ν⁻³, and the only linearly rising quantity in the whole structure is the price of a guarantee, derived in Chapter 23.

### 12.4 The loop closes
Λ₈ decomposes ν and gains dimension; the bound lattice recomposes it and sheds dimension, closing the loop at dimension 1 = log r = −3 log ν, with a residual of 8.9 × 10⁻¹⁶. Two sides of one object, not two passes over it.

### 12.5 What Λ is a property of
Λ is a property of the hydrogenic limit; the quantum defect δ is the entire remainder.

> Prediction lives only in the remainder.

This is why perfecting the index moves nothing — and why that is a theorem rather than a disappointment. Part III proves it; Part V measures what is left. In its sharpest form: the reason Λ is not predictive is not that it predicts poorly, but that **a complete index has nothing to predict** — the cells it could propose are exactly those its structure admits and its extension denies, and for Λ that set is empty. Completeness and predictiveness are alternatives, not a spectrum.

### 12.6 The cylinder is a fibration, and its fibres are two-body
The tree has two ends. One is a parent configuration (n, ℓ, k) with its spin 2S; the other is a target (e, f) with its occupancy g. **They meet at q, the number of electrons transferred.** That is the shape of a two-body problem — two objects and a coupling.

### 12.6.1 It does not factorise, and then it does
As a bare product it fails: |A| × |B| × |q| = 2,244 against 976, because the two ends are coupled twice over — q ≤ k ties the transfer to the parent, g ≤ q ties the target's occupancy to the transfer. **Conditioned on the coupling, they separate exactly:**

| q | \|A(q)\| | \|B(q)\| | product |
|---|---|---|---|
| 0 | 33 | 5 | 165 |
| 1 | 33 | 10 | 330 |
| 2 | 23 | 15 | 345 |
| 3 | 8 | 17 | 136 |

      |Λ| = Σ_q |A(q)| × |B(q)| = 976, exactly.

That is how a two-body problem separates — into centre-of-mass and relative motion — with q playing the conserved coupling. [MC-18]

### 12.6.2 Which names the cylinder
The base is q, the axis along the cylinder; the fibre is A(q) × B(q), the cross-section at each q; and each cross-section is itself a product of two lattices. The cross-sections **165, 330, 345, 136** are the cylinder's profile, computed rather than drawn.

![Figure 12.2](figures/figure-12.2.png)

*Figure 12.2. Cross-sections of the tower cylinder at each transfer, on a √-cell scale — Λ₁₃ solid, Λ₈ dashed inset. Every section is itself closed; the tower of the next chapter widens each without breaking one.*

### 12.7 The fibres, in closed form
Each side of the cylinder has its own expression, and they are different shapes:

      A_q(z) = Σ_{n=1}^{3} zⁿ Σ_{ℓ=0}^{min(n−1,1)} z^ℓ Σ_{k=max(q,1)}^{min(4ℓ+2,3)} z^k · (1 − z^{min(k,3)+1})/(1 − z)
      B_q(z) = Σ_{e=1}^{3} z^e Σ_{f=0}^{min(e−1,1)} z^f · (1 − z^{min(q,4f+2)+1})/(1 − z)

Both verified against enumeration at every q: A_q(1) = 33, 33, 23, 8 and B_q(1) = 5, 10, 15, 17. [MC-19]

### 12.7.1 And they are not the same tree
A_q is a caterpillar — n — ℓ — k with 2S pendant at k; B_q is a plain path — e — f — g, capped by the base. The whole lattice is a caterpillar because it is these two glued at q, with the pendant on the A side only.

### 12.7.2 A tower of fibrations, terminating in boxes

| level | base | fibre |
|---|---|---|
| Λ | q | A_q × B_q |
| A_q | k | (n, ℓ)-set × 2S-chain |
| B_q | f | e-set × g-chain |

Three levels, and at the bottom every fibre is a product of chains — a box — with the closed form Box(a,b)(z) = ∏ᵢ z^{aᵢ}(1 − z^{bᵢ−aᵢ+1})/(1 − z).

### 12.8 What the fibre table says
The counts 165, 330, 345, 136 carry more than their sum.

**A Pareto frontier inside the lattice.** |A_q| falls 33, 33, 23, 8 while |B_q| rises 5, 10, 15, 17: raising the transfer costs the parent and pays the target, monotonically, and no q improves both. It is the same shape as the bracket's dw/dh > 0 with dV/dh < 0 in Part V — there a fact about brackets, here a fact about the index itself.

**A most-probable transfer.** The fibre peaks at q = 2 with 345 cells — 35.3% of Λ — and the sequence is log-concave, hence unimodal. The mean transfer across all admissible configurations is ⟨q⟩ = 1.4631, with standard deviation 0.930.

**An eight-to-three compression that loses no count.** Λ's F has eight variables; the shape has three, and S(1, 1, 1) = 976. It is not a projection that forgets cells but one that forgets *which* coordinate inside each side and keeps *how many* — a general fact about caterpillars, which reduce to (base, left, right) whatever their length.

**Every cross-section is itself closed and modular.** For every q, both sides A and B are closed, modular, and have E(X) = 0. The shape is not a cylinder over an arbitrary set; it is a cylinder whose every cross-section satisfies this book's own law. And that does not follow from Λ being closed — a closed index could in principle have defective slices that cancel in the total. Here none do, which is a new invariant: E(Λ) = 0 and E(A_q) = E(B_q) = 0 for every q. [MC-20]

### 12.9 Every other shape the lattice contains
**Intervals.** The interval [x, y] is a box exactly when no constraint binds across it — y_i ≤ f(x_j) for every constraint i ≤ f(j). Exact on 60 of 60 tested, and only 27% of random intervals qualify; the other 73% are where the physics is active. The binding rates rank the constraints:

| constraint | binds |
|---|---|
| g ≤ q | 35.6% |
| q ≤ k | 33.0% |
| g ≤ 4f+2 | 4.9% |

The most active constraint is the coupling; the least is the Pauli bound — which is why it is also the cheapest to violate (§16.8). Two independent measures, one answer.

**Rank levels.** Eighteen antichains, the largest 122 at rank 11 — the biggest set of configurations no two of which can be reached from each other by adding electrons. Λ is exactly eight times its widest level.

**Maximal chains.** A distributive lattice is J(P), and its maximal chains are the linear extensions of P. With seventeen join-irreducibles and a chain of length seventeen, e(P) = 1,113,045,672. The seventeen generators and the chain length of seventeen are the same seventeen. [MC-21]

**And one shape absent.** No Möbius band, no cycle, no non-planar minor — the constraint graph is a tree, so there is nothing to twist and nothing to close. The cylinder of §12.1 follows by construction, not by search.

### 12.10 An axis the index did not carry, and now does
A_q carries 2S, a spin label on the parent; B_q carried none. The index had recorded the parent's spin and not the target's. That was never a closure defect — the reconstruction cannot see a coordinate that was never supplied — but an axis the extension admits, and the asymmetry of the two fibres is what made it visible.

Built by the same construction: the parent's spin is bounded by the parent's capacity, 2S ≤ k, so the target's is bounded by the target's, 2S′ ≤ g — one pendant, on the other fibre, by the identical rule. This gives Λ₉:

| | Λ₈ | Λ₉ |
|---|---|---|
| cells | 976 | 1,654 |
| box | 6,912 | 27,648 |
| E(X) | 0 | 0 |
| sublattice | yes | yes |
| rank-modular | 475,800 pairs | 200,000 tested, 0 violations |
| constraint graph | a tree | a tree — 2S′ attaches as a leaf |
| F(1) | 976 | 1,654 |
| F(−1) | 2 | 2 |
| rank levels | 18, widest 122 at 11 | 21, widest 185 at 12 |
| log-concave | yes | yes |

And Λ₈ is the exact projection of Λ₉ — 976 cells, identical — with fibres of one to four preimages, mean 1.69. The extra coordinate carries real information.

The bound 2S′ ≤ g was built by analogy rather than read from spectroscopy, so it raised a genuine physical question: whether it is the correct selection rule for a target's spin. The lattice closes regardless — but closure is not physical confirmation. Exact vector coupling has since confirmed 2S′ ≤ g as a true bound, with zero violations over every fibre, and shown it is not tight. The construction of Λ₉ by the same rule, and the next dimension it opens, is the subject of the following chapter.