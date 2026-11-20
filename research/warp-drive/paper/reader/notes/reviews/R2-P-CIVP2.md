# R2-P-CIVP2: confirming reading of proofs/P-CIVP2.md after the fix round F-P-CIVP2

File read: `research/warp-drive/paper/reader/proofs/P-CIVP2.md`, md5 924a45ecfbef762ee34a500044e9414f, 796 lines. It
was compared line by line with the version the first reader read (md5 775b987a80e56ec8ac91a5ebfad0bfe1, taken from
commit 46a74595). Every changed line was read in context, and so were the unchanged lines around each change. Nothing
under method/, drive/, extracted/ or recovered/ was read. No chapter, crosswalk or proof file was edited.

**Verdict: CONFIRMED.** All 19 findings are resolved and read correctly in context. Outside the pending interface I
found no new Major or minor issue. Inside the pending interface there is one minor: the paragraph *The small-data
theorem* does not state T3 as the first reader specified it, and it miscounts where the marker is used (N1 below).
There are also four nits (N2–N5).

## The 19 findings

- minor 1: resolved. The hypothesis "and let q_in, q_out ≥ 0 on U" is at l. 265. The transport argument is at
  l. 523–527, and it is correct:
  - F solves D_3q_in = −e^α χ̲ q_in (l. 241) and ∂_vq_out = −e^α χ q_out (l. 237) on 𝒮_δ × (0, π/2).
  - 𝒮_δ is a past set, so [0, u] × {v} and {u} × [0, v] lie in it.
  - F's b vanishes off [ϑ_a − η0, ϑ_b + η0], so the lines ϑ = const there are integral curves. Curves that start in
    the band stay in it, and they reach u = 0.
  - On 𝒞_out, F's q_in is the data's (f̄₃); on 𝒞_in, F's q_out is the data's (f̄₄). Both are ≥ 0, and the integrating
    factors are positive.
  The later uses are now covered: Step 4 ("Where F is geometric … by that proposition", l. 532), the corner step's
  edge data (prop:civp-large-corner needs q ≥ 0), and Step 5.
- minor 2: resolved, at l. 36–39, 41–43 and 418–419. Every other place agrees:
  - lem:civp-large-data (b)(i), l. 325–326: "𝒞_out ∩ (Q1 × (0, π/2))".
  - Step 5, l. 590: "extended by (g0, q̊_in, q̊_out) to the axes".
  - thm:civp-large (b), (c) and the T3 paragraph: equality with g0 "at the points with ϑ ∉ […]".
  - rem:civp-large-domain, l. 614.
  No "[0, π/2]", "N_o × S³" or "𝒞_out ∩ (Q1 × S³)" is left as the domain of the functions.
- minor 3: resolved. "u1" and "v1" no longer occur, and "phases u_1 = v" is gone (l. 37–38). u_1 and v_1 are used
  consistently: l. 29–30, 42, 52, 56–58, 489–493, 503–515, 535, 611, 620–627 and 688. In chapter 83, u_1 occurs
  nowhere and v_1 is already the cone length of prop:loc-cones (l. 575, 578, 594). The renderer prints "_" literally
  (`render/build_html.py`), so u_1 and the chapter's u1 = 5.7 stay distinct in print.
- minor 4: resolved. rem:civp-large-beyond (l. 619–623) and placement item 3 (l. 687–690) are the reviewer's texts,
  reflowed.
- minor 5: resolved. Item 4 now has two old/new pairs (l. 697–721). Both old texts occur once in chapters/90-scope.md,
  at l. 195–196 and l. 204. After both replacements the paragraph is true: the opening sentence covers the slice
  results, which are near the background's data, and the cone results, which are of any size (prop:loc-cones,
  thm:civp-large), and the rest of the paragraph is unchanged.
