# R-P-G1: independent reading of proofs/P-G1.md (gap G1, chapter 33)

**Verdict: NOT CONFIRMED.** 1 Major, 12 minor, 16 nits.

File read: `proofs/P-G1.md`, md5 1cd8f781545862cce8159aed13a34a31, 942 lines (checked before reading). Chapter 33 was read
as it stands at HEAD (it includes the F2-G24 changes). Line numbers below are P-G1 lines unless marked "33:", "95:" etc.

The mathematics of the new section holds up. The classes, the four-coordinate structure checks, the microsupport calculus,
duality, regularisation, items (a)–(j), Lemma C, Lemma D and the rewritten (5.44)/(5.45) are correct, apart from the points
below. Every new constant was recomputed. The one Major finding is about a source statement: the inclusion (3.38) that the
disjoint-support lemma rests on is misprinted in **both** versions of [Hin26d]. The file says the published version corrects
it, and it does not.

Sources consulted (copies and excerpts are in `.../scratchpad/reader/sources/`):

- [Hin26d] arXiv v1: `Hin26d-arXiv-2408.06651v1.txt`, the full text, with pages taken from the running headers
  (`v1-page-headers.tsv`).
- [Hin26d] published version (Commun. Amer. Math. Soc. 6 (2026) 153–243, the AMS PDF S2692-3688-2026-00058-6): targeted
  verbatim excerpts in `Hin26d-published-AMS-excerpts.txt`. They come from an excerpt-mode web fetch, because the proxy
  refuses ams.org. The earlier partial copy, which stops at Definition 3.23, is `Hin26d-CAMS-published-partial.md`.
- The author's revised manuscript (sites.psu.edu, `sc-bdd-geo-rr.pdf`, 78 pp.; its numbering is the published one):
  excerpts in `Hin26d-author-revised-rr-excerpts.txt`.
- [Hin23d] v1 and v2, and the arXiv abstract page for v2: excerpts read through the same fetch route.
- `proofs/P-G24b.md` does not exist (it is not in `proofs/` or anywhere in the tree), so no overlap check was possible. None
  of the lines F2-G24 changed (33:1096, 1361, 1759–1760, 1822–1823, 1831–1833, 1948, 2372–2374, 2382–2383) lies inside a
  P-G1 anchor.

---

## Major

**M1. (3.38) is misprinted in the published version too. The disjoint-support lemma uses the corrected form without saying
so.** Lines 899–901 (C95-3, (S16)), used at lines 180–181 (lem:iv5-calc-disjoint).

Current text (899–901):

> Finally, WF′^(w_1w_2)_𝒱(A_1 ∘ A_2) ⊂ WF′^(w_1)_𝒱(A_1) ∩ WF′^(w_2)_𝒱(A_2). (3.38) The map A ↦ A* is continuous, and
> the map (A_1, A_2) ↦ A_1 ∘ A_2 is jointly continuous." (The arXiv version prints A_1 in the last place of (3.38); the
> published version prints A_2.)

What is wrong:

- arXiv v1, p. 55, prints "WF′^{w_2}_𝒱(A_1)" in the last place.
- The published Theorem 3.52 prints "WF′^{w_1}_𝒱(A_1) ∩ WF′^{w_2}_𝒱(A_1)". The fetched AMS text renders the same line's
  composition as "(𝐴 1 ∘ 𝐴 2 )", so the last factor is unambiguously A_1. The author's revised manuscript (p. 57) is the
  same.
- So the parenthetical is false, and the quotation, which prints A_2, matches neither version.
- This matters for the mathematics. As printed, (3.38) gives only WF′(A_1A_2) ⊂ WF′(A_1). The proof of
  lem:iv5-calc-disjoint (180–181) needs WF′(Op(c_1)TOp(c_2)) ⊂ ess supp c_1 ∩ ess supp c_2, which needs the right-factor
  inclusion. [Hin26d] states no WF′ rule for adjoints that could supply it.
- Everything built on lem:iv5-calc-disjoint (microsupport, (c), (e), Lemma C, C33-5/-9/-11) therefore rests on a corrected
  reading that no version of the source prints. The writer's report (§3) records the published text wrongly on this point.

Proposed replacement for 899–901:

> Finally, WF′^(w_1w_2)_𝒱(A_1 ∘ A_2) ⊂ WF′^(w_1)_𝒱(A_1) ∩ WF′^(w_2)_𝒱(A_1). (3.38) The map A ↦ A* is continuous, and
> the map (A_1, A_2) ↦ A_1 ∘ A_2 is jointly continuous." Both the arXiv version and the published version print A_1 in
> the last place of (3.38); A_2 is meant. The proof writes Op_𝒱(a_1) ∘ Op_𝒱(a_2) as Op_𝒱(a) plus a residual operator,
> with a given in each chart "with the usual full symbol expansion" [Hin26d, p. 56], whose terms are products of
> derivatives of a_1 and of a_2. The proofs that cite (S16) use (3.38) with A_2 in the last place.

In lem:iv5-calc-disjoint (180–181), replace "so two applications of the wave front set inclusion of [Hin26d, Theorem 3.51]
((S16))" with "so two applications of the wave front set inclusion of [Hin26d, Theorem 3.51], read with A_2 in the last
place of (3.38) ((S16))". Rewrap the line.

Whether the edition may rest a lemma on an editorial correction of a source misprint is the author's decision. The
alternative is a written proof of the right-factor inclusion in the edition: the essential support of the full-symbol
expansion, through [Hin26d, Lemmas 3.30 and 3.41]. That is a larger change.

---

## minor

**m1. The iteration in (e) chooses J too small when s < 0.** Lines 457–460.

