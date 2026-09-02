#!/usr/bin/env python3
"""split.py — unpack BUILD bundles into a directory.

REBUILT FROM SCRATCH, chat 28, under RULING 54, together with bundle.py.

  python3 split.py BUNDLE [BUNDLE ...] [-o DIR] [--quiet]

WHY THIS FILE IMPORTS bundle.py RATHER THAN CARRYING ITS OWN REGEX:
the retired pair held two copies of the format and they drifted — the packer
wrote a newline before the END marker and the splitter did not consume it, so
89 of 89 members came back one byte long and nothing noticed for fourteen
builds. One definition, imported, cannot drift. (G7: a reimplementation that
disagrees with an instrument is the thing that is wrong.)

newline="" on both the read and every write: a member holding CRLF must come
out holding CRLF. In text mode it does not.

VERIFICATION IS AGAINST THE BUNDLE, NOT AGAINST A SECOND RESTORE. Comparing
one restore with another compares two corrupted trees and passes. Here the
extracted members are re-assembled and the result is required to be
byte-identical to the bundle that produced them; anything else is a FAIL and
the exit status is nonzero.
"""
import sys, os

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)
import bundle as B                     # the format lives in exactly one place


def split_one(src, outdir=".", quiet=False):
    text = B.read_bytes_exact(src)
    found, declared = B.unpack(text)

    names = [n for n, _ in found]
    spurious = len(declared) - len(found)
    dupes = [n for n in set(names) if names.count(n) > 1]

    rebuilt = B.JOIN.join(B.OPEN_FMT.format(name=n) + b +
                          B.CLOSE_FMT.format(name=n) for n, b in found)
    exact = rebuilt.encode("utf-8") == text.encode("utf-8")

    os.makedirs(outdir, exist_ok=True)
    for n, body in found:
        B.write_bytes_exact(os.path.join(outdir, os.path.basename(n)), body)

    status = "EXACT" if exact else "NOT BYTE-EXACT"
    if not quiet:
        print("%s: declared %d · paired %d · spurious %d · re-assembly %s"
              % (os.path.basename(src), len(declared), len(found),
                 spurious, status))
        if dupes:
            print("  DUPLICATE MEMBER NAMES:", sorted(dupes))
    return found, exact and not dupes


def main(argv):
    outdir, quiet, srcs = ".", False, []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "-o":
            outdir = argv[i + 1]; i += 2; continue
        if a == "--quiet":
            quiet = True; i += 1; continue
        srcs.append(a); i += 1
    if not srcs:
        sys.exit("usage: split.py BUNDLE [BUNDLE ...] [-o DIR] [--quiet]")
    ok, total = True, 0
    for s in srcs:
        found, good = split_one(s, outdir, quiet)
        total += len(found)
        ok = ok and good
    if not quiet:
        print("TOTAL MEMBERS WRITTEN: %d -> %s" % (total, outdir))
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])

