# P-CIVP3: fix round after R-P-CIVP3, and re-base on the merged Tiers 1–2

I edited one file: `/home/user/Claude-Method-Works/research/warp-drive/paper/reader/proofs/P-CIVP3.md`.
- Before: md5 1d196fae6ed5c92557721eb8dadfd294, 1,126 lines.
- **After: md5 d4c83116408265dc0c64406172842077, 1,102 lines.** The section is lines 1–823, the Placement starts at line
  825 and the crosswalk rows at line 1057.

No chapter, crosswalk or other proof file was edited, and nothing was committed. Plain `assemble.py` ran only in the
scratch copy.

## Labels renamed or removed (for the Tier 4 and Tier 5 files)

- **Removed: `lem:loc-axis-rectangle`.** The corollary now cites Tier 2's lem:civp-large-rectangle (a). Neither
  P-CIVP4.md nor P-CIVP5.md cites the removed label.
- **Renamed: none.**
- **The other 30 labels are unchanged.** That includes sec:loc-axis-leaves, which P-CIVP5.md cites.
- **cor:loc-axis-cones** keeps its label but is now stated for every v_1 > 0, the rectangle being [0, 7.2] × [0, v_1].
  This is because Tier 2's lemma gives every v_1.

**Mapping for Tier 4's pending markers:**
- `tier3-section` → sec:loc-axis.
- `tier3-theorem` → thm:loc-axis.
- `tier3-theorem-general` → also thm:loc-axis. It is stated for any round two-dust background on a rectangle
  Q1 = [0, u_1] × [0, v_1] with a margin δ_1: σ_e and R_e > 0 smooth on [−δ_1, u_1 + 2δ_1] × [−δ_1, v_1 + 2δ_1], solving
  the equations on its part in F. The data must be near the background's in C^(m_1), m_1 = 12k + 42, k ≥ 9, in the
  normalised gauge, with nonnegative densities. A rectangle Q_0 ⊂ G qualifies when the background extends past its far
  sides with a margin, as Tier 2's lemma shows for [0, 7.2] × [0, v_1].

## Findings applied

All findings were applied. Where I changed the replacement text, the reason is given.

### Major 1 (lem:loc-axis-dependence, θ chosen after ϵ′)

Applied as given. The infinite-order vanishing on the convex set 𝒦 = R′ ∩ {t ≤ t*} gives, by Taylor's formula, a bound
Cθ^(k+1) on 𝒩_θ. That absorbs the cut-off, and ϵ′ is gone. The review named lines 638–649; the text it replaces is
638–648, so I applied it by content.

### Minor findings

- **Minor 1 (sign in σ_A[V]).** Applied.
- **Minor 2 (def:loc-axis-data).** Applied as "extends to a smooth field of Lorentzian forms on D × S³" instead of "a
  smooth Lorentzian metric". D may be an edge, where the forms act on the 5-dimensional tangent spaces along D × S³. The
  non-degeneracy is what the equivalence needs.
- **Minor 3 (the extension keeps the localisation).** Both replacements applied. In the proof I wrote "every
  v-derivative of f − f̊ at v = v_1 vanishes" instead of "every h_j vanishes", because h_j is not named in that proof. I
  also added that γ̃ is unchanged by its renormalisation there.
- **Minor 4 (the decoupling of the jet equations through (Ψ1) and (Ψ3)).** Applied. I checked it against (Ψ1) and (Ψ3)
  of lem:loc-cone-jets as merged.
- **Minor 5 (four places, plus the uniqueness wave map).** Applied.
- **Minor 6 and minor 7 (placement items 9 and 3).** Absorbed by the re-base below. Item 3 no longer rewrites Tier 1's
  Tier 2 clause at all: it inserts a sentence. So the superseded "v_1 > 4.5 and u_1 > 7.2" clause cannot come back, and
  the merged "u_1 = 7.2, v_1 = 4.5 admissible" text stands.

### Nits

- **Nits 3, 5–12, 14, 15, 19 and 20.** Applied as given. For nit 11 the letter is ξ; nit 19 uses it.
- **Nit 1.** Applied, with "and 2δ_e < δ_1" added. This is why extending Δ by 0 is smooth: the support strips lie inside
  𝒮, away from its inner boundary.
