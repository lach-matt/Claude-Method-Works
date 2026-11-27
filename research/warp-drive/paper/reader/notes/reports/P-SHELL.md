# P-SHELL: leaf-aligned null shells for the characteristic problem of chapter 83

Output: `research/warp-drive/paper/reader/proofs/P-SHELL.md` (759 lines). The section `### Null shells along the leaves
{#sec:loc-shells}` is about 630 chapter lines. It is followed by a Placement section with 8 items and by 19 crosswalk
rows, tab-separated. No chapter or crosswalk file was edited, and nothing was committed.

## What is stated and proved

- **def:loc-shell-solution.** A solution with null shells along finitely many leaves {v = c_k}, {u = d_j}:
  - the metric is continuous and cellwise smooth in the gauge eq:loc-double-null;
  - Ric is taken in the sense of distributions, in every chart (u, v, y);
  - the source is T = (q_in + Σ 𝔪_k δ(v − c_k)) dv² + (q_out + Σ 𝔫_j δ(u − d_j)) du²;
  - the dust laws hold in divergence form.
- **lem:loc-shell-ricci (full proof).** The δ-part of Ric across a null leaf, in invariant form:
  - 𝒮 = ½(dv⊗Y + Y⊗dv) − ½(tr h) dv⊗dv, with h = [∂_v g];
  - in the gauge, 𝒮_k = −[tr χ] dv² + (γ_ϑ[∂_v b]/(4Ω²))(dv⊗(dϑ − b du) + sym.) and 𝒮′_j = −[tr χ̲] du².
- **lem:loc-shell-identities.** Two identities read off from Tier 1's lem:loc-cone-ricci:
  - Ric(L̲, ∂_ϑ);
  - an exact angular-trace identity eq:loc-shell-trace, whose remainder 𝔞 contains only ϑ-derivatives (round check:
    𝔞 = 6/R², which recovers (R³)_uv = −3Re^(2σ)).
- **prop:loc-shell-junction (full proof).**
  - (a) [∂_v b] obeys a homogeneous transport equation along L̲, and is continuous through crossings.
  - (b) If [∂_v b] = 0, then 𝒱[tr χ] obeys the null-dust conservation law.
  - (c) ∂_v(𝒱[tr χ̲]) = 0 always.
  - (d) Necessary and sufficient junction conditions for the distributional equations: (J1) [∂_v b] = 0; (J2) the
    densities are −[tr χ] and −[tr χ̲]; (J3) the transverse densities are continuous.
  - No condition is placed on [∂_u b], on the jumps of ∂ ln Ω, or on the shear.
