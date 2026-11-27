# R2-F-G5: confirming reading of the F2-G5 fix round (G5 re-sourcing, [HJS] → [Mel94])

Reader's review, 2026-11-20. Read: `git diff 50716bf9 99cdddb7` on chapters 20, 22, 95, 98 and the crosswalks of 20, 22
and 95. The range also changes chapters 10 and 63. That is commit 62349051 (review R-P-K), which does not belong to
this round, and I did not read it. `chapters/` and `crosswalk/` in the working tree match 99cdddb7, so the line numbers
below are those of the current files. The first review is notes/reviews/R-F-G5.md and the fix report is
notes/reports/F2-G5.md. I checked against the saved sources in `scratchpad/reader/sources/` (mel94-pages.txt for every
[Mel94] item).

**Verdict: NOT CONFIRMED.** All thirteen findings are resolved, and all four departures are correct and at least as
good as the first reader's texts. There is one new minor issue (m6). It is a pre-existing false clause that survived
in the very sentence m4 rewrote. It came in with the first reader's replacement text, so the writer is not at fault, and
nothing downstream depends on it. There are also three nits (n9–n11) and one crosswalk nit (n12). If m6 is applied, as
one line in place, I expect a confirmation.

---

## The thirteen findings

| # | Status | Where |
|---|---|---|
| m1 | resolved | 22:111 "(after (C8) in [[sec:i-a-2-1]])". The paragraph meant is 20:279–282, which follows the (C8) statement (274–277) directly |
| m2 | resolved | 20:585–592. The hypothesis is the form w φ Q^(1/2) of lem:i-b-2-12 at h = 1. The elliptic estimate is reached through (C5) at h = 1 (departure 1). I checked it against prop:i-a-5-2 below |
| m3 | resolved | 20:221–226 ((C2) states the reading with a link, the bracket order comes from the formula, (5.22) is "in coordinates near the boundary"); 95:824–829 (the reason, with (5.10), (5.13), (5.14), (5.12)) |
| m4 | resolved as asked | 20:260–261. The order gain is now conditional on scalar σ(A). The symbol formula in the same clause is still too general: see m6 |
| m5 (a) | resolved | 20:213–216. (C1) has the composition formula from thm:i-b-2-4 at h = 1, with seminorm bounds and the disjoint-support statement. Step 0 of lem:i-a-3-1 (487–488) now cites what (C1) states |
| m5 (b) | resolved | 20:216–219 (the statement), 289–296 (the proof), 327–328 ((C5) continuity) and 333 ((C6) clause). For the wording at 327–328 see n9 |
| n1 | resolved | 20:314–317 |
| n2 | resolved | 20:346–349 |
| n3 | resolved | 20:194–196 |
| n4 | resolved | 20:245 |
| n5 | resolved | 20:323–324 |
| n6 | resolved | 20:200–202. Both inclusions are now shown. For the citation see n10 |
| n7 | resolved | 95:768–771. Every page and equation matches the per-page extraction: (5.4) p. 16; (5.10) p. 17; (5.15)–(5.20) p. 18; (5.22), (5.27) p. 19. Nothing is split across lines |
| n8 (a) | resolved | 95:1192–1194 |
| n8 (b) | resolved | 98:147–150 |

## The new material, checked

**(C1) composition (20:213–216).** It follows from the statement of thm:i-b-2-4 alone. Take M = 2N in eq:i-b-2-4. The
terms with N ≤ |α| < 2N lie in the class of order 𝐨 + 𝐨′ − |α|𝟏 + ϵ𝟏 (last sentence of the theorem). At h = 1, with
constant orders, the log class of order (m + m′ − N + ϵ, ℓ + ℓ′ − N + ϵ) lies in S^(m+m′−N+δ,ℓ+ℓ′−N+δ)_sc for δ > ϵ,
continuously. The product-of-seminorms bound is in the theorem. It also follows that a#a′ ∈ S^(m+m′,ℓ+ℓ′)_sc itself,
with bounds: take N = 2 and note that the |α| = 1 terms are genuine S_sc symbols. The disjoint-support clause is
consequence (iv) after thm:i-b-2-5. Because every term of the expansion vanishes on U together with its derivatives, it
even holds on U itself, so "closure in U" is a harmless strengthening.

