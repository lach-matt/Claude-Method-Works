# R-P-GRD6: review of proofs/P-GRD6.md (sec:tl5-hfw, "The terms with ϱ, sharpened")

File reviewed: research/warp-drive/paper/reader/proofs/P-GRD6.md, md5 6f10eb9c80d4742ec5efcef77a655845, 95 lines, at
b8d033b5 (branch ccr-af9edcf6-9a60sz; HEAD d589f0b7 adds only rule/, the reader's chapters are those of b8d033b5 and
cb200e34). Chapter: chapters/87-ten-l5.md, 6254 lines, md5 78dd5c4b…, last changed by 86f3d84e (sec:tl5-hfv merged),
as the Placement says. "87:n" is a chapter line, "P:n" a line of the file.

Fixed copy: scratchpad/reader/rpgrd6/P-GRD6.fixed.md, md5 4a08f9e37e0e33b4d15dd1b6b781963a, 103 lines, made by
scratchpad/reader/rpgrd6/tools/fix.py (7 replacements, each found exactly once; crosswalk @PENDING numbers recomputed).

## 1. Mechanics (both the file as submitted and the fixed copy)

Scratch merge into a fresh `git archive HEAD` tree with the writer's placement (item 2 found once at 87:6253-6254, the
section appended after the new last line with one blank line):

| check | P-GRD6.md | P-GRD6.fixed.md |
|---|---|---|
| lint.py --chapters | 62 files, 5245 labels (5239 + 6), 0 hits | same, 0 hits |
| assemble.py --check | 0 problems | 0 problems |
| in-memory check | `[] 0` | `[] 0` |
| lines over 121 characters / forbidden wrapped starts | none outside the crosswalk rows / none | none / none |
| crosswalk rows: label at the stated line | 6 of 6 | 6 of 6 (lines 1, 10, 14, 18, 21, 35) |
| chapter labels = crosswalk + new rows | 394 = 394 | 394 = 394 |
| printed numbers of the 5239 existing labels | 0 changed | 0 changed |

New: Section 57.21, Definition 57.199, Theorem 57.200, Remark 57.201, displays (57.144), (57.145). Labels lowercase.

## 2. The five checks asked for

### 2.1 No circularity: correct

- **Order.** thm:tl5-hfw runs lem:tl5-continuation (87, its (H1)-(H4)) with A := A_w^v, B := B_v. The a priori estimate is
  applied to a solution on D^κ_s with Y_σ ≤ 2A_w^v for all σ ∈ [1/2, s] (assumed). Step 1 (87:4468-4475, as
  re-used at 87:5312-5317, 5690-5694, 5925-5930, 6108) is a continuity argument in σ inside [1/2, s]: Σ_* := {σ : 𝔰 ≤ 𝔰₀ on D^κ_σ}
  contains 1/2 (𝔰 ≤ η₀ < 𝔰₁ on N₀), is closed, and is open because at p ∈ D^κ_σ the low-quantity bound with
  ℰ ≤ e^φ Y_σ² ≤ 4e^φ A² gives 𝔰(p) ≤ 𝔰_* < 𝔰₁ ≤ 𝔰₀/2. It uses only the assumed bound on Y and η₀ < 𝔰₁, 𝔰_* < 𝔰₁;
  it concludes 𝔰 ≤ 𝔰_*^w < 𝔰₁^v at every point of D^κ_s. Step 2 then integrates over Q(a′, b′) ⊂ D^κ_s (b′ ≤ s),
  and the products lemmas are applied at points of D^κ_s with ϱ(p) ≤ ϱ (87:5317, 5694). So the bound 𝔰 < 𝔰₁^v is
  available at every point where Step 2 uses it, and it is derived before Step 2 from the hypothesis alone; Step 3 and
  the strict improvement Y_s ≤ A + BY_s² ⇒ Y_s < 2A then close the outer continuity as before.
