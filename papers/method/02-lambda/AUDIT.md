# AUDIT.md — 02-lambda, "The Lattice of One-Electron Transitions"

Audit of the draft dated 24 September 2026 (PAPER.md 583 lines, check.py 1,543 lines, SOURCES.md,
FIGURES.tsv, eight figures; rendered to `out/02-lambda.pdf`, 26 pages). Written 2026-09-24 against
`BRIEF-AUDIT.md` and `PAPER-SPEC.md` §4, §5, §8, §9, §10. Nothing in PAPER.md or check.py was edited.

Runs used: `python3 check.py` — 72 rows, 0 failures, 53 s, exit 0; `python3 check.py --selftest` — 78
rows, 0 failures, 61 s, all six negative controls refuted (PATH with `method/bin` first, Python 3.12.3,
Z3 5.1.0). `python3 papers/method/lint.py papers/method/02-lambda` — 0 hits. Two independent
recomputations were written for this audit from the paper's own definitions, importing nothing from
check.py: (i) the cover relations of Λ derived from the order alone (x < y with no z strictly between),
and (ii) the set-cover instance of Theorem 17 and its exhaustive enumeration grouped by full witness
signature without the element reduction. Their results are quoted where they bear on a finding.

Severity: BLOCKING / MAJOR / MINOR, as the brief defines them. Findings are `A-n` (Part A) and `R-n`
(Part B); Part C tabulates all of them with the disposition column blank.

---

## Part A — content audit

### A.1 Every definition, lemma, theorem and number against the source

The source passages are those `SOURCES.md` names (M = main volume, C = mathematical compendium, I =
index of indices, all under `method/members/`). "Relation" says whether the paper's statement is the
source's, weaker, or stronger; "proof" whether every step is justified in the paper.

| item (PAPER.md line) | source | relation | proof complete? |
|---|---|---|---|
| Physics paragraph (57) | M §7.1 1755–1768; C §IV.L 1092–1170 | source's, but see R-16, R-17, R-19, R-20 | n/a |
| D1–D4 (59–77) | M §7 1729–1768; I 11–38 | source's; caps convention M §8 1801–1816 made explicit; A₄, A₇, A₈ inferred (R-8) | n/a |
| D5, D6 (79–81) | standard | — | n/a |
| Theorem 1 (83) | M §7.3 1781–1793; C §IV.L 1432–1440 | source's (both operations written out, as C does) | yes |
| Lemma 1 (87) | new (generalises §7.3) | stronger than source (φ uninterpreted) | yes ("the argument of Theorem 1 restricted to one bound" is exactly that argument) |
| D7 (91) | M §6.1 via SOURCES; M §14.1 3687–3715 | source's | n/a |
| Lemma 2 (97) | M §14.1 3687–3715 (one direction) | weaker than source's iff (only ⟹ is proved; the converse is deferred to the companion paper) | yes |
| Theorem 2 (101) | M §7.3 1791–1792; C 990–998; I 1355–1362 | source's, plus five settings named where the source names only counts (SOURCES interpretation 5) | computation; wording defect A-7 |
| Table 1 (105) | M §7.1 1755–1768 | source's | — |
| Table 2, Corollary 1 (117–127) | C 1181–1202; M §11.5 2236–2247; M §10.2 2043–2050 | source's (673, 575, 564, 308, 300, 200, 25, 24; 1,000; the 24 at f = 0, g = 3) | computation |
| Lemma 3 (129) | M §8.5 1906–1918; §11.4 2231–2235; C 1642–1650 | stronger (adds the orientation and its acyclicity, needed by Theorem 4) | yes |
| Theorem 3 (145) | M §8.1 1818–1823; C 1482–1490 | source's | yes |
| Theorem 4 (149) | M §8.2 1824–1851; C 1522–1530 | stronger: the grading (every cover is a unit step) is proved; the source only asserts a "rank grading" | yes — the rewritten step is checked below (A.2) |
| Theorem 5 (157) | M §8.4 1878–1905; C 1602–1610, 1592–1600 | source's (122 at 11, 854 matching edges, log-concave, skew −0.43) | yes for the instance (Dilworth, König, Fulkerson cited) |
| Theorem 6 (171) | M §8.3 1852–1877; A.19.0 10140–10180; C 1032–1040 | stronger: the form j(i,v) and the closed count are proved where the source states them | one line missing in the injectivity step (R-4) |
| Table 3 (189) | M A.19.0 table | source's, cell for cell, weights and forces identical | — |
| Theorem 7 (213) | M §8.3, §11.1.1 2099–2178; C 1062–1080 | source's | CITED + instance |
| Theorem 8 (219) | M A.19.0 10170–10180; C 1422–1430 | source's (9 within, 11 between, the eleven listed identically) | yes |
| Corollary 2 (231) | M §8.6 1919–1940; C 1472–1480 | source's (7, the same antichain, seven chains) | CITED + certificates |
| Corollary 3 (235) | C 1222–1243 | source's (1,113,045,672; "the two seventeens are one") | yes |
| Theorem 9 (239) | M §8.4 1892–1899; A.19.1 10182–10192; §11.8.1 2287–2307 | source's (the eight cells, ranks 6–14 even, no fixed point) | yes |
| D9, D10 (254–260) | M §9 1941–1962; §9.2 1963–2016 | source's | n/a |
| Theorem 10 (262) | M §9.2 (five forms); C 1532–1540 | source's | yes; wording R-12 |
| Theorem 11 (274) | M §9.2; C 1502–1510 | source's (same coordinate argument as C) | yes |
| D11 (298) | M §10 2026–2030 | source's | n/a; the word "volume" clashes with Figure 4 (A-11) |
| Theorem 12 (306) | M §10.4 2062–2079; A.10 10021–10035; C 1082–1104 | source's, with the source's 0-based hi₆/hi₇ re-indexed to hi₇/hi₈ | the leaf-order elimination is complete; the "read from the other end" aside contradicts the statement (R-2) |
| Theorem 13 (324) | M §10.3 2058–2060; C 1662 | source's | yes |
| Proposition 1 (330) | C 1662–1671 (base caps) | source's base-cap figures 0.2835/0.2013/1.4081 and 69.95–98.06 %; the 776M-pair figures of M §10.2 correctly not printed | computation; the Chebyshev remark is heuristic (R-9) |
| D12, Theorem 14 (342–356) | M §11.3 2216–2230; §11.1 2143–2147; C 1000–1010 | source's | yes |
| Corollary 4 (358) | M §11.1; C 1572–1580 | source's (976, 2, 10801/976) | computation |
| Lemma 4 (362) | M §11.6 2248–2255; C 1612–1620 | source's (319, k + 1 spins, E = 0) | yes |
| Theorem 15 (372) | M §11.8.1 2287–2307; C 1000–1030 | reproduces differently: the paper's five even alphabets against the source's "ℓ and f each have exactly two" (SOURCES item 2) — correct in the paper | yes for the instance; it is a cap-bound computation (R-3) |
| Corollary 5 (376) | M §11.8 2280–2286; C 1552–1560 | source's | computation; the equivalence with Theorem 9 is overstated (R-7) |
| D13, Theorem 16 (392–402) | M §9.3 2017–2025; A.9 10009–10020; C 1512–1520 | source's (the proof follows A.9 step for step) | yes (Birkhoff and Rota cited) — see R-14 on the precise citation |
| Corollary 6 (406) | M §9.3; C 1512 | stronger and corrected: the source's biconditional is stated only among unit hypercubes (SOURCES item 3); the paper states the exact form, 19,079 / 99,034 / 17,104 | yes; the comparison count in the remark is wrong (R-6) |
| D14, Theorem 17 (418–426) | C §IV.S 598–606, 782–790; M §14.5.7 via §14.5.9 | source's, proved from Theorem 2 rather than imported | yes |
| Theorem 18 (430) | M §14.5.9 3922–3963; C 670–678, 722–730 | source's exact figures (7, LB 5, 102 elements, 24,585, one common cell); the source's "forced by Chvátal's reduction" correctly rejected (SOURCES item 5) | exhaustiveness argued and independently reproduced (A.4) |
| Remark after 18 (440) | C 670–678; M §14.5.10–14.5.14 (superseded) | prints only the exact enumeration's figures | — |
| Corollary 7 (442) | C 660–668 (envelope-step law; s → s 71 %); M §14.5.12 | source's, proved from Theorem 17; 17,403/24,585 = 70.8 % | yes |
| Corollary 8 (446) | M §14.5.1 3768–3775; C 804–822 | source's | yes |
| §8 (462) | M §11.7 2256–2279; §7.1 1765–1768 | source's | — |

