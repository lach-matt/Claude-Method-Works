# The Occupation Law as a Lower Convex Hull

**The rule that the entering electron takes the subshell of least ν = n − a·√r is the minimisation of the linear functional y − a·x over a finite point set {(√r, n)}; only a vertex of that set's lower convex hull can be chosen, the slopes that choose a given vertex are exactly the open interval between its two flanking hull-edge slopes, and along the 106 observed ground-configuration steps from lithium to hassium the observed entrant is such a vertex at every step, with no lower bound on its slope exactly when it carries no radial node.**

**Matthew Lach** · Independent Researcher · 24 September 2026

---

## Abstract

An occupation law for the periodic table assigns to each admissible subshell (n, ℓ) with occupancy q the number ν = n − a·√r, r = n − ℓ − 1 + q/(2(2ℓ+1)), and says that the electron entering at atomic number Z takes the subshell of least ν. This paper reads the law as geometry. Each admissible subshell is the point (√r, n) of a plane, ν is the value of y − a·x there, and the law selects the point a line of slope a reaches first when raised from below. Three consequences are proved. Only a vertex of the lower convex hull of the point set can be selected for any slope, and every vertex is selected for some slope (Theorem 1). The set of slopes selecting a given vertex is exactly the open interval between the slopes of the two hull edges that meet there, so the corridors of the vertices partition the slope axis (Theorem 2). And the corridor of the entrant is the same whatever finite frame of subshells is admitted, provided the frame reaches n = 15 (Theorem 3). Read against the tabulated ground configurations of the 108 neutral atoms (NIST Atomic Spectra Database), the entrant is a hull vertex at every one of the 106 steps from Z = 3 to Z = 108, in both the node-only and the finished form of the radicand; the 106 node-only corridors have nineteen distinct endpoints, each an element of ℚ(√2, √3, √5, √6, √7); the corridor has no lower bound exactly when the entering subshell is node-free, n − ℓ − 1 = 0 (Theorem 4), which is 26 steps of the 106, and at the two f openings the two cases are realised — cerium, where 4f opens with no floor, and protactinium, where 5f opens with p = 1, floor 0 and ceiling (1 + √3)/2. A slope carried from step to step and moved only when its corridor forces it is recalibrated 18 times, at nine of which it moves and at eight of which it merely touches an endpoint it already sits on; every subshell fills at constant slope except 5d, moved once at cerium, and 6d, moved at protactinium and at lawrencium. Three slopes suffice for all 106 corridors and three are necessary, since the corridors of boron, lanthanum and lawrencium are pairwise disjoint; the best single slope covers 86 of 106. Every identity is decided in exact arithmetic on sums of square roots, the hull theorem is discharged by an SMT solver for up to five points, and the law is placed: it orders subshells and constrains nothing but membership of an interval — it does not value.

---

## §0 · The result

**The occupation law is a lower convex hull, and that is both what it can do and what it cannot.**

The law has one free number, a, and a fixed geometric content. Write each admissible subshell as the point (x, y) = (√r, n). Then ν = y − a·x, and "least ν" means the first point met by a line of slope a rising from below. That picture is exact, and it settles three questions at once.

*Which subshells can the law ever select?* Only vertices of the lower convex hull of the point set, and each of those for some slope (Theorem 1, PROVED and MACHINE-CHECKED). A point set with two distinct abscissae has at least two such vertices (Corollary 1), so at no step does the form alone determine the entrant: the observed subshell is one admissible answer among at least two, and which one is a matter of the slope.

*Which slopes select a given subshell?* Exactly the open interval between the slopes of the two hull edges flanking it — its left neighbour on the hull supplies the floor, its right neighbour the ceiling, and where there is no neighbour there is no bound (Theorem 2, PROVED). The corridors of the hull vertices, taken in order of abscissa, are consecutive open intervals sharing their endpoints, and together with those endpoints they partition the whole slope axis. So the corridor that the ordering data impose on a is not a fitted quantity: it is a pair of edge slopes, each a number of the form Δn(√r₁ + √r₂)/(r₂ − r₁) with r₁, r₂ node counts, and there are nineteen of them across the table.

*Does the observed order fit this form at all?* At every one of the 106 steps from lithium to hassium the observed entrant is a hull vertex, in both forms of the radicand (EXHAUSTIVE). That is the content of "the corridor is non-empty at 106 of 106". It is a statement about the form and it survives every other demotion the law suffers below.

**The floor.** The corridor has no lower bound exactly when the entering subshell is node-free, n − ℓ − 1 = 0 (Theorem 4). The reason is that a node-free subshell sits on the axis x = 0, so nothing lies to its left; and conversely, because 5g — node-free, capacity 18, occupied in no tabulated ground configuration — is admissible at every step, every subshell with a node has 5g to its left and so has a floor. Across the walk the node-free entrants are 2p, 3d and 4f at 26 steps; every other corridor is two-sided. At cerium 4f opens with p = 0 and no floor; at protactinium 5f opens with p = 1, the floor is 0, supplied by 5g, the ceiling is (1 + √3)/2, and the carried slope arrives above the ceiling and is placed at it, so the corridor fraction t = (a − L)/(U − L) is 1 there and undefined at cerium. If g subshells are excluded from the candidate set the equivalence fails at exactly the eleven 5f steps 91–95 and 97–102, where the floor disappears; the paper's convention admits g and says so.

**The walk.** Carrying a from step to step and moving it only when it leaves its corridor — to the nearer endpoint, a distance ε = 10⁻⁶ inside — recalibrates it 18 times (§6). Nine of those are moves: potassium, rubidium, caesium, cerium, mercury, thallium, francium, protactinium, lawrencium. Eight are touches, where the carried value already sits at an endpoint of the new corridor and is nudged 2ε across it: molybdenum, technetium, rhodium, gadolinium, terbium, curium, berkelium, rutherfordium. Eight of the nine moves are at the opening of the entering subshell; mercury is the exception. Every subshell fills at constant a except two: 5d, moved once while open, at cerium, and 6d, moved at protactinium and at lawrencium — both d subshells that straddle an f opening. These sites do not depend on ε between 10⁻⁴ and 10⁻¹⁰.

**One slope for many steps.** No single slope serves the table. The running intersection of the corridors empties fourteen times in the node-only form and eleven in the finished form. The corridors of boron, lanthanum and lawrencium are pairwise disjoint, so at least three slopes are needed, and three explicit rational slopes pierce all 106, so three suffice (Theorem 5). The best single slope covers 86 of the 106 corridors, on the band (√3/3, √2/2); in the finished form 90, on (1, (5√2 + √5)/9).

**What is not claimed.** The law is not derived from the Schrödinger equation, and nothing here bears on that derivation: the point set is built from node counts and Pauli capacities, and the observed order enters only through the choice of the slope. A non-empty corridor does not confirm the form; an empty one would refute it, and none is empty. The carried slope, placed as above, reproduces the observed entrant at 88 of the 105 steps it is asked to predict before seeing them, against 96 of 106 for the memoryless rule that takes the least (n + ℓ, n) with no parameter at all; the law is not offered as a predictor. The candidate set includes g subshells, a convention that no observation below Z = 109 can test, and the measurable consequence of the alternative is stated. The walk's placement rule is one rule among several that respect the corridors, and the count of eighteen belongs to it, not to the table. And the law orders: ν is not an energy, a carries no unit, and the corridor constrains membership of an interval and nothing inside it (§8).

Five status words are used and never merged.

