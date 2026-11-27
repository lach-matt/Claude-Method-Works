# P-S7: the paraphrase (S7) of [Hin26d] in sec:ii-a-3 and the sites that cite it (chapters 23, 27, 33, 37, 95)

This is a proof file for the coordinator. No file was written in chapters/ or crosswalk/, and none in proofs/ except
this one. This version answers the reading notes/reviews/R-P-S7.md (1 Major, 5 minor, 7 nits) of the version with md5
16e6e03f795d2c73d79116cdce206e38; section 9 lists what changed. Every old text below is copied from the chapters at HEAD
(commit edafc288): chapters/23-s04-compactified.md (md5 58661f3220bae91f567080b61ae42d3d),
chapters/27-s08-iota-normal.md (3e54a9cf5f565c3705732eaa1c2e2fbc), chapters/33-s14-constraint-damping.md
(3c9903830291c7d9b1030e40e6ba85b6), chapters/37-s18-augmented.md (c720c56c058bfbc52cef67623816580b) and
chapters/95-standard-results.md (bdbfff695b2f66f6022311c52e9e4820), equal to the working-tree files. The crosswalk rows
are from crosswalk/23-s04-compactified.tsv (a54a180aea26fbcca1a2bb3669ea658a), 27-s08-iota-normal.tsv
(f19be3aa9b3271feb3e8e178d5322e1d), 33-s14-constraint-damping.tsv (6c799c08c4a333be156ff8baae2542c3),
37-s18-augmented.tsv (a74ee10adbc363846138409aeb43567b) and 95-standard-results.tsv (f18197428a5f85249375febc4c37522b).
Each old text occurs exactly once in its file as whole lines; line numbers are those of these files. The texts were
applied to a scratch copy and checked there (section 8).

## 1. Summary

**What p. 59 states.** [Hin26d] (arXiv:2408.06651v1, the version the edition cites) defines on p. 59 the symbols and
operators of a parameterised structure (Definitions 3.58 and 3.59), states that such operators are bounded uniformly in
p (a special case of Theorem 3.44 on P′ × M, P′ countable, footnote 13), that "the properties of adjoints,
compositions, commutators, and principal symbols in Theorem 3.51 carry over verbatim", and characterises wDiff. It does
not state that "the above", that is (S1)–(S6), holds uniformly in p: microlocal elliptic regularity
([Hin26d, Proposition 3.55 (3)]), the Fredholm property (Theorem 3.52; Remark 3.60 discusses why "fully symbolic" can
fail in parameterised settings), compact inclusions (Theorem 3.21) and duality (Proposition 3.22) are not stated for
parameterised structures, and Remark 3.57 says the Sobolev norms of compatible ℬ^(p,×) need not be uniformly
equivalent. The full text of p. 59 is in section 2.1.

