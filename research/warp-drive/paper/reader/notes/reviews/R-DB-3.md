# R-DB-3: confirming reading of the F3-IS-SP fix round on P-U71-IS and P-U71-SP

Reader: R-DB-3 (independent; changed nothing in the repository). Texts: proofs/P-U71-IS.md (660 lines, md5
9f6712db894f79bac029bbd011d38814) and proofs/P-U71-SP.md (604 lines, md5 aef5b588ba70c00b395588529b5ff03e), read at
HEAD 7ade0593 and re-checked unchanged at f877acb1 (the commits in between touch neither text, nor chapters 33, 34,
35, 40 or 71). "IS l. n" and "SP l. n" are lines of these files. Read against: READER-BRIEF, STYLE,
notes/reviews/R3-IS-SP.md, notes/reports/F3-IS-SP.md, the diff against b571483c (the R3 versions, md5 545148…/
f2461a…, recovered into the scratch directory and re-hashed), chapters 33 (lem:s14-delta50), 34 (μ_b), 35
(eq:iii-g-2-6, -7), 40 (eq:iii-i9-1-1), 71 (def:ec-point, prop:gap-sums), and every citation of cor:sp-lstar in
P-U71-close, P-U71-assembly and P-U71-cstar. Private checks (mpmath at 60 digits; an exact exponent model of
[[eq:is-l1]]) in scratchpad/reader/scratch/r_db3/ (nums.py, logs_a.py, wrap.py, lint*.txt).

## Verdicts

- **P-U71-IS: CONFIRMED** — 0 Major, 0 minor, 2 nits.
- **P-U71-SP: CONFIRMED** — 0 Major, 0 minor, 1 nit.

Every R3-IS-SP finding is resolved correctly, with R3's fix texts applied word for word, and the diff contains those
changes and nothing else. The three nits below are optional; none moves a number or a statement.

## Findings

### P-U71-IS

**DB3-IS-1 (nit) — IS l. 654-658 (rem:is-summary): "One thing is not determined" names two, and the remark names a
third.** The sentence created by IS-F1 (R3's wording, applied verbatim) reads "One thing is not determined by this
paper: the coefficient c_b … ; whether an admissible ℰ_ind can omit 𝔡₁ is not decided either. Neither question …".
It counts one item, then adds a second, and the next sentence says "Neither question" and "the two questions". Four
lines earlier (IS l. 648) the same remark says the exact multiplicities of the roots below −101 are not decided by this
paper. The original said "Two further things"; dropping "(1)" made the count wrong. Nothing mathematical is affected.
*Fix.* Replace IS l. 654 from "One thing is not determined" to l. 660's end by (wrapped, at most 121 characters; the
line before, l. 653, unchanged):

    are all 1 ([[cor:sp-lstar]] (a)), so they do not raise l_* above L. Two further things are not determined by this paper:
    the coefficient c_b of [[def:is-cb]] at a rotating b, which for index sets that keep 𝔡₁ decides whether ε_K may be taken
    up to μ♭ ([[cor:is-flat]]) or only below μ_G ([[thm:is-gap]]), and whether an admissible ℰ_ind can omit 𝔡₁. Neither
    enters an upper bound for d: the index sets as constructed serve with every ε_K < μ_G, and the two decide only whether
    smaller index sets, with a larger ε_K, are available. The individual roots ι ∈ Z of [[prop:is-iota]] are fixed by the
    polynomials of [[prop:np-10-12]] and located by [[sec:s14-pa]]; they lie above 3 as exponents of ℰ^ι_ind and do not enter
    Λ below 3 + ε_+.

