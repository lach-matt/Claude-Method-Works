# Queyranne & Tardella (2008) — *Sublattices of product spaces: Hulls, representations and counting*

> **THIRD-PARTY COPYRIGHTED WORK. NOT OURS, NOT PART OF THE CORPUS, NOT A GENERATED TREE.**
>
> Maurice Queyranne and Fabio Tardella, "Sublattices of product spaces: Hulls, representations and
> counting", *Discrete Mathematics* **308**(9) (2008), 1508–1523.
> DOI 10.1016/j.disc.2007.04.007 · PII S0012365X07002117
>
> **Status: PARTIAL RECONSTRUCTION FROM SCREENSHOT OCR.** Reconstructed 2026-09-12 from 50 phone
> screenshots supplied by the repository owner, read through the Google Drive connector's OCR. The
> publisher's site is unreachable from this environment (egress policy 403; Elsevier
> `tdm-reservation` set), so no authoritative text was available.
>
> **Coverage: Sections 1, 2, 3 and the first part of Section 4 (through Lemma 21).** Sections 4
> (remainder), 5 (corner representation) and 6 (membership algorithm) are **NOT transcribed** — they
> concern counting bounds, encoding and algorithms, none of which bear on the question this repository
> needed the paper for. Ask if they are wanted.
>
> **Fidelity warning.** The OCR reliably recovers prose and reliably mangles mathematical notation.
> Symbols have been restored by hand from context and are a *reading*, not a transcription. Two
> displayed formulas are marked `[form uncertain]` where the OCR was unrecoverable. **Do not quote a
> formula from this file in anything published — check it against the paper.** Prose is close to
> verbatim; every theorem number, hypothesis and inclusion direction was cross-read against the
> screenshots.
>
> **Why it is here.** It is the provenance for `decomposable.py`'s theorem T1. See `docs/`, and
> `paper/CLAIMS.md` H110/H111.

---

## 1. Introduction

Lattices and sublattices are fundamental algebraic structures with applications ranging from
Economics [12], [17] to Optimization [7], [8], Graph Theory [6], Engineering [13], [14] and other
fields (see, e.g., [3], [4], [5]). Recall that a lattice is a partially ordered set L such that each
pair of elements u, v ∈ L has a greatest lower bound, or meet, u ∧ v ∈ L and a smallest upper bound,
or join, u ∨ v ∈ L. A sublattice S of a lattice L is a subset of L closed for the join and meet
operations of L.

For many applications, it is often important to be able to represent a (sub)lattice in a
computationally or algebraically convenient way. It is also useful to be able to recognize if a given
subset Q of a lattice is a sublattice and, if not, to construct its sublattice hull LQ, that is, the
smallest sublattice containing Q.

Topkis and Veinott [16], [17], [18] present several results concerning the representation and
recognition of sublattices of product spaces, i.e., Cartesian products of lattices with componentwise
meet and join operations. Typical examples of product spaces include the Euclidean vector space Rⁿ,
the integer lattice Zⁿ, the Boolean lattice Bⁿ = {0,1}ⁿ and, more generally, any function space Y^X
where Y is a lattice.

The importance of product spaces was demonstrated, among others, by Birkhoff [1], [2] who shows that
any finite distributive lattice is isomorphic to a sublattice of some Boolean lattice Bⁿ.

Topkis proves that every sublattice L of a finite product of lattices can be represented as the
intersection of the "cylinders" based on all the two-dimensional projections of L onto coordinate
planes. Veinott extends this result to a class of infinite-dimensional product spaces. In Section 2
we present a similar and more general representation by projections for sublattice hulls and for a
broader class of product spaces.

Topkis also proves that every sublattice L of a finite product space can be represented as the set of
all points that are in the Cartesian product ∏ᵢ πᵢL of its projections on the coordinate axes, and
that satisfy a certain system of nonlinear inequalities involving at most two variables
(coordinates). In Section 3 we refine and extend this result by showing that the sublattice hull of
every subset in a broad class of product spaces is the intersection of the cylinders based on the
epigraphs of certain single-variable isotone (i.e., nondecreasing) functions, the boundary functions.
We use this representation with proper boundary epigraphs and show that the sublattice hull of a
convex (resp., polyhedral) subset is convex (resp., polyhedral).

In 1937 Birkhoff [1] posed the problem of determining the number of sublattices of the Boolean
lattice B^d. In Section 4, using the representation by proper boundary epigraphs, we determine upper
and lower bounds on the number of sublattices in a finite product of finite chains. (A chain is a
totally ordered set.) These bounds are close to (i.e., within a constant factor of) each other in a
logarithmic sense.

In Section 5 we present a corner representation of isotone functions and of their epigraphs when the
space is a finite product of finite chains. This corner representation of the boundary epigraphs
provides us with a way of encoding an arbitrary sublattice of a given product space. Using the base-2
logarithm of the number of sublattices, we show that this sublattice encoding is optimal (up to a
constant factor) in terms of memory space required.

In Section 6 we consider the sublattice hull membership problem of deciding whether a given point is
in the sublattice hull of a given subset of a product space. When the space is a finite product of
finite chains, we present a good characterization and a polynomial-time algorithm for this sublattice
hull membership problem. We also show how to construct in polynomial time a data structure
implementing the representation of Section 3 for the sublattice hull of a given subset. This data
structure then allows us to answer sublattice hull membership queries in time logarithmic in the
subset size.

## 2. Representation of sublattice hulls by projections

