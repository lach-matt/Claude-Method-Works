# Report P-RI: the index-0 step of prop:iv6-1-1

The output is research/warp-drive/paper/reader/proofs/P-RI.md. It is not committed. No chapter, crosswalk or other proof
file was edited. The old texts are from HEAD (chapter 33 md5 9571426c902bea231329690543c17455, the file after the P-T49
merge); the working tree is the same file.

## Route chosen, and why

I chose route (iii): the paper's own relative index formula. It is exactly route (i), already proved in the paper.
- **lem:iii-f1-3-1** (chapter 34, "Relative index") is the relative index formula for N_tf(P̂, e^(iθ)), for any P̂
  satisfying (H1)–(H2), on the spaces of thm:i-c-4-3. These operators are scattering at sctf and b at ztf.
  - Steps 1–3 of its proof are the localisation at r = 0. With steps of width < 1, formal solutions of the normal
    operator are enough.
  - Its *Multiplicity* paragraph proves rank = ord det on each isotypic block, by the Smith form. This is the identity
    the coordinator's note and R-P-G24b M1 (β) ask for, so no Appendix A quotation is needed.
- **lem:iii-f1-2-4** and *Types and representations* (sec:iii-f1-1) reduce the count to the type-wise matrices,
  uniformly in a parameter.
- **The proof of prop:iii-f1-3-3 (iii)** deforms chapter 34's operator to the free one, through the invariant
  G = ind − Σ_π (n_π − dim W_π).

The new text runs that argument for □^C_b, deforming γ_C = λh⁻¹ with λ from 1 to 0. As the note asks, it combines the
formula with chapter 33's own counts with multiplicity: lem:iv4-1-3 (a) and prop:np-10-54 (i).

The other routes:
- **Route (i), written out in chapter 33.** I drafted it (a sector Mellin lemma plus a companion-matrix count). It works,
  but it duplicates lem:iii-f1-3-1, and it still needs the Fredholm property at weights that are root-free for one
  sector only.
- **Route (ii), a fixed-weight homotopy.** It fails: the paper proves nothing about the roots at intermediate h, so it
  cannot exclude a root of the sector crossing the weight line during the deformation.

## What is proved

The index of eq:iv6-1-1 is 0 for every admissible (s, ℓ, β) and every σ ∈ e^(i[0,π]).
- Only weights that are root-free for the whole indicial family are used. So the Fredholm property at every λ comes from
  thm:i-c-4-3 (3).
- This also removes a second gap in the old step (ii): the old text claimed the Fredholm property at a weight that is
  root-free for one sector only, which the chapter's estimates do not give.

The changes, all in chapter 33:
- **P-RI-1** rewrites the overview sentence of sec:iv6, 2 lines becoming 4. It now cites lem:iii-f1-3-1, with
  thm:std-relative-index as attribution only.
- **P-RI-2** replaces the "Index 0" part of the proof of prop:iv6-1-1, lines 2394–2426: 33 lines become 62.
- **Typos.** Two are fixed inside the rewritten sentence: θ_in → ϑ_in, and r_mid → 𝗋_mid.
- **Labels.** None is added. No Appendix A entry is added.
- **Crosswalk.** The note of the prop:iv6-1-1 row is extended; the proof file gives the old and new rows.

## Points for the coordinator

1. **Forward citation.** Chapter 33 now cites lem:iii-f1-3-1 and lem:iii-f1-2-4 of chapter 34 in a proof step.
   - This is not circular. These lemmas use only chapter 22 and the representation theory of sec:iii-f1-1. Chapter 34
     uses chapter 33 only in prop:iii-f1-3-3.
   - Chapter 33 already cites chapter 34 elsewhere.
   - If wanted, the "Weights" paragraph of sec:iii-f1-3 and the two lemmas can move unchanged to chapter 22.
2. **lem:s14-tf-inputs (v) is now cited nowhere.** It is still correct. Keep it or drop it.
3. **P-G24b.** Its §6.1 and its class (c) item are closed by this file.
   - None of its 43 old texts meets P-RI-1 or P-RI-2, so either order works. I checked this by applying all 43 first.
   - P-G1's texts do not meet them either.
4. **A remark on the old counts.** The old "j = 2, 3, 1" left out the harmonic multiplicity dim π. The same factor
   occurs on both sides, so the conclusion was unaffected. The new count is per isotypic block, with dim π explicit.

Nothing is left open.

## Check outputs

Copy A (HEAD, with P-RI applied; /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pri/tree/):

    before:  lint --chapters: 62 file(s), 4649 label(s), 0 hit(s);  assemble --check: labels 4649, problems 0
    after:   lint --chapters: 62 file(s), 4649 label(s), 0 hit(s);  assemble --check: labels 4649, problems 0
             lint --paper: PAPER.md: 0 hit(s)

Copy B (all 43 P-G24b texts, then P-RI): lint 0 hits over 4665 labels, assemble 0 problems, PAPER.md 0 hits.

Further checks:
- **Line lengths.** No line of the assembled chapter 33 exceeds 121 characters. The new texts stay within 121 characters
  even with every label replaced by "Proposition 33.123".
- **Typography.** There is no backslash, and no new line starts with a forbidden marker.
- **The proof file.** Applying its two old/new pairs to the HEAD chapter reproduces copy A exactly.
