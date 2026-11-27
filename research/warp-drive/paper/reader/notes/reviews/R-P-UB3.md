# R-P-UB3: independent reading of proofs/P-UB3.md

File read: research/warp-drive/paper/reader/proofs/P-UB3.md, md5 00c0b5a11bc2db904135d473bc60b6fb, 2019 lines plus a
final newline (the "2020 lines" of the report), every line. Writer's report: notes/reports/P-UB3.md. Base: HEAD fab88210
(chapters 71, 00, 01, 03, 90 byte-identical to 1680675a, chapter 71 md5 bb53f3e8…) with P-D0 (md5 1265f3bd…) T1–T16.
Nothing in the repository was edited or committed. I did not read method/, drive/, extracted/ or recovered/.

Scratch: scratchpad/rpub3/ (tree/ = git archive of HEAD + P-D0 + the 60 texts; pd0tree/ = HEAD + P-D0; headtree/ = HEAD;
nittree/ = tree + the two optional nits below; tools/merge.py my own parser and applier). Arithmetic: my own script
scratchpad/reader/tools/ub3chain.py (exact rationals) and checks_new.py (93 asserted comparisons). The writer's scripts
were not used. Afterwards I compared only the merged chapter: my chapter 71 has md5 ca38b230ec43bccfb7e72a60bde5a62f, the
same as the writer's scratch copy.

## 1. Placement

