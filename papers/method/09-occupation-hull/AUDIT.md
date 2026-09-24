# AUDIT — 09-occupation-hull, "The Occupation Law as a Lower Convex Hull"

Audited 24 September 2026 against `PAPER.md` (412 lines, dated 24 September 2026), `check.py`
(1,158 lines, last changed 03:24), `SOURCES.md`, `FIGURES.tsv`, the three figures, and the render
at `papers/method/out/09-occupation-hull.pdf` (18 pages) / `.html`. Nothing in `PAPER.md` or
`check.py` was edited.

**What was run.**

| run | result |
|---|---|
| `python3 check.py` (method/bin 3.12 first on PATH) | 113 of 113, ALL CHECKS PASS, exit 0, 80 s (log `scratchpad/09-audit-check.log`); identical line for line to the drafter's `checks/09c.log` |
| `python3 check.py --selftest` | 116 of 116 (89 EXHAUSTIVE, 17 GUARD, 7 MACHINE-CHECKED, 3 NEGATIVE), exit 0, 69 s |
| `python3 papers/method/lint.py papers/method/09-occupation-hull` | 0 hits |
| `tools/slopeaxis.py --selftest` | SELFTEST OK, 21 fixtures, corridor/hull mismatches 0 in both forms |
| `method/proofs/walkresets.py`, `candidateset.py`, `fdomain.py` `--selftest` | all SELFTEST OK |
| figures | md5 of each PNG equals its `FIGURES.tsv` row |
| render | 18 pages rasterised (PyMuPDF, 80 dpi) and read; text layer scanned for `_`, `^`, `\`, `**`: none |

A note on the run itself: the scratchpad is shared with sibling audits, and a sibling's `05-tower`
run truncated the file my first run was writing to. The run was repeated under a unique log name;
both runs (mine and the drafter's 03:40 run) print the same 113 lines.

---

## Part A — content audit

### A.1 Sources opened

Main volume `The_Method_1_6-2.md` §34.1 (9500–9530), §34.4–§34.6 (9576–9650), §34.7–§34.9
(9652–9686); Mathematical Compendium 656–658, 3558–3600, 3631–3650; The Register entries 1328, 1401,
1402, 1403, 1404, 1414, 1437, 1445, 1460, 1463, 1580 (in `The_Method_1_6___The_Register-2.md` —
`SOURCES.md` §2 gives their line numbers as if in the main volume, where those lines are unrelated
text; a bookkeeping slip in the provenance map, not in the paper); Register lines 4643, 4683 and
Index of Indices 1456 (the references); `RULINGS-R4e.md` §1, §3, §4; `SETTLED-R4.tsv` rows D-21a–j
and T-01; `tools/slopeaxis.py` (docstring, `Store`, `hull`, `corridor`); `docs/SLOPE-AXIS.md`;
`method/proofs/walkresets.py`, `candidateset.py`, `fdomain.py` in full; `method/members/LW1-ground.py`
header and Z = 91–108; `r2-ch16y.py` `radicand()` and `corridor()`.

### A.2 Definitions, lemmas, theorems — source, strength, proof

| object (line) | source | paper vs source | proof |
|---|---|---|---|
| D1 node count, capacity (51–55) | §34.4 "the node theorem supplies n − ℓ − 1 and antisymmetry the capacity 2(2ℓ+1)" | same | node theorem marked CITED with **no reference** (A-6) |
| D2, D3 data, step, entrant (57–59) | LW1-ground.py header (NIST ASD 5.12, GSIE, retrieved 2026-08-09) | same; "twelve steps gain two" is true (Cr Cu Nb Ru Pd Pr Tb Pt Pa Pu Bk Rf, recomputed) but printed by no check line (A-4) | — |
| D4 admissible set, frame, two forms (61–69) | §34.1/§34.4 formula; RULINGS-R4e §1 (g admitted); `Store.LMAX_RULED = 4` | same convention as the ruling; frame n ≤ 15 is the paper's (justified by Theorem 3) | distinctness EXHAUSTIVE where a one-line proof exists (A-18) |
| D5 the law (71–75) | §34.4 | same (open corridor: strict least ν, as `lo < hi` in the instrument) | — |
| D6 corridor (77–81) | Compendium 3560–3570 | same; cites Lemma 1 forward (A-20) | — |
| D7 lower hull, vertices, edge slopes (83–91) | Compendium 3640–3648; slopeaxis docstring | same; cites Theorem 2(a) forward (A-20); Δn(√r₁+√r₂)/(r₂−r₁) is the rationalised slope, sign read entrant-minus-rival as SOURCES §3.4 says | — |
| D8 walk (93) | walk.py's rule quoted in walkresets.py; Register 1328 | same rule; ε = 10⁻⁶, move/touch threshold 10⁻³ (walkresets uses 10⁻⁴; no |Δa| lies between 2·10⁻⁶ and 0.07, so the partition is the same) | — |
| D9 running intersection, piercing (95) | Registers 1401, 1463, 1580 | same; notation K₃ (A-11) | — |
| D10 opening, Madelung pick (97) | Register 1437 ("conditionally, given the observed configuration at Z−1") | same; "completion" used later but never defined (A-9) | — |
| Lemma 1 (103–113) | Compendium 3560 "one inequality per rival" | same, made precise (three cases, empty max/min) | complete |
| Theorem 1 (115–133) | Compendium 3640 "only vertices of the lower convex hull are ever taken" (prose) | stronger: the source states (i)⇒(ii) in prose; the paper proves the three-way equivalence | complete; (i)⇒(ii) affine argument correct; (ii)⇒(iii) correct; (iii)⇒(i) convex-combination identity verified by hand (it is (y(w)−y(u)) = (y(s)−y(u)) + (y(w)−y(s)) over x(w)−x(u)) |
| Corollary 1 (135–139) | Compendium "a point set carrying two distinct node counts has at least two such vertices" | same | complete |
| Theorem 2 (145–165) | slopeaxis docstring "the interval between the two hull-edge slopes flanking its observed entrant"; Compendium 3631 "constrains only membership of the interval" | stronger: the source asserts the identity and tests it; the paper proves it in general with the partition (c) | complete; one typo x(i) for x(pᵢ) (A-10); the step "taking a slightly greater than L" is right (a > m₀ and x(r) − x(v) > 0) but could show the chain (R-4) |
| Theorem 3 (177–185) | none — new (SOURCES §2 says so); prompted by r2-ch16y's "sweep (NMAX, LMAX)" | new | derivative of φ = (n+5)/(2(n−1)√(n−1)) and of ψ = (n+7)/(2n√n) verified by hand; φ(38) = 31/√37 > √6+√7 and ψ(56) = 49/√56 > (10√11+5√26)/9 exact in the log; the left-point bound N/d ≤ N/x(e) for N < 0, 0 < d ≤ x(e) is right; the "no floor" case is correctly routed through Theorem 4. Gap: the corridor over an *infinite* set is not defined (A-19); the abstract's paraphrase is false (A-1) |
| Table 1 (187–224) | §34.5; `check.py --table` | every one of the 106 rows verified against the check's own per-Z table (0 mismatches) and 30 of the row groups re-derived by hand from Lemma 1 | — |
| Table 2 (228–252) | §34.5 "nineteen distinct surds" | the source does not list its nineteen; the paper's nineteen counted by hand: floors sum to 80, ceilings to 106, 19 distinct values, least gap 1+√2 → (√5+√7)/2 = 0.0267 | — |
| Proposition 1 (254–260) | §34.5 and Compendium 3572–3580 | same closed form; the source's decimals at n = 6, 7 are wrong by 8.5·10⁻⁵ and 2.0·10⁻⁵ and the paper prints the exact values (SOURCES §4, correct) | complete (over-ceremonial, R-5) |
| Theorem 4 (268–272) | Register 1414; RULINGS-R4e §1; SETTLED D-21i | **same as the settled position, verbatim in content**: "no floor exactly when the entering subshell is node-free — 2p, 3d, 4f across the walk"; the paper adds the finished-form clause (Z = 5, 21, 58) and the proof through 5g | complete; rests on "5g admissible at every step", which the check pins (line 450) |
| Corollary 2 (274) | RULINGS-R4e §1 table; SETTLED D-21c, D-21d, D-21h, D-21j | **exactly the settled table**: Ce 4f p = 0, L = −∞, t undefined; Pa 5f p = 1, L = 0 (from 5g), U = (1+√3)/2, t = 1 (1 − ε/U) | — |
| l.276 (ℓ ≤ 3 alternative) | SETTLED D-21g; candidateset.py | the eleven 5f steps are right and pinned; but the alternative also changes the Rf–Hs floors, which the paper omits (A-2) | — |
| D-21i's "73 of 106 two-sided" | Register 1580 / walk.py's truncated set | the paper prints 80 with the frame-free reason (Theorem 3) and SOURCES §4 records the 73/7/26 as a truncated-frame figure; the theorem itself is stated as settled. Not a variant. | — |
| Table 3, Proposition 2 (284–323) | Registers 1328, 1403, 1404; SETTLED D-21a, D-21b, D-21f; walkresets.py | same measurement as walkresets (18 = 1 + 9 + 8; moves K Rb Cs Ce Hg Tl Fr Pa Lr; touches Mo Tc Rh Gd Tb Cm Bk Rf; 5d and 6d not constant); the paper follows the measurement where the Register has La for Ce and seven-at-L for seven-at-L-two-at-U (SOURCES §4, fair). Wording slips at (d) and (e) (A-8, A-9); "value" column is the endpoint (A-7) | — |
| Proposition 3 (333–335) | Registers 1401, 1463 | same fourteen (node-only) and same eleven (finished) | exact in the check |
| Theorem 5 (337–341) | §34.6; Register 1580 | same; the paper certifies both bounds by exhibited sets rather than by Gallai's theorem | complete; the three rationals checked by hand against all 106 rows |
| Proposition 4 (343) | slopeaxis fixtures 86 / 90; SLOPE-AXIS.md "at a = 0.5780 / 1.0010" | the paper prints the exact band containing those probes | — |
| §8 (353–359) | Registers 1437, 1445, 1460; §34.6's parabola | 96/106 and its ten misses reproduce Register 1437; 88/105 is the paper's own scorer (the source's 90 is a different scorer and is not claimed, SOURCES §4, fair) | n + ℓ = 2n − p − 1 checked |

### A.3 Every printed number against the check's output

Matched to a printed `[ok]` line: 108 of 108 electron counts; 106 steps; 106/106 non-empty (both
forms); vertex counts min 11 / max 15 and 7 / 15; {3: 6, 4: 56, 5: 28, 6: 14, 7: 2}; the frame list
of l.185 and the six finished-form differences at 38 43 48 56 80 88; F(7,4) differing at 87 88 103;
17 endpoints on n ≤ 7; the four extremes; φ(38), ψ(56), −31/√6, −49/√(13/2); F(37,36) and F(55,54);
19 and 138 endpoints, min gaps 0.0267 and 0.0002178; no ceiling absent; the four crossings; 26
no-floor steps; [5, 21, 58]; Pa p = 1, L = 0, U = (1+√3)/2 from 5g, 5g the only node-free
admissible; the eleven 5f steps; 18 = 1 + 9 + 8; ε-invariance over 10⁻⁴…10⁻¹⁰; touches 2ε; the
nine and the eight sites; not-at-opening [80]; 5d (57, 79, [58]) and 6d (89, None, [91, 103]); the
four shared endpoints; 8.9·10⁻¹⁶; the seven missing ceilings [3, 11, 19, 37, 47, 55, 87]; 15/14/0;
Pa placed at U; the fourteen and the eleven emptyings; the disjoint triple and quadruple; the three
and four stabs (7071067/10⁷, 17071067/10⁷, 3051137/1250000; 1380131/2000000, 17071067/10⁷,
19840593/10⁷, 3051137/1250000); 86 on (√3/3, √2/2), 90 on (1, (5√2+√5)/9); 88/105 and 91/105 with
their miss lists; 96/106 with its ten misses; the Madelung pick a vertex at all 106 in both forms;
6,868 sets / 31,040 point-instances; 300 / 1,041 / seed 11 / 300 disagreements; the seven Z3 lines
(k = 2…5 forward, k = 2…4 converse in [0,10]²); 24 digits and 4.43·10⁻⁸; 113 = 89 + 17 + 7; 116 with
the three negative controls; 18 mismatching steps for the collinear-keeping hull.

**Printed by a line whose pass condition is the literal `True`** (the line prints the value but
cannot fail; see A-4): 19 and 138 endpoints (check.py 598), the 11–15 / 7–15 vertex ranges (483
asserts only ≥ 2), {3: 6, …} (508), 15/14/0 (760), the finished-form emptyings list (815), 86 and 90
and their bands (860), 88 and 91 and the miss lists (882), 96 and the ten misses (892). The
node-only emptyings list is separately asserted (862); the finished-form list is not.

**Printed by no line at all** (A-4): "twelve steps" (l.59); "80 two-sided" (l.226, l.228 — derivable
as 106 − 26 − 0 from two printed lines); Table 3's endpoint column, in particular that cerium is
placed at U (only Pa's placement is asserted, line 764); the fourteen finished-form sites and which
are at L or U (l.323; held in `NUM["real_sites_q"]`, never printed); "at least eleven" (l.357).

### A.4 The Z3 obligations and the guards (check.py 960–1070)

- `strict_min` encodes "s is the unique minimiser at a": y₀ − a·x₀ < yᵢ − a·xᵢ for all i ≥ 1. Correct.
- `in_E` encodes s = Σ λᵢ pᵢ + (0, t), λ ≥ 0, Σ λ = 1, t ≥ 0. This is D7's E(P − {s}). Correct.
- `pairwise` encodes (iii): same-abscissa points strictly above, and for x_u < x₀ < x_w the sign
  (x_w − x_u)(y₀ − y_u) − (y_w − y_u)(x₀ − x_u) < 0, which is slope(u, s) < slope(u, w), i.e. s
  strictly below the line. Correct.
- Forward: `strict_min ∧ in_E` unsat for k = 2, 3, 4, 5, unconstrained reals — this is (i)⇒(ii) over
  all of ℝ², as the paper says (l.133). Converse: box [0,10]², distinct, `pairwise`, and
  ∀a some other point ties or beats s — unsat for k = 2, 3, 4 — this is (iii)⇒(i) in the named box.
  The paper names both boxes and the k ranges correctly (l.133, l.370, l.396).
- Guards run before any obligation is reported (`z3_checks` orders them so): non-vacuity of both
  hypotheses at k = 4; fidelity on 300 seeded instances; a negative control on the reference; and a
  second fidelity guard for the strict-minimiser formula. **But the fidelity guard evaluates a Python
  transcription of the predicate (`enc = all(...)`), not the Z3 expression** returned by
  `pairwise()`/`strict_min()`. §9 l.381 says "the Z3 predicate … is evaluated". See A-5.
- The self-test's Z3 negative control (`strict_min ∧ ∃i yᵢ < y₀` is sat) is a real refutation.
- Nothing is marked MACHINE-CHECKED for a box the check does not cover.

### A.5 SOURCES.md §4 — the claims that do not reproduce

Each of the twelve entries is fairly represented and the measured value is in the check's output,
with two small exceptions folded into A-4: "80 two-sided" is derived rather than printed, and the
"two at U (Ce, Pa)" reading of Register 1403 is asserted only for Pa. The first agent's eight
failures (SOURCES §1) are convincingly attributed to the check's own chain implementation and two
wrong expected lists; the present chain (strict turns, exact signs) agrees with the pairwise test
on 106 × 2 steps, 6,868 grid sets and 300 random instances, and the collinear-keeping chain is
caught by the negative control (18 steps). The identity holds at every step in both forms.

### A.6 Figures against captions and text

- Figure 1 (fig1-hull-and-corridor.png): left panel shows the La point set in F(8,4) with hull
  vertices 4f, 5d, 6p, 7s, 8s and 5d highlighted, L = √2/2 and U = (2+√2)/2 labelled; right panel
  shows 4f | 5d | 6p across the slope axis with rules at 0.7071 and 1.7071. Matches the caption
  (l.171) and Table 1's La row. The "6p" label overprints its marker slightly; legible.
- Figure 2 (fig2-walk-and-resets.png): nine filled markers labelled K Rb Cs Ce Hg Tl Fr Pa Lr, eight
  open markers at 42 43 45, 64 65, 96 97, 104; bands open at the bottom for the no-floor rows; the
  line is flat except at the nine moves. Matches l.327 and Table 3.
- Figure 3 (fig3-corridors.png): 106 rows, 19 vertical rules, left-edge arrowheads on the 26
  no-floor rows, B / La / Lr in orange, the band (0.577, 0.707) shaded. Matches the data. Two
  defects: the in-image title says "the widest band one slope can cover" (A-17), and the caption's
  sentence about the three highlighted corridors is wrong (A-3).
- FIGURES.tsv: rows name file, content, generator and md5; md5s match. The table's "made_by" column
  says fig2 is `figures.py fig3()` and fig3 is `fig2()`; harmless, but the drafter may want the
  function names to follow the figure numbers.

### A.7 Lint and typography (rendered PDF)

Lint: clean. Subscripts and superscripts are Unicode throughout (r₁, r₂, σᵢ, vᵢ₋₁, 10⁻⁶, 2ᵈ-type
forms); no underscore, caret, backslash or asterisk reaches the page; every table fits its column
with no clipped cell; every figure appears with its caption. Defects found: the half-subscript
"Uₘax" (page 8, A-23); the alt text "Figure n" printed as a stray line between each image and its
caption (pages 7, 13, 14, A-24); Table 3's caption paragraph orphaned at the foot of page 11 with
its table on page 12 (A-25); the status word EXHAUSTIVE hyphenated "EX-HAUSTIVE" (page 15, A-26);
Table 1's header has two columns each headed "L" and "U" (page 9, A-27); figure lettering small at
print size (A-28).

### A.8 Findings

**A-1 (MAJOR)** l.11 (abstract). "the corridor of the entrant is the same whatever finite frame of
subshells is admitted, provided the frame reaches n = 15 (Theorem 3)" is false as written: F(15, 3)
reaches n = 15 and gives different corridors at sixteen steps (91–95, 97–102, 104–108; recomputed
with `ent_corridor(Z, "p", 15, 3)`). Theorem 3 compares F(15, 4) with the unbounded set. Since L is a
maximum and U a minimum over the admissible set (Lemma 1), both are monotone in the set, so any
frame containing F(12, 4) gives the F(15, 4) corridors. Resolve: "…the same whatever frame of
subshells is admitted, provided it contains every subshell with n ≤ 12 and ℓ ≤ 4 (Theorem 3)", and
add that one-sentence monotonicity remark after Theorem 3.

**A-2 (MAJOR)** l.276 and l.33. The stated consequence of dropping g ("the set of steps without a
floor grows by exactly the eleven 5f steps") is true but incomplete: at Rf–Hs (104–108) the floor
√3/3 supplied by 5g becomes 0 supplied by 6f (Table 1's row 104–108 changes u, L). So l.33's "the
measurable consequence of the alternative is stated" is not yet true. Resolve: add to l.276 "and
the floor of the five 6d steps 104–108 falls from √3/3 to 0, supplied by 6f in place of 5g; no
other corridor changes" and pin the sixteen-step difference list in check.py.

**A-3 (MAJOR)** l.347 (Figure 3 caption). "so no slope serves fewer than three of them at once" is
the wrong statement — a single slope lies in at most one of three pairwise-disjoint open intervals.
Resolve: "so no single slope lies in more than one of them, and at least three slopes are needed".

**A-4 (MAJOR)** check.py 483, 508, 598, 760, 815, 860, 882, 892 and PAPER l.379. Eleven lines
report a value with the pass condition `True`, so the paper's 19 and 138 endpoints, the 11–15 /
7–15 vertex ranges, the n ≤ 7 histogram, the finished-form 15/14/0, the finished-form emptyings
list, 86 and 90 with their bands, 88 and 91 with their miss lists, and 96 with its ten misses
would print `[ok]` at any value; and "one hundred and thirteen obligations run and none fails"
counts them. Five further printed facts are produced by no line: "twelve" (l.59), "80 two-sided"
(l.226/228), Table 3's endpoint column including Ce placed at U (l.295), the fourteen finished-form
sites and their L/U (l.323), "at least eleven" (l.357). Resolve: pin each to the paper's value as
line 862 does (`== 19`, `== 138`, `== (86, [("√3/3","√2/2")])`, `== 88`, …); print the eighteen
Table 3 rows and the finished-form sites under `--table`; add a line for the twelve two-electron
steps; then re-count the obligations in §9.

**A-5 (MAJOR)** check.py 996–1030; PAPER l.381. The encoding-fidelity guard evaluates a Python
re-statement of the pairwise condition and of the strict-minimiser condition on the 300 instances;
the Z3 expressions built by `pairwise()` and `strict_min()` are never instantiated on a concrete
point set. The guard therefore checks that condition (iii) agrees with the chain (which
`vertex_pairwise` already does 6,868 + 212 times), not that the *encoding* is faithful, and §9's
sentence "the Z3 predicate for 's ∉ E(P − {s})' is evaluated on 300 pseudorandom point sets"
describes something the code does not do. Resolve: substitute the instance's rationals into the
Z3 expressions (`z3.substitute` + `z3.simplify`, or `model.eval` on a solver that fixes the
variables) and compare that truth value with `hull_chain`; or reword §9 to say a concrete
transcription is compared.

**A-6 (MAJOR)** l.55. "(CITED: the node theorem for the radial equation)" has no entry in
References; the spec requires a CITED result to carry its source with full author list and year.
Resolve: add Courant, R. and Hilbert, D. (1953). *Methods of Mathematical Physics*, Vol. I.
Interscience, New York (ch. VI, Sturm's oscillation theorem) — or Messiah, A. (1961). *Quantum
Mechanics*, Vol. I. North-Holland — and cite it at l.55.

**A-7 (MINOR)** Table 3, l.286–305. The column headed "value" prints the endpoint (Li 0.0000000,
K 0.5773503) where the placed value is endpoint ± ε (0.0000010, 0.5773513 in the check's own
walk). Resolve: head the column "endpoint (7 dp)" or state in the caption that a = value + ε at an
L and value − ε at a U.

**A-8 (MINOR)** l.315 and l.29. "6s, which had opened at caesium and been left at gold": 6s falls
from 2 to 1 at platinum (Ir [Xe]4f¹⁴5d⁷6s² → Pt 5d⁹6s¹) and is unchanged at gold. Resolve: "6s,
which opened at caesium, was completed at barium, lost an electron at platinum and is refilled at
mercury".

**A-9 (MINOR)** l.317. "completion" is undefined. check.py takes the first step at capacity
(`spans`: 6s → (55, 56), 5s → (37, 38), 4d → (39, 46)), so a subshell re-entered after losing an
electron (5s at Ag, 6s at Hg) is outside every span; that is what makes (e) true at Hg. Resolve:
define "completion" in D10 and say that 5s and 6s are re-entered after completion.

**A-10 (MINOR)** l.157. "x(u) = Σ λᵢ x(i)" → "x(u) = Σ λᵢ x(pᵢ)".

**A-11 (MINOR)** l.95. "I := K₃" — D6's notation is K(Z); write K(3).

**A-12 (MINOR)** l.339. "lie, respectively, strictly inside every corridor of Table 1 that contains
one of them" is circular. Resolve: "each of the 106 corridors contains, strictly, at least one of
the three; 7071067/10⁷ lies below √2/2, 17071067/10⁷ below (2 + √2)/2, and 3051137/1250000 below
(√5 + √7)/2".

**A-13 (MINOR)** l.45 against l.381. "The one randomised step is a guard" but §9 describes two
300-instance randomised guards. Resolve: "The only randomised steps are the two fidelity guards of
§9, and no result rests on them".

**A-14 (MINOR)** l.377. "Ten frames" lists F(8, 4) twice (once per form) to reach ten. Resolve:
"nine frames, F(8, 4) in both forms: …", or list them per form as l.185 does.

**A-15 (MINOR)** check.py 547–560. The output labels read "Lemma 4" for what the paper calls
Theorem 3. Resolve: relabel.

**A-16 (MINOR)** l.11. "the hull theorem is discharged by an SMT solver for up to five points":
one direction to five points, the converse to four (l.133, l.396). Resolve: "…for up to five points
in one direction and four in the other".

**A-17 (MINOR)** figures.py 144 (Figure 3's in-image title). "the widest band one slope can cover"
— the shaded band is where coverage is maximal, not the widest band. Resolve: "the band on which
one slope covers the most corridors (86 of 106)"; regenerate and update the md5.

**A-18 (MINOR)** l.69. "No two admissible subshells share a point in either form at any step
(EXHAUSTIVE)" has a one-line proof: two subshells with the same n and the same integer part of r
have the same ℓ, and the fractional part is below 1. Resolve: give the proof and keep the check as
a guard.

**A-19 (MINOR)** l.177–183. Theorem 3 compares with "all admissible subshells whatever, with no
bound on n or ℓ" — an infinite set — while D6 and Lemma 1 define K(s) for finite P. Resolve: either
extend D6 by sup/inf (the proof's bounds are uniform in n, so both are attained inside F(37, 36) /
F(55, 54)), or state Theorem 3 for every finite frame containing F(15, 4), which is all the paper
uses and follows from monotonicity (see A-1).

**A-20 (MINOR)** l.81 and l.87. D6 invokes Lemma 1 and D7 invokes Theorem 2(a) before they are
stated. Resolve: state the two facts inside the definitions as remarks with their one-line proofs
(Theorem 2(a)'s proof is one sentence), or write "(proved below as Lemma 1 / Theorem 2(a))".

**A-21 (MINOR)** l.355. "its own recalibration sites less lithium, together with the touches" —
the recalibration sites already include the touches. Resolve: delete "together with the touches".

**A-22 (MINOR)** l.409. The NIST reference should carry the retrieval date (2026-08-09, from the
data file's own header): ASD is a live database and the version number does not fix the
ground-configuration table.

**A-23 (MINOR, typography)** l.179–181, page 8. "Uₘax" renders as a subscript m followed by
full-size "ax" — a half-subscript, which the spec forbids. Resolve: rephrase ("the largest ceiling
over the walk, Ū" / "U⁺", or "U(max)" in a display block); "Lₘᵢₙ" is fine.

**A-24 (MINOR, typography)** pages 7, 13, 14. The image alt text "Figure 1" / "Figure 2" /
"Figure 3" prints as a small stray line between each image and its bold caption. Resolve: empty
alt text, or alt equal to the caption, in `![…]` (or in render.py if it is the renderer's doing).

**A-25 (MINOR, typography)** l.284, page 11–12. Table 3's caption paragraph is the last item on
page 11 and the table starts page 12. Resolve: keep-with-next on table captions, or move the
caption below the table as the figure captions are.

**A-26 (MINOR, typography)** page 15 (§8). "EXHAUSTIVE" is hyphenated across a line break
("EX-HAUSTIVE"). Resolve: no-hyphenation / nowrap on bold status words in the stylesheet.

**A-27 (MINOR, typography)** l.189, page 9. Table 1 has two columns headed "L" and two headed
"U" (exact and decimal). Resolve: head the last two "L (7 dp)" and "U (7 dp)" as `--table` does.

**A-28 (MINOR, typography)** pages 7, 13. Figure 1's right-panel labels and Figure 2's element
labels are about 5 pt at print size. Resolve: raise the font size in figures.py.

---

## Part B — reader audits

### B.1 A mathematician (convex geometry, discrete optimisation)

I have not seen the books. Every object is defined before use, with two forward references (D6 →
Lemma 1, D7 → Theorem 2(a)) that are harmless but untidy. The proofs of Lemma 1, Theorem 1, Corollary
1 and Theorem 2 are complete: I checked each inequality, the convex-combination identity in
(iii)⇒(i), the affine argument in (i)⇒(ii), and the two-sided argument in Theorem 2(b), which is
the delicate one and is right. Theorem 5's certificate (a disjoint triple and an exhibited stab set,
both decided exactly) is the right way to state a piercing number and needs no Gallai. The exact
arithmetic on ℚ(√ℕ) with Besicovitch's theorem for zero and rational enclosure for sign is sound
and clearly described. What I would send back:

**R-1 (MAJOR)** l.101–167 (§2–§3, and the framing at l.17–25). Theorems 1 and 2 are classical.
Theorem 1 is the statement that the minimisers of a linear functional over a finite set are extreme
points of its convex hull (here of the upward-closed hull E(P)), and Theorem 2 is the one-parameter
normal fan of the lower hull: the slopes selecting vertex vᵢ form the cone between the normals of
its two edges, and consecutive cones share a boundary ray. A referee in *Discrete & Computational
Geometry* or *Order* would reject "Three consequences are proved" without a sentence saying so. The
paper may keep its self-contained proofs (they are short and its shape needs them) but must say
these are standard and cite them: Ziegler, G. M. (1995). *Lectures on Polytopes*, Graduate Texts in
Mathematics 152, Springer (normal fans, §7); Grünbaum, B. (2003). *Convex Polytopes*, 2nd ed.,
Springer; and for the lower-envelope form de Berg, M., Cheong, O., van Kreveld, M. and Overmars, M.
(2008). *Computational Geometry: Algorithms and Applications*, 3rd ed., Springer (§11.4, duality).
The contribution is then correctly located in §4–§7: frame-freeness, the floor theorem, the nineteen
surds, the walk and the piercing census.

**R-2 (MINOR)** l.177. Same as A-19: K is defined for finite P and Theorem 3 quantifies over an
infinite set; state it for finite frames containing F(15, 4) or define sup/inf.

**R-3 (MINOR)** l.81, l.87. Same as A-20.

**R-4 (MINOR)** l.155. In Theorem 2(b), "taking a slightly greater than L, y(r) − y(v) >
m₀·(x(r) − x(v))" is correct because a > m₀ and x(r) − x(v) > 0 give a·(x(r) − x(v)) >
m₀·(x(r) − x(v)); write that chain, since the limit a → L⁺ alone gives only ≥.

**R-5 (MINOR)** l.260. "(u + v)(u − v) = u² − v², an identity of degree two verified on a 3 × 3
rational grid" reads as parody inside a proof. Keep the grid check in the code; in the proof write
the algebra and say the check exists.

**R-6 (MINOR)** l.93 (D8). The rule presumes L + ε < U − ε at every step, i.e. every corridor is
wider than 2ε. It is (the narrowest, lawrencium's, has width (√5 + √7)/2 − (√3 + √5)/2 = 0.4568),
and the exactness paragraph at l.321 implies it; say it in D8, and say what the rule does when
L = −∞ (only a ≥ U can fail, so a := U − ε).

**R-7 (MINOR)** l.339. Same as A-12.

**R-8 (MINOR)** l.177 (title of Theorem 3) and l.11. "the corridor does not depend on the frame"
overstates the theorem, which needs ℓ ≤ 4 present (F(15, 3) differs at sixteen steps, A-1).
Resolve: "the corridor is frame-free beyond F(12, 4)".

**R-9 (MINOR)** l.69. Same as A-18: a one-line proof replaces an exhaustive check.

**R-10 (MINOR)** l.133. The grid family "{0, 1, 2, 3}² read as (√r, n) with r ∈ {0, 1, 4, 9}" is
just the integer grid; the reading adds nothing to the exhaustive check of Theorem 1 (whose
statement is about arbitrary points) and might suggest the family was chosen to look atomic. Say
"the integer grid {0, …, 3}²" and drop the reading, or explain what it buys.

### B.2 An atomic physicist (aufbau, Madelung's rule and its exceptions, orbital collapse)

The paper is honest in the right places: ν is not an energy, a has no unit, the form is not derived
from the Schrödinger equation, and the memoryless (n + ℓ, n) rule out-predicts the carried slope.
The definitions are physically clean — p = n − ℓ − 1 is the radial node count of any central-field
nℓ orbital, 2(2ℓ + 1) is the Pauli capacity, and the step-conditional admissibility is the same
reading of the aufbau that the 4s/3d literature uses. But the paper leans on "observed" where the
data are calculated, presents the law without saying whose it is or what motivates its form, and
quotes a Madelung score that a physicist will read as contradicting the known exception list.

**R-11 (MAJOR)** l.3, l.11, l.25, l.59, l.409. "observed ground-configuration steps" and "the
tabulated ground configurations of the 108 neutral atoms": NIST ASD's neutral ground configurations
for lawrencium and for rutherfordium to hassium are theoretical predictions, not spectroscopic
determinations. The paper's own data file carries a bare J ("0", "5/2", "4") with no term as the
ground level of Sg, Bh and Hs, which is what a calculated entry looks like; Lr's [Rn]5f¹⁴7s²7p is
from relativistic coupled-cluster work (Eliav, E., Kaldor, U. and Ishikawa, Y. (1995). *Physical
Review A* 52, 291–296) and the 2015 ionisation-potential measurement (Sato, T. K. et al. (2015).
*Nature* 520, 209–211) is consistent with it but does not establish the configuration. Resolve: in
D3 and the abstract write "as tabulated in the NIST Atomic Spectra Database, whose entries for
Z ≥ 103 rest on calculation rather than spectroscopy", and replace "observed" by "tabulated" in the
thesis sentence and l.25.

**R-12 (MAJOR)** l.11, l.31, l.337–341, l.347. The consequence of R-11 for a headline result: the
lawrencium corridor ((√3 + √5)/2, (√5 + √7)/2) exists because Lr's entrant is 7p. With the
alternative 6d¹ configuration — the aufbau expectation, and what the paper's own Madelung pick gives
at 103 (l.355) — the entrant corridor at Lr is (√3/3, (√3 + √5)/2), which meets lanthanum's; the
largest pairwise-disjoint family is then {B, La} and the piercing number is 2 (recomputed with
check.py's `corridor` and the same greedy sweep). "Three are necessary" is therefore a statement
conditional on a calculated configuration. Resolve: say so in §7 and in the abstract ("given the
tabulated 7p¹ at lawrencium; with 6d¹ the piercing number is 2"), and add the sensitivity as a
check line.

**R-13 (MAJOR)** l.11, l.19, l.71–75. The law appears with no origin and no motivation: whose form
is ν = n − a√r, why a square root, why r is a node count plus a fractional occupancy. The paper's
abstinence from valuing ν is correct, but a reader must be told whether this is the author's
proposal (in which case say "proposed here") or a published one, and must be told that the choice
of abscissa √r is what makes the endpoints surds and that the hull, its cells and the whole census
would change under x = r (the map is not affine, so it does not preserve hull vertices). Without
that paragraph the node-count/reduced-occupancy definitions read as fitted rather than motivated.
Resolve: one paragraph in §0 stating provenance, what supports the form here (106/106 consistency,
Theorems 3–4), and that the √ is a choice the paper tests but does not derive.

**R-14 (MAJOR)** l.33, l.355. "96 of 106 for the memoryless rule" and "missing at 42, 45, 46, 57,
64, 79, 89, 90, 96 and 103" will be read against the standard list of about twenty anomalous
ground configurations (Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, La, Ce, Gd, Pt, Au, Ac, Th, Pa, U, Np, Cm,
Lr). The paper's pick is step-conditional — the admissible set is taken from C(Z − 1), so at
chromium 4s is already full in vanadium and the pick is 3d — which absorbs Cr, Cu, Nb, Ru, Pt, Pa,
U, Np and Ag as non-misses. That is a legitimate score, but the paper must say it is the
conditional score and how it relates to the usual count, and cite the exception literature:
Scerri, E. R. (2007). *The Periodic Table: Its Story and Its Significance*. Oxford University Press;
Scerri, E. R. (2013). The trouble with the aufbau principle. *Education in Chemistry* 50, 24–26;
Schwarz, W. H. E. (2010). The full story of the electron configurations of the transition elements.
*Journal of Chemical Education* 87, 444–448; Melrose, M. P. and Scerri, E. R. (1996). Why the 4s
orbital is occupied before the 3d. *Journal of Chemical Education* 73, 498–503.

**R-15 (MINOR)** l.59 ("The walk is the sequence of the 106 steps Z = 3, …, 108"). No reason is
given for starting at lithium. With the paper's own machinery the 1s corridor at Z = 1 and Z = 2 is
(−∞, 1) in the node-only form, which contains the starting slope a = 0, so hydrogen and helium add
no recalibration; they would add two no-floor corridors (28 of 108), leave the piercing number at 3,
and make the best coverage 88 of 108. State the convention and that it is harmless to the walk.

**R-16 (MINOR)** l.29, l.317. The two "mid-filling" moves, at cerium (5d) and protactinium (6d),
sit exactly where 4f and 5f collapse into the core — the orbital-collapse sites of the atomic
literature. One sentence placing them, with Griffin, D. C., Andrew, K. L. and Cowan, R. D. (1969).
*Physical Review* 177, 62–71, and Connerade, J.-P. (1978). The non-Rydberg spectroscopy of atoms.
*Contemporary Physics* 19, 415–448, would tell a physicist what the walk is seeing.

**R-17 (MINOR)** l.27, l.274, l.276. The floor 0 at protactinium is supplied by 5g, an orbital that
at Z = 91 lies far above 5f in every calculation. The paper is right to call the candidate set a
convention; say plainly that this floor is a property of the convention and of no measured level,
so that "the floor is 0, supplied by 5g" is not read as a physical statement.

**R-18 (MINOR)** l.55. "the hydrogenic orbital nℓ": for a many-electron atom the relevant orbital
is the central-field nℓ orbital, whose radial node count is also n − ℓ − 1 (Sturm's theorem for any
central potential). Write "central-field" and cite the theorem (A-6).

**R-19 (MINOR)** l.409. Same as A-22: give the retrieval date, and say the table ends at Z = 108
because ASD's neutral ground configurations end there.

### B.3 A journal referee

The paper is clearly written, self-contained, and its verification record is unusually explicit.
The abstract and §0 promise what the body delivers with three exceptions (the frame claim, the
five-point claim, and "observed"). The literature it cites is correct in every bibliographic detail
I checked (Madelung 1936 3rd ed.; Klechkovskii, *Sov. Phys. JETP* 14, 334; Löwdin, *IJQC* 3 S3A,
331; Demkov and Ostrovsky, *Sov. Phys. JETP* 35, 66; Allen and Knight, *IJQC* 90, 80; Andrew, *IPL*
9, 216; Besicovitch, *JLMS* 15, 3; de Moura and Bjørner, LNCS 4963; Janet 1929; Kramida et al. 5.12).
What I would require:

**R-20 (MAJOR)** Novelty. As R-1: the paper must separate what is classical (Theorems 1–2, the
normal fan; Lemma 1 as one-variable linear feasibility) from what is new (Theorem 3, Theorem 4, the
nineteen surds and their closed forms, Proposition 2's move/touch partition, Theorem 5's
certificate, §8's placement of the law), and cite the classical part.

**R-21 (MAJOR)** Abstract against body: A-1 (frame), A-16 (five points), R-11 ("observed"). Each is
a sentence in the abstract that the body does not support as written.

**R-22 (MAJOR)** Verification record: A-4 (eleven unfalsifiable lines inside "113 of 113") and A-5
(the fidelity guard is not a test of the Z3 encoding, and §9 says it is). Until both are repaired
the record's "none fails" is weaker than it reads.

**R-23 (MAJOR)** Missing standard references, with full author lists: Karapetoff, V. (1930). A
chart of consecutive sets of electronic orbits within atoms of chemical elements. *Journal of the
Franklin Institute* 210, 609–624 (the n + ℓ ordering before Madelung, beside Janet); Wong, D. P.
(1979). Theoretical justification of Madelung's rule. *Journal of Chemical Education* 56, 714–717;
Ostrovsky, V. N. (2001). What and how physics contributes to understanding the periodic law.
*Foundations of Chemistry* 3, 145–181; Schwarz, W. H. E. and Rich, R. L. (2010). Theoretical basis
and correct explanation of the periodic system: review and update. *Journal of Chemical Education*
87, 435–443; Goudsmit, S. A. and Richards, P. I. (1964). The order of electron shells in ionized
atoms. *Proceedings of the National Academy of Sciences* 51, 664–671 (the step-conditional ordering
in ions, which the admissibility test resembles); Scerri 2007 and 2013, Melrose and Scerri 1996,
Schwarz 2010 (R-14); Courant and Hilbert 1953 (A-6); Ziegler 1995 and Grünbaum 2003 (R-1);
Helly, E. (1923). Über Mengen konvexer Körper mit gemeinschaftlichen Punkten. *Jahresbericht der
Deutschen Mathematiker-Vereinigung* 32, 175–176, and Hajnal, A. and Surányi, J. (1958). Über die
Auflösung von Graphen in vollständige Teilgraphen. *Annales Universitatis Scientiarum Budapestinensis,
Sectio Mathematica* 1, 113–121 (Gallai's interval theorem, for l.341); Griffin, Andrew and Cowan
1969 and Connerade 1978 (R-16); Eliav, Kaldor and Ishikawa 1995 and Sato et al. 2015 (R-11). The
Index of Indices in the source gives Allen and Knight as 2003; the paper's 2002 is the correct year
for *IJQC* volume 90.

**R-24 (MINOR)** l.341. "the general theorem that for intervals on a line the largest
pairwise-disjoint subfamily and the smallest piercing set have the same size" is Gallai's theorem
(interval graphs are perfect); name it and cite Hajnal and Surányi 1958 even though it is not used.

**R-25 (MINOR)** l.33 and l.276. "a convention that no observation below Z = 109 can test" — true
for the entrants (every entrant is a vertex under both conventions) and, as it happens, for the
walk (no recalibration changes); say the second, since a reader will ask, and state the Rf–Hs
floor change (A-2).

**R-26 (MINOR)** l.377. Same as A-14.

**R-27 (MINOR)** l.347. Same as A-3; a false sentence in a caption is what a referee quotes first.

**R-28 (MINOR)** l.1. The title's definite article ("The Occupation Law") presumes a law the
reader knows; given R-13, "An occupation law as a lower convex hull" or "The n − a√r occupation
rule as a lower convex hull" would match the abstract's own "An occupation law…".

**R-29 (MINOR)** l.402. The Allen and Knight annotation "the standing of the derivation problem
the law re-poses" — the paper nowhere says how the law re-poses it (that is in the books, which it
cannot cite). Either drop "re-poses" or add the one sentence in §8 that says what the law does to
Löwdin's question (it names the tabulated order exactly, where n + ℓ names it at 96 of 106).

---

## Part C — the record

| id | line(s) | severity | finding | disposition |
|---|---|---|---|---|
| A-1 | 11 | MAJOR | abstract's frame claim false for F(15, 3); needs "contains F(12, 4)" | |
| A-2 | 276, 33 | MAJOR | ℓ ≤ 3 consequence incomplete: Rf–Hs floors change √3/3 → 0 | |
| A-3 | 347 | MAJOR | Figure 3 caption: wrong statement about the disjoint triple | |
| A-4 | check.py 483, 508, 598, 760, 815, 860, 882, 892; PAPER 59, 226, 295, 323, 357, 379 | MAJOR | eleven report-only obligations; five printed facts produced by no line | |
| A-5 | check.py 996–1030; PAPER 381 | MAJOR | fidelity guard tests a transcription, not the Z3 encoding; §9 misdescribes | |
| A-6 | 55 | MAJOR | CITED node theorem has no reference | |
| A-7 | 286–305 | MINOR | Table 3 "value" is the endpoint, not a | |
| A-8 | 315, 29 | MINOR | 6s lost its electron at Pt, not Au | |
| A-9 | 317 | MINOR | "completion" undefined; spans end at first capacity | |
| A-10 | 157 | MINOR | typo x(i) | |
| A-11 | 95 | MINOR | K₃ notation | |
| A-12 | 339 | MINOR | circular sentence in Theorem 5's proof | |
| A-13 | 45 | MINOR | "one randomised step" vs two guards | |
| A-14 | 377 | MINOR | "Ten frames" counts F(8, 4) twice | |
| A-15 | check.py 547–560 | MINOR | output labelled "Lemma 4" for Theorem 3 | |
| A-16 | 11 | MINOR | "up to five points" — converse is four | |
| A-17 | figures.py 144 | MINOR | Figure 3 in-image title "widest band" | |
| A-18 | 69 | MINOR | distinctness has a one-line proof | |
| A-19 | 177–183 | MINOR | corridor over an infinite set undefined | |
| A-20 | 81, 87 | MINOR | forward references in D6, D7 | |
| A-21 | 355 | MINOR | "together with the touches" redundant | |
| A-22 | 409 | MINOR | NIST retrieval date | |
| A-23 | 179–181 (page 8) | MINOR | half-subscript "Uₘax" | |
| A-24 | pages 7, 13, 14 | MINOR | alt text printed as stray "Figure n" line | |
| A-25 | 284 (pages 11–12) | MINOR | Table 3 caption orphaned at page foot | |
| A-26 | page 15 | MINOR | "EX-HAUSTIVE" hyphenated | |
| A-27 | 189 (page 9) | MINOR | duplicate L / U headers in Table 1 | |
| A-28 | pages 7, 13 | MINOR | figure lettering small at print size | |
| R-1 | 101–167, 17–25 | MAJOR | Theorems 1–2 are classical; say so and cite | |
| R-2 | 177 | MINOR | = A-19 | |
| R-3 | 81, 87 | MINOR | = A-20 | |
| R-4 | 155 | MINOR | write the inequality chain in Theorem 2(b) | |
| R-5 | 260 | MINOR | grid check of (u+v)(u−v) reads as parody in the proof | |
| R-6 | 93 | MINOR | D8: say corridors are wider than 2ε and the L = −∞ case | |
| R-7 | 339 | MINOR | = A-12 | |
| R-8 | 177, 11 | MINOR | Theorem 3's title overstates (needs ℓ ≤ 4) | |
| R-9 | 69 | MINOR | = A-18 | |
| R-10 | 133 | MINOR | grid family: drop the "(√r, n)" reading or explain it | |
| R-11 | 3, 11, 25, 59, 409 | MAJOR | "observed": Lr, Rf–Hs configurations are calculated | |
| R-12 | 11, 31, 337–347 | MAJOR | "three are necessary" depends on Lr = 7p¹; with 6d¹ the piercing number is 2 | |
| R-13 | 11, 19, 71–75 | MAJOR | law's provenance and the √r choice unmotivated | |
| R-14 | 33, 355 | MAJOR | 96/106 is the step-conditional Madelung score; relate to the ~20 exceptions; cite | |
| R-15 | 59 | MINOR | walk from Z = 3: state the convention (1s corridors (−∞, 1) contain a = 0) | |
| R-16 | 29, 317 | MINOR | Ce and Pa moves are the orbital-collapse sites; cite | |
| R-17 | 27, 274, 276 | MINOR | Pa's floor 0 from 5g is conventional, say so | |
| R-18 | 55 | MINOR | "hydrogenic" → "central-field"; cite | |
| R-19 | 409 | MINOR | = A-22 plus why the table ends at 108 | |
| R-20 | §2–§3 | MAJOR | = R-1 (novelty statement) | |
| R-21 | 11 | MAJOR | = A-1, A-16, R-11 (abstract vs body) | |
| R-22 | 379–381 | MAJOR | = A-4, A-5 (verification record) | |
| R-23 | References | MAJOR | missing standard references (list in B.3) | |
| R-24 | 341 | MINOR | name Gallai's theorem | |
| R-25 | 33, 276 | MINOR | say the walk is also unchanged without g; state the Rf–Hs change | |
| R-26 | 377 | MINOR | = A-14 | |
| R-27 | 347 | MINOR | = A-3 | |
| R-28 | 1 | MINOR | title's definite article | |
| R-29 | 402 | MINOR | "re-poses" unsupported in the text | |

Tally: 57 rows. BLOCKING 0. MAJOR 15 rows, 12 distinct issues (R-20, R-21, R-22 restate A-1,
A-4, A-5, A-16, R-1, R-11). MINOR 42 rows, 35 distinct issues (R-2, R-3, R-7, R-9, R-19, R-26,
R-27 restate A-findings).
