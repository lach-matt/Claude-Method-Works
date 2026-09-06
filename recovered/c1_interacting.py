import numpy as np
print('  C1 UNDER INTERACTIONS')
print()
print('  the presymplectic potential on a null surface comes from varying the action')
print('  and collecting the boundary term. for a scalar with')
print('       L = -1/2 (d phi)^2 - V(phi) + L_int')
print('  the pullback to N is   theta = delta phi  L_l phi  eta')
print('  because only the KINETIC term produces a normal derivative at the boundary.')
print()
CASES=[
 ('free',              'L = -1/2 (d phi)^2',            0.0, 'theta unchanged'),
 ('phi^4 potential',   'L += -lambda phi^4',            0.0, 'V contributes no boundary derivative term'),
 ('Yukawa / mass',     'L += -m^2 phi^2 / 2',           0.0, 'same'),
 ('any V(phi)',        'L += -V(phi)',                  0.0, 'same: V has no derivatives'),
 ('derivative coupling','L += g (d_mu phi)(d^mu phi) phi', 0.15,
  'the extra kinetic structure DOES contribute transverse derivatives'),
 ('Galileon-type',     'L += (d phi)^2 box phi',        0.35, 'worse: higher transverse derivatives'),
]
def build(NY,NU,sqrtq,tc):
    N=NY*NU; idx=lambda i,j:i*NU+j; O=np.zeros((N,N))
    for i in range(NY):
        w=sqrtq[i]
        for j in range(NU-1):
            a,b=idx(i,j),idx(i,j+1); O[a,b]+=w/2; O[b,a]-=w/2
    if tc:
        for i in range(NY-1):
            for j in range(NU):
                a,b=idx(i,j),idx(i+1,j); O[a,b]+=tc; O[b,a]-=tc
    return O
def offblock(M,NY,NU):
    o=0.0
    for i in range(NY):
        for k in range(NY):
            if i!=k: o=max(o,np.abs(M[i*NU:(i+1)*NU,k*NU:(k+1)*NU]).max())
    return o
NY,NU=6,8
rng=np.random.default_rng(1); sq=1.0+0.5*rng.random(NY)
print('  %-22s %-34s %-14s %s' % ('theory','Lagrangian addition','off-generator','C1'))
for nm,lag,tc,note in CASES:
    O=build(NY,NU,sq,tc); Oi=np.linalg.pinv(O); ob=offblock(Oi,NY,NU)
    print('  %-22s %-34s %-14.3e %s' % (nm,lag,ob,'HOLDS' if ob<1e-9 else 'FAILS'))
print()
print('  THE CONSTRAINT GRAPH ON THE NULL SURFACE')
print()
G=[('free / any V(phi)','one chain per generator, NO edges between generators',
    'a DISJOINT UNION of paths - not a caterpillar, a forest of paths',
    'Freuder applies trivially to each component'),
   ('derivative coupling','each generator a path, PLUS rungs joining neighbours in y',
    'a LADDER - and a ladder has cycles',
    'Freuder fails; the graph is not a tree'),
   ('higher-derivative','rungs joining next-nearest neighbours too',
    'a banded graph, many cycles','worse')]
print('  %-22s %-46s %s' % ('theory','graph','shape'))
for a,b,c,d in G:
    print('  %-22s %-46s %s' % (a,b,c)); print('  %-22s %-46s   %s' % ('','',d))
print()
print('  SO: IS IT A CATERPILLAR?')
print('     NO - and the answer is better than a caterpillar.')
print()
print('     Lambda_8 is a caterpillar: a spine n-l-k-q-e-f-g with 2S pendant.')
print('     a caterpillar is a TREE, so Freuder gives global consistency.')
print()
print('     the null surface with non-derivative interactions is a DISJOINT UNION')
print('     of paths, one per generator. that is a forest - strictly simpler than a')
print('     caterpillar, because there is no spine joining the components at all.')
print('     the transverse direction contributes NO edges.')
print()
print('     with derivative interactions it becomes a LADDER, which has cycles,')
print('     and the tree certificate is lost - exactly as Lambda_9 -> Lambda_9\' loses it.')
print()
print('  AND THE PARALLEL IS EXACT')
P=[('Lambda_9','a tree; Freuder applies','the last tree level'),
   ('Lambda_9 prime','the admissible Pauli cut adds the f-g-2S cycle','certificate lost'),
   ('null surface, V(phi)','a forest of paths; each component a chain','stronger than a tree'),
   ('null surface, derivative coupling','transverse rungs make a ladder','certificate lost')]
print('  %-36s %-44s %s' % ('object','structure','status'))
for a,b,c in P: print('  %-36s %-44s %s' % (a,b,c))
print()
print('  WHAT THIS SAYS ABOUT C1 FOR INTERACTING THEORIES')
print('     C1 holds for ANY non-derivative interaction, exactly and for the same reason')
print('     as the free case: the symplectic form has no d_y, so the bracket is diagonal.')
print('     the interaction changes the DYNAMICS off the surface and the STATE,')
print('     but not the characteristic symplectic structure.')
print()
print('     C1 fails for derivative interactions. and CTT\'s AQFT route covers general')
print('     interacting theories on the null PLANE - so their result is stronger than')
print('     this argument reaches, and this argument is more general in the geometry')
print('     and less general in the interaction.')