exec(open('/tmp/pq7.py').read().split('print("="*88)')[0])
import numpy as np, random
from itertools import product, permutations
random.seed(307)
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def true_c1p(S):
    A=alpha(S); sup=sup_of(S); out=set()
    for p in permutations(A[1]):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for r in A[0]:
            t=sorted(ic[c] for c in sup[r])
            if t!=list(range(t[0],t[0]+len(t))): ok=False; break
        if ok: out.add(p)
    return out
def anchors(S):
    A=alpha(S); sup=sup_of(S); ROWS=set(sup.values())
    root=build(set(A[1]),list(sup.values()))
    if root is None: return None,None
    nodes=[]
    def walk(v):
        nodes.append(v)
        for k in v.kids: walk(k)
    walk(root)
    res={}
    for r in ROWS:
        f=None
        for v in nodes:
            if v.leaves==r: f=('exact',); break
        if f is None:
            for v in nodes:
                if not v.kids or not (r<v.leaves): continue
                ks=v.kids
                for i in range(len(ks)):
                    acc=frozenset()
                    for j in range(i,len(ks)):
                        acc|=ks[j].leaves
                        if acc==r: f=('run',); break
                        if not (acc<r): break
                    if f: break
                if f: break
        res[r]=f
    return res,root
print("="*88)
print("  AFTER SPLITTING: DO ALL ROWS ANCHOR, AND ARE FRONTIERS STILL EXACT?")
print("="*88)
n=0; noanchor=0; kinds={'exact':0,'run':0}; fr_ok=0; fr_n=0
for _ in range(1500):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    am,root=anchors(S)
    if am is None: continue
    n+=1
    for r,v in am.items():
        if v is None: noanchor+=1
        else: kinds[v[0]]+=1
    if len(Aa[1])<=5:
        F=set(valid_frontiers(root,S)); T=true_c1p(S)
        fr_n+=1; fr_ok+= (F==T)
print("\n     instances                : %d"%n)
print("     anchors EXACT            : %d"%kinds['exact'])
print("     anchors as a RUN         : %d"%kinds['run'])
print("     **rows with NO anchor**  : %d"%noanchor)
print()
print("     frontier sets checked    : %d"%fr_n)
print("     **frontiers == C1P orders: %d  (%.1f%%)**"%(fr_ok,100*fr_ok/max(fr_n,1)))