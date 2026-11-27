# P-U71-cstar report: the integer bound for c_*

**Outcome.** c_* < C_* = 643,680,000,000,000,000,000,000,000,000,000,000 = 6.4368·10³⁵ (prop:cs-cstar). I removed [[pending:issue-db-1]], and no pending marker remains.

## Integers (thm:uc-integer)
- d_acc ≤ D_acc = D_e + M_c C_* = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 < 1.57157·10⁵⁰
- d_NM = d_R ≤ D_NM := D_acc
- N_NM ≤ 21D_NM + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006 < 3.30029·10⁵¹
- The lower bounds (3R > 1.2497·10²⁴) are unchanged.

## How the bound is built
- **Rule.** Each single-step loss is at most the sum of the charges of its applications (lem:cs-sum (a)).
- **Parameters.** These enter by finite-rank assemblies, as in the proof of prop:ec-upper. An elimination therefore counts each statement once, plus 11 (lem:cs-sum (b)).
- **Free choices (def:cs-choices).**
  - ϑ_in = 0, from lem:ec-theta-in-zero.
  - ϑ_ℋ < 9/4: δ = ¼ in lem:iii-f2-1-1, with ℬ_* inside its neighbourhood.
  - s_c = 3, 𝗋_in = −¼, 𝖻 ≡ 0, and N = 5 in lem:iii-i2-4-1.
  - The increments η ∈ [2/5, ½) in prop:iii-i1-2-1.

## Steps and bounds (cstar file line numbers)
- **Elementary charges** (lem:cs-elem, l. 76):
  - 0 for the FIN and INT families, the Mellin inversions and the tails.
  - 1 for prop:ii-g1-3-3 (1), L̃_b(0)⁻¹ and ℓ_tf.
  - 2 for L_b and L̂_b; 11 for the BG families (prop:uc-dbg).
  - FWD 20,183: thm:fwd-loss plus 3 for h_rem(q).
  - prop:iii-g4-4-4 ≤ 3; prop:iii-g4-5-1 ≤ 9, counted from its proof; thm:iii-g4-3-1 ≤ 1.
  - lem:iii-a-1-4 ≤ 8, so lem:iii-i11-2-1 ≤ 9; prop:iii-g3-3-7 = 30.
- **Transforms** (lem:cs-transforms, l. 155):
  - prop:ii-g1-3-3 (2) ≤ 3; ℓ_F ≤ 5; prop:ii-g1-3-5 (2) ≤ 5 or 6.
  - cor:ii-g1-4-2, prop:ii-g1-4-7 and lem:iii-i2-4-2: 2.
  - cor:ii-g1-4-5 ≤ 20, with ℓ_3 = 6, ℓ_4 = 4 (ν = 1), ℓ_5 ≤ 3; lem:iii-i2-4-1 ≤ 30; lem:iii-i2-3-1 ≤ 2.
- **Null infinity** (lem:cs-null, l. 208):
  - prop:iii-i1-3-1 ≤ 6: two windows, and ℰ^C_I has no logarithms.
  - prop:iii-i1-2-1 ≤ 37·11 = 407: at most 37 steps, each applying L̃ once.
- **Fourier steps** (lem:cs-fourier, l. 233):
  - Step 0: ≤ 9 + N_ι.
  - Step 7 (item 4 of the brief): n_ι = 0, because every tf-exponent of the pieces has real part ≥ 1.
  - Step 7: n_K ≤ N_ι + N_Λ. The zf-degrees below 1 + ε_K are λ − 2 with λ ∈ Λ ∩ [2, 3 + ε_K), and their logarithmic orders are ≤ k̄(λ) + 1. This uses (G), {−μ} ≥ ε_ind and the realness of Λ.
- **Level steps** (lem:cs-levels, l. 289):
  - c(β) ≤ 497 for β < 3.
  - c(β) ≤ C_lev = 2N_ι + N̄_Λ + 529 for β > 3.
  - Both bounds include the background terms of Step 2 (11), E^ν at a rotating b, and e_S, e_S⁰ for ℛ(U).
