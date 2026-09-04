# THE METHOD 1.7 — HANDOFF

*Written at the close of 2026-08-11. The register is the durable artefact; this
file is a map to it, not a substitute.*

## THE BOARD

**`BOARD.md` is M's view of what is open — one table, eighteen rows.** Update it
whenever an item OPENS, CLOSES or CHANGES KIND, and log the change in its own
change log. **Detail belongs in QUEUE.md; BOARD.md is the view, not the record.**

*M asked for it kept current and handy. It is how he prioritises.*

## 1 · WHAT TO UPLOAD

`restore-point-1_8s.tar.gz` — complete, gated, verified by extraction.
Registers **165–1469, 1,262 entries. ALL TWENTY-FIVE PASS. 5 of 5 round-trip.**

Nothing needs reconstructing from a transcript. That was true this morning and
cost most of a session; see PROVENANCE.md for why, and keep it true.

## 2 · READ THESE FIRST, IN THIS ORDER

    QUEUE.md            the state record: closed, open, and section VII's path
    PROVENANCE.md       which files are original, recovered, rebuilt or absent
    NU-DEACTIVATED.md   what demotes with ν and what does not
    TWO-CHAINS.md       Belokolos beside this work, and the eight gaps
    NU-AND-DELTA.md     why the two objects cannot be joined
    LOWDIN-LITERATURE.md  the field, with attributions and §8's mathematics

## 3 · THE DAY'S SHAPE, IN FIVE LINES

- The bridge from 1.6.1 was rebuilt from prose after that container rolled back.
- ν is **deactivated as a law and retained as a form** (R 1460). The corridor is
  the instrument and survives intact.
- The corridor is **additive representability of a ranked order**; an empty
  feasible set is a **cancellation condition** — Kraft–Pratt–Seidenberg 1959,
  Scott 1964, Krantz–Luce–Suppes–Tversky 1971 (R 1461).
- The form's domain is **where Madelung stops**: it recovers five of Madelung's
  ten exceptions from node counts with nothing fitted (R 1464).
- F2a was run. Two findings EARNED, one correctly FORCED, two weaker than they
  read (R 1469).

## 4 · TOMORROW IS A DIFFERENT TOPIC

The person's instruction: visit a different queue item in the morning and return
to Löwdin later. **Do not open the Löwdin thread unprompted.** Something learned
elsewhere may apply here, and that is the reason for the gap.

Candidates that are ready and independent of this thread:

    ★★ H1   re-coordinatise Λ_spectra on (block, ℓ, charge)   R 1459 — one script
    ★★ D3   Theodosiou, Inokuti & Manson 1986, ~5,100 defects — the biggest lever
    ★★ D2   the ionisation ladders, 15 of 108; next capture K–Kr
    ★  B1   the L-shell lines, to test the nine transition types at a second depth
    ★  G2   Q.exch withdrawn, needs an ℓ-dependent exchange term
    ★★ F2   the book, now **244 entries behind** — highest cited 1225

## 5 · THE PROTOCOLS, AND TODAY'S LESSON ABOUT THEM

Zeno: bounded steps, result written before the next opens, checkpoint when a save
path fails. Domain: never pool across cells. Contingency: **WITNESS · SPACE ·
RATE · VANISHING**, and the space stated BEFORE the run. Roundtrip: DECLARE ·
ISOLATE · DIFF · REFUSE.

**The lesson.** `contingency.py` sat in this tree all day, rebuilt in the morning
and not run on a single finding until the person asked. When it was run it
damaged two of five results and found two faults in itself. Run it on a finding
before reporting the finding, not after.

**And today's errors were all in the newest work, not the oldest** — a sentinel
collision in code written the same hour, a shared "origin" that was my own
default, an atomic claim contradicted twenty minutes later by a theorem I had
just imported. The register caught every one because the corrections were written
in rather than tidied away.

## 6 · WHAT IS OPEN AND GENUINELY HARD

    the amplitude a          R 1311 named its two missing sources the day it was
                             built: electron–electron repulsion and exchange.
                             SIX placement rules have failed. Do not attempt a
                             seventh (R 1460, P4).
    the exceptions           neither this work nor any claimant carries them
    why the onsets are exact K(x) = (1/6)x(x²+2−3µ(x)) reproduces all eight
                             Janet block openings with NO error, and it is
                             nobody's derivation
    AME2020                  cited in five places, held nowhere; blocks
                             E.nuclide = 9 and isotopic_null.py
    xray_index.py            blocked on the eleven candidate coordinates

## 7 · THE RULES

Read orderings from a source · don't invent a cell or column · three axes never
two · an axis is determined when its values form a monotone chain · E = 0 is
informative only where refusal was possible · never fill your own values when the
source is meant to be accurate · before calling a coordinate system new, ask
whether its axes are the parent's letters relabelled · read E as predictions,
not defects · **a result that reproduces a known one is stronger, not weaker** ·
**evidence that disagrees is good too, and localises rather than confirms**.

**Recurring faults.** Reading a pattern in my own output · asserting a relation
without computing it · quoting a check before its null is known · summary
statistics over a series that turns · taking the collection's edge for the
subject's · rebuilding what the restore point already contains.

*The purpose is understanding, shared in book form.*

## M's input material — held at register 1616

`captures/INPUTS-GEMINI.md` holds all six Gemini inputs IN FULL, with a
closing table saying when to reach for each part. It is a SECONDARY ACCOUNT
and nothing in it is a source. The sorted verdicts are in `LITERATURE.md`;
the intake rules are in `INTAKE.md`.

**Live from it:** the temperature axis (board 4b), Rosenzweig-Porter 1960
(board 4a), and the figure-8 benchmark for the three-body chapter.

## The fetch queue — standing, across sessions (R 1637)

`captures/FETCH-QUEUE.tsv` holds **61 species, one request each**, with a
`TODO` column. Mark each `DONE` as its levels arrive.

**One spectrum per request.** `energy1.pl` returns a level table and a level
table is per spectrum. Ranges are `ie.pl` syntax and were rejected six times.

    https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectra=La+I&submit=Retrieve+Data

Minimal form, two parameters. If one returns levels, add `units=1` and
`format=2` for cm⁻¹ and text, one per round.

**Order:** La I and Ce I first — where Madelung fails — then Ac I and Th I,
then by channels wanted.

**Per species, on arrival:** read the limit off its header BY EYE and never
parse it; check the defects for a constant fractional part, which is the
signature of a wrong limit; refuse any channel with no single 2S+1.
