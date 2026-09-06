import sys; sys.path.insert(0,"/tmp")
import li_mod as li
from itertools import combinations, product
import random

R,C = 4,5
cells_all = [(r,c) for r in range(R) for c in range(C)]

# CLAIM: if every row holds at most one cell, some ordering makes the
# assignment monotone, hence min E = 0 — forced, not measured.
inj = [S for S in combinations(cells_all,4)
       if len({r for r,_ in S})==4]
bad = []
for S in inj:
    E,_ = li.minE(set(S),[R,C])
    if E!=0: bad.append((S,E))
print(f"row-injective 4-cell sets on a {R}x{C} grid : {len(inj)}")
print(f"   of these, ones with min E > 0            : {len(bad)}")

# and the converse: let two ladders share a row, does E>0 become reachable?
noninj = [S for S in combinations(cells_all,4) if len({r for r,_ in S})==3]
sample = random.Random(0).sample(noninj, 400)
pos = [S for S in sample if li.minE(set(S),[R,C])[0] > 0]
print(f"\n4-cell sets with ONE shared row (sample of 400): {len(pos)} have min E > 0"
      f"  ({100*len(pos)/len(sample):.0f}%)")