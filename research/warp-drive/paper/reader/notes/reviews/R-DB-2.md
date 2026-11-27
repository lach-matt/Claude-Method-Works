# R-DB-2: reading of the explicit upper bound on the loss d (P-U71-assembly, P-U71-close)

Reader: R-DB-2 (independent; changed nothing). Texts, in full: proofs/P-U71-assembly.md (632 lines, md5
76949f9291df10382c20ece842a67fe3) and proofs/P-U71-close.md (559 lines, md5 5716048084d55cd13ec23e020eaa0287),
unchanged during the reading. Inputs read at every cited statement: proofs/P-U71-forward.md (thm:fwd-loss, texts 7–12),
proofs/P-U71-IS.md (md5 9f6712db…, sec:is, lem:is-offsets, prop:is-ind/-logs/-iota/-mult/-ci-pp/-lambda/-count,
thm:is-gap, thm:is-d0, rem:is-summary), proofs/P-U71-SP.md (thm:sp-spectrum, cor:sp-lstar), proofs/P-U71-cstar.md
(def:cs-choices, lem:cs-levels, prop:cs-cstar, rem:cs-sharpness); chapters 32, 34, 36, 39, 40, 41, 42, 43, 46, 48, 71,
3 and 90 at every key used; notes/reviews/R-P-U71-close.md, notes/reports/W-DB.md, STATUS.md and INTEGRATION.md.
"cl. n" / "as. n" are lines of P-U71-close / P-U71-assembly; "ch. 41:n" is line n of chapters/41-….md as read.

Private checks (exact rationals with fractions/Decimal at 60 digits, mpmath at 50–80 digits), in
scratchpad/reader/scratch/r_db2/ (refs.py, eval1.py, eval2.py, eval3.py, gauge.py): every number of sec:uc-eval,
lem:uc-two-offsets, cor:uc-two-offsets, thm:uc-integer's integers, the ε_Υ table of lem:ec-gauge-gap, and the
resolution of all 211 distinct keys of the two texts against chapters/ and proofs/.

## Verdicts

- **P-U71-close: NOT CONFIRMED** — 1 Major, 2 minor, 3 nits.
- **P-U71-assembly: NOT CONFIRMED** — 0 Major, 2 minor, 1 nit.

Every number of sec:uc-eval re-derives exactly and is rounded in the safe direction; the accounting of prop:ec-upper
is right; every finding of R-P-U71-close and the three summarised findings of the assembly's second reading are
resolved. The Major (C1) is an admissibility condition that the choice of def:uc-choice violates: ε_+ = 1.9·10⁻⁸ breaks
(G⁺) of def:iii-j-g-plus and (Ex1) of def:iii-j3-1-3, which the constructions of thm:iii-j2-4-2 and the exact scales on
which d_NM is taken require; for the index sets as constructed (G⁺) holds exactly when ε_+ < μ_G. The repair changes
one number (ε_+ := 1.64160217·10⁻¹⁴) and adds checks; **no evaluated number moves** (D_e, M_c, N_Λ, N_ι, D_acc,
3R all stand). Section "Chapter changes" gives the exact texts the integration round must place, including the
loss-3 replacements of lem:iii-j2-2-4 (ch. 43) and lem:iii-k-2-2 (d) (ch. 46).

## 1. Earlier findings (task 1)

R-P-U71-close (3M 7m 1n), each checked at the current text:

- F1 (premise "least real parts only"): resolved. cl. 6–12 rewritten; cl. 44–55 is the reviewer's text, with "which
  it does not list" correctly replaced by "[[sec:is]] lists them".
- F2 (enlargement bounds nothing): resolved. cl. 65–67 and 82–83 carry the reviewer's sentences; thm:uc-reduction (iii)
  and its proof (cl. 315–330) now state the values from IS/SP and cite thm:uc-integer; no "no positive number is
  admissible" remains.
- F3 (rem:uc-missing): resolved by the later rewrite (out of scope beyond consistency, which holds).
- F4: resolved (cl. 61–63). F5: resolved (cor:uc-two-offsets (b), cl. 130–145; rem:uc-offset-d0, cl. 149–152;
  cl. 125). F6: resolved (cl. 254, 268–269). F7: resolved (cl. 168–169, 198–199, 204–206). F8: resolved
  (lem:uc-spec-as and lem:uc-theta-in deleted; prop:uc-ltf uses lem:ec-theta-in-zero; as. 349–350, 385, 619).
  F9: resolved (cl. 292–295). F10: the assembly items are resolved in the rewritten as. 152–157, 599–632; the chapter
  items are in "Chapter changes" below. F11: not yet placed in chapter 46; text in CH-46 below.
- Assembly second reading (as summarised): (iii) now carries "levels more than ½(α − 4) apart" (as. 148) and
  prop:ec-upper "Δβ > ½(α − 4)" (as. 528) — resolved; "s is free" — lem:ec-tf-loss takes any integer s ≥ 1, s = 1
  allowed (as. 348–350) — resolved; "chapter-3 text bounds only d_acc" — the chapter text is not in these files; CH-3
  below bounds d (= d_NM) and N_NM.

## 2. Findings

### P-U71-close

