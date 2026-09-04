# READ-ch13h.md — Phase R2, chat 81, segment 1: main §14.5 (L3732–3762) and §14.5.1 (L3763–3797)

Instrument: `r2-ch13h.py` (banked). Every general claim re-measured on all 976 cells of Λ₈, all 1,654
of Λ₉, and every subset of the three small ambients. Findings only — no repair (chat 67 hold).

## A — deviations

**13h-01 (R3) — L3756's §8.4 pointer credits a count that section does not make.**
Text: *"a Moore family is determined by its meet-irreducible members, and **§8.4 already counts those
for Λ under a different name**. Q item R. Register 461."*
§8.4 (L1873–1899, *Sperner, and not symmetric*) counts the largest antichain (122 at rank 11), states
log-concavity, the −0.43 skew, and the self-duality survivors (8 of 976). It counts no irreducibles of
any kind. The irreducibles of Λ are counted at **§8.3** — seventeen join-irreducibles and twenty
covering relations (L1848, L1851, L1869), which L10092 confirms in the same words (*"§8.3 states that
Λ has seventeen join-irreducibles"*). The only site in either volume that gives Λ a **meet**-irreducible
count is **Appendix D.5.7 L10735**, *"17 meet-irreducibles = 17 join-irreducibles"*, listed there as one
of four elements the companion paper adds. Same class as 13d-01: the pointer resolves to a heading, not
to the claim. Note also that the meet-irreducibles of §14.5.1's Moore family (closed **sets**) and the
meet-irreducibles of the lattice Λ (cells) are different objects; L3756 slides between them.

**13h-02 (R3) — L3780 points at a subsection that has no body.**
Text: *"Greedy removal gives an upper bound, not a minimum; **§14.5.6 records the spread across shuffles
and both operators**."*
§14.5.6 is L3806, a bare heading with no body (the block L3798–3809 is six bare headings two lines
apart; MEASURED in chat 80, READ-ch13g). The spread is in fact recorded at **§14.5.9 L3942–3944**
(*"Thirty-three on Λ₈, where reverse-delete gives forty against an exact seven"*). "Both operators"
points the same way at **§14.5.5** (L3804, *ℛ₄ — the four orientations, adopted*), also a bare heading.
Same class as 12h-01 / 13g-02, and load-bearing: L3780 is the only qualification the boxed seven-cell
claim at L3775 carries.

**13h-03 (R3) — L3787's "about 1.25 per cell" is true of one ambient of three.**
Text: *"Meet-irreducible closed sets number 12, 14 and 20 at 8, 9 and 16 cells — **about 1.25 per
cell**"*. MEASURED: 12/8 = **1.5000**, 14/9 = **1.5556**, 20/16 = **1.2500**; unweighted mean 1.4352,
pooled 46/33 = 1.3939. Only the 16-cell ambient gives 1.25, and it is the smallest of the three ratios,
so the figure understates the count at both of the others. The counts 12, 14, 20 themselves reproduce
exactly, as does the linearity the sentence draws from them.

**13h-04 (R3; Register 467 and Register 505 inherit) — "139 to 1, exactly" is a rounded ratio.**
Text L3775: *"**Λ is the closure of SEVEN of its cells — a compression of 139 to 1, exactly.**"*
MEASURED: 976 / 7 = **139.4286**; 976 = 7·139 + 3. The **seven is exact** (re-measured here by exhaustive
branch and bound — see B), so the sentence is true if *exactly* attaches to *seven* and false if it
attaches to the ratio, and as printed it attaches to the ratio. Register 467's correction line settles
the reading against the text — *"superseded by register 505, which gives seven cells and **139 to 1,
exact**"* — and the same rounding sits in 467's own superseded figure, *"a compression of **89 to 1**"*
for eleven cells (976/11 = 88.7273), which §14.5.8 L3821 repeats as *"Λ₈ compresses 89×"*. §14.5.9's box
L3935 prints the ratio without the word: *"976 cells from seven — a compression of 139 to 1."*

**13h-05 (R3) — L3795's "has never cited Carathéodory" is contradicted by this volume's own References.**
Text: *"**This book already cites Helly and has never cited Carathéodory**, which is the second
bibliography gap the cycle's step 2 has found in two runs. Registers 466–468."*
The References carry a Carathéodory entry at **L11765–11769** (*"Carathéodory number / convexity
spaces … Located through the enumeration literature; no single work is cited because the result used is
standard and appears in several"*), and the Mathematical Compendium carries a full entry with prior art
(MC L650–658, *Caratheodory 1911*) and lists it in the bibliography table (MC L3411). Register 468's own
body records the entry being made — *"This book cites Helly and did not cite Carathéodory. **Entered.**"*
— and §14.5.8 L3836 then reads *"The coefficient was already in this book's References, glossed and
left."* The present-tense sentence at L3795 describes the state before the entry it announces; on the
live text it is false. **Census row 1077** (C9-OVERGENERALISATION-WORD, *never*) closes as a **defect**
on this ground, not as a regex artefact.

**13h-06 (R3, residue) — the References entry carries the withdrawn eleven.**
L11767–11768: *"**§14.5.1's eleven-cell generating set** is an irredundant set in this sense."* §14.5.1
as printed gives seven (L3775), and Register 467's eleven is marked superseded by Register 505. The
References site is a residue of the same supersession, alongside the withdrawn ten-to-thirteen §14.5.9
L3934 reports. The later line governs (G0b): the seed is 7.

## B — verified

- **L3768–3770, on all 976 cells.** ℛ(Λ \ {x}) = Λ for **every one of the 976**; the operator restores
  each single deletion **exactly**, |ℛ(Λ\{x})| − |Λ\{x}| = 1 at all 976 with no other value. E(Λ₈) = 0.
  Register 466 reproduces in full.
- **L3738–3741, the whole table.** Closed subsets **73 / 146 / 731** at 8, 9 and 16 cells (the empty set
  excluded; with it, 74 / 147 / 732); shares of 2ⁿ **28.516 % / 28.516 % / 1.115 %**, printed 28.5 / 28.5
  / 1.1; **∩ closed at 100 %** on every pair in all three families; **∪ closed 64.38 % / 68.34 % /
  32.56 %**, printed 64.4 / 68.3 / 32.6 — reproduced exactly on unordered distinct pairs of the
  ∅-excluded family, the same convention as the counts. Register 461's *"intersection-closed at 100 %,
  union-closed at 32 to 68 %"* reproduces. The Moore-family statement (L3743–3744) holds as measured: the
  families are ∩-closed and not ∪-closed.
- **L3786–3789.** Meet-irreducible closed sets **12, 14, 20**, and they **generate the whole family under
  intersection exactly, once the empty set is counted among the closed** — measured: 74, 147 and 732
  sets generated, matching the families including ∅. Linear against a family that is not.
- **L3775, the seven, re-measured independently of §14.5.9.** Reducing §14.5.7's definition (G is a seed
  iff φ̂(G) = φ̂(X)) to a set cover — 200 elements (25 value slots, 175 envelope steps) over 976 candidate
  cells, then two exact reductions to 27 irredundant elements and 59 non-dominated covers — exhaustive
  branch and bound finds **no seed of size 1…6 and a seed of size 7**. Witness (7 cells):
  (2,1,3,3,2,1,3,0) (3,1,3,3,1,0,0,0) (1,0,2,2,3,1,2,0) (1,0,2,2,1,0,2,2) (2,1,3,0,1,0,0,3)
  (3,0,1,0,3,1,0,0) (3,1,1,1,3,0,1,1); ℛ(witness) = Λ₈ exactly, |ℛ| = 976. **seed(Λ₈) = 7 is exact.**
- **L3772–3773's greedy figures.** Prune-greedy over five seeded shuffles: **9, 11, 11, 12, 10**; the
  printed 12, 11, 12 lies inside the measured range and 12 and 11 both occur. Descending-order prune 11,
  ascending 10.
- **L3782–3784.** Seven against Birkhoff's **seventeen** join-irreducibles (§8.3 L1851; 17 confirmed in
  chat 80, READ-ch13g): the operator's generating set is smaller than the lattice's, as stated.
