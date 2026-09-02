# Drive mirror: The Method folders

Byte-exact copies of the Google Drive folders **The Method Materials** (with its
subfolders COWORK, LOWDIN-DELIVERY-1, THREEBODY-DELIVERY-1) and **The Method Prints & Proofs**,
pulled through the Google Drive connector on 2026-09-02.

* `MANIFEST.tsv` lists every Drive file: repo path, Drive file id, title, size, modified time,
  md5 of the copy here, and transfer status.
* Drive allows several files with the same title in one folder. The most recently modified copy keeps
  the plain name; older copies carry a `__<driveFileId>` suffix before the extension.
* Google Docs (5 files) were exported as Markdown, so their sizes differ from the Drive listing.
* 413 of 444 files transferred. The 31 that did not are listed in `MANIFEST.tsv` with status
  `not-transferred` and are still only in Drive.

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
