# Handoff after the container restart (2026-11-14)

Bash could not start in the old session after a container restart. The SessionStart hook had appended the same Lean
environment block to that session's env file 209 times (about 130 KB), and the file is inlined into every bash call, over
the 128 KiB argument limit. `.claude/hooks/session-start.sh` now skips a block already present. A new session is needed
because the old session's env file cannot be trimmed.

## State

- Everything up to commit f38a4ee is pushed, and this commit adds the hook fix, this note and `notes/`.
- STATUS.md and INTEGRATION.md record every verdict and finding to date.
- The review and report files the open items need are copied into `notes/reviews/` and `notes/reports/`. The old
  scratch paths in STATUS.md and INTEGRATION.md (`/tmp/claude-0/.../scratchpad/reader/...`) no longer exist; read
  `notes/` instead.
- CONFIRMED this segment: chapters 25 and 26 (S06), 46, 48 and 65 (S27), 63, 70, 87, 81 (R5-81), 85 (R3-85, nits applied)
  and 82 (R4-82; its five wording nits still to apply, with the P-K82 merge).

## Interrupted by the restart: relaunch each, starting from the files as committed

Their partial, uncommitted edits were lost. Start every relaunched agent from the committed file.

1. F3-83: apply `notes/reviews/R2-83.md` (0 Major, 5 minor, 6 nits) to chapters/83-localised-data.md. m3 concerns
   chapter 81's W_0 and support clauses: check against chapter 81 as it stands. Then a confirming reading, R3-83.
2. F2-P-U71-IS: apply `notes/reviews/R2-P-U71-IS.md` (1 Major, 1 minor, 5 nits; exact replacement texts) to
   proofs/P-U71-IS.md.
   - F1: for 134 ≤ l ≤ 172, the two roots of P_l near a(x) are distinct (sign changes at l = 134, 135, no real root
     at l ≥ 136).
   - F2: the hκ > 70 roots are simple by conjugation, so drop the "at most 3".
   - No number moves: l_* = 50 and K_ι ≤ 52.
3. F-P-U71-SP: apply `notes/reviews/R-P-U71-SP.md` (1 Major, 5 minor, 10 nits) to proofs/P-U71-SP.md.
   - F1: the same root-distinctness gap.
   - F3: simple for hκ > 70.
   - F4: cite cor:iii-g3-3-1 (1) for the raise of 𝒮_(λ₀).
   - State K_ι ≤ 2 on Σ, with the texts' 52 and 101 also true, and l_* = L ∈ [39, 50], taking 50.
   - Rename the integer N, the λ in cor:sp-lstar and the moments 𝔪_k.
   - Cite IS only as: simple on Re ∈ [−101, 5], L ≤ 50, M ≤ 7.
4. R2-P-K82: confirming reading of proofs/P-K82.md (741 lines) after its fix round (`notes/reports/F-P-K82.md`; first
   review `notes/reviews/R-P-K82.md`). Check every use of chapters 81 and 82 as they now stand, and every merge anchor.
5. XW-1: crosswalk sweep. One row per label, in order. Chapter 95's crosswalk had 25 rows for 67 labels. Report only on
   82, 83 and 03. Retire proofs/P-C-lambda0.md if R-86 confirmed and all its labels live in chapters.

## Next after those

- Merge P-K82 into chapter 82 and its block into chapter 03, and apply R4-82's five nits (`notes/reviews/R4-82.md`).
  Then a confirming reading R5-82 of the merged chapter. F4-82's merge notes are in `notes/reports/F4-82.md`.
- When IS and SP are confirmed: one combined confirming reading of the five d-bound texts (proofs/P-U71-forward.md,
  P-U71-close.md, P-U71-assembly.md, P-U71-IS.md, P-U71-SP.md; `notes/reviews/R-P-U71-close.md` lists (IS) and (SP)).
  Then integrate them into chapters 71, 3 and the others listed in INTEGRATION.md.
  - Remove the statements that (SP) is missing (close 313-316, 339-340, 352; assembly 632, 636, 648-649).
  - The ten undefined s14 references in chapters 33, 34 and 71 should resolve here.
- Chapter 90 (scope, written last) and Appendix B (96-tables).
- Integration items in INTEGRATION.md: F-82's suggestions for chapter 7 line 230 and chapter 81 lines 976-980, renames,
  and a final lint sweep. Lint now shows 12 hits: the pending markers in 35 and 82, and ten undefined s14 keys.
- assemble.py, lint, render the PDF, final report to the author.

## Standing rules (from the author)

- Agents: model opus, general-purpose. No Workflow tool.
- Continue without pauses. Parallel readers are fine.
- Say "proved" or "confirmed" only after an independent line-by-line reader with every finding seated.
- Commit and push at every stop on branch ccr-66909215-gi0qa5 (PR #139). Use these trailers:
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and `Claude-Session: <the session URL>`.
- Formatting:
  - Lines are at most 121 characters.
  - No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".
  - Label keys are lowercase.
  - Never put '|' inside a STATUS.md cell.
- The paper contains no file names, program names, code or AI language, and every proof is written in full.
- Do not scan or cite method/, drive/, extracted/ or recovered/. Never write in the repository root.
- Kill processes only by exact PID. Use they/them for the author.
