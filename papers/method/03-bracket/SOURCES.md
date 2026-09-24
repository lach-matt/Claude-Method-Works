# SOURCES — paper 03, the bracket

Internal provenance map. **Not published.** Which source passages each section of `PAPER.md` draws
on, what was corrected, and every claim of the source that `check.py` could not reproduce, with the
measured value beside the stated one.

Paths are relative to the repository root.

Source files read in full for this paper:

| tag | file | passage |
|---|---|---|
| **MV** | `method/members/The_Method_1_6-2.md` | §22–§27, lines 5944–7369 |
| **MV-A** | same | Appendix A.12, A.13, lines 9973–10199 |
| **MV-D** | same | D.4.1, lines 10402–10413 |
| **MC** | `method/members/The_Method_1_6___Mathematical_Compendium-2.md` | §IV.B "The bracket — 21 objects", lines 1884–2108 |
| **PC** | `method/members/The_Method_1_6___The_Physics_Compendium-2.md` | lines 139–192 (where relativity enters; the bracket as an interface entry) |
| **SC** | `method/members/The_Method_1_6___Spectra_Compendium-2.md` | lines 935–973 (mechanisms, sources, the count paragraph) and the channel table, lines 293–935 |
| **RB** | `method/members/ruled_bracket.py` | the sealed strict test — the object under test, imported by path, never copied. The reference beside it (`check.py` `ref_series`) is written from D8 in a different form — Decimal at 40 digits, the test in δ-space with the floor mapped by Lemma 2's inverse, the floor from the decimal exponent, admissibility from T, members by n — and shares no line with RB (audit A-7); it agrees at all 1,551 cells (E1) |
| **IE** | `extracted/archives/method16-rp-b-data/LADDER-H-Ar-I-III.tsv` | NIST ASD 5.12 ionization energies, H–Ar I–III, retrieved 2026-08-10; read by E9 for the published Li III value 987,661.0139 ± 0.0009 (flag T, theoretical) |

The level tables `check.py` reads: `extracted/archives/restore-point-2-13/spectra_raw/*.tsv`
(76 tables with a threshold; 8 level tables and the cross-check file `QD-CHECK.tsv` without),
`drive/The Method Materials/` (6 tables plus `channels.py`, which carries the thresholds and the
label → species map `NAME`), and
`extracted/archives/spectra-levels-store/deliver/queue2/` (4 tables with a threshold, 57 without).
86 tables in all, covering 64 distinct spectra (E0); 74 table labels contribute cells, and those
cover 58 spectra (E2) — Si I is held as eight tables, Ne II as four, Ne I and Ba III as three, Ar II
and Ca II as two. The first draft said "86 tables, one per spectrum" and "74 spectra" (audit A-10). The fixed series list of Run A comes from `method/members/run489_final.json`
and `method/members/run489_45.json`; the channel table of **SC** supplies each row's n-range.

---

## 1 · Per-section provenance

