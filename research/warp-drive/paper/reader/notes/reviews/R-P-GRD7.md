# R-P-GRD7: review of proofs/P-GRD7.md (sec:tl5-hfx, "The first-order constant, counted over the words")

File reviewed: research/warp-drive/paper/reader/proofs/P-GRD7.md, md5 3f06af9236ed18210ebb41f562df20be, 87 lines, at
3d367b13 (= HEAD of ccr-af9edcf6-9a60sz). Chapter: chapters/87-ten-l5.md, 6297 lines, md5 c41fdded…, last changed by
cf314394 (sec:tl5-hfw merged), identical at a3d0c091, as the Placement says. "87:n" is a chapter line, "P:n" a line
of the file.

Fixed copy: scratchpad/reader/rpgrd7/P-GRD7.fixed.md, md5 31812b4ddaf9be2fc261e43014801aa3, 96 lines, made by
scratchpad/reader/rpgrd7/tools/fix.py (6 replacements, each found exactly once; crosswalk @PENDING numbers recomputed).

## 1. Mechanics (both the file as submitted and the fixed copy)

Scratch merge into a fresh `git archive HEAD` tree with the writer's placement (item 2 found once at 87:6296-6297; it
replaces two lines by two, so line 6297 stays the last line, as item 1 says):

| check | P-GRD7.md | P-GRD7.fixed.md |
|---|---|---|
| lint.py --chapters | 62 files, 5250 labels (5245 + 5), 0 hits | same, 0 hits |
| assemble.py --check | 0 problems | 0 problems |
| in-memory check | `[] 0` | `[] 0` |
| lines over 121 / forbidden wrapped starts | none outside the crosswalk rows / none | none / none |
| crosswalk rows: label at the stated line | 5 of 5 | 5 of 5 (lines 1, 9, 14, 33, 40) |
| chapter labels = crosswalk + new rows | 399 = 399 | 399 = 399 |
| printed numbers of the 5245 existing labels | 0 changed | 0 changed |

## 2. The five checks asked for

### 2.1 The distinctness argument: correct

For fixed B, J ↦ JB is injective on the 43 words J of rotations with |J| ≤ 2 (1 + 6 + 36): words are formal
sequences, concatenation with a fixed suffix B is injective (different lengths give different lengths, equal lengths
keep the different prefix). (K₁K₂, K₂K₁) and (K, K) are distinct words, and 𝒥_g sums over formal words of Γ, as the
counts 7^j and 𝔐 = Σ 7^j (87:4323, eq:tl5-hfg-cinf) show; the rotations are in Γ, |JB| ≤ |B| + 2 ≤ N − 1, and
μ^(|B|+3) ≤ μ^(|JB|). So Σ_J μ^(|B|+3)|D̂Ψ_(JB)|² ≤ 𝒥_g². The zeroth-order step of the chapter uses the same fact
(87:4343-4345). What is not distinct is correctly not counted once: the remainders R′_J reuse the Ψ_C for different J
and are counted with their multiplicities 6 and 36 in ϖ′.

### 2.2 Why 43 stays on k₁^μ: correct as stated

D̂²Ψ_(JB) is bounded per word by eq:tl5-hfs-m2 (or eq:tl5-hfq-m2, or M_g of lem:tl5-hft-small (b)), each with the whole
𝒥_g on the right, so the ℓ² sum over the 43 words gives 43^(1/2) times the maximum. The deduced comment in the Comparison
is right that the nonlinear part of the recovery (k₃𝔰 ≤ 1/4 per word, with M_g the maximum over all shorter words) does
not sum in ℓ². Observation, no finding: the leading term of the recovery, (Σ_Z |D̂Ψ_(ZJB)|²)^(1/2), would count once
(the words ZJB are distinct for distinct (Z, J)); what blocks an ℓ² recovery is the couplings 𝔄 (sums over the words of
lower length, repeated across J) and the nonlinear part.

### 2.3 The formula's factors: correct

