# Drive mirror: The Method folders

Byte-exact copies of the Google Drive folders **The Method Materials** (with its subfolders COWORK,
LOWDIN-DELIVERY-1, THREEBODY-DELIVERY-1, CORPUS, BUILD175-PARTS, Claude Memories, Claude Metadata,
Claude Projects and Claude Chats) and **The Method Prints & Proofs**, pulled through the Google Drive
connector on 2026-09-02.

* `MANIFEST.tsv` lists every Drive file: repo path, Drive file id, title, size, modified time,
  md5 of the copy here, and transfer status.
* Drive allows several files with the same title in one folder. The most recently modified copy keeps
  the plain name; older copies carry a `__<driveFileId>` suffix before the extension.
* Google Docs (5 files) were exported as Markdown, so their sizes differ from the Drive listing.
* `MANIFEST.tsv` covers the 444 files the first mirroring pass inventoried; 413 of those transferred.
* `PENDING.tsv` covers everything still outstanding, from every cause, one row per file with a reason.

## Why 31 files are missing

Not a dropped or expired session — **a hard payload ceiling in the Drive connector, just above
6 MiB**. Every file at or below 6,303,034 B (6.011 MiB) transferred; every file at or above
6,365,840 B (6.071 MiB) failed. Re-tested on 2026-09-02: three consecutive download attempts on the
smallest failing file returned `MCP server "Google_Drive" session expired` immediately and
identically, while a metadata call on that same file through that same connector succeeded in
between — the connector and its auth were live, and the oversized response payload itself is what
tears the session down. Retrying cannot help.

The 31 are all `The_Method_1_6_BUILD<N>_compendia_papers_audits.md`, BUILD143–BUILD158, 6.07–7.26 MiB
each, 220,527,615 B in total — but only 16 unique files (111,959,412 B); the rest are the same builds
duplicated into `LOWDIN-DELIVERY-1` and `THREEBODY-DELIVERY-1`. All 31 were re-verified in Drive on
2026-09-02: all still present, all byte counts unchanged.

The seven files here that are larger than the ceiling (up to 14.2 MB) did not come through the
connector; the owner uploaded them directly, and the eight manifest rows concerned say so in their
`status`.

## Finishing the job

Use [`../tools/drive_sync.py`](../tools/drive_sync.py), which streams downloads and therefore has no
size limit:

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/drive_sync.py --only BUILD14 --only BUILD15 -v
```

Full setup (Google Cloud project, OAuth desktop client, the other sync routes, and the gotchas) is in
[`../docs/DRIVE-SYNC.md`](../docs/DRIVE-SYNC.md).


## What the first pass missed

Re-auditing the mirror against Drive found two gaps the original run never recorded.

**Six subfolders of "The Method Materials" were never walked at all** — `CORPUS` (346 files),
`BUILD175-PARTS`, `Claude Memories`, `Claude Metadata`, `Claude Projects` and `Claude Chats`,
361 files between them.

**Eighteen files were added to the already-mirrored folders after the pass ran** — BUILD174 to
BUILD179, HANDOFF-98 to HANDOFF-102, and the chat149 export bundles.

What was already mirrored is sound. All 444 manifest rows were re-checked against Drive: every one is
still present, in the folder its `repo_path` implies, with no size drift, and every local copy matches
its recorded md5 exactly.

Two things cannot be fixed by any transfer method:

* `Claude Chats/conversations.json` exists in Drive as two 370 MB copies. GitHub hard-limits files at
  100 MB, so these cannot enter the repo as ordinary git objects. See `../docs/REPO-SIZE.md`.
* `Claude Metadata/users.json` and `Claude Metadata/login_history.json` are Claude account records,
  the latter containing login IP addresses, timestamps and user agents. They are held back on purpose:
  git history is permanent and awkward to purge, so committing them should be a deliberate choice.
  To include them: `python3 tools/drive_sync.py --only "Claude Metadata"`