**C1 (Major) — cl. 343, 345–351, 353–385, 468: the choice violates (G⁺) and (Ex1); lem:uc-admissible omits them.**
def:iii-j-g-plus (ch. 42:564–567) asks: no λ ∈ Λ has real part in (3, 3 + ε_+]. It is a standing hypothesis of the
setting of thm:iii-j1-2-1 and thm:iii-j-2-4 (ch. 42:885, "α with (A_J), (G⁺)"), which thm:iii-j2-4-1 uses through
lem:iii-j1-1-1 (ch. 43:389) and thm:iii-j2-4-2 through thm:iii-j1-2-1; and (Ex1) of def:iii-j3-1-3 (ch. 43:501), the
same condition at its closed endpoint, is a hypothesis of the exact scales of cor:iii-j3-6-6, on which lem:iii-k-2-3
and so d_R = d_NM are taken. By thm:is-gap and its table, λ_♯ + 1109655𝔡₀ + 31682𝔡₁ = 3 + μ_G ∈ Λ, μ_G < 1.6416022·10⁻¹⁴,
so (G⁺) holds exactly when ε_+ < μ_G. def:uc-choice takes ε_+ = 1.9·10⁻⁸; (G⁺) and (Ex1) fail, and the bounds of
thm:uc-integer are stated for constructions that are not defined at that choice. lem:uc-admissible checks (G),
eq:iii-i9-1-1, (H4), η_1, η_2, ε, α, the levels and a♭_K, but neither (G⁺) nor (Ex1)–(Ex4) nor (A_J).
No count depends on ε_+ beyond ε_+ < δ̄ (prop:is-lambda, prop:is-count hold for every ε_+ ∈ (0, δ̄)) and
η_2 − η_1 < ε_+ in T_2, so taking ε_+ ∈ (ε_K, μ_G) moves no number. With ε_+ := 1.64160217·10⁻¹⁴:
ε_+ − ε_K = 2.17·10⁻²⁰, ε′_0 = 1.085·10⁻²⁰ < 0.001ε_K, so every admissible α has 0.999ε_K ≤ α − 4 ≤ ε_K; (Ex2) holds
(near 3 the exponents of ℰ^tot_I are 3 and numbers at distance at least 0.0099, prop:is-ci-pp (a) and eq:iii-c-3-1);
sec:iii-j2-1's 5ε_1 < ε_+ − η^0_2 (ch. 43:104) and lem:iii-j1-1-1's η_2 = ε_+ − 3ε only make ε smaller.

