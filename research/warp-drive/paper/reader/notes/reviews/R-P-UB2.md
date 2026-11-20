# R-P-UB2: line-by-line review of proofs/P-UB2.md

**File reviewed: the final version, md5 69990efadbb064fb43ca5679c0b9d705, 2001 lines** (commit b1b958c4), as the
coordinator asked mid-review. I read the provisional version (md5 eb5f55fcc614dcad6625c8778ac03c70, 1946 lines) in
full first. A word-level diff of every new block confirms the coordinator's delta. Words change only in M6, M7, M8 and
M15a (items 3–6 of the file's §8). Every other block differs only in its numbers or its wrapping, and
prop:uc-dependence (M12 and F6) is identical. So the structural reading carries over unchanged. Line numbers below are
those of the final file unless marked "(eb5f)". I edited no repository file.

## Verdict

**NOT CONFIRMED.** Open findings: **2 Major, 1 minor, 7 nits.** Numbers aside, the main set is right, including the
split-level improvement and the two reality repairs. Every printed integer and decimal of the final main set checks in
exact arithmetic at P-UB1's inputs.

- **Major 1.** The proof of prop:uc-dependence leaves out a hypothesis it uses: T_11 < T_12. The proposition fails to
  be proved for every admissible ε_K below about 8.47·10⁻¹⁸.
- **Major 2.** The fallback set is not usable as drafted.
- **minor 1.** In M10, the identity printed for N_ι is false.

Four defects of the provisional version were fixed in the final:

- the four lines over 121 characters in the assembled paper;
- M15a's citation of lem:iii-i10-1-2 (a);
- FO4's indentation;
- three wrapped lines that started with "− ".

## Findings

### Major 1. prop:uc-dependence uses T_11 < T_12, which its hypotheses do not give (M12 lines 739–773; F6 1685–1719)

**Current text** (statement; proof, first sentence):

    [[def:uc-choice]], except that ε_K and ε_+ are any numbers with 0 < ε_K < ε_+ < 10⁻¹³ for which it is admissible, and let
    N̄_Λ ≥ N_Λ, k̄_0, J_* and l_* be integers for which [[lem:uc-lambda]] (b) and (c) hold, with J′ := (J_* + 1)(l_* + 1).
    ...
    with D_e any number at least F_1. Then d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM and N_NM ≤ 21D_NM + 6. ...
    *Proof.* The proofs of [[prop:uc-explicit]], ..., [[rem:uc-small-reading]] and [[prop:uc-d-small]] use, of
    the numbers of [[def:uc-choice]] and [[lem:uc-lambda]], only N_Λ ≤ N̄_Λ, k̄(λ_i) ≤ k̄_0 + J′i, Δβ ≥ Δβ_0, a♭_K − 2 ≥
    Δβ_0, Δτ ≥ Δτ_0, ε_K < ε_+ < 10⁻¹³ and the bounds of [[lem:is-offsets]] (b); and they give ...

**What is wrong.**

**(a) The proofs use more than the listed inputs.**

- lem:uc-small-orders (d) (chapter 71 at HEAD, "charged at most C_lev − 11 + I_lev + X_12 and T_11 ([[lem:cs-rest]]),
  both less than T_12") needs T_11 < T_12.
- rem:uc-small-reading's "ρ_K ≤ T_12 + 2 + C_lev − 11 + I_lev, Step 4′ reading the solution at α at an order below
  T_12 + 2" (M24) needs it too.
- With T_11 = 20,183 + 1,914 + I_base + 22 + C_lev + I_lev and T_12 = C_lev + I_lev + X_12, the inequality T_11 < T_12
  is X_12 = 4k̄_max + 24 > I_base + 22,119.
- lem:uc-small-orders (e) (M23c) also uses 2R_base + 16 < T_12 and X_12 > R_base − 9.

Under the old inputs these held with room to spare: X_12 ≈ 5.1·10²² against I_base ≈ 1.4·10²¹. Now:

- X_12 is fixed by N̄_Λ: 2,783,094,768,362,907,767,098,404.
- I_base + 22,119 = 1,407,588,774,438,516,741,176,921, about 2.35·10⁷/(0.998ε_K), which grows as ε_K falls.
- The margin at the choice is only a factor 1.98.
- At N̄_Λ = 909,507,124,095,312 the inequality fails for every ε_K below about 8.47·10⁻¹⁸, computed exactly:
  R_b ≥ 118,299,852,598,340,691.
- P-UB1's thm:is-gap makes every ε_K ∈ (0, μ_Z) admissible.

So the proposition is not proved on about half of the range it states. Where T_11 > T_12, the argument gives d_NM up to
about D_NM + R_base, not D_NM. The bound at the choice is unaffected: there T_11 < T_12 holds, as the printed X_12 and
I_base show.

**(b) Two smaller gaps in the hypotheses.**

- "For which it is admissible" does not give Δβ ≥ 0.999²ε_K or a♭_K − 2 ≥ 0.999²ε_K. lem:uc-admissible derives these
  from the specific values (ε′_0 < 0.001ε_K), yet the proof lists them as used.
- "Integers for which [[lem:uc-lambda]] (b) and (c) hold" cannot cover other k̄_0, J_*, l_*, since (b) fixes their
  values. What the proof uses is (c).

**Replacement** for the whole statement and proof of prop:uc-dependence (M12 lines 739–773, and identically F6
1685–1719):

```
**Proposition {#prop:uc-dependence}** (The bound as a function of the choice.) Let a choice be made as in
[[def:uc-choice]], except that ε_K and ε_+ are any numbers with 0 < ε_K < ε_+ < 10⁻¹³ for which it is admissible and the
hypotheses of [[prop:ec-upper]] and of [[eq:ec-upper-counts]] hold with Δβ_0 := 0.999²ε_K and Δτ_0 := 0.999ε_Υ, as
[[lem:uc-admissible]] shows at the choice of [[def:uc-choice]], and let N̄_Λ ≥ N_Λ, k̄_0, J_* and l_* be integers with
which [[lem:uc-lambda]] (c) holds, with J′ := (J_* + 1)(l_* + 1). Put L_<, L_> and R_b as in [[eq:uc-levels]], N_ι as in
[[eq:uc-n-iota]], k̄_max := k̄_0 + J′N̄_Λ, d̄_Φ := 62N̄_Λ + 2, C_lev := 2N_ι + N̄_Λ + 529, I_lev := 34,268,829,852,
I_base := 935R_b + 466 + 23,524,832(R_b + 3), T_12 := C_lev + I_lev + 4k̄_max + 24, R_base := 22,097 + I_base,

    F_1 := 3((1 + Δβ_0/2)² + (1 + ε_K + Δβ_0/2)²)/(2Δβ_0Δτ_0) + 3(3 + 2ε_K)/Δβ_0 + 6 + 4/Δτ_0 + 8
           + 3((1 + ε_K)/Δβ_0 + 1)((1 + ε_+)/𝔡₁ + 2) + 16(0.4901/𝔡₁ + 1)((3 + ε_K)/Δβ_0 + 5),
    C_* := 6N_ι + 3N̄_Λ + 3I_lev + 8k̄_max + I_base + d̄_Φ + (N̄_Λ + 2)(d̄_Φ + 30) + 45,862,
    D′_* := T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base,
    D_acc := D_e + 497L_< + L_>C_lev + 935R_b + 466 + C_*,     D_NM := D_acc + D′_* + d̄_Φ,

with D_e any number at least F_1, and suppose that 4k̄_max + 24 > I_base + 22,119. Then d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM
and N_NM ≤ 21D_NM + 6. Each of N_ι, k̄_max, d̄_Φ, C_lev, I_base, T_12, R_base, C_*, D′_* and D_acc − D_e is a polynomial
with non-negative coefficients in N̄_Λ, k̄_0, J′, L_<, L_> and R_b; L_<, L_> and R_b are non-increasing in ε_K, and F_1
is non-increasing in ε_K and non-decreasing in ε_+. So, with D_e := F_1, D_acc and D_NM are non-decreasing in N̄_Λ, k̄_0,
J′ and ε_+ and non-increasing in ε_K. Moreover D_acc = L_>C_lev + D_e + 497L_< + 935R_b + 466 + C_*, and L_>C_lev >
J′N̄_Λ(N̄_Λ + 1)(1 + ε_K)/Δβ_0: the bound is at least quadratic in N̄_Λ and of the order 1/ε_K.

*Proof.* The proofs of [[prop:uc-explicit]], [[lem:cs-levels]], [[lem:cs-base]], [[lem:cs-iterations]], [[lem:cs-rest]],
[[prop:cs-cstar]], [[lem:cs-sharp]], [[lem:uc-small-orders]], [[rem:uc-small-reading]] and [[prop:uc-d-small]] use, of
the numbers of [[def:uc-choice]] and [[lem:uc-lambda]], only N_Λ ≤ N̄_Λ, k̄(λ_i) ≤ k̄_0 + J′i, Δβ ≥ Δβ_0, a♭_K − 2 ≥
Δβ_0, Δτ ≥ Δτ_0, ε_K < ε_+ < 10⁻¹³ and the bounds of [[lem:is-offsets]] (b), and, in Steps 4′ and 4 of
[[lem:uc-small-orders]] (d) and in [[rem:uc-small-reading]], T_11 < T_12 ([[lem:cs-rest]]), which is the inequality
supposed. With it every order of the smallness conditions is at most max(2R_base + 16, T_12 + 14, C_lev + I_lev +
R_base + 5) ≤ D′_* for the fixed seminorms of [[lem:uc-small-orders]] (d) (the proof of its (e)), and at most D′_* for
those of [[rem:uc-small-reading]]; so they give d_acc, d_R ≤ D_acc and d_NM ≤ D_NM with the expressions above. F_1 is the
bound for the first line of [[eq:ec-upper]] that [[eq:ec-upper-counts]], [[eq:uc-t2-w]], ℓ⁺_tf = 1, r_ι ≤ 16 and η_2 −
η_1 < ε_+ give, with N_< ≤ 1/Δβ_0, N_> ≤ (1 + ε_K)/Δβ_0 + 1 and N_b ≤ 1/Δβ_0 + 1 ([[eq:ec-upper-counts]]): 3(T_< + T_> +
T_2) + 4(1/Δτ + 2) + 16W(N_< + N_> + N_b + 3), 1/Δτ ≤ 1/Δτ_0, written out; 1/𝔡₁ may be replaced by any upper bound. C_*
is the right side of [[eq:cs-c0]] written out (1,587 + 44,227 + 48 = 45,862 and 2X_12 = 8k̄_max + 48), I_base is that of
[[eq:cs-iterations]] (469R_b + 466(R_b + 1) = 935R_b + 466 and 16 · 1,470,302 = 23,524,832), and 22,097 = 20,183 + 1,914.
These are sums of products of N̄_Λ, k̄_0, J′, L_<, L_>, R_b and positive constants, so they do not decrease when one of
these integers increases. As ε_K increases, Δβ_0 increases, and 1/Δβ_0 and (1 + ε_K)/Δβ_0 = 1/Δβ_0 + 1/0.998001 decrease,
and so do their integer parts; each term of F_1 is non-increasing in ε_K, as x ↦ (1 + cx)²/x decreases on (0, 1/c) and
(1 + ε_K)/Δβ_0 and (3 + ε_K)/Δβ_0 decrease, and ε_+ enters F_1 only through the factor 1 + ε_+. Finally C_lev > 2N_ι ≥
J′N̄_Λ(N̄_Λ + 1) and L_> > (1 + ε_K)/Δβ_0. ∎
```

**Why the max bound holds.** Under the reading of lem:uc-small-orders (d), the orders are:

- 20,183, k̄_0 + 5 and 2R_base + 16 for (a)–(c);
- ρ + 14 with ρ < T_12 in Steps 4′ and 4, by T_11 < T_12;
- ρ + R_base + 16 with ρ ≤ C_lev − 11 + I_lev at a reference point.

Since C_lev + I_lev < T_12, all of these are at most T_12 + 2R_base + 18 ≤ D′_*. So D_NM covers both readings without
2R_base + 16 < T_12.

**Checks on the replacement.**

- Every line is at most 121 characters, both in the source and with labels resolved.
- Merged at HEAD b1b958c4 with P-UB1's T1–T14 and the rest of the final main set: lint --chapters gives 0 hits (4815
  labels), assemble --check 0 problems, assemble 0, lint --paper 0 hits.
- At the choice, 4k̄_max + 24 = X_12 = 2,783,094,768,362,907,767,098,404 > 1,407,588,774,438,516,741,176,921 =
  I_base + 22,119.

**Optional, M23c line 1215.** "exceeds R_base." → "exceeds R_base + 22, so that also T_11 < T_12 in (d)." This prints
the check that (d) relies on at the choice.

### Major 2. The fallback set is not usable as drafted (§6 lines 1508–1519 and the rule-kept blocks)

**Current text:** "**Rule for the other main blocks (M6–M11, M13–M25):** apply them with every evaluated number deleted together
with the words that state it (...) ... Since P-UB1 proved an admissible choice, this set is not needed; it is kept as
asked."

**What is wrong.** For about 20 blocks the rule is all there is; their fallback text is not written out. Applied
literally, the rule gives the following.

**(i) It contradicts its own premise.** The set applies "if no admissible choice is proved", yet the blocks the rule
keeps now cite P-UB1's proved results:

- M6 (line 365) "(G) holds exactly for ε_K < μ_Z ... ([[thm:is-gap]], [[eq:is-mu-z]])";
- M7 (427) "With them (G) holds exactly for ε_K < μ_Z";
- M8 (456), likewise;
- M15a (900) "real part at most 2.514 are real ([[prop:is-lambda]])".

Without P-UB1's texts, eq:is-mu-z is undefined and these claims are unproved. The fallback was checked only merged
with P-UB1 (§7).

**(ii) Some sentences become false.**

- M6 (359): "at the computational point all four are bounded: (1), (2) and (4) are evaluated". Item (1), ε_K and N_Λ,
  is not evaluated under the premise.
- M7 (428): "[[sec:uc-eval]] fixes an admissible choice of the weights, evaluates every count of [[eq:ec-upper]] at it".

**(iii) Some definitions dangle.**

- The rule deletes "is less than D_e := 1.23382·10²⁷" (M11, 617). lem:cs-sharp (M22, 1132: "With D_e, L_<, L_> and
  R_b of [[prop:uc-explicit]]") still uses D_e.
- The rule deletes the *The counts.* paragraph of prop:uc-explicit (M11, 632). That paragraph proves 1/Δτ_0 <
  6.847261·10⁹, (1 + η_2 − η_1)/𝔡₁ + 2 < 3.000005·10⁶ and the 1,470,302-window count. lem:cs-iterations (a) cites
  these for I_lev, and lem:uc-small-orders (d) cites them too; both stay in the fallback.
- "N_Λ ≤ N̄_Λ := 909,…" becomes "N_Λ ≤ N̄_Λ" (M9, 493). N̄_Λ is then defined nowhere, and lem:uc-lambda (a)'s proof
  ("is [[prop:is-count]] (a)") no longer applies.

**(iv) Some sentences break.**

- M13 (833) "make all of D_acc but less than 1.9·10³⁹ ([[lem:cs-sharp]]), far above D_e".
- M14 (878) "less than 6N_ι + 5.13·10³¹".
- M20 (1054, 1060) "all but less than 5.13·10³¹ is 6N_ι", "being all of D_acc but less than 1.9·10³⁹".
- M20 (1037): C_* is defined only as 6N_ι + 3N̄_Λ + (an evaluated constant).

**(v) A sentence the set does not cover.** thm:uc-reduction's closing paragraph (chapter 71 at HEAD, lines 2566–2568):
"the upper bound of [[thm:uc-integer]], in which every number of steps of the long iterations and every count of an
index set is explicit".

**(vi) It inherits Major 1.** At an ε_K that is not evaluated, nobody can check whether T_11 < T_12 and 2R_base + 16 <
T_12 hold. Then D_* = T_12 + 14 (lem:uc-small-orders (e), prop:uc-d-small (b)) and D′_* are not proved.

**Replacement.** Preferred: delete §6 (F1–F9, FO1–FO7) and the fallback rows of the §4 table. P-UB1 proves the
admissible choice, and §6 itself says the set is not needed. If the set is kept, it needs explicit blocks that cite
nothing of P-UB1. The minimum is the following exact replacements in the rule-kept blocks, plus the items after them.

- M6 (358–359): "at the computational point all four are bounded: (1), (2) and (4) are evaluated, and (3) through the
  numbers C_lev and C_*, which [[lem:cs-levels]] and [[prop:cs-cstar]] bound." → "at the computational point (2) and
  (4) are evaluated, (3) is bounded through the numbers C_lev and C_*, which [[lem:cs-levels]] and [[prop:cs-cstar]]
  bound in terms of (1), and (1) is bounded but not evaluated."
- M6 (364–366): "and with the generators 1 + 𝒵 of Λ (G) holds exactly for ε_K < μ_Z, where μ_Z < 1.6747859·10⁻¹⁷
  ([[thm:is-gap]], [[eq:is-mu-z]]); [[prop:is-count]] and [[cor:sp-lstar]] give N_Λ ≤ 909,507,124,095,312, k̄_0 = 3"
  → "and the generators 1 + 𝒵 of Λ ask ε_K < 1.67488·10⁻¹⁷ ([[thm:is-gap]]); neither the admissible ε_K nor N_Λ is
  evaluated here, and [[prop:is-count]] and [[cor:sp-lstar]] give k̄_0 = 3".
- M7 (427–429): "With them (G) holds exactly for ε_K < μ_Z ([[thm:is-gap]]), and N_Λ, k̄_0, l_* and J_* are explicit
  ([[prop:is-count]], [[cor:sp-lstar]]). [[sec:uc-eval]] fixes an admissible choice of the weights, evaluates every
  count of [[eq:ec-upper]] at it, and proves" → "With them k̄_0, l_* and J_* are explicit ([[prop:is-count]],
  [[cor:sp-lstar]]); the admissible ε_K and N_Λ are not evaluated here. [[sec:uc-eval]] takes a choice of the weights
  as in [[def:uc-choice]] at an admissible ε_K, bounds every count of [[eq:ec-upper]] at it in terms of ε_K, and
  proves".
- M8 (456–457): "(G) holds exactly for ε_K < μ_Z, where 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷ ([[thm:is-gap]],
  [[eq:is-mu-z]]); N_Λ ≤ 909,507,124,095,312, k̄_0 = 3" → "every ε_K with which (G) holds is below 1.67488·10⁻¹⁷
  ([[thm:is-gap]]), and neither the admissible ε_K nor N_Λ is evaluated here; k̄_0 = 3".
- M9 (493): "(a) N_Λ = #(Λ ∩ {Re < 3 + ε_+}) is an integer with N_Λ ≤ N̄_Λ := 909,507,124,095,312;" → "(a) N_Λ =
  #(Λ ∩ {Re < 3 + ε_+}) is finite, and N̄_Λ denotes an integer with N̄_Λ ≥ N_Λ;". In its proof, "(a) is
  [[prop:is-count]] (a)." → "(a) is [[lem:iii-i10-1-2]] (a)."
- M11:
  - keep "and every window loop has at most 1,470,302 windows", the bounds of 1/Δτ_0, 1/𝔡₁ and 0.4901/𝔡₁, and the
    sentence ending "< 3.000005·10⁶";
  - replace "is less than D_e := 1.23382·10²⁷; of it, the window loops at ι⁺ contribute less than 4.22261·10²⁴." by
    "is at most D_e := F_1 of [[prop:uc-dependence]].";
  - put the display eq:uc-counts as "1/Δτ_0 < 6.847261·10⁹,   (1 + η_2 − η_1)/𝔡₁ + 2 < 3.000005·10⁶,   W <
    1,470,302.27".
- M13 (832–833): "at most L_> = 59,831,791,007,643,520 of them, each charged at most C_lev < 6.32812·10³⁸, make all of
  D_acc but less than 1.9·10³⁹ ([[lem:cs-sharp]]), far above D_e." → "at most L_> of them, each charged at most C_lev,
  give the term L_>C_lev of D_acc ([[lem:cs-sharp]], [[prop:uc-dependence]])."
- M14 (877–878): "less than 6N_ι + 5.13·10³¹ ([[lem:cs-rest]]). So c_* ≤ C_* < 1.89844·10³⁹" → "at most C_*
  ([[lem:cs-rest]]). So c_* ≤ C_*".
- M20:
  - put the display as "c_* ≤ C_* := 6N_ι + 3N̄_Λ + 3I_lev + 8k̄_max + I_base + d̄_Φ + (N̄_Λ + 2)(d̄_Φ + 30) + 45,862.";
  - in rem:cs-sharpness, "Of the bound of [[eq:cs-cstar]], all but less than 5.13·10³¹ is 6N_ι:" → "The term 6N_ι of
    the bound of [[eq:cs-cstar]] is";
  - "L_>C_lev being all of D_acc but less than 1.9·10³⁹" → "giving the term L_>C_lev of D_acc".
- thm:uc-reduction, closing paragraph: "in which every number of steps of the long iterations and every count of an
  index set is explicit." → "an explicit function of the admissible ε_K and of the counts of the index sets
  ([[prop:uc-dependence]])."

Two further items for a kept fallback:

- It needs Major 1's hypothesis carried into F1, F3, F5, F6 and F9 ("explicit functions ... when 4k̄_max + 24 >
  I_base + 22,119").
- Or it uses the form valid at every admissible ε_K: replace T_12 by T_12 + R_base in D_* and D′_*. This holds because
  T_11 − T_12 = I_base + 22,119 − X_12 < R_base.

### minor 1. M10: the identity printed for N_ι is false (lines 550–553)

**Current text:**

    (k̄_0 + 1)N_Λ + J′N_Λ(N_Λ + 1)/2, which increases with N_Λ; at N_Λ = N̄_Λ = 909,507,124,095,312, where (N̄_Λ + 1)/2 =
    454,753,562,047,656, it equals

        4 · 909,507,124,095,312 + 765,000,816 · 909,507,124,095,312 · 454,753,562,047,656 = N_ι.

**What is wrong.**

- N̄_Λ is even, so (N̄_Λ + 1)/2 = 454,753,562,047,656.5 is not 454,753,562,047,656.
- The display evaluates 4N̄_Λ + J′N̄_Λ²/2, which falls short of N_ι by J′N̄_Λ/2 ≈ 3.48·10²³. The printed N_ι is right,
  so this display is the only thing in error.
- The provisional version had the same defect at N̄_Λ = 910,000,000,000,000, also even.
- The generator's template "(N̄_Λ + 1)/2 = <<NLp1h>>" (blocks_main.py) is right only for odd N̄_Λ.

**Replacement:**

    (k̄_0 + 1)N_Λ + J′N_Λ(N_Λ + 1)/2, which increases with N_Λ; at N_Λ = N̄_Λ = 909,507,124,095,312, where N̄_Λ/2 =
    454,753,562,047,656, it equals

        4 · 909,507,124,095,312 + 765,000,816 · 454,753,562,047,656 · 909,507,124,095,313 = N_ι.

The new identity is exact, the lines are within 121 characters, and the merge checks pass. The generator should branch
on parity: "N̄_Λ/2 = h" with J′ · h · (N̄_Λ + 1) when N̄_Λ is even, and the current form when it is odd.

### Nits

1. **M3, lines 271–272.** "1.59022 ×" / "10⁵⁷." splits the number. Replace by "and N_NM at most one below" /
   "1.59022 × 10⁵⁷.".
2. **M25a, line 1304.** "with D_NM := D_♭ + D′_* + d̄_Φ of [[thm:uc-integer]]" defines D_NM a second time. Replace by
   "with D_NM = D_♭ + D′_* + d̄_Φ of [[thm:uc-integer]]".
3. **FO3, lines 1834–1836.** "an upper bound there is an explicit function of the admissible ε_K of the set Λ" leaves
   out the counts, which F1 and FO5 include. Add "and of the counts of the index sets". Chapter 03 writes "× 10" and
   never "·10", so FO3's "1.6747859·10⁻¹⁷" should read "1.6747859 × 10⁻¹⁷".
4. **FO2, lines 1816–1817.** It leaves a line holding the single word "A". This is cosmetic.
5. **M23a, line 1168.** lem:uc-small-orders (b) defines k̄_0 := 20,602 + 466R_b, while k̄_0 = 3 is now a named input of
   eq:uc-n-iota, lem:uc-lambda and prop:uc-dependence in the same chain. The clash predates P-UB2. Rename the local one
   (for instance k̂_0) in M23a and in (b)'s proof and (c) at HEAD. Optional.
6. **Generator.** The templates hard-code "k̄ > 10⁵⁷", "10⁻⁵⁵" (M26b) and "1.0072" (M12). They hold at the final
   inputs; recheck them on any regeneration.
7. **File header.** It gives 90-scope.md as md5 8c96f1f3…, but HEAD b1b958c4 has f8bb7fcc…. The quoted lines O4 and FO5
   still occur once, at the stated lines.

## What I checked and found correct

**Old texts.**

- All 52 old texts (M1–M26b, O1–O4, F1–F9, FO1–FO7) occur exactly once, as whole lines, at the stated line numbers.
  I checked this at HEAD 51844d44 (start), 4efdaefb and b1b958c4 (final). Chapters 01, 03 and 90 changed between them,
  but the quoted lines did not.
- Within a set no two blocks overlap, and no block overlaps P-UB1's T1–T14.

**Scratch merges** in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rpub2/,
from a git archive of b1b958c4. Nothing was run in the repository, and assemble.py ran only there.

| merge | lint --chapters | assemble --check | assemble | lint --paper |
|---|---|---|---|---|
| base (fbase/) | 0 hits, 4803 labels | 0 problems | 0 problems | 0 hits |
| P-UB1 T1–T14 + main set (fmain/) | 0 hits, 4815 labels | 0 problems | 0 problems | 0 hits |
| P-UB1 + fallback set + main blocks it keeps (ffall/) | 0 hits, 4815 labels | 0 problems | 0 problems | 0 hits |
| P-UB1 + main set + my fixes for Major 1, minor 1, nits 1–2 (ffix/) | 0 hits, 4815 labels | 0 problems | 0 problems | 0 hits |

- Every new line of the final is at most 121 characters (Python len).
- No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|", and none starts with "− ".
- The provisional version gave 4 lint --paper hits (eb5f lines 376, 424, 814, 822). They are gone in the final.

**Exact rational arithmetic at the old inputs** (ε_K = 1.6416·10⁻¹⁴, N̄_Λ = 16,747,199,999,999, printed
R_b = 61,038,200,000,000, C_* = 6.4368·10³⁵, D_e = 1.2587·10²⁴, M_c = 2.44153·10¹⁴). The formulas reproduce every
printed integer of the old chain:

- N_ι, k̄_max, d_Φ, C_lev, I_lev, I_base, X_12, T_12, D_*;
- R_base, 2R_base + 16, the c_0 bound of eq:cs-cstar and its tail 17,389,163,815,025,371,354,557,103,786;
- K̄ = ⌊(2 + ε_K)/Δβ_0⌋, D_♭, D′_*, K̄(C_lev + I_lev − 9);
- prop:uc-d-small (b) with 21·(b) + 6, and (c);
- D_acc = D_e + M_c C_*, and the small-orders k̄_0.

F_1 = 1.25869033·10²⁴ < 1.2587·10²⁴, and the windows contribute 4.30774·10²¹ < 4.30775·10²¹. At the old inputs the split
form gives D_♭ ≈ 1.309628·10⁴⁹ and D_NM ≈ 2.619256·10⁴⁹, as claimed. R-V-I11's scaling reproduces the new level-by-level
form to 12 digits.

**Exact arithmetic at the final inputs** (ε_K = 1.6747·10⁻¹⁷, ε_+ = 1.67478·10⁻¹⁷, N̄_Λ = 909,507,124,095,312, k̄_0 = 3,
J′ = 765,000,816).

- Every comma-grouped integer in the final blocks equals the exact value of the quantity at its place. I mapped each to
  its named quantity, compared positions with the provisional text (checked separately), and checked the 12 residual
  integers one by one.
- The three products 16,713,522,747 · L show ⌊1/Δβ_0⌋ = 59,831,791,007,643,518 and ⌊(1 + ε_K)/Δβ_0⌋ =
  59,831,791,007,643,519.
- These final values are exact: N_ι, k̄_max, d̄_Φ, C_lev, I_base, R_base, X_12, T_12, D_*, C_* (= 6N_ι + 3N̄_Λ + seven
  numbers), D_♭, D′_*, D_b, D_NM, 21D_NM + 6, 21D_b + 6, 22D_NM, 22D_NM + 345, 22D_b + 345, and the small-orders k̄_0.
  So are the products in M22's and M24's *integer* paragraphs.

35 decimal and inequality checks, all true:

- F_1 = 1.2338127·10²⁷ < D_e = 1.23382·10²⁷; windows 4.2225993·10²⁴ < 4.22261·10²⁴; the whole decimal chain of M11's
  proof (1/Δβ_0, 1/(2Δβ_0Δτ_0), T_<, T_>, T_2, W, the 3 · 5.98318·10¹⁶ + 3 step, the final sum);
- N_ι < 3.16406·10³⁸, C_lev and D_* < 6.32812·10³⁸, C_* < 1.89844·10³⁹;
- D_acc − L_>C_lev < 1.9·10³⁹, C_* − 6N_ι < 5.13·10³¹, (N̄_Λ + 2)(d̄_Φ + 30) < 5.129·10³¹;
- D_acc, D′_*, D_b < 3.78623·10⁵⁵, D_NM < 7.57245·10⁵⁵, 21D_b + 6 < 7.9511·10⁵⁶, N_NM < 1.59022·10⁵⁷;
- K < 1.66594·10⁵⁷, 22D_b + 345 < 8.3297·10⁵⁶;
- k̄ > 10⁵⁷ with 48k̄ + 109 < 10⁻⁵⁵k̄², k̄ < 1.6659378235·10⁵⁷, 1.6659378235² < 2.775348832, (4 + 10⁻⁵⁵)·2.775348832·10¹¹⁴ <
  1.11014·10¹¹⁵, and 4k̄² + 48k̄ + 109 < 1.11014·10¹¹⁵ directly;
- ε_Kδ̂ = 2.448645858·10⁻²⁷ exactly, 3R > 1.2251·10²⁷, 1.0072 · 1.2251·10²⁷ > 1.23382·10²⁷;
- 0.3168·(6.46·10⁻²⁹)⁻² > 7.57245·10⁵⁵; the exact threshold is h ≤ 6.4681·10⁻²⁹;
- 2R_base + 16 < T_12, X_12 > R_base, and X_12 > I_base + 22,119;
- leading digits 3.786222, 7.951066, 7.572444, 1.590213 and 1.6659378.

Option L's arithmetic (§8) also checks: 22 · 1.2250·10²⁷ = 2.695·10²⁸, (4/3)·7.263025·10⁵⁶ > 9.684·10⁵⁶, and
21 · 1.2250·10²⁷ + 6 > 2.5725·10²⁸.

**The formulas of prop:uc-dependence, re-derived from chapter 71.**

- L_<, L_> and R_b come from lem:ec-counts (a), (f) and eq:ec-upper-counts by integrality. In (2, 3) the levels number
  m < (3 − α_1)/Δβ ≤ 1/Δβ_0, so m ≤ ⌊1/Δβ_0⌋. In (3, α] they number at most (1 + ε_K)/Δβ_0 + 1. N_b ≤ 1/Δβ_0 + 1 <
  ⌊1/Δβ_0⌋ + 2. No level equals 3 (def:uc-choice).
- F_1 is the first line of eq:ec-upper, term by term (3T_<, 3T_>, 3T_2 with η_2 − η_1 < ε_+, 4(1/Δτ + 2), r_ιW(N_< + N_>
  + N_b + 3) with eq:uc-t2-w), and it is monotone as stated.
- N_ι is the sum over i of k̄_0 + 1 + J′i. C_lev's constant 529 is the sum in lem:cs-levels (b).
- I_base = 935R_b + 466 + 23,524,832(R_b + 3), and R_base = 22,097 + I_base.
- C_* = eq:cs-c0 written out: 3C_lev gives 6N_ι + 3N̄_Λ + 1,587; 2 · 20,183 + 2 · 1,914 + 22 + 11 = 44,227; 2X_12 =
  8k̄_max + 48.
- D_acc = D_♭ = D_e + 497L_< + L_>C_lev + 935R_b + 466 + C_*.
- D′_*: 20,565,308,337 = 2 + 497 + 23,524,832 + 20,541,783,006, and the recursion telescopes to T_12 +
  Σ_k(step k), split by side.
- D_NM = D_♭ + D′_* + d̄_Φ covers both readings, since D′_* ≥ D_*. Then N_NM, K, d_1, N, k1 and K* follow by
  prop:uc-data-order.
- The coefficients are non-negative (I_lev − 9 > 0), the floors are monotone, and x ↦ (1 + cx)²/x decreases.
- Apart from Major 1, these are all exact.

**Repairs.**

- lem:uc-lambda (c) needs no reality at all. n(λ) = #{λ′ ∈ Λ : Re λ′ < Re λ} (def:iii-i10-1-1) gives n(λ_i) ≤ i − 1 for
  any order of non-decreasing real part.
- In lem:cs-fourier (b) I traced every case.
  - At level 1, α_0 ∈ Λ with Re α_0 ∈ [2, 2 + η_1). A term below 1 + ε_K with i ≥ 1, v1 or μ = 0 needs Re α_0 < 2 + ε_K,
    so Re α_0 = 2 by (G), and then α_0 = 2 by reality at real part 2. Rows with −1 < μ < 0 are excluded by −μ ≥ ε_ind
    > ε_K.
  - At level 2, only the s1 term with i = 0 lies below 1 + ε_K (η_1 > ε_K), with λ = α_0 + 1 and Re λ < 3 + ε_K.
  - The ℕ₀-shifts need only degree 0, by (G) and reality.
  - k̄(2) ≤ k̄(3) holds because n is monotone in the real part.
  - So the proof needs exactly (G) and "elements of Λ of real part 2 are real". P-UB1's prop:is-lambda gives "every
    element of Λ of real part at most 2.514 is real" (its statement in the merged chapter 71).
- No other place in chapter 71 outside sec:is uses that Λ is real (grep). lem:cs-rest Step 2 orders by real part with
  equal real parts independent, which is fine for complex exponents.
- P-UB1 supplies R1–R4 as stated: eq:uc-deltas with 1.6713522747·10⁻¹⁷, N_Λ ≤ 909,507,124,095,312, prop:is-lambda as
  above, and thm:is-gap with (G) ⟺ ε_K < μ_Z, μ_Z < 1.6747859·10⁻¹⁷. R5 is P-I11's.

**Split levels, the new claim.** It is correct.

- c(β_k) is the charge of the step into β_k. lem:cs-levels gives (a) 497 if β_k < 3, a count independent of Λ and N_ι,
  and (b) C_lev if β_k > 3. At most L_< levels lie in (2, 3) and at most L_> in (3, α], and every level lies in one of
  the two. So Σ_k c(β_k) ≤ 497L_< + L_>C_lev. The same bounds hold for c^Ψ and at rotating b.
- In rem:uc-small-reading a step into β_k < 3 costs 2 + 497 + 16 · 1,470,302 + 3 · 6,847,261,002. This is the count of
  lem:uc-small-orders (d), conservative since it keeps the 11 of the background terms. A step into β_k > 3 costs
  2 + C_lev − 11 + I_lev, and ρ_K ≤ T_12 + 2 + C_lev − 11 + I_lev. Unrolling gives exactly M24's bound.
- The places that still charge C_lev unsplit are correct: T_11 and T_12 (top level α > 3) in C_*, and the maximum ρ of
  lem:uc-small-orders (d).

**Sites.** I grepped HEAD's chapters for 1.57157, 3.30029, 3.45745, 4.78156, 5.7624, 1.15248, 2.6193, 5.2386, 1.10009,
5.5005, 6.4368, 1.2587, 4.30775, 6.1038, 1.22077, 2.44153, M_c, 16,747,199, 1,038,326,399, 214,558, 12,811,621,
1.67472, 1.62066, D_acc and thm:uc-integer. Every occurrence lies:

- in a P-UB2 block;
- in a P-UB1 block (rem:gap-sums, sec:is, def:uc-choice, lem:uc-admissible, thm:is-gap, prop:is-count, rem:is-summary);
- or in a sentence that stays true (thm:loss-d's "(G) asks ε_K < μ_G", cor:uc-two-offsets, rem:ec-other-losses in the
  main set, 03:363–366 in the main set).

After the merge with P-UB1, chapter 71 has no M_c, no K̄, no stale μ_G-based (G) statement and no ε_K = 1.6416·10⁻¹⁴
admissibility claim. Outside chapters/, P-TR.md, STATUS.md, INTEGRATION.md and PAPER.md remain stale, as the file says.

**Fallback.**

- The lower bounds are kept: d > 1.2497·10²⁴ (F1, FO1–FO3, FO5), K > 22d > 2.7493·10²⁵ (F2, F7, F8), and
  K* > 1.0078·10⁵¹ (F7, F8, by prop:uc-data-order (c)'s lower formula and (4/3)(2.74934·10²⁵)² > 7.5588·10⁵⁰).
- None of 1.57157·10⁵⁰, 3.30029·10⁵¹, 3.45745·10⁵¹ or 4.78156·10¹⁰³ survives the fallback merge.
- What does survive is in the rule-kept blocks of Major 2.
