#!/usr/bin/env python3
"""merged_triples.py — REBUILT from register 1420, with the source coordinates
as specified in the 1.6.1 recovery.

    source l          0 for the notional outside, l + 1 otherwise
    source occupancy  its count BEFORE the step
    source distance   source(n+l) - target(n+l) + 2, a RELATIVE measure shifted
                      to stay non-negative

1420's finding: every landing arrangement containing q puts its single defect at
q = 2 -- the twelve donor steps -- and adding ANY source coordinate closes it,
twelve of twenty three-axis combinations closing.

TWO THINGS THIS REBUILD CANNOT MATCH, DECLARED RATHER THAN GLOSSED.

  · The TWENTY is not reconstructible. 1420's candidate set was five landing
    axes plus source coordinates; five landing axes and three source coordinates
    give C(8,3) = 56 systems, of which 46 contain a source coordinate. No
    grouping of these yields twenty. The counts below are this rebuild's own.

  · Orderings are searched over DIRECTION FLIPS only, 2^3 per system, because
    every axis here is a monotone chain and its order is therefore given while
    only its direction is free. That is what makes the search tractable at all
    (the full permutation product is what OOM-killed 1.6.1 twice). It also means
    the E values are UPPER bounds: a non-monotone relabelling might do better,
    though it would violate the rule that admits the axis in the first place.
"""
import sys, io, contextlib, itertools, math
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack
import ground as G

L = "spdfg"
cap = lambda l: 2 * (2 * l + 1)
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)


def occ(Z):
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


def cands(prev):
    c = []
    for l in range(5):
        for n in range(l + 1, 9):
            if prev.get((n, l), 0) >= cap(l):
                continue
            c.append((n, l))
            if prev.get((n, l), 0) == 0:
                break
    return c


CELLS = []
for Z in STEPS:
    _, gn, gl, gp, lo, hi, blo, bhi = IV[Z]
    prev, cur = occ(Z - 1), occ(Z)
    tgt = (gn, gl)
    lost = [k for k in prev if prev[k] > cur.get(k, 0)]
    src = lost[0] if lost else None
    eb = gn + gl
    CELLS.append({
        # LANDING coordinates — where it arrives relative to its bounds
        "ceilblk": (bhi[0] + bhi[1] - eb) if bhi else 9,
        "floorblk": (blo[0] + blo[1] - eb) if blo else 9,
        "sides": int(lo > -1e8) + int(hi < 1e8),
        "rivl": bhi[1] if bhi else 9,
        "q": cur[tgt] - prev.get(tgt, 0),
        # SOURCE coordinates — 1420's specification
        "sl": 0 if src is None else src[1] + 1,
        "sq": 0 if src is None else prev[src],
        # SENTINEL FIX: outside = 0, not 2. Six of the twelve real sources
        # have shifted distance 2 and were indistinguishable from "no source".
        "sd": 0 if src is None else (src[0] + src[1]) - eb + 2,
    })

LAND = ["ceilblk", "floorblk", "sides", "rivl", "q"]
SRC = ["sl", "sq", "sd"]


def opR(X, d):
    X = set(X)
    vals = [sorted({x[i] for x in X}) for i in range(d)]

    def env(i, j):
        m = {}
        for x in X:
            m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m):
            b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*vals)
            if all(x[i] <= phi[(i, j)][x[j]]
                   for i in range(d) for j in range(d) if i != j)}


def minE(cells, want_defects=False):
    d = len(next(iter(cells)))
    vals = [sorted({c[i] for c in cells}) for i in range(d)]
    sizes = [len(v) for v in vals]
    best, arg, refused, seen = None, None, 0, 0
    for flips in itertools.product((False, True), repeat=d):
        perm = tuple(tuple(range(s))[::-1] if f else tuple(range(s))
                     for s, f in zip(sizes, flips))
        cs = {tuple(perm[i][vals[i].index(c[i])] for i in range(d)) for c in cells}
        E = len(opR(cs, d)) - len(cs)
        seen += 1; refused += E > 0
        if best is None or E < best:
            best, arg = E, (perm, vals, cs)
    if not want_defects:
        return best, refused / seen
    perm, vals, cs = arg
    inv = [{perm[i][j]: vals[i][j] for j in range(len(vals[i]))} for i in range(len(vals))]
    dif = [tuple(inv[i][x[i]] for i in range(len(vals)))
           for x in sorted(opR(cs, len(vals)) - cs)]
    return best, refused / seen, dif


print("  LANDING SYSTEMS ALONE — R 1420 says every one containing q has its")
print("  single defect at q = 2, and those without q split it into two\n")
print(f"    {'axes':<28}{'cells':>6}{'minE':>6}{'refuse':>8}  defect at q =")
for combo in itertools.combinations(LAND, 3):
    cells = {tuple(c[a] for a in combo) for c in CELLS}
    if len(cells) < 2:
        continue
    E, rate, dif = minE(cells, want_defects=True)
    tag = ""
    if "q" in combo and dif:
        qi = combo.index("q")
        tag = str(sorted({x[qi] for x in dif}))
    print(f"    {'·'.join(combo):<28}{len(cells):>6}{E:>6}{rate:>7.0%}   {tag}")

print("\n  ADDING A SOURCE COORDINATE\n")
print(f"    {'axes':<28}{'cells':>6}{'box':>6}{'minE':>6}{'refuse':>8}")
tot = closed = 0
for combo in itertools.combinations(LAND + SRC, 3):
    if not (set(combo) & set(SRC)):
        continue
    cells = {tuple(c[a] for a in combo) for c in CELLS}
    if len(cells) < 2:
        continue
    E, rate = minE(cells)
    tot += 1; closed += E == 0
    if E == 0:
        box = math.prod(len({c[i] for c in cells}) for i in range(3))
        print(f"    {'·'.join(combo):<28}{len(cells):>6}{box:>6}{E:>6}{rate:>7.0%}")
print(f"\n    {closed} of {tot} systems containing a source coordinate CLOSE")
print(f"    (R 1420 reports twelve of twenty; the twenty is not reconstructible")
print(f"     — see this file's header. The counts above are this rebuild's own.)")
