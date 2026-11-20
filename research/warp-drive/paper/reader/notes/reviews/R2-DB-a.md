# R2-DB-a: confirming reading of the F-DB-a fixes (P-U71-close, P-U71-assembly, P-U71-IS)

Reader: R2-DB-a (independent; changed nothing in the repository). Texts as read, unchanged during the reading:
proofs/P-U71-close.md (575 lines, md5 14b1cb4431c56bf5e5c20e122e5404f7), proofs/P-U71-assembly.md (635 lines, md5
8e95e76c371c27dcccd840b9ff1db516), proofs/P-U71-IS.md (662 lines, md5 0bee2e2588fcaa33c72af282a69d425f). Baseline
18a19178 (close 5716048…, assembly 76949f9…, IS a455d37…, the md5s R-DB-2 read). Inputs read at every cited place:
notes/reviews/R-DB-2.md (all), R-DB-1.md (finding 10, arithmetic), notes/reports/F-DB-a.md; chapters 35 (lem:iii-g1-1-3),
36 (def:iii-c-3-1, eq:iii-c-3-1), 38 (eq:iii-i-1-4), 40 (sec:iii-i8-1, admissible levels, lem:iii-i8-3-1, lem:iii-i8-3-2,
prop:iii-i8-4-1 and proof, sec:iii-i9-1), 41 (sec:iii-i10-1 with (H4), def:iii-i10-1-3, sec:iii-i11-1, sec:iii-i12-1,
def:iii-i13-1-1), 42 (sec:iii-j-1, def:iii-j-g-plus, def:iii-j-a-j, thm:iii-j-2-4, lem:iii-j1-1-1, thm:iii-j1-2-1,
sec:iii-i14-1), 43 (sec:iii-j2-1, sec:iii-j3-1, def:iii-j3-1-3, lem:iii-j3-1-4, cor:iii-j3-6-6), 46 (prop:iii-k-1-2,
lem:iii-k-2-2, thm:iii-k-3-2 Smallness, the choice table w1–w2, d2, thm:vi-c-2-1 (4)); P-U71-cstar.md (sec:cs intro,
def:cs-choices, lem:cs-fourier, lem:cs-levels, lem:cs-base, lem:cs-iterations, lem:cs-rest, prop:cs-cstar,
rem:cs-sharpness), P-U71-SP.md (cor:sp-lstar (d)), P-U71-forward.md (thm:fwd-loss statement).
"cl. n", "as. n", "IS n" are lines of the current files.

Private checks, exact (fractions; mpmath at 60–90 digits), in scratchpad/reader/scratch/r2_db_a/ (check1.py, check2.py,
check3.py, form.py): every number listed in item 2 below, an independent recomputation of the least excess above 3 of
Λ, the real parts of ℰ^tot_I near 3, line lengths and wrapped-line prefixes.

## Verdicts

- **P-U71-close: CONFIRMED** — 0 Major, 0 minor, 1 nit (N1).
- **P-U71-assembly: CONFIRMED** — 0 Major, 0 minor, 0 nit.
- **P-U71-IS: CONFIRMED** — 0 Major, 0 minor, 0 nit.

Every finding of R-DB-2 (C1–C6, A1–A3, O2) and R-DB-1's finding 10 is resolved correctly; the two additions of the
writer are true; no evaluated number moves; the diff contains only these fixes; the six cstar keys exist and say what
close uses.

## 1. The findings (task 1)

**C1 (Major) — resolved.** ε_+ := 1.64160217·10⁻¹⁴ (cl. 343).

- *ε_K < ε_+ < μ_G.* Exactly: ε_+ − ε_K = 217·10⁻²² = 2.17·10⁻²⁰ > 0; μ_G = 1.6416021719712707792…·10⁻¹⁴ (90 digits
  from the closed forms of lem:is-offsets (a)), so ε_+ < 1.64160217197·10⁻¹⁴ < μ_G, with μ_G − ε_+ ≈ 1.97·10⁻²³.
