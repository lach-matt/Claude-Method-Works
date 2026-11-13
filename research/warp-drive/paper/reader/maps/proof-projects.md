# Proof projects: the 88 ANALYTIC and NUMERIC-ONLY programs, for an edition without code

Planning note, 2026-11-13. Inputs: `registry.tsv` (columns `hand_route`, `hand_estimate`), the "Hand-proof triage"
of `registry-notes.md` (25 ANALYTIC, 63 NUMERIC-ONLY), the paper and the supplement, read at the lines cited.
Abbreviations: `P:` is `research/warp-drive/paper/RESPONSE-HL-5D.md`; `S/` is `research/warp-drive/docket68/n1star/`.
Programs are named by the triage's C/S numbers. A "line" of printed length is a 121-character line of the edition.

## 0. Verdict

| class | items | what the edition must do |
| --- | ---: | --- |
| (a) mathematical claim | 25 | prove it in writing (projects A-G), or drop the claim |
| (b) numerical experiment | 57 | no proof; report as an experiment in prose, or drop |
| (c) statement about a computational route | 6 | delete (no object without code) |

- Seven (a) items carry a theorem or a proof step: C87 (Theorem 4), C222 (Theorem 1's Lemma 1.1 (e) and Lemma 2.3),
  C173, C174 and C175 (FAMILIES5's Theorem L″ and Corollary Q), C203 (EQUALITY5-LAYER's Theorem L_1E‴ and Proposition
  L.26 for the record's envelope), C156 (SETTLE-GLAM5 Theorem R5.1, settling of g_λ's own data). The other 18 are
  stand-alone results (certified constants, residuals, bounds) that no theorem uses; `P:1603` says so for the
  constants of the linear theory, and `P:1743-1749` for existence at 10 l5.
- Theorem 4's only dependency, ε_ind (C87), has a hand proof with the paper's own constant δ_50 (section 3).
- Two (a) projects concern objects that exist only in data files or in a program's output: the approximants at 10 l5
  (project D: 3,074 and 2 × 62,000 floating coefficients) and the computed background's spline (project E). Their
  written proofs would have to print those numbers. Section 2 recommends dropping D and redesigning E.

## 1. Classification of the 88

Rule. (a): the text asserts a property of a mathematically defined object (an operator, a root, an explicit function,
a spacetime, an explicit approximant), as certified, proved or exact. (b): the content is the output of a numerical
approximation (solver runs, convergence in a grid, floating-point measurements of a norm, a root, a coefficient, model
illustrations), and no proof step uses it. (c): the content is about what a computational or estimation route can or
cannot deliver. For each (b) item the sentence is quoted and the surrounding text was read for a use in a proof.

### 1.1 Class (a): 25 items (details in section 2)

| item | program | project | stated at | depends on it |
| --- | --- | --- | --- | --- |
| C87 | eindcert5 | A | `P:1105-1111`, `P:1514-1517`; `S/N1STAR-PROOF.md:7259-7297` | Theorem 4 |
| C266 | gapsums5 | A | `S/LOSS-D.md:362-410` (LD9) | none |
| C210 | e2trapband5 | B | `P:1555-1561`; `S/E2-PILOT.md:696-744` | none |
| C256 | e2trapcert5 | B | `S/E2-PILOT.md:666-695` | C210 |
| C258 | e2certify5 | B | `S/E2-PILOT.md:297-365` | 963.4 (`P:1559`), C123 |
| C281 | e2h1_5 | B | `S/E2-PILOT.md:454-540` | 963.4, 1516 |
| C282 | e2lzero5 | B | `S/E2-PILOT.md:366-416` | 1516, 275.2 |
| C284 | e2asymcert5 | B | `S/E2-PILOT.md:561-571` | C256's tails |
| C285 | e2asymlzero5 | B | `S/E2-PILOT.md:572-587` | none |
| C286 | e2asympsi5 | B | `S/E2-PILOT.md:588-598` | none |
| C287 | e2bandtop5 | B | `S/E2-PILOT.md:733-744` | none |
| C123 | inverse6_5m | B | `P:1578-1582`; `S/INVERSE5-SIX.md:278-329` | none |
| C125 | envelope5 | C | `P:1604-1607`; `S/CONSTANTS5.md:449-457` | λ0 bounds, λ_L |
| C261 | stage0bd5 | C | `S/CONSTANTS5.md:473-` (R2.2 (c)) | none |
| C222 | eps1hyp5 | C | `S/N1STAR-PROOF.md:118-131`; `S/CONSTANTS5.md:459-471` | Thm 1 (step) |
| C259 | stage1rate5 | C | `S/CONSTANTS5.md:1291-1314` | none |
| C136 | cdata5 | D | `P:1689-1691`; `S/CERTIFY-10L5-RESULT.md:264-304` | none |
| C137 | rich5 | D | `P:1691-1695`; `S/CERTIFY-10L5-RESULT.md:2473-2534` | none |
| C138 | rcert5d | D | `P:1695-1697`; `S/CERTIFY-10L5-RESULT.md:1840-1890` | none |
| C262 | rcert5 | D | `P:2631`; `S/CERTIFY-10L5-RESULT.md:677-723` | none |
| C173 | intcert5 | E | `P:1813-1825`; `S/FAMILIES5-R8.md:93-228` | Thm L″, Cor Q |
| C174 | truebg5 | E | `P:1813-1825`; `S/FAMILIES5-R8.md:127-228` | Thm L″, Cor Q |
| C175 | racslice5 | E | `P:1818-1819`; `S/FAMILIES5-R8.md:229-242` | Thm L″ |
| C203 | hyp5 | F | `P:1845-1849`; `S/EQUALITY5-LAYER.md:3165-3192` | Thm L_1E‴ |
| C156 | r5op5 | G | `P:1776-1782`; `S/SETTLE-GLAM5.md:866-872, 1316-1323, 1600-1612` | Thm R5.1 |

Two re-routings against the registry: C156 and C175 are NUMERIC-ONLY in `registry.tsv`, but each supplies a number a
stated theorem uses (C156: the decay exponents behind SETTLE-GLAM5's energy inequality and weight window; C175 S3: the
bend's thickness 0.00116 in Theorem L″'s statement). Both have short exact replacements (projects E, G).

### 1.2 Class (b): 57 items

Each entry: the sentence (shortened with …), where, and the check that nothing proved uses it.

Libraries and the separate programme (no claim of their own):

- S1 emitter_process, S3 source_spec: modules of the author's separate programme, loaded by C48 and C25 (registry).
  Their importers are (b).
- S2 hf_mirror5 (solver for C24, C130), S5 bondisph5 ("(computed, `checks/bondisph5.py` …)",
  `S/CERTIFY-10L5-RESULT.md:154`), S6 cpsolve5 ("Computed (`checks/cpsolve5.py`, `checks/cplate5.py`)", same file
  `:491`), S9 g5zeros5 ("re-run with every zero recorded (`checks/g5zeros5.py` …)", `:197`), S11 szrun5 ("The runs
  are scratch runs of `dnsolve5.py` through `checks/szrun5.py`", `P:2619-2620`), C184 dnsolve5 ("The characteristic
  problem itself is computed (… computed, not certified)", `P:1678-1680`). Check for all: each produces runs read by
  other (b) programs; `P:1743-1745` claims existence at 10 l5 only where the solution is the seed.

Sections 6 and 8 (the solver and linear settling):

- C24 hf_core5: "the statement is about the round family, as the numerical solver's is: `hf_core5.py` evolves the
  metric …" (`P:661-664`). Check: Proposition 3.3 is "(deduced)" (`P:659`); the solver is compared, "It agrees".
- C25 hf_anchor5: "The one finer run … which the solver's anchor check records as grid-limited" (`P:697-699`).
  Check: `P:700-701`, "what Theorem 3 proves is that g_λ obeys it"; the comparison tests the solver, not the law.
- C28 settle5 (T3, T5, T6): "No growing mode appears … (settle5.py T5; a finite-time observation)" (`P:912`), the
  ringdown "reproduces to 1% (settle5.py T3 …)" (`P:917-920`), the tail t^(−7.05) (T6). Check: `P:921-922`, "the class
  is settled by Hintz's route instead (sections 8.3–8.4, Theorem 4)". T1 (DERIVE) is not part of this item.
- C48 seed_escape: "The linear scattering of the shell off the seed at 10 l5 is computed in … `seed_escape.py`"
  (`P:1677-1678`; also `P:919`, the barrier for T3). Check: no conclusion is drawn from it. Its E3 (the class's
  perturbation types, `S/N1STAR-PROOF.md:1767`) duplicates settle5 T1, which the paper cites (`P:797-798`).

Section 9, the linear theory's constants and the loss count:

- C116 e2meas5: "the bound lies 9.5 to 22 times above the computed norm at the sampled frequencies (computed, floating
  point, …`e2meas5.py`)" (`P:1561-1562`). Check: a comparison with the certified bound; `P:1603`.
- C277 e2band5: "`checks/e2band5.py` computes the band … Labels: computed, not certified." (`S/E2-PILOT.md:186-187`).
- C278 e2pilot5: "P2: numerical illustration, scipy solve_ivp at rtol 10⁻¹¹" (`S/E2-PILOT.md:866-867`). P1 (the
  radial equation) is DERIVE and not part of this item.
- C283 e2asym5: "(… `checks/e2asym5.py` A1-A5, computed in floating point, not certified)" (`S/E2-PILOT.md:541`);
  superseded by the certified C284 and C285 (`:561`, `:572`).
- C255 e2high5: "Computed, not certified; the scaling law is a fit over 3 ≤ σ ≤ 96, not a bound."
  (`S/E2-PILOT.md:832-833`).
- S8 e2trap5: "(`checks/e2trap5.py` T1-T5; computed, not certified)" (`S/E2-PILOT.md:613`); "the certificate checks
  this multiplier, not the program's float" (`:667-668`). Its output, the multipliers' parameters, is an object a
  written proof of 11.477 would have to print (project B).
- C265 gapscan5: "`checks/gapscan5.py` computes the gap near 2 of the scalar indicial roots over that region … about
  3.1 × 10⁻⁵ (G3)" (`S/LOSS-D.md:265-270`). Check: LD5 bounds how much another damping point could improve the
  counts; the paper's floor uses only ε_ind ≤ δ_50 (`P:1511-1517`).
- C268 s1coef5: "Computed (D442; `checks/s1coef5.py` S1-S5): the s1 system solved from the horizon …"
  (`S/LOSS-D.md:433`), A = 141.4269 at the record's point. Check: decides only whether d1 ∈ ℰ_ind, i.e. LD9's δ_G;
  neither Theorem 4 nor the paper's floor uses it.

Section 9, physical wavelengths and the wavelength 10 l5:

- C127 lam0data5 (harmonic solve) and C128 m22evol5: "solved harmonic by harmonic (floating point …)", "the stage
  gives that number as 2.207738 … (computed, floating point, …`m22evol5.py`)" (`P:1610-1616`). Check: `P:1620-1621`,
  "So the sharpening is computed, not certified; the certified bounds are the ones stated." The exact parts of C127
  (the data in closed form, `S/LAMBDA0-DATA5.md` Lemma 7.1, G1-G3) serve only the uncertified M_22.
- C130 growth5: "The solver's own scheme came first, with the growth factor measured on its computed solution at 10 l5"
  (`P:1633-1634`). C131 excise5: "the order holds for every such duration from 0.005 to 0.06 (…`excise5.py`)"
  (`P:1638-1642`). C132 g5angle5: "at its own step it is unstable in angle at N_x = 24 and 32 … (computed, …
  `g5angle5.py` A1–A2 …)" (`P:1646-1648`). Check for all three: `P:1642-1643`, "So no approximant on D_T comes from
  that scheme at 10 l5"; nothing is built on the scheme.
