print('  WORKING BACKWARDS FROM THE DESIRED OUTPUT')
print()
print('  WANT:  K_A = 2 pi int dx+ d^{d-2}y  (x+ - A(y))  T_{++}(x+, y)')
print('         i.e. the modular Hamiltonian is a LOCAL integral along the generators.')
print()
S=[
('B1','K_A local along generators',
 'the modular flow moves points along each generator, with a y-dependent velocity, '
 'and does not mix generators',
 'WANTED'),
('B2','the modular flow does not mix generators',
 'Delta^{it} decomposes as a DIRECT INTEGRAL over y:  Delta = int^{+} Delta_y dy',
 'implied by B3'),
('B3','the algebra factorises over generators',
 'A(N) = int^{+} A_y dy   -- each null generator carries its own independent algebra',
 'THIS IS THE ROOT'),
('B4','what makes B3 true on a null plane?',
 'the induced commutator on a null surface is proportional to delta(y - y\') times a '
 'CHIRAL kernel in x+. different generators commute.',
 'a property of the INDUCED field data'),
('B5','and where does THAT come from?',
 'the CHARACTERISTIC INITIAL VALUE PROBLEM: on a null hypersurface the free data is '
 'specified independently along each generator. the constraint equations propagate '
 'ALONG generators (Raychaudhuri), not across them.',
 'a property of NULL HYPERSURFACES, not of symmetry'),
]
for a,b,c,d in S:
    print('  %-4s %s' % (a,b)); print('  %-4s   %s' % ('',c)); print('  %-4s   [%s]' % ('',d)); print()
print('  THE CLAIM THIS SUGGESTS')
print('     CTT prove B3 using conformal symmetry (OPE route) or the null plane\'s')
print('     translation structure (AQFT route).')
print('     but B5 says B3 might follow from the CHARACTERISTIC STRUCTURE of any null')
print('     hypersurface: the transverse coordinates label independent free data.')
print('     -> if so, the needed input exists under a different name and no new symmetry')
print('        is required.')
print()
print('  WHAT WOULD HAVE TO BE CHECKED, IN ORDER')
C=[('C1','does the induced field commutator on an NEH vanish between distinct generators?',
    'this is a computation in the characteristic formulation. for FREE fields it should '
    'follow from the null Green function being supported on the generator.',
    'plausible, uncomputed here'),
   ('C2','does the vacuum/Hadamard state respect that factorisation?',
    'the ALGEBRA factorising is not enough - the STATE must be a product across generators, '
    'or at least Markov across them.',
    'THE REAL QUESTION, and it is the same question as I(A:C|B) = 0'),
   ('C3','does the direct integral survive interactions?',
    'CTT handle interacting theories by the AQFT route, which uses the plane. for a general '
    'NEH neither route is available.',
    'open'),
]
print('  %-4s %s' % ('','requirement'))
for a,b,c,d in C:
    print('  %-4s %s' % (a,b)); print('  %-4s   %s' % ('',c)); print('  %-4s   -> %s' % ('',d)); print()
print('  AND HERE IS WHERE THE BACKWARD PASS LANDS')
print()
print('     C1 is about the ALGEBRA and is plausibly general.')
print('     C2 is about the STATE and is EXACTLY the Markov condition we started from.')
print()
print('     so working backwards does NOT reduce the problem to something new.')
print('     it returns to the same place: does the state factorise / is it Markov')
print('     across cuts on the horizon.')
print()
print('  WHICH IS INFORMATIVE, NOT CIRCULAR')
print('     the forward chain said: Markov => locality => HSMI => ANEC.')
print('     the backward chain says: locality REQUIRES the state to factorise across')
print('     generators, which is the Markov property again.')
print('     -> Markov and locality are not two steps. they are one condition seen twice,')
print('        and the algebraic factorisation (C1) is the only genuinely separate input.')
print()
print('  SO THE MINIMAL TARGET, CORRECTED')
print('     NOT: "prove locality without symmetry, then get Markov"')
print('     BUT: "show the Hadamard state on an NEH is Markov across cuts"')
print('          - and locality follows, given the algebraic factorisation C1.')
print()
print('     the chain has one fewer independent step than the forward reading suggested.')