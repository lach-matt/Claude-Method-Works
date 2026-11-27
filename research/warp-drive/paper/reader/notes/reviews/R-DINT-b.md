# R-DINT-b: confirming reading of chapter 71 after D-INT-2

Reader R-DINT-b. Chapter read: `chapters/71-explicit-constants.md` at HEAD bcb6c358 (unchanged since 74074c98; md5
74fb1f976ee3c2c2338cfd4155cf8c34, 4,371 lines, 203 labels). Sources: the six texts and the old chapter at d1509feb;
R-DB-2 §7 (CH-71); R2-DB-b; D-INT-2 and its compare.txt; STATUS.md row "71 M Ch 18" and INTEGRATION.md (R-71, F-71).
Nothing in the repository was changed. Scratch work (byte alignment, exact arithmetic, dependency graph) is under
`.../scratchpad/reader/scratch/r_dint_b/`.

**Verdict: NOT CONFIRMED: 0 Major, 2 minor, 6 nits.** The integer bound on d stands as the chapter states it:
d_acc, d_NM ≤ D_acc < 1.57157·10⁵⁰ and N_NM ≤ 21D_acc + 6 < 3.30029·10⁵¹ (thm:uc-integer). No finding touches it.

---

## Findings

### 1. minor: the moved sentence points to the wrong section for the lower bound (l. 385–386)

*Evidence.* The coordinator's change reads "[[sec:ec-floor]] bounds two of these iterations from below". After the
merge, sec:ec-floor (l. 1250–1294) holds only the description of the iterations, lem:ec-round-loss (a lower bound for
the charge of one round) and lem:ec-level-sum. The bound on the number of rounds is prop:ec-rounds, and the lower bound
for d is thm:loss-d (ii). Both sit in sec:ec-gauge-gap (l. 1380, 1422). Before the merge they were in sec:ec-floor,
which is why "the next section" was right there. So the sentence now sends the reader to a section that does not prove
what it says.

*Fix.* Replace l. 385–386 from "[[sec:ec-floor]] bounds two of these iterations" to the end of the paragraph by:

> numbers of steps of the iterations of the inventory of [[sec:iii-j2-3]]; two of these iterations bound d_acc from
> below ([[lem:ec-round-loss]], [[prop:ec-rounds]], [[thm:loss-d]] (ii)), and at the computational point
> [[thm:uc-integer]] bounds d_acc, d_NM and N_NM from above.

(Rewrap within 121 characters.)

### 2. minor: the forward solution operators at the backgrounds with q do not have split loss (d_F; d_F, d_F) (l. 1555–1557)

*Evidence.*
- l. 1555: "The forward solution operators have split loss (d_F; d_F, d_F), d_F the loss d of [[thm:iii-i-5-3]] and of
  [[cor:iii-h2-5-1]]". Split loss is defined with ‖β‖ ([[eq:ec-split-loss]]), and ‖β‖_k = ‖h‖_(𝒳^k) + |p⃗| +
  ‖q‖_(𝒬^k) (ch. 43 l. 79).
- The proof of lem:cs-elem (e) (l. 3926–3933) bounds ‖h̃‖_(𝒳^m) for h̃ = h + h_rem(q) + h_tot(p⃗) by
  ‖q‖_(𝒬^(m+3)). It charges these families 20,180 + 3 = 20,183.
- So, at those backgrounds, eq:iii-i-5-2 gives split loss (d_F; d_F + 3, d_F). Then l. 1562 "every family other
  than the background terms has c, b ≤ a" fails for them as written.
- R2-DB-b noted this as a side observation and did not count it, because the two texts were separate files. In one
  chapter the two statements now disagree.
- Nothing downstream moves:
  - cstar charges 20,183 in full;
  - with the weakened split loss (d_F + 3; d_F + 3, d_F + 3), which follows because the norms increase with the
    order, c, b ≤ a holds and lem:ec-split-loss (d) applies unchanged;
  - the parenthetical in the proof of prop:ec-upper (l. 1872–1876) is unaffected.
- The statements "the loss of the forward solution operators is at most 20,180" (l. 14, 1433–1434, 1556, 1919) are
  true as statements about [[eq:iii-i-5-2]] with ‖h̃‖ in place of ‖h‖, which is how R2-DB-b read cor:fwd-near-b0.