All of the twelve "source claims that do not reproduce" in SOURCES.md were read against their source
lines. Items 1–7 (the ones with a measured value) are fairly represented and every measured value
appears in the check's output: 17/24/33 at the further settings (row "Theorems 2 and 6, further cap
settings"); five even alphabets (row "Theorem 15, the free box vanishes"); 99,034 agree / 17,104 differ
(row "Corollary 6"); 17 and 17 against the compendium's "18 and 18" (row "Theorem 6"); smallest witness
set 4 against "Chvátal's reduction" (row "Theorem 18, one cell"); 0.2835 / 0.2013 / 1.4081 at the base
caps against the 776M-pair family (row "Proposition 1, the void-free fraction"); and the exhaustive
replacements of the sampled verifications (their rows). Item 3 is put slightly harder on the source
than the compendium deserves — C 1512 already restricts μ_arith's support to unit hypercubes in its
fine print — but the paper's Corollary 6 is the correct precise statement either way. Items 8–12 are
not printed, as SOURCES says.

### A.2 The rewritten proofs, read step by step

**Theorem 4, the grading (line 153).** Let x < y in Λ, S the set of differing coordinates. The child
relation (i is a child of j when the bound reads xᵢ ≤ φ(xⱼ)) restricted to S is a sub-relation of the
orientation of Lemma 3, hence acyclic; a finite acyclic relation has an element with no successor, so
some i ∈ S has no child in S. z := y − eᵢ. Box: zᵢ = yᵢ − 1 ≥ xᵢ ≥ floor. Bounds with i bounded:
zᵢ < yᵢ ≤ φ(yⱼ) = φ(zⱼ), j ≠ i. Bounds with i bounding, xₘ ≤ φ(xᵢ), m a child of i: m ∉ S so
zₘ = yₘ = xₘ ≤ φ(xᵢ) ≤ φ(yᵢ − 1) = φ(zᵢ), using xᵢ ≤ yᵢ − 1 (i ∈ S) and monotonicity. Bounds not
naming i unchanged. So z ∈ Λ, x ≤ z < y, and a cover forces z = x. Every step is justified; the
counterexample {(0,0),(1,1)} correctly shows why the shape is needed. Complete. Independently
confirmed: computing covers from the order alone gives 3,749 covers and every one is a unit step
(this is what check.py cannot confirm — see A-1).

**Theorem 6, the converse (line 185).** j join-irreducible with unique lower cover j⁻; Theorem 4 gives
j = j⁻ + eᵢ; v := jᵢ ≥ min Aᵢ + 1 since j⁻ᵢ = v − 1 ∈ Aᵢ. For x ∈ Sᵥ with j ≰ x: z = j ∧ x ∈ Λ (Theorem
1), z < j, zᵢ = min(v, xᵢ) = v. In a finite lattice every z < j lies below some lower cover of j (the
last step of a maximal chain from z to j), hence z ≤ j⁻, zᵢ ≤ v − 1: contradiction. So j = min Sᵥ.
Complete. The injectivity sentence "j(i, v) covers only j(i, v) − eᵢ" is asserted, not derived — one
line is missing (R-4), and the map is injective once it is supplied.

**Theorem 16 (line 398–402).** Follows M A.9: [x,y] ≅ down-sets of Q; antichain ⟹ Boolean ⟹ (−1)ᵐ;
non-antichain ⟹ the join of the atoms {m}, m minimal in Q, is the set of minimal elements, a proper
subset of Q ⟹ no subset of atoms joins to the top ⟹ every qₖ = 0 in Rota's crosscut sum ⟹ μ = 0.
Sound. The "meet 0̂" clause quoted in the crosscut statement is harmless here. The precise citation is
the corollary of the crosscut theorem (R-14).

**Corollary 6 (line 408).** |Q| = m by Theorems 7 and 4 (each cover adds one generator and one rank).
Boolean interval ⟹ atoms are x + eᵢ on distinct coordinates, top is their join, so y − x is a 0/1
vector with m ones; 2ᵐ elements fill the 2ᵐ-point box ⟹ box inside Λ. Converse: full box of 0/1
differences is Boolean of rank m ⟹ Q antichain. Arithmetic: N(y)/N(x) squarefree iff all yᵢ − xᵢ ≤ 1.
Complete and the statement is precise. The remark's "eight comparisons" is a miscount (R-6).

**Theorem 17 (line 425–426).** (⟹) (a): ℛ(G) ⊆ B(G) so Aᵢ(Λ) ⊆ Aᵢ(G) ⊆ Aᵢ(Λ). (b): φ̂(a;G) ≤ φ̂(a;Λ);
strict at (i,j,a) ⟹ the attaining cell z of Λ has zᵢ > φ̂(a;G) ≥ φ̂(zⱼ;G) (monotone in a, zⱼ ≤ a) so
z ∉ ℛ(G). The envelope over G is defined because (a) puts the minimum of Aⱼ in G. (⟸) same box, same
envelopes ⟹ ℛ(G) = ℛ(Λ) = Λ by Theorem 2 — at the caps where E(Λ) = 0. Complete; note the cap
dependence (R-3). The step reduction ("only the least argument realising each value needs covering") is
justified by monotonicity of φ̂(·;G) and is right.

**Theorem 18 (line 432–438).** Reduction: e₁'s witness set ⊇ e₂'s ⟹ e₁ may be dropped, preserving the
set of covers — right, and check.py's `keep` implements exactly this with a tie-break on equal sets.
Lower bound: pairwise-disjoint witness sets need distinct cells — right. Exhaustiveness: branching on
an uncovered element over every signature witnessing it, pruning only when depth + bound > limit —
every cover contains a witness of the chosen element, so no cover is lost; the record at `cov == RFULL`
precedes the depth cut, so covers of size exactly the limit are kept; covers are deduplicated as sorted
tuples; expansion by the product of multiplicities is right because signatures partition the cells and
distinct signature sets give distinct cell sets, and a cell cover of size 7 with two cells sharing a
signature would be a 6-signature cover, which does not exist. The enumeration is exhaustive. The
audit's independent implementation (no reduction, full 102-element signatures — which happen to be
distinct for all 976 cells — plain depth-limited branching) returns 0 covers at limits 1–6 and
24,585 at limit 7, common cell (2,1,3,3,2,1,3,0) only, minimum witness set 4, no uniquely witnessed
element, and q = k = 1, q = k = 2, q = k = 3 each present in all 24,585 covers.

**Theorem 11 triangle (line 280–284).** |a − c| + 1 ≤ u + v + 1 ≤ (u+1)(v+1); product over coordinates;
logarithm turns it additive. Complete.

