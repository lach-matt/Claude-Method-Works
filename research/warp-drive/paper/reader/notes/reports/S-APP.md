# S-APP: printing the approximant on D\* and D_A in the paper

Report only. I edited no chapter, crosswalk or proof file and committed nothing. I read nothing under method/, drive/,
extracted/ or recovered/. What I read: chapter 87, Appendix B (chapters/96-tables.md), G0.md §§0–12, G0b.md (the
whole report), S-H123.md §§1, 4 and 7, G0's and G0b's scratch data and scripts (scratchpad/g0/), and the record's
docket68/n1star/data/ listing. Nothing here is proved. Every number carries one of three labels:
- **computed**: floating point, mine; the scripts and outputs are in `scratchpad/sapp/` (§7);
- **deduced**: an argument or a model given here;
- **record**: a figure from G0, G0b, S-H123, chapter 87 or the edition's files, cited where it stands.

The author has decided that the paper must stand alone: every coefficient of the approximant is printed, and the
residual is certified from the printed numbers. This report says how to print them compactly and how many pages that
takes.

---

## 0. Recommendation and page estimates

### 0.1 The four cases at G0b's targets

Targets are G0b §G0b.6 (record): weighted closing with a margin of 10. The level weight μ is the one at G0b's
M_w optimum, and φ is that optimum's weight, both record.

The printed object (deduced; §§3–5) is a set of spectral elements in (ξ, v), ξ = arsinh((u + 1)/0.002), with x a
single element on [−1, 1]:
- a C^∞ partition of unity on overlaps, each element used on the inner 90 % of its t- and σ-ranges;
- fields printed in the seed-subtracted form F = F_seed + (v − ½)⁴ G;
- the Chebyshev coefficients of G printed as integers z, with C = z × 10^(−p) and one quantum 10^(−p) per element and
  field, over the staircase |C| ≥ ½ × 10^(−p);
- the residual budget allocated by the weight e^(−φ/2) of G0's source norm ε_w.

**Pages at the edition's dense table format** (79 lines of at most 121 characters, as in sec:cone-tables; §0.3). All
pages are computed from the size model of §2.3 on measured decay rates.

| case (G0b target f) | layout (ξ × v elements) | printed entries | digits | **pages, worst-case rounding rule** | pages, expected rounding rule | pages if the decay is 30 % slower | pages at the paragraph density of sec:tab-d |
|---|---|---|---|---|---|---|---|
| seed 1, D\* (10^−21.9) | 3 × 2 | 1.46 × 10⁶ | 12.1 × 10⁶ | **1,740** | 1,530 | 5,730 | 3,040 |
| seed 2, D\* (10^−19.1) | 2 × 2 | 0.98 × 10⁶ | 8.05 × 10⁶ | **1,160** | 1,020 | 3,860 | 2,020 |
| seed 1, D_A (10^−16.5) | 2 × 2 | 0.42 × 10⁶ | 3.08 × 10⁶ | **450** | 395 | 1,520 | 790 |
| seed 2, D_A (10^−15.6) | 2 × 2 | 0.41 × 10⁶ | 2.88 × 10⁶ | **425** | 370 | 1,440 | 740 |

How to read the columns:
- *Worst-case rule.* The rounding errors and the omitted coefficients are added up as if every one of them pushed the
  residual the same way. This guarantees in advance that rounding cannot spoil the certified residual.
- *Expected rule.* The rounding errors are treated as independent, so they add in quadrature. The certification is
  done on the printed numbers anyway, so this is what will happen in practice.
