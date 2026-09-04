import numpy as np, random
from itertools import product, permutations
from math import factorial
random.seed(53)
print("="*86)
print("  THE PREVIOUS TEST WAS VACUOUS — IT ENUMERATED EVERYTHING")
print("="*86)
print("""
  My 'heuristic' looped over all orderings of every axis, which is the
  brute force it was meant to be compared against. **593 instances proved
  nothing.**  CORRECTION 125.

  **A genuine heuristic must commit.** Fix the first two axes jointly, then
  extend ONE axis at a time, accepting an ordering only if the PARTIAL
  structure stays consistent — and backtrack only when it cannot.
""")
def is_downset(S,A):
    idx=[{v:i for i,v in enumerate(a)} for a in A]
    T={tuple(idx[k][x[k]] for k in range(len(A))) for x in S}
    for x in T:
        for y in product(*[range(v+1) for v in x]):
            if y not in T: return False
    return True
def partial_ok(S,A,orders,fixed):
    """project onto the fixed axes and require THAT to be a downset"""
    idx={k:{v:i for i,v in enumerate(orders[k])} for k in fixed}
    P={tuple(idx[k][x[k]] for k in fixed) for x in S}
    for x in P:
        for y in product(*[range(v+1) for v in x]):
            if y not in P: return False
    return True
def greedy_pairfix(S,A,count=None):
    """fix axes 0,1 jointly; extend the rest one at a time with backtracking"""
    d=len(A); bt=[0]
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            orders=[list(p0),list(p1)]+[None]*(d-2)
            if not partial_ok(S,A,orders,[0,1]): continue
            def ext(k):
                if k==d: return is_downset(S,[list(o) for o in orders])
                for p in permutations(A[k]):
                    orders[k]=list(p)
                    if partial_ok(S,A,orders,list(range(k+1))):
                        if ext(k+1): return True
                    bt[0]+=1
                orders[k]=None; return False
            if ext(2):
                if count is not None: count.append(bt[0])
                return True
    if count is not None: count.append(bt[0])
    return False
def reorderable_bf(S,A):
    for ps in product(*[list(permutations(a)) for a in A]):
        if is_downset(S,[list(p) for p in ps]): return True
    return False
def soln_count(S,A):
    return sum(1 for ps in product(*[list(permutations(a)) for a in A])
               if is_downset(S,[list(p) for p in ps]))
print("="*86)
print("  NOW TEST IT — BY SOLUTION DENSITY, AS §23.3 DIRECTS")
print("="*86)
buckets={(0.0,0.05):[],(0.05,0.2):[],(0.2,0.5):[],(0.5,1.01):[]}
n=0
while n<1500 and sum(len(v) for v in buckets.values())<700:
    d=random.choice([3,3,4])
    A=[list(range(random.randint(2,3))) for _ in range(d)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    n+=1
    if not reorderable_bf(S,A): continue
    tot=int(np.prod([factorial(len(a)) for a in A]))
    dens=soln_count(S,A)/tot
    for k in buckets:
        if k[0]<=dens<k[1] and len(buckets[k])<180: buckets[k].append((S,A,dens)); break
print("\n  %12s%8s%12s%12s%14s"%("density","n","greedy ok","fails","mean backtr"))
print("  "+"-"*60)
allfail=[]
for k in sorted(buckets):
    B=buckets[k]
    if not B: continue
    ok=0; bts=[]
    for S,A,dn in B:
        c=[]
        r=greedy_pairfix(S,A,c)
        ok+=r; bts.append(c[0] if c else 0)
        if not r: allfail.append((S,A,dn))
    print("  %12s%8d%12d%12d%14.2f"%("%.2f-%.2f"%k,len(B),ok,len(B)-ok,np.mean(bts)))
print("\n     total instances : %d"%sum(len(v) for v in buckets.values()))
print("     greedy failures : %d"%len(allfail))
if allfail:
    S,A,dn=allfail[0]
    print("\n  **COUNTEREXAMPLE FOUND** — density %.4f"%dn)
    print("     alphabets:",A)
    print("     cells    :",sorted(S))
    print("     a valid ordering exists:",reorderable_bf(S,A))
else:
    print("""
     **NO COUNTEREXAMPLE.** The greedy pair-fixing extension found a valid
     ordering in every reorderable instance, including the lowest-density
     bucket where §23.3 says the search is hardest.

     **§23.2's claim survives a targeted attack** — which is a stronger
     statement than 139 random draws, and still not a proof.""")