**DB3-IS-2 (nit) — IS l. 229-235 (proof of prop:is-logs (a)): the two steps at m = 1 are not written out.** This is
the first item the writer left (judged in §2 below). The proof bounds the orders at real part at most 3/2 construction
by construction but never treats the first step of (1) (m = 1) or the first step of the class 1 − l at l = 2
(μ = −1, m = μ + 2 = 1); and "a chain of at most three later steps starting from order 0" (l. 233) uses, for the chain
of (1) and of that class, that these steps have order 0 at the offset 1, which nothing states. Below real part 5/2 they
have the exponents 1 (u₀), 2 (u₁ alone: the right side is ρ¹C^∞, and by [[lem:is-count]] (b) the order is
ord(1) + ord(2) = 0, as 1 and 2 are not roots, [[lem:is-roots]] (a)) and 2 + 𝔡₀, 2 + 𝔡₁ (u₂ alone, 𝒢 ⊂ {Re ≥ 3},
k = 0 exactly as for the classes); so offsets 1, 1 + 𝔡₀, 1 + 𝔡₁ with order 0, below the 3 that (c2) attains there,
and (a) stands (checked: logs_a.py). This is the same kind of omission as IS-N2, graded a nit by R3. *Fix.* Replace IS
l. 230-235 by (wrapped, at most 121 characters; l. 229 unchanged):

    from u₂ alone, with no term of 𝒢 ⊂ {Re ≥ 3} below it, so k = 0; the same at 2 + 𝔡₁ for m = 1 − 𝔡₀ and m = 1 − 𝔡₁, and at
    2 + 𝔡₀ for m = 1 − 𝔡₁. The two steps at m = 1, the first step of (1) and that of the class 1 − l at l = 2, have order 0
    at the offsets 1, 1 + 𝔡₀ and 1 + 𝔡₁: the exponent 2 comes from u₁ alone, of order 0 by [[lem:is-count]] (b), as 1 and 2
    are not roots ([[lem:is-roots]] (a)), and 2 + 𝔡₀ and 2 + 𝔡₁ come from u₂ alone, as for the classes. At the integer offset
    1 of a step at m ≤ 0 the exponent m + 1 comes from u₁ alone; for the class first steps with m ∈ {0, −1, −2} this gives at
    most ord(m + 1) ≤ 1, and for the later steps the order is that of the step before at offset 1 plus ord(m + 1) ≤ 1, which
    along a chain of at most three later steps starting from order 0 gives at most 3. So the largest order at real part at
    most 3/2 is 3, at 1, 1 + 𝔡₁ and 1 + 𝔡₀, and (a) follows, the other exponents of [[eq:is-low]] having order 0.

### P-U71-SP

**DB3-SP-1 (nit) — SP l. 285: μ as a coordinate index after the declaration of SP l. 26.** SP-N1 (i) now declares
"μ denoting indicial roots in this section", but the proof of lem:sp-two-roots writes "(δ̄k)_μ = −Σ_j ∂_jk_(μj)", μ a
spacetime index. A GR reader parses it, but it is the double use SP-N1 set out to remove, now against an explicit
declaration. (The other μ with a subscript, μ_b = |dR/R| dg̸ at SP l. 93, is the edition's b-density of chapter 34,
l. 1129, never bare; it needs no change.) *Fix.* SP l. 285: "(δ̄k)_μ = −Σ_j ∂_jk_(μj)" → "(δ̄k)_β = −Σ_j ∂_jk_(βj)"
(β occurs nowhere else in SP; the line length is unchanged).

## 1. The R3-IS-SP findings

| Finding | Where now | Resolved |
|---|---|---|
| IS-F1 (minor), rem:is-summary | IS l. 653-660 | Yes. R3's text verbatim; the pole orders are settled by cor:sp-lstar (a), whose first sentence states exactly that every pole of N_ι⁺(L̄, ·)⁻¹ at real part at most 5 has order 1, and "they do not raise l_* above L" is right (least admissible l_* = max(1, L, M) = L, L ≥ 39). c_b is named as undetermined; the count wording is DB3-IS-1. No other sentence of IS says (SP) is open (searched "(SP)", "not determined", "not decided"). |
| IS-N1 (nit), IS l. 532 | IS l. 532 | Yes, verbatim. lem:uc-fourier-count (close l. 251-265) bounds J_* by ⌈5/ε_Υ⌉ + 2; prop:is-count (c) gives 15,000,015. |
| IS-N2 (nit), prop:is-logs (a) | IS l. 228-235 | Yes, verbatim; redone below. |
| SP-F1 (minor), cor:sp-lstar (d) | SP l. 549-553 | Yes; checked below. |
| SP-N1 (nit), the weight and μ_0…μ_3 | SP l. 25-28, 320-330 | Yes. "we write c for the weight μ there" matches chapter 35 l. 349-351, where the pair is (s, μ) with μ ∈ (Re ϰ − 1, Re ϰ); SP then writes (s, c) at l. 118, 124, 198 and c > k + 1 at l. 86, 98. All 24 occurrences of μ_0…μ_3 became ν_0…ν_3, none left; the only other ν of SP is the moment vector ν ∈ W_π^(K+1) of prop:sp-visible (l. 254-258), an object of the same kind, so no clash. Residual: DB3-SP-1. |
| SP-N2 (nit), prop:gap-sums | SP l. 342-343 | Yes. The proof of prop:gap-sums ("*The offsets.*", ch. 71 l. 81-92) gives 1.3333327·10⁻⁶ < 𝔡₀ < 1.3333334·10⁻⁶ and 3.333330462964·10⁻⁷ < 𝔡₁ < 3.333330462967·10⁻⁷, which implies the printed 3.3333·10⁻⁷ < 𝔡₁ < 3.3334·10⁻⁷. prop:gap-sums is now defined once (ch. 71 l. 72), so the reference is unambiguous. |

