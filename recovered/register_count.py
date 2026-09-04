#!/usr/bin/env python3
"""register_count.py — THE DECLARED COUNTING INSTRUMENT FOR THE REGISTER (R 1730).

Three sessions measured `REGISTER-DATA.md` and reported 1,352, 1,483 and 1,486.
All three were correct; none was declared. R 1706 recorded the same gap from the
other side — the book's §26 tripwire can no longer recompute its own register
range, and per the null protocol the gap wants a different instrument than a
regex over §28 prose.

DECLARED CANONICAL: `entries` — the count of DISTINCT entry ids, suffixes
included. It is the only reading that counts each entry exactly once whatever
its formatting, and it is the number the bridges have cited.

The other two are printed alongside, never silently: an entry authored without
bold headings is still an entry, and the gap between `numbered` and `entries`
is exactly the suffixed ids (368a, 1215a, 1476a — R 1691's 368a precedent).

This instrument REPORTS. It does not gate, and it is not wired into the press:
that is a change to the book press and M has not ruled on it (R 1706).
"""
import re, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "REGISTER-DATA.md"
text = open(SRC, encoding="utf-8").read()

HEADING = re.compile(r"^ {0,3}(\d{3,4})([a-z]?)\. ", re.M)
BOLDED  = re.compile(r"^ {0,3}\d{3,4}[a-z]?\. \*\*", re.M)

ids = [m.group(1) + m.group(2) for m in HEADING.finditer(text)]
distinct = sorted(set(ids))
numeric = sorted({int(m.group(1)) for m in HEADING.finditer(text)})
suffixed = sorted(i for i in distinct if not i.isdigit())
dupes = sorted({i for i in ids if ids.count(i) > 1})

print(f"source            {SRC}")
print(f"entries           {len(distinct)}      <- DECLARED CANONICAL (distinct ids)")
print(f"numbered headings {len(ids)}")
print(f"bolded headings   {len(BOLDED.findall(text))}")
print(f"max id            {numeric[-1]}")
print(f"min id            {numeric[0]}")
print(f"suffixed ids      {len(suffixed)}  {' '.join(suffixed)}")
print(f"duplicates        {len(dupes)}  {' '.join(dupes) if dupes else '(none)'}")

# The check must be capable of failing (§4.6): a duplicate id is a fault.
sys.exit(1 if dupes else 0)
