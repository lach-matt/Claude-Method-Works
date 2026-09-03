#!/usr/bin/env python3
"""restage.py — re-extract the bundles into method/members/ and retarget the witness check.

    python3 tools/restage.py --bundle TAG=PATH [--bundle TAG=PATH ...] [--prune]

`method/` mirrors the two live bundles as an extracted tree: every member byte-exact under
`members/`, an index in `MEMBER-INDEX.tsv`, and `verify.py` asserting both. When a bundle is
rebuilt — by `close.py` on the compendia side or `close_main.py` on the main side — that mirror
is stale until it is rebuilt from the new bundles. Nothing in the tree did that; this does.

It is deliberately not a member and not an instrument. It maintains the repository's copy of the
store of record, not the store of record itself, which is why it sits beside `verify.py` rather
than inside a bundle.

The extraction is asserted, not assumed: each member is spliced back into the bundle at the offset
recorded for it and the bundle's own md5 must come back. `--prune` additionally removes member
files that no longer appear in any bundle; without it they are reported and left alone.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys

MEMBER = re.compile(rb"^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n", re.S | re.M)
md5 = lambda b: hashlib.md5(b).hexdigest()


def parse(raw: bytes):
    ms = [(m.group(1).decode(), m.group(2), m.start(2)) for m in MEMBER.finditer(raw)]
    assert len({n for n, _, _ in ms}) == len(ms), "duplicate member name"
    return ms


def main(argv=None):
    root = pathlib.Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--bundle", action="append", required=True, metavar="TAG=PATH")
    ap.add_argument("--prune", action="store_true",
                    help="delete member files no longer in any bundle (default: report only)")
    a = ap.parse_args(argv)

    bundles = {}
    for spec in a.bundle:
        tag, _, path = spec.partition("=")
        assert path, f"--bundle wants TAG=PATH, got {spec!r}"
        bundles[tag] = pathlib.Path(path)

    mem = root / "method" / "members"
    mem.mkdir(parents=True, exist_ok=True)
    rows, seen = [], set()

    for tag, path in bundles.items():
        raw = path.read_bytes()
        ms = parse(raw)
        for n, b, off in ms:
            (mem / n).write_bytes(b)
            rows.append([n, tag, pathlib.Path(n).suffix, str(len(b)), md5(b), str(off)])
            seen.add(n)
        # assert the extraction rather than assume it: splice every member back
        back = bytearray(raw)
        for n, b, off in ms:
            back[off:off + len(b)] = (mem / n).read_bytes()
        got = md5(bytes(back))
        ok = got == md5(raw)
        print(f"{tag:<20} {len(ms):>3} members  {len(raw):,} B  md5 {md5(raw)}  "
              f"round-trip {'OK' if ok else 'MISMATCH ' + got}")
        assert ok, f"{tag}: extraction does not reproduce the bundle"

    rows.sort(key=lambda r: (r[1], r[0]))
    idx = root / "method" / "MEMBER-INDEX.tsv"
    idx.write_text("member\tbundle\text\tbytes\tmd5\tbundle_offset\n"
                   + "\n".join("\t".join(r) for r in rows) + "\n", encoding="utf-8")
    print(f"MEMBER-INDEX.tsv     {len(rows)} rows")

    orphans = sorted(p.name for p in mem.iterdir() if p.is_file() and p.name not in seen)
    if orphans:
        if a.prune:
            for n in orphans:
                (mem / n).unlink()
            print(f"pruned {len(orphans)} orphan member file(s): {', '.join(orphans)}")
        else:
            print(f"NOTE {len(orphans)} member file(s) are in no bundle and were left in place "
                  f"(--prune removes them): {', '.join(orphans)}")

    vp = root / "method" / "verify.py"
    v = vp.read_text(encoding="utf-8")
    v = re.sub(r"BUNDLES = \{.*?\n\}",
               "BUNDLES = {\n" + "".join(f"    '{t}': '{p.name}',\n" for t, p in bundles.items())
               + "}", v, count=1, flags=re.S)
    v = re.sub(r"EXPECT_MD5 = \{.*?\n\}",
               "EXPECT_MD5 = {\n"
               + "".join(f"    '{t}': '{md5(p.read_bytes())}',\n" for t, p in bundles.items())
               + "}", v, count=1, flags=re.S)
    vp.write_text(v, encoding="utf-8")
    print(f"verify.py            retargeted to {', '.join(bundles)}")
    print("\nrun: python3 method/verify.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