**IS-N2, redone.** By [[eq:is-l1]] with E(α) = R + ℕ₀ (all of order 0, least element 2 + 𝔡₁):

- (c2) at 1 + 𝔡₀ (offset 𝔡₀): F = (1, 0) ∪ (E_(c1) − 1) has 1 + 𝔡₀ with ℓ̂_F = 1 (from (c1) at 2 + 𝔡₀, k = 0) and
  nothing on 𝔡₀ − ℕ₀; E(α) meets the ladder nowhere; so ℓ̂ = 1, k = 0.
- (c2) at 1 + 𝔡₁ (offset 𝔡₁): the same with 𝔡₁; k = 0.
- The class at m = 1 − 𝔡₁ at 2 + 𝔡₀ (offset 1 + 𝔡₀ + 𝔡₁): u₀ and u₁ have exponents in m + ℕ₀ only; u₂ is
  [[lem:iii-a-1-4]] with F = 𝒢 ⊂ (m + ℕ₀) ∩ {Re ≥ 3}, which meets the ladder 2 + 𝔡₀ − ℕ₀ nowhere, and E(α) meets it at
  2 + 𝔡₀ only (1 + 𝔡₀ ∉ R + ℕ₀); so ℓ̂ = 1, k = 0.

An exact model (exponents as an integer part plus a vector over 𝔡₀, 𝔡₁, δ′₁, δ₂, d₁(2), …; logs_a.py) gives these
three 0s, and also (c1) 0, 0, 1 at 2 + 𝔡₀, 2 + 𝔡₁, 3 + 𝔡₀; (c2) 3, 3 at 2 + 𝔡₀, 2 + 𝔡₁; (c2) 0, 0 at 2 + δ′₁,
2 + δ₂; (c2) 3, 9, 17, 27, 39 at 2, …, 6; the classes 1 − 𝔡₀, 1 − 𝔡₁ order 0 at both 2 + 𝔡₀ and 2 + 𝔡₁. So the
values 0, 0, 3, 0, 3, 0, 0, 3, 0, 0 of (a) stand.

**SP-F1, checked.**

- *The hypothesis.* [[eq:iii-i9-1-1]] (ch. 40 l. 1256) is 0 < ε_K < ε_+ < min(δ_♯, ε_ind), and [[def:ec-point]] (ch. 71
  l. 39-40) gives ε_ind(10⁻⁶) = δ_50 < δ̄ = 1.94137057·10⁻⁸; so ε_+ < δ_50 < 2·10⁻⁸, with the two citations right. The
  evaluation's ε_+ = 1.9·10⁻⁸ (close l. 343) meets it.
- *The numbers.* δ_50 = 1.9413705684633555848…·10⁻⁸ (from prop:np-10-52 (i) at u = 51, 60 digits), so
  1.94137056846·10⁻⁸ to twelve figures, inside lem:s14-delta50's (1.941370568463, 1.941370568464)·10⁻⁸.
  ι_v(2) = 250002000009^(1/2) − 499999 = 3.000004999980000055…, so 3.00000499998 to twelve figures, and
  ι_v(2) − (3 + 4·10⁻⁶) = 9.9998·10⁻⁷ > 0; the written proof's (500002 + 4·10⁻⁶)² = 250002000008.000016 <
  250002000009 is exact.
