# R-P-S7: independent reading of proofs/P-S7.md

File read: research/warp-drive/paper/reader/proofs/P-S7.md, 955 lines, md5 16e6e03f795d2c73d79116cdce206e38 (confirmed),
with notes/reports/P-S7.md (135 lines). Branch ccr-66909215-gi0qa5. HEAD moved during the reading (cca730a2 → 6c07b297 →
52609127, all snapshot/merge commits touching chapters 03, 81, 83, 90, 98 and proof files only); chapters 23, 27, 37, 95
and the four crosswalk files have the md5s P-S7 states at every HEAD I checked, including 52609127.
Source: [Hin26d] = arXiv:2408.06651v1, read page by page through the alphaXiv PDF reader (pp. 1–2, 5, 7–10, 12–13, 27,
29–30, 32, 34, 36–38, 40–41, 44–46, 51–52, 55, 57–62, 64, 66–69, 74–75). arXiv v2 has no PDF on the reader, so the
published number of Remark 4.9 could not be checked by me either.

## Verdict

**NOT CONFIRMED: 1 Major, 5 minor, 7 nits.**

What is confirmed: the verdict on (S7) (it overclaims; the omissions are real), every quotation of [Hin26d] in sections 2
and 5, the new (S7) text apart from one sentence (m1), lem:ii-a-3-1 (a)–(f) (re-derived step by step; (c) is
measurability-free; (e) holds modulo a reading of (S8) that predates this file, m5), the defect of the literal Ell and the
correctness of the corrected Ell, the new proof of lem:ii-f-2-2 (c), the restated 37:824 on c/2 ≤ |σ| ≤ 1, the Appendix A
items, and all placement mechanics. The Major is the writer's own open item (task item 4): the locality of products on
𝒫_ι, on which prop:ii-f-2-3 rests, is proved neither in chapter 27 as it stands nor after this file. It is pre-existing,
not introduced by P-S7; full replacement text is given below and was checked in a scratch merge.

## Findings

### Major

**M1. Locality of products in the calculus on ι⁺ (chapter 27) is not proved; the WF′ definition it needs is the
unweighted one.** Chapter 27:552–556 (unchanged by P-S7):

> *Proof.* The proofs in [[ch:s02]] use of the calculus: the mapping property ([[prop:i-b-2-8]]), the composition and
> adjoint theorems with the principal symbols of products, adjoints and commutators ([[thm:i-b-2-4]], [[thm:i-b-2-5]] and
> [[eq:i-b-2-5]]), the elliptic estimate ([[prop:i-b-2-10]]), the symbol properties of [[lem:i-b-2-2]], the square roots
> of [[lem:i-b-2-11]] and [[lem:i-b-2-12]], and the L² pairing of H^𝐨 with H^(−𝐨). These are [[lem:ii-f-2-2]] (a)–(e)
> here, ...

What is wrong.
- The transferred proofs of chapter 21 also use the locality of products: consequence (iv) after thm:i-b-2-5
  (21:390), its corollary WF′_h(AB) ⊂ WF′_h(A) ∩ WF′_h(B) (21:461), and that an operator with empty WF′_h is residual.
  Examples: 21:561–562 (proof of lem:i-b-3-3, "Ǎ(I − Φ) and (I − Φ)^(*h)Ǎ are residual"), 21:481 (proof of
  lem:i-b-2-11, "E ∈ Ψ^(2𝐦−(1−ϵ)𝟏) near WF′_h(B)", then ⟨EBu, Bu⟩), lem:i-b-3-4 (G_j with WF′(G_j) ⊂ Ell(B^(j))).
  lem:ii-f-2-2 (a)–(e) contain no locality statement ((b) gives principal symbols only), and nothing else in chapter 27
  does. So the list "(a)–(e)" is incomplete and the transfer has a missing step.
- [Hin26d] gives locality only as (3.38) on the microlocalisation locus 𝔐 of a single structure (p. 55), carried over
  "verbatim" to P × M (p. 59), with Remark 4.9 for variable orders. Translating it to WF′ ⊂ 𝒫_ι, defined by symbol
  bounds near points of X := ^(0ħ,cħ)T̄*ι⁺_ħ uniformly in h, needs the converse of the translation done in
  lem:ii-a-3-1 (e): (e) turns cut-off hypotheses into WF′ ⊂ Ell on 𝔐; locality must turn a statement on 𝔐 back into
  symbol bounds near ϖ ∈ X, uniformly in h. Neither (e) nor anything else in the file does this (P-S7 §6.3 says so).
  [Hin26d, §3.8, pp. 60–62] (WF′ "via testing with elements of C^∞(T̄*M)" for admissible compactifications, and p. 62:
  "Definition 3.61 carries over to this setting mutatis mutandis" in the parameterised case) would be a citation route,
  but it needs Definition 3.61 (1)–(3) verified for X and is not used anywhere in the edition.
- The definition of WF′ in sec:ii-f-2-1 (27:412–413, kept by P-S7-3) uses S^(−K𝐞), with no weight. In chapter 21,
  S^(−M𝟏) for every M equals S^(𝐨−M𝟏) for every M (𝟏 lowers all three orders); in chapter 27, 𝐞 = (1; 0, 0, 0; 1) does
  not lower the weights at 0f, cf, tf, so S^(−K𝐞) is not the weighted condition. With it locality is false: take
  ϖ ∈ F_I, A = Op(φe^(−1/ρ_sf)) ∈ Ψ⁰ (φ a cut-off near ϖ) and B = multiplication by ρ_0f⁻¹ ∈ Ψ^((0;1,0,0;0)); then
  ϖ ∉ WF′(A) (e^(−1/ρ_sf) ≤ C_Kρ_sf^K), but the symbol φe^(−1/ρ_sf)ρ_0f⁻¹ of AB is not O(ρ_sf^K) near ϖ (on
  x_I = e^(−2/h) it grows), so ϖ ∈ WF′(AB). The weighted condition S^(𝐨−K𝐞) (that of [Hin26d, Definition 3.25],
  ess supp^w with χa ∈ wρ^∞S^(−∞)) is the one for which locality holds. For B ∈ Ψ⁰ the two agree, so P-S7-5 is
  unaffected.

Fix (all texts below were applied in a second scratch tree on top of P-S7-1 to P-S7-11: lint --chapters 0 hits,
assemble --check 0 problems, assembled PAPER.md 0 hits, longest line 121 characters; no wrapped line starts with a
forbidden character; also checked with every [[kind:key]] replaced by "Proposition 33.123").

