# R-I1a: confirming reading of the I-1 integration sweep, chapters 04-29

Reader R-I1a. Scope: every hunk of `scratch/i1/i1.diff` (base 9f47d2bc) in chapters 04, 06, 08, 09, 10, 20, 21, 22, 23,
24, 25, 26, 27, 28 and 29 (52 hunks). Read first: READER-BRIEF.md, STYLE.md, OUTLINE.md (notation), I-1.md,
I-1-items.tsv and the INTEGRATION.md lines each item cites.

## Method

- The working tree matches the diff for all fifteen chapters: `git diff 9f47d2bc -- <chapter>` and the chapter's part of
  i1.diff have the same +/- lines.
- Each hunk's old and new lines were compared word by word (difflib on the whitespace-split text, privately). Every
  difference is listed below and each one belongs to its item. Chapter 28 was also compared after mapping 𝓘 → ℐ and
  ℂ^N → ℂ^(N_E) in the old text. What is left is one insertion, "< r_0 + δ_0". The counts are 101 𝓘 before, 101 ℐ
  after, and no 𝓘 left anywhere in the edition.
- Every added line was measured in code points, which is what lint.py counts. None is over 121, and no wrapped line
  starts with "+ ", "- ", "* ", "> ", "#", "=", "|" or a numeric marker "0. ", "0) ", "1. ", "1) ". The flagged starts
  are a list item (21:143, unchanged) and a heading (28:109).
- Each rename was grepped across the whole chapter, across every chapter that cites the object, and in the base version
  (to confirm the new letter was free).

## Hunk by hunk

