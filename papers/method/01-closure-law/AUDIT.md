# AUDIT — 01-closure-law, "The Closure Law of a Finite Index"

Audited 2026-09-24 against `PAPER.md` (634 lines, dated 21 September 2026), `check.py`, `SOURCES.md`,
`FIGURES.tsv`, the five figures, and the rendered `out/01-closure-law.pdf` (25 pages). The audit does
not edit `PAPER.md` or `check.py`; it records, the drafter repairs.

**What was run.** `python3 check.py` (PATH = `method/bin` first, Python 3.12): 126 rows, 0 failures,
88 s — 17 GUARD, 53 MACHINE-CHECKED, 44 EXHAUSTIVE, 6 REFUTATION, 6 CITED, exit 0.
`python3 check.py --selftest`: 129 rows, the three negative controls all reported refuted, exit 0.
`python3 papers/method/lint.py papers/method/01-closure-law`: 0 hits. The PDF was rasterised page by
page (PyMuPDF, 110 dpi) and every page read; the HTML was screenshotted with headless Chromium per the
brief. Figure md5s match `FIGURES.tsv`; `fig-periodic-table.png` is byte-identical to the audited plate
(`PROOF-FIGURES.tsv` row for `figure-6.2.png`, md5 `b383daa6…`).

**Headline.** The mathematics is sound: every proof was read step by step and none is wrong; every
Z3 encoding is the operator the paper defines, both guards run before any obligation is reported, and
every printed number matches a line of `check.py`'s output. The paper cannot go to the author as
"finished", for one reason above all others: **the c = 2 case of Theorem 15 — the result the paper
treats as its new theorem — is Theorem 2.1 of G. Czédli, "Generating Boolean lattices by few elements
and exchanging session keys" (arXiv:2303.10790, 2023; Novi Sad J. Math., doi 10.30755/NSJOM.16637),
proved there by the same Sperner argument, and the paper does not cite it** (A-1). Beside that: two
sentences of §0 state things the paper does not prove (NP-hardness of the seed problem; "global
consistency" as the name of E = 0), the verification record overstates its guards at three points, and
the rendered PDF carries literal `_`, `^{}` and `\|` on most pages.

---

## Part A — content audit

### A.1 Definitions and results against the sources

Every source passage `SOURCES.md` names was opened and read (M = `The_Method_1_6-2.md`,
C = `…Mathematical_Compendium-2.md`). Row by row:

| paper | source | relation | proof complete? |
|---|---|---|---|
| D1–D5 (alphabet, box, hull, boundary, staircase) | M 1537–1556; C 168–178, 324–332 | the source's, own-box regime made explicit; the source's `max ∅ = −∞` convention is replaced by restricting D4 to `a ∈ A_j`, which Lemma 1 justifies | — |
| D6–D8 (closed, defect, seed) | M 3686–3700; C 146–156, 782–792 | the source's; seed defined for closed X only, as C 782 | — |
| Prop. 1 (defect range) | C 236–244 | the source's, with an explicit attaining witness added | yes |
| §2 calendar 365/372/7, seven cells | M 1682–1686, 1710–1725 | exact | — (EXHAUSTIVE) |
| §2 periodic table 90/126/36, blocks; He at 2 gives 20 | M 1516–1556, 1557–1598 | exact | — |
| §2 ordered box 56, E = 0 | M 1599–1610 | exact | — |
| Lemmas 1–3, Theorem 1 | hierarchy paper §2–§3; M 1605–1608 | proofs written independently; complete | yes |
| Lemma 4 | — | new here | yes |
| Lemma 5, Theorem 2 | hierarchy paper §4; M 3688–3700; C 366–376 | stronger than source (source states only "closed iff fixed"); lift cited to Baker–Pixley | yes at d = 2; d ≥ 3 one CITED step, correctly applied (T is a sublattice of a finite product of lattices; the median is a majority term) |
| Theorem 3 | M 3686–3700 (Thm 14.1) | the source's | yes |
| Theorem 4, normal form | M 10414–10466 | stronger (source asserts the pointwise minimum; paper proves φ is the least isotone representation) | yes |
| Theorem 5, nine-cell staircase | C 3592–3610, 554–562 | stronger (source states the band form; paper proves the biconditional) | yes |
| Theorem 6, Table 1, Fig. 4 | M 3737–3762, 4081–4104; C 824–866 | exact at every ambient the source reports (73/146/731; 65.3/68.8/32.7 with ∅, 64.4/68.3/32.6 without; meet-irreducibles 12/14/20) | yes |
| Prop. 2, Theorem 7 | M 4125–4152 | the source's (13/3 … 320/3,776, plus 2⁴) with a written proof; the source's "12 of 12, 56 of 56, 72 of 72" are the separation counts at 4, 8, 9 cells | yes |
| Theorem 8; six-cell refutation; 117/52 | M 9990–10000, 4985–5002 | the source's "roughly one in five" **not reproduced** — measured 44.4 % on the family the witness lives in; recorded in SOURCES.md, the phrase not printed. Correct handling. | yes |
| Theorem 9, Cor. 1, Prop. 3, Remark | M 4804–4845, 10049–10058, 4975–4980 | stronger (biconditional where the source has two one-way statements); the source's 424-test figure not reproduced and not needed | yes |
| Prop. 4 | C 472–492 | the source's, proved | yes |
| Theorems 10–11, region C, Table 2, witnesses | M 10088–10124, 4929–4935 | exact: 12,654 / 113,568 / 565,284; both witnesses | yes |
| Theorems 12–13 | C 598–608, 660–670, 680–688; M 3922–3980 | the source's criterion and set-cover reading, proved | yes (one compressed step, R-M4) |
| Prop. 5; Carathéodory refutation | C 650–658 | source's "seed ≥ Carathéodory number = d" **refuted** by the 3-coordinate chain; correct, and SOURCES.md records it | yes |
| Theorem 14 | C 690–698; M 3942 | stronger (source: d + c − 1 "exact at d = 4, c = 4"; paper proves all d, c, uniqueness, every cell forced) | yes |
| Theorem 15; linear-law refutation | C 638–648; M 3942 | source's d + c − 2 **refuted at d = 5**; paper proves c − 2 + m(d) | yes — see A-1 for what it does not say |

The superseded seed table M 3815–3921 is correctly not used (SOURCES.md item 4). The Freuder
correction (M 3686–3705) is carried as the source's own correction; C 376–390's third reading of
Freuder is not followed, M being later. Both are the right calls.

### A.2 Findings — content

**A-1 · BLOCKING · lines 11, 27, 497–533 (Theorem 15) and SOURCES.md 94–105.** Theorem 15's c = 2
case — `seed({0,1}^d) = min{m : C(m,⌊m/2⌋) ≥ d}` — is Theorem 2.1 of Czédli (2023): "B_n has an at
most k-element generating set iff n ≤ C(k,⌊k/2⌋)", proved there from Sperner's theorem by the antichain
argument the paper gives at line 531. By this paper's own Theorem 2, `ℛ(G) = ⟨G⟩`, so `seed(X)` *is*
the least size of a generating set of the lattice X (see R-M1), and Theorem 15 at c = 2 is Czédli's
theorem verbatim. The paper presents Theorem 15 without attribution and SOURCES.md calls it "new to
this paper". *Resolution:* add the reference — Czédli, G. (2023). Generating Boolean lattices by few
elements and exchanging session keys. arXiv:2303.10790; Novi Sad Journal of Mathematics, doi
10.30755/NSJOM.16637 (author to confirm volume and year) — cite it at Theorem 15 and at line 531 as the
c = 2 case, marked CITED; re-scope the paper's claim to the extension to c ≥ 3 by the Bollobás set-pair
inequality and the `c − 2` shift; and check Czédli's later generating-set papers (arXiv:2309.13783,
2401.00842) for products of chains before claiming the c ≥ 3 case as new. Correct SOURCES.md.

