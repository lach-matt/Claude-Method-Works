import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(443)
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord(S,d,cap=10**6):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
print("="*88)
print("  A GRAMMAR OF REORDERABLE INDICES")
print("="*88)
print("""
  Four rules already measured: sublattice, interval, product, fibration.
  **Test the rest of the natural constructions.**
""")
def gen_reord(d,a,tries=200):
    for _ in range(tries):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        if reord(S,d) is True: return S,d
    return None,None
RES={}
# 1. PROJECTION — delete an axis
n=ok=0
for _ in range(300):
    S,d=gen_reord(3,2)
    if S is None: continue
    i=random.randrange(d)
    P={tuple(x[k] for k in range(d) if k!=i) for x in S}
    Ap=alph(P,d-1)
    if any(len(z)<2 for z in Ap): continue
    n+=1; r=reord(P,d-1); ok+= (r is True)
RES['projection (delete an axis)']=(ok,n)
# 2. ADD A FREE AXIS
n=ok=0
for _ in range(300):
    S,d=gen_reord(2,3)
    if S is None: continue
    vals=list(range(random.randint(2,3)))
    P={tuple(list(x)+[v]) for x in S for v in vals}
    n+=1; r=reord(P,d+1); ok+= (r is True)
RES['add a free axis (full)']=(ok,n)
# 3. DISJOINT UNION on a new axis
n=ok=0
for _ in range(250):
    S1,d=gen_reord(2,3)
    S2,_=gen_reord(2,3)
    if S1 is None or S2 is None: continue
    P={tuple(list(x)+[0]) for x in S1} | {tuple(list(y)+[1]) for y in S2}
    n+=1; r=reord(P,d+1); ok+= (r is True)
RES['disjoint union on a new axis']=(ok,n)
# 4. DUAL — reverse every axis
n=ok=0
for _ in range(300):
    S,d=gen_reord(3,2)
    if S is None: continue
    A=alph(S,d)
    rev=[list(reversed(a)) for a in A]
    P=relab(S,rev,d)
    n+=1; r=reord(P,d); ok+= (r is True)
RES['dual (reverse every axis)']=(ok,n)
# 5. QUOTIENT — merge two values on one axis
n=ok=0
for _ in range(300):
    S,d=gen_reord(3,3)
    if S is None: continue
    A=alph(S,d); i=random.randrange(d)
    if len(A[i])<3: continue
    u,v=random.sample(A[i],2)
    P={tuple(u if (k==i and x[k]==v) else x[k] for k in range(d)) for x in S}
    Ap=alph(P,d)
    if any(len(z)<2 for z in Ap): continue
    n+=1; r=reord(P,d); ok+= (r is True)
RES['quotient (merge two values)']=(ok,n)
# 6. SUBLATTICE (re-measure at this d)
n=ok=0
for _ in range(300):
    S,d=gen_reord(3,3)
    if S is None: continue
    cur=set(random.sample(sorted(S),min(3,len(S))))
    while True:
        new=set(cur)
        for x,y in combinations(sorted(cur),2):
            new.add(tuple(max(x[i],y[i]) for i in range(d)))
            new.add(tuple(min(x[i],y[i]) for i in range(d)))
        new&=set(S)
        if new==cur: break
        cur=new
    Ap=alph(cur,d)
    if any(len(z)<2 for z in Ap): continue
    n+=1; r=reord(cur,d); ok+= (r is True)
RES['sublattice']=(ok,n)
print("  %-34s%10s%10s%12s"%("construction","n","preserved","rate"))
print("  "+"-"*66)
for k,(o,t) in RES.items():
    print("  %-34s%10d%10d%12s"%(k,t,o,("%.0f%%"%(100*o/t)) if t else "—"))
print("""
{0}
  THE GRAMMAR
{0}
""".format("="*88))
keep=[k for k,(o,t) in RES.items() if t and o==t]
lose=[k for k,(o,t) in RES.items() if t and o<t]
print("     **PRESERVE reorderability:**")
for k in keep: print("        · %s"%k)
print("\n     **DO NOT:**")
for k in lose: print("        · %s   (%d of %d)"%(k,RES[k][0],RES[k][1]))
print("""
  **A construction grammar is a CERTIFICATE.** An index built only from
  preserving rules is reorderable without any decision procedure — which is
  how Λ qualifies, and why §23.4's general question is not load-bearing.
""")