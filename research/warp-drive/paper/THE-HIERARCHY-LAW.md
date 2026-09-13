# The Hierarchy Law of Mathematical Languages

**Eight clauses on five closure operators over a finite index — fully derived, with provenance.**

**Matthew Lach** · Independent Researcher · 12 September 2026

---

## §0 · Scope, and what this document is not

This derives a law about **five closure operators on a finite index**. It is a statement in lattice
theory. It is **not** a statement about spacetime, about energy conditions as physics, or about
whether a warp corridor is buildable. Nothing here bears on the physical obstruction measured
elsewhere in this research tree — `persist.py`'s shortfall of 69.03 orders of magnitude and
`higgs.py`'s required coupling ξ ≥ 9.782907 × 10³¹ — and no clause below moves either.

Five status words are used and never merged. **The distinction between the third and fourth is the
one most easily lost, and this document has lost it before.**

| status | meaning |
|---|---|
| **PROVED** | a proof is written out below and every step is justified |
| **MACHINE-CHECKED** | Z3 returned `unsat` on the negation of an obligation whose variables range over *every* subset of a named finite box. §10 says which objects carry it, over which boxes, and which fragment of each was encoded |
| **EXHAUSTIVE** | a decision procedure visited *every* case in a stated finite family |
| **SAMPLED** | a seeded pseudorandom sweep of a stated size. **Not exhaustive.** A figure like "300/300" is a sample result, and §10 marks these separately |
| **CITED** | taken from the literature; marked READ or UNREAD |

Two further words appear as markers rather than statuses: **REFUTATION** (§7, a claim disproved) and
**CANDIDATE** (§8b, §8c, operators outside the five, filed as evidence).

**The ceiling that is real:** no Lean or Coq is available in this environment, so nothing above `d = 3`
and nothing over an unbounded box is machine-checked. What is machine-checked is named in §10 and
nowhere else.

---

## §1 · Notation and definitions

Throughout, `d ≥ 2` is finite and `X` is a finite non-empty set of `d`-tuples.

**D1 (observed alphabet).** `A_i := π_i(X)`, the set of values `X` realises at coordinate `i`. Each
`A_i` carries a total order, so each is a **finite chain**.

**D2 (box).** `Box(X) := A_1 × ⋯ × A_d`. As a product of chains it is a lattice under coordinatewise
`∧ = min` and `∨ = max`. Any subset of a chain is a sublattice of it, so `Box(X)` is closed under both.

**D3 (generated sublattice).** `⟨X⟩` := the smallest subset of `Box(X)` containing `X` and closed
under `∧` and `∨`. Since `∧` and `∨` act coordinatewise, no new coordinate value is ever created, so
the closure stays inside `Box(X)`. This is what `op_algebra` computes.

**D4 (boundary function).** For `i ≠ j` and `a ∈ A_j`,

> `φ_ij(a) := max { y_i : y ∈ X, y_j ≤ a }`,  undefined if that set is empty.

**D5 (staircase).** `R(X) := { x ∈ Box(X) : x_i ≤ φ_ij(x_j) for all i ≠ j }`. This is what `op_order`
computes.

**D6 (join-closure).** `J(X)` := the smallest superset of `X` closed under `∨` alone.

**D7 (geometry).** `G(X) := { x ∈ Box(X) : (x_i,x_j) ∈ conv(π_ij X) for all i<j }`.

**D8 (statistics, order 2).** `St(X) := { x ∈ Box(X) : π_ij(x) ∈ π_ij(X) for all i<j }`.

**D9 (pair-definable).** An operator `L` is *pair-definable* if there exist `C_ij ⊆ A_i × A_j` with
`L(X) = { x ∈ Box : (x_i,x_j) ∈ C_ij for all i<j }`.

**D10 (k-determined).** `S ⊆ Box` is *k-determined* if
`S = { x ∈ Box : every k-fold projection of x is a k-fold projection of some element of S }`.

**Two ambient regimes**, distinguished because conflating them caused an error earlier in this work:

- **own-box**: each set is read in its own `Box(·)`;
- **fixed-box**: `X ⊆ Y` are both read in one declared `Box` (which may exceed either observed box).

Clause A is proved in **both**. Clause B holds in the **own-box** regime and can fail in the other
(§8, N1).

---

## §2 · Preliminaries

**Lemma 1 (φ is total and isotone in its argument).** For `a ∈ A_j` there is `y ∈ X` with `y_j = a`
(D1), so `{y ∈ X : y_j ≤ a} ≠ ∅` and `φ_ij(a)` is defined. If `a ≤ a'` the candidate set for `a'`
contains that for `a`, so `φ_ij(a) ≤ φ_ij(a')`. ∎ **PROVED.**

> **D1 is used in exactly two places, and this note previously claimed one.** Here, to make `φ`
> total; and in Lemma 5, where two of the four witnesses are produced by it (`a ∈ A_1 = π_1(X)`).
> Nowhere else.

**Lemma 2 (φ is monotone in `X`).** For `X ⊆ Y` in a fixed box and any `i ≠ j`, `a`:
`{y_i : y ∈ X, y_j ≤ a} ⊆ {y_i : y ∈ Y, y_j ≤ a}`, so `φ^X_ij(a) ≤ φ^Y_ij(a)` whenever the left side
is defined; and where `φ^X` is undefined the staircase rejects outright. ∎ **PROVED**, and
EXHAUSTIVE: 0 failures over 400 nested pairs.

**Lemma 3 (the staircase does not move its own boundary).** `φ^{R(X)}_ij = φ^X_ij` on `Box(X)`.
*Proof.* `X ⊆ R(X)` (Lemma 4a) gives `≥` by Lemma 2. For `≤`: let `y ∈ R(X)` with `y_j ≤ a`. Then
`y_i ≤ φ^X_ij(y_j) ≤ φ^X_ij(a)` by Lemma 1. So every candidate contributed by `R(X)` is bounded by
`φ^X_ij(a)`, hence the max is too. ∎ **PROVED**, 0 failures over 400 cases.

---

## §3 · Clause A — every admitted language is a closure operator

> **A.** Each of `order`, `algebra`, `geometry`, `information`, `statistics` is **extensive**,
> **monotone** and **idempotent** on subsets of a fixed box.

This answers a correction made during the work: the axioms had been *measured* 300/300 and never
derived. Each is now derived.

**A.1 Extensive.**
- `order`: for `x ∈ X` and any `i≠j`, `x` itself witnesses `x_j ≤ x_j`, so `φ_ij(x_j) ≥ x_i`. ∎
- `algebra`, `information`: immediate from D3, D6. ∎
- `geometry`: `π_ij(x) ∈ π_ij X ⊆ conv(π_ij X)`. ∎
- `statistics`: `π_ij(x) ∈ π_ij X`. ∎

**A.2 Monotone** (`X ⊆ Y`, fixed box).
- `order`: by Lemma 2 every constraint is weaker for `Y`, so `R(X) ⊆ R(Y)`. ∎
- `algebra`: `⟨Y⟩` is a sublattice containing `X`, hence contains `⟨X⟩`. ∎
- `information`: `J(Y)` is join-closed and contains `X`, hence contains `J(X)`. ∎
- `geometry`: `conv` is monotone. ∎
- `statistics`: `π_ij X ⊆ π_ij Y`. ∎

In the **own-box** regime, `order` and `algebra` inherit monotonicity from `⟨·⟩` via Clause B instead
— **SAMPLED** at 4,000 nested pairs, 0 failures (own-box regime).