- **Well defined.** 𝔰₁^v = min(𝔰₀/2, c_*κ_m/2, 𝔰_(θ,v)) with 𝔰₀ = 𝔰₀^♮, 𝔰₀^μ or 𝔰₀^q (87:5652, 5912, 6087): background
  quantities and ϑ₁, ϑ₂ only, no A, ε, Y or ϱ. So ε^w (fixed by 𝔰₁^v), then A_w^v, then 𝔰_*^w are defined in that
  order; 𝔰_*^w < 𝔰₁^v is a condition with 𝔰₁^v on both sides, not a fixed point. A_w^v = 0 still forces R̂ic = 0
  (s_N[2R̂ic] = 0, the term J = I carrying 𝔮_(jj) = 1), so the trivial case of the proof of thm:tl5-hf (87:4577) is
  unchanged.

### 2.2 Every occurrence: correct for ε^v; the level-four terms 𝔑^M_I are outside it (finding m2)

ε^v = 𝒮[s_N[2R̂ic] + (1/4)𝔤_ϱ^v k₂ ϱ] (87:5662, 5913, 6092). Its first part is the linear forcing Σ_J 𝔔_IJ ℒ^J(2R̂ic)
(87:4482-4487), unchanged. Its second part is exactly the ϱ part of the nonlinear terms −Σ_(J≠I) 𝔔_IJ ℒ^J N(h) − 𝔑^L_I.
Every one of these monomials is residual × a factor bounded by 𝔰:
- the ϱ comes only from the bound of a factor Φ₂ = D̂²Ψ_C (eq:tl5-hfg-m2, eq:tl5-hfs-m2, eq:tl5-hfq-m2, the recovery
  from the equation, where the residual enters); a factor Φ₂ that is not a second derivative is bounded by 𝔨_B 𝒥_g, with
  no ϱ (87:5606);
- the monomial has q ≥ 2 solution factors (N(h) is at least quadratic, H counting as one), and the ϱ term is
  ν 𝔰^(q−1)·(weights)·2k₂ϱ: lem:tl5-hfg-products (87:5228-5232), lem:tl5-hfs-products (87:5602-5608, Φ₁ ∈ {H, h, Ψ_B}
  when Φ₂ = D̂²Ψ_C, all quantities of 𝔰 = max(|H|, |Ψ_B| (|B| ≤ N−2), |D̂Ψ_B| (|B| ≤ N−3), |D̂²Ψ_B| (|B| ≤ N−4)), 87:4241),
  lem:tl5-hft-products (87:5895-5903, "ν 𝔰^(q−1)"), lem:tl5-hfq-theta (87:6059-6063, "𝔰^(q−1)");
- in H^(αβ) D̂_αD̂_βΨ_J, |J| < n, the ϱ term is |H|·2k₂ϱ with |H| ≤ 𝔰 (87:5236-5237, 5611-5612, 5902);
- the 𝔰 is the unweighted one, which Step 1 bounds in every option: μ = 1 in eq:tl5-hfg-linfty and eq:tl5-hfs-linfty
  (87:5312-5314, 5690-5692), eq:tl5-hft-small/-smallb (87:5925-5928), eq:tl5-hfq-small (87:6108);
- every Step 2 writes the term as 2k₂𝔰ϱ and then uses 𝔰 ≤ 1/8 (87:4500, 5331, 5703, 5934, 6112); both routes of the
  min at level four carry it, so the min survives the replacement.
No nonlinear term carries ϱ times a background quantity alone or ϱ alone. What else carries ϱ, all unchanged and
correctly left: the parts with ϱ of 𝔰_P and 𝔓 (C_(P,ϱ)ϱ, 𝔎_ϱϱ) in 𝔟_(o,s), 𝔟_(i,s), hence 𝔯_(w,s) (Y² terms); the
threshold term C_(∞,ϱ)ϱ (or ν^(−2)C_((∞,ϱ),ν)ϱ) of 𝔰_*; and at level four the terms 𝔑^M_I, whose ϱ enters through
‖M_g‖_Σ ≤ λ𝔍 + ς_t ϱ in X₂ and 𝔜′ϱ in Y₁ (lem:tl5-hfs-mixed, 87:5614-5645): ϱ𝔍 terms go into 𝔯_M, the ϱη₀ term into
ε_M = μ^(−3/2) ϱ η₀ ∫ …, already a product of the residual with the data bound η₀, and S_M has no ϱ. N ≥ 6: the M terms
are 0 (87:5673). So the sharpening is right where it is made. But the intro (P:3-4) and the proof (P:25-26) say "the
part with ϱ of the nonlinear terms" and "the nonlinear terms of level j contribute … a part 2Ω̂² 𝔤_ϱ^v 2k₂ 𝔰 ϱ": at level
four the terms 𝔑^M_I are nonlinear terms that do not; the merged proofs say "other than 𝔑^M_I" (87:5321, 5698). m2.

