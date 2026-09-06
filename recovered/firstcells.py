from itertools import product
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_=range(9)
PAT=[Sc_,IC_,L_,DNc_,DNd_]
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[0]>=3: rz(4,2)
        if x[1]>=2: rz(2,1)
        if x[2]>=2: rz(0,1)
        if x[3]>=2: rz(2,2)
        if x[3]>=1: rz(4,1)
        if x[4]>=4: rz(0,1)
        if x[5]>=1: rz(8,1)
        if x[6]>=1: rz(2,2)
        if x[7]>=2: rz(2,2); rz(5,1); rz(8,2)
        if x[8]>=2: rz(7,2)
    return tuple(x)
def RRs(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
allc={close(x) for x in product(*RNG)}
V=sorted({c for c in allc if not(c[4]>=3 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))})
Vs=set(V); ex=sorted(RRs(V,9)-Vs)
P=sorted({tuple(e[i] for i in PAT) for e in ex})
def sP(c):
    v=tuple(c[i] for i in PAT); return min(sum(1 for k in range(5) if v[k]!=p[k]) for p in P)
def dP(c):
    v=tuple(c[i] for i in PAT); return min(sum(abs(v[k]-p[k]) for k in range(5)) for p in P)
def s_f(c): return (1 if c[X_]>0 else 0)+(1 if c[U_]>0 else 0)+(1 if c[SD_]>0 else 0)+(1 if c[NEC_]!=3 else 0)+sP(c)
def d_f(c): return c[X_]+c[U_]+c[SD_]+abs(c[NEC_]-3)+dP(c)
def gap(c): return [v for v in range(5) if close(tuple(list(c[:4])+[v]+list(c[5:]))) in Vs]
def objs(c):
    r=[]
    if c[NEC_]>=1: r.append('evaporating BH')
    if c[NEC_]>=2: r.append('Planck wormhole')
    if c[NEC_]>=3: r.append('macroscopic wormhole')
    if c[X_]>=2: r.append('universal horizon')
    if c[X_]>=3: r.append('time machine')
    return ', '.join(r) or '-'
o=close((0,1,0,0,1,0,0,0,0))
print('  ORIGIN  %s   s=%d  d=%d  NEC reachable %s' % (o, s_f(o), d_f(o), gap(o)))
print()
hdr = '  %-8s %-30s %-24s %4s %3s %3s %-16s' % ('step','cell','drags','cost','s','d','NEC reachable')
print(hdr)
rows=[]
for i in range(9):
    t=list(o); t[i]+=1
    if t[i] >= len(RNG[i]): continue
    tc=close(tuple(t))
    if tc not in Vs:
        print('  %-8s %-30s %-24s' % (NM[i]+' +1', str(tc), 'NOT ADMISSIBLE (the gap)'))
        continue
    dr=[NM[j] for j in range(9) if tc[j]!=o[j] and j!=i]
    cost=sum(1 for j in range(9) if tc[j]!=o[j])
    g=gap(tc)
    rows.append((NM[i],tc,dr,cost,s_f(tc),d_f(tc),g))
    print('  %-8s %-30s %-24s %4d %3d %3d %-16s' % (NM[i]+' +1', str(tc), (', '.join(dr) or '-'), cost, s_f(tc), d_f(tc), str(g)))
print()
desc={'X':'a preferred threading of spacetime; the aether has a twist but no foliation',
      'Sc':'correlations pass Tsirelson; information causality fails at once (dragged)',
      'IC':'information causality fails while correlations stay quantum',
      'U':'evolution becomes non-unitary at the Lindblad rung, energy-momentum conserved',
      'NEC':'ANEC violated at arbitrarily small scale; Planck-scale wormholes exist',
      'L':'quantum mechanics becomes nonlinear; discrimination beats the optimum (dragged)',
      'SD':'microcausality fails, forcing signalling and a preferred frame (dragged twice)',
      'DNc':'cloning beats the quantum optimum without reaching perfect cloning',
      'DNd':'discrimination beats the quantum optimum'}
print('  WHAT EACH FIRST CELL IS')
for nm,tc,dr,cost,s,d,g in rows:
    tag = 'gap closed - has paid' if 3 in g else 'still sees the gap'
    print('     %-4s +1  %s' % (nm, desc[nm]))
    print('               cost %d coordinate(s), distance to blind spot %d, %s' % (cost,d,tag))
    print('               objects available: %s' % objs(tc))
print()
print('  first cells still seeing the gap: %d of %d' % (sum(1 for r in rows if 3 not in r[6]), len(rows)))
print('  first cells that have paid      : %d of %d' % (sum(1 for r in rows if 3 in r[6]), len(rows)))