Let I be an arbitrary index set. For all i ∈ I, let Tᵢ be a lattice with join and meet operations
denoted by ∨ and ∧, respectively, and with associated partial order ≤ (defined by u ≤ v iff
u ∧ v = u). The Cartesian product, or product space, T_I = ∏_{i∈I} Tᵢ is the set of all vectors (or
points) x = (xᵢ)_{i∈I} with components xᵢ ∈ Tᵢ for all i ∈ I. The product space T_I is a lattice with
respect to the operations ∨ and ∧ defined componentwise, i.e., x ∨ y = (xᵢ ∨ yᵢ)_{i∈I} and
x ∧ y = (xᵢ ∧ yᵢ)_{i∈I} for any x, y ∈ T_I. Its associated partial order is then defined by x ≤ y iff
xᵢ ≤ yᵢ for all i ∈ I. A subset L of T_I is called a sublattice of T_I if x ∧ y ∈ L and x ∨ y ∈ L for
all x, y ∈ L. The intersection of any family of sublattices of L is a sublattice of L. If Q is an
arbitrary subset of T_I, we let LQ denote the sublattice hull of Q, that is, the intersection of all
sublattices of T_I that contain Q; thus LQ is the smallest sublattice of L containing Q. In this
section, we review results of Topkis and Veinott on the representation of sublattices of a product
space, and extend these results, in particular to the representation of the sublattice hull of a
given subset in terms of one- and two-dimensional projections.

Given a subset J ⊆ I and x ∈ T_I, let x_J denote (xⱼ)_{j∈J}, so x_J ∈ T_J. The projection of a subset
Q ⊆ T_I onto the subspace T_J is π_J Q = {x_J : x ∈ Q}. We use the simpler notations πᵢ and π_{ij} for
π_{{i}} and π_{{i,j}}, respectively. Conversely, given J ⊆ I and R ⊆ T_J, the cylinder Cyl_J R
generated by R in T_I is Cyl_J R = {x ∈ T_I : x_J ∈ R}.

**Proposition 1 (Projections and sublattice hulls commute).**
If J ⊆ I and T_I = ∏_{i∈I} Tᵢ is a product lattice, then π_J LQ = L π_J Q for every subset Q ⊆ T_I.

*Proof.* The inclusion π_J LQ ⊇ L π_J Q follows from Q ⊆ LQ, which implies π_J LQ ⊇ π_J Q, and from
the fact that the projection π_J L of a sublattice L ⊆ T_I is a sublattice of T_J. For the converse
inclusion, note that Q ⊆ Cyl_J L π_J Q. Since the latter cylinder is a sublattice of T_I and the
lattice hull operator L preserves inclusion, we have LQ ⊆ Cyl_J L π_J Q. Then
π_J LQ ⊆ π_J Cyl_J L π_J Q = L π_J Q. ∎

Topkis proved [16, Theorem 1] that every sublattice L of a finite product T_I of lattices can be
represented as the intersection of the cylinders Cyl_{ij} π_{ij} L for all i, j ∈ I with i ≠ j.
Veinott proved this result for certain sublattices of an arbitrary product of chains [18, Corollary
11; see also footnotes 12 and 13, p. 694 therein]. The following example shows that this result does
not hold for a general sublattice of an arbitrary (not necessarily finite) product of chains or
lattices.

**Example 2.** Let I be any infinite set and, for all i ∈ I, let Tᵢ be the two-element chain
B = {0, 1}. Viewing each element x ∈ T_I as the characteristic vector of the subset
S(x) = {i ∈ I : xᵢ = 1}, we thus define a lattice isomorphism S from T_I to the powerset 2^I of I,
mapping the join and meet operations in T_I to the union and intersection in 2^I. Let L¹ be the set
of all characteristic vectors of finite subsets of I. By the above isomorphism, L¹ is a sublattice of
T_I, and, since I is infinite, L¹ ≠ T_I. For every i, j ∈ I (with i ≠ j), we have {i,j} ∈ S(L¹) and
thus π_{ij} L¹ = Tᵢ × Tⱼ. Therefore, Cyl_{ij} π_{ij} L¹ = T_I and
⋂_{i,j∈I, i≠j} Cyl_{ij} π_{ij} L¹ = T_I ≠ L¹.

We now extend the results of Topkis and Veinott to the sublattice hull LQ of a subset Q of an
arbitrary product lattice. As suggested by the preceding example, we need to impose some conditions
on the index set I or on Q. For this, we recall the following definitions. An element l in a poset M
is a lower bound of a subset K ⊆ M if l ≤ k for all k ∈ K. A meet semilattice M is meet complete if
every nonempty subset K ⊆ M has a greatest lower bound (meet) ⋀K in M. A subset S of a meet
semilattice M is a meet subsemilattice of M if it is closed for the meet operation between pairs of
elements in M.

A subset S of a meet semilattice M is meet subcomplete if every nonempty subset K of S has a meet in
M and this meet is also in S; it is conditionally meet subcomplete if the preceding requirement only
applies to subsets K that have a lower bound in M; it is (conditionally) κ-meet subcomplete if the
corresponding requirement only applies to subsets K of M with cardinality ≤ κ. The join counterparts
of all these notions are defined dually. We use the adjective "countably" to refer to the case where
κ is the countable cardinal ℵ₀. Note that, by a standard argument, a sublattice L is conditionally
countably meet (resp. join) subcomplete iff the preceding condition is in fact restricted to
countable decreasing (resp. increasing) chains K in L. Let |I| denote the cardinal of I.

