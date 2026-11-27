# F-G5: the scattering calculus re-sourced; minor sourcing items; C3

Fixer's report, 2026-11-20. Paper directory: research/warp-drive/paper/reader/. Items: G-SWEEP G5, the "Minor items"
paragraph after G4, and C3 of section 2.

## Summary

- **G5.** Chapter 20's calculus section (sec:i-a-2-1, items (C1)–(C8)) no longer rests on the lecture notes [HJS]. Every
  constant-order statement is now cited from Melrose's published scattering-calculus paper [Mel94] (Lecture Notes in
  Pure and Appl. Math. 161, Dekker 1994, 85–130), with statement numbers and pages verified in the author's corrected
  online edition. What [Mel94] does not state (adjoints, the seminorm bound, compactness of the Sobolev embeddings,
  duality, the microlocal parametrix, the whole variable-order theory, the regularising family) is now proved in the
  section, from [Mel94] and from the semiclassical calculus that ch. 21 §i-b-2 proves from Fourier analysis, used at h = 1.
  Ch. 20 is edited. Ch. 21, 22, 23 also cite [HJS] (13 sites); the replacement texts are given below (they point to
  (C1)–(C8) of sec:i-a-2-1). Ch. 33 contains no [HJS] citation: §iv6 depends on [HJS] only through ch. 22's spaces, which
  the ch. 22 texts re-source. [Vas18] was not used: it has no arXiv version and its printed text was not accessible, so
  no statement number or page could be verified.
- **Minor items.** thm:std-hin26a-cform: removed (texts below). Ch. 33 states the conditions itself in lem:iv4-1-4, and
  [Hin26a] is a preprint. [AN00, Theorem 3.1]: its text is paywalled and could not be read, so ch. 35 now cites the
  published, verified [ABK20, Theorem 1.1, p. 2], which covers the case used. An Appendix A entry is added and [AN00]
  is removed. [Hin17, Proposition 4.1]: the in-paper proof prop:np-10-17-i covers only 1-forms, while ch. 34 and 38 use
  the proposition on S²T*. So the citation stays: an Appendix A entry quoting Definition 3.8, Proposition 4.1 and
  p. 26 is added, the arXiv id is added to [Hin17], and the ch. 32 header carries the page.
- **C3.** The ch. 03 summary of cor:vlasov-two-dust now carries the hypothesis that the outgoing packet does not reach
  R = a, in the corollaries' own form, with the remark from ch. 90 that the construction of the background does not
  decide it.
- **Checks.** The live tree gives lint 0 hits and assemble 0 problems. With all 24 coordinator texts below applied to a
  copy of the tree, lint gives 0 hits and assemble 0 problems, and no [HJS], [AN00], thm:std-hjs-calculus or
  thm:std-hin26a-cform remains.

## 1. G5: sources verified, statement by statement

**Source.** R. B. Melrose, *Spectral and scattering theory for the Laplacian on asymptotically Euclidian spaces*, in:
Spectral and Scattering Theory (Sanda, 1992), Lecture Notes in Pure and Appl. Math. 161, Dekker, New York (1994),
85–130 (MR1291640; reprint doi:10.1201/9781003072096-5). Read in full on 2026-11-20 from the author's corrected
online edition (https://math.mit.edu/~rbm/papers/sslaes/sslaes1.pdf, "Corrected (Jan 15, 1997)" per
math.mit.edu/~rbm/paper.html; 57 pages, pages printed on the PDF and equal to the PDF page index). Two reads were made:
the whole text, and page-tagged extracts of pp. 1–6, 8–9, 12–21, 23–25, 47–52 and 56. Appendix A already cites [Mel93]
by its online edition's pages, so [Mel94] is cited the same way, and the policy sentence in 95's opening says so.
Melrose's decay order l has the opposite sign: his Ψ^(m,l)_scc is the edition's Ψ^(m,−l)_sc. His H^(m,l)_sc is the
edition's H^(s,r)_sc with the same indices, as ch. 20 now states.

| Item (old [HJS] source) | New source / proof |
|---|---|
| Ψ_sc on ℝⁿ, compactification | [Mel94, (4.1)–(4.2), pp. 12–13; Definition 1, p. 13] (amplitude estimates (1+\|z\|)^(−l−\|α\|)(1+\|ζ\|)^(m−\|β\|)); stereographic projection "We call this the radial compactification", x = 1/\|z\| boundary defining function [Mel94, (1.1), p. 4] |
| (C1) composition [HJS (2.1)] | [Mel94, (5.1), p. 15] "Ψ^(m1,l1)_sk(X) ∘ Ψ^(m2,l2)_sk(X) ⊂ Ψ^(m1+m2,l1+l2)_sk(X)", sk = sc or scc (p. 14) |
| (C1) principal symbol, exact sequence, multiplicativity [HJS Def. 7.2, (7.29)] | [Mel94, (5.11)–(5.14), p. 17] |
| (C1) asymptotic sums (used in parametrices, lem:i-a-2-3) | [Mel94, Lemma 6, p. 20] |
| (C1) adjoints [HJS Prop. 7.4] | not stated in [Mel94]; **proved** from thm:i-b-2-5 at h = 1 (ch. 21) |
| (C2) commutators, Poisson bracket [HJS Prop. 7.5] | [Mel94, Proposition 4, (5.16), p. 18] with the order from [Mel94, Lemma 5, (5.18), p. 18]; bracket (5.22), p. 19 |
| (C2)/prop:i-a-5-2 (a): H_p = weight × b-vector field [HJS (7.34)] | [Mel94, Lemma 5, (5.17), p. 18] (for amplitudes smooth after removal of the weight) |
| lem:i-a-4-4 (c): the sc Hamilton field in (τ, μ) [HJS (7.33)–(7.34)] | **derived** in the proof by the chain rule from [Mel94, (5.20), p. 18] (τ = x²ξ, μ = xη) and (5.22), p. 19; the displayed formula was rechecked by hand |
| (C3) boundedness [HJS Prop. 3.11] | [Mel94, Proposition 5, (5.28), p. 20] |
| (C3) continuity in the symbol [HJS Rem. 3.12] | **proved**: closed graph theorem (the edition already uses it, ch. 23:1417) |
| (C4) Rellich compactness [HJS Prop. 3.13] | **proved** from the criterion of [Mel94, Proposition 5, p. 20] (compact iff the joint symbol vanishes, classical operators) with [Mel94, Proposition 3, (5.10), p. 17]: A = ⟨D⟩^(−δ/2)⟨x⟩^(−δ)⟨D⟩^(−δ/2), A^k compact on L² for δ = 1/k, hence A compact by the spectral theorem |
| (C4) duality [HJS Prop. 3.7] | not stated in [Mel94]; **proved** (unitary maps ⟨D⟩^(±s)⟨x⟩^(±r)) |
| (C5) parametrix, microlocal parametrix, microlocality [HJS Props. 2.3, 4.9, 4.10, 10.1] | WF′ and microlocality [Mel94, (7.1), (7.2), (7.6), p. 23]; parametrices **proved** (Neumann series and asymptotic sums, as [Mel94, (6.2)–(6.5), pp. 21–22]); microlocal elliptic estimate stated and proved |
| (C6) variable orders [HJS §§10.1–10.3, p. 79, p. 81] | **proved**: the class is that of def:i-b-2-1 at h = 1 (logarithmic losses); composition, adjoints, commutators, L² bound from thm:i-b-2-4, thm:i-b-2-5, eq:i-b-2-5, thm:i-b-2-7 at h = 1; asymptotic sums from [Mel94, Lemma 6] in constant orders; spaces H^(s,𝗋) defined, Hilbert, independent of choices, boundedness with seminorm bound, monotonicity, compactness, duality proved |
| (C7) bundles [HJS §7.5] | stated as the definition (matrices on the trivial bundle); [Mel94, Proposition 3, (5.10), p. 17] for the symbol sequence on bundles |
| (C8) regularising family [HJS Lemma 12.5] | T_t := Op(χ(tx)χ(tξ)); **proved** (bounded in S^(0,0), → 1 in S^(δ,δ) with seminorms O(t^δ), strong convergence on every H^(s,𝗋)); [Mel94, (5.30), p. 20] cited for existence of such sequences; T_t maps 𝒮′ to 𝒮 by [Mel94, (5.34), p. 21] |
| rem:i-a-1-1 quote [HJS p. 77] | replaced by a pointer to sec:i-a-2-1 (constant differential order) |
| 20:376 [HJS p. 79], 20:1001 [HJS p. 81] | (C6); the Q_ε^(1/2) argument re-stated in the class of (C6), as in lem:i-b-2-12; the HJS aside dropped |

Notes.

1. Melrose's Proposition 4 prints (5.16) with j_(sc,m1+m2,l1+l2)([A, B]). By his Lemma 5, (5.18), the bracket has
   orders (m1 + m2 − 1, l1 + l2 + 1), and by (5.13)–(5.14) [A, B] lies in that class. The Appendix A entry quotes (5.16)
   verbatim and adds this reading in its closing sentence, with the reason.
2. Ch. 20 now depends forward on ch. 21 §i-b-2 (def:i-b-2-1, thm:i-b-2-4, thm:i-b-2-5, eq:i-b-2-5, thm:i-b-2-7,
   lem:i-b-2-12). There is no circularity. The proofs of those results use Fourier analysis, integration by parts and
   Schur's test. §i-b-2 refers to ch. 20 only in the remark identifying H_h^𝐨 with the spaces of sec:i-a-2-2, which no
   proof in §i-b-2 uses. Lemma i-b-3-1, which uses (C8), comes after §i-b-2.
3. The variable-order class is now the logarithmic class of def:i-b-2-1 at h = 1, in place of HJS's ⟨x⟩^(−δ)𝒱_b class,
   and it lies in that class for every δ > 0. Every use in ch. 20 was checked against it: the weights ⟨ξ⟩^s⟨x⟩^𝗋, the
   commutants with log ϱ (rem:i-a-3-3), Q_ε^(1/2) (prop:i-a-5-2) and the regularisers.

## 2. Minor items: sources verified

- **thm:std-hin26a-cform (95:286).** No chapter references it by label. Ch. 33 cites "[Hin26a, Proposition 5.1]" as
  attribution, and lem:iv4-1-4 (33:1096–1108) states and proves conditions (1)–(6) itself, in dimension 4 + 1. The
  entry quotes a preprint, against 95's own first sentence ("published results"). **Removed** (text below; crosswalk row
  too). An optional ch. 33 text points 33:554 to lem:iv4-1-4, which is later in the chapter.
