# R2-DINT-a: confirming reading of the fix round F-DINT-a (chapters 00, 01, 25, 90)

Reader: R2-DINT-a (independent; changed nothing in the repository). Tree read at HEAD 392770f4 (the fix round is
ce748932; after it, e915e3e4 changed chapter 71, 724edab6 removed uncited entries from 95 and 98, 392770f4 changed
chapter 46). Read: R-DINT-a, F-DINT-a, the diff of ce748932 for 00, 01, 25, 90 and crosswalk (word diff: the rewraps
drop and add no word beyond the stated replacements); chapters 00, 01 and 90 in full; 25:1–40; chapter 71 at
ch:explicit-constants (opening), def:ec-point, rem:ec-point-outside, sec:fwd, thm:fwd-loss, lem:fwd-orders and the
paragraph after it, lem:fwd-tame, sec:ec-floor, prop:ec-rounds, thm:loss-d, prop:ec-delta-cap, sec:uc-close,
prop:uc-no-eps, lem:uc-two-offsets, cor:uc-two-offsets, rem:uc-offset-d0, def:uc-choice, lem:uc-admissible,
thm:uc-integer, rem:uc-missing, def:cs-choices, rem:ec-not-evaluated; 23 at lem:ii-a-8-5 and prop:ii-a1-2-4 (Texts 12
and 7); 70 (intro, the potentials, lem:rb-transfer, prop:morawetz-master-potentials, thm:band, rem:band-observed); 84
(prop:layer-regions); 85 (def:edge-hypotheses, thm:very-edge, eq:edge-envelope, cor:edge-envelope, thm:l-24,
prop:edge-dips, rem:edge-criterion); 83 (prop:loc-band, thm:loc-bent-slice); 81 (cor:class-seed-families and the
paragraph after it); 87 (rem:tl5-constants); 61 (sec:after-shell-gluing, thm:after-shell-reach,
cor:after-shell-every-rate); 63 (thm:own-data, prop:own-tail, prop:own-uniqueness, rem:own-low-weight); 02
(prop:reduction, prop:vaidya); 03 (thm:main, rem:envelope-regularity, prop:boundary-spacelike, prop:one-zero,
prop:mean-mass, thm:bondi-law, thm:settling); 86 (prop:lambda0, the factor 409); 95 and 96 (openings); 46 at the
Smallness paragraph (46:1527–1562) and notes/reports/P-46-R1.md, only to check what 90 and 71 say of it.

## Verdict