### 2.3 The size estimate: G0g and G0h are right, the file's 10⁻¹⁵…10⁻¹⁸ is wrong (finding m1)

At level four G0g reports 𝔰₁^q = 8.3 × 10⁻⁶, 1.3 × 10⁻⁶, 4.5 × 10⁻⁶, 1.8 × 10⁻⁶ (G0g.0, row "μ; 𝔰_♭; 𝔰₁^q"; seed 1
D_A, seed 2 D_A, seed 1 D*, seed 2 D*), i.e. 10^−5.1…−5.9 (its line 62), and G0h 𝔰₁^v = 2.0 × 10⁻⁵, 5.9 × 10⁻⁶,
1.4 × 10⁻⁵, 4.5 × 10⁻⁶, each the cap 𝔰_(θ,v) (G0h.0). Both are bounded by the cap ≈ ϑκc/(√2 + ½) with ϑ = κ = 10⁻² and
by 𝔰_♭/2 = 5 × 10⁻⁵. Nothing in the reports gives 10⁻¹⁵…10⁻¹⁸ at level four; the nearest figure is option (a)'s 𝔰₁^♮ at
level six, 10^−11…−17 (G0h line 101). The ratio 8𝔰₁^v is then 10^−3.8, −4.3, −4.0, −4.4 at G0h's values (10^−4.2,
−5.0, −4.4, −4.8 at G0g's), not 14-17 decades. The conclusion survives at these points: G0h's addendum finds the room
for a ϱ lever to be 1.9, 2.2, 2.6 and 3.3 decades before f binds, and every 8𝔰₁^v above is smaller than 10^−3.3. The
𝔰₁ quoted are those of the f-optimal points; at the max-min points of the addendum they are not listed, and the
evaluation will settle them (a larger 𝔰₁ costs decades one for one).

### 2.4 rem:tl5-hfw-what: "free split" true, but the first sentence is false (finding m3)

𝒮 (eq:tl5-hf-source, 87) is a sum of integrals of weighted L² norms of 2Ω̂²s, so it is monotone, subadditive and
positively homogeneous; ε^w ≤ 𝒮[s_N[2R̂ic]] + 2𝔰₁^v ϱ 𝒮[𝔤_ϱ^v k₂], and every hypothesis is monotone in ε^w. So any
bounds of the two parts with which the hypotheses hold are admissible and the theorem fixes no ratio: correct. But
"The closing condition contains the residual only through ε^w + ε_M^v" is false: [[eq:tl5-hfw-closing]] contains η =
1 − max(ϑ₁, ϑ₂) − 𝔯^v, and 𝔯^v contains ϱ (𝔟_(o,s), 𝔟_(i,s) at 87:5657-5658; 𝔯_(M,q) at 87:6094); 𝔰_*^w contains ϱ
too. The sentence then names "the conditions on 𝔯^v" although the theorem has none apart from η > 0 in (c). The
Comparison repeats "the theorem needs only the sum". Also "s_N[2R̂ic] and ϱ enter by the triangle inequality" describes
a bound, not how they enter (ε^w is 𝒮 of their sum), and "the coefficient of ϱ in ε^w" needs that bound to be defined.
Note for the evaluation: f and ϱ are two bounds of the same residual of one approximant, so the "split" is a choice of
how to allot the ε budget when setting the rule's targets, which is what G0h.rule does; the theorem itself never splits.

### 2.5 Every earlier closing condition stays valid: yes, and thm:tl5-hfw contains thm:tl5-hfv