- eq:tl5-hf-cs-r with r = 3 (87, lem:tl5-hf-sobolev): 6C_(S³)²𝔭₃𝔴⁶(… 𝔳⁶R⁻³((1 + 2r²|D̂∂_γ|²)|ℒ^J A|² + 2|∂_γ|²|D̂ℒ^J A|²)
  …): 18 = 2·3²; the intrinsic reading is 6C_(E,3)², 𝔳₀, 𝔴₀ (lem:tl5-hft-face (a), and 87:5845: "258 C_(E,3)² in place of
  258 C_(S³)² 𝔭₃ in C₁"). So 6C²𝔴⁶𝔳⁶ is right in both readings, and 258 = 6·43 is the old count.
- ρ′: lem:tl5-hfs-quadratic (a) gives 2C(k, j) monomials with a factor carrying j letters (2 for |J| = 1; 4 and 2 for
  |J| = 2), each with one Ψ_C, |C| = |JB| − a; Λ_a bounds the coefficients and their D̂ (def:tl5-hfg-graded). With
  μ^(|B|+3) ≤ μ^(1+a)μ^(|C|): ρ′₁ = 2μΛ₁, ρ′₂ = 4μΛ₁ + 2μ^(3/2)Λ₂, and √2 for D̂R′_J from |Ψ_C| + |D̂Ψ_C| ≤ √2(…)^(1/2).
  Consistent with Λ₂^μ = max(μΛ₁, μ^(3/2)Λ₂) of the old count (87:5469-5470, 5578-5581). (Observation: for |J| = 1, |C| =
  |B| exactly, so ρ′₁ could be 2μ^(3/2)Λ₁; 2μΛ₁ is valid.)
- Minkowski over the words: (Σ_J …|ℒ^J A|²)^(1/2) ≤ (1 + ϖ′^(1/2))𝒥_g and (Σ_J …|D̂ℒ^J A|²)^(1/2) ≤ 43^(1/2)·2(k₁^μ + 1)𝒥_g
  + (2ϖ′)^(1/2)𝒥_g + 43^(1/2)·(part with ϱ). Splitting the 𝒥_g part from the ϱ part by (x + y)² ≤ 2x² + 2y² gives
  2|∂_γ|²·2X² = 4|∂_γ|²(2·43^(1/2)(k₁^μ + 1) + (2ϖ′)^(1/2))², the second line of the display, with 2(43^(1/2))² = 2·43 for
  the part with ϱ against 4·43 in the old split (87:4347-4353, C_(1,ϱ) with 32 = 2·4·4): keeping the old C_(1,ϱ) is valid.
  The η₀ part on S_a is a maximum (η₀ is a sup over N₀), so its 43 stays, as kept.
- The weighted forms: lem:tl5-hfs-linfty (87:5578-5583), lem:tl5-hft-small (a) unweighted (87:5869-5872), (b) and
  lem:tl5-hfq-theta (ϱ part with ν) all have this structure; "keep the parts with ϱ and η₀ as there" covers the ϱ part
  unweighted in (a) and with ν in hfq-theta, but the proof does not say how the 𝒥_g and ϱ parts are separated (n2).

### 2.4 C₁^x ≤ C₁^♮: false in general (finding m1)

The lemma replaces C₁^♮ outright, so thm:tl5-hfx contains thm:tl5-hfw only if C₁^x ≤ C₁^♮. Term by term, with
x := k₁^μ + 1 and Λ := Λ₂^μ (ρ′₁ ≤ 2Λ, ρ′₂ ≤ 6Λ, so ϖ′ ≤ 1320Λ², with equality when μΛ₁ = μ^(3/2)Λ₂):
- (1 + ϖ′^(1/2))² ≤ (1 + 36.4Λ)² ≤ 43(1 + 6Λ)² = (6.56 + 39.3Λ)²: always.
- (2·43^(1/2)x + (2ϖ′)^(1/2))² = 172x² + 4·43^(1/2)x(2ϖ′)^(1/2) + 2ϖ′ ≤ 172x² + 1347.7xΛ + 2640Λ², against 43(8x² + 72Λ²) =
  344x² + 3096Λ²: holds when 456t² − 1347.7t + 172 ≥ 0, t = Λ/x, i.e. t ≤ 0.134 or t ≥ 2.82, so in particular when
  8Λ₂^μ ≤ k₁^μ + 1; it fails for 0.134 < t < 2.82 through the cross term, which has no counterpart in C₁^♮.
Example: μ = 1, Λ₁ = Λ₂ = 2, k₁^μ + 1 = 8, |∂_γ| = 1, D̂∂_γ = 0: C₁^x = 1.108 C₁^♮. A random sample of 300,000 points
(μ ∈ [10⁻⁶, 1], Λ₁ ≤ Λ₂, x ∈ [1, 100], |∂_γ|, |D̂∂_γ| ∈ [10⁻², 10²]) gave C₁^x/C₁^♮ up to 1.16, and no case above 1 with
8Λ₂^μ ≤ k₁^μ + 1. At the evaluation's values (G0e: Λ₂^μ ≤ 4 × 10⁻³, k₁^μ = 7-16) the new number is the smaller, by
√2 when the k₁ part dominates. The earlier closing conditions themselves stay valid (nothing earlier is edited), but
the remark and the Comparison present C₁^x as a sharpening without the cross term. Fix: take the smaller of the two,
as both bounds hold with the same parts with ϱ and η₀ (the same device as the confirmed m1 of R-P-GRD5).

### 2.5 Every place C₁^♮ is replaced: covered, one statement incomplete (n1); the Comparison's level 6 is wrong (m2)

C₁^♮ enters (87:5547-5550, 5872, 5876, 6194-6199): C_(∞,μ)^(m) (so C_P^♮ = C_(∞,μ)^(1) at N ≥ 6, and C_(∞,μ)^(N−4)
in 𝔰_*), and at N = 4 C_P^v = 2max(2C_S, C₁, 𝔨_rec) directly and through 𝔨_rec. Through C_P it enters 𝔎 and 𝔞_(·,s),
hence S_F^v; it does not enter C_(1,ϱ), C_(1,0)^♮, 𝔎_ϱ, 𝔎₀, 𝔯^v, 𝔰₁^v, the level-four mixed constants 𝔛, 𝔜, or the
graded C₁^g of sec:tl5-hfg. Every use is through the bounds of lem:tl5-hfs-linfty, lem:tl5-hft-small and
lem:tl5-hfq-theta (lem:tl5-hfv-rec's μ²|D̂Ψ_Z| ≤ C₁ℰ^(1/2) + … is the first-order bound with B = Z), so the
theorem's proof is right. Two statements are not:
- thm:tl5-hfx says "in C_P^v (through 𝔨_rec)": at N = 4 C₁ is also a direct entry of C_P^v, and at N ≥ 6 C_P^v has no
  𝔨_rec; "the constants of level four" is vague. n1.
- The Comparison ends "Level 6: not changed", while C₁^x enters C_P^v = C_(∞,μ)^(1) and C_(∞,μ)^(2) of 𝔰_*^w at N = 6,
  and the chapter text says the section applies at every N ≥ 4. The evaluation reads this line. m2.

## 3. Findings

### Major

None.

### minor

**m1. C₁^x can exceed C₁^♮ (lem:tl5-hfx-c1 P:9-14, the proof's end P:27-30, rem:tl5-hfx-what P:39-42; Comparison
P:68-71).** Why: §2.4. Replacements (all in the fixed copy):

Old (P:9-14):

    **Lemma {#lem:tl5-hfx-c1}** (The first-order constant.) Let ρ′₁ := 2μΛ₁, ρ′₂ := 4μΛ₁ + 2μ^(3/2)Λ₂ and ϖ′ := 6ρ′₁² +
    36ρ′₂², and let C₁^x be C₁^♮ with (1 + ϖ′^(1/2))²/43 in place of (1 + 6Λ₂^μ)² and with (2(43)^(1/2)(k₁^μ + 1) +
    (2ϖ′)^(1/2))²/43 in place of 72(Λ₂^μ)² + 8(k₁^μ + 1)²:

        C₁^x² = 6 C² 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))²
                + 4|∂_γ|² (2(43)^(1/2) (k₁^μ + 1) + (2ϖ′)^(1/2))²),                                          {#eq:tl5-hfx-c1}

New:

    **Lemma {#lem:tl5-hfx-c1}** (The first-order constant.) Let ρ′₁ := 2μΛ₁, ρ′₂ := 4μΛ₁ + 2μ^(3/2)Λ₂ and ϖ′ := 6ρ′₁² +
    36ρ′₂², and let C₁^x be the smaller of C₁^♮ and the number formed as C₁^♮ with (1 + ϖ′^(1/2))²/43 in place of
    (1 + 6Λ₂^μ)² and with (2(43)^(1/2)(k₁^μ + 1) + (2ϖ′)^(1/2))²/43 in place of 72(Λ₂^μ)² + 8(k₁^μ + 1)²:

        C₁^x² = min(C₁^♮², 6 C² 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))²
                + 4|∂_γ|² (2(43)^(1/2) (k₁^μ + 1) + (2ϖ′)^(1/2))²)),                                        {#eq:tl5-hfx-c1}

Old (P:27-30):

    Sobolev inequality [[eq:tl5-hf-cs-r]] (or that of [[lem:tl5-hft-face]]) with r = 3, insert these bounds in place of
    the bounds of the 43 words by 𝒥 used in the proof of [[lem:tl5-hf-linfty]], keep the parts with ϱ and η₀ as there, and
    use ∫ 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g; this gives the part with ℰ_g of the bound with C₁^x, the parts with ϱ and η₀
    being those of that proof. ∎

New (also n2: the split of the 𝒥_g and ϱ parts, and why the old ϱ part may be kept):

    Sobolev inequality [[eq:tl5-hf-cs-r]] (or that of [[lem:tl5-hft-face]]) with r = 3, insert these bounds in place of
    the bounds of the 43 words by 𝒥 used in the proof of [[lem:tl5-hf-linfty]], separate the parts with 𝒥_g from those with
    ϱ by (x + y)² ≤ 2x² + 2y² as there, and use ∫ 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g; this gives the part with ℰ_g of the
    bound with the second entry of [[eq:tl5-hfx-c1]], and parts with ϱ and η₀ at most those of that proof, the part with ϱ
    being half of it. The bound with C₁^♮ holds as well, with the same parts with ϱ and η₀; so it holds with C₁^x. ∎

Old (P:39-42):

    **Remark {#rem:tl5-hfx-what}** (What changes.) In C₁^x the count 43 remains only with the recovery constant k₁^μ, and
    its coefficient there is 4 · 43 · 4 against 4 · 43 · 8 in C₁^♮; the terms without k₁^μ carry (1 + ϖ′^(1/2))² against
    43(1 + 6Λ₂^μ)². As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfx]] are established in this
    paper for no background at 10 l5.

