exec(open('/tmp/pq6.py').read().split('print("="*88)')[0])
import numpy as np, random, itertools
from itertools import product, permutations, combinations
random.seed(281)
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Ev(S,o):
    T=relabel(S,o); A=[sorted({t[i] for t in T}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    Nn={};run=-1
    for w in A[1]:
        c=[x for (x,y) in T if y<=w]; run=max(run,max(c) if c else -1); Nn[w]=run
    return sum(1 for r in A[0] for c in A[1] if c<=M[r] and r<=Nn[c])-len(T)
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Ev(S,[list(p0),list(p1)])==0: return True
    return False
def nostrict(sp): return not any(a<c and d<b for (a,b) in sp for (c,d) in sp)
print("="*88)
print("  CLAIM: ON A CORRECT TREE, NO ROW SPANS TWO P-NODE CHILDREN")
print("="*88)
def check_span(S):
    A=alpha(S); sup=sup_of(S)
    root=build(set(A[1]),list(sup.values()))
    if root is None: return None
    bad=0
    def walk(v):
        nonlocal bad
        if v.t=='P' and len(v.kids)>1:
            for r in sup.values():
                if r<=v.leaves and r!=v.leaves:
                    hit=[k for k in v.kids if r&k.leaves]
                    if len(hit)>1: bad+=1
        for k in v.kids: walk(k)
    walk(root)
    return bad
n=0; tot=0
for _ in range(1500):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    b=check_span(S)
    if b is None: continue
    n+=1; tot+=b
print("\n     instances : %d     rows spanning >1 P-child : %d"%(n,tot))
print("     **claim holds : %s**"%(tot==0))
print("="*88)
print("  THE REDUCED SEARCH")
print("="*88)
print("""
  P-node with k children : choose which is LEFTMOST and which RIGHTMOST
                           -> k(k−1) options, not k!
  Q-node                 : forward or reversed -> 2 options
""")
def frontiers_reduced(v,cap=200000):
    if v.t=='L': return [tuple(v.leaves)]
    ks=[frontiers_reduced(k,cap) for k in v.kids]
    out=[]
    if v.t=='P':
        k=len(ks)
        if k==1:
            return ks[0]
        for i in range(k):
            for j in range(k):
                if i==j: continue
                mid=[t for t in range(k) if t!=i and t!=j]
                for combo in product(*[ks[t] for t in [i]+mid+[j]]):
                    out.append(tuple(itertools.chain(*combo)))
                    if len(out)>=cap: return out
    else:
        for combo in product(*ks):
            f=tuple(itertools.chain(*combo)); out.append(f); out.append(f[::-1])
            if len(out)>=cap: return out
    return out
def decide_reduced(S):
    A=alpha(S); sup=sup_of(S)
    root=build(set(A[1]),list(sup.values()))
    if root is None: return False,0
    tried=0
    for f in frontiers_reduced(root):
        ic={c:i for i,c in enumerate(f)}
        sp=[]; ok=True
        for r in A[0]:
            t=sorted(ic[c] for c in sup[r])
            if t!=list(range(t[0],t[0]+len(t))): ok=False; break
            sp.append((t[0],t[-1]))
        tried+=1
        if ok and nostrict(sp): return True,tried
    return False,tried
def decide_full(S):
    A=alpha(S); sup=sup_of(S)
    root=build(set(A[1]),list(sup.values()))
    if root is None: return False
    for f in valid_frontiers(root,S):
        ic={c:i for i,c in enumerate(f)}
        sp=[(lambda t:(t[0],t[-1]))(sorted(ic[c] for c in sup[r])) for r in A[0]]
        if nostrict(sp): return True
    return False
def gen_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%9s%9s%12s%12s%14s"%("source","n","agree","false pos","false neg","median tried"))
print("  "+"-"*70)
TF=0
for lab in ("random","nested"):
    n=ag=fp=fn=0; tr=[]
    for _ in range(1200):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=gen_nested(random.randint(3,5))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        n+=1
        a=reorderable(S); b,t=decide_reduced(S); tr.append(t)
        ag+=(a==b)
        if b and not a: fp+=1
        if a and not b: fn+=1
    TF+=fp+fn
    print("  %12s%9d%9d%12d%12d%14d"%(lab,n,ag,fp,fn,int(np.median(tr))))
print("\n  **%s**"%("EXACT" if TF==0 else "%d errors"%TF))