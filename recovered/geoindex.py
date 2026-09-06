import math
print('  THE TWO WINDOWS, SIDE BY SIDE')
rows=[
 ('subject',            'muon-catalysed fusion',        'traversable wormhole'),
 ('vessel',             'the muonic molecule',          'the throat'),
 ('characteristic size','280 fm (dtmu)',                'throat radius b0'),
 ('what supplies approach','molecular binding geometry','Casimir geometry (MMP: flux + near-extremal pair)'),
 ('binder',             'mu- (207 me)',                 'negative Casimir energy of charged fermions'),
 ('LOWER bound (rate)',  'fusion must outrun the cycle -> m > 119 me',
                         'throat must flare fast enough to traverse (Fewster-Roman: Kuhfittig model non-traversable)'),
 ('UPPER bound (degeneracy)','N_states = sqrt(M/m) >= 2 -> m < 918 me',
                         'QI forces submicroscopic OR large throat/curvature discrepancy'),
 ('occupants in window','exactly 1 (mu; pion filtered by absorption)',
                        'MMP at sub-electroweak; macroscopic branch EMPTY'),
 ('what is cheap',      'fuel: 1.66e7 kWh/litre',       'exotic mass: arbitrarily small (VKD)'),
 ('what is expensive',  'the binder: 94.8% of return',  'the geometry: submicroscopic or pathological'),
]
for a,b,c in rows:
    print('     %-24s' % a)
    print('        muCF     : %s' % b)
    print('        wormhole : %s' % c)
print()
print('  THE SHARED STRUCTURE')
print('     both windows are bounded BELOW by a RATE ratio')
print('        does the process outrun the vessel lifetime?')
print('     and ABOVE by an INDEX DEGENERACY')
print('        does the state count survive?')
print('     joules appears in neither bound.')
print()
print('  WHY JOULES IS THE WRONG FIRST COORDINATE')
Q=17.59e6*1.602e-19; V=(4/3)*math.pi*(280e-15)**3
print('     muCF vessel energy density  %.3g J/m^3' % (Q/V))
print('     -> extreme, and it constrains NOTHING: the bounds are m > 119 and m < 918,')
print('        neither of which mentions energy.')
print('     wormhole: total exotic mass arbitrarily small (VKD) and it constrains NOTHING:')
print('        the binding constraint is throat size vs curvature radius.')
print()
print('  CANDIDATE COORDINATES FOR THE SECOND INDEX')
COORDS=[('SCALE',      'characteristic size of the vessel, in units of the process length',
                       'muCF: R/r_nuclear ~ 280fm/5fm = 56 ; wormhole: b0/l_Planck'),
        ('RATE',       'process rate / vessel lifetime',
                       'muCF: lambda_fus/lambda_cycle = 1e12/2.6e8 = 3800 ; wormhole: flaring vs affine transit'),
        ('STATES',     'number of bound states of the confining index',
                       'muCF: sqrt(M/m) ; wormhole: -'),
        ('DUTY',       'fraction of time the vessel exists',
                       'muCF: 1ps/3.8ns = 2.6e-4 ; wormhole: static, duty = 1'),
        ('OCCUPANCY',  'vessels per unit volume achievable',
                       'muCF: set by muon flux ; wormhole: set by nothing known'),
        ('BINDER COST','binder energy / liberated energy',
                       'muCF: 94.8% ; wormhole: 0 (geometry is not consumed)')]
print('     %-12s %s' % ('coordinate','meaning'))
for a,b,c in COORDS:
    print('     %-12s %s' % (a,b))
    print('     %-12s   %s' % ('',c))
print()
print('  THE ONE COORDINATE THAT SEPARATES THEM')
print('     BINDER COST. muCF consumes its binder (94.8% of return).')
print('     a wormhole does not: geometry, once made, is not spent.')
print('     that is why muCF has a flux gap and a wormhole has none -')
print('     and why the wormhole problem is entirely about whether the cell exists,')
print('     while muCF is entirely about how many cells per second.')