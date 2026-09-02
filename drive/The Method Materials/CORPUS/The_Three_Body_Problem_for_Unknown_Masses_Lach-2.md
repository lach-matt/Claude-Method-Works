
# The Three-Body Problem for Unknown Masses
## A Closed Index of Families

**Matthew Lach** — Independent researcher

<div class='abstract'><b>Abstract.</b> The gravitational three-body problem is posed for three positive masses m₁, m₂, m₃ that are not specified. We show that the problem has a complete solution in the exact sense given to *complete* by the theory of closed indexes: a coordinate system for the totality of motions that is closed under its own meet and join, has defect E = 0, and therefore lists every family of motion and predicts no individual trajectory. We derive the solution's coordinates (the shape sphere), its metric (the Jacobi–Maupertuis metric on shape space), its five fixed points (Euler and Lagrange), its algebraic potential (a degree-8 norm), its strata (quasi-periodic, periodic, chaotic, ergodic, collisional), and the law that forbids anything sharper: the three-body constraint graph is a triangle, and a triangle's exact bound is a sum, a difference and a symmetric function at once — the three forms a closed index cannot carry. The result is proved uniformly over all thirteen order-types of the masses. Every component is attributed; two things are new, and they are named.</div>

---

## 1. What is being asked, and what an answer can be

Poincaré (1890) proved there is no analytic first integral of the three-body problem beyond energy, linear momentum and angular momentum, and hence no global algebraic formula r~i~(t). That theorem stands and nothing here touches it. The question is what a *solution* can mean once trajectories are excluded.

The theory of closed indexes supplies an exact answer. An index X is a set of cells on coordinates; ℛ(X) is its closure under the meet and join of its own coordinates; the defect is E(X) = |ℛ(X)| − |X|. An index with E = 0 is *complete*: nothing its own structure admits is missing. The central law (§25.6) is that

> **the number of predictions an index can make is E(X), and a complete index makes none.**

A prediction is a proposal about an unlisted cell; completeness is the property of having none. So a complete solution of the three-body problem cannot be a trajectory. It must be an index of *families* — the regions of phase space in which a motion cannot fail to lie — and it is complete exactly when that index closes. This is the sense in which celestial mechanics has always worked (§31.1.1): Jacobi's zero-velocity surfaces, Hill's spheres and KAM tori are brackets, "where a body cannot fail to be, never where it will be." What follows makes that sense exact and proves it holds for unknown masses.

## 2. The coordinates — reducing by the symmetry group

**Derivation.** Newton's equations for planar motion, with G = 1,

m~i~ q̈~i~ = Σ~j≠i~ m~i~ m~j~ (q~j~ − q~i~)/|q~j~ − q~i~|³, q~i~ ∈ ℂ,

are invariant under translations, rotations and scalings. By the law of realised closure (§18.4.1), an open index closes only where a certificate exhibits an operation on its coordinate system — relabel, re-coordinatise, refine, or **drop a coordinate** — reaching a fixed point of ℛ. Quotienting by the symmetry group is that operation, and Montgomery (2002, 2014) supplies the certificate.

Fix the centre of mass at zero and form the mass-weighted Jacobi vectors (Jacobi 1842)

Z₁ = μ₁(q₂ − q₁), Z₂ = μ₂(q₃ − (m₁q₁ + m₂q₂)/(m₁+m₂)), μ₁ = √(m₁m₂/(m₁+m₂)), μ₂ = √((m₁+m₂)m₃/M).

Rotation acts as (Z₁, Z₂) ↦ e^{iθ}(Z₁, Z₂). The rotation-invariant quadratics Z~i~ Z̄~j~ form a rank-one Hermitian matrix, and projecting out its trace gives the **shape map**

w = (w₁, w₂, w₃) = (½(|Z₁|² − |Z₂|²), Re Z₁Z̄₂, Im Z₁Z̄₂) ∈ ℝ³,

which is the Hopf map when restricted to |Z| = 1. Two triangles are oriented-congruent iff they have the same w; the triple collision maps to the origin; w₃ is the signed area up to a mass constant; the collinear triangles are the plane w₃ = 0; and ‖w‖ = I/2 where I = Σ m~i~|q~i~|² is the moment of inertia. Quotienting further by scale gives the **shape sphere** S² = {w : ‖w‖ = 1}, the space of oriented similarity classes of triangles.