**A.3 Idempotent.**
- `order`: by Lemma 3 the boundary functions of `R(X)` equal those of `X`, so `R(R(X)) = R(X)`. ∎
- `algebra`, `information`: a closure is closed. ∎
- `geometry`: `π_ij X ⊆ π_ij G(X) ⊆ conv(π_ij X)`, and `conv` of a set between `S` and `conv(S)` is
  `conv(S)`; so the hulls are unchanged and `G(G(X)) = G(X)`. ∎
- `statistics`: `π_ij St(X) ⊆ π_ij X` by definition, and `⊇` because each witnessing element of `X`
  lies in `St(X)`; so the marginals are unchanged. ∎

**Status: PROVED**, all five, both regimes. Cross-checked EXHAUSTIVE at 300/300 (`law.py`).

---

## §4 · Clause B — `order` and `algebra` are one operator

> **B.** `R(X) = ⟨X⟩`. Equivalently `op_order = op_algebra`, and both compute the sublattice hull.

### 4.1 The easy inclusion

**Lemma 4.** `R(X)` is a sublattice of `Box(X)` containing `X`.
*(a)* Extensivity is A.1. *(b)* Let `p,q ∈ R(X)` and fix `i≠j`.
- **Join.** WLOG `p_i ≥ q_i`. Then `(p∨q)_i = p_i ≤ φ_ij(p_j) ≤ φ_ij((p∨q)_j)` by Lemma 1.
- **Meet.** WLOG `p_j ≤ q_j`, so `(p∧q)_j = p_j`. Then `(p∧q)_i ≤ p_i ≤ φ_ij(p_j) = φ_ij((p∧q)_j)`. ∎

Hence **`⟨X⟩ ⊆ R(X)`**, using nothing but Lemma 1. The content is the reverse.

### 4.2 The two-dimensional case

**Lemma 5.** For `d = 2`, `R(X) ⊆ ⟨X⟩`.
*Proof.* Let `(a,b) ∈ R(X)`. Four witnesses exist in `X`:

| witness | exists because |
|---|---|
| `y` with `y_A = a` | `a ∈ A_1 = π_1(X)` (D1) |
| `z` with `z_B = b` | `b ∈ A_2 = π_2(X)` (D1) |
| `u` with `u_A ≤ a`, `u_B ≥ b` | `b ≤ φ_BA(a)`, and the max is attained |
| `v` with `v_A ≥ a`, `v_B ≤ b` | `a ≤ φ_AB(b)`, and the max is attained |

Set `α := y ∨ u` and `γ := z ∨ v`. Then
`α = (max(a,u_A), max(y_B,u_B)) = (a, β)` with `β ≥ u_B ≥ b`, and
`γ = (max(z_A,v_A), max(b,v_B)) = (α′, b)` with `α′ ≥ v_A ≥ a`. Therefore

> `α ∧ γ = (min(a,α′), min(β,b)) = (a,b)`,

and `α, γ ∈ ⟨X⟩`, so `(a,b) ∈ ⟨X⟩`. ∎ **PROVED.** EXHAUSTIVE: the construction was *built*, not
inferred, on **54,392** cells of `R`, 0 failures.

### 4.3 The lift

**Lemma 6.** `π_ij` is a lattice homomorphism, so `π_ij⟨X⟩ = ⟨π_ij X⟩`. Also `φ_ij` depends only on
`π_ij X`, and `π_i(π_ij X) = A_i`, so D1 passes to the projection. With Lemma 5,
`⟨π_ij X⟩ = R_ij := {(s,t) : s ≤ φ_ij(t), t ≤ φ_ji(s)}`. ∎

**Lemma 7 (the lift).** `⟨X⟩ = { x ∈ Box(X) : (x_i,x_j) ∈ π_ij⟨X⟩ for all i<j }`.

With Lemma 6 the right-hand side is exactly D5, giving **B**. ∎

Lemma 7 is where the work is, and it is **prior art**:

- **Queyranne–Tardella Theorem 11** states it for the sublattice hull directly, and their **Theorem 3**
  gives the projection representation under the sufficient condition **"`I` is finite"** — i.e.
  finitely many coordinates. Their proof is direct: fix `x`, choose `y^{ij} ∈ LQ` agreeing with `x` on
  coordinates `i,j`, form the meets `u^i = ⋀_j y^{ij}`, then the join `z = ⋁_i u^i`, and show `z = x`.
- **Baker–Pixley** gives the same conclusion abstractly: lattices have the majority term
  `m(x,y,z) = (x∧y)∨(y∧z)∨(z∧x)`, and a variety with a majority term has every subalgebra of a finite
  product determined by its 2-fold projections (**k-decomposability**).

Either route suffices. **At `d = 2` no lift is needed** — Lemma 5 is the whole proof.

**Status: PRIOR ART, READ.** EXHAUSTIVE cross-check: **36,252** cases over observed boxes, 0 failures;
Lemma 7's conclusion checked directly on **4,128** generated sublattices, 0 exceptions, majority term
valid on every one.

### 4.4 The correspondence, term by term

| Queyranne–Tardella | here |
|---|---|
| `δ^Q_ij(h) = ⋁{x_i : x ∈ Q, x_j ≤ h}` | `φ_ij` (D4) |
| Proposition 1, `π_J LQ = L π_J Q` | Lemma 6 |
| Theorem 9(ii), factors are **chains** | Lemma 5 |
| Theorem 11, `LQ = ⋂ Cyl_ij E_ij Q` | Clause B |
| Example 10, failure off the chains | §8, N2 |
| **proper** boundary epigraph: `k ≥ δ` where attained, `k > δ` where not | **§8, N1 — the hypothesis we needed and they did not** |

The last row is the instructive one, and an earlier draft overstated it. Their Remark 6 says that when
each `T_i` is a chain **and `Q` is finite**, `P^Q_ij` is everything and the proper epigraph collapses to
the plain one — so in *our* setting their strictness device is inactive too, and both formulations rely
on the same finiteness-and-chains footing. What is true is narrower: **their formulation states the
attainment condition explicitly and ours smuggled it into D1**, which is why our necessity analysis took
two attempts and theirs needed none.

---

## §5 · Clause C — `information` is the join-closure

> **C.** `op_information(X) = J(X)`, and therefore `information ⊆ algebra`.

`op_information` extracts the join-irreducibles of `X` and re-closes them under `∨`.

**Lemma 8.** Every `x ∈ X` is a join of join-irreducibles of `X`.
*Proof.* Induction on `n(x) = |{y ∈ X : y < x}|`. If `x` is join-irreducible it is its own seed. Else
the supremum of `{y ∈ X : y < x}` equals `x`, so `x` is the join of those elements, each with
`n(y) < n(x)`, each therefore a join of seeds by induction. ∎

Hence the seed regrows `X`, so `op_information(X) ⊇ X`; being join-closed it contains `J(X)`; and
being generated by a subset of `X` it is contained in `J(X)`. So `op_information(X) = J(X)`.
A sublattice is join-closed, so `J(X) ⊆ ⟨X⟩`. ∎

**Status: PROVED.** EXHAUSTIVE: 200/200 (`law.py`), 0 failures over 600 worlds (`induce.py` sweep).

> `information ⊆ algebra` is therefore a **theorem**, not the tendency it was recorded as.

---

## §6 · Clause D — 2-determinacy, and where the content actually is

> **D.** `L(X)` is 2-determined **iff** it is pair-definable. Four of the five are; `information` is not.

