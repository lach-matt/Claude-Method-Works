# R2-P-G24b: second reading of proofs/P-G24b.md

File read: `research/warp-drive/paper/reader/proofs/P-G24b.md`, md5 a44f9f97a98e435754cf15153bedef33, 1,645 lines
(committed at 373ce930, unchanged at HEAD b7553023). Diffed line by line against the first-read version (md5
ad4e510f…, commit 730b5739). Read with it: STYLE.md, notes/reviews/R-P-G24b.md, notes/reports/F-P-G24b.md, chapter 33
(at 332f13ca, md5 147ca162…, and after the P-G1 merge, md5 d2184d75…), chapters 20 and 95 where cited, proofs/P-G1.md
(md5 b2d824fb…), the head of proofs/P-RI.md, and the preprint arXiv:2606.27658v2 through the alphaXiv full text the
first reader's writer saved (scratchpad/reader/sources/hin26a-v2-fulltext.txt). Nothing under method/, drive/,
extracted/ or recovered/ was read. No repository file was edited.

**Verdict: NOT CONFIRMED.** Every first-round finding is resolved (m1–m4 and n1–n12; the mathematics of m1–m4
re-derived), T44 and T45 are correct, M1 is correctly marked as open and nothing depends on it. One new minor
remains: T35 states the forward cone estimate on {τ ≥ T/40}, which the commutant of T33 does not give (r1 below; a
one-token fix, harmless downstream). Nine nits. The scratch merges are clean, also on the actual post-P-G1 chapter.

## First-round findings

| item | status | evidence |
|---|---|---|
| M1 | open, correctly marked | see "M1" below; nit n-h on the marker's scope |
| m1 | resolved | T4 now requires a cut-off to be positive on I and 0 outside; the formula is positive on (−∞, β) (checked: χ = A/(A + B), both terms positive on (α, β)). Re-checked every site: prop:iv5-2-1 (2) needs χ_K > 0 on [0, 2] (support [0, 3)); prop:iv5-3-1 (1) needs χ_K > 0 on [0, (3/2)δ_r] and χ_sf > 0 on [0, 3/2] (supports [0, 2δ_r), [0, 2)); prop:iv5-4-1 χ_R > 0 on [−(3/2)δ_sf, (3/2)δ_sf] (support (−2δ_sf, 2δ_sf)); prop:iv5-5-1 χ_K > 0 on [0, t_2⁻¹] (support [0, t_1⁻¹), t_1 < t_2) and χ₂ > 0 on (r_1, r_4). Each E covers its derivative's support. §1 text added (nit n-a on its wording). |
| m2 | resolved | T24: ℓ_1 > −½ − h⁻¹(1 − e)(1 − v) near R_out is exactly prop:i-a-4-9 (2)'s a priori order −𝗋₀ − 1 with ℓ < 𝗋₀ < −½ + S̄; T27 states eq:iv6-1-4 in the weak sense, the strong sense of eq:iv6-1-2 and eq:iv6-1-3 through rem:i-a-7-3 (which says exactly this) and lem:i-c-2-5. |
| m3 | resolved | T33 (𝔛 := δ_r⁻¹, χ_cf = 1 on [0, 5/2], support [0, 4)), T35 (backward on τ ≥ (2.75/10)T, where χ̃ = χ_(τ,2) is 1), new T44, §6.3 bullet deleted. Re-derived: the backward a priori set {(5/2)δ_r ≤ ρ_cf < 4δ_r} ∩ {τ ≥ (2.25/10)T} lies in the reach of (c) (2) (ρ_cf ≥ 2δ_r, τ > κ = 1/9 < 0.1125); (c) (1)'s a priori set {δ_r ≤ ρ_cf ≤ 2δ_r} and s ∈ [2δ_r, 3δ_r] lie in ρ_cf < 4δ_r. The cone-face symbols' need on 𝔛 does not grow as δ_r decreases (j-terms at \|ζ\| ≤ 2𝔛⁻¹, Q-terms with C₂ a supremum over a shrinking set), so T44 is not circular (nit n-g asks to say so). But see r1 for the forward range. |
| m4 | resolved | §3.2 is the reader's five steps verbatim; re-checked each step (S₀ spacelike and acausal for a smoothed max with max ≤ F; every causal curve through {r ≥ r_♯} meets S₀; supp ω ⊂ J(K) gives τ < T_0/2 on M^♭; the cut-off product is compactly supported, P_h* = 0 on τ⁻¹([0, T_0]), zero on τ⁻¹([T_0/2, T_0]), nonzero at p). |
| n1 | resolved | header and §2–§7 rebased to 147ca162 (md5 checked). Citations: 248 = 208 + 29 + 4 + 3 + 2 + 1 + 1, recounted; every citation line of the chapter is covered by a row of §2.2 and every listed single line carries a citation (script). Line 6 is now 124 characters (nit n-b). |
| n2 | resolved | row "1980–2092, 2110". |
| n3 | resolved | T42: Λ⁻ a parametrix of Λ* (re-derived: ⟨F, Aω⟩ = ⟨B*F, ΛAω⟩ with BΛ ≈ I, so B* is a parametrix of Λ*), "(5.25)–(5.26)". |
| n4 | resolved | T41 and variant A, last sentences: supp e ⊂ {δ ≤ ρ_K < 3δ, \|ζ\| < 2𝔛⁻¹} ⊂ Ell(E); B̃_0 microsupported near supp a ⊂ Ell(B_1). |
| n5 | resolved | §8 rewritten; the fallback clause is the one P-G1's C33-11 ends with. |
| n6 | resolved | thresholds at lines 933–934, 945–946, 960–961 re-derived from (∗): γ = ½, m = 3\|α_K\| + 1, \|u\| ≥ r_♯ (added covectors of norm ≤ \|α_K\|(1 + √2) + 1); γ = 3/5, m = \|α_sf\| + 1, \|u\| ≥ 1; λ = ¾𝔛\|u\|. |
| n7 | resolved | lines 923–929 carry the reader's words; the rewrap before "near K⁺" is right: the reader's line resolves to 122 ("Definition 24.27"), the rewrapped one to 113. |
| n8 | resolved | T28 cites (H2) of sec:i-a-1-3 (P̂(0) = ρ²P^(0), P^(0) − ((ρD_ρ)² + Δ) ∈ Diff¹_b + ρDiff²_b). |
| n9 | resolved | T32 extended by chapter line 2468; χ′_(τ,1) is the cut-off whose derivative gives E_τ in prop:iv5-1-3. |
| n10 | resolved | T17. |
| n11 | resolved as worded | w is "a product of powers of boundary defining functions"; the f clash is noted. The φ_k are still "composed with a function on M^♭" while T33/T34 use the lemma on M (nit n-e). |
| n12 | resolved | blank lines before §7 and §9; "the ambiguity treated in section 4"; the T22 clause (on {t = 0}, ∂_t is transverse and 𝓛_(∂_t) − ∇_(∂_t) is of order 0, so the two data determine each other); prop:iv5-7-1 is T45. T22's rewrap leaves a short line (nit n-c). |

