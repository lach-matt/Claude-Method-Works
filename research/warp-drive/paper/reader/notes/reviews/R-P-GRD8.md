# R-P-GRD8: review of proofs/P-GRD8.md (sec:tl5-hfy, "The absorption with the bootstrap's smallness")

File reviewed: research/warp-drive/paper/reader/proofs/P-GRD8.md, md5 80431453d47edfc402d894dae2c78615, 83 lines, at
c0543b1e (= HEAD). Chapter: chapters/87-ten-l5.md, 6344 lines, md5 fda8b8aa…, last changed by 2500bc7f (sec:tl5-hfx
merged), identical at 11a31701, as the Placement says. "87:n" is a chapter line, "P:n" a line of the file.

Fixed copy: scratchpad/reader/rpgrd8/P-GRD8.fixed.md, md5 742cd674ea21447e282a24978464ea07, 96 lines, made by
scratchpad/reader/rpgrd8/tools/fix.py (6 replacements, each found exactly once; crosswalk @PENDING numbers recomputed).

## 1. Mechanics (both the file as submitted and the fixed copy)

Scratch merge into a fresh `git archive HEAD` tree with the writer's placement (item 2 found once at 87:6343-6344; two
lines by two, so 6344 stays the last line):

| check | P-GRD8.md | P-GRD8.fixed.md |
|---|---|---|
| lint.py --chapters | 62 files, 5254 labels (5250 + 4), 0 hits | same, 0 hits |
| assemble.py --check | 0 problems | 0 problems |
| in-memory check | `[] 0` | `[] 0` |
| lines over 121 / forbidden wrapped starts | none outside the crosswalk rows / none | none / none |
| crosswalk rows: label at the stated line | 4 of 4 | 4 of 4 (lines 1, 10, 32, 43) |
| chapter labels = crosswalk + new rows | 403 = 403 | 403 = 403 |
| printed numbers of the 5250 existing labels | 0 changed | 0 changed |

## 2. The four checks asked for

### 2.1 The continuity argument: legitimate, no circularity

Old Step 1 (87:4468-4475): Σ_* = {σ : 𝔰 ≤ 𝔰₀ on D^κ_σ}, and the gap 𝔰_* < 𝔰₁ ≤ 𝔰₀/2 opens it. Nothing there needs
the factor 1/2 between 𝔰₁ and 𝔰₀: openness needs only a strict gap between the bound 𝔰_* and the hypothesis. With
Σ_* = {σ : 𝔰 ≤ 𝔰₁^v on D^κ_σ}:
- **start**: D^κ_(1/2) = S ⊂ N₀ and 𝔰 ≤ η₀ < 𝔰₁^v on N₀ ∩ D^κ_s (87:4466, hypothesis (a));
- **closed**: 𝔰 is continuous and the D^κ_σ increase;
- **open**: for p ∈ D^κ_σ, Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ, so 𝔰 ≤ 𝔰₁^v on it and the bounds at p hold with k₃𝔰 ≤ 𝔵; with
  ℰ(p) ≤ e^(φ(p)) Y_σ² ≤ 4e^(φ(p))A² they give 𝔰(p) ≤ 𝔰_* < 𝔰₁^v uniformly, so a neighbourhood of D^κ_σ, containing some
  D^κ_(σ′), has 𝔰 < 𝔰₁^v;
- 𝔰₁^v ≤ 𝔰₀/2 also keeps everything else the old hypothesis 𝔰 ≤ 𝔰₀ gave: 𝔰 ≤ 𝔰_♭ (the expansions with 𝔠^♮), |H| ≤ 1/8
  (the factor 6/5 of the recovery), 𝔰 ≤ 1 (the powers 𝔰^(q−2)), |h| < c_*κ_m/2 and θ_H ≤ ϑ after Step 1.
- **No circularity**: 𝔵 = 𝔰₁^v sup k₃ is a background number (𝔰₁^v = min(𝔰₀/2, c_*κ_m/2, 𝔰_(θ,v)), k₃ from 𝔠^♮ and the
  𝔔); the replaced C_∞, C_P are then fixed, A from the data and ε, and 𝔰_* from these. The conclusion 𝔰 ≤ 𝔰_* on D^κ_s
  holds at every point Steps 2 and 3 use.
