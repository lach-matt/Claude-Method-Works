#!/usr/bin/env python3
"""traj_index.py — Lambda_traj, the trajectory as an index.

REBUILT from registers 1417-1420. The original was lost with the 1.6.1 container;
this is a reconstruction from the registers that describe it, NOT the original,
and every figure it prints should be read as recomputed rather than reproduced.
See PROVENANCE.md.

WHY THE TRAJECTORY NEEDS AN INDEX AT ALL

Register 1412 separates two claims that had been running together. The LAW says
the incoming electron takes the Pauli-admissible subshell of least nu; it is
tested by whether a corridor exists at each element, and 106 of 106 are non-empty.
The TRAJECTORY says this particular sequence of a values produces the table, and
that is where every failure lives. Register 1402 sharpens it: the reset COUNT is
rule-dependent, ten to thirty-three over the same 106 steps, so membership cannot
be the derived condition -- only EMPTINESS is trajectory-free.

That split is what makes an index of the trajectory worth building. The
trajectory carries the observer-dependence; indexing it puts that dependence on a
coordinate instead of leaving it in the method.

THE SIX CANDIDATE AXES (R 1417), each read off the step, each a monotone chain

    p        the entrant's node count, n - l - 1
    l        the entrant's angular momentum
    q        how many electrons arrive
    ceilblk  where the binding CEILING sits, relative to the entrant's Janet block
    floorblk where the binding FLOOR sits, relative to the entrant's Janet block
    sides    how many sides of the corridor are finite

The first three describe WHAT THE ENTRANT IS, before it moves. The last three
describe WHERE IT LANDS. Register 1417's finding is that the first three close
and the landing coordinates do not -- and R 1418 corrects 1417's reading of what
that means: Lambda_traj is a PROJECTION of Lambda, not a new index, because
n by l by q are Lambda's own letters and replacing n by the node count is a
relabelling (A.erel), not a new construction.

THE PERMUTATION CAP

minE searches orderings of each axis's values. The product of factorials is
factorial in the largest axis and OOM-killed the container twice. The cap is
applied to the ITERATOR here and never by building the product first, and when it
bites it is DECLARED in the output.
"""
import sys, io, contextlib, itertools, math, random
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack
import ground as G

CAP = 200_000          # orderings examined per axis system before sampling


# ---------------------------------------------------------------- cells ---
def block(n, l):
    return n + l


STEPS = []
for Z, gn, gl, gp, lo, hi, blo, bhi in brack.IV:
    pr = {(n, l): o for n, l, o in G.expand(Z - 1)}
    cu = {(n, l): o for n, l, o in G.expand(Z)}
    q = cu[(gn, gl)] - pr.get((gn, gl), 0)
    fin_lo, fin_hi = lo > -1e8, hi < 1e8
    STEPS.append({
        "Z": Z,
        "p": gp,
        "l": gl,
        "q": q,
        "ceilblk": (block(*bhi[:2]) - block(gn, gl)) if bhi else None,
        "floorblk": (block(*blo[:2]) - block(gn, gl)) if blo else None,
        "sides": int(fin_lo) + int(fin_hi),
    })

AXES = ["p", "l", "q", "ceilblk", "floorblk", "sides"]
IS_A = {"p", "l", "q"}                       # what the entrant IS
print(f"  Lambda_traj — {len(STEPS)} walk steps as cells\n")
for a in AXES:
    vals = sorted({s[a] for s in STEPS if s[a] is not None})
    miss = sum(1 for s in STEPS if s[a] is None)
    kind = "IS " if a in IS_A else "LANDS"
    print(f"    {kind} {a:<9} {len(vals)} values {vals}"
          + (f"   ({miss} steps undefined)" if miss else ""))


# ---------------------------------------------------------------- opR -----
def opR(X, d):
    X = set(X)
    vals = [sorted({x[i] for x in X}) for i in range(d)]

    def env(i, j):
        m = {}
        for x in X:
            m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m):
            b = max(b, m[t])
            o[t] = b
        return o

    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*vals)
            if all(x[i] <= phi[(i, j)][x[j]]
                   for i in range(d) for j in range(d) if i != j)}