- C134 secondzero5: "the zero set computed at 100 l5² for v ≤ 1.75 r_h in `secondzero5.py`" (`P:1652-1653`).
  Check: the proved part is "(deduced, its identities computed in `sectexp5.py`)" (`P:1652`); `P:1669-1670`, "The
  event horizon is not located".
- C135 szconv5: "… consistent with the data truncation, halving as the radius doubles, at two radii (computed,
  …`szconv5.py`)" (`P:1661-1664`). Check: a grid study of a rebuilt zero.
- C182 g1curv5: "beyond v ≈ 3.25 the second seed's late region is not resolved in angle (computed, floating point:
  …`g1curv5.py --seed2-2400` …)" (`P:1684-1687`). Check: `P:1894-1895` lists it among "(measurements)".
- C296 axisdrift5, C297 g1geom5, C298 g1cells5, C299 g1uv5, C300 g1cut5, C301 g1axis5, C302 g1amp5, C303 g1map5:
  supplement only, `S/CERTIFY-10L5.md:255, 364-365, 401, 422, 444, 512, 536`, under the heading "## 6b. F2: the
  prototype and what it measured (computed, D344; non-rigorous)" (`:178`). Check: a feasibility study; no paper use.
- C212 resid5: "the computed residual of a smoothed run. Section 9 now cites the certified residuals of
  `checks/rich5.py` and `checks/rcert5d.py` instead" (`P:2630-2631`). Check: superseded.
- C288 late5: "## 3. The late region (computed, `checks/late5.py`)", "the computed fields are not an approximation of a
  vacuum solution in this gauge" (`S/CERTIFY-10L5-RESULT.md:369, 396-398`). Check: supplement only, superseded.
- C153 late5b, C151 cpaxis5, C152 cp3grid5, C154 mtrunc5: "converges at second order in the null step to v ≈ 1.8
  r_h …", "consistent with second-order convergence …", "the unimposed constraint falls 3.84-fold …" (`P:1724-1742`,
  under "Computed (floating point):", `P:1720`). Check: `P:1743-1745`, "So at 10 l5 existence is proved where the
  solution is the seed (v ≤ r_h/2) and is not claimed beyond it".
- C291 cplate5, C293 cplate5c, C294 cplate5d: "A constraint-preserving scheme … agrees with the free one below v = 1.8
  …: one solution", "So v ≥ 1.9 at areal radius 1.0–1.2 is still not decided (`checks/cplate5d.out`)"
  (`S/CERTIFY-10L5-RESULT.md:491-493, 988-997`). Check: supplement only; no use.
