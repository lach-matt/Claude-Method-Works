# AUDIT.md — 06-order-recovery, "Order Recovery and the Reorderability Law"

Audited 2026-09-24 against `PAPER.md` (652 lines, dated 24 September 2026), `check.py` (1,371 lines),
`SOURCES.md`, `FIGURES.tsv`, the five figures, and the render at `papers/method/out/06-order-recovery.pdf`
(25 pages; HTML and PDF both newer than `PAPER.md`). Written by the audit stage; `PAPER.md` and
`check.py` were not edited. Every claim below carries a line of `PAPER.md` and, where a number is at
issue, the line of the check's output or the independent computation that decides it.

**Runs.** `python3 check.py --selftest` was run twice to completion with `method/bin` first on PATH
(Python 3.12.3, Z3 5.1.0, NumPy 2.5.2 — the versions §8 prints): 202.7 s and 202.9 s, exit 0, **90
obligations: 52 EXHAUSTIVE, 29 MACHINE-CHECKED, 6 REFUTATION, 3 SAMPLED, all discharged; SELFTEST
PASS on the four negative controls.** Both guards ran first and passed (non-vacuity in 3×3, 2×2×3,
3×3×3; fidelity 150 instances / 1,387 pairs / 120 / 120, 0 disagreements; the negative control on the
guard detected 8 disagreements). `check.py` rewrites the tracked `results.json` on every run (17 lines
of timings differed); it was restored with `git checkout` so the tree carries the drafter's run.
`python3 papers/method/lint.py papers/method/06-order-recovery`: **0 hits.**

**Every number the paper prints was matched to a line of the check's output** (the map is in A.2
below). No printed number is without a check. The three source figures `SOURCES.md` says do not
reproduce are not printed, and the paper's replacements are the ones the check produces (A.4).

**One finding is BLOCKING and it is mathematical, not clerical**: the paper's headline law counts
bijunctivity on the *difference* relations `T(x,y)` and presents the result as a property of the
constraint system on the *orientation variables* `C(x,y)` that D9 defines. Majority-closure is not
invariant under the exclusive-or change of variables that takes `C` to `T`, and on `C` the first
non-bijunctive constraint appears at arity 3, i.e. at `d = 3`, with a six-cell witness in `{0,1}³`
(A-1). The rest of the paper — Theorems 1–6, 9, Lemmas 1–9, the Λ recovery, the census — is sound,
and the proofs are complete where they are claimed, with the exceptions listed.

---

## Part A — content audit

### A.1 What was read, and how

- `PAPER.md` in full, twice (once as text, once as the rendered pages).
- Every source passage `SOURCES.md` names, with `sed -n`: MAIN §30 8321–8614, §15.2–15.5 4279–4337,
  §7 1729–1810, §16.5 4460–4485, App. A.7–A.8 9995–10022, A.19 10122–10160, §16.8.6 4784–4794,
  §16.7.1 4610–4640, §16.1 4348–4360, §16.4.1 4426–4448, §16.8 4655–4730; MATH §IV.A 144–175,
  256–265 (certificate condition), 266–274 (Moore family), 376–384 (Freuder 1982), 418–440 (failure
  modes A and B), 890–900 (constraint index).
- All 1,371 lines of `check.py`, including every Z3 encoding (`order_vars`, `enc_closed_s`, `enc_P`,
  `enc_canonical`, the Theorem 3 encodings `interval`/`lo_le`/`hi_le`/`mono`, the Lemma 9 encodings
  `remclosed`/`jp`/`mp`, the Theorem 9 cardinality queries) and the harness predicates they call
  (`prover.observed`, `prover.closed`, `prover.subset_vars`) and the fixtures (`cypher._lambda`,
  `_periodic`, `_janet`).
- The five figure images with the Read tool, against captions and text, and the provenance rows of
  the two copied plates in `method/PROOF-FIGURES.tsv` (md5 of `fig2` = `figure-15.1.png`
  `09482efe…`, `fig3` = `fig26.png` `8983923b…`, both matching `FIGURES.tsv`).
- The 25 rendered pages, two per image, plus the brief's chrome screenshot of the HTML.
- Independent computations (Python, stdlib): the bijunctive census on `T` (reproduces 2, 8, 73,
  1,442) and on `C` (2, 5, 15, 52 — see A-1); Λ's 16 admissible ordering systems at each cap
  setting, listed, with the identical-fibre pairs and the vacuous tree edges that produce them
  (A-21); `E` of the Janet layout over the 19 subshells actually occupied through Z = 118 and over
  the 20 through 8s (A-9); the source plate's arity-3 count on its own apparent parametrisation
  (A.4).

### A.2 Every printed number, matched to the check

| paper (line) | number | check line (both runs identical) |
|---|---|---|
| §0.1, §2.1 (23, 172) | 70,598 = 502 + 247 + 247 + 4,083 + 65,519 | section B, five "E(X) = 0 <=> sublattice" lines |
| §2.1, §5.1, §7.1 (176, 371, 505) | 6,912 ambient points, agree at every one | A "totality: chi decided on all 6,912" (but see A-14) |
| §2.3 (214) | 3×3 2⁹×6, 4×4 2¹⁶×24, 2×2×3 2¹²×2, 3×3×3 2²⁷×6; 16 obligations | D, sixteen MACHINE-CHECKED lines |
| §2.3 (216) | witness in each of four boxes; "the full box" | D, four REFUTATION lines: 3×3, 4×4, 2×2×3 witnesses are the full boxes; 3×3×3 a 16-cell subset |
| §3.1 (238) | 3×3, 4×4, 3×5 (2¹⁵×6), 5×4 (2²⁰×120); 4 obligations | E, four lines |
| §3.2 (253, 255) | 2,354 families; 1,098 refuted | F (`family=2354 holds=2354 sort-test=2354`; `refuted=1098`) |
| §3.3 (267) | 25, 79, 265, 2,161, 41,503 = 44,033 | H, five lines |
| Figure 1 (271) | 13 cells, 4 of 2,880, one tie | B2 (`cells=13 admissible=4 of 2880; ties=[(0,4)]`; `recovered0=[1,2,0,4,3]` is the digraph's order) |
| §4.1 (283) | 193 / 3,271 / 63,775; 98 / 2,460 / 61,462; the three witnesses | H2, three lines, witnesses printed |
| Table 1 (318–329) | 175, 6,625 (4,819 reorderable), 343, 343; 4,200, 346,968, 5,488, 5,488 = 362,144 | I, four lines |
| §4.4 (342) | 2×2×2: 182 = 92 + 52 + 38; 2²²²: 64,804 = 3,438 + 38,768 + 22,598; 0 neither | B, "every defective subset" lines |
| §4.4 (353) | 90 cells, box 126, E = 36; 22 cells, E = 0 | C (`periodic cells=90 E=36; janet cells=22 E=0`) — but see A-9 |
| §5.1 (369–371) | 976, 6,912, E = 0; 216 | A, first and last lines |
| §5.2 (375–381) | 18 / 18 / none both; Σ(|Aᵢ|−1) = 17; 16 binding pairs; tree | A, lines 3–4 |
| §5.3 (387–391) | 20 of 20 twice; ≤ 2 root orders; 16 and 16; 3 of 20, 0 of 20; 94; 11,943,936 | I, two SAMPLED lines (`root_orders_tried_max` 2 and 1) and the sum/product line |
| §6.1 (401) | 1,792 and 1,966,080 pair constraints, all complement-closed | K, two box lines |
| §6.2 (421, 423–432) | 1, 2, 8; 1, 2, 8, 128; table 2/2, 8/8, 73/128, 1,442/32,768 | K (per-arity census; four "relations on m difference variables" lines) |
| §6.2 (436–441) | T = {000, 011, 101}; maj = 001; +110 → {110,101,011} | K, witness / REFUTATION / translation lines |
| Table 2 (448–463) | all forty entries | G, ten lines |
| Figure 4 (495) | 1.000, 0.724, 0.077, 0.050 | `fraction_reorderable` in results (47,416/65,536 = 0.72351 → 0.724; `SOURCES.md` says 0.723, A-28) |
| §6.4 (479) | bounds 3, 6, 12, 24, 48; steps 1, 2, 4, 8, 16 | J, six MACHINE-CHECKED lines (see A-13) |
| §7.2 (511) | 60 maps, seed 3, 60 of 60 | L |
| §7.3 (521) | 5,936; 15; 309; 380.9; 1,795; none zero | M |
| §7.4 (545) | 4 cells, the two endpoints, 972, 471,906; 475,800, 16, 503.5, 5,091, 739.0, none zero | A, "step(Lambda)" and "pushback" lines |
| §8 (561–569) | 3 boxes; 150; 1,387; 120; 120; detected | GUARDS block |
| §8 (611) | 90 = 52 + 29 + 6 + 3; four negative controls | summary line; SELFTEST block |

### A.3 Definitions, lemmas, theorems, proofs — against the source and step by step

Legend for "vs source": **=** the source's statement; **weaker**; **stronger** (paper proves or
quantifies more); **new** (not in the source). "Proof" records whether every step is justified.

