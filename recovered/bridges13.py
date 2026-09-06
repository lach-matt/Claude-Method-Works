from itertools import product
from collections import defaultdict
import sys
NM,EM,LM,KM,FM=3,3,1,3,1
phi={1:3,2:4,3:5}
NAME=['n','l','k','q','e','f','g','2S',"2S'",'v','2Jc','K','2J']
X=[]
for n in range(1,NM+1):
 for l in range(0,min(LM,n-1)+1):
  for k in range(1,min(KM,2*(2*l+1))+1):
   for q in range(0,k+1):
    for s in range(0,k+1):
     for e in range(1,EM+1):
      for f in range(0,min(FM,e-1)+1):
       for g in range(0,min(q,2*(2*f+1))+1):
        for sp in range(0,g+1):
         for v in range(sp,g+1):
          for jc in range(0,phi[k]+1):
           for K in range(0,jc+2*FM+1):
            for J in range(max(0,K-1),K+2):
             X.append((n,l,k,q,e,f,g,s,sp,v,jc,K,J))
print(f"|Λ₁₃| = {len(X):,}")
A=[0,1,2,7,10,11,12]; B=[4,5,6,8,9]; Q=3
def defect(Y):
    tot=0
    for q in sorted({y[Q] for y in Y}):
        a={tuple(y[i] for i in A) for y in Y if y[Q]==q}
        b={tuple(y[i] for i in B) for y in Y if y[Q]==q}
        tot+=len(a)*len(b)
    return tot-len(Y)
print(f"factorisation over q, as built: defect {defect(X)}")

print(f"\nevery A-side/B-side coupling, imposed and priced:")
print(f"{'bridge':>12} {'cells':>8} {'retained':>9} {'defect':>8}")
rows=[]
for i in A:
    for j in B:
        for lo,hi in ((i,j),(j,i)):
            Y=[y for y in X if y[lo]<=y[hi]]
            if len(Y)==len(X) or len(Y)<100: continue
            rows.append((f"{NAME[lo]} ≤ {NAME[hi]}", len(Y), 100*len(Y)/len(X), defect(Y)))
for r in sorted(rows, key=lambda r:-r[1]):
    print(f"{r[0]:>12} {r[1]:>8,} {r[2]:>8.1f}% {r[3]:>8,}")
nz=sum(1 for r in rows if r[3]!=0)
print(f"\n{len(rows)} candidate second bridges · {nz} break the factorisation · "
      f"{len(rows)-nz} leave it exact")