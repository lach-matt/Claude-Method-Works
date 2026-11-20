# P-U71-small: the smallness orders, d_*, and the d of thm:iii-k-3-2

Tree read at HEAD ed41ea95. Nothing in the repository was edited. One file was written:
`research/warp-drive/paper/reader/proofs/P-U71-small.md` (409 lines). It holds the new subsection for chapter 71 and the
replacement texts.

## Outcome

- **The printed numbers stand, the integers included.** The d with which thm:iii-k-3-2 applies thm:ii-g-2-1 is
  d_NM := max(d_R, d_* + d_F + d_Φ). It satisfies d_acc ≤ d_R ≤ d_NM < D_acc, so the statements below stay true as
  written:
  - d_NM ≤ D_NM := D_acc < 1.57157·10⁵⁰;
  - N_NM = 21d_NM + 6 ≤ 21D_acc + 6 < 3.30029·10⁵¹.
- **Only the definition of d_NM changes.** It was "the largest of the losses" and becomes "the largest of the d's of the
  three results", each d at least its loss and its smallness orders. The sentences that called d_NM = d_R or
  d_NM = max(d_R, d_FM, d_Ψ) change with it: 13 replacement texts, all in chapter 71.
- **No other chapter changes.** Chapters 00, 01, 03, 46 and 90 need no edit: each states its bound for the loss d with
  which the settling proof applies Nash–Moser, and that loss is the new d_NM.
- **The lower bounds stand.** They need only d ≥ d_acc, and d_NM ≥ d_R ≥ d_acc. So 1.403·10²⁰, 2.946·10²¹, 1.2497·10²⁴,
  2.624·10²⁵ and log₁₀ δ < −1.351·10²¹ all hold for the new d_NM.

| | Fine reading of the fixed seminorms | Cumulative reading (rem:uc-small-reading) |
|---|---|---|
| d_* ≤ | D_* = 214,558,790,360,104,032,305,147,901,608,827,158 < 2.14559·10³⁵ | D′_* < 2.6193·10⁴⁹ |
| d_NM ≤ | 26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644 < 2.6193·10⁴⁹ | 52,385,…,831,693 < 5.2386·10⁴⁹ |
| N_NM ≤ | 550,043,…,351,530 < 5.5005·10⁵⁰ | < 1.10009·10⁵¹ |

- **Fine reading:** each fixed seminorm is taken at the regularity at which the maps that read coefficients from the
  forcing are bounded. This is how the proof of lem:iii-j2-2-3 itself uses them.
- **Cumulative reading:** each fixed seminorm must also bound the remainder maps, as the text of sec:iii-i8-1 can be
  read. The regularities then grow level by level.
- **Both readings give d_NM < D_acc.** D_acc exceeds the cumulative bound by 1.0477·10⁵⁰.

The new results:

- **lem:cs-sharp.** This proves the figure of rem:cs-sharpness as a lemma: d_acc, d_R ≤ D_♭ < 2.6193·10⁴⁹.
- **lem:uc-small-orders.** The orders of every smallness condition, and d_* ≤ D_*.
- **rem:uc-small-reading.** The cumulative reading, with d_* ≤ D′_*.
- **prop:uc-d-small.** The d of thm:iii-k-3-2, with bounds (a)–(d).

All four sit in a new subsection sec:cs-small, at the end of sec:cs, after rem:cs-sharpness and before
sec:ec-linear (71:4321).

Without lem:cs-sharp only the decimals would stand. Under the fine reading, d_* + d_Φ ≈ 2.1·10³⁵ is far below the
margin 1.57157·10⁵⁰ − D_acc = 596,959,999,999,999,999,998,741,300,000,000,000,000,000,000 ≈ 5.97·10⁴⁴. But
D_NM = D_acc would fail, and the cumulative reading would fail outright. With lem:cs-sharp everything stands under both
readings.

## The value of every order

The order of a condition is j when it holds for ‖β‖_j small and ‖β‖_(j+D) bounded, D the d of thm:iii-j2-4-1. The
bounded part is lem:iii-j2-2-3's "u_j bounded at a fixed order"; d_0 = d_* + D covers it. Background terms are
handled by a difference form of prop:uc-dbg (F1, eq:uc-small-diff):

    ‖(A_β − A_β′)u‖_k ≤ C_k‖β − β′‖_(k+11)‖u‖_(k+2),   C_k depending on bounds for ‖β‖_(k+14), ‖β′‖_(k+14).

