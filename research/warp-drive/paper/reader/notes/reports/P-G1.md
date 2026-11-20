# P-G1: report on the fix for gap G1 (the semiclassical 3b-calculus in chapter 33)

Proof file: `research/warp-drive/paper/reader/proofs/P-G1.md` (942 lines). No chapter, crosswalk, Appendix A or
bibliography file was edited. `assemble.py` was not run. `lint.py proofs/P-G1.md` was run: the only hits are
(i) "reference to undefined label" for 19 chapter labels, every one of which exists in chapters 23, 33 or 95 (checked),
and (ii) "file name" on the 14 crosswalk rows at the end, which carry the path in their source column by convention and
are not edition text. No line exceeds 121 characters (Python `len`); labels only shorten on resolution. Proof/∎ count
balanced (8/8).

## 1. Structure of the fix

The insertable text (lines 1–545) is a new `####` section `sec:iv5-calc`, "The semiclassical 3b- and eb-calculi", to
go between the *Notation* paragraph and `sec:iv5-1` in chapter 33. It contains:

| Label | Content |
|---|---|
| `def:iv5-calc-cells` | The 4 + 1 cells (Hin26a (2.20)–(2.21) with ℝ⁴: U_(1),j and U_(2),i,±,j,k,m), the eb cells (as printed at 33:2427), scalings h. The classes wΨ^m_(3b,ħ) are **defined through the P′ × M device**: a family belongs if its restriction to N_P′ = P′ × M₀° is in wΨ^m_𝒱(N_P′) for every countable P′ (Hintz's own device, p. 59 + fn 13). Sobolev spaces normalised so H⁰ = L²(\|dg\|, B). |
| `lem:iv5-calc-structure` | Lemma A: b.g. structure (cover, multiplicity, transitions computed), parameterised; 𝒲 = 3b-regular span of ⟨x⟩∂_z, 𝒱_h = h𝒲; C^∞(M₀) ⊂ C^∞_uni (⟨x⟩∂_z checked to be b-fields of M₀ in all coordinate regions); weights; H⁰ ≅ L²(\|dg\|; B) uniformly; C^∞([0,1]×³ᵇT̄*M₀)·ρ_∞^(−m) ⊂ S^m uniformly; eb versions. |
| `def:iv5-calc-micro` | Concrete microsupport (two-sided: Op(1−y)B and BOp(1−y) residual for all y = 1 near K), Ell (uniform invertibility near a locus point), and the meaning of WF′(B) ⊂ S, WF′(B) ∩ S = ∅, "compact operator wave front set". |
| `lem:iv5-calc-disjoint` | F4. Op(c₁)TOp(c₂) ∈ h^∞Ψ^(−∞) for disjointly supported symbols and **any** T: on N_P′, a smooth Urysohn function y gives disjoint essential supports (Def 3.25), Theorem 3.51's (3.38) twice gives empty WF′, Lemma 3.28 gives a residual symbol, ρ̄ = h on N_P′. Consequences: microsupport is a two-sided ideal; intersections; symbols supported off ∂_ħ are residual. |
| `lem:iv5-calc-d` | Property (D) for {t > 0} and {t > 0, r < r_♯} in M₀° and {t > 0} in M° (noncompact boundaries): cone convolution chart by chart (a compatible structure straightens {r = r_♯}), uniform sum bound from (3.14), truncation ψ_R. |
| `lem:iv5-calc-dual` | F9. Precise (•,−), (−,•), H̄ spaces; duality uniform in h, from ch. 23's lem:ii-a-7-1, lem:ii-a-7-3 and the (D) lemma. |
| `lem:iv5-calc-reg` | F10. J_ε = Op(⟨εζ⟩^(−K)): bounded in Ψ⁰ over (ε, h), order −K for each ε, J_ε → I strongly; H_p j_ε = ϑ_ε j_ε e_p with ϑ_ε ∈ [0,1] bounded in S⁰ and e_p ∈ S^(m−1) independent of ε; h⁻¹[P, J_ε] bounded. |
| `prop:np-10-65-a` | **Replacement**, "The calculi", items (a) contents/left quantisation/Diff, (b) algebra incl. (\|dg\|,B)-adjoints, exact sequence and commutators (with the matrix-commutator term made explicit), (c) self-adjoint quantisation A = A*, microsupported in any closed neighbourhood of supp a, kernel in supp ψ × supp ψ, (d) boundedness, (e) **microlocal elliptic estimate, weighted, uniform in h, in the strong sense** (`eq:iv5-calc-ell`), (f) square roots (Cauchy integral, B-self-adjoint), (g) duality, (h) regularisation, (i) eb, (j) **further parameters** (b ∈ U treated as part of the parameter set U × (0,1]). Each with a proof. |
| `lem:iv5-calc-garding` | Lemma C, Gårding with a margin: Re⟨Tv,v⟩ ≤ (M + η)‖v‖² + Ch‖v‖²_(−1/2) when the B-self-adjoint part of σ(T) is ≤ M; (b) weighted, (c) eb. Proof: square root of M + η − t_R, exact sequence. |
| `lem:iv5-calc-q0` | Lemma D, lower bound ⟨Qv,v⟩ ≥ −C‖wv‖² for h-independent symmetric Q ∈ w²Diff²_3b with w⁻²σ(Q) ≥ c\|ζ\|² near supp v; eb form. Proof: q_* = φ²q + (1−φ²)\|ζ\|², θ = (q_* + 1)^(1/2), left quantisation, global parametrix for Θ, interpolation. |

Deviations from the scoping plan, with reasons:

1. **F5 (elliptic estimate) is proved by a direct parametrix iteration**, not by [Hin26d, Prop. 3.55 (3)] on P′ × M₀°.
   The P′ × M route needs a translation of the concrete hypothesis WF′(B) ⊂ Ell(A) into Hintz's abstract 𝔐 (or §3.8),
   and gives the estimate without the strong sense. The parametrix gives the strong sense directly and uses only
   (b), (d) and `lem:iv5-calc-disjoint`. The P′ × M device is still central: it defines the classes, gives
   uniformity in h (subsequence argument), and is what makes Lemma 3.28 and (3.38) usable for families (F4).
2. **(S16) quotes §§3.5–3.6 (essential support, Lemma 3.28, Def. 3.43, the rest of Thm 3.51, Lemma 3.20, Lemma 3.24 (1)),
   not §3.8.** No proof uses admissible compactifications: microsupports are defined concretely and linked to Hintz's
   WF′ by the Urysohn argument. A §3.8 quotation would be an unused Appendix A item.
3. **Adjoint microsupports.** [Hin26d] states WF′ only for compositions, not adjoints. The two-sided-ideal notion of
   microsupport (closed under T₁BT₂ for all T₁, T₂) avoids any statement about WF′(A*), and the self-adjoint commutant
   is A = ψ·Op(y)·½(Op(a) + Op(a)*)·Op(y)*·ψ, which is microsupported in supp y without it.
4. **Lemma D** is stated with a localising function φ, not as Q_0 = Θ*Θ + R; no asymptotic summation (S17) is needed.

## 2. Sites (all anchors re-checked against chapter 33 as committed after "Fix rounds … chapter 33 (all R-F-G24
findings)"; every old text occurs exactly once)

