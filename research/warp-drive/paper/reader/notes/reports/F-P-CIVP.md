# F-P-CIVP: fix round on proofs/P-CIVP.md after R-P-CIVP

File: `research/warp-drive/paper/reader/proofs/P-CIVP.md`
- before: md5 aa08312166da99581416a9753bad3c98, 1188 lines
- after: **md5 280a89e05902d035236edf531de3a5a5, 1279 lines**, 18 proofs, 18 end marks

No chapter, crosswalk, Appendix A, bibliography or other proof file was edited; nothing committed. The labels Tier 2
cites (prop:loc-cone-local, lem:loc-cone-in, thm:loc-cone-development) are unchanged. No label added or removed (36).

## Applied, in the reader's words

- **Major 1** (lem:loc-cone-unique): statement now says ε, ε_2 depend only on the background, u_1, v_1, the band and k;
  steps (1)–(3) replaced by the reader's text (Stein extension of g′ − Ĝ by thm:std-sy-extension, the fixed slab
  [τ_init, τ_+], 𝒟′ := G_* ∩ angular wedge, energy estimate on Φ(𝒟′) with the competitor's matrices, s = k − 2); step
  (4) "near p"/"at p" → "on 𝒟′", "𝒟′ ∩ F" → "𝒟′"; the unused g_e′ is gone (nit 8).
- **Major 2**: thm (b) weakened to the fixed margin ϑ_a′ − η/4 − 2C_0(uv)^(1/2), ϑ_b′ + η/4 + 2C_0(uv)^(1/2); the proof
  chooses δ_c once with 2C_0(δ_c(u_1 + v_1 + 1))^(1/2) ≤ η/4; the limit δ_c → 0 is removed.
- **minor 1** G-invariance of U (end of lem:loc-cone-cauchy); **minor 2** B_♭ in the frozen part (definition, display,
  (b), proof of (a)); **minor 3** "bounds of every order" → order k + 1; **minor 4** |Ψ − id| ≤ 6σ sup|d(Ψ − id)| in case
  (II); **minor 5** degree argument replaced by the contraction; **minor 6** "a number C_* ≥ sup_𝒮 e^(σ_e)/R_e", C_* :=
  sup_(Q′) for prop:loc-cone-local, δ_2 over Q′ in terms of Ω_e, R_e, C_b "depending only on Λ, k and the background";
  **minor 7** the theorem's data on [v_1, v_1 + δ_1] determined from extended free data; **minor 8** (0, π/2) in place of
  [0, π/2] and "near ϑ = 0 and ϑ = π/2" (also in the jets lemma's X); **minor 9** past-set version of
  lem:loc-cone-jets (iv), proof "on N ∩ D"; **minor 10** placement phrases via the merged texts; **minor 11**
  rem:loc-cone-scope (i) now cites thm:civp-large, item 7 is merged text D.
- **Nits** 1, 2, 3 (both sites), 4, 6, 7, 11, 12, 13, 14 (and prop:loc-cone-formal now takes u_K, v_K ∈ [0, ∞]), 16
  (quotation closed with " …"), 17, all as proposed. **Nit 15** adopted: prop:loc-cone-local asks the equations only on
  𝒪 ∩ {u ≥ u_Q, v ≥ v_Q}, and the background sentence after lem:loc-cone-strips says so.
- **Nit 5** (notation): frame coefficient η → ϖ (28 sites, frame and Ricci lemmas), Borel scale ε_0 → ε_B
  (lem:loc-cone-borel and its two uses), extension length a_0 → λ_e (lem:loc-cone-extension, prop:loc-cone-local).
  Deviation: the rectangle of prop:loc-cone-local is not renamed 𝒬 but loses its letter ("a rectangle [u_c, u_c + λ_u]
  × [v_c, v_c + λ_v] ⊂ Q"), because 𝒬 beside the compact set Q would be a worse clash than R beside the radius. σ
  (Tier 2's name too) and u_1 (the theorem's parameter) are kept. In the merged chapter Tier 2's section has its own
  ϖ, η among its connection coefficients; the two sections define their symbols separately.
- **Nit 9 / Placement**: every old text rebased on the current head and checked to occur exactly once, as whole lines:
  item 3 chapter 83 lines 8–9, item 4 chapter 83 lines 593–600, item 5 chapter 01 lines 191–193, item 6 chapter 03
  line 375 (the site of Tier 2's item 6; this file's former item on the bullet's last lines is dropped), item 7
  chapter 90 line 208; anchors 83:591 and 83:602 exact. New texts of items 3–7 are the reader's merged texts A, B, C, E,
  D; the Placement says Tier 2 uses the same texts at the same sites (its items 2, 3, 5, 6 and the second pair of 4),
  so each site changes once. New item 11: what changes if the Tier 2 section is not merged. Item 9 notes the extension
  operator (thm:std-sy-extension, already in Appendix A) and that the degree argument is gone.
- **Nit 10 / Crosswalk**: all 36 rows now carry "paper/reader/proofs/P-CIVP.md@PENDING:N" (N = label line, checked);
  six exact new cells for existing rows (ch:localised-data, sec:loc-cones, prop:loc-cones in 83; sec:organisation in
  01; sec:further-results in 03; sec:scope-families in 90).

## Checks

- Proof file: every line ≤ 121 (raw and with worst-case label resolution); no wrapped line starting with a Markdown
  marker; no backslash; labels unique, none colliding with chapters; every reference resolves to a chapter label, a
  label of this file, or (thm:civp-large, def:civp-large-data) a label of Tier 2's section. Single-file lint: only
  "reference to undefined label" (cross-file) and "file name" on the crosswalk source fields, whose format was
  prescribed.
- Scratch merge (scratchpad/reader/merge-civp): chapters, crosswalk, assemble.py, lint.py, OUTLINE.md copied; Block A
  inserted after 83:591, Block B (heading without "Block B.") and then Tier 2's section (pending markers resolved to
  thm:loc-cone-development, lem:loc-cone-in, prop:loc-cone-local) before the heading of sec:loc-kid; items 3–7
  applied; Tier 2's Appendix A item 7 inserted before thm:std-ctg-neighbourhood. `lint.py --chapters`: 0 hits, 4717
  labels; `assemble.py --check`: 0 problems; the assembled text (built in memory, nothing written) has no line over
  121, no wrapped line in the new region starting with a marker, and the paper-mode lint scan gives 0 hits.

## Not changed

Nothing in the review was declined. The fallback of item 11 is stated as rules (drop the clauses citing Tier 2), not
as full alternative texts.