*Fix.* Replace l. 1555–1557 "The forward solution operators have split loss … [[cor:fwd-near-b0]])." by:

> The forward solution operators have split loss (d_F; d_F, d_F), d_F the loss d of [[thm:iii-i-5-3]] and of
> [[cor:iii-h2-5-1]] ([[eq:iii-i-5-2]]), at most 20,180 ([[thm:fwd-loss]], [[cor:fwd-near-b0]]), at the backgrounds
> h, h + h^(−1)(S) and h + h_tot(p⃗). At h + h_rem(q) + h_tot(p⃗), where ‖h̃‖_(𝒳^m) is bounded through ‖q‖_(𝒬^(m+3)),
> they have split loss (d_F; d_F + 3, d_F), and so (d_F + 3; d_F + 3, d_F + 3), the charge of [[lem:cs-elem]] (e).

(Rewrap the paragraph.)

### 3. nit: the section titles no longer match their contents (l. 1250, l. 1296)

*Evidence.*
- sec:ec-floor is titled "Two long iterations, and a lower bound for d", but the lower bound (prop:ec-rounds,
  thm:loss-d) is in the next section.
- That next section, sec:ec-gauge-gap, holds the chapter's main lower-bound theorem, yet its title is "The constant ε_Υ
  at the computational point".
- A reader who scans the headings for the lower bound on d is sent to the wrong section.

*Fix.*
- l. 1250: "### Two long iterations and the loss of a round {#sec:ec-floor}".
- l. 1296 (first line of the assembly block): "### The constant ε_Υ, and a lower bound for d {#sec:ec-gauge-gap}".

### 4. nit: the paragraph before sec:fwd repeats sec:fwd's first paragraph (l. 377–381 against l. 390–395)

*Evidence.*
- l. 377–381 read: "lose the d of [[thm:iii-i-5-3]], which its proof takes from [[thm:ii-f1-1-1]] in the relaxed form
  of [[rem:ii-f1-7-1]] with d_ℵ = 1 and raises by 5; there d = D_0 + D_1 + d′ + d″ + 1 + 5 ([[eq:fwd-split]]), …".
- Eight lines later, sec:fwd says the same in almost the same words and defines eq:fwd-split.
- The comma before "[[thm:fwd-loss]] shows" leaves three clauses joined by commas.

*Fix.* Replace l. 377 (from "The forward solution operators") to l. 381 ("ℬ̄_*.") by:

> The forward solution operators of [[lem:iii-j2-2-1]] (a) lose the d of [[thm:iii-i-5-3]], which [[sec:fwd]]
> evaluates: [[thm:fwd-loss]] shows that d = 20,180 may be taken, and [[cor:fwd-near-b0]] gives the same value at every
> base point with black hole parameter in ℬ̄_*.

### 5. nit: "carry no value" is stale against chapter 23 (l. 508)

*Evidence.*
- l. 508: "The indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]] come from the closed graph theorem and carry no
  value."
- Since D-INT-1, both statements in chapter 23 carry explicit values, proved by prop:fwd-calculus:
  - ch. 23 l. 1467–1471 (text 7): "M := 200Θ + 98 serves";
  - ch. 23 l. 1071–1072 (text 12): "d_0 = 200Θ + 100 serves".
- This is not circular: the proof of prop:fwd-calculus uses neither statement (checked: prop:ii-a1-2-4 occurs only in
  its statement, l. 895).

*Fix.* Replace l. 508 by: "The proofs of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]] take their indices from the closed
graph theorem, which gives no value; the values stated there are proved here." Keep the rest of the line: "We prove
them again, every derivative counted."

### 6. nit: "Every lower bound of this chapter is a lower bound for d_acc" (l. 1475–1477)

*Evidence.* Read literally, this is false. lem:ec-test-function bounds a resolvent norm from below. eq:ec-gauge-gap
bounds 𝔡_ℳ from below. Neither is a bound for d_acc. The intended statement concerns the lower bounds for d.

*Fix.* Replace it by: "Every lower bound for d_acc in this chapter holds for d_NM and N_NM as well, because
d_NM ≥ d_acc and N_NM increases with d_NM."

