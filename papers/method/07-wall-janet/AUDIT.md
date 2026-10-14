# AUDIT.md — 07-wall-janet, "The Parent-Term Wall and the Janet Collapse"

Audit of the finished draft dated 21 September 2026, written 24 September 2026 against `BRIEF-AUDIT.md`
and `PAPER-SPEC.md` §4, §5, §8, §10. Nothing in `PAPER.md` or `check.py` was edited. Line numbers are
lines of `PAPER.md`.

**What was run.** `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH` (Python 3.12.3, Z3
5.1.0), then `python3 check.py` — 101 obligations, 0 failed (EXHAUSTIVE 85, GUARD 3, MACHINE-CHECKED
13), exit 0 — and `python3 check.py --selftest` — 105 obligations, the four negative controls each
refuted, exit 0. `python3 papers/method/lint.py papers/method/07-wall-janet` — 0 hits.
`python3 papers/method/render.py papers/method/07-wall-janet` — 18 pages; every page rasterised and read.
The five figures were read as images. An independent script (kept in the auditor's scratch, not in the
tree) recomputed the encoding guard three ways, the exact Mann–Whitney distribution, E for two
presentations the paper does not print, and the single-term cut under the observed configurations; its
results are quoted where they bear on a finding.

---

## Part A — content audit

### A.1 Definitions, results and their sources

| object (line) | source passage | paper vs source | proof complete? |
|---|---|---|---|
| D1–D4 index, box, reach bounds, ℛ, E (80–94) | main volume 1530–1545 (§6.1) | the source's definitions verbatim, with the non-emptiness and monotonicity of φ̂ added | — |
| Lemma 1 extensivity, Lemma 2 idempotence (118–124) | main volume 1621–1622 states idempotence and points elsewhere for its proof | paper proves both in full — stronger than the passage | Lemma 1 yes; Lemma 2 yes for idempotence, monotonicity is "immediate" (A-19) |
| Theorem 1 chain ⇒ fixed (128–138) | no source passage; the paper's own | — | yes (see A.3) |
| Theorem 2 bi-monotone ⇒ fixed (140–148) | no source passage; the paper's own | — | yes (see A.3) |
| Lemma 3 corners ⇒ box (152–154) | no source passage; the paper's own | — | yes |
| Theorem 3, E = 36 (180–184) | main 1516–1522; Index of Indices 1361–1372 | same numbers; proof via Lemma 3 is the paper's own | yes |
| Theorem 4, the 36 identified (186–195) | main 1551–1566 | same decomposition 25 + 11, same reason for "five not six"; the slot rule is the paper's addition (SOURCES §"Interpretations" 4) | finite check, stated |
| Proposition 1, helium at 2 → E = 20 (201–205) | main 1573–1580 | same, with the mechanism ("the envelope") written as a proof | yes |
| 32-column E = 106; block coordinate E = 100 (207) | main 1582–1586; the seated three-coordinate fixture | same | E = 100 asserted, not explained (a number with a check and no argument; acceptable "for scale") |
| Theorem 5, E(n+ℓ, Z) = 0 both routes (227–237) | Index of Indices 1374–1388, 1446–1452 | source states E = 0 at 118/944 and at 120; the two proofs are the paper's own | yes |
| row coordinate from ground configurations; six differentiating-electron exceptions (241) | `LW1-ground.py`, `populate.janet_cell` (imported) | the paper's own measurement | — |
| subshell index 22/40/0 (243) | `cypher._janet` fixture | same | — |
| §5 thresholds 21, 57, 89; first occupation 21, 58, 91 (249–251) | Spectra 268–283; Math 3060–3070; Physics 478–486 | same thresholds; the first-occupation offsets are the paper's addition | — |
| Proposition 2 (253–255) | Spectra 279; Math 3068 | **source states 116 cells, medians 0.637 / 0.036, p = 9.8 × 10⁻⁴; paper prints 128, 0.6202 / 0.0335, 2.5 × 10⁻⁴** — recorded in SOURCES; see A.6 | statistic, see A-8 |
| obstacle counts 9,756 / 11,605 / 5,280 as term counts (263) | Spectra 47–52 | counts the source's; the identification with term maxima is the paper's | see A-2 |
| Theorem 6 term tables (273–285) | Math 742–754 (Condon & Shortley ch. VII; Racah 1943) | paper computes the full p, d, f tables; source states only d⁴ = 16 | **no** — see A-4 |
| Corollaries 1, 2 (289–291) | Spectra 256 ("one series per parent, all interleaved") | Corollary 1's "exactly one series per ℓ" is the source's sentence | follow from Theorem 6 |
| Proposition 3 (293–297) | `compendia4.py` header (the ruled criterion) | **stated as an equivalence; source records only the criterion** | **no** — see A-3 |
| §7 data counts (303) | Spectra 973–1027 | same to the row | — |
| Table 2 conventions 80 / 9 / 20 / 30 / 457 (305–316) | `compendia3.PARENT`, `compendia4` note (139 vs 80) | the 30/9 split is the paper's own reading | — |
| Table 3 core classes (320–330) | the paper's own, from `LW1` + three overrides | — | — |
| Proposition 4 (332–334) | `compendia4.py` header | true, but see R-20 | — |
| Table 4, four species (342–351) | `compendia4` selftest fixtures | same | — |
| ceiling IV (353) | Spectra 268, Math 750 ("no open-shell ion above charge 6") | **source not reproduced; paper prints the measured IV** — correctly handled, see A.7 | — |
| measurable-cells chain 61,152 → 11,416 → 4,395 → 1,755 (355) | Spectra 258–261 | **numbers reproduce; the stated cuts do not** — see A-1 | — |
| §8 repeats (363–373) | `compendia4` fixtures | same | — |
| §9 bracket figures (383) | Spectra 297, 1000–1004; main 1633–1646 | same | — |

### A.2 Every printed number against the check's output

Every number below was matched to a line of `check.py`'s output (the `--selftest` log). Numbers with
no assertion behind them are listed at the end.

| where | numbers | check line |
|---|---|---|
| abstract, §0 table, Thm 3 | 90, 126, 36; 118, 224, 106; 118, 944, 0; 120, 960, 0 | B "(period, group): 90 cells, box 126, E = 36"; "32-column layout: 118 cells, box 224, E = 106"; C "(n+l, Z): 118 cells, box 944, E = 0"; "120 cells, box 960, E = 0" |
| §0, Thm 4 | 16 + 10 + 10; 1d 10, 1p 5, 2d 10 = 25; 3d 10, 1s 1 = 11 | B "the 36 are period 1 groups 2-17…"; "36 = 25 forbidden … + 11 deferred"; I "25 + 11 = 36 and 16 + 10 + 10 = 36" |
| Prop 1 | E = 20, 110, 16 | B "helium drawn at group 2: 90 cells, E = 20"; `periodic_he_cost` |
| §3 | E = 100 with block | B "with a block coordinate adjoined … E rises to 100" |
| §2 guards | 300, seed 7, 3,578, 0, 2,007 | D two GUARD lines |
| §2 obligations | 13 discharged; boxes | D thirteen MACHINE-CHECKED lines |
| §4 | rows 2,2,8,8,18,18,32,30; openings 1,3,5,13,21,39,57,89; ends 2,4,12,20,38,56,88,118; 6,903 pairs; 108/0; six exceptions 25,30,43,47,48,80; (3,13) → 0; (5,30)→(2,30) → 54; 22/40/0 | C, all present |
| §5 | 21, 58, 91; 148, 128, 7, 121; 0.6202, 0.0335; U = 74, z = −3.66, p = 2.5 × 10⁻⁴; seven defects; 0.9084, 0.7559; 0.0618; 104,832; 9,756, 11,605, 5,280; 5/8/16; 7/17/47/73/119 | H and G lines |
| Thm 6 | 17,476; Table 1 rows | E "p^k terms …; d^k …; f^6 = f^7 = f^8 = 119 (17476 determinants)" — **the f-row entries 7, 17, 47, 73 and the p/d rows are asserted; the f-row entries at k = 2…5 and 9…14 are not asserted in E** (A-13) |
| §7 | 596, 119, 70, 28, 3,342, 2,269; 80/9/20/30/457, 139, 59; 38/159/174/127/98; 5/2/77/55; 371, 7, 225, 132, 93; 13 species | F lines |
| Table 4 | limits, separations 17,550; 780.34, 217,047.60; 25,840.700; 287.240; rows 20/2, 4/2/1, 29/8, 15/18; 99 | F lines; **the per-limit assignment of rows is asserted only as a sorted multiset** (A-12) |
| §7 ceiling | IV, Al IV, Fe XV, Fe XVI; 61,152; 11,416; 4,395; 1,755; 2,640 | F last line; G chain line — **with cuts other than the paper states** (A-1) |
| §8 | 4 Ar II pairs, 44 rows; 5–7/8–22, 6–8/9–23; two Si I keys; +0.0126/+0.0129, +0.0570/+0.0573 | F lines |
| §9 | 225, 93, 2,269, 1,577/1,738/392, 78, 126 | F bracket line |
| §10 | 101, four controls; 26,641 | summary; I last line |

