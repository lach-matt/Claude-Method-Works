# The Hierarchy Law

**A fully derived expansion, with provenance, for review.**

Instrument: `law.py` · Formalization: `decomposable.py` · Refutation of clause E: `induce.py`
Prior art, reconstructed: `refs/QUEYRANNE-TARDELLA-2008.md`

---

## §0 · Scope, and what this document is not

This derives a law about **five closure operators on a finite index**. It is a statement in lattice
theory. It is **not** a statement about spacetime, about energy conditions as physics, or about
whether a warp corridor is buildable. §12 says so again with the numbers.

Three verification statuses are kept apart throughout and never merged:

| status | meaning |
|---|---|
| **PROVED** | a proof is written out below and every step is justified |
| **EXHAUSTIVE** | a decision procedure checked every case in a stated finite family |
| **CITED** | taken from the literature; marked READ or UNREAD |

**Nothing in this document is MACHINE-CHECKED.** There is no proof assistant on the machine this was
produced on and no network route to one.

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

> *Totality is the only place D1 is used in the whole derivation.* Everything else survives without it.

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
— EXHAUSTIVE at 4,000/4,000.

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

The last row is the instructive one. Their *proper* epigraph handles non-attainment by strictness. We
handled it by requiring every ambient value to be observed (D1) — a hypothesis their formulation makes
unnecessary. **They solved by construction what we patched by hypothesis.**

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

**The other four are order-dependent by construction**: `φ` (D4), `∧`/`∨` (D3, D6) and `conv` (D7) are
each defined from `≤`.

**And an independent corroboration of Clause B falls out.** If `order` and `algebra` are one operator
they must break on *exactly the same instances*, not merely as often. Measured: **400 / 400 agreement
on which instances break.** Neither operator was designed with relabelling in mind, so this is Clause B
confirmed by a transformation from outside its own derivation.

**What the clause does and does not support.** The claim under review was that *every rung above the
first requires the language below it*. For `algebra`, `information` and `geometry` that is measured and
true. For `statistics` it is **false** — and `statistics` is the rung the ladder placed at the top.
Necessity of language is a condition of order for four of the five; the fifth needs only identity.

**Status: PROVED** (`statistics`), **EXHAUSTIVE** (the other four, 400 draws).

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

Clause B is an order-theoretic theorem. **A condition stated in the membership register cannot be
necessary for it.** N1's entire role was to *imply* an order fact as a side effect — attainment of the
maxima in Lemma 1 — which it does without stating it. That is exactly why N1 is sufficient-and-not-
necessary while N2 is necessary. **The category explains the necessity**, and no counterexample was
needed to see it. The counterexamples in §8 confirm what the register already forces.

**G.6 — what is NOT testable here, stated so it is not smuggled in.** The review's chain runs
*statistics gives the `if` → analysis gives the `then` → logic verifies both against the original
geometry.* The first and third steps are measured above and hold. **The middle step cannot be
measured**: `analysis` has **no operator** in the cypher — it is declared-only — and which languages
exist is open docket 20x-04/20x-09. **No operator for `analysis` was invented for this clause**, and
none should be until that docket is ruled on.

---

## §6d · Clause H — the lawful skeleton: which part of the ranking *is* a law

Clause E refutes the *total* ranking. It does not follow that no ordering is lawful, and review
pressure made that worth measuring. Over 600 worlds, exactly **seven** containments hold without
exception:

| holds always | |
|---|---|
| `order ⊆ algebra` and `algebra ⊆ order` | **= Clause B, recovered from outside its own derivation** |
| `information ⊆ algebra`, `information ⊆ order` | Clause C |
| `statistics ⊆ algebra`, `statistics ⊆ order` | |
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
| `statistics` is the **minimum** | 106 / 400 |
| `statistics` is the **maximum** | **128 / 400** |
| `geometry` vs `information` | `info < geom` 183 · incomparable 144 · equal 57 · `geom < info` 16 |
| `order` is the maximum | 398 / 400 (both exceptions `geometry`, both incomparability) |

And **two indexes the corpus itself seats already disagree**:

> NEC index: `statistics < geometry < information < algebra = order`
> periodic 3-D: `statistics < information < geometry < algebra = order`