**Verdict.** The current (S7) is not a faithful paraphrase. Its words "the above holds uniformly in p" claim more than
[Hin26d] prints. It also omits three things that the chapters cite under (S7) or need: Definition 1.9 (the definition
itself, and the semiclassical case), the weights of P × M and the wDiff characterisation (cited by chapter 33), and
Remark 4.9 (p. 67), which extends Section 3.7 to variable orders ("the discussion in §3.7 applies with only
straightforward notational modifications"), with p. 64 for phase space weights and p. 74 for (S10). C23-1
(notes/reports/P-G1-C23-1-deferred.md) corrects the first point, but it keeps the omissions, and its claim that 23:778
is covered by its new text needs Remark 4.9, the order 𝗌 there being variable. P-S7-1 is C23-1 corrected accordingly.
It states the weights of P × M by their definition (the bounds of (S2) uniform in p), not by the sufficient condition
printed after Definition 3.58, which read literally is false (section 3); the one site that used that condition
(33:1515–1516) is changed to use the definition (P-S7-18).

**Sites.** Outside its own item and the appendix entry, (S7) is cited at 23:778, 27:366, 27:444 and 37:824, and at
eleven lines of chapter 33; the uniformity of the old words is also used, without a citation of (S7), at 27:450. The
fix round adds the sites that rested on statements [Hin26d] does not give in the form used: the locality of products
on 𝒫_ι (27:552–556), the microlocal elliptic estimate of (S5) for variable orders (23:1052–1054, 27:1432–1436), and the
sufficient condition on weights (33:1515–1516). Each is settled as follows (HEAD line numbers).

| Site | Statement used | Status | Text |
|---|---|---|---|
| 23:367–369, (S7) | the paraphrase | replaced | P-S7-1 |
| 23:776–778, proof of lem:ii-a-7-1 | parametrix of a variable-order elliptic family and its bounds, uniform in σ | covered by the new (S7): p. 59 (Theorem 3.51 verbatim, boundedness) with Remark 4.9 | none |
| 23:1052–1054, proof of lem:ii-a-8-4 (d) | microlocal elliptic estimate of (S5) for a variable order, B = I | proved: lem:ii-a-3-1 (e) | P-S7-12 |
| 27:366, sec:ii-f-2-1 | the semiclassical 0- and cone structure is parameterised | covered (Definition 1.9) | none |
| 27:408–416, sec:ii-f-2-1 | WF′, Ell and the compact phase space; smooth functions on it are symbols | corrected; lem:ii-f-2-phase added | P-S7-3 |
| 27:420, 444–445, lem:ii-f-2-2 (a) | uniform boundedness, with norm bounded by a seminorm, uniformly in h | covered (p. 59, Remark 4.9); the bound by a seminorm made uniform in h | P-S7-13 |
| 27:450, lem:ii-f-2-2 (b) | composition calculus uniform in h (no citation of (S7)) | covered; (S7) cited | P-S7-4 |
| 27:460–461, lem:ii-f-2-2 (c) | microlocal elliptic estimate uniform in h | not stated in [Hin26d]; proved from lem:ii-a-3-1 (e) | P-S7-5, with P-S7-2, P-S7-3 |
| 27:441–442 and 489–491, lem:ii-f-2-2 | locality of products on 𝒫_ι | not stated in [Hin26d]; (h) added and proved from lem:ii-a-3-1 (g) | P-S7-14, P-S7-15 |
| 27:552–556, proof of prop:ii-f-2-3 | the list of what the transferred proofs use | locality added to the list | P-S7-16 |
| 27:1432–1440, proof of lem:ii-f-5-6 (a) | microlocal elliptic estimate of (S5) for a variable order, B = I | proved: lem:ii-a-3-1 (e) | P-S7-17 |
| 33:1515–1516, proof of lem:iv5-calc-structure (b) | the sufficient condition on weights after Definition 3.58 | replaced by the definition | P-S7-18 |
| 37:822–824, proof of lem:iii-h1-3-1 | uniform equivalence of norms on c/2 ≤ \|σ\| ≤ C_0 | not stated in [Hin26d]; proved from lem:ii-a-3-1 (f), (d) | P-S7-6, with P-S7-2 |
| 33:1432, 1447, 1453, 1484, 1668, 1703–1704, 1747, 1819, 1828, 1904 | Definition 1.9, weights, footnote 13 and the p. 59 argument, wDiff, uniform boundedness of order-0 differential operators | covered by the new (S7) | none |
| 95:914–989, Appendix (S7); 95:1093–1138, (S16) | quotations | extended with the passages now cited | P-S7-7 to P-S7-11 |

**27:460 needs a correction of the definition it rests on (P-S7-3).** lem:ii-f-2-2 (c) is asserted uniformly for
h ∈ (0, 1]. With Ell(A) read literally as in def:i-b-2-9 (a neighbourhood U and some h_0 > 0, the bound required only
for h < h_0), the condition is empty at the points of 𝒫_ι at fibre infinity over h_1 > 0: take U inside {h > h_1/2} and
h_0 = h_1/2. Then every A would be elliptic there, and (c) would fail for B microsupported at fibre infinity over
h ∈ [½, 1] (for A = 0, G = I it would give ‖Bu‖_𝐨 ≤ C‖u‖_(𝐨−K𝐞)). P-S7-3 states Ell with the bound on a neighbourhood at
all its points over h ∈ (0, 1]; at points over sf this is the condition of def:i-b-2-9, and the condition does not
depend on the representative of the principal symbol. It also states that the phase space includes the slice h = 1,
which is not a face. The sentence "it is compact" of 𝒫_ι needs this, since ι⁺_ħ is defined over [0, 1)_h, and the new
proof of (c) uses the compactness of the whole phase space. With the corrected definition, (c) is proved as stated. In
the applications of (c) in chapter 27, P_(ι,h,z) is elliptic at fibre infinity for every h (the last sentence of
prop:ii-f-2-6, 27:634, by eq:ii-f-1-10), so the corrected definition holds where it is used; section 4.9 lists every
use.

**Locality on 𝒫_ι (P-S7-3, P-S7-14 to P-S7-16).** The proofs of chapter 21 that prop:ii-f-2-3 transfers use the
locality of products (consequence (iv) of thm:i-b-2-5, WF′_h(AB) ⊂ WF′_h(A) ∩ WF′_h(B), and that an operator with
empty WF′_h is residual), and lem:ii-f-2-2 did not contain it. With WF′ defined by S^(−K𝐞), as at 27:412, it is false:
at ϖ ∈ F_I, A = Op(φe^(−1/ρ_sf)) and B = ρ_0f⁻¹ give ϖ ∉ WF′(A) but ϖ ∈ WF′(AB), since 𝐞 does not lower the weights at
0f, cf, tf. P-S7-3 defines WF′ with S^(𝐨−K𝐞) (relative to the order 𝐨 at which A is taken), which for Ψ⁰ is the old
condition; lem:ii-f-2-2 (h) (P-S7-14, P-S7-15) states and proves locality, from lem:ii-a-3-1 (g); and P-S7-16 lists it
in the proof of prop:ii-f-2-3.

**37:824 is restated before it is proved.** The sentence uses "the semiclassical norm at the semiclassical parameter
|σ|⁻¹" for |σ| < 1, where sec:ii-a-5-1 (4) defines it only for |σ| ≥ 1, and "the fixed norm" without a definition.
P-S7-6 defines both: the first by the same formula on the space of the spectral structure at σ, the second as the norm
with the same orders of the structure of sec:ii-a-5-1 (2) (the spectral structure at |σ| = 1). It then proves the
uniform equivalence on c/2 ≤ |σ| ≤ 1, extends it to 1 ≤ |σ| ≤ C_0, and identifies the fixed norm, uniformly for
c/2 ≤ |σ| ≤ C_0, with the norm of the orders (s_c, 𝗋_σ + β) in which thm:i-a-7-2 is applied in the next paragraph. That
the latter is the fixed-frequency space of thm:i-a-7-2 at each σ is (C1) of def:iii-h1-1-1 with sec:ii-a-5-1 (2), and
is unchanged.

**The new lemma (P-S7-2).** lem:ii-a-3-1, after the list in sec:ii-a-3, carries out the reduction that C23-1 suggests,
as in the proof of prop:np-10-65-a.
- (a)–(c): N_(P′) := P′ × M is a single scaled b.g. structure. Its norms are the ℓ² sums of the norms of the slices.
  Families of the parameterised classes restrict to its classes. A function on P that is bounded on every countable
  subset is bounded.
- (d): elliptic families defining the variable-order norms give uniformly equivalent norms.
- (e): an elliptic estimate uniform in p, with its hypotheses stated by three cut-off families. It is proved by a
  parametrix with nested cut-off symbols, as in lem:ii-a-8-4 (b)–(c), from the calculus of (S7) and (S8) and from (g)
  only, for variable orders, for the (S8) classes and for ℂ^N-valued systems; Proposition 3.55 (3) is not used.
- (f): parameterised structures with the same charts and comparable scalings have the same classes and uniformly
  equivalent norms; this is the comparison of different structures that Remark 3.57 says is not automatic.
- (g): locality of products in terms of cut-off symbols, uniform in p: (3.38) on each N_(P′) (Theorem 3.51, with (S8)
  for variable orders), translated back from the microlocalisation locus to the symbols by the continuous extension j.

**The new lemma (P-S7-3).** lem:ii-f-2-phase: a smooth function on the compactified phase space of chapter 27 lies in
S⁰, uniformly in h. Chapter 27 used this without proof (the orders are smooth functions on that space and "variable
orders in the sense of (S8)"); the new proof of (c) and the proof of (h) use it for their cut-offs.

**No other open proof file meets these lines** (grep of proofs/ for the old texts and the labels).

**md5 and length of this file:** given in the report (it cannot contain its own md5).

## 2. What [Hin26d] prints

The text is that of arXiv:2408.06651v1, read in full through the alphaXiv full-text tool. Pages were confirmed with
the alphaXiv PDF reader, whose output for pp. 9, 58, 59, 64, 66 and 67 is the text below. Remark 4.9 was confirmed
independently in the arXiv HTML through the Firecrawl paper reader; that is the same version, as Lemma 2.11 and the
footnote numbers agree. Mathematics is written in the Unicode notation of chapter 95; subscripts in parentheses.

### 2.1 Page 59, in full

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

### 2.2 The other passages used

**Definition 1.9, p. 9**, with the paragraph after it:

> Let M be a smooth n-dimensional manifold, and let P be a set. Then a parameterized scaled bounded geometry structure on
> (M, P) is a collection {𝓑_(p,×)} of scaled bounded geometry structures 𝓑_(p,×) = {(U_(α_p), φ_(α_p), ρ_(α_p)) :
> α_p ∈ 𝒜_p} on M for each p ∈ P so that the quantities A and the C^∞ bounds on transition functions in Definition 1.1
> as well as the constants C_γ in (1.6) are uniform also in p ∈ P. […] Furthermore, it includes semiclassical bounded
> geometry settings when P = (0, 1]_h if all 𝓑_(h,×) feature the same b.g. structure {(U_α, φ_α)}, and the scalings are
> ρ_(α_h,i) = h for h ∈ (0, 1].
>
> The generalization of Theorem 1.4 for parameterized scaled b.g. structures, discussed in §3.7, asserts the existence
> of an algebra Ψ_𝒱(M) of 𝒱-pseudodifferential operators with the usual properties (principal symbol calculus,
> boundedness on weighted Sobolev spaces). […] Similarly, the relevant Sobolev spaces are p-dependent function spaces
> (corresponding to the scaled b.g. structure 𝓑_(p,×)), and the boundedness of ps.d.o.s is understood as uniform (in p)
> boundedness.

**p. 58** (start of Section 3.7): "On the space P × M = ⊔_(p∈P) {p} × M, with P given the discrete topology, we can
again consider the space of uniformly continuous functions […]". "Denote by ρ_p ∈ C^∞(M) a scaling weight for
(M, 𝓑_(p,×)) from Definition 3.6 (with constants which are independent of p, cf. the discussion following
Definition 3.58 below), and by λ_p ∈ S^(−1)(^(𝒱_p)T*M) a uniformly bounded family of weights as in Lemma 3.24 for which
λ^(−1) ∈ S¹(^(𝒱_p)T*M) is uniformly bounded as well. Write ρ, λ for the functions which on {p} × M, resp.
{p} × ^(𝒱_p)T*M are given by ρ_p, λ_p. Analogously to Definition 3.25, the microlocalization locus is then the compact
subset 𝔐 := u(^𝒱T*M) ∩ {j(ρλ) = 0}. (3.40)"

**Remark 3.56** (Subsets of P), p. 58: "In applications, one often only works with operators defined for (typically
countable) subsets of parameters p ∈ P (e.g. in the semiclassical setting: sequences of semiclassical parameters
h_j ↘ 0). Since one can implement this simply by replacing P by such a subset (and then defining the microlocalization
locus as in (3.40) for the new set P), we do not explicitly allow for symbols to be defined only on subsets of P here."

**Remark 3.57** (Compatibility of different scaled b.g. structures), pp. 58–59: "In applications, two scaled b.g.
structures 𝓑_(p,×) and 𝓑_(p′,×) for different values of p, p′ ∈ P are often strongly compatible, though not uniformly
so in p and p′ ∈ P. (This implies, for example, the equality of all Sobolev spaces H^s_(𝒱_p)(M) as sets, but still
allows for the norms to not be uniformly equivalent as p varies.) Since imposing this condition would not lead to any
simplifications, we do not do this here."

**p. 60** (end of Remark 3.60 and the sentence after): "[if P =] (P_(h_j))_(j∈ℕ) ∈ Ψ^m_𝒱(ℝ^n) is elliptic, then it is
invertible between H^s_(𝒱_(h_j))(ℝ^n) = H^s_(h_j)(ℝ^n) and H^(s−m)_(𝒱_(h_j))(ℝ^n) = H^(s−m)_(h_j)(ℝ^n) when h_j is
sufficiently small. Indeed, P has a parametrix Q ∈ Ψ^(−m)_𝒱(ℝ^n) with QP = I + R, R ∈ hΨ^(−1)_𝒱(ℝ^n) […]. Similarly,
the notion of wave front set (Definition 3.54) generalizes to the parameterized setting, with WF^(m,w,l)_𝒱(u) ⊂ 𝔐
defined for u = (u_p)_(p∈P) ∈ wρ^(−∞)H^(−∞)_𝒱(M), by which we mean that u_p ∈ w_pρ_p^(−N)H^(−N)_(𝒱_p)(M) for some fixed
N, with norm bounded uniformly in p." This is the only statement about ellipticity in the parameterised setting; no
parameterised version of Proposition 3.55 is stated.

**p. 64** (Section 4.1): "Operators with phase space weights can also be defined in the parameterized scaled b.g.
setting. As an application, this allows one to recover the resolved algebra […] which was introduced by Vasy [Vas21c]
for low energy resolvent analysis. We leave the details to the interested reader."

**Remark 4.9** (Parameterized version), p. 67, in Section 4.2 (variable orders, (S8)): "The discussion in the present
section generalizes to variable order symbols, ps.d.o.s, and Sobolev spaces depending on a parameter; indeed, the
discussion in §3.7 applies with only straightforward notational modifications. For example, in a semiclassical bounded
geometry setting, one can work with variable semiclassical orders. Applications in the literature include [Gal19, §2.3]
and [HV17]; see also Example 4.19."

**p. 74** (Section 4.4, commutator 𝒲-vector fields, (S10)): "We only discuss the scaled b.g. setting, and leave the
purely notational modifications for parameterized settings to the reader."

**Theorem 3.44**, p. 51: "Let w, w′ ∈ C^∞(M) be weights on (M, 𝓑); let s, m ∈ ℝ. Then every A ∈ wΨ^m_𝒱(M) defines a
bounded linear map w′H^s_𝒱(M) → ww′H^(s−m)_𝒱(M), and more generally w′H^(s;k)_(𝒱;𝒲)(M) → ww′H^(s−m;k)_(𝒱;𝒲)(M) for all
k ∈ ℕ₀."

**Theorem 3.51**, pp. 55–56: "Let w, w_1, w_2 ∈ C^∞(M) be weights on (M, 𝓑). Let m, m_1, m_2, l, l_1, l_2 ∈ ℝ. Fix a
uniformly positive 𝒱-density on M. Then A ∈ wρ^(−l)Ψ^m_𝒱(M) ⟹ A* ∈ wρ^(−l)Ψ^m_𝒱(M),
A_j ∈ w_jρ^(−l_j)Ψ^(m_j)_𝒱(M) ⟹ A_1 ∘ A_2 ∈ (w_1w_2)ρ^(−(l_1+l_2))Ψ^(m_1+m_2)_𝒱(M). Furthermore,
σ^(m,l)_𝒱(A*) = σ^(m,l)_𝒱(A)‾ and σ^(m_1+m_2,l_1+l_2)_𝒱(A_1 ∘ A_2) = σ^(m_1,l_1)_𝒱(A_1) · σ^(m_2,l_2)_𝒱(A_2). The
principal symbol of i[A_1, A_2] ∈ wρ^(−(l_1+l_2−1))Ψ^(m_1+m_2−1)_𝒱(M) is the Poisson bracket of the principal symbols
of A_1, A_2. Finally, WF′^(w_1w_2)_𝒱(A_1 ∘ A_2) ⊂ WF′^(w_1)_𝒱(A_1) ∩ WF′^(w_2)_𝒱(A_1). (3.38) The map A ↦ A* is
continuous, and the map (A_1, A_2) ↦ A_1 ∘ A_2 is jointly continuous." (The last A_1 of (3.38) stands for A_2.)

**Proposition 3.55** (3), p. 57: "(3) (Microlocal elliptic regularity.) If WF′_𝒱(B) ⊂ Ell^(m,w)_𝒱(A), then for any N
there exists C_N so that ‖Bu‖_(wρ^lH^m_𝒱(M)) ≤ C_N(‖Au‖_(ww′ρ^lH^(m−m′)_𝒱(M)) + ‖u‖_(wρ^(−N)H^(−N)_𝒱))", for
A ∈ w′Ψ^(m′)_𝒱(M) and B ∈ Ψ⁰_𝒱(M); the superscripts of the elliptic set stand for those of A.

**Definition 3.25**, p. 41 (the elliptic set): "Let w ∈ C^∞(^𝒱T*M) be a weight on (^𝒱T*M, 𝓑*). For a symbol
a ∈ wS⁰(^𝒱T*M), we define its elliptic set by Ell^w_𝔐(a) := {ϖ ∈ 𝔐 : ∃ b ∈ w⁻¹S⁰(^𝒱T*M),
ϖ ∉ supp_(u^𝒱T*M)(ab − 1)} ⊂ 𝔐." **Definition 3.43**, p. 51: "Using Lemma 3.29, we define the elliptic set of A as
Ell^(m,w)_𝒱(A) := Ell^(wλ^(−m))_𝔐(σ^(m,w)_𝒱(A))".

**Definition 4.6**, p. 66, and the text after it (variable orders): "ρ^(−𝗅)S^𝗆(^𝒱T*M) := ρ^(−𝗅)λ^(−𝗆) ⋂_(δ∈(0,1/2))
S⁰_(1−δ,δ)(^𝒱T*M)", "wΨ^(𝗆,𝗅)_𝒱(M) := {Op_𝒱(a) + R : a ∈ wρ^(−𝗅)S^𝗆(^𝒱T*M), R ∈ wρ^∞Ψ^(−∞)_𝒱(M)}", the principal
symbol taken modulo ⋂_δ wρ^(−𝗅+1−2δ)S^(𝗆−1+2δ) (4.10), "Fixing an elliptic operator A ∈ wρ^(−𝗅)Ψ^𝗆_𝒱(M), we
furthermore define wH^(𝗆,𝗅)_𝒱(M) := {u ∈ wρ^(inf 𝗅)H^(inf 𝗆)_𝒱(M) : Au ∈ L²(M)}", and "Theorem 3.44 remains valid,
mutatis mutandis, in the variable order case. As the microlocalization locus, one may work with 𝔐."

## 3. The verdict in detail

The current item reads: "(S7) [Hin26d, Definitions 3.58 and 3.59, p. 59.] For a parameterised scaled b.g. structure
(ℬ^(p,×))_(p∈P), with all bounds uniform in p, the above holds uniformly in p; operators are families with uniformly
bounded symbols and residual parts, bounded uniformly on the p-dependent spaces."

- "the above" is (S1)–(S6): structures, weights, Sobolev spaces (with their compact inclusions and duality),
  quantisation, the calculus (boundedness, adjoints, compositions, principal symbols, commutators, WF′ of products),
  microlocal elliptic regularity and the Fredholm property, and the regularity of symbols. p. 59 states uniformly in p
  only the boundedness, the properties of Theorem 3.51 and the wDiff characterisation. p. 9 summarises §3.7 as "the
  usual properties (principal symbol calculus, boundedness on weighted Sobolev spaces)". Remark 3.60 shows that the
  fully symbolic condition behind the Fredholm property can fail, and Remark 3.57 that norms need not be uniformly
  equivalent. So "the above holds uniformly in p" is not what [Hin26d] states. It is true for some items (the calculus)
  and is not stated for others (Proposition 3.55 (3), Theorems 3.21 and 3.52, Proposition 3.22, comparisons of
  structures).
- The rest of the sentence is faithful, but the cited range (Definitions 3.58 and 3.59, p. 59) leaves out what the
  chapters use under (S7): Definition 1.9 and its semiclassical case (33:1447, 1484, 1904; 27:366), the weights
  (33:1453, 1516), footnote 13 and the argument of p. 59 (33:1432, 1819), and the wDiff characterisation (33:1828; with
  the boundedness, 33:1668, 1703–1704).
- For variable orders it has no source: Section 3.7 is stated for constant orders, and Section 4.2 (variable orders)
  for a single structure. Remark 4.9 (p. 67) is the statement that joins them, and it is needed at 23:778 (the order 𝗌
  of lem:ii-a-7-1 is variable) and 27:444 (the orders 𝐨 are variable). Likewise p. 64 for the phase space weights of
  27:444, and p. 74 for the subalgebra of (S10) in which chapter 27 takes its classes.

C23-1 drops "the above holds uniformly in p" and adds the boundedness argument and Theorem 3.51. P-S7-1 keeps this,
and adds Definition 1.9, the weights, the wDiff characterisation, Remarks 3.56–3.57, Remark 4.9 and pp. 64, 74. It
ends with a pointer to the new lemma for what [Hin26d] does not state.

Two readings are made explicit.
- (i) "for all weights w′ in (3.30)" in Definition 3.59 is read as all weights of P × M, which is how p. 59 uses it:
  the structure there is P × M.
- (ii) For variable orders, the calculus of Theorem 3.51, with (3.38) (WF′ of a product), is used through (S8), which
  reads Theorem 3.44 "remains valid, mutatis mutandis, in the variable order case" as including that calculus;
  lem:ii-a-3-1 applies it only to single structures, the N_(P′). The microlocal elliptic estimate of Proposition
  3.55 (3), stated for constant orders and scalar operators, is not used outside its scope: lem:ii-a-3-1 (e) proves the
  estimate from the calculus and (g), and the two sites that applied Proposition 3.55 (3) to variable orders through
  that reading of (S8) (23:1052–1054 and 27:1432–1436) now cite (e) (P-S7-12, P-S7-17).

**The weights.** After Definition 3.58, [Hin26d] states that for w = (w_p) to be a weight of P × M it is necessary but
not sufficient that each w_p be a weight of ℬ^(p,×), "a sufficient additional condition" being the uniform boundedness
of the ratios w_(p,α)/w_(p,β) over overlapping cells (section 2.1). Read literally the sufficient condition is false:
on M = ℝ with the standard cells and P = ℕ, w_p := 2 + sin(p²x) is a weight of each ℬ^(p,×) and the ratios of its
weight families are at most 3, but ∂_xw_p/w_p is of size p², so (w_p) is not a weight of P × M. P-S7-1 therefore
states the definition (the bounds of (S2) for the cells of all ℬ^(p,×) together, uniform in p) and the necessity
remark, not the sufficient condition. Its one use, 33:1515–1516, concerns weights and charts that do not depend on h,
for which the bounds of (S2) are uniform trivially; P-S7-18 says so. The quotation of the passage in Appendix A
(95:969–970) is accurate as a quotation and is kept.

## 4. The sites

### 4.1 23:776–778, the proof of lem:ii-a-7-1 (uniform duality): covered, no change

The sentence is "It is built as in [[lem:ii-a-8-4]] (b), with I in place of B there, by (S5), (S7) and (S8)." With
B = I and A elliptic everywhere, all the cut-offs χ̃_j of lem:ii-a-8-4 (b) can be taken equal to 1. The construction
then uses:
- the quantisation of the family symbols a⁻¹ and σ(R_j)/a;
- compositions with multiplicative principal symbols;
- the principal symbol sequence, that is, an element with principal symbol 0 lies in the class one step lower;
- the uniform boundedness of A, B, R_1, R_2 and their adjoints between the spaces of σ.

For the families of the parameterised calculus these are:
- Definition 3.59, whose principal symbol is the class of a in wS^m/wρS^(m−1), so σ(R_j) is a family;
- Theorem 3.51 "carry over verbatim";
- the boundedness of p. 59;
- for the variable order 𝗌, the same with (S8), by Remark 4.9.

All are in P-S7-1. The density of C_c^∞ in the proof is a statement at each fixed σ. So the new (S7) covers the site as
it stands, as C23-1 said, once Remark 4.9 is included.

### 4.2 27:366 and 27:420, 444–445, lem:ii-f-2-2 (a): covered; the bound by a seminorm made uniform (P-S7-13)

- 27:366 calls the semiclassical 0- and cone structure "the parameterised scaled b.g. structure (S7)". That is
  Definition 1.9.
- (a) is "(S5) with (S7), (S8) and (S11)": boundedness uniform in h, in orders 𝐨 with variable 𝗌 and 𝖻, and with the
  weights at 0f, cf, tf. This is the boundedness of p. 59, with Remark 4.9 for variable orders.
- "with norm bounded by a seminorm of A", uniformly in h, is not given by the uniform boundedness of each family alone:
  on N_(P′) the bound holds by (S5) and lem:ii-a-3-1 (b), but its constant and seminorm might depend on P′. P-S7-13
  adds the diagonal argument: if no constant and seminorm served for all h, there would be h_k and A_k with
  ‖(A_k)_(h_k)‖ > kq_k(A_k) for an increasing sequence of seminorms q_k, against the bound on N_(P′) for
  P′ := {h_k : k ∈ ℕ} (for k ≥ max(k_0, C), q_k ≥ q_(k_0) gives ‖(A_k)_(h_k)‖ ≤ Cq_(k_0)(A_k) ≤ kq_k(A_k)).

### 4.3 27:450, lem:ii-f-2-2 (b): covered; (S7) cited (P-S7-4)

(b) is stated uniformly in h, and its proof cites (S5) and (S8) only. The uniformity is p. 59 ("carry over verbatim")
with Remark 4.9. P-S7-4 adds "uniformly in h by (S7)".

### 4.4 27:460–461, lem:ii-f-2-2 (c): not stated in [Hin26d]; proved (P-S7-5, with P-S7-2 and P-S7-3)

The current proof is "(c) is the microlocal elliptic estimate of (S5), with (S8) for variable orders, localised by the
composition calculus as in the proof of [[prop:i-b-2-10]]." Two things are missing.
- The estimate of (S5) is Proposition 3.55 (3), stated for one scaled b.g. structure, constant orders and scalar
  operators. With the old (S7) its uniformity in h was part of "the above holds uniformly in p"; [Hin26d] does not
  state it, nor its form for variable orders or systems.
- The hypothesis WF′(B) ⊂ Ell(A) ∩ Ell(G) of (c) concerns the compactified phase space of chapter 27, including sf.
  Proposition 3.55 (3) has its hypothesis on the microlocalisation locus 𝔐 of the structure.

The new proof works as follows.
- It chooses cut-offs y_1, y_2, y_3 on the compact phase space X; they lie in S⁰ by lem:ii-f-2-phase.
- (1 − y_1)b is residual: away from 𝒫_ι by (f) (i) of the same lemma, near 𝒫_ι ∖ WF′(B) by the definition of WF′
  (B ∈ Ψ⁰, so the weighted and unweighted conditions agree).
- y_3(ga)⁻¹ is a symbol, by (d) of the lemma with lem:i-b-2-2 (e).
- It applies lem:ii-a-3-1 (e) to GA and B. That estimate is proved by a parametrix B = QGA + R_K with nested cut-off
  symbols z_k = φ_k(y_2), using only the composition calculus with principal symbols (S7), (S8) and the locality (g),
  whose proof does not use (e); it holds for variable orders, the (S8) classes and systems, uniformly in p.
- No localisation as in prop:i-b-2-10 is needed, since the estimate is applied to the product GA, whose principal symbol
  is ga.

The statement of (c) is not provable with Ell read literally as in def:i-b-2-9, at the points of fibre infinity over
h > 0 (section 1). It is provable with the reading of P-S7-3, and P-S7-3 also includes h = 1, for the compactness.

### 4.5 37:822–824, the proof of lem:iii-h1-3-1: not stated in [Hin26d]; restated and proved (P-S7-6)

The claim is a uniform equivalence of the norms of different scaled structures over a compact set of σ. Remark 3.57 is
the warning that this is not automatic, and no statement of [Hin26d] gives it. P-S7-6 proves it from lem:ii-a-3-1 (f).
- The spectral structures at σ (scalings (1 + |σ|⟨x⟩)⁻¹ on the b-cells) and at |σ| = 1 have the same cells and
  scalings within the factor 2/c on c/2 ≤ |σ| ≤ 1, and within C_0 on 1 ≤ |σ| ≤ C_0, so their classes coincide and their
  norms are uniformly equivalent.
- The three norms are those of w_∗ϱ^(𝗌_σ)H^(𝗌_σ), of the variable orders (𝗌_σ, 𝗌_σ), with w_∗ = ρ_scf^βρ_tf^β and
  ϱ = ρ_scf (sc-b), w_∗ = ρ^β and ϱ = hρ (semiclassical), w_∗ = ρ^β and ϱ = ρ (fixed). Since ρ_scf⟨x⟩, hρ⟨x⟩ and ρ_tf
  are bounded above and below on the compact set of σ, with bounded b-derivatives of the logarithms, these scaling
  weights and the base weights are interchangeable, uniformly ((f), last sentence).
- (d) removes the dependence on the elliptic families.
- The next paragraph of the proof applies thm:i-a-7-2 in the norm of the orders (s_c, 𝗋_σ + β). P-S7-6 identifies the
  fixed norm with it, uniformly for c/2 ≤ |σ| ≤ C_0: 𝗌_σ − s_c vanishes at fibre infinity ((C1)) and 𝗌_σ − 𝗋_σ over
  ∂X, so λ^(s_c−𝗌_σ), ρ^(𝗋_σ−𝗌_σ) and their inverses are bounded in S⁰, the two pairs of orders define the same
  classes, and the first terms of the two norms are bounded by each other modulo the second, as in the proof of (d).

The two terms the original sentence leaves undefined are defined in the new text (section 1).

### 4.6 Chapter 33: covered; one sentence changed (P-S7-18)

At the current HEAD these are lines 1432, 1447, 1453, 1484, 1516, 1668, 1703–1704, 1747, 1819, 1828 and 1904. Each
uses one of: Definition 1.9 and its semiclassical case; the weights of P × M; the device of footnote 13 and the
argument of p. 59; the wDiff characterisation; the uniform boundedness of families of order-0 differential operators.
All are in P-S7-1. The section's proofs carry out the reduction to N_(P′) themselves (def:iv5-calc-cells,
prop:np-10-65-a). They are consistent with lem:ii-a-3-1 and need not cite it. The one exception is 1515–1516, which
cited "the sufficient condition after [Hin26d, Definition 3.58]"; read literally that condition is false (section 3),
and the site does not need it, the weights and charts there not depending on h. P-S7-18 replaces the sentence by the
definition: the bounds of (S2) for the parameterised structure are those for ℬ, uniformly in h.