- **L3939's arithmetic** (resolved forward from L3777): d = 8, c = max alphabet 4, d + c − 1 = **11**.
  Per-coordinate value counts of Λ₈ are (3, 2, 3, 4, 3, 2, 4, 4); ambient box 6,912 cells.
- **L3751–3753 and Register 458.** Λ₉ is closed (E(Λ₉) = 0) and **300 of 300** random subsets are open
  under an independent sample (sizes 3…1,653).
- **Pointers resolved to the claim, not the heading:** §14.2 → L3711 (ℛ a closure operator, the meets/joins
  asymmetry L3748 relies on); §14.6 → L4076–4082 (the family shown open, with the #P-completeness reason);
  §14.5.9 → L3917–3934, which does give *seven, exact by branch and bound*; §2.24 → L1184–1197, which is
  the run-two-heuristics-and-report-the-spread protocol L3778 credits it with. Registers 461, 466, 467,
  468 all resolve and all state what the text attributes to them.

## C — incidental

- The subsection uses **two ∅ conventions**, each correct where it stands and neither stated: the table
  (L3739–3741) counts and pairs the closed sets **without** ∅, while the generation claim (L3788)
  requires ∅ **among** them. A reader recomputing 73 from 74, or 64.4 % from 65.8 %, has no way to know
  which is meant.
- The union column's denominator is **unordered distinct pairs**; ordered pairs give 64.87 / 68.56 /
  32.65 and would print as 64.9 / 68.6 / 32.7. Not stated anywhere in the section.
- **Cross-note for the §14.5.9 segment:** that section's table L3929 gives Λ₈ a *reverse* figure of **40**
  and a spread of 33. Prune in descending cell order measures **11** here, so 40 comes from a different
  algorithm (reverse-delete proper, not order-reversed prune); the 33 rests on it. Measure it there.
- **Cross-note for the §14.5.2–§14.5.7 segment:** 13h-02 is a second load-bearing pointer into the empty
  block, after §14.5.8 L3812's back-reference to §14.5.7 (chat 80). Both are pointers to claims, not
  headings, and neither survives as printed.
