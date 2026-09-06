import sys; sys.path.insert(0,"/home/claude/method")
from itertools import combinations, product
import violations as V

BASE=[(a,b) for a,b,_ in V.IMP]
def build(imp):
    def close(S):
        S=set(S); grew=True
        while grew:
            grew=False
            for a,b in imp:
                if a in S and b not in S: S.add(b); grew=True
        return frozenset(S)
    return {V.vec(close(c)) for r in range(len(V.LAWS)+1) for c in combinations(V.LAWS,r)}

surv=[]; brk=[]
for a in V.LAWS:
    for b in V.LAWS:
        if a==b or (a,b) in BASE: continue
        X=build(BASE+[(a,b)])
        E=len(V.RR(X,8))-len(X)
        (surv if E==0 else brk).append((a,b,len(X),E))
print(f"candidate new implications tested: {len(surv)+len(brk)}")
print(f"  preserve E = 0 : {len(surv)}")
print(f"  force  E > 0 : {len(brk)}")
print("\nthe only unidentified relations that cost nothing:")
for a,b,n,E in surv: print(f"    {a} -> {b}   |V| {n:3d}   E {E}")
print("\nlargest external definition costs imposed:")
for a,b,n,E in sorted(brk,key=lambda r:-r[3])[:6]: print(f"    {a} -> {b}   |V| {n:3d}   E {E}")