# R-DB-1: first reading of P-U71-cstar.md, with thm:uc-integer and rem:uc-missing

Reader R-DB-1. Scope: `proofs/P-U71-cstar.md` (489 lines) in full, and `thm:uc-integer`, its proof and
`rem:uc-missing` in `proofs/P-U71-close.md` (lines 500–559). Nothing in the repository was changed. Arithmetic was redone
in exact integers (plain Python `int`/`Fraction`) under the session scratchpad.

**Verdict: NOT CONFIRMED: 2 Major, 8 minor, 5 nit.**

**Does the integer bound on d stand?** Yes, once findings 1 and 2 are fixed. Every integer and inequality of
`prop:cs-cstar` and `thm:uc-integer` checks exactly. The computed bound for c_* is
643,676,388,469,322,172,480,826,383,357,103,759, which sits 3.61·10³⁰ below C_*. Finding 1 can be closed by a free
choice that changes no printed number, or by adding at most 2.06·10¹⁰ charges, which the margin absorbs. Finding 2 needs
a stated extension of `thm:fwd-loss` to base points with b ≠ b₀. Its proof plausibly carries over unchanged, but it is
not written. No other finding changes a printed integer. As written, the proof of D_acc is incomplete at these two
places.

---

## Findings

### 1. Major: the base inside thm:iii-i11-4-1 has uncounted transition-face rounds (cstar l. 423–426)

*Evidence.* `lem:cs-rest` bounds the base that `thm:iii-i11-4-1` applies by
"20,183 + 1,914 + I_base by lem:cs-iterations (b) (its forward solution, and the 1,914 of the base ...)". The 1,914
contains item (6), lem:iii-i8-3-2 from α_0 to α_1 at 497. Item (6) assumes that this level step has no transition-face
round: "as τ_0 = 2 + ε_g − 2ε exceeds α_1 − ε′, α_1 − 2 < ε_K < ε_g − 2ε" (l. 417–418). That holds for the α_1 of Step 1 of
thm:iii-i14-3-1, which def:uc-choice places in (2, α − 2) ⊂ (2, 2 + ε_K). The base of thm:iii-i11-4-1 is at a different
level. Its proof says "Fix an admissible α′ ∈ (2, 3)" (ch. 41 l. 966), and neither def:uc-choice nor def:cs-choices fixes
this α′. For α′ − ε′ ≥ τ_0, Step 3.4′ of lem:iii-i8-3-2 from α_0 to α′ runs up to (α′ − 2)/Δτ + 1 < 6,847,261,001 rounds,
each charged up to ℓ⁺_tf + 2 = 3 (lem:ec-round-charges (a)). lem:cs-iterations (b) charges rounds of prop:iii-i5-2-1,
steps of prop:iii-i2-5-1 and windows, but no transition-face rounds. So these rounds are counted nowhere.

*Fix (no printed number changes).* Add to def:cs-choices, after (e):

> (f) in the proof of [[thm:iii-i11-4-1]], an admissible α′ ∈ (2, 2 + ε_g − 2ε), and in the proof of
> [[prop:iii-i8-4-1]] at α′ an admissible α_0 ∈ (2, α′);

Add to the justification paragraph:

> (f): that proof takes any admissible α′ ∈ (2, 3), the admissible levels are dense ([[sec:iii-i8-1]]), and
> α′ − α_0 < 1 < a_K − 2, so [[prop:iii-i8-4-1]] at α′ has one level step.

In l. 424, replace "applies [[prop:iii-i8-4-1]] at α′ ∈ (2, 3), a base," with:

> applies [[prop:iii-i8-4-1]] at the level α′ of [[def:cs-choices]] (f), a base whose level step α_0 → α′ has no
> transition face round (τ_0 = 2 + ε_g − 2ε > α′ − ε′, as in (6) of Step 1),

*Alternative.* Add 3 · 6,847,261,001 = 20,541,783,003 to T_11. This changes the printed sums of eq:cs-cstar but not C_*.

### 2. Major: the forward charge 20,183 is proved only at b₀, but it is used at every b ∈ ℬ̄_* (cstar l. 98, 129–133)