### 7. nit: rem:ec-not-evaluated credits def:ec-point with all the numerical choices (l. 4358–4359)

*Evidence.*
- l. 4358 reads "so explicit constants need those choices made with numbers, which [[def:ec-point]] does only at a
  point outside the proved set".
- def:ec-point fixes only the gauge and damping parameters.
- The weights and the free orders and inner products that d depends on are fixed by def:uc-choice and def:cs-choices.
  Both are new in this chapter since the merge.

*Fix.* Replace "which [[def:ec-point]] does only at a point outside the proved set" by "which this chapter does only at
a point outside the proved set: [[def:ec-point]] for the gauge and damping parameters, and [[def:uc-choice]] and
[[def:cs-choices]] for the weights, orders and inner products on which d depends".

### 8. nit: the crosswalk note of rem:ec-other-losses is out of date (crosswalk row 20)

*Evidence.* The note ends "the paragraph now follows sec:fwd". After 74074c98 the paragraph comes before sec:fwd.
Two earlier clauses describe text that the merge removed:
- "what an upper bound for d_NM needs";
- "FWD's loss from thm:iii-i-5-3 / eq:ii-f1-3-3, not evaluated".

*Fix.* In the note:
- replace "; what an upper bound for d_NM needs; FWD's loss from thm:iii-i-5-3 / eq:ii-f1-3-3, not evaluated" by
  "; FWD's loss evaluated in sec:fwd";
- replace "the paragraph now follows sec:fwd" by "remark and paragraph placed at the end of sec:ec-accounted, before
  sec:fwd (74074c98), 'the next section' written [[sec:ec-floor]]".

---

## The checks of the brief

### 1. The merged blocks against their sources: byte-identical

I did my own alignment: difflib on lines, with no junk heuristic. Each source text at d1509feb was aligned against the
whole chapter, independently of the writer's offsets. Line equality on the decoded text is byte equality. The file has
no CR, no tab and no trailing blank, and ends in a single newline.

| text | source lines | chapter lines | result |
|---|---|---|---|
| forward | 6–866 | 388–1248 | identical |
| assembly | 1–184 | 1296–1479 | identical |
| assembly | 186–212 | 1483–1509 | identical |
| assembly | 214–634 | 1511–1931 | identical |
| close | 1–574 | 1933–2506 | identical |
| IS | 1–662 | 2508–3169 | identical |
| SP | 1–604 | 3171–3774 | identical |
| cstar | 1–526 | 3776–4301 | identical |

- The offsets of the forward block are those after the coordinator's move (D-INT-2 lists 354–1214, from before it).
- Source lines not carried:
  - forward 1–4 (the placement comment) and 867–899 (a blank and the comment with texts 7–12);
  - assembly 185 and 213, both blank.
- Texts 7, 8 and 12 sit in chapters 23 (l. 1071–1072, 1467–1471) and 25 (l. 29). Texts 9–11 already read so in
  chapter 26 (l. 1376, 1411).
- So nothing of the six texts is lost.

### 2. The changed sentences: true in place, apart from finding 1

I diffed the chapter outside the eight blocks against the chapter at d1509feb. The diff contains exactly the changes
D-INT-2 lists, the deletions (old l. 435–517, 521–595) and the coordinator's move. I word-diffed the planned texts of
R-DB-2 §7 CH-71 (b), (c), (d) and (e) against the chapter. The only departures are the listed ones and "the next
section" → "[[sec:ec-floor]]".

- **(b), the opening (l. 12–24).** Each claim is in the chapter:
  - 20,180 at b₀ is thm:fwd-loss; at b ∈ ℬ̄_* it is cor:fwd-near-b0.
  - 1.403·10²⁰ and 2.946·10²¹ are thm:loss-d (ii). I redid them in fractions: (1 − 5δ̂ − δ̄)/δ̂² = 4.67759…·10¹⁹,
    so 3R > 1.40325·10²⁰ and 21 · 1.403·10²⁰ = 2.9463·10²¹.
  - 1.2497·10²⁴ and 2.624·10²⁵ are cor:uc-two-offsets (a). R > 4.16598·10²³ at ε_K = 1.6417·10⁻¹⁴.
  - D_acc = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 < 1.57157·10⁵⁰, and 21D_acc + 6 <
    3.30029·10⁵¹, both recomputed exactly. The text says "at one admissible choice", which is the scope of
    thm:uc-integer.
  - "δ by a power of 2 that decreases with d" is prop:ec-delta-cap: δ ≤ 2^(−(32d+9)).
