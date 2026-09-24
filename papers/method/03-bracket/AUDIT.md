# AUDIT — paper 03, "The Bracket: a Guarantee on Rydberg Levels, and What It Costs"

Audit of the draft dated 21 September 2026 (`PAPER.md`, 452 lines; `check.py`, 837 lines; `SOURCES.md`;
`FIGURES.tsv`; five plates; `out/03-bracket.pdf`, 18 pages). Written 24 September 2026 to the brief in
`papers/method/BRIEF-AUDIT.md`. Not published. Nothing in `PAPER.md` or `check.py` was edited; a finding is
recorded here and repaired by the drafter.

Line numbers are lines of `PAPER.md`. Obligation tags (I1…I38, M1…M4, G1–G2, E1…E11, N1–N5) are the check's.

**Runs.** `python3 check.py`: 56 obligations, 0 failed, exit 0 (EXHAUSTIVE 9, GUARD 3, MACHINE-CHECKED 4,
MEASURED 10, PROVED 30). `python3 check.py --selftest`: 61 obligations, the five negative controls N1–N5 each
reported as refuted, exit 0. `lint.py`: 0 hits. `render.py`: 18 pages. Every number the paper prints was matched
to a line of the check's output or to `results.json` (see A.3); the ones with no printed line are A-16.

**Counts.** 37 distinct findings: 2 BLOCKING · 15 MAJOR · 20 MINOR (Part A: A-1…A-26; Part B: R-1…R-24; a
reader's finding that restates an A-finding says so and is not counted twice — see Part C).

---

## Part A — content audit

### A.1 Definitions against the source

| paper | source | relation | note |
|---|---|---|---|
| R = 109,737.31568 (42) | MV §22.1.1.1 | same, CITED to CODATA 2018 | correct value of R∞ |
| D1 level/threshold/term (44) | MV §22.1 | same | "in cm⁻¹" added, fine |
| D2 ν, δ (46–50) | MV §22.2 Rule 2, §23.4 | same | |
| D3 series/cell/interior (52) | SC channel-table header; RB `run_series` | paper's own, matches RB's "true neighbours" rule | D3 defines interior for unit step only, yet Theorem 5 (153) and §7 (302) use cells at step h = 2 — A-21 |
| D4 the bracket (54–58) | MV §22.1, A.12 | same | |
| D5 the defect bracket (60–62) | MV §25.6.1 | **inverted labels** | with δ_lo ≤ δ_hi the definitions give E_lo ≥ E_hi, so "E_lo ≤ E(n) ≤ E_hi" is the reversed interval; Lemma 2 (94) states it the right way round — A-2 |
| D6 width/error/price (64) | MV §23.1 | same | |
| D7 quotation floor, r_adm ≥ 5 (66–70) | MV §22.5 verbatim; RB lines 2–6, 30–31 | same | |
| D8 the strict test (72) | RB lines 21–36; SC count paragraph | same, clause for clause | inherits D5's inverted labels; the code sorts (lo, hi) so the implementation is right and the text is wrong |
| D9 power-law observable (74) | MV §23.1 | same | |
| D10 decrement, self-concordance (76) | MV §23.8.1–2; MC | same | the inequality is not scale-invariant — A-4 |
| D11 critical depth (124) | MV §25.3, A.13 | same formula, now an *estimate* between two exact thresholds | correct re-reading |
| D12 resolution at order k (280) | MV §23.10.4 | same rule | the ν_V sentence after it does not follow from it — A-6 |

### A.2 Results and proofs

| result | source | paper vs source | proof complete? | check |
|---|---|---|---|---|
| Th. 1 (82–84) | MV §22.1 (asserted) | stronger: stated as an iff, proved | yes | M4 |
| Cor. 1 (86) | MV §24, PC | same | yes (trivial) | — |
| Th. 2 (88–90) | A.12 | same; A.12's proof written out | yes; the chain at 90 writes one step with the inequalities reversed in order ("max(−a,−b) ≥ −c ≥ min(−a,−b)"), equivalent but untidy | M1 |
| Lemma 2 (94–96) | MV §25.6.1 ("E being decreasing in δ") | same, now a lemma | yes | — |
| Th. 3 (104–108) | A.13 | **replaces** the source's leading-order "⟺ ΔT > 2Z²R/ν³" with the exact two-sided condition | yes | M3 |
| Lemma 3 (112–120) | A.13's "half-spacing … to leading order" | new: exact gaps and the sandwich g₊ < 2A/ν³ < g₋ | yes (the second inequality needs 3ν > 2; stated for ν > 1) | I21, I22 |
| Cor. 2 (122) | MV §25.5, A.13 inversion | replaces "held ⟹ ΔT < 2Z²R/ν³" with a bound of w/2 | **no — the last sentence does not follow from the first** (A-1) | I23, I24; E7 measures w/2 |
| Th. 4 (141–149) | MV §23.4 | same | yes, every step checked by hand | I1–I3 |
| Cor. 3 (151) | MV §23.4.1, §22.4 | same | yes | I4, I13 |
| Th. 5 (153–159) | MV §23.2–23.3 | source *asserts* the floor; paper proves monotonicity via the difference identity | yes; the factorisation and the positivity argument verified by hand | I6, I9, I10 |
| Cor. 4 (163) | MV §23.3 | corrects "exact to four decimals" to three | yes | I5, I11, I12 |
| Th. 6 (169–171) | MV §23.2 Prop. 23.1 | same, plus V = 2(1+t)/(1−t) | yes | M2, I31 |
| Th. 7 (175–186) | MV §23.5.2 (asserted, "verified over 172 steps") | source asserts; paper proves | the main argument is complete and correct (the cancelling terms at 184 are A(h)A(t) and B(h)B(t), not "squares"); **the extension to y′ < 0 by "apply the result to −y" is wrong**: −y is concave, and the Rydberg term is the y′ < 0 case — A-3 | — |
| Th. 8 (190–198) | MV §23.1, §23.9.1–2 | source's "4x/(h|p−1|), under 1 %" corrected; second-order coefficient (p−2)(p+1)/12 is new | yes (binomial expansion verified; p = −2 gives 1/3 = Cor. 4) | I29, I30, I32 |
| Th. 9 (219–223) | MV §23.6 | source prints w/T = 4s + 8s³ (two terms); paper gives the closed forms | yes | I7, I8, I14 |
| Prop. 1 (225) | MV §23.5.3 (marked NOT CHECKABLE in MC) | paper states the objective and proves the stationary point at leading order | yes, as bounded | — |
| Th. 10 (233–235) | MV §23.8.1, D.4.1 | same | yes | I16–I18 |
| Th. 11 (239–241) | MV §23.8.2 | same statement; source's "deepest channel ν = 55 / sevenfold" replaced by 66.99 / 6.06 | the algebra is right; the *interpretation* is unit-dependent — A-4 | I19, I20, E11 |
| Th. 12 (243–253) | MV §26.6 | source asserts "→ T/3"; paper gives the exact rational form | yes, every line of the algebra verified by hand | I27, I28 |
| Lemma 4 (270–272) | MV §23.10.1 | same | yes (finite-difference mean-value theorem CITED) | I33 |
| Th. 13 (274–276) | MV §23.10.1 | same | yes (remainder CITED) | I34 |
| Lemma 5 (278) | MV §23.10.4, §23.12 | same | yes | I35 |
| D12 → ν_V (280) | MV §23.10.4, §23.15 | the two source thresholds are presented as one rule | **not consistent**: 3A/ν⁴ is e, not the second difference (Δ²T = 2e ≈ 6A/ν⁴), and D12 at k = 1 is |Δ²T| > 20q ⟺ e > 10q, whereas ν_V is solved from e > 5q — A-6 | I26 |
| Lemma 6 (359) | MV §26.1 | same | trivial, fine | — |
| Lemma 7 (361) | MV §26.2 | same | yes | E10 (float SVD) |

### A.3 Numbers against the check

Every number in the paper was located. Those with a printed obligation line: I1–I38, M1–M4, G1–G2, E1–E11 as
tagged in the text; the tags in the paper are correct throughout (the tag → number correspondence was checked
line by line, including Tables 1–6, both figure captions with numbers, and the §10 table). Numbers that are
computed by `check.py` but *not printed* in any obligation line (they sit in `results.json` under `numbers`)
are listed in A-16; one number, the "−0.005 growing as n³" of line 353, is computed nowhere.

Two arithmetic identities of printed values were re-derived: 738,547 − 735,860 = 2,687 and 737,380 − 735,860
= 1,520 (335) ✓; 2·0.9812 − 1.0057 = 0.9567 ✓. Table 5's row totals (1,551; 1,148; 850; 649; 495; 391) are the
sums of E8's triples ✓. Table 4's percentages 733/894 = 82.0 %, 1,145/1,551 = 73.8 % ✓.

### A.4 The central correction, examined

The source (MV §25.3, A.13, MC "when the bracket fails" / "what silence implies") states *fails ⟺ |ΔT| >
2Z²R/ν³* and inverts it to *held ⟹ |ΔT| < 2Z²R/ν³*. The paper's diagnosis is right on both counts and is
proved: Theorem 3 (M3) gives the exact condition −(c − b) ≤ Δ ≤ a − c, and Lemma 3 (I21–I22) shows the two
gaps straddle the derivative, g₊ < 2A/ν³ < g₋, so the source's biconditional is false in both directions and
its inversion claims a bound tighter than containment gives (a displacement Δ with 2A/ν³ < Δ ≤ g₋ is held,
against the source). On the data E6 confirms the straddle (medians 1.264 and 0.818).

**But the paper's replacement bound is wrong by the same mechanism.** Corollary 2 (122) proves |Δ| ≤ max(g₋,
g₊) = g₋ and then concludes "So each held cell bounds its own local perturbation by half the width of its
bracket". With w = g₋ + g₊ and g₊ < g₋, w/2 < g₋: the half-width is *smaller* than the bound containment
supplies. Exactly: g₋ = w/2 + e (the level lies e below the chord, Theorem 4), so the claimed bound w/2 is
too tight by e, that is by the fraction 1/V ≈ 3h/(4ν) — 34 % at ν = 2, 1.2 % at ν = 64. Read from the data, the
deductive bound at a held cell (unperturbed neighbours, unperturbed level somewhere in the interval) is the
*larger observed gap*, max(E − E₋, E₊ − E), not (E₊ − E₋)/2; E7, Figure 4, the abstract (11), §0 (19) and §7
(310) all carry w/2. Re-measured from `results.json` (`cells`, verdict = pass): 1,135 of the 1,145 held cells
have the larger gap on the same side as Lemma 3 predicts; the tightest bound by the larger gap is **0.970
cm⁻¹** (Ga I 4s²np, n = 66, ν = 63.8), not 0.925; the median is **5,389 cm⁻¹**, not 4,308. The paper thus
corrects the source's *leading-order* overreach (2A/ν³ < w/2 by the factor (1 − h²/ν²)²) and commits an
*exact* one of the same sign (w/2 < g₋ by e). See A-1.