**Theorem 12 tree factorisation (line 312–320).** The leaf-order elimination (2S, n, then ℓ, k, q, g, f,
e) is exactly `count_tree` and every message has one argument; the "read from the other end" aside
does not (R-2). The two leaf formulas match M §10.4 with the paper's 1-based subscripts.

**F(z) (Theorem 14, Corollary 4, Theorem 15).** The nesting is `nested_F`; F(1) = 976 and F(−1) = 2 are
exact integer evaluations; 10801/976 and 23/2 − 10801/976 = 0.4334 exact. Φ(−1) = 0 with five even
alphabets (A₂, A₄, A₆, A₇, A₈); the k-split (0, +2, 0) and the spin-sum parity argument are right.

### A.3 The Z3 obligations and the guards (check.py 171–337)

- **Theorem 1** (`z3_obligations`, 283–289): variables are 5 caps + 8 + 8 coordinates, all `Int`;
  hypothesis `member(X) ∧ member(Y)`, conclusion `member(J) ∧ member(M)` with J, M coordinatewise
  `If`-max/min; negation `unsat`. `z3_member` = range ∧ the seven bounds, caps free — so the result is
  over every integer cap. Encoding is the operator D4/D5 defines. The row label says "13 variables";
  there are 21 (A-2). Guards: non-vacuity with X ≠ Y and caps ≥ 3, `sat` (row 1); fidelity of
  `z3_member` against `in_range ∧ admissible` on all 6,912 box points plus 400 tuples from a wider
  range, 7,312 compared, 0 disagreements (row 4). Both run before, and `main()` refuses to report if
  either fails (line 1509). Box named in the paper: yes (§1 Theorem 1, §9).
- **Lemma 1** (292–303): φ uninterpreted with ∀u,v (u ≤ v → φ(u) ≤ φ(v)); negation of closure of
  {a ≤ φ(b)} under max/min; `unsat`. Guard: a monotone φ with two distinct admissible pairs, `sat`.
  Selftest (2) drops the axiom and gets `sat`. Faithful to Lemma 1.
- **Theorem 13, sufficient half** (306–322): lo, hi, w, caps all integer; hypothesis lo ≤ hi in range,
  the seven comparisons, lo ≤ w ≤ hi; conclusion `member(w)`; `unsat`. Faithful. Its non-vacuity is
  covered by guard 1's box (any cell as lo = hi = w) — acceptable, though no separate row says so.
- **Lemma 2** (325–335, via `prover.prove` on (3,3) and (3,3,3)): `observed(X) ∧ (X = in_R(X)) →
  closed(X)`, where `in_R` is the witness form of the staircase membership over the whole box — under
  `observed` the whole box is X's own box, so this is D7 in the own-box regime. Guards: a proper,
  non-empty fixed point exists in 3×3×3 (`sat`, row 3); `prover.in_R` against `cypher.op_order`, the
  operator under test, on 120 random subsets over three shapes, 1,352 cells, 0 disagreements (row 5).
  Boxes named in the paper: yes. MACHINE-CHECKED is claimed for exactly these four obligations and no
  other — no MACHINE-CHECKED claim in the paper lacks a row.
- **Negative control (1)** verifies the printed witness concretely (`sum_ok`), so the pair in §9 does
  not depend on the model Z3 returns. Good.

### A.4 Numbers against the check's output

The §9 table (72 rows) was diffed mechanically against the check's 72 printed rows: same labels, same
statuses, same order, same details, modulo transliteration (Lambda → Λ, Moebius → Möbius, | → ∣,
Koenig → König, -> → →, Phi → Φ). Every number in §0's table, §1–§7 and the captions was traced to a
row; the exceptions are A-4. Two rows are conditional on what they test (A-1) and six rows print
without pinning (A-3).

### A.5 Figures

md5 of every file in `figures/` equals FIGURES.tsv, and the five archival plates are byte-identical to
their named sources under `extracted/archives/` (fig1 = build8 figure-7.1, fig3 = build8 figure-8.2,
fig4/5/6 = restore-point-2-13 fig05/07/08); `method/PROOF-FIGURES.tsv` lists all five as
caption-matched. Each image was read against its caption:

- Figure 1 (fig1): e—f—g—q—k—ℓ—n with 2S at k, labelled edges. Matches Lemma 3, except the labels
  read k ≤ 2(2ℓ+1), g ≤ 2(2f+1) where the paper writes 4ℓ+2, 4f+2 (A-10).
- Figure 2 (fig3): the 18 bars, centre of mass 11.07, midpoint 11.5, skew −0.43, "more caps than
  floors". Matches Theorem 5 and its caption.
- Figure 3 (fig2, computed): 17 boxes at ranks 4–15, 9 solid and 11 dashed edges; every edge is one of
  the twenty in the check's row; weights 856…16 match Table 3. Matches.
- Figure 4 (fig4): four panels as captioned; panel (a) prints "volume = 12, count = 5 × 4 = 20", which
  is the caption's point but conflicts with D11's use of "volume" for the count (A-11). Panel (d) prints
  log 2 = 0.69 and log(11/10) = 0.095. Matches otherwise.
- Figure 5 (fig7, computed): (a) 673…24 in the paper's order; (b) seven rates from 0.98 (g ≤ 4f+2) to
  0.70 (g ≤ q), lines at 0.2835 and 0.2013, lift 1.4081. Matches Table 2 and Proposition 1.
- Figure 6 (fig6): bars and reversed dashed line, "forwards 1, 5, 15, 34 … backwards 1, 4, 10, 21",
  mean 11.07, midpoint 11.5. Matches Corollary 5.
- Figure 7 (fig5): path n→ℓ→k→q→g→f→e with 2S pendant, "g ≤ 2(2f+1) ← the Pauli principle", and the
  leaf annotation "(1−z⁸ᵏ⁺¹)/(1−z₈)" with the 8 rendered as a superscript. The arrows put g before f
  and e, which is not the nesting Theorem 14 displays (A-9).
- Figure 8 (fig8, computed): (a) 370 cells, one at 24,585, log scale; (b) histogram with a bar at 100 %
  and one near 59 %, median 0.24 %. Matches Theorem 18's remark.

### A.6 Lint, render, typography

Lint: 0 hits. Render: 26 pages, 0.75 MB. Subscripts and superscripts are Unicode throughout the
running text (xᵢ, φ̂ᵢⱼ, eᵢ, j⁻, 2ᵐ, ℓ¹, μℤ, z³ … z²⁰); no underscore, caret, asterisk or backslash
leaks into prose; the ∣ bars in table cells hold; the §9 table wraps without clipping; all eight
figures appear, legible at print size. Defects found on the page: the Theorem 14 display (A-8), the
Figure 7 plate's superscript (A-9), and four page-break faults (A-12).

### A.7 Part A findings

- **A-1 (MAJOR)** — check.py 464–475 `covers_of()` finds a cell's lower covers by testing y − eᵢ ∈ Λ,
  i.e. it *assumes* every cover is a unit step. The rows "Theorem 4, Λ is graded" (every cover raises
  rank by 1), "Theorem 6, seventeen irreducibles" (down/up counts) and "Corollary 3, maximal chains"
  (paths over `down`) are therefore conditional on the grading they are supposed to test; the first is
  a tautology as coded. The theorem is proved and the audit's order-derived recomputation gives 3,749
  covers, all unit steps, 17 join- and 17 meet-irreducibles — so nothing printed is wrong, but a check
  that does not test what the sentence claims is a finding. Resolve: derive covers from the order (for
  x < y, no z with x < z < y; a bitset over the 976 cells makes this fast), build `down`/`up` from
  that, and let the graded row report that every such cover is a unit step.
