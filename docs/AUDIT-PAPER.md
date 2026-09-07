# AUDIT-PAPER.md — the twenty-five audits, run over a paper

`tools/audit_paper.py` runs The Method's own audit suite over
`papers/Cold_Fusion_v1.0.src.md`. This file records what each audit means when the object is a paper
rather than the volumes, because **an audit applied to a different object without saying how is not
the same audit.**

```
python3 tools/audit_paper.py            # the report
python3 tools/audit_paper.py --selftest # each audit against the fault it was built for
```

## Where the twenty-five come from

**Twenty-two are the prime suite**, seated in §3 of `The_Method_1_6_BUILD90_main_and_register.md`
under the heading *"The twenty-two prime audits, ordered by what a failure costs"*. That section
prints four coordinates per audit — what it **reads**, what it **compares against**, what a **failure
costs**, and what it **presupposes** — and `audit_paper.py` carries all four verbatim. §3.0 splits
them: **ten test the index** (LATTICE, EQUATIONS, CELL, DISTINCTNESS, SCOPE, AGREEMENT, ARITHMETIC,
REPRODUCTION, PROJECTION, INPUT) and **twelve test whether the thing is a usable artefact.** The
report marks the ten.

**Three more come from the compendia intake** at §B of
`The_Method_1_6_BUILD180_compendia_papers_audits.md`: **23 PUBLISHED VALUES**, **24 UNBACKED CLAIMS**
and **25 UNGROUNDED COORDINATES**.

## A numbering collision, recorded and not resolved

The live table numbers audit 22 **CENSUS**. The same intake that proposes 23–25 numbers its own first
addition **"Audit 22 — TERM MATCH"**. Both are in the corpus and no ruling this repository holds
supersedes either.

`audit_paper.py` runs **CENSUS as 22**, because that is the one the live volume seats, and runs
**TERM MATCH beside the twenty-five, unnumbered**. The corpus is explicit that TERM MATCH is *external
by construction* and that *its output is a debt, not a pass* — so it could not be one of the
twenty-five even if the number were free. **Flattening the collision would be a decision this file has
no standing to take.**

## The verdicts, and why there are four

| verdict | meaning |
|---|---|
| `PASS` | the check ran and found nothing |
| `FAIL` | the check ran and found a defect — the paper is not fit to issue |
| `DEBT` | the check ran and its output is a debt, not a verdict |
| `N/A` | the check does not apply to an object of this kind, with a reason |

**A DEBT is never reported as a PASS and never counted as a FAIL.** That is the corpus's own handling
and it is the reason both statuses exist: audit 22 TERM MATCH exists *because* twenty-one audits
passed on a document containing five coordinate conflations, and reporting its silence as a pass would
reproduce exactly that failure.

## The translations

| no | audit | what it means for this paper |
|---|---|---|
| 1 | LATTICE | every `DERIVED` row the paper cites, recomputed from the instrument named in its own `verify` column |
| 2 | EQUATIONS | the identities the paper prints — condition 8, the transverse cap, the loss-budget product, the linear restatement — evaluated against the rows it cites |
| 3 | CONSISTENCY | one claim text, one value: no quantity is cited at two figures |
| 4 | REDUNDANCY | a summary that restates a table is reported; a withdrawn row cited without its status cannot reach here, because the renderer refuses it |
| 5 | ARTEFACT | reads the **built PDF**: page count, size, and the title and headings read back out of its own text layer |
| 6 | COHERENCE | every `§N.N` cross-reference resolves to a heading that exists |
| 7 | ATTRIBUTION | a References section exists, and every `MEASURED`/`SOURCED` row cited carries provenance |
| 8 | CELL | every claim id cited exists in the ledger, and no citation is malformed |
| 9 | DISTINCTNESS | no two cited ids are one quantity under two names |
| 10 | SCOPE | a value is stated with the index it belongs to — here, with its **status** |
| 11 | ANTECEDENT | no figure appears in the abstract that the body never carries |
| 12 | MARKUP | tables rectangular and ruled, emphasis closed, no unresolved citation in the rendered text |
| 13 | AGREEMENT | one quantity, one value: the ledger row against the instrument that owns it |
| 14 | ARITHMETIC | the paper's own tables recomputed — the delivered restatement, and the co-product's two corrections |
| 15 | ENUMERATION | a stated count against what it counts: *seven* conditions against a list of seven, *four* stages against four |
| 16 | FIDELITY | the gap between source and artefact, measured: distinctive values probed in **both** the `.docx` and the PDF |
| 17 | MEASURE | geometry from the artefact: pages, words, words per page inside a readable band |
| 18 | REPRODUCTION | the headline figures reproduced from the instruments, from outside the document |
| 19 | SEQUENCE | section numbers ascend, none duplicated, every subsection has its parent |
| 20 | PROJECTION | no claim of predictive power anywhere in the text |
| 21 | INPUT | every `DERIVED` row cited names its input set |
| 22 | CENSUS | spelled self-claims counted against what they count |
| 23 | PUBLISHED VALUES | external reproductions hold, and the published rows cited are carried verbatim |
| 24 | UNBACKED CLAIMS | **any numeral typed into the source prose** |
| 25 | UNGROUNDED COORDINATES | a term used with no referent. Returns `DEBT` by construction |
| — | WORKSHOP SEPARATION | matter about the **making** of the paper — the ledger, the programs, the drafting history — in a document whose reader is owed only its subject. Beside the suite, not inside it: see below |
| — | TERM MATCH | what the cited literature means by a term against what this paper means. `DEBT`, external, never automatable |