New:

    **Remark {#rem:tl5-hfx-what}** (What changes.) In the second entry of [[eq:tl5-hfx-c1]] the count 43 remains only with
    the recovery constant k₁^μ, whose coefficient is 4 · 43 · 4 against 4 · 43 · 8 in C₁^♮; the terms without k₁^μ carry
    (1 + ϖ′^(1/2))² and 4|∂_γ|² · 2ϖ′ against 43(1 + 6Λ₂^μ)² and 4|∂_γ|² · 43 · 72(Λ₂^μ)², and the cross term
    4|∂_γ|² · 4 · 43^(1/2)(k₁^μ + 1)(2ϖ′)^(1/2) has no counterpart. As ϖ′ ≤ 1320(Λ₂^μ)², the second entry is the smaller if
    8Λ₂^μ ≤ k₁^μ + 1 on Σ₁(a, b); otherwise the cross term can make it the larger, and the minimum keeps C₁^x ≤ C₁^♮. As
    for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfx]] are established in this paper for no
    background at 10 l5.

Old (Comparison, P:68-71, through "What blocks more (deduced): the"):

    Not chapter text. The one new factor is C₁^x (eq:tl5-hfx-c1), used everywhere C₁^♮ (or C₁^E) was: 𝔎, 𝔨_rec of C_P^v,
    C_(∞,μ)^(N−4) in 𝔰_*, and the level-four constants. ρ′₁ = 2μΛ₁, ρ′₂ = 4μΛ₁ + 2μ^(3/2)Λ₂, ϖ′ = 6ρ′₁² + 36ρ′₂².
    Against C₁^♮: the k₁ part loses a factor 2 under the root (0.15 decades of C₁ when it dominates), the other part
    43(1 + 6Λ₂^μ)² → (1 + ϖ′^(1/2))², up to 1.6 decades of its square when ϖ′ is small. What blocks more (deduced): the

