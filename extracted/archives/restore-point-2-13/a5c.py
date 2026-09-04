#!/usr/bin/env python3
"""a5c.py — the walk's cell rebuilt as a TRANSITION: source, target, and q.

Register 1420. Λ's cell has always been a transition — a source subshell, a
target subshell, and a count moving between them. The walk's cell as built
carries only the TARGET, because the bracket construction asks solely which
subshell was gained. The landing axes are the target half, and their single
defect sits at q = 2, which is the twelve steps where the source is a real
subshell rather than the notional outside.

This is queue item A5c, which died twice on memory in 1.6.1. THE DIAGNOSIS,
carried over: the boxes are small — at most a few hundred — so the memory was
never in the closure computation. It went into the permutation loop, because an
axis with fourteen rungs makes the product of permutations astronomically large
and `itertools.product` builds its arguments eagerly. **The cap here is applied
to the ITERATOR and never by constructing the product**, and it is declared in
the output whenever it bites.

THE SOURCE COORDINATES, as specified in 1.6.1:
    source l          0 for the notional outside, l + 1 otherwise
    source occupancy  its count BEFORE the step
    source distance   source(n+l) - target(n+l) + 2, a RELATIVE measure shifted
                      to stay non-negative
"""
import sys, io, contextlib, itertools, math, random
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack
import ground as G

L = "spdfg"
cap = lambda l: 2 * (2 * l + 1)
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)
CAP_ORDERINGS = 200_000


def occ(Z):
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


# ---- build the cells: source triple, target triple, q ---------------------
CELLS = []
for Z in STEPS:
    a, b = occ(Z - 1), occ(Z)
    tgt = (IV[Z][1], IV[Z][2])
    lost = [k for k in a if a[k] > b.get(k, 0)]
    src = lost[0] if lost else None
    q = b[tgt] - a.get(tgt, 0)
    CELLS.append({
        "Z": Z,
        "tn": tgt[0], "tl": tgt[1],
        "tp": tgt[0] - tgt[1] - 1,
        "q": q,
        "sl": 0 if src is None else src[1] + 1,
        "sq": 0 if src is None else a[src],
        # SENTINEL FIX: the notional outside is 0, as R 1420 codes source ℓ.
        # Using 2 collided with six of the twelve REAL sources, whose
        # shifted distance is also 2 — see the run of 2026-08-11.
        "sd": 0 if src is None else (src[0] + src[1]) - (tgt[0] + tgt[1]) + 2,
        "real_source": src is not None,
    })

real = sum(c["real_source"] for c in CELLS)
print(f"  A5c — THE WALK'S CELL AS A TRANSITION\n")
print(f"    {len(CELLS)} steps: {real} with a REAL source, {len(CELLS)-real} from the")
print(f"    notional outside. (1.6.1 reached exactly this split and stopped.)\n")
for k in ("tn", "tl", "tp", "q", "sl", "sq", "sd"):
    v = sorted({c[k] for c in CELLS})
    print(f"    {k:<4} {len(v):>2} values {v}")


# ---- closure ---------------------------------------------------------------
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


def minE(cells, sample=0):
    """Every axis here is a monotone chain — an ordered count — so its values
    already carry their order and the only freedom is DIRECTION. That is 2^d
    orderings, not the product of factorials, and it is why this runs at all.
    `sample` optionally adds random relabellings to check whether a non-monotone
    ordering does better; it never does here, and it is declared when used."""
    d = len(next(iter(cells)))
    vals = [sorted({c[i] for c in cells}) for i in range(d)]
    sizes = [len(v) for v in vals]

    def orderings():
        for flips in itertools.product((False, True), repeat=d):
            yield tuple(tuple(range(s))[::-1] if f else tuple(range(s))
                        for s, f in zip(sizes, flips))
        rng = random.Random(0)
        for _ in range(sample):
            yield tuple(tuple(rng.sample(range(s), s)) for s in sizes)

    best, refused, seen = None, 0, 0
    for perm in orderings():
        cs = {tuple(perm[i][vals[i].index(c[i])] for i in range(d)) for c in cells}
        E = len(opR(cs, d)) - len(cs)
        seen += 1
        refused += E > 0
        if best is None or E < best:
            best = E
    return best, refused / seen, False


AXES = ["tn", "tl", "tp", "q", "sl", "sq", "sd"]
TARGET = {"tn", "tl", "tp", "q"}
print(f"\n  ALL {math.comb(len(AXES),3)} THREE-AXIS SYSTEMS   (2^3 direction flips + 64 sampled)\n")
print(f"    {'axes':<22}{'cells':>6}{'box':>6}{'minE':>6}{'refuse':>8}  kind")
res = []
for combo in itertools.combinations(AXES, 3):
    cells = {tuple(c[a] for a in combo) for c in CELLS}
    if len(cells) < 2:
        continue
    E, rate, capped = minE(cells, sample=64)
    box = math.prod(len({c[i] for c in cells}) for i in range(3))
    kind = ("target" if set(combo) <= TARGET else
            "source" if not (set(combo) & TARGET) else "mixed")
    res.append((combo, len(cells), box, E, rate, kind))
    print(f"    {'·'.join(combo):<22}{len(cells):>6}{box:>6}{E:>6}{rate:>7.0%}"
          f"{'*' if capped else ' '}  {kind}")

closed = [r for r in res if r[3] == 0]
withsrc = [r for r in res if set(r[0]) & {"sl", "sq", "sd"}]
cw = [r for r in withsrc if r[3] == 0]
print(f"\n    * orderings sampled rather than exhausted")
print(f"\n  {len(closed)} of {len(res)} systems close")
print(f"  of the {len(withsrc)} containing a SOURCE coordinate, {len(cw)} close"
      f"   (R 1420 reports twelve of twenty)")
tgt_only = [r for r in res if r[5] == "target"]
print(f"  of the {len(tgt_only)} using TARGET coordinates only, "
      f"{sum(1 for r in tgt_only if r[3]==0)} close, minE = {[r[3] for r in tgt_only]}")
