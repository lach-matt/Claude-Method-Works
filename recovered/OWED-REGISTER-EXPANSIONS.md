# Owed REGISTER expansions — workshop that is subject-matter proof-of-work

Standing distinction (M, this session): some workshop cut from the reader prose is NOT mere
editorial/process residue for the working record — it is subject-matter proof-of-work on the
mathematics (how a result was reached, what was tried and withdrawn, what the correct method turned
out to be). That material is owed to the **subject-matter Register** (the canonical append-only record),
because the Register exists precisely to show thought-process and proof-of-work for the book's subject.

CRITICAL governance guard (Ruling 27 / project rules):
- The subject-matter Register holds SUBJECT MATTER only, append-only, never edited/relocated/renumbered.
- Reader-perspective audits and EDITORIAL/production findings go to WORKING-REGISTER.md, never here.
- This file tracks the FORMER: subject-matter workshop (seed derivations, method corrections that are
  themselves findings about the mathematics) owed as NEW register entries that CITE, never overwrite.
- A withdrawn result is corrected by a NEW entry citing the old, not by removing anything.
- These are DRAFTED as reader prose cuts now; the actual register entries are authored when the pass
  reaches the Register (M closes with it last). This file is the queue so nothing is lost.

Token series for reader-prose flags: [REG-NN] is NOT placed in reader prose (the reader never sees a
register self-citation — that is the whole point of the cut). Instead each cut is logged here with the
source §, the surviving reader claim it supports, and the subject-matter content owed to the Register.

## Batch from source Chapter 14 "Closure" — subject-matter workshop owed to the Register
| # | source § | reader claim it supports (kept in prose) | subject-matter proof-of-work owed to Register |
|---|---|---|---|
| R-01 | §14.5.1, §14.5.9 | Λ is the closure of seven cells (exact) | The route from greedy upper bounds (12/11/12) to the exact minimum: seed as MINIMUM SET COVER (elements = envelope steps, sets = cells); why prune-greedy overcounts (fits its own failures); branch-and-bound gives 7; the spread across heuristics (prune 12, cover 7, reverse-delete 40, LB 5, exact 7 → spread 33) as the quantity that reports algorithm quality. Cites the superseded greedy figures rather than deleting them. |
| R-02 | §14.5.8, §14.5.9 | a counting axis costs the seed about one cell; a coupling axis costs more (the seed reads the dichotomy) | The full withdrawn-and-corrected chain: the prune-greedy per-axis numbers (+1 counting / +10 coupling / cost=a+κ / κ=S/4−1 at r=0.980) WERE the heuristic's difficulty, not the index's cost; under set cover a two-parent axis costs ~1–2, same as one-parent; refit gives coefficient −0.079 at rms 0.999. The parent-count-drives-cost reading is withdrawn; what SURVIVES is the counting/coupling asymmetry read through the seed. This is the untangling (see reader §14.5.8 treatment). |
| R-03 | §14.5.8 | seed = Carathéodory number + alphabet cost; linear in dimension | The Carathéodory identification: breadth of a product of d chains is d; a generating set must reach the breadth; the coefficient "was in the bibliography, glossed and left"; the two bibliography gaps step 2 of the cycle found (Carathéodory never cited though Helly was). Prior-art provenance as proof-of-work. |
| R-04 | §14.1 | Theorem 14.1: X closed iff X = ℛ(X), with prior owners | The mis-citation correction: Freuder 1982 (backtrack-free search, width w, strong (w+1)-consistency) is a DIFFERENT theorem than Dechter 1992 (local→global at strong (w*+1)-consistency); the book had been citing Freuder for Dechter's result. Correction is itself a subject-matter finding about provenance. |
| R-05 | §14.5.10, §14.5.11 | four corner cells appear in every sampled seed but NONE is forced; the constraint is on the channel | The erasure-code false start ("unreconstructible core") withdrawn; nothing is forced (0 uniquely-covered envelope elements at every cap and at Λ₉); 519 completions from 66 cells, heavy-tailed (min3/med12/max157); the conditional-misread-as-necessity correction. |
| R-06 | §14.6.3 | (not carried to reader — pure register content) | The mathematics register's own state: object counts across builds, the five-component graph (main 162, modular chain 9, two fragments, B.nuV isolated), what is unfinished and why (six modular objects await two unread sources). This is register-about-register; author as the register's self-description where appropriate, NOT reader prose. |