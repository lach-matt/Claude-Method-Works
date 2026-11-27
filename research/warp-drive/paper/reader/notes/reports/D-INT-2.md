# D-INT-2: the d-bound proofs merged into chapter 71

Built from chapter 71 and the six proof texts at d1509feb (identical to HEAD). The plan followed is R-DB-2 §7, CH-71
(a)–(f). Nothing is committed.

## Section order (4371 lines)

- 1–27: opening
- 29–51: sec:ec-point
- 53–136: sec:ec-gap-sums
- 138–352: sec:ec-accounted
- 354–1248: **sec:fwd** (forward 6–866 at 354–1214), then rem:ec-other-losses and its paragraph (1216–1248)
- 1250–1294: sec:ec-floor
- 1296–1479: **sec:ec-gauge-gap** (assembly 1–184): new prop:ec-rounds at 1380, new thm:loss-d at 1422
- 1481–1509: sec:ec-delta heading, then assembly 186–212 (new prop:ec-delta-cap and its paragraph)
- 1511–1931: **sec:ec-upper** (assembly 214–634)
- 1933–2506: **sec:uc-close**
- 2508–3169: **sec:is**
- 3171–3774: **sec:sp**
- 3776–4301: **sec:cs**
- 4303–4371: sec:ec-linear

## Deleted

- The old prop:ec-rounds and thm:loss-d (old lines 435–517).
- The old prop:ec-delta-cap and the paragraph after it (old lines 521–544).
- sec:ec-integer, with rem:ec-weights-observed and rem:ec-integer-bound (old lines 546–596). No other text cited them.
- The forward text's two comments: lines 1–4, and lines 868–899 (texts 7–12).

## Sentences changed

1. **Opening, old lines 12–22.** Replaced by the CH-71 (b) text, verbatim except one change: "([[thm:fwd-loss]])" →
   "([[thm:fwd-loss]], [[cor:fwd-near-b0]])". R-DB-2 wrote its text before cor:fwd-near-b0 existed (R-DB-1 F2,
   R2-DB-b). Also from (b): "bound λ1 by δ, and the modulus" → "bound λ1 by δ, δ by a power of 2 that decreases with
   d, and the modulus".
2. **rem:ec-point-outside.** "and so does the lower bound of [[thm:loss-d]] (see its proof)." → the (c) text, verbatim.
3. **rem:gap-sums.**
   - "No other result of this paper uses [[prop:gap-sums]]." is false after the merge. New: "Besides this remark,
     [[cor:is-flat]] uses [[prop:gap-sums]], and [[lem:ec-gauge-gap]] and [[lem:sp-roots]] use the bounds on the
     offsets that its proof gives."
   - The (d) sentence on μ_G follows, verbatim.
4. **The paragraph after rem:ec-other-losses (old lines 373–387).** The (e) text is used, with two changes.
   - "raises by 6; there d = D_0 + D_1 + d′ + d″ ([[eq:ii-f1-3-3]]), and" → "in the relaxed form of
     [[rem:ii-f1-7-1]] with d_ℵ = 1 and raises by 5; there d = D_0 + D_1 + d′ + d″ + 1 + 5 ([[eq:fwd-split]]),". This
     matches sec:fwd and chapter 38.
   - Added: "and [[cor:fwd-near-b0]] gives the same value at every base point with black hole parameter in ℬ̄_*."
5. **Line 4348.** "β_0^Γ = 2" → "β_Γ = 2". This was the only site.
6. **rem:ec-not-evaluated.** "bounds λ1 by δ and the modulus at 2δ" → "bounds λ1 by δ, δ by a power of 2 that
   decreases with d, and the modulus at 2δ", as in the opening. The paragraph is rewrapped.

A grep finds none of the following left: "No upper bound", "raises by 6", 7.959, 1.671, 2.6532, 7.666, 46,236, 8.41,
"is an observation", ec-integer. The bound 1.403·10²⁰ remains only where it holds: in (b), beside 1.2497·10²⁴, and in
the merged thm:loss-d and prop:ec-delta-cap.

## Byte comparison

/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/d_int_2/compare.txt

- All eight merged blocks are **IDENTICAL** to their source ranges at d1509feb.
- No heading level had to change.
- No sentence inside any block changed.
- The diff of the chapter lines outside the blocks shows exactly the changes listed above, the deletions, and the blank
  lines between blocks.

## Checks

- lint, chapter 71 alone: 1366 hits. All are cross-chapter "undefined label", which is expected; there is no style
  hit.
- lint --chapters: 62 files, 4573 labels, **0 hits**.
- assemble --check: **problems 0**. R-CO's 6 undefined references now resolve.
- Longest line is 121 characters.
- No wrapped line has a forbidden start.
- All labels are lowercase, and none is defined twice.

## Counts

- Chapter: 665 → 4371 lines.
- Labels: 36 → 203: 6 removed, 173 merged (3 of them replace old labels).
- Labels by kind: ch 1, sec 41, def 9, lem 56, prop 18, thm 8, cor 4, rem 15, eq 51.
- Crosswalk:
  - 203 rows. Their sequence matches the chapter's label order (checked by diff).
  - Merged rows use source "…/P-U71-<name>.md@d1509feb:<label line>" and source_name "d-bound proof <name>, <kind>
    (<title>)".
  - The 6 deleted labels have no rows.
  - The six kept rows whose text changed have extended notes.
- The six proofs/P-U71-*.md files are git-rm'd (staged).

## For the coordinator

1. **Placement of sec:fwd.** The placement comment says "before that remark", so rem:ec-other-losses and its
   paragraph now fall under sec:fwd's last subsection, sec:fwd-box. Alternative: move sec:fwd to just before
   sec:ec-floor, and change "the next section" to "[[sec:ec-floor]]".
2. **sec:ec-gauge-gap** contains the new prop:ec-rounds and thm:loss-d, as the assembly laid them out.
3. **Line 26 is kept.** It says no result of this chapter is used in a proof. Chapters 23 and 62 cite chapter 71 only
   for explicit values and for the identity of d.
