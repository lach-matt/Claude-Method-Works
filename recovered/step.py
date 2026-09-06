from itertools import combinations
from collections import defaultdict
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
X=L8; S=set(X); idx={x:i for i,x in enumerate(X)}
le=lambda a,b: all(p<=q for p,q in zip(a,b))

# producers: for each cell z, the pairs of other cells that join or meet to z
prod=defaultdict(list)
for a,b in combinations(X,2):
    j=tuple(map(max,a,b)); m=tuple(map(min,a,b))
    if j!=a and j!=b: prod[j].append((a,b))
    if m!=a and m!=b: prod[m].append((a,b))

def removable(R):
    """X\R is closed iff every producing pair of every z in R meets R."""
    Rs=set(R)
    for z in R:
        for a,b in prod[z]:
            if a not in Rs and b not in Rs: return False
    return True

# all intervals of Lambda_8, by size
intervals={}
for a in X:
    for b in X:
        if a!=b and le(a,b):
            cells=tuple(sorted(y for y in X if le(a,y) and le(y,b)))
            intervals[(a,b)]=cells
print(f"comparable pairs / intervals: {len(intervals):,}")
by_size=sorted(intervals.items(), key=lambda kv: len(kv[1]))
print(f"interval sizes run {len(by_size[0][1])} to {len(by_size[-1][1])}")

found=None
for (a,b),cells in by_size:
    if removable(cells):
        found=((a,b),cells); break
print()
if found:
    (a,b),cells=found
    print(f"SMALLEST REMOVABLE INTERVAL: {len(cells)} cells")
    print(f"  from {a}\n  to   {b}")
    print(f"  survivor lattice: {len(X)-len(cells)} cells = {100*(len(X)-len(cells))/len(X):.1f}% of Lambda_8")
    rest=[x for x in X if x not in set(cells)]
    RS=set(rest)
    bad=sum(1 for p,q in combinations(rest,2)
            if tuple(map(max,p,q)) not in RS or tuple(map(min,p,q)) not in RS)
    print(f"  verified: {bad} join/meet failures among the {len(rest)*(len(rest)-1)//2:,} surviving pairs")
    # is it a box?
    lo=[min(c[i] for c in cells) for i in range(8)]
    hi=[max(c[i] for c in cells) for i in range(8)]
    boxsize=1
    for i in range(8): boxsize*= hi[i]-lo[i]+1
    print(f"  the removed set is a full coordinate box: {boxsize==len(cells)}  (box {boxsize})")
    print(f"  extent per coordinate: {[hi[i]-lo[i]+1 for i in range(8)]}")
else:
    print("no removable interval found")