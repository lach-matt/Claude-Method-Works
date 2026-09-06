import random, math
from itertools import product, permutations, combinations
random.seed(701)
print("="*88)
print("  THE REDUCTION, WITH TAG AXES")
print("="*88)
print("""
  **The obstruction:** clauses sharing variables share corners, so encoding
  one alters another.

  **The structural fix:** give each clause its own TAG AXIS. Clause c on
  variables i,j,k gets a pair of cells differing on axes i,j,k AND on tag c.
  **Different clauses differ on different tags, so their boxes are disjoint** —
  no shared corners.

     variables n, clauses m  ->  d = n + m axes.  Polynomial in the instance.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def sublat_flip(S,d,s):
    Ss=S
    for x,y in combinations(sorted(S),2):
        j=tuple((min if s[i] else max)(x[i],y[i]) for i in range(d))
        m=tuple((max if s[i] else min)(x[i],y[i]) for i in range(d))
        if j not in Ss or m not in Ss: return False
    return True
def reord(S,d,cap=2**18):
    Ss=set(S)
    if 2**d>cap: return None
    for s in product([0,1],repeat=d):
        if sublat_flip(Ss,d,s): return True,s
    return False,None
def build(clauses,n):
    """each clause gets a tag axis; d = n + m"""
    m=len(clauses); d=n+m
    X=set()
    base=tuple([0]*d)
    X.add(base)
    for ci,(a,b,c) in enumerate(clauses):
        tag=n+ci
        ax=[abs(a)-1,abs(b)-1,abs(c)-1]
        sg=[a>0,b>0,c>0]
        x=[0]*d; y=[0]*d
        for t in range(3): y[ax[t]]=1
        y[tag]=1
        X.add(tuple(x)); X.add(tuple(y))
        # add every corner of the box EXCEPT those encoding a violating assignment
        for bits in product([0,1],repeat=4):
            cor=[0]*d
            for t in range(3):
                if bits[t]: cor[ax[t]]=1
            if bits[3]: cor[tag]=1
            # "exactly one literal true" : the number of positions where the
            # flip matches the literal's polarity must be exactly 1
            k=sum(1 for t in range(3) if bits[t]==(0 if sg[t] else 1))
            if k==1: continue          # this corner is FORBIDDEN -> omit it
            X.add(tuple(cor))
    return X,d
def sat_1in3(clauses,n):
    for bits in product([0,1],repeat=n):
        ok=True
        for a,b,c in clauses:
            k=0
            for l in (a,b,c):
                v=bits[abs(l)-1] if l>0 else 1-bits[abs(l)-1]
                k+=v
            if k!=1: ok=False; break
        if ok: return True
    return False
print("="*88)
print("  TEST ON SMALL 1-IN-3 INSTANCES")
print("="*88)
TESTS=[([(1,2,3)],3),
       ([(1,2,3),(1,2,3)],3),
       ([(1,2,3),(-1,2,3)],3),
       ([(1,2,3),(1,-2,3)],3),
       ([(1,2,3),(2,3,4)],4),
       ([(1,2,3),(-1,-2,-3)],3)]
print("\n  %30s%8s%14s%14s%10s"%("clauses","d","1-in-3 SAT","reorderable","match"))
print("  "+"-"*80)
ok=0; n_=0
for cl,nv in TESTS:
    X,d=build(cl,nv)
    A=alph(X,d)
    if any(len(a)<2 for a in A):
        print("  %30s%8d%14s%14s%10s"%(str(cl)[:30],d,"—","degenerate","—")); continue
    r=reord(X,d)
    if r is None:
        print("  %30s%8d%14s%14s%10s"%(str(cl)[:30],d,sat_1in3(cl,nv),"too large","—")); continue
    rr=r[0]; s=sat_1in3(cl,nv)
    n_+=1; ok+= (rr==s)
    print("  %30s%8d%14s%14s%10s"%(str(cl)[:30],d,s,rr,"YES" if rr==s else "**NO**"))
print("\n     matches : %d of %d"%(ok,n_))
print("="*88)
print("  RANDOM INSTANCES")
print("="*88)
tot=ag=0; bad=[]
for _ in range(200):
    nv=random.randint(3,4); m=random.randint(1,2)
    cl=[]
    for _ in range(m):
        vs=random.sample(range(1,nv+1),3)
        cl.append(tuple(v*random.choice([1,-1]) for v in vs))
    X,d=build(cl,nv)
    A=alph(X,d)
    if any(len(a)<2 for a in A): continue
    r=reord(X,d)
    if r is None: continue
    tot+=1
    s=sat_1in3(cl,nv)
    if r[0]==s: ag+=1
    elif len(bad)<3: bad.append((cl,s,r[0]))
print("\n     random instances %d      encoding tracks satisfiability : %d  (%.0f%%)"%(tot,ag,100*ag/max(tot,1)))
for cl,s,r in bad: print("        %s  sat=%s reord=%s"%(cl,s,r))