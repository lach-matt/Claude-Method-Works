"""Regression tests for tools/drive_sync.py.

The mirror's guarantee is byte-exactness, and every test here guards one way a
review found that guarantee could silently break.  Each states the OLD
behaviour it exists to prevent.  No framework and no CI: run it by hand after
touching the download path.

    python3 tools/test_drive_sync.py

Exits non-zero if anything regressed.
"""
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import drive_sync as ds  # noqa: E402


class FakeHttpError(Exception):
    def __init__(self, status):
        super().__init__("HTTP {}".format(status))
        self.resp = type("R", (), {"status": status})()


def make_downloader(script):
    """script: list of (bytes_or_None, done). None means raise 416."""

    class FakeDownloader:
        def __init__(self, handle, request, chunksize=0):
            self.handle = handle
            self.steps = list(script)

        def next_chunk(self, num_retries=0):
            if not self.steps:
                return None, True
            payload, done = self.steps.pop(0)
            if payload is None:
                raise FakeHttpError(416)
            self.handle.write(payload)
            return None, done

    return FakeDownloader


def client_for(script):
    mods = ds.GoogleModules(
        build=lambda *a, **k: None,
        http_error=FakeHttpError,
        media_download=make_downloader(script),
        credentials_cls=object,
        installed_app_flow=object,
        refresh_request=object,
        refresh_error=Exception,
        authorized_http=lambda *a, **k: None,
        http_factory=lambda *a, **k: None,
    )
    class FakeFiles:
        def get_media(self, **kw):
            return object()

        def export_media(self, **kw):
            return object()

    class FakeService:
        def files(self):
            return FakeFiles()

    c = ds.DriveClient(credentials=None, modules=mods)
    c._thread_state.service = FakeService()
    return c


FAILURES = []


def check(name, condition, detail=""):
    print(("  PASS  " if condition else "  FAIL  ") + name + ("" if condition else " -- " + detail))
    if not condition:
        FAILURES.append(name)


def test_short_download_no_md5():
    """OLD: a truncated transfer with no Drive md5 was recorded status ok."""
    print("\n1. short download, Drive supplies size but no md5")
    with tempfile.TemporaryDirectory() as d:
        dest = pathlib.Path(d, "file.bin")
        dest.write_bytes(b"GOOD-ORIGINAL")
        c = client_for([(b"only-half", True)])
        try:
            c.download_file("id", dest, expected_size=100, expected_md5="")
            check("truncated transfer is rejected", False, "no exception raised")
        except ds.ContentMismatch as exc:
            check("truncated transfer is rejected", True)
            check("error names both sizes", "9" in str(exc) and "100" in str(exc), str(exc))
        check("previous good copy survives", dest.read_bytes() == b"GOOD-ORIGINAL",
              repr(dest.read_bytes()))
        leftovers = [p.name for p in pathlib.Path(d).iterdir() if p.name != "file.bin"]
        check("no .part left behind", not leftovers, str(leftovers))


def test_md5_mismatch_preserves_good_copy():
    """OLD: bad bytes were installed first, THEN the md5 was checked."""
    print("\n2. complete transfer whose md5 disagrees with Drive")
    with tempfile.TemporaryDirectory() as d:
        dest = pathlib.Path(d, "file.bin")
        dest.write_bytes(b"GOOD-ORIGINAL")
        c = client_for([(b"corrupt-but-right-length", True)])
        try:
            c.download_file("id", dest, expected_size=24, expected_md5="0" * 32)
            check("md5 mismatch is rejected", False, "no exception raised")
        except ds.ContentMismatch:
            check("md5 mismatch is rejected", True)
        check("previous good copy survives", dest.read_bytes() == b"GOOD-ORIGINAL",
              repr(dest.read_bytes()))


def test_416_midway():
    """OLD: a 416 anywhere in the loop installed the partial file as complete."""
    print("\n3. HTTP 416 partway through a transfer")
    with tempfile.TemporaryDirectory() as d:
        dest = pathlib.Path(d, "file.bin")
        dest.write_bytes(b"GOOD-ORIGINAL")
        c = client_for([(b"first-chunk", False), (None, False)])
        try:
            c.download_file("id", dest, expected_size=None, expected_md5="")
            check("mid-transfer 416 is rejected", False, "installed as complete")
        except ds.ContentMismatch as exc:
            check("mid-transfer 416 is rejected", True)
            check("error says truncated", "truncated" in str(exc), str(exc))
        check("previous good copy survives", dest.read_bytes() == b"GOOD-ORIGINAL",
              repr(dest.read_bytes()))


