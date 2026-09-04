print('  STATEMENT vs PROOF, LINK BY LINK')
print()
print('  a STATEMENT generalises when its TERMS are defined in the wider setting.')
print('  a PROOF generalises when every STEP\'S HYPOTHESIS is available there.')
print()
L=[
('Petz 1986  sufficiency',
 'equality in monotonicity of relative entropy <=> a recovery channel exists',
 'terms: relative entropy, channels, von Neumann algebras. ALL defined in Type III.',
 'the theorem IS stated for von Neumann algebras. no finite-dimensional step.',
 'STATEMENT yes','PROOF yes','fully general already'),
('Hayden-Jozsa-Petz-Winter 2004',
 'SSA saturation <=> short quantum Markov chain',
 'terms: S(A), S(AB), S(ABC). IN TYPE III THESE DO NOT EXIST - all infinite.',
 'the proof uses Koashi-Imoto, a finite-dimensional structure theorem.',
 'STATEMENT needs RE-EXPRESSION','PROOF no',
 're-express via Araki relative entropies: I(A:C|B) as a difference of relative entropies'),
('Casini-Teste-Torroba 2017  locality',
 'K_A is a local integral of T_++ along the null generators',
 'terms: null surface, cuts, stress tensor, modular Hamiltonian. ALL available on an NEH.',
 'proof 1: OPE for twist fields - needs a CFT / conformal symmetry.\n'
 '           proof 2: AQFT argument - needs the null PLANE and its translation structure.',
 'STATEMENT yes','PROOF no',
 'THE WEAK LINK: both proofs need a symmetry the statement does not mention'),
('Wiesbrock 1993/97  (Araki-Zsido 2004)',
 'HSMI <=> a positive-generator unitary group exists',
 'terms: von Neumann algebras, modular flow, inclusions. ALL general.',
 'purely algebraic. Araki-Zsido extended it from a cyclic separating VECTOR to a '
 'faithful normal semifinite WEIGHT.',
 'STATEMENT yes','PROOF yes','fully general already'),
('Borchers 1992',
 'a positive-generator U determines the commutation relations with Delta and J',
 'terms: as above.','purely algebraic.',
 'STATEMENT yes','PROOF yes','fully general already'),
]
for a,b,c,d,e,f,g in L:
    print('  %s' % a)
    print('     statement : %s' % b)
    print('     terms     : %s' % c)
    print('     proof     : %s' % d)
    print('     -> %-28s %-12s   %s' % (e,f,g))
    print()
print('  THE TALLY')
print('     fully general (statement AND proof) : 3   Petz, Wiesbrock, Borchers')
print('     statement needs re-expression       : 1   HJPW - no entropies in Type III')
print('     proof genuinely blocked             : 1   CTT locality')
print()
print('  SO THE DIFFERENCE, PRECISELY')
print()
print('     for HJPW it is a VOCABULARY problem. S(A) is infinite in Type III, so the')
print('     statement as written is not even false there - it is unsayable. the repair')
print('     is to re-express I(A:C|B) as a difference of ARAKI RELATIVE ENTROPIES,')
print('     which are finite and defined for any pair of states on any von Neumann algebra.')
print('     that is a translation, and Petz supplies the target language.')
print()
print('     for CTT it is a HYPOTHESIS problem. the statement is perfectly sayable on an')
print('     NEH - a modular Hamiltonian, a stress tensor, cuts along generators. what is')
print('     missing is the symmetry both proofs consume: conformal invariance in one,')
print('     the null plane\'s translation structure in the other. neither is available.')
print()
print('  WHICH IS THE SAME DISTINCTION THIS PAPER MAKES ABOUT INDICES')
print('     a term is EXPRESSIBLE if the vocabulary carries it   -> HJPW fails here')
print('     a constraint is CARRIABLE if the arity permits it    -> CTT fails here')
print('     unsayable, versus sayable-and-unproved. two different repairs:')
print('        translate the vocabulary   (HJPW: entropies -> relative entropies)')
print('        find a new argument        (CTT: no substitute for the symmetry)')
print()
print('  AND IT LOCATES THE WORK')
print('     three links need nothing.')
print('     one needs a translation that is standard and already exists.')
print('     ONE needs a new proof, and it is the locality of the modular Hamiltonian')
print('     on a null surface without conformal or translation symmetry.')