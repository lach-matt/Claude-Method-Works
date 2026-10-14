# AUDIT — 05-tower, "The Tower over Λ: from Eight Coordinates to Thirteen"

Audited 2026-09-24 against `PAPER.md` (639 lines, dated 21 September 2026), `check.py` (1,223 lines),
`SOURCES.md`, `FIGURES.tsv`, `figures.py`, the five figures, and the render at `out/05-tower.pdf`
(27 pages) / `out/05-tower.html`. The brief is `papers/method/BRIEF-AUDIT.md`; the contract is
`PAPER-SPEC.md` §4, §5, §8, §9, §10. The audit records; it edits neither `PAPER.md` nor `check.py`.

**What was run.**

| run | result |
|---|---|
| `python3 check.py` (PATH = `method/bin` first, Python 3.12, Z3 5.1.0) | **122 obligations — 99 EXHAUSTIVE, 8 MACHINE-CHECKED, 7 REFUTATION, 8 GUARD — 0 failures**, 307 s under load (281 s alone), exit 0 |
| `python3 check.py --selftest` | 6 obligations — 2 GUARD, 4 REFUTATION — 0 failures, the five negative controls all refuted, exit 0 |
| the same run on the 03:36 copy of `check.py`, compared line by line | identical obligation lines (timings aside) |
| `python3 papers/method/lint.py papers/method/05-tower` | 0 hits |
| md5 of the five figures against `FIGURES.tsv` | all five match; `sections-plate.png` is byte-identical to `extracted/archives/restore-point-2-13/fig-sections.png`, the row `method/PROOF-FIGURES.tsv` names for Figure 12.2 |
| render read | all 27 pages read as images (a shared scratchpad was overwritten mid-audit by another job; pages 22–25 were re-rasterised and re-read) |

Two computations were made for this audit and are not in `check.py`; they are reproduced in A-2
and A-1 below with their outputs, so the drafter can pin them.

---

## Part A — content audit

### A.0 · Every printed number against the check

Every number in Table 1, Table 2, Table 3, Table 4, Table 5, §0 items 1–7, §2, §3, §5, §6, §6.1,
§7, §8 and §9 was located on a line of the check's output. The six counts, boxes, fills and pair
counts; 97,323,996; 204 / 6,912 / 415; 287,809 and 286; the terms of p¹–p³; φ̂ = {1:3, 2:4, 3:5};
3,4,5,4,3,0 and 1,2,3,2,1,0 and 1, 0; the envelope 3,4,5,5,5,5; the six Table-2 rows including
10,585 / 77.9% and 13,585 at 2K = 0; the eight graph rows and the two-parent 14 / (0,0,1,1,2,2);
the twelve sections and three totals; ⟨q⟩ = 1.4631 and 1.9159; 55,755 / 153,680 / 15,150 / 45,450 /
21.4% / 22.8% / 12,675; 22,275 / 57,845 / 35,570 / 64,290 / 248,076,675 and the exhibited meet;
8,018 / 0; the rank profile, 122 at 11, 185 at 12, 976 = 8 × 122, the alphabet sizes, 17, 20, 976
down-sets, 1,113,045,672, 17, the bottom and top; branching 4,4,6,8,9, slack 2 / 0; 77 / 105 / 138
steps, 808 / 1,376 / 2,111 and 264 / 442 / 688 signatures, seeds 7 / 8 / 9, 25 / 29 / 33 slots,
27 / 28 / 29 kept steps against 59 / 61 / 63 reduced signatures, greedy 7 / 9 / 9, packings 6 / 7 / 8,
compressions 139 / 207 / 282; the solver's meet model a₁=0, b₁=4, c₁=4, a₂=1, b₂=2, c₂=3; 2,862 / 0,
12,654 / 0, 150 / 0 / 126; and the obligation totals 122 = 99 + 8 + 7 + 8 — all reproduce.

Numbers that are **printed by the check but not asserted**, or **not computed at all**, are A-16.

### A.1 · Definitions against the source

| object | source | relation | note |
|---|---|---|---|
| D1–D2 (box, sublattice) | main §6.1 lines 1537–1549; §7.3 | the source's | "closed" reserved for sublattice-of-own-box: consistent with `01-closure-law` D6 |
| D3 (bound, parent, arity) | the paper's own (SOURCES.md "Interpretations" 1) | stronger than the source | the distinction is sound and is what the text needs; see A-4 for what it does not deliver |
| D4 (monotone) | §7.2 | the source's | — |
| D5 (extension) | — | the paper's own | fine |
| D6 (ℛ, E) | §6.1 lines 1537–1549 | the source's | the source's φ̂ᵢⱼ is written φᵢⱼ; the collision with D12's φ̂ is thereby avoided, as SOURCES.md says |
| D7 (rank) | §12.9, §8 | the source's | **the symbol r is reused in Prop. 14 for an undefined quantity** (A-11) |
| D8 (constraint graph) | `cgraph.py`; §7.2 fig. 7.1 | the source's | — |
| D9 (coordinates) | `tower-2.py`; §12.11.1 | the source's | 2J_c → 2Jₚ renamed for typography, recorded in SOURCES.md |
| D10 (bounds) | `tower-2.py` byte-for-byte; §7.1; §12.11.3.1 | the source's | the seven Λ₈ constraints and the five extensions match the instrument exactly; the one-parent reading of the twelfth is the source's own definition (main lines 3068–3071) and `kparent.py` |
| D11 (caps) | §7.4 lines 1806–1812 | the source's | — |
| D12 (terms, σ, μ, φ̂) | §12.11.1 vocabulary block lines 3062–3080 | **weaker than what Prop. 2 uses** | φ̂ := max over ℓ of μ(ℓ,k) is not monotone by definition (A-8) |
| D13 (step, slot, seed) | §14.5.9 lines 3922–3960; `01-closure-law` D8 and Theorem 13 | the companion paper's, exactly | step = "least t at which φᵢⱼ attains its value" ⟺ "φᵢⱼ(a) ≠ φᵢⱼ(a′) or a least"; witness and slot identical; ℛ(G) in Box(G) identical to the companion's "ambient regime" |
| D14 (transfer decomposition) | §12.6–§12.6.2 lines 2364–2395 | the source's | — |

### A.2 · Results against the source and the check, proof by proof

