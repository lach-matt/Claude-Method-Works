# `tools/docfigures.py` — do the repository's own documents still state true numbers?

`arith.py` checks the arithmetic the volumes state about themselves. This does the same for the
documents that describe **the repository** — `CLAUDE.md` and `docs/` — and it exists because they
went stale without anyone noticing.

```
python3 tools/docfigures.py --selftest    # assert the checks' structure and the corpus's invariants
python3 tools/docfigures.py               # the drift report; exit 1 if anything moved
python3 tools/docfigures.py -v            # same, every row printed
```

**36 pinned figures, 0.15 s, stdlib only.** Fast enough to run at the top of a session.

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