**A-2 · MAJOR · line 27.** "the numerical law for the full box is proved, but the general minimisation
is NP-hard (Karp 1972)". Not proved. Theorem 13 shows the seed problem is an *instance* of minimum
set cover, which bounds its complexity from above; NP-hardness of the seed problem would need a
reduction *from* set cover *to* seed instances, which the paper does not give. Line 471 hedges
correctly ("not expected to have a general formula"); line 27 asserts. *Resolution:* "…but `seed` is in
general an instance of minimum set cover, NP-complete (Karp 1972), and no closed form is claimed
beyond the two families."

**A-3 · MAJOR · lines 487, 489, 539 and the §10 table.** `D(d,c)` is called "a down-set" and Theorem 14
"the down-set seed law". `D(d,c)` is not a down-set of `Box` in the product order: `(1,1) ∈ D(2,2)`,
`(0,1) ≤ (1,1)`, `(0,1) ∉ D(2,2)`. (The source's word comes from reading a non-increasing tuple as an
order ideal of a grid — it is the lattice `L(d, c−1)` of partitions in a `d × (c−1)` box.)
*Resolution:* say "ordered simplex" throughout, or "the lattice of non-increasing tuples, isomorphic to
the lattice L(d, c−1) of Young diagrams in a d × (c−1) box"; retitle Theorem 14 "the simplex seed law".

**A-4 · MAJOR · line 284; `check.py` 597–604.** Theorem 7's status reads "the column E(Cl(U)) computed
independently of the identity and found equal to it in every case". At the seventh ambient
(`2×2×2×2`) `check.py` does **not** compute `|ℛ(Cl(U))|`: for n > 12 it sets `sizeR = 2**n if all_one`
— i.e. it derives the entry from the proof's mechanism (every boundary constant at 1) and then tests
`E_fam == 2**n − len(cl)`, which is tautological there. The audit computed `stair` directly on the 732
characteristic vectors: `|ℛ| = 65,536`, `E = 64,804`, in 2 s — so the fix is free. *Resolution:*
remove the `n <= 12` branch and compute `stair(fam_index)` at every ambient, or reword line 284 to say
the seventh ambient is confirmed through the constant-boundary mechanism.

**A-5 · MAJOR · lines 608, 612; `check.py` 263–281, 378–386.** The non-vacuity guard covers four
hypothesis shapes and §10 says "each of the four hypothesis shapes used above". The obligations use
more: Theorem 4's hypothesis (an isotone integer system ψ with `X = cut(ψ)`) is a fifth, non-trivial
shape and is unguarded; Theorem 9's `bounds`, Prop. 4's non-empty factors and Theorem 5's `L ≤ U` are
further shapes (trivially satisfiable, but not "the four"). The encoding-fidelity guard covers `own`
and the hull encoding only; the Z3 predicates for D6 (`closed`), Theorem 5's band form, Theorem 9's
graph closure and Prop. 3's `hom`/`chain` are unguarded transcriptions. None is wrong (each was read
against its definition), but §10 claims a regime the check does not have. *Resolution:* add a
satisfiability check for Theorem 4's hypothesis at `3×3` and `2×2×2`, add a fidelity row evaluating
`closed` against `is_closed` on random sets, and rewrite the two §10 sentences to name exactly what is
guarded.

**A-6 · MINOR · line 379; `check.py` 389–396.** Prop. 4's Z3 obligation splits the box as (two
coordinates) × (one coordinate): `Q` is one-dimensional, so `ℛ(Q) = Q` trivially. The paper's "with the
two factors quantified over" does not say this; the exhaustive 945 pairs cover the 2-D × 2-D case.
*Resolution:* "…with the factors quantified over, the second factor one-dimensional; the exhaustive
family covers two two-dimensional factors."

**A-7 · MINOR · line 96 (Figure 1 caption).** `|ℛ(X)| = 9`, `E(X) = 4` for the five-cell example are
computed by `figures.py`, not printed by `check.py` (PAPER-SPEC §7: every caption number is in
`check.py`). Verified by hand here (φ₂₁ = 0,2,2,4,4; φ₁₂ = 0,2,2,4,4; nine cells). *Resolution:* add
a row to `check.py` for `X = {(0,0),(1,2),(2,1),(3,4),(4,3)}`.

**A-8 · MINOR · line 610; `check.py` 979–980.** Negative control (3), `seed_formula_box(2,5) != 5`,
compares the new formula with the old one; it exercises no decision procedure and cannot fail unless
the formula is edited. §10 lists it beside two genuine controls. *Resolution:* make it
`seed_bruteforce(Q(2,5), 5)[0] != 5`, or drop it from the §10 list.

**A-9 · MINOR · line 610.** "refuted by 14 failing pairs in a 2 × 2 box" counts ordered pairs (both
orders); Table 1 reports 7 unordered escaping pairs (78 − 71). *Resolution:* "7 unordered pairs" or
change the loop to `i < j`.