So a condition asked in a seminorm of regularity ρ has order ρ + 14.

| Condition (as named in the proof of lem:iii-j2-2-3) | Order |
|---|---|
| thm:iii-i-5-3 / cor:iii-h2-5-1, at h, h + h^(−1)(S), h + h_tot(p⃗) | d_T = 20,180 |
| the same at h + h_rem(q) + h_tot(p⃗) | d_T + 3 = 20,183 |
| lem:iii-i4-4-2: k_1 (Π_b: prop:iii-i1-3-1 6, L_b 2, prop:ii-g1-3-3 (1) 1, L̃_b(0)⁻¹ 1) | k_1 = 10 |
| lem:iii-i4-4-2 (a): k_0 = k_1 + 2 + L_u, with L_u ≤ 20,183 + 407 + 466R_b | k̄_0 = 28,443,801,200,020,602 |
| eq:s20-d: d ≥ max(d_T, k_0 + 2, k_1 + d_T + 7) = max(20,180, k̄_0 + 2, 20,197) | k̄_0 + 2 = 28,443,801,200,020,604 |
| the same at the q-backgrounds | k̄_0 + 5 = 28,443,801,200,020,607 |
| ch:s21 "h small in 𝒳^d" and the base, at b included (prop:iii-i15-2-8, prop:iii-i15-2-12, lem:iii-i8-3-3, prop:iii-i8-4-1, T_(h,p⃗)) | ≤ 2R_base + 16 = 2,871,940,942,598,941,194,134 |
| ch:s23 "q small" (h + h_rem(q) small in that 𝒳^d) | ≤ 2R_base + 16 (+3 already included) |
| lem:iii-i9-2-6 continuity (k ≥ 5) | 5 |
| lem:iii-i9-2-6 bounds in the forcing seminorm | ρ + 11 |
| lem:iii-i14-2-3/4 (R_q, Δ_q ≤ C‖q‖) | ρ + 11 (q at the same order in ‖β‖) |
| level reads (lem:iii-i8-3-2, lem:iii-i11-3-2, lem:iii-i13-2-2, A_b): fixed seminorm | ρ ≤ C_lev − 11 + I_lev = 214,558,790,360,052,785,818,485,043,868,830,361 |
| S^(0,0)_ν seminorm m, and d′ of lem:iii-j2-2-1 (b) at that order | m = ρ, d′ = m + 11 |
| A_k → 0 (Step 3), at b₀ | ≤ ρ + 14 |
| A_k at a reference (0, p⃗_b), b ≠ b₀ (lem:iii-i15-2-4, lem:iii-i13-2-3; extra term through prop:iii-i8-4-1 (i)) | ≤ ρ + R_base + 16 = 214,558,790,360,054,221,788,956,343,339,427,436 |
| Step 4′ (C^rot read through thm:iii-i12-3-1 at (0, 0); p⃗′_0 through thm:iii-i11-4-1) | ρ ≤ max(C_lev − 11 + I_lev + X_12, T_11) < T_12; order ≤ T_12 + 14 |
| **d_*** | **≤ D_* = T_12 + 14** |
| lem:iii-k-2-3: d_BG, m + 5 | 11; m + 5 ≤ d_* − 9 |
| lem:iii-k-2-3: d′_0 | max(d_* + d_F + d_Φ, d_R) |
| lem:iii-k-2-2, prop:iii-j2-4-3 (H³ smallness of w, lem:iii-j2-2-4 with d_1 = 3, cor:iii-i-4-2 at order 3; their 3d-smallness is covered by the domain \|U\|_(3d) < δ) | d_Φ + 8 ≤ 1,038,326,399,999,948 |
| **d_NM** | **max(d_R, d_* + d_F + d_Φ)** |

Constants used in the table:

- R_base := 20,183 + 1,914 + I_base = 1,435,970,471,299,470,597,059. It bounds every chain of a base.
- d_F ≤ d_R is the accounted loss of thm:iii-j2-4-1 at Ψ(U).

## Numbers recomputed, in exact integers

Chapter 71's own numbers, all confirmed:

