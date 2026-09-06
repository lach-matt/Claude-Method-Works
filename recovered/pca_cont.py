import sys; sys.path.insert(0,"/home/claude/work")
from contingency import contingency_rate, label, minE
AX=[5,5,3]
for n,lab in ((13,"baseline, subvalence+valence"),(15,"+X-ray at subvalence,A"),(14,"+X-ray at valence,C")):
    r=contingency_rate(set(), AX, trials=1) if False else None
import random
from itertools import product
# rate: over random cell sets of the same size on the same grid, what fraction refuse?
def rate(n,axes,trials=80):
    pool=[c for c in product(*[range(a) for a in axes])]
    pos=tot=0
    for s in range(trials):
        c=set(random.Random(s).sample(pool,n)); tot+=1
        if minE(c,axes)>0: pos+=1
    return pos/tot
for n,lab in ((13,"baseline (E=1)"),(15,"X-ray at subvalence·A (E=0)"),(14,"X-ray at valence·C (E=0)")):
    r=rate(n,AX)
    print(f"  {lab:<32} n={n:<3} {100*r:>3.0f}% of comparable sets refuse")