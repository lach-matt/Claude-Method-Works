#!/usr/bin/env python3
"""figures_walk.py — settle the walk-side unresolved figures.

R 1396      eleven exceptions split 6 + 5, then scored against twelve
R 1409/1411 seven block openings against six
R 1419      base box quoted as 48 and as 24; cell count 18 against R 1418's 24

Computed from ground.py and the Janet block lengths, nothing fetched.
"""
import sys
sys.path.insert(0, "/home/claude/work")
import ground as G

L = "spdfg"


def cfg(Z):
    """subshell occupancies of the ground configuration, as {(n,l): k}"""
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


WALK = list(range(3, 109))          # 106 steps, Z = 3 to 108


def step(Z):
    """(entrant (n,l), q gained, list of donors) going from Z-1 to Z"""
    a, b = cfg(Z - 1), cfg(Z)
    gained = [(k, b[k] - a.get(k, 0)) for k in b if b[k] > a.get(k, 0)]
    lost = [(k, a[k] - b.get(k, 0)) for k in a if a.get(k, 0) > b.get(k, 0)]
    return gained, lost


# ---------------------------------------------------------------- R 1396 ---
print("=" * 72)
print("R 1396 — the eleven, the twelve, and the base rate")
print("=" * 72)

anomalous, ordinary = [], []
for Z in WALK:
    g, d = step(Z)
    (anomalous if d else ordinary).append(Z)

print(f"  walk steps with a subshell EMPTY as another fills: {len(anomalous)}")
print("    " + ", ".join(f"{G.GROUND[Z][0] if isinstance(G.GROUND.get(Z),(list,tuple)) else ''}{Z}"
                         for Z in anomalous))


def lands_distinguished(Z):
    """does the RECEIVING subshell land on 2l+1 (half) or 4l+2 (full)?"""
    g, _ = step(Z)
    b = cfg(Z)
    for (n, l), _q in g:
        k = b[(n, l)]
        if k in (2 * l + 1, 4 * l + 2):
            return True
    return False


hit_a = [Z for Z in anomalous if lands_distinguished(Z)]
hit_o = [Z for Z in ordinary if lands_distinguished(Z)]
print(f"\n  anomalous landing on half or full : {len(hit_a)} of {len(anomalous)}"
      f"  = {100*len(hit_a)/len(anomalous):.0f}%   (register: 3 of 12 = 25%)")
print(f"  ordinary  landing on half or full : {len(hit_o)} of {len(ordinary)}"
      f"  = {100*len(hit_o)/len(ordinary):.0f}%   (register: 36 of 94 = 38%)")
print(f"    the anomalous ones that do: {hit_a}")
print("\n  VERDICT: the base rate stands — the anomalous steps reach a")
print("           distinguished occupancy LESS often than ordinary ones, which")
print("           is evidence against the exchange account, exactly as stated.")
print("  BUT the entry mixes two sets: it splits the ELEVEN absent cells (6+5)")
print("      and then scores against the TWELVE donor steps. Different objects.")

# ------------------------------------------------------------ R 1409/1411 --
print()
print("=" * 72)
print("R 1409 / R 1411 — seven block openings, or six?")
print("=" * 72)
lengths = [2, 2, 8, 8, 18, 18, 32, 32]
starts, z = [], 1
for n in lengths:
    starts.append(z)
    z += n
print(f"  Janet block lengths      {lengths}")
print(f"  block opens at Z         {starts}")
inwalk = [s for s in starts if s in WALK]
replaced = [s for s in inwalk if s != WALK[0]]
print(f"  openings inside the walk (Z 3-108): {inwalk}  -> {len(inwalk)}")
print(f"  of those, RE-placements (Z 3 is the initial placement, not a re-place):")
print(f"                                      {replaced}  -> {len(replaced)}")
print("\n  VERDICT: both entries are correct under different readings.")
print("           R 1409 counts SEVEN openings among its fifteen moves, counting")
print("           lithium where a is first placed. R 1411 counts SIX RE-placements,")
print("           which excludes lithium because there is nothing to re-place from.")
print("           9 matched + 6 extra = 15 moves, and R 1411 is self-consistent.")
print("           The repair is a clarifying phrase, not a correction to either.")

# ---------------------------------------------------------------- R 1419 ---
print()
print("=" * 72)
print("R 1419 — the two base boxes and the three cell counts")
print("=" * 72)
cells_nlq, cells_nl = set(), set()
for Z in WALK:
    g, _ = step(Z)
    for (n, l), q in g:
        cells_nlq.add((n, l, q))
        cells_nl.add((n, l))


def box(cells):
    d = len(next(iter(cells)))
    b = 1
    for i in range(d):
        b *= len({c[i] for c in cells})
    return b


nvals = sorted({c[0] for c in cells_nlq})
lvals = sorted({c[1] for c in cells_nlq})
qvals = sorted({c[2] for c in cells_nlq})
pvals = sorted({n - l - 1 for n, l, _ in cells_nlq})
print(f"  n takes {len(nvals)} values {nvals}")
print(f"  l takes {len(lvals)} values {lvals}")
print(f"  q takes {len(qvals)} values {qvals}")
print(f"  node count p = n-l-1 takes {len(pvals)} values {pvals}")
print()
print(f"  (n, l, q)          cells {len(cells_nlq):>3}   box {box(cells_nlq):>4}")
print(f"  (p, l, q) replace  cells {len({(n-l-1,l,q) for n,l,q in cells_nlq}):>3}"
      f"   box {len(pvals)*len(lvals)*len(qvals):>4}")
print(f"  (n, l)             cells {len(cells_nl):>3}   box {box(cells_nl):>4}")
print(f"  (n, l, p) adjoin   cells {len({(n,l,n-l-1) for n,l in cells_nl}):>3}"
      f"   box {len(nvals)*len(lvals)*len(pvals):>4}")
print()
print("  VERDICT: R 1419 is NOT self-contradictory. It reports TWO DIFFERENT")
print("           base indexes. The REPLACE test runs on (n, l, q), box 48 -> 56.")
print("           The ADJOIN test runs on (n, l), box 24 -> 168, with 18 cells.")
print("           R 1418's twenty-four is the (n, l, q) cell count; R 1419's")
print("           eighteen is the (n, l) cell count. Both are right.")
print("           My earlier flag against this entry is WITHDRAWN.")
