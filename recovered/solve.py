import numpy as np, random
from itertools import product, permutations, combinations
random.seed(233)
print("="*88)
print("  A d-DIMENSIONAL CONDITION: CONSTRAINTS ON PATHS, NOT NODES")
print("="*88)
print("""
  Row B strictly inside row A touches A's end **iff every node on the tree
  path from A down to B sits at the corresponding end of its parent.**

     a NODE test is a projection — §13.4 forbids it
     **a PATH test is not** — it spans the structure

  Variables: L(v), R(v) for each node; side(A,B) for each containment.

     ¬L(u) ∨ ¬L(w)          siblings — at most one left child
     ¬R(u) ∨ ¬R(w)          siblings — at most one right child
     ¬L(v) ∨ ¬R(v)          unless v is an only child
     side(A,B) → L(v)       for every v on the path
     ¬side(A,B) → R(v)      likewise

  **Every clause has two literals. This is 2-SAT.**
""")
def overlap(a,b): return bool(a&b) and not(a<=b) and not(b<=a)
def comps(sets):
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
class Nd:
    _id=0
    def __init__(s,leaves,kids=None,typ='P'):
        s.leaves=frozenset(leaves); s.kids=kids or []; s.t=typ
        s.i=Nd._id; Nd._id+=1
def build(cols,rows):
    rows=[r for r in rows if r and r!=frozenset(cols)]
    if not rows: return Nd(cols,[Nd({c}) for c in sorted(cols)])
    kids=[]; cov=set()
    for cs in comps(rows):
        sub=[rows[i] for i in cs]
        u=frozenset().union(*sub); cov|=set(u)
        if len(sub)==1: kids.append(build(set(u),[r for r in rows if r<u]))
        else:
            inner=[r for r in rows if r<u]
            kids.append(Nd(u,[Nd({c}) for c in sorted(u)],'Q'))
    for c in sorted(set(cols)-cov): kids.append(Nd({c}))
    return Nd(cols,kids)
def twosat(clauses,nvar):
    g=[[] for _ in range(2*nvar)]; gr=[[] for _ in range(2*nvar)]
    lit=lambda v,s: 2*v+(0 if s else 1); neg=lambda l: l^1
    for (a,sa),(b,sb) in clauses:
        la,lb=lit(a,sa),lit(b,sb)
        g[neg(la)].append(lb); g[neg(lb)].append(la)
        gr[lb].append(neg(la)); gr[la].append(neg(lb))
    vis=[False]*(2*nvar); order=[]
    for s in range(2*nvar):
        if vis[s]: continue
        st=[(s,0)]; vis[s]=True
        while st:
            u,i=st.pop()
            if i<len(g[u]):
                st.append((u,i+1)); w=g[u][i]
                if not vis[w]: vis[w]=True; st.append((w,0))
            else: order.append(u)
    comp=[-1]*(2*nvar); c=0
    for u in reversed(order):
        if comp[u]!=-1: continue
        st=[u]; comp[u]=c
        while st:
            x=st.pop()
            for w in gr[x]:
                if comp[w]==-1: comp[w]=c; st.append(w)
        c+=1
    return all(comp[2*i]!=comp[2*i+1] for i in range(nvar))
def path_test(S):
    A=[sorted({x[i] for x in S}) for i in range(2)]
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    ROWS=sorted(set(sup.values()),key=lambda s:(-len(s),sorted(s)))
    Nd._id=0
    root=build(set(A[1]),list(sup.values()))
    nodes=[]; parent={}
    def walk(v,p):
        nodes.append(v); parent[v.i]=p
        for k in v.kids: walk(k,v)
    walk(root,None)
    bynode={}
    for v in nodes: bynode.setdefault(v.leaves,v)
    var={}; nv=0
    def V(k):
        nonlocal nv
        if k not in var: var[k]=nv; nv+=1
        return var[k]
    cl=[]
    for v in nodes:
        ks=v.kids
        for a,b in combinations(ks,2):
            cl.append(((V(('L',a.i)),False),(V(('L',b.i)),False)))
            cl.append(((V(('R',a.i)),False),(V(('R',b.i)),False)))
        if len(ks)>1:
            for k in ks:
                cl.append(((V(('L',k.i)),False),(V(('R',k.i)),False)))
    ok=True
    for Arow in ROWS:
        if Arow not in bynode: continue
        an=bynode[Arow]
        for Brow in ROWS:
            if Brow>=Arow or not (Brow<Arow): continue
            if Brow not in bynode: ok=False; break
            bn=bynode[Brow]
            path=[]; cur=bn
            while cur is not None and cur.i!=an.i:
                path.append(cur); cur=parent[cur.i]
            if cur is None: continue
            sv=V(('S',an.i,bn.i))
            for p in path:
                cl.append(((sv,False),(V(('L',p.i)),True)))
                cl.append(((sv,True),(V(('R',p.i)),True)))
        if not ok: break
    if not ok: return False
    return twosat(cl,nv)
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Rclosed(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    NN={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); NN[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=NN[c]}==S
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
def c1p(S):
    A=alpha(S); sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    for p in permutations(A[1]):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for r in A[0]:
            s=sorted(ic[c] for c in sup[r])
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok: return True
    return False
def gen_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%9s%9s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*54)
for lab in ("random","nested"):
    n=ag=fp=fn=0; ex=[]
    for _ in range(1500):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=gen_nested(random.randint(3,5))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        n+=1
        a=reorderable(S)
        try: b=c1p(S) and path_test(S)
        except Exception: continue
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    print("  %12s%9d%9d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:56]))