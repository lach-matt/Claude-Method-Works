# R-DINT-a: the integration round D-INT-1, and a first reading of chapter 90

Reader: R-DINT-a (independent; changed nothing). Tree read at HEAD 74074c98 (D-INT-2 merged the d-bound proofs into
chapter 71; chapters 00, 01, 03, 23, 25, 43, 46 and 90 are as D-INT-1 left them at 772f67f7). Read: READER-BRIEF,
STYLE, OUTLINE, WRITER-BRIEF; notes/reports/D-INT-1.md, W-90.md, I-2.md; notes/reviews/R-DB-2.md sections 1, 5–7 and
R2-DB-a (A2, O1); the D-INT-1 diff (scratch/d_int_1/d_int_1.diff); texts 7–12 as they stood at 772f67f7 in the old
forward proof; chapter 71 at every result cited by the eight chapters (def:ec-point, rem:ec-point-outside,
prop:ec-rounds, thm:loss-d, prop:ec-delta-cap, sec:fwd with thm:fwd-loss, lem:fwd-orders, prop:fwd-calculus,
lem:uc-two-offsets, cor:uc-two-offsets, rem:uc-offset-d0, thm:uc-reduction, def:uc-choice, lem:uc-phi-loss,
prop:uc-dbg, thm:uc-integer, sec:cs intro, def:cs-choices, rem:ec-linear-observed, rem:ec-not-evaluated); chapter 29
(thm:ii-g-2-1, lem:ii-g-4-1); every result chapter 90 cites (all 104 keys, in chapters 01–03, 08, 10, 48, 60–66, 70,
71, 80–87). Checks: `python3 lint.py --chapters` 0 hits (62 files, 4573 labels); `python3 assemble.py --check`
0 problems; every line of the eight chapters ≤ 121 characters (counted in characters); no wrapped line starts with
"+ ", "- ", "* ", "> ", "#", "=" or "|" (the only such lines are list items and the block quote of 01:25–35).
Private comparison scripts in scratch/r_dint_a/.

## Verdicts

- **A (D-INT-1): NOT CONFIRMED — 1 Major, 2 minor, 1 nit.**
- **Chapter 90: NOT CONFIRMED — 0 Major, 2 minor, 5 nits.**

## A. The integration round D-INT-1

### What was checked and holds

- **Verbatim placements.** CH-43 (lem:iii-j2-2-4, 43:303–327), CH-46 (a)–(c) (46:1247–1249, 1288–1295, 1469–1473),
  CH-3 (03:351–356) and CH-90 (a) (90:56) are R-DB-2's texts word for word (whitespace-normalised comparison). Texts 7
  (23:1466–1471), 8 (25:29–30) and 12 (23:1071–1072) are the old forward proof's texts word for word; no placement
  comment is left in 23, 25 or 71. CH-90 (b) (90:60–68) is R-DB-2's text with exactly one departure, the one the report
  states.