| object | source | statement vs. source | proof | check |
|---|---|---|---|---|
| Prop. 1 (projection) | §12.11.1 "every stage projects exactly" | same | complete | `each stage projects exactly onto the one below` |
| Prop. 2 (closure) | §7.3 proof; §12.11.1 sweep table lines 3109–3125 | same | the Λ₈ half is complete and correct (join by monotonicity, meet by the case split on j); the induction step is Theorem 1; **E = 0 is asserted from the sweep and not proved, though it is provable in two lines** (A-4) | sweep + pairs, all six stages |
| Prop. 3 (fill) | §12.11.0.10 | same | the cap-independent argument is sound given Prop. 1 | `fill falls strictly` |
| Props. 4–6, spin ceiling, core–orbit range | §12.11.2; §12.11.0.6; §12.11.1 | same | enumerations | all pinned except μ(0,·) (A-16) |
| Table 2 | §12.11.1 density column; §12.11.1.1 | five of six reproduce, the 9′ row correctly omitted; both axis-11 readings printed | — | six rows pinned; **the text's claim that Table 2 is Theorem 2 (iv) is false at axes 9 and 12** (A-2); **the axis-13 sentence at line 232 is wrong** (A-3) |
| Lemma 1 | §14.1 / Appendix A.2, one direction | weaker than the source (deliberately, SOURCES.md "Interpretations" 2) | complete and correct | — |
| Theorem 1 | §7.3 generalised | stronger than the source (two parent indices) | complete; D4 is exactly what is used | Z3 over ℤ **at j = j′ only** (A-12); finite-box form 2⁹ × h |
| Theorem 2 | Appendix A.14 / §12.11.2 "each admissible extension is the monotone envelope of its physics" | **narrower than every use made of it**: F is a function of one coordinate a ∈ Aⱼ, while the exact fibres of axes 9–12 depend on two or three coordinates | (i)–(iv) correct for the statement as written | not machine-checked, and §10 says so honestly; A-2 |
| Theorem 3 | Appendix A.18 lines 10177–10190; `coupling.py` | same, with both witnesses | join proof complete; the two meet witnesses verified | Z3 join `unsat`; meet `sat`; witnesses; **check labels these "Theorem 5(i)/(ii)"** (A-13) |
| Theorem 4 | Appendix A.15 lines 10160–10175 (B_k a sublattice, C join-closed and not; 12,654 at cap 8) | same | (i) complete both ways; (ii) correctly reduced to Theorem 3's lower half; (iii) witness | Z3 with k free; C; witness; 12,654 by brute force |
| Theorem 5 (i), (ii) | §12.11.3 / Appendix A.16–A.17 | (i), (ii) the source's, made precise | (i) is Theorem 1; (ii) transported correctly, and §6 exhibits the hypothesis | EXHAUSTIVE over the thirteen bounds |
| **Theorem 5 (iii)** | Appendix A.15's closing sentence ("what the tower relies on at axis 13 is B₁") | **not what the source's own grading says** (§12.11.0.10 grades Λ₁₃ "envelope") and **false as written** | the substitution claimed does not produce the band (A-1) | none |
| Corollary 1 | §12.11.3 | **the paper's own count of cases is inconsistent** (A-9) and its thirteenth clause rests on A-1 | — | — |
| the derived-quantity remark | Appendix A.11 | same | witness | pinned |
| Props. 7–8 | `cgraph.py` with the one-parent edge list; register 1790 corrected by `kparent.py` | same as the corrected reading | Prop. 8's proof is right in substance, **miscounts the bounds** (A-14) | all rows pinned; the "independent derivation" is a hand-typed list (A-18) |
| Prop. 9 | `cgraph.py`'s own `EDGES_BY_STAGE[12]` | same | — | pinned |
| the cycle-rank remark | Mathematical Compendium's Freuder entry lines 376–384 | **misattributes the guarantee** (A-4) | — | — |
| Prop. 10 | §12.6.1, §12.11.5 | same | complete up to one wording slip (A-20) | pinned, six stages + set identity at 8 and 13 |
| Prop. 11 | §12.8.1–§12.8.2; §12.11.5 | the ⟨q⟩ row corrects the source's 1.887 → 1.9159 as SOURCES.md records | — | ⟨q⟩ pinned only at the two ends (A-16) |
| Props. 12–13 | §12.11.5 (15,150 / 45,450); Compendium "The tree or the tightness" (22,275 / 35,570) | same | witness verified | failure counts printed, not asserted (A-16) |
| Prop. 14 | §12.1 lines 2311–2330 | same as the source, which is the problem (A-11) | the parity argument is correct and trivial | 8,018 / 0 pinned |
| Lemma 2 | standard | — | complete | extremes pinned |
| Props. 15–17 | §8.3; Appendix A.19; §12.9–§12.10.1 | same | Prop. 16's "why G is a cell" complete; the join-irreducible ⟺ one-lower-cover ⟺ unit-step chain is sound but stated in an order a reader cannot follow (R-5) | all pinned |
| Theorem 6 | not in the source in this form; the paper's own | — | complete; the negative control's **formula is misprinted** (A-15) | pinned; control pinned |
| Props. 18–19 | Compendium "The tower's two ends joined" lines ~2140–2150 | same | enumerations | pinned |
| Lemma 3 | `01-closure-law` Theorem 13 | identical, both directions | complete and correct in both directions; the (⇒) slot argument Box(X) = Box(ℛ(G)) ⊆ Box(G) ⊆ Box(X) is right | GUARD 40/40 + 40/40 + the seed-minus-one control |
| **Theorem 7** | §14.5.8 lines 3830–3836 and register 511 print 7, 9, 9 (greedy); §14.5.9 seed(Λ₈) = 7 exact | **7, 8, 9 — the source's 9 at Λ₉ does not reproduce as a seed, and SOURCES.md records it correctly**; the greedy figures do reproduce and are printed as greedy | see A.3 | branch and bound 264 / 442 / 688; Z3 `unsat` on 59 / 61 / 63 against 27 / 28 / 29; the reductions as GUARDs; **no non-vacuity or fidelity guard on the seed rows** (A-7) |

### A.3 · Theorem 7, the two reductions, and whether the guards establish equivalence

Read against `check.py` lines 1020–1034 (`reduce_instance`) and 1104–1122.

- **Lower bound, first reduction (set dominance).** A cover using a signature s ⊂ t may replace s by
  t; the optimum over the 808 signatures equals the optimum over the 264 maximal ones. The GUARD
  `red1` (every signature sits inside a maximal one) is a tautology for a finite family, but it is
  checked. Exact.
- **Second reduction (element dominance).** `keep` is built so that a step e is dropped only when
  some kept k has cov(k) ⊆ cov(e) *over the maximal signatures*: every maximal signature covering k
  covers e. Then any cover of the kept steps by maximal signatures covers every step, and the
  feasible sets coincide; the optimum is unchanged. Exact, *for the instance over the maximal
  signatures*, which is the instance in hand after the first reduction. The paper's prose (line 556,
  line 611) says "every **cell** that witnesses one of the kept steps", a stronger statement than
  what is checked. **Audit computation:** at Λ₈ all 50 dropped steps are also dominated over all
  808 signatures (0 counterexamples), so the prose is true there; but the check does not test the
  prose's form, and the equivalence rests on the maximal-signature form. Acceptable; a one-clause
  fix in the prose ("every maximal covering signature") would make the text say what is checked.
- **Third reduction (set dominance again after restriction).** `dom2` = maximal non-empty
  restrictions; `red3` checks every restricted maximal signature sits inside a `dom2` member. Exact.
- **The solver query.** Boolean variables over `dom2`; each kept step covered; `AtMost(want−1)`.
  `unsat` ⇒ no (want−1)-cover of the kept steps from `dom2` ⇒ none from the restricted family ⇒ none
  of all steps from the maximal signatures ⇒ none from all cells. **The chain is valid and the guards
  do establish it.** No number changed by the reductions.
- **Upper bound.** The exhibited cover realises every slot (asserted), so by Lemma 3 it is a seed;
  regeneration under two staircases (asserted). Sound.
- **What is missing** is not the reductions but the two guards the paper's own status word demands
  of every MACHINE-CHECKED row (A-7): the seed rows carry neither a non-vacuity check (the cover
  constraints are satisfiable with `want` sets under the same encoding) nor an encoding-fidelity
  check (the Boolean formula evaluated on the exhibited cover and on the cover minus one cell).
  Both are three lines each.

### A.4 · The Z3 encodings, the guards, and the boxes

| obligation | encoding is the operator the paper defines? | both guards run before reporting? | box named in the paper? |
|---|---|---|---|
| Theorem 1 over ℤ (`counting_axis_formula`) | **almost**: lo and hi are taken at one parent value x; the theorem allows j ≠ j′ (A-12). The monotonicity hypothesis is stated at the two points, correctly, and forces l₁ = l₂, h₁ = h₂ at x₁ = x₂. | non-vacuity yes; **fidelity: no Z3 predicate is ever evaluated** (A-6) | "the unbounded integers, 8 free variables" — yes |
| Theorem 1, finite box (`counting_box_claim`) | yes: every closed S ⊆ 3×3, every monotone h into {−1..2}, y ∈ {0,1,2}, lower bound the constant 0 | non-vacuity yes (S proper, h non-constant); fidelity as above | "every closed subset of a 3 × 3 box" — yes |
| Theorem 3 join; meet refutation | yes | as above | yes |
| Theorem 4 (i) with k free; (ii); (iii) | yes | non-vacuity for the bands is `sat(hyp)` with no non-degeneracy demand — weaker than the others but adequate | yes |
| Theorem 7 × 3 (`AtMost` over `dom2`) | yes | **neither of the two defining guards; the reduction guards only** (A-7) | "every subset of the reduced family, 59 / 61 / 63" — yes |

No claim is marked MACHINE-CHECKED for a box the check does not cover. §0 item 2, however, marks
**Theorem 2 and Theorem 5 MACHINE-CHECKED** and the record does not (A-5).

### A.5 · Figures against captions and text

| figure | image read | caption | finding |
|---|---|---|---|
| 1 `stages.png` | two panels, six labelled bars 976 … 199,130 on a log axis; six labelled fill points 14.12% … 0.42% | facts only, all pinned | none |
| 2 `constraint-graph.png` | 13 vertices, 13 edges, triangle 2S′–g–v in green, q annotated, blue rims on n ℓ k 2S q e f g 2S′ v, **orange rims on 2Jₚ, 2K and 2J** | "an exact bound in the first colour, a monotone envelope in the second" | **the rims disagree with Corollary 1 in two places**: 2S′ is drawn exact (the text says envelope), 2J is drawn envelope (the text says "carried exactly") — A-10; the figure is right about 2J and the text is wrong (A-1) |
| 3 `sections-plate.png` | the audited plate; four sections, four Λ₈ insets, the eight figures as printed | matches the plate's own labels and Table 4 | none in content; typography T-1 |
| 4 `profile.png` | six series on a log axis; peaks 89,700 and 345 at q = 2 | matches | labels "165" and "136" sit on their markers (T-5) |
| 5 `brackets.png` | five bands, one composite with the direct outline inside it | matches Props. 18–19 | the sixth panel's legend overlaps the band (T-5) |

### A.6 · Findings