The theorem's proof leaves Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ unsaid (n1).

### 2.2 Each replacement: correct, and no non-absorption 2 replaced

- M ≤ k₁𝒥 + k₂ϱ + k₃𝔰(2𝒥 + M) (87:4336-4339; the 2 in 2𝒥 is 𝔧 ≤ 2𝒥₁ + M₂ from |H| ≤ 2|h|, kept): k₃𝔰 ≤ 𝔵 gives
  M ≤ ((k₁ + 2𝔵)𝒥 + k₂ϱ)/(1 − 𝔵), against 2(k₁ + 1)𝒥 + 2k₂ϱ at k₃𝔰 ≤ 1/2. In the induction of eq:tl5-hfs-m2 (87:5563-5573)
  R := ((k₁ + 2𝔵)X + k₂ϱ)/(1 − 𝔵) satisfies k₁X + k₂ϱ + 𝔵(2X + R) = R exactly; in eq:tl5-hfq-m2 (87:6034-6043) the parts
  with 𝒥_g (k₃^♮(μ)) and with ϱ (k₃^♮(ν)) close separately with the same coefficients, as k₃^♮(μ) ≤ k₃^♮(ν).
- Bounds at a point: the nonlinear term of D̂²Ψ_B is at most k₃𝔰(p)² (87:5875, hft-small (a)) or k₃𝔰(p)𝔰_g(p)
  (hft-small (b), lem:tl5-hfs-linfty, lem:tl5-hfv-rec), so 𝔰 ≤ max + 𝔵𝔰 and the outer 2 of C_∞^(m), C_(∞,ϱ)^(m),
  C_(∞,0)^(m) (87:5139-5141), of their weighted forms and of C_P^v, C_(P,ϱ)^v, C_(P,0)^v (87:6199-6200) becomes 1/(1 − 𝔵).
  The t-argument of eq:tl5-hfq-small (87:6055-6057): t ≤ 1 + 𝔵t, t ≤ 1/(1 − 𝔵), matching the outer factor.