Numbers with no assertion: "francium" at (7, 1) (true; a fact, not a check); "a factor of 10.0" (line
261 — `ratio_ti_sr` is recorded by `num` and asserted by no `rec`); Figure 5's "217,048" and "25,841"
(rounded from 217,047.60 and 25,840.700, printed nowhere else). See A-13.

### A.3 The three closure theorems

**Theorem 1 (chain).** Complete. The enumeration x⁽¹⁾ < ⋯ < x⁽ᴺ⁾ is well defined because a finite chain
of distinct cells is totally ordered; coordinate monotonicity in t follows; tᵢ exists because xᵢ ∈ Âᵢ(X);
{t : x⁽ᵗ⁾ᵢ ≤ xᵢ} = {1, …, tᵢ} uses monotonicity and the choice of tᵢ as the largest index; the
identification of φ̂ᵢⱼ(xⱼ) with x⁽ᵗʲ⁾ᵢ is correct; the choice of m with t_m minimal and the two
inequalities at (i, m) close the argument. No step assumes anything undefined.

**Theorem 2 (bi-monotone).** Complete. It uses that (a, b) ∈ ℛ(X) lies in Â₁(X) × Â₂(X), so φ̂₁₂(b) is
defined and attained; the isotone step y₁ ≤ F(y₂) ≤ F(b) is right. Line 150 then says ℛ recovers
"precisely" such pairs — a converse that is true for d = 2 (ℛ(X) is itself of Theorem 2's form with
F = φ̂₁₂, G = φ̂₂₁, both isotone by D3) but is not stated or proved (A-19).

**Lemma 3 (corners).** Complete.

**Their machine checks.** The encodings (`obl_chain`, `obl_bimonotone`, `obl_corner`, lines 326–366 of
`check.py`) are the operators the paper defines: `chain_formula` forbids two incomparable cells,
`closed_under_R` is "in_R(c) ⇒ X[c]" over the box, `obl_corner` concludes in_R for every cell, and
`obl_bimonotone` defines X from unknown isotone integer tables F: {0..n₂−1} → {0..n₁−1} and
G: {0..n₁−1} → {0..n₂−1}. Every hypothesis carries `PROVER.observed(X)` — every coordinate value
realised — which is D2's box = Â(X) and is necessary for `in_R` over the fixed box to coincide with D4;
the paper does not say so (A-7). All thirteen returned `unsat`. The two guards run before any obligation
and, if either fails, the obligations are withheld (lines 421–423): confirmed. What the guards actually
test differs from the paper's description (A-5, A-6).

### A.4 The thirty-six

Under the slot rule stated at line 186 (ℓ = 0 for g ≤ 2, ℓ = 2 for 3 ≤ g ≤ 12, ℓ = 1 for g ≥ 13,
n = p) each of the 36 cells of ℛ(X) ∖ X was checked: period 1 groups 3–12 → (1, d), forbidden, 10;
groups 13–17 → (1, p), forbidden, 5; group 2 → (1, s), deferred, 1; period 2 groups 3–12 → (2, d),
forbidden, 10; period 3 groups 3–12 → (3, d), deferred, 10. Totals 25 + 11 = 36, as `slot()` in
`check.py` also finds. The "five rather than six" sentence is the source's and is right. Correct.

### A.5 The census and the definition of "ambiguous"