*Fix.* (a) Replace cl. 343 (the display) by

        ε_Υ := 1.4619·10⁻¹⁰,     ε_K := 1.6416·10⁻¹⁴,     ε_+ := 1.64160217·10⁻¹⁴,     l_* := 50,     k̄_0 := 3.
                                                                                                         {#eq:uc-choice}

(b) Replace cl. 345–351 (from "Take ℓ_I ∈ (3 + ε_+, 3.5)" to "0.999(α − 4) ≤ a♭_K − 2 < α − 4.") by (this also
resolves C2 and C3):

    Take ℓ_I ∈ (3 + ε_+, 3.5) with ℓ_I ≤ a_I, off the exclusion sets of (H4) of [[sec:iii-i10-1]], and λ₋ ∈ (ℓ_I − 2, 3/2)
    and δ_ι ∈ (0, 3.5 − ℓ_I) in [[lem:uc-phi-loss]] and [[lem:ec-closed-forms]] (e); η_1 < η_2 in (ε_K, ε_+) with
    η_1 < ε_g such that no λ ∈ Λ has real part 2 + η_1 or 3 + η_2; the loss ε of [[lem:iii-i8-3-2]] and
    [[prop:iii-i13-2-1]] with 0 < ε ≤ 10⁻³ε_g, besides the conditions that [[sec:iii-j2-1]], [[sec:iii-i11-1]] and
    [[def:iii-i13-1-1]] place on it; α admissible ([[def:iii-i10-1-3]]) and satisfying (A_J) of [[def:iii-j-a-j]] and
    (Ex3)–(Ex4) of [[def:iii-j3-1-3]]; levels β_0 = α_1 < β_1 < ⋯ < β_K = α of Step 2 of the proof of
    [[thm:iii-i14-3-1]] with 0.999(α − 4) ≤ β_(k+1) − β_k < α − 4; the number a♭_K of [[lem:ec-counts]] with
    a♭_K > α_1 and 0.999(α − 4) ≤ a♭_K − 2 < α − 4; and the base level α_0 of [[lem:ec-counts]], admissible, with
    max(2, α_1 − (a♭_K − 2)) < α_0 < α_1.

(c) Replace cl. 353–355 (from "**Lemma {#lem:uc-admissible}**" to "of [[eq:ec-upper-counts]] hold with") by

    **Lemma {#lem:uc-admissible}** (The choice is admissible.) The choice of [[def:uc-choice]] exists and is admissible
    for [[thm:iii-i14-3-1]], [[prop:iii-i8-4-1]], [[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]], for [[thm:iii-j-2-4]] and
    [[thm:iii-j1-2-1]], and on the exact scales of [[cor:iii-j3-6-6]]. At it ε_g = ε_Υ, (G) and (G⁺) hold, and the
    hypotheses of [[prop:ec-upper]] and of [[eq:ec-upper-counts]] hold with

(d) cl. 363: "and 1.6416·10⁻¹⁴ < 1.9·10⁻⁸ < 1.9413·10⁻⁸ < δ_50," → "and 1.6416·10⁻¹⁴ < 1.64160217·10⁻¹⁴ < 1.9413·10⁻⁸ <
δ_50,".

(e) After cl. 366 "[[def:iii-i10-1-3]] asks." insert:

    *(G⁺) and the exactness conditions.* By [[thm:is-gap]] and its proof, λ_♯ + 1109655𝔡₀ + 31682𝔡₁ = 3 + μ_G has the
    least real part above 3 of the elements of Λ, and ε_+ < 1.64160217197·10⁻¹⁴ < μ_G ([[eq:is-mu]]); so no λ ∈ Λ has
    real part in (3, 3 + ε_+], which is (G⁺) of [[def:iii-j-g-plus]] and (Ex1) of [[def:iii-j3-1-3]]. (Ex2) holds: near 3
    the real parts of the exponents of ℰ^tot_I ([[eq:iii-c-3-1]]) are 3 and numbers at distance at least 0.0099 from 3
    ([[prop:is-ci-pp]] (a)), so none is 3 + ε_+, and λ_♯ < 2.

(f) cl. 366–367: "(H4) asks ℓ_I > 3 + ε_+ off discrete sets, and a_I > 3 + ε_+ of the class; so ℓ_I ∈ (3 + ε_+, 3.5)
off those sets exists." → "(H4) asks ℓ_I > 3 + ε_+ off discrete sets, with ℓ_I ≤ a_I ([[sec:iii-i8-1]]), and so
a_I > 3 + ε_+ of the class; so ℓ_I ∈ (3 + ε_+, 3.5) with ℓ_I ≤ a_I off those sets exists."

(g) cl. 370–371: "[[sec:iii-j2-1]], [[sec:iii-i11-1]] and the proofs of [[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]] ask ε
small and off finite sets," → "[[sec:iii-j2-1]], [[sec:iii-i11-1]], [[def:iii-i13-1-1]] and the proofs of
[[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]] ask ε small and off finite sets,".

(h) Replace cl. 373–375 (from "*α.* An admissible α ≥ 3" to "≤ ε_K exists.") by

    *α.* An admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K], ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
    1.085·10⁻²⁰, off a finite set ([[def:iii-i10-1-3]]), and (A_J), (Ex3) and (Ex4) exclude finitely many more
    ([[def:iii-j-a-j]], [[lem:iii-j3-1-4]]); so such an α exists, and as ε′_0 < 0.001ε_K, 0.999ε_K ≤ α − 4 ≤ ε_K.

(i) After cl. 380 "2 + 0.999(α − 4) < α − 2." insert (C2):

    *α_0.* The proof of [[prop:iii-i8-4-1]] at the level α_1, at the background of K⁺-order a♭_K, starts from an
    admissible α_0 ∈ (2, min(a♭_K, 2 + ε_g, 5/2)) below α_1; as α_1 < a♭_K, α_1 < 2 + ε_K < 2 + ε_g and the excluded
    values are finitely many, an admissible α_0 ∈ (max(2, α_1 − (a♭_K − 2)), α_1) exists.

(j) cl. 468: "As η_2 − η_1 < ε_+ = 1.9·10⁻⁸, (1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 1.9·10⁻⁸) · 3.0000026·10⁶ + 2 <" →
"As η_2 − η_1 < ε_+ < 10⁻¹³, (1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 10⁻¹³) · 3.0000026·10⁶ + 2 <".

**C2 (minor) — cl. 345–351, 353–385: the base level α_0 is not chosen.** The proof of prop:ec-upper counts the window
loops of the base as three, "the choice α_1 − α_0 < a♭_K − 2 makes that level step one" (as. 590): prop:iii-i8-4-1
climbs α_0 < α_1 < ⋯ < α_n = α_1 with steps below a♭_K − 2 (ch. 40:1131–1132), each step running a window loop of
lem:iii-i8-3-2. def:uc-choice fixes α_1 and a♭_K but not α_0, so lem:uc-admissible does not establish that the count
N_< + N_> + N_b + 3 of prop:uc-explicit applies. The choice exists (α_1 < a♭_K, α_1 < 2 + ε_g, admissible values dense).
*Fix.* C1 (b) (last clause) and C1 (i); and A1 below for the hypothesis in the assembly.

**C3 (minor) — cl. 345, 366–367: ℓ_I ≤ a_I is missing.** sec:iii-i8-1 keeps "ℓ_I with ℓ_I ≤ a_I" (ch. 40:703), and (H4)
derives a_I > 3 + ε_+ from it (ch. 41:121–123). The text takes ℓ_I ∈ (3 + ε_+, 3.5) without it and infers existence
from a_I > 3 + ε_+, which needs ℓ_I ≤ a_I in the interval. *Fix.* C1 (b) (first clause) and C1 (f).

**C4 (nit) — cl. 337, 459: "checked" narrates.** *Fix.* cl. 336–337: "and each is checked by multiplying out the numbers
printed." → "and each follows by multiplying out the numbers printed."; cl. 459: "each checked by multiplying out" →
"each by multiplying out".

**C5 (nit) — cl. 126, 131, 151: the value 1.46·10⁻¹⁰ no longer occurs in the paper.** It was the hypothesis of an
earlier form of rem:ec-upper-point; no statement of the edition takes ε_K = 1.46·10⁻¹⁰ now, so the clauses are
unmotivated. *Fix.* cl. 126: delete "; in particular (G) does not hold at ε_K = 1.46·10⁻¹⁰". cl. 131: "and for them (G)
does not hold at ε_K = 1.46·10⁻¹⁰." → "and for them every ε_K with which (G) holds is below 1.6417·10⁻¹⁴.". cl. 151:
"(G) fails at 1.46·10⁻¹⁰ ([[cor:uc-two-offsets]])" → "(G) fails at every ε_K ≥ 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]])".

**C6 (nit) — cl. 472: the window term is bounded with the integer count, the first line has W.** eq:ec-upper's first line
contains r_ιW(…) with W = 0.4901/𝔡₁ + 1 < 1,470,302.27; the proof multiplies by 1,470,302. The statement holds either
way (16 · 1,470,302.27 · 1.831147·10¹⁴ < 4.3077434·10²¹ < 4.30775·10²¹, checked exactly), but the proof should bound
the formula it states. *Fix.* cl. 472: "16 · 1,470,302 · 1.831147·10¹⁴ < 4.30775·10²¹" → "16 · 1,470,302.27 ·
1.831147·10¹⁴ < 4.30775·10²¹, and so does the integer count of the windows".

### P-U71-assembly

**A1 (minor) — as. 442–451, 527–528, 589–591: a choice used in the proof of prop:ec-upper is not a hypothesis.** The
proof counts the base's window loops as "those of Steps 0 and 2 of the proof of lem:iii-i8-3-1 and of the level step
α_0 → α_1 of prop:iii-i8-4-1 (the choice α_1 − α_0 < a♭_K − 2 makes that level step one)". Neither lem:ec-counts nor
prop:ec-upper makes that choice, and "in the setting of lem:ec-counts" (every admissible choice) prop:iii-i8-4-1 may
take several base levels, each with its own window loop, which N_< + N_> + N_b + 3 does not count. The choice is always
available. *Fix.* as. 450–451: after "it is not the K⁺-order a_K ≥ 4 + ε_K of h in Step 2)." insert " Let α_0 be the
admissible level from which the proof of [[prop:iii-i8-4-1]] at α_1 starts, taken, as that proof allows, with
α_1 − α_0 < a♭_K − 2, so that it has the single level step α_0 → α_1." as. 590: "(the choice α_1 − α_0 < a♭_K − 2 makes
that level step one)" → "(the choice of α_0 in [[lem:ec-counts]] makes that level step one)".

**A2 (minor) — as. 189–210: prop:ec-delta-cap must follow the loss-3 form of lem:iii-k-2-2 (d).** The d-bound texts
adopt that lem:iii-k-2-2 (d) loses 3 derivatives (F-P-U71-close; INTEGRATION "corrected to a fixed loss 3 … also
lem:iii-k-2-2 (d)"), and CH-46 below places it: at the order 2d, (d) then holds with ω_(2d+3) and s_(2d+3) of
prop:iii-k-1-2 (3). prop:ec-delta-cap reads "s_(2d), C_(2d) and the modulus ω_(2d) are those of lem:iii-k-2-2 (d) at the
order 2d (prop:iii-k-1-2 (3))" and concludes ω_(2d)(2δ) ≤ 2^(−(32d+8)); with the corrected (d) the proof gives this for
ω_(2d+3), and nothing relates ω_(2d) to ω_(2d+3). The other three bounds are unaffected. *Fix.* Replace as. 189–197
(from "threshold be ε_NM" to the display) by

    threshold be ε_NM = θ_0^(−(8d+2)), with θ_0 as chosen in the proof of [[thm:ii-g-2-1]]. Let ε be the data threshold
    of [[cor:s27-rate]], chosen, as in the proof of [[thm:iii-k-3-2]], with ε ≤ s̃ and C_(2d)ω̃(ε) ≤ ε_NM, where C_(2d) is
    the constant of [[lem:iii-k-2-2]] (d) at the order 2d, and ω̃ := ω_(2d+3) and s̃ := min(s_(2d+3), s_P) are the modulus
    and the threshold with which (d) holds there (those of [[prop:iii-k-1-2]] (3) at the order 2d + 3), enlarged if
    necessary so that C_(2d) ≥ 1 and ω̃(t) ≥ t on [0, s̃]; and let C_R ≥ 1 be the constant of [[cor:vii-2-3]]. Then
    δ = ½ε and λ1 satisfy

        λ1 < δ,     ω̃(2δ) ≤ 2^(−(32d+8)),     δ ≤ 2^(−(32d+9)),     log₁₀ δ < −(59/196)(32d + 9).

and in the proof and the paragraph after it: as. 199 "and ω_(2d)(t) by max(ω_(2d)(t), t)" → "and ω̃(t) by max(ω̃(t), t)";
as. 202–203 "So ω_(2d)(2δ) = ω_(2d)(ε) ≤ ε_NM/C_(2d) ≤ 2^(−(32d+8)), and as ε ≤ s_(2d), ε ≤ ω_(2d)(ε) ≤" (across the line
break) → "So ω̃(2δ) = ω̃(ε) ≤ ε_NM/C_(2d) ≤ 2^(−(32d+8)), and as ε ≤ s̃, ε ≤ ω̃(ε) ≤"; as. 210 "the inverse of ω_(2d)" → "the
inverse of ω̃". (Rewrap to 121 characters.)

**A3 (nit) — as. 610–611: the remark says four inputs are open, and then bounds all four.** "Four inputs separate
[[prop:ec-upper]] from an integer; at the computational point (1), (2) and (4) are evaluated, and (3) is reduced to one
number." Item (3) ends with prop:cs-cstar bounding that number. *Fix.* Title "(What the upper bound leaves open.)" →
"(The inputs of the upper bound.)"; the sentence → "Four inputs separate [[prop:ec-upper]] from an integer; at the
computational point all four are bounded: (1), (2) and (4) are evaluated, and (3) through one number, c_*, which
[[prop:cs-cstar]] bounds."

## 3. sec:uc-eval re-derived (task 2)

All exact; each printed bound is on the safe side.

- Gaps: 𝔡_ℳ = d₁(8) − d₂(7) = 2.924258·10⁻¹⁰ ∈ (2.9239, 2.92428)·10⁻¹⁰, half 1.462129·10⁻¹⁰ > ε_Υ; ε_g = ε_Υ
  (δ_50 > 1.9413·10⁻⁸). ε_K = 1.6416·10⁻¹⁴ < μ_G = 1.64160217197127…·10⁻¹⁴ (60 digits), ε_K < ε_Υ.
- Δβ_0 = 0.998001·1.6416·10⁻¹⁴ = 1.6383184416·10⁻¹⁴ and Δτ_0 = 1.4604381·10⁻¹⁰ exactly; Δβ ≥ 0.999(α − 4) > ½(α − 4);
  a♭_K − 2 ≥ Δβ_0; Δτ = ε_g − ε ≥ Δτ_0; Δβ_0 ≤ 1; the round increment is exactly ε_g − ε ≤ ε_Υ < δ̂.
- lem:uc-gaps: least exponent of ℰ_ind (eq:is-low) and of ℰ^ι_ind (prop:is-iota) is 𝔡₁ = η_0; the remainder index set
  of eq:iii-g4-4-3 is that of the state corrections with (1, 0) (ch. 36:1461), a subset of ℰ_ind as constructed, and
  the windows of Step 2 of prop:iii-i5-2-1 have width ε^ι_ind (ch. 39:1047–1055); so (d), (e) hold with 𝔡₁.
- lem:uc-lambda: N_Λ ∈ (16,206,600,000,000, 16,747,199,999,999]; J′ = 15,000,016 · 51 = 765,000,816;
  3 + 765,000,816 · 16,747,199,999,999 = 12,811,621,665,714,434,999,187 < 1.28117·10²²; 62N̄_Λ = 1,038,326,399,999,938,
  d_Φ ≤ …,940, d_FM, d_Ψ ≤ …,948; J_* = ⌈5/𝔡₁⌉ + 2 = 15,000,013 + 2. n(λ_i) = i − 1 needs the reality of
  Λ ∩ {Re ≤ 3 + ε_+} (prop:is-lambda) — used correctly.
- lem:uc-n-iota: 4N̄_Λ + 765,000,816 · N̄_Λ · 8,373,600,000,000 = 107,279,395,180,026,392,909,234,131,199,999,996 =
  N_ι < 1.07280·10³⁵; 1 + n_ι + 2⌊β − ε⌋ ≤ 9 + N_ι. ℰ^♭ has the property by prop:iii-i10-3-1 (c) (ch. 41:423–425),
  at every level by prop:iii-i13-2-1 and lem:iii-i13-1-3 (b).
- prop:uc-explicit: 1/Δβ_0 = 6.10381947·10¹³, 1/Δτ_0 = 6.84726042·10⁹, 1/(2Δβ_0Δτ_0) = 2.08972207·10²³,
  1/𝔡₁ = 3000002.5833, 0.4901/𝔡₁ = 1470301.26609; ε_K/Δβ_0 = 1/0.998001; T_< = 2.08972207·10²³, T_> = 2.08972207·10²³
  (both < 2.089723·10²³); T_2 < 6.10382·10¹³ · 3.000005·10⁶ = 1.83114905·10²⁰; first line < 1.2543832·10²⁴ +
  4.30775·10²¹ + 2.74·10¹⁰ = 1.2586909…·10²⁴ < D_e = 1.2587·10²⁴; K + 2N_b + 2 < 2.441528·10¹⁴ + 2 < M_c.
- lem:uc-dr: the levels, rounds, applications and windows are fixed by the weights and index sets, not by the base
  point, and the two added forcing terms are summands of steps already charged; the argument is complete.
- Lower bounds: at ε_K = 1.6417·10⁻¹⁴ the numerator is 1 − 1.9706·10⁻⁸ and ε_Kδ̂ = 2.400395238·10⁻²⁴, R > 4.165972·10²³,
  3R > 1.249794·10²⁴ > 1.2497·10²⁴, 21 · 1.2497·10²⁴ = 2.62437·10²⁵; at ε_K = 1.6416·10⁻¹⁴, ε_Kδ̂ = 2.400249024·10⁻²⁴
  exactly, 3R > 1.24987·10²⁴ > 1.2498·10²⁴, and 1.0072 · 1.2498 = 1.25880 > 1.2587.
- thm:uc-integer's integers (for consistency): D_acc and 21D_acc + 6 are the printed integers, < 1.57157·10⁵⁰ and
  < 3.30029·10⁵¹; M_cC_* = 15,715,640,304·10⁴⁰.

## 4. The structure of prop:ec-upper (task 3)

d_acc is the largest total charge along a chain of the expression; splitting each chain's total into the counted
iterations (rounds, level-1/2 applications, windows) and the rest, and bounding the first by the sum over all counted
iterations and the second by Σ c(β_k) + N_b c_b + (N_b + 1)c′_b + c_0, is a correct bound for every chain, as every
counted map occurs at most once on a chain. Each counted step's charge is bounded from above: rounds ℓ⁺_tf + 2 (ℓ⁺_tf + 4
at levels above 4, the 4(1/Δτ + 2) term), level-1/2 applications ℓ⁺_tf + 2, windows r_ι — the branches into the
solution (u_(λ_0), v_i) cost no more than the counted step and continue in the second kind. The level-2 sum over link
chains is the record's own reading of def:ec-accounted-loss (also chapter 71's rem:ec-integer-bound), and the map is
the same either way, so it gives a loss with which the tame estimates hold. The base's tf rounds at the level α_1 are
zero at the choice (τ_0 = 2 + ε_g − 2ε > α_1) and in general charged in c_0. No counted step applies a forward solution
operator; the forward loss (thm:fwd-loss, d_FWD = D_0 + 76 ≤ 20,180, the d of thm:iii-i-5-3 with the +6) is charged in
c_0 (Step 0) and in c(β), c_b, c′_b wherever a forward solve occurs, as thm:loss-d (i), lem:ec-split-loss and
rem:ec-upper-open (3) say. The only gap is A1 (with C2).

