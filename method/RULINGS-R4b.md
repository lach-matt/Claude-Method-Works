# RULINGS-R4b.md — the object test, and the order of work it fixes. M, 5 September 2026. Successor to RULINGS-R4.md.

`RULINGS-R4.md` is a member and is never edited; this is its successor and governs where the two differ.

## 1. The ruling

M, on the register-count sites: *"most of these corrections are good, but will ultimately be struck in the prose
edits. I want to focus on making sure the math, the claims, anything that isn't correctable by prose editing, is true
and proven so. … **a false claim is an object that is false when the prose is stripped away. anything that is true
before prose, but not when prose is applied, is then a prose error and fixable by me in the form of a prose edit.**
I intend for us to do the prose edit together from the beginning to the end one page/chapter at a time when all the
subject matter is true before the prose is applied."*

And, on the register counts specifically: *"the register count statements are not necessary to the reader, only the
register citations … I'd rather have a paragraph included in the front matter that explains the purpose of our
register rather than drawing specific attention to its numbers"*, in Part 0.

## 2. The test, stated for use

**Strip the prose away and look at the object underneath — the number, the equation, the measurement, the proof, the
relation, the attribution. Is that object false, unproven, or unsupported?**

- **A false claim** is one whose object is false. Fixing it requires changing a measured quantity, a computed figure,
  an equation, a proof, a data value or an attribution, or withdrawing a result. The defect survives any rewording.
  **This is the work now, and it is executorial: it is measured, proved, or recorded as unproven.**
- **A prose error** is one whose object is true and whose wording is wrong. Fixing it changes no measured quantity.
  **This is M's, done with M, page by page from the beginning to the end, after the subject matter is true underneath.**
- **An unproven claim is not the same as a false one, and it is not thereby acceptable.** M's words are *"true and
  proven so"*. A figure the record carries without an instrument, a figure reproduced once and never again, a figure
  whose inputs are not printed — each is recorded as unproven, with what would settle it, and none is quietly counted
  as true.

**The discriminator that settles most cases.** A count *about the work itself* — register entries, compendium objects,
sections, audits — is furniture, and furniture is prose. A count *about the subject* — cells of Λ, the tower's ranks,
channels, levels, elements, a percentage of a measured population — is the object, and the object must be proven.

**The case that established it.** Fifteen main-volume sentences printed the Register's size as a count of corrections,
withdrawals, errors and failures, against 186, 34 and 16 measured. Every one was a prose error: the objects — 1,677
entries, 186 corrections, 34 withdrawals, 16 faults — were true throughout, and the sentences attached true numbers to
the wrong nouns. It was flagged rather than repaired, which was right; it was then read as a false-claim class, which
was wrong. `DRAFT-R4-COUNT-SITES.md` and `DRAFT-R4-REGISTER-COUNTS.md` are kept as the record of both, and the
repair they propose waits for the joint prose pass.

## 3. What this changes in the plan

`PLAN-R4-PUBLICATION.md`'s eight phases stand, but their order and ownership change:

- **Phase 3, the main-volume prose leg, is not mine to execute.** It becomes the joint pass M describes — beginning to
  end, one page or chapter at a time — and it opens only when the subject matter beneath it is true. Every prose
  finding already gathered is held for it, not worked.
- **Phase 1, the mathematics leg, is the whole of the near work**, widened from "the classes the record names" to
  every claim in the six volumes whose object must be shown true: measured, re-derived by an instrument that is
  seated and banked, or recorded as unproven with what would settle it.
- **Phase 5, the census, is re-cut by the same test.** Its prose classes (`C13` handles, `C9` words, `C8` names,
  `C7` surviving numerals) are held for the prose pass; its object classes (`C6` numbers not in their stated source,
  `C10` proved without a Register entry, `C11` the R-form incomplete, and the pointer classes where the support is
  absent) belong to Phase 1.
- **Phase 8, the press, has already been pulled forward.** A reading copy of all six volumes exists at `out/reading/`
  (933 pages, `tools/press/`), because M cannot judge subject matter he cannot read. It is re-pressed whenever the
  volumes change, and it is not the edition.
- **Ruling 2 of `RULINGS-R4.md` is superseded by §1 above.** The count is not re-typed at fifteen sites; it leaves the
  prose, and Part 0's Preface gains the paragraph on the register's purpose, in the joint prose pass.

## 4. What is proven at this build, measured

Recorded so the next chat does not re-derive it: `tower-2.py` rebuilds Λ₈ … Λ₁₃ to **976 · 1,654 · 2,535 · 13,585 ·
70,905 · 199,130**, the six counts the volumes state; `minmax.py` gives **E(Λ₈) = 0** with the eight projections, the
three constants, min and max closed on 10 of 28 coordinate pairs and sum, product and difference on none, and φ̂
realised. Both are §0 gate steps and run every session. `tools/arith.py` over all six volumes reads **264** arithmetic
sites: **63 AGREE, 2 WITHIN-INPUT-PRECISION, 2 DISAGREE — both of them the book quoting an error it is discussing —
and 197 NOT-BOUND**, which are bare fractions with no percentage bound to them and so state no arithmetic claim. The
live golden estate is **86 of 86 green** with the census step green.