## T44 and T45 (first reading)

- **T44** (old text found once at 147ca162 and after P-G1). The sentence parses ("Fix δ_r > 0 so small that …, that …,
  and that 𝔛 = δ_r⁻¹ is as large as the cone-face symbols need"). Decreasing δ_r keeps (6) on 𝗌𝖿 ∩ {s ∈ [δ_r, …]}
  (prop:np-10-14 (v) holds for every δ_r, the chapter text itself says "δ_r may be shrunk") and the b_0 positivity on
  {ρ_cf ≤ 4δ_r}. True; nit n-g.
- **T45** (old text found once; it is a partial line, the merged line ends "([[sec:iv5-0]]). [[prop:iv5-1-3]] needs only").
  Re-checked what the new proof of (5.68)–(5.69) uses with ¾r_♯ for r_♯: lem:iv5-0-3 (c) (G(−r dr) = r²g⁻¹(dr, dr) ≤
  −½\|r dr\|², on [½r_♯, r̂]), lem:iv5-0-3 (a) (G(dt) ≤ −1 on {τ = 0}, second estimate of (2)), lem:iv5-0-4 (the c₁ of
  lem:iv5-6-core, through lem:iv4-1-causal (d), at every point of {r ≥ ½r_♯}), and the bounds derived under "The
  hypotheses of lem:iv5-6-core", stated there on {½r_♯ ≤ r ≤ r̂} ∩ {t ≥ 0}. Not (b). The other inputs (lem:s14-box-c
  for the Ricci-flat g^KS_b, prop:np-10-13 (ii), lem:iv5-6-transport) are identities free of the region, as in the old
  sentence's convention. True; nit n-d on "its hypothesis paragraph".

## M1 (not proved here, as instructed)

