print('  WHAT DO THE TWO KNOWN ROUTES SHARE?')
print()
R=[('Killing route','the Killing parameter v with L_xi = 0 identifies points across generators',
    'Killing time varies along the generators and is shared between them',
    'CLOCK: the Killing parameter'),
   ('corner route','P_alpha proportional to int alpha e^Gamma L_l mu, and L_l mu = Theta mu',
    'the AREA FORM varies along the generators when Theta is nonzero',
    'CLOCK: the area')]
for a,b,c,d in R:
    print('  %-14s %s' % (a,b)); print('  %-14s   %s' % ('',c)); print('  %-14s   %s' % ('',d)); print()
print('  THE COMMON MECHANISM')
print('     both supply a quantity that VARIES ALONG THE GENERATORS and is')
print('     comparable between them. that is what fixes the relative affine origin,')
print('     which is the one missing ingredient.')
print()
print('  WHAT VARIES ON AN ISOLATED HORIZON?')
V=[('the induced metric q_ab','L_l q_ab = 0','NEH definition'),
   ('the area form mu','L_l mu = Theta mu = 0','Theta = 0'),
   ('the expansion Theta','identically zero','NEH definition'),
   ('the shear sigma_ab','zero, by Raychaudhuri + energy condition','follows from Theta = 0'),
   ('the connection 1-form omega_a','L_l omega_a = 0','WEAKLY isolated horizon condition'),
   ('the full intrinsic connection D_a','L_l D_a = 0','ISOLATED horizon condition'),
   ('surface gravity kappa','constant','zeroth law on a WIH'),
   ('the Weyl scalar Psi_2','constant on the horizon','isolated horizon result')]
print('  %-30s %-34s %s' % ('quantity','behaviour','source'))
for a,b,c in V: print('  %-30s %-34s %s' % (a,b,c))
print()
print('  -> NOTHING INTRINSIC VARIES. that is the DEFINITION of an isolated horizon:')
print('     a black hole in equilibrium, with time-independent intrinsic geometry.')
print()
print('  SO THE ANSWER TO "IS THERE A THIRD ROUTE?"')
print()
print('     no intrinsic geometric route can exist. a clock requires time dependence,')
print('     and the surface is defined by having none. the two known routes are not')
print('     two of many - they are the only two geometric quantities available, and')
print('     both are switched off by the same defining condition.')
print()
print('     -> the two routes do NOT suggest a third. they exhaust the geometry.')
print()
print('  WHAT IS LEFT')
L=[('the bulk fields off the horizon','an NEH admits radiation arbitrarily close to it but not crossing',
    'a clock outside the surface, not on it'),
   ('the STATE',"Delta^{it} exists whenever Omega is cyclic and separating - CYC gives MOD free",
    'the modular flow IS a one-parameter group, and it does not need geometry'),
   ('the algebra itself','Borchers-Wiesbrock relate U(a) and Delta^{it} without reference to a metric',
    'the relation is algebraic: Delta^{it} U(a) Delta^{-it} = U(e^{-2 pi t} a)')]
print('  %-34s %s' % ('candidate source','why'))
for a,b,c in L: print('  %-34s %s' % (a,b)); print('  %-34s   %s' % ('',c))
print()
print('  AND THAT IS EXACTLY THE PROGRAMME ALREADY PROPOSED')
print('     "it would be interesting to develop the modular part of the construction in')
print('      a fully algebraic form for more general spacetimes, using half-sided modular')
print('      inclusions and Borchers\' theorem as the starting point rather than as a')
print('      posteriori interpretation. In that formulation, the affine group would emerge')
print('      DIRECTLY FROM THE MODULAR DATA of a half-line algebra and a translation-')
print('      invariant cyclic and separating state."')
print('        -- Modular theory and affine representations on the Rindler horizon, May 2026')
print()
print('  SO THE THIRD ROUTE IS NAMED, AND IT IS NOT GEOMETRIC')
print('     derive U(a) FROM Delta, rather than deriving both from a metric quantity.')
print('     on an isolated horizon that is the only remaining direction, because the')
print('     geometry is exhausted by construction.')