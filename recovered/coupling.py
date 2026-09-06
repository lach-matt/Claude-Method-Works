import numpy as np, random
from itertools import product, permutations, combinations
random.seed(241)
print("="*88)
print("  IS THE FAILURE A COUPLING FAILURE?")
print("="*88)
print("""
  §6.5: [g ≤ min(q,4f+2)] = [g ≤ q]·[g ≤ 4f+2] — **two conditions on ONE
  variable.** Testing them separately loses the coupling.

  Here: **C1P chooses a column order. The 2-SAT chooses end assignments.
  They must be the SAME arrangement.** I test them independently.

  **DIAGNOSTIC.** For each false positive, check whether some SINGLE column
  order satisfies both — i.e. whether the two conditions are jointly
  satisfiable rather than merely separately.
""")
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
def c1p_orders(S):
    A=alpha(S); sup=sup_of(S); out=[]
    for p in permutations(A[1]):
        ic={v:i for i,v in enumerate(p)}
        sp={}; ok=True
        for r in A[0]:
            s=sorted(ic[c] for c in sup[r])
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
            sp[r]=(s[0],s[-1])
        if ok: out.append((p,sp))
    return out
def nostrict(sp): return not any(a<c and d<b for (a,b) in sp for (c,d) in sp)
def ends_ok_for_order(S,sp):
    """given a C1P order, does every strictly-contained row touch an end?"""
    rows=sorted(set(sup_of(S).values()),key=lambda s:(-len(s),sorted(s)))
    spans={}
    for r,v in sup_of(S).items(): spans[frozenset(v)]=sp[r]
    for A in rows:
        la,ha=spans[A]
        for B in rows:
            if not (B<A): continue
            lb,hb=spans[B]
            if la<lb and hb<ha: return False
    return True
def sep_test(S):
    """the separated test: C1P anywhere, ends-OK anywhere"""
    O=c1p_orders(S)
    if not O: return False
    return any(ends_ok_for_order(S,sp) for _,sp in O)
def joint_test(S):
    """the JOINT test: one order doing both"""
    for p,sp in c1p_orders(S):
        if nostrict(list(sp.values())): return True
    return False
def gen_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%9s%16s%16s"%("source","n","separated agrees","JOINT agrees"))
print("  "+"-"*56)
for lab in ("random","nested"):
    n=s_ag=j_ag=0
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
        s_ag+= (a==sep_test(S))
        j_ag+= (a==joint_test(S))
    print("  %12s%9d%16d%16d"%(lab,n,s_ag,j_ag))
print("""
{0}
  THE DIAGNOSIS
{0}
""".format("="*88))
print("""  **If the JOINT test is exact and the separated one is not, the failure
  is a coupling failure**, and the nine conditions failed because each
  tested a factor rather than the product.

  **That is §6.5's lesson exactly: min(a,b) = [≤a]·[≤b] is a PRODUCT, and
  evaluating the factors independently is not evaluating the product.**
""")