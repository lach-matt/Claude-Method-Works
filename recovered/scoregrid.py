import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(557)
print("="*90)
print("  THE GRID OF CELL STATISTICS — READ THE EMPTY CELLS")
print("="*90)
print("""
  %-22s%-16s%-16s%s
  %-22s%-16s%-16s%s
"""%("what is measured","pairwise","triple","other",
     "----------------","--------","------","-----"))
print("""     join failures          T4 (NEW)         T6 (NEW)         ·
     meet failures          T5 (NEW)         T6 (NEW)         ·
     join AND meet          T1 (tested 73%)  ·                ·
     corner deficiency      T2 (tested 58%)  ·                ·
     fibre singularity      ·                ·                T3 (66%)
     fibre containment      T7 (NEW)         ·                ·
     rank position          ·                ·                T8 (NEW)

  **T1 conflates join and meet.** §13.4's split measured them as DISTINCT
  mechanisms — 88% of gaps join-obstructed, 12% meet-obstructed, with a
  three-hundredfold separation in join-failure count. **Separating them is
  the first empty cell, and the grid says so.**
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
def T4(S,d,z):
    Ss=set(S)
    return sum(1 for y in S if y!=z and tuple(max(z[i],y[i]) for i in range(d)) not in Ss)
def T5(S,d,z):
    Ss=set(S)
    return sum(1 for y in S if y!=z and tuple(min(z[i],y[i]) for i in range(d)) not in Ss)
def T6(S,d,z):
    Ss=set(S); c=0
    for y,w in combinations([x for x in sorted(S) if x!=z],2):
        t=(z,y,w)
        if tuple(max(x[i] for x in t) for i in range(d)) not in Ss: c+=1
        if tuple(min(x[i] for x in t) for i in range(d)) not in Ss: c+=1
    return c
def T7(S,d,z):
    A=alph(S,d); c=0
    for i in range(d):
        Fz=frozenset(tuple(x[k] for k in range(d) if k!=i) for x in S if x[i]==z[i])
        for u in A[i]:
            if u==z[i]: continue
            Fu=frozenset(tuple(x[k] for k in range(d) if k!=i) for x in S if x[i]==u)
            if not (Fz<=Fu or Fu<=Fz): c+=1
    return c
def T8(S,d,z):
    rs=[sum(x) for x in S]
    return abs(sum(z)-np.mean(rs))
STATS=[("T1 join+meet",T1),("T4 join only",T4),("T5 meet only",T5),
       ("T6 triple",T6),("T7 fibre incomparability",T7),("T8 rank extremity",T8)]
res={n:[0,0,0] for n,_ in STATS}
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
        mx=max(sc.values()); tops={z for z in S if sc[z]==mx}
        res[nm][2]+=1
        if tops & crit: res[nm][1]+=1
        if len(tops)==1 and tops<=crit: res[nm][0]+=1
print("="*90)
print("  RESULTS")
print("="*90)
print("\n  %-28s%12s%18s%16s"%("statistic","instances","top is critical","uniquely"))
print("  "+"-"*76)
for nm,_ in STATS:
    t1,tk,tot=res[nm]
    print("  %-28s%12d%17d%%%15d%%"%(nm,tot,int(100*tk/max(tot,1)),int(100*t1/max(tot,1))))
print("="*90)
print("  AND DO THEY DISAGREE ENOUGH TO COMBINE?")
print("="*90)
n=0; anyhit=0; pairs={}
for _ in range(700):
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
    n+=1
    tops={}
    for nm,f in STATS:
        sc={z:f(S,d,z) for z in S}
        mx=max(sc.values()); tops[nm]={z for z in S if sc[z]==mx}
    union=set().union(*tops.values())
    if union & crit: anyhit+=1
    for a1,b1 in combinations([nm for nm,_ in STATS],2):
        k=(a1,b1); pairs.setdefault(k,0)
        if tops[a1]==tops[b1]: pairs[k]+=1
print("\n     **ANY of the six tops a critical cell : %d of %d  (%.0f%%)**"%(anyhit,n,100*anyhit/max(n,1)))
print("\n     pairwise agreement of the top sets:")
for (a1,b1),c in sorted(pairs.items(),key=lambda t:-t[1])[:6]:
    print("        %-26s %-26s %3d%%"%(a1,b1,int(100*c/max(n,1))))