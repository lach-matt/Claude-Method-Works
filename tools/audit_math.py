#!/usr/bin/env python3
"""audit_math.py — the book's own mathematical objects read as an index, in five languages.

    python3 tools/audit_math.py

`dclose.py` is a seated instrument that treats the book's mathematical objects as an index: each
element is a (kind, discipline) fibre carrying a cell (status, verification, precedent), and it
reports E per fibre under an operator augmented with two domain rules. It finds E = 0 on all 24
fibres of its 77 elements — in the ORDER language alone.

This reads the same 77 elements in all five operator-bearing languages, three ways, and the third
produces a counterexample to the corpus's own agreement theorem.

  1. AS ONE OBJECT, kind and discipline on axes. Wide open — E = 492 in order, 1 of 10 pairs
     agreeing. That is the expected refutation, not a finding: kind and discipline are nominal,
     they individuate rather than order, and register 1356 names putting such a coordinate on an
     axis as the fault that voided Lambda_ladder. `dclose.py` fibres over them for that reason.

  2. PER FIBRE. What `dclose.py` measures, now in five languages rather than one.

  3. THE GRADING ALONE — (status, verification, precedent) over all 77 elements, every coordinate
     ordinal by construction. All five languages return the SAME 13-cell set and the index holds
     11, so the languages agree exactly and E = 2.

Register 1176 states E(X) = 0 IF AND ONLY IF the languages agree, on six indexes and three
operators, "without exception". The third reading is agreement WITHOUT closure, so the "only if"
half does not hold in general. The defect census already flags that entry's "without exception" as
C9-OVERGENERALISATION-WORD (row 1321); this supplies the exception it was flagged for.

The two cells the languages admit and the index lacks are `measured · exhaustive · found` and
`verified · sampled · found` — both gradings a mathematical object could carry, neither occurring
among the 77.
"""
from __future__ import annotations

import collections
import itertools
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cypher

STATUS = ["withdrawn", "conjectured", "measured", "verified", "proved"]
VERIF = ["cited", "sampled", "exhaustive"]
PRECED = ["none found", "found"]
OPTS = {"statistics_order": 2, "algebra_budget": 200000,
        "max_box": 10 ** 9, "max_pairwise_cells": 10 ** 9}


def elements():
    """The 77 elements dclose.py carries, read from the seated instrument itself."""
    here = pathlib.Path(__file__).resolve().parent
    for c in (here / "dclose.py", here.parent / "method" / "members" / "dclose.py",
              here.parent.parent / "method" / "members" / "dclose.py"):
        if c.exists():
            src = c.read_text(encoding="utf-8")
            break
    else:
        sys.exit("dclose.py not found beside this file or under method/members/")
    out = []
    for blk in re.findall(r'"""(.*?)"""', src, re.S):
        for line in blk.strip().splitlines():
            if "|" not in line:
                continue
            fib, name, cell = line.split("|")
            kind, disc = fib.split("·")
            a, b, c = [x.strip() for x in cell.split("·")]
            out.append((kind, disc, name, a, b, c))
    return out


def main():
    els = elements()
    kinds = sorted({k for k, *_ in els})
    discs = sorted({d for _, d, *_ in els})
    fibres = collections.defaultdict(list)
    for k, d, _, a, b, c in els:
        fibres[(k, d)].append((a, b, c))
    print(f"{len(els)} elements, {len(fibres)} (kind, discipline) fibres, "
          f"{len(kinds)} kinds, {len(discs)} disciplines\n")

    print("1. AS ONE OBJECT — kind and discipline on axes")
    cells = sorted({(k, d, a, b, c) for k, d, _, a, b, c in els})
    ix = cypher.Index("math index", ["kind", "discipline", "status", "verification", "precedent"],
                      [list(x) for x in cells],
                      value_order={"kind": kinds, "discipline": discs, "status": STATUS,
                                   "verification": VERIF, "precedent": PRECED})
    r = cypher.run(ix, "1173", OPTS)
    E = {v.language: v.E for v in r["_verdicts"] if v.E is not None}
    print(f"   cells {len(ix.cells)}  box {ix.box}   E: " +
          "  ".join(f"{k} {v}" for k, v in sorted(E.items())))
    print(f"   {r['pairs_agreeing']} of {len(r['pairs'])} pairs agree")
    print("   -> nominal coordinates on axes; the expected refutation, not a finding (reg 1356)\n")

    print("2. PER FIBRE — what dclose.py measures, in five languages")
    open_f = []
    for key, cs in sorted(fibres.items()):
        fx = cypher.Index("f", ["status", "verification", "precedent"],
                          [list(x) for x in sorted(set(cs))],
                          value_order={"status": STATUS, "verification": VERIF,
                                       "precedent": PRECED})
        fr = cypher.run(fx, "1173", OPTS)
        fe = {v.language: v.E for v in fr["_verdicts"] if v.E is not None}
        if any(v for v in fe.values()):
            open_f.append((key, len(fx.cells), fe))
    print(f"   {len(fibres)} fibres; {len(fibres) - len(open_f)} close at E = 0 in every language")
    for key, n, fe in open_f:
        print(f"   OPEN  {key[0]}·{key[1]:<18} {n} cells   " +
              "  ".join(f"{k} {v}" for k, v in sorted(fe.items())))
    print()

    print("3. THE GRADING ALONE — (status, verification, precedent) over all 77")
    g = sorted({(a, b, c) for *_, a, b, c in els})
    gx = cypher.Index("the grading", ["status", "verification", "precedent"],
                      [list(x) for x in g],
                      value_order={"status": STATUS, "verification": VERIF, "precedent": PRECED})
    sets = {}
    for nm, fn in (("order", cypher.op_order), ("algebra", cypher.op_algebra),
                   ("geometry", cypher.op_geometry), ("information", cypher.op_information),
                   ("statistics", cypher.op_statistics)):
        out, _ = fn(gx, OPTS)
        sets[nm] = frozenset(out)
    agree = len(set(sets.values())) == 1
    adm = next(iter(sets.values()))
    E = len(adm) - len(gx.cells)
    print(f"   cells {len(gx.cells)}  box {gx.box}   every language admits "
          f"{len(adm)}   E = {E}")
    print(f"   languages agree (identical admitted sets): {agree}")
    held = {tuple(gx.decode[i][v] for i, v in enumerate(c)) for c in gx.cells}
    for c in sorted(adm):
        t = tuple(gx.decode[i][v] for i, v in enumerate(c))
        if t not in held:
            print(f"     admitted and not held:  {t[0]:<12} {t[1]:<11} {t[2]}")
    ok = not (agree and E > 0)
    print(f"\n   K.langclose (E = 0 iff the languages agree): "
          f"{'holds' if ok else 'FAILS — agreement WITHOUT closure'}")
    if not ok:
        print("   Register 1176 states it on six indexes and three operators, without exception.")
        print("   This is an exception. Census row 1321 already flags that wording as")
        print("   C9-OVERGENERALISATION-WORD; this is the case it was flagged for.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