**Theorem 3 (Sublattice hull representation by projections).**
Let Q be a subset of a product T_I of lattices. Then the sublattice hull LQ is contained in the
intersection of all cylinders generated by the sublattice hulls of the two-dimensional projections of
Q, that is,

    LQ ⊆ ⋂_{i,j∈I, i≠j} Cyl_{ij} L π_{ij} Q.                                        (1)

Furthermore, if one of the following conditions holds:

  (i) I is finite;
  (ii) either (a) LQ is |I|-meet subcomplete and conditionally |I|-join subcomplete; or (b) the dual
       condition holds.

Then equality holds in (1), that is, LQ is determined by the sublattice hulls L π_{ij} Q of the
two-dimensional projections of Q:

    LQ = ⋂_{i,j∈I, i≠j} Cyl_{ij} L π_{ij} Q.                                         (2)

*Proof.* Let Q' denote the right-hand side of (1) and (2). By Proposition 1, Q' is the intersection
of the cylinders Cyl_{ij} π_{ij} LQ. Note that, for all subsets K ⊆ T_I and J ⊆ I, the inclusion
K ⊆ Cyl_J π_J K holds. Hence LQ ⊆ Q' and (1) is proved. We now show the converse inclusion under
condition (i) or (ii)-(a) of the theorem; the proof for the (b) counterpart of the latter condition
follows dually. Thus, we fix x ∈ Q' and show that x ∈ LQ. For all distinct i, j ∈ I,
(xᵢ, xⱼ) ∈ π_{ij} LQ, hence there exists y^{ij} ∈ LQ with y^{ij}ᵢ = xᵢ and y^{ij}ⱼ = xⱼ. Letting
K^i = {y^{ij} : j ∈ I, j ≠ i}, condition (i) or (ii)-(a) implies that the meet u^i = ⋀ K^i exists and
is in LQ. Furthermore, u^i_i = xᵢ and, for all j ∈ I \ {i}, u^i_j ≤ y^{ij}_j = xⱼ, so u^i ≤ x. But now
the set K = {u^i : i ∈ I} is bounded above by x in T_I, so conditions (i) or (ii) imply that the join
z = ⋁K exists and is in LQ. Furthermore, z ≤ x and, for all i ∈ I, zᵢ ≥ u^i_i = xᵢ. Therefore,
x = z ∈ LQ and the proof is complete. ∎

If, in Example 2, we let I be countable then the sublattice L¹ is meet subcomplete (the intersection
of any collection of finite sets being finite), but it is not conditionally countably join
subcomplete. Since L¹ violates (2), this example shows that the first condition in (ii)-(a) does not
suffice when I is countable. Similarly, if we let I in Example 2 be any uncountable set and L² be the
sublattice of all countable subsets of I, then we see that the first condition in (ii)-(a) does not
suffice either when I is not countable. Dually, letting L³ (resp., L⁴) denote the sublattice of
cofinite (resp., cocountable) subsets of I, i.e., subsets K ⊆ I whose complement I \ K is finite
(resp., countable), shows that the former (resp., latter) remark also applies to condition (ii)-(b).

## 3. Representation of sublattice hulls with proper boundary epigraphs

We now present a new characterization of the two-dimensional sublattices L π_{ij} Q using the
epigraphs of certain isotone functions. For this, we need further definitions. A (sub)lattice is
(sub)complete if it is both meet and join (sub)complete. Every lattice L can be embedded into a
complete lattice L̄ containing L, e.g., by the Dedekind–MacNeille completion [2], [4]. Note that if a
lattice L has a largest element ⋁L (resp., a smallest element ⋀L), then the meet (resp., join) of its
empty subset is ⋀∅ = ⋁L (resp., ⋁∅ = ⋀L). Given Q ⊆ T_I, we define, for every i, j ∈ I with i ≠ j,
the boundary function δ^Q_{ij} : T̄ⱼ → T̄ᵢ by

    δ^Q_{ij}(h) = ⋁ { xᵢ : x ∈ Q, xⱼ ≤ h }                                            (3)

Note that the function δ^Q_{ij} is isotone and meet-based, i.e.,

    δ^Q_{ij}(⋀ πⱼQ) = ⋀ πᵢQ  [form uncertain in source]                              (4)

Let

    P^Q_{ij} = { h ∈ T̄ⱼ : ∃ x ∈ Q with xᵢ = δ^Q_{ij}(h) and xⱼ ≤ h }

denote the set of all h ∈ T̄ⱼ for which the boundary value δ^Q_{ij}(h) is attained in Q. The proper
boundary epigraph E^Q_{ij} is

    E^Q_{ij} = { (h, k) ∈ L πᵢQ × L πⱼQ : k ≥ δ^Q_{ij}(h) if h ∈ P^Q_{ij},
                                          and k > δ^Q_{ij}(h) otherwise }.            (5)

The need to distinguish the two cases in definition (5) is justified in the proof of the
two-dimensional sublattice hull representation Theorem 9.

Recall that, when A is a set and B is a poset, the epigraph Ef of a function f : A → B is
E f = {(h, k) ∈ A × B : k ≥ f(h)}.

**Lemma 4.** Let f be a function from a set A to a poset B:
 (i) If f is isotone and A and B are meet semilattices, then Ef is a meet subsemilattice of A × B.
 (ii) If f is isotone, A is a chain and B is a lattice, then Ef is a sublattice of A × B.
 (iii) If A and B are chains and Ef is a meet subsemilattice of A × B, then f is isotone.