- Nothing in P-G24b states the relative-index step as proved. §1 and §2.2 class it (c) and point to §6; no placement
  text touches chapter lines 2396–2428 (the index-0 part); T23–T29 concern admissibility, the estimates and their
  uniformity, which the index-0 part does not feed; T39 only rewords thm:iv6-3-1's uniformity clause; §4.3 item 4
  checks admissibility only. The crosswalk notes claim nothing about the index.
- Every placement text is true with the step open: none asserts index 0, invertibility or a relative index formula.
- The marker (§6.1) says what is open and that proofs/P-RI.md supplies it. Two wording points (nit n-h): §6.1 asserts
  "The claim is true", which is the open step; and it scopes the gap to steps (i) and (iii), while P-RI's §1 (under
  reading now) also rewrites step (ii) (its weight β₁ is root-free for one sector only).

## New findings

### Major

None.

### minor

**r1. P-G24b.md:1370 (T35, new text), and the crosswalk note at 1643.** T35 says the forward cone estimate holds on
{ρ_cf < 4δ_r} ∩ {τ ≥ T/40}. Its commutant (T33) carries χ₁ := χ_(τ,0), which sec:iv5-1 defines as 0 for τ ≤ T/40 and 1
for τ ≥ (0.75/10)T, with no positivity in between. So b_0 = a(…)^(1/2) vanishes at τ = T/40 and possibly on
(T/40, (0.75/10)T), and the estimate controls only where χ_(τ,0) > 0; the closed set {τ ≥ T/40} is not controlled. (The
preprint's (B.39) localises the forward estimate by χ_2, not at T/40.) Nothing downstream needs more: the combination
covers τ ≤ T by eq:iv6-2-e1 and uses (a) only where τ is bounded below. Replacement for line 1370:

    (a) The forward cone estimate holds on {ρ_cf < 4δ_r} ∩ {τ ≥ (0.75/10)T} and the backward one on

and in line 1643, `on {τ ≥ T/40} and {τ ≥ (2.75/10)T}` becomes `on {τ ≥ (0.75/10)T} and {τ ≥ (2.75/10)T}`. (95
characters; checked in a scratch chapter: lint 0 hits, PAPER.md ≤ 121.)

### nit

**n-a. Lines 46–49 (§1).** After the inserted sentence on χ_sf, "Its derivative" reads as χ_sf's; line 48 is 126
characters. Replacement for lines 46–49:

      - T8 takes χ_K in prop:iv5-3-1 supported in [0, 2δ_r) and positive there (section 5, the convention of T4), rather
        than ending at (3/2)δ_r, so that b_0 is elliptic on the whole of WF′(B_0) as stated. Its derivative stays inside the
        interval where lem:iv5-0-5 (6) applies, because 2δ_r < 2/5 < v(1 − δ_sf). T8 also widens χ_sf from [0, 3/2) to
        [0, 2), and T11 inherits this.

**n-b. Lines 6 and 1622 exceed 121 characters (124, 123).** Replacement for lines 5–8:

    `chapters/33-s14-constraint-damping.md` at HEAD (the chapter last changed at the P-ADM merge, 54350a5d), md5
    147ca1624e75c280f86908a0aa499824. That file includes the F2-G24 fix round and the P-LB, P-T49 and P-ADM merges, so it
    is not the file at 003371f6. Each old text occurs exactly once, and no two old texts overlap; both facts were checked by
    a script. The line numbers given are those of that file.

Replacement for lines 1622–1623:

    - prop:iv5-7-1: "the estimates near Σ^♯ on the extended domain need lem:iv5-0-3 (a), (c), lem:iv5-0-4 and the bounds
      of the proof of prop:iv5-6-1 (T45)"

**n-c. Lines 1019–1022 (T22, new text).** The n12 insertion left a 60-character line. Replacement for the four lines
(wording unchanged):

    data extended smoothly to S with compact support (on S, (ω, r𝓛_(∂_t)ω) and (ω, ∇_nω) determine each other); by its
    support statement the solution on Ω does not depend on the extension, future causal curves from S ∩ {r < r_♯} staying
    in {r < r_♯} ([[lem:iv5-0-3]] (c)). By finite speed of propagation, ω

and the header "New (13 lines)" becomes "New (12 lines)".

**n-d. Lines 990–991 (T45, new text).** "the bounds of its hypothesis paragraph" names a paragraph by an informal
handle. Replacement for the two lines:

    bounds it derives for the hypotheses of [[lem:iv5-6-core]], which hold on {r ≥ ½r_♯}, where g is defined and c is past
    timelike ([[sec:iv5-0]]).

**n-e. Line 366 (T4).** lem:iv5-2-symbols is stated for φ_k "composed with a function on M^♭" (line 362) and proved
"for a function φ on M^♭" (line 377), but T33 and T34 apply it on M. Replacement for line 366 (two lines, ≤ 121 after
resolution):

    of [[lem:iv5-2-symbols]]. The commutants on M in [[sec:iv6-2]] have the same form, with functions on M, and
    [[lem:iv5-2-symbols]] and its proof hold for them unchanged.

**n-f. Line 1333 (T34) and line 1419 (T37).** χ̃ is introduced as "a non-decreasing cut-off in τ" and fixed as χ_(τ,2)
only in T37, after item (a) (T35) has used its value. In line 1333 replace `χ̃ a non-decreasing cut-off in τ` by
`χ̃ := χ_(τ,2)` (the line becomes 102 characters), and in line 1419 `cut-off χ̃ := χ_(τ,2) being supported` by
`cut-off χ̃ = χ_(τ,2) being supported`.

**n-g. Lines 1355–1356 (T44).** The choice is not circular only because the cone-face lower bound on 𝔛 does not grow as
δ_r decreases. Replacement for line 1356:

    symbols need, a bound that does not grow as δ_r decreases. Then:

**n-h. Lines 1484 and 1496 (§6.1, the M1 marker).** Replace `The claim is true, by the standard localisation argument,
and a proof needs about a page.` (line 1484) by `The claim is expected to follow from the standard localisation argument,
in about a page.` and, in line 1496, `(c) and left open here; the step is being proved separately (proofs/P-RI.md), and
this file keeps its marker. As the` by the two lines

    (c) and left open here, together with the rest of the index-0 part (lines 2396–2428), which proofs/P-RI.md rewrites,
    step (ii) included; this file keeps its marker. As the

(Lines 2396–2428 are the whole index-0 paragraph at 147ca162; the first line is 116 characters.)

**n-i. Line 1601 (§9, row eq:iv5-2-iter).** P-G1 is now merged (dff79ca7), so variant A is the text that enters the
chapter; its label is at line 479, not 445. Replacement row:

    eq:iv5-2-iter	paper/reader/proofs/P-G24b.md@PENDING:479	[Hin26a] (5.47)-(5.48)	the estimate before the h^(1/2) iteration; text T41, variant A (after P-G1 C33-11)

## §8 against P-G1

All checked against P-G1 at b2d824fb (C33-1 to C33-20, C95-1 to C95-3, C98-1, its crosswalk section):
- C33-11/T41: the last two lines of C33-11's new text are variant A's old text, once, and P-G1 states it keeps them.
  The fallback clause matches C33-11's last paragraph.
- C33-12/T7: either order works; the merged line is 106 characters (measured).
- C33-20/T34: C33-20's paragraph lands immediately before T34's first new line (checked in the merged chapter).
- Adjacent, not overlapping: T42/C33-9 (1465/1466), T5/C33-10 (1507/1508). By script, the only character overlaps
  between the two files' old texts at 147ca162 are T41/C33-11, T7/C33-12 and T34/C33-20 (the anchor line).
- C33-4 inserts before line 1398 (the sec:iv5-1 heading), which no T text touches. "Two lower from line 127" is right
  for P-G1's base 9571426c.
- **P-G1 has since been merged (dff79ca7; HEAD b7553023, chapter 33 md5 d2184d75289047ef76ee866214fda5d0).** My
  simulated post-P-G1 chapter is byte-identical to it. On it every old text, T41 as variant A, occurs exactly once.
  The line numbers move: T1 1273, T2 1316, T3 1374, T42 2045, T43 2051, T4 2066, T5 2088, T6 2095, T41 2137, T7 2140,
  T8 2168, T9 2176, T10 2191, T11 2214, T12 2228, T13 2253, T14 2266, T15 2327, T16 2364, T17 2455, T18 2516,
  T19 2525, T20 2549, T45 2650, T22 2736, T21 2752, T23 2937, T24 2954, T25 2960, T26 2966, T27 2981, T28 3000,
  T29 3005, T30 3080, T31 3085, T32 3088, T33 3094, T34 3114, T44 3123, T35 3125, T36 3138, T37 3147, T38 3161,
  T39 3169, T40 3280. The §2 table's counts and (a-G1) rows describe 147ca162, not the merged chapter; that is the
  stated base, and it is information for the coordinator, not a finding.

## Scratch merges

Scratch copy 1: scratchpad/reader/scratch/r2pg24b/ (reader directory from 332f13ca, chapter 33 md5 147ca162…). Applied
P-G1's chapter-33 texts C33-1 to C33-20 (C33-3 with its blank line, C33-4 lines 1–575 plus a blank line, C33-20 before
its anchor), C95-1 to C95-3 and C98-1 (C23-1, optional, not applied), its crosswalk rows; then T1–T45 with T41 as
variant A, and the 16 rows of §9 after their anchors.