- N_ι = 4N̄_Λ + 765,000,816·N̄_Λ(N̄_Λ + 1)/2 = 107,279,395,180,026,392,909,234,131,199,999,996.
- C_lev = 2N_ι + N̄_Λ + 529 = 214,558,790,360,052,785,818,485,009,600,000,520.
- k̄_max = 12,811,621,665,714,434,999,187.
- I_lev = 34,268,829,852.
- I_base = 1,435,970,471,299,470,574,962.
- The bound of eq:cs-cstar, 643,676,388,469,322,172,480,826,383,357,103,759:
  - its seven summands add to 17,389,163,815,025,371,354,557,103,786;
  - 6N_ι + 3N̄_Λ + that sum equals the bound.
- D_acc = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000.
- 21D_acc + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006.
- d_Φ ≤ 62·16,747,199,999,999 + 2 = 1,038,326,399,999,940.

New numbers:

- X_12 = 4k̄_max + 24 = 51,246,486,662,857,739,996,772.
- T_11 = 214,558,790,360,054,221,788,956,343,339,427,453.
- T_12 = C_lev + I_lev + X_12 = 214,558,790,360,104,032,305,147,901,608,827,144, so T_11 < T_12.
- K ≤ K̄ = 122,076,389,376,829, from KΔβ_0 ≤ α − α_1 < 2 + ε_K:
  - 16,383,184,416 · 122,076,389,376,829 = 2,000,000,000,000,012,824,296,864;
  - 16,383,184,416 · 122,076,389,376,830 = 2,000,000,000,000,029,207,481,280;
  - the numerator (2·10¹⁸ + 16,416)·10⁶ = 2,000,000,000,000,016,416,000,000 lies between them.
- N_b < 61,038,194,688,416 < R_b, as 16,383,184,416 · 61,038,194,688,415 > 10²⁴.
- K̄C_lev = 26,192,562,436,215,228,354,699,390,649,792,285,562,280,875,951,080.
- 469R_b + 466(R_b + 1) = 28,626,915,800,000,000 + 28,443,801,200,000,466 = 57,070,717,000,000,466.
- D_♭ = D_e + K̄C_lev + 469R_b + 466(R_b + 1) + C_* = 26,192,562,436,215,872,034,699,391,908,492,342,632,997,875,951,546
  < 2.6193·10⁴⁹.
- k̄_0 = 20,602 + 466R_b = 28,443,801,200,020,602.
- 2R_base + 16 = 2,871,940,942,598,941,194,134.
- D_* = T_12 + 14 = 214,558,790,360,104,032,305,147,901,608,827,158.
- D′_* = T_12 + 18 + K̄(C_lev + I_lev − 9) + 2R_base = 26,192,562,436,215,442,913,489,754,940,111,547,055,147,233,880,207, with:
  - K̄(C_lev + I_lev − 9) = 26,192,562,436,215,228,354,699,394,833,207,300,964,646,683,858,927;
  - 2R_base = 2,871,940,942,598,941,194,118.
- Fine reading:
  - D_♭ + D_* = 26,192,562,436,216,086,593,489,752,012,524,647,780,899,484,778,704;
  - adding d̄_Φ gives 26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644;
  - 21·that + 6 = 550,043,811,160,537,818,463,284,792,263,017,625,203,743,580,351,530.
- Cumulative reading:
  - D_♭ + D′_* = 52,385,124,872,431,314,948,189,146,848,603,889,688,145,109,831,753;
  - adding d̄_Φ gives 52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693;
  - 21·that + 6 = 1,100,087,622,321,057,613,911,972,083,820,681,705,255,901,706,465,559.
- D_acc − (cumulative bound) = 104,771,278,167,568,685,051,810,854,410,096,109,273,528,490,168,307 > 0.
- Iterations at a level below 3: 16·1,470,302 + 3·6,847,261,002 = 20,565,307,838 < I_lev. Also
  1/Δτ_0 = 10¹⁷/14,604,381 ≈ 6,847,260,421.4.

**rem:cs-sharpness checked.** Every figure in it holds:

- C_* − 6N_ι = 3,628,919,841,642,544,595,212,800,000,024 < 3.63·10³⁰;
- c̄_0 − 6N_ι = 17,389,163,815,025,421,596,157,103,783 < 1.74·10²⁸;
- (N̄_Λ + 2)(d_Φ + 30) = 17,389,059,886,080,535,910,399,999,970 < 1.739·10²⁸;
- K < 1.22077·10¹⁴;
- d_acc < 2.62·10⁴⁹, which lem:cs-sharp now proves for d_R as well.

