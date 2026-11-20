# P-G24b: the remaining preprint steps of chapter 33, stated and proved

Proof file for the coordinator. Nothing in `chapters/` or `crosswalk/` was edited. The placement texts below were applied
to a scratch copy of the tree and checked there (section 7). Every old text is copied from
`chapters/33-s14-constraint-damping.md` at HEAD (the chapter last changed at the P-ADM merge, 54350a5d), md5
147ca1624e75c280f86908a0aa499824. That file includes the F2-G24 fix round and the P-LB, P-T49 and P-ADM merges, so it is not
the file at 003371f6. Each old text occurs exactly once, and no two old texts overlap; both facts were checked by a
script. The line numbers given are those of that file.

## 1. Summary

- **Classification.** Chapter 33 has 248 bracketed citations: [Hin26a] 208, [Hin26] 29, [Hin26c] 4,
  [Hin23d] 2, [Hin26d] 3 (published), [Mel93] 1 (a book), [Shu92] 1 (published). Section 2 classifies every one.
  - (a): about 60 uses are steps used and not proved.
  - (a-G1): 9 sites belong to the semiclassical 3b-calculus, which P-G1 treats.
  - (c): one is a published theorem quoted in Appendix A but applied outside the hypotheses quoted there, the relative
    index theorem. This file does not prove it; see section 6.
  - (b): everything else is attribution, or a name for a statement the paper itself states and proves.
- **What is proved here.** Every (a) outside G1 now has a statement and proof in the paper's notation. The texts are
  T1–T45 in section 5. They give four new results with explicit constants:
  - lem:iv5-2-symbols: the commutator symbol of a product commutant. It defines the b_0, b_R, e, f, … that sec:iv5-2 to
    sec:iv5-5 and thm:iv6-2-1 took from [Hin26a, (5.39)–(5.43), (5.54), (5.57), (5.60), (B.38)].
  - lem:iv5-6-transport: the damping term as a transport term, which replaces [Hin26a, (5.77)].
  - lem:iv5-6-core: the energy estimate with damping, with explicit λ_* and C_*. It replaces [Hin26a, (5.70)–(5.78)].
  - A new proof of prop:iv5-6-1, all four estimates and (eq:iv5-6-1), from lem:iv5-6-core. It holds for every
    h ∈ (0, 1].
- **Further replacements.**
  - prop:iv6-1-1. The estimate (B.20), the dual estimate (B.28), the shift (B.24)–(B.25), the complex-σ decomposition
    (B.29) and pp. 89–90 are replaced by the boundary-face estimates of chapter 20 and the proof of thm:i-c-4-3 of
    chapter 22, with explicit thresholds. The dual estimate is now displayed.
  - thm:iv6-2-1. (B.34)–(B.41) are displayed or defined.
  - prop:iv5-1-3. (5.28) and (5.30) are displayed.
  - thm:iv5-7-3 (b). The classical Cauchy theory "[Hin26a, p. 42]" is replaced by Appendix A (BGP).
  - lem:iv5-0-2 (c) and def:iv5-0-1. Two small citations are replaced by their one-line proofs.
- **def:iv6-0-2.**
  - The definition now says what is asked at complex σ: only the condition at R_out.
  - It now defines admissibility at every real σ₀ ≠ 0.
  - It defines "admissible on a set" with chapter 20's convention: the orders used at complex σ are those for Re σ.
  - Every use was checked (section 4).
- **One statement needs a correction, which the coordinator should put to the author.** The second estimate of
  prop:iv5-6-1 (1) is false as stated ("without support condition"). It needs ω supported at Σ^♯. A counterexample is
  in section 3. Its only use, prop:iv5-7-2 (x), applies it to such ω, so nothing downstream changes. T19 adds the
  hypothesis.
- **Two harmless adjustments, flagged.**
  - T3 adds δ_r < 1/5 to lem:iv5-0-5. Every condition there survives a decrease of δ_r.
  - T8 takes χ_K in prop:iv5-3-1 supported in [0, 2δ_r) and positive there (section 5, the convention of T4), rather
    than ending at (3/2)δ_r, so that b_0 is elliptic on the whole of WF′(B_0) as stated. T8 also widens χ_sf from
    [0, 3/2) to [0, 2), and T11 inherits this. Its derivative stays inside the interval where lem:iv5-0-5 (6) applies, because
    2δ_r < 2/5 < v(1 − δ_sf).

## 2. Classification of every preprint citation in chapter 33

### 2.1 The classes

- **(a)** A step used and not proved in the paper. This covers a display, page or symbol of the preprint that the reader
  needs in order to follow the argument, or a statement used under a preprint's display number and never stated.
- **(a-G1)** Like (a), but the step is a fact of the semiclassical 3b- or eb-calculus. P-G1 handles these; its site is
  named.
- **(b)** Attribution only. Either the step is proved in the paper, or the citation names a statement that the paper
  displays and proves under that name.
- **(c)** A published result quoted in Appendix A (chapter 95), with page.

Line numbers refer to the chapter at HEAD, md5 147ca162…. "T n" is the placement text of section 5 that settles an (a).

### 2.2 The table

| lines | citation(s) | class | where it is settled |
|---|---|---|---|
| 8, 12 | [Hin26, §7 to Prop. 7.4], [Hin26a, §§3–6, App. A–B], [Hin26a, Lemma 3.2] | b | chapter overview; the form is proved in lem:s14-box-c and prop:np-10-12 (i) |
| 49 | [Hin26, (7.11)] | b | the adjoint formula is derived on the spot (δ_g = (δ*_g)*, G_g symmetric) |
| 54, 79, 88, 129 | [Hin26, Thm 7.1], [Hin26, (7.3)–(7.6)], [Hin26, §7.2] | b | statement attributions; the structure is proved in lem:iv4-1-2 and prop:np-10-21 |
| 97–98 | [Hin26a, (3.1)], [Hin26a, (3.2)] | b | notation identified; E^C and L_h are defined in the paper |
| 343, 359 | [Hin26a, Lemma 3.2], [Hin26a, Lemma 3.9] | b | proved in prop:np-10-13 (i)–(ii) and in its proof (ζ_μM^μ = −½ℓ(ζ)) |
| 554, 557, 559, 562 | [Hin26a, (5.8)], [Prop. 5.1], [p. 39], [p. 41] | b | (5.8) is written out and proved in prop:np-10-14 (v); the p. 39 fact is f = 1 − mr⁻² (prop:np-10-22 (i)); the p. 41 remark is proved in (b) |
| 783, 787 | [Hin26c, (5.17)] | b | ϑ_ℋ and β₀ are defined in sec:i-a-1-4 and (H3) |
| 1039, 1042, 1043, 1048 | [Hin26a, Lemmas 3.3–3.8, (3.8), Cor. 3.6, Lemma 3.5, 3.7] | b | lem:iv4-1-1 and lem:iv4-1-causal (F-G24) |
| 1090, 1125 | [Hin26a, (6.4)], [Hin26a, Thm 4.9] | b | lem:iv4-1-2 and lem:iv4-1-3, proved |
| 1137 | [Hin26a, p. 29] | b | the indicial family is the normal operator of ρ⁻²P, and P − P̄ ∈ ρ⁴Diff²_b by lem:iv4-1-2 |
| 1162–1186 | [Hin26a, Prop. 5.1], [(5.8)], [p. 39] | b | lem:iv4-1-4 states the six conditions in 4 + 1 and proves them |
| 1223–1239 | [Hin26a, Thm 5.2, §5.2, pp. …, §5] | b | section overview, radius names |
| 1254 | [Hin26a, Defs 2.1, 2.2, 2.5, …] | b | def:iv5-0-1 gives the definitions |
| 1273 | [Hin26a, §2] (∂_(z^μ) ∈ ρ_sf𝒱_3b) | a | T1: r⁻¹ ∈ ρ_sf C^∞(M^♭) |
| 1283, 1390 | [Hin26a, (5.19)] | b | notation |
| 1285–1286 | [Hin26a, §2.3] (supported and extendible spaces) | a-G1 | P-G1 C33-2 |
| 1288–1292 | [Hin26a, §2.3], [Hin23d] ×2, [Shu92], [Hin26d] ×3 (prop:np-10-65-a) | a-G1 | P-G1 C33-3, C33-4. [Hin26d] is published and quoted in Appendix A (thm:std-sbg-calculus) |
| 1297, 1329, 1331 | [Hin26a, Lemmas 2.3–2.4, …, Lemma 3.2, (3.2)] | b | proved in lem:iv5-0-2 |
| 1324 | [Hin26a, (2.13)–(2.14)], "with the same proof" | a | T2: the classes of ∇, □_g, δ*_g, δ_g proved |
| 1333, 1347 | [Hin26a, p. 15, Props 5.6, 5.16, p. 14] | b | lem:iv5-0-3, proved |
| 1363, 1366, 1380, 1383 | [Hin26a, Lemmas 3.3–3.9, Cor. 3.6, Lemma 3.9, Prop. 5.1] | b | lem:iv5-0-4, lem:iv5-0-5, proved |
| 1396 | [Hin26a] (cut-off conditions) | b | remark; the conditions are stated in T4 |
| 1400, 1406, 1407, 1412, 1425, 1438, 1440, 1467 | [Hin26a, Lemma 5.4, (5.20), Props 5.5, 5.6, (5.21), (5.22)] | b | the cut-offs of (5.20) are written out; (5.21)–(5.22) name eq:iv5-fib and eq:iv5-fib-adj |
| 1441 | [Hin26a, p. 45] (regularisation) | a-G1 | P-G1 C33-6 |
| 1443, 1447, 1454, 1457, 1458 | [Hin26a, (5.24)–(5.27), (5.29)] | b | displayed or described term by term; (5.26) uses square roots (P-G1 C33-8) |
| 1465 | [Hin26a, (5.25)] gives [Hin26a, (5.30)] | a | T42: (5.30) displayed |
| 1470–1471 | [Hin26a, (5.28)], [(5.29)] | a | T43: the pairing for P_h* displayed |
| 1477, 1488, 1503, 1506 | [Hin26a, (5.31)–(5.32), Prop. 5.8, (5.33)–(5.34)] | b | eq:iv5-2-1 is displayed; names |
| 1507 | χ_0, χ_K, ψ "as in [Hin26a, (5.35)]", [(5.36)] | a | T4 (cut-offs), T5 |
| 1508 | [Hin26a, (5.37)–(5.38)] | b | displayed (P-G1 C33-10 is the next line) |
| 1513–1514 | [Hin26a, (5.39)], "b_0, b_R, e and f those of [Hin26a, (5.40)–(5.43)]" | a | T4 (lem:iv5-2-symbols), T6 |
| 1528–1529 | [Hin26a, (5.44)–(5.46)] (the Q-terms) | a-G1 | P-G1 C33-11 |
| 1530–1531 | [Hin26a, (5.47)] gives [Hin26a, (5.48)]; the h^(1/2) iteration | a | T41, two variants (section 8) |
| 1534–1535 | "the b_0, b_K, e, f of [Hin26a]" | a | T7 |
| 1536 | [Hin26a, (5.44)–(5.45)] | a-G1 | P-G1 C33-12 |
| 1542, 1557, 1574, 1583, 1599, 1616, 1621, 1637 | [Hin26a, Props 5.9, 5.11, 5.12, (5.51)–(5.52), (5.55)–(5.56), (5.58)–(5.59)] | b | statements displayed in the paper; names |
| 1559–1561 | "χ_sf, χ_K and χ_0 as in [Hin26a]", [(5.53)], [(5.54)], "the b_0, b_sf, e and f of [Hin26a]" | a | T8, T9 |
| 1578 | "with the symbols of [Hin26a]" | a | T10 |
| 1602 | [Hin26a, (5.57)] (displayed; symbols undefined) | a | T11, T12 |
| 1641–1642 | [Hin26a, (5.60)], "the b_0, e_R, e_T and f of [Hin26a]" | a | T13, T14 |
| 1656, 1661–1663 | [Hin26a, pp. 57–58, (5.58), (5.59), (5.55)] | b | names of displayed forms |
| 1710 | [Hin26a, (5.44)–(5.46)], "and the iteration" | a-G1, a | P-G1 C33-15 (Q-terms); the iteration is that of prop:iv5-2-1 (T41) |
| 1713, 1750 | the adjoint pairing [Hin26a, (5.49)] | a | T7 (eq:iv5-2-adj), T15, T16 |
| 1758–1759, 1762–1763, 1834–1835 | [Hin26a, (5.61), Lemma 5.14, Cor. 5.15] | b | lem:iv5-6-tform and cor:iv5-6-energy, proved |
| 1904, 1926 | [Hin26a, Prop. 5.16, (5.66)–(5.69)], [Hin26a] (radii) | b | names of the four displayed estimates |
| 1935–1975 | [Hin26a, (5.66), (5.70)–(5.78), (5.67)–(5.69)], "as in [Hin26a]" | a | T17–T20: lem:iv5-6-transport, lem:iv5-6-core, the new proof |
| 1980–2092, 2110 | [Hin26a, Thm 5.2, Prop. 5.17, (5.18), (5.21), (5.22), (5.66)–(5.69), (5.80), (5.81)], "as in [Hin26a]" | b | names of displayed statements; (5.80) is displayed; the extension argument is written out |
| 2109 | [Hin26a, §2.3] (duality) | a-G1 | P-G1 C33-17 |
| 2119 | [Hin26a, p. 65] | b | the shift ½ is lem:iv5-0-2 (b) |
| 2124 | [Hin26a, p. 42] (the classical Cauchy theory) | a | T22, through Appendix A (thm:std-bgp-development, thm:std-bgp-cauchy (5), def:std-normally-hyperbolic) |
| 2135 | [Hin26a, (5.74) and (5.77)] | a | T21 |
| 2168–2180, 2223, 2260 | [Hin26a, Thm B.1, App. B, §B.4, (B.1), (B.3), (B.7)–(B.12), (B.15)–(B.18), (B.23)] | b | overview; the definitions are given; lem:iv6-0-1 and lem:iv6-0-flow, proved |
| 2316 | [Hin26a, (B.13)] | b, and the ambiguity treated in section 4 | T23 |
| 2322, 2339–2340, 2347, 2351 | [Hin26a, Prop. B.2, (B.21), (B.23), (B.26), (B.27)] | b | the commutant is displayed; (B.23) is lem:iv6-0-flow (c); (B.27) is derived |
| 2333 | the dual estimate [Hin26a, (B.28)], not displayed | a | T24 (eq:iv6-1-3) |
| 2341, 2345 | the shift [Hin26a, (B.24)], the symbol [Hin26a, (B.25)] | a | T25, T26 |
| 2360–2366 | [Hin26a, (B.20)] ×2, [p. 89] | a | T27 (eq:iv6-1-4) |
| 2369–2372 | [Hin26a, (B.29)], [p. 90] | a | T27 (complex σ by prop:i-a-4-9) |
| 2412–2413 | [Mel93, Thm 6.5], [Hin26a, p. 91] | c | thm:std-relative-index; applied outside its hypotheses (section 6) |
| 2439 | [Hin26a, Thm B.4] | b | |
| 2458 | [Hin26a, (B.34) and (B.35)], not displayed | a | T30 (eq:iv6-2-e1, eq:iv6-2-e2), T31 |
| 2466–2467 | [Hin26a, (B.37)], cut-offs of [Hin26a, (B.36)] | a | T32 |
| 2472 | [Hin26a, (B.38)] (displayed; symbols undefined) | a | T33 |
| 2488–2489, 2499 | [Hin26a, (B.39)], [(B.34)], [(B.40)] | a | T34, T35 |
| 2512–2524 | [Hin26a, (B.34)] ×7, [(B.37)], [(B.41)], [(B.40)] ×2, [(B.35)] | a | T36, T37 (eq:iv6-2-ap) |
| 2535 | [Hin26a, (B.37) and (B.39)] | a | T38 |
| 2539, 2541, 2551 | [Hin26a, Thm B.1, (B.44)] | b | (B.44) is displayed |
| 2571, 2585, 2588 | [Hin26a, Thm 6.2, p. 67, Def. 6.1] | b | the outgoing property used is written out |
| 2633–2635, 2666–2667 | [Hin26a, Thms B.1, 4.9 (3)], [Hin26, proof of Thm 7.1 (4)], [Hin26c, Def. 5.10, (9.115)] | b | remarks comparing routes; not used |
| 2673–3034 | [Hin26, Lemma 7.2, (7.10), Prop. 7.3, §7.2.1, Lemma 7.5, Prop. 7.4, (7.16), (7.19), (7.20), (7.31), (7.18), (8.13)] | b | each statement is proved in the paper: (7.10) is derived where it is used, (7.19) is stated and proved in a stronger form, and (8.13) is described and is prop:np-10-52 |
| 3584 | [Hin26, (8.13)] | b | the condition is described where it is used and proved in prop:np-10-52 |

## 3. A statement that needs correcting: the second estimate of prop:iv5-6-1 (1)

### 3.1 The problem

The chapter states the estimate "for every ω ∈ ρ_sf^(−α_sf−2)H²_(3b,h), without support condition". This is false near
the corner X_0 ∩ Σ^♯.

- Σ^♯ is a final hypersurface: dr is future timelike on [½r_♯, r̂] (lem:iv5-0-3 (c)).
- For the backward problem of P_h*, Σ^♯ is therefore a boundary through which data enter.

### 3.2 The counterexample

1. Fix h ∈ (0, 1] and t_1 ∈ (0, ½T_0r_♯). Take p ∈ Σ^♯ with 0 < t(p) < t_1, so 0 < τ(p) < T_0/2.
2. Let F be a smoothed maximum of t − t_1 and r_♯ − r, with dF a convex combination of dt and −dr. Put
   S₀ := {F = 0} ∩ {r > ½r_♯}.
   - Both differentials are past timelike on {½r_♯ ≤ r ≤ r̂}, by lem:iv5-0-3 (a) and (c), so S₀ is spacelike.
   - S₀ coincides with Σ^♯ near p.
   - S₀ is acausal. After a future causal curve leaves S₀, either t > t_1 or r < r_♯, and r keeps decreasing inside
     {r ≤ r̂}. So F > 0 from then on.
