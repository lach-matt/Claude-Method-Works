# Report P-S7: the paraphrase (S7) of [Hin26d] and its citing sites

Proof file: research/warp-drive/paper/reader/proofs/P-S7.md, 955 lines, md5 16e6e03f795d2c73d79116cdce206e38
(untracked, not committed). Nothing else in the repository was written. The old texts are from HEAD a8ecdce7.
- Chapters 23, 27 and 37 are unchanged since the work began. Chapter 95 changed during it (commit 9fe993fc, P-F123
  merge, other sections); the texts were re-based onto it.
- Scratch merge: /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/ps7/tree/
- lint --chapters: 0 hits (4782 → 4783 labels). assemble --check: 0 problems. Assembled PAPER.md: lint 0 hits, maximum
  line 121 characters. The new lemma assembles as Lemma 14.15.

## [Hin26d] p. 59, verbatim (arXiv:2408.06651v1, read through alphaXiv; pages confirmed by its PDF reader)

The page opens with the end of Remark 3.57, whose start is on p. 58 (section 2.2):

> as p varies.) Since imposing this condition would not lead to any simplifications, we do not do this here.
>
> We now generalize Definitions 3.8, 3.25, and 3.31.
>
> **Definition 3.58** (Symbols). Let w = (w_p)_(p∈P) be a weight on (P × M, 𝓑^×). Let m ∈ ℝ. Then we say that a family
> a = (a_p)_(p∈P) lies in wS^m(^𝒱T*M) if a_p ∈ w_pS^m(^(𝒱_p)T*M) for all p ∈ P, with uniformly bounded symbol
> seminorms. The elliptic set and essential support of a, as subsets of 𝔐, are defined in complete analogy with
> Definition 3.25.
>
> Carefully note that for w = (w_p)_(p∈P) to be a weight on (P × M, 𝓑^×), it is necessary but not sufficient that each
> w_p be a weight on (M, 𝓑_(p,×)); a sufficient additional condition is that the ratios w_(p,α)/w_(p,β) for
> α, β ∈ 𝒜_p with U_(p,α) ∩ U_(p,β) ≠ ∅ are uniformly bounded.
>
> **Definition 3.59** (𝒱-ps.d.o.s: parameterized setting). In the notation of Definition 3.58, a 𝒱-pseudodifferential
> operator A ∈ wΨ^m_𝒱(M) is a family A = (A_p)_(p∈P) of operators A_p = Op_(𝒱_p)(a_p) + R_p where the quantization map
> Op_(𝒱_p) is defined as in Definition 3.31, (a_p)_(p∈P) ∈ wS^m(^𝒱T*M), and (R_p)_(p∈P) is a family of residual
> operators R_p on (M, 𝓑_(p,×)) for which the conditions in Definition 3.34 hold with uniform constants and operator norm
> bounds for all weights w′ in (3.30). The principal symbol of A is the equivalence class of a in
> wS^m(^𝒱T*M)/wρS^(m−1)(^𝒱T*M). Finally, the space wDiff^m_𝒱(M) of 𝒱-differential operators is the subspace of
> wΨ^m_𝒱(M) consisting of differential operators.
>
> An operator A = (A_p)_(p∈P) ∈ wΨ^m_𝒱(M) defines a uniformly bounded family of operators
>
>     A_p : w′_pH^s_(𝒱_p)(M) → w_pw′_pH^(s−m)_(𝒱_p)(M),
>
> and more generally A_p : w′_pH^(s;k)_(𝒱_p;𝒲_p)(M) → w_pw′_pH^(s−m;k)_(𝒱_p;𝒲_p)(M). (This is in fact a special case
> of Theorem 3.44, applied to the scaled b.g. structure (P × M, 𝓑^×) and the input u = (u_p)_(p∈P) where u_p = 0 for all
> p ≠ p_0 ∈ P and u_(p_0) ∈ w′_(p_0)H^s_(𝒱_(p_0))(M) with norm ≤ 1, since then Au = (A_pu_p)_(p∈P) has norm ≤ C for
> some constant C only depending on A; but the norm of Au is bounded from below by the w_pw′_pH^(s−m)_(𝒱_p)(M)-norm of
> A_(p_0)u_(p_0).¹³) The properties of adjoints, compositions, commutators, and principal symbols in Theorem 3.51 carry
> over verbatim.
>
> The membership A = (A_p)_(p∈P) ∈ wDiff^m_𝒱(M) is characterized by requiring that each A_p is a differential operator,
> and (φ_(p,α))_*A_p = Σ_(|β|≤m) w_(p,α)a_(p,α,β)(x)(ρ_(p,α)∂_x)^β where the C^∞((−2, 2)^n)-seminorms of the
> coefficients a_(p,α,β) are uniformly (in p ∈ P, α ∈ 𝒜_p, β ∈ ℕ^n_0) bounded.
>
> **Remark 3.60** (Fully symbolic 𝒱). Analogously to Definition 3.27, one may call 𝒱 fully symbolic if, for every
> ϵ > 0, there exists a compact subset K ⊂ P × M (with P given the discrete topology) so that ρ|_(P×M∖K) < ϵ. In
> parameterized settings, this is occasionally stronger than necessary. For example, the Lie algebra
> 𝒱 = (𝒱_(h_j))_(j∈ℕ), h_j ↘ 0, of semiclassical vector fields on ℝ^n with uniformly smooth coefficients (see §1.2.1)
> does not satisfy this condition due to the lack of decay of the scalings at spatial infinity; nonetheless, if P =
>
> ¹³ Strictly speaking, one needs to apply this argument for all countable subsets P′ ⊂ P of parameters (so that P′ × M
> is second countable and the total index set ⊔_(p′∈P′) 𝒜_(p′) is countable, as required in Definition 1.1); but the
> uniform bound on the operators A_(p′) is independent of P′.

