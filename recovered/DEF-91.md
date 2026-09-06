
## Chat 91 — deferred out of the Chapter 21 second-part read

- **The Λ₁₃ constraint-graph repair is already specified by the record and needs no new measurement.**
  Register 1790 (reg L6603) withdrew §21.5.3's table and figure 21.1's caption and states the measured
  graph: 13 nodes, 14 edges, cycle rank 2, girth 3, one triangle 2S′–g–v from Λ₁₀ onward, diameter 6,
  radius 4, treewidth 2, hub k at degree 4 with g also at 4, degrees 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1,
  1, 1, leaves n, e, 2S, 2J, second cycle 2J_c–2K–f–g–q–k at Λ₁₂. Chat 91 reproduced all ten fields
  independently from tower-2.py's bounds. **Three sites carry the withdrawn figures: main L5745
  (caption), main L5765 (table), reg L1953 (Register 523).** Register 523 is append-only and is
  corrected by 1790, not edited (Ruling 29 does not apply — this is not a pointer removal). R3 repairs
  the two main-volume sites. **Figure 21.1's artwork is part of the repair**: 1790 records that the
  drawing omits Λ₉'s 2S′ and gives v the parents 2S and g, so the image is wrong in the same way the
  caption is, and redrawing needs M's instruction.
- **Census row 1128 is inside this class.** *"the one place in this work where ℛ has never been the
  right operator"* (L5699) is false once the tower itself carries a K₃ from Λ₁₀; closed as a defect
  and repaired with 14b-05 or not at all.
- **The star-seed class is two sentences, and the rest of §21.5.4 is already correct.** L5813–L5814
  (*the path and the star at eight and seven*) and L5818–L5819 (*seeds 8, 7, 6, 6, 6, 5*) are the only
  survivors of the withdrawn 7; the table, the monotone-in-S list and the closing paragraph all carry
  6. MEASURED exact seeds 8, 6, 6, 6, 6, 5. This is the same class as chat 90's L5685 seed band, and
  the two should be repaired in one pass.
- **"The largest orientation cost anywhere in this book" is a superlative with two counterexamples**
  (main L5843 at 15, mc L462 and reg L1773 at 750). R3 must decide whether the sentence loses the
  superlative or gains a scope; the sites are main L5785 only, but the neighbouring claim at L5786
  (*the first object on which the second operator is the only one that works*) is untested and should
  be measured before the sentence is rewritten.
- **Three pointers do not resolve and each needs a target, not a deletion.** L5692 → §32.3 (the claim
  is Register 489's); L5753–L5755 → §18.4.1 for a sparsity statement that section does not make, and
  it is the stated ground for not reading twenty-three absent constraints as predictions, so removing
  the pointer removes the argument; L5860 → §17.1, which is two lines about which cells may be added.
  R3 cannot fix these by grep — each needs the intended section identified.
- **L5704's "Registers 487–489" over-cites by two entries** (487 and 488 are off topic; 489 carries
  the claim). Cross-check when the citation counts are recomputed: register_cites.py counts the range,
  so narrowing it changes the count.
- **§14.5.7 remains heading-only and is still the ninth citing site's target** (L5799). Re-measured
  from the file this chat: zero body lines. Chat 90's item stands unchanged and still needs M's ruling
  on production loss versus authoring gap before R3 can open it; Prints & Proofs is the witness.
- **L5854's "eight rows of twenty-eight" leaves twenty against a table of twenty-four**, and
  Register 532 carries the same wording, so the gap of four is in the record as well as the volume.
  A repair to the volume alone would leave the two disagreeing.
- **Register 487 prints "Λ's eight constraints"** where §21.5.2 and tower-2.py give seven binary
  bounds. Out of range, unmeasured beyond the count itself, and it touches every site that states Λ's
  constraint count. Flagged for the cross-volume pass (R4), not for R3.
- **Owed to r2lib:** `greedy_seed(cells)` (the tie-break-sensitive greedy cover, useful for testing
  any further "greedy was wrong here" claim), the exact `treewidth(nv, E)` elimination DP, and the
  `girth` / `ecc` / `is_caterpillar` graph primitives. All are inside r2-ch14b.py with provenance
  comments until lifted. `seed_of()` is still owed from chat 90 and is now used by two instruments.
- **Method note for chat 92, from an error made this chat:** before recording any printed figure as
  unreproducible, grep the Register for a later entry naming the section. Register 1790 supersedes
  §21.5.3 and was found only after the disagreement had been written up as a reconstruction failure.
  The Register's late entries (1780–1792) are corrections to earlier chapters and are not indexed from
  the sections they correct.
- **Chapter 21 third part / Chapter 22 (chat 92, main L5874–L5936, 63 lines, three headings)** —
  boundaries MEASURED by heading scan this chat: §21.6 L5874, §21.6.1 L5905, §21.6.2 L5924, PART V
  L5937, Chapter 22 L5939, §22.1 L5943, §22.1.1 L5953, §22.1.1.1 L5982. The range is short, so
  §21.6–§21.6.2 and Chapter 22's opening may fit one chat; confirm every boundary by scan first.
