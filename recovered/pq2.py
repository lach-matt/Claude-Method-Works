import numpy as np, random, itertools
from itertools import product, permutations
random.seed(167)
print("="*88)
print("  THE Q-NODE MUST COMPUTE ITS ORDER, NOT ASSUME IT")
print("="*88)
print("""
  X = {(0,0),(0,1),(1,0),(1,2)} has rows {0,1} and {0,2}, which OVERLAP.
  The valid column order is (1,0,2) — 0 in the middle. **My Q-node used
  sorted order (0,1,2) and its reversal, and missed it.**  CORRECTION 140.
""")
def overlap(a,b): return bool(a&b) and not (a<=b) and not (b<=a)
def components(sets):
    n=len(sets); par=list(range(n))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for i in range(n):
        for j in range(i+1,n):
            if overlap(sets[i],sets[j]):
                a,b=f(i),f(j)
                if a!=b: par[a]=b
    g={}
    for i in range(n): g.setdefault(f(i),[]).append(i)
    return list(g.values())
def c1p_orders(cols,rows,cap=400):
    out=[]
    for p in permutations(sorted(cols)):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for rw in rows:
            s=sorted(ic[c] for c in rw)
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok:
            out.append(p)
            if len(out)>=cap: break
    return out
class N:
    def __init__(s,t,leaves,kids=None,orders=None):
        s.t=t; s.leaves=leaves; s.kids=kids or []; s.orders=orders
def build(cols,rows):
    rows=[r for r in rows if r and r!=frozenset(cols)]
    if not rows:
        return N('P',set(cols),[N('L',{c}) for c in sorted(cols)])
    comp=components(rows)
    kids=[]; covered=set()
    for cs in comp:
        sub=[rows[i] for i in cs]
        u=frozenset().union(*sub); covered|=set(u)
        if len(sub)==1:
            inner=[r for r in rows if r<u]
            kids.append(build(set(u),inner))
        else:
            # a genuine Q-node: compute its admissible orders
            ords=c1p_orders(set(u),sub)
            kids.append(N('Q',set(u),orders=ords))
    for c in sorted(set(cols)-covered): kids.append(N('L',{c}))
    return N('P',set(cols),kids)
def frontiers(node,cap=4000):
    if node.t=='L': return [tuple(node.leaves)]
    if node.t=='Q': return [tuple(o) for o in (node.orders or [])][:cap]
    kid=[frontiers(k,cap) for k in node.kids]
    out=[]
    for perm in permutations(range(len(kid))):
        for combo in product(*[kid[i] for i in perm]):
            out.append(tuple(itertools.chain(*combo)))
            if len(out)>=cap: return out
    return out
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Rclosed(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N2={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); N2[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=N2[c]}==S
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
def nostrict(sp): return not any(a<c and d<b for (a,b) in sp for (c,d) in sp)
def tree_test(S):
    A=alpha(S); sup=sup_of(S)
    root=build(set(A[1]),list(sup.values()))
    for f in frontiers(root):
        ic={v:i for i,v in enumerate(f)}
        sp=[]; ok=True
        for r in A[0]:
            s=sorted(ic[c] for c in sup[r])
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
            sp.append((s[0],s[-1]))
        if ok and nostrict(sp): return True
    return False
X={(0,0),(0,1),(1,0),(1,2)}
print("     the counterexample: tree_test =",tree_test(X),"  reorderable =",reorderable(X))
print("="*88)
print("  FULL TEST")
print("="*88)
def build_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("\n  %12s%10s%10s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*56)
for lab in ("random","nested"):
    n=ag=fp=fn=0; ex=[]
    for _ in range(1500):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=build_nested(random.randint(3,5))
        A=alpha(S)
        if len(A[0])<2 or len(A[1])<2: continue
        n+=1
        a=reorderable(S); b=tree_test(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    print("  %12s%10d%10d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:60]))