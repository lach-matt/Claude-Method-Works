eV=1.602176634e-19; Q=17.59e6*eV
LHD=4.25e28   # nuclei m^-3
print('  ARE THE TWO THRESHOLDS BOUNDS OR BRACKETS?')
print('     breakeven  E_mu < 3.90 GeV      : a LOWER bound on conversion efficiency')
print('     power      R_mu > 1.2e15 /s     : a LOWER bound on muon rate')
print('     both on the same axis, nested. NOT a bracket.')
print()
print('  BUT THE FLUX BOUND HAS A PARTNER: HEAT REMOVAL')
print('     %-16s %14s %14s %14s' % ('fuel volume','power density','vs PWR core','vs ITER'))
PWR=1.0e8; ITER=1.0e6
for V,lab in [(1e-3,'1 litre'),(1e-2,'10 litres'),(1e-1,'100 litres'),
              (1.0,'1 m^3'),(10.0,'10 m^3'),(100.0,'100 m^3')]:
    pd=1e6/V
    print('     %-16s %11.3g W/m^3 %13.3g %13.3g' % (lab,pd,pd/PWR,pd/ITER))
print()
print('  WHAT A CRYOGENIC TARGET CAN ACTUALLY TAKE')
print('     liquid hydrogen at 20 K. removing heat requires a refrigerator with')
print('     Carnot penalty T_amb/T_cold = 300/20 = 15x MINIMUM on the work.')
print('     so P_removed W of fusion heat costs >= 15 x P_removed W of compressor work,')
print('     before any real-cycle inefficiency (typical cryoplant: 3-5x Carnot).')
print()
for P,lab in [(1e6,'1 MW fusion')]:
    for eta,elab in [(15,'Carnot floor'),(50,'good cryoplant'),(75,'typical')]:
        print('     %-12s cooling work at %-16s %.3g W  =  %.0f%% of fusion output'
              % (lab,elab,P*eta/1.0,100*eta))
print()
print('     -> at 20 K, removing the heat costs 15-75x the heat removed.')
print('        a cryogenic muCF reactor CANNOT be net-positive while cold.')
print()
print('  THE BRACKET, PROPERLY STATED')
print('     it is not on flux. it is on TARGET TEMPERATURE, and it is already tight:')
print('     LOWER : lambda_dtmu rises resonantly to 800 K - the paper says run HOT')
print('     UPPER : hydrogen must stay dense. at 800 K, D/T is a gas.')
print()
print('     %-10s %-10s %-16s %s' % ('T (K)','phase','density','note'))
ROWS=[('13','solid','~1.3 LHD','formation slow, resonance mismatch'),
      ('20','liquid','1.0 LHD','PSI operating point; cryogenic penalty 15-75x'),
      ('33','critical','~0.3 LHD','critical point of hydrogen'),
      ('300','gas','needs ~1000 bar for 1 LHD','no cryogenic penalty'),
      ('800','gas','needs ~2700 bar for 1 LHD','lambda_dtmu maximum')]
for r in ROWS: print('     %-10s %-10s %-16s %s' % r)
print()
print('  THE REAL BRACKET IS TEMPERATURE x PRESSURE')
print('     the resonance wants 800 K. density wants cold or enormous pressure.')
print('     the JINR scan (0.2-1.2 LHD at 20-800 K) is exactly this bracket being explored.')
print('     at 800 K and 1 LHD the required pressure is of order kilobars.')
print()
print('  SO: BOUNDS OR BRACKETS?')
print('     energy gap : a BOUND. E_mu < 3.90 GeV. one-sided, nothing fails from being better.')
print('     flux gap   : a BOUND. R_mu > 1.2e15 /s. one-sided.')
print('     temperature: a BRACKET. resonance from below, density from above.')
print('     binder mass: a BRACKET. [119, 918] me. the one already in the paper.')
print()
print('     the paper has one bracket (mass) and treats the rest as bounds.')
print('     the temperature-density bracket is present in the data (JINR scan)')
print('     but is not stated as a structural window.')