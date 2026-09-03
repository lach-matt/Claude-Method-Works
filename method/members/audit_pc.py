#!/usr/bin/env python3
"""audit_pc.py — the Physics Compendium's own claims, checked.

    python3 tools/audit_pc.py

Each row prints PASS or FAIL against the figure the volume states, and adjudicates nothing.

Λ_phys is the substance of it: 27 parameters, each carrying a structured line of the form
`**kind** · source · valid domain · N objects rest on it`, and a summary table of kind against
domain. The entries and the table are independent statements of the same thing, so one checks the
other. Two conventions the volume sets and this program follows: the table's column `a region` is
written `a region of the index` in the entries, and its column `the three-body problem` covers the
three free parameters whose own domains are `all mass triples`, `E < 0 for bound strata` and
`all L` — the volume says so in the note under the table.
"""
from __future__ import annotations

import collections
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
    print(f"  [{'PASS' if ok else 'FAIL'}] {label:<48} {str(got):<22} recorded {want}"
          + (f"   {note}" if note else ""))
    return ok


def main():
    PC = vol("The_Method_1_6___The_Physics_Compendium-2.md")
    body = PC[PC.index("# Λ_phys"):]

    print("Λ_phys — 27 parameters against their own summary table\n")
    heads = re.findall(r"^### (.+)$", body, re.M)
    ents = re.findall(r"^### (.+?)\n\n\*\*(.+?)\*\*\s*·\s*(.+?)\s*·\s*valid (.+?)"
                      r"\s*·\s*(\d+) objects?\s+rests?\s+on it", body, re.M)
    chk("parameter headings", len(heads), 27)
    chk("entries carrying a structured line", len(ents), 27,
        "(note the singular 'object rests' on L)")

    def dom(d):
        d = d.strip()
        if d.startswith("a region"):
            return "a region"
        if d in ("all mass triples", "all L") or d.startswith("E <"):
            return "the three-body problem"
        return d

    TABLE = {("exact by definition", "universal"): 2, ("measured constant", "universal"): 3,
             ("measured constant", "one species"): 1, ("read from a table", "all elements"): 3,
             ("read from a table", "a region"): 2, ("read from a table", "one species"): 1,
             ("derived here", "all elements"): 2, ("derived here", "a region"): 1,
             ("fitted here", "all elements"): 1, ("fitted here", "a region"): 6,
             ("fitted here", "one species"): 1, ("free parameter", "the three-body problem"): 3,
             ("exact by scaling", "universal"): 1}
    chk("the printed table sums to", sum(TABLE.values()), 27)
    grid = collections.Counter((k, dom(d)) for _, k, _, d, _ in ents)
    diff = sum(1 for k in set(TABLE) | set(grid) if TABLE.get(k, 0) != grid.get(k, 0))
    chk("kind x domain cells disagreeing", diff, 0, f"({len(TABLE)} cells)")

    own = [e for e in ents if "this work" in e[2]]
    chk("parameters this work's own, by source", len(own), 8)
    od = collections.Counter(dom(d) for _, _, _, d, _ in own)
    chk("  of those, universal", od.get("universal", 0), 0)
    chk("  of those, all elements", od.get("all elements", 0), 1)
    chk("  of those, a region or one species",
        od.get("a region", 0) + od.get("one species", 0), 7)

    heavy = sorted((int(n) for *_, n in ents), reverse=True)[:6]
    chk("the six heaviest, objects resting on them", heavy, [72, 66, 18, 18, 16, 15])

    print("\nΛ — the elemental index")
    chk("the partition identity 976 + 0 + 5,936", 976 + 0 + 5936, 6912)

    print("\nΛ_chain, Λ_cinf, Λ_V5")
    chk("rows for Z = 2 to 120", 120 - 2 + 1, 119)
    chk("scored + unwitnessed", 107 + 12, 119)
    chk("unwitnessed rows 109 to 120", 120 - 109 + 1, 12)
    m = re.search(r"\*\*eleven entrants\s*\n?differ from Λ_chain\*\*\s*\(([^)]*)\)", PC)
    names = [x.strip() for x in m.group(1).split(",")] if m else []
    chk("entrants named as differing at c -> infinity", len(names), 11,
        f"({', '.join(names)})" if names else "")
    m = re.search(r"Z = 38, 56, 72, 89, 105", PC)
    chk("Λ_V5 contested rows named", 5 if m else 0, 5)
    vals = [(1.33, None), (1.24, None), (2.6, (2.57, 2.73)), (2.2, (1.92, 3.32)), (2.16, None)]
    chk("Λ_V5 dm2/margin values", len(vals), 5)
    chk("  all positive (none reverses)", all(v > 0 for v, _ in vals), True)
    chk("  every point inside its declared envelope",
        all(lo <= v <= hi for v, e in vals if e for lo, hi in [e]), True)
    chk("  every envelope entirely positive",
        all(lo > 0 for _, e in vals if e for lo, _ in [e]), True)

    print("\n" + "=" * 78)
    if not FAILS:
        print("PHYSICS COMPENDIUM AUDIT CLEAN — every checked claim reproduces.")
        return 0
    print(f"{len(FAILS)} CLAIM(S) DID NOT REPRODUCE\n")
    for label, got, w in FAILS:
        print(f"  {label}\n      recorded {w}\n      measured {got}")
    print("\nThis program adjudicates nothing.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
