import math
T_amb=300.0
print('  THE OUTPUT SIDE, ACROSS THE TEMPERATURE BRACKET')
print('  %-8s %-10s %-14s %-16s %s' % ('T (K)','phase','heat removal','work recoverable','net factor on output'))
ROWS=[(13,'solid'),(20,'liquid'),(33,'critical'),(100,'gas'),(300,'gas'),(500,'gas'),(800,'gas')]
for T,phase in ROWS:
    if T < T_amb:
        carnot_pen = T_amb/T                 # minimum work to pump heat out
        real_pen   = carnot_pen*3.5          # typical cryoplant 3-5x Carnot
        work=0.0
        net = -real_pen
        rem='costs %.0fx' % real_pen
        wr='none (below ambient)'
    else:
        eta = 1 - T_amb/T if T>T_amb else 0.0
        work=eta
        net = eta
        rem='free (rejects to ambient)'
        wr='%.0f%% Carnot' % (100*eta)
    print('  %-8d %-10s %-14s %-16s %+.2f' % (T,phase,rem,wr,net))
print()
print('  THE SWING')
pen20 = (T_amb/20)*3.5
eta800 = 1-T_amb/800
print('     at  20 K : net -%.0f  (must spend %.0f W per W of fusion heat)' % (pen20,pen20))
print('     at 800 K : net +%.2f (recover %.0f%% of fusion heat as work)' % (eta800,100*eta800))
print('     swing    : %.0f in the numerator, and the sign changes.' % (pen20+eta800))
print()
print('  COMPARED TO THE STATED GAPS')
print('     energy gap (accelerator)   1.28x')
print('     flux gap                   1.2e5x  (a rate, not a power)')
print('     temperature (20K -> 800K)  %.0fx and a sign change' % ((pen20+eta800)/eta800))
print()
print('  WHY THE TWO PRESSURES PUSH THE SAME WAY')
print('     resonance    : lambda_dtmu rises ~2 orders from low T to 800 K  -> HOT')
print('     thermodynamics: output worthless below ambient, 62% Carnot at 800 K -> HOT')
print('     density      : 1 LHD is free at 20 K, needs ~2700 bar at 800 K -> COLD')
print('     -> two of three want hot. only density objects, and density is purchasable')
print('        with pressure, which is CAPITAL, not a continuous power draw.')
print()
print('  REFRIGERATION vs COMPRESSION: THE STRUCTURAL DIFFERENCE')
print('     refrigeration : continuous, proportional to the heat load,')
print('                     so it scales with the very output you are trying to sell.')
print('     compression   : largely one-time. the fuel is held, not consumed;')
print('                     circulation for ash removal is a small pumping loss.')
print('     -> a cost that scales with output can never be outrun by more output.')
print('        a cost that does not scale can.')
print()
print('  THE NET-GAIN EXPRESSION, CORRECTED FOR TEMPERATURE')
eV=1.602176634e-19; Q=17.59e6*eV
E5=5.0e9*eV; E39=3.90e9*eV; E03=0.30e9*eV
print('     Q_net = (N x Q_fus x eta_T - W_cool) / E_mu')
print('     %-22s %8s %10s %10s' % ('case','N','Q (naive)','Q_net'))
for lab,N,E,T in [('20 K, 5 GeV, N=222',222,E5,20),
                  ('20 K, 3.9 GeV, N=222',222,E39,20),
                  ('800 K, 5 GeV, N=222',222,E5,800),
                  ('800 K, 3.9 GeV, N=222',222,E39,800),
                  ('800 K, 0.3 GeV, N=222',222,E03,800),
                  ('800 K, 0.3 GeV, N=427',427,E03,800)]:
    gross=N*Q
    if T<T_amb:
        net = gross*(-(T_amb/T)*3.5)
    else:
        net = gross*(1-T_amb/T)
    print('     %-22s %8d %10.2f %10.2f' % (lab,N,gross/E,net/E))