| paper section | drawn on | note |
|---|---|---|
| Abstract, §0 | MV §22.1, §22.3, §22.6, §23.1–23.4, §23.8, §24, §25.3, §25.5; PC "the bracket" | §0's separation of *guarantee* / *failure condition* / *price* / *test* is PC's distinction between MV §22.1 (on T, cannot fail) and MV §25.6.1 (on δ, can fail), stated as the paper's own frame |
| §1 D1–D2 | MV §22.1, §22.2 Rule 2, §23.4 | R from CODATA 2018 |
| §1 D3 | SC channel table header (species · series · n · levels · interior · bracket) | a series is keyed here by (configuration prefix, ℓ, term, J), which is how the tables label it |
| §1 D4 | MV §22.1; MV-A A.12; MC "monotone interpolation bracket" | |
| §1 D5 | MV §25.6.1; PC "§25.6.1, on the defect" | |
| §1 D6 | MV §23.1; MC "the price V" | |
| §1 D7 | MV §22.5 verbatim; MC "the five-sigma admissibility threshold"; RB lines 2–6 | r = 2Z²R/(ν³σ) ≥ 5 with σ the quotation floor |
| §1 D8 | RB `run_series`; SC count paragraph ("strict interval membership, the only ε the quotation floor — half a unit in the last quoted decimal of the measured level — and admissibility per §22.5") | the rule the paper states is RB's, clause for clause: strict membership, the floor applied at both edges only, refusal when r < 5, refusals counted separately |
| §1 D9, D10 | MV §23.1, §23.8.1, §23.8.2; MC "Newton decrement", "self-concordance" | |
| §2 Th. 1, Cor. 1 | MV §22.1; MV §24 ("the TRIVIAL bracket … cannot fail"); PC registers 797/800/830 note | |
| §2 Th. 2 | MV §22.3; MV-A A.12 — the paper's proof is A.12's, written out | |
| §2 Lemma 2 | MV §25.6.1 (E decreasing in δ), stated here as a lemma because D5 needs it | |
| §2 closing paragraph | PC "the monotonicity claim is the wrong form" — δ approaches δ₀ monotonically, direction = sign(δ₂) | |
| §3 Th. 3, Lemma 3, Cor. 2 | MV §25.3, §25.5; MV-A A.13 | **sharpened — see §3 below**; Cor. 2's bound is the larger observed gap g₋ = w/2 + e, not w/2 (audit A-1, §3.3), and it is stated with its hypothesis and as a bound relative to the neighbours (audit R-11) |
| §3 Table 1 | MV §25.3's ν_fail table, reproduced exactly | |
| §3 "an observation" | MV §25.4, kept as an observation and not upgraded | |
| §4 Th. 4, Cor. 3 | MV §23.4, §23.4.1; MC "the exact price" | |
| §4 Th. 5, Cor. 4 | MV §23.2, §23.3; MC "the Rydberg floor" | |
| §4 Th. 6 | MV §23.2 Proposition 23.1, proof reproduced and extended with V = 2(1+t)/(1−t); MC "the floor at two" (Jensen 1906) | |
| §4 Th. 7 and the remark | MV §23.5, §23.5.1, §23.5.2; MC "the width-price front" | **the source's own withdrawal governs — see §2 below** |
| §4 Th. 8, Table 2 | MV §23.1, §23.9.1, §23.9.2; MC "the four-thirds law" | **corrected — see §3 below** |
| §4 Th. 9 | MV §23.6; MC "the fractional widths" | |
| §4 Prop. 1 | MV §23.5.3; MC "the optimal step" (marked NOT CHECKABLE there) | **see §4 below** |
| §4 "Prior art" paragraph | MV §23.8.4 — the attribution the source says is owed to interval analysis | |
| §5 Th. 10 | MV §23.8.1; MV-D D.4.1; MC "Newton decrement" | |
| §5 Th. 11 | MV §23.8.2, §23.8.3; MC "self-concordance" | **restated with its unit dependence explicit (audit A-4, A-5) — see §3.5 below**; the source's interpretive sentences are not carried |
| §5 Th. 12, Table 3 | MV §26.6; MC "Aitken Δ² / Seki Kōwa" | |
| §5 remark in bits | MV §27.3 | |
| §6 Lemma 4 | MV §23.10.1; MC "the ordered bracket" | |
| §6 Th. 13 | MV §23.10.1; MC "the ordered bracket" (Newton remainder, Milne-Thomson) | |
| §6 Lemma 5, admissibility at order k | MV §23.10.4, §23.12; MC "the admissible order" | |
| §6 ν_V | MV §23.15; MC "the value-one crossing" | **the source's threshold (e > 5q) is replaced by D12's (Δ²T > 20q), audit A-6 — see §3.12** |
| §6 closing paragraph | MV §23.10.2 — Prop. 23.1's floor applies to the classical pair only | |
| §7 the data | SC §B.1 sources, SC count paragraph; the table headers of the level files | |
| §7 Table 4 | SC count paragraph (658/813 on 250 rows, 75/81 on 35 rows, cells refused 0); MV §24 | Run A reproduces the source exactly; Run B is this paper's own wider run |
| §7 price measured | MV §23.4.2 | **different sample and different comparand — see §3 below** |
| §7 gaps measured | MV-A A.13; MC "when the bracket fails" (median 1.201 over 742 pairs) | |
| §7 bound in the silence | MV §25.5; MC "what silence implies" | **different tightest cell and a different quantity — see §3.7 below** |
| §7 order census, Table 5 | MV §23.10.4 | **different collection — see §3 below** |
| §7 synthetic controls | MV §22.1.1.1 (36 of 36), MV §22.1.2 (widths, ratios, 274.1 vs 281.7) | reproduced exactly |
| §7 worked deduction | MV §25.6.1, §25.6.2, and §22.2.5 for δ(4s), δ(5s) | reproduced exactly; the ±400 cm⁻¹ on the threshold is the source's and is now carried |
| §8 | PC "where relativity enters, and where it does not"; IE for the published Li III value | **ratios near but not at the stated values; Li III now printed on both thresholds the tree holds — see §3.6 below** |
| §9 Lemma 6 | MV §26.1, §26.3 | |
| §9 Lemma 7 | MV §26.2; MC "the rank-one factorisation" | **σ₁ did not reproduce — see §3 below** |
| §9 remark | MV §27.1, §27.2, §27.3 | |
| §10 | the run of `check.py` | the table's rows are read off the obligation list; the counts are the SUMMARY line |

