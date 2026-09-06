# The Three-Body Solution, Derived from The Method 1.6

**Claim to be derived.** The Gemini paper's result — "the three-body problem is completely solvable when framed as a stratified geometric and topological system" — is a theorem of The Method. Every component of the paper is an instance of a construct the book already proves, and the book states in advance both what the solution must look like and what it cannot contain.

**The number first (§2.14).** Three bodies: interaction graph K₃, 3 edges, treewidth 2. Two bodies: 1 edge, treewidth 1, a tree. ℛ reaches consistency level 2; K₃ requires strong 3-consistency (Freuder). Shortfall: exactly one level (§21.5.1). Superposition φ(a,b) = a + b breaks 400 meets where φ(a) = a breaks none (§12.11.2, register 326). The restricted problem φ = min(a,b) closes with 0 failures (§31.1, §12.11).

---

## 1. What kind of object a solution can be — §25.6, §31.1.1

The book's law: **the number of predictions an index can make is E(X), and a complete index has E(X) = 0.** A solution that is *complete* — that partitions the whole of phase space with nothing left over — therefore predicts no individual cell. It gives families.

§31.1.1 says this of celestial mechanics directly: "families, not trajectories … Jacobi's zero-velocity surfaces, Hill spheres and KAM tori are all brackets in §15's sense — where a body cannot fail to be, never where it will be."

**Derivation.** The Gemini Master Theorem
ℳ_{E,L} = ℳ_KAM ∪ ℳ_per ∪ ℳ_chaos ∪ ℳ_erg ∪ 𝒩_coll (measure-disjoint, exhaustive)
is an index of five cells with E = 0: exhaustive (nothing unlisted) and disjoint (no cell counted twice). By §25.6 it is complete and predictive of nothing — which is exactly why §5 of the paper must add the Kolmogorov clause (K(s) ≈ |s| on ℳ_chaos: no finite closed form for a chaotic path). The paper's "completely solvable" and the book's "envelope precision only" are one statement. Poincaré is untouched by both (§31.1.1; Gemini §1).

## 2. Why the strata are envelopes and not exact — §12.11.2, §12.11.3

Chapter 17 excludes two constraint forms (sums, differences); §12.11.2 adds a third (symmetric bounds). §12.11.2 then states that three bodies carry **all three at once**: a sum in the superposition, a difference in the relative position, a symmetric function in the mutual interaction — "the maximal case of what Chapter 18 forbids."

**Derivation — read the three forms off the Gemini potential.**
- *Sum*: V₀ = A₁₂/√(R²+w₁) + A₃₁/√(…) + A₂₃/√(…) — three pairwise terms superposed.
- *Difference*: Jacobi vectors ρ₁, ρ₂ are mass-weighted relative positions; w₁ = ½(‖ρ₁‖² − ‖ρ₂‖²).
- *Symmetric*: the degree-8 variety P(V₀, w, R) = 0 is written entirely in power sums S_k = Σ uᵢᵏ — a symmetric polynomial in the three reciprocal distances.

The book's dichotomy (§12.11.3): counting coordinates close exactly; coupling coordinates close as envelopes; there is no third kind. The three-body potential is a coupling object in all three excluded forms, so its exact region is not a lattice and the strata are its **monotone envelope** — KAM tori (bounding quasi-periodic motion), horseshoe Cantor sets (bounding chaos), zero-velocity surfaces (bounding reach). Every one is a bracket, and the book proved before the paper was written that nothing tighter than a bracket is available.

## 3. The quotient to the shape sphere — §18.4.1, the EM quotient

§18.4.1: an open index closes only where a certificate exhibits an operation on its coordinate system reaching a fixed point of ℛ; the admitted operations are *relabel, re-coordinatise, refine, drop a coordinate*. The Index of Indices records the electromagnetic quotient as the template for "quotient versus extension."

**Derivation.** The 18-dimensional configuration space quotiented by translations (−3), SO(3) rotations (−3), and scale ℝ⁺ (−1), with centre of mass fixed, lands on Montgomery's S². Each quotient is "drop a coordinate" in §18.4.1's sense; the shape sphere is the certificate that the index closes. Gemini §3 is the realiser of §18.4.1 applied to three bodies.

## 4. Eliminating time — §12.11.0.2, §12.11.1.3, §12.11.4

