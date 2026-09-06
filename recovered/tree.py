import numpy as np, random, itertools
from itertools import product, permutations, combinations

def overlap(a,b): return bool(a&b) and not(a<=b) and not(b<=a)

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
    return [[sets[i] for i in v] for v in g.values()]

class N:
    __slots__=('t','leaves','kids')
    def __init__(s,t,leaves,kids=None):
        s.t=t; s.leaves=frozenset(leaves); s.kids=kids or []

def partition_atoms(U,touching):
    """AXIS 1 — the PARTITION: refined by every set touching U, so no row
       can cut through an atom."""
    sig={}
    for c in sorted(U):
        k=frozenset(i for i,s in enumerate(touching) if c in s)
        sig.setdefault(k,[]).append(c)
    return [frozenset(v) for v in sig.values()]

def admissible_orders(atoms,comp,cap=400):
    """AXIS 2 — the ORDER CONSTRAINT: only the COMPONENT's sets must be
       consecutive.  Inner sets constrain the partition, not the order."""
    out=[]
    for p in permutations(range(len(atoms))):
        pos={}
        for idx,i in enumerate(p):
            for c in atoms[i]: pos[c]=idx
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
    sets=list({frozenset(s) for s in sets if s and frozenset(s)!=cols})
    if not sets:
        return N('P',cols,[N('L',{c}) for c in sorted(cols)])
    maximal=[s for s in sets if not any(s<t for t in sets)]
    rest=[s for s in sets if s not in maximal]
    kids=[]; covered=set()
    for comp in components(maximal):
        U=frozenset().union(*comp); covered|=set(U)
        inner=[s for s in rest if s<U]
        if len(comp)==1:
            kids.append(build(U,inner))
        else:
            touching=list(comp)+[s for s in inner if s&U]
            atoms=partition_atoms(U,touching)
            ords=admissible_orders(atoms,comp)
            if not ords: return None
            order=ords[0]
            ch=[]
            for a in order:
                ch.append(build(a,[s for s in inner if s<a]))
            if any(c is None for c in ch): return None
            kids.append(N('Q',U,ch))
    for c in sorted(set(cols)-covered): kids.append(N('L',{c}))
    return N('P',cols,kids)

def frontiers(v,cap=200000):
    if v.t=='L' or not v.kids: return [tuple(sorted(v.leaves))]
    ks=[frontiers(k,cap) for k in v.kids]
    out=[]
    if v.t=='P':
        for perm in permutations(range(len(ks))):
            for combo in product(*[ks[i] for i in perm]):
                out.append(tuple(itertools.chain(*combo)))
                if len(out)>=cap: return out
    else:
        for combo in product(*ks):
            f=tuple(itertools.chain(*combo)); out.append(f); out.append(f[::-1])
            if len(out)>=cap: return out
    return out

def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def valid_frontiers(root,S):
    A=alpha(S); sup=sup_of(S); out=[]
    for f in frontiers(root):
        ic={c:i for i,c in enumerate(f)}
        ok=True
        for r in A[0]:
            t=sorted(ic[c] for c in sup[r])
            if t!=list(range(t[0],t[0]+len(t))): ok=False; break
        if ok: out.append(f)
    return out
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
def anchor(S):
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
            if v.leaves==r: f='exact'; break
        if f is None:
            for v in nodes:
                if not v.kids or not (r<v.leaves): continue
                ks=v.kids
                for i in range(len(ks)):
                    acc=frozenset()
                    for j in range(i,len(ks)):
                        acc|=ks[j].leaves
                        if acc==r: f='run'; break
                        if not (acc<r): break
                    if f: break
                if f: break
        res[r]=f
    return res,root

if __name__=="__main__":
    random.seed(311)
    print("="*88)
    print("  THE TREE REBUILT — TWO AXES SEPARATED")
    print("="*88)
    print("""
     PARTITION  refined by every set touching U   -> rows cannot cut atoms
     ORDER      constrained by the COMPONENT only -> no order is lost
""")
    print("  %8s%9s%16s%14s%12s%12s"%("cols","n","frontiers==C1P","no anchor","exact","run"))
    print("  "+"-"*72)
    for nc in (3,4,5):
        n=fr=na=ex=ru=0
        for _ in range(800):
            A=[list(range(random.randint(2,4))),list(range(nc))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
            Aa=alpha(S)
            if len(Aa[0])<2 or len(Aa[1])<2: continue
            am,root=anchor(S)
            if am is None: continue
            n+=1
            fr+= (set(valid_frontiers(root,S))==true_c1p(S))
            for r,v in am.items():
                if v is None: na+=1
                elif v=='exact': ex+=1
                else: ru+=1
        print("  %8d%9d%16d%14d%12d%12d"%(nc,n,fr,na,ex,ru))