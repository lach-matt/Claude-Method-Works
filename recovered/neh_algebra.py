print('  THE ALGEBRA, INGREDIENT BY INGREDIENT')
print()
ING=[
('CYC','a state Omega cyclic and separating for the cut algebra M(u)',
 'Omega in H,  M(u)Omega dense,  x Omega = 0 => x = 0',
 'supplies: the domain on which Tomita-Takesaki runs'),
('MOD','the modular objects',
 'S = J Delta^{1/2},   sigma_t = Ad(Delta^{it}),   sigma_t(M) = M',
 'supplies: a one-parameter automorphism group of M -- the thing T3 crosses by'),
('NEST','a partially ordered family of algebras',
 'u2 > u1  =>  M(u2) subset M(u1)',
 'supplies: the inclusion. NO parametrisation needed - causal inclusion suffices'),
('EDGE','corner charges conjugate to the edge modes',
 'A_beta = (1/8pi) int_S beta mu ,   P_alpha  conjugate to Upsilon_0',
 '{P_alpha, O(p)} = -alpha e^{Gamma} L_l O(p)   -- the dressing makes them act non-trivially'),
('TRANS','a positive-generator translation',
 'U(a) = e^{iPa},  P >= 0,  U(a) M(u) U(-a) subset M(u)  for a >= 0',
 'supplies: motion BETWEEN cuts. Borchers-Wiesbrock: this IS half-sided modular inclusion'),
('COND','projection onto a sharp corner location',
 'non-selective measurement of Upsilon_0^+  ->  the group reduces from C^inf(S^{d-2}) to R_s',
 'supplies: the reduction to Takesaki\'s hypothesis'),
]
for a,b,c,d in ING:
    print('  %-6s %s' % (a,b))
    print('  %-6s   %s' % ('',c))
    print('  %-6s   %s' % ('',d))
    print()
print('  WORKING BACKWARDS FROM THE OUTPUT')
print()
print('     WANT:  tau, a faithful semifinite normal trace, hence S = -tr[rho log rho]')
print()
print('     tau exists  <=  M crossed_sigma R  is semifinite            [T3 Takesaki]')
print('        the crossed product is by SIGMA, the modular flow.')
print('        so it needs:  MOD  (something to cross by)')
print('                  and COND (the group must be R, not C^inf(S^{d-2}))')
print('        it does NOT need TRANS.')
print()
print('     -> TRACE  <=  MOD + COND   ... and MOD <= CYC')
print('        every one of those is present on an NEH.')
print()
print('  SO WHAT DOES TRANS ACTUALLY GATE?')
print()
G=[('a Type II_inf algebra at ONE cut','MOD + COND','available on an NEH'),
   ('an entropy at that cut','TRACE','available on an NEH'),
   ('nesting IMPLEMENTED by unitaries','NEST + TRANS',
    'U(du) M(u) U(-du) subset M(u): needs the translation'),
   ('the GSL, d/du S_gen >= 0','the above + monotonicity of tau under inclusion',
    'BLOCKED without TRANS'),
   ('the QFC, d2/du2 S_gen <= 0','GSL + the Borchers relation between U and Delta',
    'BLOCKED without TRANS')]
print('  %-38s %-34s %s' % ('consequence','requires','on an isolated horizon'))
for a,b,c in G: print('  %-38s %-34s %s' % (a,b,c))
print()
print('  THE CORRECTED MAP')
print('     WRONG (my previous version):  TRANS gates TRACE.')
print('     RIGHT:                        TRANS gates the RELATION BETWEEN CUTS.')
print()
print('     on an isolated horizon you would have:')
print('        a Type II_inf algebra and a von Neumann entropy AT EACH CUT,')
print('        and no theorem relating the entropy at one cut to the entropy at another.')
print()
print('     that is a sharper deprivation than "no entropy". it is:')
print('        an entropy with no second law.')
print()
print('  AND IT EXPLAINS THE PAPER\'S OWN SCOPE LINE')
print('     Chandrasekaran-Flanagan prove the GSL for "non-stationary linearized')
print('     perturbations of Killing horizons" - not for Killing horizons alone, and')
print('     not for general NEHs. the perturbative regime is exactly where TRANS can be')
print('     imported from the background Killing structure.')
print()
print('  WHAT A PROOF WOULD HAVE TO PRODUCE, RESTATED')
print('     not a trace. not an entropy. not a geometric modular flow (Sorce excludes it).')
print('     a one-parameter unitary group with POSITIVE generator, on a non-expanding')
print('     horizon with no Killing field, satisfying U(a) M(u) U(-a) subset M(u).')
print('     by Wiesbrock that is exactly half-sided modular inclusion, and by Borchers')
print('     it then automatically satisfies Delta^{it} U(a) Delta^{-it} = U(e^{-2 pi t} a).')