# READ-ch14b.md — Chapter 21, second part (main L5690–L5873)

Chat 91, Phase R2, under the chat-81 cadence. Range **L5690–L5873, 184 lines, five headings**:
§21.5.1 L5690, §21.5.2 L5708, §21.5.3 L5761, §21.5.4 L5797, §21.5.5 L5835. Boundaries MEASURED by
heading scan before a line was read; §21.6 L5874 onward is chat 92's and was not opened. Instruments:
`r2-ch14b` (computable, golden 13,082 B · 9325315c · 175 lines) and `r2-ch14c` (prose, golden
10,950 B · 565b59cc · 132 lines). No correction made, no Register entry written — the chat-67 hold
stands.

---

## A — deviations

### 14b-01 · L5785 · "the largest orientation cost anywhere in this book" is refuted twice, once by the same chapter

Printed (L5784–L5786): *"**ℛ₄ cuts the defect from fifteen to four — the largest orientation cost
anywhere in this book, and the first object on which the second operator is the only one that
works.**"* The orientation cost there is 15 − 4 = **11** (arithmetic OK).

MEASURED, every site in the six volumes printing a value labelled an orientation cost:

| site | value |
|---|---|
| main L5781 | 11 (this object) |
| main L5843 | **15** — §21.5.5, 58 lines later |
| mc L462 | 0 on eight of ten indexed objects, 2 on the audits, **750 on the parity rule** |
| mc L870 | 15 |
| reg L1773 | 750 |
| reg L1985 | 15 |

Two distinct values exceed 11, and the larger of them by a factor of 68. The nearer refutation is
inside the same section run. The second half of the sentence — *the first object on which the second
operator is the only one that works* — is not contradicted by anything measured here.

### 14b-02 / 14b-03 · L5813–L5814 and L5818–L5819 · the star's withdrawn seed of seven survives in two sentences

The table at L5804 prints the star's seed as **6**. Two sentences below it still print 7:

- L5813–L5814: *"**Both extremes cost more.** The balanced trees all seed at six; the path and the
  star at eight and seven."*
- L5818–L5819: *"Diameter runs 5, 2, 3, 4, 3, 2 against seeds 8, 7, 6, 6, 6, 5"* — the star's slot
  is the second, and it reads 7.

MEASURED. All six graphs were rebuilt on six nodes over three values per node (alphabet 18, as L5823
states), every orientation enumerated, and the cell counts reproduce the printed column exactly —
path 28, star 276, caterpillar 65, binary tree 100, double star 127, forest 196. Exact seeds by
branch and bound on `seed_of()` (cover_model → cover_reduce → exact_seed): **8, 6, 6, 6, 6, 5**,
matching the table column and not the two sentences.

The section's own closing paragraph (L5829–L5831) says the seven was withdrawn: *"This section first
reported the star at seven … It does not fail: **greedy set cover fails there**, and exact search
gives six."* So the table and the closing paragraph agree with the measurement, and two intermediate
sentences were left at the old value. This is the §21.5.4 instance of the class chat 90 recorded for
the seed at L5685: a corrected figure not carried to its downstream restatements.

### 14b-04 · L5747–L5748 · figure 21.1's caption gives k degree 4 at Λ₈; measured 3

Printed: *"The base Λ₈ is a caterpillar with **k** as its hub at degree 4."*

MEASURED from tower-2.py's own generator (gate-verified, md5 c0bce27a) and independently from the
constraint list §21.5.2 prints 32 lines earlier at L5715: Λ₈'s constraint graph has degrees
n 1 · ℓ 2 · **k 3** · q 2 · e 1 · f 2 · g 2 · 2S 1. k's neighbours are ℓ, q and 2S. k reaches degree
4 only at Λ₁₁, when 2J_c ≤ φ̂(k) is added. *Caterpillar* is correct — removing the three leaves leaves
the path ℓ–k–q–g–f.

### 14b-05 · L5745–L5751 and L5765–L5769 · the Λ₁₃ graph figures were withdrawn by Register 1790 and three sites still carry them

Figure 21.1's caption and §21.5.3's table both print **twelve nodes, thirteen edges, girth 5,
radius 3, three leaves, "no triangle at any stage"**, and a degree sequence 4, 3, 3, 3, 2, 2, 2, 2,
2, 1, 1, 1.

**Register 1790 (reg L6603) already withdrew this**, in terms: *"Λ₁₃'S CONSTRAINT GRAPH IS 13 NODES
AND 14 EDGES WITH ONE TRIANGLE, 2S′–g–v, FROM Λ₁₀ ONWARD — NOT THE 12 NODES, 13 EDGES AND 'NO
TRIANGLE AT ANY STAGE' OF §21.5.3 AND FIGURE 21.1 — AND ITS TREEWIDTH IS STILL 2, SO §21.5.1'S
ONE-LEVEL SHORTFALL STANDS."* It cites Registers 249, 507, 508 and 523, and marks §21.5.3 and
figure 21.1 as owed at the prose pass. That is a proper append-only correction and it governs.

