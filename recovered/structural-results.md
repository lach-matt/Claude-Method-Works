# Structural results — for the book

*Everything here was established this session and is **not** in
`indexing-without-prediction.pdf`. Verification counts are stated per result.*

---

## PART A — THE LAW OF COMPLETE INDICES

### A1. The three coordinates

An index has three properties, all resting on **closure**, each with three
mechanisms:

| | | | |
|---|---|---|---|
| **S — reference** | S1 alphabet | S2 order | S3 bounds |
| **D — defence** | D1 𝒟_phys | D2 𝒟_def | D3 χ total |
| **E — extension** | E1 cells | E2 axes | E3 constraints |

**E is derived**: every extension question reduces to S and D. It carries no
independent content — exactly as *V* carries none beyond ν.

### A2. Self-reference (S)

> **𝓡(Λ) = Λ**, where 𝓡 reconstructs value sets Âᵢ = {xᵢ : x ∈ Λ} and bounds
> φ̂ᵢⱼ(v) = max{xᵢ : xⱼ ≤ v}

**Theorem (A.4 restated).** X closed ⟺ 𝓡(X) = X.
Verified: 200 random constructions, 200 agreements. Fixed in one step, stable
under iteration: Λ = 𝓡(Λ) = 𝓡²(Λ).

- **S1 alphabet** — a projection, always succeeds.
- **S2 order** — recoverable by **tree propagation with backtracking** when the
  constraint graph is a tree. **20/20** at two cap settings. Greedy
  propagation gives only 42%/25%; alternating refinement over all axes gives 0%.
  Cost Σᵢ|Aᵢ|!, never ∏ᵢ|Aᵢ|!.
- **S3 bounds** — 56 functions φ̂ᵢⱼ read off the cells, always succeeds.

**Scope**: requires each coordinate *presented as a chain*. Any distributive
factor can be so presented (Birkhoff). Bundling two chains into one coordinate
hides structure from 𝓡.

### A3. Self-defence (D)

> **𝒟 = dim q − rank ∂Φ/∂p ≥ dim q − dim p**

**Theorem.** Rank–nullity. dim q > dim p ⇒ 𝒟 ≥ 1. No closure needed.
Verified: 7 dimension pairs, 420 random nonlinear maps.

For Λ: p = (T, n, Z, σ), q = (ν, δ, V, r, w, e), rank 4, **𝒟 = 2**, spanned by

> (a) *V* = 4ν/3  (b) *w* = *V*·*e*

**The split is canonical.** Tested under Rydberg, power-4, exponential and
logarithmic laws: (a) is PHYSICAL (holds only for Rydberg), the rest
DEFINITIONAL (hold under all four). Verdicts identical under every
perturbation.