### 4.7 Chapter 95: Appendix A extended (P-S7-7 to P-S7-11)

The appendix entry (S7) of thm:std-sbg-calculus already quotes p. 59 accurately. It now gains:
- Remark 3.57, the sentence of p. 64, Remark 4.9 and the sentence of p. 74, with the header's ranges;
- in (S16), Proposition 3.55 (3) and the elliptic set of Definitions 3.25 and 3.43, which (S5) of sec:ii-a-3 cites
  (lem:ii-a-3-1 (g) uses the microlocalisation locus, j and the essential support quoted there already);
- in the numbering note, Remark 3.57.

The note's rule (each number from Lemma 3.36 to Definition 3.61 increased by one) makes Remark 3.57 Remark 3.58 in the
published version. The published number of Remark 4.9 is not covered by the note's rules and I could not check it
(section 6.5).

### 4.8 27:552–556, the proof of prop:ii-f-2-3: locality of products (P-S7-3, P-S7-14 to P-S7-16)

The transferred proofs of chapter 21 use the locality of products: consequence (iv) after thm:i-b-2-5, its corollary
WF′_h(AB) ⊂ WF′_h(A) ∩ WF′_h(B) after def:i-b-2-9, and that an operator with empty WF′_h is residual (for instance
21:561–562, "Ǎ(I − Φ) and (I − Φ)^(*h)Ǎ are residual"; 21:481, "E ∈ Ψ^(2𝐦−(1−ϵ)𝟏) near WF′_h(B)"; lem:i-b-3-4, the G_j
with WF′(G_j) ⊂ Ell(B^(j))). lem:ii-f-2-2 (a)–(e) contain no locality statement, so the list in the proof of
prop:ii-f-2-3 was incomplete.

- With WF′ defined by S^(−K𝐞) (27:412–413) locality is false: 𝐞 = (1; 0, 0, 0; 1) does not lower the weights at 0f,
  cf, tf. At ϖ ∈ F_I take A = Op(φe^(−1/ρ_sf)) ∈ Ψ⁰, φ a cut-off near ϖ, and B = ρ_0f⁻¹ ∈ Ψ^((0;1,0,0;0)); then
  ϖ ∉ WF′(A), as e^(−1/ρ_sf) ≤ C_Kρ_sf^K, but the symbol of AB is not O(ρ_sf^K) near ϖ (on x_I = e^(−2/h) it grows),
  so ϖ ∈ WF′(AB).
- P-S7-3 defines WF′(A), for A ∈ Ψ^𝐨, with S^(𝐨−K𝐞), that is, by the weighted essential support of [Hin26d,
  Definition 3.25] (χa ∈ wρ^∞S^(−∞)). In chapter 21, S^(−M𝟏) for every M equals S^(𝐨−M𝟏) for every M, so this is the
  faithful transport of def:i-b-2-9; for Ψ⁰ it is the old condition. The set depends on the order at which A is
  taken only through the weights at 0f, cf and tf, and the text says that the order is the one at which A is
  considered.
- lem:ii-f-2-2 (h) states WF′(AB) ⊂ WF′(A) ∩ WF′(B) and that A ∈ Ψ^(𝐨−K𝐞) for every K when WF′(A) = ∅. Its proof
  takes cut-offs y, y′ ∈ C^∞(X) (in S⁰ by lem:ii-f-2-phase) near ϖ ∉ WF′(A) and applies lem:ii-a-3-1 (g); the second
  statement is the partition of unity of the proof of (c) with y_1 = 0.
- lem:ii-a-3-1 (g) is the translation from the locus 𝔐 to the symbols: on each N_(P′), (3.38) puts the essential
  support of the product's symbol in {j(y) = 0}; a compactness argument on Z = 𝔐 ∩ supp j(y′) and a cut-off
  θ = ψ(Σ|χ_i|²) split y′c into a part with the factor χ_ic and a part supported where ρλ is bounded below; uniformity
  in p is (c) of the lemma.
- P-S7-16 adds the locality, with (h), to the list in the proof of prop:ii-f-2-3. In chapter 21's terms "residual" is
  transported by (D4) as the orders 𝐨 − K𝐞 for every K, which is what (h) gives.

### 4.9 The uses of WF′ and Ell of chapter 27 with the weighted WF′

WF′ and Ell of def:i-b-2-9 transported to 𝒫_ι are used only in chapter 27 and, through prop:ii-f-2-4 to 2-6, in
chapter 35; every other WF′ and Ell in the edition belongs to another calculus (sc, e3b, 3b,ħ, 0,b at fixed σ, ebe, the
cone calculus of chapter 35), whose definitions P-S7 does not touch. Chapter 21's own WF′_h and Ell_h (the h = 0 face 𝒫)
are unchanged.

| Site | Use | With the weighted WF′ and the corrected Ell |
|---|---|---|
| 27:408–416 | definitions | changed by P-S7-3 |
| 27:427, lem:ii-f-2-2 (c) | WF′(B) ⊂ Ell(A) ∩ Ell(G), B ∈ Ψ⁰ | B ∈ Ψ⁰, so WF′(B) is unchanged; proved by P-S7-5 |
| 27:441–442, 489–491 (new (h)) | locality | proved for the weighted WF′; false for the unweighted one (section 4.8) |
| 27:544–556, prop:ii-f-2-3 | transfers chapter 21's proofs | ch. 21's S^(−M𝟏) for all M is S^(𝐨−M𝟏) for all M, so the weighted WF′ is the faithful transport; locality by (h) |
| 27:562 | "(1 − φ_1)Ǎ is residual" | from (f) (i) (support in {ρ_sf ≥ 2δ_s} at finite frequencies), not from WF′; unaffected |
| 27:600, 622, prop:ii-f-2-4, 2-5 | B_* microsupported in U_*, G elliptic on Ū_0, E′ elliptic on K_E | the microsupported operators are in Ψ⁰, so their WF′ is unchanged; ellipticity at finite frequencies over sf, where the corrected and literal Ell agree |
| 27:632–638, prop:ii-f-2-6 | WF′(B) ⊂ K_0, G elliptic on K_0; fibre infinity in Ell(P′) for every z | B ∈ Ψ⁰; the last sentence holds in the corrected sense (the principal symbol at fibre infinity is eq:ii-f-1-10 in the rescaled fibre variables, independent of h and z) |
| 27:652 | P_(ι,h,z) elliptic at fibre infinity | as prop:ii-f-2-6 |
| 27:884–888, lem:ii-f-3-4 (a) | fibre infinity ⊂ Ell(P); points over sf with G ≠ 0 | as prop:ii-f-2-6 |
| 27:906–930, lem:ii-f-3-4 (d)–(e) | joint ellipticity on 𝒫_ι, a microlocal partition of unity, G microsupported at finite frequencies | the partition-of-unity bound is (c) with B = G = I, which needs the joint ellipticity at fibre infinity uniformly in h (the corrected Ell); the operators are in Ψ⁰ |
| 27:1159–1160, lem:ii-f-4-4 | elliptic regularity at fibre infinity at a fixed h | (c) with the corrected Ell; the regularity form is that of lem:ii-a-3-1 (e) |
| 27:1183–1185, prop:ii-f-4-3 | hypotheses of prop:ii-f-2-4 to 2-6 for the system | as prop:ii-f-2-6 |
| 35:851–912, lem:iii-g-4-5, prop:iii-g-4-6 | prop:ii-f-2-4 to 2-6 near the cone | through those propositions; unaffected |

### 4.10 23:1052–1054 and 27:1432–1440: the elliptic estimate for variable orders now cited from lem:ii-a-3-1 (e)

Both sites applied the microlocal elliptic estimate of (S5), that is Proposition 3.55 (3), to a variable order (and
with B = I), through a reading of (S8) that the edition does not state.
- 23:1052–1054, lem:ii-a-8-4 (d): an elliptic Λ ∈ C^∞_bΨ^(𝗌+1)_e3b, single structure, decay order 0. P-S7-12 takes Λ
  elliptic in the sense of lem:ii-a-3-1 (for instance Op(λ^(−𝗌−1)), whose principal symbol has the inverse
  λ^(𝗌+1) ∈ S^(−𝗌−1); lem:ii-a-4-1 applies to every element of the class) and applies (e) with P a point, B = I and
  y_1 = y_2 = y_3 = 1. The remainder of (e) is ‖v‖_(ρ^(−N)H^(−N)) ≤ C‖v‖_(H^(−N)), so the estimate is the one used.
- 27:1432–1440, lem:ii-f-5-6 (a), Step 1: N⁰(σ) at a fixed σ, in the structure of sec:ii-a-6-2. Its principal symbol is
  p Id with |p| ≥ cx_I²ρ_K⁻²λ⁻² where λ ≤ δ (eq:ii-f-1-10 near ℐ⁺, the b-symbol near K⁺, positive definite). P-S7-17
  applies (e) with B = I and y_j = ψ_j(λ) supported where λ < δ: 1 − y_1 vanishes where λ is small, so lies in
  ρ̄^∞S^(−∞), the scaling weight being bounded below at fixed σ (the largest scaling on each cell is at least
  (1 + |σ|)⁻¹ or ⟨σ⟩⁻¹); y_3p⁻¹ ∈ x_I⁻²ρ_K²S^(−2) by the chain rule. The remainder of (e), with N = M, is bounded by
  ‖u‖_(𝒳^(−M)), as before.

## 5. The new chapter texts (placement)

All eighteen items are independent: no two old texts overlap, and they apply in any order (P-S7-14 and P-S7-13 are
separated by the blank line 443).

### P-S7-1. chapters/23-s04-compactified.md, the item (S7) of sec:ii-a-3 (lines 367–369)

Old (3 lines):

```text
(S7) [Hin26d, Definitions 3.58 and 3.59, p. 59.] For a parameterised scaled b.g. structure (ℬ^(p,×))_(p∈P), with all
bounds uniform in p, the above holds uniformly in p; operators are families with uniformly bounded symbols and residual
parts, bounded uniformly on the p-dependent spaces.
```

New (25 lines):

```text
(S7) [Hin26d, Definition 1.9, p. 9; Section 3.7, pp. 58–59: Remarks 3.56 and 3.57, Definitions 3.58 and 3.59 and the text
after them, with footnote 13; p. 64; Remark 4.9, p. 67; p. 74.] A *parameterised scaled b.g. structure* on M with
parameter set P is a family (ℬ^(p,×))_(p∈P) of scaled b.g. structures ℬ^(p,×) = {(U_(p,α), φ_(p,α), ρ_(p,α)) : α ∈ 𝒜_p}
for which the bound on the multiplicity and the C^∞ bounds on the transition maps in (S1), and the constants C_γ of its
scaling condition, are uniform in p; it is *semiclassical* if P = (0, 1]_h, all ℬ^(h,×) have the same charts and all
scalings equal h. The space P × M = ⊔_(p∈P) {p} × M carries the discrete topology in p. Its weights w = (w_p) are those
of (S2) for the cells of all the ℬ^(p,×) together, that is, with the bounds of (S2) uniform in p (that each w_p be a
weight of ℬ^(p,×) is necessary but not sufficient), and the scaling weights ρ = (ρ_p) and elliptic weights λ = (λ_p)
((S8)) are taken with bounds uniform in p. A family a = (a_p) lies in wS^m if a_p ∈ w_pS^m(^(𝒱_p)T*M) for all p, with
seminorms bounded uniformly in p; wΨ^m_𝒱 consists of the families A = (A_p), A_p = Op_(𝒱_p)(a_p) + R_p, with (a_p) ∈ wS^m
and residual R_p of ℬ^(p,×) for which the conditions of (S4) hold with constants and operator norms uniform in p, for all
weights w′; the principal symbol of A is the class of a in wS^m/wρS^(m−1); and wDiff^m_𝒱 consists of the families of
differential operators A_p with (φ_(p,α))_*A_p = Σ_(|β|≤m) w_(p,α)a_(p,α,β)(x)(ρ_(p,α)∂_x)^β, the coefficients bounded in
C^∞ uniformly in p, α and β. Such an A defines maps A_p : w′_pH^((s;k))_(𝒱_p;𝒲_p) → w_pw′_pH^((s−m;k))_(𝒱_p;𝒲_p) bounded
uniformly in p. This is the boundedness of (S5) for the scaled b.g. structure P′ × M, P′ ⊂ P countable, with the cells
{p} × U_(p,α), applied to inputs supported in one slice {p} × M (P′ must be countable for (S1), and the bound does not
depend on P′). The properties of adjoints, compositions, commutators and principal symbols in [Hin26d, Theorem 3.51]
carry over verbatim. P may be replaced by a subset, such as a sequence h_j ↘ 0 (Remark 3.56); the ℬ^(p,×) for different p
may be strongly compatible, though not uniformly in p, so that their Sobolev spaces agree as sets while their norms need
not be uniformly equivalent (Remark 3.57). By Remark 4.9 the variable orders of (S8), with their operators and Sobolev
spaces, generalise to the parameterised setting, the discussion above applying with only notational changes; operators
with phase space weights ((S11)) can be defined there as well (p. 64), and the notational changes for (S10) are left to
the reader (p. 74). Microlocal elliptic estimates and the comparison of different structures are not stated in [Hin26d]
for parameterised structures; [[lem:ii-a-3-1]] gives the uniform versions that are used, and the locality of products
in terms of cut-off symbols ((g) there).
```

C23-1 corrected (section 3); the weights of P × M stated by their definition, not by the sufficient condition after
Definition 3.58 (R-P-S7 m1); Remark 3.57 as printed (n1); the last sentence names (g). The next line, "(S8) [Hin26d,
Definition 4.6 and the paragraph after it, p. 66; ...", is unchanged.

### P-S7-2. chapters/23-s04-compactified.md, the end of sec:ii-a-3: the paragraph after the list kept, lem:ii-a-3-1 added (lines 466–467)

Old (2 lines):

```text
The sharp Gårding inequality is not among these statements and is not used: the real principal type estimate
([[thm:ii-a1-5-4]]) is proved without it.
```

New (145 lines):

