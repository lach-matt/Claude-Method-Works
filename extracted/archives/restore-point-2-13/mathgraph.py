#!/usr/bin/env python3
"""mathgraph.py -- the corpus as one dependency graph.

The claim under test is that every mathematical expression connects to another.
That is checkable: build the graph on the register's `dep` edges and look at its
components. An isolated node is either a genuine gap (something the corpus uses
without deriving) or an import (something it cites and does not own).
"""
import collections
from mathreg import REG

# ---- integrity of the register first ----------------------------------------
bad = [(k, d) for k, v in REG.items() for d in v["dep"] if d not in REG]
if bad:
    print("  DANGLING DEPENDENCIES:", bad)

adj = collections.defaultdict(set)
for k, v in REG.items():
    for d in v["dep"]:
        adj[k].add(d); adj[d].add(k)

# ---- connected components ----------------------------------------------------
seen, comps = set(), []
for k in REG:
    if k in seen: continue
    stack, c = [k], []
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x); c.append(x)
        stack.extend(adj[x] - seen)
    comps.append(sorted(c))
comps.sort(key=len, reverse=True)

print(f"  objects {len(REG)}   edges {sum(len(v['dep']) for v in REG.values())}"
      f"   components {len(comps)}")
for c in comps:
    tag = "MAIN" if len(c) == len(comps[0]) else ("isolated" if len(c) == 1 else "fragment")
    print(f"    {len(c):>3}  {tag:<9} {' '.join(c) if len(c) <= 8 else c[0] + ' …'}")

# ---- roots: objects nothing here derives ------------------------------------
print("\n  ROOTS -- taken as given, not derived in the corpus:")
for k, v in sorted(REG.items()):
    if not v["dep"]:
        print(f"    {k:<12} {v['grade']:<13} {(v['named'] or '*** UNNAMED ***')[:56]}")

# ---- leaves: nothing depends on them ----------------------------------------
used = {d for v in REG.values() for d in v["dep"]}
leaves = [k for k in REG if k not in used]
print(f"\n  LEAVES -- nothing in the corpus builds on them: {len(leaves)}")
for k in sorted(leaves):
    v = REG[k]
    print(f"    {k:<12} {v['grade']:<13} {v['stmt'][:64]}")

# ---- the gap test: unnamed AND a root  ---------------------------------------
print("\n  GAP CANDIDATES -- unnamed and underived (a root with no standing name):")
for k, v in sorted(REG.items()):
    if not v["dep"] and not v["named"]:
        print(f"    {k:<12} {v['stmt'][:78]}")

# ---- unnamed and load-bearing ------------------------------------------------
deg = collections.Counter()
for k, v in REG.items():
    for d in v["dep"]:
        deg[d] += 1
print("\n  UNNAMED AND LOAD-BEARING -- search targets, by how much rests on them:")
targets = [(deg[k], k, v) for k, v in REG.items() if not v["named"] and deg[k] > 0]
for n, k, v in sorted(targets, reverse=True)[:18]:
    print(f"    {n:>2} dependents  {k:<12} {v['stmt'][:66]}")
