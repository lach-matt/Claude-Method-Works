from itertools import combinations
from collections import defaultdict
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
X=L8; S=set(X)

# pushback: for each cell, how many pairs of OTHER cells imply it back
J=defaultdict(int); M=defaultdict(int)
for a,b in combinations(X,2):
    j=tuple(map(max,a,b)); m=tuple(map(min,a,b))
    if j!=a and j!=b: J[j]+=1
    if m!=a and m!=b: M[m]+=1
P={x:J[x]+M[x] for x in X}

vals=sorted(P.values())
zero=[x for x in X if P[x]==0]
print(f"cells {len(X)}   pushback: min {vals[0]}  median {vals[len(vals)//2]}  "
      f"max {vals[-1]}  mean {sum(vals)/len(vals):.1f}")
print(f"cells with zero pushback (removable without a single failing pair): {len(zero)}")

# join- and meet-irreducibles
below={x:[y for y in X if all(p<=q for p,q in zip(y,x)) and y!=x] for x in X}
above={x:[y for y in X if all(q<=p for p,q in zip(y,x)) and y!=x] for x in X}
def irr(x,rel):
    L=rel[x]
    if not L: return True
    r=L[0]
    for y in L[1:]: r=tuple(map(max,r,y)) if rel is below else tuple(map(min,r,y))
    return r!=x
JI=[x for x in X if irr(x,below)]; MI=[x for x in X if irr(x,above)]
both=[x for x in X if x in set(JI) and x in set(MI)]
print(f"join-irreducible {len(JI)} · meet-irreducible {len(MI)} · both {len(both)}")
print(f"zero-pushback set equals the doubly-irreducible set: {set(zero)==set(both)}")
print(f"  J(x)=0 exactly on the join-irreducibles: {set(x for x in X if J[x]==0)==set(JI)}")
print(f"  M(x)=0 exactly on the meet-irreducibles: {set(x for x in X if M[x]==0)==set(MI)}")

# is pushback a function of position?
rank=lambda x: sum(x)
import statistics
by=defaultdict(list)
for x in X: by[rank(x)].append(P[x])
print("\npushback by rank:")
for r in sorted(by): print(f"  rank {r:>2}: n={len(by[r]):>3}  median {int(statistics.median(by[r])):>6}  max {max(by[r]):>7}")

# correlation with the two obvious coordinates
def corr(u,v):
    mu,mv=sum(u)/len(u),sum(v)/len(v)
    num=sum((a-mu)*(b-mv) for a,b in zip(u,v))
    den=(sum((a-mu)**2 for a in u)*sum((b-mv)**2 for b in v))**0.5
    return num/den
w_below=[len(below[x]) for x in X]; w_above=[len(above[x]) for x in X]
pv=[P[x] for x in X]
print(f"\ncorr(pushback, cells below)  = {corr(w_below,pv):+.3f}")
print(f"corr(pushback, cells above)  = {corr(w_above,pv):+.3f}")
print(f"corr(pushback, below*above)  = {corr([a*b for a,b in zip(w_below,w_above)],pv):+.3f}")

# the E1 puncture, recomputed
T=[(a,b) for a in range(0,21) for b in range(0,21) if abs(a-b)<=2]
TS=set(T)-{(0,0)}
jf=sum(1 for a,b in combinations(TS,2) if tuple(map(max,a,b)) not in TS)
mf=sum(1 for a,b in combinations(TS,2) if tuple(map(min,a,b)) not in TS)
mprod={tuple(map(min,a,b)) for a,b in combinations(TS,2) if tuple(map(min,a,b)) not in TS}
print(f"\nE1 puncture (|Δ2J| ≤ 2, cell (0,0) removed, cap 20):")
print(f"  join failures {jf} · meet failures {mf} · products of failing meets {mprod}")