Current text: "Let J be an integer with J ≥ s + N, …" and "After J steps the remaining term is at most
Ch^J‖u‖_(wH^(s−J)) ≤ Ch^N‖u‖_(wH^(−N)), as s − J ≤ −N."

What is wrong: the last inequality also needs h^J ≤ h^N, that is J ≥ N. With s < 0, J ≥ s + N allows J < N. For example,
s = −N, J = 0 would claim ‖Bu‖_(H^(−N)) ≤ Ch^N‖u‖_(H^(−N)). The rest of the proof (the step, the strong sense, uniformity in
h) is correct.

Proposed replacement for 457–462, rewrapped:

    *Iteration.* Let J be an integer with J ≥ N + max(s, 0), and choose closed sets K′ = K_0 ⊂ K_1 ⊂ ⋯ ⊂ K_J ⊂ O′, each in
    the interior of the next. Apply the step to BOp(yψ) with σ = s and K″ = K_1, then to the operator Op(φ_3) so obtained
    with σ = s − 1 and K″ = K_2, and so on. After J steps the remaining term is at most Ch^J‖u‖_(wH^(s−J)) ≤
    Ch^N‖u‖_(wH^(−N)), as J ≥ N and s − J ≤ −N. This gives [[eq:iv5-calc-ell]]. Each identity B′u = B′Op(φ_1q)GAu +
    hB′R_1Op(φ_3)u + R′u holds for u ∈ wH^(−N), all terms being defined by (d); if GAu ∈ ww′H^(s−m), then, going back from
    the last step, each Op(φ_3)u lies in wH^(σ−1), and so Bu ∈ wH^s.

**m2. In the eb case of property (D), the cut-off ψ_R does not give compact support in M°.** Lines 248–249.

Current text: "Now ψ_Rv_ε ∈ C_c^∞(Ω), and it tends to v as R → ∞ and then ε → 0. The case of M° is the same, with the charts of
ℬ_eb, in which {t > 0} is {T > −k}. ∎"

What is wrong: M° = ℝ_t × (ℝ⁴ ∖ 0). The function ψ_R(t, x) = ψ(t/R)ψ(|x|/R) equals 1 near r = 0, so ψ_Rv_ε is not
compactly supported in M°. The eb duality (lem:iv5-calc-dual, last paragraph; C33-19/20) uses this case.

Proposed replacement:

> … Now ψ_Rv_ε ∈ C_c^∞(Ω), and it tends to v as R → ∞ and then ε → 0. The case of M° is the same, with the charts of
> ℬ_eb, in which {t > 0} is {T > −k}, and with ψ_R(t, x) := ψ(t/R)ψ(|x|/R)(1 − ψ(R|x|)), which has compact support in M°
> and is bounded in C^∞_(uni,ℬ_eb) uniformly in R, as |x| ≤ CR on supp ψ(|x|/R) and R|x| ≤ C on supp ψ′(R|x|). ∎

(Check: r∂_tψ(t/R) = (r/R)ψ′ and r∂_r(1 − ψ(Rr)) = −Rrψ′(Rr) are bounded, and ψ_Rf = f for f ∈ C_c^∞(M°) once R is
large.)

**m3. The (S7) quotation silently corrects the source's subscripts.** Line 871 (C95-2).

Current text: "…but the norm of Au is bounded from below by the w_(p_0)w′_(p_0)H^(s−m)_(𝒱_(p_0))(M)-norm of A_(p_0)u_(p_0).)"

What is wrong: v1 (p. 59) and the published text both print "w_pw′_pH^(s−m)_(𝒱_p)(M)-norm of A_(p_0)u_(p_0)".

Proposed replacement: "…bounded from below by the w_pw′_pH^(s−m)_(𝒱_p)(M)-norm of A_(p_0)u_(p_0).)" To flag the slip, add
after the closing quotation mark: "(the subscripts p of that norm stand for p_0)".

**m4. The numbering note in C95-3 maps Sections 1 and 3 only.** Lines 903–908.

(S1)–(S15) also cite Section 2 items (Proposition 2.3, (S15)) and Section 4 items ((S8)–(S11), (S15)), and both sections
are renumbered in the published version. Evidence from the published text:

- Definition 3.25 cites "Definition 2.9" and "Proposition 2.10"; these are v1 2.7 and 2.8.
- Lemma 2.8 (Refinement) is v1 Lemma 2.6.
- Proposition 4.19 (Fourier transform: constant orders) is v1 Proposition 4.18.
- Definition 4.21 is v1 Definition 4.20.
- (4.25a) is v1 (4.24a).

From the author's revised manuscript: Proposition 2.4 is the metric of v1 Proposition 2.3, and Proposition 4.23 with
(4.26) and (4.29) is v1 Proposition 4.22 with (4.25) and (4.28).

A reader of the note will assume that unmentioned numbers are unchanged. Proposed addition after "footnote 13 is footnote
22.":

> This list covers Sections 1 and 3 only; Sections 2 and 4 are renumbered as well (for instance, Proposition 2.3,
> Propositions 4.17, 4.18 and 4.22, Definition 4.20 and (4.24a–b) are Proposition 2.4, Propositions 4.18, 4.19 and 4.23,
> Definition 4.21 and (4.25a–b) there).

The rest of the note is right. Lemma 3.24 (1), Definition 3.25 and Lemma 3.28 keep their numbers; this is now checked
directly in the published text, not inferred. The shift by one in Section 3 is confirmed (published Remark 3.38 = v1 3.37,
Definition 3.44, Theorems 3.45 and 3.52, Remarks 3.47, 3.48 and 3.57, Proposition 3.56, Definitions 3.59 and 3.60 and 3.62,
footnote 22). The shift actually starts one item earlier, at v1 Lemma 3.36 = published Lemma 3.37 (nit n13).

**m5. The crosswalk insertion point breaks the chapter order.** Line 927.

