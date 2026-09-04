print('  COUNTING DIMENSIONS ACROSS THE CONVERTER')
print()
O=[('the status bit  (semifiniteness)','0','a single binary value. no parameter.',
    'III_1 or II_inf. Takesaki. no continuum.'),
   ('the modular flow  Delta^{it}','1','one real parameter t','always present given CYC'),
   ('the translation  U(a)','1','one real parameter a','the OUTPUT of Borchers-Wiesbrock'),
   ('the affine group  ax+b','1 (space)','2 generators acting on a 1-DIMENSIONAL line',
    'translations a -> a+s, dilations a -> e^{2 pi t} a'),
   ('a null generator','1','one affine parameter','the geometric object identified with the above'),
   ('a null hypersurface','d-1','1 along generators + (d-2) transverse',
    'the transverse directions are NOT produced by one HSMI'),
   ('Minkowski space','d','','')]
print('  %-38s %-10s %-46s %s' % ('object','dim','','note'))
for a,b,c,d in O: print('  %-38s %-10s %-46s %s' % (a,b,c,d))
print()
print('  THE UNIT IS 1')
print('     one half-sided modular inclusion produces exactly ONE affine line.')
print('     not a surface, not a spacetime. one parameter.')
print()
print('  AND HIGHER DIMENSION IS ASSEMBLED FROM UNITS')
A=[('Borchers 1992','a 2d theory covariant under translations ONLY can be embedded into '
    'one covariant under the whole Poincare group','1D units -> 2D Poincare'),
   ('Wiesbrock, modular intersections','several HSMIs in appropriate RELATIVE POSITION '
    'generate higher symmetry groups','the assembly rule'),
   ('Morinelli-Tanimoto-Wegener 2021','inclusions of null plane regions are HSMI; the modular '
    'operator DECOMPOSES INTO FIBRES over the transverse directions','d-1 = 1 + (d-2), '
    'one HSMI per generator'),
   ('Longo-Lechner et al 2025','the relative positions of two HSMIs in a common environment '
    'were UNKNOWN until recently','the assembly rule is still being worked out')]
print('  %-34s %-72s' % ('result','content'))
for a,b,c in A:
    print('  %-34s %s' % (a,b[:72]))
    if len(b)>72: print('  %-34s %s' % ('',b[72:]))
    print('  %-34s -> %s' % ('',c))
print()
print('  SO WHAT IS SUPPORTED')
S=[('the converter outputs 1 dimension','YES','the affine group of THE LINE. computed from the '
    'Borchers relations, one real parameter.'),
   ('higher dimension is built from 1D units','YES','Borchers 2d embedding; Wiesbrock modular '
    'intersections; the null-plane fibre decomposition is literally one HSMI per generator.'),
   ('the transverse directions come from ELSEWHERE','YES','they come from the direct integral '
    'over y - that is C1, and it is a separate input, not produced by any HSMI.'),
   ('a dimensional shift is INVOLVED','YES','an algebra carries no dimension; a 1-parameter '
    'group does. the converter creates one where there was none.'),
   ('ONLY a dimensional shift can do it','NOT ESTABLISHED','this is a universal claim about '
    'all possible converters. I have one converter and no argument that it is the only kind.'),
   ('binary is the interlingua because it is 1D','CONFUSES TWO THINGS','the status bit is '
    '0-dimensional, not 1-dimensional. the affine line is 1-dimensional. they are different '
    'objects and the argument slides between them.')]
print('  %-42s %-18s %s' % ('claim','verdict','basis'))
for a,b,c in S:
    print('  %-42s %-18s %s' % (a,b,c[:60]))
    if len(c)>60: print('  %-42s %-18s   %s' % ('','',c[60:]))
print()
print('  THE DISTINCTION THAT MATTERS')
print('     the BIT (semifiniteness) is 0-dimensional: one value, no parameter.')
print('     the LINE (the affine group) is 1-dimensional: one continuous parameter.')
print()
print('     the crossed product flips the bit. Borchers-Wiesbrock produces the line.')
print('     they are different operations with different outputs, and the session')
print('     has already once collapsed TRANS and TRACE by treating them as one.')
print()
print('  WHAT I WOULD KEEP')
print('     the 1D unit is real and computed: one HSMI, one affine line, and d-1')
print('     dimensions on a null surface require one HSMI per generator PLUS the')
print('     transverse direct integral, which no HSMI supplies.')
print()
print('     that is a dimensional accounting, and it is checkable.')
print('     the universal claim is not, and this session has withdrawn two patterns')
print('     of exactly that shape.')