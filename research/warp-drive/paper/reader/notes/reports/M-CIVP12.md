# M-CIVP12: merge of proofs/P-CIVP.md (Tier 1) and proofs/P-CIVP2.md (Tier 2)

Inputs, both CONFIRMED by notes/reviews/R-P-CIVP.md ("Second final"), pinned at commit 26195481:

- proofs/P-CIVP.md: md5 f8a1e948a7f9c53831719f5d526cc3a8, 1319 lines.
- proofs/P-CIVP2.md: md5 92d89d4073f20c8ac2c8cce587918dd9, 842 lines. The nit diff against df9a4c35 touches only lines
  123–125. Two lines became three, so every line after 125 moved by +1.

`git show 26195481:…` is byte-identical to both working files. Both md5s are unchanged after the merge. I did not edit,
delete or commit any file in proofs/.

**About commits.** I made no commit. While I worked, two snapshot commits by other agents took in my edits:
5de1a56b ("P-SHELL re-based on final Tiers 1-2 …") took the six chapter files, and 269aac10 ("Snapshot: work in
progress (merges, proof files)") took the five crosswalk files. To confirm that the committed content is exactly this
merge, I rebuilt it from a `git archive` of 26195481 with the same two scripts. Each of the 11 files is identical in the
rebuild, at HEAD and in the working tree. Between 26195481 and HEAD, no other change touches chapters/ or crosswalk/.

The diff is `git diff 26195481 HEAD` over the 11 files: 1929 insertions, 22 deletions, 15 hunks. It is saved as
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/reports/M-CIVP12.diff
(md5 26d40314002e91622bceeb483c1a9e61). A plain `git diff` is now empty, because the edits are committed.

## 1. Placement items

Before each replacement, a script checked the old text against the current state of the chapters. Each old text
occurred exactly once, as whole lines, in its own chapter and across all 62 chapters. Every old text was at the line the
files give, so no item stopped. Every new text and every inserted block was copied byte for byte from the pinned files.

After the merge:

- Each new text and block occurs exactly once in chapters/.
- No old text is left as whole lines.
- Item 11's fallback texts were not used.
- The optional loc- prefix of Tier 2's item 1 was not applied. The labels stay civp-large-*, as the reader's scratch
  merge also left them.

| Item | What | Old (HEAD 26195481) | New (now) |
|---|---|---|---|
| T1-1 | Block A (P-CIVP 6–95: lem:loc-cone-in … rem:loc-cone-scope), after the proof of prop:loc-cones, one blank before and after | after 83:591 | 83:598–687 |
| T1-2 | Block B (P-CIVP 97–1038), heading without "Block B. ", new section after sec:loc-cones | before 83:602 | 83:707–1648 |
| T1-3 | chapter opening paragraph (2 → 7 lines; also T2-2) | 83:8–9 | 83:8–14 |
| T1-4 | paragraph after prop:loc-cones, after Block A (8 → 17 lines; also T2-3) | 83:593–600 | 83:689–705 |
| T1-5 | ch:introduction, the part:further paragraph (3 → 4 lines; also T2-5) | 01:191–193 | 01:191–194 |
| T1-6 | ch:theorems, More families bullet (1 → 6 lines, indented two spaces; also T2-6) | 03:376 | 03:376–381 |
| T1-7 | ch:scope, last line of the localised-data paragraph (1 → 8 lines; also T2-4's second pair) | 90:210 | 90:211–218 |
| T1-8 | "Unchanged" | — | nothing to apply |
| T1-9 | Appendix A: no new entry | — | nothing to apply |
| T1-10 | references: [Ren90] after [Rac16], before [RS1] | after 98:157–158 | 98:159–161 |
| T1-11 | fallback texts for Tier 2 not merged | — | not used (both merged) |
| T2-1 | Tier 2 section (P-CIVP2 1–740, sec:civp-large … rem:civp-large-beyond), after Block B, before sec:loc-kid | before 83:602 | 83:1650–2389; sec:loc-kid heading now 83:2391 |
| T2-2, 3, 5, 6 | no separate change (sites of T1-3, T1-4, T1-5, T1-6) | — | — |
| T2-4 | ch:scope, opening sentence of the localised-data paragraph (first pair, 2 → 3 lines) | 90:201–202 | 90:201–203 |
| T2-7 | Appendix A, thm:std-cctw-existence and thm:std-cctw-strips before thm:std-ctg-neighbourhood, one blank after each | before 95:467 | 95:467–488 and 95:490–496; thm:std-ctg-neighbourhood now 95:498 |
| T2-8 | references, [CCTW16] (3 → 3 lines: volume 515, pp. 1–67) | 98:26–28 | 98:26–28 |
| T2-9 | crosswalk rows (see section 2) | — | — |

The chapter edits are identical to the reader's scratch merge (scratchpad/rpcivp3/chapters). The one difference is
P-CIVP2's applied nit (u1 = 5.7, u2 = 7.2), now at 83:1772–1774.

**New labels: 70, each defined once.**

- Chapter 83, Block A (5): lem:loc-cone-in 598, eq:loc-cone-in 603, thm:loc-cone-development 629,
  eq:loc-cone-domain 641, rem:loc-cone-scope 670.
- Chapter 83, Block B (31): sec:loc-cone-proof 707 through rem:loc-cone-local-scope 1616.
- Chapter 83, Tier 2 (32): sec:civp-large 1650 through rem:civp-large-beyond 2373.
- Chapter 95 (2): thm:std-cctw-existence 467, thm:std-cctw-strips 490.

**Assembled numbering.**

- Lemma 53.8 is lem:loc-cone-in, Theorem 53.9 is thm:loc-cone-development and Remark 53.10 is rem:loc-cone-scope.
- Section 53.4 is sec:loc-cone-proof, with subsections 53.4.1–53.4.4.
- Section 53.5 is sec:civp-large, with subsections 53.5.1–53.5.5 and Theorem 53.38 (thm:civp-large).
- sec:loc-kid moves from 53.4 to 53.6, and each later section of the chapter moves by two.
- Theorems A.21 and A.22 are the two CCTW16 entries, so thm:std-ctg-neighbourhood is now A.23.
- All of these numbers resolve from labels. No chapter source hard-codes a result number of ours.

## 2. Crosswalk

**Pin.** Every source is paper/reader/proofs/P-CIVP.md@26195481:N or paper/reader/proofs/P-CIVP2.md@26195481:N, where N
is the line that carries the `{#label}` in `git show 26195481:…`. I recomputed every N that way. Tier 1's PENDING
numbers all equal those lines. Tier 2's lines after 125 are the post-nit lines, for example lem:civp-large-frame at 198
and rem:civp-large-beyond at 724. No crosswalk file contains "PENDING".

**New rows (70).**

- crosswalk/83-localised-data.tsv:22–89, after prop:loc-cones (21) and before sec:loc-kid (now 90):
  - Tier 1's Rows 1–36 (lines 22–57). Each was parsed from P-CIVP's "Crosswalk rows" section and split on "; " into
    label, source, source_name and note, the note keeping any later "; " (Rows 14 and 36). The sentence-final full stop
    was dropped. Rows 27, 29, 30 and 32 have no note and end with an empty fourth field.
  - Tier 2's 32 rows (lines 58–89). P-CIVP2 gives no row texts, only its item 9 ("one row for each label listed in
    item 1"). So I wrote source_name as "proof P-CIVP2, <kind> (<title>)" and a short note, in Tier 1's style, from
    each result's statement.
- crosswalk/95-standard-results.tsv:29–30: thm:std-cctw-existence (source @26195481:795) and thm:std-cctw-strips
  (@26195481:818). They sit after sec:std-characteristic (28) and before thm:std-ctg-neighbourhood (now 31). Their
  source_name and notes are also mine, and the notes carry "(P-CIVP2 text 7)".

**Changed cells on existing rows (6 rows).** These follow P-CIVP's "Existing 1–6" texts, with a "(P-CIVP text N)" or
"(P-CIVP2 text N)" tag by item number.

- 83-localised-data.tsv:2, ch:localised-data:
  - Source: "; paper/reader/proofs/P-CIVP.md@26195481:1069" appended.
  - Note: "; the sentence on the developments from the two null cones (thm:loc-cone-development, thm:civp-large),
    merged text of proofs P-CIVP and P-CIVP2 (P-CIVP text 3)" appended.
- 83-localised-data.tsv:16, sec:loc-cones:
  - Source: "; …P-CIVP.md@26195481:1" appended.
  - Note: the note was empty and is now "Block A of proof P-CIVP added after prop:loc-cones: lem:loc-cone-in,
    thm:loc-cone-development, rem:loc-cone-scope (P-CIVP text 1)".
- 83-localised-data.tsv:21, prop:loc-cones:
  - Source: "; …P-CIVP.md@26195481:1084" appended.
  - Note: replaced, not appended, by Existing 3's text plus "(P-CIVP text 4)". The old note ended "the closing
    paragraph names what is lost for cone data with dust (item m4; no development asserted)". That is false after the
    merge, and P-CIVP gives the whole new note. See section 3.
- 01-introduction.tsv:10, sec:organisation: note: "; the entry for ch:localised-data names the development from two null
  cones (proof P-CIVP) (P-CIVP text 5)" appended.
- 03-theorems.tsv:22, sec:further-results: note: "; the More families bullet names the developments from the two null
  cones (thm:civp-large, thm:loc-cone-development), merged text of proofs P-CIVP and P-CIVP2 (P-CIVP text 6)" appended.
- 90-scope.tsv:7, sec:scope-families: note: two pieces appended:
  - "; the paragraph on localised data ends with the developments from the two null cones (thm:civp-large,
    thm:loc-cone-development, rem:loc-cone-scope), merged text of proofs P-CIVP and P-CIVP2 (P-CIVP text 7)";
  - "; its opening sentence names data of any size on the two null cones through the corner sphere (P-CIVP2 text 4)".
    I added this one because P-CIVP2's item 4 changes that paragraph and gives no crosswalk text.

Chapter 98 has no crosswalk and no labels, so [Ren90] (P-CIVP text 10) and [CCTW16] (P-CIVP2 text 8) have no row.

## 3. Judgement calls (for the coordinator)

1. **prop:loc-cones note replaced.** The brief says to append notes. I followed P-CIVP's Existing 3, which gives the
   whole new note, because appending would leave "no development asserted" next to "states the developments". If the
   old wording should be kept as history, it is the cell shown above.
2. **Tier 2 row texts written by me.** Item 9 of P-CIVP2 asks for one row per label but gives no texts. The 32 + 2
   source_name and note cells are therefore my wording. The labels and pinned lines are exact.
3. **"(proof P-CIVP) (P-CIVP text 5)".** Existing 4's own text ends "(proof P-CIVP)". I kept it verbatim before the
   tag, so the cell has two parentheticals in a row.
4. The new rows keep the files' working names "Tier 1/Tier 2 of the scoping report" and "the statement T1" (Rows 3, 35
   and sec:civp-large). This is only in crosswalk/, a working file, and nowhere in the chapters.