| object (line) | source | vs source | proof | note |
|---|---|---|---|---|
| D1 alphabet convention (60) | not stated by the source (works at explicit caps) | new, explicit | — | correct that Lemma 3 and Theorem 3 need it; the exhibit at 241 is wrong (A-6) |
| D2–D3 (66–70) | MAIN §30.3.1 | = | — | reverse pairs ✓ |
| D4 ℛ, E (72–74) | MATH §IV.A 144–175, MAIN §15.2 | = | closure properties deferred to the companion, `X ⊆ ℛ(X)` shown | `max ∅ = −∞` never arises under D1 (A-17) |
| D5–D6 fibre, may precede (80–90) | MAIN §15.3 4297 | = | — | ✓ |
| D7 recovered order (92) | new | new | Lemma 4 | ✓ |
| D8 T-structured, Freuder (96–100) | MATH 376–384, 890–900 | = | — | the "Freuder condition" gloss is loose (A-20) |
| D9–D10 (102–106) | MAIN §30.3.2 | = | — | D9 defines the constraint on orientation variables; the paper then reasons about T (A-1) |
| D11 growth step (110) | MAIN §30.3.4 | new, precise | — | drop vs step conflated later (A-23) |
| Theorem 1 (120–150) | MAIN §30.3.1 measured ("1,487 instances, zero disagreements") | stronger: proved for every d | complete: (⇒) join and four meet cases ✓; (⇐) Steps 1–4 ✓, Step 2 via Theorem 3 (no circularity), Step 4 Baker–Pixley correctly invoked for the median term | opening hypothesis should be E = 0 not ℛ(X) = X (A-17) |
| Corollary 1 (154–160) | MAIN §16.5 4460 (proved there) | = | ✓ | the check evaluates the seven bounds, not the envelope conjunction (A-14) |
| Lemma 1 (166–170) | MAIN §15.3 lemma, App. A.7 | = | ✓ | — |
| Lemma 2 (172–176) | implicit in source | = | ✓ | — |
| Lemma 3 (178–190) | **not in the source** (it says "total order") | new | complete; each of the six applications of ⊑ and the two absorptions checked | correct; needs a non-empty F(v) — D1 |
| Theorem 2 (196–206) | MAIN §15.3, App. A.8 ("may precede is a total order") | corrected: total preorder | ✓ (b) both directions, (c) both | the source's sufficiency proof (10007–10015) assumes a total order; the paper's REFUTATION at 216 is right, and three of the four Z3 witnesses are the full box |
| Lemma 4 (208–212) | new | new | ✓ including the count ∏|c|! | — |
| Theorem 3 (228–236) | MAIN §30.3.3, App. A.8 | = (both directions) | ✓ interval half uses D1 once, as stated | — |
| Lemma 5 (247–251) | MAIN §30.3.3 "the fourth lemma" 8458–8462 | = | ✓ | "set of intervals" vs fibres that may coincide (R-9) |
| DECIDE₂ (261–265) | MAIN §30.3.2 "2-colouring plus transitivity" | different algorithm, honestly said | correctness ✓ | cost claim wrong (A-8) |
| §4.1 witness (281–283) | MAIN §15.3, §18.4 (not drawn on) | new | ✓ proof by the agreeing coordinate c | — |
| Theorem 4 (289–295) | MAIN §15.4 | stronger (factorisation proved) | ✓, and uses nothing about trees (A-19) | — |
| RECOVER, Theorem 5 (301–316) | MAIN §15.4 "root anywhere, fix the root by brute force, extend with backtracking; cost Σ|Aᵢ|!" | stronger (every solution) | correctness ✓ (induction on the subtree, informal but complete) | the cost paragraph is not proved and partly wrong (A-8) |
| Theorem 6 (333–340) | MATH failure modes A/B (classification without decision) | stronger | ✓ via Baker–Pixley | "exactly one of" phrasing (R-11) |
| §4.4 instance (353) | MAIN §16.7.1 | = for (period, group); the Janet count is the fixture's | — | 22 is not the occupied count (A-9) |
| §5.1–5.2 Λ (361–381) | MAIN §7, A.19, §16.8.6 | = | — | ✓; the seventh bound over-admits (R-16) |
| §5.3 (387–391) | MAIN §15.4 "20 of 20" | stronger (16 admissible measured) | — | which 16 is not said (A-21) |
| Lemma 6 (401) | MAIN §30.3.2 "3,781 constraints checked" | stronger (proved) | ✓ | — |
| Lemma 7 (405–411) | MAIN §30.3.2 | = | ✓ | typo `{0,τ} × {τ}` (A-18) |
| Theorem 7 (419) | MAIN §30.3.2 (implicit) | stated for every k | **no proof** (A-5) | — |
| Theorem 8 (423–434) | MAIN §30.3.2 "the law" (2/2, 14/14, 114/141) | different counts (paper's own parametrisation) | arity-3 row proved ✓ on T | **counts T, not C** (A-1) |
| §6.2 witness (436–441) | MAIN §30.3.8 "smallest obstruction on three XOR variables" | = | relation read off the witness ✓ | the same six cells give a non-bijunctive `C` at arity 4; the arity-3 witness is in A-1 |
| §6.3 census (448–463) | MAIN §30.3.4 (twelve boxes) | ten boxes, named | — | caption errors (A-7) |
| Theorem 9 (471–479) | MAIN §30.3.4 "verified by construction at d = 2..5" | stronger (proved all d) | ✓ attainment, bound (via Step 4), step | Rival misquoted (A-3); "growth step at the full box" = drop (A-23) |
| §6.5 (481–491) | MAIN §30.3.8 "NP-complete", declined | weaker, correctly | — | Schaefer-class sentence false (A-2); point 3 not meaningful (A-22); "open" needs the literature (R-23) |
| Lemma 8 (509–513) | MAIN §16.1 | = | ✓ | rank at a point (R-7) |
| §7.3 A(y) (519–531) | MAIN §16.8.4 (140 / 220 samples) | stronger (exhaustive) | — | ✓ |
| Lemma 9 (535–541) | MAIN §16.8.5 (removal lemma) | = | ✓ both directions | is Rival 1973's theorem in the maximal case (A-4) |
| §7.4 on Λ (545) | MAIN §16.8.5 step(Λ₈) = 4; §16.8.6 | = | — | ✓ |

### A.4 The three census figures `SOURCES.md` says do not reproduce

1. **Arity plate 2/2, 14/14, 114/141, 121/129 (MAIN 8425).** Not printed; Figure 4 is computed.
   The 14 is the number of non-empty proper complement-closed subsets of `{0,1}³` (16 − 2), i.e. the
   source counted relations on the three orientation variables *without* the origin requirement.
   Measured here on that parametrisation: **10 of the 14 are majority-closed, not 14 of 14** — the
   four failures are the three two-pair relations containing the origin and their complement-pair
   complement. So the plate's arity-3 claim fails under the source's own count as well as under the
   paper's `C` (5 of 8, A-1); it holds only for `T`. The 141 exceeds the 128 relations available on
   three difference variables and remains unexplained. Correctly excluded from the paper; the
   qualitative claim the paper keeps from it ("entirely bijunctive at arity ≤ 3") is the one that
   does not survive (A-1).
2. **18,736 = 18,736 at 2×3×3 (MAIN 8515).** Not printed. The check gives 20,068 (all subsets,
   including ∅ and singletons) and 13,051 (every value used); the source does not define its
   family. Nothing further can be said here.
3. **A(y): median 340 / minimum 59 (prose), 352 / 15 (plate) (MAIN 4688, 4712).** Not printed. The
   exhaustive 15 / 309 / 380.9 / 1,795 over all 5,936 non-cells reproduces in both runs; the plate's
   15 is the true minimum. Figure 5 is computed. ✓

### A.5 The Z3 obligations (all 29 encodings read)

- **Order variables** (`order_vars`): one Boolean per ordered pair; `Xor(s[u,v], s[v,u])` for
  `u < v` gives totality *and* antisymmetry; transitivity over distinct triples. A strict linear
  order, as D2 requires. ✓
- **Closure under (s, natural)** (`enc_closed_s`): for `x_axis = y_axis` the natural meet/join; else
  both orientations, the meet taking the s-lower axis value and the join the s-upper. Exactly D3
  with D2's coordinatewise operations. ✓ Guarded (150 instances).
- **⊑** (`enc_P`): for all ambient p over u and q over v, `X[p] ∧ X[q] → X[meet with axis u] ∧
  X[join with axis v]`. Exactly D6. ✓ Guarded (1,387 pairs).
- **s\*** (`enc_canonical`): fewer strict predecessors first, ties by label. Exactly D7. **Not
  guarded** (A-12).
- **Theorem 2** obligations 2(a) `obs → transP`, 2(b) both directions, 2(c) `obs ∧ refl ∧ total →
  (s* a strict order) ∧ closed(s*)`; every one under `prover.observed` (D1). The paper's "(c) in the
  form …" (line 214) matches. The REFUTATION `sat(obs ∧ order ∧ cl ∧ ¬antisym)` prints its witness.
  ✓ Boxes named ✓. Sixteen obligations ✓.
- **Theorem 3**: `interval` (b₁ < b₂ < b₃), `lo_le(u,v)` = every c ∈ F(v) has some c′ ≤ c in F(u),
  `hi_le` dually, `mono` = `s(u,v) → lo_le ∧ hi_le`; obligation `obs ∧ order → (cl ⟺ interval ∧
  mono)`. Correct under D1 (F(u) non-empty). **Not guarded** beyond `cl` (A-12).
- **Lemma 9**: `remclosed` on `S ∖ [a,b]`, `jp`/`mp` as join-/meet-primality within S; obligation
  `closed(S) ∧ S[a] ∧ S[b] → (remclosed ⟺ jp ∧ mp)`; all pairs a ≤ b including a = b; boxes and pair
  counts (36, 27, 54) as printed. Correct. **Not guarded** (A-12).
- **Theorem 9**: `closed ∧ proper ∧ AtLeast(bound+1)` unsat and `AtLeast(bound)` sat, d = 2..6; the
  flip argument makes "sublattice" the right object. ✓ The sixth MACHINE-CHECKED line is arithmetic
  (A-13).
- Boxes are named in the paper for every obligation ✓; no claim is marked MACHINE-CHECKED for a box
  the check does not cover ✓.

### A.6 Figures

- **Figure 1** (computed): matches B2 — 13 cells; the digraph's node order 1,2,0,4,3 is
  `recovered0`; one red opposed pair 0⇄4 is the tie; the right panel is the reverse of the left
  (checked cell by cell). Caption's 4 of 2,880 ✓. Small at print size (A-11).
- **Figure 2** (copied plate, audited row `figure-15.1.png`, md5 matches): panels and tree
  e–f–g–q–k–ℓ–n with 2S on k match `TREE`; "20 of 20, at two cap settings" ✓. The 2S node
  overprints the caption line of the plate ("from"); no axis labels on the panels; the plate says
  "with backtracking" while RECOVER is a DP (A-11, R-30).
- **Figure 3** (copied plate `fig26.png`, md5 matches): 1, 2, 4 filled and 8 open; 3/6/12/24 against
  4/8/16/32 ✓ (every number in J and G).
- **Figure 4** (computed): 2/2, 8/8, 73/128, 1,442/32,768 and the ten fractions with steps ✓ — but
  the left panel's title "the language leaves the bijunctive class at arity 4" carries A-1.
- **Figure 5** (computed): 5,936; minimum 15; median 309; dashed zero ✓.

### A.7 Typography on the rendered pages

Read on all 25 pages (pymupdf renders, 96 dpi, two pages per image) and the chrome screenshot of the
HTML head. No literal asterisk, backslash or stray markup; every table fits its column and no cell is
clipped; every figure appears with its caption beneath; subscripts that are Unicode in the source
render (2⁹, 2¹⁶, ², ³, ℛ₂, DECIDE₂, ⊑, ∧, ∨, ∏, Σ). The defects are A-10 (systematic) and A-11.

### A.8 Findings, Part A

| id | line(s) | severity | finding and the exact resolving change |
|---|---|---|---|
| **A-1** | 11, 31, 102–104, 405–441, 483, 491, 601, Figure 4 title | **BLOCKING** | **Bijunctivity is counted on the difference relation `T(x,y) ⊆ {0,1}^{k−1}` and asserted of the constraint `C(x,y) ⊆ {0,1}^k` that D9 defines on the orientation variables.** The map `σ ↦ (σ₁, σ₁⊕σ₂, …)` is affine, and majority-closure is not preserved by it: `T = {00, 01, 10}` (the 2-clause ¬δ₂ ∨ ¬δ₃) is bijunctive, but its preimage `C = {σ : σ₁ = σ₂ or σ₁ = σ₃} = {000, 001, 010, 101, 110, 111}` is not — `maj(001, 010, 111) = 011 ∉ C`. That `C` arises at `d = 3`: `X = {000, 111, 001, 110, 010, 101} ⊆ {0,1}³` uses every value, and at the pair `(000, 111)` `C(x,y) = X`. Independent census (majority-closure on complement-closed relations containing `0^k` and `1^k`): arity 2 **2 of 2**, arity 3 **5 of 8**, arity 4 **15 of 128**, arity 5 **52 of 32,768**. So "every constraint arising at arity ≤ 3 is bijunctive" and "the first non-bijunctive constraint appears at `d = 4` and not before" are false for the object the paper names; they are true of `T` only, and bijunctivity of `T` has no two-clause consequence for the orientation variables (a difference variable is an exclusive-or of two orientation variables, itself not bijunctive). Resolve by one of: (a) restate the abstract, §0 item 5, Theorem 8, §6.2 and §6.5 as results about difference relations, add the sentence that bijunctivity of `T` does not transfer to `C` with the witness above, and stop calling it "the constraint system on orientation variables"; or (b) recount on `C` (2/2, 5/8, 15/128, 52/32,768), move the boundary to arity 3 / `d = 3`, print the six-cell `d = 3` witness, and retitle the law. Either way `check.py`'s `majority_closed(T, k−1)` census and the exact table must count the object the theorem names, and Figure 4's left panel must be regenerated. The converse does hold and can be kept: `C` bijunctive ⇒ `T` bijunctive (T is C with σ₁ fixed at 0). |
| **A-2** | 37, 483 | MAJOR | "That places the *language* outside Schaefer's tractable classes" / "outside every one of Schaefer's tractable classes" is false: every `T` contains the origin (Lemma 7), so the language of difference relations is **0-valid**, a Schaefer tractable class, and every `C(x,y)` contains both constant assignments (Lemma 6), so `{C(x,y)}` is 0-valid and 1-valid. What is true: `T = {000, 011, 101}` is neither bijunctive nor affine (the two classes closed under XOR-translation, which is what "under translation and complement" preserves); the `C` of A-1 is neither bijunctive, Horn, dual-Horn nor affine; and only together with antisymmetry `o(u,v) ≠ o(v,u)` — the one relation that is neither 0- nor 1-valid — does the language `{C, ≠}` lie in none of the six classes. Rewrite both sentences to say exactly that. |
| **A-3** | 39, 479 | MAJOR | Rival's bound is printed as `|K| ≤ (3/2)|L|`, which is vacuous (`K ⊆ L`). Rival (1973) bounds a *maximal* sublattice from *below* — `|L| ≤ (3/2)|K|`, i.e. `|K| ≥ (2/3)|L|`, tight on the three-element chain — and proves that `L ∖ K` is an interval `[a,b]` with `a` join-irreducible and `b` meet-irreducible. Theorem 9 is an *upper* bound on every proper sublattice of `2^d`; "the Boolean case is tighter" compares an upper bound with a lower one. State Rival's result in the right direction and say instead that in `2^d` every maximal sublattice has exactly `3/4` of the box, strictly inside Rival's `2/3`. (The wording of Rival's theorem could not be fetched through the proxy; whichever way he writes it, the printed inequality cannot be it.) |
| **A-4** | 535–543 | MAJOR | Lemma 9 — `X ∖ [a,b]` is a sublattice iff `a` is join-prime and `b` meet-prime — is, in the maximal case, Rival's 1973 theorem (and its Lemma 1). It is presented as the paper's own. Mark the statement CITED (Rival 1973), keep the short proof, and say what is added (the biconditional for every interval, not only maximal complements). |
| **A-5** | 419–421, 601, 613 | MAJOR | Theorem 7 ("every subset of `{0,1}^{k−1}` containing the origin arises") is stated for every `k` and carries no proof; the record lists it EXHAUSTIVE for `k ≤ 4` only, and §8's list of results "proved for general d" omits it. The proof is two lines: given `T ∋ 0`, let `X = { σ, σ̄ : (σ₁⊕σ₂, …, σ₁⊕σ_k) ∈ T } ⊆ {0,1}^k`; `0^k, 1^k ∈ X` since `0 ∈ T`, so every value is used; at the pair `(0^k, 1^k)` the join determined by σ is σ and the meet is σ̄, so `C = X` and `T(x,y) = T`. Add it, mark PROVED, and list it at 613. |
| **A-6** | 241–243 | MAJOR | The exhibit for "the convention cannot be dropped" does not exhibit it: the five-cell set uses the value 1 (by `(1,1)`) and is simply not closed, which agrees with Theorem 3; "closed under both orders on `A₀` if the value 1 is deleted from `A₁`" cannot be done while `(1,1)` is a cell. The correct example: `X′ = {(0,0), (0,2), (1,0), (1,2)}` with `A₁` *declared* as `{0,1,2}` is closed (it is `{0,1} × {0,2}`) while `F(0) = {0,2}` is not an interval of `{0,1,2}`; under D1, `A₁ = {0,2}` and the fibre is an interval. Adding `(1,1)` makes 1 used and the meet `(0,1)` of `(0,2)` and `(1,1)` breaks closure — the theorem, not a counterexample. Replace the paragraph. |
| **A-7** | 463 (Table 2 caption), 448–461 | MAJOR | Two false statements in the caption, contradicted by the table's own last column. (i) "elsewhere is one less than the box": at 2×2×3 it is 10 of 12 and at 2×3×3 it is 16 of 18 — those products of chains have no doubly irreducible element, so by Lemma 9 (a = b) no single cell can be removed; the six 2-D boxes do have one, `(m−1, 0)`. (ii) "at the other eight it is attained elsewhere": at 2×2×3 and 2×3×3 `drop(full box) = box − largest = 2 = step`, so the full box attains it there too; the check's `step_attained_at_full_box` records only the *first* subset in mask order, which is why it prints False. Rewrite the caption accordingly and make `check.py` test `2^N − maxproper == step`. |
| **A-8** | 11, 25, 192, 263, 316, 391 | MAJOR | The cost claims. (i) Computing ⊑ costs `Σ_{u,v} |F(u)|·|F(v)| = |X|²` meets and joins, `O(d·|X|²)`, which §0 (25) and 192 say; 263 and 316 say `O(|A|²·|X|)`, which is wrong (`A₁ = {0,1}`, `X` the full 2×m box: `4m²` against `8m`). (ii) "the running time is output-sensitive" (316) is unproved and false for RECOVER as written: a tie-break at a child can fail at a grandchild, so its work is charged to no returned system. (iii) The `Σᵢ |Aᵢ|!` figure (391) and the abstract's "at a cost of one alphabet's permutations rather than the product" are never derived; they hold for the *memoised* form keyed on (node, order), which is what `check.py`'s `tree_recover` implements: at most `Σᵢ |Aᵢ|!` distinct evaluations, each `O(d·|X|²)` plus the enumeration of ≤ `|A_child|!` extensions, plus the output. State RECOVER with memoisation, prove that bound, delete "output-sensitive", correct the two `O(·)` claims, and qualify the abstract. |
| **A-9** | 353, 603 | MAJOR | "Coordinatised by `(n + ℓ, ℓ)` … the occupied cells number 22": the 22 are the fixture `{(n+ℓ, ℓ) : 1 ≤ n ≤ 7, ℓ ≤ min(n−1, 3)}` — the hydrogenic rule under caps — and include 6f, 7d and 7f, which no element through Z = 118 occupies. The occupied subshells number **19** (box 8 × 4 = 32); measured here, `E = 0` for those 19 (the closure admits nothing) and `E = 0` for the 20 through 8s. Print 19 (or 20 with 8s), name the box, and pin it in `check.py`; keep `E = 0`, which holds. |
| **A-10** | every page | MAJOR | Mathematics is set in code spans throughout, and inside a code span `_`, `^` and `{}` render literally: `A_i`, `x_i`, `φ_ij`, `s_i`, `x_{−i}`, `F_i(u)`, `∏_{j≠i} A_j`, `{0,1}^{k−1}`, `2^d`, `3·2^(d−2)`, `2^{2^d}` (also inside the §8 table, p. 23), `|A_r|!`, `Σ_i`, `A_0`, `A_1`, `π_ic`, `|A_c|`, `s_r`, `S_c`, `2^(2^{k−1}−1)`, `O(|A_1|²·|X|)` — on pages 1–25 without exception. §9 of the contract forbids it. Convert to Unicode (Aᵢ, xᵢ, φᵢⱼ, sᵢ, x₋ᵢ, Fᵢ(u), ∏ⱼ≠ᵢ Aⱼ, 2ᵈ, 3·2ᵈ⁻², A₀, A₁, sᵣ, |Aᵣ|!, Σᵢ, {0,1}ᵏ⁻¹); where no subscript glyph exists (`c` in `A_c`, `π_ic`, `s_c`, `S_c`) rename the child index to a letter that has one (j) or use a display block; write `2^{2^d}` as a display block or as "2 to the power 2ᵈ". |
| **A-11** | 301–308 (p. 12); 572 (p. 22); 271/385/467/495/529; Figure 2 | MINOR | (i) RECOVER's pseudocode renders as one run-on blockquote paragraph; put it in a fenced block. (ii) "**Obligations by status.**" is orphaned at the foot of p. 22 with its table on p. 23. (iii) Each figure prints a bare "Figure n" line (the image's alt text) above the "**Figure n.**" caption — a duplicated label; drop the alt text or accept it as the site's convention. (iv) Figure 2's plate: the 2S node overprints the plate's own caption line ("from"), and the panels carry no axis labels. (v) Figure 1's digraph labels are ~5 pt at print size. |
| **A-12** | 214, 238, 543, 561–569 | MAJOR | Guard coverage is narrower than §8 says. (i) The non-vacuity guard runs on 3×3, 2×2×3, 3×3×3 only — not on 4×4 (Theorem 2's fourth box) nor on Theorem 3's or Lemma 9's boxes. (ii) The fidelity guard evaluates `enc_closed_s` and `enc_P` only: `enc_canonical` (Theorem 2(c)), Theorem 3's `interval`/`lo_le`/`hi_le`/`mono`, Lemma 9's `remclosed`/`jp`/`mp` and the harness's `prover.closed` are never compared with a concrete implementation. "No Z3 result below is printed unless both pass" is true of run order, not of what the guards test. (iii) "ranging over **every** subset of the box" (214, 238, §8): every obligation carries `prover.observed`, so the range is every subset *using every value* — D1's convention, legitimately, but say so. Extend the guards (evaluate each encoding at concrete X, s against `closed_under`, a concrete interval/endpoint test, a concrete join-prime test) and the non-vacuity guard to every box, or state in §8 exactly which encodings are guarded. |
| **A-13** | 479, 605, 611, abstract 11 | MINOR | The 29 MACHINE-CHECKED lines include "step at the full box 2^d = … for d = 2..6", which is arithmetic on the five Z3 answers and not a Z3 obligation under §0's definition. Count 28 MACHINE-CHECKED + 1 derived, or label that line otherwise, and change "The five obligations give the bounds … and the step" to say the step is computed from them. |
| **A-14** | 156, 371, 505, 583 | MINOR | The check's "totality" line evaluates the seven defining bounds (χ) at all 6,912 ambient points, not the `d(d−1)` envelope comparisons Corollary 1 names; the envelope predicate's totality and agreement are entailed by the `E = 0` line (`ℛ(Λ) = Λ`, and `ℛ(Λ)` is by definition the set of ambient points satisfying that conjunction). Say in §5.1 which predicate was evaluated (the seven bounds — that is the reconstruction claim) and that Corollary 1's is covered by `E = 0`, or evaluate the envelope conjunction explicitly. |
| **A-15** | 434 | MINOR | Theorem 8's table is described as "computing its closure under the majority", but `check.py` computes the 2-clause closure for the exact table (bijunctive ⟺ 2-CNF-definable, Schaefer); majority-closure is used only for the arising relations and the witness. The two agree — 2, 8, 73 are cross-checked by both routes in the run, and an independent majority census here reproduces 1,442. Say which is computed, or compute both. |
| **A-16** | 421–432, 448–461, 283, 318–329, 521, 545 | MINOR | Numbers printed by the check but not asserted by it: the four "relations on m difference variables" lines pass unconditionally (`True`); the census lines assert only `step == 2^(d−2)` (not 506, 3,772, 47,416, 158, 1,342, 20,068, 3,290, nor the last column); the projection-gap lines assert only `gap > 0`; Table 1's 175 / 6,625 / 343 / 4,819 and the 44,033; A(y)'s 309 / 380.9 / 1,795; pushback's 503.5 / 739.0. A drift in any of them passes green. Pin them. |
| **A-17** | 126, 138 | MINOR | Theorem 1 (⇒) opens "Suppose `ℛ(X) = X`"; the hypothesis is `E(X) = 0`, and the step "with `X ⊆ ℛ(X)` (D4) this gives `ℛ(X) = X`" should be written. Step 2's parenthesis "when the set is empty, `φ_01(v) = −∞`" cannot occur under D1 (every `v` is used); delete it or say it is vacuous. |
| **A-18** | 411 | MINOR | "a union of pairs `{0,τ} × {τ}`" should read `{0,1} × {τ}`. |
| **A-19** | 289–295 | MINOR | Theorem 4's proof uses nothing about trees: for any graph `G` and `X` the intersection of the `G`-edge cylinders, `X` is closed iff each edge projection is. State it for a graph; the tree is what Theorem 5 needs. |
| **A-20** | 100 | MINOR | "This is the *Freuder condition*": Freuder (1982) says a tree-structured binary network is globally consistent after arc consistency; "T-structured" is the statement that `X` is the solution set of a binary network with graph `T`. Rephrase the citation so that it says which. |
| **A-21** | 389–391, 45 | MINOR | "Sixteen is eight reverse pairs" is arithmetic that hides two different structures. Measured here by listing the 16 at each setting: at 976 cells they are one global reversal × three pairs of values with identical fibres — `n: 2 ~ 3`, `e: 2 ~ 3` (because `ℓ, f ≤ 1`) and `2S: 0 ~ 1` (because `k ≥ 1`); at 216 cells the only tie is `2S: 0 ~ 1`, and the other factor 8 is the *independent reversal of three components* `{n, ℓ}`, `{e, f}`, `{k, q, g, 2S}`, because at `k ≤ 2` the bounds `k ≤ 4ℓ + 2` and `g ≤ 4f + 2` are vacuous (their pair projections are the full 2×2 and 2×3 products), so the tree falls into three pieces. D3's "admissible ordering systems come in reverse pairs" understates the symmetry at 216, where a proper subset of coordinates can be reversed. State the decomposition at each setting; it also explains "3 of 20" and "0 of 20". |
| **A-22** | 489 | MINOR | §6.5 point 3: "the constraint hypergraph has `d` vertices and up to `2^d − 1` hyperedges … treewidth returns the `2^d` bound" is not meaningful as written — the variables are the `Σᵢ |Aᵢ|(|Aᵢ|−1)` orientation variables, the hyperedges the sets `I(x,y)`, the treewidth of a complete hypergraph on `d` vertices is `d − 1`, and the bound a tree decomposition returns is `∏ᵢ |Aᵢ|!`, not `2^d`. Rewrite or drop the point. |
| **A-23** | 33, 110, 471, 467 | MINOR | "the growth step at the full Boolean box is exactly `2^(d−2)`" is `drop(2^d)`, not D11's `step(2^d)` (a maximum over all reorderable `Y`); §0 item 6 and Figure 3's open marker are drop values. Use `drop` explicitly where that is what is proved. |
| **A-24** | 641 | MINOR | Janet's French imprint "La classification hélicoïdale des éléments chimiques" (Beauvais, Imprimerie Départementale de l'Oise) is 1928; the 1929 item is the English "The helicoidal classification of the elements", *Chemical News* 138, 372–374 and 388–393. Fix the year or the title. |
| **A-25** | 11 | MINOR | Abstract: "The growth step of the reorderable family is `2^(d−2)`" is unqualified, while §0 says the census is exhaustive at `d ≤ 4` and only the value at the full box is known beyond. Qualify. |
| **A-26** | 348 | MINOR | "A median witness cannot be removed by any change that preserves all pair projections": a re-ordering changes meets and joins and hence the median, so the sentence needs "under the given ordering" and a definition of the admitted "change". |
| **A-27** | 112, 375, 535 | MINOR | Counting the bottom as join-irreducible / join-prime (and the top dually) is non-standard; it is declared, and Lemma 9's `a = bottom` case depends on it. Say so at Lemma 9, and reconcile "18 join-prime" with "17 generators above the bottom" in one sentence. |
| **A-28** | `SOURCES.md` (resumed-run note) | MINOR | `SOURCES.md` says Figure 4's fractions are "1.000, 0.723, 0.077, 0.050"; the check and the paper print 0.724 (47,416/65,536 = 0.72351). Unpublished, but the map should match. |
| **A-29** | 515 | MINOR | The Edlén quotation is located by the source at *Handbuch der Physik* XXVII, footnote to §17; the paper omits the section, and the quotation is second-hand (`SOURCES.md` says the Handbuch was not consulted). Add "§17" and, if the Handbuch is available to the author, verify the wording. |

