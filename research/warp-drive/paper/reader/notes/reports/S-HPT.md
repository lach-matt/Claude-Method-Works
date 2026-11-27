# S-HPT: scoping a move of the computational point h

Scoping report only. No repository file was edited and nothing was committed. Branch ccr-66909215-gi0qa5. Line numbers
are those of HEAD 7796fb09; at the current HEAD 0c913792 chapters 33, 70, 71 and 96 are unchanged and the cited lines
of 03 and 90 have not moved. P-UB1 and P-UB2 are confirmed proof files (R-P-UB1, R-P-UB2), not yet merged; their texts
are taken as the state to be moved. P-TR was revised while this report was written (section 7).
Scratch work, scripts and raw output: /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/shpt/
(section 8 lists the files). Every number in sections 3–5 is a numerical observation (50-digit roots, not certified),
except where it is quoted from a proof file.

## 0. Summary

1. **h = 10⁻⁶ is unlucky, and the luck is the whole effect.** μ_Z(h) behaves like the least of roughly a thousand
   independent uniform draws on (0, ε₀), ε₀ = 𝔡₀ − 4𝔡₁ = 5.56·10⁻¹³ (each root ι ∈ Z₃ offers about 1.25(3 − Re ι)
   residues of the lattice near 3): an exponential variable. Near h = 10⁻⁶ its observed mean is 4.3·10⁻¹⁶ (999 points),
   3.7·10⁻¹⁶ over [5·10⁻⁷, 10⁻⁶] (1001 points), and the fractions above 10⁻¹⁵ and 2·10⁻¹⁵ match exp(−t/mean) to within
   the sampling error. h = 10⁻⁶ (μ_Z = 1.6748·10⁻¹⁷) lies in the lowest 4–5 %. Every root's excess moves by ε₀ when h
   moves by about 10⁻¹⁸, so μ_Z(h) has no smooth part to optimise: there is no good *interval*, only good *points*. A
   candidate must be a fixed exact number, and its proofs must be carried out at that number.
2. **Recommended point: γ_C = 1,007,860, h = 1/1,007,860 ≈ 9.92201·10⁻⁷** (sections 3–4). Numerically:
   μ_Z ≈ 2.934416·10⁻¹⁵ (real root of P_402, (p, q) = (81106, 2192182)), next excess 4.0236·10⁻¹⁵ (37 % above),
   N̄_Λ ≈ 9.1280·10¹⁴ (+0.36 %). With P-UB2's chain: **d_NM < 4.354·10⁵³ (174 times smaller than 7.57245·10⁵⁵),
   K < 9.577·10⁵⁴ (÷174), K* < 3.669·10¹¹⁰ (÷3.0·10⁴)**. Every robustness check passes: ε_ind(h) = δ_50 (least
   h-dependent distance from ℤ 4.96·10⁻⁶, as at 10⁻⁶), the four crossing margins of lem:s14-crossings pass (141.6,
   401.1, 61.4, 368.7 against 3.1, 33, 27, 103), no near-double root, lem:sp-exceptional's conclusion holds, and the
   point is also good if 𝔡₀ is later dropped (μ♭_Z = 3.12·10⁻¹⁰ > ε_Υ; the 1D bound would be 0.8 % above h = 10⁻⁶).
   The minimiser was confirmed at 80 digits and by a rigorous root isolation (python-flint) with the interval bounds of
   lem:is-offsets (b).
3. **Runners-up:** γ_C = 1,003,580 (gain 152; needs one extra enclosure, the ι_P crossing of 51 at l = 8055 has
   margin 7.6 < 103) and the round γ_C = 1,014,000 (gain 107; all checks pass). γ_C = 1,001,670 has the best gain in
   the scans (178) but a root of P_3918 lies 4.8·10⁻⁷ from 14, below δ_C, so prop:s14-damping-distance would need a
   restatement; γ_C = 1,004,340 (gain 174) fails the 𝔡₀-dropped criterion (that bound 6.9 times worse).
   A much longer search would find μ_Z of about 3.9·10⁻¹⁵ among 10⁴ points or 4.9·10⁻¹⁵ among 10⁵ (mean × ln M): a
   further factor 1.3–1.7 at most, before the robustness filters. The cap μ_G = 1.6416·10⁻¹⁴ of Λ_ℬ is out of reach.
4. **Cost** (section 5): no new mathematics of substance, but a full re-derivation at the new point of chapter 33
   sec:s14-pa and sec:s14-exc-point (about 510 source lines, PDF pp. 607–615, essentially every constant), of the fixed
   tables sec:tab-a and sec:tab-t49 (about 415 source lines, PDF pp. 1622–1627), of about fifteen at-the-point results of
   chapter 71 (sec:is, sec:sp-point, def:ec-point, def:uc-choice, lem:uc-admissible), and a re-run of P-UB1's
   certification (sec:tab-is, about 35 pages, which P-UB1 adds in any case) and P-UB2's chain script; then a second
   reading of all of it. Two written arguments change form: lem:s14-vector-distance (its sieve uses 10⁶ = 2⁶5⁶; a
   49-row direct check replaces it) and possibly lem:sp-exceptional (its 2- and 5-adic table; a finite check on twelve
   cubics in κ is the fallback). Chapter 70 can stay at γ_C = 10⁶. If P-TR (revised for the repaired Λ) is merged,
   chapter 33's part can be skipped: its thm:tr-transfer supplies the inputs at any h outside 𝖩 (section 7).
5. **𝔡₀ dropped** (section 6): then h = 10⁻⁶ is already the best point in [5·10⁻⁷, 10⁻⁶]: μ♭_Z(10⁻⁶) = 3.548·10⁻¹⁰
   exceeds ε_Υ, so (G) costs nothing, and N♭_Λ is smallest at the largest h. About 60 % of other points have
   μ♭_Z < ε_Υ and would make that bound worse. **Sequence: decide P-D0 first. If 𝔡₀ can be dropped, do not move h. If
   not, move to γ_C = 1,007,860**, which is safe for either outcome.

## 1. Why h = 10⁻⁶, and what bounds h

**Why 10⁻⁶ (sec:ec-point, rem:ec-point-outside, rem:s14-eps-ind-scope, sec:s14-pa opening).** It is the right end of
(0, 10⁻⁶], the interval on which prop:np-10-52 (iii) defines ε_ind(h) and on which every uniform root lemma of chapter 33
is stated (prop:np-10-54, prop:s14-scalar-every-h, lem:s14-line-two, lem:s14-line-far, lem:iv4-1-3, thm:t49-uniform). At
it the location, simplicity and exceptional-set statements were proved (sec:s14-pa, sec:s14-exc-point), ε_ind = δ_50
(cor:s14-eps-ind-point), and it gives the fewest roots below 3 (the degrees with roots below 3 run up to l ≈ h^(−1/2)).
Nothing in the paper chose it for the lattice excess μ_Z, which did not exist when it was fixed.

**Upper bound: h ≤ 10⁻⁶, and moving above it is not cheap.** def:vi-c-admissible no longer caps h (P-ADM decision),
but every tool the computational point uses is stated for h ≤ 10⁻⁶:
- (C1) at the point: rem:ec-point-outside cites lem:iv4-1-3 (a), which rests on prop:np-10-54 / prop:s14-scalar-every-h,
  all for h ∈ (0, 10⁻⁶];
- ε_ind(h) and the sets 𝖹₁, 𝖹₂, 𝖹₃ are defined only on (0, 10⁻⁶] (prop:np-10-52 (ii)–(iii), lem:iv4-1-3 (b));
- the lower bounds: thm:ec-lb-proved, lem:ec-lb-ind, lem:ec-lb-rounds, cor:ec-lb-delta and rem:ec-lb-unbounded assume
  h ≤ 10⁻⁶, and thm:loss-d (ii) at the point uses ε_ind(h) ≤ δ_50 (prop:np-10-52 (iii));
