import numpy as np, random
from itertools import product, permutations
random.seed(337)
def closed(S,A):
    d=len(A); ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==S
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def reord(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(a)) for a in A]):
        T=relab(S,[list(p) for p in ps],d)
        if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): return True
    return False
print("="*84)
print("  BOUND 1 — DIMENSION OR ALPHABET SIZE?")
print("="*84)
print("\n  %6s%8s%10s%14s%14s"%("d","|A|","n","closed as-is","reorderable"))
print("  "+"-"*52)
for d,a,lim in [(2,2,500),(2,3,300),(2,4,120),(3,2,300),(3,3,60)]:
    n=c=r=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        n+=1; c+=closed(S,Aa); r+=reord(S,d)
    if n: print("  %6d%8d%10d%14.3f%14.3f"%(d,a,n,c/n,r/n))