---

## Part B — reader audits

### B.1 A mathematician (order theory, constraint satisfaction), who has never seen this material

I read the paper as a submission to *Order*. The definitions are all in place before use, which is
rarer than it should be, and Lemma 3 — transitivity of "may precede" with no hypothesis, by two
absorptions — is a clean piece of work that turns the source's "total order" into the correct
"total preorder" and gives Theorem 2 its content. Theorems 1, 3, 4, 5, 6 and 9 are proved, and I
followed every step. Three things would make me reject it as it stands.

- **R-1 (BLOCKING, lines 31, 102–104, 423–434, 483; = A-1).** The "reorderability law" is proved
  about the wrong object. D9 defines the constraint of a pair as `C(x,y) ⊆ {0,1}^I` on the
  orientation variables; Lemma 7 then passes to `T(x,y) ⊆ {0,1}^{k−1}` by `δ_t = σ₁ ⊕ σ_t`, and
  Theorem 8 counts majority-closed `T`. But the majority operation does not commute with
  exclusive-or, and bijunctivity is not invariant under that change of variables. Take `T =
  {00, 01, 10}`: bijunctive (one 2-clause). Its `C` is `{σ : σ₁ = σ₂ or σ₁ = σ₃}`, and
  `maj(001, 010, 111) = 011 ∉ C`. It arises at `d = 3`, from `X = {000, 111, 001, 110, 010, 101}` at
  the pair `(000, 111)`. Counting on `C`: 5 of 8 at arity 3, 15 of 128 at arity 4. So the sentence
  in bold at line 31 is false as a statement about the constraint system on orientation variables,
  and true only of an auxiliary relation from which nothing about two-satisfiability follows. Fix
  as in A-1; I would prefer option (b), because it is what the title promises.
