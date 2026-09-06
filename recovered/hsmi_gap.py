print('  WHAT HSMI REQUIRES vs WHAT AN NEH SUPPLIES')
print()
REQ=[('a net of algebras on nested regions','M(u) for cuts u, with M(u2) subset M(u1) for u2 > u1'),
     ('a cyclic and separating state','for each M(u)'),
     ('a partial order on the cuts','so "nested" is defined'),
     ('a ONE-PARAMETER family',  'the cuts must be labelled by a single real u, the SAME along every generator'),
     ('positive translations','U(delta) with positive generator, mapping M(u) to M(u+delta)'),
     ('modular flow preserving the inclusion','sigma_t(M(u+delta)) subset M(u+delta) for one sign of t')]
SUP=[('a null hypersurface with cross-sections','YES - an NEH is R x S^2, foliated by spheres'),
     ('a partial order on cross-sections','YES - by inclusion of causal futures. no parametrisation needed.'),
     ('an affine parameter ALONG each generator','YES - each null geodesic generator has one'),
     ('a canonical derivative operator','YES - an NEH inherits D_a intrinsically (Ashtekar)'),
     ('surface gravity constant','YES on a WEAKLY ISOLATED horizon (kappa = const fixes the boost freedom)'),
     ('a common origin ACROSS generators','NO - fixed only up to a supertranslation'),
     ('quantum field algebras on the cuts','YES - locally covariant QFT assigns them')]
print('  %-42s %s' % ('HSMI requires','')); 
for a,b in REQ: print('     %-38s %s' % (a,b))
print()
print('  %-42s %s' % ('an NEH supplies','')); 
for a,b in SUP: print('     %-38s %s' % (a,b))
print()
print('  THE MATCH')
M=[('net of algebras','SUPPLIED','locally covariant QFT on the NEH'),
   ('cyclic separating state','SUPPLIED','generic for a Hadamard state'),
   ('partial order on cuts','SUPPLIED','causal inclusion; no parametrisation used'),
   ('one-parameter labelling','MISSING','requires a common origin across generators'),
   ('positive translations','MISSING','follows from the labelling, by Borchers, IF the labelling exists'),
   ('modular flow preserving inclusion','THE THEOREM','what would have to be proved')]
print('  %-36s %-12s %s' % ('ingredient','status','note'))
for a,b,c in M: print('  %-36s %-12s %s' % (a,b,c))
print()
print('  THE ONE MISSING LETTER')
print('     the per-generator affine ORIGIN.')
print('     each generator has an affine parameter; nothing relates the zero point')
print('     of one generator to the zero point of another.')
print('     fixing them all at once IS a choice of cut, and shifting them all')
print('     independently IS a supertranslation.')
print()
print('  AND HERE IS THE STATEMENT THE METHOD CAN MAKE')
print('     supertranslations are GAUGE in the geometry vocabulary:')
print('        "supertranslations do not affect the NEH geometry" (arXiv 1707.02971)')
print('        the free data set is supertranslation-invariant.')
print()
print('     supertranslations are PHYSICAL in the algebra vocabulary:')
print('        M(u) is the algebra of a REGION. supertranslating the cut changes')
print('        the region, hence the algebra. the net is not supertranslation-invariant.')
print()
print('     -> the obstruction is a quantity that is GAUGE in one vocabulary and')
print('        PHYSICAL in another. that is not a missing fact. it is a term whose')
print('        status differs across the two indices that must be joined.')
print()
print('  WHY THAT IS THE SAME SHAPE AS EVERYTHING ELSE HERE')
print('     Buniy: a hypothesis operative in one scope and not another.')
print('     U, L, SD, X: a word meaning one thing in one literature and another elsewhere.')
print('     2K: a label meaning different things in different coupling schemes.')
print('     n, l: exact in hydrogen, approximate everywhere else.')
print('     supertranslation: gauge in geometry, physical in the algebra.')
print()
print('     five instances, one shape: A TERM WHOSE STATUS IS SCOPE-DEPENDENT,')
print('     and an index that carries the term without carrying the scope.')
print()
print('  CAN WE DO IT WITH WHAT WE HAVE?')
print('     the theorem: NO. it needs modular theory we cannot perform.')
print('     the diagnosis: YES, and it is done above. the gap is one letter, it is')
print('     nameable, and its difficulty is that it changes status between the two')
print('     vocabularies the proof would have to span.')