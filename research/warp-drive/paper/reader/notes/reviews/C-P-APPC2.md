# C-P-APPC2: confirming read of proofs/P-APPC2.md (Appendix C, "The certified approximant")

**File read:** proofs/P-APPC2.md at 446f53e8, md5 fca513baf5f0294263139544438ffdc4, 1,422 lines:
- appendix text 1–1258 (Appendix C, 90 labels);
- Placement 1260–1335;
- crosswalk rows (90).

**Review being confirmed:** notes/reviews/R-P-APPC2.md (on 1789660d, md5 17ddd646…, 1,412 lines): NOT CONFIRMED, 1 Major (M-1), 10 minor (m-1 … m-10), 9 nits (n-1 … n-9; n-8 unchanged by decision).

**Also read:**
- the whole of sec:appc-rule through sec:appc-digest in the fixed copy: the arithmetic, the functions, the nodes, the seed, the grid, the cone data, the cell map with the sequence of eq:appc-rhs, the short arithmetic, the iteration, resampling, the hand-off, the element values, the parameters, the properties, the canonical string and the digest;
- the lemma of the partition of unity and the approximant;
- the spot section;
- lem:tl5-seed and eq:tl5-seed-radius/-lapse in chapter 87 at 446f53e8 (87:512–568).

I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/cappc2/.

## Verdict in brief

All 25 replacements resolve their findings correctly and completely, and none introduces a new error or ambiguity in the appendix text. Nothing outside the findings changed.

**The binary64 part now leaves an implementation no choice.** I re-read every 𝔻 operation of def:appc-short and def:appc-iteration:
- each has its operands, its order and its rounding fixed;
- each reciprocal is one number, the rd of its 𝔽 value;
- the only 𝔻 divisions are ⊘_𝔻 3 in Ṡ and ⊘_𝔻 ē₄ in eq:appc-rule-int.

**The other findings checked closely:**
- m-1 matches IEEE's tie at ±2^(−1075).
- m-2 fixes every order of the canonical strings.
- m-4 makes lem:appc-approximant's hypothesis satisfiable, and its new seed claim is true.
- m-7's direct proof of φ₁ = 2 is correct.
- m-9 states the writer's reading.
- m-6, m-8 and m-10 are right.

**Pending markers:** the 13 are honest.

**Mechanical checks:**
- lint gives 13 hits, all pending markers;
- assemble --check gives 0 problems;
- the in-memory check gives `[] 26`;
- the 90 crosswalk rows point at their labels;
- no printed number of the 5250 old labels changes.

**One optional tidy (not required):** the crosswalk note of def:appc-short now says "reciprocals rounded from F", but that rule is in def:appc-iteration (iv). A tested replacement moving the note is given at the end.

## What changed between 1789660d and 446f53e8

`git diff 1789660d 446f53e8 -- research/warp-drive/paper/reader/proofs/P-APPC2.md` changes exactly these appendix lines of the fixed copy, each by the review's replacement text:

| Finding | Lines |
|---|---|
| m-5 | 57 |
| m-8 | 76–78 |
| m-7 | 86–89 |
| m-4 | 110–113, 116, 127 |
| n-1 | 203–206 |
| n-2 | 219–222 |
| n-4 | 325–326 |
| m-1 | 701–702 |
| n-3, n-5 | 707–710 |
| M-1 | 726–730 |
| m-3 | 733 |
| m-9 | 758 |
| m-2 | 764–766, 852–854, 858 |
| n-6 | 779–780 |
| m-10 | 788–789 |
| m-6 | 823–826 |
| n-7 | 1249, 1254–1257 |

The crosswalk rows change too: the notes of lem:appc-pou, lem:appc-approximant and def:appc-short (n-9), and the line numbers of all rows from lem:appc-pou on.

**Nothing else changed.** The right-hand-side block (fixed-copy lines 353–657) is byte-identical to the draft's lines 346–650, and the Placement text is unchanged. The commit also adds the review, other reports and files under rule/, none of which is merged text.

## Mechanical checks (scratch tree)

