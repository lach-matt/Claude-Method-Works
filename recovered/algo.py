import random, time
from itertools import product, permutations, combinations
random.seed(647)
print("="*88)
print("  THE ALGORITHM, DEFINED")
print("="*88)
print("""
  **State.** s ∈ {0,1}^d, one flip per axis. Domain of each s_i : {0,1}.

  **Constraints.** For each pair x,y ∈ X differing on axes I: the allowed
  assignments of s|_I are those for which BOTH the selected corner and its
  complement lie in X.

  **Key symmetry.** The corner and its complement are both required, so
  **every constraint is closed under complementing s|_I** — the dual
  involution. So s and ¬s are solutions together, and the search is 2^(d−1).

  **ALGORITHM**
     1. build the constraints
     2. PROPAGATE: any axis forced by a width-1 constraint is fixed; any
        pair-constraint reduced to one option fixes its axes; iterate
     3. search the residue by branching on unfixed axes
""")
def allowed(S,x,y,d):
    Ss=S; I=[i for i in range(d) if x[i]!=y[i]]
    if not I: return None,None
    ok=set()
    for bits in product([0,1],repeat=len(I)):
        j=list(x); m=list(x)
        for t,i in enumerate(I):
            if bits[t]: j[i]=min(x[i],y[i]); m[i]=max(x[i],y[i])
            else:       j[i]=max(x[i],y[i]); m[i]=min(x[i],y[i])
        if tuple(j) in Ss and tuple(m) in Ss: ok.add(bits)
    return tuple(I),ok
def build(S,d):
    Ss=set(S); out=[]
    for x,y in combinations(sorted(S),2):
        I,ok=allowed(Ss,x,y,d)
        if I is None: continue
        if len(ok)==2**len(I): continue          # no constraint
        out.append((I,ok))
    return out
def propagate(cons,d):
    dom=[{0,1} for _ in range(d)]
    changed=True; rounds=0
    while changed and rounds<40:
        changed=False; rounds+=1
        for I,ok in cons:
            live=[b for b in ok if all(b[t] in dom[I[t]] for t in range(len(I)))]
            if not live: return None,rounds
            for t,i in enumerate(I):
                vals={b[t] for b in live}
                if vals<dom[i]: dom[i]=set(vals); changed=True
    return dom,rounds
def solve(S,d):
    cons=build(S,d)
    dom,rd=propagate(cons,d)
    if dom is None: return False,0,rd,cons
    free=[i for i in range(d) if len(dom[i])>1]
    tried=0
    for assign in product(*[sorted(dom[i]) for i in range(d)]):
        tried+=1
        ok=True
        for I,okset in cons:
            if tuple(assign[i] for i in I) not in okset: ok=False; break
        if ok: return True,tried,rd,cons
    return False,tried,rd,cons
def brute(S,d):
    Ss=set(S)
    for s in product([0,1],repeat=d):
        ok=True
        for x,y in combinations(sorted(S),2):
            j=tuple((min if s[i] else max)(x[i],y[i]) for i in range(d))
            m=tuple((max if s[i] else min)(x[i],y[i]) for i in range(d))
            if j not in Ss or m not in Ss: ok=False; break
        if ok: return True
    return False
print("="*88)
print("  TEST 1 — CORRECTNESS")
print("="*88)
n=ag=0
for _ in range(900):
    d=random.choice([3,4,5,6])
    cells=list(product(*[range(2)]*d))
    S=set(random.sample(cells,random.randint(3,min(len(cells),10))))
    if any(len({x[k] for x in S})<2 for k in range(d)): continue
    a,_,_,_=solve(S,d); b=brute(S,d)
    n+=1; ag+= (a==b)
print("\n     %d instances     algorithm == brute force : %d  (%.1f%%)"%(n,ag,100*ag/max(n,1)))
print("="*88)
print("  TEST 2 — DOES PROPAGATION PRUNE?  (the blocking mechanism, checked)")
print("="*88)
print("""
  **The reduction is blocked because clauses sharing variables share corners
  — the constraints are CORRELATED.** If that correlation is real, propagation
  should fix axes. **Measure it.**
""")
print("\n  %6s%12s%14s%16s%16s"%("d","instances","2^d","after propagation","reduction"))
print("  "+"-"*68)
for d in (4,5,6,7,8):
    tot=0; res=[]; cn=[]
    for _ in range(260):
        cells=list(product(*[range(2)]*d))
        S=set(random.sample(cells,random.randint(4,min(len(cells),12))))
        if any(len({x[k] for x in S})<2 for k in range(d)): continue
        cons=build(S,d)
        dom,_=propagate(cons,d)
        tot+=1
        if dom is None: res.append(0)
        else: res.append(1)
        cn.append(1 if dom is None else 2**sum(1 for i in range(d) if len(dom[i])>1))
    import numpy as np
    print("  %6d%12d%14d%16.1f%16.1f"%(d,tot,2**d,np.mean(cn),2**d/max(np.mean(cn),1e-9)))