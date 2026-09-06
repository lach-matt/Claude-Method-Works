T_amb=300.0
f_alpha=3.5/17.59; f_n=14.1/17.59
print('  ENERGY SPLIT PER FUSION')
print('     alpha  3.5 MeV  = %.1f%%  stays in the fuel (range ~microns)' % (100*f_alpha))
print('     neutron 14.1 MeV = %.1f%%  escapes to a blanket at any temperature' % (100*f_n))
print()
def pen(T): return (T_amb/T)*3.5 if T<T_amb else 0.0
def eta(T): return 1-T_amb/T if T>T_amb else 0.0
print('  NET RECOVERY FACTOR = f_n x eta(T_blanket) - f_alpha x pen(T_fuel)')
print('  %-22s %-16s %10s %10s %8s' % ('fuel T','blanket T','recovered','cooling','net'))
CASES=[(20,800),(20,300),(33,800),(100,800),(300,800),(500,800),(800,800),(300,1000),(800,1000)]
for Tf,Tb in CASES:
    rec=f_n*eta(Tb); cool=f_alpha*pen(Tf); net=rec-cool
    print('  %-22s %-16s %10.3f %10.3f %+8.3f' % ('%d K'%Tf,'%d K'%Tb,rec,cool,net))
print()
print('  CORRECTION TO MY PREVIOUS FIGURE')
print('     I said 20 K costs 52x the output. That assumed ALL 17.59 MeV stayed cold.')
print('     Only 19.9%% does. The true penalty at 20 K is %.1fx the total fusion energy.' % (f_alpha*pen(20)))
print('     Still fatal, but 5x less so, and the swing across the bracket is:')
best=f_n*eta(800); worst=f_n*eta(800)-f_alpha*pen(20)
print('        20 K fuel / 800 K blanket : %+.3f' % worst)
print('       800 K fuel / 800 K blanket : %+.3f' % best)
print('        difference                : %.3f  (not 85x - the neutron already escapes)' % (best-worst))
print()
print('  WHERE THE FUEL TEMPERATURE STOPS MATTERING')
for Tf in (20,33,50,100,200,300):
    c=f_alpha*pen(Tf)
    print('     fuel at %3d K : cooling costs %.3f of fusion output   %s'
          % (Tf,c,'FATAL' if c>f_n*eta(800) else 'tolerable'))
print()
print('  THE CORRECTED BREAKEVEN THRESHOLD')
eV=1.602176634e-19; Q=17.59e6*eV
for lab,Tf,Tb in [('cryogenic fuel, hot blanket',20,800),
                  ('ambient fuel, hot blanket',300,800),
                  ('hot fuel, hot blanket',800,800)]:
    net=f_n*eta(Tb)-f_alpha*pen(Tf)
    if net<=0:
        print('     %-30s net factor %+.3f  -> NO E_mu works' % (lab,net))
    else:
        Ecross=222*Q*net/eV/1e9
        print('     %-30s net factor %+.3f  -> work-breakeven at E_mu < %.2f GeV' % (lab,net,Ecross))
print()
print('     (heat-breakeven, which the paper uses, is E_mu < 3.90 GeV.')
print('      WORK-breakeven is the operative figure for a power plant.)')