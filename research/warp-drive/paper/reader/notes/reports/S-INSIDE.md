# S-INSIDE: can the bounds on d be stated at a point where thm:settling is proved?

Feasibility study, read-only. Paper: `research/warp-drive/paper/reader/`, chapters as committed on 2026-11-20.
References `NN:line` are to `chapters/NN-*.md`. I did not run `assemble.py`, and nothing in the repository was changed.
Two small computations were made in the scratchpad: a sympy derivative and an mpmath root check. They are marked
**[computed here]** where they are used. They are evidence, not proofs.

**Answer in brief.**

- **The computational point is known to lie outside the proved set, because of h.** It is undecided whether the
  gauge half (γ_Υ, e_Υ) = (1/100, 1/100) lies inside.
- **Four thresholds have no value, and their proofs give none:** h_0, h_tf, ε_0 and ε_1. They come from semiclassical
  absorption, contradiction and compactness, and finite covers.
- **d is unbounded on the proved set.** Its proved lower bound grows like z⁻² and like h⁻² as the parameters tend to
  0. So no explicit upper bound can be stated at a point of the proved set unless that point is certified, which
  needs those four thresholds.
- **The lower bounds can be moved onto the proved set cheaply.** They become explicit functions of (z, h) that hold
  at every admissible point.
- **Verdict (b): feasible in part.** The decisive part, an explicit upper bound at a certified point, is (c).

---

## 1. The conditions

thm:settling (03:276–300) fixes l5, μ0, A, env, τ0, r_♭ and ℓ0 ∈ (3, 4). It takes everything else from the stability
theory: "let ε_K be the decay parameter chosen in that theory ([[thm:vi-c-2-1]] …)".

- **The set on which it is proved** is the set of parameter choices that meet every row of sec:vi-c-1 (46:1697–1779).
  The choices are made in the order (0)–(6) of thm:vi-c-2-1 (46:1782–1824).
- **The free parameters** are:
  - the damping, (v_C, e_C, C_0, h);
  - the gauge, (γ_(Υ,H), e_Υ, γ_Υ);
  - the data classes, (ℰ_0, ℓ_0, ℓ_I);
  - the weights, (ε_+, ε_K, α);
  - the parameter ball ℬ_*;
  - (ε, d_1).

**Threshold types used below:**

- **E**: an explicit number.
- **EU**: explicit in principle but not evaluated. It is a finite or algebraic computation that nobody has done.
- **X**: existential. Its proof gives no number: compactness, contradiction, a finite cover, or "for h small"
  absorption.

**Rows whose thresholds bear on the question:**