3. Every inextendible causal curve through a point of {r ≥ r_♯} meets S₀. If F < 0 at the point, the future part of
   the curve reaches F = 0 while r > ½r_♯. If F > 0, the past part does.
   - So {r ≥ r_♯} lies in D(S₀).
   - By thm:std-bgp-development and thm:std-bgp-cauchy (5) there is a smooth ω on D(S₀) with P_h*ω = 0, whose Cauchy
     data on S₀ are supported in a small neighbourhood K of p in S₀ ∩ Σ^♯, and with ω(p) ≠ 0. P_h* is normally
     hyperbolic up to the factor h².
4. supp ω ⊂ J(K).
   - Future causal curves from K enter {r < r_♯} and stay there.
   - Past causal curves from K have t < t_1 < ½T_0r_♯ ≤ ½T_0r on {r ≥ r_♯}, so τ < T_0/2 there.
   - So on M^♭, ω vanishes on τ⁻¹([T_0/2, T_0]).
5. Multiply ω by a cut-off in t that equals 1 on {t ≥ 0} and 0 on {t ≤ −1}. The product:
   - has compact support in M^♭, so it lies in ρ_sf^(−α_sf−2)H²_(3b,h);
   - satisfies P_h* = 0 on τ⁻¹([0, T_0]) and vanishes on τ⁻¹([T_0/2, T_0]);
   - is nonzero near p.
   So the left side of the estimate is positive and the right side is 0, for every h.

### 3.3 The fix and its effect

T19 adds the hypothesis "supported at Σ^♯ (as are the elements of the spaces (·)^(−,•) of def:iv5-0-1)".

- Its only use is prop:iv5-7-2 (x), on ω′ ∈ H(Ω)^(−,•). Those ω′ are supported at Σ^♯, so the use is unaffected.
- The analogue on M in thm:iv6-2-1, eq:iv6-2-e2, has no inner boundary and needs no condition.
- The fourth estimate, (2) for P_h*, already asks ω to vanish for r < r_1.

This is the same gap as in [Hin26a, (5.67)], whose statement the chapter followed. The coordinator should decide it with
the author.

## 4. def:iv6-0-2: the fix and every use

### 4.1 The fix

The old definition asked ℓ to be "non-increasing along σH_(G_σ)". For complex σ the symbol G_σ is complex, so that
condition has no clear meaning. The new definition (T23) reads as follows.

- **Real σ₀ ≠ 0.** It defines R_(σ₀,in) := {ρ = 0, ξ = 2σ₀, η = 0} and Char_(σ₀) := {ρ = 0, G_(σ₀) = 0}, where G_(σ₀) is
  real.
- **Admissible at σ.** It always asks β ∈ (0, 2 + C_0], and that ℓ be constant near R_out with ℓ below the threshold
  −½ + h⁻¹(1 − e)(1 − v) there. When σ is real, it also asks that ℓ be constant near R_(σ,in) with
  ℓ > −½ − h⁻¹(1 − e)(1 + v) there, and that σ𝖧_(G_σ)ℓ ≤ 0 on Char_σ. G_σ is real for real σ, so this is
  unambiguous.
- **Im σ > 0.** Nothing is asked off R_out, which is then the whole characteristic set over ρ = 0
  (lem:iv6-0-flow (a)). The proof uses nothing more there: off R_out only elliptic estimates, at R_out the sink estimate.
- **Admissible on a set.** Fixed orders are *admissible on* a set if they are admissible at each σ in it and at Re σ
  for each σ in it with Re σ ≠ 0. This is chapter 20's convention: "for complex σ = σ₀ + iσ₁ the orders used are those
  for σ₀" (sec:i-a-1-4). It is the reading that F-G24's proof of the uniformity already used.

### 4.2 The alternative that was rejected

Requiring admissibility at Re σ at every complex σ would impose a lower bound on the constant middle-sector orders of
chapter 22 (𝗋_mid). Chapter 22 does not impose that bound, and with it thm:iv6-4-1 could fail for very negative
𝗋_mid. Admissibility at Re σ is therefore asked only through "admissible on a set". That phrase is used only for the
uniformity near ±1.

### 4.3 The uses, each checked

1. **prop:iv6-1-1, statement** ("admissible at σ ∈ e^(i[0,π])"; "do not depend on the admissible (s, ℓ, β)"). Now well
   defined. The uniformity clause reads "for fixed orders admissible on that set" (T24).
2. **prop:iv6-1-1, proof, real and complex σ** (T27). An order admissible at σ satisfies the hypotheses of the pieces of
   chapter 20 at σ₀ = σ: (O2) and the thresholds at R_out and R_in, with the thresholds identified in the text.
3. **prop:iv6-1-1, proof, uniformity** (T29). "Admissible on the set" gives admissibility at every real σ₀ in the
   compact interval I of the Re σ. It also gives uniform margins and constancy neighbourhoods, because ℓ is constant near
   the connected compact union of the R_(σ₀,in). This is the hypothesis of thm:i-a-7-2 (1) and prop:i-a-4-6.
4. **prop:iv6-1-1, index 0.** The order of chapter 22 for the free operator is admissible at every σ for every
   h⁻¹ ≥ 0, as the text says.
   - At θ ∈ {0, π}, the order of lem:i-a-7-1 with ϑ_in = 0 and S̄ = 0 is admissible for σ₀ = ±1, with 𝗋_in > −½ and
     𝗋_out < −½.
   - At θ ∈ (0, π), 𝗋_mid is a constant below −½. Under the new definition only the threshold at R_out is asked.
5. **thm:iv6-3-1.** "Every (s, ℓ, β) admissible at σ" is now well defined. The uniformity clause reads "in each set on
   which fixed orders are admissible and eq:iv6-1-2 holds uniformly" (T39). Its proof uses ℓ = −½, a constant order,
   which is admissible at every σ.
6. **thm:iv6-4-1.** Two kinds of order occur (T40).
   - The orders 𝗋_± of chapter 22 are admissible for every σ₀ ∈ J_± ∋ Re e^(iθ). So they are admissible on
     {e^(iθ) : θ ∈ Θ_±}.
   - The constant orders used for θ ∈ (0, π) are admissible at each such σ.
   - The thresholds coincide with those of eq:i-a-1-5, as the text already shows.
7. **Other chapters.** No other chapter cites def:iv6-0-2 (checked by grep).

## 5. Placement

This part and the crosswalk rows are instructions for merging; they are not chapter text. Each old text is quoted
exactly between the fences, and each new text replaces it as a whole, with the line breaks shown. The line numbers are
those of the chapter at HEAD (md5 147ca162…) and serve only to find the place. The texts are listed in the order of
their place in the chapter; they are pairwise disjoint and may be applied in any order. Equation labels are
right-aligned so that no line exceeds 121 characters, also after the labels resolve.

### T1. def:iv5-0-1, the 3b vector fields (lines 1273–1273)

Old (1 lines):

```text
Diff^k_3b with weights; ∂_(z^μ) ∈ ρ_sf 𝒱_3b(M^♭) by [Hin26a, Section 2];
```

New (2 lines):

```text
Diff^k_3b with weights; ∂_(z^μ) = r⁻¹ · r∂_(z^μ) ∈ ρ_sf 𝒱_3b(M^♭), as r⁻¹ ∈ ρ_sf C^∞(M^♭) (r⁻¹ = ρ_sf near 𝗌𝖿,
and r ≥ r_♯);
```

### T2. lem:iv5-0-2 (c), proof (lines 1324–1325)

Old (2 lines):

```text
because ∂_(z^μ) ∈ ρ_sf 𝒱_3b. The rest is [Hin26a, (2.13)–(2.14)], with the same proof. (On Tangherlini space,
Γ ∈ mρ³C^∞ by [[prop:np-10-22]] (i).)
```

New (6 lines):

```text
because ∂_(z^μ) ∈ ρ_sf 𝒱_3b. In the frame dz^μ, ∇_(∂_(z^μ)) acts on components as ∂_(z^μ) + Γ_μ, with one
Christoffel symbol for each index; so ∇ = Σ_μ dz^μ ⊗ (∂_(z^μ) + Γ_μ) lies in ρ_sf Diff¹_3b. For V = r∂_(z^μ), the
function ρ_sf⁻¹V(ρ_sf) is smooth on M^♭: near 𝗌𝖿 it is −∂_(z^μ)r, which is 0 or −x^i/r, and elsewhere ρ_sf is smooth
and positive. Hence ρ_sf^a Diff^k_3b ∘ ρ_sf^b Diff^l_3b ⊂ ρ_sf^(a+b) Diff^(k+l)_3b, and, with g^(μν) ∈ C^∞(M^♭) by
(a), □_g = −g^(μν)(∇∇)_(μν) ∈ ρ_sf² Diff²_3b, while δ*_g, the symmetrisation of ∇, and δ_g, the contraction of ∇ with
−g⁻¹, lie in ρ_sf Diff¹_3b. (On Tangherlini space, Γ ∈ mρ³C^∞ by [[prop:np-10-22]] (i).)
```

### T3. lem:iv5-0-5, the size of δ_r (lines 1382–1382)

Old (1 lines):

```text
there are δ_r ∈ (0, (4r_c)⁻¹) and δ_sf = 1/100 such that for b ∈ U, c satisfies the conditions (1)–(6) of
```

New (1 lines):

```text
there are δ_r ∈ (0, min((4r_c)⁻¹, 1/5)) and δ_sf = 1/100 such that for b ∈ U, c satisfies the conditions (1)–(6) of
```

### T42. prop:iv5-1-3, the inequality after the Cauchy–Schwarz step (lines 1465–1465)

Old (1 lines):

```text
*Conclusion.* Cauchy–Schwarz on the left of [Hin26a, (5.25)] gives [Hin26a, (5.30)]. Drop ‖E_Rω‖², which has the sign
```

New (9 lines):

```text
*Conclusion.* Let Λ⁻ be a microlocal parametrix of Λ* near supp a. By [Hin26a, (5.25)–(5.26)] and the split of the
commutator, with ∓Im⟨P_hω, A²ω⟩ ≤ (4c_0)⁻¹‖Λ⁻AP_hω‖² + c_0‖ΛAω‖² + h^(2N)‖ω‖²_(H^(−N,(α_sf,α_K))_(3b,h)), the terms
c_0‖ΛAω‖² cancel and

    ‖B̃_0Aω‖² + h‖E_Rω‖² ≤ (4c_0)⁻¹‖Λ⁻AP_hω‖² + h‖E_Tω‖² + h|⟨B̃_2Aω, Aω⟩| + h|⟨(E + F)ω, ω⟩|
                             + h|⟨AQP_hω, ω⟩| + Ch^(2N)‖ω‖²_(H^(−N,(α_sf,α_K))_(3b,h))

([Hin26a, (5.30)]), F collecting the remainders of the split, microsupported near supp a; the term with Q is bounded by
the elliptic estimate, WF′(Q) lying off the characteristic set. Drop ‖E_Rω‖², which has the sign
```

### T43. prop:iv5-1-3, the pairing for P_h* (lines 1470–1471)

Old (2 lines):

```text
For [Hin26a, (5.22)], P_h* = □_h* + iL_h* with □_h* − □_h ∈ hDiff¹ and L_h* − L_h ∈ hDiff⁰, and [Hin26a, (5.28)] has
main term ∓ρ_sf⁻²ℓ, now negative definite. The weights in a become (−α_sf − 2, −α_K). [Hin26a, (5.29)] holds for P_h*,
```

New (3 lines):

```text
For [Hin26a, (5.22)], P_h* = □_h* + iL_h* with □_h* − □_h ∈ hDiff¹ and L_h* − L_h ∈ hDiff⁰, and the pairing is now
∓Im⟨P_h*ω, A²ω⟩ = ⟨(∓(Re L_h − Im □_h)A² ∓ (i/2)[P_h*, A²])ω, ω⟩ ([Hin26a, (5.28)]), whose main term has the symbol
∓ρ_sf⁻²ℓ, now negative definite. The weights in a become (−α_sf − 2, −α_K). The split of the commutator holds for P_h*,
```

### T4. sec:iv5-2, commutants of product form and the symbol identity (inserted before prop:iv5-2-1) (lines 1485–1487)

Old (3 lines):

```text
self-adjoint). The symbol j of J is homogeneous of degree 3 and vanishes cubically at o. Near (K⁺)°, ρ_K := t⁻¹, and the
weight at 𝗌𝖿 and the differential order are dropped.

```

New (36 lines):

```text
self-adjoint). The symbol j of J is homogeneous of degree 3 and vanishes cubically at o. Near (K⁺)°, ρ_K := t⁻¹, and the
weight at 𝗌𝖿 and the differential order are dropped.

*Commutants near o.* A *cut-off* below is a smooth function χ of one variable with values in [0, 1], equal to 1 on a
closed interval J, positive on a larger interval I that is open in the range of the variable, and 0 outside I,
non-decreasing to the left of J and non-increasing to its right, such that (χχ′)^(1/2) is smooth to the left of J and
(−χχ′)^(1/2) to its right; "supported in I" refers to this I. Such cut-offs exist: with φ(x) := e^(−1/x) for x > 0
and φ(x) := 0 for x ≤ 0, the function χ(x) := φ(β − x)/(φ(β − x) + φ(x − α)), α < β, is equal to 1 on (−∞, α],
positive on (−∞, β) and 0 on [β, ∞), and near α and near β the function −χχ′ is the square of a smooth positive
function times φ(x − α)^(1/2)(x − α)⁻¹, resp. φ(β − x)(β − x)⁻¹; cut-offs equal to 1 on a bounded J are products of
two such functions, one of them reflected. Also χ₁(x) := e^(−𝔛/x) for x > 0, χ₁(x) := 0 for x ≤ 0, is used, with
χ₁′ = 𝔛x⁻²χ₁ and (χ₁χ₁′)^(1/2) = 𝔛^(1/2)x⁻¹χ₁ smooth. Every commutant in [[sec:iv5-2]]–[[sec:iv5-5]] has the form

    a = w⁻¹φ_1⋯φ_mχ_0(𝔛|ζ|),                                                                                {#eq:iv5-2-a}

with w a positive function (a product of powers of boundary defining functions), each φ_k a cut-off or χ₁, composed
with a function on M^♭, 𝔛 ≥ 1, and χ_0 a cut-off equal to 1 on [0, 1] and supported in [0, 2); we put
a_k := w⁻¹χ_0(𝔛|ζ|)Π_(k′≠k) φ_(k′). The square roots of the symbols below are smooth: each is taken of a product of
a factor ±φ_kφ_k′ ≥ 0 (or χ₁′/χ₁ times a²), whose square root is smooth on the support in question, with a B-self-adjoint
factor that is positive definite there. In [[prop:iv5-5-3]] (2) the factor called f is one of the φ_k, not the symbol f
of [[lem:iv5-2-symbols]].

**Lemma {#lem:iv5-2-symbols}** (The commutator symbol of a product commutant; the form of [Hin26a, (5.39)–(5.43)].) For
a as in [[eq:iv5-2-a]] and either choice of sign,

    aH_(−ℓ+j)a ∓ Sa² = −a²(±S − ℓ(dw/w) − wH_j(w⁻¹)) + Σ_k a_k²φ_k(−ℓ(dφ_k) + H_jφ_k) + f,
    f := w⁻²(φ_1⋯φ_m)²χ_0(𝔛|ζ|)H_(−ℓ+j)(χ_0(𝔛|ζ|)),                                                   {#eq:iv5-2-leibniz}

and f is supported in supp a ∩ {1 ≤ 𝔛|ζ| ≤ 2}, off o.

*Proof.* H_(−ℓ+j), the Hamilton vector field of the End-valued symbol −ℓ + j, acts on scalar symbols as a derivation:
H(uv) = uHv + vHu. For a function φ on M^♭, H_(−ℓ)φ = −ℓ(dφ), ℓ being linear in the fibre; so
wH_(−ℓ+j)(w⁻¹) = w⁻¹ℓ(dw) + wH_j(w⁻¹) = ℓ(dw/w) + wH_j(w⁻¹). The Leibniz rule for the m + 2 factors of a gives
H_(−ℓ+j)a = a·wH_(−ℓ+j)(w⁻¹) + Σ_k a_kH_(−ℓ+j)φ_k + w⁻¹φ_1⋯φ_mH_(−ℓ+j)(χ_0(𝔛|ζ|)); multiplying by a and using
a·a_k = a_k²φ_k gives [[eq:iv5-2-leibniz]]. The support of f is that of χ_0′(𝔛|ζ|) within supp a. ∎

```

### T5. prop:iv5-2-1 (1), the cut-offs (lines 1507–1507)

Old (1 lines):

```text
for P_h, near o. With χ_0, χ_K and ψ as in [Hin26a, (5.35)] (r_c for r_0), take the commutant [Hin26a, (5.36)],
```

New (2 lines):

```text
for P_h, near o. Let χ_K be a cut-off equal to 1 on [0, 1] and supported in [0, 3), and ψ = ψ(r) a cut-off equal to 1
on {|r − r_c| ≤ (55/50)ε_c} and supported in {|r − r_c| < (60/50)ε_c} ([Hin26a, (5.35)]). Take the commutant
```

### T6. prop:iv5-2-1 (1), the symbols b_0, b_R, e, f (lines 1513–1514)

Old (2 lines):

