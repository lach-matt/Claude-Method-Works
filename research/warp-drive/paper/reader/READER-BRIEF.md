# Brief for an independent reader of a chapter of the reader's edition

You are an independent line-by-line reader. You did not write the chapter, and you change nothing in it: you read,
check and report. Read `STYLE.md`, `OUTLINE.md`, `WRITER-BRIEF.md` (and `WRITER-BRIEF-S.md` for files 20–48 and 60)
in this directory first: they are the contract the writer worked to.

## What to check, line by line

1. **Fidelity.** Every definition, statement, hypothesis, constant and formula is the sources' final mathematics: the
   chapter's entry in `maps/outline-M.md` or `maps/outline-S.md` names the source ranges, the folds (amendments that
   must be applied) and the exclusions. Open the source at each result and compare. Report anything strengthened,
   weakened, dropped, altered, or taken from text the map marks as replaced.
2. **Proofs.** Every step of every proof is justified inside the edition: by an earlier step, a result of the edition
   cited by its key, a published result stated exactly (in the chapter or the literature appendix), or a derivation
   written in the text. A step that rests on "as in the source", on a computation, or on nothing is a finding.
3. **New derivations.** The author ruled that the edition contains no code, so writers replaced program checks by
   written derivations, many of which do not exist in the sources. Check each one completely: redo the algebra, and
   use computer algebra privately (sympy, in a scratch directory under the session scratchpad, never in the
   repository) to confirm identities, counts and bounds. A wrong derivation is a Major finding.
4. **Self-containedness and the contract.** No file or program names, no process language, no computation words;
   `python3 lint.py <chapter>` hits other than `[[pending:…]]`; every `[[pending:…]]` either names a real cross-chapter
   gap or hides a problem (say which); cross-references point to the right results.
5. **Readability for the field.** Notation defined before use; the argument followable by a mathematician in general
   relativity without the sources.

## Report

Write your report to the path in your prompt: findings numbered, each graded **Major** (a mathematical error, a
missing or unjustified step, a fidelity change), **minor** (imprecision that does not change the mathematics), or
**nit**; each with the chapter line, the source file:line where relevant, the evidence, and the fix you propose. End
with a verdict: **CONFIRMED** (no Major, no minor), or **NOT CONFIRMED** with the counts. Be complete: a second reading
round will check only what you report and the fixes made for it.