Current text: "The row of prop:np-10-65-a is replaced; the other rows are added after it, with the columns of the chapter's rows."

What is wrong: the row of prop:np-10-65-a now sits after def:iv5-0-1. After C33-3 and C33-4 the label lives inside
sec:iv5-calc, after lem:iv5-0-5, and the fourteen rows list prop:np-10-65-a ninth. Integration checks that crosswalk rows
follow the chapter's label order (INTEGRATION.md).

Proposed replacement:

> The row of prop:np-10-65-a (after the row of def:iv5-0-1) is deleted, and the fourteen rows below are inserted, in this
> order, after the row of lem:iv5-0-5 and before the row of sec:iv5-1, with the columns of the chapter's rows.

**m6. The new definition of o conflicts with the Notation paragraph, and subsets of ³ᵇT̄*M₀ are never placed in ∂_ħ.**
Line 146 (def:iv5-calc-micro).

Current text: "…where ³ᵇS*M₀ is fibre infinity, and let o := {0} × (zero section). A family of symbols…"

What is wrong:

- The Notation paragraph (33:1391), which precedes the new section, says "o is the zero section". The chapter uses o in
  that sense, for all h ("j vanishes cubically at o", "f is supported off o").
- The new definition of o is used nowhere in the section.
- The chapter's conditions "WF′(B_j) ∩ (o ∪ ∂Σ) = ∅", "elliptic at ∂Σ", "WF′(B_0) ⊂ {…, |ζ| < 1}" and "Ell(E) ⊃ {…}" need
  a rule placing subsets of ³ᵇT̄*M₀ in ∂_ħ. The rule that reproduces lem:iv5-1-1 is {0} × o for o and [0, 1] × ∂Σ for ∂Σ.

Proposed replacement for "and let o := {0} × (zero section)." (rewrap the paragraph):

> . In statements about WF′ and Ell, a subset S of ³ᵇT̄*M₀, such as the zero section o or the set ∂Σ of the notation
> above, or a set described by a condition |ζ| < 1, stands for ({0} × S) ∪ ([0, 1] × (S ∩ ³ᵇS*M₀)) ⊂ ∂_ħ.

**m7. Three lines of C33-11 start with "|".** Lines 683, 688, 689 (C33-11 new text): "|q₁₀(z, ζ)| ≤ C₂|ζ|² …",
"|ã²q₁₀| ≤ 9C₂𝔛⁻² everywhere. …" and "|⟨Ã*TÃAω, Aω⟩| ≤ …".

Proposed replacement for 681–691, the paragraph *The term with Q_1* up to "Hence". The text is unchanged except for n3; every
line is ≤ 121 characters, also after resolution:

    *The term with Q_1* ([Hin26a, (5.45)]). T := h²Q_1 ∈ ρ_sf²Ψ²_(3b,ħ) is self-adjoint, and its principal symbol q₁₀ is the
    principal symbol of Q_1 evaluated at ζ, homogeneous of degree 2 ([[prop:np-10-65-a]] (a)). So |q₁₀(z, ζ)| ≤ C₂|ζ|² over a
    fixed neighbourhood V of K, where C₂ is the supremum of |q₁₀| over the unit sphere bundle above V, independent of 𝔛. Let
    ã := χ̃(𝔛|ζ|)φ(z), with χ̃ ∈ C_c^∞((−3, 3)), 0 ≤ χ̃ ≤ 1, χ̃ = 1 on [−5/2, 5/2], and φ ∈ C^∞(M₀), 0 ≤ φ ≤ 1, equal to 1
    near K and supported in V; put Ã := Op(ã). As χ_0 is supported in (−2, 2), A may be taken microsupported in a closed set
    near which ã = 1; then (I − Ã)A = Op(1 − ã)A lies in h^∞Ψ^(−∞)_(3b,ħ) ([[def:iv5-calc-micro]]). The self-adjoint operator
    Ã*TÃ has principal symbol ã²q₁₀, and |ã²q₁₀| ≤ 9C₂𝔛⁻² everywhere. [[lem:iv5-calc-garding]] (a), applied with η := 𝔛⁻² to
    Ã*TÃ and to −Ã*TÃ, gives |⟨Ã*TÃAω, Aω⟩| ≤ ((9C₂ + 1)𝔛⁻² + C_𝔛h)‖Aω‖². The difference ⟨TAω, Aω⟩ − ⟨Ã*TÃAω, Aω⟩ is a sum of
    three terms, each containing (I − Ã)Aω = (I − Ã)Aχω, whose norm in every H^k_(3b,h) is
    O(h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h))) ([[prop:np-10-65-a]] (d)); so it is at most 𝔛⁻²‖Aω‖² +
    C_(𝔛,N)h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h)). Hence

**m8. Placed in context, eight new texts give lines over 121 characters.**

Several old texts begin or end inside a chapter line, and the new texts are wrapped as if they stood alone. After
substitution the following lines are too long (raw / after resolution):

- C33-5: 127 / 124
- C33-6: 126 / 126 and 134 / 136
- C33-8: 174 / 172
- C33-9: 132 / 131
- C33-12: 133 / 130
- C33-18: 141 / 121 and 171 / 159
- C33-19: 185 / 179
- C95-1: chapter lines 851 and 852 become 124 and 122 raw

The Placement preamble mentions line breaks but asks for no rewrap. Proposed fix: add to the preamble "After each
replacement, the paragraph is rewrapped to lines of at most 121 characters". Or give the full lines, as below. The old text
is the full chapter lines; every new line is ≤ 121.

