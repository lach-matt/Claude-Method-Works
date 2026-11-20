# R-P-UB1: review of proofs/P-UB1.md

Read: research/warp-drive/paper/reader/proofs/P-UB1.md, 2898 lines, md5 a4e10a41efcf0b396490ffad095af7dd, on branch
ccr-66909215-gi0qa5 at HEAD 4efdaefb (chapters/71-explicit-constants.md md5 427412e02c74261f1f87da24b60ddbca,
chapters/96-tables.md md5 f577ca6233dec4e08e68ef2262f451fb, the files the proof file quotes). Also read: STYLE.md,
chapter 71 sec:is, sec:uc-eval (def:uc-choice, lem:uc-admissible), prop:ec-rounds, thm:loss-d, rem:gap-sums,
cor:uc-two-offsets; chapter 33 prop:np-10-12, prop:np-10-54, sec:s14-pa (lem:s14-vector-distance, lem:s14-sextic-split,
lem:s14-sextic-count, cor:s14-remote-point, lem:s14-sextic-small, lem:s14-sextic-large), cor:t49-right; chapter 34
prop:iii-f1-2-3; chapter 41 def:iii-i10-1-1, def:iii-i10-1-3; chapter 42 def:iii-j-g-plus; chapter 96 sec:tab-a; P-I11's
definition of 𝒵; P-UB2 (md5 a3578a831de0dde5eae90ea295bc0202) for the overlap check; V-I11 §1. Nothing in the
repository was edited; assemble.py was run only in scratch copies.

## Verdict

**Not yet CONFIRMED: 0 Major, 2 minor, 6 nits.** The mathematics is right. My own exact check reproduces every row of
both tables, μ_Z and where it is attained, the next excess, the sums behind N̄_Λ, and every other number of the texts.
The two minors are a missing step in the proof of the count "Z₃ has 2629 elements" (distinctness across degrees, true
by the table, not argued) and a missing scope qualifier in T1 (μ_Z depends on h; rem:gap-sums just quantified over
h ∈ 𝖧). Both have exact replacement texts below, tested in a scratch merge. With them applied the file is CONFIRMED.

## Findings

### minor 1. lem:is-z3: the count 2629 needs the roots of different degrees to be distinct

*Where.* P-UB1.md:401–405 (T7, proof of lem:is-z3, *Counting.*), with the table head P-UB1.md:824–825 (T14,
sec:tab-is-real, *Object.*).

*Current text (401–405).*

```
*Counting.* For each l the intervals and discs of its rows, with the conjugate discs, are pairwise disjoint (their
printed numbers differ by more than 2·10⁻²¹), lie in {2 < Re ι < 3}, and do not contain 2. So they hold distinct roots
of real part greater than 19/10, other than 2: one for l = 0; two for l = 1; three for 2 ≤ l ≤ 815 (for
136 ≤ l ≤ 815 a real root and a conjugate pair); one for 816 ≤ l ≤ 999. By the counts above, for l ≤ 815 every root of
C and of P_l of real part greater than 19/10, other than 2, lies in exactly one of these intervals and discs.
```

*What is wrong.* Z is a set. lem:is-z3 (b) states "Z₃ has 2629 elements, 1269 real and 1360 non-real", which needs the
roots of different rows to be distinct numbers. The proof shows disjointness only among the rows of one l. Nothing
excludes a priori a common root of P_l and P_l′ (for fixed ι, P_l(ι) is a cubic in κ, so up to three degrees can share
a root). For the non-real roots, distinctness across l is in the table head (b increases with l by more than 2·10⁻²¹)
and is used in the proof of prop:is-count (a), but not here. For the real roots nothing in the text says it. It is
true: I checked that any two entries r of the first table differ by more than 5.09·10⁻⁷ (least gap between l = 514,
j = 1 and l = 118, j = 2). The upper bound for N_Λ is unaffected (a sum over rows bounds a sum over elements), so only
the stated count needs it.

*Replacement (7 lines, for 401–405).*

