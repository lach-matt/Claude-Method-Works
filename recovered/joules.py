import math
eV=1.602176634e-19
Q_fus=17.59e6*eV
E5=5.0e9*eV; E03=0.30e9*eV
print('  THE QUANTA, IN JOULES')
print('     one d+t fusion            %.4g J   (17.59 MeV)' % Q_fus)
print('     one muon at 5 GeV         %.4g J' % E5)
print('     one muon at 0.30 GeV floor %.4g J' % E03)
print('     ratio cost/return, 1 cycle %.4g' % (E5/Q_fus))
print('     -> breakeven needs         %.0f fusions per muon' % (E5/Q_fus))
print()
print('  ENERGY DENSITY OF THE VESSEL')
R=280e-15; V=(4/3)*math.pi*R**3
u=Q_fus/V
print('     17.59 MeV released in     %.3g m^3' % V)
print('     energy density            %.3g J/m^3' % u)
for n,d in [('TNT',4.6e9),('gasoline',3.4e10),('solar core (thermal 3/2 nkT)',3.0e16),
            ('nuclear matter',1e35)]:
    print('        vs %-28s x %.3g' % (n,u/d))
print()
print('  PER-MUON LEDGER  (Q = N x 17.59 MeV / E_mu)')
print('     %-34s %8s %10s %10s' % ('case','cycles N','return (J)','Q'))
CASES=[('measured, Los Alamos',150,E5),
       ('sticking ceiling 1/0.0045 = 222',222,E5),
       ('scientific breakeven',284,E5),
       ('dual polarisation 1/0.0034',294,E5),
       ('polarisation + J=1 mix 1/0.00234',427,E5)]
for lab,N,E in CASES:
    ret=N*Q_fus
    print('     %-34s %8d %10.4g %10.3f' % (lab,N,ret,ret/E))
print()
print('  THE SAME CASES AT THE KINEMATIC FLOOR (0.30 GeV)')
for lab,N,_ in CASES:
    ret=N*Q_fus
    print('     %-34s %8d %10.4g %10.2f' % (lab,N,ret,ret/E03))
print()
print('  WHICH GAP IS BIGGER, IN JOULES')
N_now=222
deficit_sticking = (284-N_now)*Q_fus
deficit_accel    = E5-E03
print('     shortfall from sticking ceiling (222 -> 284) : %.4g J per muon' % deficit_sticking)
print('     shortfall from accelerator (5 GeV -> 0.30)   : %.4g J per muon' % deficit_accel)
print('     ratio accelerator / sticking                  : %.1fx' % (deficit_accel/deficit_sticking))
print()
print('  FUEL SIDE, FOR SCALE')
LHD=4.25e22*1e6      # m^-3
n_dt=LHD
E_per_m3 = n_dt/2*Q_fus
print('     liquid hydrogen density   %.3g nuclei/m^3' % LHD)
print('     if every d,t pair fused   %.4g J/m^3   (%.3g kWh per litre)' % (E_per_m3, E_per_m3*1e-3/3.6e6))
print('     petrol, for comparison    3.4e10 J/m^3   (9.4 kWh per litre)')
print('     ratio                     %.3g x' % (E_per_m3/3.4e10))
print()
print('  MUON COST AS A FRACTION OF FUEL VALUE')
print('     one muon (5 GeV) costs    %.4g J' % E5)
print('     it burns N x 1 pair; at N=300 that is 300 pairs')
print('     fuel energy released      %.4g J' % (300*Q_fus))
print('     so the binder costs       %.1f%% of what it liberates' % (100*E5/(300*Q_fus)))