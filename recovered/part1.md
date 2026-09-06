
---

# PART I — THE LATTICE

---

# 1. The periodic table is not a closed index

Take the periodic table at its word. Its coordinates are period and group;
its cells are the elements. Ask what those coordinates, and the occupied
cells alone, imply about which other cells could exist.

The answer is thirty-six cells that do not.

| | |
|---|---|
| main-table cells (lanthanides and actinides set aside) | 90 |
| cells the structure admits | 126 |
| **external definition cost E(X)** | **36** |

The thirty-six are (p1, g2) through (p1, g17), (p2, g3) through (p2, g12),
and (p3, g3) through (p3, g12) — **the gaps in the short periods, every one
of them.**

This is not a defect in the periodic table. It is a fact about what the
periodic table's coordinates can and cannot carry. Period and group locate an
element; they do not encode why period 1 has room for two elements and period
4 for eighteen. That information travels alongside the table, in the
schooling of whoever reads it.

## 1.1 What "the structure admits" means

The reconstruction is mechanical. Given a set of cells X on coordinates
(*x*₁, …, *x_d*), read off two things:

> the **value sets** Âᵢ(X) = { *xᵢ* : *x* ∈ X } — which values occur
> the **bounds** φ̂ᵢⱼ(*v*) = max{ *xᵢ* : *x* ∈ X, *xⱼ* ≤ *v* } — how far one
> coordinate reaches given another

and then form

> **𝓡(X) = { *x* ∈ ∏ Âᵢ(X) : *xᵢ* ≤ φ̂ᵢⱼ(*xⱼ*) for all *i* ≠ *j* }**

No outside knowledge enters. 𝓡(X) is what a reader could reconstruct from the
cells alone.

**E(X) = |𝓡(X)| − |X|** is the gap: cells the structure implies and the index
denies. For the periodic table it is 36. For Λ, built in the next chapter, it
is 0.

## 1.2 It is not a peculiarity of chemistry

The same computation on other indices:

| index | \|X\| | E(X) | self-defining |
|---|---|---|---|
| a box ordering, *l* ≥ *w* ≥ *h* | 56 | **0** | yes |
| a nuclide chart with drip lines | 383 | **0** | yes |
| a chessboard | 64 | **0** | yes |
| **Λ** | 976 | **0** | **yes** |
| a subnet with a hole | 248 | 8 | no |
| **the calendar**, (month, day) | 365 | **7** | **no** |
| **the periodic table** | 90 | **36** | **no** |

The calendar's seven are (2,29), (2,30), (2,31), (4,31), (6,31), (9,31) and
(11,31).

**That is the content of *Thirty days hath September*.** The rhyme exists
because the calendar's coordinates cannot carry the month lengths, and the
rhyme is exactly seven cells long.

## 1.3 The calendar can be repaired, and the repair is instructive

The calendar fails for one reason: days(*m*) is not monotone in *m*, because
February has 28. Relabel the months in order of length — February, April,
June, September, November, January, March, … — and **E drops to 0.** The 365
cells are identical; only the labels move.

**And the repaired calendar is useless.** A calendar whose months run in order
of length is self-defining and unusable.

So the trade is explicit, and it has a number:

> **E(X) = 7 is the price of keeping January first.**

Non-closure is not always a fault. It is sometimes a purchase — usability
bought with definitional self-sufficiency. What this book supplies is the
price tag, not the verdict.

## 1.4 What follows

Λ is the same 118 elements on different coordinates, with E = 0. It adds no
physics. What it removes is the thirty-six.

The rest of Part I builds it and establishes what it is. Part II proves why
E = 0 is not an isolated virtue but the source of two others.

---

# 2. The construction of Λ

Λ is a set of eight-tuples. Each is a *transition cell*: a source
configuration, a target configuration, and the electron count moved between
them.

> **(n, ℓ, k, q, e, f, g, 2S)**

| | |
|---|---|
| *n* | source shell |
| ℓ | source subshell |
| *k* | source occupancy |
| *q* | electrons removed |
| *e* | target shell |
| *f* | target subshell |
| *g* | target occupancy |
| 2*S* | multiplicity |

Three further coordinates — 2*J*_c, 2*J*, *K* — extend Λ₈ to Λ₁₁ when
angular-momentum coupling is carried explicitly. Everything in this book that
does not concern coupling is stated for Λ₈.

## 2.1 The constraints, and where each comes from

Λ is not all of the eight-fold product. It is the subset satisfying:

| constraint | origin |
|---|---|
| ℓ ≤ *n* − 1 | hydrogenic radial solution |
| *k* ≤ 2(2ℓ + 1) | Pauli exclusion |
| *q* ≤ *k* | counting — cannot remove more than are present |
| *f* ≤ *e* − 1 | hydrogenic radial solution |
| *g* ≤ 2(2*f* + 1) | Pauli exclusion |
| *g* ≤ *q* | counting — cannot place more than were removed |
| 2*S* ≤ *k* | vector coupling |

**Seven constraints, four origins, and nothing else.** No constraint in Λ
comes from anywhere but Pauli, the hydrogenic radial solution, counting, or
angular-momentum coupling. That exhaustiveness matters in Part II, where it
is the reason the object's properties can be attributed to *indexing* rather
than to physics smuggled in through a bound.

## 2.2 Every constraint is of one form

Each constraint reads *xᵢ* ≤ φ(*xⱼ*) — one coordinate bounded by a monotone
function of **one other**. None is a sum. None is a difference. That is not
an accident of presentation; Chapter 10 shows that a sum could not appear
here, because a set cut out by a sum bound is not closed.

**Consequence, developed in Chapter 3:** the graph whose nodes are
coordinates and whose edges are constraints is a **tree**.

## 2.3 Λ is closed

For any two cells *x*, *y* ∈ Λ, both *x* ∨ *y* and *x* ∧ *y* — the
coordinatewise maximum and minimum — are again in Λ.

*Proof.* Each constraint is *xᵢ* ≤ φ(*xⱼ*) with φ non-decreasing. Suppose
(*x*∨*y*)ᵢ = *xᵢ*. Then

> (*x*∨*y*)ᵢ = *xᵢ* ≤ φ(*xⱼ*) ≤ φ(max(*xⱼ*, *yⱼ*)) = φ((*x*∨*y*)ⱼ)

by monotonicity. Meets are symmetric. ∎

**And E(Λ) = 0**, verified by direct computation at four cap settings — 216,
976, 1,636 and 2,394 cells — exact in one step and stable under a second
application of 𝓡.

## 2.4 A note on caps

Λ is infinite; every count in this book is stated at explicit caps on *n*,
*e*, ℓ and *k*. **The counts change with the caps. The shape does not** — a
claim made precise in Chapter 3, where the generator patterns are shown
identical across a twenty-eight-fold range in cell count.

Where a number is cap-dependent it is marked. Where a structural claim is
made, it has been checked at no fewer than four settings.

---

# 3. What Λ is

## 3.1 Distributive

Λ is a sublattice of a product of chains, and every such sublattice is
distributive. Verified on 4,000 randomly drawn triples, no failures.

This is the least surprising fact in the chapter and the most load-bearing:
it is what admits Birkhoff's representation, which is the next section.

## 3.2 Seventeen generators

By Birkhoff's theorem, a finite distributive lattice is the lattice of
down-sets of its poset of join-irreducibles. For Λ at caps (3,3,2,3):

> **976 cells ← 17 join-irreducibles, 20 covering relations**

and the correspondence is exact: **all 976 down-sets of the 17-element poset
are precisely the 976 cells.** A fifty-seven-fold compression.

**The covering relations are the physics made visible:**

| cover | reads |
|---|---|
| *e*=2 ⋖ *e*=2, *f*=1 | a target subshell requires its shell |
| *k*=2 ⋖ *k*=2, *q*=2 | you may remove what you have |
| *n*=2 ⋖ *n*=2, ℓ=1 ⋖ *n*=2, ℓ=1, *k*=3 | shell before subshell before occupancy |

**And the shape is cap-independent.** Across six settings from 976 to 27,873
cells the generator count grows — 17, 23, 31, 32 — while the *patterns* hold
at **fifteen, with zero new and zero lost.** Only multiplicities change.

That is what licenses stating the poset once.

## 3.3 Sperner, and not symmetric

The largest antichain in Λ equals its largest rank level — the Sperner
property — verified exactly at five cap settings by Dilworth's theorem and
bipartite matching, no exceptions. At caps (3,3,2,3) the maximum is **122 at
rank 11**.

The rank sequence is **log-concave**, hence unimodal, which is why Sperner
holds rather than merely happening to.

**But Λ is not rank-symmetric**, so it has **no symmetric chain
decomposition** and the classical result for divisor lattices does not
transfer. The asymmetry is itself a measurement:

> centre of mass 11.07 against midpoint 11.5 — **skew −0.43**

Low ranks are cut by floors (*n* ≥ 1, *k* ≥ 1, *e* ≥ 1); high ranks by caps
(ℓ ≤ *n*−1, *k* ≤ 2(2ℓ+1), *q* ≤ *k*, *g* ≤ *q*). **There are more caps than
floors, so the top is pruned harder.** The skew is how much more Pauli
constrains than counting does.

**Nor is Λ self-dual.** Only 8 of 976 cells survive *x* ↦ cap − *x*. The two
sides of the object are genuinely distinguishable, which Chapter 6 develops.

## 3.4 The constraint graph is a tree

Eight coordinates, seven constraints, connected:

> **e — f — g — q — k — ℓ — n**,  with **2S** attached to **k**

**Treewidth 1.** Three consequences run through the rest of the book:

**The void needs no sieve.** A tree has no cycles, so there is nothing for
inclusion–exclusion to correct. Chapter 5 gives the closed-form count.

**The order is recoverable.** Chapter 8 recovers Λ's coordinate orders from
an unlabelled bag of cells by propagation along this tree — 20 of 20.

**And the constraint graph offers no redundancy.** There is exactly one path
between any two nodes. So the two-route protection of Chapter 9 cannot come
from the constraints; it must come from derived quantities. **That is a real
constraint on how the object defends itself, and it is visible here, three
chapters early.**

## 3.5 Order dimension

Λ₈ has order dimension exactly 8, rising by one per adjoined axis, with zero
redundant coordinates. Every axis carries information no combination of the
others supplies.

Λ occupies **6.0%** of its own bounding box — 976 cells of 16,384.

---

# 4. The arithmetic encoding

Assign the *i*th coordinate the *i*th prime and read a cell as an integer:

> **N(x) = ∏ᵢ pᵢ^{xᵢ}**

The lattice becomes arithmetic, exactly:

| lattice | arithmetic |
|---|---|
| *x* ≤ *y* | **N(x) divides N(y)** |
| *x* ∨ *y* | **lcm** |
| *x* ∧ *y* | **gcd** |
| rank Σ*xᵢ* | **Ω(N)**, prime factors with multiplicity |

> **Λ is a sublattice of the divisor lattice of a single integer.**

## 4.1 Two classical functions appear as lattice quantities

**rank(x) = Ω(N(x))** — verified on all 976 cells.

**ω(N(x)) ≤ dim(Λ)** — the count of *distinct* primes is bounded by the order
dimension, and the bound is tight. *Proof:* N(x) = ∏pᵢ^{xᵢ} uses at most one
prime per coordinate. ∎

**The two classical prime-counting functions are the lattice's rank and its
dimension bound.** Neither was put there.

## 4.2 The occupancy measure

> **d(x, y) = τ( lcm(N(x),N(y)) / gcd(N(x),N(y)) )**

with τ the divisor-counting function. **d(x,x) = 1**, because τ(1) = 1.

That is not a convention. A point has no volume, but it is one point, and it
counts itself. The measure counts *cells*, and a cell is occupied.

**Five equivalent forms**, verified 500/500 and 2,000/2,000:

1. |[*x*∧*y*, *x*∨*y*]| — interval count
2. ∏ᵢ(|*xᵢ* − *yᵢ*| + 1) — coordinate form
3. τ(N(x)N(y)/gcd²) — two integers
4. **τ(a·b) where N(x)/N(y) = a/b in lowest terms — one rational input**
5. ∏_p(|*v_p*(ρ)| + 1) — *p*-adic

**Properties.** Symmetric · *d* ≥ 1 with equality iff *x* = *y* ·
**multiplicative** triangle inequality *d*(*x*,*z*) ≤ *d*(*x*,*y*)·*d*(*y*,*z*),
4,000 of 4,000 · **log *d* is an ordinary ℓ¹ metric** · balls are hyperbolic,
with boundary (1+Δ₁)(1+Δ₂) = D · each axis is a log-distorted chain, first
step log 2, tenth step log(11/10).

## 4.3 The Möbius function in closed form

Since Λ ≅ J(P) with |P| = 17:

> **μ(x,y) = (−1)^{|y∖x|} if y∖x is an antichain in P, and 0 otherwise**

Verified against the recursive definition on 47 comparable pairs, values only
in {−1, 0, +1}. **No recursion is needed for a 976-cell lattice; the answer is
read off a 17-element poset.**