---

## 2 · Corrections in the record that the paper carries

A later passage of the source supersedes an earlier one in three places, and the later governs.

1. **The "conservation law" w·V = w²/e = 8y′²/y″.** MV §23.5.1 withdraws it: exact evaluation for
   y = x⁻² gives w²/e = 16x⁴/(h⁶ − 5h⁴x² + 7h²x⁴ − 3x⁶), which depends on h, and the table read as
   constant (366.3, 367.9, 370.6, 374.5 across h = 1…4) rises 2.2 %. The paper carries the corrected
   statement only: the product is the frontier's leading-order equation, not a conserved number, and
   a + 2b = 0 makes w²/e the unique h-free candidate at that order (§4, after Theorem 7).

2. **"The bracket holds in every one" on 1,442 cells.** MV §24 retracts it: 100 % is what the
   *trivial* form produces, and the defect form passes 546 of 789. The paper never quotes a pass
   rate of the containment statement as evidence — Corollary 1 says outright that it cannot fail on
   ordered levels — and §0 and §7 both say so.

3. **The flatness explanation for the fine-structure exclusion.** MV §25.2(ii) retracts 35.3 % and
   the flatness mechanism; the sequences are monotone in neither direction. The paper does not carry
   the exclusion list at all, so nothing of the retracted claim survives into it.

Two further corrections in the source are carried implicitly: MV §22.2.1 replaces a non-reproducible
3.7× extrapolation cost with a directional split, and MV §23.10.2 replaces the claim that V stays
near 2 at matched order. Neither claim appears in the paper.

---

## 3 · Claims of the source that `check.py` could not reproduce

In each case the paper prints the reproduced figure and not the stated one. **Nothing was repaired
in the source, and no check was altered to make a difference vanish.**

### 3.1 The asymptote's accuracy at ν = 10 — a source error, corrected

- **Stated** (MV §23.3): 4ν/3 + 4/(9ν) is "low by 0.69 % at ν = 2 and **exact to four decimals by
  ν = 10**".
- **Measured** (I12): the exact remainder is V(10) − (4·10/3 + 4/90) = 4/26,910 =
  **1.4864 × 10⁻⁴**. That is exact to three decimals and not to four.
- **Disposition:** a bug in the source's rounding, not in the check. The paper prints "exact to
  three decimals there and not to four" (§4, Corollary 4) and Figure 1's caption says "within
  1.5 × 10⁻⁴ by ν = 10".

### 3.2 "Agreement under 1 %" for the power-law price — a source error, corrected

- **Stated** (MV §23.1; MC "the four-thirds law"): V(x, p) = 4x/(h|p − 1|) "verified on power laws
  from p = −3 to +11, agreement under 1 %".
- **Measured** (I29, at x = 20, h = 1, exact rational V): p = 11 deviates by **2.24 %**;
  p = 7 by 0.83 %; p = −3 and 4 by 0.21 %; p = −2 and 3 by 0.08 %; p = 2 by 0.00 %; p = 11/6 by
  0.01 %. "Under 1 %" holds over p ∈ {−3, −2, 2, 3, 4, 7, 11/6} and fails at p = 11, the endpoint
  the sentence names.