- Not replaced, correctly: the inner 2C_S and 2C_(0,0) (|H| ≤ 2|h|), (2𝔐)^(1/2) (|Ψ|² + |D̂Ψ|²), the k₂ of C_(∞,ϱ) and of
  𝔨_rec^ϱ + k₂ (the recovery's linear residual term), and the 4|∂_γ|² of C₁^x (the split of the 𝒥_g and ϱ parts). The
  C₁^x replacement 2·43^(1/2)(k₁^μ + 1) → 43^(1/2)(k₁^μ + 2𝔵)/(1 − 𝔵) replaces the absorption's 2 only.

### 2.3 𝔵 ≤ 1/4 in every case: correct; the earlier theorems are contained

Option (a): 𝔰₁^t = 𝔰₁^♮ ≤ 𝔰₀^♮/2 = min(𝔰_♭, 1/(2 sup k₃^♮))/2 (87:5652); option (b): 𝔰₀^μ with k₃^♮(μ) (87:5912); level
four: 𝔰₀^q with k₃^♮(ν) (87:6087). So 𝔵 ≤ 1/4. With 𝔵 ≤ 1/4: (k₁ + 2𝔵)/(1 − 𝔵) ≤ 2(k₁ + 1) (equivalent to
k₁(1 − 2𝔵) + 2 − 4𝔵 ≥ 0), k₂/(1 − 𝔵) ≤ 2k₂, 1/(1 − 𝔵) ≤ 2; old/new ≥ 2(1 − 𝔵) ≥ 3/2 for each. Every constant is monotone
in them, so 𝔰_*, S_F and A only fall and the hypotheses of thm:tl5-hfx imply those of thm:tl5-hfy. Nothing earlier is
edited except the appended pointer sentence.

### 2.4 Every occurrence: not covered as stated (finding m1); one false scope claim (also m1)

The replaced bounds (eq:tl5-hfs-m2, eq:tl5-hfq-m2, M_g^(j)) enter, besides 𝔨_A, λ_t^μ and C₁^x which the lemma names:
- λ_t^(μ,2) := 2([k₁^(2,μ)]_t + 1) of lem:tl5-hfq-mixed (87:6067, from M_g^(2), in 𝔜^q_(1,t));
- ς_t := 2[k₂]_t(…)^(1/2) (87:4762; ‖M_g‖_Σ ≤ λ𝔍_g + ς_tϱ, in 𝔛′_(2,t), 𝔜′_(1,t), hence 𝔯_M and ε_M);
- C_(1,ϱ), whose 32k₂² = 8(2k₂)² comes from the ϱ part of M₂ (87:4327-4328, 4349-4353);
- the terms with ϱ of the products, 2k₂𝔰ϱ (87:5597-5608, 5898-5902, 6059-6063), hence the 2𝔰₁^v of ε^w (87:6287).
Leaving these at the old factor is valid (the old bounds are larger), so the theorem is not wrong, but the lemma states
"hence in 𝔨_A, λ_t^μ and C₁^x" and the Comparison "Replaced everywhere". The ε^w coefficient falls to 𝔰₁^v/(1 − 𝔵), a
further factor ≥ 3/2 on the ϱ coefficient, which the evaluation should have.

Also, the lemma says that lem:tl5-hfs-linfty, lem:tl5-hft-small, lem:tl5-hfq-theta, lem:tl5-hfv-rec and
lem:tl5-hfx-c1 hold with the replacements whenever 𝔰 ≤ 𝔰₁^v. Under option (b) and at level four, 𝔵 is formed with
k₃^♮(μ) or k₃^♮(ν) ≤ k₃^♮, and 𝔰₁^v need not be below 𝔰₀^♮ = min(𝔰_♭, 1/(2 sup k₃^♮)); then lem:tl5-hfs-linfty (whose
absorptions use k₃^♮) is not available, as the chapter itself avoids it there ("in place of [[lem:tl5-hfs-linfty]]",
87:5932). And 𝔨_A, λ_t^μ belong to lem:tl5-hfs-products and lem:tl5-hfs-mixed, which the list omits. The theorem uses
only the lemmas of the chosen set, so it is right; the lemma's scope is not.

## 3. Findings

### Major

None.

### minor

**m1. lem:tl5-hfy-abs (P:12-17) and thm:tl5-hfy (P:27): scope and coverage.** Why: §2.4. Replacements (fixed copy):

Old (P:12-17, from "level four), 𝔰₁^v as in"):

    level four), 𝔰₁^v as in [[def:tl5-hfv-constants]] and 𝔵 := 𝔰₁^v sup_(D^κ) k₃, so 𝔵 ≤ 1/4 as 𝔰₁^v ≤ 𝔰₀/2. If 𝔰 ≤ 𝔰₁^v on
    Q(a, b), then [[lem:tl5-hfs-linfty]], [[lem:tl5-hft-small]], [[lem:tl5-hfq-theta]], [[lem:tl5-hfv-rec]] and
    [[lem:tl5-hfx-c1]] hold with the following replacements: 2(k₁^(j,·) + 1) by (k₁^(j,·) + 2𝔵)/(1 − 𝔵) and 2k₂ by k₂/(1 − 𝔵)
    in [[eq:tl5-hfs-m2]], [[eq:tl5-hfq-m2]] and the bounds of M_g^(j), and hence in 𝔨_A, λ_t^μ and C₁^x (where
    2(43)^(1/2)(k₁^μ + 1) becomes (43)^(1/2)(k₁^μ + 2𝔵)/(1 − 𝔵)); and the factor 2 in front of the maxima defining
    C_∞^(m), C_(∞,ϱ)^(m), C_(∞,0)^(m), their weighted forms, C_P^v, C_(P,ϱ)^v and C_(P,0)^v by 1/(1 − 𝔵).

