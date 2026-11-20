# Merge M-LL: proofs/P-LL.md into chapters 84, 90, 95 and 98

**Status: merged.** The three nits of R-P-LL were applied to the proof text first. Placement items 1–6 were then
applied exactly. Every placed block is byte-identical to its block in the proof text and occurs exactly once. The
crosswalks match their chapters row for row. All three checks are clean. The proof file is retired with `git rm`.
Nothing is committed.

Paths are relative to `research/warp-drive/paper/reader/`.

## 0. The nits, applied to proofs/P-LL.md

The proof text as committed is `392f69f4`, 206 lines. With the nits applied it has 210 lines, and every line is at
most 121 characters. The diff is in `M-LL.nits.diff`.

- **n1** (theorem, lines 114–122, now 115–125). Replaced by the reviewer's replacement text, R-P-LL lines 41–51, with
  the review's 6-space list indent removed. No page image was available, so the replacement was used. The changes:
  - "p. 517;" is added to the heading's citation;
  - "−1 ≤ x ≤ 1" is removed from the quoted display (19);
  - a sentence states the range from the proof's own display "|cf^(p)(x)| ≤ |T_n^(p)(1)|, −1 ≤ x ≤ 1".
- **n2** (line 53, now 53–54). Replaced by R-P-LL lines 65–66, so the reason for C1 Δτ ≥ 0 is now stated:
  "…, and C1 Δτ ≥ 0, as C1 ≥ 0 and / τ_end ≥ v_start − q0 > τ0,".
- **n3** (placement item 7, lines 202–206, now 205–209). The phrase "[[cor:layer-interpolation-band]],
  [[lem:layer-levels]] and the statement and proof of [[thm:layer]], which use the lemma only through its inequality."
  is replaced by the reviewer's text, which adds [[thm:layer-past]] and [[prop:layer-regions]]. The paragraph is
  rewrapped at 120 characters and no other word is changed. This is placement wording only and goes into no chapter.

## 1. The placements: old text located, line ranges after the merge

For each item a script first checked the old text. For items 1 and 2 the old text was the placement's quoted text,
whitespace-normalised, with "(its equation label)" read as `{#eq:layer-interpolation}` and the heading's label marker
put back in front. For items 3–6 it was the quoted or described text. Each old text matches the chapter's text and
occurs exactly once, both as exact bytes and normalised. The script then replaced the exact bytes. Item 3 used the Edit
tool (an exact string replacement), because other agents may be editing chapter 90. The joins were read 3 lines on
either side; they are listed in §2.

| item | place | old lines | new lines (after the merge) | proof-text block (nits applied) |
|---|---|---|---|---|
| 1 | 84, lem:layer-interpolation (sec:layer-window) | 844–862 | **844–879** (eq:layer-interpolation at 848) | 7–42 |
| 2 | 84, rem:layer-threshold-size (sec:layer-threshold; end of chapter) | 1354–1365 | **1371–1435** (eq:layer-size-base 1384, -c 1390, -taylor 1399, -edge 1405) | 44–108 |
| 3 | 90, sec:scope-constants | 97–98 | **97–98** | 182–183 (4-space quote indent removed) |
| 4 | 95, opening paragraph | 8–12 | **8–12** | 189–193 (indent removed) |
| 5 | 95, sec:std-chebyshev, after thm:std-chebyshev's last line (1253) | — | blank 1254, **1255–1265** | 115–125 |
| 6 | 98, between [DS23] (50–51) and [Dya16] | — | **52–53** ([Dya16] now 54) | 202–203 (indent removed) |

- **Item 4.** A script checked the words too. The new lines, normalised, equal the old lines 8–12 with
  "[See64] and [MM87] are" replaced by "[See64], [MM87] and [DS41] are", and nothing else changed.
- **Item 6.** [DS23] was directly followed by [Dya16]. [DS41] was nowhere in chapter 98 before the merge.
- **Not inserted.** The Placement section was not inserted, and neither were the proof text's heading and opening
  paragraph (lines 1–5) or sec:ll-literature's two lines. No `sec:ll-*` key occurs in chapters/ or crosswalk/.
- **Chapter sizes.** Chapter 84 grows from 1365 to 1435 lines, 95 from 1253 to 1265, and 98 from 186 to 188. Chapter 90
  stays at 230.
- **Chapter 90.** `git diff HEAD -- chapters/90-scope.md` is exactly the one 2-line hunk of item 3. No edit by another
  agent was present when I wrote it.
- **Old texts outside chapters.** "10^(−430)", "Λ_(i,m)" and "Λ_(1,m)" now occur nowhere in chapters/.

## 2. Byte-identity check (script `m-ll/check.py`)

