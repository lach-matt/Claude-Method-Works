# F-DB-a: fixes to P-U71-close, P-U71-assembly, P-U71-IS

Baseline is the committed state at 18a19178 (md5 5716048…, 76949f9…, a455d37…). The periodic snapshot commits
(ea872549 … 5c8f45d3) picked up my edits while I was working, so the diff is taken against copies of the baseline:
scratch/f_db_a/f_db_a.diff (271 lines). Line numbers "cl."/"as." below are baseline lines.

## R-DB-2, P-U71-close

- **C1 (Major).** (a) cl. 343: ε_+ := 1.64160217·10⁻¹⁴, label moved to its own line. (b) cl. 345–351 replaced by the
  reviewer's text (ℓ_I ≤ a_I; [[def:iii-i13-1-1]] on ε; α admissible with (A_J), (Ex3)–(Ex4); base level α_0).
  (c) lem:uc-admissible statement as given. (d) cl. 363. (e) the paragraph "(G⁺) and the exactness conditions"
  inserted after (G). (f), (g) as given. (h) as given, plus one parenthesis saying why (A_J) excludes only finitely many
  α (finitely many λ₀ ∈ Λ with Re λ₀ < 3 + ε_+, finitely many −Re μ and Re π_1ℰ_K in (0, 3)). (i) the α_0 paragraph,
  plus a closing clause that α_1 − α_0 < a♭_K − 2 makes the level step single. (j) cl. 468 as given.
- **C2, C3.** Covered by C1 (b), (f), (i).
- **C4.** cl. 337 and 459 as given.
- **C5.** cl. 126, 131, 151 as given; cor:uc-two-offsets (a) and rem:uc-offset-d0 rewrapped (words otherwise unchanged).
- **C6.** Departure in wording only: "so r_ιW(N_< + N_> + N_b + 3) < 16 · 1,470,302.27 · 1.831147·10¹⁴ < 4.30775·10²¹,
  and so is the contribution of the window loops, each of at most 1,470,302 windows." This bounds the formula of
  eq:ec-upper's first line, as the reviewer asks, and reads more plainly than "and so does the integer count".

## R-DB-2, P-U71-assembly

- **A1.** Sentence on α_0 added to lem:ec-counts after "of h in Step 2)."; as. 590 parenthesis as given.
- **A2.** prop:ec-delta-cap restated in the loss-3 form (ω̃ := ω_(2d+3), s̃ := min(s_(2d+3), s_P)); proof and the
  paragraph after it changed as given. It now uses s_P, which exists only once CH-46 (a) is placed.
- **A3.** Title and first sentence of rem:ec-upper-open as given.

## O2, P-U71-IS

IS l. 497–498: "and ε_+ may be taken in (ε_K, μ_G), as [[eq:iii-i9-1-1]] and (G⁺) of [[def:iii-j-g-plus]] ask."
Nothing else changed. (The statement of thm:is-gap, "for a suitable ε_+", and cor:is-flat remain true.)

## R-DB-1 finding 10, P-U71-close

thm:uc-integer statement: "1 + n_ι ≤ c(β) ≤ 2N_ι + N̄_Λ + 529 = C_lev, with N_ι of [[eq:uc-n-iota]],
N̄_Λ = 16,747,199,999,999 and C_lev of [[eq:cs-clev]] ([[lem:cs-levels]])"; proof: ", with N̄_Λ ≥ N_Λ" deleted.
close repeats the bound nowhere else (rem:uc-missing's "n_K ≤ N_ι + N_Λ" is lem:cs-fourier (b) as stated).
Keys used from P-U71-cstar: eq:cs-clev, lem:cs-levels, lem:cs-fourier, prop:cs-cstar, rem:cs-sharpness,
def:cs-choices; all present in the cstar text as it stands (cstar unchanged since the baseline).

## Exact arithmetic (fractions and mpmath at 80 digits)

- μ_G = 1.6416021719712707…·10⁻¹⁴; ε_K < ε_+ < 1.64160217197·10⁻¹⁴ < μ_G; ε_+ − ε_K = 217·10⁻²² exactly,
  ε′_0 = 1.085·10⁻²⁰ exactly < 0.001ε_K; ε_+ < 10⁻¹³ < 0.0099 and < 1.9413·10⁻⁸.
- (Ex2): the real parts of ℰ^tot_I in (2.9, 3.1) (least ℰ^C_I and 3/2 + σ_Υ + ℕ₀) are 3 and numbers ≥ 3.0099.
- (1 + 10⁻¹³) · 3.0000026·10⁶ + 2 = 3,000,004.6000003 < 3.000005·10⁶ (true value (1 + ε_+)/𝔡₁ + 2 = 3,000,004.583…).
- 16 · 1,470,302.27 · 1.831147·10¹⁴ = 4,307,743,345,285,904·10⁶ < 4.30775·10²¹; W = 1,470,302.266… < 1,470,302.27.
- Rechecked unchanged: Δβ_0, Δτ_0 and their inverses, ε_K/Δβ_0, N bounds, T_<, T_>, T_2, D_e, M_c, J′, k̄_max, N_ι,
  C_lev = 214,558,790,360,052,785,818,485,009,600,000,520 (equal to eq:cs-clev), d_Φ, d_FM bound, D_acc, 21D_acc + 6,
  3R > 1.2498·10²⁴, 1.0072 · 1.2498 > 1.2587.

**No evaluated number moves.** ε_+ enters the counts only through ε_+ < δ̄ (prop:is-count, prop:is-lambda),
η_2 − η_1 < ε_+ (T_2), the α interval (now forcing 0.999ε_K ≤ α − 4) and upper bounds on ε; thm:uc-integer's integers
are unchanged.

## Lint and form

`lint.py` on the three files: 636 hits, every one a cross-file "undefined label" (baseline 616; the 20 new ones are the
added citations). Every key of the three files resolves in chapters/ or proofs/. No line over 121 characters; no wrapped
line starts with a listed prefix (only the list items cl. 27–42 and table rows). No label added; the only labels defined
twice are prop:ec-rounds, thm:loss-d and prop:ec-delta-cap, also in chapter 71, as before (CH-71 (a)). No pending
marker. Chapter texts of R-DB-2 §7 not applied.
