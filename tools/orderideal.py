#!/usr/bin/env python3
"""orderideal.py -- is the occupied set an order ideal of Lambda?

Register 66 states:

    THE OCCUPIED CELLS FORM AN ORDER IDEAL OF LAMBDA -- DOWNWARD CLOSED WITHOUT
    EXCEPTION. For every occupied x and every admissible y <= x componentwise, y
    is also occupied: no violations across all 118 cells. ... A property that
    does not appear to have been noted.

An unbanked re-measurement, recovered from the chat corpus and recorded as
PO-#### in PROSE-ONLY.tsv, states the opposite:

    The accumulation argument was wrong, and testing it properly overturned three
    headline results. ... Distinct cells 118 -> 110. Order ideal yes -> NO, 172
    violations, 7 holes. Z a linear extension 0 -> 9 violations. Admissible
    l-orderings 1 of 120 -> 0 of 120.

This instrument runs the test against the seated observed data and reports what it
finds. It does NOT adjudicate between the two records: both are the corpus's own,
and which stands is the author's ruling. What it can do is measure, and say
exactly which convention produces which number -- because the two records differ
on the cell count before they differ on the property, and that is the first thing
R3 needs.

CONVENTIONS, and where each comes from
--------------------------------------
Admissibility is READ from the Register's own partition (registers 11, 12):
"void (l >= n, orbital cannot exist), reactive (electron count exceeds subshell
capacity), and reserved (valid but unoccupied)". So a cell (n, l, k) is admissible
iff l < n and 1 <= k <= 2(2l+1). Status: RECOVERED -- stated by the corpus.

A cell is occupied iff some element's ground configuration contains that subshell
at exactly that occupancy. An element with 2p6 occupies (2,1,6); it does not also
occupy (2,1,1..5). Those are occupied by B, C, N, O and F. Downward closure is
therefore a question about the UNION across elements, which is what register 66
states. Status: RECOVERED -- register 66's own wording ("if an element has
ground-state configuration (n,l,k), then every configuration with no larger
shell, subshell or occupancy is likewise realised").

The ground configurations are IMPORTED from the seated member
method/members/LW1-ground.py (register 1306, NIST ASD 5.12, Z = 1..108). This
instrument never copies a member.

WHAT IT REFUSES
---------------
It refuses to report a verdict on register 66. It reports the measurement and the
convention that produced it. A DISAGREES line is not a finding that the register
is wrong; it is a finding that two records of the corpus do not agree, which is
what R3 is for.

stdlib only.  python3 tools/orderideal.py [--selftest] [--verbose]
"""
import argparse
import importlib.util
import itertools
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MEMBER = ROOT / "method" / "members" / "LW1-ground.py"
LNAME = "spdfg"