For each item the check takes the block from the proof text, joins it with "\n", encodes it as UTF-8 and counts its
occurrences in the chapter's bytes. It also locates the block as whole lines. I ran it on the live proof file before
the `git rm`, and again on the kept copy after it. Both runs gave the same output:

```
item 1  chapters/84-equality-layer.md      proof 7-42 (36 lines, 3136 bytes)  chapter 844-879  byte-identical occurrences: 1  OK
item 2  chapters/84-equality-layer.md      proof 44-108 (65 lines, 4939 bytes)  chapter 1371-1435  byte-identical occurrences: 1  OK
item 3  chapters/90-scope.md               proof 182-183 (2 lines, 171 bytes)  chapter 97-98  byte-identical occurrences: 1  OK
item 4  chapters/95-standard-results.md    proof 189-193 (5 lines, 513 bytes)  chapter 8-12  byte-identical occurrences: 1  OK
item 5  chapters/95-standard-results.md    proof 115-125 (11 lines, 883 bytes)  chapter 1255-1265  byte-identical occurrences: 1  OK
item 6  chapters/98-references.md          proof 202-203 (2 lines, 182 bytes)  chapter 52-53  byte-identical occurrences: 1  OK
ALL OK
```

The joins, 3 lines on either side:

- **Item 1.** It opens after line 842 "### The window {#sec:layer-window}" and blank 843. It closes after "… ∎" (879),
  with blank 880, then cor:layer-interpolation-band (881).
- **Item 2.** It opens after "… ν_* = |ν(v_s − τ0)|." (1369) and blank 1370. It closes at "are below 2.71·10⁻¹²." (1435),
  followed by the file's single final newline.
- **Item 3.** It continues line 96's "… λ_L is the", and is followed by blank 99 and "### After the shell".
- **Item 4.** It continues line 7's "… listed in the references;", and is followed by blank 13 and the next heading.
- **Item 5.** It follows "…". Here log is the natural logarithm." (1253) and a blank line. It ends the file with a single
  newline.
- **Item 6.** It sits after [DS23]'s continuation line (51) and before "- [Dya16]" (54). Its continuation line has the
  file's 2-space indent.

## 3. Crosswalks

### Amended (crosswalk/84-equality-layer.tsv; notes only, source and source_name unchanged)

- **lem:layer-interpolation**, note now:
  `M-LL: replaced by the lemma of the confirmed proof P-LL (paper/reader/proofs/P-LL.md@392f69f4:7-42), merged verbatim: the Chebyshev-Lobatto variant (R4.5's C^DS) is now carried, nodes at the Chebyshev points of [u - H, u] and the interpolant bounded by thm:std-duffin-schaeffer; closed form of C_(i,m) and C_(1,m) = m((2m - 2)^(m-1)/(m - 1)!)^(1/m) added; the equidistant constant Lambda_(i,m) and round 1's kappa = 1 bound dropped, nothing else using them; divided-difference step written out`
  - Was: "divided-difference step written out; round 1's constant kept as the kappa = 1 bound; Chebyshev-Lobatto variant
    not carried".
- **rem:layer-threshold-size**, note now:
  `M-LL: replaced by the remark of the confirmed proof P-LL (paper/reader/proofs/P-LL.md@392f69f4:44-107), merged verbatim with R-P-LL's nit n2 (the reason for C1 Delta tau >= 0): lambda_L <= Lambda_4 < 2.709e-12 (1 + C1 Delta tau/(2 pi))^(-1456/1442) for K = 6 and < 2.3e-12 for K >= 7, hence below 2.71e-12, using only c_e > 1 and elementary factorial bounds; the source's 2.71e-12 proved in corrected form (its C_(1,1456) a grid value, 3.89723 in log10 against the exact 3.8966206, and its coefficient 0.945 from an upper bound of Delta tau, both in the wrong direction); 0.945 and P* not carried; the hand bound 10^(-430) withdrawn; F-84: for env_C of eq:envelope, not the numerical point of prop:lambda0 (R-86 finding 5); bounds the delivered threshold, not the largest lambda (R-84 n11)`
  - Its old note, about the 10^(−430) hand bound, is superseded. The two F-84 clauses are kept.

### Added (crosswalk/84-equality-layer.tsv, after rem:layer-threshold-size, in order of definition)

```
eq:layer-size-base	paper/reader/proofs/P-LL.md@392f69f4:56	P-LL, the remark: Lambda_4 bounded by B_m^(-m/(m-p))	merged verbatim from the confirmed proof P-LL; new key, cited only in rem:layer-threshold-size
eq:layer-size-c	paper/reader/proofs/P-LL.md@392f69f4:62	P-LL, the remark: lower bounds of ln C_(1,m)	merged verbatim from the confirmed proof P-LL; new key, cited only in rem:layer-threshold-size
eq:layer-size-taylor	paper/reader/proofs/P-LL.md@392f69f4:71	P-LL, the remark: Taylor's lower bound of M_m	merged verbatim from the confirmed proof P-LL; new key, cited only in rem:layer-threshold-size
eq:layer-size-edge	paper/reader/proofs/P-LL.md@392f69f4:77	P-LL, the remark: lower bound of env_C(1/2 + x)	merged verbatim from the confirmed proof P-LL; new key, cited only in rem:layer-threshold-size
```

