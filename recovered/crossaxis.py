from itertools import product
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_=range(9)
EDGES=[(0,3,4,2,'X>=3 -> NEC>=2'),(1,2,2,1,'Sc>=2 -> IC>=1'),(2,2,0,1,'IC=2 -> X>=1'),
       (3,2,2,2,'U=2 -> IC=2'),(3,1,4,1,'U>=1 -> NEC>=1'),(4,4,0,1,'NEC>=4 -> X>=1'),
       (5,1,8,1,'L -> DNd>=1'),(6,1,2,2,'SD -> IC=2'),(7,2,5,1,'DNc=2 -> L'),
       (7,2,8,2,'DNc=2 -> DNd=2'),(8,2,7,2,'DNd=2 -> DNc=2')]
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        for ai,av,ci,cv,_ in EDGES:
            if x[ai]>=av: rz(ci,cv)
        return_flag=False
    return tuple(x)
def close2(x):
    x=list(x); g=True
    while g:
        g=False
        for ai,av,ci,cv,_ in EDGES:
            if x[ai]>=av and x[ci]<cv: x[ci]=cv; g=True
    return tuple(x)
allc={close2(x) for x in product(*RNG)}
V={c for c in allc if not(c[4]>=3 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))}
C=[('evap BH',NEC_,1),('Planck WH',NEC_,2),('macro WH',NEC_,3),('univ horizon',X_,2),
   ('time machine',X_,3),('trivial CC',Sc_,2),('signalling',IC_,2),('info loss',U_,1),
   ('NP in P',L_,1),('perfect clone',DNc_,2),('perfect disc',DNd_,2)]
K=[('unitarity',U_,0),('Lorentz invariance',X_,0),('no signalling',IC_,1),
   ('information causality',IC_,0),('microcausality',SD_,0),('linearity',L_,0),('the ANEC',NEC_,1)]
print('  EXCLUSIONS, CLASSIFIED')
print('  %-14s %-24s %-11s %s' % ('capability','principle','type','derivation'))
direct={(ai,ci) for ai,av,ci,cv,_ in EDGES}
cross=[]
for cn,cax,cv in C:
    for kn,kax,kmax in K:
        keep=[c for c in V if c[kax]<=kmax]
        if any(c[cax]>=cv for c in keep): continue
        if cax==kax:
            print('  %-14s %-24s %-11s %s' % (cn,kn,'same-axis','tautological'))
        else:
            # is it a single stated edge?
            e=[lab for ai,av,ci,cvv,lab in EDGES if ai==cax and ci==kax and av<=cv]
            typ='EDGE' if e else 'COMPOSED'
            cross.append((cn,kn,typ,e[0] if e else ''))
            print('  %-14s %-24s %-11s %s' % (cn,kn,typ,e[0] if e else 'via the closure'))
print()
print('  cross-axis exclusions: %d   (of which single edges: %d, composed: %d)'
      % (len(cross), sum(1 for r in cross if r[2]=='EDGE'), sum(1 for r in cross if r[2]=='COMPOSED')))
print()
print('  TRACING THE COMPOSED ONES')
def path(src_ax, src_val, tgt_ax):
    # BFS over edges from (src_ax>=src_val) to something forcing tgt_ax
    seen=set(); frontier=[([src_ax],[])]
    out=[]
    for depth in range(4):
        nf=[]
        for axes,labs in frontier:
            last=axes[-1]
            for ai,av,ci,cv,lab in EDGES:
                if ai!=last: continue
                if ci==tgt_ax: out.append(labs+[lab])
                else: nf.append((axes+[ci],labs+[lab]))
        frontier=nf
    return out
for cn,kn,typ,e in cross:
    if typ!='COMPOSED': continue
    cax=[a for n,a,v in C if n==cn][0]; kax=[a for n,a,v in K if n==kn][0]
    ps=path(cax,0,kax)
    if ps: print('     %-14s -> %-22s : %s' % (cn,kn,'  then  '.join(ps[0])))