```text
M^♭. This gives [Hin26a, (5.39)], aH_(−ℓ+j)a − Sa² = −c_0a² − b_0² − b_R² + e² + f, with b_0, b_R, e and f those of
[Hin26a, (5.40)–(5.43)]. Their square roots exist for the following reasons.
```

New (9 lines):

```text
M^♭. So [[lem:iv5-2-symbols]], with w = ρ_K^(α_K), φ_1 = ψ(r) and φ_2 = χ_K(𝔛ρ_K), gives
aH_(−ℓ+j)a − Sa² = −c_0a² − b_0² − b_R² + e² + f ([Hin26a, (5.39)]), with f as there and, as ρ_K⁻¹ = t and
dρ_K/ρ_K² = −dt, so that ℓ(dw/w) = −α_Kρ_Kℓ(dt) and wH_j(w⁻¹) = α_Kρ_KH_jt,

    b_0 := a(S − c_0 + α_Kρ_K(ℓ(dt) − H_jt))^(1/2),     b_R := ρ_K^(−α_K)χ_Kχ_0(ψψ′(ℓ(dr) − H_jr))^(1/2),
    e := ρ_K^(−α_K)ψχ_0ρ_K(−𝔛χ_Kχ_K′)^(1/2)(ℓ(−dt) + H_jt)^(1/2),

χ_K and χ_K′ being evaluated at 𝔛ρ_K, χ_0 at 𝔛|ζ|. H_jt and H_jr are O(|ζ|²), j vanishing cubically at o. Their square
roots exist for the following reasons.
```

### T41. prop:iv5-2-1 (1), the passage from the symbol identity to the estimate (variant for the current text) (lines 1530–1531)

Old (2 lines):

```text
Collecting, fix 𝔛 large and then h small to absorb ‖Aω‖². Then [Hin26a, (5.47)], with WF′(F) ⊂ Ell(𝓛_h), gives
[Hin26a, (5.48)], and finitely many iterations in h^(1/2) give [Hin26a, (5.33)], with δ := 𝔛⁻¹.
```

New (21 lines):

```text
Collecting, fix 𝔛 large and then h small to absorb ‖Aω‖². Let B_0, B_R, E and F be quantisations of b_0, b_R, e and
f, and B̃_0 ∈ Ψ_(3b,ħ) elliptic on a neighbourhood of supp a in which A is microsupported. The pairing, the symbol
identity and the bound |h⁻¹⟨A𝓛_hω, Aω⟩| ≤ ¼c_0‖Aω‖² + c_0⁻¹h⁻²‖A𝓛_hω‖² give

    c_0‖Aω‖² + ‖B_0ω‖² + ‖B_Rω‖²
        ≤ C(h⁻²‖A𝓛_hω‖² + ‖Eω‖² + |⟨Fω, ω⟩| + h‖B̃_0ω‖² + h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h))),

the term h‖B̃_0ω‖² collecting the remainders of the symbol calculus ([Hin26a, (5.47)]). As WF′(F) lies off o and in
Ell(𝓛_h), [[prop:iv5-1-2]] gives |⟨Fω, ω⟩| ≤ C(‖B̃_0𝓛_hω‖² + h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h))). Dropping
‖B_Rω‖²,

    ‖B_0ω‖ ≤ C(h⁻¹‖B̃_0𝓛_hω‖ + ‖Eω‖ + h^(1/2)‖B̃_0ω‖ + h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)))                 {#eq:iv5-2-iter}

([Hin26a, (5.48)]). The positivity used holds, by continuity, for commutants whose supports are larger by a fixed small
amount; so the same argument bounds h^(1/2)‖B̃_0ω‖ by h^(1/2) times the right side with B̃_0 replaced by an operator
B̃_1 of the same kind, and after 2N such steps the remaining term is h^N‖B̃_(2N)ω‖, which is at most
Ch^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)), B̃_(2N) being microsupported in a compact set at finite frequencies. On the operator
wave front set of the B_0 of the statement, b_0 is elliptic where the fibre variable has length at most 𝔛⁻¹, and
[[prop:iv5-1-2]] applies where it has length at least 𝔛⁻¹. The quantisation of e is bounded by the E of the statement,
whose elliptic set contains supp e, and B̃_0𝓛_hω by B_1P_hω, B̃_0 being microsupported in Ell(B_1), each up to
h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)). This gives [Hin26a, (5.33)], with δ := 𝔛⁻¹.
```

Variant A of T41, to be used instead of T41 when P-G1's text C33-11 is merged first, as it will be. Its old text is
the end of the new text of C33-11, from its second-to-last line, without the quotation marks of P-G1:

```text
and then h small to absorb ‖Aω‖². Then [Hin26a, (5.47)], with WF′(F) ⊂ Ell(𝓛_h) and [[prop:np-10-65-a]] (e), gives
[Hin26a, (5.48)], and finitely many iterations in h^(1/2) give [Hin26a, (5.33)], with δ := 𝔛⁻¹.
```

New:

```text
and then h small to absorb ‖Aω‖². Let B_0, B_R, E and F be quantisations of b_0, b_R, e and f, and
B̃_0 ∈ Ψ_(3b,ħ) elliptic on a neighbourhood of supp a in which A is microsupported. The pairing, the symbol
identity and the bound |h⁻¹⟨A𝓛_hω, Aω⟩| ≤ ¼c_0‖Aω‖² + c_0⁻¹h⁻²‖A𝓛_hω‖² give

    c_0‖Aω‖² + ‖B_0ω‖² + ‖B_Rω‖²
        ≤ C(h⁻²‖A𝓛_hω‖² + ‖Eω‖² + |⟨Fω, ω⟩| + h‖B̃_0ω‖² + h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h))),

the term h‖B̃_0ω‖² collecting the remainders of the symbol calculus ([Hin26a, (5.47)]). As WF′(F) lies off o and in
Ell(𝓛_h), [[prop:np-10-65-a]] (e) gives |⟨Fω, ω⟩| ≤ C(‖B̃_0𝓛_hω‖² + h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h))). Dropping
‖B_Rω‖²,

    ‖B_0ω‖ ≤ C(h⁻¹‖B̃_0𝓛_hω‖ + ‖Eω‖ + h^(1/2)‖B̃_0ω‖ + h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)))                 {#eq:iv5-2-iter}

([Hin26a, (5.48)]). The positivity used holds, by continuity, for commutants whose supports are larger by a fixed small
amount; so the same argument bounds h^(1/2)‖B̃_0ω‖ by h^(1/2) times the right side with B̃_0 replaced by an operator
B̃_1 of the same kind, and after 2N such steps the remaining term is h^N‖B̃_(2N)ω‖, which is at most
Ch^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)), B̃_(2N) being microsupported in a compact set at finite frequencies. On the operator
wave front set of the B_0 of the statement, b_0 is elliptic where the fibre variable has length at most 𝔛⁻¹, and
[[prop:iv5-1-2]] applies where it has length at least 𝔛⁻¹. The quantisation of e is bounded by the E of the statement,
whose elliptic set contains supp e, and B̃_0𝓛_hω by B_1P_hω, B̃_0 being microsupported in Ell(B_1), each up to
h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)). This gives [Hin26a, (5.33)], with δ := 𝔛⁻¹.
```

### T7. prop:iv5-2-1 (2), the adjoint pairing and its symbols (lines 1533–1536)

Old (4 lines):

```text
(2) Replace P_h* by 𝓛_h* = iP_h*(1 − iCρ_sf⁻²L_h) = −L_h* + J + iQ and take
a = ρ_K^(α_K)ψχ_K(𝔛ρ_K)χ_0(𝔛|ζ|). The main symbol is aH_(−ℓ+j)a + Sa² = c_0a² + b_0² + b_K² − e² + f with the b_0, b_K,
e, f of [Hin26a]. The same three facts give the square roots, now with b_K from the sign of −ℓ(dt) and e from
[[lem:iv5-0-5]] (6) on supp ψ′.
```

New (11 lines):

```text
(2) Replace P_h* by 𝓛_h* = iP_h*(1 − iCρ_sf⁻²L_h) = −L_h* + J + iQ and take
a = ρ_K^(α_K)ψχ_K(𝔛ρ_K)χ_0(𝔛|ζ|). As J and Q are self-adjoint and Im(−L_h*) = Im L_h = hS, the pairing is

    h⁻¹Im⟨𝓛_h*ω, A²ω⟩ = ⟨𝒞′ω, ω⟩,     𝒞′ = ((i/(2h))[−L_h* + J, A²] + h⁻¹(Im L_h)A²) + h⁻¹AQA + (1/(2h))[A, [A, Q]]
                                                                                                          {#eq:iv5-2-adj}

([Hin26a, (5.49)–(5.50)]), and the bracket has principal symbol aH_(−ℓ+j)a + Sa². By [[lem:iv5-2-symbols]] with
w = ρ_K^(−α_K), the main bracket S + ℓ(dw/w) + wH_j(w⁻¹) is again S + α_Kρ_K(ℓ(dt) − H_jt), and
aH_(−ℓ+j)a + Sa² = c_0a² + b_0² + b_K² − e² + f, where b_0, b_K and e are the b_0, e and b_R of (1) with ρ_K^(α_K) for
ρ_K^(−α_K). The same three facts give the square roots, now with b_K from the sign of −ℓ(dt) and e from
[[lem:iv5-0-5]] (6) on supp ψ′.
```

### T8. prop:iv5-3-1 (1), the cut-offs and symbols (lines 1559–1562)

Old (4 lines):

```text
*Proof.* (1) Replace P_h by 𝓛_h. With χ_sf, χ_K and χ_0 as in [Hin26a], take the commutant [Hin26a, (5.53)],
a = w⁻¹χ_sf(𝔛ρ_sf)χ_K(ρ_K)χ_0(𝔛|ζ|). Then 𝒞 ∈ ρ_sf^(−2α_sf)ρ_K^(−2α_K)Ψ_3b, and [Hin26a, (5.54)] holds:
aH_(−ℓ+j)a − Sa² = −c_0ρ_sf²a² − b_0² − b_sf² + e² + f, with the b_0, b_sf, e and f of [Hin26a]. Their square roots
exist for the following reasons.
```

New (9 lines):

```text
*Proof.* (1) Replace P_h by 𝓛_h. Let χ_sf be a cut-off equal to 1 on [0, 5/4] and supported in [0, 2), and χ_K a
cut-off equal to 1 on [0, (5/4)δ_r] and supported in [0, 2δ_r). Take the commutant ([Hin26a, (5.53)])
a = w⁻¹χ_sf(𝔛ρ_sf)χ_K(ρ_K)χ_0(𝔛|ζ|). Then 𝒞 ∈ ρ_sf^(−2α_sf)ρ_K^(−2α_K)Ψ_3b, and [[lem:iv5-2-symbols]] gives
aH_(−ℓ+j)a − Sa² = −c_0ρ_sf²a² − b_0² − b_sf² + e² + f ([Hin26a, (5.54)]), with f as there and, as dρ_sf = −ρ_sf²dr,

    b_0 := a(S − ℓ(dw/w) − wH_j(w⁻¹) − c_0ρ_sf²)^(1/2),     b_sf := w⁻¹χ_sfχ_0(−χ_Kχ_K′)^(1/2)(−ℓ(dρ_K) + H_jρ_K)^(1/2),
    e := w⁻¹χ_Kχ_0ρ_sf(−𝔛χ_sfχ_sf′)^(1/2)(−ℓ(dr) + H_jr)^(1/2),

χ_sf and χ_sf′ being evaluated at 𝔛ρ_sf, χ_K and χ_K′ at ρ_K. Their square roots exist for the following reasons.
```

### T9. prop:iv5-3-1 (1), the support of χ_K′ (lines 1567–1567)

Old (1 lines):

```text
- b_sf: on supp χ′_K, ρ_K ∈ [(5/4)δ_r, (3/2)δ_r), and [[lem:iv5-0-5]] (6) on 𝗌𝖿 ∩ {r/t ∈ [δ_r, v(1 − δ_sf)]} gives
```

New (2 lines):

```text
- b_sf: on supp χ′_K, ρ_K ∈ [(5/4)δ_r, 2δ_r) ⊂ [δ_r, v(1 − δ_sf)], as δ_r < 1/5, and [[lem:iv5-0-5]] (6) on
𝗌𝖿 ∩ {r/t ∈ [δ_r, v(1 − δ_sf)]} gives
```

### T10. prop:iv5-3-1 (2), its symbols (lines 1578–1579)

Old (2 lines):

```text
aH_(−ℓ+j)a + Sa² = c_0ρ_sf²a² + b_0² + b_K² − e² + f, with the symbols of [Hin26a]. These are those of (1) with
−α_sf − 2 for α_sf; b_0 comes from [[lem:iv5-0-5]] (4), and the a priori term from supp χ′_K. ∎
```

New (3 lines):

```text
aH_(−ℓ+j)a + Sa² = c_0ρ_sf²a² + b_0² + b_K² − e² + f by [[lem:iv5-2-symbols]] with w⁻¹ in place of w, where b_0, b_K
and e are the b_0, e and b_sf of (1) with the prefactor w in place of w⁻¹: the main bracket S + ℓ(d(w⁻¹)/w⁻¹) + w⁻¹H_jw
is again S − ℓ(dw/w) − wH_j(w⁻¹). b_0 comes from [[lem:iv5-0-5]] (4), and the a priori term from supp χ′_K. ∎
```

### T11. prop:iv5-4-1 (1), cut-offs and symbols (lines 1601–1603)

Old (3 lines):

```text
*Proof.* (1) The commutant is a = (w′)⁻¹χ_sf(𝔛ρ_sf)χ_R((r/t)/v − 1)χ_0(𝔛|ζ|), with χ_R supported in
(−2δ_sf, 2δ_sf) and equal to 1 on [−(5/4)δ_sf, (5/4)δ_sf]. Then [Hin26a, (5.57)] holds:
aH_(−ℓ+j)a − Sa² = −c_0ρ_sf²a² − b_0² + e₁² + e₂² + f. Their square roots exist for the following reasons.
```

New (9 lines):

```text
*Proof.* (1) The commutant is a = (w′)⁻¹χ_sf(𝔛ρ_sf)χ_R((r/t)/v − 1)χ_0(𝔛|ζ|), with χ_sf as in [[prop:iv5-3-1]] and
χ_R a cut-off supported in (−2δ_sf, 2δ_sf) and equal to 1 on [−(5/4)δ_sf, (5/4)δ_sf]. With s := r/t,
[[lem:iv5-2-symbols]] gives aH_(−ℓ+j)a − Sa² = −c_0ρ_sf²a² − b_0² + e₁² + e₂² + f ([Hin26a, (5.57)]), with f as there,

    b_0 := a(S − ℓ(dw′/w′) − w′H_j((w′)⁻¹) − c_0ρ_sf²)^(1/2),
    e₁ := (w′)⁻¹χ_Rχ_0ρ_sf(−𝔛χ_sfχ_sf′)^(1/2)(−ℓ(dr) + H_jr)^(1/2),
    e₂ := (w′)⁻¹χ_sfχ_0(v⁻¹χ_Rχ_R′(−ℓ(ds) + H_js))^(1/2),

χ_R and χ_R′ being evaluated at s/v − 1. Their square roots exist for the following reasons.
```

### T12. prop:iv5-4-1 (2), its symbols (lines 1615–1615)

Old (1 lines):

```text
(2) Take a = w′χ_sf(𝔛ρ_sf)χ_R((r/t)/v − 1)χ_0(𝔛|ζ|). Then aH_(−ℓ+j)a + Sa² = c_0ρ_sf²a² + b_0² + b₁² + b₂² + f. Every
```

New (3 lines):

```text
(2) Take a = w′χ_sf(𝔛ρ_sf)χ_R((r/t)/v − 1)χ_0(𝔛|ζ|). Then [[lem:iv5-2-symbols]] gives
aH_(−ℓ+j)a + Sa² = c_0ρ_sf²a² + b_0² + b₁² + b₂² + f, with b_0 as in (1) and b₁, b₂ the e₁, e₂ of (1) with the prefactor
w′ in place of (w′)⁻¹. Every
```

### T13. prop:iv5-5-1 (1), cut-offs and symbols (lines 1640–1642)

Old (3 lines):

```text
*Proof.* (1) The commutant is a = ρ_K^(−α_K)χ₁(r − r_1)χ₂(r)χ_K(ρ_K)χ_0(𝔛|ζ|), where χ₁(x) = e^(−𝔛/x) for x > 0, so
χ₁′(x) = 𝔛x⁻²χ₁(x). Then [Hin26a, (5.60)] holds: aH_(−ℓ+j)a − Sa² = −a² − b_0² + e_R² + e_T² + f, with the b_0, e_R,
e_T and f of [Hin26a]. The square roots exist for the following reasons.
```

New (11 lines):

```text
*Proof.* (1) The commutant is a = ρ_K^(−α_K)χ₁(r − r_1)χ₂(r)χ_K(ρ_K)χ_0(𝔛|ζ|), where χ₁(x) = e^(−𝔛/x) for x > 0, so
χ₁′(x) = 𝔛x⁻²χ₁(x), χ₂ is a cut-off equal to 1 on (−∞, r_3] and supported in (−∞, r_4), and χ_K a cut-off equal to 1
on [0, t_3⁻¹] and supported in [0, t_1⁻¹). Then [[lem:iv5-2-symbols]] with w = ρ_K^(α_K), as in [[prop:iv5-2-1]], gives
aH_(−ℓ+j)a − Sa² = −a² − b_0² + e_R² + e_T² + f ([Hin26a, (5.60)]), with f as there and, χ₁ and χ₁′ being evaluated
at r − r_1,

    b_0 := a(S + α_Kρ_K(ℓ(dt) − H_jt) + (χ₁′/χ₁)(ℓ(dr) − H_jr) − 1)^(1/2),
    e_R := ρ_K^(−α_K)χ₁χ_Kχ_0(−χ₂χ₂′)^(1/2)(ℓ(dr) − H_jr)^(1/2),
    e_T := ρ_K^(−α_K)χ₁χ₂χ_0ρ_K(−χ_Kχ_K′)^(1/2)(ℓ(−dt) + H_jt)^(1/2),

the term of χ₁ being −a²(χ₁′/χ₁)(ℓ(dr) − H_jr). The square roots exist for the following reasons.
```