| row | condition | source | type | at (γ_Υ, e_Υ, h) = (1/100, 1/100, 10⁻⁶) |
|---|---|---|---|---|
| c1 | (v_C, e_C, C_0) = (½, 1/102400, 100) | eq:iv4-0-1 (33:110), 46:1709 | fixed | holds (C_0 = 100 is implicit in ch. 71: its "−101" is −C_0 − 1) |
| c2a | h < 10⁻⁶ (the cap in h_*) | eq:iv4-0-1 | E | **fails**: 𝖧 ⊂ (0, h_*), h_* ≤ 10⁻⁶, and the interval is open |
| c2b | h < h_0 | thm:iv5-7-3 (33:1862), with C₁ = C_0 + 1 and the weights eq:iv4-2-1 at C_0 and at C_0 − 1; uniform in b by lem:iv5-8-1 (33:1926) | **X** (semiclassical absorption) | unknown |
| c2c | h < h_tf | thm:iv6-3-1 (33:2239): the h_0 of thm:iv6-2-1 at the weights (−5/2, 5/2) with C₁ = 1, "with h_tf ≤ 10⁻⁶" | **X**, capped by an E | fails as defined (the cap); the uncapped value is unknown |
| c2d | h ∉ 𝖹 = 𝖹₁ ∪ 𝖹₂ ∪ 𝖹₃ | lem:iv4-1-3 (b) (33:1059); prop:np-10-52 (ii), (iii) (33:2732) | **EU**: zeros of non-zero polynomials in h (discriminants, resultants, values at points), over all l | 𝖹₃ is excluded by cor:s14-eps-ind-point. 𝖹₁ and 𝖹₂ are undecided: (C2)–(C3) are open for the roots below −101 (prop:is-mult, 71:2843) |
| c3 | (C1)–(C4) | thm:iii-e-1-1 (3) | proved for h ∈ 𝖧 | (C1) holds (prop:np-10-54 is valid on (0, 10⁻⁶]). (C4) is shown for roots with \|ι − 1\| ≤ 50 (prop:s14-damping-distance) but not in general. (C2)–(C3) are undecided |
| c4 | (C5) γ_C v_C ≥ ½ and s_C > 100 | 46:1715 | E | holds |
| u1 | the 1-forms c_Υ, c_(Υ,H), c_C | 46:1718 | none | fixed |
| u2 | γ_(Υ,H) ∈ (0, ε_0], ε_0 = min(γ_2, ½ϵ) | prop:iii-d1-4-1 (32:1041), Step 2; the ϵ of prop:iii-d-6-3 (32:730) | **X** | **not specified by def:ec-point.** No number in ch. 71 depends on it: ϑ_ℋ = 1 for every γ_(Υ,H) (lem:iii-d-5-1) |
| u3 | e_Υ < min(ε_1, ε_L) | prop:iii-d1-4-1 (ε_1); lem:iii-d-7-1 (32:780) (ε_L) | ε_1 **X**; ε_L **X as proved, explicitable** | unknown |
| u4 | γ_Υ < min(ε_1, ε_L, γ_1, 3/8, ½s_C, ¼) | prop:iii-f1-3-3 (34:635) (γ_1) | γ_1 **X as proved, explicitable**; the rest E | the E caps hold; γ_1, ε_1 and ε_L are unknown |
| u5 | z = 4e_Υγ_Υ² ∈ (0, ½] ∖ 𝖹_exc | prop:iii-f1-2-3 (e) (34:422) | **EU**: countable, fixed by the roots of □^C at the h already chosen | z ∈ (0, ½] holds. Simplicity on Re ∈ [−101, 5] is proved (prop:is-mult); below −101 it is undecided |

**Rows that are explicit, or whose thresholds are harmless for d:**

- **b1–b4: the neighbourhoods of b₀ (ℬ_VI, ℬ(γ_(Υ,H)), ℬ(c_σ), (B5), b4).** These are **X**, but harmless here. Every
  bound in ch. 71 holds "at every b near b₀", and no b-radius enters d.
- **w1: ε_K < ε_+ < min(δ_♯, ε_ind, ℓ_I − 3, ¼), (G⁺), (G), ε_K < ε_Υ, and (Ex1)–(Ex2).** These are E, given Λ, ε_ind
  and ε_Υ. ch. 71 makes an admissible choice (lem:uc-admissible, 71:2310), but it uses ε_ind(10⁻⁶) = δ_50
  (cor:s14-eps-ind-point). This is the one place where w1 depends on h.
- **w2: α admissible, (A_J), (Ex3)–(Ex4).** These are finite exclusions, and they are met (lem:uc-admissible).
- **d1 and d2: the data classes.** These are E or discrete exclusions, and they are met: min Re ℰ_0 = 2 > 3/2 + 2γ_Υ
  = 1.52, and ℓ_I is chosen in def:uc-choice.
- **n1: ε and d_1 of thm:iii-k-4-3.** ε (data smallness) is X but harmless. d_1 is fixed by the Nash–Moser regularity,
  that is, by d itself.
- **δ_♯ = (1 − e_Υ)γ_Υ = 0.0099 and λ_♯ = 15099/10000** are explicit.

So **eight threshold-type quantities on (h, γ_(Υ,H), e_Υ, γ_Υ) decide membership:**

- the four of type **X**: h_0, h_tf, ε_0 and ε_1;
- two that are **X only as proved**, and could be made explicit: ε_L and γ_1;
- two countable exclusions of type **EU**: 𝖹 and 𝖹_exc.

The cap 10⁻⁶ and the caps 3/8, ½s_C and ¼ are explicit. The order of choices matters:

- γ_1 depends on h.
- ε_1 depends on γ_(Υ,H).
- 𝖹_exc depends on h.

So "admissible" means: for the given h, there is some γ_(Υ,H) ∈ (0, ε_0] with e_Υ, γ_Υ < ε_1(γ_(Υ,H)), ε_L, γ_1(h).

---

## 2. The computational point

**What rem:ec-point-outside (71:49–57) says, exactly.** It makes two different claims.

1. **h: decided.** "[[thm:settling]] takes h in the set 𝖧 …, whose supremum h_* = min(10⁻⁶, h_0, h_tf) is at most
   10⁻⁶; so h = 10⁻⁶ is not in 𝖧." Since 𝖧 = (0, h_*) ∖ 𝖹 is open at h_*, the point is **known to be outside**. It
   would stay outside even if h_0 were large, because h_tf is itself capped at 10⁻⁶ (33:2246).
2. **(γ_Υ, e_Υ): undecided.** "… required in [[thm:vi-c-2-1]] to lie below thresholds whose existence is proved and
   whose values are not determined; whether (γ_Υ, e_Υ) = (1/100, 1/100) lies below them is not decided."

**How the other texts describe it.**

- **The ch. 71 introduction (71:24) and ch. 03 (03:353: "at a parameter point that lies outside the proved set") are
  correct**, because of claim 1.
- **G-SWEEP row C7 ("whether (1/100, 1/100, 10⁻⁶) is admissible is undecided") is accurate only for the gauge half.**
  It should read: "known outside in h, by construction; undecided in (γ_Υ, e_Υ)".

**Which conditions fail, and which are unknown.**

- **Fail:** c2a, and c2c as defined.
- **Unknown:**
  - c2b (h_0) and the uncapped h_tf;
  - c2d (𝖹₁ and 𝖹₂ at 10⁻⁶);
  - c3 (C2)–(C3), and (C4) beyond |ι − 1| ≤ 50;
  - u2–u4 (ε_0, ε_1, ε_L, γ_1), and whether any γ_(Υ,H) serves;
  - u5 below Re −101.