- **(c), rem:ec-point-outside.** prop:ec-rounds says "The same bound holds at every h ∈ 𝖧", and its proof uses h only
  through ε_Υ < δ̂ and ε_ind(h) ≤ δ_50. lem:ec-gauge-gap fixes ε_Υ by (γ_Υ, e_Υ) alone. True.
- **rem:gap-sums.** The new sentences are true:
  - cor:is-flat cites prop:gap-sums for μ♭ (l. 3132–3134);
  - lem:ec-gauge-gap (l. 1333) and lem:sp-roots (l. 3512) use the bounds on 𝔡₀ and 𝔡₁ from its proof;
  - μ_G ≈ 1.6416·10⁻¹⁴ agrees with eq:is-mu.

  Remarks rem:ec-upper-open and rem:uc-offset-d0 also cite prop:gap-sums. No proof depends on them, so the sentence is
  accurate as a statement about results.
- **(e), "raises by 5" with eq:fwd-split.** This matches the proof of thm:iii-i-5-3 (ch. 38 l. 614–631): relaxed
  margin d_ℵ = 1, "d raised by 1", and h ∈ 𝒳^(k+d+5), "d raised by 5". It also matches rem:ii-f1-7-1, where the
  increase is d̄_ℵ = ⌈d_ℵ⌉ = 1.
- **(e), base points.** cor:fwd-near-b0's last sentence gives d = 20,180 at every base point with b ∈ ℬ̄_*. True.
  Finding 4 is about wording only.
- **rem:ec-not-evaluated.** prop:ec-delta-cap bounds λ1 < δ, δ ≤ 2^(−(32d+9)) and ω̃(2δ) ≤ 2^(−(32d+8)). True.
  Finding 7 is a separate, older imprecision.
- **β_Γ (old 71:642, now l. 4348).** β_Γ = ½ min_Γ |q_(z₀)| = 2 at b₀ (ch. 31 l. 206, 489, 494–495), and
  ν_min = 4·2^(−1/2) = 2^(3/2) and q^Γ = 4 agree with ch. 70 l. 1610. Correct notation.
- **The coordinator's move.** rem:ec-other-losses and its paragraph now close sec:ec-accounted, and sec:fwd follows.
  - This is needed: lem:fwd-orders uses lem:ec-theta-in (a), (b), and in this order it comes after it.
  - The forward text's placement comment said "before that remark". That would have split sec:ec-accounted. The
    chosen order reads better, and no text of sec:fwd refers back to the remark.
  - "[[sec:ec-floor]]" is finding 1.

### 3. The non-merged text: every proof step checked

I read l. 1–387, 1250–1295, 1481–1482 and 4303–4371 in full, and every cited result in its chapter.

**sec:ec-point.**
- z = 4·10⁻⁶ and λ_♯ = 15099/10000 (eq:iii-g3-0-1).
- (v_C, e_C) as in eq:iv4-0-1.
- δ_50 is from lem:s14-delta50, and ε_ind(10⁻⁶) = δ_50 from cor:s14-eps-ind-point.
- 𝖧 = (0, h_*) ∖ 𝖹 is open at h_* ≤ 10⁻⁶, so 10⁻⁶ ∉ 𝖧.
- thm:vi-c-2-1 (2) fixes e_Υ and γ_Υ below thresholds.

**sec:ec-gap-sums.**
- eq:ec-sqrt is verified symbolically. Where the lower expression is negative, the inequality is trivial.
- 𝔡₀ = d_c0 and 𝔡₁ = d_c1 (def:iii-i9-gap with μ_c0, μ_c1 of ch. 40 l. 1280).
- δ₂ = z(1 + θ₂)/15 and δ′₁ = 3z(1 + θ₁)/20, with |θ| ≤ z, from eq:s14-theta at u = 3 and u = 2.
- I recomputed every bound of the proof at 60 digits:
  - A₂, w₂, B₂ and 𝔡₁ lie in the stated intervals, and so do the intervals derived from the stated bounds;
  - the 30 triples (g, t, k) are classified completely (17 + 3 with y < 0, 3 with y = 0, 7 with y > 0);
  - all six table rows follow from the stated bounds. For instance, row 1 gives y/𝔡₁ ∈ (4470303.84942290,
    4470303.84942692) and excess ∈ (5.019098·10⁻⁸, 5.019232·10⁻⁸). The true least value is
    λ_♯ + 4470304𝔡₁ − 3 = 5.01914·10⁻⁸;
  - 5.0190·10⁻⁸/δ_50 = 2.585.
