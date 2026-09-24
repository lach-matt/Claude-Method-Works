# AUDIT — 04-seaton, "A Correction to Seaton's Ratio"

Audited 2026-09-24 against `BRIEF-AUDIT.md` and `PAPER-SPEC.md` §4, §5, §8, §10. The audit records;
it does not edit `PAPER.md` or `check.py`. Line numbers are lines of `PAPER.md` as drafted
(313 lines, dated 21 September 2026).

**What was run.** `PATH=method/bin` (Python 3.12.3). `python3 check.py` → 22 of 22 obligations
discharged, exit 0, 10 s. `python3 check.py --selftest` → 25 of 25, three negative controls each
REFUTED, exit 0. `python3 papers/method/lint.py papers/method/04-seaton` → 0 hits. `python3
papers/method/render.py papers/method/04-seaton` → `out/04-seaton.pdf`, 0.33 MB, 13 pages. The
HTML was screenshotted with headless Chromium at 1000 px width (full page, 9,205 px, sliced) and the
PDF was rasterised page by page (pypdfium2 installed into the scratchpad) and every page read.
The three figures were read as images. Every source passage `SOURCES.md` names was opened with
`sed -n` on the volumes under `method/members/`, plus `recovered/ritz.py`, `recovered/ryd_close.py`,
`tools/populate.py` (`core_p`, `config_of`) and the four NIST capture files.

Two further checks were run by the auditor and are reported where they bear: (i) an exact
propagation of the NIST quotation floors and a leave-lowest-member-out refit through the three
p = 0 fits, using `check.py`'s own `defects`/`profile_fit`; (ii) a sympy verification of Lemma 2's
rearrangement.

---

## Part A — content audit

### A.1 Every definition, lemma, theorem and number against the sources

