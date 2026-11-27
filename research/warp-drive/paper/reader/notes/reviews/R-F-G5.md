# R-F-G5: independent reading of the G5 re-sourcing ([HJS] → [Mel94]) and its companion items

Reader's review, 2026-11-20. Diff read: `git diff 796714d8 9467a875` on chapters 03, 20, 21, 22, 23, 32, 35, 95, 98
(the unrelated hunks in 95 and 98 — thm:std-sbierski item (7), thm:std-duffin-schaeffer, [DS41] — were ignored).
Working tree of `chapters/` is clean against 9467a875, so line numbers below are those of the current files.

**Verdict: NOT CONFIRMED.** No Major issue. Five minor issues (m1–m5) and eight nits (n1–n8). Every quotation, page
and equation number attributed to [Mel94], [Hin17] and [ABK20] checks out against the sources; the writer's reading of
the misprint in [Mel94, (5.16)] is correct. The minor issues are a dangling internal pointer caused by the restructuring
(m1), one justification that the change to the logarithmic class broke (m2), the (5.16) reading not being stated where
it is used (m3), an over-general commutator statement in (C6) (m4), and two calculus facts that chapter 20 uses under
the name "(C1)" but that (C1) does not state (m5; partly pre-existing).

Sources were saved under `scratchpad/reader/sources/`: `mel94.md` (full text, Firecrawl PDF parse), `mel94-pages.txt`
(text split by PDF page; each page ends with its printed number, confirming printed page = PDF page, 57 pages),
`hin17v2-pages.txt` (arXiv:1502.03183v2, 29 pages), `abk-v1-pages.txt` (arXiv:1904.03088v1, 16 pages). The PDFs
themselves could not be saved as bytes (the proxy refuses math.mit.edu and arxiv.org to curl), so the text was read
through the two fetch tools; formulas were checked in both extractions where one garbles them.

---

## Findings

### m1 (minor) — chapter 22 points to a paragraph that is no longer last

`chapters/22-s03-spectral-low.md:111`, current text:

    the scattering calculus is the classical one (last paragraph of [[sec:i-a-2-1]]). The uniformity comes from the proof