- §12.11.1.3: "An index has a time column exactly when its cells are moves."
- §12.11.0.2: "The clock is an assumption, and the assumption can be removed."
- §12.11.4: "Precision is path-dependent; physics is not."

**Derivation.** Maupertuis' principle replaces the time-parametrised flow with geodesics of the conformal metric g_{ij} = (E + V₀/R)δ_{ij}, with dt = ds/√(2Φ). The cells of the shape-space index are positions, not moves, so by §12.11.1.3 the index carries no time column; §12.11.0.2 licenses removing it; and the geodesic equations with rational Christoffel symbols Γᵏ_{ij} = (1/2Φ)(δ_{ki}∂_jΦ + δ_{kj}∂_iΦ − δ_{ij}∂_kΦ) are the path-independent physics of §12.11.4. Time is recovered afterwards as a quadrature — the transcendental part (Painlevé, hyperelliptic) the paper isolates in §5.

## 5. The three languages — Part IV, Mathematical Compendium §III

The book holds that an index is spoken in several languages, each a re-coordinatisation, and "why none is redundant" is proved object by object.

**Derivation.** Gemini §5's hierarchy is the same claim on three bodies: braid words in B₃ (order language — periodic orbits as words in σ₁, σ₂), transcendentals (arithmetic language — Painlevé/theta for t(w)), algorithmic bits (Kolmogorov — the language of what cannot be compressed). The book's title page already says it: "arithmetic, geometry and order write one quantity three ways."

## 6. The tiers are the tower, read downward — §12.11 (Λ₉…Λ₁₃), §31.1.1

The tower measures "the price of an axis, one at a time." §31.1.1 adds a limit: "the method applies to sequences and is silent on thresholds" — L4/L5 stability at μ < 0.0385209 is a single number with nothing for a bracket to act on.

**Derivation.** Gemini §6's tiers descend 12 → 4 → 2 → 1 inputs; each step drops axes and coarsens the product: full vectors → planar geodesic → braid loop → ergodic distribution. The 1-input tier (L̃ alone → P(ε), half-life) is the book's threshold regime: one number, so the output is statistical rather than a family. The 4-input planar reduced tier is the restricted problem, and §12.11 records that φ = min(a,b) closes with zero failures — the one tractable case, in both texts.

## 7. Where the deficit sits — §21.5.1

ℛ is pairwise; K₃ needs strong 3-consistency; the shortfall is one level, and "this book has exactly one genuinely ternary object, and it is the bracket": T(n−1), T(n), T(n+1), no pair determining the third.

**Derivation.** The three-body problem is the ternary object of celestial mechanics. Its solution can only be a bracket — which is what §1–§2 above showed the stratification to be. Adding the observer's reference frame as a fourth node doubles the deficit (§21.5.1), which is why the paper's full 3D tier needs 12 inputs to say anything at all.

---

## What the derivation establishes

| Gemini component | Book construct | Status |
|---|---|---|
| Master Theorem stratification | complete index, E = 0, zero predictions (§25.6) | derived |
| Strata as tori/horseshoes/surfaces | monotone envelope of three excluded forms (§12.11.2–3) | derived |
| Shape-sphere quotient | certificate of realised closure (§18.4.1) | derived |
| Maupertuis time elimination | no time column when cells aren't moves (§12.11.1.3) | derived |
| Braid / transcendental / bits | the three languages (Part IV) | derived |
| Parameter tiers 12→4→2→1 | tower priced per axis; threshold silence (§31.1.1) | derived |
| Kolmogorov incompressibility | E(X) = 0 ⇒ no prediction of an unlisted cell (§25.6) | derived |
| Poincaré non-integrability | "nothing here touches Poincaré" (§31.1.1) | agreed, both texts |

**Conclusion.** The Gemini paper is The Method's Chapter 31 run to completion on three bodies. "Completely solvable" means: the index of families closes at E = 0, and closure at E = 0 is the same fact as the absence of a trajectory formula. The book proves the shape of the solution; the paper supplies its coordinates.

**Flags for audit (not yet run).** (i) Gemini's D₃₁, C₃₁ coefficients and the degree-8 polynomial are stated, not derived — a D2 check (second route) is owed. (ii) The claim "unique, measure-disjoint stratification" needs 𝒩_coll to be measure zero; Saari's conjecture status should be cited. (iii) The Gemini attribution table omits Moeckel and Chenciner–Montgomery (2000) for the figure-eight braid; audit 7 ATTRIBUTION applies.