## Replacement texts (line numbers of chapter 71 at ed41ea95)

Every text is printed exactly in the proof file.

1. 71:162–166, the sec:ec-accounted paragraph: d_NM is the largest of the d's, which contain d_* + D + d_Φ.
2. 71:1431–1434, the statement of thm:loss-d: new definition of d_NM.
3. 71:1460–1461: adds that prop:uc-d-small evaluates the smallness orders.
4. 71:1465–1467, the proof of thm:loss-d: "d_NM … is at least the loss of ℛ(U)".
5. 71:1493, prop:ec-delta-cap: "(d ≥ d_R ≥ d_acc, …, prop:uc-d-small)". Its proof is unchanged.
6. 71:1938–1940, rem:ec-upper-open (4): replaces "so that d_NM equals it".
7. 71:1953 and 71:1960–1961, the opening of sec:uc-close.
8. lem:uc-phi-loss: the title at 71:2222, the statement at 71:2231 ("d_NM ≥ max(…)"), and the proof at 71:2243–2245.
9. 71:2255, thm:uc-reduction (ii): "=" becomes "≥".
10. lem:uc-dr: 71:2444 and 71:2457.
11. thm:uc-integer:
    - 71:2466, eq:uc-integer: d_acc ≤ d_R ≤ D_acc and d_NM ≤ D_NM := D_acc;
    - 71:2473: the finer bounds;
    - 71:2489–2491: the proof.
12. 71:4317–4319, rem:cs-sharpness: cites lem:cs-sharp.
13. 71:22–23, the chapter opening.

Checks run on a scratch copy of chapter 71 with all 13 replacements and the insertion applied, using the edition's
own checker and numbering routine in memory:

- 0 lint hits on the modified chapter 71 and on the proof file;
- every reference resolves (the new labels become Lemma 49.107, 49.108, Remark 49.109 and Proposition 49.110);
- every line is at most 121 characters, both in the source and after labels are resolved;
- no wrapped line starts with a forbidden marker;
- proofs and ∎ are balanced.

On the unmodified tree: `lint.py --chapters` gives 0 hits, and `assemble.py --check` gives "problems 0".

## What is not closed, and what to check

1. **Implicit orders.** The fixed seminorms of ch:s21–s25 have no stated order. I took them at the regularity of the
   reading maps, which is what the proof of lem:iii-j2-2-3 itself uses ("R_j → 0 only in that seminorm … u_j bounded
   at a fixed order"). The upper bound for d_NM is given under that reading and also under the larger cumulative one,
   and the printed bounds hold under both. The fine bound d_NM < 2.6193·10⁴⁹ rests on the first reading.
2. **The order convention.** Boundedness at j + D is part of the order. This makes explicit lem:iii-j2-2-3's
   requirement "u_j bounded at a fixed order"; d_0 = d_* + D covers it.
3. **(F1) is a new short argument.** The difference bound comes from the proof of prop:uc-dbg by the mean value theorem
   with lem:ii-g-4-1 (2)–(3). It deserves a reader's check. The difference form actually needs only order k + 8; I state
   k + 11 to match d_BG.
4. **Possible problem outside this task: chapter 40, prop:iii-i8-4-1 (i), proof at α″.** It bounds ‖u(0)‖_(α′) by
   ‖F‖ := ‖F‖_(𝒴(α″)), taking both in the fixed seminorms of sec:iii-i8-1. At one finite regularity this cannot hold,
   because the required regularities form a cycle:
   - ‖·‖_(α′) must control (L − L_b)u in ‖·‖_(𝒴(α″)), so it is two orders above it;
   - bounding u at α′ costs at least the forward loss;
   - the argument also needs ‖F‖_(𝒴(α′)) ≤ C‖F‖_(𝒴(α″)).

   The argument works when ‖F‖ in (i) is a seminorm of larger regularity, as prop:iii-i15-2-5 states its own
   induction bound ("‖F‖ … of large enough regularity"). The smallness conclusions and the orders above are
   unaffected. It may want a one-sentence clarification in chapter 40; I did not edit it.
5. **The headline could be sharpened, if the author wishes.** For example, d < 5.24·10⁴⁹ under both readings, or
   < 2.62·10⁴⁹ under the fine one. That is optional: the printed 1.57157·10⁵⁰ and 3.30029·10⁵¹ are proved as they stand.
