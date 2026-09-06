from itertools import combinations
from collections import defaultdict
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
L9=[c+(sp,) for c in L8 for sp in range(0,c[6]+1)]
rev=lambda c:(c[4],c[5],c[6],c[3],c[0],c[1],c[2],c[8],c[7])
R=[rev(c) for c in L9]
F=set(L9); B=set(R)
I=sorted(F&B); U=sorted(F|B)

def fails(X):
    S=set(X); j=m=0
    for a,b in combinations(X,2):
        if tuple(map(max,a,b)) not in S: j+=1
        if tuple(map(min,a,b)) not in S: m+=1
    return j,m
def R_op(X,d=9):
    from itertools import product
    A=[sorted({x[i] for x in X}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            phi[(i,j)]={v:(max([x[i] for x in X if x[j]<=v]) if any(x[j]<=v for x in X) else None)
                        for v in A[j]}
    out=[]
    def rec(p):
        k=len(p)
        if k==d: out.append(tuple(p)); return
        for v in A[k]:
            ok=True
            for j in range(k):
                b=phi[(k,j)][p[j]]
                if b is None or v>b: ok=False;break
                b2=phi[(j,k)][v]
                if b2 is None or p[j]>b2: ok=False;break
            if ok: rec(p+[v])
    rec([]); return out

for name,X in [("Λ₉  forward",L9),("rev(Λ₉)  backward",R),
               ("Λ₉ ∩ rev(Λ₉)",I),("Λ₉ ∪ rev(Λ₉)",U)]:
    j,m=fails(X)
    E=len(R_op(X))-len(X) if len(X)<3000 else None
    print(f"{name:<20} |X|={len(X):>5}  join failures {j:>5}  meet failures {m:>5}  E(X) {E}")

# the intersection as a category
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[6],c[8])
IS=set(I); by=defaultdict(list)
for c in I: by[src(c)].append(c)
comp=lambda a,b:(a[0],a[1],a[2],min(a[3],b[3]),b[4],b[5],b[6],a[7],b[8])
pairs=0; bad=0
for a in I:
    for b in by.get(tgt(a),()):
        pairs+=1
        if comp(a,b) not in IS: bad+=1
print(f"\nthe intersection as a category: {pairs} composable pairs, {bad} closure failures")

objs={src(c) for c in I}|{tgt(c) for c in I}
ident={}
for A in objs:
    for e in I:
        if src(e)==A==tgt(e):
            if all(comp(a,e)==a for a in I if tgt(a)==A) and \
               all(comp(e,b)==b for b in by.get(A,())): ident[A]=e
inv=0
for a in I:
    for b in by.get(tgt(a),()):
        if tgt(b)==src(a) and comp(a,b)==ident.get(src(a)) and comp(b,a)==ident.get(tgt(a)):
            inv+=1; break
print(f"objects {len(objs)}   objects carrying an identity {len(ident)}   "
      f"morphisms with a two-sided inverse {inv} of {len(I)}")
print(f"GROUPOID (every morphism invertible): {inv==len(I) and len(ident)==len(objs)}")

# does the intersection carry its own transfer, and does it factorise?
tot=0
for q in sorted({c[3] for c in I}):
    a={(c[0],c[1],c[2],c[7]) for c in I if c[3]==q}
    b={(c[4],c[5],c[6],c[8]) for c in I if c[3]==q}
    tot+=len(a)*len(b)
print(f"\nΣ_q |A(q)|·|B(q)| = {tot}  against |∩| = {len(I)}   defect {tot-len(I)}")