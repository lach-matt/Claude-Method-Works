# P-GRD11 report

File: proofs/P-GRD11.md (not committed), md5 975cc2072424a0863437a708a61d2e84, 322 lines.
- Lines 1–192 are the chapter text; lines 194–322 are Placement, Comparison and Crosswalk.
- Source: HEAD 89765a14, chapter 87 md5 bbe37584…, 6883 lines.

## What is proved: sec:tl5-hfu (Section 57.26), level four

The section carries the leaf constant, the short-word weights and the family counting of P-GRD10 into S_M, 𝔯_M and ε_M.
It goes after rem:tl5-hfp-what, which gains one pointer line.

1. **Lemma 57.224, lem:tl5-hfu-face.**
   - lem:tl5-hf4-face (b), in its intrinsic form, holds with the weights: C_(E,r)(𝔶)² 𝔵_r Σ_J 𝔶_|J| ‖ℒ^J A‖².
   - Part (a) holds with the two coefficients kept apart (𝔱_(r,0), 𝔱_(r,1) ≤ 𝔱_r).
2. **Lemma 57.225, lem:tl5-hfu-fam.** This holds for every N ≥ 4. For n distinct words with weights 𝔬_C² ≤ μ^(|C|+1):
   - (Σ 𝔬²|D̂²Ψ_C|²)^½ ≤ 𝔩(𝔙)𝒥_g + (Σ 𝔬²w_C²)^½ k₂^z ϱ/(1 − 𝔵^z);
   - 𝔩(𝔙) = k₁^D + μ^½(k₁^D𝔷′ + (1 − 𝔰)⁻¹𝔯_♯) + (1 − 𝔰)⁻¹𝔞_𝔄(𝔙) + n^½ 𝔵^z(k₁^(j,μ,p) + 2)/(1 − 𝔵^z);
   - 𝔩(𝔙) ≤ n^½(k₁ + 2𝔵)/(1 − 𝔵), and 𝔞_𝔄(𝔙) ≤ (n/2)^½ α.
3. **Definition 57.226, def:tl5-hfu-constants.** Two families: 𝔙₂, the 49 words of length two with weight μ^(3/2), and
   𝔙_Γ, the 301 words JZ. The new constants are:
   - 𝔛^u_(1,t) = C_(E,3)(𝔶)𝔵₃^½(1 + ϖ₁^½);
   - 𝔛^u_(2,t) = C_(E,4)(𝔶)𝔵₄^½(𝔩(𝔙_Γ) + μ^½ϖ₂^½);
   - 𝔛′^u_(2,t) = √301 𝔗(μ/ν)² C_(E,4)(𝔶)𝔵₄^½ ς_t;
   - 𝔜^u_(1,t) = (μ𝔱_(3,0) + 𝔱_(3,1)𝔩(𝔙₂)²)^½;
   - 𝔜′^u_(1,t) = 7(μ/ν)^(3/2)𝔱_(3,1)^½ ς_t;
   - 𝔜″^u_(1,t) and 𝔜″^u_(2,t), each × μ^(3/2);
   - S_M^u, 𝔯_M^u and ε_M^u.
4. **Lemma 57.227, lem:tl5-hfu-mixed.** eq:tl5-hfs-mixed holds with these constants. For 𝔶₀, 𝔶₁ ≥ 1 each is at most
   the constant of index p it replaces.
5. **Theorem 57.228, thm:tl5-hfu.** The closing condition is
   4η_u^(−3/2)(δ_w + η_u^(−1/2)(ε^z + ε_M^u))(S_F^p + S_M^u) < 1, with 𝔯^u = 𝔯^p − 𝔯_M^p + 𝔯_M^u and 𝔰_*^u < 𝔰₁^v.
   For 𝔶 ≥ 1 it contains thm:tl5-hfp at N = 4.
6. **Remark 57.229, rem:tl5-hfu-what.**

## Deduced, not evaluated, at G0m's optima

| Change | Effect (decades) |
|---|---|
| 𝔜₁: 1 + 7λ → 𝔩(𝔙₂) | −0.65 to −0.80 |
| 𝔛₁: q₃ | −1.05 to −1.41 |
| 𝔛₁: triangle inequality | 0 to −0.15 |
| S_M in all | about −1.8 to −2.3 |
| 𝔯_M: ϱ terms | −2.6 to −3.6 |
| 𝔯_M: η₀ terms and ε_M | an extra μ^(3/2) |

- After the change S_M lies 1.3–1.9 decades below S_F, where it was 0.22–0.85 above.
- Each term is at most G0m's hypothetical "S_M × q" lever, so the gain on min(f, ϱ) is at least G0m's +0.31/+0.26/+0.34/+0.14.
  Because 𝔰_* then binds within about 0.06, the gain is at most about 0.1 more than that.
- After this, 𝔰_* binds. C_P^v levers return to the 1:1 rate.

## Not done

**Target 2** (the count 7² in S_F, and 𝔠^♮₄ → 9·2⁴) was not done, for three reasons:
- After target 1 it is capped by 𝔰_*.
- The word count needs eq:tl5-hfs-products restated over each word length, monomial by monomial.
- 𝔠^♮₄(μ) + 1 ≥ 1296 for every μ, from the b = 0 terms (deduced from eq:tl5-hfs-cn). Reaching 144 would need a bound of
  the bilinear form 2𝔮̂ itself.

**Also not done:**
- The 𝒟_g split in S_M.
- The count 6 in 𝔠^Mq₁: it is attained by Minkowski over the sets S.
- 𝔜₂: no gain is available.
- 𝔪(t): no effect when 𝔴₀ ≥ 1.

## Checks

Run in a scratch tree from git archive 89765a14 plus the merge:
- `lint.py --chapters`: 62 files, 5292 labels, 0 hits.
- `assemble.py --check`: 0 problems.
- In-memory check: `[] 0`.
- Label numbers: 0 of the 5281 existing ones change; 11 are added.
- Crosswalk: 441 rows for 441 labels, in the same order.
- The Placement quotes match the source text exactly.
