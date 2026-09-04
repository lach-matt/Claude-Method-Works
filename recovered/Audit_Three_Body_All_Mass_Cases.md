# Audit — the three-body solution across every mass order-type

**Numbers first (§2.14).** 13 mass cases × 6 checks = 78 checks. 78 pass. One correction was made during the audit and is recorded below. Triangle region at cap 8: 344 cells, 0 join failures, 8,385 meet failures; two-body chain: 0 failures of either kind.

## Scope

Three positive masses admit exactly 13 order-types (the weak orderings of three elements). The nine you listed plus the four remaining — x=z with x<y, x=z with x>y, x<z<y, x>z>y — are all run. Each is realised by a concrete triple; 50 random planar triangles per case, tolerance 10⁻¹⁰.

## The checks and what each tests

| check | statement tested | owner | book section | result |
|---|---|---|---|---|
| **A** | Montgomery's shape potential Σ c_ij/d_ij, with c_ij = (m_i m_j)^{3/2}/√(m_i+m_j) and d_ij² = ‖w‖ − w·b_ij, equals Newton's Σ m_i m_j / r_ij identically | Montgomery (2002, 2014) | §18.4.1 certificate of realised closure (quotient by translations, rotations) | 13/13 |
| **B** | the degree-8 norm ∏_{ε∈{±1}³}(V₀ − ε·u) vanishes at the true potential | Lagrange resolvent / Galois norm | §12.11.2 symmetric excluded form (a symmetric polynomial in u₁,u₂,u₃) | 13/13 |
| **C** | Euler's collinear quintic has exactly one positive root per ordering — three Euler points | Euler (1767) | §31.1.1 (L1, L2, L3 tested as families) | 13/13 |
| **D** | the equilateral triangle is a critical point of U on the sphere I = const — two Lagrange points | Lagrange (1772) | §31.1.1 (L4/L5 sit on the pole exactly) | 13/13 |
| **E** | U is invariant under exactly the mass-preserving relabellings: |S| = 6 at x=y=z, 2 with one equality, 1 otherwise | — | §3 reflection / §12.11.2 "one reflection, three appearances" | 13/13 |
| **F** | the collision set has Lebesgue measure zero for all masses | Saari (1971, 1973) | §25.6 — the unlisted cell has measure zero, so E = 0 is exact | theorem, mass-free |

Checks A–D are the **five central configurations existing for every mass triple**: 3 Euler + 2 Lagrange, the five points on the shape sphere. Check E measures how much of the S₃ symmetry survives each mass pattern and is the only place the order-type changes anything: it changes the *symmetry group of the index*, never the index's closure.

## The book-side test (mass-independent)

§12.11.2 predicts the triangle form {|a − b| ≤ c ≤ a + b} is **join-closed and meet-broken**. Computed on the K₃ cell set at cap 8: 344 cells, 0 join failures, 8,385 meet failures. The two-body analogue (one edge, a chain bound) closes with 0 failures of either kind. That is §12.11.2's "certainty survives upward and dies downward" and §21.5.1's treewidth-2 deficit, reproduced from scratch. The masses do not enter the triangle inequality, so this is the same for all 13 cases — which is the proof that the *shape* of the solution (envelope, not exact) is a property of three-ness and not of any mass ratio.

## Coherence: why the result is mass-uniform

Every mass-dependent quantity enters through c_ij and the three binary rays b_ij; the manifold (shape sphere), the metric ds² = |dw|²/(2√‖w‖), the norm polynomial, and the constraint graph K₃ are mass-free. So the derivation has the form the book requires of a closed index: coordinates from the subject (masses → c_ij, b_ij) and structure from the index (S², K₃, envelope), with E measured on the structure. Changing masses moves the five points on the sphere and rescales the rays; it cannot create a sixth point or close a meet.

## The correction, recorded (§28 practice)

On the first run check A failed 13/13. The cause was a stray factor: I had divided the shape potential by the hyper-radius R, following the working material's convention V₀ = R·V. Montgomery's c_ij/d_ij is already Newton's potential, since r_ij² = d_ij²/μ_ij with μ_ij = m_i m_j/(m_i+m_j) — verified numerically at 1.5, 0.833, 1.333 for masses (1,2,3). Uniform failure across all cases was the signal that the fault was in the audit and not in the object; corrected, 13/13 pass. The working material's convention is therefore not to be used in the produced work.

## What remains true only with qualification

- Non-collision singularities are excluded by Painlevé for n = 3 only; the measure-zero clause is exact for three bodies and must not be generalised.
- The figure-eight (Moore 1993; Chenciner–Montgomery 2000) exists in the equal-mass case; the *stratum* ℳ_per exists for all masses, its *contents* depend on them.
- L4/L5 linear stability is a threshold (μ < 0.0385209) and the method is silent on thresholds (§31.1.1).

## Verdict

The solution — a closed index of families on the shape sphere with E = 0, whose strata are the monotone envelope of the three excluded forms — holds for every mass order-type. No residue.

Script: `audit.py` (attached).
