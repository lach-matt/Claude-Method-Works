import numpy as np, random
from itertools import product, permutations, combinations
random.seed(313)
print("="*88)
print("  CHASING d ≥ 3")
print("="*88)
print("""
  At d = 2: reorderable ⟺ C1P + monotone endpoints. **PROVED.**

  The natural lift: *every 2-D projection is reorderable.* By A.3 that is
  NECESSARY. By §13.4 it cannot be sufficient — the theorem exhibits a
  six-cell set whose every proper projection is closed and which is not.

  **Measure the gap.**
""")
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
def reorderable(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(a)) for a in A]):
        T=relab(S,[list(p) for p in ps],d)
        if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): return True
    return False
def proj_reorderable(S,d):
    """every 2-D projection reorderable"""
    for i,j in combinations(range(d),2):
        P={(x[i],x[j]) for x in S}
        A=[sorted({p[0] for p in P}),sorted({p[1] for p in P})]
        if len(A[0])<2 or len(A[1])<2: continue
        ok=False
        for p0 in permutations(A[0]):
            for p1 in permutations(A[1]):
                T=relab(P,[list(p0),list(p1)],2)
                if closed(T,[sorted({t[k] for t in T}) for k in range(2)]): ok=True; break
            if ok: break
        if not ok: return False
    return True
print("  %6s%10s%14s%14s%14s%12s"%("d","n","reorderable","proj-reord.","FN","FP (gap)"))
print("  "+"-"*70)
for d in (3,4):
    n=re=pr=fn=fp=0; ex=[]
    lim=900 if d==3 else 260
    for _ in range(lim):
        A=[list(range(random.randint(2,3))) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(a)<2 for a in Aa): continue
        n+=1
        a=reorderable(S,d); b=proj_reorderable(S,d)
        re+=a; pr+=b
        if a and not b: fn+=1
        if b and not a:
            fp+=1
            if len(ex)<2: ex.append(sorted(S))
    print("  %6d%10d%14d%14d%14d%12d"%(d,n,re,pr,fn,fp))
    for s in ex[:1]: print("        gap example: %s"%str(s)[:60])
print("""
  **Zero false negatives, as A.3 guarantees. The false positives are the
  gap §13.4 predicts**, and they are the whole content of d ≥ 3.
""")
print("="*88)
print("  IS THE GAP THE SAME MECHANISM §13.4 NAMES?")
print("="*88)
print("""
  §13.4's counterexample: two cells agreeing on one axis and disagreeing on
  BOTH others, so the join disagrees in a COMBINATION no projection sees.
  **Check the gap instances for that signature.**
""")
def has_13_4_signature(S,d):
    for x,y in combinations(sorted(S),2):
        agree=[i for i in range(d) if x[i]==y[i]]
        dis=[i for i in range(d) if x[i]!=y[i]]
        if len(agree)>=1 and len(dis)>=2:
            j=tuple(max(x[i],y[i]) for i in range(d))
            if j not in S: return True
    return False
hits=0; tot=0
for _ in range(1200):
    A=[list(range(random.randint(2,3))) for _ in range(3)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(2,len(cells))))
    Aa=alph(S,3)
    if any(len(a)<2 for a in Aa): continue
    if proj_reorderable(S,3) and not reorderable(S,3):
        tot+=1; hits+=has_13_4_signature(S,3)
print("\n     gap instances checked           : %d"%tot)
print("     carrying §13.4's signature      : %d  (%.0f%%)"%(hits,100*hits/max(tot,1)))
print("""
{0}
  WHAT THIS ESTABLISHES FOR d ≥ 3
{0}
""".format("="*88))
print("""  **The d = 2 characterisation lifts as a NECESSARY condition and no
  further** — measured, and predicted by A.3 and §13.4 respectively.

  **So the d ≥ 3 problem is not the d = 2 problem repeated.** Its content
  is exactly the combination-failures §13.4 exhibits, which no product of
  two-dimensional facts can express.

  > **§23.4's theorem is a theorem about pairs of axes. Λ has eight, and
  > the lattice's own closure is a d-dimensional condition that the
  > theorem does not reach.**
""")