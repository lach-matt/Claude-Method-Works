import numpy as np
from itertools import product, combinations
print("="*84)
print("  §24.3.4 — E(X) ON THE χ = ±6 SLICE OF THE KREUZER–SKARKE LIST")
print("="*84)
print("""
  **Candelas, de la Ossa, Fu & Szendroi (Triadophilia, ATMP 12 (2008) 429):**
  the KS list's χ = ±6 points are (h, h+3) and (h+3, h) for 13 ≤ h ≤ 128,
  **excluding h = 102, 103, 115, 117 and 119–126.**

  **That is an exactly specified subset, so E(X) can be computed on it.**
""")
EXC={102,103,115,117,119,120,121,122,123,124,125,126}
H=[h for h in range(13,129) if h not in EXC]
X=sorted({(h,h+3) for h in H} | {(h+3,h) for h in H})
d=2; Xs=set(X)
print("     h values admitted     : %d of 116"%len(H))
print("     excluded              : %s"%sorted(EXC))
print("     **cells in the slice  : %d**"%len(X))
def RE(S):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)},A
adm,A=RE(X)
print("\n     alphabets             : %s"%[len(a) for a in A])
print("     box                   : %d"%(len(A[0])*len(A[1])))
print("     admitted by 𝓡         : %d"%len(adm))
print("     **E(X) = %d**"%(len(adm)-len(X)))
jf=mf=0
for x,y in combinations(X,2):
    if (max(x[0],y[0]),max(x[1],y[1])) not in Xs: jf+=1
    if (min(x[0],y[0]),min(x[1],y[1])) not in Xs: mf+=1
print("     join failures         : %d of %d pairs"%(jf,len(X)*(len(X)-1)//2))
print("     meet failures         : %d"%mf)
print("="*84)
print("  AND THE MIRROR SYMMETRY OF THE SLICE")
print("="*84)
mir=sum(1 for (a,b) in X if (b,a) in Xs)
print("\n     cells with a mirror partner : %d of %d  (%.1f%%)"%(mir,len(X),100*mir/len(X)))
print("     self-mirror (h11 = h21)     : %d"%sum(1 for (a,b) in X if a==b))
print("="*84)
print("  WHAT THE EXCLUSIONS LOOK LIKE AS A CELL SET")
print("="*84)
full=sorted({(h,h+3) for h in range(13,129)} | {(h+3,h) for h in range(13,129)})
admF,_=RE(full)
print("\n     with NO exclusions : %d cells, E(X) = %d"%(len(full),len(admF)-len(full)))
print("     with the exclusions: %d cells, E(X) = %d"%(len(X),len(adm)-len(X)))
print("""
  **The exclusions are 24 of 232 cells — 10.3%% of the slice — and they are the
  interesting part.** A run of eight consecutive h (119–126) is missing, plus
  four isolated values. **That is a void, in the sense of Chapter 5.**
""")
gaps=[]
run=[]
for h in range(13,129):
    if h in EXC: run.append(h)
    elif run: gaps.append(run); run=[]
if run: gaps.append(run)
print("     the void, as runs of h :",[(g[0],g[-1]) if len(g)>1 else g[0] for g in gaps])