- **Nit 2.** Applied. F_0 is described explicitly (local terms at 𝐔̊ + ϒ(Z), the σ_A term at 𝐔) rather than "evaluated
  as just stated", because that evaluation is stated before the lemma.
- **Nit 4.** Applied in lem:loc-axis-angle. I also amended lem:loc-axis-energy:
  - its statement drops the transversality of the faces to the slices;
  - its proof says that lem:loc-cone-energy uses only that every 𝒟_s is Lipschitz;
  - so lem:loc-axis-angle cites lem:loc-axis-energy for the Lipschitz domains.
- **Nit 13.** Applied. Ω̂ > 0 is automatic, since ln Ω is the field.
- **Nits 16–18 (placement).** Carried into the re-based items 4, 2 and 6.

### Tier 2's lem:civp-large-rectangle (a)

It gives everything lem:loc-axis-rectangle gave:
- [0, 7.2] × [0, v_1] ⊂ G;
- R ≥ 1.519357 > 1.5 and R_v > 0;
- a smooth background on [0, 7.2 + 2δ] × [0, v_1 + 2δ] and smooth positive extensions on [−δ, 7.2 + δ] × [−δ, v_1 + δ].

It does so for every v_1 > 0, not only v_1 = 4.5. So my lemma is removed, and the corollary's proof derives a background
with margin δ_1 := min(δ, v_1)/2 from it.

## Re-base of the Placement on HEAD (Tiers 1–2 merged at f7b0cab8)

Every old text is quoted from chapters/ at HEAD bce54b51. The merge script checks that each occurs exactly once, as
whole lines. Item 13 is dropped.

1. **The section.** Goes into chapter 83 after the Tier 2 section (ending with rem:civp-large-beyond, line 2389), before
   sec:loc-kid (line 2391) and before any other section placed there.
2. **83:13–14.** A sentence on thm:loc-axis and cor:loc-axis-cones, added before the sentence on Σ_τ0 (nit 17).
3. **83:694–695 and 83:704–705.**
   - 694–695: one sentence on the whole-rectangle development is inserted after "([[lem:loc-cone-strips]] (c))", and the
     next sentence names its data ("the cone data localised in a band").
   - 704–705: the last sentence now says what the section adds, "cone data that differ from the background's near an
     axis and are not near the background's" are not developed, and cites rem:loc-axis-scope.
   - Two new texts are given for 704–705: one without the null-shell section, ending "no other result of this paper uses
     these developments", and one merged with P-SHELL's item 8, ending "except finitely many null shells … ; no result of
     the other chapters uses these developments". The merged one carries P-SHELL's text verbatim (checked by script).
4. **83:676–680, rem:loc-cone-scope (ii).** The last old line is 680, so P-SHELL's item 2 on line 681 composes with it
   (nit 16).
5. **83:685–687, rem:loc-cone-scope (iv).** Now cites lem:civp-large-rectangle (a) and cor:loc-axis-cones, for every
   v_1.
6. **83:1628–1630, rem:loc-cone-local-scope.** Nit 18 applied.
7. **83:2369–2371, rem:civp-large-domain.** An old/new pair with one sentence appended. A second text is P-SHELL's
   item 3 new text with the same sentence appended.
8. **ch81 1326–1329.** Tier 4's item 2 changes the same lines for the same reason. My text contains its clause, so one
   copy is kept.
9. **ch03 376–381.** Minor 6: the two kinds of data are listed separately.
10. **ch90 217–218.** One text alone and one merged with P-SHELL's item 5, which is carried verbatim.
11. **Unchanged:** ch01, the 10 l5 sentences of ch87 and ch90, and ch80.
12. **No Appendix A entry and no reference.**

**Crosswalk.** 30 rows as real tab-separated lines, source `paper/reader/proofs/P-CIVP3.md@PENDING:N`, as in the merged
Tier 1/2 rows. A copy is at
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pcivp3-crosswalk.tsv. Note
additions are given for these rows:
- chapter 81's lem:class-leaf-differences, whose source is my lines 975–997;
- rem:loc-cone-scope, rem:loc-cone-local-scope and rem:civp-large-domain.

**Still to merge by hand if Tier 4 lands.** Item 6 keeps Tier 1's claim that a statement with no background, for data
prescribed up to the axes, "is not given in this paper", and item 3's alone text keeps "no other result of this paper".
If Tier 4's thm:civp-axes (large data at the axes near the cones) is placed, these sentences must be merged with its
texts.