- **Disposition:** the paper's Table 2 prints exact and leading-order side by side and states
  2.24 % as the largest deviation, with Theorem 8's second-order coefficient (p − 2)(p + 1)/12·(h/x)²
  = 2.25 % at p = 11 accounting for it. Figure 2's caption carries 0.83 % for the five marked points
  and 2.24 % at p = 11.

### 3.3 The failure condition and its inversion — sharpened, not reproduced as stated

- **Stated** (MV §25.3, MV-A A.13, MC "when the bracket fails" / "what silence implies"):
  "the bracket fails ⟺ |ΔT| > 2Z²R/ν³", and, read backwards, "the bracket held ⟹
  |ΔT| < 2Z²R/ν³ at that cell".
- **Measured:** 2Z²R/ν³ is the derivative, and the two gaps straddle it rather than equal it.
  g₊ = A(2ν+1)/(ν²(ν+1)²) < 2A/ν³ < g₋ = A(2ν−1)/(ν²(ν−1)²) at every ν > 1 (I21–I23, exhaustive on
  796 values), and on the measured cells the lower gap has median **1.264** and the upper **0.818**
  times 2Z²R/ν³ (E6). Since w/2 = h(2A/ν³)/(1 − h²/ν²)² strictly exceeds 2A/ν³ (I24), the source's
  inversion asserts a *tighter* bound than containment deductively supplies.
- **Disposition:** the paper replaces the leading-order biconditional with the exact one
  (Theorem 3: −(c − b) ≤ Δ ≤ a − c, also MACHINE-CHECKED as M3) and the inversion with
  Corollary 2's |Δ| ≤ max(g₋, g₊) = g₋, taking the bound at each cell as **the larger observed gap
  max(E − E₋, E₊ − E) from the two measured neighbours**, which is g₋ = w/2 + e = (w/2)(1 + 2/V)
  exactly (I39–I40). The first draft took the bound as w/2, which is smaller than g₋ by e — the
  same class of overreach as the source's, caught by the audit (A-1); E7 now measures the larger
  gap and prints the w/2 figures beside it for the record. The bound carries its hypothesis
  (neighbours unperturbed) and is stated as a bound on the level's displacement relative to its
  neighbours, not on a perturbation of the series in the Lu–Fano sense (R-11). ν_fail =
  ∛(2Z²R/|Δ|) survives only as Table 1, whose caption states that it lies between the two exact
  thresholds.

### 3.4 The measured price: sample and comparand both differ

- **Stated** (MV §23.4.2): **1,033** (ν/h, V) pairs from measured levels — h = 1: 560 pairs, median
  deviation **0.49 %**; h = 2: 473, **1.15 %**; all 1,033, **0.69 %** — measured against the
  asymptote 4(ν/h)/3.
- **Measured** (E5): **1,490** pairs at h = 1, median deviation **0.84 %**; **842** at h = 2,
  **0.51 %**; **2,332** in all, **0.71 %** — measured against the *exact* 4r³/(3r² − 1).
- **Two differences, both deliberate.** (i) The run here is over every series in the 86 tables that
  holds a triple at that step, keeping triples whose curvature is resolved at the floor (e ≥ 10q),
  not over a prepared subset; the source does not state which pairs its 1,033 are. (ii) The source
  measures the deviation from the *asymptote*, which is itself low by up to 0.69 % at small r, so
  part of its residual is the asymptote's own error; the paper measures the deviation from the exact
  law, which is the law Theorem 4 proves. The two are not the same quantity and the numbers are not
  comparable term for term.
- **Disposition:** the paper prints 1,490 / 842 / 2,332 and 0.84 % / 0.51 % / 0.71 % (§7, Figure 3),
  and states the comparand explicitly.

### 3.5 "The deepest channel reaches ν = 55", the sevenfold margin, and the unit

- **Stated** (MV §23.8.2): "The deepest channel in this book reaches ν = 55 … the ratio runs 0.0049
  at ν = 2, **0.1356 at ν = 55** … self-concordant across the entire measured range, with
  **sevenfold** margin."
- **Measured** (E11): the ratio at ν = 55, Z = 1 reproduces exactly at 0.1356 (I20), but the deepest
  cell in the collection tested here is **ν = 66.99** (Ga I 4s²np, n = 69, Z = 1), where the ratio is
  **0.1651** with R in cm⁻¹ — and **77.4** with R in hartree, at the same cell (E11).
