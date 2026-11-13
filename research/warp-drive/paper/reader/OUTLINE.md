# The reader's edition: master outline

Working file. The order of the edition is the order of the chapter files' names in `chapters/`. Every key below is
**exported**: the chapter named defines it, and any chapter may cite it. A chapter defines its other labels freely.
The source map for each chapter is `maps/outline-M.md` (main argument and further results; section 4 for the chapter's
entry, section 2 for how its final text is composed, section 3 for what is dropped) or `maps/outline-S.md` (the stability
theory).

## Parts and chapters

| file | part / chapter key | content (source-map entry) |
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
| 20-s01-spectral-bounded.md | part:stability, ch:s01 | S1 |
| 21-s02-spectral-high.md | ch:s02 | S2 |
| 22-s03-spectral-low.md | ch:s03 | S3 |
| 23-s04-compactified.md | part:stability-analysis, ch:s04 | S4 |
| 24-s05-dynamics.md | ch:s05 | S5 |
| 25-s06-regularity.md | ch:s06 | S6 |
| 26-s07-energy.md | ch:s07 | S7 |
| 27-s08-iota-normal.md | ch:s08 | S8 |
| 28-s09-forward.md | ch:s09 | S9 |
| 29-s10-nash-moser.md | ch:s10 | S10 |
| 30-s11-myers-perry.md | part:stability-linear, ch:s11 | S11 |
| 31-s12-mp-dynamics.md | ch:s12 | S12 |
| 32-s13-gauge-potential.md | ch:s13 | S13 |
| 33-s14-constraint-damping.md | ch:s14 | S14 |
| 34-s15-linearised.md | ch:s15 | S15 |
| 35-s16-iota-plus.md | ch:s16 | S16 |
| 36-s17-null-infinity.md | ch:s17 | S17 |
| 37-s18-augmented.md | ch:s18 | S18 |
| 38-s19-forward-cone.md | part:stability-forward, ch:s19 | S19 |
| 39-s20-boost.md | ch:s20 | S20 |
| 40-s21-parameters.md | ch:s21 | S21 |
| 41-s22-kerr-face.md | ch:s22 | S22 |
| 42-s23-augmentation.md | ch:s23 | S23 |
| 43-s24-tame.md | ch:s24 | S24 |
| 44-s25-base-points.md | ch:s25 | S25 |
| 45-s26-exterior.md | part:stability-nonlinear, ch:s26 | S26 |
| 46-s27-nonlinear.md | ch:s27 | S27 |
| 47-s28-gluing.md | ch:s28 | S28 |
| 48-s29-linear-stability.md | ch:s29 | S29 |
| 60-settling-proof.md | part:settling, ch:settling-proof | S30 (the proof of thm:settling) |
| 61-after-shell.md | ch:after-shell | M Ch 11 |
| 62-interior.md | ch:interior | M Ch 12 |
| 63-own-data.md | ch:own-data | M Ch 13 |
| 64-rw-gauge.md | ch:rw-gauge | M Ch 14 |
| 65-harmonic-structure.md | ch:harmonic-structure | M Ch 15 |
| 66-harmonic-rate.md | ch:harmonic-rate | M Ch 16 |
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
| 95-standard-results.md | app:standard-results | M Appendix S1 |
| 96-tables.md | app:tables | Appendix B: coefficient tables the written proofs use (ruling of 2026-11-13) |
| 98-references.md | — | the bibliography (unnumbered) |

Part titles: part:statements "Introduction and statements"; part:approximant "The approximant"; part:existence
"Uniform existence"; part:remaining "The horizon, the construction from past null infinity and the mass law";
part:stability "The stability theory, I: the spectral family on bundles"; part:stability-analysis "The stability
theory, II: analysis on the compactified spacetime"; part:stability-linear "The stability theory, III: the
Myers–Perry family and the linear theory at low energy"; part:stability-forward "The stability theory, IV: forward
solutions and their asymptotics"; part:stability-nonlinear "The stability theory, V: the exterior, the nonlinear
theorem, gluing and linear stability"; part:settling "Settling at late times"; part:constants "Explicit constants";
part:further "Further results".

## Canonical keys for results of the sources

Writers work in parallel, so a result cited across chapters gets a key derived mechanically from its name in the
source; the chapter that carries the result defines exactly that key, and every other chapter cites it.

- Stability theory: `<kind>:<part>-<number>` where kind is thm, lem, prop, cor, def, rem or eq (sec for a section),
  part is outline-S's name of the part lowercased with "." and "(" ")" removed and roman numerals kept (I.A → i-a,
  II.A1 → ii-a1, II.F1 → ii-f1, III.D2 → iii-d2, III.I(15) → iii-i15, IV → iv, IV(3) → iv3, VI.B1 → vi-b1,
  VI.C → vi-c, VII → vii, IX → ix), and number is the result's number with "." replaced by "-". Examples: III.K
  Theorem 4.3 → `thm:iii-k-4-3`; III.D1 Lemma 2.1 → `lem:iii-d1-2-1`; III.B (3.6) → `eq:iii-b-3-6`; II.G Theorem
  2.1 → `thm:ii-g-2-1`. A prime is spelt out: I.B Corollary 4.6′ → `cor:i-b-4-6-prime` (two primes: `-prime2`).
