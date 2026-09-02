# Drive mirror: The Method folders

Byte-exact copies of the Google Drive folders **The Method Materials** (with its
subfolders COWORK, LOWDIN-DELIVERY-1, THREEBODY-DELIVERY-1) and **The Method Prints & Proofs**,
pulled through the Google Drive connector on 2026-09-02.

* `MANIFEST.tsv` lists every Drive file: repo path, Drive file id, title, size, modified time,
  md5 of the copy here, and transfer status.
* Drive allows several files with the same title in one folder. The most recently modified copy keeps
  the plain name; older copies carry a `__<driveFileId>` suffix before the extension.
* Google Docs (5 files) were exported as Markdown, so their sizes differ from the Drive listing.
* 405 of 444 files transferred. 39 files could not be fetched because the Drive
  connector dropped the session on every attempt (all but one are over 6.3 MB; it also refuses files over 10 MB); they are listed in
  `MANIFEST.tsv` with status `not-transferred` and are still only in Drive.