The paragraph meant ("In the interior, at fibre infinity, the scattering calculus restricted to kernels supported in a
compact set is the classical calculus …") was the last paragraph of sec:i-a-2-1 at 796714d8. It is now
`chapters/20-s01-spectral-bounded.md:272–275`, followed by the seven proof paragraphs (277–343), so "last paragraph" now
designates the proof of (C8). Proposed replacement (one line, 113 characters):

    the scattering calculus is the classical one (after (C8) in [[sec:i-a-2-1]]). The uniformity comes from the proof

### m2 (minor) — rem:i-a-3-3: the claim on b₀⁻¹ no longer follows in the logarithmic class

`chapters/20-s01-spectral-bounded.md:563–567`, current text (the hypothesis and the justification):

    Ψ^(2𝐬−𝟏+δ𝟏), while the other hypotheses hold as stated, κ < ½, and B₀ has principal symbol bounded below by c > 0
    times an elliptic weight of order 𝐬. Then the conclusion holds with the a priori term ‖Gu‖_(𝐬−κ𝟏). The proof is
    unchanged, except that (e) is bounded by C‖v‖²_(𝐬−½𝟏+δ𝟏) ≤ C‖v‖²_(𝐬−κ𝟏) for δ ≤ ½ − κ, and
    ‖Bu‖_𝐬 ≤ C(‖B₀u‖ + ‖u‖_(−𝐌)) for B microsupported in Ell(B₀): b₀⁻¹ is bounded by the inverse weight, so it is a
    symbol of order −𝐬 in the class of (C6). [[lem:i-a-3-2]] holds with this variant, since its steps have κ ≤ ¼. For

What is wrong. The variable-order class of (C6) is now the logarithmic class of def:i-b-2-1 at h = 1: |a| ≤ C w with no
logarithm, derivatives gaining their weights up to powers of 1 + log⟨x⟩ + log⟨ξ⟩. The remark assumes only that b₀ is
bounded in Ψ^(𝐬+δ𝟏) for every δ > 0 and |b₀| ≥ c w_𝐬. Then ∂(b₀⁻¹) = −b₀⁻¹(∂b₀)b₀⁻¹ is bounded only by
C_δ w_(−𝐬)·⟨x⟩^δ⟨ξ⟩^δ times the weight gained, a power loss, not a logarithmic one; so b₀⁻¹ is not shown to lie in the
class of order −𝐬, and the microlocal elliptic estimate at the order 𝐬 does not follow. (Under the old ⟨x⟩^(−δ)𝒱_b
class this loss was admitted by the class itself, which is why the sentence used to be right.) The only application,
prop:i-a-5-2 (1131–1134), is unaffected: there b_ε = μ^(1/2)ϱ^(−𝗄) · φ_εψ_ye^(−C_z z)χ_sχ_e · Q̃_ε^(1/2) has exactly the
form w φ Q^(1/2) of lem:i-b-2-12, which gives φ′b⁻¹ ∈ S^(−𝐨) and the elliptic estimate at the order 𝐨. Proposed
replacement for lines 563–567 (seven lines; line 568 "fixed ε, B_ε lies only …" follows unchanged):

    Ψ^(2𝐬−𝟏+δ𝟏), while the other hypotheses hold as stated, κ < ½, and B₀ has principal symbol w φ Q^(1/2) of the form of
    [[lem:i-b-2-12]] at h = 1, with w an elliptic weight of order 𝐬 and φ a scalar symbol of order 0. Then the conclusion
    holds with the a priori term ‖Gu‖_(𝐬−κ𝟏). The proof is unchanged, except that (e) is bounded by
    C‖v‖²_(𝐬−½𝟏+δ𝟏) ≤ C‖v‖²_(𝐬−κ𝟏) for δ ≤ ½ − κ, and ‖Bu‖_𝐬 ≤ C(‖B₀u‖ + ‖u‖_(−𝐌)) for B microsupported in an open
    set on which φ ≥ c > 0: there, by [[lem:i-b-2-12]] at h = 1, φ′b₀⁻¹ is a symbol of order −𝐬 in the class of (C6) for
    φ′ ∈ S^(0,0)_sc supported in that set, and the microlocal elliptic estimate holds for B₀ at the order 𝐬.
    [[lem:i-a-3-2]] holds with this variant, since its steps have κ ≤ ¼. For

(In lem:i-a-3-2, read with this variant, "B₀ elliptic on Ū′" and "WF′(𝒢_j) ⊂ Ell(B₀^(j))" then mean φ ≥ c there; in
prop:i-a-5-2, φ = 1 on γ([0, t₁]).)

### m3 (minor) — the reading of [Mel94, (5.16)] is not stated where it is used; (5.18) needs a classical symbol

`chapters/20-s01-spectral-bounded.md:216–219`, current text:

    (C2) (Commutators.) For A ∈ Ψ^(m₁,ℓ₁)_sc and B ∈ Ψ^(m₂,ℓ₂)_sc, [A, B] ∈ Ψ^(m₁+m₂−1,ℓ₁+ℓ₂−1)_sc, since the principal
    symbols commute, and σ(i[A, B]) = {σ(A), σ(B)} [Mel94, Proposition 4, (5.16), p. 18], a symbol of order
    (m₁ + m₂ − 1, ℓ₁ + ℓ₂ − 1) [Mel94, Lemma 5, (5.18), p. 18]. Here {a, b} = ∂_ξa·∂_xb − ∂_xa·∂_ξb = H_ab is the
    Poisson bracket of T∗ℝⁿ [Mel94, (5.22), p. 19]. If a is ⟨ξ⟩^(m₁)⟨x⟩^(ℓ₁) times a function smooth on the

`chapters/95-standard-results.md:824–826`, current text:

    By (5.18) the bracket in (5.16) has the orders (m1 + m2 − 1, l1 + l2 + 1), and by (5.13)–(5.14), the symbols commuting,
    [A, B] ∈ Ψ^(m1+m2−1,l1+l2+1)_sk(X). The decay order l of [Mel94] has the sign opposite to that of [[sec:i-a-2-1]], where
    Ψ^(m,ℓ)_sc is Ψ^(m,−ℓ)_scc(S^n_+) and H^(s,r)_sc is the space of (6).

What is wrong. (5.16) is printed with j_(sc,m1+m2,l1+l2)([A, B]) on the left (both extractions agree). At those
indices both sides vanish: the left by (5.14) (commutative values), the right because the bracket lies in
A^(m1+m2−1,l1+l2+1), which (5.12) divides out. So (5.16) has content only with j_(sc,m1+m2−1,l1+l2+1), and that is the
reading (C2) uses ("σ(i[A, B]) … a symbol of order (m₁ + m₂ − 1, ℓ₁ + ℓ₂ − 1)"). The writer's report states this reading,
but neither the paper's (C2) nor the Appendix A entry says it: the closing sentence of thm:std-melrose-sc proves the
orders and stops before the conclusion, so a reader who checks (C2) against the quoted (5.16) finds a different
statement. Two smaller points in the same sentences: (5.18) is stated for classical a ∈ C^∞(^(sc)T̄^∗X; S^(m,l)) while
(C2) concerns the scattering-conormal class (for which the orders follow from the bracket formula by the symbol
estimates); and for sk = sc the kernel statement is (5.10), not (5.13). Also (5.22) is written in coordinates (x, y) near
the boundary, x a boundary defining function, not in the coordinates x of ℝⁿ used in (C2). Proposed replacement for
ch. 20 lines 216–219 (six lines; line 220 "compactified phase space, then H_a is …" follows unchanged):

    (C2) (Commutators.) For A ∈ Ψ^(m₁,ℓ₁)_sc and B ∈ Ψ^(m₂,ℓ₂)_sc, [A, B] ∈ Ψ^(m₁+m₂−1,ℓ₁+ℓ₂−1)_sc, since the principal
    symbols commute, and σ(i[A, B]) = {σ(A), σ(B)}, a symbol of order (m₁ + m₂ − 1, ℓ₁ + ℓ₂ − 1) [Mel94, Proposition 4,
    (5.16), p. 18], read at these orders ([[thm:std-melrose-sc]]: as printed, (5.16) carries the orders (m₁ + m₂, ℓ₁ + ℓ₂),
    at which both of its sides vanish). Here {a, b} = ∂_ξa·∂_xb − ∂_xa·∂_ξb = H_ab is the Poisson bracket of T∗ℝⁿ, which
    [Mel94, (5.22), p. 19] writes in coordinates near the boundary; the order of {a, b} follows from it by the symbol
    estimates. If a is ⟨ξ⟩^(m₁)⟨x⟩^(ℓ₁) times a function smooth on the

and for ch. 95 lines 824–826 (six lines):

    By (5.18), and for a conormal a by the same count of derivatives in (5.22), the bracket in (5.16) has the orders
    (m1 + m2 − 1, l1 + l2 + 1); and by (5.10), (5.13) and (5.14), the symbols commuting, [A, B] ∈ Ψ^(m1+m2−1,l1+l2+1)_sk(X).
    So (5.16) is read, and used in [[sec:i-a-2-1]], with j_(sc,m1+m2−1,l1+l2+1)([A, B]) on its left side: with the
    subscripts as printed both of its sides vanish, the left by (5.14) and the right by (5.12). The decay order l of [Mel94]
    has the sign opposite to that of [[sec:i-a-2-1]], where Ψ^(m,ℓ)_sc is Ψ^(m,−ℓ)_scc(S^n_+) and H^(s,r)_sc is the space
    of (6).

### m4 (minor) — (C6) states the commutator gain for all matrix-valued operators

`chapters/20-s01-spectral-bounded.md:252–254`, current text:

    amplitude modulo the class of order (m − 1 + δ, 𝗅 − 1 + δ) for every δ > 0; it is multiplicative; σ(A∗) = σ(A)∗; and
    [A, B] has order (m + m′ − 1 + δ, 𝗅 + 𝗅′ − 1 + δ) for every δ > 0, with σ(i[A, B]) = H_aσ(B) if σ(A) = a Id is
    scalar. Operators of order (0, 0) are bounded on L² ([[thm:i-b-2-7]] at h = 1). For constant s, a variable order 𝗋,

What is wrong. (C6) defines S^(m,𝗅)_sc as a space of *matrix* functions (line 244). For non-commuting matrix symbols the
first term (ab − ba) of the commutator does not vanish and [A, B] has order (m + m′, 𝗅 + 𝗅′) only; eq:i-b-2-5 gives the
gain only when a is scalar modulo lower order. As written, only the formula for σ(i[A, B]) is conditional. Every use in
chapter 20 has A of scalar principal symbol (Ǎ_ε at 485; the T_t of (C8)), so nothing downstream breaks. Proposed
replacement for lines 252–254 (four lines; line 255 "E := Op(⟨ξ⟩^s⟨x⟩^𝗋 Id) and …" follows unchanged):

    amplitude modulo the class of order (m − 1 + δ, 𝗅 − 1 + δ) for every δ > 0; it is multiplicative; σ(A∗) = σ(A)∗; and
    if σ(A) = a Id is scalar, [A, B] has order (m + m′ − 1 + δ, 𝗅 + 𝗅′ − 1 + δ) for every δ > 0, with
    σ(i[A, B]) = H_aσ(B). Operators of order (0, 0) are bounded on L² ([[thm:i-b-2-7]] at h = 1). For constant s, a variable
    order 𝗋,

### m5 (minor; partly pre-existing) — two facts used as "(C1)" are not in (C1)

(a) `chapters/20-s01-spectral-bounded.md:464–466` (lem:i-a-3-1, Step 0), current text:

    … So if W_ε is any family bounded in
    some Ψ^𝐭 and microsupported in K₁ uniformly, then W_ε[P, Φ] and W_ε(Id − Φ) are bounded in Ψ^(−∞,−∞) (by the
    composition formula (C1): the product of the symbols vanishes, and the remainders are bounded by seminorms). In

The new (C1) (209–214) states only the inclusion [Mel94, (5.1)], the principal symbol, Lemma 6 and adjoints; it has no
composition formula, no seminorm bound and no disjoint-support statement. ([Mel94, (5.1)] is an inclusion only.) The
facts are available — thm:i-b-2-4 at h = 1 and consequence (iv) after thm:i-b-2-5 — and (C6) and the (C8) proof already
invoke them, but (C1), the item cited, does not carry them. The old (C1) did not either, so this is pre-existing; it is
reported because (C1)–(C8) are now the statement list of what chapter 20 proves or cites.

(b) `chapters/20-s01-spectral-bounded.md:1054` (prop:i-a-5-1, "The construction is continuous in the symbol, so its
seminorms are uniform on 𝒟"), `392–393` (lem:i-a-2-3, "The construction depends continuously on K"), and through them
thm:i-a-8-1 (1666: "Every constant above is produced by finitely many seminorms") and ch. 22 (K2) (111–112). These
constructions use the asymptotic sums of (C1), which cite [Mel94, Lemma 6]; Lemma 6 asserts existence only, with no
bound or continuity in the summands. The new (C5) proof (301–308) inherits this: B := B₀C with C ∼ Σ_j (−R₀)^j. So the
continuity/uniformity claims are not covered by what (C1)–(C8) now state or prove. (Also pre-existing; [HJS] was cited
for existence only.) The standard Borel construction closes it in a few lines.

Proposed replacement for ch. 20 lines 212–214 (seven lines; line 215 is the blank line before (C2)):

    (5.11)–(5.14), p. 17]. For a ∈ S^(m,ℓ)_sc and a′ ∈ S^(m′,ℓ′)_sc, Op(a)Op(a′) = Op(a#a′) by [[thm:i-b-2-4]] at h = 1,
    where a#a′ − Σ_(|α|<N) (1/α!) ∂_ξ^α a D_x^α a′ lies in S^(m+m′−N+δ,ℓ+ℓ′−N+δ)_sc for every N ≥ 1 and δ > 0, each
    seminorm of a#a′ and of this remainder being bounded by a product of seminorms of a and a′; so if a vanishes on an open
    set U, a#a′ and a′#a are of order (−∞, −∞) on every open set with closure in U. If A_j ∈ Ψ^(m−j,ℓ−j)_sc for j ∈ ℕ₀,
    there is A ∈ Ψ^(m,ℓ)_sc with A − Σ_(j<N) A_j ∈ Ψ^(m−N,ℓ−N)_sc for every N [Mel94, Lemma 6, p. 20]; if the A_j depend
    on a parameter b and are bounded in their classes, A can be chosen bounded in Ψ^(m,ℓ)_sc, with A − Σ_(j<N) A_j bounded
    in Ψ^(m−N,ℓ−N)_sc, and continuous in b if the A_j are. A ∈ Ψ^(m,ℓ)_sc ⇒ A∗ ∈ Ψ^(m,ℓ)_sc, with σ(A∗) = σ(A)∗.

New paragraph after line 280 (after the *Adjoints (C1)* proof, before *Seminorm bounds (C3)*):

    *Uniform asymptotic sums (C1).* Let a_j^b be the amplitudes of the A_j, χ as in (C8), and ψ_t(x, ξ) := 1 − χ(tx)χ(tξ).
    As in the proof of (C8), ψ_t is bounded in S^(0,0)_sc for t ∈ (0, 1] and ⟨x⟩⟨ξ⟩ ≥ c/t on its support, so the
    seminorm of order k of ψ_t a_j^b in S^(m−j+1,ℓ−j+1)_sc is at most C_k t p_(j,k), where p_(j,k) is the supremum over b
    of the seminorm of order k of a_j^b in S^(m−j,ℓ−j)_sc and C_k increases with k. Choose t_j ∈ (0, 1] with
    C_j t_j (1 + p_(j,j)) ≤ 2^(−j). For each N and k, the terms with j > max(N, k) of a^b := Σ_j ψ_(t_j) a_j^b have
    seminorms of order k at most 2^(−j) in S^(m−N,ℓ−N)_sc, so the series converges there, uniformly in b. As
    (1 − ψ_t)a_j^b has compact support, a^b − Σ_(j<N) a_j^b is bounded in S^(m−N,ℓ−N)_sc for every N, and a^b is continuous
    in b if the a_j^b are, each partial sum being so. Op(a^b) is the sum A.

(The estimate used: on supp ψ_t, 1 ≤ (t/c)⟨x⟩⟨ξ⟩, and the derivatives of ψ_t are O(⟨x⟩^(−|α|)⟨ξ⟩^(−|β|)) uniformly in
t and supported in supp ψ_t, both shown in the (C8) proof at 335–337.) Replacement for line 308 (two lines):

    1 − δ in both orders. By the seminorm bounds and the uniform asymptotic sums of (C1), B depends continuously on the
    amplitude of A, and is bounded when A is bounded in Ψ^(m,ℓ)_sc and uniformly elliptic near K.

(The variable-order asymptotic sums of (C6) reduce to (C1) in constant orders, so they inherit the uniform version.)

### n1 (nit) — constant-order duality stops before its conclusion

`chapters/20-s01-spectral-bounded.md:298–299`:

    *Duality (C4).* With Λ_(s,r) := ⟨D⟩^s⟨x⟩^r, u ↦ Λ_(s,r)u is unitary from H^(s,r)_sc onto L² and v ↦ Λ_(−s,−r)v from
    H^(−s,−r)_sc onto L², and ⟨u, v⟩ = ⟨Λ_(s,r)u, Λ_(−s,−r)v⟩ for u, v ∈ 𝒮, since Λ_(−s,−r) = (Λ_(s,r)⁻¹)∗.

The steps are right, but the identification itself (extension of the pairing, Riesz) is left to the reader. Replacement:

    *Duality (C4).* With Λ_(s,r) := ⟨D⟩^s⟨x⟩^r, u ↦ Λ_(s,r)u is unitary from H^(s,r)_sc onto L² and v ↦ Λ_(−s,−r)v from
    H^(−s,−r)_sc onto L², and ⟨u, v⟩ = ⟨Λ_(s,r)u, Λ_(−s,−r)v⟩ for u, v ∈ 𝒮, since Λ_(−s,−r) = (Λ_(s,r)⁻¹)∗. So the
    pairing extends to H^(s,r)_sc × H^(−s,−r)_sc with |⟨u, v⟩| ≤ ‖u‖_(s,r)‖v‖_(−s,−r), 𝒮 being dense in both, and by the
    Riesz theorem in L² every bounded functional on H^(s,r)_sc is ⟨·, v⟩ for exactly one v ∈ H^(−s,−r)_sc, of equal norm.

### n2 (nit) — variable-order compactness: N must be admissible for the target pair

`chapters/20-s01-spectral-bounded.md:325–327`:

    E′ := Op(⟨ξ⟩^(s′)⟨x⟩^(𝗋′) Id). Then E′ is bounded from H^(s,𝗋)_sc to H^(τ,τ)_sc, which embeds compactly in L², and
    H^(s,𝗋)_sc ⊂ H^(−N,−N)_sc embeds compactly in H^(−N−1,−N−1)_sc by the constant case; with N + 1 in place of N in the
    norm of H^(s′,𝗋′)_sc, the embedding H^(s,𝗋)_sc ↪ H^(s′,𝗋′)_sc is compact. *Duality.*

N is only assumed ≥ max(−s, −inf 𝗋) + 1, but the norm of H^(s′,𝗋′)_sc needs N + 1 ≥ max(−s′, −inf 𝗋′) + 1, which fails
when s − s′ > 1 or 𝗋 − 𝗋′ is large. Harmless (the space does not depend on N), but should be said. Replacement:

    E′ := Op(⟨ξ⟩^(s′)⟨x⟩^(𝗋′) Id). Then E′ is bounded from H^(s,𝗋)_sc to H^(τ,τ)_sc, which embeds compactly in L². Take
    N ≥ max(−s′, −inf 𝗋′) + 1, admissible for both pairs; then H^(s,𝗋)_sc ⊂ H^(−N,−N)_sc embeds compactly in
    H^(−N−1,−N−1)_sc by the constant case, and with N + 1 in place of N in the norm of H^(s′,𝗋′)_sc, the embedding
    H^(s,𝗋)_sc ↪ H^(s′,𝗋′)_sc is compact. *Duality.*

### n3 (nit) — the sign remark covers amplitudes and operators, not Sobolev orders

`chapters/20-s01-spectral-bounded.md:194`: "half-sphere is ℝ̄ⁿ. [Mel94] measures decay with the sign opposite to ours."
The remark is correct for amplitudes and operators ([Mel94, (4.2)] weight (1 + |z|)^(−l); (5.3)); but [Mel94]'s Sobolev
index has our sign (H^(m,l)_sc = {u : Ψ^(m,−l)_sc u ⊂ L²}, (5.27)), as line 200 itself says. Read alone the sentence
suggests otherwise. Replacement for lines 194–196 (three lines):

    half-sphere is ℝ̄ⁿ. [Mel94] measures the decay of amplitudes and operators with the sign opposite to ours, while its
    Sobolev orders have our sign. We write S^(m,ℓ)_sc for the amplitudes with |∂_x^α ∂_ξ^β a| ≤ C_αβ ⟨x⟩^(ℓ−|α|) ⟨ξ⟩^(m−|β|),
    Op(a) for the operator with that kernel, and Ψ^(m,ℓ)_sc := Op(S^(m,ℓ)_sc), which is [Mel94]'s Ψ^(m,−ℓ)_scc; and

### n4 (nit) — [Mel94, (6.2)–(6.5)] is a construction for Δ + V − z

`chapters/20-s01-spectral-bounded.md:238`: "proved below; for elliptic A it is the construction of [Mel94, (6.2)–(6.5),
pp. 21–22]." [Mel94, (6.2)–(6.5)] build the parametrix of Δ + V − z only (Theorem 1). Replacement for lines 237–240:

    WF′(BA − Id) ∩ K = ∅; if A is elliptic everywhere, there is B with AB − Id and BA − Id in Ψ^(−∞,−∞)_sc. This is
    proved below; for elliptic A it follows the construction that [Mel94, (6.2)–(6.5), pp. 21–22] makes for Δ + V − z.
    Hence the microlocal elliptic estimate: if G, Q ∈ Ψ^(0,0)_sc and WF′(Q) ⊂ Ell(A) ∩ Ell(G), then
    ‖Qu‖_(s,r) ≤ C(‖GAu‖_(s−m,r−ℓ) + ‖u‖_(−M,−M)) for every M.

### n5 (nit) — "take χ = 1" needs a invertible in the interior

`chapters/20-s01-spectral-bounded.md:305`: "If A is elliptic everywhere, take χ = 1." Ellipticity is defined at boundary
points only, so a may vanish at finite points and Op(a⁻¹) is then undefined. The case is the one with K the whole
boundary. Replacement for line 305 (two lines; line 306 "operator for GA, …" follows unchanged):

    WF′ disjoint from K, so BA − Id has too. If A is elliptic everywhere, take for K the whole boundary of phase space:
    then 1 − χ has compact support and Id − Op(χ) ∈ Ψ^(−∞,−∞)_sc. For the estimate, let B be such an

### n6 (nit) — the identification with [Mel94]'s H^(s,r)_sc shows one inclusion

`chapters/20-s01-spectral-bounded.md:200–201` shows that ⟨D⟩^s⟨x⟩^r u ∈ L² implies [Mel94]'s condition; the converse
needs ⟨D⟩^s⟨x⟩^r itself to lie in [Mel94]'s classical Ψ^(s,−r)_sc, which holds by (5.1) (each factor's amplitude is its
weight times 1). Replacement for lines 200–201 (three lines; line 202 "Its statements hold …" follows unchanged):

    This is [Mel94]'s H^(s,r)_sc [Mel94, (5.27), p. 19]: ⟨D⟩^s⟨x⟩^r lies in [Mel94]'s Ψ^(s,−r)_sc by [Mel94, (5.1)], and
    every element of it is ⟨D⟩^s⟨x⟩^r followed by an operator of order (0, 0), which is bounded on L² by (C3). Pages of
    [Mel94] are those of the author's online edition.