Two further limits of the replacement are hedged in Corollary 2 and dropped in §7: the hypothesis "whose
neighbours are unperturbed", and the fact that Δ is a displacement of the *middle level relative to its two
neighbours*, not a perturbation of the series (R-11).

### A.5 The strict-membership rule, the floor and REFUSED

D7–D8 reproduce `ruled_bracket.py` clause for clause (strict membership; q = ½·10⁻ᵏ from the printed string;
floor applied at both edges; r_adm = 2Z²R/(ν³q) ≥ 5 at the cell's own ν; REFUSED counted apart). N5 shows the
refusal path fires. Two things the paper does not say, measured from `results.json`: 39 of the 1,145 passes
pass *only* because of the floor (E outside [E_lo, E_hi] but inside [E_lo − q, E_hi + q]); 25 of the 406 fails
lie within 2q of an edge and 84 within 5q; and at 64 cells (32 of them held) the defect interval E_hi − E_lo is
itself narrower than 2q, so the verdict there is the floor's and not the data's — D7 tests whether *levels* are
separated against q, not whether the *interval* is resolvable against q. Recorded as R-14.

### A.6 The ten source claims SOURCES.md says do not reproduce

| § | source figure (as SOURCES states it) | source checked | paper figure | check line | fairly represented? |
|---|---|---|---|---|---|
| 3.1 | asymptote "exact to four decimals by ν = 10" | MV §23.3 ✓ | 4/26,910 = 1.49 × 10⁻⁴, three decimals | I12 ✓ | yes |
| 3.2 | "p = −3 to +11, agreement under 1 %" | MV §23.1 ✓ | 2.24 % at p = 11 | I29 ✓ | yes |
| 3.3 | fails ⟺ ΔT > 2Z²R/ν³; held ⟹ ΔT < 2Z²R/ν³ | A.13, MC ✓ | exact condition; bound w/2 | M3, I21–I24, E6, E7 | the diagnosis yes; the disposition ("w/2 from the two measured neighbours") is A-1 and SOURCES §3.3 must be rewritten with it |
| 3.4 | 1,033 pairs, 0.49 / 1.15 / 0.69 % against 4r/3 | MV §23.4.2 ✓ | 1,490 / 842 / 2,332; 0.84 / 0.51 / 0.71 % against the exact law | E5 ✓ | yes; comparand difference stated |
| 3.5 | deepest ν = 55, ratio 0.1356, sevenfold | MV §23.8.2 ✓ | 66.99, 0.1651, 6.06 | I20, E11 ✓ | yes |
| 3.6 | 103.94 / 0.878, 329.80 / 0.882, 816.68 / 0.894 | PC ✓ | 103.68 / 0.876, 328.66 / 0.879, 815.22 / 0.893 | E9 prints the ratios; deficits in `results.json` | yes; provenance of the thresholds is R-13 |
| 3.7 | tightest 1.398 (Al I 3s²nf n = 54) | MV §25.5 ✓ | 0.925 (Ga I n = 66) | E7 | yes as to coverage; the quantity itself changes under A-1 (0.970) |
| 3.8 | 546 of 789 | MV §24 ✓ | 1,145 of 1,551 | E2, E3 ✓ | yes |
| 3.9 | 499/187/34 admitted, 19/101/145 refused | MV §23.10.4 ✓ | Table 5 | E8 ✓ | yes; the partition difference is stated |
| 3.10 | σ₁ = 9.49 × 10¹ | MV §26.2 ✓ | 83.69 | E10 ✓ | yes |

The three corrections SOURCES §2 says the paper carries (the withdrawn w·V "conservation law", MV §23.5.1;
the retracted "holds in every one", MV §24; the retracted 35.3 %, MV §25.2(ii)) were read at source and are
carried as stated. Run A's 658/813 on 250 and 75/81 on 35 were found verbatim in SC's count paragraph (line
994) and are asserted, not merely reported, by E4.

### A.7 The Z3 obligations and the guards

| tag | encoding | is it the operator the paper defines? | guards before it | box |
|---|---|---|---|---|
| M1 | `contained(c,a,b) == contained(I−c, I−a, I−b)`, hyp True | yes (Th. 2) | G1, G2 | all real (I, a, b, c); named at 374 |
| M2 | d₀,d₁ > 0, d₀ ≠ d₁ ⟹ 2(d₀+d₁) > 2|d₀−d₁| | yes (Th. 6; the factor 2 on both sides is redundant but harmless) | G1, G2 | all positive reals d₀ ≠ d₁; named at 380 |
| M3 | a > c > b ⟹ contained(c+d, a, b) == (−(c−b) ≤ d ≤ a−c) | yes (Th. 3) | G1, G2 | all real (a, b, c, Δ); named at 376 |
| M4 | contained(c,a,b) == (a ≥ c ≥ b ∨ a ≤ c ≤ b) | yes (Th. 1) | G1, G2 | all real triples; named at 373 |

`contained` is `min ≤ c ≤ max` with min/max as `If`; this is QF_LRA with ite, for which Z3 is complete, so the
paper's "proof over every real assignment" (32, 400) is justified. G1 evaluates the z3 predicate on 400
seeded random rationals (seed 3, 20 % with c = a) against a sort-and-compare reference; N1 shows a strict
reference produces 84 disagreements. G2 asks each hypothesis for a model with all variables distinct. Both
print before M1–M4. Two defects: the guards do not *gate* — a failing G1 or G2 would print `XX` and M1–M4
would still print `[ok]` (spec §6 "refuses to report") — A-18; and the paper does not name G1's seed — A-17.
No claim is marked MACHINE-CHECKED for a box the check does not cover.

### A.8 Figures against captions

| figure | file | md5 verified | caption vs image |
|---|---|---|---|
| 1 | fig1-cost-exact.png (plate figure-23.1, build8) | source md5 c2079bfd… ✓ matches FIGURES.tsv and the tree; PROOF-FIGURES.tsv row 52 | legend reads "asymptote 4ν/3"; the caption says the asymptote "reads 26/9" at ν = 2 and the inset shows the dashed curve coincident with the exact at ν = 2 (≈ 2.9). 4ν/3 is 8/3 = 2.667 there, visibly below; the plotted curve is the two-term form 4ν/3 + 4/(9ν) and the legend is wrong. Caption and plate disagree — A-11 |
| 2 | fig2-cost-surface.png (plate figure-23.2) | ad04ecb1… ✓; PROOF-FIGURES row 53 | five marked points, pole, C₆ off-panel: all as captioned; the annotation at the pole is overprinted by two curves — A-15 |
| 3 (fig4-v-measured.png) | computed | d7f3359c… ✓ | 1,490 / 842 in legend, exact curve and floor drawn; a few h = 2 points at r < 2 sit under the floor, consistent with Theorem 5's hypothesis ν ≥ 2h; caption correct |
| 4 (fig3-bounds.png) | computed | 3afa4a9c… ✓ | legend counts 425 / 285 / 435 match `results.json`; "tightest 0.93 at ν = 63.8" as captioned; y-axis "w/2" — the quantity changes under A-1 |
| 5 | fig5-order-census.png | 90e1e48c… ✓ | bar totals 1,551 … 391 match Table 5 |

The file names fig3/fig4 are swapped relative to the figure numbers (A-24). All five appear in the PDF with
their captions, legible at print size; each carries a stray "Figure N" line above the caption (A-14).

### A.9 Lint

0 hits. But lint's pattern list does not contain the spec's own prohibition of "MEASURED-as-a-label", and the
paper uses MEASURED as a status label in seven places (A-9).

### A.10 Typography on the rendered page (PDF, 18 pages, all read)

- **Table 1 (p. 5) and Table 2 (p. 8) headers are destroyed.** `|Δ| (cm⁻¹)` and `4ν/(h·|p − 1|)` contain
  pipe characters, which pandoc reads as column separators: Table 1's header renders as ‹blank› | Δ | (cm⁻¹)
  and the two ν_fail headers are lost; Table 2's last header renders as "4ν/(h·". A-12.
- Literal carets, underscores and braces in prose and displayed blocks on pp. 1, 3, 5, 8, 9, 10, 11, 13, 14,
  15, 16: `^{1/3}`, `x^p`, `(f″)^{3/2}`, `T^{(j)}`, `(−1)^j`, `ν^{j+2}`, `Δ^j`, `(−1)^{k+1+m}`, `2^{k+1}`,
  `Δ^{k+1}`, `(3Z²R/(5q))^{1/4}`, `s^{2k}`, `ν^{2a+3b}`, `ν^{pᵢ}`, `ν_fail`, `ν_V`, `r_adm`, `x_n`, `δ_∞`,
  `R_M`, `m_e`, `E_lo`, `E_hi`, `δ_lo`, `δ_hi`, `Σ_{k odd}`, `x^{p−k} h^k`. A-13.
- Every figure prints "Figure N" as a bare line between image and caption (pandoc `implicit_figures` uses
  the alt text). A-14.
- Displayed blocks wrap mid-formula at the column width on p. 4 (Lemma 3's g₊), p. 5 (Theorem 4's V), p. 8
  (Theorem 8's sums), p. 9 (Theorem 9's e/T "+ …,"), p. 10 (Theorem 12's Â). Legible; untidy. Folded into A-13.
- No heading orphaned at a page foot (§10 sits at the foot of p. 15 with a paragraph under it). Every table
  fits its column; no cell clipped. Figures sit with their captions. Fonts and Unicode otherwise clean.

### Findings, Part A

**A-1 · BLOCKING · lines 122, 11, 19, 310, 314; E7; Figure 4; SOURCES §3.3, §3.7.** Corollary 2's last
sentence does not follow from its first: |Δ| ≤ g₋ = w/2 + e does not give |Δ| ≤ w/2. The bound each held
cell supplies is the larger observed gap max(E − E₋, E₊ − E) (or the signed pair −(E − E₋) ≤ Δ_E ≤ E₊ − E), not
the half-width. *Resolve:* restate Corollary 2 with the two-sided bound in terms of the observed gaps; change
E7 to compute the larger gap (tightest 0.970 cm⁻¹, median 5,389 cm⁻¹ on the present data); regenerate Figure 4
with the new y-quantity; rewrite the abstract's "each held cell bounds its own local perturbation, the
tightest to 0.93 cm⁻¹", §0's "by half the bracket's width", §7's paragraph, and SOURCES §3.3/§3.7. Keep the
hypothesis "neighbours unperturbed" in every statement of the bound (R-11).

**A-2 · MAJOR · lines 60–62, 72 (D5, D8) against 94 (Lemma 2).** With δ_lo ≤ δ_hi the definitions give
E_lo ≥ E_hi, so D5's "E_lo ≤ E(n) ≤ E_hi" and D8's "E_lo − q ≤ E(n) ≤ E_hi + q" name the reversed interval;
Lemma 2 correctly concludes E_hi ≤ E(n) ≤ E_lo. The code sorts and is right. *Resolve:* define E_lo := I −
Z²R/(n − δ_hi)² and E_hi := I − Z²R/(n − δ_lo)² (or define the two as the ordered pair of the two images) and
make Lemma 2's conclusion read E_lo ≤ E(n) ≤ E_hi.

**A-3 · MAJOR · line 175 (Theorem 7), 186.** "The same holds with y′ < 0 (apply the result to −y)" is false:
−y is strictly concave, outside the theorem's hypothesis; the Rydberg term is the y′ < 0 case, so the
theorem as stated does not cover its own application. *Resolve:* reduce by reflection, z(u) := y(2x − u),
which is strictly convex with z′ > 0 and has the same w, e, V; or prove the y′ < 0 case with the signs carried.
At 184–186 replace "the four squares cancel" by "the terms A(h)A(t) and B(h)B(t) cancel".

**A-4 · BLOCKING · lines 11 (abstract), 76 (D10), 239–241 (Theorem 11), 237.** The self-concordance
inequality |f‴| ≤ 2(f″)^{3/2} is not invariant under f ↦ cf, so the bound ν ≤ (√6/2)·Z√R is a statement about
the unit R is written in: 405.7 with R in cm⁻¹, 4.5 with R in eV, 0.87 in hartree, where no Rydberg state
qualifies. Theorem 11 is correct arithmetic and physically meaningless; "the term function is self-concordant
across the whole measured range with a margin of 6.06, so the decrement carries its meaning there" (241) and
the abstract's clause are artefacts of cm⁻¹. *Resolve:* either drop Theorem 11, I19–I20, the E11 ratio and the
abstract clause; or restate with Nesterov's self-concordance parameter M (|f‴| ≤ M(f″)^{3/2}), show M scales
as A^{−1/2} and therefore with the unit, and delete every sentence that reads self-concordance as a property
of the atom. SOURCES §3.5 then becomes moot.

**A-5 · MAJOR · line 237.** "The decrement is affinely invariant, which is why Z²R cancelled from V in
Theorem 4: a multiplicative constant is an affine map." The Newton decrement's affine invariance is under
affine changes of the *variable*; under T ↦ cT the decrement scales as c, which Theorem 10's own λ² = (2/3)T
shows. Z²R cancels from V because V is a ratio of two quantities each linear in T. *Resolve:* delete the
sentence, or replace it with the correct reason and, if wanted, note that V's dependence on ν/h alone (Cor. 3)
is the domain-side invariance.

**A-6 · MAJOR · line 280 (D12 and ν_V), with 302, 316.** "The leading-order second difference 3A/ν⁴
(Theorem 9 with h = 1)" — 3A/ν⁴ is e, half the second difference (Δ²T = 2e ≈ 6A/ν⁴). And D12 at k = 1 reads
|Δ²T| > 5·2²q ⟺ e > 10q, which is the filter §7 uses (302) and E8 applies (316), whereas ν_V is solved from
e > 5q; under D12 the ceilings are 2^{−1/4} times smaller (134.7, 75.7, 42.6). So ν_V does not "follow from"
D12 and the section states two thresholds as one. *Resolve:* say which threshold defines ν_V, derive it from
that threshold with the second difference named correctly, and reconcile with §7's e ≥ 10q; I26 then prints the
matching numbers.

**A-7 · MAJOR · lines 290, 400–402; check.py 554–575 (E1).** The "independent implementation" `ref_series` is
a transcription of `ruled_bracket.run_series` — same `qfloor`, same formulae, same control flow, same
sort-then-compare — so E1 cannot catch a misreading of D8 shared by both. *Resolve:* write the reference from
D8's text in a different shape (e.g. test the bracket on δ directly and map by Lemma 2; derive q from the
decimal string by a different route; iterate over n rather than over list positions), and say in §10 what
differs.

**A-8 · MAJOR · line 398; check.py labels.** "30 PROVED (every identity among them exact on a rational grid
above its degree, Fraction arithmetic, no floating point)": fourteen of the thirty are floating-point
evaluations of proved formulae (I11, I12, I13, I14, I15, I18, I20, I25, I26, I28, I32, I37, I38) and one is a
numpy SVD (E10). Spec §5: statuses are never merged. *Resolve:* give the arithmetic evaluations their own
label in `check.py` (the paper's own table already writes "arithmetic (I25)") and restate the count; label
E10 as the numerical corroboration it is; make I23's label match §10's row (A-25).

**A-9 · MAJOR · lines 34, 298, 306, 314, 327, 351, §10.** MEASURED as a status label is on the spec's §8
forbidden list ("MEASURED-as-a-label"); the paper also drops the spec's SAMPLED. `lint.py` has no pattern for
it. *Resolve:* every measurement here is a decision procedure over a stated finite family (every interior cell
of the 86 tables), so report the data runs as EXHAUSTIVE with the family named, or obtain an amendment to
the spec's vocabulary; and add the pattern to `lint.py`.

**A-10 · MAJOR · lines 288, 290.** "held as 86 tables, one per spectrum" and "395 series across 74 spectra":
the 74 table labels that contribute cells cover 58 distinct spectra (Si I has eight tables, Ne II four, Ne I
three, Ba III three, Ar II two, Ca II two), and one of the "nine further tables" without a threshold is a
cross-check file (QD-CHECK), not a level table. No cell is counted from two tables of one spectrum (checked
on `results.json` by (n, E)). *Resolve:* "86 tables covering N spectra … 395 series across 58 spectra", and
"eight further tables".

**A-11 · MAJOR · lines 165–167 (Figure 1).** The plate's legend labels the dashed curve "asymptote 4ν/3";
the caption's 26/9 and 0.69 % belong to 4ν/3 + 4/(9ν), and the inset shows that two-term curve. A caption
must state what the plate shows. *Resolve:* regenerate Figure 1 with `figures.py` from I5/I9–I12 with the
legend "4ν/3 + 4/(9ν)" (and update FIGURES.tsv), or, if the plate is kept, change the caption to what its
legend says and drop 26/9 from it.

**A-12 · MAJOR · lines 126, 200 (rendered Tables 1 and 2).** The `|Δ|` and `|p − 1|` bars in the header
cells are parsed as column separators; both headers are wrong on the page. *Resolve:* escape as `\|`, or write
the headers without bars ("displacement Δ (cm⁻¹)", "4ν/(h·(p − 1)) for p > 1").

**A-13 · MINOR · pages 1, 3, 5, 8–11, 13–16.** Literal `^{…}`, `_…` and `Σ_{…}` in prose and in displayed
blocks (list in A.10). *Resolve:* Unicode superscripts/subscripts, or backticks for the inline symbols the spec
allows; rewrite the displayed sums of Theorem 8 with Unicode.

**A-14 · MINOR · all five figures.** A bare "Figure N" line between image and caption. *Resolve:* empty alt
text (`![](figures/…)`) so the italic caption paragraph is the only caption.

**A-15 · MINOR · Figure 2.** The three-line annotation at the pole is overprinted by the ν = 20 and ν = 40
curves. *Resolve:* regenerate with the label moved, or accept as the plate.

**A-16 · MINOR · lines 288, 290, 310, 333, 335, 347–349, 353.** Numbers with no printed check line: 86 tables,
nine/57 without threshold, 74 spectra (288, 290); 0.844 cm⁻¹ (310); 851.8 … 60,212.5, the seven widths and
six ratios (333); the deficits and Dirac terms of Table 6 (only the ratios print in E9); and "−0.005 growing as
n³" (353), which no obligation computes (≈ 1.34 × 10⁻⁵·n³ = 0.0046 at n = 7). *Resolve:* print them in the
obligation lines (they are in `results.json` already) and add an arithmetic line for the δ error.

**A-17 · MINOR · line 400.** G1's 400 triples are seeded (seed 3) but the paper does not say so. *Resolve:*
"400 seeded random rational triples (seed 3)".

**A-18 · MINOR · check.py 442–494.** A failing guard does not stop M1–M4 from reporting `[ok]`. *Resolve:*
skip or mark the M rows when G1 or G2 fails.

**A-19 · MINOR · line 276.** "560 two-sided brackets" is 112 × 5 by construction (every (ν, k) has m = 0 and
m = 1 of opposite parity); it adds nothing to the 2,800 sign checks. *Resolve:* drop it or say it is
automatic.

**A-20 · MINOR · line 3.** "never below 32/11" is contradicted by the paper's own Li III n = 2 cell (161,
E11); the floor holds for ν ≥ 2h. *Resolve:* "never below 32/11 once ν ≥ 2h".