```text
The sharp Gårding inequality is not among these statements and is not used: the real principal type estimate
([[thm:ii-a1-5-4]]) is proved without it.

**Lemma {#lem:ii-a-3-1}** (Uniformity in the parameter.) Let (ℬ^(p,×))_(p∈P) be a parameterised scaled b.g. structure on
M ((S7)), with operator and coefficient Lie algebras 𝒱_p and 𝒲_p. For a countable set P′ ⊂ P let N_(P′) := P′ × M, with
the charts {p} × U_(p,α) → (−2, 2)ⁿ, (p, x) ↦ φ_(p,α)(x), and the scalings ρ_(p,α), for p ∈ P′ and α ∈ 𝒜_p. A family
f = (f_p) of functions, symbols or operators restricts to the function, symbol or operator f_(P′) on N_(P′) that is
f_p on {p} × M, an operator acting slice by slice. We write wS^(𝗆,𝗅) := wρ^(−𝗅)S^𝗆, wΨ^(𝗆,𝗅)_𝒱 and
wH^(𝗆,𝗅) := wρ^𝗅H^𝗆 for the classes and spaces of (S8) in the setting of (S7), constant orders included, and take L²,
pairings and adjoints for a family μ of uniformly positive 𝒱_p-densities with bounds uniform in p. A family
E ∈ w⁻¹Ψ^(𝗆,𝗅)_𝒱 is *elliptic* if its principal symbol has a representative e with e⁻¹ ∈ wS^(−𝗆,−𝗅); for variable
orders the space w_pH^(𝗆,𝗅)_(𝒱_p) is normed by ‖u‖² := ‖u‖²_(w_pρ_p^(inf 𝗅)H^(inf 𝗆)) + ‖E_pu‖²_(L²), with a fixed
elliptic family E. All of this applies to ℂ^N-valued functions, the operators being matrices of such families ((S14)).

(a) N_(P′) is a scaled b.g. structure. A weight w of P × M restricts to a weight of N_(P′), and ρ and λ restrict to a
scaling weight and an elliptic weight of it. For s ∈ ℝ and v = (v_p) on N_(P′),

    ‖v‖²_(w_(P′)H^s_𝒱(N_(P′))) = Σ_(p∈P′) ‖v_p‖²_(w_pH^s_(𝒱_p)(M)),

the norms being those of (S3) with a weight family of w that is one of every N_(P′) (such as the suprema of w over the
sets φ_(p,α)⁻¹((−3/2, 3/2)ⁿ), [Hin26d, Lemma 3.5]). The same holds with k further derivatives along a finite set W of
families of vector fields whose restrictions span the coefficient Lie algebras of the N_(P′), and for variable orders,
the space of N_(P′) being normed with E_(P′).

(b) If A ∈ wΨ^(𝗆,𝗅)_𝒱, A = Op(a) + R as in (S7), then A_(P′) lies in w_(P′)Ψ^(𝗆,𝗅)_𝒱(N_(P′)), with principal symbol
the class of a_(P′), for every countable P′ ⊂ P.

(c) A function on P with values in [0, ∞] that is bounded on every countable subset of P is bounded.

(d) Two elliptic families in w⁻¹Ψ^(𝗆,𝗅)_𝒱 give norms of the spaces w_pH^(𝗆,𝗅)_(𝒱_p) that are equivalent uniformly
in p.

(e) (*Elliptic estimate.*) Let A ∈ w′Ψ^(𝗆′,𝗅′)_𝒱 have principal symbol represented by a, let B = Op(b) + R ∈ Ψ^(0,0)_𝒱
as in (S7), and let y_1, y_2, y_3 ∈ S⁰ be real families with y_jy_(j+1) = y_j (j = 1, 2), such that
(1 − y_1)b ∈ ρ^∞S^(−∞), a is invertible where y_3 ≠ 0, and y_3a⁻¹, set to 0 where y_3 = 0, lies in w′⁻¹S^(−𝗆′,−𝗅′).
Then for every weight w, all orders 𝗆, 𝗅 and every N there is C, independent of p, such that for u ∈ w_pH^(−N,−N)_(𝒱_p)

    ‖B_pu‖_(w_pH^(𝗆,𝗅)) ≤ C(‖A_pu‖_(w_pw′_pH^(𝗆−𝗆′,𝗅−𝗅′)) + ‖u‖_(w_pH^(−N,−N))),

the right side being possibly infinite.

(f) (*Comparable scalings.*) Let ℬ̃^(p,×) consist of the charts of ℬ^(p,×) with scalings ρ̃_(p,α) such that
C⁻¹ρ_(p,α,i) ≤ ρ̃_(p,α,i) ≤ Cρ_(p,α,i), with C independent of p, α and i. Then (ℬ̃^(p,×))_(p∈P) is a parameterised scaled
b.g. structure with the same operator and coefficient Lie algebras, scaling weights, elliptic weights, symbol classes,
quantisations and residual families as (ℬ^(p,×))_(p∈P), hence the same classes Ψ_𝒱; and for every weight, all orders
and every k, the spaces of the two structures at p coincide, with norms equivalent uniformly in p (for variable orders
both normed with the same E). For variable orders the classes and spaces do not change, the norms up to equivalence
uniform in p, when ρ is replaced by another scaling weight and w by a weight w̃ with w/w̃ and w̃/w bounded with all their
derivatives along the 𝒲_p uniformly in p, E being replaced by (w/w̃)E.

(g) (*Locality.*) Let A ∈ wΨ^(𝗆,𝗅)_𝒱 and B ∈ w′Ψ^(𝗆′,𝗅′)_𝒱 be Op(a) + R and Op(b) + R′ as in (S7), and let y, y′ ∈ S⁰
be families with yy′ = y′ and ya ∈ wρ^∞S^(−∞). If AB = Op(c) + R″ and BA = Op(c′) + R‴ as in (S7), then y′c and y′c′
lie in ww′ρ^∞S^(−∞).

*Proof.* (a) N_(P′) is a smooth manifold, and its set of charts is countable, as P′ and the 𝒜_p are. Charts in different
slices are disjoint, so the multiplicity bound, the covering, the bounds on the transition maps in (S1) and the scaling
condition hold with the constants of the ℬ^(p,×), which are uniform in p ((S7)). The conditions defining weights, scaling
weights and elliptic weights ((S2), (S8)) are bounds in the charts, uniform over the charts, so they pass to the
restrictions. The cut-offs φ^*χ of (S3) for N_(P′) are those of the slices, so the norm (S3) of N_(P′) is the sum over p
of the norms of the slices; the fields of W act slice by slice, which gives the statement with k derivatives. For
variable orders, E_(P′) is elliptic in the class of N_(P′) by (b), whose proof uses only the constant-order part of (a)
(the symbol e⁻¹ restricts to N_(P′) with the same bounds), so it defines the space of N_(P′) ((S8)), and its norm is the
sum over p of the norms of the slices, by the constant-order case and as L²(μ_(P′)) is the sum of the L²(μ_p).

(b) The seminorms of a_(P′), the constants in the estimates of (S4) over the cells of N_(P′), are at most the suprema
over p of those of the a_p, which are finite ((S7)). The quantisation of (S4) for N_(P′) is a sum over its cells, with
the cut-offs φ_(p,α)^*χ/Σ_β φ_(p,β)^*χ, the sum running over the cells that meet the point, all of which lie in its
slice; so Op_𝒱(a_(P′)) is Op_(𝒱_p)(a_p) on each slice. A weight of N_(P′) extends to a weight of P × M, equal to 1 on the
other slices. By (S7) the norms of the maps R_p and R_p^* of (S4) for this weight are bounded uniformly in p, so by (a)
R_(P′) and its adjoint for μ_(P′) are bounded, and R_(P′) maps C_c^∞(N_(P′)), the families with finitely many members
≠ 0, each in C_c^∞(M), into itself. So R_(P′) is residual, and A_(P′) = Op_𝒱(a_(P′)) + R_(P′) lies in the class of
N_(P′), with principal symbol the class of a_(P′) ((S4), (S8)).

(c) Otherwise there are p_ℓ ∈ P with values at least ℓ for ℓ ∈ ℕ, and the function is unbounded on {p_ℓ : ℓ ∈ ℕ}.

(d) Let E, E′ be elliptic, e as in the definition, and B_0 := Op(e⁻¹) ∈ wΨ^(−𝗆,−𝗅)_𝒱. By (S7) and (S8), B_0E has
principal symbol 1, so R := I − B_0E ∈ Ψ^(−1/2,−1/2)_𝒱 (the principal symbol of (S8) is taken modulo
⋂_δ ρ^(1−2δ)S^(−1+2δ); take δ = ¼). For J ∈ ℕ put B := Σ_(j<J) R^jB_0; then BE = I − R^J, so E′ = E′BE + E′R^J. Here
E′B ∈ Ψ^(0,0)_𝒱 is bounded on L² uniformly in p, and, once J/2 ≥ 1 + sup 𝗆 − inf 𝗆 + sup 𝗅 − inf 𝗅,
E′R^J ∈ w⁻¹Ψ^(𝗆−J/2,𝗅−J/2)_𝒱 maps w_pρ_p^(inf 𝗅)H^(inf 𝗆) into H^(𝗆″,𝗅″) with 𝗆″, 𝗅″ ≥ 1, which lies in ρ_pH¹ ⊂ L²
by the definition of these spaces, uniformly in p ((S7), (S8)). So ‖E′_pu‖ ≤ C(‖E_pu‖ +
‖u‖_(w_pρ_p^(inf 𝗅)H^(inf 𝗆))), and symmetrically.

(e) Fix K ∈ ℕ. For 0 ≤ k ≤ 3K let φ_k ∈ C^∞(ℝ) be real, equal to 1 where |t − 1| ≤ 2^(k−3K−2) and to 0
where |t − 1| ≥ 2^(k−3K−1), and put z_k := φ_k(y_2), a real family in S⁰ (y_2 is real and bounded; the chain rule). Where
y_1 ≠ 0, y_2 = 1; where z_k ≠ 0, |y_2 − 1| < 2^(k−3K−1), so z_(k+1) = 1 for k < 3K; and where z_(3K) ≠ 0, y_2 ≠ 0, so
y_3 = 1. Hence y_1z_0 = y_1, z_kz_(k+1) = z_k and z_(3K)y_3 = z_(3K). Put q := y_3a⁻¹, R_0 := B and r_0 := b; then
(1 − z_0)r_0 = (1 − z_0)(1 − y_1)b ∈ ρ^∞S^(−∞), as (1 − z_0)y_1 = 0. Suppose that, for some j < K, R_j ∈ Ψ^(−j/2,−j/2)_𝒱
has the symbol r_j ((S7)) and (1 − z_(3j))r_j ∈ ρ^∞S^(−∞). Put Q_j := Op(z_(3j+1)r_jq) ∈ w′⁻¹Ψ^(−𝗆′−j/2,−𝗅′−j/2)_𝒱 and
R_(j+1) := R_j − Q_jA. As qa = y_3 (both vanish where y_3 = 0) and z_(3j+1)y_3 = z_(3j+1)z_(3K)y_3 = z_(3j+1) (from
z_k = z_kz_(k+1)), the principal symbol of Q_jA is z_(3j+1)r_j ((S7), (S8)). So R_(j+1) has principal symbol
(1 − z_(3j+1))r_j = (1 − z_(3j+1))(1 − z_(3j))r_j, which lies in ρ^∞S^(−∞), and R_(j+1) ∈ Ψ^(−(j+1)/2,−(j+1)/2)_𝒱, the
principal symbol of (S8) being taken modulo ⋂_δ ρ^(j/2+1−2δ)S^(−j/2−1+2δ) (take δ = ¼). Its symbol r_(j+1) = r_j − c_j,
c_j the symbol of Q_jA, satisfies (1 − z_(3j+3))r_(j+1) ∈ ρ^∞S^(−∞): (1 − z_(3j+3))r_j = (1 − z_(3j+3))(1 − z_(3j))r_j,
and (1 − z_(3j+3))c_j lies in ρ^∞S^(−∞) by (g), whose proof does not use (e), applied with y := 1 − z_(3j+2) and
y′ := 1 − z_(3j+3), as y·z_(3j+1)r_jq = 0 and yy′ = y′. After K steps, B = QA + R_K with
Q := Σ_(j<K) Q_j ∈ w′⁻¹Ψ^(−𝗆′,−𝗅′)_𝒱 and R_K ∈ Ψ^(−K/2,−K/2)_𝒱. By the uniform boundedness of (S7), with (S8),

    ‖B_pu‖_(w_pH^(𝗆,𝗅)) ≤ C‖A_pu‖_(w_pw′_pH^(𝗆−𝗆′,𝗅−𝗅′)) + C‖u‖_(w_pH^(𝗆−K/2,𝗅−K/2)),

with C independent of p, and B_pu lies in w_pH^(𝗆,𝗅) when the right side is finite. If K/2 ≥ N + |sup 𝗆| + |sup 𝗅|,
the last norm is at most C‖u‖_(w_pH^(−N,−N)): for orders 𝗍, 𝗍′ ≤ −N, w_pH^(−N,−N) lies in w_pρ_p^(inf 𝗍′)H^(inf 𝗍),
and the elliptic family that norms w_pH^(𝗍,𝗍′) maps it into H^(𝗋,𝗋′) with 𝗋, 𝗋′ ≥ 0, which lies in
ρ_p^(inf 𝗋′)H^(inf 𝗋) ⊂ L² by the definition of these spaces, uniformly in p ((S7), (S8)). For ℂ^N-valued functions
the construction is the same with matrices, a⁻¹ being the inverse matrix and q a = y_3 Id ((S14)).

(f) The charts are those of the ℬ^(p,×), and |∂^γ(ρ̃_(p,α,i)∂_iτ^j_(βα))| ≤ C²C_γρ̃_(p,β,j), C_γ the constants of the
ℬ^(p,×); so the family is a parameterised scaled b.g. structure. Its coefficient Lie algebras are those of the charts,
and V = Σ V^iρ̃_(p,α,i)∂_i = Σ (V^iρ̃_(p,α,i)/ρ_(p,α,i))ρ_(p,α,i)∂_i gives the same operator Lie algebras. As ρ̄̃_(p,α)
and ρ̄_(p,α) differ by a factor in [C⁻¹, C], the scaling weights are the same. In a chart, a covector is
Σ_i ξ_i dx^i/ρ_(p,α,i) = Σ_i ξ̃_i dx^i/ρ̃_(p,α,i) with ξ = Dξ̃, D := diag(ρ_(p,α,i)/ρ̃_(p,α,i)), whose entries lie in
[C⁻¹, C]; so the local expressions ã(x, ξ̃) = a(x, Dξ̃) of a function on T*M satisfy ∂_x^β∂_ξ̃^γ ã =
D^γ(∂_x^β∂_ξ^γ a)(x, Dξ̃), with C⁻¹⟨ξ̃⟩ ≤ ⟨Dξ̃⟩ ≤ C⟨ξ̃⟩, and the classes S^m and the classes S^m_(1−δ,δ) of (S8) are the
same, with seminorms equivalent uniformly in p; hence so are the elliptic weights and, with the same ρ and λ, the classes
of (S8). In the local quantisation of (S4), the substitution ξ̃ = D⁻¹ξ turns the phase Σ_j (x^j − x′^j)ξ̃_j/ρ̃_j and the
factor dξ̃/(ρ̃_1⋯ρ̃_n) into Σ_j (x^j − x′^j)ξ_j/ρ_j and dξ/(ρ_1⋯ρ_n), and the cut-offs depend on the charts only; so the
quantisations are the same. In (S3), the dilation S̃_(p,α) is D ∘ S_(p,α), so f := (S_(p,α))_*g is replaced by f ∘ D⁻¹,
and ‖f ∘ D⁻¹‖_(H^s(ℝⁿ)) = |det D|^(1/2)‖⟨D⁻¹η⟩^s f̂(η)‖_(L²) lies between C^(∓(n/2+|s|))‖f‖_(H^s(ℝⁿ)); so the norms of
the weighted spaces of the two structures are equivalent uniformly in p, and so are those with k derivatives along W, the
coefficient Lie algebras being the same. A uniformly positive density of one structure is one of the other, the factors
ρ̃_(p,α,1)⋯ρ̃_(p,α,n)/(ρ_(p,α,1)⋯ρ_(p,α,n)) lying in [C^(−n), Cⁿ]; so the conditions of (S4) on residual operators are
the same, with uniformly equivalent bounds, and the classes Ψ_𝒱 coincide. For variable orders the norms of (a) with the
same E differ only in the first term, which is of constant order. Finally, for another scaling weight ρ′ the logarithm
log(ρ′/ρ) and its derivatives along the 𝒲_p are bounded uniformly in p ((S2), the two being equivalent to the same weight
family), so (ρ′/ρ)^(±𝗅) = exp(±𝗅 log(ρ′/ρ)) lie in S⁰ uniformly, and ρ′^(−𝗅)S^𝗆 = ρ^(−𝗅)S^𝗆; the first term of the norm
changes to an equivalent one; and (w/w̃)E is elliptic in w̃⁻¹Ψ^(𝗆,𝗅)_𝒱 with ‖(w/w̃)E_pu‖ and ‖E_pu‖ comparable, as
multiplication by w/w̃ and its inverse is bounded on L² uniformly in p.

(g) Fix a countable P′ ⊂ P and write N := N_(P′). Let 𝔐 be the microlocalisation locus of N and j the continuous
extension of the uniformly continuous functions on ^𝒱T*N to its uniform compactification
((S16) of [[thm:std-sbg-calculus]]); S⁰ consists of such functions ([Hin26d, Lemma 3.24 (1)]), and j(fg) = j(f)j(g),
j(f̄) is the complex conjugate of j(f), and j(ψ(f)) = ψ(j(f)) for real f and ψ ∈ C^∞(ℝ) (ψ(f) lies in S⁰ by the chain
rule), both sides being continuous and equal on the dense subset ^𝒱T*N. By (b), A_(P′), B_(P′) and
(AB)_(P′) = A_(P′)B_(P′) lie in the classes of N, with the symbols a_(P′), b_(P′) and c_(P′). If ϖ ∈ 𝔐 and j(y)(ϖ) ≠ 0,
then ϖ is not in the essential support of a_(P′), which is WF′(A_(P′)) ((S16)); so, by the locality of products of (S5),
with (S8) for variable orders and entrywise for matrices ((S14)), the essential support of c_(P′) lies in {j(y) = 0}. The
set Z := 𝔐 ∩ supp j(y′) is compact and lies in {j(y) = 1}, as j(y′)(1 − j(y)) = j(y′(1 − y)) = 0. Each point of Z has a
χ ∈ S⁰ with j(χ) ≠ 0 there and χc_(P′) ∈ ww′ρ^∞S^(−∞); finitely many, χ_1, …, χ_n, give g := Σ_i |χ_i|² ∈ S⁰ with
j(g) > ε on a neighbourhood O of Z, for some ε > 0. Let ψ ∈ C^∞(ℝ) vanish on (−∞, ε/2] and equal 1 on [ε, ∞), and put
θ := ψ(g) ∈ S⁰. Then y′θc_(P′) = y′(ψ(g)/g)Σ_i χ̄_i(χ_ic_(P′)) lies in ww′ρ^∞S^(−∞), ψ(s)/s being smooth. And
f := y′(1 − θ) ∈ S⁰ has j(f) = 0 on O and off supp j(y′), hence on a neighbourhood of 𝔐 = {j(ρλ) = 0}; so j(ρλ) ≥ δ on
the compact set supp j(f) for some δ > 0, f vanishes where ρλ < δ, and fc_(P′) ∈ ww′ρ^∞S^(−∞), as ρ and λ are bounded
below on the support of f. So y′c_(P′) = y′θc_(P′) + fc_(P′) lies in ww′ρ^∞S^(−∞) on N. Each seminorm of y′c_(P′) is the
supremum over p ∈ P′ of that of y′c_p; so, as a function of p, each seminorm of y′c_p is bounded on every countable
subset of P, hence bounded, by (c). The same argument applies to BA. ∎
```

