# Drive mirror: The Method folders

Byte-exact copies of the Google Drive folders **The Method Materials** (with its subfolders COWORK,
LOWDIN-DELIVERY-1, THREEBODY-DELIVERY-1, CORPUS, BUILD175-PARTS, Claude Memories, Claude Metadata,
Claude Projects and Claude Chats) and **The Method Prints & Proofs**.

**820 of the 824 Drive files in scope are mirrored here.** 819 were verified by md5 against the copy
Drive served; one, `The Method Materials/warp drive theory.pdf`, was seated by `drive_sync.py
--adopt` and carries status `ok-adopted` because the route that fetched it returned no Drive md5 to
compare — its byte count was checked and nothing more. The four still outstanding are listed in
`PENDING.tsv` with the reason for each.

* `MANIFEST.tsv` inventories every mirrored file: repo path, Drive file id, title, mime type, size,
  modified time, md5, and status. One row per Drive file, no two rows sharing a path. The
  row-to-file bijection is asserted **across the two mirrored root folders only**. `chats/` is not
  mirrored Drive content — it is the sharded chat export, inventoried by its own `chats/INDEX.tsv`
  — so it has no manifest rows and `--prune`, which walks only the mirrored roots, leaves it alone.
* `PENDING.tsv` inventories what is still missing and why, in the same one-row-per-file form.
* Drive allows several files with the same title in one folder. The most recently modified copy keeps
  the plain name; every other copy carries a `__<driveFileId>` suffix before the extension. Three
  files titled `The_Method_1_6_BUILD174_compendia_papers_audits.md` sit in one folder, so that rule
  is load-bearing rather than theoretical.
* Google Docs (5 files) were exported as Markdown, so their sizes differ from the Drive listing.

## What is still outstanding

| File | Size | Why |
| --- | --- | --- |
| `Claude Chats/conversations.json` (two copies) | 388,264,753 B each | Above GitHub's 100 MB per-file limit |
| `BUILD174` third copy, `BUILD178` second copy | ~5.4 MB each | Same-folder duplicates, unreachable from a Drive mount |

The two chat exports cannot enter the repo as ordinary git objects by any transfer method. Shard them
with [`../tools/shard_conversations.py`](../tools/shard_conversations.py); the reasoning and the
alternatives are in [`../docs/DRIVE-SYNC.md`](../docs/DRIVE-SYNC.md).

The other two are duplicates of files already mirrored here, identical in title and byte count to
their mirrored twins. A mounted filesystem cannot show two entries with the same name in one folder,
so the Colab route can never see them. `tools/drive_sync.py` addresses files by Drive id and can:

```sh
python3 tools/drive_sync.py --only BUILD174 --only BUILD178 -v
```

## How this mirror was actually built, and what went wrong first

The first pass ran through the Claude Google Drive connector and stopped short, in three ways worth
recording because each has a different cause.

**A hard payload ceiling in the connector, just above 6 MiB.** Every file at or below 6,303,034 B
transferred; every file at or above 6,365,840 B failed. Three consecutive attempts on the smallest
failing file returned `MCP server "Google_Drive" session expired` immediately and identically, while
a metadata call on that same file through that same connector succeeded in between. The connector and
its auth were live: the oversized response payload itself is what tore the session down, so retrying
could never help. This blocked 31 files.

**Six subfolders were never walked at all** — CORPUS (346 files), BUILD175-PARTS, Claude Memories,
Claude Metadata, Claude Projects and Claude Chats, 361 files between them. The first pass reported
"413 of 444 files" without noticing that its denominator was wrong.

**Eighteen files were added to Drive after the pass ran** — BUILD174 to BUILD179, HANDOFF-98 to
HANDOFF-102, and the chat149 export bundles.

What that first pass did mirror was sound. All 444 of its rows were re-checked against Drive: every
one still present, in the folder its `repo_path` implies, no size drift, every local copy matching its
recorded md5.

The gap was closed by running [`../tools/drive_sync_colab.ipynb`](../tools/drive_sync_colab.ipynb),
which mounts Drive as a filesystem and so has no payload ceiling. It moved 283 files in one pass, all
byte-exact.