**A-21 · MINOR · lines 52, 153, 302.** "Interior cell" is defined at unit step; Theorem 5 and §7 use cells at
step h. *Resolve:* define interior at step h in D3.

**A-22 · MINOR · line 32.** MACHINE-CHECKED is redefined from the spec's finite box to all of linear real
arithmetic. Stronger and justified at 400; recorded so the deviation from spec §5 is on the record.

**A-23 · MINOR · lines 288, 290.** "re-retrieved" and "the sealed implementation" are process words (spec §8).
*Resolve:* "retrieved in August 2026"; "the implementation of D8".

**A-24 · MINOR · FIGURES.tsv, lines 304, 312.** fig3-bounds.png is Figure 4 and fig4-v-measured.png is Figure 3.
Cosmetic; rename or leave with FIGURES.tsv as the map.

**A-25 · MINOR · line 377; check.py I23.** I23 is PROVED in the check (796 cases) and EXHAUSTIVE in §10's table;
the statement for every ν > 1 follows from I24 in one line, (1 − h²/ν²)² < 1. *Resolve:* make the label match
and cite I24 for the proof.

**A-26 · MINOR · lines 110–114.** "Gap above / gap below" means the T-order at 110 and the n-order at 112
(g₋ is "the gap below the cell" in n and the gap *above* c in T). *Resolve:* name the gaps by neighbour,
"toward n − 1" and "toward n + 1".

