# F3-P-TR: fix round after R2-P-TR

- **File:** proofs/P-TR.md, now md5 **20e494d7c5d171be7b1aa6b1ca3f9880**, 920 lines. It was 48074b35…, 924 lines.
- **Base:** HEAD 9d133b0c, whose chapters are those of ebc73adf. P-I11, P-UB1 and P-UB2 are merged there.
- **Repository:** no chapter edited, nothing committed.

## What changed

The required findings (m1–m8 and nits 1, 4–8) use the reader's exact texts.

- **m1** (prop:tr-fail): the hypothesis ε_ind(h) < 1.99·10⁻²⁸ is back at the front of the statement. The proof now reads 5Θ_g + Θ_η < 10⁻²⁷ + δ̄ < 2.1·10⁻⁸.
- **m2** (proof of (iii)): the rows that 1 + 𝒵 adds are now described by their exponents λ ∈ Λ ∖ Λ_ℬ, which have real part above 2 + 1.4646·10⁻¹⁰ (prop:tr-lambda (a)).
- **m3** (proof of (iii)): cor:is-flat is removed from the list of results "fixed by the gauge".
- **m4–m6** (state only what is proved):
  - (a)–(d) now carry over "in the form in which the proof uses them", in the opening, in rem:tr-scope and in text 3.
  - The claim about admissible points near h_μ becomes: μ(h) → 0 and the lower bound tends to infinity. This is in the opening, in text 4 and in crosswalk row 28.
  - "the count grows like h^(−1/2)" becomes a bound on the count, in the opening, in text 2 and in crosswalk row 4.
- **m7**: text 5 now has the range γ_C ≤ 2.1 × 10¹⁰ and the exclusion of a small set. Text 6 restores h ≥ 4.76 × 10⁻¹¹, the excluded set and "for d and N_NM".
- **m8**: texts 2, 3, 4 and 6 now define or cite κ (as l(l + 2)), Λ, N_Λ and μ(h), and describe μ(h) as in def:tr-excess.
- **nit 1** (rem:tr-scope): rewritten in the reader's text.
- **nit 4**: the square of the h-bound now replaces 10⁻¹² in the F₃ term.
- **nit 5**: the first reading's nit 11 is finally applied: the factor 1/x is taken at the left end.
- **nit 6**: "at least 3 + ε_Υ".
- **nit 7** (placement):
  - All items are now against HEAD; no proof-file names or commit 8d583306 remain.
  - Line numbers: item 1 at 5499, item 8 at 5491.
  - Item 1 names the results it uses.
- **nit 8**: crosswalk notes for rows 1, 4, 27 and 28. All 28 PENDING pins re-pinned and checked against their label lines.

The three optional nits are all applied:

- **nit 2:** def:tr-excess adds "Z₃(h) is finite at every such h ([[prop:np-10-54]] (iii)), so μ(h) is a positive minimum and N̄(h) is defined". I dropped "(Z₃(h) finite)" from the display, since it now always holds.
- **nit 3:** in (iii), min(μ(h), 10⁻¹³) becomes μ(h). The proof's chain reads 0 < ε_K < ε_+ < μ(h) ≤ μ_G < ε_Υ ≤ ε_ind.
- **nit 9:** the proof of (iii) adds "and 𝒵 ⊂ {Re > 1}, which holds at every h ([[prop:iii-f1-2-3]] (a))".

## Delta against the reader's fixed copy

The body differs from P-TR-fixed2.md only by the three optional nits.

The placement differs because the reader's copy left it stale and nit 7 asks for it to be redone:

- the preamble names no proof files;
- the line numbers are those at HEAD;
- item 1 lists its sources;
- items 3, 4 and 8 have no notes about proof files.

The New texts of items 2–8 are the reader's (2–6) or unchanged (7–8).

## Checks

- **Scratch merge** of HEAD + P-TR:
  - `lint.py --chapters`: 62 files, 4956 labels, 0 hits;
  - `assemble.py --check`: 0 problems;
  - longest new line after label resolution: 121 characters.
- **Numbering in the assembled paper:** sec:tr is Section 49.15, thm:tr-transfer Theorem 49.128, eq:tr-split (49.67), prop:tr-mu-small Proposition 49.142.
- **Old texts:** each occurs exactly once at HEAD. Item 1 is at 5499, item 2 at 30, item 3 at 85–86, item 4 at 1820–1821, item 5 at 364 of chapter 3, item 6 at 81 of chapter 90, item 7 at 4535–4537 of chapter 33, and item 8 at 5491.
- **The file:** lines are at most 121 characters, also after label resolution. No bad wrap starts, no backslash, lowercase labels. The style lint flags only the crosswalk file locations and labels that live in other files.