## 5. The loss-3 correction and the chapter statements the texts rely on (task 4)

lem:iii-j2-2-4 (ch. 43:303–318) states both halves without loss; its proof rests on lem:ii-g-4-1 (2)–(3), which lose
d = 3 (> 5/2 on the 5-dimensional manifold, > 4/2 on faces) on one factor. The edition proves the replacement CH-43
below, with the loss on a factor of one's choice. Its uses, all checked: lem:iii-j2-2-1 (b) (ch. 43:186–189) keeps
‖Au‖_k ≤ C_k(‖u‖_(k+2) + ‖β‖_(k+d)‖u‖_d) by putting the coefficient at the order k + 3 (d free) — absorbed;
prop:iii-j2-4-3 (ch. 43:438, 452–453), d free — absorbed; cor:iii-j3-6-6 (ch. 43:1068), fixed loss — absorbed;
ch. 44:671 names the range only; lem:uc-phi-loss (cl. 295) uses the loss 3 explicitly (d_FM ≤ d_Φ + 8 stands);
prop:uc-dbg does not use the lemma. No other chapter text changes for it.
lem:iii-k-2-2 (d) (ch. 46:1247–1248, 1285–1290) uses the same lossless composition ("(a Moser bound)"). Its uses:
the Smallness paragraph of thm:iii-k-3-2 (ch. 46:1464–1466) absorbs the loss (2d + 3 + k′_(2d+3) ≤ N_NM + k″ ≤ d_1, as
2d + 3 ≤ N_NM = 21d + 6 and k′_k is non-decreasing, ch. 46:248; s_♭ ≤ s_(2d+3)) but quotes the constants and must change
(CH-46); prop:ec-delta-cap must change (A2); lem:viii-2-1 (ch. 48:240) cites only "k′_k as in lem:iii-k-2-2 (d)", which
CH-46 keeps meaning prop:iii-k-1-2 (3)'s k′_k — no change.

