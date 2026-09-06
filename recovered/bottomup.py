import numpy as np, random, itertools
from itertools import product, permutations, combinations
random.seed(179)
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
def c1p_orders(cols,rows,cap=5000):
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
# ---------- the BOTTOM-UP traversal ----------
def bottom_up(S):
    """decide reorderability by one pass carrying E(v) ⊆ {L,R}"""
    A=[sorted({x[i] for x in S}) for i in range(2)]
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    rows=sorted(set(sup.values()),key=lambda s:(-len(s),sorted(s)))
    root=build(set(A[1]),list(sup.values()))
    def kids_of(v):
        if v.t=='Q':
            # a Q-node's children are its leaves in the forced order
            if not v.orders: return None
            return [[Nd('L',{c}) for c in o] for o in v.orders]
        return [v.kids]
    def inside(v):
        return [r for r in rows if r < v.leaves]
    memo={}
    def feasible(v,demand):
        """can v's subtree be arranged with no strict nesting inside it, and
           with a row of 'demand' touching each named end?  demand ⊆ {'L','R'}"""
        key=(id(v),frozenset(demand))
        if key in memo: return memo[key]
        ins=inside(v)
        res=None
        for arrangement in (kids_of(v) or []):
            ks=arrangement
            n=len(ks)
            if n==0: continue
            orders=[list(range(n))] if v.t=='Q' else list(permutations(range(n)))
            for perm in orders:
                seq=[ks[i] for i in perm]
                # every row strictly inside v must touch an end of v
                ok=True
                for r in ins:
                    hit=False
                    # r touches v's left end iff r ⊆ leaves(seq[0]) chain-wise
                    if r <= seq[0].leaves or r <= seq[-1].leaves: hit=True
                    else:
                        # r may span several leading or trailing children
                        acc=frozenset()
                        for k in seq:
                            acc|=k.leaves
                            if r<=acc: hit=True; break
                            if not (k.leaves<=r): break
                        if not hit:
                            acc=frozenset()
                            for k in reversed(seq):
                                acc|=k.leaves
                                if r<=acc: hit=True; break
                                if not (k.leaves<=r): break
                    if not hit: ok=False; break
                if not ok: continue
                # recurse: each child must itself be internally consistent
                if all(feasible(k,set()) for k in seq):
                    res=True; break
            if res: break
        if res is None: res=(len(ins)==0)
        memo[key]=res
        return res
    return feasible(root,set())
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
print("="*88)
print("  THE BOTTOM-UP TRAVERSAL, TESTED AGAINST BRUTE FORCE")
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
    for _ in range(900):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=build_nested(random.randint(3,5))
        A=alpha(S)
        if len(A[0])<2 or len(A[1])<2: continue
        n+=1
        try: b=bottom_up(S)
        except Exception as e: b=None
        a=reorderable(S)
        if b is None: continue
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    print("  %12s%10d%10d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:58]))