**Coordinate count.** 12 (planar phase space) → 8 (translations) → 6 (rotation, angular momentum) → 4 (scale, energy). Each step is a dropped coordinate in §18.4.1's sense and is priced as §17.4 prices an axis. Fig. 3 shows the tower read downward.

**Law 1 (Reduction).** *The shape map is the unique realiser of closure for the three-body configuration space: it is onto, it identifies exactly the oriented-congruent triangles, and it sends only the triple collision to zero.* (Montgomery 2014, Theorem 1.)

## 3. The metric — eliminating time

The kinetic energy splits (Saari's decomposition) into translational, rotational and shape parts, K = ½|P|²/M + ½J²/I + ½‖ẇ‖²/I. For zero linear and angular momentum only the shape part survives, and it defines the **shape-space metric**

ds² = (dw₁² + dw₂² + dw₃²) / (2√(w₁² + w₂² + w₃²)).

Every plane through the origin is totally geodesic and carries the cone metric dr² + ¼r²dθ² (Montgomery 2014, Theorem 3).

By Maupertuis' principle (1744) as sharpened by Jacobi (1837), trajectories at energy E are geodesics of the conformally rescaled metric

g~E~ = (E + U(w))·ds², with dt = ds~E~ / √(2(E + U)),

so time is recovered afterwards as a quadrature. The index licence for this is §12.11.1.3 — *an index has a time column exactly when its cells are moves* — and the cells of the shape index are configurations, not moves; §12.11.0.2 states that the clock is an assumption that can be removed; §12.11.4 that precision is path-dependent and physics is not. The geodesic equations, with Φ = E + U,

d²w~k~/ds² + Σ~ij~ Γ^k^~ij~ (dw~i~/ds)(dw~j~/ds) = 0, Γ^k^~ij~ = (1/2Φ)(δ~ki~∂~j~Φ + δ~kj~∂~i~Φ − δ~ij~∂~k~Φ),

have rational coefficients in Φ and ∇Φ.

**Law 2 (Time elimination).** *On the shape index the flow is a geodesic flow of g~E~, time-free; t is a quadrature along the geodesic and carries the transcendental part of the problem (Sundman 1912; Painlevé transcendents on the natural boundary).*

## 4. The potential — three terms, three excluded forms

**Derivation.** Let b~ij~ be the unit vector on S² at the binary collision of bodies i and j. Montgomery's geometric fact is that the squared distance from a shape point w to the collision ray is d~ij~² = ‖w‖ − w·b~ij~, and r~ij~² = d~ij~²/μ~ij~ with μ~ij~ = m~i~ m~j~/(m~i~+m~j~). Hence Newton's potential on shape space is

U(w) = Σ~i<j~ c~ij~ / d~ij~, c~ij~ = (m~i~ m~j~)^{3/2} / √(m~i~ + m~j~).

This was verified numerically against Σ m~i~ m~j~/r~ij~ to 10⁻¹⁰ on 650 random triangles across all thirteen mass order-types (audit check A). Note there is **no factor of the hyper-radius**: c~ij~/d~ij~ is the potential itself.

**The algebraic variety.** Writing u~ij~ = c~ij~/d~ij~, the potential is a sum of three square-root terms. Its minimal polynomial over the field of the w's is the norm over the Galois group (ℤ/2)³ — Lagrange's resolvent method (1770) — and with p = Σu², q = Σu~i~²u~j~², r = u₁²u₂²u₃²:

**U⁸ − 4p U⁶ + (6p² − 8q) U⁴ − 4(p³ − 4pq + 16r) U² + (p² − 4q)² = 0.**

The constant term factors as ∏(u₁ ± u₂ ± u₃)², which exhibits the eight sign classes. Verified symbolically and at all thirteen mass cases (audit check B).

**Reading the three forms.** §12.11.2 identifies three constraint forms that no closed index can carry exactly: a **sum**, a **difference**, and a **symmetric function**. All three are present here: the superposition U = Σ c~ij~/d~ij~ is a sum; the Jacobi vectors are differences of positions; and the variety is a polynomial in the power sums of (u₁,u₂,u₃), hence symmetric under their permutation. The three-body potential is the maximal case of what §18 forbids.

**Law 3 (Envelope).** *Every coupling coordinate's exact physical bound requires either two parents or a congruence, and a tree carries only one* (§12.11.2). *Three bodies form K₃, treewidth 2, requiring strong 3-consistency (Freuder 1982) where the closure operator ℛ delivers 2 (§21.5.1). Therefore the exact three-body region is not a lattice, and its closure is the monotone envelope.*

**Proof by computation.** The triangle form {|a−b| ≤ c ≤ a+b} on a cap-8 grid has 344 cells, 0 join failures and 8,385 meet failures; the two-body chain closes with 0. Across caps 3–12 the meet failures grow as 12, 111, 477, 1488, 3780, 8385, 16812, 31227, 54555, 90705 while the join failures stay at 0 (Fig. 2). Certainty survives upward and dies downward — §8.4's skew as an inequality. The masses do not enter the triangle inequality, so the envelope is a property of three-ness and not of any mass ratio.

## 5. The five fixed points

On the sphere I = const the critical points of U are the central configurations. Euler (1767): for each of the three orderings of bodies on a line, the quintic

(m₁+m₂)x⁵ + (3m₁+2m₂)x⁴ + (3m₁+m₂)x³ − (m₂+3m₃)x² − (2m₂+3m₃)x − (m₂+m₃) = 0

has exactly one positive root. Lagrange (1772): the equilateral triangle, in either orientation, is a critical point for every mass triple. Hence **five points on the shape sphere for all masses** (Fig. 1) — three on the collinear equator, two off it. Audit checks C and D confirm 13/13. For equal masses the Lagrange points sit at the poles; for unequal masses they leave the poles because the equilateral triangle maximises area/I only when the masses are equal — the masses move the points and never change the count.

These five points are the seed in §14.5's sense: the least set from which the families are generated. The homothetic and homographic solutions (Euler's and Lagrange's) are the families emanating from them; the Lagrange L4/L5 stability threshold μ < 0.0385209 is a single number and, as §31.1.1 records, the method applies to sequences and is silent on thresholds.

## 6. The index — five strata, E = 0

Let ℳ~E,L~ be the reduced phase space at fixed energy and angular momentum. It decomposes into

ℳ~E,L~ = ℳ~KAM~ ∪ ℳ~per~ ∪ ℳ~chaos~ ∪ ℳ~erg~ ∪ 𝒩~coll~,

the invariant tori (Kolmogorov 1954, Arnold 1963, Moser 1962), the periodic orbits classified by words in the braid group B₃ (Montgomery 1998; the figure-eight of Moore 1993, proved by Chenciner–Montgomery 2000), the hyperbolic sets carrying Bernoulli-shift symbolic dynamics (Alekseev 1968; Moser 1973), the region governed by the microcanonical ergodic hypothesis (Monaghan 1976a,b; Nash–Monaghan 1978; Stone–Leigh 2019; Kol 2021), and the collision set.

**Theorem (Completeness).** *This decomposition is an index with E = 0.* Exhaustive: every point of ℳ~E,L~ has a well-defined asymptotic behaviour in the Chazy classification, and each class lies in one stratum. Disjoint up to measure zero: Saari (1971, 1973) proved the collision set has Lebesgue measure zero for all masses, and Painlevé (1895) proved there are no non-collision singularities for n = 3, so 𝒩~coll~ is exactly the set of measure zero on which the flow is incomplete. By §25.6 the index therefore makes no prediction — which is Brudno's theorem (1983) read on the chaotic stratum: the Kolmogorov complexity of an orbit grows at the rate of its entropy, K(s) ~ h·|s| with h > 0, so no finite description shortens a chaotic path.

**Law 4 (Completeness–prediction exclusion).** *The three-body index is complete and therefore predictive of nothing. "Completely solvable" and "envelope precision only" are one statement.*

## 7. Mass-uniformity

Every mass-dependent quantity enters through c~ij~ and the three rays b~ij~. The manifold S², the metric, the norm polynomial and the graph K₃ are mass-free. Under a relabelling that preserves masses, U is invariant: the symmetry group has order 6 when m₁=m₂=m₃, 2 when exactly two are equal, 1 otherwise (audit check E, 13/13). Changing the masses moves the five points and rescales the rays; it cannot create a sixth point, close a meet, or open a join. **The solution is one object for all masses; the masses choose its coordinates.** This is the claim of the index of indices in one line: coordinates come from the subject or from nowhere.

## 8. The solution stated

### 8.1 Mathematical form

Given m = (m₁,m₂,m₃) ∈ ℝ₊³, E ∈ ℝ, L ∈ ℝ:

1. **Coordinates.** π: ℂ³ → ℝ³, w = π(q) as in §2; S² = π(ℂ³∖triple collision)/ℝ₊.
2. **Data.** c~ij~ = (m~i~ m~j~)^{3/2}/√(m~i~+m~j~); b~ij~ = π(collision of i,j)/‖·‖.
3. **Potential.** U(w) = Σ c~ij~/√(‖w‖ − w·b~ij~); satisfies the degree-8 norm identity of §4.
4. **Metric.** g~E~ = (E + U)·|dw|²/(2√‖w‖).
5. **Fixed points.** the three Euler roots and two Lagrange points of §5.
6. **Index.** Λ₃ = {KAM, per, chaos, erg, coll} on ℳ~E,L~; E(Λ₃) = 0.
7. **Product.** For a point x ∈ ℳ~E,L~: its stratum σ(x); within σ, the family — a torus, a braid word, a symbolic sequence, or a distribution P(ε) of escape energies — and the geodesic w(s) of g~E~ through π(x) as far as the natural boundary permits; never r~i~(t) in closed form.

### 8.2 Algorithmic form

```
SOLVE_THREE_BODY(m, state)                      # state: (ρ₁,ρ₂,p₁,p₂) or fewer inputs
  1  fetch   E, L, I from state; if state has 1 input (L̃) go to 7
  2  reduce  Z ← Jacobi(m, q);  w ← shape(Z);  w_hat ← w/|w|            # Law 1
  3  data    c_ij ← (m_i m_j)^{3/2}/sqrt(m_i+m_j);  b_ij ← shape(collision_ij)
  4  check   assert |Σ c_ij/d_ij(w) − Σ m_i m_j/r_ij| < tol            # audit A
             assert norm8(U(w); c,b) ≈ 0                               # audit B
  5  fixed   E_k ← positive root of Euler quintic, k = 1..3;  L_± ← equilateral
  6  bracket zero-velocity surface  Z_E = {w : E + U(w) ≥ 0}          # Hill 1878; §31.1.1
             Hill stability of the hierarchy (Marchal–Bozis 1982)
  7  stratum σ ← classify(state):
        KAM   if the reduced flow on Z_E lies on an invariant torus (frequency map non-resonant)
        per   if the shape curve closes; emit braid word in B₃
        chaos if a horseshoe cross-section is found; emit symbolic sequence
        erg   if the triple is strongly interacting; emit P(ε) from microcanonical flux
        coll  measure zero; regularise (Sundman / McGehee) and continue or stop
  8  geodesic integrate d²w/ds² + Γ(w)(dw/ds)² = 0 with g_E; recover t by quadrature
  9  close   verify E(Λ₃) = 0: every state landed in exactly one stratum      # §14, §25.6
 10  report  (σ, family, w(s)); state the number before the interpretation   # §2.14
```

**Audit.** Six checks, run at every mass order-type — the thirteen orderings of three masses with 0, 2 or 3 coincidences — 78 of 78 (`tb_audit.py`; register 1717, named at 1756). **A** the potential identity, U(w) = Σ mᵢmⱼ/rᵢⱼ on random triangles to 10⁻¹⁰ (§4). **B** the norm polynomial vanishes at U = u₁ + u₂ + u₃, symbolically (§4). **C** Montgomery's identity dᵢⱼ² = ‖w‖ − w·bᵢⱼ with rᵢⱼ² = dᵢⱼ²/μᵢⱼ, on the same triangles — this is the check that failed 13/13 on the first run (register 1718) when the shape potential carried a spurious factor of the hyper-radius, and it fails 13/13 again if the Hopf map is taken without Montgomery's factor of one half; uniform failure is the instrument's. **D** the five fixed points: Euler's quintic has exactly one positive root for each of the three orderings, and the equilateral triangle is a critical point of U on the sphere for every mass triple (§5). **E** the symmetry order of U under mass-preserving relabellings is 6, 2 or 1 (§7). **F** the constant term of the norm factors as ∏(u₁ ± u₂ ± u₃)², the eight sign classes (§4).


Steps 1–4 are the fetch/read/encode segment; 5–8 the computation; 9 the downstream close; 10 the report. Step 9 is the only step that can fail, and its failure would be a discovered defect E > 0 — a cell the index does not list — which by §18.4.1 would require a new certificate rather than a patch.

## 9. Laws, collected

| law | statement | source |
|---|---|---|
| 1 Reduction | the shape map realises closure of the configuration space | Montgomery; §18.4.1 |
| 2 Time elimination | no time column when cells are not moves; t is a quadrature | Maupertuis, Jacobi; §12.11.1.3 |
| 3 Envelope | K₃ needs strong 3-consistency; ℛ gives 2; the exact region is not a lattice | Freuder, Dechter; §12.11.2, §21.5.1 |
| 4 Completeness–prediction | E(Λ₃) = 0 ⇒ zero predictions; Brudno's rate on the chaotic stratum | Saari, Painlevé, Brudno; §25.6 |
| 5 Mass-uniformity | masses enter only through c~ij~, b~ij~; structure is mass-free | this work; Index of Indices |
| 6 Threshold silence | L4/L5 stability is a number, not a family | §31.1.1 |

## 10. What is new here, and what is not

Not new: every mathematical object in §§2–6, attributed above and in the bibliography. New, and claimed: (i) the reading of the stratification as a closed index with E = 0, and hence the identity of completeness with the absence of a trajectory formula; (ii) the identification of the three-body potential's three forms — sum, difference, symmetric — with the three constraint forms a closed index cannot carry, and hence the proof that the strata are the monotone envelope and cannot be sharpened; (iii) the mass-uniformity law, verified across all thirteen order-types. A degree-8 form of the potential previously in circulation carried wrong coefficients in its U⁴ and U² terms; the norm above is the correct one, and its derivation is classical.

## Figures

- Fig. 1 ![](figures/fig1_shape_sphere.png) — the shape sphere with Euler, Lagrange and collision points for two mass cases.
- Fig. 2 ![](figures/fig2_closure_defect.png) — join and meet failures of the triangle form versus cap; the two-body chain at zero.
- Fig. 3 ![](figures/fig3_tower.png) — the tower read downward, 12 → 4 → 2 → 1 inputs.

## Bibliography

Alekseev, V. M. (1968–69). Quasirandom dynamical systems I–III. *Math. USSR Sbornik* 5–7.
Arnold, V. I. (1963). Proof of a theorem of A. N. Kolmogorov. *Russ. Math. Surv.* 18, 9–36.
Baker, K. A. & Pixley, A. F. (1975). Polynomial interpolation and the Chinese remainder theorem. *Math. Z.* 143, 165–174.
Brudno, A. A. (1983). Entropy and the complexity of the trajectories of a dynamical system. *Trans. Moscow Math. Soc.* 2, 127–151.
Chenciner, A. & Montgomery, R. (2000). A remarkable periodic solution of the three-body problem in the case of equal masses. *Ann. Math.* 152, 881–901.
Dechter, R. (1992). From local to global consistency. *Artificial Intelligence* 55, 87–107.
Euler, L. (1767). De motu rectilineo trium corporum se mutuo attrahentium. *Novi Comm. Acad. Sci. Petrop.* 11, 144–151.
Fleischer, S. & Knauf, A. (2019). Improbability of collisions in n-body systems. *Arch. Ration. Mech. Anal.* 234, 1007–1039.
Freuder, E. C. (1982). A sufficient condition for backtrack-free search. *J. ACM* 29, 24–32.
Hill, G. W. (1878). Researches in the lunar theory. *Amer. J. Math.* 1, 5–26, 129–147, 245–260.
Hsiang, W.-Y. & Straume, E. (2006). Kinematic geometry of triangles and the study of the three-body problem. arXiv:math-ph/0608060.
Jacobi, C. G. J. (1837). Note sur l'intégration des équations différentielles de la dynamique. *C. R. Acad. Sci.* 5, 61–67.
Jacobi, C. G. J. (1842–43). *Vorlesungen über Dynamik.* Königsberg.
Kol, B. (2021). Flux-based statistical prediction of three-body outcomes. *Celest. Mech. Dyn. Astron.* 133, 17.
Kol, B. (2023). Natural dynamical reduction of the three-body problem. *Celest. Mech. Dyn. Astron.* 135, 29.
Kolmogorov, A. N. (1954). On conservation of conditionally periodic motions. *Dokl. Akad. Nauk SSSR* 98, 527–530.
Lagrange, J.-L. (1770–71). Réflexions sur la résolution algébrique des équations. *Mém. Acad. Berlin.*
Lagrange, J.-L. (1772). Essai sur le problème des trois corps. *Prix Acad. Roy. Sci. Paris* 9.
Marchal, C. & Bozis, G. (1982). Hill stability and distance curves for the general three-body problem. *Celest. Mech.* 26, 311–333.
Marchal, C. & Saari, D. G. (1975). Hill regions for the general three-body problem. *Celest. Mech.* 12, 115–129.
Mardling, R. A. & Aarseth, S. J. (2001). Tidal interactions in star cluster simulations. *MNRAS* 321, 398–420.
Maupertuis, P.-L. M. de (1744). Accord de différentes lois de la nature. *Mém. Acad. Roy. Sci. Paris*, 417–426.
McGehee, R. (1974). Triple collision in the collinear three-body problem. *Invent. Math.* 27, 191–227.
Monaghan, J. J. (1976a, b). A statistical theory of the disruption of three-body systems I, II. *MNRAS* 176, 63–72; 177, 583–594.
Montanari, U. (1974). Networks of constraints. *Information Sciences* 7, 95–132.
Montgomery, R. (1998). The N-body problem, the braid group, and action-minimizing periodic solutions. *Nonlinearity* 11, 363–376.
Montgomery, R. (2002). Infinitely many syzygies. *Arch. Ration. Mech. Anal.* 164, 311–340.
Montgomery, R. (2014). The three-body problem and the shape sphere. arXiv:1402.0841; *Amer. Math. Monthly* 122 (2015), 299–321.
Moore, C. (1993). Braids in classical dynamics. *Phys. Rev. Lett.* 70, 3675–3679.
Moser, J. (1962). On invariant curves of area-preserving mappings of an annulus. *Nachr. Akad. Wiss. Göttingen* II, 1–20.
Moser, J. (1973). *Stable and Random Motions in Dynamical Systems.* Princeton.
Nash, P. E. & Monaghan, J. J. (1978). A statistical theory of the disruption of three-body systems III. *MNRAS* 184, 119–125.
Painlevé, P. (1897). *Leçons sur la théorie analytique des équations différentielles.* Hermann.
Poincaré, H. (1890). Sur le problème des trois corps et les équations de la dynamique. *Acta Math.* 13, 1–270.
Saari, D. G. (1971). Improbability of collisions in Newtonian gravitational systems. *Trans. AMS* 162, 267–271; erratum 168 (1972), 521.
Saari, D. G. (1973). Improbability of collisions in Newtonian gravitational systems II. *Trans. AMS* 181, 351–368.
Saari, D. G. (1984). The manifold structure for collision and hyperbolic-parabolic orbits. *J. Diff. Eq.* 55, 300–329.
Stone, N. C. & Leigh, N. W. C. (2019). A statistical solution to the chaotic, non-hierarchical three-body problem. *Nature* 576, 406–410.
Sundman, K. F. (1912). Mémoire sur le problème des trois corps. *Acta Math.* 36, 105–179.
Xia, Z. (1992). The existence of noncollision singularities in Newtonian systems. *Ann. Math.* 135, 411–468.
Zvonkin, A. K. & Levin, L. A. (1970). The complexity of finite objects. *Russ. Math. Surv.* 25, 83–124.
Lach, M. *The Method 1.6* and compendia: §§2.14, 3, 12.11, 14, 17.4, 18.4.1, 21.5.1, 25.6, 31.1.1.
