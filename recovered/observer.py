from itertools import product, combinations
def E(S,d,ret=False):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    R={x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
    box=1
    for v in vals: box*=len(v)
    return (len(R)-len(S),sorted(R-S),box) if ret else len(R)-len(S)
def orders(S,d,NM,tgt):
    out=[]
    for j in range(d):
        if j==tgt: continue
        m={}
        for c in S: m[c[j]]=max(m.get(c[j],-99),c[tgt])
        out.append((NM[j],[m[v] for v in sorted(m)]))
    return out
def minsup(V,d,NM):
    mins=[]
    for r in (2,3,4,5):
        found=[]
        for idx in combinations(range(d),r):
            if any(set(m)<=set(idx) for m in mins): continue
            P={tuple(c[i] for i in idx) for c in V}
            if E(P,r)>0: found.append(idx)
        for idx in found:
            if not any(set(m)<set(idx) for m in mins): mins.append(idx)
        if found: return r,[[NM[i] for i in m] for m in found]
    return None,[]

print('  WITHOUT AN OBSERVER')
NM1=['THETA','KILLING','NET','STATE','ST','STATUS']
def cl1(x):
    x=list(x)
    if x[1]==0 and x[0]>0: x[0]=0
    return tuple(x)
V1={c for c in {cl1(x) for x in product(*[range(2)]*6)} if (c[1]==0) or (c[4]==0 and c[5]==1)}
e1,_,b1=E(V1,6,ret=True); r1,m1=minsup(V1,6,NM1)
print('     cells %d  box %d  E %d  minimal supports %s' % (len(V1),b1,e1,m1))
print('     order of ST:')
for a,s in orders(V1,6,NM1,4): print('        max ST given %-8s = %s' % (a,s))
print()

print('  WITH AN OBSERVER')
NM2=['THETA','KILLING','OBS','NET','STATE','ST']
# OBS 0 = an observer is adjoined (crossed product; the cut is specified relative to a clock)
#     1 = no observer; the cut is specified intrinsically
def cl2(x):
    x=list(x)
    if x[1]==0 and x[0]>0: x[0]=0          # Killing => non-expanding
    if x[2]==0 and x[5]>0: x[5]=0          # an observer FIXES the origin: ST ceases to be free
    if x[1]==0 and x[5]>0: x[5]=0          # a Killing field also fixes it
    return tuple(x)
A2={cl2(x) for x in product(*[range(2)]*6)}
A2={cl2(c) for c in A2}
# a positive translation exists iff the origin is fixed, by EITHER route
V2={c for c in A2 if c[5]==0}
e2,_,b2=E(V2,6,ret=True); r2,m2=minsup(V2,6,NM2)
print('     cells %d  box %d  E %d  minimal supports %s' % (len(V2),b2,e2,m2 if m2 else 'none'))
print('     order of ST:')
for a,s in orders(V2,6,NM2,5): print('        max ST given %-8s = %s' % (a,s))
print()
print('  NAMED CASES')
def mk(**kw):
    x=[0]*6
    for k,v in kw.items(): x[NM2.index(k)]=v
    return cl2(tuple(x))
for lab,c in [('Killing horizon, no observer needed',mk(OBS=1)),
              ('isolated horizon + observer (crossed product)',mk(KILLING=1,OBS=0)),
              ('isolated horizon, no observer',mk(KILLING=1,OBS=1)),
              ('expanding surface + observer',mk(KILLING=1,THETA=1,OBS=0)),
              ('expanding surface, no observer',mk(KILLING=1,THETA=1,OBS=1))]:
    print('     %-46s %s  %s' % (lab,str(list(c)),'admissible' if c in V2 else 'EXCLUDED'))