# Claude-Method-Works
all works for the books

## What is here

[`drive/`](drive/) is a mirror of two Google Drive folders:

| Path | Contents |
| --- | --- |
| [`drive/The Method Materials/`](drive/The%20Method%20Materials/) | The working materials, plus the `COWORK`, `LOWDIN-DELIVERY-1` and `THREEBODY-DELIVERY-1` subfolders |
| [`drive/The Method Prints & Proofs/`](drive/The%20Method%20Prints%20%26%20Proofs/) | Prints and proofs |
| [`drive/MANIFEST.tsv`](drive/MANIFEST.tsv) | File-by-file inventory: repo path, Drive id, title, size, modified time, md5, status |

**822 of the 826 Drive files are mirrored: 819 verified against Drive's own md5, 3 adopted by another route (`ok-adopted`).**
[`drive/MANIFEST.tsv`](drive/MANIFEST.tsv) inventories them; [`drive/PENDING.tsv`](drive/PENDING.tsv)
lists the four still outstanding with a reason each. Two are the 370 MB `conversations.json` exports,
which exceed GitHub's 100 MB per-file limit and need sharding rather than transferring. Two are
same-folder duplicates of files already mirrored, reachable only by Drive id.

See [`drive/README.md`](drive/README.md) for the detail.

## The index as a website — [`public/`](public/)

A zoomable reading of the index: the drawn periodic layout at the top, each element opening into its
ions, channels and cells, every value badged with its status. `python3 tools/webindex.py` writes
`public/data/` from the instruments; serve `public/` from any static host. See
[`docs/WEB-INDEX.md`](docs/WEB-INDEX.md).

## Everything the mirror had sealed — [`extracted/`](extracted/)

Thirty-one of the mirrored files are archives and nine are Claude project exports. Between them they
held **2,504 file occurrences** that no search over the tree could reach, because they sat inside
`.zip`, `.tar.gz` and JSON `content` fields — instruments, transcripts, figures and data tables
alike.

[`tools/consolidate.py`](tools/consolidate.py) unpacks all of them and writes each distinct body
**once**: **779 files, 57.4 MB** — 384 `.py` instruments, 4 session transcripts, 80 figures,
189 data tables and the 2_13 restore-point data set.
[`extracted/LEDGER.tsv`](extracted/LEDGER.tsv) holds one row per source occurrence saying where it
resolved to, so 188 MB of duplicate content became a pointer instead of a second copy.
[`extracted/PROJECT-INDEX.tsv`](extracted/PROJECT-INDEX.tsv) lists all nine projects.

It is a generated tree: regenerate with `python3 tools/consolidate.py`, check with
`python3 tools/consolidate.py --verify`, and never hand-edit it. `drive/` remains the mirror of
record and is not written to. See [`extracted/README.md`](extracted/README.md) and
[`docs/CONSOLIDATE.md`](docs/CONSOLIDATE.md).

What is *not* here is now written down too. [`tools/coverage.py`](tools/coverage.py) resolves every
artefact the books name against the whole repo: **1,005 names — 559 held, 15 held under a figure's
pre-rename source name, 431 absent.** All 33 main-volume figures are present, and `method/verify.py`
still passes on 343 members, so the corpus itself is complete; what is missing is working material —
68 of the 88 handoffs the books refer to, 71 reading slips, and the papers' 25-file `f<N>_<M>.png`
figure set. Nearly all of it would be in the two 388 MB chat exports still listed in
`drive/PENDING.tsv`. See [`docs/COVERAGE.md`](docs/COVERAGE.md).

## Getting the rest — and keeping it in sync

* [`docs/DRIVE-SYNC.md`](docs/DRIVE-SYNC.md) — how to get Drive content into this repo: the four
  routes, the full setup walkthrough, and the limits and gotchas.
* [`tools/drive_sync.py`](tools/drive_sync.py) — the recommended route. Streams downloads (no size
  limit), skips unchanged files, regenerates `drive/MANIFEST.tsv`. Run `--help` for the flags.
* [`tools/drive_sync_colab.ipynb`](tools/drive_sync_colab.ipynb) — the same sync from a browser,
  with nothing installed locally: Colab mounts Drive, copies, commits and pushes.
* [`tools/shard_conversations.py`](tools/shard_conversations.py) — turns a 370 MiB
  `conversations.json` export into one small JSON file per conversation (or one `.gz`), so git
  can hold it.
* [`docs/REPO-SIZE.md`](docs/REPO-SIZE.md) — size audit against GitHub's limits, and when Git LFS
  would actually be worth it.