C33-5 (33:1418–1420):

    χ_(τ,2)χ_(r,2)ω = χ_(τ,2)χ_(r,2)ω′. By [[lem:iv5-1-1]], ρ_sf⁻²P_h is elliptic on WF′(B_1), and B_1χ_(τ,1)χ_(r,1) is
    elliptic on WF′(B_0χ_(τ,2)χ_(r,2)), as χ_(•,1) = 1 near supp χ_(•,2) ([[lem:iv5-calc-disjoint]] (b), (c)). So
    [[prop:np-10-65-a]] (e), applied to ω′ with A := P_h ∈ ρ_sf²Ψ²_(3b,ħ), G := B_1χ_(τ,1)χ_(r,1) and B := B_0χ_(τ,2)χ_(r,2),
    gives the estimate, in the weighted spaces and in the strong sense. For P_h* the proof is the same, its principal symbol
    being G + iℓ. ∎

C33-6 (33:1437–1438; the rest of the paragraph from 33:1439 is unchanged):

    *Proof.* We prove [Hin26a, (5.21)] for ω ∈ H^(s,(α_sf,α_K))_(3b,h). The strong sense follows by running the same argument
    with the commutant aj_ε, j_ε := ⟨εζ⟩^(−K) as in [[lem:iv5-calc-reg]] with K so large that every pairing below is finite
    when the right side of [[eq:iv5-fib]] is. By [[lem:iv5-calc-reg]] (c), H_G(aj_ε) = j_εH_Ga + ϑ_εj_εae_G, so the terms in
    which j_ε is differentiated are bounded multiples of a²j_ε², uniformly in ε, like the terms in which the weights are
    differentiated; they join the term hAB̃_2A below and are absorbed in the same way. The estimate then holds with
    B_0χ_(τ,2)χ_(r,2)ω replaced by J_εB_0χ_(τ,2)χ_(r,2)ω, J_ε := Op(j_ε), with a constant independent of ε. As ε → 0,
    J_εB_0χ_(τ,2)χ_(r,2)ω tends to B_0χ_(τ,2)χ_(r,2)ω in H^(−N,(α_sf,α_K))_(3b,h) ([[lem:iv5-calc-reg]] (b)) and is bounded
    in H^(s,(α_sf,α_K))_(3b,h); a weakly convergent subsequence identifies the limit, which therefore lies in
    H^(s,(α_sf,α_K))_(3b,h) and satisfies the estimate. By [[prop:iv5-1-2]] it suffices to work in an h-independent
    neighbourhood of ∂Σ_±;

C33-8 (33:1451):

    subprincipal, □_h having real scalar principal symbol. With the square roots of [[prop:np-10-65-a]] (f) and the rules of
    [[prop:np-10-65-a]] (b), this gives [Hin26a, (5.26)], with E microsupported near supp a ([[lem:iv5-calc-disjoint]] (b)):

C33-9 (33:1463):

    of the main term, and absorb h⟨B̃_2Aω, Aω⟩ ≤ Ch‖B̃_0Aω‖² + h^N‖ω‖², which holds by [[prop:np-10-65-a]] (e), B̃_0 being
    elliptic on a neighbourhood of supp a in which A is microsupported. Iterate in h^(1/2) on the error term

C33-12 (33:1533):

    [[lem:iv5-0-5]] (6) on supp ψ′. Q enters with a lower bound, the adjoint pairing containing +h⁻¹⟨AQAω, ω⟩:
    h⟨Q_0Aω, Aω⟩ ≥ −Ch‖Aω‖² by [[lem:iv5-calc-q0]], and ⟨h²Q_1Aω, Aω⟩ ≥ −((9C₂ + 2)𝔛⁻² + C_𝔛h)‖Aω‖² − C_(𝔛,N)h^(2N)‖χω‖²
    as in (1), by [[lem:iv5-calc-garding]] applied to −Ã*h²Q_1Ã. The iteration is the same. ∎

C33-18 (33:2157–2159; see also n6):

    hence independently of b. The calculus facts used ([[prop:np-10-65-a]], [[lem:iv5-calc-garding]] and [[lem:iv5-calc-q0]])
    hold with constants uniform in b by [[prop:np-10-65-a]] (j): the coefficients of P_h and of Q_0, Q_1, the symbols of the
    commutants, of their square roots and of the auxiliary operators, the ellipticity bounds and the positivity margins are
    bounded uniformly for b ∈ U. In particular the margin 9C₂ + 2 in the proof of [[prop:iv5-2-1]] is uniform, C₂ being the
    supremum of a symbol continuous in b over a compact set, and for each fixed 𝔛 the constant C_𝔛 is uniform, the square
    root in [[lem:iv5-calc-garding]] having the margin η = 𝔛⁻² for every b. Each absorption step needs h below a threshold
    determined by these quantities. So each h_0 and C is

C33-19 (33:2430–2431):

    (2^j(k − 2), 2^j(k + 2))_t × (2^(j−2), 2^(j+2))_r × U̸_β, with U̸_β charts of 𝕊³, give the parameterised scaled bounded
    geometry of [[def:iv5-calc-cells]], and [[prop:np-10-65-a]] (i) gives the semiclassical eb-calculus. On it
    P_h := h²□^C = □_h − iL_h ∈ r⁻²Diff²_(eb,ħ)(M; 𝒯*) has principal symbol G − iℓ

C95-1 (95:851–853). This version also adds (3.38), which (S16) cites, to the list of displays:

    **Theorem {#thm:std-sbg-calculus}** ([Hin26d, Definitions 1.1–4.20, Lemmas 3.20, 3.24, 3.28 and 3.42,
    Propositions 2.3–4.22, Remarks 3.13–3.56, Theorems 3.21–3.52, footnote 13, (1.6), (2.3), (2.5), (3.2), (3.26), (3.28),
    (3.38), (4.24a–b), (4.27), (4.28), pp. 2–75].) On a smooth manifold M of any dimension n, without boundary, the
    following hold.