- **[AN00, Theorem 3.1, p. 787] (35:1340).** Math. Z. 234 (2000) is paywalled. The Springer abstract confirms the
  result ("if we assume f to be locally bounded … it suffices that φ∘f is holomorphic for all φ ∈ W, where W is a
  separating subspace of X′") but not its number or page, so it could not be verified. **Replaced** by W. Arendt,
  M. Bernhard, M. Kreuter, *Elliptic problems and holomorphic functions in Banach spaces*, Illinois J. Math. 64 (2020),
  331–347, doi:10.1215/00192082-8591584 (data from Crossref). The source was read in arXiv:1904.03088v1 (v2 has no PDF).
  It defines "very weakly holomorphic" (p. 1) and "locally L¹-bounded" (pp. 1–2), and Theorem 1.1 (p. 2) reads: "Let X
  be a Banach space and Ω ⊂ ℂ (Ω ⊂ ℝ^d) be open. A function f : Ω → X is holomorphic (harmonic) if and only if it is
  locally L¹-bounded and very weakly holomorphic (very weakly harmonic)." The step from locally bounded to locally
  L¹-bounded is proved in the new Appendix A entry. Ch. 35 is edited (citation lines only).
- **[Hin17, Proposition 4.1].** Read in arXiv:1502.03183v2 (the version ch. 38:773 cites). Definition 3.8 is on p. 16,
  Proposition 4.1 on p. 20, and Theorem 4.8 with the sentence "By restriction, the analogous statements are true for □
  acting on subbundles of the tensor bundle on M, for instance differential forms of all degrees and symmetric
  2-tensors" on p. 26, which ch. 38:786 cites as [Hin17, p. 26]. prop:np-10-17-i proves only the 1-form case, and ch. 34
  (39, 202) and ch. 38 (773–804) use the proposition on S²T*. So the proposition stays cited. An **Appendix A entry**
  is added, and the ch. 32 header now reads "[Hin17, Proposition 4.1, p. 20] on 1-forms". The arXiv id is added to the
  [Hin17] reference so that the page convention of 95 applies.

## 3. C3

Ch. 03:363–365 now reads: "… not on the whole of that domain, under the hypothesis of both corollaries that the
outgoing packet of the two-dust background does not reach its inner sphere, {u1 ≤ u ≤ u2} ∩ Ω₂ ∩ {R = a} = ∅, which the
construction of that background does not decide ([[cor:vlasov-two-dust]])". This is the condition of cor:class-two-dust
(81:1625–1628) and cor:vlasov-two-dust (82:2321–2323, there written with ϕ_out), with the wording of ch. 90:173–176.

## 4. Edits made (files: ch. 20, 03, 32, 35 and their crosswalks)

New labels: none. Removed labels: none. Crosswalk notes were updated for sec:i-a-2-1, rem:i-a-1-1, lem:i-a-4-4 and
prop:i-a-5-2 (ch. 20), sec:further-results (ch. 03), prop:np-10-17-i (ch. 32) and thm:iii-g1-3-1 (ch. 35). The
coordinator's snapshot commits 0f34f539 and 60172920 picked these edits up while I worked. The diffs below are against
796714d8, the HEAD at the start.

### Chapter 20
```diff
--- /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/20-orig.md	2026-11-20 17:41:15.636084407 +0000
+++ chapters/20-s01-spectral-bounded.md	2026-11-20 17:43:05.697395124 +0000
@@ -173,66 +173,175 @@
     H̄^(s,𝗋) := H̄^(s,𝗋)_sc(X̄; E),     Ḣ^(s,𝗋) := Ḣ^(s,𝗋)_sc(X̄; E),
 
 extendible, respectively supported, at ∂_♯X ([[sec:i-a-6-1]]), built componentwise from the scattering Sobolev spaces
-of [HJS, Definition 10.2] on ℝ⁴ (constant regularity order, variable decay order).
+of (C6) in [[sec:i-a-2-1]] on ℝ⁴ (constant regularity order, variable decay order).
 
 **Remark {#rem:i-a-1-1}** (Constant regularity order.) [Hin26c] lets the regularity order vary at fibre infinity over a
-region {r > r_Γ}, r_Γ > r_e, where P̂(σ) is elliptic. The calculus of [HJS] used here takes the differential order
-constant ([HJS, p. 77]: "we will take the differential order to be constant, and the spatial order to be variable"),
-and every proof below uses only s ≡ s_c, so [[thm:i-a-7-2]] is stated and proved for constant s. The semiclassical
-calculus of [[ch:s02]] has variable orders in all three senses; with the semiclassical parameter equal to 1 it would
-supply the elliptic estimate at a variable s over {r > r_Γ}, but no result of this chapter needs it.
+region {r > r_Γ}, r_Γ > r_e, where P̂(σ) is elliptic. The calculus used here ([[sec:i-a-2-1]]) takes the differential
+order constant and lets only the decay order vary, and every proof below uses only s ≡ s_c, so [[thm:i-a-7-2]] is
+stated and proved for constant s. The semiclassical calculus of [[ch:s02]] has variable orders in all three senses;
+with the semiclassical parameter equal to 1 it would supply the elliptic estimate at a variable s over {r > r_Γ}, but
+no result of this chapter needs it.
 
 ### The calculus {#sec:i-a-2}
 
 #### The statements used {#sec:i-a-2-1}
 
-The following statements of [HJS] are used as black boxes. They are stated in [HJS] on ℝⁿ for every n, so they hold at
-n = 4; page numbers are those printed in [HJS]. Every operator below has Schwartz kernel supported in X̃ × X̃, and
-X̄ ⊂ ℝ̄⁴, so the calculus on ℝ⁴ is the calculus used.
-
-(C1) (Composition, [HJS, (2.1), p. 9]; principal symbol, [HJS, pp. 49–50].) Ψ^(m,ℓ)_sc ∘ Ψ^(m′,ℓ′)_sc ⊂
-Ψ^(m+m′,ℓ+ℓ′)_sc. By [HJS, Proposition 7.4], "A ∈ Ψ^(m,l)_sc(M) ⇒ A∗ ∈ Ψ^(m,l)_sc(M)", and
-"σ_(m₁+m₂,l₁+l₂)(AB) = σ_(m₁,l₁)(A) σ_(m₂,l₂)(B)" [HJS, (7.29)], the principal symbol taking values in
-S^(m,l)_sc/S^(m−1,l−1)_sc [HJS, Definition 7.2].
-
-(C2) (Commutators, [HJS, Proposition 7.5, p. 50].) "[A, B] ∈ Ψ^(m₁+m₂−1,l₁+l₂−1)_sc(M) and
-σ(i[A, B]) = {σ(A), σ(B)}", the Poisson bracket being H_p a, with the scattering Hamilton vector field of
-[HJS, (7.34)].
-
-(C3) (Boundedness, [HJS, Proposition 3.11 and Remark 3.12, p. 20].) "If A ∈ Ψ^(m,l)_sc, then, for all s, r ∈ ℝ, A maps
-A : H^(s,r)_sc → H^(s−m,r−l)_sc … and does so boundedly"; and "Op(a), viewed as an element of
-L(H^(s,r)_sc, H^(s−m,r−l)_sc), depends continuously on a". Since a ↦ Op(a) is linear and continuous from the Fréchet
-space S^(m,l)_sc to a Banach space, it is bounded by one seminorm: a family bounded in Ψ^(m,l) is uniformly bounded
-H^(s,r) → H^(s−m,r−l).
-
-(C4) (Compactness, [HJS, Proposition 3.13, p. 20]; duality, [HJS, Proposition 3.7, p. 19].) "For any s, s′, r, r′,
-with s < s′ and r < r′, the embedding H^(s′,r′)_sc ↪ H^(s,r)_sc is compact." The L² pairing identifies (H^(s,r)_sc)∗
-with H^(−s,−r)_sc.
-
-(C5) (Ellipticity, [HJS, Propositions 2.3, 4.9, 4.10 and 10.1, pp. 12, 27–29, 79].) "Every elliptic element of the
-scattering calculus has a parametrix" (Proposition 2.3). There is a microlocal parametrix at a closed subset of the
-elliptic set (Proposition 4.10: "AB − 1, BA − 1 have WF′_sc disjoint from p. This also applies with p replaced by any
-closed subset"), also for variable orders (Proposition 10.1). Microlocality (Proposition 4.9):
-"WF^(s,r)_sc(Au) ⊆ WF^(s+m,r+l)_sc(u) ∩ WF′_sc(A)".
-
-(C6) (Variable orders, [HJS, Sections 10.1–10.3, pp. 77–80].) The symbol classes S^(m,l)_sc with l variable are defined
-with the vector fields ⟨x⟩^(−δ)𝒱_b [HJS, (10.3)–(10.4)], so that "the logarithmic factor" in derivatives of
-⟨x⟩^(l(x,ξ)) costs an arbitrary δ > 0; composition and the principal symbol are as in [HJS, Section 10.2]; and the
-spaces [HJS, Definition 10.2 and Section 10.3] are independent of the choices and Hilbert, with Ψ^(m,l)_sc bounded on
-them.
-
-(C7) (Bundles, [HJS, Section 7.5, pp. 52–53].) "Ψ^(m,l)_sc(M; E, F) := C^∞(X; Hom(E, F)) ⊗ Ψ^(m,l)_sc(M) …
-Equivalently, an element in Ψ^(m,l)_sc(M; E, F) is a matrix with entries in Ψ^(m,l)_sc(M)."
-
-(C8) (A regularising family, [HJS, Lemma 12.5, p. 95].) T_t := χ(t⟨z⟩) Op(χ(⟨tζ⟩)) ∈ Ψ^(−∞,−∞)_sc, t ∈ (0, t₀], with
-T_t → Id strongly on each H^(s,r)_sc; the proof of [HJS, Lemma 12.5] records "T_r being uniformly bounded in
-Ψ^(0,0)_sc and T_r → Id in the operator topology of Ψ^(δ,δ)_sc".
+The calculus is Melrose's scattering calculus [Mel94, Sections 4, 5 and 7]. For every n, [Mel94, Definition 1,
+p. 13] defines Ψ^(m,l)_scc as the operators on 𝒮(ℝⁿ) with Schwartz kernels (2π)^(−n) ∫ e^(i(z−z′)·ζ) a(z, ζ) dζ, the
+amplitude satisfying |D_z^α D_ζ^β a(z, ζ)| ≤ C_αβ (1 + |z|)^(−l−|α|) (1 + |ζ|)^(m−|β|) [Mel94, (4.1)–(4.2),
+pp. 12–13], transferred to the half-sphere by stereographic projection. [Mel94, Section 1, (1.1), p. 4] calls this the
+radial compactification of ℝⁿ, with boundary defining function |z|⁻¹ and collar coordinates (|z|⁻¹, z/|z|): the
+half-sphere is ℝ̄ⁿ. [Mel94] measures decay with the sign opposite to ours. We write S^(m,ℓ)_sc for the amplitudes
+with |∂_x^α ∂_ξ^β a| ≤ C_αβ ⟨x⟩^(ℓ−|α|) ⟨ξ⟩^(m−|β|), Op(a) for the operator with that kernel, and
+Ψ^(m,ℓ)_sc := Op(S^(m,ℓ)_sc), which is [Mel94]'s Ψ^(m,−ℓ)_scc; and
+
+    H^(s,r)_sc := {u ∈ 𝒮′ : ⟨D⟩^s ⟨x⟩^r u ∈ L²},     ‖u‖_(s,r) := ‖⟨D⟩^s ⟨x⟩^r u‖_(L²).
+
+This is [Mel94]'s H^(s,r)_sc [Mel94, (5.27), p. 19]: an element of [Mel94]'s Ψ^(s,−r)_sc is ⟨D⟩^s⟨x⟩^r followed by an
+operator of order (0, 0), which is bounded on L² by (C3). Pages of [Mel94] are those of the author's online edition.
+Its statements hold on every compact manifold with boundary, in particular on ℝ̄ⁿ for every n, so at n = 4. Every
+operator below has Schwartz kernel supported in X̃ × X̃, and X̄ ⊂ ℝ̄⁴, so the calculus on ℝ⁴ is the calculus used.
+[Mel94] treats constant orders and states neither adjoints nor duality. What it does not state is proved after the
+list, from [Mel94] and from the semiclassical calculus of [[sec:i-b-2]]. That calculus is proved there from Fourier
+analysis alone, for every h ∈ (0, 1], and is used here at h = 1: an amplitude independent of h is a family in the
+classes of [[def:i-b-2-1]], with ζ = ξ, and Op_1 = Op.
+
+(C1) (Composition, principal symbol, asymptotic sums, adjoints.) Ψ^(m,ℓ)_sc ∘ Ψ^(m′,ℓ′)_sc ⊂ Ψ^(m+m′,ℓ+ℓ′)_sc
+[Mel94, (5.1), p. 15]. The principal symbol σ(A) of Op(a) ∈ Ψ^(m,ℓ)_sc is the class of a in
+S^(m,ℓ)_sc/S^(m−1,ℓ−1)_sc; the symbol map is onto, its kernel is Ψ^(m−1,ℓ−1)_sc, and σ(AB) = σ(A)σ(B) [Mel94,
+(5.11)–(5.14), p. 17]. If A_j ∈ Ψ^(m−j,ℓ−j)_sc for j ∈ ℕ₀, there is A ∈ Ψ^(m,ℓ)_sc with
+A − Σ_(j<N) A_j ∈ Ψ^(m−N,ℓ−N)_sc for every N [Mel94, Lemma 6, p. 20]. A ∈ Ψ^(m,ℓ)_sc ⇒ A∗ ∈ Ψ^(m,ℓ)_sc, with
+σ(A∗) = σ(A)∗.
+
+(C2) (Commutators.) For A ∈ Ψ^(m₁,ℓ₁)_sc and B ∈ Ψ^(m₂,ℓ₂)_sc, [A, B] ∈ Ψ^(m₁+m₂−1,ℓ₁+ℓ₂−1)_sc, since the principal
+symbols commute, and σ(i[A, B]) = {σ(A), σ(B)} [Mel94, Proposition 4, (5.16), p. 18], a symbol of order
+(m₁ + m₂ − 1, ℓ₁ + ℓ₂ − 1) [Mel94, Lemma 5, (5.18), p. 18]. Here {a, b} = ∂_ξa·∂_xb − ∂_xa·∂_ξb = H_ab is the
+Poisson bracket of T∗ℝⁿ [Mel94, (5.22), p. 19]. If a is ⟨ξ⟩^(m₁)⟨x⟩^(ℓ₁) times a function smooth on the
+compactified phase space, then H_a is ⟨ξ⟩^(m₁−1)⟨x⟩^(ℓ₁−1) times a smooth vector field tangent to both boundary faces
+[Mel94, Lemma 5, (5.17), p. 18].
+
+(C3) (Boundedness.) Every A ∈ Ψ^(m,ℓ)_sc is bounded H^(s,r)_sc → H^(s−m,r−ℓ)_sc for all s, r [Mel94, Proposition 5,
+(5.28), p. 20], with norm bounded by a seminorm of its amplitude in S^(m,ℓ)_sc. So a family bounded in Ψ^(m,ℓ)_sc is
+uniformly bounded H^(s,r)_sc → H^(s−m,r−ℓ)_sc.
+
+(C4) (Compactness, duality.) For s < s′ and r < r′ the embedding H^(s′,r′)_sc ↪ H^(s,r)_sc is compact, and the L²
+pairing identifies (H^(s,r)_sc)∗ with H^(−s,−r)_sc. Compactness is proved below from the criterion of [Mel94,
+Proposition 5, p. 20]: an operator whose amplitude is its weight times a function smooth on the compactified phase
+space is compact between the spaces of (C3) if and only if its principal symbol vanishes.
+
+(C5) (Ellipticity, microlocality.) The operator wavefront set WF′(A) is the closed subset of the boundary of phase
+space off which the amplitude of A is locally of order (−∞, −∞); WF′(AB) ⊂ WF′(A) ∩ WF′(B), and WF′(A) = ∅ if and
+only if A ∈ Ψ^(−∞,−∞)_sc [Mel94, (7.1), (7.2) and (7.6), p. 23]. A is elliptic at a point of the boundary of phase
+space if its amplitude a is invertible near it with |a⁻¹| ≤ C⟨ξ⟩^(−m)⟨x⟩^(−ℓ); Ell(A) is the open set of such points.
+If A is elliptic on a neighbourhood of a closed set K, there is B ∈ Ψ^(−m,−ℓ)_sc with WF′(AB − Id) ∩ K = ∅ and
+WF′(BA − Id) ∩ K = ∅; if A is elliptic everywhere, there is B with AB − Id and BA − Id in Ψ^(−∞,−∞)_sc. This is
+proved below; for elliptic A it is the construction of [Mel94, (6.2)–(6.5), pp. 21–22]. Hence the microlocal elliptic
+estimate: if G, Q ∈ Ψ^(0,0)_sc and WF′(Q) ⊂ Ell(A) ∩ Ell(G), then ‖Qu‖_(s,r) ≤ C(‖GAu‖_(s−m,r−ℓ) + ‖u‖_(−M,−M)) for
+every M.
+
+(C6) (Variable orders.) A variable order is a real function 𝗅 on ℝ⁴ × ℝ⁴ that is smooth on ℝ̄⁴ × ℝ̄⁴, so that its
+derivatives obey |∂_x^α ∂_ξ^β 𝗅| ≤ C_αβ ⟨x⟩^(−|α|) ⟨ξ⟩^(−|β|) ([[sec:i-b-2-1]]). For constant m, S^(m,𝗅)_sc is the
+space of smooth matrix functions a with |a| ≤ C⟨ξ⟩^m⟨x⟩^𝗅 and, for (α, β) ≠ 0,
+
+    |∂_x^α ∂_ξ^β a| ≤ C_αβ ⟨ξ⟩^m ⟨x⟩^𝗅 ⟨x⟩^(−|α|) ⟨ξ⟩^(−|β|) (1 + log⟨x⟩ + log⟨ξ⟩)^(μ_αβ),
+
+the class S^𝐨 of [[def:i-b-2-1]] at h = 1 with 𝐨 = (m, 𝗅, 0). For a constant 𝗅 = ℓ it is the logarithmic class of
+order (m, ℓ): it contains S^(m,ℓ)_sc and lies in S^(m+δ,ℓ+δ)_sc for every δ > 0. By [[thm:i-b-2-4]], [[thm:i-b-2-5]]
+and [[eq:i-b-2-5]] at h = 1 these classes are closed under composition and adjoints, and every term after the first
+of the expansions there gains 1 − δ in both orders, for every δ > 0. So the principal symbol is the class of the
+amplitude modulo the class of order (m − 1 + δ, 𝗅 − 1 + δ) for every δ > 0; it is multiplicative; σ(A∗) = σ(A)∗; and
+[A, B] has order (m + m′ − 1 + δ, 𝗅 + 𝗅′ − 1 + δ) for every δ > 0, with σ(i[A, B]) = H_aσ(B) if σ(A) = a Id is
+scalar. Operators of order (0, 0) are bounded on L² ([[thm:i-b-2-7]] at h = 1). For constant s, a variable order 𝗋,
+E := Op(⟨ξ⟩^s⟨x⟩^𝗋 Id) and an integer N ≥ max(−s, −inf 𝗋) + 1, let
+
+    H^(s,𝗋)_sc := {u ∈ H^(−N,−N)_sc : Eu ∈ L²},     ‖u‖²_(s,𝗋) := ‖Eu‖²_(L²) + ‖u‖²_(−N,−N).
+
+Asymptotic sums exist; H^(s,𝗋)_sc is a Hilbert space, independent of N and, up to equivalent norms, of the elliptic
+operator of order (s, 𝗋) used in place of E, and it is H^(s,r)_sc for constant 𝗋 = r; and (C3), (C4) and (C5) hold
+with variable orders, the compactness of the embedding requiring the decay order to drop by a positive constant. These
+statements are proved below.
+
+(C7) (Bundles.) On the trivial bundle ℂ^N the operators of order (m, ℓ) are the N × N matrices with entries in
+Ψ^(m,ℓ)_sc; [Mel94, Proposition 3, (5.10), p. 17] states the symbol sequence for operators between bundles.
+
+(C8) (A regularising family.) Fix χ ∈ C_c^∞(ℝ⁴) equal to 1 near 0, and let T_t := Op(τ_t) with
+τ_t(x, ξ) := χ(tx)χ(tξ), t ∈ (0, 1]. Then T_t ∈ Ψ^(−∞,−∞)_sc, which maps 𝒮′ to 𝒮 [Mel94, (5.34), p. 21]; T_t is
+bounded in Ψ^(0,0)_sc, T_t → Id in Ψ^(δ,δ)_sc for every δ > 0, and T_t → Id strongly on every H^(s,𝗋)_sc. This is
+proved below; [Mel94, (5.30), p. 20] states that such approximating sequences exist.
 
 In the interior, at fibre infinity, the scattering calculus restricted to kernels supported in a compact set is the
 classical calculus, and the scattering principal symbol there is the classical one: over a compact set ⟨x⟩ is bounded
 above and below, so the scattering estimates of order (m, ℓ) for symbols supported over it are the Kohn–Nirenberg
 estimates of order m.
 
+*Proofs of the statements not taken from [Mel94].* *Adjoints (C1).* For a ∈ S^(m,ℓ)_sc, [[thm:i-b-2-5]] at h = 1
+gives Op(a)∗ = Op(a^♮), where a^♮ − Σ_(|α|<4) (1/α!) ∂_ξ^α D_x^α a∗ obeys the bounds of [[def:i-b-2-1]] of order
+(m − 2, ℓ − 2), so lies in S^(m−1,ℓ−1)_sc, the logarithms costing any δ > 0. The terms with α ≠ 0 lie in
+S^(m−1,ℓ−1)_sc. So a^♮ ∈ S^(m,ℓ)_sc and a^♮ − a∗ ∈ S^(m−1,ℓ−1)_sc.
+
+*Seminorm bounds (C3).* For fixed s and r, the map a ↦ Op(a) from the Fréchet space S^(m,ℓ)_sc to the Banach space of
+bounded operators H^(s,r)_sc → H^(s−m,r−ℓ)_sc is linear and has closed graph. Indeed, if a_j → a and Op(a_j) → T, then
+Op(a_j)u = (2π)^(−n) ∫ e^(ix·ξ) a_j(x, ξ) û(ξ) dξ → Op(a)u pointwise for u ∈ 𝒮, so T = Op(a) on 𝒮, which is dense in
+H^(s,r)_sc because ⟨D⟩^s⟨x⟩^r maps 𝒮 onto 𝒮. By the closed graph theorem the map is continuous, so the norm of Op(a)
+is bounded by a seminorm of a. The same argument on L² gives the seminorm bound for the operators of order (0, 0) of
+(C6).
+
+*Compactness (C4).* Let k ∈ ℕ with δ := 1/k ≤ min(s′ − s, r′ − r), and A := ⟨D⟩^(−δ/2) ⟨x⟩^(−δ) ⟨D⟩^(−δ/2), a
+nonnegative operator on L². Each factor has as amplitude its weight times a function smooth on the compactified phase
+space, and [Mel94, (5.1)] keeps this property, so A^k, of order (−1, −1), is such an operator of order (0, 0) with
+vanishing principal symbol [Mel94, Proposition 3, (5.10), p. 17]. By [Mel94, Proposition 5], A^k is compact on L².
+Then A = (A^k)^(1/k), a norm limit of polynomials in A^k without constant term, is compact. The embedding
+H^(δ,δ)_sc ↪ L² is A ∘ A⁻¹, with A⁻¹ = ⟨D⟩^(δ/2) ⟨x⟩^δ ⟨D⟩^(δ/2) bounded from H^(δ,δ)_sc to L² by (C3), so it is
+compact. The embedding H^(s′,r′)_sc ↪ H^(s,r)_sc is the bounded embedding into H^(s+δ,r+δ)_sc followed by
+⟨x⟩^(−r)⟨D⟩^(−s) J ⟨D⟩^s⟨x⟩^r, where J is the compact embedding H^(δ,δ)_sc ↪ L².
+
+*Duality (C4).* With Λ_(s,r) := ⟨D⟩^s⟨x⟩^r, u ↦ Λ_(s,r)u is unitary from H^(s,r)_sc onto L² and v ↦ Λ_(−s,−r)v from
+H^(−s,−r)_sc onto L², and ⟨u, v⟩ = ⟨Λ_(s,r)u, Λ_(−s,−r)v⟩ for u, v ∈ 𝒮, since Λ_(−s,−r) = (Λ_(s,r)⁻¹)∗.
+
+*Ellipticity (C5).* Let χ ∈ S^(0,0)_sc equal 1 near K, with a elliptic near its support, and B₀ := Op(χa⁻¹), which
+lies in Ψ^(−m,−ℓ)_sc. By (C1), AB₀ = Op(χ) + R₀ with R₀ ∈ Ψ^(−1,−1)_sc. Let C ∼ Σ_j (−R₀)^j (C1), so that
+(Id + R₀)C − Id ∈ Ψ^(−∞,−∞)_sc, and B := B₀C. Then Id − AB = (Id − Op(χ))C + E with E ∈ Ψ^(−∞,−∞)_sc, whose WF′
+misses K, as χ = 1 near K. A left parametrix B′ is built in the same way, and B′ − B = B′(Id − AB) − (Id − B′A)B has
+WF′ disjoint from K, so BA − Id has too. If A is elliptic everywhere, take χ = 1. For the estimate, let B be such an
+operator for GA, which is elliptic near K := WF′(Q). Then Q = QBGA + Q(Id − BGA), where the last operator has empty
+WF′ and so lies in Ψ^(−∞,−∞)_sc, and (C3) gives the estimate. With variable orders the same holds by (C6), R₀ gaining
+1 − δ in both orders.
+
+*Variable orders (C6).* Asymptotic sums: let A_j have order (m − j + δ, 𝗅 − j + δ) for a fixed δ ∈ [0, 1). With
+δ′ := (1 + δ)/2 and ω := sup 𝗅 − inf 𝗅, A_j lies in Ψ^(m−j+δ′,sup𝗅−j+δ′)_sc, and an asymptotic sum A there [Mel94,
+Lemma 6] has A − Σ_(j<N) A_j of order (m − N + δ′, sup 𝗅 − N + δ′), so of variable order (m, 𝗅) − (N − ω − 1)(1, 1),
+for every N. *Spaces.* Let E⁻ be a parametrix of E ((C5)). If u ∈ H^(−N,−N)_sc and Eu ∈ L², then
+u = E⁻Eu + (Id − E⁻E)u lies in H^(−N₁,−N₁)_sc, with norm at most C(‖Eu‖ + ‖u‖_(−N,−N)), for every integer
+N₁ ≥ max(−s, −inf 𝗋) + 1, by (C3) in constant orders, E⁻ lying in Ψ^(−s+δ,−inf𝗋+δ)_sc for δ ∈ (0, 1); so the space
+and its norm do not depend on N. If E₁ is elliptic of order (s, 𝗋), then
+E₁u = (E₁E⁻)Eu + E₁(Id − E⁻E)u, so ‖E₁u‖ ≤ C(‖Eu‖ + ‖u‖_(−N,−N)), and symmetrically. For constant 𝗋 = r take
+E₁ := ⟨D⟩^s⟨x⟩^r. The norm comes from an inner product, and the space is complete: if Eu_j → f in L² and u_j → u in
+H^(−N,−N)_sc, then Eu_j → Eu in 𝒮′, so Eu = f. *Boundedness.* Let B have order (m, 𝗅), and let
+E′ := Op(⟨ξ⟩^(s−m)⟨x⟩^(𝗋−𝗅) Id). For u ∈ H^(s,𝗋)_sc, E′Bu = (E′BE⁻)Eu + E′B(Id − E⁻E)u, where E′BE⁻ has order (0, 0)
+and E′B(Id − E⁻E) ∈ Ψ^(−∞,−∞)_sc; and Bu ∈ H^(−N′,−N′)_sc for N′ := N + |m| + sup |𝗅| + 1, B having the constant
+order (m + 1, sup 𝗅 + 1). So B is bounded H^(s,𝗋)_sc → H^(s−m,𝗋−𝗅)_sc, with norm bounded by a seminorm of its
+amplitude, by the seminorm bounds of [[thm:i-b-2-4]] and of (C3). With B = Id, H^(s,𝗋)_sc ⊂ H^(s′,𝗋′)_sc for s′ ≤ s
+and 𝗋′ ≤ 𝗋. *Compactness.* Let s′ < s and 𝗋′ ≤ 𝗋 − c with a constant c > 0, τ := min(s − s′, c, 1), and
+E′ := Op(⟨ξ⟩^(s′)⟨x⟩^(𝗋′) Id). Then E′ is bounded from H^(s,𝗋)_sc to H^(τ,τ)_sc, which embeds compactly in L², and
+H^(s,𝗋)_sc ⊂ H^(−N,−N)_sc embeds compactly in H^(−N−1,−N−1)_sc by the constant case; with N + 1 in place of N in the
+norm of H^(s′,𝗋′)_sc, the embedding H^(s,𝗋)_sc ↪ H^(s′,𝗋′)_sc is compact. *Duality.*
+For u ∈ 𝒮 and v ∈ H^(−s,−𝗋)_sc, ⟨u, v⟩ = ⟨Eu, (E⁻)∗v⟩ + ⟨u, (Id − E⁻E)∗v⟩, where (E⁻)∗ maps H^(−s,−𝗋)_sc to L² and
+(Id − E⁻E)∗ ∈ Ψ^(−∞,−∞)_sc maps it to H^(N,N)_sc; so |⟨u, v⟩| ≤ C‖u‖_(s,𝗋)‖v‖_(−s,−𝗋). Conversely, u ↦ (Eu, u)
+embeds H^(s,𝗋)_sc isometrically into L² × H^(−N,−N)_sc, so by the Hahn–Banach theorem and (C4) a bounded functional on
+H^(s,𝗋)_sc is u ↦ ⟨Eu, f⟩ + ⟨u, g⟩ with f ∈ L² and g ∈ H^(N,N)_sc, that is u ↦ ⟨u, E∗f + g⟩ with
+E∗f + g ∈ H^(−s,−𝗋)_sc. As 𝒮 is dense in H^(s,𝗋)_sc ((C8)), v ↦ ⟨·, v⟩ is a bounded bijection from H^(−s,−𝗋)_sc onto
+the dual of H^(s,𝗋)_sc, and the open mapping theorem gives equivalent norms.
+
+*The regularising family (C8).* τ_t ∈ C_c^∞(ℝ⁸), so T_t ∈ Ψ^(−∞,−∞)_sc. For α ≠ 0, ∂_x^α(χ(tx)) = t^|α| (∂^αχ)(tx)
+is supported where |tx| is bounded above and below, so it is O(⟨x⟩^(−|α|)) uniformly in t, and likewise in ξ; so τ_t
+is bounded in S^(0,0)_sc. On the support of 1 − τ_t, ⟨x⟩⟨ξ⟩ ≥ c/t, so the seminorms of 1 − τ_t in S^(δ,δ)_sc are
+O(t^δ). By (C3), T_t − Id → 0 in norm from H^(s+δ,r+δ)_sc to H^(s,r)_sc, and T_t is bounded on H^(s,r)_sc uniformly in
+t; as 𝒮 is dense in H^(s,r)_sc, T_t → Id strongly there. For a variable order 𝗋,
+‖(T_t − Id)u‖_(s,𝗋) ≤ ‖(T_t − Id)Eu‖ + ‖[E, T_t]u‖ + ‖(T_t − Id)u‖_(−N,−N). The first and last terms tend to 0 by the
+constant case. [E, T_t] = [E, T_t − Id] has an amplitude that tends to 0 in the class of order (s − ½, 𝗋 − ½), by the
+expansion of [[thm:i-b-2-4]] with its seminorm bounds, its first term vanishing; so [E, T_t]u → 0 in L² by the
+boundedness just proved.
+
 #### Matrix-valued operators {#sec:i-a-2-2}
 
 Write Ψ^(m,ℓ) := Ψ^(m,ℓ)_sc(ℝ⁴; ℂ^(N_E)), the N_E × N_E matrices with entries in Ψ^(m,ℓ)_sc(ℝ⁴), by (C7), and
@@ -259,7 +368,7 @@
 write A = ã Id + A′ and B = b̃ Id + B′, with A′ ∈ Ψ^(m−1,ℓ−1) and B′ ∈ Ψ^(m′−1,ℓ′−1). Then
 [A′, B′] ∈ Ψ^(m+m′−2,ℓ+ℓ′−2) by (a); [ã Id, B′] and [A′, b̃ Id] lie there by the first statement; and [ã, b̃] gives
 H_a b. (d) Boundedness, compactness and duality are statements about each entry. For an elliptic A, take
-B₀ := Op(σ(A)⁻¹χ) for a cut-off χ, and run the Neumann series of [HJS, Proposition 2.3] with matrices: AB₀ = Id − R₁,
+B₀ := Op(σ(A)⁻¹χ) for a cut-off χ, and run the Neumann series of (C5) with matrices: AB₀ = Id − R₁,
 R₁ ∈ Ψ^(−1,−1) by (a), and the asymptotic sum Σ_j R₁^j exists entrywise. The microlocal versions are identical. ∎
 
 **Lemma {#lem:i-a-2-2}** (Square roots.) Let 𝒦 be a compact set of h-self-adjoint endomorphisms with spectra in
@@ -373,7 +482,7 @@
 top order it need not act on H^(𝐬−κ𝟏). As t → 0, w_t → v in H^(𝐬−κ𝟏), and Ǎ_εw_t → Ǎ_εv in H^(½(𝐦−𝟏)).
 
 Write Pv = ΦPu + [P, Φ]u (Step 0), so that Ǎ_εPw_t = Ǎ_εT_tΦPu + Ǎ_εT_t[P, Φ]u + Ǎ_ε[P, T_t]v. (This avoids
-[Ǎ_ε, T_t], which for a variable decay order is bounded only in ⋂_δ Ψ^(𝐤−κ𝟏−𝟏+(0,δ)) [HJS, p. 79].) The first term
+[Ǎ_ε, T_t], which for a variable decay order is bounded only in ⋂_δ Ψ^(𝐤−κ𝟏−𝟏+δ𝟏), by (C6).) The first term
 tends to Ǎ_εΦPu in H^(½(𝟏−𝐦)+κ𝟏), since T_t → Id strongly on H^(𝐬−𝐦+𝟏) and Ǎ_ε ∈ Ψ^(𝐤−κ𝟏) for the fixed ε. The
 second is bounded in Ψ^(−∞,−∞) uniformly in t, as Ǎ_ε and [P, Φ] have disjoint microsupports and T_t is bounded in
 Ψ^(0,0), and it tends to Ǎ_ε[P, Φ]u. In the third, [P, T_t] is bounded in Ψ^(𝐦−𝟏) and tends to 0 in Ψ^(𝐦−𝟏+δ𝟏)
@@ -630,7 +739,9 @@
 ρ²Diff¹_b = ρ · ρDiff¹_b with ρDiff¹_b ⊂ Diff¹_sc. The symbol of ρDiff¹_b at ρ = 0 is linear in (ξ, η): its
 zeroth-order part lies in ρC^∞. Self-adjointness follows from [[lem:i-a-2-1]] (b).
 
-(c) By [HJS, (7.33)–(7.34), p. 50], for covectors τ dx/x² + μ·dy/x,
+(c) With fibre coordinates (ξ′, η′) dual to (x, y), so that τ = x²ξ′ and μ = xη′ [Mel94, (5.20), p. 18], the chain
+rule turns H_p = ∂_(ξ′)p ∂_x − ∂_xp ∂_(ξ′) + ∂_(η′)p·∂_y − ∂_yp·∂_(η′) [Mel94, (5.22), p. 19] into, for covectors
+τ dx/x² + μ·dy/x,
 
     H_p = ∂_τp (x²∂_x) + ∂_μp (x∂_y) − (x²∂_xp + xμ·∂_μp)∂_τ − (x∂_yp − x(∂_τp)μ)·∂_μ.
 
@@ -948,8 +1059,9 @@
 Suppose the following.
 
 (a) Near a compact set Λ ⊂ F, P_R = Re_h P has principal symbol p Id with p real. Then H_p = μ𝖵 near Λ, where μ > 0
-is a weight of order 𝐦 − 𝟏 and 𝖵 is a smooth vector field tangent to F ([HJS, (7.34)]; at fibre infinity 𝖵 = ρ_∞H_p
-for 𝐦 = 2, and over ∂X it is given by [[eq:i-a-4-4]]). Fix a sign ε_f and set 𝖧_f := ε_f𝖵, the *forward* field.
+is a weight of order 𝐦 − 𝟏 and 𝖵 is a smooth vector field tangent to F ([Mel94, Lemma 5, (5.17), p. 18]; at fibre
+infinity 𝖵 = ρ_∞H_p for 𝐦 = 2, and over ∂X it is given by [[eq:i-a-4-4]]). Fix a sign ε_f and set 𝖧_f := ε_f𝖵, the
+*forward* field.
 
 (b) P_I = P_I^sub + P_I^abs, where P_I^sub ∈ Ψ^(𝐦−𝟏) is h-self-adjoint and ε_fP_I^abs = −c L^(∗h)L + K′ with c ≥ 0
 a constant, L of order ½𝐦 and WF′(K′) ∩ W̄ = ∅ for a neighbourhood W of Λ.
@@ -996,9 +1108,10 @@
 Choose C_z ≥ 1 + sup_O (2|𝗄_εϱ⁻¹𝖧_fϱ| + 2‖p′‖), uniformly in ε since 𝗄_ε ∈ (𝗄 − κ, 𝗄]. Then Q_ε ≥ C_z Id. It is a
 symbol of the logarithmic class of (C6), and so is Q_ε^(1/2). To see this, write Q_ε = Q₀ + Λ_ϱ Id with
 Q₀ := (2C_z + 2𝗄_εϱ⁻¹𝖧_fϱ) Id − 2p′ ≥ C_z Id, bounded, and Λ_ϱ := 2(𝖧_f𝗄) log ϱ ≥ 0, scalar. By Cauchy's formula as in
-[[lem:i-a-2-2]], ∂_Λ^j(Q₀ + Λ)^(1/2) = O((C_z + Λ)^(½−j)), and the derivatives of Q₀ and of Λ_ϱ along the vector fields
-⟨x⟩^(−δ)𝒱_b of (C6) are bounded; by the chain rule Q_ε^(1/2) lies in the class for every δ > 0. ([[lem:i-a-2-2]] does
-not apply to Q_ε/(1 + |log ϱ|), which is not bounded below where 𝖧_f𝗄 = 0; [HJS, p. 81] notes the point.)
+[[lem:i-a-2-2]], ∂_Λ^j(Q₀ + Λ)^(1/2) = O((C_z + Λ)^(½−j)); each derivative of Q₀ and of Λ_ϱ gains its weight up to a
+power of 1 + log⟨x⟩ + log⟨ξ⟩, and Λ_ϱ is bounded by such a power. By the chain rule Q_ε^(1/2) lies in the class of (C6)
+of order (δ, δ) for every δ > 0, as in [[lem:i-b-2-12]]. ([[lem:i-a-2-2]] does not apply to Q_ε/(1 + |log ϱ|), which
+is not bounded below where 𝖧_f𝗄 = 0.)
 
 *Decomposition.* As in [[sec:i-a-4]], σ(ε_fC_ε) = μ[𝖧_f(ǎ_ε²) Id + 2ǎ_ε²p′] + ε_fσ(Ǎ²P_I^abs + P_I^absǍ²), and
 
```

### Chapter 03
```diff
--- /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/03-orig.md	2026-11-20 17:43:30.305919616 +0000
+++ chapters/03-theorems.md	2026-11-20 17:43:45.593351285 +0000
@@ -362,7 +362,9 @@
   massless Vlasov limits, for fields that are caustic-free families of dusts meeting the hypotheses stated there, as
   weak limits of class vacuum metrics along odd numbers of dusts ([[thm:vlasov]]), also with the two radial dusts of
   [[thm:two-dusts]] added to a small field, as weak limits on domains of the type of Ω inside the adapted domain of
-  [[cor:class-two-dust]], not on the whole of that domain ([[cor:vlasov-two-dust]]); and exactly localised vacuum data
+  [[cor:class-two-dust]], not on the whole of that domain, under the hypothesis of both corollaries that the outgoing
+  packet of the two-dust background does not reach its inner sphere, {u1 ≤ u ≤ u2} ∩ Ω₂ ∩ {R = a} = ∅, which the
+  construction of that background does not decide ([[cor:vlasov-two-dust]]); and exactly localised vacuum data
   near the initial data of an explicit two-dust background of [[thm:two-dusts]] ([[sec:bg-data]]): on a vacuum band
   of the initial slice (a shell {R1 < r < R2} whose closure lies where the background is vacuum), data equal to the
   background's outside a compact subset of the band and vacuum in the band, whose first-order part in a small
```

### Chapters 32, 35 and the crosswalks
```diff
diff --git a/research/warp-drive/paper/reader/chapters/32-s13-gauge-potential.md b/research/warp-drive/paper/reader/chapters/32-s13-gauge-potential.md
index ea7d2ad1..4184df72 100644
--- a/research/warp-drive/paper/reader/chapters/32-s13-gauge-potential.md
+++ b/research/warp-drive/paper/reader/chapters/32-s13-gauge-potential.md
@@ -442,8 +442,8 @@ S_sub(P) := −iH_G + σ_sub(P), σ_sub(P) being the matrix p̃_1 − (1/2i)Σ_j
 [[prop:np-10-18]] (iii). The static Christoffel symbols are Γ^t_tr = f′/(2f), Γ^r_tt = ff′/2, Γ^r_rr = −f′/(2f),
 Γ^r_ab = −rf(g_𝕊)_ab, Γ^a_rb = r⁻¹δ^a_b and the Γ^a_bc of g_𝕊; the others vanish.
 
-**Proposition {#prop:np-10-17-i}** (The subprincipal operator; [Hin17, Proposition 4.1].) For every metric g, on
-half-densities by |dg| and in a coordinate frame, □_g = 2δ_gG_gδ*_g has principal part G Id and
+**Proposition {#prop:np-10-17-i}** (The subprincipal operator; [Hin17, Proposition 4.1, p. 20] on 1-forms.) For every
+metric g, on half-densities by |dg| and in a coordinate frame, □_g = 2δ_gG_gδ*_g has principal part G Id and
 subprincipal symbol the matrix iΓ^μ_(αν)∂_(ζ_α)G. Equivalently, S_sub(□_g) = −i∇^(π*T*)_(H_G).
 
 *Proof.* By [[prop:np-10-16]] (i), □_g = ∇*∇ − Ric, and the Ricci term is of order zero. The proof of
diff --git a/research/warp-drive/paper/reader/chapters/35-s16-iota-plus.md b/research/warp-drive/paper/reader/chapters/35-s16-iota-plus.md
index 51112d26..d691b225 100644
--- a/research/warp-drive/paper/reader/chapters/35-s16-iota-plus.md
+++ b/research/warp-drive/paper/reader/chapters/35-s16-iota-plus.md
@@ -1337,8 +1337,9 @@ weighted space holds on {Re ζ < ℓ_I}: there H_s is the transform of −χΠ_s
 [½, 1). The remainder, h minus the finite expansion, is holomorphic in the weaker weight in which h(ϰ) is, and bounded in
 the ℓ_I-weighted space locally uniformly in ϰ, the constants of Steps 1–5 being built from N_sf(ϰ)⁻¹ and fixed-circle
 integrals. A locally bounded map g from an open subset of ℂ into a Banach space X such that x* ∘ g is holomorphic for
-every x* in a subspace of X* that separates the points of X is holomorphic ([AN00, Theorem 3.1, p. 787]); applied with X
-the ℓ_I-weighted space and the functionals of the larger space, this shows that the remainder is holomorphic in the
+every x* in a subspace of X* that separates the points of X is holomorphic ([ABK20, Theorem 1.1, p. 2], a locally
+bounded map being locally L¹-bounded); applied with X the ℓ_I-weighted space and the functionals of the larger space,
+this shows that the remainder is holomorphic in the
 ℓ_I-weighted space. So [[eq:iii-g1-3-3]] is finite-meromorphic on {Re ϰ < ℓ_I}. Its principal part at ϰ_0 is obtained by
 expanding R^(±ϰ) about ϰ_0: its Laurent coefficients are finite combinations of R^(−ϰ_0)(log R)^iA_(−j)(log
 R)^(i′)R^(2+ϰ_0), with A_(−j) those of N_sf⁻¹. These have finite rank and do not depend on (s, μ), as the inverses agree
diff --git a/research/warp-drive/paper/reader/crosswalk/03-theorems.tsv b/research/warp-drive/paper/reader/crosswalk/03-theorems.tsv
index 61d48165..b975bb0d 100644
--- a/research/warp-drive/paper/reader/crosswalk/03-theorems.tsv
+++ b/research/warp-drive/paper/reader/crosswalk/03-theorems.tsv
@@ -19,4 +19,4 @@ eq:bondi-law	paper/RESPONSE-HL-5D.md:430	P (3.3)	squares written (d_v p_i)^2
 eq:flux-mean	paper/RESPONSE-HL-5D.md:679	P (6.1) = NP (9.10) with the factor 1 - π/2	
 sec:settling-statement	paper/RESPONSE-HL-5D.md:1180-1269; paper/RESPONSE-HL-5D.md:777-796	P 8.7-8.8, 8.2	
 thm:settling	paper/RESPONSE-HL-5D.md:1239-1259; docket68/n1star/proof5/PART-VII-ASSEMBLY.md:94-96	P Theorem 4 = proof5 Part VII Theorem 0.2	parameters cited by the stability keys eq:iii-i9-1-1, eq:iii-f1-2-2, def:iii-j-g-plus, def:iii-i9-gap, def:iii-i10-1-3 and ch:s27 (row w1); former pending stability-parameters resolved; (ii) states the norm < delta of Part VII Theorem 0.2 (ii)
-sec:further-results	paper/RESPONSE-HL-5D.md:1486-1863 (first sentences)	P section 9	qualifiers restored from P 1499-1501 (harmonic gauge), 1792-1795 (class stability), 1798-1803 (Vlasov), 1820-1837 (localised data), 1609-1620 (the mean correction is not a proved value)
+sec:further-results	paper/RESPONSE-HL-5D.md:1486-1863 (first sentences)	P section 9	qualifiers restored from P 1499-1501 (harmonic gauge), 1792-1795 (class stability), 1798-1803 (Vlasov), 1820-1837 (localised data), 1609-1620 (the mean correction is not a proved value); G-SWEEP C3: the Vlasov two-dust summary carries the hypothesis of cor:class-two-dust and cor:vlasov-two-dust that the outgoing packet does not reach R = a
diff --git a/research/warp-drive/paper/reader/crosswalk/20-s01-spectral-bounded.tsv b/research/warp-drive/paper/reader/crosswalk/20-s01-spectral-bounded.tsv
index 65d9ce4e..7db887c8 100644
--- a/research/warp-drive/paper/reader/crosswalk/20-s01-spectral-bounded.tsv
+++ b/research/warp-drive/paper/reader/crosswalk/20-s01-spectral-bounded.tsv
@@ -13,9 +13,9 @@ eq:i-a-1-4	docket68/n1star/proof5/PART-I-SPECTRAL.md:124-126	I.A (1.4)
 sec:i-a-1-4	docket68/n1star/proof5/PART-I-SPECTRAL.md:140-182	I.A section 1.4	lambda_max and lambda_min written max spec and min spec
 def:i-a-admissible	docket68/n1star/proof5/PART-I-SPECTRAL.md:149-173	I.A order pairs, (O1)-(O3)	private key; unnumbered in source
 eq:i-a-1-5	docket68/n1star/proof5/PART-I-SPECTRAL.md:163-165	I.A (1.5)	
-rem:i-a-1-1	docket68/n1star/proof5/PART-I-SPECTRAL.md:184-190	I.A Remark 1.1	Part I.B (in preparation) replaced by ch:s02; D186 tag and READ dropped; conditional of source 188-189 kept: would supply ..., not needed in this chapter
+rem:i-a-1-1	docket68/n1star/proof5/PART-I-SPECTRAL.md:184-190	I.A Remark 1.1	Part I.B (in preparation) replaced by ch:s02; D186 tag and READ dropped; conditional of source 188-189 kept: would supply ..., not needed in this chapter; G5: [HJS, p. 77] quote replaced by a pointer to sec:i-a-2-1
 sec:i-a-2	docket68/n1star/proof5/PART-I-SPECTRAL.md:192	I.A section 2	
-sec:i-a-2-1	docket68/n1star/proof5/PART-I-SPECTRAL.md:194-245	I.A section 2.1, (C1)-(C8)	[HJS] black boxes stated with pages; access date and the aside at 244-245 dropped
+sec:i-a-2-1	docket68/n1star/proof5/PART-I-SPECTRAL.md:194-245	I.A section 2.1, (C1)-(C8)	[HJS] black boxes stated with pages; access date and the aside at 244-245 dropped; G-SWEEP G5: (C1)-(C8) re-sourced from [HJS] (lecture notes, unpublished) to [Mel94] (published; pages of the author's corrected online edition, read 2026-11-20); adjoints, seminorm bounds, compactness, duality, microlocal parametrix, the variable-order classes and spaces (via sec:i-b-2 at h = 1) and the regularising family proved in the section; [HJS] no longer cited
 sec:i-a-2-2	docket68/n1star/proof5/PART-I-SPECTRAL.md:247-252	I.A section 2.2	rank N written N_E; M_N(...) written in words
 lem:i-a-2-1	docket68/n1star/proof5/PART-I-SPECTRAL.md:254-277	I.A Lemma 2.1	D186 tag dropped (263)
 lem:i-a-2-2	docket68/n1star/proof5/PART-I-SPECTRAL.md:279-292	I.A Lemma 2.2	weight lambda renamed Lambda
@@ -43,7 +43,7 @@ eq:i-a-4-2	docket68/n1star/proof5/PART-I-SPECTRAL.md:604	I.A (4.2)
 eq:i-a-4-3	docket68/n1star/proof5/PART-I-SPECTRAL.md:609	I.A (4.3)	
 rem:i-a-4-3	docket68/n1star/proof5/PART-I-SPECTRAL.md:703-708	I.A Remark 4.3	computed in 10.79 (hthresh5.py) replaced by pointer to ch:s13, ch:s14
 sec:i-a-4-2	docket68/n1star/proof5/PART-I-SPECTRAL.md:710-770	I.A section 4.2	
-lem:i-a-4-4	docket68/n1star/proof5/PART-I-SPECTRAL.md:712-753	I.A Lemma 4.4	READ dropped (745)
+lem:i-a-4-4	docket68/n1star/proof5/PART-I-SPECTRAL.md:712-753	I.A Lemma 4.4	READ dropped (745); G5: (c) derived by the chain rule from [Mel94, (5.20), (5.22)] in place of [HJS, (7.33)-(7.34)]
 eq:i-a-4-4	docket68/n1star/proof5/PART-I-SPECTRAL.md:724-725	I.A (4.4)	
 eq:i-a-4-5	docket68/n1star/proof5/PART-I-SPECTRAL.md:758-760	I.A (4.5)	
 eq:i-a-4-6	docket68/n1star/proof5/PART-I-SPECTRAL.md:764-766	I.A (4.6)	
@@ -69,7 +69,7 @@ sec:i-a-4-6	docket68/n1star/proof5/PART-I-SPECTRAL.md:1128-1135	I.A section 4.6
 lem:i-a-4-10	docket68/n1star/proof5/PART-I-SPECTRAL.md:1137-1144	I.A Lemma 4.10 = [Hin26c] Remark 9.14, (9.53)	
 sec:i-a-5	docket68/n1star/proof5/PART-I-SPECTRAL.md:1146	I.A section 5	
 prop:i-a-5-1	docket68/n1star/proof5/PART-I-SPECTRAL.md:1148-1159	I.A Proposition 5.1	
-prop:i-a-5-2	docket68/n1star/proof5/PART-I-SPECTRAL.md:1161-1265	I.A Proposition 5.2	sign epsilon renamed eps_f, curve length T renamed t_1, scalar lambda renamed Lambda_rho; D186, D187, D195 dropped (1198, 1208, 1235, 1255); large constant M renamed C_z (M reserved for orders)
+prop:i-a-5-2	docket68/n1star/proof5/PART-I-SPECTRAL.md:1161-1265	I.A Proposition 5.2	sign epsilon renamed eps_f, curve length T renamed t_1, scalar lambda renamed Lambda_rho; D186, D187, D195 dropped (1198, 1208, 1235, 1255); large constant M renamed C_z (M reserved for orders); G5: [HJS, (7.34)] replaced by [Mel94, Lemma 5, (5.17)]; Q_eps^(1/2) via the class of (C6) and lem:i-b-2-12
 eq:i-a-5-1	docket68/n1star/proof5/PART-I-SPECTRAL.md:1183-1184	I.A (5.1)	
 rem:i-a-5-2-uses	docket68/n1star/proof5/PART-I-SPECTRAL.md:1267-1278	I.A The two uses	private key
 sec:i-a-6	docket68/n1star/proof5/PART-I-SPECTRAL.md:1280	I.A section 6	
diff --git a/research/warp-drive/paper/reader/crosswalk/32-s13-gauge-potential.tsv b/research/warp-drive/paper/reader/crosswalk/32-s13-gauge-potential.tsv
index a9721030..5a919045 100644
--- a/research/warp-drive/paper/reader/crosswalk/32-s13-gauge-potential.tsv
+++ b/research/warp-drive/paper/reader/crosswalk/32-s13-gauge-potential.tsv
@@ -26,7 +26,7 @@ prop:np-10-18	docket68/n1star/N1STAR-PROOF.md:3928-3956	NP 10.18, Prop 10.15 (i)
 prop:np-10-19-i	docket68/n1star/N1STAR-PROOF.md:4000-4004; docket68/n1star/N1STAR-PROOF.md:4034-4036	NP 10.19, Prop 10.16 (i); deduced (a), first clause	(a), (b) derived by hand (A_w = -gamma M_D, A_w + S-bar = Xi S-bar Xi, Xi the radial reflection); (c) is deduced (a), fixing A_w against p_in of S1; replaces hienergy5.py V1
 lem:iii-d-5-1	docket68/n1star/proof5/PART-III-D-GAUGEPOT.md:249-264	III.D Lemma 5.1	computed sentence 240-247 replaced by prop:np-10-18 (iii)
 sec:iii-d-5-2	docket68/n1star/proof5/PART-III-D-GAUGEPOT.md:269-288	III.D §5.2	facts (a)-(d); NP 10.17 (i), (iii)-(v), 10.19 (iii) carried here, (ii) and 10.19 (ii) cited to S12
-prop:np-10-17-i	docket68/n1star/N1STAR-PROOF.md:3854-3855	NP 10.17, Prop 10.14 (i)	derived in coordinates; replaces trap5.py T0
+prop:np-10-17-i	docket68/n1star/N1STAR-PROOF.md:3854-3855	NP 10.17, Prop 10.14 (i)	derived in coordinates; replaces trap5.py T0; header cites [Hin17, Proposition 4.1, p. 20] (arXiv 1502.03183v2), the 1-form case; quoted in Appendix A (G-SWEEP minor item)
 prop:np-10-17-iii	docket68/n1star/N1STAR-PROOF.md:3860-3862	NP 10.17, Prop 10.14 (iii)	Gram matrix and H_G C = 0 derived; replaces trap5.py T2
 prop:np-10-17-iv	docket68/n1star/N1STAR-PROOF.md:3863	NP 10.17, Prop 10.14 (iv)	connection derived in the static chart; replaces trap5.py T3
 prop:np-10-17-v	docket68/n1star/N1STAR-PROOF.md:3864-3865	NP 10.17, Prop 10.14 (v)	eigenvalues of a 3x3 matrix; replaces trap5.py T4
diff --git a/research/warp-drive/paper/reader/crosswalk/35-s16-iota-plus.tsv b/research/warp-drive/paper/reader/crosswalk/35-s16-iota-plus.tsv
index 9b208ccd..8e90e821 100644
--- a/research/warp-drive/paper/reader/crosswalk/35-s16-iota-plus.tsv
+++ b/research/warp-drive/paper/reader/crosswalk/35-s16-iota-plus.tsv
@@ -79,7 +79,7 @@ lem:iii-g1-2-1	docket68/n1star/proof5/PART-III-G2-IOTA.md:130-180	III.G1 Lemma 2
 eq:iii-g1-2-1	docket68/n1star/proof5/PART-III-G2-IOTA.md:133-135	III.G1 (2.1)	
 lem:iii-g1-2-2	docket68/n1star/proof5/PART-III-G2-IOTA.md:184-203	III.G1 Lemma 2.2	
 sec:iii-g1-3	docket68/n1star/proof5/PART-III-G2-IOTA.md:205-419	III.G1 section 3	
-thm:iii-g1-3-1	docket68/n1star/proof5/PART-III-G2-IOTA.md:207-419	III.G1 Theorem 3.1 = [Hin26] Proposition 9.4	(2) at the final order ell_I; Step 5 (ii) with d_1 = 0 folded; Steps 3-4 variable mu renamed nu, Omega renamed O; [AN00, Theorem 3.1] stated at its use
+thm:iii-g1-3-1	docket68/n1star/proof5/PART-III-G2-IOTA.md:207-419	III.G1 Theorem 3.1 = [Hin26] Proposition 9.4	(2) at the final order ell_I; Step 5 (ii) with d_1 = 0 folded; Steps 3-4 variable mu renamed nu, Omega renamed O; [AN00, Theorem 3.1] stated at its use; G-SWEEP minor item: [AN00, Theorem 3.1, p. 787] (paywalled, not read) replaced by [ABK20, Theorem 1.1, p. 2] (arXiv 1904.03088v1, read 2026-11-20), quoted in Appendix A
 eq:iii-g1-3-1	docket68/n1star/proof5/PART-III-G2-IOTA.md:210-212	III.G1 (3.1)	
 eq:iii-g1-3-2	docket68/n1star/proof5/PART-III-G2-IOTA.md:216-218	III.G1 (3.2)	
 eq:iii-g1-3-3	docket68/n1star/proof5/PART-III-G2-IOTA.md:224-227	III.G1 (3.3)	
```

## 5. Exact texts for the coordinator

Apply in the order listed. Every old text was checked to occur exactly once in the live file at the time of writing.
Applying all 24 to a copy of the tree gives `lint --chapters` 0 hits and `assemble --check` 0 problems (outputs in §6).
Dependencies:

- Remove the [HJS] reference (98, item 4) only together with the ch. 21, 22 and 23 texts. Ch. 20 already cites no [HJS].
- The [AN00] removal goes with the ch. 35 edit, which is already made.
- The 95 crosswalk rows go with the 95 entries.

New Appendix A labels: thm:std-melrose-sc, thm:std-hin17-subprincipal, thm:std-abk-holomorphy. Removed:
thm:std-hjs-calculus and thm:std-hin26a-cform; no chapter references either by label (checked by grep).

### Chapter 95 (Appendix A) (chapters/95-standard-results.md)

**95.1** opening: the page convention for [Mel94]

Old text:
```
the arXiv text of [BGP] carries the book's page numbers, [See64], [MM87] and [DS41] are cited by their journal pages,
[Mel93] by the page of the author's online edition (version 5.0E, 1993), [Hö90], [RS1] and [Tre19] by the pages of
the printed books, and [DLMF] by equation number. Quotation marks enclose the source's own wording, transcribed into
this edition's typography; an ellipsis marks words of the statement left out because no proof here depends on them.
Inside each item the letters are the source's.
```
New text:
```
the arXiv text of [BGP] carries the book's page numbers, [See64], [MM87] and [DS41] are cited by their journal pages,
[Mel93] and [Mel94] by the pages of the author's online editions (for [Mel93] version 5.0E, 1993, for [Mel94] the
corrected edition of 1997), [Hö90], [RS1] and [Tre19] by the pages of the printed books, and [DLMF] by equation number.
Quotation marks enclose the source's own wording, transcribed into this edition's typography; an ellipsis marks words of
the statement left out because no proof here depends on them. Inside each item the letters are the source's.
```

**95.2** remove thm:std-hin26a-cform

Old text:
```
**Theorem {#thm:std-hin26a-cform}** ([Hin26a, Proposition 5.1, p. 38].) "Fix any v ∈ (0, 1) and C0 > 0. Fix moreover
α_sf, α_K ∈ ℝ subject to the conditions α_sf < −1/2 and α_K > α_sf + 1/2. Set ρ_sf = r⁻¹ and ρ_K = r/t; put
w := ρ_sf^(α_sf+1) ρ_K^(α_K) and w′ := ρ_sf^(α_sf+1). Then for all sufficiently small e > 0, there exists a 1-form
c ∈ ρ_sf C^∞(M; T*) satisfying the following properties for some r0 > 100m, 0 < δ_r < (4r0)⁻¹, and δ_sf > 0:
- (1) (Basic properties.) c is stationary, i.e., ℒ_(∂_t) c = 0 … Moreover, rc ∈ C^∞(M; T*) is past timelike and
  nowhere vanishing.
- (2) (Explicit regions.) We have c = (1/2) r0^(−2) (r0 dt − v(r − r0) dr) for r0/2 ≤ r ≤ 2r0 (5.1), and
  c = r⁻¹ (dt − v dr) for r ≥ 3r0 (5.2).
- (3) (Interior saddle point …) The endomorphism S_(g,c,e) from Lemma 3.9 is positive definite (with respect to the
  inner product B_(g,c,e) on T* from Lemma 3.3) at all points with |r − r0| ≤ (5/6) r0 √(e/v).
- (4) (Saddle point at ∂𝒦⁺ …) For ρ_sf ≤ 2δ_r and ρ_K ≤ 2δ_r, the endomorphism r²(−ℓ_(g,c,e)(dw/w) + S_(g,c,e)) is
  positive definite.
- (5) (Sink in sf° …) At points where r/t/v ∈ [1 − 2δ_sf, 1 + 2δ_sf] and r⁻¹ ≤ 2δ_r, the endomorphism
  r²(−ℓ_(g,c,e)(dw′/w′) + S_(g,c,e)) is positive definite.
- (6) (Positivity along escape functions …) For m ≤ r ≤ r0 − r0√(e/v), −ℓ_(g,c,e)(−dr) is positive definite. For
  r0 + r0√(e/v) ≤ r < ∞, −ℓ_(g,c,e)(dr) is positive definite. On sf ∩ {r/t ∈ [δ_r, v(1 − δ_sf)]},
  −r² ℓ_(g,c,e)(d(r/t)) is positive definite, and on sf ∩ {r/t ∈ [v(1 + δ_sf), 10]}, −r² ℓ_(g,c,e)(−d(r/t)) is
  positive definite."

The objects S_(g,c,e), B_(g,c,e) and ℓ_(g,c,e) are those of [Hin26a, Lemmas 3.3 and 3.9], and r/t/v in (5) is (r/t)/v.


```
New text:
```
(empty: delete the old text)
```

**95.3** replace thm:std-hjs-calculus by thm:std-melrose-sc and thm:std-hin17-subprincipal

Old text:
```
**Theorem {#thm:std-hjs-calculus}** ([HJS, (2.1), Propositions 2.3, 3.7, 3.11, 3.13, 4.9, 4.10, 7.4, 7.5 and 10.1,
Definitions 7.2 and 10.2, Sections 7.5 and 10.1–10.3, Lemma 12.5, pp. 9–95].) The scattering calculus Ψ^(m,l)_sc on
ℝⁿ, n arbitrary, and on scattering manifolds M has the following properties.

(1) Composition [HJS, (2.1), p. 9]: Ψ^(m,l)_sc ∘ Ψ^(m′,l′)_sc ⊂ Ψ^(m+m′,l+l′)_sc.

(2) Ellipticity [HJS, Proposition 2.3, p. 12]: "Every elliptic element of the scattering calculus has a parametrix",
that is, a B ∈ Ψ^(−m,−l)_sc with AB − Id ∈ Ψ^(−∞,−∞)_sc ∋ BA − Id ((2.9)).

(3) Duality [HJS, Proposition 3.7, p. 19]: the L² pairing "extends boundedly to a (conjugate linear) isomorphism
H^(−s,−r)_sc ≅ (H^(s,r)_sc)*".

(4) Boundedness [HJS, Proposition 3.11 and Remark 3.12, p. 20]: "If A ∈ Ψ^(m,l)_sc, then, for all s, r ∈ ℝ, A maps
A : H^(s,r)_sc → H^(s−m,r−l)_sc, and does so boundedly". Moreover "Op(a), viewed as an element of
L(H^(s,r)_sc, H^(s−m,r−l)_sc), depends continuously on a in the sense that if a_1, a_2, ⋯ ∈ S^(m,l)_sc is some
sequence such that a_n → a in S^(m,l)_sc, then Op(a_n) → Op(a) in L(H^(s,r)_sc, H^(s−m,r−l)_sc)".

(5) Compactness [HJS, Proposition 3.13, p. 20]: "For any s, s′, r, r′, with s < s′ and r < r′, the embedding
H^(s′,r′)_sc ↪ H^(s,r)_sc is compact."

(6) Microlocality [HJS, Proposition 4.9, p. 27]: "If A ∈ Ψ^(m,l)_sc and u ∈ 𝒮′, then
WF^(s,r)_sc(Au) ⊆ WF^(s+m,r+l)_sc(u) ∩ WF′_sc(A)."

(7) Microlocal parametrix [HJS, Proposition 4.10, p. 29]: "Suppose that A ∈ Ψ^(m,l)_sc is elliptic at
p ∈ ∂(ℝⁿ × ℝⁿ). Then, there exists a B ∈ Ψ^(−m,−l)_sc such that AB − 1, BA − 1 have WF′_sc disjoint from p. This also
applies with p replaced by any closed subset."

(8) Adjoints and principal symbols [HJS, Definition 7.2, p. 48; Proposition 7.4, pp. 49–50]. The principal symbol of
A ∈ Ψ^(m,l)_sc(M) is a class σ_(m,l)(A) ∈ S^(m,l)_sc(M)/S^(m−1,l−1)_sc(M). Further,
"A ∈ Ψ^(m,l)_sc(M) ⇒ A* ∈ Ψ^(m,l)_sc(M)", and "σ_(m1+m2,l1+l2)(AB) = σ_(m1,l1)(A) σ_(m2,l2)(B)" (7.29).

(9) Commutators [HJS, Proposition 7.5, p. 50]: for A ∈ Ψ^(m1,l1)_sc(M) and B ∈ Ψ^(m2,l2)_sc(M),
"[A, B] ∈ Ψ^(m1+m2−1,l1+l2−1)_sc(M) and σ_(m1+m2−1,l1+l2−1)(i[A, B]) = {σ_(m1,l1)(A), σ_(m2,l2)(B)}" (7.30). Here
{p, a} = H_p a (7.31), with the scattering Hamilton vector field H_p of (7.34).

(10) Bundles [HJS, Section 7.5, pp. 52–53]: "Ψ^(m,l)_sc(M; E, F) := C^∞(X; Hom(E, F)) ⊗ Ψ^(m,l)_sc(M)" (7.43), the
tensor product being over C^∞(M).

(11) Variable spatial orders [HJS, Sections 10.1–10.3, pp. 77–80]. "We will take the differential order to be
constant, and the spatial order to be variable" (p. 77). A variable order is a classical symbol of order (0, 0).
Proposition 10.1 (p. 79): "Let A ∈ Ψ^(m,l)_sc be elliptic. Then there exists a parametrix B ∈ Ψ^(−m,−l)_sc such that
AB − Id ∈ Ψ^(−∞,−∞)_sc ∋ BA − Id." Definition 10.2 (p. 80): for s ∈ ℝ and a variable spatial order r, a constant
order L ≤ r, an elliptic A ∈ Ψ^(s,r)_sc and Λ = ⟨ξ⟩^s ⟨x⟩^L, "the Sobolev space H^(s,r) is defined to be the set of
u ∈ 𝒮′(ℝⁿ) such that Au ∈ L² and Λu ∈ L²", with ‖u‖²_(H^(s,r)) = ‖Au‖²_(L²) + ‖Λu‖²_(L²) (10.8). By the text that
follows, this space is independent of the choices and is a Hilbert space, and B ∈ Ψ^(m,l)_sc maps H^(s,r) to
H^(s−m,r−l) boundedly.

(12) A regularising family [HJS, Lemma 12.5, p. 95]: "There exists a family of T_r ∈ Ψ^(−∞,−∞)_sc for r ∈ (0, r0]
with some r0 > 0 such that T_r → Id (12.7) as r → 0 with respect to the strong operator topology". The family is
T_r = χ(r⟨z⟩) Op(χ(⟨rζ⟩)), with χ ∈ C_c^∞(ℝⁿ) even, equal to 1 near the origin and decreasing on [0, ∞). Its proof
records that one "can require T_r being uniformly bounded in Ψ^(0,0)_sc and T_r → Id in the operator topology of
Ψ^(δ,δ)_sc".


```
New text:
```
**Theorem {#thm:std-melrose-sc}** ([Mel94, (1.1), p. 4; (4.1)–(4.3) and Definition 1, pp. 12–13; Definition 2, p. 14;
(5.1), p. 15; Proposition 3, (5.12)–(5.14), p. 17; Proposition 4, Lemma 5, (5.19)–(5.20), p. 18; (5.22) and (5.27), p.
19; Proposition 5 and Lemma 6, p. 20; (5.34), p. 21; (7.1), (7.2) and (7.6), p. 23].) Let X be a compact manifold with
boundary and x a boundary defining function.

(1) (1.1), p. 4: SP : ℝⁿ ∋ z ↦ ((1 + |z|²)^(−1/2), z(1 + |z|²)^(−1/2)) ∈ S^n_+, the closed upper half of the unit sphere
of ℝ^(n+1). "This is clearly an isomorphism onto the interior of S^n_+, so it compactifies ℝⁿ. We call this the radial
compactification. Indeed the function t_0 = (1 + |z|²)^(−1/2) is a defining function for the boundary of S^n_+, hence so
is x = 1/|z|, which is defined in t_0 < 1."

(2) Definition 1, p. 13: "The space Ψ^(m,l)_scc(S^n_+) consists of those operators A : Ċ^∞(S^n_+) → Ċ^∞(S^n_+) such that
if A′ is defined by SP^∗(Aϕ) = A′(SP^∗ϕ) ∀ ϕ ∈ Ċ^∞(S^n_+) (4.4) then A′ is of the form (4.1), (4.2)". These are the
kernels A′(z, z′) = (2π)^(−n) ∫ e^(i(z−z′)·ζ) a_L(z, ζ) dζ (4.1), "where the amplitude satisfies the estimates |D_z^α
D_ζ^β a_L(z, ζ)| ≤ C_αβ (1 + |z|)^(−l−|α|) (1 + |ζ|)^(m−|β|)" (4.2); SP^∗ : Ċ^∞(S^n_+) → 𝒮(ℝⁿ) "is a isomorphism, with
Ċ^∞(X) = ⋂_k x^k C^∞(X)" (4.3). By Definition 2 (p. 14) the classical subspace Ψ^(m,l)_sc(S^n_+) consists of the
operators with a_L ∈ SP^∗(ρ_N^l ρ_σ^(−m) C^∞(S^n_+ × S^n_+)), where "SP^∗ρ_N = (1 + |z|²)^(−1/2) and SP^∗ρ_σ =
(1 + |ζ|²)^(−1/2)" (p. 13); and "we shall let 'sk' stand for either 'sc' or 'scc' but fixed throughout a particular
discussion" (p. 14).

(3) (5.1), p. 15: "Ψ^(m1,l1)_sk(X) ∘ Ψ^(m2,l2)_sk(X) ⊂ Ψ^(m1+m2,l1+l2)_sk(X)."

(4) p. 17: with A^({m,l})(C_scX) = A^(m,l)(^(sc)T̄^∗X)/A^(m−1,l+1)(^(sc)T̄^∗X) (5.12), "Proposition 3 is replaced for
the scattering-conormal calculus by a short exact sequence 0 → Ψ^(m−1,l+1)_scc(X) → Ψ^(m,l)_scc(X) → A^({m,l})(C_scX) →
0 (5.13)", the third map being the symbol map j_(sc,m,l), "and similarly for operators on sections of vector bundles. In
both cases the symbol maps are multiplicative: j_(sc,m1+m2,l1+l2)(A · B) = j_(sc,m1,l1)(A) · j_(sc,m2,l2)(B) A ∈
Ψ^(m1,l1)_sk(X), B ∈ Ψ^(m2,l2)_sk(X), with values in commutative algebras" (5.14). Proposition 3 states the sequence for
the classical calculus "for any compact manifold with boundary, X, and any vector bundles E and F over X", with kernel
Ψ^(m−1,l+1)_sc(X; E, F) (5.10).

(5) Proposition 4, p. 18: "The Poisson bracket on T^∗X extends by continuity from the interior of ^(sc)T̄^∗X to define …
and for any m1, m2, l1, l2 ∈ ℝ j_(sc,m1+m2,l1+l2)([A, B]) = (1/i){j_(sc,m1,l1)(A), j_(sc,m2,l2)(B)} ∀ A ∈
Ψ^(m1,l1)_sk(X), B ∈ Ψ^(m2,l2)_sk(X)" (5.16). Lemma 5, p. 18: "If a ∈ C^∞(^(sc)T̄^∗X; S^(m,l)) the Hamilton vector field
extends from the interior to be of the form H_a = ρ_σ^(−m+1) ρ_N^(l+1) ^(sc)H^(m,l)_a, ^(sc)H^(m,l)_a ∈ 𝒱_b(^(sc)T̄^∗X)
(5.17) and for any b ∈ A^({m′,l′})(^(sc)T̄^∗X) {a, b} = ρ_σ^(−m+1) ρ_N^(l+1) ^(sc)H^(m,l)_a b ∈
A^({m+m′−1,l+l′+1})(^(sc)T̄^∗X) (5.18) …", with ρ_σ = (1 + |ζ|²)^(−1/2) and ρ_N = x (5.19). In coordinates (x, y) with
dual coordinates (ξ, η), "τ = x²ξ, μ = xη" (5.20), and the bracket is {a, b} = ∂_ξa ∂_xb − ∂_xa ∂_ξb + Σ_j (∂_(η_j)a
∂_(y_j)b − ∂_(y_j)a ∂_(η_j)b) (5.22), p. 19.

(6) (5.27), p. 19: "H^(m,l)_sc(X) = {u ∈ C^(−∞)(X); Ψ^(m,−l)_sc(X)u ⊂ L²_sc(X)}"; "For the case of S^n_+,
H^(m,0)_sc(S^n_+) is the image under SP^∗ of the standard Sobolev space H^m(ℝⁿ)."

(7) Proposition 5, p. 20: "For any m, l, M, L ∈ ℝ each A ∈ Ψ^(m,l)_scc(X) defines a continuous linear operator A :
H^(M,L)_sc(X) → H^(M−m,L+l)_sc(X); (5.28) if A ∈ Ψ^(m,l)_sc(X) this map is compact if and only if j_(sc,m,l)(A) ≡ 0."

(8) Lemma 6, p. 20: "If A_j ∈ Ψ^(m−j,l)_sk(X), B_j ∈ Ψ^(m,l+j)_sk(X), and C_j ∈ Ψ^(m−j,l+j)_sk(X), for j ∈ ℕ₀, there
exist asymptotic sums A, B, C ∈ Ψ^(m,l)_sk(X) in the sense that A − Σ_(j=0)^(N−1) A_j ∈ Ψ^(m−N,l)_sk(X), B −
Σ_(j=0)^(N−1) B_j ∈ Ψ^(m,l+N)_sk(X), C − Σ_(j=0)^(N−1) C_j ∈ Ψ^(m−N,l+N)_sk(X) (5.29) and the sums are determined
uniquely modulo Ψ^(−∞,l)_sk(X), Ψ^(m,∞)_sk(X) and Ψ^(−∞,∞)_sc(X) respectively."

(9) (5.34), p. 21: "Ψ^(−∞,∞)_sc(X) ∋ A : C^(−∞)(X) → Ċ^∞(X)".

(10) p. 23: "WF′_sc(A) ⊂ C_scX ∀ A ∈ Ψ^(m,l)_sk(X)" (7.1), C_scX = ∂(^(sc)T̄^∗X) being the boundary of the
fibre-compactified scattering cotangent bundle ((5.4), p. 16); "The scattering pseudodifferential operators are
microlocal in the sense that WF′_sc(A ∘ B) ⊂ WF′_sc(A) ∩ WF′_sc(B)" (7.2); and "WF′_sc(A) = ∅ ⟺ A ∈ Ψ^(−∞,∞)_sc(X)"
(7.6).

By (5.18) the bracket in (5.16) has the orders (m1 + m2 − 1, l1 + l2 + 1), and by (5.13)–(5.14), the symbols commuting,
[A, B] ∈ Ψ^(m1+m2−1,l1+l2+1)_sk(X). The decay order l of [Mel94] has the sign opposite to that of [[sec:i-a-2-1]], where
Ψ^(m,ℓ)_sc is Ψ^(m,−ℓ)_scc(S^n_+) and H^(s,r)_sc is the space of (6).

**Theorem {#thm:std-hin17-subprincipal}** ([Hin17, Definition 3.8, p. 16; Proposition 4.1, p. 20; Theorem 4.8, p. 26].)
Definition 3.8: "For P ∈ Ψ^m(X, E ⊗ Ω^(1/2)) with scalar principal symbol p, there is a well-defined subprincipal
operator S_sub(P) ∈ Diff¹(T^∗X ∖ 0, π^∗E), homogeneous of degree m − 1 with respect to dilations in the fibers of T^∗X ∖
0, defined as follows: If {e_1(x), …, e_N(x)} is a local frame of E, define the operators P_jk ∈ Ψ^m(X, Ω^(1/2)) by
P(Σ_k u_k(x)e_k(x)) = Σ_jk P_jk(u_k)e_j(x), u_k ∈ C^∞(X, Ω^(1/2)). Then S_sub(P)(Σ_k q_k(x, ξ)e_k(x)) := Σ_jk
(σ_sub(P_jk)q_k)e_j − i Σ_k (H_p q_k)e_k. In shorthand notation, S_sub(P) = σ_sub(P) − iH_p, understood in a local frame
as a matrix of first order differential operators." Here σ_sub is the subprincipal symbol of a scalar operator, [Hin17,
(3.3)].

Proposition 4.1, in the setting of [Hin17, Section 4, p. 20]: "Let (M, g) be a smooth manifold equipped with a metric
tensor g of arbitrary signature. Denote by T^kM = ⊗^k T^∗M, k ≥ 1, the bundle of (covariant) tensors of rank k on M. The
metric g induces a metric (which we also call g) on T^kM. We study the symbolic properties of Δ_k = − tr ∇² ∈ Diff²(M,
T^kM), the Laplace-Beltrami operator on M acting on the bundle T^kM. Denote by G ∈ C^∞(T^∗M) the metric function, i.e.
G(x, ξ) = |ξ|²_(G(x)), where G is the dual metric of g." Then: "The subprincipal operator of Δ_k is S_sub(Δ_k)(x, ξ) =
−i∇^(π^∗T^kM)_(H_G) ∈ Diff¹(T^∗M ∖ 0, π^∗T^kM), (4.1) where ∇^(π^∗T^kM) is the pullback connection, with π : T^∗M ∖ 0 →
M being the projection."

After Theorem 4.8 (p. 26): "By restriction, the analogous statements are true for □ acting on subbundles of the tensor
bundle on M, for instance differential forms of all degrees and symmetric 2-tensors."


```

**95.4** add thm:std-abk-holomorphy after thm:std-analytic-fredholm

Old text:
```
(Id + F(z))⁻¹ exists for z off a discrete set S ⊂ D, and it is meromorphic on D with finite-rank residues.

```
New text:
```
(Id + F(z))⁻¹ exists for z off a discrete set S ⊂ D, and it is meromorphic on D with finite-rank residues.

**Theorem {#thm:std-abk-holomorphy}** ([ABK20, pp. 1–2; Theorem 1.1, p. 2].) Let Ω ⊂ ℂ be open and X a complex Banach
space. "We say that f is very weakly holomorphic … if there exists a separating subset W ⊂ X′ such that x′ ∘ f is
holomorphic … for all x′ ∈ W." "We say that a set F of functions from Ω to X is locally L¹-bounded if there exists a
function g ∈ L¹_loc(Ω, ℝ) such that ‖f(ξ)‖_X ≤ g(ξ) holds for almost all ξ ∈ Ω and for all f ∈ F. A single function f :
Ω → X is called locally L¹-bounded if {f} is locally L¹-bounded." Theorem 1.1: "Let X be a Banach space and Ω ⊂ ℂ (Ω ⊂
ℝ^d) be open. A function f : Ω → X is holomorphic (harmonic) if and only if it is locally L¹-bounded and very weakly
holomorphic (very weakly harmonic)."

A locally bounded f is locally L¹-bounded: if K_1 ⊂ K_2 ⊂ … are compact sets whose interiors exhaust Ω and K_0 := ∅,
then g := Σ_j (sup_(K_j) ‖f‖) 1_(K_j ∖ K_(j−1)) is measurable and bounded on compact sets, so g ∈ L¹_loc(Ω, ℝ).

```

### crosswalk/95 (crosswalk/95-standard-results.tsv)

**cw95.1** remove the row thm:std-hin26a-cform

Old text:
```
thm:std-hin26a-cform	paper/RESPONSE-HL-5D.md:2006-2010; docket68/n1star/N1STAR-PROOF.md:3577-3584	[Hin26a] Proposition 5.1 p. 38, READ 2026-10-21 (pp. 38-41); NP 10.14 setting	

```
New text:
```
(empty: delete the old text)
```

**cw95.2** replace the row thm:std-hjs-calculus by rows for thm:std-melrose-sc and thm:std-hin17-subprincipal

Old text:
```
thm:std-hjs-calculus	docket68/n1star/proof5/PART-I-SPECTRAL.md:196-206; docket68/n1star/proof5/PART-I-SPECTRAL.md:1932	[HJS] (2.1), Propositions 7.4-7.5 and the calculus, READ in Part I.A ((C1) onward)	

```
New text:
```
thm:std-melrose-sc	[Mel94] author's corrected online edition (1997), https://math.mit.edu/~rbm/papers/sslaes/sslaes1.pdf, pp. 4, 12-23	[Mel94] (1.1), Definitions 1-2, (5.1), Propositions 3-5, Lemmas 5-6, (5.12)-(5.34), (7.1), (7.2), (7.6), read 2026-11-20	replaces thm:std-hjs-calculus ([HJS] lecture notes, unpublished) (G-SWEEP G5); quoted from the source
thm:std-hin17-subprincipal	arXiv:1502.03183v2 pp. 16, 20, 26	[Hin17] Definition 3.8, Proposition 4.1, Theorem 4.8, read 2026-11-20	cited at 32 (prop:np-10-17-i), 34 and 38 (G-SWEEP minor item); quoted from the source

```

**cw95.3** add the row thm:std-abk-holomorphy after thm:std-analytic-fredholm

Old text:
```
thm:std-analytic-fredholm	docket68/n1star/proof5/PART-I-C-LOWENERGY.md:122-125; docket68/n1star/proof5/PART-I-C-LOWENERGY.md:1508-1509	I.C (K5): [RS1] Theorem VI.14 (analytic Fredholm theorem)	

```
New text:
```
thm:std-analytic-fredholm	docket68/n1star/proof5/PART-I-C-LOWENERGY.md:122-125; docket68/n1star/proof5/PART-I-C-LOWENERGY.md:1508-1509	I.C (K5): [RS1] Theorem VI.14 (analytic Fredholm theorem)	
thm:std-abk-holomorphy	arXiv:1904.03088v1 pp. 1-2	[ABK20] definitions p. 1-2 and Theorem 1.1 p. 2, read 2026-11-20	replaces [AN00, Theorem 3.1] at 35 (thm:iii-g1-3-1), whose text was not accessible (G-SWEEP minor item); quoted from the source; locally bounded implies locally L1-bounded drawn in the entry

```

### Chapter 98 (references) (chapters/98-references.md)

**98.1** add [ABK20] after [AB26]

Old text:
```
- [AB26] L. Alpöge, T. Buckmaster, *Blowup for the Boussinesq equations with smooth forcing*, preprint (2026),
  https://cims.nyu.edu/~tristanb/boussinesq.pdf.

```
New text:
```
- [AB26] L. Alpöge, T. Buckmaster, *Blowup for the Boussinesq equations with smooth forcing*, preprint (2026),
  https://cims.nyu.edu/~tristanb/boussinesq.pdf.
- [ABK20] W. Arendt, M. Bernhard, M. Kreuter, *Elliptic problems and holomorphic functions in Banach spaces*,
  Illinois J. Math. 64 (2020), 331–347. doi:10.1215/00192082-8591584 arXiv:1904.03088v1

```

**98.2** remove [AN00]

Old text:
```
- [AN00] W. Arendt, N. Nikolski, *Vector-valued holomorphic functions revisited*, Math. Z. 234 (2000), 777–805.
  doi:10.1007/s002090050008

```
New text:
```
(empty: delete the old text)
```

**98.3** [Hin17]: add the arXiv id

Old text:
```
- [Hin17] P. Hintz, *Resonance expansions for tensor-valued waves on asymptotically Kerr–de Sitter spaces*, J. Spectr.
  Theory 7 (2017), 519–557. doi:10.4171/JST/171

```
New text:
```
- [Hin17] P. Hintz, *Resonance expansions for tensor-valued waves on asymptotically Kerr–de Sitter spaces*, J. Spectr.
  Theory 7 (2017), 519–557. doi:10.4171/JST/171 arXiv:1502.03183v2

```

**98.4** remove [HJS] (only with the ch. 21–23 texts)

Old text:
```
- [HJS] A. Hassell, Q. Jia, E. Sussman, *Lecture notes on non-elliptic Fredholm theory*, lecture notes (2026).
  arXiv:2604.18956v1

```
New text:
```
(empty: delete the old text)
```

**98.5** add [Mel94] after [Mel93]

Old text:
```
- [Mel93] R. B. Melrose, *The Atiyah–Patodi–Singer index theorem*, Res. Notes Math. 4, A K Peters, Wellesley, MA (1993).
  doi:10.1201/9781439864609

```
New text:
```
- [Mel93] R. B. Melrose, *The Atiyah–Patodi–Singer index theorem*, Res. Notes Math. 4, A K Peters, Wellesley, MA (1993).
  doi:10.1201/9781439864609
- [Mel94] R. B. Melrose, *Spectral and scattering theory for the Laplacian on asymptotically Euclidian spaces*, in:
  Spectral and Scattering Theory (Sanda, 1992), Lecture Notes in Pure and Appl. Math. 161, Dekker, New York (1994),
  85–130. doi:10.1201/9781003072096-5; author's corrected online edition (1997),
  https://math.mit.edu/~rbm/papers/sslaes/sslaes1.pdf.

```

### Chapter 21 (chapters/21-s02-spectral-high.md)

**21.1** 

Old text:
```
[[ch:s01]], except the facts of Fourier analysis used in [[sec:i-b-2]] and the results of [HJS] used in [[ch:s01]]. In
```
New text:
```
[[ch:s01]], except the facts of Fourier analysis used in [[sec:i-b-2]] and the results of [Mel94] used in [[ch:s01]]. In
```

**21.2** 

Old text:
```
defines it and refers to [VZ00] and [Hin25a, Section 6.6]; [HJS] treats only the non-semiclassical calculus. We prove
```
New text:
```
defines it and refers to [VZ00] and [Hin25a, Section 6.6]; [Mel94] treats only the non-semiclassical calculus. We prove
```

### Chapter 22 (chapters/22-s03-spectral-low.md)

**22.1** 

Old text:
```
calculus of [HJS] as used in [[ch:s01]], and the facts about Hankel functions from [DLMF] stated in [[sec:i-c-5-2]].
```
New text:
```
calculus of [Mel94] as used in [[ch:s01]], and the facts about Hankel functions from [DLMF] stated in [[sec:i-c-5-2]].
```

**22.2** 

Old text:
```
(K3) *Rellich.* [HJS, Proposition 3.13]: for distributions supported in a fixed compact set and s′ > s, the inclusion
```
New text:
```
(K3) *Rellich.* (C4) of [[sec:i-a-2-1]]: for distributions supported in a fixed compact set and s′ > s, the inclusion
```

**22.3** 

Old text:
```
as in [Hin26c]. By [HJS, Propositions 3.7, 3.11 and 3.13,
Sections 10.1–10.3] and [[lem:i-c-2-2]]: the L²(|dx̂|)
```
New text:
```
as in [Hin26c]. By (C3), (C4) and (C6) of [[sec:i-a-2-1]]
and [[lem:i-c-2-2]]: the L²(|dx̂|)
```

**22.4** 

Old text:
```
the results of [HJS] used in [[ch:s01]], and uses [Hin26c, (9.117)], whose printed proof omits a term
```
New text:
```
the calculus of [[sec:i-a-2-1]], and uses [Hin26c, (9.117)], whose printed proof omits a term
```

**22.5** 

Old text:
```
[HJS, Lemma 12.5], there being no artificial boundary); near ztf
```
New text:
```
(C8) of [[ch:s01]], there being no artificial boundary); near ztf
```

**22.6** 

Old text:
```
The microlocal elliptic estimate ([HJS, Propositions 4.9 and 4.10]) for
```
New text:
```
The microlocal elliptic estimate ((C5) of [[sec:i-a-2-1]]) for
```

**22.7** 

Old text:
```
isomorphically onto H_sc^(s,𝗋) ([HJS, Definition 10.2]), and the same holds with k
```
New text:
```
isomorphically onto H_sc^(s,𝗋) ((C6) of [[sec:i-a-2-1]]), and the same holds with k
```

**22.8** 

Old text:
```
microlocally there ([HJS,
Propositions 2.3, 4.9 and 4.10]); near the zero section,
```
New text:
```
microlocally there ((C5) of
[[sec:i-a-2-1]]); near the zero section,
```

### Chapter 23 (chapters/23-s04-compactified.md)

**23.1** 

Old text:
```
says so), and [HJS] has constant differential orders. In this edition
```
New text:
```
says so), and [Mel94] has constant orders. In this edition
```

### Chapter 33 (optional; for the removal of thm:std-hin26a-cform) (chapters/33-s14-constraint-damping.md)

**33.1** 

Old text:
```
Moreover: (a) conditions (4)–(5) of [Hin26a, Proposition 5.1] off 𝗌𝖿, for 0 < ρ_sf ≤ 2δ_r with some δ_r > 0, follow
from (iv) by continuity, since Tangherlini space differs from its Minkowski model by terms in ρ_sf C^∞ ([Hin26a, p. 39]);
```
New text:
```
Moreover: (a) conditions (4)–(5) of [Hin26a, Proposition 5.1], which [[lem:iv4-1-4]] restates, off 𝗌𝖿, for
0 < ρ_sf ≤ 2δ_r with some δ_r > 0, follow from (iv) by continuity, since Tangherlini space differs from its Minkowski
model by terms in ρ_sf C^∞ ([Hin26a, p. 39]);
```

## 6. Check outputs

Live tree, after my edits:

```
$ python3 lint.py --chapters
chapters: 62 file(s), 4586 label(s) defined, 0 hit(s)
$ python3 assemble.py --check
labels 4586, computations cited 0, problems 0
```

A copy of the tree with all 24 texts of §5 applied:

```
$ python3 lint.py --chapters
chapters: 62 file(s), 4587 label(s) defined, 0 hit(s)
$ python3 assemble.py --check
labels 4587, computations cited 0, problems 0
$ grep -n "HJS\|AN00\|std-hjs\|hin26a-cform" chapters/*.md
(no output)
```

After label resolution, the longest line is 121 characters in each of ch. 03, 20, 21, 22, 23, 32, 33, 35, 95 and 98
(simulated tree).
