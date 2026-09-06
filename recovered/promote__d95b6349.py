from itertools import product, combinations
def env_E(S,d,ret=False):
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
def nonmono(S,d,NM):
    bad=[]
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in S: m[c[j]]=max(m.get(c[j],-99),c[i])
            s=[m[v] for v in sorted(m)]
            if s!=sorted(s) and s!=sorted(s,reverse=True): bad.append((NM[i],NM[j],s))
    return bad
def minsup(V,d,NM):
    mins=[]
    for r in (2,3,4,5):
        found=[]
        for idx in combinations(range(d),r):
            if any(set(m)<=set(idx) for m in mins): continue
            P={tuple(c[i] for i in idx) for c in V}
            if env_E(P,r)>0: found.append(idx)
        for idx in found:
            if not any(set(m)<set(idx) for m in mins): mins.append(idx)
        if found: return r,[[NM[i] for i in m] for m in found]
    return None,[]

# ---------- BEFORE: geometry quotients ST ----------
NM1=['THETA','KILLING','NET','STATE','ST','STATUS']
def cl1(x):
    x=list(x)
    if x[1]==0 and x[0]>0: x[0]=0
    return tuple(x)
A1={cl1(x) for x in product(*[range(2)]*6)}
V1={c for c in A1 if (c[1]==0) or (c[4]==0 and c[5]==1)}
e1,ex1,b1=env_E(V1,6,ret=True); r1,m1=minsup(V1,6,NM1); nm1=nonmono(V1,6,NM1)
print('  BEFORE  (geometry quotients ST)')
print('     letters %s' % NM1)
print('     cells %d  box %d  E %d' % (len(V1),b1,e1))
print('     non-monotone pairs %d : %s' % (len(nm1),[(a,b) for a,b,_ in nm1]))
print('     minimal supports (size %s): %s' % (r1,m1))
print()

# ---------- AFTER: promotion. CORNER retains the modes; ST becomes a geometry coordinate ----------
NM2=['THETA','KILLING','CORNER','NET','STATE','ST']
# CORNER 0 = corner edge modes retained (ST physical in geometry)
#        1 = quotiented away (ST gauge in geometry)
def cl2(x):
    x=list(x)
    if x[1]==0 and x[0]>0: x[0]=0            # Killing => non-expanding
    if x[2]==0 and x[5]>0: x[5]=0            # modes retained => the origin is FIXED, not free
    return tuple(x)
A2={cl2(x) for x in product(*[range(2)]*6)}
A2={cl2(c) for c in A2}
# HSMI possible iff a positive translation exists:
#   either a Killing field supplies it, or the corner modes do.
V2={c for c in A2 if (c[1]==0) or (c[2]==0)}
e2,ex2,b2=env_E(V2,6,ret=True); r2,m2=minsup(V2,6,NM2); nm2=nonmono(V2,6,NM2)
print('  AFTER  (promotion: CORNER retains the modes)')
print('     letters %s' % NM2)
print('     cells %d  box %d  E %d' % (len(V2),b2,e2))
print('     non-monotone pairs %d : %s' % (len(nm2),[(a,b) for a,b,_ in nm2]))
print('     minimal supports (size %s): %s' % (r2,m2))
print()
print('  WHERE THE NAMED CASES SIT (AFTER)')
def mk(**kw):
    x=[0]*6
    for k,v in kw.items(): x[NM2.index(k)]=v
    return cl2(tuple(x))
for lab,c in [('Killing horizon',mk()),
              ('isolated horizon, modes retained',mk(KILLING=1)),
              ('isolated horizon, modes quotiented',mk(KILLING=1,CORNER=1)),
              ('expanding null surface, modes retained',mk(KILLING=1,THETA=1)),
              ('expanding, modes quotiented',mk(KILLING=1,THETA=1,CORNER=1))]:
    print('     %-42s %s  %s' % (lab,str(list(c)),'admissible' if c in V2 else 'EXCLUDED'))
print()
print('  ORDER OF ST IN EACH VOCABULARY (AFTER)')
for j,lab in [(0,'THETA'),(1,'KILLING'),(2,'CORNER'),(3,'NET')]:
    m={}
    for c in V2: m[c[j]]=max(m.get(c[j],-99),c[5])
    print('     max ST given %-8s = %s' % (lab,[m[v] for v in sorted(m)]))