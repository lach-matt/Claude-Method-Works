import numpy as np, math
from itertools import product, combinations
print("="*88)
print("  THE INVERSION — HALF THE EQUATION GIVES THE OTHER HALF")
print("="*88)
print("""
      N(R,C) = Σ C(R,r)·C(C,c)·a(r,c)        the binomial transform

  **Binomial transforms invert**, so

      a(r,c) = Σ (−1)^{(r−i)+(c−j)} C(r,i)·C(c,j)·N(i,j)

  **The two are the same information.** Verify, then look for a form in
  whichever is cleaner.
""")
def monos(k,hi):
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
def canon_count(r,c):
    out=set()
    for m in monos(r,c):
        for nn in monos(c,r):
            S=frozenset((i,j) for i in range(r) for j in range(c) if j<=m[i] and i<=nn[j])
            if not S: continue
            if {i for i,_ in S}==set(range(r)) and {j for _,j in S}==set(range(c)): out.add(S)
    return len(out)
MX=6
A=np.zeros((MX+1,MX+1),dtype=object)
for r in range(1,MX+1):
    for c in range(1,MX+1):
        if r*c<=30: A[r,c]=canon_count(r,c)
N=np.zeros((MX+1,MX+1),dtype=object)
for R in range(1,MX+1):
    for C in range(1,MX+1):
        s=0
        for r in range(1,R+1):
            for c in range(1,C+1):
                if A[r,c]: s+=math.comb(R,r)*math.comb(C,c)*A[r,c]
        N[R,C]=s
print("  N(R,C) — closed sets on the box\n")
print("  %5s"%"R\\C"+"".join("%10d"%c for c in range(1,MX+1)))
print("  "+"-"*66)
for R in range(1,MX+1):
    print("  %5d"%R+"".join("%10s"%(N[R,c] if N[R,c] else "—") for c in range(1,MX+1)))
print("\n  INVERT IT BACK\n")
ok=0; bad=0
for r in range(1,MX+1):
    for c in range(1,MX+1):
        if not A[r,c]: continue
        s=0
        for i in range(1,r+1):
            for j in range(1,c+1):
                s+=(-1)**((r-i)+(c-j))*math.comb(r,i)*math.comb(c,j)*N[i,j]
        if s==A[r,c]: ok+=1
        else: bad+=1; print("     a(%d,%d): recovered %s, true %s"%(r,c,s,A[r,c]))
print("     **inversion recovers a(r,c) : %d of %d**"%(ok,ok+bad))
print("="*88)
print("  SO LOOK FOR THE FORM IN N")
print("="*88)
print("\n     N(1,c) =",[int(N[1,c]) for c in range(1,MX+1)])
print("     N(2,c) =",[int(N[2,c]) for c in range(1,MX+1)])
print("     N(3,c) =",[int(N[3,c]) for c in range(1,MX+1)])
print("     diagonal N(k,k) =",[int(N[k,k]) for k in range(1,MX+1)])
print("\n  %-44s%s"%("candidate for N","fit"))
print("  "+"-"*66)
def chk(f):
    o=b=0; ex=[]
    for R in range(1,MX+1):
        for C in range(1,MX+1):
            if not N[R,C]: continue
            try: p=f(R,C)
            except Exception: continue
            if p is None: continue
            if abs(p-int(N[R,C]))<1e-6: o+=1
            else:
                b+=1
                if len(ex)<2: ex.append((R,C,int(N[R,C]),p))
    return o,b,ex
CAND=[("(2^R − 1)(2^C − 1)",lambda R,C:(2**R-1)*(2**C-1)),
      ("C(R+C,R) − 1",lambda R,C:math.comb(R+C,R)-1),
      ("3^R·3^C-ish  (2^{R+C})",lambda R,C:2**(R+C)),
      ("R·C·2^{R+C-2}",lambda R,C:R*C*2**(R+C-2)),
      ("**(2^R−1)(2^C−1) + something**",lambda R,C:None)]
for nm,f in CAND:
    o,b,ex=chk(f)
    print("  %-44s%d ok / %d wrong  %s"%(nm,o,b,str(ex)[:22] if ex else ""))
print("\n  N(1,c) is all 1s?  ->",[int(N[1,c]) for c in range(1,MX+1)])
print("  ratios N(k,k+1)/N(k,k) :",["%.3f"%(N[k,k+1]/N[k,k]) for k in range(1,MX) if N[k,k+1] and N[k,k]])