## Check outputs

The scratch copy was made by `git archive HEAD` (bce54b51):
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/m3/research/warp-drive/paper/reader/.
The section was inserted, and items 2–10 (the texts without the null-shell section) were applied by `scratchpad/tools/merge3.py`.

- `python3 lint.py --chapters`: "chapters: 62 file(s), 4781 label(s) defined, 0 hit(s)".
- `python3 assemble.py --check`: "labels 4781, computations cited 0, problems 0".
- `python3 assemble.py`, in the scratch copy only: "labels 4781, computations cited 0, problems 0".
- `python3 lint.py --paper`: "PAPER.md: 0 hit(s)".
- The resolved-length and line-start check over the 876 changed chapter lines found no line over 121 characters before
  or after label resolution, no bad wrapped start, no backslash and no unresolved reference.
- In P-CIVP3.md itself, no non-TSV line is over 121 characters and no wrapped prose line starts badly.

## Final round (after the null-shells merge, 878e20e2)

**P-CIVP3.md: md5 dfa0b5519b02565e8586e46db00d12a4, 1,109 lines.** The section is lines 1–823, byte-identical to
d4c83116. The Placement starts at 825 and the crosswalk rows at 1064, and the 30 rows themselves are unchanged. The full
diff from d4c83116 is at
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/P-CIVP3.d4c831-to-dfa0b5.diff
(167 lines; every hunk is at line 826 or later).

What changed, all in the Placement:
- **Intro paragraph.** Old texts are now quoted from HEAD with Tiers 1–2 and the null-shells section merged. The
  "New, with the null-shell section" variants are gone, and so is the composition note on item 4.
- **Item 1.** The section goes immediately after the last line of rem:civp-large-beyond, "not explicit and no estimate
  of the solution is given." (83:2407), and immediately before "### Null shells along the leaves {#sec:loc-shells}"
  (83:2409), with one blank line before and one after.
- **Item 3 (first part).** Only its line numbers moved: paragraph 83:702–721, lines 707–708.
- **Item 3 (continued).** Old is 83:717–721 as at HEAD. New inserts only "and are not near the background's
  ([[rem:loc-axis-scope]])" after "near an axis"; the null-shell wording follows verbatim.
- **Item 4.** Old 83:684–688, content unchanged. "(iii), which begins on the next line, is unchanged" replaces the note
  on the null-shell placement.
- **Items 5 and 6.** Only line numbers moved: 83:698–700 and 83:1644–1646.
- **Item 7.** Old is 83:2385–2389 as at HEAD, with the null-shell wording. New is that text verbatim with one sentence
  appended.
- **Item 10.** Old is 90:217–223 as at HEAD. New inserts the thm:loc-axis sentence before "Developments of cone data …"
  and narrows that sentence to "… near an axis and are not near the background's … ([[rem:loc-cone-scope]],
  [[rem:loc-axis-scope]])"; the null-shell sentence follows verbatim.
- **Items 2, 8 and 9.** Unchanged; their old texts were checked at HEAD.
- **Item 13, new.** It rewraps 83:4707–4711 (prop:bg-slice, paragraph *The packet*) without changing a word. With the
  section inserted, [[prop:bg-rays]] becomes Proposition 53.102 and that line reaches 122 characters after assembly, the
  one hit `lint.py --paper` found. The new lines are at most 121 characters also with every chapter-83 label padded to
  three digits after the point, so later sections cannot push them over.
- **Crosswalk.** The rows go before the row of sec:loc-shells. The ch81 row's source lines are now 975–997 → 965–987
  (item 8's lines in this file).

Checks, on a `git archive` of HEAD b5284962 in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/m4/research/warp-drive/paper/reader/,
with the section inserted and items 2–10 and 13 applied (`tools/merge4.py`, which asserts each old text exactly once as
whole lines):
- `lint.py --chapters`: "chapters: 62 file(s), 4833 label(s) defined, 0 hit(s)".
- `assemble.py --check`: "labels 4833, computations cited 0, problems 0".
- `assemble.py`, scratch only: "labels 4833, computations cited 0, problems 0".
- `lint.py --paper`: "PAPER.md: 0 hit(s)".
- The changed-lines check over 887 lines found no flags.

Labels: none renamed or removed in this round. lem:loc-axis-rectangle, removed in the previous round, stays removed.