| check | before | after |
|---|---|---|
| `lint.py --chapters` | 4652 labels, 0 hits | 4681 labels, 0 hits |
| `assemble.py --check` | 0 problems | 4681 labels, 0 problems |
| `assemble.py`, then `lint.py --paper` | — | PAPER.md: 0 hits |
| PAPER.md longest line (characters) | — | 121 |
| chapter 33 longest line; backslashes | — | 121; 0 |
| wrapped lines starting with "+ ", "- ", "* ", "> ", "#", "=", "\|" | — | 0 in chapter 33, 0 in its part of PAPER.md |
| crosswalk 33 | 200 rows | 229 rows for 229 labels, one per label, in chapter order |

- Each of the 45 old texts occurs exactly once at 147ca162 (T41 in its own form) and after P-G1 (T41 as variant A);
  no two P-G24b old texts overlap.
- Conservative test: the 16 new labels resolved as "Proposition 49.999" / "(49.999)", the rest to their numbers:
  chapter 33's longest line is 121.
- Chapter 33 after the merge: md5 1bad83dc06e13f279a2190e2efe232ef.

Scratch copy 2: scratchpad/reader/scratch/r2pg24b-head/ (HEAD b7553023, P-G1 already merged). Applying only T1–T45
(variant A) and the 16 rows gives the same chapter 33 (md5 1bad83dc…), lint 0 hits, 4681 labels, 0 problems, PAPER.md
0 hits, longest line 121, crosswalk 229 rows in chapter order.