- **A-2 (MINOR)** — check.py 289, PAPER.md 479: "all 13 variables INTEGER (5 caps, 2 cells)". The
  obligation has 21 integer variables (5 caps + 2 × 8 coordinates); §1 line 85 says "all sixteen cell
  coordinates". Resolve: relabel "all 21 variables INTEGER (5 caps, 2 cells of 8)" in check.py and
  re-quote in §9.
- **A-3 (MINOR)** — Rows that print values and assert nothing (`ok=True`): "Table 3, the seventeen
  letters" (607), "Theorem 8, the twenty implications written out" (651), "Theorem 7, the bit
  accounting" (713), "Theorem 11, the log-distorted chain" (791), "Proposition 1, the void-free
  fraction" (899: 134,871, 0.2835, 0.6995, 0.9806, 0.2013, 1.4081 all unpinned), "Theorem 18, the
  covers by cell" (median 59 and 14,492 unpinned). A drift in any of those would leave the run green.
  Resolve: assert the printed values in each row.
- **A-4 (MINOR)** — Numbers in the paper with no row: 8,064 (lines 123, 547; the check enumerates the
  extended box but never prints its size); 87.7 % and 1.6 % (line 211); "1.5 × 10⁸ and 9.3 × 10⁸"
  (line 553), which also count the same kind of family two ways — C(976,3) ≈ 1.5 × 10⁸ unordered
  triples for distributivity against 976³ ≈ 9.3 × 10⁸ ordered triples for the triangle. Resolve: print
  8,064 in the Table 2 row, print the two percentages in the Table 3 row, and give both family sizes
  as ordered triples (976³ = 929,714,176) or both as unordered.
- **A-5 (MINOR)** — Row "Theorem 17, covering is generating" (1219–1233): none of the 80 random subsets
  of size 4–10 is a cover (recomputed: 0 of 80), so the sample confirms only "not a cover ⟹ does not
  close". The positive direction is the separate row "Theorem 18, the minimum covers close" (40 covers).
  Resolve: print "k of 80 are covers" in the row and say in §9 (line 553) that the two SAMPLED rows
  together test both directions.
- **A-6 (MINOR)** — Corollary 7 (line 442) claims a full transfer q = k for each k ∈ {1, 2, 3}; the row
  (1335–1351) tests only "some cell with q = k". The per-k statement is proved and holds (recomputed:
  0 covers lack each of q = k = 1, 2, 3). Resolve: three properties in `props`, one per k.
- **A-7 (MINOR)** — Theorem 2's proof (line 103): "built twice, once by the construction of D4 and once
  by sieving all 6,912 points of the box against the seven bounds" — D4 *is* the sieve. The other
  construction is the nested enumeration along the tree (the order of Theorem 14). Resolve: "built by
  nested enumeration in the order of Theorem 14 and by sieving the box".
- **A-8 (MINOR, typography)** — Theorem 14's display (lines 346–350; PDF p14) mixes Unicode
  superscripts (zⁿ, zˡ, zᵏ, z²ˢ, zᵉ, zᶠ, zᵍ) with the words "z to the q", and the fenced block wraps
  mid-sum on the page. Resolve: inside the fenced block write every power as z^n, z^ℓ, z^k, z^{2S},
  z^q, z^e, z^f, z^g (a code block renders ^ literally, which §9 of the spec permits) and break the
  block one sum per line.
- **A-9 (MINOR, figure)** — Figure 7's plate prints "(1−z⁸ᵏ⁺¹)/(1−z₈)" with the subscript 8 raised,
  and its arrows n→ℓ→k→q→g→f→e put g before f and e, whereas the caption calls it "the nesting order
  of the expression" and Theorem 14 nests e, f before g. Resolve: regenerate the figure in figures.py
  (arrows in Theorem 14's order, z₈^{k+1} set correctly), or reword the caption to "the constraint
  graph as a path with one pendant; arrows point from a coordinate to the one that bounds it" and drop
  "nesting order".
- **A-10 (MINOR, figure)** — Figures 1 and 7 label the Pauli bounds 2(2ℓ+1) and 2(2f+1); D2 and Table
  1 write 4ℓ+2 and 4f+2. Resolve: one clause in each caption ("2(2ℓ+1) = 4ℓ+2"), or regenerate.
- **A-11 (MINOR, figure)** — Figure 4 (a) prints "volume = 12, count = 20" and the caption says "d
  counts its points, not its volume", but D11 (line 298) defines vol(lo,hi) := ∏(hiᵢ − loᵢ + 1), which
  is the point count. Resolve: rename D11's quantity (∣[lo,hi]∣ or "size") — it is not used afterwards
  — or add to the caption that the plate's "volume" is ∏∣Δᵢ∣.
- **A-12 (MINOR, typography in the PDF)** — Table 1's bold heading sits alone at the foot of p4 with
  its table on p5; Figure 1's image is on p5 and its caption on p6; Figure 3's image is on p9 and its
  caption on p10; the §9 row "Theorem 16, the Möbius function" is split across p23–p24. Resolve: give
  each image its caption as alt text so pandoc emits a `<figure>` (the template already keeps figures
  whole), or add `img + p { page-break-before: avoid }`; add `tr { page-break-inside: avoid }` and
  `p strong:only-child { page-break-after: avoid }` — these are template changes, to be raised with
  the render owner, but the defect is on this paper's page.
- **A-13 (MINOR)** — Figure files are numbered by an earlier order (fig2 = Figure 3, fig3 = Figure 2,
  fig5 = Figure 7, fig6 = Figure 6, fig7 = Figure 5). Not a defect on the page; a maintenance hazard.
  Resolve: rename to match, or add a "figure" column to FIGURES.tsv.
- **A-14 (MINOR)** — Line 23, the run-in heading "Measured, at the stated caps." uses the spec's status
  word MEASURED in a sense the paper never declares (its table says EXHAUSTIVE). Resolve: "Counted, at
  the stated caps."

---

## Part B — reader audits

### B.1 A lattice theorist who has not seen this material

I can follow the paper without the books; every object is defined before use, and the definitions are
the standard ones. The mathematics is sound — I checked each proof, and the two rewritten ones
(Theorem 4's grading, Theorem 6's converse) are now correct. My findings are about statements that are
false as written, a theorem contradicted by its own proof's aside, and the paper's account of which
results are cap-free.

- **R-1 (MAJOR)** line 155: "Λ's rank meets the equality, which is the graded signature of
  distributivity." False. Rank modularity is the graded signature of *modularity* (Birkhoff 1940: a
  finite lattice is modular iff it is graded and rank(x ∨ y) + rank(x ∧ y) = rank x + rank y); the
  diamond M₃ satisfies it and is not distributive. The paper's Theorem 3 gives distributivity; this
  sentence would let a reader believe the O(N²) test establishes it. Change: "…which is the graded
  signature of modularity (Birkhoff 1940); distributivity is the stronger property, Theorem 3's, and a
  failure of the pair condition refutes it in O(N²) where the triple law costs O(N³) — a pass does not
  establish it."
- **R-2 (MAJOR)** lines 306–320: Theorem 12 states that "every intermediate quantity is a function of a
  single coordinate", and its proof then offers "Read from the other end, g may instead be summed last
  of the three coordinates q, f, g it touches, as #{g} = max(0, min(hi₇, q, 4f + 2) − lo₇ + 1)" — a
  message in two live coordinates, contradicting the statement; and g there is summed *first* of the
  three, not last. The count is still right (no term is subtracted), but the theorem as stated is
  about message arity. Change: delete the sentence, or replace it with "if g is eliminated while q and
  f are both live, the message depends on both; the single-argument property belongs to the leaf order
  above, which is the one the check runs."
