import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(439)
print("="*88)
print("  DOES THE PROBLEM DECOMPOSE?")
print("="*88)
print("""
  Every formulation today sought ONE procedure. **But the constraints may
  split into independent groups**, each solvable separately — in which case
  the answer is a conjunction of small solutions, not one large one.

  **Candidate decomposition: the AXIS-INTERACTION graph.** Axes i and j are
  linked if some pair of cells differs on both. Components of that graph
  are independent constraint blocks.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord(S,d):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>10**6: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def axis_components(S,d):
    par=list(range(d))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for x,y in combinations(sorted(S),2):
        I=[i for i in range(d) if x[i]!=y[i]]
        for a,b in combinations(I,2):
            u,v=f(a),f(b)
            if u!=v: par[u]=v
    g={}
    for i in range(d): g.setdefault(f(i),[]).append(i)
    return list(g.values())
print("  %5s%7s%9s%16s%16s"%("d","|A|","n","components","median size"))
print("  "+"-"*56)
for d,a,lim in [(2,3,200),(3,2,200),(3,3,120),(4,2,120)]:
    n=0; nc=[]; sz=[]
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        n+=1
        C=axis_components(S,d)
        nc.append(len(C)); sz.append(int(np.median([len(c) for c in C])))
    if n: print("  %5d%7d%9d%16.2f%16.1f"%(d,a,n,np.mean(nc),np.mean(sz)))
print("""
  **The axis-interaction graph is usually CONNECTED** — one component. So
  that decomposition does not split anything, and the constraints really are
  global.
""")
print("="*88)
print("  BUT DOES THE ANSWER DECOMPOSE OVER Λ's OWN FIBRATION?")
print("="*88)
print("""
  §7.6: Λ = Σ_q A_q × B_q, and each A_q, B_q is closed with E = 0. **If
  reorderability decomposes over a fibration, then an index with a known
  fibration needs only its fibres solved.**
""")
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
import math as m
print("\n     Λ : ∏|A_i|! = %d"%int(np.prod([m.factorial(len(a)) for a in AX])))
Aidx=[0,1,2,3,7]; Bidx=[4,5,6]
Apart={tuple(x[i] for i in Aidx) for x in LAM}
Bpart={tuple(x[i] for i in Bidx) for x in LAM}
sa=int(np.prod([m.factorial(len({t[k] for t in Apart})) for k in range(len(Aidx))]))
sb=int(np.prod([m.factorial(len({t[k] for t in Bpart})) for k in range(len(Bidx))]))
print("     A-part alone : %d orderings      B-part alone : %d"%(sa,sb))
print("     product      : %d      **vs %d for the whole**"%(sa*sb,int(np.prod([m.factorial(len(a)) for a in AX]))))
print("="*88)
print("  AND THE GENERAL TEST: DOES A PRODUCT OF REORDERABLES REORDER?")
print("="*88)
ok=0; n=0; bad=[]
for _ in range(400):
    d1=2; d2=1
    A1=[list(range(random.randint(2,3))) for _ in range(d1)]
    c1=list(product(*A1)); X=set(random.sample(c1,random.randint(2,len(c1))))
    A2=[list(range(random.randint(2,3)))]
    Y=set(random.sample(list(product(*A2)),random.randint(1,len(A2[0]))))
    r1=reord(X,d1)
    if r1 is not True: continue
    P={tuple(list(x)+list(y)) for x in X for y in Y}
    Ap=alph(P,d1+d2)
    if any(len(z)<2 for z in Ap): continue
    n+=1
    rp=reord(P,d1+d2)
    ok+= (rp is True)
    if rp is not True and len(bad)<3: bad.append((sorted(X),sorted(Y)))
print("\n     X reorderable, Y a single axis : %d cases"%n)
print("     the PRODUCT X × Y reorderable  : %d  (%.0f%%)"%(ok,100*ok/max(n,1)))
if bad:
    print("\n     counterexamples:")
    for X,Y in bad: print("       X=%s  Y=%s"%(str(X)[:34],Y))
print("""
{0}
  WHAT THIS SAYS ABOUT 'MORE THAN ONE SOLUTION'
{0}
""".format("="*88))
print("""  **If products of reorderables are reorderable, then reorderability is
  COMPOSITIONAL**, and an index with a product structure needs only its
  factors solved. **That is more than one solution by construction — one per
  factor — and it is how Λ is built.**
""")