- rem:gap-sums:
  - 2 ∈ Λ through 2 + π_1ℰ_col;
  - the three windows are those of def:iii-i10-1-3;
  - thm:settling takes ε_K < ε_+ < ε_ind (ch. 03 l. 280).

**sec:ec-accounted.**
- def:ec-accounted-loss matches lem:iii-j2-1-2 (a)–(f). d_NM and N_NM = 21d_NM + 6 match eq:ii-g-2-5 and ch. 46
  l. 1251–1253.
- lem:ec-theta-in (a):
  - I redid every adjoint identity: (ρ∂_ρ)^† = −ρ∂_ρ + 4 for ρ⁻⁵dρ dω; (ρ²ρ∂_ρ)^† = −ρ²ρ∂_ρ + 2ρ²;
    (ρ²(ρ∂_ρ)²)^† = ρ²((ρ∂_ρ)² − 4ρ∂_ρ + 4); and ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ) is self-adjoint;
  - Im_h(−ρ²Aρ∂_ρ) = iρ²Re_h(A)ρ∂_ρ + ρ²C^∞;
  - the intersection ρ³Diff²_b ∩ ρ²Diff¹_b = ρ³Diff¹_b holds;
  - the symbol at (ξ, η) = (−2, 0) is −2Re_h(A);
  - the eigenvalue argument gives ϑ_in ≥ −2 Re μ.
- lem:ec-theta-in (b):
  - in 4 dimensions, −Δ = ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ + Δ_𝕊³) (checked), so □̄ contributes nothing to A;
  - the ∂_r-coefficients follow from lem:iii-f-2-1 (2) with d|x| for dt_*;
  - dt_* + 2d|x| = dt̄ + d|x|;
  - the kernel has dimension ≥ 15 − 10;
  - the transfer to N_tf follows sec:i-c-4-1 (a) and eq:i-c-1-3.
- lem:ec-closed-forms, checked part by part against the proofs it reads:
  - (a) is lem:ii-g1-4-1.
  - (b) is ℓ_a + ℓ̃ of cor:ii-g1-4-2 with s_c ≥ 0.
  - (c) is the proof of prop:ii-g1-4-7, with 𝗋_in − 𝗋_out = (ϑ_in/2 + 5/2 + ε/2 − β_scf)_+.
  - (d): lem:i-a-7-1 gives 𝗋 = 𝗋_in at R_in, and 𝗋_out < −½ < 𝗋_in.
  - (e): m(s) = 2 + ⌈max(0, −s)⌉ + j with j = ⌈½ − s⌉ (lem:iii-g1-2-1 (iii)); then ⌈ℓ_I − Re ϰ⌉ + 2 steps of loss 2
    (Step 5 (iii)). Every case of the 12 and 11 bounds was redone, including Re ϰ ∈ [2 − δ_ι, 2).
  - (f): l = 2⌈ℓ_I⌉ + 10 (lem:iii-g3-2-2) and l′ = l + sup d (prop:iii-g3-2-4). The right inverse u ↦ f costs 2 (the
    proof of lem:iii-g3-3-5), plus a finite-rank part bounded at order sup d_ι. 8 + 10 + 12 = 30.
  - (g): the count 1 + n_ι + 2(n_K + ⌊β_K⌋), and the general E_I case through β′_K ∈ (B, ⌊B⌋ + 1), follow
    prop:iii-a-4-2's proof step by step. Part (2), n_ι + n_K + ℓ_F with the harmless commutator terms, is checked too.
  - (h): prop:ii-g1-3-5 (1) at output weights (β_ι + 1, β_K + 1) gives ⌈(β_K + ½ + ε)_+⌉; prop:ii-g1-2-8 (2) at
    β = γ + 1 gives ⌈γ + ½⌉.