- nit 1: resolved (l. 245).
- nit 2: resolved (l. 248).
- nit 3: resolved (l. 16–19).
- nit 4: resolved (l. 289–291).
- nit 5: resolved (l. 483–485).
- nit 6: resolved (l. 459–462; rem:civp-large-domain l. 611 now names the cut-off and the extension).
- nit 7: resolved (l. 607–609).
- nit 8: resolved (l. 627).
- nit 9: resolved (l. 740–744).
- nit 10: resolved (l. 794–796).
- nit 11: resolved (l. 761).
- nit 12: resolved (l. 302–307).
- nit 13: resolved (l. 256, 491).
- nit 14: resolved, and every renaming is complete:
  - R → 𝒬: l. 297, 367–403, 417, 545–572, 575–583. The only remaining standalone R is the area radius (l. 30–31) and
    the curvature R(X, Y) (l. 145–179).
  - η → κ: l. 412, 416, 421, 424, 432, 436 and 543 ("κ := η0"). No other η is the margin.
  - k → w: l. 376–400, 510 and 512. k = e^(α−β) is kept (l. 226–272), and CCTW's "k = ℓ − 1" (l. 768) is untouched.
  - No placement text contains R, η, k or u1.

The writer's own changes are both correct:
- "while b on N_o becomes b − b(u_c, v_c, ·)" (l. 557). At u = u_c, Φ = id and ∂_uΦ = −b(u_c, v_c, ·), so the new
  b = ∂_uΦ + b∂_ϑΦ equals b − b(u_c, v_c, ·). This changes neither ∂_vb nor the constraints, and it vanishes off the
  band.
- The re-broken line at l. 418–419.

Clashes with chapter 83:
- 𝒬 occurs there only at l. 1941–1944, as a local quantity 𝒬 := μ/ℓ_v inside a proof in sec:bg-rays. No clash.
- w occurs there only as variables local to proofs (l. 438, 830–900, 1334–1335, 1421–1600). No clash.
- κ is a chapter-level symbol there. See N4.

## The pending interface

- **T1 and T4** (l. 407–413): stated exactly as the first reader specified. The paragraph covers: a corner anywhere
  in Q1; any lengths of the edges; Ω arbitrary on both edges; b arbitrary on N_o and zero on N_i; q ≥ 0; no smallness;
  σ depending only on Λ, κ, m and the background, uniformly in the corner and in the lengths; and m defined in the
  construction.
- **T2** (l. 54–61): stated as the first reader specified. That statement, however, omits an initial value. See N2.
- **T3** (l. 21–26): not stated as specified. See N1.

Every use of a marker:
- civp-tier1-cin-cones (l. 54, 640) matches its paragraph.
- civp-tier1-local (l. 407, 409, 416, 427, 641) matches its paragraph.
- civp-tier1-theorem at l. 612, 629, 668, 693 and 720 is a comparison, and matches.
- civp-tier1-theorem at l. 4 is also a comparison, but it is not among the places the paragraph lists.
- civp-tier1-theorem at l. 426 ("This is the development theorem of … with its smallness hypothesis replaced …") is
  a use in the proof of prop:civp-large-corner, not a comparison. The paragraph says the marker is "used only for
  comparison".
- l. 638 and 645 locate the section, and they are fine.

## Placement and typography (checked on a scratch copy)

Every old text occurs exactly once, as whole lines, at the stated lines of the current chapters (after a722cb42):
- chapter 83: l. 8–9 and l. 593–600;
- chapter 90: l. 195–196 and l. 204;
- chapter 01: l. 192–193;
- chapter 03: l. 368;
- chapter 98: l. 26–28.

The two insertion points are where the file says. The heading of sec:loc-kid is at l. 602 of chapter 83, after a
blank line. thm:std-ctg-neighbourhood is at l. 467 of chapter 95, after the heading of sec:std-characteristic and a
blank line. Each new text joins the following line and reads correctly in context.

On the scratch copy
(`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/r2civp2/`), I copied
chapters/, crosswalk/, assemble.py, lint.py and OUTLINE.md, then applied the section, items 2–8 and the two appendix
theorems:
- Baseline before the placement: `lint.py --chapters` gives 62 files, 4609 labels, 0 hits.
- After the placement, `lint.py --chapters` gives 62 files and 4641 labels (+32 = 30 + 2). It reports 13 hits, every
  one a pending marker.
- `assemble.py --check` reports labels 4641 and problems 0.
- In the assembled text, with each [[pending:…]] counted as "Proposition 83.123", no line is longer than 121
  characters. The section resolves to 53.4.
- No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". The two "- [CCTW16]" lines are list items after
  blank lines.
