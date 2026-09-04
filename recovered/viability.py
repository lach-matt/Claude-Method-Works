eV=1.602176634e-19
Q=17.59e6*eV
tau_mu=2.197e-6; lam0=4.665e5
lam_c=2.6e8
print('  THE VIABILITY CONDITION FOR A CONSUMABLE BINDER')
print('     viable  <=>  N_service > E_binder / Q_event')
print()
print('  THE TWO CEILINGS ON N')
for ws,lab in [(0.0045,'measured SIN'),(0.0056,'measured PSI'),(0.0034,'dual polarisation'),
               (0.00234,'polarisation + J=1 mix')]:
    n_stick=1/ws
    for phi in (1.2,2.0,3.0):
        n_life=phi*lam_c*tau_mu
        binding='sticking' if n_stick<n_life else 'LIFETIME'
        if phi==1.2:
            print('     ws=%.3f%% (%-22s) sticking ceiling %6.0f   lifetime ceiling(phi=1.2) %6.0f  -> %s'
                  % (100*ws,lab,n_stick,n_life,binding))
print()
print('  N REQUIRED, BY ACCELERATOR EFFICIENCY')
print('     %-26s %10s %10s %10s' % ('E_mu','N required','N avail(222)','viable?'))
for E,lab in [(0.30,'kinematic floor'),(1.0,'3.3x floor'),(2.0,'6.7x floor'),
              (3.0,'10x floor'),(3.9,'CROSSOVER'),(5.0,'achieved today')]:
    Nreq=E*1e9*eV/Q
    print('     %-26s %10.0f %10d %10s' % ('%.2f GeV (%s)'%(E,lab), Nreq, 222,
          'YES' if 222>Nreq else 'no'))
print()
Ecross=222*17.59e6/1e9
print('  CROSSOVER: E_mu = N_max x Q = 222 x 17.59 MeV = %.2f GeV' % Ecross)
print('     today 5.00 GeV -> need a %.0f%% reduction, i.e. efficiency 16.7x -> %.1fx' % (100*(1-Ecross/5.0), 5.0/0.30*(Ecross/5.0)))
print('     that is a %.2fx accelerator improvement, against a 16.7x theoretical headroom.' % (5.0/Ecross))
print()
print('  MARGIN AT THE FLOOR')
Nreq_floor=0.30e9*eV/Q
print('     required %.1f, available %d  ->  margin %.1fx' % (Nreq_floor,222,222/Nreq_floor))
print('     the consumable-binder regime is VIABLE with room to spare.')
print('     what is not viable is the present binder factory.')
print()
print('  THE SAME CONDITION, AS A DESIGN RULE')
print('     N_service  >  E_binder / Q_event')
print('     muCF today : 222 vs 284   FAILS by 1.28x')
print('     muCF floor : 222 vs  17   PASSES by 13.0x')
print()
print('  WHAT SETS N_SERVICE, AND WHICH CEILING BINDS')
print('     %-28s %8s %8s %8s' % ('configuration','sticking','lifetime','binds'))
for ws,lab in [(0.0056,'PSI measured'),(0.0045,'SIN measured'),(0.0034,'dual polarisation'),
               (0.00234,'polarisation + J=1')]:
    for phi in (1.2,3.0):
        ns=1/ws; nl=phi*lam_c*tau_mu
        print('     %-28s %8.0f %8.0f %8s' % ('%s, phi=%.1f'%(lab,phi), ns, nl,
              'sticking' if ns<nl else 'lifetime'))
print()
print('     sticking binds in every configuration at phi=1.2;')
print('     at phi=3.0 the lifetime ceiling rises to %.0f and sticking still binds.' % (3.0*lam_c*tau_mu))
print('     -> N_service is a STICKING quantity, and E_binder is an ACCELERATOR quantity.')
print('        the two gaps of the paper are exactly the two sides of this one inequality.')