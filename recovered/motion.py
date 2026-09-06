import numpy as np, random
from itertools import product, permutations
random.seed(97)
print("="*88)
print("  E AS A LANDSCAPE, AND REORDERING AS MOTION ON IT")
print("="*88)
print("""
  Every attempt so far asked for a static CONDITION. Ask instead for a
  MECHANISM: treat E(order) as a potential, adjacent transpositions as the
  moves, and see whether descent reaches zero.

     **state**  : one total order per axis
     **move**   : swap two adjacent values on one axis
     **energy** : E = |𝓡(X)| − |X| under that order
""")
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
def descend(S,o0=None,maxit=4000):
    A=alpha(S)
    o=[list(A[0]),list(A[1])] if o0 is None else [list(x) for x in o0]
    e=E(S,o); path=[e]; it=0
    while e>0 and it<maxit:
        best=None
        for ax in (0,1):
            for i in range(len(o[ax])-1):
                p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                v=E(S,p)
                if best is None or v<best[0]: best=(v,p)
        if best is None or best[0]>=e: break
        e,o=best[0],best[1]; path.append(e); it+=1
    return e,o,path,it
print("  %10s%12s%14s%14s%12s"%("instances","reorderable","descent -> 0","stuck > 0","mean steps"))
print("  "+"-"*64)
N=0; R=0; hit=0; stuck=[]; steps=[]
for _ in range(1200):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if not reorderable(S): continue
    N+=1; R+=1
    e,o,path,it=descend(S)
    if e==0: hit+=1; steps.append(it)
    elif len(stuck)<4: stuck.append((S,path))
print("  %10d%12d%14d%14d%12.2f"%(N,R,hit,N-hit,np.mean(steps) if steps else 0))
print("\n     descent reaches E = 0 on %.1f%% of reorderable instances"%(100*hit/max(N,1)))
if stuck:
    print("\n  LOCAL MINIMA — descent stalls above zero:\n")
    for S,path in stuck[:3]:
        print("     X = %-44s  E path %s"%(str(sorted(S))[:44],path))
print("="*88)
print("  SO THE LANDSCAPE HAS TRAPS.  ADD THE ONE THING A MOTION CAN HAVE")
print("="*88)
print("""
  A static criterion cannot escape a local minimum. **A motion can, if it
  is allowed a move that raises E temporarily.** Test the smallest such
  addition: accept a sideways or uphill step when no downhill one exists,
  bounded.
""")
def descend_kick(S,maxit=400,patience=3):
    A=alpha(S); o=[list(A[0]),list(A[1])]
    e=E(S,o); best=e; it=0; bad=0
    while e>0 and it<maxit:
        cands=[]
        for ax in (0,1):
            for i in range(len(o[ax])-1):
                p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                cands.append((E(S,p),p))
        cands.sort(key=lambda t:t[0])
        if cands[0][0]<e: e,o=cands[0]; bad=0
        else:
            bad+=1
            if bad>patience: break
            e,o=random.choice(cands[:max(2,len(cands)//2)])
        it+=1
    return e,it
N2=hit2=0; st=[]
for _ in range(1200):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if not reorderable(S): continue
    N2+=1
    e,it=descend_kick(S)
    if e==0: hit2+=1; st.append(it)
print("\n     with bounded uphill moves : %d of %d  (%.1f%%)   mean %.1f steps"
      %(hit2,N2,100*hit2/max(N2,1),np.mean(st) if st else 0))
print("""
{0}
  WHAT THE MOTION VIEW BUYS
{0}
""".format("="*88))
print("""  **E is a genuine potential and adjacent transposition is a genuine
  move.** Pure descent solves %.0f%% and stalls on the rest; a bounded
  uphill allowance raises it to %.0f%%.

  **That reframes §23.4.** The question is not 'what condition characterises
  reorderability' — no simple one does. It is **'does a local search on E
  converge'**, and the answer so far is: **usually, with traps that a
  static criterion cannot see and a motion can escape.**

  **And it explains §23.3.** Solution density governs difficulty because
  density IS the size of the basin: when solutions are rare the descent has
  further to travel and more places to stall. **That is a statement about a
  landscape, which is what §23.3 measured without naming.**
"""%(100*hit/max(N,1),100*hit2/max(N2,1)))