---

## Part B — reader audits

### B.1 A mathematician (order, combinatorics; has never seen the material)

I read the paper as a sequence of elementary but exact statements about three numbers and a rational
function, and most of it is what it says it is. Theorems 1–3 and 6 are one-line facts about real triples,
proved and machine-checked, and the paper is honest that they are trivial. Theorem 4, Corollary 4, Theorem 5's
difference identity, Theorem 8's second-order coefficient and Theorem 12's exact Aitken form are correct — I
re-derived each by hand and they hold, and the grid checks are proofs of the identities. Theorem 7 is the one
argument with content, and its main body is a clean integral-kernel proof. What a referee for *Order* would
send back is not the mathematics but three places where a sentence claims more than the line before it proved.

**R-1 · BLOCKING · line 122.** Corollary 2 proves |Δ| ≤ g₋ and then asserts |Δ| ≤ (g₋ + g₊)/2, which is
smaller. This is a non sequitur, and it is the paper's headline consequence. (Same as A-1; the resolving change
is A-1's.)

**R-2 · MAJOR · lines 60–62, 94.** D5 and Lemma 2 assert opposite orderings of E_lo and E_hi under the same
definitions; one of them is empty. (A-2.)

**R-3 · MAJOR · line 175.** "Apply the result to −y" applies a convexity theorem to a concave function. The
theorem is true for y′ < 0, but not by that sentence; reflect the variable instead. (A-3.)

**R-4 · MAJOR · lines 76, 239–241.** Self-concordance is a property of a function together with a scale; the
paper computes it for A/ν² with A a dimensionful number and then interprets the threshold. As mathematics
Theorem 11 is fine; as a claim about "the term function" it depends on the unit of A, which no theorem should.
Either state it with the parameter M and its scaling, or omit it. (A-4.)

**R-5 · MAJOR · line 237.** Affine invariance of the Newton decrement is invariance under x ↦ Mx + b, not
under f ↦ cf; the sentence explaining the cancellation of Z²R by it is false, and the paper's own λ² = (2/3)T
disproves it. (A-5.)

**R-6 · MINOR · line 225.** Proposition 1's objective αw + βV adds an energy to a pure number; α and β
carry units and the paper should say so, or non-dimensionalise w by T. Not wrong, but a referee will ask.

**R-7 · MINOR · lines 361–363.** Lemma 7 (a centred log-matrix of monomials has rank one) is a triviality
dressed as a lemma, and the SVD numbers beside it prove nothing the lemma does not already say. The remark on
"three names for one quantity" (363) speaks of "an ambient over an actual" with neither term defined anywhere
in the paper; unmotivated for a reader who has not seen the books. *Resolve:* fold Lemma 7 into Lemma 6 as a
sentence, and either define the ambient/actual vocabulary or drop the remark.

**R-8 · MAJOR · line 280.** The sentence deriving ν_V says "second difference" of a quantity that is half the
second difference, and applies a threshold that is not D12's. (A-6.)