**(⟸)** Let `L(X) = {x ∈ Box : (x_i,x_j) ∈ C_ij ∀i<j}`. Then `π_ij(L(X)) ⊆ C_ij`, so
`{x : (x_i,x_j) ∈ π_ij L(X) ∀i<j} ⊆ L(X)`; the reverse inclusion is free. ∎ **Two lines.**

**(⟹)** If `L(X)` is 2-determined then `C_ij := π_ij(L(X))` witnesses pair-definability. ∎

**The `iff` is true and nearly vacuous in the `⟹` direction**, and saying so matters: `order` (D5),
`geometry` (D7) and `statistics` (D8) are each *defined* in pair form, so their 2-determinacy is free.
**Measuring it measured nothing** — a correction to an earlier reading in this work that treated
500/500 across four operators as evidence.

**The content is in exactly two places.**

1. **`algebra` is 2-determined and is not pair-defined.** It is defined by closure under operations.
   Its 2-determinacy is precisely Lemma 7 — Theorem 11 / Baker–Pixley. **This is the whole substance.**
2. **`information` is not 2-determined**, minimal witness at `d = 3`:

> `X = {(0,0,0), (0,1,1), (1,0,1)}`. `J(X)` adds `(1,1,1)` and stops at **4** cells. Rebuilt from its
> own pairwise projections, `J(X)` **invents `(0,0,1)`**. On the same `X`, all four other operators
> are 2-determined.

**One three-element set separates `information` from the rest of the hierarchy.** The reason is
structural: a **join-semilattice has no majority term**, so nothing in the Baker–Pixley family reaches
it. Consistent with this, `information` still fails at `k = 3` (270/300).

**Status: PROVED** (both directions, plus the witness). EXHAUSTIVE: 150/150 for the four, failure
confirmed for `information`.

---

## §6b · Clause F — the order language is a precondition, and one language escapes it

> **F.** Four of the five operators are **not invariant** under a relabelling of values that preserves
> their identity and destroys their order. `statistics` is invariant. **The order language is a
> precondition for `order`, `algebra`, `information` and `geometry`, and is not one for `statistics`.**

This clause exists because of a reading made in review: *"language is order. If order is necessary for
algebra, then so is the language."* That is right, and it reassigns the emphasis of §8 — see N1/N2
below.

**The test.** Take `X` in its box. Apply a bijection `σ_i` to each coordinate's observed values — pure
relabelling, so every value keeps its identity and every membership fact is preserved, while the order
`≤` is scrambled. Compute the operator on `σX`, map back by `σ⁻¹`, compare with the operator on `X`.

| operator | invariant | verdict |
|---|---|---|
| `order` | 58 / 400 | **requires the order** |
| `algebra` | 58 / 400 | **requires the order** |
| `information` | 59 / 400 | **requires the order** |
| `geometry` | 102 / 400 | **requires the order** |
| `statistics` | **400 / 400** | **ORDER-FREE** |

*(The survivors are the draws where the shuffle happened to preserve the order, or the structure was
degenerate. `geometry` survives more often because a 2-D convex hull also survives order-reversal.)*

**`statistics`' invariance is a theorem, not luck.** D8 reads only the membership
`π_ij(x) ∈ π_ij(X)`, and every bijective relabelling preserves membership. Two lines. **PROVED.**

**And the other four are order-dependent by explicit witness, not merely by inspection.** Minimal
counterexamples, found by exhaustive search over `d ≤ 3` and alphabets `≤ 4`:

| operator | `X` | `σ` | `\|L(X)\|` → `\|σ⁻¹L(σX)\|` |
|---|---|---|---|
| `order` | `{(0,0),(1,1)}` | swap coordinate 2 | 2 → 4 |
| `algebra` | `{(0,0),(1,1)}` | swap coordinate 2 | 2 → 4 |
| `information` | `{(0,0),(1,1)}` | swap coordinate 2 | 2 → 3 |
| `geometry` | `{(0,0),(0,1),(1,2)}` | `1↔2` in coordinate 2 | 3 → 4 |

**Two cells suffice for three of the four.** `{(0,0),(1,1)}` is a chain; relabel one coordinate and it
becomes the antichain `{(0,1),(1,0)}`, whose sublattice closure is the whole box. **Order-dependence in
two cells.** `PROVED` by witness, not by construction-inspection.

**And they break on exactly the same instances — 400 / 400.** An earlier draft called this an
*independent* corroboration of Clause B. **It is not independent: it is entailed by it.** "`order`
breaks on `X`" is `σ⁻¹R(σX) ≠ R(X)` and "`algebra` breaks on `X`" is `σ⁻¹⟨σX⟩ ≠ ⟨X⟩`; Clause B says
`R(Y) = ⟨Y⟩` for every `Y`, so with both `X` and `σX` in range the two conditions are literally the same
condition. **The 400/400 is a consistency check on the implementation, not evidence for the theorem.**

**What the clause does and does not support.** The claim under review was that *every rung above the
first requires the language below it*. For `algebra`, `information` and `geometry` that is measured and
true. For `statistics` it is **false** — and `statistics` is the rung the ladder placed at the top.
Necessity of language is a condition of order for four of the five; the fifth needs only identity.

**Status: PROVED** — `statistics` from D8 in two lines, and the other four by the explicit witnesses
above. The 400-draw sweep is **SAMPLED** corroboration, not the proof; an earlier draft filed the four
as EXHAUSTIVE, which they were not.

---

## §6c · Clause G — `statistics` is the hypothetical language, and that settles N1

> **G.** `statistics` is the only operator whose data is *cells* rather than *relations between cells*.
> Its admission condition is a membership test, so it is order-free; it lies inside `geometry` always;
> and its hypothetical extension preserves the geometry that generated it.

This clause exists because of a reading offered in review: *"Statistics remains without order because it
is the only language that speaks in hypotheticals. Each other language requires order. Statistics only
needs a singularity."* Each part is measurable and each part holds.

**G.1 — "it only needs a singularity."** `St(X)`'s constraint set is `π_ij(X) = ⋃_{y∈X} {π_ij(y)}` — a
**union of single-cell contributions**. No relation between two cells is ever consulted.

| | union of single-cell facts |
|---|---|
| `statistics` | **500 / 500** |
| `algebra` *(control)* | **98 / 500** |

The control matters: the property is not generic. `algebra` needs `∧` and `∨`, which are relations
*between* cells; `statistics` needs only the cells themselves. **PROVED** (immediate from D8) and
EXHAUSTIVE.

**G.2 — the hypothetical character and the order-freedom are the same fact.** A membership test asks
*"has this pair been seen?"* — an `if`, evaluated against observation. Membership is preserved by every
bijection, so Clause F's `400/400` order-freedom is not a second property; **it is G.1 restated**. The
other four read `≤` directly (`φ`, `∧`, `∨`, `conv`) and cannot be evaluated without it.

**G.3 — `statistics ⊆ geometry`, always.** **500 / 500**, and it is a one-line proof:
`π_ij(X) ⊆ conv(π_ij X)`, so any cell whose pair-projections are *observed* has them in the *hull*.
**PROVED.** This is the second lawful containment after Clause C.

**G.4 — the hypotheticals never leave the geometry that generated them.**

> `geometry(statistics(X)) = geometry(X)` — **500 / 500.**

`X ⊆ St(X) ⊆ G(X)` by G.3, and `conv` of any set between `S` and `conv(S)` is `conv(S)`, so the hulls
are unchanged. **PROVED.** This is the measurable part of the review's third sentence — *"logic verifies
the if and then against the original geometry being statisticized."* **The verification step holds.**