**A-10 · MINOR · lines 606, 612.** "The four integer obligations" — three are `unsat` obligations and
the fourth is the `sat` refutation. "Lemmas 1, 2, 3, Proposition 1, Corollary 1, Proposition 2 … are
confirmed over the exhaustive families named above" — Lemmas 1–3 and Corollary 1 have no family in the
table (all "—"). *Resolution:* "three integer obligations and one integer refutation"; "Lemmas 1–3 and
Corollary 1 carry written proofs only; Proposition 1, Proposition 2, Theorems 7, 14 and 15 …".

**A-11 · MINOR · lines 23, 100, 104.** §0 says "Two illustrations run through §2"; §2 measures three.
§0 says "The Gregorian calendar" where §2 says "a common year" — a leap year gives E = 6. Line 104,
"the rhyme every speaker of English is taught", is unprovable. *Resolution:* "Three", "a common year of
the Gregorian calendar", "the rhyme taught beside the calendar".

**A-12 · MINOR · line 264.** "the count [of meet-irreducibles] grows linearly in the ambient" — per
cell the seven values are 1.50, 1.50, 1.50, 1.56, 1.58, 1.42, 1.25: not linear, and falling at the
largest ambient; nothing is proved. *Resolution:* report the counts and say no law is claimed, or drop
the clause.

**A-13 · MINOR · lines 11, 36.** "6 refutations by explicit witness" (abstract) and the status word's
definition "disproved by an explicit witness": one of the six is the solver's `sat` on the triangle
meet with no witness printed (line 578). *Resolution:* "6 refutations, five by explicit witness and one
by solver", or print the solver's model.

**A-14 · MINOR · line 27.** The Birkhoff sentence is garbled by nested dashes and never says what the
chains are: "…since any finite distributive factor can be so presented — as the down-sets of its poset
of join-irreducibles, by Birkhoff's representation theorem (Birkhoff 1967) — but that…". The source
(M 3724–3730) says "one chain per irreducible". *Resolution:* "a finite distributive factor L embeds as
a sublattice of `{0,1}^J`, `J` its join-irreducibles, one two-element chain per irreducible (Birkhoff
1967), so the requirement is only that no two chains be folded into one non-chain coordinate".

**A-15 · MINOR · line 106.** "the f block set aside: 90 cells" — 90 = 118 − 28 presumes Ce–Lu and
Th–Lr detached with La, Ac (or Lu, Lr) in group 3; the paper does not say which 28. *Resolution:* name
the convention in one clause (see R-P1).

### A.3 Findings — the checks (`check.py`) and the verification record

- Encodings: `own` = `realised ∧ in_R` is D5 by Lemma 2 (own-box conjunct present); `ob_hardhalf` is
  Theorem 2's first sentence with S any sublattice of the ambient; `ob_closed_iff_fixed`,
  `ob_moore_intersection`, `ob_projection`, `ob_graph` (h into a 3-chain, both directions),
  `ob_difference`, `ob_seed` (alphabet equality and `φ` equality via reach-sets guarded by `inS`),
  `ob_normalform`, `ob_product`, `ob_staircase_form` (both directions) — each read against its
  definition; each is the statement the paper marks MACHINE-CHECKED, and each names its box. The
  integer obligations quantify over ℤ with the band hypothesis checked satisfiable. Guards run in
  `main()` before `z3_obligations()` and a failed guard returns 1 with nothing reported. **No claim is
  marked MACHINE-CHECKED for a box the check does not cover.**
- Every printed number was matched to an output line: 74,569; 26,206; 815,072; Table 1 (all seven rows,
  both percentage sets, meet-irreducibles, E); 117/52/44.4 %; 438; 3,713; Table 2; 945; 5,111; 219; the
  seven box seeds and thirteen clique counts; nine simplices; 2,919; 400; 24/50; 73/2,851; 60; twelve
  non-vacuity rows; 53/44/6/6/17. Two caption numbers are not from `check.py` (A-7). Row counts by
  status in the §10 table reconcile to 53 boxes and 44 families.
- The sentence at line 608, "each of the four hypothesis shapes", and line 284, "computed
  independently", are the two places the record overstates (A-4, A-5). Line 612's "the two soundness
  guards are the only SAMPLED figures" is accurate as a classification (both guards are sampled).

### A.4 Findings — figures

Figures 1, 3, 4, 5 were checked cell by cell against the check's data: Figure 1's five cells, four
added cells and both staircases are D4 read correctly (solid = φ₂₁, dashed = φ₁₂); Figure 3's nine
cells and L, U match; Figure 4's thirteen members (1 + 4 + 5 + 2 + 1) and the two ringed chains are
right; Figure 5's steps are `m(d)` (2 at d = 2, 3 at 3, 4 on 4–6, 5 on 7–10, 6 on 11–20, 7 on 21–35),
the c = 3 curve is one higher, the six circles are the six instances.

**A-16 · MAJOR · Figure 2 (line 110), rendered p. 5.** The audited plate carries its own title, "36
cells the structure admits and the table denies", drawn *over* the period-1 row of cells; at print size
the title overprints the red cells it describes. The y-axis labels only periods 1, 3, 5, 7. The data
are right (90 blue, 36 red, blocks as captioned), but a figure with text overprinting its data is not
publication quality. *Resolution:* regenerate it in `figures.py` from `check.py`'s periodic-table row
(all four caption facts are produced there), or crop the title band; record the new md5.

**A-17 · MINOR · Figure 3 (line 236).** The grid draws a `t = 5` row that is outside `Box(X)`
(`A₂ = {0,…,4}`); the figure shows a 4 × 6 grid for a 4 × 5 box. *Resolution:* drop the row, or say in
the caption that the grid is the ambient and the box is the lower five rows.

**A-18 · MINOR · Figure 5 caption (line 537).** "a seventh, at c = 4, lies off both curves" — the
seventh instance (4², seed 4) is not drawn at all. *Resolution:* "a seventh, 4² with seed 4, is not
plotted".

### A.5 Findings — lint and the rendered PDF

`lint.py`: 0 hits. The rendered pages (all 25 read) show:

**A-19 · MAJOR · throughout (pp. 1, 3, 5–9, 12–13, 16–19, 22–23).** Mathematics is set in code spans
and the subscripts and superscripts fall back to literal ASCII: `φ_ij(a)`, `x_i`, `A_j`, `π_ij`,
`2^{|U|}` (abstract, p. 1), `φ^{ℛ(X)}_ij` and `φ^X_ij` (p. 6), `φ_{day,month}` and
`φ_{group,period}(1)` (p. 5), `φ_{pq}(0)` (p. 12), `B_k`, `M_a`, `a_p` (p. 16), `(c−1)^k 0^{d−k}`
(p. 18), `Σ_{j=1}^{d} 1 / C(|A_j| + |B_j|, |A_j|)` (p. 19), `2^{\|U\|}` (p. 22). The brief's criterion
is explicit: an underscore or caret in prose is a defect. *Resolution:* Unicode subscripts for every
single-letter index (`φᵢⱼ`, `xᵢ`, `Aⱼ`, `πᵢⱼ`, `Bₖ`, `Mₐ`) as the paper already does for `φ₂₁`, `S₁`,
`x₁`; write the few genuine superscripts without braces (`2^|U|`, `(c−1)ᵏ0ᵈ⁻ᵏ`, `Σⱼ 1/C(|Aⱼ|+|Bⱼ|,
|Aⱼ|)`); reserve code spans for whole displayed formulas.

**A-20 · MAJOR · Table 1 header (p. 11), Table 2 header (p. 17), §10 table rows for Theorem 7,
Theorem 10 and the region (pp. 22–23).** Literal backslashes on the page: `\|Cl(U)\|`,
`\|a − b\| ≤ c`, `E(Cl(U)) = 2^{\|U\|} − \|Cl(U)\|`, `band \|a−b\| ≤ k`, `region \|a−b\| ≤ c`. The
pipe escapes needed inside a pipe table are not unescaped inside code spans. *Resolution:* in table
cells use U+2223 `∣` for the bar, or move `|…|` outside the backticks.

**A-21 · MAJOR · pp. 21–23.** §10's table is forced whole to a new page (`page-break-inside: avoid`),
leaving page 21 two-thirds blank after one paragraph, and then splits anyway across pp. 22–23 with the
row "Proposition 3, the difference" broken: its cells (`✓ | 3×3, 4×4, 3×3×3`) end p. 22 with an empty
label and its label opens p. 23 with empty cells. *Resolution:* in `paper.html` set
`table { page-break-inside: auto }` and `tr { page-break-inside: avoid }` (with `thead` repeating), or
split the table into two.

**A-22 · MINOR · pp. 4–5, 10, 12, 20.** Every image is followed by a stray line "Figure N" — the
markdown alt text rendered as an implicit figcaption — above the real bold caption; and Figure 1's
image sits at the foot of p. 4 with its caption at the head of p. 5. *Resolution:* empty the alt text
(`![](…)`) or make the alt the caption; keep image and caption in one `figure`.

**A-23 · MINOR · pp. 6, 14, 17.** Theorem 1's clauses render as "1. 2. 3." while the proof and the
whole paper cite "(i)", "(ii)", "(iii)"; Theorem 9's and Theorem 12's "(a)", "(b)" render as "1.",
"2." while the proofs and Corollary 1 cite "(a)", "(b)". Pandoc reads `> (i) …` as an ordered list.
*Resolution:* write the labels so they are not list markers (`> **(i)** …` on one paragraph, or
`(i)\ ` with a non-breaking space).

---

## Part B — reader audits

### B.1 A lattice theorist (order and combinatorics), who has not seen this material

I read the paper from D1. The objects are defined before use, the proofs are proofs — I checked
Lemma 5's four-witness identity, Theorem 5 in both directions, Theorem 9's necessity, Proposition 3's
incomparable case, Theorem 14's forced cells, and Theorem 15's two bounds step by step and found no
gap. Baker–Pixley is invoked exactly where it applies (a sublattice of a finite product of lattices;
the median is a majority term). The Bollobás inequality is applied to the right set-pair system
(`A_j ∩ B_j = ∅`, `A_i ∩ B_j ≠ ∅` for all ordered `i ≠ j`), the central-binomial bound is right, and
the antichain construction is surjective and pairwise compatible for `m ≥ 2`. My findings are about
what is *not said* and about statements that are false as written.

**R-M1 · MAJOR · D8 (line 68) and §9 (line 441).** By Theorem 2, `ℛ(G) = ⟨G⟩`. So "G is a seed of X"
means "G generates the lattice X", and `seed(X)` is the minimum number of generators of X as a lattice
— a classical quantity. The paper never says this, and it should, in one sentence after Theorem 2 or
at D8: it makes Theorems 12–15 legible to an order theorist, it is what makes Czédli's theorem (A-1)
apply, and it tells the reader that Theorem 14 concerns the minimum generating set of Young's lattice
`L(d, c−1)`. *Resolution:* add the sentence, and rename "seed" or keep it with the gloss.

**R-M2 · MAJOR.** I concur with A-2 (NP-hardness asserted, not proved) and A-3 ("down-set" is false in
the product order). A referee in *Order* would stop at both.

**R-M3 · MINOR · Theorem 12 (line 446).** Clause (b) quantifies `φ^G_ij(a)` over `a ∈ A_j` (X's
alphabet), but D4 defines `φ^G` on `π_j(G)` only; before (a) is assumed, (b) is not well formed.
*Resolution:* "(a), and, given (a), (b) …", or define `φ^G` on `A_j` by the same maximum and note it is
attained when `a ≥ min π_j(G)`.

**R-M4 · MINOR · Theorem 13 proof (line 467).** "By the choice of the steps, `φ^X_ij` is constant on
`[t, a]`" compresses a step: it needs Lemma 1 (isotonicity) — the value `φ(a)` is first attained at some
step `t'' ≤ a`, `t'' ≤ t` by maximality of `t`, and `φ(t'') ≤ φ(t) ≤ φ(a) = φ(t'')`. *Resolution:* write
those two lines.

**R-M5 · MINOR · Theorem 5 statement (line 214).** "write `A_1, A_2` for the observed alphabets of a set
`S ⊆ A_1 × A_2`" is circular. *Resolution:* "Let `S` be a finite set of pairs with observed alphabets
`A_1 = π_1(S)`, `A_2 = π_2(S)`".

**R-M6 · MINOR · line 208.** "φ is the pointwise smallest, and the set it cuts is therefore the
smallest" — every ψ in the hypothesis cuts the same X; the clause says nothing. *Resolution:* delete
"and the set it cuts is therefore the smallest".

**R-M7 · MINOR · Theorem 15 (lines 505, 511).** The "Equivalently" clause needs `k ≥ c` (for `k < c`
the binomial is degenerate and no `k` cells generate). The upper-bound paragraph should open "Suppose
`G` of size `k` generates `Q(c,d)`". *Resolution:* add both.