- All labels are lowercase.
- In the proof file itself the longest line is 121 characters, also after resolution. There are 7 proofs and 7 ∎.

## New findings

### N1 (minor, pending interface): the paragraph *The small-data theorem* does not state T3 (l. 21–26)

The paragraph has three problems.

1. It says the marker is "used only for comparison, in [[rem:civp-large-domain]] and [[rem:civp-large-beyond]]". It
   is also used in the opening paragraph (l. 4). The proof of prop:civp-large-corner (l. 426) uses the theorem
   itself, as the result whose smallness hypothesis is replaced.
2. It widens the quantifier. T3 asks that the theorem's data (Ω the background's) be cone data in the sense of
   def:civp-large-data, so that thm:civp-large (c) applies. The paragraph instead requires a development for every
   cone data near the background's, with Ω the background's on 𝒞_out only. That is more than the comparison needs. It
   is also more than the Tier 1 draft states: its theorem keeps Ω the background's on both cones, and the corner
   values of prop:loc-cones and of its 𝒞_in lemma are the background's there.
3. It uses Q1, "past set" and "class solution in the gauge" before the Notation paragraph defines them.

Old (l. 21–26):

    *The small-data theorem.* [[pending:civp-tier1-theorem]] is used only for comparison, in [[rem:civp-large-domain]] and
    [[rem:civp-large-beyond]], and what is used of it is the following statement: for cone data in the sense of
    [[def:civp-large-data]] near the background's, with Ω the background's on 𝒞_out, there is a class solution in the gauge
    [[eq:loc-double-null]] on the explicit past set {uv ≤ δ_*²} ∩ Q1, times S³, that induces the data and equals (g0,
    q̊_in, q̊_out) at the points with ϑ ∉ [η′, π/2 − η′] for some η′ > 0; it comes with an estimate of the solution, and
    its uniqueness is stated near the background only.

New: delete these six lines and the blank line after them. Insert the following, as its own paragraph, after l. 61
(the line ending "Data with q_in = q_out = 0 are vacuum data."), with one blank line before and after. All lines are
at most 120 characters, also after resolution.

    *The small-data theorem.* [[pending:civp-tier1-theorem]] is used for comparison, in the first paragraph of this
    section, in [[rem:civp-large-domain]] and in [[rem:civp-large-beyond]]; the proof of [[prop:civp-large-corner]] modifies
    its local construction, and what that proposition requires of it is stated before it. What the comparison uses is the
    following statement: for the cone data that [[prop:loc-cones]] and its analogue on 𝒞_in produce from free data near
    the background's, which are cone data in the sense of [[def:civp-large-data]] with Ω the background's on both cones,
    there is a class solution in the gauge [[eq:loc-double-null]] on the explicit past set {uv ≤ δ_*²} ∩ Q1, times S³,
    that induces the data and equals (g0, q̊_in, q̊_out) at the points with ϑ ∉ [η′, π/2 − η′] for some η′ > 0; it comes
    with an estimate of the solution, and its uniqueness is stated near the background only.

The lint count of pending hits does not change: one marker line becomes one marker line.

### N2 (nit, pending interface): the analogue on 𝒞_in needs the value of ∂_uϕ at S (l. 58–61)

On 𝒞_in the constraint is the second-order equation y″ + (1/3)(Σ(ℓ_i′)² + q_out) y = 0, with y = e^ϕ. Agreement with
𝒞_out at S fixes ϕ there but not the transversal ∂_uϕ. prop:loc-cones fixes the corresponding values at its corner
(ϕ and ∂_vϕ), and the Tier 1 draft's lem:loc-cone-in fixes ϕ and ∂_uϕ at u = 0 to the background's. The first
reader's T2 text omitted this value too.

Old (l. 58–61):

    background's outside a compact subset of [0, u_1] × (ϑ_a, ϑ_b), with b = 0 and Ω the background's on 𝒞_in, the
    constraint Ric(∂_u, ∂_u) = q_out determines γ_ϑ, A_c, A_s on every generator on which e^ϕ stays positive, and the
    result is the background's at every ϑ outside the band. No step of the proof of [[thm:civp-large]] uses it, the theorem
    taking cone data as given. Data with q_in = q_out = 0 are vacuum data.