- *Every condition on ε_+.* I collected the conditions the chapters and texts place on ε_+: eq:iii-i9-1-1
  (0 < ε_K < ε_+ < min(δ_♯, ε_ind)); (H4) (ℓ_I > 3 + ε_+, ℓ_I ≤ a_I, so a_I > 3 + ε_+ of the class); ch. 38's
  ε_+ < min(ε_ind, ε_I) < 1 (a_I = 3 + ε_I); ch. 46's row w1 and thm:vi-c-2-1 (4) (ε_+ < min(δ_♯, ε_ind, ¼, ℓ_I − 3),
  (G⁺), (Ex1)–(Ex2)); def:iii-j-g-plus (G⁺); def:iii-j3-1-3 (Ex1), (Ex2); def:iii-j-a-j (ℓ_K(λ₀) ∈ (0, 3) needs
  ε_+ < ¼); prop:is-lambda and prop:is-count (ε_+ < δ̄ = 1.94137057·10⁻⁸, and ε_+ < 𝔡₁ for T(ε_+) = 1); cor:sp-lstar (d)
  (ε_+ < δ_50); prop:uc-ltf (ε_+ < δ_♯ < ¼); ch. 43:766, 783–784 (ε_+ < ε_ind); and the relative ones, which only make
  later choices smaller: δ_+ ∈ (0, ε_+ − ε_K) (sec:iii-i12-1), 2ε < ε_+ − η_2 (sec:iii-i11-1), 5ε_1 < ε_+ − η^0_2
  (ch. 43:104), η_2 = ε_+ − 3ε and τ_3 = 1 + ε_+ − 5ε > 1 + ε_K (lem:iii-j1-1-1, ch. 43:110–112). All hold:
  ε_+ < 10⁻¹³ < 1.9413·10⁻⁸ < δ_50, ε_+ < δ̄ < 𝔡₁, ε_+ < 0.0099 = δ_♯, ε_+ < ℓ_I − 3 by the choice of ℓ_I.
- *(G⁺) and (Ex1) (cl. 370–373).* True. That 3 + μ_G is the least real part above 3 in Λ follows from thm:is-gap's
  statement itself ((G) holds for every ε_K < μ_G, so no element has real part in (3, 3 + μ_G), and
  λ_♯ + 1109655𝔡₀ + 31682𝔡₁ ∈ Λ), and its proof says so. I recomputed it independently over the 29 numbers of ℬ by the
  reduction of lem:is-reduction: the three least excesses above 3 are μ_G (β = λ_♯), 2.3181480702·10⁻¹⁴
  (β = λ_♯ + 1 + δ′₁) and 8.0959353087·10⁻¹⁴ (β = λ_♯ + 1 + δ₂), the next 4.594·10⁻¹³; and prop:is-lambda makes every
  element below 3 + ε_+ real. So (G⁺) ⟺ ε_+ < μ_G, and (Ex1), being (G⁺) with its closed endpoint, holds.
- *(Ex2) (cl. 373–375).* True. With the least ℰ^C_I = {(1 + n/2 + c, 0)} (prop:is-ci-pp (a)) and the part
  (3/2 + s, 0) + ℕ₀ of eq:iii-c-3-1, the real parts of ℰ^tot_I are 3 and numbers at distance ≥ 0.0099 from 3 (exact
  enumeration: in (2.9, 3.1) they are 3, 3.0099, 3.01, …; below 3 the largest is 2.56); 3 + ε_+ is none of them, and
  λ_♯ = 1.5099 ≠ 3 + ε_+.
- *(H4), C3 (cl. 346, 375–376).* "with ℓ_I ≤ a_I" is placed in def:uc-choice and the existence argument now uses it:
  (3 + ε_+, min(3.5, a_I)] is a non-degenerate interval as a_I > 3 + ε_+, and the exclusions are discrete.
- *α, (A_J), (Ex3)–(Ex4) (cl. 350–351, 382–387).* def:iii-i10-1-3 gives ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
  1.085·10⁻²⁰ exactly, < 0.001ε_K = 1.6416·10⁻¹⁷, so every admissible α ≥ 3 has ε_K − ε′_0 < α − 4 ≤ ε_K, hence
  0.999ε_K ≤ α − 4 ≤ ε_K. (A_J), (Ex3), (Ex4) remove finitely many values (lem:iii-j3-1-4 for (Ex3)–(Ex4)), so such α
  exist. These are the conditions of sec:iii-j3-1 (α admissible in (4 + ε_K − ε′_0, 4 + ε_K], (A_J), def:iii-j3-1-3)
  and of the setting of sec:iii-j-1 ("α with (A_J), (G⁺)") in which thm:iii-j-2-4 and thm:iii-j1-2-1 are stated.
