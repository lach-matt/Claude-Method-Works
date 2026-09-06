OLD=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
NEW=[
 ('X_exp','explicit Lorentz violation in the Lagrangian',4,'split from X','ghost condensate has X_exp=0'),
 ('X_spon','spontaneous Lorentz breaking (VEV picks a frame)',2,'split from X','ghost condensate has X_spon=1'),
 ('Sc','CHSH correlation strength',3,'unchanged - clean',''),
 ('IC','information causality',3,'unchanged - clean',''),
 ('U_open','open-system non-unitarity (CPTP, Lindblad)',3,'split from U','metric intact; Nikolic operators'),
 ('U_ghost','indefinite metric / ghosts',2,'split from U','the spin-statistics metric postulate'),
 ('NEC_pt','pointwise NEC violation (scale-graded)',5,'split from NEC','Casimir = 1; ours'),
 ('NEC_ach','achronal ANEC violated',2,'split from NEC','MMP has NEC_pt>=2, NEC_ach=0'),
 ('L_dyn','nonlinear evolution, state space linear (Weinberg)',2,'split from L','Abrams-Lloyd, Polchinski'),
 ('L_kin','nonlinear state space (superposition fails)',2,'split from L','would abolish Lambda'),
 ('SD_obs','spacelike commutativity of observables',2,'split from SD','spin-statistics hypothesis'),
 ('SD_field','spacelike commutativity of fields',2,'split from SD','Burgoyne: wrong choice -> no theory'),
 ('DNc','cloning fidelity',3,'unchanged - partial conflation noted',''),
 ('DNd','state discrimination',3,'unchanged - partial conflation noted',''),
 ('EOM','derivative order of the equations of motion',2,'NEW','Buniy operative hypothesis'),
]
print('  THE CORRECTED ALPHABET')
print('  %-9s %-46s %-5s %s' % ('letter','meaning','rungs','provenance'))
for a,b,r,p,ev in NEW:
    print('  %-9s %-46s %-5d %s' % (a,b,r,p))
    if ev: print('  %-9s %s' % ('', '  '+ev))
print()
print('     old alphabet: %d letters   new: %d letters' % (len(OLD),len(NEW)))
box=1
for _,_,r,_,_ in NEW: box*=r
print('     ambient box before any closure: %d' % box)
print()
print('  WHAT BECOMES EXPRESSIBLE')
EXP=[('Buniy jurisdiction','X_exp = 0 AND EOM = 2nd-order',
      'was approximated by X=0 alone; the operative hypothesis is now an axis'),
     ('the ghost condensate','X_exp=0, X_spon=1, EOM=higher, NEC_pt>=2',
      'Lorentz-invariant THEORY, Lorentz-violating VACUUM, higher derivatives - outside Buniy'),
     ('MMP long wormhole','NEC_pt=2, NEC_ach=0, X_exp=0, U_open=0',
      'violates ANEC, satisfies achronal ANEC - now distinguishable'),
     ('spin-statistics hypotheses','X_exp=0, SD_obs=0, U_ghost=0',
      'all three postulates now have letters'),
     ('Burgoyne boundary','SD_field=1 -> the theory does not exist',
      'a cell that is not a universe, now markable')]
for a,b,c in EXP:
    print('     %-24s %s' % (a,b))
    print('     %-24s %s' % ('',c))
print()
print('  WHAT IS STILL NOT EXPRESSIBLE')
MISS=['CPT invariance (Greenberg edge into X_exp)',
      'energy-momentum conservation (the other BSP disjunct)',
      'the generalised second law (a charger trigger with no axis)',
      'weak cosmic censorship (predicted by pair-completion)',
      'the holographic / Bekenstein bound (predicted)',
      'black-hole information recovery (predicted)',
      'global symmetry conservation',
      'the equivalence principle',
      'jurisdiction conditions: causality, field content, dimension, flatness,',
      '   simple connectedness, determinism, ultralocality, stability, minimal coupling']
for m in MISS: print('     %s' % m)
print()
print('     letters added this pass : %d' % (len(NEW)-len(OLD)))
print('     letters still missing   : at least %d' % (len(MISS)-1))
print()
print('  THE POINT')
print('     item 2 asks whether Buniy extends to Lorentz-violating theories.')
print('     in the OLD alphabet that question is ambiguous: X conflated two meanings,')
print('     and the counterexample turns on which one. in the NEW alphabet it is sharp:')
print('        does Buniy hold for X_exp >= 1 with EOM = 2nd-order?')
print('     that is a well-posed question about a theorem, and it can now be asked.')