- **R-3 (MAJOR)** line 39: "the written proofs of Theorems 3, 4, 6, 10, 11, 12, 13, 15, 16 and 17 and of
  Corollaries 6, 7 and 8 use no cap." Theorem 15 is a computation at the caps (which alphabets are
  even, the k-split); Theorem 17 (⟸) invokes ℛ(Λ) = Λ, which is Theorem 2 at the caps; Corollary 7's
  proof names the cell (1,0,1,0,2,1,0,0) and the slot g = 3; Corollary 8 rests on Theorem 18's count.
  Change: "…Theorems 3, 4, 6 (the form and the closed count), 10, 11, 12, 13 and 16 and Corollary 6 use
  no cap; Theorem 17 holds at any setting where the closure defect is 0; Theorem 15 and Corollaries 7
  and 8 are at the stated caps."
- **R-4 (MINOR)** line 187: "j(i, v) covers only j(i, v) − eᵢ" is not derived. Supply: by Theorem 4 the
  unique lower cover of m = j(i, v) is m − eᵢ′ for some i′; if i′ ≠ i then (m − eᵢ′)ᵢ = v, so m − eᵢ′
  ∈ Sᵥ lies strictly below m, against minimality; hence i′ = i.
- **R-5 (MINOR)** lines 173 and 398: J(Λ) is the set of join-irreducibles, J(Q) the lattice of down-sets
  of Q. Use 𝒪(Q) (or 𝒟(Q)) for down-sets.
- **R-6 (MINOR)** line 410: "decided by eight comparisons of coordinates and one parity" — Corollary 6
  needs the seven containment comparisons of Theorem 13 and the eight unit tests yᵢ − xᵢ ≤ 1: fifteen.
  Change the count.
- **R-7 (MINOR)** line 376: "which is the statement Theorem 9 makes" — Theorem 9 shows one candidate
  anti-automorphism fails; Corollary 5 excludes every rank-reversing automorphism. Change: "of which
  Theorem 9's reflection is one instance".
- **R-8 (MINOR)** lines 71–75 (D3): A₄, A₇, A₈ = {0, …, kₘₐₓ} is nowhere stated; at the five further
  settings a reader cannot reconstruct the box. Add the sentence to D3.
- **R-9 (MINOR)** line 332: the Chebyshev remark asserts what it does not prove — "holding with
  probability 1 at zero width" is not true of hiᵢ ≤ φ(loⱼ) in general (it depends on the width in i
  too), and the comparisons are functions of several widths. Either mark it "a heuristic reading, not
  measured here", or delete it; if it stays, cite Hardy, Littlewood and Pólya (1934) for the sum
  inequality.
- **R-10 (MINOR)** lines 306–310: Theorem 12 is stated as a procedure ("is computed by eliminating…").
  State the object: display the nested sum with the two closed leaves (the form `count_tree` computes)
  and prove that identity.
- **R-11 (MINOR)** line 452: "the lower bound of 5 says at most two of those seven are slack" — the
  minimum is exact; no cell is slack. Delete, or say "the disjoint-witness bound certifies 5 and the
  search closes the gap to 7".
- **R-12 (MINOR)** line 272: "(1 of D10) = (2)" is opaque. Write "so d as defined in D10 equals (2)".
- **R-13 (MINOR)** line 163: the Sperner property is used before it is defined (it is named only at the
  end of the proof); and "log-concave, no internal zero ⟹ unimodal" is elementary — the standard
  citation is Stanley (1989), not EC1. Define "Sperner" in D8 or in the statement of Theorem 5 and cite
  Stanley 1989.