- **The second point governs the first.** The self-concordance inequality |T‴| ≤ 2(T″)^{3/2} is not
  invariant under T ↦ cT: (T‴)²/(4(T″)³) = ν²/(3A/2) exactly (I19b), so the ratio scales as
  A^{−1/2} and the threshold ν ≤ √(3A/2) as A^{1/2} — 405.7 with R in cm⁻¹, 4.52 in eV, 0.866 in
  hartree (I20). The source's "self-concordant across the entire measured range" and "sevenfold
  margin" are statements about cm⁻¹, not about the atom; so was the first draft's "the decrement
  carries its meaning there" (audit A-4), and so was its "affinely invariant, which is why Z²R
  cancelled" (A-5: the decrement is invariant under affine maps of the variable, not of f; Z²R
  cancels from V because V is a ratio of two quantities linear in T).
- **Disposition:** Theorem 11 is restated as the exact identity for the ratio with its unit
  dependence explicit, the interpretive sentences are dropped, and §5 says what survives a change
  of unit: λ² = (2/3)T (exact in every unit, an energy in that unit) and the ratios V, w/T, e/T.
  E11 prints the ratio at the deepest cell in two units. The source's coverage difference (ν = 55
  versus 66.99) is still recorded here but the paper no longer draws a margin from it.

### 3.6 The hydrogenic threshold deficits, and which thresholds

- **Stated** (PC): Li III deficit **103.94**, Dirac 118.32, ratio **0.878**; Be IV **329.80**,
  373.97, **0.882**; B V **816.68**, 913.03, **0.894**; "0.8849 ± 0.0069 across Z = 3, 4, 5".
- **Measured** (E9, nuclear masses from AME2020 as atomic mass less Z·mₑ), on the thresholds the
  tree holds, each with its provenance:
  - Li III, the published ASD 5.12 ionization energy **987,661.0139 ± 0.0009** (IE, flag T):
    deficit **102.41**, ratio **0.865**;
  - Li III, the limit fitted to the series of theoretical levels, **987,662.29 ± 0.36** (register
    879, `channels.py`): deficit **103.68**, ratio **0.876**;
  - Be IV **1,756,018.8100 ± 0.0008** (ASD 5.12, the table header; the fitted value coincides):
    328.66, 373.97, **0.879**;
  - B V **2,744,111.38**, fitted to the series (register 892), no published uncertainty held:
    815.22, 913.03, **0.893**. `recovered/dirac.py` carries 2,744,107.933 for Z = 5 with no
    provenance and is not used.
- The three **Dirac terms reproduce exactly**. The source's deficits match neither threshold for
  Li III, and the source does not state which thresholds or which masses it used.
- The referee's recollection (R-13) that ASD lists Li III at 987,661.0 is **corroborated by the
  tree** (IE row 17); the first draft used only the fitted limit and printed 0.876 without saying
  which threshold it was. The two Li III values differ by 1.28 cm⁻¹, 3.5σ of the fit.
- **Disposition:** Table 6 prints every threshold with its value, its uncertainty and its source,
  and Li III on both; the text gives the range 0.865–0.893 and the 9R deficit on both thresholds
  (26.45 fitted, 25.17 published). Nothing is chosen between the two Li III values.

### 3.7 The tightest perturbation bound

- **Stated** (MV §25.5): over 1,442 cells the tightest is **1.398 cm⁻¹**, Al I 3s²nf, n = 54,
  ν = 54.0; then Ga I 4s²np n = 54 at 1.585 and Li I np n = 42 at 3.25 — each read as w/2.
- **Measured** (E7): over the **1,145 held cells** of Run B, with the bound taken as the larger
  observed gap (Corollary 2, §3.3 above), the tightest is **0.970 cm⁻¹**, at Ga I 4s²np ²P°, n = 66,
  ν = 63.8, where 2Z²R/ν³ = 0.844; the median over the held cells is **5,389 cm⁻¹**; the larger gap
  is the one toward n − 1 at 1,141 of the 1,145 cells, as Lemma 3 predicts. Read as w/2 the same
  cells give 0.925 and 4,308 (E7 prints both), which is what the first draft printed.
