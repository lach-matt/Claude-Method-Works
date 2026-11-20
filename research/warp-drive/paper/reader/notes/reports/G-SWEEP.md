# G-SWEEP: unproved or uncovered statements in the reader's edition

Auditor's inventory, read-only. Paper: `research/warp-drive/paper/reader/`, chapters as committed on 2026-11-20
(STATUS: final build, every chapter CONFIRMED). File:line references are to `chapters/*.md`. Nothing in the
repository was changed.

## How the sweep was done

1. **Phrase greps over all 62 chapter files**, with each hit read in context. The phrases were: not prove(d),
   not shown, not known, we assume, is/are assumed, conjecture, heuristic, not covered, left open, not carried,
   does not establish, not attempted, not treated / does not treat, is open, not determined, not decided,
   not evaluated, should, expected, presumably, formally, provided, would give/need/follow, standard,
   well-known, classical, omitted, verbatim, carries over, the same proof/argument, as in [..],
   used as stated, as stated, in every/any dimension, free of the dimension.
2. **Dependency checks.** Labels were traced with grep from each candidate to its users. A script checked
   whether any of the 44 remarks headed "(Numerical observation.)" is cited inside a `*Proof*…∎` block.
3. **A citation audit.** Every numbered literature citation (`[Key, Theorem/Lemma/…]`) in the chapters was
   compared with the sources Appendix A (ch. 95) quotes. Each source's status (published, preprint, lecture
   notes) was taken from ch. 98. The aim was to find results that are used but neither proved nor quoted from
   a published source.
4. **A sample of "in dimension 4 + 1" adaptations** (section 3).
5. **Comparison with the coordinator's records**: `notes/reports/final-report-items.txt` (FRI) and
   `INTEGRATION.md` (INT).

## Summary

- **Real gaps: 5.** They are G1–G5 below. Four of them sit in one place: the constraint-damping analysis of
  ch. 33, §§iv5–iv6. The fifth is item (3) of thm:own-data. None is recorded in FRI or INT.
- **Main theorems affected:**
  - **thm:settling** (i) and (ii), with everything downstream of the stability theory: thm:own-data,
    prop:interior, the linear statements thm:viii-2-2 / cor:viii-2-3, thm:rw-settling and thm:harmonic-rate.
    The route is thm:iii-e-1-1 (constraint damping), which ch. 34, 35, 38 and 46 use.
  - **thm:own-data**, item (3) in particular (G3).
  - **thm:main, thm:past-construction and thm:bondi-law: no gap found.** Their chain (ch. 02–10) cites only
    published results quoted in Appendix A, or derives what it uses ([TTS09] and [Tou23a/b] are comparisons only).
- **Numerical observations used by a proof: none.** No numerical-observation label occurs inside a proof.

---

## 1. Real gaps, used by proofs of stated results (ranked by importance to the main theorems)

### G1. The semiclassical 3b-calculus, with the sharp Gårding inequality, rests on preprints and is not quoted

- **Where:**
  - 33-s14-constraint-damping.md:1210–1212, def:iv5-0-1: "The semiclassical 3b-pseudodifferential calculus
    Ψ_(3b,ħ)(M^♭) carries with it … elliptic parametrices, the sharp Gårding inequality and the Sobolev
    spaces …; it exists in this dimension by [[prop:np-10-65-a]]".
  - 33:1221–1228, prop:np-10-65-a, which cites "[Hin26a, Section 2.3] … [Hin23d, … Proposition 5.10, p. 109]
    … [Hin26d …]". Its proof reads, in full: "*Proof.* These are the cited results, stated there for every
    dimension. ∎"
- **What is assumed.** The whole semiclassical 3b-calculus on M^♭ in dimension 4 + 1: composition, adjoints,
  principal symbols, WF′, elliptic parametrices, L²-boundedness on the weighted spaces H^(s,(β_sf,β_K))_(3b,h),
  and the **sharp Gårding inequality**. The sharp Gårding inequality is used at 33:1458 ("which gives [Hin26a,
  (5.45)] by Gårding", inside the proof of prop:iv5-2-1). The uniformity argument at 33:1935 lists the calculus
  estimates it relies on as composition, elliptic parametrices, the sharp Gårding inequality and L²-boundedness.
