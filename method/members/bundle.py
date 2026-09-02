#!/usr/bin/env python3
"""bundle.py — pack the working tree into the two BUILD bundles.

REBUILT FROM SCRATCH, chat 28, under RULING 54. The retired pair is not the
ancestor of this file; only the on-disk FORMAT is inherited, because every
existing bundle is written in it and must remain readable.

  python3 bundle.py 28              write The_Method_1_6_BUILD28_*.md
  python3 bundle.py 28 --dir DIR    pack DIR instead of the working directory

FORMAT (fixed, do not change — BUILD-1..28 are written in it):
    <<<FILE: name>>>\n <body> \n<<<END FILE: name>>>\n
  member blocks joined by "\n". The packer contributes exactly ONE newline
  before the END marker; the splitter consumes exactly that one.

THREE DEFECTS OF THE RETIRED PAIR, EACH ANSWERED HERE:
  1. the old split.py did not consume the packer's newline, so every member
     came back one byte long. Answered by a SHARED regex — one definition,
     imported by the splitter, so the two sides cannot drift apart again.
  2. both sides opened in text mode, so universal-newline translation folded
     CRLF to LF before the regex ran and a CRLF member could not survive a
     round trip. Answered by newline="" on EVERY read and EVERY write.
  3. an md5 of one restore against another compares two corrupted trees and
     passes. Answered by verify(): the members are re-assembled and the
     result compared to the BUNDLE'S OWN BYTES. Nothing is written unless
     that comparison is exact.
"""
import sys, os, re

# ---- the format, defined once, shared with split.py -------------------------
OPEN_FMT  = "<<<FILE: {name}>>>\n"
CLOSE_FMT = "\n<<<END FILE: {name}>>>\n"
MEMBER_RE = re.compile(r"<<<FILE: (.+?)>>>\n(.*?)\n<<<END FILE: \1>>>", re.S)
DECLARE_RE = re.compile(r"^<<<FILE: (.+?)>>>$", re.M)
JOIN = "\n"

B1 = ["The_Method_1_6-2.md", "The_Method_1_6___The_Register-2.md"]

# binaries cannot ride in a UTF-8 text bundle (chat 15). ref.docx is rebuilt
# from W-013's recipe by any session that presses; the figures are refetched.
SKIP_EXT = {".prepoint", ".bak", ".pyc",
            ".docx", ".pdf", ".zip", ".png", ".jpg", ".tar", ".gz",
            # COORDINATES-2.13 is the Spectra Compendium's DATA COMPANION,
            # delivered beside the volume, 10.9 MB, reached in /mnt/project.
            # NOT .tsv — the seven spectra level files are members and have
            # been since chat 10; excluding them dropped 7 silently (chat 18).
            ".csv"}
SKIP_NAME = {"__pycache__", "tmp.md"}       # build.py's scratch file
SKIP_SUFFIX = (".pages.md", ".pages.md.chk")  # build.py regenerates these


def read_bytes_exact(path):
    """Text, with NO newline translation. The whole point of defect 2."""
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read()


def write_bytes_exact(path, text):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def members(root="."):
    out, dropped = [], []
    for f in sorted(os.listdir(root)):
        if not os.path.isfile(os.path.join(root, f)):
            continue
        if f in SKIP_NAME or any(f.endswith(e) for e in SKIP_EXT):
            continue
        if f.endswith(SKIP_SUFFIX):
            dropped.append(f); continue
        if f.startswith("The_Method_1_6_BUILD"):
            continue
        out.append(f)
    for f in dropped:                      # a drop is REPORTED, never silent
        print("bundle.py: excluded derived press file", f)
    return out


def pack(names, root="."):
    blocks = []
    for n in names:
        body = read_bytes_exact(os.path.join(root, n))
        blocks.append(OPEN_FMT.format(name=n) + body + CLOSE_FMT.format(name=n))
    return JOIN.join(blocks)


def unpack(text):
    """Ordered members. Also reports what was declared but never paired."""
    found = [(m.group(1), m.group(2)) for m in MEMBER_RE.finditer(text)]
    declared = DECLARE_RE.findall(text)
    return found, declared


def verify(text, names, root="."):
    """Verify against the BUNDLE'S BYTES — defect 3.

    Returns (fatal, warnings). THE AUTHORITATIVE TEST IS RE-ASSEMBLY: if the
    members that came out, re-packed in order, are byte-identical to the
    bundle, nothing was lost or invented, whatever else the text contains.
    A stray `<<<FILE: x>>>` line inside a body is a WARNING, not a refusal —
    it is only dangerous if it captures, and if it captured, re-assembly
    would already have failed. Refusing on the count alone would block a
    handoff that merely QUOTES the format, which several members do.
    """
    found, declared = unpack(text)
    fatal, warn = [], []
    got_names = [n for n, _ in found]
    if len(found) != len(names):
        fatal.append("paired %d, packed %d" % (len(found), len(names)))
    if len(set(got_names)) != len(got_names):
        fatal.append("duplicate member names on unpack")
    if len(declared) != len(names):
        strays = [d for d in declared if d not in set(names)]
        warn.append("declared %d, packed %d — stray markers inside bodies: %s"
                    % (len(declared), len(names), strays[:5] or "repeated name"))
    got = dict(found)
    for n in names:
        if n not in got:
            fatal.append("missing member " + n); continue
        if got[n] != read_bytes_exact(os.path.join(root, n)):
            fatal.append("body differs " + n)
    rebuilt = JOIN.join(OPEN_FMT.format(name=n) + b + CLOSE_FMT.format(name=n)
                        for n, b in found)
    if rebuilt.encode("utf-8") != text.encode("utf-8"):
        fatal.append("re-assembly is not byte-identical to the bundle")
    return fatal, warn


def main(build, root="."):
    all_m = members(root)
    b1 = [f for f in B1 if f in all_m]
    b2 = [f for f in all_m if f not in b1]
    ok = True
    for tag, names in (("main_and_register", b1),
                       ("compendia_papers_audits", b2)):
        text = pack(names, root)
        bad, warn = verify(text, names, root)
        for w in warn:
            print("bundle.py: NOTE %s: %s" % (tag, w))
        if bad:
            print("ROUND-TRIP FAIL %s: %s" % (tag, bad[:5]))
            ok = False
            continue
        fn = os.path.join(root, "The_Method_1_6_BUILD%s_%s.md" % (build, tag))
        write_bytes_exact(fn, text)
        print("%s  members %d  bytes %s  verified against bundle bytes"
              % (os.path.basename(fn), len(names),
                 format(len(text.encode("utf-8")), ",")))
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    root = "."
    if "--dir" in args:
        i = args.index("--dir"); root = args[i + 1]; del args[i:i + 2]
    if not args:
        sys.exit("usage: bundle.py BUILDNUMBER [--dir DIR]")
    main(args[0], root)