New:

    Not chapter text. The one new factor is C₁^x (eq:tl5-hfx-c1), used everywhere C₁^♮ (or C₁^E) was: C_P^v (directly,
    and at level four through 𝔨_rec), hence 𝔎 and S_F^v, and C_(∞,μ)^(N−4) in 𝔰_*, at level four and at N ≥ 6 alike.
    ρ′₁ = 2μΛ₁, ρ′₂ = 4μΛ₁ + 2μ^(3/2)Λ₂, ϖ′ = 6ρ′₁² + 36ρ′₂² ≤ 1320(Λ₂^μ)². Against C₁^♮, in the second entry of the
    minimum: the k₁ part loses a factor 2 under the root (0.15 decades of C₁ when it dominates), the part without k₁ and
    ∂_γ, 43(1 + 6Λ₂^μ)² → (1 + ϖ′^(1/2))², up to 1.6 decades of its square when ϖ′ is small, and the cross term
    4|∂_γ|² · 4 · 43^(1/2)(k₁^μ + 1)(2ϖ′)^(1/2) is new. The second entry is the smaller where 8Λ₂^μ ≤ k₁^μ + 1, so at G0e's
    Λ₂^μ ≤ 4 × 10⁻³ with k₁^μ = 7–16; at μ = 1, Λ₁ = Λ₂ = 2, k₁^μ + 1 = 8, |∂_γ| = 1, D̂∂_γ = 0 it is 11 % above C₁^♮,
    hence the minimum. What blocks more (deduced): the