Nothing earlier is edited except the appended sentence of rem:tl5-hfv-what. 𝔰₁^v ≤ 𝔰_♭/2 ≤ 1/16 in every option
(𝔰₀^♮, 𝔰₀^μ, 𝔰₀^q all start with min(𝔰_♭, …), 87:5652, 5912, 6087; 𝔰_♭ ∈ (0, 1/8], 87:5047), so 2𝔰₁^v ≤ 1/8 < 1/4,
ε^w ≤ ε^v, A_w^v ≤ A_v, 𝔰_*^w ≤ 𝔰_*^v: the hypotheses of thm:tl5-hfv imply those of thm:tl5-hfw. η, B_v, 𝔯^v are
untouched. Correct.

### 2.6 The rest

def:tl5-hfw-constants: the three choices of 𝔤_ϱ^v are exactly the factors of (1/4)k₂ϱ in ε_(w,s), ε_(w,t) option (b)
and ε_(w,q) (87:5662, 5913, 6092). [[eq:tl5-hfw-closing]] = 4A_w^vB_v: correct. The theorem's statement, the conclusions
with A_w^v and 𝔰_*^w, and the Placement's commit statements (cb200e34 = HEAD for the chapter; 86f3d84e is the merge of
sec:tl5-hfv) are correct.

## 3. Findings

### Major

None.

### minor

**m1. Comparison, the size estimate (P:76-77).** Why: §2.3; the evaluation reads this paragraph. Old:

    ϱ coefficients is 8𝔰₁^v: at G0g's values 𝔰₁^q ≈ 10⁻¹⁵…10⁻¹⁸ at level four (from the reports; not recomputed here) this
    removes about 14–17 decades from the coefficient that binds ϱ, so that, by G0h's addendum, f binds again.

