#!/usr/bin/env python3
"""Part-to-chapter fibre map: contents against body.

Audits 6 (COHERENCE) and 20 (PROJECTION) compare the *set* of headings in the
contents against the set in the body.  A chapter listed under one Part in the
contents and printed under another Part in the body has identical set
membership on both sides and is invisible to both.  This computes the two
fibre maps and returns the symmetric difference.
"""
import re, sys
from zeno import State, step

SRC = "The Method 1.6.md"
s = open(SRC, encoding="utf-8").read()
lines = s.split("\n")

PART = re.compile(r"^# (PART [^\n]*|APPENDICES|END MATTER)\s*$")
CHAP = re.compile(r"^## (\d+)\. (.*)$")

# the contents block runs from the first PART heading to the second occurrence
# of "# PART 0", which is where the body begins.
starts = [i for i, l in enumerate(lines) if l.startswith("# PART 0")]
assert len(starts) >= 2, starts
contents_lo, contents_hi = starts[0], starts[1]


def fibre(lo, hi):
    """map chapter number -> the Part heading in force at that point"""
    part, out = None, {}
    for i in range(lo, hi):
        m = PART.match(lines[i])
        if m:
            part = m.group(1)
            continue
        c = CHAP.match(lines[i])
        if c:
            out.setdefault(int(c.group(1)), (part, c.group(2), i + 1))
    return out


with State("fibre") as st:
    toc = step(st, "contents fibre", lambda: fibre(contents_lo, contents_hi), budget=10)
    body = step(st, "body fibre", lambda: fibre(contents_hi, len(lines)), budget=10)

toc = {int(k): v for k, v in toc.items()}
body = {int(k): v for k, v in body.items()}

print(f"\n  chapters in contents: {len(toc)}   chapters in body: {len(body)}")
print(f"  set membership equal: {set(toc) == set(body)}")

bad = []
for ch in sorted(set(toc) & set(body)):
    if toc[ch][0] != body[ch][0]:
        bad.append((ch, toc[ch], body[ch]))

print(f"\n  part-to-chapter fibre disagreements: {len(bad)}")
for ch, t, b in bad:
    print(f"\n    chapter {ch} — {b[1]}")
    print(f"      contents  line {t[2]:>5}   {t[0]}")
    print(f"      body      line {b[2]:>5}   {b[0]}")

# what each Part holds, both sides
print("\n  Part -> chapters")
for name, m in (("contents", toc), ("body", body)):
    d = {}
    for ch, (p, _, _) in sorted(m.items()):
        d.setdefault(p, []).append(ch)
    print(f"    {name}:")
    for p, chs in d.items():
        print(f"      {p:<32} {chs}")

sys.exit(len(bad))