- rem:ec-other-losses: every bullet matches lem:iii-j2-2-1 (a)–(g) and the printed losses of prop:ii-g1-3-3 (2) and
  prop:ii-g1-3-5 (1), (2). ℓ_4 is a closed form in the orders (lem:ii-g1-4-3 proof), and max(2, d_BG) is tame by
  monotonicity.

**sec:ec-floor.**
- The three bullets match the proofs:
  - thm:iii-i14-3-1 Step 2 (β_(K−1) > 4, R_qu in G̃);
  - lem:iii-i8-3-2 Step 3.4′ (τ_0 = 2 + ε_g − 2ε, τ_(i+1) = τ_i + ε_g − ε, "while τ_i ≤ α − ε′");
  - prop:iii-i13-2-1 Step 4 (κ_3 = 1 + η_2 − 2ε, increments ε_g − ε).
- lem:ec-round-loss (b): λ_♯ ≤ Re ϰ_0 < 2 − δ_ι gives ℓ_I − Re ϰ_0 ∈ (1, 1.9901], so d_ι = 11 and the round costs
  ≥ 15.
- lem:ec-level-sum is correct as stated.

**sec:ec-linear.** Every constant agrees with chapter 70:
- I = {6/5 ≤ r ≤ 4};
- 11.477 is thm:band;
- 283.06, 305.31 and 308.46 are cor:band-one-derivative, with ψ = 2ηz², z = 1 − 2/r² (zero at r² = 2), unweighted
  at l = 1;
- 1.002659 at κ_Γ = 2^(−3/2) with h_0 ≤ 1 is lem:rb-interpolation.

The proof of lem:ec-test-function is correct (uniqueness in prop:resolvent-outgoing (a)). In
rem:ec-lower-bounds-observed, the quotients prop:band-points / lower bounds are 19.73, 18.73, 40.75, 49.54, 67.46 and
93.44, all below the printed 19.8 … 93.5. The percentages 39.8–46.4 against rem:rb-large-frequency-observed give
"about 40 to 46".

**Consistency.**
- The greps of D-INT-2 find nothing left: "No upper bound", "raises by 6", 7.959, 1.671, 2.6532, 7.666, 46,236, 8.41,
  "is an observation", ec-integer.
- My own greps also find nothing: 2.65327, 7.9598, 4.624, 9.710, 4.45, 1.065, 188·10⁻¹⁰, 19·10⁻⁹, "not evaluated"
  (outside its label), 1.386, 1.29238.
- 1.403·10²⁰ occurs at l. 17, 1438, 1474–1475 and 1504 only, where it holds.
- No `[[pending:` marker.
- Apart from findings 1–2 and 5–7, no non-merged statement contradicts a merged one:
  - (d) of lem:ec-closed-forms, a lower bound, against prop:uc-ltf and lem:ec-tf-loss (ℓ_tf = max(1, s − 1) ≥ 1);
  - max(2, d_BG) against prop:uc-dbg and lem:cs-elem (d) (11);
  - d_ι + 2 and 30 against lem:cs-elem (h);
  - lem:ec-round-loss (b) (≥ 15) against lem:cs-base (≤ 469).

**Order of the argument.**
- I built the citation graph of the statements and proofs (remarks excluded).
- In the non-merged text, every proof cites only earlier results: lem:ec-closed-forms uses lem:ec-theta-in, and
  lem:ec-round-loss uses lem:ec-closed-forms and rem:ec-other-losses.
- The forward references in the non-merged text are in the opening and in remarks.
- The merged blocks keep R-DB-2 §7 (a)'s layout. thm:uc-integer (sec:uc-close) is proved with results of sec:is,
  sec:sp and sec:cs, which come after it, and the text says so (l. 1944–1947, 2496). None of those results uses
  thm:uc-integer.
- The apparent cycles the graph shows all come from statements that cite in passing, not from proof steps:
  - thm:loss-d's closing paragraph cites cor:uc-two-offsets and thm:uc-integer;
  - lem:ec-tf-loss cites prop:uc-ltf parenthetically;
  - prop:fwd-calculus's note cites lem:fwd-box.
- No circular step.

