### The first-order constant, counted over the words {#sec:tl5-hfx}

In the first-order step of the proof of [[lem:tl5-hf-linfty]], and in its weighted forms, each of the 43 words J of
rotations with |J| ≤ 2 is bounded by the whole of 𝒥₁, which gives the factor 258 = 6 · 43 of C₁. This section counts
the terms that are first derivatives over the words, as the words JB are distinct, and keeps the count 43 only for the
second derivatives, which are bounded through their maximum; it applies to the constant C₁^♮ of [[lem:tl5-hfs-linfty]]
with either choice of Sobolev constants, at every level N ≥ 4. The notation is that of [[sec:tl5-hfw]].

**Lemma {#lem:tl5-hfx-c1}** (The first-order constant.) Let ρ′₁ := 2μΛ₁, ρ′₂ := 4μΛ₁ + 2μ^(3/2)Λ₂ and ϖ′ := 6ρ′₁² +
36ρ′₂², and let C₁^x be the smaller of C₁^♮ and the number formed as C₁^♮ with (1 + ϖ′^(1/2))²/43 in place of
(1 + 6Λ₂^μ)² and with (2(43)^(1/2)(k₁^μ + 1) + (2ϖ′)^(1/2))²/43 in place of 72(Λ₂^μ)² + 8(k₁^μ + 1)²:

    C₁^x² = min(C₁^♮², 6 C² 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))²
            + 4|∂_γ|² (2(43)^(1/2) (k₁^μ + 1) + (2ϖ′)^(1/2))²)),                                        {#eq:tl5-hfx-c1}

6C² 𝔴⁶ 𝔳⁶ standing for 6C_(S³)² 𝔭₃ 𝔴⁶ 𝔳⁶ or 6C_(E,3)² 𝔴₀⁶ 𝔳₀⁶. Then [[lem:tl5-hfs-linfty]], [[lem:tl5-hft-small]] and
[[lem:tl5-hfq-theta]] hold with C₁^x in place of C₁^♮.

*Proof.* In the first-order step for A := D̂Ψ_B, |B| ≤ N − 3, write ℒ^J A = D̂Ψ_(JB) + R′_J and D̂ℒ^J A = D̂²Ψ_(JB) +
D̂R′_J. The words JB are distinct for distinct J, so Σ_J μ^(|B|+3) |D̂Ψ_(JB)|² ≤ 𝒥_g², as μ^(|B|+3) ≤ μ^(|JB|). By
[[lem:tl5-hfs-quadratic]] (a) with Ψ_B in place of h, R′_J has 2 monomials whose coefficient carries one letter if |J| =
1, and 4 with one letter and 2 with two letters if |J| = 2, each contracted with a Ψ_C, |C| = |JB| − a; with μ^(|B|+3)
≤ μ^(1+a) μ^(|C|), μ^((|B|+3)/2) |R′_J| ≤ ρ′_(|J|) 𝒥_g and μ^((|B|+3)/2) |D̂R′_J| ≤ √2 ρ′_(|J|) 𝒥_g, so that, by
Minkowski's inequality over the words, (Σ_J μ^(|B|+3) |ℒ^J A|²)^(1/2) ≤ (1 + ϖ′^(1/2)) 𝒥_g and (Σ_J μ^(|B|+3) |D̂ℒ^J
A|²)^(1/2) ≤ 43^(1/2) max_J μ^((|B|+3)/2) |D̂²Ψ_(JB)| + (2ϖ′)^(1/2) 𝒥_g. By [[eq:tl5-hfs-m2]] (or [[eq:tl5-hfq-m2]], or
the bound of M_g in [[lem:tl5-hft-small]] (b)), μ^((|B|+3)/2) |D̂²Ψ_(JB)| ≤ 2(k₁^μ + 1) 𝒥_g + (its part with ϱ). In the
Sobolev inequality [[eq:tl5-hf-cs-r]] (or that of [[lem:tl5-hft-face]]) with r = 3, insert these bounds in place of
the bounds of the 43 words by 𝒥 used in the proof of [[lem:tl5-hf-linfty]], separate the parts with 𝒥_g from those with
ϱ by (x + y)² ≤ 2x² + 2y² as there, and use ∫ 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g; this gives the part with ℰ_g of the
bound with the second entry of [[eq:tl5-hfx-c1]], and parts with ϱ and η₀ at most those of that proof, the part with ϱ
being half of it. The bound with C₁^♮ holds as well, with the same parts with ϱ and η₀; so it holds with C₁^x. ∎