## 6. Contract (task 5)

All 211 distinct keys resolve (chapters/ or proofs/) to statements that say what is used; the use of every IS, SP and
cstar statement matches its text (thm:is-gap, eq:is-mu, prop:is-count (a)–(c) "for every ε_+ ∈ (0, δ̄)",
prop:is-lambda, eq:is-low, prop:is-iota, lem:is-offsets (b), thm:is-d0, cor:sp-lstar (a), thm:sp-spectrum,
prop:cs-cstar). No label is defined twice in the two texts; prop:ec-rounds, thm:loss-d and prop:ec-delta-cap are also
defined in chapter 71, which they replace (CH-71 (a)). lint on the two files: only the expected cross-file
"undefined label" hits, no style hit, no pending marker; no line over 121 characters (counted in characters); the only
lines starting with a listed prefix are the table rows (as. 43–62) and list items (cl. 27–42). Process words: C4.
Every proof is given in full.

## 7. Chapter changes the integration round must make

**CH-43 (lem:iii-j2-2-4).** Replace ch. 43:303–318 (statement and proof) by

    **Lemma {#lem:iii-j2-2-4}** (Tame products in partially polyhomogeneous spaces.) Let E, E′ be partially polyhomogeneous
    spaces of [[sec:iii-j2-1]] at one or more faces, at the loss ε, and G the space that the membership statements
    ([[lem:iii-c-2-1]]) give to products. There is d_1 ≥ 3 with

        ‖uv‖_(G^k) ≤ C_k (‖u‖_(E^(k+3)) ‖v‖_(E′^(d_1)) + ‖u‖_(E^(d_1)) ‖v‖_(E′^k)),

    and the same with the roles of u and v exchanged; and if the exponents of E have positive real parts, as those of the
    background do, then for a smooth Θ, depending also on the point (through g_0, g_0⁻¹ and their derivatives), with
    Θ(·, 0) = 0, there is δ_Θ > 0 with ‖Θ(u)‖_(G^k) ≤ C_k ‖u‖_(E^(k+3)) for ‖u‖_(E^(d_1)) ≤ δ_Θ, G the space of Θ(u) by
    the same statements.

    *Proof.* The coefficient of uv at an exponent is a finite sum of products of coefficients of u and of v, functions on
    the face, of dimension at most 4, bounded by [[lem:ii-g-4-1]] (2) there with d = 3 > 4/2; a product with a remainder
    factor is bounded by [[lem:ii-g-4-1]] (2) with d = 3 > 5/2 in the weighted b-Sobolev space, the weights adding
    ([[cor:ii-a-9-7]]) and a coefficient being extended from its face by a cut-off; in each product the factor from u is
    the one that (2) measures at the order k + 3; and a term whose exponent lies beyond the remainder's weight is put in
    the remainder with the same bound. As the norms are non-decreasing in the order and d_1 ≥ 3, this gives the bound
    stated, and by symmetry the one with u and v exchanged. For Θ: Taylor's formula to an order M, fixed by the weights,
    at which M times the least real part of the exponents exceeds the remainder's weight. The polynomial part is a finite
    sum of terms c u^γ, |γ| < M, with c smooth; [[lem:ii-g-4-1]] (2), applied |γ| − 1 times with one factor u at the
    order k + 3 and the product of the others at the order 0, bounded through (1) by the L^∞-norms of its factors, gives
    ‖c u^γ‖_(G^k) ≤ C_k ‖u‖_(E^(k+3)) ‖u‖_(E^(d_1))^(|γ|−1). The Taylor remainder is bounded by [[lem:ii-g-4-1]] (3) with
    d = 3 in the weighted b-Sobolev space after a finite partition of unity: the proof of (3), by the chain rule and
    [[eq:ii-g-4-1]], applies verbatim to a function smooth also in the point, with bounded derivatives on the chart
    domains, and δ_Θ is fixed by the domain of Θ and C_Sob. ∎

No other text of chapter 43 changes (section 5).

**CH-46 (lem:iii-k-2-2 (d), thm:iii-k-3-2).** (a) Replace ch. 46:1247–1248 by

    (d) P_5(Ψ(0)) is supported in {T̂ + 7/4 ≤ t^♭_* ≤ T̂ + 2}, and there is s_P > 0 such that
    ‖P_5(Ψ(0))‖_(ℱ^k_ex) ≤ C_kω_(k+3)(‖(γ̃, k̃)‖_(H^(k+3+k′_(k+3)))) when ‖(γ̃, k̃)‖_(H^(k+3+k′_(k+3))) ≤ min(s_(k+3), s_P),
    with k′_k, s_k and ω_k of [[prop:iii-k-1-2]] (3).

(b) Replace ch. 46:1287–1290 (from "So it vanishes outside supp dχ_−," to "ω_k(‖(γ̃, k̃)‖_(H^(k+k′_k))). ∎") by

    So it vanishes outside supp dχ_−, and it is a smooth function of h_0 and its derivatives of order at most 2,
    vanishing at h_0 = 0, on the compact set supp dχ_−(t^♭_*); so, by [[lem:ii-g-4-1]] (3) with d = 3 after a finite
    partition of unity, in the form for functions smooth also in the point (the proof of [[lem:iii-j2-2-4]]), its
    ℱ^k_ex-norm is at most C_k‖h_0‖_(H^(k+5)) while ‖h_0‖_(H^5) is small. By [[prop:iii-k-1-2]] (3) at the order 3,
    ‖h_0‖_(H^5) ≤ ω_3(‖(γ̃, k̃)‖_(H^(3+k′_3))), which is that small once ‖(γ̃, k̃)‖_(H^(3+k′_3)) ≤ s_P for some
    s_P ∈ (0, s_3], as ω_3(s) → 0; and ‖(γ̃, k̃)‖_(H^(3+k′_3)) ≤ ‖(γ̃, k̃)‖_(H^(k+3+k′_(k+3))), k′_k being non-decreasing.
    At the order k + 3, [[prop:iii-k-1-2]] (3) bounds ‖h_0‖_(H^(k+5)) by ω_(k+3)(‖(γ̃, k̃)‖_(H^(k+3+k′_(k+3)))). ∎

(c) Replace ch. 46:1464–1466 (from "By [[lem:iii-k-2-2]] (d)," to "for data small in H^(d_1).") by

    By [[lem:iii-k-2-2]] (d), ‖P_5(Ψ(0))‖_(ℱ^(2d)_ex) ≤ C_(2d)ω_(2d+3)(‖(γ̃, k̃)‖_(H^(2d+3+k′_(2d+3)))) for data of that
    norm at most min(s_(2d+3), s_P), and 2d + 3 + k′_(2d+3) ≤ N_NM + k″ ≤ d_1, as 2d + 3 ≤ N_NM and k′_k is
    non-decreasing; as ω_(2d+3)(s) tends to 0 with s, ‖P_5(Ψ(0))‖_(ℱ^(2d)_ex) < ε_NM for data small in H^(d_1).

(d) With A2 applied, prop:ec-delta-cap agrees with (a)–(c).

**CH-04, CH-06 (forward loss).** Place texts 7, 8 and 12 at the end of P-U71-forward.md (taken as confirmed), and the
section sec:fwd where its placement comment says; delete both comments. R6-S06's observation (the order list omits −10
and −8, inside the bound) stays with that placement.

