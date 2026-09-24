# The paper contract

Every paper under `papers/method/` is built to this contract. It is the build's own instruction file
and is not published.

## 1. What a paper is

A professional research paper, complete in itself, for readers who know mathematics and physics and
have never seen the books it is drawn from. It states every definition it uses, states every result
in full, proves every result it claims, and machine-checks every claim that has a finite, decidable
form. It carries its own abstract and its own references. Nothing in it points at the books, their
chapters, their registers, their builds, their instruments or their working record.

The model is the hierarchy-law paper at `research/warp-drive/paper/THE-HIERARCHY-LAW.md`: read its
§0, §1, §10 and its status vocabulary before writing anything.

## 2. Layout

```
papers/method/<NN>-<slug>/
  PAPER.md        the paper, the only published text
  check.py        the machine checks: every stated number and every decidable claim
  figures/        the figures the paper embeds, PNG or SVG
  figures.py      regenerates every figure in figures/ that is computed (optional if none is)
  FIGURES.tsv     one row per figure: file, what it shows, how it was made or where it came from
  SOURCES.md      internal provenance map, NOT published: which passages of the books each
                  section draws on, what was corrected, what could not be reproduced
  AUDIT.md        written by the audit stage, not the drafter
```

## 3. Structure of PAPER.md

```
# <Title>
**<one-sentence thesis in bold>**
**Matthew Lach** · Independent Researcher · <day month year>
---
## Abstract
## §0 · The result            (what is claimed, what is not, the status words used)
## §1 · Definitions           (D1, D2, … every object before it is used)
## §2 … §k                    (lemmas, theorems, proofs, figures, tables)
## §k+1 · Verification record (a table: object · PROVED · EXHAUSTIVE · SAMPLED · MACHINE-CHECKED,
                               the families exhausted, the boxes checked, the obligation count,
                               the two guards, what is not machine-checked and why)
## References                 (real literature, full author lists, no citation of the books)
```

Sections are numbered `§n` and referred to as `§n` — those marks are the paper's own. Results are
numbered within their kind: Definition D1, Lemma 1, Theorem 1, Corollary 1, Figure 1, Table 1.

## 4. Mathematical completeness

- Every symbol is defined before it is used, in a numbered definition.
- Every lemma, theorem, law and corollary is stated in full and then proved in full. No "clearly",
  no "it is easy to see", no "by a standard argument" without the argument. A proof ends with ∎.
- A result taken from the literature is stated, attributed with the full author list and year, and
  marked CITED; it is not re-proved unless the proof is short and the paper needs its shape.
- Every number the paper prints is either recomputed by `check.py` or marked CITED with its source.
- A claim the source material states that `check.py` cannot reproduce is not printed. It goes in
  `SOURCES.md` with the measured value beside the stated one. A finding is recorded, never repaired:
  the drafter does not "fix" the source, and does not alter a check to make a discrepancy vanish.
- Where the record has since corrected a claim of the books, the paper carries the corrected result
  and `SOURCES.md` names the correction.

## 5. Status vocabulary (exactly these, never merged)

| word | meaning |
|---|---|
| **PROVED** | a proof is written out in the paper and every step is justified |
| **MACHINE-CHECKED** | Z3 returned `unsat` on the negation of an obligation whose variables range over every subset of a named finite box, with both guards passed |
| **EXHAUSTIVE** | a decision procedure visited every case in a stated finite family |
| **SAMPLED** | a seeded pseudorandom sweep of a stated size; never exhaustive |
| **CITED** | taken from the literature, with the source |
| **REFUTATION** | a claim disproved by an explicit witness |
| **MEASURED** | a number computed from cited data by a stated procedure — the paper's own result, with its sample stated; never a proof, never merged with PROVED |

A machine-checked claim names its box. A sampled figure names its size and seed. "300/300" without
a box or a seed is not a status.

## 6. The machine checks (`check.py`)