**Scratch tree:** `git archive 446f53e8 research/warp-drive/paper/reader`, extracted under scratchpad/reader/cappc2/tree.
- The appendix (lines 1–1258) is placed as chapters/97-approximant.md, between 96-tables and 98-references, as Placement item 1 says.
- The 90 rows, with `@PENDING:` → `@446f53e8:` and the four-column header of the other crosswalk files, are in crosswalk/97-approximant.tsv (tools/place.py).

**Results:**
- `python3 lint.py --chapters`: 63 files, 5340 labels (5250 + 90), **13 hits, all pending markers**. They are at appendix lines 130, 689, 709, 804, 826, 863, 1201, 1202, 1219, 1220, 1221, 1224 and 1249.
- `python3 assemble.py --check`: labels 5340, **problems 0**. PAPER.md was not rewritten; its md5 is unchanged.
- In-memory assembled check: prints **`[] 26`**, the 13 markers counted twice.

**Numbering:** I compared assemble.number on the trees with and without the appendix.
- **None of the 5250 old labels changes its printed number.**
- The appendix is Appendix C; sec:appc-rule is Section C.2, lem:appc-approximant is Lemma C.6, def:appc-short is Definition C.16 and def:appc-iteration is Definition C.17.

**Crosswalk:** 90 rows equal the 90 labels of the appendix, in order, each at the line it names. Every row has four columns and none is duplicated.

**Line rules on the changed appendix lines:**
- All are at most 119 characters. The longest appendix line is 121 (line 1205, unchanged).
- Lines 852 and 1254 start with "- ", and both are list items.
- No line starts with "+ ", "* ", "> ", "#", "=" or "|".
- All 90 labels are lowercase.
- There are no file or program names and no code in the text.

## M-1 — the binary64 part (def:appc-short, def:appc-iteration (iv)): RESOLVED

I re-read the whole 𝔻 part and checked each operation for its operands, its order and its rounding.

**Rounding and the elements of 𝔻** (def:appc-short).
- rd is nearest, with ties to even mantissa and 0 counting as even, and is undefined beyond (2^53 − 1)2^971.
- ⊕, ⊖, ⊗ and ⊘_𝔻 are each rounded once.
- ⟨a, g⟩_𝔻 is a left fold in increasing index, and ⋆^𝔻 is built from it.
- Negation is exact.
- A sum of more than two written terms is formed from the left, in the order written.

**The inputs** of (iv).
- J̄ = rd J(G), the 31 jets of the G of the current outer step, are 𝔽 numbers, so rd is unique.
- The cell's numbers are each rd of their 𝔽 value: the matrices Q_ξ, D_ξ, Q_v, D_v, W, V, QQ_v, D¹ and D²; h_ξ and h_v; e₂, e₃ and e₄; u_ξ; the angular nodes; and the five reciprocals 1 ⊘ h_ξ, 1 ⊘ h_v, 1 ⊘ e₂, 1 ⊘ e₃ and 1 ⊘ u_ξ, each "one number, the rd of its value in 𝔽, … not formed again in 𝔻".
- Rational constants are rd q, and the integers 2, 3 and 4 are exact.
- The barred jets in the tangent formulas (R̄⁻¹, ē^(±S), Ω̄^(±2)) are entries of J̄, and x̄ is the rounded angular node, so they agree with the list.

**The D-quantities.** (b) of def:appc-cell is transcribed with d for G, ⊗ for ⊙, ⊕ for + and ⋆^𝔻 for ⋆. Its formulas contain only products, two-term sums, ⋆, the integer multiple 4 (as 4 ⊗ ·) and the listed reciprocals:
- (D_v ⋆_b G^F) ⊙ (1 ⊘ h_v) → (D̄_v ⋆^𝔻_b d^F) ⊗ (the listed 1 ⊘ h_v);
- e₄ ⊙ G^F_ξ ⊙ (1 ⊘ u_ξ) → (ē₄ ⊗ Ġ^F_ξ) ⊗ (the listed 1 ⊘ u_ξ), left-associative;
- 4(e₃ ⊙ G^F) + e₄ ⊙ G^F_v → (4 ⊗ (ē₃ ⊗ d^F)) ⊕ (ē₄ ⊗ Ġ^F_v).