- **The departure in chapter 90** ("and N_NM > 2.624 × 10²⁵ at every admissible choice of the weights"): accepted. It
  is cor:uc-two-offsets (a) as stated (71:2056–2061: "For every admissible choice of the weights … d_NM ≥ d_acc >
  1.2497·10²⁴ and N_NM = 21d_NM + 6 > 2.624·10²⁵"), whose hypothesis holds for the index sets as constructed by (b);
  21 · 1.2497·10²⁴ = 2.62437·10²⁵. It makes the "every"/"one" contrast with thm:uc-integer explicit and states no more.
- **Chapter 90's d paragraph against chapter 71.** λ1 < δ ≤ 2^(−(32d+9)), modulus at 2δ ≤ 2^(−(32d+8)) (prop:ec-delta-cap);
  d_acc composed of closed-form losses, the forward loss ≤ 20,180 and step counts (thm:loss-d (i)); d > 1.403·10²⁰,
  N_NM > 2.946·10²¹, log₁₀ δ < −1.351·10²¹ (thm:loss-d (ii), prop:ec-delta-cap); d ≤ D_NM < 1.57157·10⁵⁰ and
  21D_NM + 6 < 3.30029·10⁵¹ (thm:uc-integer; integers re-multiplied exactly); the point outside the proved set
  (rem:ec-point-outside). All true and cited to the right keys.
- **lem:iii-j2-2-4 with loss 3.** The proof is right in place: lem:ii-g-4-1 (2) at d = 3 (> 5/2 on the manifold,
  > 4/2 on faces), the factor at k + 3 chosen, d_1 ≥ 3 and monotone norms give both orders of the factors; the
  polynomial part by iterating (2) (‖u^(m+1)‖_k ≤ C‖u‖_(k+3)‖u‖_3^m by induction), the remainder by (3). Every citing
  use absorbs the loss: 43:188 (lem:iii-j2-2-1 (b), d free; the loss can be put on the coefficient), 43:462
  (prop:iii-j2-4-3, d free), 43:1077 (cor:iii-j3-6-6, fixed losses), 44:671 (names the range), 46:1291 (the proof of (d)),
  71:2227 (lem:uc-phi-loss, which counts the 3 explicitly: d_FM, d_Ψ ≤ d_Φ + 8); prop:uc-dbg (71:2142–2178) uses
  lem:ii-g-4-1 at d = 3 directly and is consistent. But see A1 for two passages of chapter 46 that use the lossy
  products without citing the lemma.
- **lem:iii-k-2-2 (d) and prop:ec-delta-cap.** (d) and its proof are right: ‖h_0‖_(H^5) ≤ ω_3(…) small once the data
  norm of order 3 + k′_3 is ≤ s_P ≤ s_3; the order 3 + k′_3 is dominated by k + 3 + k′_(k+3) as k′ is non-decreasing; the
  order k + 3 of prop:iii-k-1-2 (3) gives ‖h_0‖_(H^(k+5)). prop:ec-delta-cap's ω̃ := ω_(2d+3), s̃ := min(s_(2d+3), s_P)
  and C_(2d) are exactly the modulus, threshold and constant of (d) at k = 2d; the 2d-part of the Smallness paragraph
  (2d + 3 + k′_(2d+3) ≤ N_NM + k″ ≤ d_1) holds. 48:240 still means prop:iii-k-1-2 (3)'s k′_k and is lossless (a
  commutator with a smooth cut-off), as D-INT-1 says.
- **Texts 7, 8, 12 against chapter 71.** Text 7: M = 200Θ + 98 is prop:fwd-calculus's M + 2 = 200T + 100; (d)'s M + 1
  covers 34T + 32; (e) with N ≤ Θ and six quantizations, (f) with μ in [−6Θ − 3, 6Θ + 3], and "(e) without the commutator
  expansion" are prop:fwd-calculus (e), (f) and the end of its proof of (e). Text 12: d_0 = 200Θ + 100 for (a) when 𝗌 has
  values in [−Θ, Θ], and for (b) when 𝗌_0 does and sup 𝗌 − inf 𝗌_0 ≤ Θ, as prop:fwd-calculus states (the proof of
  (b) as the case r = 3 of (e)). Text 8: N′ ≥ −inf 𝗌_0 is what the a priori terms need; 13 = −inf 𝗌_0 of lem:fwd-orders
  and the N := 13 after it. See A3 for the citation that Text 8 lacks.
- **Chapter 25's ℋ.** 48 sites, all ℋ (U+210B), none of 𝓗 (U+1D4D7) left anywhere in chapters/. Every site is the
  horizon: ∂R_(ℋ⁺) (def:ii-b-4-1), ℋ⁺ ∩ K⁺, ϑ_ℋ (eq:i-a-1-5, chapter 20:159–163), R_ℋ (prop:ii-b-8-1, 24:582), V_ℋ,
  𝒳_ℋ. Chapter 25 has no Hilbert space ℋ.