| ch | hunks | item | result |
|---|---|---|---|
| 04 | 2 | 𝒦_m → 𝒴_m | All 4 sites renamed. No 𝒦 is left in 04. 𝒴 was unused in 04 (base count 0). No other chapter cites 𝒦_m: 05, 07 and 09 have no 𝒦, and 07's 𝒴 is a local energy in another chapter. The Kretschmann 𝒦 of 01-03 is untouched. |
| 08 | 1 | 𝒦_1 → 𝒴_1 | All 4 sites renamed, consistent with 04. No 𝒦 is left in 08. |
| 06 | 4 | L → Θ; ε2; BH17 key | 15 sites L → Θ, in (i) and (ii) only. The torus period L (06:337) and the Lebesgue L⁴ (432-437) are kept. Θ was unused in 06 and is not reserved in OUTLINE. Every bound reads the same with Θ: Θ ≥ 2 and C λ ≤ 1/(10 Θ⁴) ≤ 1/160. The added "once C M λ0^(K−3) ≤ ε2/2" is a valid extra smallness condition on λ0(M), consistent with Step 3 (λ ≤ λ0(M)), and it suffices since K ≥ 6 > 3. The claim that ε2 does not depend on λ is true (N4). [[thm:std-bh17-embedding]] (95:663) quotes [BH17, Thm 7.27, p. 56] word for word, and the use (s, p, t, q, n) = (1, 2, 0, 4, 4) meets s − n/p ≥ t − n/q (−1 ≥ −1). The rewrap changes no other word. |
| 09 | 1 | l.46, l.58 | g0⁻¹(dτ, dτ) = −1 − μ/r² < 0 is true, the contraction of g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0 (02:270), and so {τ = const} is spacelike (N1 is a nit on scope). The l.58 hypothesis is now on Σ̂_τ1 ∩ P ∩ {v ≤ v_start}, which is weaker. The proof still runs: it starts from R_ε ∩ Σ̂_τ1 ⊂ Σ̂_τ1 ∩ P ∩ {v ≤ v_start}, because v + ε h_P ≤ v_start forces v ≤ v_start, and its conclusion is unchanged. The rewrap is word for word. |
| 10 | 1 | l.172 | P⁺ ∩ {τ′ ≤ τ} is the region meant (P⁺ = P ∩ {v ≥ v_start}, eq:past-domain). The glyph differs from the chapter's (N2). |
| 20 | 6 | rewrap; N3, N5, N6 | 375-376: words unchanged, no line now starts "0. ". lem:i-a-4-1: y := ρ_∞²G₀ now opens the statement, C_y y² is unchanged in content, and the proof's local coordinates (y, z, w) use the same y. 𝔯₁, 𝔯₂, 𝔯₃: every symbol site is renamed (773, 837, 838). No r₁ or r₃ is left. The radius r₂ is untouched (29, 43-48, 101, 1036-1189). 𝔯 was unused, and no other chapter cites these symbols (24:884 names the same symbol p_in, not r₃). 𝔑 := ker P̂(σ_*): all 5 sites renamed, no 𝒩 is left in 20, and OUTLINE keeps 𝒩 for energies. |
| 21 | 10 | radii; β_Γ; d_O | Radii chain: the condition is S1's standing hypothesis (20:29, 43-48), so the insertion restates it. β_0 → β_Γ on exactly the 12 lines of (Γ.4)'s constant (143-147, 176, 231, 1257, 1343, 1490, 1494, 1952, 1970-1971). The horizon β_0 at 1005, 1023-1026 (ρ⁻¹β_0 on ∂ℛ_±) is kept. β_Γ was unused in 21 and fits the chapter's Γ-subscripted trapped-set constants (h_Γ, c_Γ, C_Γ, ε_Γ, δ_Γ). δ_O → d_O at all 3 sites. |
| 22 | 2 | l.33; |Y_0| | 22:33 reads correctly: sec:i-a-1-2 defines E = X̃ × ℂ^(N_E) (20:52), and ch:s02 uses N_E (21:30). 22:867, estimate redone: by lem:i-c-5-4 at ℓ = 0, θ = 0 (ν = 1, σ̂ = 1), f_1 = r̂⁻¹H_1^(1)(r̂), so w = e^(−ir̂) r̂⁻¹ H_1^(1)(r̂) Y_0 and |e^(−ir̂)| = 1 for real r̂. Hence r̂²|w| = r̂|H_1^(1)(r̂)||Y_0|. This is bounded on (0, 2] by [DLMF, (10.7.7)] (r̂|H_1^(1)| → 2/π; checked numerically, about 1.17 at r̂ = 2) and continuity. The L² conclusion for c < −2 follows as written. The β_0 at 22:687 is a tf weight, not the trapped-set constant, and is correctly kept. |
| 23 | 6 | rank; M → C_z | 23:550 ℂ^(N_E), N_E × N_E. ℂ^(N′) (1389-2292) is a deliberately general rank, outside the item. M → C_z at exactly 27 sites, all of them the commutant constant of prop:ii-a1-5-3's proof. M̃ (the manifold) and M′ (2023-2024) are untouched. C_z matches S1's identical construction (20:973-1005) and was unused elsewhere in 23. Rewraps are word for word. |
| 24 | 11 | radii; β_Γ; rank; ϵ₂ | β₀ → β_Γ at 477-478, 1577, 1590 and 1645, all (Γ.4). The horizon β₀ of eq:ii-b-4-1 (390-415) is kept. ℂ^N → ℂ^(N_E) at every site (643-1052), so no ℂ^N is left in 20-29. N_E = 5^(p+q) is correct for (p, q)-tensors on ℝ^(1+4). In lem:ii-c-2-5, Λ := diag(1, δ⁻¹, …, δ^(1−N_E)) is now correct: the matrix has size N_E, and the nilpotent N keeps its letter, with ΛNΛ⁻¹ = δN because δ^(1−i)·δ^(i) = δ on the superdiagonal. ϵ₁ → ϵ₂ at 1667 only: the ϵ₁ of 1193-1295 is the ϵ_G threshold of another lemma, ϵ₂ is used nowhere else and no other chapter cites it (N3). |
| 25 | 2 | notation sentence; radii | 25:32-34 is true now that 21 and 24 write β_Γ. It agrees with 25:591-592 and with 24:1645 (½β_Γ). |
| 26 | 1 | radii | Restates S1's hypothesis. The rest of the sentence ("a smaller inner radius r_0 does not make harder") stays true: decreasing r₀ keeps r₀ + δ₀ < r₂. |
| 27 | 3 | S^(−M𝟏); K_0 | S2 writes S^(−M𝟏) and ‖u‖_(−M𝟏) (21:267, 458, 467 …), and no K𝟏 is left anywhere. K → K_0 at all 4 sites of the statement of prop:ii-f-2-6; its proof does not name the set. K_0 matches prop:i-b-4-2's own K_0 (21:682) and was unused in 27. The order K of ‖u‖_(𝐨−K𝐞) is kept. |
| 28 | 37 | ℐ; radii; rank | 101 sites of 𝓘 → ℐ, with nothing else changed. The radii chain restates S1's hypothesis. 28:124 ℂ^(N_E). The heading at 109 is unchanged. |
| 29 | 2 | radii; cite | lem:iii-i2-4-2 (38:1626) is the right citation: its proof is "the proof of [[prop:ii-g1-4-7]], with [[cor:iii-h-4-2]] and [[thm:iii-h-4-1]] (3) for L̃_b in place of [[thm:i-c-6-4]] (4)–(5)". That is exactly the replacement the sentence describes. It is a forward pointer in a remark-like paragraph and creates no circularity. |