| status | meaning |
|---|---|
| **PROVED** | a proof is written out below and every step is justified |
| **MACHINE-CHECKED** | Z3 returned `unsat` on the negation of an obligation over a named finite family of points, with both guards passed (§9) |
| **EXHAUSTIVE** | a decision procedure visited every case in a stated finite family, in exact arithmetic |
| **MEASURED** | a number computed from the cited configurations by a stated procedure whose one parameter, the walk's ε, is stated |
| **CITED** | taken from the literature or a public database, with the source |

SAMPLED is not among them: no claim rests on a pseudorandom sweep. The one randomised step is a guard on the machine check (§9), not a result.

---

## §1 · Definitions

**D1 (subshell, capacity, node count).** A subshell is a pair (n, ℓ) of integers with n ≥ 1 and 0 ≤ ℓ ≤ n − 1, written nℓ with ℓ = 0, 1, 2, 3, 4 as s, p, d, f, g. Its capacity is `c(ℓ) := 2(2ℓ + 1)`, the number of one-electron states it holds. Its node count is

> `p(nℓ) := n − ℓ − 1`,

the number of radial nodes of the hydrogenic orbital nℓ (CITED: the node theorem for the radial equation). A subshell is **node-free** when p = 0; the node-free subshells are 1s, 2p, 3d, 4f, 5g, ….

**D2 (configuration, occupancy).** A configuration is a map q from subshells to integers with 0 ≤ q(nℓ) ≤ c(ℓ) and finite support; q(nℓ) is the occupancy of nℓ.

**D3 (the data, the step, the entrant).** For Z = 1, …, 108, `C_Z` is the ground configuration of the neutral atom of atomic number Z as tabulated in the NIST Atomic Spectra Database (Kramida, Ralchenko, Reader and the NIST ASD Team, version 5.12; CITED), with closed cores expanded; its occupancies sum to Z at every Z (EXHAUSTIVE, 108 of 108). The **step** Z is the passage from `C_{Z−1}` to `C_Z`. The **entrant** e(Z) is the subshell whose occupancy rises across the step. At every Z from 3 to 108 exactly one subshell gains (EXHAUSTIVE), so e(Z) is well defined; at twelve steps the gain is two electrons and another subshell loses one, and the entrant is the subshell that gains. The **walk** is the sequence of the 106 steps Z = 3, …, 108, from lithium to hassium.

**D4 (admissible set, frame, the two forms, the point set).** At step Z a subshell is **admissible** when it is not at capacity in the configuration before the step, `q_{Z−1}(nℓ) < c(ℓ)`. A **frame** F(N, Λ) is the set of subshells with n ≤ N and ℓ ≤ Λ; the default frame is F(15, 4). The **radicand** of an admissible subshell is, in the **node-only form**,

> `r := p(nℓ)`,

and in the **finished form**,

> `r := p(nℓ) + q_{Z−1}(nℓ) / c(ℓ)`,

which lies in [p, p + 1). The **point** of the subshell is `π(nℓ) := (√r, n) ∈ ℝ²`, and the **point set** `P_Z` of the step is the set of points of the admissible subshells in the frame. No two admissible subshells share a point in either form at any step (EXHAUSTIVE), so `P_Z` has one point per admissible subshell. Unless a form is named, the node-only form is meant.

**D5 (the law).** For a real number a, the **slope**, the law assigns to each admissible subshell

> `ν(nℓ) := n − a·√r = y − a·x`  at the point (x, y) = π(nℓ),

and states that the electron entering at step Z takes the admissible subshell of least ν. The law **holds with slope a at step Z** when e(Z) is the unique minimiser of ν over the admissible set.

**D6 (corridor).** For a finite point set P and a point s ∈ P, the **corridor** of s is

> `K(s) := { a ∈ ℝ : y_s − a·x_s < y_r − a·x_r for every r ∈ P, r ≠ s }`,

the set of slopes at which s is the unique minimiser of y − a·x. By Lemma 1 it is empty or an open interval (L, U) with L ∈ ℝ ∪ {−∞} and U ∈ ℝ ∪ {+∞}; L is the **floor** and U the **ceiling**. The corridor of the step, `K_Z`, is the corridor of the entrant's point in `P_Z`; `L_Z` and `U_Z` are its floor and ceiling. A corridor with L = −∞ **has no floor**; one with both bounds finite is **two-sided**.

**D7 (the lower hull, its vertices and edges).** For a finite set Q ⊂ ℝ² let

> `E(Q) := conv(Q) + {(0, t) : t ≥ 0}`,

the convex hull of Q together with everything above it. A point s ∈ P is a **vertex of the lower hull** of P when s ∉ E(P ∖ {s}). By Theorem 2(a) no two vertices share an abscissa, so the vertices are listed in order of increasing abscissa as v₁, …, v_m; the **hull edges** are the segments [v_i, v_{i+1}] and the **edge slopes** are `σ_i := slope(v_i, v_{i+1})`, where for points with x₁ ≠ x₂

> `slope((x₁, y₁), (x₂, y₂)) := (y₂ − y₁)/(x₂ − x₁)`.

For two subshell points with radicands r₁ ≠ r₂ this is `Δn·(√r₁ + √r₂)/(r₂ − r₁)`, rationalised. The vertices flanking a vertex v_i are v_{i−1} and v_{i+1}.

**D8 (the walk of the slope).** The carried slope starts at a = 0 before lithium. At each step Z in order, if `L_Z < a < U_Z` the value is kept; otherwise it is **recalibrated**: a := L_Z + ε when a ≤ L_Z, a := U_Z − ε when a ≥ U_Z, with ε = 10⁻⁶. A recalibration is a **move** when |Δa| > 10⁻³ and a **touch** otherwise. The **corridor fraction** at a two-sided step is `t := (a − L_Z)/(U_Z − L_Z)`; it is undefined where the corridor has no floor.

**D9 (running intersection, piercing).** The **running intersection** is the interval I carried along the walk: I := K₃ at lithium, and at each later step I := I ∩ K_Z if that is non-empty, in which case a is said to be **holdable**; otherwise the intersection **empties** at Z and I := K_Z. A set of slopes **pierces** a family of corridors when every corridor contains one of them; the **piercing number** is the least size of a piercing set. Two corridors are **disjoint** when they share no point.

**D10 (opening, the Madelung pick).** A subshell **opens** at Z when `q_{Z−1} = 0` and `q_Z > 0`. The **Madelung pick** at step Z is the admissible subshell in the frame with the least value of (n + ℓ, n) in lexicographic order.

---

## §2 · The hull theorem

**Lemma 1 (one inequality per rival).** Let P be finite, s ∈ P, and a ∈ ℝ. Then s is the unique minimiser of y − a·x over P if and only if for every r ∈ P ∖ {s}:

- if x_r = x_s, then y_r > y_s;
- if x_r > x_s, then a < slope(s, r);
- if x_r < x_s, then a > slope(r, s).

Consequently K(s) is empty if some r ≠ s has x_r = x_s and y_r ≤ y_s, and otherwise K(s) = (L, U) with

> `L := max { slope(r, s) : r ∈ P, x_r < x_s }`,  `U := min { slope(s, r) : r ∈ P, x_r > x_s }`,

where an empty maximum is −∞ and an empty minimum is +∞; K(s) is non-empty exactly when L < U.