- **23:361.** "compact set I ⊂ ℝ" renders the source's I ⋐ ℝ correctly; the statement is quoted as unused.
- **Chapter 3's bullet** (03:351–356): true. Lower bounds at the point (thm:loss-d), upper bounds for d and N_NM at one
  admissible choice (thm:uc-integer), and through the lower bounds explicit upper bounds for δ and the modulus
  (prop:ec-delta-cap; δ ≤ 2^(−(32d+9)) holds for every d, the numbers come from the lower bounds).

### Findings

**A1 (Major) — 46:1251–1255, 46:1466–1469 (and 46:1334–1341): the Smallness paragraph's data dependence is not what
the loss-3 products give.**
Evidence. 46:1466–1468: "The constants C_k (k ≤ N_NM), C_1, C_2 and δ depend on the data only through
‖(γ̃, k̃)‖_(H^(N_NM+k″)) …; they are bounded independently of the data once that norm is at most s_♭, the threshold of
prop:iii-k-1-2 (3) at the orders k ≤ N_NM", with k″ := k′_(N_NM) and s_♭ := min_(k≤N_NM) s_k (46:1252–1253). The C_k
are those of eq:ii-g-2-3 for U ↦ P_5(Ψ(U)), and at U = 0 that hypothesis gives C_k ≥ ‖P_5(Ψ(0))‖_(ℱ^k_ex) for d ≤ k ≤
N_NM; thm:ii-g-2-1's ε depends on C_k for k ≤ N_NM (29:78–79). The corrected (d) bounds ‖P_5(Ψ(0))‖_(ℱ^k_ex) only by
C_kω_(k+3)(‖(γ̃, k̃)‖_(H^(k+3+k′_(k+3)))), and only when that norm is ≤ min(s_(k+3), s_P). At k = N_NM this is a norm of
order N_NM + 3 + k′_(N_NM+3) > N_NM + k′_(N_NM) = N_NM + k″ (k′ non-decreasing), under thresholds s_(N_NM+3) and s_P that
s_♭ does not contain. The same loss enters (c) and the e_S, e_(S⁰) bound (46:1334–1341), which the first sentence cites:
the coefficients of D_hP_5(Ψ(U)) and of P_5(Ψ(U)) − P_5(Φ(U)) carry h_(−S,−S⁰) and its derivatives to order 2, and a
product of such a coefficient with ∂_S H (or with h̃) is bounded by lem:ii-g-4-1 (2)–(3), which put one factor at the
order k + 3; with both factors built from h_(−S,−S⁰) this needs ‖h‖_(H^(k+5)), that is ω_(k+3) of the norm of order
k + 3 + k′_(k+3), not the ω_k of the display. R-DB-2 (section 5) replaced only the "(a Moser bound)" of (d) and the 2d
line of the Smallness paragraph; the first sentence and the definitions of k″, s_♭, ω_♭ still assume lossless
composition. So "bounded independently of the data once ‖(γ̃, k̃)‖_(H^(N_NM+k″)) ≤ s_♭" is not proved, and with it the
uniformity of ε_NM for data small in H^(d_1), d_1 = max(d_0, N_NM + k″). The conclusion survives with a larger d_1;
d_1 is symbolic everywhere downstream (thm:iii-k-4-3, thm:settling's K = d_1 + 14, rem:half-class-changes), so only
chapter 46 changes. prop:ec-delta-cap is unaffected (it uses k = 2d only).
Fix. 46:1252–1255, replace "k″ := max_(k≤N_NM) k′_k = k′_(N_NM),
s_♭ := min_(k≤N_NM) s_k and ω_♭ := max_(k≤N_NM) ω_k on [0, s_♭]. The smallness constants use orders k ≤ N_NM only; a
bound needed at every order k (the bound on e_S and e_(S⁰) in the proof of [[lem:iii-k-2-3]], which feeds
[[eq:ii-g-2-4]]) carries k′_k and ω_k." by

    k″ := k′_(N_NM+3) + 3, s_♭ := min(min_(k≤N_NM+3) s_k, s_P) and ω_♭ := max_(k≤N_NM+3) ω_k on [0, s_♭]. The
    smallness constants use orders k ≤ N_NM only, and so, since a product or a composition bounded by [[lem:ii-g-4-1]]
    (2)–(3) takes one factor at the order k + 3, the initial family at the orders k ≤ N_NM + 3, as in (d); a bound needed
    at every order k (the bound on e_S and e_(S⁰) in the proof of [[lem:iii-k-2-3]], which feeds [[eq:ii-g-2-4]]) carries
    k′_(k+3) and ω_(k+3).

46:1336–1340 (the e_S display and the sentence after it): ω_k(‖(γ̃, k̃)‖_(H^(k+k′_k))) → ω_(k+3)(‖(γ̃, k̃)‖_(H^(k+3+k′_(k+3))))
(twice), and "when ‖(γ̃, k̃)‖_(H^(k+k′_k)) ≤ s_k" → "when ‖(γ̃, k̃)‖_(H^(k+3+k′_(k+3))) ≤ min(s_(k+3), s_P)"; "by
[[prop:iii-k-1-2]] (3) and the tame bounds of [[sec:iii-j2-1]]" → "by [[prop:iii-k-1-2]] (3) at the order k + 3 and the
tame bounds of [[sec:iii-j2-1]], with [[lem:ii-g-4-1]] (2)–(3) for the products of the coefficients, which carry
h_(−S,−S⁰), with ∂_S H, ∂_(S⁰) H and h̃"; "in every H^(k+2)" stays. 46:1467–1468, replace "the threshold of
[[prop:iii-k-1-2]] (3) at the orders k ≤ N_NM." by "the threshold of [[prop:iii-k-1-2]] (3) at the orders k ≤ N_NM + 3
and of [[lem:iii-k-2-2]] (d); in particular C_k ≥ ‖P_5(Ψ(0))‖_(ℱ^k_ex), which (d) bounds for k ≤ N_NM through the norm
of order k + 3 + k′_(k+3) ≤ N_NM + k″." The 2d line (46:1469–1473) then holds as written. (The writer of chapter 46's
fix round should re-derive the e_S display before placing it; the dependence above is the least the lossy lemmas give.)

