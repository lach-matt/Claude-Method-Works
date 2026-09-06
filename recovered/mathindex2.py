import numpy as np
from itertools import product, combinations
print("="*90)
print("  WHY THE FIRST INDEX DID NOT CLOSE")
print("="*90)
print("""
  **𝓡 recovers MONOTONE bounds. It requires ORDERED coordinates.** Of the five
  I assigned, only three are genuinely ordered:

     STATUS   withdrawn < conjectured < measured < verified < proved   ORDERED
     VERIF    cited < sampled < exhaustive                            ORDERED
     PRECED   none found < found                                      ORDERED
     KIND     definition, mechanism, formula, theorem, law, method …   CATEGORICAL
     LANGUAGE order, combinatorics, analysis, complexity, physics …    CATEGORICAL

  **Imposing an order on a categorical axis makes the closure meaningless** —
  it admits every cell above an arbitrary ranking. **That is the precondition
  the book never states: 𝓡 applies to ordered coordinates only.**

  **So the right structure is a FIBRATION: fibre over (kind, language), with
  the three ordered coordinates inside.** Exactly Λ's own shape.
""")
K=['definition','mechanism','formula','theorem','law','method','measurement']
L=['order','combin','analysis','complexity','physics','algeom']
S={'withdrawn':0,'conjectured':1,'measured':2,'verified':3,'proved':4}
V={'cited':0,'sampled':1,'exhaustive':2}
E=[
("E(X) closure defect",'definition','order','proved','exhaustive',1),
("the operator 𝓡",'mechanism','order','proved','exhaustive',1),
("Λ's construction",'definition','combin','proved','exhaustive',1),
("join/meet closure of Λ",'theorem','order','proved','exhaustive',1),
("rank modularity",'theorem','order','verified','exhaustive',1),
("the single expression F",'formula','combin','proved','exhaustive',1),
("F(−1) = 2",'measurement','combin','proved','exhaustive',0),
("the fibration",'theorem','combin','verified','exhaustive',0),
("maximal chains = lin ext",'theorem','order','proved','exhaustive',1),
("the bracket method",'method','analysis','proved','sampled',1),
("V = 4ν/3",'formula','analysis','measured','exhaustive',1),
("λ² = Newton decrement",'formula','analysis','proved','cited',1),
("self-concordance",'theorem','analysis','verified','sampled',1),
("Aitken bias = 1/3",'theorem','analysis','proved','exhaustive',1),
("the Ritz expansion",'formula','physics','proved','cited',1),
("the Sc VI bracket",'measurement','physics','verified','exhaustive',0),
("closure not locally det.",'theorem','order','proved','exhaustive',0),
("reorderable ≡ sublattice",'theorem','order','verified','exhaustive',1),
("the arity law",'law','complexity','proved','exhaustive',1),
("the step law 2^(d−2)",'theorem','order','proved','exhaustive',1),
("C1P + monotone endpoints",'theorem','combin','proved','exhaustive',1),
("the level-3 signature",'method','combin','verified','exhaustive',0),
("a(r,c) polynomials",'formula','combin','proved','exhaustive',0),
("N(R,C) transform",'formula','combin','proved','exhaustive',0),
("Tucker obstructions",'theorem','combin','proved','cited',1),
("Dilworth width",'theorem','order','proved','cited',1),
("the construction grammar",'method','order','verified','sampled',1),
("the obstruction census",'measurement','combin','verified','exhaustive',0),
("mirror symmetry 1,095",'measurement','algeom','verified','cited',1),
("the resonance order cut",'measurement','physics','verified','exhaustive',0),
]
print("="*90)
print("  THE FIBRATION")
print("="*90)
from collections import defaultdict
fib=defaultdict(list)
for nm,k,l,s,v,p in E: fib[(k,l)].append((S[s],V[v],p,nm))
print("\n  %-13s%-12s%8s%36s"%("kind","language","cells","the elements"))
print("  "+"-"*74)
for key in sorted(fib,key=lambda t:(K.index(t[0]),L.index(t[1]))):
    els=fib[key]
    print("  %-13s%-12s%8d  %s"%(key[0],key[1],len(els),", ".join(e[3][:20] for e in els)[:40]))
print("\n     fibres occupied : %d of %d possible"%(len(fib),len(K)*len(L)))
print("="*90)
print("  CLOSURE WITHIN EACH FIBRE  (the three ordered coordinates)")
print("="*90)
def Rop(S,dd=3):
    Ls=sorted(S); Aa=[sorted({x[i] for x in Ls}) for i in range(dd)]
    ph={}
    for i in range(dd):
        for j in range(dd):
            if i==j: continue
            f={}; run=-1
            for v in Aa[j]:
                c=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*Aa) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(dd) for j in range(dd) if i!=j)}
tot=0; closed=0; gaps=[]
print("\n  %-13s%-12s%8s%10s%10s"%("kind","language","cells","E(fibre)","closed"))
print("  "+"-"*56)
for key in sorted(fib,key=lambda t:(K.index(t[0]),L.index(t[1]))):
    pts={(a,b,c) for a,b,c,_ in fib[key]}
    e=len(Rop(pts))-len(pts)
    tot+=1; closed+= (e==0)
    print("  %-13s%-12s%8d%10d%10s"%(key[0],key[1],len(pts),e,"YES" if e==0 else "no"))
    if e: gaps.append((key,Rop(pts)-pts))
print("\n     **fibres closed : %d of %d**"%(closed,tot))
SI={v:k for k,v in S.items()}; VI={v:k for k,v in V.items()}
if gaps:
    print("\n  THE ADMITTED-BUT-ABSENT CELLS — the questions still askable:\n")
    for key,ex in gaps:
        for c in sorted(ex):
            print("     %-12s %-10s -> status %s, verification %s, precedent %s"
                  %(key[0],key[1],SI[c[0]],VI[c[1]],"found" if c[2] else "none"))
else:
    print("""
  > **Every fibre closes. E = 0 throughout.**
  > **No combination of status, verification and precedent is admitted by the
  > structure and missing from the book — within any kind-and-language.**
""")