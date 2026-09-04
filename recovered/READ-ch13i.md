# READ-ch13i.md — Phase R2, chat 81, segment 2: main §14.5.2–§14.5.7 (L3798–3809)

Instrument: `r2-ch13i.py` (banked). The six headings' disposition, measured as the handoff directs:
what each promises, against where the content actually sits. Findings only — no repair (chat 67 hold).

## A — deviations

**13i-01 (R3; the largest pointer gap found in the review so far) — six subsections with no body, and
41 pointers into them.**
MEASURED, L3798–3809: each of §14.5.2, §14.5.3, §14.5.4, §14.5.5, §14.5.6 and §14.5.7 carries **zero
body lines**; the six headings sit two lines apart and the next section with a body is §14.5.8 (79 body
lines). The block is not dead weight — it is cited **41 times**, on 40 lines, across five members:

| target | pointers | where |
|---|---|---|
| §14.5.2 | 4 | MC L15; Register L1789, L1805, L1945 |
| §14.5.3 | 1 | main L11563 |
| §14.5.4 | 4 | MC L63, L510, L560; Register L1769 |
| §14.5.5 | 4 | MC L64, L66, L466, L500 |
| §14.5.6 | 3 | main L3780, L9281; IoI L281 |
| §14.5.7 | 25 | main L1203, L3812, L3919, L3923, L3961, L3979, L4107, L5656, L5799, L7799, L11759; MC L69, L130, L684, L788; Register L1809, L1817, L1877, L1905, L2065, L2117, L2225 (×2), L2397; MAIN_AUDIT L106 |

Forty of the forty-one occurrences are in the **four reader-facing volumes** (main 14, MC 12, Register 13,
Index of Indices 1); the forty-first is in MAIN_AUDIT, a process member. §14.5.7 alone carries 25.

**13i-02 (R3; the sharpest of the class) — five Mathematical Compendium entries carry an R-FORM
citation chain that resolves to an empty section.**
MEASURED, the five `Proved —` / `Computed —` lines whose first link is one of the six:

- MC L466 *Computed — M §14.5.5; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999.*
- MC L500 *Computed — M §14.5.5; Deville et al. 1999.*
- MC L510 *Proved — M §14.5.4; Beeri, Fagin, Maier & Yannakakis 1983.*
- MC L560 *Proved — M §14.5.4; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995.*
- MC L788 *Proved — M §14.5.7; Birkhoff 1937; Moore 1910.*

R-FORM makes the citation chain the entry's warrant. For these five the first link is a heading with no
text, so the chain is broken at its own volume before it reaches the prior art. The same applies to the
MC's **notation table**, which defines the two operators the compendium uses by pointer alone — L63
(**ℛ**, *"closure at the (≤,≤) corner of Deville's staircase class"*, → §14.5.4), L64 (**ℛ₄**, → §14.5.5),
L66 (**E₄**, *"the defect under ℛ₄; E − E₄ is the orientation cost"*, → §14.5.5), L69 (**seed**, *"least
G with ℛ(G) = X — NP-hard"*, → §14.5.7) — and to the MC's opening sentence L15, *"The whole of this work
is one recursion, stated at §14.5.2."*

**13i-03 (R3) — the promised content is absent, not displaced.**
The handoff's hypothesis was that the bodies might sit at §14.5.8–§14.5.14. MEASURED over L3810–4075:
`ℛ₄`/`orientation` **0 lines**, `840` **0**, `750` **0**, `localis` **0**, `two pairwise operators` **0**,
`cycle` **0**, `anti-exchange` **0**. Nothing was moved down. Two consequences:

- **`anti-exchange` occurs nowhere in the main volume at all** (0 lines in 18,470), yet MC L130 cites
  *"§14.5.7's anti-exchange failure"* alongside Register 618. The cited claim has no site in any volume.
- **The seed's definition survives only as a quotation of the section that would state it.** `seed iff` /
  `φ̂(G)` occurs on exactly one line of the main volume, L3923 inside §14.5.9: *"§14.5.7 says G is a seed
  iff φ̂(G) = φ̂(X)."* Every seed figure in the book — including the exact seven re-measured in segment 1 —
  rests on a definition that exists only in another section's report of it.

**13i-04 (R3) — main L11563 attributes the 840-cell witness to §14.5.3; it sits at §13's L3579.**
References text: *"E(ℛ) = 0 IMPLIES 2-decomposability and is not implied by it — **§14.5.3 gives an
840-cell witness** determined by its pairwise projections with E(ℛ) = 750."* §14.5.3 is empty. The
witness is the **parity rule** at L3577–3579 (*|Δℓ| = 1, δ⁻¹({−1,+1}), imposed on Λ₉ — 840 cells,
E = 750*), restated at L5676 in the open-index table (*the parity rule 840 · 750 · seed 13 · printed 763
· 1.1×*). The **figures are exact**: chat 80's r2-ch13e, re-run OK at this chat's gate, measures 840
cells and |ℛ(X)| = 1,590, E = **750**, with the companion spin rule at **526 cells, E = 0**. The claim
and its witness are sound; only the pointer is wrong. Same class as 13d-01 and 13h-01.

**13i-05 (R3, second-order) — three pointers into the block assert findings the block cannot contain.**
main L3780 (*"§14.5.6 records the spread across shuffles and both operators"*, = 13h-02), main L9281
(*"both outside · dishonest, the same pair §14.5.6 finds"*) and IoI L281 (*"the audits index's two
frontier cells are the same pair **ℛ₄ refuses at §14.5.6**"*) all report a specific measured result out
of an empty section, and the last carries it into a second volume. Register L1769, L1789, L1805 and
L1945 do the same for §14.5.2 and §14.5.4 — L1789 quoting figures (*"ℛ at 11, 12, 12, 13 across
shuffles, ℛ₄ at 12, 15, 15"*) that no surviving section prints.

## B — verified

- The block's boundaries: `### 14.5.2` at L3798 through `### 14.5.7` at L3808, each followed by one blank
  line; §14.5.8 opens at L3810 with 79 body lines. Chat 80's measurement of six bare headings two lines
  apart is confirmed exactly.
- §14.5.8's back-reference L3812 (*"§14.5.7 measures the seed on scattered shapes"*) and §14.5.9's
  L3919/L3923/L3961/L3979 all treat §14.5.7 as extant and quotable; §14.5.9 L3979 even records
  *"§14.5.7 stands unamended"*. The block's absence is therefore a production loss, not an authorial
  deletion — nothing in Chapter 14 reads as though the six were meant to be empty.
- The 840 / 750 and 526 / 0 figures of the misattributed witness reproduce exactly (r2-ch13e.out,
  re-run at this chat's gate).
- No census row falls in L3798–3809 (`r2-tools.py census 3798 3809` → *rows in range: 0*).

## C — incidental

- The heaviest single dependency in the review so far: **§14.5.7 is cited 25 times**, four of them from
  the MC and nine from the Register, and it defines the seed — the object §14.5.8 through §14.5.14, all
  of Chapter 14's remaining measurements, and §21.5.3, §5656's count/constraint result and §7799's
  register-shape reading are built on.
- **For M's disposition at R3:** the six bodies are either recoverable from the run that wrote the
  headings or they must be rewritten. Nothing here can be repaired by re-pointing, unlike 13h-01 or
  13i-04 — five R-FORM chains and a notation table in a second volume depend on text that does not
  exist. This is the one finding of the review so far that blocks a volume rather than a line.
- The contents list (L120–L135) is chapter-level only, so no navigation apparatus exposes the gap to a
  reader; a reader meets it only by following one of the 40 pointers.
