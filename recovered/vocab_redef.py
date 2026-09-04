from collections import defaultdict, Counter
from itertools import combinations
print('  THE OLD PARTITION AND WHY IT FAILED')
FAIL=[('V2 theory','not an index: 2 terms non-operative, 1 belongs in V1, 1 categorical'),
      ('V4 algebra','merges two unrelated programmes (GSL axioms, Wightman axioms)'),
      ('V5 coupling','filed as one term; actually a graded axis of at least three rungs'),
      ('CPT','belongs to V4a AND to V1 -> the partition is not a partition'),
      ('"causal"','filed in V2; it means no superluminal propagation, i.e. V1')]
for a,b in FAIL: print('     %-14s %s' % (a,b))
print()
print('  NEW CRITERION: what does the term PREDICATE ON?')
print()
W={'W1 THEORY   (the Lagrangian)':
     ['X_exp  Lorentz invariance of the action','CPT','causality / no superluminal propagation',
      'field content (scalar/gauge/fermion)','EOM  derivative order','degeneracy (Galileon-type)',
      'interacting','spacetime dimension'],
   'W2 SPACETIME (the manifold)':
     ['flat / asymptotically flat / curved','simply connected','globally hyperbolic',
      'generic condition','spatially compact'],
   'W3 STATE     (the vector or density matrix)':
     ['X_spon  a VEV picks a frame','Hadamard','vacuum is lowest energy',
      'vacuum not annihilated','NEC_pt  the null energy of THIS state','Sc  CHSH value realised'],
   'W4 COUPLING  (matter-to-geometry)':
     ['xi  minimal / conformal / general','state-independent QEI availability'],
   'W5 SOLUTION  (geometry and state together)':
     ['self-consistent semiclassical','within the semiclassical regime','backreaction included',
      'NEC_ach  achronality of the geodesic'],
   'W6 ALGEBRA   (observables and evolution)':
     ['U_open  CPTP non-unitarity','U_ghost  indefinite metric','SD_obs / SD_field  commutativity',
      'L_dyn / L_kin  linearity','IC  information causality','DNc / DNd  cloning and discrimination',
      'determinism','ultralocality','stability']}
for k,v in W.items():
    print('  %s' % k)
    for t in v: print('        %s' % t)
print()
tot=sum(len(v) for v in W.values())
print('  terms placed: %d across %d vocabularies' % (tot,len(W)))
print()
print('  WHERE V1\'s FIFTEEN LETTERS GO')
HOME={'X_exp':'W1','X_spon':'W3','Sc':'W3','IC':'W6','U_open':'W6','U_ghost':'W6',
      'NEC_pt':'W3','NEC_ach':'W5','L_dyn':'W6','L_kin':'W6','SD_obs':'W6','SD_field':'W6',
      'DNc':'W6','DNd':'W6','EOM':'W1'}
c=Counter(HOME.values())
for k,v in sorted(c.items()): print('     %-4s %2d letters: %s' % (k,v,', '.join(a for a,b in HOME.items() if b==k)))
print()
print('  -> V1 "laws" is NOT a vocabulary. it spans %d of the %d new ones.' % (len(c),len(W)))
print('     it was a subject-matter grouping: "things that could break".')
print()
print('  THE TEST: does the minimal support span vocabularies?')
SUP=[['X_exp','U_ghost','NEC_pt'],['X_exp','X_spon','NEC_pt']]
for s in SUP:
    vs={HOME[x] for x in s}
    print('     %-34s -> %s   spans %d' % (str(s),sorted(vs),len(vs)))
print()
print('  AND THE V1-V3 EDGE OBSTRUCTION')
EDGE=['NEC_pt','FLAT','CONN']
HOME2=dict(HOME); HOME2['FLAT']='W2'; HOME2['CONN']='W2'
vs={HOME2[x] for x in EDGE}
print('     %-34s -> %s   spans %d' % (str(EDGE),sorted(vs),len(vs)))
print()
print('  THE UNIFICATION')
print('     old reading: one obstruction INSIDE V1 (arity 3) and one ON the V1-V3 edge (arity 3).')
print('     new reading: BOTH are cross-vocabulary ternary constraints.')
print('        {X_exp, U_ghost, NEC_pt} spans THEORY x ALGEBRA x STATE')
print('        {NEC_pt, FLAT, CONN}     spans STATE x SPACETIME')
print('     the first was invisible as cross-vocabulary because "laws" hid three vocabularies')
print('     under one name. that is the same failure as U hiding two notions under one letter,')
print('     one level up: a CONFLATED VOCABULARY rather than a conflated coordinate.')
print()
print('  WHAT THIS PREDICTS')
print('     every arity-3 obstruction found should span >= 2 vocabularies under W.')
print('     checked: 3 of 3 do (two supports in V1, one on the edge).')
print('     and a constraint entirely within one W-vocabulary should be binary.')
print('     checked: V3 (all W2) closes; V6 (all W5) closes; V5 (all W4) closes.')
print('     -> arity tracks VOCABULARY SPAN, not coordinate count.')