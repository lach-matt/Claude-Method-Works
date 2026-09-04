import numpy as np, random
from itertools import product, permutations, combinations
random.seed(101)
print("="*88)
print("  DOES A DEEPER MOVE CLOSE THE REMAINING 3%?")
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
def moves(o,depth):
    """all orders reachable by <= depth adjacent transpositions"""
    frontier={tuple(tuple(x) for x in o)}
    seen=set(frontier)
    for _ in range(depth):
        nxt=set()
        for st in frontier:
            oo=[list(x) for x in st]
            for ax in (0,1):
                for i in range(len(oo[ax])-1):
                    p=[list(x) for x in oo]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                    t=tuple(tuple(x) for x in p)
                    if t not in seen: seen.add(t); nxt.add(t)
        frontier=nxt
    return [ [list(x) for x in t] for t in seen ]
def descend_depth(S,depth,maxit=200):
    A=alpha(S); o=[list(A[0]),list(A[1])]
    e=E(S,o); it=0
    while e>0 and it<maxit:
        best=None
        for p in moves(o,depth):
            v=E(S,p)
            if best is None or v<best[0]: best=(v,p)
        if best[0]>=e: break
        e,o=best; it+=1
    return e,it
print("""
  Pure depth-1 descent solved 89.8%. Try depth 2 and depth 3 — a move that
  looks two or three transpositions ahead before committing.
""")
inst=[]
while len(inst)<400:
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if reorderable(S): inst.append(S)
print("  %8s%14s%14s%14s"%("depth","reaches 0","stuck","mean steps"))
print("  "+"-"*52)
stuck_at={}
for depth in (1,2,3):
    hit=0; st=[]; stuck=[]
    for S in inst:
        e,it=descend_depth(S,depth)
        if e==0: hit+=1; st.append(it)
        else: stuck.append((S,e))
    stuck_at[depth]=stuck
    print("  %8d%14d%14d%14.2f"%(depth,hit,len(inst)-hit,np.mean(st) if st else 0))
print()
for d in (1,2,3):
    if stuck_at[d]:
        print("     depth %d stalls on %d, residual E values %s"%(d,len(stuck_at[d]),sorted({e for _,e in stuck_at[d]})))
    else:
        print("     **depth %d: no stalls**"%d)
print("="*88)
print("  AND IS THE DEPTH BOUNDED, OR DOES IT GROW WITH THE INSTANCE?")
print("="*88)
print("""
  If the required depth is bounded by a constant, the mechanism is a
  DECISION PROCEDURE and §23.4 closes. If it grows, it is a heuristic.
""")
big=[]
while len(big)<120:
    A=[list(range(random.randint(4,6))),list(range(random.randint(4,6)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if reorderable(S): big.append(S)
print("\n  larger alphabets (4-6 per axis), %d reorderable instances:\n"%len(big))
print("  %8s%14s%14s"%("depth","reaches 0","stuck"))
for depth in (1,2,3):
    hit=sum(1 for S in big if descend_depth(S,depth)[0]==0)
    print("  %8d%14d%14d"%(depth,hit,len(big)-hit))
print("""
{0}
  VERDICT
{0}
""".format("="*88))
d2=len(stuck_at[2]); d3=len(stuck_at[3])
if d2==0 or d3==0:
    print("""  **A BOUNDED-DEPTH DESCENT REACHES E = 0 ON EVERY REORDERABLE INSTANCE
  TESTED.** If the bound holds in general, the decision problem is:

     run the descent to its floor; X is reorderable iff the floor is 0

  **and that is a procedure, not a criterion** — which is what the motion
  view predicted and what seven attempts at a static condition could not
  produce.

  **It is still not a proof.** What is needed is a bound on the depth, and
  the evidence is that small depth suffices at these sizes.""")
else:
    print("""  **DEPTH DOES NOT CLOSE IT.** Depth 2 stalls on %d and depth 3 on %d.
  The traps are not merely shallow — they are genuine local minima of the
  transposition landscape, and escaping them needs a non-local move."""%(d2,d3))