(In the parenthesis, the subscripts p of the norm that bounds the norm of Au from below stand for p_0, as chapter 95
already notes.)

## Verdict on (S7)

The current (S7) is not faithful. "The above holds uniformly in p" claims for all of (S1)–(S6) what p. 59 states only
for three things: the boundedness (via Theorem 3.44 on P′ × M, footnote 13), the properties of Theorem 3.51 ("carry over
verbatim") and the wDiff characterisation. Not stated for parameterised structures: microlocal elliptic regularity
(Proposition 3.55 (3)), the Fredholm property (Remark 3.60 shows full symbolicity can fail), compact inclusions,
duality, and the comparison of structures (Remark 3.57: norms need not be uniformly equivalent).

The item also lacks what the chapters use under (S7):
- Definition 1.9 (p. 9) and its semiclassical case;
- the weight condition after Definition 3.58;
- the wDiff characterisation;
- above all Remark 4.9 (p. 67): "the discussion in §3.7 applies with only straightforward notational modifications" to
  variable orders. Without it there is no parameterised source for variable orders, which 23:778 and 27:444 use;
- p. 64 (phase space weights) and p. 74 ((S10)).

C23-1 fixes the first point but keeps these omissions. Its claim that 23:778 is covered needs Remark 4.9. P-S7-1 is
C23-1 corrected.

## Sites (HEAD line numbers)

- 23:367–369, (S7): replaced (P-S7-1).
- 23:776–778, proof of lem:ii-a-7-1 (variable-order parametrix, uniform in σ): covered by the new (S7). It uses
  Definition 3.59 symbols, Theorem 3.51 verbatim and the boundedness of p. 59, with Remark 4.9. No edit.
- 27:366 (the structure is parameterised): covered by Definition 1.9. No edit.
- 27:444, lem:ii-f-2-2 (a) (uniform boundedness, variable orders, phase space weights): covered by p. 59, Remark 4.9 and
  p. 64. No edit.
- 27:450, lem:ii-f-2-2 (b): asserted uniformly in h but cites only (S5), (S8). Covered; P-S7-4 adds "uniformly in h by
  (S7)".
- 27:460–461, lem:ii-f-2-2 (c) (microlocal elliptic estimate, uniform in h): not stated in [Hin26d]. Proved: P-S7-5 via
  the new lem:ii-a-3-1 (e), which applies Proposition 3.55 (3) on N_(P′) = P′ × M with cut-offs translated into
  WF′ ⊂ Ell via j, then the countable-subset argument.
  - (c) is not provable as stated with Ell read literally as in def:i-b-2-9. At fibre-infinity points over h > 0 the
    "h < h_0" condition is empty, which would make (c) false near h = 1.
  - P-S7-3 corrects the definition of Ell in sec:ii-f-2-1: the bound is required on a neighbourhood at all its points
    over h ∈ (0, 1].
  - P-S7-3 also includes the slice h = 1, needed for "𝒫_ι is compact". ι⁺_ħ is defined over [0, 1)_h.
  - Citing sites of the corrected definition: (c) itself and its uses through prop:ii-f-2-3. There P_(ι,h,z) is
    elliptic at fibre infinity for all h, so I expect them to be unaffected; I did not check every use.
- 37:822–824, proof of lem:iii-h1-3-1 (uniform equivalence of three norms on c/2 ≤ |σ| ≤ 1): not stated in [Hin26d].
  - Restated and proved in P-S7-6 via lem:ii-a-3-1 (f): same cells, scalings within the factor 2/c, scaling weights
    interchangeable, and (d) for the elliptic families.
  - The sentence used two undefined terms, the semiclassical norm at h = |σ|⁻¹ > 1 and "the fixed norm". P-S7-6 defines
    them.
- Chapter 33 (lines 1432, 1447, 1453, 1484, 1516, 1668, 1703–1704, 1747, 1819, 1828, 1904): covered by the new (S7).
  These sites use Definition 1.9, the weights, footnote 13 and the p. 59 argument, wDiff, and order-0 boundedness. No
  edit.
- Chapter 95 (Appendix A): P-S7-7 to P-S7-11 add quotations of the passages now cited:
  - Remark 3.57, the sentence of p. 64, Remark 4.9 and the sentence of p. 74;
  - Proposition 3.55 (3) and the elliptic sets of Definitions 3.25 and 3.43;
  - Remark 3.57 in the numbering note.

## New label and texts

- lem:ii-a-3-1 (chapter 23, after the list of sec:ii-a-3; private, cited from chapters 27 and 37). Its parts:
  - (a) P′ × M is a scaled b.g. structure with ℓ² norms;
  - (b) families restrict to its classes;
  - (c) bounded on countable subsets ⇒ bounded;
  - (d) elliptic families give uniformly equivalent norms;
  - (e) uniform microlocal elliptic estimate;
  - (f) same charts and comparable scalings ⇒ the same classes and uniformly equivalent norms.
- Eleven placement items, all independent. Crosswalk: five changed rows and one new row (lem:ii-a-3-1, source
  P-S7.md@COMMIT:418-529).

## For the coordinator

- The published number of Remark 4.9 is not covered by the appendix note's rules and I could not check it. Only arXiv
  v1 was available, as PDF and HTML.
- notes/reports/P-G1-C23-1-deferred.md is closed by P-S7-1.
- Outside the (S7) sites: prop:ii-f-2-3 uses the locality of products (thm:i-b-2-4 (iv)). For constant orders [Hin26d]
  gives it uniformly as (3.38) "carried over verbatim", and for variable orders through Remark 4.9. Its translation to
  𝒫_ι is of the same kind as in lem:ii-a-3-1 (e). Not checked further.
