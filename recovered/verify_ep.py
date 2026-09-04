import lam8
from collections import defaultdict
from itertools import combinations
import random
L8=lam8.L8(); S=set(L8)

# MC-21: e(P) = linear extensions of the poset of join-irreducibles P, where L8 = J(P).
# For a distributive lattice L=J(P), maximal chains of L = linear extensions of P.
# Faster: number of maximal chains from bottom to top = number of ways to add one "electron"
# (increment total rank by 1) at a time staying inside L, from min element to max element.
# That equals the number of monotone lattice paths = e(P). Count via DP over the lattice:
# maximal chains through a graded lattice where each cover step raises rank by exactly 1.
# chains(x) into x = sum over lower covers. We count saturated chains bottom->top.
bottom=tuple(min(x[i] for x in L8) for i in range(8))
top=tuple(max(x[i] for x in L8) for i in range(8))
print("bottom",bottom,"top",top, "bottom in S", bottom in S, "top in S", top in S)
# cover: y covers x if y>=x componentwise, sum(y)=sum(x)+1, both in S
# DP by increasing rank
byrank=defaultdict(list)
for x in L8: byrank[sum(x)].append(x)
ranks=sorted(byrank)
ways=defaultdict(int); ways[bottom]=1
for r in ranks:
    for x in byrank[r]:
        if ways[x]==0: continue
        # generate upper covers: increment one coordinate by 1
        for i in range(8):
            y=list(x); y[i]+=1; y=tuple(y)
            if y in S and sum(y)==r+1:
                ways[y]+=ways[x]
print("e(P) = saturated chains bottom->top:", ways[top], " claim 1,113,045,672")

# interval-is-box: exact on 60/60 tested; 27% of random intervals qualify
# constraint binds if the interval is NOT a box because of that constraint
# constraints: q<=k, g<=q, g<=4f+2  (indices: n0 l1 k2 q3 e4 f5 g6 S7)
def isbox(x,y):
    # [x,y] is box iff every element with x<=z<=y componentwise is in S
    rngs=[range(x[i],y[i]+1) for i in range(8)]
    from itertools import product as prod
    for z in prod(*rngs):
        if z not in S: return False
    return True
random.seed(1)
Ll=list(L8)
tested=0; boxes=0
# comparable pairs x<=y
def leq(a,b): return all(a[i]<=b[i] for i in range(8))
pairs=[]
for _ in range(20000):
    a,b=random.choice(Ll),random.choice(Ll)
    if leq(a,b) and a!=b:
        pairs.append((a,b))
    if len(pairs)>=2000: break
for a,b in pairs:
    tested+=1
    if isbox(a,b): boxes+=1
print(f"interval-is-box on {tested} random comparable intervals: {boxes} boxes = {100*boxes/tested:.0f}%  (claim ~27%)")