from collections import Counter
V=['T','M','A','S']
# assignment rule: what does the term PREDICATE ON?
#   T the functor (the Lagrangian) | M the source objects (the manifold)
#   A the target objects (the algebra) | S functionals on the algebra (states)
TERMS={
 # --- V1, the fifteen letters
 'X_exp':((1,0,0,0),'Lorentz invariance OF THE ACTION'),
 'X_spon':((0,0,0,1),'a VEV: a property of the vacuum STATE'),
 'Sc':((0,0,0,1),'the CHSH value realised IN a state'),
 'IC':((0,0,1,0),'a property of the operations the algebra admits'),
 'U_open':((0,0,1,0),'CPTP structure of the evolution on the algebra'),
 'U_ghost':((0,0,1,0),'indefinite metric ON the algebra'),
 'NEC_pt':((0,0,0,1),'<T_kk> evaluated in a state'),
 'NEC_ach':((0,1,0,0),'achronality of a geodesic: purely causal structure'),
 'L_dyn':((0,0,1,0),'the evolution law on the algebra'),
 'L_kin':((0,0,1,0),'the state space structure'),
 'SD_obs':((0,0,1,0),'commutativity of algebra elements'),
 'SD_field':((0,0,1,0),'commutativity of fields'),
 'DNc':((0,0,1,0),'admissible maps on states = algebra structure'),
 'DNd':((0,0,1,0),'as DNc'),
 'EOM':((1,0,0,0),'derivative order of the action'),
 # --- V3
 'FLAT':((0,1,0,0),'curvature of the manifold'),
 'CONN':((0,1,0,0),'topology of the manifold'),
 'HYP':((0,1,0,0),'existence of a Cauchy surface'),
 'GEN':((0,1,0,0),'the generic condition on causal geodesics'),
 'ASYM':((0,1,0,0),'presence of an asymptotic region'),
 # --- V6
 'SC   self-consistent semiclassical':((0,1,0,1),'G(g) = 8pi <T>_psi -- RELATES the metric and the state'),
 'HAD  Hadamard':((0,0,0,1),'short-distance behaviour of a state'),
 'REG  within the semiclassical regime':((0,1,0,1),'a condition on the PAIR (g, psi)'),
 'ACH  achronal geodesic':((0,1,0,0),'causal structure'),
 # --- V5
 'xi   curvature coupling':((1,0,0,0),'appears in the action'),
 'STATEIND  state-independent QEI':((1,0,0,1),'a bound holding for ALL states of a theory'),
 # --- charger hypotheses
 'causal / no superluminal':((1,0,0,0),'a property of the action'),
 'field content':((1,0,0,0),'what fields the action contains'),
 'interacting':((1,0,0,0),'whether the action has interaction terms'),
 'dimension':((1,0,0,0),'a parameter of the theory'),
 'CPT':((1,0,0,0),'a symmetry of the action'),
 'non-degenerate':((1,0,0,0),'the kinetic structure of the action'),
 'determinism':((0,0,1,0),'a property of the evolution'),
 'ultralocality':((0,0,1,0),'a property of the algebra net'),
 'stability':((0,0,1,0),'spectrum condition on the algebra'),
 'vacuum is lowest energy':((0,0,0,1),'a property of a distinguished state'),
 'vacuum not annihilated':((0,0,0,1),'a property of a distinguished state'),
 # --- the flagged cases
 'q  Lambda transfer count':((0,0,0,0),'no referent in the spectroscopic literature'),
 'supertranslation, whole horizon':((0,0,0,0),'the NEH free data is supertranslation-invariant'),
 'supertranslation, subregion':((0,0,1,0),'the cut names a region, hence an algebra'),
}
print('  THE TEST: every term in the construction, by weight')
print()
by=Counter()
flags={'weight 0':[], 'weight >= 2':[]}
for k,(v,why) in TERMS.items():
    w=sum(v); by[w]+=1
    if w==0: flags['weight 0'].append((k,why))
    if w>=2: flags['weight >= 2'].append((k,v,why))
print('  terms tested : %d' % len(TERMS))
for w in sorted(by): print('     weight %d : %d' % (w,by[w]))
print()
print('  WEIGHT >= 2  -- an unsplit conflation, or a relation')
for k,v,why in flags['weight >= 2']:
    print('     %-40s %s   %s' % (k,str(v),why))
print()
print('  WEIGHT 0  -- needs a translator, or is ungrounded')
for k,why in flags['weight 0']:
    print('     %-40s %s' % (k,why))
print()
print('  DID THE TEST FIND ANYTHING NOT ALREADY KNOWN?')
KNOWN={'SC   self-consistent semiclassical':'identified as a relation in the BFV derivation',
       'REG  within the semiclassical regime':'identified as a relation, and separately as conflated',
       'STATEIND  state-independent QEI':'identified as a relation in the BFV derivation',
       'q  Lambda transfer count':'identified as UNGROUNDED in the Lambda audit',
       'supertranslation, whole horizon':'identified as the gauge/physical reversal'}
newf=[k for k,_ ,_ in flags['weight >= 2']]+[k for k,_ in flags['weight 0']]
for k in newf:
    print('     %-40s %s' % (k, KNOWN.get(k,'*** NEW ***')))
print()
print('  AND WHAT THE WEIGHT-2 TERMS HAVE IN COMMON')
print('     all three are conditions on a PAIR: (metric, state) twice, (theory, state) once.')
print('     none is a conflation. splitting them would be wrong - there is one condition,')
print('     and it genuinely mentions two vocabularies.')
print('     -> weight 2 does NOT always mean "unsplit". it means "relation OR conflation",')
print('        and the test cannot tell them apart. that is a limit of the instrument.')
print()
print('  LAMBDA IS NOT TESTABLE')
LAM=['n','l','k','q','e','f','g','2S',"2S'",'2J','2K','v','L']
print('     Lambda\'s 13 coordinates: %s' % ', '.join(LAM))
print('     none predicates on the functor, the manifold, the algebra or a state.')
print('     they predicate on a CONFIGURATION - a labelling of solutions to a')
print('     one-particle problem. that is outside the BFV partition entirely.')
print('     -> the test applies to the transitions material and not to Lambda,')
print('        which is a further reason Lambda was never the right control.')