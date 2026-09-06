#!/usr/bin/env python3
"""mathfill.py -- the missing edges, taken from the corpus's own prose.

mathgraph.py returns six components. Before that is reported as a defect it must
be asked whether the corpus STATES the connection somewhere and simply never
carries it as a derivation. Each edge below is quoted from the text that asserts
it. Filling them is protocol: "look for gaps and fill with information on hand."
"""
import collections
from mathreg import REG

FILL = [
    # (child, new parent, the sentence that already asserts the link, where)
    ("A.slack", "B.V",
     "E(X) is the slack counted. The void is the slack counted over an interval. "
     "V is the slack measured. They are one quantity under three measures.",
     "M §25.2"),
    ("B.adm", "B.ordk",
     "§21.13 gives r >= 5 for the spacing and nu_V for the curvature. Those are "
     "two instances of one rule.", "M §21.10.4"),
    ("B.nuV", "B.ordk",
     "the same sentence: two instances of one rule", "M §21.10.4"),
    ("B.coll", "B.V43",
     "<r> prop nu^2 and DeltaE prop nu^-3, both from T = Z^2 R / nu^2",
     "M §24.1"),
    ("B.V43", "B.brk",
     "V is defined from the bracket's own w and e", "M §21.1"),
    ("M.C1", "A.freuder",
     "a forest of paths, one per generator, no edges between them -- stronger "
     "than a tree; and the failure mode when it does is the same one Lambda_9' "
     "exhibits: an added constraint closes a cycle and Freuder is lost.",
     "T §10.4c"),
    ("M.C1", "T.a9p",
     "the same sentence: 'lost, as at Lambda_9''", "T §10.4c"),
    ("K.helly", "A.modeB",
     "This is sub-case B at arity 5, showing the mode scales beyond the ternary "
     "case.", "T §4.4"),
    ("W.rel", "A.modeB",
     "a relation cannot be a coordinate of either side -- the arity mode at the "
     "level of vocabularies", "T §8.4"),
    ("L.dim", "L.birk",
     "order dimension of a distributive lattice is the width of its "
     "join-irreducible poset (Dilworth); the book states dim = 8 and never "
     "derives it", "M §8.6 -- INFERRED, not stated"),
]

print("  edges the corpus asserts in prose and does not carry:\n")
for child, parent, quote, where in FILL:
    mark = "*" if "INFERRED" in where else " "
    print(f"  {mark} {child:<10} <- {parent:<12} {where}")
    print(f"      \"{quote[:104]}\"")

for child, parent, _, _ in FILL:
    if parent not in REG[child]["dep"]:
        REG[child]["dep"].append(parent)

adj = collections.defaultdict(set)
for k, v in REG.items():
    for d in v["dep"]:
        adj[k].add(d); adj[d].add(k)

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

print(f"\n  after filling: {len(REG)} objects, "
      f"{sum(len(v['dep']) for v in REG.values())} edges, "
      f"{len(comps)} component(s)")
for c in comps:
    print(f"    {len(c):>3}  {c[0]} …" if len(c) > 8 else f"    {len(c):>3}  {' '.join(c)}")

if len(comps) == 1:
    print("\n  ONE COMPONENT. Every expression connects to another -- but only "
          "after ten\n  edges are supplied, nine of them quotable from the "
          "corpus and one inferred.")