* [`tools/consolidate.py`](tools/consolidate.py) — unpacks the archives and project exports in
  `drive/` into `extracted/`, deduplicated against the repo and against itself, with a full
  provenance ledger. See [`docs/CONSOLIDATE.md`](docs/CONSOLIDATE.md).
* [`tools/coverage.py`](tools/coverage.py) — the other half of the question: for every artefact the
  books name, is it here? Writes [`COVERAGE.tsv`](COVERAGE.tsv). See
  [`docs/COVERAGE.md`](docs/COVERAGE.md).
* [`tools/recover.py`](tools/recover.py) — extracts the artefacts the chats wrote into
  [`recovered/`](recovered/): 2,337 files, 71 handoffs, 68 reading slips. See
  [`docs/RECOVER.md`](docs/RECOVER.md).

The mirror is one-way: Drive → repo. Edits made under `drive/` are not pushed back to Drive and will
be overwritten by the next sync.

## Instruments

The repository is a document corpus, not a software project — but a few real programs run against
it, each with a real contract and a self-check.

* [`method/verify.py`](method/verify.py) — the witness check for the store of record. Asserts every
  member's md5 and splices each one back into its bundle to recover the bundle's own md5.
* [`tools/cypher.py`](tools/cypher.py) — the cypher analysis of §33 run as a program: ask each
  language of a declared roster whether it can speak of an index, and read the answer off the
  pattern of who answers and who does not. `--selftest` asserts the corpus's own recorded numbers.
  See [`docs/CYPHER.md`](docs/CYPHER.md).
* [`tools/arith.py`](tools/arith.py) — the arithmetic audit of `DOCKET.md` §2 run as a class over
  whole members: every ratio, percentage, equation chain and pair count the volumes state about
  themselves, recomputed in `Decimal` under a named convention. Only `DISAGREE` and
  `ROUNDING-SENSITIVE` are findings; a fraction and a percentage sharing a line are `NOT-BOUND`
  until the text binds them. See [`docs/ARITH.md`](docs/ARITH.md).
* [`tools/pointers.py`](tools/pointers.py) — the pointer audit: every `§`, chapter, appendix,
  register, theorem and figure pointer resolved across all six volumes plus the companion, as
  sources and targets at once, under both resolvers and to the body occurrence. Answers census
  classes C1, C2, C3 and C5. See [`docs/POINTERS.md`](docs/POINTERS.md).
* [`tools/buildtrace.py`](tools/buildtrace.py) — provenance across the BUILD series. Starts from
  `drive/MANIFEST.tsv`, bisects for the first archived build carrying a string in about eight reads
  instead of 107, and states its byte budget before touching the tree. See
  [`docs/BUILDTRACE.md`](docs/BUILDTRACE.md).
* [`tools/populate.py`](tools/populate.py) — an element on every axis of every index. Give it a
  ground-state atomic number and it returns that element and every ion of it: the observed ground
  configuration, the per-subshell quantum axes, the three layout indexes, the Rydberg channels of
  the spectra index, the Pauli bound, the quantum defect under the method equation, and the Λ₈
  transition cells of its ionisation ladder with the caps each one needs. Runs **both halves of the
  method equation** (register 1206) — ℛ places the cells, the channel equation values them. See
  [`docs/POPULATE.md`](docs/POPULATE.md).
* [`tools/lowdin_walk.py`](tools/lowdin_walk.py) — the Löwdin solution's entrant walk,
  **reconstructed**: the record's own chain (`THE-LOWDIN-SOLUTION-2.md` §II.2) with the
  Koelling–Harmon equation and one constant, run in a local-exchange field — not the record's
  Hartree–Fock, whose code never arrived — at c = 137.035999 and c → ∞, into
  [`LOWDIN-WALK.tsv`](LOWDIN-WALK.tsv). Every value is RECONSTRUCTED and placed beside the record's
  READ result, never in its place; its selftest is exact hydrogenic and Dirac levels plus a
  deliberate failure mode. See [`docs/LOWDIN-WALK.md`](docs/LOWDIN-WALK.md).

Every one of them runs `--selftest`, whose fixtures are the corpus's own recorded numbers, and every
one is stdlib-only so an audit can run it from any tree.

## Working with Claude here

Once the one-time setup in [`.github/CLAUDE_GITHUB_SETUP.md`](.github/CLAUDE_GITHUB_SETUP.md) is
done, you can mention `@claude` in this repository — in an issue comment, a pull request comment
or review, or the title or body of a new issue — and Claude will pick up the thread and reply
there. The setup is owner/admin work: install the Claude GitHub App on the repo and add the API
key secret. `CLAUDE.md` at the repo root holds the conventions Claude reads on every run.