**And a transfer condition to the arithmetic side:** μ_Λ = μ_arith **iff** the
interval is a void-free unit hypercube. Exact — 60 void-free pairs all agree,
56 void-bearing pairs all disagree, no mixed case. Decidable in seven
comparisons.

---

# 5. The void

Between two cells sits a box. Not all of it is Λ.

> **void(x,y) = ∏ᵢ(|Δᵢ| + 1) − |[x∧y, x∨y] ∩ Λ|**

## 5.1 What the void is made of

The excluded cells are exactly those forbidden by Pauli (*k* > 2(2ℓ+1),
*g* > cap), by the hydrogenic bound (ℓ ≥ *n*, *f* ≥ *e*), or by counting
(*q* > *k*, *g* > *q*).

> **The void is the shadow of the exclusion principle.**

## 5.2 Its size, and its stability

**The void-free fraction is 27.7–30.1%** across 776 million pairs and a
seventeenfold range in cell count. Stable, no trend.

**And the constraints are correlated.** Satisfied individually 67–94%; their
product is 20.19%; the joint figure is **30.13%** — a factor of **1.49** above
independence. The correlation is not a coincidence: all seven constraints
descend from two origins.

## 5.3 Containment in seven comparisons

A box is entirely inside Λ iff hi_i ≤ φ(lo_j) for each of the seven
constraints. **O(1), verified against enumeration on 3,168 pairs.**

## 5.4 The count, with no sieve

Because the constraint graph is a tree, the count factorises:

> |box ∩ Λ| = Σ over *n*, ℓ, *k*, *q*, *e*, *f* of
> [ℓ ≤ *n*−1][1 ≤ *k* ≤ 2(2ℓ+1)][*q* ≤ *k*][*f* ≤ *e*−1] · **#{2S ≤ k}** · **#{g ≤ min(q, 2(2f+1))}**

with the two leaves in closed form:

> **#{2S} = max(0, min(hi₇, k) − lo₇ + 1)**
> **#{g} = max(0, min(hi₆, q, 2(2f+1)) − lo₆ + 1)**

Verified against direct enumeration on eight random intervals.

**No Möbius function. No 2⁷-term inclusion–exclusion.** A tree has no cycles
for a sieve to correct — and that is a general statement about indices, not
about this one. **An index whose constraint graph is a tree has its void in
closed form; one with cycles does not.**

---

# 6. The shape

## 6.1 A cylinder, not a Möbius band

Λ's derived quantities fall into two classes:

| **ascending** — rise up a series | **descending** — fall up a series |
|---|---|
| *e*, ν, *V* | *T*, *r*, δ, spacing, *w* |

exchanged under ν ↦ ν⁻³.

**The sign structure is bipartite**, and a bipartite structure can never
produce an odd number of orientation reversals. Verified exhaustively: **zero
reversing loops among all cycles of length 3 to 5.**

> **Λ is orientable. It is a cylinder.**

That is a *reason*, not an absence. And both alternative routes to a Möbius
band close: a non-monotone quantity has **undefined** edges rather than
reversing ones; a quantity independent of ν has **no** edge. There is no third
option.

## 6.2 "Over ν", not "graded by ν"

ν grades every *chain* of Λ. It grades Λ itself **nowhere** — 24 of 70
comparable pairs have ν decreasing.

**That near-miss is the structure in one sentence.** The bracket of Part III
operates along chains *because that is exactly where ν is a grading.*

The name follows: **the Lach Index Lattice — a hydrogenic cylinder over ν.**
Not *graded by*. *Over.*

## 6.3 One scale, and one exception

Height goes as ν⁻², the metric as ν⁻³, and **the only linearly rising
quantity in the entire structure is the price of a guarantee.** Chapter 14
derives it.

## 6.4 The loop closes

Λ₈ → derived quantities (*V*, *r*) → the bound lattice → dimension 1 =
log *r* = **−3 log ν**, with residual **8.9 × 10⁻¹⁶**.

Λ *decomposes* ν and gains dimension; the bound lattice *recomposes* it and
sheds dimension. **Two sides of one object, not two passes over it.**

## 6.5 What Λ is a property of

Λ is a property of the **hydrogenic limit**. δ — the quantum defect — is the
entire remainder.

> **Prediction lives only in the remainder.**

Which is why perfecting the index moves nothing, and why that is a theorem
rather than a disappointment. Part II proves it; Part III measures what is
left.