- **Why it is a gap:**
  - [Hin23d] and [Hin26a] are listed as preprints in ch. 98.
  - Appendix A quotes neither of them. Its only [Hin26a] entry (thm:std-hin26a-cform, Proposition 5.1) is
    cited by no chapter.
  - Appendix A's [Hin26d] entry (thm:std-sbg-calculus, 95:836) quotes the non-semiclassical scaled
    bounded-geometry calculus. It contains no semiclassical statement and no Gårding inequality.
  - Ch. 23 deliberately avoids sharp Gårding for the e3b calculus (23:466, 23:2177). Ch. 33 does not.
- **Depends on it:**
  - prop:iv5-1-2, prop:iv5-1-3, prop:iv5-2-1, prop:iv5-3-1, prop:iv5-5-x, prop:iv5-6-1 and prop:iv5-7-1;
  - then thm:iv5-7-3 ([Hin26a, Theorem 5.2] in 4 + 1, 33:1862), thm:iv4-2-1 (= thm:iii-e-1-1 (1)–(3), 33:2269),
    and the transition-face theorem thm:iv6-2-1 (33:2136, 2156), hence thm:iii-e-1-1 (4);
  - thm:iii-e-1-1 is used in ch. 34 (10 sites), 35, 38 and 46 (6 sites), so **thm:settling** and everything
    built on the stability theory, including **thm:own-data**.
- **Size.** It depends on whether a published source states the calculus:
  - If [Hin26d] (published, which prop:np-10-65-a says has the 3b-algebra as example (10)) or another published
    work states the semiclassical calculus and its sharp Gårding inequality, the fix is an Appendix A quotation
    plus a real proof of prop:np-10-65-a: about a day.
  - If not, the one Gårding step (33:1458) must be replaced by a positivity argument that does without it, as
    ch. 23 does for e3b, and the remaining calculus facts quoted. That is a section-sized proof project.
- **Already reported?** No: neither FRI nor INT mentions [Hin23d], prop:np-10-65-a, the 3b-calculus or sharp
  Gårding.

### G2. [Hin26a, Lemma 5.14] and [Hin26a, Corollary 5.15] are "used as stated", from a preprint, unquoted, with notation undefined

- **Where:**
  - 33:1687–1688: "[Hin26a, Lemma 5.14] is stated for an arbitrary time-oriented Lorentzian vector space, and
    [Hin26a, Corollary 5.15] on ℝ^(1+n) for every n and on n-dimensional manifolds of bounded geometry … Both are
    used as stated, with n = 4."
  - Proof of prop:iv5-6-1 (33:1695 ff.), at 33:1728–1734: "The principal symbol of 𝒞 is aT_(G,da,ℓ) − a²E in the
    notation of [Hin26a, (5.61)] …", then "[Hin26a, Corollary 5.15] is integrated over … twice".
  - Again at 33:2160, in the transition-face energy estimate: "[Hin26a, Lemma 5.14 and Corollary 5.15], stated in
    every dimension".
- **What is assumed.** The positivity of the quadratic form T_(G,η,ℓ) for past timelike η, when ℓ is positive
  definite on future causal covectors; and its integrated form, an energy inequality with δ-weighted boundary
  terms on bounded-geometry manifolds. T_(G,·,ℓ) is never defined in the edition (grep finds it only at 33:1728
  and 1731), so the proof cannot be checked without the preprint.
- **Depends on it:** prop:iv5-6-1, which is [Hin26a, (5.66)–(5.69)]; then thm:iv5-7-3 and thm:iv6-2-1. From there
  the route is as in G1: **thm:iii-e-1-1, thm:settling, thm:own-data**.