*Evidence.* `lem:cs-elem` (e) charges "every application" of the forward solution operators of lem:iii-j2-2-1 (a) 20,183.
`lem:cs-levels`, `lem:cs-base` and `lem:cs-rest` then claim their bounds "at a rotating black hole parameter" and for
ℛ(U), whose base point Ψ(U) has the parameter b of U ∈ ℬ_*. The proof of (e) begins "By [[thm:fwd-loss]],
[[eq:iii-i-5-2]] holds with d = 20,180 for g = g₀ + h". thm:fwd-loss is stated for thm:iii-i-5-3, which is at b₀, and
lem:fwd-orders is stated "For P_0 = 2L_(b₀)". At b ≠ b₀, lem:iii-j2-2-1 (a) takes the operators from cor:iii-h2-5-1. Its
proof is that of thm:iii-i-5-3 with P_0 := 2L_b and thm:iii-h2-4-1, an existence statement ("There are ε_0 > 0 and
d ∈ ℕ"). Nothing in sec:fwd, ch. 71 or the assembly evaluates that d; a grep finds no mention of cor:iii-h2-5-1 or
thm:iii-h2-4-1 there. The extension is plausible: by (B4) of sec:iii-h2-0 the order 𝗌 used at every b is the one built
for 2L_(b₀), so d′ = 10 and d″ = 11 are unchanged, and the counts behind D_0 and D_1 are structural. It is still not
written. Steps 0 and 1 of c_0 and the base contain forward solutions at the base point's b, so d_acc at b ≠ b₀ is not
bounded without it.

*Fix.* Add after the proof of thm:fwd-loss, in the forward chain:

> **Remark {#rem:fwd-near-b0}** (The forward loss near b₀.) At every b ∈ ℬ̄_*, [[cor:iii-h2-5-1]] holds with
> d = 20,180.

Prove it by running sec:fwd with P_0 := 2L_b and the order 𝗌 of (B4): its thresholds hold at b with ϑ_ℋ < 9/4 on ℬ̄_*
(def:cs-choices (a)), and its counts do not involve the values of the coefficients. Then add to the proof of
`lem:cs-elem` (e), after its first sentence:

> At a base point with parameter b ∈ ℬ̄_* these operators are those of [[cor:iii-h2-5-1]], for which d = 20,180 by
> [[rem:fwd-near-b0]].

The ec-split-loss paragraph of P-U71-assembly and thm:loss-d (i) cite thm:fwd-loss in the same way and need the same
citation. Those are outside this scope and are reported for the coordinator.

### 3. minor: lem:cs-sum (b) states a weaker bound than the paragraph after it uses (cstar l. 28–43)

*Evidence.* (b) concludes "at most A_M + A_ℓ + 11". The functionals ℓ_i of an elimination are read from M(e), so the
maps that give them contain the applications of M, and A_ℓ ≥ A_M. The paragraph at l. 42–43 and every later use
(lem:cs-rest items (3), (5), (6): "11 + 0 + 497 = 508") need "each counted once, plus 11", which is A_M + 11. The
proof shows max(A_M, A_ℓ, A_M + 11), and this max gives A_M + 11 when A_ℓ ≤ A_M. The statement does not.

*Fix.* Replace the conclusion of (b) by:

> Then e ↦ M(e) + Σ_i ℓ_i(e)v^i is assigned at most max(A_ℓ, A_M + 11); in particular at most A_M + 11 when each ℓ_i
> is a coefficient functional (charge 0) of the output of maps whose applications are among those of M.

In the proof, replace "≤ A_M + A_ℓ + 11" by "= max(A_ℓ, A_M + 11)".

### 4. minor: the choice N := 5 is not admissible for prop:ii-g1-3-5 (cstar l. 56, 70–71, 181–183, 197–199)

*Evidence.* lem:iii-i2-4-1 and cor:ii-g1-4-5 reach the weights (·, N, N) through prop:ii-g1-3-5 (1) and (2) at K-weight
N. prop:ii-g1-3-5 asks "β_K ∈ (0, ∞) ∖ ℕ" (ch. 29 l. 885), and 5 ∈ ℕ. So the charges computed at N = 5 ("⌈N − ½ + ε⌉ = 5",
"β′ = ... = 5", "ℓ_3 = 1 + ⌈(5 − ½)_+⌉ = 6") come from applications outside that hypothesis. At N = 21/4 every one of
these numbers is unchanged (checked exactly: 5, 5, 6, 20, 30), and 21/4 still exceeds every target weight (3 + η_2 at
ι⁺, α − ε < 5 at K⁺).

*Fix.* In def:cs-choices (c), replace "the weights N := 5 of u_hi" with "the weights N := 21/4 of u_hi". In the
justification of (c), add "with N ∉ ℕ, as [[prop:ii-g1-3-5]] asks". In the proof of lem:cs-transforms (c), replace
"β′ = max(N, N − (3/2 − 2ε)) = 5; the loss ⌈(3/2 − δ)_+⌉ + ⌈(β′ − ½)_+⌉ is 0 + 5" with
"β′ = max(N, N − (3/2 − 2ε)) = 21/4; the loss ⌈(3/2 − δ)_+⌉ + ⌈(β′ − ½)_+⌉ is 0 + ⌈19/4⌉ = 5", and replace
"ℓ_3 = 1 + ⌈(5 − ½)_+⌉ = 6" with "ℓ_3 = 1 + ⌈19/4⌉ = 6". In (e), replace "(charge ⌈N − ½ + ε⌉ = 5)" with
"(charge ⌈19/4 + ε⌉ = 5)". (N := 9/2 also works and lowers the charges, to 4, 5, 18 and 28.)

### 5. minor: the reason given for charging E^ν 11 is not a tameness argument (cstar l. 126–127)

*Evidence.* "The errors E^ν are bounded by C|b − b₀||W| in a fixed seminorm (lem:s25-p6), so they are charged at most 11
as well." A bound in one fixed seminorm gives smallness, not a bound at every order k. The right reason is the structure
of E^ν in lem:s25-p6: E^ν(W) = L_(h,p⃗)(h^(b₀)_ν − h^b_ν)(W) + δ*_(g_0,E_C)(ϑ^(b₀)_(ν,♯) − ϑ^b_(ν,♯))(W).

*Fix.* Replace the sentence with:

> The errors E^ν(W) = L_(h,p⃗)(h^(b₀)_ν − h^b_ν)(W) + δ*_(g_0,E_C)(ϑ^(b₀)_(ν,♯) − ϑ^b_(ν,♯))(W) ([[lem:s25-p6]]) are
> differential operators of order at most two with coefficients polynomial in the background, applied to fixed sections
> and linear in the finite-dimensional W; the proof of [[prop:uc-dbg]] applies to them, and they are charged at most 11.

### 6. minor: lem:iii-a-1-4 makes two small choices per step, and their bound is not stated (cstar l. 145–148)

*Evidence.* "each step of which raises the weight by at least ¾ when its small number is taken at most ¼". In the proof
of lem:iii-a-1-4, a step goes from α to min(β, α + 1) − δ″, where δ″ is the decrease that avoids roots on the line, and
the next step starts at γ − δ′. The raise is 1 − δ′ − δ″, so it is at least ¾ only if δ′ + δ″ ≤ ¼. If each is only at
most ¼, the raise is at least ½, up to 6 steps can occur, and lem:iii-i11-2-1 is charged 13, not 9. This is also a free
choice that def:cs-choices does not list.

*Fix.* In l. 147, replace "when its small number is taken at most ¼" with "when its two small numbers, the decrease of
γ and δ′, are taken with sum at most ¼ ([[def:cs-choices]] (g))". Add to def:cs-choices:

> (g) in each application of [[lem:iii-a-1-4]] in [[lem:iii-i11-2-1]], the decrease of γ and the number δ′ of its proof
> with sum at most ¼;

The justification is that both are arbitrary small positive numbers, off a set that is discrete in every strip.

### 7. minor: X_12 = 4k̄_max + 24 is not derived (cstar l. 389, 427–439)

*Evidence.* The proof lists five transforms: (vi) 4k̄_max + 4 + 5, (viii) 5 and 5, (ix) 5 and 5. Their sum is
4k̄_max + 29, not 24. The bound X_12 = 4k̄_max + 24 is valid only by the rule that a sum is charged its largest part: the
pieces (i)–(ix) are summands of u, so the largest of these charges, 4k̄_max + 9, bounds them. The text does not say this.

*Fix.* At l. 438–439, replace "So [[thm:iii-i12-3-1]] is charged at most C_lev − 11 + I_lev + 4k̄_max + 24 ≤ T_12." with:

> The pieces (i)–(ix) are summands of u, so by [[def:ec-accounted-loss]] they are charged the largest of these charges,
> 4k̄_max + 9 < X_12; so [[thm:iii-i12-3-1]] is charged at most C_lev − 11 + I_lev + X_12 = T_12.

### 8. minor: why Step 4 adds no further application of thm:iii-i11-4-1 is not stated (cstar l. 11, 421–426, 482)

*Evidence.* Step 4 of thm:iii-i14-3-1 uses "p⃗′_0 = p⃗′_(h,p⃗)(G̃_0)" and "thm:iii-i12-3-1 with F = G̃_0 (Step 4′)" at the
final W⃗′^rot. Read literally, it re-applies thm:iii-i11-4-1 and thm:iii-i12-3-1 after W⃗′^rot is fixed. A chain would
then carry 2T_11 + 2T_12, and C_* would rise to about 8.6·10³⁵. The bound 11 + T_11 + 2T_12 holds because G̃_0 is affine
in the finite-dimensional W⃗′^rot and both theorems are linear in F. Step 4 therefore reuses the applications of
Step 4′, with W⃗′^rot entering through a finite-rank assembly (reading (a)). Also, the 11 of Step 4′ covers the whole
forcing G̃_0 = F − Δ_q(p⃗′) − R_q u − Σ f^ν(W′_ν), a sum of background terms, and not only the f^ν. Finally, l. 11 and
l. 482 say that c_0 "contains" three runs of the top level; it is the bound that counts three runs.

*Fix.* At l. 421–423, replace "Step 4′ subtracts the sources f^ν(W′_ν) of the rotation rows (11), identifies ..." with:

> Step 4′ forms G̃_0 = F − Δ_q(p⃗′) − R_q u − Σ f^ν(W′_ν), a sum of background terms (11), identifies ...

After "We charge each in full." insert:

> G̃_0 is affine in the finite-dimensional W⃗′^rot, and [[thm:iii-i11-4-1]] and [[thm:iii-i12-3-1]] are linear in F; so
> the applications in Step 4 are those of Step 4′, with W⃗′^rot entering by a finite-rank assembly, and no further
> application of [[thm:iii-i11-4-1]] lies on a chain.

In l. 11, replace "which contains three runs of the top level" with "whose bound counts three runs of the top level".
In l. 482, replace "three runs of the top level that c_0 contains" with "three runs of the top level counted in the
bound for c_0".

### 9. minor: rem:cs-sharpness misstates the excess of C_* over 6N_ι (cstar l. 481)

*Evidence.* "Of C_*, all but less than 1.74·10²⁸ is 6N_ι." Exactly, C_* − 6N_ι = 3,628,919,841,642,544,595,212,800,000,024
≈ 3.63·10³⁰. It is the bound of eq:cs-cstar that exceeds 6N_ι by 17,389,163,815,025,421,596,157,103,783 < 1.74·10²⁸.

*Fix.* Replace "Of C_*, all but less than 1.74·10²⁸ is 6N_ι:" with "Of the bound of [[eq:cs-cstar]], all but less than
1.74·10²⁸ is 6N_ι:".

### 10. minor: thm:uc-integer states a level bound that the cited lemma does not give (close l. 513–514, 531–532)

*Evidence.* The statement says "1 + n_ι ≤ c(β) ≤ 2N_ι + N_Λ + 529 ... ([[lem:cs-levels]])", and the proof says "the
statements at the levels above 3 are lem:uc-fourier-count and lem:cs-levels (b), with N̄_Λ ≥ N_Λ". lem:cs-levels (b)
gives c(β) ≤ 2N_ι + N̄_Λ + 529. Since N̄_Λ ≥ N_Λ, the bound with N_Λ does not follow from it; the inequality runs the wrong
way. The N_Λ form is true, because the proof of lem:cs-fourier (b) gives the Step 7 charge N_ι + N_Λ + 2, but neither
statement says so. The intro of the cstar file (l. 10) has the same N_Λ form.

*Fix (simplest).* In close l. 514, replace "c(β) ≤ 2N_ι + N_Λ + 529" with "c(β) ≤ 2N_ι + N̄_Λ + 529 = C_lev". In close
l. 532, replace "and [[lem:cs-levels]] (b), with N̄_Λ ≥ N_Λ" with "and [[lem:cs-levels]] (b)". In cstar l. 10, replace
"at most 2N_ι + N_Λ + 529" with "at most 2N_ι + N̄_Λ + 529". (Alternatively, keep N_Λ and cite "the proof of
[[lem:cs-levels]] (b), in which the proof of [[lem:cs-fourier]] (b) gives the Step 7 charge N_ι + N_Λ + 2".)

### 11. nit: the tf-exponents of the prop:iii-g4-4-4 pieces are described imprecisely (cstar l. 257)

"tf-exponents α_0 − 2 + j plus ℕ₀". By Step 1.1 of the proof of prop:iii-g4-4-4, u has the tf-index set
α_0 − 2 + ((0, 0) ∪ ℰ_ind), and the G^exc term adds 2 and α_0. Only the lower bound Re ≥ 1 is used, and it holds.
*Fix:* replace "α_0 − 2 + j plus ℕ₀, of real part at least 1" with "α_0 − 2 + j + ((0, 0) ∪ ℰ_ind) and 2 + j
([[prop:iii-g4-4-4]], Step 1.1 of its proof), of real part at least 1".

### 12. nit: "class roots" is too narrow at l. 271

The roots of the table with −1 < μ < 0 include the □^Υ rows (sl, l + j), for instance (0, 2) with {−μ} ∈ (0, ¼). These
are not class roots. The fact used is d(Re μ, ℤ) ≥ ε_ind for every non-integer root, eq:iii-f1-2-2. *Fix:* replace
"those with −1 < μ < 0 are class roots with −μ ≥ ε_ind > ε_K" with "those with −1 < μ < 0 have −μ ≥ ε_ind > ε_K by
[[eq:iii-f1-2-2]]".

### 13. nit: lem:iii-a-3-3 is charged 0 in lem:cs-elem (a), but 1 per step in lem:ec-closed-forms (g) (cstar l. 82, 109–110)

lem:iii-a-3-3 occurs only inside prop:iii-a-4-2, whose loss formula already counts its one-factor steps (ec-closed-forms
(g): "each one-factor integration step by lem:iii-a-1-2 or lem:iii-a-3-3 costs one"). The 0 is never used, but it
contradicts that count. *Fix:* delete "[[lem:iii-a-3-3]]," from (a) at l. 82, and delete "; [[lem:iii-a-3-3]] is an
integration of the kind of [[lem:iii-a-1-2]], one factor at a time" from its proof.

### 14. nit: lem:cs-transforms (e) treats prop:ii-g1-3-3 (1) and (2) as parallel without saying so (cstar l. 197–199)

"(charges 1 and 3) ... so at most 3 + 2 + 5". The 3 is the largest of the two charges; the two maps act on the two
frequency ranges of one sum. *Fix:* replace "(charges 1 and 3)" with "(charges 1 and 3, on the two frequency ranges of one
sum, so at most 3)".

### 15. nit: the row term of Step 3.5 is not listed in lem:cs-levels (a) (cstar l. 305–316)

Step 3 runs Steps 3–3.3 of prop:iii-i6-2-1, and Step 3.5′ uses the assembly eq:iii-i6-2-8. That assembly contains the row
term (U_r, B_r, Σ_r) of Step 3.5, fixed sections L̃_b(σ)⁻¹(0, E_k) times the coefficients e_k(σ), with charge 0. It is
listed for Step 3.4′ but not for Step 3.5. *Fix:* after "and [[eq:iii-i8-3-3]] is a sum" add "; so is [[eq:iii-i6-2-8]],
whose row term of Step 3.5 is of the same kind (0)".

---

## The three readings the writer asks to confirm

**(a) Finite-dimensional parameters enter as finite-rank assemblies, charged by their largest part.** This is right.
def:ec-accounted-loss assigns "a sum, a finite-rank assembly or a family with several components the largest of the
losses of its parts". lem:iii-j2-1-2 (c) proves the matching tame bound: a functional bounded in a low norm times
sections tame with loss d is tame with loss d. The proof of prop:ec-upper reads the parameters this way (P-U71-assembly
l. 547–548). The rewriting is an identity, not a choice of estimate: by linearity and the uniqueness of forward solutions,
the forward solution for F − D_(p⃗)P(p⃗′) is the solution for F plus Σ p′_i times the solutions for the fixed directions.
It is worth stating this once, where the reading is first used: in def:ec-accounted-loss, or at the start of sec:cs.
lem:cs-sum (b) should then be stated as in finding 3.

*If (a) were wrong*, each elimination would be a composition. In the base, cor:iii-i4-4-3 (the boost S″), cor:iii-i7-4-6
(ḃ and Ṡ⁽⁰⁾_1) and the step of prop:iii-i8-4-1 each feed a forcing computed from an earlier output into a fresh
application of prop:iii-i4-4-1 (1) or prop:iii-i5-2-1. The N_b + 1 steps of prop:iii-i2-5-1 and the N_b rounds of
prop:iii-i5-2-1 would then recur several times along one chain: at least twice from cor:iii-i4-4-3 inside cor:iii-i5-2-2
and again for G(S⃗) in prop:iii-i8-4-1. So N_b and N_b + 1 in eq:ec-upper would be too small by that multiplicity. The
level eliminations would do the same: level k + 1 would re-solve from F through Step 0, the base and levels 1, …, k. The
multiplicity of c(β_k) would then grow geometrically in k, and no bound of the form eq:ec-upper would follow.

**(b) c_0 is overcounted by three full runs of the top level.** This is right, given (a). The bound charges
thm:iii-i11-4-1 once (T_11, with one run of lem:iii-i11-3-2 at α) and thm:iii-i12-3-1 twice (2T_12, each with
C_lev − 11 + I_lev). Under (a), thm:iii-i12-3-1's Step 0 is the decomposition of the run in thm:iii-i11-4-1 (it reads "As
in the proof of thm:iii-i11-4-1"), and Step 4 reuses Step 4′, because G̃_0 is affine in W⃗′^rot. So at most one run
beyond the levels lies on a chain, and charging three is an upper bound. The text must say this, though (finding 8).
Under a literal reading, Step 4 would re-run thm:iii-i11-4-1 and thm:iii-i12-3-1 and need 2T_11 + 2T_12. That would raise
C_* to about 8.6·10³⁵ and D_acc to about 2.1·10⁵⁰. At a rotating b, Step 4′ is not used (sec:s23-base-points (2)), and
Step 4 is cor:iii-i15-2-10, about T_12, so the bound is again an overcount.

**(c) lem:iii-a-1-4 is charged although neither lem:iii-j2-2-1 nor rem:ec-other-losses lists it.** This is right.
lem:iii-i11-2-1 asserts the expansion û ∈ H^(∞,(E′,q′−2)), and the tame bound in that partially polyhomogeneous norm is
part of the construction. lem:iii-j2-2-1 lists only L̃_b(0)⁻¹ (loss 1), which gives the conormal order q − 2, so the
expansion must be charged. It is a regularity statement in the sense of lem:iii-j2-1-2 (f). Each of its steps applies
A − N(A) and the commutator term A(χ̃u) − χAu, both of order 2 with fixed coefficients, and then the Mellin inversion,
which by (E1)–(E2) gains the two orders back. So 2 per step is a valid upper bound, possibly not sharp. The step count is
4, under finding 6.

---

## The Step 7 count of prop:iii-i11-3-1 (lem:cs-fourier (b)): confirmed

*n_ι = 0.* In prop:iii-a-4-2 (2), E_ι = E_tf + 1 and β_ι = β′_+ < 3/2, so n_ι counts the pairs of E_tf of real part at
most β′_+ − 1 < ½. Every tf-exponent of a counted piece has real part at least 1:

- û_0 has exponents in (ℰ^♭ − 1) ∪ (1 + ℰ_col) ∪ (2, ·) plus ℕ₀, all ≥ 1.
- σ^jû_j, j ≥ 1, has exponents ≥ q_j − 2 + j ≥ 1 + η_1.
- The pieces of prop:iii-g4-4-4 have exponents ≥ Re α_0 − 2 + j ≥ 1 (finding 11 corrects the description, not the bound).
- The level-3 pieces, the last level and the non-constant columns are conormal of tf-weight above 2 (lem:iii-i2-4-3: at
  least ℓ_3 + 4 − ε for σ³ĝ^aug and ℓ_3 + 4 − ε for σ³ĥ^aug).

*n_K ≤ N_ι + N_Λ.* I redid the enumeration of the zf-degrees below 1 + ε_K. At level 1, the degrees are α_0 − 2 + i
(s1), α_0 − 1 + i (v1) and α_0 − 1 − μ + i (other rows). Λ is real below 3 + ε_+ and meets (2, 2 + ε_K] in no point, so
α_0 = 2 or α_0 > 2 + ε_K. The roots are real, and every non-integer root has −μ ≥ ε_ind > ε_K. So only the following
remain:
- s1, i = 0, at degree α_0 − 2;
- at α_0 = 2, degree 1, from s1 with i = 1, v1 with i = 0 and the μ = 0 rows;
- at level 2, s1 with i = 0, at degree α_0 − 1 = (α_0 + 1) − 2;
- the log-free integer degrees 0 and 1, including the tf-part terms of lem:iii-i11-2-3 for larger R.

The ℕ₀-shifts add only degree 1. Each degree is λ − 2 with λ ∈ Λ ∩ [2, 3 + ε_K), and its logarithmic order is at most
k̄(λ) + 1, using k̄(2) ≤ k̄(3) at degree 1. So n_K ≤ Σ_(i≤N_Λ)(k̄(λ_i) + 2) = 5N_Λ + J′N_Λ(N_Λ + 1)/2 ≤ N_Λ + N_ι, by the
monotonicity in lem:uc-n-iota. ℓ_F ≤ ⌈3/2 + ε_K⌉ = 2 checks, and the charge is at most N_ι + N_Λ + 2 ≤ N_ι + N̄_Λ + 2.

---

## The elementary charges (task item 2): each redone from the chapter's proof

- **FWD 20,183.** By thm:fwd-loss, plus 3 from ‖h_(b,rem)(q)‖_(𝒳^m) ≤ C‖q‖_(𝒬^(m+3)) (prop:uc-dbg, first paragraph).
  Valid at b₀; at b ≠ b₀ see finding 2.
- **BG 11.** prop:uc-dbg gives split loss (2; 11, 2).
- **prop:iii-g4-4-4 ≤ 3.** From lem:ec-round-charges (b): the solution costs ℓ_tf = 1 and the remainder 3.
- **prop:iii-g4-5-1 ≤ 9.** Step 1 runs over j = k₀, …, ⌊ℓ_zf⌋, at most 3 values since ℓ_zf < 3. Each j applies
  g_(j+1) = ±iρ^(j+1−α)ρ(ρ∂_ρ − 3/2 − S̄)v_j, the parts of L̂_b − L̄̂ and the commutators (2 each). Then N_tf⁻¹ (1) and
  f₁ − L̂_b(σ)u₂ (2): 2·3 + 3 = 9.
- **prop:iii-i1-3-1 ≤ 6.** Step 1 (2), then two windows [2, 3) and [3, 4) at Re z ≤ ℓ_I < 3.5. ℰ^C_I is log-free with
  least exponent 2 (prop:is-ci-pp (a)), so each term is solved once. Each window passes f − L_b(·) (2): 6.
- **prop:iii-i1-2-1 ≤ 407.** At most 7 + 1 + 5 + 8 + 13 = 34 ≤ 37 steps, from the four ceilings ⌈2.51/0.4⌉,
  ⌈2/0.4⌉, ⌈3/0.4⌉ and ⌈5/0.4⌉ with η ∈ [2/5, ½). Each step applies L̃ of L^(g,g_0) once (11).
- **lem:iii-a-1-4: 2 per step, at most 4 steps.** See reading (c) and finding 6.

Also checked:
- lem:cs-transforms (a)–(f): (a) ⌈5/2⌉ = 3. (d) ⌈3/2 + ε⌉ = 2 and ⌈1 + 7ε/2⌉ = 2. (e) ℓ_1 = 2 (from ¼ + 3ε/2 and
  s_c − 1 = 2), ℓ_2 = 0, ν = 1 and ℓ_4 = 4, which gives 19 + 1 = 20 and 20 + 10 = 30. (f) the three triples match
  prop:iii-i2-5-1, prop:iii-i3-2-1 and prop:iii-i5-2-1 (iv).
- lem:cs-elem (h): 30, from lem:ec-closed-forms (f).
- The step lists against the proofs: lem:iii-i8-3-2 with Steps 3–3.3, 3.4′, 4–8 of prop:iii-i6-2-1; lem:iii-i11-3-2 with
  prop:iii-i10-3-1 and prop:iii-i11-3-1 Steps 0–7 (prop:iii-i13-2-1 for β < 4); prop:iii-i2-5-1 Steps 1–3;
  prop:iii-i5-2-1 Steps 0–4 with Steps 2–3 of prop:iii-i3-2-1 (43); the base items (1)–(7) (1,914);
  thm:iii-i12-3-1 (i)–(ix); Steps 1–3 of thm:iii-j1-2-1. Apart from findings 1, 7, 8 and 15, the lists match what the
  proofs do.

## The free choices (task item 3)

- **(a)** ϑ_in = 0 is admissible: (O3) and sec:i-b-1-4 choose the inner product separately for each radial set, and
  lem:ec-theta-in-zero applies at the computational point. ϑ_ℋ < 9/4 on ℬ̄_* follows from lem:iii-f2-1-1 with δ = ¼.
  Shrinking ℬ_* is allowed: ch. 39 and ch. 40 shrink it repeatedly, "every statement holds on the final ℬ_*".
  s_c = 3 > 11/4 suffices for cor:ii-g1-4-2, prop:ii-g1-4-7, lem:iii-i2-4-2, which goes through thm:iii-h-4-1 ("s > ½ +
  ϑ_ℋ constant"), prop:ii-g1-4-4 and cor:ii-g1-4-5. The s_c of (C1) in def:iii-h1-1-1 is the order of the forward problem
  and is a separate object.
- **(b)** 𝗋_in = −¼ meets 𝗋_in > −½ and 𝗋_in ≥ 𝗋_out = −½ − 3ε/2. In prop:ii-g1-4-4, 𝖻 ≡ 0 is the order its own proof
  takes. β′_I = 3/2 − 2ε < min(β_I, 3/2) holds.
- **(c)** is not admissible as written (finding 4).
- **(d)** is admissible.
- **(e)** is prop:uc-ltf.

The thm:iii-i11-4-1 level α′ and the small numbers of lem:iii-a-1-4 are choices that def:cs-choices must add (findings 1
and 6). No statement of the chapters changes under any of these choices.

## Arithmetic (task item 6): every integer checked exactly

- k̄_max = 12,811,621,665,714,434,999,187.
- N_ι = 107,279,395,180,026,392,909,234,131,199,999,996.
- C_lev = 214,558,790,360,052,785,818,485,009,600,000,520.
- The step sums: 497, 529, 466, 469, 43, 1,914 and 508.
- I_lev = 34,268,829,852.
- I_base = 1,435,970,471,299,470,574,962.
- d_Φ ≤ 1,038,326,399,999,940.
- (N̄_Λ + 2)(d_Φ + 30) = 17,389,059,886,080,535,910,399,999,970.
- 3I_lev = 102,806,489,556 and 2X_12 = 102,492,973,325,715,479,993,544.
- The sum of the seven numbers is 17,389,163,815,025,371,354,557,103,786.
- 6N_ι = 643,676,371,080,158,357,455,404,787,199,999,976 and 3N̄_Λ = 50,241,599,999,997.
- The bound of eq:cs-cstar is 643,676,388,469,322,172,480,826,383,357,103,759 < C_*, with margin 3.61·10³⁰. It equals
  the right side of eq:cs-c0 computed directly.
- D_acc = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 < 1.57157·10⁵⁰.
- 21D_NM + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006 < 3.30029·10⁵¹.
- rem:cs-sharpness gives D_e + K·C_lev + 469N_b + 466(N_b + 1) + C_* = 2.6193·10⁴⁹ < 2.62·10⁴⁹, with
  K < 1.22077·10¹⁴ and N_b < 6.10382·10¹³.
- (N̄_Λ + 2)(d_Φ + 30) < 1.739·10²⁸.
- In thm:uc-integer: 3ε_K + 2δ̂ + δ̄ = 1.9706·10⁻⁸ < 1.98·10⁻⁸; 3R > 1.24987·10²⁴ > 1.2498·10²⁴;
  1.0072 · 1.2498 > 1.2587; 62N̄_Λ + 10 = 1,038,326,399,999,948.

The only false number is the 1.74·10²⁸ claim of finding 9.

thm:uc-integer's statement and proof carry the integers and no pending marker; the file has no `[[pending:` left.
rem:uc-missing agrees with them (M_c C_* of order 10⁵⁰, the free choices, the Step 7 count).

## The contract (task item 7)

- `python3 lint.py proofs/P-U71-cstar.md proofs/P-U71-close.md`: every hit is a cross-file undefined reference. All
  775 references of the two files resolve across chapters/ and proofs/.
- No line exceeds 121 characters: the maximum is 121, at cstar l. 425 and close l. 517.
- No wrapped line starts with a forbidden token. The hits at close l. 30–33 and l. 41–42 are intended list items.
- All labels are lowercase, and none of the 59 labels of the two files is defined elsewhere.
- No process or program words; "computational point" is the defined term of def:ec-point.

## Outside this scope (for the coordinator)

ch. 71 l. 20–22 ("No upper bound for d is proved ...") and rem:ec-other-losses l. 385–387 ("None is proved here;
rem:ec-integer-bound records one ...") contradict thm:uc-integer and rem:uc-missing. The writer's report gives
replacement texts for both. The P-U71-assembly paragraphs it lists have already been updated. Finding 2 also concerns the
forward chain and the assembly's split-loss paragraph and thm:loss-d (i).

**Verdict: NOT CONFIRMED: 2 Major (1, 2), 8 minor (3–10), 5 nit (11–15).** The integer bound
d_acc, d_NM ≤ D_acc < 1.57157·10⁵⁰, N_NM < 3.30029·10⁵¹ stands once findings 1 and 2 are fixed. Neither fix, as
proposed, changes a printed integer.