def minE(cells, want_rate=False):
    d = len(next(iter(cells)))
    vals = [sorted({c[i] for c in cells}) for i in range(d)]
    sizes = [len(v) for v in vals]
    total = math.prod(math.factorial(s) for s in sizes)
    capped = total > CAP

    def orderings():
        gens = [itertools.permutations(range(s)) for s in sizes]
        if not capped:
            yield from itertools.product(*gens)
        else:
            rng = random.Random(0)
            for _ in range(CAP):
                yield tuple(tuple(rng.sample(range(s), s)) for s in sizes)

    best, refused, seen = None, 0, 0
    for perm in orderings():
        cs = {tuple(perm[i][vals[i].index(c[i])] for i in range(d)) for c in cells}
        E = len(opR(cs, d)) - len(cs)
        seen += 1
        if E > 0:
            refused += 1
        if best is None or E < best:
            best = E
    return (best, refused / seen, seen, capped) if want_rate else best


# --------------------------------------------------- the twenty systems ---
print(f"\n  ALL {math.comb(6,3)} THREE-AXIS SYSTEMS  (cap {CAP:,} orderings each)\n")
print(f"    {'axes':<28}{'cells':>6}{'box':>6}{'minE':>6}{'refuse':>8}  kind")
results = []
for combo in itertools.combinations(AXES, 3):
    cells = {tuple(s[a] for a in combo) for s in STEPS
             if all(s[a] is not None for a in combo)}
    if len(cells) < 2:
        continue
    E, rate, seen, capped = minE(cells, want_rate=True)
    box = math.prod(len({c[i] for c in cells}) for i in range(3))
    kind = ("IS" if set(combo) <= IS_A else
            "LANDS" if not (set(combo) & IS_A) else "mixed")
    results.append((combo, len(cells), box, E, rate, kind, capped))
    print(f"    {' x '.join(combo):<28}{len(cells):>6}{box:>6}{E:>6}"
          f"{rate:>7.0%}{'*' if capped else ' '}  {kind}")

print("\n    * orderings sampled rather than exhausted; the cap bit here.")

# ------------------------------------------------------------- readings ---
closed = [r for r in results if r[3] == 0]
print(f"\n  {len(closed)} of {len(results)} systems reach E = 0")
for combo, n, box, E, rate, kind, _ in closed:
    print(f"      {' x '.join(combo):<28} {n} cells in {box}, {rate:.0%} refuse, {kind}")

pure_is = [r for r in results if r[5] == "IS"]
pure_land = [r for r in results if r[5] == "LANDS"]
print(f"\n  R 1417's claim: every axis describing WHAT THE ENTRANT IS closes,")
print(f"                  every axis describing WHERE IT LANDS fails.")
print(f"    IS    systems: {len(pure_is)}, minE = {[r[3] for r in pure_is]}")
print(f"    LANDS systems: {len(pure_land)}, minE = {[r[3] for r in pure_land]}")

# R 1420 — where do the landing systems put their defect?
print(f"\n  R 1420 — the landing systems' defect, and whether q = 2 is where it sits")
for combo, n, box, E, rate, kind, _ in results:
    if kind == "LANDS" or (kind == "mixed" and "q" in combo):
        cells = {tuple(s[a] for a in combo) for s in STEPS
                 if all(s[a] is not None for a in combo)}
        d = 3
        vals = [sorted({c[i] for c in cells}) for i in range(d)]
        # defects under the identity ordering, reported with the axis names
        dif = sorted(opR(cells, d) - cells)
        if dif and E > 0:
            qi = combo.index("q") if "q" in combo else None
            tag = (f"all at q = {sorted({x[qi] for x in dif})}" if qi is not None
                   else "")
            print(f"      {' x '.join(combo):<28} E = {E}, {len(dif)} defect(s) {tag}")

print("\n  NOTE: this is a REBUILD from R 1417-1420, not the lost original.")
print("        Figures are recomputed. Where they disagree with the registers,")
print("        neither is privileged until the disagreement is examined.")