| object (line) | where the source states it | paper vs source | proof / check |
|---|---|---|---|
| Thesis, §0 table (3, 23–26) | Physics Compendium 841–868: the table p = 0 / 3 / 1.150 / 0.206 and p ≥ 1 / 10 / −0.015 / 0.177; "valid at p = 0 and undefined at p ≥ 1, which is a domain statement" | the source's, stated as MEASURED; the paper adds the "ρ defined" column (3 and 6), which the source table lacks and which is the correct reading of `ryd_close.py` (the median/pstdev are taken over `abs(seat) > 1e-9`, i.e. six series, while `len(B_)` counts ten) | reproduced by `check.py` ("the four statistics reproduce") |
| "holds to 15%" (11, 28, 254) | Physics Compendium 855 | read as |median ρ − 1| = 0.150; the paper prints the three individual departures (15 / 10 / 56 %) — a stronger, more honest statement than the source | from ρ |
| Sign of δ₂ by p, Prop. 2 (32, 234) | Physics Compendium 866–867; Index of Indices 1622–1623 ("0 of 3 positive at p = 0, 2 of 2 at p = 5, monotone in p between") | the source's; the paper supplies the full table 0, ½, ½, ½, 1, 1 which the source only asserts as "monotone" | `check.py` sign rule + non-decreasing |
| Attribution of the ratio to Seaton (104, 311) | Mathematical Compendium 3737–3738 ("Seaton's ratio δ₂/δ₀ = −ℓ(ℓ+1)/3 is Seaton's; the domain restriction to p = 0 is this work's"); Physics Compendium 518–526, 684 | the paper's attribution sentence goes beyond the source: "as it is in the spectroscopic literature" is asserted, and `SOURCES.md` records that Seaton 1958 was not consulted and no passage in the tree quotes it — see R-21 | — |
| D1 n*, δ, z, R_M (52–56) | Physics Compendium 24–42 (n* = Z_c √(R_M/(I − E)), δ = n − n*; Z_c the core charge; R_M reduced-mass); Spectra Compendium 14–20; `ritz.py` 5, 26 | the source's; `R_M = R∞/(1 + 1/(A·m_p/m_e))` is exactly `ritz.py` line 26 — but the paper describes A as "in unified mass units" while multiplying by m_p/m_e = 1836.15 rather than u/m_e = 1822.89, and calls Rb's 84.912 a "tabulated atomic weight" (it is the ⁸⁵Rb isotope mass; the atomic weight is 85.468) — A-16 | R_M values printed by `check.py` Table 1 |
| D2 Ritz curve (58–62) | Spectra Compendium 950–958; Mathematical Compendium 770–784; `ritz.py` line 30 | the source's form δ₀ + δ₂/(n − δ₀)²; "at least four members" is `ritz.py` line 29 (`len(n)<4: continue`) | — |
| D3 p (64–68) | Spectra Compendium 102–106; Register 1261 ("p, the core's orbital count at this ℓ"); Mathematical Compendium 3030–3038; `populate.core_p` | the count is the source's; **the identification "non-penetrating ⇔ p = 0" is the paper's and is stronger than the source**, which splits p = 0 into two regimes (Register 1261 regimes 3 and 4, uncollapsed / collapsed) and records p = 0 channels with δ of order 0.6–0.9 (Mathematical Compendium 3066–3070, 530–534) — A-20 | `check.py` p table = `PMAP` |
| D4 polarisation model (70) | Physics Compendium 500–526; Mathematical Compendium 3120–3131 | the source's; the paper's prefactor 6α z²/K(ℓ) is **twice** the source's 3αc²/K(ℓ) — `SOURCES.md` records this correctly, and the paper is right: with α_d(Na⁺) = 0.9457 a₀³ the paper's form gives δ₀(Na nf) = 0.00150 against the observed ≈ 0.00155, the source's gives 0.00075 | ob_prefactor |
| Lemma 1 ⟨r⁻⁴⟩ (86–92) | Mathematical Compendium 1954–1958 (Bethe & Salpeter §3, cited); not derived anywhere in the source | stated for all n, proved by exact computation for n ≤ 30 (435 states) and CITED beyond; the two forms' equality is the identity (ℓ+3/2)(ℓ+½)(ℓ−½) = (2ℓ+3)(2ℓ+1)(2ℓ−1)/8, true — see R-2 for a full proof that is available | ob_r4, ob_r2_sanity |
| Lemma 2 (94–100) | not in the source (paper's own) | the displayed identity is correct and grid-verified; **the rearranged factor "(n−δ)²/(n(2n−δ))" is wrong by a factor 2 and the expansion in the proof is wrong** — A-1 | ob_energy_expansion checks only the first display |
| Theorem 1 (102–116) | Physics Compendium 684 / Register 1240 ("δ₂/δ₀ should be −ℓ(ℓ+1)/3 with the polarisability cancelling") | the source states the ratio; the paper derives it; derivation correct given Lemma 1 and Lemma 2's first-order conclusion (which survives A-1) | ob_ratio_identity (2,280 points), ob_z3 |
| Lemma 3 (120–126) | `SOURCES.md` "Interpretations chosen"; not in the source | correct; grid degree in δ₀ mis-stated (A-4) | ob_ritz_vs_n2 |
| §3 provenance (132–134) | `ritz.py` S; captures; Register 1258 (Rb I limit published; a fitted limit gave 33474.6) | consistent; "a second, independent retrieval" = the per-species capture files of the same database | ob_captures 79 of 80 |
| Table 1 (138–152) | `ritz.py`; `populate` | every cell matches `check.py`'s printed Table 1 | printed |
| Table 2 (158–199) | `ritz.py` S | auditor re-parsed all 80 rows: exact bijection with `ritz.py`, 80 = 80 | ob_captures |
| §4 procedure, Table 3 (205–223) | `ryd_close.py` output (`SOURCE_FIT`) | every (δ₀, δ₂, δ₂/δ₀, ρ, rms) cell matches `check.py`'s table; agreement with the source's curve_fit to 4 dp on 26 coefficients | profile_fit + SOURCE |
| Prop. 1, means, LOO, 1/n² refit (225–232) | Physics Compendium 841–868; Index of Indices 1614–1626 | reproduced; the extra figures (1.273 ± 0.253, 0.017 ± 0.194, LOO 1.334/1.357/1.127, 1/n² 1.175/0.221/−0.040/0.547) are the paper's own, all printed by `check.py` | stats() |
| §5.1 Hartree 1928 (252) | Mathematical Compendium 2908; Physics Compendium 554 | the source's attribution; weak against the literature (R-25) | — |
| §5.2 corrections and their direction (254) | Physics Compendium 500–508, 518–526 (quadrupole) | **the direction "those corrections point" is asserted, not derived** — R-14 | none |
| §5.3 separating cores (256) | `ob_separating_cores` | the argon-like and 60–79-electron cases are what `populate` returns; but Ca II nd is a pre-collapse d series (Register 1262) and would not test the p-statement cleanly — A-20 | ob_separating_cores |
| §5.5 limit sensitivity (264) | Physics Compendium 44–60 | reproduced to 5.5 × 10⁻⁶ | ob_limit_sensitivity |
| §5.5 fields (266) | Physics Compendium 46–50 ("needs tens of tesla", "begins at n > 60") | the source's numbers, uncited and unchecked — A-9 | none |
| §5.5 perturbers, In I nd (265) | `SOURCES.md` | reproduced | In I d obligation |
| References (302–313) | `SOURCES.md` reference table | every printed component is held **except** that the Ritz entry omits a title, journal, volume and pages that the tree DOES hold (Mathematical Compendium 780, Physics Compendium 464: "Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310") — `SOURCES.md` grepped for "Annalen" and missed "Ann. Phys." — A-13 | — |

### A.2 `check.py` output against every printed number

Every number in §0, §1, §2, §3 (Tables 1, 2), §4 (Table 3, Propositions 1–2, robustness), §5 and
§6 was matched to a line of `check.py`'s output: 435 / 0 disagree; 64 and 60 grid points; 200 values
of ℓ and 0.740718; 2,280; 8 obligations, 200 compared, 0 disagree; the p table (5,3,2,0)/(4,3,1,0)
and 16 cells; argon-like p = 0 at ℓ = 2 against 1, 20 cores in 60–79; 13 series, 80 levels; R∞,
m_p/m_e, the four R_M; 401 points, 90 steps, bracket ≤ 1.5 × 10⁻¹⁸ ("below 10⁻¹⁷"), max local
minima 1; all 13 rows of Table 3; 13 of 13 against the source fit; class sizes 3/10, defined 3/6;
1.150/0.206/−0.015/0.177 and 1.273/0.253/0.017/0.194; the ratios; LOO 1.334/1.357/1.127; 1/n²
1.175/0.221/−0.040/0.547; the sign counts and 0, ½, ½, ½, 1, 1; In I d 0.01755 vs 0.00141 and
2.18→2.31; 5.49 × 10⁻⁶ at ΔI = 0.01; 79 of 80 and Cd I 5p 43692.384; selftest 28 of 28, sat,
1.296/0.188. Derived figures (15 / 10 / 56 %, "factor of 1.6", "move by 0.03", "triples", "0.06 and
0.13", "0.0002 to 0.0003", "an order of magnitude") follow from printed values by arithmetic.

**Numbers with no check:** "tens of tesla" and "n of order 60" (line 266) — A-9. "forty significant
digits" is `getcontext().prec = 40`, set but not printed (trivial).

**Checks that do not test what the sentence claims:** line 205 "every scan shows exactly one local
minimum" — `check.py` prints only the maximum over series (1); the auditor confirmed all thirteen
are exactly 1, but the check as printed does not establish "every" — A-5. Line 294 "three
comparisons … against an independent implementation of the same fit" — A-6. Line 102/280 "MACHINE-
CHECKED" — A-2.

### A.3 The Z3 obligation (`ob_z3`, check.py 238–275)

- **Encoding.** For each ℓ ∈ {1..8}, with α, z real: `c0 = 6αz²/K(ℓ)`, `c2 = −2αz²ℓ(ℓ+1)/K(ℓ)`, claim
  `3c2 = −ℓ(ℓ+1)c0 ∧ (α > 0 ∧ z ≠ 0 ⇒ c0 > 0 ∧ c2 < 0)`, negation asserted, `unsat` expected.
- **Is it the relation the paper states?** Only in part. The paper's Theorem 1 is: *the first-order
  polarisation defect (α/2) z² n³ ⟨r⁻⁴⟩ has the form c₀ + c₂/n² with c₂/c₀ = −ℓ(ℓ+1)/3.* The Z3 terms
  for c0, c2 are the theorem's **conclusion** typed in; the obligation checks that two typed
  expressions stand in a ratio they were written to stand in. The content of the theorem — that
  n³⟨r⁻⁴⟩ decomposes this way — is carried entirely by the exact grid (`ob_ratio_identity`, 2,280
  points, PROVED), not by Z3.
- **Guards.** Non-vacuity (α > 0 ∧ z ≠ 0 satisfiable) runs. Encoding fidelity compares Z3's c0, c2 at
  200 seeded random rationals (`random.Random(5)`) with `seaton_coeffs` — **the same two formulae in
  `Fraction`**, not an independent implementation; the independent implementation in the file is
  `expect_power` (the Laguerre integral), which the guard never touches. Both guards gate the report
  (`z3ok and nonvac and disagree == 0`) — correct.
- **Box named in the paper?** Yes: line 102 and §6 line 280, "ℓ ∈ {1..8}, α_d and z real".
- **Verdict:** A-2 (MAJOR). The MACHINE-CHECKED status is honestly described but covers a
  near-tautology; the paper reads as though Z3 checked the theorem.

### A.4 Figures (read as images)

- **Figure 1.** (a) Thirteen points against p with the four Seaton lines; labels In I f / Cd I f /
  Sr II f / Rb I d / In I d; matches Table 3. (b) Nine points; medians and bands at the printed
  values. Defects: the annotation "median -0.015, sd 0.177" is drawn across the In I d marker at
  (2, 0.219); the annotations use an ASCII hyphen "-0.015" where the axes use a true minus; at
  print size (p. 9) the panel text is ~5 pt. — A-11.
- **Figure 2.** Correct values, bands and counts; the p ≥ 1 annotation crosses the ρ = 0 line; ASCII
  hyphen again. Caption matches. — A-11.
- **Figure 3.** Three panels, correct panel order (Cd, In, Sr) for "15%, 10% and 56%"; the orange
  curve is δ₀(1 − 4/(x−δ₀)²), i.e. Theorem 1's ratio in the Ritz denominator, which is what the
  caption says. No defect.
- `FIGURES.tsv` md5s match the files on disk.

### A.5 Lint

Clean (0 hits).

### A.6 Typography in the rendered pages

- **p. 11, §5.5 "Fields" bullet (line 266).** The source `n*⁷ … n*¹⁰` is read by pandoc as an
  emphasis pair: the page prints "A residual growing as n⁷ *is the signature of a magnetic field,
  which needs tens of tesla to matter, and one growing as n*¹⁰" — the run is italicised and the
  effective quantum number has lost its asterisk in both places, so the sentence as printed is
  about n, not n*. — A-12a (MAJOR).
- **Underscore and caret fallbacks on every page from 2 to 13.** In code spans (30 of the 64 on the
  page): `E_n`, `R_M`, `R_∞`, `δ_n`, `α_d`, `V_pol`, `⟨r⁻⁴⟩_z`, `⟨r⁻⁴⟩_1`, `R_nℓ(r) = N r^ℓ e^{−r/n}
  L^{(2ℓ+1)}_{n−ℓ−1}(2r/n)`, `r^{s+2}`, `(n/2)^{k+1}`, `r_i`, `w_i`, `δ_i`, `n_i`, `n*³ ΔI /
  (2z²R_M)`. In prose: α_d 16 times (§0 line 19 "−α_d/(2r⁴)", Theorem 1 statement, §2, §5, §6),
  R_M three times (Table 1 header "R_M (cm⁻¹)", Table 1 caption, §5), δ_n once (line 264), and
  "⟨r^s⟩" in the Bethe & Salpeter reference (line 304). — A-12b (MAJOR), A-12e.
- **p. 6, Table 1.** The R_M column is too narrow: every value breaks as "109736.78 / 4" over two
  lines. — A-12c.
- **p. 5 and p. 6, orphaned captions.** "Table 1 — the thirteen series …" is the last paragraph of
  p. 5, which is two-thirds blank, with the table on p. 6; "Table 2 — the levels" is the last line
  of p. 6 with the table on p. 7 (the template's `table { page-break-inside: avoid }` pushes each
  whole table to a fresh page and leaves its caption behind). — A-12d.
- Figures each sit with their caption (pp. 9–10). No §-heading is orphaned at a page foot (§4
  heads p. 8, §5 sits mid-p. 10, §6 heads p. 12). Tables 2 and 3 and the §6 table fit their columns.
  No literal backslash or stray markup other than the two items above. Unicode subscripts/
  superscripts (δ₀, δ₂, ⁻⁴, ², ³) render correctly wherever they were used.

### A.7 Findings, Part A

- **A-1 (BLOCKING) — lines 98 and 100, Lemma 2.** The rearrangement is wrong by a factor 2, and the
  expansion offered in the proof is wrong. From the (correct) identity, δ = −ΔE · 2n²(n−δ)²/(z²(2n−δ))
  = −(n³/z²) ΔE · **2**(n−δ)²/(n(2n−δ)); the paper's factor (n−δ)²/(n(2n−δ)) tends to ½, not 1, so
  "whose second factor is 1 + O(δ/n)" is false as printed, and the proof's "(n−δ)²/(n(2n−δ)) =
  1 − (3nδ − δ²)/(n(2n−δ))" is false (sympy: the two sides differ by (2δ − n)/(2n − δ)). The correct
  line is 2(n−δ)²/(n(2n−δ)) = 1 − (3nδ − 2δ²)/(n(2n−δ)) = 1 + O(δ/n). The first-order conclusion
  δ = −(n³/z²)ΔE, and hence Theorem 1, survive; the printed intermediate does not. *Resolve:* insert
  the factor 2 at line 98, replace the expansion at line 100 with the one above, and add the
  rearranged identity to `ob_energy_expansion` so that the check covers what the lemma prints.
- **A-2 (MAJOR) — lines 102, 280, 294, 296; check.py 238–275.** The Z3 obligation encodes Theorem 1's
  conclusion, and its fidelity guard compares that encoding with the same formula. *Resolve:* encode
  the theorem — declare n real ≥ 2 as well, assert `δ(n) := (α/2)·z²·n³·4(3n² − ℓ(ℓ+1))/(n⁵K(ℓ))`,
  and let Z3 refute the negation of "∃ c₀, c₂ with δ(n) = c₀ + c₂/n² for all n ⇒ 3c₂ = −ℓ(ℓ+1)c₀"
  (or, simpler and still meaningful, that δ(n)·n² is affine in n² with the stated slope/intercept
  ratio); make the fidelity guard evaluate the Z3 δ(n) term against `expect_power(n, ℓ, −4)` at
  the 200 sample points. Print the seed (5). Otherwise change §0/§6 to say what Z3 checked: the
  sign and ratio of the closed-form coefficients.
- **A-3 (MINOR) — line 19.** "⟨r⁻⁴⟩ in a hydrogenic state is (3n² − ℓ(ℓ+1)) times a function of ℓ
  alone" omits the n⁻⁵; as written the defect would not have the form δ₀ + δ₂/n². *Resolve:* "is
  (3n² − ℓ(ℓ+1))/n⁵ times a function of ℓ alone, and the defect is n³ times the energy shift".
- **A-4 (MINOR) — line 126.** After clearing the denominator the identity has degree 2 in δ₀, not 3
  (the 4 × 5 × 3 grid still exceeds it). *Resolve:* "degree 2 in n, 2 in δ₀ and 1 in δ₂".
- **A-5 (MINOR) — line 205; check.py 610–613.** "capped below the first member's n" is capped at
  n_min − ½; "every scan shows exactly one local minimum" is supported by the auditor's run (all
  thirteen = 1) but `check.py` prints only the maximum. *Resolve:* print min and max of `basins`
  and state the cap as n_min − ½.
- **A-6 (MAJOR) — line 294 and §6 table rows "Table 3", "Proposition 1".** The "independent
  implementation of the same fit" is not in `check.py`: `SOURCE_FIT` and `SOURCE_STAT` are typed
  transcriptions of an earlier nonlinear fit's printed output, and the third "comparison" is a mean
  δ of one series against a table the paper cannot cite. A reader cannot re-run the comparison.
  *Resolve:* either implement a second fitter inside `check.py` (a float Gauss–Newton on the same
  model, 20 lines) and compare to 4 dp, or reword line 294 to "two comparisons against the
  coefficients of a previously computed nonlinear least-squares fit of the same data" and drop the
  Cd I d row from the count.
- **A-7 (MINOR) — lines 205, 284, 289, 290, 294.** EXHAUSTIVE (spec: "a decision procedure visited
  every case in a stated finite family") is applied to loading 13 series, to a monotonicity read of
  six numbers, and to the fit itself ("The fit is EXHAUSTIVE over the thirteen series in that
  sense"). *Resolve:* keep EXHAUSTIVE for the 435 / 2,280 / 200 / 16 families and the sign rule;
  mark the rest MEASURED or "checked", and count accordingly in line 294.
- **A-8 (MINOR) — lines 102, 296.** "200 random rational" — the guard is seeded (`Random(5)`); the
  paper should say so, since it insists elsewhere that a sampled figure names its seed.
- **A-9 (MINOR) — line 266.** "needs tens of tesla" and "begins above n of order 60" are printed with
  no check and no citation. *Resolve:* state the field strengths the two thresholds assume and cite
  (Gallagher 1994 for the n⁴B² diamagnetic and n⁷F² quadratic-Stark scalings), or drop the numbers
  and keep only the powers.
- **A-10 (MINOR) — line 281; check.py 278–292.** The prefactor identity holds for all ℓ in one line
  (K(ℓ) = 8ℓ(ℓ+1)(ℓ−½)(ℓ+½)(ℓ+3/2)), so a 200-value EXHAUSTIVE is beside the point; "rises to
  0.740718" is checked monotone at three points (10, 50, 200) only. *Resolve:* state the identity,
  and either check monotonicity over all 200 or say "at ℓ = 10, 50, 200".
- **A-11 (MINOR) — Figures 1(b) and 2.** Annotation over the In I d marker; ASCII hyphen in
  "-0.015"; annotation crossing the ρ = 0 line. *Resolve:* in `figures.py` move the p ≥ 1 label
  below the band (or right-align at p = 3.6, y = −0.32) and format with "−" (`"%.3f" % x` →
  `("%.3f" % x).replace("-", "−")`).
- **A-12a (MAJOR) — line 266, rendered p. 11.** `n*⁷ … n*¹⁰` becomes italic and loses both
  asterisks. *Resolve:* write `n\*⁷` and `n\*¹⁰`, or put both in backticks.
- **A-12b (MAJOR) — throughout, rendered pp. 1–13.** Underscore/caret subscripts and superscripts in
  code spans and in prose (α_d ×16, R_M ×3, δ_n, E_n, V_pol, the Laguerre line, r^{s+2},
  (n/2)^{k+1}, r_i, w_i, δ_i, n_i). The spec (§9) told the drafter to use backticks; the brief says
  a defect visible on the page is a finding regardless. *Resolve:* pandoc's default markdown has the
  `subscript`/`superscript` extensions on: outside code spans write `α~d~`, `R~M~`, `E~n~`,
  `V~pol~`, `⟨r⁻⁴⟩~z~`, `R~nℓ~(r)`, `e^−r/n^`, `L^(2ℓ+1)^~n−ℓ−1~`, `r^s+2^`, and move the displayed
  formulae from backticks to plain blockquote text so the marks render. Where a Unicode subscript
  exists (ₙ, ᵢ, ₘ, ₚ) it may be used directly.
- **A-12c (MINOR) — Table 1, rendered p. 6.** R_M column wraps every value. *Resolve:* shorten the
  "core" column (print "Cd⁺", "In⁺", "Kr-like") or move A and R_M to a four-row note under the table.
- **A-12d (MINOR) — rendered pp. 5–7.** Table 1's and Table 2's captions are orphaned at page feet.
  *Resolve:* in `paper.html` give caption paragraphs `page-break-after: avoid`, or allow Table 2 to
  break (`page-break-inside: auto` for tables longer than a page).
- **A-12e (MINOR) — line 304, rendered p. 13.** "⟨r^s⟩" with a literal caret. *Resolve:* ⟨rˢ⟩.
- **A-13 (MAJOR) — line 310 and `SOURCES.md` 141.** The Ritz reference was stripped to "Ritz, W.
  (1903). The two-term quantum-defect expansion δ = δ₀ + δ₂/n²" on the ground that no part of the
  full citation is in the tree. The tree holds it twice: Mathematical Compendium 780 and Physics
  Compendium 464, "Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310" (the grep
  was for "Annalen"; the record abbreviates). The present entry is a description, not a reference,
  and it names δ₂/n² where D2 fits δ₂/(n − δ₀)². *Resolve:* "Ritz, W. (1903). Zur Theorie der
  Serienspektren. *Annalen der Physik* **12**, 264–310." and correct `SOURCES.md`.
- **A-14 (MINOR) — `SOURCES.md` 136.** Says Drake's initials "G. W. F. … is printed"; the paper's
  entry (line 306) prints no initials. *Resolve:* align `SOURCES.md` with the paper.
- **A-15 (MINOR) — lines 305–313, `SOURCES.md` 134.** Five journal names are expanded from the
  abbreviations the record holds (MNRAS, Phys. Rev., Proc. Camb. Phil. Soc., At. Data Nucl. Data
  Tables, Rep. Prog. Phys.); `SOURCES.md` declares only the Z. Phys. expansion. All five are
  unambiguous. *Resolve:* say so in `SOURCES.md`.
- **A-16 (MINOR) — lines 56, 132; Table 1.** "A the atomic mass in unified mass units" with the
  factor 1836.15267343 (m_p/m_e) instead of 1822.888 (u/m_e): under the stated definition the four
  R_M would read 109736.780, .791, .607, .631 — the printed third decimals differ by 0.004–0.005
  cm⁻¹. And Rb's 84.912 is the ⁸⁵Rb isotope mass, not "the tabulated atomic weight" (85.468). The
  effect on any δ is ≈ 3 × 10⁻⁷ and on ρ invisible. *Resolve:* say "A·m_p/m_e, treating the core mass
  as A proton masses" and "⁸⁵Rb and ⁸⁸Sr isotope masses", or recompute with u/m_e and reprint R_M.
- **A-17 (MINOR) — line 56.** "reduced mass of the electron and the nucleus" should be the electron
  and the ion core; the atomic mass is the right proxy for the latter. *Resolve:* wording.
- **A-18 (MINOR) — Table 2.** Levels quoted by NIST to 0.1 cm⁻¹ (Cd I nf, Sr II nf, Sr II ns above
  7s, Sr II nd above 6d) and to 0.01 (In I) are printed with three decimals ("65586.000"). *Resolve:*
  print each level to its quoted precision, or add a column of NIST uncertainties.
- **A-19 (MAJOR) — §0, §3, §5 (the choice of ℓ = 3 as the non-penetrating test).** The source places
  Seaton's term at ℓ ≥ 4 and says it "fails at l < 4" (Physics Compendium 518–526; Mathematical
  Compendium 3122; Physics Compendium 116–139 "Above ℓ = 4 the electron never enters the core") and
  warns that nf "treated as non-penetrating" gives α_d and α_q that disagree with ng (500–508). The
  paper's three p = 0 series are all nf, and it does not say that its test sits at the ℓ its own
  sources regard as marginal. Merged with R-12 for the resolution.
- **A-20 (BLOCKING) — lines 17, 68, 30, 252, 256 (the domain "p = 0").** The paper defines
  non-penetrating as p = 0 and then argues physically that p = 0 is "the condition under which the
  core has no orbital of the electron's ℓ for it to overlap" and that "the statement in p is the one
  the derivation supports". The record says otherwise, twice: Register 1261 splits p = 0 into
  regime 3 (uncollapsed, Z < T) and regime 4 (collapsed, Z ≥ T); Mathematical Compendium 3066–3070
  measures "across 116 p = 0 channels at ℓ = 2 or 3: collapsed median 0.637, uncollapsed 0.036",
  naming Ba II nf = 0.756 and Ca I nd = 0.908, and 530–534 records Seaton's term failing on Ba II
  and Hg II "where the 4f orbital has collapsed into the core and the series penetrates". A p = 0
  channel with δ₀ ≈ 0.7 is not one on which the polarisation model's hypothesis holds, so "valid at
  p = 0" as a domain statement is contradicted by cases the source already holds; and §5.3's
  proposed discriminating test, Ca II nd, is itself a pre-collapse d series (Register 1262 gives the
  argon-core d channels y = 0.086 → 0.373 across the 3d threshold). The three series measured here
  are all uncollapsed nf on cores with Z ≤ 48, so the measurement stands; the stated domain does
  not. *Resolve:* (i) state p = 0 as necessary and not sufficient, and define the paper's class as
  "p = 0 and uncollapsed" (or, operationally, p = 0 with δ₀ ≪ 1); (ii) change the §0 headline and
  the thesis accordingly; (iii) add an "Orbital collapse" bullet to §5.5 with the Ba II nf case and
  the standard references the tree holds (Goeppert-Mayer 1941; Griffin, Andrew and Cowan 1969 —
  Mathematical Compendium 3070); (iv) rewrite §5.3: the cores that separate p from ℓ at ℓ = 2 are
  all in or near the 3d collapse zone, so no clean test of "p = 0 at ℓ = 2" exists among low-charge
  argon-like cores, and ℓ = 4 has p = 0 on every core — the honest sentence is that the derivation's
  hypothesis is non-penetration, which neither p nor ℓ alone guarantees.

---

## Part B — reader audits

### B.1 A mathematician (order / combinatorics; has never seen this material)

I can follow the paper without the books, and I take D1–D6 and the Notation line as a complete
list of symbols: every symbol used in §2–§6 is defined before use, K(ℓ) included. The paper's
mathematics is small — two rational identities, one expectation value, one first-order argument —
and a referee in *Order* would not be its referee; but the algebra has to be right and the words
"proved", "proposition" and "exhaustive" have to mean what they say. Three places they do not.

- **R-1 (BLOCKING) — lines 98, 100.** Lemma 2's second sentence is false as printed and its proof's
  last step is false. This is A-1; I checked it independently by hand and by sympy. A lemma marked
  PROVED with a wrong displayed identity is disqualifying until fixed, even though the first-order
  conclusion is right. *Change:* as A-1.
- **R-2 (MAJOR) — lines 86–92, and 280.** Lemma 1 is stated for every (n, ℓ) with ℓ ≥ 1 and its
  "Proof" is an exact computation for n ≤ 30 plus a citation for the rest, closed with ∎. That is a
  verification and a citation, not a proof; and Theorem 1 is then marked PROVED although it rests on
  a lemma that is CITED for n > 30. A proof for all n is short and the paper's own machinery
  supplies its seeds: the Kramers–Pasternack recursion, (s+1)/n² ⟨rˢ⟩ − (2s+1)⟨rˢ⁻¹⟩ +
  (s/4)[(2ℓ+1)² − s²]⟨rˢ⁻²⟩ = 0, with ⟨r⁻¹⟩ = 1/n² (virial) and ⟨r⁻²⟩ = 1/(n³(ℓ+½)) (which the paper
  already verifies as its control) gives at s = −1 the standard ⟨r⁻³⟩ = 1/(n³ℓ(ℓ+½)(ℓ+1)) and at
  s = −2 exactly the closed form of Lemma 1. I verified the recursion at 112 (n, ℓ, s) against
  `expect_power` and the recursion's ⟨r⁻⁴⟩ against `r4_formula` for n ≤ 12: identical. *Change:*
  prove Lemma 1 by the recursion (citing Pasternack 1937 for it, or proving it — it is a
  two-integration-by-parts identity), keep the 435-state computation as the check, and let
  Theorem 1's PROVED stand on its own; otherwise write "Lemma 1: EXHAUSTIVE (n ≤ 30) and CITED;
  Theorem 1: PROVED given Lemma 1" in §6.
- **R-3 (MAJOR) — line 102, §6.** The MACHINE-CHECKED claim is a restatement (A-2). From where I
  sit the exact grid is the real check, and Z3 adds nothing a reader should be told it adds.
  *Change:* as A-2, or delete the MACHINE-CHECKED status from Theorem 1 and keep PROVED.
- **R-4 (MINOR) — lines 225, 234.** "Proposition 1" and "Proposition 2" are data summaries. A
  proposition is a claim with a proof; these are measurements, and the paper says so ("MEASURED").
  *Change:* "Measurement 1", "Measurement 2" (or "Result").
- **R-5 (MINOR) — line 62.** "For ℓ = 0 the model's value is 0" — the model is undefined at ℓ = 0
  (K(0) = 0, ⟨r⁻⁴⟩ diverges); only the formal expression −ℓ(ℓ+1)/3 is 0. *Change:* "the formal value
  of −ℓ(ℓ+1)/3 is 0 and the model itself does not apply".
- **R-6 (MINOR) — line 100.** "legitimate for 0 < δ < 2n" — the division needs only 2n − δ ≠ 0 and
  n ≠ δ (n ≠ 0); state the actual conditions.
- **R-7 (MINOR) — lines 205, 286.** "certified least-squares solution" — certified against a
  401-point scan and one bracket; §6 says so honestly. *Change:* "scan-certified" in §4, so the two
  places agree.
- **R-8 (MINOR) — line 19.** The n⁻⁵ omission (A-3).
- **R-9 (MINOR) — line 126.** Degree 2, not 3, in δ₀ (A-4).
- **R-10 (MINOR) — line 292.** "16 cells: the four cores at ℓ = 0, 1, 2, 3" — the family is stated;
  fine. But "13 minimisers … each certified" is not a family a decision procedure visits; see A-7.

Unmotivated: nothing. The paper says what it is for. What I would reject: R-1 as it stands.

### B.2 An atomic physicist who works with NIST spectra

The data are right. I recognise every level in Table 2 (Rb 6s 20132.510, Sr II 6s 47736.53, Cd
6s ³S₁ 51483.980, In 6s 24372.957, Cd 5s5p ¹P°₁ 43692.384), the limits are the ASD values (Cd
72540.05, In 46670.107, Rb 33690.81, Sr II 88965.18), R∞ is CODATA, and the term labels are the
single-parent series a spectroscopist would pick. The fit is done carefully and reproducibly. My
objections are to what the fit is asked to mean.

- **R-11 (BLOCKING) — lines 17, 68, 252, 256.** "Non-penetrating ⇔ p = 0" is not how the literature
  uses the word and is not true. Penetration is graded, and the classic counter-cases are exactly
  the p = 0 orbitals that collapse: 3d at Z ≈ 21 and 4f at Z ≈ 57. Ba II nf (core [Xe], p = 0) has
  δ_f ≈ 0.76 and is a penetrating series by any measure; Ca II nd (core [Ar], p = 0) has δ_d ≈ 0.6–0.7
  and is the paper's own proposed test case in §5.3. The paper's four cores (Z ≤ 48) sit below both
  thresholds, so its three nf series are genuinely non-penetrating — but that is because of where
  they sit, not because p = 0. The headline "valid at p = 0" would be falsified the moment someone
  fits Ba II nf. This is A-20; *change* as there. The word the literature uses for the paper's p is
  the count of core subshells of the same ℓ, i.e. the number of radial nodes the Rydberg orbital is
  forced to carry inside the core (Bohr's penetrating orbits; Edlén 1964, who states the rule
  floor(δ) ≈ p); the paper's §5.1 gives exactly that argument and D3 should say that p is that
  count and that "penetrating/non-penetrating" is the paper's operational label for it.
- **R-12 (MAJOR) — lines 30, 254; §3.** The test is made on nf series, the marginal case. The
  polarisation formula is tested in the literature on ng and nh (Freeman & Kleppner 1976 on Na;
  the paper's own source warns that nf "treated as non-penetrating" is inconsistent with ng). The
  paper never makes the check its own model invites: δ₀ = 6α_d z²/K(ℓ) predicts the limit defect
  from a known polarisability. For Sr²⁺, α_d = 5.8 a₀³ (Mitroy, Safronova and Clark 2010), which
  predicts δ₀(Sr II nf) = 0.037 against the fitted 0.0648 — the series with ρ = 1.564 fails the
  model at the δ₀ level by a factor 1.8 before any ratio is taken, which is the real reason its ρ is
  off. The implied α_d for Cd⁺ (24.8 a₀³) and In⁺ (26.2) should be set beside published values
  too. *Change:* add a column "α_d implied" to Table 3 for the p = 0 rows and a sentence comparing
  with published polarisabilities; say in §0 and §5.2 that ℓ = 3 is the lowest ℓ at which the model
  can be tried on these cores and that the 10–56 % departures are of the size expected at nf.
- **R-13 (MAJOR) — §4, Table 3, §5.4.** No per-series uncertainty on ρ, and an unweighted fit over
  levels quoted to 0.1 cm⁻¹ (Cd I nf, Sr II nf) and 0.01 cm⁻¹ (In I nf). I propagated the quotation
  floors through `check.py`'s own fit: ±0.009 (Cd), ±0.001 (In), ±0.001 (Sr) in ρ — small. But the
  lowest member matters: dropping n = 4 moves ρ from 1.150 → 1.051 (Cd), 1.105 → 1.154 (In), 1.564
  → 1.623 (Sr). The 4f member is where penetration, the quadrupole term and the (n−δ₀)² ≠ n*²
  difference are all largest, and it moves the "15 %" by 5–10 points. *Change:* add the
  leave-lowest-out refit and the quotation-floor sensitivity to "Robustness of the figures" and
  to `check.py`; consider stating the p = 0 result as a range (1.05–1.15 for Cd I) rather than a
  single ρ.
- **R-14 (MAJOR) — lines 30, 254.** "the quadrupole term, second-order dipole terms and the residual
  penetration … are the natural account of a ρ above 1" and "which is the direction those
  corrections point" — no direction is derived. Only the quadrupole term's is obvious: ⟨r⁻⁶⟩ ∝
  35n⁴ − 5n²(6ℓ(ℓ+1) − 5) + …, so its n⁻²/constant ratio is −(6ℓ(ℓ+1) − 5)/7 = −9.57 at ℓ = 3 against
  the dipole's −4, and a positive α_q term does push ρ above 1. The non-adiabatic second-order
  dipole term enters ⟨r⁻⁶⟩ with the opposite sign to α_q (Drake and Swainson 1991), and residual
  penetration adds a nearly n-independent positive term to δ₀, which pulls ρ *below* 1. *Change:*
  keep and derive the quadrupole sentence (one line from ⟨r⁻⁶⟩), and say the other two are of
  undetermined sign here.
- **R-15 (MINOR) — lines 56, 132.** m_p/m_e in place of u/m_e; Rb isotope mass called an atomic
  weight; "nucleus" for the ion core (A-16, A-17).
- **R-16 (MINOR) — Table 2.** Trailing zeros beyond NIST's quoted precision (A-18); the physicist
  reading 65586.000 will look for a source that does not exist.
- **R-17 (MINOR) — Table 3, Rb I rows.** The Rb Rydberg–Ritz coefficients are known to five figures
  from millimetre-wave and EIT spectroscopy: nd₃/₂ δ₀ = 1.34809, δ₂ = −0.6029; ns 3.13118, 0.1784;
  np₁/₂ 2.65488, 0.2900 (Li, Mourachko, Noel and Gallagher 2003; Mack et al. 2011). The paper's
  six-member unweighted fits give 1.3504/−0.7418, 3.1308/0.1980, 2.6540/0.3258: right signs, δ₂
  10–25 % off. That is the scale of what a six-member Ritz fit can say about δ₂, and a sentence
  comparing with these values would give the reader a calibration the paper otherwise lacks.
- **R-18 (MINOR) — line 266.** The field thresholds are quoted without the field strengths they
  assume (A-9).
- **R-19 (MINOR) — line 264.** "The limits of Table 1 are tabulated, not fitted" — true; but
  the Cd II limit carries ±0.13 cm⁻¹ (the capture header), which by the paper's own n*³ΔI/(2z²R_M)
  is 4 × 10⁻⁴ in δ at n = 9, larger than the Cd I f rms of 0.00029. *Change:* propagate the limit
  uncertainty into ρ for the three p = 0 series (it is common-mode across a series and feeds both
  coefficients).
- **R-20 (MINOR) — line 30.** "Seaton's derivation assumes …" attributes a derivation to a paper
  the author records not having read. *Change:* "the derivation assumes".

What is overstated: the domain (R-11) and the direction of the corrections (R-14). What is right
and worth keeping: the data, the fit, the honest 3-vs-6 accounting, the p ≥ 1 result, the sign
rule as a rule.

### B.3 A journal referee (atomic physics / spectroscopy)

**Novelty and framing.** The n-dependent polarisation defect, δ ∝ α_d z² [3 − ℓ(ℓ+1)/n²]/K(ℓ), is a
textbook result (Van Vleck and Whitelaw 1933; Mayer and Mayer 1933; Edlén 1964; Freeman and
Kleppner 1976), and that it applies only to non-penetrating series is the sentence with which every
one of those treatments introduces it. There is no "Seaton's ratio" in the literature and there is
nothing in Seaton (1958) that this paper corrects. What the paper actually contributes is (i) a
reading of "non-penetrating" off the core's ground configuration, (ii) a clean, exact, reproducible
fit of thirteen NIST series with an honest small-sample accounting, and (iii) the observation that
the sign of δ₂ tracks the core count p. Those are worth a short paper; the title and §0 promise
something else.

- **R-21 (MAJOR) — title, lines 1, 3, 17, 104, 311.** "A Correction to Seaton's Ratio" and "attributed
  to Seaton here as it is in the spectroscopic literature" are unsupported (`SOURCES.md`: Seaton
  1958 not consulted; no passage quotes it). *Change:* retitle ("The domain of the polarisation
  ratio δ₂/δ₀ = −ℓ(ℓ+1)/3, tested on thirteen Rydberg series", or similar); in §0 replace "What is
  corrected" with a plain statement of the three contributions above; attribute the ratio to the
  polarisation formula and its authors, and cite Seaton (1958) for the quantum defect method only.
- **R-22 (MAJOR) — References.** Missing standard references, with full author lists and years.
  Those marked *held* are in the tree and may be printed under the paper's own policy now; the
  others need the author's confirmation of the bibliographic details.
  - Edlén, B. (1964). Atomic Spectra. In *Handbuch der Physik*, vol. 27, 80–220. — *held*
    (Mathematical Compendium 184–188; the main volume's entry says 1960). The standard account of
    penetrating vs non-penetrating orbits and of the polarisation formula.
  - Ritz, W. (1903). Zur Theorie der Serienspektren. *Annalen der Physik* **12**, 264–310. — *held*
    (A-13).
  - Goeppert-Mayer, M. (1941). Rare-earth and transuranic elements. *Physical Review* **60**,
    184–187; and Griffin, D. C., Andrew, K. L. and Cowan, R. D. (1969). Theoretical calculations of
    the d-, f-, and g-electron transition series. *Physical Review* **177**, 62–71. — *held*
    (Mathematical Compendium 3070). Orbital collapse, needed for A-20.
  - Freeman, R. R. and Kleppner, D. (1976). Core polarization and quantum defects in
    high-angular-momentum states of alkali atoms. *Physical Review A* **14**, 1614–1619. — the
    modern test of the polarisation formula with the quadrupole term (the tree holds "Freeman &
    Kleppner 1976, Na I ng", Spectra Compendium 1016).
  - Van Vleck, J. H. and Whitelaw, N. G. (1933). The quantum defect of nonpenetrating orbits, with
    special application to Al II. *Physical Review* **44**, 551–569.
  - Gallagher, T. F. (1994). *Rydberg Atoms*. Cambridge University Press. — for the field scalings
    of §5.5 and the polarisation model.
  - Pasternack, S. (1937). On the mean value of rˢ for Keplerian systems. *Proceedings of the
    National Academy of Sciences* **23**, 91–94. — if R-2 is taken.
  - Li, W., Mourachko, I., Noel, M. W. and Gallagher, T. F. (2003). Millimeter-wave spectroscopy of
    cold Rb Rydberg atoms in a magneto-optical trap: Quantum defects of the ns, np, and nd series.
    *Physical Review A* **67**, 052502; Mack, M., Karlewski, F., Hattermann, H., Höckh, S.,
    Jessen, F., Cano, D. and Fortágh, J. (2011). Measurement of absolute transition frequencies of
    ⁸⁷Rb to nS and nD Rydberg states by means of electromagnetically induced transparency. *Physical
    Review A* **83**, 052515. — if R-17 is taken.
  - Mitroy, J., Safronova, M. S. and Clark, C. W. (2010). Theory and applications of atomic and
    ionic polarizabilities. *Journal of Physics B* **43**, 202001. — if R-12 is taken.
  - Drake and Swainson (1991) is printed without its title while every other article has one; the
    title is "Quantum defects and the 1/n dependence of Rydberg energies: Second-order polarization
    corrections" — not held in the tree; for the author to confirm.
- **R-23 (MAJOR) — §6.** Honesty of the verification record: the "independent implementation"
  (A-6), MACHINE-CHECKED over a restatement (A-2), EXHAUSTIVE for non-families (A-7). Each is
  defensible in isolation; together they make the record read stronger than the checks are.
  *Change:* as A-2, A-6, A-7.
- **R-24 (MINOR) — Abstract, §0.** "derives it exactly from the hydrogenic expectation value" —
  Lemma 1 for general n is cited (R-2); the abstract should say "derives it from the standard
  hydrogenic ⟨r⁻⁴⟩" or the proof should be completed. Otherwise the abstract and §0 promise what the
  body delivers, and the "what is not established" paragraph is exemplary.
- **R-25 (MINOR) — lines 252, 307.** Hartree (1928) is cited for "the penetration argument by which
  the defect falls with ℓ"; that paper is the self-consistent-field method. The centrifugal
  argument is Bohr's (penetrating orbits, 1922–23) and is standard in Edlén (1964). *Change:* cite
  Edlén, or Bohr, and keep Hartree for the SCF potential if it is wanted at all.
- **R-26 (MINOR) — line 310.** The Ritz entry is a description, not a reference, and names δ₂/n²
  where D2 fits δ₂/(n − δ₀)² (A-13).
- **R-27 (MINOR) — lines 132, 308.** NIST's own citation form asks for the retrieval date;
  "retrieved in August 2026" is the best the record supports and should be kept, but the reference
  entry should carry it too ("[retrieved August 2026]").
- **R-28 (MINOR) — line 256.** "every core of sixty to seventy-nine electrons — twenty of them" is an
  arbitrary window: cores of 58 and 59 electrons and of 80 upward also hold an f subshell. *Change:*
  "every core from cerium-like (58 electrons) upward".
- **R-29 (MINOR) — line 132.** "confirmed level by level against a second, independent retrieval of
  the same tables" — two captures of one database are not independent evidence of the levels; they
  guard against transcription only. *Change:* "against a second capture of the same tables".

Correctness: A-1 must be fixed; A-20 must be reworded; nothing else is wrong as arithmetic.
Clarity: good. Verification record: see R-23.

---

## Part C — the record

Duplicates across readers are marked "= A-n" and counted once.

| id | severity | line(s) | finding (short) | disposition |
|---|---|---|---|---|
| A-1 | BLOCKING | 98, 100 | Lemma 2 rearranged factor wrong by 2; expansion wrong |  FIXED — Lemma 2 now prints δ = −(n³/z²)ΔE·2(n−δ)²/(n(2n−δ)) and 2(n−δ)²/(n(2n−δ)) = 1 − (3nδ−2δ²)/(n(2n−δ)); both are exact obligations on grids above degree (121 points) and the factor without the 2 is a negative control. Theorem 1 unaffected |
| A-2 | MAJOR | 102, 280, 294, 296 | Z3 obligation encodes the conclusion; fidelity guard not independent |  FIXED — Z3 now receives the premise D(n) = (α/2)z²n³·4(3n²−L)/(n⁵K) and derives the ratio from the two-point coefficients, with a third point for affineness; the fidelity guard compares D(n) with the Laguerre integral; seed 5 printed |
| A-3 | MINOR | 19 | ⟨r⁻⁴⟩ summary omits n⁻⁵ |  FIXED — "(3n² − ℓ(ℓ+1))/n⁵ times a function of ℓ alone, and the defect is n³ times the energy shift" |
| A-4 | MINOR | 126 | degree in δ₀ is 2 not 3 |  FIXED — degree 2 in δ₀, in the paper and in the check's docstring |
| A-5 | MINOR | 205 | scan cap mis-stated; "every scan" not printed by check |  FIXED — cap stated as n − ½ for the first member's n; the check prints min and max local minima (1 and 1) |
| A-6 | MAJOR | 294, §6 rows | "independent implementation" is a typed transcription; third comparison mis-described |  FIXED — a float Gauss–Newton fitter added to the check (26 of 26 coefficients to 4 dp); §4 and §6 call it a cross-check; the three prior-figure comparisons are described as such, with the Cd I d row named as one mean defect, and no claim rests on them |
| A-7 | MINOR | 205, 284–294 | EXHAUSTIVE applied to non-families |  FIXED — EXHAUSTIVE kept for the 902/435/406/2,280/200/16-cell/108-core families, the 80 captures and the sign counts; loading, the fit, class sizes, the monotone fraction and the sensitivities are MEASURED; the count sentence rewritten (7 PROVED, 11 EXHAUSTIVE, 2 MACHINE-CHECKED, 8 MEASURED, 1 cross-check, 3 comparisons) |
| A-8 | MINOR | 102, 296 | guard seed not stated |  FIXED — seed 5 stated in Theorem 1, Corollary 1 and §6 |
| A-9 | MINOR | 266 | "tens of tesla", "n of order 60" unchecked, uncited |  FIXED — the two numbers dropped; the powers n∗⁷ and n∗¹⁰ kept, with Gallagher 1994 cited |
| A-10 | MINOR | 281 | prefactor identity holds for all ℓ; monotone checked at 3 points |  FIXED — the prefactor identity stated as degree 5 in ℓ (PROVED at 200 values); monotonicity now checked at every consecutive pair in 1..200 |
| A-11 | MINOR | Fig. 1(b), Fig. 2 | annotation over In I d marker; ASCII hyphen; annotation over ρ = 0 line |  FIXED — p ≥ 1 label below its band at the right edge (Fig. 1b); row labels at the right edge (Fig. 2); true minus signs via fmt(); panel (b) title shortened (it was clipped); figures regenerated, FIGURES.tsv md5s updated |
| A-12a | MAJOR | 266 (p. 11) | `n*⁷ … n*¹⁰` rendered as italics, asterisks lost |  FIXED — the effective quantum number is written n∗ (U+2217) throughout, so no markdown asterisk can pair |
| A-12b | MAJOR | pp. 1–13 | underscore/caret subscripts in code spans and prose (α_d ×16, R_M, δ_n, E_n, V_pol, Laguerre line, r_i, w_i …) |  FIXED — every code span removed from mathematics; α_d → α (D5 defines α dipole, β quadrupole); R_M → Rₘ, E_n → Eₙ, δ_n → δₙ, r_i/w_i/δ_i/n_i → rᵢ/wᵢ/δᵢ/nᵢ; the Laguerre line rewritten in words with rˡ and (n/2)ᵏ⁺¹; displayed formulas as plain blockquote text |
| A-12c | MINOR | Table 1 (p. 6) | R_M column wraps every value |  FIXED — the core column prints the ion symbol; the configurations are in the text above the table |
| A-12d | MINOR | pp. 5–7 | Table 1 and Table 2 captions orphaned at page feet |  FIXED — captions now follow their tables (as figure captions do), so none can be stranded; the shared template has since also been changed to let tables break |
| A-12e | MINOR | 304 (p. 13) | "⟨r^s⟩" literal caret |  FIXED — ⟨rˢ⟩ |
| A-13 | MAJOR | 310; SOURCES 141 | Ritz citation stripped though the tree holds it (Ann. Phys. 12, 264–310) |  FIXED — Ritz restored exactly as Mathematical Compendium 780 / Physics Compendium 464 give it (Zur Theorie der Serienspektren, Annalen der Physik 12, 264–310); SOURCES.md corrected |
| A-14 | MINOR | SOURCES 136 | SOURCES says Drake initials printed; paper prints none |  FIXED — Drake's and Swainson's initials and the title verified against the APS record and printed; SOURCES.md aligned |
| A-15 | MINOR | 305–313 | five journal expansions undeclared in SOURCES |  FIXED — SOURCES.md declares every expansion |
| A-16 | MINOR | 56, 132, Table 1 | m_p/m_e vs u/m_e; Rb isotope mass called atomic weight; printed R_M third decimal |  FIXED — D1 states A·m_p/m_e with the core mass as A proton masses, names the standard atomic weights of Cd and In and the ⁸⁵Rb and ⁸⁸Sr isotope masses, and says the convention moves δ by parts in 10⁷; no Rₘ recomputed |
| A-17 | MINOR | 56 | "nucleus" for ion core |  FIXED — "the electron and the ion core" |
| A-18 | MINOR | Table 2 | levels printed beyond NIST's quoted precision |  FIXED — Table 2 printed at NIST's quoted precision, generated by the check from the capture strings |
| A-19 | MAJOR | §0, §3, §5 | test at ℓ = 3, which the source places below Seaton's domain (ℓ ≥ 4); merged into R-12 |  FIXED (with R-12) — §0 and §5.2 say ℓ = 3 is the lowest ℓ available on these cores and the marginal case, and that departures of 10–56% are of the size expected at nf |
| A-20 | BLOCKING | 17, 30, 68, 252, 256 | "non-penetrating ⇔ p = 0" contradicted by collapsed p = 0 channels the record holds (Ba II nf, Ca II nd; Register 1261 regimes 3/4) |  FIXED — D3 makes p ≥ 1 "penetrating"; D4 defines N := p = 0 and uncollapsed with the collapse account (Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969, as the tree prints them); abstract, thesis, §0, §5.1, §5.3, §5.5 rewritten, a collapse bullet added; §5.3 re-examined (the argon-like d test is not clean; ℓ = 4 has p = 0 on every core); the obligation over the whole configuration table added |
| R-1 | BLOCKING | 98, 100 | = A-1 |  FIXED — = A-1 |
| R-2 | MAJOR | 86–92, 280 | Lemma 1 proved only to n ≤ 30; Theorem 1 PROVED on a CITED lemma; Kramers–Pasternack proof available |  FIXED — Lemma 1 proved for all n from the Kramers–Pasternack recursion (Pasternack 1937, CITED, verified by search) and ⟨r⁻²⟩ (Bethe & Salpeter 1957, CITED); the check verifies the recursion at 902 triples, the seeds on 435 states and the algebra on a rational grid; the 435-state computation kept as corroboration; Theorem 1's PROVED stands |
| R-3 | MAJOR | 102, §6 | = A-2 |  FIXED — = A-2 |
| R-4 | MINOR | 225, 234 | "Proposition" for a measurement |  FIXED — Measurement 1, Measurement 2 |
| R-5 | MINOR | 62 | model undefined at ℓ = 0, not "value 0" |  FIXED — D6: the formal value is 0, the model does not apply (K(0) = 0, ⟨r⁻⁴⟩ diverges) |
| R-6 | MINOR | 100 | division conditions mis-stated |  FIXED — "provided n ≠ δ and 2n ≠ δ" |
| R-7 | MINOR | 205, 286 | "certified" → "scan-certified" |  FIXED — "scan-certified" in §4 and §6 |
| R-8 | MINOR | 19 | = A-3 |  FIXED — = A-3 |
| R-9 | MINOR | 126 | = A-4 |  FIXED — = A-4 |
| R-10 | MINOR | 292 | = A-7 |  FIXED — = A-7 |
| R-11 | BLOCKING | 17, 68, 252, 256 | = A-20 (physicist's statement) |  FIXED — = A-20; D3 now says p is the count of radial nodes forced by orthogonality and that "penetrating" is the paper's label for p ≥ 1 |
| R-12 | MAJOR | 30, 254, §3 | nf is the marginal case; model's own δ₀ prediction from α_d not checked (Sr²⁺: 0.037 predicted vs 0.0648 fitted); includes A-19 |  FIXED — an "α implied" column (24.76, 26.20, 10.21 a₀³, from the check) and the marginal-ℓ statement added; the comparison with a published Sr²⁺ value is stated in §5.2 as NOT made and why (no published value could be verified against its source — arXiv, IOP and APS are blocked by the proxy); Mitroy, Safronova & Clark 2010 cited as where to make it; recorded for the author in SOURCES.md |
| R-13 | MAJOR | §4, Table 3, §5.4 | no per-series uncertainty; leave-lowest-out moves ρ by 0.05–0.10 |  FIXED — leave-lowest-out ρ (1.051 / 1.154 / 1.623), quotation-floor sums (0.016 / 0.002 / 0.002, by a linearised procedure stated in §4), Cd limit ±0.13 (1.120–1.180) and +0.1 cm⁻¹ sensitivities all in the check and in §4; Cd I stated as the range 1.05–1.15 |
| R-14 | MAJOR | 30, 254 | direction of the three corrections asserted; only the quadrupole's is derivable (and it is) |  FIXED — Lemma 4 derives ⟨r⁻⁵⟩ and ⟨r⁻⁶⟩ by the recursion (406 states, grid) and Corollary 1 machine-checks that a positive quadrupole term gives ρ > 1 at the coefficient level; the other two directions stated as undetermined; the q₄/n⁴ term named as unaccounted |
| R-15 | MINOR | 56, 132 | = A-16, A-17 |  FIXED — = A-16, A-17 |
| R-16 | MINOR | Table 2 | = A-18 |  FIXED — = A-18 |
| R-17 | MINOR | Table 3 | compare Rb fits with published Rydberg–Ritz coefficients |  DECLINED — the published Rb coefficients (Li et al. 2003; Mack et al. 2011) are not held in the tree and could not be verified against their sources here, and the paper prints no number on recollection; recorded in SOURCES.md for the author as a calibration worth adding |
| R-18 | MINOR | 266 | = A-9 |  FIXED — = A-9 |
| R-19 | MINOR | 264 | Cd II limit ±0.13 cm⁻¹ exceeds the Cd I f rms; propagate into ρ |  FIXED — ±0.13 cm⁻¹ propagated through the fit: ρ(Cd I f) 1.120–1.180; §5.5 names it the largest single sensitivity after the choice of members |
| R-20 | MINOR | 30 | "Seaton's derivation" → "the derivation" |  FIXED — "the derivation" |
| R-21 | MAJOR | title, 1, 3, 17, 104, 311 | "Seaton's ratio" / "as the literature attributes it" unsupported; retitle and restate the contribution |  FIXED — retitled (working title recorded in SOURCES.md with the old title and the reason); §0 states what is established and what is not claimed; a Provenance paragraph replaces the attribution sentence; Seaton 1958 cited for the quantum defect method only; no priority claimed |
| R-22 | MAJOR | References | missing standard references (Edlén 1964, Ritz 1903, Goeppert-Mayer 1941, Griffin–Andrew–Cowan 1969, Freeman–Kleppner 1976, Van Vleck–Whitelaw 1933, Gallagher 1994; conditionally Pasternack 1937, Li et al. 2003, Mack et al. 2011, Mitroy–Safronova–Clark 2010); Drake–Swainson title |  FIXED — Edlén 1964, Ritz 1903, Goeppert-Mayer 1941, Griffin–Andrew–Cowan 1969 (from the tree), Freeman–Kleppner 1976, Van Vleck–Whitelaw 1933, Gallagher 1994, Pasternack 1937, Mitroy–Safronova–Clark 2010 (verified by search) added with full author lists; Drake–Swainson title verified ("second-order polarization effects"); Van Vleck–Whitelaw's last page not verified and not printed; Li 2003 / Mack 2011 not added (R-17 declined) |
| R-23 | MAJOR | §6 | = A-2, A-6, A-7 |  FIXED — = A-2, A-6, A-7 |
| R-24 | MINOR | Abstract | "derives it exactly" vs cited Lemma 1 (= R-2 consequence) |  FIXED — abstract: "derives it from the hydrogenic expectation value ⟨r⁻⁴⟩ through the Kramers–Pasternack recursion" |
| R-25 | MINOR | 252, 307 | Hartree 1928 is the wrong citation for the penetration argument |  FIXED — Edlén 1964 cited for the penetration account; Hartree 1928 dropped |
| R-26 | MINOR | 310 | = A-13 |  FIXED — = A-13 |
| R-27 | MINOR | 132, 308 | retrieval date in the NIST reference entry |  FIXED — "[retrieved August 2026]" in the entry |
| R-28 | MINOR | 256 | "sixty to seventy-nine" window arbitrary |  FIXED — "every core from 58 electrons upward, 51 cores in the configuration table", from the check |
| R-29 | MINOR | 132 | "independent retrieval" overstates |  FIXED — "a second capture of the same tables — a guard against transcription, not independent evidence" |

**Counts (unique findings, 41).** BLOCKING 2 (A-1, A-20). MAJOR 11 (A-2, A-6, A-12a, A-12b, A-13,
R-2, R-12 with A-19, R-13, R-14, R-21, R-22). MINOR 28 (A-3, A-4, A-5, A-7, A-8, A-9, A-10, A-11,
A-12c, A-12d, A-12e, A-14, A-15, A-16, A-17, A-18, R-4, R-5, R-6, R-7, R-17, R-19, R-20, R-24, R-25,
R-27, R-28, R-29). Cross-references (R-1, R-3, R-8, R-9, R-10, R-11, R-15, R-16, R-18, R-23, R-26)
are not counted again.

**What stands.** All 22 obligations and the three negative controls; every printed number
reproduces; Table 2 is an exact bijection with the level data; Table 3 and the four class statistics
are correct; the fit is exact, single-basin and reproducible; lint is clean; the 3-of-10 accounting
for ρ on the penetrating branch is right and honestly stated; the paper's prefactor 6α_d z²/K(ℓ) is
the correct one (the source's is half of it) and `SOURCES.md` records that correctly.

---

## Repair record (2026-09-24)

Repaired by the drafter against every finding above; the findings are unchanged and each carries its
disposition in the table. **Dispositions:** BLOCKING 2 of 2 FIXED (A-1, A-20); MAJOR 11 of 11 FIXED
(A-2, A-6, A-12a, A-12b, A-13, R-2, R-12 with A-19, R-13, R-14, R-21, R-22); MINOR 27 FIXED and 1
DECLINED (R-17, with the reason in its row). Every cross-reference row carries the disposition of the
finding it points to.

**The two BLOCKING findings.** A-1: Lemma 2's rearrangement is now δ = −(n³/z²)ΔE·2(n−δ)²/(n(2n−δ)),
with 2(n−δ)²/(n(2n−δ)) = 1 − (3nδ − 2δ²)/(n(2n−δ)); both identities are exact obligations of `check.py`
(`ob_defect_rearrangement`, grids 4 × 4 and 7 × 5 × 3 above degree, 121 points) and the factor without the
2 is a fourth negative control of `--selftest`, so the printed identity can no longer pass unchecked.
Theorem 1's first-order conclusion was never affected and its status is unchanged. A-20 / R-11: the paper
no longer identifies non-penetrating with p = 0. D3 defines p and calls p ≥ 1 penetrating; D4 defines the
class N := p = 0 and uncollapsed, with the orbital-collapse account cited to Goeppert-Mayer 1941 and
Griffin, Andrew & Cowan 1969 exactly as the tree prints those references; the four cores' nuclear
charges (37, 38, 48, 49) are stated and are far below the 4f onset, so the three measured series are in N
and no number moved. The abstract, thesis, §0, §5.1, §5.3 and §5.5 were rewritten accordingly, a
collapse bullet added to §5.5, and §5.3's Ca II nd proposal replaced by the honest statement that the
argon-like cores with p = 0 at ℓ = 2 sit within two units of the 3d threshold and are not a clean test,
while ℓ = 4 has p = 0 on every core in the configuration table (a new obligation over all 108 cores).

**Title.** "A Correction to Seaton's Ratio" → "The Domain of the Polarisation Ratio δ₂/δ₀ = −ℓ(ℓ+1)/3: a
Necessary Condition from the Core Configuration, Tested on Thirteen Rydberg Series" — a working title,
recorded as such in `SOURCES.md` with the old title and the reason (R-21, A-13).

**Checks.** `python3 check.py`: 32 of 32 obligations discharged (7 PROVED, 11 EXHAUSTIVE, 2
MACHINE-CHECKED in 8 + 7 instances, 8 MEASURED, 1 CROSS-CHECK, 3 SOURCE), exit 0, ~35 s; `--selftest`:
36 of 36 with four negative controls each REFUTED. Ten obligations were added and none weakened;
no number moved to fit a sentence. `check.py` is what now prints Table 2 at NIST's quoted precision,
the implied polarisabilities, and every sensitivity §4 reports. Lint: 0 hits. The figures were
regenerated and `FIGURES.tsv` carries the new md5s; no plotted value changed.

**Render and typography.** RENDER_PLACEHOLDER

**Still open for the author** (recorded in `SOURCES.md`): the comparison of the implied polarisabilities
(24.76, 26.20, 10.21 a₀³) with published values — the paper says it is not made and why; the Rb I
calibration against the millimetre-wave / EIT coefficients (R-17, declined); the prefactor question
(the tree's 3αc²/K against the derived 6αz²/K, unchanged from the first pass); and the working title.
