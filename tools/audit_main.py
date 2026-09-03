#!/usr/bin/env python3
"""audit_main.py — the main volume's structure, checked against itself.

    python3 tools/audit_main.py

The volume carries a table of contents and then the body, so the two are independent statements of
the same structure and each checks the other. Each row prints PASS or FAIL and adjudicates nothing.

Two conventions the volume sets and this program follows, because getting either wrong produces a
false FAIL. Appendix A numbers nineteen theorems but writes out only ten: its own second sentence
says *"Nine proofs are given in full in the chapters and are cross-referenced here. The remaining
ten are written out below — nineteen in all,"* and the nine are tabulated with where each is
proved, so a missing `### A.N` heading is the design and not a gap. And the principles P1 to P19
are tabulated in Chapter 1 rather than headed; only P20 to P23 carry `PN — ` lines. Principle
numbering is docket 33 and is not re-raised here.
"""
from __future__ import annotations

import pathlib
import re
import sys

FAILS = []


def chk(label, got, want, note=""):
    ok = got == want
    if not ok:
        FAILS.append((label, got, want))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label:<52} {str(got):<16} recorded {want}"
          + (f"   {note}" if note else ""))
    return ok


def main():
    here = pathlib.Path(__file__).resolve().parent
    for base in (here, here.parent / "method" / "members",
                 here.parent.parent / "method" / "members"):
        p = base / "The_Method_1_6-2.md"
        if p.exists():
            break
    else:
        sys.exit("The_Method_1_6-2.md not found beside this file or under method/members/")
    T = p.read_text(encoding="utf-8")
    L = T.split("\n")
    body0 = next(i for i, l in enumerate(L) if l.startswith("# PART 0") and i > 150)
    toc, body = L[:body0], L[body0:]

    print("CONTENTS AGAINST BODY\n")
    bc = [(int(m.group(1)), m.group(2).strip())
          for m in (re.match(r"^## (\d+)\. (.+)$", l) for l in body) if m]
    th = [(int(m.group(1)), m.group(2).strip())
          for m in (re.match(r"^## (\d+)\. (.+)$", l) for l in toc) if m]
    tb = [(int(m.group(1)), m.group(2).strip())
          for m in (re.match(r"^\s+(\d+)\. (.+)$", l) for l in toc) if m]
    chk("chapters in the body", len(bc), 36)
    chk("body numbering contiguous 1..36",
        sorted(n for n, _ in bc) == list(range(1, 37)), True)
    chk("chapters listed in the contents", len(th) + len(tb), 36, "(none is missing)")
    db, dt = dict(bc), dict(th + tb)
    chk("titles differing between contents and body",
        len([n for n in db if n in dt and db[n] != dt[n]]), 0)

    print("\n  FINDING — how they are listed")
    print(f"    listed as '## N. Title' headings : {len(th)}")
    print(f"    listed as plain indented text    : {len(tb)}  "
          f"{[n for n, _ in tb]}")
    chk("every chapter listed with the same marker", len(tb), 0,
        "<-- the two are PART IV's, and only PART IV's")

    parts = {}
    cur = None
    for l in toc:
        m = re.match(r"^# (PART [0IV]+)", l)
        if m:
            cur = m.group(1)
            parts.setdefault(cur, 0)
        elif cur and re.match(r"^## \d+\. ", l):
            parts[cur] += 1
    empty = [k for k, v in parts.items() if v == 0 and k != "PART 0"]
    chk("parts showing no chapters when counted as headings", empty, [],
        "<-- PART IV's two are the plain-text ones")

    print("\nAPPENDIX A — nineteen theorems, nine cross-referenced and ten written out")
    # The contents lists every appendix too, so anchor on the LAST occurrence — the body's.
    # Anchoring on the first "# PART 0" after an offset lands in the contents and yields the
    # one-line entry rather than the appendix.
    a = T.rindex("## Appendix A — Proofs")
    b = T.index("## Appendix B", a)
    seg = T[a:b]
    written = sorted({int(m.group(1)) for m in re.finditer(r"^### A\.(\d+)", seg, re.M)})
    xref = sorted({int(m.group(1)) for m in
                   re.finditer(r"^\s+A\.(\d+)\s{2,}", seg, re.M)})
    chk("theorems written out below", len(written), 10, f"{written}")
    chk("theorems cross-referenced in the table", len(xref), 9, f"{xref}")
    chk("nineteen in all", len(written) + len(xref), 19)
    chk("the two sets do not overlap", sorted(set(written) & set(xref)), [])
    chk("together they cover A.1 to A.19",
        sorted(set(written) | set(xref)) == list(range(1, 20)), True)

    print("\nAPPENDICES")
    ta = [m.group(1) for m in (re.match(r"^## Appendix ([A-G])\b", l) for l in toc) if m]
    ba = [m.group(1) for m in (re.match(r"^## Appendix ([A-G])\b", l) for l in body) if m]
    chk("appendices in the contents", ta, list("ABCDEFG"))
    chk("appendices in the body", ba, list("ABCDEFG"))

    print("\n" + "=" * 78)
    if not FAILS:
        print("MAIN VOLUME AUDIT CLEAN — every checked claim reproduces.")
        return 0
    print(f"{len(FAILS)} CLAIM(S) DID NOT REPRODUCE\n")
    for label, got, w in FAILS:
        print(f"  {label}\n      recorded {w}\n      measured {got}")
    print("\nThis program adjudicates nothing.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