- The main proof's section 10 items carried into the stability chapters: `<kind>:np-10-<n>[-<item>]`, for example
  NP 10.17 (ii) → `prop:np-10-17-ii`. The chapter carrying it is the lowest-numbered stability chapter whose entry in
  outline-S lists it; the others cite it.
- Where OUTLINE.md assigns an exported key (thm:main, thm:settling, ...), that key is used instead.

## Exported results (the chapter named defines each with `{#key}`)

Chapter 3 (the theorems; proofs elsewhere):
{#thm:main} Theorem 1 of the record (uniform existence on D_T, the weak limit, items 1–7).
{#thm:past-construction} Theorem 2 (the construction from past null infinity).
{#thm:bondi-law} Theorem 3 (the five-dimensional Bondi mass law at past null infinity).
{#thm:settling} Theorem 4 (settling of glued data to Schwarzschild–Tangherlini); proved in file 60.
{#prop:boundary-spacelike} Proposition 3.2 of the record (x_K = 1 spacelike, margin for g_λ).
{#prop:one-zero} Proposition 3.3 (one zero per column of the spheres' outgoing expansion).
{#prop:mean-mass} Proposition 3.4 (the mean mass).

Chapter 4: {#thm:approximant} the record's Theorem A (the approximant to every order).
Chapter 6: {#thm:uniform-existence} the record's Theorem E.
Chapter 7: {#thm:data} the record's Theorem D (exact data within O(λ^K) of the approximant).
Chapter 9: {#thm:past-approximant} Theorem A_P; {#prop:past-items} Proposition 9.10 (items 6–7 for Theorem 2's
solutions).
Chapter 10: {#lem:every-order-fixed} Lemma 11.0 (every order at fixed λ); {#prop:bondi-hierarchy} Proposition 11.1.
Chapter 62: {#prop:interior} BEYOND5 Proposition 6.2 (the development continues inside to the curvature boundary).
Chapter 63: {#thm:own-data} SETTLE-GLAM5 Theorem R5.1 (g_λ's own data settle, half-integer class, no gluing).
Chapter 64: {#thm:rw-settling} GAUGEDECAY5 Theorem 1.5 (settling in the Regge–Wheeler-type gauge).
Chapter 66: {#thm:harmonic-rate} the harmonic-gauge representative and its rate τ^(−min(p,3/2)+ε).
Chapter 71: {#thm:loss-d} the loss d and the regularity N = 21d + 6, with the explicit figures.
Chapter 80: {#thm:two-dusts} Theorem E_2 (two crossing dusts).
Chapter 81: {#thm:class-stability} Cauchy stability of the class Einstein–null-dust system (Theorem N′).
Chapter 82: {#thm:vlasov} Theorem V (restricted massless Vlasov limits).
Chapter 83: {#thm:charge-sign} the sign of the charge of exactly localised data (inside and outside the horizon).
Chapter 84: {#thm:layer} Theorem L and {#cor:layer} Corollary L.7.
Chapter 85: {#thm:very-edge} Theorem L_1E‴ (one theorem, one proof).
Chapter 86: {#prop:lambda0} the certified bounds on λ0 and the computed M_22.
Chapter 87: {#thm:ten-l5} existence at 10 l5 where the solution is the seed, and why not beyond.

## No computations (the author's ruling)

The edition contains no code and cites no computation. Every step the record supports by a program is written out as
mathematics. Steps that only a large or floating-point computation establishes are marked
`[[pending:computational-N]]` and decided by the coordinator with the author.

## Notation fixed for the whole edition (from outline-M section 5.4)

- N: the number of stages of the approximant only. The Nash–Moser regularity is written N_NM = 21d + 6.
- θ: the phase. The polar angle is ϑ.
- μ0: the seed's mass. The black-hole parameter of the stability theory is written m (with ϖ_K where the record does).
- λ: the wavelength only. The spectral parameter is σ; an indicial root is written ι (or as the source names it, with
  the name kept consistent within its chapter and declared at first use).
- K: the approximant's order, O(λ^K). The Kretschmann scalar is 𝒦; the curvature coordinate keeps the name x_K;
  the mass change of the gauge chapters is written K* as in the source.
- Results named by letters in the record (Theorems A, D, E, P, M, L, Q, T, X, V, N, K; Lemma A; Proposition L) get
  edition numbers only; a chapter may say once, in words, what a result does, never its record letter.