- **Disposition:** a coverage difference (the tables here carry Ga I to n = 69) and a change of
  quantity. The paper prints 0.970 (§7) and 0.97 (abstract, Figure 4 caption).

### 3.8 The bracket's pass rate on the earlier collection

- **Stated** (MV §24; PC): the defect form passes **546 of 789** interior cells (69.2 %), failing 243
  across 62 channels; the containment form passes 789 of 789.
- **Measured** (E2, E3): **1,145 of 1,551** (73.8 %) across 395 series; the containment form
  **1,551 of 1,551**.
- **Disposition:** a different and larger collection, not a contradiction; the qualitative claims —
  containment cannot fail, the defect form can, and the failures are places where δ is not locally
  monotone — reproduce. The paper prints its own two runs and says what each is.

### 3.9 The order-k census

- **Stated** (MV §23.10.4): at k = 1, 3, 6 the census reads admitted 499, 187, 34 with refusals 19,
  101, 145 and median bounds 25.96, 0.715, 0.0164 cm⁻¹; refusals rise from 3.7 % to 81 %.
- **Measured** (E8), over every run of k + 2 consecutive measured members in the 86 tables:
  k = 1 → 1,478 admitted / 12 wrong sign / 61 unresolved; k = 3 → 612 / 62 / 176;
  k = 6 → 147 / 43 / 201.
- **Disposition:** the *rule* reproduces verbatim (|Δ^{k+1}T| > 5·2^{k+1}σ, wrong sign = refused),
  the *counts* are of a different collection, and the source's three-column tabulation is not the
  same partition as the paper's three (the source's "held" column equals its "admitted" column
  throughout, so it carries no third class). The paper prints its own census as Table 5 and
  Figure 5, and does not quote the source's percentages.

### 3.10 The rank-one singular values

- **Stated** (MV §26.2; MC "the rank-one factorisation"): singular values **9.49 × 10¹** then
  **1.8 × 10⁻¹⁴** for fifteen observables over forty values of ν.
- **Measured** (E10): σ₁ = **83.69**, σ₂ = 1.75 × 10⁻¹⁴, σ₂/σ₁ = **2.1 × 10⁻¹⁶**.
- σ₁ is not an invariant of the claim: it depends on the exponent list and the ν grid, neither of
  which the source states. The conclusion — rank exactly one — reproduces, and the second singular
  value agrees to the digit printed.
- **Disposition:** the paper prints 83.69 and 2.1 × 10⁻¹⁶, with the grid stated (fifteen exponents,
  forty values of ν).

### 3.11 Small rounding differences that are not findings

- MV §23.8.1 prints λ² = **731.5820** at ν = 10; the exact value is **731.5821** (I18).
- MV §26.6 prints T(10) = **1097.3730**; R/100 = **1097.3732** (I28). The three Aitken columns
  reproduce to every digit printed.
- MV §23.8.2's self-concordance bounds 406 / 811 / 2,434 reproduce as 405.7 / 811.4 / 2,434.3 (I20).

### 3.12 ν_V — the source's threshold is not D12's

- **Stated** (MV §23.15): ν_V = (3Z²R/(5q))^{1/4} = 160 / 90 / 50.7 at q = 10⁻⁴ / 10⁻³ / 10⁻²,
  from "3A/ν⁴ > 5q".
