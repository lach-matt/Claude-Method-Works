# PAPER-WORKSHOP.md — how `Cold_Fusion_v1.0` is made and checked

**This file exists because none of it belongs in the paper.**

Matter about the *process* of making a document — the ledger it draws on, the programs that render
and check it, the drafting history, the faults found and fixed on the way — is owed to the record and
not to the reader. A reader of the paper is owed its subject and owes nothing to its production. The
two were mixed in the first draft, in two whole sections and a dozen phrases, and this is where that
matter went.

**The separation is enforced.** `tools/audit_paper.py` runs a **WORKSHOP SEPARATION** check beside the
twenty-five audits, and a paper that has taken any of this back fails it. Its selftest plants a
workshop sentence in the paper to prove the check can fail, because a check that cannot fail is not a
check.

**Why it is beside the twenty-five and not one of them.** The Method's volumes are *about* their own
construction: the register, the audits, the corrections and the process that produced them are the
subject matter. No audit of theirs separates workshop from subject, because in that object there is
nothing to separate. A paper is not like that, so the separation is a requirement of this document and
not of the corpus — the same reason TERM MATCH is run beside the suite rather than inside it.

---

## What the paper is built from

**Every quantity is a ledger row.** `papers/CLAIMS.tsv` carries one row per stated quantity: value,
unit, status, provenance, and the computation that verifies it. `tools/verify_paper.py` runs three
passes over that ledger — it **recomputes** every `DERIVED` row from the instruments, **binds** every
cited constant to the instrument holding it, and fails on any number in the prose that no ledger row
carries.

**The paper's prose states no number of its own.** The source carries `[[C044]]` citations, which
`tools/render_paper.py` resolves against the ledger at render time. A sentence therefore cannot
acquire a figure the mathematics does not produce, because a sentence cannot hold a figure at all.
**This closes a weakness the working papers recorded and did not repair**: pass 3 is a *value* test
and not a *binding* test, and two wrong figures had passed it — three §9 quantities wrong by 1–5
percent, and a 0.855 that should have been 0.854.

**A status is never flattened.** A row's status travels with its value. Where the paper cites a figure
that is `WITHDRAWN`, `RECONSTRUCTED`, `PROJECTED`, `ASSUMED` or a `DESIGN` target, the renderer
**requires** the status to be printed beside it and refuses the citation otherwise. Every bracketed
status in the document is there because the mechanism would not let it be omitted.

**Four outputs, one source.** Markdown, HTML, `.docx` and PDF are emitted from the one resolved text,
which is what makes audit 16 FIDELITY hold by construction rather than by care.

## The residual the mechanism does not close

**The renderer makes a number with no ledger row impossible. It cannot make a citation of the *wrong*
row impossible.** That failure mode is real and has occurred: a cell of §5.4's table cited the
delivered work figure at the wider bore where it needed the same figure through the optimised target
— both valid rows, both the right shape, one of them wrong. It was caught by reading the rendered PDF.

**Audit 14 ARITHMETIC now closes most of it** by recomputing every cell of both restatement tables
from its own row and the factor that produces it, and returning FAIL with the cell named when one
disagrees. What remains open is a citation in *prose* rather than in a table, where no arithmetic
relation constrains it. **That is a recorded limit, not a repaired one.**

## Reproducing the paper

```
python3 tools/render_paper.py papers/Cold_Fusion_v1.0.src.md --all
python3 tools/audit_paper.py
python3 tools/verify_paper.py papers/out/Cold_Fusion_v1.0.md
python3 tools/machine.py --selftest
python3 tools/collector.py --selftest
python3 tools/mucf.py --selftest
python3 tools/render_paper.py --selftest
python3 tools/audit_paper.py --selftest
```

The audits are documented in `docs/AUDIT-PAPER.md`, which records what each of the twenty-five means
when the object is a paper rather than the volumes, and the three faults the suite found **in itself**
before it found any in the paper.

## What was removed from the paper, and where each piece went

| removed from | what it was | where it is now |
|---|---|---|
| the date line | a note that every quantity is a citation | above |
| the abstract's last sentence | the ledger and the binding | above |
| §5.1's pull-quote | *"the one place in this work where a model of ours is validated … against our own corpus"* | rewritten to state the validation without naming the corpus |
| §5.3 | *"an earlier reading of this work said otherwise"* | rewritten as a withdrawal of the figures in the superseded preprints, which is a scholarly notice rather than a drafting note |
| §5.4 | *"prices the first of them against the bred-fuel route only … an omission rather than a finding"* | above, in **What the paper is built from** |
| §7.3 | *"an earlier reconstruction of this work had wrong by nearly seven"* | the sourced figure stands; the history is here |
| §9.3 | *"the one figure in this work that the acceptance census rescales"* | rewritten as *a collection factor* |
| §11's opening | *"a finding is recorded, never repaired … what this paper's method forbids"* | the limits stand; the method's rule is here |
| **§12, in full** | *How this paper is verified* — the ledger, the three passes, the renderer, the statuses, the instruments | above |
| **§15, in full** | *The verification record* — the twenty-five audits, the numbering collision, the commands | above and in `docs/AUDIT-PAPER.md` |
| reference 17 | *"the corpus this paper's method and audit suite are drawn from"* | the citation stands; the note is here |

**Two things were kept in the paper deliberately, and they are not workshop matter.** A **withdrawal**
of a figure published in a cited preprint is a scholarly notice a reader is owed. And a **limit** on
what the paper establishes — §11 — is about the subject, not about the process, however much the two
resemble each other in tone.