**CH-71.** (a) Delete chapter 71's prop:ec-rounds (ch. 71:435–469), thm:loss-d (471–517) and prop:ec-delta-cap with
the paragraph after it (521–544), which as. 85–212 replace; place sec:ec-gauge-gap before prop:ec-rounds, sec:ec-upper
after sec:ec-delta, then sec:uc-close, sec:is, sec:sp, sec:cs.

(b) Replace ch. 71:12–22 (from "Its elementary losses other than" to "is an observation.") by

    Its elementary losses have closed forms in the weights, the threshold quantities of the operators, the index sets and
    the order of the bounds of the background terms ([[lem:ec-closed-forms]], [[rem:ec-other-losses]]), and the loss of
    the forward solution operators is at most 20,180 ([[thm:fwd-loss]]); the iterations of the construction contribute
    their numbers of steps, among them three nested ones; and at one parameter point of the gauge and damping
    parameters two of these iterations alone make d_acc, and so d, larger than 1.403 × 10²⁰ and N_NM larger than
    2.946 × 10²¹, each of their steps being charged at least one derivative for the inverse of the model at the
    transition face, whose incoming threshold is non-negative ([[lem:ec-theta-in]], [[thm:loss-d]]), and larger than
    1.2497 × 10²⁴ and 2.624 × 10²⁵ for the index sets as the proofs construct them ([[cor:uc-two-offsets]]). At that
    point, at one admissible choice of the weights, d_acc and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM
    at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which
    [[thm:settling]] is proved ([[rem:ec-point-outside]]), and the bounds bound what this proof's choices produce, not
    the optimal loss.