*Proof.* The condition on r is `y_r − a·x_r > y_s − a·x_s`, that is `y_r − y_s > a·(x_r − x_s)`. If x_r = x_s it reads y_r > y_s. If x_r > x_s, division by the positive number x_r − x_s gives a < (y_r − y_s)/(x_r − x_s) = slope(s, r). If x_r < x_s, division by the negative number x_r − x_s reverses the inequality and gives a > (y_s − y_r)/(x_s − x_r) = slope(r, s). The three cases are exclusive and exhaustive over r. The set of a satisfying finitely many strict lower bounds and finitely many strict upper bounds is the open interval between the largest lower bound and the smallest upper bound, empty when the former is not below the latter. ∎ **PROVED.**

**Theorem 1 (the hull theorem).** Let P ⊂ ℝ² be finite and s ∈ P. The following are equivalent:

- (i) K(s) ≠ ∅: some slope makes s the unique minimiser of y − a·x;
- (ii) s ∉ E(P ∖ {s}): s is a vertex of the lower hull of P;
- (iii) no r ∈ P ∖ {s} has x_r = x_s and y_r ≤ y_s, and for every pair u, w ∈ P ∖ {s} with x_u < x_s < x_w the point s lies strictly below the line through u and w.

*Proof.* (i) ⇒ (ii). Suppose s ∈ E(P ∖ {s}): s = Σ_i λ_i p_i + (0, t) with p_i ∈ P ∖ {s}, λ_i ≥ 0, Σ λ_i = 1, t ≥ 0. For any a, the functional f_a(x, y) = y − a·x is affine, so f_a(s) = Σ λ_i f_a(p_i) + t ≥ min_i f_a(p_i). Hence some p_i ≠ s has f_a(p_i) ≤ f_a(s), and s is not the unique minimiser at a. As a was arbitrary, K(s) = ∅.

(ii) ⇒ (iii). Suppose (iii) fails. If some r has x_r = x_s and y_r ≤ y_s, then s = r + (0, y_s − y_r) ∈ E(P ∖ {s}). If some u, w with x_u < x_s < x_w have s on or above the line through them, write x_s = λx_u + (1 − λ)x_w with λ = (x_w − x_s)/(x_w − x_u) ∈ (0, 1); the point λu + (1 − λ)w lies on the segment [u, w] at abscissa x_s, and s is it plus (0, t) with t ≥ 0, so s ∈ E(P ∖ {s}). Either way (ii) fails.

(iii) ⇒ (i). By Lemma 1 it suffices to show L < U, since the same-abscissa clause of (iii) is exactly the first condition of the lemma. If no point lies to the left of s then L = −∞ < U; if none lies to the right then U = +∞ > L. Otherwise let u attain L among the left points and w attain U among the right points, so x_u < x_s < x_w, and suppose L ≥ U, that is slope(u, s) ≥ slope(s, w). The slope of the line through u and w is the convex combination

> `slope(u, w) = [ (x_s − x_u)·slope(u, s) + (x_w − x_s)·slope(s, w) ] / (x_w − x_u)`,

as the identity (y_w − y_u) = (y_s − y_u) + (y_w − y_s) shows after dividing by x_w − x_u. A convex combination of two numbers does not exceed the larger, so slope(u, w) ≤ slope(u, s). The height of the line through u and w at abscissa x_s is y_u + slope(u, w)·(x_s − x_u) ≤ y_u + slope(u, s)·(x_s − x_u) = y_s. So s lies on or above that line, contradicting (iii). Hence L < U and K(s) is non-empty. ∎ **PROVED.**

**MACHINE-CHECKED**, for the implication (i) ⇒ (ii) with k = 2, 3, 4, 5 points of arbitrary real coordinates — Z3 returns `unsat` on "s is the strict minimiser at some a, and s is a convex combination of the others plus a non-negative vertical shift" — and for the implication (iii) ⇒ (i) with k = 2, 3, 4 distinct points in the box [0, 10]², encoded as "the pairwise condition holds and for every real a some other point ties or beats s". Both guards pass (§9). **EXHAUSTIVE**: on the point set of every step, in both forms, and on every set of two to five points of the grid {0, 1, 2, 3}² read as (√r, n) with r ∈ {0, 1, 4, 9} — 6,868 point sets, 31,040 point instances — the three sets {corridor non-empty}, {pairwise condition} and {vertex returned by a monotone-chain hull algorithm with strict turns} coincide. The third route is an independent implementation (Andrew 1979, CITED) and enters only as a guard; nothing in the proof depends on it.

**Corollary 1 (at least two vertices).** If P has at least two distinct abscissae, its lower hull has at least two vertices, and so at least two points of P have non-empty corridors.

*Proof.* Let s be the lowest point among those of least abscissa and s′ the lowest among those of greatest abscissa; s ≠ s′ since their abscissae differ. For s, no pair u, w ∈ P ∖ {s} has x_u < x_s < x_w, because every point has x ≥ x_s, and every other point of abscissa x_s lies strictly above s. So s satisfies (iii) of Theorem 1 and is a vertex. The same holds for s′ with the inequalities reversed. ∎ **PROVED.**

At every step of the walk the admissible set carries several node counts, hence several abscissae, so at no step is the entrant the only subshell some slope could select. In the default frame every step has between 11 and 15 vertices (node-only) and between 7 and 15 (finished); in a frame limited to n ≤ 7 the counts run from 3 to 7 (node-only), with the distribution 3 at 6 steps, 4 at 56, 5 at 28, 6 at 14 and 7 at 2. **EXHAUSTIVE.** The count of vertices depends on the frame; that the count is at least two does not.

---

## §3 · The corridor is the interval between the flanking edge slopes

**Theorem 2 (corridor = flanking edge slopes).** Let P be finite and let v₁, …, v_m be the vertices of its lower hull. Then:

- (a) no two vertices share an abscissa, so the order by abscissa is strict;
- (b) for each i, the corridor of v_i is (L_i, U_i) with `L_i = slope(v_{i−1}, v_i)` for i > 1 and L₁ = −∞, and `U_i = slope(v_i, v_{i+1})` for i < m and U_m = +∞;
- (c) hence `U_i = L_{i+1}` for i < m: the edge slopes σ₁ < σ₂ < … < σ_{m−1} are strictly increasing, the corridors of the vertices are the consecutive open intervals (−∞, σ₁), (σ₁, σ₂), …, (σ_{m−1}, +∞), and they partition ℝ together with the edge slopes; at a = σ_i the minimum of y − a·x is attained at v_i, at v_{i+1}, and at exactly those points of P lying on the segment between them.

*Proof.* (a) If two vertices v, v′ share an abscissa with y_v ≤ y_{v′}, then v′ = v + (0, y_{v′} − y_v) ∈ E(P ∖ {v′}), so v′ is not a vertex.

(b) Fix a vertex v = v_i. By Theorem 1 its corridor (L, U) is non-empty, so L < U. Consider the points of P to the left of v. If there are none, L = −∞ by Lemma 1, and no vertex lies to the left of v since a vertex is a point of P. Otherwise let m₀ := L, the maximum of slope(r, v) over the left points, and let g be the line through v with slope m₀: g(x) = y_v + m₀·(x − x_v). Every point of P lies on or above g. For a left point r this is the maximality of m₀: slope(r, v) ≤ m₀ gives y_r ≥ g(x_r). For v itself it is equality. For a point r with x_r = x_v, y_r > y_v by Lemma 1. For a right point r, Lemma 1 gives y_r − y_v > a·(x_r − x_v) for every a in the non-empty interval (L, U); taking a slightly greater than L, y_r − y_v > m₀·(x_r − x_v), so r lies strictly above g. Let T be the set of left points attaining m₀; they lie on g, and distinct points of a non-vertical line have distinct abscissae, so T has a unique leftmost point u.