Against the version 16e6e03f: (b) no longer claims a class with phase space weights (m2); the proof of (a) says that (b)
uses only its constant-order part (n4); (e) is proved by a parametrix from the calculus and (g) (m5, option (b)); (g) is
new (M1 (i)–(ii)), with 𝔐 and j defined in its proof and (S16) of the appendix named. The next lines, a blank line and
"### The e3b-calculus in dimension 4 + 1 {#sec:ii-a-4}", are unchanged. lem:ii-a-3-1 is a new label of chapter 23, cited
from chapters 23 (lem:ii-a-8-4), 27 and 37.

### P-S7-3. chapters/27-s08-iota-normal.md, the paragraph *Phase space.* of sec:ii-f-2-1, and lem:ii-f-2-phase added after it (lines 408–416)

Old (9 lines):

```text
*Phase space.* 𝒫_ι := ^(0ħ,cħ)T̄*_(sf)ι⁺_ħ ∪ ^(0ħ,cħ)S*ι⁺_ħ is the fibre-compactified phase space over sf together with
fibre infinity over all of ι⁺_ħ; it is compact. The part over sf is a manifold with corners whose boundary hypersurfaces
are fibre infinity, F_I (over sf ∩ 0f = {x_I = 0}) and F_K (over sf ∩ tf = {R = 0}); F_I ∩ F_K = ∅. On it we use the
semiclassical 0-covectors ξ dx_I/(hx_I) + η dω/(hx_I) near F_I and the semiclassical cone covectors of [[sec:ii-f-1-3]]
near F_K, over sf ξ_cħ dR/h + η_cħ R dω/h. WF′(A) and Ell(A) ⊂ 𝒫_ι are defined as in [[def:i-b-2-9]], with S^(−K𝐞) in
place of S^(−M𝟏): ϖ ∉ WF′(A) if the symbol of A lies in S^(−K𝐞) on a neighbourhood of ϖ in ^(0ħ,cħ)T̄*ι⁺_ħ for every K.
The principal symbol of A ∈ Ψ^𝐨 is its symbol modulo S^(𝐨−(1−ϵ)𝐞), ϵ > 0 small (S8); over sf at finite frequencies it is
determined by its restriction to 𝒫_ι, as a symbol w_𝐨a with a smooth and vanishing at sf lies in S^(𝐨−(0;0,0,0;1)),
which at finite frequencies is S^(𝐨−𝐞).
```

New (43 lines):

```text
*Phase space.* 𝒫_ι := ^(0ħ,cħ)T̄*_(sf)ι⁺_ħ ∪ ^(0ħ,cħ)S*ι⁺_ħ is the fibre-compactified phase space over sf together with
fibre infinity over all of ι⁺_ħ; here, in the paragraph *Orders and spaces* above and below, ι⁺_ħ and ^(0ħ,cħ)T̄*ι⁺_ħ
include the slice h = 1 (not counted among the four faces, no estimate concerns it), the operators being given for
h ∈ (0, 1], so 𝒫_ι is compact. The part over sf is a manifold with corners whose boundary hypersurfaces are fibre
infinity, F_I (over sf ∩ 0f = {x_I = 0}) and F_K (over sf ∩ tf = {R = 0}); F_I ∩ F_K = ∅. On it we use the semiclassical
0-covectors ξ dx_I/(hx_I) + η dω/(hx_I) near F_I and the semiclassical cone covectors of [[sec:ii-f-1-3]] near F_K,
over sf ξ_cħ dR/h + η_cħ R dω/h. For A ∈ Ψ^𝐨 (the order being the one at which A is considered), WF′(A) and Ell(A) ⊂ 𝒫_ι
are defined as in [[def:i-b-2-9]], with S^(𝐨−K𝐞) in place of S^(−M𝟏): ϖ ∉ WF′(A) if the symbol of A lies in S^(𝐨−K𝐞)
on a neighbourhood of ϖ in ^(0ħ,cħ)T̄*ι⁺_ħ for every K; and ϖ ∈ Ell(A) if ϖ has a neighbourhood U in ^(0ħ,cħ)T̄*ι⁺_ħ such
that a representative a of the principal symbol of A (defined below) is invertible, with |a⁻¹| ≤ Cw_𝐨⁻¹, at the points of
U over h ∈ (0, 1] (at a point over sf this is the condition of [[def:i-b-2-9]], with U inside {h < h_0}; the condition
does not depend on the representative, after U is shrunk: two representatives differ by w_𝐨 times a symbol bounded by
C(⟨ζ⟩⁻¹ρ_sf)^(1−ϵ), which is small near 𝒫_ι). The principal symbol of A ∈ Ψ^𝐨 is its symbol modulo S^(𝐨−(1−ϵ)𝐞), ϵ > 0
small (S8); over sf at finite frequencies it is determined by its restriction to 𝒫_ι, as a symbol w_𝐨a with a smooth and
vanishing at sf lies in S^(𝐨−(0;0,0,0;1)), which at finite frequencies is S^(𝐨−𝐞).

**Lemma {#lem:ii-f-2-phase}** (Smooth functions on the phase space.) A smooth function on ^(0ħ,cħ)T̄*ι⁺_ħ, taken for
h ∈ (0, 1], lies in S⁰, uniformly in h as in (S7); in particular the orders 𝗌 and 𝖻 lie in S⁰.

*Proof.* Write Y := ι⁺_ħ and X := ^(0ħ,cħ)T̄*ι⁺_ħ, the fibre-radial compactification of the dual of the bundle
^(0ħ,cħ)Tι⁺_ħ over Y of which the fields spanning 𝒱_ħ in *The structure* are local frames (with ∂_ω standing for the
coordinate fields of local coordinates ω on the sphere); its fibre over {h} × (ι⁺)° is ^(𝒱_ħ)T*(ι⁺)°. Let f ∈ C^∞(X). On
an open set U ⊂ Y on which such fields form a frame F_1, …, F_4, X is U × B̄⁴, B̄⁴ the radial compactification of ℝ⁴,
whose points ζ ∈ ℝ⁴ are the coordinates of a covector in the dual frame. Finitely many such sets U cover the compact Y,
and with a partition of unity on Y it suffices to take f supported over a compact subset of one U. The fields ⟨ζ⟩∂_(ζ_k)
and the functions ζ_k/⟨ζ⟩ are smooth on B̄⁴, so ∂_ζ^γ is ⟨ζ⟩^(−|γ|) times a combination, with coefficients smooth on B̄⁴,
of products of at most |γ| of the fields ⟨ζ⟩∂_(ζ_k); hence |V_1⋯V_k∂_ζ^γ f| ≤ C⟨ζ⟩^(−|γ|) for smooth vector fields
V_1, …, V_k on U, acting at fixed ζ.

The fields ρ_K∂_(ρ_K) and ∂_ω near ι⁺ ∩ K⁺, x_I∂_(x_I) and ∂_ω near ι⁺ ∩ ℐ⁺, and coordinate fields in between, which span
the coefficient Lie algebra C^∞_b𝒱_b(ι⁺) over C^∞_b(ι⁺), are, at fixed h, smooth vector fields on Y, as vector fields
tangent to {h = 0} and to the centre {0} × (ι⁺ ∩ K⁺) of the blow-up lift to smooth ones (near sf ∩ tf, R∂_R at fixed h is
R∂_R − ĥ∂_ĥ in the coordinates ĥ, R). Consider a cell of the structure at h, with chart coordinates x and scalings ρ_i.
The fields ∂_(x^i) lie in the coefficient Lie algebra, so they are combinations of the fields just listed with
coefficients bounded with all their derivatives ∂_x, uniformly in h and in the cell. The fields ρ_i∂_(x^i) span 𝒱_ħ
((S1)), and so do F_1, …, F_4, over C^∞_b(ι⁺) uniformly in h (*The structure*); so ρ_i∂_(x^i) = Σ_k D_(ik)F_k with D and
D⁻¹ bounded with all their derivatives ∂_x, uniformly. The fibre coordinates ξ of the chart, ξ_i the value of a covector
on ρ_i∂_(x^i), are then ξ = Dζ, and C⁻¹⟨ζ⟩ ≤ ⟨ξ⟩ ≤ C⟨ζ⟩. So f is f̃(x, ξ) = f(x, D(x)⁻¹ξ) in the chart, and, by induction
on |β| + |γ|, ∂_x^β∂_ξ^γ f̃ is a finite sum of terms c(x)ξ^μ(V_1⋯V_k∂_ζ^ν f)(x, D(x)⁻¹ξ), with c bounded uniformly, the
V_l among the fields above and |ν| ≥ |μ| + |γ|: a derivative ∂_(ξ_l) lowers |μ| or, through the entries of D⁻¹,
raises |ν| by one, and a derivative ∂_(x^i) differentiates c, adds a field V_l, or adds a factor ((∂_(x^i)D⁻¹)ξ)_k with a
derivative ∂_(ζ_k). Each term is bounded by C⟨ξ⟩^(|μ|−|ν|) ≤ C⟨ξ⟩^(−|γ|), uniformly in h and in the cell; so f ∈ S⁰. The
orders are smooth on X (*Orders and spaces*). ∎
```