`geometry` and `information` **swap**. Nothing had to be generated to find this; it was available all
along and was not looked at.

**Status: REFUTATION, EXHAUSTIVE.** The ladder this work ran on was a property of one 17-cell index.

---

## §8 · Necessity — each hypothesis dropped until it breaks

> **The two hypotheses are not peers, and review corrected this.** N2 is the *order language* being
> present and total. N1 is a bookkeeping condition about attainment. The reading offered was: *"language
> is order; if order is necessary for algebra, so is the language."* Clause F measures exactly that —
> scramble the order and `algebra` changes in 342 of 400 draws. **So the necessary hypothesis of Clause
> B is the language (N2), and N1 is not necessary at all.** They are listed in that order below and the
> emphasis has been moved accordingly.

**N1 · `A_i = π_i(X)` (observed alphabet) — SUFFICIENT, NOT NECESSARY. A BOOKKEEPING CONDITION.**
Recorded earlier in this work as *necessary*; that was wrong. Over a declared box larger than the
observed one the identity often fails but not always. A weaker sufficient condition is
**order-convexity**: no value of `A_i` strictly between `min π_i(X)` and `max π_i(X)` may go
unobserved; values above the max or below the min are harmless. Measured: **convex → 1,853 hold, 0
fail**; **gapped → 632 hold, 1,643 fail**. So convexity is *also* sufficient and not necessary.
Minimal counterexample: `d = 2`, box of 3 cells, `X = {(0,0),(2,0)}` with value 1 unobserved —
staircase 3 cells, sublattice 2.
*Queyranne–Tardella need no such hypothesis at all: their proper boundary epigraph handles
non-attainment by strict inequality.*

**N2 · each `A_i` a chain — NECESSARY. THIS IS THE LANGUAGE CONDITION, and the failure is one-directional.**
Off the chains the staircase **never over-generates**; it **under**-generates. `R(X) ⊆ ⟨X⟩` survives
arbitrary finite lattice factors — it is Lemma 4, which needs `φ` isotone and hence a total order,
that dies. Measured over non-chain factors:

| factors | equal | staircase ⊃ sublattice | staircase ⊂ sublattice |
|---|---|---|---|
| chain × chain | 120 / 120 | 0 | 0 |
| M3 × chain | 290 / 560 | **0** | 270 |
| M3 × M3 | 700 / 2600 | **0** | 1900 |
| N5 × chain | 371 / 560 | **0** | 189 |
| N5 × N5 | 1144 / 2600 | **0** | 1456 |

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

## §9 · Provenance ledger

| item | status | source |
|---|---|---|
| **B**, `R(X) = ⟨X⟩` | **PRIOR ART, READ** | Queyranne & Tardella, *Discrete Math.* **308**(9) (2008) 1508–1523 — Prop 1, Thm 9(ii), Thm 11 |
| the lift, abstractly | **PRIOR ART, CITED-UNREAD** | Baker & Pixley, *Math. Z.* **143** (1975) 165–174, DOI 10.1007/BF01187059 |
| sublattices of finite products | **PRIOR ART, CITED via Q–T** | Topkis [16, Thm 1] |
| products of chains | **PRIOR ART, CITED via Q–T** | Veinott [18, Cor 11] |
| `⟨X⟩` as sublattice closure | **PRIOR ART** | Birkhoff, *Lattice Theory* — already `op_algebra`'s citation |
| the majority term | **PRIOR ART, STANDARD** | `m(x,y,z) = (x∧y)∨(y∧z)∨(z∧x)` |
| Lemmas 1–3, Clause **A** | **OURS, PROVED** | §2–§3 |
| Lemma 5, the four-witness construction | **OURS, PROVED** | §4.2 — no source known; **no novelty claimed** |
| **N1** order-convexity | **OURS, PROVED + EXHAUSTIVE** | supersedes this work's mistaken necessity claim |
| **N2** one-directional failure off chains | **OURS, EXHAUSTIVE** | §8 |
| Clause **C** | **OURS, PROVED** | §5 |
| Clause **D** | **OURS, PROVED** | §6 — three of four cases trivial, and said so |
| Clause **E** | **OURS, REFUTATION** | §7 |
| the code-to-mathematics bridge | **OURS, EXHAUSTIVE** | `decomposable.py`, 400/400 |

