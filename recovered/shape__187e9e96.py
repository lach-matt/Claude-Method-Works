import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(563)
print("="*88)
print("  THE SHAPE, DEFINED")
print("="*88)
print("""
  **T7(z) = the number of (axis, value) pairs whose fibre is INCOMPARABLE to
  z's own fibre on that axis.**

  Immediate consequences to check:

     · T7(z) = 0 for every z  <=>  every fibre pair is comparable
                              <=>  the fibre-chain condition
                              **=> reorderable** (sufficient, measured)

     · so ΣT7 is a MEASURE of how far X is from the chain condition, and
       the cells with T7 > 0 are where the obstruction lives

  **DEFINITION.** shape(X) = the multiset {T7(z) : z ∈ X}.
  **CLAIM.** shape(X) = {0,0,…,0}  =>  X reorderable.
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
def reord(S,d,cap=60000):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def fib(S,d,i,u): return frozenset(tuple(x[k] for k in range(d) if k!=i) for x in S if x[i]==u)
def T7(S,d,z):
    A=alph(S,d); c=0
    for i in range(d):
        Fz=fib(S,d,i,z[i])
        for u in A[i]:
            if u==z[i]: continue
            Fu=fib(S,d,i,u)
            if not (Fz<=Fu or Fu<=Fz): c+=1
    return c
def shape(S,d): return sorted(T7(S,d,z) for z in S)
print("="*88)
print("  TEST 1 — DOES shape = ALL ZEROS IMPLY REORDERABLE?")
print("="*88)
print("\n  %6s%7s%9s%14s%18s%14s"%("d","|A|","n","shape all 0","of those reord.","violations"))
print("  "+"-"*72)
for d,a,lim in [(2,3,300),(2,4,150),(3,2,300),(3,3,120),(4,2,120)]:
    n=z=zr=0
    for _ in range(lim):
        Ax=[list(range(a)) for _ in range(d)]
        cl=list(product(*Ax))
        S=set(random.sample(cl,random.randint(2,len(cl))))
        A=alph(S,d)
        if any(len(x)<2 for x in A): continue
        r=reord(S,d)
        if r is None: continue
        n+=1
        sh=shape(S,d)
        if max(sh)==0:
            z+=1; zr+= (r is True)
    print("  %6d%7d%9d%14d%18d%14d"%(d,a,n,z,zr,z-zr))
print("="*88)
print("  TEST 2 — DOES THE SHAPE PREDICT REORDERABILITY IN GENERAL?")
print("="*88)
print("""
  Group instances by max(shape) and measure the reorderable fraction.
""")
buck={}
for _ in range(2500):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    r=reord(S,d)
    if r is None: continue
    m=max(shape(S,d))
    buck.setdefault(m,[0,0])
    buck[m][0]+=1; buck[m][1]+= (r is True)
print("\n  %12s%10s%14s%14s"%("max T7","n","reorderable","rate"))
print("  "+"-"*52)
for m in sorted(buck):
    t,rr=buck[m]
    if t>=8: print("  %12d%10d%14d%13.3f"%(m,t,rr,rr/t))
print("="*88)
print("  TEST 3 — AND ΣT7 AS A DISTANCE")
print("="*88)
rows=[]
for _ in range(700):
    d=3; a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(3,min(len(cl),7))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    r=reord(S,d)
    if r is not False: continue
    dist=None
    for k in (1,2,3):
        for T in combinations(sorted(S),k):
            U=S-set(T); AU=alph(U,d)
            if any(len(x)<2 for x in AU): continue
            if reord(U,d) is True: dist=k; break
        if dist: break
    if dist is None: continue
    rows.append((sum(shape(S,d)),dist))
if rows:
    s=np.array([r[0] for r in rows],float); dd=np.array([r[1] for r in rows],float)
    print("\n     instances %d"%len(rows))
    print("     corr(ΣT7, cell distance) : %+.3f"%np.corrcoef(s,dd)[0,1])
    for k in sorted(set(dd)):
        v=s[dd==k]
        if len(v)>=5: print("        distance %d : mean ΣT7 %.1f   n=%d"%(int(k),v.mean(),len(v)))