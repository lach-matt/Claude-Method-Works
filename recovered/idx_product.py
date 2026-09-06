from itertools import product, combinations
# --- V2 theory ---
V2N=['CAUS','FIELD','INT','DIM']
# CAUS 0 causal 1 acausal | FIELD 0 scalar/gauge+fermion 1 other | INT 0 free 1 interacting
# DIM 0 d=2 1 d>2
V2R=[range(2),range(2),range(2),range(2)]
# --- V3 geometry (as built) ---
V3N=['FLAT','CONN','HYP','GEN','ASYM']
V3R=[range(3),range(2),range(2),range(2),range(2)]
# --- V4 algebra ---
V4N=['DET','ULOC','STAB','VACLOW','VACANN']
V4R=[range(2),range(2),range(2),range(2),range(2)]
# --- V1 fragment needed for Hartman: NEC_pt, X_exp, U_ghost, SD_obs
V1N=['NEC_pt','X_exp','U_ghost','SD_obs']
V1R=[range(5),range(4),range(2),range(2)]

NM=V1N+V3N
RNG=V1R+V3R
NEC,XE,UG,SO,FLAT,CONN,HYP,GEN,ASYM=range(9)

def close(x):
    x=list(x); g=True
    while g:
        g=False
        def up(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        def dn(i,v):
            nonlocal g
            if x[i]>v: x[i]=v; g=True
        # within V3
        if x[FLAT]==0: dn(CONN,0); dn(HYP,0); dn(GEN,0); dn(ASYM,0)
        if x[CONN]>=1: up(FLAT,1)
        if x[HYP]>=1:  up(FLAT,1)
        if x[ASYM]>=1: up(FLAT,2)
        # within V1
        if x[XE]>=3: up(NEC,2)
        if x[NEC]>=4: up(XE,1)
        return_flag=False
    return tuple(x)

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

def build(rules):
    allc={close(x) for x in product(*RNG)}
    allc={close(c) for c in allc}
    return {c for c in allc if all(r(c) for r in rules)}

print('  V1 x V3 PRODUCT, WITH THE CROSS-VOCABULARY EDGE')
print()
print('  the cross edge, stated three ways:')
CASES=[
 ('A  NEC_pt>=2 -> FLAT>=2   (curvature required)',
  lambda c: c[NEC]<2 or c[FLAT]>=2),
 ('B  NEC_pt>=2 -> FLAT>=1   (asymptotic curvature enough)',
  lambda c: c[NEC]<2 or c[FLAT]>=1),
 ('C  NEC_pt>=2 -> (FLAT>=2 or CONN=1 or ASYM=1)   curvature OR topology',
  lambda c: c[NEC]<2 or c[FLAT]>=2 or c[CONN]>=1 or c[ASYM]>=1),
]
for lab,rule in CASES:
    V=build([rule]); e,ex,box=E(V,9,ret=True)
    ar=None
    mins=[]
    for r in (2,3,4):
        found=[]
        for idx in combinations(range(9),r):
            if any(set(m)<=set(idx) for m in mins): continue
            P={tuple(c[i] for i in idx) for c in V}
            if E(P,r)>0: found.append(idx)
        for idx in found:
            if not any(set(m)<set(idx) for m in mins): mins.append(idx)
        if found: ar=r; break
    print('  %-58s cells %5d  E %4d  arity %s' % (lab,len(V),e,ar if ar else '-'))
    if mins:
        for m in mins[:2]: print('        minimal support: %s' % [NM[i] for i in m])
print()
print('  HARTMAN, COMPUTED RATHER THAN ASSERTED')
V=build([CASES[2][1]])
# Hartman: trigger NEC_pt>=2 ; jurisdiction FLAT=0 (Minkowski: also CONN=0, ASYM=0 by closure)
trig=[c for c in V if c[NEC]>=2]
jur =[c for c in V if c[FLAT]==0]
both=[c for c in V if c[NEC]>=2 and c[FLAT]==0]
print('     cells satisfying the trigger    (NEC_pt >= 2) : %d' % len(trig))
print('     cells satisfying the jurisdiction (FLAT = 0)  : %d' % len(jur))
print('     cells satisfying BOTH                          : %d' % len(both))
print('     -> Hartman is %s' % ('VACUOUS - it can never fire' if not both else 'ACTIVE on %d cells'%len(both)))
print()
print('  WHY, PRECISELY')
print('     FLAT = 0 forces CONN = 0 and ASYM = 0 by the V3 closure (Minkowski is')
print('     simply connected and non-compact). the cross edge then requires')
print('     FLAT >= 2 or CONN = 1 or ASYM = 1, all three excluded. the conjunction is empty.')
print()
print('     the earlier statement -- "ANEC violation requires curvature" -- is imprecise.')
print('     a FLAT spacetime with a compactified dimension violates the ANEC by the')
print('     Casimir effect (Wall 2010, on chronal geodesics). the correct antecedent is')
print('     curvature OR non-trivial topology, and that disjunction is what makes the')
print('     cross-vocabulary constraint TERNARY.')
print()
print('  CONSEQUENCE FOR THE SYSTEM')
print('     reading A (curvature only)   : binary cross-edge, arity 2 on the V1xV3 product')
print('     reading C (curvature or topology): arity %s' % ar)
print('     so the V1-V3 edge is not a simple forcing. it carries its own arity-3')
print('     obstruction, INDEPENDENT of the one inside V1.')
print('     -> the system has at least two arity-3 obstructions, not one.')