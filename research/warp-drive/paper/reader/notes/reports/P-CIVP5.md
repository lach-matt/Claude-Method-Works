# Report: proofs/P-CIVP5.md, fix round 3 (Tier 5, further dust families at the axes)

File: research/warp-drive/paper/reader/proofs/P-CIVP5.md, 1,233 lines, md5 cb809324233a1f50b9dbfb8e50e02f6a.
Previous version: 226d1eae. Delta against HEAD: +550 −544 lines, most of it rewrapping. Not committed. No chapter or
crosswalk file was edited.

The starting point was the reader's fixed copy, P-CIVP5-fix.md (minors 1–3a, 4 for lem:loc-t5-past, 6–12 applied). It
is built on P-CLD as merged first: P-CLD 39e7fd67 (its fix round, 14 placement items) on HEAD 99e16794.

## The three Majors

### Major 2 (𝔤 ≠ ∂g along Kato iterates): fixed by restructuring the iteration
- New part (d) of thm:class-kato-memory, "a part solved by integration". The unknown splits as u = (u_0, u′). The u_0
  block (the metric components) has A^μ = δ^μ_0 I, and its rows are ∂_t u_0 = Πu′.
- The *split step* replaces the linear step. It solves the u′ block with [[lem:class-kato-history]], then sets w_0 :=
  h_0(t1) + ∫Πw′.
- For a class 𝒞 of paths with (C1)–(C4), parts (a)–(c) hold with every hypothesis assumed only on 𝒞:
  - (C1) u_* ∈ 𝒞 and is compatible;
  - (C2) 𝒞 is preserved by the split step;
  - (C3) 𝒞 is closed under the limits taken;
  - (C4) every history in 𝒞 has an extension in 𝒞.
- The proof covers the existence step, the contraction, the limit, (b) and the global iteration of (c).
- In the application, 𝒞 is the set of paths with Z_(g_τ) = ∂_τ Z_g and Z_(g_a) = ∂_a Z_g:
  - (C2) comes from the split step and the third row of the wave block, which has no forcing;
  - (C4) comes from E_(t1) applied to h_g with N = k + 2, the derivative components then defined as derivatives.
- The system's first row is now taken as ∂_τ Z_g − Z_(g_τ) = 0 for every Z.
- For Z ∈ 𝒞 the metric's first derivatives are actual, so every slice of t_A carries a state in P-CLD's sense, and P-CLD's
  divergence form applies.
- The extension used in lem:loc-t5-forcing is now compatible: Stein's X_b on Z_g, its derivatives as the other metric
  components (minor 9).

### Major 1 (logarithmic loss in step (6)): fixed by P-CLD's radial form
- lem:class-leaf-tame no longer has its own seven steps. Its proof runs Steps 1–7 of P-CLD's proof of
  lem:class-leaf-differences (a) for the family W(t), with every norm integrated over t on I × Q̂, I × Q̂_n and I × Q_ρ.
  T includes ∂_t. P-CLD's Step 5 (the radial form in s, with ‖T^j η‖ ≤ 9δ² ‖T^j δs‖) handles the transverse
  derivatives.
- Six changes are listed and justified:
  - (i) Step 1: smooth approximants are G-averaged, built from a metric and its own derivatives, with radius C_S r
    (nit 2);
  - (ii) Step 4: sup bounds up to order four come from the C^5 smallness;
  - (iii) rule (P): H³ ⊂ L^∞ on the 4-dimensional boxes, used only when a factor carries a ≥ 5 derivatives, hence n ≥ 10;
  - (iv) eq:class-leaf-compose on I × Q̂, with sup |Dω| ≤ r;
  - (v) the disc-wise bounds of Steps 5 and 6 are integrated over (t, z0);
  - (vi) Step 7 and the norm comparison of Step 2.
- The constant C_n depends, for n ≥ 10, on ‖W − W̊‖_(H^(n−1)). (M1_σ) in thm:class-kato-memory (c) now allows C_σ(L)
  with L ≥ ‖u‖_(H^(σ−1)); the proof of (c) uses L := L_(σ−1). Nit 5 is applied: θ and the partition are chosen anew
  for each σ.

### Major 3 (σ, not σ²): fixed
- eq:class-leaf-tame now bounds σ_A[W]² − σ_A[W̊]².
- Every use goes through σ²:
  - lem:loc-t5-forcing bounds −½χψ_♮ξ_A σ_A² directly;
  - lem:loc-t5-residual (b) uses the σ² terms;
  - (M2) and the energy estimates use L² differences of σ from lem:class-leaf-states (c), with |σ| ≤ C.
- rem:class-kato-memory and rem:loc-t5-scope (iv) now say σ².
- No H^n bound for σ itself remains in the file.

## Other changes for P-CLD
- lem:class-leaf-arc and eq:class-leaf-arc are removed. Block A1 defines no state, bounds or arcs; it uses the definitions
  before lem:class-leaf-states.