- **R-2 (MAJOR, 419; = A-5).** Theorem 7 has no proof. The construction in A-5 is the proof; write
  it.
- **R-3 (MAJOR, 39, 479, 535; = A-3, A-4).** Rival's inequality is quoted backwards and Lemma 9 is
  Rival's theorem without the citation.
- **R-4 (MAJOR, 263, 316, 391, 11; = A-8).** The complexity paragraph is not a proof of anything:
  the `O(|A_c|²·|π|)` is wrong, "output-sensitive" is asserted, and `Σ|Aᵢ|!` appears only as a
  number. Prove the memoised bound or remove the cost claims from the abstract and §0.
- **R-5 (MAJOR, 241; = A-6).** The exhibit that D1 is load-bearing exhibits the opposite.
- **R-6 (MINOR, 289; = A-19).** Theorem 4 does not use that `T` is a tree. State it for a graph.
- **R-7 (MINOR, 509–511).** `D = b − rank(∂Φ/∂p)` is the rank at a point; "the number of
  functionally independent relations the derived quantities must satisfy" is the codimension of the
  image only where the rank is locally constant (or generically). Add "at a point of constant rank"
  or "generic".
- **R-8 (MINOR, 110, 448–463, 471; = A-23).** `drop` and `step` are conflated after D11, and the
  census counts the empty set and singletons as reorderable ("16 of 16") although D1 says an index is
  non-empty. Say what the family is.
