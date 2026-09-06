import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(449)
print("="*88)
print("  A MONOTONE CLOSURE — SEED-FREE BY CONSTRUCTION")
print("="*88)
print("""
  The loop failed because it STARTED from an order and iterated. **A
  monotone closure starts from the EMPTY relation and only ever adds
  relations that are FORCED** — so it has a unique fixed point and no seed.

     state : a partial order P_i on each axis (initially empty)
     step  : add u <_i v if assuming v <_i u contradicts the sublattice
             requirement, GIVEN what is already known
     stop  : fixed point
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
def reord(S,d,cap=10**6):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def closure(S,d,verbose=False):
    """monotone: add only forced relations; returns (P, contradiction)"""
    A=alph(S,d); Ss=set(S)
    P=[set() for _ in range(d)]           # (u,v) means u < v
    def lt(i,u,v):
        return (u,v) in P[i]
    def trans(i):
        ch=True
        while ch:
            ch=False
            for (a,b) in list(P[i]):
                for (c,e) in list(P[i]):
                    if b==c and (a,e) not in P[i]:
                        P[i].add((a,e)); ch=True
    def contradiction():
        for i in range(d):
            for (u,v) in P[i]:
                if (v,u) in P[i]: return True
        return False
    changed=True; rounds=0
    while changed and rounds<60:
        changed=False; rounds+=1
        for x,y in combinations(sorted(S),2):
            I=[i for i in range(d) if x[i]!=y[i]]
            if not I: continue
            # enumerate orientations consistent with P; if only one, adopt it
            cons=[]
            for bits in product([0,1],repeat=len(I)):
                good=True
                for t,i in enumerate(I):
                    hi = y[i] if bits[t] else x[i]
                    lo = x[i] if bits[t] else y[i]
                    if lt(i,hi,lo): good=False; break   # contradicts known
                if not good: continue
                j=list(x); m=list(x)
                for t,i in enumerate(I):
                    if bits[t]: j[i]=y[i]; m[i]=x[i]
                    else: j[i]=x[i]; m[i]=y[i]
                if tuple(j) in Ss and tuple(m) in Ss: cons.append(bits)
            if not cons: return P,True
            if len(cons)==1:
                bits=cons[0]
                for t,i in enumerate(I):
                    lo = x[i] if bits[t] else y[i]
                    hi = y[i] if bits[t] else x[i]
                    if (lo,hi) not in P[i]:
                        P[i].add((lo,hi)); changed=True
                for i in range(d): trans(i)
                if contradiction(): return P,True
    return P,contradiction()
def extend(S,d,P):
    """total orders consistent with P; try each"""
    A=alph(S,d); cand=[]
    for i in range(d):
        good=[p for p in permutations(A[i])
              if all(p.index(u)<p.index(v) for (u,v) in P[i])]
        if not good: return None
        cand.append(good)
    if int(np.prod([len(c) for c in cand]))>200000: return 'big'
    for ps in product(*cand):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
print("  %5s%7s%9s%14s%14s%14s%12s"%("d","|A|","n","reorderable","closure NO","closure+ext","exact"))
print("  "+"-"*80)
for d,a,lim in [(2,3,180),(2,4,90),(3,2,180),(3,3,70)]:
    n=r=cn=ce=ex=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        rr=reord(S,d)
        if rr is None: continue
        n+=1; r+=rr
        P,bad=closure(S,d)
        if bad:
            cn+=1; ex+= (rr==False); continue
        e=extend(S,d,P)
        if e=='big': continue
        ce+= (e is True)
        ex+= ((e is True)==rr)
    print("  %5d%7d%9d%14d%14d%14d%12d"%(d,a,n,r,cn,ce,ex))
print("""
  **'closure NO' must never fire on a reorderable instance** — it only adds
  forced relations. **'exact' is the score.**
""")