**CONFIRMED — 0 Major, 0 minor, 6 nits** (listed below as N1–N6; all are wording, none affects a statement's truth).

## The original findings

| Finding | Status | Why |
|---|---|---|
| A2 (01:151–153) | Resolved | 01:153 now carries "for the index sets as the proofs construct them", the qualifier of cor:uc-two-offsets (b) and thm:uc-integer ("with the index sets as constructed"); the lower bound is eq:uc-lower, under the hypothesis of cor:uc-two-offsets (a). The rewrap (01:150–156) changes no other word. See N1 for the upper bound's qualifier. |
| A3 (25:29–30) | Resolved | "N′ = 13 for the operator of [[thm:iii-i-5-3]] at the orders of [[lem:fwd-orders]]": lem:fwd-orders is stated for P_0 = 2L_(b₀) and the weights of the proof of thm:iii-i-5-3, and gives inf 𝗌_0 = −13 (𝗌_0 = 𝗌 − 3), so 13 = −inf 𝗌_0 is the least admissible N′ (the paragraph after the lemma, 71:466, says the same; cor:fwd-near-b0, 71:1205, has N = N′ = 13 at every b). Chapter 71's opening (71:30) records this value and says it is used only there. No other site of 25 changed. |
| A4 (00:33) | Resolved | "for one admissible choice of the weights"; lem:uc-admissible proves def:uc-choice admissible. See N1. |
| B1 (90:79–81) | Resolved | 90:84–86 adds the master operators, citing prop:morawetz-master-potentials, which bounds ‖χ_I R(σ) χ_I‖ for every real σ ≠ 0 for V^□, V^v, V^s, V_T, V_V, V_S at every harmonic at which each is defined (rows A–T3, with V^□ at l = 0 by prop:morawetz-harmonics (ii)), as chapter 70's introduction (70:18–19) says. "The same identities" is right: the rows use lem:morawetz-identity. The insertion leaves "The smaller values observed …" without its scalar antecedent (N4). |
| B2 (90:36–39) | Resolved | The band near R = 1 is no longer claimed decided: 90:36–41 states (i) and (ii) of prop:layer-regions, the band up to 1 ± 2λ^(1/10) (γ = 1/10 there; rem:edge-criterion "decides up to the factor 1 ± 2λ^γ in the band"), and the band decided by one switch per column only under thm:l-24's hypotheses (env increasing with (H_N)). True in place. P is new and undefined in 90, and "decides the character … on the windows" means "has points of both characters" there (N3). |
| B3 (90:40–41) | Resolved | "an explicit smooth envelope": prop:edge-dips is for the one envelope eq:edge-dips (h_n = e^(−n²)), smooth and continued to C_c^∞; the rest of the clause is its last sentence. |
| B4 (90:183–184) | Resolved | 90:189–190 is prop:loc-band: hyperbolic (round-sphere foliation) off [4.2882, 4.5310], hyperbolic for no foliation on [4.2955, 4.5258]; the thin intervals between are no longer claimed. "inside the shell" agrees with 83:11. |
| B5 (90:69–70) | Partly resolved | The two results of chapter 23 are now named (their explicit values, 23:1071 and 23:1467, occur nowhere outside 23 and 71). The value N′ = 13 of chapter 25, which R-DINT-a's evidence also named and chapter 71 now lists (71:30), is still omitted, and "any theorem of this paper" includes chapter 71's own theorems (71:28 now says "outside it"). Nit, N2. |
| B6 (90:161–166) | Resolved | 90:171–172 is the paragraph after cor:class-seed-families (81:1019–1020: "It assumes the data. They are not constructed here"). |
| B7 (90:210) | Resolved | "a numerical solution at the first seed"; rem:tl5-constants says "a computed solution at the first seed". |

The fix round introduced nothing false in 00, 01, 25 or 90.

## New findings

Each replacement block is to be pasted without its 4-space indent. Every line of every block has been measured with
Python len (≤ 121) and none starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". No block adds a label.

**N1 (nit) — 00:33, 01:154, 90:68–69: the upper bound is stated at "one admissible choice of the weights"; thm:uc-integer
is at that choice and at the free orders and inner products of def:cs-choices.**
thm:uc-integer (71:2450–2453): "with the index sets as constructed, the admissible choice of the weights of
[[def:uc-choice]] and the free orders and inner products of [[def:cs-choices]]"; rem:ec-not-evaluated (71:4369)
says d depends on "the weights, orders and inner products", and chapter 71's opening (71:20–21) now reads "at one
admissible choice of the weights and of the free orders and inner products". As existence statements the three sites
are true (and the abstract's lower bound holds at def:uc-choice, whose index sets are the constructed ones, 3R >
1.2498·10²⁴), but they read as if the bound depended on the weights alone. (R-DINT-a's O3, not counted there; chapter 71
has since adopted it.)
Fix. 00:33–36, replace

    on which settling is proved, for one admissible choice of the weights, 1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰ for the loss d
    with which the settling proof applies the Nash–Moser theorem; at equality, μ0 = √72 l5², timelike curves of g_λ cross the
    boundary in a layer whose width tends to zero with λ; and at the physical wavelength 10 l5 there is no separation of
    scales, existence holding where the solution is the seed.

by

    on which settling is proved, for one admissible choice of the weights, orders and inner products and the index sets as
    the proofs construct them, 1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰ for the loss d with which the settling proof applies the
    Nash–Moser theorem; at equality, μ0 = √72 l5², timelike curves of g_λ cross the boundary in a layer whose width tends to
    zero with λ; and at the physical wavelength 10 l5 there is no separation of scales, existence holding where the solution
    is the seed.

01:153–156, replace

    d > 1.2497 × 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct them, and
    d < 1.57157 × 10⁵⁰ at one ([[thm:uc-integer]]). A high-frequency theorem, whose expansion parameter is the wavelength
    over the curvature length, does not apply at a prescribed wavelength of 10 l5; there existence holds where the solution
    is the seed ([[thm:ten-l5]]). [[ch:scope]] collects these statements.

by

    d > 1.2497 × 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct them, and
    d < 1.57157 × 10⁵⁰ at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]). A
    high-frequency theorem, whose expansion parameter is the wavelength over the curvature length, does not apply at a
    prescribed wavelength of 10 l5; there existence holds where the solution is the seed ([[thm:ten-l5]]). [[ch:scope]]
    collects these statements.

