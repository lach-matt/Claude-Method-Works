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
* [`tools/register_counts.py`](tools/register_counts.py) — keeps the Register's own entry counts
  current: counts it, checks the front and back matter against it, exits 1 on drift, and `--write`
  emits a corrected copy without ever writing in place.
* [`tools/close_main.py`](tools/close_main.py) — the guarded build of the **main** bundle, for
  Register entries and its counts. `close.py` writes only the compendia bundle; this is the missing
  half, to the same discipline: append, recount, assert no other member changed, and reverse
  everything to recover the old bundle's md5 before writing.

## Working with Claude here

Once the one-time setup in [`.github/CLAUDE_GITHUB_SETUP.md`](.github/CLAUDE_GITHUB_SETUP.md) is
done, you can mention `@claude` in this repository — in an issue comment, a pull request comment
or review, or the title or body of a new issue — and Claude will pick up the thread and reply
there. The setup is owner/admin work: install the Claude GitHub App on the repo and add the API
key secret. `CLAUDE.md` at the repo root holds the conventions Claude reads on every run.