**A2 (minor) — 01:151–153: the lower bound at every admissible choice drops "for the index sets as the proofs construct
them".**
Evidence. "there d > 1.2497 × 10²⁴ at every admissible choice of the weights, and d < 1.57157 × 10⁵⁰ at one
([[thm:uc-integer]])". The bound 1.2497·10²⁴ is cor:uc-two-offsets (a) under the hypothesis 𝔡₀, 𝔡₁ ∈ π_1(ℰ_ind ∪
ℰ^ι_ind), which holds "for ℰ_ind as the proof of prop:iii-d2-3-1 constructs it" ((b)); thm:uc-integer states it "with
the index sets as constructed" (71:2447); rem:uc-offset-d0 (71:2079–2091) leaves open whether a smaller admissible
ℰ_ind exists, and for any admissible index sets chapter 71 proves only d > 1.403·10²⁰ (thm:loss-d (ii)). Chapter 71's
opening (71:18–19) and chapter 90 (90:65) carry the qualifier; chapter 1 does not, so it claims more than chapter 71
proves. (The abstract's sentence is at one choice, def:uc-choice, whose index sets are the constructed ones, so it is
true as it stands.)
Fix. 01:153: "d > 1.2497 × 10²⁴ at every admissible choice of the weights, and d < 1.57157 × 10⁵⁰ at one" → "d > 1.2497
× 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct them, and d < 1.57157 ×
10⁵⁰ at one" (rewrap 01:150–156).

