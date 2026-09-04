print('  THE FIVE INSTANCES, BY WHAT THE SCOPE IS')
print()
I=[('U  open vs ghost','WHICH NOTION','two literatures use "unitarity" for different things',
    'SPLIT the letter','done here: U_open / U_ghost','a translator is not needed; the terms are simply distinct'),
   ('L  dynamical vs kinematical','WHICH NOTION','"nonlinear" means evolution or state space',
    'SPLIT the letter','done here: L_dyn / L_kin','same'),
   ('SD obs vs field','WHICH NOTION','commutativity of observables or of fields',
    'SPLIT the letter','done here: SD_obs / SD_field','same'),
   ('2K','WHICH SCHEME','jK gives Jc+l, LK gives Ltot+Score, jj has no K',
    'CARRY the scheme as a coordinate','not done','the schemes are inter-translatable: Racah recoupling '
    'coefficients ARE the translator, and they exist'),
   ('n, l','WHICH APPROXIMATION','exact in hydrogen, configuration labels under the central field',
    'CARRY the approximation','not done','no translator: the exact and approximate objects are not '
    'related by an isomorphism, only by a limit'),
   ('X  spontaneous vs explicit','WHERE THE BREAKING SITS','the Lagrangian or the vacuum',
    'SPLIT the letter','done here: X_exp / X_spon','the vacuum is a STATE and the Lagrangian is the '
    'THEORY - two different BFV parts, so the split is forced by the partition'),
   ('supertranslation','WHOLE vs PART','gauge on the whole horizon, relational data for a subregion',
    'ADD the missing data','edge modes (Chandrasekaran-Flanagan 2026)',
    'THE TRANSLATOR EXISTS AND IS CONSTRUCTED: gravitational dressing, with corner edge modes '
    'as the translation data')]
print('  %-26s %-22s %s' % ('instance','the scope is','repair'))
for a,b,c,d,e,f in I:
    print('  %-26s %-22s %s' % (a,b,d))
    print('  %-26s %-22s   %s' % ('','',c))
    print('  %-26s %-22s   status: %s' % ('','',e))
    print('  %-26s %-22s   translator: %s' % ('','',f))
    print()
from collections import Counter
c=Counter(x[1] for x in I)
print('  DISTINCT SCOPE KINDS: %d across %d instances' % (len(c),len(I)))
for k,v in c.items(): print('     %-24s %d' % (k,v))
print()
print('  SO "ONE SHAPE" IS DOING LESS WORK THAN CLAIMED')
print('     the common statement -- "a term whose status depends on a scope the index does')
print('     not carry" -- is true of all seven and is nearly a tautology: any term whose')
print('     meaning varies has SOME scope it varies over.')
print()
print('     what is NOT common is the repair. three kinds:')
print('        SPLIT   the two meanings are simply different terms.  4 instances.')
print('        CARRY   the scope is a real variable and must become a coordinate.  2 instances.')
print('        ADD     the term is genuinely absent from one side and must be constructed. 1.')
print()
print('  AND ONLY THE THIRD NEEDS A TRANSLATOR')
print('     SPLIT needs no translation: the terms were never the same.')
print('     CARRY needs a DICTIONARY: Racah recoupling coefficients translate between')
print('        coupling schemes exactly, and they exist. for n and l there is no dictionary,')
print('        only a limit - the central-field approximation is not invertible.')
print('     ADD needs a TRANSLATOR proper: a map that manufactures the missing data.')
print('        gravitational dressing is that map, and the corner edge modes are its output.')
print()
print('  THE BFV FUNCTOR IS THE GEOMETRY-TO-ALGEBRA TRANSLATOR')
print('     A : Loc -> Alg is well-defined on whole spacetimes.')
print('     it does not extend to SUBREGIONS: specifying a subregion in a')
print('     diffeomorphism-invariant theory requires dressing, and the dressing')
print('     depends on data the functor does not carry.')
print()
print('     so the reversal has a precise categorical form:')
print('        the translator exists globally and fails locally,')
print('        and the edge modes are exactly what restores it on subregions.')
print()
print('     that is a statement about ONE instance, not about a shape shared by seven.')