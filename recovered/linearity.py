from itertools import product
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
print('  WHAT EACH LAMBDA CONSTRAINT PRESUPPOSES')
rows=[
 ('l <= n-1',      'node counting in the radial equation',
                   'state space: Sturm-Liouville on a linear ODE'),
 ('k <= 4l+2',     'Pauli exclusion',
                   'state space: antisymmetrisation of a tensor product'),
 ('q <= k',        'counting',                    'none'),
 ('g <= min(4f+2,q)','Pauli and counting on the target','state space: same as above'),
 ('2S <= k',       'vector coupling of spins',    'state space: SU(2) rep theory'),
 ('2S\' <= g',      'target multiplicity',         'state space: SU(2) rep theory'),
 ('v seniority',   'Racah seniority',             'state space: SU(2) rep theory'),
 ('2J_c, 2K, 2J',  'angular momentum addition',   'state space: Clebsch-Gordan'),
]
for a,b,c in rows: print('     %-18s %-38s %s' % (a,b,c))
print()
print('     NOT ONE of them invokes the evolution law.')
print()
print('  TWO KINDS OF NONLINEARITY')
print('     dynamical (Weinberg 1989): H(psi) nonlinear, homogeneous degree 1;')
print('        Hilbert space unchanged, rays superpose, tensor products decompose')
print('        -> every Lambda constraint survives -> NO LATTICE ACTION')
print('     kinematical (nonlinear state space): superposition itself fails')
print('        -> tensor products, antisymmetrisation and Clebsch-Gordan all lose meaning')
print('        -> Lambda is not merely modified, it is undefined')
print()
print('     the index grades L from Abrams-Lloyd and Polchinski, both Weinberg-type')
print('     => L = 1 as graded is DYNAMICAL => no lattice action')
print()
print('  THE TWO CONFLATED AXES')
print('     %-6s %-34s %-34s' % ('axis','rung as graded','the distinct thing it merges'))
print('     %-6s %-34s %-34s' % ('U','Lindblad, CPTP, metric intact','ghosts, indefinite metric'))
print('     %-6s %-34s %-34s' % ('L','dynamical (Weinberg)','kinematical (state space nonlinear)'))
print()
print('     in both cases the graded rung has NO lattice action')
print('     and the unmerged partner WOULD have one')
print('     both were invisible until a lattice question forced the distinction')
print()
print('  FINAL CLASSIFICATION OF THE NINE')
final=[('X',  'LATTICE', 'spin-statistics hypothesis (Lorentz invariance); also the l-bound'),
       ('Sc', 'LATTICE', 'Sc>=3 breaks the spin-statistics conclusion directly'),
       ('SD', 'LATTICE', 'spin-statistics hypothesis (spacelike commutativity)'),
       ('NEC','measure', 'shifts energies; no quantum number moves'),
       ('U',  'none',    'Lindblad is CPTP; the metric hypothesis is about ghosts, not this rung'),
       ('L',  'none',    'Weinberg nonlinearity leaves the state space linear'),
       ('IC', 'none',    'correlations between separated systems, not bound states'),
       ('DNc','none',    'state manipulation, not structure'),
       ('DNd','none',    'state manipulation, not structure')]
for a,b,c in final: print('     %-5s %-8s %s' % (a,b,c))
print()
print('     lattice action: 3 of 9    measure only: 1    none: 5')
print('     all three lattice-acting coordinates act through ONE theorem: spin-statistics')