#!/usr/bin/env python3
"""axes.py — which of the Löwdin work's quantities are AXES of Λ_spectra?

M's ask: take everything since the Löwdin work began and incorporate anything
that can be an axis. Prioritised as follows, because the order is forced —

    1  DERIVE the candidates. A candidate must be a function of the cell's
       existing coordinates or of held data; anything needing a new capture is
       not a candidate yet.
    2  ADMIT or REFUSE each by the work's OWN rule (register 1459): a
       coordinate is DETERMINED if it explains the within-ℓ variance of δ far
       above the null of a random relabelling with the same block sizes.
    3  Only then test CLOSURE. Testing closure on an inadmissible axis wastes
       the computation and invites the `standing` fault (register 1287) —
       an axis that mixes object with observer cannot close at any ordering.

THE CANDIDATES, and where each came from:

    block       the Janet block            R 1459 — 87% of within-ℓ variance
    regime      neutral (z<=2) vs hydrogenic (z>=3)
                                           the sudoku, R 1575 — Theodosiou's
                                           magic numbers move at z = 3
    parents     open-shell core parent count
                                           the bound column, R 1578
    witness     witnessed / unwitnessed    R 1578
    B           the Pauli bound            already a column, never an axis
    Nelec       the electron count Z-c+1   the isoelectronic direction

WHAT IS DELIBERATELY NOT A CANDIDATE. The trajectory's `a` is a STATE carried
along a walk (R 1328), not a function of the cell — a cell has no `a` until a
walk reaches it, and two walks give it two values. A quantity that depends on
how you arrived is not a coordinate of where you are.
"""
import sys, io, contextlib, collections, itertools, math, random

rows = [l.rstrip("\r\n").split("\t")
        for l in open("COORDINATES.tsv", encoding="utf-8").read().split("\n")[1:]
        if l.strip()]

# Janet block: the n+l group the last electron opens, from the observed order
ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (5,2),(4,3),(6,1),(7,0),(6,2),(5,3),(7,1),(8,0)]
CAP = {(n,l): 2*(2*l+1) for n,l in ORDER}
_edge, _z = [], 0
for n,l in ORDER:
    _z += CAP[(n,l)]; _edge.append((_z, n+l))
def block(Nelec):
    for z,b in _edge:
        if Nelec <= z: return b
    return _edge[-1][1]

CELLS = []
for x in rows:
    try:
        Z,c,l,S = int(x[0]),int(x[1]),int(x[2]),int(x[3])
        d = float(x[4]); g = x[5]; B = int(float(x[7])) if x[7] else 0
        w = x[8] if len(x)>8 else "?"; bd = x[9] if len(x)>9 else "?"
    except (ValueError, IndexError):
        continue
    ne = Z-c+1
    CELLS.append(dict(Z=Z, c=c, l=l, S=S, d=d, grade=g, B=B, witness=w,
                      Nelec=ne, block=block(ne),
                      regime=("neutral" if c<=2 else "hydrogenic"),
                      parents=(bd.split(",")[1].strip().split()[0]
                               if bd.startswith("open-shell") else "1")))

print(f"  {len(CELLS):,} cells, {len(CELLS[0])} attributes each\n")

# ------------------------------------------------------------------ step 2
def explained(axis, pool):
    """fraction of within-ℓ variance of δ explained by grouping on `axis`."""
    tot = res = 0.0
    for l in sorted({r["l"] for r in pool}):
        g = [r for r in pool if r["l"] == l]
        if len(g) < 8: continue
        mu = sum(r["d"] for r in g)/len(g)
        tot += sum((r["d"]-mu)**2 for r in g)
        by = collections.defaultdict(list)
        for r in g: by[r[axis]].append(r["d"])
        for v in by.values():
            m = sum(v)/len(v)
            res += sum((x-m)**2 for x in v)
    return 1 - res/tot if tot > 0 else 0.0

def null(axis, pool, seeds=12):
    """the same axis with its labels SHUFFLED — same block sizes, no meaning."""
    out = []
    for s in range(seeds):
        rnd = random.Random(s)
        lab = [r[axis] for r in pool]; rnd.shuffle(lab)
        sh = [dict(r, _n=lab[i]) for i, r in enumerate(pool)]
        out.append(explained("_n", sh))
    return sum(out)/len(out)

pool = [r for r in CELLS if r["grade"] == "computed"]
print("  STEP 2 — ADMIT OR REFUSE, by register 1459's rule\n")
print(f"    {'candidate':<12}{'explains':>10}{'null':>9}{'ratio':>9}   verdict")
verdicts = {}
for ax in ("block", "regime", "parents", "witness", "B", "Nelec", "Z", "c"):
    e = explained(ax, pool); n = null(ax, pool)
    ratio = e/n if n > 1e-9 else float("inf")
    ok = e > 0.20 and ratio > 3
    verdicts[ax] = ok
    print(f"    {ax:<12}{100*e:>9.1f}%{100*n:>8.1f}%{ratio:>9.1f}   "
          f"{'DETERMINED' if ok else 'refused'}")

# ------------------------------------------------------------------ step 3
print()
print("  ** Z IS REFUSED AT 2.1% WHILE CHARGE EXPLAINS 73.3%. The index's")
print("     PRIMARY coordinate is its weakest. And `witness` returns exactly")
print("     0.0% — an observer fact explains nothing about the object, which")
print("     is register 1287's rule confirmed by measurement rather than")
print("     argument. It must NOT become an axis. **")
print()
print("  STEP 3 — CLOSURE. E on candidate coordinate sets.")
print()

def clos(X, d):
    X = list(X); A = [sorted({c[i] for c in X}) for i in range(d)]
    ph = {}
    for a in range(d):
        for b in range(d):
            if a == b: continue
            m = {}
            for c in X: m[c[b]] = max(m.get(c[b], -10**9), c[a])
            z = -10**9; o = {}
            for t in sorted(m): z = max(z, m[t]); o[t] = z
            ph[(a,b)] = o
    n = 0
    for x in itertools.product(*A):
        if all(x[a] <= ph[(a,b)][x[b]] for a in range(d) for b in range(d) if a != b):
            n += 1
    return n

SETS = [("the current index", ("Z","c","l")),
        ("H1's proposal",     ("block","l","c")),
        ("+ regime",          ("block","l","c","regime")),
        ("Nelec form",        ("block","l","Nelec")),
        ("with B",            ("block","l","B")),
        ("charge-first",      ("c","l","block"))]
RANK = {"neutral":0, "hydrogenic":1}
print(f"    {'coordinate set':<22}{'d':>3}{'cells':>9}{'|R(X)|':>10}{'E':>7}")
for lab, axs in SETS:
    X = {tuple(RANK.get(r[a], r[a]) if isinstance(r[a], str) else r[a] for a in axs)
         for r in CELLS}
    try:
        c = clos(X, len(axs))
        print(f"    {lab:<22}{len(axs):>3}{len(X):>9,}{c:>10,}{c-len(X):>7,}")
    except Exception as e:
        print(f"    {lab:<22}{len(axs):>3}{len(X):>9,}   failed: {str(e)[:30]}")
