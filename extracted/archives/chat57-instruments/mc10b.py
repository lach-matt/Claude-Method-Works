from itertools import combinations
from lam8 import L8
from mc10 import CONS
import numpy as np
cells=L8()
rows=[]
for a,b in combinations(cells,2):
    lo=tuple(min(u,v) for u,v in zip(a,b)); hi=tuple(max(u,v) for u,v in zip(a,b))
    rows.append([1 if f(lo,hi) else 0 for _,f in CONS])
A=np.array(rows,dtype=np.int8); N=len(A)
p=A.mean(0)
names=[n for n,_ in CONS]
print("N",N)
# pairwise lift P(Ci&Cj)/(P(Ci)P(Cj))
print("pairwise lift matrix (rows/cols in constraint order):")
print("            "+" ".join(f"{n[:9]:>9s}" for n in names))
for i in range(7):
    print(f"{names[i]:12s}"+" ".join(f"{((A[:,i]&A[:,j]).mean()/(p[i]*p[j])):9.3f}" for j in range(7)))
# coordinate-sharing adjacency
share={(0,1):'l',(1,2):'k',(2,3):'q',(3,4):'g',(4,5):'f',(2,6):'k'}
print("shared-coordinate pairs:",{f"{names[i]}|{names[j]}":c for (i,j),c in share.items()})
# chain rule along tree order: C0 l<=n-1, C1 k<=.., C2 q<=k, C6 2S<=k, C3 g<=q, C4 g<=2(2f+1), C5 f<=e-1
order=[0,1,2,6,3,4,5]
mask=np.ones(N,dtype=bool); prod=1.0; joint=1.0
print("chain-rule decomposition (tree order):")
for i in order:
    cond=A[mask,i].mean(); lift=cond/p[i]; prod*=lift
    print(f"  P({names[i]:11s}| previous) = {cond:.4f}   marginal {p[i]:.4f}   lift {lift:.4f}")
    mask&=A[:,i].astype(bool)
print("product of lifts =",round(prod,4),"  joint/product =",round(mask.mean()/np.prod(p),4))
# lifts restricted to immediate tree-neighbour conditioning only (Markov check)
print("Markov check: P(Ci | only its shared-coordinate neighbours already in order):")
nb={1:[0],2:[1],6:[2],3:[2],4:[3],5:[4]}
prodm=1.0
for i in order:
    if i==0: continue
    m=np.ones(N,dtype=bool)
    for j in nb[i]: m&=A[:,j].astype(bool)
    lift=A[m,i].mean()/p[i]; prodm*=lift
    print(f"  {names[i]:11s} given {[names[j] for j in nb[i]]}: lift {lift:.4f}")
print("product of neighbour-only lifts =",round(prodm,4))