| Item | Site (approx. line) | Change |
|---|---|---|
| C33-1 | def:iv5-0-1 calculus sentence (1272) | drop "elliptic parametrices, the sharp Gårding inequality"; point to sec:iv5-calc, Lemmas C, D. |
| C33-2 | spaces on Ω (1279) | cite lem:iv5-calc-dual; "restrictions to {r > r_♯}" (precise form). |
| C33-3 | old prop:np-10-65-a (1284–1291) | delete (the label moves). |
| C33-4 | before `#### Elliptic estimates …` (1395) | insert lines 1–545 of the proof file. |
| C33-5 | prop:iv5-1-2 proof (1416) | parametrix sentence → prop (e) with A := P_h, G := B_1χ₁, B := B_0χ₂; weights and strong sense included. |
| C33-6 | prop:iv5-1-3 first sentence (1437) | "standard regularisation ([Hin26a, p. 45])" → the regularised commutant a j_ε and the ε → 0 limit (lem:iv5-calc-reg). |
| C33-7 | "A = A* with WF′(A) = supp a" (1443) | prop (c), microsupport in a neighbourhood (only ⊂ was used). |
| C33-8 | (5.26) (1450) | cite (f) square roots, (b), microsupport of E. |
| C33-9 | absorption (1462) | cite (e). |
| C33-10 | prop:iv5-2-1 commutant (1505) | A from (c) with kernel in K × K. |
| C33-11 | "For Q" (1523–1527) | full rewrite: (5.44) by Lemma D; (5.45) by Ã = Op(χ̃(𝔛\|ζ\|)φ), (I − Ã)A residual, Lemma C with η = 𝔛⁻² on ±Ã*h²Q₁Ã, bound ((9C₂ + 2)𝔛⁻² + C_𝔛h)‖Aω‖² + C h^(2N)‖χω‖²; double commutator by (b); "fix 𝔛, then h" unchanged. |
| C33-12 | prop:iv5-2-1 (2) (1532) | lower bounds by Lemmas D and C (−T). |
| C33-13 | prop:iv5-3-1 (1570) | one paragraph: weighted Lemma D (w = ρ_sf, positivity from lem:iv5-0-4) and Lemma C (b). |
| C33-14 | prop:iv5-4-1 (1608) | "with the weighted Q-terms of prop:iv5-3-1". |
| C33-15 | prop:iv5-5-2 (1706) | Q-terms → Lemmas D, C. |
| C33-16 | prop:iv5-7-1 strong sense (2036) | compact WF′ near o; regularisation at fibre infinity. |
| C33-17 | thm:iv5-7-3 (a) duality (2105) | cite lem:iv5-calc-dual, uniform in h. |
| C33-18 | lem:iv5-8-1 (2156) | "sharp Gårding … finitely many seminorms" → prop (j); margin 9C₂ + 2 and C_𝔛 uniform. |
| C33-19 | sec:iv6-2 eb cells (2427) | def:iv5-calc-cells, prop (i). |
| C33-20 | thm:iv6-2-1 cone face (before "This gives [Hin26a, (B.39)]", 2482) | one paragraph: eb Lemmas D (w = r⁻¹) and C. |
| C23-1 (optional) | ch. 23 (S7) paraphrase (367) | tighten to what p. 59 states (boundedness + "carry over verbatim" for Thm 3.51). |
| ch. 27 | 27:1256, 27:1529 | **no change**: [Hin23d, Lemma 2.25] is the same lemma, same title and statement, in v1 (p. 41) and v2/published (p. 43). |
| C95-1 | thm:std-sbg-calculus header | add Lemmas 3.20, 3.28, Remarks up to 3.56, footnote 13. |
| C95-2 | (S7) (one line → full quotations) | Def 1.9 sentence (semiclassical case), p. 58 discrete topology, Remark 3.56, Defs 3.58–3.59, the boundedness paragraph with "carry over verbatim", footnote 13, the Diff characterisation. |
| C95-3 | new (S16) + numbering note | as in §1 item 2; v1 → published numbering. |
| C98-1 | [Hin23d] | Ars Inven. Anal. (2026), Paper No. 5, 159 pp. doi:10.15781/yw47vq75 arXiv:2302.13803v2. |

