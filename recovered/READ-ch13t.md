# READ-ch13t.md — Phase R2 section read, chat 87 — **Chapter 18 whole, main L4922–L5380**

Instruments: `r2-ch13t.py` (computable, 81 s, golden `904428e4`) and `r2-ch13u.py` (prose, 1 s,
golden `f75dc951`). Both banked. Measured from the members; no volume changed.

## Boundary, MEASURED by heading scan

Chapter 18 runs **L4922–L5380**; **Chapter 19 opens L5381**. Sixteen sections, not the eight
HANDOFF-39 listed: §18.1 L4931, §18.1.1 L4937, §18.1.2 L4959, §18.1.3 L4964, §18.2 L4970,
§18.3 L4976, §18.4 L4980, §18.4.1 L4999, **§18.4.2 L5248, §18.5 L5294, §18.6 L5303, §18.6.1 L5313,
§18.6.2 L5341, §18.6.3 L5352, §18.6.4 L5368, §18.7 L5375**. Every one verified in the file.
Fourth consecutive handoff to under-measure a chapter's extent (after L4157, L4477, L4899).

## The claim census

**Computable (18).** Theorem 18.1's componentwise join/meet (L4932); Theorem 18.2's σ-algebra
containment (L4940); 28 of 511 non-componentwise joins (L4948); dimension-indifference at Λ₁₁
(L4960); ν's 86 violations (L4971); the six-cell counterexample (L4985–4988); "one in five"
(L4990); the certificate table (L5022–5027); 12! and the 365-cell check (L5030–5031); the E table
(L5052–5062); the six cap forms (L5102–5108); the provenance table (L5128–5130); the fibre table
(L5164–5169); K3 and K4 widths (L5183, L5200); the cavity pair counts (L5242); the concave/Cesàro
table (L5259–5263); the min/max proposition (L5268–5272); the prediction-budget table (L5315–5321).

**Prose (14).** Twenty-one section and chapter pointers; twenty register citations; the theorems
§18.1.3 names (L4965); the conserving poset's definition site (L4947); ν's two printed definitions;
the chapter's own running count of its negatives (L4923, L5304, L5373); the Brylawski, Freuder,
Dechter and Baker–Pixley attributions; §16.7.1's two verdicts against Chapter 18's third (L5331);
§18.4 against §15.3 and A.8 (13l-05); the back-matter Index term count (L5192); the "of §16.4 form"
class (13o-01); the asteroid-belt and subnet figures; §7.1's two citations.

---

## A — deviations

**13t-01 — §18.1.3 disclaims two theorems that do not exist.** L4964–4965, the section headed
*What the theorem does not establish*, opens: *"Theorems 11.1 and 11.2 bound information, not
estimation."* MEASURED across all six volumes: **`Theorem 11.1` and `Theorem 11.2` occur zero
times**. The theorems argued in the section above it are **18.1** (L4932) and **18.2** (L4940),
and §18.6.2 L5344 cites 18.2 by that number correctly, as do L1980, L7321, L10637–L10640 and
ioi L367. The disclaimer is sound; the numbers attached to it are of no theorem in the work.
The 13p-04 class (a figure left stale by a renumbering) applied to a theorem label.

**13t-02 — the audits row prints two different E ten lines apart.** L5025 (the certificate table):
*"the audits, four coordinates  **16**  drop DEPTH, the fourth coordinate  **0**"*. L5062 (the E
table): *"the audits, four coordinates  **17**  fourteen cells with no audit in them"*. Same object,
same chapter, same subsection, no reconciling sentence. Register 275 (reg L1055) records
*E(audits) = 0 was true and weak* and the fourth coordinate DEPTH, but does not carry either
figure. One of the two must move. The 13p-10 / 13r-01 class — a section contradicting its own
adjacent table.

**13t-03 — the provenance table classifies eight objects where the sentence above it says ten.**
L5126: *"Tested against all ten indexed objects it half held."* The table at L5129–5130 classifies
**3 + 5 = 8**. MEASURED: the E table at L5053–L5062 does list exactly **ten** rows, so *ten* is the
population and two of its objects are unaccounted for in the classification. The 13j-11 / 13p-03 /
13p-09 class — a running self-count printed two ways.

