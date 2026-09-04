import numpy as np, random, math
from itertools import product, permutations, combinations
from collections import defaultdict
random.seed(599)
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
def sigk(S,d,k):
    """the agreement complex at level k — same form for every d"""
    Ss=set(S); out=[]
    for t in combinations(sorted(S),k):
        I=tuple(i for i in range(d) if len({x[i] for x in t})>1)
        if not I: continue
        j=tuple(max(x[i] for x in t) for i in range(d))
        m=tuple(min(x[i] for x in t) for i in range(d))
        inner=0
        for u,v in combinations(t,2):
            if tuple(max(u[i],v[i]) for i in range(d)) in Ss: inner+=1
            if tuple(min(u[i],v[i]) for i in range(d)) in Ss: inner+=1
        out.append((len(I),1 if j in Ss else 0,1 if m in Ss else 0,inner))
    return tuple(sorted(out))
def sig2(S,d):
    Ss=set(S); out=[]
    for x,y in combinations(sorted(S),2):
        I=tuple(i for i in range(d) if x[i]!=y[i])
        if not I: continue
        pat=[]
        for bits in product([0,1],repeat=len(I)):
            c=list(x)
            for t,i in enumerate(I): c[i]= y[i] if bits[t] else x[i]
            pat.append(1 if tuple(c) in Ss else 0)
        out.append((len(I),tuple(pat)))
    return tuple(sorted(out))
print("="*88)
print("  THE HIERARCHY — LEVEL BY LEVEL, SAME CONSTRUCTION")
print("="*88)
for d,a,lim in [(3,3,3000),(4,2,2200)]:
    print("\n  ---- d = %d, |A| = %d ----"%(d,a))
    data=[]
    for _ in range(lim):
        Ax=[list(range(a)) for _ in range(d)]
        cl=list(product(*Ax))
        S=set(random.sample(cl,random.randint(2,min(len(cl),9))))
        A=alph(S,d)
        if any(len(x)<2 for x in A): continue
        r=reord(S,d)
        if r is None: continue
        data.append((S,r))
    LEV=[("2",lambda S,dd: sig2(S,dd)),
         ("2+3",lambda S,dd: (sig2(S,dd),sigk(S,dd,3))),
         ("2+3+4",lambda S,dd: (sig2(S,dd),sigk(S,dd,3),sigk(S,dd,4))),
         ("2+3+4+5",lambda S,dd: (sig2(S,dd),sigk(S,dd,3),sigk(S,dd,4),sigk(S,dd,5)))]
    print("  %-12s%12s%16s%12s%14s"%("levels","classes","multi-instance","MIXED","purity"))
    print("  "+"-"*66)
    for nm,f in LEV:
        cls=defaultdict(list)
        for S,r in data: cls[f(S,d)].append(r)
        multi=[v for v in cls.values() if len(v)>1]
        mixed=[v for v in multi if len(set(v))>1]
        pur=1-len(mixed)/max(len(multi),1)
        print("  %-12s%12d%16d%12d%13.3f"%(nm,len(cls),len(multi),len(mixed),pur))
    print("     instances : %d"%len(data))
print("="*88)
print("  IS THE HIERARCHY CONVERGING?")
print("="*88)
print("""
  **The test that matters:** does MIXED fall to zero at some level, and does
  the level needed stay bounded as d grows? **If the level is bounded, the
  procedure is O(|X|^level) — polynomial, and dimension-free in form.**
""")
print("="*88)
print("  AND THE RESIDUAL CLASSES AT d = 3 — WHAT ARE THEY?")
print("="*88)
data=[]
for _ in range(3000):
    d=3; a=3
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,min(len(cl),9))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    r=reord(S,d)
    if r is None: continue
    data.append((S,r))
cls=defaultdict(list)
for S,r in data: cls[(sig2(S,3),sigk(S,3,3),sigk(S,3,4))].append((S,r))
mixed=[v for v in cls.values() if len({r for _,r in v})>1]
print("\n     mixed classes at levels 2+3+4 : %d"%len(mixed))
for grp in mixed[:3]:
    yes=[S for S,r in grp if r]; no=[S for S,r in grp if not r]
    if yes and no:
        print("\n        YES : %s"%str(sorted(yes[0]))[:56])
        print("        NO  : %s"%str(sorted(no[0]))[:56])
        print("        sizes %d vs %d    alphabets %s vs %s"%(len(yes[0]),len(no[0]),
              [len(x) for x in alph(yes[0],3)],[len(x) for x in alph(no[0],3)]))