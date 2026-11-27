# Report: proofs/P-CIVP5.md, fix round 4 (Tier 5, further dust families at the axes)

File: research/warp-drive/paper/reader/proofs/P-CIVP5.md, 1,240 lines, md5 5536e949d28784c53d757a650bec8c1f.
Previous version: cb809324 (at HEAD 13a5b209). Delta against HEAD: +115 −108 lines. Against the reader's fixed copy
P-CIVP5-fix2.md (md5 46e7e2ee): 196 changed lines, nearly all from rewrapping, the two nits below and the placement.
Not committed. No chapter or crosswalk file was edited.

The starting point is the reader's fixed copy P-CIVP5-fix2.md. That copy already carries minors A–D and nit 2. Nits 1
and 3, the rebased placement and the regenerated crosswalk are added here.

## Minors A–D (the reader's texts, as given in fix2)
- **A.** lem:class-leaf-tame (ii): eq:class-leaf-s is differentiated five times.
- **B.** lem:loc-t5-uniqueness: further families agree on a compact neighbourhood 𝒦_A^+ of 𝒦_A″, and κ_A is built from
  it. In thm:loc-t5 (c), 𝒦_A^+ is taken inside int 𝒦_A′.
- **C.** The bound is Cθ², not Cθ.
- **D.** The L² to H^σ constant of E_b is Σ|c_l| l^(1/2).

## Nits
- **Nit 1.** Stein's operator is bounded on H^(n+1), not H^n (Block A2, line 38).
- **Nit 2.** The jet recursion in lem:loc-t5-jets (b) is in the order the reader gave: q_A of order j + 1 lies in
  C^(m_0−5j−3). The text is the reader's, rewrapped only.
- **Nit 3.** This one goes further than the reader's text. In the continuity step of lem:loc-t5-uniqueness, χ̃_A is no
  longer a fixed cut-off.
  - **Why the reader's text was not enough.** It says the two states have the same phase type at the axis points of
    supp χ̃_A. That gives no lower bound on |p_A(∂_z)| for W where U_2 ≠ U_1. Away from the agreement region the slices
    of t_A^N need not be spacelike for g_2, so a convex combination does not obviously keep the bound c′.
  - **What replaces it.** c_A bounds |p_A(∂_z)| below for U_1 on the relevant axis points, and L_A bounds the C¹ norm of
    the difference of the family-A components. Set d_A := min(1, c_A/(4L_A)), small enough that both phases are defined
    on the d_A-neighbourhood of supp κ_A. χ̃_A equals 1 on the d_A/2-neighbourhood of supp κ_A ∩ {τ^N ≤ s_* + θ}, is
    supported in its d_A-neighbourhood, and has |∂χ̃_A| ≤ C/d_A.
  - **Why it works.** The second Taylor bound and the mean value theorem make the family-A part of U_2 − U_1 at most
    Cθ^(k+1) + L_A d_A in C¹ there. On the axis, therefore, |p_A(∂_z)| ≥ c_A/2 for θ small. W's further components have
    C¹ norm at most that of U_1 plus C(Cθ^(k+1)/d_A + 1 + L_A). So the bounds (M′, c′) depend on U_1 and U_2 but not on
    θ, and the rest of the step stands as written.

## Placement
Rebased on HEAD directly, and the "with P-CLD applied" framing is gone. The intro now says that old texts are whole lines
of the chapter sources at the current head, each occurring once. Block A1 cites lem:class-leaf-states, the definitions
before it, and Steps 1–7 of the proof of lem:class-leaf-differences, all at the current head. Each anchor was checked
against HEAD.
- **Item 1.** Block A1 goes before the heading of sec:class-axes-stability (81:1909), after lem:class-leaf-reference.
- **Item 2.** Block A2 goes after rem:class-kato-model, whose last line is 81:876, and before the heading of
  sec:class-off-axes (81:878).
- **Item 3.** Block B goes after the last line of rem:loc-axis-scope (83:3256), before the heading of sec:civp-axes
  (83:3258).
- **Item 4.** 83:738.
- **Item 5.** rem:loc-axis-scope (ii), 83:3254–3255.
- **Item 6.** rem:class-scope, 81:2215–2216.
- **Item 8.** Now ends "and the proof of lem:class-leaf-differences, which uses no other."
- None of the old texts has changed since the merge base. Chapters 81 and 83 and the crosswalk are unchanged between
  1c3ba1ba and HEAD 13a5b209.

## Crosswalk
31 tab-separated rows, with line numbers regenerated after the edits:
- 5 after rem:class-kato-model;
- 2 after lem:class-leaf-reference;
- 24 after rem:loc-axis-scope.

## Checks
Scratch merge at /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pcivp5/merge5:
HEAD 13a5b209 plus this file's placement and 31 rows. Items 4, 5 and 6 each match their old text exactly once.
- `lint.py --chapters`: 62 files, 5110 labels, 0 hits.
- `assemble.py --check`: labels 5110, 0 problems.
- `assemble.py`, run in the scratch copy only, gives 0 problems.
- In the assembled text of the three blocks (65, 253 and 774 lines), every line is at most 121 characters. No wrapped
  line has a bad start; the only lines starting "#" are Block B's five #### subsection headings.
- thm:loc-t5 assembles as Theorem 53.73.
- In the file, every non-tab line is at most 121 characters with each [[…]] counted as 18. There are no backslashes,
  no pending markers and no reference to lem:class-leaf-arc.

## For the reader to check first
- The quantitative χ̃_A construction (nit 3) in the continuity step of lem:loc-t5-uniqueness.
