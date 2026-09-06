eV=1.602176634e-19
Q_fus=17.59e6*eV; E_floor=0.30e9*eV; E_now=5.0e9*eV
print('  CAN A FUSION EVENT PAY FOR ITS OWN BINDER?')
print('     energy released per fusion      %8.2f MeV' % 17.59)
print('     kinematic floor for one muon    %8.2f MeV' % 300)
print('     achieved cost per muon          %8.0f MeV' % 5000)
print('     events needed to fund one muon  %8.1f  (at the floor)' % (300/17.59))
print('     events needed at 5 GeV          %8.1f' % (5000/17.59))
print()
print('     => k_binder = 0. The reaction produces no muons.')
print('        chain multiplication is not merely unachieved, it is excluded by a factor of 17.')
print()
print('  THE BINDER LEDGER ACROSS TECHNOLOGIES')
print('  %-24s %-16s %-10s %-22s %s' % ('process','binder','k_binder','binder cost / yield','regime'))
ROWS=[('fission chain','neutron','2.4','~0 after initiation','SELF-SUPPLYING'),
      ('thermal / inertial fusion','none (kinetic)','n/a','0 - no binder','NO BINDER'),
      ('chemical combustion','none','n/a','0','NO BINDER'),
      ('muon-catalysed fusion','muon','0','1/Q, currently 1.90','EXTERNALLY SUPPLIED, CONSUMED'),
      ('traversable wormhole','Casimir geometry','n/a','0 - not consumed','NOT CONSUMED')]
for r in ROWS: print('  %-24s %-16s %-10s %-22s %s' % r)
print()
print('  muCF BINDER COST AS A FUNCTION OF N AND E_mu')
print('     BC = E_mu / (N x Q_fus) = 1/Q_gain')
print('     %-8s %12s %12s' % ('N','BC at 5 GeV','BC at floor'))
for N in (150,222,284,300,427,1000):
    print('     %-8d %11.1f%% %11.2f%%' % (N, 100*E_now/(N*Q_fus), 100*E_floor/(N*Q_fus)))
print()
print('  THE THREE REGIMES, STATED STRUCTURALLY')
print('     k_binder > 1   : the process multiplies its binder. Chain. BC -> 0.')
print('                      fission. the binder is a PRODUCT.')
print('     k_binder = 0,')
print('     binder reused  : the process recycles one binder N times. BC = E_b/(N Q).')
print('                      muCF. the binder is a CONSUMABLE with a service life.')
print('     no binder      : approach supplied kinetically or the binder is not spent.')
print('                      thermal fusion; a wormhole. BC = 0 by construction.')
print()
print('  WHAT WOULD MOVE muCF BETWEEN REGIMES')
print('     to k_binder > 1 : one fusion would have to yield a muon.')
print('                       needs Q_fus > 300 MeV. d+t gives 17.59. EXCLUDED by 17x.')
print('                       no light-nucleus channel reaches 300 MeV:')
for lab,q in [('d+t -> 4He+n',17.59),('d+d -> 3He+n',3.269),('d+d -> 4He+gamma',23.847),
              ('p+11B -> 3 alpha',8.7),('3He+3He',12.86),('fission of U-235',200.0)]:
    print('                          %-22s %7.2f MeV   %s' % (lab,q,'sufficient' if q>300 else 'short by %.0fx'%(300/q)))
print()
print('     -> even URANIUM FISSION at 200 MeV falls short of the 300 MeV muon floor.')
print('        no nuclear process known produces enough per event to fund a muon.')
print('        muCF cannot be made self-sustaining by any choice of fuel.')