- **R-9 (MINOR, 247).** Lemma 5 is stated for a set of distinct intervals but applied to fibres,
  which may coincide (that is what a tie is). State it for a multiset; the proof is unchanged.
- **R-10 (MINOR, 112; = A-27).** The bottom as join-irreducible is a convention; flag it at the point
  of use.
- **R-11 (MINOR, 333–336).** "Exactly one of the following holds" where the second alternative is
  itself a disjunction reads oddly; the content is `E(X) > 0 ⟺ (A) ∨ (B)`. Say that.
- **R-12 (MINOR, 411; = A-18).** `{0,τ} × {τ}`.
- **R-13 (MINOR, 489; = A-22).** Point 3 of §6.5 does not parse as mathematics.
- **R-14 (MINOR, 25, 192 against 263, 316).** The paper gives two incompatible costs for computing
  ⊑; `O(|X|²)` is the right one.

### B.2 An atomic physicist who works with NIST spectra

This paper is almost all order theory, and I read §5, §4.4's periodic instance, §7.2 and §7.3 as
the parts that touch the atom. There are no spectral quantities, no units and no data from the ASD
here, so nothing to check on that side; what I can check is what the index is said to be.

- **R-15 (MAJOR, 353; = A-9).** "The occupied cells number 22" for the left-step layout is not the
  count of anything occupied. Through oganesson the occupied subshells are 19 (1s … 7p); the 22
  add 6f, 7d and 7f, which no known atom fills. The `E = 0` conclusion survives on the 19 (I had it
  computed: the closure admits nothing), so the fix costs the paper nothing but the number, and
  should say "subshells", not "cells of the periodic system".
- **R-16 (MAJOR, 361–369, 519–531).** The paper says Λ "indexes transitions between electron
  configurations" and calls `2S ≤ k` "a vector-coupling envelope" without saying what an envelope
  admits: `2S` of the wrong parity. One electron (`k = 1`) has `2S = 1`; the cell
  `(1, 0, 1, 0, 1, 0, 0, 0)` — one electron, singlet — is in Λ. The parity rule `2S ≡ k (mod 2)` is
  not among the seven bounds, and it is not of the D4 form, so it could not be. That matters
  twice. First, §7.3 prices the insertion of a "fabricated" ambient non-cell while Λ itself already
  holds cells no atom has; the reader should be told that Λ is the index of *admissible labels* under
  seven envelope bounds, not of realised configurations. Second, the tie `2S: 0 ~ 1` that gives Λ
  its ambiguity at both cap settings (A-21) is exactly this over-admission: the index cannot
  distinguish `2S = 0` from `2S = 1` because it admits both for every `k`. One sentence at §5.1 and
  one at §5.3 resolve it.
- **R-17 (MINOR, 361–367).** "`g ≤ q` — counting": physically a target subshell may already hold
  electrons; the bound is a convention of the index (only the moved electrons are counted in `g`).
  Say so. "Hydrogenic radial condition" for `ℓ ≤ n − 1` is the range of the quantum numbers; fine,
  but "range of ℓ for principal quantum number n" is plainer.
- **R-18 (MINOR, 353).** The (period, group) instance is right (90 occupied of 126, He in group
  18, `E = 36`, no monotone bound at all), but its cells are elements and the left-step's cells are
  subshells; the paper says the two are not a bijection — say what each cell *is*.
- **R-19 (MINOR, 515; = A-29).** Edlén's remark is quoted at second hand; give the section (§17
  footnote) so a reader with the Handbuch can find it, and say the fit he declines is of a series
  formula's parameters to the levels of that series.
- **R-20 (MINOR, 519–527).** Give one physical example of an ambient non-cell (e.g. a 1p source
  subshell, `n = 1, ℓ = 1`) and name the cell at which `A(y) = 15` is attained, so the reader sees
  what is being priced.

### B.3 A journal referee

Novelty: the one-coordinate criterion as a total preorder with its linear extensions (Theorem 2,
Lemma 3, Lemma 4), the exhaustive comparison of the propagation's *solution sets* with brute force,
the diagnostic split with witnesses (Theorem 6), and the three-quarters theorem for the Boolean box
(Theorem 9, a short and correct proof from Baker–Pixley) are publishable as they stand. The
verification record is unusually honest — the 16 admissible orderings qualifying "20 of 20", the
declined NP-completeness headline, the unprinted source figures. Against that:

- **R-21 (BLOCKING; = A-1).** The title result is not established for the object it names. Until
  it is recounted on `C` or restated as a fact about difference relations with the transfer failure
  stated, the paper cannot go to the author as finished.