- P-D0's 16 old texts each occur once, as whole lines, at HEAD; applied, chapter 71 has md5 1b1056fa…, as the file says.
- All 60 old texts of P-UB3 occur exactly once, as whole lines, in their chapters with P-D0 applied. They are pairwise
  disjoint. Every stated line number is right, "with P-D0" and "HEAD" alike. U11–U15 do not occur at HEAD (they replace
  P-D0's new texts of T6–T9 and T12). U42 leaves T16's lines alone.
- Every "Old (n lines)" and "New (n lines)" count is right.
- Checks on tree/:
  - `lint.py --chapters`: 62 files, 5088 labels, 0 hits.
  - `assemble.py --check`: 5088 labels, 0 problems.
  - The required one-liner prints `[] 0`.
  - No assembled line is longer than 121 characters (0, as in pd0tree/).
  - No new line is longer than 121 characters, has trailing space, starts with a Markdown marker or with "n. ", or
    contains a backtick. A word list (now, was, former, found, version, computed, program, record, …) finds nothing in
    the new texts.
- Crosswalk:
  - Every label whose text changes has exactly one existing row; eq:uc-integer sits inside U19 but is unchanged.
  - The 46 rows of §6 have four fields each, and every "@PENDING:N" points at the first line of its new text.
  - 00-front has no labels, as stated.

## 2. Part 1

### (a) The hypothesis 4k̄_max + 24 > I_base + 22,119: removed by proof, confirmed

- **It is T_11 < T_12.** With T_11 = 20,183 + 1,914 + I_base + 22 + C_lev + I_lev = C_lev + I_lev + R_base + 22 (as in
  lem:cs-rest) and T_12 = C_lev + I_lev + X_12, T_12 − T_11 = 4k̄_max + 24 − I_base − 22,119.
- **Uses.** I grepped all 62 chapters (with P-D0 applied) for T_11, T_12, X_12, 22,119, 22,083, 3,060,003,264, 4k̄_max
  and N₁. Each hit was read. The comparison of T_11 with T_12 occurs only in:
  - lem:uc-small-orders (d), the Step 4′ reads "both less than T_12";
  - (e), "X_12 … exceeds R_base + 22, so that also T_11 < T_12";
  - rem:uc-small-reading, "at an order below T_12 + 2";
  - prop:uc-dependence;
  - and, as consequences, P-D0's lem:uc-lambda (a) and the N₁ of thm:tr-transfer (iii) and its proof.

  lem:cs-rest, prop:cs-cstar and prop:uc-d-small (d) only add T_11 and T_12, or compare them at the choice.
- **The weakened proofs.**
  - In (d) the reads are charged at most T_12 − 11 and T_11 − 11 ≤ T_11. So ρ ≤ max(T_11, T_12) whatever the sign.
  - A reference-point condition has order at most C_lev + I_lev + R_base + 5 = T_11 − 17.
  - (a)–(c) give 2R_base + 16. In general this need not be below T_12 + 14; U20 rightly keeps it inside
    max(2R_base + 16, max(T_11, T_12) + 14).
  - rem:uc-small-reading with max(T_11, T_12) + 2 for the Step 4′ read gives exactly
    D′_* = max(T_11, T_12) + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base. That is at least
    2R_base + 18 and max + 14, so it bounds both readings.
  - The monotonicity statements survive, as the larger of two non-decreasing polynomials is non-decreasing.
  - At the choice X_12 = 11,270,575,291,594,154,340 > R_base + 22 = 161,579,883,606,189,032, so lem:uc-small-orders and
    rem:uc-small-reading rightly keep T_12.
- **sec:tr.** With N₁ gone, N̄_Λ := N̄(h) is an integer (a floor) with N_Λ ≤ N̄(h) (prop:tr-lambda (c)). At h, ε_K can
  be arbitrarily small (μ(h) → 0 at h_μ), so T_11 > T_12 can occur there. The max form is therefore what makes the
  removal of N₁ correct.

### (b) ε_+ < 10⁻¹³ replaced by ε_K < 0.998ε_Υ: confirmed

- **Explicit uses** of the old cap, in sec:uc-eval–sec:cs-small:
  - (1 + η_2 − η_1)/𝔡₁ + 2 < 3.000005·10⁶ in prop:uc-explicit;
  - through it, 3,000,004 in lem:cs-iterations and so I_lev, which lem:uc-small-orders (d) and rem:uc-small-reading
    reuse.

  Under admissibility ε_+ < ε_ind ≤ δ_50 < δ̄ < 10⁻⁷, and (1 + 10⁻⁷) · 3,000,002.6 + 2 = 3,000,004.90000026 < 3,000,005.
  prop:tr-lambda's own "ε_+ < 10⁻¹³" is a hypothesis of a sec:tr result, met there since ε_+ < μ(h) ≤ μ_G < 1.65·10⁻¹⁴.
- **Tacit smallness of ε_K.** I listed every occurrence of ε_K, ε_+, ε_g, τ_0 and ε in chapter 71 and of ε_K in chapters
  31, 35, 38–44, 46 and 48. The conditions that bind near ε_K = 1.4589·10⁻¹⁰ are these.
  - def:iii-i10-1-3, ε_K < ε_Υ: margin 3.0·10⁻¹³. (G) also gives d_c0, d_c1 > ε_K, which holds.
  - (G), (G⁺) for Λ^φ: ε_K < ε_+ = 1.459·10⁻¹⁰ < μ♭_Z ∈ (3.548125563, 3.548125564)·10⁻¹⁰ (cor:is-flat). cor:is-flat's
    proof needs ε_+ ≤ 10⁻⁸ ("real part at most 3 + 10⁻⁸"), which holds.
  - Ch. 41 Step 4, δ + ℓ_3 + 2ε < ε_g with ℓ_3 + 2ε = α − 4 + ε ≤ ε_K + ε. This needs ε_K + ε < ε_g:
    1.4589·10⁻¹⁰ + 1.4619·10⁻¹³ < 1.4619·10⁻¹⁰.
  - Bases (lem:cs-rest (6), sec:cs-small): α_1 − 2 < ε_K < ε_g − 2ε. With ε_g = ε_Υ and ε ≤ 10⁻³ε_g,
    ε_g − 2ε ≥ 1.4589762·10⁻¹⁰ > ε_K, a margin of 7.6·10⁻¹⁵. def:cs-choices (f) and the α′ of lem:iii-i11-3-3 and
    lem:iii-i13-2-3 lie in (2, 2 + ε_g − 2ε) by choice.
  - η_1 < ε_g with η_1 ∈ (ε_K, ε_+), and ε_+ < ε_g: holds. α_0 < 2 + ε_g: α_1 < 2 + ε_K < 2 + ε_g.
  - ε′_0 = ½(ε_+ − ε_K) = 5·10⁻¹⁵ < 0.001ε_K, so 0.999ε_K ≤ α − 4 ≤ ε_K. Ch. 41's 2ε < ε_+ − η_2 < 10⁻¹⁴ is only a
    further smallness of ε, allowed by "besides".
  - The rest hold for any ε_K below ½ or δ_♯, or follow from admissibility:
    - ε_K < δ_♯ + ½ (41:456) and ε_K < δ_♯ (35:1417);
    - ⌈3/2 + ε_K⌉ = 2, ⌈α + ε − ½⌉ = 4 and −μ ≥ ε_ind > ε_K in lem:cs-fourier, and reality of Λ up to 2 + ε_K;
    - 4 + ε_K < 5;
    - 43:104 (5ε_1 < ε_+ − η^0_2), 46:1807 (w1);
    - prop:ec-rounds and lem:ec-lb-rounds (ε_K < δ̂);
    - (1 + cx)²/x decreasing for x < 1/c ≈ 0.667.
- **Is ε_Υ the real limit?** def:iii-i10-1-3 and Step 4 of prop:iii-i11-3-1 need ε_K < ε_g ≤ ε_Υ. The claim is in the
  proof file only; no chapter text states it.

### U20's proof

- I read it sentence by sentence.
- The index-set facts it names hold for both families:
  - the least ℰ^C_I is built from σ_Υ alone (prop:is-ci-pp (a));
  - min Re = 𝔡₁ (lem:uc-gaps after P-D0);
  - Λ^φ ⊂ Λ (thm:is-flat-serves).
- The other uses of the cited proofs are admissibility, (G) and (G⁺), the counts N_Λ ≤ N̄_Λ and k̄(λ_i) ≤ k̄_0 + J′i,
  and the facts (1)–(3).
- C_* equals the right side of eq:cs-c0 exactly. I checked this as integers at the new choice.
- sec:tr-proof (iii) meets the new hypotheses at h:
  - ε_K < μ(h) ≤ μ_G < 0.998ε_Υ (U44);
  - (1) holds because ε_+ < μ_G;
  - (2) holds because ε_g = ε_Υ there.

## 3. The arithmetic, recomputed independently

**At HEAD's inputs** (ε_K = 1.6747·10⁻¹⁷, ε_+ = 1.67478·10⁻¹⁷, N̄_Λ = 909,507,124,095,312, D_e = 1.23382·10²⁷, T_12 form),
with F_1 = 1.2338126…·10²⁷ ≤ D_e, every printed integer of HEAD reproduces exactly:

- L_<, L_>, R_b, N_ι, k̄_max (from 2X_12), d̄_Φ, C_lev, I_base, R_base, X_12, T_12;
- D_*, C_*, D_♭ = D_acc, D′_*, D_b, D_NM, 21D_NM + 6, 22D_NM + 345, 22D_b + 345, k̄_0-hat.

So d_NM < 7.57245·10⁵⁵. T_11 < T_12 there.

**At P-D0's inputs** (9.99·10⁻¹⁴, 9.995·10⁻¹⁴, N̄_Λ = 77,112,616,084, D_e = 2.06834·10²³):

- D_acc = 45,626,410,950,904,844,471,104,575,139,346,875,130,945,114 < 4.56265·10⁴³;
- D_NM = 91,252,821,901,800,591,008,473,304,551,381,395,888,219,703 < 9.12529·10⁴³;
- 1.91631·10⁴⁵ and 2.00757·10⁴⁵, as P-D0.

"(a) alone" (N̄_Λ = 3,683,190,611, max form) reproduces the file's §1 exactly:

- T_11 > T_12 by 224,694,281,620,649,059,325;
- D_acc = 104,091,…,814,011 and D_NM = 208,182,…,464,022 < 2.08183·10⁴¹;
- 4.37183·10⁴² and 4.58002·10⁴².

**At the new choice** (ε_K = 14589/10¹⁴, ε_+ = 1459/10¹³, N̄_Λ = 3,683,190,611, k̄_0 = 3, J_* = 15,000,015, l_* = 50,
D_e = 1.41633·10²⁰), every integer of the texts is reproduced:

- Δβ_0 = 14,559,836,589·10⁻²⁰ exactly;
- L_< = 6,868,208,951 and L_> = R_b = 6,868,208,953;
- J′ = 765,000,816;
- N_ι = 5,188,959,638,229,843,970,554,286,700;
- k̄_max = 2,817,643,822,898,538,579;
- d̄_Φ = 228,357,817,884 and 62N̄_Λ + 10 = 228,357,817,892;
- C_lev = 10,377,919,276,459,687,944,791,764,540;
- I_base = 161,579,883,606,166,913 and R_base = 161,579,883,606,189,010;
- k̂_0 = 3,200,585,392,700;
- X_12 = 11,270,575,291,594,154,340;
- T_11 = 10,377,919,276,621,267,862,666,783,424 < T_12 = 10,377,919,287,730,263,270,654,748,732;
- D_* = T_12 + 14;
- C_* = 31,133,758,693,167,165,978,342,162,162, equal to the right side of eq:cs-c0;
- D′_* = 71,277,718,098,469,630,550,670,708,708,947,562,256;
- D_acc = 71,277,718,119,225,469,720,805,142,747,913,308,950 < 7.12778·10³⁷;
- D_NM = 142,555,436,217,695,100,271,475,851,685,218,689,090 < 1.42556·10³⁸;
- 21D_NM + 6 < 2.99367·10³⁹ and K ≤ 22D_NM + 345 < 3.13622·10³⁹;
- D_b < 7.12778·10³⁷, 21D_b + 6 < 1.4969·10³⁹ and 22D_b + 345 < 1.5682·10³⁹.

The max form and the T_12 form give the same D_NM there.

- F_1 = 1.4163178…·10²⁰ ≤ D_e. The proof file's "1.41631…" is right; the report's "1.41632…" is a slip (n3).
- Every product, sum and decomposition printed in U17, U18, U24–U30, U32–U36 and U38–U41 is asserted equal. That
  includes the three floor products, 10²⁰(1 + ε_K), the seven summands of prop:cs-cstar, the L_>C_lev, 497L_<,
  469R_b and 466(R_b + 1) of lem:cs-sharp, the four summands of D′_*, and D_♭ + D_*, D_♭ + D′_* and 22D_NM.
- Every printed decimal comparison holds in exact arithmetic (93 assertions, none failing). Among them:
  - 1/Δβ_0 < 6.868209·10⁹, 1/Δτ_0 < 6.847261·10⁹ and 1/(2Δβ_0Δτ_0) < 2.3514208·10¹⁹;
  - (1 + Δβ_0/2)² < 1 + 1.5·10⁻¹⁰ and (1 + ε_K + Δβ_0/2)² < 1 + 4.4·10⁻¹⁰;
  - the two T bounds, and the actual T_<, T_> < 2.35143·10¹⁹;
  - T_2 < 2.06047·10¹⁶, the window term < 4.84721·10¹⁷, and the first line < 1.41633·10²⁰;
  - 3ε_K + 2δ̂ + δ̄ < 2.015·10⁻⁸ and ε_Kδ̂ = 2.133116046·10⁻²⁰ exactly;
  - 3(1 − 2.015·10⁻⁸)/2.13312·10⁻²⁰ > 1.40639·10²⁰ (exact 3R bound 1.4063932…·10²⁰), and D_e/3R < 1.00707 < 1.0071;
  - U21's 3.12·10²⁸, U23's and U27's 8.64·10²⁰, and 8.411·10²⁰;
  - k̄ > 10³⁹, 48k̄ + 109 < 10⁻³⁷k̄², k̄ < 3.1362195968·10³⁹, 3.1362195968² < 9.83587336 and
    (4 + 10⁻³⁷) · 9.83587336·10⁷⁸ < 3.93435·10⁷⁹;
  - 3.094058² = 9.573194907364 and (4/3) · 9.573194907364·10⁴² > 1.27642·10⁴³;
  - 22 · 1.40639 = 30.94058.
- **The moved lower bounds:**
  - 0.3168/(4.71·10⁻²⁰)² = 1.42805…·10³⁸ > 1.42556·10³⁸ > D_NM (the exact threshold is 4.714·10⁻²⁰);
  - 3(1 − 2.1·10⁻⁸)/(1.45·10⁻¹⁹)² > 1.4268·10³⁸ > D_NM;
  - 1002001 · 1.447·10⁻²⁵ < 1.45·10⁻¹⁹;
  - 5 · 1.45·10⁻¹⁹ + δ̄ < 10⁻¹⁸ + δ̄ < 2.1·10⁻⁸.

## 4. The 60 texts

- **Each new text read against the merged chapter.** All are correct and state only what is proved.
  - The index sets of def:uc-choice are ℰ^φ (P-D0's T6). Accordingly, thm:uc-integer, prop:cs-cstar,
    lem:uc-small-orders, prop:uc-d-small and prop:uc-data-order (d) now read "with the choices of [[def:uc-choice]]".
  - The bounds for the index sets as constructed (cor:is-lower, eq:uc-lower, thm:loss-d's closing, the opening,
    01-introduction, 90-scope) are kept and qualified.
  - The choice-specific lower bound 3R > 1.40639·10²⁰ replaces 1.2250·10²⁷ wherever the choice is meant: U9, U19, U41.
- **sec:tr.**
  - U41a makes the index sets as constructed the section's standing assumption, and says the smaller sets are proved to
    serve at the computational point only.
  - thm:tr-transfer already says "Take … the index sets as constructed".
  - rem:tr-scope (U43a, U43), sec:tr-proof (U44a, U45), rem:ec-point-outside (U3a), rem:ec-lb-unbounded (U6a),
    03-theorems (U50a) and 90-scope (U53) carry the qualifier.
  - No text claims a bound for ℰ^φ at h ≠ 10⁻⁶.
  - prop:tr-fail and the bound 0.3168h⁻² do not depend on the index sets, and are stated without the qualifier, rightly.
- **Superseded numbers.** I grepped all 62 merged chapters for 54 old figures, including:
  - 7.57245, 7.5755, 9.12529, 1.66594, 2.00757, 1.59022, 3.78623, 6.32812, 1.89844, 5.13, 1.9·10³⁹;
  - 59,831,791, 77,112,616, 10,030,060, 1.23382, 1.2251, 1.0072, 2.695, 9.684, 1.11014, 8.3297, 7.9511;
  - 6.46·10⁻²⁹, 1.99·10⁻²⁸, 1.986·10⁻³⁴, 56,389,441, 1.6713522747, 4.22261, 2.04842, 1.79496, 5.98318;
  - 2.0538, 2.06834, 9.99·10⁻¹⁴, 58,991,214, 4,780,982, 316,405, 632,811, 1,407,588, 2,783,094, 27,881,614;
  - 37,862, 75,724, 1,665,937, 832,968, 2.448645, 1.6659378.

  Nothing remains except figures that belong to the index sets as constructed: 909,507,124,095,312 in thm:uc-reduction,
  sec:is, prop:is-count and rem:tr-scope; 1.6747·10⁻¹⁷ in the table and thm:is-gap. Every integer of ≥ 10 digits and
  every decimal·10^k in the evaluation sections is a new-choice value or unrelated.

## 5. Findings

### Major

None.

### minor

None.

### nit

**n1. U20, prop:uc-dependence statement:** "D_acc, D′_* and D_NM are the integers of [[thm:uc-integer]]".

- thm:uc-integer prints D_acc and D_NM. D′_* is printed in rem:uc-small-reading, which thm:uc-integer only cites.
- The sentence before already says that D′_* "is the number of [[rem:uc-small-reading]]".
- Replacement (whole lines of U20's new text, checked in nittree/: lint 0 hits, assemble 0 problems, `[] 0`, no line
  above 121 after resolution):

Old:
```old
[[def:uc-choice]] the inequality holds ([[lem:uc-small-orders]] (e)), and, with D_e of [[prop:uc-explicit]], D_acc, D′_*
and D_NM are the integers of [[thm:uc-integer]]. Each of N_ι, k̄_max, d̄_Φ, C_lev, I_base, R_base, T_11, T_12, C_* and
```
New:
```new
[[def:uc-choice]] the inequality holds ([[lem:uc-small-orders]] (e)), and, with D_e of [[prop:uc-explicit]], D_acc and
D_NM are the integers of [[thm:uc-integer]]. Each of N_ι, k̄_max, d̄_Φ, C_lev, I_base, R_base, T_11, T_12, C_* and
```

**n2. Optional, outside the 60 texts: rem:uc-missing, first paragraph** (chapter 71 with P-D0 lines 2880–2884, HEAD
2872–2876, after P-UB3 2904–2908).

- It cites [[thm:is-gap]] and [[prop:is-count]] for "(G), N_Λ, … are explicit".
- At the choice, which takes ℰ^φ, (G) and N_Λ come from cor:is-flat. lem:uc-lambda, also cited, rests on it, so the
  sentence is true; the citation is only incomplete.
- Replacement (checked in nittree/ as for n1):

Old:
```old
to 1 ([[thm:sp-spectrum]], [[cor:sp-lstar]]). With them (G), N_Λ, k̄_0, l_*, J_* and every number of steps of the long
iterations are explicit ([[thm:is-gap]], [[prop:is-count]], [[lem:uc-lambda]], [[prop:uc-explicit]]), and so is a bound
for the count n(E, w) of every index set whose exponents below 3 + ε_+ lie in Λ with the logarithmic orders k̄(λ)
([[lem:uc-n-iota]]), which [[lem:iii-i10-1-2]] (c) and [[lem:iii-i13-1-3]] (b) assert of every exponent that the level
steps produce.
```
New:
```new
to 1 ([[thm:sp-spectrum]], [[cor:sp-lstar]]). With them (G), N_Λ, k̄_0, l_*, J_* and every number of steps of the long
iterations are explicit ([[thm:is-gap]], [[prop:is-count]], [[cor:is-flat]], [[lem:uc-lambda]], [[prop:uc-explicit]]),
and so is a bound for the count n(E, w) of every index set whose exponents below 3 + ε_+ lie in Λ with the logarithmic
orders k̄(λ) ([[lem:uc-n-iota]]), which [[lem:iii-i10-1-2]] (c) and [[lem:iii-i13-1-3]] (b) assert of every exponent
that the level steps produce.
```
If taken, append "P-UB3 review n2: cor:is-flat cited" to the crosswalk note of rem:uc-missing.

**n3. Report only, no chapter text:** notes/reports/P-UB3.md, "The final choice and numbers", gives
"F_1 = 1.41632…·10²⁰".

- The value is 1.4163178…·10²⁰, as the proof file's §3 says ("F_1 = 1.41631…·10²⁰").
- D_e = 1.41633·10²⁰ ≥ F_1 either way.

Verdict: CONFIRMED