**Naming corrections carried by the ledger.** The property in Lemma 7 is called **k-decomposability**.
It is *not* "near-unanimity" — that names the *term*, and a `(k+1)`-ary near-unanimity term is what is
*equivalent* to k-decomposability. It is *not* "skew-free" — that is the Fraser–Horn property about
congruences of a product, a different statement that sits in the same textbook section.

**On the reconstruction.** `refs/QUEYRANNE-TARDELLA-2008.md` covers Sections 1–3 and the start of 4,
transcribed from screenshot OCR because every publisher route is blocked from this environment. Prose
is close to verbatim; **mathematical notation was restored by hand and is a reading**. Two displayed
formulas are marked uncertain. Do not quote a formula from it without checking the paper.

---

## §10 · Verification record

| object | PROVED | EXHAUSTIVE frontier | MACHINE-CHECKED |
|---|---|---|---|
| Lemma 1, 2, 3 | ✓ | 400 nested pairs, 0 failures | ✗ |
| Clause A, five operators | ✓ | 300/300 | ✗ |
| Lemma 4 (easy inclusion) | ✓ | — | ✗ |
| Lemma 5 (`d=2`) | ✓ | **54,392 cells, construction built** | ✗ |
| Lemma 7 (the lift) | cited | **4,128 sublattices, 0 exceptions** | ✗ |
| Clause B overall | cited + ✓ | **36,252 cases, 0 failures** | ✗ |
| Clause C | ✓ | 200/200; 600 worlds | ✗ |
| Clause D | ✓ | 150/150 + explicit witness | ✗ |
| Clause F | ✓ (`statistics`) | 400 draws; B corroborated 400/400 | ✗ |
| Clause G | ✓ (G.1, G.3, G.4) | 500 worlds each; control 98/500 | ✗ |
| Clause H | ✓ (the four relations) | 600 worlds, 7 always-containments | ✗ |
| N2a (proper epigraph) | ✓ | 6,440 non-chain instances | ✗ |
| Clause E | refutation | 400 worlds, 14 orderings | ✗ |
| N1 | ✓ | 1,853 convex / 2,275 gapped | ✗ |
| N2 | — | 6,440 non-chain instances | ✗ |
| code ↔ mathematics bridge | — | 400/400 | ✗ |

**The MACHINE-CHECKED column is empty and that is the honest ceiling.** A Lean 4 development exists
for Lemma 5 with a complete proof and for the general case with an explicit `sorry` at the lift; no
kernel has seen either.

---

## §11 · Open questions

1. Does Queyranne–Tardella §4–§6 (untranscribed) bear on any of this? Their counting and membership
   results were not read.
2. Is order-convexity the **weakest** sufficient condition in the fixed-box regime, or merely weaker
   than D1? The 632 gapped-but-holding worlds say a sharper condition exists.
3. ~~Can the proper-epigraph formulation recover equality off the chains?~~ **ANSWERED: NO.** See
   §8, N2a.
4. Is `information` provably **never** k-determined for any `k`, via the absence of a near-unanimity
   term in join-semilattices? Measured failure at `k=2` and `k=3`; not proved.
5. Machine-check Lemma 5 and Clause B.

---

## §12 · What the law does not do

It does not advance the warp corridor, and no version of it can. The law concerns closure operators on
a finite index. The obstruction is two measured physical quantities, neither touched by anything above:

> **`persist.py`** — a shortfall of **69.03 orders of magnitude** between the mass the corridor
> requires and the mass a Ford–Roman bound permits.
>
> **`higgs.py`** — a required non-minimal coupling **ξ ≥ 9.782907 × 10³¹** for the Barceló–Visser
> effective-ANEC gate at the electroweak VEV; the hierarchy problem squared.

What the law provides is narrower and real: the cypher's verdicts on an index now rest on a **published
theorem** rather than on agreement among five operators, two of which are one operator. **That makes
the cypher citable. It does not make the corridor closer.**

**Nothing in this document repairs anything.** `tools/cypher.py` is read, never written.
