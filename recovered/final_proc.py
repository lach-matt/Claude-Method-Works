import numpy as np, random, math, time
from itertools import product, permutations, combinations
random.seed(457)
print("="*88)
print("  THE QUESTION IN STEP 2, AND ITS ELEMENTS")
print("="*88)
print("""
  **Question.** Must the orientations be enumerated?

  **Elements.**
     · an orientation matters only if BOTH its corners lie in X
     · every such corner is a CELL of X
     · so the orientations that matter are indexed by cells, not by bits

  **Answer.** Iterate over X ∩ box(x,y). For each cell z there that agrees
  with x or y on every axis, z is a candidate JOIN; its complementary
  corner is the forced MEET. **O(|X|) per pair, not O(2^k).**
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
def reord_bf(S,d,cap=10**6):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def orientations_naive(S,x,y,d):
    Ss=S; I=[i for i in range(d) if x[i]!=y[i]]
    out=[]
    for bits in product([0,1],repeat=len(I)):
        j=list(x); m=list(x)
        for t,i in enumerate(I):
            if bits[t]: j[i]=y[i]; m[i]=x[i]
            else: j[i]=x[i]; m[i]=y[i]
        if tuple(j) in Ss and tuple(m) in Ss: out.append(tuple(bits))
    return set(out)
def orientations_cells(S,x,y,d):
    """iterate over CELLS of X inside the box — O(|X|) not O(2^k)"""
    I=[i for i in range(d) if x[i]!=y[i]]
    out=set()
    for z in S:
        ok=True
        for i in range(d):
            if i in I:
                if z[i] not in (x[i],y[i]): ok=False; break
            elif z[i]!=x[i]: ok=False; break
        if not ok: continue
        bits=tuple(1 if z[i]==y[i] else 0 for i in I)
        m=list(x)
        for t,i in enumerate(I): m[i]= x[i] if bits[t] else y[i]
        if tuple(m) in S: out.add(bits)
    return out
print("  VERIFY THE TWO AGREE\n")
n=ag=0
for _ in range(300):
    d=random.choice([2,3,4]); a=random.choice([2,3])
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(2,len(cells))))
    for x,y in list(combinations(sorted(S),2))[:12]:
        n+=1
        ag+= (orientations_naive(S,x,y,d)==orientations_cells(S,x,y,d))
print("     pairs compared : %d      agree : %d  (%.1f%%)"%(n,ag,100*ag/max(n,1)))
print("="*88)
print("  THE PROCEDURE, WITH BOTH FIXES")
print("="*88)
def closure(S,d):
    A=alph(S,d); P=[set() for _ in range(d)]
    def trans(i):
        ch=True
        while ch:
            ch=False
            for (a,b) in list(P[i]):
                for (c,e) in list(P[i]):
                    if b==c and (a,e) not in P[i]: P[i].add((a,e)); ch=True
    def bad():
        return any((v,u) in P[i] for i in range(d) for (u,v) in P[i])
    changed=True; rnd=0
    while changed and rnd<80:
        changed=False; rnd+=1
        for x,y in combinations(sorted(S),2):
            I=[i for i in range(d) if x[i]!=y[i]]
            if not I: continue
            cand=orientations_cells(S,x,y,d)
            cand={b for b in cand
                  if not any(( (y[i] if b[t] else x[i]), (x[i] if b[t] else y[i]) ) in P[i]
                             for t,i in enumerate(I))}
            if not cand: return P,True
            if len(cand)==1:
                b=list(cand)[0]
                for t,i in enumerate(I):
                    lo = x[i] if b[t] else y[i]; hi = y[i] if b[t] else x[i]
                    if (lo,hi) not in P[i]: P[i].add((lo,hi)); changed=True
                for i in range(d): trans(i)
                if bad(): return P,True
    return P,bad()
def extension_count(S,d,P):
    A=alph(S,d); c=1
    for i in range(d):
        g=sum(1 for p in permutations(A[i]) if all(p.index(u)<p.index(v) for (u,v) in P[i]))
        c*=g
    return c
def decide(S,d,cap=200000):
    P,b=closure(S,d)
    if b: return False,0
    A=alph(S,d); cand=[]
    for i in range(d):
        g=[p for p in permutations(A[i]) if all(p.index(u)<p.index(v) for (u,v) in P[i])]
        if not g: return False,0
        cand.append(g)
    tot=int(np.prod([len(c) for c in cand]))
    if tot>cap: return None,tot
    for ps in product(*cand):
        if lat(relab(S,[list(p) for p in ps],d),d): return True,tot
    return False,tot
print("\n  %5s%7s%8s%13s%12s%16s%14s"%("d","|A|","n","reorderable","exact","median ext","max ext"))
print("  "+"-"*76)
for d,a,lim in [(2,3,180),(2,4,90),(3,2,180),(3,3,70),(4,2,70)]:
    n=r=ex=0; sz=[]
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        rr=reord_bf(S,d)
        if rr is None: continue
        n+=1; r+=rr
        v,t=decide(S,d); sz.append(t)
        if v is not None: ex+= (v==rr)
    print("  %5d%7d%8d%13d%12d%16d%14d"%(d,a,n,r,ex,int(np.median(sz)) if sz else 0,max(sz) if sz else 0))
print("""
  **'max ext' bounds step 4** — the number of total orders left after the
  closure. If it is small, the search is bounded in practice.
""")