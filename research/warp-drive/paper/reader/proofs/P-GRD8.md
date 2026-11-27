### The absorption with the bootstrap's smallness {#sec:tl5-hfy}

In the recovery of second derivatives and in the bounds at a point of [[sec:tl5-hfs]], [[sec:tl5-hft]],
[[sec:tl5-hfq]], [[sec:tl5-hfv]] and [[sec:tl5-hfx]], the nonlinear terms are absorbed with k₃𝔰 ≤ 1/2, which gives the
factors 2 in 2(k₁ + 1), in 2k₂ and in front of the maxima of the constants C_∞. After Step 1 of the bootstrap, 𝔰 is at
most 𝔰₁^v; this section runs the bootstrap with that smallness as the hypothesis of the bounds at a point, so that the
absorption costs 1/(1 − 𝔵) with 𝔵 := 𝔰₁^v sup_(D^κ) k₃ ≤ 1/4 in place of 2, at every level N ≥ 4. The notation is that
of [[sec:tl5-hfx]].

**Lemma {#lem:tl5-hfy-abs}** (Absorption with the smallness of the bootstrap.) Let k₃ denote the constant of the
absorption in the chosen set (k₃^♮ for option (a) of [[def:tl5-hft-constants]], k₃^♮(μ) for option (b), k₃^♮(ν) at
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

*Proof.* In each of these proofs the smallness is used through 𝔰 ≤ 𝔰_♭, |H| ≤ 1/8 and 𝔰 ≤ 1, which 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2
keeps, and through k₃ 𝔰 ≤ 1/2 in the absorptions, the constant there being k₃ of the chosen set or, at level four,
k₃^♮(μ) ≤ k₃^♮(ν); with 𝔰 ≤ 𝔰₁^v each of these products is at most 𝔵. In the bound of the second derivatives,
M ≤ k₁ 𝒥 + k₂ ϱ + 𝔵 (2𝒥 + M) gives M ≤ ((k₁ + 2𝔵) 𝒥 + k₂ ϱ)/(1 − 𝔵), and in the inductions of [[eq:tl5-hfs-m2]] and
[[eq:tl5-hfq-m2]] the same inequality for the parts with 𝒥_g and with ϱ closes with these coefficients; the bounds that
use them (of the products, of ‖M_g‖_Σ and of the first-order step) follow with the replaced coefficients. In the bounds
at a point, 𝔰_g ≤ m + 𝔵 𝔰_g, m the largest of the linear bounds, gives 𝔰_g ≤ m/(1 − 𝔵); in the argument with t of
[[lem:tl5-hfq-theta]], t ≤ 1 + 𝔵 t gives t ≤ 1/(1 − 𝔵). The rest of each proof holds as written. ∎

**Theorem {#thm:tl5-hfy}** (Existence with the absorption at the bootstrap's smallness.) The conclusions of
[[thm:tl5-hfx]] hold under its hypotheses with every constant formed with the replacements of [[lem:tl5-hfy-abs]], and
with 𝔰₁^v/(1 − 𝔵) in place of 2𝔰₁^v in ε^w.

*Proof.* In Step 1 of the proof, let Σ_* be the set of σ with 𝔰 ≤ 𝔰₁^v on D^κ_σ. It contains 1/2, as 𝔰 ≤ η₀ < 𝔰₁^v on
N₀, and it is closed. For σ ∈ Σ_* and p ∈ D^κ_σ, Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ, so [[lem:tl5-hfy-abs]] applies at p and
gives 𝔰(p) ≤ 𝔰_* < 𝔰₁^v, 𝔰_* formed with the replaced constants; by the uniform continuity of 𝔰, Σ_* is open in
[1/2, s], so Σ_* = [1/2, s]. Steps 2 and 3 then use the bounds of [[lem:tl5-hfy-abs]] in place of those they replace; in
the terms with ϱ of Step 2, k₂ 𝔰 ϱ/(1 − 𝔵) ≤ 𝔰₁^v k₂ ϱ/(1 − 𝔵) gives ε^w with 𝔰₁^v/(1 − 𝔵) in place of 2𝔰₁^v. The
rest of the proof of [[thm:tl5-hfx]] holds as written. ∎

**Remark {#rem:tl5-hfy-what}** (What changes.) With 𝔵 small the recovery constant 2(k₁^μ + 1) becomes nearly k₁^μ, 2k₂
nearly k₂, and the maxima of the constants C_∞ and C_P lose their factor 2; at 𝔵 = 1/4 the replacements are
(4/3)(k₁^μ + 1/2), (4/3)k₂ and 4/3; for every 𝔵 each new factor is at least 2(1 − 𝔵) times smaller than the one it
replaces. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfy]] are established in this paper
for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD 11a31701, where sec:tl5-hfx is merged (Section 57.22,
merge 2500bc7f). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfy) through the last line of
[[rem:tl5-hfy-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfx-what]] (line 6344, as
changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfx-what]] (lines 6343–6344).* Old:

for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfx]] are established in this paper for no
background at 10 l5.

New:

for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfx]] are established in this paper for no
background at 10 l5. [[sec:tl5-hfy]] absorbs the nonlinear terms with the bootstrap's smallness ([[thm:tl5-hfy]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

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

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfy	paper/reader/proofs/P-GRD8.md@PENDING:1	P-GRD8, section	new; at the end of ch:ten-l5, after rem:tl5-hfx-what; absorption at the bootstrap smallness
    lem:tl5-hfy-abs	paper/reader/proofs/P-GRD8.md@PENDING:10	P-GRD8, Lemma	absorption with k3 s <= x = s1^v sup k3 (<= 1/4): factors 2 -> 1/(1 - x)
    thm:tl5-hfy	paper/reader/proofs/P-GRD8.md@PENDING:32	P-GRD8, Theorem	thm:tl5-hfx with the replaced constants; Step 1 with s <= s1^v
    rem:tl5-hfy-what	paper/reader/proofs/P-GRD8.md@PENDING:43	P-GRD8, Remark	what changes

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hfx-what, add "; points to sec:tl5-hfy
(P-GRD8 item 2)".
