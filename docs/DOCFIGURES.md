# `tools/docfigures.py` — do the repository's own documents still state true numbers?

`arith.py` checks the arithmetic the volumes state about themselves. This does the same for the
documents that describe **the repository** — `CLAUDE.md` and `docs/` — and it exists because they
went stale without anyone noticing.

```
python3 tools/docfigures.py --selftest    # assert the checks' structure and the corpus's invariants
python3 tools/docfigures.py               # the drift report; exit 1 if anything moved
python3 tools/docfigures.py -v            # same, every row printed
```

**88 pinned figures, ~4 s, stdlib only.** Fast enough to run at the top of a session.

## Why it exists

`CLAUDE.md` said **559** artefacts held against **431** `ABSENT`. The instrument measured **702** and
**4**. `extracted/` and `recovered/` had landed 143 of them and nothing updated the prose, so the
entry-point document — the one every chat reads first — **overstated the gap by two orders of
magnitude**. A session that trusted it would have gone looking for hundreds of files the repository
already holds.

Four more had drifted the same way, all found in the same pass:

| document said | measured | what happened |
|---|---|---|
| `recovered/` **2,337 files** | **2,382** | 2,337 is a superseded first run that was not idempotent; `docs/RECOVER.md` records why, and `CLAUDE.md` was still quoting the old figure |
| **94** `__<driveFileId>` duplicates | **99** | five more arrived with later syncs |
| figure bundles **BUILD8 to BUILD13** | **three: 8, 9, 13** | a range was written where a set was meant |
| `READ-*` **48 held**, `HANDOFF-*` **12 held** | **114** and **54** | recovery landed and no document said so |

None of these is a fault in the corpus. **The tree was right and the sentence was old**, every time —
which is exactly why a count in prose needs a program behind it.

## What a row is

Each row pins a **claimed** value beside a **measurement**, and is `STALE` when they differ. The
claim is the number a document states; the measurement is taken from the tree, a manifest or a
ledger. The report names the document to read.

Coverage: the member count and both bundles' recovery; `drive/`'s manifest, its bijection and its
`PENDING`; `extracted/`'s occurrences, bodies and bytes; `recovered/`'s files, rows and truncations;
the chat export's conversations and messages; all six `COVERAGE.tsv` statuses; the BUILD series'
counts and ranges; the `__<driveFileId>` count; and the row counts and headline verdicts of
`PROSE-ONLY.tsv`, `RETRACTION-AUDIT.tsv` and `REGISTER-GAPS.tsv`.

## The instrument totals, and why they needed a separate check

The last fourteen rows come from `pointers.py --json` and `arith.py --json`: 1,932 pointer tokens
across seven verdicts with 42 findings, and 235 arithmetic claims across four verdicts with 2.

**Their own selftests do not cover these.** `pointers.py --selftest` checks 53 fixtures and
`arith.py --selftest` checks 42, and every one of them is an individual **site** — this token
resolves there, this fraction computes to that. A change in a corpus-wide **total** passes both
without a word. `docs/POINTERS.md` and `docs/ARITH.md` state those totals in prose, which is exactly
the position `CLAUDE.md`'s coverage paragraph was in when it went stale. Both documents are currently
correct to the digit; these rows are what will say so next time.

**The finding predicate is neither half alone**, and both halves have been got wrong here. A site is
a finding when it carries a census class **or** its verdict is one of the four the doc names.
`census_class` alone gives **40** and misses `APPSEC`'s two `PREFIX-ONLY`; finding verdicts alone
give **25** and miss the seventeen `REGISTER-RANGE` census rows. Their union is 42 and matches the
text report class by class. The selftest asserts all three numbers, so the mistake cannot return
quietly — I made it once in the course of writing this, read 40 against the report's 42, and was
about to file a bug against `pointers.py --json` that does not exist.

## The pointer row, and why pinning numbers was not enough

One row does not pin a number: **"standing artefacts CLAUDE.md does not name"**, which must be 0.