Changes: the slice h = 1 is included (compactness) and is not counted among the faces (n3); WF′ is defined with the
weighted classes S^(𝐨−K𝐞) (M1 (iii)); Ell(A) is spelled out, with the independence of the representative (n3);
lem:ii-f-2-phase is added after the paragraph and proved (n5). The next lines, a blank line and "**Lemma
{#lem:ii-f-2-2}** (The calculus.) Uniformly for h ∈ (0, 1]:", are unchanged. lem:ii-f-2-phase is a new label of chapter
27; assembly numbers it Lemma 18.7, so the numbers of the later lemmas of that chapter increase by one.

### P-S7-4. chapters/27-s08-iota-normal.md, the proof of lem:ii-f-2-2 (b), first two lines (lines 450–451)

Old (2 lines):

```text
(b) is (S5) and (S8): the principal symbol is taken modulo ⋂_δ ρ̄^(−𝖻+1−2δ)S^(𝗌−1+2δ), and σ(i[A_1, A_2]) =
H_(σ(A_1))σ(A_2). Adjoints with respect to μ_b and 𝔢 differ from those of (S5) (the 𝒱_ħ-density and the Euclidean inner
```

New (3 lines):

```text
(b) is (S5) and (S8), uniformly in h by (S7): the principal symbol is taken modulo ⋂_δ ρ̄^(−𝖻+1−2δ)S^(𝗌−1+2δ), and
σ(i[A_1, A_2]) = H_(σ(A_1))σ(A_2). Adjoints with respect to μ_b and 𝔢 differ from those of (S5) (the 𝒱_ħ-density and
the Euclidean inner
```

Adds "uniformly in h by (S7)" and rewraps. The next line, "product) by conjugation with the weight ρ_sf⁻⁴ρ_0f⁻³ ...", is
unchanged.

### P-S7-5. chapters/27-s08-iota-normal.md, the proof of lem:ii-f-2-2 (c) (lines 460–461)

Old (2 lines):

```text
(c) is the microlocal elliptic estimate of (S5), with (S8) for variable orders, localised by the composition calculus as
in the proof of [[prop:i-b-2-10]].
```

New (13 lines):

```text
(c) Let a and g represent the principal symbols of A and G, and let b be the symbol of B ((S7)); by (b), GA ∈ Ψ^(𝐦′) has
principal symbol ga. Let X := ^(0ħ,cħ)T̄*ι⁺_ħ, which is compact; smooth functions on X lie in S⁰ ([[lem:ii-f-2-phase]]).
WF′(B) is a closed subset of the compact set 𝒫_ι, so finitely many of the neighbourhoods in the definitions of Ell(A) and
Ell(G) cover it, and there are an open set O ⊂ X containing WF′(B) and C such that ga is invertible
with |(ga)⁻¹| ≤ Cw_(𝐦′)⁻¹ at the points of O over h ∈ (0, 1]. Choose real y_1, y_2, y_3 ∈ C^∞(X) with y_1 = 1 near
WF′(B), y_(j+1) = 1 near supp y_j and supp y_3 ⊂ O. Then y_3(ga)⁻¹ ∈ S^(−𝐦′), by (d) ([[lem:i-b-2-2]] (e)). The
compact set supp(1 − y_1) is covered by finitely many open sets V_i such that z b ∈ S^(−K𝐞) for every K and every smooth
function z supported in V_i: neighbourhoods of points of 𝒫_ι outside WF′(B), by the definition of WF′, and sets
{ρ_sf > δ, |ζ| < C_0} with δ > 0, which cover X ∖ 𝒫_ι, by (f) (i). With a partition of unity subordinate to the V_i,
(1 − y_1)b ∈ S^(−K𝐞) for every K, that is, (1 − y_1)b ∈ ρ̄^∞S^(−∞), as ρ̄ ≍ ρ_sf ([[lem:ii-f-2-1]] (a)). So
[[lem:ii-a-3-1]] (e) applies to GA, B and the y_j, in the spaces of (a) with the shift of the density made there; it
gives (c) with C independent of h, the remainder ‖u‖_(𝐨−K𝐞) bounding the remainder there once N is large, by (a) applied
to the identity.
```

The next lines, a blank line and "(d) The proof of [[lem:i-b-2-2]] uses only ...", are unchanged. Against 16e6e03f: the
smooth functions on X are in S⁰ by lem:ii-f-2-phase (n5). Inputs: section 6.2.

### P-S7-6. chapters/37-s18-augmented.md, the proof of lem:iii-h1-3-1, first sentence (lines 822–824)

Old (3 lines):

```text
*Proof.* Write β := α_sf + 1. The transform û_hi is supported in |σ| ≥ c/2, and on c/2 ≤ |σ| ≤ 1 the sc-b norm at σ
and the semiclassical norm at the semiclassical parameter |σ|⁻¹ are both equivalent to the fixed norm, uniformly on this
compact set (the parameterised calculus, (S7) in [[sec:ii-a-3]]). So by [[lem:ii-a-5-2]],
```

New (20 lines):

```text
*Proof.* Write β := α_sf + 1. The transform û_hi is supported in |σ| ≥ c/2, and on c/2 ≤ |σ| ≤ 1 the sc-b norm at σ and
the semiclassical norm at the semiclassical parameter h := |σ|⁻¹ ∈ [1, 2/c] (given there by the same formula, the space
being that of the spectral structure at σ) are both equivalent to the fixed norm, the norm with the same orders for the
structure C^∞_b𝒱_sc(X̃) of [[sec:ii-a-5-1]] (2), the spectral structure at |σ| = 1, uniformly on this compact set.
Indeed, by the definitions in [[sec:ii-a-5-1]] (2)–(4), the three are norms of spaces w_∗ϱ^(𝗌_σ)H^(𝗌_σ), of the
variable orders (𝗌_σ, 𝗌_σ) of (S8) at a scaling weight ϱ, with k − j_1 − j_2 further b-derivatives, where ρ := ⟨x⟩⁻¹,
with w_∗ = ρ_scf^βρ_tf^β and ϱ = ρ_scf for the sc-b norm, w_∗ = ρ^β and ϱ = hρ for the semiclassical one, and w_∗ = ρ^β
and ϱ = ρ for the fixed one. The spectral structures at σ and at |σ| = 1 have the same cells, with scalings
(1 + |σ|⟨x⟩)⁻¹ and (1 + ⟨x⟩)⁻¹ whose ratio lies in [1, 2/c]. For c/2 ≤ |σ| ≤ 1, ρ_scf⟨x⟩ = ⟨x⟩/(1 + |σ|⟨x⟩) and
hρ⟨x⟩ = 1/|σ| lie in [½, 2/c], ρ_tf lies between positive constants, and the logarithms of these functions have bounded
b-derivatives, all uniformly in σ; so ρ_scf, hρ and ρ are scaling weights of both structures, and ρ_scf^βρ_tf^β and ρ^β
are equivalent weights, uniformly in σ. The orders 𝗌_σ = S_(z_0)(·, ·/|σ|) ([[def:iii-h1-1-1]]) form a family bounded in
S⁰, |σ| ranging over a compact subset of (0, ∞). So [[lem:ii-a-3-1]] (f), with (d) there for the choice of the elliptic
families, gives the uniform equivalence. The same holds for 1 ≤ |σ| ≤ C_0, the scalings (1 + |σ|⟨x⟩)⁻¹ then lying within
the factor C_0 of (1 + ⟨x⟩)⁻¹; and, uniformly for c/2 ≤ |σ| ≤ C_0, the fixed norm is equivalent to the norm of the same
structure with the orders (s_c, 𝗋_σ + β), in which [[thm:i-a-7-2]] is applied below. Indeed 𝗌_σ − s_c vanishes at
fibre infinity ((C1)) and 𝗌_σ − 𝗋_σ over ∂X, so λ^(s_c−𝗌_σ), ρ^(𝗋_σ−𝗌_σ) and their inverses are bounded in S⁰ (each
exponent is λ, resp. ρ, times a function bounded in S⁰, and λ log λ and ρ log ρ are bounded with their derivatives); so
the two pairs of orders define the same classes, and the first terms of the two norms ((S8)) are bounded by each other
modulo the second, as in the proof of [[lem:ii-a-3-1]] (d). So by [[lem:ii-a-5-2]],
```

Against 16e6e03f: the weights written w_∗ (n2); the extension to 1 ≤ |σ| ≤ C_0 and the identification with the orders
(s_c, 𝗋_σ + β) added (m3). The next lines, a blank line and the display "‖u_hi‖² ∼ Σ_(j_1+j_2≤k) ...", are unchanged.

### P-S7-7. chapters/95-standard-results.md, the header of thm:std-sbg-calculus, second line (line 914)

Old (1 line):

```text
Propositions 2.3–4.22, Remarks 3.13–3.56, Theorems 3.21–3.52, footnote 13, (1.6), (2.3), (2.5), (3.2), (3.19), (3.26),
```

New (1 line):

```text
Propositions 2.3–4.22, Remarks 3.13–4.9, Theorems 3.21–3.52, footnote 13, (1.6), (2.3), (2.5), (3.2), (3.19), (3.26),
```

Remarks 3.57 and 4.9 are now quoted; the page range pp. 2–75 already contains pp. 64, 67 and 74.

### P-S7-8. chapters/95-standard-results.md, the header of the appendix entry (S7) (lines 956–957)

Old (2 lines):

```text
(S7) Parameterised structures [Hin26d, Definition 1.9, p. 9; p. 58 and Remark 3.56, p. 58; Definitions 3.58 and 3.59 and
the text after them, with footnote 13, p. 59]. Definition 1.9 defines a parameterized scaled bounded geometry structure
```

New (3 lines):

```text
(S7) Parameterised structures [Hin26d, Definition 1.9, p. 9; p. 58 and Remark 3.56, p. 58; Remark 3.57, pp. 58–59;
Definitions 3.58 and 3.59 and the text after them, with footnote 13, p. 59; p. 64; Remark 4.9, p. 67; p. 74].
Definition 1.9 defines a parameterized scaled bounded geometry structure
```

The next line, "on (M, P) as a collection {𝓑_(p,×)} of scaled b.g. structures ...", is unchanged.

### P-S7-9. chapters/95-standard-results.md, the end of the appendix entry (S7) (line 989)

Old (1 line):

```text
a_(p,α,β) are uniformly (in p ∈ P, α ∈ 𝒜_p, β ∈ ℕ^n_0) bounded."
```

New (12 lines):

```text
a_(p,α,β) are uniformly (in p ∈ P, α ∈ 𝒜_p, β ∈ ℕ^n_0) bounded." Remark 3.57 (Compatibility of different scaled b.g.
structures): "In applications, two scaled b.g. structures 𝓑_(p,×) and 𝓑_(p′,×) for different values of p, p′ ∈ P are
often strongly compatible, though not uniformly so in p and p′ ∈ P. (This implies, for example, the equality of all
Sobolev spaces H^s_(𝒱_p)(M) as sets, but still allows for the norms to not be uniformly equivalent as p varies.) Since
imposing this condition would not lead to any simplifications, we do not do this here." On p. 64: "Operators with phase
space weights can also be defined in the parameterized scaled b.g. setting. … We leave the details to the interested
reader." Remark 4.9 (Parameterized version), p. 67, in the section on variable orders ((S8)): "The discussion in the
present section generalizes to variable order symbols, ps.d.o.s, and Sobolev spaces depending on a parameter; indeed,
the discussion in §3.7 applies with only straightforward notational modifications. For example, in a semiclassical
bounded geometry setting, one can work with variable semiclassical orders." On p. 74, for the commutator 𝒲-vector
fields of (S10): "We only discuss the scaled b.g. setting, and leave the purely notational modifications for
parameterized settings to the reader."
```

The next lines, a blank line and "(S8) Variable orders [Hin26d, Definition 4.6, p. 66]: ...", are unchanged.

### P-S7-10. chapters/95-standard-results.md, the end of the appendix entry (S16) (line 1130)

Old (1 line):

```text
WF^(m−m′,ww′,l)_𝒱(Au) ⊂ WF^(m,w,l)_𝒱(u) ∩ WF′^(w′)_𝒱(A). …"
```

New (6 lines):

```text
WF^(m−m′,ww′,l)_𝒱(Au) ⊂ WF^(m,w,l)_𝒱(u) ∩ WF′^(w′)_𝒱(A). (3) (Microlocal elliptic regularity.) If WF′_𝒱(B) ⊂
Ell^(m,w)_𝒱(A), then for any N there exists C_N so that ‖Bu‖_(wρ^lH^m_𝒱(M)) ≤ C_N(‖Au‖_(ww′ρ^lH^(m−m′)_𝒱(M)) +
‖u‖_(wρ^(−N)H^(−N)_𝒱))." (In (3) the superscripts of the elliptic set stand for those of A, m′ and w′.) The elliptic set
is that of Definition 3.43, "Ell^(m,w)_𝒱(A) := Ell^(wλ^(−m))_𝔐(σ^(m,w)_𝒱(A))", where Definition 3.25 reads: "Let
w ∈ C^∞(𝒱T*M) be a weight on (𝒱T*M, 𝓑*). For a symbol a ∈ wS⁰(𝒱T*M), we define its elliptic set by
Ell^w_𝔐(a) := {ϖ ∈ 𝔐 : ∃ b ∈ w⁻¹S⁰(𝒱T*M), ϖ ∉ supp_(u𝒱T*M)(ab − 1)} ⊂ 𝔐."
```

The "…" that ended the quotation of Proposition 3.55 is replaced by its part (3); the Ell definitions of Definitions
3.25 and 3.43 follow. The next lines, a blank line and "The numbers and pages in (S1)–(S16) are those of arXiv version 1
...", are unchanged. (S5) of sec:ii-a-3 cites Proposition 3.55; lem:ii-a-3-1 (g) uses the locus, j and the essential
support already quoted in (S16).

### P-S7-11. chapters/95-standard-results.md, the numbering note after (S16) (lines 1135–1138)

Old (4 lines):

```text
Lemma 3.36 to Definition 3.61 each number is increased by one, so that Proposition 3.39, Lemma 3.42, Definition 3.43,
Theorems 3.44, 3.51 and 3.52, Remarks 3.46–3.48, Definition 3.54, Proposition 3.55, Remark 3.56 and Definitions 3.58 and
3.59 are Proposition 3.40, Lemma 3.43, Definition 3.44, Theorems 3.45, 3.52 and 3.53, Remarks 3.47–3.49,
Definition 3.55, Proposition 3.56, Remark 3.57 and Definitions 3.59 and 3.60 there; footnote 13 is footnote 22; and in
```

New (5 lines):

```text
Lemma 3.36 to Definition 3.61 each number is increased by one, so that Proposition 3.39, Lemma 3.42, Definition 3.43,
Theorems 3.44, 3.51 and 3.52, Remarks 3.46–3.48, Definition 3.54, Proposition 3.55, Remarks 3.56 and 3.57 and
Definitions 3.58 and 3.59 are Proposition 3.40, Lemma 3.43, Definition 3.44, Theorems 3.45, 3.52 and 3.53, Remarks
3.47–3.49, Definition 3.55, Proposition 3.56, Remarks 3.57 and 3.58 and Definitions 3.59 and 3.60 there; footnote 13 is
footnote 22; and in
```

Adds Remark 3.57 (Remark 3.58 in the published version) by the note's own rule. The next line, "Section 4, Proposition
4.2 and Definition 4.6 keep their numbers, ...", is unchanged. The published number of Remark 4.9 is not added (section
6.5).

### P-S7-12. chapters/23-s04-compactified.md, the proof of lem:ii-a-8-4 (d), first three lines (lines 1052–1054)

Old (3 lines):

```text
(d) By [[lem:ii-a-4-1]] (with (S8) for variable orders), an elliptic Λ ∈ C^∞_b Ψ^(𝗌+1)_e3b is Σ_(l=0)^N Λ_lV_l with
Λ_l ∈ C^∞_b Ψ^𝗌_e3b. Microlocal elliptic regularity (S5), with I in place of B, gives
‖v‖_(H^(𝗌+1)) ≤ C(‖Λv‖_(L²) + ‖v‖_(H^(−N))) ≤ C Σ_l ‖V_lv‖_(H^𝗌). Apply this to v = V^J u, |J| ≤ k − 1, and sum, using
```

New (5 lines):

```text
(d) By [[lem:ii-a-4-1]] (with (S8) for variable orders), an elliptic Λ ∈ C^∞_b Ψ^(𝗌+1)_e3b is Σ_(l=0)^N Λ_lV_l with
Λ_l ∈ C^∞_b Ψ^𝗌_e3b; we take Λ elliptic in the sense of [[lem:ii-a-3-1]], for instance Op(λ^(−𝗌−1)), λ the elliptic
weight of (S8). The elliptic estimate of [[lem:ii-a-3-1]] (e), for this single structure (P a point) with B = I and
y_1 = y_2 = y_3 = 1, gives ‖v‖_(H^(𝗌+1)) ≤ C(‖Λv‖_(L²) + ‖v‖_(H^(−N))) ≤ C Σ_l ‖V_lv‖_(H^𝗌), the remainder there being at
most C‖v‖_(H^(−N)). Apply this to v = V^J u, |J| ≤ k − 1, and sum, using
```

The elliptic estimate is cited from lem:ii-a-3-1 (e) instead of (S5) with (S8) (m5); Λ is taken elliptic in that lemma's
sense. The next line, "[[eq:ii-a-8-1]]. Iterating gives the second claim. ...", is unchanged.

### P-S7-13. chapters/27-s08-iota-normal.md, the proof of lem:ii-f-2-2 (a), first two lines (lines 444–445)

Old (2 lines):

```text
*Proof.* (a) is (S5) with (S7), (S8) and (S11), the weights by [[lem:ii-f-2-1]] (b) and the decay order at ρ̄ ≍ ρ_sf by
[[lem:ii-f-2-1]] (a). The density μ_b is ρ̄⁴ρ_0f³ times a uniformly positive 𝒱_ħ-density: near cf the scalings multiply
```

New (5 lines):

```text
*Proof.* (a) is (S5) with (S7), (S8) and (S11), the weights by [[lem:ii-f-2-1]] (b) and the decay order at ρ̄ ≍ ρ_sf by
[[lem:ii-f-2-1]] (a). The bound by a seminorm holds on each N_(P′) of [[lem:ii-a-3-1]] ((S5), and (b) there), and its
constant and seminorm can be taken independent of P′: otherwise, with q_1 ≤ q_2 ≤ ⋯ the seminorms, there are h_k and
A_k with ‖(A_k)_(h_k)‖ > kq_k(A_k) for every k, which contradicts the bound on N_(P′) for P′ := {h_k : k ∈ ℕ}. The
density μ_b is ρ̄⁴ρ_0f³ times a uniformly positive 𝒱_ħ-density: near cf the scalings multiply
```

The bound by a seminorm, uniformly in h, by a diagonal argument (m4). The fifth new line is the tail of the old line
445; the next line, "to ρ̄⁴ up to bounded factors, as dim ι⁺ = 4, ...", is unchanged.

### P-S7-14. chapters/27-s08-iota-normal.md, lem:ii-f-2-2: (h) added after (g) (lines 441–442)

Old (2 lines):

```text
(g) (Density.) For fixed h > 0, z and orders 𝐨, C^∞_c((ι⁺)°) is dense in {u ∈ H^𝐨 : P_(ι,h,z)u ∈ H^(𝐨−𝐦+𝐞)} with the
graph norm, and likewise for P*_(ι,h,z) and the orders −𝐨 + 𝐦 − 𝐞.
```

New (5 lines):

```text
(g) (Density.) For fixed h > 0, z and orders 𝐨, C^∞_c((ι⁺)°) is dense in {u ∈ H^𝐨 : P_(ι,h,z)u ∈ H^(𝐨−𝐦+𝐞)} with the
graph norm, and likewise for P*_(ι,h,z) and the orders −𝐨 + 𝐦 − 𝐞.

(h) (Locality.) WF′(AB) ⊂ WF′(A) ∩ WF′(B) for A ∈ Ψ^𝐨 and B ∈ Ψ^(𝐨′); and if A ∈ Ψ^𝐨 and WF′(A) = ∅, then
A ∈ Ψ^(𝐨−K𝐞) for every K.
```

The two old lines are kept; (h) (locality) follows (M1 (iv)). The next lines, a blank line and "*Proof.* (a) is (S5)
with ..." (replaced by P-S7-13), follow.

### P-S7-15. chapters/27-s08-iota-normal.md, the end of the proof of lem:ii-f-2-2: the proof of (h) added (lines 489–491)

Old (3 lines):