**A3 (minor) — 25:29–30 (Text 8): "N′ = 13 for the operator of [[thm:iii-i-5-3]]" is not justified in place.**
Evidence. 13 = −inf 𝗌_0 holds for the orders s_in = 11, s_out = −10 and 𝗌_0 = 𝗌 − 3 that lem:fwd-orders chooses
(71:412–417, 465); the construction of sec:ii-c-5-2 (24:1245–1260) fixes s_in, s_out only by inequalities, so the proof
of thm:iii-i-5-3 does not by itself fix 13, and chapter 25 gives no citation. The number agrees with chapter 71 (and
with "N := 13, the least integer with −N ≤ inf 𝗌_0", 71:464); only its source is missing in place.
Fix. 25:29–30: "(N′ = 13 for the operator of [[thm:iii-i-5-3]])" → "(N′ = 13 for the operator of [[thm:iii-i-5-3]] at
the orders of [[lem:fwd-orders]])".

**A4 (nit) — 00:33: "for one choice of the weights".** thm:uc-integer is at an admissible choice (lem:uc-admissible), as
chapters 1, 3 and 90 say; a choice that is not admissible gives no proof. Fix: "for one choice of the weights" → "for one
admissible choice of the weights".

## B. Chapter 90 (first reading)

Every sentence was held against the result it cites. The following hold as written (no finding): the domain paragraph
(sec:domain, lem:domain, sec:why-five, thm:main's dependence on l5, prop:vaidya); rem:envelope-regularity;
prop:one-zero/rem:round-family, prop:mean-mass/rem:mean-mass-aspect, prop:bondi-hierarchy/rem:bondi-scope;
prop:boundary-spacelike, thm:layer, cor:layer and the paragraph after it (prop:eq-domain "not shown to be needed");
rem:edge-criterion's "decides nothing"; λ0 (sec:main-statement, prop:lambda0 in its three readings, the paragraph after
its proof, rem:m22-value); λ1 and δ (rem:ec-not-evaluated, prop:ec-delta-cap, the paragraph after it); the d paragraph
(section A); the explicit-values paragraph (rem:ec-not-evaluated, summarised without loss); rb-quasimode,
rem:band-observed; thm:own-data's λ_2 and dependence on the class, rem:layer-threshold-size (10^(−430)),
rem:edge-thresholds; the after-shell section (thm:settling, sec:after-shell-gluing, rem:settling-class,
thm:after-shell-reach with cor:after-shell-every-rate for a > 3, prop:interior, lem:interior-one-spacetime,
rem:interior-one-spacetime, rem:vii-4-1, rem:interior-reach, prop:own-tail (d), prop:own-uniqueness,
rem:own-low-weight); the gauges (cor:ix-2-3, rem:ix-2-4, thm:rw-settling (b)–(c), rem:rw-zeta, thm:rwg-1, thm:rwg-2,
thm:rwg-2-prime and the paragraph after it, prop:np-10-1 (iv-b), lem:np-10-1b, thm:harmonic-rate (a)–(c), thm:gd-2-3,
prop:gd-r2-13 (c)); the families (rem:two-dust-scope, thm:class-stability, rem:class-scope, cor:class-two-dust,
thm:vlasov with (Ω), (V1)–(V3), lem:vlasov-open, prop:vlasov-nonempty, rem:vlasov-obstructions, cor:vlasov-two-dust,
rem:vlasov-radial-scope, thm:loc-bent-slice (0.0011596 < 0.0012), thm:charge-sign (a)–(c)); 10 l5 (sec:lambda0-bound's
factor 409, prop:tl5-scales 2.912 and 0.9211, sec:tl5-scales, thm:ten-l5 (b)–(c), lem:tl5-continuation, rem:tl5-beyond,
def:tl5-problem, rem:tl5-constants); the numerical observations paragraph. The two markers of W-90 are gone; the
replacement at 90:174–178 states the four points W-90 listed and matches cor:vlasov-two-dust and rem:vlasov-radial-scope.