u is a vertex. Suppose not: u = Σ λ_i p_i + (0, t) with p_i ∈ P ∖ {u}, λ_i ≥ 0 summing to 1, t ≥ 0. Since g is affine and every point lies on or above it, y_u = Σ λ_i y_i + t ≥ Σ λ_i g(x_i) + t = g(x_u) + t = y_u + t, so t = 0 and every p_i with λ_i > 0 lies on g. The points of P on g are T ∪ {v}, all of abscissa ≥ x_u. Then x_u = Σ λ_i x_i with every x_i ≥ x_u forces x_i = x_u for every i with λ_i > 0, and a point of g with abscissa x_u is u itself, contradicting p_i ≠ u.

No vertex lies strictly between u and v in abscissa. A point r with x_u < x_r < x_v has y_r ≥ g(x_r), so r lies on or above the segment [u, v], and r ∈ E(P ∖ {r}) by the argument of Theorem 1, (ii) ⇒ (iii) read backwards: r is not a vertex.

Therefore u is the vertex immediately to the left of v, u = v_{i−1}, and L = slope(v_{i−1}, v_i). The statement for U is the mirror image under the reflection x ↦ −x, which sends slopes to their negatives, exchanges left with right, and sends the maximum defining L to the minimum defining U: the set of right points attaining U lies on a line h through v, every point lies on or above h, the rightmost such point w is a vertex, no vertex has abscissa strictly between x_v and x_w, and so w = v_{i+1} and U = slope(v_i, v_{i+1}).

(c) By (b), U_i = slope(v_i, v_{i+1}) = L_{i+1}. Each corridor is non-empty (Theorem 1), so σ_{i−1} = L_i < U_i = σ_i, and the edge slopes increase strictly. The intervals (σ_{i−1}, σ_i), with σ₀ = −∞ and σ_m = +∞, are pairwise disjoint and their union with {σ₁, …, σ_{m−1}} is ℝ. At a = σ_i the values y − σ_i·x at v_i and at v_{i+1} agree, since σ_i is the slope between them. For a in (σ_{i−1}, σ_i) the point v_i is the unique minimiser, and each r ↦ y_r − a·x_r is continuous in a, so at a = σ_i the value at v_i is still at most the value at every point: v_i and v_{i+1} are minimisers. A point r attains the same value exactly when it lies on the line through v_i and v_{i+1}. Such an r with x_r < x_{v_i} would give slope(r, v_i) = σ_i > σ_{i−1} = L_i, contradicting the maximality in Lemma 1; symmetrically none lies right of v_{i+1}. So the minimisers at σ_i are exactly the points of P on the segment [v_i, v_{i+1}]. ∎ **PROVED.**

**EXHAUSTIVE**: at every step of the walk, in both forms, and on the 6,868 grid sets of §2, the floor and ceiling of every vertex, computed from Lemma 1, equal the slopes to its flanking vertices, computed from the hull, as exact elements of ℚ(√ℕ).

So the corridor is not an interval that happens to be non-empty: it is one of the m cells into which the hull cuts the slope axis, and its endpoints are hull edges. Figure 1 shows the point set at lanthanum, where 5d enters with 4f to its left and 6p to its right: the corridor is (slope(4f, 5d), slope(5d, 6p)) = (√2/2, (2 + √2)/2).

![Figure 1](figures/fig1-hull-and-corridor.png)

*Figure 1. Left: the admissible subshells at Z = 57 (lanthanum) as points (√r, n) in the node-only form, drawn in the frame n ≤ 8, ℓ ≤ 4, with the lower convex hull; the entrant 5d is a vertex, flanked by 4f and 6p. Right: the subshell a line of slope a reaches first, as a runs across the axis; 5d is reached exactly on the corridor (√2/2, (2 + √2)/2) = (0.7071068, 1.7071068), and the endpoints are the two hull-edge slopes.*

---

## §4 · The atomic point set, its frame, and the 106 corridors

**Theorem 3 (the corridor does not depend on the frame).** At every step of the walk, in either form, the entrant's corridor computed over the admissible subshells of the frame F(15, 4) equals the corridor computed over all admissible subshells whatever, with no bound on n or ℓ.

*Proof.* Over the 106 steps the entrant's point has radicand r_e ≤ 6 (node-only) or r_e ≤ 13/2 (finished) and n_e ≤ 7; the largest ceiling over the walk is `U_max = √6 + √7 = 5.0952411` (node-only) and `(10√11 + 5√26)/9 = 6.5179273` (finished); the smallest finite floor is `L_min = 0` (node-only) and `−√14 = −3.7416574` (finished). These extremes are computed exactly (EXHAUSTIVE). Let s be any admissible subshell outside the frame, with quantum numbers (n, ℓ) and radicand r. Its radicand satisfies r ≤ n − 1 in the node-only form and r < n in the finished form, because p = n − ℓ − 1 ≤ n − 1 and the fractional part is below 1.

First suppose n ≥ 38 (node-only) or n ≥ 56 (finished). If x_s > x_e, then by Lemma 1 the subshell can only lower the ceiling, and its candidate value is slope(e, s) = (n − n_e)/(√r − √r_e) ≥ (n − 7)/√(n − 1) =: φ(n) in the node-only form, or ≥ (n − 7)/√n =: ψ(n) in the finished form. Both are increasing for n ≥ 8: the derivative of φ is (n + 5)/(2(n − 1)^{3/2}) > 0 and that of ψ is (n + 7)/(2n^{3/2}) > 0. Now φ(38) = 31/√37 = 5.0963686 > U_max and ψ(56) = 49/√56 = 6.5479004 > U_max (EXHAUSTIVE, exact), so the candidate value exceeds the existing ceiling and the minimum in Lemma 1 is unchanged. If x_s < x_e, the subshell can only raise the floor, with candidate value slope(s, e) = (n_e − n)/(x_e − x_s) ≤ −(n − 7)/√r_e ≤ −31/√6 = −12.6556970 (node-only) or ≤ −49/√(13/2) = −19.2193812 (finished), each below L_min; and this case arises only when r_e > 0, in which case the frame already supplies a finite floor (Theorem 4 below), so the maximum is unchanged. If x_s = x_e, then n > n_e and the subshell imposes no constraint.

Second, every subshell with n ≤ 37 (node-only) or n ≤ 55 (finished), and every ℓ ≤ n − 1, is in the frame F(37, 36), respectively F(55, 54); and the corridors computed in those frames equal the corridors computed in F(15, 4) at all 106 steps (EXHAUSTIVE). The two cases exhaust the admissible subshells outside F(15, 4). ∎ **PROVED**, with its extremes and its two closed frames **EXHAUSTIVE**.

The frames F(8, 4), F(12, 4), F(20, 4), F(30, 4), F(15, 14) and F(8, 14) also give the F(15, 4) corridors at every step in the node-only form, and F(12, 4), F(20, 4), F(30, 4) and F(15, 14) do so in the finished form; F(8, 4) does not in the finished form, differing at Z = 38, 43, 48, 56, 80, 88. A frame limited to n ≤ 7 differs from the full set in the node-only form at exactly three steps — francium, radium and lawrencium — where it has no subshell to the right of the entrant and so no ceiling, and it has 17 distinct endpoints where the full set has 19: the two it lacks are the ceilings √6 + √7 of the 7s steps and (√5 + √7)/2 of lawrencium. **EXHAUSTIVE.**

**Table 1 — the 106 node-only corridors.** Consecutive steps with the same entrant, floor and ceiling are one row. u and w are the hull vertices flanking the entrant; L = slope(u, e) and U = slope(e, w) by Theorem 2, and — is the absence of a neighbour. Every entry is exact; the decimals are rounded to seven places.