### T14. prop:iv5-5-1 (2), its symbols (lines 1653–1654)

Old (2 lines):

```text
(2) Take a = ρ_K^(α_K)χ₁(r_4 − r)χ̃₂(r)χ_K(ρ_K)χ_0(𝔛|ζ|), with χ̃₂ = 0 near (−∞, r_1] and 1 near [r_2, ∞). Then
aH_(−ℓ+j)a + Sa² = a² + b_0² + b_T² − e_R² + f, and the only a priori term is e_R, on supp χ̃₂′. ∎
```

New (4 lines):

```text
(2) Take a = ρ_K^(α_K)χ₁(r_4 − r)χ̃₂(r)χ_K(ρ_K)χ_0(𝔛|ζ|), with χ̃₂ a cut-off equal to 0 near (−∞, r_1] and 1 near
[r_2, ∞). Then [[lem:iv5-2-symbols]] gives aH_(−ℓ+j)a + Sa² = a² + b_0² + b_T² − e_R² + f, the symbols formed from the
factors of a as in (1), the term of χ₁(r_4 − r) now being a²(χ₁′/χ₁)(r_4 − r)(ℓ(dr) − H_jr) ≥ 0; the only a priori term
is e_R, on supp χ̃₂′. ∎
```

### T15. prop:iv5-5-2 (2), the adjoint pairing (lines 1713–1713)

Old (1 lines):

```text
the sign the adjoint pairing [Hin26a, (5.49)] needs
```

New (1 lines):

```text
the sign the adjoint pairing [[eq:iv5-2-adj]] needs
```

### T16. prop:iv5-5-3 (2), the adjoint pairing (lines 1750–1750)

Old (1 lines):

```text
the adjoint pairing [Hin26a, (5.49)] the main term must be positive
```

New (1 lines):

```text
the adjoint pairing [[eq:iv5-2-adj]] the main term must be positive
```

### T17. cor:iv5-6-energy (i), up to three boundary pieces (lines 1841–1842)

Old (2 lines):

```text
(i) (*The divergence identity, integrated.*) Let k ∈ {1, 2}, let f_1, …, f_k ∈ C^∞(N) have linearly independent
differentials at each point where they vanish, and let R := {f_1 ≤ 0, …, f_k ≤ 0}, ∂_iR := R ∩ {f_i = 0}, and σ_i the
```

New (3 lines):

```text
(i) (*The divergence identity, integrated.*) Let k ∈ {1, 2, 3}, let f_1, …, f_k ∈ C^∞(N) be such that at each point at
most two of them vanish, and those that vanish there have linearly independent differentials, and let
R := {f_1 ≤ 0, …, f_k ≤ 0}, ∂_iR := R ∩ {f_i = 0}, and σ_i the
```

### T18. new lem:iv5-6-transport and lem:iv5-6-core, inserted after the proof of cor:iv5-6-energy (lines 1902–1903)

Old (2 lines):

```text
each term is at most Cr⁻⁴(|r∇ω|²_B + B(ω, ω)), B being comparable to the Euclidean inner product on K₀. ∎

```

New (99 lines):

```text
each term is at most Cr⁻⁴(|r∇ω|²_B + B(ω, ω)), B being comparable to the Euclidean inner product on K₀. ∎

**Lemma {#lem:iv5-6-transport}** (The damping term as a transport term.) Let N, g, c, e, ℓ, B, ∇, R, f_i, ∂_iR and σ_i
be as in [[cor:iv5-6-energy]], and A := (2ih)⁻¹L_(g,c,e,h) = 2δ_g(c ⊗_s ·) + e dι_(c♯), so that −iL_(g,c,e,h) = 2hA.

(i) Aω = −½ℓ⟨∇ω⟩ + 𝒩ω, with the bundle map 𝒩 of the proof of [[prop:np-10-13]] (ii),
(𝒩ω)_a = −K(ω♯, ∂_a) − (tr K)ω_a + eK(∂_a, ω♯), K(X, Y) = (∇_Xc)(Y).

(ii) For real φ ∈ C^∞(N) and real ω ∈ C¹(N; T*N) with R ∩ supp ω compact, S being the bundle map of [[eq:s14-s]],

    ½∫_R B(ℓ(dφ)ω, ω) |dg| − ½Σ_i ∫_(∂_iR) φB(ℓ(df_i)ω, ω) σ_i = ∫_R φ(2B(Aω, ω) − B(Sω, ω)) |dg|.  {#eq:iv5-6-transport}

(iii) Where the components of g and rc lie in a compact set K₀ as in [[cor:iv5-6-energy]] (ii) and those of g, g⁻¹
and rc have bounded derivatives of order at most 2 along the r∂_(z^μ), we have |𝒩ω|_B + |Sω|_B ≤ C_Nr⁻²|ω|_B, where
the norm is |·|_B := B(·, ·)^(1/2) and C_N depends only on these bounds, K₀ and e.

Replacing c by −c replaces A, ℓ, 𝒩 and S by −A, −ℓ, −𝒩 and −S and leaves B unchanged.

*Proof.* (i) In the proof of [[prop:np-10-13]] (ii), Aω = ∇_μ(M^μω) = M^μ∇_μω + 𝒩ω, with ζ_μM^μ = −½ℓ(ζ) for every
covector ζ; so M^μ = −½ℓ^μ and M^μ∇_μω = −½ℓ⟨∇ω⟩.

(ii) Each M^μ is B-self-adjoint. As in that proof, at every point,
B(Aω, ω) = ∇_μ(B(M^μω, ω)) − (∇_μB)(M^μω, ω) − B(ω, M^μ∇_μω) and B(ω, M^μ∇_μω) = B(ω, Aω) − B(ω, 𝒩ω); so
2B(Aω, ω) = ∇_μ(B(M^μω, ω)) + B(ω, 𝒩ω) − (∇_μB)(M^μω, ω) = ∇_μ(B(M^μω, ω)) + B(Sω, ω), by the formula for S there.
Multiplying by φ and using −(∂_μφ)M^μ = ½ℓ(dφ),

    2φB(Aω, ω) = ∇_μ(φB(M^μω, ω)) + ½B(ℓ(dφ)ω, ω) + φB(Sω, ω).

Integrate over R. By the divergence theorem, as in the proof of [[cor:iv5-6-energy]] (i), the first term gives
Σ_i ∫_(∂_iR) φB((df_i)_μM^μω, ω) σ_i = −½Σ_i ∫_(∂_iR) φB(ℓ(df_i)ω, ω) σ_i, the vector field φB(M^μω, ω)∂_(z^μ) being
C¹ and R ∩ supp ω compact. This is [[eq:iv5-6-transport]].

(iii) With ĉ := rc, K_(μν) = ∂_μc_ν − Γ^λ_(μν)c_λ = r⁻²(r∂_μĉ_ν − (∂_μr)ĉ_ν − rΓ^λ_(μν)ĉ_λ), and
rΓ = ½g⁻¹(r∂g) is bounded; so the components of K are O(r⁻²), and |𝒩ω|_B ≤ Cr⁻²|ω|_B, B being comparable to the
Euclidean inner product on K₀. Each term of [[eq:s14-s]] is a product of one component of K with components of g⁻¹,
of c and of G(c)⁻¹, with twice as many factors c as factors G(c)⁻¹; under c = r⁻¹ĉ, G(c)⁻¹ = r²G(ĉ)⁻¹, with |G(ĉ)|
bounded below on K₀, so each term is O(r⁻²), and |Sω|_B ≤ Cr⁻²|ω|_B. ∎

**Lemma {#lem:iv5-6-core}** (The energy estimate with damping.) Let N, g, c, e ∈ (0, 2/5), ℓ, B, ∇, R, f_i, ∂_iR and
σ_i be as in [[cor:iv5-6-energy]], A as in [[lem:iv5-6-transport]], h ∈ (0, 1], and P := h²□_g + 2hA + hY, where Y is
a linear differential operator of order at most 1 with |Yω|_B ≤ C_Yr⁻²(|ω|_B + h|r∇ω|_B) pointwise. Let ψ ∈ C^∞(N) be
real, w := e^(−ψ), η_0 := dψ = −dw/w and η_1 := η_0 + r⁻¹dr; let κ ∈ (0, 1], λ ≥ 1, and {1, …, k} = I_+ ⊔ I_−. Let
ω ∈ C²(N; T*N) be real, with R ∩ supp ω compact, and suppose that at every point of R ∩ supp ω the components of g
and rc lie in a compact set K₀ as in [[cor:iv5-6-energy]] (ii), the bounds of [[cor:iv5-6-energy]] (iii) hold with a
constant C₁, rη_0 is past timelike with G(rη_0) ≤ −κ|rη_0|², rη_1 is past causal, and |rη_0|, |rη_1| ≥ λ; and that
for i ∈ I_+, at every point of ∂_iR ∩ supp ω, df_i is past timelike with G(r df_i) ≤ −κ|r df_i|². Put

    E_0 := ∫_R w²r⁻⁴|ω|²_B |dg|,     E_1 := ∫_R w²r⁻⁴|r∇ω|²_B |dg|,     F := ∫_R w²|Pω|²_B |dg|,
    β⁰_i := ∫_(∂_iR) w²r⁻⁴|r df_i||ω|²_B σ_i,     β¹_i := ∫_(∂_iR) w²r⁻⁴|r df_i||r∇ω|²_B σ_i.

There are λ_* and C_*, depending only on K₀, κ, e, C₁ and C_Y, such that if λ ≥ λ_*, then

    E_0 + h²E_1 + Σ_(i∈I_+)(β⁰_i + h²β¹_i) ≤ C_*(h⁻²F + Σ_(i∈I_−)(β⁰_i + β¹_i)).                         {#eq:iv5-6-core}

*Proof.* Write |·| for |·|_B, and ∫ for integrals over R against |dg| and over ∂_iR against σ_i. *Constants.* Let c₀
be the constant of [[cor:iv5-6-energy]] (ii) for K₀ and κ, C_R that of [[cor:iv5-6-energy]] (iii) for C₁, K₀ and e,
and C_N that of [[lem:iv5-6-transport]] (iii). By [[lem:iv4-1-causal]] (d) with K := K₀ there is c₁ > 0 with
B(ℓ_(g,ĉ,e)(ζ)v, v) ≥ c₁|ζ||v|² for (g, ĉ) ∈ K₀ and future causal ζ, and by continuity on compact sets there are C_ℓ
and C_Q with |B(ℓ_(g,ĉ,e)(ζ)v, v)| ≤ C_ℓ|ζ||v|² and |𝒬_(G,ζ,ℓ_(g,ĉ,e))(ξ)| ≤ C_Q|ζ|Σ_μ|ξ_μ|² for (g, ĉ) ∈ K₀ and all
ζ, v and ξ. As ℓ_(g,c,e)(ζ) is bilinear in (c, ζ) and B does not change under c ↦ rc, at the points of R ∩ supp ω
B(ℓ(ζ)v, v) ≥ c₁r⁻²|rζ||v|² for future causal ζ, |B(ℓ(ζ)v, v)| ≤ C_ℓr⁻²|rζ||v|², and, by the identity in the proof of
[[cor:iv5-6-energy]] (ii), |𝒬_(G,ζ,ℓ)(ξ)| ≤ C_Qr⁻⁴|rζ|Σ_μ|rξ_μ|². Put C₂ := 2C_Y² + 4C_N² + C_R and

    λ_* := max(1, 2(2C_Y² + C_R)/c₀, 8C_N/c₁, 4C₂^(1/2)/c₁),     C_* := (32c₁⁻² + 4c₀⁻¹)(1 + C₂C_ℓ/c₁ + C_Q) + 2C_ℓ/c₁.

*The energy identity.* Apply [[eq:iv5-6-energy]], with −d(w²) = 2w²η_0. By the hypotheses and [[cor:iv5-6-energy]] (ii),
its bulk term is at least c₀∫w²r⁻⁴|rη_0||r∇ω|² ≥ c₀λE_1, its boundary terms for i ∈ I_+ are at least ½c₀β¹_i, and
those for i ∈ I_− are at least −½C_Qβ¹_i. By [[lem:iv5-6-transport]] (i), h²□_gω = Pω − hYω + hℓ⟨∇ω⟩ − 2h𝒩ω. With
Λ := ∫w²|ℓ⟨∇ω⟩|², the Cauchy–Schwarz inequality, ∫w²|Yω|² ≤ 2C_Y²(E_0 + h²E_1), the bound |𝒩ω| ≤ C_Nr⁻²|ω| and
the bound |𝓡(ω)| ≤ C_Rr⁻⁴(|r∇ω|² + |ω|²) of [[cor:iv5-6-energy]] (iii), the right side of [[eq:iv5-6-energy]] is
at most

    −h⁻¹Λ + h⁻²F^(1/2)Λ^(1/2) + h⁻¹(2C_Y²(E_0 + h²E_1))^(1/2)Λ^(1/2) + 2h⁻¹C_NE_0^(1/2)Λ^(1/2) + C_R(E_0 + E_1)
        ≤ −¼h⁻¹Λ + h⁻³F + 2C_Y²h⁻¹(E_0 + h²E_1) + 4C_N²h⁻¹E_0 + C_R(E_0 + E_1),

each of the three products being at most ¼h⁻¹Λ plus the corresponding square. As h ≤ 1,

    (c₀λ − 2C_Y² − C_R)E_1 + ½c₀Σ_(I_+)β¹_i + ¼h⁻¹Λ ≤ h⁻³F + C₂h⁻¹E_0 + ½C_QΣ_(I_−)β¹_i.               {#eq:iv5-6-core-1}

*The transport identity.* Apply [[eq:iv5-6-transport]] with φ := r⁻²w². Then dφ = −2φη_1, and −rη_1 is future causal,
so ½B(ℓ(dφ)ω, ω) = φB(ℓ(−η_1)ω, ω) ≥ c₁λw²r⁻⁴|ω|²; for i ∈ I_+, −df_i is future timelike, so
−½φB(ℓ(df_i)ω, ω) ≥ ½c₁w²r⁻⁴|r df_i||ω|²; for i ∈ I_−, −½φB(ℓ(df_i)ω, ω) ≥ −½C_ℓw²r⁻⁴|r df_i||ω|². By (i) and (iii)
of [[lem:iv5-6-transport]], |2B(Aω, ω) − B(Sω, ω)| ≤ |ℓ⟨∇ω⟩||ω| + 2C_Nr⁻²|ω|². So

    c₁λE_0 + ½c₁Σ_(I_+)β⁰_i − ½C_ℓΣ_(I_−)β⁰_i ≤ Λ^(1/2)E_0^(1/2) + 2C_NE_0 ≤ (c₁λ)⁻¹Λ + ¼c₁λE_0 + 2C_NE_0,

and as 2C_N ≤ ¼c₁λ,

    ½c₁λE_0 + ½c₁Σ_(I_+)β⁰_i ≤ (c₁λ)⁻¹Λ + ½C_ℓΣ_(I_−)β⁰_i.                                             {#eq:iv5-6-core-2}

*Conclusion.* By [[eq:iv5-6-core-2]] and λ ≥ 1, E_0 ≤ 2(c₁λ)⁻²Λ + (C_ℓ/c₁)Σ_(I_−)β⁰_i. Insert this into
[[eq:iv5-6-core-1]]: as λ ≥ λ_*, c₀λ − 2C_Y² − C_R ≥ ½c₀λ and 2C₂(c₁λ)⁻² ≤ ⅛, so

    ½c₀λE_1 + ½c₀Σ_(I_+)β¹_i + ⅛h⁻¹Λ ≤ h⁻¹Θ,     Θ := h⁻²F + (C₂C_ℓ/c₁)Σ_(I_−)β⁰_i + ½C_QΣ_(I_−)β¹_i.

Hence Λ ≤ 8Θ, h²(E_1 + Σ_(I_+)β¹_i) ≤ 4c₀⁻¹hΘ ≤ 4c₀⁻¹Θ, and, by [[eq:iv5-6-core-2]] once more,
E_0 + Σ_(I_+)β⁰_i ≤ 4c₁⁻²Λ + (2C_ℓ/c₁)Σ_(I_−)β⁰_i ≤ 32c₁⁻²Θ + (2C_ℓ/c₁)Σ_(I_−)β⁰_i. Adding, and using
Θ ≤ h⁻²F + (C₂C_ℓ/c₁ + C_Q)Σ_(I_−)(β⁰_i + β¹_i), gives [[eq:iv5-6-core]] with the C_* above. ∎

```

### T19. prop:iv5-6-1 (1), the support condition at Σ^♯ of the second estimate (lines 1911–1911)

Old (1 lines):

```text
and for every ω ∈ ρ_sf^(−α_sf−2)H²_(3b,h), without support condition,
```

New (2 lines):

```text
and for every ω ∈ ρ_sf^(−α_sf−2)H²_(3b,h) supported at Σ^♯ (as are the elements of the spaces (·)^(−,•) of
[[def:iv5-0-1]]), without support condition at X_0,
```

### T20. prop:iv5-6-1, the proof (lines 1935–1978)

Old (44 lines):

