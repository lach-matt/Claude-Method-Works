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