It exists because the rest of this file could not catch what it is for. On 2026-09-04 an index-based
splice in `CLAUDE.md` deleted five paragraphs — the pointers to `PROSE-ONLY.tsv`,
`RETRACTION-AUDIT.tsv`, `REGISTER-GAPS.tsv`, `HANDOFF-GAP.tsv` and `docs/GRAPH-FINDINGS.md`, 5,757
characters — and **every pinned figure still held.** They were all still *true*. They simply had no
sentence left to be true about. Five standing artefacts became invisible to any future session and
the guard said `all 56 pinned figures still hold`.

So the row checks a different thing: every `docs/*.md`, every top-level `*.tsv` and every
`tools/*.py` must be **named in `CLAUDE.md`**. A file deliberately not pointed at belongs in the
`EXEMPT` map in the source, with a reason, rather than being quietly tolerated. `EXEMPT` is currently
empty — everything is named.

Verified against the real failure: removing one pointer takes the row from 0 to 1.

**The general lesson, which is worth more than the row.** A guard that pins values answers *"is this
number still right?"* and cannot answer *"is this document still whole?"* Those are different
questions and they need different instruments. Ask, of any check: what would a deletion look like
here?

## The two parse rows

Two rows census `.py` files by *parsing* them — never importing, never executing, which matters in a
tree of mirrored and recovered artefacts.

**`seated members needing Python >= 3.12` = 10.** All ten are PEP 701: a backslash inside an f-string
expression, such as `gate.py`'s `t.count(b"\n")`. A `SyntaxError` before 3.12, valid from it. They
are **not corrupt** — they are newer than this container's default `python3` (3.11), and `gate.py`
and `close.py` are among them. Under 3.12 all 117 seated members parse.

**`.py files that parse under NO available interpreter` = 6.** The row runs against the newest
`python3.X` on `PATH` so it is not hostage to whichever interpreter happens to be running
`docfigures`. These six are genuine fragments, all recovered or extracted, none a member.

The distinction is the whole point of having two rows. A first pass at this census reported *34 files
that do not parse* and read it as a recovery-quality problem. It was mostly an interpreter-version
artefact: 28 of the 34 are valid Python that 3.11 refuses. Counting against one interpreter and
calling the result corruption would have been wrong about the corpus and wrong about the tool.

## What it refuses

- **It does not edit a document**, and it does not decide which side is correct. It reports drift and
  names the file. Correcting the prose is a person's call, and on this corpus a `STALE` row is a
  finding — recorded, never repaired by the instrument.
- **It does not pin a claim it cannot check exactly.** Ranges and prose phrases are left alone; a
  check that cannot be made exactly is not made.
- **It never reads the 393 MB chat export.** `coverage.py --chats` owns that, and this stays fast.

## Two traps it encodes, because both have already produced a wrong number here

1. **Grouped headings.** Register entries are headed `### 219, 220, 221` as well as `### N`. A bare
   read gives 1,628 entries where the true count is 1,660, **inventing 32 gaps that are not gaps**.
   The selftest asserts the shortfall is exactly 32, so the trap cannot silently return.
2. **`COVERAGE.tsv` must be the `--chats` run.** A plain `python3 tools/coverage.py` overwrites it
   with a 288-`ABSENT` census and drops every `IN-CHAT` resolution. The selftest asserts `IN-CHAT`
   rows are present, so a degraded file is caught rather than committed.

The selftest also asserts **Ruling 27** directly — the two registers must not overlap — because that
is a property of the corpus rather than a preference, and a violation would mean an entry had been
seated twice.

## When a row goes STALE

Read the named document and correct the sentence, then update the pinned value here in the same
commit. **Do not update the pin alone** — that converts a real finding into a silent one, which is
the failure this instrument was written to catch.

If the measurement itself looks wrong, check it against the tree by hand before changing anything:
three of the five drifts above were found only because a hand count disagreed with the prose, and one
of my own intermediate counts (`drive/` at 822 files) was the wrong number, not the document's — the
manifest's bijection covers the two mirrored roots and excludes `MANIFEST.tsv`, `PENDING.tsv` and
`README.md`, exactly as `CLAUDE.md` says.