**R-9 · MINOR · line 276.** "560 two-sided brackets" is not a count of anything found; it is 112 × 5. (A-19.)

I found the proofs otherwise complete: every symbol is defined before use except the ambient/actual pair of
R-7; every ∎ closes an argument; no "clearly". The status vocabulary is used consistently in the text; the
mismatch is between the text and `check.py`'s labels (A-8, A-25).

### B.2 An atomic physicist who works with NIST spectra

I work with Rydberg series the way the field does: with Lu–Fano plots, extended Ritz fits and MQDT. Read
against that practice, the paper's guarantee — a level lies between its neighbours — is, as it says itself,
the statement that the series is ordered, and no spectroscopist has ever needed it. The "defect bracket" test
is a monotonicity check on δ(n) between adjacent members, and its 406 failures are the local non-monotonicity a
Lu–Fano plot displays as a resonance profile; that is not new information, and the paper does not claim it
is. What could be a contribution is the *bound* — a statement about a cell that uses no fit — and that is
where I have my one serious objection, and one hedge that is missing.

**R-10 · BLOCKING · lines 11, 19, 122, 310–314.** The bound claimed per held cell, w/2, is not the bound
containment gives; the larger observed gap is (A-1). Numerically small at high ν; logically it is the same
mistake the paper corrects in its source. (A-1.)

**R-11 · MAJOR · lines 11, 19, 310, 122.** "Each held cell bounds its own local perturbation" is stated in the
abstract, §0 and §7 without the hypothesis Corollary 2 carries, "whose neighbours are unperturbed". In an
atom a perturber does not displace one level and leave its neighbours alone: it shifts every level within a
few units of n along a smooth phase profile (Lu and Fano 1970), the neighbours move in the same direction as
the cell, and a series can stay monotone while every level is displaced by more than the local gap. What the
held cell bounds is the displacement of the level *relative to its two neighbours*. That is a legitimate and
weaker statement, and the paper's "no configuration interacts with … by more than" reading (the source's
wording, which the paper wisely drops) is not licensed. *Resolve:* state the bound as a bound on the
displacement relative to the neighbours, under the stated hypothesis, in all four places; add Lu and Fano
(1970) and say in one sentence what a Lu–Fano analysis gives instead (a fitted, model-dependent, and far
tighter bound).

**R-12 · BLOCKING · lines 11, 239–241.** In atomic units A = Z²/2 and the self-concordance threshold is
ν ≤ 0.87 Z: no Rydberg state of a neutral atom is "self-concordant". The paper's 405.7 is a statement about
cm⁻¹. (A-4.)

**R-13 · MAJOR · lines 343–351, Table 6.** The thresholds behind Table 6 are not stated, only "tabulated". The
check uses Li III 987,662.29, Be IV 1,756,018.81, B V 2,744,111.38 cm⁻¹. My recollection is that ASD lists Li III
at 987,661.0 cm⁻¹ (122.454 35 eV); if so the Li III deficit is 102.4 and the ratio 0.866, not 0.876 — to be
verified against the database, not against my memory. Either way, three numbers on which a published
ratio depends must be printed with their source and uncertainty (ASD gives ±). Also print the masses used
(atomic mass minus Z·mₑ is fine; say so). *Resolve:* a column "I (cm⁻¹, source, ±)" in Table 6 and the
values in the E9 line.

**R-14 · MAJOR · lines 66–72, 298, 300.** "Half a unit in the last quoted decimal as the only tolerance"
treats the printed precision as the uncertainty. ASD levels are routinely printed to more digits than their
uncertainty, and sometimes fewer; the strict rule therefore manufactures failures at well-measured cells and
passes at coarsely quoted ones. On the present data 39 of the 1,145 passes are decided by the floor alone, 25
of the 406 failures lie within 2q of an edge and 84 within 5q, and at 64 cells (32 held) the defect interval is
itself narrower than 2q — there the verdict is the floor's and not the atom's, and D7's admissibility test
(level separation against q) does not catch it, because it never looks at the interval's width. *Resolve:*
(i) add a refusal clause "REFUSED when E_hi − E_lo < 2q" or report that class separately; (ii) print the
sensitivity of the 1,145 / 406 split to the tolerance (q, 2q, 5q); (iii) where ASD gives an uncertainty, say
what the test does with it, or say that it does not use it.

**R-15 · MINOR · lines 42, 46–50.** R∞ is used for ν and δ of every species; the reduced-mass Rydberg differs
by up to 1.4 × 10⁻⁴ (Li) and 8 × 10⁻⁵ (He), which puts a spurious ≈ 10⁻⁴·ν/2 into every δ of the light species.
It largely cancels across a triple, so the test is unaffected; the paper should say so in one sentence, since it
is careful about the same term in §8.

**R-16 · MINOR · lines 42, 343.** Z is "the charge seen by the excited electron" in §1 and the nuclear charge in
§8; they coincide for the hydrogenic ions but the symbol is overloaded. *Resolve:* Z_c for the spectroscopic
charge, or a sentence.

**R-17 · MINOR · line 353.** "The remainder has the sign and the Z⁴ scaling of the 1s Lamb shift" — the
measured ratios rise 0.876 → 0.893 with Z, which is what the logarithm in the Lamb shift does; fine as
hedged ("not pursued here"), but "0.88–0.89 at all three charges" should be "0.876 to 0.893".

