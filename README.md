# Claude-Method-Works
all works for the books

## What is here

[`drive/`](drive/) is a mirror of two Google Drive folders:

| Path | Contents |
| --- | --- |
| [`drive/The Method Materials/`](drive/The%20Method%20Materials/) | The working materials, plus the `COWORK`, `LOWDIN-DELIVERY-1` and `THREEBODY-DELIVERY-1` subfolders |
| [`drive/The Method Prints & Proofs/`](drive/The%20Method%20Prints%20%26%20Proofs/) | Prints and proofs |
| [`drive/MANIFEST.tsv`](drive/MANIFEST.tsv) | File-by-file inventory: repo path, Drive id, title, size, modified time, md5, status |

**819 of the 823 Drive files are mirrored, every one verified by md5.**
[`drive/MANIFEST.tsv`](drive/MANIFEST.tsv) inventories them; [`drive/PENDING.tsv`](drive/PENDING.tsv)
lists the four still outstanding with a reason each. Two are the 370 MB `conversations.json` exports,
which exceed GitHub's 100 MB per-file limit and need sharding rather than transferring. Two are
same-folder duplicates of files already mirrored, reachable only by Drive id.

See [`drive/README.md`](drive/README.md) for the detail.

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
* [`tools/audit_lambda.py`](tools/audit_lambda.py) — every reconstructible numeric claim about Λ,
  checked against the volumes: 61 checks, 59 pass, three findings written up in
  [`docs/AUDIT-LAMBDA.md`](docs/AUDIT-LAMBDA.md). It adjudicates nothing.
* [`tools/audit_mc.py`](tools/audit_mc.py) — the Mathematical Compendium's non-Λ claims: 24
  checks, 23 pass. All 18 section object counts and the eighteen roots reproduce, as do all three
  of Λ_law's ordering figures.
* [`tools/audit_pc.py`](tools/audit_pc.py) — the Physics Compendium: 19 checks, all pass. Λ_phys's
  27 parameters are cross-checked against their own summary table, which is an independent
  statement of the same thing.
* [`tools/audit_sc.py`](tools/audit_sc.py) — the Spectra Compendium and the Löwdin solution it
  carries: 16 checks, 15 pass. The two supplies state the same quantities, so each checks the other.
* [`tools/audit_main.py`](tools/audit_main.py) — the main volume's structure: 15 checks, 13 pass.
  The contents and the body are independent statements of one structure, so each checks the other.
* [`tools/audit_ioi.py`](tools/audit_ioi.py) — the Index of Indices against the volumes it
  indexes: 18 checks, 17 pass. Λ₉'s composable count and Λ₁₀'s g = 0 cells are recomputed from the
  objects rather than compared.
* [`tools/audit_math.py`](tools/audit_math.py) — the book's own mathematical objects read as an
  index in five languages. All 24 fibres close at E = 0; the grading alone gives a counterexample
  to the agreement theorem's "only if" half.
* [`tools/sweep.py`](tools/sweep.py) — the class sweep of RUL-152 item 2: the thirteen classes
  of `DEFECT-CENSUS.tsv` run over the four compendia that close by sweep rather than by reading.
  Every detector is calibrated against the census's own rows — `--selftest` asserts eleven exact
  reproductions — and a class whose predicate cannot be recovered is reported NOT-RUN rather than
  guessed. See [`docs/SWEEP.md`](docs/SWEEP.md).
* [`tools/register_counts.py`](tools/register_counts.py) — keeps the Register's own entry counts
  current: counts it, checks the front and back matter against it, exits 1 on drift, and `--write`
  emits a corrected copy without ever writing in place.
* [`tools/close_main.py`](tools/close_main.py) — the guarded build of the **main** bundle, for
  Register entries and its counts. `close.py` writes only the compendia bundle; this is the missing
  half, to the same discipline: append, recount, assert no other member changed, and reverse
  everything to recover the old bundle's md5 before writing.
* [`tools/reseat.py`](tools/reseat.py) — replaces a seated member's body under the same reverse
  guard. `close.py` adds members and grows append-only ones but by design refuses to rewrite one;
  this is what a revised document needs.
* [`tools/restage.py`](tools/restage.py) — rebuilds `method/members/`, `MEMBER-INDEX.tsv` and
  `verify.py` from the live bundles after either close, asserting the extraction by splicing every
  member back and recovering each bundle's own md5.

## Working with Claude here

Once the one-time setup in [`.github/CLAUDE_GITHUB_SETUP.md`](.github/CLAUDE_GITHUB_SETUP.md) is
done, you can mention `@claude` in this repository — in an issue comment, a pull request comment
or review, or the title or body of a new issue — and Claude will pick up the thread and reply
there. The setup is owner/admin work: install the Claude GitHub App on the repo and add the API
key secret. `CLAUDE.md` at the repo root holds the conventions Claude reads on every run.