**m2. Comparison, level 6 (P:74).** Why: §2.5. Old: "… the reasons given with P-GRD5. Level 6: not changed." New:

    in ℓ²; the rank 3, 𝔨₂ and the (E₁, E₁) component remain for the reasons given with P-GRD5. Level 6: C₁^x enters there
    as well (C_P^v = C_(∞,μ)^(1), and C_(∞,μ)^(2) in 𝔰_*^w); its effect there is not evaluated here.

### nits

**n1. thm:tl5-hfx (P:33-34), chapter text.** Old: "… in particular in 𝔎, / in C_P^v (through 𝔨_rec), in C_(∞,μ)^(N−4)
of 𝔰_*^w and in the constants of level four." New:

    [[thm:tl5-hfw]] hold under its hypotheses with every constant formed with C₁^x in place of C₁^♮, in particular in C_P^v
    (directly, and at level four also through 𝔨_rec), hence in 𝔎 and S_F^v, and in C_(∞,μ)^(N−4) of 𝔰_*^w.

**n2. The proof's last sentence (P:27-30).** It does not say how the parts with 𝒥_g and with ϱ are separated, nor why
the old part with ϱ may be kept; the new split gives half of it. Replacement given under m1.

Crosswalk rows in the fixed copy (only line numbers change): sec 1, lem 9, eq:tl5-hfx-c1 14, thm 33, rem 40.

## 4. Checked and correct, no change

The distinctness argument; ρ′₁, ρ′₂, ϖ′, √2 for D̂R′_J; Minkowski over the words; the factors 6, 18, 4, 2·43^(1/2),
(2ϖ′)^(1/2) and both Sobolev readings; the coefficient 4·43·4 against 4·43·8; "0.15 decades" (log₁₀√2) and "up to 1.6
decades" (log₁₀43); the theorem's proof (every use of C₁^♮ is through the three lemmas); the Placement and its commits
(a3d0c091 = HEAD for the chapter, cf314394 the merge of sec:tl5-hfw).

## 5. Verdict

The counting argument is right, and at the evaluation's values the new constant is the smaller (by √2 when the k₁ part
dominates). Two minor findings are open: the new number can exceed C₁^♮ through the cross term when 8Λ₂^μ > k₁^μ + 1
(fixed by the minimum, which both proofs support), and the Comparison's "Level 6: not changed". With the six
replacements above, all tested in the fixed copy (lint 0 hits, assemble --check 0 problems, in-memory `[] 0`, crosswalk
399 = 399, no printed number changed), nothing else is open.

Verdict: NOT CONFIRMED
