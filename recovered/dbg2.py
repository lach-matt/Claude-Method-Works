from itertools import product
def Rop(S,d=2):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
A=[sorted({x[i] for x in PT}) for i in range(2)]
sup={a:frozenset(y for (x,y) in PT if x==a) for a in A[0]}
occ={b:sum(1 for a in A[0] if b in sup[a]) for b in A[1]}
o0=sorted(A[0],key=lambda a:(-len(sup[a]),a))
o1=sorted(A[1],key=lambda b:(-occ[b],b))
i0={v:i for i,v in enumerate(o0)}; i1={v:i for i,v in enumerate(o1)}
T={(i0[x],i1[y]) for (x,y) in PT}
print("|PT| =",len(PT)," |T| =",len(T))
print("|R(PT)| - |PT| =",len(Rop(PT))-len(PT))
print("|R(T)|  - |T|  =",len(Rop(T))-len(T))
ex=Rop(T)-T
print("excess:",sorted(ex)[:10])
print()
print("REVERSED row order (ascending) for comparison:")
o0b=sorted(A[0],key=lambda a:(len(sup[a]),a))
i0b={v:i for i,v in enumerate(o0b)}
T2={(i0b[x],i1[y]) for (x,y) in PT}
print("  |R(T2)| - |T2| =",len(Rop(T2))-len(T2))
print()
print("**In proof3.py the reported 36 came from the DESCENDING sort — check")
print("  whether canon() there used the same key.**")