The ⊘_𝔻 that the draft had here is gone, so nothing is formed twice.

**The tangent jets.** The six special tangents are fully bracketed: Ṙ, (R⁻¹)˙, Ṡ = (((Ḋ^m ⊕ x̄⊗Ḋ^m) ⊕ Ḋ^n) ⊖ x̄⊗Ḋ^n) ⊘_𝔻 3, (e^(±S))˙, (Ω²)˙ and (Ω⁻²)˙. The other 25 tangents are the corresponding Ḋ.

**The sequence of (c) in pairs.** I parsed the 236 definitions mechanically.
- They contain no ⊘, no function call and no bare integer multiple.
- Every binary operator is ⊙, + or −.
- The only brackets are (1 + x), (1 − x), the bracket of X_R and the negations −(…).

So the stated pair rules cover every line:
- a product chain is left-associative, with value ā ⊗ b̄ and tangent (ȧ ⊗ b̄) ⊕ (ā ⊗ ḃ);
- sums and differences take ⊕/⊖ from the left in the order written;
- a negation negates both entries;
- x and the constants carry tangent 0, and 0 ⊗ y = 0 and 0 ⊕ y = y are exact.

**The output.**
- Ψ̇^F = ū_ξ ⊗ Ẋ_F and Φ̇ = Ẋ_s.
- I_𝔻(d) is eq:appc-rule-int with ⊗, ⊕ and ⋆^𝔻, and the listed 1 ⊘ e₃ and 1 ⊘ e₂ in row 0.
- In rows j ≥ 1 it is ((h̄_ξ ⊗ h̄_v) ⊗ (Q̄_ξ ⋆^𝔻 (Q̄_v ⋆^𝔻 Ψ̇))) ⊘_𝔻 ē₄, and likewise for I^s with QQ_v. The division by e₄ is stated to be ⊘_𝔻.

**The outer step.**
- r̃ = rd(2^ν r), with ν fixed by 2^(−ν) ≤ max|r| < 2^(1−ν).
- Then N_i times d := r̃ ⊕ I_𝔻(d), entrywise over all F.
- Then G := G + ⌊2^(−ν)d⌋_B.

**Conclusion.** Every 𝔻 operation is defined once. The only 𝔻 divisions are by 3 in Ṡ and by ē₄, which the new sentence states and the formulas confirm. An implementation has no choice left. Signed zero cannot be observed, since the only 𝔻 divisors are 3 and ē₄ ≠ 0 and d enters 𝔽 only through ⌊2^(−ν)d⌋_B. So the n-5 sentence, "a zero of either sign read as 0", is consistent.

## m-1 — the tie at the least subnormal (lines 700–702): RESOLVED

"0 counting as even" settles y = ±2^(−1075), the only tie involving 0: it rounds to 0, whereas the least subnormal has the odd mantissa 1. That is IEEE's round-to-nearest-even result.

## m-2 — the orders in the canonical strings (lines 764–766, 852–854, 858): RESOLVED

**Hand-off:** rows j increasing, then F in the order R, m, n, W, then b increasing, then k = 0, …, M within the line.

**Block:**
- the header first;
- then lines in increasing a, and for equal a in increasing b;
- within a line, k from 0 to K, with K the largest k with z_abk ≠ 0, and interior zeros written 0.

**Case:** blocks in increasing i, then j, then F in the order R, m, n, W, s, which is lexicographic.

Together with the integer format (decimal, no leading zeros, hyphen-minus, single spaces, a line feed after each line) and SHA-256 over ASCII bytes in lowercase hex, every digest is fixed.

## m-4 — lem:appc-approximant under layout B (lines 110–113, 116, 127): RESOLVED

**The new paragraph is true.**
- ξ < 0 ⇔ u < −1, since a > 0.
- For u < −1 the right side of eq:tl5-seed-radius, e^(v−2u)(u + 1)/(u − 1), is positive for every v.
- F is an increasing bijection of (0, ∞) onto (−1, ∞) (87:521, 533), so R > 1 exists and is unique.
- It is real-analytic by the analytic implicit function theorem, since F′ > 0, and W is real-analytic, since u ≠ 1 and R > 0 (87:539).
- That argument uses neither u ≥ −10 nor v ≥ 0.

