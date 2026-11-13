# The reader's edition: master outline

Working file. The order of the edition is the order of the chapter files' names in `chapters/`. Every key below is
**exported**: the chapter named defines it, and any chapter may cite it. A chapter defines its other labels freely.
The source map for each chapter is `maps/outline-M.md` (main argument and further results; section 4 for the chapter's
entry, section 2 for how its final text is composed, section 3 for what is dropped) or `maps/outline-S.md` (the stability
theory).

## Parts and chapters

| file | part / chapter key | content (outline entry) |
|---|---|---|
| 00-front.md | — | title, subtitle, author line, abstract |
| 01-introduction.md | part:statements, ch:introduction | M Ch 1 |
| 02-setting.md | ch:setting | M Ch 2 |
| 03-theorems.md | ch:theorems | M Ch 3 |
| 04-approximant.md | part:approximant, ch:approximant | M Ch 4 |
| 05-inequalities.md | part:existence, ch:inequalities | M Ch 5 |
| 06-uniform-existence.md | ch:uniform-existence | M Ch 6 |
| 07-data.md | ch:data | M Ch 7 |
| 08-horizon-mass.md | part:remaining, ch:horizon-mass | M Ch 8 |
| 09-past-construction.md | ch:past-construction | M Ch 9 |
| 10-bondi.md | ch:bondi | M Ch 10 |
| 20-…59-…md | part:stability, chapters of the stability theory | outline-S (keys fixed when it reports) |
| 60-after-shell.md | part:settling, ch:after-shell | M Ch 11 |
| 61-interior.md | ch:interior | M Ch 12 |
| 62-own-data.md | ch:own-data | M Ch 13 |
| 63-rw-gauge.md | ch:rw-gauge | M Ch 14 |
| 64-harmonic-structure.md | ch:harmonic-structure | M Ch 15 |
| 65-harmonic-rate.md | ch:harmonic-rate | M Ch 16 |
| 70-resolvent-bounds.md | part:constants, ch:resolvent-bounds | M Ch 17 |
| 71-explicit-constants.md | ch:explicit-constants | M Ch 18 |
| 80-two-dusts.md | part:further, ch:two-dusts | M Ch 19 |
| 81-class-system.md | ch:class-system | M Ch 20 |
| 82-vlasov.md | ch:vlasov | M Ch 21 |
| 83-localised-data.md | ch:localised-data | M Ch 22 |
| 84-equality-layer.md | ch:equality-layer | M Ch 23 |
| 85-equality-edge.md | ch:equality-edge | M Ch 24 |
| 86-lambda0.md | ch:lambda0 | M Ch 25 |
| 87-ten-l5.md | ch:ten-l5 | M Ch 26 |
| 90-scope.md | ch:scope | M Ch 27 |
| 95-standard-results.md | app:standard-results | M Appendix S1: results of the literature used, exact statement, page |
| 96-computations.md | app:computations | generated: the {{APPENDIX-A}} placeholder |
| 97-code.md | app:code | generated from the cleaned programs |

## Exported results (the chapter named defines each with `{#key}`)

Chapter 3 (the theorems; proofs elsewhere):
{#thm:main} Theorem 1 of the record (uniform existence on D_T, the weak limit, items 1–7).
{#thm:past-construction} Theorem 2 (the construction from past null infinity).
{#thm:bondi-law} Theorem 3 (the five-dimensional Bondi mass law at past null infinity).
{#thm:settling} Theorem 4 (settling of glued data to Schwarzschild–Tangherlini).
{#prop:boundary-spacelike} Proposition 3.2 of the record (x_K = 1 spacelike, margin for g_λ).
{#prop:one-zero} Proposition 3.3 (one zero per column of the spheres' outgoing expansion).
{#prop:mean-mass} Proposition 3.4 (the mean mass).

Chapter 4: {#thm:approximant} the record's Theorem A (the approximant to every order).
Chapter 6: {#thm:uniform-existence} the record's Theorem E.
Chapter 7: {#thm:data} the record's Theorem D (exact data within O(λ^K) of the approximant).
Chapter 9: {#thm:past-approximant} Theorem A_P; {#prop:past-items} Proposition 9.10 (items 6–7 for Theorem 2's
solutions).
Chapter 10: {#lem:every-order-fixed} Lemma 11.0 (every order at fixed λ); {#prop:bondi-hierarchy} Proposition 11.1.
Chapter 61: {#prop:interior} BEYOND5 Proposition 6.2 (the development continues inside to the curvature boundary).
Chapter 62: {#thm:own-data} SETTLE-GLAM5 Theorem R5.1 (g_λ's own data settle, half-integer class, no gluing).
Chapter 63: {#thm:rw-settling} GAUGEDECAY5 Theorem 1.5 (settling in the Regge–Wheeler-type gauge).
Chapter 65: {#thm:harmonic-rate} the harmonic-gauge representative and its rate τ^(−min(p,3/2)+ε).
Chapter 71: {#thm:loss-d} the loss d and the regularity N = 21d + 6, with the explicit figures.
Chapter 80: {#thm:two-dusts} Theorem E_2 (two crossing dusts).
Chapter 81: {#thm:class-stability} Cauchy stability of the class Einstein–null-dust system (Theorem N′).
Chapter 82: {#thm:vlasov} Theorem V (restricted massless Vlasov limits).
Chapter 83: {#thm:charge-sign} the sign of the charge of exactly localised data (inside and outside the horizon).
Chapter 84: {#thm:layer} Theorem L and {#cor:layer} Corollary L.7.
Chapter 85: {#thm:very-edge} Theorem L_1E‴ (one theorem, one proof).
Chapter 86: {#prop:lambda0} the certified bounds on λ0 and the computed M_22.
Chapter 87: {#thm:ten-l5} existence at 10 l5 where the solution is the seed, and why not beyond.

## Computation keys

A computation is cited as `[[C:key]]`, where key is the program's file name without `.py`, lowercased, with `_`
replaced by `-` (`checks/support5c.py` → `[[C:support5c]]`, `lemmas/hf_theorem5.py` → `[[C:hf-theorem5]]`). All the
labelled items of one program are one computation. The assembler numbers computations by first citation.

## Notation fixed for the whole edition (from outline-M section 5.4)

- N: the number of stages of the approximant only. The Nash–Moser regularity is written N_NM = 21d + 6.
- θ: the phase. The polar angle is ϑ.
- μ0: the seed's mass. The black-hole parameter of the stability theory is written m (with ϖ_K where the record does).
- λ: the wavelength only. The spectral parameter is σ; an indicial root is written ι (or as the source names it, with
  the name kept consistent within its chapter and declared at first use).
- K: the Kretschmann scalar. The approximant's order is written K_ord where it would collide; the mass change of the
  gauge chapters is written K* as in the source.
- Results named by letters in the record (Theorems A, D, E, P, M, L, Q, T, X, V, N, K; Lemma A; Proposition L) get
  edition numbers only; a chapter may say once, in words, what a result does, never its record letter.