- *Slower decay.* Every ln ρ is multiplied by 0.7. This is the main uncertainty (§6 item 1).
- The edition today has **1,948 pages** (record: the PDF's page count), and Appendix B's integer tables occupy about
  186 of them (computed from the PDF).

### 0.2 The same objects on the f grid of the brief (pages, dense format, worst-case rule; computed)

| region, seed | layout | f = 10⁻¹⁵ | 10⁻²⁰ | 10⁻²⁵ | 10⁻³⁰ |
|---|---|---|---|---|---|
| D\*, seed 1 (μ = 10⁻⁴) | 3 × 2 | 615 (0.64 × 10⁶ entries) | 1,344 (1.19 × 10⁶) | 2,561 (1.98 × 10⁶) | 4,437 (3.05 × 10⁶) |
| D\*, seed 2 (μ = 10⁻³) | 2 × 2 | 638 (0.61 × 10⁶) | 1,304 (1.08 × 10⁶) | 2,365 (1.72 × 10⁶) | 3,944 (2.55 × 10⁶) |
| D_A, seed 1 (μ = 10⁻³) | 2 × 2 | 356 (0.35 × 10⁶) | 741 (0.62 × 10⁶) | 1,362 (1.00 × 10⁶) | 2,291 (1.50 × 10⁶) |
| D_A, seed 2 (μ = 10⁻³) | 2 × 2 | 386 (0.38 × 10⁶) | 799 (0.67 × 10⁶) | 1,460 (1.07 × 10⁶) | 2,449 (1.60 × 10⁶) |

- The average entry carries 6.4–7.1 digits at f = 10⁻¹⁵, rising to 10.5–11.2 at f = 10⁻³⁰.
- Each decade of f costs about 12–17 % more pages near the targets (computed from the table).
- The largest degrees per element (t, σ, x) at the targets are (computed):
  - seed 1, D\*: (60, 93, 134);
  - seed 2, D\*: (80, 77, 88);
  - seed 1, D_A: (42, 56, 79);
  - seed 2, D_A: (42, 65, 74).
- They grow by about 2–5 per decade of f in each direction, fastest in x.

### 0.3 The print density assumed

- **The edition (computed from the PDF's text layer).**
  - The indented tables, e.g. sec:cone-table-c1, set 79 lines per A4 page of at most 125 characters.
  - The paragraph-set integer tables of sec:tab-d-coefficients set 46 lines per page of at most 119 characters.
  - The whole edition averages about 4.3 kB of PAPER.md per page (8,408,647 bytes over 1,948 pages; computed from
    record sizes).
- **Assumed here:** the indented format, 79 lines × 121 characters, with 86 % of the cells used. The rest goes to row
  labels, line checks and line-wrap waste (§4): the specimen of §4.4 measures an overhead of 1.15–1.20 over digits,
  signs and separators. That gives **8,220 useful characters per page**.
- An entry costs its digits, plus a minus sign for about half of the entries, plus one space.

### 0.4 Recommendation

1. **Representation:** the one in §0.1. Each piece earns its place:
   - Absolute-precision rounding and the staircase together print about 1/22 of the digits of a full degree box written
     at fixed width (computed, §3c). They are what makes printing possible at all.
   - The weight allocation is worth −11 to −25 % (computed).
   - Overlapping elements with interior use are worth −30 to −39 % (computed, including their 23 % volume overhead).
   - Seed subtraction is worth −4 to −6 % (computed), but it also makes the approximant agree with the seed's 3-jet on N₀
     exactly, which G0b's L1 requires anyway.
   - Low rank, parity, eliminating fields by constraints, and coarse-plus-correction tables bring nothing, or break the
     "finite computation on printed numbers" property (§3).
2. **Precision:** print each case at its G0b target divided by 10. This leaves one decade for the slack of the
   certified bound over the true residual. It costs about +13–17 % pages (computed from §0.2).
   - Plan the page budget on the worst-case rule. Expect the expected-rule figure.
   - G0b used the D\* conversion ε ≈ 2.5 × 10² f for D_A too. On D_A the conversion is ε ≈ 76 f (computed, `ralloc.py`),
     so D_A's targets could be about 0.5 decades looser (−5 % pages).
3. **D_A first.**
   - It is about 400–450 pages (370–400 expected; up to about 1,500 if the decay is slower than measured).
   - It needs only double-double precision, and it is GO at both seeds in G0b.
   - Seed 1 and seed 2 cost the same within 6 %. Choose the seed by where D\* will be done: G0b has seed 2's D\* GO
     and seed 1's in between.
   - Then **D\* at seed 2**: about 1,160 pages (1,020 expected; up to about 3,900). Its table supersedes seed 2's D_A
     table, because the D\* approximant restricted to D_A meets D_A's looser target. If seed 2's D\* closing is firm
     before printing starts, print only the D\* table.
   - Seed 1's D\* is about 1,740 pages (up to about 5,700). Do not print it until its closing is GO.
4. **Placement:**
   - A new **Appendix C** after Appendix B, about 10–15 pages, with:
     - the definition of the printed approximant: the element map, the partition of unity and the seed form;
     - the format and the checks;
     - the certification procedure as mathematics (§5);
     - the certified outcomes, one bound per element, plus the rate tables of L7.
   - The coefficient tables themselves go in a **separate final part of the paper** ("Tables of the approximant"),
     after the references. It can be bound as a second volume and is paginated on.
   - Reason: at 400–1,800 pages they would add 20–90 % to the edition and push the references and the index away from
     the text. A part can grow from the D_A table to the D\* table without moving anything else.
   - For D_A alone, the tables would also fit inside Appendix C itself.
5. **What the paper text then says** (deduced). Appendix B's existing statement "the certified residual is computed
   from the printed (exact decimal) coefficients themselves" carries over word for word: the approximant is defined
   by the printed integers and the explicit formulas of Appendix C.

---

## 1. Data used and how far it can be trusted

**The data (record: G0 §6.3, G0b §G0b.4).** I used the record's double-null solver runs, made by G0 and G0b, on
u ∈ [−10, −1.05], v ∈ [0, 3.6]:
- seed 1: `runs/d1_M24_264.npz` (M = 24 angular nodes, 264 × 288 null grid) and `d1_M16_{132,264,528}.npz`;
- seed 2: `runs/d2_*` likewise;
- also G0's single-element Chebyshev fit `appC_R528_264_40_48.npz` and the record's `rcert5_C3R.npz` (listing only;
  S-H123 §4 already reports its rates).

**What I did with them (computed).** On each element:
- resample at Chebyshev–Lobatto nodes of degree 32–48 in t and σ (8-point Lagrange, as G0's fitD2);
- convert to coefficients c_ijk, with x through the 24 Chebyshev–Gauss nodes (degree 23).

**Noise floors (computed).**
- *Resampling.* The 8-point and 12-point resamplings differ by 10⁻¹²–10⁻¹⁵ relative, and the coefficient envelopes
  are clean down to about 10⁻¹¹ (`elemdecay.py`).
- *The runs' own error.* It is 10⁻⁵–10⁻⁹. The Richardson differences are 10⁻⁷–10⁻⁵ (computed), and the run differs
  from the exact seed by 5 × 10⁻⁵ on v ≤ ½ (computed, `seedsub.py`).
- This error is smooth (it is h² times derivatives of the solution), so the decay rates measured below it still
  describe a function with the solution's analyticity (deduced). They are measured over about 10 decades. The tables
  need 26–33 (§2.3), so every page count is an extrapolation (§6 item 1).

**Seed 1's corner is not converged in angle (computed, `xdecay.py`).**
- Near (u\*, v ≥ 2), the x-coefficients of the M = 16 and M = 24 runs differ by up to 5 × 10⁻⁴ in s and 2 × 10⁻⁴ in
  m, at every degree.
- The M = 24 spectra of m and n there have a plateau near 5 × 10⁻⁶ for k ≥ 13. This matches G0 §6.3: angular
  truncation dominates there (record).
- At seed 2 the two runs agree to 1.6 × 10⁻⁵ (record, G0b §G0b.4).

---

## 2. Resolution: decay rates, degrees, element counts

### 2.1 x (computed: `xdecay.py`, `xmap.py`, `tsdecay.py`)

- **The data fix an upper bound on the x-rate.** On N₁, m and n carry h(x) = (2/(1 + x²))^½ (eq:cone-data, record).
  Its poles at x = ±i bound the Chebyshev rate on [−1, 1] by 1 + √2 = 2.414 (deduced).
- **Measured over most of D\*.** ρ_x ≈ 2.2–3.0 per degree for every field, at both seeds; the median over D\* nodes is
  2.4–2.8.
- **Seed 1, u ∈ [−1.2, −1.1], v ∈ [2, 3.5].** ρ_x falls to 1.6–1.9. The shift s is the slowest, at ρ ≈ 1.6 at
  (u\*, 2.5), with a clean geometric spectrum (amplitude 2.8 down to 10⁻⁵ at k = 22).
  - Its signs alternate strictly, so the nearest singularity is real and just beyond the axis x = −1, at
    x ≈ −1.11 (deduced from the rate).
  - G0b found the largest |s| (6.1) and |π^E| there, at x = −0.993 (record).
- **Seed 2 has no such slow region.** ρ_x ≥ 2.3 everywhere measured (computed, `rates_s2_*`); G0b reports a shift
  eight times smaller (record).
- **Splitting x does not pay (deduced, from the singularity model ρ = a + √(a² − 1)).**
  - Splitting [−1, 1] at −0.8 gives ρ ≈ 3.95 on the small piece. The large piece is then limited to ρ ≈ 2.24 by the
    same singularity.
  - The total cost Σ 1/ln ρ is 1.97, against 1.88 for one element at ρ = 1.7. A graded triple is worse still.
  - Against the data's poles at ±i, two halves cost 2/ln 4.61 = 1.31 against 1/ln 2.414 = 1.13.
- **No x-parity (computed).** Even and odd x-coefficients are of the same size: for m over D\*, the largest even one
  is 0.18 and the largest odd one 0.25. The reflection x → −x, φ1 ↔ φ2 maps (m, n) to (n, m), and the data
  (m = hφ cos θ, n = hφ sin θ) are not invariant under it (deduced).

### 2.2 t (u in the arsinh map) and σ (v) (computed: `elemdecay.py`, `rates.py`, `rates_table.out`)

| element size | ρ_t (min over fields) | ρ_σ (min over fields) |
|---|---|---|
| one element on D\* (Δξ = 4.5, Δv = 3) | 1.9–3.2 | 1.5–1.6 |
| 2 × 2 on D\* (Δξ = 2.25, Δv = 1.5) | 2.7–5.5 | 2.2–3.0 |
| 3 × 3 on D\* (Δξ = 1.5, Δv = 1) | 3.5–11 (R: 11–16) | 2.7–6 |
| 6 × 6 on D\* (Δξ = 0.75, Δv = 0.5) | 7–30 | 5–12 |

- The slowest decay in σ is near u\* at v ∈ [1.5, 3.5]: 2.2–2.4 on the 2 × 2 elements, at both seeds. This is the
  envelope's peak near the horizon.
- The slowest decay in t is in m and n at late v in the far element.
- Far from the horizon the v-dependence is super-geometric: the data are entire in v. A geometric extrapolation is
  therefore conservative there (deduced).

### 2.3 From rates to degrees, entries and digits: the size model (deduced; `model.py`)

**Coefficient model.**
- Per element and field, |C_ijk| = A 10^dq ρ_t^(−i) ρ_σ^(−j) ρ_x^(−k), with the measured A and ρ.
- dq calibrates the separable model to the measured count #{|C| > A 10^(−q)} at q = 6 (q = 4 where 24 x-modes saturate).
  Measured dq lies between −4 and +3.5 (computed).
- Without dq the separable model undercounts m and s by a factor of 2 at q = 8 (computed, `tensor3d.py`).

**The printed set and the error budget.**
- Print z = round(C/δ) on the staircase |C| ≥ δ/2. The omitted coefficients and the rounding errors move the residual
  through derivative weights w_ijk = κ W_Ric W_Γ, with κ = 2 and the five fields sharing the budget equally.
- *W_Ric: two derivatives in curvature units (f_ab = ρ Ric, ρ = R⁴/√72).* The scales are
  - L_c|dt/du|/(2Ω²) in t;
  - 2L_c/Δv in σ;
  - 0.69R in x,
  with L_c = R²/72^(1/4). In x the frame field is √(1 − x²)∂_x, so the growth is k per derivative. In t and σ it is
  the Markov endpoint value T_n^(l)(1) = Π_(r<l)(n² − r²)/(2r + 1), or the interior value (n/√(2η − η²))^l when
  each element is used only on |t| ≤ 1 − η (§3b).
- *W_Γ: the level-3 commutation fields with G0's weights.* It is max over l ≤ 3 of μ^(l/2)(growth × scale)^l, with
  scales |dt/du|/2, 2/Δv and 2 (for x). This is the "derivative loss on the coefficients".
  - It also checks G0b's assumption that the residual's Γ-derivatives contribute ≤ (10√μ)^j. For a residual limited by
    truncation at degree n the factor is larger; the model pays for that with digits, so G0b's conversion
    ε ≈ 2.5 × 10² f stays valid for the printed object (deduced).
- *The rule.*
  - Worst case: Σ min(|C|, δ/2) w ≤ f_e/5.
  - Expected: omissions + (δ/√12)(Σw²)^½ ≤ f_e/5.
- *The target per element.* Either f_e = f, or the allocated target f_e = f e^(φ_min,e/2) (§3g).

**What the derivative loss costs (computed).** The quanta that satisfy the budget sit 10–14 decades below f:
- p = 26–30 for seed 1's D_A (target 10^−16.5);
- p = 29–33 for seed 2's D\* (target 10^−19.1).
The far field needs the smallest quanta. There the curvature length is L_c ≈ 50 (R ≈ 10–12), so the far elements
carry about 55 % of all entries: 57 % for seed 2's D\* (u ≤ −1.95) and 55 % for seed 1's D_A (u ≤ −4) (computed,
`detail_*.out`).

**Element counts (computed; worst-case rule, allocated target, Markov growth, the case's target).**

| case | 1 × 1 | 2 × 2 | 2 × 3 | 3 × 2 | 3 × 3 |
|---|---|---|---|---|---|
| seed 1, D\* | — | 1.93 × 10⁶ | 2.01 × 10⁶ | **1.91 × 10⁶** | 1.98 × 10⁶ |
| seed 2, D\* | — | **1.32 × 10⁶** | 1.48 × 10⁶ | — | 1.56 × 10⁶ |
| seed 1, D_A | 0.66 × 10⁶ | **0.60 × 10⁶** | 0.67 × 10⁶ | — | 0.78 × 10⁶ |
| seed 2, D_A | 0.73 × 10⁶ | **0.60 × 10⁶** | 0.70 × 10⁶ | — | — |

- On seed 1's D\* with G0's μ = 10⁻⁵, at f = 10⁻²⁰ and uniform f: one element needs 3.8 × 10⁶ entries (degrees up to
  155 × 251 × 181), while 2 × 2 needs 1.7 × 10⁶. 4 × 6 and 6 × 6 are worse (2.6 × 10⁶ and 3.1 × 10⁶): the rates grow
  only logarithmically as the elements shrink, and the element count grows linearly.
- **The optimum is 4–6 elements.** x needs 75–135 modes in every case: most of the information is the angular
  structure.

**For comparison (record).** S-H123 estimated 2 × 10⁶–10⁷ coefficients for D\* at quad-double precision without compression; Appendix B
prints 124,000 integers for the two Π approximants.

---

## 3. Compression: what each lever does and whether certification stays a finite computation on printed numbers

The lever ladder for seed 1's D\* at its target (3 × 2; pages at the dense format, computed):
1. uniform target, Markov growth, worst-case rule: 2.39 × 10⁶ entries, **3,450 pages**;
2. + allocation by e^(−φ/2): 1.91 × 10⁶, **2,580**;
3. + overlapping elements used on their inner 90 % (×1.23 volume overhead included): 1.52 × 10⁶, **1,820**;
4. + seed subtraction: 1.46 × 10⁶, **1,740**;
5. expected rounding rule instead of worst case: 1.32 × 10⁶, **1,530**.

Seed 1's D_A (2 × 2): 866 → 741 → 478 → 451 → 395. Seed 2's D\*: 2,112 → 1,798 → 1,212 → 1,158 → 1,022. Seed 2's
D_A: 832 → 737 → 452 → 425 → 371. All computed.

**(a) Symmetry. No gain** (computed, §2.1).
- The class form already uses T² and reduces to three variables.
- There is no x-parity, and the reflection exchanging the two circles is not a symmetry of the data.
- Certification is unaffected.

**(b) Adaptive elements. Factor about 2 against one element** (computed, §2.3). They also enable (g) and the
interior-growth lever.
- The arsinh map in u already does the near-u\* refinement. Equal splits in ξ and v, 2 × 2 or 3 × 2, are best;
  finer is worse.
- *Smoothness across elements (deduced).* lem:tl5-continuation wants a smooth ĝ, so the pieces must be glued by an
  explicit C^∞ partition of unity on overlaps, for instance products χ_a(ξ)ψ_b(v) built from e^(−1/s).
- That lets each element be used only on its inner part, |t|, |σ| ≤ 0.9. Bernstein's inequality then replaces the
  endpoint growth n^(2l) by (2.29n)^l. This is worth 30 % after paying the 23 % overlap volume (computed).
- The blend's own derivatives, about (1/(2ηh))^l, are far below the polynomials' (deduced). On the overlaps, the
  neighbouring elements' approximants must agree to their own accuracy, which they do since both approximate the same
  solution.
- *Certification stays finite* (deduced): the blend is an explicit formula, and its jets enter the residual formula like
  any other jet.
- x stays one element (§2.1).

**(c) Absolute-precision rounding and the staircase. The decisive lever** (computed, §2.3).
- One quantum 10^(−p) per element and field. Every coefficient is printed as an integer multiple of it, and all
  |C| < δ/2 are zero and not printed.
- The staircase holds 17.5–18 % of the full box (n_t + 1)(n_σ + 1)(n_x + 1) at each block's largest degrees.
- The average entry carries 7.3–8.2 digits at the targets, against p + 1 ≈ 27–34 for a fixed width at the same
  quantum.
- Together: **4.5 % of the digits of the full box**, a factor of about 22.
- The existing sec:tab-d tables already use this idea in a cruder form: one quantum, 10⁻¹⁸, and a full box (record).
- *Certification is exact* (deduced): the approximant is defined by the printed integers; nothing is rounded after
  printing.

**(d) Low-rank structure (Tucker / tensor train). No gain** (computed, `measure.py`).
- The multilinear (HOSVD) ranks at the threshold A 10^(−q) are 0.7–0.9 of the degrees in every mode.
- The Tucker storage r_t r_σ r_x + Σ n_d r_d is 1–3 × the staircase count at q = 2–8, on every element measured.
- The coefficients decay with the *sum* of the indices, the signature of analyticity, which the staircase already
  exploits. A product structure is not present beyond that.
- Certification would stay finite (products of printed factor series), but there is nothing to gain.

**(e) Fewer printed fields, the rest from formulas.**
- *Constraints.* Ric_vv = 0 (Raychaudhuri) would give R from (m, n, W), and Ric_vx = 0 would give s; G0b's L1 makes the
  same remark for the data. Either way the field is fixed by an ODE along each generator, not by an explicit formula.
  The approximant would then be defined by solutions of a (u, x)-parametrised family of ODEs. Certifying it needs
  validated ODE enclosures, not arithmetic on printed numbers, and it saves at most one field in five: about 4 % of the
  digits for R after seed subtraction. **Not recommended** (deduced).
- *Gauge.* In the double-null class form the only free functions are reparametrisations u ↦ U(u) and v ↦ V(v). They
  cannot remove W(u, v, x) or any other field (deduced).
- *The seed.* What does work is the exact seed (lem:tl5-seed): F = F_seed + (v − ½)⁴G for F = R, W, and F = (v − ½)⁴G for
  m, n, s.
  - The solution agrees with the seed to C³ across N₀, so G is analytic on D\* (deduced; record: G0b L1 item 1).
  - It lowers the amplitudes of R by 2–4 decades and of W by 1–3, at unchanged rates (computed, `seedsub.py`): −4 %
    pages.
  - It makes the 3-jet match on N₀ exact by construction.
  - *Certification stays finite* (deduced): the seed's jets are enclosed by interval Newton on
    F(R) = e^(v−2u)(u + 1)/(u − 1), as for lem:tl5-seed.

**(f) Coarse approximant plus correction. No gain beyond (c) and (e)** (deduced).
- Absolute-precision rounding already prints exactly the information of "the leading digits plus a correction".
- Two tables would repeat the staircase description and the headers.
- The one useful coarse part is the exact seed, i.e. (e).

**(g) Not in the brief: allocate the residual by the norm's own weight.** It is worth −11 to −25 % (computed, §3
ladder), and it is deduced from G0 §8.2 (record: ε_w = ‖2Ric(ĝ)‖ with the weight e^(−φ/2)).
- Put f_e := f e^(φ_min,e/2) on element e. Since φ ≥ φ_min,e on e, ε_w(ĝ) ≤ ε_r(f) exactly, and the closing is
  unchanged.
- Under G0's φ at μ = 10⁻⁵ (computed, `phimap.py`), e^(φ/2) grows from 1 at (−10, ½) to 10^(10.6) at (u\*, 7/2): it
  is 10^(6.5) at (u\*, ½) and 10^(4.1) at (−10, 7/2).
- The corner (u\*, 7/2), G0b's hardest place, is where the relaxation is largest.
- G0b's careful count lowers the level-3 F² (log₁₀F₃² = 18.37 for seed 1's D\* at μ = 10⁻⁴, record). I rescaled G0's
  φ to G0b's total for each case. Seed 2 borrows seed 1's shape (estimate).
- *Certification stays finite* (deduced): the bound per element is f e^(φ_min,e/2), with φ from L7's certified,
  printed rates.
- **A second allocation was tried and does not pay (computed, `ralloc.py`).** The norm weights |Ric| by Ω²R^(3/2). Letting
  f grow like (R/R_min)^(5/2) relaxes the far field by 2.5 decades but must lower f everywhere by 1.17 decades.

**(h) Not in the brief: the rounding rule** (computed).
- The worst-case rule is the a priori guarantee.
- The expected rule (independent rounding errors) saves 12–13 %.
- Since the certificate is computed on the printed numbers, the expected rule is safe in practice. If an element then
  fails its certificate, only that element is reprinted with p + 1.

---

## 4. The printed format

### 4.1 What is printed (deduced)

**Appendix C** (definitions):
1. The element map:
   - the ξ-breakpoints and v-breakpoints as exact decimals;
   - a = 1/500;
   - the affine maps to (t, σ) on each enlarged element;
   - the overlap fraction η = 1/10.
2. The partition of unity: its 1D factors as explicit formulas.
3. The seed form F = F_seed + (v − ½)⁴ Σ_e χ_e G_e^F, with G_e^F(t, σ, x) = Σ z^(e,F)_ijk 10^(−p_eF) T_i(t)T_j(σ)T_k(x).
4. The format and checks, below.
5. The certification procedure (§5), with every parameter fixed: boxes or nodes, orders, working precision.
6. The certified bounds, one per element and residual component, rounded up. Then ε_w.

**The tables part:** for each element e (in order a, then b) and each field F (R, m, n, W, s, as in sec:tab-d), one
block.

### 4.2 A block (deduced)

**The header** gives:
- the element (a, b), its ξ- and v-intervals, and the field;
- p (the quantum 10^(−p));
- the number of rows and the number of entries;
- three exact integers:
  - S1 := Σ z = 10^p G(1, 1, 1);
  - S2 := Σ (−1)^(i+j+k) z = 10^p G(−1, −1, −1);
  - S0 := Σ over even i, j, k of (−1)^((i+j+k)/2) z = 10^p G(0, 0, 0), using T_n(0) = cos(nπ/2).

**The rows:**
- Row (i, j) lists z_ij0, z_ij1, …, z_ijK in order of k. The x-index is innermost because x has the most modes, so
  rows are long and the staircase is described by the row lengths alone.
- K(i, j) is the row's length: its last entry is non-zero. Rows with no entry are omitted. Rows come in order of i,
  then j.
- An entry is a decimal integer without leading zeros, with "−" for negatives (as in the edition) and "0" for an
  interior zero.
- A row longer than a line continues on lines labelled "+".

**The lines:**
- at most 121 characters, set as an indented table like sec:cone-tables;
- a label of 8 characters ("(i,j)" or "+");
- the entries, separated by single spaces;
- at the end, " |cc".

### 4.3 Check digits (deduced)

- **Line check:** cc := (Σ_m m z_m) mod 97, over the integers z₁, z₂, … of that line, written as two digits.
  - 97 is prime and exceeds the number of entries per line (≤ 30) and every digit, so it detects:
    - every single-digit error (the change is d · 10^r · m);
    - every transposition of adjacent digits within an entry (the change is 9(d − d′)10^r · m);
    - every sign error on an entry z ≢ 0 (mod 97).
  - It misses about 1 in 97 of the swaps of two entries and of the dropped or duplicated entries.
- **Block checks:** the entry count and S1, S2, S0. These are exact and are values of the printed field at three
  points, so they catch what a line check misses, including a misplaced line.
- **A decay check without arithmetic:** within a row the number of digits falls roughly linearly in k. A long entry
  where short ones are expected is a transcription error.

### 4.4 Specimen (computed, `specimen.py`)

Seed 1, element ξ ∈ [−7.605, −6.105] (u ∈ [−3.01, −1.45]), v ∈ [3/2, 5/2], field m. These are provisional data rounded
at p = 12: this shows the format, not the final numbers.

    element (2, 2): xi in [-7.605077, -6.105173], v in [3/2, 5/2]; field m; p = 12; rows 213; entries 3864;
    S1 = −60066532560,  S2 = 1444965316,  S0 = −71331079114
        (0,0)    −45899457226 5685535854 −845328613 372183230 −60710058 15182605 1830190 −1529894 −42129 304225 −59541 −42846 |28
        +        19752 1773 −1407 −2071 2416 −1786 1437 −1212 961 −646 223 1 |05
        (0,1)    −23174155817 954201590 −3849307270 927269517 −138957305 13651275 5045272 −396979 −328516 171564 −35028 −16244 |31
        +        14475 −2837 −1088 −333 1571 −1522 1104 −808 636 −418 96 |02

- The labels, checks and wrapping cost a factor of 1.15–1.20 over digits, signs and separators (computed at p = 12, 16
  and 20). That is the 86 % utilisation of §0.3.
- At the targets' p = 26–33, the first entries have 25–33 digits and the rows run to k ≈ 75–135.

---

## 5. How the paper describes the certification, so a reader can re-run it (deduced)

Stated as mathematics, for any arbitrary-precision interval or ball arithmetic. The paper fixes every parameter.

1. **Exact coefficients.** C = z × 10^(−p) is an exact rational. The fields on element e are polynomials in (t, σ, x).
   Their derivatives are polynomials whose Chebyshev coefficients follow exactly from eq:tl5-cheb-derivative.
   - Those coefficient sums, with T_n^(l)(1) as in lem:tl5-rounding, bound the derivatives on boxes.
   - Clenshaw's recurrence evaluates the polynomials at interval arguments.
2. **The other ingredients.** Enclosures on boxes of:
   - the seed's jets (interval Newton on F(R) = e^(v−2u)(u + 1)/(u − 1), lem:tl5-seed);
   - the partition of unity's jets (explicit);
   - the chart: ξ = arsinh((u + 1)/a), eq:tl5-chain.
3. **The residual.**
   - f_ab, and μ^(|I|/2)Γ^I f_ab for |I| ≤ 3, are explicit expressions in the 5-jets of the five fields: eq:tl5-components,
     eq:tl5-derivatives and eq:tl5-frame-derivatives, plus the commutation fields T and E_ab written out.
   - **One prerequisite:** the chapter's formula contains 1/(1 ± x), x/w and (1 + x²)/w² (eq:tl5-derivatives). These
     cancel only in combination, so intervals that reach x = ±1 would blow up. The certified points and boxes of
     sec:tl5-residuals avoid the axes, and G0b's L6 needs the whole of D (record).
   - L6 must therefore state f_ab in an axis-regular form, with the removable singularities cancelled symbolically.
     This is not an obstacle for the printed object (deduced): with P = (2(1 + x)m − (1 − x)n)/3 and Q likewise,
     2P + Q = 0 at x = −1 and P + 2Q = 0 at x = +1 for any m, n, which are the no-cone conditions, and b = (1 − x²)s.
     So any printed polynomials define a metric that is smooth across the axes.
4. **The enclosure.** One of two methods, both finite and both already in the chapter in smaller form.
   - **(A) Taylor models on boxes**, extending lem:tl5-taylor, lem:tl5-field-box and sec:tl5-enclosures to order K.
     Partition each element into boxes; on each box form the fields' Taylor polynomials of order K at the centre (exact
     rationals) with interval remainders from coefficient sums. Propagate them through the formula one operation at a
     time, in the order the paper fixes. The bound on the box is the sup of the resulting interval polynomial plus its
     remainder.
   - **(B) Interpolation of the residual** (S-H123 §4, record). Evaluate each component at the tensor Chebyshev nodes
     of degree N per direction in ball arithmetic, and transform to coefficients in interval arithmetic. Bound the
     interpolation error by the maximum on a polyellipse, as in lem:cone-ellipse extended to three factors. That
     maximum is enclosed by covering the polyellipse with complex boxes, which is valid because every ingredient is
     analytic near the element once the formula is axis-regular.
   - The paper prints the method's parameters: box partition, K, N, ellipse parameters and working precision. For
     δ = 10^(−p) with p ≈ 30, about p + 15 decimal digits (≈ 150–200 bits) suffice.
5. **The outcome.**
   - Per element: the printed bound B_e ≥ the computed sup of max_ab max_(|I|≤3) μ^(|I|/2)|Γ^I f_ab|. The check is
     B_e ≤ f e^(φ_min,e/2).
   - Then ε_w ≤ Σ_e (conversion integral over e) B_e e^(−φ_min,e/2). The conversion integral is computed like G0's
     epsconv.py, over the seed's geometry with the approximant's R, Ω.
   - The rates (a_o, a_i) and φ are L7's printed piecewise-linear functions.
6. **What the reader needs:** the printed integers, the formulas of chapter 87 and Appendix C, and an interval
   arithmetic. No file and no code.
   - The cost is S-H123's estimate: about 10³ s of ball arithmetic per element at 128–256 bits (record). The 4–6
     elements here give hours.

---

## 6. Risks

1. **Extrapolation of the decay (the largest uncertainty).**
   - The rates are measured over about 10 decades. The tables need 26–33 decades of coefficient magnitude.
   - If the asymptotic decay is 30 % slower in every direction, every page count is ×3.3 (computed, `slow.py`).
   - Super-geometric v-behaviour far from the horizon argues the other way (deduced).
   - The first spectral solver runs at quad-double (S-H123 §7's L6a) will settle this; re-run this model on them.
2. **Seed 1's corner.** Its x-rates come from an angularly unconverged run (§1). G0b's "hardest place" is also where
   this report's rates are least certain. Seed 2 does not have the problem.
3. **φ for the allocation** is G0's shape rescaled to G0b's totals, and seed 2's is borrowed from seed 1. If the
   allocation is not used, add 12–34 % to the pages (computed, §3 ladder).
4. **The derivative weights are a model.** κ = 2, the curvature-unit scales at each element's largest R, and the
   maximum over directions. A factor of 10 in the weights moves the pages by about 10 %, since it moves p by one
   (deduced).
5. **The partition of unity** adds the blend's jets to the residual formula and needs the overlap mismatch to be
   certified too. Both are finite (deduced). The 1.23 overhead assumes η = 0.1.
6. **Margin for the certificate.** The certified bound exceeds the true residual. One decade is budgeted (§0.4 item 2,
   about +13–17 % pages).
7. **The page density** assumes the indented-table font of sec:cone-tables (79 lines). At the paragraph setting of
   sec:tab-d, the pages are ×1.75 (§0.1 last column).

---

## 7. Files (all under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/sapp/`)

| file | what |
|---|---|
| `xdecay.py`, `xdecay.out` | x-spectra of the five fields per (u, v) region, M = 24 and M = 16, parity split, M16–M24 differences |
| `xmap.py`, `xmap.out` | map of ρ_x(u, v); spectra near (u\*, v) |
| `tsdecay.py`, `tsdecay.out` | sign pattern of s's x-spectrum (the singularity beyond x = −1); t and σ decay of G0's single-element fit |
| `elemdecay.py`, `elemdecay.out` | t and σ decay per element on the Richardson data, with the noise and resampling floors |
| `tensor3d.py`, `t3d_1_1.out` | 3D coefficient tensors per element; empirical counts against the separable model |
| `measure.py`, `measure_*.json` | per-element counts and Tucker (HOSVD) ranks against degrees |
| `rates.py`, `rates_*.json`, `rates_*.out`, `rates_table.out` | per-element rates and calibrations, seeds 1 and 2, D\* and D_A layouts |
| `phimap.py`, `phimap.out` | e^(φ/2) over D\* and D_A from G0's stored level-3 rates |
| `ralloc.py`, `ralloc.out` | ε/f on D\* (231) and D_A (76); the R-weighted allocation |
| `seedsub.py`, `seedsub.out` | amplitudes and rates of F − F_seed and of (F − F_seed)/(v − ½)⁴ |
| `model.py` | the size model: lattice, derivative weights (Markov or interior growth), rounding rules, allocation |
| `cases.py`, `case_*.out`, `case_*.json` | the four cases on candidate layouts, uniform and allocated, on the f grid |
| `variants.py`, `var_*.out`, `var_*.json` | the best layout per case with the levers stacked (V1–V3) |
| `slow.py`, `slow_*.out` | the 30 %-slower-decay sensitivity |
| `detail.py`, `detail_*.out` | per element and field: quantum p, entries, degrees |
| `specimen.py`, `specimen.out`, `spec_p.py` | the format specimen and its measured overhead |
| `model_*.out` | first layout scan (seed 1, D\*, G0's μ = 10⁻⁵) |
| `ed.txt` | the edition's text layer (pdftotext of the repository's PDF), used only to measure lines per page |