```text
*Proof.* [Hin26a, (5.66)]. Take the multiplier a²L_h with a = ρ_sf^(−α_sf−2)e^(−𝔛τ)H(T_0 − τ)H(r − r_♯) (H the
Heaviside function), and the pairing [Hin26a, (5.70)],
h⁻¹Im⟨P_hω, a²L_hω⟩ = ⟨𝒞ω, ω⟩ − h⁻¹‖aL_hω‖². The principal symbol of 𝒞 is aT_(G,da,ℓ) − a²E, with T of
[[eq:iv5-6-t]], since H_Ga = 2g⁻¹(ζ, da). This leads to the decomposition [Hin26a, (5.71)], whose derivation only
expands (i/2)(□_h*bL_h − L_h*b□_h) in local coordinates with b = a². Its part from □_h and from the principal part
−ihℓ⟨∇·⟩ of L_h is h²∫_R B(□_gω, w²ℓ⟨∇ω⟩)|dg| for real ω, and the sum of this for Re ω and Im ω in general, with the
R and w below; [[eq:iv5-6-energy]] writes it through the 𝒬-terms and 𝓡 (for ω vanishing for t < 0 by density, each
term being continuous in the norm of ρ_sf^(α_sf)H²_(3b,h)). Then a da is [Hin26a, (5.72)], and the weight identity
[Hin26a, (5.73)] holds: aT_(G,−da,ℓ) = ρ_sf⁴T_(ρ_sf⁻²G, −a da, ρ_sf⁻²ℓ), as T is linear in each of its three arguments,
free of the dimension.

−a da is past timelike for 𝔛 large, since dτ is past timelike with r²g⁻¹(dτ, dτ) ≤ −¾ ([[lem:iv5-0-3]] (b)) and the
δ(r − r_♯)-part of −a da is a positive multiple of −dr, past timelike ([[lem:iv5-0-3]] (c)). So [[cor:iv5-6-energy]]
applies, on N := ℝ_t × {r > ½r_♯} and R := {r ≥ r_♯, τ ≤ T_0}, with f_1 := τ − T_0, f_2 := r_♯ − r and
w := ρ_sf^(−α_sf−2)e^(−𝔛τ), so that a = wH(T_0 − τ)H(r − r_♯). Its bulk term carries
−d(w²) = 2w²(𝔛dτ + (α_sf + 2)dρ_sf/ρ_sf), and its two boundary terms carry dτ on {τ = T_0} and −dr on Σ^♯; these are
the three parts of −a da = −½d(a²) = a²(𝔛dτ + (α_sf + 2)dρ_sf/ρ_sf) + ½w²δ(T_0 − τ)dτ − ½w²δ(r − r_♯)dr.
The hypotheses of [[cor:iv5-6-energy]] (ii) hold uniformly for b ∈ U. The components of g and rc, continuous on the
compact Ω and in b ([[lem:iv5-0-2]] (a), (d)), lie in a compact set of pairs, rc being past timelike
([[lem:iv5-0-5]] (1)); e = 1/102400 < 2/5; and r(𝔛dτ + (α_sf + 2)dρ_sf/ρ_sf) = 𝔛(dt − τ dr) − (α_sf + 2)dr,
r dτ = dt − T_0 dr on {τ = T_0} and −r dr on Σ^♯ satisfy its condition with one κ > 0 for 𝔛 large, by
[[lem:iv5-0-3]] (b), (c). So each of the three terms is at least c₀ times the corresponding weighted integral of the
square of |r∇ω|_B, the bulk term with the factor 𝔛. Here the level sets of τ carry r⁴|dr d𝑔̸|, which tensored with |dτ|
is |dg| ([[lem:iv5-0-2]] (b)). This gives [Hin26a, (5.74)].

The other terms of [Hin26a, (5.71)] carry the total weight ρ_sf⁴ of ∇*T∇ and are bounded by [Hin26a, (5.75)] and its
companions. Among them is h² times the term with 𝓡 in [[eq:iv5-6-energy]], bounded by [[cor:iv5-6-energy]] (iii), as
the components of g, g⁻¹ and rc lie in C^∞(M^♭) and r∂_(z^μ) ∈ 𝒱_3b(M^♭), with r⁻¹ = ρ_sf. The left side of
[Hin26a, (5.70)] is at least −½h⁻¹(‖aP_hω‖² + ‖aL_hω‖²), which gives [Hin26a, (5.76)]. The fundamental theorem of
calculus for L_h, [Hin26a, (5.77)], uses [[lem:iv5-0-4]] ([[lem:iv4-1-causal]] (a)) for the future timelike covector
ρ_sf a d(ρ_sf a). It gives the bulk term C𝔛ρ_sf⁴a² and the two positive δ-terms, hence [Hin26a, (5.78)]. Adding
[Hin26a, (5.76)] and (5.78) and absorbing for h small gives [Hin26a, (5.66)].

[Hin26a, (5.68)] follows by the same argument with a = ρ_K^(−α_K)e^(𝔛r)H(r − r_1), applied to χω (χ = 1 on r ≤ r_2,
0 on r ≥ r_3), as −dr is past timelike on [r_♯, r̂] ([[lem:iv5-0-3]] (c)); in [[cor:iv5-6-energy]], R = {r ≥ r_1},
f_1 = r_1 − r and w = ρ_K^(−α_K)e^(𝔛r). [Hin26a, (5.67) and (5.69)] are the same arguments for P_h* = □_h* + iL_h*,
whose damping acts backwards, as in [Hin26a]; its damping symbol is −ℓ, for which [[cor:iv5-6-energy]] holds with the
time orientation reversed.

[[eq:iv5-6-1]]. Run the proof of [Hin26a, (5.66)] at fixed h with a multiplied by H(τ). The boundary τ = 0 then adds to
[Hin26a, (5.74) and (5.77)] the terms of the boundary τ = T_0 with the opposite sign. Each is a quadratic form in
(ω, ∂_τω)|_(τ=0) with bounded coefficients in the 3b frame, so it is bounded by
C‖(ω, r𝓛_(∂_t)ω)|_(X_0)‖²_(ℋ_data). Here ∂_τ = r∂_t at fixed (r, ω), and the weight matches by [[lem:iv5-0-2]] (b):
ρ_sf^(α+½)H̄^k_b(X_0, r³|dr d𝑔̸|) = ρ_sf^α H̄^k_b(X_0, r⁴|dr d𝑔̸|). ∎
```

New (89 lines):

```text
*Proof.* *The operators.* As g is Ricci-flat, P_h = h²□_g − iL_h = h²□_g + 2hA ([[lem:s14-box-c]]), with A of
[[lem:iv5-6-transport]], a real operator; so it suffices to prove the estimates for real ω, those for complex ω
following by adding the estimates for Re ω and Im ω. For the adjoint, A* = S − A ([[prop:np-10-13]] (ii)), and
B(ω, ω′) = ⟨ω, Θω′⟩ with Θω := ω − (1 + e)G(c)⁻¹⟨c, ω⟩c, which is invertible, B being positive definite; as □_g is
symmetric for ⟨·, ·⟩ and |dg|, □_g* = Θ⁻¹□_gΘ = □_g + Z with Z := −Θ⁻¹(2(∇^μΘ)∇_μ + (∇^μ∇_μΘ)). So

    P_h* = h²□_g + 2h(−A) + hY,     Y := 2S + hZ,

and −A is the operator A of the 1-form −c, which is past timelike for the opposite time orientation
([[lem:iv5-6-transport]]). Θ depends only on g and rc, so ∇Θ = O(r⁻¹) and ∇∇Θ = O(r⁻²) under the bounds below, and
with [[lem:iv5-6-transport]] (iii), |Yω|_B ≤ C_Yr⁻²(|ω|_B + h|r∇ω|_B).

*The hypotheses of [[lem:iv5-6-core]].* Let N := ℝ_t × {r > ½r_♯}. On {r ≥ ½r_♯} ∩ τ⁻¹([0, T_0]) and on
{½r_♯ ≤ r ≤ r̂} ∩ {t ≥ 0}, whose closures in the compactification of [[def:iv5-0-1]] are compact, the components of g,
g⁻¹ and rc are smooth up to the faces at infinity and continuous in b, by the proofs of [[lem:iv5-0-2]] (a), (d), which
hold on {r ≥ ½r_♯}; r∂_(z^μ) ∈ 𝒱_3b; and rc is past timelike there ([[sec:iv5-0]]). So the components of g and rc lie
in a compact set K₀ of pairs, and the bounds of [[cor:iv5-6-energy]] (iii) hold with one C₁, for b ∈ U, for the
pair (g, c) and, with the opposite orientation, for (g, −c); so does the bound on Y with one C_Y. Let Γ bound the
Euclidean operator norm of g⁻¹ over K₀. We use: (∗) if u is past timelike with G(u) ≤ −γ|u|², γ ∈ (0, 1], |·| the
Euclidean norm of the components, |v| ≤ m and 𝔛|u| ≥ 6m max(1, Γ/γ), then 𝔛u + v is past timelike, with
G(𝔛u + v) ≤ −(γ/4)|𝔛u + v|² and |𝔛u + v| ≥ ¾𝔛|u|. Indeed, with q := 𝔛|u| ≥ 6m, so that Γm ≤ γq/6,
G(𝔛u + v) ≤ −γq² + 2Γmq + Γm² ≤ −γq² + (9/4)Γmq ≤ −(5/8)γq² ≤ −(γ/4)(5q/4)², while
q − m ≤ |𝔛u + v| ≤ q + m ≤ 5q/4; the same holds with sv, s ∈ [0, 1], in place of v, so 𝔛u + v lies in the cone of u.
Let λ_* be the number of [[lem:iv5-6-core]] for K₀, κ := ⅛, e, C₁ and C_Y. All constants below are uniform for b ∈ U.

*The first estimate of (1)* ([Hin26a, (5.66)]). There ρ_sf = r⁻¹. Take R := {τ ≤ T_0, r ≥ r_♯} ⊂ N, f_1 := τ − T_0,
f_2 := r_♯ − r, I_+ := {1, 2}, Y := 0 and w := ρ_sf^(−α_sf−2)e^(−𝔛τ). With u := r dτ = dt − τ dr,
rη_0 = 𝔛u − (α_sf + 2)dr and rη_1 = 𝔛u − (α_sf + 1)dr. On τ⁻¹([0, T_0]), G(u) ≤ −¾ ≤ −(3/5)|u|²
([[lem:iv5-0-3]] (b); |u|² = 1 + τ² ≤ 5/4) and |u| ≥ 1, so by (∗) with γ := 3/5 and m := |α_sf| + 2, both are past
timelike with G ≤ −(3/20)|·|² and of length at least ¾𝔛, for 𝔛 ≥ 6m max(1, 5Γ/3). On {τ = T_0}, r df_1 = u; on
Σ^♯, r df_2 = −r dr is past timelike with G(−r dr) ≤ −½|r dr|² ([[lem:iv5-0-3]] (c)). Fix 𝔛 ≥ max(6m max(1, 5Γ/3),
(4/3)λ_*). Then [[eq:iv5-6-core]] holds for every real ω, smooth on N, vanishing for t < 0, with R ∩ supp ω compact.
On R ∩ supp ω ⊂ τ⁻¹([0, T_0]), w²r⁻⁴ = ρ_sf^(−2α_sf)e^(−2𝔛τ) ≥ e^(−𝔛)ρ_sf^(−2α_sf) and w² ≤ ρ_sf^(−2α_sf−4); and
r∇_μω = r∂_(z^μ)ω − rΓ_μω with rΓ_μ bounded ([[lem:iv5-0-2]] (c)), the r∂_(z^μ) spanning 𝒱_3b, and B is comparable to
the Euclidean inner product. So E_0 + h²E_1 ≥ c‖ω‖²_(ρ_sf^(α_sf)H¹_(3b,h)(τ⁻¹([0,T_0]))) for some c > 0 and
F ≤ ‖P_hω‖²_(ρ_sf^(α_sf+2)L²(τ⁻¹([0,T_0]))), and the estimate holds with C := (C_*/c)^(1/2), for every h ∈ (0, 1]. It
extends to every ω ∈ ρ_sf^(α_sf)H²_(3b,h) vanishing for t < 0: such ω are limits in that space of smooth sections
vanishing for t < 0 with compact support (extend across Σ^♯, translate in t, mollify and cut off at large r), and both
sides are continuous in its norm.

*The first estimate of (2)* ([Hin26a, (5.68)]). Let χ = χ(r) be smooth, equal to 1 for r ≤ r_2 and to 0 for r ≥ r_3,
and ω′ := χω, with ω smooth, vanishing for t < 0 and with compact support. On {t > −r} put ρ_K := r/(t + r), extended
smoothly and positively to N; on r⁻¹([r_♯, r̂]) ∩ {t ≥ 0} it is ρ_K′/(1 + ρ_K′), ρ_K′ the ρ_K of [[def:iv5-0-1]]
near K⁺, so the weights are equivalent. Take R := {r ≥ r_1}, f_1 := r_1 − r, I_+ := {1}, Y := 0 and
w := ρ_K^(−α_K)e^(𝔛r). With u := −r dr, rη_0 = 𝔛u + α_K(dr − r(dt + dr)/(t + r)) and rη_1 = rη_0 + dr, the added
covectors having Euclidean norm at most 3|α_K| + 1 on {t ≥ 0}. On r⁻¹([r_1, r_3]) ⊂ r⁻¹([r_♯, r̂]), u is past timelike
with G(u) ≤ −½|u|² and |u| ≥ r_♯ ([[lem:iv5-0-3]] (c)), and so is r df_1 = u. By (∗) with γ := ½ and m := 3|α_K| + 1,
[[lem:iv5-6-core]] applies to ω′, whose support meets R in r⁻¹([r_1, r_3]) ∩ {t ≥ 0}, with κ = ⅛ and λ := ¾𝔛r_♯, for
𝔛 ≥ r_♯⁻¹ max(6(3|α_K| + 1) max(1, 2Γ), (4/3)λ_*). There w²r⁻⁴ and w² lie between positive multiples of ρ_K^(−2α_K), so
‖ω′‖_(ρ_K^(α_K)H¹_(3b,h)(r⁻¹([r_1,r_3]))) ≤ Ch⁻¹‖P_hω′‖_(ρ_K^(α_K)L²(r⁻¹([r_1,r_3]))). Now
P_hω′ = χP_hω + [P_h, χ]ω, where [P_h, χ]ω = −h²(2∇^μχ∇_μω + (∇^μ∇_μχ)ω) − hℓ(dχ)ω by [[lem:iv5-6-transport]] (i),
supported in r⁻¹([r_2, r_3]) with bounded coefficients; so h⁻¹‖[P_h, χ]ω‖ ≤ C‖ω‖_(ρ_K^(α_K)H¹_(3b,h)(r⁻¹([r_2,r_3]))).
As ω′ = ω on r⁻¹([r_1, r_2]), this gives the estimate, which extends by density as before.

*The second estimate of (1)* ([Hin26a, (5.67)]). Let ω be smooth with compact support in {r > r_♯}; such sections are
dense among those supported at Σ^♯, both sides being continuous in the norm of ρ_sf^(−α_sf−2)H²_(3b,h). Let χ = χ(τ)
be smooth, equal to 1 for τ ≤ ½T_0 and to 0 for τ ≥ ¾T_0, and ω′ := χω. Apply [[lem:iv5-6-core]] to P_h*, with the
1-form −c and the opposite time orientation, R := {τ ≥ 0} ∩ N, f_1 := −τ, I_+ := {1} and w := ρ_sf^(α_sf)e^(𝔛τ). Now
rη_0 = −𝔛u + α_sf dr and rη_1 = −𝔛u + (α_sf + 1)dr, with −u past timelike for the opposite orientation, and
r df_1 = −u; by (∗) as before, the hypotheses hold on R ∩ supp ω′ ⊂ τ⁻¹([0, ¾T_0]) ∩ {r > r_♯} for
𝔛 ≥ max(6(|α_sf| + 1) max(1, 5Γ/3), (4/3)λ_*), with λ := ¾𝔛. There
w²r⁻⁴ ≥ ρ_sf^(2α_sf+4) and w² ≤ e^(2𝔛T_0)ρ_sf^(2α_sf), so
‖ω′‖_(ρ_sf^(−α_sf−2)H¹_(3b,h)(τ⁻¹([0,T_0]))) ≤ Ch⁻¹‖P_h*ω′‖_(ρ_sf^(−α_sf)L²(τ⁻¹([0,T_0]))). Here
P_h*ω′ = χP_h*ω + [P_h*, χ]ω, where
[P_h*, χ]ω = −h²(2∇^μχ∇_μω + (∇^μ∇_μχ)ω) + hℓ(dχ)ω − 2h²Θ⁻¹(∇^μΘ)(∂_μχ)ω is supported in τ⁻¹([½T_0, ¾T_0]),
and |[P_h*, χ]ω|_B ≤ Chr⁻²(|ω|_B + h|r∇ω|_B), as dχ = χ′(τ)r⁻¹u; so
h⁻¹‖[P_h*, χ]ω‖_(ρ_sf^(−α_sf)L²) ≤ C‖ω‖_(ρ_sf^(−α_sf−2)H¹_(3b,h)(τ⁻¹([T_0/2,T_0]))). As ω′ = ω on τ⁻¹([0, ½T_0]),
this gives the estimate.

*The second estimate of (2)* ([Hin26a, (5.69)]). Let ω be smooth, with compact support in {r > r_1}, dense as before.
Apply [[lem:iv5-6-core]] to P_h*, with −c and the opposite orientation, R := {τ ≥ 0, r ≤ r_3} ∩ N, f_1 := −τ,
f_2 := r − r_3, I_+ := {1, 2} and w := ρ_K^(α_K)e^(−𝔛r), ρ_K as above. Now rη_0 = −𝔛u − α_K(dr − r(dt + dr)/(t + r))
and rη_1 = rη_0 + dr, with u = −r dr as above, and r df_2 = −u, r df_1 = −r dτ; −u = r dr is past timelike for the
opposite orientation on [r_♯, r̂], with G(−u) ≤ −½|u|², and on {τ = 0}, −r dτ = −dt is past timelike for it, with
G(dt) ≤ −1 = −|dt|² ([[lem:iv5-0-3]] (a)). By (∗) the hypotheses hold, with λ := ¾𝔛r_♯,
for 𝔛 ≥ r_♯⁻¹ max(6(3|α_K| + 1) max(1, 2Γ), (4/3)λ_*), and as there w²r⁻⁴ and w² lie between positive multiples of
ρ_K^(2α_K), [[eq:iv5-6-core]] gives the estimate.

[[eq:iv5-6-1]]. Fix h, and let ω be smooth on N with compact support. Apply [[lem:iv5-6-core]] as for the first
estimate of (1), on R := {0 ≤ τ ≤ T_0, r ≥ r_♯} with the third function f_3 := −τ and I_− := {3}; at most two of
f_1, f_2, f_3 vanish at any point. On X_0 = {τ = 0}, |dg| = |dτ| ⊗ r⁴|dr d𝑔̸| ([[lem:iv5-0-2]] (b)), |r dτ| = 1 and
w²r⁻⁴ = ρ_sf^(−2α_sf); r∇_tω = r𝓛_(∂_t)ω − rΓ_tω, the coordinates being stationary, and
r∇_(x^i)ω = r∂_(x^i)ω − rΓ_iω, the r∂_(x^i) being b-vector fields on X̄; so
β⁰_3 + β¹_3 ≤ C‖(ω, r𝓛_(∂_t)ω)|_(X_0)‖²_(ℋ_data), and [[eq:iv5-6-core]] gives [[eq:iv5-6-1]], which extends to
ω ∈ ρ_sf^(α_sf)H̄²_3b by density, the traces on X_0 depending continuously on ω. Applied with T ∈ (0, T_0] in place of
T_0 in R, the same bounds the term β⁰_1 + h²β¹_1 on {τ = T}, which is comparable to
‖(ω, r∇ω)|_(τ=T)‖² in ρ_sf^(α_sf)L²(r⁴|dr d𝑔̸|), by the right side of [[eq:iv5-6-1]], uniformly in T. Here
∂_τ = r∂_t at fixed (r, ω), and the weight matches by [[lem:iv5-0-2]] (b):
ρ_sf^(α+½)H̄^k_b(X_0, r³|dr d𝑔̸|) = ρ_sf^α H̄^k_b(X_0, r⁴|dr d𝑔̸|). ∎
```