- **Base** (lem:cs-base, l. 337): c′_b ≤ 466 and c_b ≤ 469.
- **Iterations charged in full** (lem:cs-iterations, l. 361): I_lev = 34,268,829,852 and I_base = 1,435,970,471,299,470,574,962.
- **c_0** (lem:cs-rest, l. 389). The bound eq:cs-c0 adds up:
  - Step 0: 20,183. Base remainder: 1,914.
  - Steps 3/4′/4 charged as one full thm:iii-i11-4-1 run plus two full thm:iii-i12-3-1 runs, i.e. three level-step runs at α. The extras include (vi) with n_ι ≤ 4(k̄_max + 1).
  - d_Φ.
  - Steps 1–3 of thm:iii-j1-2-1: ≤ (N̄_Λ + 2)(d_Φ + 30) < 1.739·10²⁸. The chain passes every exponent of Λ_*.
- **Total** (prop:cs-cstar, l. 460): c_* ≤ 6N_ι + 3N̄_Λ + 17,389,163,815,025,371,354,557,103,786 = 643,676,388,469,322,172,480,826,383,357,103,759.
- **Sharper variant** (rem:cs-sharpness): charge the level steps with C_lev and add c_0 once. This gives d_acc < 2.62·10⁴⁹.

## Readings to confirm
1. **Finite-rank reading.** Parameters enter as finite-rank assemblies, charged by the largest part. Without this reading the base would be traversed several times along a chain, and prop:ec-upper's coefficients N_b and N_b + 1 would be too small.
2. **c_0 overcounts on purpose.** It counts thm:iii-i11-4-1 (base and level step) and thm:iii-i12-3-1 twice in full. A single-run reading would give about 2N_ι + 1.7·10²⁸.
3. **lem:iii-a-1-4.** Neither lem:iii-j2-2-1 nor rem:ec-other-losses lists it. I charged it 2 per step.

## Statements that must change (I did not edit these)
- **P-U71-close.md l. 15–18.** Replace "d_acc and d_NM are at most 1.2587·10²⁴ plus 2.44153·10¹⁴ times the largest loss c_* of a single step outside the long iterations, against the lower bound 1.2497·10²⁴; [[rem:uc-missing]] states what separates this from an integer." with: "d_acc and d_NM are at most an integer D_acc < 1.57157·10⁵⁰, the largest single-step loss being below 6.4368·10³⁵ ([[prop:cs-cstar]]), against the lower bound 1.2497·10²⁴; [[rem:uc-missing]] states what the bound rests on."
- **Assembly l. 156–158.** Replace "d_acc and d_NM are at most 1.2587 × 10²⁴ plus 2.44153 × 10¹⁴ times the largest single-step loss c_*, which [[rem:uc-missing]] describes." with: "d_acc and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹."
- **Assembly l. 609–610.** Replace "[[thm:uc-integer]] bounds them through their largest value c_*." with: "[[prop:cs-cstar]] bounds their largest value c_* by 6.4368·10³⁵."
- **Assembly l. 627–628.** Replace "[[rem:uc-missing]] says what its value needs." with: "[[prop:cs-cstar]] bounds it by 6.4368·10³⁵."
- **Ch. 71 l. 20–22** (W-DB's text). Use: "[[thm:uc-integer]] bounds d_acc and d_NM by an integer below 1.57157 × 10⁵⁰ and N_NM by one below 3.30029 × 10⁵¹, counting the logarithmic terms of the index sets at the bound k̄(λ)."
- **Ch. 71 rem:ec-other-losses l. 385–387.** Use: "[[lem:uc-lambda]], [[lem:uc-dr]] and [[sec:cs]] give them; [[thm:uc-integer]] states the resulting bound."

## Lint and size
- `lint.py proofs/P-U71-cstar.md proofs/P-U71-close.md`: only cross-file undefined references remain.
- All 132 references resolve across chapters/ and proofs/. The 23 new cs- labels are unique.
- No line exceeds 121 characters, and no wrapped line has a forbidden start.
- Line counts: P-U71-cstar.md 489 (new), P-U71-close.md 559.
