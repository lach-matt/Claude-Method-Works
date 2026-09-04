#!/usr/bin/env python3
"""lshell_test.py — does Lambda_xray's nine-cell closure hold at a second depth?

Lambda_xray closed at E = 0 on (Delta-n, Delta-l, jtype_hole) with nine cells,
built from K-shell lines (R 1379, 1387). The five L-shell captures are the
second depth. THE TEST: classify them on the SAME three coordinates and ask
whether they land in the SAME nine cells, or open new ones.

THE COORDINATES, from Lambda's own transition alphabet:
    Delta-n     = n_initial - n_final of the electron making the jump
    Delta-l     = l_final - l_initial
    jtype_hole  = whether the HOLE state has j = l + 1/2 or j = l - 1/2

THE FIVE LINES, decomposed. The hole is in the L shell (n = 2); the electron
falls from M (n = 3) or N (n = 4).

    line   hole    electron   Delta-n   Delta-l   jtype_hole
    L3M1   2p3/2   3s         1         -1        +  (j = l + 1/2)
    L3M4   2p3/2   3d         1         +1        +
    L3M5   2p3/2   3d         1         +1        +
    L2M1   2p1/2   3s         1         -1        -  (j = l - 1/2)
    L2M4   2p1/2   3d         1         +1        -
    L1N2   2s      4p         2         +1        0  (l = 0, no splitting)
    L1N3   2s      4p         2         +1        0

DECLARED BEFORE THE RUN. If the nine-cell closure is a property of the ALPHABET
rather than of the K shell, these land inside it. If it is a property of the K
shell, the L lines open cells the K lines never reached — and Delta-n = 2 with
a 2s hole is the obvious candidate, since no K line has an s-hole at all.

I expect NEW CELLS, because L1 is an s-hole and the K shell's only s-hole is
the 1s itself, which cannot be the FINAL state of an L-shell transition.
"""
import itertools
from collections import defaultdict

# (name, hole_n, hole_l, hole_j_type, elec_n, elec_l)
LINES = [
    ("L3M1", 2, 1, +1, 3, 0),
    ("L3M4", 2, 1, +1, 3, 2),
    ("L3M5", 2, 1, +1, 3, 2),
    ("L2M1", 2, 1, -1, 3, 0),
    ("L2M4", 2, 1, -1, 3, 2),
    ("L1N2", 2, 0,  0, 4, 1),
    ("L1N3", 2, 0,  0, 4, 1),
]
# the K-shell set that produced the nine cells: hole is 1s, electron from n>=2
KLINES = [
    ("KL2", 1, 0, 0, 2, 1), ("KL3", 1, 0, 0, 2, 1),
    ("KM2", 1, 0, 0, 3, 1), ("KM3", 1, 0, 0, 3, 1),
    ("KN2", 1, 0, 0, 4, 1), ("KN3", 1, 0, 0, 4, 1),
]


def cell(hn, hl, hj, en, el):
    return (en - hn, hl - el, hj)


print("  DOES THE NINE-CELL CLOSURE HOLD AT L-SHELL DEPTH?\n")
print("  Coordinates: (Delta-n, Delta-l, jtype_hole), Lambda_xray's own.\n")
print(f"    {'line':<7}{'hole':<8}{'electron':<10}{'Dn':>4}{'Dl':>5}{'jtype':>7}   cell")
kc = set()
for nm, hn, hl, hj, en, el in KLINES:
    c = cell(hn, hl, hj, en, el); kc.add(c)
    print(f"    {nm:<7}{f'{hn}{chr(115+0)}':<8}{f'{en}{chr(115)}pdf'[0]:<10}"
          f"{c[0]:>4}{c[1]:>5}{c[2]:>7}   {c}")
print()
lc = defaultdict(list)
L = "spdfg"
for nm, hn, hl, hj, en, el in LINES:
    c = cell(hn, hl, hj, en, el)
    lc[c].append(nm)
    print(f"    {nm:<7}{f'{hn}{L[hl]}':<8}{f'{en}{L[el]}':<10}"
          f"{c[0]:>4}{c[1]:>5}{c[2]:>7}   {c}")

print(f"\n  K-shell cells reached : {len(kc)}   {sorted(kc)}")
print(f"  L-shell cells reached : {len(lc)}   {sorted(lc)}")
new = set(lc) - kc
print(f"\n  ** CELLS THE L-SHELL OPENS THAT THE K-SHELL NEVER REACHED: {len(new)} **")
for c in sorted(new):
    print(f"      {c}   from {', '.join(lc[c])}")
shared = set(lc) & kc
print(f"\n  cells shared with the K shell: {len(shared)}  {sorted(shared)}")

print("\n  AND THE COLLAPSE — how many distinct lines per cell:\n")
for c in sorted(lc):
    print(f"      {c}  <- {len(lc[c])} line(s): {', '.join(lc[c])}")
print(f"\n    seven L lines collapse to {len(lc)} cells, a {7/len(lc):.2f}:1 reduction")