*Proof.* (i) For every (h, k), (h', k') ∈ Ef we have f(h ∧ h') ≤ f(h) ∧ f(h') ≤ k ∧ k'. Hence
(h, k) ∧ (h', k') ∈ Ef. (ii) Furthermore, if A is a chain and B is a lattice, then
f(h ∨ h') = f(h) ∨ f(h') ≤ k ∨ k'. Hence (h, k) ∨ (h', k') ∈ Ef. (iii) Let h, h' ∈ A with h ≤ h'.
Since x = (h, f(h)) ∈ Ef, x' = (h', f(h')) ∈ Ef and Ef is a meet subsemilattice, we have
x ∧ x' = (h, f(h) ∧ f(h')) ∈ Ef, so that f(h) ∧ f(h') ≥ f(h), implying f(h) ≤ f(h'). ∎

The following example shows that when A is a lattice, B is a chain, and f : A → B is isotone, the
epigraph Ef need not be a join subsemilattice of A × B.

**Example 5.** Let lattice A = {0, a, b, 1} with a ∧ b = 0 and a ∨ b = 1, and chain B = {0, 1} with
0 < 1. Let f : A → B be defined by f(h) = 1 if h = 1 and 0 otherwise, so f is isotone. Then
(a, 0), (b, 0) ∈ Ef while (a, 0) ∨ (b, 0) = (1, 0) ∉ Ef.

**Remark 6.** If j ∈ I and πⱼQ is a meet subcomplete subset of Tⱼ, then for all i ∈ I, i ≠ j, we have
P^Q_{ij} = T̄ⱼ and

    E_{ij} Q = {(h, k) ∈ L πᵢQ × L πⱼQ : k ≥ δ^Q_{ij}(h)},                            (6)

that is, the proper boundary epigraph E_{ij}Q is the intersection of the epigraph of the boundary
function δ^Q_{ij} and of L πᵢQ × L πⱼQ. This is the case, e.g., when Q is a meet subcomplete subset
of T_I, or when each Tᵢ is a chain and Q is finite.

**Remark 7.** In the case where T_I = Rⁿ and Q is a polyhedron, the boundary function δ^Q_{ij} is the
value function of a Linear Program. Thus in this case, the boundary function is convex and piecewise
linear, and the proper boundary epigraph E_{ij}Q is a polyhedron.

**Lemma 8.** Let Q be a subset of a product T_I of lattices, and let πⱼQ be either a chain or a meet
subcomplete subset of Tⱼ. Then for all i ∈ I, i ≠ j, and for every point (h, k) ∈ E_{ij}Q:
 (i) there exists x ∈ Q such that xⱼ ≥ h and xᵢ ≤ k;
 (ii) if (h', k') ∈ L πᵢQ × L πⱼQ satisfies h' ≤ h and k' ≥ k, then (h', k') ∈ E_{ij}Q.