| Z | elements | entrant | p | u | L | U | w | L | U |
|---|---|---|---|---|---|---|---|---|---|
| 3–4 | Li, Be | 2s | 1 | 2p | 0 | 1 + √2 | 3s | 0.0000000 | 2.4142136 |
| 5–10 | B – Ne | 2p | 0 | — | −∞ | √2/2 | 3s | — | 0.7071068 |
| 11–12 | Na, Mg | 3s | 2 | 3d | 0 | √2 + √3 | 4s | 0.0000000 | 3.1462644 |
| 13–18 | Al – Ar | 3p | 1 | 3d | 0 | (1 + √3)/2 | 4s | 0.0000000 | 1.3660254 |
| 19–20 | K, Ca | 4s | 3 | 3d | √3/3 | 2 + √3 | 5s | 0.5773503 | 3.7320508 |
| 21–24 | Sc – Cr | 3d | 0 | — | −∞ | √2/2 | 4p | — | 0.7071068 |
| 25 | Mn | 4s | 3 | 3d | √3/3 | 2 + √3 | 5s | 0.5773503 | 3.7320508 |
| 26–29 | Fe – Cu | 3d | 0 | — | −∞ | √2/2 | 4p | — | 0.7071068 |
| 30 | Zn | 4s | 3 | 4f | 0 | 2 + √3 | 5s | 0.0000000 | 3.7320508 |
| 31–36 | Ga – Kr | 4p | 2 | 4f | 0 | (2 + √2)/2 | 5s | 0.0000000 | 1.7071068 |
| 37–38 | Rb, Sr | 5s | 4 | 4d | 1 | 2 + √5 | 6s | 1.0000000 | 4.2360680 |
| 39–41 | Y – Nb | 4d | 1 | 4f | 0 | (1 + √3)/2 | 5p | 0.0000000 | 1.3660254 |
| 42 | Mo | 4d | 1 | 4f | 0 | 1 | 5s | 0.0000000 | 1.0000000 |
| 43 | Tc | 5s | 4 | 4d | 1 | 2 + √5 | 6s | 1.0000000 | 4.2360680 |
| 44 | Ru | 4d | 1 | 4f | 0 | (1 + √3)/2 | 5p | 0.0000000 | 1.3660254 |
| 45–46 | Rh, Pd | 4d | 1 | 4f | 0 | 1 | 5s | 0.0000000 | 1.0000000 |
| 47–48 | Ag, Cd | 5s | 4 | 4f | 1/2 | 2 + √5 | 6s | 0.5000000 | 4.2360680 |
| 49–54 | In – Xe | 5p | 3 | 4f | √3/3 | (√3 + √5)/2 | 6s | 0.5773503 | 1.9840594 |
| 55–56 | Cs, Ba | 6s | 5 | 5d | (√2 + √5)/3 | √5 + √6 | 7s | 1.2167605 | 4.6855577 |
| 57 | La | 5d | 2 | 4f | √2/2 | (2 + √2)/2 | 6p | 0.7071068 | 1.7071068 |
| 58–63 | Ce – Eu | 4f | 0 | — | −∞ | √2/2 | 5d | — | 0.7071068 |
| 64 | Gd | 5d | 2 | 4f | √2/2 | (2 + √2)/2 | 6p | 0.7071068 | 1.7071068 |
| 65–70 | Tb – Yb | 4f | 0 | — | −∞ | √2/2 | 5d | — | 0.7071068 |
| 71–78 | Lu – Pt | 5d | 2 | 5g | 0 | (2 + √2)/2 | 6p | 0.0000000 | 1.7071068 |
| 79 | Au | 5d | 2 | 5g | 0 | (√2 + √5)/3 | 6s | 0.0000000 | 1.2167605 |
| 80 | Hg | 6s | 5 | 5f | (1 + √5)/4 | √5 + √6 | 7s | 0.8090170 | 4.6855577 |
| 81–86 | Tl – Rn | 6p | 4 | 5f | 1 | (2 + √6)/2 | 7s | 1.0000000 | 2.2247449 |
| 87–88 | Fr, Ra | 7s | 6 | 6d | (√3 + √6)/3 | √6 + √7 | 8s | 1.3938469 | 5.0952411 |
| 89–90 | Ac, Th | 6d | 3 | 5f | (1 + √3)/2 | (√3 + √5)/2 | 7p | 1.3660254 | 1.9840594 |
| 91–95 | Pa – Am | 5f | 1 | 5g | 0 | (1 + √3)/2 | 6d | 0.0000000 | 1.3660254 |
| 96 | Cm | 6d | 3 | 5f | (1 + √3)/2 | (√3 + √5)/2 | 7p | 1.3660254 | 1.9840594 |
| 97–102 | Bk – No | 5f | 1 | 5g | 0 | (1 + √3)/2 | 6d | 0.0000000 | 1.3660254 |
| 103 | Lr | 7p | 5 | 6d | (√3 + √5)/2 | (√5 + √7)/2 | 8s | 1.9840594 | 2.4409096 |
| 104–108 | Rf – Hs | 6d | 3 | 5g | √3/3 | (√3 + √5)/2 | 7p | 0.5773503 | 1.9840594 |

All 106 corridors are non-empty; 80 are two-sided, 26 have no floor, none lacks a ceiling. **EXHAUSTIVE.** In the finished form all 106 are likewise non-empty, with 138 distinct endpoints.

**Table 2 — the nineteen endpoints.** Every floor and every ceiling of Table 1 is one of nineteen numbers. The last two columns count the corridors taking the value as floor and as ceiling; the floors sum to 80 and the ceilings to 106.

| value | decimal | as floor | as ceiling |
|---|---|---|---|
| 0 | 0.0000000 | 44 | 0 |
| 1/2 | 0.5000000 | 2 | 0 |
| √3/3 | 0.5773503 | 14 | 0 |
| √2/2 | 0.7071068 | 2 | 26 |
| (1 + √5)/4 | 0.8090170 | 1 | 0 |
| 1 | 1.0000000 | 9 | 3 |
| (√2 + √5)/3 | 1.2167605 | 2 | 1 |
| (1 + √3)/2 | 1.3660254 | 3 | 21 |
| (√3 + √6)/3 | 1.3938469 | 2 | 0 |
| (2 + √2)/2 | 1.7071068 | 0 | 16 |
| (√3 + √5)/2 | 1.9840594 | 1 | 14 |
| (2 + √6)/2 | 2.2247449 | 0 | 6 |
| 1 + √2 | 2.4142136 | 0 | 2 |
| (√5 + √7)/2 | 2.4409096 | 0 | 1 |
| √2 + √3 | 3.1462644 | 0 | 2 |
| 2 + √3 | 3.7320508 | 0 | 4 |
| 2 + √5 | 4.2360680 | 0 | 5 |
| √5 + √6 | 4.6855577 | 0 | 3 |
| √6 + √7 | 5.0952411 | 0 | 2 |

The nineteen are pairwise distinct as elements of ℚ(√2, √3, √5, √6, √7), and consecutive values are separated by more than 1/10,000 — the least separation is certified above 0.0267 (node-only) and above 0.0002178 (finished form, 138 endpoints). **EXHAUSTIVE.**

**Proposition 1 (the ns against (n − 1)d crossing).** At the opening of ns for n = 4, 5, 6, 7 — potassium, rubidium, caesium, francium — the floor is supplied by (n − 1)d and equals

> `L = (√(n − 1) + √(n − 4)) / 3`,

