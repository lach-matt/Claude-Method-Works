import numpy as np, random
from itertools import product, permutations, combinations
random.seed(229)
print("="*88)
print("  §23.2's CLAIM, STATED SHARPLY")
print("="*88)
print("""
  'Fixing one PAIR of axes jointly and extending found a valid ordering in
  384 of 384.' **With unlimited backtracking that is exhaustive search and
  completeness is trivial.** The content must be the stronger claim:

  > **Once a pair of axes is fixed compatibly, the remaining axes always
  > extend — no revision of the fixed pair is ever needed.**

  **Test it: does a valid pair-fixing ever dead-end while another
  succeeds?**
""")
def is_closed(S,orders,d):
    idx=[{v:i for i,v in enumerate(o)} for o in orders]
    T={tuple(idx[k][x[k]] for k in range(d)) for x in S}
    A=[sorted({t[i] for t in T}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in T if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==T
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def pair_projection_ok(S,d,p0,p1,i,j):
    """is the (i,j) projection closed under the given orders?"""
    P={(x[i],x[j]) for x in S}
    return is_closed(P,[p0,p1],2)
def extends(S,d,fixed,axes_done,orders):
    """can the remaining axes be ordered to close the whole thing?"""
    rest=[k for k in range(d) if k not in axes_done]
    A=alph(S,d)
    if not rest:
        full=[None]*d
        for k,o in zip(axes_done,orders): full[k]=o
        return is_closed(S,full,d)
    k=rest[0]
    for p in permutations(A[k]):
        full=[None]*d
        for kk,o in zip(axes_done,orders): full[kk]=o
        full[k]=list(p)
        if extends(S,d,fixed,axes_done+[k],orders+[list(p)]): return True
    return False
print("  %6s%10s%16s%18s%16s"%("d","instances","reorderable","≥1 pair works","ALL valid pairs work"))
print("  "+"-"*70)
for d in (3,4):
    n=re=onep=allp=0; ex=[]
    for _ in range(1400):
        A=[list(range(random.randint(2,3))) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(1,len(cells))))
        Aa=alph(S,d)
        if any(len(a)<2 for a in Aa): continue
        # brute force reorderability
        ok=False
        for ps in product(*[list(permutations(a)) for a in Aa]):
            if is_closed(S,[list(p) for p in ps],d): ok=True; break
        if not ok: continue
        n+=1; re+=1
        # enumerate pair-fixings of axes 0,1 whose 2-D projection is closed
        valid=[]
        for p0 in permutations(Aa[0]):
            for p1 in permutations(Aa[1]):
                if pair_projection_ok(S,d,list(p0),list(p1),0,1):
                    valid.append((list(p0),list(p1)))
        if not valid: continue
        works=[v for v in valid if extends(S,d,v,[0,1],[v[0],v[1]])]
        if works: onep+=1
        if len(works)==len(valid): allp+=1
        elif len(ex)<3: ex.append((sorted(S),len(valid),len(works)))
    print("  %6d%10d%16d%18d%16d"%(d,n,re,onep,allp))
    for S,v,w in ex[:2]:
        print("        %d valid pairs, %d extend : %s"%(v,w,str(S)[:48]))
print("""
{0}
  WHAT THIS SETTLES
{0}
""".format("="*88))
print("""  **If 'ALL valid pairs work' equals the reorderable count, the strong
  claim holds: any compatible pair-fixing extends, and the heuristic needs
  no revision of its first choice.**

  **If it is smaller, the heuristic must try several pairs**, and §23.2's
  'fixing one pair' is a description of what happened to work rather than
  a property of the method.
""")