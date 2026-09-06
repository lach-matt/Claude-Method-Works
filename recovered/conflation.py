NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
AUDIT=[
 ('X','causal ladder 0-3',
   'CONFLATED','spontaneous vs explicit Lorentz breaking; and stated vs operative hypothesis',
   'ghost condensate is a Lorentz-invariant THEORY with a Lorentz-violating VACUUM',
   'lattice (via spin-statistics) + l-bound'),
 ('Sc','CHSH 2 / 2sqrt2 / 4',
   'clean','graded by a measured number; no ambiguity in what the rung asserts',
   '-','lattice (Sc>=3 breaks the spin-statistics conclusion)'),
 ('IC','information causality',
   'clean','m>0 vs m=0 is explicit in the grading',
   '-','none'),
 ('U','unitary / Lindblad / BSP-violating',
   'CONFLATED','open-system non-unitarity (CPTP, metric intact) vs ghosts (indefinite metric)',
   'the spin-statistics postulate is about the METRIC, which Lindblad preserves',
   'none as graded; the ghost rung WOULD act'),
 ('NEC','intact/pointwise/ANEC/macroscopic/QI',
   'CONFLATED','ANEC vs ACHRONAL ANEC',
   'MMP violates ANEC and satisfies achronal ANEC; different theorems apply',
   'measure only'),
 ('L','linear / nonlinear',
   'CONFLATED','dynamical (Weinberg, state space linear) vs kinematical (state space nonlinear)',
   'Lambda uses state-space structure only, never the evolution law',
   'none as graded; the kinematical rung would DESTROY the lattice'),
 ('SD','microcausality holds / fails',
   'CONFLATED','commutativity of OBSERVABLES vs of FIELDS',
   'wrong field choice -> fields identically zero -> the theory does not exist (Burgoyne)',
   'lattice, but only under the observable reading'),
 ('DNc','cloning: optimal/beyond/perfect',
   'partial','deterministic vs probabilistic cloning at rungs 0-1; rung 2 says deterministic explicitly',
   'Rastegin: the cloning-discrimination equivalence is deterministic only',
   'none'),
 ('DNd','discrimination: optimal/beyond/perfect',
   'partial','same as DNc',
   '-','none'),
]
print('  CONFLATION AUDIT OF ALL NINE COORDINATES')
print()
for n,rungs,status,what,ev,act in AUDIT:
    print('  %-4s %-38s  %s' % (n, rungs, status))
    print('       merges : %s' % what)
    if ev!='-': print('       shown  : %s' % ev)
    print('       lattice: %s' % act)
    print()
c=sum(1 for a in AUDIT if a[2]=='CONFLATED')
p=sum(1 for a in AUDIT if a[2]=='partial')
print('  fully conflated: %d of 9    partially: %d    clean: %d' % (c,p,9-c-p))
print()
print('  THE MISSING RUNGS, COLLECTED')
miss=[('U','a ghost rung - indefinite metric, distinct from CPTP non-unitarity'),
      ('L','a kinematical rung - nonlinear state space, distinct from nonlinear evolution'),
      ('SD','separate observable- and field-commutativity rungs'),
      ('NEC','separate ANEC and achronal-ANEC conditions'),
      ('-','a derivative-order axis - Buniy\'s operative hypothesis')]
for a,b in miss: print('     %-4s %s' % (a,b))
print()
print('  PATTERN')
print('     every conflation merges a rung with NO lattice action')
print('     and a partner that WOULD act (or would abolish the lattice entirely)')
print('     each was invisible until a specific question forced it:')
print('        U   <- which spin-statistics hypothesis does U encode?')
print('        L   <- does nonlinearity destroy vector coupling?')
print('        SD  <- observables or fields?')
print('        NEC <- which exclusion theorems apply to a long wormhole?')
print('        X   <- is the ghost condensate inside Buniy\'s jurisdiction?')
print()
print('     none was found by inspecting the axis. All five were found by asking')
print('     what a specific theorem needs, and checking whether the rung supplies it.')