**G.5 — and this settles N1.** N1 and N2 are stated in different *registers*, and the register decides
which one can be necessary:

| hypothesis | invariant under an order-destroying relabelling | register |
|---|---|---|
| **N1** every ambient value observed | **500 / 500** | **membership** |
| **N2** the order relation itself | **84 / 500** | **order** |

**And the tempting inference from this is invalid, so it is not made.** An earlier draft argued *"a
condition stated in the membership register cannot be necessary for an order-theoretic theorem"* — that
does not follow. Invariance mismatch blocks *equivalence*; it does not block one-way implication, and an
order-invariant condition can perfectly well imply an order-dependent one. Indeed N1 does exactly that:
it implies attainment (Lemma 1) without stating it.

**What the register table does establish** is weaker and still useful: N1 and N2 are conditions of
different kinds, so the fact that one is necessary and the other is not is **not a coincidence of
counterexamples but a difference in what they can express.** The necessity itself is settled by
Lemma N1\* and its corollary in §8, not by this table.

**G.6 — what is NOT testable here, stated so it is not smuggled in.** The review's chain runs
*statistics gives the `if` → analysis gives the `then` → logic verifies both against the original
geometry.* The first and third steps are measured above and hold. **The middle step cannot be
measured**: `analysis` has **no operator** in the cypher — it is declared-only — and which languages
exist — the roster of operator-bearing languages — is an open question in the corpus this cypher comes
from, and is not settled here. **No operator for `analysis` was invented for this clause**, and none
should be until that roster question is ruled on.

---

## §6d · Clause H — the lawful skeleton: which part of the ranking *is* a law

Clause E refutes the *total* ranking. It does not follow that no ordering is lawful, and review
pressure made that worth measuring. Over 600 worlds, exactly **seven** containments hold without
exception:

| holds always | |
|---|---|
| `order ⊆ algebra` and `algebra ⊆ order` | **= Clause B, recovered from outside its own derivation** |
| `information ⊆ algebra`, `information ⊆ order` | Clause C |
| `statistics ⊆ algebra`, `statistics ⊆ order` | **proved below** — the fourth relation, which an earlier draft left with a blank cell |
| `statistics ⊆ geometry` | G.3 |

Everything else varies — `geometry ⊆ order` 585/600, `statistics ⊆ information` 422/600,
`information ⊆ geometry` 301/600, and so on down to 139/600.

**The lawful skeleton, with `O := order = algebra`:**

```
        O = order = algebra              geometry
         /                \             /
   information          statistics ────
```

- `O` and `geometry` are **incomparable** — neither contains the other in general.
- `information` and `statistics` are **incomparable** with each other.
- `statistics` is the only language below **two** maxima, and the only one below `geometry`.
- `information` and `statistics` are the **minimal** elements; `O` and `geometry` the **maximal**.

**The fourth lawful relation, `statistics ⊆ order = algebra`, has a three-line proof** and an earlier
draft cited three clauses for four relations, leaving this one unjustified:

> Let `x ∈ St(X)`. For each pair `i ≠ j` there is, by D8, some `y ∈ X` with `(y_i, y_j) = (x_i, x_j)`.
> That `y` satisfies `y_j ≤ x_j` and `y_i ≥ x_i` — with equality — so it is exactly the witness Clause
> B's form of `R(X)` requires. Hence `x ∈ R(X) = ⟨X⟩`. ∎

**Each incomparability is PROVED by an explicit minimal witness**, not merely measured:

| non-containment | `X` | witness cell |
|---|---|---|
| `geometry ⊄ order` | `{(0,0),(0,1),(1,2),(2,2)}` | `(1,1)` |
| `order ⊄ geometry` | `{(0,1),(1,0)}` | `(0,0)`, `(1,1)` |
| `information ⊄ statistics` | `{(0,1),(1,0)}` | `(1,1)` |
| `statistics ⊄ information` | `{(0,0,0),(0,1,1),(1,0,1)}` | `(0,0,1)` |
| `information ⊄ geometry` | `{(0,1),(1,0)}` | `(1,1)` |
| `geometry ⊄ information` | `{(0,0),(0,2),(1,1)}` | `(0,1)` |

**The two-cell antichain `{(0,1),(1,0)}` separates three of the six.** And the `statistics ⊄
information` witness is *the same three-cell set* that breaks 2-determinacy in Clause D — one object
doing both jobs, which is why `information` is the odd language in two independent senses.

**This is the precise sense in which the ladder was right and wrong.** It was wrong as a total order
(Clause E). It was right that there is a hierarchy: **a genuine partial order with four lawful
relations**, in which `statistics` sits at a minimum — the most restrictive position, which in the
ladder's own idiom is the *top* rung. **Status: EXHAUSTIVE** (600 worlds); the four relations are each
individually **PROVED** (Clause B, C, G.3).

---

## §7 · Clause E — the ranking is not part of the law

> **E.** The **total** order in which the five languages nest is a property of the index, not a
> law. (Clause H gives the part that *is* lawful — read them together.)

Measured in `induce.py` over **400 random worlds**:

| observation | value |
|---|---|
| distinct size-orderings of the five | **14** |
| frequency of the energy-condition index's ordering | **42 / 400** (fourth most common) |
| `statistics` is the **minimum** *(below **all four** others, including `information`)* | 106 / 400 |
| `statistics` is the **maximum** | **128 / 400** |
| `geometry` vs `information` | `info < geom` 183 · incomparable 144 · equal 57 · `geom < info` 16 |
| `order` is the maximum | 398 / 400 (both exceptions `geometry`, both incomparability) |