### n7 (nit) — Appendix A header of thm:std-melrose-sc

`chapters/95-standard-results.md:768–771`: item (10) quotes (5.4), p. 16, and item (4) quotes (5.10), neither in the
bracketed list; (5.15)–(5.18) are quoted but only "(5.19)–(5.20)" is listed for p. 18; and "p." / "19" are split across
lines 769–770. Replacement:

    **Theorem {#thm:std-melrose-sc}** ([Mel94, (1.1), p. 4; (4.1)–(4.3) and Definition 1, pp. 12–13; Definition 2, p. 14;
    (5.1), p. 15; (5.4), p. 16; Proposition 3, (5.10) and (5.12)–(5.14), p. 17; Proposition 4, Lemma 5 and (5.15)–(5.20),
    p. 18; (5.22) and (5.27), p. 19; Proposition 5 and Lemma 6, p. 20; (5.34), p. 21; (7.1), (7.2) and (7.6), p. 23].)
    Let X be a compact manifold with boundary and x a boundary defining function.

### n8 (nit) — two small items in Appendix A and the references

(a) `chapters/95-standard-results.md:1189–1190` (thm:std-abk-holomorphy): the proof never says that g dominates ‖f‖,
which is the point. Replacement:

    A locally bounded f is locally L¹-bounded: if K_1 ⊂ K_2 ⊂ … are compact sets whose interiors exhaust Ω and K_0 := ∅,
    then g := Σ_j (sup_(K_j) ‖f‖) 1_(K_j ∖ K_(j−1)) is measurable, bounded on compact sets and ≥ ‖f‖_X on Ω, so
    g ∈ L¹_loc(Ω, ℝ).