and in ch. 71:22–23 "The same formulas bound λ1 by δ, and the modulus" → "The same formulas bound λ1 by δ, δ by a power
of 2 that decreases with d, and the modulus".

(c) ch. 71:48–49: "and so does the lower bound of [[thm:loss-d]] (see its proof)." (across the line break) → "and the lower bound of
[[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at every h, ε_Υ being fixed by (γ_Υ, e_Υ)
([[lem:ec-gauge-gap]], [[prop:ec-rounds]])."

(d) rem:gap-sums, after "No other result of this paper uses [[prop:gap-sums]]." (ch. 71:132) add: "For the index sets
as the proofs construct them, Λ contains further sums, and (G) holds exactly for ε_K < μ_G ≈ 1.6416·10⁻¹⁴
([[thm:is-gap]])."

(e) Replace ch. 71:373–387 (from "The forward solution operators of [[lem:iii-j2-2-1]] (a)" to "at one choice of the
weights.") by

    The forward solution operators of [[lem:iii-j2-2-1]] (a) lose the d of [[thm:iii-i-5-3]], which its proof takes from
    [[thm:ii-f1-1-1]] and raises by 6; there d = D_0 + D_1 + d′ + d″ ([[eq:ii-f1-3-3]]), and [[thm:fwd-loss]] shows that
    d = 20,180 may be taken. The order of choices behind ℓ + 1 is: d_acc and d_NM first, then N_NM, then the trapping data
    at the orders k ≤ N_NM ([[cor:iii-h2-1-2]]); the constants of the smallness conditions are used at those orders only,
    the tame estimates themselves at every order. An explicit value of d_acc needs, besides these closed forms, the order
    d_BG, numbers for the weights at the parameters in question, the counts n(E, β) of the index sets and the numbers of
    steps of the iterations of the inventory of [[sec:iii-j2-3]]; the next section bounds two of these iterations from
    below, and at the computational point [[thm:uc-integer]] bounds d_acc, d_NM and N_NM from above.

(f) sec:ec-integer (ch. 71:546–595). Its two numerical observations are at weights that are not admissible at the
computational point: ε_K = 188·10⁻¹⁰ exceeds ε_Υ < 1.46214·10⁻¹⁰ (lem:ec-gauge-gap) against ε_K < ε_Υ of
def:iii-i10-1-3; the increments ε_* − ε with ε_* = 19·10⁻⁹ exceed ε_g − ε ≤ ε_Υ, so "when ε_g ≥ ε_*" never holds; (G)
fails for the index sets as constructed (thm:is-gap); ε_+ = 189·10⁻¹⁰ violates (G⁺); and "ε_Υ is not evaluated at the
point" is no longer true. Recommended: delete sec:ec-integer (no proof uses it; the admissible evaluation is
thm:uc-integer). If the coordinator keeps it, replace ch. 71:548–550 by

    The bookkeeping of [[def:ec-accounted-loss]] gives an integer at one choice of the weights at the computational point
    that is not admissible there; the following two remarks state it, and no proof uses them. The bound at an admissible
    choice is [[thm:uc-integer]].

delete "(ε_Υ is not evaluated at the point; an increment smaller than ε_g − ε is allowed, a forcing of tf-weight κ
having every smaller tf-weight)" (ch. 71:553–554), and replace ch. 71:567–570 (from "the gap condition (G) holds by" to
"in this paper.") by

    the gap condition (G) holds by [[prop:gap-sums]] for the subset 𝒮 of Λ, also with the least index set of the class
    data adding 23 chains, none coming nearer than 3 + 5.019·10⁻⁸. These were decided in exact rational arithmetic and by
    certified enclosures of the irrational roots, at the scale of 10⁸ levels; they are not proved in this paper. These
    weights are not admissible: ε_K exceeds ε_Υ < 1.46214·10⁻¹⁰ ([[lem:ec-gauge-gap]]), the increments exceed ε_g − ε,
    and (G) and (G⁺) fail for the index sets as the proofs construct them ([[thm:is-gap]], [[def:iii-j-g-plus]]).

