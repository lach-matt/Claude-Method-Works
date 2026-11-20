# S-G1: scoping the fix for gap G1 (the semiclassical 3b-calculus in ch. 33)

Read-only scoping report. Paper: `research/warp-drive/paper/reader/`, chapters as on disk on 2026-11-20. Line numbers
are `chapters/33-s14-constraint-damping.md` unless another file is named. Nothing in the paper was edited.

**Verdict in one paragraph.** Route (b), in a light form.
- [Hin26d] is published (Commun. Amer. Math. Soc. 6 (2026), 153–243). Its §3.7 treats *parameterised*
  scaled-bounded-geometry structures, of which the semiclassical 3b- and eb-calculi are instances (scalings h). That
  section states uniform L²/Sobolev boundedness and says the adjoint, composition, commutator and principal-symbol
  properties of its Theorem 3.51 "carry over verbatim". So everything ch. 33 uses can be quoted from a published
  source, except three things: an explicitly parameterised microlocal elliptic estimate, the Gårding step, and two
  routine Sobolev-space facts (duality of the supported/extendible spaces, and regularisation).
- No published source states a Gårding inequality for Ψ_(3b,ħ). But the step at 33:1458 does **not** need the *sharp*
  Gårding inequality. It needs only the Gårding inequality *with a positive margin*. Hintz's own (5.45) bounds the
  pairing by 2C𝔛⁻² when the symbol is bounded by C𝔛⁻². That inequality follows in about ten lines from composition,
  adjoints and L²-boundedness by a square root, exactly as ch. 23 does for e3b with lem:ii-a1-2-6.
- Separately, [Hin23d] was published on 2026-11-11 (Ars Inven. Anal. 2026, Paper No. 5), but it contains no
  semiclassical 3b-calculus. Its citation in prop:np-10-65-a does not support the claim it is attached to.

Estimated size: about 4–5½ pages of new or rewritten text in ch. 33, plus about ½ page of Appendix A quotations;
3–4 days of writing and 1 day of checking.

---

## 1. Facts used

What ch. 33 takes from the calculus is listed by fact, with each site and the precise statement the proof needs.
"Ψ" means Ψ_(3b,ħ)(M^♭; 𝒯*) (weighted by ρ_sf, ρ_K, families in h ∈ (0, 1)) unless "eb" or "non-semiclassical" is
said.