**Uniform asymptotic sums (20:289–296).** Correct. The constant C_k is independent of j. In the Leibniz expansion, the
undifferentiated ψ_t contributes (t/c)⟨x⟩⟨ξ⟩ ≥ 1 on its support. The derivatives of ψ_t are O(⟨x⟩^(−|α|)⟨ξ⟩^(−|β|))
uniformly in t and are supported in supp ψ_t. So the bound C_k t p_(j,k) holds. For j > max(N, k):
- the S^(m−N,ℓ−N) seminorm is at most the S^(m−j+1,ℓ−j+1) seminorm, since j ≥ N + 1;
- C_k ≤ C_j and p_(j,k) ≤ p_(j,j), since k < j;
- so the term is at most 2^(−j).

The finitely many (1 − ψ_(t_j))a_j^b are supported in a fixed compact set and are bounded in every class. Continuity
follows from uniform convergence of continuous partial sums. "χ as in (C8)" and "as in the proof of (C8)" point
forward to elementary facts, and the (C8) proof does not use asymptotic sums, so there is no circle.

**(C5) continuity (20:327–328) and its three uses.** Keep the cut-off χ fixed, which uniform ellipticity near K allows.
Then:
1. a ↦ χa⁻¹ is continuous.
2. R₀ = Op(a#(χa⁻¹) − χ) is continuous into S^(−1,−1)_sc, by the N = 2 form of the (C1) formula.
3. The powers R₀^j are continuous into S^(−j,−j)_sc, by the same formula.
4. C ∼ Σ(−R₀)^j is bounded, and continuous in a parameter, by the uniform sums.

So B = B₀C is bounded for a bounded, uniformly elliptic family, and continuous in its parameter. This covers each use:
- prop:i-a-5-1 (1079–1080): P̂(σ) is polynomial in σ, and 𝒟 is compact.
- lem:i-a-2-3 (414–415, 426): L₀ comes from lem:i-a-2-2, the l_j come from the Lyapunov integrals, which are continuous
  in k and k_j, and L ∼ Σ L_j uses the uniform sum.
- thm:i-a-8-1 (1691–1698): bounded families near each b₁, with ℬ compact.
- ch. 22 (K2) (111–114): a family over the compact closure of ℱ.

Every use is a bounded family over a parameter. The sentence as written says more than that (n9).

**rem:i-a-3-3 against prop:i-a-5-2.** The limit symbol is b₀ = μ^(1/2)ϱ^(−𝗄)ψ_ye^(−C_z z)χ_sχ_eQ̃₀^(1/2), with φ_ε → 1
(def:i-a-regulariser) and 𝗄_ε → 𝗄. The cut-off of prop:i-a-4-2 gives Q̃₀ = χ̃Q₀ + (1 − χ̃)c Id + χ̃Λ_ϱ Id. That is
"Q_0 + κ Id" with κ = χ̃Λ_ϱ ≥ 0 scalar and of log growth, which is the hypothesis of lem:i-b-2-12. (Hermitian means
h-Hermitian; the fibre-inner-product paragraph of sec:i-b-2-2 covers this.) Take w = μ^(1/2)ϱ^(−𝗄), whose quotient by
the weight w_𝐬 is a positive symbol of order 0 that can be absorbed into φ. Then φ = ψ_ye^(−C_z z)χ_sχ_e, which is
≥ c > 0 on a neighbourhood of γ([0, t₁]) (z ∈ (−δ/2, t₁ + δ/2), |y| small). So "B₀ elliptic on γ([0, t₁])" (1157) holds
in the remark's sense, and lem:i-a-3-2 runs. The start Op(φ′b₀⁻¹) gives AB₀ − Op(φ′) of order −1 + δ for every δ, as
in the proof of lem:i-b-2-12. Hence the Neumann series and the variable-order sums of (C6) apply, and B = Op(φ′b₀⁻¹)C
lies in Ψ^(−𝐬), as the estimate needs.

## The departures

1. **m2, the elliptic estimate through (C5) from Op(φ′b₀⁻¹).** Correct, and better than the first reader's text. The
   last clause of lem:i-b-2-12 invokes prop:i-b-2-10. That proposition rests on prop:i-b-2-8 and on the spaces H_h^𝐨,
   which are defined only for h < h₀, so it does not give the estimate at h = 1. The symbolic part does carry over,
   and the (C5) construction with the variable-order sums supplies the rest.
2. **m2, the lem:i-a-3-2 note moved into the remark; the prop:i-a-5-2 note left out.** Correct, and at least as good.
   The writer's stated reason is slightly off: with e^(−C_z z) counted in w, φ = ψ_yχ_sχ_e really is 1 on γ. But
   φ ≥ c > 0 near γ under either counting, and prop:i-a-5-2 (1157) already names where χ_s = χ_e = ψ_y = 1. So nothing
   is lost.
3. **m5 (b), the clause at 20:333 on variable-order sums.** Correct. Bounded or continuous A_j in the log class of order
   (m − j + δ, 𝗅 − j + δ) are bounded or continuous in Ψ^(m−j+δ′,sup𝗅−j+δ′)_sc. The uniform (C1) then gives the
   remainder bounded in Ψ^(m−N+δ′,sup𝗅−N+δ′)_sc, which embeds continuously in the variable class of order
   (m, 𝗅) − (N − ω − 1)(1, 1). The clause is needed: the (C5) Neumann series with variable orders runs through these
   sums.
4. **Rewrapping.** The words are unchanged at 20:194–196, 245–247, 260–262 and 333–336. No new line is longer than 121
   characters, in the source or after label resolution, and none starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".

## [Mel94] citations against the saved source

- **(5.4), p. 16**: C_scX = ∂(^(sc)T̄^∗X). Correct (95:770, 819–820).
- **(5.10), p. 17**: the exact sequence of Proposition 3, with kernel Ψ^(m−1,l+1)_sc(X; E, F). Correct, as the kernel
  statement for sk = sc (95:813–814, 825; 20:272).
- **(5.15)–(5.18), p. 18**:
  - (5.15) is the extension of the bracket to C^∞(C_scX; S^(m,l)) and A^({m,l}). It is elided by "…" in item (5), and
    the header lists it.
  - (5.16) is printed with j_(sc,m1+m2,l1+l2)([A, B]) = (1/i){j(A), j(B)}.
  - (5.17) and (5.18) are as quoted. (5.18) takes a classical a ∈ C^∞(^(sc)T̄^∗X; S^(m,l)) and b ∈ A^({m′,l′}), with the
    bracket in A^({m+m′−1,l+l′+1}).
  - The 95 sentence "By (5.18), and for a conormal a by the same count of derivatives in (5.22)" is accurate. (5.22) is
    the canonical bracket in (x, y, ξ, η) near ∂X, valid at all frequencies. Under (5.20), the fibre derivatives are
    x²∂_τ and x∂_μ, and ∂_x at fixed (ξ, η) is x⁻¹ times a b-field. The count gives both orders.
- **(5.22), p. 19**: "in terms of coordinates x, y₁, …, y_(n−1) where x is a local defining function for the boundary"
  (p. 18), with (5.22) on p. 19. So "writes in coordinates near the boundary" (20:225) is right.
- **The lowered-order reading of (5.16).** At the printed indices:
  - the left side j_(sc,m1+m2,l1+l2)(AB − BA) vanishes by (5.14), whose values lie "in commutative algebras";
  - the right side vanishes because the bracket lies in A^({m1+m2−1,l1+l2+1}), the subspace that the quotient (5.12)
    divides out.

  So (5.16) has content only with j_(sc,m1+m2−1,l1+l2+1) on the left. The bracket is well defined there: changing
  j(A) by A^(m1−1,l1+1) changes it by A^(m1+m2−2,l1+l2+2). The signs agree. With Op the left quantisation,
  [Op(a), Op(b)] has symbol (1/i)(∂_ξa∂_xb − ∂_xa∂_ξb) + lower, so σ(i[A, B]) = {σ(A), σ(B)} as in (C2). In our sign,
  the printed orders (m1 + m2, l1 + l2) are (m₁ + m₂, ℓ₁ + ℓ₂), as 20:223 says.
- **(5.1), with n6**: correct as a composition. For the membership of the two factors see n10.

## Chapter 33

The proof of prop:iv6-1-1 (33:2319) cites chapter 20 at 2354, 2379–2384, 2401 and 2651. All the citations still hold:
- 2354 cites prop:i-a-5-2 with rem:i-a-5-2-uses (ii), and 2379–2384 cites prop:i-a-4-6 and prop:i-a-5-2 with
  rem:i-a-5-2-uses (ii). Neither statement changed in this round, and neither did rem:i-a-5-2-uses.
- The only change under prop:i-a-5-2 is in its proof, which relies on rem:i-a-3-3. The new hypothesis there holds, as
  shown above. The uniformity in σ ∈ I + i[0, ν] uses bounded parametrix families, which (C1) and (C5) now state.
- prop:i-a-4-6 runs lem:i-a-3-2 with constant decay orders. It does not use rem:i-a-3-3 or the (C6) commutator clause,
  and its commutators with Ǎ_ε go through lem:i-a-2-1 (c), which is unchanged.
- 2401 and 2651 cite lem:i-a-7-1, which is unchanged.

## Checks

```
$ python3 lint.py --chapters
chapters: 62 file(s), 4593 label(s) defined, 0 hit(s)
$ python3 assemble.py --check
labels 4593, computations cited 0, problems 0
$ python3 -c "...in-memory check..."
[] 0
```

The longest line in the assembled text is 121 characters. All labels are lowercase. Each replacement proposed below was
put into an in-memory copy of chapter 20 and run through number, resolve and scan_text, and the result is `[] 0`. The
script is scratchpad/reader/r2g5/sim.py.

---

## New findings

### m6 (minor) — (C6): the symbol of the commutator needs more than a scalar principal symbol of A

`chapters/20-s01-spectral-bounded.md:260–262`, current text:

    if σ(A) = a Id is scalar, [A, B] has order (m + m′ − 1 + δ, 𝗅 + 𝗅′ − 1 + δ) for every δ > 0, with
    σ(i[A, B]) = H_aσ(B). Operators of order (0, 0) are bounded on L² ([[thm:i-b-2-7]] at h = 1). For constant s, a variable
    order 𝗋, E := Op(⟨ξ⟩^s⟨x⟩^𝗋 Id) and an integer N ≥ max(−s, −inf 𝗋) + 1, let

**What is wrong.** If only σ(A) is scalar, the amplitude of A is a Id + a₁ with a₁ of order (m − 1 + δ, 𝗅 − 1 + δ). In
the expansion of eq:i-b-2-5 at h = 1, i(a₁σ(B) − σ(B)a₁) has the same order as H_aσ(B), namely
(m + m′ − 1 + δ, 𝗅 + 𝗅′ − 1 + δ). So it belongs to σ(i[A, B]), and it is not zero in general. A constant-order
example: a₁ = ⟨ξ⟩^(m−1)⟨x⟩^(ℓ−1)E₁₂ and σ(B) = ⟨ξ⟩^(m′)⟨x⟩^(ℓ′)E₂₁ give i⟨ξ⟩^(m+m′−1)⟨x⟩^(ℓ+ℓ′−1)(E₁₁ − E₂₂).

The h = 1 reading of eq:i-b-2-5 gives the order. The paragraph after that equation gives only the order too: there
(i/h)[Op_h(a), Op_h(b)] − Op_h(H_p b) lies in the class of order 𝐨 + 𝐨′ − (1, 1, 0) + ϵ𝟏, the order of H_p b itself.
The formula holds if A = Op(a Id) exactly, or if σ(B) is also scalar. These are exactly the cases lem:i-a-2-1 (c) states
in constant orders (20:377–381).

Every use in chapters 20–23 falls in one of the two cases:
- prop:i-a-5-2 at 1141: P_R and Ǎ_ε² both have scalar principal symbols;
- the (C8) proof at 363–364: E is exactly scalar;
- lem:i-a-3-1 at 507: the order only.

So nothing downstream breaks. The clause came from R-F-G5's m4 replacement text, which treated the formula as correctly
conditioned. Proposed replacement (four lines; line 263 "    H^(s,𝗋)_sc := …" follows after the blank line, unchanged):

    if σ(A) = a Id is scalar, [A, B] has order (m + m′ − 1 + δ, 𝗅 + 𝗅′ − 1 + δ) for every δ > 0, with
    σ(i[A, B]) = H_aσ(B) if moreover A = Op(a Id) or σ(B) is scalar. Operators of order (0, 0) are bounded on L²
    ([[thm:i-b-2-7]] at h = 1). For constant s, a variable order 𝗋, E := Op(⟨ξ⟩^s⟨x⟩^𝗋 Id) and an integer
    N ≥ max(−s, −inf 𝗋) + 1, let

### n9 (nit) — (C5): "B depends continuously on the amplitude of A" says more than the proof gives

`chapters/20-s01-spectral-bounded.md:327–328`, current text:

    1 − δ in both orders. By the seminorm bounds and the uniform asymptotic sums of (C1), B depends continuously on the
    amplitude of A, and is bounded when A is bounded in Ψ^(m,ℓ)_sc and uniformly elliptic near K.

B is not a function of A. The cut-offs t_j of the asymptotic sum are chosen from bounds over a family, and the uniform
version of (C1) is stated for a bounded family. A Fréchet space has no bounded neighbourhoods, so a map from amplitudes
to B is not what the proof gives. Every use is a bounded family over a parameter (𝒟, ℬ, the closure of ℱ, the bounded
families of lem:i-a-2-3), so this is wording only. Replacement (three lines):

    1 − δ in both orders. By the seminorm bounds and the uniform asymptotic sums of (C1), if A depends on a parameter, is
    bounded in Ψ^(m,ℓ)_sc and is uniformly elliptic near K, then B can be chosen bounded in Ψ^(−m,−ℓ)_sc, and continuous
    in the parameter if the amplitude of A is.

### n10 (nit) — n6's citation: membership of the factors is [Mel94, Definition 2]

`chapters/20-s01-spectral-bounded.md:200–202`, current text:

    This is [Mel94]'s H^(s,r)_sc [Mel94, (5.27), p. 19]: ⟨D⟩^s⟨x⟩^r lies in [Mel94]'s Ψ^(s,−r)_sc by [Mel94, (5.1)], and
    every element of it is ⟨D⟩^s⟨x⟩^r followed by an operator of order (0, 0), which is bounded on L² by (C3). Pages of
    [Mel94] are those of the author's online edition.

(5.1) is the composition. The factors ⟨D⟩^s and ⟨x⟩^r lie in [Mel94]'s classical classes Ψ^(s,0)_sc and Ψ^(0,−r)_sc by
Definition 2, since their amplitudes are ρ_σ^(−s) · 1 and ρ_N^(−r) · 1. The (C4) proof (306–307) gives the same
reasoning. Replacement (four lines; line 203 "Its statements hold …" follows unchanged):

    This is [Mel94]'s H^(s,r)_sc [Mel94, (5.27), p. 19]: ⟨D⟩^s⟨x⟩^r lies in [Mel94]'s Ψ^(s,−r)_sc, its factors having
    the classical amplitudes ⟨ξ⟩^s and ⟨x⟩^r [Mel94, Definition 2 and (5.1)], and every element of it is ⟨D⟩^s⟨x⟩^r
    followed by an operator of order (0, 0), which is bounded on L² by (C3). Pages of [Mel94] are those of the author's
    online edition.

### n11 (nit) — F2-G5's account of departure 2

This is in the report, not the paper, so no change to the text is needed. F2-G5 says that with e^(−C_z z) "counted in
w the statement needs no separate remark". With that counting, the first reader's "φ = 1 on γ" is in fact true. The
omission is right for another reason: φ ≥ c > 0 near γ under either counting, which is all that rem:i-a-3-3 asks. If the
report is kept as a record, its sentence could say that.

### n12 (nit, crosswalk) — column 3 of thm:std-melrose-sc lags the new header

`crosswalk/95-standard-results.tsv:49`, third column, current text:

    [Mel94] (1.1), Definitions 1-2, (5.1), Propositions 3-5, Lemmas 5-6, (5.12)-(5.34), (7.1), (7.2), (7.6), read 2026-11-20

The header (95:768–770) now also cites (4.1)–(4.3), (5.4) and (5.10). Replacement:

    [Mel94] (1.1), (4.1)-(4.3), Definitions 1-2, (5.1), (5.4), Propositions 3-5, (5.10), Lemmas 5-6, (5.12)-(5.34), (7.1), (7.2), (7.6), read 2026-11-20

---

## Final

**Verdict: CONFIRMED.** I checked the files at 192646dd. `chapters/20-s01-spectral-bounded.md` and
`crosswalk/95-standard-results.tsv` have no uncommitted changes.

The four texts below are applied in my exact words, and they read correctly in context:
- **m6**, 20:261–264: the (C6) symbol formula now requires A = Op(a Id) or a scalar σ(B). This matches lem:i-a-2-1 (c).
- **n9**, 20:329–331: the (C5) parametrix is now stated for a bounded, uniformly elliptic family depending on a
  parameter.
- **n10**, 20:200–203: the citation is now [Mel94, Definition 2 and (5.1)]. Line 204 "Its statements hold …" follows
  unchanged.
- **n12**, crosswalk/95:49, column 3: it lists (4.1)–(4.3), (5.4) and (5.10). The row still has four fields.

`git diff 99cdddb7 HEAD` on chapters 20, 22, 95 and 98 and their crosswalks shows only these four edits. n11 needed no
change. With m6 resolved, every finding is resolved and no Major or minor issue remains.

Checks on the current tree. The label count went from 4593 to 4609 because of the merge another agent is running in
chapters 00, 01, 03, 33, 71 and 90; I did not read those changes.

```
$ python3 lint.py --chapters
chapters: 62 file(s), 4609 label(s) defined, 0 hit(s)
$ python3 assemble.py --check
labels 4609, computations cited 0, problems 0
$ python3 -c "...in-memory check..."
[] 0
```

After label resolution the applied lines are at most 117 characters long. None starts with "+ ", "- ", "* ", "> ", "#",
"=" or "|".
