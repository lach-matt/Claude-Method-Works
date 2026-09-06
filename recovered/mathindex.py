import numpy as np
from itertools import product, combinations
print("="*94)
print("  A LATTICE INDEX OF THE BOOK'S MATHEMATICS")
print("="*94)
print("""
  **Coordinates.** Each mathematical element of the book gets five:

     KIND     0 definition · 1 mechanism · 2 formula · 3 theorem · 4 law
              · 5 method · 6 measurement
     LANGUAGE 0 order/lattice · 1 combinatorics · 2 analysis · 3 complexity
              · 4 physics · 5 algebraic geometry
     STATUS   0 withdrawn · 1 conjectured · 2 measured · 3 verified · 4 proved
     VERIF    0 cited · 1 sampled · 2 exhaustive
     PRECED   0 none found · 1 found in the literature

  **Then close the index. E(X) counts the combinations the structure admits
  and the book does not carry — the questions still askable.**
""")
NM=['kind','language','status','verification','precedent']
K={'definition':0,'mechanism':1,'formula':2,'theorem':3,'law':4,'method':5,'measurement':6}
L={'order':0,'combin':1,'analysis':2,'complexity':3,'physics':4,'algeom':5}
S={'withdrawn':0,'conjectured':1,'measured':2,'verified':3,'proved':4}
V={'cited':0,'sampled':1,'exhaustive':2}
E=[
("E(X) closure defect",      'definition','order',  'proved',   'exhaustive',1),
("the operator 𝓡",           'mechanism', 'order',  'proved',   'exhaustive',1),
("Λ's construction",         'definition','combin', 'proved',   'exhaustive',1),
("join/meet closure of Λ",   'theorem',   'order',  'proved',   'exhaustive',1),
("rank modularity",          'theorem',   'order',  'verified', 'exhaustive',1),
("the single expression F",  'formula',   'combin', 'proved',   'exhaustive',1),
("F(−1) = 2",                'measurement','combin','proved',   'exhaustive',0),
("the fibration Σ|A_q||B_q|",'theorem',   'combin', 'verified', 'exhaustive',0),
("maximal chains = lin ext", 'theorem',   'order',  'proved',   'exhaustive',1),
("the bracket method",       'method',    'analysis','proved',  'sampled',   1),
("V = 4ν/3",                 'formula',   'analysis','measured','exhaustive',1),
("λ² = Newton decrement",    'formula',   'analysis','proved',  'cited',     1),
("self-concordance of T",    'theorem',   'analysis','verified','sampled',   1),
("Aitken bias = 1/3",        'theorem',   'analysis','proved',  'exhaustive',1),
("the Ritz expansion",       'formula',   'physics', 'proved',  'cited',     1),
("the Sc VI bracket",        'measurement','physics','verified','exhaustive',0),
("closure not locally det.", 'theorem',   'order',  'proved',   'exhaustive',0),
("reorderable ≡ sublattice", 'theorem',   'order',  'verified', 'exhaustive',1),
("the arity law",            'law',       'complexity','proved','exhaustive',1),
("the step law 2^(d−2)",     'theorem',   'order',  'proved',   'exhaustive',1),
("C1P + monotone endpoints", 'theorem',   'combin', 'proved',   'exhaustive',1),
("the level-3 signature",    'method',    'combin', 'verified', 'exhaustive',0),
("a(r,c) polynomials",       'formula',   'combin', 'proved',   'exhaustive',0),
("N(R,C) binomial transform",'formula',   'combin', 'proved',   'exhaustive',0),
("Tucker obstructions",      'theorem',   'combin', 'proved',   'cited',     1),
("Dilworth width",           'theorem',   'order',  'proved',   'cited',     1),
("the construction grammar", 'method',    'order',  'verified', 'sampled',   1),
("the obstruction census",   'measurement','combin','verified', 'exhaustive',0),
("mirror symmetry 1,095",    'measurement','algeom','verified', 'cited',     1),
("the resonance order cut",  'measurement','physics','verified','exhaustive',0),
]
X=set()
for nm,k,l,s,v,p in E: X.add((K[k],L[l],S[s],V[v],p))
d=5
print("     elements catalogued : %d      distinct coordinate cells : %d"%(len(E),len(X)))
A=[sorted({x[i] for x in X}) for i in range(d)]
print("     alphabets           : %s"%[len(a) for a in A])
print("     box                 : %d"%int(np.prod([len(a) for a in A])))
def Rop(S):
    Ls=sorted(S); Aa=[sorted({x[i] for x in Ls}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in Aa[j]:
                c=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*Aa) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}
adm=Rop(X); ex=adm-X
print("\n  **E(math index) = %d**"%len(ex))
def lat(S):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
print("     sublattice          : %s"%lat(X))
INV={v:k for k,v in K.items()}; LINV={v:k for k,v in L.items()}
SINV={v:k for k,v in S.items()}; VINV={v:k for k,v in V.items()}
if ex:
    print("\n  THE CELLS THE STRUCTURE ADMITS AND THE BOOK DOES NOT CARRY:\n")
    print("  %-13s%-12s%-13s%-13s%s"%("kind","language","status","verification","precedent"))
    print("  "+"-"*62)
    for c in sorted(ex):
        print("  %-13s%-12s%-13s%-13s%s"%(INV[c[0]],LINV[c[1]],SINV[c[2]],VINV[c[3]],
              "found" if c[4] else "none found"))