**Theorem {#thm:tl5-hfx}** (Existence with the first-order constant counted over the words.) The conclusions of
[[thm:tl5-hfw]] hold under its hypotheses with every constant formed with C₁^x in place of C₁^♮, in particular in C_P^v
(directly, and at level four also through 𝔨_rec), hence in 𝔎 and S_F^v, and in C_(∞,μ)^(N−4) of 𝔰_*^w.

*Proof.* The proofs of [[thm:tl5-hfw]] and of the results it rests on use C₁^♮ only through the bounds of
[[lem:tl5-hfs-linfty]], [[lem:tl5-hft-small]] and [[lem:tl5-hfq-theta]], which hold with C₁^x by [[lem:tl5-hfx-c1]]. ∎

**Remark {#rem:tl5-hfx-what}** (What changes.) In the second entry of [[eq:tl5-hfx-c1]] the count 43 remains only with
the recovery constant k₁^μ, whose coefficient is 4 · 43 · 4 against 4 · 43 · 8 in C₁^♮; the terms without k₁^μ carry
(1 + ϖ′^(1/2))² and 4|∂_γ|² · 2ϖ′ against 43(1 + 6Λ₂^μ)² and 4|∂_γ|² · 43 · 72(Λ₂^μ)², and the cross term
4|∂_γ|² · 4 · 43^(1/2)(k₁^μ + 1)(2ϖ′)^(1/2) has no counterpart. As ϖ′ ≤ 1320(Λ₂^μ)², the second entry is the smaller if
8Λ₂^μ ≤ k₁^μ + 1 on Σ₁(a, b); otherwise the cross term can make it the larger, and the minimum keeps C₁^x ≤ C₁^♮. As
for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfx]] are established in this paper for no
background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD a3d0c091, where sec:tl5-hfw is merged (Section 57.21,
merge cf314394). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfx) through the last line of
[[rem:tl5-hfx-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfw-what]] (line 6297, as
changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfw-what]] (lines 6296–6297).* Old:

[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfw]] are established in this paper for no background
at 10 l5.

New:

[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfw]] are established in this paper for no background
at 10 l5. [[sec:tl5-hfx]] counts the first-order constant over the words ([[thm:tl5-hfx]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text. The one new factor is C₁^x (eq:tl5-hfx-c1), used everywhere C₁^♮ (or C₁^E) was: C_P^v (directly,
and at level four through 𝔨_rec), hence 𝔎 and S_F^v, and C_(∞,μ)^(N−4) in 𝔰_*, at level four and at N ≥ 6 alike.
ρ′₁ = 2μΛ₁, ρ′₂ = 4μΛ₁ + 2μ^(3/2)Λ₂, ϖ′ = 6ρ′₁² + 36ρ′₂² ≤ 1320(Λ₂^μ)². Against C₁^♮, in the second entry of the
minimum: the k₁ part loses a factor 2 under the root (0.15 decades of C₁ when it dominates), the part without k₁ and
∂_γ, 43(1 + 6Λ₂^μ)² → (1 + ϖ′^(1/2))², up to 1.6 decades of its square when ϖ′ is small, and the cross term
4|∂_γ|² · 4 · 43^(1/2)(k₁^μ + 1)(2ϖ′)^(1/2) is new. The second entry is the smaller where 8Λ₂^μ ≤ k₁^μ + 1, so at G0e's
Λ₂^μ ≤ 4 × 10⁻³ with k₁^μ = 7–16; at μ = 1, Λ₁ = Λ₂ = 2, k₁^μ + 1 = 8, |∂_γ| = 1, D̂∂_γ = 0 it is 11 % above C₁^♮,
hence the minimum. What blocks more (deduced): the
count 43 with k₁^μ remains because the second derivatives D̂²Ψ_(JB) are bounded through their maximum; an ℓ² count over
the words needs an ℓ² form of the recovery, whose nonlinear terms carry k₃𝔰 ≤ 1/4 per word and so do not become small
in ℓ²; the rank 3, 𝔨₂ and the (E₁, E₁) component remain for the reasons given with P-GRD5. Level 6: C₁^x enters there
as well (C_P^v = C_(∞,μ)^(1), and C_(∞,μ)^(2) in 𝔰_*^w); its effect there is not evaluated here.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfx	paper/reader/proofs/P-GRD7.md@PENDING:1	P-GRD7, section	new; at the end of ch:ten-l5, after rem:tl5-hfw-what; first-order constant counted over the words
    lem:tl5-hfx-c1	paper/reader/proofs/P-GRD7.md@PENDING:9	P-GRD7, Lemma	C1^x: first derivatives counted over the 43 words, count 43 kept only with k1^mu
    eq:tl5-hfx-c1	paper/reader/proofs/P-GRD7.md@PENDING:14	P-GRD7, display	new
    thm:tl5-hfx	paper/reader/proofs/P-GRD7.md@PENDING:33	P-GRD7, Theorem	thm:tl5-hfw with C1^x in place of C1^nat
    rem:tl5-hfx-what	paper/reader/proofs/P-GRD7.md@PENDING:40	P-GRD7, Remark	what changes in C1

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hfw-what, add "; points to sec:tl5-hfx
(P-GRD7 item 2)".
