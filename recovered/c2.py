print('  C2 -- THE STATE CONDITION, DEFINED')
print()
print('  SETUP')
print('     N a non-expanding horizon, coordinates (u, y), u affine along generators.')
print('     cuts u1 < u2 partition it into consecutive regions')
print('        A = N_{u<u1}      B = N_{u1<u<u2}      C = N_{u>u2}')
print('     M(u) = the von Neumann algebra of N_{>u}, so   M(u2) subset M(u1).')
print('     omega = a Hadamard state, cyclic and separating (Reeh-Schlieder).')
print()
print('  THREE CANDIDATE FORMS, AND THEY ARE NOT EQUIVALENT')
print()
F=[
('C2a  SSA SATURATION  (the CTT "Markov property")',
 'S(AB) + S(BC) - S(B) - S(ABC) = 0,  i.e.  I(A:C|B) = 0',
 'PROBLEM in Type III: every term is infinite. the statement is UNSAYABLE as written.',
 're-express as a difference of ARAKI RELATIVE ENTROPIES, which are finite for any '
 'pair of normal states on any von Neumann algebra.',
 'this is the vocabulary translation identified earlier'),
('C2b  FULL MODULAR INVARIANCE',
 'sigma_t^omega ( M(u2) ) = M(u2)   for ALL t',
 'by TAKESAKI\'s conditional expectation theorem this holds iff there is a normal '
 'conditional expectation E: M(u1) -> M(u2) with omega . E = omega.',
 'TOO STRONG. null cut algebras are Type III_1 factors and admit no such normal '
 'conditional expectation. if C2b held, the inclusion would be trivial in the wrong way.',
 'this is the form to AVOID, and it is easy to write down by mistake'),
('C2c  HALF-SIDED CONTAINMENT',
 'sigma_t^{M(u1)} ( M(u2) ) subset M(u2)   for t <= 0 only',
 'this is the DEFINITION of a half-sided modular inclusion.',
 'sayable in Type III with no translation needed. it mentions only the modular group '
 'and the inclusion, both of which exist.',
 'THIS IS C2. it is what Wiesbrock converts into U(a) with P >= 0.'),
]
for a,b,c,d,e in F:
    print('  %s' % a)
    print('     condition : %s' % b)
    print('     status    : %s' % c)
    print('     note      : %s' % d)
    print('     -> %s' % e)
    print()
print('  THE RELATION BETWEEN THEM')
print('     C2b  =>  C2c        full invariance implies half-sided containment, trivially')
print('     C2c  does NOT imply C2b   -- the containment is strict, and that strictness')
print('                                 is exactly what makes the generator NONZERO')
print('     C2a  is what CTT PROVE on a null plane, and it is what makes K_A local,')
print('          which is how they reach C2c.')
print()
print('     so the logical order is:   C2a  ->  K local  ->  C2c  ->  U(a), P >= 0')
print('     and C2b sits OUTSIDE the chain as a condition that must FAIL.')
print()
print('  C2, STATED FOR AN ISOLATED HORIZON')
print()
print('     Let N be a non-expanding horizon with no Killing field, omega a Hadamard')
print('     state on the induced algebra, and M(u) the algebra of N_{>u}.')
print()
print('     C2 :   Delta_{M(u1)}^{it}  M(u2)  Delta_{M(u1)}^{-it}  subset  M(u2)')
print('            for all t <= 0, and all u1 < u2.')
print()
print('     equivalently, by Wiesbrock: there exists a one-parameter unitary group')
print('     U(a) = e^{iPa} with P >= 0 such that U(a) M(u) U(-a) subset M(u), a >= 0.')
print()
print('  WHAT IS AND IS NOT AVAILABLE FOR IT')
A=[('the algebra M(u)','locally covariant QFT on N','AVAILABLE'),
   ('the inclusion M(u2) subset M(u1)','causal inclusion of cross-sections','AVAILABLE'),
   ('a cyclic separating omega','Hadamard state + Reeh-Schlieder','AVAILABLE'),
   ('Delta^{it}','Tomita-Takesaki from the above','AVAILABLE'),
   ('factorisation of the algebra over generators','computed: the bracket is diagonal in y '
    'because the symplectic form has no transverse derivative','COMPUTED, C1'),
   ('factorisation / Markov property of the STATE','---','THE OPEN QUESTION')]
print('  %-44s %-52s %s' % ('ingredient','source','status'))
for a,b,c in A: print('  %-44s %-52s %s' % (a,b,c))
print()
print('  AND WHY C1 DOES NOT SETTLE C2')
print('     C1 says the ALGEBRA is a direct integral over generators:  A(N) = int^+ A_y.')
print('     a state on a direct integral need NOT be a product over the fibres.')
print('     the Hadamard condition constrains the SHORT-DISTANCE behaviour of the')
print('     two-point function; it says nothing about correlations BETWEEN generators')
print('     at finite transverse separation.')
print()
print('     -> C1 gives the tensor decomposition. C2 asks whether the state respects it')
print('        in the way that makes the modular flow preserve the later cuts.')
print('        those are independent, and the second is the whole remaining problem.')