- **R-22 (MAJOR, 481–491).** "The problem's complexity is open here" is not situated in the
  literature. The nearest published result is **Green, M. J., and Cohen, D. A. (2008). Domain
  permutation reduction for constraint satisfaction problems. *Artificial Intelligence* 172 (8–9),
  1094–1118**, which asks exactly whether permutations of the domains exist making a CSP instance
  max-closed and (per its abstract, which I could read only in summary through the proxy — verify
  the wording) shows this tractable for bounded-arity instances over a Boolean domain and
  NP-complete for domain size three even for binary instances; the underlying class is **Jeavons,
  P. G., and Cooper, M. C. (1995). Tractable constraints on ordered domains. *Artificial
  Intelligence* 79 (2), 327–339**. Reorderability asks for min- *and* max-closure of one relation
  with an order per coordinate, and in the T-structured case it is literally a binary CSP whose
  constraints are the edge projections, so the distance to Green–Cohen is small. Cite both, state
  what they decide, and say precisely why neither settles reorderability (both directions: their
  hardness is for max-closed alone over arbitrary binary constraint sets on a common domain; their
  Boolean tractability is for a common Boolean domain with bounded arity, which is the `d`-ary
  relation of a Boolean box). "Open" then means "open relative to these".
- **R-23 (MAJOR, 39, 479, 535; = A-3, A-4).** Rival 1973 — misquoted and, at Lemma 9, uncited.
- **R-24 (MAJOR, 11, 25, 31, 33; = A-1, A-8, A-25).** The abstract and §0 promise more than the body
  delivers on three counts: "at a cost of one alphabet's permutations" (not proved as stated), "the
  growth step … is `2^(d−2)`" (exhaustive at `d ≤ 4` only), "the first non-bijunctive constraint
  appears at `d = 4`" (false for `C`).
- **R-25 (MAJOR, 37, 483; = A-2).** The Schaefer sentence is wrong: an origin-containing language
  is 0-valid.
- **R-26 (MINOR, 257, 617–659).** References to add: Jeavons & Cooper (1995) and Green & Cohen
  (2008) as above. Optional but apt: **Roberts, F. S. (1969). Indifference graphs. In F. Harary
  (ed.), *Proof Techniques in Graph Theory*, Academic Press, New York, 139–146** — the ordering
  with both endpoints non-decreasing is the canonical ordering of a proper interval family, and
  Lemma 5's "no strict nesting" is the weakening that admits shared endpoints; **Fishburn, P. C.
  (1985). *Interval Orders and Interval Graphs*. Wiley, New York** if "interval" is to be tied to
  the interval-order literature at all. The citation of Booth & Lueker and Tucker at 257 is
  decorative: say what a PQ-tree would decide here (the consecutive-ones property of the fibre
  matrix under a row permutation, which is the one-coordinate problem with the other order free) or
  drop it. Baker & Pixley (1975) *Math. Z.* 143, 165–174 and Rival (1973) *Proc. AMS* 37, 417–420
  are confirmed; Booth & Lueker, Tucker, Schaefer, Jeavons–Cohen–Gyssens, Freuder ×2, Dechter,
  Dechter–Pearl, Montanari, Deville et al., van Beek–Dechter, Ward, Moore, Birkhoff,
  Davey–Priestley, de Moura–Bjørner, Edlén, Scerri are correctly given. Janet: see A-24.
- **R-27 (MINOR, 561–613; = A-12, A-13, A-16).** The verification record overstates in three
  places: guard coverage, the 29, and the numbers the check prints without asserting.
- **R-28 (MINOR, 385).** Figure 2's plate says "with backtracking"; the paper's RECOVER is a dynamic
  program that enumerates linear extensions. Say in the caption that the plate's phrase refers to
  the enumeration.
- **R-29 (MINOR, 45).** "What is not established — Λ's recovery is exact up to the orderings that
  admit Λ at all. There are 16 of them" should say what they are (A-21); as printed a reader cannot
  tell whether 16 is a tie count, a symmetry count, or both.

---

## Part C — the record