- **R-14 (MINOR)** line 402: the fact used is the corollary of the crosscut theorem ("if 1̂ is not a join
  of atoms, μ(0̂, 1̂) = 0" — Rota 1964, the corollary to Theorem 3; Stanley 2012, Corollary 3.9.5), and
  the closed form of Theorem 16 itself is a textbook statement about finite distributive lattices
  (Stanley 2012, §3.9). Cite both precisely and say the paper verifies the instance.

### B.2 An atomic physicist

I read the one physics paragraph and D1–D2 as a spectroscopist would, then asked what a cell is. The
seven inequalities are correctly attributed to node counting, Pauli capacity, conservation and spin
addition, and the Pauli principle enters exactly at k ≤ 4ℓ+2 and g ≤ 4f+2 — that part is right. The
paper carries no spectral data and makes no spectral claim, which is honest. Three things are
overstated or under-specified, and one of them is structural.

- **R-15 (MAJOR)** title, lines 1 and 11: "One-Electron Transitions" / "A one-electron transition … is
  specified by … the number of electrons moved". q ranges over 0–3: 481 of the 976 cells move two or
  three electrons, and the q = 0 cells move none. If "one-electron" means the hydrogenic one-electron
  labels (n, ℓ), the title and abstract must say so; otherwise retitle ("The Lattice of Subshell
  Transitions", or "of Electron-Transfer Cells") — or restrict q ≤ 1 and recompute, which changes
  every count.
- **R-16 (MAJOR)** lines 57, 69, 19: "The total spin of k equivalent electrons cannot exceed k/2, so
  2S is bounded by k" is true but is not the spin rule. For k equivalent electrons 2S ≡ k (mod 2), and
  by particle–hole symmetry 2S ≤ 4ℓ+2 − k. At the stated caps 413 cells have 2S of the wrong parity
  (s² with 2S = 1, p¹ with 2S = 0 or 2, …) and 180 exceed the particle–hole maximum (s² with 2S = 2,
  p³ with 2S = 2 is fine but s² with 2S = 1 or 2 is not); 503 cells in all carry a spin label no
  k-electron configuration has. The book itself calls 2S ≤ k an envelope. The reason for the envelope
  is the paper's own: the true rule is a congruence, not of the form xᵢ ≤ φ(xⱼ), and would break
  Theorem 1 — so it *was* chosen for the shape, and §0's "Nothing in the construction is chosen for
  convenience: every bound comes from one of four physical facts" overstates. Change: in §1 say that
  2S ≤ k is the monotone envelope of the spin rule, that parity and the particle–hole bound are
  deliberately not imposed because a congruence is not a monotone bound, and print the count of
  envelope-only cells (503 at these caps; add a row to check.py); soften §0 to "every bound is the
  monotone envelope of one of four physical facts".
- **R-17 (MAJOR)** lines 57, 63, 111–114: what g is. D1 says the target "ends holding g"; Table 1 says
  g ≤ q means "no more may arrive than left". Together these say the target was empty before the move
  and that in the 515 cells with g < q, q − g electrons went nowhere — that is ionisation, not a
  transition between configurations. And 200 cells have (e, f) = (n, ℓ), a "transition" into the
  subshell the electrons left. If g is the number *deposited*, say so and drop "final occupancy"; if g
  is the final occupancy, the target's initial occupancy is a ninth coordinate the index does not carry
  and the Pauli bound on the target is on initial + arriving. State the model in one sentence and say
  what a cell with g < q or with source = target represents.
- **R-18 (MINOR)** lines 57, 63: "the multiplicity label 2S" — the multiplicity is 2S + 1. Write "the
  spin label 2S (multiplicity 2S + 1)".
- **R-19 (MINOR)** line 57: "the radial equation has a solution only for ℓ ≤ n − 1 (Bohr 1913)" — Bohr
  1913 has no ℓ and no radial equation; the condition is Sommerfeld's k ≤ n (1916) and, as stated, is
  Schrödinger (1926). Cite Schrödinger, E. (1926). Quantisierung als Eigenwertproblem (Erste
  Mitteilung). Annalen der Physik 79, 361–376, and keep Bohr for n.
- **R-20 (MINOR)** line 57: S ≤ k/2 is the addition of k spin-½ angular momenta, not Hund's rule (Hund
  1925 says which term lies lowest). Cite Condon and Shortley alone, or say "by addition of angular
  momenta".
- **R-21 (MINOR)** abstract and §1: the index carries no selection rule — Δℓ = ±1 would remove the
  s → s and p → p cells that Corollary 7 finds in every seed, and no energy, parity or intensity
  enters. Say once that "transition" means a change of configuration labels, not a radiative line,
  and that the paper tests nothing against measured spectra.

### B.3 A journal referee

The verification record is honest: 72 rows reproduce, the table quotes the check's output exactly
(transliterated), the guards run first, the negative controls refute, and the one exhaustive search
whose completeness is not machine-certified is argued in the text and reproduces under an independent
implementation. The abstract promises what the body delivers. What a referee would send back:

- **R-22 (MAJOR)** lines 95, 462 (and §0's pointer to §9): "the companion paper on the closure law" is
  relied on four times — for ℛ being a closure operator, for the converse of Lemma 2, for the box-seed
  law — and has no entry in the References, no title, no status. A referee cannot check a citation to
  an unnamed paper. Add the reference (author, title, year, "in preparation" if so), or remove the
  dependence: Theorem 17 uses only D7, and Lemma 2's converse is not needed anywhere in this paper.
- **R-23 (MINOR)** §0 (lines 17–37): the headline list mixes textbook consequences of "sublattice of a
  product of chains" — distributive, rank-modular, Birkhoff's representation, dimension = width,
  maximal chains = linear extensions, the antichain form of μ, log d an ℓ¹ metric — with the paper's
  own results: the exhaustive seed enumeration and the one-common-cell / no-unique-witness finding, the
  localisation of F(−1) = 2 on k = 2, the void lift, the 7-against-17 comparison of the two closures,
  and the tree factorisation verified on every sub-box. §8 says so in passing. Say in §0, in one
  sentence, which results are inherited and which are new, so the contribution is not overstated.
- **R-24 (MINOR)** references missing, with full author lists and years:
  - Harary, F. and Schwenk, A. J. (1973). The number of caterpillars. *Discrete Mathematics* 6, 359–365
    — "caterpillar" is used throughout with no citation.
  - Schrödinger, E. (1926). Quantisierung als Eigenwertproblem (Erste Mitteilung). *Annalen der Physik*
    79, 361–376 (R-19).
  - Stanley, R. P. (1989). Log-concave and unimodal sequences in algebra, combinatorics, and geometry.
    *Annals of the New York Academy of Sciences* 576, 500–535 (line 163).
  - Baker, K. A. and Pixley, A. F. (1975). Polynomial interpolation and the Chinese remainder theorem
    for algebraic systems. *Mathematische Zeitschrift* 143, 165–174; and Bergman, G. M. (1977). On the
    existence of subalgebras of direct products with prescribed d-fold projections. *Algebra
    Universalis* 7, 341–356 — a sublattice of a product of chains is determined by its two-fold
    projections, which is the fact behind D7, Lemma 2 and Theorem 17 (⟸).
  - Davey, B. A. and Priestley, H. A. (2002). *Introduction to Lattices and Order*, 2nd ed. Cambridge
    University Press — the standard reference for D8, Birkhoff's representation, and "a sublattice of
    a distributive lattice is distributive", now cited to Birkhoff 1940 without a page.
  - Trotter, W. T. (1992). *Combinatorics and Partially Ordered Sets: Dimension Theory*. Johns Hopkins
    University Press — for Corollary 2.
  - Proctor, R. A., Saks, M. E. and Sturtevant, D. G. (1980). Product partial orders with the Sperner
    property. *Discrete Mathematics* 30, 173–180; and Stanley, R. P. (1980). Weyl groups, the hard
    Lefschetz theorem, and the Sperner property. *SIAM Journal on Algebraic and Discrete Methods* 1,
    168–184 — the product of chains is Sperner (indeed Peck); a sublattice need not inherit it, which is
    the reason Theorem 5 has to be computed and is worth one sentence.
  - Garey, M. R. and Johnson, D. S. (1979). *Computers and Intractability*. W. H. Freeman — optional,
    beside Karp for set cover.
  - Hardy, G. H., Littlewood, J. E. and Pólya, G. (1934). *Inequalities*. Cambridge University Press —
    only if the Chebyshev sentence of R-9 stays.
- **R-25 (MINOR)** line 468: "Every number printed above is recomputed by the accompanying checks" —
  the exceptions are A-4; and "under the check's own label" (line 470) should add "transliterated to
  Unicode", since Λ, ∣, Möbius and König are not what the check prints.
- **R-26 (MINOR)** line 3, the thesis: "a minimum generating set of seven of its own cells, every one of
  which carries a null transition, a full transfer and each of the three channels" — "every one of
  which" grammatically means every one of the seven cells, which is false; it is every minimum
  generating set. Change: "…seven of its own cells, every such set containing a null transition, a full
  transfer and each of the three channels s → p, p → s and p → p."
- **R-27 (MINOR)** lines 39, 432: "the general problem is NP-complete (Karp 1972)" — minimum set cover
  is an optimisation problem, NP-hard; Karp's "set covering" is the decision version. Write "NP-hard
  (its decision version is NP-complete, Karp 1972)".
- **R-28 (MINOR)** lines 217, 256: "occupancy" is used for k and g (electron occupancy), for d ("the
  occupancy measure") and for the fraction 0.7446 % ("an occupancy of the space the cells are written
  in"). Keep the physical sense and rename the other two (the source calls d "the interval measure";
  the bit fraction is a density).

---

## Part C — the record

| id | severity | where | finding (short) | disposition |
|---|---|---|---|---|
| A-1 | MAJOR | check.py 464–475; rows Thm 4 graded, Thm 6, Cor 3 | covers found by unit steps, so the grading row cannot test the grading | FIXED — `covers_of()` derives covers from the order alone (x < y, no cell between, by bitset); the graded row asserts 3,749 covers, every one a unit step and rank +1; Theorem 6 and Corollary 3 use those cover sets; the further-caps row says its unit-step covers are licensed by the proved Theorem 4 |
| A-2 | MINOR | check.py 289; PAPER.md 479 | "13 variables" — the obligation has 21 | FIXED — label and §9 read "all 21 variables INTEGER (5 caps, 2 cells of 8)" |
| A-3 | MINOR | check.py 607, 651, 713, 791, 899, 1386 | six rows print values and pin nothing | FIXED — all six rows pin their values (Table 3 ranks/weights, the twenty implications as a set, 17 / 9.9307 / 7.0693 / 0.7446, 0.6931 / 0.0953, 134,871 / 0.2835 / 0.6995 / 0.9806 / 0.2013 / 1.4081, median 59 and 14,492); Table 2's marginals pinned too |
| A-4 | MINOR | PAPER.md 123, 211, 547, 553 | 8,064; 87.7 % / 1.6 %; 1.5 × 10⁸ vs 9.3 × 10⁸ have no row and count two ways | FIXED — and the row caught an error: the box extended to k = 0 has 9,216 points, not the draft's 8,064; the paper prints 9,216 (SOURCES.md records it); 87.7 % / 1.6 % printed by the Table 3 row; both SAMPLED rows name the family as 976³ = 929,714,176 ordered triples |
| A-5 | MINOR | check.py 1219–1233; PAPER.md 426, 553 | the 80-subset sample contains no cover; tests one direction only | FIXED — the row prints "0 of them are covers"; Theorem 17's clause and §9 say the two SAMPLED rows test the two directions between them |
| A-6 | MINOR | check.py 1335–1351; PAPER.md 442 | Corollary 7's per-k claim checked only as "some k" | FIXED — three properties q = k = 1, 2, 3 in the row; the statement's status names them |
| A-7 | MINOR | PAPER.md 103 | "built twice, once by D4 and once by sieving" — D4 is the sieve | FIXED — "by nested enumeration in the order of Theorem 14 and by sieving the box" (the construction imported is that nested enumeration) |
| A-8 | MINOR | PAPER.md 346–350; PDF p14 | Theorem 14 display: "z to the q", mixed superscripts, wrapped block | FIXED — a display block, one sum per line, Unicode superscripts throughout; the one letter Unicode lacks (q) is an HTML superscript, not a caret, since the rendered page must carry no caret; verified in the PDF text |
| A-9 | MINOR | figures/fig5-caterpillar.png; PAPER.md 386 | plate's superscript garbled; arrow order is not Theorem 14's nesting | FIXED — Figure 7 is now computed by figures.py from the seven bounds: arrows in Theorem 14's nesting order from a coordinate to one whose range it bounds, leaf label (1 − zᵏ⁺¹)/(1 − z) set correctly; caption rewritten |
| A-10 | MINOR | figures/fig1, fig5; PAPER.md 135, 386 | plates label 2(2ℓ+1), text 4ℓ+2 | FIXED — Figure 1's caption says the plate's 2(2ℓ + 1), 2(2f + 1) are 4ℓ + 2, 4f + 2; Figure 7 regenerated with 4ℓ + 2 and 4f + 2 |
| A-11 | MINOR | figures/fig4; PAPER.md 290, 298 | "volume" means the count in D11 and the continuous volume on the plate | FIXED — D11 defines the size ∣[lo, hi]∣, the number of points; Figure 4's caption notes the plate's own title |
| A-12 | MINOR | PDF p4–6, p9–10, p23–24 | Table 1 heading orphaned; Figures 1 and 3 split from captions; a §9 row split | FIXED in the paper, in the §9 form (empty alt, caption paragraph **Figure n.** directly under the image; table headings as bold paragraphs before their tables) and without touching the template: Table 1 now follows D2, Figure 1 precedes Lemma 3 and Figure 4 precedes Theorem 11, so on the re-render every figure sits with its caption on one page (pp. 6, 8, 11, 13, 15, 17, 17, 21), every table heading with its table (pp. 4, 6, 9), and no §9 row is split (the template's tr rule holds). A first repair used pandoc figures with the caption as alt text and pandoc table captions; the coordinator ruled that non-conformant to §9 and lost on the site, and it was reverted |
| A-13 | MINOR | figures/, FIGURES.tsv | file numbers ≠ figure numbers | FIXED — files renamed so figN is Figure N (fig2 rank sequence, fig3 generating poset, fig4 interval measure, fig5 void, fig7 caterpillar); figures.py and FIGURES.tsv follow |
| A-14 | MINOR | PAPER.md 23 | "Measured" used as a run-in heading for EXHAUSTIVE counts | FIXED — "Counted, at the stated caps." |
| R-1 | MAJOR | PAPER.md 155 | rank modularity called "the graded signature of distributivity" — it is modularity's | FIXED — the sentence now names modularity (Birkhoff 1940; Davey and Priestley 2002, CITED, with a CITED row), says distributivity is Theorem 3's, and that the pair test can refute but not establish it, with M₃ as the witness |
| R-2 | MAJOR | PAPER.md 306–320 | Theorem 12's "single coordinate" statement contradicted by the g-first aside | FIXED — the aside is replaced by the sentence that the single-argument property belongs to a leaf order and that g eliminated with q and f live would carry two arguments; the theorem is stated as the nested formula the check computes |
| R-3 | MAJOR | PAPER.md 39 | cap-free list wrongly includes Theorem 15, 17, Corollaries 7, 8 | FIXED — §0 lists Theorems 3, 4, 6 (form and closed count), 10, 11, 12, 13, 16 and Corollary 6 as cap-free; Theorem 17 at any setting with E = 0 (stated in the theorem too); Theorem 15 and Corollaries 7, 8 at the stated caps |
| R-4 | MINOR | PAPER.md 187 | injectivity step in Theorem 6 needs one line | FIXED — the line is supplied in the proof |
| R-5 | MINOR | PAPER.md 173, 398 | J(Λ) vs J(Q) notation clash | FIXED — 𝒪(Q) for down-sets; J(Λ) stays for the join-irreducibles |
| R-6 | MINOR | PAPER.md 410 | "eight comparisons" — fifteen | FIXED — fifteen: the seven of Theorem 13 and the eight unit tests |
| R-7 | MINOR | PAPER.md 376 | Corollary 5 is stronger than Theorem 9, not "the statement Theorem 9 makes" | FIXED — "of which Theorem 9's reflection is one instance" |
| R-8 | MINOR | PAPER.md 71–75 | A₄, A₇, A₈ = {0..kₘₐₓ} not stated | FIXED — D3 states the alphabets at a general setting, q, g, 2S taking kₘₐₓ |
| R-9 | MINOR | PAPER.md 332 | Chebyshev remark asserts what it does not prove | FIXED — marked "a heuristic reading, not measured here", the probability-1 and Chebyshev claims removed; Hardy–Littlewood–Pólya therefore not cited |
| R-10 | MINOR | PAPER.md 306–310 | Theorem 12 stated as a procedure, not a formula | FIXED — Theorem 12 displays the nested sum with the two closed leaves, and the proof derives it |
| R-11 | MINOR | PAPER.md 452 | "at most two of those seven are slack" is meaningless once the minimum is exact | FIXED — "the disjoint-witness bound certifies 5 and the search closes the gap to 7" |
| R-12 | MINOR | PAPER.md 272 | "(1 of D10) = (2)" | FIXED |
| R-13 | MINOR | PAPER.md 163 | Sperner property used before defined; cite Stanley 1989 for unimodality | FIXED — Sperner defined in D8 and stated in Theorem 5; Stanley 1989 cited, with a CITED row; the product-of-chains remark (Proctor–Saks–Sturtevant, Stanley 1980) says why it is computed |
| R-14 | MINOR | PAPER.md 402 | cite the crosscut corollary precisely; note the closed form is textbook | FIXED — the corollary of the crosscut theorem cited to Rota 1964 and Stanley 2012 Corollary 3.9.5; the closed form noted as textbook (Stanley 2012 §3.9) with the instance verified |
| R-15 | MAJOR | title; PAPER.md 1, 11 | "one-electron" while 481 cells move two or three electrons | FIXED — retitled "The Lattice of Subshell Transitions" (old title recorded in SOURCES.md and below, for the author to settle); abstract, thesis and §0 follow; §0 prints 165 / 330 / 345 / 136 cells by q and 481 moving two or three, from the new row "D1, electrons moved" |
| R-16 | MAJOR | PAPER.md 19, 57, 69 | 2S ≤ k is an envelope (503 unphysical spin labels); "nothing chosen for convenience" overstates | FIXED — §1 states the rule 2S ≡ k (mod 2), 2S ≤ min(k, 4ℓ + 2 − k), says why neither part is a monotone bound in one coordinate, and prints 503 (413 parity, 180 particle–hole, 90 both; 473 physical = 48.5 %) from the new row "Table 1, the spin envelope"; Table 1 has a kind column, exact for six and envelope for 2S ≤ k; §0's "nothing chosen for convenience" is replaced by the exact/envelope statement |
| R-17 | MAJOR | PAPER.md 57, 63, 111–114 | semantics of g: 515 cells lose electrons, 200 have source = target; state the model | FIXED — the physics paragraph and D1 state the model from the source's own definitions: g is the number placed, the target is taken to begin empty and the index has no coordinate for prior occupancy, so the Pauli bound reads g as the occupancy after the move; g < q (515) is removed-and-not-placed with no second destination carried; q = 0 (165) is a null transition; source = target (200) is admitted because no bound compares source and target labels; counts from the new row "D1, the model of a cell" |
| R-18 | MINOR | PAPER.md 57, 63 | 2S called "multiplicity"; multiplicity is 2S + 1 | FIXED — "spin label 2S (multiplicity 2S + 1)" |
| R-19 | MINOR | PAPER.md 57 | ℓ ≤ n − 1 cited to Bohr 1913; cite Schrödinger 1926 | FIXED — Schrödinger 1926 for ℓ ≤ n − 1, Bohr 1913 kept for n; reference added |
| R-20 | MINOR | PAPER.md 57 | S ≤ k/2 is spin addition, not Hund's rule | FIXED — addition of angular momenta, Condon and Shortley; Hund 1925 removed from the references as uncited |
| R-21 | MINOR | abstract, §1 | say that no selection rule or spectral datum enters | FIXED — in the abstract and at the end of the physics paragraph, with Δℓ = ±1 named |
| R-22 | MAJOR | PAPER.md 95, 462 | "the companion paper" cited four times, no reference entry | FIXED — References: Lach, M. (2026). The Closure Law of a Finite Index. This collection; cited (Lach 2026) at D7 and §8, the only two places the companion is named |
| R-23 | MINOR | PAPER.md 17–37 | say which headline results are inherited and which are new | FIXED — one paragraph in §0 separates the inherited results from the new ones |
| R-24 | MINOR | References | missing: Harary–Schwenk 1973, Schrödinger 1926, Stanley 1989, Baker–Pixley 1975, Bergman 1977, Davey–Priestley 2002, Trotter 1992, Proctor–Saks–Sturtevant 1980, Stanley 1980 (Garey–Johnson 1979, HLP 1934 optional) | FIXED for the nine named (Harary–Schwenk, Schrödinger, Stanley 1989, Baker–Pixley, Bergman, Davey–Priestley, Trotter, Proctor–Saks–Sturtevant, Stanley 1980), each cited where used; the two optional ones DECLINED — Karp suffices for set cover and the Chebyshev sentence is gone (R-9) |
| R-25 | MINOR | PAPER.md 468, 470 | "every number recomputed" has exceptions (A-4); "check's own label" is transliterated | FIXED — every printed number now has a row (A-4), so the sentence stands; the transliteration is stated with its list |
| R-26 | MINOR | PAPER.md 3 | thesis: "every one of which" attaches to the cells, not the sets | FIXED — "every such set containing …" |
| R-27 | MINOR | PAPER.md 39, 432 | minimum set cover is NP-hard; the decision version is NP-complete | FIXED — NP-hard, decision version NP-complete, in §0, Theorem 18 and the CITED row |
| R-28 | MINOR | PAPER.md 217, 256 | "occupancy" carries three meanings | FIXED — "interval metric / interval measure" (the source's own name) for d, "density" for the bit fraction; occupancy is now only the electron count |

Totals: 0 BLOCKING, 8 MAJOR (A-1, R-1, R-2, R-3, R-15, R-16, R-17, R-22), 34 MINOR; 42 findings.

---

## Repair record (2026-09-24, the repairing drafter)

**What was run.** After the repair, with `method/bin` first on PATH (Python 3.12.3, Z3 5.1.0):
`python3 check.py` — **77 rows, 0 failures, 66 s** (5 GUARD, 5 MACHINE-CHECKED, 54 EXHAUSTIVE, 4 SAMPLED,
9 CITED); `python3 check.py --selftest` — **83 rows, 0 failures, 65 s**, all six negative controls refuted.
`python3 papers/method/lint.py papers/method/02-lambda` — 0 hits. `python3 papers/method/render.py
papers/method/02-lambda` — 29 pages, 0.77 MB. Every page was rasterised (pypdfium2) and read; a pypdf text
extraction of the PDF contains **0 underscores, 0 carets, 0 backslashes and 0 asterisks**.

**Dispositions.** 42 findings: 8 MAJOR, all FIXED; 34 MINOR, all FIXED, R-24 declining only its two
optional references (Garey–Johnson 1979, Hardy–Littlewood–Pólya 1934). Nothing DECLINED outright. No
finding was deleted or rewritten; the column above is the only addition to Parts A–C.

**The title.** "The Lattice of One-Electron Transitions" → **"The Lattice of Subshell Transitions"**, because
481 of the 976 cells move two or three electrons (R-15) and the cells are transfers between subshells with
q from 0 to 3. The old title is recorded here and in SOURCES.md for the author; the retitle is his to
settle.

**check.py gained and never lost.** Three rows (D1 electrons moved; D1 the model of a cell; Table 1 the
spin envelope), two CITED rows, order-derived covers with a unit-step assertion, pins on six previously
unasserted rows plus Table 2, per-k properties for Corollary 7, printed family sizes for the SAMPLED rows,
and the cover count in the Theorem 17 sample. One number changed on the page as a result: the box extended
to k = 0 has **9,216** points, not 8,064 (A-4); the draft's figure reproduced from nothing.

**What the physicist's readings resolved to.** R-16: the spin bound is declared an envelope, the exact rule
is stated, the reason it is not imposed is the shape (a congruence is not monotone; the particle–hole
ceiling has two parents), and the envelope's admission is counted — 503 of 976, with the split — from a
check line, with the main volume's own 48.5 % reproduced as 473/976. R-17: the model of a cell is stated
once, from the source's own reading (g is the number placed; the target begins empty; no coordinate for
prior occupancy), and the three kinds of cell the reader asked about are named with their counts.

**Typography.** Every figure is in PAPER-SPEC.md §9's form — `![](figures/…)` with empty alt text and a
caption paragraph beginning **Figure n.** directly under it — and every table heading is a bold paragraph
before its table; an interim repair that carried captions as pandoc alt text and table captions was
reverted on the coordinator's ruling (the site's image handler drops alt text, so a caption there is lost).
Splits at page feet were removed by placement instead: Table 1 follows D2, Figure 1 precedes Lemma 3,
Figure 4 precedes Theorem 11. On the final render (29 pages) every figure sits with its caption on one
page, no caption or table heading is orphaned, no §9 row is split, and the pypdf text has 0 underscores,
0 carets, 0 backslashes. The one superscript Unicode lacks (z to the q in Theorem 14) is an HTML
superscript inside a display block. The template `paper.html` was not edited.

**Unresolved, for the author.** (1) Whether "The Lattice of Subshell Transitions" is the title to keep.
(2) The 200 cells with source = target and the 515 with g < q are carried as cells of the index, as the
source carries them; the paper says the index does not decide which cells are physical transitions, and
does not restrict the index. (3) The figure placements that keep each caption with its image (Figure 1 before Lemma 3, Figure 4
before Theorem 11) hold for this render; a template change of the kind A-12 proposes would make them
robust to future edits.
