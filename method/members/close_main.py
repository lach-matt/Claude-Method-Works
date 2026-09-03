#!/usr/bin/env python3
"""close_main.py — the guarded build of the MAIN bundle, for Register entries and its counts.

    python3 tools/close_main.py --old OLD --new NEW --entries ENTRIES.md [--recount]
                               [--tag BUILD91_main] [--restage]

`close.py` builds the compendia bundle. It reads the main bundle only to compute the manifest and
never writes it, so a Register entry has had no route into the store of record and the Register's
own counts have had no route at all — they are two numerals INSIDE a member, and `close.py`'s
change-set assertion (every changed member equals old body + appended text) refuses that by design.
This is the missing half, built to the same discipline:

  1. NEW must not exist; the entries must be well formed and continue the Register's numbering
     without collision.
  2. The entries are appended to the Register member's body, which is the only member that changes.
  3. With --recount, the front and back matter figures are recomputed FROM THE APPENDED REGISTER
     and rewritten in place — the one edit `close.py` cannot make. Each site keeps its own
     thousands-separator convention; only digits move.
  4. Change set: no other member differs, byte for byte.
  5. REVERSE GUARD: the appended entries are stripped and every count edit undone, and the result
     must reproduce the old bundle's own md5. Nothing is written until it does.
  6. Only then is NEW written.

--restage additionally re-extracts method/members/, regenerates method/MEMBER-INDEX.tsv and
updates method/verify.py's two constants, so `python3 method/verify.py` passes against the new
bundle rather than the old one.

Note what this does NOT do. The compendia bundle's MANIFEST.tsv records the main bundle's members
by size and md5, so a main build makes those two rows stale until the next `close.py` run
regenerates them. That is reported, not silently repaired.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import register_counts as rc

MEMBER = re.compile(rb"^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n", re.S | re.M)
HEAD = re.compile(r"^### (\d{1,4})\s*$", re.M)
REGISTER = "The_Method_1_6___The_Register-2.md"

md5 = lambda b: hashlib.md5(b).hexdigest()


def parse(raw: bytes):
    ms = [(m.group(1).decode(), m.group(2), m.start(2)) for m in MEMBER.finditer(raw)]
    assert len({n for n, _, _ in ms}) == len(ms), "duplicate member name"
    return ms


def recount(body_text: str):
    """Rewrite every count the front matter carries, from the body's own text.

    Two sets, and both move when entries are seated. The EXTENT — total, range, mature — comes
    from the headings. The KIND table, "What the entries are", comes from the seated classifier
    kinds.py, run over the appended Register rather than the old one. Seating seven corrections
    in one session moved `a correction` from 149 to 156 with nothing maintaining it, which is
    what this second half exists to prevent.

    Returns (new_text, edits), the edits being the exact (old, new) pairs so the reverse guard
    can undo them."""
    c = rc.count(body_text)
    hi, edits = c["highest"], []

    def sub(pattern, build, text):
        m = pattern.search(text)
        if not m:
            return text
        old, new = m.group(0), build(m)
        if old == new:
            return text
        edits.append((old, new))
        return text[:m.start()] + new + text[m.end():]

    t = body_text
    t = sub(rc.FRONT_TOTAL,
            lambda m: f"{m.group(1)}{rc.like(m.group(2), c['headings'])} entries, "
                      f"1 to {hi}{m.group(4)}", t)
    t = sub(rc.FRONT_MATURE,
            lambda m: f"{m.group(1)}{hi}{m.group(3)}"
                      f"{rc.like(m.group(4), c['mature'])}{m.group(5)}", t)
    t = sub(rc.BACK, lambda m: f"{m.group(1)}{hi}{m.group(3)}", t)
    # the kind table, measured on the appended Register by the seated classifier
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as fh:
        fh.write(t)
        tmp = pathlib.Path(fh.name)
    try:
        km = rc.kinds_measured(tmp)
    finally:
        tmp.unlink(missing_ok=True)
    if km:
        for m in list(rc.KIND_ROW.finditer(t)):
            want = km.get(m.group(1))
            if want is None:
                continue
            old = m.group(0)
            new = f"| **{m.group(1)}** | {rc.like(m.group(2), want)} |"
            if old != new:
                edits.append((old, new))
                t = t.replace(old, new, 1)
    # the back matter repeats the total in its own sentence
    for m in list(re.finditer(r"(\*\*)(\d[\d,]*)( entries, 1 to )(\d+)(\*\*)", t)):
        old = m.group(0)
        new = (f"{m.group(1)}{rc.like(m.group(2), c['headings'])}"
               f"{m.group(3)}{hi}{m.group(5)}")
        if old != new:
            edits.append((old, new))
            t = t.replace(old, new)
    return t, edits


def find_root():
    """The repository root, whether this runs seated (members/) or from tools/."""
    here = pathlib.Path(__file__).resolve().parent
    for c in (here.parent, here.parent.parent, here.parent.parent.parent):
        if (c / "method" / "members").is_dir():
            return c
    return here.parent


def main(argv=None):
    root = find_root()
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--old", required=True)
    p.add_argument("--new", required=True)
    p.add_argument("--entries", help="Markdown file of new '### N' Register entries")
    p.add_argument("--recount", action="store_true",
                   help="recompute the front and back matter figures from the appended Register")
    p.add_argument("--tag", default=None, help="bundle tag for --restage, e.g. BUILD91_main")
    p.add_argument("--restage", action="store_true",
                   help="re-extract members/, regenerate MEMBER-INDEX.tsv, update verify.py")
    a = p.parse_args(argv)

    old_p, new_p = pathlib.Path(a.old), pathlib.Path(a.new)
    assert not new_p.exists(), f"{new_p} exists — never overwrite"
    old = old_p.read_bytes()
    ms = parse(old)
    names = [n for n, _, _ in ms]
    assert REGISTER in names, f"{old_p.name} carries no {REGISTER}"
    reg_old = dict((n, b) for n, b, _ in ms)[REGISTER]
    reg_text = reg_old.decode("utf-8")

    nl = b"\n"
    print(f"old {old_p.name}")
    print(f"    {len(old):,} B  md5 {md5(old)}  {old.count(nl):,} lines  {len(ms)} members")

    before = rc.count(reg_text)
    appended = ""
    if a.entries:
        appended = pathlib.Path(a.entries).read_text(encoding="utf-8")
        assert appended.startswith("### "), "entries must begin with a '### N' heading"
        assert appended.endswith("\n"), "entries must end with a newline"
        nums = [int(x) for x in HEAD.findall(appended)]
        assert nums, "no '### N' headings found in the entries file"
        assert nums == sorted(nums) and len(set(nums)) == len(nums), "entry numbers not ascending"
        assert nums[0] == before["highest"] + 1, (
            f"entries start at {nums[0]}; the Register's highest is {before['highest']}, "
            f"so the next is {before['highest'] + 1}")
        assert nums == list(range(nums[0], nums[0] + len(nums))), "entry numbers are not contiguous"
        existing = {int(x) for x in HEAD.findall(reg_text)}
        assert not (set(nums) & existing), f"collision with existing entries: " \
                                           f"{sorted(set(nums) & existing)}"
        print(f"    appending {len(nums)} entries: {nums[0]}–{nums[-1]}")

    reg_new_text = reg_text + appended
    edits = []
    if a.recount:
        reg_new_text, edits = recount(reg_new_text)
        for o, n in edits:
            print(f"    recount: {o.strip()[:70]}\n          -> {n.strip()[:70]}")
        if not edits:
            print("    recount: figures already current, nothing to change")
    after = rc.count(reg_new_text)
    print(f"    Register {before['headings']:,} -> {after['headings']:,} headings, "
          f"highest {before['highest']} -> {after['highest']}")

    reg_new = reg_new_text.encode("utf-8")
    block = lambda n, b: b"<<<FILE: " + n.encode() + b">>>\n" + b + b"<<<END FILE: " + n.encode() + b">>>\n"
    assert old.count(block(REGISTER, reg_old)) == 1, "the Register block is not unique"
    new = old.replace(block(REGISTER, reg_old), block(REGISTER, reg_new))

    # (4) change set
    nd = dict((n, b) for n, b, _ in parse(new))
    od = dict((n, b) for n, b, _ in ms)
    changed = [n for n in names if nd[n] != od[n]]
    assert changed == [REGISTER], f"unexpected change in members: {changed}"
    print(f"new {new_p.name}")
    print(f"    {len(new):,} B  md5 {md5(new)}  {new.count(nl):,} lines  "
          f"{len(nd)} members;  changed: {changed}")

    # (5) reverse guard
    rev_text = reg_new_text
    for o, n in reversed(edits):
        assert rev_text.count(n) >= 1, "reverse: edited text not found"
        rev_text = rev_text.replace(n, o, 1)
    assert rev_text.endswith(appended) if appended else True, "reverse: appended text not at the end"
    rev_text = rev_text[:len(rev_text) - len(appended)] if appended else rev_text
    rev = old.replace(block(REGISTER, reg_old), block(REGISTER, rev_text.encode("utf-8")))
    print(f"    reverse recovers md5 {md5(rev)}  == old: {md5(rev) == md5(old)}")
    assert md5(rev) == md5(old), "REVERSE GUARD FAILED — nothing written"

    # (6) write
    new_p.write_bytes(new)
    print(f"    written {new_p}")

    print("\nMANIFEST.tsv in the compendia bundle records this bundle's members by size and md5.")
    print(f"  {REGISTER} is now {len(reg_new):,} B / {md5(reg_new)} — that row is STALE until the")
    print("  next close.py run regenerates it. Not repaired here.")

    if a.restage:
        tag = a.tag
        assert tag, "--restage needs --tag, e.g. --tag BUILD91_main"
        mem = root / "method" / "members"
        idx = root / "method" / "MEMBER-INDEX.tsv"
        rows = [l.rstrip("\n").split("\t") for l in idx.read_text(encoding="utf-8").splitlines()]
        head, body = rows[0], rows[1:]
        old_tag = {r[1] for r in body if r[0] == REGISTER}.pop()
        keep = [r for r in body if r[1] != old_tag]
        for n, b, off in parse(new):
            (mem / n).write_bytes(b)
            keep.append([n, tag, pathlib.Path(n).suffix, str(len(b)), md5(b), str(off)])
        keep.sort(key=lambda r: (r[1], r[0]))
        idx.write_text("\t".join(head) + "\n"
                       + "\n".join("\t".join(r) for r in keep) + "\n", encoding="utf-8")
        vp = root / "method" / "verify.py"
        v = vp.read_text(encoding="utf-8")
        v = v.replace(f"'{old_tag}': '{old_p.name}'", f"'{tag}': '{new_p.name}'")
        v = re.sub(rf"'{re.escape(old_tag)}': '[0-9a-f]{{32}}'", f"'{tag}': '{md5(new)}'", v)
        vp.write_text(v, encoding="utf-8")
        print(f"\nrestaged: {len(parse(new))} members re-extracted, "
              f"MEMBER-INDEX.tsv regenerated, verify.py retargeted {old_tag} -> {tag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