| # | Fact | Where used | Precise statement needed |
|---|---|---|---|
| F1 | **Existence and contents** of the weighted semiclassical 3b-calculus on 𝒯*, in dimension 4 + 1 | def:iv5-0-1 (1210–1219); prop:np-10-65-a (1221–1228); every commutant "a quantisation A = A* with WF′(A) = supp a" (1377, and the commutants at 1438, 1490, 1531, 1565, 1625, 1666, 1676) | (i) ρ_sf^(−l) Diff^m_(3b,ħ) with C^∞(M^♭)-coefficients ⊂ ρ_sf^(−l) Ψ^m (P_h, 𝓛_h, J, Q, the cut-offs χ_(τ,j), χ_(r,j), the weights). (ii) h-independent Diff^m_3b ⊂ Ψ^m_3b (non-semiclassical), and h^m Diff^m_3b ⊂ Ψ^m (Q_0, Q_1). (iii) For a ∈ ρ_∞^(−m) C^∞ of the compactified semiclassical phase space (scalar or End ℂ⁵): Op(a) ∈ Ψ^m with principal symbol a; Op(f) = f; (Op(a) + Op(a)*)/2 is self-adjoint with the same symbol and WF′ ⊂ supp a. |
| F2 | **Algebra**: composition, adjoints for (\|dg\|, B), principal symbols, commutators; the exact sequence 0 → hΨ^(m−1) → Ψ^m → S^m/hS^(m−1) → 0 | 1352 (w⁻¹[P_h, w] for weights); (5.25)–(5.29) at 1377–1393; (5.37)–(5.39) at 1437–1441; "the double commutator lies in hΨ" (1458); 1497–1499, 1531–1533, 1565–1573, 1617–1637, 1664–1680; cone face 2168–2186 | A ∘ B ∈ Ψ^(m+m′) with σ(AB) = σ(A)σ(B); A* ∈ Ψ^m with σ(A*) = σ(A)^(*_B); σ(h⁻¹ i[A, B]) = H_a b for scalar a; σ(A) = 0 ⇒ A ∈ hΨ^(m−1); all with weights ρ_sf^β ρ_K^(β′). |
| F3 | **Boundedness**, uniformly in h, on H^(s,(β_sf,β_K))_(3b,h), with norms bounded by finitely many seminorms | every "≤ C‖·‖" in §§iv5-1–iv5-7; 1935 | A ∈ ρ^w Ψ^m maps H^(s,β) → H^(s−m,β−w) with norm ≤ a seminorm of A, uniformly in h; the same for the eb spaces. |
| F4 | **Microlocal sets**: WF′, Ell; microsupports; disjoint microsupports compose to h^∞Ψ^(−∞); microlocalisers | statements of prop:iv5-1-2 – prop:iv5-5-3, thm:iv6-2-1 (WF′(B_0) ⊂ Ell(B_1), sets such as {\|r − r_c\| ≤ (55/50)ε_c, ρ_K ≤ 2δ, \|ζ\| < 1}) | WF′ and Ell are closed and open subsets of the compactified semiclassical phase space [0, 1]_h × ³ᵇT̄*M₀, on the locus {h = 0} ∪ fibre infinity. WF′(AB) ⊂ WF′(A) ∩ WF′(B). If A, B are microsupported in disjoint closed sets, then AB ∈ h^∞Ψ^(−∞). For K ⊂ U there is G with WF′(G) ⊂ U and WF′(I − G) ∩ K = ∅. |
| F5 | **Microlocal elliptic estimate** (equivalently, a microlocal parametrix), semiclassical, weighted, uniform in h, strong sense | prop:iv5-1-2 proof (1351–1353: "A microlocal parametrix in the calculus … gives the estimate"); (5.47) at 1459–1461 ("WF′(F) ⊂ Ell(𝓛_h)"); absorption at 1395; "f is elliptic" (1452, 1555, 2181); Λ⁻ in prop:iv5-1-3 | WF′(B) ⊂ Ell(A) ∩ Ell(G) ⇒ ‖Bu‖_(H^(s,β)) ≤ C(‖GAu‖_(H^(s−m,β+w)) + h^N‖χu‖_(H^(−N,β))) for h < h_0. |
| F6 | **Exact sums of squares**: smooth square roots of positive definite B-self-adjoint symbol fields, quantised as B*B | notation (1321–1327); (5.26) at 1384; the b_0, b_R, e, b_sf, b_K, e₁, e₂ square roots (1443–1452, 1490–1499, 1533–1541, 1565–1580, 1621–1637, 2173–2182) | If q ≥ c > 0 is a B-self-adjoint symbol on a set W with uniform symbol bounds, then q^(1/2) has the same bounds. Then F2 gives Op(q^(1/2))*Op(q^(1/2)) = Op(q) + hΨ^(m−1). No Gårding is involved. |
| F7 | **Non-semiclassical lower bound for Q_0** ([Hin26a, (5.44)]: "Q_0 = Θ*Θ + R, R ∈ Ψ^(−∞)_3b") | 1456–1457; reused at 1465, 1503–1504, 1541–1542, 1580, 1639, 1671–1672, 1684; cone face 2168–2186 | ⟨Q_0 v, v⟩ ≥ −C‖v‖² for v supported in the compact K. In weighted form, ⟨Q_0 v, v⟩ ≥ −C‖ρ_sf v‖², with r⁻¹ for ρ_sf at 𝖼𝖿. Only this lower bound is used. |
| F8 | **The Gårding step** ([Hin26a, (5.45)]) | 1457–1458 ("…O(𝔛⁻²) on supp a, which gives [Hin26a, (5.45)] by Gårding"); the same sites as F7; listed at 1211 ("the sharp Gårding inequality") and 1935 | What is needed: if T ∈ Ψ⁰ is self-adjoint with principal symbol t and \|t\| ≤ M, then \|⟨Tv, v⟩\| ≤ (M + η)‖v‖² + C_η h‖v‖². This is **Gårding with a margin**, not sharp Gårding (t ≥ 0 with loss h). It is applied with T = Ã*h²Q_1Ã and M ≈ C𝔛⁻². |
| F9 | **Sobolev spaces on Ω**: supported and extendible spaces, uniform duality | 1215–1219 ("([Hin26a, Section 2.3])"); 1883–1884 (duality in thm:iv5-7-3 (a), "([Hin26a, Section 2.3])"); quotient norms in the extension/restriction at 1798–1822 | H^(s,β)_(3b,h)(Ω)^(•,−) and H^(−s,−β)_(3b,h)(Ω)^(−,•) are dual under ⟨·, ·⟩, with constants uniform in h. This requires property (D) at X_0 and at Σ^♯. |
| F10 | **Regularisation** for the "strong sense" | 1367, 1370–1371 ("the standard regularisation ([Hin26a, p. 45])"); 1815 | A family J_ε, bounded in Ψ⁰ uniformly in (ε, h), of order −∞ for each ε, with J_ε → I strongly and [P_h, J_ε] bounded in hΨ^(m−1) uniformly. |
| F11 | **The semiclassical eb-calculus** on M = [ℝ̄^(1+4); {r = 0}] with eb-regular coefficients: F1–F10 for it | 2132–2136 ("give the parameterised scaled bounded geometry ([[prop:np-10-65-a]])"); thm:iv6-2-1 proof (2148–2229) | The same statements on the eb spaces, with the cells of 2133–2135 and scaling h. |
| F12 | **Uniformity in b**: the calculus constants depend on finitely many seminorms | lem:iv5-8-1, 1934–1938 | Operator norms are bounded by seminorms (continuity of Op, of composition and of adjoints); every auxiliary symbol depends continuously on b. |

**Not part of G1:** the sc-b and sc calculus with variable orders, the radial and real principal type estimates, the
relative index theorem (prop:iv6-1-1; G4/G5), and the energy estimates via [Hin26a, Lemma 5.14, Corollary 5.15] (G2).
The regularisation sentence at 2077 concerns the sc-b calculus (G5).

---

## 2. Published sources, verified

