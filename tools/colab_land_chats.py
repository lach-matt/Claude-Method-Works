#!/usr/bin/env python3
"""Shard the Claude Chats export and land it in the repository. Colab only.

Run this from a Colab notebook that has already mounted Drive and cloned the
repo (cells 1 and 2 of ``drive_sync_colab.ipynb``)::

    !python3 /content/repo/tools/colab_land_chats.py

It does, in order, refusing rather than guessing at every step:

1. finds ``conversations.json`` on the Drive mount;
2. installs ``ijson`` and says plainly whether it got it -- without it the
   sharder falls back to ``json.load`` and needs 4-8x the file size in RAM;
3. dry-runs ``shard_conversations.py``, then writes to ``/content/chats-shards``;
4. copies the tree to ``drive/chats`` in the clone, refusing to clobber a
   non-empty one;
5. commits and pushes, and on a failed push names the likely cause -- cell 6
   unsets the credential helper, so a clone that has run it can no longer
   authenticate. The commit is made either way; nothing is lost.

``--dry-run`` stops after step 3's dry run. Stdlib only, apart from the ijson it
installs for the sharder.
"""

import argparse
import os
import shlex
import shutil
import subprocess
import sys

DRIVE_ROOT = "/content/drive/MyDrive"
CHATS = ("The Method Materials", "Claude Chats")
TITLE = "conversations.json"
REPO = "/content/repo"
SHARD_OUT = "/content/chats-shards"
DEST_REL = os.path.join("drive", "chats")


def die(message):
    print("\nSTOP: %s" % message)
    raise SystemExit(1)


def run(command, **kwargs):
    print("$ %s" % shlex.join(command))
    return subprocess.run(command, text=True, **kwargs)


def norm(name):
    return name.strip().strip(".").casefold()


def find_export():
    if not os.path.isdir(DRIVE_ROOT):
        die("Drive is not mounted at %s. Run cell 1 first." % DRIVE_ROOT)
    folder = DRIVE_ROOT
    for part in CHATS:
        matches = [e for e in os.listdir(folder) if norm(e) == norm(part)]
        if len(matches) != 1:
            die("expected exactly one %r inside %r, found %d: %s"
                % (part, folder, len(matches), sorted(matches)))
        folder = os.path.join(folder, matches[0])
    copies = sorted(os.path.join(folder, e) for e in os.listdir(folder)
                    if norm(e) == norm(TITLE) and os.path.isfile(os.path.join(folder, e)))
    if not copies:
        die("no file named %r in %r" % (TITLE, folder))
    print("found %d copy/copies of %s:" % (len(copies), TITLE))
    for path in copies:
        print("  %s  (%s bytes)" % (path, format(os.path.getsize(path), ",")))
    if len(copies) == 1:
        print("  (only one is visible: a mount cannot show two files of the same name in a folder)")
    return copies[0]


def check_repo():
    if not os.path.isdir(os.path.join(REPO, ".git")):
        die("no clone at %s. Run cell 2 first." % REPO)
    script = os.path.join(REPO, "tools", "shard_conversations.py")
    if not os.path.isfile(script):
        die("%s is missing. This clone is on a branch that predates it; check out the "
            "branch carrying it and re-run." % script)
    branch = subprocess.run(("git", "-C", REPO, "rev-parse", "--abbrev-ref", "HEAD"),
                            text=True, capture_output=True).stdout.strip()
    print("clone at %s is on branch %s" % (REPO, branch))
    return script, branch