**The writer's choices (W-90).** λ0 "bounded", not "evaluated": right; prop:lambda0 proves upper bounds only, and the
sentence says no lower bound is given. The 10 l5 reason: right; F² = 10^66.9 is rem:tl5-constants, a numerical
observation, so the reason must be rem:tl5-beyond's (smooth data, (F1)–(F3) not established, (H1) on a whole region with
the axes, residual bounds at points and on boxes), and 90:205–212 gives exactly that, with the observation labelled as
such; "v ≤ 1/2 in units of the horizon radius" is def:tl5-seeds' unit. Dropped items: Hung's route is dropped by
outline-M (3.2; "not proved and not used") and no chapter states it; the uncertified sharpened λ0 bounds appear only as
rem:m22-value, without figures; log₁₀ δ < −4.45·10¹⁷ belonged to a superseded integer. All right.

### Findings

**B1 (minor) — 90:79–81: "Explicit resolvent bounds are proved for one operator".**
Evidence. Chapter 70 also proves explicit cut-off resolvent bounds for every master operator of the 1-form wave
operator and of the linearised Einstein operator, at every harmonic and every real σ ≠ 0, with the table of B(σ)
(prop:morawetz-master-potentials, 70:1082–1099; carried to the tensor- and vector-type blocks by lem:rb-transfer), as
chapter 70's own introduction (70:16–18) and sec:ec-linear (71:4314–4316) say. The sentence states less than chapter 70
proves and reads as a limitation that does not hold.
Fix. 90:79–81: "Explicit resolvent bounds are proved for one operator, the scalar wave operator on five-dimensional
Tangherlini of mass 1, cut off to {6/5 ≤ r ≤ 4}: … ([[prop:morawetz-resolvent-l-ge-1]], [[prop:morawetz-l-zero]],
[[thm:band]])." → "Explicit resolvent bounds are proved for the scalar wave operator on five-dimensional Tangherlini of
mass 1, cut off to {6/5 ≤ r ≤ 4}: … ([[prop:morawetz-resolvent-l-ge-1]], [[prop:morawetz-l-zero]], [[thm:band]]); the same
identities bound the cut-off resolvent of every master operator of the 1-form wave operator and of the linearised
Einstein operator, at every harmonic and every real σ ≠ 0 ([[prop:morawetz-master-potentials]])." (the middle of the
sentence unchanged).

**B2 (minor) — 90:36–39: "the character of the boundary is decided in the parts of the layer that
[[prop:layer-regions]] describes".**
Evidence. prop:layer-regions (84:1193–1206) decides (i) where E ≥ λ^(3−δ) (spacelike), (ii) on the windows from
first-reach points with λ^P ≤ |env| ≤ λ^(3+δ) (both characters), but (iii) on the band λ^(3+δ) ≤ E ≤ λ^(3−δ) only where
R ≥ 1 + 2λ^γ or R ≤ 1 − 2λ^γ; rem:edge-criterion (85:2034–2043): "the ratio |S|/m0 decides up to the factor 1 ± 2λ^γ in
the band". For a general envelope the band near R = 1 is not decided; only thm:l-24, under its hypotheses, resolves it.
As written the sentence claims the band is decided wherever prop:layer-regions describes it, and omits this limit.
Fix. Replace 90:36–39 ("Inside the layer … ([[thm:very-edge]], [[cor:edge-envelope]]).") by

    Inside the layer [[prop:layer-regions]] decides the character of the boundary above the band between the levels
    λ^(3+δ) and λ^(3−δ), on the windows of length 4πλ that start where |env| first reaches a level between λ^P and
    λ^(3+δ), and on the band up to a factor 1 ± 2λ^(1/10) in the ratio of the first-degree amplitude to the margin
    ([[rem:edge-criterion]]). For an envelope increasing at its edge with the hypothesis (H_N) of [[def:edge-hypotheses]]
    the band is decided by one switch per column ([[thm:l-24]]), and the very edge for envelopes with the edge
    hypotheses, which hold for env_C ([[thm:very-edge]], [[cor:edge-envelope]]).

