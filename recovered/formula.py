import numpy as np, math
from itertools import product, combinations
print("="*88)
print("  IS THERE A SINGLE EXPRESSION FOR THE COUNT?")
print("="*88)
def monos(k,hi):
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
def closed_canonical(r,c):
    """closed sets using exactly r rows and c columns, in place"""
    out=set()
    for m in monos(r,c):
        for nn in monos(c,r):
            S=frozenset((i,j) for i in range(r) for j in range(c) if j<=m[i] and i<=nn[j])
            if not S: continue
            rows={i for i,_ in S}; cols={j for _,j in S}
            if rows==set(range(r)) and cols==set(range(c)): out.add(S)
    return out
def closed_box(R,C):
    out=set()
    for r in range(1,R+1):
        for c in range(1,C+1):
            for S in closed_canonical(r,c):
                for rows in combinations(range(R),r):
                    for cols in combinations(range(C),c):
                        out.add(frozenset((rows[i],cols[j]) for (i,j) in S))
    return out
print("\n  THE CANONICAL COUNTS  a(r,c) — closed sets using every row and column\n")
print("  %6s"%"r\\c"+"".join("%9d"%c for c in range(1,7)))
print("  "+"-"*60)
A={}
for r in range(1,7):
    row="  %6d"%r
    for c in range(1,7):
        if r*c<=25:
            A[(r,c)]=len(closed_canonical(r,c)); row+="%9d"%A[(r,c)]
        else: row+="%9s"%"—"
    print(row)
print("="*88)
print("  READING THE TABLE")
print("="*88)
print("""
  **Symmetry.** a(r,c) = a(c,r) — the transpose is a bijection.
""")
sym=all(A.get((r,c))==A.get((c,r)) for r in range(1,6) for c in range(1,6) if (r,c) in A and (c,r) in A)
print("     symmetric : %s"%sym)
print("\n  first row and column:")
print("     a(1,c) =",[A.get((1,c)) for c in range(1,7)])
print("     a(r,1) =",[A.get((r,1)) for r in range(1,7)])
print("\n  the diagonal a(k,k) =",[A.get((k,k)) for k in range(1,6)])
print("\n  second row a(2,c) =",[A.get((2,c)) for c in range(1,7)])
print("  third  row a(3,c) =",[A.get((3,c)) for c in range(1,6)])
print("="*88)
print("  CANDIDATE CLOSED FORMS")
print("="*88)
print("\n  %-40s%s"%("candidate","check on a(r,c)"))
print("  "+"-"*70)
def test(f,name):
    ok=[]; bad=[]
    for (r,c),v in sorted(A.items()):
        try: p=f(r,c)
        except Exception: p=None
        if p is None: continue
        (ok if abs(p-v)<1e-9 else bad).append((r,c,v,p))
    return len(ok),len(bad),bad[:3]
CAND=[("C(r+c, r)",lambda r,c: math.comb(r+c,r)),
      ("C(r+c-2, r-1)",lambda r,c: math.comb(r+c-2,r-1)),
      ("binom product / (r+c)",lambda r,c: math.comb(r+c,r)*math.comb(r+c,c)/(r+c)),
      ("Catalan-like C(2r,r)/(r+1) at r=c",lambda r,c: (math.comb(2*r,r)//(r+1)) if r==c else None),
      ("r*c",lambda r,c: r*c),
      ("2^(r+c-2)",lambda r,c: 2**(r+c-2))]
for nm,f in CAND:
    o,b,ex=test(f,nm)
    print("  %-40s%d ok / %d wrong  %s"%(nm,o,b,str(ex)[:26] if ex else ""))
print("="*88)
print("  THE BOX COUNT FROM THE CANONICAL COUNT — an exact expression")
print("="*88)
print("""
  **This part IS a single expression, and it is exact:**

      N(R,C) = Σ_{r=1..R} Σ_{c=1..C}  C(R,r) · C(C,c) · a(r,c)

  **the canonical count times the number of embeddings.** Verify it against
  the direct enumeration.
""")
print("  %8s%14s%16s%10s"%("box","direct","by the sum","match"))
print("  "+"-"*50)
for R,C in [(2,2),(2,3),(3,3),(2,4),(3,4)]:
    direct=len(closed_box(R,C))
    s=sum(math.comb(R,r)*math.comb(C,c)*A[(r,c)] for r in range(1,R+1) for c in range(1,C+1) if (r,c) in A)
    print("  %8s%14d%16d%10s"%("%dx%d"%(R,C),direct,s,"YES" if direct==s else "no"))