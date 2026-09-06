import numpy as np
print('  THE SWITCH SPACE')
print()
print('  two switches control TRANS:')
print('     KILL   a Killing field tangent to the horizon   (present / absent)')
print('     Theta  the expansion                            (a real number)')
print()
print('  and the corner generator scales as   P_alpha  proportional to  Theta')
print('  so its MAGNITUDE vanishes at Theta = 0.')
print()
th=np.array([-0.5,-0.1,-0.01,0.0,0.01,0.1,0.5])
print('  %-10s %-14s %-14s %-14s %s' % ('Theta','|P| ~ |Theta|','corner route','Killing route','TRANS'))
for k in (True,False):
    print('  --- Killing field %s ---' % ('PRESENT' if k else 'ABSENT'))
    for t in th:
        corner = abs(t)>0
        trans = corner or k
        print('  %-10.2f %-14.3f %-14s %-14s %s'
              % (t,abs(t),'yes' if corner else 'NO','yes' if k else 'NO',
                 'available' if trans else '*** BLOCKED ***'))
    print()
print('  THE STRUCTURE')
print('     with a Killing field : TRANS available everywhere, including Theta = 0.')
print('     without one          : TRANS available for all Theta =/= 0,')
print('                            and blocked at the single point Theta = 0.')
print()
print('  SO THE ISOLATED HORIZON IS A BOUNDARY POINT, NOT A REGION')
print('     it is the zero-crossing of the corner generator, with the other switch off.')
print('     measure zero in Theta, and a non-generic condition on the metric.')
print()
print('  WHAT IS DEFENSIBLE ABOUT CALLING IT THE LOCUS WHERE THE BIT FLIPS')
D=[('the generator vanishes there','P_alpha proportional to L_l mu = Theta mu, and Theta = 0','YES, computed'),
   ('it is a boundary in Theta','expanding on one side, contracting on the other','YES, structural'),
   ('both routes fail exactly there','the corner route needs Theta =/= 0, the Killing route needs KILL','YES, computed'),
   ('the TYPE flips there','III_1 -> II_inf is done by the crossed product, which needs MOD and COND',
    'NO. the type flip does not depend on Theta at all. TRACE survives at Theta = 0.'),
   ('it is where the translator switches','the translator is the crossed product; it works there',
    'NO. what fails at Theta = 0 is the DYNAMICS, not the translation.')]
print('  %-34s %-52s %s' % ('claim','basis','verdict'))
for a,b,c in D: print('  %-34s %-52s %s' % (a,b,c))
print()
print('  THE CORRECTION')
print('     the isolated horizon IS the locus where both routes to the TRANSLATION')
print('     vanish. it is NOT the locus where the translator switches, because the')
print('     translator - the crossed product by the modular flow - works there.')
print()
print('     TRACE survives at Theta = 0. what does not survive is the RELATION')
print('     BETWEEN CUTS. so the bit that flips is not III_1 -> II_inf.')
print('     it is: does the one-parameter family of Type II_inf algebras have a')
print('     unitary implementing motion along it.')
print()
print('     an entropy at every cut, and no flow connecting them.')