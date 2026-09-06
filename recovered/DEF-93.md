## Chat 93 — deferred out of the Chapter 22 read (main L5937–L6035)

- **F.3's four-column standard is a class test, not a Chapter 22 item** (14f-01). §22.1.1.1 claims
  *F.3's highest standard* on three columns. F.3 (main L11278–L11300) states four — the method, the
  input set, the inputs, the refutation — and says a statement carrying fewer than four is a different
  kind of object. R3 must grep **every site that cites F.3 or claims its standard** and test each for
  all four columns; that census has not been taken. The repair for this site is either supplying the
  refutation (a level failing containment is the available falsifier, and the table's *contained*
  column could have printed less than 9) or dropping *highest*. The decision is M's, but the census is
  R3's and is wider than one section.
- **The printed-input standard is broken one subsection after it is claimed** (C-1). §22.1.1.1 prints
  its input set in full; §22.1.2's seven widths are reproducible only at δ = 0.35, which the section
  never prints. Same for M in §22.1.1 (C-2), which the *N ≈ √(M/m)* bound needs and which solves to
  the deuteron mass. Both are one-word repairs, but they belong with the F.3 sweep above rather than
  as isolated fixes, because the standard is what makes them defects.
- **Register 319's placement, and the entry that does not exist** (14f-03). Moving the pointer to the
  end of L5975 fixes the citation. It does not fix the gap it exposes: **no Register entry carries the
  one-dimensional refinement of §18.4.1's criterion** — *for a bracket on one chain, monotone in
  either direction suffices; only closure in a product requires increasing*. That is a subject-matter
  claim standing without a record. Register entries are append-only and this one is missing, not
  wrong, so R3 writes a new entry rather than correcting 319. Held until the review closes.
- **The "single run" §22.1.1.1 improves on has no printed site** (14f-02). Before L6004 can be
  repaired, R3 must determine whether a one-defect containment run is printed anywhere in the six
  volumes or whether the comparison should read *what a single defect could not distinguish*. A grep
  for a containment run outside §22.1.1.1 has not been made; §22.1 itself prints none, which is what
  this chat measured.
- **§33.4 and §22.1.1 are an unlinked conceptual twin** (C-5). *An index is closed when its output
  class is a singleton* against *a bracket whose admissible set is a singleton*. Same structure,
  different objects, and neither section points at the other — tested both ways. R4: either a
  cross-reference in both directions, or a single sentence naming the relation and its limit. Note
  that the Index of Indices (ioi L1609–L1611) and the Mathematical Compendium (mc L3753) both carry
  the output rule and neither carries the bracket use, so the compendia would need the same link.
- **The companion paper is cited, listed and unmeasurable** (C-8). *Muon-Catalysed Fusion*, Lach 2026,
  is at References R.3 (main L11598–L11601) and is **not a member of either bundle**. Three claims in
  this range are companion-side: the paper's own 61 / 4.2 / 1.03, the first observed r_ℓ exit
  predicted from ν⁻³ scaling, and the reference line's own list of reproduced figures (cycle cap
  2.6 × 10⁸ s⁻¹, breakeven sticking 0.203/0.262/0.292 %, decay lengths 11.2 m and 623 m). This is the
  same standing item chat 92 recorded for the *other* companion: if either paper is ever seated as a
  member these close in one pass, and R4 should say they are unverifiable rather than leave them
  looking open. This book's own recomputation of the trio **is** verified (14f-B6).
- **Register 391's markup** (C-6). Five unbalanced emphasis runs (`* **`) inside one entry, closing
  the wrong span mid-sentence. Production class, noted not repaired, per M's standing priority — but
  the Register is reader-facing and this is the second entry found with the fault, so R3 should sweep
  the Register for the pattern rather than fixing one entry.
- **L6003's order-of-magnitude claim** (C-4) is true of the output energies (107×) and loose for the
  input δ (7.57× between the nonzero extremes, undefined from zero). Register 391 restates it in the
  same form. If R3 tightens the sentence it must tighten the Register entry's successor too — the
  entry itself is append-only.
- **Owed to r2lib**, unchanged from chat 92 and not added to this chat: `seed_of()`, `greedy_seed()`,
  the exact `treewidth(nv, E)` DP, the `girth` / `ecc` / `is_caterpillar` primitives,
  `rung_multisets()`, and the `E(X)` / `grid(X)` pair on `r2lib.Rset`. Chat 93's instruments needed
  none of them — Chapter 22 is arithmetic on a Rydberg series and pointer resolution, with no tower
  computation at all, which is why r2-ch14f does not import r2lib.
- **Method note for chat 94, from this chat's own errors.** Four instrument faults, all caught before
  banking. The one to carry: **after writing any verdict that compares two measured numbers, re-read
  the comparison against the numbers.** F11 printed *LARGER* for 0.29 % against 2.72 % and drew the
  opposite conclusion from the correct measurement. This is chat 92's inverted-verdict class in a new
  form — there a substring match, here a comparison word — and in both chats the arithmetic was right
  while the sentence built on it was wrong. Also: a summary line that generalises over a list must be
  written after the list is printed, not before (G8 described nineteen sites it had not yet classified).
- **Chapter 22 remainder (chat 94, main L6036 onward)** — boundaries MEASURED by heading scan this
  chat: §22.2 L6036, §22.2.1 L6056, §22.2.2 L6071, §22.2.3 L6087, §22.2.4 L6101, §22.2.5 L6107,
  §22.3 L6129, §22.4 L6138, §22.4.1 L6148, §22.5 L6168, §22.6 L6175, chapter ends L6178 (Chapter 23
  opens L6179). 143 lines, eleven headings. Confirm every boundary by scan again before reading a
  line. §22.2's *four rules* and §22.2.1's ablation are the computable core; §22.3's *limit-free* and
  §22.4's *price of limit-freedom* are where the prose batch will sit.