The 596 rows parse as the check says; the independent reader (`compendia4.rows`) returns the same row
indices. The five-way split 80 / 9 / 20 / 30 / 457 was recomputed from `label_convention`; the
`JJPAIR` regex `\(\s*\d+/\d+\s*,\s*\d+/\d+\s*\)` is what separates the 30 jj pairs from the 9 run-on
configurations, and I found no label that would be misfiled by it. The core classes were re-derived
for all 70 species (listing in the auditor's scratch): every core configuration the check builds from
the neutral-atom table at the core's electron count is the ion's true ground configuration, and the
three overrides (Ti IV 3d, Zn III 3d¹⁰, Hg III 5d¹⁰) are exactly the three needed — Cd II (4d¹⁰5s),
Ga III / Ge IV / Zn II (3d¹⁰4s), Bi III (5d¹⁰6s²), Ba IV (5p⁵) all come out right without one.
"Names a parent" is operationally "the label contains a parenthesis" (line 779 of `check.py`); the 7
single-level rows that "write one anyway" are C II's 5 and Ga II's 2 (A-24).

"Ambiguous" (line 293, SOURCES "Interpretations" 1) = the species prints two limits and the row names
no parent. That is the criterion the compilation itself was labelled to — `compendia4.py`'s header
records that exactly the rows meeting it (Ba III 12, Ne II 37, Si I 14, Ne I 3) were given a parent —
so Proposition 4 confirms that a labelling rule was applied without exception rather than discovering a
property of spectra (R-20). The weaker reading (core has two levels, no parent written) gives 93 rows,
and the paper prints both, as SOURCES says.

### A.6 The collapse statistic

The sample is what the paper says: of the 148 measured cells with ℓ ∈ {2, 3} in the coordinate index,
the 128 with `populate.core_p(core, ℓ) = 0`, p read from the observed ground configuration of the core
(register-free: `config_of(core, "observed")`), split at Z ≥ 21 (ℓ = 2) / Z ≥ 57 (ℓ = 3). The seven
"collapsed" cells are (21,3), (22,3) ×2, (22,4), (26,8), (26,15), (26,16), all ℓ = 2. The medians are
right. The U statistic is right: U = min(U₁, n₁n₂ − U₁) = 74, i.e. the collapsed value exceeds the
uncollapsed one in 773 of the 847 pairs. **The p-value is the tie-corrected normal approximation with no
continuity correction** (12 ties among 128); the paper calls it "a two-sided Mann–Whitney test" and does
not say so. The exact two-sided p (enumerating the U distribution, n₁ = 7, n₂ = 121, ties ignored) is
3.4 × 10⁻⁵. The conclusion is unchanged; the description is not what was computed (A-8). The reported
z = −3.66 is negative by the min-U convention, not by direction.

The 128 are index cells keyed (Z, charge, 2S+1, ℓ) — "Ti III nd at two multiplicities" is two cells —
not channels in the sense of D6, which carry a parent (A-17).

### A.7 The three source claims SOURCES.md says do not reproduce

1. **116 / 0.637 / 0.036 / 9.8 × 10⁻⁴.** None of the four figures appears in `PAPER.md` (grepped; the
   one "0.036" is Li I's limit gap). The paper prints the measured 128 / 0.6202 / 0.0335 / 2.5 × 10⁻⁴
   and the split 7 / 121. Handled as the contract requires. SOURCES' guess at the cause ("likeliest")
   is labelled as a guess. Correct.
2. **"No open-shell ion above charge 6."** The paper prints "no core with more than one level above
   spectrum number IV" and names Fe XV and Fe XVI; both are true of the table (F, last line). Correct
   — but line 353's "which is what Corollary 2 predicts" is not (A-23).
3. **Fe IV.** Not printed anywhere; the term count d⁴ = 16 is printed and checked. Correct.

**A fourth discrepancy SOURCES does not record.** The measurable-cells chain (A-1).

### A.8 The thirteen Z3 obligations

Read in full. Encodings faithful to D3–D4 (A.3). Both guards run first; obligations withheld on
failure. The guard's content is narrower than the paper's account: see A-5 and A-6. Independently,
the auditor evaluated (i) `R_ref` (written from D3–D4), (ii) the seated `op_order`, and (iii) the
actual Z3 term `PROVER.in_R` under `z3.simplify` with X substituted, on the guard's own 300 draws
(seed 7): 3,578 cell decisions, 0 disagreements between any pair. So the encoding is sound; only its
description in the paper is off.

### A.9 Figures

- **Figure 1** (audited plate, `figure-6.2.png`): 90 blue, 36 red in the right pattern, 126 cells.
  **The red title "36 cells the structure admits and the table denies" is drawn across the first row of
  cells and overprints them** — visible in the PNG and on page 7 of the render (A-15).
- **Figure 2**: matches Theorem 4 and Proposition 1 cell for cell (1s gold at (1, 2), 1d/1p/2d red,
  3d gold; right panel twenty gold at periods 2–3, groups 3–12).
- **Figure 3**: matches; row lengths and box sizes as printed.
- **Figure 4**: eight rows with openings 1, 3, 5, 13, 21, 39, 57, 89; 128 points; seven orange at
  Z = 21–26; the largest point at Z = 20 (Ca I) is blue, as the text says. Matches. One f-channel
  point sits at δ ≈ −0.24 (Fe XV nf, −0.2367 in the data); the text does not mention a negative
  defect in the sample — not a defect of the figure.
- **Figure 5**: left panel 38/159/174/127/98 with 5/2/77/55 blue; right panel four species, parents
  and row counts as in Table 4 (Ba III 20 at ²P°₃/₂, 2 at ²P°₁/₂; Si I 15 at ²P°₁/₂, 18 at ²P°₃/₂ —
  the auditor confirmed the per-limit assignment from the table since the check pins only the
  multiset). Spans printed as "217,048" and "25,841", rounded numbers the check does not print (A-13).
- `FIGURES.tsv` md5s match the files (`md5sum` agrees on all five).

### A.10 Lint

0 hits. But `lint.py` does not test the contract's status vocabulary: the paper uses **MEASURED**,
which PAPER-SPEC §5 does not list and §8 forbids as a work label ("MEASURED-as-a-label"), and does not
use SAMPLED though the fidelity guard is a seeded sample of 300 (A-10).

### A.11 Typography of the render (18 pages read)

- **Underscore fallbacks in prose**: `x_d` (p. 4, D1); `E_n`, `δ_n` (p. 4, D6); `M_L`, `M_S` (p. 4,
  D7; p. 11, Thm 6 four times); `m_ℓ`, `m_s` (p. 11); `t_m`, `x_m`, `x⁽ᵗᵐ⁾_m` (p. 5, Thm 1 proof);
  `a_min`, `a_max`, `b_min`, `b_max` (p. 6, Lemma 3, nine times); `y_j`, `x_j` (p. 6); `j_core`
  (p. 2, §0). Every one is a literal underscore on the page.
- **Caret fallbacks**: `ℓ^k`, `p^k`, `d^k`, `f^k` (p. 1 abstract, p. 11 Theorem 6 heading, Table 1
  header and row labels, p. 16 verification record) — thirteen on the page.
- Figure 1's title overprints its top row (p. 7).
- Page 6: §3's heading and its one paragraph sit at the foot above ~45 % blank page because Figure 1
  moved to page 7; page 3 leaves its lower third blank before §1. Not orphaned headings, but a
  print-layout defect (A-16).
- Tables: no clipped cell; Table 1's last column wraps "17, 7, 1, 1" onto two lines but is legible.
  Superscripts in term symbols (²P°₃/₂, ¹S₀, ²ˢ⁺¹L) render as real Unicode. `unsat`/`sat` in
  monospace. No stray asterisks or backslashes.

### A-findings

| id | line | severity | finding | resolving change |
|---|---|---|---|---|
| A-1 | 355 | **BLOCKING** | The measurable-cells chain is printed with the source's cuts — "61,152 have Z ≤ 92; of those 11,416 also have core charge ≤ 10; of those 4,395 also have ℓ ≤ 4" — but `check.py` reproduces 11,416 only as **Z ≤ 83 and charge ≤ 10**, and 4,395 only as **Z ≤ 83, charge ≤ 6, ℓ ≤ 4** (lines 950–960); its own next line shows the paper's stated cuts give **12,720 and 7,135**. The paper prints numbers whose stated procedure the check refutes, and SOURCES.md lists the chain under "Reproduced exactly". | Either print the cuts the check applies (Z ≤ 92: 61,152; Z ≤ 83 and spectrum number ≤ 10: 11,416; Z ≤ 83, spectrum number ≤ 6, ℓ ≤ 4: 4,395; and a single-term core: 1,755) with the "single term" qualified per A-2, or delete the paragraph. Move the item in SOURCES.md to "Stated by a source and NOT reproduced" with 12,720 / 7,135 beside the stated cuts. Drop "where series resolve" unless a check supports it. |
| A-2 | 263, 355 | MAJOR | The obstacle-count identification (§5) and the single-term cut (§7) recompute each cell's core with `populate.aufbau_config` — the Madelung-order configuration — not the ground configuration D8 defines. Under the observed configurations the single-term cut is **1,925**, not 1,755 (the cores Pd, Ce, Pt differ), and the paper never says which rule is in force. | In §5 and §7 say "with the core configuration taken in Madelung order, as the index itself was built" and note that D8's ground configuration would give 1,925; or recompute under D8 and print that. |
| A-3 | 293–295, and 3, 11, 37 | **BLOCKING** | Proposition 3 is stated as "if and only if" and proves only sufficiency; "necessity" is one witness (Ba III), and the direction is false in general — a stripped (ℓ, term/K, J) label is admissible on one parent only whenever the K or J value cannot couple to the other core J (K = 7/2 with ℓ = 2 needs J₁ = 3/2). The thesis (line 3 "ambiguous exactly when"), abstract (line 11) and §0 (line 37) repeat the equivalence. | Restate: "If the species prints one limit at that (ℓ, term), the channel is determined. Two limits do not by themselves leave it undetermined; the label can fail, and does — Ba III's `nd 2[3/2]* J=2` at both limits." Replace "exactly when" by "when" at lines 3, 11, 37 and give the Ba III witness its own status (REFUTATION of "the outer label determines the parent"). |
| A-4 | 283, 285, 404, 411 | MAJOR | Theorem 6 is marked PROVED but the proof's load-bearing step — that the entry of largest M_S then largest M_L is the (L, S) of a term whose full rectangle is present, so that the peel removes exactly one term per pass — is asserted and then delegated to "asserted at every decrement" in the run. Also the f-row (7, 17, 47, 73, 119) is CITED to Condon & Shortley 1935, who tabulate pⁿ and dⁿ but not fⁿ. | Add the highest-weight argument (a state at maximal M_S and, within it, maximal M_L is annihilated by S₊ and L₊, hence belongs to a term with S = M_S, L = M_L, which contributes one state to every cell of its rectangle; induct on the total) or mark Theorem 6 EXHAUSTIVE only. Cite Nielson & Koster (1963) for the fⁿ row. |
| A-5 | 160, 414 | MAJOR | The fidelity guard is described as evaluating the witness form "against the closure computed directly from D3 and D4". `guard_encoding` (check.py 369–391) compares a Python transcription of the witness form against the **seated** `op_order`; `R_ref`, the D3–D4 implementation, is compared with the seated operator on the paper's two indices only; the Z3 term itself is never evaluated. (The auditor's re-run shows all three agree on the 300 draws, so the guard is sound; the sentence is not what it does.) | Either reword ("against an independently implemented staircase operator, itself checked against D3–D4 on the two indices of §3–§4") or extend `guard_encoding` to compare `R_ref` and `z3.simplify(in_R(...))` on the same draws and print the three counts. |
| A-6 | 160, 414 | MAJOR | "The non-vacuity guard checks that each hypothesis is satisfiable …" — it is run for the chain hypothesis on 3×3 and 3×3×3, for the corner hypothesis on 4×4 and for the bi-monotone hypothesis on 4×4 (check.py 405–418): four (hypothesis, box) pairs for thirteen obligations. PAPER-SPEC §6 requires both guards per obligation. The 7×18 corner obligation, the one §3 rests on, has no non-vacuity check of its own. | Run `non_vacuous` for every (hypothesis, box) pair in the obligation lists before `prove`, and print thirteen guard lines; or state in §2 and §10 exactly which four boxes the guard covered. |
| A-7 | 156, 168, 396–398 | MINOR | "quantify over every subset X of the box" / "over all 2¹²⁶ subsets": every hypothesis includes the condition that X realises every coordinate value (so that the fixed box is Â(X), D2). The count of subsets satisfying the hypothesis is smaller than 2¹²⁶, and the theorems' generality over non-observing X is covered only through smaller boxes. | Say "every subset that realises every value of both coordinates — the box is then its own Â(X) by D2" and drop "all 2¹²⁶". |
| A-8 | 54, 253, 418 | MAJOR | The p-value 2.5 × 10⁻⁴ is a tie-corrected normal approximation without continuity correction, on n₁ = 7; the paper says only "a two-sided Mann–Whitney test". The exact two-sided p is 3.4 × 10⁻⁵. The sign of z follows the min-U convention and carries no direction; the direction (collapsed larger in 773 of 847 pairs) is not printed. | Print "normal approximation with tie correction" and add the exact p, or print the exact p alone; give U₁ = 773 of 847 (or the probability 0.913) as the direction. Mann and Whitney (1947) for the exact distribution. |
| A-9 | 11, 52, 305 | MAJOR | "A parent is written in five distinct conventions" (abstract), "A parent may be written in five conventions" (§0), "Table 2 — the five conventions in which a parent is written": Table 2 lists four conventions that write a parent and a fifth row that writes none. | "four conventions, and a fifth in which no parent is written"; retitle Table 2 "the four conventions in which a parent is written, and the rows that write none". |
| A-10 | 65–74, 255, 410, 418 | MAJOR | Status vocabulary departs from PAPER-SPEC §5 ("exactly these, never merged"): **MEASURED** is added — and §8 lists "MEASURED-as-a-label" among forbidden work labels — while **SAMPLED** is dropped although the fidelity guard is a seeded sample of 300. | Mark the enumeration behind Proposition 2 EXHAUSTIVE over the 128 cells (as `check.py` itself does) and report the statistic as a number with its approximation; label the 300-draw guard SAMPLED (size 300, seed 7) in §2 and §10; delete the MEASURED row. |
| A-11 | check.py 1064–1065 | MINOR | Section I's first obligation is labelled "944 − 944 = 0" and "126 − 106 = 20"; the true subtractions are 118 − 118 and 110 − 90, and the assertion `126 − 106 == 20` tests nothing the paper claims. | Correct the label to "118 − 118 = 0, 110 − 90 = 20" and assert exactly those two subtractions from the computed |ℛ(X)| values. |
| A-12 | 346, 349 | MINOR | Table 4's "rows at each" (Ba III 20 / 2; Si I 15 / 18) is asserted only as sorted multisets (`sorted(bylim[...].values())`); which limit carries 20 or 15 is not pinned. The auditor confirmed the assignments from the table. | Assert `bylim["Ba III"]["289,100.000"] == 20` and `bylim["Si I"]["65,747.760"] == 15`. |
| A-13 | 261, 281, Figure 5 | MINOR | Three printed numbers have no assertion: "a factor of 10.0" (recorded by `num`, no `rec`); Table 1's f-row entries at k = 2–5 and 9–14 are asserted only through §G's set of term counts; Figure 5 prints "217,048" and "25,841", rounded values printed nowhere else and not produced by the check. | Add `rec`s for the ratio and the full f row; print the spans in Figure 5 as the check prints them (217,047.60; 25,840.700) or to the nearest wavenumber with the rounding stated in the caption. |
| A-14 | pp. 2, 4, 5, 6, 11, 16 | MAJOR | Underscore and caret fallbacks in prose (list in A.11): x_d, E_n, δ_n, M_L, M_S, m_ℓ, m_s, t_m, x_m, a_min/a_max/b_min/b_max, y_j/x_j, j_core; ℓ^k, p^k, d^k, f^k. The brief makes any such fallback a finding. | Write x_d as xd with a real subscript (x_𝑑 → xₔ is unavailable; use "x = (x₁, …, x_d)" → "(x₁, …, xd)" with d in italics, or rename the last coordinate), Eₙ, δₙ, M_L → M_L in Unicode is unavailable — use ML/MS with italic L, S or "M(L)", mℓ, mₛ, tₘ, xₘ, a_min → a₋, a₊ (or amin with small caps), yⱼ, xⱼ, j(core); ℓᵏ, pᵏ, dᵏ, fᵏ. Where the render script converts `_x` in code spans, the fix may belong in `render.py`. |
| A-15 | 176, Figure 1 | MAJOR | The plate's red title is drawn over the first row of cells and overprints ten of them (page 7). | Regenerate Figure 1 from `figures.py` with the same data (`periodic_cells`, `E_of`), or crop the title band; update `FIGURES.tsv` (made_by, md5). |
| A-16 | pp. 3, 6 | MINOR | §3's heading and its one paragraph are stranded at the foot of page 6 over ~45 % blank page; page 3's lower third is blank. | Let Figure 1 float above the §3 heading or force a page break before §3; check page 3 after the other fixes. |
| A-17 | 54, 60, 253, 259, 410, 418 | MINOR | "128 measured d and f channels": they are index cells keyed (Z, charge, 2S+1, ℓ) — Ti III nd is two of them — not channels in D6's sense, which carry a parent. | Say "cells" (or "multiplicity-resolved series") throughout §5, Figure 4's caption and §10. |
| A-18 | 100 | MINOR | D7: "the number of distinct (L, S) pairs, counted with multiplicity" — distinct and with multiplicity contradict. | "the number of (L, S) pairs in the decomposition of its (M_L, M_S) table, a pair counted as often as it occurs". |
| A-19 | 124, 150 | MINOR | Lemma 2's "Monotonicity in X is immediate" needs its one line (X ⊆ X′ gives Âᵢ(X) ⊆ Âᵢ(X′) and φ̂ ≤ φ̂′ on Âⱼ(X), so ℛ(X) ⊆ ℛ(X′)). Line 150's "precisely a pair of isotone bounds" asserts the converse of Theorem 2, which holds for d = 2 (ℛ(X) is of Theorem 2's form with F = φ̂₁₂, G = φ̂₂₁) but is neither stated nor proved. | Add the line to Lemma 2; add a one-sentence Remark after Theorem 2 with that proof, and say "for d = 2". |
| A-20 | 295 | MINOR | The stripping in Proposition 3's proof removes a parenthesised group at the start of the label (`compendia4.PREFIX`); jj-pair labels, whose parent J sits mid-label, are not stripped, so "exactly two keys" is a statement under a partial normalisation. | Say "stripping the parent prefix of the three prefix conventions (the jj pair carries its parent's J in the pair itself and is left intact)". |
| A-21 | 11, 28 | MINOR | "machine-checked … over every subset of six boxes" — Theorem 1 over six, Theorem 2 over three, Lemma 3 over four. | "over every subset of up to six boxes per obligation (Table, §2)". |
| A-22 | 98, 303, 353 | MINOR | "core charge z" (D6), "core charge" (§7 column), "charge 16 / charge 4" and "spectrum number IV" are used interchangeably without one definition (z = spectrum number = ionic charge + 1). | Define once in D6: "z, the spectrum number, is the charge seen by the outer electron". |
| A-23 | 353 | MINOR | "The compilation reaches charge 16 and stops at charge 4 for multi-level cores, which is what Corollary 2 predicts": Corollary 2 predicts interleaved series, not a charge ceiling; the ceiling is a fact about which species were captured (SOURCES says the source's own "charge 6" does not reproduce either). | Delete "which is what Corollary 2 predicts…" or replace with "a fact about which series were captured". |
| A-24 | 41–48, 322–330 | MINOR | "label names a parent" is operationally "the label contains a parenthesised group"; the 7 single-level rows that name one are C II (5, a closed-shell core written as `2s2(1S)`) and Ga II (2). | State the operational rule in §7 and name the two species. |

---

## Part B — reader audits

### B.1 A mathematician (lattice theory, order, combinatorics), new to the material

I read §1–§4 and §10 as a referee for *Order* would. The objects are defined before use; D1–D5 are
clean and the closure operator is genuinely a closure operator (Lemma 2's proof of idempotence is
correct and pleasant — the equality of the two bound families is the right thing to prove). Theorem 1,
Theorem 2 and Lemma 3 are proved; I checked each step and found no gap other than the ones below. What
I would reject is not a proof but the framing.

- **R-1 (line 3, 11, 37, 293–295) — BLOCKING.** Proposition 3 is announced as an equivalence and the
  "only if" is not a proof: one witness shows the label *can* fail to determine the channel, not that
  it *must* whenever two limits are present. As stated the direction is false (a K or J value that
  couples to one core J only determines the parent). Same as A-3; the change is the one given there.
- **R-2 (line 227–239, and 3, 11, 21–28) — BLOCKING.** The paper's headline contrast — E = 36 on
  (period, group) against E = 0 on (n + ℓ, Z) — compares two different *second* coordinates, and Theorem
  1 makes the second result automatic: any partition of Z into contiguous blocks laid out in increasing
  order is a chain on (row, Z). The eighteen-column table's own periods are such a partition; I
  computed (period, Z) with `E_of`: 118 cells, box 826, E = 0. Conversely the left-step table on its own
  drawn coordinates (row, column, right-justified in 32 columns) holds the corners (1, 32) and (8, 1),
  so by Lemma 3 it admits its whole 256-cell box: E = 136. So E distinguishes *group* from *Z* as a
  coordinate, not Mendeleev's table from Janet's; the abstract's "the elemental index itself … closes with
  defect zero on (n + ℓ, Z)" and the §0 table invite the other reading, and "the box on the right is
  more than seven times larger" (Figure 3) compares boxes over unlike coordinates. *Change:* add the row
  "(period, Z) · 118 · 826 · 0" to the §0 table; state after Theorem 5 that closure on (r, Z) holds for
  every contiguous-block presentation, the eighteen-column table's periods included, and that the
  left-step table on (row, column) has E = 136 by Lemma 3; rewrite the thesis and abstract to claim what
  is shown — E on (period, group) counts the gaps the group coordinate creates, and against Z any
  monotone row coordinate closes — and call the closed object "the (n + ℓ, Z) presentation" rather than
  "the left-step table".
- **R-3 (line 273–285) — MAJOR.** Theorem 6 carries PROVED with a proof that outsources its only
  non-trivial step to a runtime assertion. Same as A-4.
- **R-4 (line 124, 150) — MINOR.** Monotonicity of ℛ deserves its line; "precisely" after Theorem 2
  asserts an unstated converse. Same as A-19.
- **R-5 (line 100) — MINOR.** "distinct … counted with multiplicity" (A-18).
- **R-6 (line 156, 168) — MINOR.** The machine check's hypothesis includes "X realises every coordinate
  value"; say so, and stop counting 2¹²⁶ (A-7).
- **R-7 (line 126) — MINOR.** "the reason a *drawn* band never has a defect" — "drawn band" is defined
  nowhere in this paper; the sentence reads as a reference to something the reader has not seen.
  *Change:* either define ("an index that is itself of the form ℛ(Y) for some Y") or delete the sentence.
- **R-8 (line 213–217) — MINOR.** "2k′² for k′ = 1, 1, 2, 2, 3, 3, 4, 4, which is arithmetic" — the
  paper checks eight products and calls it arithmetic; fine, but the reader is not told that the pairing
  k′ = ⌈r/2⌉ is where the content lies (it is the n + ℓ rule's own statement, Löwdin's question). One
  clause: "with k′ = ⌈(n + ℓ)/2⌉ — the pairing is the whole of what is unexplained".

### B.2 An atomic physicist who works with NIST spectra, LS coupling and parent terms

The atomic physics is mostly read correctly: the four two-limit species are the textbook cases (inverted
²P° doublets for the p⁵ cores of Ne II, Ba IV and the Ne I inner-shell limit; the normal doublet for
Si II's 3p; Ne III's ³P and ¹D as two terms of 2p⁴), Ti IV's 3d ground state and the d¹⁰ ground states of
Zn III and Hg III are the right corrections, and the Ba III reading — one hole in 5p⁵, one term, two
levels, the K = 3/2 label admissible on J₁ = 3/2 and on J₁ = 1/2, hence two channels — is correct.
The census's core configurations for all 70 species are the ions' true ground configurations (I checked
every one). What is overstated is the rule itself, one sentence in §5, the provenance, and the
"exactly".

- **R-9 (line 3, 11, 269–271) — MAJOR.** "One series per parent term … each converges on its own
  limit" is not how the literature states it and is not how the paper's own D6 states it. Since Russell
  and Saunders, Hund and Condon & Shortley the statement is: series are built on parent *levels*, each
  parent level is an ionisation limit, and within one parent level and one ℓ there are several series —
  one per (K, J) in Racah's J₁ℓ coupling (Racah 1942, *Phys. Rev.* **61**, 537), which is exactly the
  `2[3/2]°` notation Table 2 uses. The paper's own data say so: 20 Ba III rows converge on the ²P°₃/₂
  limit. A term with two levels gives two limits, so "per parent term" and "its own limit" contradict
  each other. *Change:* "series built on different parent levels converge on different limits; within a
  parent level and an ℓ there are several series, one for each allowed (K, J), all with that level's
  limit" — and cite Racah 1942 for the pair-coupling notation.
- **R-10 (line 261) — MAJOR.** "a contrast between species that differ in nothing else the index
  records: Ti IV nd is 0.6202 and Sr II nf is 0.0618 … and both have p = 0" — Ti IV (Z = 22, spectrum
  number 4, ℓ = 2) and Sr II (Z = 38, 2, ℓ = 3) differ in every coordinate the index records. More
  seriously, the seven "collapsed" cells are all ions at spectrum numbers 3–16, while 63 of the 121
  "below" cells are neutral or singly ionised; ionisation stage is what the collapse literature (Griffin,
  Andrew & Cowan 1969; Connerade 1978) identifies as moving the collapse to lower Z — which is why Ba II
  nf is 0.7559 at Z = 56. The split is therefore confounded with charge, and Fe XV nd = 0.1278 and Fe
  XVI nd = 0.0750 are in the "collapsed" class with defects smaller than Ca I's. *Change:* delete the
  sentence; print the charge distribution of both classes beside Proposition 2; say the split controls
  for ℓ and p but not for ionisation stage; where a same-charge comparison exists, give it (Ca II nd
  0.6341 at Z = 20 against Sc III nd 0.6533 at Z = 21 is the honest pair).
- **R-11 (line 11, 346, 363) — MAJOR.** "17,550 cm⁻¹ apart, exactly the fine-structure interval of
  the core's ²P° term": the two printed limits are round to 50 cm⁻¹ (289,100.000 / 306,650.000), the
  difference is "exact" only in rational arithmetic on those rounded values, and the equality is the
  construction — the two limits *are* the two levels — not an independent test; no Ba IV level is cited.
  *Change:* drop "exactly"; cite the Ba IV 5p⁵ ²P°₁/₂ level from NIST ASD and write "the difference of
  the printed limits, 17,550 cm⁻¹, is the tabulated ²P° interval of Ba IV to the precision the limits
  are printed at".
- **R-12 (line 303, 412) — MAJOR.** Provenance is incomplete. Kaufman & Martin (Al I–II), Kramida &
  Martin (Be I) and Sansonetti (Na I, K I) with NIST ASD cover about a third of the 70 species; nothing
  is said for Sc III, Ti III, Ti XI, Ca IX, Fe VIII, Fe XV, Fe XVI, K II, Ba III, Ne II, the S, P, N, O,
  B and C ions, Bi I–III or Ge III. The compilation's own source list names Sugar & Corliss (1985) and
  Sugar & Musgrove (1990, 1995). *Change:* cite Sugar, J. and Corliss, C. (1985) *J. Phys. Chem. Ref.
  Data* **14**, Suppl. 2 (potassium through nickel) and the Sugar & Musgrove compilations, and state
  that every other level is a NIST ASD retrieval (version 5.12).
- **R-13 (line 249–251) — MINOR.** Goeppert-Mayer 1941 and Griffin, Andrew & Cowan 1969 do not give
  integer thresholds; the Thomas–Fermi picture (Fermi 1928 is the origin) puts the neutral-atom 4f
  collapse between Z = 56 and 58 and makes it depend on ionisation stage. *Change:* "the literature
  places the collapse near these atomic numbers; the integers are the index's row openings" and cite
  Fermi (1928) and Connerade (1978).
- **R-14 (line 52, 312) — MINOR.** The jj pair `(3/2,5/2)` is J₁j coupling notation; its first entry
  is the core's J, which fixes the parent *level* only because these cores have a single term — say so,
  and name the `2[K]` labels as Racah's J₁ℓ (jK) coupling.
- **R-15 (line 50, 332) — MINOR.** Ar II: 30 rows with no parent on a 3-term (five-level) core and
  one printed limit. NIST holds Ar II series converging on the ¹D₂ and ¹S₀ limits of Ar III; the paper's
  "prints exactly one limit" is a fact about the capture and should be illustrated with this case
  rather than left abstract.
- **R-16 (line 98) — MINOR.** D6's quantum defect is defined with "R the Rydberg constant for the
  species" — good; but the index's δ is the *mean* defect of a fitted channel (§7's column), and
  Proposition 2 uses that mean. Say in §5 that δ is the channel's mean defect as tabulated, not a
  single level's.

### B.3 A journal referee (novelty, literature, honesty of the record)

The paper is two papers: a short order-theoretic note (a closure operator on an index, three
sufficient conditions for closure, all proved and machine-checked) and a data paper on parentage in a
Rydberg compilation. The first is correct and modest; its interest depends entirely on the elemental
contrast, which R-2 shows is not the contrast the abstract sells. The second is careful with its
numbers, honest about what it did not establish (§0's list is exemplary), and undermined in three
places by claims stated more strongly than the record supports.

- **R-17 (line 21–28, 3, 11) — BLOCKING** — the framing finding R-2, restated for the abstract and §0:
  the abstract promises that the index "closes with defect zero on (n + ℓ, Z)" as a fact about Janet's
  ordering; the body proves it is a fact about Z as a coordinate. Fix as R-2.
- **R-18 (line 332–334, 50, 11) — MAJOR.** Proposition 4 ("the compilation carries no ambiguous row")
  is verified EXHAUSTIVE, and it is true — but the compilation's labelling convention is that a parent
  is written on every row of a species that prints two limits (that is how 66 rows came to carry one),
  so the proposition confirms a rule was applied without exception, not a property of the spectra. The
  §0 sentence "a measurement about this compilation, not a theorem about labels" is nearly there.
  *Change:* state the convention as a fact about the data ("the compilation writes a parent on every row
  of a species with two printed limits") and present Proposition 4 as the check that the convention
  holds on all 596 rows.
- **R-19 (line 429, 205, 213) — MAJOR.** The Janet citation is wrong: *La classification hélicoïdale des
  éléments chimiques* is the 1928 pamphlet (Beauvais, Imprimerie Départementale de l'Oise, November
  1928); the 1929 work is *Considérations sur la structure du noyau de l'atome*; the English version is
  Janet, C. (1929) *Chemical News* **138**, 372–374, 388–393 — see Stewart (2010), who is in the reference
  list and cited nowhere. And Janet's table is never described (rows of n + ℓ, blocks f, d, p, s from
  left to right, helium above beryllium); what the paper closes is (n + ℓ, Z), which is not Janet's
  drawing (R-2). *Change:* cite Janet 1928 with the right title, cite Stewart 2010 in §4, describe the
  left-step table in one sentence and say the (n + ℓ, Z) presentation is its row coordinate against Z.
- **R-20 (References) — MAJOR.** Missing standard references, with full author lists: Racah, G. (1942)
  On a new type of vector coupling in complex spectra, *Physical Review* **61**, 537–538 (the `2[K]`
  notation); Cowan, R. D. (1981) *The Theory of Atomic Structure and Spectra*, University of California
  Press, Berkeley (term counting, parentage, coupling schemes); Nielson, C. W. and Koster, G. F. (1963)
  *Spectroscopic Coefficients for the pⁿ, dⁿ and fⁿ Configurations*, MIT Press, Cambridge MA (the fⁿ
  term tables the paper attributes to Condon & Shortley); Martin, W. C. and Wiese, W. L. (1996) Atomic
  spectroscopy, in *Atomic, Molecular, and Optical Physics Handbook*, ed. G. W. F. Drake, AIP Press,
  Woodbury NY, ch. 10 (the NIST label conventions Table 2 parses); Sugar, J. and Corliss, C. (1985)
  Atomic energy levels of the iron-period elements: potassium through nickel, *Journal of Physical and
  Chemical Reference Data* **14**, Suppl. 2 (data provenance, R-12); Fermi, E. (1928) Eine statistische
  Methode zur Bestimmung einiger Eigenschaften des Atoms und ihre Anwendung auf die Theorie des
  periodischen Systems der Elemente, *Zeitschrift für Physik* **48**, 73–79, and Connerade, J.-P. (1978)
  The non-Rydberg spectroscopy of atoms, *Contemporary Physics* **19**, 415–447 (orbital collapse);
  Klechkovskii, V. M. (1962) Justification of the rule for successive filling of (n + l) groups, *Soviet
  Physics JETP* **14**, 334–335, and Hakala, R. W. (1952) The periodic law in mathematical form, *Journal of
  Physical Chemistry* **56**, 178–181 (the row-length formulas the paper calls "arithmetic"); Schwarz,
  W. H. E. and Rich, R. L. (2010) Theoretical basis and correct explanation of the periodic system: review
  and update, *Journal of Chemical Education* **87**, 435–443, and Scerri, E. R. (2009) The dual sense of
  the term "element", attempts to derive the Madelung rule, and the optimal form of the periodic table,
  if any, *Foundations of Chemistry* **11**, 69–79 (the left-step literature §3 and §4 enter).
- **R-21 (References) — MINOR.** Eleven references are never cited in the text: Hund 1925, Madelung
  1936, Mendeleev 1869, Pauli 1925, Racah 1942, Ritz 1903, Rydberg 1890, Seaton 1983, Stewart 2010,
  Theodosiou et al. 1986, and Kramida et al. 2024 (present only as "NIST ASD"). Cite each where it
  belongs (Rydberg and Ritz at D6; Seaton at D6; Madelung at §4; Pauli and Hund at Theorem 6; Mendeleev
  at §3; Theodosiou at §7's data; Kramida et al. at every "NIST ASD") or drop it.
- **R-22 (line 65–74, 391) — MAJOR.** The verification record's vocabulary is not the contract's (A-10),
  and "Every number printed in this paper is produced there" is not quite true (A-13). A referee
  checking the record against the check will find MEASURED undefined by the contract and three numbers
  unasserted. Fix as A-10 and A-13.
- **R-23 (line 379–385) — MINOR.** §9 rests on "a companion study in this series" that is neither
  cited nor summarised, and prints that study's numbers (1,577 of 1,738 on 392 rows; 78; 126) for a
  test this paper does not define. Either define the containment test in one paragraph or move the
  numbers out.
- **R-24 (line 353) — MINOR.** "which is what Corollary 2 predicts" (A-23).
- **R-25 (line 11, 28) — MINOR.** Abstract: "over every subset of six boxes" (A-21); abstract and §0
  otherwise promise what the body delivers.

---

## Part C — the record

| id | line(s) | severity | finding (short) | disposition |
|---|---|---|---|---|
| A-1 | 355 | BLOCKING | measurable-cells chain printed with cuts the check refutes; SOURCES misfiles it |  FIXED. §7 prints the chain with the cuts that produce it (Z ≤ 92; Z ≤ 83 and spectrum number ≤ 10; Z ≤ 83, spectrum number ≤ 6, ℓ ≤ 4), the last cut under both configuration rules (1,925 with D8's tabulated core, 1,755 in Madelung order, the 170 differing cells named), and the chain under the stated cuts beside it (61,152 / 12,720 / 7,950 / 3,550); "where series resolve" dropped. SOURCES.md moves the chain to "NOT reproduced" (item 5) and says the numbers reproduce but the procedure does not. |
| A-2 | 263, 355 | MAJOR | index-cell cores in Madelung order, not D8's ground configuration; 1,755 vs 1,925 |  FIXED. §5 and §7 state which rule is in force at each number and print both: the obstacle identification 26,641 (Madelung) / 21,271 (tabulated, with the 4,675 + 565 + 130 accounted for) and the single-term cut 1,755 / 1,925; obligations for each; §10 lists both. |
| A-3 | 3, 11, 37, 293–295 | BLOCKING | Proposition 3 "iff" — necessity unproved and false in general |  FIXED. Proposition 3 states the proved implication only (one printed limit determines the channel); the converse is said not to hold in general with the K/J reason; Ba III's label at two limits is a REFUTATION of "the outer label determines the parent" with its own status; thesis, abstract and §0 say "can fail … and does fail once", never "exactly when". |
| A-4 | 283, 285, 404, 411 | MAJOR | Theorem 6 proof incomplete; fⁿ row mis-cited to Condon & Shortley |  FIXED. The highest-weight step is written out (a rectangle containing the top entry must have its corner there, else a higher entry exists), with induction on the term count; the run's 17,476 decrements with 0 below zero and an independent second-difference count are both obligations; Theorem 6 is PROVED given the CITED multiplet decomposition, and the fⁿ row is cited to Nielson and Koster (1963). |
| A-5 | 160, 414 | MAJOR | fidelity guard misdescribed (compares seated operator, not D3–D4; Z3 term never evaluated) |  FIXED. `guard_encoding` now evaluates the Z3 term `in_R` under `z3.simplify` with the drawn X substituted, the seated `op_order` and the fresh `R_ref` on the same 300 draws and prints the three pairwise disagreement counts (0, 0, 0 over 3,578 cells); §2 and §10 describe exactly that, as SAMPLED. |
| A-6 | 160, 414 | MAJOR | non-vacuity guard run on 4 pairs, not per obligation; none for 7×18 |  FIXED. `non_vacuous` runs for every (hypothesis, box) pair — thirteen GUARD lines, the 7×18 corner box included — before any obligation; §2 and §10 say so. |
| A-7 | 156, 168 | MINOR | "every subset" / "2¹²⁶" — hypothesis includes observedness |  FIXED. "every subset X of the box that realises every value of both coordinates — so that the box is its own Â(X) by D2"; "2¹²⁶" removed; §10 says "every observing subset". |
| A-8 | 54, 253, 418 | MAJOR | p is an unnamed normal approximation; exact p = 3.4 × 10⁻⁵; z sign conventional |  FIXED. The exact permutation distribution of the rank sum over all C(128, 7) = 94,525,795,200 assignments (midranks for the 12 ties) is computed: two-sided p = 3.4 × 10⁻⁵, one-sided 1.7 × 10⁻⁵, Mann and Whitney (1947) cited; the direction 773 of 847 cross pairs is printed; the normal approximation is named as tie-corrected without continuity correction and kept for comparison; the sign of z is said to carry no direction. |
| A-9 | 11, 52, 305 | MAJOR | "five conventions in which a parent is written" — four, plus none |  FIXED. "four conventions, and a fifth class of rows writes none" in abstract, §0 and Table 2's title. |
| A-10 | 65–74, 255, 410, 418 | MAJOR | status vocabulary: MEASURED added (forbidden as a label), SAMPLED dropped |  FIXED as the contract now stands. PAPER-SPEC §5 (revised 2026-09-24) admits MEASURED as a declared status word for a paper's own measured result with its sample stated, which is how Proposition 2 uses it; SAMPLED is used for the 300-draw guard (size and seed stated) in §2 and §10; seven status words, none merged. Deleting MEASURED is declined per the revised spec. |
| A-11 | check.py 1064 | MINOR | wrong arithmetic labels in section I |  FIXED. Section I asserts 118 − 118 = 0 on (n+ℓ, Z) and on (period, Z), 110 − 90 = 20, 224 − 118 = 106, 256 − 118 = 138, each from the computed |ℛ(X)|, and E = box − cells on the three drawn tables. |
| A-12 | 346, 349 | MINOR | per-limit row counts pinned only as multisets |  FIXED. `bylim` is asserted per limit: Ba III 20 at 289,100.000 and 2 at 306,650.000; Si I 15 at 65,747.760 and 18 at 66,035.000; Ne I 4 / 2 / 1 ascending; Ne II 29 / 8. |
| A-13 | 261, 281, Fig. 5 | MINOR | three numbers unasserted (10.0; f-row; rounded spans) |  FIXED. `rec`s for the factor 10.0 and the full fⁿ row; Figure 5 prints the spans to the three decimals of the limits (17,550.000; 217,047.600; 25,840.700; 287.240) exactly as `span_labels` pins them, and the caption says so. |
| A-14 | pp. 2, 4, 5, 6, 11, 16 | MAJOR | underscore and caret fallbacks on the page |  FIXED. Every subscript and superscript is Unicode (xᵢ, Eₙ, δₙ, Mₗ, Mₛ, mℓ, mₛ, tₘ, xₘ, a₋/a₊/b₋/b₊, yⱼ, ℓᵏ, pᵏ, dᵏ, fᵏ); pypdf text of all 22 rendered pages holds 0 underscores, 0 carets, 0 backslashes. The re-render also showed the stars in Theorem 6's (μ*, ν*) read as Markdown emphasis; replaced by (μ₀, ν₀). |
| A-15 | Fig. 1, p. 7 | MAJOR | plate title overprints row 1 |  FIXED. Figure 1 is drawn by `figures.py` from `periodic_cells` and `E_of` with the title above the grid; `FIGURES.tsv` records the replacement and the plate's md5; `figures.py` re-run reproduces every md5. The five figure lines also lost their alt text, which the template was rendering as a stray "Figure n" line above each caption. |
| A-16 | pp. 3, 6 | MINOR | stranded §3 heading, blank page-thirds |  FIXED in part. §3's heading is no longer stranded (page 7 carries it with its paragraph; Theorem 3 and Figure 1 follow on page 8), and every figure sits with its caption. Page 10 still ends ~35 % blank because Figure 3 opens page 11: a float rule of the shared template, which this paper's directory may not edit. Recorded. |
| A-17 | 54, 253, 259, 410 | MINOR | "channels" for index cells |  FIXED. "cells" (keyed Z, spectrum number, 2S+1, ℓ) throughout §0, §5, Figure 4's caption and §10; Ti III nd at two multiplicities named as two cells. |
| A-18 | 100 | MINOR | D7 wording |  FIXED. D7: "the number of (L, S) pairs in the decomposition of its multiplicity table, a pair counted as often as it occurs". |
| A-19 | 124, 150 | MINOR | monotonicity line; converse of Theorem 2 |  FIXED. Lemma 2 proves monotonicity in its own paragraph; a Remark after Theorem 2 states and proves the converse for d = 2. |
| A-20 | 295 | MINOR | stripping applies to prefix conventions only |  FIXED. The REFUTATION paragraph says the stripping removes the three prefix conventions and leaves the (J₁, j) pair intact, with the reason. |
| A-21 | 11, 28 | MINOR | "six boxes" |  FIXED. "thirteen named boxes" in the abstract and §0; the table in §2 gives each obligation's boxes. |
| A-22 | 98, 303, 353 | MINOR | z / core charge / spectrum number undefined once |  FIXED. D6 defines z, the spectrum number, once, and §7 uses "spectrum number" throughout. |
| A-23 | 353 | MINOR | "which is what Corollary 2 predicts" |  FIXED. "consistent with, though not predicted by, the interleaving of Corollary 3"; the ceiling is called a fact about which series were captured. |
| A-24 | 41–48, 322 | MINOR | "names a parent" = contains a parenthesis; C II, Ga II |  FIXED. §7 states the operational rule and names C II (5 rows, `(1S)` on a closed core) and Ga II (2), with an obligation. |
| R-1 | 3, 11, 37, 293 | BLOCKING | = A-3 (mathematician) |  FIXED — as A-3. |
| R-2 | 3, 11, 21–28, 227 | BLOCKING | E = 0 on (n+ℓ, Z) is automatic for any row partition of Z; (period, Z) also E = 0; left-step on (row, column) E = 136 |  FIXED. §0's table gains (period, Z) · 118 · 826 · 0 and the left-step table on its drawn (row, column) coordinates · 118 · 256 · 138 (and 120 · 256 · 136); Corollary 1 (contiguous rows against a totally ordered coordinate) is stated and proved after Theorem 1 and run on all 117 two-row partitions; §4 closes both indices and keeps them apart; the thesis and abstract claim what is shown — Z closes under any contiguous row partition, every drawn table is a corner-filled box — and the closed object is "the (n+ℓ, Z) presentation"; Figure 3's caption says the boxes are not comparable. The title is changed to the working title "The Parent-Term Wall and the Cost of a Drawn Coordinate"; SOURCES.md records the old title for the author and the source's contrast as a finding about the source. |
| R-3 | 273–285 | MAJOR | = A-4 |  FIXED — as A-4. |
| R-4 | 124, 150 | MINOR | = A-19 |  FIXED — as A-19. |
| R-5 | 100 | MINOR | = A-18 |  FIXED — as A-18. |
| R-6 | 156, 168 | MINOR | = A-7 |  FIXED — as A-7. |
| R-7 | 126 | MINOR | "drawn band" undefined |  FIXED. The sentence now defines its object: "an index that is itself a closure — one of the form ℛ(Y) for some Y — never has a defect". |
| R-8 | 213–217 | MINOR | say where the 2k′² content lies |  FIXED. "k′ = ⌈r/2⌉, and the pairing of consecutive rows into equal lengths is where the content lies" in §4; §0 says the pairing is the whole of what is unexplained. |
| R-9 | 3, 11, 269 | MAJOR | "one series per parent term" — per level, several per (level, ℓ); cite Racah 1942 |  FIXED. D6/D7 and §6 state series per parent level, several per (level, ℓ) in Racah's pair coupling, with Racah (1942) cited (Physical Review 61, 537–538) and the compilation's own Ba III rows (20 at one limit) as the instance; the thesis says "a separate Rydberg series on each of its levels". |
| R-10 | 261 | MAJOR | "differ in nothing else" false; split confounded with ionisation stage |  FIXED. The sentence is deleted; the Ti IV / Sr II pair is kept only as "illustrates the size of the effect and controls for nothing"; the charge distribution of both classes is printed (7 collapsed at spectrum numbers 3, 3, 3, 4, 8, 15, 16; 34 neutral and 29 singly ionised among the 121), the confound is stated in §0, §5 and §10, Fe XV and Fe XVI's small defects are named, and the argon-core nd sequence K I 0.2460 / Ca II 0.6341 / Sc III 0.6533 is given. |
| R-11 | 11, 346, 363 | MAJOR | "exactly the fine-structure interval" — rounded limits, no Ba IV level cited |  FIXED in part. "exactly" is dropped; §8 says the two limits are the two levels by construction, so the difference is the compilation's fine-structure interval and not an independent test, printed "to the precision at which the limits are printed". The Ba IV ²P°₁/₂ level from NIST ASD is not cited: it could not be verified from the tree or in this session, and a number `check.py` does not produce is not printed (PAPER-SPEC §4). |
| R-12 | 303, 412 | MAJOR | provenance covers a third of the species; Sugar & Corliss 1985 missing |  FIXED. `check.py` reads the compilation's own source list: 25 of 70 species attributed by compilation (Kaufman & Martin 2, Kramida & Martin 1, Sansonetti 2, NIST ASD 20), Sugar & Corliss 1985 and Sugar & Musgrove 1990, 1995 named as additional sources, 45 species with no species-level attribution; §7 prints that and cites all of them, with NIST ASD version 5.12 (Kramida et al. 2024). |
| R-13 | 249–251 | MINOR | literature thresholds are not integers; Fermi 1928, Connerade 1978 |  FIXED. §5 says the literature places the collapse near these atomic numbers and makes it depend on ionisation stage, and does not give integers; Fermi (1928) and Connerade (1978) cited. |
| R-14 | 52, 312 | MINOR | J₁j and J₁ℓ notation named |  FIXED. Table 2's paragraph names the (J₁, j) pair as J₁j coupling, says its first entry fixes the parent level only because every such core has a single term (all 30 rows), and names the `2[K]°` labels as Racah's pair coupling. |
| R-15 | 50, 332 | MINOR | Ar II as the concrete single-limit capture |  FIXED. Ar II is the concrete case in §7 (core 3p⁴, 3 terms, 5 levels, 30 unnamed + 14 named rows, one printed limit), with an obligation. |
| R-16 | 98 | MINOR | δ in §5 is the channel's mean defect |  FIXED. D6 defines the channel's mean defect and says the compilations tabulate it per channel; §5's sample paragraph says each cell carries the mean defect of the channel fitted there. |
| R-17 | 3, 11, 21–28 | BLOCKING | = R-2 (referee) |  FIXED — as R-2. |
| R-18 | 11, 50, 332 | MAJOR | Proposition 4 verifies the compilation's labelling rule |  FIXED. Proposition 4 is "the compilation's labelling convention holds on every row"; §0 and §7 say it confirms a rule applied without exception and is not a property of the thirteen spectra. |
| R-19 | 205, 213, 429 | MAJOR | Janet citation wrong; Janet's table not described; Stewart uncited |  FIXED. Janet (1928) *La classification hélicoïdale des éléments chimiques* and Janet (1929) *Considérations sur la structure du noyau de l'atome*, both Imprimerie Départementale de l'Oise, Beauvais, as the search confirms; Stewart (2010) cited in §4; the left-step table described in one sentence (rows of n + ℓ, blocks f, d, p, s left to right, helium above beryllium); the closed object is the (n+ℓ, Z) presentation. SOURCES.md item 7 records the tree's own inconsistency. |
| R-20 | References | MAJOR | missing standard references (Racah 1942, Cowan 1981, Nielson & Koster 1963, Martin & Wiese 1996, Sugar & Corliss 1985, Fermi 1928, Connerade 1978, Klechkovskii 1962, Hakala 1952, Schwarz & Rich 2010, Scerri 2009) |  FIXED in part. Added and cited: Racah 1942 (D7, §6), Cowan 1981 (§0, §6), Nielson & Koster 1963 (Theorem 6), Sugar & Corliss 1985 (§7), Fermi 1928 and Connerade 1978 (§5), Klechkovskii 1962 (§4), Mann & Whitney 1947 (Proposition 2), Martin & Wiese 1996 (Table 2) — details verified by search or from the compilation's own source list. Declined: Hakala 1952 (the search returns the journal inconsistently, so the details are unverified; the row-length formula is presented as arithmetic given the pairing, which Klechkovskii covers), Schwarz & Rich 2010 and Scerri 2009 (the paper takes no position on the left-step table's merit, cites Scerri 2020 for helium's placement, and a reference uncited in the body is what R-21 objects to). |
| R-21 | References | MINOR | eleven uncited references |  FIXED. A script over the reference list finds every author-year cited in the body (Rydberg and Ritz at D6; Seaton at D6; Madelung at §4; Pauli at Theorem 6; Mendeleev at §3; Theodosiou at §7; Kramida et al. at §7; Racah 1942 at D7; Stewart at §4); Hund 1925 dropped. |
| R-22 | 65–74, 391 | MAJOR | = A-10 + A-13 |  FIXED — as A-10 and A-13; "Every number printed in this paper is produced there or is CITED" is now true of every number the audit listed. |
| R-23 | 379–385 | MINOR | companion study uncited; its test undefined here |  FIXED in part. §9 states the containment statement in one sentence, says the companion paper defines and tests it, and marks the column's totals as the column's own figures reproduced from it (EXHAUSTIVE over the column), with the test itself not defined or examined here. Moving the numbers out is declined: they are what the column holds and an obligation pins them. |
| R-24 | 353 | MINOR | = A-23 |  FIXED — as A-23. |
| R-25 | 11, 28 | MINOR | = A-21 |  FIXED — as A-21. |

**Counts (distinct findings; a finding raised by more than one reader is counted once):**
BLOCKING 3 — A-1; A-3 (= R-1); R-2 (= R-17).
MAJOR 16 — A-2; A-4 (= R-3); A-5; A-6; A-8; A-9; A-10 (= R-22); A-14; A-15; R-9; R-10; R-11; R-12;
R-18; R-19; R-20.
MINOR 21 — A-7 (= R-6); A-11; A-12; A-13; A-16; A-17; A-18 (= R-5); A-19 (= R-4); A-20; A-21 (= R-25);
A-22; A-23 (= R-24); A-24; R-7; R-8; R-13; R-14; R-15; R-16; R-21; R-23.
Rows in the table: 49 (24 A, 25 R); distinct findings: 40.

---

## Repair record (2026-09-24)

Written by the repairing drafter; nothing above this line was deleted or rewritten. A first repair
attempt was cut off by a session limit with `PAPER.md`, `check.py`, `figures.py` and three figures
already changed and `FIGURES.tsv` half-updated; this pass read that state, completed it, and wrote
every disposition.

**Dispositions.** 49 rows, none blank: 45 FIXED, 4 FIXED in part with the residue declined for a
stated reason (A-16, R-11, R-20, R-23). By severity over the 40 distinct findings: BLOCKING 3 —
all FIXED; MAJOR 16 — 14 FIXED, 2 FIXED in part (R-11, R-20); MINOR 21 — 19 FIXED, 2 FIXED in part
(A-16, R-23). No finding was declined outright.

**How the framing was resolved.** The paper now claims that Z, as the second coordinate, closes
under any contiguous row partition (Theorem 1, Corollary 1: the n + ℓ rows, the periods, and all
117 two-row partitions), and that every drawn table — eighteen-column, thirty-two-column, left-step
— admits its whole box on its drawn coordinates by Lemma 3, with E = box − cells (36, 106, 138). The
closure distinguishes a coordinate, not an ordering. Title changed to the working title "The
Parent-Term Wall and the Cost of a Drawn Coordinate"; the old title is recorded in SOURCES.md.

**What was run.** `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH`; `python3 check.py`
— 145 obligations, 0 failed (EXHAUSTIVE 117, GUARD 15, MACHINE-CHECKED 13), exit 0; `python3
check.py --selftest` — 151, the six negative controls each refuted, exit 0 (both detached, never
concurrent). `python3 papers/method/lint.py papers/method/07-wall-janet` — 0 hits. `python3
papers/method/render.py papers/method/07-wall-janet` — 22 pages; every page rasterised and read;
pypdf text extraction over all 22 pages: 0 underscores, 0 carets, 0 backslashes. `python3
figures.py` re-run reproduces all five md5s in `FIGURES.tsv`. The five figures were read as images
against their captions.

**Obligations gained, none weakened.** 101 → 145 (see SOURCES.md's table). Every printed number
was matched to a line of the check's output before this record was written.

**Unresolved.** One layout artefact of the shared template (page 10's blank lower third, A-16),
which this directory may not edit. The Ba IV level R-11 asks for is uncited for the reason given
in its row. Hakala 1952, Schwarz & Rich 2010 and Scerri 2009 (R-20) are not added, for the reasons
given in that row.