MEASURED independently this chat, before that entry was found: a bounded search over six readings of
tower-2.py's axis bounds. The reading in which Λ₁₂'s 2K takes f as a second parent
(2K ≤ 2J_c + 2f, the reading that makes 2K a two-parent axis as §21.5.3 L5788–L5789 requires)
reproduces Register 1790 on **10 of 10 fields**: 13 nodes, 14 edges, cycle rank 2, girth 3,
treewidth 2, diameter 6, radius 4, four leaves, hub degree 4, degree sequence
4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1. The triangle is {g, 2S′, v}, forced by 2S′ ≤ g at Λ₉ together
with 2S′ ≤ v ≤ g at Λ₁₀.

The three sites still printing the withdrawn figures: **main L5745** (caption), **main L5765**
(table), **reg L1953** (Register 523, the entry 1790 corrects; append-only, so it stays and is
corrected by 1790, not edited). Consequence recorded, not repaired: §21.5.2's own claim that Λ has
no 3-body is **true at Λ₈** (measured, zero of thirty-five triples) — it is the caption's extension
of that to *any stage* that 1790 refutes.

### 14b-06 · L5735–L5736 · "each existing edge sitting in exactly one triangle-completing position" is false under every reading

Printed: *"**Seven constraints, seven near-misses** — the edge count of a tree on eight nodes, with
each existing edge sitting in exactly one triangle-completing position Λ declines."*

MEASURED, three readings, all failing:

1. triangles completed per added near-miss → 1, 1, 1, 1, 1, 1, 1 — **this one is true**, and is
   almost certainly what was meant;
2. near-misses each existing edge helps complete → n–ℓ 1, ℓ–k 3, k–q 3, e–f 1, f–g 2, q–g 2,
   k–2S 2 (total 14 = 2 × 7);
3. one-edge triangle extensions per existing edge → 1, 3, 3, 1, 2, 2, 2.

The count of seven near-misses and *fourteen of the twenty-one unused edges are safe* are both exact.
Only the bijection between edges and positions fails.

### 14b-07 · L5854 · "eight rows of twenty-eight" leaves twenty, against the table's twenty-four