- **Size: small.** Define T (Hintz's (5.61)), state and prove Lemma 5.14 (pointwise linear algebra on one fibre),
  and prove Corollary 5.15 by integrating the divergence identity with the two δ-weights. About 1–3 pages.
  Quoting [Hin26a] in Appendix A would not satisfy the requirement of a *published* source.
- **Already reported?** No.

### G3. thm:own-data (3): "the maximal vacuum development" of data on a surface with an inner boundary, asserted without definition or citation

- **Where:**
  - 63-own-data.md:58, the statement: "(3) the maximal vacuum development ĝ of (γ, k) settles to a Tangherlini
    metric …".
  - 63:1908–1912, the proof: "this development embeds in the maximal vacuum development of (γ, k), which therefore
    settles in the same sense."
- **What is assumed:**
  - (a) That a maximal globally hyperbolic vacuum development of (γ, k) exists. "Maximal vacuum development"
    occurs nowhere else in the paper. Appendix A's [Sbi15] entry (95:307) quotes Theorems 2.6, 2.7, 3.4 and
    3.13 and the proof of 2.7, but not an existence theorem for a maximal development.
  - (b) That the development given by thm:own-half-settling, on Ω_* ∪ 𝒟, is a globally hyperbolic development of
    (γ, k) in Sbierski's sense, with the initial surface a Cauchy surface. This is not shown at that step.
  - (c) That the notion applies at all. Σ^IVP = t_IVP⁻¹(0) carries data only down to its inner boundary
    {|x| = r_♭} (thm:iii-k-4-3, 46:1658; 30:863). Sbierski's initial data are given on a manifold without
    boundary.
  - Ch. 62 handles the same issue correctly for lem:interior-one-spacetime, by working with the open
    Σ = {r_♭ < |x| < R} and checking acausality (62:307–323). Ch. 63 does not.
- **Depends on it:** item (3) of **thm:own-data** as worded. Items (1) and (2) do not depend on it, and the
  settling of *a* G-invariant development is proved.
- **Size:**
  - Trivial if (3) is reworded to "a G-invariant vacuum development of (γ, k) settles …", the form of
    thm:settling (i).
  - About 1–2 pages if the maximal development is kept: use the interior Σ^IVP°, quote Sbierski's main existence
    theorem, and prove global hyperbolicity of the development's interior. The time function t_*/t_IVP and the
    spacelike inner boundary, along which r decreases to the future, give the argument; ch. 62:301–323 is the
    template.
- **Already reported?** No.

### G4. Ch. 33 §§iv5–iv6: further steps adapted from preprint displays rather than written out (outline-level)

- **Where.**
  1. 33:2075 (proof of prop:iv6-1-1): "real principal type propagation applies along Char_σ, which flows from R_in
     to R_out by [Hin26a, (B.16)]". The flow statement is taken from the 3 + 1 preprint.
  2. 33:2088–2089: "*Uniformity* in σ near ±1 is the limiting absorption principle: the full Hamilton field on the
     cut-offs keeps the sign structure of [Hin26a, (B.23)] ([Hin26a, p. 91])".
  3. 33:1055–1057 (lem:iv4-1-2): "the differences enter S̃, Q, R and P^C_b as in the proof of [Hin26a, (6.4)], by
     the same counting".
  4. 33:1035–1043 and 33:1296–1309 (lem:iv4-1-1, lem:iv5-0-4): "[Hin26a, Lemmas 3.3–3.8] hold in dimension 4 + 1
     verbatim". The three facts behind them are proved in prop:np-10-13 (i) for any dimension D. [Hin26a,
     Lemma 3.5] (used at 33:1380, 1691, 1742) and Corollary 3.6 are never stated in the edition, though they do
     follow from prop:np-10-13 (i) with compactness.
- **What is assumed.** Dimension-free computations of the 3 + 1 source: the sc-Hamilton flow of the model,
  commutant symbols, and error counting at infinity. The dimension-dependent quantities (density, weights, shifts
  of S̄) are recomputed in the edition; the remaining steps are taken by reference.