- P-TR (proofs/P-TR.md, not merged) is stated for h ∈ [h_m, 10⁻⁶).
So h > 10⁻⁶ needs new arguments in chapters 33 and 71 (the uniform lemmas re-proved on a longer interval). The gain is
small: Σ(3 − Re ι)², which fixes N_Λ, falls by about 0.47 % per 1 % increase of h, so d_NM by about 0.9 % per 1 %. Not
recommended; everything below keeps h < 10⁻⁶.

**Lower bound.** Nothing in the definitions bounds h below (s_C > 100 holds for every h < 4.99·10⁻³). What does:
- *The written proofs at the point* (prop:is-iota, prop:is-logs (c), prop:is-mult) separate the real roots ι ∈ Z from
  the gauge entries by "more than 2.93·10⁻⁶ from ℤ" against "within 1.34·10⁻⁶ of ℤ". The root of P_2 near 2 lies in
  (2 + (40/13)h(1 − 5·10⁴h), 2 + (40/13)h) (lem:ec-lb-ind), so it is within 1.34·10⁻⁶ of 2 once h is below about
  4.4·10⁻⁷. Below that the separation must be argued type by type, as P-TR's prop:tr-inputs (b) does.
- *P-TR*: below 13ε_Υ/40 = 4.751·10⁻¹¹, ε_ind(h) < ε_Υ (lem:ec-lb-ind), so ε_g < ε_Υ and the chain (Δτ_0, T_<, T_>,
  I_lev, …) changes. For h ≤ 6.309·10⁻⁹, (40/13)h < δ_50, so ε_ind(h) < δ_50 there (rem:ec-lb-ind).
- *Cost*: the number of roots below 3 grows like h^(−1/2) (2629 at 10⁻⁶, 3719 at 5·10⁻⁷), Σ(3 − Re ι)² with it
  (793.6 → 1103.6), and N̄_Λ² by a factor 1.91 at 5·10⁻⁷; the new table of P-UB1 (sec:tab-is) grows in proportion.
- *Avoid*: the three intervals of prop:t49-six inside [5·10⁻⁷, 10⁻⁶], (5.62, 5.83)·10⁻⁷, (7.27, 7.47)·10⁻⁷ and
  (8.88, 9.07)·10⁻⁷, each holding an h at which P_l (l = 133, 134, 135) has a double real root near 5/2. There
  lem:s14-sextic-small/large and the case split of prop:is-mult (two close real roots in |ι − a| < 0.45) need finer
  work. P-UB1's sample point 9·10⁻⁷ lies in the last of them.

So the admissible window for a cheap move is roughly [4.4·10⁻⁷, 10⁻⁶) minus those intervals, and in practice
h close to 10⁻⁶ is best, because N̄_Λ is smallest there.

## 2. Every site that uses h = 10⁻⁶ or a number computed from it

Status: **U** holds for every h in an interval, or is stated at γ_C = 10⁶ explicitly and stays true (nothing changes,
at most a wording choice); **R** re-evaluation by the same method (size given); **N** needs a new argument, or the
method may fail at the new point and must be checked (risk named). **T** a quoted number that follows from R sites.
Line numbers are those of HEAD 7796fb09.

### 2.1 Chapter 33 (constraint damping)

| site | status | what changes |
|---|---|---|
| 33:91–132 sec:iv4-0, eq:iv4-0-1 (𝖧, h_*, 𝖹; "10⁻⁶ ∉ 𝖹") | U | uniform; the clause on the point 10⁻⁶ stays true |
| 33:286–331 prop:np-10-54 (all h ∈ (0, 10⁻⁶]) | U | — |
| 33:781–841 prop:np-10-79; 1191–1204 lem:iv4-1-5 ("ϑ_ℋ = −4995.83… at h = 10⁻⁶") | U | values quoted at 10⁻⁶ as examples; bounds hold for every h ≤ 10⁻⁶ |
| 33:842–1036 sec:s14-every-h (lem:s14-half-plane-count, lem:s14-line-two, lem:s14-line-far, lem:s14-limit-sides, prop:s14-scalar-every-h) | U | — |
| 33:1125–1160 lem:iv4-1-3 (a)–(b) | U | (C1) at the new point follows from (a) |
| 33:3059, 3540 (tf model, h_tf ≤ 10⁻⁶) | U | — |
| 33:4028–4120 prop:np-10-52, rem:s14-delta50 | U | ε_ind(h) ≤ δ_50 at every h; δ_50 depends on z only |
| 33:4121–4141 sec:s14-pa opening ("h := 10⁻⁶, ε₀ := e/h = 625/64, x := hκ, δ_C := 2.94·10⁻⁶") | R | new h, ε₀ = γ_C/102400, δ_C ≈ 2.94h-type constant |
| 33:4144 lem:s14-delta50 | U | z only |
| 33:4169 lem:s14-vector-distance (Γ = 250002000000, X_k = k² + 10⁶(k − 2), congruences mod 64 and 25 because 10⁶ = 2⁶5⁶, nine leftover k) | R/N | for an integer γ_C the same scheme gives Γ = N² + 3γ_C − 1, N = (γ_C − 2)/2; the mod-64/25 sieve is specific to 10⁶; replace by a direct check that no X_k ± 1, X_k ± 2 (2 ≤ k ≤ 50) is a square, which gives abs((l + 1)² − X_k) ≥ 3 — a 49-row table, but the written argument is new |
| 33:4197 lem:s14-scalar-zero | R | two sign checks |
| 33:4208 lem:s14-sextic-split (c, c⁰, c₁, c₂, x₋, x₊, Λ⁰, Λ₁, Λ₂, Π⁰ and all their bounds) | R | every exact polynomial at ε₀ = 625/64 re-derived at the new ε₀; about 100 lines |
| 33:4313 lem:s14-majorant, 4330 lem:s14-fixed-point | U | general lemmas |
| 33:4343 lem:s14-sextic-count, 4362 cor:s14-remote-point | R | majorant numbers |
| 33:4372 lem:s14-sextic-small ("1 ≤ l ≤ 133", (2 + 2.93h, 2 + 2.94h), the four signs) | R | the l-range (x < 0.018) and the P_2 bracket re-checked (at γ_C = 1,007,860 both stay: l ≤ 133, (2 + 2.93h, 2 + 2.94h)); G₀, L₀ bounds re-derived |
| 33:4405 lem:s14-sextic-large (rows of sec:tab-a-pieces) | R | every row's constants re-verified; rows near x₋ may need re-splitting |
| 33:4441 lem:s14-crossings (K_n, K′_n, the tolerances 3.1, 33, 27, 103) | R/N | the distances of l(l + 2) from K_n, K′_n at the new h must exceed the tolerances; if one does not, that (l, n) needs its own enclosure (a few lines each). Check section 4 |
| 33:4477 prop:s14-damping-distance ("dist > 2.94·10⁻⁶ … except P_2", "> 2.93·10⁻⁶") | R/N | holds at the new h only if no root with abs(ι − 1) ≤ 50 comes within about 2.94h of an integer; checked numerically for the candidates (section 4) |
| 33:4511 cor:s14-eps-ind-point (ε_ind(10⁻⁶) = δ_50) | R | holds at the new h if every h-dependent distance exceeds δ_50 = 1.94·10⁻⁸ (checked, section 4) |
| 33:4528 rem:s14-eps-ind-scope | T | names the point |
| 33:4542–4589 sec:s14-exceptional opening, rem:t49-sets | U | — |
| 33:4590–4689 sec:s14-exc-shifted (lem:t49-shifted, thm:t49-uniform) | U | every h ∈ (0, 10⁻⁶] |
| 33:4690–4706 sec:s14-exc-point opening (𝒫 = 64·10¹⁸P, 𝔇, 𝔖) | R | new scaling, new polynomials |
| 33:4707 prop:t49-simple (𝔇 of degree 9, four positive roots bracketed between integers) | R | generic; failure would need a root of 𝔇 at some l(l + 2) |
| 33:4724 prop:t49-pairs (𝔖(k, ·) cubics, l_k table, 3 ≤ k ≤ 51) | R | generic, as above |
| 33:4741 thm:t49-point, 4757 cor:t49-right (κ₀ = 8365·8367) | R | κ₀ and the real root of 𝒫(51; ·) change |
| 33:4778–4863 sec:s14-exc-interval (prop:t49-six, prop:t49-vector) | U | statements on (0, 10⁻⁶]; "the largest h^v below 10⁻⁶" is about 10⁻⁶, not the point |
| 33:4864 rem:t49-scope | T | names the damping point |