New:

    level four), 𝔰₁^v as in [[def:tl5-hfv-constants]] and 𝔵 := 𝔰₁^v sup_(D^κ) k₃, so 𝔵 ≤ 1/4 as 𝔰₁^v ≤ 𝔰₀/2. If 𝔰 ≤ 𝔰₁^v on
    Q(a, b), then the lemmas that the chosen set uses hold with the replacements below: [[lem:tl5-hfs-linfty]],
    [[lem:tl5-hft-small]] (a) and [[lem:tl5-hfs-products]] for option (a); [[lem:tl5-hft-small]] (b) and
    [[lem:tl5-hft-products]] for option (b); these, [[lem:tl5-hfq-theta]], [[lem:tl5-hfs-mixed]] and [[lem:tl5-hfq-mixed]]
    at level four; and [[lem:tl5-hfv-rec]] and [[lem:tl5-hfx-c1]]. The replacements are 2(k₁^(j,·) + 1) by
    (k₁^(j,·) + 2𝔵)/(1 − 𝔵) and 2k₂ by k₂/(1 − 𝔵) in [[eq:tl5-hfs-m2]], [[eq:tl5-hfq-m2]] and the bounds of M_g^(j), and
    hence wherever these bounds enter: in 𝔨_A, λ_t^μ and λ_t^(μ,2); in C₁^x, where 2(43)^(1/2)(k₁^μ + 1) becomes
    (43)^(1/2)(k₁^μ + 2𝔵)/(1 − 𝔵); in ς_t, 2[k₂]_t by [k₂]_t/(1 − 𝔵); in C_(1,ϱ), 32k₂² by 8k₂²/(1 − 𝔵)²; and in the terms
    with ϱ of the products, 2k₂ 𝔰 ϱ by k₂ 𝔰 ϱ/(1 − 𝔵); and the factor 2 in front of the maxima defining C_∞^(m),
    C_(∞,ϱ)^(m), C_(∞,0)^(m), their weighted forms, C_P^v, C_(P,ϱ)^v and C_(P,0)^v by 1/(1 − 𝔵).

Old (P:27): "[[thm:tl5-hfx]] hold under its hypotheses with every constant formed with the replacements of
[[lem:tl5-hfy-abs]]." New:

    [[thm:tl5-hfx]] hold under its hypotheses with every constant formed with the replacements of [[lem:tl5-hfy-abs]], and
    with 𝔰₁^v/(1 − 𝔵) in place of 2𝔰₁^v in ε^w.

and in the theorem's proof (P:30-33, with n1), old:

    N₀, and it is closed. For σ ∈ Σ_*, [[lem:tl5-hfy-abs]] applies at every p ∈ D^κ_σ and gives 𝔰(p) ≤ 𝔰_* < 𝔰₁^v, 𝔰_* formed
    with the replaced constants; by the uniform continuity of 𝔰, Σ_* is open in [1/2, s], so Σ_* = [1/2, s]. Steps 2 and 3
    then use the bounds of [[lem:tl5-hfy-abs]] in place of those they replace, and the rest of the proof of [[thm:tl5-hfx]]
    holds as written. ∎

new:

    N₀, and it is closed. For σ ∈ Σ_* and p ∈ D^κ_σ, Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ, so [[lem:tl5-hfy-abs]] applies at p and
    gives 𝔰(p) ≤ 𝔰_* < 𝔰₁^v, 𝔰_* formed with the replaced constants; by the uniform continuity of 𝔰, Σ_* is open in
    [1/2, s], so Σ_* = [1/2, s]. Steps 2 and 3 then use the bounds of [[lem:tl5-hfy-abs]] in place of those they replace; in
    the terms with ϱ of Step 2, k₂ 𝔰 ϱ/(1 − 𝔵) ≤ 𝔰₁^v k₂ ϱ/(1 − 𝔵) gives ε^w with 𝔰₁^v/(1 − 𝔵) in place of 2𝔰₁^v. The
    rest of the proof of [[thm:tl5-hfx]] holds as written. ∎