**m9. The optional C23-1 narrows (S7), and (S7) is cited at sites the file does not consider.** Lines 820–821.

Current text: "The uses of (S7) in [[lem:ii-a-7-1]] (a parametrix to finite order, uniformly in σ) need only compositions and
principal symbols, which this covers."

What is wrong: the new (S7) drops the old words "the above holds uniformly in p". (S7) is also cited at:

- 27:444: the proof of lem:ii-f-2-2, which is stated "Uniformly for h ∈ (0, 1]". Its (a), boundedness, is covered. Its (c),
  a microlocal elliptic estimate whose proof (27:460) cites (S5), relied on the old wording.
- 37:824: uniform equivalence of norms on a compact set of σ, which p. 59 does not state.

Proposed replacement:

> (S7) is cited at 23:778 (the proof of [[lem:ii-a-7-1]]: compositions, principal symbols and boundedness, covered by the
> new text), at 27:444 (the proof of [[lem:ii-f-2-2]]: its (a) is covered, while its (c), an elliptic estimate asserted
> uniformly in h, used the old words "the above holds uniformly in p") and at 37:824 (uniform equivalence of norms, not a
> statement of p. 59). C23-1 is to be applied only together with a check of 27:460 and 37:824. The uniformity there can be
> obtained by the reduction in the proof of [[prop:np-10-65-a]] (statements on P′ × M for countable P′).

**m10. Source numbers appear in the edition text without "[Hin26d, …]".** They can be read as the edition's own numbers;
the edition prints its displays as "(24.n)" and its results as "Definition 24.n".

- Line 36, "((S7), with footnote 13)": replace with "((S7), with [Hin26d, footnote 13])".
- Line 88, "condition (1.6)": replace with "condition [Hin26d, (1.6)]".
- Line 121, "the sufficient condition after Definition 3.58": replace with "the sufficient condition after [Hin26d,
  Definition 3.58]".
- Line 175, "((S16), Lemma 3.24 (1))": replace with "([Hin26d, Lemma 3.24 (1)], (S16))".
- Line 176, "((S16), Definition 3.25)": replace with "([Hin26d, Definition 3.25], (S16))".
- Lines 213 and 233, "by (3.14)" and "By (3.14)": replace with "by [Hin26d, (3.14)] ([[rem:std-sbg-sobolev]])".
- Lines 125 and 538, "By (3.14) ([[rem:std-sbg-sobolev]])" and "by (3.14) ([[rem:std-sbg-sobolev]])": write
  "[Hin26d, (3.14)]".

Rewrap the affected lines.

**m11. Multiplication by w is not an isometry.** Line 279 (proof of lem:iv5-calc-dual).

Current text: "multiplication by w is an isometry of H^s_(𝒱_h) onto wH^s_(𝒱_h) that preserves supports".

What is wrong: the norm of wH^s_𝒱 is [Hin26d, (3.14)], with a weight family. Multiplication by w is an isomorphism with
equivalent norms, not an isometry.

Proposed replacement: "multiplication by w is an isomorphism of H^s_(𝒱_h) onto wH^s_(𝒱_h), with bounds independent of h
((S3), (S7)), that preserves supports". Rewrap lines 279–280.

**m12. Some (S…) items are cited for content that only the list in chapter 23 states.** Lines 35, 117 and 399–400.

The section anchors (S4) and (S14) to [[thm:std-sbg-calculus]] (line 35) and cites (S16), which exists only there. But two
items are used for content stated only in the list of [[sec:ii-a-3]]:

- Line 117, "By (S2), w > 0 is a weight if Ww/w is bounded…": Appendix A's (S2) is only "Weights [Hin26d, Definitions 3.4 and
  3.6, pp. 29–30]."
- Line 399, "In the local quantisation of (S4) the symbol is evaluated at the left variable … and the χ_α of (S4) sum to 1":
  Appendix A's (S4) does not display (3.26) or the partition of unity.

Chapter 23 also says "Later chapters cite them as (S1)–(S15)". Proposed addition at the end of the first paragraph (after
line 11):

> Below, (S1)–(S15) are the items of [[sec:ii-a-3]], which [[thm:std-sbg-calculus]] repeats with quotations under the same
> numbers, and (S16) is the item of [[thm:std-sbg-calculus]].

---

## nits

- **n1** (line 5). "No Gårding inequality is used." Lemma C is a Gårding-type bound, and its label and crosswalk call it
  Gårding. Replace with "The sharp Gårding inequality is not used."
- **n2** (line 513). Current text: "[[lem:iv5-calc-garding]] is the semiclassical form of [[lem:ii-a1-2-6]]: the remainder of
  order −1 there becomes a remainder of size O(h) here." That lemma bounds ‖Op(z)v‖², not Re⟨Tv, v⟩, and its remainder has
  order −1 + 2δ. Replacement:

  > [[lem:iv5-calc-garding]] is a semiclassical analogue of [[lem:ii-a1-2-6]], stated for Re⟨Tv, v⟩ rather than
  > for ‖Op(z)v‖²: the remainder of order −1 + 2δ there becomes a remainder of size O(h) here.

- **n3** (line 687). "(I − Ã)A = Op(1 − ã)A lies in h^∞Ψ^(−∞)_(3b,ħ) ([[lem:iv5-calc-disjoint]])": this is the definition
  of microsupport. Cite [[def:iv5-calc-micro]]; the m7 text already does.
- **n4** (line 700). "the coefficient of ‖Aω‖² is at most −c_0 + (9C₂ + 2)𝔛⁻² + C′_𝔛h". Counting the ¼c_0 from the
  Cauchy–Schwarz step, the net coefficient is −¾c_0 + …. Write "−¾c_0" or "at most −½c_0 for 𝔛 large and h small".