(b) `chapters/98-references.md:147–150` ([Mel94]): Crossref gives doi:10.1201/9781003072096-5 as a chapter of the CRC
Press reissue of the volume, published 2020-12-17, pp. 85–130, title as printed. Placed directly after the 1994 Dekker
data, it reads as the original's DOI. The [Mel93] entry does the same, so this is house style; if it is to be precise:
"… Dekker, New York (1994), 85–130; reissued CRC Press (2020), doi:10.1201/9781003072096-5; author's corrected online
edition (1997), https://math.mit.edu/~rbm/papers/sslaes/sslaes1.pdf."

---

## What I verified and found correct

### [Mel94] — quotations, pages and equation numbers (chapter 20 and thm:std-melrose-sc)

Page boundaries taken from the per-page extraction; each page closes with its printed number, equal to the PDF index.
Checked one by one, all correct:

- (1.1) and the sentences "This is clearly an isomorphism … radial compactification. Indeed the function t_0 = … which
  is defined in t_0 < 1", p. 4; collar map giving (x, ω) = (1/|z|, z/|z|), p. 4. The extraction prints ";" and ":"
  after formulas: these are cmmi's comma and period (glyph slots 59 and 58), so the transcription with "," and "." is
  right.
- (4.1), p. 12; (4.2), its weight (1 + |z|)^(−l)(1 + |ζ|)^m, and (4.3) with "is a isomorphism" [sic], p. 13;
  Definition 1, p. 13, quoted verbatim; SP^∗ρ_N, SP^∗ρ_σ, p. 13; Definition 2, (4.7), and the "sk" sentence, p. 14.