**Uniformity argument (33:1934–1938 in the scoping report, now ~2150).** It holds, but not quite as the report says.
"Constants depend on finitely many seminorms" (Remark 3.47) does not cover the residual bounds produced by the
disjoint-support argument, which are not quantitative. The fix treats b as part of the parameter set (prop (j)): the
families indexed by (b, h) ∈ U × (0,1] lie in the classes, since the coefficients of P_h, Q₀, Q₁ and B are smooth in b
on the compact U, and the cut-offs and commutants do not depend on b. Every constant, the residual bounds included, is
then uniform by the same subsequence argument. The margin 9C₂ + 2 is uniform, since C₂ is the supremum of a
b-continuous symbol over a compact set. For fixed 𝔛, C_𝔛 is uniform, because the square root in Lemma C has margin
η = 𝔛⁻² for every b. Lemma D's constant is uniform because lem:iv5-0-4's C and positivity are uniform.

## 3. Quotations verified

**[Hin26d] published version** (Commun. Amer. Math. Soc. 6 (2026), 153–243, doi:10.1090/cams/58, published
electronically 14 Jan 2026, per the AMS article page). arXiv lists **only v1** (live check, 20 Nov 2026). No revised
arXiv version was found, although S-G1 mentions one dated 15 Dec 2025. Its numbering agrees with the published
numbering. The AMS PDF was read through Firecrawl (the proxy refuses ams.org); its text extraction stopped after
Definition 3.23, about 40 % of the article. The rest was read through Firecrawl's agent over the same PDF in two
turns.

- Checked directly against the published text: Definition 1.10 (= v1 Def. 1.9) with the semiclassical sentence. That
  sentence is identical. The definition itself says "such that" where v1 says "so that", and it cites Definition 1.2
  and (1.11) where v1 cites Definition 1.1 and (1.6). The (S7) quote follows v1, as Appendix A's policy requires.
  Also checked directly: Lemma 3.20 (Density), identical; the §3 overview naming Definition 3.44, Theorem 3.45 and
  Theorem 3.52; Remark 3.61 cited in §1; Definitions 1.2, 1.4, 3.1, 3.14, 3.17, 3.23, Proposition 3.19, Theorem 3.21
  and Proposition 3.22, all with v1 numbers.