- **n5** (line 679). "[[lem:iv5-calc-q0]] gives −h⟨Q_0Aω, Aω⟩ ≤ Ch‖Aω‖²": add "with w = 1", which is the reading that the
  remark "near K, ρ_sf lies between two positive constants" supports.
- **n6** (line 777). "In particular the margin 9C₂ + 2": replace with "the constant 9C₂ + 2"; η is the margin.
- **n7** (lines 150, 499, 517). Clashing letters:
  - Lemma C's "c := (M + η − t_R)^(1/2)" clashes with the 1-form c and with the constant c of (f). Suggest θ_η and
    Θ_η := Op(θ_η).
  - Lemma D's "U ⊂ M₀ open" and the neighbourhood "U in 𝒫" of def:iv5-calc-micro clash with U ⊂ ℬ, which (j) also uses.
    Suggest 𝒪 and 𝒰.
- **n8** (line 374). (f): "for φ ∈ C^∞(𝒫) supported in W" should say "for real φ"; (φq^(1/2))^(*_B)φq^(1/2) = φ²q needs φ
  real.
- **n9** (lines 238–240, writer's point 1). The H^s(ℝ⁵) facts (multipliers, and diffeomorphisms bounded in C^∞, on a fixed
  compact set) are classical and are used at the same level in lem:ii-a-7-d. This is acceptable as is; a textbook citation
  is optional.
- **n10** (line 897). "Theorem 3.51, whose first part is quoted in (S5)": Appendix A's (S5) paraphrases Theorem 3.51.
  Write "whose first part is stated in (S5)".
- **n11** (line 896). The quoted exact sequence drops the arrow label σ^m_𝒱 of the source. Write
  "wΨ^m_𝒱(M) →^(σ^m_𝒱) wS^m…" or mark the omission.
