# Rewrite — Chapter 3, "The twenty-two prime audits, ordered by what a failure costs"

**Treatment (reader-volume reduction).** Chapter 3 is reduced to **§3.0 only** for the reader-facing volume. Everything from §3.1 to §3.9 is workshop material — the histories, self-corrections, and growth of the audit instrument (whitespace measurements, figure dpi, the precedence certificate, how the set grew from 7 to 20). It is not deleted; it is retained in the process/working record where it belongs, and cut from the reader volume. §3.0 alone gives the reader what they need: what is audited, the ten/twelve split, the seven costed audits, and the ordering-by-cost principle.

**Cross-reference dependency map (for write-back).** References to the cut §3.1–§3.9 from material that may survive in the reader volume:

- §2.18, §2.19 (Ch 2) → §3.8 and "§3.1–7". These live in Chapter 2's later protocols, which are themselves workshop-flavoured and likely cut when Chapter 2 is finalised; resolve there.
- **Chapter 18 ("What the law forbids") → §3.7** — the certificate idea ("a certificate is checkable where a search is not"). A genuine reader dependency: when §3.7 leaves the reader volume, this point must be made where Chapter 18 uses it, or the reference re-pointed. **Flagged.**
- **Chapter 21 ("Translation, and what it costs") → §3.7** — same certificate idea. **Flagged.**
- Appendix C → §3.5 (figure dpi distribution). Appendix C is provenance/workshop; resolve when Appendix C is handled.
- Index → §3.7 under "extension". Update the index entry at production.

Self-references *within* §3.1–§3.9 (lines pointing from one cut section to another) leave with the sections and need no action.

---

## 3. The twenty-two prime audits, ordered by what a failure costs

Every session closes with twenty-two audits. They are not spot checks, and they are not equal.

### Ten of the twenty-two test the index; twelve test the book

**For a reader who wants the index rather than the artefact, ten audits carry the whole of it:**

| | audit | what it checks |
|---|---|---|
| 1 | LATTICE | Λ's cells, closure and defect, recomputed from the construction |
| 2 | EQUATIONS | the printed identities re-derived — F(1), F(−1), d(x,y), E |
| 8 | CELL | every cell the text names exists in the index |
| 9 | DISTINCTNESS | no two index coordinates collapse |
| 10 | SCOPE | an E value is stated with the index it belongs to |
| 13 | AGREEMENT | one quantity, one value across the whole work |
| 14 | ARITHMETIC | the tower's own table against the recomputed tower |
| 18 | REPRODUCTION | the two headline figures reproduce |
| 20 | PROJECTION | no claim of predictive power anywhere in the text |
| 21 | INPUT | every computation names its input set |

    These ten would still have to pass if the book were rewritten from scratch in another form. They
    are about Λ and the objects around it.

**The other twelve test whether this book is a usable artefact** — CONSISTENCY, REDUNDANCY, ARTEFACT, COHERENCE, ATTRIBUTION, ANTECEDENT, MARKUP, ENUMERATION, FIDELITY, MEASURE, SEQUENCE and CENSUS. Every one has caught something real. But a reader assessing the mathematics does not need to know that a § reference resolves or that a figure count matches; those protect the reader from the author.

    The split is stated rather than enforced. All twenty-two run on every build, and the artefact twelve
    have caught more faults than the index ten — which is the honest reason not to demote them.

**The twenty-two are ordered by the cost of the failure each one catches.** The first two can make the book *wrong*. The next two can make it *unreadable as an argument*. The next two can make it *unusable as an object*. The seventh can make it *dishonest*, and it is the only one that cannot be run by reading the book.

**1 — LATTICE.** Every structural claim recomputed from the construction: closure under join and meet, E(X) = 0, rank modularity, the fibre identities, the rank polynomial, F(1) and F(−1), the join-irreducible count and the height. Over all 475,800 pairs of Λ, not a sample. First, because if the object is not closed the book has no subject.

**2 — EQUATIONS.** Every equation the book states, evaluated numerically against the data it claims to describe — all of them, including the ones unchanged since the session that first wrote them. Second, because a wrong equation is a false claim.

**3 — CONSISTENCY.** No two statements in the book may contradict. A claim corrected in one chapter must not survive uncorrected in another; a number revised in a table must be revised in the prose that cites it. Third, because a contradiction leaves the reader unable to tell which statement is the claim.

**4 — REDUNDANCY.** No statement may survive its own supersession. Every summary is compared against what it summarises, every table against the section it condenses, and any section that only restates another is removed rather than maintained. Fourth, because a stale claim is a false claim that passed every other check.

**5 — ARTEFACT.** Audits 1–4 read the *source*; this one reads the built PDF. Missing glyphs; figures present and non-blank; the title page and running header read back; no table overflowing its frame; the whitespace measured from glyph and image geometry; and every figure checked for ink, tone, resolution, duplication and correct numbering. Fifth, because the source can be perfect and the page still wrong.

**6 — COHERENCE.** Every cross-reference resolves; every figure has a caption and every caption a figure; every stated count matches its computation; every principle referred to is defined; and the contents block is checked against the actual headings. Placed last of the argument-level audits, because these failures cost navigation rather than truth — and because it is the only audit that can be run before the others.

**7 — ATTRIBUTION.** Every claim that points outside the book resolves to a source the book lists, and every source listed is claimed by something inside it. Five checks: each work cited in the text appears in the References; each entry in the References is cited somewhere; the owner column of §29.2 names people the References carry; every Appendix D element recorded as *precedent found* has a reachable citation; and every data source in Appendix B is listed. Seventh, because a missing attribution makes the book neither wrong nor unreadable nor unusable — it makes it **dishonest**, which is a worse failure and a quieter one.

    Audits 1–2 check the book against the world. Audits 3–4 check the book against itself. Audits 5–6
    check the book against what a reader receives. Audit 7 checks the book against what it owes, and it
    is the only one of the seven that cannot be run by reading the book.