- C289 jordan5: "*Computed (`checks/jordan5.py`).* Measured in the scheme itself: k = 2 → 8 multiplies the response by
  20.4." (`S/CERTIFY-10L5-RESULT.md:461`). Check: the claim is the Jordan block, deduced exactly by symbol5 (`:455`).
- C144 wgron5: "Computed (floating point): on |x| ≤ 1/2 … F² = 10^138, and 10^66.9 with Theorem 8.W's weights"
  (`P:1720-1721`). Check: `P:1745-1749`; F² is a number of the computed solution, and existence is not claimed.
  W1's model check of Theorem 8.W is redundant with the deduced theorem.

Section 9, beyond the boundary and more families (supplement statements):

- C304 transfer5: "At the record's γ_C = 10⁶ (D434; `checks/transfer5.py` T1-T3, computed, not certified)"
  (`S/BEYOND5.md:345-346`). C305 strip5: "r · r²φ → about −0.785 … (−0.784 at r = 400 and still drifting;
  `checks/strip5.py`)" (`:466-468`). C307 stripderiv5: "a pre-asymptotic consistency check at s = 1 only"
  (`:528-534`). C308 stripradial5: R3, "gives r^(3+q)φ → K_(3+q,l) to 0.07 %" (`:577-590`; its R1-R2 are exact).
  Check for all four: BEYOND5 section 3 is "What remains"; the paper's "Beyond the boundary" rests on BEYOND5
  Propositions 6.1-6.2 and SETTLE-GLAM5 Theorem R5.1, not on section 3.
- C319 r5models5: "(computed in a model, r5models5 M2)", "(computed, r5models5 M3 and its control)"
  (`S/FAMILIES5-R6.md:92, 102`). C320 katonl5: "(e): Theorem K, Lemma E, Lemma A′: proved here (deduced; the iteration
  computed in a model, katonl5)" (`S/FAMILIES5-VLASOV.md:358`). Check: the lemmas are deduced; models illustrate.
- C321 ehband5: "The argument is written out … and labelled deduced. It is also computed on the computed background."
  (`S/FAMILIES5-R11.md:39-43`). Check: the deduction stands alone.
- C161 twobg5: "(deduced, the identities computed, `checks/twobg5.py` …)" (`P:1788-1790`), "computed example"
  (`S/FAMILIES5-FULL.md:62, 168`). C180 twodomainx5: "is computed for one choice of the outgoing family's
  characteristic data …; for the data the supplement states … the background on the whole domain is deduced"
  (`P:1901-1905`). Check: the statements are deduced. Note: twobg5 G1's identities (exact) are a DERIVE step of
  project E's reduction (`S/FAMILIES5-R8.md:133`), to be written there.
- C172 racglobal5: "R between 4.29 and 4.53 (computed, …`racglobal5.py`; its extent certified by interval arithmetic
  … `intcert5.py`, `truebg5.py`)" (`P:1813-1817`). Check: the certified version is C173-C174 (project E).

### 1.3 Class (c): 6 items

- C129 m22cert5: "The a posteriori estimate for that solve … amplifies … by a factor of at least 1.8 × 10¹⁴ …; this
  estimate cannot certify that number at the data's own truncation" (`P:1616-1620`). Replace by "M_22 is not
  certified", which `P:1620-1621` already says.
- C292 rcert5b: "a usable certified sup over the box is a matter of machine time … not of method"
  (`S/CERTIFY-10L5-RESULT.md:976-985`).
- C263 rcert5c: the approximant pinned by md5, and a control that a perturbed coefficient moves the enclosure
  (`S/CERTIFY-10L5-RESULT.md:1278, 1446-1456`).
- C149 blocks5 (H2) and C150 blockw5: "so the block (Schur) condition under which an estimate on the high angular modes
  would lower the constant fails at every angular resolution" (`P:1722-1724`). H1 (N-independence) is an exact
  identity and may stay as a remark if wanted.
- C290 ampresp5: "The demand is then δ + ∫ε < 3.0 × 10⁻⁵ … The record's computed residual, 2.5 × 10⁻³, is 84 and
  3.2 × 10³ times too large" (`S/CERTIFY-10L5-RESULT.md:468-472`).

## 2. Proof projects

Each project: the claims, the constants, the sources, a hand strategy, feasibility, and any object defined only by
code. Lengths are printed lines of 121 characters, with a factor of about 2 either way.

### Project A. The indicial roots' distance from the integers (C87, C266)

- Claim A1 (C87; `P:1105-1111`). For the linearised gauge-fixed operator at the record's point, (8.13) holds: every
  non-integer indicial root λ with |λ| ≤ 50 has dist(Re λ, Z) ≥ δ_50, at every harmonic degree l, with δ_50 =
  1.94137056846 × 10⁻⁸, attained at l = 50 by the root 1 − l − δ_50 of the gauge potential's factor; the constraint
  damping's roots with |λ| ≤ 50 stay at least 2.9 × 10⁻⁶ from Z (2.93235 × 10⁻⁶ at l = 2, `S/checks/eindcert5.out`).
- Claim A2 (C266; `S/LOSS-D.md:398-410`). From the computed roots, the least value above 2 or 3 of the sums that the
  gap condition (G) reads is 3 + 5.02 × 10⁻⁸ (λ_♯ + 4,470,304 d1), so (G) does not bind below ε_ind.
- Depends on A1: Theorem 4 (`P:1239-1241`, ε_K < ε_+ < min(δ♯, ε_ind, ℓ_I − 3, 1/4)); the write-out's parameter row
  w1 (`S/proof5/PART-VI4-PARAMS.md:38`); the floor d > 7.95 × 10¹⁵ through the upper bound 1.94138 × 10⁻⁸
  (`P:1511-1517`). Nothing depends on A2.
- Sources: `S/N1STAR-PROOF.md:7259-7297` (10.52, Proposition 10.43), `:4600-4640` (10.24 (a)), `:3414-3520`
  (10.12, Proposition 10.9); `S/eind5.py` and `S/checks/eindcert5.py` docstrings; `S/CONSTANTS5.md:158`.
- Strategy, feasibility and length: section 3. A1 can be proved by hand with the paper's constant δ_50 exactly;
  about 490 lines, of which about 100 are a crossing table of 92 rows. A2: closed forms of d0, d1, δ_2, δ′_1 from section 3's
  formulas and one ceiling computation; about 40 lines, but A2 needs d1 to 15 digits and nothing uses it: drop.
- Objects defined only by code: none. The sextic's coefficients come from damping5's det N (DERIVE, C50), which the
  edition writes out anyway; A1 needs it printed as seven polynomials in κ.

### Project B. Morawetz and resolvent bounds on five-dimensional Tangherlini (C210, C256, C258, C281, C282, C284-C287, C123)

Claims and constants (μ = 1, I = {1.2 ≤ r ≤ 4}, a = l(l + 2) + 3/4, b = 9/4, V_l = (1 − y)(ay + by²), y = 1/r²):