- **Depends on it:** prop:iv6-1-1, hence thm:iv6-2-1 and thm:iii-e-1-1 (4), and **thm:settling**; and
  lem:iv4-1-2, lem:iv5-0-4 inside the G1/G2 chain.
- **Size: small to moderate.** State Lemma 3.5 and Corollary 3.6 as corollaries of prop:np-10-13 (half a page).
  Write out the model's flow, the (B.23) symbol and the error count in 4 + 1 (a few pages, routine).
- **Already reported?** No. Ch. 33 is CONFIRMED in STATUS; these are dependencies on the source that were
  accepted there.

### G5. The scattering calculus is used "as black boxes" from unrefereed lecture notes [HJS]

- **Where:**
  - 20-s01-spectral-bounded.md:189: "The following statements of [HJS] are used as black boxes."
  - Appendix A, thm:std-hjs-calculus (95:783), cites [HJS], listed in ch. 98:90 as "lecture notes (2026)".
- **What is assumed.** Composition, parametrices, duality, boundedness, compactness, microlocality, symbols and
  adjoints of Ψ_sc. These are classical and quoted correctly, but the source is not a published one.
- **Depends on it:** ch. 20–22 (spectral theory) and the sc-analysis of ch. 33 §iv6, hence all of the stability
  theory and **thm:settling**.
- **Size: small.** Re-source each quoted item to published literature (Melrose's scattering calculus; [Vas18],
  already in the bibliography). Ranked last because the mathematics is standard and quoted; this is a sourcing
  gap, not a missing argument.
- **Already reported?** No (one review in `notes/` mentions [HJS] in passing).

Minor items, not gaps: Appendix A's thm:std-hin26a-cform (95:286) is cited by no chapter. [AN00, Theorem 3.1]
(35:1340) and [Hin17, Proposition 4.1] (proved anyway as prop:np-10-17-i, 32:445) are cited with page numbers
but are not in Appendix A, against its own policy (95:3).

---

## 2. Conditional statements: hypothesis carried openly in the statement

