# P-CIVP3: Tier 3 of the characteristic problem (cone data through the axes)

File written: `/home/user/Claude-Method-Works/research/warp-drive/paper/reader/proofs/P-CIVP3.md`
(1,126 lines, md5 1d196fae6ed5c92557721eb8dadfd294). The section text is lines 1–833 (31 labels); the Placement
section starts at line 835 and the crosswalk rows at "### Crosswalk rows". I edited no chapter, crosswalk, Tier 1 or
Tier 2 file and committed nothing. A tab-separated copy of the 31 new crosswalk rows is at
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pcivp3-crosswalk.tsv`.

## The theorem as stated (thm:loc-axis)

Let k ≥ 9, m_0 = 6k + 18 and m_1 = 12k + 42. Take a background on Q1 = [0, u_1] × [0, v_1] with margin δ_1 (a round
two-dust solution on Q^♯ = [−δ_1, u_1 + 2δ_1] × [−δ_1, v_1 + 2δ_1]). Take cone data through the axes on
{0} × [0, v_1] and [0, u_1] × {0}: fields ln Ω, γ and b smooth through the axes as tensors on S³, in the normalised
gauge, with nonnegative densities. Let ε be their size in C^(m_1). Then there are ε_0, C and ε_2 depending only on k,
u_1, v_1, δ_1 and the background such that, for ε ≤ ε_0:

- (a) there is a class solution in the double-null gauge through the axes on Q1 × S³ that induces the data, with phases
  v and u, smooth with the axes included;
- (b) its fields and densities are within Cε of the background's in C^(k−4);
- (c) on every Q1′ ⊂ Q1 it is unique among class solutions in that gauge that induce the data and whose fields are
  ε_2-close in C^(k−4);
- (d) localisation: where the data equal the background's on {0} × [0, v_K) and [0, u_K) × {0}, the solution equals
  the background on u < u_K, v < v_K. Where the data equal the background's at ϑ < ϑ_a′ ≤ π/4, the solution does too
  at ϑ < ϑ_a′ − 2C_*(uv)^(1/2), and symmetrically at the other axis.

cor:loc-axis-cones applies the theorem to the chapter's background on [0, 7.2] × [0, 4.5]. It takes free data within ε
in C^(m_1 + 3) and allows the shell and the packet to be perturbed at once, with densities on either cone and the axes
included. lem:loc-axis-rectangle proves in writing that this rectangle lies in G with R ≥ 1.5 and R_v > 0. Its numbers
are |R_u(7.2, 0)| ≤ 0.84778, f ≥ 0.63461, R_v(7.2, 0) ≥ 0.18713, R(7.2, 3) ≥ 2.0613, μ ≤ 3.6059 and f > 0.15
through the shell.

## What is proved

Every statement is proved in full. The lemmas, in order:

- **def:loc-axis-data and lem:loc-axis-constraints.** The constraints are linear ODEs in tensorial form (Y, γ̂, W), so
  they are smooth through the axes. The data are extended beyond u_1 and v_1 by Borel sums.
- **lem:loc-axis-jets (T3-0).** The transverse jets are written as tensors on S³. The derivatives across N_o and N_i
  solve linear ODEs whose coefficients are smooth through the axes. This gives Ĝ, Û and Δ, with ‖Δ‖_(C^(k+3)) ≤ Cε.
- **lem:loc-axis-leaf (Lemma A).** (i) Any time that increases with u and with v meets each face in at most one data
  sphere; this includes t = u + v. (ii) In the actual chart: a G-invariant hypersurface on which p_A vanishes is a leaf
  exactly when Θ_A equals its expansion. (iii) A curve is a leaf of one state exactly when it is a leaf of another
  state with the same p_A, Θ_A, metric and first derivatives along it. For Ů and Û the spheres are the leaves of both
  families.
- **lem:loc-axis-shear (T3-2).** This is lem:class-leaf-differences (b) proved leaf by leaf. It holds on any set O such
  that, for each point of O near the axis, the arc of the first state's leaf from the axis to that point lies in the
  closure of O. The constant does not depend on O (Hardy average of prop:class-flat-model (b)).
- **The reduced problem.** The chart time is adapted to Q1 (eq:loc-axis-time). The slice-triangles 𝔗(s) contain Q1
  and meet the cones only where the data are given. The closure eq:loc-axis-closure covers both families with no
  cut-off at the axes.
- **lem:loc-axis-system.** (F1)–(F3) hold on 𝒟_ρ.
- **lem:loc-axis-energy.** The energy estimate with a non-local term.
- **lem:loc-axis-cauchy.** Kato's theorem holds on the whole interval.
- **lem:loc-axis-past.** U = Û to the past of the cones.
- **lem:loc-axis-propagation.** The constraints propagate on 𝔗(s*) ⊃ Q1, the axes included.
- **lem:loc-axis-gauge.** The double-null gauge through the axes.
- **lem:loc-axis-dependence (Lemma R).** Two solutions in one wave gauge that agree to all orders on the past faces of a
  double-null rectangle agree on it, with no smallness. The proof uses continuity in t = ũ + ṽ, the chart
  x = e^(ṽ−μũ) ω̃ with 4μΩ² > γ(b, b), and a localised comparison state W.
- **lem:loc-axis-unique.** Uniqueness in the double-null gauge: extension of the competitor, a wave map, then Lemma R.
- **lem:loc-axis-angle.** Angular localisation.
- **Proof of the theorem.**
- **rem:loc-axis-constants.** Says where smallness enters (three places) and that the leaf constants depend only on
  the ball about Û and the chart.
- **rem:loc-axis-scope.** What the theorem does not give: large data at the axes, further families, finite regularity.

## Pending markers and needs

There are **no pending markers** in the file and no outstanding needs from other tiers.

**Tier 1 labels cited** (25, as they stand now):
- thm:loc-cone-development, rem:loc-cone-scope, sec:loc-cone-reduced, sec:loc-cone-setting
- eq:loc-cone-collar, eq:loc-cone-domain, def:loc-cone-data, lem:loc-cone-in, eq:loc-cone-in
- lem:loc-cone-extension, lem:loc-cone-borel, lem:loc-cone-jets, prop:loc-cone-formal
- lem:loc-cone-ricci, eq:loc-cone-frame-ricci, eq:loc-cone-time, eq:loc-cone-modified
- lem:loc-cone-system, lem:loc-cone-energy, lem:loc-cone-past, lem:loc-cone-constraints
- lem:loc-cone-gauge, lem:loc-cone-unique, lem:loc-cone-support, lem:loc-cone-strips

The Placement also names sec:loc-cone-proof and rem:loc-cone-local-scope.

**Tier 2 labels cited:** thm:civp-large in the section text. The Placement also names def:civp-large-data,
rem:civp-large-domain and rem:civp-large-beyond.

**Renames.** The coordinator's rename list is still to come and I will apply it when it arrives. Tier 1's symbol
renames (η → ϖ, ε_0 → ε_B, a_0 → λ_e) do not touch this file:
- The ε_0 here is this theorem's own constant.
- The a_j here are the jets of lem:loc-cone-jets, which Tier 1 still writes a_j.
- I use u_1 and v_1 for the sides of Q1, which matches Tier 1 and Tier 2's rename u1 → u_1 (its minor 3).

## Departures from the GN-T3 outline, with reasons

1. **T3-2 is one leaf-wise lemma, not an extension version (a) plus a leaf-wise version (b).** The estimate only needs
   the first state's leaves to be closed under arcs from the axis; the second state's leaves need no closure. That
   one-sided condition covers every use: the past region, whose slices are spheres (the leaves of Û); the
   slice-triangle, bounded by two leaves of U; the angular region, whose slices contain the arcs of the background's
   spheres; and Lemma R. So the extension version is not needed. It is written leaf by leaf with a constant independent
   of the set, as asked.
2. **GN3 forcing smoothness, including the corner case, is not needed as an O(d^∞) argument.** In the slices of any
   time that increases with u and v, the leaves of Û are exactly the coordinate spheres (lem:loc-axis-leaf (iii)). So
   σ_A[Û] is a smooth local function of the 1-jet of Ĝ, and the closure residual of Û is −E(P̂, P̂), which is local
   and vanishes to infinite order on N (lem:loc-axis-system (d), (e)). The corner case is therefore moot.
3. **Item (4), the chart time.** τ = ln((u+δ_c)(v+δ_c)) + M(β((u−u_1)/δ_1) + β((v−v_1)/δ_1)). With it, 𝔗(s*)
   contains Q1 but meets the cones only on the given data and their extension (lem:loc-axis-constraints (c),
   m_1 = 2m_0 + 6).
4. **k ≥ 9 and uniqueness in C^(k−4).** Tier 1 has k ≥ 6. The uniqueness lemma's wave-map step runs at s = k − 5 > 3
   with the competitor's fields in C^(k−4), the same norm as the estimate (b). Uniqueness also no longer lets the
   rectangle grow: the competitor is extended across the far faces by the operator of thm:std-ly-extension (i) in one
   variable, so ε_2 does not depend on Q1′.
5. **Lemma A, statement (ii).** It assumes that p_A vanishes on the hypersurface and characterises leaves by Θ_A = θ_S.
   The converse, that a leaf is annihilated by p_A, is false for a general state and is never used. Where a level set
   has to be a leaf (the propagation lemma, Lemma R), this is argued through (ii), using nullness of the phase on an
   open set.
6. **Lemma R** is proved by continuity in t with no smallness, as S-T4 §4.5 asks. It is stated for two states in one
   wave gauge relative to an arbitrary metric Ĝ′.
7. **Angular localisation is restricted to ϑ_a′ ≤ π/4 (and ϑ_b′ ≥ π/4).** This way each region meets one axis only.
   The (uv)^(1/2) form comes from an auxiliary δ′ → 0 inside one fixed construction. Letting δ_c → 0 instead, as an
   earlier draft did, would have been wrong, because ε_0 depends on δ_c.
8. **Item (5).** Only the two double-null families are treated (rem:loc-axis-scope (ii)). Further families reaching the
   axes are left to Tier 5.
9. **Constants are traced.** rem:loc-axis-constants lists them, including the dependence on the size of Û through
   ‖Δ‖_(C^(k+3)).

## Placement (summary)

The section goes into chapter 83 right after the Tier 2 section, before sec:loc-kid. The merged texts replace Tier 1's
items 3, 4, 6 and 7, together with the corresponding Tier 2 items:
- items 2 and 3: chapter 83's opening paragraph and the paragraph after prop:loc-cones;
- item 9: chapter 03, "More families";
- item 10: chapter 90, the localised-data paragraph.

The other items:
- **Items 4 and 5:** rem:loc-cone-scope (ii) and (iv) inside Tier 1's Block A. Its sentence that no domain-of-dependence
  statement near an axis is proved is now false for double-null rectangles.
- **Item 6:** the last sentence of rem:loc-cone-local-scope.
- **Item 7:** a sentence appended to Tier 2's rem:civp-large-domain. It is an append, not an old/new pair, because that
  remark is being revised.
- **Item 8:** chapter 81, lem:class-leaf-differences. The new definitional clause reads H_L[Θ_A] with p_A(n) and with
  the plane fixed by p_A. No statement of chapter 81 changes.
- **Item 11, unchanged:** chapter 01 (Tier 1's item 5 suffices), chapter 87 and chapter 90's sentences on 10 l5.
  lem:tl5-continuation's (F2) is not given by this section.
- **Item 12:** no Appendix A entry and no reference.
- **Item 13:** what changes if Tier 2 is not merged.
- **Crosswalk:** 31 new chapter-83 rows, plus note and source additions for chapter 81's lem:class-leaf-differences row
  and for the three amended remarks' rows.

**Caveat.** The old texts in items 4–6 quote Tier 1 as it stands now. The merged new texts in items 2, 3, 9 and 10 are
built on Tier 1's current new texts. If Tier 1's fix round or Tier 2's wiring round changes those texts, these items
must be re-merged.

## Check outputs

On a scratch copy (`.../scratchpad/pcivp3/`), I inserted Tier 1's Block A and Block B, the Tier 2 section with its
Appendix A entries, and this section, and applied placement items 2–10.

- `python3 lint.py --chapters` printed `chapters: 62 file(s), 4764 label(s) defined, 10 hit(s)`. All 10 hits are Tier
  2's `[[pending:civp-tier1-*]]` markers; none comes from this section or from my placement texts.
- `python3 assemble.py --check` printed `labels 4764, computations cited 0, problems 0`. One intermediate run showed 7
  undefined-label problems in chapter 33. They came from another task's edit in progress and were gone on the rerun.
- A resolved-length check (labels replaced by their assembled numbers) over all changed lines found no line over 121
  characters before or after resolution, no wrapped line starting with "+ ", "- ", "* ", "> ", "#", "=" or "|", no
  backslash and no unresolved reference.
