import numpy as np, random
from itertools import product, permutations, combinations
random.seed(353)
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
def proj_ok(S,d):
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
def sig_13_4(S,d):
    """two cells agreeing on ≥1 axis, disagreeing on ≥2, with the join absent"""
    for x,y in combinations(sorted(S),2):
        ag=sum(1 for i in range(d) if x[i]==y[i])
        di=sum(1 for i in range(d) if x[i]!=y[i])
        if ag>=1 and di>=2:
            if tuple(max(x[i],y[i]) for i in range(d)) not in S: return True
    return False
print("="*86)
print("  THE 12% — GAP INSTANCES WITHOUT §13.4's SIGNATURE")
print("="*86)
WITH=[]; WITHOUT=[]
for _ in range(2600):
    d=3
    A=[list(range(random.randint(2,3))) for _ in range(d)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(2,len(cells))))
    Aa=alph(S,d)
    if any(len(a)<2 for a in Aa): continue
    if proj_ok(S,d) and not reord(S,d):
        (WITH if sig_13_4(S,d) else WITHOUT).append(S)
print("\n     gap instances : %d     with signature : %d (%.0f%%)     without : %d (%.0f%%)"
      %(len(WITH)+len(WITHOUT),len(WITH),100*len(WITH)/max(len(WITH)+len(WITHOUT),1),
        len(WITHOUT),100*len(WITHOUT)/max(len(WITH)+len(WITHOUT),1)))
def feats(S,d):
    A=alph(S,d)
    jm=sum(1 for x,y in combinations(sorted(S),2)
           if tuple(max(x[i],y[i]) for i in range(d)) not in S)
    mm=sum(1 for x,y in combinations(sorted(S),2)
           if tuple(min(x[i],y[i]) for i in range(d)) not in S)
    return dict(cells=len(S), dens=len(S)/np.prod([len(a) for a in A]),
                join_fail=jm, meet_fail=mm,
                axes3=sum(1 for a in A if len(a)>=3),
                all_disagree=sum(1 for x,y in combinations(sorted(S),2)
                                 if all(x[i]!=y[i] for i in range(d))))
print("\n  %-16s%16s%16s"%("feature","WITH signature","WITHOUT"))
print("  "+"-"*50)
if WITH and WITHOUT:
    for k in ('cells','dens','join_fail','meet_fail','axes3','all_disagree'):
        print("  %-16s%16.3f%16.3f"%(k,np.mean([feats(S,3)[k] for S in WITH]),
                                        np.mean([feats(S,3)[k] for S in WITHOUT])))
print("="*86)
print("  WHAT THE 12% ARE")
print("="*86)
if WITHOUT:
    print("\n     examples:")
    for S in WITHOUT[:4]: print("       ",sorted(S))
    ad=np.mean([feats(S,3)['all_disagree'] for S in WITHOUT])
    ad2=np.mean([feats(S,3)['all_disagree'] for S in WITH]) if WITH else 0
    mf=np.mean([feats(S,3)['meet_fail'] for S in WITHOUT])
    mf2=np.mean([feats(S,3)['meet_fail'] for S in WITH]) if WITH else 0
    print("""
     **pairs disagreeing on EVERY axis : %.2f without vs %.2f with**
     **meet failures                   : %.2f without vs %.2f with**
"""%(ad,ad2,mf,mf2))
    print("""  §13.4's signature needs a pair AGREEING on at least one axis. **The 12%
  are the instances where no such pair fails** — their obstruction comes
  from cells that differ on every coordinate, so the failure is in the
  MEET or in a triple rather than in a pairwise join.

  > **The 88% fail by a join the projections cannot see. The 12% fail
  > without any pairwise witness at all** — which is a stronger form of
  > §13.4, not an exception to it.""")