**A-1 · BLOCKING · lines 3, 13, 23, 336, 342, 346 (and 31, 44).** *Theorem 5(iii) is false as
written, and with it "the thirteenth axis is carried exactly".* Clause (iii) says: replace xⱼ by a
constant k in (ii)'s F(x) = { y : |xᵢ − xⱼ| ≤ y ≤ xᵢ + xⱼ } and "then F(x) = { y : |xᵢ − y| ≤ k }
is the band Bₖ". The substitution gives { y : |xᵢ − k| ≤ y ≤ xᵢ + k }, which is not the band and is
not a sublattice: in the plane (xᵢ, y) the cells (0, k) and (k, 0) both satisfy it and their meet
(0, 0) does not (k ≥ 1). The two sets agree exactly where xᵢ ≥ k. For the tower at k = 1 the physical
thirteenth fibre — even before the parity congruence — is { 2J : |2K − 1| ≤ 2J ≤ 2K + 1 }, which
differs from D10's band at every 2K = 0 cell (physics {1}, band {0, 1}), and it fails meet-closure
*inside the construction*: audit computation, (1,0,1,0,1,0,0,0,0,0,0,**0,1**) ∧
(1,0,1,0,1,0,0,0,0,0,0,**1,0**) = (…,0,0), the last two coordinates (2K, 2J); 185,545 cells at that
reading against 199,130. With the congruence the exact fibre is the doublet of Table 2 (128,225
cells, 64.4%). D10's |2J − 2K| ≤ 1, 2J ≥ 0 is precisely Theorem 2's least envelope of that doublet
(audit computation: l⋆ = 0,0,1,2,…, h⋆ = 2K + 1, total 199,130 — the only axis at which the
construction's bound *is* the least envelope, see A-2). So the thirteenth axis is carried as an
envelope, exactly as the eleventh and twelfth are, with a realised share of 64.4%; what is special
about it is that its envelope is a band of arity 1 and its loss is a congruence plus one cell per
2K = 0. The source's own grading agrees (§12.11.0.10: Λ₁₃ "envelope"), and so does the paper's
Figure 2, which rims 2J as an envelope bound. The thesis sentence (line 3), the abstract (line 13),
§0 (line 23), the Theorem 4 remark (line 336), Theorem 5(iii) (line 342) and Corollary 1 (line 346)
all say "carried exactly". **Resolving change:** restate (iii) as: *if xⱼ is replaced by a constant k,
the exact set { y : |xᵢ − k| ≤ y ≤ xᵢ + k } is not a sublattice (witness (0,k) ∧ (k,0)); its
Theorem-2 envelope over xᵢ is { y : max(l⋆(xᵢ)) ≤ y ≤ xᵢ + k }, which for k = 1 on ℕ is the band
B₁, a sublattice by Theorem 4(i), of arity 1;* and rewrite the thesis, abstract, §0 item 2's gloss,
line 336 and Corollary 1 to say that the last step is carried as a band-shaped envelope whose only
loss is the parity congruence and the K = 0 singleton — not "exactly". Then A-3 and A-10 follow.

**A-2 · BLOCKING · lines 13, 219–230, 282–300, 346.** *Theorem 2 is stated for F a function of one
coordinate, and is applied to fibres that depend on two or three; and the construction's bounds at
axes 9 and 12 are not Theorem 2's least envelope, so "Table 2 is clause (iv)" and "carried as its
monotone envelope" are false there.* Theorem 2 takes F : Aⱼ → sets. The exact fibres of Table 2
depend on (f, g) at axis 9, on (f, g, 2S′) at axis 10, on (ℓ, k, 2S) at axis 11 and on (2Jₚ, f) at
axis 12; only axis 13's depends on one coordinate. Read in the only way that makes sense — F on the
whole cell, l⋆(a) := min{ min F(x) : xⱼ ≥ a }, h⋆(a) := max{ max F(x) : xⱼ ≤ a } — the theorem and
its proof go through verbatim, but then the least envelope is **not** D10's bound: audit computation,
axis 9 (j = g): l⋆ = (0, 0, 0, **1**), h⋆ = (0, 1, 2, 3), admitting **1,638** cells against D10's
1,654; axis 12 (j = 2Jₚ): l⋆ = (0, 0, 0, **1, 2, 3**), h⋆ = 2Jₚ + 2, admitting **60,320** against
70,905; axis 13: l⋆, h⋆ reproduce D10 exactly, 199,130. D10's lower bound 0 at axes 9 and 12 is a
member of 𝔈 and not its least member. Line 300 ("Table 2 is clause (iv), evaluated at each axis"),
line 13 ("admit only their monotone envelopes"), line 346 ("carried as its envelope") and §3.1's
first paragraph therefore overstate. **Resolving change:** (a) restate Theorem 2 with F : S → finite
non-empty sets and the fibre-wise l⋆, h⋆ above (proof unchanged in shape; (iv) unchanged); (b) say
that the construction's bound is *an* envelope of Theorem 2's shape and that at axes 9 and 12 it is
not the least one, printing the least envelope's counts 1,638 and 60,320 beside the admitted
column (and pinning them in `check.py`); (c) for axis 10, whose bound has two parents, say Theorem 2
in one-coordinate form does not apply and the admitted count is D10's; (d) delete "Table 2 is clause
(iv)" or make it true.

**A-3 · MAJOR · line 232.** *"the loss is not this axis's, it is inherited through 2K" is false.*
The admissible fibre at axis 13 is a triplet {2K−1, 2K, 2K+1} ∩ ℕ and the exact fibre a doublet;
128,225 = 2 · 70,905 − 13,585 says the loss is one value in three at every cell, the value 2K
excluded by the congruence 2J ≡ 2K + 1 (mod 2), plus the singleton at 2K = 0. That is this axis's
own loss (the source attributes the ⅔ to exactly this and the residue to the K = 0 singlet, main
lines 3145–3150). Nothing about it is inherited through 2K. **Resolving change:** replace the
sentence with the parity attribution; it then supports A-1's rewording.

**A-4 · MAJOR · lines 166–180, 250, 390.** *E(Λₛ) = 0 is provable in two lines and the paper
proves it only by sweep, while §5's remark attributes the guarantee to treewidth 1 and says
treewidth 2 removes it.* Every bound of D10 has the form xᵢ ≤ ψ(xⱼ) with ψ monotone (a lower bound
xᵢ ≥ ψ(xⱼ) with ψ monotone is xⱼ ≤ ψ⁻(xᵢ) with ψ⁻ monotone: 2S′ ≤ v is v ≥ 2S′, 2K ≤ 2J + 1 is
2J ≥ 2K − 1), the rest are alphabets. For such an X and any x ∈ ℛ(X), xᵢ ≤ φᵢⱼ(xⱼ) ≤ ψ(xⱼ) on every
constraint pair, because y ∈ X with yⱼ ≤ xⱼ has yᵢ ≤ ψ(yⱼ) ≤ ψ(xⱼ); so ℛ(X) ⊆ X, and with Lemma 1's
containment ℛ(X) = X. The argument uses the shape of the bounds and nothing about the graph; it
holds at every stage, at every cap, with or without the triangle. Hence (i) Prop. 2's "E = 0" can be
PROVED rather than swept; (ii) line 390's "at treewidth 1 the pairwise operator ℛ is exact by a
theorem, and at treewidth 2 it is not guaranteed to be … what the cycle removes is the guarantee" is
wrong — the guarantee never came from the treewidth; Freuder's theorem is about arc-consistent
tree-structured networks and is not the statement being used. **Resolving change:** add a lemma
(PROVED, one paragraph) to §4 or §2; keep the sweep as EXHAUSTIVE confirmation; rewrite the remark
so that what the cycle costs is the tree-clustering guarantee for *arbitrary* binary constraints,
not ℛ's exactness on this construction.

**A-5 · MAJOR · line 31.** *§0 item 2 marks Theorem 2 and Theorem 5 MACHINE-CHECKED; Table 5 marks
them PROVED only, and §10 line 615 explains why Theorem 2 cannot be.* **Resolving change:** "Theorems
1, 3 and 4 are PROVED and MACHINE-CHECKED over the unbounded integers; Theorems 2 and 5 are
PROVED, and Theorem 5's instances are EXHAUSTIVE over the thirteen bounds."

**A-6 · MAJOR · line 609; `check.py` 799–858.** *The encoding-fidelity guard never evaluates a Z3
predicate.* `guard_encoding` builds T₆ from a Python lambda `abs(a−b) <= c <= a+b`, compares that set
to `coupling.triangle`, and brute-forces failures; the Theorem 1 guard extends random sublattices in
Python. The Z3 formulas of `triangle_formulas`, `band_formulas`, `cband_formulas` and
`counting_axis_formula` — built from the `If`-based `Abs`, `Max`, `Min` — are not evaluated on a
single concrete cell. A wrong `Abs` would pass the guard. Line 609's "the predicates the solver is
given are evaluated in ordinary arithmetic against independently written concrete implementations"
is therefore not what the code does. **Resolving change:** in `guard_encoding`, substitute concrete
integers into each Z3 predicate (`z3.simplify(z3.substitute(f, …))`, or a fresh solver per cell) over
the cap-6 / cap-8 / cap-7 boxes and over the 150 random instances, and compare cell by cell with the
lambdas and the instrument; print the disagreement count; keep the existing brute force as the
independent reference.

**A-7 · MAJOR · lines 48, 552–558, 611; `check.py` 1104–1122.** *The three MACHINE-CHECKED rows of
Theorem 7 carry neither of the two guards §0's status word requires.* §0 defines MACHINE-CHECKED as
"with the non-vacuity and encoding-fidelity guards passed first"; §10 line 605 then restricts "both
guards" to "no MACHINE-CHECKED row of §4", and line 611 substitutes the two reduction guards for the
seed rows. The reductions are exact (A.3), but they are a different thing from non-vacuity (are the
cover constraints satisfiable at all under this encoding?) and fidelity (does the Boolean encoding
say "covers" of the exhibited cover and "does not cover" of the cover minus one cell?). **Resolving
change:** add both to `check_seed` (a `sat` with `AtMost(want)` that returns the branch-and-bound
cover, and a concrete evaluation of the clause set on `best` and on `best[1:]`), report them as
GUARD, and make §0's definition true of every MACHINE-CHECKED row; or, failing that, amend the
definition to name the seed rows' guards.

**A-8 · MAJOR · lines 131, 176.** *D12's φ̂(k) := max{ μ(ℓ, k) : ℓ ≤ ℓₘₐₓ } is not monotone by
definition, and Prop. 2 says "φ̂ monotone by D12".* At ℓ ≤ 1 the definition gives 3, 4, 5, 4, 3, 0
for k = 1..6 — Prop. 6's own non-monotone row. It is monotone at the caps because k ≤ 3, which the
check pins, but the induction in Prop. 2 invokes it as a property of the definition. **Resolving
change:** define φ̂(k) := max{ μ(ℓ, k′) : ℓ ≤ ℓₘₐₓ, k′ ≤ k } (the running maximum, which is what
"monotone envelope" means and what Prop. 6 computes), and note it equals {1:3, 2:4, 3:5} at D11.

**A-9 · MAJOR · lines 13, 346.** *The abstract and Corollary 1 disagree on how many coupling axes
are triangles.* The abstract: "of the five adjoined coordinates, the two whose exact physical set is
a triangle in two coordinates admit only their monotone envelopes, and the one whose second argument
is a constant … is carried exactly". Corollary 1: "Of the three bounds whose exact physical content
is a coupling condition, the ninth and the eleventh carry a non-monotone realised ceiling … the
twelfth's exact content is a triangle of arity 2 … and the thirteenth's is B₁" — four axes named
under "three", and only one of them a triangle in two coordinates. **Resolving change:** one count,
stated once: four coupling axes (9, 11, 12, 13) and one seniority axis (10); 9 and 11 non-monotone
ceilings, 12 a triangle of arity 2 with a congruence, 13 a triangle with one side constant plus a
congruence (after A-1).

**A-10 · MAJOR · line 367; `figures.py` 75–76.** *Figure 2's rims disagree with Corollary 1.*
`envelope = {"2J_c", "2K", "2J"}`: 2S′ is drawn exact and 2J is drawn as an envelope; the text says
the opposite of both. The spec: "a figure whose data disagrees with the paper's text is not used".
**Resolving change:** after A-1 and A-9 the figure is right about 2J; add 2S′ (and, if the ninth
row of Table 2 is the criterion, 2S′ only — v's bound is the source's "law") to the envelope set, or
change the rim criterion to the one the text uses and say which in the caption.

**A-11 · MAJOR · lines 452–460 (and 86, D7).** *§6.2 proves a triviality about eight undefined
quantities.* "e, ν, V" and "T, r, δ, the local spacing and w" are never defined, "rise or fall along
a series" is never defined (no series exists in the paper), "the surface", "cylinder" and "Möbius
band" are never defined, and the symbol r collides with the rank of D7. The proposition proved is
that a sign assignment induced by a bipartition is balanced — Harary's balance theorem (1953),
uncited — and it bears on nothing in §§2–9. **Resolving change:** delete §6.2 and the 8,018 / 0
row; or define the eight quantities from a cell, define the edge sign, cite Harary (1953), and say
what the balance claim does for the tower.

**A-12 · MINOR · lines 276, 578; `check.py` 732–745.** *The Z3 form of Theorem 1 is the case
j = j′.* lo and hi are both taken at one parent value x; the theorem allows lo of xⱼ and hi of xⱼ′.
The encoded statement implies the general one — the conclusion is a conjunction of a lower-bound
clause using only l and an upper-bound clause using only h, and each can be instantiated with the
other bound made constant — but that two-line reduction is not in the paper, and Table 5 says the
theorem is checked "over the unbounded integers" without qualification. **Resolving change:** add the
two variables x′₁, x′₂ for hi's parent (a one-line change to `counting_axis_formula` and to the
non-vacuity guard), or state the encoding and the reduction in Table 5.

