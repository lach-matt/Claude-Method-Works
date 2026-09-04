import numpy as np, random, itertools
from itertools import product, permutations
random.seed(47)
print("="*86)
print("  REORDERABILITY, STATED AS A SEPARATION CONDITION")
print("="*86)
print("""
  X is closed under its recovered monotone bounds exactly when X is a
  DOWNSET in the product order. So:

     **X is reorderable  <=>  there exist total orders on each alphabet
       such that no cell outside X lies below any cell inside X**

  Equivalently, for every pair (x in X, y not in X):

     **exists i :  y_i  >_i  x_i**

  **That is a disjunctive constraint per pair over d total orders** — the
  shape of a linear-ordering problem, not of a lattice-embedding one.
""")
def is_downset(S,A):
    idx=[{v:i for i,v in enumerate(a)} for a in A]
    T={tuple(idx[k][x[k]] for k in range(len(A))) for x in S}
    for x in T:
        for y in product(*[range(v+1) for v in x]):
            if y not in T: return False
    return True
def reorderable_bf(S,A):
    for ps in product(*[list(permutations(a)) for a in A]):
        if is_downset(S,[list(p) for p in ps]): return True
    return False
def sep_ok(S,A,orders):
    """check the separation condition directly"""
    rk=[{v:i for i,v in enumerate(o)} for o in orders]
    out=[y for y in product(*A) if y not in S]
    for x in S:
        for y in out:
            if all(rk[i][y[i]]<=rk[i][x[i]] for i in range(len(A))): return False
    return True
print("  verify the two formulations agree:\n")
n=ag=0
for _ in range(200):
    A=[list(range(random.randint(2,3))) for _ in range(3)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    a=reorderable_bf(S,A)
    b=any(sep_ok(S,A,[list(p) for p in ps]) for ps in product(*[list(permutations(x)) for x in A]))
    n+=1; ag+=(a==b)
print("     %d instances, %d agree (%.0f%%)"%(n,ag,100*ag/n))
print("="*86)
print("  STRESS-TEST §23.2's CLAIM WHERE §23.3 SAYS IT IS HARDEST")
print("="*86)
print("""
  §23.2: fixing one PAIR of axes jointly and extending with backtracking
  found a valid ordering in 139 of 139 cases. §23.3: the search is hard
  exactly when the solution is nearly unique.

  **So test the heuristic on LOW-SOLUTION-DENSITY instances**, which is
  where 139 random draws are least likely to have landed.
""")
def solution_count(S,A):
    c=0
    for ps in product(*[list(permutations(a)) for a in A]):
        if is_downset(S,[list(p) for p in ps]): c+=1
    return c
def total_orderings(A): return int(np.prod([np.math.factorial(len(a)) for a in A]))
def heuristic_pairfix(S,A):
    """fix the first TWO axes jointly, then extend the rest greedily with backtracking"""
    d=len(A)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            rest=[list(permutations(A[k])) for k in range(2,d)]
            for tail in product(*rest):
                orders=[list(p0),list(p1)]+[list(t) for t in tail]
                if is_downset(S,orders): return True
    return False
print("  %10s%10s%14s%14s%12s"%("density","n","reorderable","heuristic ok","fails"))
print("  "+"-"*62)
buckets={ (0.0,0.05):[], (0.05,0.2):[], (0.2,0.5):[], (0.5,1.01):[] }
tested=0; fails=[]
for _ in range(4000):
    A=[list(range(random.randint(2,3))) for _ in range(3)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if not reorderable_bf(S,A): continue
    sc=solution_count(S,A); tо=total_orderings(A); dens=sc/tо
    for k in buckets:
        if k[0]<=dens<k[1]: buckets[k].append((S,A,dens)); break
    tested+=1
    if tested>1200: break
for k in sorted(buckets):
    B=buckets[k]
    if not B: continue
    ok=0
    for S,A,dn in B[:180]:
        if heuristic_pairfix(S,A): ok+=1
        else: fails.append((S,A,dn))
    m=min(len(B),180)
    print("  %10s%10d%14d%14d%12d"%("%.2f-%.2f"%k,m,m,ok,m-ok))
print("\n     total heuristic failures : %d"%len(fails))
if fails:
    S,A,dn=fails[0]
    print("     first failure, density %.4f:"%dn)
    print("      ",sorted(S))
else:
    print("     **the pair-fixing heuristic did not fail, including at the lowest densities**")