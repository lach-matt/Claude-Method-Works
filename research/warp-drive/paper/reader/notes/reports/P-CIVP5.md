# Report: proofs/P-CIVP5.md, round 2 (Tier 5, further dust families at the axes)

File: research/warp-drive/paper/reader/proofs/P-CIVP5.md, 1,227 lines, md5 226d1eae5f915d229723114e4b63121b.
Not committed. No chapter or crosswalk file edited.

## The theorem (thm:loc-t5)
Hypotheses: Tier 3's (k ≥ 9, m_0 = 6k + 18, m_1 = 12k + 42, background on Q1 with margin δ_1, cone data through
the axes, normalised gauge, nonnegative densities), plus any number of further families (def:loc-t5-family) with:
- (F-a) no density near the corner circles S_c ∩ axis i;
- (F-b) density only where the family crosses the edge;
- (F-c) corner compatibility;
- fixed neighbourhoods 𝒦_A′ of the supports.
The exclusions and their reasons are written into the statement. (F-b) is backed by prop:loc-t5-grazing, (F-a) by
lem:loc-t5-tubes.

Conclusions match Tier 3:
- (a) a class solution with the further families on Q1 × S³, smooth through the axes;
- (b) a Cε estimate in C^(k−4);
- (c) uniqueness on every Q1′ ⊂ Q1 among solutions within ε_2 in C^(k−4);
- (d) localisation.
For N_f = 2 it is thm:loc-axis.

## Smoothness (item 2): the tame estimate route
Tier 5 now has Tier 3's regularity, a smooth solution.
- lem:class-leaf-tame (Block A1) gives a linear bound in every H^n, in space-time, on C^5-small balls.
- Part (c) of thm:class-kato-memory (Block A2) proves persistence of all H^σ norms by a global iteration from u_*.
  It needs R = 0 on the history interval and the hypothesis (M1_σ).
- lem:loc-t5-forcing proves (M1_σ) from the tame lemma. lem:loc-t5-existence concludes smoothness.

## lem:class-leaf-tame (item 4)
The proof is written in full in seven steps and does not use the proof of lem:class-leaf-differences:
1. divergence form of the leaf equation, (D), and its fixed point along the arcs, (V);
2. the planar shear as a smooth function 𝔖 with no division by |y|;
3. a box in the leaf coordinates (t, z0, y) and Hardy's inequality (H);
4. C² bounds (L);
5. a tame composition estimate (C), proved from the Gagliardo–Nirenberg inequality inside the proof of
   lem:class-composition (a), Hölder's inequality and Stein's extension (thm:std-sy-extension);
6. induction on the order;
7. conclusion.

I replaced the past-set version I had drafted with this product-box version. The extension E_b handles times beyond
t2, as F at a time depends only on the past.

## Tier 3 citations (item 1)
All 16 pending markers are gone; none remain. Citations are to the merged chapter 83 at HEAD.

| Former marker | Now cites |
|---|---|
| t3-setting | sec:loc-axis-reduced, eq:loc-axis-time, eq:loc-axis-region, lem:loc-axis-system (a)–(e), eq:loc-cone-modified (F̃ := (1 − θ1_F)𝔄_χ(Û)), sec:loc-cone-reduced (Δ vanishes for τ0 ≤ ln(9δ_c²/16)) |
| t3-cone-data | lem:loc-axis-constraints (a)–(c), with the further sources added |
| t3-jets / t3-residual | lem:loc-axis-jets (a)–(c), lem:loc-axis-system (d) |
| t3-leaf-criterion | lem:loc-axis-leaf (ii), (iii) |
| t3-gauge | lem:loc-axis-gauge, applied with 𝒯 = F ∩ {τ ≤ s*} in place of 𝔗(s*) |
| t3-wave-map | steps (1)–(4) of the proof of lem:loc-axis-unique, with lem:loc-t5-uniqueness in place of lem:loc-axis-dependence |
| t3-theorem | thm:loc-axis and def:loc-axis-data |

Also used:
- lem:loc-axis-propagation (phases paragraph);
- lem:loc-axis-past;
- lem:loc-axis-energy;
- the paragraphs *The equations* and *Continuity in t* of lem:loc-axis-dependence, including its fixed Taylor bound
  Cθ^(k+1).

What Tier 3 does not supply, and the file proves:
- **Uniqueness with further families.** Tier 3's Lemma R needs the slice spheres to be leaves of every family. This
  fails for further families, and their arcs can leave R′ through the future null faces, which they may be tangent to.
  The new lem:loc-t5-uniqueness exhausts R′ by triangles T_N := F ∩ {τ^N ≤ 1}, with a bent time built from
  Φ_N = (ũ/a)^N + (ṽ/b)^N + (ũ + ṽ)/(N(a + b)). On each T_N it argues by continuity in τ^N, as Tier 3 does, so the
  slices need only be spacelike for W near the set where the two solutions agree. No smallness is assumed.