and the remark (P:35-38), old:

    **Remark {#rem:tl5-hfy-what}** (What changes.) With 𝔵 small the recovery constant 2(k₁^μ + 1) becomes nearly k₁^μ, and
    the maxima of the constants C_∞ and C_P lose their factor 2; at 𝔵 = 1/4 the replacements are (4/3)(k₁^μ + 1/2) and 4/3.
    As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfy]] are established in this paper for no
    background at 10 l5.

new:

    **Remark {#rem:tl5-hfy-what}** (What changes.) With 𝔵 small the recovery constant 2(k₁^μ + 1) becomes nearly k₁^μ, 2k₂
    nearly k₂, and the maxima of the constants C_∞ and C_P lose their factor 2; at 𝔵 = 1/4 the replacements are
    (4/3)(k₁^μ + 1/2), (4/3)k₂ and 4/3; for every 𝔵 each new factor is at least 2(1 − 𝔵) times smaller than the one it
    replaces. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfy]] are established in this paper
    for no background at 10 l5.

**m2. The lemma's proof (P:19-24, chapter text): "the smallness is used only through k₃𝔰 ≤ 1/2".** Why: §2.1; it is also
used through 𝔰 ≤ 𝔰_♭, |H| ≤ 1/8 and 𝔰 ≤ 1, which 𝔰₁^v ≤ 𝔰₀/2 keeps, and at level four the absorptions carry k₃^♮(μ) as
well as k₃^♮(ν). Old (P:19-24):

    *Proof.* In each of these proofs the smallness is used only through k₃ 𝔰 ≤ 1/2 in an absorption; with 𝔰 ≤ 𝔰₁^v, k₃ 𝔰 ≤
    𝔵. In the bound of the second derivatives, M ≤ k₁ 𝒥 + k₂ ϱ + 𝔵 (2𝒥 + M) gives M ≤ ((k₁ + 2𝔵) 𝒥 + k₂ ϱ)/(1 − 𝔵), and in
    the inductions of [[eq:tl5-hfs-m2]] and [[eq:tl5-hfq-m2]] the same inequality for the parts with 𝒥_g and with ϱ closes
    with these coefficients. In the bounds at a point, 𝔰_g ≤ m + 𝔵 𝔰_g, m the largest of the linear bounds, gives 𝔰_g ≤
    m/(1 − 𝔵); in the argument with t of [[lem:tl5-hfq-theta]], t ≤ 1 + 𝔵 t gives t ≤ 1/(1 − 𝔵). The rest of each proof holds
    as written. ∎

New:

    *Proof.* In each of these proofs the smallness is used through 𝔰 ≤ 𝔰_♭, |H| ≤ 1/8 and 𝔰 ≤ 1, which 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2
    keeps, and through k₃ 𝔰 ≤ 1/2 in the absorptions, the constant there being k₃ of the chosen set or, at level four,
    k₃^♮(μ) ≤ k₃^♮(ν); with 𝔰 ≤ 𝔰₁^v each of these products is at most 𝔵. In the bound of the second derivatives,
    M ≤ k₁ 𝒥 + k₂ ϱ + 𝔵 (2𝒥 + M) gives M ≤ ((k₁ + 2𝔵) 𝒥 + k₂ ϱ)/(1 − 𝔵), and in the inductions of [[eq:tl5-hfs-m2]] and
    [[eq:tl5-hfq-m2]] the same inequality for the parts with 𝒥_g and with ϱ closes with these coefficients; the bounds that
    use them (of the products, of ‖M_g‖_Σ and of the first-order step) follow with the replaced coefficients. In the bounds
    at a point, 𝔰_g ≤ m + 𝔵 𝔰_g, m the largest of the linear bounds, gives 𝔰_g ≤ m/(1 − 𝔵); in the argument with t of
    [[lem:tl5-hfq-theta]], t ≤ 1 + 𝔵 t gives t ≤ 1/(1 − 𝔵). The rest of each proof holds as written. ∎