So R_s and W_s are real-analytic on {ξ < 0}. The G^F_ij are polynomials in t, σ and x; χ_i, ψ_j and (v − 1/2)^κ are smooth on ℝ. Hence the fields are smooth on {ξ < 0}, which contains the region (ξ ≤ ξ_A or ξ*) and every box (ξ ≤ −4473/1000).

**The hypothesis is satisfiable.** The region is compact in {ξ < 0}, so if R > 0 on the region, continuity gives an open 𝒪 ⊂ {ξ < 0} containing it with R > 0. The old hypothesis 𝒪 ⊂ ⋃B_ij could not be met at v = 1/2.

The proof of (a) ("since the seed's are on {ξ < 0}") matches. The false "inside B_ij" claim is gone. lem:appc-approximant is not cited elsewhere, so nothing downstream changes.

## m-5 — the gap (line 57): RESOLVED

ξ₀ = −arsinh 4500 = −9.104979868664035…, so −1821/200 − ξ₀ = −2.0131 × 10⁻⁵. "2.01 × 10⁻⁵" is right.

## m-6 — where the rule is defined (lines 823–826): RESOLVED

The condition is now stated once: no divisor vanishes, no logarithm meets a nonpositive argument, no square root meets a negative one, and no rd falls out of range. That matches the domains in eq:appc-arith (√x for x ≥ 0) and in def:appc-functions (log y for y > 0).

Each named divisor occurs as one:
- z, in sin z ⊘ z;
- λ̂, in θ and α₃;
- r ⊙ √r, in κ;
- u₁ − 2, in H;
- R ⊙ R − 1, in the Newton step;
- g, in ∂_uR_s and Ω_s²;
- u_ξ, Ω_s² and R_s + D^R = R, in the jets;
- e₂, e₃, e₄, h_ξ, h_v and the node differences.

"among them" keeps the list non-exhaustive, so the wrong split and η₄ are gone. The marker count is unchanged. Here z is the local z of def:appc-rule-data; the output integers z are never divisors, so n-8's decision to keep the local names causes no ambiguity.

## m-7 — the direct proof of φ₁ = 2 (lines 86–89): RESOLVED

With t = s(1 − s) and g = (1 − 2s)/t:
- Φ = 1/(1 + e^g), since 1/s − 1/(1 − s) = g.
- (1 − 2s)² = 1 − 4t, so g′ = −(1 − 2t)/t². With e^g/(1 + e^g)² = 1/(4cosh²(g/2)) this gives Φ′ = (1 − 2t)/(4t²cosh²(g/2)).
- cosh²(y) ≥ 1 + y² gives 4t²cosh²(g/2) ≥ 4t² + t²g² = 4t² + (1 − 2s)² = (1 − 2t)².
- Hence 0 < Φ′ ≤ 1/(1 − 2t) ≤ 2, since t ≤ 1/4, with equality at s = 1/2, where t = 1/4 and g = 0.
- Off (0, 1), Φ′ = 0.

The interval argument is now claimed only for k ≠ 1. The proof is correct and complete.

## m-8 — lem:appc-pou (b) on the region (lines 76–78): RESOLVED

"on the region" scopes the three support claims, which hold there with c₀ − d := ξ₀ and c_(n_ξ) + d the upper end of the region. That is exactly what prop:appc-overlap uses. The first sentence of (b) (smooth, nonnegative, the sums equal to 1) holds on all of ℝ and stays outside that scope.

## m-9 — resampling at equal M (line 758): RESOLVED, in the writer's reading

"…to the M of the receiving one, also when the two are equal" makes resampling happen at every segment boundary, consistent with line 311 ("resampled … when cell (i − 1, j) belongs to another segment") and with def:appc-handoff's "before any resampling". def:appc-resample is defined for M′ = M. Element values are still resampled only when the cell's M differs from M_e (line 793), which is a separate and explicit rule.

## m-10 — the Lagrange bases of the element values (lines 788–789): RESOLVED

