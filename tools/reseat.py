#!/usr/bin/env python3
"""reseat.py — replace the body of a member already seated, under the same guard.

    python3 tools/reseat.py --old OLD --new NEW --member NAME=PATH [--member NAME=PATH ...]

`close.py` adds members and grows append-only ones; by design it refuses to rewrite a seated
member, asserting that every changed member equals old body + appended text. That is the right
default and it is why a member has to be right before it is seated. But a document that is seated
and then revised has nowhere to go: the repository copy and the member diverge, and nothing in the
tree can close the gap.

This closes it, and keeps the guarantee that made the refusal worth having:

  1. NEW must not exist; every named member must already be in OLD.
  2. Each named member's body is replaced outright, and the change is reported as a line count
     rather than assumed.
  3. Change set: no member other than those named differs, byte for byte.
  4. REVERSE GUARD: every replacement is undone and the result must reproduce the old bundle's own
     md5. Nothing is written until it does.

It does not touch MANIFEST.tsv, which records member sizes and md5s and is therefore left stale by
a replacement. That is reported, and the next `close.py` run regenerates it.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import pathlib
import re
import sys

MEMBER = re.compile(rb"^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n", re.S | re.M)
md5 = lambda b: hashlib.md5(b).hexdigest()


def parse(raw: bytes):
    ms = [(m.group(1).decode(), m.group(2)) for m in MEMBER.finditer(raw)]
    assert len({n for n, _ in ms}) == len(ms), "duplicate member name"
    return ms


def block(name: str, body: bytes) -> bytes:
    n = name.encode()
    return b"<<<FILE: " + n + b">>>\n" + body + b"<<<END FILE: " + n + b">>>\n"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--old", required=True)
    p.add_argument("--new", required=True)
    p.add_argument("--member", action="append", required=True, metavar="NAME=PATH")
    a = p.parse_args(argv)

    old_p, new_p = pathlib.Path(a.old), pathlib.Path(a.new)
    assert not new_p.exists(), f"{new_p} exists — never overwrite"
    old = old_p.read_bytes()
    od = dict(parse(old))
    nl = b"\n"
    print(f"old {old_p.name}\n    {len(old):,} B  md5 {md5(old)}  {old.count(nl):,} lines  "
          f"{len(od)} members")

    repl = {}
    for spec in a.member:
        name, _, path = spec.partition("=")
        assert path, f"--member wants NAME=PATH, got {spec!r}"
        assert name in od, f"{name} is not a member of {old_p.name}"
        body = pathlib.Path(path).read_bytes()
        assert body.endswith(b"\n"), f"{name}: body must end with a newline"
        assert old.count(block(name, od[name])) == 1, f"{name}: block is not unique"
        repl[name] = body
        o, n = od[name].decode("utf-8").splitlines(), body.decode("utf-8").splitlines()
        d = list(difflib.unified_diff(o, n, lineterm="", n=0))
        adds = sum(1 for x in d if x.startswith("+") and not x.startswith("+++"))
        dels = sum(1 for x in d if x.startswith("-") and not x.startswith("---"))
        print(f"    replace {name}: {len(od[name]):,} -> {len(body):,} B, "
              f"+{adds} / -{dels} lines")

    new = old
    for name, body in repl.items():
        new = new.replace(block(name, od[name]), block(name, body))

    nd = dict(parse(new))
    changed = [n for n in od if nd[n] != od[n]]
    assert sorted(changed) == sorted(repl), f"unexpected change in members: {changed}"
    assert set(nd) == set(od), "member set changed"
    print(f"new {new_p.name}\n    {len(new):,} B  md5 {md5(new)}  {new.count(nl):,} lines  "
          f"{len(nd)} members;  changed: {sorted(changed)}")

    rev = new
    for name, body in repl.items():
        assert rev.count(block(name, body)) == 1
        rev = rev.replace(block(name, body), block(name, od[name]))
    print(f"    reverse recovers md5 {md5(rev)}  == old: {md5(rev) == md5(old)}")
    assert md5(rev) == md5(old), "REVERSE GUARD FAILED — nothing written"

    new_p.write_bytes(new)
    print(f"    written {new_p}")
    if "MANIFEST.tsv" in od and "MANIFEST.tsv" not in repl:
        print("\nMANIFEST.tsv records member sizes and md5s and is now STALE for the members")
        print("replaced above. The next close.py run regenerates it. Not repaired here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