- **D1 𝒟_phys** — catches a wrong value in the *data*.
- **D2 𝒟_def** — catches a wrong *derivation*, but **only under independent
  recomputation**. *w* = *V*·*e* is vacuous if *V* is defined as *w*/*e*.
  **The defence is the disagreement between paths, not the relation.**
- **D3 χ_Λ total** — catches a *missing* value coerced to a real one.

**Theorem (totality).** Λ closed ⇒ χ_Λ : ∏Aᵢ → {0,1} is total, being a finite
conjunction of decidable comparisons. Verified: 30,000 uniform ambient points,
values {0,1}, nothing undecided.

**The three failure modes are disjoint**, and each occurred this session:

| mechanism | catches | instance |
|---|---|---|
| 𝓡(Λ) = Λ | rules not recoverable from cells | periodic table, E = 36 |
| 𝒟 ≥ 1 | wrong value in data or derivation | wrong *Z*; *w* = 3ν·*e* |
| χ_Λ total | missing value coerced to a real one | the cap = 4 discard |

### A4. Extension (E)

- **E1 cells.** Λ ∪ {x} closed ⟺ ∀y ∈ Λ: x∨y, x∧y ∈ Λ ∪ {x}. **100% / 288 tests.**
- **E2 axes.** Λ × h closed ⟺ h is a lattice homomorphism. **100% / 424 tests.**
- **E3 constraints.** **{h ≤ q} closed ⟺ h(x∨y) ≤ q for all x,y with h(x),h(y) ≤ q.**
  **100% / 2,513 tests**, nine functions. *q*-dependent — admissibility belongs
  to the pair (h, q), not to h alone.

**Theorem (adjunction never repairs).** For any h : S → H with
S′ = {(x, h(x))}: **S′ closed ⇒ S closed**. Contrapositive: a non-closed set
cannot be repaired by adjoining any function of its coordinates. Verified on
seven functions including identity and constant.

**Three repair routes, and only three**: enlarge, restrict, **reorder**.

---

## PART B — THE EXTERNAL DEFINITION COST

> **E(X) = |𝓡(X)| − |X|**

**𝓡 is a closure operator** — extensive, monotone, idempotent, **150/150 on all
three axioms**. So E(X) is a **closure defect**, a standard object in Galois
theory, formal concept analysis and database dependency theory.

| index | \|X\| | E(X) | self-defining |
|---|---|---|---|
| box *l* ≥ *w* ≥ *h* | 56 | 0 | yes |
| nuclide chart | 383 | 0 | yes |
| chessboard | 64 | 0 | yes |
| **Λ** | 976 | **0** | **yes** |
| **periodic table** (period, group) | 90 | **36** | **no** |
| calendar (month, day) | 365 | 7 | no |
| subnet with a hole | 248 | 8 | no |

**The headline result.** The periodic table is not closed. The 36 cells its own
structure admits and the table denies are the gaps in the short periods —
(p1,g2)…(p1,g17), (p2,g3)…(p2,g12), (p3,g3)…(p3,g12). **You must be told that
period 1 holds two elements; the table cannot tell you.**

**Λ is the same 118 elements re-indexed, with E = 0.** The re-indexing adds no
physics. **What it removes is the external definition cost.**

**The calendar's E = 7** is exactly *(2,29), (2,30), (2,31), (4,31), (6,31),
(9,31), (11,31)* — the content of *Thirty days hath September*. Repairable by
reordering months by length, which drops E to 0 and makes the calendar useless.
**E = 7 is the price of keeping January first.**

---

## PART C — Λ's STRUCTURE

**Distributive** — 4,000 triples, 0 failures. Automatic for a sublattice of a
product of chains.

**Birkhoff reduction.** Λ ≅ the down-set lattice of a **17-element poset**, 20
covering relations. **976 down-sets, 976 cells, isomorphic.** 57× compression.
**Shape is cap-independent**: 15 generator patterns at every setting tested up
to 27,873 cells, zero new patterns; only multiplicities grow (17 → 23 → 31 → 32).

The covers are the constraints made visible:
*e*=2 ⋖ *e*=2,*f*=1 (hydrogenic bound) · *k*=2 ⋖ *k*=2,*q*=2 (conservation) ·
*n*=2 ⋖ *n*=2,ℓ=1 ⋖ *n*=2,ℓ=1,*k*=3 (shell before subshell before occupancy).

**Sperner** — max antichain = largest rank level, exact at five settings
(38, 122, 160, 237, 326), computed by Dilworth via bipartite matching.
**Rank sequence log-concave**, hence unimodal, hence Sperner has a cause.

**Not rank-symmetric** — so **no symmetric chain decomposition**; de Bruijn
(1951) does not transfer. The asymmetry is a measurement: centre of mass 11.07
against midpoint 11.5, **skew −0.43**, because there are more caps (Pauli,
hydrogenic, conservation) than floors.

**Not self-dual** — only 8 of 976 cells survive *x* ↦ cap − *x*. Confirms the
cylinder's two sides are genuinely distinguishable.

**Λ occupies 6.0% of its own bounding box** (976 of 16,384).

**Constraint graph is a TREE** — 8 nodes, 7 edges, connected. **Treewidth 1.**

> **e — f — g — q — k — ℓ — n**, with **2S** on **k**

Consequences: the void needs **no sieve** (below); order recovery works by
propagation (S2); and **the constraint graph offers no redundancy** — exactly
one path between any two nodes — so 𝒟_def must come from derived quantities.

---

## PART D — THE ARITHMETIC ENCODING

> **N(x) = ∏ᵢ pᵢ^xᵢ**  ·  **d(x,y) = τ( lcm(N(x),N(y)) / gcd(N(x),N(y)) )**

**Occupancy measure.** *d*(*x*,*x*) = **1**, because τ(1) = 1 — one cell,
occupied. Not a convention: a point has no volume but is one point.

**Equivalent forms**, all verified 500/500 and 2,000/2,000:

1. |[x∧y, x∨y]| — interval count
2. ∏ᵢ(|xᵢ − yᵢ| + 1) — coordinate form
3. τ(N(x)N(y)/gcd²) — two integers
4. τ(a·b) where N(x)/N(y) = a/b in lowest terms — **one rational**
5. ∏_p(|v_p(ρ)| + 1) — p-adic

**Properties.** Symmetric · *d* ≥ 1 with equality iff x = y · **multiplicative**
triangle inequality *d*(x,z) ≤ *d*(x,y)·*d*(y,z), 4,000/4,000 · log *d* is an
ordinary ℓ¹ metric · balls are **hyperbolic**, boundary (1+Δ₁)(1+Δ₂) = D ·
each axis is a **log-distorted chain**, first step log 2, tenth log(11/10).

**The lattice becomes arithmetic**: *x* ≤ *y* ⟺ N(x) | N(y) · join = **lcm** ·
meet = **gcd** · **Λ is a sublattice of the divisor lattice of one integer.**

**Prime-chain theorem.** #primes = dim(Λ); **ω(N(x)) ≤ dim(Λ)**, tight.
**rank(x) = Σxᵢ = Ω(N(x))** — 976/976. *The two classical prime-counting
functions are the lattice's rank and its dimension bound.*

**Möbius, closed form.** Λ ≅ J(P), so
**μ(x,y) = (−1)^|y∖x| if y∖x is an antichain in P, else 0** — 47/47 against
recursion, values only {−1, 0, +1}. No recursion needed.

**Möbius transfer.** μ_Λ = μ_arith **iff** the interval is a void-free unit
hypercube (every |Δᵢ| ≤ 1). Exact: 60 void-free all agree, 56 void-bearing all
disagree, no mixed cases. Decidable in seven comparisons.

---

## PART E — THE VOID

> **void(x,y) = ∏ᵢ(|Δᵢ|+1) − |[x∧y, x∨y] ∩ Λ|**

**O(1) containment test.** Box ⊆ Λ iff hi_i ≤ φ(lo_j) for every constraint —
seven comparisons, verified against enumeration on 3,168 pairs.

**Void-free fraction ≈ 28%**, exhaustive: 27.7–30.1% across 776 million pairs
and a seventeenfold range in cell count. **Stable, no trend.**

**The constraints are correlated.** Individually satisfied 67–94%; product
20.19%; **joint 30.13%** — a factor of **1.49** above independence, because all
seven descend from two origins (Pauli, the hydrogenic radial solution).

**The sieve — and it is not an inclusion–exclusion.** Because the constraint
graph is a tree:

> |box ∩ Λ| = Σ over *n*, ℓ, *k*, *q*, *e*, *f* of
> [ℓ ≤ *n*−1][1 ≤ *k* ≤ 2(2ℓ+1)][*q* ≤ *k*][*f* ≤ *e*−1] · **#{2S ≤ k}** · **#{g ≤ min(q, 2(2f+1))}**
>
> **#{2S} = max(0, min(hi₇, k) − lo₇ + 1)**
> **#{g} = max(0, min(hi₆, q, 2(2f+1)) − lo₆ + 1)**

Verified against enumeration on eight random intervals, all match. **No Möbius
function, no 2⁷-term sieve** — a tree has no cycles for inclusion–exclusion to
correct.

**The void's identity**: the excluded cells are exactly those forbidden by
Pauli (*k* > 2(2ℓ+1), *g* > cap), the hydrogenic bound (ℓ ≥ *n*, *f* ≥ *e*), or
counting (*q* > *k*). **The void is the shadow of the exclusion principle.**

---

## PART F — THE SHAPE

**Eleven axes.** *n*, ℓ, *k*, *q*, *e*, *f*, *g*, 2*S* generate Λ₈; 2*J*_c, 2*J*, *K*
extend to Λ₁₁. Every bound traces to Pauli, the hydrogenic radial solution,
counting, or vector coupling — **and to nothing else**. Order dimension exactly
8, rising by 1 per adjoined axis.

**Orientable — a cylinder, not a Möbius band.** Zero orientation-reversing
loops among all cycles of length 3–5, and the sign matrix is **bipartite**:

- **ascending** — *e*, ν, *V* (rise up the series)
- **descending** — *T*, *r*, δ, spacing, *w* (fall up the series)

exchanged by ν ↦ ν⁻³. A bipartite sign structure can never produce an odd
number of reversals, so orientability is a *reason*, not an absence.

**Both routes to Möbius close.** A non-monotone quantity (perturbed δ) has
*undefined* edges, not reversing ones. A quantity independent of ν (σ, dilution,
Σ, members) has *no* edge. **There is no third option.**

**The loop closes exactly.** Λ₈ → derived (*V*, *r*) → bound lattice →
dimension 1 = log *r* = **−3 log ν**, residual 8.9 × 10⁻¹⁶. Λ *decomposes* ν and
gains dimension; the bound lattice *recomposes* it and sheds dimension. Two
sides, not two passes.

**One scale.** Height ν⁻², metric ν⁻³, and the only linearly rising quantity is
the price of the guarantee.

**Λ is a property of the hydrogenic limit.** δ is the entire remainder.
**Prediction lives only in the remainder** — which is why perfecting the index
moves nothing, and why that is a theorem rather than a disappointment.

**Name**: *The Lach Index Lattice — a hydrogenic cylinder over ν.* "Over" and
not "graded": ν grades every *chain* of Λ and grades Λ itself **nowhere** — 24
of 70 comparable pairs have ν decreasing. That near-miss is the structure in one
sentence: the bracket operates along chains *because* that is exactly where ν is
a grading.

---

## PART G — THE COST SURFACE

> **V(x, p) = 4x / (h·|p − 1|)**

Two coordinates: position along a series, and the **curvature class** of the
observable. Everything in the paper is the slice *p* = −2, *h* = 1, where it
reads 4ν/3. Verified on power laws *p* = −3…+11, agreement under 1%.

**A pole at *p* = 1.** A straight line has no curvature, so the interpolation
error vanishes and a bracket costs infinitely more than the thing it brackets.
**The method has no domain at *p* = 1** — the only hard singularity in the
structure; every other limit is a threshold with data on both sides.

***V* is a bound, not a tool.** *V* = *w*/*e* contains no σ: improving precision
by **six orders of magnitude** leaves *V* = 26.689 unchanged. **No spectrometer
can buy a narrower bracket.** The four impossibility statements:

