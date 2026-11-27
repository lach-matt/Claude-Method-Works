### The terms with ϱ, sharpened {#sec:tl5-hfw}

In the proofs of [[prop:tl5-hf-bootstrap]] and of all its sharpened forms, the part with ϱ of the nonlinear terms is a
product of the residual with a factor 𝔰 of the solution, and it is bounded there by (1/4) k₂ ϱ through 𝔰 ≤ 1/8. After
Step 1 of those proofs, 𝔰 is at most 𝔰_*^v < 𝔰₁^v on D^κ_s; this section uses that bound instead, at level four and at
level N ≥ 6, which multiplies the coefficient of ϱ in the error ε by 8𝔰₁^v. The closing condition is
[[eq:tl5-hfw-closing]]; the earlier ones remain valid. The notation is that of [[sec:tl5-hfv]].

**Definition {#def:tl5-hfw-constants}** (The constants with the terms with ϱ sharpened.) In the setting of
[[def:tl5-hfv-constants]], let 𝔤_ϱ^v be the factor that multiplies (1/4) k₂ ϱ in ε^v: 𝔤_(ϱ,s) for N ≥ 6 with option (a)
of [[def:tl5-hft-constants]], μ^(−1/2) 𝔤_(𝒥,s) with option (b), and min(𝔤_(ϱ,q), μ^(−1/2) 𝔤_(𝒥,s)) for N = 4. Put

    ε^w := 𝒮[s_N[2R̂ic] + 2𝔰₁^v 𝔤_ϱ^v k₂ ϱ],      A_w^v := η^(−1/2) δ_w + η⁻¹ (ε^w + ε_M^v),            {#eq:tl5-hfw-eps}

and let 𝔰_*^w be 𝔰_*^v with A_w^v in place of A_v.

**Theorem {#thm:tl5-hfw}** (Existence close to an explicit background, with the terms with ϱ sharpened.) In the
setting of [[thm:tl5-hfv]], suppose (a) and (b) of that theorem and (c) η > 0, 𝔰_*^w < 𝔰₁^v and the closing condition

    4 A_w^v B_v = 4 η^(−3/2) (δ_w + η^(−1/2) (ε^w + ε_M^v)) (S_F^v + S_M^v) < 1.                    {#eq:tl5-hfw-closing}

Then the conclusions of [[thm:tl5-hfv]] hold with A_w^v and 𝔰_*^w in place of A_v and 𝔰_*^v.

*Proof.* The proof of [[thm:tl5-hfv]] applies with ε^w, A_w^v and 𝔰_*^w in place of ε^v, A_v and 𝔰_*^v, with one change
in Step 2. Step 1 uses only 𝔰_*^w < 𝔰₁^v and gives 𝔰 ≤ 𝔰_*^w < 𝔰₁^v on D^κ_s. In Step 2, the nonlinear terms of level j
contribute to the bulk a part with 𝒥_g, bounded as there, and a part 2Ω̂² 𝔤_ϱ^v 2k₂ 𝔰 ϱ (√e_o + √c √e_i): in each
monomial the factor bounded by its part with ϱ is multiplied by a factor Φ₁ with |Φ₁| ≤ 𝔰, or, in H^(αβ) D̂_αD̂_βΨ_J, by
H with |H| ≤ 𝔰, as in the proofs of [[lem:tl5-hfs-products]], [[lem:tl5-hft-products]] and [[lem:tl5-hfq-theta]]; the
constant 𝔤_ϱ^v is the one of those proofs. There the bound 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ was used; we use 2k₂ 𝔰 ϱ ≤ 2𝔰₁^v k₂ ϱ,
by Step 1. As in the proof of [[prop:tl5-hf-linear]] this part is bounded by Y_s 𝒮[2𝔰₁^v 𝔤_ϱ^v k₂ ϱ], which with the
forcing term gives Y_s ε^w in place of Y_s ε^v. ∎

**Remark {#rem:tl5-hfw-what}** (The split of the error.) The closing condition [[eq:tl5-hfw-closing]] contains the
residual only through ε^w + ε_M^v, in which s_N[2R̂ic] and ϱ enter by the triangle inequality for 𝒮; any bounds of
𝒮[s_N[2R̂ic]] and of ϱ whose combination keeps [[eq:tl5-hfw-closing]] and the conditions on 𝔯^v and 𝔰_*^w are
admissible, and the theorem does not fix their ratio. The coefficient of ϱ in ε^w is 8𝔰₁^v times that of ε^v, where
𝔰₁^v ≤ 𝔰_♭/2 ≤ 1/16. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfw]] are established in
this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
The earlier sections stay as they are and their closing conditions remain valid; this section is added beside them.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD cb200e34, where sec:tl5-hfv is merged (Section 57.20,
merge 86f3d84e). Line numbers serve only to find the place. Each new text replaces its old text as a whole, with the
line breaks shown.

*1. Where the section goes.* The section above, from its heading ("The terms with ϱ, sharpened", label sec:tl5-hfw)
through the last line of [[rem:tl5-hfw-what]], is inserted at the end of [[ch:ten-l5]], after the last line of
[[rem:tl5-hfv-what]] (line 6254, as changed by item 2), with one blank line before it, as a sibling "###" section. It
cites the earlier sections as they stand and the proof of thm:tl5-hfv with the change it states. It defines the labels
listed in the crosswalk rows, none defined elsewhere. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfv-what]] (lines 6253–6254).* Old:

numbers κ, κ′ of [[def:tl5-wg-domains]] are those of the setting. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfv]] are established in this paper for no background at 10 l5.

