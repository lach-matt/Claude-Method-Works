import pickle, numpy as np
from itertools import combinations, product
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
res=pickle.load(open('/home/claude/stage/s2.pkl','rb'))
cells=D['cells']; tab=D['tab']; NF=D['nforms']; n=len(cells)
print("="*88)
print("  THE CHARACTERISTICS AS COORDINATES — AN INDEX OF INSTANCES")
print("="*88)
print("""
  **Each form count is a coordinate. Each signature class is a cell.** So the
  observed classes are a cell set in a 19-dimensional box, and the question
  the book always asks applies: **is the reorderable region CLOSED?**
""")
DUAL=[(0,7),(2,8),(3,9),(4,11),(5,10),(6,12),(16,17)]
merge={}
for a,b in DUAL: merge[b]=a
keep=[j for j in range(NF) if j not in merge]
print("     raw coordinates      : %d"%NF)
print("     after duality merge  : %d"%len(keep))
cls={}
for mask in range(1,1<<n):
    v=res[mask]
    if not v: continue
    idx=[i for i in range(n) if mask>>i & 1]
    c=[0]*NF
    for T in combinations(idx,3): c[tab[T]]+=1
    for b,a in merge.items(): c[a]+=c[b]
    k=tuple(c[j] for j in keep)
    if k in cls and cls[k]!=v: cls[k]=-1
    elif k not in cls: cls[k]=v
mixed=sum(1 for v in cls.values() if v==-1)
Y={k for k,v in cls.items() if v==2}
N={k for k,v in cls.items() if v==1}
print("\n     classes after merge  : %d      MIXED : %d"%(len(cls),mixed))
print("     YES classes          : %d      NO : %d"%(len(Y),len(N)))
d=len(keep)
def Rop(S,d):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                cc=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(cc) if cc else -1); f[v]=run
            ph[(i,j)]=f
    box=1
    for a in A: box*=len(a)
    if box>4*10**6: return None,box
    adm={x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
         for i in range(d) for j in range(d) if i!=j)}
    return adm,box
print("="*88)
print("  IS THE YES REGION CLOSED IN CHARACTERISTIC SPACE?")
print("="*88)
for nm,S in [("YES region",Y),("NO region",N)]:
    A=[sorted({x[i] for x in S}) for i in range(d)]
    adm,box=Rop(S,d)
    print("\n     %s : %d cells   box %d"%(nm,len(S),box))
    print("        alphabet sizes : %s"%[len(a) for a in A])
    if adm is None:
        print("        box too large to enumerate (%d)"%box)
    else:
        print("        **E(X) = %d**"%(len(adm)-len(S)))
print("="*88)
print("  AND IS IT A SUBLATTICE?  (join and meet on count vectors)")
print("="*88)
def sublat(S,d,cap=400000):
    Ss=set(S); Ls=sorted(S); jf=mf=0; t=0
    for x,y in combinations(Ls,2):
        t+=1
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: jf+=1
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: mf+=1
        if t>=cap: break
    return t,jf,mf
for nm,S in [("YES region",Y),("NO region",N)]:
    t,jf,mf=sublat(S,d)
    print("\n     %s : %d pairs tested"%(nm,t))
    print("        join failures %d   meet failures %d   **sublattice : %s**"%(jf,mf,jf==0 and mf==0))
print("="*88)
print("  AND IS IT A DOWNSET — PROPERLY TESTED THIS TIME")
print("="*88)
print("""
  **The earlier test was vacuous** — it decremented coordinates and looked for
  the result among OBSERVED classes, and one-step decrements rarely land on
  one. **Test instead: for each YES class, is every observed class BELOW it
  also YES?**
""")
allk=set(cls)
below_tested=0; below_bad=0
Ylist=sorted(Y)[:150]; alll=sorted(allk)
for y in Ylist:
    for z in alll:
        if z!=y and all(z[i]<=y[i] for i in range(d)):
            below_tested+=1
            if cls[z]!=2: below_bad+=1
print("     YES classes sampled : %d"%len(Ylist))
print("     observed classes strictly below them : %d"%below_tested)
print("     of those, NOT YES : %d"%below_bad)
print("     **downset : %s**"%(below_bad==0 if below_tested else "no data"))