Size: sec:s14-pa and sec:s14-exc-point are about 510 source lines (PDF pp. 607–615 of 1,948). Every result keeps its
statement and proof structure; essentially every printed constant changes.

### 2.2 Chapter 70 (resolvent bounds)

| site | status | what changes |
|---|---|---|
| 70:1694–1699 (numbers "at (γ_C, γ_Υ, e_Υ) = (10⁶, 1/100, 1/100)"; not of the form h⁻¹ with h ∈ 𝖧) | U | stated at γ_C = 10⁶ explicitly, not at the computational point; still true |
| 70:1758 lem:rb-roots-point (roots 1.0000747438, 1.0000029324, 1.0000169224) | U (optional R) | no result of chapter 71 uses it; re-doing it at the new γ_C is half a page of exact arithmetic |
| 70:1879–1884 horizon exponents at x = 5000 | U | — |
| 70:1929; 70:2011 prop:rb-quasimode-point; rem:rb-quasimode-observed; 70:2058–2061 (M_33, γ_Ca = 5000) | U (optional R) | illustrative upper bounds at γ_C = 10⁶; re-doing prop:rb-quasimode-point needs six new integer vectors w (numerical search, then exact arithmetic) |

Recommendation: leave chapter 70 at γ_C = 10⁶ and say once (70:1694) that this is not the computational point.

### 2.3 Chapter 71 (explicit constants)

