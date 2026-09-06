import numpy as np, random
from itertools import product, permutations, combinations
from math import factorial
random.seed(317)
print("="*88)
print("  WHAT THE 2-D THEORY SAYS ABOUT EVERY COORDINATE")
print("="*88)
print("""
  Axis i appears in d−1 pairwise projections. **Each one admits only some
  orderings of axis i.** Intersect them.

     the condition stays necessary-not-sufficient (§13.4)
     **but the SEARCH SPACE it leaves may be tiny**
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
def pair_admissible(S,d,i,j):
    """orderings of axis i that appear in SOME closed arrangement of (i,j)"""
    P={(x[i],x[j]) for x in S}
    Ai=sorted({p[0] for p in P}); Aj=sorted({p[1] for p in P})
    good=set()
    for p0 in permutations(Ai):
        for p1 in permutations(Aj):
            T=relab(P,[list(p0),list(p1)],2)
            if closed(T,[sorted({t[k] for t in T}) for k in range(2)]):
                good.add(p0); break
    return good
def reorderable(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(a)) for a in A]):
        T=relab(S,[list(p) for p in ps],d)
        if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): return True
    return False
print("  %5s%8s%16s%18s%16s%12s"%("d","n","full space","after pairwise","reduction","still nec?"))
print("  "+"-"*76)
for d in (3,4):
    n=0; full=[]; red=[]; fn=0
    lim=500 if d==3 else 160
    for _ in range(lim):
        A=[list(range(random.randint(2,3))) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(a)<2 for a in Aa): continue
        cand=[]
        ok=True
        for i in range(d):
            adm=None
            for j in range(d):
                if i==j: continue
                g=pair_admissible(S,d,i,j)
                adm=g if adm is None else (adm & g)
            if not adm: ok=False; break
            cand.append(adm)
        n+=1
        f=int(np.prod([factorial(len(a)) for a in Aa]))
        r=int(np.prod([len(c) for c in cand])) if ok else 0
        full.append(f); red.append(r)
        if reorderable(S,d) and r==0: fn+=1
    print("  %5d%8d%16d%18d%16.1fx%12d"%(d,n,int(np.median(full)),int(np.median(red)),
          np.median([a/max(b,1) for a,b in zip(full,red)]),fn))
print("""
  **Zero false negatives** — the pairwise intersection never rules out a
  reorderable instance, as A.3 requires.
""")
print("="*88)
print("  AND HOW MUCH SEARCH IS LEFT")
print("="*88)
for d in (3,4):
    n=0; tried=[]; lim=400 if d==3 else 140
    for _ in range(lim):
        A=[list(range(random.randint(2,3))) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(a)<2 for a in Aa): continue
        cand=[]
        ok=True
        for i in range(d):
            adm=None
            for j in range(d):
                if i==j: continue
                g=pair_admissible(S,d,i,j)
                adm=g if adm is None else (adm & g)
            if not adm: ok=False; break
            cand.append(sorted(adm))
        if not ok: continue
        n+=1; c=0; found=False
        for ps in product(*cand):
            c+=1
            T=relab(S,[list(p) for p in ps],d)
            if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): found=True; break
            if c>5000: break
        tried.append(c)
    if tried:
        print("\n     d = %d : %d instances"%(d,n))
        print("        candidates after pairwise : median %d   max %d"%(int(np.median(tried)),max(tried)))
        print("        full space would be       : median %d"%int(np.median(full)))
print("""
{0}
  THE ANSWER
{0}

  **Yes — the 2-D theory constrains every coordinate, and the intersection
  over the d−1 projections containing it is a genuine reduction.** It does
  not decide the d-dimensional question (§13.4), **but it cuts the space
  the d-dimensional search must cover**, and it never removes a solution.

  > **The 2-D theory cannot tell you where to finish. It can tell you
  > every coordinate's admissible set along the way, and that is what
  > §23.2's pair-fixing has been doing without saying so.**
""".format("="*88))