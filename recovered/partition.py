from collections import defaultdict, Counter
print('  DERIVING THE PARTITION FROM BFV RATHER THAN MATCHING IT')
print()
print('  Brunetti-Fredenhagen-Verch: a locally covariant QFT is a functor')
print('        A : Loc  ->  Alg')
print('  that object has exactly four parts:')
print('     1  the SOURCE objects   : globally hyperbolic spacetimes')
print('     2  the TARGET objects   : unital *-algebras')
print('     3  the FUNCTOR itself   : what the Lagrangian determines')
print('     4  FUNCTIONALS on the target : states')
print()
V={'T  THEORY   (the functor)':
     ['X_exp   Lorentz invariance of the action','CPT','causality / no superluminal propagation',
      'field content','EOM  derivative order','degeneracy','interacting','dimension',
      'xi  coupling to curvature  <- was V5/W4'],
   'M  SPACETIME (source objects)':
     ['flat / asymptotically flat / curved','simply connected','globally hyperbolic',
      'generic condition','spatially compact','achronality of a geodesic  <- was W5'],
   'A  ALGEBRA  (target objects)':
     ['U_open','U_ghost','SD_obs','SD_field','L_dyn','L_kin','IC','DNc','DNd',
      'determinism','ultralocality','stability'],
   'S  STATE    (functionals on the algebra)':
     ['X_spon  a VEV picks a frame','Sc  CHSH value realised','NEC_pt  <T_kk> in THIS state',
      'Hadamard','vacuum is lowest energy','vacuum not annihilated']}
for k,v in V.items():
    print('  %s' % k)
    for t in v: print('        %s' % t)
print()
n=sum(len(x) for x in V.values())
print('  terms placed: %d in %d vocabularies' % (n,len(V)))
print()
print('  WHAT WOULD NOT PLACE')
REL=[('self-consistent semiclassical','a RELATION between M and S: G(g) = 8pi <T>_psi'),
     ('within the semiclassical regime','a RELATION: the pair (g, psi) stays where the expansion holds'),
     ('backreaction included','the same relation, stated as a modelling choice'),
     ('state-independent QEI availability','a RELATION between T and S: does a bound hold for ALL psi')]
for a,b in REL: print('     %-36s %s' % (a,b))
print()
print('     these are exactly the terms that made V6 look like a vocabulary.')
print('     they are not properties of anything. they are conditions ON PAIRS.')
print()
print('  THE TEST: does xi belong to the theory?')
print('     xi appears in the action as xi*R*phi^2. it changes the Lagrangian,')
print('     hence the functor, hence the algebra assigned to each spacetime.')
print('     it is not a separate layer. -> V5 collapses into T. confirmed by construction.')
print()
print('  THE TEST: where does NEC_pt live?')
print('     NEC_pt is <T_munu> k^mu k^nu -- an EXPECTATION VALUE.')
print('     an expectation value is a functional on the algebra evaluated at a state.')
print('     -> S, unambiguously. the earlier W3-or-W5 hesitation is resolved by the derivation.')
print()
print('  CONSEQUENCES FOR THE OBSTRUCTIONS')
HOME={'X_exp':'T','EOM':'T','X_spon':'S','Sc':'S','NEC_pt':'S','NEC_ach':'M',
      'IC':'A','U_open':'A','U_ghost':'A','L_dyn':'A','L_kin':'A','SD_obs':'A',
      'SD_field':'A','DNc':'A','DNd':'A','FLAT':'M','CONN':'M','HYP':'M','GEN':'M','ASYM':'M'}
OBS=[(['X_exp','U_ghost','NEC_pt'],'the Buniy charge'),
     (['X_exp','X_spon','NEC_pt'],'its shadow via X_spon'),
     (['NEC_pt','FLAT','CONN'],'the V1-V3 edge')]
for s,lab in OBS:
    vs=sorted({HOME[x] for x in s})
    print('     %-34s %-28s spans %s' % (lab,str(s),vs))
print()
print('  AND THE CLOSED INDICES')
CL=[('V3 geometry','M','all five letters in M'),
    ('V6 solution','M + S + RELATIONS','it was never one vocabulary'),
    ('V5 coupling','T','xi is a theory parameter'),
    ('Lambda','?','atomic structure sits outside this partition entirely')]
for a,b,c in CL: print('     %-14s %-22s %s' % (a,b,c))
print()
print('  THE ANSWER')
print('     the V index is FOUR: Theory, sPacetime, Algebra, State.')
print('     it is not my partition. it is the BFV functor, read as a list of its parts.')
print('     the three extra vocabularies I had were:')
print('        V5 coupling  -> a parameter of the theory')
print('        V6 solution  -> a relation between spacetime and state')
print('        V7 degeneracy-> a parameter of the theory')
print('     and V2 "theory" was not an index because it was the functor itself,')
print('        described by a list of its properties rather than graded.')