def test_416_at_zero_bytes_still_means_empty():
    """Guard the behaviour we must NOT break: 416 with nothing written = empty file."""
    print("\n4. HTTP 416 before any byte (a genuinely empty Drive file)")
    with tempfile.TemporaryDirectory() as d:
        dest = pathlib.Path(d, "empty.bin")
        c = client_for([(None, False)])
        size, digest = c.download_file("id", dest, expected_size=0, expected_md5="")
        check("empty file still installs", dest.is_file() and size == 0, str(size))
        check("md5 is of empty content", digest == "d41d8cd98f00b204e9800998ecf8427e", digest)


def test_happy_path():
    """A good transfer still works and returns real size and md5."""
    print("\n5. a correct transfer")
    import hashlib
    body = b"the actual bytes"
    want = hashlib.md5(body).hexdigest()
    with tempfile.TemporaryDirectory() as d:
        dest = pathlib.Path(d, "file.bin")
        c = client_for([(body, True)])
        size, digest = c.download_file("id", dest, expected_size=len(body), expected_md5=want)
        check("file installed", dest.read_bytes() == body)
        check("size returned", size == len(body), str(size))
        check("md5 returned", digest == want, digest)


def test_worker_exception_keeps_manifest():
    """OLD: one unexpected exception aborted run_sync and lost every outcome."""
    print("\n6. an unexpected exception in one worker")
    entries = []
    for i in range(4):
        entries.append((ds.DriveEntry(
            file_id="id{}".format(i), title="f{}.txt".format(i), mime_type="text/plain",
            size=10, md5="", modified_time="2026-01-01T00:00:00.000Z", folder_path="",
        ), "f{}.txt".format(i)))

    real = ds.sync_entry

    def boom(client, entry, repo_path, dest_root, previous, dry_run):
        if repo_path == "f2.txt":
            raise KeyError("something nobody predicted")
        return ds.SyncOutcome(repo_path, ds.Action.ADDED,
                              ds.build_row(entry, repo_path, 10, "x" * 32, ds.STATUS_OK))

    ds.sync_entry = boom
    try:
        outcomes = ds.run_sync(None, entries, pathlib.Path("/tmp"), {}, 2, False)
    finally:
        ds.sync_entry = real
    check("run completes instead of aborting", len(outcomes) == 4, str(len(outcomes)))
    failed = [o for o in outcomes if o.action == ds.Action.FAILED]
    check("the bad file is one FAILED row", len(failed) == 1 and failed[0].repo_path == "f2.txt",
          str([(o.repo_path, o.action) for o in outcomes]))
    ok = [o for o in outcomes if o.action == ds.Action.ADDED]
    check("the other three keep their rows", len(ok) == 3, str(len(ok)))
    check("failure reason is recorded", "KeyError" in failed[0].row.status, failed[0].row.status)


def test_exclusion():
    """OLD: no way to exclude a path, so a default run pulled the 388 MB files."""
    print("\n7. exclusion by pattern and by size")
    big = ds.DriveEntry(file_id="a", title="conversations.json", mime_type="application/json",
                        size=388264753, md5="", modified_time="", folder_path="")
    small = ds.DriveEntry(file_id="b", title="note.md", mime_type="text/markdown",
                          size=1024, md5="", modified_time="", folder_path="")
    limit = ds.GITHUB_FILE_LIMIT_BYTES
    r = ds.excluded_reason(big, "Claude Chats/conversations.json", [], limit)
    check("388 MB file excluded by default size cap", bool(r), repr(r))
    check("reason names the limit", str(limit) in r, r)
    check("small file not excluded", not ds.excluded_reason(small, "note.md", [], limit))
    check("pattern excludes", bool(ds.excluded_reason(small, "note.md", ["note"], limit)))
    check("size cap disabled by None", not ds.excluded_reason(big, "x", [], None))


for fn in (test_short_download_no_md5, test_md5_mismatch_preserves_good_copy,
           test_416_midway, test_416_at_zero_bytes_still_means_empty, test_happy_path,
           test_worker_exception_keeps_manifest, test_exclusion):
    fn()

print("\n" + ("ALL PASS" if not FAILURES else "FAILURES: " + ", ".join(FAILURES)))
sys.exit(1 if FAILURES else 0)
