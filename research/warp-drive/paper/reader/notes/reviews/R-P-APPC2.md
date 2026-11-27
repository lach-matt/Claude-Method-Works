# R-P-APPC2: independent line-by-line reading of proofs/P-APPC2.md

File: `proofs/P-APPC2.md`, md5 17ddd6468c288a0af34a64bac0e52ab7, 1,412 lines, at HEAD 1789660d (branch
ccr-af9edcf6-9a60sz). Appendix C, "The certified approximant", rewritten so that each seed's approximant is defined by
an exactly specified rule. Line numbers below are those of this file unless stated otherwise.

Scratch work (all under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpappc2/`):
`research/...` (scratch tree of the file as given), `fixedtree/research/...` (scratch tree of the fixed copy),
`P-APPC2.fixed.md` (the fixed copy, md5 fca513baf5f0294263139544438ffdc4, 1,422 lines), `xwalk.py`, and in `work/`:
`rhscmp.py` (right-hand side, paper against program), `regcheck.py` and `detcheck.py` (right-hand side against
eq:appc-regular), `fn.py` and `spot.py` (the functions and spot values in exact integers), `nodes.py`, `layout.py`,
`recip.py` (the measurement behind the Major), `pou.py`, `mkfixed.py` (builds the fixed copy from the file by
exact replacements). Everything ran under `nice -n 19` on one core. No repository file was edited, nothing was
committed, and no process was killed.

## Summary

The rule is very nearly a complete definition. The 𝔽 part (320-bit floor arithmetic) determines every integer: each
operation, rounding, order and count is stated, and I found no reading under which two careful implementations of the
𝔽 part disagree. The right-hand side matches the solver's generated program symbol by symbol (236 of 236 definitions,
compared as parse trees), and in exact arithmetic it solves the five equations of eq:appc-regular exactly. So the
pending identity appc-evolution-identity is true, and its marker is honest. All nine case-independent spot values come
out bit for bit from my own exact-integer implementation of def:appc-functions and def:appc-rule-seed. The layouts are
admissible as stated, and the certification propositions still hold with the inner-nine-tenths condition relaxed.

There is one Major finding. In the binary64 part (def:appc-iteration (iv)), two of the text's own instructions give
different values for the reciprocals 1 ⊘ h_ξ, 1 ⊘ h_v, 1 ⊘ e₂, 1 ⊘ e₃ and 1 ⊘ u_ξ, and the two values differ in the last
bit for about a third to a half of the actual numbers. So the integers are not uniquely determined. There are also ten
minor findings and several nits. One minor finding matters beyond wording: under layout B, the hypothesis of
lem:appc-approximant can never be satisfied.

Each finding has an exact replacement, and all of them are applied in the fixed copy, which passes every mechanical
check.

## Mechanical checks

The scratch tree comes from `git archive 1789660d`, with the appendix (lines 1–1248) placed as
`chapters/97-approximant.md`, after Appendix B (96-tables) and before the references, as Placement item 1 says. The
crosswalk rows are in `crosswalk/97-approximant.tsv`.

| check | file as given | fixed copy |
|---|---|---|
| `lint.py --chapters` | 13 hits, all pending markers | 13 hits, all pending markers |
| `assemble.py --check` | labels 5335, problems 0 | labels 5335, problems 0 |
| in-memory assembled lint | `[] 26` (13 markers counted twice) | `[] 26` |
| crosswalk rows | 90 rows = 90 labels, each at the line it names, in order, 4 columns, no duplicates | the same, line numbers regenerated |
| lines ≤ 121 in the appendix text | yes (only the tab-separated crosswalk rows are longer, as in other crosswalk files) | yes |
| labels lowercase | yes | yes |
| wrapped lines starting with a marker | none; every line starting with "- " is a list item | none |
| file or program names or code in the text | none (SHA-256, ASCII, binary64 and IEEE are names of standards) | none |

The appendix numbers as Appendix C (sections C.1–C.7, with twelve subsections in C.2).

## 1. Is the definition unique?

I went through every operation in sec:appc-rule to sec:appc-digest. Everything below is uniquely determined:

- Rounding:
  - ⌊·⌋_B floors negative values too;
  - every rational constant q stands for ⌊q⌋_B;
  - √ is ⌊√x⌋_B;
  - ⟨a, g⟩ is an exact sum rounded once;
  - z = ⌊10^p C + 1/2⌋ has its ties fixed.
- Precedence: ⊙ and ⊘ bind equally, more strongly than + and −, and are applied from the left. An integer written before
  a bracket or symbol is an exact multiple. Leading minus signs only ever stand before a single symbol or before a
  bracket that encloses the whole expression, and inside sums every "− (q) ⊙ …" is a binary minus.
- The functions, π̂, L̂₂ and ĉ(j, n), including the reduction of j modulo 2n and the exact endpoint values.
- The nodes: ĉ(0, n) = 1 and ĉ(n, n) = −1 exactly, so τ^L_0 = −1, τ^L_p = τ^R_p = 1, and the element nodes hit the box
  ends.
- The matrices: floors of exact rationals on the rounded nodes, with QQ formed from the rounded Q.
- The seed: 80 bisection steps, then 6 Newton steps.
- The grid. ξ^(n_c) = ξ_e and v^(n_r) = v_e hold exactly.
- The cone data and the N_Ray sweeps. The ρ that is passed on is the one formed in the last sweep, and Γ is taken after
  the last replacement.
- The boundary terms, the jets, the right-hand side, the Goursat map and the edges. The top values use the Φ of the last
  evaluation of P, which is at the G before the last update; that is well defined.
- Resampling.
- The cell of an element node, with its tie rule and nodes outside the grid. I checked the extreme nodes in 𝔽: the first
  v-node of the first v-box is exactly 1/2, the last v-node is v_e − 2^(−320), the first ξ-node lies below ξ̂₀, and the
  last ξ-nodes are at most ξ_e. All of them are handled by the stated rule.
- The DCT order and z.
- The counts: N_o, N_i, N_Ray, 45, 22, 70, 80 and 6 are all fixed. The only data-dependent branches are k in exp and in
  sin/cos, m in log, ν, and "r = 0 leaves G unchanged". Each is determined, and none stops early.
- The segment boundaries, which are column sets.
- The digest: SHA-256 of the bytes, written in lowercase hex.

What is not determined is listed as M-1, m-1, m-2, m-9 and m-10 below.

## 2. The binary64 part

- **Rounding:** round to nearest with ties to even, each operation rounded once. That excludes fused multiply-add and
  double rounding through extended precision.
- **Subnormals:** included, with e = −1074 and m < 2^52. The tie between 0 and ±2^(−1074) is not defined, because 0 has
  no mantissa (m-1).
- **Overflow:** rd is undefined for |y| > (2^53 − 1)2^971. The text departs here from IEEE: IEEE rounds values between
  the largest double and the overflow threshold down to the largest double. This is harmless, since
  rem:appc-rule-defined makes the rule undefined there (n-5).
- **Signed zero:** 𝔻 has one zero. No operation of the rule can tell the sign of a zero: the only divisions in 𝔻 are by
  3 and by ē₄, and d enters 𝔽 only through ⌊2^(−ν) d⌋_B. So an IEEE implementation agrees.
- **Order of every sum:**
  - ⟨·,·⟩_𝔻 is taken in the order of the index;
  - the pair evaluation of (c) runs from the left, in the order written;
  - the D-quantities have two-term sums;
  - Ṡ is fully bracketed.

  Only the word "increasing" is missing (n-3).

**Feeding the outer step.** The inner sweeps' result d enters the rule only through (iii): G := G + ⌊2^(−ν) d⌋_B in 𝔽.
So the certificate, which is a theorem about whatever integers come out, is unaffected by the binary64 part. Its
validity holds for any d. What does depend on 𝔻 bit for bit is which integers the rule defines, and with them the
digests and spot values. That is why M-1 is Major even though the certificate is untouched.

## 3. The right-hand side (eq:appc-rhs)

**Paper against program.** `rhscmp.py` parses lines 346–650 of the paper and solver/rhs_gen.h. Each K[i] is replaced by
KNUM/KDEN, and the symbols are mapped (R⁻¹ ↔ iR, e^S ↔ ES, e^(−S) ↔ iES, Ω² ↔ OM2, Ω⁻² ↔ iOM2,
X_R…X_s ↔ XR…Svv). Both sides are parsed into trees with the same rules: ⊙/* left-associative and binding more
strongly than +/−, and unary minus. Result:

- 236 definitions on each side, the same names in the same order;
- 0 differences;
- the constants, the factor order of every product, the nesting of every bracket and the order of every sum are
  identical.

solver/gen.py emits exactly the shape the paper prints: left-associative product chains, powers as chains, and
subtraction of positive-coefficient terms.

**Program against the evolution system.** `regcheck.py` is my own transcription of eq:appc-regular from the paper's text
(lines 882–935, with ℓ, S, P, Q from eq:tl5-derivatives). It is not the solver's regform.py. At 30 random rational
points, in exact rational arithmetic, with the jets random and e^S and Ω² as independent positive symbols:

- f̃_11 − f̃_xx vanishes at x = −1, and f̃_22 − f̃_xx at x = 1, so the polynomial divisions of rem:appc-rhs-origin are
  exact.
- Setting R_uv, m_uv, n_uv, W_uv and s_vv to the paper's X_R, X_m, X_n, X_W and X_s, evaluated exactly, makes all five
  of (f̃_11 − f̃_xx), (f̃_22 − f̃_xx), f̃_xx, f̃_ln and f̃_lx vanish exactly, for arbitrary values of every other second
  derivative.
- Negative controls fire. Changing t₁'s constant from 1/4 to 1/3, or dropping a factor from t₂₂₅, breaks the identity
  at every point.

`detcheck.py` confirms the rest of the identity:

- the 4 × 4 system in (R, m, n, W)_uv has determinant exactly −1/(Ω⁸R), as Placement item 2 says;
- f̃_lx contains none of those four unknowns;
- the coefficient of s_vv in f̃_lx is nonzero.

So the identity that rem:appc-rhs-origin states and marks pending is true, the 236 definitions compute exactly that
solution, and the marker is labelled honestly: what is missing is a written derivation. The remark rightly says that
neither the definition nor the certificate uses it.

## 4. Elementary functions and constants

Each algorithm is fully specified, with its range reduction, its fixed term counts, its rounding and the order of its
operations, and is well defined on its stated domain. The text states no error bounds ("the accuracy of these
functions plays no part"), so there is none to check.

`fn.py` implements def:appc-arith, def:appc-functions and def:appc-rule-seed in exact Python integers, written from the
text alone. All nine printed spot values match bit for bit:

| value | match | error against the true value, in units of 2^(−320) |
|---|---|---|
| π̂ | yes | −15.7 |
| L̂₂ | yes | −92.3 |
| ξ̂₀ | yes | +1202 |
| â | yes | −0.15 |
| λ̂ (2nd seed) | yes | −1.56 |
| R_s(ξ̂₀, 1/2) | yes | −13418 against the root r_s of eq:cone-v |
| exp 1 | yes | −18.0 |
| log 3 | yes | −186 |
| sin 1 | yes | −7.5 |

R_s(ξ̂₀, 1/2) = 10.24756039016491688190697…, which agrees with r_s = 10.2475603901… of eq:cone-v.

The nodes:

- `nodes.py`: the Lobatto and Radau nodes increase for p = 26, 28, 30, 39, 42 and 45; no Radau node is −1; the angular
  nodes decrease for M = 104, 136, 152, 168, 184, 200 and 328.
- The text states these properties for every p ≥ 1 and every M, which fails for astronomically large degrees (n-1).
- In 𝔽 the computed cosines are not antisymmetric: ĉ(n − j, n) ≠ −ĉ(j, n) at every j for n = 184. That is harmless,
  since the text never assumes it.

## 5. The certification sections

- The draft's "the tables give" and "printed" have become "the rule gives", "stated" and "the integers z" throughout. I
  diffed the kept sections against proofs/P-APPC.md: only the wording changed, together with the outcomes table.
- The inner-nine-tenths condition is relaxed at ξ = ξ₀ and v = 1/2:
  - prop:appc-element-bound uses no property of 𝔅 beyond being a sub-box of [−1, 1]³ with rational data. For the first
    element, 𝔅 still lies in [−1, 1]³: t(ξ₀) = −1 + 3.3 × 10⁻⁵, which rounds outward to −1.000, and σ(1/2) = −1
    exactly.
  - lem:appc-analytic's hypotheses are checked per element, and its ellipse may reach below u = −10 and below v = 1/2,
    where the seed and the polynomials are holomorphic.
  - prop:appc-overlap needs only U_ij inside the region and the polynomials defined there.
  - eq:appc-certificate is unaffected.
  - All three propositions hold as stated.
- What the relaxation breaks is lem:appc-approximant, whose hypothesis can no longer be met (m-4).
- The targets table matches notes/reports/G0h.md divided by 10 (f / ϱ = −31.2 / −31.3, −38.5 / −38.6, −35.4 / −35.9
  for (1, D_A), (1, D*), (2, D*)), and ϱ_t is the stricter target in each row.

## 6. Layouts, elements and the partition of unity

`layout.py` checks the layouts in exact rationals, with ξ₀, ξ_A and ξ* to 40 digits.

- Every case is admissible.
  - Smallest margins in ξ: 2.01 × 10⁻⁵ (the first box against ξ₀) and 3 × 10⁻⁴.
  - In v: 0 at v = 1/2 by construction, and 7 × 10⁻⁵ at v = 7/2.
- The u-boxes to three decimals are as printed in all three cases.
- The extension beyond the region at the other edges is 5.105 % (1, D_A), 5.025 % (2, D*) and 5.027 % (1, D*) in ξ, and
  5.004 % in v. "About one twentieth" is right, and the 5.1 % is (1, D_A).
- The first ξ-box begins 1.81 × 10⁻⁴ below u = −10, which the text rounds to 2 × 10⁻⁴ (fine).
- The gap −1821/200 − ξ₀ is 2.0131 × 10⁻⁵, not 2.02 × 10⁻⁵ (m-5).

The element-node ownership rule (least i with ξ_a ≤ ξ^(i+1), least j with v_b ≤ v^(j+1)) is determined, and covers the
extrapolated first ξ-node. M_e is in practice unambiguous: in (1, D*) the M change falls at column 48, ξ ≈ −5.664, and
the last nodes of the first two ξ-boxes, −7.447 and −5.943, lie below it. The wording is tightened anyway (n-6).

For the partition of unity, `pou.py` sampled sup |Φ^(k)| on [0.02, 1/2] and finds every φ_k an upper bound:

| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| sampled sup | 0.5 on (0, 1/2], 1 on ℝ | 2.000 | 9.841 | 110.6 | 2280 | 7.72e4 | 4.82e6 |

But φ₁ = 2 is attained at s = 1/2, so the proof's interval enclosures cannot deliver it (m-7).

## 7. What is claimed as proved

All 13 pending markers name genuine open items:

- lem-tl5-cip-axis, -f3-residual and -l7-rates (carried over);
- appc-evolution-identity (true, but no derivation is written);
- computational-appc-parameters (×2), -targets, -1a, -2d, -1d and -spot;
- ref-ieee-754 and ref-fips-180-4.

The "⟨to be entered⟩" slots of the spot list lie outside the line that carries the spot marker (n-7). Other claims
needing comment are m-3 to m-8 and n-1. Nothing else is claimed beyond what is shown.

## Findings

### Major

**M-1 (lines 716–721, def:appc-iteration (iv)): the reciprocals in 𝔻 are defined twice, differently.**

- **Reading A.** The parenthetical says the cell's numbers are each replaced by their rd, and lists 1 ⊘ h_ξ, 1 ⊘ h_v,
  1 ⊘ e₂, 1 ⊘ e₃ and 1 ⊘ u_ξ among them. So each is rd of its value in 𝔽.
- **Reading B.** The first bullet forms the D-quantities from (b) "with … ⊘_𝔻 in place of ⊘", and the last bullet forms
  I_𝔻 from eq:appc-rule-int "with the operations of eq:appc-short in place of those of eq:appc-arith". Read literally,
  this re-forms the same subexpressions as 1 ⊘_𝔻 rd(h_v) and so on.
- **They differ.** On case (1, D_A), `recip.py` finds rd(1 ⊘ y) ≠ rd(1/rd(y)) for:
  - 32 of the 62 cell half-widths h_ξ, h_v;
  - 26 of the 80 values e₂, e₃ at the row-0 v-nodes;
  - 31 of the 108 values u_ξ at the ξ-nodes of the first four columns.
- **Consequence.** A one-ulp change in a factor of I_𝔻 changes d, so G after the update differs by about 2^(−53) of the
  correction. With a last correction near 10⁻⁴⁵ that is far above 2^(−320). So the hand-off digests differ, and z
  differs with positive probability per coefficient.

The output is not uniquely determined.

Replacement (applied). Old:

    e₂, e₃, e₄, 1 ⊘ e₂, 1 ⊘ e₃, u_ξ, 1 ⊘ u_ξ and the angular nodes; a rational constant q stands for rd q):
    - the D-quantities Ḋ^F, Ḋ^F_x, Ḋ^F_xx, Ḋ^F_v, Ḋ^F_vx and Ḋ^F_u are those of (b) of [[def:appc-cell]] with d in place
      of G, ⊗ in place of ⊙, ⊕ in place of +, ⊘_𝔻 in place of ⊘ and ⋆^𝔻 in place of ⋆ (the integer multiple 4(·) is 4 ⊗ (·));

New:

    e₂, e₃, e₄, 1 ⊘ e₂, 1 ⊘ e₃, u_ξ, 1 ⊘ u_ξ and the angular nodes; a rational constant q stands for rd q). Each reciprocal
    in this list is one number, the rd of its value in 𝔽, and is not formed again in 𝔻; the only divisions formed in 𝔻 are
    the division by 3 in Ṡ below and the division by e₄ in [[eq:appc-rule-int]], both by ⊘_𝔻:
    - the D-quantities Ḋ^F, Ḋ^F_x, Ḋ^F_xx, Ḋ^F_v, Ḋ^F_vx and Ḋ^F_u are those of (b) of [[def:appc-cell]] with d in place
      of G, ⊗ in place of ⊙, ⊕ in place of + and ⋆^𝔻 in place of ⋆ (the integer multiple 4(·) is 4 ⊗ (·));

Reading A is what the list states, and it is the cheaper of the two. If the author prefers reading B, the replacement
is to delete the five reciprocals from the list instead. Either way the text must say one of them.

I checked separately that "a rational constant q stands for rd q" is unambiguous for the 29 constants of eq:appc-rhs:
rd q = rd ⌊q⌋_B for every one of them.

### minor

**m-1 (line 694): the tie between 0 and the least subnormal.** "Of two equally near the one with even mantissa" does not
cover y = ±2^(−1075), because 0 has no mantissa in the definition. This never happens in practice, but it is a gap in a
definition.

- Old: `nearest to y, and of two equally near the one with even mantissa; rd y is not defined for larger |y|. For x, y ∈ 𝔻 and`
  / `finite families a, g in 𝔻 of equal length n,`
- New: `nearest to y, and of two equally near the one with even mantissa, 0 counting as even; for larger |y|, rd y is not`
  / `defined. For x, y ∈ 𝔻 and finite families a, g in 𝔻 of equal length n,`

**m-2 (lines 755–756, 843, 848): the orders in the canonical strings.** The hand-off string says "for each row j"
without saying in which order. The block lines are "in the order of a and then b", and the blocks "in the order of i,
then j". The intended orders are increasing, but the digests are fixed data of the paper, so the text should say so.

- Hand-off. Old: `[[def:appc-canonical]]: for each row j, each F in the order R, m, n, W and each b in increasing order, one line made of`.
  New: `[[def:appc-canonical]]: for each row j in increasing order, then each F in the order R, m, n, W, then each b in` /
  `increasing order, one line made of the word "edge", …` (reflowed over three lines).
- Block lines. Old: `in the order of a and then b, a line with a, b and then`. New: `in increasing order of a and, for equal a, of b,
  a line with a, b and then` (reflowed).
- Case. Old: `in the order of i, then j, then F in the order R, m, n, W, s.` New: `in increasing order of i, then of j, then F in
  the order R, m, n, W, s.`

**m-3 (line 724): "the other twenty-four jets" is wrong.** There are 31 jets, six of them with special tangents (R, R⁻¹,
e^S, e^(−S), Ω², Ω⁻²); S is not a jet. That leaves twenty-five. Old `twenty-four`, new `twenty-five`.

**m-4 (lines 107–108, 110–111, 122): lem:appc-approximant cannot apply under layout B.** The v-boxes are now
[1/2, 21231/10000] and [18769/10000, 7171/2000], so ⋃B_ij lies in {v ≥ 1/2}. No open set 𝒪 ⊂ ⋃B_ij of the plane
contains a point of the region with v = 1/2, so the lemma's hypothesis is never satisfied, and its conclusion (a smooth
Lorentzian metric on a neighbourhood of the region) is not available. The draft's first v-box began at 829/2000, so the
problem is new.

Lines 107–108 also say each term "is defined where χ_iψ_j ≠ 0, which is inside B_ij by lem:appc-pou (b)". On the plane
this is false: χ₁ψ₁ = 1 below v = 1/2. And the premise is unnecessary, since the G^F_ij are polynomials.

The citation of lem:tl5-seed (b) for the seed's smoothness covers only −10 ≤ u < 0, while the first ξ-box reaches
u = −10.0002.

Replacements (applied):

- Lines 107–108. Old: `Each term of the sum is defined where χ_iψ_j ≠ 0, which is inside B_ij by [[lem:appc-pou]] (b), so the fields are`
  / `defined on the region and on a neighbourhood of it in the union of the boxes.` New: `Each G^F_ij is a polynomial in t
  and σ, which are affine functions of ξ and v, so the fields are defined wherever the` / `seed's are. [[eq:tl5-seed-radius]]
  and [[eq:tl5-seed-lapse]] define R_s and W_s, real-analytic, for every u < −1 and` / `every v, by the argument of
  [[lem:tl5-seed]] (a) and (b), which does not use u ≥ −10 or v ≥ 0; so the fields are` / `defined and smooth on {ξ < 0},
  which contains the region and the boxes.` I checked the claim: for u < −1 the right side of eq:tl5-seed-radius is
  positive for every v, and F maps (1, ∞) onto (0, ∞).
- Line 111. Old: `an open set 𝒪 ⊂ ⋃ B_ij containing the region. Then:`. New: `an open set 𝒪 ⊂ {ξ < 0} of the (ξ, v)-plane containing
  the region. Then:`
- Line 122. Old: `… since the seed's are ([[lem:tl5-seed]] (b)), the polynomials are, and so`. New: `… since the seed's are on
  {ξ < 0}, the polynomials are, and so`.

**m-5 (line 57): the gap is 2.01, not 2.02.** −1821/200 lies 2.0131 × 10⁻⁵ below ξ₀ = −9.104979868664…, so "2.02 × 10⁻⁵"
should be "2.01 × 10⁻⁵". Old `2.02 × 10⁻⁵ below ξ₀`, new `2.01 × 10⁻⁵ below ξ₀`.

**m-6 (lines 812–817): rem:appc-rule-defined's list of divisors is wrong in three ways.**

1. It omits divisors that depend on what the rule forms: the seed's own u₁ − 2, q + 1, R + 1, R ⊙ R − 1,
   2 + 2 ⊘ (R ⊙ R − 1), R ⊙ R, u ⊙ u, g and R ⊙ R ⊙ R, and the cone data's z, λ̂, r ⊙ √r and 1 + x ⊙ x. It also omits
   the square-root argument r.
2. It lists η₄, which is never a divisor (B divides by e₄).
3. Its split ("depend on the values the rule forms, and not on the parameters alone") puts R_s, Ω_s² and u_ξ on the
   wrong side, since they depend on the node alone.

Since the remark ends in a pending check anyway, the replacement drops the split and states the condition once.

- Old (from `logarithm or square root meets a nonpositive argument` through `the arguments positive, at every step
  [[pending:computational-appc-parameters]].`).
- New: `logarithm meets a nonpositive argument, no square root a negative one, and no rounding rd a number beyond the range of`
  / `𝔻. For the parameters of [[sec:appc-parameters]] this holds at every step: every divisor of the rule (among them the`
  / `differences of nodes, h_ξ, h_v, e₂, e₃, e₄, z, λ̂, r ⊙ √r, u₁ − 2, R ⊙ R − 1, g, u_ξ, Ω_s² and R_s + D^R) is nonzero,`
  / `and every argument of a logarithm or a square root has the sign required [[pending:computational-appc-parameters]].`
- The marker count is unchanged.

**m-7 (lines 75, 85–86, kept from the draft): φ₁ = 2 is true but not proved.** sup |Φ′| = Φ′(1/2) = 2 exactly. The proof
covers [1/100, 1/2] by interval enclosures whose "largest end points, times k!, are at most φ_k", but an enclosure over a
sub-interval of positive width containing 1/2 has an upper end above 2. So for k = 1 the stated argument cannot deliver
φ₁ = 2. The bound itself is true, and has a two-line proof (checked numerically at four points).

- Old: `times k!, are at most φ_k. On (0, 1/100] use Cauchy's estimate on the disc |z − s| ≤ s/2: there Re(1/z) ≥ 2/(3s),`
- New: `times k!, are at most φ_k for k ≠ 1. For k = 1 the bound is attained, Φ′(1/2) = 2, and is shown directly: with` /
  `t := s(1 − s) ≤ 1/4 and g := (1 − 2s)/t one has Φ = 1/(1 + e^g), Φ′ = (1 − 2t)/(4t² cosh²(g/2)) and` /
  `4t² cosh²(g/2) ≥ 4t² + t²g² = (1 − 2t)², so that 0 < Φ′ ≤ 1/(1 − 2t) ≤ 2 on (0, 1). On (0, 1/100] use Cauchy's` /
  `estimate on the disc |z − s| ≤ s/2: there Re(1/z) ≥ 2/(3s),`

**m-8 (lines 76–78, kept from the draft): lem:appc-pou (b) holds only on the region.** "χ_i vanishes outside
[c_(i−1) − d, c_i + d]" is false for i = 1 below c₀ − d := ξ₀ (χ₁ = 1 − Φ₁ = 1 there) and for i = n_ξ beyond the region.
It is true on the region, which is all prop:appc-overlap uses. Old `Σ_j ψ_j = 1; χ_i vanishes outside [c_(i−1) − d,`
(three lines), new `Σ_j ψ_j = 1; on the region, χ_i vanishes outside` (reflowed, same three lines).

**m-9 (lines 303–304, 748–749): resampling between segments of equal M.** The text resamples at every segment boundary,
including 184 → 184 at every boundary of (1, D_A) and (2, D*). In 𝔽 that resampling is not the identity, and an
implementer who treats equal M as a no-op gets different integers. The text means it (line 303: "when cell (i − 1, j)
belongs to another segment"), but it should say so. By contrast, element values are resampled only when M differs.

- Old: `for each node v_b, from the M of the sending segment to the M of the receiving one.`
- New: `for each node v_b, from the M of the sending segment to the M of the receiving one, also when the two are equal.`
- If the author intended no resampling at equal M, the alternative is "… to the M of the receiving one, when the two
  differ", together with the same condition on line 304.

**m-10 (lines 777–778): the Lagrange bases in the element values.** "The Lagrange bases ℓ^ξ of its ξ-nodes (Lobatto,
degree p_ξ)" can be read as the basis of the cell's physical nodes ξ_a. Mapped back, those differ from τ^L_a by
rounding, while τ* is a reference coordinate.

- Old: `bases ℓ^ξ of its ξ-nodes (Lobatto, degree p_ξ) and ℓ^v of its v-nodes (Radau or Lobatto, degree p_v), the value of a`
  / `field at (ξ_a, v_b, x_k), x_k an angular node of the cell's M, is`
- New: `bases ℓ^ξ of the Lobatto family τ^L of degree p_ξ and ℓ^v of the cell's v-family τ_b of degree p_v ([[def:appc-grid]];`
  / `Radau in row 0, Lobatto otherwise), the value of a field at (ξ_a, v_b, x_k), x_k an angular node of the cell's M, is`

### nits (applied unless stated otherwise)

**n-1 (lines 198–200): the node properties hold only for the degrees used.** "Both families increase with j … the Radau
nodes do not contain −1" and "they decrease" are stated for every p and M. That is true for every degree used (checked)
but false for astronomically large degrees. Also, "the integer M of the case" should be "of a segment", since (1, D*)
has two values of M. New text: `… τ^L_0 = −1` / `and τ^L_p = τ^R_p = 1, and for every degree used below both families
increase with j and no Radau node equals −1. For` / `an integer M ≥ 1, the angular degree of a segment, the angular nodes
are x_k := ĉ(k, M), k = 0, 1, …, M; x₀ = 1 and` / `x_M = −1, and for every M used below they decrease.`

**n-2 (line 213): the floor convention for W, V, D¹ and D².** The convention "each entry is ⌊e⌋_B" is stated before the
display of Q, D, QQ, but W, V, D¹ and D² follow in later sentences. Added: `The entries of W, V, D¹ and D², too, are the`
/ `floors ⌊e⌋_B of the exact rational numbers e shown.` (reflowed).

**n-3 (line 700): the summation order.** "The sum taken in the order of the index" becomes "in increasing order of the
index".

**n-4 (lines 318–319): the scope of the parentheticals in (b).** The scopes "(F = R, m, n)" and "(F ≠ s)" each attach to
one item of a comma list, but G^s_x and G^s_v are needed. New display:
`G^F_v := …,   G^F_x := D¹ ⋆_k G^F,   G^F_vx := D¹ ⋆_k G^F_v   (every F),` /
`G^F_ξ := …  (F = R, m, n),   G^F_xx := D² ⋆_k G^F  (F ≠ s),`.

**n-5 (lines 702–703): the IEEE sentence.** "These are the operations of the binary64 format …" holds only where rd is
defined, and only with one zero. New: `Where rd is defined these are the operations of the binary64 format of the IEEE
standard [[pending:ref-ieee-754]], with rounding to nearest and ties to even, each operation rounded once, subnormal
numbers kept, and a zero of either sign read as 0.`

**n-6 (line 769): M_e.** "Whose cells contain one of the element's nodes" could mean geometric containment, under which a
node on a breakpoint lies in two cells. New: `M_e be the largest M of the segments that contain the column i_c of the cell
(i_c, j_c), defined below, of one of the` / `element's nodes.`

**n-7 (lines 1239–1247): the spot list.**

- The pending marker covers the whole list but sits on its fourth item, so the "⟨to be entered⟩" slots of items 1–3 and 5
  are on unmarked lines. The fixed copy moves it to the lead-in, `**Per case.** For each of the cases (1, D_A), (2, D*)
  and (1, D*) [[pending:computational-appc-spot]]:`, which keeps the count at 13.
- "(ξ₀, v₀)" collides with ξ₀ := −arsinh 4500 and becomes "(ξ_0, v_0)".
- "The latter after the N_Ray sweeps" becomes "G_R after the N_Ray sweeps".

**n-8 (not changed): local names.** The local names κ, h, α₁, α₂ and z of def:appc-rule-data also denote the contact order
κ = 4, the layout's α_i, the α₁ of eq:appc-hat and the integers z_abk. N₁ (the cone) also names an interpolation degree in
lem:appc-coefficients. Every use is local and no ambiguity arises.

**n-9 (crosswalk).** The notes of the rows lem:appc-pou, lem:appc-approximant and def:appc-short are updated in the fixed
copy to say what changed. All 90 rows' line numbers are regenerated against the fixed copy.

## The fixed copy

`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpappc2/P-APPC2.fixed.md`
(md5 fca513baf5f0294263139544438ffdc4, 1,422 lines) is produced by `work/mkfixed.py` from the file as given. It applies
25 exact replacements, each asserted to occur once, and then regenerates the crosswalk line numbers.

The right-hand side block is byte-identical to the original. Tested in a fresh scratch tree with the same placement:

- lint --chapters: 13 hits, all pending markers;
- assemble --check: 0 problems;
- in-memory assembled lint: `[] 26`;
- crosswalk: 90 rows matching 90 labels at their lines, in order;
- no text line over 121 characters;
- no wrapped line starting with a marker.

Verdict: NOT CONFIRMED