### T45. prop:iv5-7-1, what the estimates near Σ^♯ need on the extended domain (lines 2036–2037)

Old (2 lines):

```text
[[prop:iv5-6-1]] are used, with ¾r_♯ for r_♯; they need only [[lem:iv5-0-3]] (c) and [[lem:iv5-0-4]], which hold on
{r ≥ ½r_♯}, where g is defined and c is past timelike ([[sec:iv5-0]]).
```

New (3 lines):

```text
[[prop:iv5-6-1]] are used, with ¾r_♯ for r_♯; their proof needs only [[lem:iv5-0-3]] (a), (c), [[lem:iv5-0-4]] and the
bounds of its hypothesis paragraph, which hold on {r ≥ ½r_♯}, where g is defined and c is past timelike
([[sec:iv5-0]]).
```

### T22. thm:iv5-7-3 (b), the Cauchy problem for smooth data (lines 2119–2124)

Old (6 lines):

```text
dτ to |dg|; the shift ½ does not depend on the dimension ([Hin26a, p. 65]). *Smooth data.* Take f and data smooth with
compact support in Ω° ∪ X_0°. The initial value problem then has a solution ω smooth on Ω ∖ (K⁺ ∪ 𝗌𝖿), for the
following reasons. □^C_b has scalar principal symbol G Id ([[lem:iv5-0-2]] (d)). Every past-inextendible causal curve in
Ω° meets X_0: t decreases along it ([[lem:iv5-0-3]] (a)), r increases along it inside {r ≤ r̂} ([[lem:iv5-0-3]] (c)),
and |dr/dt| is bounded along causal curves, since g is a 3sc-metric. So the classical theory of the Cauchy problem for
linear wave equations with scalar principal symbol applies ([Hin26a, p. 42]). By finite speed of propagation, ω
```

New (13 lines):

```text
dτ to |dg|; the shift ½ does not depend on the dimension ([Hin26a, p. 65]). *Smooth data.* Take f smooth with compact
support in Ω°, and data smooth on X_0 with compact support in X_0 ∖ 𝗌𝖿. The initial value problem then has a solution
ω smooth on Ω ∖ (K⁺ ∪ 𝗌𝖿), for the following reasons. □^C_b is normally hyperbolic ([[def:std-normally-hyperbolic]]):
its second-order part is that of □_g = −∇^a∇_a ([[lem:s14-box-c]]). Let N := ℝ_t × {r > ½r_♯} and
S := N ∩ {t = 0}, which is acausal, as t increases strictly along future causal curves ([[lem:iv5-0-3]] (a)). Every
inextendible causal curve through a point of Ω ∖ (K⁺ ∪ 𝗌𝖿) meets S: t decreases along it towards the past, r increases
along it inside {r ≤ r̂} ([[lem:iv5-0-3]] (c)), so it stays in N, and |dr/dt| is bounded along causal curves, since g
is a 3sc-metric. So Ω ∖ (K⁺ ∪ 𝗌𝖿) lies in the Cauchy development D of S, which is globally hyperbolic with Cauchy
hypersurface S ([[thm:std-bgp-development]]), and [[thm:std-bgp-cauchy]] (5) on D gives a smooth solution, for the
data extended smoothly to S with compact support (on S, (ω, r𝓛_(∂_t)ω) and (ω, ∇_nω) determine each other); by its
support statement the solution on Ω does not depend on the
extension, future causal curves from S ∩ {r < r_♯} staying in {r < r_♯} ([[lem:iv5-0-3]] (c)). By finite speed of
propagation, ω
```

### T21. thm:iv5-7-3 (b), the continuity in τ (lines 2135–2137)

Old (3 lines):

```text
C([0, T_0]_τ; ρ_sf^(α_sf)H̄¹_b) ∩ C¹([0, T_0]_τ; ρ_sf^(α_sf)H̄⁰_b): the boundary term at τ = T of [Hin26a, (5.74) and
(5.77)], run at every T ∈ [0, T_0] in the proof of [[eq:iv5-6-1]], bounds the norm of (ω, ∂_τω)|_(τ=T) by the right
side of [[eq:iv5-6-1]]. So the limit takes the data and solves [[eq:iv5-5-16]]. For uniqueness, let
```

New (4 lines):

```text
C([0, T_0]_τ; ρ_sf^(α_sf)H̄¹_b) ∩ C¹([0, T_0]_τ; ρ_sf^(α_sf)H̄⁰_b): the term of [[eq:iv5-6-core]] on {τ = T}, for the
region {0 ≤ τ ≤ T, r ≥ r_♯} of the proof of [[eq:iv5-6-1]] at every T ∈ (0, T_0], bounds the norm of
(ω, ∂_τω)|_(τ=T) by the right side of [[eq:iv5-6-1]]. So the limit takes the data and solves [[eq:iv5-5-16]]. For
uniqueness, let
```

### T23. def:iv6-0-2, admissibility at complex σ (lines 2316–2318)

Old (3 lines):

```text
**Definition {#def:iv6-0-2}** (Admissible orders; [Hin26a, (B.13)] in dimension 4 + 1.) (s, ℓ, β) is *admissible at σ*
if β ∈ (0, 2 + C_0], ℓ < −½ + h⁻¹(1 − e)(1 − v) at R_out, and, when σ = ±1, ℓ > −½ − h⁻¹(1 − e)(1 + v) at R_in, with ℓ
constant near R_in and R_out and non-increasing along σH_(G_σ).
```

New (9 lines):

```text
**Definition {#def:iv6-0-2}** (Admissible orders; [Hin26a, (B.13)] in dimension 4 + 1.) For real σ₀ ≠ 0 let
R_(σ₀,in) := {ρ = 0, ξ = 2σ₀, η = 0} and Char_(σ₀) := {ρ = 0, G_(σ₀) = 0}, with the real symbol G_(σ₀) of
[[lem:iv6-0-1]] (c); for σ₀ = ±1 these are the R_in of [[sec:iv6-0]] and the Char_σ of [[lem:iv6-0-flow]] (b). For
σ ∈ ℂ ∖ 0 with Im σ ≥ 0, (s, ℓ, β) is *admissible at σ* if β ∈ (0, 2 + C_0], ℓ is constant near R_out with
ℓ < −½ + h⁻¹(1 − e)(1 − v) there, and, when σ is real, ℓ is also constant near R_(σ,in) with
ℓ > −½ − h⁻¹(1 − e)(1 + v) there and σ𝖧_(G_σ)ℓ ≤ 0 on Char_σ, 𝖧 as in [[eq:iv6-0-flow]]. For Im σ > 0 nothing is
asked off R_out, which is then the whole characteristic set over ρ = 0 ([[lem:iv6-0-flow]] (a)). Fixed orders are
*admissible on* a set of such σ if they are admissible at every σ of the set and at Re σ for every σ of the set with
Re σ ≠ 0: as in [[sec:i-a-1-4]], the orders used at a complex σ are those for Re σ.
```

### T24. prop:iv6-1-1, the dual estimate and the uniformity clause (lines 2333–2334)

Old (2 lines):

```text
(for admissible s_0 < s, ℓ_0 < ℓ, β_0 < β, in the strong sense) and its dual ([Hin26a, (B.28)]) hold uniformly for σ in
e^(i[0,π−δ]) near 1 and in e^(i[δ,π]) near −1, for fixed orders admissible there.
```

New (8 lines):

```text
(for admissible s_0 < s, ℓ_0 < ℓ, β_0 < β, in the strong sense) and its dual

    ‖ω‖_(H^(−s+2,(−ℓ−1,−β+2))_(sc,b)) ≤ C(‖((□^C)^(σ))*ω‖_(H^(−s,(−ℓ,−β))_(sc,b)) + ‖ω‖_(H^(s_1,(ℓ_1,β_1))_(sc,b)))
                                                                                                          {#eq:iv6-1-3}

(for s_1 < −s + 2, β_1 < −β + 2 and ℓ_1 < −ℓ − 1 with ℓ_1 > −½ − h⁻¹(1 − e)(1 − v) near R_out, in the strong sense,
the adjoint being taken for the L² pairing of these spaces; [Hin26a, (B.28)]) hold uniformly for σ in e^(i[0,π−δ]) near
1 and in e^(i[δ,π]) near −1, for fixed orders admissible on that set ([[def:iv6-0-2]]).
```

### T25. prop:iv6-1-1, the shift at the sink (lines 2339–2342)

Old (4 lines):

```text
- *Sink R_out.* With the commutant [Hin26a, (B.21)], a = ρ^(−ℓ−½)χ_0(ρ)χ₁(|η|²)χ₂(ξ), the principal symbol of
(i/2)[(□^C)^(σ), A²] is aH_(G_σ)a = ρa𝖧_(p_σ)a, given by [[lem:iv6-0-flow]] (c) ([Hin26a, (B.23)]). That of
(2i)⁻¹((□^C)^(σ) − (□^C)^(σ)*)A² adds at the zero section the shift [Hin26a, (B.24)]. By [[lem:iv6-0-1]] the shift
comes only from −2iσρh⁻¹S̄: (□^C)^(0) − (□^C)^(0)* ∈ ρ²Diff¹_b, whose quotient by ρ has scattering symbol vanishing at
```

New (6 lines):

```text
- *Sink R_out.* With the commutant a = ρ^(−ℓ−½)χ_0(ρ)χ₁(|η|²)χ₂(ξ) ([Hin26a, (B.21)]), the principal symbol of
(i/2)[(□^C)^(σ), A²] is aH_(G_σ)a = ρa𝖧_(p_σ)a, given by [[lem:iv6-0-flow]] (c) ([Hin26a, (B.23)]). That of
(2i)⁻¹((□^C)^(σ) − (□^C)^(σ)*)A² is a²ρ times the principal symbol of (2iρ)⁻¹((□^C)^(σ) − (□^C)^(σ)*), whose value at
the zero section, the shift, adds to the coefficient (2ℓ + 1)σ of the main term. By [[lem:iv6-0-1]] the shift
comes only from −2iσρh⁻¹S̄: (□^C)^(0) − (□^C)^(0)* ∈ ρ²Diff¹_b ([[rem:i-a-hypotheses]] (a)), whose quotient by ρ has
scattering symbol vanishing at
```

### T26. prop:iv6-1-1, the symbol and threshold at the sink (lines 2345–2347)

Old (3 lines):

```text
([[lem:iv6-0-1]] (b)), the shift is −2h⁻¹S̄, which gives [Hin26a, (B.25)].
The main term (2ℓ + 1)(σ − ξ) − 2h⁻¹S̄ is negative near the zero section iff
ℓ < −½ + h⁻¹ min spec S̄ = −½ + h⁻¹(1 − e)(1 − v); this is [Hin26a, (B.26)].
```

New (4 lines):

```text
([[lem:iv6-0-1]] (b)), the shift is −2h⁻¹S̄. So the principal symbol of the commutator term is
ρ^(−2ℓ)((2ℓ + 1)(σ − ξ) − 2h⁻¹S̄ + O(|ξ| + |η|))χ_0²χ₁²χ₂² plus the three cut-off terms of [[lem:iv6-0-flow]] (c)
([Hin26a, (B.25)]). The main term (2ℓ + 1)(σ − ξ) − 2h⁻¹S̄ is negative near the zero section iff
ℓ < −½ + h⁻¹ min spec S̄ = −½ + h⁻¹(1 − e)(1 − v), the threshold of [[def:iv6-0-2]] at R_out.
```

### T27. prop:iv6-1-1, the estimates for real and complex σ (lines 2360–2372)

Old (13 lines):

```text
The regularisation argument gives the strong form, and this proves [Hin26a, (B.20)], whose error term carries the
b-weight β. Near r = 0 the operator r²(□^C)^(σ) is b-elliptic ([[lem:iv6-0-1]] (c)), with Mellin transformed normal
operator that of r²(□^C)^(0). By (a) and the inversion ρ = r⁻¹, its indicial roots at r = 0 are −ι, with ι running over
those of [[lem:iv4-1-3]] at infinity. These have Re ι ∉ [−100, 19/10], and only ι = 2 in [−100, 2]. So no root at 0 has
real part in (−2, 100], and the b-weight β − 2 ∈ (−2, C_0] is root-free. With [β_0 − 2, β − 2] root-free as well, the
inverse Mellin transform of the normal operator gives [[eq:iv6-1-2]] from [Hin26a, (B.20)] ([[lem:s14-tf-inputs]]
(ii); [Hin26a, p. 89]). The dual estimate is the same with the propagation reversed.

*Complex σ.* Only R_out is characteristic ([[lem:iv6-0-flow]] (a)). Write σ⁻¹(□^C)^(σ) = P − iQ as in
[Hin26a, (B.29)], with Q_0 = 2ρh⁻¹S̄, P_1 = Re 2i(ρ²∂_ρ − (3/2)ρ), and Q_3 = (Im σ)Re (□^C)^(0) a nonnegative
absorption. With the same commutant, the zero-section symbol is (2ℓ + 1 − 2h⁻¹S̄)ρ^(−2ℓ). −AQ_3A has the sign of the
main term, because the b-principal symbol of (□^C)^(0) is ξ_b² + |η_b|², so (□^C)^(0) = Σ_jT_j*T_j + R with
T_j ∈ ρDiff¹_b and R ∈ ρ²Diff¹_b. The rest is subprincipal or elliptic ([Hin26a, p. 90]).
```

New (34 lines):

