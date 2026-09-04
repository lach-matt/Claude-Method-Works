import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(547)
print("="*88)
print("  THREE LOCAL STATISTICS FOR THE CRITICAL CELL")
print("="*88)
print("""
  **T1 — join/meet failure count.** How many pairs (z,y) have an absent join
  or meet. The direct consequence of the lattice condition.

  **T2 — corner deficiency.** For each pair containing z, how many corners of
  their box are absent. **A different mechanism: this is the CSP's constraint
  weight, not the lattice's failure count.**

  **T3 — fibre singularity.** Is z the sole occupant of a value on some axis?
  **A structural mechanism: a value with one cell pins that value's position
  and cannot be traded away.**

  Score every cell by each, and ask whether the CRITICAL cell ranks first.
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
def reord(S,d,cap=40000):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def T1(S,d,z):
    Ss=set(S); c=0
    for y in S:
        if y==z: continue
        if tuple(max(z[i],y[i]) for i in range(d)) not in Ss: c+=1
        if tuple(min(z[i],y[i]) for i in range(d)) not in Ss: c+=1
    return c
def T2(S,d,z):
    Ss=set(S); c=0
    for y in S:
        if y==z: continue
        I=[i for i in range(d) if z[i]!=y[i]]
        for bits in product([0,1],repeat=len(I)):
            w=list(z)
            for t,i in enumerate(I):
                if bits[t]: w[i]=y[i]
            if tuple(w) not in Ss: c+=1
    return c
def T3(S,d,z):
    A=alph(S,d); c=0
    for i in range(d):
        if sum(1 for x in S if x[i]==z[i])==1: c+=1
    return c
STATS=[("T1 join/meet failures",T1),("T2 corner deficiency",T2),("T3 fibre singularity",T3)]
res={n:[0,0,0] for n,_ in STATS}   # [top1, topk, total]
N=0
for _ in range(900):
    d=3; a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(3,min(len(cl),7))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    if reord(S,d) is not False: continue
    crit=set()
    for z in sorted(S):
        U=S-{z}; AU=alph(U,d)
        if any(len(x)<2 for x in AU): continue
        if reord(U,d) is True: crit.add(z)
    if not crit: continue
    N+=1
    for nm,f in STATS:
        sc={z:f(S,d,z) for z in S}
        mx=max(sc.values())
        tops={z for z in S if sc[z]==mx}
        res[nm][2]+=1
        if tops & crit: res[nm][1]+=1
        if len(tops)==1 and tops<=crit: res[nm][0]+=1
print("  %-24s%12s%16s%16s"%("statistic","instances","top score is a","uniquely so"))
print("  %-24s%12s%16s%16s"%("","","critical cell",""))
print("  "+"-"*70)
for nm,_ in STATS:
    t1,tk,tot=res[nm]
    print("  %-24s%12d%15d%%%15d%%"%(nm,tot,int(100*tk/max(tot,1)),int(100*t1/max(tot,1))))
print("\n     non-reorderable instances with a critical cell : %d"%N)
print("="*88)
print("  AND THE PROCEDURE THE BEST ONE IMPLIES")
print("="*88)
best=max(STATS,key=lambda s:res[s[0]][1])
print("""
  **score each cell · remove the highest · recurse until reorderable**

  If the top-scoring cell is critical, the procedure terminates in ≤ |X|
  steps, each O(|X|²). **Test it end to end with %s.**
"""%best[0])
def procedure(S,d,f,maxit=12):
    cur=set(S); it=0
    while it<maxit:
        r=reord(cur,d)
        if r is True: return True,it
        if r is None: return None,it
        sc={z:f(cur,d,z) for z in cur}
        z=max(sc,key=lambda k:(sc[k],k))
        cur=cur-{z}
        A=alph(cur,d)
        if len(cur)<2 or any(len(x)<2 for x in A): return False,it
        it+=1
    return False,it
n=ok=0; steps=[]
for _ in range(500):
    d=3; a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(3,min(len(cl),7))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    if reord(S,d) is not False: continue
    # true minimum distance
    true=None
    for k in (1,2,3):
        for T in combinations(sorted(S),k):
            U=S-set(T); AU=alph(U,d)
            if any(len(x)<2 for x in AU): continue
            if reord(U,d) is True: true=k; break
        if true: break
    if true is None: continue
    v,it=procedure(S,d,best[1])
    if v is None: continue
    n+=1
    if v and it==true: ok+=1
    steps.append((it,true))
print("     instances %d      greedy removal reached the TRUE minimum : %d  (%.0f%%)"
      %(n,ok,100*ok/max(n,1)))
if steps:
    print("     mean greedy steps %.2f   mean true distance %.2f"%(np.mean([s[0] for s in steps]),np.mean([s[1] for s in steps])))