**A-13 · MINOR · `check.py` 908–913.** The obligations for the paper's **Theorem 3** are printed as
"Theorem 5(i): the triangle region … is join-closed" and "Theorem 5(ii): … not meet-closed". The
verification record is checked against this output. **Resolving change:** rename the two obligations.

**A-14 · MINOR · line 384.** "Of the thirteen bounds, twelve name two coordinates of the same block
and one, g ≤ q, … the bound q ≤ k …" counts fourteen. Eleven are within a block (six in P, five in T)
and two are at q. **Resolving change:** "eleven".

**A-15 · MINOR · line 504.** The negative control's multinomial is printed as
"20!/(2!1!2!3!2!1!3!3!)"; the spans sum to 17 and the check computes 17!/(…) = 205,837,632,000, the
number Table 5 prints. **Resolving change:** "17!".

**A-16 · MINOR · lines 205, 428, 444; `check.py` 320, 362.** Numbers printed by the check but not
asserted, or not computed: the four middle entries of the ⟨q⟩ row (1.6850, 1.8304, 1.8874, 1.9141 —
only the two ends are pinned); Prop. 13's 52,767,450 failing meets and 28,742,850 failing joins
(pinned only as "bm > 0"); μ(0, 1) = 1 and μ(0, 2) = 0 (computed inside `mu` and never asserted).
**Resolving change:** pin each.