- (5.1), p. 15 (for sk = sc or scc); (5.4), p. 16; Proposition 3 with its quoted clause, (5.10), (5.11)–(5.14), p. 17
  (the (5.13) and (5.14) quotations verbatim, including "with values in commutative algebras").
- Proposition 4 and (5.16), Lemma 5, (5.17), (5.18), (5.19), (5.20), p. 18; (5.22), (5.27) and the H^(m,0)_sc sentence,
  p. 19; Proposition 5, (5.28), Lemma 6, (5.29) and its uniqueness clause, (5.30), p. 20; (5.34), p. 21; (6.2)–(6.3),
  p. 21, (6.4)–(6.5), p. 22; (7.1), (7.2), (7.6), p. 23 (all on that page).
- "[Mel94] treats constant orders and states neither adjoints nor duality": a search of the whole text finds "adjoint"
  only for d, δ and Δ, never for pseudodifferential operators, and no duality statement for H^(m,l)_sc. Correct.
- The misprint: the writer's reading is right. Both extractions print j_(sc,m1+m2,l1+l2)([A, B]) in (5.16) (and (5.15)
  gives the bracket the unreduced target S^(m1+m2,l1+l2)), while (5.18) gives A^({m+m′−1,l+l′+1}). As printed, (5.16)
  is vacuous (both sides 0); the lowered indices are the only contentful reading. Only its statement in the paper is
  missing (m3).