```
*Counting.* The intervals and discs of all the rows, with the conjugate discs, are pairwise disjoint: any two numbers
r of the first table differ by more than 2·10⁻²¹, the numbers b of the second table increase with l by more than
2·10⁻²¹, and every b exceeds 10⁻²¹. They lie in {2 < Re ι < 3} and do not contain 2. So the roots of different rows are
distinct, and they are roots of real part greater than 19/10, other than 2: one for l = 0; two for l = 1; three for
2 ≤ l ≤ 815 (for 136 ≤ l ≤ 815 a real root and a conjugate pair); one for 816 ≤ l ≤ 999. By the counts above, for
l ≤ 815 every root of C and of P_l of real part greater than 19/10, other than 2, lies in exactly one of these
intervals and discs.
```

*And in T14 (824–825), current:*

```
*Object.* For each row, the j-th real root, in increasing order, of real part in (2, 3) of P_l (of C for l = 0); it
lies in (r, r + 10⁻²¹). The rows are those of [[lem:is-z3]] (c).
```

*replacement (3 lines):*

```
*Object.* For each row, the j-th real root, in increasing order, of real part in (2, 3) of P_l (of C for l = 0); it
lies in (r, r + 10⁻²¹). The rows are those of [[lem:is-z3]] (c). Any two entries of the column r differ by more than
2·10⁻²¹.
```

### minor 2. T1 (rem:gap-sums): μ_Z is stated without its point

*Where.* P-UB1.md:192–194 (T1, the new last sentence of rem:gap-sums, 71:169–170 at HEAD).

*Current text.*

```
contains further sums and the elements that the generator 1 + 𝒵 of [[def:iii-i10-1-1]] produces, and (G) holds
exactly for ε_K < μ_Z ≈ 1.6748·10⁻¹⁷ ([[thm:is-gap]]); on the part of Λ built from the other generators the least
excess above 3 is μ_G ≈ 1.6416·10⁻¹⁴.
```

