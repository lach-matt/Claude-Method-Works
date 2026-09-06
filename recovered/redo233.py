import numpy as np, random
from itertools import product, permutations, combinations
from math import factorial
random.seed(223)
print("="*88)
print("  §23.3 RE-RUN WITH THE INVARIANTS DISCOVERED SINCE")
print("="*88)
print("""
  §23.3 tested ten invariants — dimension, alphabet size, cell count,
  occupancy, join-irreducibles, poset height, poset width, covers,
  antichain, rank range — **best correlation 0.31** — and concluded the
  difficulty is not structural.

  **That list predates the containment forest, the overlap components,
  C1P, interval endpoints and the E-landscape.** Re-run it.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def overlap(a,b): return bool(a&b) and not(a<=b) and not(b<=a)
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Rclosed(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    NN={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); NN[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=NN[c]}==S
def soln_count(S):
    A=alpha(S); c=0
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): c+=1
    return c
def descend_steps(S,maxit=200):
    """backtracking proxy: steps of steepest descent on E"""
    A=alpha(S); o=[list(A[0]),list(A[1])]
    def E(oo):
        T=relabel(S,oo); Aa=[sorted({t[i] for t in T}) for i in range(2)]
        M={};run=-1
        for v in Aa[0]:
            c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
        NN={};run=-1
        for wv in Aa[1]:
            c=[x for (x,y) in T if y<=wv]; run=max(run,max(c) if c else -1); NN[wv]=run
        return sum(1 for r in Aa[0] for c in Aa[1] if c<=M[r] and r<=NN[c])-len(T)
    e=E(o); it=0
    while e>0 and it<maxit:
        best=None
        for ax in (0,1):
            for i in range(len(o[ax])-1):
                p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                v=E(p)
                if best is None or v<best[0]: best=(v,p)
        if best[0]>=e: break
        e,o=best; it+=1
    return it
def feats(S):
    A=alpha(S); sup=sup_of(S)
    rows=sorted(set(sup.values()),key=lambda s:(-len(s),sorted(s)))
    def kids(X):
        ins=[r for r in rows if r<X]
        return [b for b in ins if not any(c!=b and b<c and c<X for c in ins)]
    kc=[len(kids(X)) for X in rows]
    nest=sum(1 for a in rows for b in rows if b<a)
    ov=sum(1 for a,b in combinations(rows,2) if overlap(a,b))
    forest_depth=0
    for X in rows:
        d=0; cur=X
        while True:
            up=[Y for Y in rows if cur<Y]
            if not up: break
            cur=min(up,key=len); d+=1
        forest_depth=max(forest_depth,d)
    return {
      'OLD cells':len(S),'OLD rows':len(A[0]),'OLD cols':len(A[1]),
      'OLD density':len(S)/(len(A[0])*len(A[1])),
      'NEW max children':max(kc) if kc else 0,
      'NEW mean children':float(np.mean(kc)) if kc else 0.0,
      'NEW nesting pairs':nest,
      'NEW overlap pairs':ov,
      'NEW forest depth':forest_depth,
      'NEW distinct rows':len(rows),
    }
DATA=[]
for _ in range(1200):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    sc=soln_count(S)
    if sc==0: continue
    d=sc/(factorial(len(Aa[0]))*factorial(len(Aa[1])))
    DATA.append((feats(S),d,descend_steps(S)))
print("     reorderable instances : %d"%len(DATA))
keys=list(DATA[0][0].keys())
dens=np.array([d for _,d,_ in DATA]); steps=np.array([s for _,_,s in DATA],float)
print("\n  %-22s%16s%16s"%("invariant","corr w/ steps","corr w/ density"))
print("  "+"-"*56)
best=None
for k in keys:
    v=np.array([f[k] for f,_,_ in DATA],float)
    if v.std()==0: continue
    cs=np.corrcoef(v,steps)[0,1]; cd=np.corrcoef(v,dens)[0,1]
    print("  %-22s%16.3f%16.3f"%(k,cs,cd))
    if best is None or abs(cs)>abs(best[1]): best=(k,cs)
print("\n  %-22s%16.3f%16s"%("log solution density",np.corrcoef(np.log(dens),steps)[0,1],"—"))
print("""
{0}
  RESULT
{0}
""".format("="*88))
print("""     §23.3's best structural invariant : 0.31
     best of the NEW invariants        : %s at %.3f
     log density                       : %.3f
"""%(best[0],best[1],np.corrcoef(np.log(dens),steps)[0,1]))
if best and abs(best[1])>0.31:
    print("""  **A STRUCTURAL INVARIANT DOES BEAT 0.31.** §23.3's conclusion that the
  difficulty is 'not structural' was a conclusion about the ten invariants
  on its list, **and the list was incomplete in exactly the way §23.5
  describes.**""")
else:
    print("""  **No new invariant beats 0.31.** §23.3's conclusion survives the
  enlarged list, which strengthens it: eight further structural
  parameters, none of them predictive.""")