On the physical quantities and units otherwise: R correct; the Dirac 1s term Z⁴α²R_M/4 correct; ν_fail's
table correct; the hydrogenic ν < 2 at Li III 2s correctly explained (161). Provenance is the weak point
(R-13, and the referee's R-19). The perturbation-bound claim, once stated as a relative bound under its
hypothesis and with the correct gap, is a small but genuine contribution: a fit-free, falsifiable number per
cell. It is not a competitor to quantum-defect analysis and the paper should not let a reader think it is.

### B.3 A journal referee

The paper delivers what its §0 promises, with two exceptions: the per-cell bound (A-1, R-11) and the
self-concordance claim (A-4). The abstract's other sentences are borne out by the body and the check. The
verification record is unusually explicit and mostly honest; where it is not, it is because labels are used
loosely rather than because anything is hidden (A-7, A-8, A-9). Novelty is modest and the paper mostly says
so: the exact price 4r³/(3r² − 1) with the floor 32/11, the exact gaps and the corrected failure condition,
the exact Aitken form, and the data run are the contributions. Two of these need a literature sentence.

**R-18 · MAJOR · References.** Missing standard references, with what each is for:
- Lu, K. T. and Fano, U. (1970). Graphic analysis of perturbed Rydberg spectra. *Physical Review A* 2, 81–86 —
  the standard treatment of locally non-monotone quantum defects, which is what the 406 failures are (R-11).
- Fano, U. (1970). Quantum defect theory of ℓ uncoupling in H₂ as an example of channel-interaction treatment.
  *Physical Review A* 2, 353–365 — MQDT's origin, beside Seaton (1983).
- Aymar, M., Greene, C. H. and Luc-Koenig, E. (1996). Multichannel Rydberg spectroscopy of complex atoms.
  *Reviews of Modern Physics* 68, 1015–1123 — the review a physicist expects in a paper about perturbed series.
- Edlén, B. (1964). Atomic spectra. In *Handbuch der Physik* 27, 80–220. Springer — the classical account of
  Rydberg–Ritz series analysis; the source itself cites it.
- Brezinski, C. and Redivo Zaglia, M. (1991). *Extrapolation Methods: Theory and Practice*. North-Holland,
  Amsterdam — Aitken's Δ² on algebraically convergent sequences x_n ∼ L + c n^{−α} is known to converge to
  L + c n^{−α}/(α + 1) asymptotically; Theorem 12 is the exact α = 2 instance and should say so (see also Wimp, J.
  (1981). *Sequence Transformations and Their Applications*. Academic Press, New York).
- Moore, R. E., Kearfott, R. B. and Cloud, M. J. (2009). *Introduction to Interval Analysis*. SIAM, Philadelphia;
  Neumaier, A. (1990). *Interval Methods for Systems of Equations*. Cambridge University Press — the modern
  statements of excess width that §4's "Prior art" paragraph invokes through Moore (1966) alone.
- Nesterov, Y. (2018). *Lectures on Convex Optimization*, 2nd ed. Springer — the self-concordance parameter M
  that A-4's repair needs, if Theorem 11 is kept.
Also: the ASD entry should carry the retrieval dates the text mentions.

**R-19 · MAJOR · lines 288–290.** Data availability. "Held as 86 tables" does not tell a reader where to get
them, and Run A's "fixed list of 285 series whose membership … was assigned in advance" does not say by what
rule or by whom. A paper whose result is a count over a data set must make the data set obtainable: publish
the 86 tables (or the ASD query per spectrum: spectrum, level-table options, retrieval date, version) and the
285-series list with thresholds as supplementary data, and state the selection rule for Run A. This is the
one thing a journal would refuse to waive.

**R-20 · MAJOR · lines 290, 400–402.** The verification record calls E1 an independent implementation; it
is the same algorithm written twice (A-7). Say what is independent or make it so.

**R-21 · MAJOR · line 398, and the status labels.** "30 PROVED … no floating point" is not true of fourteen
of the thirty (A-8); MEASURED is a label the contract forbids (A-9). The record must match the check.

**R-22 · MINOR · lines 3, 11.** The thesis says "never below 32/11" without the ν ≥ 2h qualifier the abstract
carries (A-20); the abstract's self-concordance and per-cell-bound clauses are A-4 and A-1.

**R-23 · MINOR · line 227.** The prior-art paragraph should also concede that Theorems 1–3 and 6 are
elementary (the source's own compendium attributes the monotone bracket to Milne-Thomson and the floor to
Jensen) and that Theorem 12 is an instance of a known asymptotic (R-18); the paper's novelty is then stated
exactly.

**R-24 · MAJOR · Figure 1.** Caption and plate disagree on which asymptote is drawn (A-11); a referee checks
figure legends against captions first.

Correctness otherwise: I checked Theorems 4, 5, 8, 10, 11, 12 by hand and the Z3 encodings against the
theorem statements; all hold. Clarity is good; the §0 separation of guarantee / failure / price / test is the
right frame and is kept. Readiness: not yet — A-1 and A-4 change sentences in the abstract.

---

## Part C — the record

| id | severity | line(s) | finding (short) | disposition |
|---|---|---|---|---|
| A-1 | BLOCKING | 122, 11, 19, 310, 314; E7; SOURCES §3.3/§3.7 | Corollary 2's w/2 does not follow from |Δ| ≤ g₋; bound is the larger observed gap (0.970 / 5,389) | FIXED — Corollary 2 restated: |Δ| ≤ max(g₋, g₊) = g₋ = w/2 + e = (w/2)(1 + 2/V), new exact identities I39–I40 and the excess 2/V (I41); E7 now measures the larger observed gap (tightest 0.970 cm⁻¹, median 5,389; larger gap toward n − 1 at 1,141 of 1,145, w/2 printed beside it for the record); Figure 4 regenerated on the new quantity; abstract, §0, §7 and SOURCES §3.3/§3.7 rewritten; the hypothesis "neighbours unperturbed" carried in every statement. |
| A-2 | MAJOR | 60–62, 72, 94 | D5/D8 name the reversed interval; Lemma 2 has it right | FIXED — D5 now defines E_lo := I − Z²R/(n − δ_hi)², E_hi := I − Z²R/(n − δ_lo)² ("the larger defect giving the lower energy"); Lemma 2 concludes E_lo ≤ E(n) ≤ E_hi; D8 inherits the ordered labels. |
| A-3 | MAJOR | 175, 186 | Theorem 7's y′ < 0 case by "−y" is wrong (concave); "squares" wording | FIXED — the y′ < 0 case reduces by reflection z(u) := y(2x − u), with z′ > 0, z(x ± h) = y(x ∓ h), w, e, V unchanged; "the four squares cancel" → "the terms A(h)A(t) and B(h)B(t) cancel". |
| A-4 | BLOCKING | 11, 76, 237, 239–241 | self-concordance threshold is unit-dependent; interpretive claims are artefacts of cm⁻¹ | FIXED — Theorem 11 restated as the exact identity |T‴|/(2T″√T″) = ν/√(3A/2) (new grid identity I19b) with its unit dependence explicit: 405.7 (cm⁻¹), 4.52 (eV), 0.866 (hartree) at Z = 1 (I20); E11 prints the ratio at the deepest cell in cm⁻¹ (0.1651) and hartree (77.4); the sentence "carries its meaning across the whole measured range" and the abstract's clause are removed; §5 states what survives a change of unit (λ² = (2/3)T exact, and the ratios V, w/T, e/T); D10 states the non-invariance; Nesterov (2018) cited. |
| A-5 | MAJOR | 237 | "affinely invariant … why Z²R cancelled" is false | FIXED — sentence replaced: invariance is under affine maps of the variable, T ↦ cT carries λ² to cλ²; Z²R cancels from V because w and e are each linear in T and V is their ratio; V's dependence through r alone is the domain-side invariance. |
| A-6 | MAJOR | 280 (302, 316) | ν_V does not follow from D12; "second difference 3A/ν⁴" is e; thresholds 5q vs 10q | FIXED — D12 now derives ν_V from its own k = 1 rule: Δ²T = 2e ≈ 6A/ν⁴, |Δ²T| > 20q ⟺ ν < ∜(3Z²R/(10q)) = 134.7, 75.7, 42.6 (I26, which prints the 5q form beside it for the record); §7's e ≥ 10q filter identified as the same threshold; SOURCES §3.12 records the source's threshold as superseded. |
| A-7 | MAJOR | 290, 400–402; check.py 554–575 | E1's reference is a transcription, not independent | FIXED — `ref_series` rewritten from D8 in a different form: Decimal arithmetic at 40 digits, the test taken in δ-space with the floor carried by the inverse of Lemma 2's map, the floor from the decimal exponent of the printed string, admissibility as 2T√T/(qZ√R), members addressed by n; shares no line with the instrument; agrees at all 1,551 cells (E1); §10 states each difference and the guard's limit (a shared misreading of D8 would pass). |
| A-8 | MAJOR | 398; check.py labels | 14 float evaluations and an SVD labelled PROVED; count overstated | FIXED — new label ARITHMETIC in check.py for the 14 floating-point evaluations of proved closed forms (I14, I15, I18, I20, I25, I26, I28, I32, I37, I38, I41, E9b, E10, E13); I11 and I12 made exact (1/144; 4/26,910 strictly between 10⁻⁴ and 10⁻³); E10 relabelled a numerical corroboration; the count restated as 21 PROVED (all exact Fraction), 10 EXHAUSTIVE, 4 MACHINE-CHECKED, 12 MEASURED, 14 arithmetic, 3 guards; §0 and §10 define the label. |
| A-9 | MAJOR | 34, 298, 306, 314, 327, 351, §10 | MEASURED-as-a-label is forbidden by spec §8; lint lacks the pattern | DECLINED — resolved by the contract: PAPER-SPEC §5 now admits MEASURED as a declared status word ("a number computed from cited data by a stated procedure — the paper's own result, with its sample stated") and §8 exempts it as such. §0's row is reworded to §5's definition and every MEASURED caption and table row now names its sample. SAMPLED is not used because the paper runs no seeded sweep as a claim (G1's 400 seeded triples are a guard, now labelled with its seed). lint.py lies outside the paper's directory and is not edited by the drafter. |
| A-10 | MAJOR | 288, 290 | "one per spectrum" false; 74 labels are 58 spectra; "nine" tables includes a non-table | FIXED — new obligation E0 measures 86 tables covering 64 distinct spectra (label → species map read from the thresholds file), 8 level tables and 1 cross-check file set aside; E2 prints 395 series across 58 spectra (74 table labels); §7 text corrected accordingly. |
| A-11 | MAJOR | 165–167 | Figure 1 legend "4ν/3" vs caption's 26/9 (two-term form) | FIXED — Figure 1 regenerated by figures.py (now COMPUTED, from I5/I9–I12) with the legend "two-term asymptote 4ν/3 + 4/(9ν)" and the one-term 4ν/3 drawn in the inset; caption revised to match; FIGURES.tsv records the replaced plate's md5 and the reason. |
| A-12 | MAJOR | 126, 200 (PDF pp. 5, 8) | Table 1 and Table 2 headers broken by the bars in \|Δ\| and \|p − 1\| | FIXED — headers escaped (\|Δ\|, \|p − 1\|); Chrome screenshot of the rendered HTML read: both headers intact (Table 1: |Δ| (cm⁻¹) · ν_fail, Z = 1 · ν_fail, Z = 2; Table 2: 4ν/(h·|p − 1|)). |
| A-13 | MINOR | pp. 1, 3, 5, 8–11, 13–16 | literal ^{…}, _…, Σ_{…} in prose and displayed blocks; mid-formula wraps | FIXED — every ^{…}, _… and Σ_{…} replaced: Unicode superscripts (xᵖ, T⁽ʲ⁾, (−1)ᵏ⁺¹⁺ᵐ, 2ᵏ⁺¹, s²ᵏ, ν²ᵃ⁺³ᵇ, νᵖⁱ, n⁻ᵅ), root signs (∛, ∜), f″√f″ for the 3/2 power, xₙ, mₑ, and backticks for ν_fail, ν_V, r_adm, E_lo, E_hi, δ_lo, δ_hi, δ_∞, R_M; Theorem 8's sums rewritten and its displayed block split onto two lines; no caret or brace remains in the source. |
| A-14 | MINOR | all figures | bare "Figure N" line above each caption | FIXED — empty alt text on all five figures. |
| A-15 | MINOR | Figure 2 | pole annotation overprinted by curves | DECLINED — Figure 2 is the audited plate held byte-exact from the tree (FIGURES.tsv, md5 ad04ecb1…); the annotation is overprinted but legible, and regenerating would trade a tree-audited plate for a redrawn one to cure a cosmetic overlap. |
| A-16 | MINOR | 288, 290, 310, 333, 335, 347–349, 353 | numbers with no printed check line; −0.005 computed nowhere | FIXED — E0 prints the table, spectrum and set-aside counts; E7 prints 2Z²R/ν³ at the tightest cell (0.844); I37 prints all seven widths and six ratios; E9 prints every threshold with its deficit and Dirac term; new E9b computes the δ shift (−1.34 × 10⁻⁵·ν³, −0.0046 at n = 7) and §8 now prints that instead of "−0.005 growing as n³". |
| A-17 | MINOR | 400 | G1's seed not named | FIXED — "400 seeded random rational triples (seed 3)" in G1's printed line and in §10. |
| A-18 | MINOR | check.py 442–494 | guards do not gate M1–M4 | FIXED — `GUARDS_OK` gates `z3_prove`: if G1 or G2 fails, M1–M4 are reported as failed with "NOT REPORTED: guard … failed"; §10 says a failing guard is not silent. |
| A-19 | MINOR | 276 | "560 two-sided brackets" is automatic | FIXED — Theorem 13 and I34's line now say the 560 two-sided brackets are automatic (m = 0 and m = 1 have opposite parity) and are not a finding; §10's row counts the 2,800 sign checks only. |
| A-20 | MINOR | 3 | thesis "never below 32/11" lacks ν ≥ 2h | FIXED — thesis reads "never below 32/11 once ν ≥ 2h". |
| A-21 | MINOR | 52, 153, 302 | interior cell defined at unit step only | FIXED — D3 defines an interior cell at step h (h = 1 when unqualified) and a triple at step h. |
| A-22 | MINOR | 32 | MACHINE-CHECKED redefined from spec §5 (stronger; recorded) | DECLINED (recorded) — the check ranges over all of linear real arithmetic, which is stronger than the spec's finite box; §0's row already said so and §10 now adds "stronger than a box, and stated as such". No change to the check. |
| A-23 | MINOR | 288, 290 | "re-retrieved", "sealed implementation" are process words | FIXED — "retrieved from the database in August 2026"; "the implementation of D8 the data were first tested with". |
| A-24 | MINOR | FIGURES.tsv, 304, 312 | fig3/fig4 file names swapped against figure numbers | FIXED — files renamed fig3-v-measured.png (Figure 3) and fig4-bounds.png (Figure 4); figures.py, FIGURES.tsv and the paper updated; fig3's bytes unchanged (same md5). |
| A-25 | MINOR | 377; check.py I23 | I23 PROVED in check, EXHAUSTIVE in §10 | FIXED — I23 labelled EXHAUSTIVE (796 cases) and its line says the general statement follows from I24; Corollary 2 cites I24 for the identity and I23 for the family. |
| A-26 | MINOR | 110–114 | "above/below" means T-order in one sentence and n-order in the next | FIXED — gaps named by neighbour ("toward n − 1", "toward n + 1") in Lemma 3, the sentence before it, Table 1's caption and §7's gaps paragraph. |
| R-1 | BLOCKING | 122 | = A-1 (mathematician) | = A-1: FIXED. |
| R-2 | MAJOR | 60–62, 94 | = A-2 | = A-2: FIXED. |
| R-3 | MAJOR | 175 | = A-3 | = A-3: FIXED. |
| R-4 | MAJOR | 76, 239–241 | = A-4 (as mathematics) | = A-4: FIXED. |
| R-5 | MAJOR | 237 | = A-5 | = A-5: FIXED. |
| R-6 | MINOR | 225 | Proposition 1's objective adds an energy to a number; units of α, β | FIXED — Proposition 1 states that α carries the reciprocal unit of w and β is dimensionless, so the objective is a number. |
| R-7 | MINOR | 361–363 | Lemma 7 trivial; "ambient/actual" undefined | FIXED in part — the SVD is relabelled a floating-point corroboration and moved out of the proof (E10 ARITHMETIC); "an ambient over an actual" replaced by a plain sentence ("the ratio of what the bracket admits, an interval, to what the estimate misses, an error"); Lemma 7 is kept as a lemma, stated as elementary, because Table 2's reading rests on it — that part DECLINED. |
| R-8 | MAJOR | 280 | = A-6 | = A-6: FIXED. |
| R-9 | MINOR | 276 | = A-19 | = A-19: FIXED. |
| R-10 | BLOCKING | 11, 19, 122, 310–314 | = A-1 (physicist) | = A-1: FIXED. |
| R-11 | MAJOR | 11, 19, 122, 310 | bound is relative to neighbours under "neighbours unperturbed"; hypothesis dropped in abstract/§0/§7; cite Lu–Fano | FIXED — the hypothesis "neighbours unperturbed" and the words "relative to its neighbours" now appear in the abstract, §0 (twice, including "What is not claimed"), Corollary 2 and §7; Corollary 2 carries a paragraph on the Lu–Fano case (a perturber moves the neighbours with the cell; a series can stay monotone while every level is displaced) and says what a Lu–Fano or MQDT analysis returns instead; Lu and Fano (1970), Fano (1970) and Aymar, Greene and Luc-Koenig (1996) cited. |
| R-12 | BLOCKING | 11, 239–241 | = A-4 (in atomic units ν ≤ 0.87 Z) | = A-4: FIXED. |
| R-13 | MAJOR | 343–351 | Table 6 thresholds unstated; Li III value to be verified against ASD (987,661.0?) | FIXED — Table 6 gains columns I (cm⁻¹), ± and source; the thresholds are printed as the tree holds them: Li III twice — the database's published ionization energy 987,661.0139 ± 0.0009 (the referee's recollection is corroborated by the tree, not by memory; ratio 0.865) and the limit fitted to the theoretical level series 987,662.29 ± 0.36 (0.876) — Be IV 1,756,018.8100 ± 0.0008 (0.879), B V 2,744,111.38 fitted with no published uncertainty held (0.893); masses stated as AME2020 atomic mass less Z·mₑ; nothing chosen between the two Li III values (SOURCES §3.6). |
| R-14 | MAJOR | 66–72, 298, 300 | floor as sole tolerance; 39 passes and 25/84 fails within q/2q/5q; 64 intervals narrower than 2q; D7 never looks at interval width | FIXED — new obligation E12 and a §7 paragraph "What the tolerance decides": 39 of 1,145 passes hold only by the floor; 25 of 406 fails within 2q, 84 within 5q; 64 cells with E_hi − E_lo < 2q (32 held) reported as a class; the split at tolerance 0/q/2q/5q (1,106/445; 1,145/406; 1,170/381; 1,229/322); the test uses no database uncertainty and says so. Part (i), a new refusal clause in D8, DECLINED: D8 is the rule the instrument implements and no threshold in the check may move; the class is reported apart instead. |
| R-15 | MINOR | 42, 46–50 | R∞ vs reduced-mass R for light species; say it cancels | FIXED — §1 states the reduced-mass difference (≤ 7.8 × 10⁻⁵, lithium) and §7 gives its effect: 3.9 × 10⁻⁵·ν, the same to within 3.9 × 10⁻⁵ across a triple (new E13); the containment statement does not see it. (The audit's Li/He figures were transposed; lithium is the lightest species tested and its m_e/M is 7.8 × 10⁻⁵.) |
| R-16 | MINOR | 42, 343 | Z overloaded (spectroscopic vs nuclear) | FIXED — §1 says Z is the nuclear charge for a one-electron ion and §8 uses it in that sense; §8 opens by saying so. |
| R-17 | MINOR | 353 | "0.88–0.89" → "0.876 to 0.893" | FIXED — "runs from 0.865 to 0.893 across the three charges, rising with Z" (the range widened with R-13). |
| R-18 | MAJOR | References | missing Lu–Fano 1970, Fano 1970, Aymar–Greene–Luc-Koenig 1996, Edlén 1964, Brezinski–Redivo Zaglia 1991 (Wimp 1981), Moore–Kearfott–Cloud 2009, Neumaier 1990, Nesterov 2018 | FIXED — Lu and Fano (1970), Fano (1970), Aymar, Greene and Luc-Koenig (1996), Edlén (1964), Brezinski and Redivo Zaglia (1991), Wimp (1981), Moore, Kearfott and Cloud (2009), Neumaier (1990) and Nesterov (2018) added, each with details verified by search or from the tree (Edlén), and each cited where it belongs (Corollary 2, §2, §4 prior art, §5 remark, D10); the ASD reference carries its retrieval. |
| R-19 | MAJOR | 288–290 | data availability; Run A's selection rule | FIXED — a Data availability paragraph names NIST ASD 5.12, the retrieval, the query form, and offers the 86 tables with thresholds, the 285-series list with n-ranges and the per-cell verdicts as supplementary data; Run A's selection rule stated (a channel compilation that fitted δ₀ + δ₂/(n − δ₀)² and recorded the n-range, 250 + 35 series, fixed before the test). |
| R-20 | MAJOR | 290, 400–402 | = A-7 | = A-7: FIXED. |
| R-21 | MAJOR | 398 | = A-8, A-9 | = A-8 (FIXED), A-9 (DECLINED, resolved by the contract). |
| R-22 | MINOR | 3, 11 | = A-20, A-1, A-4 in the front matter | = A-20, A-1, A-4: FIXED. |
| R-23 | MINOR | 227 | prior-art paragraph: concede the elementary theorems and the Aitken asymptotic | FIXED — the prior-art paragraph concedes that Theorems 1–3 are remarks on ordered triples and Theorem 6 is Jensen on three points, and that Theorem 12 is the exact α = 2 instance of a known asymptotic (new remark after Table 3, with Wimp 1981 and Brezinski–Redivo Zaglia 1991). |
| R-24 | MAJOR | 165–167 | = A-11 | = A-11: FIXED. |

Distinct findings: **2 BLOCKING** (A-1, A-4) · **15 MAJOR** (A-2, A-3, A-5, A-6, A-7, A-8, A-9, A-10, A-11, A-12,
R-11, R-13, R-14, R-18, R-19) · **20 MINOR** (A-13 … A-26, R-6, R-7, R-15, R-16, R-17, R-23). The R rows marked "="
restate an A row and take its disposition.

---

## Repair record (drafter, 24 September 2026)

Every finding above carries a disposition. Counts by severity: **BLOCKING 2 — 2 FIXED** (A-1, A-4);
**MAJOR 15 — 14 FIXED, 1 DECLINED** (A-9, resolved by the contract's own amendment of §5/§8; R-14 fixed with
its clause (i) declined); **MINOR 20 — 18 FIXED, 2 DECLINED** (A-15, the audited plate kept; A-22, recorded
as a deviation stronger than the spec). The R rows marked "=" take their A row's disposition.

**PAPER.md.** Date 24 September 2026. Thesis qualified (ν ≥ 2h). Abstract: self-concordance clause replaced
by its unit dependence; the per-cell bound restated as the larger observed gap, relative to unperturbed
neighbours, tightest 0.97 cm⁻¹; the tolerance's share announced. §0: the failure-condition and price
paragraphs, two new items under "What is not claimed", the MEASURED row reworded to §5's definition, a
sentence defining an arithmetic evaluation. §1: Z for hydrogenic ions and the reduced-mass sentence; D3 at
step h; D5 with ordered labels; D8 uses no database uncertainty; D9 and D10 in Unicode, D10 with the
non-invariance stated. §2: Lemma 2's conclusion; Edlén cited. §3: gaps named by neighbour; Corollary 2
rewritten with I39–I41 and a paragraph on the Lu–Fano case; D11 and Table 1 with ∛ and escaped bars. §4:
Figure 1 caption and file; Theorem 7 by reflection and the cancelling terms; Theorem 8 in Unicode with the
block split; Table 2 header escaped; Proposition 1's units; the prior-art paragraph's concessions and the
modern interval references. §5: the affine-invariance sentence replaced; Theorem 11 restated with its unit;
the general Aitken asymptotic as a remark after Table 3. §6: Unicode throughout; the 560 brackets as
automatic; D12 with ν_V from D12's own threshold. §7: the data paragraph (86 tables / 64 spectra; eight set
aside; one cross-check file), the two-runs paragraph (Run A's rule; 58 spectra; the independent reference),
Table 4's sample, the new paragraph "What the tolerance decides" (E12, E13), Figure 3's file, the gaps by
neighbour, the bound paragraph on the larger gap (E7), Figure 4's file and caption, Table 5's sample, a Data
availability paragraph. §8: Z as nuclear charge; Table 6 with I, ± and source columns and Li III on both
thresholds; the range 0.865–0.893; the δ shift from E9b. §9: Lemma 7's SVD as corroboration; the remark's
first sentence. §10: the table's rows and columns, the count (64 obligations: 21 PROVED, 10 EXHAUSTIVE, 4
MACHINE-CHECKED, 12 MEASURED, 14 arithmetic, 3 guards), the guards' seed and gating, a paragraph on the
data guard's independence. References: nine added (Aymar–Greene–Luc-Koenig 1996; Brezinski–Redivo Zaglia
1991; Edlén 1964; Fano 1970; Lu–Fano 1970; Moore–Kearfott–Cloud 2009; Nesterov 2018; Neumaier 1990;
Wimp 1981); ASD retrieval noted.

