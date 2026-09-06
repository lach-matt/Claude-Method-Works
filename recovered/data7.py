import json
D=json.load(open('data4.json'))
D['neh']={
 'target':'half-sided modular inclusion on an isolated horizon: a non-expanding null '
          'hypersurface with no Killing field',
 'why_that_cell':'two routes to the translation exist. the Killing parameter, and the corner '
   'charge P_alpha, which is proportional to L_l mu = Theta mu. an isolated horizon has '
   'Theta = 0 exactly and no Killing field, so both are switched off. Theta =/= 0 or a Killing '
   'field present, and a route exists. it is a boundary point, not a region.',
 'exhaustion':'no third GEOMETRIC route can exist: both known routes need a quantity varying '
   'along the generators, and an isolated horizon is DEFINED by nothing intrinsic varying '
   '(L_l q_ab = 0, L_l D_a = 0, kappa and Psi_2 constant).',
 'chain':[('I(A:C|B) = 0','vanishing conditional mutual information','the Markov property'),
          ('short quantum Markov chain','Hayden-Jozsa-Petz-Winter 2004',''),
          ('exact Petz recovery','Petz 1986, stated FOR VON NEUMANN ALGEBRAS',''),
          ('K_A local: an integral of T_++','Casini-Teste-Torroba 2017',''),
          ('sigma_t(M(u+d)) subset M(u+d)','half-sided modular inclusion',''),
          ('U(a) with P >= 0','Wiesbrock 1993/97; Araki-Zsido 2004',''),
          ('P = integral of T_++','identification via dressed commutators',''),
          ('the achronal ANEC','','')],
 'generalisation':{'fully general':['Petz','Wiesbrock','Borchers'],
   'needs re-expression':['Hayden-Jozsa-Petz-Winter: S(A) is infinite in Type III, so the '
     'statement is unsayable; re-express via Araki relative entropies'],
   'proof blocked':['Casini-Teste-Torroba locality: the OPE route needs conformal symmetry, '
     'the AQFT route needs the null plane. neither is available on an isolated horizon.'],
   'distinction':'a STATEMENT generalises when its terms are defined in the wider setting; '
     'a PROOF generalises when every step\'s hypothesis is available there. one failure of '
     'each kind, and they need different repairs: translate the vocabulary, or find a new argument.'},
 'C1':{'question':'does the induced bracket factorise across null generators?',
   'answer':'YES, computed',
   'basis':'the presymplectic potential on a null surface is theta = delta phi L_l phi eta, '
     'which contains NO transverse derivative. so Omega is block diagonal in y, so Omega^{-1} '
     'is, so { phi(u,y), phi(u\',y\') } = (1/4 sqrt(q)(y)) sgn(u-u\') delta(y-y\').',
   'computed':'symplectic form built and inverted at 4, 6 and 8 generators; off-generator block '
     'of the inverse is 0.000e+00 at every size, for arbitrary y-dependence of sqrt(q). '
     'a control adding an artificial d_y term makes it nonzero immediately.',
   'scope':'holds for ANY NON-DERIVATIVE interaction, since V(phi) contributes no boundary '
     'derivative term. FAILS for derivative couplings, which add transverse rungs.',
   'graph':'free or V(phi): a DISJOINT UNION of paths, one per generator - a forest, strictly '
     'simpler than a caterpillar. derivative coupling: a LADDER, which has cycles, and the '
     'tree certificate is lost exactly as at Lambda_9 prime.',
   'comparison':'CTT cover general interacting theories on the null PLANE. this argument is '
     'more general in the geometry and less general in the interaction. neither contains the other.'},
 'C2':{'statement':'Delta_{M(u1)}^{it} M(u2) Delta_{M(u1)}^{-it} subset M(u2) for all t <= 0 '
     'and all u1 < u2, on a non-expanding non-Killing horizon with a Hadamard state',
   'equivalently':'by Wiesbrock, there exists U(a) = e^{iPa} with P >= 0 and '
     'U(a) M(u) U(-a) subset M(u) for a >= 0',
   'wrong_forms':[('SSA saturation as written','unsayable in Type III: every entropy is infinite'),
     ('full modular invariance sigma_t(N) = N for all t','TOO STRONG. by Takesaki it would give '
      'a normal conditional expectation, which Type III_1 factors do not admit. and it would '
      'make the generator ZERO.')],
   'status':'OPEN. C1 gives the tensor decomposition; C2 asks whether the state respects it. '
     'the Hadamard condition constrains short-distance behaviour and says nothing about '
     'correlations between generators at finite transverse separation.'},
 'converter':{'what':'half-sided modular inclusion, via Borchers and Wiesbrock',
   'in':'(M, N subset M, Omega) with sigma_t(N) subset N. no manifold, no metric, no coordinates.',
   'out':'U(a) = e^{iPa}, P >= 0, with Delta^{it} U(a) Delta^{-it} = U(e^{-2 pi t} a) and '
     'J U(a) J = U(-a) -- the affine ax+b group acting on a LINE',
   'reading':'a null generator with its affine parameter, manufactured from an inclusion of '
     'algebras. Leutheusser-Liu use this for emergent horizons and emergent time.',
   'inversion':'in holography the algebra is given and the geometry derived. on an isolated '
     'horizon the geometry is GIVEN and the algebraic certificate is what is missing.',
   'caution':'the theorem produces a group representation. identifying that group with the '
     'horizon\'s own null line is a further step, free on a null plane and not free here.'},
 'dimensional_ledger':{'unit':'one HSMI produces exactly ONE affine line: one real parameter',
   'assembly':'higher dimension comes from SEVERAL HSMIs - Borchers 2d embedding, Wiesbrock '
     'modular intersections, and the null-plane fibre decomposition is one HSMI per generator',
   'accounting':'d - 1 = 1 + (d - 2). the 1 comes from HSMI along a generator; the (d-2) comes '
     'from the transverse direct integral, which no HSMI supplies.',
   'consequence':'the two open pieces are dimensionally distinct, which is why one yielded to '
     'a symplectic computation and the other has not.',
   'not_established':'that ONLY a dimensional shift can convert algebra to geometry. and the '
     'status bit is 0-dimensional while the affine line is 1-dimensional; they are different '
     'objects and must not be collapsed.'}}
D['withdrawals_2'].append(('TRANS gates the trace',
 'the crossed product is by the MODULAR flow, so the trace needs MOD and COND only. TRANS gates '
 'the relation BETWEEN cuts: the GSL and the QFC. an isolated horizon would carry an entropy at '
 'each cut and no law relating them.'))
D['withdrawals_2'].append(('the vanishing of the two-sided term at Theta = 0 is favourable',
 'the whole generator vanishes there, since P_alpha is proportional to Theta. a limit read as a '
 'simplification when it was the obstruction.'))
D['withdrawals_2'].append(('the modular relocation is circular',
 'it is directed: HSMI implies the ANEC, not the reverse. Chandrasekaran-Flanagan warn explicitly '
 'that the identification P = integral T_++ is not the method for proving positivity.'))
D['error_class_2']['instances']=30
json.dump(D,open('data4.json','w'),indent=1,default=str)
print('recorded. neh keys:',list(D['neh'].keys()))
print('withdrawals_2:',len(D['withdrawals_2']),' errors:',D['error_class_2']['instances'])