New:

    background's outside a compact subset of [0, u_1] × (ϑ_a, ϑ_b), with b = 0, Ω the background's on 𝒞_in and ∂_uϕ the
    background's at S, the constraint Ric(∂_u, ∂_u) = q_out determines γ_ϑ, A_c, A_s on every generator on which e^ϕ stays
    positive, and the result is the background's at every ϑ outside the band. No step of the proof of [[thm:civp-large]]
    uses it, the theorem taking cone data as given. Data with q_in = q_out = 0 are vacuum data.

### N3 (nit, placement item 4): "δ … is explicit only for data near the background's" (l. 719–721)

The δ of thm:civp-large is never explicit. For data near the background's, the small-data theorem gives a different,
explicit neighbourhood {uv ≤ δ_*²}. Items 2 and 3 already say this precisely.

Old (l. 719–721):

    the gauge among solutions that equal the background near the axes; δ depends on the data and is explicit only for data
    near the background's ([[thm:civp-large]], [[pending:civp-tier1-theorem]]). Developments of cone data that differ from
    the background's near an axis are not established.

New:

    the gauge among solutions that equal the background near the axes; δ depends on the data, and a neighbourhood is
    explicit only for data near the background's ([[thm:civp-large]], [[pending:civp-tier1-theorem]]). Developments of
    cone data that differ from the background's near an axis are not established.

### N4 (nit, pending interface): κ is a chapter-level symbol of chapter 83 (l. 412)

Chapter 83 uses κ in several senses:
- κ := K(e_R, e_R) (l. 82), with κK^l_l in the very paragraph that item 2 edits (l. 10);
- κ0 in sec:loc-kid and sec:loc-momentum, directly after the insertion point (l. 707–716, 943–1025);
- κ_L, κ1, κ2;
- ϰ_i in sec:loc-cones (l. 532).

The section binds its κ in prop:civp-large-corner, so the proposition is unambiguous. However, the requirement
paragraph uses κ two lines before that binding. The letter can stay if the paragraph names it.

Old (l. 412–413):

    with b = 0 on N_i; densities q_in, q_out ≥ 0; no smallness of the data; and σ depending only on Λ, κ, m and the
    background on a neighbourhood of Q1 × S³, uniformly in the corner and in the lengths of the edges.

New:

    with b = 0 on N_i; densities q_in, q_out ≥ 0; no smallness of the data; and σ depending only on the bound Λ, the
    margin κ, m and the background on a neighbourhood of Q1 × S³, uniformly in the corner and in the lengths of the edges.

### N5 (nit, placement item 2): the first paragraph of chapter 83 still confines its data to slices

After the placement, chapter 83's first paragraph still says "data are taken on its slice Σ_τ0, τ0 = −0.68, or on a
slice bent from it" (l. 5–6). The second paragraph (item 2) and the new section treat data on the two null cones,
which prop:loc-cones already did. This is the same repair that minor 5 made for chapter 90. Item 2's header also calls
l. 8–9 "its opening paragraph", but they open the second paragraph. The old text below occurs exactly once in
chapters/83-localised-data.md.

Old (l. 656 of the proof file):

    *2. [[ch:localised-data]], its opening paragraph (lines 8–9).* Old:

New, followed by the existing pair for l. 8–9, which then begins with its own line "Old:":

    *2. [[ch:localised-data]], its first two paragraphs (lines 5–6 and 8–9).* The end of the first and the start of the
    second change. Old:

    of [[sec:two-dust-background]] with the explicit characteristic data of [[sec:bg-data]], and data are taken on its
    slice Σ_τ0, τ0 = −0.68, or on a slice bent from it.

    New:

    of [[sec:two-dust-background]] with the explicit characteristic data of [[sec:bg-data]], and data are taken on its
    slice Σ_τ0, τ0 = −0.68, on a slice bent from it, or on the two null cones through its corner sphere.

    Old:

(The old and new chapter lines are unindented in the file, as in the other items.)

## For the coordinator (not a finding)

The writer's interface remark in F-P-CIVP2 stands. The Tier 1 draft's prop:loc-cone-local asks for edge data on
lengths l + δ_1, and its σ depends on δ_1. T1, as now stated in the requirement paragraph, needs σ to be uniform in
the lengths of the edges.