The chapter 90 site is in the replacement of N2.

**N2 (nit) — 90:71–73: the B5 sentence omits N′ = 13 and says "any theorem of this paper".**
Chapter 71 (71:28–30) now reads: "No result of this chapter is used in the proof of any theorem of this paper outside
it. Other chapters state explicit values that rest on it, the indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]], which
[[prop:fwd-calculus]] proves, and the value N′ = 13 of [[ch:s06]], which rests on [[lem:fwd-orders]]; these values are
used only in this chapter." Chapter 90 lists the first two values but not N′ = 13 (25:29–30), and "any theorem of this
paper" is literally false of chapter 71's own theorems (thm:uc-integer's proof uses prop:cs-cstar). "used only there" is
also less clear than "used only in that chapter".
Fix. Replace the paragraph 90:62–73 (this also makes N1's change at 90:68–69) by

    The loss d is at least the loss d_acc that the proof assigns to the tame estimates, and the regularity of the Nash–Moser
    step is N_NM = 21d + 6; d_acc is composed of elementary losses in closed form, of the loss of the forward solution
    operators, at most 20,180, and of the numbers of steps of the iterations of the construction ([[thm:loss-d]] (i)). At the
    computational point of [[def:ec-point]], d > 1.403 × 10²⁰ and N_NM > 2.946 × 10²¹, so that log₁₀ δ < −1.351 × 10²¹
    ([[thm:loss-d]] (ii), [[prop:ec-delta-cap]]), and d > 1.2497 × 10²⁴ and N_NM > 2.624 × 10²⁵ at every admissible choice of
    the weights, for the index sets as the proofs construct them ([[cor:uc-two-offsets]]). These are lower bounds for the
    loss that this proof's choices produce, not for the least loss with which the tame estimates hold ([[thm:loss-d]]). At
    that point, for those index sets and at one admissible choice of the weights and of the free orders and inner products,
    d is at most an integer below 1.57157 × 10⁵⁰ and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). The
    computational point is a point at which the formulas of the proof can be evaluated, and it lies outside the set on which
    [[thm:settling]] is proved ([[rem:ec-point-outside]]). No result of [[ch:explicit-constants]] is used in the proof of any
    theorem outside that chapter; the explicit indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]], which
    [[prop:fwd-calculus]] proves, and the value N′ = 13 of [[ch:s06]], which rests on [[lem:fwd-orders]], are used only in
    that chapter ([[ch:explicit-constants]]).

(Only lines 68–69 and 71–73 change in substance; the first six lines are 90:62–67 as they stand, rewrapped from 68 on.)

**N3 (nit) — 90:36–38: P (and δ) undefined in chapter 90, and "decides the character … on the windows".**
prop:layer-regions fixes δ ∈ (0, 1/2] and P > 4 (84:1193–1194); chapter 90 introduces neither, and P is new with the
fix. On the windows, (ii) proves that the boundary has points where it is timelike and points where it is spacelike;
"decides the character of the boundary … on the windows" reads as a pointwise decision. Above the band (i) gives
spacelike; on the band (iii) decides up to the factor, as rem:edge-criterion says.
Fix. Replace 90:34–44 ("where it is timelike for g_λ, and future … [[rem:edge-criterion]] decides nothing.") by

    where it is timelike for g_λ, and future timelike curves cross it into D_T ([[thm:layer]], [[cor:layer]]). That the
    domain of [[prop:eq-domain]], whose inner boundary no future causal curve enters, is needed in place of D_T is not shown
    ([[cor:layer]]). Inside the layer, for δ ∈ (0, 1/2] and P > 4, the boundary is spacelike above the band between the
    levels λ^(3+δ) and λ^(3−δ), and it has points of both characters on every window of length 4πλ that starts where |env|
    first reaches a level between λ^P and λ^(3+δ) ([[prop:layer-regions]]); on the band its character is decided up to a
    factor 1 ± 2λ^(1/10) in the ratio of the first-degree amplitude to the margin ([[rem:edge-criterion]]). For an envelope
    increasing at its edge with the hypothesis (H_N) of [[def:edge-hypotheses]] the band is decided by one switch per column
    ([[thm:l-24]]), and the very edge for envelopes with the edge hypotheses, which hold for env_C ([[thm:very-edge]],
    [[cor:edge-envelope]]). Some regularity of the edge is needed: for an explicit smooth envelope whose intervals of zeros
    accumulate at the edge, the boundary is spacelike throughout intervals of length 4πλ below the level λ^(3+δ), for every
    small λ ([[prop:edge-dips]]), and at a dip of a general envelope the criterion of [[rem:edge-criterion]] decides nothing.