| | forbids |
|---|---|
| *V* = 4ν/3 | a guarantee costs 4ν/3 × an estimate, and no measurement reduces it |
| *V* ≥ 32/11 | no guarantee is ever cheaper than 2.909 × |
| pole at *p* = 1 | no guarantee exists for a linear observable |
| ν_V | above the ceiling the cost cannot be *measured* |

**Exact *V* is rational at every ν** — 32/11, 54/13, 256/47, 250/37, 4000/299 —
and 4ν/3 + 4/(9ν) is its asymptotic form, low by 0.69% at ν = 2, exact to four
decimals by ν = 10. **The floor 32/11 belongs to the exact expression.**

**The inversion**, fixed: |*p*−1| = 4*x*/(*hV*), then *p* = 1 ± |*p*−1| with the
sign set by sign(*y*′) and sign(*y*″). Controls now recover *p* = −1 and −3
correctly; 9/10 within 5%. Real series: Na I −1.993, K I −1.998, C₃ 3.999,
α 6.990, **C₆ 10.956**.

**Two involutions on the exponent axis.** Cost *p* ↦ 2−*p* (pairs multiply to
ν²); virial *p* ↦ −*p* (pairs multiply to a constant). Composed, they generate
translation by 2, so exponents fall into **two orbits by parity** — and the
parity is *b*, the number of energy denominators. The pole at *p* = 1 sits in
the odd orbit; **nothing built purely from ⟨r⟩ powers can reach it.**

