#!/usr/bin/env python3
"""ebook.py -- E(book), computed. O1 and O2.

§30.1 defines the index and never runs it:

    "Its cells are (claim, location, support). Its coordinates are the part, the
     chapter and the section. Its constraints are of §16.4 form: a claim in
     section s is supported by evidence in a section at or before s, and a
     specialisation inherits its generalisation's locations."

Operationalised exactly as written:
  claim     a paragraph carrying a quantitative claim -- §30.6's own test
  location  the chapter the claim sits in
  support   the earliest chapter it cites as evidence
  constraint  support <= location, which is §16.4 form: one coordinate bounded
              by a monotone function of one other

Two resolutions are reported, because §18.4.1's asymmetry says E > 0 at low
density measures sparsity rather than structure.
"""
import re, sys, itertools
from collections import Counter
from zeno import State, step

S = open("The Method 1.6.md", encoding="utf-8").read()
BODY_START = S.index("# PART 0 — THE SHAPE", S.index("# PART 0 — THE SHAPE") + 10)
B = S[BODY_START:]
RS = B.rindex("## 26. Withdrawals"); RE_ = B.rindex("## 27.")

def R(X, d):
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

NUM = re.compile(r"\b\d[\d,]*(?:\.\d+)?\b|\b\d+(?:\.\d+)?%")
CITE = re.compile(r"§(\d+)(?:\.\d+)*")

def harvest():
    """every claim-bearing paragraph, with the chapter it sits in and the
    earliest chapter it cites."""
    cells, unsupported, chap = [], 0, None
    for para in re.split(r"\n\s*\n", B):
        h = re.match(r"^#{2,4} (\d+)[\. ]", para.strip())
        if h: chap = int(h.group(1)); continue
        m = re.match(r"^#{2,4} (\d+)\.(\d+)", para.strip())
        if m: chap = int(m.group(1)); continue
        if chap is None: continue
        # the register is excluded: it is a record, not a claim -- register 397
        pos = B.index(para) if para in B else -1
        if RS < pos < RE_: continue
        if not NUM.search(para): continue
        if len(para.split()) < 12: continue
        cited = [int(x) for x in CITE.findall(para)]
        cited = [c for c in cited if 1 <= c <= 30]
        if not cited:
            unsupported += 1
            continue
        cells.append((chap, min(cited)))
    return cells, unsupported

with State("ebook") as st:
    cells, unsupported = step(st, "harvest the claim-bearing paragraphs", harvest, budget=180)

X = set(cells)
print(f"  claim-bearing paragraphs harvested   {len(cells)}")
print(f"  ...carrying no § citation at all     {unsupported}   (no support coordinate)")
print(f"  distinct (location, support) cells   {len(X)}")

nch = 30
box = nch * nch
Rx = R(X, 2)
E = len(Rx) - len(X)
print(f"\n  THE BOOK'S OWN INDEX, at chapter resolution")
print(f"    cells        {len(X)}")
print(f"    ambient box  {box}   (30 chapters × 30)")
print(f"    density      {100*len(X)/box:.1f}%")
print(f"    |ℛ(X)|       {len(Rx)}")
print(f"    E(book)      {E}")
print(f"    possibility bound  0 ≤ E ≤ {box - len(X)}")

# the stated constraint: support <= location. how many claims violate it?
viol = [(a, b) for a, b in X if b > a]
print(f"\n  §30.1's constraint — support at or before the claim:")
print(f"    cells violating it   {len(viol)}   {sorted(viol)[:8]}{' …' if len(viol)>8 else ''}")
print(f"    forward references are the violation, and the book allows none by its own rule")

# restricted to the constraint the book states
Xc = {c for c in X if c[1] <= c[0]}
Rc = R(Xc, 2)
print(f"\n  RESTRICTED to the cells §30.1 admits:")
print(f"    cells {len(Xc)}   |ℛ| {len(Rc)}   E = {len(Rc)-len(Xc)}   "
      f"density {100*len(Xc)/(nch*(nch+1)//2):.1f}% of the admissible triangle")

gap = sorted(Rc - Xc)
print(f"\n  admitted and absent, first twelve of {len(gap)}:")
for g in gap[:12]:
    print(f"    a claim in chapter {g[0]:>2} supported no earlier than chapter {g[1]:>2}")
sys.exit(0)
