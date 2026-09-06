import numpy as np, random, itertools
from itertools import product, permutations
random.seed(181)
print("="*88)
print("  THE REDUCTION THAT MAKES IT POLYNOMIAL")
print("="*88)
print("""
  **At a P-node, every row lies inside a single child** — a row spanning
  two children would make them overlap, and overlapping sets are collected
  into a Q-node by construction.

  **So at a P-node only the choice of leftmost and rightmost child matters**
  — k(k−1) options, not k!. At a Q-node the order is fixed up to reversal:
  2 options. **That is the whole search.**
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
def c1p_orders(cols,rows,cap=2000):
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
class Nd:
    __slots__=('t','leaves','kids','orders')
    def __init__(s,t,leaves,kids=None,orders=None):
        s.t=t; s.leaves=frozenset(leaves); s.kids=kids or []; s.orders=orders
def build(cols,rows):
    rows=[r for r in rows if r and r!=frozenset(cols)]
    if not rows: return Nd('P',cols,[Nd('L',{c}) for c in sorted(cols)])
    kids=[]; covered=set()
    for cs in components(rows):
        sub=[rows[i] for i in cs]
        u=frozenset().union(*sub); covered|=set(u)
        if len(sub)==1: kids.append(build(set(u),[r for r in rows if r<u]))
        else: kids.append(Nd('Q',u,orders=c1p_orders(set(u),sub)))
    for c in sorted(set(cols)-covered): kids.append(Nd('L',{c}))
    return Nd('P',cols,kids)
def decide(S):
    A=[sorted({x[i] for x in S}) for i in range(2)]
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    ROWS=sorted(set(sup.values()),key=lambda s:(-len(s),sorted(s)))
    root=build(set(A[1]),list(sup.values()))
    memo={}
    def solve(v,need):
        """need ⊆ {'L','R'} : ends of v that must be reachable by a row
           demanded from above.  returns True if v's subtree can be
           arranged with no strict nesting AND offering the needed ends."""
        key=(id(v),frozenset(need))
        if key in memo: return memo[key]
        ins=[r for r in ROWS if r < v.leaves]
        if v.t=='L':
            memo[key]=True; return True
        cand=[]
        if v.t=='Q':
            for o in (v.orders or []):
                cand.append([Nd('L',{c}) for c in o])
        else:
            k=len(v.kids)
            if k==1: cand.append(list(v.kids))
            else:
                for i in range(k):
                    for j in range(k):
                        if i==j: continue
                        mid=[v.kids[t] for t in range(k) if t!=i and t!=j]
                        cand.append([v.kids[i]]+mid+[v.kids[j]])
        res=False
        for seq in cand:
            # each row strictly inside v must touch an end of v
            okrows=True; needL=set(); needR=set()
            for r in ins:
                if r<=seq[0].leaves: needL.add(id(seq[0]))
                elif r<=seq[-1].leaves: needR.add(id(seq[-1]))
                else:
                    acc=frozenset(); hit=False
                    for kk in seq:
                        acc|=kk.leaves
                        if r<=acc and all(x.leaves<=r or not (x.leaves&r) for x in seq[:seq.index(kk)+1]):
                            hit=True; break
                        if not (kk.leaves<=r): break
                    if not hit:
                        acc=frozenset()
                        for kk in reversed(seq):
                            acc|=kk.leaves
                            if r<=acc: hit=True; break
                            if not (kk.leaves<=r): break
                    if not hit: okrows=False; break
            if not okrows: continue
            good=True
            for idx,kk in enumerate(seq):
                nd=set()
                if id(kk) in needL: nd.add('L')
                if id(kk) in needR: nd.add('R')
                if not solve(kk,nd): good=False; break
            if good: res=True; break
        memo[key]=res
        return res
    return solve(root,set())
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
def build_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%10s%10s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*56)
for lab in ("random","nested"):
    n=ag=fp=fn=0; ex=[]
    for _ in range(900):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=build_nested(random.randint(3,5))
        A=alpha(S)
        if len(A[0])<2 or len(A[1])<2: continue
        n+=1
        a=reorderable(S); b=decide(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    print("  %12s%10d%10d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:58]))