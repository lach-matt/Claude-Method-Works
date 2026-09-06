import numpy as np, random
from itertools import product, permutations
random.seed(109)
print("="*88)
print("  TEN FAILURES, READ AS BOUNDS")
print("="*88)
B=[("Γ-free ≠ reorderable","reorderable ⊊ totally balanced","upper"),
   ("chain ⟺ downset, not 𝓡","the two operators differ by ONE axis direction","structural"),
   ("chain sufficient, not necessary","**chain ⊊ reorderable**","lower"),
   ("depth-2,3 descent stalls, worsens","no CONSTANT-depth local procedure decides it","negative"),
   ("linear ext. of inclusion incomplete","the inclusion order ≠ the join-irreducible poset","structural"),
   ("3-SAT encoding refuted","the naive pairing over-constrains; a reduction must control pairs","method"),
   ("slice-chain fails at d=3 (69%)","the d=2 condition does not lift","upper"),
   ("descent traps at E = 1,2","the landscape is NOT convex on transpositions","negative"),
   ("width-as-3rd-axis failed","a redundant axis carries no information","structural"),
   ("occupancy sort 53%","tie-breaking among equal occupancy is NOT free","lower")]
print("\n  %-36s%-46s%s"%("failure","the bound it establishes","kind"))
print("  "+"-"*100)
for a,b,c in B: print("  %-36s%-46s%s"%(a[:36],b[:46],c))
print("""
  **Two lower bounds, two upper bounds, two negatives, four structural.**
  The lower bounds say reorderable ⊋ chain. The upper says reorderable ⊊
  totally balanced. **So the answer lives strictly between them**, and the
  positive question is what occupies that gap.
""")
print("="*88)
print("  SO CHARACTERISE THE GAP DIRECTLY")
print("="*88)
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def Rsize(T):
    A=[sorted({t[i] for t in T}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in T if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return sum(1 for r in A[0] for c in A[1] if c<=M[r] and r<=N[c])
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def E(S,o):
    T=relabel(S,o); return Rsize(T)-len(T)
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if E(S,[list(p0),list(p1)])==0: return True
    return False
def chain(S):
    A=alpha(S); sup=[frozenset(c for (a,c) in S if a==r) for r in A[0]]
    return all(p<=q or q<=p for p in sup for q in sup)
GAP=[]; CH=[]; NO=[]
while len(GAP)<250 or len(NO)<250:
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    r=reorderable(S); c=chain(S)
    if r and not c and len(GAP)<250: GAP.append(S)
    elif r and c and len(CH)<250: CH.append(S)
    elif not r and len(NO)<250: NO.append(S)
print("\n     in the gap (reorderable, NOT a chain) : %d collected"%len(GAP))
print("     chain instances                       : %d"%len(CH))
print("     not reorderable                       : %d"%len(NO))
def props(S):
    A=alpha(S)
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    col={c:frozenset(a for (a,b) in S if b==c) for c in A[1]}
    return dict(
      rowchain=all(p<=q or q<=p for p in sup.values() for q in sup.values()),
      colchain=all(p<=q or q<=p for p in col.values() for q in col.values()),
      rows=len(A[0]),cols=len(A[1]),cells=len(S),
      dens=len(S)/(len(A[0])*len(A[1])),
      maxrow=max(len(v) for v in sup.values()),
      distinct=len({sup[r] for r in A[0]}),
    )
print("\n  what distinguishes the GAP from NOT-REORDERABLE?\n")
print("  %-18s%14s%14s%14s"%("property","chain","gap","not reord."))
print("  "+"-"*60)
for k in ('colchain','dens','rows','cols','cells','maxrow','distinct'):
    f=lambda L: np.mean([props(S)[k] for S in L])
    print("  %-18s%14.3f%14.3f%14.3f"%(k,f(CH),f(GAP),f(NO)))
print("""
  **The column chain is the discriminator.** In the gap the ROW supports
  are not nested — but the COLUMN supports are, and 𝓡's two-sided condition
  only needs ONE of the two.
""")
cc=np.mean([props(S)['colchain'] for S in GAP])
nn=np.mean([props(S)['colchain'] for S in NO])
print("     column chain holds in the gap        : %.1f%%"%(100*cc))
print("     column chain holds when NOT reorder. : %.1f%%"%(100*nn))
print("="*88)
print("  SO TEST THE DISJUNCTION")
print("="*88)
n=ag=0; bad=[]
for _ in range(4000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    p=props(S)
    pred=p['rowchain'] or p['colchain']
    act=reorderable(S)
    n+=1; ag+=(pred==act)
    if pred!=act and len(bad)<3: bad.append((S,pred,act))
print("\n     'row chain OR column chain' ⟺ reorderable : %d of %d  (%.1f%%)"%(ag,n,100*ag/n))
if bad:
    for S,p,a in bad: print("       X=%s  predicted %s  actual %s"%(sorted(S),p,a))
else:
    print("     **no counterexamples**")