- Every former use now cites lem:class-leaf-states (a), (b), (c) or eq:class-leaf-pointwise, with the roles of the two
  states swapped. Minors 1 and 2 are moot.

## Minors 3–15 and nits
- **Minor 3.** r_* ≤ ρ1(p)/4 follows P-CLD; δ_1 and r are uniform, and C_n depends on δ. The closure radius uses δ := δ′
  ≤ δ_1.
- **Minor 4.** In lem:loc-t5-constraints and lem:loc-t5-uniqueness the sets D are unions of the arcs of the points where
  the closure is used, with δ := δ_♮/2. The reader's text was already in lem:loc-t5-past.
- **Minor 5.** Weights κ_A replace the lateral boundaries:
  - κ_A is constant along P_A and equals 1 on 𝒯_A;
  - near the axes it is a function of U_A on the caps of the edge, so it is constant on the arcs;
  - P-CLD's (c) holds with such a weight, by its proof, which integrates leaf by leaf (stated in lem:loc-t5-constraints).
- **Minor 6.** The reader's texts were already applied.
- **Minor 9.** Applied, with the compatible extension.
- **Minor 13.** (N4) is added: no family of 𝒢 crosses both edges at a point of S_c ∩ (N_c ∖ int N_0). ε also depends on
  the C^(m_1) norm of the cut-offs χ_c.
- **Minor 14.** lem:loc-t5-jets (b) bounds the jets with a loss of five derivatives per order (C^(m_0−5j)), with the
  induction written out. m_0 = 6k + 18 ≥ k + 3 + 4j for j ≤ k + 3 covers ‖Û − Ů‖_(C^(k+3)).
- **Minor 15.**
  - 𝒦_A^♯ is built from the background's caps, so ξ_A, 𝒲 and ψ_A do not depend on the data. The data's cap-closed
    𝒦_A″ ⊂ 𝒦_A^♯ is defined in lem:loc-t5-constraints.
  - K := 2 + max sup |Ĝ̊_A^(i)|, from the background.
  - The conditions on δ_♮ are collected as (i)–(iv) where it is fixed.
  - lem:loc-t5-faces assumes ζ_A = 1 on S near the axis.
- **Nits.** 3: crosswalk lines regenerated. 4: tangency remark. 6: line wrap. 8: scope (i). Nits 1 and 7 are moot.
- **Uniqueness lemma, beyond minors 4–6.**
  - Agreement of a further family is tracked only on supp κ_A.
  - Its derivatives are bounded by Taylor's formula along the curves of P_1^A.
  - The auxiliary state W takes its metric from g_1 + χ_θ(g_2 − g_1), with its own first derivatives, and its further
    components from U_1 + χ̃_A(U_2 − U_1), χ̃_A a fixed cut-off. W has bounds that do not depend on θ.

## Placement
Old texts are whole lines at HEAD 99e16794, each occurring once there and once with P-CLD applied (checked by script).
Line numbers are HEAD's.
- **Item 1.** Block A1, only lem:class-leaf-tame, goes immediately before the heading of sec:class-axes-stability
  (81:1534), after lem:class-leaf-reference. This is clear of P-CLD's texts at 81:1371–1395.
- **Item 2.** Block A2 goes after rem:class-kato-model (81:875).
- **Item 3.** Block B goes after the last line of sec:loc-axis (83:3253), before the heading of sec:civp-axes (83:3255).
- **Item 4.** 83:735, the reader's rebased text.
- **Item 5.** rem:loc-axis-scope (ii), 83:3251–3252.
- **Item 6.** rem:class-scope, 81:1839–1840.
- **Items 7–8.** Unchanged in substance.
- **Class solutions.** Tier 4's notion is not needed; the class solution with further families is defined in thm:loc-t5.

## Crosswalk
31 tab-separated rows: 5 after rem:class-kato-model, 2 after lem:class-leaf-reference, 24 after rem:loc-axis-scope.

## Checks
Scratch merge at
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pcivp5/merge3: HEAD 99e16794,
P-CLD's 14 placement items and 16 rows, then this file's placement and 31 rows.
- `lint.py --chapters`: 62 files, 5110 labels, 0 hits.
- `assemble.py --check`: 0 problems.
- `assemble.py`, run in the scratch copy only: 0 problems. Every assembled line of the three blocks is ≤ 121 characters,
  with no bad starts. thm:loc-t5 is Theorem 53.73.
- In the file, lines are ≤ 120 characters raw and ≤ 121 with every [[…]] counted as 18. There are no backslashes and no
  pending markers.

## For the reader to check first
- The six changes of lem:class-leaf-tame's proof against P-CLD's Steps 1–7.
- Part (d) of thm:class-kato-memory and the verification of (C1)–(C4) in the paragraph *Compatible paths*.
- The weighted form of lem:class-leaf-states (c) and the cap-constant weights κ_A.
- The continuity step of lem:loc-t5-uniqueness with the family-wise auxiliary state W.
- The jet count of lem:loc-t5-jets (b).