New:

    ϱ coefficients is 8𝔰₁^v. At level four G0h reports 𝔰₁^v = 2.0 × 10⁻⁵, 5.9 × 10⁻⁶, 1.4 × 10⁻⁵ and 4.5 × 10⁻⁶ (seed 1
    D_A, seed 2 D_A, seed 1 D*, seed 2 D*; each the cap 𝔰_(θ,v)) and G0g 𝔰₁^q = 8.3 × 10⁻⁶, 1.3 × 10⁻⁶, 4.5 × 10⁻⁶ and
    1.8 × 10⁻⁶: the ratio removes about 3.8, 4.3, 4.0 and 4.4 decades from the coefficient that binds ϱ (4.2, 5.0, 4.4 and
    4.8 at G0g's values), more than the room of 1.9, 2.2, 2.6 and 3.3 decades that G0h's addendum finds for a lever on
    it, so that there f binds again. These 𝔰₁ belong to the f-optimal points (not recomputed here); the evaluation will
    settle the number at the max-min points.

**m2. The terms 𝔑^M_I at level four (P:3-7 and P:25-31, chapter text).** Why: §2.2. The statements cover all nonlinear
terms; at level four the 𝔑^M_I carry ϱ into 𝔯_M and ε_M, not through 𝔰 ≤ 1/8. The same replacement makes two small
corrections: "a factor 𝔰 of the solution" (the factor is bounded by 𝔰), and "𝔰_*^v" where this section's Step 1 gives
𝔰_*^w. Old (P:3-7):

    In the proofs of [[prop:tl5-hf-bootstrap]] and of all its sharpened forms, the part with ϱ of the nonlinear terms is a
    product of the residual with a factor 𝔰 of the solution, and it is bounded there by (1/4) k₂ ϱ through 𝔰 ≤ 1/8. After
    Step 1 of those proofs, 𝔰 is at most 𝔰_*^v < 𝔰₁^v on D^κ_s; this section uses that bound instead, at level four and at
    level N ≥ 6, which multiplies the coefficient of ϱ in the error ε by 8𝔰₁^v. The closing condition is
    [[eq:tl5-hfw-closing]]; the earlier ones remain valid. The notation is that of [[sec:tl5-hfv]].

New:

    In the proofs of [[prop:tl5-hf-bootstrap]] and of all its sharpened forms, the part with ϱ of the nonlinear terms (at
    level four, of those other than the terms 𝔑^M_I, whose parts with ϱ go into 𝔯_M and ε_M) is a product of the residual
    with a solution factor bounded by 𝔰, and it is bounded there by (1/4) k₂ ϱ through 𝔰 ≤ 1/8. After Step 1 of the proof
    of [[thm:tl5-hfw]], 𝔰 is at most 𝔰_*^w < 𝔰₁^v on D^κ_s; this section uses that bound instead, at level four and at level
    N ≥ 6, which multiplies the coefficient of ϱ in the error ε by 8𝔰₁^v. The closing condition is [[eq:tl5-hfw-closing]];
    the earlier ones remain valid. The notation is that of [[sec:tl5-hfv]].

Old (P:25-31, from "in Step 2."):

    in Step 2. Step 1 uses only 𝔰_*^w < 𝔰₁^v and gives 𝔰 ≤ 𝔰_*^w < 𝔰₁^v on D^κ_s. In Step 2, the nonlinear terms of level j
    contribute to the bulk a part with 𝒥_g, bounded as there, and a part 2Ω̂² 𝔤_ϱ^v 2k₂ 𝔰 ϱ (√e_o + √c √e_i): in each
    monomial the factor bounded by its part with ϱ is multiplied by a factor Φ₁ with |Φ₁| ≤ 𝔰, or, in H^(αβ) D̂_αD̂_βΨ_J, by
    H with |H| ≤ 𝔰, as in the proofs of [[lem:tl5-hfs-products]], [[lem:tl5-hft-products]] and [[lem:tl5-hfq-theta]]; the
    constant 𝔤_ϱ^v is the one of those proofs. There the bound 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ was used; we use 2k₂ 𝔰 ϱ ≤ 2𝔰₁^v k₂ ϱ,
    by Step 1. As in the proof of [[prop:tl5-hf-linear]] this part is bounded by Y_s 𝒮[2𝔰₁^v 𝔤_ϱ^v k₂ ϱ], which with the
    forcing term gives Y_s ε^w in place of Y_s ε^v. ∎

New:

    in Step 2. Step 1 uses only 𝔰_*^w < 𝔰₁^v and gives 𝔰 ≤ 𝔰_*^w < 𝔰₁^v on D^κ_s. In Step 2, the nonlinear terms of level j
    other than 𝔑^M_I contribute to the bulk a part with 𝒥_g, bounded as there, and a part 2Ω̂² 𝔤_ϱ^v 2k₂ 𝔰 ϱ (√e_o + √c
    √e_i): in each monomial the factor bounded by its part with ϱ is multiplied by a factor Φ₁ with |Φ₁| ≤ 𝔰, or, in
    H^(αβ) D̂_αD̂_βΨ_J, by H with |H| ≤ 𝔰, as in the proofs of [[lem:tl5-hfs-products]], [[lem:tl5-hft-products]] and
    [[lem:tl5-hfq-theta]]; the constant 𝔤_ϱ^v is the one of those proofs, and the terms 𝔑^M_I are bounded as there. There
    the bound 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ was used; we use 2k₂ 𝔰 ϱ ≤ 2𝔰₁^v k₂ ϱ, by Step 1. As in the proof of
    [[prop:tl5-hf-linear]], this part together with the forcing term 2Ω̂² s_N[2R̂ic] (√e_o + √c √e_i) is bounded by
    Y_s ε^w, in place of Y_s ε^v. ∎

(The last sentence also fixes a small slip: bounding the ϱ part alone by Y_s𝒮[2𝔰₁^v𝔤_ϱ^v k₂ϱ] and the forcing term
alone by Y_s𝒮[s_N[2R̂ic]] gives their sum, which is at least Y_s ε^w by subadditivity; Y_s ε^w needs the two integrands
bounded together, as the merged Step 3 does at 87:4502.)

**m3. rem:tl5-hfw-what (P:33-38, chapter text), and the Comparison's "needs only the sum" (P:81).** Why: §2.4. Old
(P:33-38):

    **Remark {#rem:tl5-hfw-what}** (The split of the error.) The closing condition [[eq:tl5-hfw-closing]] contains the
    residual only through ε^w + ε_M^v, in which s_N[2R̂ic] and ϱ enter by the triangle inequality for 𝒮; any bounds of
    𝒮[s_N[2R̂ic]] and of ϱ whose combination keeps [[eq:tl5-hfw-closing]] and the conditions on 𝔯^v and 𝔰_*^w are
    admissible, and the theorem does not fix their ratio. The coefficient of ϱ in ε^w is 8𝔰₁^v times that of ε^v, where
    𝔰₁^v ≤ 𝔰_♭/2 ≤ 1/16. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfw]] are established in
    this paper for no background at 10 l5.

