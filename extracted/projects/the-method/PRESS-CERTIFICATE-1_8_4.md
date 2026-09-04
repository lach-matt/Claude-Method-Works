# PRESS CERTIFICATE — session 1.8.4 (the press run)
Ruling: **press against the source as it stands — a truthful snapshot, open threads named as open.**
Bank: `restore-point-2_13.tar.gz`, 694 files + 14 dirs, matching certificate C4 exactly.
Network disabled for bash this session; no fetch was attempted and none was needed.

## The six documents, as pressed and measured

| document | pages | searchable chars | U+FFFD | leaked markup | bytes |
|---|---|---|---|---|---|
| The Method 1.6 (book) | 254 | 698,333 | 0 | 0 | 3,767,321 |
| The Register | 239 | 1,116,676 | 0 | **6 (disclosed)** | 1,062,197 |
| Mathematical Compendium | 58 | 179,159 | 0 | 0 | 273,231 |
| The Index of Indices | 39 | 76,945 | 0 | 0 | 968,384 |
| Spectra Compendium | 22 | 71,695 | 0 | 0 | 729,571 |
| Physics Compendium | 12 | 40,898 | 0 | 0 | 126,954 |

## Gates

| | baseline | at close |
|---|---|---|
| prime audits | 25/25 PASS | **25/25 PASS** |
| round-trip | 6/6 PASS | **6/6 PASS** |

The newly pressed book was staged back into the working directory before the closing audit run,
because the PDF is an INPUT to the prime audits and not an artefact copy (R 1004).

## The book was pressed twice, and the second pass is the true one
Pass 1 rebuilt byte-identical to the banked PDF (3,767,085) — the source had not moved since
10 August. `pagemap.py` then located **486 of 487 headings** and rewrote `PAGEMAP.tsv` with
**136 changed lines** against the banked copy. Pass 2 is 236 bytes larger. The banked contents
was stale; it is now true. This is R 665's mechanism, working as designed.

## One repair, fenced and reversible
`press_compendia.py` line 211 only. The blockquote branch rendered one line at a time while the
body branch (since R 632) joins consecutive lines, so a `**bold**` statement wrapped across two
`> ` lines printed its asterisks. The quote branch now buffers the same way.
**Mathematical Compendium: 4 leaks → 0.**
The original line is preserved verbatim in `UNDO-PRESS-REPAIR.txt`; restoring it reverts the change.
No source, no index and no `REGISTER-DATA.md` was touched, so no A.cert operation is involved.
This is R 259's instance-fix pattern: a fix applied to one branch and never to its neighbour.

## Two things disclosed rather than repaired — M's ruling

**1 · Six asterisks in the Register, on 239 pages.** Source lines 5822, 5830, 5834, 5846, 5850,
5866 of `REGISTER.md` — entries in the R 1640s–1660s band. Each is a SINGLE source line of
1,474–3,607 characters carrying an ODD number of `**` markers: a span opened with `**` and closed
with a single `*`. No joining logic can balance a pair that was never balanced. `REGISTER.md` is
generated from `REGISTER-DATA.md`, so repairing it means editing the record; M ruled to leave the
record untouched so the state remains reversible. The affected entries include *THE FETCH QUEUE
CLOSES: 60 OF 60*, *INCORPORATION PHASE 2* and *PHASE 3*, *THE d120 FAILS ON GEOMETRY*, *THE REPLY
ON THE BOUND*, and *TWO DIFFERENT LATTICES ARE BOTH CALLED Λ_spectra*. No claim is altered by the
markup; only its emphasis.

**2 · The §26 register tripwire no longer fires, and that is a finding.** The book press prints
`F.3: E(G) not recomputed: min() iterable argument is empty` at line 533. The block slices §28
Withdrawals and counts entries matching `^\s{0,3}(\d{3})\.\s`. Measured: 3-digit matches **0**,
4-digit matches **0**, any leading number **1**, across 62,835 characters and 44 headings. The
section did not outgrow a numbering — **it no longer prints a numbered entry list at all**. R 633
moved the entries to the Register Compendium and §28 kept the argument as prose, opening *"one
thousand one hundred and seventy-one claims…"* — spelled, not enumerated. Per P8 the failure is a
true answer and therefore a bound: **the book can no longer recompute its own register range at
build.** It fails loudly rather than printing a stale number. The quantity it guarded is now
unguarded, and per the null protocol the gap wants a different instrument — a count read from
`REGISTER-DATA.md`, not a regex over §28 prose. NOT BUILT; it is a change to the book press and
M has not ruled on it.

## Carried unchanged and unhidden
`G.3 tripwire: 2,987 claim-bearing numbers, 1,573 without a provenance cue (53%)`. It reports and
does not fail the build, as F.3.2 rules. `F.3: E(G) = 44 over 6 fibres` and `E.1.2: 9 open items,
E(Q) = 5 unfibred` both recomputed at build and printed.

## What this press did NOT do
No write to `COORDINATES.tsv`, `MEASUREMENTS.tsv` or `REGISTER-DATA.md`. The index stands at
104,832 cells, 7,260 pairs, E = 0, untouched. Board rows 1–5 remain open and are rendered as open:
ladder-as-limit, T8-J width, Kr II, the 93 unwritten series, T9's 65. The ~150,000 unread words
remain named as unread (§H.8 C7).

## The full audit set, run against all six documents (R 994's protocol)