| site | status | what changes |
|---|---|---|
| 71:19–20, 1493–1496, 1564–1569, 1725–1815 (thm:ec-lb-proved, lem:ec-lb-ind, lem:ec-lb-rounds, cor:ec-lb-delta, "γ_C ≥ 10⁶", "h ≤ 10⁻⁶") | U | the proved-set lower bounds; the new point has h < 10⁻⁶ |
| 71:22–23, 1462–1528 thm:loss-d (ii), prop:ec-rounds, cor:uc-two-offsets (1.403·10²⁰, 2.946·10²¹, 1.2497·10²⁴, 2.624·10²⁵) | U | z only, and ε_ind(h) ≤ δ_50, h ≤ 10⁻⁶ (the last sentence of thm:loss-d, 1497–1499, quoting the upper bound, is T: P-UB2's M3) |
| 71:24–33 chapter summary (upper bound, K) | T | P-UB2's M1, M2 at the new inputs |
| 71:44–54 def:ec-point | R | the value of h; "ε_ind(h) = δ_50" by the new cor:s14-eps-ind-point |
| 71:56–85 rem:ec-point-outside (s_C = 499995.1171875; h ∉ 𝖹, Z_exc = ∅ by thm:t49-point) | R | s_C = (1 − e_C)γ_C/2; the rest follows from the new chapter 33 |
| 71:87–171 sec:ec-gap-sums, rem:gap-sums | U | z only (P-UB1's T1 last sentence: T, it cites the Z₃ data) |
| 71:466, 486 (horizon threshold, eigenvalues of S̄) | U | every γ_C |
| 71:1336–1411 lem:ec-gauge-gap | U | z only |
| 71:1413 rem:ec-gauge-gap ("ε_ind(10⁻⁶) = δ_50") | R | one citation |
| 71:1678 rem:ec-lb-ind (h = 10⁻⁶ as example) | U | true as stated; may stay |
| 71:1806 rem:ec-lb-unbounded (h ≤ 4.48·10⁻²⁶, P-UB2's 6.46·10⁻²⁹) | T | threshold √(0.3168/D_NM) |
| 71:1895–1951 lem:ec-theta-in-zero ("1.5·10⁶{1, 2, 1 − 1/102400}") | T | the number 1.5γ_C |
| 71:2206 rem:ec-upper-point, 2217 rem:ec-upper-open, 2246 sec:uc-close | T | P-UB2's M5–M7 |
| 71:2583 def:uc-choice (ε_K, ε_+), eq:uc-deltas | R | new ε_K < μ_Z(h), ε_+ ∈ (ε_K, μ_Z(h)); Δβ_0 = 0.999²ε_K |
| 71:2599 lem:uc-admissible ("ε_ind(10⁻⁶) = δ_50 > ε_Υ", (G), (G⁺)) | R | needs ε_ind(h) > ε_Υ at the new h (checked, section 4) |
| 71:2646 lem:uc-gaps, 2716–2728 (1/𝔡₁, W) | U | z only |
| 71:2662–2823 lem:uc-lambda, lem:uc-n-iota, prop:uc-explicit, thm:uc-integer (+ P-UB2's prop:uc-dependence), rem:uc-missing | R | P-UB2's chain at the new (ε_K, ε_+, N̄_Λ): its script regenerates every integer and every text (M9–M13) |
| 71:2825–2857 sec:is opening ("h = 10⁻⁶"); P-UB1's T2 | R/T | — |
| 71:2858–2991 lem:is-roots, lem:is-offsets, lem:is-count, sec:is-rules | U | z only |
| 71:2992 prop:is-ind | U | gauge roots only |
| 71:3034 prop:is-logs (c) (ι real "more than 2.93·10⁻⁶ from ℤ" against F "within 1.34·10⁻⁶") | R/N | needs the real ι ∈ Z with Re ι ≤ 6 more than 1.34·10⁻⁶ from ℤ at the new h, or P-TR's type-by-type argument |
| 71:3106 prop:is-iota (at (1/2, 1/102400, 10⁻⁶); 2.93·10⁻⁶; 3.00000499998…; 1000009, 2000016, 3000025) | R | vector-root integer check redone with the new Γ; the P_2 brackets |
| 71:3132 prop:is-mult (thm:t49-point at 10⁻⁶; l = 134–172, x₋, the values of Δ at l = 134, 135, 136) | R | the l-window around x₋/h and its Δ values change; the near-double pair must be separated at the new h (checked, section 4) |
| 71:3187 prop:is-ci-pp | U | gauge only |
| P-UB1 T7: new sec:is-z, lem:is-disc (U), lem:is-z3 (2629, 1269, 1360, l-ranges 135/136/815/999, 2 + 2.932·10⁻⁶, 2.514, 3 + 4.99·10⁻⁶) | R | regenerated from the new table; its count cites the chapter 33 location lemmas, which must be the re-proved ones |
| P-UB1 T7: prop:is-lambda (2.514, 2.932·10⁻⁶) | R | numbers |
| P-UB1 T8, T9: lem:is-gap-z (ι_* at P_390, (356327, 1116082), μ_Z, next 1.1076·10⁻¹⁵), thm:is-gap, cor:is-lower (1.2250·10²⁷) | R | new minimiser, new bounds, lower bound 3R ≈ 3/(μ_Zδ̂) (falls, see section 4) |
| P-UB1 T10, T11: prop:is-count (a) (S₁, S₂, N̄_Λ = 909,507,124,095,312, the non-real lower bound) | R | sums over the new table |
| 71:3361–3466 sec:is-smaller, thm:is-d0 (U), cor:is-flat / P-UB1 T12 (μ♭_Z at P_700, N_Λ ≤ 3,683,190,611) | R | μ♭_Z(h) and the 1D count; at many h, μ♭_Z(h) < ε_Υ (section 6) |
| 71:3469 rem:is-summary / P-UB1 T13 | T | — |
| 71:3489–3823 sec:sp to sec:sp-matrix | U | general |
| 71:3824–3832 sec:sp-point opening (h, δ_C, ι_v with 250002000000 and 499999) | R | — |
| 71:3833 lem:sp-roots (1413/1414, (2 + 3h, a(3h)), l = 134–172 and the Δ values) | R | — |
| 71:3910 lem:sp-exceptional (exact c_0(q) for twelve q, 2- and 5-adic valuations; ι_v ≠ q by integrality of 499999) | R/N | the valuation table must be recomputed; it may fail for a γ_C whose 2- and 5-adic structure differs, in which case the alternative is a finite check that the cubic κ ↦ P(q; κ) has no root at any l(l + 2) (checked numerically, section 4); ι_v ≠ q works for every integer γ_C |
| 71:3966 thm:sp-spectrum (lists with 1413) | R | — |
| 71:4014 cor:sp-lstar ((d): ε_+ < δ_50; ι_v(2) > 3 + 4·10⁻⁶ via (500002 + 4·10⁻⁶)²) | R | — |
| 71:4092–4925 sec:cs, sec:cs-small (lem:cs-fourier, lem:cs-levels, …, prop:uc-d-small; 4397 "−μ ≥ ε_ind > ε_K") | R | P-UB2's M14–M25 at the new inputs |
| 71:5101 prop:uc-data-order (d) | R | P-UB2's M26 |
| 71:5236, 5290–5292 (sec:ec-linear; γ_C = 10⁶, 10⁷, 10⁸ numerical observation) | U | — |

### 2.4 Chapter 96 (Appendix B)

| table | status | size |
|---|---|---|
| 96:6–17 sec:tab-a header ("(v, e, h) = (1/2, 1/102400, 10⁻⁶), ε₀ = 625/64") | R | — |
| 96:18–29 sec:tab-a-sextic (π_k(κ)) | R | 7 polynomials |
| 96:30–74 sec:tab-a-split: R₁, R₂, R₃ in (ι, x, ε₀) | U | symbolic in ε₀ |
| same: the re-expansions, majorants R̄_j, R̄_j′ and the quotient 𝒲 at ε₀ = 625/64 | R | about 30 lines |
| 96:75–115 sec:tab-a-expansions (G_k, L_k, the two summed bounds) | R | about 30 lines |
| 96:116–171 sec:tab-a-pieces (location constants by x-interval) | R | every row recomputed |
| 96:172–240 sec:tab-a-crossings (K_n, K′_n, the distances) | R/N | recomputed; see lem:s14-crossings |
| 96:241–259 sec:tab-a-vector (nine numbers) | R | new leftover set |
| 96:260–421 sec:tab-t49 (𝔇 of degree 9; 𝔖 of degree 15 in k and 3 in κ; l_k for 49 values of k) | R | all coefficients |
| P-UB1 T14: sec:tab-is (1269 + 680 rows) | R | regenerated by P-UB1's scripts with h made a parameter; about 35 A4 pages, a few % more rows at h < 10⁻⁶ |
| 96:422–478 sec:tab-s14-numerators | U | Tangherlini, no h |

The fixed tables (sec:tab-a, sec:tab-t49) are PDF pp. 1622–1627, about 6 pages, every number of which changes.

### 2.5 Other chapters

| site | status |
|---|---|
| 00-front:33–37 (lower bound for γ_C ≥ 10⁶: U; "1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰": T, via P-UB2 O1) | U/T |
| 01-introduction:152–156 (same) | U/T |
| 03-theorems:313–319 (K bound), 358–366 | T / U |
| 34-s15-linearised:501 ("any h ∈ (0, 10⁻⁶]") | U |
| 46-s27-nonlinear:1754–1759, 1768, 1919–1920 (def:vi-c-admissible, prop:vi-c-adm-exist) | U |
| 63-own-data:70, 298–299 ("bounded above only at the computational point") | U |
| 90-scope:62–82 (T for the upper bound and the index-set lower bound; U for the rest) | U/T |
| 84, 85, 87, 83 (their 10⁻⁶ are other quantities) | not sites |

Outside chapters/: PAPER.md and the PDF (regenerate), STATUS.md, INTEGRATION.md, notes/DECISIONS.md, and
proofs/P-TR.md, whose current text treats h = 10⁻⁶ as the one point at which μ(h) and (R_h) are decided (opening,
thm:tr-transfer, rem:tr-scope, prop:tr-mu-small); those sentences would name the new point.

## 3. The scan

### 3.1 Method (numerical, not proved)

At each h = 1/γ_C: the roots of C and of P_l (l ≥ 1, up to hκ ≤ 1.08) at (v, e) = (1/2, 1/102400), from the exact
symbolic sextic (it reproduces sec:tab-a-sextic, eq:is-c-int and P-UB1's 𝒫_390 exactly), seeded in double precision
and polished by Newton at 50 digits; Z₃ = roots with 2 < Re ι < 3 (the root 2 of P_1 removed); y_ι = 3 − Re ι;
the least excess m(y_ι) by the reduction of lem:is-reduction (as in P-UB1's script), with 𝔡₀, 𝔡₁ to 50 digits;
μ_Z(h) = min over Z₃ of m(y_ι), also checked against every root with Re ι ∈ [3, 3.08] (no root of a P_l comes within 3·10⁻⁵ of 3 at
the points below) and the vector root at l = 2 (3 + 5h/(1 + 6h) or more). Then, exactly as P-UB1 and P-UB2 do:
ε_K = μ_Z cut to five digits, ε_+ between ε_K and μ_Z, N̄_Λ = 16,747,200,000,000 +
(S₂ + 2ν₀S₁ + #Z₃·ν₀²)·1125001468750.5 with S₁ = Σ y_ι, S₂ = Σ y_ι², ν₀ = 1.69·10⁻⁶, and P-UB2's chain (its own
chain.py, finish) for D_NM, K = 22D_NM + 345 and K* = 4k̄² + 48k̄ + 109, k̄ = 22D_NM + 340; k̄_0 = 3, J_* = 15,000,015,
l_* = 50 as at 10⁻⁶. **Validation:** at h = 10⁻⁶ the engine gives #Z₃ = 2629 (1360 non-real), S₂ = 793.559258,
S₁ = 1207.936308, μ_Z = 1.67479·10⁻¹⁷ at l = 390, (p, q) = (356327, 1116082), next 1.1076·10⁻¹⁵ at l = 23,
μ♭_Z = 3.5481·10⁻¹⁰ at l = 700, Σ(n⁺ + 1) = 3,623,813,354, and the chain gives D_NM < 7.57245·10⁵⁵, K < 1.66594·10⁵⁷,
K* < 1.11014·10¹¹⁵: every number of P-UB1's lem:is-z3, lem:is-gap-z, prop:is-count, cor:is-flat and of P-UB2's final
evaluation. The nine points of P-UB1 §2.2 are reproduced to every printed digit (9.6·10⁻⁷ gives the same gain 84).

Integer γ_C are used throughout: lem:s14-vector-distance, prop:is-iota, lem:sp-roots and lem:sp-exceptional use that
the vector roots are N_γ ± (N_γ² + κ + 3γ_C)^(1/2) with N_γ = (γ_C − 2)/2, Γ = N_γ² + 3γ_C − 1 an integer. P-UB1's
decimal points such as 9.6·10⁻⁷ (γ_C = 1,041,666.6…) would need rational versions of those arguments.

### 3.2 P-UB1's sample points, with the chain

| h | #Z₃ | Σy² | μ_Z | next | gain in d_NM |
|---|---|---|---|---|---|
| 1·10⁻⁶ | 2629 | 793.56 | 1.6748·10⁻¹⁷ | 1.1076·10⁻¹⁵ | 1 |
| 9.9·10⁻⁷ | 2642 | 797.32 | 7.7731·10⁻¹⁶ | 1.7811·10⁻¹⁵ | 46.0 |
| 9.6·10⁻⁷ | 2683 | 808.96 | 1.4605·10⁻¹⁵ | 2.0143·10⁻¹⁵ | 84.0 |
| 9.5·10⁻⁷ | 2696 | 812.96 | 7.0909·10⁻¹⁶ | (conjugate) | 40.4 |
| 9·10⁻⁷ (in a prop:t49-six interval) | 2771 | 833.97 | 4.1155·10⁻¹⁶ | 1.2599·10⁻¹⁵ | 22.3 |
| 8·10⁻⁷ | 2939 | 881.79 | 6.5076·10⁻¹⁶ | (conjugate) | 31.6 |
| 5·10⁻⁷ | 3719 | 1103.61 | 1.1925·10⁻¹⁵ | 1.2435·10⁻¹⁵ | 37.2 |

### 3.3 Coarse grid: γ_C = 10⁶ + 1000k, k = 0, …, 1000 (h from 10⁻⁶ down to 5·10⁻⁷), the twelve best

Gain = D_NM(10⁻⁶)/D_NM(h). (l, p, q): the root of P_l attaining μ_Z and the lattice point; next: the second excess
and its degree.

| γ_C | h | #Z₃ | Σy² | μ_Z | (l, p, q) | next (l) | next/μ_Z | gain |
|---|---|---|---|---|---|---|---|---|
| 1005000 | 9.950249·10⁻⁷ | 2635 | 795.424 | 2.4185·10⁻¹⁵ | (409, 302206, 1289418) | 2.7590·10⁻¹⁵ (502) | 1.141 | 143.7 |
| 1014000 | 9.861933·10⁻⁷ | 2647 | 798.769 | 1.8103·10⁻¹⁵ | (96, 531580, 408006) | 1.8413·10⁻¹⁵ (270) | 1.017 | 106.7 |
| 1036000 | 9.652510·10⁻⁷ | 2676 | 806.884 | 1.7013·10⁻¹⁵ | (179, 118238, 956563) | 1.9187·10⁻¹⁵ (536) | 1.128 | 98.3 |
| 1161000 | 8.613264·10⁻⁷ | 2832 | 851.469 | 1.7490·10⁻¹⁵ | (134, 304918, 398917) | 2.3714·10⁻¹⁵ (305) | 1.356 | 90.9 |
| 1352000 † | 7.396450·10⁻⁷ | 3057 | 915.246 | 2.0137·10⁻¹⁵ | (491, 143351, 523625) | 2.1075·10⁻¹⁵ (231) | 1.047 | 90.8 |
| 1287000 | 7.770008·10⁻⁷ | 2983 | 894.074 | 1.8819·10⁻¹⁵ | (802, 126236, 992033) | 2.1923·10⁻¹⁵ (462) | 1.165 | 88.9 |
| 1763000 † | 5.672150·10⁻⁷ | 3492 | 1038.833 | 2.4986·10⁻¹⁵ | (162, 100171, 1065294) | 3.2974·10⁻¹⁵ (529) | 1.320 | 87.8 |
| 1059000 | 9.442871·10⁻⁷ | 2706 | 815.278 | 1.5386·10⁻¹⁵ | (51, 377778, 1369379) | 1.6529·10⁻¹⁵ (87) | 1.074 | 87.1 |
| 1128000 | 8.865248·10⁻⁷ | 2793 | 839.937 | 1.6086·10⁻¹⁵ | (916, 92157, 395000) | 2.2265·10⁻¹⁵ (342) | 1.384 | 85.9 |
| 1108000 † | 9.025271·10⁻⁷ | 2767 | 832.868 | 1.5464·10⁻¹⁵ | (42, 665427, 257356) | 1.5471·10⁻¹⁵ (268) | 1.000 | 84.0 |
| 1028000 | 9.727626·10⁻⁷ | 2664 | 803.943 | 1.4387·10⁻¹⁵ | (656, 33216, 1607495) | 1.7533·10⁻¹⁵ (93) | 1.219 | 83.7 |
| 1398000 | 7.153076·10⁻⁷ | 3109 | 929.928 | 1.8741·10⁻¹⁵ | (213, 439421, 1144064) | 1.9949·10⁻¹⁵ (605) | 1.064 | 81.9 |

† inside one of the three prop:t49-six intervals (near-double roots of P_133…135); avoid. Statistics of the 1001
points: mean μ_Z 3.70·10⁻¹⁶, median 2.58·10⁻¹⁶, maximum 2.50·10⁻¹⁵; 6.6 % above 10⁻¹⁵ (exp(−t/mean): 6.7 %),
0.40 % above 2·10⁻¹⁵ (0.45 %); 4.7 % at or below μ_Z(10⁻⁶). Smaller h pays twice: more draws (smaller typical μ_Z)
and a larger N̄_Λ (Σy² + 39 % at 5·10⁻⁷).

### 3.4 Fine grid near 10⁻⁶: γ_C = 10⁶ + 10k, k = 1, …, 999, the twelve best

| γ_C | h | #Z₃ | Σy² | μ_Z | (l, p, q) | next (l) | next/μ_Z | gain |
|---|---|---|---|---|---|---|---|---|
| 1001670 | 9.983328·10⁻⁷ | 2631 | 794.183 | 2.9780·10⁻¹⁵ | (24, 276005, 1869028) | 3.0355·10⁻¹⁵ (118) | 1.019 | 177.5 |
| 1004340 | 9.956788·10⁻⁷ | 2635 | 795.178 | 2.9269·10⁻¹⁵ | (513, 4837, 888644) | 3.3449·10⁻¹⁵ (193) | 1.143 | 174.1 |
| **1007860** | 9.922013·10⁻⁷ | 2638 | 796.488 | 2.9344·10⁻¹⁵ | (402, 81106, 2192182) | 4.0236·10⁻¹⁵ (394) | 1.371 | 174.0 |
| 1005240 | 9.947873·10⁻⁷ | 2635 | 795.513 | 2.5885·10⁻¹⁵ | (445, 283609, 1271960) | 2.6242·10⁻¹⁵ (376) | 1.014 | 153.8 |
| 1003580 | 9.964328·10⁻⁷ | 2632 | 794.895 | 2.5482·10⁻¹⁵ | (94, 503406, 959429) | 2.9415·10⁻¹⁵ (27) | 1.154 | 151.7 |
| 1004890 | 9.951338·10⁻⁷ | 2635 | 795.383 | 2.4869·10⁻¹⁵ | (336, 619211, 184139) | 3.0392·10⁻¹⁵ (96) | 1.222 | 147.8 |
| 1008140 | 9.919257·10⁻⁷ | 2639 | 796.593 | 2.4901·10⁻¹⁵ | (417, 165840, 446556) | 2.5380·10⁻¹⁵ (427) | 1.019 | 147.6 |
| 1005000 | 9.950249·10⁻⁷ | 2635 | 795.424 | 2.4185·10⁻¹⁵ | (409, 302206, 1289418) | 2.7590·10⁻¹⁵ (502) | 1.141 | 143.7 |
| 1005020 | 9.950051·10⁻⁷ | 2635 | 795.431 | 2.1852·10⁻¹⁵ | (314, 492768, 732772) | 2.7918·10⁻¹⁵ (195) | 1.278 | 129.9 |
| 1005320 | 9.947082·10⁻⁷ | 2635 | 795.543 | 2.0330·10⁻¹⁵ | (807, 30649, 929215) | 2.3782·10⁻¹⁵ (331) | 1.170 | 120.8 |
| 1005220 | 9.948071·10⁻⁷ | 2635 | 795.506 | 2.0023·10⁻¹⁵ | (87, 622981, 137567) | 2.3217·10⁻¹⁵ (641) | 1.160 | 119.0 |
| 1000240 | 9.997601·10⁻⁷ | 2629 | 793.649 | 1.9686·10⁻¹⁵ | (620, 232834, 912054) | 2.2232·10⁻¹⁵ (109) | 1.129 | 117.5 |

Statistics of the 999 points: mean μ_Z 4.28·10⁻¹⁶, median 3.04·10⁻¹⁶, maximum 2.98·10⁻¹⁵ (exp(−t/mean) predicts
about 2.96·10⁻¹⁵ for the largest of 1000); 9.4 % above 10⁻¹⁵ (9.6 %), 1.1 % above 2·10⁻¹⁵ (0.9 %); 4.0 % at or below
μ_Z(10⁻⁶). Neighbouring points are independent draws: the autocorrelation of log μ_Z between points 10 apart in γ_C
(h 10⁻¹¹ apart) is 0.03, and −0.04 to 0.00 at lags 2–50; the means over windows of 50 points (3.2 to 5.7·10⁻¹⁶) vary
as sampling noise would. Near 10⁻⁶, N̄_Λ grows by only 0.1–0.5 %, so the gain is μ_Z/μ_Z(10⁻⁶) to within 1 %.

**Robustness in h.** The minimising root at γ_C = 1,007,860 is real, at l = 402 (κ = 162,408), and moves at
dι/dh ≈ κ; a change of h by 2·10⁻²⁰ (relative 2·10⁻¹⁴) moves its excess by μ_Z. So "robust" can only mean robust as
a statement about one exact number: separated from the next excess (next/μ_Z), far from integer crossings, far from
double roots, far from the points of lem:sp-exceptional. Section 4 checks those.

## 4. The candidates, checked

All numerical (50 digits; the minimiser of the recommended point also at 80 digits and by python-flint's rigorous
complex_roots of the exact rational sextic: with lem:is-offsets (b)'s bounds for 𝔡₀ and 𝔡₁, the excess at
(p, q) = (81106, 2192182) lies in (2.9344160182, 2.9344160204)·10⁻¹⁵).

Columns: **dist** the least distance from ℤ of Re ι over every root of C, P_l (hκ ≤ 70) and p_(v) with abs(ι − 1) ≤ 50, the
root of P_2 near 2 excluded (it lies between 2 + 2.93h and 2 + 2.94h at every point below, more than 1.34·10⁻⁶ from 2) —
prop:s14-damping-distance needs it above about 2.94h ≈ 2.9·10⁻⁶ to hold as written, cor:s14-eps-ind-point above
δ_50 = 1.94·10⁻⁸ for ε_ind(h) = δ_50, P-TR's (H_ε) above ε_Υ; **cross** the four margins of lem:s14-crossings in κ-units
(B n ≤ 17, B n ≥ 18, P n ≤ 28, P n ≥ 29; needed: 3.1, 33, 27, 103; at 10⁻⁶ the engine gives 14.40, 321.67, 141.10,
392.19 against the printed 14.39, 321.67, 141.07, 392.12); **pair** the closest two roots of one P_l in (2, 3.5) (a
near-double root would show here); **Q** the least distance of a real root κ of the cubic κ ↦ P(q; κ, h), q in the twelve
points of lem:sp-exceptional, from the nearest l(l + 2) (positive means P_l(q) ≠ 0 for every l); **μ♭_Z** the 𝔡₀-dropped
excess (it should exceed ε_Υ = 1.4619·10⁻¹⁰).

| γ_C | gain | next/μ_Z | dist (where) | cross | pair | Q | μ♭_Z | verdict |
|---|---|---|---|---|---|---|---|---|
| 1000000 | 1 | 66.1 | 5.0·10⁻⁶ (v, l = 2) | 14.4, 322, 141, 392 | 1.9·10⁻⁴ | 112 | 3.55·10⁻¹⁰ | the present point |
| 1001670 | 177.5 | 1.019 | **4.8·10⁻⁷ (P_3918 near 14)** | — | 1.2·10⁻⁴ | 115 | 1.81·10⁻¹⁰ | prop:s14-damping-distance needs restating (ε_ind = δ_50 still holds) |
| 1004340 | 174.1 | 1.143 | 4.98·10⁻⁶ (v, 2) | — | 1.2·10⁻⁴ | 120 | **2.1·10⁻¹¹** | 𝔡₀-dropped bound 6.9× worse |
| **1007860** | **174.0** | **1.371** | 4.96·10⁻⁶ (v, 2) | **141.6, 401.1, 61.4, 368.7** | 1.2·10⁻⁴ | 68 | **3.12·10⁻¹⁰** | **recommended** |
| 1005240 | 153.8 | 1.014 | 4.97·10⁻⁶ (v, 2) | — | 1.2·10⁻⁴ | 5.3 | 2.5·10⁻¹¹ | 𝔡₀-dropped bound worse |
| 1003580 | 151.7 | 1.154 | 4.98·10⁻⁶ (v, 2) | 220.2, 53.3, 128.0, **7.6** | 1.9·10⁻⁴ | 38 | 3.33·10⁻¹⁰ | second choice; one extra enclosure (ι_P near 51 at l = 8055) |
| 1004890 | 147.8 | 1.222 | 4.98·10⁻⁶ (v, 2) | — | 1.9·10⁻⁴ | 25 | 2.6·10⁻¹¹ | 𝔡₀-dropped bound worse |
| 1008140 | 147.6 | 1.019 | 4.96·10⁻⁶ (v, 2) | — | 1.2·10⁻⁴ | 18 | 1.11·10⁻¹⁰ | 𝔡₀-dropped bound 1.3× worse |
| 1005000 | 143.7 | 1.141 | 4.98·10⁻⁶ (v, 2) | — | 1.9·10⁻⁴ | 78 | 6.3·10⁻¹¹ | 𝔡₀-dropped bound 2.3× worse |
| 1014000 | 106.7 | 1.017 | 4.93·10⁻⁶ (v, 2) | 34.6, 180.6, 107.6, 275.1 | 1.2·10⁻⁴ | 68 | 4.25·10⁻¹⁰ | round alternative; all checks pass |
| 1000240 | 117.5 | 1.129 | 5.0·10⁻⁶ (v, 2) | — | 1.2·10⁻⁴ | 61 | 3.7·10⁻¹² | 𝔡₀-dropped bound 39× worse |
| 1028000 | 83.7 | 1.219 | 4.86·10⁻⁶ (v, 2) | — | 1.9·10⁻⁴ | 13 | 2.89·10⁻¹⁰ | — |

(— : not computed.) At every candidate the least distance from ℤ of a real root of Z of real part at most 6 is the P_2
root near 2 (2.86–2.93·10⁻⁶ > 1.34·10⁻⁶), so prop:is-iota, prop:is-logs (c) and prop:is-mult keep their form; no
X_k + f (0 < abs(f) ≤ 2, 2 ≤ k ≤ 50) is a square at 1007860, 1003580 or 1014000, so lem:s14-vector-distance's conclusion
abs((l + 1)² − X_k) ≥ 3 holds there, and no X_k (k = 3, …, 50) is a square, so no vector root is an integer; no point is
in a prop:t49-six interval; every root of C and of P_l with Re ι ≥ 3 is at least 3.4·10⁻⁵ above 3, and the vector
roots at least 4.86·10⁻⁶ (l = 2), as at 10⁻⁶.

### 4.1 The recommended point γ_C = 1,007,860

h = 1/1,007,860 = 9.92201298·10⁻⁷; ε₀ = e/h = 50393/5120; s_C = (1 − e_C)γ_C/2 = 503925.0788…; γ_C = 2²·5·7·23·313.
Numerically:

| quantity | at 10⁻⁶ (P-UB1, P-UB2) | at γ_C = 1,007,860 |
|---|---|---|
| Z₃ (real, non-real) | 2629 (1269, 1360) | 2638 (1272, 1366) |
| S₁, S₂ | 1207.936, 793.559 | 1212.686, 796.488 |
| μ_Z, attained at | 1.6747857·10⁻¹⁷, P_390, (356327, 1116082) | 2.934416·10⁻¹⁵, real root 2.1611320106331204329… of P_402, (81106, 2192182) |
| next excess (l) | 1.1076·10⁻¹⁵ (23) | 4.0236·10⁻¹⁵ (394) |
| ε_K, ε_+ (as P-UB1 rounds) | 1.6747·10⁻¹⁷, 1.67478·10⁻¹⁷ | 2.9344·10⁻¹⁵, 2.93441·10⁻¹⁵ |
| N̄_Λ | 909,507,124,095,312 | ≈ 912,802,448,0··,··· (+0.36 %; to be fixed by the certified sums) |
| D_NM (d_NM ≤) | < 7.57245·10⁵⁵ | < 4.354·10⁵³ (÷174.0) |
| 21D_NM + 6 | < 1.59022·10⁵⁷ | < 9.142·10⁵⁴ |
| K | < 1.66594·10⁵⁷ | < 9.577·10⁵⁴ |
| K* | < 1.11014·10¹¹⁵ | < 3.669·10¹¹⁰ (÷3.03·10⁴) |
| lower bound for the index sets as constructed (cor:is-lower: 3R ≥ 3(1 − 1.98·10⁻⁸)/(μ_Zδ̂)) | > 1.2251·10²⁷ | ≈ 6.99·10²⁴ |
| rem:ec-lb-unbounded threshold (d_NM > D_NM where h ≤ …) | 6.46·10⁻²⁹ | 8.53·10⁻²⁸ |
| μ♭_Z (𝔡₀ dropped), N♭_Λ | 3.548·10⁻¹⁰ (P_700), 3,683,190,611 | 3.124·10⁻¹⁰ (P_821), 3,697,439,516 |

Unchanged: ε_Υ, δ_50, δ̄, 𝔡₀, 𝔡₁, μ_G, Λ_ℬ, k̄_0 = 3, J_* = 15,000,015, l_* = 50 (P-UB1 §3's reasons do not use h; l_*
needs prop:is-logs, prop:is-mult and cor:sp-lstar at the new point, which the checks above support), the lower bounds of
thm:loss-d (ii), cor:uc-two-offsets and thm:ec-lb-proved (z only, or every h ≤ 10⁻⁶), and the bounds on δ and λ1
(prop:ec-delta-cap, through the lower bound). The index-set lower bound falls with μ_Z, as it must: at the new point
the two bounds for the index sets as constructed bracket d_NM in [7.0·10²⁴, 4.4·10⁵³] instead of [1.2·10²⁷, 7.6·10⁵⁵].

## 5. Cost, risk and gain of the move

### 5.1 Work

1. **Chapter 33, sec:s14-pa and sec:s14-exc-point at h = 1/1,007,860** (about 510 source lines, PDF pp. 607–615):
   every result keeps its statement and proof structure, and nearly every printed constant is recomputed: the opening
   constants, lem:s14-vector-distance (new Γ; the 2⁶5⁶ congruence sieve replaced by a direct check that no
   k² + γ_C(k − 2) ± f, f ∈ {1, 2}, 2 ≤ k ≤ 50, is a square — a 49-row table in place of nine numbers),
   lem:s14-scalar-zero, lem:s14-sextic-split (the polynomials c, Λ, Π at ε₀ = 50393/5120 and their bounds; x₋, x₊),
   lem:s14-sextic-count, lem:s14-sextic-small (x < 0.018 still means l ≤ 133; the P_2 bracket stays
   (2 + 2.93h, 2 + 2.94h), the root being at 2 + 2.9335h; x₋ moves from 0.018659 to about 0.01850, as
   24ε₀ − 20 = 1715/8 becomes 216.22, and the real/non-real split stays between l = 135 and l = 136),
   lem:s14-sextic-large (every row of sec:tab-a-pieces re-verified), lem:s14-crossings and prop:s14-damping-distance (margins pass, section 4), cor:s14-eps-ind-point,
   prop:t49-simple (new 𝔇), prop:t49-pairs (new 𝔖, 49 cubics), thm:t49-point, cor:t49-right (new κ₀).
2. **Chapter 96**: sec:tab-a and sec:tab-t49 regenerated (about 415 source lines, about 6 PDF pages, every number);
   sec:tab-is (P-UB1's T14) generated at the new h (about 2000 source lines, about 35 pages — the same size, as P-UB1
   adds it in any case; 1272 + 683 rows against 1269 + 680).
3. **Chapter 71 at the point**: def:ec-point, rem:ec-point-outside (s_C, citations), rem:ec-gauge-gap,
   lem:ec-theta-in-zero (one number), def:uc-choice, lem:uc-admissible, the sec:is opening, prop:is-iota (vector check
   with the new Γ), prop:is-logs (c) (one phrase), prop:is-mult (the l-window around x₋/h and its Δ values),
   sec:sp-point opening, lem:sp-roots (the l at which ι_v passes 5, the window around x₋), lem:sp-exceptional (the
   valuation table recomputed; if the 2- or 5-adic separation fails at γ_C = 2²·5·7·23·313, replace it by the finite
   check of the twelve cubics in κ, whose real roots lie at least 68 from every l(l + 2)), thm:sp-spectrum,
   cor:sp-lstar. About fifteen results, PDF pp. 1285–1311 in part.
4. **P-UB1's texts T1–T14 regenerated** at the new h (its scripts take h in three places), and **P-UB2's main set
   regenerated** by its mkproof.py at the new (ε_K, ε_+, N̄_Λ). Both are mechanical; P-UB2 needs ε_+ < 10⁻¹³, which
   holds.
5. **Summaries**: 00-front, 01, 03, 90 (P-UB2's O1–O4) and the chapter-71 summary (M1, M2), numbers only.
6. **Review**: a second reading of 1–4. This is the larger part of the cost: chapter 33's two sections were the
   chapter's heaviest numerical verification, and every constant is new.

If P-UB1 and P-UB2 are merged first at 10⁻⁶ and the move made afterwards, items 2 (sec:tab-is), 4 and 5 are done twice;
if the move is decided now, P-UB1's certification and P-UB2's evaluation should be run once, at the new point.

### 5.2 Risks, and their status at γ_C = 1,007,860

| risk | where it bites | status (numerical) |
|---|---|---|
| a root of □^C within about 2.94h of an integer | prop:s14-damping-distance, lem:s14-crossings | none: least distance 4.96·10⁻⁶ (vector root at l = 2, as at 10⁻⁶); all four crossing margins pass |
| a root within δ_50 of an integer | ε_ind(h) = δ_50 (def:ec-point, lem:uc-admissible, rem:ec-gauge-gap) | none |
| a real root of Z with Re ≤ 6 within 1.34·10⁻⁶ of ℤ | prop:is-iota, prop:is-logs (c), prop:is-mult | none: least 2.91·10⁻⁶ (P_2 near 2) |
| a near-double root (near x₋, or prop:t49-six) | lem:s14-sextic-small/large, prop:is-mult, lem:sp-roots | none: closest pair 1.2·10⁻⁴; h outside the prop:t49-six intervals |
| a root of 𝔇 or 𝔖 at some l(l + 2) | prop:t49-simple, prop:t49-pairs | generic; to be confirmed by the exact tables |
| P_l(q) = 0 for q ∈ Q, or the valuation argument failing | lem:sp-exceptional | conclusion holds (κ-roots ≥ 68 from every l(l + 2)); the written argument may change form |
| a row of sec:tab-is whose 10⁻²¹ enclosure does not fix n⁺, n⁻ or p_n | lem:is-gap-z | not checked; the 10⁻²¹ width over ε₀ gives about 2·10⁻⁹ per quantity, about 10⁻⁵ for the whole table; a finer enclosure for that row if it occurs |
| a root of Z in (3, 3 + ε_+] | (G) directly | none: the nearest is the vector root at 3 + 4.96·10⁻⁶ (l = 2); the nearest root of a P_l is 1.4·10⁻⁴ above 3 |
| the numerical scan missed a smaller excess | lem:is-gap-z | the certified table decides; the count (2638) matches the root counts by degree |

The one risk that is not numerical: the whole argument at the new point must be re-read, and every number in about
50 PDF pages of text and tables is new.

### 5.3 Gain

At γ_C = 1,007,860: d_NM, N_NM and K fall by a factor 174, K* by 3.0·10⁴ (section 4.1). The best of 2000 sampled points
gives 177.5, and a search of 10⁵ points would give perhaps 250–300 before the robustness filters; a gain beyond about
300 is not available from h. For comparison, dropping 𝔡₀ (if P-D0 succeeds) gives about 5·10¹⁷ (d_NM ≈ 1.4·10³⁸).

## 6. The comparison with 𝔡₀ dropped (one-dimensional lattice ι + q𝔡₁)

The least excess is then μ♭_Z(h) = min over Z₃ of (⌊y_ι/𝔡₁⌋ + 1)𝔡₁ − y_ι, the least of #Z₃ ≈ 2630 uniform draws on
(0, 𝔡₁): mean about 𝔡₁/#Z₃ ≈ 1.3–1.6·10⁻¹⁰. But (G) asks ε_K < ε_Υ = 1.4619·10⁻¹⁰ anyway (Step 4 of
prop:iii-i11-3-1 caps it near 0.998ε_Υ), so μ♭_Z(h) matters only when it is below ε_Υ, and otherwise
d_NM ≈ 2J′N♭_Λ²/(0.998·0.998ε_Υ) with N♭_Λ ≤ 59,377,257 + Σ(⌊y_ι/𝔡₁⌋ + 1), which grows as h decreases.

| h (γ_C) | μ♭_Z (l) | next | N♭_Λ ≤ | d_NM (scaling estimate) | vs 10⁻⁶ |
|---|---|---|---|---|---|
| 10⁻⁶ | 3.548·10⁻¹⁰ (700) | 4.241·10⁻¹⁰ | 3,683,190,611 | 1.43·10³⁸ | 1 |
| 1,007,860 | 3.124·10⁻¹⁰ (821) | 6.827·10⁻¹⁰ | 3,697,439,516 | 1.44·10³⁸ | 1.008 |
| 1,003,580 | 3.329·10⁻¹⁰ (954) | 4.817·10⁻¹⁰ | 3,689,687,302 | 1.43·10³⁸ | 1.004 |
| 1,014,000 | 4.246·10⁻¹⁰ (663) | 5.973·10⁻¹⁰ | 3,708,531,183 | 1.45·10³⁸ | 1.014 |
| 1,001,670 | 1.814·10⁻¹⁰ (814) | 2.996·10⁻¹⁰ | 3,686,222,619 | 1.43·10³⁸ | 1.002 |
| 1,005,000 | 6.31·10⁻¹¹ (761) | 2.061·10⁻¹⁰ | 3,692,261,939 | 3.31·10³⁸ | 2.33 |
| 1,004,340 | 2.11·10⁻¹¹ (483) | 1.380·10⁻¹⁰ | 3,691,065,303 | 9.88·10³⁸ | 6.93 |
| 1,000,240 | 3.72·10⁻¹² (362) | 7.490·10⁻¹¹ | 3,683,626,807 | 5.59·10³⁹ | 39.2 |

Over the two grids, μ♭_Z(h) > ε_Υ at 38 % (coarse) and 42 % (fine) of the points; h = 10⁻⁶ is one of them, and among
those it has the smallest N♭_Λ, so **with 𝔡₀ dropped no point of [5·10⁻⁷, 10⁻⁶] improves on 10⁻⁶** (the best
alternatives lose 0.1–1 %; a careless choice loses up to a factor 40). The h-dependence of the 1D lattice is thus the
opposite of the 2D one: there, h = 10⁻⁶ is in the lowest 5 %; here it is already optimal. (With ε_K near ε_Υ the
chain's I_lev, which assumes ε_+ < 10⁻¹³, must be re-derived; that is P-D0's matter, and the figures here use P-UB1's
scaling 2J′N̄²/(0.998ε_K).)

**Recommendation on sequence.** Decide P-D0 before moving h. If 𝔡₀ can be dropped, keep h = 10⁻⁶: the move would
gain nothing. If it cannot (or stays conditional), move to γ_C = 1,007,860: it gains 174 in the bound that is proved,
and it is also among the points at which a later 𝔡₀ result would need no second move (μ♭_Z > ε_Υ, 0.8 % cost). If the
author prefers a round number, γ_C = 1,014,000 has the same two properties with gain 107.

## 7. A cheaper route through P-TR (if it is merged)

proofs/P-TR.md, in its current revision (after R-P-TR's NOT CONFIRMED and the fix round F-P-TR it was revised again
for the repaired Λ; not re-read, not merged), proves the h-inputs uniformly: for h ∈ [h_m, 10⁻⁶) outside its exceptional
set 𝖩, ε_Υ ≤ ε_ind(h) ≤ δ_50, the exponents of ℰ^ι_ind, the simplicity on [−101, 5] and the pole orders at ι⁺
(thm:tr-transfer (i)); for every admissible h the lower bound d_NM > 2.0517·10¹⁰/μ(h) (ii); and, under a further
condition (R_h) (no root of P_l with hκ > 70 of real part in [2, 3 + ε_Υ)), the upper bound of prop:uc-dependence at
the gap μ(h) and the count N̄(h) (iii). Its prop:tr-mu-small is the rigorous form of section 3's observation: μ(h) has
no positive lower bound just below 10⁻⁶. With P-TR merged, moving the computational point needs at the new h only:
- h ∉ 𝖩: the roots near the integers 3, …, 51 located well enough to show a distance ≥ ε_Υ — the crossing check again,
  with tolerance ε_Υ instead of 2.94h (at γ_C = 1,007,860 the least distance is 4.96·10⁻⁶), and no multiple root for
  123 ≤ l ≤ 142 (closest pair 1.2·10⁻⁴);
- (R_h): cor:t49-right's two exact computations (𝒫(51; ·) and 𝔖(51, ·)) at the new h;
- μ(h) and N̄(h): P-UB1's sec:tab-is and lem:is-z3, lem:is-gap-z, prop:is-count at the new h, as in section 5.1 item 2,
  with the count of roots below 3 resting on P-TR's lem:tr-small and lem:tr-large plus direct enclosures of the roots
  with Re ι near 3 (P-TR's discs of radius 1/100 and 1/20 do not decide the side of 3 for some tens of degrees);
- the chain (P-UB2's script) and the summaries.
Chapter 33's sec:s14-pa and sec:s14-exc-point could then stay at 10⁻⁶ (used by no step of the settling proof), and
sec:sp-point and prop:is-iota/is-mult/is-logs at the point would cite thm:tr-transfer (i). The price: def:ec-point would
state ε_Υ ≤ ε_ind(h) ≤ δ_50 rather than ε_ind = δ_50 (all the chain needs), and P-TR needs its second reading. This
saves the chapter-33 rewrite (about 9 PDF pages and 6 table pages) at the cost of merging P-TR (about 700 source lines, some 12 pages);
it is the better route if P-TR is to be merged anyway.

## 8. Files

In /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/shpt/:
- polys.py, polys.pkl: the symbolic sextic and C (checked against sec:tab-a-sextic, eq:is-c-int, 𝒫_390);
- engine.py: roots, Z₃, m(y), μ_Z, μ♭_Z, S₁, S₂ at one h; drive.py: parallel grid; coarse.tsv, fine.tsv: the two
  grids (one row per γ_C);
- post.py, analyze.py, final.py: P-UB2's chain (imported from scratchpad/pub2/chain.py) at the scan's inputs;
  coarse_rank.txt, fine_rank.txt, final.out;
- epsind.py, qcheck.py, cand.py, cand.out: the robustness checks of section 4; crossm.py, cm1–cm4.out: the crossing
  margins; verify.py: the 80-digit and python-flint check of the recommended point;
- v1–v4.out: P-UB1's nine points reproduced.