- B1 (C258, `S/E2-PILOT.md:297-365`). Lemma E2.9's hypothesis: with φ_* = tanh((r_* − r_*(√2))/s), s = 49/50,
  w_1 = −φ_*V_1′ − ½φ_*‴ ≥ 0 on ℝ, tails included; m′ ≥ 0.005793, M′ ≤ 1.02041, min_I w_6 ≥ 1.0610; the B_l table
  (l = 1: 129.7, 160.4, 264.5, 708.9 at σ = 0+, 1, 3, 10; every l ≥ 6: 18.07, 18.27, 19.22, 26.80).
- B2 (C282, `:366-416`). l = 0 by Lemma E2.8′ with q a sum of 43 sech² bumps: W_q ≥ 0 and φ′ − q ≥ 0 on ℝ;
  min_I W_q ≥ 0.02886, m′ ≥ 0.002580, M′ ≤ 0.3809; B_0(3) ≤ 275.2.
- B3 (C281, `:454-540`). Corollary E2.11's arithmetic: X_l, A_l, C_l (C ≤ 675.1 over l ≥ 1, 808.6 with l = 0, 986.4
  unweighted on 0 < |σ| ≤ 3).
- B4 (C284, C285, C286, `:561-598`). The asymmetric multiplier: B_1(3) ≤ 93.96, C_1 ≤ 184.82, C_l ≤ 64.18 (l ≥ 2);
  l = 0 with 37 bumps, B_0(3) ≤ 359.01, X_0(3) ≤ 158.57; ψ/ψ_* ≥ 0.712.
- B5 (C256, C210, C287, `:666-744`). ‖χ_I R_l(σ) χ_I‖ ≤ 10.989 at σ = 3, 5.8726, 3.7719, 2.3724, 1.5222, 0.99697 at
  σ = 6, …, 96, and ≤ 11.477 for every l ≥ 0 and 3 ≤ σ ≤ 384 (`P:1555-1561`), from one core-and-flank multiplier
  per l_1 = 5, …, 768 and 7,620 σ-intervals; per-interval values 0.56257, 0.49119, 0.47635 (0.43792) at σ = 256,
  320, 384 (C287). With B1-B3: X ≤ 963.4 (l ≥ 1) and C = X_0 ≤ 1516 on the band (`P:1559`; E2-PILOT `:745-758`).
- B6 (C123, `S/INVERSE5-SIX.md:278-329`). Eight certificates for the master potentials V_0, V_1, V_2, V_T, V_V, V_S
  (rows M1-M5: largest 95.35, 246.2, 574.6, 1739 at σ = 0+, 1, 3, 10, for V_2 at l = 1) and the transfers (15/16)B.
- Depends on B: nothing. `P:1603`: "This is a limit of the explicit computation, not a gap in Theorem 4."

Strategy. Lemmas E2.8, E2.8′, E2.9 and Corollary E2.11 are already proved in the text; only the positivity of the
weight and the constants are computed. Replace the tanh multipliers by multipliers algebraic in y = 1/r², for which
w is (1 − y) y^(3/2) times a polynomial in y, since d/dr_* = (1 − y)(−2y^(3/2)) d/dy. A planning check (sympy,
scratch, not part of the record; the writer must re-derive it) gives:

- φ = 1 − 2y (increasing, ±1 at the ends, zero at the photon sphere, where U′ also changes sign, so Lemma E2.9's
  monotonicity in a holds unchanged): w_1 = ½ (1 − y) y^(3/2) p(y), p(y) = 15 − 90y + 189y² − 106y³, and p has no
  root in [0, 1] (p(0) = 15, p(1) = 8, least value 2.0727 at y = 0.3293). So w_l ≥ w_1 ≥ 0 on ℝ for every l ≥ 1,
  tails included, by a three-line argument. On I: m′ = 0.05859 (at r = 4), M′ = 0.74361, min_I w_1 = 0.07388, so
  B_1 ≈ 23.7, 42.9, 93.8, 281.6 at σ = 0+, 1, 3, 10 against the record's 129.7, 160.4, 264.5, 708.9; for l ≥ 6 the
  least weight on I is w_1(√2) ≈ 0.354, B_l(3) ≈ 21 against 19.22.
- l = 0: φ = 1 − 2y with q = ½ y^(3/2)(1 − y)(1 + 3y/2) gives W_q = (3/8)(1 − y) y^(3/2)(149y⁴ − 280y³ + 177y² −
  42y + 4), the quartic positive on [0, 1] (least 0.678 at y = 0.2004), and q ≤ φ′/3. This replaces both bump sums.
- B3 follows by Corollary E2.11's closed formulas from the new constants.
- B6: the same multiplier for the six potentials (b ∈ {9/4, 5/4, −7/4, −27/4, −39/4}; V_S through the record's
  majorant). w is affine in (a, b), so each family needs its corners only; the planning check finds w/((1 − y)
  y^(3/2)) a cubic in y with no root in [0, 1] at (a, b) = (15/4, 9/4), (15/4, 5/4), (35/4, −7/4), (35/4, 9/4),
  (63/4, −39/4), (63/4, 9/4) and (99/4, −39/4), which covers M1-M4. The horizon needs a + b ≥ 4; three of the four
  single harmonics the record certifies one by one (V_2 at l = 1, V_V and V_S at l = 2) fail it and need their own
  algebraic multiplier or a Lagrangian term as at l = 0; V_S at l = 3 needs E(y, 1/m) cleared of (1 + 6εy)³.
- B5 is the hard part. A fixed multiplier gives B_l(σ) of order σ/w_I, so 11.477 on the band needs σ-dependent
  multipliers narrowing like l^(−1/2) at the trapped harmonic. By hand: an algebraic family φ_ν(y) = Φ(ν(1 − 2y)),
  Φ(x) = x/(1 + x²)^(1/2), with admissibility proved uniformly in ν ≥ ν_0 by an expansion in 1/ν with explicit
  remainder and finitely many ν below; Lemma E2.7 above the barrier; the σ-interval argument of E2-PILOT `:696-712`
  is already a proof.

Feasibility. B1-B4 and B6 with algebraic multipliers: feasible, exact constants, comparable to or better than the
record's (by the check above); about 60 (B1), 70 (B2), 60 (B3), 200 (B6) lines; B4 is then superseded (0-30 lines).
B5: a semiclassical estimate with explicit constants, 600-1,200 lines, constant likely 2-5 times weaker than 11.477;
the H¹ constants 963.4 and 1516 move with it. Recommendation: prove B1-B3 and B6, state the fixed-multiplier bound
B_l(σ) ≤ ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2) for every real σ ≠ 0, and drop 11.477, 963.4 and 1516 unless the
author wants the semiclassical project.