**m3. Comparison (P:64-71): "Replaced everywhere" and "𝔵 ≪ 1".** Why: the list misses λ_t^(μ,2), ς_t, C_(1,ϱ) and the
products' terms with ϱ (so ε^w); and 𝔵 ≪ 1 does not follow from the cap setting 𝔰₁^v: 𝔵 = 1/4 exactly where
𝔰₁^v = 1/(4 sup k₃), as at three of G0h's four level-6 points (k₃^♮(μ) = 6.3 × 10³ … 1.3 × 10⁵), and 0.19 at the fourth
(cap 1.4 × 10⁻⁵ against 1/(4k₃) = 1.8 × 10⁻⁵). Each factor gains at least log₁₀(2(1 − 𝔵)), 0.18 decades at 𝔵 = 1/4.
Old (P:64-71): the paragraph from "Not chapter text. One new number" to "targets 4 not attempted." New:

    Not chapter text. One new number, 𝔵 = 𝔰₁^v sup k₃ (≤ 1/4), with k₃ the absorption constant of the chosen set. Replaced
    everywhere: 2(k₁^(j,·) + 1) → (k₁^(j,·) + 2𝔵)/(1 − 𝔵) (in 𝔨_A, λ_t^μ, λ_t^(μ,2), M_g bounds, eq:tl5-hfs-m2,
    eq:tl5-hfq-m2; in C₁^x the term 2√43(k₁^μ + 1) → √43(k₁^μ + 2𝔵)/(1 − 𝔵)); 2k₂ → k₂/(1 − 𝔵) (in the same bounds, in ς_t,
    in C_(1,ϱ) as 32k₂² → 8k₂²/(1 − 𝔵)², and in the products' terms with ϱ, so that ε^w carries 𝔰₁^v/(1 − 𝔵) in place of
    2𝔰₁^v); the factor 2 in C_∞^(m), C_(∞,ϱ)^(m), C_(∞,0)^(m), C_P^v, C_(P,ϱ)^v, C_(P,0)^v → 1/(1 − 𝔵). Each replaced factor
    gains at least log₁₀(2(1 − 𝔵)): 0.18 decades at 𝔵 = 1/4, up to log₁₀ 2 ≈ 0.3 as 𝔵 → 0. 𝔵 = 1/4 exactly where 𝔰₁^v =
    1/(4 sup k₃), as at three of G0h's four level-6 points; where the cap 𝔰_(θ,v) sets 𝔰₁^v, 𝔵 is the cap times sup k₃
    (0.19 at the fourth), small only if the cap lies far below 1/(4 sup k₃). (In C₁: the "factors 2·2" item loses one 2,
    and k₁ + 1 → about k₁ when 𝔵 is small.) Not done: the ℓ² recovery over the words (target 1, the √43 with k₁): its
    nonlinear terms now carry 𝔵 per word, so they could be summed, but the couplings 𝔄 counted over the words need an ℓ²
    operator norm of the coupling family (a Schur bound over rows and columns) that is not written here; targets 4 not
    attempted.

### nits

**n1. The theorem's proof (P:30).** The lemma applies at p because Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ carries 𝔰 ≤ 𝔰₁^v; say so.
Replacement under m1.

(Observation, no change: in the "Not done" sentence, "could be summed" would need √43·𝔵 < 1 or an ℓ² absorption; with
𝔵 up to 1/4 that is not automatic.)

Crosswalk rows in the fixed copy (only line numbers change): sec 1, lem 10, thm 32, rem 43.

## 4. Verdict

The new continuity argument is legitimate and the replacements are right, each from an absorption, each at most the old
factor, so thm:tl5-hfy contains thm:tl5-hfx. Three minor findings are open: the lemma's scope (lem:tl5-hfs-linfty is not
available under option (b) and at level four with this 𝔵) and its incomplete list of where the replaced bounds enter
(λ_t^(μ,2), ς_t, C_(1,ϱ), the products' terms with ϱ and so ε^w); the proof's "used only through"; and the Comparison's
"Replaced everywhere" and "𝔵 ≪ 1". With the six replacements above, all tested in the fixed copy (lint 0 hits, assemble
--check 0 problems, in-memory `[] 0`, crosswalk 403 = 403, no printed number changed), nothing else is open.

Verdict: NOT CONFIRMED