- **An integrated energy lemma** (lem:loc-t5-energy).
- **The edge-section leaf lemma for crossing families** (lem:loc-t5-faces).
- **Constraint propagation** on the tubes (lem:loc-t5-constraints).
- **A closure radius δ_♮.** It is fixed after the bend scale δ_* and after the leaf and tame constants in the bent
  charts. This removes a circularity, since the constants depend on δ_* through third derivatives of the bend.

## Derivative counts (k ≥ 9)
- k ≥ 9 gives C^5 control by ⟦Z⟧_k (k − 5 > 2), which is the smallness the tame lemma needs.
- The estimate is C^(k−4), from Ψ − id in C^(k−3), as in Tier 3.
- Uniqueness assumes ε_2-closeness in C^(k−4), as in Tier 3.
- Data are in C^(m_1); the extension goes to C^(m_0) by lem:loc-axis-constraints (c), with q_A's Borel extension cut
  off in v (or u) so that (F-a) and (F-b) persist.

## Grazing families (item 3): excluded, reason proved
prop:loc-t5-grazing proves three things for a family that is tangent to an edge at an axis:
- (a) The edge is characteristic for it along the axis generator: ∂_uU_A = 0 there, and the coefficient of ∂_vu_A in
  the eikonal equation vanishes.
- (b) Suppose the restriction of U_A − U_A(x_0) to an edge section vanishes to finite order 2j (j = 1 when
  ½∂²_ϑU_A ≠ 0). Then the level set through the axis point lies strictly on one side of the edge, and points on that
  side arbitrarily near x_0 have arcs that start on the other side. So the energy estimate on P or on F fails in any
  slicing.
- (c) If all edge sections are leaves, U_A is locally constant on the edge and the rays run in it.

One case is stated as not analysed: vanishing to infinite order without vanishing nearby. (F-b) excludes all of these.

prop:loc-t5-cut (statement W) gives, for families violating (F-a)/(F-b), a development on D′ = F ∩ {λ ≤ 0} (λ a time
function, {λ = 0} away from the axes, D′ ∩ N_c = ∅) and proves it independent of the cut χ_c. It does not give
uniqueness among other solutions on D′; rem:loc-t5-scope (i) says so. This replaces round 1's uniqueness claim, which
needed an extension step that does not work on non-rectangular D′.

## Placement
- **Block A1:** after rem:class-leaf-numerics (81:1367), after Tier 4's lem:class-leaf-reference if present, before
  sec:class-axes-stability.
- **Block A2:** after rem:class-kato-model (81:875), before sec:class-off-axes.
- **Block B:** immediately after the last line of sec:loc-axis (83:3246). It goes before "### Developments of data of
  any size through the axes {#sec:civp-axes}" if Tier 4 is merged, otherwise before sec:loc-shells (83:3248).
- **Old/new pairs, all whole lines at HEAD:**
  - item 4 replaces only line 83:728, inserting the further-families sentences before "No development is". It states
    only what this section adds and composes with the shared sentence.
  - item 5 is rem:loc-axis-scope (ii), 83:3244–3245, with a pointer to sec:loc-t5.
  - item 6 is rem:class-scope, 81:1674–1675.
- **Unchanged:** chapters 03 and 90 (90:183 concerns the Cauchy problem). No Appendix A entry is needed.
- **Class-solution notion:** the further-families notion is defined in thm:loc-t5 from def:loc-axis-data. Tier 4's
  broader notion is not needed.

## Crosswalk
33 tab-separated rows (4 fields), in chapter order:
- 5 for 81 after rem:class-kato-model;
- 4 for 81 after rem:class-leaf-numerics;
- 24 for 83 after rem:loc-axis-scope.

## Checks
Scratch merge at
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pcivp5/merge2: chapters/ and
crosswalk/ at HEAD a03de14d (Tiers 1–3 and shells merged), plus Blocks A1, A2, B, items 4–6 and the rows. Results:
- `python3 lint.py --chapters`: 0 hits, 4917 labels;
- `python3 assemble.py --check`: 0 problems.

Lines are ≤ 120 characters raw, and ≤ 121 with every [[…]] counted as 18 characters. No bad line starts, no backslashes,
lowercase labels, and no file or program names in the paper text.

## For the reader to check first
- Step (5) of lem:class-leaf-tame (the composition estimate) and step (6) (the induction).
- The order of choice of constants: K, δ_*, the leaf and tame constants in the bent charts, δ_♮, ρ, ε.
- lem:loc-t5-uniqueness: the slab argument on T_N.
- prop:loc-t5-grazing (b).