New:

    **Remark {#rem:tl5-hfw-what}** (The split of the error.) The residual enters the hypotheses of [[thm:tl5-hfw]] through
    ε^w and ε_M^v, and through ϱ also in 𝔯^v, and so in η, and in 𝔰_*^w. As 𝒮 is subadditive and positively homogeneous,
    ε^w ≤ 𝒮[s_N[2R̂ic]] + 2𝔰₁^v ϱ 𝒮[𝔤_ϱ^v k₂], and the hypotheses hold whenever they hold with ε^w replaced by this sum; so
    any bounds of 𝒮[s_N[2R̂ic]] and of ϱ with which they hold are admissible, and the theorem does not fix their ratio. The
    coefficient 2𝔰₁^v 𝒮[𝔤_ϱ^v k₂] of ϱ there is 8𝔰₁^v times the one for ε^v, where 𝔰₁^v ≤ 𝔰_♭/2 ≤ 1/16. As for
    [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfw]] are established in this paper for no background
    at 10 l5.

Old (P:80-81, the sentence beginning "The"): "split of ε between f and ϱ is free (rem:tl5-hfw-what); the theorem needs
only the sum. 𝔯 is not involved." New:

    split of ε between f and ϱ is free (rem:tl5-hfw-what); in ε^w the theorem needs only the sum, but ϱ also enters 𝔯^v
    (so η), 𝔰_*^w and ε_M^v, which this section leaves as they are.

### nits

**n1. Placement item 1 (P:50).** After item 2 replaces two lines by three, the last line of rem:tl5-hfv-what is 6255
(as in the merged P-GRD5). Old: "(line 6254, as changed by item 2)". New: "(line 6255 once item 2 is applied)".

**n2. Comparison, closing condition (P:71-72).** η > 0 is part of (c). Old:

    *Closing condition (proved, levels 4 and ≥ 6):* 4 η^(−3/2) (δ_w + η^(−1/2)(ε^w + ε_M^v)) (S_F^v + S_M^v) < 1 with η₀ <
    𝔰₁^v, 𝔰_*^w < 𝔰₁^v and the rate condition of thm:tl5-hfv.

New:

    *Closing condition (proved, levels 4 and ≥ 6):* 4 η^(−3/2) (δ_w + η^(−1/2)(ε^w + ε_M^v)) (S_F^v + S_M^v) < 1 with
    η > 0, η₀ < 𝔰₁^v, 𝔰_*^w < 𝔰₁^v and the rate condition of thm:tl5-hfv.

Crosswalk rows in the fixed copy (only line numbers change): sec 1, def 10, eq:tl5-hfw-eps 14, thm 18,
eq:tl5-hfw-closing 21, rem 35.

## 4. Verdict

The theorem is correct and the gain is real: the ϱ coefficient of ε falls by the factor 8𝔰₁^v, with no circularity and
no ϱ term of ε left at the old coefficient. Three minor findings are open in the file as submitted: the size estimate in
the Comparison (10^−3.8…−5.0, not 14-17 decades), the level-four terms 𝔑^M_I omitted from two statements, and a false
first sentence of the remark. With the seven replacements above, all tested in the fixed copy (lint 0 hits, assemble
--check 0 problems, in-memory `[] 0`, crosswalk 394 = 394, no printed number changed), nothing else is open.

Verdict: NOT CONFIRMED
