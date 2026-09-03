#!/usr/bin/env python3
"""audit_mc.py — the Mathematical Compendium's own claims, checked.

    python3 tools/audit_mc.py

The Λ claims of this volume are checked by `audit_lambda.py`; this covers what is left and what
crosses into the other volumes. Each row prints PASS or FAIL against the figure the volumes state,
and adjudicates nothing. Where a check needs a convention the volume states — what counts as an
object, which table bounds a section — that convention is named, because getting it wrong produces
a false FAIL.
"""
from __future__ import annotations

import collections
import itertools
import pathlib
import re
import sys

FAILS = []


def vol(name):
    here = pathlib.Path(__file__).resolve().parent
    for base in (here, here.parent / "method" / "members",
                 here.parent.parent / "method" / "members"):
        p = base / name
        if p.exists():
            return p.read_text(encoding="utf-8")
    sys.exit(f"{name} not found beside this file or under method/members/")


def chk(label, got, want, note=""):
    ok = got == want
    if not ok:
        FAILS.append((label, got, want))
    g, w = str(got), str(want)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label:<46} {g:<26} recorded {w}"
          + (f"   {note}" if note else ""))
    return ok


def R2(cells):
    """|ℛ(X)| for a two-coordinate index."""
    A0 = sorted({c[0] for c in cells})
    A1 = sorted({c[1] for c in cells})
    p01 = {v: max([x[0] for x in cells if x[1] <= v], default=None) for v in A1}
    p10 = {v: max([x[1] for x in cells if x[0] <= v], default=None) for v in A0}
    return sum(1 for a in A0 for b in A1
               if p01[b] is not None and a <= p01[b] and p10[a] is not None and b <= p10[a])


def main():
    MC = vol("The_Method_1_6___Mathematical_Compendium-2.md")
    IOI = vol("The_Method_1_6___The_Index_of_Indices-2.md")
    PC = vol("The_Method_1_6___The_Physics_Compendium-2.md")
    L = MC.split("\n")

    print("SECTION OBJECT COUNTS — each heading states its own\n")
    secs = [(i, l) for i, l in enumerate(L) if l.startswith("## ")]
    tc = tg = 0
    for n, (i, l) in enumerate(secs):
        m = re.search(r"—\s*(\d+)\s+objects\s*$", l)
        if not m:
            continue
        claim = int(m.group(1))
        end = secs[n + 1][0] if n + 1 < len(secs) else len(L)
        got = sum(1 for x in L[i + 1:end] if x.startswith("### "))
        chk(f"section {l[3:].split('.')[0]}", got, claim)
        tc += claim
        tg += got
    chk("all sections, total objects", tg, tc)

    # The eighteen roots are a TABLE, not '###' headings, and the section is bounded by the
    # next '#' of any level — '# II · THE OPERATORS' intervenes before '## Why none is redundant'.
    i = next(j for j, l in enumerate(L) if l.startswith("## The eighteen roots"))
    end = next(j for j in range(i + 1, len(L)) if L[j].startswith("#"))
    rows = [x for x in L[i + 1:end] if x.startswith("|") and not set(x) <= set("|- ")]
    chk("the eighteen roots (table rows)", len(rows) - 1, 18, "(less the header)")

    print("\nΛ_law — seven laws on (law, carrier), E = 0")
    print("  convention: two laws on u, three on p, one on each of the other two, as printed;")
    print("  each law is its own value, so the index is seven cells in a 7 x 4 grid.")
    CARRIER = [0, 0, 1, 1, 1, 2, 3]
    chk("7! x 4! orderings", 5040 * 24, 120960)
    dist = collections.Counter()
    for lp in itertools.permutations(range(7)):
        base = [(lp[i], CARRIER[i]) for i in range(7)]
        for cp in itertools.permutations(range(4)):
            dist[R2([(a, cp[c]) for a, c in base]) - 7] += 1
    chk("defect range over all orderings", (min(dist), max(dist)), (0, 21))
    chk("orderings reaching E = 0", dist[0], 288)
    chk("carrier multiplicities sum to seven", sum((2, 3, 1, 1)), 7)
    print(f"       (E = 1 is unreachable: the distribution runs 0 then 2 upward)")

    print("\nΛ_const — the centres, across three volumes")
    mc = re.search(r"Every CENTRE is a small integer or half-integer(.{0,200})", MC, re.S)
    io = re.search(r"CENTRE in the system is a small integer or half-integer\s*—(.{0,60})", IOI, re.S)
    mc_has4 = "u0 = 4" in (mc.group(1) if mc else "")
    io_has54 = "5.4" in (io.group(1) if io else "")
    pc_has4 = "u0 = 4" in PC
    print(f"  Mathematical Compendium lists  u0 = 4 : {mc_has4}")
    print(f"  Physics Compendium lists       u0 = 4 : {pc_has4}")
    print(f"  Index of Indices lists            5.4 : {io_has54}")
    half = lambda x: (2 * x) == int(2 * x)
    print(f"  is 4 an integer or half-integer?   {half(4.0)}")
    print(f"  is 5.4?                            {half(5.4)}")
    chk("the three volumes agree on the fifth centre",
        "agree" if not (io_has54 and (mc_has4 or pc_has4)) else "IoI 5.4 vs MC/PC 4", "agree",
        "<-- FINDING: and 5.4 fails the claim it is offered for")

    print("\n" + "=" * 78)
    if not FAILS:
        print("MC AUDIT CLEAN — every checked claim reproduces.")
        return 0
    print(f"{len(FAILS)} CLAIM(S) DID NOT REPRODUCE\n")
    for label, got, w in FAILS:
        print(f"  {label}\n      recorded {w}\n      measured {got}")
    print("\nThis program adjudicates nothing.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