**R-M8 · MINOR · Proposition 3 (line 345) at `3×3×3`.** On a box with `d > 2`, `⊑` compares only the
two coordinates `h` reads and is a preorder, not an order; cells equal on those two coordinates are
mutually comparable. The theorem and check are right under that reading; say "chain in the preorder
⊑" or state the proposition for `d = 2` and remark on the lift.

**R-M9 · MINOR · line 252 and Table 1.** "a Moore family is generated under intersection by those
members alone" needs `U` as the empty intersection, and the count excludes `U` (the top is not
meet-irreducible in the check's convention). *Resolution:* one clause.

**R-M10 · MINOR · §0 line 27.** I concur with A-14: the Birkhoff sentence does not parse.

What is unmotivated: §5's Theorem 7 is presented as striking ("the family of closed indexes is itself
maximally open") but, read as R-M1 suggests, it says only that the characteristic vectors of a
separating, ∅- and U-containing family have trivial pairwise bounds — true of any Moore family on U
that separates points. State that generality or the reader will suspect a trick. Otherwise the
motivation (E as the price of a layout) is clear and the examples carry it.

### B.2 An atomic physicist who works with NIST spectra

This paper is mathematics; there are no spectra, energies, units or NIST provenance to check, and I
find nothing wrong on those heads because nothing of that kind is claimed. I read §2's worked defects
and the framing, and §8, which borrows the language of coupling.

**R-P1 · MINOR · line 106.** "the eighteen-column table with the f block set aside: 90 cells". Ninety
is 118 minus the 28 elements Ce–Lu and Th–Lr, with La and Ac (equivalently Lu and Lr) in group 3 so
that periods 6 and 7 are full. Say so; a reader who detaches all thirty f-block elements gets 88
cells and a different E. *Resolution:* one parenthesis naming the 28.

**R-P2 · MINOR · lines 23, 106.** "E is a property of a drawing, not of chemistry" and "They are not a
defect in chemistry" overstate. The 36 gaps are where the coordinates (period, group) fail to carry
the shell structure — `ℓ ≤ n − 1` forbids most of them and the Madelung order defers the rest — which
is chemistry the coordinatisation cannot encode. *Resolution:* "a property of the coordinatisation,
not of the elements", and "not a defect in the elements".

**R-P3 · MINOR · line 108.** "Helium's position is the most argued question in periodic-table design"
is an uncited opinion. *Resolution:* cite Scerri, E. R. (2020), *The Periodic Table: Its Story and Its
Significance*, 2nd ed., Oxford University Press, and Grochala, W. (2018), On the position of helium and
neon in the Periodic Table of Elements, *Foundations of Chemistry* **20**, 191–207; note IUPAC's
placement at group 18.

**R-P4 · MINOR · §8, lines 387, 400–402, 435.** Δ is introduced as "the triangle inequality, as it
constrains a third quantity formed by combining two others" and the section closes with "a coupling
whose admissibility is a triangle inequality cannot be carried exactly". If the intended coupling is
angular momentum, the physical region also carries the integrality condition (in doubled units,
`2J ≡ 2j₁ + 2j₂ (mod 2)`), which Δ ⊆ ℤ³ omits; the meet failures would need re-counting on the
physical region. As written the section is purely mathematical and correct. *Resolution:* either keep
it mathematical and drop the word "coupling" from lines 387 and 435, or state the physical region with
its parity condition and say the counts are for the relaxation.

**R-P5.** I concur with A-11: "the Gregorian calendar" in §0 should read "a common year", since a leap
year has E = 6 under the same operator.

Nothing here is overstated about spectra because nothing is said about them; the "companion paper"
note at line 541 is the right scope.

### B.3 A referee for *Order* / *Algebra Universalis*

**Novelty.** The closure-operator and hull results (Theorems 1–3) are, as the paper says, classical
(Moore; Baker–Pixley; Topkis; Queyranne–Tardella) and the paper claims for them only the reading of
`E` as a defect — acceptable. The consequences in §4–§8 are correct and elementary; I would accept
them as a systematic development. §9 is where the paper's weight lies and where it fails as submitted:

**R-C1 · BLOCKING.** A-1. Theorem 15 at `c = 2` is Czédli's Theorem 2.1 (2023), with the same proof.
A submission that presents it as its own would be returned. The `c ≥ 3` extension via Bollobás may be
new; the author must say so after checking Czédli's subsequent papers on generating direct products.

**R-C2 · MAJOR · lines 25, 188.** "The property `E(X) = 0` also has a name in constraint satisfaction —
global consistency of a binary network — and two certificates there: Montanari (1974) … and Dechter
(1992)". This is not right. Global consistency is a property of a *network* (every locally consistent
partial assignment extends), not of a relation; the network of recovered staircases is globally
consistent for *every* X — for `X = {(0,1),(1,0)}` its network is the full `2×2` box, globally
consistent, and `E = 2`. What `E(X) = 0` says is that X *is the solution set* of a binary network of
staircase constraints — in Montanari's terms, X is binary-decomposable into (≤,≤)-monotone
constraints — and, that network being path consistent and row convex, it is then globally consistent
by van Beek and Dechter (1995). Dechter (1992) is about width-based local-to-global consistency and
does not certify the identification. *Resolution:* rewrite both sentences as above; drop
"certificates"; keep Montanari for "binary decomposable", van Beek–Dechter for row-convex global
consistency, Deville et al. for the class; cite Dechter (1992) only for what it proves or not at all.

**R-C3 · MAJOR · line 479.** "for a semilattice with its subsemilattices as convex sets the
Carathéodory number is the breadth, and the breadth of a product of d chains is d (Queyranne and
Tardella 2008, CITED)". The 2008 *Discrete Mathematics* paper is about hulls, representations by
projections and epigraphs, and counting; the semilattice statement is Jamison's, and Queyranne and
Tardella's work on these numbers is their 2017 paper. Carathéodory (1911) is in the reference list and
cited nowhere in the text. *Resolution:* cite Jamison, R. E. (1974), *A General Theory of Convexity*,
Ph.D. thesis, University of Washington (or Jamison-Waldner, R. E. (1982), A perspective on abstract
convexity: classifying alignments by varieties, in *Convexity and Related Combinatorial Geometry*,
Dekker, 113–150) and van de Vel, M. L. J. (1993), *Theory of Convex Structures*, North-Holland, for
"Carathéodory number = breadth"; and Queyranne, M. and Tardella, F. (2017), Carathéodory, Helly, and
Radon numbers for sublattice and related convexities, *Mathematics of Operations Research* **42**(2),
495–516, for the sublattice convexity; cite Carathéodory 1911 at the definition or remove it.