```text
*The estimates.* These three commutator arguments are those of the estimates of [[ch:s01]] at the boundary face over
∂X, which give them: the pieces (C), (D), (E) and (F) of the proof of [[thm:i-a-7-2]] (1) ([[sec:i-a-7-1]]), namely
[[prop:i-a-4-6]] at R_in, [[prop:i-a-5-2]] with [[rem:i-a-5-2-uses]] (ii) along Char_σ, [[prop:i-a-4-9]] at R_out and
the elliptic estimate [[prop:i-a-5-1]] off Char_σ. These use only the form (H1)–(H2) of [[sec:i-a-1-3]] on {ρ < ρ_1},
their commutants being microsupported at the boundary face, and near ρ = 0, (□^C)^(σ) = (□^C)^(0) + σT has this form
with T := 2iρ(ρ∂_ρ − 3/2 − h⁻¹S̄), S = h⁻¹S̄, Q = 0 and P₂ = 0 ([[eq:iv6-0-2]]; the ξ of [[ch:s01]] is −ξ here). Their
thresholds are those found above: in the fibre inner product for which an eigenbasis of S̄ is orthonormal, S̄ is
self-adjoint and ½ inf min spec(S + S^(*h)) = h⁻¹(1 − e)(1 − v) in [[prop:i-a-4-9]]; and ϑ_in = −2h⁻¹(1 − e)(1 + v)
([[eq:s14-theta-in]]), so that (−1 + ϑ_in)/2 = −½ − h⁻¹(1 − e)(1 + v) in [[prop:i-a-4-6]]. So an order admissible at
σ ([[def:iv6-0-2]]) satisfies the conditions of these estimates at σ₀ := σ. Moreover (□^C)^(σ) = N_tf(σ) for
P̂ := (□^C_b)^ ([[lem:iv6-0-1]] (d)), which satisfies (H1)–(H2) ([[lem:iv4-1-6]]) with the indicial gap (β_−, 2), and
2 − β ∈ [−C_0, 2) lies in that gap. So the proof of [[thm:i-c-4-3]] (1) ([[sec:i-c-4-4]]) applies with q := β and with
these estimates at σ₀ := σ in place of those of [[thm:i-a-7-2]] (1): near the boundary at infinity the pieces, the a
priori term at R_in being absorbed as there; in the interior the elliptic estimate (K2) of [[sec:i-c-2-1]]; and near
r = 0 [[lem:i-c-2-5]] and [[lem:i-c-2-6]] for L := r²(□^C)^(σ), which is b-elliptic with the normal operator of
r²(□^C)^(0) ([[lem:iv6-0-1]] (c), the terms with σ being O(r)), at the b-weight β − 2 ([[lem:s14-tf-inputs]] (ii)). By
[[lem:iv6-0-1]] (a) and the inversion ρ = r⁻¹, the indicial roots at r = 0 are −ι, with ι running over those of
[[lem:iv4-1-3]] at infinity. These have Re ι ∉ [−100, 19/10], and only ι = 2 in [−100, 2]. So no root at 0 has real
part in (−2, 100], and β − 2 ∈ (−2, C_0] is not the real part of a root. This gives, for every M and every ω in the
domain of [[eq:iv6-1-1]],

    ‖ω‖_(H^(s,(ℓ,β))_(sc,b)) ≤ C(‖(□^C)^(σ)ω‖_(H^(s−2,(ℓ+1,β−2))_(sc,b)) + ‖ω‖_(H^(−M,(−M,−M))_(sc,b)))     {#eq:iv6-1-4}

([Hin26a, (B.19)–(B.20)]), which implies [[eq:iv6-1-2]]; its strong sense is that of the pieces ([[rem:i-a-7-3]]) and
of [[lem:i-c-2-5]]. The adjoint chain of the same proof (the estimates (2) of
[[prop:i-a-4-6]] and [[prop:i-a-4-9]], [[prop:i-a-5-2]] along the backward field, and near r = 0 [[lem:i-c-2-5]] and
[[lem:i-c-2-6]] for the normal operator of the adjoint) gives [[eq:iv6-1-3]] with the error term
‖ω‖_(H^(−M,(−M,−M))_(sc,b)), which is smaller, for ω in the domain, and in the strong sense with the a priori orders of
[[eq:iv6-1-3]] ([[rem:i-a-7-3]]).

*Complex σ.* Only R_out is characteristic over ρ = 0 ([[lem:iv6-0-flow]] (a)); so off R_out the elliptic estimate
[[prop:i-a-5-1]] applies at the boundary face, and at R_out [[prop:i-a-4-9]] (1), for σ in any compact subset of
{σ ≠ 0, Im σ ≥ 0}, with the threshold found above. With ℓ constant near R_out and below that threshold, the proof of
[[thm:i-c-4-3]] (2) applies as for real σ and gives [[eq:iv6-1-4]] and the dual estimate.
```

### T28. prop:iv6-1-1, uniformity: the absorption and the orders (lines 2379–2379)

Old (1 lines):

```text
not depend on σ either, and −AQ_3A has the sign of the main term. So the estimate at R_out holds with constants
```

New (3 lines):

```text
not depend on σ either, and the absorption (Im σ)Re (□^C)^(0) has the sign of the main term, as
(□^C)^(0) = Σ_jT_j*T_j + R with T_j ∈ ρDiff¹_b and R ∈ ρ²Diff¹_b, its b-principal symbol being ξ_b² + |η_b|²
near ρ = 0 ((H2) of [[sec:i-a-1-3]], which (□^C)^(σ) satisfies, as above). So the estimate at R_out holds with constants
```

### T29. prop:iv6-1-1, uniformity: the orders on a set (lines 2384–2387)

Old (4 lines):

```text
[[rem:i-a-5-2-uses]] (ii) for the absorption (Im σ)Re T. Their constants are uniform for σ ∈ I + i[0, ν], I a compact
interval about ±1 not containing 0 (for [[prop:i-a-5-2]] by the argument of the proof of [[thm:i-a-7-2]] (1)), the
orders being admissible at every real σ₀ ∈ I with uniform margins, as the
orders constructed in the proof of [[lem:i-a-7-1]] are.
```

New (6 lines):

```text
[[rem:i-a-5-2-uses]] (ii) for the absorption (Im σ)Re T. Their constants are uniform for σ ∈ I + i[0, ν], I the
compact interval of the Re σ, σ in the given set near ±1, which does not contain 0 (for [[prop:i-a-5-2]] by the
argument of the proof of [[thm:i-a-7-2]] (1)): the orders are admissible on that set ([[def:iv6-0-2]]), hence at every
real σ₀ ∈ I, with uniform margins and constancy neighbourhoods, as ℓ is continuous and constant near each R_(σ₀,in),
σ₀ ∈ I, hence near the compact connected union of these. The orders constructed in the proof of [[lem:i-a-7-1]] are of
this kind.
```

### T30. thm:iv6-2-1, the energy estimates near X_0 (lines 2458–2460)

Old (3 lines):

```text
[[prop:iv5-6-1]], with the level-set density r⁴|dr d𝑔̸|, gives [Hin26a, (B.34) and (B.35)] at T := ½, with
ρ_sf = (1 + r)⁻¹ and ρ_cf = r(1 + r)⁻¹ there. In it, [[lem:iv5-6-tform]] and [[cor:iv5-6-energy]] are used on
N := ℝ_t × (ℝ⁴ ∖ 0), with k = 1 and f_1 := τ − T, as there is no inner boundary. Their hypotheses hold: the components
```

New (15 lines):

```text
[[prop:iv5-6-1]] (1), with the level-set density r⁴|dr d𝑔̸|, gives at T := ½, with ρ_sf = (1 + r)⁻¹ and
ρ_cf = r(1 + r)⁻¹ there, its two estimates on M with the weight ρ_sf^(α_sf)ρ_cf^(α_cf) in place of ρ_sf^(α_sf)
([Hin26a, (B.34) and (B.35)]): for ω vanishing for t < 0,

    ‖ω‖_(H^(1,(α_sf,α_cf))_(eb,h)(τ⁻¹([0,T]))) ≤ Ch⁻¹‖P_hω‖_(H^(0,(α_sf+2,α_cf−2))_(eb,h)(τ⁻¹([0,T]))),    {#eq:iv6-2-e1}

and, with no support condition, there being no inner boundary,

    ‖ω‖_(H^(1,(−α_sf−2,−α_cf+2))_(eb,h)(τ⁻¹([0,T/2])))
        ≤ C(h⁻¹‖P_h*ω‖_(H^(0,(−α_sf,−α_cf))_(eb,h)(τ⁻¹([0,T]))) + ‖ω‖_(H^(1,(−α_sf−2,−α_cf+2))_(eb,h)(τ⁻¹([T/2,T])))).
                                                                                                         {#eq:iv6-2-e2}

In it, [[lem:iv5-6-tform]], [[cor:iv5-6-energy]], [[lem:iv5-6-transport]] and [[lem:iv5-6-core]] are used on
N := ℝ_t × (ℝ⁴ ∖ 0), with k = 1, f_1 := τ − T and w := ρ_sf^(−α_sf−2)ρ_cf^(−α_cf+2)e^(−𝔛τ) for [[eq:iv6-2-e1]], and
f_1 := −τ and w := ρ_sf^(α_sf)ρ_cf^(α_cf)e^(𝔛τ) for [[eq:iv6-2-e2]]. Their hypotheses hold: the components
```

### T31. thm:iv6-2-1, the bulk covectors (lines 2463–2464)

Old (2 lines):

```text
0 ≤ τ ≤ ½; and r dρ_sf/ρ_sf and r dρ_cf/ρ_cf are bounded, so that the bulk covector of the weight is past timelike,
with a uniform κ, for 𝔛 large.
```

New (2 lines):

```text
0 ≤ τ ≤ ½; and r dρ_sf/ρ_sf and r dρ_cf/ρ_cf are bounded, so that rη_0 and rη_1 of [[lem:iv5-6-core]] are past
timelike (for [[eq:iv6-2-e2]], with −c and the opposite time orientation), with a uniform κ, for 𝔛 large.
```

### T32. thm:iv6-2-1, nonzero and infinite frequencies (lines 2466–2468)

Old (3 lines):

```text
*Nonzero and infinite frequencies.* [Hin26a, (B.37)] is [[prop:iv5-1-3]] with the cut-offs χ_j(τ) of
[Hin26a, (B.36)] and no cut-off in r. There is no E_r term; the E_τ term is a negative square because ±H_Gτ > 0 at
future, resp. past, lightlike covectors, dτ being past timelike on supp χ₁′.
```

New (4 lines):

```text
*Nonzero and infinite frequencies.* The estimates [[eq:iv5-fib]] and [[eq:iv5-fib-adj]] of [[prop:iv5-1-3]] hold on M,
by its proof, with the weights of [[eq:iv6-2-e1]], resp. [[eq:iv6-2-e2]], the cut-offs χ_(τ,j) of [[sec:iv5-1]]
at T and no cut-off in r (χ_(r,j) := 1) ([Hin26a, (B.36)–(B.37)]). There is no E_r term; the E_τ term is a negative
square because ±H_Gτ > 0 at future, resp. past, lightlike covectors, dτ being past timelike on supp χ′_(τ,1).
```

### T33. thm:iv6-2-1, the symbols at the cone face (lines 2472–2474)

Old (3 lines):

```text
a = w⁻¹χ_cf(𝔛ρ_cf)χ_0(𝔛|ζ|)χ₁(t/r), w := ρ_sf^(α_sf+1)ρ_cf^(α_cf−1). The symbol identity is [Hin26a, (B.38)]:
aH_(−ℓ+j)a − Sa² = −c_0r⁻²a² − b_0² − b_cf² + e_τ² + f. Since dw/w ≡ (α_cf − 1)dr/r modulo
ρ_cf C^∞(M; ^(eb)T*M), the square roots exist for the following reasons.
```

New (10 lines):

```text
a = w⁻¹χ_cf(𝔛ρ_cf)χ_0(𝔛|ζ|)χ₁(t/r), w := ρ_sf^(α_sf+1)ρ_cf^(α_cf−1), with 𝔛 := δ_r⁻¹, χ_cf a cut-off equal to 1 on
[0, 5/2] and supported in [0, 4), and χ₁ := χ_(τ,0) of [[sec:iv5-1]] at T, δ_r being fixed below so small that 𝔛 is
large enough. By
[[lem:iv5-2-symbols]], with r⁻¹ for ρ_sf, aH_(−ℓ+j)a − Sa² = −c_0r⁻²a² − b_0² − b_cf² + e_τ² + f ([Hin26a, (B.38)]),
with f as there and, χ_cf, χ_cf′ being evaluated at 𝔛ρ_cf and χ₁, χ₁′ at t/r,

    b_0 := a(S − ℓ(dw/w) − wH_j(w⁻¹) − c_0r⁻²)^(1/2),     b_cf := w⁻¹χ₁χ_0(−𝔛χ_cfχ_cf′)^(1/2)(−ℓ(dρ_cf) + H_jρ_cf)^(1/2),
    e_τ := w⁻¹χ_cfχ_0(χ₁χ₁′)^(1/2)(−ℓ(d(t/r)) + H_j(t/r))^(1/2).

Since dw/w ≡ (α_cf − 1)dr/r modulo ρ_cf C^∞(M; ^(eb)T*M), the square roots exist for the following reasons.
```

### T34. thm:iv6-2-1, the estimates at the cone face (lines 2488–2489)

Old (2 lines):

```text
This gives [Hin26a, (B.39)], whose a priori term lies in τ ≤ (2.75/10)T, covered by [Hin26a, (B.34)]; and
[Hin26a, (B.40)] for P_h* likewise.
```

New (8 lines):

```text
This gives, by the proof of [[prop:iv5-3-1]] (1), the estimate of the form of [[prop:iv5-3-1]] (1) at 𝖼𝖿, with 𝖼𝖿,
ρ_cf and the weights of [[eq:iv6-2-e1]] in place of ∂K⁺, ρ_K and those of M^♭, its operator E elliptic on
supp χ₁′(t/r) ⊂ {τ ≤ (2.75/10)T}, which [[eq:iv6-2-e1]] covers; we call it the forward cone estimate
([Hin26a, (B.39)]). For P_h*, with the commutant wχ_cf(𝔛ρ_cf)χ_0(𝔛|ζ|)χ̃(τ), χ̃ a non-decreasing cut-off in τ, and 𝓛_h*,
[[lem:iv5-2-symbols]] gives aH_(−ℓ+j)a + Sa² = c_0r⁻²a² + b_0² − b_cf² + b_τ² + f with the symbols formed in the same
way: the term of χ̃ has the sign of the main term, and that of χ_cf gives the a priori term. This gives the estimate of
the form of [[prop:iv5-3-1]] (2) at 𝖼𝖿, with the weights of [[eq:iv6-2-e2]], its a priori operator elliptic on
supp χ_cf′(𝔛ρ_cf) ∩ supp χ̃; we call it the backward cone estimate ([Hin26a, (B.40)]).
```

P-G1 C33-20 inserts a paragraph before the old text of T34, which T34 replaces. If both are merged, insert the
paragraph of C33-20 before the new text of T34, that is, before its first line, "This gives, by the proof of
[[prop:iv5-3-1]] (1), …".

### T44. thm:iv6-2-1, the choice of 𝔛 at the cone face (lines 2497–2497)

Old (1 lines):

```text
the dilations), and that (6) holds on 𝗌𝖿 ∩ {s ∈ [δ_r, v(1 − δ_sf)]}. Then:
```

New (2 lines):

```text
the dilations), that (6) holds on 𝗌𝖿 ∩ {s ∈ [δ_r, v(1 − δ_sf)]}, and that 𝔛 = δ_r⁻¹ is as large as the cone-face
symbols need. Then:
```

### T35. thm:iv6-2-1, item (a) (lines 2499–2499)

Old (1 lines):

```text
(a) [Hin26a, (B.39) and (B.40)] hold on {ρ_cf ≤ 4δ_r} ∩ {τ ≥ T/40}, globally in t, with a priori sets in
```

New (2 lines):

```text
(a) The forward cone estimate holds on {ρ_cf < 4δ_r} ∩ {τ ≥ T/40} and the backward one on
{ρ_cf < 4δ_r} ∩ {τ ≥ (2.75/10)T}, globally in t, with a priori sets in
```

### T36. thm:iv6-2-1, the combination (lines 2512–2518)

Old (7 lines):

```text
*Combination.* *Forward*: [Hin26a, (B.34)] on {τ ≤ ½} and [Hin26a, (B.37)]; (a) forward; (c) (1) on every compact
subset of Ω ∩ {ρ_cf ≥ 2δ_r}, from [Hin26a, (B.34)] and (a), with ε_X ≤ δ_rT so that its set {½ε_X ≤ t ≤ ε_X} lies
under [Hin26a, (B.34)], as τ ≤ ε_X/δ_r on {ρ_cf ≥ δ_r}; (b) along 𝗌𝖿 from s ∈ [2δ_r, 3δ_r] (by (a), as
ρ_cf = s/(1 + s) + O(ρ_sf) near 𝗌𝖿) and from s ∈ [5, 10] (by [Hin26a, (B.34)]), their interior a priori sets by (c);
and the sink, its a priori sets by (b) and (c). These cover a neighbourhood of o over Ω: near 𝖼𝖿 by (a) and
[Hin26a, (B.34)], near 𝗌𝖿 by (a), (b), the sink and [Hin26a, (B.34)], and the compact rest by (c). This gives
[Hin26a, (B.41)] at the Sobolev order 1, and at every order ≥ 1 by extension and restriction. *Adjoint*: the sink,
```

New (11 lines):

```text
*Combination.* *Forward*: [[eq:iv6-2-e1]] on {τ ≤ ½} and [[eq:iv5-fib]] on M; (a) forward; (c) (1) on every compact
subset of Ω ∩ {ρ_cf ≥ 2δ_r}, from [[eq:iv6-2-e1]] and (a), with ε_X ≤ δ_rT so that its set {½ε_X ≤ t ≤ ε_X} lies
under [[eq:iv6-2-e1]], as τ ≤ ε_X/δ_r on {ρ_cf ≥ δ_r}; (b) along 𝗌𝖿 from s ∈ [2δ_r, 3δ_r] (by (a), as
ρ_cf = s/(1 + s) + O(ρ_sf) near 𝗌𝖿) and from s ∈ [5, 10] (by [[eq:iv6-2-e1]]), their interior a priori sets by (c);
and the sink, its a priori sets by (b) and (c). These cover a neighbourhood of o over Ω: near 𝖼𝖿 by (a) and
[[eq:iv6-2-e1]], near 𝗌𝖿 by (a), (b), the sink and [[eq:iv6-2-e1]], and the compact rest by (c). This gives

    ‖ω‖_(H^(1,(α_sf,α_cf))_(eb,h)(Ω)^(•,−)) ≤ Ch⁻¹‖P_hω‖_(H^(0,(α_sf+2,α_cf−2))_(eb,h)(Ω)^(•,−))           {#eq:iv6-2-ap}

([Hin26a, (B.41)]) at the Sobolev order 1, and the same estimate at every order s ≥ 1, with H^(s) and H^(s−1), by
extension and restriction. *Adjoint*: the sink,
```

### T37. thm:iv6-2-1, the adjoint chain (lines 2521–2524)

Old (4 lines):

```text
t_1 < δ_r/9, as ρ_cf ≥ 2δ_r gives r ≥ 2δ_r), which contains the a priori set of [Hin26a, (B.40)], its χ₂(τ) being
supported in τ ≥ (2.25/10)T > κ; its late set (large t, r ≤ (t + c₁)/κ, ρ_cf ≥ δ_r) lies near 𝗌𝖿 with s ∈ [δ_r, 10], by
κ = 1/9, covered by the previous two steps; (a) adjoint, that is [Hin26a, (B.40)], its a priori set
{(5/2)δ_r ≤ ρ_cf ≤ 4δ_r} covered by (c) (2) and, near 𝗌𝖿, by (b) (2); and [Hin26a, (B.35)], its a priori set
```

