from itertools import product
NM=['NEC_pt','X_exp','U_ghost','SD_obs','FLAT','CONN','HYP','GEN','ASYM']
RNG=[range(5),range(4),range(2),range(2),range(3),range(2),range(2),range(2),range(2)]
NEC,XE,UG,SO,FLAT,CONN,HYP,GEN,ASYM=range(9)
def close(x, cross):
    x=list(x); g=True
    while g:
        g=False
        def up(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        def dn(i,v):
            nonlocal g
            if x[i]>v: x[i]=v; g=True
        if x[FLAT]==0: dn(CONN,0); dn(HYP,0); dn(GEN,0); dn(ASYM,0)
        if x[CONN]>=1: up(FLAT,1)
        if x[HYP]>=1:  up(FLAT,1)
        if x[ASYM]>=1: up(FLAT,2)
        if x[XE]>=3: up(NEC,2)
        if x[NEC]>=4: up(XE,1)
    return tuple(x)
def base(cross):
    cells={close(x,cross) for x in product(*RNG)}
    cells={close(c,cross) for c in cells}
    if cross:
        cells={c for c in cells
               if c[NEC]<2 or c[FLAT]>=2 or c[CONN]>=1 or c[ASYM]>=1}
    return cells
print('  DOES HARTMAN FIRE?  measured as: how many cells does it EXCLUDE')
print()
for lab,cross in [('WITHOUT the cross-edge (no Hartman content pre-loaded)',False),
                  ('WITH the cross-edge (as I built it before)',True)]:
    B=base(cross)
    # Hartman: in FLAT spacetime, unitary + Lorentz + microcausal => ANEC holds.
    # so it EXCLUDES cells with FLAT=0, NEC>=2, X_exp=0, U_ghost=0, SD_obs=0
    hit=[c for c in B if c[FLAT]==0 and c[NEC]>=2 and c[XE]==0 and c[UG]==0 and c[SO]==0]
    print('  %-52s' % lab)
    print('     cells in the product           : %d' % len(B))
    print('     cells Hartman EXCLUDES         : %d' % len(hit))
    print('     -> Hartman %s' % ('FIRES' if hit else 'has nothing to exclude'))
    if hit:
        print('     e.g. %s' % str(dict(zip(NM,sorted(hit)[0]))))
    print()
print('  THE CIRCULARITY')
print('     the cross-edge "NEC_pt >= 2 -> curved or handle or compact" IS Hartman-plus-more:')
print('     it asserts that flat simply-connected non-compact spacetime cannot host')
print('     an ANEC violation AT ALL, for any theory.')
print('     Hartman proves that only for unitary, Lorentz-invariant, microcausal theories.')
print('     so the edge is STRONGER than Hartman and subsumes it.')
print('     measuring Hartman against an index already carrying the edge finds nothing left.')
print()
print('  THE CORRECTED PICTURE')
print('     Hartman is NOT vacuous. it fires, in flat spacetime, and excludes')
print('     exactly the cells where a flat ANEC violation would sit.')
print('     what is true is narrower and unchanged in consequence:')
print('        its jurisdiction (flat) and the region of interest (curved, where')
print('        macroscopic wormholes live) are DISJOINT.')
print('     so it cannot reach the core cell -- not because it is dead,')
print('     but because it works somewhere else.')
print()
print('  AND THE SEVERANCE SURVIVES, RESTATED')
print('     old: "Hartman is vacuous, so the V1-V3 edge carries no traffic."')
print('     new: "Hartman is a V1-V3 edge that terminates at FLAT = 0.')
print('           the wormhole question lives at FLAT >= 1. the edge exists and')
print('           does not span the distance."')
print('     the graph is connected; the path does not reach the destination.')