which is √3/3 = 0.5773503, 1, (√2 + √5)/3 = 1.2167605 and (√3 + √6)/3 = 1.3938469.

*Proof.* The node counts are p(ns) = n − 1 and p((n − 1)d) = n − 4, and Δn = 1, so slope((n − 1)d, ns) = 1/(√(n − 1) − √(n − 4)). Multiplying numerator and denominator by √(n − 1) + √(n − 4) and using (u + v)(u − v) = u² − v², an identity of degree two verified on a 3 × 3 rational grid, gives (√(n − 1) + √(n − 4))/((n − 1) − (n − 4)) = (√(n − 1) + √(n − 4))/3. That (n − 1)d is the flanking vertex at those four steps is Table 1, and the four floors equal the closed form exactly. ∎ **PROVED**; the four instances **EXHAUSTIVE.**

**How the numbers are decided.** Every endpoint is a finite sum Σ c_m √m with rational c_m and squarefree m, held in that form. Two such sums are equal exactly when their representations coincide, because {1} ∪ {√m : m squarefree > 1} is linearly independent over ℚ (Besicovitch 1940, CITED); the sign of a non-zero sum is decided by enclosing each √m between rationals and refining until the enclosure of the sum excludes zero, which the same theorem guarantees terminates. Over the whole computation the deepest enclosure needed was 24 decimal digits and the smallest non-zero magnitude certified was above 4.43 × 10⁻⁸. No comparison in §§2–5 and §7 is made in floating point.

---

## §5 · The floor

**Theorem 4 (no floor exactly when node-free).** In the node-only form, at every step of the walk, `L_Z = −∞` if and only if the entrant is node-free, p(e(Z)) = 0. In the finished form, `L_Z = −∞` if and only if the entrant is node-free and empty before the step — that is, a node-free subshell opening — which happens at Z = 5 (2p, boron), 21 (3d, scandium) and 58 (4f, cerium).

*Proof.* By Lemma 1, L_Z = −∞ exactly when no admissible subshell has a point strictly to the left of the entrant's, that is, no admissible r has radicand r_r < r_e. Radicands are non-negative. If r_e = 0 there is nothing to the left and L_Z = −∞. If r_e > 0, the subshell 5g is admissible at every step of the walk — it is node-free, its capacity is 18, and no tabulated ground configuration up to Z = 108 occupies a g subshell (EXHAUSTIVE) — and its radicand is 0 in either form, since p(5g) = 0 and its occupancy is 0. So 5g lies strictly to the left of the entrant and L_Z is finite. Hence L_Z = −∞ ⟺ r_e = 0. In the node-only form r_e = p(e), and r_e = 0 ⟺ e is node-free. In the finished form r_e = p(e) + q_{Z−1}(e)/c(ℓ), which is 0 ⟺ p(e) = 0 and q_{Z−1}(e) = 0 ⟺ e is node-free and opens at Z. The three steps are read off the data. ∎ **PROVED**; the equivalence at all 106 steps, both forms, **EXHAUSTIVE.**

In the node-only form the 26 steps without a floor are the 2p steps 5–10, the 3d steps 21–24 and 26–29, and the 4f steps 58–63 and 65–70; 1s does not enter the walk and 5g never enters. The corridor fraction t is defined at the other 80 steps.

**Corollary 2 (the two f openings).** At cerium (Z = 58) 4f opens with p = 0: the corridor is (−∞, √2/2), the ceiling supplied by 5d, and t is undefined. At protactinium (Z = 91) 5f opens with p = 5 − 3 − 1 = 1: the corridor is (0, (1 + √3)/2), the floor 0 supplied by 5g — the only admissible node-free subshell at that step, the four others 1s, 2p, 3d, 4f being full at thorium — and the ceiling (1 + √3)/2 = 1.3660254 by 6d. The carried slope arrives at protactinium at (√3 + √6)/3 + ε = 1.3938 from francium, above the ceiling, and is placed at U − ε; so t = 1 − ε/U, which is 1 to the precision of the walk. **EXHAUSTIVE** for the corridors, **MEASURED** for the walk's arrival.

The floor at protactinium is 0 because Δn = 0 between 5g and 5f: a rival with the same n and a smaller radicand contributes a floor of exactly 0, which is why 44 of the 80 two-sided corridors have floor 0 (Table 2). If g subshells are removed from the candidate set (ℓ ≤ 3), the node-free subshells are 1s, 2p, 3d, 4f, all full from lutetium on, and the set of steps without a floor grows by exactly the eleven 5f steps 91–95 and 97–102 (curium, Z = 96, enters 6d and is not among them): the equivalence of Theorem 4 then fails at those eleven and holds elsewhere. **EXHAUSTIVE.** The paper's convention — every subshell not at capacity is admissible, whatever its ℓ — is the law's own admissibility test; it is the convention under which Theorem 4 holds without exception, and it is stated here because no observation below Z = 109 distinguishes it from the alternative.

---

## §6 · The walk and its recalibrations

The walk of D8 is a placement rule, not a law: it says where in its corridor a is put when the corridor forces a change, and it moves a the least distance that re-enters. Its one parameter is ε.

**Table 3 — the eighteen recalibrations of the node-only walk.** "Endpoint" is the bound the carried value is placed ε inside. A move changes a by more than 10⁻³; a touch by exactly 2ε, because the carried value already sat ε beyond the endpoint the new corridor shares with the last one.

| Z | element | entrant | kind | endpoint | value |
|---|---|---|---|---|---|
| 3 | Li | 2s | initial placement | L = 0 | 0.0000000 |
| 19 | K | 4s | move | L = √3/3 | 0.5773503 |
| 37 | Rb | 5s | move | L = 1 | 1.0000000 |
| 42 | Mo | 4d | touch | U = 1 | 1.0000000 |
| 43 | Tc | 5s | touch | L = 1 | 1.0000000 |
| 45 | Rh | 4d | touch | U = 1 | 1.0000000 |
| 55 | Cs | 6s | move | L = (√2 + √5)/3 | 1.2167605 |
| 58 | Ce | 4f | move | U = √2/2 | 0.7071068 |
| 64 | Gd | 5d | touch | L = √2/2 | 0.7071068 |
| 65 | Tb | 4f | touch | U = √2/2 | 0.7071068 |
| 80 | Hg | 6s | move | L = (1 + √5)/4 | 0.8090170 |
| 81 | Tl | 6p | move | L = 1 | 1.0000000 |
| 87 | Fr | 7s | move | L = (√3 + √6)/3 | 1.3938469 |
| 91 | Pa | 5f | move | U = (1 + √3)/2 | 1.3660254 |
| 96 | Cm | 6d | touch | L = (1 + √3)/2 | 1.3660254 |
| 97 | Bk | 5f | touch | U = (1 + √3)/2 | 1.3660254 |
| 103 | Lr | 7p | move | L = (√3 + √5)/2 | 1.9840594 |
| 104 | Rf | 6d | touch | U = (√3 + √5)/2 | 1.9840594 |

**Proposition 2 (the recalibration sites).** In the node-only form, with ε = 10⁻⁶:

- (a) there are 18 recalibrations: the initial placement, 9 moves and 8 touches, at the steps of Table 3;
- (b) the sites, and the endpoint reached at each, are the same for ε = 10⁻⁴, 10⁻⁶, 10⁻⁸ and 10⁻¹⁰, and every touch changes a by exactly 2ε;
- (c) at every touch the endpoint reached is the endpoint at which a was last placed: the four consecutive pairs Mo/Tc, Gd/Tb, Cm/Bk and Lr/Rf have corridors sharing exactly one endpoint — 1, √2/2, (1 + √3)/2 and (√3 + √5)/2 respectively — one's ceiling being the other's floor;
- (d) eight of the nine moves occur at the opening of the entering subshell; the ninth, at mercury, re-enters 6s, which had opened at caesium and been left at gold;
- (e) every subshell fills at constant a — no move falls strictly between its opening and its completion — except 5d, open from lanthanum (57) to gold (79) and moved at cerium (58), and 6d, open from actinium (89) to the end of the table and moved at protactinium (91) and lawrencium (103).

**MEASURED**, from the corridors of Table 1 by the rule of D8; (b) is the invariance of the measurement under the rule's parameter. A second, independently written implementation of the same rule over a candidate set truncated at n ≤ 8 with the first empty subshell of each ℓ finds the same 18 sites, the same nine values to within 10⁻¹⁵, and the same partition into moves and touches; its candidate set lacks a ceiling at seven ns openings — lithium, sodium, potassium, rubidium, silver, caesium, francium — and that difference changes no site, since at each of those steps a arrives from below.

*Why the walk is decided exactly although a is a floating-point number.* The test L_Z < a < U_Z compares a value that is always a corridor endpoint plus or minus ε, ε ≥ 10⁻¹⁰, against endpoints that are pairwise separated by more than 10⁻⁴ (§4) or equal as exact numbers. A comparison between distinct endpoints has margin above 10⁻⁴ and cannot be flipped by double-precision rounding; a comparison against the endpoint a sits on has margin ε; a comparison against an equal endpoint of a later corridor — a touch — is decided by the sign of ε. The floating-point walk therefore reproduces the walk that would be run in exact arithmetic with the same ε, which is why the sites are ε-invariant over six orders of magnitude.

In the finished form the same rule recalibrates 15 times — the initial placement and 14 moves, no touches — at potassium, manganese, rubidium, technetium, caesium, cerium, gadolinium, terbium, francium, protactinium, curium, berkelium, lawrencium and rutherfordium, at the floor except at the f entrants cerium, terbium, protactinium and berkelium and at rutherfordium, where it is the ceiling. **MEASURED.**

![Figure 2](figures/fig2-walk-and-resets.png)

*Figure 2. The carried slope of the node-only walk against Z. Grey bands are the corridors of Table 1 (a band open at the bottom has no floor); the blue line is a; filled circles are the nine moves and open circles the eight touches. The slope is constant across every subshell's filling except 5d, moved at cerium, and 6d, moved at protactinium and lawrencium.*

---

## §7 · One slope for many steps

**Proposition 3 (the running intersection).** In the node-only form the running intersection empties fourteen times, at Z = 37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103 and 104; in the finished form eleven times, at Z = 25, 43, 58, 64, 65, 87, 91, 96, 97, 103 and 104. **EXHAUSTIVE**, exact.

An emptying is a fact about the intervals alone, independent of where a sits; every emptying forces a recalibration of any placement rule that keeps a inside the corridors. The four remaining node-only recalibrations — potassium, thallium, francium and the initial placement at lithium — are not forced by emptiness; they are where this particular rule, arriving from below, finds the floor above it.

**Theorem 5 (the piercing number).** In the node-only form the piercing number of the 106 corridors is exactly 3; in the finished form exactly 4.

*Proof.* A piercing set contains at least one slope in each corridor of any pairwise-disjoint subfamily, and distinct disjoint corridors need distinct slopes, so the piercing number is at least the size of any pairwise-disjoint subfamily. In the node-only form the corridors of boron, (−∞, √2/2), lanthanum, (√2/2, (2 + √2)/2), and lawrencium, ((√3 + √5)/2, (√5 + √7)/2), are pairwise disjoint as exact intervals — each ceiling is at most the next floor — so the piercing number is at least 3. The three rationals 7071067/10⁷, 17071067/10⁷ and 3051137/1250000 lie, respectively, strictly inside every corridor of Table 1 that contains one of them, and every one of the 106 contains one of the three; so the piercing number is at most 3. In the finished form the corridors of cerium, lanthanum, curium and lawrencium are pairwise disjoint and the four rationals 1380131/2000000, 17071067/10⁷, 19840593/10⁷ and 3051137/1250000 pierce all 106. Both memberships are decided exactly. ∎ **PROVED** from an **EXHAUSTIVE** certificate on each side.

Both bounds are exhibited, so the general theorem that for intervals on a line the largest pairwise-disjoint subfamily and the smallest piercing set have the same size is not needed here; the certificate is the pair of sets.

**Proposition 4 (coverage by one slope).** The number of corridors containing a given slope is piecewise constant between consecutive endpoints, so its maximum is found by probing one rational in each of the twenty gaps between the nineteen endpoints and beyond them. The maximum is 86 of 106, attained on the band (√3/3, √2/2) and on no other; in the finished form it is 90 of 106, on the band (1, (5√2 + √5)/9). **EXHAUSTIVE**, exact.

![Figure 3](figures/fig3-corridors.png)

*Figure 3. The 106 node-only corridors as intervals on the slope axis, one per row, with the nineteen distinct endpoints as vertical rules; an arrow at the left edge marks a corridor with no floor. The three highlighted corridors — boron, lanthanum, lawrencium — are pairwise disjoint, so no slope serves fewer than three of them at once. The shaded band (√3/3, √2/2) is where one slope covers the most corridors: 86 of 106.*

---

## §8 · What the law does not do

**It does not determine a.** By Theorem 2 the ordering data at a step confine a to a cell of the hull's partition of the slope axis and say nothing about where in that cell a sits. Any placement rule that respects the cells reproduces the observed entrant at every step by construction; the count of recalibrations belongs to the rule. The eighteen of §6 are what the rule "hold, else move least" costs, and the fourteen forced emptyings of Proposition 3 are what every rule costs.

**It does not predict.** Asked, at each step Z from 4 to 108, which subshell the slope carried out of step Z − 1 selects, the node-only walk names the observed entrant at 88 of the 105 steps, with no ties, missing at 19, 37, 42, 43, 45, 55, 58, 64, 65, 80, 81, 87, 91, 96, 97, 103 and 104 — its own recalibration sites less lithium, together with the touches; the finished form names it at 91, missing at 19, 25, 37, 43, 55, 58, 64, 65, 87, 91, 96, 97, 103 and 104. The memoryless Madelung pick, which carries nothing from step to step and has no parameter, names the observed entrant at 96 of 106, missing at 42, 45, 46, 57, 64, 79, 89, 90, 96 and 103. **MEASURED** and **EXHAUSTIVE** respectively. Out of sample the law with its carried slope does worse than the rule it re-expresses.

**A non-empty corridor is not a confirmation.** By Corollary 1 every step admits at least two subshells that some slope selects, and in the default frame at least eleven. The observed entrant being among them is a constraint the form passes, not a prediction it makes. An empty corridor at any step would refute the form; the 106 non-empty ones do not confirm it. The Madelung pick, too, is a hull vertex at every step in both forms (**EXHAUSTIVE**): the form admits the rule it is measured against as readily as it admits the observed order.

**It orders; it does not value.** ν is not an energy and a has no unit; the point set is built from node counts and capacities, and the only numbers the law produces are the nineteen edge slopes of Table 2, elements of ℚ(√2, √3, √5, √6, √7) fixed by arithmetic on integers. The law says which admissible subshell comes first; it says nothing about how far the others are behind, and no quantity in it is comparable with a binding energy. Nor is the Madelung number a linear object in this plane: since n + ℓ = 2n − p − 1 (an identity, checked on the frame), with x = √p and y = n the level sets of n + ℓ are the parabolas 2y − x² − 1 = constant, whereas ν sweeps lines. The two rules are different geometric objects that agree on most of the occupied region, and their disagreement is a matter of ordering, not of value.

