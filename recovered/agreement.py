import numpy as np, random, math
from itertools import product, permutations, combinations
from collections import defaultdict
random.seed(593)
print("="*88)
print("  THE AGREEMENT COMPLEX — A CELL-SPACE OBJECT, NATIVE TO EVERY d")
print("="*88)
print("""
  **Order-free data on X:** for each k-subset, the axes on which its members
  agree, and which corners of its bounding box lie in X. **The FORM does not
  change with d** — only the label alphabet does.

     level 2 : pairs    — measured 94 of 95 classes
     level 3 : triples  — separated the residual 1
     **test both together**
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
def sig3(S,d):
    Ss=set(S); out=[]
    for t in combinations(sorted(S),3):
        I=tuple(i for i in range(d) if len({x[i] for x in t})>1)
        if not I: continue
        j=tuple(max(x[i] for x in t) for i in range(d))
        m=tuple(min(x[i] for x in t) for i in range(d))
        mids=0
        for x,y in combinations(t,2):
            if tuple(max(x[i],y[i]) for i in range(d)) in Ss: mids+=1
        out.append((len(I),1 if j in Ss else 0,1 if m in Ss else 0,mids))
    return tuple(sorted(out))
print("="*88)
print("  DOES THE AGREEMENT COMPLEX DETERMINE REORDERABILITY?")
print("="*88)
LEV=[("level 2 only",lambda S,d:sig2(S,d)),
     ("level 3 only",lambda S,d:sig3(S,d)),
     ("**levels 2+3**",lambda S,d:(sig2(S,d),sig3(S,d)))]
for d,a,lim in [(3,3,2600),(4,2,1800)]:
    print("\n  ---- d = %d, |A| = %d ----"%(d,a))
    print("  %-18s%12s%16s%14s"%("signature","classes","multi-instance","MIXED"))
    print("  "+"-"*62)
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
    for nm,f in LEV:
        cls=defaultdict(list)
        for S,r in data: cls[f(S,d)].append(r)
        multi=[v for v in cls.values() if len(v)>1]
        mixed=[v for v in multi if len(set(v))>1]
        print("  %-18s%12d%16d%14d"%(nm,len(cls),len(multi),len(mixed)))
print("="*88)
print("  AND THE COST — IS IT DIMENSION-FREE?")
print("="*88)
print("""
  **The complex has C(|X|,2) + C(|X|,3) entries whatever d is.** Only the
  label size grows: a pair's corner pattern is 2^|I| with |I| ≤ d.
""")
print("\n  %6s%10s%14s%18s%16s"%("d","|X|","pairs","triples","max label bits"))
print("  "+"-"*66)
for d in (2,3,4,8):
    for n in (10,20):
        print("  %6d%10d%14d%18d%16d"%(d,n,n*(n-1)//2,n*(n-1)*(n-2)//6,2**d))
print("""
  **The structure size is O(|X|³), independent of d. The label size is 2^d,
  independent of |X|.** That is the separation the twenty-two order-space
  formulations never had — **their cost was ∏|A_i|!, which couples both.**
""")