| # | file:line | quote | hypothesis | non-vacuous? | used by / feeds | in FRI / INT? |
|---|---|---|---|---|---|---|
| C1 | 87-ten-l5.md:1153 (lem:tl5-continuation) | "Suppose moreover that the characteristic initial value problem … has … (F1)–(F3)" | smooth data; (H1)–(H3); (F1)–(F3) local existence, uniqueness and continuation in the gauge | (H1)–(H3) established for no v* > 1/2 (rem:tl5-beyond, 87:1229–1238); the data are only C³ | **no proof uses it**: grep finds only prose at 87:18, 595, 1229–1233 and 90:219 | FRI lines 43–47, 65–69; INT 1222 |
| C2 | 87:579, 591–593 (thm:ten-l5 (c)) | "for every solution on a set D … whose transverse derivative ∂_vR on C₀ is the seed's" | existence of a solution on D, and the seed's ∂_vR on C₀ | vacuous beyond the seed region unless a solution exists there; no existence claimed for v > 1/2 (87:595) | stands alone; (b) proves existence only where the solution is the seed | INT records the M1 repair (generator-segment hypotheses) |
| C3 | 81-class-system.md:1625–1628 (cor:class-two-dust); 82-vlasov.md:2122 (setting of prop:vlasov-radial-background, 82:2161); 82:2321–2323 (cor:vlasov-two-dust) | "assume that the outgoing packet does not reach the inner sphere: {u1 ≤ u ≤ u2} ∩ Ω₂ ∩ {R = a} = ∅" | the packet stays off R = a on Ω₂ | **not shown for any background**: "a property of the background that [[prop:two-dust-background]] does not decide" (81:1659); only the unused numerical observation rem:two-dust-example (80:431–445) suggests it; ch. 83's proved background facts (thm:bg-margins) cover only R ≤ R_*, before the shell | the two corollaries; ch. 03:363–365 summarises cor:vlasov-two-dust **without** the hypothesis (03:326 says each result "is stated in full where it is proved"; ch. 90:173–176 states it) | INT 923, 1036, 1051 (made a hypothesis); not in FRI |
| C4 | 81:1009 (cor:class-seed-families), 81:1019 | "It assumes the data. They are not constructed here" | existence of small non-round dust data on the seed | non-trivial data not constructed (ch. 90:176–177 says so) | stands alone | ch. 90 only |
| C5 | 82:256–283 (thm:vlasov) | "We assume: (Ω) … (V1) … (V2) … (V3)" | hypotheses on the field | yes: prop:vlasov-nonempty (82:1710) and lem:vlasov-open | the theorem | – |
| C6 | 85-equality-edge.md:46 (def:edge-hypotheses: (H_N), (H_D), (H_t), (H_*), (B_J)), used with (B_(c′)) at 85:367, 912, 1243 | "These are properties of env near v_s alone" | regularity of env at the edge | yes: cor:edge-envelope (85:1510) proves them for env_C and exp(−a/(v − v_s)) | thm:very-edge, thm:l-24 | INT 1138 (decision) |
| C7 | 03:276–292 (thm:settling hypotheses: ε_K with (G), (G⁺), ε_K < ε_Υ; γ_Υ, e_Υ, h below proved thresholds; K = d_1 + 14) | "let ε_K be the decay parameter chosen in that theory" | gap conditions on a discrete set Λ, and parameters below existence-only thresholds | satisfiable by the proofs (Λ discrete and fixed first); whether (1/100, 1/100, 10⁻⁶) is admissible is undecided (rem:ec-point-outside, 71:49–57), which matters only for ch. 71 | thm:settling | FRI 33–37, 80–85 (ε_K at the computational point) |
| C8 | 03:10–12, 49–58 (thm:main, rem:envelope-regularity) | "An envelope of finite smoothness is not covered" | env ∈ C_c^∞ | yes: env_C | thm:main; the C³ profile sin⁴ is covered for no K ≥ 6 (proved: Step 4 takes 8 derivatives of env) | FRI 43–45 |
| C9 | 83:1322 | "Seeds in the radical of Q are not treated." | scope restriction after the proof of thm:loc-inside | – | – | – |

Losses named openly (weakened statements, honest; not gaps):

- cor:layer: whether the domain of prop:eq-domain is needed in place of D_T is not shown (90:35).
- lem:interior-one-spacetime: how far the identification reaches is left open (62:13, 330–332); no proof of
  thm:settling uses it (rem:vii-4-1).
- thm:rw-settling (c): whether the spherical gauge part decays faster is not determined (64:420).
- thm:harmonic-rate: the ℐ⁺ expansion is "not carried" and (iii) states the plain weight (65:1145).
- rem:own-low-weight: existence is not attempted at a_0 ≤ 1/2 (63:1827).
- ch. 83 (c): radial localisation inside the lens is dropped (FRI 97–99).

---

## 3. "In dimension 4 + 1" adaptations sampled, and their status

**How the sample was chosen.**

- **(i) Deterministic sample.** A script took, in each file 20–48, the *first* theorem-level statement (Theorem,
  Lemma, Proposition or Corollary) whose header attributes it to a source "in dimension 4 + 1". Where a chapter
  has none in a header, it took the first sentence "This is [Hin…] in dimension 4 + 1" and the statement before
  it. It then checked whether a `*Proof*` follows inside the block, or a "proof is in" pointer, and followed any
  pointer to the proof.
- **(ii) Targeted sample.** Every "verbatim", "as stated", "free of the dimension", "in every dimension" and
  "same proof" adaptation found by grep in ch. 20–48 was read, about 25 sites. The sources of G1, G2 and G4 came
  out of this pass.

In all, 28 statements came from (i) and 8 sites from (ii). There are 517 occurrences of "in dimension 4 + 1" in
total.