- *The writer's first addition (cl. 385–386), why (A_J) excludes only finitely many α: true.* ℓ_K(λ₀) = α − Re λ₀ lies
  in (0, 3) (def:iii-j-a-j); the roots μ of L̂_(b₀)(0) are real and discrete (sec:iii-i8-1, ch. 40:726–729;
  prop:iii-f1-2-3), so finitely many −Re μ lie in (0, 3); ℰ_K is an index set independent of α (lem:iii-g1-1-3 (a)),
  so finitely many Re π_1ℰ_K lie in (0, 3); and Λ ∩ {Re < 3 + ε_+} is finite (lem:iii-i10-1-2 (a)). So the excluded α
  are the finitely many Re λ₀ + x.
- *lem:uc-admissible's extended statement (cl. 356–359).* Each item is proved: thm:iii-i14-3-1, lem:iii-i8-3-2,
  prop:iii-i13-2-1 (as before, with def:iii-i13-1-1's conditions on ε now named); prop:iii-i8-4-1 (the α_0 paragraph,
  below); thm:iii-j-2-4 and thm:iii-j1-2-1 ((G⁺), (A_J), and ε within sec:iii-j2-1's ε_1); the exact scales of
  cor:iii-j3-6-6 (admissibility in (4 + ε_K − ε′_0, 4 + ε_K], (A_J), (Ex1)–(Ex4)); (G) and (G⁺) hold.
- *(j) (cl. 484).* (1 + 10⁻¹³) · 3.0000026·10⁶ + 2 = 3,000,004.60000030000026 < 3.000005·10⁶ (true value
  (1 + ε_+)/𝔡₁ + 2 = 3,000,004.58333…); η_2 − η_1 < ε_+ < 10⁻¹³ is right (indeed η_2 − η_1 < ε_+ − ε_K).

**C2 / A1 — resolved.** The choice α_1 − α_0 < a♭_K − 2 is imposed (def:uc-choice cl. 353–354; lem:ec-counts as.
452–453) and used (as. 592: "the choice of α_0 in [[lem:ec-counts]] makes that level step one", hence the "+ 3" in
N_< + N_> + N_b + 3, which prop:uc-explicit evaluates). Existence (cl. 393–396): prop:iii-i8-4-1's proof (ch.
40:1131–1132) chooses admissible α_0 < α_1 < ⋯ < α_n = α with α_0 ∈ (2, min(a_K, 2 + ε_g, 5/2)) and steps below
a_K − 2, the exclusions being finite (ch. 40:726–729); at the level α_1 with a_K = a♭_K, (max(2, α_1 − (a♭_K − 2)), α_1)
is non-empty (α_1 > 2, a♭_K − 2 > 0) and lies in that range, as α_1 < a♭_K and α_1 < α − 2 ≤ 2 + ε_K < 2 + ε_g < 5/2.
In the general setting of lem:ec-counts the same holds (a♭_K ∈ (α_1, α − 2), ε_K < ε_g), so A1's "as that proof
allows" is true. *The writer's second addition (cl. 395–396), "that proof then has the single level step
α_0 → α_1": true* — with α_1 − α_0 < a♭_K − 2 the chain α_0 < α_1 (n = 1) meets every requirement of that proof, and
the clause, like A1's "so that it has the single level step", states that this chain is the one taken.

**C3 — resolved** (above).

**C4 — resolved** (cl. 337 "each follows by multiplying out"; cl. 475 "each by multiplying out").

**C5 — resolved** (cl. 126, 131, 151 as R-DB-2 gave them; the rewraps of cor:uc-two-offsets (a) and rem:uc-offset-d0
change no word, checked by a word diff).