- Checked through the agent's extraction, with wording identical to v1 up to typography:
  - Remark 3.57 (= v1 3.56);
  - Definitions 3.59 and 3.60 (= v1 3.58, 3.59);
  - the boundedness paragraph, which cites "Theorem 3.45" and "Theorem 3.52 carry over verbatim", with footnote 22
    (= v1 13);
  - Remark 3.61 (= v1 3.60);
  - Definition 3.62 (= v1 3.61);
  - Proposition 3.56 (3) (= v1 3.55 (3)), where the published text reads "for all N … such that";
  - Theorem 3.52 (= v1 3.51), where the published text has WF′(A₂) in (3.38), correcting v1's misprint A₁ (noted in
    (S16));
  - Remark 3.48 (= v1 3.47); Lemma 3.30 (asymptotic summation); Lemma 3.42 (Left reduction), title only;
  - Definition 3.44's text cites "Definition 3.25" and "Lemma 3.29".

  The agent's page numbers were inconsistent between its two turns (Theorem 3.52 at p. 227, then p. 224), so **no
  published page numbers are given**. Appendix A keeps v1 pages, per its stated policy, and gets a numbering note.
  The note claims only mappings that are corroborated.
- Not obtained from the published text, so quoted from v1 only:
  - Definition 3.25 (the agent returned a paraphrase that does not match v1; not used);
  - Lemma 3.28 (the agent's second turn mislabelled it);
  - Lemma 3.24 (1);
  - the Diff-characterisation sentence after Definition 3.59.

  Numbering in the published version is inferred: 3.24, 3.25 and 3.28 keep their numbers, since 3.23 and 3.29 do.
- v1 pages used: Def. 1.9 p. 9; Lemma 3.20 p. 38; Lemma 3.24 p. 40; Def. 3.25 p. 41; Lemma 3.28 p. 42; Def. 3.43 p. 51;
  Thm 3.51 p. 55; Remark 3.56 p. 58; Defs 3.58–3.59, fn 13 and the Diff sentence p. 59 (all read from the v1 full text).

**[Hin23d]**: the published article is arXiv v2. Its PDF carries the header "Ars Inveniendi Analytica (2026), Paper
No. 5, 159 pp. DOI 10.15781/yw47vq75", CC-BY, and the arXiv stamp of 18 Nov 2026. Lemma 2.25, "Fourier transform of
symbols: conormal case", is on p. 43 of v2 and p. 41 of v1, with the same statement; v2 corrects only a misprint in
the proof ("N > 1 − z"). v1 Proposition 5.10 (p. 109) is composition in the large non-semiclassical 3b-calculus, which
confirms that the old citation did not support a semiclassical calculus. v2's references list [Hin26] = CAMS 6:153–243,
doi:10.1090/cams/58, which corroborates the venue of [Hin26d].

## 4. Not closed / for the coordinator

1. **Lemma (D)** uses standard facts about H^s(ℝ⁵): invariance, on distributions supported in a fixed compact set,
   under multipliers and diffeomorphisms bounded in C^∞. These facts are not quoted in Appendix A. Ch. 23's
   lem:ii-a-7-d takes the same facts for granted.
2. **ch. 23's lem:ii-a-7-1** is stated for general parameterised structures and is cited as such. Its proof builds the
   finite parametrix "as in lem:ii-a-8-4 (b)", an e3b-section lemma, so the generality may deserve a glance.
3. **Strong sense of prop:iv5-1-3 (C33-6)** is written as a paragraph on top of the existing compressed argument. Its
   rigour is that of the surrounding proof, which belongs to G4 rather than G1.
4. **lem:iv5-0-4** is being edited by the other writer. Lemma D's applications rely on its sentence "There is C > 0,
   uniform for b ∈ U, such that C(ρ_sf⁻²ℓ(ζ))² + ρ_sf⁻²G(ζ) is B-positive definite …", which is still present.
   C33-11/13/20 also refer to the cone-face constant "as in lem:iv5-0-4".
5. Line numbers in the Placement section are approximate. Re-run the anchor check after the other writer finishes:
   each old text must occur once.
6. The published page numbers of [Hin26d] are not established (see §3). Should the author want Appendix A to cite the
   published pagination, the PDF's later pages have to be read directly; the proxy blocks ams.org.
7. Crosswalk: the row of prop:np-10-65-a is replaced (source now the proof file); 13 new rows. The rows sit at the end
   of the proof file with their line numbers.
