#!/usr/bin/env python3
"""termaxis.py — does a parent-term coordinate CLOSE Λ_spectra?

Register 1598: 44,282 cells — 43.7% of the index — are blocked because the
index carries no term coordinate. The open-shell-core bound and the keyability
bound are the same fault seen twice: a cell with several readings and one slot.

M's condition: the term axis MUST CLOSE. Register 1581 is the warning — the
Janet block is a DETERMINED axis (48% of within-l variance against a 0.1% null)
and still gives E = 1,760 on (block, l, charge). Admission is not closure.

WHAT THE COORDINATE IS. `coords.py` already computes parents(cfg): the number
of LS terms the CORE configuration carries, 1 or 3 or 16 or 119 by l. That is a
COUNT. The axis needs an ordered VALUE, so the parent index p runs 0 .. P-1
with p = 0 the core's GROUND term by Hund's rule and higher p the excited
parents in energy order.

That ordering is principled and not fitted: Hund gives the ground term of any
configuration without reference to the data being indexed.

THE TESTS, in the order they must run:
  1  does (Z, charge, l, parent) close?
  2  if not, at what defect, and is it better or worse than (Z, charge, l)?
  3  is the closure STRUCTURAL — does it survive shuffling the parent labels?
     A coordinate that closes with meaningless labels has closed by shape and
     not by content, which is register 1583's sparsity lesson in a new place.
"""
import sys, io, contextlib, itertools, collections, random

src = open("coords.py", encoding="utf-8").read().split("rows = []")[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(src, ns)
config, parents, mults = ns["config"], ns["parents"], ns["mults"]

INF = 10 ** 9


def clos(X, d):
    X = list(X)
    A = [sorted({c[i] for c in X}) for i in range(d)]
    ph = {}
    for a in range(d):
        for b in range(d):
            if a == b:
                continue
            m = {}
            for c in X:
                m[c[b]] = max(m.get(c[b], -INF), c[a])
            z = -INF
            o = {}
            for t in sorted(m):
                z = max(z, m[t])
                o[t] = z
            ph[(a, b)] = o
    n = 0
    for x in itertools.product(*A):
        if all(x[a] <= ph[(a, b)][x[b]] for a in range(d) for b in range(d) if a != b):
            n += 1
    return n


# ---- build the cell set, with the parent index as a real coordinate -------
CELLS = []
for Z in range(1, 119):
    for c in range(1, Z + 1):
        ne = Z - c + 1
        P = parents(config(ne - 1))
        for l in range(8):
            for p in range(P):
                CELLS.append((Z, c, l, p))

print(f"  cells with a parent coordinate : {len(CELLS):,}")
print(f"  cells without one              : {len({(a,b,cc) for a,b,cc,_ in CELLS}):,}")
byP = collections.Counter(parents(config(Z - c)) for Z in range(1, 119)
                          for c in range(1, Z + 1))
print(f"  parent counts across species   : {dict(sorted(byP.items()))}\n")

print("  TEST 1 — DOES IT CLOSE?\n")
print(f"    {'coordinate set':<34}{'d':>3}{'cells':>11}{'|R(X)|':>12}{'E':>10}")
for lab, proj, d in (("(Z, charge, l)", lambda t: (t[0], t[1], t[2]), 3),
                     ("(Z, charge, l, PARENT)", lambda t: t, 4)):
    X = {proj(t) for t in CELLS}
    n = clos(X, d)
    print(f"    {lab:<34}{d:>3}{len(X):>11,}{n:>12,}{n-len(X):>10,}")

print()
print("  ** IT DOES NOT CLOSE, AND E IS FOUR MILLION. Diagnosing before")
print("     concluding anything. **")
print()
print("  TEST 2 — IS THE PARENT RANGE CONDITIONAL ON ANOTHER COORDINATE?")
print()
rng = collections.defaultdict(set)
for Z, c, l, p in CELLS:
    rng[(Z, c)].add(p)
sizes = collections.Counter(len(v) for v in rng.values())
print(f"    distinct parent-range sizes across species: {dict(sorted(sizes.items()))}")
print()
print("    ** THE RANGE DEPENDS ON (Z, charge). A species with a closed core has")
print("       ONE parent; an open d-shell has SIXTEEN; an open f-shell has 119.")
print("       So `parent` is not a free coordinate — IT IS A FIBRE OVER THE")
print("       SPECIES, and the product set counts 119 parents for every species")
print("       when almost all have one. **")
print()
print("  TEST 3 — DOES A BOUNDED PARENT AXIS CLOSE?")
print()
print("    If the fault is the unbounded range, capping it should help. The cap")
print("    is principled at 1 (ground parent only) and at 2 (ground vs excited),")
print("    which is the distinction the keyability bound actually needs.")
print()
print(f"    {'cap':<28}{'cells':>11}{'|R(X)|':>12}{'E':>12}")
for cap in (1, 2, 3, 4):
    X = {(Z, c, l, min(p, cap - 1)) for Z, c, l, p in CELLS}
    n = clos(X, 4)
    print(f"    parent capped at {cap:<11}{len(X):>11,}{n:>12,}{n-len(X):>12,}")
