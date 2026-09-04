#!/usr/bin/env python3
"""a_inward.py — read a's placement DOWN AND INWARD rather than up and outward.

The tower was built by finding that transition happens down and inward: the
coupling hierarchy resolves configuration, then term, then level, and the tower
adds its axes in that order (R 1429). The walk has been read the other way —
a ASCENDING per Janet block, across the table, outward in Z (R 1409).

If the tower's direction is the right one, then a's order should be governed by
how far IN the entrant sits, not by how far ALONG the table it is. The candidate
depth coordinates are all already in the work:

    p = n - l - 1   the node count            (R 1414: the floor exists iff p > 0)
    l               angular momentum          (R 1417: closes; a property before the move)
    n               the shell
    block           the Janet row, n + l

R 1415 already measured something with exactly this shape and did not name it as
a direction: the binding CEILING sits in the entrant's own block 85% of the time,
the binding FLOOR in the NEXT block 89% of the time. Bounded above from where it
is; bounded below by what has not opened yet. The six floor exceptions are all f
or d INTRUDERS — a deeper subshell already sitting inside the current block,
which is the down-and-inward case arriving as the named exception set.

This script asks the narrow question the framing makes testable: under which
coordinate are the eight recorded a values monotone?
"""
import sys
sys.path.insert(0, "/home/claude/work")
import ground as G

# The eight recorded values, register 1403. Seven sit at L, protactinium at U.
RECORDED = {19: 0.5774, 37: 1.0000, 55: 1.2168, 57: 0.7071,
            80: 0.8090, 87: 1.3938, 91: 1.3660, 103: 1.9841}
SYM = {19: "K", 37: "Rb", 55: "Cs", 57: "La", 80: "Hg", 87: "Fr", 91: "Pa", 103: "Lr"}


def cfg(Z):
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


def entrant(Z):
    a, b = cfg(Z - 1), cfg(Z)
    g = [(k, b[k] - a.get(k, 0)) for k in b if b[k] > a.get(k, 0)]
    return g[0][0] if g else None


LENGTHS = [2, 2, 8, 8, 18, 18, 32, 32]
STARTS, _z = [], 1
for _n in LENGTHS:
    STARTS.append(_z); _z += _n


def block(Z):
    return max(i for i, s in enumerate(STARTS) if s <= Z) + 1


rows = []
for Z in sorted(RECORDED):
    nl = entrant(Z)
    if nl is None:
        continue
    n, l = nl
    rows.append({"Z": Z, "sym": SYM[Z], "a": RECORDED[Z], "n": n, "l": l,
                 "p": n - l - 1, "block": block(Z), "nl": n + l})

print("  THE EIGHT RECORDED VALUES, WITH EVERY DEPTH COORDINATE\n")
print(f"    {'':4}{'Z':>4}{'entrant':>9}{'a':>9}{'n':>4}{'l':>4}{'p':>4}"
      f"{'n+l':>5}{'block':>7}")
for r in rows:
    print(f"    {r['sym']:<4}{r['Z']:>4}{f'{r['n']}{chr(115+0)}' if False else f'{r['n']}{"spdfg"[r['l']]}':>9}"
          f"{r['a']:>9.4f}{r['n']:>4}{r['l']:>4}{r['p']:>4}{r['nl']:>5}{r['block']:>7}")


def monotone(key, reverse=False):
    seq = sorted(rows, key=lambda r: (r[key], r["Z"]), reverse=reverse)
    a = [r["a"] for r in seq]
    up = all(y >= x for x, y in zip(a, a[1:]))
    down = all(y <= x for x, y in zip(a, a[1:]))
    return up, down, [r["sym"] for r in seq], a


print("\n  IS a MONOTONE UNDER EACH COORDINATE?\n")
for key in ("Z", "p", "l", "n", "nl", "block"):
    up, down, order, a = monotone(key)
    verdict = "RISES" if up else ("FALLS" if down else "neither")
    print(f"    by {key:<6} {verdict:<8} {' < '.join(order)}")
    print(f"    {'':13}{'  '.join(f'{x:.3f}' for x in a)}")

print("\n  WITHIN A BLOCK, IS a MONOTONE IN DEPTH? (R 1409's per-block claim,")
print("  re-read inward rather than outward)\n")
from collections import defaultdict
byb = defaultdict(list)
for r in rows:
    byb[r["block"]].append(r)
for b in sorted(byb):
    g = sorted(byb[b], key=lambda r: r["p"])
    a = [r["a"] for r in g]
    tag = ("rises with p" if all(y >= x for x, y in zip(a, a[1:]))
           else "falls with p" if all(y <= x for x, y in zip(a, a[1:])) else "neither")
    print(f"    block {b}  {len(g)} value(s)  {tag:<13} "
          + ", ".join(f"{r['sym']}(p={r['p']}) {r['a']:.4f}" for r in g))

print("\n  AND THE TWO DESCENTS IN THE RECORD (R 1409 says both are block openings)\n")
seq = sorted(rows, key=lambda r: r["Z"])
for x, y in zip(seq, seq[1:]):
    if y["a"] < x["a"]:
        opens = y["Z"] in STARTS
        print(f"    {x['sym']} {x['a']:.4f} -> {y['sym']} {y['a']:.4f}   "
              f"Z = {y['Z']}, block opening: {opens}   "
              f"p goes {x['p']} -> {y['p']}   l goes {x['l']} -> {y['l']}")