**C6 — resolved; the writer's wording is acceptable.** cl. 488–489: "r_ιW(N_< + N_> + N_b + 3) < 16 · 1,470,302.27 ·
1.831147·10¹⁴ < 4.30775·10²¹, and so is the contribution of the window loops, each of at most 1,470,302 windows." It
bounds the term of eq:ec-upper's first line (r_ι ≤ 16, W < 1,470,302.27, the loop count < 1.831147·10¹⁴, all positive),
which is what R-DB-2 asked, and then the integer count, which is smaller. Exactly: 16 · 1,470,302.27 · 1.831147·10¹⁴ =
4,307,743,345,285,904·10⁶ < 4.30775·10²¹. It reads more plainly than the reviewer's "and so does the integer count".

**A2 — resolved, given CH-46.** prop:ec-delta-cap (as. 187–212) is in the loss-3 form with ω̃ := ω_(2d+3),
s̃ := min(s_(2d+3), s_P), the text R-DB-2 gave. Given R-DB-2's CH-46 (a)–(c), the proof is complete: at k = 2d, (d)
reads ‖P_5(Ψ(0))‖ ≤ C_(2d)ω_(2d+3)(‖(γ̃, k̃)‖_(H^(2d+3+k′_(2d+3)))) for that norm ≤ min(s_(2d+3), s_P), so C_(2d), ω̃ and
s̃ are exactly the constant, modulus and threshold with which (d) holds; max(C_(2d), 1) and max(ω̃(t), t) keep (d)
true, non-decreasing and tending to 0, which is all CH-46 (c) uses; ε ≤ s̃ gives ε ≤ ω̃(ε) ≤ ε_NM/C_(2d) ≤ 2^(−(32d+8));
and the domain [0, s̃] ⊂ [0, s_(2d+3)] of ω_(2d+3) is respected. As the files stand, chapter 46 does not define s_P and
its lem:iii-k-2-2 (d) and thm:iii-k-3-2 Smallness are still in the lossless ω_k form, so prop:ec-delta-cap and
chapter 46 disagree until CH-46 is placed (O1; not counted, as the integration round is pending).