| id | line(s) | severity | finding | disposition |
|---|---|---|---|---|
| A-1 | 11, 31, 102–104, 405–441, 483, 491, 601 | BLOCKING | bijunctivity counted on T, asserted of C; first non-bijunctive constraint on C is at arity 3 (d = 3), witness `{000,111,001,110,010,101}` |  **FIXED.** The audit's figures were verified independently in the check by two routes — majority-closure at k ≤ 4 and the two-clause closure at every k ≤ 5, agreeing on every relation — and reproduce: 2/2, 5/8, 15/128, 52/32,768, with the six-cell witness realising C(000,111) = X and maj(001,010,111) = 011 ∉ C while T = {00,01,10} is majority-closed. Theorem 8 is restated as the partition-constraint characterisation (bijunctive ⇔ the orientations agree on the blocks of a partition; B(k) of them, the Bell numbers) with a full proof for every k; the boundary moves to d = 3 in the thesis, abstract, §0 item 5, Theorem 8, §6.2, §6.5, Figure 4 (regenerated) and §8; the T census stays as a labelled auxiliary column with the transfer statement — C bijunctive ⇒ T bijunctive (checked), the converse failing from arity 3, and no two-clause consequence because an exclusive-or is not bijunctive (D10). The title is kept: the paper still states one reorderability law, now sharper, and the old title does not overclaim it; the superseded statement is recorded in SOURCES.md for the author. |
| A-2 | 37, 483 | MAJOR | "outside every Schaefer class" false: origin-containing language is 0-valid; hardness of the language needs ≠ |  **FIXED.** §0 and §6.5 now say: every pair constraint contains both constant assignments, so the language of pair constraints is 0-valid and 1-valid and trivially satisfiable; antisymmetry ≠ is neither; the arity-3 witness is closed under neither majority, ∧, ∨ nor ternary ⊕ (EXHAUSTIVE line), so {C₃, ≠} lies in none of the six classes and satisfiability *for that language* is NP-complete; the realisability gap is restated. |
| A-3 | 39, 479 | MAJOR | Rival's bound printed backwards (vacuous); "tighter" compares upper with lower bound |  **FIXED.** Rival's bound is stated as |L| ≤ (3/2)|K|, a lower bound on a maximal sublattice, tight on the three-element chain (EXHAUSTIVE line), and the "tighter" comparison is replaced by Corollary 2: every maximal proper sublattice of 2ᵈ is {x : xᵢ ≤ xⱼ}, exactly three quarters, d(d−1) of them (PROVED from Rival's interval theorem; EXHAUSTIVE at d = 2, 3, 4). Rival's interval theorem was verified through a reachable restatement (Adaricheva, Mata, Silberger and Zamojska-Dzienio, arXiv:2507.22682, quoting Rival 1973 Theorem 3 and the exact bibliographic entry); the bound's own wording could not be fetched and SOURCES.md says so. |
| A-4 | 535–543 | MAJOR | Lemma 9 is Rival 1973's theorem in the maximal case; uncited |  **FIXED.** Lemma 9 is headed "the maximal case is Rival 1973, CITED"; the paragraph before the proof states Rival's theorem and what the lemma adds (the biconditional for every interval of a closed index). |
| A-5 | 419–421, 601, 613 | MAJOR | Theorem 7 stated for every k, no proof; two-line proof supplied |  **FIXED.** Theorem 7 carries the audit's proof (X = C at the pair (0ᵏ, 1ᵏ)), marked PROVED; the construction is also run for every pair constraint at k ≤ 4 (138 relations, EXHAUSTIVE line) and Theorem 7 is listed among the general-d results in §8. |
| A-6 | 241–243 | MAJOR | D1 exhibit does not exhibit; correct example supplied |  **FIXED.** The paragraph is replaced by the audit's example — X′ = {0,1} × {0,2} with A₁ declared {0,1,2}: closed, fibre {0,2} not an interval of the declared chain, an interval under D1, and (1,1) breaking closure through the meet (0,1) — as a REFUTATION with a check line that verifies each clause. |
| A-7 | 463 | MAJOR | Table 2 caption: "one less than the box" false at 2×2×3, 2×3×3; "attained elsewhere" misleading |  **FIXED.** The caption is rewritten as the audit resolves it (attained at the full box in every row; one short exactly at d = 2 by the doubly irreducible corner; two short at the two non-Boolean 3-D boxes; 2ᵈ⁻² short at the Boolean boxes), and the check asserts box − largest = step in every box, largest = box − 1 exactly at d = 2, and the doubly-irreducible count 2 / 0. |
| A-8 | 11, 25, 192, 263, 316, 391 | MAJOR | cost of ⊑ misstated; "output-sensitive" unproved; Σ|Aᵢ|! underived (holds for the memoised form) |  **FIXED.** ⊑ costs |X|² meets and joins (§2.2, §0 item 2, DECIDE₂ — the two O(|A₁|²·|X|) claims are gone); "output-sensitive" is deleted and the reason stated; RECOVER is stated memoised in a fenced block and Theorem 5 carries the cost clause with its proof, O(F·(d·|X|² + F)) with F = Σᵢ|Aᵢ|!, for deciding and returning one system; the abstract and §0 say "at most Σᵢ|Aᵢ|! evaluations". |
| A-9 | 353, 603 | MAJOR | Janet "22 occupied cells" is the capped fixture incl. 6f, 7d, 7f; occupied are 19, E = 0 there |  **FIXED.** §4.4 prints the 19 subshells occupied through Z = 118 (box 32, E = 0) and the 20 with 8s (E = 0), from two new check lines; the fixture's 22 is no longer printed; the cells are named as subshells. |
| A-10 | all pages | MAJOR | mathematics in code spans: `_`, `^`, `{}` literal on every page |  **FIXED.** Every mathematics code span rewritten as Unicode (a mechanical pass, then hand rewrites where no glyph exists: ∏ᵢ Aᵢ for the product, (sᵢ : i = 1, …, d), the child index renamed c → j, "2 to the power 2ᵈ"); only `unsat` and `sat` remain as code spans; the pypdf text of the rendered PDF contains no underscore, caret or backslash (Repair record). |
| A-11 | 301–308, 572, figure labels, Figure 2 | MINOR | pseudocode run-on; orphaned heading p. 22; duplicated "Figure n" label; plate overprint, no axis labels; small Figure 1 |  **FIXED in (i), (ii), (iii), (v); (iv) DECLINED.** (i) RECOVER is a fenced block; (ii) see the Repair record for the page check; (iii) empty alt text on every figure; (v) Figure 1 redrawn with 10 pt node labels, larger nodes and a wider canvas. (iv) Figure 2 is a copied audited plate and is not redrawn; the overprint and the missing axis labels are the plate's, and the caption now says what its "with backtracking" refers to. |
| A-12 | 214, 238, 543, 561–569 | MAJOR | guards do not cover `enc_canonical`, Theorem 3's and Lemma 9's encodings, `prover.closed`; non-vacuity not on 4×4 etc.; "every subset" means every observed subset |  **FIXED.** The non-vacuity guard runs on all six Theorem 2/3 boxes, Lemma 9's three and Theorem 9's five; the fidelity guard now evaluates every encoding — s* (944 pairs), Theorem 3's interval / lo / hi / mono (120 instances, 3,700 comparisons, 120), Lemma 9's remclosed / jp / mp (120), the harness's closed (150) — against references written from the definitions; §8's guard table lists each; the status word and §2.3/§3.1 say "every subset that uses every value". |
| A-13 | 479, 605, 611 | MINOR | one of the 29 MACHINE-CHECKED lines is arithmetic, not a Z3 obligation |  **FIXED.** The drop is asserted on the five Z3 lines themselves; the separate line is gone; 28 MACHINE-CHECKED; §6.4 says the drop is arithmetic on the answers. |
| A-14 | 156, 371, 505 | MINOR | totality check evaluates the seven bounds, not Corollary 1's envelope conjunction (covered by E = 0) |  **FIXED.** The envelope conjunction (56 comparisons) is evaluated at all 6,912 ambient points by the guarded local routine — a new EXHAUSTIVE line — and Corollary 1, §5.1 and §7.1 say both predicates were evaluated. |
| A-15 | 434 | MINOR | table computed by 2-clause closure, described as majority closure |  **FIXED.** Theorem 8's EXHAUSTIVE paragraph says the two-clause closure decides at every k and majority-closure as well at k ≤ 4, agreeing on every relation; the check counts the disagreements (0). |
| A-16 | 421–432, 448–461, 283, 318–329, 521, 545 | MINOR | printed numbers not asserted by the check |  **FIXED.** Every number the check prints is asserted: the four difference-relation lines (2/8/128/32,768 and 2/8/73/1,442), the census (506, 3,772, 47,416, 158, 1,342, 20,068, 3,290 and the last column), the projection gap (193/3,271/63,775; 98/2,460/61,462), Table 1 (175/6,625/343/343; 4,819; 4,200/346,968/5,488), 44,033's five counts, A(y)'s 309/380.9/1,795, pushback's 503.5/739.0, the 16 admissible and 3/0 exact-or-dual, the 413 parity cells, the 32 minimum cells. |
| A-17 | 126, 138 | MINOR | Theorem 1 (⇒) hypothesis; vacuous `−∞` parenthesis |  **FIXED.** Theorem 1 (⇒) opens from E(X) = 0 and derives ℛ(X) = X; the −∞ clause is removed from D4 and Step 2 (the set is non-empty under D1, and Step 2 says why). |
| A-18 | 411 | MINOR | `{0,τ} × {τ}` typo |  **FIXED.** {0,1} × {τ}. |
| A-19 | 289–295 | MINOR | Theorem 4 holds for any graph |  **FIXED.** D8 defines G-structured for any graph; Theorem 4 is stated and proved for a graph; the tree is what Theorem 5 needs, and the paragraph after Theorem 4 says so. |
| A-20 | 100 | MINOR | "Freuder condition" gloss |  **FIXED.** D8 states what Freuder (1982) proves (backtrack-free after arc consistency on a tree) and what T-structured means (the solution set of the binary network is X). |
| A-21 | 389–391, 45 | MINOR | which 16 orderings: ties at 976, component reversals at 216 |  **FIXED.** §5.3 "Which sixteen" states the two structures (ties n:2~3, e:2~3, 2S:0~1 × global reversal at 976; tie 2S:0~1 × independent reversal of {n,ℓ}, {e,f}, {k,q,g,2S} at 216, with the vacuous edges named); two EXHAUSTIVE lines verify that RECOVER's sixteen equal the generated sets, the fibre identities and the binding pattern; §0's bullet says which. |
| A-22 | 489 | MINOR | §6.5 point 3 not meaningful |  **FIXED.** Point 3 rewritten as the audit states it (orientation variables, scopes I(x,y), complete hypergraph, treewidth d − 1, the ∏|Aᵢ|! bound), with the contrast to Theorem 5's hypothesis on X. |
| A-23 | 33, 110, 471, 467 | MINOR | drop vs step |  **FIXED.** drop is used where drop is proved: §0 item 6, Theorem 9 ("drop(2ᵈ) = 2ᵈ⁻², step ≥ drop"), D11's note, Figure 3's caption (the open marker is drop at the full box, a lower bound on the step). |
| A-24 | 641 | MINOR | Janet 1928 / 1929 |  **FIXED.** Janet (1928), the French imprint, cited as such. |
| A-25 | 11 | MINOR | abstract's unqualified step law |  **FIXED.** The abstract says "at every censused box of dimension d ≤ 4, and at the full Boolean box the drop is 2ᵈ⁻² for every d". |
| A-26 | 348 | MINOR | "any change that preserves all pair projections" undefined |  **FIXED.** Step 3 now says "under the given ordering, not removed by any operation that leaves every pair projection as it is", and that a re-ordering may remove it — the reorderability question of §6. |
| A-27 | 112, 375, 535 | MINOR | bottom counted as join-irreducible: flag at use |  **FIXED.** Notation flags the bottom-as-join-irreducible convention as declared and non-standard; Lemma 9's paragraph states the bottom case; §5.2 reconciles 18 join-primes = bottom + 17 join-irreducibles in one sentence; Corollary 2 says Rival's theorem uses the standard sense. |
| A-28 | SOURCES.md | MINOR | 0.723 vs 0.724 |  **FIXED.** SOURCES.md says 0.724. |
| A-29 | 515 | MINOR | Edlén §17, second-hand |  **FIXED.** Edlén (1964, §17, footnote), "quoted here at second hand", and the fit named as one of a series formula's parameters to the levels of that series. |
| R-1 | 31, 102–104, 423–434, 483 | BLOCKING | = A-1 (mathematician) |  **FIXED** — as A-1, option (b). |
| R-2 | 419 | MAJOR | = A-5 |  **FIXED** — as A-5. |
| R-3 | 39, 479, 535 | MAJOR | = A-3, A-4 |  **FIXED** — as A-3 and A-4. |
| R-4 | 263, 316, 391, 11 | MAJOR | = A-8 |  **FIXED** — as A-8: the memoised bound is proved; the two costs are one; "output-sensitive" is gone. |
| R-5 | 241 | MAJOR | = A-6 |  **FIXED** — as A-6. |
| R-6 | 289 | MINOR | = A-19 |  **FIXED** — as A-19. |
| R-7 | 509–511 | MINOR | rank at a point / constant rank |  **FIXED.** "the rank taken at a point; where the rank is locally constant, D is the number of functionally independent relations … near that point". |
| R-8 | 110, 448–463, 471 | MINOR | drop vs step; ∅ and singletons in the census |  **FIXED.** drop and step separated (A-23); Table 2's caption states the family (every subset, ∅ and singletons included, each trivially closed; the step over |Y| ≥ 2 as D11 says). |
| R-9 | 247 | MINOR | Lemma 5 for multisets |  **FIXED.** Lemma 5 is stated for a multiset, the proof notes it uses no distinctness, and the check adds the 5,084 multisets of 2..4 intervals on 2..5 points (EXHAUSTIVE). |
| R-10 | 112 | MINOR | = A-27 |  **FIXED** — as A-27. |
| R-11 | 333–336 | MINOR | "exactly one of" phrasing |  **FIXED.** "E(X) > 0 if and only if at least one of (A), (B) holds." |
| R-12 | 411 | MINOR | = A-18 |  **FIXED** — as A-18. |
| R-13 | 489 | MINOR | = A-22 |  **FIXED** — as A-22. |
| R-14 | 25, 192, 263, 316 | MINOR | two incompatible costs for ⊑ |  **FIXED** — as A-8: one cost, |X|² meets and joins. |
| R-15 | 353 | MAJOR | = A-9 (physicist) |  **FIXED** — as A-9. |
| R-16 | 361–369, 519–531 | MAJOR | `2S ≤ k` over-admits (parity); Λ is an index of admissible labels; the 2S tie is this over-admission |  **FIXED.** §5.1 says the seventh bound is an envelope, not a selection rule, that Λ holds (1,0,1,0,1,0,0,0) and 413 wrong-parity cells (new EXHAUSTIVE line), that the parity rule is not of D4's form, and that Λ is an index of admissible labels; §5.3 names the 2S:0~1 tie as this over-admission seen from the other side; §7.3 says A does not see admissible-but-unrealised labels. |
| R-17 | 361–367 | MINOR | `g ≤ q` is a convention; wording of the hydrogenic bound |  **FIXED.** "counting conventions of the index — g counts the moved electrons only, whatever the target subshell already holds"; "the range of ℓ for principal quantum number n". |
| R-18 | 353 | MINOR | elements vs subshells |  **FIXED.** §4.4 says the eighteen-column cells are elements and the left-step cells are subshells, and that the two indexes have different cells. |
| R-19 | 515 | MINOR | = A-29 |  **FIXED** — as A-29. |
| R-20 | 519–527 | MINOR | a physical example of a non-cell and of the A(y) = 15 cell |  **FIXED.** A 1p source subshell (n = 1, ℓ = 1, violating ℓ ≤ n − 1) is the example non-cell; the minimum 15 is attained at 32 non-cells, the first (2,1,3,2,2,1,3,0) with g = 3 > q = 2, both pinned in the check. |
| R-21 | 11, 31, 423–434, 483 | BLOCKING | = A-1 (referee) |  **FIXED** — as A-1. |
| R-22 | 481–491 | MAJOR | "open" not situated: Green & Cohen 2008, Jeavons & Cooper 1995 |  **FIXED.** §6.5 cites Jeavons and Cooper (1995) for the max-closed class and Green and Cohen (2008) for the domain permutation reduction, states what they decide — tractable over a Boolean domain, NP-hard in general (their Proposition 38) — and why neither settles reorderability in either direction; "open" is declared relative to them. The wording was verified against a reachable restatement (Takhanov, arXiv:1708.08292, §1 and §3.1, which quotes the problem, the Boolean tractability and Proposition 38); the abstract's "domain size three, binary instances" detail could not be verified and is not printed. |
| R-23 | 39, 479, 535 | MAJOR | = A-3, A-4 |  **FIXED** — as A-3 and A-4. |
| R-24 | 11, 25, 31, 33 | MAJOR | abstract/§0 promise more than delivered (three counts) |  **FIXED.** The three counts: "at most Σᵢ|Aᵢ|! evaluations" (proved), the step law qualified (A-25), the boundary at d = 3 (A-1). |
| R-25 | 37, 483 | MAJOR | = A-2 |  **FIXED** — as A-2. |
| R-26 | 257, 617–659 | MINOR | references to add; decorative PQ-tree citation |  **FIXED in part; the optional references DECLINED.** Jeavons and Cooper (1995) and Green and Cohen (2008) added and cited; the PQ-tree sentence now says what a PQ-tree decides (the consecutive-ones property of the fibre matrix under a row permutation) and why Lemma 5 asks less. Roberts (1969) and Fishburn (1985) are not added: the paper does not tie "interval" to the interval-order literature, and Lemma 5's families are named as interval systems of the consecutive-ones literature only. Janet: A-24. |
| R-27 | 561–613 | MINOR | = A-12, A-13, A-16 |  **FIXED** — as A-12, A-13, A-16. |
| R-28 | 385 | MINOR | "with backtracking" in the copied plate |  **FIXED.** Figure 2's caption says the plate's "with backtracking" refers to the enumeration of the root's orders and of the linear extensions, and that there is no other search. |
| R-29 | 45 | MINOR | say what the 16 are |  **FIXED.** §0's bullet says what the sixteen are at each setting and points at §5.3. |

**Counts.** BLOCKING 3 (one issue, A-1, seen by all three readers: A-1, R-1, R-21); MAJOR 20
(A-2 … A-10, A-12; R-2 … R-5, R-15, R-16, R-22 … R-25); MINOR 35. Distinct issues: 1 blocking,
12 major, 26 minor.

---

## Repair record — 2026-09-24

Repaired by the drafter against every finding above; nothing above was deleted or rewritten, and every
disposition in Part C is filled. A first repair attempt was cut off by a service limit while it was
independently verifying A-1 (its census script, run to completion here, agreed with the audit on every
figure: C-bijunctive 2, 5, 15, 52; the witness; 10 of 14 on the plate's own parametrisation; the
maximal sublattices of 2², 2³, 2⁴); this record is the completed repair.

**Dispositions.** BLOCKING 1: FIXED. MAJOR 12 distinct (A-2 … A-10, A-12, R-16, R-22): 12 FIXED.
MINOR 26 distinct: 24 FIXED, 2 FIXED in part with the remainder DECLINED — A-11 (iv), the copied
plate's own overprint and missing axis labels, not redrawn; R-26's optional references (Roberts 1969,
Fishburn 1985), not added. Every R-n that restates an A-n carries that A-n's disposition.

**How A-1 resolved.** The audit's census on C was reproduced in `check.py` by two independent
decision procedures (majority-closure at k ≤ 4; the two-clause closure at every k ≤ 5), agreeing on
every relation; the six-cell witness realises its constraint at (000, 111) and the constraint's
majority failure is computed, not asserted. The law is now Theorem 8: *a pair constraint is bijunctive
iff it is a partition constraint*, so the bijunctive constraints at arity k number B(k) — 2, 5, 15,
52 — proved for every k (⇐ directly; ⇒ through Schaefer's two-clause characterisation, complement
closure pairing the clauses into equalities) and enumerated at k ≤ 5. The boundary is at d = 3 in the
thesis, abstract, §0, Theorem 8, §6.5, Figure 4 and §8. The T census (2, 8, 73, 1,442) stays as a
labelled auxiliary column; C bijunctive ⇒ T bijunctive is checked (0 failures), the converse fails
from arity 3, and the paper says why bijunctivity of T has no two-clause consequence (an exclusive-or
is not bijunctive, D10). Title kept — see A-1's disposition and SOURCES.md §1a for the superseded
statement.

**What changed.** `PAPER.md`: every mathematics code span rewritten as Unicode (A-10); thesis,
abstract, §0 items 2, 4, 5, 6 and every "not established" bullet; D4 (no −∞), D8 (G-structured, the
Freuder gloss), D9 (pair and partition constraint), D10 (XOR not bijunctive), D11 (drop ≤ step),
Notation (the convention flagged); Theorem 1 (⇒) hypothesis and Step 2; §2.2 cost; §3.1 D1 exhibit;
Lemma 5 for multisets; the PQ-tree sentence; DECIDE₂ cost; Theorem 4 for a graph; RECOVER in a
fenced block, memoised, with Theorem 5's cost clause and proof; Theorem 6's phrasing; step 3 of the
loop; the Janet instance (19/20 subshells); §5.1 parity paragraph; §5.2 the 18 = 17 + bottom; Figure
2's caption; "Which sixteen"; Lemma 7's typo; Theorem 7 with proof; Theorem 8 restated and proved;
both witnesses; Table 2's and Figure 3's captions; Theorem 9 in terms of drop; Corollary 2 (new, with
Rival); §6.5 rewritten (0-/1-valid, ≠, the three points, Green–Cohen and Jeavons–Cooper); Figure 4's
caption; §7.2 rank at a point and Edlén §17; §7.3 the 1p example and the 32 minimum cells; Lemma 9
headed with Rival and the convention; §8 rewritten (guards table, obligations table, totals 111);
references (Green–Cohen, Jeavons–Cooper added; Janet 1928; Scerri's imprint unchanged). `check.py`
(never weakened; 30 new obligation lines, one folded): as listed in SOURCES.md "The repair".
`figures.py`: `fig_arity` redrawn on `pair_constraint_exact` with T as hollow markers; Figure 1's
labels enlarged. `FIGURES.tsv`: three new md5s (fig1, fig4, fig5), the plates unchanged.
`SOURCES.md`: rewritten for the repair (the plate's 10 of 14, the superseded law, Rival, Green–Cohen,
Jeavons–Cooper, Janet, the 19/20 subshells, 0.724).

**Re-verification.** `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH; python3 check.py
--selftest`: **111 obligations — 72 EXHAUSTIVE, 28 MACHINE-CHECKED, 8 REFUTATION, 3 SAMPLED — all
discharged, exit 0, 273.4 s; SELFTEST PASS on five negative controls** (the new fifth: "every arity-3
pair constraint is bijunctive" refuted, 5 of 8). Guards: non-vacuity on 14 boxes; fidelity 150 / 1,387
/ 944 / 150 (closure-under-s, ⊑, s*, harness closed), 120 / 3,700 / 120 (Theorem 3's encodings), 120
(Lemma 9's), 120 / 120 (reference closure), negative control 10 disagreements detected. `python3
papers/method/lint.py`: 0 hits. `render.py`: 28 pages. **Page check (BRIEF-AUDIT step 6)**: the
chromium screenshot of the HTML head and all 28 PDF pages (pymupdf, 110 dpi, read as 2×2 grids) show
Unicode subscripts and superscripts throughout, every figure with its caption beneath it, the RECOVER
block whole on p. 12, no table cell clipped, and "Obligations by status." on the same page (25) as its
table (A-11 (ii) resolved by the reflow; the guard table splits across pp. 24–25 at a row boundary,
which the template allows). pypdf text extraction of the PDF: **0 underscores, 0 carets, 0
backslashes**; 11 asterisks, all the recovered order s*. The status-word table splits across pp. 3–4
at a row boundary, as before.

**Unresolved, recorded for the author.** Rival's cardinality bound is printed in the audit's
direction, |L| ≤ (3/2)|K|, and is used in no proof; its wording could not be verified (only the
interval theorem was, through arXiv:2507.22682). Green and Cohen's "domain size three, binary
instances" detail is not printed because it could not be verified (their Boolean tractability and
general NP-hardness were, through arXiv:1708.08292). Janet 1928 follows the audit and is not
independently verified.