- **n12** (line 851). "and continues: "Furthermore, …"": two sentences of the source lie between ("We define parameterized
  bounded geometry structures analogously. This includes scaled b.g. structures as the special case when P is a singleton
  set."). Write "and two sentences later states:".
- **n13** (line 905). "from Remark 3.37 to Definition 3.61 each number is increased by one" is true. But the shift starts at
  v1 Lemma 3.36 (published Lemma 3.37, "Schwartz kernels of residual operators"), so "from Lemma 3.36" is more precise.
- **n14** (line 919). C98-1 writes "Ars Inven. Anal. (2026), Paper No. 5", while [Usu26] (98:182) writes "Ars Inven. Anal.
  2026, Paper No. 4". Match: "Ars Inven. Anal. 2026, Paper No. 5, 159 pp. doi:10.15781/yw47vq75 arXiv:2302.13803v2". The
  data themselves are correct.
- **n15** (lines 929–942). The rows give "paper/reader/proofs/P-G1.md:N" without the @commit and line ranges of the
  convention (for example "P-A3-every-h.md@0a8a4fa:155-198"). The changed rows get no "G1: …" note, unlike the F-G24 rows:
  def:iv5-0-1, prop:iv5-1-2, prop:iv5-1-3, prop:iv5-2-1, prop:iv5-3-1, prop:iv5-4-1, prop:iv5-5-2, prop:iv5-7-1,
  thm:iv5-7-3, lem:iv5-8-1, sec:iv6-2 and thm:iv6-2-1.
- **n16** (line 345). (a) lists "the cut-offs χ_(τ,j), χ_(r,j)" as elements of the calculus. χ_(τ,j)(t/r) is not smooth at
  t = r = 0 on M₀, and only the products χ_(τ,j)χ_(r,j′) are used. Write "to the products χ_(τ,j)χ_(r,j′) of the cut-offs
  and to χ_(r,j)".

---

## Writer's open points

1. **Standard H^s(ℝ⁵) facts in lem:iv5-calc-d.** Acceptable. They are classical, and chapter 23 (lem:ii-a-7-d) uses them
   the same way. One of them, Σ_α‖w_α‖² ≈ ‖v‖², even follows from the p. 36 statement on cut-off families quoted in
   rem:std-sbg-sobolev. A citation is optional (n9).
2. **Generality of lem:ii-a-7-1.** Fine. Its parametrix "as in lem:ii-a-8-4 (b), with I in place of B" uses only the
   composition calculus, the principal symbol sequence and an elliptic symbol of order 𝗌. All three exist in any
   (parameterised) scaled b.g. structure; for the 3b- and eb-structures the elliptic symbol is ρ_∞^(−s), by
   lem:iv5-calc-structure (d). For constant orders, density is [Hin26d, Lemma 3.20]. Nothing there is specific to e3b.
3. **The strong-sense paragraph C33-6.** Acceptable at the rigour of the surrounding proof:
   - H_G(aj_ε) = j_εH_Ga + ϑ_εj_εae_G is right (lem:iv5-calc-reg (c)).
   - The j_ε-terms carry the factor h, as the weight terms do, and are bounded in the same symbol class uniformly in ε.
   - The weak-limit step is standard.
   - The one compressed step is "the estimate then holds with … replaced by J_εB_0χ_(τ,2)χ_(r,2)ω". That step needs (e) and
     the iteration, as in the unregularised proof.
4. **Dependence on lem:iv5-0-4's positivity sentence.** The sentence is still present at 33:1362–1364; F2-G24 changed only
   "(g, c, e)" to "(g, rc, e)" at 33:1361. C33-11 and C33-13 use it correctly. C33-20's "as in lem:iv5-0-4" is a
   transposition to the Minkowski model. It holds because there r²G and r²ℓ depend on the angle only, and the existing
   sec:iv6-2 already presupposes it.

---

## Verified and found correct

**The new section (lines 1–545), step by step.**

- **def:iv5-calc-cells.** Both chart families map onto (−2, 2)⁵. The cover has every coordinate at most ½. Multiplicity is
  at most 4 per index. The N_(P′) structure is a scaled b.g. structure. The P′ × M class definition is coherent, and the
  "seminorms bounded independently of P′" argument holds.
- **lem:iv5-calc-structure (a)–(d).**
  - The transitions T′, X′ and Ω̃′ are recomputed.
  - |x| < 7|x^i|; |k − k′| ≤ 7 (in fact ≤ 6); |Ω̃_(i′)| ≥ 2^(k′−k−4); 2^(k−k′)j − j′ ∈ 2^(−7)ℤ is bounded.
  - ∂_T, ∂_X, ∂_(Ω_a) and their inverses are recomputed, as is ⟨x⟩/|x^i| ∈ [1, 11] (the true bound is about 8.1).
  - The b-fields near 𝗌𝖿, K⁺ and K⁺ ∩ 𝗌𝖿 for M₀, and near 𝖼𝖿 and 𝖼𝖿 ∩ 𝗌𝖿 for M, are recomputed.
  - Weights; the density (ln 2)2^k|x^i|⁴|dT dX dΩ|; H⁰ ≈ L²(B) uniformly in h through the h^(−5) of the dilation; the
    chain-rule symbol estimates through ξ = C_α(y)ζ.
- **def:iv5-calc-micro.** The independence of Ell from the representative (hρ_∞ → 0 on ∂_ħ).
- **lem:iv5-calc-disjoint.**
  - The Urysohn argument with j(y) is checked against [Hin26d, Definition 3.25 and Lemma 3.24 (1)].
  - Lemma 3.28 is applied on N_(P′), where ρ̄ = h.
  - The two-sided ideal property (b), the intersection argument (c) (the compactness construction of y_1, y_2 checked) and
    (d). The one caveat is M1.
- **lem:iv5-calc-d.**
  - The modified structure for Ω₃: kept charts cover {|x| > R₁}, since 2^(k−2) > R₁/42 > R₁/56 > R₀.
  - The product form of Ω in each chart; the cone Γ (every Y ∈ Γ ∖ 0 has Y_T > 0 > Y_1).
  - The sum bound ‖Σg_α‖² ≤ LΣ‖g_α‖²; the identity w_α = m_α(φ_α)_*(φ_α^*χv); the Fourier multiplier ϱ̂(εξ) − 1; dominated
    convergence; ψ_R on M₀°. The exception is m2 for M°.
- **lem:iv5-calc-dual.**
  - The identity ⟨u, v⟩ = ∫(B̂Iu)·(Iv)‾μ_h; μ_h is a uniformly positive 𝒱_h-density.
  - (a): cl Ω₁ ∖ Ω₂ = cl Ω₃, and both property-(D) steps.
  - (b): both directions match the two statements of lem:ii-a-7-3 (3) with −s for 𝗌 (the closed kernel and Hahn–Banach
    checked).
- **lem:iv5-calc-reg.**
  - Uniform S⁰ bounds through ε⟨ξ⟩ ≤ ⟨εξ⟩.
  - ‖(J_ε − I)u‖ ≤ Cε^δ‖u‖_(s+δ), giving strong convergence.
  - H_pj_ε = ϑ_εj_εe_p, with ϑ_ε = ε²⟨ζ⟩²⟨εζ⟩^(−2) = 1 − (1 − ε²)⟨εζ⟩^(−2) ∈ [ε², 1].
  - e_p ∈ wS^(m−1).
  - The principal symbol H_pj_ε of h⁻¹i[P, J_ε], via (b) and antisymmetry.
- **prop:np-10-65-a (a)–(j).**
  - (a) Op(f) = f from the left quantisation and the partition of unity of v1 Definition 3.31; the Diff membership through
    the p. 59 characterisation.
  - (b) A* = (⟨x⟩⁵B̂)⁻¹A^⋆(⟨x⟩⁵B̂) (the h⁵ factors cancel), so a^(*_B) = B̂⁻¹a^⋆B̂. The covector scaling gives the factor h,
    and h⁻¹i[A_1, A_2] has symbol H_(a_1)a_2 + i[e, a_2].
  - (c) A = ψOp(y)·½(Op(a) + Op(a)*)·Op(y)*ψ.
  - (d) Proved by Theorem 3.44 on N_(P′).
  - (e) The cover O′ and the bound for (ga)⁻¹; the reduction to K′ ⊂ O′; q ∈ w′⁻¹S^(−m); R_1 ∈ Ψ^(−1) and its microsupport;
    the identity B′ = B′Op(φ_1q)GA + hB′R_1Op(φ_3) + R′; the iteration and the strong sense, uniform in h. The exception
    is m1.
  - (f) The resolvent contour and |(z − q̂)⁻¹| ≤ 2/c.
  - (i), (j).
- **Lemma C.**
  - R := (M + η)I − ½(T + T*) − C₀*C₀ ∈ hΨ^(−1).
  - The pairing gives (M + η)‖v‖² − Re⟨Tv, v⟩ ≥ −Ch‖v‖²_(−1/2).
  - (b) through w⁻¹Tw⁻¹.
- **Lemma D.**
  - B((q_* + 1)v, v) ≥ min(c, 1)⟨ζ⟩²B(v, v).
  - ⟨φ²Op(q)u, u⟩ = ⟨Op(q)u, u⟩ and ⟨(1 − φ²)Op(|ζ|²)u, u⟩ = 0.
  - ⟨Q̃u, u⟩ = ‖Θu‖² − ‖u‖² + ⟨Ru, u⟩, interpolation with ⟨ξ⟩ ≤ ε⟨ξ⟩² + (4ε)⁻¹, and ε = (4C₁C₂²)⁻¹ gives
    ½‖Θu‖² − C‖u‖².
- **C33-11.**
  - −h⁻¹⟨AQAω, ω⟩ = −h⟨Q_0Aω, Aω⟩ − ⟨h²Q_1Aω, Aω⟩.
  - Q_0 and Q_1 are h-independent and symmetric, and ρ_sf⁻²(G + Cρ_sf⁻²ℓ²) = ρ_sf⁻²G + C(ρ_sf⁻²ℓ)².
  - |ã²q₁₀| ≤ 9C₂𝔛⁻² on supp ã, where 𝔛|ζ| < 3.
  - Lemma C with M = 9C₂𝔛⁻² and η = 𝔛⁻², applied to ±Ã*TÃ ∈ Ψ⁰, gives (9C₂ + 1)𝔛⁻². The three-term difference adds
    𝔛⁻²‖Aω‖² + C_(𝔛,N)h^(2N)‖χω‖², for a total of 9C₂ + 2.
  - This matches [Hin26a, (5.45)] with 2C replaced, as [Hin26a] (read in `hin26a-v2-fulltext.txt`) prints
    "(2C𝔛⁻² + C_𝔛h)‖Aω‖²".
  - C₂ is independent of 𝔛, and uniformity in b holds through (j) (C33-18).
  - C33-12, C33-13 (Lemma D with w = ρ_sf; Lemma C (b)), C33-14, C33-15 and C33-20 are consistent with it.
- **Other placements.** C33-5 (the hypotheses of (e) from WF′(B_0) ⊂ Ell(B_1), WF′(B_j) ∩ (o ∪ ∂Σ) = ∅ and
  lem:iv5-calc-disjoint (c); G + iℓ for P_h*), C33-7, -8, -9, -10, -16, -17 (the weights pair correctly), -18 and -19 are
  correct in context.
- **Typography.** 8 proofs and 8 ∎. Labels lowercase. No lint hits in lines 1–545 other than cross-chapter labels, all of
  which exist. No line of the file exceeds 121 characters before or after resolution; the in-context exceptions are m8.

**Placement anchors.** Every old text occurs exactly once in the current chapter 33, compared after normalising whitespace.
The text of C33-3 is found at 33:1285–1291 and the heading of C33-4 at 33:1395. Line estimates are within 3. Every old text
for chapter 23 (367), Appendix A (851, 893, and the (S15) end words before rem:std-sbg-sobolev) and chapter 98 (76) also
occurs exactly once. The only other labelled references to prop:np-10-65-a are those C33-1 and C33-19 replace.

**Crosswalk rows.** 14 rows with 4 tab-separated fields; labels and line numbers match the file. Exceptions: m5 and n15.

**[Hin26d] v1, all at the stated pages.**

- Definition 1.9, p. 9: the quoted "so that … uniform also in p ∈ P" and "Furthermore, … ρ_(α_h,i) = h for h ∈ (0, 1]."
  (n12).
- p. 58: "with P given the discrete topology".
- Remark 3.56, p. 58, verbatim.
- Definition 3.58, p. 59, and the sufficient condition after it, verbatim.
- Definition 3.59, p. 59, verbatim.
- The boundedness paragraph, verbatim except m3, including "Theorem 3.44" and "Theorem 3.51 carry over verbatim".
- Footnote 13, p. 59, verbatim.
- The Diff characterisation, p. 59, verbatim.
- Lemma 3.20, p. 38, verbatim.
- Lemma 3.24 (1), p. 40, verbatim.
- Definition 3.25, p. 41: the extension map, the locus {j(λρ) = 0} and the essential support with ⋂_(m,l) wρ^lS^m, all
  verbatim.
- Lemma 3.28, p. 42, verbatim.
- Definition 3.43, p. 51: the principal symbol, WF′ and the exact sequence (n11).
- Theorem 3.51, p. 55: the commutator sentence verbatim; (3.38) as in M1; the continuity sentence verbatim.

**[Hin26d] published.**

- Theorem 3.52 has (3.38) with A_1 in the last place (M1).
- Lemma 3.24 (1) is identical.
- Definition 3.25 keeps its number. Its text adds "= 𝔲𝒱T*M ∩ ({j(λ) = 0} ∪ {j(ρ̄) = 0})" and cites Definition 2.9 and
  Proposition 2.10.
- Lemma 3.28 is identical, with (3.22).
- Definition 3.44 (citing "Definitions 3.31 and 3.34"), Theorem 3.45, Lemma 3.37, Remark 3.38, Proposition 3.56,
  Remark 3.57 and footnote 22 are as the note maps them.
- The boundedness paragraph still prints w_pw′_p (m3).
- Definition 4.6 keeps its number; Proposition 4.19, Definition 4.21 and (4.25a) are shifted (m4).
- The bibliographic data of C98-1 and of [Hin26d] (CAMS 6 (2026) 153–243, doi:10.1090/cams/58) are right.

**[Hin23d].**

- The arXiv page gives v2 (18 Nov 2026) as "the version published by Ars Inveniendi Analytica", with journal reference Ars
  Inveniendi Analytica (2026), Paper No. 5, DOI 10.15781/yw47vq75, 159 pages. The v2 PDF header reads "Ars Inveniendi
  Analytica (2026), Paper No. 5, 159 pp. DOI 10.15781/yw47vq75".
- Lemma 2.25, "Fourier transform of symbols: conormal case", has the same title and the same opening statement in v1 and
  v2, and v2's proof has "N > 1 − z". The excerpts confirm the v1 page as 41–42 and the v2 page as 43 or later; no chapter
  cites a page.
- v1 Proposition 5.10 ("Compositions", §5.2, p. 109) concerns the large non-semiclassical 3b-calculus,
  A ∈ Ψ^s_3b(M) + Ψ^(−∞,E)_3b(M), so the old citation did not give a semiclassical calculus.
- Chapter 27 needs no change.