**A-17 · MINOR · lines 45–53, 572–604.** "Six are used and never merged": SAMPLED appears in the
table and nowhere else; GUARD appears in fourteen Table-5 cells and in every check line but is not
in the vocabulary. **Resolving change:** drop SAMPLED from the table or add GUARD to it ("a
soundness check on the checker, never a result").

**A-18 · MINOR · line 592; SOURCES.md "The correction".** "the edge list against an independent
derivation from the bounds" — `EDGES` in `check.py` is a hand-typed dictionary, not derived from
`tower-2.py`. It is an independent *transcription*. **Resolving change:** say so, or derive it (the
instrument's five comprehensions name their parents explicitly).

**A-19 · MINOR · line 444.** "E = 35,570 — larger than the set is short" is not parseable (short of
what? 70,905 − 22,275 = 48,630 > 35,570). **Resolving change:** "larger than the set itself".

**A-20 · MINOR · line 400.** "no bound of D10 other than g ≤ q names coordinates from both" — q ≤ k
also names q; both bounds at q become one-sided once q is fixed. **Resolving change:** "other than
the two bounds at q, each of which is a bound on one side once q is fixed".

**A-21 · MINOR · SOURCES.md.** The source grades Λ₉ and Λ₁₀ "exact" and Λ₁₃ "envelope"
(§12.11.0.10); Corollary 1 grades the ninth an envelope and the thirteenth exact. The departure is
the paper's reading and may be the better one for the ninth, but it is not recorded. **Resolving
change:** a line under "Interpretations chosen", and after A-1 the thirteenth agrees with the source.

**A-22 · MINOR · `check.py` 632–639.** The axis-10 exact fibre (`new_at`) tests that a term of spin
2S′ is new at occupancy v but not that seniority-v terms survive to occupancy g (v ≤ 4f + 2 − g). At
D11 the omission cannot bite (f ≤ 1, g ≤ 3), so 1,132 stands; at wider caps it would. **Resolving
change:** add the conjugate ceiling to the test and say the fibre is "the seniorities of the terms of
fᵍ carrying spin 2S′".

**A-23 · MINOR · line 5.** Dated 21 September; SOURCES.md says finished 24 September, when the seed
result changed. **Resolving change:** date the paper to its finishing day.

**Typography, in the rendered PDF (BRIEF-AUDIT A.6).** Subscripts and superscripts are Unicode
throughout; no underscore, caret, asterisk or backslash reaches the page; every table fits its
column and no cell is clipped; every figure appears at legible size with its caption. Six defects:

- **A-24 · MINOR · pages 7, 14, 16 (twice), 19.** A stray small-type "Figure n" is printed above
  every bold caption — pandoc's `implicit_figures` renders the image's alt text as a figcaption, so
  each figure carries its label twice. **Resolving change:** empty alt text (`![](figures/…)`) or a
  template rule hiding `figcaption`.
- **A-25 · MINOR · pages 11–13 (Theorems 2, 4, 5).** The clauses "(i) … (ii) …" inside blockquotes
  render as ordered lists numbered "1., 2." — and in Theorem 2, where a display interrupts the list,
  as "1., 2., 1., 2." — while the proofs and line 300 refer to (i)–(iv). A reader of the PDF cannot
  match a clause to its proof. **Resolving change:** write the clauses as plain lines with a hard
  break, or as "(i)" prefixed by a non-list character.
- **A-26 · MINOR · page 13.** The six "stage n:" lines of the §5 edge list collapse into one run-on
  line inside the blockquote. **Resolving change:** two trailing spaces or a blank `>` between lines.
- **A-27 · MINOR · page 22.** "Table 5. The verification record, by object." sits alone at the foot
  of the page with two-thirds of the page blank; the table starts on page 23. A caption orphaned at
  a page foot. **Resolving change:** `page-break-inside: avoid` on caption + table, or move the
  caption below.
- **A-28 · MINOR · pages 16, 19.** Figure 4's labels "165" and "136" print on their markers; Figure
  5's sixth-panel legend prints on the plotted band. **Resolving change:** offset the labels; move
  the legend to the upper left.
- **A-29 · MINOR · pages 5, 8.** The D9 table's "#" column and Prop. 5's "k" column each take a
  third of the text width for a one-character entry. Cosmetic. **Resolving change:** column widths
  in the template, or fewer columns.

---

## Part B — reader audits

### B.1 · A mathematician (lattice theory, order, combinatorial optimisation)

I have not seen this material before. Everything is defined before use except in §6.2, and the
proofs of Lemma 1, Theorem 1, Theorem 3, Theorem 4, Lemma 3 and Theorem 6 are proofs I would accept.
Two things I would not accept, and they are the paper's centre.

**R-1 · BLOCKING · line 342 (Theorem 5(iii)).** The clause asserts an identity that is false:
substituting a constant for one side of the triangle gives { y : |xᵢ − k| ≤ y ≤ xᵢ + k }, whose
lower bound is V-shaped in xᵢ, and (0, k) ∧ (k, 0) = (0, 0) leaves it. The band { |xᵢ − y| ≤ k } is a
different set. Since the whole dichotomy and the title-sentence rest on (iii), this is where an
*Order* referee stops. Change: as A-1 — the constant-side triangle is not a sublattice, the band is
its least monotone envelope, and "carried exactly" becomes "carried as an envelope of arity 1".

**R-2 · BLOCKING · lines 282–300.** Theorem 2 is stated for F : Aⱼ → 𝒫(ℤ) and then applied (line
300, Table 2) to fibres that are functions of several coordinates; under the natural generalisation
the least envelope is not the construction's bound at two of the five axes (1,638 ≠ 1,654; 60,320 ≠
70,905). Either the theorem is generalised and the paper says which member of 𝔈 the construction
uses, or the words "the smallest such extension … is that set's monotone envelope" must not be
attached to D10. Change: as A-2.

**R-3 · MAJOR · lines 166–180, 390.** E(Λₛ) = 0 has a two-line proof from the shape of the bounds
(A-4), and the paper instead sweeps 47 million cells and then tells me the property is "not
guaranteed" at treewidth 2. A referee reads that as the author not knowing why the result holds.
Change: as A-4.

**R-4 · MAJOR · lines 452–460.** Proposition 14 names eight objects that do not exist in the paper
and proves that a bipartite sign assignment is balanced. Delete it or define its objects (A-11).

**R-5 · MINOR · lines 478–492.** Proposition 16 says the generators "are exactly the
join-irreducible elements — the cells with exactly one lower cover", then proves the Birkhoff map
is rank-preserving, then concludes "the covers of Λ₈ are exactly its unit steps". The logical order
is the reverse: first, |{G ≤ x}| = r(x) − 3 for all x shows Λ₈ is graded by r − 3 (a finite
distributive lattice's rank is the number of join-irreducibles below); hence covers are unit steps;
hence "exactly one lower cover" may be tested on unit decrements, which is what the check does.
Change: state the three steps in that order, so the check's `lower_covers` is justified before it
is used.

**R-6 · MINOR · line 556.** "exact in the sense that every branch not pruned by the bound is
visited" — say what the bound is (|chosen| + ⌈|uncovered| / max coverage⌉ ≥ best, and the +1 rule
on a non-empty remainder) so a reader can see it is valid; one sentence.

**R-7 · MAJOR · lines 131, 176.** D12 does not define a monotone function and Prop. 2 uses it as
one (A-8). Change: the running maximum.

What is unmotivated: §8. It is a clean enumeration with no theorem and no reason offered for the
slack being 2; as an EXHAUSTIVE record it is honest, but a referee will ask what it is for.

### B.2 · An atomic physicist (angular-momentum coupling; NIST spectra)

The coordinates and bounds are, taken one at a time, the standard ones: 2S ≤ k for a subshell's
spin (Pauli), Racah seniority with 2S′ ≤ v ≤ g, the triangle rule for K = J₁ + l, and J = K ± ½ for
the last electron — the J₁l (jK) scheme of Racah, in NIST's "J₁l" designation. The term derivation
by microstate counting is right, the p-shell anchors are right, and the particle–hole symmetry is
right. The paper is candid that it measures no spectrum and that closure is a statement about
tuples. Two things are nevertheless said that a spectroscopist will not let pass, and one is used as
a physical reason in the title sentence.

**R-8 · MAJOR · lines 3, 13, 23, 336 (and D10 line 122, Table 2 line 228).** The thirteenth bound,
|2J − 2K| ≤ 1, is the coupling of K with a **single** electron of spin ½. But the ninth coordinate
carries the *target's total spin* 2S′ up to 3 and the seventh puts up to g = 3 electrons in the
target subshell. For g ≥ 2 the last coupling is J = K + S′ (or, properly, the target's own L′S′ term
coupled to the core — the J₁l scheme does not exist for two or more equivalent outer electrons), and
2J then ranges from |2K − 2S′| to 2K + 2S′, not 2K ± 1. So "the 1 is a constant because the outer
electron's spin is one half whatever else the cell holds" (line 336) contradicts the paper's own
2S′ ≤ 3. The tower's last three coordinates are the one-outer-electron jK labels applied *formally*
at every g; the paper should say so, and should not present the constant as physics forced by the
cell. Change: state the assumption in D9/D10 ("2Jₚ, 2K and 2J are the J₁l-coupling labels for one
electron in the target subshell, applied at every g as bookkeeping"), soften "in the order the
physics forces" (line 25), and in the thesis replace "the spin one-half of the outer electron" with
"a constant" or with the scoped statement.

**R-9 · MAJOR · lines 107–109, 114–118.** Which state does 2Jₚ label? The bound 2Jₚ ≤ φ̂(k) is
built from the terms of ℓᵏ, the parent subshell *before* q electrons leave it; but K = J₁ + l is a
coupling in the *final* state, whose core is ℓ^{k−q}. At q = k the core is empty and J₁ = 0, while
the bound admits φ̂(k). Either 2Jₚ is a label of the initial configuration (then K couples an
initial-state J to a final-state l, which is not a coupling scheme) or it is the residual core's J
(then the bound should be φ̂(k − q)). The paper inherits the source's choice and should name it and
its cost. Change: one paragraph in §3 stating that 2Jₚ is the parent term's J and that the K and J
labels are formal couplings of that J to the target's orbital and spin.

**R-10 · MINOR · line 192.** "the vector-coupling rule that makes 2J run from |2L − 2S| to 2L + 2S
… is Wigner's (1931) and Racah's (1942)" — the Clebsch–Gordan triangle rule is not Racah's; Racah
(1942), *Phys. Rev.* **62**, 438 is the algebra of recoupling. The jK scheme itself is Racah, G.
(1942). On a new type of vector coupling in complex spectra. *Physical Review* **61**(7–8), 537, which
the paper should cite for K (it cites the wrong Racah 1942 paper for the coupling at line 192 and in
the Compendium's entry). Change: cite Wigner (1931) alone for the triangle rule and add Racah 1942a
for jK.

**R-11 · MINOR · line 109.** "twice the resultant of the core's momentum with the target's orbital
momentum" — in J₁l coupling the l is the outer electron's, which is the target subshell's f only
when g = 1 (see R-8). Change: "with the orbital angular momentum f of the target subshell, read as a
single outer electron's".

**R-12 · MINOR · line 232.** The two-thirds is parity: 2J must have the opposite parity to 2K, so
one of the three admitted values is never physical, and the K = 0 singleton is the rest. "Inherited
through 2K" is wrong (A-3).

**R-13 · MINOR · lines 225–230.** The row "11 (wider)" calls [0, μ(ℓ, k)] an "exact fibre". It is
not a physical set: p¹ has the single term ²P with 2Jₚ ∈ {1, 3}, and [0, 3] admits 0 and 2, which no
term carries. It is an interval bound whose top is exact. Change: label the row "the interval
[0, μ(ℓ, k)]" and call only the first row exact.

**R-14 · MINOR · line 200.** terms(ℓᵏ) = terms(ℓ^{4ℓ+2−k}) is Condon and Shortley (1935), ch. VII
(the equivalence of a shell and its complement); Racah (1943) is seniority and its
conjugation-preserving form. Change: cite both, in that order.

Does "the tower" claim anything physical beyond bookkeeping? No — and the paper says so at line 44
in words I would sign. The one place it borrows a physical reason is the constant in the thirteenth
bound, and that reason is inconsistent with its own ninth coordinate (R-8). Nothing here bears on a
measured level; the spectra are not touched.

### B.3 · A journal referee

**Novelty and attribution.**

**R-15 · MAJOR · lines 252–276, 324–334, 336; References.** Theorem 1 — a set { (x, y) : x ∈ S,
lo(xⱼ) ≤ y ≤ hi(xⱼ′) } with S a sublattice of ℤᵈ and lo, hi monotone is a sublattice — and Theorem
4(i) are standard results on sublattices of ℝⁿ / ℤⁿ cut out by monotone constraints: Topkis, D. M.
(1978). Minimizing a submodular function on a lattice. *Operations Research* **26**(2), 305–321, and
Topkis, D. M. (1998). *Supermodularity and Complementarity*. Princeton University Press, Princeton
(ch. 2, sublattices of ℝⁿ defined by monotone constraint functions); the same construction underlies
Milgrom, P. and Shannon, C. (1994). Monotone comparative statics. *Econometrica* **62**(1), 157–180.
In the constraint-satisfaction vocabulary the paper already draws on, "join-closed and not
meet-closed" is "max-closed and not min-closed": Jeavons, P. G. and Cooper, M. C. (1995). Tractable
constraints on ordered domains. *Artificial Intelligence* **79**(2), 327–339 — whose main theorem
(max-closed constraints are decided by arc consistency) is exactly the remark the paper wants at line
390 — and Jeavons, P., Cohen, D. and Gyssens, M. (1997). Closure properties of constraints. *Journal
of the ACM* **44**(4), 527–548. The paper may keep its short proofs (the spec allows it) but must
mark Theorems 1 and 4(i) CITED-with-proof and place Theorems 3–4 in the max-closed literature. What
is new here is the application: the envelope theorem in its fibre-wise form (once A-2 is done), the
priced dichotomy on this construction, the constraint-graph, cylinder, chain and seed computations,
and the corrected seed of Λ₉.

**R-16 · MAJOR · lines 13, 31.** The abstract and §0 do not promise what the body delivers: §0 item
2 marks Theorems 2 and 5 MACHINE-CHECKED against Table 5's PROVED (A-5); the abstract's "the two whose
exact physical set is a triangle in two coordinates" is not Corollary 1's count (A-9); and both say
"carried exactly" of an axis whose own Table 2 row shows a 64.4% realised share (A-1). Change: as
A-1, A-5, A-9.

**R-17 · MAJOR · lines 605–613; `check.py` 799–858, 1104–1122.** The verification record is honest
about its numbers and dishonest, unintentionally, about its guards: the fidelity guard does not
evaluate the encodings it certifies (A-6), and the three seed rows are labelled with a status word
whose definition they do not meet (A-7). Both are repairable in a few lines of `check.py`, and both
must be repaired before the phrase "with a non-vacuity guard and an encoding-fidelity guard passed
first" (line 13) is true.

**R-18 · MINOR · References; lines 454, 560.** Missing standard references, with full author lists:
Harary, F. (1953). On the notion of balance of a signed graph. *Michigan Mathematical Journal*
**2**(2), 143–146 (Prop. 14, if it survives); for "the ordinary behaviour of greedy on set cover"
(line 560): Johnson, D. S. (1974). Approximation algorithms for combinatorial problems. *Journal of
Computer and System Sciences* **9**(3), 256–278; Lovász, L. (1975). On the ratio of optimal integral
and fractional covers. *Discrete Mathematics* **13**(4), 383–390; Chvátal, V. (1979). A greedy
heuristic for the set-covering problem. *Mathematics of Operations Research* **4**(3), 233–235; for
sublattices of products of chains and the embedding of a finite distributive lattice in one:
Dilworth, R. P. (1950). A decomposition theorem for partially ordered sets. *Annals of Mathematics*
**51**(1), 161–166; for the jK scheme: Racah, G. (1942). On a new type of vector coupling in complex
spectra. *Physical Review* **61**(7–8), 537. The seventeen references given are correctly cited
(volumes, pages and years verified for Birkhoff 1937, Freuder 1978 and 1982, Dechter and Pearl 1989,
Robertson and Seymour 1986, Karp 1972, Pauli 1925, Racah 1942 and 1943, de Moura and Bjørner 2008).

**R-19 · MINOR · line 367.** A figure that contradicts the text in two rims (A-10) would be returned
by any editor.

**R-20 · MINOR · lines 45–53.** A status table that lists a word never used and omits one used
fourteen times (A-17).

**Correctness and clarity otherwise.** The numbers are right, the proofs of what is proved are
right, the corrected seed at Λ₉ is a genuine finding against the source and is presented as one, and
SOURCES.md is a model of what a provenance file should be. The paper is clearly written where it is
right. Its defects are concentrated in one claim — the thirteenth axis — and in the statement of the
theorem that claim invokes.

---

## Part C — the record

| id | severity | where | finding | disposition |
|---|---|---|---|---|
| A-1 | BLOCKING | 3, 13, 23, 336, 342, 346 | Theorem 5(iii) false as written; the thirteenth axis is an envelope (B₁ = least envelope of the doublet, 64.4%), not "carried exactly"; witness inside the tower |  **FIXED.** Theorem 5(iii) restated: the constant-side triangle {|xᵢ − k| ≤ y ≤ xᵢ + k} is join-closed and not meet-closed (witness (0,k) ∧ (k,0) = (0,0)), and its least envelope is the band Bₖ, of arity 1, strictly larger — proved, join MACHINE-CHECKED with k free, meet a REFUTATION, the envelope EXHAUSTIVE on {0..M} (56 cases). Thesis, abstract, §0 (the opening paragraphs, item 2, a new item 3), the Theorem 4 remark and Corollary 1 rewritten: the thirteenth axis is carried as an envelope, B₁ is the least envelope of the doublet, and the loss is 70,905 = 57,320 (parity) + 13,585 (2K = 0). `check_envelope_family()` builds both exact thirteenth stages (128,225 and 185,545 cells), exhibits the audit's meet witness inside the construction, measures E = 70,905 and 13,585 with ℛ of each equal to Λ₁₃, and verifies the band is Λ₁₃ as a set and the least envelope of the doublet. SOURCES.md records the source sentence no longer carried. |
| A-2 | BLOCKING | 13, 219–230, 282–300, 346 | Theorem 2 stated for one-coordinate F, applied to multi-coordinate fibres; D10's bounds at axes 9 and 12 are not the least envelope (1,638 ≠ 1,654; 60,320 ≠ 70,905); "Table 2 is clause (iv)" false |  **FIXED.** Theorem 2 restated fibre-wise, with two parent indices (j, j′) as in Theorem 1 — F a function of the whole cell, l⋆ over {x : xⱼ ≥ a}, h⋆ over {x : xⱼ′ ≤ b}; proof rewritten; a remark on empty fibres (600 at axis 10, 1,305 at axis 11 strict) says how the theorem is applied there, with l⋆ ≤ h⋆ verified at every cell. Table 2 gains *least* and *empty* columns, pinned: 1,638 / 2,535 / 12,425 / 13,585 / 60,320 / 199,130. The two-index form covers axis 10 directly (2S′ below, g above), so the audit's option (c) was not needed; the construction's bound is the least envelope at 10, 13 and 11 (wider) and not at 9, 12 and 11 (strict), stated in the abstract, §0 item 3, §3.1 and the Theorem 2 remark. "Table 2 is clause (iv)" replaced by what is true (the least column is clause (ii); (iv) is least minus realised); "admit only their monotone envelopes" and "carried as its envelope" rewritten. |
| A-3 | MAJOR | 232 | axis-13 loss misattributed to 2K; it is this axis's parity congruence plus the K = 0 singleton |  **FIXED.** The paragraph now attributes the loss to this axis: the value 2J = 2K at every cell of Λ₁₂, excluded by parity at 57,320 cells and by the constant-side triangle at the 13,585 cells with 2K = 0; both counts pinned. |
| A-4 | MAJOR | 166–180, 250, 390 | E = 0 provable in two lines from the bound shape; §5 remark attributes the guarantee to treewidth |  **FIXED.** Lemma 2 (new, PROVED, one paragraph) after Lemma 1's corollary: ℛ(X) = X for any set cut out by constant bounds and monotone one-coordinate upper or lower bounds; Proposition 2 derives E = 0 from it and keeps the sweep as confirmation. The §5 remark rewritten: Freuder's guarantee is for arbitrary binary constraints on a tree, the construction never used it, exactness comes from the bounds' shape; Jeavons and Cooper (1995) cited for the related max-closed fact. Old Lemmas 2 and 3 renumbered 3 and 4. |
| A-5 | MAJOR | 31 | §0 marks Theorems 2 and 5 MACHINE-CHECKED; the record does not |  **FIXED.** §0 item 2 reads as the audit proposed, extended for Theorem 5(iii)'s join (MACHINE-CHECKED) and meet (REFUTATION); Table 5 agrees. |
| A-6 | MAJOR | 609; check.py 799–858 | fidelity guard never evaluates a Z3 predicate |  **FIXED.** `z3_eval()` substitutes concrete integers and simplifies to a constant; `guard_encoding()` evaluates every Z3 predicate the solver is given (triangle, |a−b| ≤ c, Bₖ, the constant-side triangle, Theorem 1's hypothesis and conclusion) on cap boxes, random pairs, 600 random points and 450 cell pairs from the 150 random instances — 10,176 evaluations, 0 disagreements — and keeps the brute-force references. §10's encoding-fidelity paragraph rewritten to say what the code does. |
| A-7 | MAJOR | 48, 552–558, 611; check.py 1104–1122 | seed MACHINE-CHECKED rows lack the two defining guards |  **FIXED.** `check_seed()` runs, per stage, a non-vacuity GUARD (the clauses satisfiable with `want` signatures; the model read back and verified as a cover) and an encoding-fidelity GUARD (the clause set evaluated at concrete assignments against the direct cover test on the carried minimum, each one-member deletion and 40 random subsets, with at least one deletion answered "no"); the MACHINE-CHECKED row is gated on both. §0's definition is now true of every MACHINE-CHECKED row; §9 and §10 name the guards. |
| A-8 | MAJOR | 131, 176 | φ̂ not monotone by definition; Prop. 2 says it is |  **FIXED.** D12 defines φ̂(k) := max{μ(ℓ, k′) : ℓ ≤ ℓₘₐₓ, k′ ≤ k}, the running maximum; the check pins it against the instrument's table. |
| A-9 | MAJOR | 13, 346 | abstract vs Corollary 1: how many triangles, "three bounds" then four named |  **FIXED.** One count, stated once in Corollary 1 and echoed in the abstract and §0: five adjoined coordinates, every one carried as an envelope; the ninth and eleventh with non-monotone ceilings (and the ninth a parity class), the tenth seniority's non-interval, the twelfth a triangle of arity 2 with a congruence, the thirteenth a triangle with one side constant plus a congruence. |
| A-10 | MAJOR | 367; figures.py 75 | Figure 2 rims contradict Corollary 1 at 2S′ and 2J |  **FIXED.** `figures.py` rims the five adjoined coordinates and the legend reads "first-stage coordinate" / "adjoined coordinate, an envelope"; the caption states the criterion; the legend moved clear of the e–f edge; new md5 in FIGURES.tsv. |
| A-11 | MAJOR | 452–460, 86 | §6.2: eight undefined quantities, trivial proposition, Harary uncited, r reused |  **FIXED, by cutting.** §6.2, Proposition 14 and the 8,018 / 0 row deleted; the obligation removed from `check.py` (it tested a signed K₈ on eight labels and no object of the paper); D7's r no longer collides. Harary 1953 not added, since nothing now cites it. SOURCES.md records the source claim not carried. |
| A-12 | MINOR | 276, 578; check.py 732 | Theorem 1's Z3 form is j = j′; reduction unstated |  **FIXED.** `counting_axis_formula()` carries u₁, u₂ for the upper bound's parent (10 free variables); the non-vacuity guard demands x₁ < x₂ and u₁ > u₂ with both bounds strictly monotone; Theorem 1's status line and Table 5 say so. |
| A-13 | MINOR | check.py 908–913 | obligations for Theorem 3 labelled "Theorem 5(i)/(ii)" |  **FIXED.** Both obligations renamed to Theorem 3. |
| A-14 | MINOR | 384 | "twelve" within-block bounds; eleven |  **FIXED.** "eleven … six inside P and five inside T — and the remaining two name q". |
| A-15 | MINOR | 504 | "20!" should be "17!" |  **FIXED.** 17!. |
| A-16 | MINOR | 205, 428, 444; check.py 320, 362 | ⟨q⟩ middle four, Prop. 13's two failure counts, μ(0,·) not asserted |  **FIXED.** All pinned: the six ⟨q⟩ values; 248,076,675 pairs, 52,767,450 failing meets, 28,742,850 failing joins; μ(0, 1) = 1, μ(0, 2) = 0. |
| A-17 | MINOR | 45–53, 572–604 | SAMPLED unused; GUARD used and unlisted |  **FIXED.** SAMPLED dropped (five words); GUARD explained beneath the table as a soundness check on the checker, never the status of a result. |
| A-18 | MINOR | 592; SOURCES.md | "independent derivation" is a hand-typed edge list |  **FIXED.** "independent transcription" in the `EDGES` comment, Table 5 and SOURCES.md. |
| A-19 | MINOR | 444 | "larger than the set is short" unparseable |  **FIXED.** "larger than the set itself". |
| A-20 | MINOR | 400 | Prop. 10 proof: q ≤ k also names q |  **FIXED.** "other than the two bounds at q — q ≤ k and g ≤ q … each a bound on one side alone once q is fixed". |
| A-21 | MINOR | SOURCES.md | departure from the source's exact/envelope grading of Λ₉, Λ₁₀, Λ₁₃ unrecorded |  **FIXED.** SOURCES.md, "Interpretations chosen" 7 and "What the repair changed" 3: the source's "exact" at Λ₉, Λ₁₀ is E = 0 (Proposition 2 here); the paper grades by the exact physical set, all five adjoined axes envelopes, the thirteenth agreeing with the source. |
| A-22 | MINOR | check.py 632–639 | axis-10 exact fibre omits the conjugate ceiling; harmless at D11 |  **FIXED.** `senior_set()` adds v ≤ 4f + 2 − g; 1,132 unchanged; Table 2 names the fibre as "the seniorities v ≡ g (mod 2), v ≤ 4f + 2 − g, at which a term of spin 2S′ is new in fᵛ". |
| A-23 | MINOR | 5 | date 21 September; finished 24 September |  **FIXED.** 24 September 2026. |
| A-24 | MINOR | pp. 7, 14, 16, 16, 19 | stray "Figure n" alt-text label above each caption |  **FIXED.** Empty alt text, the caption in the image's own paragraph; no stray label on any page of the re-render. |
| A-25 | MINOR | pp. 11–13 | Theorem 2/4/5 clauses render as "1., 2., 1., 2." against (i)–(iv) in the proofs |  **FIXED.** Clause labels written **(i)**–**(iv)** as separate blockquote paragraphs in Theorems 2, 4 and 5, and the proof paragraphs that open with a label likewise; the page shows (i)–(iv), never 1.–4. |
| A-26 | MINOR | p. 13 | §5 edge list collapses to one run-on line |  **FIXED.** The edge list is a two-column table. |
| A-27 | MINOR | p. 22 | "Table 5." caption orphaned at a page foot, table on p. 23 |  **FIXED.** In the re-render (30 pages) Table 5's caption sits at the foot of p. 24 directly above the table's header and its first row, and the table continues on p. 25 with the header repeated; no caption is orphaned (verified on the rasterised pages). |
| A-28 | MINOR | pp. 16, 19 | Figure 4 labels on markers; Figure 5 legend on the band |  **FIXED.** Figure 4's first-stage labels offset from the markers and the dotted line; Figure 5's sixth-panel legend given headroom above the band; both regenerated, new md5s. |
| A-29 | MINOR | pp. 5, 8 | one-character columns a third of the width |  **FIXED.** Relative column widths set by the separator's dash counts in the D9 table, Proposition 5's table and Table 2; the one-character columns are narrow and "10"–"13" no longer wrap. |
| R-1 | BLOCKING | 342 | (mathematician) Theorem 5(iii)'s identity is false — same repair as A-1 |  **FIXED** — as A-1. |
| R-2 | BLOCKING | 282–300 | (mathematician) Theorem 2's scope and "least" — same repair as A-2 |  **FIXED** — as A-2. |
| R-3 | MAJOR | 166–180, 390 | (mathematician) E = 0 unproved though provable — same repair as A-4 |  **FIXED** — as A-4. |
| R-4 | MAJOR | 452–460 | (mathematician) Prop. 14's undefined objects — same repair as A-11 |  **FIXED** — as A-11. |
| R-5 | MINOR | 478–492 | (mathematician) Prop. 16's argument stated in the wrong order |  **FIXED.** Proposition 16 restated in the order asked: G(i, v) a cell; the generators exactly the join-irreducibles, PROVED both ways; the count and |{G ≤ x}| = r(x) − 3 EXHAUSTIVE; the grading r − 3 from the cited rank fact; hence covers are unit steps; hence lower covers may be found by unit decrements, which the check does — and the one-lower-cover test is then a second verification. |
| R-6 | MINOR | 556 | (mathematician) state the branch-and-bound's bound |  **FIXED.** The bound stated: c + ⌈m / M⌉ ≥ best, and c + 1 ≥ best on a non-empty remainder. |
| R-7 | MAJOR | 131, 176 | (mathematician) φ̂'s definition — same repair as A-8 |  **FIXED** — as A-8. |
| R-8 | MAJOR | 3, 13, 23, 25, 122, 228, 336 | (physicist) spin-½ constant contradicts 2S′ ≤ 3, g ≤ 3; jK is a one-electron scheme; state the scope |  **FIXED.** A paragraph in §3 states that 2K and 2J are the J₁l labels of Racah (1942a) for one outer electron, applied at every g ≤ 3 as bookkeeping, and that the constant 1 is a convention of the labelling, not a consequence of 2S′ ≤ 3; D9 rows 12–13 and D10 point to it; §0 reads "in the order in which a spectroscopic designation lists them"; the thesis no longer names the spin; "What is not established" scopes it. |
| R-9 | MAJOR | 107–109, 114–118 | (physicist) which state 2Jₚ labels (ℓᵏ before the transfer vs the residual core ℓ^{k−q}) |  **FIXED.** The same paragraph: 2Jₚ is bounded by the terms of ℓᵏ before the transfer, not the residual core (at q = k the core is empty while the bound admits φ̂(k)); the residual-core reading would give the bound two parents and is named, not priced. D9 row 11 says "as it stands before the transfer". |
| R-10 | MINOR | 192; References | (physicist) triangle rule is not Racah's; cite Racah 1942, Phys. Rev. 61, 537 for jK |  **FIXED.** Wigner (1931) alone for the triangle rule; Racah (1942a), Phys. Rev. 61, 537, cited for J₁l; Racah (1942b) kept for the classification of terms. Only the first page of 1942a is printed: the APS page is behind the egress proxy and the end page could not be verified. |
| R-11 | MINOR | 109 | (physicist) "target's orbital momentum" is the outer electron's l only at g = 1 |  **FIXED.** D9 row 12: "the orbital angular momentum f of the target subshell, read as a single outer electron's". |
| R-12 | MINOR | 232 | (physicist) the ⅔ is parity — same repair as A-3 |  **FIXED** — as A-3. |
| R-13 | MINOR | 225–230 | (physicist) row "11 (wider)" is an interval bound, not an exact fibre |  **FIXED.** The row reads "the interval [0, μ(ℓ, k)] … an interval whose top is exact, not a set of physical values", with the ²P example in the text; only the first row is called exact. |
| R-14 | MINOR | 200 | (physicist) particle–hole equivalence is Condon and Shortley ch. VII first |  **FIXED.** Condon and Shortley (1935), ch. VII, then Racah (1943) in the seniority-preserving form. |
| R-15 | MAJOR | 252–276, 324–336; References | (referee) Theorems 1, 4(i) are Topkis 1978/1998 (Milgrom–Shannon 1994); Theorems 3–4 are max-closed constraints, Jeavons–Cooper 1995, Jeavons–Cohen–Gyssens 1997 |  **FIXED.** Topkis (1978; 1998, ch. 2) and Milgrom and Shannon (1994) cited before Theorem 1, Theorems 1 and 4(i) marked CITED with proof; Jeavons and Cooper (1995) and Jeavons, Cohen and Gyssens (1997) cited at Theorem 3's remark (max-closed, not min-closed) and in §5. Every reference verified by web search on 2026-09-24 (SOURCES.md item 7). |
| R-16 | MAJOR | 13, 31 | (referee) abstract/§0 promise vs delivery — same repairs as A-1, A-5, A-9 |  **FIXED** — as A-1, A-5, A-9. |
| R-17 | MAJOR | 605–613; check.py | (referee) the guards the record claims are not the guards run — same repairs as A-6, A-7 |  **FIXED** — as A-6, A-7. |
| R-18 | MINOR | References; 454, 560 | (referee) missing: Harary 1953; Johnson 1974, Lovász 1975, Chvátal 1979; Dilworth 1950; Racah 1942 (Phys. Rev. 61, 537) |  **FIXED.** Johnson (1974), Lovász (1975), Chvátal (1979) at the greedy sentence; Dilworth (1950) at Lemma 3; Racah (1942a) at §3. Harary (1953) omitted because §6.2 was cut (A-11). |
| R-19 | MINOR | 367 | (referee) figure contradicts text — same repair as A-10 |  **FIXED** — as A-10. |
| R-20 | MINOR | 45–53 | (referee) status table — same repair as A-17 |  **FIXED** — as A-17. |

**Counts.** 49 rows: **4 BLOCKING** (2 distinct issues, A-1/R-1 and A-2/R-2), **17 MAJOR** (12
distinct: A-3 to A-11, R-8, R-9, R-15), **28 MINOR** (24 distinct). Unique issues: 38.

**What is not a finding.** Theorem 7's two reductions are exact and the guards establish the
equivalence (A.3). D13 and Lemma 3 agree with the closure-law paper's D8 and Theorem 13 in every
clause, including which box ℛ(G) is computed in. seed(Λ₉) = 8 against the source's 9 is a correct
correction of the source, recorded correctly in SOURCES.md. The constraint graph's 13 edges and
cycle rank (0,0,1,1,1,1) are the one-parent reading the source itself defines, and the source's 14 /
(0,0,1,1,2,2) is stated as the counterfactual it is. The maximal-chain count is right and its
recursion is well-founded. The bracket system is right. All 122 obligations pass, the selftest's
five controls are refuted, and lint is clean.


---

## Repair record — 2026-09-24

Repaired by the drafter against every finding above; no finding was deleted or rewritten. **Dispositions: 49 FIXED, 0 DECLINED** (BLOCKING 4/4, MAJOR 17/17, MINOR 28/28); every R row that restates an A row carries that row's disposition.

**What the thesis now says.** The thirteenth axis is carried as a monotone envelope, like the four before it. Theorem 5(iii) is corrected: substituting a constant for one side of the triangle gives {|xᵢ − k| ≤ y ≤ xᵢ + k}, which is not meet-closed ((0,k) ∧ (k,0) = (0,0)); its least envelope in Theorem 2's sense is the band Bₖ, a sublattice of arity 1 (Theorem 4(i)), strictly larger. In the tower, D10's |2J − 2K| ≤ 1 is that least envelope of the exact doublet 2J = 2K ± 1, reproducing 199,130 as a set; the 70,905 cells it admits and the doublet does not are one value (2J = 2K) per cell of Λ₁₂ — 57,320 by parity, 13,585 at 2K = 0 — and the realised share is 64.4 per cent, as Table 2, the source's own grading and Figure 2 said. Theorem 2 is stated fibre-wise with two parent indices; the construction's bound is a member of its envelope family at every axis and the least member at axes 10, 13 and 11 (wider reading) only — at axes 9 and 12 the least envelopes admit 1,638 and 60,320 against 1,654 and 70,905, at axis 11 (strict) 12,425 against 13,585 — every figure pinned. E = 0 is proved from the shape of the bounds (Lemma 2). The coupling scheme (J₁l, one outer electron, applied at every g as bookkeeping) is named and scoped, and every attribution the referee asked for is cited and was verified from the tree or by search.

**What changed.** `PAPER.md`: thesis, abstract, §0, D9, D10, D12, §3 (the scheme paragraph, Table 2 with *least* and *empty* columns, the thirteenth-row paragraph), §4 (Lemma 2 new, Theorem 1 attribution and two-index check, Theorem 2 fibre-wise, Theorem 3's max-closed remark, Theorem 5 and Corollary 1 rewritten), §5 (edge table, Proposition 8's count, the treewidth remark), §6 (Proposition 10's proof, Proposition 13's wording, §6.2 cut), §7 (Lemma 3 with Dilworth, Proposition 16 reordered and proved, 17!), §9 (Lemma 4, the bound, the guards, the greedy attribution), §10 (Table 5 and the guard paragraphs), References (ten added, Racah split into 1942a/b); date 24 September 2026; typography (empty alt text, bold clause labels, the edge table, column widths). `check.py` (never weakened; one obligation removed with its cut proposition, none relaxed): `check_envelope_family()`, `cst_formulas()`, `z3_eval()`, `py_counting_axis()`, `senior_set()`, the two-index Theorem 1, the predicate-evaluating fidelity guard, the seed guards, the renamed Theorem 3 rows, the pins of A-16 and A-8, a sixth negative control. `figures.py`: Figure 2's rims and legend, Figure 4's labels, Figure 5's legend. `FIGURES.tsv`: three new md5s. `SOURCES.md`: "What the repair changed" (nine items) and "Changes made in the repair pass" (items 12–22), two new interpretations.

**Re-verification** (PATH = `method/bin`, Python 3.12, Z3 5.1.0). `python3 check.py`: **EXHAUSTIVE 115, GUARD 14, MACHINE-CHECKED 9, REFUTATION 10  — total 148, 0 failures**, 390 s, exit 0. `python3 check.py --selftest`: GUARD 2, REFUTATION 5  — total 7, 0 failures, the six negative controls all refuted, exit 0. `python3 papers/method/lint.py papers/method/05-tower`: 0 hits. `python3 papers/method/render.py papers/method/05-tower`: **30 pages**. Every page rasterised (pymupdf, 80 dpi) and read as an image; the PDF's extracted text (pypdf) scanned: 30 pages; underscores 0, carets 0, backslashes 0, asterisks 0 in the extracted text. The HTML screenshotted with headless Chromium per BRIEF-AUDIT step 6 and read.