**N4 (nit) — 90:86: "The smaller values observed from |σ| = 12 on" now follows the master-operator clause.**
rem:band-observed concerns the scalar wave (V_l, every l ≥ 0); after B1's insertion the nearest antecedent is the
master operators.
Fix. Replace 90:82–89 by

    Explicit resolvent bounds are proved for the scalar wave operator on five-dimensional Tangherlini of mass 1, cut off to
    {6/5 ≤ r ≤ 4}: for every harmonic and every real 0 < |σ| ≤ 3, and with the constant 11.477 for 3 ≤ |σ| ≤ 384
    ([[prop:morawetz-resolvent-l-ge-1]], [[prop:morawetz-l-zero]], [[thm:band]]); the same identities bound the cut-off
    resolvent of every master operator of the 1-form wave operator and of the linearised Einstein operator, at every harmonic
    and every real σ ≠ 0 ([[prop:morawetz-master-potentials]]). For the scalar wave operator, the smaller values observed
    from |σ| = 12 on, and their decay in |σ|, are not proved ([[rem:band-observed]]). For the scalar-type blocks of the
    linearised gauge-fixed operator at zero energy, an upper bound for the least singular value obstructs a good constant at
    a weight next to an indicial root ([[lem:rb-quasimode]]).

**N5 (nit) — 90:105–106 (not touched by the fix): "a perturbation of order of decay a > 3 … is reached directly, for
3/2 < a ≤ ℓ0 the rate does not decide" overlaps on 3 < a ≤ ℓ0.**
Both halves are true: thm:after-shell-reach (i) reaches a > ℓ0 directly at the given ℓ0, which over the admissible ℓ0
covers every a > 3 (cor:after-shell-every-rate, run with ℓ0 ∈ (3, min(a, 4))), and (ii) leaves 3/2 < a ≤ ℓ0 undecided
at the given ℓ0. Juxtaposed without the change of ℓ0, they read as contradicting each other for a ∈ (3, ℓ0].
Fix. Replace 90:104–107 by

    perturbations that (ii) reaches, directly or through gluing uniformly in the gluing radius, are exactly those small in
    Hintz's class: a perturbation of order of decay a > ℓ0 and small enough size is reached directly, which over the
    admissible ℓ0 covers every a > 3 ([[cor:after-shell-every-rate]]), for 3/2 < a ≤ ℓ0 the rate does not decide, and the
    statement that (ii) applies up to the gluing is false for fixed size and large radius at every such a
    ([[thm:after-shell-reach]]).

**N6 (nit) — 01:193–194 (not touched by the fix): the appendices.**
"each with its source, number and page": app:standard-results cites each result "by its source, with its number and its
page where given", and proves five items itself (95:3–8). app:tables, which the proofs use, is the one part of the
paper the Organisation does not name.
Fix. Replace 01:193–194 by

    [[app:standard-results]] states the results of the literature that the proofs use, each with its source and, where the
    source gives them, its number and page; [[app:tables]] prints the coefficients of the explicit polynomials, approximants
    and enclosures that the proofs use.

## Checked and found to hold

- **Checks.** `python3 lint.py --chapters`: "chapters: 62 file(s), 4570 label(s) defined, 0 hit(s)".
  `python3 assemble.py --check`: "labels 4570, computations cited 0, problems 0". On a scratch copy of chapters/ and
  assemble.py, the assembled paper has 95,968 lines and none over 121 characters (the 123-character line F-DINT-a
  reported is gone).