**check.py.** New obligations E0 (tables/spectra), E12 (the tolerance's share), E9b (the δ shift), E13
(reduced mass), I19b (the self-concordance ratio identity), I39–I40 (the gaps against w and e), I41 (the
excess 2/V). E7 measures the larger observed gap and prints w/2 beside it. E9 reads the published Li III
ionization energy from the tree and prints every threshold with its uncertainty and source. I26 derives ν_V
from D12 and prints the 5q form for the record. I11, I12 made exact; I23 relabelled EXHAUSTIVE; fourteen
float evaluations (and E10) relabelled ARITHMETIC; I20 prints the threshold in three units; E11 prints the
ratio in two units. `ref_series` rewritten as an independent implementation (Decimal, δ-space, decimal
exponent, admissibility from T, members by n). `GUARDS_OK` gates M1–M4. G1's line names its seed. Nothing
was weakened and no threshold moved: every pre-existing assertion still holds and the only assertions
touched became stricter (I11, I12) or gained a conjunct. Runs: `python3 check.py` 64 obligations, 0 failed;
`--selftest` 69, N1–N5 each refuted, 0 failed.

**Figures.** `figures.py` now draws Figure 1 (fig1-cost-exact.png, COMPUTED; the audited plate figure-23.1,
whose legend disagreed with its curve, is no longer used), Figure 3 (renamed fig3-v-measured.png, bytes
unchanged), Figure 4 (fig4-bounds.png, the larger observed gap on the y-axis) and Figure 5 (unchanged
bytes). Figure 2 remains the audited plate. FIGURES.tsv rewritten with the new md5s and the reasons.

**SOURCES.md.** RB row (the reference's independence), a new IE row (the ASD ionization-energy table), the
level-table paragraph (64/58 spectra), the per-section notes for §3, §5, §6, §7, §8, §3.3 (the bound is
the larger gap; the first draft's w/2 named as the audit's finding), §3.5 (the unit), §3.6 (both Li III
thresholds; B V's provenance), §3.7 (0.970 / 5,389), a new §3.12 (ν_V), §5's table rows, and
interpretations 10–13.

**Lint, render, typography.** `lint.py`: 0 hits. `render.py`: 22 pages (18 before the repair). The
rendered HTML was screenshotted with headless Chromium and read: Table 1 and Table 2 headers intact, Table 6
intact with its new columns, no caret, underscore or brace in prose.

**Second pass (coordinator's note, same day): no code spans for symbols.** The first pass had set nine
symbols in backticks, which PAPER-SPEC §9 reserves for code, and the rendered PDF's text carried fifty
literal underscores. Every one is replaced by a Unicode form, each introduced once where the old symbol
stood: the ordered defects and interval ends δₗₒ ≤ δₕᵢ and Eₗₒ ≤ Eₕᵢ (D5; chosen so as not to collide with
δ₋/δ₊ and E₋/E₊, which name the neighbours), the admissibility ratio rₐ (D7), the critical depth νᶜ (D11,
Table 1), the resolution bound νᵛ (D12), the reduced-mass Rydberg constant Rₘ (§8), the Ritz limit δ₀ in
the worked deduction (the symbol §2 already uses), and ΔE for the energy displacement (Corollary 2). Source
and PDF text now carry zero underscores (pypdf extraction over all 22 pages: 0 "_", 0 "^", 0 "\\"), lint 0
hits, `check.py` 64/0 and `--selftest` 69/0 unchanged; the backticks that remain are `unsat` and the tag
letters of §10, which are code.

