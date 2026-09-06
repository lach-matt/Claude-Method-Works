import numpy as np, math, time
from itertools import product, permutations, combinations
print("="*88)
print("  THE GENERATOR, BUILT TO THE INDEX'S ALPHABET CONVENTION")
print("="*88)
print("""
  **The convention.** A closed set's alphabet is RECOVERED from its cells.
  So {(0,1)} on a 2×2 box is the same object as {(0,0)} — one cell, one row,
  one column. **Generation must produce one CANONICAL representative per
  class, and the box count is representatives × embeddings.**
""")
def monos(k,hi):
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
def gen_canonical(r,c):
    """closed sets using EXACTLY r rows and c columns, in canonical position"""
    out=set()
    for m in monos(r,c):
        for nn in monos(c,r):
            S=frozenset((i,j) for i in range(r) for j in range(c) if j<=m[i] and i<=nn[j])
            if not S: continue
            rows={i for i,_ in S}; cols={j for _,j in S}
            if len(rows)==r and len(cols)==c and rows==set(range(r)) and cols==set(range(c)):
                out.add(S)
    return out
def is_closed(S):
    A=[sorted({x[i] for x in S}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        cc=[y for (x,y) in S if x<=v]; run=max(run,max(cc) if cc else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        cc=[x for (x,y) in S if y<=w]; run=max(run,max(cc) if cc else -1); N[w]=run
    return {(a,b) for a in A[0] for b in A[1] if b<=M[a] and a<=N[b]}==set(S)
def closed_by_test(R,C):
    cells=list(product(range(R),range(C))); n=len(cells); out=set()
    for m in range(1,1<<n):
        S=frozenset(cells[i] for i in range(n) if m>>i & 1)
        if is_closed(S): out.add(S)
    return out
def generate_box(R,C):
    """all closed sets on an R×C box, by generation + embedding"""
    out=set()
    for r in range(1,R+1):
        for c in range(1,C+1):
            reps=gen_canonical(r,c)
            for S in reps:
                for rows in combinations(range(R),r):
                    for cols in combinations(range(C),c):
                        out.add(frozenset((rows[i],cols[j]) for (i,j) in S))
    return out
print("="*88)
print("  TEST 1 — COUNT AGREEMENT (a census test)")
print("="*88)
print("\n  %8s%10s%14s%14s%10s%12s%12s"%("box","cells","by TESTING","by GENERATION","match","test s","gen s"))
print("  "+"-"*82)
for R,C in [(2,2),(2,3),(3,3),(2,4),(3,4)]:
    n=R*C
    t0=time.time(); A=closed_by_test(R,C); t1=time.time()-t0
    t0=time.time(); B=generate_box(R,C); t2=time.time()-t0
    print("  %8s%10d%14d%14d%10s%12.3f%12.3f"%("%dx%d"%(R,C),n,len(A),len(B),
        "YES" if A==B else "no",t1,t2))
print("="*88)
print("  TEST 2 — SOUNDNESS (an independent property test)")
print("="*88)
print("""
  **Different question:** is every generated set actually closed? This does
  not compare counts — it checks each object against the definition.
""")
bad=0; tot=0
for R,C in [(2,2),(2,3),(3,3),(3,4),(4,4),(2,5)]:
    for S in generate_box(R,C):
        tot+=1
        if not is_closed(S): bad+=1
print("\n     generated sets checked : %d      not closed : %d      **sound : %s**"%(tot,bad,bad==0))
print("="*88)
print("  TEST 3 — COMPLETENESS ON A BOX THE CENSUS CANNOT REACH")
print("="*88)
print("""
  **Different question again:** on a box too large to enumerate subsets,
  sample RANDOM closed sets by a third method — close a random seed under the
  operator — and check each is generated.
""")
import random
random.seed(577)
def close_random(R,C,k):
    S=set(random.sample(list(product(range(R),range(C))),k))
    while True:
        A=[sorted({x[i] for x in S}) for i in range(2)]
        M={};run=-1
        for v in A[0]:
            cc=[y for (x,y) in S if x<=v]; run=max(run,max(cc) if cc else -1); M[v]=run
        N={};run=-1
        for w in A[1]:
            cc=[x for (x,y) in S if y<=w]; run=max(run,max(cc) if cc else -1); N[w]=run
        T={(a,b) for a in A[0] for b in A[1] if b<=M[a] and a<=N[b]}
        if T==S: return frozenset(S)
        S=T
for R,C in [(4,5),(5,5)]:
    G=generate_box(R,C)
    miss=0; n=0
    for _ in range(400):
        S=close_random(R,C,random.randint(2,8))
        if not S: continue
        n+=1
        if S not in G: miss+=1
    print("\n     box %dx%d : generated %d sets"%(R,C,len(G)))
    print("        random closures sampled %d     NOT in the generated set : %d"%(n,miss))
    print("        subsets of this box would be 2^%d = %d"%(R*C,2**(R*C)))