- Sign convention: correct. With [Mel94]'s weight (1 + |z|)^(−l), the edition's Ψ^(m,ℓ)_sc is [Mel94]'s Ψ^(m,−ℓ)_scc;
  (5.28) A : H^(M,L) → H^(M−m,L+l) becomes H^(s,r) → H^(s−m,r−ℓ), matching (C3); (5.27) makes [Mel94]'s H^(m,l)_sc the
  edition's H^(s,r)_sc with the same letters (scope of the wording: n3). Also consistent with (5.3).
- Use of the classical-only statements: Proposition 5's compactness criterion and (5.10) are applied in (C4) to
  A^k = (⟨D⟩^(−δ/2)⟨x⟩^(−δ)⟨D⟩^(−δ/2))^k, which is classical (each factor's amplitude is its weight times 1; (5.1) for sc),
  of [Mel94]-order (−1, 1), so in ker j_(sc,0,0) = Ψ^(−1,1)_sc. Correct.
- Edition: math.mit.edu/~rbm/paper.html lists "Corrected, (Jan 15, 1997): … sslaes1.pdf", and "Edited by M. Ikawa,
  1994, Marcel Dekker"; Crossref confirms the chapter pages 85–130 and the title spelling "Euclidian".

### [Hin17] (arXiv:1502.03183v2, 29 pages, dated 27 May 2020)

Definition 3.8, p. 16, verbatim through "matrix of first order differential operators."; (3.3) is on p. 13; the
setting paragraph of Section 4 and Proposition 4.1 with (4.1), p. 20, verbatim; Theorem 4.8 and the sentence "By
restriction, the analogous statements are true for □ acting on subbundles of the tensor bundle on M, for instance
differential forms of all degrees and symmetric 2-tensors.", p. 26. Ch. 32's header "[Hin17, Proposition 4.1, p. 20] on
1-forms" is right: k = 1 of Δ_k = −tr∇², and the Ricci term of □_g = ∇*∇ − Ric is of order 0, so it does not enter the
subprincipal operator. The arXiv id added to [Hin17] makes ch. 38's page citations (773, 786) follow the stated policy.

### [ABK20] (arXiv:1904.03088v1, 16 pages)

"very weakly holomorphic" (p. 1) and "locally L¹-bounded" (pp. 1–2) quoted correctly, ellipses where "(very weakly
harmonic)" and "(harmonic)" are dropped; Theorem 1.1, p. 2, verbatim. Crossref: Illinois J. Math. 64 (2020), no. 3,
331–347, doi:10.1215/00192082-8591584, authors and title as in ch. 98. Ch. 35's use (a subspace of X* separating points
is a separating subset; locally bounded implies locally L¹-bounded, proved in the entry, n8 (a)) is correct.

