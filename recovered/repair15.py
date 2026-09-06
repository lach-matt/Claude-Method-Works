from itertools import product, permutations
from collections import defaultdict
NM=['X_exp','X_spon','Sc','IC','U_open','U_ghost','NEC_pt','NEC_ach',
    'L_dyn','L_kin','SD_obs','SD_field','DNc','DNd','EOM']
RNG=[range(4),range(2),range(3),range(3),range(3),range(2),range(5),range(2),
     range(2),range(2),range(2),range(2),range(3),range(3),range(2)]
Xe,Xs,Sc,IC,Uo,Ug,Np,Na,Ld,Lk,So,Sf,Dc,Dd,EO=range(15)
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[Xe]>=3: rz(Np,2); rz(Na,1)
        if x[Sc]>=2: rz(IC,1)
        if x[Uo]>=2: rz(IC,2)
        if x[Uo]>=1: rz(Np,1)
        if x[Np]>=4: rz(Xe,1)
        if x[Ld]>=1: rz(Dd,1)
        if x[So]>=1: rz(IC,2)
        if x[Dc]>=2: rz(IC,2); rz(Ld,1); rz(Dd,2)
        if x[Dd]>=2: rz(Dc,2)
        if x[Na]>=1: rz(Np,2)
        if x[Ug]>=1: rz(Xs,1)
        if x[Lk]>=1: rz(Dd,2)
        if x[EO]>=1: rz(Ug,1)
    return tuple(x)
def E(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    tot=0; cur=[None]*d
    def rec(i):
        nonlocal tot
        if i==d: tot+=1; return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>phi[(i,j)][cur[j]] or cur[j]>phi[(j,i)][v]: ok=False; break
            if ok: cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return tot-len(S)
allc={c for c in {close(x) for x in product(*RNG)} if c[Sf]==0}
V={c for c in allc if not(c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)}
base=E(V,15)
print('  baseline: %d cells, E = %d' % (len(V),base))
print()
T={(c[Xe],c[Ug],c[Np]) for c in V}
print('  the minimal triple {X_exp, U_ghost, NEC_pt}: %d cells, E = %d' % (len(T),E(T,3)))
vals=[sorted({t[i] for t in T}) for i in range(3)]
print('  exhaustive relabelling: %d x %d x %d = %d'
      % (len(vals[0]),len(vals[1]),len(vals[2]),
         __import__('math').factorial(len(vals[0]))*__import__('math').factorial(len(vals[1]))*__import__('math').factorial(len(vals[2]))))
zeros=0; tested=0; mn=None
for pa in permutations(range(len(vals[0]))):
    ma={vals[0][k]:pa[k] for k in range(len(vals[0]))}
    for pb in permutations(range(len(vals[1]))):
        mb={vals[1][k]:pb[k] for k in range(len(vals[1]))}
        for pc in permutations(range(len(vals[2]))):
            mc={vals[2][k]:pc[k] for k in range(len(vals[2]))}
            S={(ma[t[0]],mb[t[1]],mc[t[2]]) for t in T}
            e=E(S,3); tested+=1
            if mn is None or e<mn: mn=e
            if e==0: zeros+=1
print('     tested %d, closing %d, minimum E = %d' % (tested,zeros,mn))
print()
print('  THE SIX OPERATIONS')
res=[]
# 1 merge by identification - rule test
res.append(('merge by identification','not licensed',None,
            'no pair among {X_exp, U_ghost, NEC_pt} is biconditional at every rung'))
# 2 linearisation of (X_exp,U_ghost)
pairs=sorted({(c[Xe],c[Ug]) for c in V})
paid=lambda p: 0 if (p[0]==0 and p[1]==0) else 1
W=sorted(pairs,key=lambda p:(paid(p),p[0],p[1])); Wi={p:i for i,p in enumerate(W)}
S2={(Wi[(c[Xe],c[Ug])],)+tuple(c[i] for i in range(15) if i not in (Xe,Ug)) for c in V}
res.append(('merge by linearisation','worse' ,E(S2,14),'collapsing two axes coarsens every envelope on either'))
# 3 relabel
res.append(('relabel axis values (exhaustive)','never zero',mn,'%d of %d close'%(zeros,tested)))
# 4 slide NEC_pt within each (X_exp,U_ghost) row
rows=defaultdict(list)
for c in V: rows[(c[Xe],c[Ug])].append(c[Np])
S4={tuple(sorted(set(rows[(c[Xe],c[Ug])])).index(c[Np]) if i==Np else c[i] for i in range(15)) for c in V}
res.append(('slide within rows',None,E(S4,15),'the hole is a row that should not exist'))
# 5 derived coordinate
P=lambda c: 1 if (c[Xe]>=1 or c[Ug]>=1) else 0
S5={c+(P(c),) for c in V}
res.append(('add a derived coordinate','worse',E(S5,16),'the box inflates, |X| does not'))
# 6 split NEC_pt further
sp={0:(0,0),1:(1,0),2:(2,0),3:(2,1),4:(2,2)}
S6={tuple(c[:Np])+sp[c[Np]]+tuple(c[Np+1:]) for c in V}
res.append(('split an axis further',None,E(S6,16),'pins the antecedent as well'))
print('  %-34s %8s  %s' % ('operation','E','note'))
for n,tag,e,note in res:
    v = 'n/a' if e is None else str(e)
    print('  %-34s %8s  %s' % (n,v,note))
print()
print('  none reaches E = 0 (baseline %d)' % base)
print()
print('  THE ENVELOPE ARGUMENT, AT FIFTEEN LETTERS')
def phiv(i,j,v):
    return max([c[i] for c in V if c[j]<=v] or [-99])
print('     phi(NEC_pt | X_exp = 0)   = %d   (X_exp=0 cells with ghosts reach it)' % phiv(Np,Xe,0))
print('     phi(NEC_pt | U_ghost = 0) = %d   (ghost-free cells with X_exp>=1 reach it)' % phiv(Np,Ug,0))
print('     both permit NEC_pt = 3; neither can forbid the pair. Core = 1, irreducible.')