**R-C4 · MINOR · lines 25, 188.** "the double-projection theorem of Bergman (1977)". Bergman's paper
proves the *converse* — that d-fold projection determination of subalgebras of finite products
characterises varieties with a (d+1)-ary near-unanimity term — and states the forward direction as
Baker–Pixley's. For sublattices of products of chains the forward direction is also Topkis (1976) and
Veinott (1989). *Resolution:* attribute the determination theorem to Baker and Pixley (1975), cite
Bergman for the converse and the terminology, and add Veinott, A. F. Jr. (1989), Representation of
general and polyhedral subsemilattices and sublattices of product spaces, *Linear Algebra and its
Applications* **114/115**, 681–704 — the reference a referee in this area expects beside Topkis and
Queyranne–Tardella.

**R-C5 · MINOR · line 531.** "Sperner (1928) … of which Bollobás's inequality is the generalisation".
The intermediate is the LYM inequality (Yamamoto 1954; Meshalkin 1963; Lubell 1966), which Bollobás's
set-pair inequality generalises. *Resolution:* one clause and, optionally, Lubell, D. (1966), A short
proof of Sperner's lemma, *Journal of Combinatorial Theory* **1**, 299.

**R-C6 · MINOR · line 62 (D5).** The word "staircase" is adopted from Deville, Barette and Van
Hentenryck (1999) but the citation appears only in §0 and §3. Cite it where the term is introduced.
The Moore-family literature (Moore 1910, Ward 1942, Caspard–Monjardet 2003) and the row-convex
literature (van Beek–Dechter 1995, Deville et al. 1999) are otherwise cited where expected; Ganter and
Wille (1999), *Formal Concept Analysis*, would be a natural addition for "closure defect" but is not
required.

**R-C7 · MINOR · Theorem 14.** `D(d,c)` is the lattice `L(d, c−1)` (Stanley, R. P. (1980), Weyl
groups, the hard Lefschetz theorem, and the Sperner property, *SIAM J. Algebraic and Discrete Methods*
**1**, 168–184); a minimum generating set of `L(m,n)` may exist in the literature. *Resolution:* name
the lattice and check.

