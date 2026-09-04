# READ-ch13n.md — Phase R2 section read, chat 84

**Section:** main volume §16.1 through §16.5.1, **L4332–L4481** (150 lines) — the counting argument
and the three defences D1, D2, D3. Instruments: `r2-ch13n.py` (computable) and `r2-ch13o.py` (prose).

**Boundary, MEASURED.** HANDOFF-36 states Chapter 16 runs L4332–L4477 with Chapter 17 opening at
L4478. Both are false. Heading scan: Chapter 16 opens `## 16.` at **L4332** and its last subsection
§16.8.6 opens at L4772; **Chapter 17 opens at L4789**. Chapter 16 is **457 lines**, not 146. The
section read taken here is §16.1–§16.5.1; §16.6–§16.8 (L4482–L4788, 307 lines) is the next one.

---

## Claim census

**Computable (13 claims).** C1 L4338 the bound ⅅ = dim q − rank ∂Φ/∂p ≥ dim q − dim p; C2 L4342 its
verification on seven dimension pairs and 420 random nonlinear maps; C3 L4344 the corollary
dim q > dim p ⇒ ⅅ ≥ 1; C4 L4347 the Λ instance, rank 4 and ⅅ = 2 over p = (T, n, Z, σ),
q = (ν, δ, V, r, w, e), spanned by (a) V = 4ν/3 and (b) w = V·e; C5 L4352 (a) holds under the Rydberg
law and fails under three others, (b) holds under all four; C6 L4357 four unrelated perturbations,
verdicts identical; C7 L4363/L4371 the bracket held 56 of 56; C8 L4366/L4368 the δ̄ and V figures at
Z_eff = 1 and 2; C9 L4385–4394 the nine-row tripwire table; C10 L4396 150 of 216 rejected, 69.4 %;
C11 L4398–4400 d⁴ at 2S′ = 2 admitting v ∈ {2, 4} and d³ at 2S = 3 admitting 2J_c ∈ {1,3,5,7,9};
C12 L4415 the 540.0 / 1215.0 pair and L4423–4426 the 0.09σ agreement; C13 L4428 the tree, L4450–4457
totality on 6,912 ambient points, L4475 the process index at 36 cells with E = 0.

**Prose (10 claims).** P1 the eight in-range pointers (§12.11.1, §16.1, §16.4, §17-in-quote, §28.8,
§2.9, Register 242, Register 248); P2 Appendix A's A.4 → §16.1 and A.5 → §16.5; P3 the self-counts
restated elsewhere (56, fifty, 420, 150 of 216, 69.4 %, 6,912, 30,000, 36 cells, 0.09σ); P4 Figure
16.1's placement against the two figure registries; P5 attribution in range (Edlén; the antiprotonic
helium figures; Referee flag 5); P6 heading integrity; P7 Ruling 45/46 compliance; P8 census rows
1085–1089; P9 the caption's factual form; P10 the vocabulary of "offered" and "admissible".

---

## A. Deviations

**13n-01 — "That is ⅅ = 0" where the argument gives only ⅅ ≥ 0. Two sites.**
Printed, L4442: *"That is ⅅ = 0, in the special case dim q = dim p."* Restated, L11622:
*"1960 precedent for ⅅ = 0 when parameters equal observations (§16.4.1)."*
The counting argument printed at L4338 is ⅅ = dim q − rank ∂Φ/∂p ≥ dim q − dim p. At dim q = dim p it
yields ⅅ ≥ 0, not ⅅ = 0; ⅅ = 0 additionally requires the Jacobian to have full rank, which the
argument does not supply and which Edlén's least-squares setting does not guarantee. **Measured:** over
60 random nonlinear maps at dim q = dim p = 4 the rank was full in 60 of 60, so the claim is true
*generically*; a constructed map whose fourth output is a function of the first three has **rank 3,
hence ⅅ = 1 at dim q = dim p**. The substance (Edlén's "no check is possible" when parameters equal
levels) is sound; the equality as printed is not entailed. R3: weaken to *the bound vanishes* / *ⅅ = 0
when Φ has full rank*, at both sites together.