The bases are now those of the reference families: τ^L of degree p_ξ, and the cell's τ_b of degree p_v (Radau in row 0, Lobatto otherwise). They are evaluated at the reference coordinates τ* and ς* as ⌊ℓ_j(τ*)⌋_B (def:appc-nodes), so they are unique.

## m-3 and the nits: RESOLVED

**m-3.** There are 31 jets: R, R⁻¹, e^S, e^(−S), Ω² and Ω⁻² (6); R_u, R_v, R_x, R_xx and R_vx (5); W_v, W_x, W_xx and W_vx (4); m and n with their u, v, x, xx and vx jets (6 + 6); and s, s_v, s_x and s_vx (4). The six special ones leave **twenty-five**.

**n-1.** τ^L_0 = −ĉ(0, p) = −1, τ^L_p = −ĉ(p, p) = 1 and τ^R_p = ĉ(0, 2p + 1) = 1. The monotonicity and the absence of −1 are now claimed only "for every degree used below", and the angular degree is that "of a segment".

**n-2.** The floor convention now covers W, V, D¹ and D².

**n-3.** "in increasing order of the index".

**n-4.** The display now puts G^F_v, G^F_x and G^F_vx under "(every F)", G^F_ξ under (F = R, m, n) and G^F_xx under (F ≠ s). That matches the D-quantities and jets that are formed: D^s_v, D^s_x and D^s_vx are needed; D^s_xx and D^W_u are not.

**n-5.** The IEEE sentence is limited to where rd is defined, with subnormals kept and signed zeros read as 0.

**n-6.** M_e is fixed through the column i_c of each node's cell.

**n-7.** The spot marker now sits on the lead-in, covering every per-case slot; "(ξ_0, v_0)" is used; and "G_R after the N_Ray sweeps".

**n-9.** The three notes are updated, and the line numbers are regenerated (verified above).

## The 13 pending markers: honest

- lem-tl5-cip-axis, lem-tl5-f3-residual and lem-tl5-l7-rates are carried over.
- appc-evolution-identity (rem:appc-rhs-origin) needs a written derivation; the remark says neither the definition nor the certificate uses it.
- computational-appc-parameters (×2): the parameters are provisional, and the check of rem:appc-rule-defined is still to be done.
- computational-appc-targets, -1a, -2d and -1d: the targets and outcomes, "⟨to be entered⟩".
- computational-appc-spot now heads the per-case list, whose every item is "⟨to be entered⟩". The case-independent spot values are entered and carry no marker.
- ref-ieee-754 and ref-fips-180-4: bibliography entries.

Placement item 2 lists exactly these, so each marker names a genuinely open item.

## Optional tidy (not required): the crosswalk note of def:appc-short

The n-9 note of def:appc-short reads "…; reciprocals rounded from F". That rule is stated in def:appc-iteration (iv), not in def:appc-short. If wanted:

Old (row def:appc-short, fourth column):

    binary64 arithmetic: rounding to nearest even (0 even), ordered sums; reciprocals rounded from F

New:

    binary64 arithmetic: rounding to nearest even (0 even), ordered sums

Old (row def:appc-iteration, fourth column):

    defect correction: outer defect steps in B = 320, inner linearised sweeps in binary64

New:

    defect correction: outer defect steps in B = 320, inner linearised sweeps in binary64; each reciprocal rounded once from its value in F, divisions in binary64 only by 3 and e4

**Tested:**
- Each old text occurs exactly once.
- The variant is scratchpad/reader/cappc2/P-APPC2.variant.md, md5 47a323770aa0f5e4dc57b3b9922167bf, 1,422 lines.
- Placed in a fresh archive (tree2/), it gives lint 13 hits (all pending), assemble --check 0 problems and in-memory `[] 26`, with 90 rows at their labels.

## Scratch artefacts

All paths are under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/cappc2/:
- tree/: the placed appendix at 446f53e8;
- tree2/: the same with the optional tidy;
- orig/: the unplaced archive;
- tools/place.py: places the appendix and writes the crosswalk;
- rhs.txt: the sequence of (c), extracted for the parse checks;
- 87.md: chapter 87 at 446f53e8;
- appc2.diff: the diff.

Verdict: CONFIRMED