**Correctness and clarity.** The proofs are correct (I concur with R-M3–R-M8 on presentation). The
abstract and §0 promise what the body delivers with three exceptions: A-2 (NP-hard), A-11 ("Two
illustrations"), A-13 ("by explicit witness"). **Verification record.** It is honest in substance — the
encodings are the definitions, the guards run first, the boxes are named — and overstated at three
points I would ask to be fixed before acceptance: A-4 (an "independent" column that is derived at one
ambient), A-5 ("the four hypothesis shapes"), A-8 (a negative control that tests nothing). The
typography (A-19–A-23) would be returned by any copy-editor.

**References.** Present entries check out (Baker–Pixley Math. Z. 143; Bergman Alg. Univ. 7; Bollobás
Acta Math. Hungar. 16; Dechter AI 55; Deville et al. AI 109; Freuder JACM 29; Karp 1972; Montanari
Inf. Sci. 7; Queyranne–Tardella DM 308; Sperner Math. Z. 27; Topkis PJM 65; Ward Ann. Math. 43; van
Beek–Dechter JACM 42; Caspard–Monjardet DAM 127). Missing, in order of necessity: Czédli 2023 (A-1);
Veinott 1989 (R-C4); van de Vel 1993 and Queyranne–Tardella 2017 (R-C3); Lubell 1966 (R-C5, optional);
Stanley 1980 (R-C7, optional); Scerri 2020 and Grochala 2018 (R-P3).

---

## Part C — the record

| id | severity | where | finding | disposition |
|---|---|---|---|---|
| A-1 / R-C1 | BLOCKING | 11, 27, 497–533; SOURCES.md 94–105 | Theorem 15 at c = 2 is Czédli 2023, Thm 2.1; uncited; "new" claim | **FIXED.** Czédli 2023 verified on the arXiv full text (Thm 2.1 = the c = 2 case, both halves by the Sperner antichain argument); his arXiv:2308.15625 Thm 2.4 + Obs 3.1 (Griggs–Stahl–Trotter) covers every c, so Theorem 15 is CITED in full, headed "Czédli", with the paper's proof kept as a second proof; abstract, §0, §3, §9, §10, references, check.py CITED row and SOURCES.md re-scoped — the paper claims Theorems 13–14 and the linear-law refutation only. One discrepancy recorded: Czédli 2023b table (4.30) prints 18 at (5-chain, 2023) where its Thm 2.4 and the law give 17; check.py prints both. |
| A-2 / R-M2 | MAJOR | 27 | "general minimisation is NP-hard" — not proved (seed is an instance of set cover, not shown hard) | **FIXED.** §0 and §9 now say seed is an instance of minimum set cover, NP-complete (Karp 1972) — a bound from above, no hardness claimed, no closed form beyond the two families. |
| A-3 / R-M2 | MAJOR | 487, 489, 539 | D(d,c) is not a down-set of the product order; "down-set seed law" misnamed | **FIXED.** "ordered simplex" throughout, Theorem 14 retitled "the simplex seed law", the (1,1)/(0,1) counterexample stated, D(d,c) identified with L(d, c−1) (Stanley 1980); §10 row renamed. |
| A-4 | MAJOR | 284; check.py 597–604 | E(Cl(U)) at 2×2×2×2 derived from all-ones boundary, not computed; "independently" false there (direct computation: 65,536, 2 s) | **FIXED.** check.py computes stair() on the family at every ambient (|ℛ(Cl)| = 65,536 at 2×2×2×2, ~2 s) and prints it; the n ≤ 12 branch is gone; Theorem 7's status and the §10 row say the column is computed directly. |
| A-5 | MAJOR | 608, 612; check.py 263–281, 378 | "four hypothesis shapes" — Theorem 4's is a fifth, unguarded; `closed` and other Z3 predicates have no fidelity guard | **FIXED.** Two new guards: Theorem 4's hypothesis satisfiable non-trivially at 3×3 and 2×2×2; the Z3 closure predicate evaluated against is_closed on 300 random sets over five shapes (0 disagreements). §10 names the three guarded predicates, lists the unguarded transcriptions, and says fourteen non-vacuity checks over five shapes. 20 guards. |
| A-6 | MINOR | 379 | Prop. 4 Z3 box splits (2 coords)×(1 coord); text does not say so | **FIXED.** Wording as resolved: second factor one-dimensional; the exhaustive family covers two two-dimensional factors. |
| A-7 | MINOR | 96 | Figure 1 caption numbers not produced by check.py | **FIXED.** check.py row "Figure 1: the five-cell index in 5x5" (|ℛ| = 9, E = 4, both φ printed); figures.py draws from check.FIG1_INDEX. |
| A-8 | MINOR | 610; check.py 979 | selftest control (3) compares two formulas; no decision procedure | **FIXED.** Control (3) is now seed_bruteforce(2⁵, 5) by direct closure: every subset of size < 4 fails, four cells generate; §10 says each control is a decision procedure. |
| A-9 | MINOR | 610 | "14 failing pairs" are ordered; Table 1 says 7 | **FIXED.** Loop is i < j; 7 unordered pairs; §10 says so. |
| A-10 | MINOR | 606, 612 | "four integer obligations" (three + a refutation); Lemmas 1–3, Cor. 1 have no exhaustive family | **FIXED.** "three integer obligations and one integer refutation"; Lemmas 1–3 and Corollary 1 "carry written proofs only", the exhaustive list starts at Proposition 1. |
| A-11 / R-P5 | MINOR | 23, 100, 104 | "Two illustrations" (three); "Gregorian calendar" (common year; leap year E = 6); "every speaker of English" | **FIXED.** "Three illustrations"; "A common year of the Gregorian calendar"; "the rhyme taught beside the calendar". |
| A-12 | MINOR | 264 | meet-irreducibles "grow linearly" — 1.50…1.25 per cell, unproved | **FIXED.** Clause dropped; the caption reports the counts and says no law is claimed. |
| A-13 | MINOR | 11, 36 | "6 refutations by explicit witness" — one is by solver `sat` | **FIXED.** Abstract: "five by explicit witness and one by solver"; the REFUTATION status word admits a solver's satisfying assignment. |
| A-14 / R-M10 | MINOR | 27 | Birkhoff sentence garbled; does not name the chains | **FIXED.** Rewritten as resolved: L embeds in {0,1}ᴶ, one two-element chain per join-irreducible (Birkhoff 1967); the requirement is only that no two chains be folded. |
| A-15 / R-P1 | MINOR | 106 | which 28 f-block elements are detached is not stated | **FIXED.** The 28 named (Ce–Lu, Th–Lr), La and Ac in group 3 so periods 6 and 7 are full. |
| A-16 | MAJOR | Fig. 2, p. 5 | plate title overprints the period-1 cells; y-axis labels 1,3,5,7 only | **FIXED.** Figure 2 regenerated by figures.py fig_periodic() from check.periodic_cells()/stair(): no text over the grid, all seven periods labelled, legend below; FIGURES.tsv records the replaced plate's md5 and the reason; caption says the figure is computed. |
| A-17 | MINOR | Fig. 3 | t = 5 row drawn outside Box(X) | **FIXED.** Grid trimmed to the 4×5 box; caption names the box. |
| A-18 | MINOR | 537 | "seventh … lies off both curves" — it is not plotted | **FIXED.** "a seventh, 4² with seed 4, and an eighth, 5² with seed 5, are not plotted." |
| A-19 | MAJOR | pp. 1–23 | literal `_`, `^{}` in code-span mathematics throughout | **FIXED.** Every mathematics code span rewritten as plain Unicode (mechanical pass, then hand rewrites where no glyph exists: φᵢⱼ[X] for a named boundary function, ∏ᵢ Aᵢ for the product, n = |U| and 2ⁿ, cells p ≠ r, u/v/w in the §8 proofs, Pⱼ/Zⱼ in Theorem 15, xᵢ ≥ xᵢ₊₁ for the simplex); a text scan of all 27 rendered pages finds no _, ^, \\ or *. |
| A-20 | MAJOR | pp. 11, 17, 22–23 | literal `\|` in Table 1/2 headers and §10 rows | **FIXED.** ∣ (U+2223) in every table cell that carries a bar (Table 1 and 2 headers, §10 rows for Theorems 7, 10 and the region). |
| A-21 | MAJOR | pp. 21–23 | §10 table: p. 21 two-thirds blank; row "Proposition 3" split across pages | **FIXED.** The §10 table is split in two (§2–§5; §6–§9); no row is split; the second table moves whole to the next page and leaves about a quarter of p. 23 blank, within the finding's criterion. |
| A-22 | MINOR | pp. 4–5, 10, 12, 20 | stray "Figure N" line under every image; Fig. 1 separated from caption | **FIXED.** Empty alt text and the caption in the image's own paragraph: no stray "Figure N" line; Figure 1 and its caption share p. 5. |
| A-23 | MINOR | pp. 6, 14, 17 | (i)–(iii) and (a)/(b) render as 1./2./3.; proofs cite the letters | **FIXED.** Labels written **(i)**, **(a)** and the clauses separated as blockquote paragraphs, so the proofs' "(i)", "(a)" match the page. |
| R-M1 | MAJOR | 68, 441 | seed(X) = minimum generating set of the lattice X (by Thm 2) never stated | **FIXED.** Gloss at D8 (seed(X) = least generating size of the lattice X, by Theorem 2) and at the opening of §9; this is what makes the Czédli identification exact. |
| R-M3 | MINOR | 446 | Thm 12(b) uses φ^G outside its domain before (a) | **FIXED.** Clause (b) reads "given (a)", with the note that (a) makes Box(G) = Box(X). |
| R-M4 | MINOR | 467 | Thm 13 "constant on [t,a]" needs Lemma 1 spelled out | **FIXED.** The two lines written: t″ ≤ t by maximality, then Lemma 1 sandwiches the three values. |
| R-M5 | MINOR | 214 | Thm 5 statement circular ("alphabets of S ⊆ A₁ × A₂") | **FIXED.** "let S be a finite non-empty set of pairs with observed alphabets A₁ = π₁(S), A₂ = π₂(S)". |
| R-M6 | MINOR | 208 | "the set it cuts is therefore the smallest" — empty clause | **FIXED.** Clause deleted. |
| R-M7 | MINOR | 505, 511 | Thm 15 "Equivalently" needs k ≥ c; upper bound should assume a generating G | **FIXED.** "for k ≥ c" added (k < c handled by Proposition 5); the upper bound opens "Suppose G, of size k, generates Q(c, d)". |
| R-M8 | MINOR | 345 | ⊑ is a preorder for d > 2; "chain" needs the qualifier | **FIXED.** ⊑ stated as a partial order at d = 2 and a preorder for d > 2; "chain in ⊑" defined as any two cells comparable. |
| R-M9 | MINOR | 252, 264 | meet-irreducible generation needs U as empty intersection; top excluded | **FIXED.** Caption: members other than U; the family is generated by them together with U, the empty intersection. |
| R-P2 | MINOR | 23, 106 | "not of chemistry" overstated — of the coordinatisation | **FIXED.** "a property of the coordinatisation, not of the elements"; "not a defect in the elements", with the shell structure named as what the coordinates do not carry. |
| R-P3 | MINOR | 108 | helium claim uncited (Scerri 2020; Grochala 2018) | **FIXED.** Scerri 2020 and Grochala 2018 cited; IUPAC's group-18 placement named. |
| R-P4 | MINOR | 387, 400, 435 | "coupling" language vs Δ ⊆ ℤ³ without the parity condition | **FIXED.** "coupling" dropped at both places; §8 kept mathematical (the parity condition is not introduced). |
| R-C2 | MAJOR | 25, 188 | E(X) = 0 is not "global consistency"; it is decomposability into a staircase network; Dechter 1992 misused | **FIXED.** §0 and §3 rewritten: E = 0 is binary decomposability into staircase constraints (Montanari 1974), global consistency then by van Beek & Dechter 1995; the {(0,1),(1,0)} counterexample at E = 2 printed; Dechter 1992 removed from text, references and check.py's CITED row; SOURCES.md records that the source's Dechter attribution is not carried. |
| R-C3 | MAJOR | 479 | Carathéodory/breadth attributed to Queyranne–Tardella 2008; correct sources Jamison / van de Vel 1993 / Q–T 2017; Carathéodory 1911 uncited | **FIXED.** Jamison-Waldner 1982, van de Vel 1993 and Queyranne–Tardella 2017 cited (the last verified: MOR 42(2), 495–516); Carathéodory 1911 cited at the definition; the 2008 paper kept only for the hull statement in §3. |
| R-C4 | MINOR | 25, 188 | Bergman 1977 vs Baker–Pixley emphasis; add Veinott 1989 | **FIXED.** Forward direction attributed to Baker & Pixley 1975, Bergman 1977 to the name and the converse, Veinott 1989 added beside Topkis and Queyranne–Tardella; abstract reworded. |
| R-C5 | MINOR | 531 | LYM inequality omitted between Sperner and Bollobás | **FIXED.** "by way of the LYM inequality (Lubell 1966)"; Lubell 1966 in the references. |
| R-C6 | MINOR | 62 | cite Deville et al. where "staircase" is introduced | **FIXED.** Deville, Barette & Van Hentenryck 1999 cited at D5. |
| R-C7 | MINOR | 487 | D(d,c) = L(d, c−1); check the generating-set literature | **FIXED.** D(d,c) = L(d, c−1) named with Stanley 1980; the paper states that Theorem 14 is not a case of Czédli's direct-power theorem and that no statement of it in the literature is known (Czédli's generating-set papers checked; Young's-lattice literature not searched further — SOURCES.md says so). |

Counts: **1 BLOCKING, 11 MAJOR, 28 MINOR** (40 findings; A-1/R-C1, A-2/R-M2, A-3/R-M2, A-11/R-P5,
A-14/R-M10 and A-15/R-P1 are each one row).

Re-verification commands: `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH;
cd papers/method/01-closure-law; python3 check.py; python3 check.py --selftest;
python3 ../lint.py .; python3 ../render.py .` — and for A-4, the two-second direct computation of
`stair` on the 732 characteristic vectors at `2×2×2×2`, which returned 65,536.

---

## Repair record — 2026-09-24

Repaired by the drafter against every finding above; nothing above was deleted or rewritten.
**Dispositions: 40 FIXED, 0 DECLINED** (BLOCKING 1/1, MAJOR 11/11, MINOR 28/28).

**Czédli verified.** arXiv:2303.10790v3 read in full: Theorem 2.1 is the c = 2 case of Theorem 15,
proved by the same two-sided Sperner argument. The later papers the audit named (arXiv:2309.13783,
2401.00842) do not cover products of chains, but arXiv:2308.15625 (Ural Math. J. 10(1), 2024) does —
Theorem 2.4 (k ↦ G_min(Dᵏ) is the left adjoint of n ↦ S(J(D), n)) with Observation 3.1(d) and the
Griggs–Stahl–Trotter count gives c − 2 + m(d) for every c. Theorem 15 is therefore CITED in full and the
paper claims only Theorems 13–14 and the linear-law refutation. One discrepancy recorded, not repaired:
Czédli 2023b's table (4.30) prints 18 for the five-element chain at d = 2022, 2023, where its own
Theorem 2.4 (p = 3, f*(2023) = 14) and the law give 17; `check.py` prints both.

**What changed.** `PAPER.md`: every mathematics code span rewritten as plain Unicode (A-19, A-20); §0,
§3 and §9 rewritten for A-1, A-2, R-C2, R-C3, R-C4; every other finding at its line; the §10 record in
two tables; date 24 September 2026. `check.py` (never weakened): Theorem 4 non-vacuity guard (2 rows),
closure-predicate fidelity guard, |ℛ(Cl(U))| computed directly at every ambient, Figure 1 row, 5² box,
the law at (5, 2023), eight CITED rows, selftest controls (2) and (3) replaced by decision procedures,
`periodic_cells()` factored out for `figures.py`. `figures.py`: computed Figure 2 (`fig_periodic`),
Figure 3 grid trimmed. `FIGURES.tsv`: rewritten (two new md5s, replaced plate recorded). `SOURCES.md`:
novelty section, Czédli verification and discrepancy, R-C2/R-C3 attributions, guard figures, figures.

**Re-verification.** `python3 check.py`: 134 rows, 0 failures (20 GUARD, 53 MACHINE-CHECKED,
47 EXHAUSTIVE, 6 REFUTATION, 8 CITED), exit 0. `--selftest`: 137 rows, three controls refuted, exit 0.
`lint.py`: 0 hits. `render.py`: 27 pages. Every page rasterised and its text scanned: no literal
underscore, caret, backslash or asterisk; the HTML screenshotted with headless Chromium per
BRIEF-AUDIT step 6.

