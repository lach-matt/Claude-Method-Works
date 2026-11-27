# Report P-UB3: the chain at h = 10⁻⁶ without its two side hypotheses, and its evaluation

Proof file: research/warp-drive/paper/reader/proofs/P-UB3.md (2020 lines, md5 00c0b5a11bc2db904135d473bc60b6fb).
Nothing else in the repository was edited, and nothing was committed. Old texts are against HEAD (chapters 71, 00, 01,
03, 90 at md5 bb53f3e8…, 7304f875…, 648eb9ee…, aef99018…, f771640b…, unchanged since 2b9cb2ea) with P-D0's sixteen
texts applied (P-D0 confirmed at 1265f3bd, commit 5d862c93); chapter 71 with them: md5 1b1056fa….

## Part 1: outcome

**(a) 4k̄_max + 24 > I_base + 22,119 — removed by proof.**

- It is exactly T_11 < T_12 (T_12 − T_11 = X_12 − R_base − 22).
- Used only in lem:uc-small-orders (d) and (e) and rem:uc-small-reading, to say that the reads of Step 4′ (charged
  C_lev − 11 + I_lev + X_12 < T_12 and T_11) have order below T_12. Plus its consequences: P-D0's choice of
  N̄_Λ = 77,112,616,084 and N₁ in thm:tr-transfer (iii). lem:cs-rest and prop:cs-cstar only add T_11 and T_12.
- Without it the same proofs hold with max(T_11, T_12) in place of T_12 (the reference-point conditions have order
  ≤ C_lev + I_lev + R_base + 5 < T_11 + 14). So prop:uc-dependence holds with
  D′_* := max(T_11, T_12) + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base.
- Cost ≤ I_base + 22,119 (≈ 10⁻²¹ of D_NM).
- At P-D0's ε_K = 9.99·10⁻¹⁴, N̄_Λ can be the proved count 3,683,190,611:
  D_NM = 208,182,308,114,874,770,522,794,546,328,109,871,464,022 < 2.08183·10⁴¹ (P-D0 estimated 2.08·10⁴¹).

**(b) ε_+ < 10⁻¹³ — replaced by proof with ε_K < 0.998ε_Υ.**

- Explicit use: one numerical bound (T_2 and the count 3,000,004 in I_lev). Every admissible ε_+ meets it, as
  ε_+ < ε_ind ≤ δ_50 < δ̄ < 10⁻⁷ and (1 + 10⁻⁷) · 3.0000026·10⁶ + 2 < 3.000005·10⁶.
- Tacit uses of ε_K small:
  - ε_K + ε < ε_g, in Step 4 of prop:iii-i11-3-1 (lem:uc-admissible);
  - ε_K < ε_g − 2ε, so that the bases of lem:cs-rest (6) and sec:cs-small have no transition face round.

  With ε_g = ε_Υ and ε ≤ 10⁻³ε_g, both follow from ε_K < 0.998ε_Υ. Every other occurrence was checked.
- ε_Υ cannot be passed: def:iii-i10-1-3 itself asks ε_K < ε_Υ (so ε_K < ε_g), and Step 4 of prop:iii-i11-3-1 uses it.
  The factor 0.998 could go with a smaller ε. That is not drafted: the gain is < 0.21 % (1.42273·10³⁸ at
  ε_K = 1.4618·10⁻¹⁰, an estimate).

**Resulting bound:** d_NM < 1.42556·10³⁸.

## The final choice and numbers

**Choice:**
- ε_K = 1.4589·10⁻¹⁰, ε_+ = 1.459·10⁻¹⁰ (ε′_0 = 5·10⁻¹⁵ < 0.001ε_K);
- N̄_Λ = 3,683,190,611;
- unchanged: k̄_0 = 3, J_* = 15,000,015, l_* = 50, J′ = 765,000,816, ε_Υ = 1.4619·10⁻¹⁰, and P-D0's ℰ^φ_ind, ℰ^(ι,φ)_ind.
- At the choice T_11 < T_12, so the texts of lem:uc-small-orders and rem:uc-small-reading keep T_12.

**Values:**
- Δβ_0 = 1.4559836589·10⁻¹⁰;
- L_< = 6,868,208,951; L_> = R_b = 6,868,208,953;
- D_e = 1.41633·10²⁰ (F_1 = 1.41632…·10²⁰);
- N_ι = 5,188,959,638,229,843,970,554,286,700;
- C_lev = 10,377,919,276,459,687,944,791,764,540 < 1.0378·10²⁸;
- C_* < 3.11338·10²⁸;
- D_acc = 71,277,718,119,225,469,720,805,142,747,913,308,950 < 7.12778·10³⁷;
- D_NM = 142,555,436,217,695,100,271,475,851,685,218,689,090 < 1.42556·10³⁸;
- N_NM ≤ 21D_NM + 6 = 2,993,664,160,571,597,105,700,992,885,389,592,470,896 < 2.99367·10³⁹;
- K ≤ 22D_NM + 345 = 3,136,219,596,789,292,205,972,468,737,074,811,160,325 < 3.13622·10³⁹;
- for the fixed seminorms: d_NM < 7.12778·10³⁷, N_NM < 1.4969·10³⁹, K < 1.5682·10³⁹;
- K* (class ℰ_0^½): 1.27642·10⁴³ < K* < 3.93435·10⁷⁹.