- **rem:loc-shell-poisson.** Comparison with [Poi02], which I read: p. 1, and (2.15) on p. 4. No proof uses it.
- **def:loc-shell-data** and **prop:loc-shell-cones** (S-T6's MV-2): free data with atoms.
  - [∂_vϕ] = −m_k/3 at each atom.
  - ∂_v b is automatically continuous.
- **thm:loc-shells.** The data are cone data with shells, around g0; no smallness is assumed.
  - (a) Existence on 𝒮_δ = {min(u, v) ≤ δ}, with δ < min(c_1, d_1), so no two shells cross there.
  - (b) Localisation in bands widened by ½ min(ϑ_a, π/2 − ϑ_b) at each restart.
  - (c) Uniqueness among solutions with shells along the same leaves that equal g0 near the axes.
  - (d) Small data: a domain 𝒮_w whose width depends only on g0, u_1, v_1, the leaves and the band, and a Cε estimate
    in C¹ on every cell. This uses the index cascade k_(i−1) = 6k_i + 23 and needs pieces of the free data that extend.
  - Proof: slab by slab, with a change of angle that makes b = 0 on each restart face, glued by the junction proposition.
- **prop:loc-shell-crossing.**
  - (a) Crossing rule (tr χ tr χ̲)_(++)(tr χ tr χ̲)_(−−) = (tr χ tr χ̲)_(+−)(tr χ tr χ̲)_(−+) for every solution. For round
    metrics it reads f_(++)f_(−−) = f_(+−)f_(−+), that is (R² − μ_(++))(R² − μ_(−−)) = (R² − μ_(+−))(R² − μ_(−+)). Mass
    jumps are given too.
  - (b) Round continuation through a crossing sphere on a small square, by a contraction argument on the Volterra system
    of prop:two-dust-background. Unique among round solutions.
  - (c) Continuation off the axes on a small square, by Tier 1's prop:loc-cone-local. Existence and uniqueness on a
    neighbourhood of both leaves under (T2).
  - (d) At an axis: the identities and the junction conditions hold by continuity. No continuation is asserted when the
    shells are non-round at an axis.
- **rem:loc-shell-scope.** What remains open, listed below.

## Pending markers

Both are stated in full in the paragraph "*The smooth theorems at other corners.*":

- **[[pending:civp-large-at-a-corner]] (T2).** thm:civp-large (a)–(c) at any rectangle [u_c, u′] × [v_c, v′] ⊂ Q1:
  - its corner sphere, its edges and its past sets take the place of S, the cones and the past sets of Q1;
  - 𝒮_δ becomes {min(u − u_c, v − v_c) ≤ δ}.
  - P-CIVP2's proof uses of g0 only that it is a smooth round class solution with b = 0, and its corner step already
    handles arbitrary corners. Used by thm:loc-shells (a)–(c) and by prop:loc-shell-crossing (c).
- **[[pending:loc-cone-development-at-a-corner]] (T1).** thm:loc-cone-development (a)–(c) at corners (0, c) or (d, 0):
  - cone data in the sense of def:loc-cone-data, with b = 0 on N_i and any Ω;
  - domain {(u − u_c)(v − v_c) ≤ δ_*²}, with δ_* independent of the data;
  - this is case (I) of sec:loc-cone-reduced at that corner, but there it is phrased with C_* := C_0, the chapter's
    background at S.
  - Used only by thm:loc-shells (d).

## Open (rem:loc-shell-scope)

- General measures, non-leaf shells, and accumulating shells.
- Developments past crossings beyond small squares; a development on all of Q1.
- Perturbations of a round background that itself carries shells. This is GM-3: Tier 1 and Tier 2 around a background
  that is smooth only on a closed cell.
- Shells that are non-round at an axis.
- Uniqueness in weaker classes.
- Limits of densities that concentrate on a leaf.

A global round development with atomic profiles is not written. Only the local crossing continuation is.

## Deviations from S-T6 and things to know

- **Notation.** The section is written in chapter 83's gauge. S-T6's μ = −(3/R)[∂_vR] is −[tr χ] here; the shell
  densities are named 𝔪_k and 𝔫_j because μ is the mass function.
- **MV-3 checkerboard.** I did not claim it inside the neighbourhood of the cones. The smooth theorems give
  neighbourhoods of edges, not whole rectangles, so crossings are handled locally.
- **Dependence on Tier 1.** The proofs rely on Tier 1's formulas in lem:loc-cone-ricci. I checked all its components
  independently with sympy (private: `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pshell/ca/ricci83.py`, `singular.py`), and checked the
  trace identity and the 𝔞 in the text the same way. P-CIVP was being edited while I worked; I used its labels as they
  stood at 19:07 UTC.
- **References.** [Poi02] is a new reference, cited as the arXiv preprint v1; I could not confirm a journal version.
  Barrabès–Israel is named only through Poisson's title, and is not cited.
- **No code in the text.** No program, computation or file name appears in the section.

## Checks

On a scratch copy
(`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pshell/check`) I
inserted Tier 1's Blocks A and B, the Tier 2 section with its Appendix A entries, and my items 1–6 and crosswalk rows.

- `lint.py --chapters`: 62 files, 4736 labels, 12 hits. All 12 are pending markers: 10 in the Tier 2 text and my 2.
- `assemble.py --check`: labels 4736, problems 0.
- Assembled paper: no line longer than 121 characters, and no unresolved label in the new section.