```text
bounded coefficients. Then u_(j,ϵ) := χ_jJ_ϵu ∈ C^∞_c((ι⁺)°) converges to u in the graph norm as ϵ → 0 and then j → ∞,
as in the proof of [[lem:i-b-3-1]]; the weights x_I^aρ_K^c commute with χ_j and conjugate J_ϵ into a family with the
same properties. ∎
```

New (11 lines):

```text
bounded coefficients. Then u_(j,ϵ) := χ_jJ_ϵu ∈ C^∞_c((ι⁺)°) converges to u in the graph norm as ϵ → 0 and then j → ∞,
as in the proof of [[lem:i-b-3-1]]; the weights x_I^aρ_K^c commute with χ_j and conjugate J_ϵ into a family with the
same properties.

(h) Let ϖ ∈ 𝒫_ι ∖ WF′(A), let a be the symbol of A, and let U be a neighbourhood of ϖ in X (as in the proof of (c)) on
which a lies in S^(𝐨−K𝐞) for every K. Choose y, y′ ∈ C^∞(X) supported in U with y = 1 near supp y′ and y′ = 1 near ϖ.
They lie in S⁰ ([[lem:ii-f-2-phase]]), and ya ∈ S^(𝐨−K𝐞) for every K, that is, ya ∈ wρ̄^∞S^(−∞) with w the weight of 𝐨 at
0f, cf and tf ([[lem:ii-f-2-1]] (a)). By [[lem:ii-a-3-1]] (g) the symbols c and c′ of AB and BA satisfy
y′c, y′c′ ∈ S^(𝐨+𝐨′−K𝐞) for every K, so ϖ lies in neither WF′(AB) nor WF′(BA); with A and B exchanged, this gives the
first statement. If WF′(A) = ∅, the partition of unity of the proof of (c), with WF′(A) in place of WF′(B) and 0 in place
of y_1, gives a ∈ S^(𝐨−K𝐞) for every K, so A ∈ Ψ^(𝐨−K𝐞). ∎
```

The ∎ moves to the end of the proof of (h) (M1 (iv)); the cut-offs are in S⁰ by lem:ii-f-2-phase. The next lines, a
blank line and "#### The positive commutator scheme {#sec:ii-f-2-2}", are unchanged.

### P-S7-16. chapters/27-s08-iota-normal.md, the proof of prop:ii-f-2-3, first five lines (lines 552–556)

Old (5 lines):

```text
*Proof.* The proofs in [[ch:s02]] use of the calculus: the mapping property ([[prop:i-b-2-8]]), the composition and
adjoint theorems with the principal symbols of products, adjoints and commutators ([[thm:i-b-2-4]], [[thm:i-b-2-5]] and
[[eq:i-b-2-5]]), the elliptic estimate ([[prop:i-b-2-10]]), the symbol properties of [[lem:i-b-2-2]], the square roots
of [[lem:i-b-2-11]] and [[lem:i-b-2-12]], and the L² pairing of H^𝐨 with H^(−𝐨). These are [[lem:ii-f-2-2]] (a)–(e)
here, the pairing being (S3) and (S11) with the weight shift of the proof of [[lem:ii-f-2-2]] (a). [[lem:i-b-4-3]] and
```

New (7 lines):

```text
*Proof.* The proofs in [[ch:s02]] use of the calculus: the mapping property ([[prop:i-b-2-8]]), the composition and
adjoint theorems with the principal symbols of products, adjoints and commutators ([[thm:i-b-2-4]], [[thm:i-b-2-5]] and
[[eq:i-b-2-5]]), the locality of products ((iv) of the consequences of [[thm:i-b-2-5]], and WF′_h(AB) ⊂ WF′_h(A) ∩
WF′_h(B) after [[def:i-b-2-9]]) with the fact that an operator whose WF′_h is empty is residual, the elliptic estimate
([[prop:i-b-2-10]]), the symbol properties of [[lem:i-b-2-2]], the square roots of [[lem:i-b-2-11]] and
[[lem:i-b-2-12]], and the L² pairing of H^𝐨 with H^(−𝐨). These are [[lem:ii-f-2-2]] (a)–(e) and (h) here, the pairing
being (S3) and (S11) with the weight shift of the proof of [[lem:ii-f-2-2]] (a). [[lem:i-b-4-3]] and
```

The locality of products added to the list, supplied by lem:ii-f-2-2 (h) (M1 (v)). The first two lines are unchanged.
The next line, "[[lem:i-b-4-4]] are statements about vector fields ...", is unchanged.

### P-S7-17. chapters/27-s08-iota-normal.md, the proof of lem:ii-f-5-6 (a), Step 1 (lines 1432–1440)

Old (9 lines):

```text
*Proof.* (a) *Step 1: the elliptic estimate.* N⁰(σ) is elliptic in x_I²ρ_K⁻²Diff²_(0,b) ([[sec:ii-f-1-3]]), so
microlocal elliptic regularity in the calculus of the structure of [[sec:ii-a-6-2]] ((S5) of [[sec:ii-a-3]], with (S8)
for variable orders, and B = I) gives, as in [[lem:ii-a-8-4]] (c),

    ‖u‖_(𝒳^𝗌) ≤ C(‖N⁰(σ)u‖_(𝒴^(𝗌−2)) + ‖u‖_(𝒳^(−M)))                                                     {#eq:ii-f-5-8}

(the remainder of (S5) is bounded by ‖u‖_(𝒳^(−M))). Let χ ∈ C^∞_c([0, 2)) equal 1 on [0, 1], read as χ(R), and χ_1(x_I)
the same function of x_I. Since 1 − χ(R) is supported in {R ≥ 1} = {x_I ≤ 1}, where χ_1(x_I) = 1, ‖u‖_(𝒳^(−M)) ≤
‖χ(R)u‖_(𝒳^(−M)) + C‖χ_1(x_I)u‖_(𝒳^(−M)).
```

New (13 lines):

```text
*Proof.* (a) *Step 1: the elliptic estimate.* N⁰(σ) is elliptic in x_I²ρ_K⁻²Diff²_(0,b): its principal symbol in the
structure of [[sec:ii-a-6-2]] at this σ is p Id with |p| ≥ cx_I²ρ_K⁻²λ⁻² where λ ≤ δ, for some c, δ > 0, λ being the
elliptic weight of (S8) of [[sec:ii-a-3]] ([[sec:ii-f-1-3]], [[eq:ii-f-1-10]]). Let ψ_1, ψ_2, ψ_3 ∈ C^∞(ℝ) equal
1 near 0, with ψ_(j+1) = 1 near supp ψ_j and supp ψ_3 ⊂ (−δ, δ), and put y_j := ψ_j(λ) ∈ S⁰. Then 1 − y_1 vanishes where
λ is small, so it lies in ρ̄^∞S^(−∞), the scaling weight ρ̄ being bounded below at fixed σ; and y_3p⁻¹ ∈ x_I⁻²ρ_K²S^(−2),
by the chain rule. So the elliptic estimate of [[lem:ii-a-3-1]] (e), for this single structure with B = I and these
y_j, gives

    ‖u‖_(𝒳^𝗌) ≤ C(‖N⁰(σ)u‖_(𝒴^(𝗌−2)) + ‖u‖_(𝒳^(−M)))                                                     {#eq:ii-f-5-8}

(the remainder there, with N = M, is bounded by ‖u‖_(𝒳^(−M))). Let χ ∈ C^∞_c([0, 2)) equal 1 on [0, 1], read as χ(R), and
χ_1(x_I) the same function of x_I. Since 1 − χ(R) is supported in {R ≥ 1} = {x_I ≤ 1}, where χ_1(x_I) = 1, ‖u‖_(𝒳^(−M)) ≤
‖χ(R)u‖_(𝒳^(−M)) + C‖χ_1(x_I)u‖_(𝒳^(−M)).
```

The elliptic estimate is cited from lem:ii-a-3-1 (e) instead of (S5) with (S8) (m5), with cut-offs in the elliptic
weight; the display and its label are unchanged. The next lines, a blank line and "*Step 2: near ι⁺ ∩ K⁺.* ...", are
unchanged.

### P-S7-18. chapters/33-s14-constraint-damping.md, the proof of lem:iv5-calc-structure (b), last two lines (lines 1515–1516)

Old (2 lines):

```text
and the charts do not depend on h, the ratios of the weight across overlapping charts of the parameterised structure are
those for ℬ, which are bounded ((S7), the sufficient condition after [Hin26d, Definition 3.58]).
```

New (2 lines):

```text
and the charts do not depend on h, the bounds of (S2) for the parameterised structure are those for ℬ, uniformly in h,
so these are weights of the parameterised structure ((S7)).
```

The weights by the definition of (S7), not by the sufficient condition after [Hin26d, Definition 3.58] (m1). The next
lines, a blank line and "(c) On U_((2),i,±,j,k,m), ...", are unchanged.

## 6. Notes for the readers (not chapter text)

### 6.1 The inputs of lem:ii-a-3-1, part by part

- (a) The axioms of (S1) for P′ × M are those of the slices, since charts of different slices are disjoint; the
  countability of P′ is the point of footnote 13. The norm identity is (3.14) of [Hin26d] (rem:std-sbg-sobolev), whose
  cut-offs φ_α^*χ are unnormalised and so are those of the slices. For variable orders, the space of N_(P′) is that of
  Definition 4.6 for the elliptic operator E_(P′), with the graph norm; that E_(P′) is elliptic uses (b), whose proof
  uses only the constant-order part of (a).
- (b) Definitions 3.8, 3.31, 3.34 and 3.43 for N_(P′). The normalised cut-offs of Op_𝒱 sum over the cells meeting a
  point, all in its slice. A weight of N_(P′) extends by 1 to a weight of P × M, so the uniformity of Definition 3.59,
  "for all weights w′", gives the residual bounds on N_(P′). For variable orders the classes of the parameterised
  setting are those of Definitions 3.58–3.59 with the symbol classes of (S8) (Remark 4.9). No class with phase space
  weights is claimed: [Hin26d, p. 64] leaves its parameterised definition to the reader, and no use needs one.
- (c) If unbounded, there is a sequence on which the function exceeds 1, 2, 3, …; it is used as in the proof of
  prop:np-10-65-a.
- (d) Parametrix by a finite Neumann series, B_0E = I − R with R of order (−½, −½), using only (S7) with Remark 4.9
  (compositions, principal symbols, boundedness). No principal symbol of a remainder beyond the first step is needed.
- (e) A finite parametrix, as in lem:ii-a-8-4 (b)–(c), with the cut-offs z_k = φ_k(y_2), 0 ≤ k ≤ 3K, nested so that
  y_1z_0 = y_1, z_kz_(k+1) = z_k and z_(3K)y_3 = z_(3K). Each step Q_j := Op(z_(3j+1)r_jq), q = y_3a⁻¹, removes the
  principal symbol of R_j modulo a residual symbol, gaining ½ in both orders (the principal symbol of (S8) being taken
  modulo ⋂_δ ρ^(1−2δ)S^(−1+2δ) relative to the order, δ = ¼); that the new remainder's full symbol is again residual off
  z_(3j+3) = 1 is (g), applied with y = 1 − z_(3j+2) and y′ = 1 − z_(3j+3). The estimate then follows from the uniform
  boundedness of Q and R_K, and the remainder norm of order −K/2 is bounded by that of order (−N, −N) by the
  definition of the variable-order spaces. For systems the same construction runs with matrices ((S14)). Proposition
  3.55 (3) is not used, so (e) holds for variable orders, the (S8) classes and systems without a reading of (S8).
- (f) Elementary: the same charts and comparable scalings give the same Lie algebras and the same symbol classes (a
  diagonal rescaling D of the fibre variables); the same quantisations (the substitution ξ̃ = D⁻¹ξ in (3.26)); norms
  of (3.14) differing by a dilation D with ‖f ∘ D⁻¹‖_(H^s) comparable to ‖f‖_(H^s); comparable uniformly positive
  densities, hence the same residual classes. The replacement of the scaling weight ρ by another one uses
  (ρ′/ρ)^(±𝗅) ∈ S⁰, which is also the fact behind [Hin26d]'s remark that ρ^(−𝗅)S^𝗆 depends on 𝗆, 𝗅 only modulo lower
  terms. No compatibility statement of [Hin26d] is used.
- (g) (3.38) of Theorem 3.51 on N_(P′) (with (S8) for variable orders, which (S8) states, and entrywise for systems),
  Definition 3.25 (𝔐 = {j(λρ) = 0}, the essential support), Definition 3.43 (WF′ = ess supp), Lemma 3.24 (1) (S⁰
  consists of uniformly continuous functions) and the multiplicativity of j, all quoted in (S16) of Appendix A. This is
  the converse of the translation in lem:iv5-calc-disjoint of chapter 33: from the locus back to the symbols.

### 6.2 What the new proofs of 27:460 and of (h) take from chapter 27

- lem:ii-f-2-phase (new, P-S7-3): smooth functions on the compactified phase space X are symbols of order 0, uniformly in
  h. Chapter 27 asserted this for its orders without proof; the cut-offs y_j of (c), y and y′ of (h) and the partitions
  of unity need it. The proof compares the scaled chart frames ρ_i∂_(x^i) of each cell with smooth frames of the
  bundle whose sections are 𝒱_ħ, both spanning 𝒱_ħ uniformly in h, and uses that the chart fields are bounded
  combinations of b-vector fields of ι⁺ which, at fixed h, are smooth on ι⁺_ħ (tangent to {h = 0} and to the centre of
  the blow-up). Chapter 33 proves its own analogue (lem:iv5-calc-structure (d)) for its structure.
- (d) of lem:ii-f-2-2 (lem:i-b-2-2 (e), inverse of an elliptic symbol times a cut-off) and (f) (i) (symbols supported in
  {ρ_sf ≥ δ, |ζ| ≤ C_0} have every order −K𝐞).
- lem:ii-f-2-1 (a) (ρ̄ ≍ ρ_sf) and the density shift of the proof of (a).

### 6.3 Points near the sites, outside the question

- **(S11) at 27:444 and 27:556.** Chapter 27's classes have base weights only, which (S8) covers; the citations of
  (S11) there rest on the p. 64 sentence and appear unnecessary. Not changed (R-P-S7 m2 proposes no change either).
- **The quotation at 95:969–970** of the sufficient condition on weights is accurate as a quotation and is kept; the
  chapters no longer use the condition.
- **[Hin26d, p. 66]** prints the elliptic operator defining wH^(m,l) as "A ∈ wρ^(−l)Ψ^m_𝒱(M)"; with Theorem 3.44's
  conventions it is w⁻¹ρ^(−l)Ψ^m, which lem:ii-a-3-1 uses (E ∈ w⁻¹Ψ^(𝗆,𝗅)_𝒱). Chapter 95 quotes the definition only as
  "for a fixed elliptic A". Not changed.

### 6.4 Alternatives weighed

- **Define the parameterised classes by restriction to every N_(P′)**, as chapter 33 does (def:iv5-calc-cells). This
  makes compositions immediate without Remark 4.9, but it loses the global family symbols that chapter 27's
  definitions of WF′ and of the principal symbol use. With Remark 4.9 the classes of Definition 3.59 serve for variable
  orders too, so this is not needed. Chapter 33 is unaffected: its classes contain those of (S7) by
  lem:ii-a-3-1 (b).
- **(e) through Proposition 3.55 (3) on N_(P′)**, as in the version 16e6e03f, with (S8) read as including that
  proposition. That needs a reading of (S8) that the edition does not state, for variable orders, the (S8) classes and
  systems. The coordinator chose the parametrix (R-P-S7 m5, option (b)), which needs only the calculus and the
  locality (g); the two older sites that rested on the same reading (23:1052–1054, 27:1432–1436) now cite (e).
- **Locality on 𝒫_ι through [Hin26d, §3.8]** (WF′ tested with C^∞(T̄*M) for admissible compactifications, and p. 62's
  "Definition 3.61 carries over to this setting mutatis mutandis"). It would need Definition 3.61 (1)–(3) verified for
  the phase space of chapter 27, which the edition uses nowhere. Not chosen; (g) does the translation directly.

### 6.5 The published numbering

The note at the end of Appendix A converts numbers to the published version by rules for the items it lists. Remark
3.57 falls under its Section 3 rule and is added to the list (P-S7-11). Remark 4.9 lies in Section 4, where the note
lists individual items, and its published number cannot be read from the note's rules (Definition 4.6 keeps its
number, Definition 4.11 does not). The versions available to me (arXiv v1 as PDF and HTML) carry the v1 numbers; arXiv
v2 has no PDF on the reader. The coordinator should add Remark 4.9's published number to the note, or leave the note as
it is: it states that the numbers in (S1)–(S16) are those of arXiv version 1.

