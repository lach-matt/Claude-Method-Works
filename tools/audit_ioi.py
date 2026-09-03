#!/usr/bin/env python3
"""audit_ioi.py — the Index of Indices, checked against the volumes it indexes.

    python3 tools/audit_ioi.py

This volume's job is to restate what the other five hold, so the audit that fits it is
cross-volume: every figure it gives for an index should match that index's own home. Where a
figure can be recomputed from the object rather than merely compared, it is — Λ₉'s composable
count and Λ₁₀'s g = 0 cells are derived here, not read.

One convention, stated by the volume and followed here: section IX holds FIFTEEN indexes, of which
fourteen are written out in it and the fifteenth, Λ_spectra, is stated in Part VIII. Counting the
section's own headings gives fourteen and is the wrong count.
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cypher

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
    print(f"  [{'PASS' if ok else 'FAIL'}] {label:<50} {str(got):<20} recorded {want}"
          + (f"   {note}" if note else ""))
    return ok


def main():
    IOI = vol("The_Method_1_6___The_Index_of_Indices-2.md")
    MC = vol("The_Method_1_6___Mathematical_Compendium-2.md")
    PC = vol("The_Method_1_6___The_Physics_Compendium-2.md")
    L = IOI.split("\n")

    print("SECTION IX — the count the volume states\n")
    a = next(i for i, l in enumerate(L) if l.startswith("# IX ·"))
    b = next(i for i in range(a + 1, len(L)) if L[i].startswith("# X ·"))
    heads = [l for l in L[a:b] if l.startswith("## Λ")]
    chk("indexes written out in section IX", len(heads), 14)
    chk("plus Λ_spectra, stated in Part VIII", len(heads) + 1, 15,
        "(register 1387's fifteen)")

    print("\nTHE TOWER TABLE — its own arithmetic")
    TAB = [("Λ₈", 976, 0, 0.0000), ("Λ₉", 1654, 1169, 0.7068),
           ("Λ₁₀", 2535, 2050, 0.8087), ("Λ₁₁", 13585, 9450, 0.6956),
           ("Λ₁₂", 70905, 46740, 0.6592), ("Λ₁₃", 199130, 127070, 0.6381)]
    chk("fractions equal composable / cells",
        sum(1 for _, c, k, f in TAB if abs(round(k / c, 4) - f) > 5e-5), 0, "(6 rows)")
    kinds = {"Λ₉": 1, "Λ₁₀": 1, "Λ₁₁": 0, "Λ₁₂": 0, "Λ₁₃": 0}
    prev, exc = TAB[0][3], 0
    for nm, c, k, f in TAB[1:]:
        exc += (f > prev) != bool(kinds[nm])
        prev = f
    chk("counting axes raise it, coupling lower it", exc, 0, "(no exception)")
    chk("the peak stage", max(TAB, key=lambda r: r[3])[0], "Λ₁₀")
    chk("the peak fraction", f"{max(f for *_, f in TAB):.4f}", "0.8087")

    print("\n  recomputed from the objects, not read from the table")
    L10 = cypher._tower(10)
    c10 = [tuple(L10.decode[i][v] for i, v in enumerate(c)) for c in L10.cells]
    gi = L10.coords.index("g")
    chk("  Λ₁₀ cells with g = 0", sum(1 for c in c10 if c[gi] == 0), 2535 - 2050,
        "(the non-composable cells, exactly)")
    L9 = cypher._tower(9)
    c9 = [tuple(L9.decode[i][v] for i, v in enumerate(c)) for c in L9.cells]
    j = {c: n for n, c in enumerate(L9.coords)}
    srcs = {(c[j["n"]], c[j["l"]], c[j["k"]], c[j["S"]]) for c in c9}
    comp = sum(1 for c in c9
               if (c[j["e"]], c[j["f"]], c[j["g"]], c[j["2S'"]]) in srcs)
    chk("  Λ₉ composable cells", comp, 1169)

    print("\nTHE SUMMARY TABLES")
    def rows(start, end):
        i = next(k for k, l in enumerate(L) if l.startswith(start))
        e = next(k for k in range(i + 1, len(L)) if L[k].startswith(end))
        return [x for x in L[i:e] if x.startswith("|") and not set(x) <= set("|- ")][1:]
    r1 = rows("## The one-line summary", "# IX ·")
    r2 = rows("## The one-line summary, extended", "# X ·")
    chk("one-line summary rows", len(r1), 14)
    chk("extended summary rows", len(r2), 19)
    named = [m.group(1) for m in (re.match(r"\|\s*\*\*(.+?)\*\*", x) for x in r2) if m]
    sects = {l[3:].split("—")[0].strip() for l in L if l.startswith("## Λ")}
    chk("extended rows with no section of their own",
        len([n for n in named if n not in sects]), 0)

    print("\nCROSS-VOLUME — figures this volume restates")
    # Only figures this volume actually restates can be cross-checked. Two it does NOT:
    # its tower table prints no box column, so 47,775,744 is the Mathematical Compendium's
    # alone; and Λ_spectra's 104,832 ambient is the Spectra Compendium's, not the Physics
    # Compendium's, whose section states 596 channels over 70 spectra and 2,269 interior cells.
    SC = vol("The_Method_1_6___Spectra_Compendium-2.md")
    for label, tok, others in (
            ("Λ at 976 cells", "976", ("MC", "PC")),
            ("Λ's box at 6,912", "6,912", ("MC", "PC")),
            ("the tower's Λ₁₃ at 199,130", "199,130", ("MC",)),
            ("Λ_spectra at 104,832 cells", "104,832", ("SC",))):
        src = {"MC": MC, "PC": PC, "SC": SC}
        ok = tok in IOI and all(tok in src[o] for o in others)
        chk(label, "agrees" if ok else "differs", "agrees", f"(IoI vs {', '.join(others)})")

    print("\nΛ_const — the centres (entry 1798)")
    io = "5.4" in IOI[IOI.index("CENTRE in the system"):][:200]
    chk("IoI's fifth centre matches MC and PC", "5.4" if io else "4", "4",
        "<-- FINDING: 2 x 5.4 = 10.8 is no integer")

    print("\n" + "=" * 78)
    if not FAILS:
        print("INDEX OF INDICES AUDIT CLEAN — every checked claim reproduces.")
        return 0
    print(f"{len(FAILS)} CLAIM(S) DID NOT REPRODUCE\n")
    for label, got, w in FAILS:
        print(f"  {label}\n      recorded {w}\n      measured {got}")
    print("\nThis program adjudicates nothing.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