### Added (crosswalk/95-standard-results.tsv, after thm:std-chebyshev, the chapter's last label)

```
thm:std-duffin-schaeffer	paper/reader/proofs/P-LL.md@392f69f4:114	P-LL, the result of the literature: [DS41] Theorem III (Duffin-Schaeffer)	merged verbatim from the confirmed proof P-LL with R-P-LL's nit n1 (p. 517 added to the citation; the range -1 <= x <= 1 of (19), not legible in the journal's text layer, stated from the proof's own display); p. 525 by page arithmetic, not read from the folio; [DS41] added to the opening paragraph's journal-page list
```

**The commit in the sources.** `392f69f4` is the only commit that holds proofs/P-LL.md, and HEAD's copy is identical
to it (checked with cmp). The nit-applied text exists in no commit, because the file is retired without a commit. So
the sources cite `392f69f4` with that commit's line numbers, and the notes name the nits applied. In the nit-applied
copy, the remark's equation keys sit one line lower (57, 63, 72, 78) and the theorem sits at 115.

### Verification (script `m-ll/xwcheck.py`; label definitions found with lint.py's DEF_RX)

```
84-equality-layer.tsv: 92 labels, 92 rows, 4 fields in every row: True, same keys in same order: True -> OK
95-standard-results.tsv: 63 labels, 63 rows, 4 fields in every row: True, same keys in same order: True -> OK
90-scope.tsv: 8 labels, 8 rows, 4 fields in every row: True, same keys in same order: True -> OK
```

The header row (label, source, source_name, note) is checked separately. Chapter 90's labels are unchanged. Chapter 98
defines no labels and has no crosswalk.

## 4. Check outputs (from the paper directory, after the `git rm`)

```
$ python3 lint.py --chapters
chapters: 62 file(s), 4584 label(s) defined, 0 hit(s)
$ python3 assemble.py --check
labels 4584, computations cited 0, problems 0
$ python3 -c "...in-memory assembled lint..."
[] 0
```

Before the merge the counts were 4579 labels, 0 hits, 0 problems and `[] 0`. The five new labels are the four
eq:layer-size-* keys and thm:std-duffin-schaeffer. `python3 assemble.py` without --check was not run.

## 5. Retirement and files

- **The proof file.** I ran `git rm -f proofs/P-LL.md`. The `-f` was needed because the nit-applied file differed from
  HEAD. The deletion is staged; the chapter and crosswalk edits are unstaged. Nothing is committed.
- **The copy.** The nit-applied text, the one merged, is kept as
  `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/reports/M-LL.P-LL.md`
  (md5 4d2208fa6f4a70749fda80f0842ab2fd). The pre-nit text is `392f69f4:research/warp-drive/paper/reader/proofs/P-LL.md`.
- **M-LL.diff.** `git diff HEAD` over the 7 touched paths: chapters 84, 90, 95 and 98, crosswalks 84 and 95, and
  proofs/P-LL.md as a deletion of the committed text.
- **M-LL.nits.diff.** The nits, from 392f69f4 to the merged text.
- **The scripts,** under `scratchpad/reader/m-ll/`: nits.py, blocks.py, place.py, check.py, xw.py and xwcheck.py.
  Snapshots taken before the merge are in `m-ll/before/`.

## 6. For the coordinator (outside this merge's edit list; not touched)

- **eq:layer-interpolation's crosswalk row** (84) still has an empty note. Its source is "EL L.5, A15", though the
  equation now defines C_(i,m) with 2^i T_(m−1)^(i)(1). The task named only the lemma's and the remark's rows. A note
  such as "M-LL: the Chebyshev constant (R4.5's C^DS) of P-LL@392f69f4:11" would complete it.
- **OUTLINE.md.** The writer's report asks to register the bibliography key DS41 and the exported key
  thm:std-duffin-schaeffer. Lint does not need it, since the label is defined in chapters/.
- **Stale copies of 10^(−430).** The review notes that STATUS.md:57 and INTEGRATION.md:960 and 1196 still say it, and
  PAPER.md (generated) stays stale until the next full assembly.
- **sec:layer-threshold's crosswalk note,** "certified numbers not carried, see rem:layer-threshold-size", is still
  accurate: the edition carries its own proved bound, not the source's certified figures at P*.