def inspect_existing(out):
    """Classify whatever is already at ``out``.

    ``None``      nothing there, shard normally
    ``"partial"`` non-empty but not a finished tree, re-shard over it
    ``(n, rows)`` a finished tree: n shard files against INDEX.tsv's row count
    """
    if not os.path.isdir(out) or not os.listdir(out):
        return None
    index = os.path.join(out, "INDEX.tsv")
    if not os.path.isfile(index):
        return "partial"
    with open(index) as handle:
        rows = max(0, sum(1 for _ in handle) - 1)
    shards = sum(1 for dirpath, _, names in os.walk(out) for name in names
                 if name.endswith(".json") and os.path.abspath(dirpath) != os.path.abspath(out))
    return (shards, rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true",
                        help="stop after the sharder's dry run; write nothing")
    parser.add_argument("--force", action="store_true",
                        help="re-shard even if a finished tree is already at the output path")
    parser.add_argument("--max-shard-mib", type=float, default=40.0,
                        help="refuse to commit if any shard is at least this large "
                             "(default 40, the trigger in docs/REPO-SIZE.md)")
    args = parser.parse_args()

    source = find_export()
    script, branch = check_repo()

    print("\ninstalling ijson (constant-memory streaming for the sharder):")
    subprocess.run((sys.executable, "-m", "pip", "install", "--quiet", "ijson"), check=False)
    try:
        import ijson  # noqa: F401
        print("  ijson present - the sharder will stream at flat memory.")
    except ImportError:
        print("  ijson NOT available. The sharder will fall back to json.load, which needs\n"
              "  roughly 1.5-3 GB of RAM for a 370 MiB export. It will still work on a\n"
              "  standard Colab instance, but it will say so in its own output.")

    print("\n--- dry run ---")
    if run((sys.executable, script, source, "--out", SHARD_OUT, "--dry-run")).returncode != 0:
        die("the dry run failed. Read its output above; nothing was written.")
    if args.dry_run:
        print("\n--dry-run given: stopping here. Nothing was written.")
        return 0

    existing = inspect_existing(SHARD_OUT)
    reuse = False
    if isinstance(existing, tuple) and not args.force:
        shards, rows = existing
        if shards and shards == rows:
            print("\n--- reusing the shard tree already at %s ---" % SHARD_OUT)
            print("  %s shard file(s), and INDEX.tsv agrees at %s row(s)."
                  % (format(shards, ","), format(rows, ",")))
            print("  A previous run wrote this. Re-reading 370 MiB over the Drive mount would\n"
                  "  only reproduce it; pass --force to do that anyway.")
            reuse = True
        else:
            print("\nA tree at %s disagrees with its own INDEX.tsv (%s shard file(s), %s row(s)),\n"
                  "so it is not trustworthy. Re-sharding over it."
                  % (SHARD_OUT, format(shards, ","), format(rows, ",")))
    elif existing == "partial" and not args.force:
        print("\n%s is non-empty but has no INDEX.tsv, so a previous run did not finish.\n"
              "Re-sharding over it." % SHARD_OUT)

    if not reuse:
        print("\n--- writing shards ---")
        command = [sys.executable, script, source, "--out", SHARD_OUT]
        if existing is not None:
            command.append("--force")
        if run(command).returncode != 0:
            die("sharding failed. Read the output above.")

    largest, largest_path, total = 0, "", 0
    for dirpath, _, names in os.walk(SHARD_OUT):
        for name in names:
            size = os.path.getsize(os.path.join(dirpath, name))
            total += size
            if size > largest:
                largest, largest_path = size, os.path.join(dirpath, name)
    mib = 1024.0 * 1024.0
    print("\nshard tree: %s file(s), %.1f MiB total; largest %.1f MiB (%s)"
          % (format(sum(len(f) for _, _, f in os.walk(SHARD_OUT)), ","),
             total / mib, largest / mib, os.path.relpath(largest_path, SHARD_OUT)))
    if largest >= 100 * 1000 * 1000:
        die("that shard is at or above GitHub's 100 MB hard block. Committing it would make the\n"
            "push fail with the blob already in history, which then needs history surgery to\n"
            "remove. Nothing was committed. Split or exclude that conversation first.")
    if largest / mib >= args.max_shard_mib:
        die("that shard is at or above the %.0f MiB trigger in docs/REPO-SIZE.md, which says do\n"
            "not commit it. Nothing was committed; the shards are at %s. Re-run with\n"
            "--max-shard-mib set higher if you have read that section and accept the cost."
            % (args.max_shard_mib, SHARD_OUT))

    dest = os.path.join(REPO, DEST_REL)
    if os.path.isdir(dest) and os.listdir(dest):
        die("%s already exists and is not empty. Inspect it before overwriting; this "
            "script will not clobber an existing shard tree." % dest)
    shutil.copytree(SHARD_OUT, dest, dirs_exist_ok=True)
    landed = sum(len(files) for _, _, files in os.walk(dest))
    print("\ncopied %s file(s) into %s" % (format(landed, ","), dest))

    for step in (("git", "-C", REPO, "add", "--", DEST_REL),
                 ("git", "-C", REPO, "commit", "-m",
                  "drive: shard the Claude Chats conversations.json export into drive/chats")):
        if run(step).returncode != 0:
            die("%r failed. Nothing was pushed; the shards are at %s." % (step[3], dest))

    if run(("git", "-C", REPO, "push", "-u", "origin", branch)).returncode != 0:
        print("\nPush failed, and the commit is already made - nothing is lost.\n"
              "Cell 6 unsets the credential helper when it finishes, so the usual cause is\n"
              "that this clone can no longer authenticate. Re-run cell 2, then re-run:\n"
              "  !git -C %s push -u origin %s" % (REPO, branch))
        return 1
    print("\nPushed to %s. The shards are in the repository." % branch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