**13t-04 — §18.2's "86 violations" does not reproduce under any reading tested.** L4971 and
Appendix A.11 L10020 both print *86 violations at the caps tested* for ν. MEASURED over **fifteen
readings** — three definitions (ν = e − δ with §17.3's δ = f − ℓ; ν = n − δ per L6422; δ alone) ×
five counts (comparable cell pairs, covering pairs, unit steps, join-homomorphism failures, and the
projection reduction over realised value tuples) — at **three cap settings** (976, 1,636, 2,394
cells). No cell yields 86. At Λ₈: comparable 9,894 / 15,450 / 31,185; covering and unit-step
384 / 384 / 240; join-homomorphism 131,328 / 152,160 / 166,464; projection 4 / 5 / 2. The claim
that ν is non-monotone is **true under every reading**; the figure attached to it is not
reproducible as printed. The 13g-01 / 13h-04 / 13j-01 / 13l-01 / 13n-01 / 13p-02 / 13r-03 class,
compounded by 13t-05.

**13t-05 — ν has two printed definitions and they are different functions.** MEASURED:
**ν = e − δ** at main L4849, L4971 and A.11 L10016; **ν = n − δ** at main L6422 (*"ν = n − δ is
nearly linear in n, and p = 1 is the pole"*, which §18.5 L5295 depends on). δ itself is defined
as **f − ℓ** at §17.3 L4819/L4825 and reg L1637, while §18.6.3 L5362 calls δ *"the value's
departure from what the index determines"* — a value, not a coordinate function. Under the first
reading ν is a lattice function and measurable; under the second it is not a function of the
coordinates at all, and *violations in the cell order* has no referent. The defining term is
unstated at every site — the 13j-07 / 13l-06 / 13n-02 / 13o-03 / 13p-11 / 13r-08 / 13r-09 class.

**13t-06 — the conserving poset is named, used and never defined.** L4947–4950 carries the
chapter's only non-componentwise witness: *"The conserving poset of §18.1.1 has 28 of its 511 joins
differing from componentwise maximum."* MEASURED: **`conserving poset` occurs at exactly two sites
in the six volumes, L4947 and L4955, both inside §18.1.1 itself.** The pointer sends the reader to
the section they are reading, and the object — its cells, its coordinates, its constraints — is
given nowhere. 28 and 511 are therefore unverifiable by any reader and were not re-measurable here.
(511 is *not* impossible: a poset need not have all joins, so it may be a sub-count of C(33,2) = 528
or similar. No impossibility is claimed — C9 discipline.)

**13t-07 — L4990's "one in five" measures 0.2991.** MEASURED exhaustively over every subset of the
2³ cube: **117** subsets pass every proper-projection test and **35** of them fail closure —
**0.2991**, nearer three in ten than one in five. At d = 4, c = 2 over 20,000 seeded samples the
ratio is **0.4566**, so the figure does not become one in five at greater width either. The
qualifier *roughly* absorbs some of this; the population it is roughly one-fifth of is not stated.

**13t-08 — §18.4.1 cites §7.1 twice for claims §7.1 does not carry, and §7.2 does.** L5150:
*"a tree — Λ's own shape, which §7.1 says three central results follow from."* MEASURED:
**`three central results` occurs once in the main volume, at L5150 itself**; §7.1 (L1750–L1763)
is the seven-row constraint table and its closing line is *"Seven constraints, four origins, and
nothing else."* L5244: *"§7.1 had said so without saying what it bought"*, of every bound being
single-argument — MEASURED, that statement is **§7.2 L1764–1766**: *"Each constraint reads
xᵢ ≤ φ(xⱼ) — one coordinate bounded by a monotone function of one other."* Both pointers are one
section short. The 13d-01 / 13l-03 / 13o-01 / 13p-06 / 13r-05 class, with the correct target named.

**13t-09 — L4923 declares every result of the chapter negative and §18.6.1 prints one that is not.**
L4923: *"The results of this chapter are the strongest in the book, and every one of them is
negative."* L5321–5323: the bibliography row of the prediction-budget table reads *"**6 | 6 | all
occupiable — two already named**"*, and the text calls it *"the only place in this book where a
prediction is both available and true."* A positive result inside a chapter whose opening sentence
forecloses one. Either the opening sentence takes an exception clause or the fifth row belongs
elsewhere.

**13t-10 — the chapter's count of its own negatives is printed two ways.** L5304 (§18.6): *"The
**five** limitations above."* MEASURED, the sections above §18.6 are §18.1, §18.2, §18.3, §18.4 and
§18.5 — five, and the count is exact. L5373 (§18.6.4): *"This is the **fifth** and largest of the
negatives"* — of §18.6 itself, which is the sixth thing counted. The two lines cannot both hold.
The 13j-11 / 13p-03 / 13p-09 class again, and the second instance in this chapter after 13t-03.

**13t-11 — the back-matter Index prints two of its rows twice.** MEASURED at L11409 onward: **59
entry rows** carrying the entry separator, **57 distinct term names**. The duplicated rows are
***interiority*** (plain at L11429, italicised at L11432) and ***index, self-referencing***. The
Index's own extent line L11419 — *"57 terms, 311 entries, 44 specialisation relations, 0
violations — E(index) = 0"* — is therefore **exact on terms and exact on relations** (44 sub-term
rows measured), and the duplication is a presentational defect that does not disturb its arithmetic.

---

## B — verified

1. **Theorem 18.1 is exact on the tower.** Λ₈, Λ₉ and Λ₁₀ are closed under componentwise max and
   min with **zero leaks** on all 952,576 / 2,735,716 / 6,426,225 ordered pairs.
2. **L4960's dimension-indifference holds at Λ₁₁.** Λ₁₁'s 13,585 cells: all **110** φ̂ bounds are
   monotone on their realised values, so the object is closed under both operations — established
   by chat 86's projection reduction and controlled against Λ₁₀, where the reduction and the direct
   measure agree. (The first draft used a 2,000-cell prefix of Λ₁₁ as a control; a prefix of a
   lattice is not a sublattice, so that control was ill-posed by construction and was replaced
   before banking, not after seeing its result.)
3. **The six-cell counterexample is exact.** All six proper projections of
   S = {(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,1),(1,1,0)} are ℛ-fixed points, and
   (1,0,1) ∨ (1,1,0) = (1,1,1) ∉ S.
4. **The cap table reconstructs 6 of 6 rows exactly** at a box of side 4 with the occupancy
   coordinate 0-based: 0/0, **875**/0, 0/0, 0/**260**, 0/**16**, 0/**400**, and the morphism
   columns follow. No other side or base reproduces more than five.
5. **The fibre table reconstructs 5 of 5 rows exactly** on the **364** non-increasing triples over
   1…12: 21 / 10.71, 6 / 2.53, **1 / 1.00**, 78 / 7.91, 12 / 1.27. Neither the 0-based nor the
   all-ordered reading reproduces it, so the printed reading is determined.
6. **The concave/Cesàro table reconstructs 5 of 5 rows exactly.** Cells are the partial-sum vectors
   of ordered non-increasing mass vectors, i.e. partitions of s ≤ N into at most n parts:
   (3,12) 102/142/40, (3,16) 204/294/90, (3,20) 358/526/168, (4,12) 155/341/186, (5,12) 197/712/515;
   envelope join/meet failures **0/0** at every cap; exact joins 224 / 896 / 2,772 / 1,073 / 2,491;
   **exact meets 0 at every cap**.
7. **The proposition is exact.** Over the 5,151 pairs of the (3,12) exact set, componentwise minimum
   leaves concavity intact **0 failures**, componentwise maximum breaks it **224** times.
8. **K3 has induced width 2 and K4 induced width 3**, by elimination over all orderings — L5183's
   *treewidth 2, not a tree* and L5200's *four nodes, six edges, complete, width 3*.
9. **The printed constants check.** 12! = **479,001,600** exactly; 5,184 = 4!·3!·3!·3!, consistent
   with the bibliography's four coordinates; **15,400 = C(176,2)** and **114,960 = C(480,2)**, so
   L5242's pair counts follow the volume's own C(N, 2) convention (13r-01); 36 = 1 + 35 kin and
   7 = 1 + 6.
10. **Nineteen of twenty-one pointers resolve to the claim**, not merely the heading — §12.11.2's
    coupling computation, §2.18 on decisions, §3.7's certificate-versus-search, §16.7.1's
    removability question, §6.2's drip lines, §6.3's relabelling, §12.11.3.1's provenance rule,
    §2.18.1's two-parent decisions, §17.4's repair, Chapter 23's pole, Chapter 30's cost,
    Chapter 19's literature, §22's brackets, §25.6's Sc VI cell, §29.1's search. The two that fail
    are 13t-08's pair.
11. **All twenty register citations resolve**, and each entry's subject matches the sentence citing
    it: 412 (the law promoted), 298 (§6.2's nuclide row), 275 (E(audits) and the two levers), 306
    (the cap-arity criterion false in one direction), 326 (the law–extent rule declined), 317 (the
    inverse three-body filter), 406 (a fourth node, width 3), 316 (K_n through §18.4.1), 299 (a
    second named law), 302 (order- and identity-realisation), 303 (the occupancy criterion), 325
    (three tiers), 224 (the central theorem's precedent), 355 (the n-body space found in print).
12. **Every named attribution in the chapter is carried elsewhere in the work**: Brylawski (main,
    reg), Freuder and Dechter (main, mc, reg, ioi), Baker–Pixley (main, mc, pc, reg), Jacobi, Hill
    and KAM (main, mc, pc, reg, ioi). Maxwell and Ampère appear **only** in this chapter (2 and 1
    sites), which is not a defect but is the chapter's only uncorroborated pair.
13. **13p-04 reaches its second site as measured.** L5192's *fifty-one author-chosen terms* is the
    site chat 85 already recorded against L4523; the Index's extent line reads 57 and names the six
    terms Chapters 35–36 added. Confirmed, not re-opened.
14. **13l-05 confirmed from the file.** §15.3 L4302 and A.8 L9969–9970 state the d = 2 criterion in
    the vocabulary of *may precede*, *total order* and *relabelling*; **none of those four phrases
    occurs anywhere in §18.4** (L4980–L4998). The promised development is absent, as chat 83
    measured.

---

## C — incidental

1. **L5011's `§4.6` is UNRESOLVED at a third site** (after 13r's C1 and its predecessor). Chapter 4's
   protocol rows take no headings; R3 decides the class once, and this is not counted a defect here.
2. **§16.7.1 contains neither of the two phrases Chapter 18 attributes to it verbatim** — *fact
   about the world* (L5039, L5331) and *mechanism* (L5040) are absent from L4578's span, though
   *artefact*, *removable*, *irreducible* and *asteroid* are all present. The sense is carried; the
   wording is Chapter 18's, and both sites read as quotation.
3. **The asteroid belt's 2 → 1** (L5336) sits against §16.7.1's own belt lines at L4597, L4599 and
   L4609; the figures were not compared here because the belt catalogue is still not in r2lib.
4. **The subnet with a hole, E = 8** (L5319) has two other sites, main L1609 and L7255; not compared.
5. **The certificate table and the E table disagree on nothing but the audits row** — calendar 7,
   periodic table 36, nuclide 9 and bibliography 6 each agree across all three tables in the
   chapter (L5023–5027, L5052–5062, L5315–5321).
6. **Maxwell's slack argument (L5078–5094) is the chapter's one physics claim with no register
   citation**, and the conjecture it states is explicitly two points; noted, not counted.
7. **The periodic-table, Janet, audit and bibliography catalogues are still not in r2lib**, so the
   certificate and E tables were checked for arithmetic and cross-site agreement only. Adding them
   is owed before Chapter 6 or 19, as chats 85 and 86 also recorded.
8. **L5148–5158 and L5180–5224 are §18.4.1's three-body and four-node material**, which DEFERRED
   carries under 12i-01/02 at L5150; the pointer defect there is 13t-08 and the rest reads sound.