---

## §9 · Verification record

| object | PROVED | EXHAUSTIVE | MACHINE-CHECKED (Z3) | CITED / MEASURED |
|---|---|---|---|---|
| D3, the data | — | 108 electron counts; one entrant at each of 106 steps; no g subshell occupied | — | configurations CITED |
| D4, distinct points | — | 106 steps × 2 forms | — | — |
| Lemma 1 | ✓ | — | — | — |
| **Theorem 1** | ✓ | 212 step-instances; **6,868 grid sets**, 31,040 point instances; three routes agree | **✓ 7 obligations**: (i)⇒(ii) for k = 2…5 points, all real coordinates; (iii)⇒(i) for k = 2…4 distinct points in [0,10]² | third route CITED (Andrew 1979) |
| Corollary 1 | ✓ | vertex counts at 106 steps, two forms, two frames | — | — |
| **Theorem 2** | ✓ | endpoints = flanking edge slopes at 212 step-instances and 6,868 grid sets, exact | — | — |
| **Theorem 3** | ✓ | extremes of L, U, r_e, n_e; the four bounds; frames F(37,36), F(55,54) and eight others | — | — |
| Table 1, Table 2 | — | 106 corridors; 19 endpoints, min gap 0.0267; 138 in the finished form, min gap 0.0002178 | — | — |
| Proposition 1 | ✓ | (u+v)(u−v) = u²−v² on a 3×3 grid; four floors exact | — | — |
| **Theorem 4** | ✓ | both forms, 106 steps; without g, the eleven 5f exceptions | — | — |
| Corollary 2 | — | Ce and Pa corridors exact; Pa's floor from 5g | — | the arrival at Pa MEASURED |
| Table 3, Proposition 2 | — | four consecutive pairs share one endpoint, exact | — | MEASURED, ε ∈ {10⁻⁴, 10⁻⁶, 10⁻⁸, 10⁻¹⁰}; independent implementation agrees |
| Proposition 3 | — | running intersection, exact, both forms | — | — |
| **Theorem 5** | ✓ | disjoint triple and piercing triple exact; disjoint quadruple and piercing quadruple exact | — | — |
| Proposition 4 | — | 20 probes between 19 endpoints; 139 between 138 | — | — |
| §8, prediction | — | Madelung pick 96 of 106; Madelung pick a vertex at 106 steps, two forms | — | walk scores MEASURED |
| exact arithmetic | — | every sign by rational enclosure; deepest 24 digits; least certified magnitude 4.43 × 10⁻⁸ | — | linear independence CITED (Besicovitch 1940) |

**The exhausted families, named.** 106 steps: Z = 3 to 108, each in the node-only and the finished form. 6,868 grid sets: every set of two, three, four or five distinct points of {(√r, n) : r ∈ {0, 1, 4, 9}, n ∈ {0, 1, 2, 3}}. 108 electron counts: Z = 1 to 108. Ten frames: F(8,4), F(12,4), F(20,4), F(30,4), F(15,14), F(8,14), F(37,36), F(55,54), F(7,4) and F(8,4) in the finished form, each at 106 steps. 20 probes: one rational strictly between each pair of consecutive endpoints and one beyond each end.

**The obligation count.** One hundred and thirteen obligations run and none fails: 89 EXHAUSTIVE, 17 guards, and 7 MACHINE-CHECKED. The self-test adds three negative controls, each of which must be reported as refuted, and each is: a hull algorithm that keeps collinear points, which disagrees with the corridor identity at 18 of the 106 steps; the wrong crossing formula (√(n − 1) + √(n − 4))/2, which fails against potassium's floor; and the false claim that the strict minimiser is always the point of least y, which Z3 returns satisfiable with a model. A fourth control runs in every run, inside the encoding guard: a deliberately wrong reference — the hull without its first vertex — is caught with 300 disagreements.

**The two guards on the machine check.** *Non-vacuity*: both hypotheses — "s is the strict minimiser at some a" and "the pairwise condition holds for four distinct points" — are satisfiable. *Encoding fidelity*: the Z3 predicate for "s ∉ E(P ∖ {s})" is evaluated on 300 pseudorandom point sets of two to five points (1,041 point instances, seed 11) and agrees with the monotone-chain hull in every case, while the deliberately wrong reference disagrees 300 times; and the strict-minimiser formula agrees with brute-force minimisation over a rational slope on 300 further instances. These 600 instances are a guard on the encoding and not a result of the paper.

**What is not machine-checked, and why.** Theorem 2 is proved and exhaustively verified on the atomic steps and the grid family; its statement quantifies over the hull's vertex order, which is not first-order in the point coordinates without enumerating orderings, and the exhaustive family is where its content lies. Theorem 3 rests on two inequalities proved by a derivative and evaluated exactly at n = 38 and n = 56, and on two closed frames checked exhaustively. The walk is a measurement with a stated parameter; its exactness argument is in §6. The converse direction of Theorem 1 is machine-checked for up to four points in a bounded box because the universal quantifier over a makes the obligation harder for the solver; the proof is general.

---

## References

- Allen, L. C. and Knight, E. T. (2002). The Löwdin challenge: origin of the n + l, n (Madelung) rule for filling the orbital configurations of the periodic table. *International Journal of Quantum Chemistry* **90**, 80–88. — the standing of the derivation problem the law re-poses.
- Andrew, A. M. (1979). Another efficient algorithm for convex hulls in two dimensions. *Information Processing Letters* **9**, 216–219. — the monotone-chain algorithm used as the third, independent route to the vertex set.
- Besicovitch, A. S. (1940). On the linear independence of fractional powers of integers. *Journal of the London Mathematical Society* **15**, 3–6. — linear independence over ℚ of the square roots of distinct squarefree integers, on which the exact decision of every endpoint rests.
- Demkov, Yu. N. and Ostrovsky, V. N. (1972). n + l filling rule in the periodic system and focusing potentials. *Soviet Physics JETP* **35**, 66–69. — a potential class whose levels depend on n + ℓ alone.
- de Moura, L. and Bjørner, N. (2008). Z3: an efficient SMT solver. In *Tools and Algorithms for the Construction and Analysis of Systems*, Lecture Notes in Computer Science **4963**, 337–340. — the solver behind every MACHINE-CHECKED obligation.
- Janet, C. (1929). *Considérations sur la structure du noyau de l'atome*. Beauvais. — the left-step table and the n + ℓ ordering before Madelung.
- Klechkovskii, V. M. (1962). Justification of the rule for successive filling of (n + l) groups. *Soviet Physics JETP* **14**, 334–335. — the (n + ℓ, n) rule in the form the Madelung pick uses.
- Kramida, A., Ralchenko, Yu., Reader, J. and the NIST ASD Team (2024). *NIST Atomic Spectra Database*, version 5.12. https://physics.nist.gov/asd, DOI 10.18434/T4W30F. — the ground configurations of the 108 neutral atoms.
- Löwdin, P.-O. (1969). Some comments on the periodic system of the elements. *International Journal of Quantum Chemistry* **3** (S3A), 331–334. — the challenge to derive the filling rule.
- Madelung, E. (1936). *Die mathematischen Hilfsmittel des Physikers*, 3rd edition. Springer, Berlin. — the n + ℓ rule as usually attributed.