(W-DB's text 2 for ch. 71:20–22 is superseded by (b): it still calls c_* unevaluated.)

**CH-3.** Replace ch. 3:351–355 (the bullet "*The constants of [[thm:settling]].*") by

    - *The constants of [[thm:settling]].* The loss d with which the Nash–Moser step is applied, at least the loss that
      the proof assigns to the tame estimates, and its regularity N_NM = 21d + 6, with explicit lower bounds at a
      parameter point that lies outside the proved set ([[thm:loss-d]]) and, there, explicit upper bounds for d and N_NM
      at one admissible choice of the weights ([[thm:uc-integer]]); through the lower bounds, upper bounds for δ and for
      the modulus of the initial family at 2δ (and λ1 < δ); explicit resolvent bounds on five-dimensional Tangherlini
      ([[ch:resolvent-bounds]]); and where explicit evaluation of λ1 and δ stops ([[ch:explicit-constants]]).

**CH-90.** (a) ch. 90:56–57: "The proof's formulas give λ1 < δ and bound" → "The proof's formulas give
λ1 < δ ≤ 2^(−(32d+9)) and bound". (b) Replace ch. 90:60–66 (from "The loss d is at least" to
"[[pending:scope-d-upper]].") by

    The loss d is at least the loss d_acc that the proof assigns to the tame estimates, and the regularity of the
    Nash–Moser step is N_NM = 21d + 6; d_acc is composed of elementary losses in closed form, of the loss of the forward
    solution operators, at most 20,180, and of the numbers of steps of the iterations of the construction ([[thm:loss-d]]
    (i)). At the computational point of [[def:ec-point]], d > 1.403 × 10²⁰ and N_NM > 2.946 × 10²¹, so that
    log₁₀ δ < −1.351 × 10²¹ ([[thm:loss-d]] (ii), [[prop:ec-delta-cap]]), and d > 1.2497 × 10²⁴ for the index sets as the
    proofs construct them ([[cor:uc-two-offsets]]). These are lower bounds for the loss that this proof's choices
    produce, not for the least loss with which the tame estimates hold ([[thm:loss-d]]). At that point, at one admissible
    choice of the weights, d is at most an integer below 1.57157 × 10⁵⁰ and N_NM at most one below 3.30029 × 10⁵¹
    ([[thm:uc-integer]]).

## 8. Observations outside my scope (not counted)

- O1 (for the reader of thm:uc-integer and P-U71-cstar) — cl. 514 states c(β) ≤ 2N_ι + N_Λ + 529, and cl. 532 derives
  it from lem:cs-levels (b), which gives c(β_k) ≤ 2N_ι + N̄_Λ + 529, "with N̄_Λ ≥ N_Λ": the inequality runs the wrong
  way for that inference. Fix: cl. 514 "≤ 2N_ι + N_Λ + 529" → "≤ 2N_ι + N̄_Λ + 529, N̄_Λ = 16,747,199,999,999,"; cl. 532
  ", with N̄_Λ ≥ N_Λ" → "".
- O2 (for P-U71-IS) — IS l. 497–498, "and ε_+ may be taken in (ε_K, δ_50), as [[eq:iii-i9-1-1]] asks", is true of
  eq:iii-i9-1-1 but, with (G⁺) (def:iii-j-g-plus), ε_+ must lie in (ε_K, μ_G); this sentence is what C1 followed. Fix:
  "and ε_+ may be taken in (ε_K, μ_G), as [[eq:iii-i9-1-1]] and (G⁺) of [[def:iii-j-g-plus]] ask".