**Lower bounds that move:**
- 3R > 1.40639·10²⁰ at the choice, D_e < 1.0071 · 3R;
- K > 22d > 3.094058·10²¹;
- rem:ec-lb-unbounded and the line after prop:tr-mu-small: h ≤ 4.71·10⁻²⁰;
- prop:tr-fail: ε_ind(h) < 1.45·10⁻¹⁹ gives > 1.4268·10³⁸ for 0 < |h − h_c| < 1.447·10⁻²⁵.

**Lower bounds unchanged:**
- 1.403·10²⁰ at every admissible choice;
- 1.2250·10²⁷ for the index sets as constructed. eq:uc-lower is now stated as such.

**Reproduction:** at HEAD's inputs the formulas give HEAD's 21 integers exactly, and P-D0's D_acc and D_NM at its own
inputs.

## Sites changed (60 texts, U1–U53 with U3a, U6a, U22b, U41a, U43a, U44a, U50a)

**Chapter 71:**
- the opening (U1–U3);
- rem:ec-point-outside, last sentence (U3a);
- thm:loss-d (U4, U5);
- rem:ec-lb-unbounded (U6, U6a);
- rem:ec-upper-point (U7), rem:ec-upper-open (U8), sec:uc-close (U9);
- lem:uc-fourier-count, last sentence (U10);
- def:uc-choice, lem:uc-admissible, lem:uc-lambda (U11–U15, on P-D0's T6–T9 and T12);
- lem:uc-n-iota (U16, U17), prop:uc-explicit (U18);
- thm:uc-integer (U19: "with the index sets of def:uc-choice"; eq:uc-lower qualified);
- prop:uc-dependence (U20: Part 1, and either family of index sets);
- rem:uc-missing (U21);
- cor:is-lower (U22, U22b): the former-choice clause removed; optional;
- sec:cs opening (U23), lem:cs-levels (U24), lem:cs-iterations (U25), lem:cs-rest (U26);
- prop:cs-cstar and rem:cs-sharpness (U27);
- sec:cs-small R_base (U28), lem:cs-sharp (U29, U30);
- lem:uc-small-orders (U31–U35), rem:uc-small-reading (U36), prop:uc-d-small (U37–U39);
- prop:uc-data-order (d) (U40, U41);
- sec:tr:
  - opening (U41a);
  - thm:tr-transfer (iii) (U42: N₁ removed; disjoint from P-D0's T16);
  - rem:tr-scope (U43a, U43);
  - sec:tr-proof (iii) (U44a, U44, U45);
  - prop:tr-fail (U46);
  - the paragraph after prop:tr-mu-small (U47).

**Other chapters:** 00-front (U48), 01-introduction (U49), 03-theorems (U50, U50a), 90-scope (U51–U53).

Every sec:tr statement and every sentence built on it is kept or made explicitly "for the index sets as constructed".
No bound for ℰ^φ at other h is claimed.

## sec:tr once the flat set serves (listed in the file's section 5, not rewritten)

- def:tr-excess: μ♭(h) and a count linear in the y_ι.
- prop:tr-lambda:
  - (a): only 𝔡₁ as an increment below 1;
  - (b): "(G) iff ε_K < μ(h)" stays true for the sets as constructed; for Λ^φ it becomes "iff ε_K < μ♭(h)";
  - (c): the linear count.
- thm:tr-transfer:
  - (ii) is for the sets as constructed only;
  - (iii) with ℰ^φ, ε_K < min(μ♭(h), 0.998ε_Υ) and N̄♭(h).
- prop:tr-mu-small: uses 𝔡₀ as an increment, so it does not apply to Λ^φ.
- These would follow: the sec:tr opening, sec:tr-proof (iii), rem:tr-scope, and the sentences built on them.
- All of this first needs thm:is-flat-serves proved at h.

## Checks

On the scratch copy (working tree, with chapters 71/00/01/03/90 equal to HEAD, + P-D0 T1–T16 + the 60 texts parsed back
from the file and applied by matching):
- lint --chapters: 0 hits (5088 labels);
- assemble --check: 0 problems;
- the required assembled-paper command prints `[] 0`.

Every new line has at most 121 characters, also after labels resolve. No wrapped line starts with a marker.

Scratch work: /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pub3/
- chain3.py: the exact chain;
- vals3.py: the printed values, with asserts;
- blocks3.py: the templates;
- gen3.py, mkfile3.py, verify3.py: generation, assembly and verification.