Tools used: alphaXiv (full text of 2408.06651v1, the author's revised version of the same paper, 2302.13803v2,
2606.27658v2, the book PDF [Hin25a], the online [DZ19]); Firecrawl (search, the journal page of Ars Inveniendi
Analytica, Hintz's CV dated 2026-09-11); Consensus and SciSpace (venue confirmation; no further source found). The
research-desk reference lookup failed: the proxy refused OpenAlex and arXiv with a 403.

### 2.1 [Hin26d] — P. Hintz, *Pseudodifferential operators on manifolds with scaled bounded geometry*

- **Published:** Commun. Amer. Math. Soc. 6 (2026), 153–243, doi:10.1090/cams/58. Confirmed by Hintz's CV (entry [40]),
  the ResearchGate record ("6(3):153-243"), the Consensus record ("2026, Communications of the American Mathematical
  Society") and the bibliography of [Hin23d] v2. Ch. 98 already lists it as published.
- **Dimension:** any smooth n-manifold (Def. 1.3).
- **Semiclassical: yes, through parameterised structures.** Quotations, from arXiv v1, whose pages Appendix A uses
  (95:5–7):
  - Def. 1.9, p. 9: "…it includes semiclassical bounded geometry settings when P = (0, 1]_h if all 𝓑_(h,×) feature
    the same b.g. structure {(U_α, φ_α)}, and the scalings are ρ_(α_h,i) = h for h ∈ (0, 1]."
  - §3.7, pp. 58–60:
    - Def. 3.58 (symbols with uniformly bounded seminorms).
    - Def. 3.59 (V-ps.d.o.s in the parameterised setting; principal symbol in wS^m/wρS^(m−1)).
    - "An operator A = (A_p)_(p∈P) ∈ wΨ^m_𝒱(M) defines a uniformly bounded family of operators A_p :
      w′_p H^s_(𝒱_p)(M) → w_p w′_p H^(s−m)_(𝒱_p)(M) … (This is in fact a special case of Theorem 3.44, applied to the
      scaled b.g. structure (P × M, 𝓑^×) …)" (p. 59), with footnote 13 (countable P′ ⊂ P).
    - "The properties of adjoints, compositions, commutators, and principal symbols in Theorem 3.51 carry over
      verbatim." (p. 59)
    - Remark 3.56 (subsets of P, p. 58).
    - Remark 3.60 (pp. 59–60): an elliptic P "has a parametrix Q … with QP = I + R, R ∈ hΨ^(−1)_𝒱(ℝⁿ)", and
      "Similarly, the notion of wave front set (Definition 3.54) generalizes to the parameterized setting".
  - §3.8: Def. 3.61 (admissible compactifications, p. 60); the definition of Ell/WF′ as images under (3.44) (p. 61);
    and p. 62: "In the parameterized setting … Definition 3.61 carries over to this setting mutatis mutandis. For
    example, for the semiclassical b.g. algebra … ℏT̄*M := [0, 1]_h × T̄*M … the microlocalization locus is the union
    of [0, 1] × S*M and {0} × T̄*M."
- **Non-parameterised statements:**
  - Thm 3.44 (p. 51, boundedness) and Remark 3.47 (seminorms; continuity).
  - Thm 3.51 (p. 55: adjoints, compositions, commutators; WF′(A₁A₂) ⊂ WF′(A₁) ∩ WF′(A₂)).
  - Thm 3.52 (p. 56): parametrix in the proof, and footnote 12 ("one can refine Q to yield a residual remainder").
  - Prop. 3.55 (p. 57), including (3), microlocal elliptic regularity.
  - Lemma 3.30 (p. 42, asymptotic summation); Lemma 3.29 and Def. 3.25 (elliptic sets).
- **Examples:** (10), p. 14, is the 3b-algebra, in spacetime dimension n, with b-regular coefficients, near the corner
  only, non-semiclassical. (9), p. 14, is the edge-b algebra. (3) and (11) are the semiclassical scattering and
  semiclassical cone algebras. No semiclassical 3b-algebra is listed by name; it is the recipe of Def. 1.9 applied to
  3b cells.
- **Not stated:**
  - Any Gårding inequality.
  - Propagation ("We shall not attempt to study the propagation of singularities", p. 57).
  - Prop. 3.55 (3) for *parameterised* structures: §3.7 says only that boundedness and Thm 3.51 carry over and that the
    wave front set "generalizes".
  - Operators on bundles are "left to the interested reader" (Remark 3.46). This is harmless here, since 𝒯* is
    globally trivialised by dt, dx¹, …, dx⁴.
- **Covers:** F2, F3, F12 fully (via §3.7); F1, F4, F11 once the 4+1 cell structure is written down (an in-paper check);
  F5 through Prop. 3.55 (3) plus the P′ × M device that §3.7 itself uses (p. 59). It does not cover F7, F8, F9 or F10.
- **Numbering caveat.** The author's revised version, dated 15 Dec 2025 (presumably the accepted text), keeps all of
  this verbatim but renumbers it: Def. 1.10, Defs 3.59–3.60, Thm 3.45 / 3.52 / 3.53, Prop. 3.56, Remarks 3.57 / 3.61,
  and "carry over verbatim" moves to p. 60. Appendix A's stated policy (arXiv-v1 pages) is consistent with v1
  numbering, but a note mapping v1 to published numbers would help. The typeset CAMS pages were not checked.

### 2.2 [Hin23d] — *Microlocal analysis of operators with asymptotic translation- and dilation-invariances*

- **Now published:** Ars Inven. Anal. (2026), Paper No. 5, 159 pp., doi:10.15781/yw47vq75, published 2026-11-11 (the
  journal's article page). The article is arXiv v2 (posted 18 Nov 2026). Ch. 98:76 still lists it as "preprint (2023)
  arXiv:2302.13803v1".
- **Content (v2):** the non-semiclassical small and large 3b-calculus on the compactification of ℝ_t × ℝ^(n−1)_x for
  general n, built with double and triple spaces.
  - Def. 4.3: Ψ^m_3b(M; E, F).
  - Def. 4.22: weighted 3b-Sobolev spaces and boundedness.
  - Remark 4.23 (p. 103): the bounded-geometry/[Shu92] view of the Sobolev spaces.
  - Prop. 5.10 (p. 119): composition in the *large* calculus.
  - Page 109 holds a proposition on normal-operator families; its item (2) is a semiclassical *scattering* family.
  - The only semiclassical algebras are models of spectral families (semiclassical scattering §2.3.1, semiclassical
    cone).
- **No semiclassical 3b-calculus and no Gårding.** prop:np-10-65-a's "[Hin23d, pp. 3, 7, 10–12, and Proposition 5.10,
  p. 109]" does not support "the semiclassical 3b-calculus … is constructed …". **Covers none of F1–F12 in
  semiclassical form.**

### 2.3 [Hin26a] — *Constraint damping on subextremal Kerr spacetimes*

- **Status:** preprint (arXiv 2606.27658v2, 15 Sep 2026; "Preprint" in Hintz's CV). Not usable as a source; it is the
  blueprint.
- §2.3.2 (pp. 23–25) *defines* the semiclassical 3b-calculus as the parameterised structure with the cells
  (2.20)–(2.21) and scalings h, "following the general recipe in [Hin26d]". It refers to [Hin26d, §3] for proofs, to
  [Hin25a, Theorems 4.29 and 4.53] for parametrices ("in the usual fashion"), to [Hin25a, Prop. 6.61] for Prop. 5.5,
  to [Vas18, §4.4] or [Hin25a, §8.5] for regularisation, and to [Hin25a, Chapter 9] for the supported/extendible
  spaces ("straightforwardly adapted").
- (5.45), p. 50, verbatim: "|q₁₀| ≤ C𝔛⁻² on supp a … and hence Gårding's inequality gives
  Re(h⁻¹⟨Ah³Q₁Aω, ω⟩) ≤ (2C𝔛⁻² + C_𝔛 h)‖Aω‖²". The factor 2 is a positive margin. **Sharp Gårding is not what is used.**

### 2.4 [Hin25a] — P. Hintz, *An introduction to microlocal analysis*, GTM 304, Springer (2025)

- **Published.**
- Semiclassical calculus on ℝⁿ: Thm 4.50 (adjoints, compositions, commutators), Thm 4.51 (boundedness), Thm 4.53
  (semiclassical elliptic parametrix; "proof … left to the reader").
- Prop. 6.61: semiclassical microlocal elliptic estimate on manifolds, compact supports.
- §8.5: regularisation.
- Gårding appears **only as Exercise 4.5**, non-semiclassical and with an ε-loss; sharp Gårding is referred to
  Hörmander, Thm 18.1.14.
- **Not 3b; no Gårding theorem.**

### 2.5 [DZ19] — S. Dyatlov, M. Zworski, GSM 200 (published; in ch. 98)

- Appendix E, Prop. E.23: sharp Gårding. "Let A ∈ Ψ^(2k+1)_h(M) be compactly supported … Re σ_h(A) ≥ 0 … Re⟨Au, u⟩ ≥
  −Ch‖u‖²_(H^k_h)". Its proof reduces to [Zw12, Theorem 9.11].
- Prop. E.24: ‖A‖ ≤ sup\|σ_h(A)\| + Ch^(1/2).
- Thm E.33: elliptic estimate. Prop. E.34: microlocal Gårding.
- All of these are for **compactly supported** operators. The operators at 33:1458 live in K = {\|r − r_c\| ≤ (3/2)ε_c,
  ρ_K ≤ 4δ}, which reaches K⁺ (t → ∞), so they are not compactly supported in M^♭°. **Not directly applicable.**

### 2.6 Others

- Vasy's and Vasy–Zworski's published semiclassical calculi ([VZ00], [Vas13], [Vas18]) and Hintz's Minkowski papers
  ([Hin23a], [HV20]) concern b-, sc-, de,sc- and semiclassical sc-calculi, not the 3b- or eb-calculus. They were not
  re-read here, since the fix does not need them. [Vas18, Theorem 5.3] is what [Hin26c] cites for variable-order
  propagation with sharp Gårding (23:2173).
- Firecrawl "semiclassical 3b" returns only [Hin26a]. Consensus and SciSpace found no other source.

---

## 3. Recommended route and detailed plan

### 3.1 Decision

- **(a) is not available.** No published source states a Gårding inequality for Ψ_(3b,ħ) or Ψ_(eb,ħ), or (explicitly)
  the parameterised microlocal elliptic estimate.
- **(c) is not needed.** [Hin26d] is published and covers the calculus once the cells are written down.
- **(b) is recommended.** The replacement is small because F8 never needed sharp Gårding.

Plan:
1. Quote [Hin26d] §§3.7–3.8 in Appendix A.
2. Replace prop:np-10-65-a by a construction of the 4+1 semiclassical 3b- and eb-structures and a proposition listing
   F1–F6 and F9–F11, with a real proof.
3. Add two short lemmas: Gårding with a margin (F8) and the Q_0 lower bound (F7).
4. Re-point the proof steps.

The rest of prop:iv5-2-1, the propositions that end "the rest is the proof of [[prop:iv5-2-1]]", thm:iv6-2-1 and the
uniformity at 1935 go through unchanged in structure ("fix 𝔛 large, then h small"). §3.6 below checks this.

### 3.2 Appendix A (95:836–980): quotations to add

1. **(S7) (95:878).** Replace the bare pointer by quotations:
   - Def. 1.9 (p. 9; the sentence quoted in §2.1 above);
   - Defs 3.58–3.59 (p. 59);
   - the uniform-boundedness paragraph with "(This is in fact a special case of Theorem 3.44, applied to the scaled
     b.g. structure (P × M, 𝓑^×) …)" and footnote 13 (p. 59);
   - "The properties of adjoints, compositions, commutators, and principal symbols in Theorem 3.51 carry over
     verbatim." (p. 59);
   - Remark 3.56 (p. 58);
   - from Remark 3.60, the wave-front-set sentence ("Similarly, the notion of wave front set (Definition 3.54)
     generalizes to the parameterized setting, with WF^(m,w,l)_𝒱(u) ⊂ 𝔐 defined for u = (u_p)_(p∈P) ∈
     wρ^(−∞)H^(−∞)_𝒱(M), by which we mean that u_p ∈ w_p ρ_p^(−N) H^(−N)_(𝒱_p)(M) for some fixed N, with norm bounded
     uniformly in p.", p. 60).

   Also tighten ch. 23's paraphrase of (S7) (sec:ii-a-3, "the above holds uniformly in p"): the source says this only
   of boundedness and Thm 3.51.
2. **New (S16), admissible compactifications** ([Hin26d, Definition 3.61, p. 60; pp. 61–62]): conditions (1)–(3); the
   sentence that Ell, ess supp and WF′ "as the images in 𝔐_(T̄*M) of the corresponding subsets of 𝔐 under the map
   (3.44); or via testing with elements of C^∞(T̄*M)"; and the p. 62 paragraph on parameterised compactifications with
   the semiclassical example. This is optional if F4 is proved in the paper, as ch. 23 does for e3b (§3.3 C).
3. **Optional (S17), Lemma 3.30** (asymptotic summation, p. 42). Needed only if the edition keeps the exact form
   "Q_0 = Θ*Θ + R, R ∈ Ψ^(−∞)_3b". The plan below avoids it.
4. **Numbering note** for the published version (§2.1).

### 3.3 New text replacing prop:np-10-65-a (a subsection "The semiclassical 3b- and eb-calculi", inside §iv5-0)

**A. Definition (the semiclassical 3b-structure in 4 + 1).**
- Work on M₀° = ℝ_t × ℝ⁴_x, with 3b-vector fields ⟨x⟩∂_(z^μ). This is the device of [Hin26a, p. 19]: M₀ has no inner
  boundary, and operators act with Schwartz kernels in Ω′ × Ω′, as the edition already requires at 1321.
- Cells, transcribing [Hin26a, (2.20)–(2.21)] with ℝ⁴ for ℝ³:
  - U_((1),j) = (j − 2, j + 2)_t × (−2, 2)⁴_x, with φ = (t − j, x), j ∈ ℤ;
  - U_((2),±i,j,k,m) = (2^k(j − 2), 2^k(j + 2))_t × ±(2^(k−2), 2^(k+2))_(x^i) × Π_(a≠i)(m_a − 2, m_a + 2)_(ω_a),
    with ω_a = x^a/x^i, φ = (2^(−k)t − j, log₂(±x^i) − k, ω − m), i = 1, …, 4, k ∈ ℕ₀, j ∈ ℤ, m ∈ {−2, …, 2}³.
- Parameter set (0, 1]_h; all scalings ρ_(h,α,μ) = h.

Checks, with the [Hin26a, pp. 20–21] computations carried out for four spatial coordinates:
- The pushforwards are |x^i|∂_t ↦ 2^X ∂_T, |x^i|∂_(x^i) ↦ ±(log 2)⁻¹∂_X ∓ Σ_a ω_a∂_(ω_a), and |x^i|∂_(x^a) ↦ ±∂_(ω_a).
  They are uniformly bounded and span. So 𝒲 consists of the 3b-regular 3b-vector fields, 𝒱_h = h𝒲, and
  C^∞(M₀) ⊂ C^∞_uni.
- (S1) holds, and condition (1.6) is automatic for constant scalings h.
- ρ_sf^β ρ_K^(β′) are weights on ((0, 1] × M₀, 𝓑^×): they are h-independent, and their ratios across adjacent cells
  are bounded.
- ‖·‖_(H^s_(𝒱_h)) is equivalent to ‖·‖_(H^s_(3b,h)) up to the constant factor h^(−5/2), from the density in (3.15).
  The factor is harmless because it appears on both sides of every estimate.
- 𝒯* has the global frame dt, dx^μ, so operators on it are 5 × 5 matrices (as ch. 23 sec:ii-a-4-3 does). The
  (\|dg\|, B)-adjoint is the ν_3b-adjoint conjugated by the weight ⟨x⟩⁵ and by the smooth invertible matrix field B̂.
  Both are in Ψ⁰ or are weights, so closure under adjoints and σ(A^(*_B)) = σ(A)^(*_B) follow from (S5) and (S7).
- **eb version:** the cells already printed at 2133–2135, with scaling h.

**B. Proposition (replacing prop:np-10-65-a): F1–F6, F9–F11 as listed in §1, for Ψ_(3b,ħ) and Ψ_(eb,ħ).** Proof plan,
item by item:
- *F1–F3, F12:* (S3)–(S5) and (S7) (as expanded), (S12) for chart changes, Remark 3.47 for seminorms; the bundle and
  adjoint as in A.
- *F4:* follow ch. 23 sec:ii-a1-1-2. Two lemmas:
  1. Smooth functions on [0, 1]_h × ³ᵇT̄*M₀, times ρ_∞^(−m), are symbols for 𝒱_h. In a cell, the 𝒱_h-fibre coordinate
     is the semiclassical 3b-covector, so this is the argument of lem:ii-a1-1-1 verbatim.
  2. Symbols with disjoint closed supports in this compact space are uniformly separated in the charts of the secondary
     structure, so their product is residual (h^∞Ψ^(−∞)) by (3.38). This is lem:ii-a1-1-2's argument.

  Alternatively, cite (S16) and check conditions (1)–(3) of Def. 3.61: ρ = h, λ = ⟨ζ⟩⁻¹, and (1) is lemma 1 above.
- *F5, by the P′ × M device of [Hin26d, p. 59 and footnote 13].*
  - For countable P′ ⊂ (0, 1], the cells {(h, U_α)} with scalings h form a scaled b.g. structure on the manifold
    P′ × M₀°.
  - A family in Ψ^m_(3b,ħ), restricted to P′, is an element of Ψ^m on P′ × M₀°: Def. 3.58 gives the symbols, and the
    residual part is residual because H^s(P′ × M₀°) = ℓ²-⊕_h H^s_(𝒱_h). Ell and WF′ correspond.
  - Prop. 3.55 (3) on P′ × M₀°, applied to u = (u_h) with one non-zero entry, gives the estimate with a constant
    independent of h ∈ P′. The error term ‖u‖_(wρ^(−N)H^(−N)) equals h^N‖u‖_(wH^(−N)), because ρ = h.
  - The constant is uniform on (0, 1]: otherwise a sequence h_j with constants tending to infinity would contradict the
    case P′ = {h_j}.
  - Cut-offs χ are inserted because B and G have compactly supported kernels.
  - (Alternative: the direct parametrix iteration of ch. 23 thm:ii-a1-3-1 in its smooth case, about the same length.)
- *F6:* ch. 23 lem:ii-a1-2-5 (i) with ν = 0, in the cell coordinates: the Cauchy integral (2πi)⁻¹∮ z^(1/2)(z − q)⁻¹dz.
  It is a pointwise statement and applies verbatim.
- *F9:* ch. 23 lem:ii-a-7-1 (uniform duality) and lem:ii-a-7-3 are stated for an **arbitrary parameterised** scaled
  b.g. structure (23:764), so they apply as they stand.
  - Add a lemma "property (D) for {t > 0}, {r > r_♯} and their intersection Ω°". Its proof is that of lem:ii-a-7-d:
    convolve with ϱ_ε supported in a cone, in the cells.
  - The boundaries are non-compact (X_0 along r, Σ^♯ along t), but they are uniformly transversal in the 3b cells, and
    the corner X_0 ∩ Σ^♯ ≅ 𝕊³ is compact. So the cell-by-cell argument with the uniform partition of (S4) works.
  - Then H(Ω)^(•,−) = Ḣ({t ≥ 0}) / Ḣ({t ≥ 0, r ≤ r_♯}). Its dual is the annihilator in H̄^(−s)({t > 0}), namely
    H^(−s)(Ω)^(−,•), with uniform constants.
- *F10:* J_ε := Op_h(⟨εζ⟩^(−K)), a two-parameter family. (S7) with P = (0, 1]_ε × (0, 1]_h shows that it is bounded in
  Ψ⁰, of order −K for each ε, and that [P_h, J_ε] is bounded in hΨ^(m−1). The rest is the standard argument
  ([Hin25a, §8.5]; it can also be modelled on ch. 23 lem:ii-a1-2-3).
- *F11:* the same proofs with the eb cells. In the edition, the eb ellipticity at 𝖼𝖿 uses the C of lem:iv5-0-4 on the
  model (2168).

**C. Lemma (Gårding inequality with a margin; replaces F8).**

*Statement.* Let T ∈ Ψ⁰_(3b,ħ)(M₀; 𝒯*) (or eb), and let t be a B-self-adjoint representative of its principal symbol
with t ≤ M everywhere, for some M ≥ 0. Then for every η > 0 there are C and h_0 with

    Re⟨Tv, v⟩ ≤ (M + η)‖v‖² + Ch‖v‖²_(H^(−1/2)_(3b,h)),     v ∈ L², h < h_0.

C depends only on η, M and finitely many seminorms of t and of T − Op(t).

*Proof.*
- The symbol M + η − t is at least η, so c := (M + η − t)^(1/2) ∈ S⁰ is B-self-adjoint (F6).
- Op(c)*Op(c) + Re T − (M + η) has principal symbol 0, so it lies in hΨ^(−1) (F2). Its H^(−1/2) → H^(1/2) norm is at
  most Ch (F3).
- Pair with v. ∎

This is ch. 23's lem:ii-a1-2-6 ("The supremum bound") transposed to the semiclassical setting. The h-remainder replaces
ch. 23's lower-order remainder.

**D. Lemma (lower bound for Q_0; replaces F7).**

*Statement.* Let Q̃ ∈ Diff²_3b(M₀; 𝒯*) be h-independent and formally self-adjoint, with principal symbol q B-positive
definite on ³ᵇT*_U M₀ ∖ o, for a neighbourhood U of a compact K ⊂ M₀. Then ⟨Q̃w, w⟩ ≥ −C‖w‖² for supp w ⊂ K.
Weighted form: for Q ∈ ρ_sf² Diff²_3b with ρ_sf⁻¹Qρ_sf⁻¹ as above, ⟨Qv, v⟩ ≥ −C‖ρ_sf v‖²; the same with r⁻¹ in the eb
case.

*Proof*, in the non-semiclassical calculus, which is (S5) with scalings 1:
- Take φ = 1 near K with supp φ ⊂ U. Then q_* := φ²q + (1 − φ²)\|ζ\|² ≥ c\|ζ\|², so θ := (q_* + 1)^(1/2) ∈ S¹. Put
  Θ := Op(θ).
- Since Op(φ²q) = φ²Op(q) (left quantization, eq:ii-a1-1-1) and φ = 1 on supp w,
  ⟨Q̃w, w⟩ = ‖Θw‖² − ‖w‖² − ⟨Rw, w⟩ with R ∈ Ψ¹_3b.
- Then \|⟨Rw, w⟩\| ≤ C‖w‖²_(H^(1/2)) ≤ ε‖w‖²_(H¹) + C_ε‖w‖², and ‖w‖²_(H¹) ≤ C(‖Θw‖² + ‖w‖²) by elliptic regularity
  ((S5), Prop. 3.55 (3)).
- Take ε small. ∎

### 3.4 The replacement at 33:1455–1461, in detail

Current text: "For Q: … so Q_0 = Θ*Θ + R with R ∈ Ψ^(−∞)_3b, which is [Hin26a, (5.44)]; the symbol of h⁻¹h³Q_1 vanishes
quadratically at o, so it is O(𝔛⁻²) on supp a, which gives [Hin26a, (5.45)] by Gårding; …". Replacement:

- *(5.44).* −h⁻¹⟨AQAω, ω⟩ = −h⟨Q_0Aω, Aω⟩ − h²⟨Q_1Aω, Aω⟩. By Lemma D, applied with K the kernel support of A and
  lem:iv5-0-4 for the positivity of G + Cρ_sf⁻²ℓ² over a neighbourhood of Ω, −h⟨Q_0Aω, Aω⟩ ≤ Ch‖Aω‖². This is (5.44)
  in the form it is used.
- *(5.45).*
  - q₁₀, the semiclassical principal symbol of h²Q_1, is the homogeneous quadratic symbol σ₂(Q_1)(ζ). So
    \|q₁₀(z, ζ)\| ≤ C\|ζ\|², where C is the supremum of \|q₁₀\| over the unit sphere bundle over the compact support of
    the kernels. C is independent of 𝔛 and uniform for b ∈ U.
  - Choose ã := χ̃(𝔛\|ζ\|)φ(z), with χ̃ = 1 on supp χ_0, supp χ̃ ⊂ (−3, 3), and φ = 1 near π(supp a). Put Ã := Op(ã).
  - (I − Ã)A ∈ h^∞Ψ^(−∞) (disjoint microsupports, F4).
  - Apply Lemma C, with η = 𝔛⁻², to ±Re(Ã*h²Q_1Ã), whose principal symbol ±ã²q₁₀ satisfies \|ã²q₁₀\| ≤ 9C𝔛⁻². This
    gives

        Re h⁻¹⟨Ah³Q₁Aω, ω⟩ ≤ ((9C + 1)𝔛⁻² + C_𝔛 h)‖Aω‖² + C_N h^N‖χω‖²_(H^(−N)),

    which is [Hin26a, (5.45)] with 9C + 1 for 2C and an h^N term that joins the existing one.
- *(5.46)* is unchanged: F2 and F5.
- *(5.47)* "with WF′(F) ⊂ Ell(𝓛_h)" cites F5.
- "Collecting, fix 𝔛 large and then h small" is unchanged: the coefficient of ‖Aω‖² is
  ¼c_0 + (9C + 1)𝔛⁻² + (C + C_𝔛)h, which is less than c_0 for 𝔛 large and then h small, as in [Hin26a, p. 50].

### 3.5 Propagation to the other sites

- **prop:iv5-2-1 (2)** (1465: "Q enters with a lower bound by [Hin26a, (5.44)–(5.45)]"). The adjoint pairing has
  +h⁻¹⟨AQAω, ω⟩. Lemma D gives h⟨Q_0Aω, Aω⟩ ≥ −Ch‖Aω‖², and Lemma C applied to −T gives the lower bound for the Q_1
  term. Same structure.
- **prop:iv5-3-1** (1502–1504, corner ∂K⁺; the weight matters). The main term is −c_0ρ_sf²a², and the left side is
  estimated with ‖ρ_sfAω‖².
  - Apply Lemma D to Q̃_0 := ρ_sf⁻¹Q_0ρ_sf⁻¹ ∈ Diff²_3b, which is positive definite since conjugation by the weight
    ρ_sf preserves Diff_3b and the principal symbol.
  - Apply Lemma C to Ã*ρ_sf⁻¹h²Q_1ρ_sf⁻¹Ã, with v = ρ_sfAω.
  - Add one sentence there. The same applies to **prop:iv5-4-1** (1541–1542) and **prop:iv5-5-2 (b)–(c)** (1639: "the
    Q-terms [Hin26a, (5.44)–(5.46)]").
- **prop:iv5-5-1, prop:iv5-5-3** (1580, 1671–1672): unweighted. They inherit through "the rest is the proof of
  [[prop:iv5-2-1]]".
- **thm:iv6-2-1** (2168–2186, cone face): the same with r⁻¹ for ρ_sf, the eb versions of Lemmas C and D, and the
  positivity of G + Cr²ℓ² on the model (lem:iv5-0-4 as used at 2168).
- **lem:iv5-8-1** (1934–1938): replace "the sharp Gårding inequality" by "the Gårding inequality with a margin
  ([[Lemma C]]) and the lower bound of [[Lemma D]]".
  - The margin constant 9C + 1 is uniform for b ∈ U by continuity of q₁₀ in b.
  - C_𝔛 depends on seminorms of the square-root symbol c. By the Cauchy integral, these are bounded by seminorms of
    ã²q₁₀ and by 𝔛² (the inverse margin), so they too are uniform for b ∈ U.
  - Remark 3.47 ((S5), with (S7)) supplies the seminorm dependence of operator norms. The proof is otherwise unchanged.

### 3.6 Does the rest of the proof of prop:iv5-2-1, and of the chain, still work?

Yes. Every other positivity in §§iv5-1–iv5-5 is an **exact** sum of squares of smooth symbols. The edition already
arranges these square roots (notation at 1321–1327; (∓χχ′)^(1/2) ∈ C^∞ for the cut-offs), and they are quantised with
remainders in hΨ and microsupport in supp a. The remainders are absorbed by F5 and the h^(1/2) iteration, which uses
only F2, F4 and F5. In particular:
- [Hin26a, (5.26)] at 1384 is an exact square root, A(B̃_0*B̃_0 + c_0Λ*Λ)A + hE, of the symbol ±ρ_sf⁻²ℓ − c_0λ². That
  symbol is positive definite on supp a by lem:iv5-0-4.
- "absorb h⟨B̃_2Aω, Aω⟩ ≤ Ch‖B̃_0Aω‖² + …" (1395) is F5, because B̃_0 is elliptic on supp a.
- The order of choices ("fix 𝔛, then h") is unchanged.

### 3.7 The real proof of the rewritten prop:np-10-65-a, in outline

> *Proof.* By Lemma A the cells define a parameterised scaled b.g. structure on M₀° (and on M° for eb), whose
> operator Lie algebra is h·𝒜_3b𝒱_3b (resp. h·𝒜_eb𝒱_eb).
> - (F1)–(F3) and (F12) are (S4), (S5), (S7) and (S12): uniform boundedness and the calculus of [Hin26d, Theorem 3.51]
>   "carry over verbatim" to the parameterised structure (p. 59). On 𝒯* use the global frame (S14); the
>   (|dg|, B)-adjoint is a conjugate of the ν_3b-adjoint by a weight and a smooth invertible matrix field.
> - (F4) is the two lemmas of B (or (S16)).
> - (F5) is [Hin26d, Proposition 3.55 (3)] on P′ × M₀° (footnote 13), with uniformity in h by the subsequence argument.
> - (F6) is lem:ii-a1-2-5 (i).
> - (F9) is lem:ii-a-7-1 and lem:ii-a-7-3 with the property (D) lemma.
> - (F10) is (S7) with parameters (ε, h).
> - (F11) is the same with the eb cells. ∎

All of it is "in every dimension". The dimension enters only through the cells (four spatial coordinates, three
angular coordinates per cell).

---

## 4. Sites that change

| File:line | Item | Change |
|---|---|---|
| 33:1210–1212 | def:iv5-0-1, calculus sentence | Drop "the sharp Gårding inequality". Say that the calculus is that of the new subsection, with the margin Gårding (Lemma C) and Lemma D. |
| 33:1215–1219 | spaces "([Hin26a, Section 2.3])" | Cite the property (D) lemma and lem:ii-a-7-1 / lem:ii-a-7-3. |
| 33:1221–1228 | prop:np-10-65-a | Rewrite the statement (F1–F6, F9–F11) and give the real proof (§3.7). Drop [Hin23d] and the bare [Hin26a, §2.3] as support (keep [Hin26a] only as an attribution of the cells). Insert Lemma A (cells), Lemma C (margin Gårding) and Lemma D (Q_0) next to it, or in a new subsection #### "The semiclassical 3b- and eb-calculi". |
| 33:1351–1353 | prop:iv5-1-2 proof | "A microlocal parametrix in the calculus…" becomes a citation of F5. |
| 33:1370–1371 | prop:iv5-1-3 proof, "standard regularisation ([Hin26a, p. 45])" | Cite F10. |
| 33:1377 | "A = A* with WF′(A) = supp a" | Cite F1 (iii). Optionally "WF′(A) ⊂ supp a" (only ⊂ is used). |
| 33:1384, 1395 | (5.26); absorption | Cite F6 and F5 (no change of argument). |
| 33:1456–1458 | prop:iv5-2-1, "For Q" | Replace by §3.4: Lemma D for (5.44); Ã-localisation plus Lemma C for (5.45), with 9C + 1 for 2C and the extra h^N term. |
| 33:1459–1461 | (5.47) | Cite F5. |
| 33:1465 | prop:iv5-2-1 (2), "Q enters with a lower bound by [Hin26a, (5.44)–(5.45)]" | Cite Lemmas D and C (with −T). |
| 33:1502–1504 | prop:iv5-3-1, weights | Add one sentence: Lemmas C and D applied to the ρ_sf-conjugated Q_1 and Q_0. |
| 33:1541–1542 | prop:iv5-4-1, "the rest is the proof of" | Same weighted remark (or a pointer to 1502). |
| 33:1639 | prop:iv5-5-2, "the Q-terms [Hin26a, (5.44)–(5.46)]" | Cite Lemmas C and D (weighted in (b)–(c)). |
| 33:1815 | "hold … in the strong sense" | Cite F10 (no change of argument). |
| 33:1883–1884 | thm:iv5-7-3 (a), duality "([Hin26a, Section 2.3])" | Cite F9. |
| 33:1934–1938 | lem:iv5-8-1 | "sharp Gårding inequality" becomes "the Gårding inequality with a margin and Lemma D". Add the seminorm dependence via (S5)/(S7) Remark 3.47 and the uniformity of the margin. |
| 33:2133–2136 | sec:iv6-2, eb structure "([[prop:np-10-65-a]])" | Cite the eb part of the new proposition (F11). |
| 33:2168–2186 | thm:iv6-2-1 cone face | One sentence: Lemmas C and D in the eb calculus with r⁻¹ for ρ_sf. |
| 95:878 | (S7) | Expand with the §3.7 quotations (§3.2 item 1). |
| 95:836 header, new (S16) [and (S17)] | thm:std-sbg-calculus | Add §3.8 (Def. 3.61, pp. 60–62) [and Lemma 3.30, p. 42, only if Θ*Θ + R is kept]. Add the v1-to-published numbering note. |
| 23 sec:ii-a-3, (S7) | ch. 23's local (S7) paraphrase | Tighten "the above holds uniformly in p" to what p. 59 states (consistency only; ch. 23's uses, compositions in lem:ii-a-7-1, are covered). |
| 98:76 | [Hin23d] | Update to "Ars Inven. Anal. (2026), Paper No. 5, 159 pp. doi:10.15781/yw47vq75 arXiv:2302.13803v2" if it is still cited. After the rewrite it is cited only in ch. 27 (27:1256, 1529, "[Hin23d, Lemma 2.25]"), whose v1 numbering must then be checked against v2. |
| 98:87 | [Hin26a] | Unchanged (still a preprint; after the fix it is cited only as attribution and for display numbers). |

Not changed: §§iv5-4 – iv5-7 statements; the energy estimates (G2); prop:iv6-1-1 (G4/G5).

---

## 5. Estimate

| Piece | Length | Notes |
|---|---|---|
| Lemma A (4+1 cells, structure checks, weights, norms, bundle/adjoint) and the eb cells | 0.6–0.8 p | transcription of [Hin26a, (2.20)–(2.21)], 4 spatial coordinates |
| Rewritten prop:np-10-65-a: statement and proof (F1–F6, F11), including the P′ × M device for F5 and the two microsupport lemmas | 1.3–1.6 p | ch. 23 sec:ii-a1-1-2 is the template |
| Lemma C (Gårding with a margin) | 0.3 p | ch. 23 lem:ii-a1-2-6 is the template |
| Lemma D (Q_0 lower bound, weighted and eb forms) | 0.4 p | |
| F9: property (D) at X_0, Σ^♯ and the mixed-space duality | 0.5 p | ch. 23 lem:ii-a-7-d is the template; non-compact but uniform boundaries |
| F10: regularisation family | 0.3 p | |
| Edits in proofs (§4: 1351 … 2186) | 0.5 p net | mostly re-pointing; §3.4 is the only rewritten argument |
| Appendix A: (S7) expanded, (S16) added, numbering note | 0.5 p | verbatim quotations listed in §3.2 |
| **Total** | **≈ 4.5–5.5 p** | |

**Effort:** 3–4 days to draft. Add 1 day to check: `lint.py`, `assemble.py --check`, the labels, a re-read of
§§iv5-1–iv6-2 against the new references, and the ch. 98 entry. This is less than a "section-sized proof project" because
every non-trivial calculus property is quoted from [Hin26d], and the only new analysis is Lemma C, Lemma D and the
property (D) lemma.

**Risks and choices for the author:**
1. Whether to state the F4 notions abstractly via (S16), or concretely as ch. 23 does. Concretely is recommended, for
   consistency with ch. 23.
2. Whether to keep the exact form "Q_0 = Θ*Θ + R, R ∈ Ψ^(−∞)" (then quote Lemma 3.30 and do the full iteration) or
   Lemma D's lower bound. Lemma D is recommended; only the lower bound is used.
3. [Hin26d] numbering: v1 against the published version (§2.1).
4. [Hin23d] is newly published, so the bibliography is stale; and ch. 27 cites its v1 numbering.
