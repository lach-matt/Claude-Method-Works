import random, math
from itertools import product, permutations, combinations
from collections import Counter
random.seed(683)
print("="*88)
print("  THE REALISABILITY RESTRICTION, QUANTIFIED")
print("="*88)
print("""
  **A cell set X ⊆ {0,1}^d carries |X|·d bits and generates up to C(|X|,2)
  constraints, each drawn from a language of many relations.** So the
  realisable constraint systems are a tiny subfamily — **and that is the
  structure to use, not to fight.**

  Measure: how many distinct constraint systems arise, against how many the
  language admits?
""")
def constraints(S,d):
    Ss=set(S); out=[]
    for x,y in combinations(sorted(S),2):
        I=tuple(i for i in range(d) if x[i]!=y[i])
        if not I: continue
        ok=set()
        for bits in product([0,1],repeat=len(I)):
            j=list(x); m=list(x)
            for t,i in enumerate(I):
                j[i]= max(x[i],y[i]) if bits[t]==0 else min(x[i],y[i])
                m[i]= min(x[i],y[i]) if bits[t]==0 else max(x[i],y[i])
            if tuple(j) in Ss and tuple(m) in Ss: ok.add(bits)
        if len(ok)<2**len(I): out.append((I,frozenset(ok)))
    return frozenset(out)
print("  %6s%10s%14s%18s%18s"%("d","|X|","cell sets","distinct systems","bits |X|·d"))
print("  "+"-"*68)
for d in (4,5):
    for sz in (5,6,7):
        cells=list(product(*[range(2)]*d))
        seen=set(); n=0
        for _ in range(900):
            S=set(random.sample(cells,sz))
            if any(len({x[k] for x in S})<2 for k in range(d)): continue
            n+=1; seen.add(constraints(S,d))
        print("  %6d%10d%14d%18d%18d"%(d,sz,n,len(seen),sz*d))
print("="*88)
print("  THE CONSTRAINT GRAPH — HOW COUPLED ARE THE CONSTRAINTS?")
print("="*88)
print("""
  **If clauses sharing variables share cells, the constraint hypergraph is
  dense and highly coupled.** Measure the coupling: how many constraints
  touch each variable, and how many cells each constraint depends on.
""")
print("\n  %6s%10s%14s%16s%18s"%("d","|X|","constraints","per variable","distinct scopes"))
print("  "+"-"*66)
for d in (4,5,6):
    tot=[]; per=[]; sc=[]
    for _ in range(200):
        cells=list(product(*[range(2)]*d))
        S=set(random.sample(cells,min(len(cells),8)))
        if any(len({x[k] for x in S})<2 for k in range(d)): continue
        C=constraints(S,d)
        tot.append(len(C))
        cnt=Counter()
        for I,_ in C:
            for i in I: cnt[i]+=1
        per.append(sum(cnt.values())/max(d,1))
        sc.append(len({I for I,_ in C}))
    import numpy as np
    if tot: print("  %6d%10d%14.1f%16.1f%18.1f"%(d,8,np.mean(tot),np.mean(per),np.mean(sc)))
print("="*88)
print("  AND THE DECISIVE COUNT")
print("="*88)
print("""
  **The number of distinct scopes is at most 2^d − 1** (subsets of axes), and
  the number of variables is d. **So the constraint hypergraph has d vertices
  and at most 2^d − 1 hyperedges — a complete hypergraph on d vertices.**

  > **Its treewidth is at most d − 1, trivially.** So the CSP is solvable by
  > dynamic programming in 2^d · poly — **which is the FPT bound already
  > known, and the realisability restriction does NOT reduce it.**

  **The structural solution therefore has to come from the CORRELATION between
  constraints, not from the sparsity of the hypergraph** — because the
  hypergraph is complete.
""")