Objects defined only by code: B2's and B4's bump sums (43 and 37 bumps; c_k "rounded to four digits from a linear
program", `S/E2-PILOT.md:376-380`), which a literal written proof must print (43 and 37 lines of (c_k, x_k, κ_k)), and
B5's 764 core-and-flank multipliers chosen by S8's float search (s_R, s_c rational to four digits, κ; plus m′, M′,
w_I per l_1): about 770 printed rows, each also needing its own positivity proof. The algebraic route removes all
three.

### Project C. The λ0 constants (C125, C261, C222, C259)

- C1 (C125, `S/CONSTANTS5.md:449-457`, `S/LAMBDA0-DATA5.md:223-248`). env(v) = c β((2v − 4)/3), β(y) = cos¹²(πy/2)
  exp(−y²/(1 − y²)) on |y| < 1, c = ((105/128)/((3/2)∫β²))^(1/2) ∈ [1.3240711, 1.3241035]; e_k = sup|env^(k)| for
  k ≤ 14: 1.324, 3.077, 18.6, 95.75, 739.5, 5166, 4.611e4, 3.841e5, 3.780e6, 3.539e7, 3.733e8, 3.796e9, 4.214e10,
  4.552e11, 5.248e12. Depends: the certified bounds λ0 < 0.0024433 (operator), 0.0019079 (Frobenius), 0.0012228
  (entry) (`P:1605-1608`) go through C_app ≥ (4/3) c_lo a^(−3/2) = 12.593309 (`S/CONSTANTS5.md:2233, 2442`;
  `S/checks/lzerotrace5.py:434-440`), so through the lower end of c; λ_L < 3·10⁻¹² uses c ≤ 1.3241035
  (`S/EQUALITY5-LAYER.md:1555-1557`). The e_k feed C261 only.
- C2 (C261, `S/CONSTANTS5.md:473-`). Bounds to order 14 on every directional derivative of W_TT, χ dv dv and the
  stage-1 source S on Ω × S¹ at P*; S ≤ 3.32 × 10³ at order 0. Depends: nothing (a leaf of the λ0 value, which is
  not computed). Its exact Cartesian forms feed lzerotrace5 (ARITH, outside the 88).
- C3 (C222, `S/N1STAR-PROOF.md:118-131`). Lemma 1.1 (e) holds for every ε1 ≤ 3/5 with ε1 < μ0/a² − 1; at P* none
  above 0.6013096 serves; for ε1 ≥ s0 some Lorentzian g̃ within ε1 of g0 has |g̃⁻¹| unbounded, so Lemma 2.3 takes
  0 < ε1 < min(s0, μ0/a² − 1). Depends: Theorem 1's proof (this step), and the reading ε1 < s0 behind the λ0 bounds.
- C4 (C259, `S/CONSTANTS5.md:1291-1314`). Lemma 2.3 at g0 written out: κ ≤ 13.2197 on Ω at P* (at r = a), c_Y² = 2,
  T(Y, Y) between 0.196683 and 280.545 times |du|², Gronwall factor e^39.244 = 1.105 × 10¹⁷, the source coefficient
  < 3.525 × 10¹⁷. Depends: nothing in the paper (M22CERT5's route, class (c)).

Strategy. C1: admissibility is already proved (LAMBDA0-DATA5 Lemma 7.1). c needs an upper bound on ∫β² (for c_lo)
and a lower bound (for c_hi): β² is even and decreasing in |y|, and below 10⁻²² on 0.9 ≤ |y| < 1, so a
Gauss-Legendre or Simpson rule on [−0.9, 0.9] with an analytic error bound (Cauchy estimate on a strip, where
|cos¹²| ≤ cosh¹²(π Im/2)) gives c to 10⁻⁶ relative with about 20 printed node values. For e_k: Cauchy estimates
|β^(k)(y)| ≤ k! ρ^(−k) max over |ζ − y| = ρ, with ρ chosen per k and per distance to ±1, and the tail bound of
envelope5 E2 (exp(−1/(2t)) and its polynomials P_j). C2: Leibniz and Faà di Bruno on the explicit profiles, with
the e_k and Cauchy bounds for the rational factors in r on r ≥ a = 0.2699. C3: the least eigenvalues of g0 on ker dτ,
on ker dr at r = a and on ker d(v + τ) are 1, min(1, μ/a² − 1) and min(1, (3 + μ/r²)/5) in closed form; the direct
cone argument of eps1hyp5 H2; the sharp value at the corner r = b(τ0) is a 2 × 2 eigenvalue computation; s0 = (m*² +
1)^(1/2) − m*, m* = μ_end/a². C4: κ is the supremum over Ω of explicit algebraic functions of (r, μ, μ′/r), with μ ∈
[μ0, μ_end] and 0 ≤ μ′ ≤ (2/9)c²; monotone in r, attained at r = a, so a one-variable argument.

Feasibility. All four are feasible. C1: c the same to 6 digits if the quadrature is carried to about 20 nodes, so
0.0024433 stands (it has a relative slack of about 2 × 10⁻⁵); e_k likely 10-100 times weaker at k = 14, harmless as
nothing uses them; about 90 lines. C2: about 150 lines; constants weaker; recommend trimming to the orders λ0's
formula reads (i ≤ k + 5 = 11) or dropping. C3: about 50 lines, constants exact. C4: about 70 lines, same constants
to 4 digits; droppable. Objects defined only by code: none (c is defined by an integral, bounded in writing).

### Project D. Certified residuals at the wavelength 10 l5 (C136, C137, C138, C262)

- D1 (C136). On the data cone u = −10 an explicit approximant R_app satisfies sup|Ric_vv[g_app]| ≤ 4.97 × 10⁻⁵ (seed 1)
  and 2.28 × 10⁻⁵ (seed 2), 4.1-4.3 % of the terms that cancel; jumps of R_rr ≤ 3.6 × 10⁻⁸ and 8.5 × 10⁻⁸.
- D2 (C137). The Richardson approximant (`data/rcert5_C3R.npz`) has Einstein residual ≤ 3.73 × 10⁻⁵ of the curvature
  scale at 16,128 points and ≤ 5.0 × 10⁻⁴ as a supremum over a sub-box of each of four of the 416 boxes, where the
  single-grid approximant (`data/rcert5_C3.npz`) has 1.09-2.41 × 10⁻³.
- D3 (C138). The single-grid approximant's supremum over one interior box is ≤ 3.01 × 10⁻⁴ (32,768 sub-boxes).
- D4 (C262). The single-grid approximant's residual at 16,128 points (≤ 2.41 × 10⁻³) and its order-3 Taylor-model
  suprema over 416 boxes (6.8 × 10⁴ to 1.7 × 10⁸, or unbounded).
- Depends: nothing. `P:1743-1749`: the closing condition asks a residual of order 10⁻⁶⁸/G, "and its hypotheses are
  established on no region of its form beyond the seed".

Objects defined only by code. D1: a tensor Chebyshev series of degrees (40, 28) and (64, 28): 41 × 29 + 65 × 29 =
3,074 fitted floating coefficients, plus two affine corrections per seed (`S/checks/cdata5.py:187-203, 356`); about
520 printed lines. D2-D4: each approximant is five fields of 25 × 31 × 16 coefficients, 62,000 numbers, and there are
two (124,000 numbers, about 21,000 printed lines); D2-D3 also rest on two scratch runs not in the repository.

Strategy and feasibility. A hand proof would replace the box enclosures (12,288 and 18,432 boxes for D1, 16,128
points and 32,768 sub-boxes for D2-D3) by explicit derivative bounds on the printed polynomials; the residual is a
cancellation to 10⁻³ of the terms, so the bounds must be nearly sharp. Not feasible in a paper, and nothing would
use it. Recommendation: drop D2-D4, or keep them as a reported numerical experiment, class (b). For D1 there is a
written replacement that needs no approximant: on each generator the Raychaudhuri constraint is the linear ODE
R_rr = −(4/(3f²)) R s(r, x) with explicit s, so exact data exist; Sturm comparison with sup s ≤ 1.2 × 10⁻³ gives
R > 0 and |R − r| explicitly. About 60 lines.

### Project E. Margins of the angle-localised families and the background tube (C173, C174, C175)

- E1 (C173 C1, C1d, C2, C3; `S/FAMILIES5-R8.md:93-126`). For the computed background (its ψ_III a stated spline):
  Γ/E² ≥ 0.4475 (C1); with ψ_P, ψ_P′, ψ_P″ widened by d = (10⁻³, 10⁻³, 3 × 10⁻²) and μ0 by 10⁻⁴, still ≥ 0.048
  (C1d); hyperbolicity margin ≤ −3.01 × 10⁻⁴ on the bent slice (C2); for the background itself on R ≥ R_*, κ′K′^l_l
  ≤ −2.96 × 10⁻⁴ from R_* to 5.75, and on Σ_τ0 Nk < 0 outside the edge zones [4.2882, 4.2955] and [4.5258, 4.5310]
  and > 0 on [4.2955, 4.5258] (C3).
- E2 (C174 T1-T4; `:127-228`). The background itself: κK^l_l ≤ −4.76 × 10⁻³ on Σ_τ0 for R ∈ [0.683, R_*] (T3; 276
  rays, 8,834 packet step boxes); the n = 160 spline lies within 5.1 × 10⁻⁵, 2.6 × 10⁻⁴, 8.7 × 10⁻⁴ (k = 0, 1, 2) of
  the true ψ_III at the cell ends, inside C1d's tube, so Γ > 0 on the seed region (T2); μ3 ∈ [0.8220998, 0.8221253].
- E3 (C175 S3; `:229-242`). The bend φ″ = 0.01 (b(R; 4.1, 4.7) − l1 b(R; 3.5, 4.05) − l2 b(R; 4.85, 5.75)) has φ = φ′
  = 0 outside [3.5, 5.75], τ-thickness max|φ| = 0.00116 ("bent by at most 0.0012", `P:1818`), angular widening ≤
  3.3 × 10⁻⁴ rad; l1 = 0.6438152011922511…, l2 = 0.2732240437158471… in closed form.
- Depends: Theorem L″ (hyperbolicity on Σ′, `S/FAMILIES5-R8.md:229-242`) and Corollary Q (Γ > 0 on the seed region);
  `P:1813-1825` states both as certified.

Strategy. The reduction to ODEs is deduced (region I ingoing Vaidya; below R_* the rays obey dR/du = G(u, R) with data
from N′; region III vacuum), so E is a set of inequalities for explicit functions of solutions of small ODE systems
with explicit data. A hand proof needs (i) an explicit approximate solution of the data ODE on N′ (R″ = −B/(3R²),
u ∈ [5.7, 7.2]) and of the ray ODEs with their variational equations (J, K, L), with a posteriori error bounds by
Grönwall on intervals; (ii) the margins as one- and two-variable inequalities. E3 is elementary: φ is an iterated
integral of explicit bumps, and |φ| ≤ A(h_P K + …) by the moment identities; about 20 lines.

Feasibility. E3: feasible, the same constant or slightly weaker. E1-E2 at the record's parameters: hard. The margins
are small against the terms (−2.96 × 10⁻⁴; the tube is 10⁻³ in ψ), so the hand enclosures must be accurate to
10⁻⁴-10⁻⁵ over u ∈ [5.7, 7.2] and v̂ ∈ [0, 3.1]; written out, that is a printed piecewise-polynomial solution with
tens of pieces and their error bounds, 900-1,500 lines, and the constants would come out weaker, possibly losing
C2's and C3's signs near the bend. Recommended redesign (the theorems need some admissible example, not this one):
choose the bend amplitude larger than A = 0.01 (A = 0.001 fails, A = 0.01 gives 3 × 10⁻⁴), so that C2-C3's margin
grows, and re-centre C1d's tube on explicit enclosures of ψ_III rather than on the spline; then 200-300 lines.

Object defined only by code: the computed background's spline ψ_III ("a scipy spline; its piecewise-polynomial form
has float coefficients. The stated interpolant is that piecewise polynomial", `S/FAMILIES5-R8.md:98-99`), a cubic
spline on the n = 160 grid, about 640 floating coefficients (about 110 printed lines). Only C1, C1d and C2 use it;
T3 does not, and T2 uses it only as the tube's centre, so the redesign removes it.

### Project F. The hypotheses of the edge theorem for the record's envelope (C203)

- Claim (Proposition L.27, `S/EQUALITY5-LAYER.md:3165-3192`). On (v_s, v_s + 1/200], for the record's envelope:
  (H_N) for every N ≤ 14 with α = 1/2 and c_R = 3.35875, κ_k/κ ∈ [0.74998, 1.00745]; |κ′| ≥ c_t κ^(3/2) with c_t =
  2.13951; L.16 (c) with c_j ≤ 1.00321 (j ≤ 16); κ(v − v_s)² ∈ [0.7499, 0.81]; (b) every hypothesis holds on some
  (v_s, v_s + x0(N)] for every N; (c) (H_D) for every c > 0. The same for exp(−1/(v − v_s)) (c_R = 2.58122).
- Depends: Theorem L_1E‴ and Proposition L.26 for the record's envelope, "for every K ≥ 6" (`P:1845-1849`).
- Strategy. (b) and (c) are already hand proofs (analyticity at x = 0, Q_k(0) = A_1(0)^k by the recursion, A_1(0) =
  3/4). For (a): A_j(x) is in closed form, with g(z) = log(sin z/z) = −Σ ζ(2n) z^(2n)/(n π^(2n)); each quantity
  (Q_k, R_k = Q_(k+1)/Q_k, P_k = 2R_k − xR_k′, the c_t ratio) is its value at 0 plus x times a bound from majorant
  series on |x| ≤ 1/100 (A_j is analytic on |x| < 3), propagated through the recursion Q_(k+1) = Σ C(k, i) x^i
  A_(i+1) Q_(k−i).
- Feasibility. Feasible, about 180 lines. The printed constants come out weaker (e.g. c_R ≤ 4, κ_k/κ ∈ [0.7, 1.05]),
  which is enough: the theorem asks only κ_k/κ ∈ [1/2, 2] and some c_R, c_t, and the later thresholds (λ_25 below
  10⁻⁶⁶¹³ "whatever they are") are upper bounds that do not move. Objects defined only by code: none.

### Project G. The far-region exponents for the settling of g_λ's own data (C156)

- Claim (`P:1776-1782`; `S/SETTLE-GLAM5.md:866-872, 1316-1323, 1600-1612`). On the write-out's full gauge-fixed
  operator: the coefficients' decay exponents (O1), the residual's degree P(Σ) = O(λ r^(−13/2)) once p = 4 is in Σ
  (O2), and naturality P(σ*h) = Λᵀ P(h)(Λ·) Λ for G = O(2) × O(2) (O3). They fix the energy inequality's κ := C(μ +
  λ)(1 + |σ|)^(−2) + C ε (1 + |σ|)^(−1/2−a), ρ := C λ (1 + |σ|)^(a−9/2), the kernel (v_1 − t)^(a−9/2), integrable for
  a < 7/2, and with r6sigma5's exponents the weight window a ∈ (max(ℓ0 − 1, 5/2), 3).
- Depends: SETTLE-GLAM5 Proposition R3.6 and Theorem R5.1 (g_λ's own data settle with no gluing; `P:1757-1777`).
- Strategy. A homogeneity count, as the registry says: expand g_b0 + Σ at large r (Tangherlini's μ/r² terms, the
  waves' r^(−3/2), Σ's G_(2p) of degree −p), read off each coefficient's degree; the first omitted order of Σ gives
  O2's degree; O3 is the naturality of Ric and of the gauge term under isometries that fix the gauge data, a
  paragraph. Feasible, about 100 lines, exponents exact. Objects defined only by code: none.

## 3. Theorem 4 and ε_ind (C87), in detail

What Theorem 4 needs. The statement (`P:1239-1241`) and row w1 (`S/proof5/PART-VI4-PARAMS.md:38`) need only that
(8.13) hold for some ε_ind > 0: every non-integer indicial root with |λ| ≤ 50 has dist(Re λ, Z) ≥ ε_ind. The value
enters twice: the paper's sentence that ε_ind may be any number up to δ_50 (`P:1107, 1514`), which bounds the rate's
ε, and the floor on d, which needs only the upper bound δ_50 < 1.94138 × 10⁻⁸ (`P:1516-1517`).

The roots (`S/N1STAR-PROOF.md:7262-7268`). κ := l(l + 2), z := 4 e_Υ γ_Υ² = 4 × 10⁻⁶, and at the point (v, e_C,
h) = (1/2, 1/102400, 10⁻⁶). For l ≥ 2: scalar type −l, l + 2 (integers); box^Υ's 2 − l, l + 4 (integers) and the four
roots of Q(λ − 1), Q(λ′) = s² − (2 + 2κ + z)s + κ(κ + 1) + zκ, s = λ′(λ′ − 1); box^C's six scalar roots less 1.
Vector type: integers and box^C's two vector roots less 1. Tensor type: −l, l + 2. Shifts by integers do not change
dist(·, Z), so the question is about Q's roots and box^C's polynomials.

Answer to the question asked: yes. Given the closed form, the gauge potential's roots are bounded away from Z for
every l ≥ 2 by an explicit function of l, δ_l ≈ z l/(2(l + 1)(2l + 1)) ≈ z/(4l); this tends to 0, so no bound
uniform in l exists without the window |λ| ≤ 50, which cuts the roots off at l = 50 and makes the minimum δ_50. The
constraint damping's roots have no closed form, but an exact scaling identity reduces them to a cubic with closed-form
roots plus an O(h) correction, and a finite crossing table finishes them. Outline:

Step 1 (box^Υ, closed form; about 90 lines).
- Since 2 + 2κ = 2(l + 1)², Q's roots in s are s_∓ = (l + 1)² + z/2 ∓ R/2, R := (4(l + 1)² + 4z + z²)^(1/2).
- Exactly: s_− − l(l + 1) = 2lz/(2(l + 1) + z + R) =: d_l and s_+ − (l + 1)(l + 2) = 2(l + 2)z/(R + 2(l + 1) − z)
  =: d′_l (rationalise; (2(l + 1) + z)² − R² = 4lz and R² − (2(l + 1) − z)² = 4(l + 2)z).
- From λ′ = (1 ± (1 + 4s)^(1/2))/2, λ = λ′ + 1, the four roots are l + 2 + δ_l, 1 − l − δ_l, l + 3 + δ′_l, −l − δ′_l,
  with δ_l = 2d_l/((2l + 1) + ((2l + 1)² + 4d_l)^(1/2)) and δ′_l = 2d′_l/((2l + 3) + ((2l + 3)² + 4d′_l)^(1/2)).
- Two-sided bounds: z f(l)(1 − z) ≤ δ_l ≤ z f(l), f(l) := l/(2(l + 1)(2l + 1)), and the same for δ′_l with g(l) :=
  (l + 2)/(2(l + 1)(2l + 3)); so 0 < δ, δ′ < z/4 < 1/2 and the nearest integers are those displayed.
- The window: |λ| ≤ 50 keeps 1 − l − δ_l for l ≤ 50, −l − δ′_l for l ≤ 49, l + 2 + δ_l and l + 3 + δ′_l for l ≤ 47
  (at l = 51 the first is 50 + δ_51 > 50). f and g decrease for l ≥ 1 ((l + 1)(2l + 1) − l(4l + 3) = 1 − 2l² < 0), and
  f(50) = 50/10302 is below g(49) = 51/10100 by 4 %, far more than the O(z) = 4 × 10⁻⁶ relative error. So the
  minimum over the window is δ_50, at λ = −49 − δ_50.
- The number: δ_50 = 1.94137056846 × 10⁻⁸ from the closed form with R_50 and the square root expanded to second order
  with alternating remainders (planning check: the closed form gives 1.94137056846336 × 10⁻⁸, as eindcert5.out). The
  floor's upper bound is the line δ_50 ≤ z f(50) = 1.9413706 × 10⁻⁸ < 1.94138 × 10⁻⁸.
- l = 1 uses the same Q at κ = 3 (`S/LOSS-D.md:370-371`: λ_s1,2 = (1 + (17 + 2z − 2(z² + 4z + 16)^(1/2))^(1/2))/2),
  distance δ_1 = z/12 + O(z²); l = 0 has (1 ± (9 + 4z)^(1/2))/2 + 1, distance z/3 + O(z²). Both exceed δ_50.

Step 2 (box^C, vector type; about 20 lines). 10⁶ p_v(λ) = κ + 3 × 10⁶ − 999998λ − λ² has integer values at integers.
The lower root is near −10⁶. If the upper root λ_v is not an integer and m is its nearest integer, the mean value
theorem gives 1 ≤ |10⁶ p_v(m)| ≤ (999998 + 2 · 52.5)|m − λ_v| while |λ_v| ≤ 52.5, so dist(λ_v, Z) ≥ 1/1000103 >
9.9989 × 10⁻⁷ for every l. (Planning check: the true least value over l < 10⁴ is 5.0 × 10⁻⁶, at l = 2; the only
integer root is λ_v = 3 at l = 1.)

Step 3 (box^C, scalar sextic; about 270 lines with the table). The identity. With t := hκ and ε := e_C/h (=
9.765625 at the point), h³ det N(λ; κ) is a polynomial in h of degree 3,

    U(λ, t) + h R_1(λ, t) + h² R_2(λ, t) + h³ R_3(λ, t),
    U(λ, t) = (2 + t − λ)(2λ² − (3t + 10)λ + t² + (5 + 3ε)t + 12),

with R_1, R_2, R_3 of total degrees 4, 5, 6 (21, 19 and 10 terms), and in λ = μ/h the leading part is −μ³(μ + 1)²(μ
+ 2). (Planning check against damping5's det N, sympy, scratch.)
- Lower roots: near −1/h (twice) and −2/h by Rouché in μ; all below −10⁵, outside the window.
- Upper roots for 8 ≤ κ < κ* = 10⁸, i.e. 8 × 10⁻⁶ ≤ t < 100.02. B1 ≈ 2 + t (the continuation of the Coulomb root 2,
  exact at l = 0, 1). The quadratic's discriminant is t² − (24ε − 20)t + 4, positive for t < 0.01866 (l ≤ 135; the
  record's discriminant root l = 135.59) and t > 214.36 (l ≥ 14,640; the record's 14640.49): for l ≤ 135 two real
  roots between 2 and 3 (near 2 + (3ε − 1)t/2 and 3 − (3ε − 4)t/2 for small t), for 136 ≤ l < 10⁴ a complex pair
  with real part (3t + 10)/4 = 2.5 + 0.75t and imaginary part (214.375t − t² − 4)^(1/2)/4.
- Rouché on discs about U's roots with h|R_1 + hR_2 + h²R_3| < |U| on their boundaries; |∂_λ U| at B1 equals 3(ε −
  1)t, so the discs have radius O(h(1 + t²)/t) and the correction is h c(t) with c explicit. (Check: at l = 2, 10,
  135, 1000, 5000, 9999 the exact upper roots agree with U's to within 10⁻⁵-10⁻²; the planning comparison is in the
  scratch notes.)
- Near t = 0 U has the double root 2 (U(λ, 0) = −2(λ − 2)²(λ − 3)), so for small l the expansion parameter is h/t =
  1/κ ≤ 1/8: B1 and the quadratic's lower root are 13t apart (10⁻⁴ at l = 2) against corrections of 5 × 10⁻⁶; one
  disc holds both, then the roots are separated by the sign of P on a dividing circle. l = 2 gives B1 − 2 =
  2.93235 × 10⁻⁶, the record's least box^C distance; l ≤ about 20 are best written as explicit cases.
- Crossing table: B1 meets the integer n (3 ≤ n ≤ 51) at one κ_n ≈ (n − 2) × 10⁶ + c_n with c_n of order (n − 2)²
  (κ_3 = 1,000,013.4, κ_51 = 49,002,580.7), a root of the cubic κ ↦ P(n, κ) with integer coefficients; the pair's
  real part meets n (3 ≤ n ≤ 45; beyond, |λ − 1| > 50 for box^C's root) at one κ′_n ≈ (4n − 10) × 10⁶/3 + c′_n, a root of the Hurwitz
  determinant of P shifted to Re λ = n (a cubic in κ). Exactly one root each in [8, κ*] (Sturm counts in planning).
  The table prints, for each of the 49 + 43 crossings, a bracket of κ_n between two rationals with a sign change, the
  neighbouring values l(l + 2) and the gap. The least gap in planning is 14.4 (n = 3, l = 999) for B1 and 141 for
  the pair (n = 18, l = 4545).
- Distance: between consecutive crossings each root stays strictly between consecutive integers; near a crossing
  |root − n| ≥ |κ − κ_n| · inf |dλ/dκ|, with dλ/dκ = h(1 + O(ht)) for B1 and 0.75h(1 + O(ht)) for the real part of
  the pair, from the implicit function theorem on the disc. With gaps ≥ 14 this gives ≥ 1.0 × 10⁻⁵ at the
  crossings (planning values: ≥ 1.44 × 10⁻⁵), and ≥ 10⁻⁴ for the two real roots of the regime l ≤ 135.

Step 4 (l ≥ 10⁴; about 30 lines). eind5 E2's Sturm certificate in writing: substitute κ = κ* + u in the constant
coefficient and in the Hurwitz determinant of P shifted to Re λ = 51 (cubics in κ in planning) and show by
Descartes' rule, or a Sturm sequence of four printed polynomials, that neither has a root u ≥ 0; with three upper
roots right of 51 at κ* (Step 3 at t = 100) none crosses for u ≥ 0. The vector
root: λ_v > 51 for κ ≥ κ* from the quadratic formula. box^Υ: |λ| ≥ l − 1 > 50 for l ≥ 52 by Step 1.

Step 5 (l = 0, 1; about 40 lines). box^C's quartic at l = 0 and the sextic at κ = 3 (Coulomb root 2 exact, an integer,
and a quintic cofactor), with the vector quadratic at κ = 3 (integer root 3): Rouché brackets of the few roots in
the window; box^Υ as in Step 1.

Step 6 (assembly; about 20 lines). The least distance is min(δ_50, box^C's bound) = δ_50, since Steps 2-5 give at
least 9.9 × 10⁻⁷ for box^C (2.93 × 10⁻⁶ with the explicit l = 2 case). So (8.13) holds for every ε_ind ≤ δ_50, the
paper's statement, and δ_50 is attained.

Feasibility. All of it by hand with exact arithmetic; the constant δ_50 comes out exactly, since it is box^Υ's and
closed form, and box^C's bound has a margin of about 50 (vector) to 150 (scalar) over it, so crude derivative
bounds suffice. The labour is the crossing table: 92 rows, each a sign check of an integer cubic with 20-digit
coefficients at two rationals (or the expansion of κ_n about (n − 2) × 10⁶ to second order with an explicit
remainder, which needs κ_n only to ±1). Total about 490 lines (9-10 pages), of which about 100 are the table. It
depends on damping5's det N (C50, DERIVE), which the edition must print as seven polynomials in κ in any case.

## 4. Summary

| class / project | items | printed length, minimal | printed length, full |
| --- | ---: | ---: | ---: |
| (a) A indicial roots (C87; C266) | 2 | 490 (drop C266) | 530 |
| (a) B Morawetz and resolvent (algebraic multipliers; band) | 10 | 390 (drop 11.477) | 1,000-1,600 |
| (a) C λ0 constants | 4 | 140 (C125, C222) | 360 |
| (a) D residuals at 10 l5 | 4 | 0 (to (b) or drop; D1 by exact ODE: 60) | not feasible (≈ 21,000 + certificates) |
| (a) E angle-localised families | 3 | 220-320 (redesigned example) | 900-1,500 |
| (a) F edge-theorem hypotheses | 1 | 180 | 180 |
| (a) G far-region exponents | 1 | 100 | 100 |
| (a) total | 25 | about 1,500-1,600 | about 3,100-4,300 |
| (b) numerical experiments | 57 | 0 (drop) to 60 (one prose paragraph per section) | 150 (1-3 lines each) |
| (c) computational-route statements | 6 | 0 | 0 |

At about 55 lines a page, the minimal (a) programme is about 28 pages and the full one 55-80 pages. The registry's
DERIVE, ENUMERATE and ARITH estimate (about 17,955 lines) is separate and unchanged.

## 5. Decisions the author has to make

1. Project D: drop the certified residuals at 10 l5 (no theorem uses them; their objects are 3,074 and 124,000
   floating coefficients) or keep them as an experiment; replace D1 by exact data on the cone.
2. Project B: keep the band constant 11.477 (and 963.4, 1516) as a semiclassical project, or state the
   fixed-multiplier bounds that algebraic multipliers give in a few pages.
3. Project E: prove the margins at the record's example (long; the spline must be printed), or change the example
   (larger bend, tube centred on explicit enclosures) so that a written proof is short.
4. Class (b): report the 57 experiments in prose, labelled as numerical, or remove them; none is used by a proof.
5. Class (c): delete the six statements; where a sentence must remain, say only what is not certified.
6. C266 (gapsums5), C261 (stage0bd5), C259 (stage1rate5), B4 (asymmetric multipliers): stand-alone, droppable.