| audit | result |
|---|---|
| prime audits (25) | **25/25 PASS** |
| round-trip (6) | **6/6 PASS** |
| `appendix_audit` | ALL CHECKS PASS |
| `criterion_probe` | PASSES — monotone and exhaustive |
| `cross_audit` (Part 1) | PART 1 PASSES |
| `compendium_audit` (Part 2) | PART 2 PASSES |
| `artefact_audit` (Part 3) | 1 failure — the Register's six, disclosed by ruling |
| `mech_audit` | PASS (repaired, below) |
| `audit_figures` | STAGE 2: 0 failures |
| `check_audit` | 2 self-named fields remain, against 91 at R 849 |
| `math_audit` | 11 of 12 — the 12th is R 849–852's class, below |
| `cypher_audit` · `audit_laws` · `compare_audit` | report by design; findings below |

## Three further repairs, all reversible, none touching the record

**1 · `mech_audit` — the P family restored.** `mathreg.py` held 17, `MECHANISMS.md` 17,
`QUEUE-LOG.md` 17, `QUEUE.md` **zero**: the 1.6.1 rollback rebuilt the queue from transcript and
the list did not survive. Restored from `MECHANISMS.md` with the rollback recorded in the block.
Previous state at `QUEUE.prev.md`. **MECHANISM LISTS AGREE.**

**2 · `artefact_audit` — the Physics Compendium added to Part 3.** R 995's omission, open since
register 901, closed in the second instrument. Physics now reads 12 pp · 40,062 chars · 0 glyphs ·
0 markup · 0 lost statements.

**3 · The figure assertions corrected against measurement.** Index of Indices 4 → **5** (R 993
moved `fig-spectra-lattice.png` into it; five referenced, five render). Spectra 0 → **3**, so an
under-asserted document is no longer silently unchecked. The book's 33 and the Register's 0 were
NOT touched: the book press walks `figures/` rather than reading image tags (0 source refs against
33 rendered), and the Register's single apparent reference is R 1848's own literal example
`![caption](file.png)` — a register entry about figure syntax, read by a regex as figure syntax.
A rule deriving expectation from source refs would have broken the book and swallowed R 1848.
Computed before proposing (P5, §2.14).

## A finding about the instruments themselves — the Zeno cache serves stale verdicts
The widened Part 3 printed five rows twice: `zeno.py`'s `step()` keys on the step's NAME, so
`.zeno/artefact_audit.json` replayed the five-document result after the instrument had been
widened. **An audit rerun after an instrument change must clear `.zeno/` or pass `force=True`,
or its pass is a pass of the OLD instrument.** Cache cleared, step relabelled *the six artefacts*,
sixth row appeared. Same family as R 998 and R 649 — a guard behaving correctly and unhelpfully —
except this one did not fire at all; it answered from memory.

## Findings that belong to the record, not to the press
- **`math_audit`:** 125 objects whose check field says PRIOR ART without measured content —
  R 849–852's class, the compendium overclaiming its own auditing rather than its mathematics.
- **`compare_audit` — three standing contradictions**, one index in two languages:
  δ falls with ℓ (order 194/205 · analysis 102/205); triplet exceeds singlet (55/66 · 33/66, the
  fitted sign OPPOSITE to the measured); δ falls with charge (89/143 · 135/143, the equation MORE
  monotone than the data). R 1169 attributes the first to a noise floor at 11 pairs, which accounts
  for the 11 and not for the 92.
- **`audit_laws`:** law 2 at r² 0.356 on 19 species; law 6 resting on ONE published radius;
  u₀ ≈ 4 untested as a locked value.

## Self-correction, registered not hidden (§H.11)
A parity census run over `REGISTER-DATA.md` returned **3,956 odd-`**` lines and 1,564 "solo"**,
printed in full — a tool return of many hundreds of lines against §H.11's ~25-line clause. Two
things follow. The clause was broken and is recorded as broken. And the measurement itself is
VOID as a fault count: at source level, entries interleave bold, italic and notation asterisks
across wrapped lines, so parity cannot distinguish markup from content — **which register 1565
already established** ("the parity checker cannot tell any of these from an emphasis delimiter").
The six leaks are visible in the RENDERED text and nowhere else. The generated `REGISTER.md`
parity check that found exactly six was the right instrument at the right level.

## Register entries owed, to be written when REGISTER-DATA.md is next opened
- **R 1701** — the ruling: press the source as it stands, a truthful snapshot.
- **R 1702** — the ingestion finding: the six project-knowledge files named `.pdf` are not PDFs.
  Two are UTF-8 text extractions (702,517 and 562,568 chars), four are zips of page rasters
  (56, 38, 20, 12 jpeg). All six fail `pdftotext` with *Couldn't find trailer dictionary*. Had they
  been staged as audit inputs on the strength of their names, FIDELITY and PROJECTION would have
  compared source against a derivative of the artefact. **The R 1672 pattern and the
  `destination_url` guard are one guard: check what arrived, not what it is called.**
- **R 1703** — the press repair to the quote branch, with its undo.
- **R 1704** — the §26 tripwire's empty min(), diagnosed as a bound, instrument not built.
- **R 1705** — `artefact_audit` widened to six documents; R 995's omission closed.
- **R 1706** — the P family restored to `QUEUE.md` from `MECHANISMS.md`.
- **R 1707** — the Zeno step cache serves a stale verdict after an instrument changes.
- **R 1708** — figure assertions corrected to measurement; the derive-from-source rule REFUTED
  before adoption by the book's directory walk and R 1848's literal example.
- **R 1709** — self-correction: §H.11 broken by an unbounded census; the census void by R 1565.