- **Measured** (I26): those figures reproduce as 160.2 / 90.1 / 50.7 — but 3A/ν⁴ is e, not the
  second difference (Δ²T = 2e ≈ 6A/ν⁴), and the admissibility rule at order k = 1 (MV §23.10.4,
  the paper's D12) reads |Δ²T| > 5·2²q = 20q, i.e. e > 10q, which is also the filter §7 applies.
  Solved from D12, ν_V = (3Z²R/(10q))^{1/4} = **134.7 / 75.7 / 42.6**, smaller by 2^{1/4}.
- **The lithium threshold, settled 2026-09-24 at the author's direction.** Table 6 held Li III twice — the database's published ionisation energy and a limit fitted to the series of theoretical levels — and chose neither. The paper now takes the published value, on the rule it applies to every other species (the tabulated limit, never one fitted from the series), and keeps the fitted row as the sensitivity of the ratio (0.865 against 0.876). No number changed; the caption says which is the paper's.
- **Disposition:** the first draft presented the two thresholds as one (audit A-6). The paper now
  derives ν_V from D12 with the second difference named correctly and prints 134.7 / 75.7 / 42.6;
  I26 prints the 5q form beside it for the record.

---

## 4 · Claims the source marks as not checkable, and what became of them

**MC, "the optimal step":** marked *NOT CHECKABLE* there, because MV §23.5.3's objective is not
stated in the text and so the stationary point could not be verified. The paper states the objective
explicitly — αw + βV with α, β > 0 — and proves the stationary point at leading order
(Proposition 1), marking it "**PROVED** at leading order only". MV §23.5.3's own numbers show the
formula missing by 11 % at ν = 40, β/α = 10, where h* approaches ν/4; the paper states the validity
condition h* ≪ x and claims nothing beyond it. This is not a reproduction of the source's numbers,
which are not printed.

---

## 5 · Reproductions that are exact

Recorded because they are the paper's spine.

| claim | source | obligation |
|---|---|---|
| r = 2Z²R/(ν³σ) ≥ 5, σ the quotation floor, refusal counted separately | MV §22.5, RB | E7, E8, E1, N5 |
| Run A: 658 of 813 on 250 series, 75 of 81 on 35 series, 0 refused | SC count paragraph | E4 (asserted, not merely reported) |
| V = 4ν³/(h(3ν² − h²)) = 4r³/(3r² − 1), Z and R cancel | MV §23.4 | I1–I3 |
| V(20,1) = V(40,2) = V(60,3) = V(80,4) = 26.688907; V(10,1) = V(40,4) = 13.377926 | MV §23.4.1 | I13 |
| the exact rationals 32/11, 54/13, 256/47, 250/37, 4000/299 | MV §23.3 | I9 |
| Proposition 23.1 (V > 2) and its proof | MV §23.2 | I31, M2 |
| w/T and e/T at (20,1), (40,1), (40,2) | MV §23.6 | I7, I8, I14 |
| λ² = (2/3)T; 731.58 at ν = 10, 7.3158 at ν = 100 | MV §23.8.1, MV-D D.4.1 | I16–I18 |
| self-concordance ⟺ ν ≤ (√6/2)·Z√R, with R in cm⁻¹ (unit-dependent, §3.5) | MV §23.8.2 | I19, I19b, I20 |
| Aitken lands at T(2n²−1)/(6n²−2); the four-row table | MV §26.6 | I27, I28 |
| the eight-observable price table at ν = 20 | MV §23.9.1 | I29 |
| V at p = 50, 300, 10,000 → 2 | MV §23.9.2 | I30 |
| ordered bracket: 2,800 sign checks over ν = 8…119, k = 1…5, no failure (the 560 two-sided brackets are automatic) | MV §23.10.1 | I34 |
| 36 of 36 at δ = 0, 0.35, 1.35, 2.65, and the four energy ranges | MV §22.1.1.1 | I36 |
| widths 4,799…370; presumed 274.1 against true 281.7, 2.72 %; law ratio 0.764 | MV §22.1.2 | I37 |
| Sc VI: δ₂ = 1.0889, δ_∞ = 0.9376, δ(6s) = 0.9679, E = 736,688, [735,860, 738,547], [735,860, 737,380] | MV §25.6.1–2 | I38 |
| Li III limit written as 9R∞ is low by 26.45 cm⁻¹ against the fitted limit (25.17 against the published one) | PC | E9 |
| log₂V = 3.74 at ν = 10, 5.74 at ν = 40, floor log₂(32/11) = 1.54 | MV §27.3 | I15 |
| ν_fail table at |Δ| = 3,000 / 1,000 / 100 / 10 | MV §25.3 | I25 |

One corroboration worth recording. The channel table of **SC** carries a `m/k` bracket column per
row. Summed over the 363 series the two run files name, the table itself states **730 of 891**.
`check.py` recomputes, from the level files and the sealed instrument, **733 of 894** over the 285 of
those series that hold three consecutive measured members below the threshold — three more cells
tested and three more passes, a difference of 0.34 % in cell count. The paper does not print the
730/891 figure; it is recorded here as an independent agreement between the table and the
recomputation.

---

## 6 · Interpretations chosen

Places where the source admitted more than one reading and the paper had to fix one.

1. **Two runs rather than one.** The source's tested collection is a prepared series list
   (Run A, 285 series). The paper also runs every series in the 86 tables that holds a triple
   (Run B, 395 series). Run A is reported because it is the reproduction; Run B because it is the
   wider and less selected test. Both are in Table 4, with their difference stated.

2. **Deviation measured against the exact law.** §3.4 above. The exact law is what Theorem 4
   proves, so it is what the measurement is taken against.

3. **The curvature filter on the price measurement.** The source excludes cells above ν_V, a
   per-channel ceiling. The paper applies the same idea per cell: a triple enters the V measurement
   only when e ≥ 10q, q the coarsest quotation floor among its three levels. This is a stricter and
   purely local rule; it is stated in §7.

4. **Series identity.** A series is keyed by (configuration prefix, ℓ, term, J) as the tables print
   them, and only true neighbours count: a cell at n is interior only if members at exactly n − 1 and
   n + 1 are present. That is RB's own rule and it is what makes 1,551 the cell count rather than a
   larger one.

5. **Derived levels excluded.** A level the table marks as derived (bracketed, or non-numeric) is
   dropped before the test. The source does not say this in so many words; the paper states the
   reason — such a value is generated by the law the bracket assumes and cannot falsify it.

6. **Z per spectrum, not per cell.** Z is the charge seen by the excited electron and is read from
   the thresholds table for the spectrum, as the source does.

7. **"The deepest channel".** §3.5 above: read as a statement about the tested cells, it is false of
   this collection, so the paper states the measured maximum instead of repeating the claim.

8. **The blockade-radius row of Table 2.** p = 11/6 is not an integer, so V there is computed in
   floating point from (x ± h)^p rather than in exact rational arithmetic; every other row of that
   table is exact. The paper prints it to two decimals, which is within the float's accuracy by many
   orders.

9. **The threshold's own uncertainty in the worked deduction.** The source attaches ±400 cm⁻¹ to the
   Sc VI threshold "to be added at both edges". The paper carries it, marked CITED, and says it
   shifts both edges together and does not change their separation.

10. **Status of §9's rank-one claim.** The identity is proved in the paper (Lemma 7); the singular
    values are a numerical corroboration and `check.py` labels E10 ARITHMETIC (a floating-point
    SVD), not PROVED (audit A-8). The paper says so.

11. **The check's labels.** Fourteen obligations evaluate a proved closed form in floating point
    (I14, I15, I18, I20, I25, I26, I28, I32, I37, I38, E9b, E10, E13, I41); they are labelled
    ARITHMETIC and the paper counts them apart from the 21 PROVED, every one of which is exact
    Fraction arithmetic (audit A-8). I11 and I12 were made exact (1/144; 4/26,910 between 10⁻⁴ and
    10⁻³). I23 is EXHAUSTIVE, as §10 always said (A-25). The guards gate M1–M4 (A-18).

12. **Which Li III threshold.** §3.6: both are printed, neither is chosen.

13. **The tolerance's share.** E12 measures how many verdicts the floor alone decides and reports
    the 64 cells whose interval is narrower than 2q as a class; the rule D8 is not changed, because
    it is the instrument's, and no threshold in `check.py` moved (audit R-14).

---

## 7 · What the paper deliberately does not carry

Material inside the named passages that is out of the paper's scope, listed so its absence is not
mistaken for an omission: MV §22.2's four rules and §22.2.1–22.2.4's ablation table (a rule set for
*point estimates*, not for the bracket); §22.4.1's δ-versus-T bracket comparison; §23.11's
four-verdict refusal-pattern classifier and §23.11.1's per-channel reading; §23.13's inversion of p
from measured series; §23.14's capacity/resolution distinction; §24's collection description;
§25.2's five exclusions; §26.4–26.5's C₆ parameterisation; §27.4–27.6's slack table; MV-A's other
proofs (A.3, A.8–A.11, A.15, A.18, A.19), which belong to the lattice and not to the bracket; and
SC's mechanisms table and flagged-channel list. None of these is contradicted by the paper.
