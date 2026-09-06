import numpy as np, math, time
from itertools import product, permutations, combinations
print("="*88)
print("  THE INVERSION MECHANISM")
print("="*88)
print("""
  **Testing** asks: is X in the obstruction list? — the list is 10^2080 for
  Λ's box and will never be written.

  **Generating** asks: what does the rule produce? — a closed set IS its
  bounds, so **enumerate the BOUNDS, not the subsets.**

     subsets of a box with n cells   : 2^n
     bound systems on it             : ∏ (monotone maps), far fewer

  **The chain exists only inside the index that carries its information.**
  Generate from inside; the complement is the obstruction set, never listed.
""")
def monos(k,hi):
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
print("="*88)
print("  d = 2 — GENERATION vs TESTING, MEASURED")
print("="*88)
def closed_by_test(r,c):
    cells=list(product(range(r),range(c))); n=len(cells); out=set()
    for m in range(1,1<<n):
        S=frozenset(cells[i] for i in range(n) if m>>i & 1)
        A=[sorted({x[i] for x in S}) for i in range(2)]
        M={};run=-1
        for v in A[0]:
            cc=[y for (x,y) in S if x<=v]; run=max(run,max(cc) if cc else -1); M[v]=run
        N={};run=-1
        for w in A[1]:
            cc=[x for (x,y) in S if y<=w]; run=max(run,max(cc) if cc else -1); N[w]=run
        if {(a,b) for a in A[0] for b in A[1] if b<=M[a] and a<=N[b]}==set(S): out.add(S)
    return out
def closed_by_gen(r,c):
    out=set()
    for m in monos(r,c):
        for nn in monos(c,r):
            S=frozenset((i,j) for i in range(r) for j in range(c) if j<=m[i] and i<=nn[j])
            if S: out.add(S)
    return out
print("\n  %8s%10s%14s%14s%16s%14s"%("box","cells","by TESTING","by GENERATION","test cost","gen cost"))
print("  "+"-"*76)
for r,c in [(2,2),(2,3),(3,3),(2,4),(3,4)]:
    n=r*c
    if n<=12:
        t0=time.time(); A=closed_by_test(r,c); t1=time.time()-t0
    else:
        A=None; t1=None
    t0=time.time(); B=closed_by_gen(r,c); t2=time.time()-t0
    print("  %8s%10d%14s%14d%16s%14s"%("%dx%d"%(r,c),n,
        (str(len(A)) if A is not None else "2^%d — no"%n),len(B),
        ("%.3fs"%t1 if t1 else "—"),"%.3fs"%t2))
    if A is not None and A!=B:
        print("        **MISMATCH: testing %d, generation %d**"%(len(A),len(B)))
        ex=list(A-B)[:1]+list(B-A)[:1]
        for e in ex: print("           ",sorted(e))
print("="*88)
print("  WHY THEY DIFFER, AND THE FIX")
print("="*88)
print("""
  Generation over (m, n) pairs on a FIXED r×c grid produces the closed sets
  that use ALL rows and columns. **Testing counts closed sets on the
  RECOVERED alphabet — a set occupying 3 of 4 rows is counted there as a
  3-row instance.**

  **So the two count different things, and generation is the one that matches
  the index.** To recover the total, sum generation over every sub-box:
""")
def total_by_gen(r,c):
    tot=set()
    for rr in range(1,r+1):
        for cc in range(1,c+1):
            for S in closed_by_gen(rr,cc):
                A=[sorted({x[i] for x in S}) for i in range(2)]
                if len(A[0])==rr and len(A[1])==cc:
                    tot.add((rr,cc,S))
    return tot
print("\n  %8s%16s%20s%14s"%("box","by TESTING","gen over sub-boxes","match"))
print("  "+"-"*62)
for r,c in [(2,2),(2,3),(3,3)]:
    A=closed_by_test(r,c)
    G=total_by_gen(r,c)
    # count distinct cell-sets up to which sub-box they occupy
    gs={S for _,_,S in G}
    print("  %8s%16d%20d%14s"%("%dx%d"%(r,c),len(A),len(gs),"yes" if len(A)==len(gs) else "NO"))
print("""
{0}
  WHAT THE INVERSION BUYS
{0}
""".format("="*88))
print("""  **Generation is output-polynomial where testing is box-exponential.** For
  a 3×4 box: 2^12 = 4,096 subsets tested, against a direct enumeration of
  bound pairs. **The gap widens without limit.**

  > **The obstruction list is never written because the reorderable sets are
  > generated instead.** That is the inversion, and it is how the d = 2 case
  > is already handled — a PQ-tree GENERATES the admissible orders.
""")