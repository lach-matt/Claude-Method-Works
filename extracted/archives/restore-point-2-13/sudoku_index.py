#!/usr/bin/env python3
"""sudoku_index.py — sudoku as an index, under ℛ.

WHY. The register already holds the constraint-satisfaction statement:

    A.gc   E(X) = 0  ⟺  the binary constraint network is GLOBALLY CONSISTENT
           (Freuder 1978; Dechter 1992)
    A.bpc  binary path consistency / 2-decomposability (Cooper 1989;
           Janssen, Jegou, Nouguier & Vilarem 1989; Kimura et al. 2024)

So "closed index" and "globally consistent constraint network" are the same
statement, and a completed sudoku is the canonical globally-consistent-looking
object that is NOT globally consistent — which is exactly why solving one needs
search and not only propagation.

THE PREDICTION, STATED BEFORE THE RUN (R 1120's practice — a conjecture on the
record so it can be refuted). Registers 1119-1122 measured REDUNDANCY — the
largest fraction of cells removable with exact recovery by ℛ — and found that
DIMENSION explains it, because ℛ works on pairwise envelopes and an index of
dimension d carries d(d-1) of them:

        Λ (d=8) 61%    Λ_spectra (d=3) 20%    box ordering (d=3) 0%
        Janet (d=2) 0%   periodic table (d=2) 0%   calendar (d=2) 0%

    and Λ's own projection: d=8 61%, d=7 30%, d=6 30%, d=5 30%, d=4 5%, d=3 0%.

A sudoku grid encoded as (row, column, value) is d = 3, so the projection series
predicts REDUNDANCY AT OR NEAR ZERO, and E(X) LARGE. If sudoku comes back
redundant, the dimension explanation is wrong and 1122 needs reopening.

*Recorded before running: I expect near-zero, and I expect the interesting number
to be E(X) rather than the redundancy.*
"""
import itertools, random

# a completed 9x9 sudoku, constructed rather than looked up
BASE = 3
SIDE = BASE * BASE


def pattern(r, c):
    return (BASE * (r % BASE) + r // BASE + c) % SIDE


rows = [g * BASE + r for g in range(BASE) for r in range(BASE)]
cols = [g * BASE + c for g in range(BASE) for c in range(BASE)]
nums = list(range(1, SIDE + 1))
GRID = [[nums[pattern(r, c)] for c in cols] for r in rows]


def valid(g):
    ok = all(sorted(row) == nums for row in g)
    ok &= all(sorted(col) == nums for col in zip(*g))
    for br in range(0, SIDE, BASE):
        for bc in range(0, SIDE, BASE):
            box = [g[br + i][bc + j] for i in range(BASE) for j in range(BASE)]
            ok &= sorted(box) == nums
    return ok


print(f"  a completed 9×9 grid, valid: {valid(GRID)}\n")

CELLS = {(r, c, GRID[r][c]) for r in range(SIDE) for c in range(SIDE)}


def opR(X, d):
    """ℛ: the monotone pairwise envelope closure."""
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


clo = opR(CELLS, 3)
E = len(clo) - len(CELLS)
print(f"  cells                : {len(CELLS)}")
print(f"  ℛ(cells)             : {len(clo)}")
print(f"  E(X) = |ℛ(X)| − |X|  : {E}")
print(f"  box                  : {SIDE**3}")
print(f"  closed?              : {E == 0}\n")

print("  REDUNDANCY — remove k cells at random, ask whether ℛ puts them back\n")
rng = random.Random(0)
print(f"    {'removed':>9}{'trials':>8}{'exact recovery':>17}")
best = 0
for frac in (0.01, 0.02, 0.05, 0.10, 0.20, 0.40):
    k = max(1, int(len(CELLS) * frac))
    hits = 0
    T = 40
    for _ in range(T):
        keep = set(rng.sample(sorted(CELLS), len(CELLS) - k))
        hits += opR(keep, 3) == clo
    if hits == T:
        best = frac
    print(f"    {frac:>8.0%}{T:>8}{hits}/{T:>16}")
print(f"\n    largest fraction removable with EXACT recovery every time: {best:.0%}")
print(f"\n  THE PREDICTION WAS: near zero, from d = 3 (registers 1119–1122).")