---

## PART H — COLLECTIVE SECTIONS

> **p = 2a + 3b** for an observable assembled as ⟨*r*⟩^*a* / (Δ*E*)^*b*

**Derived, not fitted**: ⟨*r*⟩ ∝ ν², Δ*E* ∝ ν⁻³.

| observable | *a*, *b* | *p* |
|---|---|---|
| ⟨*r*⟩ | 1, 0 | 2 |
| σ_geo, C₃, quadrupole, diamagnetic | 2, 0 | 4 |
| polarisability α | 2, 1 | 7 |
| **C₆** | 4, 1 | **11** |
| C₈ | 6, 1 | 15 |

**Scope**: applies to observables built from ⟨*r*⟩ and Δ*E*. **Hyperfine is
excluded** — it scales as ν⁻³ via |ψ(0)|², which is neither.

**Every Rydberg property is ν to a power**, and rank(log **q**) = **1** across 15
quantities × 40 values of ν — singular values 9.49×10¹ then 1.8×10⁻¹⁴.
**One dimension, fifteen perspectives.**

**Collective coefficients are not a separate class.** C₆ = ν¹¹ *is* (ν²)⁴/ν⁻³ —
four single-atom dipole factors over one single-atom denominator. **The
collective value is assembled from the constituent's ν and nothing else.**