**13n-02 — the process index's 36 cells is not re-measurable from the printed text.**
L4475 and L7740 both print *"36 cells, closed, E = 0"* for the index (step, visible, alternatives,
committed) under **visible ≤ committed**. Neither site states the four alphabets. **Measured:** of all
alphabet readings with each coordinate carrying 2–5 values and either 0- or 1-based labels, **32 give
exactly 36 cells, and all 32 close with E = 0**. Only **3** of the 32 also admit the witness cell
L7742 names, (step 2, visible 2, alternatives 3, committed 0) — all three requiring committed ∈ {0,1}
— and in all three the witness lies outside the index, as L7742 says. So the arithmetic and the
closure claim are consistent and the witness is coherent, but 36 stands on alphabets the reader is
never given. The 13j-07 / 13l-09 class.

**13o-01 — "§16.4 form" names a form §16.4 does not contain. Eight sites. Closes a chat-74 DEFERRED item.**
The form-sentence is *"one coordinate bounded by a monotone function of one other"*. It occurs at
exactly **two** main-volume lines: **L1765**, where the constraint form is defined (*"Each constraint
reads xᵢ ≤ φ(xⱼ)"*), and **L7740**, where it is glossed as *"That is §16.4 form"*. **§16.4 (L4407–4430)
contains it zero times, contains "monotone" zero times, and is about ⅅ_def and two disjoint routes.**
Eight sites name the form after §16.4: **L261, L653, L4475, L4525, L4899, L7740, L8803, L11417**;
L4886 uses the same label negated (*"a bound on a sum, hence outside §16.4"*). R3: either §16.4 gains
the form, or all eight re-point to L1765's section. The two DEFERRED Chapter-16 items are hereby
closed — this is the '§16.4 "form"' item; the two-route protection is B4 below.

**13o-02 — the antiprotonic-helium figures are printed with no attribution.**
L4419–4426 gives cell (35,33), 804,633,059.0 ± 8.2 MHz measured directly against
804,633,057.8 ± 10.6 MHz from two-photon minus a different single-photon, agreeing at 0.09σ.
**Measured:** those two figures occur at exactly two sites in the whole work (L4423, L4424) and no
source is named anywhere in range — the only named sources in the 150 lines are Edlén and Rydberg.
This is a published laboratory result used as a worked case for path-disjointness "realised in
hardware". Under R-ATTR the measurement is attributable and is not attributed. With 13h-05, 13h-06,
13j-13 and 13l-04.

**13o-03 — the "fifty cells" at L4368 against "56 of 56" at L4363 and "fifty-six" at L4371.**
One paragraph runs three populations: the bracket held **56 of 56**; correction gave spread 0.047
**over ten members** and V to 0.86 % **across the fifty cells**; an index carrying only what its method
consumes would have passed **fifty-six** wrong cells. **Measured:** the string "fifty cells" occurs
nowhere else in any volume; "56 of 56" occurs at L4137 (a different claim — separating pairs) and at
L7395 (the same D1 case, where it is again 56). Neither the ten members nor the fifty cells is defined
at either site. Either 50 is an error for 56, or the corrected pass covered 50 of the 56 and the text
does not say so. Not resolvable from the printed text.

**13o-04 — four heading titles are truncated, their remainder rendering as body text.**
**Measured** volume-wide: **L4407/4408** — `### 16.4 D2 — D_def catches a wrong derivation, but only
under two` with `routes` alone on the next line; **L7721/7722** — `### 28.8 A dependent choice is
indexable, and naming the` with `dependency names the coordinate`; **L6582/6583** — `### 23.14 Two
kinds of bound, and the book has been calling them` with `one`; **L8659/8660** — `### 31.2 String
theory — the pole, the generating function, and a` with `disanalogy`. Every contents list, running
head and cross-reference generated from these headings carries the truncated title. (Seven further
heading-plus-indented-line pairs were measured and are legitimate — a displayed formula or table
header following the heading: L574, L579, L4277, L6606, L6634, L7207, L10173.)

**13o-05 — Figure 16.1's registry line number is wrong, extending 13l-07's offset range.**
FIGURE_ASSETS.md L23 and FIGURE_MAP.md L20 register Figure 16.1 at **4342**; it is placed at **L4373**.
Offset **−31**, outside 13l-07's measured range of −11 to +29. Both registries are process members, so
this is production, not reader-facing; the consequence is unchanged — R3 must recompute that column
from the `![Figure N.N]` placements.

---

## B. Verified

**B1 — the counting argument and its corollary hold on every map run.** 420 random nonlinear maps over
seven dimension pairs (2,3), (3,4), (3,5), (4,6), (5,7), (2,4), (4,4), Jacobians by central difference
and rank by pivoted elimination: **ⅅ = dim q − rank ≥ dim q − dim p in 420 of 420**, and
**dim q > dim p ⇒ ⅅ ≥ 1 in 360 of 360**. L4342's "seven dimension pairs and 420 random nonlinear maps"
is reproduced at that scale.

**B2 — the Λ instance's arithmetic and the independence of its two relations.** dim q − dim p = 6 − 4
= 2, and the gradients of V − 4ν/3 and w − V·e on q-space have **rank 2**: the two named relations are
functionally independent, as "spanned by" requires.

**B3 — the D1 tripwire table is exact, all nine rows, and so is the population behind it.**
Independently recomputed by Slater-determinant enumeration (allowed 2S from
N(M_S = S) − N(M_S = S+1)): **0 of 9 printed rows disagree**. Every admissible set matches
(s¹{1}, s²{0}, p²{0,2}, p³{1,3}, p⁵{1}, d⁴{0,2,4}, d⁷{1,3}, d⁹{1}, f⁴{0,2,4}), and every
rejected/offered pair matches under offered = k + 1. Summed over s, p, d and f complete at
k = 1…4ℓ+2: **offered 216, admissible 66, rejected 150, share 69.4444 %** — L4396's *"150 of 216
offered assignments are rejected — 69.4 %"* reproduces **exactly**, as do its restatements at L858,
L8173–8174 and L11097 and Register 242. This is the strongest verified claim in the section: the
figure is a population, not a sample, and the population is the one the text names.

**B4 — the two-route protection, and the constraint that ⅅ_def must be built deliberately.**
DEFERRED, chat 74. §16.4's two worked cases both hold as printed. **Measured:** w = 3ν·e against
w = V·e with V = 4ν/3 gives a ratio of exactly **9/4 = 2.2500**, and 1215.0 / 540.0 = **2.2500** — the
mis-stated law's value is the correct one scaled by exactly that factor, so the two printed numbers are
mutually consistent and the disagreement is the one the section claims. The apparatus case:
|804,633,059.0 − 804,633,057.8| = 1.2 MHz against a combined σ of √(8.2² + 10.6²) = 13.401 MHz gives
**0.0895σ**, printed as **0.09σ** — correct to the stated precision. And L4428's constraint on where
ⅅ_def can come from holds: **Λ₈'s constraint graph is a tree** (7 edges on 8 nodes, `is_tree` True)
with **exactly one path between each of the 28 coordinate pairs, 0 exceptions** — the constraints
supply no redundancy, so ⅅ_def must indeed be built from derived quantities. This DEFERRED item closes
affirmatively.

**B5 — totality on every ambient point, and the sampling remark.** Λ₈'s eight alphabets are
(3, 2, 3, 4, 3, 2, 4, 4), whose product is **6,912** — L4454's ambient box. Enumerated in full:
**χ ∈ {0,1} at all 6,912 points, 0 undecided**, and **χ agrees with membership at 6,912 of 6,912**,
including all **976** cells. L4455's arithmetic holds too: 30,000 draws from a box of 6,912 is more
draws than cells. Register 248 restates it correctly.

**B6 — d⁴ at 2S′ = 2 admits v ∈ {2, 4}, and d³ at 2S = 3 admits 2J_c ∈ {1, 3, 5, 7, 9}.** Both
recomputed from the term decomposition. The seniority set is exactly {2, 4}. The five 2J values are
right because d³ carries **two** quartet terms, ⁴P (L = 1, giving 2J ∈ {1,3,5}) and ⁴F (L = 3, giving
2J ∈ {3,5,7,9}); their union is the printed set. Read from ⁴F alone the printed set would carry a
spurious 2J = 1, which is why this was measured rather than checked by eye.

**B7 — every in-range pointer other than §16.4 resolves to the claim.** §12.11.1 (L3032) does compute
exact sets; §16.1 (L4335) does carry the general form L4446 credits it with; §28.8 (L7721) does apply
χ to the process coordinate; §2.9 (L617) does state *refuse rather than coerce*; Register 242 and 248
restate their sections correctly. L4440's `§17` is Edlén's Handbuch §17 inside a quoted citation, not
this book's Chapter 17 — a pointer-regex artefact, not a defect.

**B8 — Appendix A's A.4 and A.5 resolve to the claim, clearing 13l-03's neighbours.** A.4
*"ⅅ ≥ dim q − dim p" → §16.1, in full*: §16.1 carries the statement and a proof closed with ∎.
A.5 *"χ_Λ is total" → §16.5, in full*: §16.5 opens with the theorem and a proof closed with ∎. The
same measurement on A.7 returns **0** matches at §16.3, reproducing 13l-03. Chat 83's reading stands:
one misdirected row, not a drifted table.

**B9 — no Ruling 45 or 46 breach in range.** No script name, build number, internal file reference or
editorial-process remark appears in the 150 lines. Figure 16.1's caption states facts only.

---

## C. Incidental

**C1** — The Appendix A index at L9945–9954 carries **nine rows**, and the nine are exactly the
statements that have **no** `### A.N` section; the **ten** statements that do have sections (A.3, A.8,
A.9–A.13, A.15, A.18, A.19) appear in no index row. The two sets are disjoint, which is coherent as a
design — the index routes the reader to statements proved in the body — but a reader looking up A.8,
the site of 13l-01, will not find it in the index that heads its own appendix. Under the compendium
standard's "robust index" this is a navigation gap, for the Appendix A segment.

**C2** — §16.1's Λ instance names q = (ν, δ, V, r, w, e) and asserts rank 4 without defining δ, r or e
in range, so the rank itself is not re-measurable here; only dim q − dim p = 2 and the independence of
the two named relations are. Likewise C5/C6 (L4352, L4357 — the four laws and the four perturbations)
name neither the laws' parameterisation nor the perturbations, so "verdicts identical" is recorded,
not measured. If those definitions live in Chapter 12, the pointer is absent.

**C3** — L4368 prints the corrected spread as **0.047 over ten members** and the corrected V agreement
as **0.86 %**; 1.271 appears once elsewhere (sc L306) and 0.86 at twelve sites. The "ten members" is
the third undefined population in that paragraph, with the fifty cells and the fifty-six.

**C4** — 23 of the 150 lines are 4-space-indented paragraphs that render as code blocks, carrying the
chapter's theorem statements, corollary, proofs and the Edlén quotation. This is the chapter's
display convention and is consistent within it; noted for the typesetting pass, since a code face for
a theorem is not the intent.

**C5** — "Referee flag 5" (L4380) is answered in full here; flags are also referenced at L3126, L7919
and L8215. Whether the flag list itself is reader-facing is a question for the front-matter pass.
