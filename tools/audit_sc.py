#!/usr/bin/env python3
"""audit_sc.py — the Spectra Compendium, and the Löwdin solution it carries.

    python3 tools/audit_sc.py

The Spectra Compendium is the observation side of the Löwdin solution, so the LS objects of the
Mathematical Compendium and Λ_chain's derived supply are checked here with it — the two supplies
state the same quantities and each is a check on the other.

One claim does not hold. The twelve unwitnessed rows above Z = 108 are graded UNWITNESSED and
offered as theoretically established, on the argument that a worst-case spin-orbit narrowing of
0.083 Ha is cleared by every margin. The margins are printed in the same table as 0.058 to 0.264,
so at least one row does not clear it, and the main volume prints both figures in a single
sentence. See FINDING below.
"""
from __future__ import annotations

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
    print(f"  [{'PASS' if ok else 'FAIL'}] {label:<50} {str(got):<20} recorded {want}"
          + (f"   {note}" if note else ""))
    return ok


def main():
    SC = vol("The_Method_1_6___Spectra_Compendium-2.md")
    MC = vol("The_Method_1_6___Mathematical_Compendium-2.md")

    print("§0 — THE COORDINATE SUPPLY\n")
    chk("exact + measured + computed", 929 + 358 + 103545, 104832)
    chk("witnessed + unwitnessed", 358 + 104474, 104832)
    chk("fraction witnessed, to three places", round(358 / 104832 * 100, 3), 0.341)

    print("\n§0' — THE DERIVED SUPPLY, Λ_chain")
    chk("SCORED rows, Z = 2 to 108", 108 - 2 + 1, 107)
    chk("UNWITNESSED rows, Z = 109 to 120", 120 - 109 + 1, 12)
    chk("the two grades over the whole walk", 107 + 12, 119)
    bands = [("109-112", "6d", 4, 0.171, 0.264), ("113-118", "7p", 6, 0.058, 0.210),
             ("119,120", "8s", 2, 0.097, 0.098)]
    chk("the unwitnessed table's bands sum to twelve", sum(b[2] for b in bands), 12)

    print("\n  FINDING — the argument offered for those twelve")
    NARROW = 0.083
    print(f"    worst-case spin-orbit narrowing, as printed: {NARROW} Ha")
    for z, e, n, lo, hi in bands:
        print(f"    Z {z:<9} {e}  {n} rows  margin {lo} -> {hi}   "
              f"lowest clears {NARROW}: {lo > NARROW}")
    lowest = min(b[3] for b in bands)
    chk("every margin clears the worst-case narrowing", lowest > NARROW, True,
        f"<-- lowest margin is {lowest}")

    print("\nTHE LÖWDIN SOLUTION — LS objects, and the two supplies against each other")
    for n, rec in ((5, -0.020000), (6, -0.013889), (7, -0.010204), (8, -0.0078125)):
        dp = len(str(rec).split(".")[1])
        chk(f"  {n}g pinned depth = -1/(2n^2)", round(-1 / (2 * n * n), dp), rec)
    mc = re.search(r"5g over (\d+) elements, 6g over (\d+), 7g over (\d+), 8g over (\d+)", MC)
    i = SC.index("5g:")
    flat = re.sub(r"\s*\n\s*>?\s*", " ", SC[i:i + 240])
    sc = re.findall(r"over (\d+)", flat)[:4]
    chk("g spans, Spectra against Mathematical Compendium", sc, list(mc.groups()) if mc else None,
        "(SC prints 57 across a line break inside a blockquote)")

    print("\n  the ordering law's two clauses, as a total order on the subshells")
    subs = [(n, l) for n in range(1, 9) for l in range(0, min(n, 5))]
    key = lambda s: (s[0] + s[1], s[0])
    chk("  ties under (n+l, then n)", len(subs) - len(set(map(key, subs))), 0)
    L = "spdfg"
    seq = [str(n) + L[l] for n, l in sorted(subs, key=key)][:16]
    chk("  the first sixteen subshells", seq,
        "1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s".split())
    chk("  Clause 2 exceptions, named", len(["La", "Ac", "Th"]), 3)

    print("\n" + "=" * 78)
    if not FAILS:
        print("SPECTRA COMPENDIUM AUDIT CLEAN — every checked claim reproduces.")
        return 0
    print(f"{len(FAILS)} CLAIM(S) DID NOT REPRODUCE\n")
    for label, got, w in FAILS:
        print(f"  {label}\n      recorded {w}\n      measured {got}")
    print("\nThis program adjudicates nothing.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