- stdlib only, plus `z3` (`pip install z3-solver`). Python 3.12 (`export PATH="$PWD/method/bin:$PATH"`).
- Imports `research/warp-drive/prover.py` by path for every lattice/order obligation, and every
  seated instrument it needs by path (`method/members/tower-2.py`, `tools/cypher.py`'s ℛ, …).
  **An instrument imports a seated member; it never copies one.**
- Every z3 obligation runs the two guards first — non-vacuity of the hypothesis and encoding
  fidelity against an independent concrete implementation — and refuses to report if either fails.
- Exact arithmetic: `fractions.Fraction`, never floats, for every identity. A polynomial identity
  is checked on a grid exceeding its degree in every variable (see `research/warp-drive/proofs.py`).
- Exhaustive checks name the family and print its size. Sampled checks print size and seed.
- `python3 check.py` prints one line per obligation and a summary; exits 1 on any failure.
- `python3 check.py --selftest` includes a **negative control**: a deliberately false claim that
  must be reported as refuted, so a green run is evidence and not a restatement.
- The paper's verification record is generated from or checked against `check.py`'s output.

## 7. Figures

- Prefer a figure the tree already holds and has audited: `method/PROOF-FIGURES.tsv` names the
  file behind every figure of the books that passed its caption check. Copy it into `figures/`
  and record the source path and md5 in `FIGURES.tsv`.
- A figure computed for the paper is made by `figures.py` from the same data `check.py` verifies;
  never drawn by hand; matplotlib is available.
- A caption states facts only, and every number in a caption is in `check.py`.
- A figure whose data disagrees with the paper's text is not used.

## 8. Forbidden in the published text

The site cites nothing from the unpublished books, and the site's build guard refuses any string
that does. `lint.py` enforces the guard's patterns and the following. None may appear in `PAPER.md`
or a caption:

- register numbers ("register 401"), chapter or section numbers of the books, build numbers,
  script or data-file names, member names, the phrases "The Method 1.6", "the book", "this book",
  "the volume", "the compendium", "the corpus", "the record", "the store", "handoff", "docket",
  "ruling", "seated", "bundle", "working register";
- process narration: "an earlier draft said", "this section previously read", "withdrawn",
  "corrected here", "recorded rather than repaired", "M ruled";
- work labels: PINNED, RECOVERED, RECONSTRUCTED, HELD, BANKED, W-nnn, FINDING-, DEF-, RUL-, and
  MEASURED / INFERRED used as provenance tags in the working record's sense. (MEASURED as a
  declared status word of §5, for a paper's own measured result with its sample stated, is allowed.)
- the words "warp" and the research tree's directory name;
- file paths and extensions (`.py`, `.md`, `.tsv`, `.csv`).

What a paper may say instead: "the data", "the index", "the atomic index Λ", "the atomic
spectra data of NIST", "the electron-configuration lattice". Provenance outward is public sources
(NIST ASD, arXiv, DOI, the literature).

## 9. Voice

Third person, present tense, professional. Short sentences. No hedging, no filler, no
self-reference to the writing. The hierarchy-law paper's §0 is the register to match. Unicode
mathematics (Λ, ℛ, ⟨X⟩, ≤, ∧, ∨, ∏, √, subscripts), no LaTeX; a displayed formula goes in an
indented block or a fenced block; inline symbols in backticks where they carry subscripts that
would otherwise be lost.

## 10. The audit stage

Every paper is audited after drafting, and the audit is written to `AUDIT.md`:

1. **Content audit** — every definition, lemma, theorem and number read against the source
   passages named in `SOURCES.md` and against `check.py`'s output; every proof read step by step.
2. **Reader audits** from three points of view, each written as that reader would write it:
   a mathematician who has never seen the material; a physicist who works with atomic spectra;
   a referee for a journal in the paper's field. Each names what is unclear, unproved, unmotivated
   or wrong, with the line.
3. **Lint** — `python3 papers/method/lint.py <dir>` clean.
4. **Render** — `python3 papers/method/render.py <dir>` produces the PDF that is reviewed.

A finding in an audit is fixed in the paper by the drafter and re-audited; the audit record keeps
both the finding and its disposition.