**But error amplifies as *k*.** 1% in ν gives 3% in lifetimes and **11% in C₆**.
Inverted: measuring C₆ to 1% fixes ν to **0.09%** — nine times sharper than
three levels. **The collective quantity is the most sensitive probe of
dimension 1.**

**Terminology**: use the field's names for the objects — *superatom*,
*macrodimer*, *ultralong-range Rydberg molecule* — and **collective section**
for the operation. A superatom's blockade radius is the *p* = 11/6 collective
section of the cell its constituents occupy.

---

## PART I — THE SECOND ADMISSION BOUND

> **ν_V = (3*Z*²*R* / 5*q*)^¼** — the *V*-resolution ceiling

*w* ≈ 4*Z*²*R*/ν³ and *V* = 4ν/3, so *e* = 3*Z*²*R*/ν⁴. Requiring *e* ≥ 5*q*
for quotation granularity *q* gives the ceiling.

**Distinct from *r*.** The bracket needs levels *separated* (ν⁻³, governed by
*r*); the cost needs curvature *resolved* (ν⁻⁴, governed by ν_V). **Curvature
washes out first, in every channel in this work.**

| channel | *q* | ν_V | ν_r | ν reached |
|---|---|---|---|---|
| K I *n*d | 0.0001 | 160 | 397 | 45.7 |
| Na I *n*s | 0.001 | 90 | 280 | 20.0 |
| **Al I *n*f** | **0.01** | **50.7** | 95.8 | **55.0** |

**Al I *n*f is the first channel to reach its own ceiling.** Predicted 50.7; the
four failing cells are *n* = 48, 51, 53, 54. **Per-cell, not a range cutoff** —
49, 50 and 52 pass. The bracket is unaffected in all 94 cells: containment needs
only monotonicity, which rounding preserves.

---

## PART J — THE PRINCIPLES, FORMALISED

Ten of seventeen have exact form. **Three were corrected by the act of
formalising them.**

| | principle | expression |
|---|---|---|
| 1 | self-referencing | 𝓡(Λ) = Λ |
| 2 | self-defending | 𝒟 = dim q − rank ∂Φ/∂p ≥ 1 |
| 3 | work backwards | invert Φ; separate the fibre |
| 7 | all questions close | ∃N : Ω_N = ∅ — **terminal, not monotone** |
| 8 | every answer is a bound | A_n ⊆ A_{n−1} — a filtration |
| 9 | dim 1 and perspectives | **rank(log q) = 1** |
| 10 | allow expansions | §9.4-form constraints preserve closure |
| 12 | test every cell | ρ = 0 certain ⟺ n = \|Λ\| (no sampling proof) |
| 13 | coherence | COHERENT ⟺ Ω = ∅ |
| 17 | path through the bounds | cost ratio 1/N per bound followed |

**Principle 7 was corrected.** |Ω| this session went 5 → 4 → 3 → 4 → 3 → 7 → 3
→ 3. **Not monotone.** Closure requires a well-founded measure, not a shrinking
count — which is why the principle correctly says *a claim cannot be made while*
Ω ≠ ∅.

**Seven remain procedural** — audit, compute before assuming, reframe, close
gaps, structural solutions, fetching, bounds as coordinates. They govern how an
agent uses an index, not what an index is. **They have no expressions, and
saying so is better than manufacturing one.**

---

## PART K — ANTIMATTER AND EXOTIC ATOMS

**Λ is CPT-invariant.** Every coordinate is CPT-even — all counts and
magnitudes. **Charge never appears as an axis**: *q* counts particles removed,
the same integer for electrons and positrons. So Λ(antimatter) = Λ(matter) cell
for cell, **no map required**. ALPHA measures antihydrogen 1S–2S agreeing with
hydrogen at 2 × 10⁻¹².