## Why WORKSHOP SEPARATION is beside the twenty-five and not one of them

**The Method's volumes are *about* their own construction.** The register, the audits, the corrections
and the process that produced them are the subject matter, so no audit of theirs separates workshop
from subject: in that object there is nothing to separate, and an audit for it would have no work to
do.

**A paper is not like that.** Its reader is owed the subject and owes nothing to the production, so
the separation is a requirement of *this* document and not of the corpus. That is the same reason
TERM MATCH sits beside the suite — and the reason neither is given a number.

The removed matter is in `docs/PAPER-WORKSHOP.md`, which also records the one residual the citation
mechanism does not close: it makes a number with **no** ledger row impossible, and cannot make a
citation of the **wrong** row impossible.

## Audit 24 is the one whose PASS is structural

Every other audit measures. Audit 24's pass is a **fact about how the paper is written**: the source
carries no numerals, only citations, so a numeral found there is either a label or a defect. The
exemptions are therefore the whole of its judgement, and each is a place where a digit **addresses**
rather than **asserts** — a section label, an ordered-list marker, a condition or audit by number, a
claim id, a nuclide, a year, a symbol inside a formula, a named case such as φ = 3, and the whole of
the References section, where a volume and a page address a document rather than stating a quantity.

**It was blind twice and both are fixed.** It read paragraphs and not table cells, so a number typed
into a cell went straight through; and its selftest mutated the source text without re-parsing the
blocks the audit actually reads, so the injected fault was invisible to the very check meant to prove
the audit works. Both are now fixtures.

## A limit of the PDF reader, recorded rather than repaired

Audit 5 reads the built PDF's own text layer. The paper's fonts are **embedded subsets**, and where
two subsets both carry a given code, nothing in this reader says which font a particular run was set
in — that needs the page's resource dictionary, which it does not parse. A symbol drawn from the
second subset may therefore fail to decode, and Greek letters and operators are the ones affected.

**The glyphs are in the file.** reportlab writes a `ToUnicode` entry only for a glyph it has actually
embedded, and audit 5 counts those: the Greek is present. So the audit checks **Latin words and
numerals**, which decode unambiguously, reports the count of embedded Greek glyphs, and **does not
claim to have read the mathematics.** Saying so is the point: an audit that reported "the text layer
reads back" while silently failing on every symbol in §13 would be worse than one that names what it
did not check.

## Three faults the suite found in itself before it found any in the paper

An audit has to be right before its verdict means anything, and three of these were wrong first.

- **ARTEFACT and FIDELITY reported the PDF empty.** The reader was wrong, not the paper. A kerned run
  is a `TJ` array, so joining every string with a space splits words that *are* on the page; an
  embedded font subset writes hex codes in its own encoding, so strings must be decoded through that
  font's `ToUnicode` table; and reportlab's page content is **ASCII85 then Flate**, so a decompressor
  alone finds the fonts and none of the text. All three are now handled.
- **COHERENCE and SEQUENCE reported every section orphaned.** The heading regex required whitespace
  where the paper writes a period, so no top-level section was ever recognised.
- **ENUMERATION and MARKUP reported the conditions list broken.** The renderer's parser treated a
  **wrapped list item** as a new paragraph, which silently turned a seven-item list into two items and
  an unclosed emphasis. Fixed in `render_paper.py`, which is where the fault was.

**Each of those would have been reported as a defect in the paper.** They are recorded here because
the corpus's own rule applies to the instrument as much as to the object: *a finding is recorded,
never repaired* — and an instrument that reports its own limitation as the object's fault is the
failure mode these three share.