| file:line | statement | source | status |
|---|---|---|---|
| 20:302 | lem:i-a-2-4 | [Hin26c, Lemma 5.12] | proved in full (Jordan form, partition of unity) |
| 21:192 | thm:i-b-1-3 | [Hin26c, Theorem 9.16] | proved, 21:1866–1930 |
| 22:600 | thm:i-c-4-3 | [Hin26c, Theorem 9.38] | proved, sec:i-c-4-4; (9.115) not proved and not used (22:606, 1422) |
| 23:615 | lem:ii-a-5-1 | [Hin26c] | proved |
| 24:850 | lem:ii-c-2-5 | [Hin23c, Proposition B.1] | proved |
| 25:131 | thm:ii-d-1-2 | [Hin26c, Proposition 7.1] | proved, sec:ii-d-5 (25:1034) |
| 26:92 | lem:ii-e-1-1 | [Hin26c] | proved |
| 27:139 | lem:ii-f-1-2 | [Hin26c] | proved |
| 28:76 | lem:ii-f-6-1 | [Hin26c, (10.47)] | proved |
| 29:972 | lem:ii-g1-4-1 | [Hin26c] | proved |
| 30:184 | lem:iii-a1-1-5 | [Hin26] | proved |
| 32:81 | lem:iii-d-2-1 | [Hin26] | proved |
| 33:54 | thm:iii-e-1-1 | [Hin26, §7], [Hin26a] | proved via thm:iv4-2-1 (33:2269) and thm:iv6-4-1 (33:2340), **subject to G1, G2, G4** |
| 33:1096 | lem:iv4-1-4 | [Hin26a, Proposition 5.1] | proved from prop:np-10-14 (conditions restated in 4 + 1) |
| 33:1035 | lem:iv4-1-1 | [Hin26a, Lemmas 3.3–3.8] "verbatim" | justified by prop:np-10-13 (i); statements not printed (G4) |
| 33:1221 | prop:np-10-65-a | [Hin23d], [Hin26a, §2.3], [Hin26d] | **asserted only** (G1) |
| 33:1695 | prop:iv5-6-1 | [Hin26a, Proposition 5.16] | proof uses [Hin26a, Lemma 5.14 and Corollary 5.15] as stated and undefined notation (G2) |
| 33:2042 | prop:iv6-1-1 | [Hin26a, Proposition B.2] | outline: dimension-dependent shifts computed; flow and uniformity by reference (G4) |
| 34:98 | lem:iii-f-2-1 | [Hin26] | proved |
| 35:362 | prop:iii-g-2-4 | [Hin26] | proved |
| 36:285 | lem:iii-c-3-5 | [Hin26] | proved |
| 37:334 | prop:iii-h-3-2 | [Hin26] | proved |
| 38:140 | lem:iii-i-2-2 | [Hin26] | proved |
| 39:190 | lem:iii-i3-1-2 | [Hin26] | proved |
| 40:271 | lem:iii-i7-2-2 | [Hin26] | proved |
| 41:951 | thm:iii-i11-4-1 | [Hin26] | proved (98-line block) |
| 42:377 | thm:iii-i14-3-1 | [Hin26] | proved (154-line block) |
| 43:465 | prop:iii-j2-4-3 | [Hin26] | proved |
| 45:80 | lem:iii-c1-1-1 | [Hin23a], [Hin26] | proved; ch. 45 writes [Hin23a, §3] out in 4 + 1 |
| 45:1835 | prop:iii-c2-4-1 | [Hin26, Proposition 5.25] | proved in full ("we follow [Hin26]", with the computation) |
| 46:1658 | thm:iii-k-4-3 | [Hin26, Theorem 13.1] | proved |
| 47:587 | thm:v-3-1 | [CD03, Theorem 8.1] in space dimension 4 | proved; the missing Proposition F.1 equivalent is prop:v-2-3 (47:196); [CD03] results "hold for every n ≥ 2" (47:302) |
| 48:249 | thm:viii-2-2 | [Hin26] | proved |