- *The list.* Restricting the union of thm:sp-spectrum (a) to {2 ≤ Re ϰ ≤ 3 + ε_+}: from {3, 4, 5} only 3; 4 + 𝔡₀,
  4 + 𝔡₁ lie above; ι₁ ∈ (2 + δ_C, 5/2) lies in the strip, ι₁ + 1 > 3 + δ_C = 3 + 2.94·10⁻⁶ > 3 + ε_+ and ι₁ + 2
  above it; from the P_l family, j = 0 gives the roots with 2 < Re ι ≤ 3 + ε_+, j = 1 gives ι + 1 exactly when
  Re ι ≤ 2 + ε_+ (and then Re(ι + 1) > 3 ≥ 2), j ≥ 2 would need Re ι ≤ 1 + ε_+ < 2; from the vector family every
  ι_v(l) + j ≥ ι_v(2) > 3 + 4·10⁻⁶ > 3 + ε_+ (ι_v increases with l; ι_v(1) = 3 is not in the family). So the poles
  on the strip are exactly 3; ι₁; the roots ι of P_l with 2 < Re ι ≤ 3 + ε_+; and ι + 1 for those with Re ι ≤ 2 + ε_+,
  as (d) lists. The two conditional clauses whose deletion R3 traced are now empty under the stated hypothesis, as
  required. The proof (SP l. 587-594) already used this hypothesis and is consistent with the statement.
- *Uses of cor:sp-lstar.* P-U71-close l. 14, 319, 416, 543 and P-U71-assembly l. 617 cite it for l_* = 50 admissible
  and for the pole orders 1, that is part (a), which the fix round did not touch; each sentence still holds as written
  (l. 416: 15,000,016 · 51 = 765,000,816). P-U71-cstar cites no key of SP; it uses l_* = 50 only through
  k̄_max = 3 + 765,000,816 · N̄_Λ of close's lem:uc-lambda, unchanged. No text cites (d), and no text uses the strip
  list or whether a pole lies in Λ (searched "pole" in all three).

## 2. The two items the writer left

**prop:is-logs (a), the steps at m = 1.** The writer's description is right: below real part 5/2 these steps have
order 0 at the offsets 1, 1 + 𝔡₀, 1 + 𝔡₁, below the 3 attained there, so no value of (a) moves. But it should be
written out: the proof of an upper bound has to bound every construction, and l. 233's "starting from order 0" rests on
the order 0 of the m = 1 steps at the offset 1, which the text never derives. Graded a nit for consistency with IS-N2;
fix text in DB3-IS-2.

**c_i in SP.** The letter c carries five local meanings: the weight c (declared l. 26) and its descent
c_i := c − i(1 + η) (proof of thm:sp-reduction, l. 206-209, with c_0 = c consistently); c_τ(ϰ_0), the order of the
zero of det 𝔐_τ (def:sp-matrix, always with a type subscript and its argument); c_(−p), a Laurent coefficient (proof
of prop:sp-visible, l. 260-262); and c_0(ι), c_1(ι), c_2(ι), c_3, the coefficients of P_l in κ (lem:sp-exceptional).
Each is defined where it is used. The only two that share a proof are c_i and c_τ(ϰ_0) in thm:sp-reduction, and they
cannot be confused: the subscript is an integer step in one and a type in the other, and c_τ always carries (ϰ_0).
lem:sp-exceptional uses neither the weight nor c_τ. No change needed; not a finding.

## 3. The diff and the contract

- **The diff contains only these changes.** git diff b571483c HEAD for the two files is byte-identical to
  scratch/f3_is_sp/is-sp.diff, and a word-level comparison of the b571483c texts with the current ones shows exactly:
  IS-N2's two insertions; IS-N1's three replacements; IS-F1's replacement and the deletion of "in (2)"; SP-N1 (i)'s
  declaration; the 24 renamings μ_i → ν_i; SP-N2's "proof of"; SP-F1's "where" and "δ_50 < 2·10⁻⁸ ([[eq:iii-i9-1-1]],
  [[def:ec-point]])" for "1/4". Nothing else moved.
- **lint.** python3 lint.py proofs/P-U71-IS.md proofs/P-U71-SP.md: 249 hits, every one "reference to undefined
  label"; all 95 distinct keys are defined in chapters/ or proofs/, and none of the 58 labels of the two texts is
  defined twice there. The 247 → 249 change is exactly SP's two new occurrences of def:ec-point and eq:iii-i9-1-1
  (lint counts per occurrence; IS's new [[cor:sp-lstar]] resolves within the two-file run). No forbidden word in the
  changed lines.
- **Lines.** Longest line 121 characters in both texts (counted as characters, not bytes). No wrapped line starts with
  "+ ", "- ", "* ", "> ", "#", "=" or "|"; the only lines that do are headings and the table of IS l. 450-480, as
  before. The fix texts above are wrapped to at most 121 with no such start.