*Proof.* (i) If h ∈ P^Q_{ij} then, by definition of E_{ij}Q we have k ≥ δ^Q_{ij}(h) and, by definition
of P^Q_{ij}, there exists x ∈ Q such that xⱼ ≥ h and xᵢ = δ^Q_{ij}(h) ≤ k. If πⱼQ is meet subcomplete,
then P^Q_{ij} = T̄ⱼ by Remark 6, and (i) follows. The remaining case is where πⱼQ is a chain and
h ∉ P^Q_{ij}. In this case, if xᵢ > k for all x ∈ Q with xⱼ ≥ h then δ^Q_{ij}(h) ≥ k, contradicting
the assumption (h, k) ∈ E_{ij}Q since h ∉ P^Q_{ij}. Thus (i) must hold.
(ii) Since δ^Q_{ij} is isotone, we have δ^Q_{ij}(h') ≤ δ^Q_{ij}(h) ≤ k ≤ k'. If h ∉ P^Q_{ij} or
δ^Q_{ij}(h') < δ^Q_{ij}(h), then δ^Q_{ij}(h') < k' and thus (h', k') ∈ E_{ij}Q. Otherwise,
h ∈ P^Q_{ij} and δ^Q_{ij}(h') = δ^Q_{ij}(h). Then there exists x ∈ Q with xⱼ ≥ h ≥ h', and
xᵢ = δ^Q_{ij}(h) = δ^Q_{ij}(h'). Therefore, h' ∈ P^Q_{ij} and δ^Q_{ij}(h') ≤ k', and thus
(h', k') ∈ E_{ij}Q. ∎

Note that the assumption that πⱼQ is a chain is trivially satisfied when Tⱼ is a chain. Furthermore,
if Q is meet subcomplete then so is each πⱼQ.

With the proper boundary epigraph E_{ij}Q ⊆ Tⱼ × Tᵢ, we also consider its "transpose"
Ẽ_{ji}Q = {(h, k) : (k, h) ∈ E_{ji}Q} ⊆ Tᵢ × Tⱼ.

**Theorem 9 (Two-dimensional sublattice hull representation).**
Let Q be a subset of a product T_I of lattices, let i, j ∈ I with i ≠ j, and assume that πᵢQ, as well
as πⱼQ, is either a chain or meet subcomplete. Then, we have

    L π_{ij} Q ⊆ E_{ij}Q ∩ Ẽ_{ji}Q.                                                   (7)

Furthermore, if one of the following conditions hold:

  (i) π_{ij}Q is a sublattice of Tᵢ × Tⱼ;
  (ii) Tᵢ and Tⱼ are chains;

then equality holds in (7), that is,

    L π_{ij} Q = E_{ij}Q ∩ Ẽ_{ji}Q.                                                   (8)

*Proof.* We first prove inclusion (7). Let (h, k) ∈ L π_{ij}Q. Then h ∈ L πᵢQ = πᵢLQ by definition and
Proposition 1. Hence, there exists y ∈ LQ such that yᵢ = h. By Lemma 8(i), there exists x ∈ Q such
that xⱼ ≥ h and xᵢ ≤ k. This completes the proof of (7).

To prove the reverse inclusion, and hence equality (8), let (h, k) ∈ E_{ij}Q ∩ Ẽ_{ji}Q. Under
condition (i), L π_{ij}Q = π_{ij}Q and there exists y ∈ Q with yᵢ = h and yⱼ = k. Under condition
(ii), we prove the existence of an element y ∈ Q with yᵢ ≥ h and yⱼ ≤ δ^Q_{ij}(h), using the
assumption that (h, k) ∈ L π_{ij}Q = π_{ij}LQ. Therefore, under either condition (i) or (ii), there
exists y ∈ Q with yᵢ ≥ h and yⱼ = δ^Q_{ij}(h). If k > δ^Q_{ij}(h) then, by definition,
(h, k) ∈ E_{ij}Q. Otherwise, k = δ^Q_{ij}(h). Since yᵢ ≥ h and yⱼ ≤ k = δ^Q_{ij}(h) ≤ yⱼ, this implies
yⱼ = k and thus h ∈ P^Q_{ij} and (h, k) ∈ E_{ij}Q. A dual argument shows that (k, h) ∈ E_{ji}Q, i.e.,
(h, k) ∈ Ẽ_{ji}Q. This completes the proof. ∎

The following example shows that equality (8) may not hold if neither condition (i) nor (ii) of
Theorem 9 is satisfied. To simplify notations, in the following and in later examples we represent
any two-dimensional vector x = (u, v) as uv.

**Example 10.** Let I = {1, 2}, and lattices T₁ = T₂ = {0, a, b, c, 1} with a ∧ b = 0, a ∨ b = c and
c < 1. Let Q = {aa, bb, 11} ⊆ T₁ × T₂. Then the boundary function δ_{12} satisfies
δ_{12}(0) = ⋁∅ = 0, δ_{12}(a) = a, δ_{12}(b) = b, and δ_{12}(c) = δ_{12}(1) = 1. Since
P_{12}Q = {a, b, c, 1}, the proper boundary epigraph is

    E_{12}Q = {0a, 0b, 0c, 01, aa, ac, a1, bb, bc, b1, c1, 11}.

Note that E_{12}Q is not a sublattice since 00 = 0a ∧ 0b ∉ E_{12}Q. By symmetry,
E_{21}Q = Ẽ_{12}Q and E_{12}Q ∩ Ẽ_{21}Q = {aa, bb, 11} = Q ≠ LQ = L π_{12}Q.

We are now in the position to establish the main result of this section.

**Theorem 11 (Sublattice hull representation with proper boundary epigraphs).**
Let Q be a subset of a product T_I of lattices. If condition (i) or (ii) of Theorem 3 holds, then

    LQ ⊆ ⋂_{i,j∈I, i≠j} Cyl_{ij} E_{ij}Q.                                             (9)

Furthermore, if each πᵢQ is either a chain or meet subcomplete, and for every i, j ∈ I with i ≠ j
condition (i) or (ii) of Theorem 9 is satisfied, then equality holds in (9), that is,

    LQ = ⋂_{i,j∈I, i≠j} Cyl_{ij} E_{ij}Q.                                            (10)

*Proof.* The inclusion (9) follows from equality (2), inclusion (7), and the fact that
Cyl_{ij} Ẽ_{ji}Q = Cyl_{ji} E_{ji}Q. The equality in (10) then follows from (8) under the stated
conditions. ∎

We can use Theorem 11 to show that the convexity or polyhedrality structure is preserved by the
lattice hull operator.

**Corollary 12.** If T_I = Rⁿ and Q is a polyhedron, then LQ is a polyhedron.

*Proof.* Follows immediately from Theorem 11 and Remark 7. ∎

Recall that a vector lattice (or Riesz space) is a real vector space with a lattice ordering which is
preserved by translation and multiplication by positive scalars (see, e.g., [11]). When T_I is a
vector lattice we can apply Theorem 11 to prove that the lattice hull LQ of a convex set Q is convex.

**Theorem 13 (Convexity of the sublattice hull in a vector lattice).**
Assume that condition (i) or (ii) of Theorem 3 holds; T_I is a vector lattice; and Q is a convex
subset of T_I such that L πᵢQ is convex for all i ∈ I. Then LQ is convex.

*Proof.* By Theorem 11 we have LQ = ⋂_{i,j∈I, i≠j} Cyl_{ij} E_{ij}Q. Hence it is sufficient to prove
that the proper boundary epigraphs E_{ij}Q are convex whenever Q is convex. Indeed, let (h¹, k¹) and
(h², k²) belong to E_{ij}Q. Then, by Lemma 8(i), there exist two points x¹, x² ∈ Q such that
x¹ⱼ ≥ h¹, x²ⱼ ≥ h², x¹ᵢ ≤ k¹ and x²ᵢ ≤ k². By convexity of Q, for every α ∈ [0, 1] the point
x(α) = αx¹ + (1 − α)x² is in Q. Furthermore, we have αh¹ + (1 − α)h² ≤ xⱼ(α) and
αk¹ + (1 − α)k² ≥ xᵢ(α). Hence, from the convexity of L πᵢQ and L πⱼQ, and from the definition of
E_{ij}Q it follows that α(h¹, k¹) + (1 − α)(h², k²) ∈ E_{ij}Q. ∎

**Corollary 14.** Assume that each Tᵢ is a chain; condition (i) or (ii) of Theorem 3 holds; T_I is a
vector lattice; and Q is a convex subset of T_I. Then LQ is convex.

*Proof.* Follows from Theorem 13, the equalities L πᵢQ = πᵢQ and the convexity of πᵢQ. ∎

If Q is a sublattice of T_I, then condition (i) of Theorem 9 is satisfied and Eq. (10) holds under
condition (i) or (ii) of Theorem 3, thus providing a representation of sublattices of product spaces
with proper boundary epigraphs. This representation is related to those in Topkis [16] and Veinott
[18], as we now discuss. For i, j ∈ I, the i-decreasing j-increasing hull Q^{ij} of a set Q ⊆ T_I is
defined (see [18]) as

    Q^{ij} = {x ∈ T_I : ∃ y ∈ Q, xᵢ ≥ yᵢ and xⱼ ≤ yⱼ}   [form partly uncertain]      (11)

In the two-dimensional case I = {1, 2}, Topkis [16] calls the sets Q^{12} and Q^{21} the bimonotone
hulls of Q. For general I and all i, j ∈ I with i ≠ j, we have Q^{ij} = Cyl_{ij} π_{ij} Q^{ij}, that
is, Q^{ij} is a cylinder generated by a subset of Tᵢ × Tⱼ. Furthermore, for i ≠ j, the sets Q^{ij} are
related to the proper boundary epigraphs E_{ij}Q as follows.

(Note the order ji of the indices in the set in the right-hand side of Eq. (12).)

**Proposition 15.** Let Q be a subset of a product T_I of lattices, and let πⱼQ be either a chain or a
meet subcomplete subset of Tⱼ. Then for all i ∈ I, i ≠ j,

    Q^{ji} = Cyl_{ij} E_{ij}Q.                                                       (12)

*Proof.* Since the right-hand side of (12) is a cylinder generated by a subset of Tᵢ × Tⱼ, it suffices
to show that

    E_{ij}Q = π_{ij}(Q^{ji} ∩ Cyl_i L πᵢQ ∩ Cyl_j L πⱼQ)
            = π_{ij}Q^{ji} ∩ ((L πᵢQ) × (L πⱼQ)).                                    (13)

We first show that E_{ij}Q is included in the right-hand side of the last equality. By definition,
E_{ij}Q ⊆ L πᵢQ × L πⱼQ. Let (h, k) ∈ E_{ij}Q. By Lemma 8(i), there exists y ∈ Q such that yⱼ ≥ h and
yᵢ ≤ k. To show the reverse inclusion, let (h', k') ∈ π_{ij}Q^{ji} ∩ ((L πᵢQ) × (L πⱼQ)). By definition
of Q^{ji}, there exists y ∈ Q such that yᵢ ≤ k' and yⱼ ≥ h'. Since Q ⊆ E_{ij}Q, we have
(yᵢ, yⱼ) ∈ E_{ij}Q and, by (ii) of Lemma 8, (h', k') ∈ E_{ij}Q. ∎

If each πᵢQ is either a chain or meet subcomplete, and condition (i) of Theorem 9 is satisfied for all
i, j (i ≠ j), then ⋂_{i∈I} Cyl_i L πᵢQ = ⋂_{i∈I} Cyl_i πᵢQ. Eq. (10) is then equivalent to

    LQ = ⋂_{i,j∈I, i≠j} Q^{ij} ∩ ⋂_{i∈I} Cyl_i πᵢQ.                                  (14)

If Q is a sublattice of T_I, implying condition (i) of Theorem 9 for all i, j (i ≠ j); each πᵢQ is
either a chain or meet subcomplete; and I is finite; then (14) implies Theorems 2 and 3 of Topkis
[16]. On the other hand, since Q^{ij} = Cyl_{ij} π_{ij}Q^{ij}, if I is finite and every Tᵢ is a chain,
Eq. (10) becomes the representation of sublattices and sublattice hulls in Theorem 9 and Corollary 12
of Veinott [18].

**Remark 16.** Topkis [16] and Veinott [18] show that, under conditions (i) or (ii) of Theorem 9, the
subsets Q^{ij} are sublattices. By Eq. (13), this implies that the proper boundary epigraphs E_{ij}Q
are also sublattices when each πᵢQ is either a chain or meet subcomplete. Hence, the cylinders
Cyl_{ij} E_{ij}Q in representation (10) are also sublattices.

Another representation of sublattices in product lattices has been described by Topkis [16], [17] in
terms of level sets of functions. More precisely, Topkis has shown that, when I = {1, ..., d}, a
subset Q of a product lattice T_I is a sublattice of T_I if and only if it can be represented as the
intersection of the level sets of d univariate functions and of d(d−1)/2 bimonotone functions from
T_I into a chain C. Recall that a function f : T_I → C is called univariate if f(x) = fᵢ(xᵢ) for some
i ∈ I and fᵢ : Tᵢ → C. It is called bimonotone if f(x) = f_{ij}(xᵢ, xⱼ) for some
f_{ij} : Tᵢ × Tⱼ → C, with i, j ∈ I, i ≠ j and f_{ij}(xᵢ, xⱼ) isotone in xᵢ and antitone in xⱼ.

In view of Theorem 11, we can replace the level sets of bimonotone functions in Topkis's
representation with the epigraphs of meet-based isotone functions as follows.

**Proposition 17.** Let Tᵢ be a chain for every i ∈ I, and Q ⊆ T_I. Assume that each πᵢQ is meet
complete, and that condition (i) or (ii) of Theorem 3 holds. Then Q is a sublattice of T_I if and
only if there exist functions fᵢ : Tᵢ → {0, 1} for all i ∈ I, and meet-based isotone functions
f_{ij} : lev₀(fᵢ) → lev₀(fⱼ) for all i, j ∈ I with i ≠ j, such that

    Q = {x ∈ T_I : fᵢ(xᵢ) ≤ 0 ∀i ∈ I, and xⱼ ≥ f_{ij}(xᵢ) ∀i, j ∈ I, i ≠ j}.

*Proof.* The "if" part follows from the fact that Q is the intersection of the product, for all
i ∈ I, of the chains {x ∈ T_I : fᵢ(xᵢ) ≤ 0}, and of the cylinders based on the epigraphs E f_{ij} for
all i ≠ j ∈ I, which are sublattices by Lemma 4. For the "only if" part, define fᵢ by fᵢ(h) = 0 if
h ∈ πᵢQ, and 1 otherwise; and f_{ij} = δ^Q_{ij} for all i, j ∈ I with i ≠ j, and apply Theorem 11. ∎

In summary, the sublattice hull representation (10) with proper boundary epigraphs in Theorem 11
generalizes corresponding results in [16], [18], and is equivalent to them when their assumptions
apply. In addition, the present representation is computationally convenient, as will be seen in the
following sections.

## 4. Counting sublattices in product spaces

In this section, we assume that the index set I and each lattice Tᵢ is finite and, to simplify
notations, we let I = {1, ..., d}. Our purpose here is to provide upper and lower bounds on the number
of sublattices of T_I. More precisely we will use the sublattice hull representation Theorem 11 to
obtain an upper bound on the number of such sublattices in terms of the number of meet-based isotone
functions between each pair of lattices Tᵢ and Tⱼ. With the same tool we will also obtain a lower
bound on the number of sublattices in the case where each Tᵢ is a chain. We also show how to encode
concisely a sublattice Q by means of an encoding of the boundary functions and of Representation
Theorem 11.

For i, j in I (with i ≠ j) and sublattices Pᵢ ⊆ Tᵢ and Pⱼ ⊆ Tⱼ, consider the set S_{ij}(Pᵢ, Pⱼ) of all
sublattices Q of T_I with πᵢQ = Pᵢ and πⱼQ = Pⱼ. Let J(Pᵢ, Pⱼ) denote the set of all meet-based
isotone functions f from Pᵢ to Pⱼ. By Remark 6, the boundary epigraphs E_{ij}Q ⊆ (Pᵢ × Pⱼ) for all
Q ∈ S_{ij}(Pᵢ, Pⱼ). Hence, the number of distinct sets E_{ij}Q for all Q ∈ S_{ij}(Pᵢ, Pⱼ) is at most
|J(Pᵢ, Pⱼ)|.

Let S(L) denote the set of all sublattices of a given lattice L. Let
R(T_I) = {(P₁, ..., P_d) : Pᵢ ∈ S(Tᵢ) ∀i ∈ I}. For (P₁, ..., P_d) ∈ R(T_I), the product
∏_{i,j∈I, i≠j} |J(Pᵢ, Pⱼ)| is the number of tuples f = (f_{ij})_{i,j∈I, i≠j} of functions
f_{ij} ∈ J(Pᵢ, Pⱼ). By Eq. (10) and the remark above, this number is an upper bound on the number of
sublattices Q ∈ S(T_I) with projections πᵢQ = Pᵢ for all i ∈ I. Therefore, we obtain the following
upper bound on the number of sublattices of a product space T_I:

    |S(T_I)| ≤ U(T_I),  where U(T_I) = Σ_{(P₁,...,P_d)∈R(T_I)} ∏_{i,j∈I, i≠j} |J(Pᵢ, Pⱼ)|.   (15)

Note that this upper bound U(T_I) may exceed |S(T_I)| for at least two reasons: (i) distinct tuples f
may give rise to the same intersection ⋂_{i,j∈I, i≠j} Cyl_{ij} E f_{ij}, as shown in Example 18;
(ii) the epigraph of a meet-based isotone function f_{ij} ∈ J(Pᵢ, Pⱼ) may fail to be a sublattice, as
shown in Example 5.

However, when all Tᵢ's are chains, Lemma 4 shows that the latter difficulty does not arise. For the
rest of this section we therefore assume that all Tᵢ's are chains.

**Example 18.** Let I = {1, 2, 3} and Tᵢ = {0, 1} for all i ∈ I. Consider the sublattice
Q = {000, 111}. Then all πᵢQ = {0, 1} and all π_{ij}Q = {00, 11}. Thus δ_{ij}(h) = h for all h ∈ Tᵢ.
However, we can also obtain Q = ⋂_{i,j∈I, i≠j} Cyl_{ij} E f_{ij} with a different tuple f. For
example, we can let f₁₃ = f₃₁ = 0 and f_{ij} = δ_{ij} for all other i, j. Indeed, letting
Q' = ⋂_{i,j∈I, i≠j} Cyl_{ij} E f_{ij}, we have Q ⊆ Q'. To show the converse inclusion, let x ∈ Q'.
Then x ∈ Cyl E f₁₂ implies x₂ ≥ x₁, whereas x ∈ Cyl E f₂₁ implies x₁ ≥ x₂, and therefore x₁ = x₂.
Similarly we have x₂ = x₃, and thus x ∈ Q. This shows that Q = Q'.

Assume C₁ and C₂ are two finite chains with c₁ = |C₁| and c₂ = |C₂|. Noting that |J(C₁, C₂)| is equal
to the number of nondecreasing sequences of c₁ − 1 integers taken from {1, ..., c₂}, we have

    |J(C₁, C₂)| = C(c₁ + c₂ − 2, c₁ − 1).                                            (16)

Let p = (p₁, ..., p_d) and t = (t₁, ..., t_d), where tᵢ = |Tᵢ| for all i. Combining Eqs. (15) and (16)
we obtain

    U(T_I) = Σ_p ∏_{i≠j} C(pᵢ + pⱼ − 2, pᵢ − 1) · ∏ᵢ C(tᵢ, pᵢ).   [form partly uncertain]  (17)

We now present a lower bound on the number of sublattices of a finite product T_I of finite chains. In
order to obtain this bound we will use the following results that allow us to generate distinct
sublattices.

**Lemma 19.** Let T_I be a product of chains. For all i ∈ I let Pᵢ be a subchain of Tᵢ. Let J, K form a
partition of the index set I. For all j ∈ J and k ∈ K, let f_{jk} ∈ J(Pⱼ, P_k). Let
Q = ⋂_{(j,k)∈J×K} Cyl E f_{jk}. Then Q ∈ S(T_I) and π_{jk}Q = E f_{jk} for all j ∈ J, k ∈ K.

*Proof.* By Lemma 4, the epigraph E f_{jk} is a sublattice of Pⱼ × P_k. Therefore, Q is a sublattice of
T_I. Since Q ⊆ Cyl E f_{jk}, then trivially π_{jk}Q ⊆ E f_{jk}. To prove the converse inclusion,
consider any point (xⱼ, x_k) ∈ E f_{jk}. For all u ∈ J \ {j} define x_u = ⋀ P_u and for all
v ∈ K \ {k} define x_v = ⋁ P_v. We now show that the point x = (xᵢ)_{i∈I} thus defined is in
Cyl E f_{uv} for all u ∈ J and v ∈ K. This is trivial if u = j and v = k. If u ∈ J \ {j} and v ∈ K
then, since f_{uk} ∈ J(P_u, P_k), we have f_{uk}(x_u) = f_{uk}(⋀P_u) = ⋀P_k and thus
(x_u, x_k) ∈ E f_{uk}. For u = j and v ∈ K \ {k}, then f_{jv}(xⱼ) ≤ ⋁P_v = x_v, and thus
(xⱼ, x_v) ∈ E f_{jv}. It follows that x ∈ Q and the proof is complete. ∎

**Corollary 20.** Let T_I be a product of chains. For all i ∈ I let Pᵢ be a subchain of Tᵢ. Let J, K
form a partition of the index set I. Assume that Q = ⋂_{(j,k)∈J×K} Cyl E f_{jk} and
R = ⋂_{(j,k)∈J×K} Cyl E g_{jk} where f_{jk} and g_{jk} ∈ J(Pⱼ, P_k) for all j ∈ J and k ∈ K. Then
Q = R if and only if f_{jk} = g_{jk} for all j ∈ J and k ∈ K.

*Proof.* The if part is trivial. The only if part follows from Lemma 19 by noting that
f_{jk} = g_{jk} iff E f_{jk} = E g_{jk}. ∎

With every P = (P₁, ..., P_d) ∈ R(T_I) we associate a nontrivial subset J(P) of the index set I (that
is, ∅ ⊂ J(P) ⊂ I), that with its complement K(P) = I \ J(P) forms a partition of I. By Corollary 20,
for any tuple 𝒥 = (J(P))_{P∈R(T_I)} we obtain the following lower bound on the number of sublattices
of T_I:

    |S(T_I)| ≥ L_𝒥(T_I),  where L_𝒥(T_I) = Σ_{P∈R(T_I)} ∏_{j∈J(P), k∈K(P)} |J(Pⱼ, P_k)|.   (18)

We now construct a tuple 𝒥 such that log L_𝒥(T_I) ≥ ¼ log U(T_I), where "log" denotes the base-2
logarithm. Fix P = (P₁, ..., P_d) ∈ R(T_I). To simplify the notation, assume (w.l.o.g.) that
|P₁| ≥ |P₂| ≥ ... ≥ |P_d|.

**Lemma 21.** Let P = (P₁, ..., P_d) ∈ R(T_I) with |P₁| ≥ |P₂| ≥ ... ≥ |P_d|. Let J(P) be the set of
all odd integers in I = {1, ..., d} and K(P) = I \ J(P). Then

    log ∏_{j∈J(P), k∈K(P)} |J(Pⱼ, P_k)| ≥ ¼ log ∏_{u,v∈I, u≠v} |J(P_u, P_v)|.        (19)


---

*(Transcription ends at Lemma 21, page ~1517 of the printed article. Sections 4 (remainder), 5 and 6
are not transcribed — see the header.)*
