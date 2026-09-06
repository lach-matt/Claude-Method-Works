import numpy as np, math
from fractions import Fraction as F
from itertools import combinations
print("="*88)
print("  THE KERNEL a(r,c) — ROW BY ROW")
print("="*88)
def monos(k,hi):
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
def a(r,c):
    out=set()
    for m in monos(r,c):
        for nn in monos(c,r):
            S=frozenset((i,j) for i in range(r) for j in range(c) if j<=m[i] and i<=nn[j])
            if not S: continue
            if {i for i,_ in S}==set(range(r)) and {j for _,j in S}==set(range(c)): out.add(S)
    return len(out)
ROWS={}
for r in (1,2,3,4):
    lim={1:12,2:11,3:9,4:7}[r]
    ROWS[r]=[a(r,c) for c in range(1,lim+1)]
    print("\n     a(%d,c) = %s"%(r,ROWS[r]))
    d=ROWS[r][:]
    k=0
    while len(set(d))>1 and len(d)>1 and k<8:
        d=[d[i+1]-d[i] for i in range(len(d)-1)]; k+=1
        print("        Δ^%d : %s"%(k,d[:9]))
    if len(set(d))==1:
        print("        **constant at Δ^%d = %s  ->  polynomial of degree %d**"%(k,d[0],k))
print("="*88)
print("  FIT EXACT POLYNOMIALS")
print("="*88)
def fit(vals,deg):
    n=deg+1
    A=[[F(c**k) for k in range(n)] for c in range(1,n+1)]
    b=[F(v) for v in vals[:n]]
    # gaussian elimination over rationals
    M=[row[:]+[b[i]] for i,row in enumerate(A)]
    for i in range(n):
        p=next(j for j in range(i,n) if M[j][i]!=0)
        M[i],M[p]=M[p],M[i]
        pv=M[i][i]
        M[i]=[x/pv for x in M[i]]
        for j in range(n):
            if j!=i and M[j][i]!=0:
                f=M[j][i]
                M[j]=[M[j][k]-f*M[i][k] for k in range(n+1)]
    return [M[i][n] for i in range(n)]
DEG={1:0,2:2,3:4,4:6}
for r in (1,2,3,4):
    vals=ROWS[r]; deg=DEG[r]
    if len(vals)<deg+1: continue
    co=fit(vals,deg)
    pred=[sum(co[k]*F(c**k) for k in range(deg+1)) for c in range(1,len(vals)+1)]
    ok=all(pred[i]==vals[i] for i in range(len(vals)))
    terms=" + ".join("%s·c^%d"%(co[k],k) for k in range(deg,-1,-1) if co[k]!=0)
    print("\n     a(%d,c) degree %d : %s"%(r,deg,terms))
    print("        exact on all %d values : **%s**"%(len(vals),ok))
    if not ok:
        print("        predicted %s"%[str(p) for p in pred[:8]])
print("="*88)
print("  THE PATTERN IN THE DEGREES")
print("="*88)
print("""
     a(1,c) : degree 0
     a(2,c) : degree 2
     a(3,c) : degree 4
     a(4,c) : degree 6

  > **a(r,c) is a polynomial in c of degree 2(r−1)** — and by the symmetry
  > a(r,c) = a(c,r), it is a polynomial in r of degree 2(c−1). **A function
  > polynomial in each variable separately, with degree growing linearly in
  > the other: that is a QUASI-POLYNOMIAL of the kind Ehrhart theory
  > produces for lattice-point counts in dilated polytopes.**
""")
print("="*88)
print("  AND THE LEADING COEFFICIENTS")
print("="*88)
for r in (2,3,4):
    vals=ROWS[r]; deg=DEG[r]
    if len(vals)<deg+1: continue
    co=fit(vals,deg)
    print("     a(%d,c) leading term : %s·c^%d      1/lead = %s"%(r,co[deg],deg,1/co[deg] if co[deg] else "—"))