No hunk changes mathematics beyond its item, and the diff contains nothing in these chapters that no item accounts for.

## Findings

**N1 (nit), 09:46.** The statement is (a) "Each Σ̂_τ is spacelike", with Σ̂_τ defined at 09:23 as "the whole level set
of τ". The new proof proves the inequality "at every point of P". The identity holds wherever g0 is defined (μ ≥ μ0 > 0),
so the restriction is narrower than the statement, though harmless. Fix (the line becomes shorter, 112 characters):
"< 0 at every point of P, the contraction" → "< 0 wherever r > 0, the contraction".

**N2 (nit), 10:172.** The new set {τ′ ≤ τ} uses the prime U+2032. The rest of chapter 10 writes the same dummy variable
with an ASCII apostrophe, including the same paragraph: 10:178 "P ∩ {τ_n ≤ τ' ≤ τ}", and also 191, 193, 236 and 237.
Fix: 10:172 "P⁺ ∩ {τ′ ≤ τ}" → "P⁺ ∩ {τ' ≤ τ}". Alternatively, change the five other sites to τ′.

**N3 (nit), 24:1667.** "For ϵ ≤ ϵ₂, sup …" introduces ϵ₂ with no quantifier. ϵ₂ appears nowhere else. (Before the
change, the sentence borrowed ϵ₁, the threshold of the lemma at 1193-1295.) Fix, lines 1667-1668:

    to Γ^(u/s) := ∂Σ⁺ ∩ U ∩ (φ^(u/s))⁻¹(0). There is ϵ₂ > 0 such that, for ϵ ≤ ϵ₂, sup t_*^(ℓ_K)|∂^αφ̃^(u/s)| ≤ 1 over the
    stated ranges of α. The same holds, with uniform constants, for the stationary models of parameters b near b₀ ((K4)).

(118 and 117 characters.)

