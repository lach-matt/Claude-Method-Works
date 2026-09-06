from itertools import combinations
from collections import defaultdict
from functools import reduce
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
X=L8; le=lambda a,b: all(p<=q for p,q in zip(a,b))
bot=min(X,key=sum); top=max(X,key=sum)
JI=set();MI=set()
for x in X:
    B=[y for y in X if le(y,x) and y!=x]; A=[y for y in X if le(x,y) and y!=x]
    if x!=bot and reduce(lambda p,q:tuple(map(max,p,q)),B)!=x: JI.add(x)
    if x!=top and reduce(lambda p,q:tuple(map(min,p,q)),A)!=x: MI.add(x)
# join-PRIME = join-irreducible or the bottom; meet-PRIME = meet-irreducible or the top
JP=JI|{bot}; MP=MI|{top}
prod=defaultdict(list)
for u,v in combinations(X,2):
    j=tuple(map(max,u,v)); m=tuple(map(min,u,v))
    if j!=u and j!=v: prod[j].append((u,v))
    if m!=u and m!=v: prod[m].append((u,v))
def removable(R):
    Rs=set(R)
    return all(not(u not in Rs and v not in Rs) for z in R for u,v in prod[z])

for name,Aset,Bset in [("irreducible only",JI,MI),("prime (irreducible or extreme)",JP,MP)]:
    dis=0; tot=0; ex=[]
    for a in X:
        for b in X:
            if not le(a,b): continue
            tot+=1
            R=[y for y in X if le(a,y) and le(y,b)]
            pred=(a in Aset) and (b in Bset)
            if pred!=removable(R):
                dis+=1
                if len(ex)<3: ex.append((a,b,len(R),pred))
    print(f"{name:<32} {dis} disagreements in {tot:,} intervals  {ex[:2] if ex else ''}")

best=None
for a in JP:
    for b in MP:
        if le(a,b):
            n=sum(1 for y in X if le(a,y) and le(y,b))
            if 1<n<len(X) and (best is None or n<best[0]): best=(n,a,b)
print(f"\ncorrected step = {best[0]}   interval {best[1]} .. {best[2]}")
R=[y for y in X if le(best[1],y) and le(y,best[2])]
rest=[y for y in X if y not in set(R)]; RS=set(rest)
bad=sum(1 for u,v in combinations(rest,2)
        if tuple(map(max,u,v)) not in RS or tuple(map(min,u,v)) not in RS)
print(f"removing it leaves {len(rest)} cells with {bad} join/meet failures  "
      f"({100*len(rest)/len(X):.2f}% of Λ₈)")