### 6.6 Effect on other items

- notes/reports/P-G1-C23-1-deferred.md is closed by this file: P-S7-1 replaces C23-1, and its three cited sites are
  settled in section 4.
- No other open proof file touches these lines or labels.
- Two labels are added: lem:ii-a-3-1 in chapter 23 (cited from chapters 23, 27 and 37; assembled as Lemma 14.15) and
  lem:ii-f-2-phase in chapter 27 (cited there; assembled as Lemma 18.7, after which the numbers of the later lemmas of
  that chapter increase by one, all references being by label). No equation label is added.

## 7. Crosswalk

Each old row occurs once in its file at HEAD; every new row has four tab-separated fields and is ASCII. COMMIT in the
two new rows is the commit that adds this file; the line ranges are those of the two lemmas in section 5 (P-S7-2 and
P-S7-3).

**crosswalk/23-s04-compactified.tsv, row sec:ii-a-3** (line 29).

Old row:

```text
sec:ii-a-3	docket68/n1star/proof5/PART-II-A-SETUP.md:343	II.A section 3	quoted [SBG] = [Hin26d] black box (S1)-(S11) as a numbered list; pages added from arXiv:2408.06651v1 (printed page = PDF page); F3-S04: (S15) added ([Hin26d] Prop 2.3 with (2.3), (2.5) pp. 19-20; Lemma 3.42 and proof p. 51; p. 52; proof of Prop 4.22 p. 75), quoted from arXiv v1; list cited as (S1)-(S15)
```

Replaced by two rows, the row itself and the new row lem:ii-a-3-1 inserted after it:

```text
sec:ii-a-3	docket68/n1star/proof5/PART-II-A-SETUP.md:343	II.A section 3	quoted [SBG] = [Hin26d] black box (S1)-(S11) as a numbered list; pages added from arXiv:2408.06651v1 (printed page = PDF page); F3-S04: (S15) added ([Hin26d] Prop 2.3 with (2.3), (2.5) pp. 19-20; Lemma 3.42 and proof p. 51; p. 52; proof of Prop 4.22 p. 75), quoted from arXiv v1; list cited as (S1)-(S15); P-S7: (S7) restated from [Hin26d] Def. 1.9 p. 9, pp. 58-59 (Remarks 3.56-3.57, Defs 3.58-3.59, the boundedness paragraph with footnote 13, Theorem 3.51 verbatim, wDiff), p. 64, Remark 4.9 p. 67, p. 74; the words 'the above holds uniformly in p' dropped (not stated there); lem:ii-a-3-1 added after the list; the weights of P x M are those with the bounds of (S2) uniform in p (the sufficient condition after Def. 3.58 is not used)
lem:ii-a-3-1	paper/reader/proofs/P-S7.md@COMMIT:540-681	proof S7, uniformity in the parameter	new lemma; reduction to P' x M for countable P' ([Hin26d] p. 59, footnote 13); (d) norms of elliptic families by a Neumann parametrix; (e) uniform elliptic estimate by a parametrix with nested cut-off symbols, from the calculus of (S7)-(S8) and (g) only, for variable orders, the (S8) classes and systems; (f) same charts and comparable scalings; (g) locality of products by (3.38) on P' x M translated back to cut-off symbols
```

**crosswalk/23-s04-compactified.tsv, row lem:ii-a-8-4** (line 63; its note was empty).

Old row:

```text
lem:ii-a-8-4	docket68/n1star/proof5/PART-II-A-SETUP.md:893	II.A Lemma 8.4	
```

New row:

```text
lem:ii-a-8-4	docket68/n1star/proof5/PART-II-A-SETUP.md:893	II.A Lemma 8.4	P-S7: (d) cites lem:ii-a-3-1 (e) (single structure, B = I, Lambda elliptic in that lemma's sense) in place of (S5) with (S8)
```

**crosswalk/27-s08-iota-normal.tsv, row sec:ii-f-2-1** (line 34; its note was empty).

Old row:

```text
sec:ii-f-2-1	docket68/n1star/proof5/PART-II-F-IOTA.md:326	II.F section 2.1	
```

New row:

```text
sec:ii-f-2-1	docket68/n1star/proof5/PART-II-F-IOTA.md:326	II.F section 2.1	P-S7: phase space includes the slice h = 1 (compactness of P_iota); Ell(A) stated with the bound at all points over h in (0, 1] of a neighbourhood (def:i-b-2-9's h < h_0 at points over sf); WF' with the weighted classes S^(o-Ke), relative to the order at which A is taken (locality, lem:ii-f-2-2 (h)); the slice h = 1 is not a face; the Ell condition does not depend on the representative
```

**crosswalk/27-s08-iota-normal.tsv, row eq:ii-f-2-2** (line 37; its note was empty).

Old row:

```text
eq:ii-f-2-2	docket68/n1star/proof5/PART-II-F-IOTA.md:383	II.F (2.2)	
```

Replaced by two rows, the row itself and the new row lem:ii-f-2-phase inserted after it:

```text
eq:ii-f-2-2	docket68/n1star/proof5/PART-II-F-IOTA.md:383	II.F (2.2)	
lem:ii-f-2-phase	paper/reader/proofs/P-S7.md@COMMIT:725-751	proof S7, smooth functions on the phase space	new lemma; smooth functions on the compactified phase space (slice h = 1 included) lie in S^0 uniformly in h, so the orders are variable orders; frames of the semiclassical 0- and cone tangent bundle against the scaled chart frames
```

**crosswalk/27-s08-iota-normal.tsv, row lem:ii-f-2-2** (line 38).

Old row:

```text
lem:ii-f-2-2	docket68/n1star/proof5/PART-II-F-IOTA.md:412	II.F Lemma 2.2	localisation constant delta_0 of (f) renamed delta_s (collision with the collar delta_0)
```

New row:

```text
lem:ii-f-2-2	docket68/n1star/proof5/PART-II-F-IOTA.md:412	II.F Lemma 2.2	localisation constant delta_0 of (f) renamed delta_s (collision with the collar delta_0); P-S7: (b) cites (S7) for the uniformity in h; (c) proved uniformly in h by lem:ii-a-3-1 (e), with cut-offs y_1, y_2, y_3 on the compact phase space and (f) (i) off P_iota, in place of 'the microlocal elliptic estimate of (S5) ... localised as in prop:i-b-2-10'; (a) the bound by a seminorm uniform in h by a diagonal argument over countable P'; (h) locality added (WF'(AB) in WF'(A) and WF'(B), empty WF' gives the orders o-Ke) by lem:ii-a-3-1 (g)
```

**crosswalk/27-s08-iota-normal.tsv, row prop:ii-f-2-3** (line 41).

Old row:

```text
prop:ii-f-2-3	docket68/n1star/proof5/PART-II-F-IOTA.md:556	II.F Proposition 2.3	I.B Corollary 4.6-prime cited through a pending marker (no canonical key for a primed number)
```

New row:

```text
prop:ii-f-2-3	docket68/n1star/proof5/PART-II-F-IOTA.md:556	II.F Proposition 2.3	I.B Corollary 4.6-prime cited through a pending marker (no canonical key for a primed number); P-S7 (reader): the locality of products listed and supplied by lem:ii-f-2-2 (h)
```

**crosswalk/27-s08-iota-normal.tsv, row lem:ii-f-5-6** (line 107).

Old row:

```text
lem:ii-f-5-6	docket68/n1star/proof5/PART-II-F-IOTA.md:1544	II.F Lemma 5.6	N and Z_N written M and Z_M; Mellin variable lambda written zeta
```

New row:

```text
lem:ii-f-5-6	docket68/n1star/proof5/PART-II-F-IOTA.md:1544	II.F Lemma 5.6	N and Z_N written M and Z_M; Mellin variable lambda written zeta; P-S7: Step 1 cites lem:ii-a-3-1 (e) (single structure, B = I, cut-offs in the elliptic weight) in place of (S5) with (S8)
```

**crosswalk/33-s14-constraint-damping.tsv, row lem:iv5-calc-structure** (line 71).

Old row:

```text
lem:iv5-calc-structure	paper/reader/proofs/P-G1.md@3b715dd5:50-143	proof G1, structures	structures, weights, symbols
```

New row:

```text
lem:iv5-calc-structure	paper/reader/proofs/P-G1.md@3b715dd5:50-143	proof G1, structures	structures, weights, symbols; P-S7: (b) the weights of the parameterised structure by the bounds of (S2) uniform in h, in place of the sufficient condition after [Hin26d] Def. 3.58
```

**crosswalk/37-s18-augmented.tsv, row lem:iii-h1-3-1** (line 52).

Old row:

```text
lem:iii-h1-3-1	docket68/n1star/proof5/PART-III-H2-ADMISS.md:176	III.H1 Lemma 3.1	tagged parenthesis at 222-223 dropped; (3.1) kept with its 2 epsilon; the loss parameter of I.B T1.3 (5) written epsilon-prime (source reuses epsilon); proof bounds the weight beta, then beta - 2 epsilon
```

New row:

```text
lem:iii-h1-3-1	docket68/n1star/proof5/PART-III-H2-ADMISS.md:176	III.H1 Lemma 3.1	tagged parenthesis at 222-223 dropped; (3.1) kept with its 2 epsilon; the loss parameter of I.B T1.3 (5) written epsilon-prime (source reuses epsilon); proof bounds the weight beta, then beta - 2 epsilon; P-S7: on c/2 <= |sigma| <= 1 the semiclassical norm at h = 1/|sigma| >= 1 and the fixed norm (spectral structure at |sigma| = 1) defined; uniform equivalence of the three norms by lem:ii-a-3-1 (f), (d) in place of the citation of (S7); the same for 1 <= |sigma| <= C_0, and the fixed norm identified with the orders (s_c, r_sigma + beta) uniformly
```

**crosswalk/95-standard-results.tsv, row thm:std-sbg-calculus** (line 54; its note was empty).

Old row:

```text
thm:std-sbg-calculus	docket68/n1star/N1STAR-PROOF.md:8178-8193; paper/RESPONSE-HL-5D.md:2058-2060	[Hin26d] READ in NP 10.65 (the 3b-calculus in bounded geometry)	
```

New row:

```text
thm:std-sbg-calculus	docket68/n1star/N1STAR-PROOF.md:8178-8193; paper/RESPONSE-HL-5D.md:2058-2060	[Hin26d] READ in NP 10.65 (the 3b-calculus in bounded geometry)	P-S7: (S7) also quotes Remark 3.57, p. 64, Remark 4.9 and p. 74, header ranges extended; (S16) quotes Prop. 3.55 (3) and the elliptic set of Defs 3.25 and 3.43; numbering note lists Remark 3.57
```

## 8. Checks (on a scratch copy)

The scratch copy is in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/ps7/tree3/.
It holds chapters/, crosswalk/, assemble.py, lint.py and OUTLINE.md, taken from HEAD (edafc288) with git archive.

Before:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4928 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4928, computations cited 0, problems 0

After P-S7-1 to P-S7-18, and the crosswalk rows of section 7:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4930 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4930, computations cited 0, problems 0
    $ python3 assemble.py && python3 lint.py --paper
    PAPER.md: 0 hit(s)

The two new labels are lem:ii-a-3-1, assembled as Lemma 14.15, and lem:ii-f-2-phase, assembled as Lemma 18.7.
assemble.py was run only in the scratch copy.

Further checks:
- **Old texts.** Each occurs exactly once, as whole lines, in its chapter at HEAD (edafc288), the five chapter files
  being unchanged since the version 16e6e03f was written; the same holds for the old crosswalk rows.
- **Line lengths.** No new line exceeds 121 characters, counted as characters. With every [[kind:key]] replaced by
  "Proposition 33.123", the only longer lines are the first two of P-S7-16, which are old lines kept unchanged
  (27:552–553). The longest line of the assembled PAPER.md has 121 characters.
- **Typography.** No new line after a non-blank line starts with "+ ", "- ", "* ", "> ", "#", "=", "|" or "<". There
  is no backslash and no backtick in the new texts. Labels are lowercase.
- **Proofs and ∎.** The proofs of the two new lemmas end with ∎. The proof of lem:ii-f-2-2 keeps one ∎, moved to the end
  of the new proof of (h) (P-S7-15); P-S7-5, P-S7-6, P-S7-13, P-S7-16 and P-S7-17 sit inside proofs whose ∎ is
  unchanged. lint's count of proofs against ∎ is clean.
- **Crosswalk.** The new rows keep four tab-separated fields and are ASCII; each old row occurs once.
- **md5 of the scratch files after the merge:** chapters 23-s04-compactified.md 488db29ebf71ea8e2735c126a880f30c,
  27-s08-iota-normal.md b30eac972f9b5fb233f4187c8e31d8e1, 33-s14-constraint-damping.md 4b86643613f7b207c5b127d964e9ee86,
  37-s18-augmented.md f803ece3e930a233b26f05f94c64394e, 95-standard-results.md 8060f7c5ec3f4d858cfd4281fd01d3e2;
  crosswalk 23 ca8fc45b24f9bb1d797d3cdef1e47d9e, 27 69331a852abc7689d6c4afdfd836420f, 33
  3395b3df9caaf9c7625ddc1074d627f4, 37 d5d53ce8a29c7ecfbdf70a98fc6d01b2, 95 8e032fe33e2ba3b95111db1aa4685faf (computed
  with the two new crosswalk rows carrying placeholders for COMMIT and for the line ranges).

## 9. Changes against the version 16e6e03f (the fix round of R-P-S7)

| Finding | Change | Where |
|---|---|---|
| M1 (i)–(ii) | lem:ii-a-3-1 (g), locality in terms of cut-off symbols, with proof; 𝔐 and j defined there, (S16) of the appendix named | P-S7-2 |
| M1 (iii) | WF′ with S^(𝐨−K𝐞), relative to the order at which A is taken; "For A ∈ Ψ^𝐨" moved to the front | P-S7-3 |
| M1 (iv) | lem:ii-f-2-2 (h), locality on 𝒫_ι, with proof; the ∎ moved | P-S7-14, P-S7-15 (new) |
| M1 (v) | the proof of prop:ii-f-2-3 lists locality, supplied by (h) | P-S7-16 (new) |
| M1 (vi) | crosswalk notes for lem:ii-a-3-1, sec:ii-f-2-1, lem:ii-f-2-2, prop:ii-f-2-3; the last sentence of (S7) names (g) | section 7, P-S7-1 |
| M1, check | every use of WF′ and Ell of chapter 27 re-read with the weighted WF′ | section 4.9 |
| m1 | (S7) states the weights by their definition; 33:1515–1516 uses the definition | P-S7-1, P-S7-18 (new) |
| m2 | (b) of lem:ii-a-3-1 no longer claims a class with phase space weights | P-S7-2 |
| m3 | 1 ≤ \|σ\| ≤ C_0 and the identification with the orders (s_c, 𝗋_σ + β), uniformly | P-S7-6 |
| m4 | the bound by a seminorm in lem:ii-f-2-2 (a) made uniform in h by a diagonal argument | P-S7-13 (new) |
| m5 (coordinator: option (b)) | lem:ii-a-3-1 (e) proved by a parametrix from the calculus and (g), for variable orders, the (S8) classes and systems; 23:1052–1054 and 27:1432–1436 cite (e) instead of (S5) with (S8) | P-S7-2, P-S7-12, P-S7-17 (new) |
| n1 | Remark 3.57 as printed ("strongly compatible, though not uniformly") | P-S7-1 |
| n2 | the weights of P-S7-6 written w_∗ | P-S7-6 |
| n3 | the slice h = 1 not counted among the faces, its scope reaching *Orders and spaces*; Ell independent of the representative; the principal symbol "defined below" | P-S7-3 |
| n4 | the proof of (a) says that (b) uses only the constant-order part of (a) | P-S7-2 |
| n5 | lem:ii-f-2-phase: smooth functions on the phase space lie in S⁰, uniformly in h, with proof; cited in (c) and (h) | P-S7-3, P-S7-5, P-S7-15 |
| n6 | the ellipticity of P_(ι,h,z) at fibre infinity for every h cited from the last sentence of prop:ii-f-2-6 | section 1 |
| n7 | recorded, no change | section 6.3 |

Outside the findings: the old text of P-S7-3 now runs to line 416, so that lem:ii-f-2-phase follows the paragraph;
the header, sections 1, 3, 4, 6, 7 and 8 are revised accordingly; HEAD moved from a8ecdce7 to edafc288 without a change
to the five chapter files or their crosswalk rows.