### Chapter 20 proofs, line by line

Correct as written: the adjoint proof (thm:i-b-2-5 at h = 1, M = 4, remainder of log order (m − 2, ℓ − 2) ⊂
S^(m−1,ℓ−1)_sc; the α ≠ 0 terms are genuine symbols); the closed-graph seminorm bound (pointwise and 𝒮′ limits agree,
𝒮 dense since ⟨D⟩^s⟨x⟩^r maps 𝒮 onto 𝒮); compactness (A ≥ 0, A^k of order (−1, −1) compact, A = (A^k)^(1/k) a norm
limit of polynomials without constant term, the factorisation through J); the parametrix construction (AB₀ = Op(χ) + R₀,
Neumann series, Id − AB = (Id − Op(χ))C + E, the left/right comparison B′ − B = B′(Id − AB) − (Id − B′A)B, and the
estimate Q = QBGA + Q(Id − BGA), with GA elliptic on Ell(A) ∩ Ell(G) since the lower-order part is small at the
boundary); the variable-order asymptotic sums (δ′ = (1 + δ)/2, ω = sup 𝗅 − inf 𝗅, and the order count
(m, 𝗅) − (N − ω − 1)(1, 1)); the Neumann series with R₀ gaining 1 − δ (R₀ lies in the log class of order −1 + δ for
every δ, so R₀^j has order −j + δ for each fixed δ, as the (C6) sums require); the space paragraph (independence of N
and of E, completeness); boundedness (N′ admissible for (s − m, 𝗋 − 𝗅): N′ ≥ −(s − m) + 1 and ≥ −inf(𝗋 − 𝗅) + 1);
monotonicity (Id as a symbol of order (s − s′, 𝗋 − 𝗋′)); duality (Hahn–Banach on L² × H^(−N,−N), g ∈ H^(N,N) ⊂
H^(−s,−𝗋) since N ≥ −s and N ≥ −inf 𝗋, open mapping; the density used is from (C8), whose proof does not use duality,
so there is no circle); (C8) (derivatives of χ(tx) supported where |tx| is bounded above and below; ⟨x⟩⟨ξ⟩ ≥ c/t on
supp(1 − τ_t); seminorms O(t^δ); [E, T_t] = [E, T_t − Id] tending to 0 in the class of order (s − ½, 𝗋 − ½), its
first term vanishing as T_t is scalar). lem:i-a-4-4 (c): I redid the chain rule from (x, y, ξ′, η′) to (x, y, τ, μ)
with τ = x²ξ′, μ = xη′ (∂_ξ′ = x²∂_τ, ∂_η′ = x∂_μ, ∂_x|old = ∂_x + (2τ/x)∂_τ + (μ/x)·∂_μ) and obtain exactly the
displayed H_p; with τ = −ξ, μ = η, division by ρ and ρ = 0 give eq:i-a-4-4. prop:i-a-5-2: Q_ε and Q_ε^(1/2) in the
class of (C6) of order (δ, δ) for every δ, via lem:i-b-2-12 (Λ_ϱ ≥ 0 scalar, bounded by a power of the logarithm,
derivatives gaining their weights); z_ε = μ^(−1/2)Q̃_ε^(−1/2) of order −½(𝐦 − 𝟏).