Scratch copy 3 (scratchpad/reader/scratch/r2pg24b-nits/): copy 2 with the chapter-text replacements of r1, n-c, n-d,
n-e, n-f and n-g applied: lint 0 hits, 0 problems, PAPER.md 0 hits, longest line 121.

## Quotations of the preprint (alphaXiv full text of arXiv:2606.27658v2)

- (5.20), the cut-offs χ_(τ,j), χ_(r,j): 0 below ((j + ¼)/10)T, 1 above ((j + ¾)/10)T, as sec:iv5-1 states.
- (5.35)–(5.36), quoted by T5: χ_K ∈ C_c^∞([0, 3)) equal to 1 near [0, 1]; ψ = 1 for \|r − r_0\| ≤ (55/50)r_0√e/v,
  supported in \|r − r_0\| < (60/50)r_0√e/v. T5 agrees (r_c for r_0, ε_c = r_c e^(1/2)/v).
- (5.53), T8: χ_sf ∈ C_c^∞([0, 3/2)) equal to 1 on [0, 5/4], χ_K ∈ C_c^∞([0, (3/2)δ_r)) equal to 1 on [0, (5/4)δ_r]. T8
  widens both supports; §1 says so for both.
- (5.60), T13: χ₂ = 1 near (−∞, r_3], 0 near [r_4, ∞); χ_K = 1 near [0, t_2⁻¹], 0 near [t_1⁻¹, ∞). T13's χ_K (1 on
  [0, t_3⁻¹], positive on [0, t_1⁻¹)) differs, and with the positivity of T4 it serves; T13 cites (5.60) only for the
  identity.
- (B.36)–(B.40), T32–T35: χ_cf ∈ C_c^∞([0, 3)) equal to 1 near [0, 1] and the commutant's χ_1 of (B.36) (j = 1); (B.39)
  bounds ‖B_0χ_2ω‖ with a priori ‖Eχ_0(1 − χ_2)ω‖; (B.40) bounds ‖B_0χ_4(τ)χ_cf,2ω‖ with a priori term carrying χ_2(τ).
  The paper's T33 choices (𝔛 = δ_r⁻¹, [0, 5/2] and [0, 4), χ_(τ,0)) are its own, are flagged in §1/m3, and are
  consistent except for the forward range (r1). The backward range (2.75/10)T matches the preprint's use of χ_2.
- (5.67): the preprint states it "For ω ∈ ρ_sf^(−α_sf−2)H²_(3b,h)(M) without support restrictions", as §3.3 says
  ("the same gap").
