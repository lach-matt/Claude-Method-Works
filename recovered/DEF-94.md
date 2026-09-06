## Chat 94 — deferred out of the Chapter 22 remainder read (main L6036–L6177)

- **§32.3 is a citation class, not a site** (14h-05). Four prose citations of §32.3 exist in the
  main volume and three disagree with the section: L5692 cites it for ℛ reaching level 2 (chat 91),
  L6138 for presenting limit-freedom as pure gain (this chat), and L7492's erratum speaks of its
  *four clauses* where three are printed (ⅅ_def, ⅅ_phys, D3). The three index entries at
  L11472/L11476/L11477 resolve. R3 should treat this as one docket: read §32.3 once, then test all
  four prose citations against it, rather than repairing sites as they are met. The candidate target
  for L6138 is **App A.12** (*The bracket is limit-free*, L10022) or **§22.3** itself, both of which
  carry the claim; the decision is M's and the census is R3's.
- **"ν, δ and V all need the ionisation limit" stands at two sites** (14h-02): main L6133 and App
  A.12 L10035, worded almost identically. V = w/e is invariant under T = I − E by the same
  cancellation A.12 proves for containment. One decision, two sites, and App A.12's Consequence is
  the more load-bearing of the two because it is the theorem's own statement. Note that the repair
  is not simply deleting V from the list: V *expressed as* 4ν/3 does need the limit to evaluate,
  while V *measured as* w/e does not, and the sentence needs to say which it means.
- **The σ collision is chapter-wide, not §22.5-local** (14h-01). Rule 4 (L6047) and §22.5 (L6168)
  use σ for different quantities. Before R3 rewrites either, it must grep every σ in Chapters 22–23
  and in App A, because the cost surface of Chapter 23 uses the same symbol again and the
  admissibility ratio is quoted in the Spectra Compendium. Whether *r falls as ν⁻³* survives depends
  entirely on which σ the book means, and that is a subject-matter decision.
- **The unprinted-input class now has six members and should be repaired as one class, not six
  edits** (14h-08, 14h-09, and chat 93's C-1/C-2). §22.1.2 needs δ = 0.35; §22.4.1 needs δ₂ = 0.06;
  L6060's 446×, L6068's 1,577, L6093's 3.47 % and L6104's *factor of 17* each need an input more
  precise than the one printed beside them. §22.1.1.1 claims F.3's highest standard, whose columns
  include the input set. R3's census is: **every site in the six volumes that prints a derived
  figure beside its inputs, tested for whether the printed inputs reproduce it.** That census has
  not been taken and is wider than Chapter 22.
- **Seventeen single-witness figures in 141 lines** (C6). 69.6, 41.3, 12,942, 0.8189, 0.7129,
  0.7376, 0.7835, 3.47, 14,602, 4,329, 4,267, 1.387, 1.386, 68.06, 0.00102, 0.0210, 7.613 appear at
  no other site in any of the six volumes. They are internally consistent where a check exists
  (H5, H12, H13 all reproduce from them) but nothing in the collection can contradict them. This is
  the same standing item as chat 93's C-8 and chat 92's companion-paper note: R4 should state which
  figures are unverifiable rather than leaving them looking checked.
- **§25.6's vocabulary is unsettled inside itself** (C4). Its title and §25.6.3 deny that the Sc VI
  value is a prediction; its own opening line at L6992 and §25.6.6's title use the word. Ten uses
  against three of *deduction*. Chapter 22's L6098 follows the second usage, so the citing site
  cannot be judged until §25.6 settles. R3 must fix §25.6 before it touches L6098, and the order
  matters — repairing the citation first would lock in the usage the section is trying to withdraw.
- **The antiprotonic-helium pointer needs a target chosen, not corrected** (14h-05). L6135's cells
  are at §16.4 (L4419) and §19.2 (L5401, L5416); §2.8's L612 already names §16.4 for the same
  check, so the book has a working form to copy. But §16.4 and §19.2 use the case for different
  purposes — an apparatus check and a retrieval-redundancy count — and only M can say which one
  limit-freedom is supposed to have admitted.
- **§22.6's *only linearly rising quantity* and Chapter 23** (14h-06). The counterexample is
  §22.4's L = n/3, and §23.1's general V(x, p) = 4x/(h|p − 1|) adds one per p ≠ 1. Chapter 23 has
  not yet been read, so R3 should not repair the sentence until the cost surface is read — the
  qualification it needs may already be stated there.
- **Row 4 of the ablation table** (C2). ±1σ coverage 96.2 % against 69.6 %, with the nominal at
  68.3 % unstated. The row is the only one where the larger number is the violation, and it reads
  as a defect of the table rather than of the rule. R3 should consider printing the nominal.
- **Owed to r2lib**, unchanged and again not added: `seed_of()`, `greedy_seed()`, the exact
  `treewidth(nv, E)` DP, the `girth` / `ecc` / `is_caterpillar` primitives, `rung_multisets()`, and
  the `E(X)` / `grid(X)` pair on `r2lib.Rset`. Chapter 22 needed none of them; neither instrument
  this chat imports r2lib. **Newly owed, and used twice this chat:** `section_span()` by dotted-number
  extension (rank fails because the book sets §25.6 and §25.6.1 at the same `###` depth),
  `has_token()` word-bounded matching, and an appendix-aware `enclosing()`. All three are in
  r2-ch14i.py with provenance comments and should be lifted before the next prose batch rather than
  copied a third time.
- **Method note for chat 95, from this chat's own errors.** Seven instrument faults, all caught
  before banking. The one to carry: **an instrument that contradicts a measurement already taken
  from the file is wrong until proved otherwise.** Twice this chat an instrument reported a pointer
  failing that the hand reading had already resolved, and both times the instrument was at fault —
  once through a span rule, once through a substring match. Second: **never round with Python's
  `round()` in an instrument**; it is binary and returns 17.2 for 17.25 and 2.1 for 2.15. Use
  `Decimal.quantize` and name the convention, because three of this chat's faults were that alone.
- **Chapter 23 (chat 95, main L6178 onward)** — boundaries MEASURED by heading scan this chat only
  for the chapter's opening: §23.1 L6180, §23.2 L6196, §23.2.1 L6215; the chapter runs to L6622 and
  Chapter 24 opens L6623. **445 lines, far larger than any section read yet closed** (93, 63, 99,
  141), so chat 95 must scan the headings forward, confirm every boundary on the member, and take
  §23.1–§23.2.x as the first unit rather than the chapter. Chapter 23 contains Proposition 23.1
  (L6199–L6204) with a printed proof, a figure at L6191 with a caption carrying 32/11 = 2.909 and
  26/9 and 0.69 %, and a pole at p = 1 — the computable core. Note that 14h-02 and 14h-06 both
  resolve against Chapter 23's definitions, so the read should confirm them rather than re-derive.
