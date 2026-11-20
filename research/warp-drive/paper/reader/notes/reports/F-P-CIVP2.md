# F-P-CIVP2: fix report for proofs/P-CIVP2.md

Review applied: notes/reviews/R-P-CIVP2.md (verdict NOT CONFIRMED, five minor findings, fourteen nits, no Major).
md5 before: 775b987a80e56ec8ac91a5ebfad0bfe1 (750 lines). **md5 after: 924a45ecfbef762ee34a500044e9414f** (796 lines).
I edited only `proofs/P-CIVP2.md` and scratch files. No chapter, crosswalk or other proof file was touched, and
nothing was committed.

## Findings, as applied

All five minor findings and all fourteen nits are applied in the reviewer's words, except where noted.

- **minor 1 (densities ≥ 0).** prop:civp-large-system (b) now assumes "q_in, q_out ≥ 0 on U". Step 3 gets the
  reviewer's transport argument: F's q_in and q_out are the data's along the integral curves, times a positive factor.
- **minor 2 (A_c, A_s at the axes).** Three places now take their functions on (0, π/2): the class solution in the
  gauge (smooth off the axes, the metric extending smoothly to the axes), the definition of cone data, and
  prop:civp-large-corner. The definition and the proposition give the ranges [0, v_1], [0, u_1], [v_c, v_c + l_v] and
  [u_c, u_c + l_u].
- **minor 3 (clash with chapter 83's u1 = 5.7).** The bounds are renamed u1 → u_1 and v1 → v_1 throughout, including
  inside formulas such as 4q1²v_1 and η0/(4u_1β1). "Phases u_1 = v, u_2 = u" is gone.
- **minor 4 (rem:civp-large-beyond and placement item 3).** Replaced by the reviewer's texts:
  - the positivity of e^ϕ is now a stated condition;
  - "the background is defined in the gauge on Q1 for some v_1 > 4.5 and u_1 > 7.2" is stated as a condition;
  - the undefined 𝒞_out^(v1) is replaced by 𝒞_out ∩ {v ≤ v_1}.
- **minor 5 (chapter 90's opening sentence).** Placement item 4 now has two old/new pairs. The first rewrites the
  opening sentence (lines 195–196) in the reviewer's words; the second appends to line 204, as before.
- **nits 1–13.** Applied verbatim, including:
  - nit 4: the CCTW misprint is now stated in the text;
  - nit 11: the stray full stop in the quotation is removed ("× Y Consider");
  - nit 13: "the flat connection as both ∇ and ∇̊", in both places.
- **nit 14.** Three letters are renamed:
  - the rectangle R → 𝒬 (including 𝒬_p and sup_(𝒬×J));
  - the band margin of prop:civp-large-corner η → κ, with "κ := η0" in Step 4;
  - the spread k(u, v) → w(u, v) in the energy lemma and in Step 3.

  k = e^(α−β) stays, and the "k = ℓ − 1" inside the CCTW quotation is untouched.
- **My own changes.**
  - In the corner step I added "while b on N_o becomes b − b(u_c, v_c, ·)", the reviewer's observation from section C.
  - I re-broke one line of prop:civp-large-corner so that "Ω > 0" is not split across two lines.

## The pending markers (T1–T4)

All three markers are kept. Each now has a short paragraph, where it is first used, stating what is required:

- **T3, `[[pending:civp-tier1-theorem]]`:** a new paragraph "*The small-data theorem.*" after the opening paragraph. The
  required statement: a solution in the gauge on {uv ≤ δ_*²} ∩ Q1 that induces the data, equals (g0, q̊) off
  [η′, π/2 − η′], comes with an estimate, and is unique only near the background. It is used for comparison only.
- **T2, `[[pending:civp-tier1-cin-cones]]`:** the paragraph after def:civp-large-data now states the 𝒞_in analogue of
  prop:loc-cones (b = 0, Ω the background's). It also says that no step of the proof of thm:civp-large uses it.
- **T1 and T4, `[[pending:civp-tier1-local]]`:** a new paragraph "*What is required of …*" before
  prop:civp-large-corner. It says the construction must provide that proposition exactly as stated, with its
  regularity index m defined there (T4). It lists every feature used:
  - a corner anywhere in Q1, and edges of any length;
  - Ω arbitrary on both edges, and b arbitrary on N_o;
  - densities q ≥ 0;
  - no smallness;
  - σ = σ(Λ, κ, m, background), uniform in the corner and in the edge lengths.

**For the coordinator (interface remark, not a finding).** The Tier 1 draft's prop:loc-cone-local looks like the
intended source of T1, but it does not match it yet in two ways:

1. It requires edge data on lengths l + δ_1 with δ_1 ≤ min(l_u, l_v)/2.
2. Its σ depends on δ_1.

The continuation of Step 4 uses short edges of length about σ, so it needs either σ independent of how short the edges
are, or a remark that edge data can be extended past their ends by a fixed length. Such an extension would continue the
free data and solve the constraint ODEs along the edge, with norms controlled by Λ. The rest of the draft's statement
(any gauge, any b on N_i, any corner values, localisation off [η, π/2 − η]) covers T1.

## Placement re-copied

Every old text was re-copied from the current chapters, and each occurs exactly once in its chapter (checked by
script). The line numbers that moved are now:

| Chapter | Site | Old lines | Current lines |
|---|---|---|---|
| 90 | opening sentence | 192 | 195–196 |
| 90 | last line | 200 | 204 |
| 01 | paragraph on Part V | 190–191 | 192–193 |
| 03 | item *More families* | 367 | 368 |
| 95 | insertion before thm:std-ctg-neighbourhood | — | 467 |

These did not move: 83 at lines 8–9 and 593–600, 83's sec:loc-kid at 602, and 98 at lines 26–28. Item 9 now also asks
for the two crosswalk rows of the appendix.

## Checks (on a scratch copy with the whole placement applied)

The section was inserted before sec:loc-kid, items 2–6 and 8 were applied, and the Appendix A entries were inserted.

- **`lint.py --chapters`:** 62 files, 4641 labels (baseline 4609, +32 = 30 + 2), 13 hits, all of them the pending
  markers. The baseline has 0 hits.
- **`assemble.py --check`:** labels 4641, problems 0.
- **Line lengths after label resolution:** 0 lines over 121 in the assembled text, with each `[[pending:…]]` replaced by
  "Proposition 83.123". The section resolves to chapter 53 (Theorem 53.15, Proposition 53.14).
- **Single-file `lint.py`:** only the pending markers and the cross-file labels a single-file run cannot see. Maximum
  line length 121, 7 proofs and 7 ∎, no backslash.
