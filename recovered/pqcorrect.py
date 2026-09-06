import numpy as np, random, itertools
from itertools import product, permutations, combinations
random.seed(277)
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
    return [ [sets[i] for i in v] for v in g.values() ]
class N:
    def __init__(s,t,leaves,kids):
        s.t=t; s.leaves=frozenset(leaves); s.kids=kids
def atoms_of(U,comp):
    """columns grouped by which sets of comp contain them"""
    sig={}
    for c in U:
        k=frozenset(i for i,s in enumerate(comp) if c in s)
        sig.setdefault(k,set()).add(c)
    return [frozenset(v) for v in sig.values()]
def atom_orders(atoms,comp,cap=200):
    """orders of atoms making every set of comp consecutive"""
    out=[]
    for p in permutations(range(len(atoms))):
        pos={}
        idx=0
        for i in p:
            for c in atoms[i]: pos[c]=idx
            idx+=1
        ok=True
        for s in comp:
            ix=sorted({pos[c] for c in s})
            if ix!=list(range(ix[0],ix[0]+len(ix))): ok=False; break
        if ok:
            out.append([atoms[i] for i in p])
            if len(out)>=cap: break
    return out
def build(cols,sets):
    cols=frozenset(cols)
    sets=[frozenset(s) for s in sets if s and frozenset(s)!=cols]
    sets=list({s for s in sets})
    if not sets:
        return N('P',cols,[N('L',{c},[]) for c in sorted(cols)])
    kids=[]; covered=set()
    for comp in comps(sets):
        U=frozenset().union(*comp); covered|=set(U)
        inner=[s for s in sets if s<U and s not in comp]
        if len(comp)==1:
            kids.append(build(U,inner))
        else:
            at=atoms_of(U,comp)
            ords=atom_orders(at,comp)
            if not ords:
                return None
            order=ords[0]
            ch=[build(a,[s for s in inner if s<=a and s!=a]) for a in order]
            if any(c is None for c in ch): return None
            kids.append(N('Q',U,ch))
    for c in sorted(set(cols)-covered): kids.append(N('L',{c},[]))
    return N('P',cols,kids)
def frontiers(v,cap=200000):
    if v.t=='L': return [tuple(v.leaves)]
    ks=[frontiers(k,cap) for k in v.kids]
    out=[]
    if v.t=='P':
        for perm in permutations(range(len(ks))):
            for combo in product(*[ks[i] for i in perm]):
                out.append(tuple(itertools.chain(*combo)))
                if len(out)>=cap: return out
    else:
        for combo in product(*ks):
            f=tuple(itertools.chain(*combo)); out.append(f)
            out.append(f[::-1])
            if len(out)>=cap: return out
    return out
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def true_c1p_orders(S):
    A=alpha(S); sup=sup_of(S); out=set()
    for p in permutations(A[1]):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for r in A[0]:
            s=sorted(ic[c] for c in sup[r])
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok: out.add(p)
    return out
print("="*88)
print("  VERIFY THE TREE: ITS FRONTIERS MUST BE EXACTLY THE C1P ORDERS")
print("="*88)
print("  %10s%10s%14s%14s%12s"%("size","n","exact match","tree misses","tree extra"))
print("  "+"-"*62)
for sz in (3,4,5):
    n=ok=miss=extra=0
    ex=None
    for _ in range(700):
        A=[list(range(random.randint(2,4))),list(range(sz))]
        cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        T=true_c1p_orders(S)
        root=build(set(Aa[1]),list(sup_of(S).values()))
        F=set(frontiers(root)) if root is not None else set()
        n+=1
        if F==T: ok+=1
        else:
            if T-F: miss+=1
            if F-T: extra+=1
            if ex is None and (T-F): ex=(sorted(S),sorted(T-F)[:2],sorted(F-T)[:2])
    print("  %10d%10d%14d%14d%12d"%(sz,n,ok,miss,extra))
    if ex: print("        e.g. %s"%str(ex[0])[:56]); print("             missing %s"%str(ex[1])[:52])