New:

numbers κ, κ′ of [[def:tl5-wg-domains]] are those of the setting. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfv]] are established in this paper for no background at 10 l5. [[sec:tl5-hfw]] sharpens the
terms with ϱ ([[thm:tl5-hfw]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text.

*Closing condition (proved, levels 4 and ≥ 6):* 4 η^(−3/2) (δ_w + η^(−1/2)(ε^w + ε_M^v)) (S_F^v + S_M^v) < 1 with η₀ <
𝔰₁^v, 𝔰_*^w < 𝔰₁^v and the rate condition of thm:tl5-hfv.

*The one new factor:* ε^w = 𝒮[s_N[2R̂ic] + 2𝔰₁^v 𝔤_ϱ^v k₂ ϱ], with 𝔤_ϱ^v = min(𝔤_(ϱ,q), μ^(−1/2) 𝔤_(𝒥,s)) at level four
(and 𝔤_(ϱ,s) or μ^(−1/2) 𝔤_(𝒥,s) at level N ≥ 6 by option), against 𝒮[s_N[2R̂ic] + (1/4) 𝔤_ϱ^v k₂ ϱ]. The ratio of the
ϱ coefficients is 8𝔰₁^v: at G0g's values 𝔰₁^q ≈ 10⁻¹⁵…10⁻¹⁸ at level four (from the reports; not recomputed here) this
removes about 14–17 decades from the coefficient that binds ϱ, so that, by G0h's addendum, f binds again.

*The briefed items.* 1–3 (𝔤_(ϱ,q), k₂, 𝒮): unchanged; item 4 answers them: the ϱ part never needed an O(1) coefficient,
as it is quadratic (residual times a low quantity), and the bootstrap's own smallness bounds the second factor. The
split of ε between f and ϱ is free (rem:tl5-hfw-what); the theorem needs only the sum. 𝔯 is not involved.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfw	paper/reader/proofs/P-GRD6.md@PENDING:1	P-GRD6, section	new; at the end of ch:ten-l5, after rem:tl5-hfv-what; the terms with rho bounded through s <= s1 instead of 1/8
    def:tl5-hfw-constants	paper/reader/proofs/P-GRD6.md@PENDING:9	P-GRD6, Definition	eps^w with coefficient 2 s1^v in place of 1/4 on the rho term; A_w^v, s_*^w
    eq:tl5-hfw-eps	paper/reader/proofs/P-GRD6.md@PENDING:13	P-GRD6, display	new
    thm:tl5-hfw	paper/reader/proofs/P-GRD6.md@PENDING:17	P-GRD6, Theorem	thm:tl5-hfv with the terms with rho sharpened; levels 4 and N >= 6
    eq:tl5-hfw-closing	paper/reader/proofs/P-GRD6.md@PENDING:20	P-GRD6, display	closing condition: 4 eta^(-3/2)(delta_w + eta^(-1/2)(eps^w + eps_M))(S_F + S_M) < 1
    rem:tl5-hfw-what	paper/reader/proofs/P-GRD6.md@PENDING:33	P-GRD6, Remark	the split of the error between the residual and rho is free; coefficient ratio 8 s1^v

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hfv-what, add "; points to sec:tl5-hfw
(P-GRD6 item 2)".
