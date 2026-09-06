#!/usr/bin/env python3
"""onbank.py — what the FOLDER alone can answer about facets 1-5.

Source: /mnt/project/COORDINATES-2_13.csv (grade == 'measured' only).
No fetch. No computed-grade value is read as evidence.

Diagonal reading (bridge Finding II): on a Madelung diagonal M = n + l,
    p = n - l - 1 = M - 2l - 1.
So at fixed M the vector index p is determined by l alone, and the facet
inequalities of Finding I are second differences of the measured channel
defect read across l.
"""
import csv, sys

ROWS = list(csv.DictReader(open('/mnt/project/COORDINATES-2_13.csv', encoding='utf-8')))
MEAS = {}
for r in ROWS:
    if r['grade'] == 'measured':
        MEAS.setdefault((int(r['Z']), int(r['charge'])), {})[int(r['l'])] = float(r['delta'])

FACETS = {
    1: ((0, +1), (2, -2), (4, +1)),
    2: ((0, +2), (2, -3), (6, +1)),
    3: ((1, +1), (4, -2), (6, +1)),
    4: ((1, +1), (3, -2), (5, +1)),
    5: ((3, +1), (5, -2), (7, +1)),
}

def vvec(species, M):
    """v[p] from measured delta at diagonal M; p = M - 2l - 1."""
    d = MEAS.get(species, {})
    return {M - 2 * l - 1: v for l, v in d.items() if 0 <= M - 2 * l - 1 <= 7}

def evaluate(name, species, M, facets):
    v = vvec(species, M)
    print(f"\n{name}  (Z={species[0]}, charge={species[1]}, diagonal M={M})")
    print("  measured v[p]: " + ", ".join(f"v{p}={v[p]:.5f}" for p in sorted(v)) or "  none")
    for f in facets:
        need = [p for p, _ in FACETS[f]]
        have = [p for p in need if p in v]
        if len(have) == len(need):
            val = sum(c * v[p] for p, c in FACETS[f])
            print(f"  facet {f}  {val:+.5f}   {'SATISFIED (<0)' if val < 0 else 'VIOLATED (>=0)'}")
        else:
            miss = [p for p in need if p not in v]
            ls = [(M - 1 - p) // 2 for p in miss]
            print(f"  facet {f}  NOT EVALUABLE — missing v{miss} = measured delta at l={ls}")

print("=" * 68)
print("REPRODUCTION — M=7 diagonal, Xe core (bridge Finding III, facets 1-2)")
print("=" * 68)
evaluate("Cs I", (55, 1), 7, [1, 2])
evaluate("Ba II", (56, 2), 7, [1, 2])

print("\n" + "=" * 68)
print("THE M=8 DIAGONAL — facets 4 and 5, from the folder alone")
print("=" * 68)
for name, sp in [("Fr I", (87, 1)), ("Ra II", (88, 2)), ("Ac III", (89, 3)),
                 ("Tl I", (81, 1)), ("Hg II", (80, 2))]:
    evaluate(name, sp, 8, [4, 5])

print("\n" + "=" * 68)
print("FACET 3 — the cross-diagonal chord, on whatever carries v1,v4,v6")
print("=" * 68)
for name, sp in [("Tl I", (81, 1)), ("Fr I", (87, 1)), ("Cs I", (55, 1))]:
    evaluate(name, sp, 8, [3])