Printed: *"**Eight rows of twenty-eight were coordinate systems entered as constraints**, and
removing them emptied the column."* L5842 prints **24 constraints**. 28 − 8 = 20. Register 532
carries the same wording (*"EIGHT ROWS OF TWENTY-EIGHT WERE COORDINATE SYSTEMS ENTERED AS
CONSTRAINTS"*), so the gap of four is in the record as well as the volume. Every other count in
§21.5.5 sums to 24 exactly: parents 14 + 10, form 11 + 7 + 3 + 3, source 16 + 3 + 5, role 4 + 20,
carried 22 + 2 + 0, and 24 − 15 = 9 collisions.

### 14c-01 · L5692 · §32.3 does not record ℛ's level

Printed: *"§32.3 records that ℛ reaches **level 2** — pairwise consistency."* MEASURED: §32.3 is
*Self-defence* (L9038–L9058, 14 body lines) — ⅅ_def's two routes to every number, 102 quantitative
claims re-derived, ⅅ_phys, and D3 totality. Neither *level 2* nor *pairwise* occurs in it. The claim
is Register 489's: *"THE THREE-BODY SHORTFALL IS EXACTLY ONE LEVEL. ℛ reaches pairwise consistency;
a K₃ of treewidth 2 requires strong 3-consistency."*

### 14c-02 · L5753–L5755 · §18.4.1 does not say E measures sparsity

Printed: *"**3.2% density, where §18.4.1's asymmetry says E measures sparsity and not structure**."*
MEASURED: across §18.4.1's 205 body lines (L4999–L5247) the strings *sparse* and *sparsity* do not
occur, and the section's only line naming an asymmetry (L5157) is about φ = min(a,b) closing with
zero failures. The pointer is load-bearing here: it is the stated ground for not reading the
twenty-three absent constraints as predictions.

### 14c-03 · L5859–L5860 · §17.1 does not admit or refuse coordinates

Printed: *"**Defines against constrains is the coordinate the data asked for**, and §17.1 admits no
other here."* MEASURED: §17.1 is *E1 — which cells may be added* (L4794–L4798, **2 body lines**): the
closure condition on Λ ∪ {x}, and 100% over 288 tests. It is about cells, not about which coordinate
axes an index may take.

### 14c-04 · L5704 · "Registers 487–489" cites a three-entry range of which two are off topic

MEASURED: Register 487 is *THE MATHEMATICS CLOSED TO 14% OPEN ON REAL NUMBERS*; Register 488 is
*THREE OBSTRUCTIONS, ONE LANGUAGE ERROR*. Neither is about consistency levels or the four-body
reading the citation supports. Register 489 alone carries it. Per chat 70's R1 vocabulary an
unreferenced or misdirected citation row is a defect.

### 14c-05 · L5799 · §14.5.7 is heading-only — re-measured, not carried

Printed: *"§14.5.7 makes the seed a covering problem and §21.5.3 measures the graph."* MEASURED:
§14.5.7 is L3808–L3809 with **zero body lines**. This re-asserts chat 90's finding from the file
rather than from its disposition (G0b). It is the ninth citing site of a section with no body, and
§21.5.4's whole construction rests on it.

### 14c-06 · discipline, not the volume · HANDOFF-43 mis-cites W-107

HANDOFF-43 and chat 90's DEFERRED block both send §21.5.1's three-body check to **W-107**. MEASURED:
W-107 (working register L4705–L4716) is *BUILD96 GATED IN FULL; PHASE R2 CONTINUED THROUGH MAIN
CHAPTERS 10, 11 AND §12.1–12.7*, and contains no mention of three-body or ternary. The Phase 0–4
discard as executed carried state is recorded in **W-118** (chat 81), with the absorption itself in
W-009, W-059 and W-063 and in Registers 1701–1724. The check was therefore run against the Register,
which is where subject matter lives: §21.5.1's claim resolves to Registers 489 and 507. The plan was
not re-opened and was not put to M.

---

## B — verified

1. All seven of Λ's constraints (L5715) hold on all 976 cells and **each is attained with equality**.
2. The constraint graph is 8 nodes, 7 edges, one component — **a tree** (L5726).
3. The triple table (L5720–L5723) is exact: 0 / 7 / 20 / 8, total 35 = C(7,3), and *zero of
   thirty-five* holds.
4. **Exactly seven** triangle-completing non-edges, and the seven pairs named at L5730–L5733 are
   exactly the measured set, each completing exactly one 3-body.
5. *Fourteen of the twenty-one unused edges are safe* — exact (C(8,2) = 28, less 7 edges, less 7
   near-misses).
6. Λ₈ **is** a caterpillar (the half of the L5747 caption that holds).
7. All six shape cell counts rebuild exactly; all six exact seeds match the table column.
8. **The seed is monotone in S with no exception** (L5826): 8→5, 10→6, 16→6, 16→6, 22→6, 30→8,
   monotone on both the printed and the measured column. The list is stated with the star at 6,
   i.e. the list is consistent with the table and inconsistent with 14b-02/03.
9. L5818–L5819's diameters (5, 2, 3, 4, 3, 2) and maximum degrees (2, 5, 3, 3, 4, 2) match the table
   and the rebuilt graphs exactly. L5819–L5820's cell-count remark is exact.
10. *The alphabet … is eighteen for every shape* — six nodes × three values.
11. Fifteen printed sums, densities and products check out, including 7/216 → 3.2%, 9/24 → 38%,
    15/96 → 16%, box 96 = 2 × 4 × 2 × 3 × 2, 9 + 15 = 24, 21 − 6 = 15, 24 − 15 = 9, and the degree
    sequence's sum of 26 = 2 × 13.
12. Pointers resolving to the claim: §18.4.1 (*doubling*, L5702), §24.9 (*independence is a property
    of TRIPLES*, L6771), §36.3 (L9914, *supplied the deficit and its size. One level*), §21.5.1,
    §21.5.2, §21.5.3 ×2, §2.24 ×2, §14.5.9.
13. Registers on topic: 489, 507, 508, 523, 524, 525, 526, 531, 532.
14. References: **Freuder present**; **Adams, Dwinger & Schmid (1996) present** at main L11685; and
    *chordal*, *treewidth*, *tree decomposition* and *girth* are **absent from the References**
    exactly as L5756–L5757 claims, while occurring 2, 32, 2 and 15 times in the volumes' own text.
    Register 508 records the same finding independently.
15. Citation verb (G0i): five sites cite (*Registers 487–489, 507–508, 523–524, 531–532*;
    *Register 525*) and one names in lowercase (*register 526*, L5811) and is not counted.

---

## C — incidental

1. **L5726's definition is loose.** *"a tree is exactly a graph with no cycle"* defines a **forest**;
   a tree is a *connected* acyclic graph. The conclusion is unaffected — the graph is measured
   connected — so this is imprecision, not a false claim.
2. **The greedy result does not reproduce, and this is not a deviation.** L5810–L5811 says greedy set
   cover gave the star 7. Under this chat's greedy implementation the star comes out at 6. Greedy is
   tie-break dependent, so a different tie-break is a sufficient explanation and the printed claim is
   about a particular historical run. Recorded as non-reproduction.
3. **Register 487 says "Λ's eight constraints"**; §21.5.2 and tower-2.py both give **seven** binary
   bounds (the eighth would be a unary cap). Out of range, cross-chapter — deferred.
4. Register 1790 notes the drawing's own figures *reproduce exactly as drawn* — the figure is
   internally consistent and describes a graph the axes do not define. The repair is therefore to
   the drawing and the table together, not to one of them.
5. `figures/figure-21.1.png` is not present in the container; members extract flat, so absence here
   is not evidence of absence in the build.
6. *(1−f)³* has five sites across the volumes (main L5698, reg L1625, reg L1821, mc L980, mc L1324).
7. §21.5.5's ninth collision is described as one *"the form axis has no value for"* (L5865–L5866),
   yet the form counts sum to 24 with no unassigned row. The miscoded constraint is therefore
   counted under some form value; the two statements are reconcilable but not as printed.
