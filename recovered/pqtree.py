import numpy as np, random, itertools
from itertools import product, permutations, combinations
random.seed(163)
print("="*88)
print("  BUILDING THE PQ-TREE VIA OVERLAP COMPONENTS")
print("="*88)
print("""
  **Structure theorem.** Two row-sets either are disjoint, nested, or
  properly OVERLAP. Overlapping sets constrain each other rigidly; the
  connected components of the overlap graph are **Q-nodes** — order forced
  up to reversal. Everything else is free — **P-nodes**.

  Verify the rigidity claim first: a non-trivial overlap component should
  admit exactly TWO column orders.
""")
def overlap(a,b):
    return (a&b) and not (a<=b) and not (b<=a)
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
def c1p_orders_of(cols,rows):
    """all orders of cols making every row consecutive"""
    out=[]
    for p in permutations(sorted(cols)):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for rw in rows:
            s=sorted(ic[c] for c in rw)
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok: out.append(p)
    return out
print("  %10s%12s%14s%16s"%("comp size","instances","median orders","=2 (rigid)"))
print("  "+"-"*54)
for k in (2,3):
    cnt=[]; rig=0; n=0
    for _ in range(400):
        nc=random.randint(3,5)
        rows=[]
        for _ in range(k):
            a=random.randint(0,nc-1); b=random.randint(a,nc-1)
            rows.append(frozenset(range(a,b+1)))
        comp=components(rows)
        big=[c for c in comp if len(c)>1]
        if not big: continue
        cs=big[0]; sub=[rows[i] for i in cs]
        cols=set().union(*sub)
        o=c1p_orders_of(cols,sub)
        if not o: continue
        n+=1; cnt.append(len(o)); rig+= (len(o)==2)
    if n: print("  %10d%12d%14d%16s"%(k,n,int(np.median(cnt)),"%d/%d"%(rig,n)))
print("""
  **Rigidity is only up to the columns the component does not pin down.**
  A component fixes the order of the columns it OVERLAPS on; free columns
  inside a row remain permutable, which is why the count exceeds two.

  **So build the tree properly instead: recursive containment + overlap.**
""")
print("="*88)
print("  THE TREE, AND THE TRAVERSAL")
print("="*88)
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
class Node:
    def __init__(self,typ,leaves,kids): self.typ=typ; self.leaves=leaves; self.kids=kids
def build(cols,rows):
    """cols: set of columns; rows: list of frozensets, all ⊆ cols"""
    rows=[r for r in rows if r and r!=cols]
    if not rows:
        return Node('P',set(cols),[Node('L',{c},[]) for c in sorted(cols)])
    comp=components(rows)
    blocks=[]
    for cs in comp:
        sub=[rows[i] for i in cs]
        u=set().union(*sub)
        blocks.append((u,sub))
    covered=set().union(*[u for u,_ in blocks]) if blocks else set()
    kids=[]
    for u,sub in blocks:
        if len(sub)==1:
            inner=[r for r in rows if r<u and r!=u]
            kids.append(build(u,inner))
        else:
            kids.append(Node('Q',set(u),[Node('L',{c},[]) for c in sorted(u)]))
    for c in sorted(set(cols)-covered): kids.append(Node('L',{c},[]))
    return Node('P',set(cols),kids)
def frontiers(node,cap=5000):
    if node.typ=='L': return [tuple(node.leaves)]
    kid=[frontiers(k,cap) for k in node.kids]
    out=[]
    if node.typ=='P':
        for perm in permutations(range(len(kid))):
            for combo in product(*[kid[i] for i in perm]):
                out.append(tuple(itertools.chain(*combo)))
                if len(out)>cap: return out
    else:
        for combo in product(*kid):
            f=tuple(itertools.chain(*combo)); out.append(f); out.append(f[::-1])
            if len(out)>cap: return out
    return out
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Rclosed(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=N[c]}==S
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
print("\n  %12s%10s%10s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*56)
def build_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
for lab in ("random","nested"):
    n=ag=fp=fn=0; ex=[]
    for _ in range(1200):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
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