**N4 (nit), 06:332-333.** "ε2 does not depend on λ" is true but given without a reason. c_0 and ε2 depend on the
bounds of (i): δ/2 ≤ γ ≤ Θ and ν ≥ ν_min, both uniform for λ ≤ λ_ext. They also depend, through the coordinates y, on
bounds for DΦ_Z and its inverse. Those bounds are uniform in λ because |∂β_ext| ≤ C, which follows from
|∂g_app| ≤ C (06:413-414). The text states this for the derivatives of Φ_Z only as uniformity in τ_i (06:382-384).
Optional fix: replace the paragraph 06:329-337 by

    (iii) *The cut-off.* Let ϒ be a smooth map of the components, the identity on |w| ≤ ε2/2 and with values in |w| ≤ ε2,
    with ε2 so small that every metric within ε2 of g_ext keeps the conditions g^(00) ≤ −c_0 and g^(ab) ξ_a ξ_b ≥ c_0 |ξ|²
    with a fixed constant c_0 > 0 in (τ, y). Put ϒ(w) for w in the coefficients and lower-order terms. The modified system
    agrees with the original where |w| ≤ ε2/2, which holds on Ω once C M λ0^(K−3) ≤ ε2/2 (|w| ≤ C M λ^(K−3), Step 3; c_0 and
    ε2 depend only on Θ and on bounds for DΦ_Z and its inverse, which do not depend on λ since |∂g_app| ≤ C). The
    coefficients and the forcing term are taken at time τ̄(τ), τ̄ smooth, equal to τ on [τ0 − 1, τ_end + 1] and constant
    outside [τ0 − 2, τ_end + 2]: the coordinates of (ii) degenerate as |τ| grows (the flow lines of Z pile up where β_ext
    vanishes), and [DS23, (A1)] asks for bounds uniform in t; on [τ0, τ_end] nothing changes. The coefficients and the
    forcing term equal Minkowski's outside a compact set in y, so the system is posed on a torus T⁴_L of large period L.

(Every line is at most 120 characters, and apart from the parenthesis the words are unchanged.)

The next two nits are outside the I-1 diff. They concern objects whose glyph I-1 unified elsewhere, and are recorded
for the coordinator.

**N5 (nit, outside the diff), 27:196-1127 and 35:900.** Chapter 27 names its semiclassical radial sets over null
infinity with a Latin I: R_(I⁺,±1,in), R_(I⁺,1,in) and R_(I⁺,out), 27 occurrences on 22 lines (196, 206, 213-217, 222,
801, 803, 893, 894, 907, 910, 911, 914, 916, 927, 1050, 1051, 1125, 1127). Chapter 35 cites R_(I⁺,1,in) once (35:900).
Here I⁺ is ℐ⁺: these sets lie in {x_I = 0}, and x_I is "the defining function x_I of ℐ⁺" (28:18). OUTLINE requires ℐ⁺
(U+2110) "in every chapter", and chapters 24, 25 and 28 write R_(ℐ⁺,…). The I-1 rename covered the 𝓘 glyph only.
Fix: "R_(I⁺," → "R_(ℐ⁺," at those 28 sites. Line lengths are unchanged, since both are one code point.

**N6 (nit, outside the diff), 25 (37 sites).** Chapter 25 writes the horizon with 𝓗 (U+1D4D7): ϑ_𝓗 and ∂R_(𝓗⁺), for
example 25:110, 323-342. The same objects are ϑ_ℋ of eq:i-a-1-5 and ∂R_(ℋ⁺) of def:ii-b-4-1, which chapters 20, 21, 24 and
29 write with ℋ (U+210B). This is the analogue for the horizon of the 𝓘/ℐ unification. Chapter 30 has two 𝓗 and the
appendix has four (95). Fix: 𝓗 → ℋ in 25 (and in 30 if the other reader agrees). Line lengths are unchanged.

Checked, no finding: 22:268 opens with "2. " inside a paragraph, outside the diff. The renderer reads GFM
(render/build_html.py:78), and in GFM an ordered marker other than 1 cannot interrupt a paragraph, so the line renders
as text.

## Lint and assembly

- `python3 lint.py --chapters`: 62 files, 4405 labels, 1 hit, chapters/90-scope.md:66 (the pending marker, as expected).
- `python3 assemble.py --check`: labels 4405, computations cited 0, problems 0.
- `git status` is clean after both runs.

## Verdict

**CONFIRMED**: 0 Major, 0 minor, 6 nits (N1-N4 on I-1 hunks; N5-N6 outside the diff, for the coordinator).