**B3 (nit) — 90:40–41: "for an envelope whose intervals of zeros accumulate at the edge, the boundary is spacelike
throughout intervals …".** prop:edge-dips proves this for the one envelope [[eq:edge-dips]] (bump heights e^(−n²)), not
for every such envelope; "an envelope" can be read as "every". Fix: "for an envelope" → "for an explicit smooth
envelope".

**B4 (nit) — 90:183–184: "on Σ_τ0 itself the split is hyperbolic except in one band inside the shell, where it is
hyperbolic for no foliation".** prop:loc-band (83:137–140) proves hyperbolicity off 4.2882 ≤ R ≤ 4.5310 and failure for
every foliation on 4.2955 ≤ R ≤ 4.5258; the two thin intervals between are not decided. Fix: "except in one band inside
the shell, where it is hyperbolic for no foliation" → "off the band 4.2882 ≤ R ≤ 4.5310 inside the shell, and on
4.2955 ≤ R ≤ 4.5258 it is hyperbolic for no foliation".

**B5 (nit) — 90:69–70: "No result of [[ch:explicit-constants]] is used in the proof of any theorem of this paper".**
Since D-INT-1, the explicit indices that Texts 7 and 12 add to prop:ii-a1-2-4 (23:1466–1471) and lem:ii-a-8-5
(23:1071–1072) are proved by prop:fwd-calculus, and N′ = 13 (25:29–30) rests on lem:fwd-orders. These clauses are used
only in chapter 71 (thm:fwd-loss), so no theorem's proof depends on chapter 71, but a reader who reads "theorem" as
"result" finds two results of chapter 23 proved there. Fix (90:69–70, and the same at 71:27 for that chapter's reader):
"No result of [[ch:explicit-constants]] is used in the proof of any theorem of this paper ([[ch:explicit-constants]])."
→ "No result of [[ch:explicit-constants]] is used in the proof of any theorem of this paper; the explicit indices of
[[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]], which [[prop:fwd-calculus]] proves, are used only there
([[ch:explicit-constants]])."

**B6 (nit) — 90:161–166: a limitation stated in chapter 81 is not collected.** After cor:class-seed-families
(81:1017–1021): "It assumes the data. They are not constructed here", the outward solve for a small non-round dust
density with regularity at the axes "is not examined here". Chapter 90 collects cor:class-two-dust's assumption but not
this one. Fix: after "…which the construction of that background does not decide ([[cor:class-two-dust]])." add "On the
seed with small non-round families away from the axes the data are assumed, not constructed
([[cor:class-seed-families]])."

**B7 (nit) — 90:210: "on a solution found at the first seed".** "found" narrates a computation outside a remark headed
as a numerical observation. Fix: "a solution found at the first seed" → "a numerical solution at the first seed".

## Observations for the reader of chapter 71 (not counted)

- O1 — 71:1487–1488 (prop:ec-delta-cap): "ω̃ := ω_(2d+3) and s̃ := min(s_(2d+3), s_P) are the modulus and the threshold
  with which (d) holds there (those of [[prop:iii-k-1-2]] (3) at the order 2d + 3)": s_P is lem:iii-k-2-2 (d)'s, not
  prop:iii-k-1-2 (3)'s. Possible fix: "(ω_(2d+3) and s_(2d+3) those of [[prop:iii-k-1-2]] (3) at the order 2d + 3, and
  s_P that of [[lem:iii-k-2-2]] (d))". Also the proof of thm:iii-k-3-2 asks ‖P_5(Ψ(0))‖ < ε_NM (strict, 46:1472–1473)
  where prop:ec-delta-cap takes C_(2d)ω̃(ε) ≤ ε_NM.
- O2 — 71:27, the same sentence as B5.
- O3 — 71:19–20 and thm:uc-integer: the upper bound holds at the choice of def:uc-choice and of def:cs-choices (the
  free orders, inner products and increments as well as the weights); "at one admissible choice of the weights" (71,
  and 01, 03, 90 after it) is true as an existence statement, but "of the weights and of the free orders" would be exact.