(i) P-S7-2 (chapter 23, lem:ii-a-3-1), statement: after P-S7.md line 463 ("derivatives along the 𝒲_p uniformly in p,
E being replaced by (w/w̃)E.") insert a blank line and

```text
(g) (*Locality.*) Let A ∈ wΨ^(𝗆,𝗅)_𝒱 and B ∈ w′Ψ^(𝗆′,𝗅′)_𝒱 be Op(a) + R and Op(b) + R′ as in (S7), and let y, y′ ∈ S⁰
be families with yy′ = y′ and ya ∈ wρ^∞S^(−∞). If AB = Op(c) + R″ and BA = Op(c′) + R‴ as in (S7), then y′c and y′c′
lie in ww′ρ^∞S^(−∞).
```

(ii) P-S7-2, proof: in P-S7.md line 529 delete the final " ∎" (the line then ends "uniformly in p."), and add a blank
line and

```text
(g) Fix a countable P′ ⊂ P and write N := N_(P′), with 𝔐 and j as in the proof of (e). By (b), A_(P′), B_(P′) and
(AB)_(P′) = A_(P′)B_(P′) lie in the classes of N, with the symbols a_(P′), b_(P′) and c_(P′). If ϖ ∈ 𝔐 and
j(y)(ϖ) ≠ 0, then ϖ is not in the essential support of a_(P′), which is WF′(A_(P′)) ((S16)); so, by the locality of
products of (S5), with (S8) for variable orders, the essential support of c_(P′) lies in {j(y) = 0}. The set
Z := 𝔐 ∩ supp j(y′) is compact and lies in {j(y) = 1}, as j(y′)(1 − j(y)) = j(y′(1 − y)) = 0. Each point of Z has a
χ ∈ S⁰ with j(χ) ≠ 0 there and χc_(P′) ∈ ww′ρ^∞S^(−∞); finitely many, χ_1, …, χ_n, give g := Σ_i |χ_i|² ∈ S⁰ with
j(g) > ε on a neighbourhood O of Z, for some ε > 0. Let ψ ∈ C^∞(ℝ) vanish on (−∞, ε/2] and equal 1 on [ε, ∞), and put
θ := ψ(g) ∈ S⁰. Then y′θc_(P′) = y′(ψ(g)/g)Σ_i χ̄_i(χ_ic_(P′)) lies in ww′ρ^∞S^(−∞), ψ(s)/s being smooth. And
f := y′(1 − θ) ∈ S⁰ has j(f) = 0 on O and off supp j(y′), hence on a neighbourhood of 𝔐 = {j(ρλ) = 0}; so
j(ρλ) ≥ δ on the compact set supp j(f) for some δ > 0, f vanishes where ρλ < δ, and fc_(P′) ∈ ww′ρ^∞S^(−∞), as ρ and
λ are bounded below on the support of f. So y′c_(P′) = y′θc_(P′) + fc_(P′) lies in ww′ρ^∞S^(−∞) on N. Each seminorm
of y′c_(P′) is the supremum over p ∈ P′ of that of y′c_p; so, as a function of p, each seminorm of y′c_p is bounded
on every countable subset of P, hence bounded, by (c). The same argument applies to BA. ∎
```

(Checked: j(ψ(g)) = ψ(j(g)) and j(χ̄χ) = |j(χ)|² by continuity on the dense subset; 𝔐 ⊂ O ∪ (complement of
supp j(y′)) because 𝔐 ∩ supp j(y′) = Z ⊂ O; on {ρλ ≥ δ} both ρ and λ are ≥ δ/C, so every class weight ρ^Nλ^N is
bounded below there; the locality used on N is (S5)'s "WF′(A_1A_2) ⊂ WF′(A_1) ∩ WF′(A_2)", i.e. (3.38), which (S8)'s
stated reading "including the calculus of its Theorem 3.51" covers for variable orders.)

(iii) P-S7-3: replace its New text by (10 lines; changes: "For A ∈ Ψ^𝐨," moved to the front, S^(−K𝐞) → S^(𝐨−K𝐞) twice,
rewrap)

```text
*Phase space.* 𝒫_ι := ^(0ħ,cħ)T̄*_(sf)ι⁺_ħ ∪ ^(0ħ,cħ)S*ι⁺_ħ is the fibre-compactified phase space over sf together with
fibre infinity over all of ι⁺_ħ; here and below ι⁺_ħ and ^(0ħ,cħ)T̄*ι⁺_ħ include the slice h = 1, the operators being
given for h ∈ (0, 1], so 𝒫_ι is compact. The part over sf is a manifold with corners whose boundary hypersurfaces
are fibre infinity, F_I (over sf ∩ 0f = {x_I = 0}) and F_K (over sf ∩ tf = {R = 0}); F_I ∩ F_K = ∅. On it we use the
semiclassical 0-covectors ξ dx_I/(hx_I) + η dω/(hx_I) near F_I and the semiclassical cone covectors of [[sec:ii-f-1-3]]
near F_K, over sf ξ_cħ dR/h + η_cħ R dω/h. For A ∈ Ψ^𝐨, WF′(A) and Ell(A) ⊂ 𝒫_ι are defined as in [[def:i-b-2-9]],
with S^(𝐨−K𝐞) in place of S^(−M𝟏): ϖ ∉ WF′(A) if the symbol of A lies in S^(𝐨−K𝐞) on a neighbourhood of ϖ in
^(0ħ,cħ)T̄*ι⁺_ħ for every K; and ϖ ∈ Ell(A) if ϖ has a neighbourhood U in ^(0ħ,cħ)T̄*ι⁺_ħ such that a representative a
of the principal symbol of A is invertible, with |a⁻¹| ≤ Cw_𝐨⁻¹, at the points of U over h ∈ (0, 1] (at a point over sf
this is the condition of [[def:i-b-2-9]], with U inside {h < h_0}).
```

(iv) New placement item, chapters/27-s08-iota-normal.md, lem:ii-f-2-2: after line 442 ("graph norm, and likewise for
P*_(ι,h,z) and the orders −𝐨 + 𝐦 − 𝐞.") insert a blank line and

```text
(h) (Locality.) WF′(AB) ⊂ WF′(A) ∩ WF′(B) for A ∈ Ψ^𝐨 and B ∈ Ψ^(𝐨′); and if A ∈ Ψ^𝐨 and WF′(A) = ∅, then
A ∈ Ψ^(𝐨−K𝐞) for every K.
```

and replace line 491 ("same properties. ∎") by "same properties.", a blank line and

```text
(h) Let ϖ ∈ 𝒫_ι ∖ WF′(A), let a be the symbol of A, and let U be a neighbourhood of ϖ in X (as in the proof of (c)) on
which a lies in S^(𝐨−K𝐞) for every K. Choose y, y′ ∈ C^∞(X) supported in U with y = 1 near supp y′ and y′ = 1 near ϖ.
They lie in S⁰, and ya ∈ S^(𝐨−K𝐞) for every K, that is, ya ∈ wρ̄^∞S^(−∞) with w the weight of 𝐨 at 0f, cf and tf
([[lem:ii-f-2-1]] (a)). By [[lem:ii-a-3-1]] (g) the symbols c and c′ of AB and BA satisfy y′c, y′c′ ∈ S^(𝐨+𝐨′−K𝐞) for
every K, so ϖ lies in neither WF′(AB) nor WF′(BA); with A and B exchanged, this gives the first statement. If
WF′(A) = ∅, the partition of unity of the proof of (c), with WF′(A) in place of WF′(B) and 0 in place of y_1, gives
a ∈ S^(𝐨−K𝐞) for every K, so A ∈ Ψ^(𝐨−K𝐞). ∎
```

(v) New placement item, chapters/27-s08-iota-normal.md, prop:ii-f-2-3, proof, lines 552–556 (old text quoted above,
5 lines, occurs once) → 7 lines:

```text
*Proof.* The proofs in [[ch:s02]] use of the calculus: the mapping property ([[prop:i-b-2-8]]), the composition and
adjoint theorems with the principal symbols of products, adjoints and commutators ([[thm:i-b-2-4]], [[thm:i-b-2-5]] and
[[eq:i-b-2-5]]), the locality of products ((iv) of the consequences of [[thm:i-b-2-5]], and WF′_h(AB) ⊂ WF′_h(A) ∩
WF′_h(B) after [[def:i-b-2-9]]) with the fact that an operator whose WF′_h is empty is residual, the elliptic estimate
([[prop:i-b-2-10]]), the symbol properties of [[lem:i-b-2-2]], the square roots of [[lem:i-b-2-11]] and
[[lem:i-b-2-12]], and the L² pairing of H^𝐨 with H^(−𝐨). These are [[lem:ii-f-2-2]] (a)–(e) and (h) here, the pairing
being (S3) and (S11) with the weight shift of the proof of [[lem:ii-f-2-2]] (a). [[lem:i-b-4-3]] and
```

(vi) Crosswalk: add to the notes of lem:ii-a-3-1 "; (g) locality of products by (3.38) on P' x M translated back to
cut-off symbols", of sec:ii-f-2-1 "; WF' with the weighted classes S^(o-Ke)", of lem:ii-f-2-2 "; (h) locality added",
and to prop:ii-f-2-3 (27-s08-iota-normal.tsv) "P-S7 (reader): the locality of products listed and supplied by
lem:ii-f-2-2 (h)". Optionally, the last sentence of P-S7-1 can name (g): "...; [[lem:ii-a-3-1]] gives the uniform
versions that are used, and the locality of products in terms of cut-off symbols ((g) there)."

### minor

**m1. The sufficient condition on weights, paraphrased in P-S7-1, is false as stated; its one use (33:1516) does not
need it.** P-S7.md 379–380 (new (S7)): "(it suffices that each w_p be a weight of ℬ^(p,×) and that the ratios
w_(p,α)/w_(p,β) of the weight families over overlapping cells be bounded uniformly in p)". This is a faithful
paraphrase of [Hin26d] after Definition 3.58, but read literally it is false: on M = ℝ with the standard cells and
P = ℕ, w_p := 2 + sin(p²x) is a weight of each ℬ^(p,×), the weight families (sup over the cells) have ratios ≤ 3, but
∂_x w_p/w_p is of size p², so (w_p) is not a weight of P × M (the coefficient Lie algebra contains the family ∂_x).
The edition states it as a fact. Its only use, 33:1515–1516 "the ratios of the weight across overlapping charts of the
parameterised structure are those for ℬ, which are bounded ((S7), the sufficient condition after [Hin26d, Definition
3.58])", concerns h-independent weights and charts, for which the bounds of (S2) are trivially uniform.
Fix. P-S7-1, replace P-S7.md lines 379–380 by

```text
of (S2) for the cells of all the ℬ^(p,×) together, that is, with the bounds of (S2) uniform in p (that each w_p be a
weight of ℬ^(p,×) is necessary but not sufficient), and the scaling weights
```

and add a placement item for chapters/33-s14-constraint-damping.md lines 1515–1516 (whole lines, occur once) →

```text
and the charts do not depend on h, the bounds of (S2) for the parameterised structure are those for ℬ, uniformly in h,
so these are weights of the parameterised structure ((S7)).
```

The quotation in Appendix A (95:969–970, "a sufficient additional condition ...") is accurate as a quotation and can
stay, or be cut as unused.

**m2. lem:ii-a-3-1 (b) asserts something about a class the edition never defines.** P-S7.md 440 "; likewise with a
phase space weight ((S11))" and 482 "((S4), (S8), (S11))". [Hin26d, p. 64] only says that operators with phase space
weights "can also be defined in the parameterized scaled b.g. setting ... We leave the details to the interested
reader"; the new (S7) reports exactly that, so no parameterised class with phase space weights exists in the edition,
and no use of lem:ii-a-3-1 needs one (chapter 27's Ψ^𝐨 is an (S8) class with base weights, 27:398–400). Fix: delete
"; likewise with a phase space weight ((S11))" (line 440) and change "((S4), (S8), (S11))" to "((S4), (S8))" (line
482). (The citations of (S11) at 27:444 and 27:556 then rest on the same p. 64 sentence; they appear unnecessary, as
the duality and boundedness for variable orders are in (S8); no change proposed there.)

**m3. P-S7-6 leaves out a uniform identification that the same proof uses, which P-S7 §6.3 derives but does not
place.** P-S7-6 defines "the fixed norm" as the norm with orders (𝗌_σ, 𝗌_σ) for the structure at |σ| = 1 and proves the
equivalence on c/2 ≤ |σ| ≤ 1. The proof then (37:844–860, paragraph "*c/2 ≤ |σ| ≤ C_0.*") bounds the integrand, which
is in the semiclassical norms ((𝗌_σ; k′), 𝗌_σ + β, 𝗌_σ) at |σ|⁻¹, by [[thm:i-a-7-2]] in the fixed-frequency spaces of
the orders (s_c, 𝗋_σ) with weight β, uniformly for c/2 ≤ |σ| ≤ C_0. That needs (1) the equivalence of the fixed norm with
the norm of the orders (s_c, 𝗋_σ + β), uniformly in σ (not written; §6.3 has the argument) and (2) the same for
1 ≤ |σ| ≤ C_0 (not addressed). Both are uniform equivalences over a compact parameter set, which [Hin26d] does not state
(Remark 3.57), so the (S7) question at this site is only half closed. Fix: in P-S7-6 replace P-S7.md line 640 ("(0, ∞).
So [[lem:ii-a-3-1]] (f), with (d) there ... gives the uniform equivalence.") by

```text
(0, ∞). So [[lem:ii-a-3-1]] (f), with (d) there for the choice of the elliptic families, gives the uniform equivalence.
The same holds for 1 ≤ |σ| ≤ C_0, the scalings (1 + |σ|⟨x⟩)⁻¹ then lying within the factor C_0 of (1 + ⟨x⟩)⁻¹; and,
uniformly for c/2 ≤ |σ| ≤ C_0, the fixed norm is equivalent to the norm of the same structure with the orders
(s_c, 𝗋_σ + β), in which [[thm:i-a-7-2]] is applied below. Indeed 𝗌_σ − s_c vanishes at fibre infinity ((C1)) and
𝗌_σ − 𝗋_σ over ∂X, so λ^(s_c−𝗌_σ), ρ^(𝗋_σ−𝗌_σ) and their inverses are bounded in S⁰ (each exponent is λ, resp. ρ,
times a function bounded in S⁰, and λ log λ and ρ log ρ are bounded with their derivatives); so the two pairs of
orders define the same classes, and the first terms of the two norms ((S8)) are bounded by each other modulo the
second, as in the proof of [[lem:ii-a-3-1]] (d).
```

(New count of P-S7-6: 21 lines. The identification of that sc-structure space with the fixed-frequency space of
[[thm:i-a-7-2]] at each σ is the one P-S7 §6.3 attributes to (C1) and sec:ii-a-5-1 (2); I did not re-check it.)

**m4. lem:ii-f-2-2 (a) claims "norm bounded by a seminorm of A" uniformly in h; the new (S7) gives only uniform
boundedness of each family.** 27:444 "(a) is (S5) with (S7), (S8) and (S11)". P-S7 §4.2 treats this as covered (Remark
3.47 on P′ × M, "uniform by the argument of (c)"), but that argument is only in the notes, and (c) alone does not give
it: the constant and the seminorm from (S5) on N_(P′) may a priori depend on P′. Fix (placement item for 27:444–445,
which become 5 lines):

```text
*Proof.* (a) is (S5) with (S7), (S8) and (S11), the weights by [[lem:ii-f-2-1]] (b) and the decay order at ρ̄ ≍ ρ_sf by
[[lem:ii-f-2-1]] (a). The bound by a seminorm holds on each N_(P′) of [[lem:ii-a-3-1]] ((S5), and (b) there), and its
constant and seminorm can be taken independent of P′: otherwise, with q_1 ≤ q_2 ≤ ⋯ the seminorms, there are h_k and
A_k with ‖(A_k)_(h_k)‖ > kq_k(A_k) for every k, which contradicts the bound on N_(P′) for P′ := {h_k : k ∈ ℕ}. The
density μ_b is ρ̄⁴ρ_0f³ times a uniformly positive 𝒱_ħ-density: near cf the scalings multiply
```

(The contradiction: on N_(P′), ‖A_h‖ ≤ Cq_(k_0)(A) for all A and h ∈ P′; for k ≥ max(k_0, C), q_k ≥ q_(k_0) gives
‖(A_k)_(h_k)‖ ≤ kq_k(A_k).) The fifth new line is the tail of the old line 445, so line 446 onwards ("to ρ̄⁴ up to
bounded factors, ...") is unchanged.

**m5. lem:ii-a-3-1 (e) applies [Hin26d, Proposition 3.55 (3)] outside its stated scope, through a reading of (S8) that
the edition does not state.** P-S7.md 504–505: "the microlocal elliptic estimate of (S5), with (S8) for variable orders,
holds on N". Proposition 3.55 is stated for standard classes and scalar operators. (e) needs it (1) for variable orders,
(2) for the (S8) classes with constant orders (B ∈ Ψ^(0,0) is in ⋂_δ S⁰_(1−δ,δ)), and (3) for ℂ^N-valued systems
([Hin26d, Remark 3.46]: "We leave the details to the interested reader"). Chapter 23's (S8) reads "Theorem 3.44
remains valid" as "including the calculus of its Theorem 3.51" only. P-S7 §3 (ii) calls this reading "not new", which
is true (lem:ii-a-8-4 (d) at 23:1052–1054, 27:1432–1434, the old 27:460), but it is nowhere stated in the text, and the
new lemma now rests on it in writing. Fix, for the coordinator: either (a) state the reading in (S8), e.g. after "we
read it as including the calculus of its Theorem 3.51" add "and the microlocal elliptic estimate of its Proposition
3.55 (3), whose proof (p. 57) is an application of that calculus", with the same for systems in (S14); or (b) prove (e)
on N for these classes by the parametrix of lem:ii-a-8-4 (b)–(c), which uses only the calculus and, with M1 (ii),
locality. Not counted against the mathematics of (e) itself, which is right once the estimate on N is granted.

### nits

**n1.** P-S7.md 391–392: "the ℬ^(p,×) for different p may be compatible without the norms ... (Remark 3.57)".
Remark 3.57 says "strongly compatible, though not uniformly so in p and p′". Suggested (3 lines replacing 391–392,
the following text "of (S8), with their operators ..." unchanged):

```text
P may be replaced by a subset, such as a sequence h_j ↘ 0 (Remark 3.56); the ℬ^(p,×) for different p may be strongly
compatible, though not uniformly in p, so that their Sobolev spaces agree as sets while their norms need not be
uniformly equivalent (Remark 3.57). By Remark 4.9 the variable orders
```

**n2.** P-S7.md 632–634: "spaces ρ^βϱ^(𝗌_σ)H^(𝗌_σ) ... where ρ := ⟨x⟩⁻¹: for the sc-b norm ρ^β is ρ_scf^βρ_tf^β" gives
ρ^β two meanings (equal to ⟨x⟩^(−β) and to ρ_scf^βρ_tf^β, which are only equivalent). Write "spaces w_∗ϱ^(𝗌_σ)H^(𝗌_σ)
... with w_∗ = ρ_scf^βρ_tf^β and ϱ = ρ_scf for the sc-b norm, w_∗ = ρ^β and ϱ = hρ for the semiclassical one, and
w_∗ = ρ^β and ϱ = ρ for the fixed one".

**n3.** P-S7-3 (P-S7.md 551–560): (a) including the slice h = 1 adds a boundary hypersurface {h = 1}, while 27:353 says
ι⁺_ħ "has four boundary hypersurfaces"; (b) "here and below" does not reach the paragraph *Orders and spaces* above,
where the orders are smooth functions on ^(0ħ,cħ)T̄*ι⁺_ħ (their boundedness up to h = 1 is what is wanted). Suggested:
"here, in the paragraph *Orders and spaces* above and below, ι⁺_ħ and ^(0ħ,cħ)T̄*ι⁺_ħ include the slice h = 1 (not
counted among the four faces, no estimate concerns it), ...". (c) The Ell clause uses "a representative a of the
principal symbol" one sentence before the principal symbol is defined, and P-S7-5 (607–608: "finitely many of the
neighbourhoods in the definitions of Ell(A) and Ell(G) cover it") uses that the condition does not depend on the
representative; add "(the condition does not depend on the representative, after U is shrunk: two representatives
differ by w_𝐨 times a symbol bounded by C(⟨ζ⟩⁻¹ρ_sf)^(1−ϵ), which is small near 𝒫_ι)". [Hin26d, p. 62]'s parameterised
example compactification [0, 1]_h × T̄*M also includes h = 1, which supports (a).

**n4.** lem:ii-a-3-1, proof of (a) for variable orders (P-S7.md 470–473) uses (b), whose proof (481) uses (a). The
order is sound ((b) uses only the constant-order part of (a), for the residual conditions), but say so: "(b) below
uses only the constant-order part of (a)".

**n5.** Pre-existing, now used: P-S7-5 (599–600) "smooth functions on X lie in S⁰, as the orders of [[sec:ii-f-2-1]]
do" rests on an assertion chapter 27 makes without proof (the orders are "smooth functions on the fibre-radially
compactified phase space ..., variable orders in the sense of (S8)"). Chapter 33 proves its analogue
(lem:iv5-calc-structure (d)). P-S7 §6.2 flags it. For the coordinator; no change to P-S7 needed.

**n6.** Notes only: P-S7.md 57–58 cite "(g) of the lemma" for ellipticity of P_(ι,h,z) at fibre infinity for every h;
(g) is a fixed-h statement. The uniform statement is the last sentence of prop:ii-f-2-6 (27:634, by eq:ii-f-1-10).

**n7.** For the record (no change): [Hin26d, p. 66] prints the elliptic operator defining wH^(m,l) as
"A ∈ wρ^(−l)Ψ^m_𝒱(M)"; with Theorem 3.44's conventions it must be w⁻¹ρ^(−l)Ψ^m. lem:ii-a-3-1 uses E ∈ w⁻¹Ψ^(𝗆,𝗅)_𝒱,
which is the consistent reading, and chapter 95's (S8) quotes the definition only as "for a fixed elliptic A". Also
"m′ − s" in p. 66's mapping statement is a misprint for m′ − m; (S8) in chapter 23 states the corrected form.

## The uses of def:i-b-2-9 and of Ell (task item 3)

def:i-b-2-9 is cited only at 27:412 (and defined at 21:457). The Ell of chapter 27 is used at the sites below; every
other Ell in the edition is a different definition.

| Site | Use | Status with the corrected Ell (P-S7-3) |
|---|---|---|
| 21:457 def:i-b-2-9 and its uses in ch. 21 (45 occurrences of Ell_h/WF′_h) and 29:1092–1107 | the h = 0 face 𝒫 | not changed by P-S7-3; unaffected |
| 27:412–413 | definition | corrected (P-S7-3); with M1 (iii) also WF′ weighted |
| 27:427 lem:ii-f-2-2 (c) | WF′(B) ⊂ Ell(A) ∩ Ell(G) | proved by P-S7-5; false with the literal Ell (fibre infinity over h ≥ ½) |
| 27:544–550 prop:ii-f-2-3 | transfers prop:i-b-2-10 (via (c)), lem:i-b-2-11 (positivity near WF′(B)), lem:i-b-3-3 (G elliptic on K_1, WF′(Φ) ⊂ Ell(G), WF′(J) ⊂ Ell(P), E′ elliptic on K_E), lem:i-b-3-4/(D5) (WF′(G_j) ⊂ Ell(B^(j))), prop:i-b-4-5, cor:i-b-4-6, lem:i-b-5-1 | all ellipticity at finite frequencies over sf, where the corrected and the literal conditions agree, or through (c): unaffected. The transfer itself lacks locality (M1) |
| 27:600 prop:ii-f-2-4 | G elliptic on Ū_0, E′ on K_E ⊂ Ū_0 (finite frequencies near F_I, F_K) | unaffected |
| 27:622 prop:ii-f-2-5 | G elliptic on Ū_0, E′ on K_E (near a curve at finite frequencies) | unaffected |
| 27:632–638 prop:ii-f-2-6 | G elliptic on compact K_0 ⊂ 𝒫_ι; "fibre infinity of 𝒫_ι lies in Ell(P′) for every z" | holds in the corrected sense: the principal symbol at fibre infinity is eq:ii-f-1-10 in the rescaled fibre variables, independent of h and z, the rest of lower order; the bound holds on a neighbourhood at all h ∈ (0, 1]. Under the literal Ell this sentence was vacuous over h > 0 |
| 27:652 | "P_(ι,h,z) is elliptic there" (fibre infinity) | as prop:ii-f-2-6 |
| 27:884–888 lem:ii-f-3-4 (a) | fibre infinity ⊂ Ell(P) by prop:ii-f-2-6; points over sf with G ≠ 0 | unaffected |
| 27:906–930 lem:ii-f-3-4 (d)–(e) | "points off Σ_1 are elliptic", "the elliptic set", "together with elliptic ones, are jointly elliptic on 𝒫_ι; a microlocal partition of unity gives ‖u‖_𝐨 ≤ C(Σ_i‖B_(*,i)u‖_𝐨 + ‖u‖_(𝐨−K𝐞))" | correct with the corrected Ell, and needs it: the partition-of-unity bound is (c) with A = Σ_i B_(*,i)*B_(*,i), B = G = I, so joint ellipticity at fibre infinity must hold uniformly in h (it does for the cut-offs used); with the literal Ell the hypothesis would be empty at fibre infinity over h > 0 |
| 27:1159–1160 lem:ii-f-4-4 | "elliptic regularity at fibre infinity ([[lem:ii-f-2-2]] (c), at this fixed h)" | correct with the corrected Ell, and needs it (fibre infinity over that h lies in Ell(P) by prop:ii-f-2-6); the regularity form of (c) is supplied by lem:ii-a-3-1 (e) ("the right side being possibly infinite") |
| 27:1183–1185 prop:ii-f-4-3, step 1 | hypotheses of prop:ii-f-2-4–2-6 for the system, "at fibre infinity and on the elliptic set because the principal symbol is G_(ι,z) Id" | as prop:ii-f-2-6; unaffected |
| 35:851–912 lem:iii-g-4-5, prop:iii-g-4-6 | prop:ii-f-2-4–2-6 near the cone, "elliptic points", prop:ii-f-2-6 "at the fibre infinity of the cone calculus" | through prop:ii-f-2-6; unaffected |
| 20:243 (sc), 23:1349 and ch. 25 (e3b), 33:1546 (3b,ħ), 27:169, 1300–1365, 1432–1502 (0,b at fixed σ, full ellipticity) | other definitions | unaffected (33:1546 already has the corrected form "invertible on 𝒰 ∩ 𝒫°") |

So the writer's expectation is right, and two further uses (27:906–930 and 27:1159) actually require the correction.

## What I checked and found correct

- **Quotations** (sections 2.1–2.2 and P-S7-7 to P-S7-11), against the PDF pages: Definition 1.9 and the paragraph
  after it (p. 9); p. 58 (Section 3.7 opening, the scaling and elliptic weights, (3.40)); Remarks 3.56 and 3.57
  (pp. 58–59); p. 59 in full (Definitions 3.58–3.59, the boundedness paragraph, footnote 13, Theorem 3.51 "verbatim",
  wDiff); Remark 3.60 and p. 60 (wave front sets); Theorem 3.44 (p. 51), Theorem 3.51 with (3.38) (p. 55; the printed
  second A_1 is a misprint for A_2), Proposition 3.55 (3) (p. 57; the superscripts m, w of Ell stand for A's),
  Definitions 3.25 (p. 41) and 3.43 (p. 51); p. 64; Definition 4.6 and the paragraph after it (p. 66); Remark 4.9
  (p. 67); p. 74. All verbatim up to the edition's notation. (3.14) uses the unnormalised cut-offs φ_α^*χ (p. 34),
  Definition 3.31 the normalised ones (p. 44), as the proofs of (a) and (b) say.
- **Verdict on (S7)**: confirmed. p. 59 states uniformity only for boundedness, the Theorem 3.51 properties and the
  wDiff characterisation; Proposition 3.55, Theorems 3.21 and 3.52 and Proposition 3.22 are not stated for parameterised
  structures; Remark 3.57 says norms need not be uniformly equivalent; Remark 3.60 that full symbolicity can fail.
  Remark 4.9, p. 64 and p. 74 are the parameterised statements for (S8), (S11) and (S10).
- **New (S7)** (P-S7-1): faithful except m1 (false sufficient condition) and n1; the reading "for all weights w′" of
  Definition 3.59 as weights of P × M matches p. 59's use.
- **lem:ii-a-3-1**, re-derived:
  (a) countable index set; disjoint slices give multiplicity, covering, transition and (1.6) bounds with p-uniform
  constants; weights, scaling and elliptic weights restrict; norm identity from (3.14) with slice-local cut-offs;
  k derivatives from the norm after Lemma 3.18; variable orders via (b).
  (b) restricted seminorms ≤ family seminorms; normalised cut-offs live in the slice; a weight of N_(P′) extended by 1 is
  a weight of P × M, so Definition 3.59's "all weights w′" gives the residual bounds; C_c^∞(N_(P′)) = finitely
  supported families, mapped to itself.
  (c) correct and measurability-free: an unbounded f gives (countable choice) p_ℓ with f(p_ℓ) ≥ ℓ; f = ∞ somewhere
  is the case of a one-point subset.
  (d) BE = I − R^J with B = Σ_(j<J) R^jB_0 is right; R ∈ Ψ^(−1/2,−1/2) from (4.10) with δ = ¼; E′R^J maps
  wρ^(inf 𝗅)H^(inf 𝗆) into H^(𝗆″,𝗅″), 𝗆″ ≥ J/2 − (sup 𝗆 − inf 𝗆) ≥ 1 and likewise 𝗅″, under the stated condition on J.
  (e) the translation of the cut-off hypotheses into WF′(B_(P′)) ⊂ Ell(A_(P′)) on 𝔐 is right (aq − 1 = y_3 − 1 is a
  standard S⁰ symbol, so j applies even for variable orders); slice extension, (a) and (c) give uniformity. Subject
  to m5.
  (f) the scaling condition with C²C_γ; same 𝒱 (ratios ρ̃/ρ constant per cell); ξ = Dξ̃ with D = diag(ρ/ρ̃); same
  S^m and S^m_(1−δ,δ); quantisation kernels identical after ξ̃ = D⁻¹ξ; ‖f ∘ D⁻¹‖_(H^s) = |det D|^(1/2)‖⟨D⁻¹η⟩^s f̂‖
  within C^(±(n/2+|s|)); densities within C^(±n); residual classes equal; change of scaling weight via
  (ρ′/ρ)^(±𝗅) ∈ S⁰ and of weight via (w/w̃)E. All correct.
- **Ell**: the literal reading of def:i-b-2-9 at a fibre-infinity point over h_1 > 0 (U ⊂ {h > h_1/2}, h_0 = h_1/2)
  is vacuous, and (c) then fails (A = 0, G = I, B elliptic at fibre infinity over h ∈ [½, 1)). The corrected Ell
  agrees with def:i-b-2-9 at points over sf (U ∩ {h < h_0} is again a neighbourhood). The slice h = 1 is needed for
  "𝒫_ι is compact" (with [0, 1)_h fibre infinity is not compact).
- **P-S7-5**: every step checked: closedness of WF′(B), the finite cover and the bound for (ga)⁻¹ on O, the nested
  y_j, y_3(ga)⁻¹ ∈ S^(−𝐦′) by (d), the cover of supp(1 − y_1) by neighbourhoods off WF′(B) and by {ρ_sf > δ,
  |ζ| < C_0} via (f) (i), the partition of unity, ρ̄ ≍ ρ_sf, the remainder comparison for N ≥ K − inf 𝗌, K − inf 𝖻.
- **P-S7-6** on c/2 ≤ |σ| ≤ 1: the ratios ρ_scf⟨x⟩ ∈ [1/(1 + |σ|), 1/|σ|] ⊂ [½, 2/c], hρ⟨x⟩ = 1/|σ|, scalings
  within 2/c, ρ_tf bounded above and below, b-derivatives of the logarithms bounded; (f) and (d) apply. Subject to m3
  and n2.
- **Other sites**: 23:776–778 (lem:ii-a-7-1: with B = I the parametrix of lem:ii-a-8-4 (b) needs only family
  quantisation, Theorem 3.51 verbatim, the principal symbol of Definition 3.59 and boundedness, with Remark 4.9);
  lem:ii-a-7-3 and 33:1703–1704 use only lem:ii-a-7-1; 27:366 (Definition 1.9); 27:450 (P-S7-4, fine); chapter 33's
  eleven sites (only 1516 uses the sufficient condition, m1). No other (S7) citation exists (grep of all chapters,
  including (S·) ranges). No other proof file touches these labels.
- **Item 4 (locality)**: decided: not proved, as the chapter stands or after this file (M1).

## Placement checks (scratch only)

Scratch: /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rps7/
(tree/ = git archive of HEAD 52609127 with P-S7-1 to P-S7-11 and the section 7 crosswalk rows applied; tree2/ = the same
plus M1 (i)–(v)).
- Every old text occurs exactly once as whole lines at HEAD 52609127, at the stated lines (23:367, 466; 27:408, 450,
  460; 37:822; 95:914, 956, 989, 1130, 1135). Chapter 95 is unchanged since a8ecdce7 (the P-F123 edits to it landed
  in snapshot 9fe993fc, before the file's base); md5 bdbfff695b2f66f6022311c52e9e4820 at HEAD. No two items overlap.
- Every crosswalk old row occurs once; new rows have 4 tab-separated fields.
- tree/: before, lint --chapters 4833 labels 0 hits, assemble --check 0 problems; after, 4834 labels, 0 hits,
  0 problems; assemble.py and lint.py --paper: 0 hits; lem:ii-a-3-1 assembles as Lemma 14.15; longest line of
  chapters 23, 27, 37, 95 and of PAPER.md 121 characters (counted as characters).
- New texts: no line over 121 characters, none over 121 with each [[kind:key]] replaced by "Proposition 33.123", no
  wrapped line starting with "+ ", "- ", "* ", "> ", "#", "=", "|" or "<", no backtick, no backslash.
- tree2/ (with M1): 4834 labels, lint 0 hits, assemble --check 0 problems, PAPER.md 0 hits, longest line 121.
- assemble.py was not run in the repository; no repository file was written.

## Confirmation (fix round: proofs/P-S7.md md5 0571d41d9f9ff4f7999f4f76dd73eb55, 1447 lines; report notes/reports/F-P-S7.md)

**NOT CONFIRMED: 0 Major, 1 minor (new, not raised in round 1), 3 nits.** Every finding of round 1 (M1, m1–m5,
n1–n7) is resolved as proposed or better. I read every changed and new line, using a diff against 16e6e03f (904
changed lines). The one open item is a further site of the m3 kind, at 28:212. I missed it in round 1 too. Its
replacement text is below and passes a scratch merge.

### Round-1 findings, one by one

- **M1 (i)–(ii), lem:ii-a-3-1 (g)** (P-S7.md 587–589, 665–681): the statement is as proposed. The proof is as proposed,
  with 𝔐 and j now introduced in it and three properties of j stated: j(fg) = j(f)j(g), j(f̄) is the conjugate, and
  j(ψ(f)) = ψ(j(f)) for real f. Each holds by continuity on the dense subset. "Entrywise for matrices ((S14))" is
  added. Re-checked line by line: correct.
- **(S16) where cited**: thm:std-sbg-calculus (95:913ff.) has the item "(S16) Residual operators, essential supports and
  wave front sets" (95:1093). It quotes Definition 3.25 (u𝒱T*M, j, 𝔐, the essential support), Lemma 3.24 (1) and
  Definition 3.43 (WF′ = ess supp), which is all that (g) takes from it. The first mention is qualified, "(S16) of
  [[thm:std-sbg-calculus]]", and the second, a sentence later, is "((S16))". This is unambiguous, and chapter 33 cites
  "(S16)" the same way. Correct.
- **M1 (iii), weighted WF′** (P-S7-3, 715–717): "For A ∈ Ψ^𝐨 (the order being the one at which A is considered) ... with
  S^(𝐨−K𝐞)". This is correct and consistent with [Hin26d]'s WF′^w. **The writer's claim about the uses** is checked and
  true.
  - Outside the transferred chapter-21 proofs, chapter 27 takes WF′ or "microsupported" only of operators of order 0:
    27:427 (B ∈ Ψ⁰), 27:600 and 622 (B_*), 27:633 (B), 27:921 (G). In each case it is Ψ⁰ through (D2), and the
    transferred statements say B, B_* ∈ Ψ^0 (21:682, 21:738, 21:918).
  - Inside the transferred proofs (Ǎ ∈ Ψ^𝐤, E, J, R), chapter 21's "S^(−M𝟏) for every M" equals "S^(𝐨−M𝟏) for every
    M", so the weighted condition is the faithful transport.
  - Elsewhere, only chapter 35 uses this WF′, and only through prop:ii-f-2-4 to 2-6 (35:851–912). Its own WF′ at
    35:269–384 and 35:805 belongs to the cone calculus and to the chapter-21-type semiclassical calculus (orders
    (s, 𝖻), h⁻¹), not to 𝒫_ι.
  - grep finds no other chapter citing sec:ii-f-2, lem:ii-f-2-2, prop:ii-f-2-x or 𝒫_ι, except chapter 28 (see m6).
- **M1 (iv), lem:ii-f-2-2 (h)** (P-S7-14, P-S7-15): as proposed, with the cut-offs cited from lem:ii-f-2-phase. The ∎
  moved correctly. Correct.
- **M1 (v), prop:ii-f-2-3** (P-S7-16): as proposed. **M1 (vi)**: crosswalk notes for lem:ii-a-3-1, sec:ii-f-2-1,
  lem:ii-f-2-2 and prop:ii-f-2-3 are present (checked in full). The last sentence of (S7) names (g).
- **m1**: P-S7-1, lines 500–501, and P-S7-18 (33:1515–1516) are as proposed; the crosswalk row of
  lem:iv5-calc-structure is noted. Correct.
- **m2**: (b) no longer claims a phase-space-weight class, and its proof cites "((S4), (S8))". Correct.
- **m3**: P-S7-6, lines 835–842, is as proposed. Correct.
- **m4**: P-S7-13 is as proposed; the fifth line is the tail of the old line 445. Correct.
- **m5, option (b)**: (e) is proved by a parametrix (P-S7.md 620–641). Re-derived step by step.
  - z_k := φ_k(y_2) ∈ S⁰. Then y_1z_0 = y_1 (y_2 = 1 where y_1 ≠ 0), and z_kz_(k+1) = z_k, because z_k ≠ 0 forces
    |y_2 − 1| < 2^(k−3K−1), where z_(k+1) = 1. Also z_(3K)y_3 = z_(3K), because |y_2 − 1| < ½ forces y_2 ≠ 0, hence
    y_3 = 1. Iterating gives z_(3j+1)z_(3K) = z_(3j+1).
  - (1 − z_0)b = (1 − z_0)(1 − y_1)b is residual. qa = y_3, so the principal symbol of Q_jA is z_(3j+1)r_j, and
    R_(j+1) has principal symbol (1 − z_(3j+1))(1 − z_(3j))r_j, which is residual. With the class of (4.10) at δ = ¼
    this gives R_(j+1) ∈ Ψ^(−(j+1)/2,−(j+1)/2). The symbol r_(j+1) = r_j − c_j stays in the class of R_j, so it
    represents the principal symbol, as needed.
  - (1 − z_(3j+3))r_j is residual, since z_(3j)z_(3j+3) = z_(3j). (1 − z_(3j+3))c_j is residual by (g) with A := Q_j,
    B := A, y := 1 − z_(3j+2) and y′ := 1 − z_(3j+3). Here ya = (1 − z_(3j+2))z_(3j+1)r_jq = 0 and yy′ = y′; (g) holds
    for every symbol c_j of the product. All indices stay ≤ 3K.
  - Telescoping gives B = QA + R_K. The bound follows from the boundedness of Q ∈ w′⁻¹Ψ^(−𝗆′,−𝗅′) and
    R_K ∈ Ψ^(−K/2,−K/2) ((S7) with Remark 4.9). The remainder comparison is right: 𝗆 − K/2, 𝗅 − K/2 ≤ −N, the first
    term of the variable-order norm is dominated by the (−N, −N)-norm, and the elliptic family maps that space into
    H^(𝗋,𝗋′) ⊂ ρ^(inf 𝗋′)H^(inf 𝗋) ⊂ L². Regularity is included. Matrices work in the order (z r_j q)a with
    qa = y_3 Id.
  - **No circularity.** The proof of (g) uses only (b), (c), (S5), (S16) and (S14). The proof of (b) uses only the
    constant-order part of (a). The variable-order part of (a) uses (b). (d), (f) and (g) do not use (e). The proof of
    (e) cites (g) forward, with "whose proof does not use (e)". No proof of lem:ii-a-3-1 cites lem:ii-a-8-4.
  - Proposition 3.55 (3) is no longer used, so (e) holds for variable orders, the (S8) classes and systems without an
    unstated reading.
- **The two old sites now cite (e).**
  - P-S7-12 (old 23:1052–1054, 5 new lines): Λ := Op(λ^(−𝗌−1)) is in C^∞_bΨ^(𝗌+1)_e3b, which by 23:513 is the class of the structure, and
    its symbol has the inverse λ^(𝗌+1) ∈ S^(−𝗌−1). (e) applies with P a point, B = I and y_j = 1. The remainder
    ‖v‖_(ρ^(−N)H^(−N)) is ≤ C‖v‖_(H^(−N)) since ρ ≤ 1. Correct.
  - P-S7-17 (old 27:1432–1440, 13 new lines): at fixed σ the scalings, and hence ρ̄, are bounded below. y_j = ψ_j(λ) are nested, and
    1 − y_1 vanishes where λ < (a constant), so it is residual. On {λ < δ}, |p| ≥ cx_I²ρ_K⁻²λ⁻² (eq:ii-f-1-10 near ℐ⁺,
    the b-symbol near K⁺, lower-order terms absorbed for δ small), so y_3p⁻¹ ∈ x_I⁻²ρ_K²S^(−2). Correct.
- **n1** applied (511–513). **n2** applied (827–830). **n3** applied (710–711, 718–721): the h = 1 slice is not a face,
  its scope reaches *Orders and spaces*, Ell does not depend on the representative, and the principal symbol is "defined
  below". **n4** applied (597). **n6** applied (section 1, lines 72–73). **n7** recorded (§6.3).
- **n5, lem:ii-f-2-phase** (P-S7.md 725–751): re-derived.
  - The 𝒱_ħ-spanning fields are local frames of a smooth bundle over Y = ι⁺_ħ. Near sf ∩ tf the K⁺-frame is
    (ĥ/(1 + ĥ))(R∂_R − ĥ∂_ĥ) and (ĥ/(1 + ĥ))∂_ω, which is smooth.
  - On U × B̄⁴, ∂_ζ^γ = ⟨ζ⟩^(−|γ|)Σc_α(⟨ζ⟩∂_ζ)^α with c_α smooth, so |V_1⋯V_k∂_ζ^γ f| ≤ C⟨ζ⟩^(−|γ|).
  - The b-fields at fixed h lift smoothly to Y, being tangent to {h = 0} and to the blow-up centre.
  - ρ_i∂_(x^i) = ΣD_(ik)F_k, with D and D⁻¹ uniformly bounded with their ∂_x-derivatives: both are frames of 𝒱_ħ, the
    F_k by *The structure* and the chart frame by (S1). Then ξ = Dζ and ⟨ξ⟩ ≍ ⟨ζ⟩.
  - The induction invariant |ν| ≥ |μ| + |γ| is preserved by each derivative: ∂_ξ lowers |μ| or raises |ν|; ∂_x
    differentiates c, adds a field, or raises |μ| and |ν| together.
  - Hence |∂_x^β∂_ξ^γ f̃| ≤ C⟨ξ⟩^(−|γ|), uniformly in h and in the cell. Correct.
  - It is cited in (c) (P-S7-5) and (h). The new label assembles as Lemma 18.7. No chapter refers to a result of
    chapter 18 by a written-out number, so the renumbering of the later lemmas is harmless.

### Open finding

**m6 (minor, new). 28:212 asserts a uniform equivalence of norms over a compact range of the parameter, which
[Hin26d] does not give and sec:ii-f-2-1 states only at fixed h.** Chapter 28 (unchanged by P-S7), line 212, in the
proof of prop:ii-f-6-2:

> ‖·‖_(𝐨;k,+) at h = |ζ|⁻¹ ∈ [h_0, 1] are equivalent to the 0,b-norms uniformly ([[sec:ii-f-2-1]]), and

What is wrong:
- sec:ii-f-2-1 says (27:405–406) "For fixed h > 0, H^𝐨 is the space H^(𝗌,(a,c))_(0,b)(ι⁺) with an h-dependent
  equivalent norm". Uniformity over h ∈ [h_0, 1] for the variable orders 𝗌_(0ħ,cħ), 𝖻_± against 𝗌_(0,b) is not stated
  there.
- It is the same kind of statement as 37:824 (Remark 3.57: norms of different structures need not be uniformly
  equivalent). Before P-S7 it could only have rested on the blanket "the above holds uniformly in p" of the old (S7).
- It is used: the bound on the line for 1 ≤ |ζ| ≤ h_0⁻¹ needs it.

Fix: a new placement item for chapters/28-s09-forward.md, replacing line 212 (one whole line, occurring once at HEAD
31ee2458; chapter 28 md5 6e4db0694c74fad4469257bec90c24cf) by 7 lines:

```text
‖·‖_(𝐨;k,+) at h = |ζ|⁻¹ ∈ [h_0, 1] are equivalent to the 0,b-norms uniformly, by [[lem:ii-a-3-1]] (f) and (d):
for these h the cells are those of the 0,b-structure, with scalings within a factor depending only on h_0 and γ_+ of
its own; ρ_sf and ρ_tf lie between positive constants and ρ_cf ≍ ρ_K ([[sec:ii-f-2-1]]), so the weights and the
sf-order change the norms only to equivalent ones; 𝗌_(0ħ,cħ) and 𝗌_(0,b), induced by the same 𝗌, agree at fibre
infinity ([[sec:ii-f-1-3]]), so that λ^(𝗌_(0ħ,cħ)−𝗌_(0,b)) and its inverse are bounded in S⁰ (the exponent is λ times
a function bounded in S⁰, and λ log λ is bounded with its derivatives); and the factors h^(−j) of ‖·‖_(𝐨;k,+) lie
between 1 and h_0^(−k). Moreover
```

- The next line, "𝒴^(𝗌_(0,b)−2)_k ⊃ H^((𝗌_(0,b)−1;k),(2γ_I+2,γ_cf−2))_(0,b;b) continuously. ...", is unchanged; it now
  follows "Moreover".
- Crosswalk 28-s09-forward.tsv, row prop:ii-f-6-2 (its note is empty): add the note "P-S7: the uniform equivalence for
  h in [h_0, 1] justified by lem:ii-a-3-1 (f), (d)".
- The writer should confirm one point against sec:ii-f-1-3 and [Hin26c, §10.1.1], which that section cites: that
  𝗌_(0ħ,cħ) at fibre infinity over h > 0 and 𝗌_(0,b) are the same restriction of 𝗌. They are, if the spectral
  restriction of a dilation-invariant order is read at fibre infinity, where the τ-dual component drops out. If they
  were not, the sentence as printed would be false, not merely unproved.
- The sf-order is harmless because ρ̄ ≍ ρ_sf is bounded below for h ≥ h_0. Then ρ̄^(±𝖻) ∈ S⁰, as in the last sentence of
  lem:ii-a-3-1 (f), with log ρ_sf of bounded derivatives (lem:ii-f-2-1 (b)).
- Scratch check (tree5 = tree4 plus this item): lint --chapters 4930 labels, 0 hits; assemble --check 0 problems;
  PAPER.md 0 hits; longest line 121. Each new line is ≤ 121 characters, also with every [[kind:key]] replaced by
  "Proposition 33.123", and none starts with a forbidden character.

A grep for other uniform-equivalence claims ("equivalent … uniform" in chapters 20–39) found only sites proved on the
spot by comparing cells (23:659, 23:1089, 23:1435, 23:2372, 27:1006, 33:1523), sites of the h-independent spanning set
(27:1074–1078, covered by the boundedness in (S7)), chapter-21-calculus sites (21:438, 21:1128, 29:1090, 29:1206) and
31:615 (smoothness in a Kerr parameter b). None is an (S7) site.

### nits (this round)

- **N1.** P-S7-3, line 710: "here, in the paragraph *Orders and spaces* above and below, ι⁺_ħ and ..." reads as if the
  paragraph were both above and below. Suggested: "here and below, and in the paragraph *Orders and spaces* above,
  ι⁺_ħ and ...". The line stays under 121 characters after rewrap.
- **N2.** Notes only: sections 1 (line 42), 3 (ii), 6.4 and 9 give 27:1432–1436 for the site of P-S7-17. P-S7-17
  replaces 27:1432–1440.
- **N3.** (e), line 620: "Fix K ∈ ℕ." Its condition, K/2 ≥ N + |sup 𝗆| + |sup 𝗅|, appears only at line 637. Saying
  "Fix K ∈ ℕ with K/2 ≥ N + |sup 𝗆| + |sup 𝗅|" up front reads more easily. No change to the mathematics.

### Placement and checks (fix round)

- HEAD moved during the reading (b657322f → 31ee2458). The chapters 23, 27, 33, 37 and 95 and their crosswalks have
  the md5s the file states at both. Scratch tree4 is git archive of 31ee2458:
  /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rps7/tree4/
- All 18 old texts occur exactly once as whole lines, at the stated lines, with no overlaps: 23:367, 466, 1052;
  27:408, 441, 444, 450, 460, 489, 552, 1432; 33:1515; 37:822; 95:914, 956, 989, 1130, 1135. All 10 crosswalk old rows
  occur once. The new rows have 4 fields and are ASCII; the line ranges 540–681 and 725–751 match the two lemmas in
  P-S7.md.
- Before: 4928 labels, 0 hits, 0 problems. After P-S7-1 to P-S7-18 and the crosswalk rows: lint --chapters 4930
  labels, 0 hits; assemble --check 0 problems; assemble.py and lint --paper 0 hits. The longest line of PAPER.md and of
  each changed chapter is 121 characters.
- New texts: none over 121 characters. With every [[kind:key]] replaced by "Proposition 33.123", only the two kept old
  lines 27:552–553 exceed it, and their real expansions are shorter. No wrapped line starts with a forbidden character;
  no backtick or backslash. lem:ii-a-3-1 → Lemma 14.15 and lem:ii-f-2-phase → Lemma 18.7.
- The scratch chapter md5s after the merge equal those the file states for its own scratch merge:
  488db29e…, b30eac97…, 4b866436…, f803ece3…, 8060f7c5….
- assemble.py was not run in the repository. No repository file was written.