**Verdict.** Every sampled theorem-level adaptation outside ch. 33 §§iv5–iv6 is proved in the paper, not merely
asserted. The exceptions are the ch. 33 sites in the table (prop:np-10-65-a, prop:iv5-6-1, prop:iv6-1-1,
lem:iv4-1-1/lem:iv5-0-4, lem:iv4-1-2), which make up G1, G2 and G4. Other "same proof" sites read in pass (ii)
supply the argument or point to one in the edition: 24:1141, 1175; 25:195; 26:511, 696, 1433; 27:1488; 31:1079;
32:1151, 1699–1802; 33:1257 (Christoffel classes, (2.13)–(2.14)); 40:235, 894; 41:116; 42:175; 43:347; 46:173,
605, 837, 1185.

---

## 4. Values not evaluated on which a statement depends

None of these is a gap in proof: each statement is existential. They are listed because the statement *refers to*
the value.

- **V1. d_1, the regularity of thm:iii-k-4-3.**
  - thm:settling fixes the approximant's order as K = d_1 + 14 (03:289).
  - thm:own-data takes k1 = max(8, d_1 + 4) and K > max(d_1 + 14, K*(a, M, k1)), with K* from lem:own-e-flux
    (63:44–45).
  - d_1 and K* are not evaluated. Ch. 71 bounds the Nash–Moser loss d (1.2497·10²⁴ < d < 1.57157·10⁵⁰), but only
    at a point outside the proved set (rem:ec-point-outside). So the order K that these theorems require is not a
    known number.
- **V2. ε_K, the decay improvement in thm:settling.** thm:settling's rate is t*^(−2−ε) with ε < ε_K, and ε_K is not
  evaluated on the proved set. At the computational point, (G) forces ε_K < 1.6417·10⁻¹⁴ (cor:uc-two-offsets,
  71:2079; FRI 80–85).
- **V3. The thresholds λ0, C, λ_H, λ_P, λ1, δ, λ_2, λ_L and those of thm:very-edge and thm:l-24.** None is
  evaluated. Only upper bounds are proved: prop:lambda0 (λ0 < 0.0024433), prop:ec-delta-cap
  (λ1 < δ ≤ 2^(−(32d+9))), and λ_L ≤ 10^(−430) for env_C. No statement depends on their values.
- **V4. The parameter thresholds for (γ_Υ, e_Υ) and h_*.** These have existence only. Whether (1/100, 1/100) lies
  below them is undecided (71:52, 70:1696). This affects only ch. 71's numbers, which no theorem outside ch. 71
  uses (90:76–80).
- **V5. The number of derivatives of env used for a fixed K** "is not determined" (03:51). It decides which
  finite-smoothness envelopes would be covered. thm:main assumes C_c^∞, so no statement depends on the number,
  and the negative claim about the C³ profile is proved.
- **V6. M_22.** A numerical observation, unused (rem:m22-value).

---

## 5. Checked and not gaps

- **Ch. 22 statements of [Hin26c], declared not proved and not used** (22:606, 683, 1317–1318, 1422): (9.115);
  the improvements of Remark 9.37; a smallness independent of k; uniformity in α; (9.120) for augmented
  operators. Spot check: thm:i-c-6-4 (5) is used at single weights only (29:1227, 66:1007).
- **Other source statements not proved and not used:**
  - [Hin26c, Remark 7.3] (25:153);
  - [Hin26c, Theorem 11.1] (a) and (b), where (b) is replaced by thm:iii-h2-3-1 and thm:iii-h2-4-1 (28:933–945,
    38:1146–1147);
  - [Hin26, Theorem 5.23 (1)] without the constraints (45:1790);
  - the "w−"-weight statements of ch. 43 (43:99, 1108);
  - uniqueness at rotating b (44:482).
  The text checks that every use avoids each of these.
- **Hypotheses verified downstream:**
  - (H5)–(H8) of ch. 20–21 (21:1963, verified in ch. 31 and per operator);
  - (Dyn), (C1)–(C3) (35:1421, 35:53);
  - ℵ-admissibility (28:945 → thm:iii-h2-3-1);
  - 2 + ℰ_ind ⊂ ℰ_+ (39:612, 40:146), a choice of ℰ_+;
  - (Fin) (47:376 → 47:600, 83:772);
  - the [CD03, Proposition 5.10] smallness, a hypothesis of lem:s28-setting (b), checked for compact support
    (47:458).