def seated_ground():
    """Import the seated member by path. Never copy a member."""
    spec = importlib.util.spec_from_file_location("lw1_ground", MEMBER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def admissible(n, l, k):
    """Register 11/12's partition: l < n (not void), k <= 2(2l+1) (not reactive)."""
    return 0 <= l < n and 1 <= k <= 2 * (2 * l + 1)


def occupied_cells(ground, zmax=None):
    """The union, across elements, of (n, l, k) triples actually realised."""
    cells = set()
    for Z in sorted(ground.GROUND):
        if zmax is not None and Z > zmax:
            continue
        for n, l, k in ground.expand(Z):
            cells.add((n, l, k))
    return cells


def below(x):
    """Every admissible y <= x componentwise, y != x."""
    n, l, k = x
    for nn in range(1, n + 1):
        for ll in range(0, l + 1):
            for kk in range(1, k + 1):
                if (nn, ll, kk) != x and admissible(nn, ll, kk):
                    yield (nn, ll, kk)


def ideal_violations(cells):
    """(x, y) pairs where x is occupied, y admissible and <= x, and y is not occupied."""
    bad = []
    for x in sorted(cells):
        for y in below(x):
            if y not in cells:
                bad.append((x, y))
    return bad


def holes(cells):
    """An occupied subshell (n,l) whose occupancy run 1..max has a gap."""
    tops = {}
    for (n, l, k) in cells:
        tops[(n, l)] = max(tops.get((n, l), 0), k)
    out = []
    for (n, l), top in sorted(tops.items()):
        missing = [k for k in range(1, top) if (n, l, k) not in cells]
        if missing:
            out.append(((n, l), top, missing))
    return out


def z_linear_extension(ground, zmax=None):
    """Is Z a linear extension: does each element's cell set contain the previous one's?

    Register 66's neighbourhood claims Z orders the occupied set. A violation is an
    element that drops a cell its predecessor held.
    """
    bad = []
    prev_Z, prev = None, None
    for Z in sorted(ground.GROUND):
        if zmax is not None and Z > zmax:
            continue
        cur = {(n, l, k) for n, l, k in ground.expand(Z)}
        if prev is not None:
            lost = {(n, l) for n, l, k in prev} - {(n, l) for n, l, k in cur}
            if lost:
                bad.append((prev_Z, Z, sorted(lost)))
        prev_Z, prev = Z, cur
    return bad


def l_orderings(cells):
    """Over all 120 permutations of l in {s,p,d,f,g}, how many make the set an ideal?

    The l axis is re-ordered; n and k keep their natural order. Admissibility is
    evaluated in the ORIGINAL coordinates (l < n, Pauli capacity are physics, not
    an artefact of the ordering); only the <= test on l is permuted.
    """
    ok = []
    ls = [0, 1, 2, 3, 4]
    for perm in itertools.permutations(ls):
        rank = {l: i for i, l in enumerate(perm)}
        good = True
        for (n, l, k) in cells:
            for nn in range(1, n + 1):
                for ll in ls:
                    if rank[ll] > rank[l]:
                        continue
                    for kk in range(1, k + 1):
                        if (nn, ll, kk) == (n, l, k):
                            continue
                        if admissible(nn, ll, kk) and (nn, ll, kk) not in cells:
                            good = False
                            break
                    if not good:
                        break
                if not good:
                    break
            if not good:
                break
        if good:
            ok.append(perm)
    return ok


def cell_str(c):
    n, l, k = c
    return f"{n}{LNAME[l]}{k}"


def report(verbose=False):
    g = seated_ground()
    n_el = len(g.GROUND)
    cells = occupied_cells(g)
    viol = ideal_violations(cells)
    hol = holes(cells)
    zbad = z_linear_extension(g)
    lok = l_orderings(cells)

    print("  ORDER IDEAL -- the test register 66 states, run on the seated data\n")
    print(f"      source          method/members/LW1-ground.py (register 1306, NIST ASD 5.12)")
    print(f"      elements        {n_el}   (Z = 1..{max(g.GROUND)})")
    print(f"      occupied cells  {len(cells)}")
    print(f"      subshells       {len({(n, l) for n, l, k in cells})}")
    print()
    print("  THE PROPERTY\n")
    print(f"      downward-closure violations   {len(viol)}")
    print(f"      subshells with an occupancy gap {len(hol)}")
    print(f"      Z-order violations              {len(zbad)}")
    print(f"      admissible l-orderings          {len(lok)} of 120")
    print()
    verdict = "IS an order ideal" if not viol else "is NOT an order ideal"
    print(f"      => on this data the occupied set {verdict}.")
    print()

    if verbose and viol:
        print("  VIOLATIONS (occupied x -> admissible y <= x that is not occupied)\n")
        for x, y in viol[:40]:
            print(f"      {cell_str(x):>6}  ->  {cell_str(y)}")
        if len(viol) > 40:
            print(f"      ... and {len(viol) - 40} more")
        print()
    if verbose and hol:
        print("  OCCUPANCY GAPS\n")
        for (n, l), top, missing in hol:
            print(f"      {n}{LNAME[l]}: top {top}, missing k = {missing}")
        print()
    if verbose and zbad:
        print("  Z-ORDER VIOLATIONS (element drops a subshell its predecessor held)\n")
        for a, b, lost in zbad:
            names = f"{g.GROUND[a][0]}->{g.GROUND[b][0]}"
            print(f"      Z {a}->{b} ({names}): lost {[f'{n}{LNAME[l]}' for n, l in lost]}")
        print()

    print("  THE THREE RECORDS DO NOT AGREE ON THE CELL COUNT\n")
    print(f"      register 66 (seated)            118 cells, 0 violations, order ideal")
    print(f"      unbanked re-measurement         110 cells, 172 violations, 7 holes")
    print(f"      this run, on the seated member  {len(cells)} cells, {len(viol)} violations, {len(hol)} gaps")
    print()
    print("      The counts differ before the property does. 118 is the Register's own")
    print("      first census (registers 11, 12: 180 void, 240 reactive, 78 reserved,")
    print("      118 occupied, 14 ghost). This run reads Z = 1..108 from the seated")
    print("      member; the census covered the full table. NO VERDICT IS OFFERED --")
    print("      recorded for R3.")
    return {"cells": len(cells), "violations": len(viol), "holes": len(hol),
            "z": len(zbad), "l": len(lok), "elements": n_el}


def selftest():
    """Fixtures are the corpus's own recorded numbers and its own seated data."""
    g = seated_ground()
    fails = []

    # 1. the seated member is intact: every element's electron count equals Z
    bad = [Z for Z in g.GROUND if g.occ_count(Z) != Z]
    if bad:
        fails.append(f"electron-count check failed at {bad}")

    # 2. admissibility matches the Register's partition on known cells
    if not admissible(2, 1, 6):
        fails.append("2p6 should be admissible")
    if admissible(1, 1, 1):
        fails.append("1p is void (l >= n) and must not be admissible")
    if admissible(2, 1, 7):
        fails.append("2p7 exceeds Pauli capacity and must not be admissible")

    # 3. the four anomalies register 66's neighbourhood turns on are present
    #    as the corpus records them (LW1-ground.py's own docstring names Pd)
    want = {24: "3d5", 29: "3d10", 46: "4d10", 78: "5d9"}
    for Z, shell in want.items():
        cur = {f"{n}{LNAME[l]}{k}" for n, l, k in g.expand(Z)}
        if shell not in cur:
            fails.append(f"Z={Z} should carry {shell}; has {sorted(cur)}")

    # 4. the holes those anomalies imply: nothing has 3d4, 3d9, 4d9, 5d8
    cells = occupied_cells(g)
    for miss in [(3, 2, 4), (3, 2, 9), (4, 2, 9), (5, 2, 8)]:
        if miss in cells:
            fails.append(f"{cell_str(miss)} should be unoccupied; the re-measurement turns on it")

    # 5. a trivially closed set is reported as an ideal
    tiny = {(1, 0, 1), (1, 0, 2)}
    if ideal_violations(tiny):
        fails.append("a downward-closed set must report zero violations")

    if fails:
        print("  SELFTEST FAILED\n")
        for f in fails:
            print(f"      {f}")
        return 1
    print("  selftest OK -- seated member intact, admissibility matches registers 11/12,")
    print("                 the four anomalies and the four holes they imply are present.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true", help="assert the corpus's own numbers")
    ap.add_argument("--verbose", action="store_true", help="list violations, gaps and Z-order breaks")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    report(verbose=a.verbose)
    return 0


if __name__ == "__main__":
    sys.exit(main())