### No circularity

Chapter 20 now cites def:i-b-2-1, lem:i-b-2-12 (via sec:i-b-2-1), thm:i-b-2-4, thm:i-b-2-5, eq:i-b-2-5 and thm:i-b-2-7.
I read sec:i-b-2 (ch. 21, lines 240–498) in full: its proofs (lem:i-b-2-2, lem:i-b-2-3, thm:i-b-2-4, thm:i-b-2-5 and
its consequences, lem:i-b-2-6, thm:i-b-2-7, prop:i-b-2-8, prop:i-b-2-10, lem:i-b-2-11, lem:i-b-2-12) use only Fourier
analysis, integration by parts, Taylor's formula, Peetre's inequality, Schur's test and the Cauchy formula. The only
references to chapter 20 are line 243 ([Mel94]) and the remark at 438–441 identifying H_h^𝐨 with H^(s,𝗋_h); no proof
in sec:i-b-2 uses that remark. Results at h = 1: an h-independent amplitude obeying the bounds with L_1 obeys them with
L_h ≥ L_1, and every estimate of sec:i-b-2 is uniform in h ∈ (0, 1], so evaluating at h = 1 is legitimate; the parts
that need h < h_0 (Sobolev spaces of sec:i-b-2-3, prop:i-b-2-8) are not used by chapter 20. lem:i-b-3-1, which uses (C8),
comes after sec:i-b-2.

### Downstream uses of chapter 20's calculus, against what it now proves

ch. 21:9, 243 (pointers), 438–441 and 516–519 (H_h^𝐨 = H^(s,𝗋_h) at fixed h: W_𝐨 = Op(w_𝐨(x, hξ)) is an elliptic symbol
of the logarithmic class of order (s, 𝗋_h) at fixed h, so (C6)'s independence of E applies; T_t and [P, T_t] from (C8)
and lem:i-a-2-1 (c)); ch. 22:21, 116 ((C4) restricted to a fixed compact support), 550 ((C3), (C4), (C6): duality and
compactness with the decay order dropping by a constant), 604, 644, 786 ((C5) as a regularity statement), 960 ((C6)
independence of the elliptic operator; dilations preserve the logarithmic class), 976–977 ((C5) with variable orders);
ch. 23:1321 (descriptive pointer to rem:i-a-3-3) and 2176; ch. 29:991–998 (boundedness, microlocality, composition;
commutators of ⟨x⟩D_x with Ψ^(0,0), scalar); ch. 35:214; ch. 66:747 (norm via any elliptic operator: (C6)); ch. 70:1589.
Within chapter 20: 386 (lem:i-a-2-2 with the variable weight: the logarithmic class is closed under the chain rule),
404, 427, 457, 459–462, 485 ([Ǎ_ε, T_t] with scalar principal symbol), 552, 1049, 1174, 1182, 1449 and 1626 (variable
orders drop by 2ε, a positive constant, so (C6)'s compactness applies), 1480. All covered, apart from m2 and m5. The
change of class itself is safe: the only non-constant-order symbols produced in chapters 20–23 that rely on chapter
20's class carry logarithmic factors (ϱ^(−𝗄), log ϱ, the regulariser φ_ε, which is bounded in S⁰), and chapters 23 and
27 use their own (S8) class.

### Chapters 03, 21–23, 32, 35, 98

- ch. 03:365–367: matches cor:class-two-dust (81:1627–1628), cor:vlasov-two-dust (82:2322–2323, written with ϕ_out,
  which is u for the background) and the wording of 90:174–176 and 81:1659–1660. Correct.
- ch. 21–23: no [HJS] remains anywhere in `chapters/`; every replacement points to an item of sec:i-a-2-1 that states
  what is used, except ch. 22:111 (m1).
- ch. 32:445–446 and ch. 35:1339–1342: correct (see [Hin17], [ABK20] above). Ch. 35:1342 is left as a short line by
  the edit; the rules allow it.
- ch. 98: every reference cited in the chapters has an entry and every entry is cited (a scripted cross-check of all
  bracketed keys outside [[labels]]; dHUV15 is cited at 23:2174). [HJS] and [AN00] are gone from both; [Mel94], [ABK20]
  and the [Hin17] arXiv id are present and agree with Crossref and the PDFs.
- Appendix A: thm:std-hjs-calculus and thm:std-hin26a-cform are referenced nowhere; the three new entries are not
  linked from the chapters, as the removed [HJS] entry was not either (m3 proposes one link).
- `python3 lint.py --chapters`: 62 files, 0 hits. All proposed replacement texts above were checked by script: no line
  over 121 characters and no wrapped line starting with "+ ", "- ", "* ", "> ", "#", "=" or "|".
