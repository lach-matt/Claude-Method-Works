NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
MISSING=[
 ('CPT invariance',
  'Greenberg 2002: CPT violation implies violation of Lorentz invariance',
  'would EDGE into X; also a hypothesis of Wall\'s ANEC-from-GSL derivation',
  'YES - a theorem links it to an existing axis'),
 ('energy-momentum conservation',
  'Banks-Susskind-Peskin: non-unitarity violates locality OR energy-momentum conservation',
  'it is one of the two BSP disjuncts; the index has the other (locality) and not this',
  'YES - half of a disjunction already in use is missing'),
 ('the generalised second law',
  'Dubovsky-Sibiryakov, Eling et al, Wall - used as a charger throughout',
  'GSL violation is the trigger of a charge but is not a coordinate',
  'YES - a charger trigger with no axis'),
 ('global symmetry conservation',
  'Hsin-Iliesiu-Yang: replica wormholes violate global symmetries',
  'no coordinate; the swampland literature treats it as a law-class',
  'no theorem links it to an existing axis in this index'),
 ('determinism',
  'Wall\'s GSL axioms name it explicitly',
  'a jurisdiction condition, like ultralocality and stability',
  'jurisdiction, not a law-class - arguably belongs in the setting index'),
 ('the equivalence principle',
  'MICROSCOPE bounds it; ghost condensate maximally violates it',
  'no coordinate, though it is measured to 1e-15',
  'measured, and absent'),
 ('derivative order of the EOM',
  'Buniy\'s operative hypothesis; Creminelli et al escape through it',
  'identified this session as a needed axis',
  'YES - already established as missing'),
]
print('  LAW-CLASSES APPEARING IN CITED SOURCES WITH NO COORDINATE')
print()
for n,src,role,verdict in MISSING:
    print('  %-32s %s' % (n, verdict))
    print('       source : %s' % src)
    print('       role   : %s' % role)
    print()
print('  count: %d' % len(MISSING))
print()
print('  THE SHARPEST TWO')
print('     CPT   - Greenberg gives CPT violation -> Lorentz violation, i.e. an EDGE into X.')
print('             its absence means the index is missing a forcing, not just an axis.')
print('     E-p   - BSP\'s disjunction is (not locality) OR (not energy-momentum conservation).')
print('             the index encodes the first disjunct and silently drops the second,')
print('             which is exactly the mis-typing corrected in Part VII, uncorrected here.')
print()
print('  WHAT I DO NOT HAVE')
print('     no completeness criterion for the coordinate set.')
print('     the nine came from one pass of retrieval on "which laws could break".')
print('     a different pass gives different axes, and nothing in the method says when to stop.')
print('     E measures what the index cannot carry.')
print('     the vocabulary debt measures what it has not checked it carries correctly.')
print('     NOTHING measures what it never named at all.')
print()
print('  CONSEQUENCE FOR EVERY NUMBER IN THIS WORK')
print('     2370 cells, defect 30, core 1 - all computed over NINE coordinates.')
print('     adding CPT, energy-momentum conservation, the GSL and derivative order')
print('     would change the cell count, the defect, and possibly the core\'s location.')
print('     the structural results (arity, ordering, vocabulary mismatch) do NOT depend on the count.')
print('     the physical results DO.')