New (5 lines):

```text
t_1 < δ_r/9, as ρ_cf ≥ 2δ_r gives r ≥ 2δ_r), which contains the a priori set of the backward cone estimate, its
cut-off χ̃ := χ_(τ,2) being supported in τ ≥ (2.25/10)T > κ; its late set (large t, r ≤ (t + c₁)/κ, ρ_cf ≥ δ_r) lies
near 𝗌𝖿 with s ∈ [δ_r, 10], by κ = 1/9, covered by the previous two steps; (a) adjoint, that is the backward cone
estimate, its a priori set {(5/2)δ_r ≤ ρ_cf ≤ 4δ_r} covered by (c) (2) and, near 𝗌𝖿, by (b) (2); and [[eq:iv6-2-e2]],
its a priori set
```

### T38. thm:iv6-2-1, strong uniqueness (lines 2535–2535)

Old (1 lines):

```text
localisation in (t − 1)/r), together with [Hin26a, (B.37) and (B.39)]. So a solution with zero forcing that is supported
```

New (2 lines):

```text
localisation in (t − 1)/r), together with [[eq:iv5-fib]] on M and the forward cone estimate. So a solution with zero
forcing that is supported
```

### T39. thm:iv6-3-1, the uniformity clause (lines 2543–2543)

Old (1 lines):

```text
uniformly for σ in each sector where fixed orders are admissible ([[prop:iv6-1-1]]).
```

New (2 lines):

```text
uniformly for σ in each set on which fixed orders are admissible ([[def:iv6-0-2]]) and [[eq:iv6-1-2]] holds uniformly
([[prop:iv6-1-1]]).
```

### T40. thm:iv6-4-1, admissibility of the orders of [[sec:i-c-4]] (lines 2654–2655)

Old (2 lines):

```text
those of [[lem:i-a-7-1]] at σ_* = ±1, constant near the radial sets and monotone along the flow, functions of ξ
and |η|²; and their thresholds are those of [[eq:i-a-1-5]] for (□^C_b)^, which are the data of □^C_b at ρ = 0
```

New (4 lines):

```text
those of [[lem:i-a-7-1]] at σ_* = ±1, constant near the radial sets and monotone along the flow, functions of ξ
and |η|², and admissible on {e^(iθ) : θ ∈ Θ_±}, being admissible for every σ₀ ∈ J_± ∋ Re e^(iθ) ([[sec:i-c-4-3]]); the
constant orders used for θ ∈ (0, π) ([[thm:i-c-4-3]] (2)) are admissible at e^(iθ), being constant below the threshold
at R_out; and the thresholds are those of [[eq:i-a-1-5]] for (□^C_b)^, which are the data of □^C_b at ρ = 0
```

## 6. What is not proved here, and why

### 6.1 The relative index theorem in the index-0 part of prop:iv6-1-1

Steps (i) and (iii) of the index-0 argument (lines 2408–2424) move the b-weight at r = 0 of the map (eq:iv6-1-1) on one
sector. They read the change of index off [Mel93, Theorem 6.5], which is quoted in Appendix A as thm:std-relative-index.

The quoted theorem is stated for b-elliptic operators on a compact manifold with boundary. The operator here is b at
r = 0 and scattering, with radial points, at r = ∞. So the theorem does not apply as quoted, and "[Hin26a, p. 91]" does
not close the gap.

The claim is true, by the standard localisation argument, and a proof needs about a page. Write D := {u ∈ 𝒳_(β₁) :
Pu ∈ 𝒴_β} for β₁ < β, both weights free of roots.

1. Elements of D expand near r = 0, modulo 𝒳_β, in the formal solutions of the normal operator with exponents in the
   strip. This is the Mellin contour shift of lem:i-c-2-3 and lem:i-c-2-7, with the residues kept.
2. Each formal solution, cut off near r = 0, lies in D.
3. So dim D/𝒳_β is the number of roots in the strip, with multiplicity, and ind(P|_D) = ind(P|_(𝒳_β)) + dim D/𝒳_β.
4. Finally, ind(P|_D) = ind(P|_(𝒳_(β₁))), because the range of P on D is that on 𝒳_(β₁) intersected with 𝒴_β, which is
   dense in 𝒴_(β₁).

Step 1 needs the multiplicity count for the matrix indicial polynomials of the sectors, which is not written anywhere in
the paper. This is a published theorem applied beyond its stated hypotheses, not a preprint step, so it is classified
(c) and left open here; the step is being proved separately (proofs/P-RI.md), and this file keeps its marker. As the
reader of this file notes, the multiplicity count may be short: at a root z of a sector's regular matrix indicial
polynomial, Melrose's rank_j(z) is the order of vanishing of its determinant at z (the sum of the partial multiplicities,
by the Smith form), and those determinants are the P_l and p_(v) of prop:np-10-12, whose roots lem:iv4-1-3 (a) counts.

### 6.2 The calculus facts (G1)

These are listed in section 2 as (a-G1) and are left to P-G1, whose texts C33-1 to C33-20 they are:
[Hin26a, §2.3] ×3, [Hin26a, p. 45], [Hin26a, (5.44)–(5.46)], [Hin23d], [Shu92] and [Hin26d] in prop:np-10-65-a.

### 6.3 Details the texts leave at the chapter's own level

- **The h^(1/2) iteration** (T41) enlarges supports by a fixed small amount, using "positivity persists by continuity".
  Each positivity used is strict on a compact set, so this holds; it is not quantified further.

## 7. Checks (on the scratch copy)

The scratch copy is the current `chapters/`, `crosswalk/`, `assemble.py` and `lint.py`, in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pg24b/. T1–T45 were
applied to chapter 33 at HEAD (md5 147ca162…), with T41 in its variant for the current text, and the 16 crosswalk rows
of section 9 were added.

Before the texts were applied:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4652 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4652, computations cited 0, problems 0

After:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4668 label(s) defined, 0 hit(s)
    $ python3 assemble.py --check
    labels 4668, computations cited 0, problems 0
    $ python3 assemble.py; python3 lint.py --paper
    PAPER.md: 0 hit(s)

Further checks:

- **Resolved lines.** No line of the assembled PAPER.md exceeds 121 characters. The conservative test,
  with every new label resolved as "Proposition 49.999", also finds no line over 121.
- **Crosswalk.** 216 rows for 216 labels, in chapter order; the 200 old rows keep their order.
- **Typography.** No backslash in chapter 33. No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|"
  (lint).
- **Old texts.** Each of the 45 old texts occurs exactly once in the chapter at HEAD, and no two overlap. Applying them
  to that chapter reproduces the checked scratch chapter exactly. The variant A old text of T41 occurs exactly once in
  the new text of P-G1 C33-11 as P-G1 now stands, and the 45 texts also apply after P-G1's (section 8).

## 8. Overlap with P-G1

proofs/P-G1.md exists. Its chapter-33 old texts, as P-G1 stands in its fix round, were compared with those of this file
in the chapter at HEAD. P-G1 gives the line numbers of an earlier chapter, two lower than the ones here from line 127 on.

- **C33-11 and T41 overlap.** C33-11 replaces the whole "For Q: …" paragraph, including the sentence that T41 replaces.
  T41 is therefore given in two variants. P-G1 merges first, so use variant A, given below T41; its old text is the last
  two lines of C33-11's new text, which P-G1 states it keeps unchanged. If T41 were merged on the current text instead,
  C33-11 would have to stop before "Collecting", and its last paragraph ("Collecting, the Q-terms add at most
  (9C₂ + 2)𝔛⁻² + C′_𝔛h to the coefficient −c_0 of ‖Aω‖², …") would go into T41's first sentence.
- **C33-12 and T7 share one sentence.** The old text of T7 ends with "[[lem:iv5-0-5]] (6) on supp ψ′." at the start of
  line 1536, and the old text of C33-12 is that whole line. Both new texts keep these words in place, so either order
  works: after C33-12 the old text of T7 is found once, and after T7 the old text of C33-12 is. After both, the line is
  "[[lem:iv5-0-5]] (6) on supp ψ′. Q enters with a lower bound, the adjoint pairing containing +h⁻¹⟨AQAω, ω⟩:", 106
  characters.
- **C33-20 and T34.** C33-20 inserts a paragraph before the sentence "This gives [Hin26a, (B.39)], …", which T34
  replaces. If both are merged, insert C33-20's paragraph before T34's new text; P-G1 says the same.
- **Adjacent but not overlapping.** T42 (line 1465) and C33-9 (line 1466); T5 (line 1507) and C33-10 (line 1508).
- **No other overlap.** C33-1 to C33-10 and C33-13 to C33-19 share no characters with T1–T45; C33-4 inserts before
  line 1398, which no text here touches.
- **Simulated merge in P-G1's order.** All of P-G1's chapter-33 texts (C33-1 to C33-20, with C33-4 the new section and
  C33-3 the deletion) were applied to the chapter at HEAD, and then T1–T45 with variant A for T41. Each of the 45 old
  texts occurs exactly once in the chapter after P-G1, no two overlap, and the paragraph of C33-20 ends up immediately
  before the new text of T34. The combined chapter has no line over 121 characters and no backslash. The P-G1 reader
  ran the full merge in this order (P-G1, then T1–T45 with variant A) and found every old text once, lint 0 hits and
  assembly 0 problems.

## 9. Crosswalk

New rows for crosswalk/33-s14-constraint-damping.tsv, in its four tab-separated columns, the source pinned as
"paper/reader/proofs/P-G24b.md@PENDING:N", N the line of this file that carries the label. Each row goes after the row of
the label named before it, which keeps the file in chapter order.

| new label | goes after the row of |
|---|---|
| eq:iv5-2-a | eq:iv5-2-1 |
| lem:iv5-2-symbols | eq:iv5-2-a |
| eq:iv5-2-leibniz | lem:iv5-2-symbols |
| eq:iv5-2-iter | prop:iv5-2-1 |
| eq:iv5-2-adj | eq:iv5-2-iter |
| lem:iv5-6-transport | eq:iv5-6-energy |
| eq:iv5-6-transport | lem:iv5-6-transport |
| lem:iv5-6-core | eq:iv5-6-transport |
| eq:iv5-6-core | lem:iv5-6-core |
| eq:iv5-6-core-1 | eq:iv5-6-core |
| eq:iv5-6-core-2 | eq:iv5-6-core-1 |
| eq:iv6-1-3 | eq:iv6-1-2 |
| eq:iv6-1-4 | eq:iv6-1-3 |
| eq:iv6-2-e1 | eq:iv6-2-1 |
| eq:iv6-2-e2 | eq:iv6-2-e1 |
| eq:iv6-2-ap | eq:iv6-2-e2 |

```text
eq:iv5-2-a	paper/reader/proofs/P-G24b.md@PENDING:359	commutants of [Hin26a, §5.2.2–5.2.5], common form	a = w^-1 phi_1...phi_m chi_0(X|zeta|); cut-off conventions with smooth (+-chi chi')^(1/2), existence by an explicit formula
lem:iv5-2-symbols	paper/reader/proofs/P-G24b.md@PENDING:368	[Hin26a] (5.39)-(5.43), (5.54), (5.57), (5.60), (B.38): the symbol decompositions	Leibniz identity for aH_(-l+j)a -+ Sa^2 of a product commutant; replaces "the b_0, b_R, e and f of [Hin26a]"
eq:iv5-2-leibniz	paper/reader/proofs/P-G24b.md@PENDING:372	[Hin26a] (5.39)-(5.43)	the identity and the definition of f
eq:iv5-2-iter	paper/reader/proofs/P-G24b.md@PENDING:445	[Hin26a] (5.47)-(5.48)	the estimate before the h^(1/2) iteration; text T41 (variant for the current text; a variant after P-G1 C33-11 is given)
eq:iv5-2-adj	paper/reader/proofs/P-G24b.md@PENDING:509	[Hin26a] (5.49)-(5.50)	the adjoint pairing for L_h*, used in prop:iv5-2-1 (2), prop:iv5-5-2 (2), prop:iv5-5-3 (2)
lem:iv5-6-transport	paper/reader/proofs/P-G24b.md@PENDING:718	[Hin26a] (5.77), the fundamental theorem of calculus for L_h, as an identity	A = -1/2 l<nabla> + N; integrated identity for 2B(Aw, w) with boundary terms; |N|, |S| = O(r^-2)
eq:iv5-6-transport	paper/reader/proofs/P-G24b.md@PENDING:726	[Hin26a] (5.77)	the integrated transport identity
lem:iv5-6-core	paper/reader/proofs/P-G24b.md@PENDING:754	[Hin26a] (5.70)-(5.78), the energy argument of Proposition 5.16	energy estimate for h^2 box + 2hA + hY from eq:iv5-6-energy and eq:iv5-6-transport, with good and bad boundary pieces; explicit lambda_*, C_*
eq:iv5-6-core	paper/reader/proofs/P-G24b.md@PENDING:768	[Hin26a] (5.74), (5.76), (5.78)	the conclusion of lem:iv5-6-core
eq:iv5-6-core-1	paper/reader/proofs/P-G24b.md@PENDING:793	[Hin26a] (5.74)-(5.76)	the energy step
eq:iv5-6-core-2	paper/reader/proofs/P-G24b.md@PENDING:804	[Hin26a] (5.77)-(5.78)	the transport step
eq:iv6-1-3	paper/reader/proofs/P-G24b.md@PENDING:1083	[Hin26a] (B.28)	the dual estimate, displayed
eq:iv6-1-4	paper/reader/proofs/P-G24b.md@PENDING:1175	[Hin26a] (B.19)-(B.20), p. 89	the estimate with error term in H^(-M,(-M,-M)), by the boundary-face pieces of ch. 20 and the proof of thm:i-c-4-3
eq:iv6-2-e1	paper/reader/proofs/P-G24b.md@PENDING:1245	[Hin26a] (B.34)	energy estimate near X_0 on M, forward
eq:iv6-2-e2	paper/reader/proofs/P-G24b.md@PENDING:1251	[Hin26a] (B.35)	energy estimate near X_0 on M, adjoint
eq:iv6-2-ap	paper/reader/proofs/P-G24b.md@PENDING:1398	[Hin26a] (B.41)	the a priori estimate of thm:iv6-2-1 at Sobolev order 1
```

Notes to append to existing rows, each with "; P-G24b:" before it:

- def:iv5-0-1: "∂_(z^μ) ∈ ρ_sf𝒱_3b by r⁻¹ ∈ ρ_sf C^∞ (T1)"
- lem:iv5-0-2: "(c) proved: classes of ∇, □_g, δ*_g, δ_g (T2)"
- lem:iv5-0-5: "δ_r < 1/5 added (T3)"
- prop:iv5-1-3: "(5.30) and (5.28) displayed (T42, T43)"
- prop:iv5-7-1: "the estimates near Σ^♯ on the extended domain need lem:iv5-0-3 (a), (c), lem:iv5-0-4 and the bounds of the
  proof of prop:iv5-6-1 (T45)"
- sec:iv5-2: "cut-off conventions (cut-offs positive on their support) and lem:iv5-2-symbols inserted (T4)"
- prop:iv5-2-1: "cut-offs defined; b_0, b_R, e from lem:iv5-2-symbols; adjoint pairing eq:iv5-2-adj; (5.47)–(5.48) and the
  iteration written out as eq:iv5-2-iter (T5–T7, T41)"
- prop:iv5-3-1: "cut-offs defined (χ_K now supported in [0, 2δ_r)); symbols from lem:iv5-2-symbols (T8–T10)"
- prop:iv5-4-1: "χ_R a cut-off; b_0, e₁, e₂ explicit (T11–T12)"
- prop:iv5-5-1: "χ₂, χ_K defined; b_0, e_R, e_T explicit (T13–T14)"
- prop:iv5-5-2, prop:iv5-5-3: "adjoint pairing cites eq:iv5-2-adj (T15, T16)"
- cor:iv5-6-energy: "(i) allows k = 3 (T17)"
- prop:iv5-6-1: "second estimate of (1) needs ω supported at Σ^♯ (T19; counterexample in P-G24b §3); proof rewritten from
  lem:iv5-6-core, all four estimates and eq:iv5-6-1, every h ∈ (0, 1] (T20)"
- thm:iv5-7-3: "(b): continuity in τ from eq:iv5-6-core (T21); Cauchy problem via thm:std-bgp-development and
  thm:std-bgp-cauchy (5) (T22)"
- def:iv6-0-2: "admissibility at complex σ only at R_out; admissible at real σ₀; admissible on a set, as in sec:i-a-1-4
  (T23)"
- prop:iv6-1-1: "dual estimate displayed (eq:iv6-1-3), its strong sense with ℓ_1 above the threshold at R_out; shift and
  sink symbol defined; (B.20), (B.29), pp. 89–90 replaced
  by the pieces of ch. 20 and the proof of thm:i-c-4-3 (eq:iv6-1-4); uniformity on sets of admissible orders (T24–T29)"
- thm:iv6-2-1: "(B.34)–(B.35) displayed (eq:iv6-2-e1, eq:iv6-2-e2); (B.36)–(B.37) as eq:iv5-fib on M; (B.38) symbols from
  lem:iv5-2-symbols, with 𝔛 = δ_r⁻¹ and χ_cf supported in [0, 4); (B.39)–(B.40) the forward and backward cone estimates,
  on {τ ≥ T/40} and {τ ≥ (2.75/10)T}; (B.41) displayed (eq:iv6-2-ap) (T30–T38, T44)"
- thm:iv6-3-1: "uniformity clause refers to def:iv6-0-2 (T39)"
- thm:iv6-4-1: "orders admissible on Θ_± and the middle sector (T40)"