**These two figures measure different things and an earlier draft let them sit fifty lines apart
unreconciled.** "`statistics` is the minimum" here means below *all four* other languages — which fails
whenever `information` is incomparable with it. Clause H's `statistics ⊆ order`, `⊆ algebra`, `⊆
geometry` hold **always**; it is only `statistics` vs `information` that varies. **106/400 is the
four-way count; the three lawful containments are 600/600.**

And **two indexes the corpus itself seats already disagree** — but on *size*, not on containment, and
an earlier draft conflated the two:

| index | `\|geometry\|` | `\|information\|` | set relation |
|---|---|---|---|
| NEC index | 29 | 156 | **INCOMPARABLE** |
| periodic 3-D | 173 | 114 | **INCOMPARABLE** |

> **⚠ THE "SWAP" IS A CARDINALITY ARTEFACT.** `geometry` and `information` are set-theoretically
> **incomparable on both** seated indexes — neither contains the other — so nothing nests one way on one
> index and the other way on the other. What differs is only which set is *larger*. The earlier draft
> presented the size order as a nesting order and called the reversal a swap; **that reading is
> withdrawn.** The clause survives on the sampled evidence above, and on the fact that a size ranking is
> not an order relation at all — which is itself the point.

**Status: REFUTATION, EXHAUSTIVE.** The ladder this work ran on was a property of one 17-cell index.

---

## §8 · Necessity — each hypothesis dropped until it breaks

> **The two hypotheses are not peers, and review corrected this.** N2 is the *order language* being
> present and total. N1 is a bookkeeping condition about attainment. The reading offered was: *"language
> is order; if order is necessary for algebra, so is the language."* Clause F measures exactly that —
> scramble the order and `algebra` changes in 342 of 400 draws. **So the necessary hypothesis of Clause
> B is the language (N2), and N1 is not necessary at all.** They are listed in that order below and the
> emphasis has been moved accordingly.

**N1 · `A_i = π_i(X)` (observed alphabet) — SUFFICIENT, NOT NECESSARY, AND THE SHARP CONDITION IS
NOW PROVED.**

> **Lemma N1\*.** For any declared box `B ⊇ Box(X)`:  `R_B(X) ∩ Box(X) = ⟨X⟩`.
> *Proof.* `φ_ij` is computed from `X` alone and does not mention `B`. So for `x ∈ Box(X)` the staircase
> conditions over `B` are literally the same conditions as over `Box(X)`, whence
> `R_B(X) ∩ Box(X) = R_{Box(X)}(X)`, which is `⟨X⟩` by Clause B. ∎
>
> **Corollary (necessary and sufficient).**  `R_B(X) = ⟨X⟩`  **iff**  `R_B(X) ⊆ Box(X)`.
> The failure set is exactly `R_B(X) \ Box(X)` — the cells outside the observed box that survive the
> staircase. **PROVED**, and EXHAUSTIVE at **0 failures in 702,628 cases**.

**An earlier draft recorded N1 as *necessary*. That was wrong**, and the correction has two stages, both
kept because the second supersedes the first rather than erasing it.

*First correction.* Over a declared box larger than the observed one the identity often fails but **not
always**, so N1 is sufficient and not necessary. A weaker sufficient condition is **order-convexity** —
no value of `A_i` strictly between `min π_i(X)` and `max π_i(X)` may go unobserved, while values above
the max or below the min are harmless. Measured over declared boxes: **convex → 1,853 hold, 0 fail;
gapped → 632 hold, 1,643 fail.** The 632 show convexity is *also* not necessary. Minimal
counterexample: `d = 2`, box of 3 cells, `X = {(0,0),(2,0)}` with value 1 unobserved — staircase 3
cells, sublattice 2.

*Second correction, which supersedes it.* **Convexity is not the boundary; the corollary is.** A gapped
world holds precisely when no outside cell survives the staircase, and convexity is sufficient exactly
because it forces that. The 632 are not an anomaly to be explained away — they are the corollary being
weaker than convexity, as it should be.

*And Queyranne–Tardella need no such hypothesis, though not for the reason first given here:* their
Remark 6 has the proper epigraph collapse to the plain one when the factors are chains and `Q` is
finite, so the strictness device is inactive in our setting too. What their formulation does is **state
the attainment condition explicitly** where ours buried it in D1.

**N2 · each `A_i` a chain — NECESSARY. THIS IS THE LANGUAGE CONDITION, and the failure is one-directional.**
Off the chains the staircase **never over-generates**; it **under**-generates. `R(X) ⊆ ⟨X⟩` survives
arbitrary finite lattice factors — it is Lemma 4, which needs `φ` isotone and hence a total order,
that dies. Measured over non-chain factors:

**The ambient must be stated, because off the chains it is load-bearing and the counts move with it.**
A subset of a non-chain factor need not be a sublattice of it, so D2's justification fails and there are
two defensible ambients: the **observed** product `∏ π_i(X)`, and the **closed** product in which each
factor's observed values are closed under that factor's own meet and join.

| factors | observed ambient — eq / under / **over** | closed ambient — eq / under / **over** |
|---|---|---|
| chain × chain | 120 / 0 / **0** | 120 / 0 / **0** |
| M3 × chain | 290 / 270 / **0** | 356 / 204 / **0** |
| M3 × M3 | 700 / 1900 / **0** | 1066 / 1534 / **0** |
| N5 × chain | 371 / 189 / **0** | 415 / 145 / **0** |
| N5 × N5 | 1144 / 1456 / **0** | 1428 / 1172 / **0** |

> **Every equality and under-generation count changes with the ambient. The over-generation column does
> not: it is 0 under both.** So the conclusion this section draws — that the staircase *under*-generates
> off the chains and never over-generates — is ambient-independent, while the individual counts are not.
> An earlier draft printed one ambient's numbers without naming the convention.

Queyranne–Tardella's **Example 10** is the same phenomenon on `{0,a,b,c,1}` with `a∧b=0`, `a∨b=c<1`.

**N2a · the proper-epigraph formulation does NOT rescue the non-chain case — tested, and it is a
proof rather than a measurement.**
Queyranne–Tardella's *proper* boundary epigraph distinguishes attained from unattained boundary values,
admitting `k ≥ δ` in the first case and requiring `k > δ` in the second. The obvious hope was that this
strictness is what chains were standing in for. **It is not.** Implemented over non-chain factors and
run against the naive staircase:

| factors | cases | naive: eq / under / over | proper: eq / under / over |
|---|---|---|---|
| chain × chain | 120 | 120 / 0 / 0 | 120 / 0 / 0 |
| M3 × chain | 560 | 290 / 270 / 0 | **290 / 270 / 0** |
| M3 × M3 | 2600 | 700 / 1900 / 0 | **700 / 1900 / 0** |
| N5 × chain | 560 | 371 / 189 / 0 | **371 / 189 / 0** |
| N5 × N5 | 2600 | 1144 / 1456 / 0 | **1144 / 1456 / 0** |

**Identical to the case.** And the reason is a one-line proof, not a coincidence: strictness can only
*remove* admitted cells, so `proper(X) ⊆ naive(X)` always. Off the chains the failure is
**under**-generation — `naive(X) ⊊ ⟨X⟩` — so no operator contained in the naive one can reach `⟨X⟩`.
**Attainment-strictness cannot repair under-generation.** The chain hypothesis is doing independent
work: it is what makes Lemma 4 (`⟨X⟩ ⊆ R(X)`) true, and Lemma 4 is the inclusion that dies.

**N3 · `d ≥ 2` — a convention.** `op_order` returns SILENT at `d = 1`; both sides would be `X`.

**N4 · finiteness — it is the *number of factors* that Lemma 7 needs**, not finiteness of the factors.
Queyranne–Tardella's Example 2 (finite subsets of an infinite index set) shows the representation
failing when `I` is infinite without a subcompleteness condition.

---

## §8b · Appendix — `analysis`, the residual, and why `logic` is needed

> **THE ROSTER OF OPERATOR-BEARING LANGUAGES IS NOT SETTLED HERE.** `tools/cypher.py` is untouched and
> no roster is changed. This is a candidate operator, specified in review, measured, and filed as **evidence**.

> **⚠ THE FIRST VERSION OF THIS APPENDIX IS WITHDRAWN.** It formalized "best possible closure route"
> as *minimum number of `∧`/`∨` steps* and concluded that `logic` had almost nothing to do — only
> 0.3 % of geometric positions unreachable. **That measured REACHABILITY, which is not closure**, and
> the conclusion was wrong by a factor of two hundred. The corrected reading and measurement follow.

**The specification, corrected in review.** *"E = |X| means not all statistical positions can close at
E = 0."* So `E = |X|` is not a value to hit; it is the assertion that **the residual is not always
zero**. `analysis` reports, for each statistical position, the **best achievable residual** — and
because that residual is often nonzero, something must adjudicate it. **That is `logic`.**

**Formalization.** For each statistical position `x ∈ St(X) \ X`, form `Y = X ∪ {x}` and compute
`E_L(Y) = |L(Y)| − |Y|` for each language `L`. The *best closure route* for `x` is the `L` minimising
`E_L(Y)`; `analysis` reports that minimum. `x` **closes** iff the minimum is 0.

**Measured over 155 statistical positions in 79 worlds:**

| | |
|---|---|
| reachable — a finite route exists | **100 %** (theorem: `statistics ⊆ algebra`, Clause H) |
| **closes at E = 0 by its best route** | **45 / 155 — 29 %** |
| **CANNOT close at E = 0 by any route** | **110 / 155 — 71 %** |
| worlds containing at least one such position | 34 / 79 |

Distribution of the best achievable residual: `{0:45, 1:36, 2:26, 3:3, 4:11, 5:26, 7:8}`.

> **REACHABLE BUT NOT CLOSABLE.** Every statistical hypothetical lies in the sublattice hull, so a
> route always exists — and yet **71 % of them cannot be closed to E = 0 by any language.** The two
> properties are independent, and conflating them is what produced the withdrawn version above.

**And the best route is always `statistics`.** Per language, the fraction of positions reaching E = 0:

| language | at E = 0 |
|---|---|
| `order` | 2.6 % |
| `algebra` | 2.6 % |
| `information` | 7.1 % |
| `geometry` | 8.4 % |
| **`statistics`** | **29.0 %** |

The best-over-all-languages figure is **also 29.0 %** — identical to `statistics` alone. **Whenever any
language can close a position, `statistics` can.** But it is **not** true that no other language ever
beats it, and §8c's own routing table shows why: **`information` alone is the best route on 13
positions**, where it reaches a strictly smaller residual than `statistics` does. The correct statement
is the one about reaching zero, not about the residual in general.

> **`statistics` is optimal for E = 0 and not optimal in general.** An earlier draft asserted the
> stronger claim and the paper refuted it sixty lines later without noticing.

**What this settles about `analysis`.** It returns a **residual magnitude**, not a cell decision, and
the magnitude is nonzero for 71 % of its domain. That is precisely the corpus's recorded reason for
excluding it (*"has a mechanism but returns a magnitude rather than a cell decision"*) — now with the
mechanism named and the magnitude measured. **`analysis` is not a sixth operator-bearing language**,
and the 71 % is exactly why the chain needs a third step: `statistics` proposes the `if`, `analysis`
returns the residual, **`logic` adjudicates the residual that analysis declines to judge.**

**Status: EXHAUSTIVE, CANDIDATE, NOT A RULING.**

---

## §8c · Appendix — `logic` is an interpreter, not a language, and its refusals are seed-dependent

> **THE ROSTER OF OPERATOR-BEARING LANGUAGES IS NOT SETTLED HERE.** Candidate, measured, filed as
> evidence.
> `tools/cypher.py` untouched.

> **⚠ THIS APPENDIX'S FIRST HEADLINE IS WITHDRAWN.** It reported *"8 of 155 positions refuted"* and
> concluded that **the residual does not determine the verdict**, calling that the argument for `logic`
> being a distinct step. **All 8 refutations were tie-break artifacts.** When several languages tie at
> the minimum residual, "the best closure route" does not name a unique closure, and my code broke the
> tie by iteration order — two runs of the same worlds gave 147 and 152. The claim rested entirely on
> those 8 and does not survive. Corrected below.

**The specification, refined in review.** *"Logic is not exactly a language. It is an interpreter. It
interprets the statistical analysis into a binary verdict. So logic is multilingual."* That dissolves
rather than settles the earlier tension: the previous version applied **language criteria** (Clause A's
closure axioms) to something that is **not a language**, and unsurprisingly found a contradiction.

**The obvious reading is empty.** Asking whether the *position* lies in `G(X)` is **155 / 155** — that
is just Clause G.3. Logic must read the closure `analysis` produced.

**The verdict, bracketed — because the tie-break is not part of the specification:**

| rule | admitted |
|---|---|
| **unanimous** — every minimizing language admits | **147 / 155 (94.8 %)** |
| **existential** — some minimizing language admits | **155 / 155 (100 %)** |
| **the gap** — verdict depends on which tied language is read | **8 (5.2 %)** |

The gap sits at residuals `{2: 2, 4: 3, 5: 3}`. Languages tie at the minimum in **35 of 155** positions
(2-way 16, 3-way 13, 5-way 6); only **120** have a unique best route.

> **AT THIS SEED, `logic` never refutes a position outright** — every one of the 155 is admitted by at
> least one minimizing language.
>
> **⚠ AND THAT DOES NOT GENERALISE.** At seed 77 the same sweep gives **21 refusals in 177 positions**.
> The universal reading — "there is no language-independent rejection" — was asserted in an earlier
> draft on the strength of one seed and is **WITHDRAWN**. What survives is the weaker and still
> interesting fact that outright refutation is *rare* and *seed-dependent*, which is itself evidence
> that the verdict is not a property of the position alone.

**And that is what makes it an interpreter.** Its output is **not a language-independent fact about the
position** — it is a verdict *relative to a language*, and where languages tie it must arbitrate
between them. A closure operator returns a set; a language returns a binary about a cell; **an
interpreter returns a binary about a claim made in some language, and must say which language it read.**
The 8 gap positions are the multilingualism made visible: same position, same residual, different
language, different answer.

**Which language does `analysis` route through?**

| best route | positions |
|---|---|
| `statistics` alone | 107 |
| `information` alone | 13 |
| `geometry` = `information` = `statistics` | 13 |
| `geometry` = `statistics` | 11 |
| all five tied | 6 |
| `information` = `statistics` | 5 |

`statistics` is in the winning set for **142 of 155**, consistent with Clause G — but it is not alone in
**35**, and that is where an interpreter is required.

**Forced monolingual, the verdict swings wildly:** `order` 19/155 · `algebra` 19/155 · `information`
67/155 · `geometry` 155/155 · `statistics` 155/155. **A single language cannot stand in for the
interpreter** — reading only `order` would reject 88 % of what reading only `geometry` accepts.

**What this settles about Clause A.** Nothing. `logic` is not a language, so the closure axioms were
never the right test, and the earlier "passes the binary criterion, fails Clause A" tension was an
artifact of the wrong frame. **Clause A stands unchallenged**; `logic` is simply outside its scope.

**Status: EXHAUSTIVE, CANDIDATE, NOT A RULING.** The tie-break remains unspecified; any figure quoted
without saying *unanimous* or *existential* is unstable across an 8-position band.

---

## §8d · The generalized theorem

The law as stated is one point in a three-axis family. This section names the axes, says what survives
each weakening, and marks what is open.

**The abstract form.** Let `V` be a variety with a `(k+1)`-ary **near-unanimity term**, let
`B = ∏_{i∈I} A_i` be a product of algebras of `V` over a **finite** index set `I`, and let `Q ⊆ B`.
Then the subalgebra generated by `Q` is **k-decomposable**:

> `⟨Q⟩ = { x ∈ B : π_S(x) ∈ π_S⟨Q⟩ for every S ⊆ I with |S| = k }`.

**Our law is the instance** `V = lattices`, `k = 2`, majority term `m(x,y,z) = (x∧y)∨(y∧z)∨(z∧x)`, each
`A_i` a finite chain — with the additional computational content, *not* supplied by the abstract form,
that the 2-fold projections are given in closed form by the staircase `φ` (Lemma 5). **The abstract
theorem says the projections determine the hull; Lemma 5 says what the projections are.**

### The three axes

**Axis 1 — the variety, i.e. the arity of the near-unanimity term.** A `(k+1)`-ary NU term buys
`k`-decomposability. Lattices have a 3-ary one, hence pairs. **Join-semilattices have none** — an NU
term forces congruence distributivity, which semilattices lack — and this is exactly why
`op_information`, which is a join-closure (Clause C), escapes the whole family.

> **PROVED, for every dimension.** Earlier drafts of this work reported the `k`-universality as open,
> on the strength of a run showing `188/188` at `k = 4` — **a size artifact**, which vanished once
> `|X|` grew (219/250 fails). The general statement is now a theorem with an explicit construction.
>
> **Proposition (`information` is `k`-determined for no non-vacuous `k`).** For `d ≥ 3` put
> `X_d = {0} ∪ { e_i + e_d : 1 ≤ i ≤ d−1 } ⊆ {0,1}^d`. Then:
>
> *(a)* `e_d ∉ J(X_d)`. Every element of `X_d` is `0` or has at least two ones, and a coordinatewise
> join of such elements is `0` or has at least two ones; `e_d` has exactly one. ∎
>
> *(b)* For every `T` with `|T| = k ≤ d−1`, `π_T(e_d)` is a `k`-projection of an element of `J(X_d)`.
> If `d ∉ T` then `π_T(e_d) = 0 = π_T(0)`. If `d ∈ T` then, since `|T| ≤ d−1`, some `i ∉ T` with
> `i ≠ d` exists, and `e_i + e_d` agrees with `e_d` off coordinate `i`, so
> `π_T(e_i + e_d) = π_T(e_d)`. ∎
>
> *(c)* Hence `J(X_d)` is not `k`-determined for any `k ≤ d−1`, and `k ≥ d` is vacuous. ∎
>
> Verified in every dimension `3 ≤ d ≤ 8`, with `|J(X_d)| = 2^{d−1}` throughout. **`information`
> escapes the near-unanimity family entirely — not for small `k`, but for all of it.**

**Axis 2 — the factors.** The abstract form needs only `A_i ∈ V`. **Lemma 5 needs chains**, and that is
where the law is sharp: off the chains `⟨X⟩ ⊆ R(X)` fails while `R(X) ⊆ ⟨X⟩` survives, so the staircase
**under**-generates (§8, N2), and no attainment-strictness repairs it (§8, N2a). The abstract layer
survives arbitrary factors in `V`; **the computational layer does not.**

**Axis 3 — the index set.** `|I|` finite is what Theorem 3(i) of the source requires. Dropping it
breaks the representation — Queyranne–Tardella's Example 2 (finite subsets of an infinite index set) is
a sublattice whose 2-fold projections are everything. Subcompleteness conditions (their (ii)) recover
it. **The factors need not be finite; the index set does.**

### What is general and what is ours

| layer | statement | status |
|---|---|---|
| abstract | NU term ⟹ `k`-decomposability | **PRIOR ART** — Baker & Pixley 1975 |
| representation | the hull is fixed by 2-fold projections, chains | **PRIOR ART** — Queyranne–Tardella Thm 11 |
| computational | the projections are `φ`; the four-witness construction | Lemma 5 — **ours as written, theirs in substance** |
| the five operators | Clauses A, C, D, F, G, H | **ours** |

**The honest summary of the generalization.** Clause B generalizes cleanly along Axis 1 and Axis 3 and
**not at all along Axis 2**. Clauses C, F, G and H are statements about five specific operators and do
not generalize beyond them — they are facts about *this* cypher, not about closure operators at large.

---

## §9 · Provenance ledger

| item | status | source |
|---|---|---|
| **B**, `R(X) = ⟨X⟩` | **PRIOR ART, READ** | Queyranne & Tardella, *Discrete Math.* **308**(9) (2008) 1508–1523 — Prop 1, Thm 9(ii), Thm 11 |
| the lift, abstractly | **PRIOR ART, CITED-UNREAD** | Baker & Pixley, *Math. Z.* **143** (1975) 165–174, DOI 10.1007/BF01187059 |
| sublattices of finite products | **PRIOR ART, CITED via Q–T, RESOLVED** | Topkis [16, Thm 1] = D.M. Topkis, *The structure of sublattices of the product of n lattices*, **Pacific J. Math. 65 (1976) 525–532**. Bracket number read off Queyranne–Tardella's own bibliography, now transcribed in `refs/QUEYRANNE-TARDELLA-2008.md` §References. **Not read in the original**; the theorem's content is taken from Q–T's statement of it |
| products of chains | **PRIOR ART, CITED via Q–T, RESOLVED** | Veinott [18, Cor 11] = A.F. Veinott Jr., *Representation of general and polyhedral subsemilattices and sublattices of product spaces*, **Linear Algebra Appl. 114/115 (1989) 681–704**. Stated there for *certain* sublattices of an arbitrary product of chains — the restriction is in Q–T's text and must not be dropped. **Not read in the original**, as above |
| `⟨X⟩` as sublattice closure | **PRIOR ART** | Birkhoff, *Lattice Theory* — already `op_algebra`'s citation |
| the majority term | **PRIOR ART, STANDARD** | `m(x,y,z) = (x∧y)∨(y∧z)∨(z∧x)` |
| Lemmas 1–3, Clause **A** | **OURS, PROVED** | §2–§3 |
| Lemma 5, the four-witness construction | **OURS AS WRITTEN, THEIRS IN SUBSTANCE** | §4.2. Queyranne–Tardella Theorem 9(ii) is the same statement; the four-witness proof is written here, the result is not new. §4.4 maps them |
| **N1 sharp (Lemma N1\*)** | **OURS, PROVED + MACHINE-CHECKED** | the necessary-and-sufficient corollary in §8; order-convexity is demoted to *sufficient for that corollary* |
| **N2** one-directional failure off chains | **OURS, EXHAUSTIVE** | §8 |
| Clause **C** | **OURS, PROVED** | §5 |
| Clause **D** | **OURS, PROVED** | §6 — three of four cases trivial, and said so |
| Clause **E** | **OURS, REFUTATION** | §7 |
| the code-to-mathematics bridge | **OURS, EXHAUSTIVE** | `decomposable.py`, 400/400 |

**Naming corrections carried by the ledger.** The property in Lemma 7 is called **k-decomposability**.
It is *not* "near-unanimity" — that names the *term*, and a `(k+1)`-ary near-unanimity term is what is
*equivalent* to k-decomposability. It is *not* "skew-free" — that is the Fraser–Horn property about
congruences of a product, a different statement that sits in the same textbook section.

**On the reconstruction.** `refs/QUEYRANNE-TARDELLA-2008.md` covers Sections 1–3, the start of 4, and
the Acknowledgements, References and the Theorem 9 attribution endnote, transcribed from screenshot
OCR because every publisher route is blocked from this environment. Prose is close to verbatim;
**mathematical notation was restored by hand and is a reading**. Two displayed formulas are marked
uncertain. Do not quote a formula from it without checking the paper.

**The two rows above read `RESOLVED` only as of the final pass.** They stood at `UNRESOLVED` because
the first transcription stopped at Lemma 21 and never reached the reference list — which was in the
screenshot set the whole time. The lesson is filed rather than hidden: **an `UNRESOLVED` provenance
row is a claim about this repository's reading, never about the source.** The endnote recovered with
the bibliography is also the authors' own division of credit for Theorem 9, and it is quoted in full
there: condition (i) ⟹ (2) is Topkis's Theorem 1 with their Proposition 1, or Veinott's Corollary 11
when every factor is a chain, and **condition (ii) they claim as new**. That is the clause this paper
imports, and Queyranne–Tardella are its authors.

---

## §10 · Verification record

Every filename in this paper is relative to `research/warp-drive/`: the law is `law.py`, its
formalization `decomposable.py`, the machine checking `machinecheck.py` over the harness `prover.py`
(route in `PROOF-ASSISTANT.md`), the figures `lawfigures.py`, the evidence for Clause E `induce.py`,
and the reconstructed prior art `refs/QUEYRANNE-TARDELLA-2008.md`.

**EXHAUSTIVE and SAMPLED are different words here.** A figure like "300/300" is a *seeded pseudorandom
sweep*, not a decision procedure over a finite family, and an earlier draft filed both under
EXHAUSTIVE. They are separated below. Every SAMPLED figure is reproduced by `lawfigures.py` with its
generator and seed; every EXHAUSTIVE figure names the family it exhausted.

| object | PROVED | EXHAUSTIVE | SAMPLED (seeded) | MACHINE-CHECKED (Z3) |
|---|---|---|---|---|
| Lemmas 1, 2, 3 | ✓ | — | 400 nested pairs | — |
| Clause A, five operators | ✓ | — | 300 worlds | — |
| **Lemma 4** | ✓ | — | — | **✓ 3×3, 4×4, 2³, 3×3×3** |
| Lemma 5 (`d = 2`) | ✓ | **54,392 cells, construction built** | — | **✓ via Clause B at d = 2** |
| Lemma 7 (the lift) | **cited** | 4,128 sublattices | — | — |
| **Clause B** | cited + ✓ | **36,252 cases** | — | **✓ 2×2, 3×3, 4×4, 2³, 3×3×3** |
| **Clause C** (engine, Lemma 8) | ✓ | — | 600 worlds | **✓ 3×3, 2³, 3×3×3** |
| **Clause C** (⊆ algebra) | ✓ | — | 200 positions | **✓ 3×3, 2³, 3×3×3** |
| Clause D | ✓ | — | 150 worlds + explicit witness | — |
| Clause E | refutation | — | 400 worlds | — |
| Clause F | ✓ + 4 witnesses | — | 400 draws | — |
| Clause G | ✓ (G.1, G.3, G.4) | — | 500 worlds; control 98/500 | — |
| Clause H | ✓ + 6 witnesses + the §6d proof | — | 600 worlds | — |
| **N1 (sharp, Lemma N1\*)** | ✓ | **702,628 cases** | — | **✓ both directions, 3×3, 4×4, 3×3×3** |
| N2 / N2a (non-chain) | ✓ (direction) | 6,440 instances × 2 ambients | — | — |
| §8d, `information` at every `k` | ✓ (construction) | `d = 3…8` | — | — |
| code ↔ mathematics bridge | — | — | 400 indexes, 3 of 5 operators | — |

**21 of 21 machine-check obligations discharged** (`machinecheck.py`, Z3 5.1.0), behind two soundness
guards that must pass first.

### What machine-checking bought that enumeration could not

Obligations are quantified formulas whose variables range over **every** subset `X` of the box — and,
where `⟨X⟩` appears, over **every** closed superset `S`. Z3 returns `unsat` on the negation.

> At `d = 3` over a 3×3×3 box that is **2²⁷ = 134,217,728 subsets**. The enumeration frontier there
> (`decomposable.py`) is `|X| ≤ 4`. **Machine-checking covers cases enumeration cannot enumerate.**

**Two encodings make it decidable.** `φ` and `max` are eliminated — `x ∈ R(X)` iff for all `i ≠ j` there
is `y ∈ X` with `y_j ≤ x_j` and `y_i ≥ x_i`, since a maximum is attained exactly when a witness exists.
And `⟨X⟩` is encoded **without a fixed point**, as the intersection of all closed supersets.

**Two guards run first, and an earlier draft's version of the second was blind.** *Non-vacuity*: an
unsatisfiable hypothesis makes the implication vacuously true, so `unsat` would prove nothing — checked
satisfiable, and satisfiable with `S` strictly inside the box. *Encoding fidelity*: the guard now
**evaluates `prover.in_R` itself**, with `X` pinned to concrete booleans, against the staircase the
repository computes — the earlier version re-typed the witness formula as a Python literal, which tested
the typist rather than the encoding. It carries a **negative control** that fails on a deliberately
wrong reference.

**Scope of each obligation, stated rather than implied.** `lemma4` and `clauseB` carry the `observed`
hypothesis, so they range over every subset **satisfying D1**, not every subset simpliciter. `lemmaN1`
and its reverse carry no such hypothesis. Clause C is discharged in two parts: the **engine** (Lemma 8 —
the join-irreducibles regrow `X`) and the **containment** in `algebra`.

### What remains unchecked, and why

Clauses **D, E, F, G, H** and Lemma 7 are **not** machine-checked. They are not of that shape: **D**
quantifies over *operators*, **E** and **H** are about five specific named operators, **F** over
relabellings, and **Lemma 7** is the cited abstract theorem. Machine-checking them would mean
formalizing the five operators themselves, which is a larger undertaking than this document represents.

---

## §11 · Questions raised in review, and their disposition

Every question this work raised about the law is now closed. They are listed with the manner of
closing, so a reader can check the closing rather than take it.

**1. Do Queyranne–Tardella §4–§6 bear on the law?** **NO — closed by the paper's own §1**, which is
transcribed in full. Their introduction states §4 gives *upper and lower bounds on the number of
sublattices*, §5 a *corner representation … for encoding*, and §6 the *sublattice hull membership
problem and a polynomial-time algorithm*. The representation theorem this work depends on is §2–§3,
and §2–§3 are transcribed complete. Counting, encoding and algorithmics cannot bear on whether the hull
is fixed by its 2-fold projections.

**2. Is order-convexity the weakest sufficient condition for N1?** **NO, and the sharp condition is
now proved** — Lemma N1\* and its corollary in §8: `R_B(X) = ⟨X⟩` **iff** `R_B(X) ⊆ Box(X)`. Necessary
and sufficient, three lines, and 0 failures in 702,628 exhaustive cases. Convexity is a sufficient
condition *for that corollary*.

**3. Does the proper-epigraph formulation rescue the non-chain case?** **NO — closed with a proof**,
§8 N2a. Strictness only removes cells, so `proper ⊆ naive`, while off the chains the failure is
*under*-generation. Attainment-strictness cannot repair under-generation.

**4. Is `information` `k`-determined for no `k`?** **CORRECT, and now a theorem for every `d ≥ 3`** —
the construction `X_d = {0} ∪ {e_i + e_d}` in §8d, Axis 1. This one was reported open in an earlier
draft on the strength of a measurement that turned out to be a size artifact.

**5. Machine-checking.** **DONE for the core, by Z3, and the record says exactly which parts.** Lemma
4, Clause B, both parts of Clause C and **both directions of** Lemma N1\* are discharged over every
subset of the cubic boxes named in §10 — **21 of 21** obligations, `unsat` on each negation
(`machinecheck.py`), behind two soundness guards. Clauses D–H and Lemma 7 are **not** machine
checked, for the reason given in §10: they are not of that logical shape. Each has a written proof and,
where applicable, an explicit witness. **The dichotomy is three-way, not two**: a step is checked by a
solver, checked by a reader, or **taken from the literature** — and §10's PROVED column reads "cited"
for Lemma 7 and "cited + ✓" for Clause B precisely because the lift is imported rather than reproved
here. No clause rests on a step that is *unaccounted for*; one clause rests on a step accounted for by
citation, and §9 says which citation.

### Scope note

Clauses **A–H are the law, and they are complete**. Appendices **§8b** (`analysis`) and **§8c**
(`logic`) are **not clauses of the law** — they concern candidate operators outside the five, filed as
evidence bearing on the roster of operator-bearing languages, and they carry their own status markers. Nothing in A–H depends on
either appendix.
