# The reader's edition: contract for writers and readers

This directory builds the self-contained edition of the paper, for readers outside this repository. Its title is
"Five-Dimensional Vaidya Black Holes as High-Frequency Limits of Vacuum Spacetimes", with the subtitle "Large data,
T² symmetry, and settling to Schwarzschild–Tangherlini", by Matthew Lach, Independent Researcher.

`RESPONSE-HL-5D.md` (one directory up) and the supplement under `docket68/` are the internal record. The edition is
written from them and never changes them. This file, `lint.py`, `CROSSWALK.tsv` and the chapter sources are working
files; only the assembled `PAPER.md`, its PDF and the code appendix are published.

## 1. What the edition is

- Self-contained. Every result the theorems rest on is stated and proved in the edition, including the complete
  five-dimensional stability theory. Results from the published literature are cited as theorems of that literature
  (author, year, theorem number, page where useful) and used as such; they are not reproved.
- The mathematics is the record's final mathematics, unchanged. A writer composes the final statement and proof from the
  sources named in the chapter brief (latest form, every amendment folded in), removes the history, and writes it as
  ordinary mathematical prose. A writer never strengthens, weakens or "improves" a claim. Where the sources disagree or a
  step is missing, the writer stops and reports it; the writer does not repair mathematics silently.
- No code whatsoever (the author's ruling). The edition carries no program, no computation citation and no code
  appendix: every step is proved in the text. Where the record supports a step by a program, the edition writes that
  step's mathematics out (the identity and its derivation, the count and its enumeration, the bound and its estimate).
  Writers may check their algebra privately with computer algebra; the text presents only the mathematics. A step the
  record establishes only by a large or floating-point computation, for which no written proof is found, is not stated
  as proved: it is marked `[[pending:computational-N]]` for the coordinator, who decides it with the author.

## 2. Forbidden in the edition (checked by `lint.py`)

- File names, paths and extensions of any kind (`.py`, `.md`, `.tsv`, `.out`, `.json`, `checks/`, `proof5`, `docket`,
  `n1star`, `lemmas/`), program names, label sets of programs (X1–X8, R1–R14 as program labels), md5s.
- The research tree's directory name and the word "warp".
- Process language: verifier, reader (as a reviewer), seated, seating, round(s) of work, pass, final pass, finding,
  Major, minor, nit, repair, amended, superseded, withdrawn, "the record", "the supplement", the author's words,
  commission, brief, workstream, ledger, census, provenance, selftest, mutant, pin, docket, ruling, D-labels (D612),
  round labels (R10.1, [R11-nits]), working names (N1*, SOURCE, "Theorem E" of the record), "M", agent, Claude, AI.
- The record's status tags as tags: "(computed …)", "(deduced …)", "READ", "computed, not certified" as a parenthetical
  label. Say what is true in prose instead: "Computation C12 verifies the identity exactly"; "this follows from Lemma
  5.3"; "[Hin26, Prop. 6.9] states …".
- Narration of how the work was done: "an earlier version", "was found", "was corrected", "now", "at this stage",
  "this paper previously", dates of work.

## 3. Voice and form

- Standard mathematical prose for analysis and general relativity: "we" is used as in the field's literature; present
  tense for mathematics. Definitions, lemmas, propositions, theorems, corollaries and remarks, each proof closed by ∎.
- Short, plain sentences. No filler or rhetoric: no "crucially", "importantly", "it is worth noting", "delve",
  "leverage", "seamless", "in essence", "Let us now turn to". No bold except result headings and defined terms.
- Mathematics in Unicode in running text (φᵢⱼ, x², ∂_θ, ≤, ∫, √), displayed formulas in an indented block or a fenced
  block. No LaTeX. A backtick span is for nothing in the edition (it renders literally).
- Lines of at most 121 characters in the source files.

## 4. Labels and numbering (resolved at assembly)

Chapters are written in parallel, so numbers are symbolic in the chapter sources and fixed by `assemble.py`:

- A result: `**Theorem {#thm:key}** (Optional title.)` — also `lem:`, `prop:`, `cor:`, `def:`, `rem:`. Assembly prints
  "**Theorem 12.3**".
- A displayed equation ends with `{#eq:key}` on its last line; assembly prints "(12.7)".
- A chapter or section heading ends with `{#ch:key}` or `{#sec:key}`.
- A reference: `[[thm:key]]`, `[[eq:key]]`, `[[ch:key]]`, `[[sec:key]]`, printed "Theorem 12.3", "(12.7)",
  "Chapter 12", "Section 12.4". Keys are lowercase words joined by hyphens. Exported keys (results other chapters use)
  are fixed in `OUTLINE.md`; a chapter may define private keys freely.
- Literature: `[Hin26, Theorem 6.9]` with the bibliography keys of `OUTLINE.md`.

## 5. The appendix

- **Appendix A. Results from the literature.** Each published result the proofs use as a black box, stated exactly,
  with its source, number and page. There is no other appendix: no computations and no code.