- **Main-chain citations (ch. 02–10):**
  - [Tou23a/b] are comparisons (02:234, 05:44, 06:10, 07:89–96), and the commutator identity is proved exactly in
    4 + 1 (02:215–235).
  - [TTS09]: the Bondi law is derived anew, "nothing … taken from [TTS09] except the comparison" (10:5–6).
  - [DS23] (torus) and [AO14] are applied after extension and a change of coordinates, with every hypothesis
    checked (06:260–440).
  - [CBCM10], [BGP], [SY21], [LY22], [BH17], [GO13] and [KP88] are quoted with hypotheses and dimension n.
- **Dimension coverage of quoted sources:** [KI03] and [HKW18] (any n; [HKW18] decay "in spacetime dimension six
  and below"); [Sbi15] (any d ≥ 1); [CD03] (n ≥ 2); [Rac16] (general n); [CTG23] ("in higher dimension", title,
  98:39).
- **Numerical observations.** None of the 44 is cited inside a proof (script check). Proofs that use computation
  are exact or interval-certified, with printed tables (Appendix B). No proof rests on an unprinted computation:
  the grep for numerical, quadrature or certified inside proofs found only analytic uses.
- **"Should", "expected", "heuristic":** rem:gd-r4-bounds (65:933) is a labelled heuristic about the method that no
  proof uses; 64:659 quotes [HKW18]; 87:1193 quotes [CP12]. Nothing else.
- **The half-integer class** (rem:half-class-changes, 62:571–580): the question it leaves open is settled by
  prop:own-same-index-sets and thm:own-half-settling (63:186–281).
- **ch. 24's [Hin21, Theorem 2.6] and [Hin23c, Lemma 5.8]:** replaced by proofs (thm:ii-c1-1-1; 24:1155–1165,
  1730–1742).

---

## 6. Cross-reference: the chapter 83 gap and the chapter 87 continuation lemma (for the other agent; not scoped here)

- **Chapter 83.**
  - The dust case: 83-localised-data.md:597–600: "For cone data that carry dust … no development is asserted here:
    [[prop:loc-cones]] gives the cone data only, and no result of this paper uses their development."
    prop:loc-cones (83:572) constructs the cone data. The development of dust cone data would need a characteristic
    initial value theorem for five-dimensional Einstein–null dust, which no published theorem covers (FRI 97–99,
    P-K83c; INT 1256).
  - The vacuum case (83:593–597) is covered by [CTG23, Theorem 1.1], a preprint, in prose only, with no theorem
    resting on it.
  - Related loss: localisation (c) drops radial localisation inside the lens (FRI 99).
  - No stated result depends on the missing development.
- **Chapter 87, lem:tl5-continuation** (87:1153–1227). Its hypotheses are:
  - smooth T²-invariant characteristic data on N₀ ∪ N₁;
  - (H1) an a priori bound y_s ≤ A + B y_s²; (H2) uniform C^k bounds under y ≤ 2A; (H3) 4AB < 1 and y_(1/2) ≤ A;
  - (F1) local existence, (F2) uniqueness and (F3) continuation of the characteristic problem in the gauge. These
    rest on three facts the paper does not establish (87:1181–1196): extension of the T² action and both
    reflections to the development, existence of the double-null gauge on a region D_(s′), and uniqueness up to
    isometry of the development of characteristic data, which [CP12, §4.3, p. 16] and [CCTW16, p. 55] call open.

  The data of def:tl5-problem are only C³, and (H1)–(H3) hold for no v* > 1/2 (rem:tl5-beyond). **The lemma is
  used by no proof** (grep: 87:18, 87:595, 87:1229–1233, 90:219, all prose). Also open beyond v = 1/2: the shift
  constraint Ric_vx = 0 on N (def:tl5-problem, 87:572).
  Recorded at FRI 43–47 and 65–69, and INT 1222.