**A3 — resolved** (as. 612–614, title and sentence as given; the sentence agrees with item (3), which ends with
prop:cs-cstar's bound).

**O2 (IS 499–500; R-DB-2's IS 497–498) — resolved.** "and ε_+ may be taken in (ε_K, μ_G), as [[eq:iii-i9-1-1]] and
(G⁺) of [[def:iii-j-g-plus]] ask." True: μ_G < 10⁻¹³ < min(δ_♯, δ_50), and (G⁺) ⟺ ε_+ < μ_G by the proof just given. It
agrees with thm:is-gap's statement ("every ε_K ∈ (0, μ_G) available for a suitable ε_+"); nothing else in IS changed,
and cor:is-flat is unaffected.

**R-DB-1 finding 10 (thm:uc-integer) — resolved.** cl. 529–531: "1 + n_ι ≤ c(β) ≤ 2N_ι + N̄_Λ + 529 = C_lev, with N_ι
of [[eq:uc-n-iota]], N̄_Λ = 16,747,199,999,999 and C_lev of [[eq:cs-clev]] ([[lem:cs-levels]])"; the proof (cl. 548) no
longer infers from N̄_Λ ≥ N_Λ. The bound is lem:cs-levels (b) as stated (β ∈ (3, α] is some β_k, k ≥ 1), and exactly
2N_ι + N̄_Λ + 529 = 214,558,790,360,052,785,818,485,009,600,000,520, the integer of eq:cs-clev.

## 2. No evaluated number moves (task 2)

All exact (check1.py, check2.py): Δβ_0 = 0.998001 · 1.6416·10⁻¹⁴ = 1.6383184416·10⁻¹⁴ and Δτ_0 = 1.4604381·10⁻¹⁰
exactly; ε′_0 = 1.085·10⁻²⁰; 1/Δβ_0 = 6.10381946884…·10¹³, 1/Δτ_0 = 6.8472604213…·10⁹, 1/(2Δβ_0Δτ_0) =
2.0897220734…·10²³, 1/𝔡₁ = 3,000,002.58333…, 0.4901/𝔡₁ = 1,470,301.26609…, all under the printed bounds; the two
"for instance" products and 3.333330462964850822194855·10⁻⁷ < 𝔡₁; ε_K/Δβ_0 = 1/0.998001; N_<, N_>, N_b < 6.10382·10¹³;
the three auxiliary inequalities before T_<, T_>; T_< = 2.08972207402…·10²³ and T_> = 2.08972207463…·10²³ from the
formulas of eq:ec-upper-counts, both < 2.089723·10²³ (and the printed chains hold); T_2 < 6.10382·10¹³ · 3.000005·10⁶ =
1.83114905…·10²⁰ < 1.83115·10²⁰; W = 1,470,302.26609… < 1,470,302.27; 4(1/Δτ_0 + 2) < 2.74·10¹⁰; the loop count
< 1.831147·10¹⁴; the window term < 4.30775·10²¹ (above); the first line < 1.2586909…·10²⁴ < D_e = 1.2587·10²⁴;
K + 2N_b + 2 < 2.44153·10¹⁴ = M_c; M_cC_* = 15,715,640,304·10⁴⁰; D_acc and 21D_acc + 6 are the printed integers,
< 1.57157·10⁵⁰ and < 3.30029·10⁵¹; at the choice 3ε_K + 2δ̂ + δ̄ = 1.9706…·10⁻⁸ < 1.98·10⁻⁸, ε_Kδ̂ = 2.400249024·10⁻²⁴
exactly, 3R > 1.24987·10²⁴ > 1.2498·10²⁴, 1.0072 · 1.2498 > 1.2587; at ε_K = 1.6417·10⁻¹⁴, R > 4.16598·10²³,
3R > 1.2497·10²⁴, 21 · 1.2497·10²⁴ > 2.624·10²⁵; J′ = 765,000,816, k̄_max, 62N̄_Λ, N_ι < 1.07280·10³⁵, C_lev; the
cstar iteration integers that use the counts (I_lev = 34,268,829,852 with 3,000,004 > (1 + η_2 − η_1)/𝔡₁ + 1, I_base);
c_* bound < C_*. The N_Λ bounds of prop:is-count hold at the new ε_+ (ε_+ + 𝔡₀ + 𝔡₁ < 1.69·10⁻⁶; upper value
1.6747170…·10¹³ < 1.67472·10¹³). ε_+ enters only through ε_+ < δ̄ (prop:is-lambda, prop:is-count), η_2 − η_1 < ε_+
(T_2), the α interval and smallness conditions on ε; prop:ec-rounds and lem:ec-counts (c) use only η_2 < ε_+ < δ̄ and
κ_3 > 1. No printed number changed.

## 3. The diff and the cstar keys (task 3)

The working-tree diff of the three files against 18a19178 is identical to scratch/f_db_a/f_db_a.diff (compared line by
line), the three files are committed as they stand, and every hunk is one of the fixes: close — C5 (cl. 124–131,
147–159), C4 (cl. 337, 475), C1 (a)–(i) with C2, C3 (cl. 343–396), C1 (j) (cl. 484), C6 (cl. 488–489), finding 10
(cl. 529–531, 548); assembly — A2 (as. 187–212), A1 (as. 452–453, 592), A3 (as. 612–615); IS — O2 (IS 499–500). No
other word changed.

P-U71-cstar.md is being edited by another writer (md5 9d174b443b3bfe2618d8024b7c82b4b4 at the start and at the end of
my reading; it has changed since 18a19178, so F-DB-a's "cstar unchanged since the baseline" no longer holds, without
consequence). All keys close cites from it exist there — eq:cs-clev, lem:cs-levels, lem:cs-fourier, prop:cs-cstar,
rem:cs-sharpness, def:cs-choices, and also sec:cs, lem:cs-base, lem:cs-rest, lem:cs-transforms — and say what close
uses: def:cs-choices (a) gives s_c = 3 > ½ + 9/4, ϑ_in = 0, ϑ_ℋ < 9/4 (rem:uc-missing, thm:uc-integer's choices);
lem:cs-levels (b) and eq:cs-clev give c(β_k) ≤ C_lev = 2N_ι + N̄_Λ + 529 = 214,558,…,520 for β_k > 3, with N̄_Λ :=
16,747,199,999,999 (cstar l. 18), as thm:uc-integer states; lem:cs-fourier (b) gives n_K ≤ N_ι + N_Λ (rem:uc-missing);
prop:cs-cstar gives c_* < C_* = 643,680,…,000 = 6.4368·10³⁵, the same integer (intro, thm:uc-integer); rem:cs-sharpness
ends with the k̄(λ) statement rem:uc-missing cites. cstar's intro now carries R-DB-1 finding 10's form ("C_lev =
2N_ι + N̄_Λ + 529, with the bound N̄_Λ ≥ N_Λ below"), and its uses of def:uc-choice and lem:uc-admissible (3 + ε_+ < ℓ_I,
ε ≤ 10⁻³ε_g < 10⁻¹², r_ι ≤ 16, the strip conditions, the bound 3.000005·10⁶) hold for the fixed texts. No mismatch.
(assembly's thm:fwd-loss "at most 20,180" agrees with P-U71-forward's statement as it stands.)

## 4. Contract (task 4)

`python3 lint.py` on the three files: 636 hits (baseline 616), every one "reference to undefined label"; the 181
distinct keys all resolve in chapters/ or proofs/; no style hit, no pending marker. Labels: 88 before and after; none
defined twice within the three files; prop:ec-rounds, thm:loss-d and prop:ec-delta-cap are also defined in chapter 71
(pending CH-71 (a); noted only). Longest line 121 characters in each file (code points; also 121 with combining marks
not counted); no wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|" — the only such lines are the list
items cl. 27–42 and the table rows as. 43–62 and IS 452–482. No process or program words in the added text
("computational point" is the defined term). The rewraps leave two short lines (as. 615, cl. 548), which break no rule.

## 5. Finding

**N1 (nit) — cl. 350, 382–383: def:uc-choice no longer states the range of α, which its proof assumes.** The baseline
read "α admissible with 0.999ε_K ≤ α − 4 ≤ ε_K"; the new clause reads "α admissible ([[def:iii-i10-1-3]]) and satisfying
(A_J) … and (Ex3)–(Ex4)", and def:iii-i10-1-3's admissible numbers include α ∈ (2, 3). The proof then argues for "an
admissible α ≥ 3". The range is implied by the context (the levels' spacing 0.999(α − 4) > 0, and sec:iii-j3-1, where
(A_J) and (Ex3)–(Ex4) are stated, takes α ∈ (4 + ε_K − ε′_0, 4 + ε_K]), so the mathematics is unaffected. *Fix.*
cl. 350: "α admissible ([[def:iii-i10-1-3]])" → "α ≥ 3 admissible ([[def:iii-i10-1-3]])".

## 6. Observations (not counted)

- O1 (for the integration round) — A2 makes prop:ec-delta-cap rely on s_P and the loss-3 form of lem:iii-k-2-2 (d),
  which exist only once R-DB-2's CH-46 (a)–(c) are placed (ch. 46:1247–1248, 1287–1290, 1464–1466 are still in the
  lossless ω_k form). Place CH-46 in the same round as the assembly text.
- O2 — chapter 71's sec:ec-integer still takes ε_+ = 189·10⁻¹⁰ (ch. 71:553–554), which violates (G⁺) for the index sets
  as constructed; R-DB-2's CH-71 (f) covers it.
- O3 — the δ_+ of sec:iii-i12-1 (δ_+ ∈ (0, ε_+ − ε_K), δ_+ ≤ η_E, η_2 ∈ (ε_+ − δ_+, ε_+)) is not named in def:uc-choice,
  before or after the fix; it exists for every choice made there (any δ_+ ∈ (ε_+ − η_2, ε_+ − ε_K), all below
  η_E = 𝔡₁) and enters no count.

**Verdicts.** P-U71-close: CONFIRMED (0 Major, 0 minor, 1 nit). P-U71-assembly: CONFIRMED (0, 0, 0). P-U71-IS:
CONFIRMED (0, 0, 0).