**Structure.**
- The section order is: opening, point, gap sums, accounted loss with rem:ec-other-losses, forward loss, the two
  iterations, ε_Υ with the lower bound, δ and λ1, upper bound, its inputs, IS, SP, cstar, linear theory.
- It reads as one chapter, and the opening announces it.
- rem:ec-other-losses is well placed.
- The defects are findings 1, 3 and 4.

### 4. The coordinator's applied fixes from R2-DB-b

I word-diffed each proof at d1509feb~1 against d1509feb. The only changes are these, and each is R2-DB-b's text:
- cstar: "= T_12" → "< T_12" (now l. 4250–4251). True, since T_12 − (C_lev − 11 + I_lev + X_12) = 11.
- forward:
  - "are no sites" → "are not sites" (l. 1228);
  - "satisfy [[eq:iii-i-5-2]]" → "satisfy [[eq:iii-i-5-2]], in the form of [[lem:iii-j2-2-1]] (a)," (l. 1189–1190).
- assembly, texts 1, 3, 4 and 5 (text 2 was optional and is not applied):
  - l. 1433–1434: "at every base point ([[thm:fwd-loss]] at b₀, [[cor:fwd-near-b0]] at b ∈ ℬ̄_*)";
  - l. 1467: "…, [[thm:fwd-loss]] and [[cor:fwd-near-b0]]";
  - l. 1555–1557: "and of [[cor:iii-h2-5-1]] … ([[thm:fwd-loss]], [[cor:fwd-near-b0]])";
  - l. 1919–1920: "([[thm:fwd-loss]], [[cor:fwd-near-b0]])".

All four citations are true. Finding 2 concerns the split-loss claim beside text 4, not the citation itself.

### 5. Contract

- `crosswalk/71-explicit-constants.tsv`:
  - 203 rows of 4 fields each;
  - the label column equals the chapter's label sequence exactly (diff empty);
  - the 173 merged rows each point to `…/P-U71-<name>.md@d1509feb:<line>`, and that line of the source carries the
    label (173 of 173 checked);
  - finding 8 is a stale note.
- No label is defined twice in chapters/.
- `python3 lint.py --chapters`: 62 files, 4,573 labels, **0 hits**. Chapter 71 alone: 1,366 hits, all "undefined
  label" across chapters.
- `python3 assemble.py --check`: **problems 0**.
- Lines: at most 121 characters (code points).
- 72 lines start with "- " or "|" after a non-blank line. All are list items or table rows (l. 99–115, 357–375,
  1255–1264, 1338–1357, 1959–1974, 2960–2989); none is a wrapped line.

---

## Observations outside the count

1. R2-DB-b's nit 2 is not applied. That nit was optional: add the order 𝗌 of (B4) (that of lem:fwd-orders) to
   def:cs-choices. thm:uc-integer still names only def:uc-choice and def:cs-choices, and the choice is made in passing
   in the proof of lem:cs-elem (e) (l. 3928–3929). The coordinator may wish to decide it explicitly.
2. In chapter 43 (the other reader's), lem:iii-j2-2-1 (a) ends "and [[eq:iii-i-5-2]] with ‖β‖ in place of ‖h‖". At
   the backgrounds with q this holds at the order k + d + 3 in ‖β‖, as lem:cs-elem (e) shows. This is the
   chapter-43 side of finding 2.
3. lem:ec-tf-loss (l. 1644) and prop:uc-ltf (l. 2095) prove nearly the same statement twice, once from each proof
   text. This is harmless, and both are confirmed texts.

## Verdict for chapter 71

**NOT CONFIRMED: 0 Major, 2 minor (findings 1, 2), 6 nits (findings 3–8).** The merged blocks are byte-identical to
their sources, nothing of the six texts is lost except the forward comments, and the coordinator's R2-DB-b fixes are
exact.

**The integer bound on d stands as the chapter states it:** d_acc, d_NM ≤ D_acc < 1.57157·10⁵⁰ and
N_NM ≤ 21D_acc + 6 < 3.30029·10⁵¹ at one admissible choice. Against it, d_NM ≥ d_acc > 1.2497·10²⁴ for every
admissible choice with the index sets as constructed, and d_acc > 1.403·10²⁰ in general at the computational point.
