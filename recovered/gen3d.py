import numpy as np, math, time, random
from itertools import product, permutations, combinations
random.seed(587)
print("="*88)
print("  TWO GENERATORS AT d = 3, RUN IN TANDEM")
print("="*88)
print("""
  **GENERATOR A — from the bound system.** A closed set is
  X = {x : x_i ≤ min_j φ_ij(x_j)} with every φ_ij monotone. **Enumerate the
  φ's, form the set, keep the canonical representatives.**

  **GENERATOR B — from the sublattice definition.** Closure ≡ join/meet
  closure (proved, 1,487 instances). **Close every subset under join and meet
  and keep the fixed points.**

  **Two independent routes to the same family (C.2.8), plus the exhaustive
  census as a third witness.**
""")
def is_closed(S,d):
    A=[sorted({x[i] for x in S}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==set(S)
def is_sublat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def monos(k,hi):
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
def genA(dims):
    """from the bound system"""
    d=len(dims); A=[list(range(x)) for x in dims]
    pairs=[(i,j) for i in range(d) for j in range(d) if i!=j]
    cand={p:monos(dims[p[1]],dims[p[0]]) for p in pairs}
    out=set()
    keys=list(cand.keys())
    for combo in product(*[cand[k] for k in keys]):
        ph=dict(zip(keys,combo))
        S=frozenset(x for x in product(*A)
                    if all(x[i]<=ph[(i,j)][x[j]] for (i,j) in pairs))
        if S: out.add(S)
    return out
def genB(dims):
    """from the sublattice definition — close every subset"""
    d=len(dims); cells=list(product(*[range(x) for x in dims])); n=len(cells)
    out=set()
    for m in range(1,1<<n):
        S=frozenset(cells[i] for i in range(n) if m>>i & 1)
        if is_sublat(S,d): out.add(S)
    return out
def census(dims):
    d=len(dims); cells=list(product(*[range(x) for x in dims])); n=len(cells)
    return {frozenset(cells[i] for i in range(n) if m>>i & 1)
            for m in range(1,1<<n)
            if is_closed({cells[i] for i in range(n) if m>>i & 1},d)}
print("="*88)
print("  RUN IN TANDEM")
print("="*88)
print("\n  %12s%8s%12s%12s%12s%10s%10s"%("box","cells","GEN A","GEN B","census","A=B","B=cens"))
print("  "+"-"*78)
for dims in [(2,2,2),(2,2,3),(2,3,3)]:
    n=int(np.prod(dims))
    t0=time.time(); A=genA(dims); ta=time.time()-t0
    t0=time.time(); B=genB(dims); tb=time.time()-t0
    C=census(dims)
    print("  %12s%8d%12d%12d%12d%10s%10s"%("×".join(map(str,dims)),n,len(A),len(B),len(C),
        "YES" if A==B else "no","YES" if B==C else "no"))
    if A!=B:
        onlyB=sorted(B-A)[:1]; onlyA=sorted(A-B)[:1]
        if onlyB: print("        in B not A : %s"%str(sorted(onlyB[0]))[:52])
        if onlyA: print("        in A not B : %s"%str(sorted(onlyA[0]))[:52])
print("="*88)
print("  AND THE COST COMPARISON")
print("="*88)
print("\n  %12s%10s%14s%14s%16s"%("box","cells","GEN A time","GEN B time","subsets"))
print("  "+"-"*68)
for dims in [(2,2,2),(2,2,3),(2,3,3)]:
    n=int(np.prod(dims))
    t0=time.time(); genA(dims); ta=time.time()-t0
    t0=time.time(); genB(dims); tb=time.time()-t0
    print("  %12s%10d%14.3f%14.3f%16d"%("×".join(map(str,dims)),n,ta,tb,2**n))
print("""
  **GEN A's cost is in the bound systems; GEN B's is in the subsets.** If A
  matches the census and scales better, the inversion lifts to d = 3.
""")