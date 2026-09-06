import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(541)
print("="*88)
print("  APPROACHES TO A 'REAL AND RARE' MISSING PIECE")
print("="*88)
print("""
  **1. From the rare cases.** Study only instances where the degeneracy
     exists. What distinguishes them?
  **2. From the boundary.** Instances barely reorderable vs barely not.
  **3. From a single cell.** How many cells must change to flip the answer?
  **4. From cell criticality.** Which cells are decisive, and are they
     identifiable without solving?

  **Run 3 first — it tests the 'single cell' reading directly.**
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
def reord(S,d,cap=200000):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
print("="*88)
print("  3.  DISTANCE TO REORDERABILITY — CELLS REMOVED")
print("="*88)
print("\n  %6s%8s%10s%12s%12s%12s%12s"%("d","|A|","n","dist 1","dist 2","dist 3+","median"))
print("  "+"-"*72)
for d,a,lim in [(2,3,260),(2,4,120),(3,2,260),(3,3,90)]:
    n=0; dist=[]
    for _ in range(lim):
        Ax=[list(range(a)) for _ in range(d)]
        cl=list(product(*Ax))
        S=set(random.sample(cl,random.randint(3,len(cl))))
        A=alph(S,d)
        if any(len(x)<2 for x in A): continue
        if reord(S,d) is not False: continue
        found=None
        for k in (1,2,3):
            for T in combinations(sorted(S),k):
                U=S-set(T); AU=alph(U,d)
                if any(len(x)<2 for x in AU): continue
                if reord(U,d) is True: found=k; break
            if found: break
        if found is None: found=4
        n+=1; dist.append(found)
    if n:
        print("  %6d%8d%10d%12d%12d%12d%12.1f"%(d,a,n,
            sum(1 for x in dist if x==1),sum(1 for x in dist if x==2),
            sum(1 for x in dist if x>=3),np.median(dist)))
print("""
  **If most non-reorderable instances are one cell away, the obstruction is
  a single cell** and the deciding structure is local.
""")
print("="*88)
print("  4.  ARE THE CRITICAL CELLS IDENTIFIABLE WITHOUT SOLVING?")
print("="*88)
print("""
  For each instance one cell away from reorderable, **is the critical cell
  distinguished by any local statistic?** Test its join/meet failure count
  against the non-critical cells'.
""")
crit=[]; noncrit=[]
for _ in range(900):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(3,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    if reord(S,d) is not False: continue
    Ss=set(S)
    def failcount(z):
        c=0
        for y in S:
            if y==z: continue
            if tuple(max(z[i],y[i]) for i in range(d)) not in Ss: c+=1
            if tuple(min(z[i],y[i]) for i in range(d)) not in Ss: c+=1
        return c
    for z in sorted(S):
        U=S-{z}; AU=alph(U,d)
        if any(len(x)<2 for x in AU): continue
        if reord(U,d) is True: crit.append(failcount(z))
        else: noncrit.append(failcount(z))
if crit and noncrit:
    print("\n     critical cells      : %d    mean join/meet failures %.2f"%(len(crit),np.mean(crit)))
    print("     non-critical cells  : %d    mean join/meet failures %.2f"%(len(noncrit),np.mean(noncrit)))
    print("     **separation        : %.2f×**"%(np.mean(crit)/max(np.mean(noncrit),1e-9)))
    thr=np.median(crit+noncrit)
    tp=sum(1 for c in crit if c>thr); fp=sum(1 for c in noncrit if c>thr)
    print("     at the median threshold : %d of %d critical caught, %d of %d non-critical wrongly flagged"
          %(tp,len(crit),fp,len(noncrit)))
else:
    print("\n     insufficient data")