## 4. Checks

Live tree (note: another merger is now working on chapters 33/34; at the time of these runs `git status` was clean, so
the live tree equals HEAD):

- `python3 lint.py --chapters`: "chapters: 62 file(s), 4735 label(s) defined, 0 hit(s)". Before the merge it was 4665.
- `python3 assemble.py --check`: "labels 4735, computations cited 0, problems 0". PAPER.md was not rewritten (md5
  ed137936047ddf5c5bd45a2fe9fe4fa3 before and after).
- In-memory assembled check: `[] 0`.

Isolated copy, to rule out interference from chapters 33/34: `git archive 26195481` plus only this merge, rebuilt by the
same scripts, at scratchpad/mcivp/regen/research/warp-drive/paper/reader. The same three results: 4735 labels and 0
hits, 0 problems, `[] 0`.

**Label counts.** 4665 → 4735 (+70). Chapter 83: 159 → 227. Chapter 95: 64 → 66.

**Crosswalks.** Every crosswalk file has one row per `{#label}` of its chapter, in chapter order, each row with exactly 4
tab-separated fields, and no "PENDING" anywhere. Touched: 01 (9/9), 03 (21/21), 83 (227/227), 90 (8/8), 95 (66/66).
Across all chapters, 0 files mismatch.

**Line length.** No line of any chapter source and no line of the assembled, label-resolved text (101,216 lines) is
over 121 characters. Both trees were checked.

**Line starts.** Lines that continue a paragraph were checked for a start of "+ ", "- ", "* ", "> ", "#", "=" or "|".

- Chapter regions 01:190–195, 03:375–382, 83:7–15 and 83:595–2392, 90:200–219 and 95:465–498: no hit.
- Chapter 98: the only hits are the bibliography's own "- [Key]" entries, which are intended list items. The
  continuation lines of [Ren90] and [CCTW16] start with two spaces and text.
- Assembled new region (75663–77456): no hit.