**"Reciprocal lattice" is a false friend** — that is the Fourier dual of a
*translation* lattice. Λ is an *order* lattice. **The two senses are unrelated.**
The order dual Λᵒᵖ exists and is the **descending side of the cylinder**.

**The real second axis is reduced mass**, not charge:

| system | μ/*m*ₑ | radius / Å |
|---|---|---|
| positronium | 0.50 | 1.058 |
| hydrogen, antihydrogen | 1.00 | 0.529 |
| muonic hydrogen | 186 | 0.0028 |
| antiprotonic helium | 1,467 | 0.00036 |

**A factor of 2,900 in size, running exactly opposite to energy**: *E* ∝ μ,
*a* ∝ 1/μ, so *E*·*a* is constant. **ν and *V* are invariant** under the whole
rescaling — pure numbers. The object is a cylinder over ν **times** a cylinder
over μ; a product of orientable cylinders is orientable.

**The bracket cannot help antihydrogen.** It is 1.8 × 10¹² times wider than
ALPHA's existing comparison, and *V* = 32/11 there is already the floor. **δ = 0
exactly, so there is nothing to bound.** Antihydrogen is pure hydrogenic limit;
δ is pure correction. **Antiprotonic helium is the only antimatter system with
a real defect and a real series** — untested.

---

## PART L — OPEN

**Research problems.** Reorderability at *d* ≥ 3 *without* a tree — solved for
trees, no reduction otherwise. Complexity class of reorderability — brute force
∏\|Aᵢ\|!, tree case Σ\|Aᵢ\|!, general case unestablished.

**Empirical.** Four documents bounding the *V* = 4ν/3 novelty claim at ~75%:
**Edlén, *Handbuch der Physik* XXVII (1964)**; **Ritz, *Physikalische
Zeitschrift* 9, 521 (1908)**, reprinted in *Œuvres* (1911) pp. ~142–150;
**Paschen & Götze, *Seriengesetze der Linienspektren* (Springer, 1922)**;
**Dunz, *Seriengesetze der Linienspektra* (Leipzig, 1911)**. Ritz's ApJ version
read in full — **no bound of any kind**, though it contains the qualitative
ancestor: *differences and sums of observed wave-numbers are naturally more
accurate*. Martin 1980 checked — a **flat ±0.03 cm⁻¹**, not ν-dependent.

**Collection.** 29 of 33 candidate spectra, all with identified compilations —
including the four gap-fillers **Sugar & Corliss 1985 (JPCRD 14 Suppl. 2, Ni I)**,
**Sugar & Musgrove 1990 (JPCRD 19, 527, Cu I/II)**, **Sugar & Musgrove 1995
(JPCRD 24, 1803, Zn I/II)**, cited from documents already read. Li I needs the
full ASD — the Handbook runs only to *n* = 4.

**The collection is bounded, not open.** The census fixes the candidate set at
**33 spectra**; each has an identified compilation; the compilations name one
another. **Completion is a finite traversal.**

---

## PART M — THE RECORD

**Thirty-two corrections this session**, of which the most instructive:

- **The *Z* error** — Al II and K II computed with *Z*_eff = 1. The bracket held
  56/56 and could not notice, because *Z* cancels from containment. δ and *V*
  both flagged it. **𝒟_phys working.**
- **"*w* = 3ν·*e*"** — written down wrongly, with the two disagreeing numbers
  printed on the same line. **The check caught the check. 𝒟 ≥ 1 does not require
  the auditor to be right.**
- **The cap = 4 discard** — a guard returned `None`, coerced to `False`, which
  produced "3 of 85", which produced "almost never reorderable", which produced
  a false dismissal of the *d* = 3 evidence. **One silent discard propagated
  through three conclusions**, none of which looked wrong. This required D3 and
  D3 was not yet stated.
- **"K I is integrated"** — claimed 516 cells and never wrote them. Found by
  auditing the built PDF, not the source.
- **A curve fit through non-monotone data** — extrapolated the void-free
  fraction to zero from a series that goes down then up.

**The dominant pattern**: prose asserting a conclusion while the output
contradicting it sits on the same screen. **The instrument corrected its own
specification three times in twenty minutes** — which is the strongest evidence
in the session that 𝒟 ≥ 1 must live in the object, not in the person.

---

*Compiled at the close of session. Nothing here is in the paper.*