*What is wrong.* The sentence before it in rem:gap-sums speaks of every h ∈ 𝖧 ("[[thm:settling]] takes
ε_K < ε_ind(h) ≤ δ_50 < 5.019·10⁻⁸ for every h ∈ 𝖧"). The old last sentence (μ_G) was true at every such h, Λ_ℬ
depending only on the gauge parameters. The new one is true only at the computational point: Z₃, and with it μ_Z,
moves with h (the file's own §2.2 and §6 say so, e.g. about 1.46·10⁻¹⁵ at h = 9.6·10⁻⁷). Unqualified, after a sentence
quantified over h, it reads as a statement for every h, and is then false.

*Replacement (3 lines).*

```
contains further sums and the elements that the generator 1 + 𝒵 of [[def:iii-i10-1-1]] produces; at the computational
point (G) then holds exactly for ε_K < μ_Z ≈ 1.6748·10⁻¹⁷ ([[thm:is-gap]]), and on the part of Λ built from the other
generators the least excess above 3 is μ_G ≈ 1.6416·10⁻¹⁴.
```

### nit 1. lem:is-z3, *The rows.*: the letter r is the table column and the radius

P-UB1.md:393–394. Current:

```
With M = 7·10²¹ and r = 10⁻²¹, so that Mr²/2 = 3.5·10⁻²¹, every row satisfies the last condition of [[lem:is-disc]]
for 𝒫_l: 10¹³²𝒫_l(c) and 10¹¹⁰𝒫_l′(c) are Gaussian integers, and in every row
```

Two sentences earlier r is the column of the first table. Replacement (2 lines):

```
In [[lem:is-disc]] take the centre c, the radius 10⁻²¹ and M = 7·10²¹, so that Mr²/2 = 3.5·10⁻²¹ there; every row
satisfies its last condition for 𝒫_l: 10¹³²𝒫_l(c) and 10¹¹⁰𝒫_l′(c) are Gaussian integers, and in every row
```

### nit 2. T12 (cor:is-flat): "now"

P-UB1.md:717: "increments only those of real part below 1, which are now 𝔡₁ alone; so every element of Λ ∖ Λ_ℬ has
real part greater". "now" is on STYLE's list; here it means "for ℰ′_ind". Replacement line:

```
increments only those of real part below 1, for ℰ′_ind 𝔡₁ alone; so every element of Λ ∖ Λ_ℬ has real part greater
```

### nit 3. T2: "for every ε_K that [[def:iii-i10-1-3]] allows" is circular

P-UB1.md:304. def:iii-i10-1-3 contains (G) itself; what is meant is the bound ε_K < ε_Υ it asks besides (G). Current
line:

```
3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰, so for every ε_K that [[def:iii-i10-1-3]] allows, and N_Λ ≤ 3,683,190,611
```

Replacement line:

```
3.548125563·10⁻¹⁰ < μ♭_Z < 3.548125564·10⁻¹⁰, so for every ε_K < ε_Υ ([[def:iii-i10-1-3]]), and N_Λ ≤ 3,683,190,611
```

### nit 4. T14 heading wording

P-UB1.md:797: "### Tables for the roots of the damping polynomials below the real part 3 {#sec:tab-is}". Replacement:

```
### Tables for the roots of the damping polynomials of real part below 3 {#sec:tab-is}
```

and in the crosswalk row of sec:tab-is (P-UB1.md:2842) "the roots of the damping polynomials of real part below 3".

### nit 5. T14 header: "The column (p, q)"

P-UB1.md:806, "The column (p, q) gives the pair": there are two columns. Replacement line (110 characters):

```
p, q ∈ ℕ₀ ([[lem:is-reduction]]). The columns p and q give the pair at which m(y) is attained, p = 0 meaning
```

### nit 6. §4 merge note is stale against the current P-UB2

P-UB1.md:153–158 says lint.py --paper finds four lines over 121 characters in P-UB2's M6, M7, M13. With P-UB2 at md5
a3578a83… (which states it was regenerated at these inputs) the joint merge gives lint.py --paper 0 hits and no line
over 121 characters. A note to the coordinator, not paper text; it can say "0 hits with P-UB2 a3578a83".

The six nits were applied, together with the two minors, to a scratch merge (scratch/rpub1/fixed): lint.py --chapters 0
hits (4792 labels), assemble.py --check and assemble.py 0 problems, lint.py --paper 0 hits, longest line 121
characters in chapters 71, 96 and PAPER.md. (Nits 5 and 6 were not part of that test; nit 5 lengthens one line to
110 characters, nit 6 is outside the texts.)

## The independent table check

Written from scratch before looking at the writer's directory:
scratchpad/reader/rpub1check/check.py (with merge2.py, census.py, fix/). Integers and Fractions only; no floating
point decides anything. It parses the two tables as printed in T14 and uses only printed numbers and the printed
bounds of lem:is-offsets (b).

- **Inputs re-derived.** The table of sec:tab-a-sextic equals 64·10¹⁸ det(hN_l(ι)) of eq:s14-nl at
  (v, e, h) = (1/2, 1/102400, 10⁻⁶) identically in (ι, κ) (exact bivariate expansion); P_0 = −(ι − 2)C and
  eq:is-c-int = 102400·10¹²C exactly; 𝒫_390 as printed. The printed bounds for 𝔡₀, 𝔡₁, ε₀ of lem:is-offsets (b)
  contain rigorous integer-square-root enclosures (scale 10⁶⁰), and the ε₀ bounds follow from those for 𝔡₀, 𝔡₁.
- **Row pattern.** 1269 and 680 rows; l = 0 one, l = 1 two, 2 ≤ l ≤ 135 three, 136 ≤ l ≤ 999 one; second table one for
  each 136 ≤ l ≤ 815; j = 1, 2, 3 in increasing r. r has 21 decimals, a and b 22.
- **Real rows.** For all 1269: 10¹²⁶𝒫_l (10⁶³𝒫_0) at R and R + 1 (R = 10²¹r) are nonzero integers of opposite signs;
  2 < r, r + 10⁻²¹ < 3; rows of one l are more than 2·10⁻²¹ apart; any two r overall more than 5.09·10⁻⁷ apart.
- **Non-real rows.** For all 680, with X = 10¹³²𝒫_l(c), Y = 10¹¹⁰𝒫_l′(c) Gaussian integers, the integer inequality
  |Re X| + |Im X| + 35·10¹¹⁰ < 10·max(|Re Y|, |Im Y|) holds (this is the printed condition times 10¹³²); the largest
  ratio of the two sides is 0.0966. a < 3, b < 3, b > 10⁻²¹, a ± 10⁻²¹ ∈ (2, 3), a² + b² < 36; b increases with l,
  the least step 3.70·10⁻³. The majorant: max over 136 ≤ l ≤ 815 of Σ k(k − 1)|π_k(κ)|6^(k−2) is
  6,826,040,157,841,263,270,178 < 7·10²¹, and each link of the printed chain (|π₂| < 1.10914·10²¹, |π₃|, |π₄|, the
  five terms, < 7·10²¹) holds exactly for every 1 ≤ l ≤ 815.
- **Least excesses.** For all 1949 rows, on the printed y-intervals: n⁺ and n⁻ determined at both ends, n⁺ − n⁻ ≤ 2,
  every p_n determined (also where 4p_n > n), the candidates of lem:is-reduction enclosed both as p𝔡₀ + q𝔡₁ − y and as
  p_nε₀ − θ_n (each form alone also passes); in every row the minimiser is unique with a margin (its upper bound below
  every other candidate's lower bound), it is the printed (p, q), and the printed m equals its lower bound rounded down
  to five significant figures (all 1949 rows). Least: row l = 390, j = 1, (356327, 1116082), lower bound
  1.674772·10⁻¹⁷ from the 10⁻²¹ interval; next 1.1076143078·10⁻¹⁵ (l = 23, j = 2, (305806, 1751938)), then
  1.3074150·10⁻¹⁵ (l = 417), 1.5347861·10⁻¹⁵ (l = 874). Every row other than (390, 1) has m(y) ≥ 1.1076·10⁻¹⁵ and
  printed m ≥ 1.1076·10⁻¹⁵; in row 390 the other candidate exceeds 1.3537·10⁻⁷.
- **ι_* and μ_Z.** 𝒫_390(r_*) = 2.15539·10⁻⁴ > 2.155·10⁻⁴, 𝒫_390(r_* + 10⁻²⁴) = −4.17698·10⁻⁵ < −4.17·10⁻⁵;
  (r_*, r_* + 10⁻²⁴) lies in the row's interval; y-interval as printed; n⁺ = 2541390, n⁻ = 2541389, θ_n/ε₀ ∈
  (356326, 356327); the two product bounds contain the products of the printed bounds. The printed sum's lower end
  equals the sum of the two printed lower ends exactly, and the printed μ_Z interval (1.674785657·10⁻¹⁷,
  1.674785869·10⁻¹⁷) is exactly (sum bound − y bound); every inequality used is strict, so the open intervals are
  right. μ_Z ∈ (1.6747856·10⁻¹⁷, 1.6747859·10⁻¹⁷) = eq:is-mu-z.
- **Census.** 56 elements of Λ ∖ Λ_ℬ in (3, 3 + 1.6416·10⁻¹⁴] and 1144 in (3, 3 + 4.2·10⁻¹³], counting every candidate
  of the minimum (none undecided), R-V-I11's figures.
- **Sums.** Over upper ends (non-real rows twice) S₁ = 1207.9363079930 < 1207.93630800 and S₂ = 793.5592580999 <
  793.55925810; over lower ends of the non-real rows, twice, 150.7079167024 > 150.70791670.
  1125001468750.4 < 1/(2𝔡₀𝔡₁) < 1125001468750.5; δ̄ + 𝔡₀ + 𝔡₁ < ν₀ = 1.69·10⁻⁶.
- **N̄_Λ recomputed.** (S₂ + 2ν₀S₁ + 2629ν₀²)·1125001468750.5 with the printed S's is 892,759,924,095,312.2186… <
  …312.22 (with the exact sums 892,759,924,095,195); plus 16,747,200,000,000 gives 909,507,124,095,312.22, so
  N_Λ ≤ 909,507,124,095,312. Lower bound: 16,206,600,000,000 + 150.70791670·1125001468750.4 = 185,753,227,639,812.9…
  > 1.85753·10¹⁴.
- **cor:is-flat.** Least (n⁺ + 1)𝔡₁ − y at l = 700 (non-real), n⁺ = 394194, y-interval as printed, μ♭_Z ∈
  (3.548125563, 3.548125564)·10⁻¹⁰; next 4.2406821·10⁻¹⁰ at l = 869; Σ(n⁺ + 1) = 3,623,813,354 over Z₃ and
  1,227,124,256 over the non-real ones; 56,436,656 + 1,227,124,256 = 1,283,560,912, 59,377,257 + 3,623,813,354 =
  3,683,190,611.
- **Other numbers.** (500002 + 4.99·10⁻⁶)² = 250002000008.99001996… < Γ + 9; least r 2.000002932350446240725 at
  (2, 1); largest r + 10⁻²¹ or a + 10⁻²¹ is 2.99998560201713… (l = 999) < 2.99998561; least a 2.51411628819699…
  (l = 136); x at l = 816 is 0.667488 with a(x) − 3 = 6.16·10⁻⁴ exactly; 8365·8367 ≤ 7·10⁷ < 8366·8368; x = 1.002 at
  l = 1000; Δβ_0 = 0.999²·16747/10²¹ = 16713522747/10²⁷ exactly; ε′_0 = ½(ε_+ − ε_K) = 4·10⁻²² exactly; cor:is-lower:
  3ε_K + 2δ̂ + δ̄ < 1.98·10⁻⁸, ε_Kδ̂ < 2.44878·10⁻²⁷ at 1.6747859·10⁻¹⁷ and < 2.44865·10⁻²⁷ at 1.6747·10⁻¹⁷,
  R > 4.08366·10²⁶, 3R > 1.2250·10²⁷, 21·1.2250·10²⁷ = 2.5725·10²⁸, and 3R > 1.2251·10²⁷ at the choice.
- **Negative controls.** Perturbing one r (l = 500), one a (l = 500), one m (row 23/2 to 1.1077·10⁻¹⁵) and one (p, q)
  (row 10/1) each makes the check fail at that row.

Compared afterwards with the writer's notes (§8 of the file): the same majorant (6.826·10²¹), the same disc ratio
(≤ 0.097), the same least, next and third excess, the same census. No disagreement.

## What I checked and found correct

- **lem:is-disc.** Taylor with integral remainder on the segment, |P − L| ≤ Mr²/2 < r|P′(c)| − |P(c)| ≤ |L| on the
  circle, Rouché, the one root c − P(c)/P′(c) of L inside (P′(c) ≠ 0 follows from the hypothesis), so exactly one root
  with multiplicity, hence simple; the sufficient condition by |w| ≤ |Re w| + |Im w| and |w| ≥ max(|Re w|, |Im w|).
  The per-row inequality is exactly the one my integer check tests.
- **lem:is-z3, the count from the chapter-33 lemmas.** Z = the C root above 2, the P_l roots of real part above 19/10
  other than 2, the larger p_(v) roots for l ≥ 2 (prop:is-iota); C has one, P_l three (counted with multiplicity, 2
  among them at l = 1) of real part above 19/10 (prop:np-10-54 (i), (ii) and the proof). For l ≤ 815 the rows give
  that many distinct roots in (2, 3), so all of them; for 816 ≤ l ≤ 8365 (x ∈ [0.667488, 70]) lem:s14-sextic-large
  (a), (c) give ι_B, ι_P, ῑ_P (three distinct roots, of real part above 19/10 by their bounds, so the three); Π < 0 on
  [0, 35] (Π⁰ convex, Π⁰(0) < −79.6, Π⁰(35) < −423, |Π − Π⁰| < 0.57), so Re ι_P > a(x) − e_P ≥ a(x) − 11h on [0.5, 4]
  (row e_P/h = 11), > 3 + 6·10⁻⁴; on [4, 70], > 5.49 (|Π| ≤ 1994.17, e_P ≤ 72h); ι_B ≥ 3.002 − 39.004h on [1.002, 4]
  (c ≤ 39, e_B = 0.004h), ≥ 6 − 321.1h on [4, 16], ≥ 18 − 5184h on [16, 70]; for 816 ≤ l ≤ 999 the table's real root is
  ι_B; l ≥ 8365 by cor:t49-right. The vector roots exceed 3 + 4.99·10⁻⁶ (increasing in l, l = 2 by the printed square).
  So (a), (b) (with minor 1) and (c) hold, and the gap 4.99·10⁻⁶ above 3 is the l = 2 vector root.
- **prop:is-lambda.** 1 + 𝒵 = {3} ∪ {ι ∈ Z : Re ι < 4} from prop:iii-f1-2-3's list (after the semicolons: 2, integers
  ≥ 3, numbers 1 + ι^Υ above 3, the ι^C_(·,+) − 1; the root 3 of □^C at v1 removed; before them real part ≤ 0) and
  P-I11's 𝒵 (0 < Re μ < 3). Generators of Re ≥ 3 give > 3 + ε_+; from ι ∈ Z₃ the increments below 1 are 𝔡₀, 𝔡₁
  (eq:is-low, prop:is-iota), one of real part ≥ 1 gives > 3 + 2.932·10⁻⁶. The two displayed equalities, reality of
  Λ_ℬ ∩ {Re ≤ 3 + ε_+}, real part > 2.514 of the non-real elements, reality of Λ ∩ {Re ≤ 2.514}, and Re > 2 + 2.932·10⁻⁶
  on Λ ∖ Λ_ℬ all follow.
- **lem:is-gap-z and lem:is-reduction's use.** The hypotheses y/𝔡₁, 4y/𝔡₀ ∉ ℤ follow from the equal floors at both
  ends (strict open intervals); the minimum has at most three numbers; the "Moreover": a positive p𝔡₀ + q𝔡₁ − y not in
  the minimum set exceeds ε₀ > 5.5·10⁻¹³ or 𝔡₁, so every one below 1.1076·10⁻¹⁵ is in the minimum set, and the rows
  leave only μ_Z.
- **thm:is-gap, both directions.** If ε_K < μ_Z: Λ_ℬ meets no window for ε_K < μ_G; Λ ∖ Λ_ℬ misses the first window
  (Re > 2 + 2.932·10⁻⁶) and the third (Λ + 𝔡_i ⊂ Λ); in the second its least excess is μ_Z. If ε_K ≥ μ_Z, the real
  element 3 + μ_Z ∈ Λ (ι_* ∈ 1 + 𝒵, 𝔡₀, 𝔡₁ increments) lies in (3, 3 + ε_K]. Same for (G⁺) with ε_+. 3 + μ_Z ∉ Λ_ℬ
  (Λ_ℬ has nothing in (3, 3 + μ_G)), so it is the only element in (3, 3 + 1.1076·10⁻¹⁵). The old proof's remainder
  reads correctly as the part Λ_ℬ after T8's "An element of Λ_ℬ in" and T9.
- **prop:is-count (a).** Upper bound N_ℬ + Σ_rows T(y + ε_+) with T(X) ≤ (X + 𝔡₀ + 𝔡₁)²/(2𝔡₀𝔡₁) and
  ε_+ + 𝔡₀ + 𝔡₁ < ν₀ for all ε_+ < δ̄; lower bound from the non-real families (distinct by lem:is-offsets (c), not real,
  distinct across ι by Im). Recomputed above. (b), (c) and cor:sp-lstar unchanged: the repair adds a generator, not an
  increment, and k̄_0's sets below 2λ_♯ do not involve 1 + 𝒵.
- **The choice.** ε_K = 1.6747·10⁻¹⁷ < μ_Z, ε_+ = 1.67478·10⁻¹⁷ < 1.6747856·10⁻¹⁷ < μ_Z; 0 < ε_K < ε_+ < min(δ_♯, ε_ind);
  ε_K < ε_Υ; (η_1, η_2) ⊂ (ε_K, ε_+) nonempty; ε_K + ε ≤ 1.6747·10⁻¹⁷ + 1.4619·10⁻¹³ < ε_g; ε′_0 = 4·10⁻²² < 0.001ε_K,
  so 0.999ε_K ≤ α − 4 ≤ ε_K; Δβ_0 ∈ (0, 1]; (Ex1) by (G⁺), (Ex2), (H4), the levels, a♭_K and α_0 as before; ε_+ < 10⁻¹³
  as P-UB2 needs. Every condition of def:uc-choice and lem:uc-admissible holds.
- **𝔡₀ (thm:is-d0, cor:is-flat).** thm:is-d0 is unchanged. cor:is-flat is stated under "Suppose c_b = 0 for every b
  near b₀"; its proof is correct (Λ ∖ Λ_ℬ families ι + q𝔡₁, least excess (n⁺ + 1)𝔡₁ − y, the counts). T2 and T13 state
  it conditionally ("If c_b vanishes", "decides whether"); nothing conditional is stated as proved. T13's "or only
  below μ_Z" is right for any index sets that keep both offsets (3 + μ_Z ∈ Λ then).
- **cor:is-lower.** prop:ec-rounds' bound decreases in ε_K; numbers above; thm:loss-d (ii) gives d_NM ≥ d_acc ≥ 3R.
- **Placement.** All 14 old texts occur exactly once as whole lines at the stated lines of the HEAD files and are
  pairwise disjoint (own merge script). Scratch merge from a git archive of HEAD in scratch/rpub1/alone: lint.py
  --chapters 0 hits (4782 → 4792 labels, the ten new ones), assemble.py --check 0 problems, assemble.py 0 problems,
  lint.py --paper 0 hits; longest line 121 characters (counted as characters) in the merged chapters 71, 96 and in
  PAPER.md; no line of the new texts starts with "+ ", "- ", "* ", "> ", "#" (other than headings), "=" or "|"
  (other than table rows); no trailing spaces or tabs. With P-UB2's main set (M1–M26, O1–O4; P-UB2 md5 a3578a83…) in
  scratch/rpub1/both: 50 blocks, no overlap, 4794 labels, 0 problems, lint.py --paper 0 hits. The fallback set
  (F1–F9, FO1–FO7) also overlaps none of T1–T14.
- **Crosswalk.** Ten rows, four tab-separated columns; each PENDING line number is the line of its label (339, 349,
  351, 361, 492, 496, 584, 797, 822, 2101); the anchors keep chapter order.
- **Self-containedness.** No program, file, code or computation citation in T1–T14; every step is arithmetic on printed
  numbers (integer signs, Gaussian-integer inequalities, floors of quotients of printed bounds, sums of printed ends),
  with Appendix B carrying the objects, headed by their definition and the results that use them.

## Notes for the coordinator (not findings)

- T1, T2, T7, T13 cite "the generator 1 + 𝒵 of [[def:iii-i10-1-1]]", which exists only with P-I11 merged: merge P-I11
  first or together.
- Merged alone, T7 leaves lem:uc-lambda (c) and lem:cs-fourier (b) citing prop:is-lambda for reality of all of
  Λ ∩ {Re < 3 + ε_+}; P-UB2's M9 and M15a repair those (the file's §6 says so). Merge P-UB1 with P-UB2's main set.
- thm:loss-d (71:1494, "(G) asks ε_K < μ_G") and cor:uc-two-offsets, rem:uc-offset-d0 (1.6417·10⁻¹⁴) stay true and
  weaker; cor:is-lower could be cited there, as the file says.