- **Hold:** everything else (c1, c4, the E caps, z ∈ (0, ½], d1, d2, w1 and w2 at ch. 71's choice).

**The exclusion in h is soft in one sense and hard in another.**

- **Soft.** It comes from an open interval and a cap placed where the indicial analysis was done: lem:iv4-1-3 and
  prop:np-10-54 hold on the closed interval (0, 10⁻⁶].
- **Hard.** Because h_0 and h_tf are existential, **no** h ∈ (0, 10⁻⁶) is known to lie in 𝖧. 𝖧 is non-empty, but
  its supremum is unknown.

**Which of ch. 71's numbers depend on h, and which on the gauge.** I traced every use of h in ch. 71.

- **h enters only through four inputs:**
  - (a) ε_ind(10⁻⁶) = δ_50 > ε_Υ. lem:uc-admissible uses it for ε_g = ε_Υ and for ε_+ < ε_ind.
  - (b) The exponents ι + 1 + j, ι ∈ Z, of ℰ^ι_ind (prop:is-iota, 71:2817). They lie above 3 and do not enter
    Λ ∩ {Re ≤ 3 + ε_+} (rem:is-summary).
  - (c) Simplicity on the strip [−101, 5] (prop:is-mult).
  - (d) The poles of N_ι⁺ (lem:sp-roots, thm:sp-spectrum, 71:3534–3720).
- **Inputs that hold for every γ_C > 0 and γ_Υ > 0:** the forward loss and the orders of lem:fwd-orders (ϑ_L < 2),
  and lem:ec-theta-in-zero.
- **Inputs fixed by the gauge alone:**
  - the gap sums (prop:gap-sums) and ε_Υ (lem:ec-gauge-gap);
  - Λ below 3 + ε_+ (prop:is-lambda: its 29 generators and 𝔡₀, 𝔡₁, δ₂, δ′₁, σ_Υ);
  - μ_G (thm:is-gap), N_Λ, k̄_0 and J_*;
  - the least ℰ^C_I and ℰ_++.

**The bounds on d depend on the parameters, and they blow up as the parameters tend to 0.** This is a direct reading
of prop:ec-rounds and thm:loss-d, whose proof uses only ε_K < ε_g ≤ δ̂ and ε_ind ≤ δ̄:

    d ≥ 3R > 3(1 − 5δ̂ − δ̄)/δ̂²    for any upper bound δ̂ of ε_g = min(ε_Υ, ε_ind(h)).

Neither factor of ε_g is bounded below on the proved set.

- **In the gauge.** At every gauge point, ε_Υ < ½𝔡_ℳ ≤ ½(d₁(8) − d₂(7)). By eq:s14-theta, which holds for all
  z ∈ (0, ½], this is z/27360 + O(z²). The leading coefficients 5/171 − 7/240 = 1/13680 do not depend on the
  parameters. Hence d ≳ 3·27360²/z² ≈ 2.2457·10⁹/z² at every admissible point.
  - At z = 4·10⁻⁶ this gives 1.4036·10²⁰, the bound of thm:loss-d (ii).
  - For the index sets as constructed, μ_G ≤ 𝔢 := 𝔡₀ − 4𝔡₁ whenever the second set of lem:is-reduction is non-empty.
    𝔢 = (5/144)z² + …, which is 5.5556·10⁻¹³ at the point **[computed here]**. So the raised lower bound scales
    roughly like z⁻³. This last scaling is a heuristic, not checked in general.
- **In h.** The root of P_2 that tends to 2 as h → 0 is 2 + (40/13)h + O(h²).
  - The coefficient is −∂_hP_2/∂_ιP_2 at (2, 0), with e = 1/102400 and v = ½ **[computed here]**. Numerically,
    (root − 2)/h = 3.0755, 3.0769 and 3.0769 at h = 10⁻⁸, 10⁻¹⁰ and 10⁻¹² **[computed here]**.
  - This is consistent with lem:s14-sextic-small (b): (2.93h, 2.94h) at h = 10⁻⁶, where e/h ≈ 9.8 is not large.
  - The root gives the entry 1 + (40/13)h + O(h²) of ℛ^sc_2. So ε_ind(h) ≤ (40/13)h(1 + O(h)) for every small h.
  - Three consequences:
    - Below h ≈ 4.75·10⁻¹¹, ε_ind(h) < ε_Υ and ε_g = ε_ind(h).
    - Below h ≈ 5.3·10⁻¹⁵, the ε_+ of def:uc-choice is no longer allowed.
    - d ≳ 3(13/40)²/h² ≈ 0.317/h². This exceeds the upper bound D_acc < 1.57157·10⁵⁰ of thm:uc-integer once
      h < 4.5·10⁻²⁶.

So **the upper bound of thm:uc-integer cannot hold at every point of 𝖧, even with the gauge values (1/100, 1/100)**,
unless h_* ≳ 4.5·10⁻²⁶. Whether it holds at the points of 𝖧 depends on the unknown h_*. The same is true in z.

**Any explicit number valid at a point of the proved set therefore requires an explicit lower bound for the
thresholds that define that set, or a direct certificate that a particular point belongs to it.** These sketches
re-run proved statements with general constants. They are not stated in the paper.

---

## 3. Thresholds, one by one

For each threshold below:

- **Trace:** where its proof comes from.
- **Explicit?** Whether it can be made explicit, and at what cost.
- **Another point:** whether a different parameter point helps.
- **Re-run:** whether ch. 71's machinery could then be re-run there.

### T1. The cap 10⁻⁶ and the open interval (E)

- **Trace.** The cap is placed where the indicial analysis was done.
- **Explicit?** Already explicit. One could close the interval at 10⁻⁶ when h_0, h_tf > 10⁻⁶. h_tf would have to be
  uncapped: its definition caps it, but nothing in its proof needs the cap.
- **Cost.** Nil, but it is useful only once T2 and T3 are resolved.

### T2. h_0 (X): the semiclassical forward estimate

- **Trace.**
  - thm:iv5-7-3 rests on prop:iv5-7-1 and prop:iv5-7-2, which chain about ten microlocal estimates: radial points at
    r_c, the sink and ∂K⁺, propagation along 𝗌𝖿 and K⁺, and energy estimates.
  - These are built on the semiclassical 3b-calculus: composition, parametrices and the sharp Gårding inequality.
  - The h^N‖χω‖ errors are absorbed "for h small". lem:iv5-8-1 says each threshold is "determined by" finitely many
    seminorms and positivity margins.
- **Explicit?** Only with a quantitative semiclassical 3b-calculus: remainder constants in composition and in sharp
  Gårding with the seminorms tracked, explicit radial and propagation estimates, and the absorptions carried out with
  numbers.
  - The input carries G-SWEEP gaps G1, G2 and G4. The calculus rests on unquoted preprints, [Hin26a, Lemma 5.14 and
    Corollary 5.15] are used as stated, and several steps are written at outline level. Those would have to be closed
    first.
  - **Cost:** monograph scale, thousands of lines. **Not feasible with present methods within this paper.**
- **Another point: a non-semiclassical route.** Prove (1)–(4) of thm:iii-e-1-1 directly at one explicit h, at b₀,
  harmonic by harmonic:
  - each harmonic gives a 3 × 3 system with γ_C = h⁻¹ large;
  - large l is handled by asymptotics, and finitely many l by validated numerics;
  - the step to b near b₀ is by openness, which is harmless.
  - thm:iv5-7-3 is used in the proof of (1) and of surjectivity in (2) (33:2269–2330), so both need a new argument.
  - **Cost:** a research project, high risk.

### T3. h_tf (X): the transition-face model

- **Trace.** thm:iv6-3-1 takes the h_0 of thm:iv6-2-1, which is semiclassical in the edge-b setting "by the arguments
  of [[sec:iv5]]".
- **Explicit?** Same nature as T2, and not feasible in this frame.
- **Another point.** The tf model is dilation-invariant on Minkowski space, so a direct proof of kernel triviality at
  a fixed h is an ODE question per harmonic (a regular singular point at 0 and an irregular one at ∞). This is easier
  than T2.
  - **Cost:** moderate to high, roughly 800–2,000 lines with large-l uniformity. Risk: medium to high.

### T4. 𝖹 = 𝖹₁ ∪ 𝖹₂ ∪ 𝖹₃ (EU)

- **Trace.** Each piece is the zero set in h of explicit non-zero polynomials.
- **Explicit? Deciding a given h:**
  - For 𝖹₃ only finitely many l matter (prop:np-10-54 (iii)).
  - For 𝖹₁ (simplicity for all l), the six roots near ±κ^(1/2) need large-l asymptotics, plus a finite check.
  - At 10⁻⁶ only (C2)–(C3) below −101 are open.
  - **Cost:** about 200–400 lines. Risk: low to medium.

### T5. ε_0 (X): mode stability with the horizon modification alone

- **Trace.** ε_0 = min(γ_2, ½ϵ), from three pieces:
  - γ_2 comes from Step 1 of prop:iii-d1-4-1: a Grushin problem with a Schur complement −4π²(−iσ + γ) +
    o(|σ| + γ). The o-term comes from a sequential-compactness "Claim" (Rellich).
  - γ_1, c_0 and C come from thm:i-c-7-1 and thm:i-c-6-4, both proved by contradiction (22:1323 ff.).
  - ϵ comes from prop:iii-d-6-3: a finite cover of a compact frequency set, using openness (thm:i-a-8-1).
- **Explicit? It would need all of the following, for □ on 1-forms on Tangherlini:**
  - an explicit inverse bound for the augmented zero-energy operator 𝒫_0(0) in weighted b-spaces;
  - an explicit remainder in the low-energy expansion;
  - explicit bounds at bounded frequencies;
  - an explicit high-frequency (trapping) estimate.
- **What ch. 70 provides.** It is the paper's only start. It gives explicit cut-off resolvent bounds for the scalar
  wave operator on the real axis, the band 3 ≤ |σ| ≤ 384, and the master potentials of the 1-form operator
  (prop:morawetz-master-potentials). It records where it stops:
  - the absorbed inverse "gives no bound" (lem:rb-absorbed);
  - at zero energy there is a quasimode obstruction for the Einstein scalar blocks (lem:rb-quasimode);
  - the trapping estimate is proved by a defect-measure contradiction (rem:ec-not-evaluated).
- **Cost.** Several chapters the size of ch. 70 (about 1,500 lines each): an estimated 5,000–10,000 lines, at high
  risk. **Not feasible with present methods in reasonable scope.**
- **Another point.** Only *some* γ_(Υ,H) ≤ ε_0 with ε_1(γ_(Υ,H)) > 1/100 is needed. But that is the same problem: an
  explicit mode-stability theorem at a specific parameter.

### T6. ε_1 (X): mode stability of the whole family

- **Trace.** Step 2 of prop:iii-d1-4-1:
  - low energies by perturbation from (Z) at 𝗉_γ (thm:i-c-7-1);
  - high energies from prop:iii-d-6-1, whose C_0 rests on the trapping estimate;
  - a finite cover of the compact middle band.
- **Explicit?** It would need explicit lower bounds for the inverse of P̂_𝗉(σ) on all of Im σ ≥ 0, together with an
  explicit Lipschitz dependence on 𝗉. This is the cost class of T5.
- **Another point.** The direct alternative is a computer-assisted proof of mode stability of □^Υ_(b₀) at
  (e_Υ, γ_Υ) = (1/100, 1/100) and some γ_(Υ,H), enhanced at σ = 0. The cost is the same. The uniformity in l and
  σ near 0 is the crux.

### T7. ε_L (X as proved; explicitable)

- **Trace.** lem:iii-d-7-1 asks C′|γ_Υ| ≤ ½. Its C is the constant of cor:i-c-5-2 (b) at γ_Υ = 0, which is proved by
  contradiction (22:711). Its C′ is the norm of −2ie^(iθ)ρ̂S̄ + γ_Υρ̂²M_E between the sc-b spaces.
- **Explicit? Yes, at moderate cost.**
  - At γ_Υ = 0 the model is the componentwise Helmholtz operator on ℝ⁴. Its inverse is explicit per harmonic through
    Hankel functions (lem:i-c-5-4, prop:i-c-5-3).
  - What remains is to carry that inverse through the variable-order sc-b norms, uniformly over the three θ-sectors,
    and to bound C′ and the order margins (S̄ = O(γ_Υ) explicitly).
  - A cleaner alternative: prove tf-admissibility at γ_Υ = 1/100 directly, by kernel triviality per harmonic plus
    index 0.
  - **Cost:** about 400–800 lines. Risk: medium; the variable orders are the awkward part.

### T8. γ_1 (X as proved; explicitable)

- **Trace.** Step 6 of prop:iii-f1-3-3 has the same structure as T7, for □ on S²T* and P̂′. Its constant depends on
  the orders, and so on h, which is fixed first.
- **Explicit?** It needs the same machinery as T7, plus a check that weight 1 lies in the gap of P̂′(0) at
  γ_Υ = 1/100. That check is explicit, since the roots are within O(γ_Υ) of integers.
  - **Cost:** about 400–800 lines, sharing most of the work with T7. Risk: medium.

### T9. 𝖹_exc (EU)

- **Trace.** The countable set of z at which a root of □^C coincides with ι^Υ + 2 or 3 − ι^Υ of the same type and
  degree (prop:iii-f1-2-3 (e)).
- **Explicit? At the point** the strip is done. Below −101, large l must be compared: the low □^C roots ≈ −√κ ≈
  −(l + 1) + O(1/l), against 2 − ι^Υ ≈ 1 − l − d₂ and −l − d₁.
  - The two families agree to O(1/l), so the asymptotics must be carried to the order at which they separate, plus a
    finite check.
  - **Cost:** about 200–400 lines. Risk: medium.

### T10. Is there a better parameter point?

**No point is better known than the computational one.**

- Every threshold is an upper threshold. Without values, a point nearer to 0 is no more certainly admissible, and by
  §2 its bound on d is worse, like z⁻² and h⁻².
- **The natural candidates, in order:**
  1. (h, 1/100, 1/100) with h just below 10⁻⁶. This keeps ch. 71's numbers.
  2. If T7–T8 give thresholds below 1/100, the largest gauge values under them, with the gauge part of ch. 71 re-run.
- **How to prove a point admissible.** Either make T2–T8 explicit, or certify the point directly (T2 alternative, T3,
  T6 direct, T7/T8 direct, and T4, T9).

### T11. Re-running ch. 71 at another point

The parts of ch. 71 split into those that need no change at another point and those tied to the point.

- **Generic, and unchanged:**
  - the accounting rules and the forward loss 20,180/20,183 (lem:fwd-orders holds for every γ_C);
  - ϑ_in = 0, ℓ_tf = 1 and d_BG = 11;
  - the counting lemmas lem:ec-counts and prop:ec-upper, and lem:is-reduction as an algorithm.
- **Point-specific:**
  - sec:ec-gap-sums and lem:ec-gauge-gap;
  - sec:is (exponents, μ_G, N_Λ, J_*) and sec:sp (the poles at ι⁺);
  - sec:s14-pa with the ch. 96 tables, on which prop:is-iota, prop:is-mult and lem:sp-roots rest;
  - the evaluation in sec:uc-eval and sec:cs.
- **At (h′, 1/100, 1/100), h′ ∈ [h₁, 10⁻⁶).** Only inputs (a)–(d) of §2 change. h₁ is about 5·10⁻¹¹, the floor set by
  ε_ind(h′) ≥ ε_Υ.
  - The roots of P_l must be enclosed over an interval of h. The ch. 96 expansions assume e = ε₀h with ε₀ = 625/64
    fixed, so they become two-parameter enclosures with ε₀ ∈ [625/64, (625/64)·10⁻⁶/h₁].
  - Finitely many near-coincidence values of h, from 𝖹₂ and 𝖹₃ and from lem:sp-roots (c), must be excised.
  - **Cost:** about 400–900 lines.
- **At a new gauge point.** Everything point-specific changes, including the μ_G search and (SP).
  - **Cost:** about 2,000–3,000 lines.
- **A parametric version d ≤ F(z, λ_♯, σ_Υ, h), valid at every admissible point**, is conceivable:
  - μ_G is given by lem:is-reduction as an algorithm, or bounded below by a Liouville estimate for the
    linear forms in the algebraic numbers 𝔡₀, 𝔡₁ and λ_♯. An exact hit at 3 is harmless, because the window
    (3, 3 + ε_K] is open at 3.
  - The roots of □^C would have to be located uniformly in h.
  - **Cost:** at least as large as the above. It certifies no number, since no point is certified.

---

## 4. Verdict and plan

**Verdict: (b), feasible only in part. The part that decides the question is (c).**

- **(c), for what was asked.** An explicit bound on d at a point *shown* to satisfy every hypothesis of thm:settling
  is not feasible with present methods. h_0, h_tf, ε_0 and ε_1 are existential (T2, T3, T5, T6). §2 shows that they
  cannot be bypassed: d is unbounded on the proved set, so an upper bound needs a certified point.
  - rem:ec-not-evaluated (71:4689) already names the four kinds of argument responsible: a compact error removed by
    contradiction, compactness in parameters, a defect-measure trapping estimate, and finite covers.
- **(b), what can be done.**
  - The lower bounds can be stated at every point of the proved set.
  - The h-direction can be decoupled conditionally.
  - ε_L, γ_1, 𝖹 and 𝖹_exc can be made explicit, or decided at a point.

**The plan, in order of value for cost:**

0. **Correct the status wording.** Under one page, no risk.
   - G-SWEEP C7: "known outside in h (by construction); undecided in (γ_Υ, e_Υ)".
   - rem:ec-point-outside could add that γ_(Υ,H) is unspecified and that d does not depend on it.
1. **Lower bounds on the proved set.** About 120–250 lines, 1–2 weeks, low risk.
   - (i) A lemma: for every z ∈ (0, ½], 𝔡_ℳ ≤ d₁(8) − d₂(7) ≤ z/13680 + c·z². This follows from eq:s14-theta.
   - (ii) A lemma: for every h ∈ (0, 10⁻⁶], ε_ind(h) ≤ (40/13)h(1 + c′h). The proof is a sign computation on P_2 at
     2 + c₁h and 2 + c₂h, like lem:s14-sextic-small (b) but for general h with e fixed. The derivative computed here
     fixes the constant.
   - (iii) prop:ec-rounds and thm:loss-d (ii) re-run with δ̂ := min(½𝔡_ℳ(z), ε̄_ind(h)).
   - **The result:** at every admissible (h, γ_Υ, e_Υ), d_NM ≥ d_acc > 3(1 − 5δ̂ − δ̄)/δ̂², roughly
     max(2.2457·10⁹/z², 0.317/h²). This reproduces 1.403·10²⁰ at z = 4·10⁻⁶.
   - **The value:** every lower bound of ch. 71 that uses only ε_g becomes a statement about the proved set, and the
     reader sees why no upper bound can be uniform.
   - The raised bound 1.2497·10²⁴ needs μ_G at general z. Leave it at the point, or add the z⁻³ heuristic as a
     remark.
2. **A conditional transfer in h.** About 400–900 lines, 3–6 weeks, medium risk.
   - The theorem: if (1/100, 1/100) is admissible, then for every h ∈ 𝖧 ∩ [h₁, 10⁻⁶) the bounds of thm:uc-integer
     hold.
   - The work is T11's h-interval re-run of the four h-inputs (a)–(d).
   - **Risks:** the two-parameter enclosures, and near-coincidence points inside the interval.
   - **Value: modest.** The theorem stays conditional, and its hypothesis may be vacuous if h_* < h₁.
3. **The explicitable thresholds.** About 1,000–2,000 lines in total, 2–4 months, medium risk.
   - T7 and T8, either as explicit ε_L and γ_1, or as direct tf-admissibility at γ_Υ = 1/100.
   - T4 and T9, deciding the countable sets at the chosen point.
   - This settles four of the eight threshold-type quantities. ε_0, ε_1, h_0 and h_tf remain.
4. **Out of reach in this paper.** T5 and T6 (an explicit mode stability for the gauge-modified 1-form operator at all
   frequencies, enhanced at zero energy), and T2 and T3 (an explicit semiclassical 3b and edge-b theory, which needs
   G1, G2 and G4 closed first). Monograph scale, years.

**If the question is whether the computational point might in fact be admissible:**

- **In the paper's own definition:** no. h = 10⁻⁶ ∉ 𝖧 is decided (§2).
- **The meaningful version** replaces "below thresholds" by "where the conclusions hold". That is, 𝖧 and the gauge
  thresholds are replaced by the set of parameters at which all of these hold:
  - thm:iii-e-1-1 (1)–(4) and (C1)–(C5);
  - prop:iii-d1-4-1 for some γ_(Υ,H);
  - lem:iii-d-7-1 and prop:iii-f1-3-3;
  - z ∉ 𝖹_exc.
- **Deciding the meaningful version would take, in order:**
  1. **An audit.** Check that the proof of thm:settling uses smallness only through those conclusions. Rows
     u1–u5 and the continuity statements (lem:iii-d-5-1 and prop:iii-d-6-1, on compact parameter sets) suggest it
     does. 37:54 ("γ_Υ small") and 46:92 ("small enough for …") should be checked against this. About 1–2 weeks of
     reading.
  2. **The cheap steps:** T4 and T9 at (10⁻⁶, 4·10⁻⁶), and T7 and T8 directly at γ_Υ = 1/100.
  3. **The two research-level certifications:**
     - mode stability of □^Υ_(b₀) at (1/100, 1/100) (T6, direct);
     - thm:iii-e-1-1 at γ_C = 10⁶ without semiclassics (T2 alternative and T3).
- **A cheap first probe** is numerical: compute the quasinormal modes of □^Υ_(b₀) at these parameters over a range of
  l and σ in the closed upper half-plane. It can give evidence only, labelled as a numerical observation, never a
  proof.