- **Line rules.** Every line of 00, 01, 90 and of 25:1–40 is at most 121 characters (Python len). The only lines that
  start with a forbidden prefix are headings, the list items of 01:97–119 and the block quote of 01:24–36. Every label key
  in these files is lowercase. The fix round added no label; the crosswalks of 00, 01, 25 and 90 match their chapters'
  labels in order (0, 9, 93, 8 labels).
- **Contract.** No file name, program name, code, or AI or assistant language in 00, 01, 25 or 90. Every bibliography
  key cited in 00, 01 and 90 is still in chapter 98 after PR-1.
- **The loss d.** 1.2497·10²⁴ < d holds for the index sets as constructed at every admissible choice of the weights
  (cor:uc-two-offsets (a)–(b), eq:uc-lower). d < 1.57157·10⁵⁰ holds at def:uc-choice with def:cs-choices
  (thm:uc-integer: d_NM = d_R ≤ D_NM; the integers re-multiply as printed). "d" in 00, 01 and 90 is d_NM, the loss with
  which the Nash–Moser theorem is applied (thm:loss-d, prop:ec-delta-cap). The lower bound does not depend on the free
  orders, since ℓ_tf ≥ 1 in every inner product (thm:loss-d (ii)). 90:62–70 agrees with thm:loss-d (i)–(ii),
  prop:ec-delta-cap (log₁₀ δ < −1.351·10²¹), cor:uc-two-offsets (21 · 1.2497·10²⁴ > 2.624·10²⁵), thm:uc-integer and
  rem:ec-point-outside. The qualifiers are right apart from N1.
- **Chapter 46 as it now stands.** 00, 01 and 90 cite no label of chapter 46. 90:57–60 summarises prop:ec-delta-cap,
  whose hypotheses (ε ≤ s̃, C_(2d)ω̃(ε) < ε_NM) are still those of chapter 46's Smallness after P-46-R1 (46:1557–1560).
  90:125 ("ε, d_1 and λ_2 depend on the class") is thm:own-data's last paragraph; d_1 stays a symbol there.
- **Chapter 25, Text 8.** True in place and justified by lem:fwd-orders (above). The rewrap changes no other word, and
  the remaining notation (β_0, β_Γ, ϕ^u, φ_ε, N_E) is as before.
- **Chapter 00.** Checked against prop:reduction (target (3/2) dψ² + 2 dω²), thm:main items 4, 6 and 7 with
  prop:one-zero and prop:mean-mass (one zero at O(λ); mass to O(λ²) after the shell), thm:bondi-law item 3 (μ(v) + O(λ)
  in the shell; μ(v_end) + (2/9)λ²A²∫env′² + O(λ³) after it), thm:settling (i)–(ii) and sec:after-shell-gluing ("a
  continuation of the data of g_λ beyond a ball" is the glued data, not the data of a continuation of g_λ, consistent
  with 90:99–101), prop:interior, thm:own-data, prop:lambda0 and cor:layer. All hold (N1 aside).
- **Chapter 01.** sec:what-is-proved, sec:why-five (prop:boundary-spacelike; r = a < r_q ≤ √μ, so Ω's inner boundary is
  spacelike even at equality, as the relation list says), sec:introduction-scope (sec:domain, prop:vaidya (b),
  prop:interior, prop:lambda0, thm:ten-l5) and sec:organisation. The latter is checked against every part and chapter
  heading: chapter 90 lies in part:further, as said. All hold (N1, N6 aside). The quotations of [HL18], [HL24], [LR20]
  and [Tou23a] were not checked against their sources.
- **Chapter 90, the rest.** Spot-checked anew: rem:envelope-regularity, prop:boundary-spacelike, prop:lambda0 (0.0024433,
  0.0019079, 0.0012228) and the factor 409 (86:304), rem:layer-threshold-size (10^(−430), 84:1357–1365),
  rem:ec-not-evaluated (90:75–80), thm:own-data, prop:own-tail (d), prop:own-uniqueness, rem:own-low-weight,
  thm:loc-bent-slice (0.0011596 < 0.0012), cor:class-seed-families and rem:tl5-constants. The other sentences were
  verified sentence by sentence by R-DINT-a at 74074c98. Since then only chapters 46, 71, 95 and 98 changed in content,
  and the word-free rewrap 49385df7 touched 34, 47, 61, 65, 83 and 85; the changed results of chapter 71 that 90 cites are
  re-checked above.
