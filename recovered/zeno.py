import math
STAGES=['A1 proton driver','A2 production target (pi- yield)','A3 capture solid angle',
        'A4 decay channel acceptance','A5 transport','A6 stopping fraction']
n=len(STAGES)
TOT=16.7            # achieved / kinematic floor
print('  THE COMPOUND FACTOR, SEGMENTED')
print('     total inefficiency  E_mu(achieved)/E_mu(floor) = %.1fx across %d stages' % (TOT,n))
eff_each=TOT**(1/n)
print('     if evenly distributed, each stage loses a factor %.3fx  (efficiency %.1f%%)'
      % (eff_each, 100/eff_each))
print()
print('  WHAT EACH GAP REQUIRES, PER STAGE')
print('     %-34s %10s %12s %12s' % ('target','total factor','per stage','per stage %'))
GOALS=[('scientific breakeven (5.00->3.90 GeV)',5.00/3.90),
       ('Q = 2 (5.00->1.95 GeV)',5.00/1.95),
       ('Q = 5 (5.00->0.78 GeV)',5.00/0.78),
       ('kinematic floor (5.00->0.30 GeV)',16.7),
       ('flux gap 1 MW (1e10 -> 1.2e15 /s)',1.2e5)]
for lab,f in GOALS:
    ps=f**(1/n)
    print('     %-34s %10.3g %12.4f %11.1f%%' % (lab,f,ps,100*(ps-1)))
print()
print('  THE CROSSOVER, IN PLAIN TERMS')
f=5.00/3.90; ps=f**(1/n)
print('     breakeven needs %.3fx total = %.1f%% improvement at EACH of %d stages' % (f,100*(ps-1),n))
print('     for comparison, A3 (capture) is called "the largest single loss" in the source.')
print('     a single stage improving %.2fx alone would suffice.' % f)
print()
print('  WHY THE FLUX GAP DOES NOT SEGMENT')
print('     efficiency gap : E_mu is INTENSIVE. every stage multiplies. segmentation works.')
print('     flux gap       : muons/s is EXTENSIVE. it scales with BEAM POWER, not efficiency.')
print()
P_beam_now=1.4e6   # W, ~1.4 MW class proton driver (PSI HIPA)
R_now=1e10
print('     present class driver     ~%.1f MW  ->  ~%.0e mu/s' % (P_beam_now/1e6,R_now))
print('     1 MW fusion needs         %.1e mu/s' % 1.2e15)
print('     at fixed efficiency that is  %.0e MW of proton beam' % (P_beam_now*1.2e15/R_now/1e6))
print('     at the kinematic floor (16.7x better) still %.0f MW' % (P_beam_now*1.2e15/R_now/1e6/16.7))
print()
print('     -> even a PERFECT accelerator needs %.0f MW of driver for 1 MW of fusion.' % (P_beam_now*1.2e15/R_now/1e6/16.7))
print('        segmentation cannot touch this: it is a power ratio, not an efficiency chain.')
print()
print('  THE HONEST SPLIT')
print('     energy gap : 1.28x. segments to %.1f%% per stage. ONE stage could do it.' % (100*((5.00/3.90)**(1/n)-1)))
print('     flux gap   : extensive. no segmentation. needs a different machine class,')
print('                  and at perfect efficiency still %.0e MW of driver per MW of fusion.'
      % (P_beam_now*1.2e15/R_now/1e6/16.7))
print()
print('  WHERE THE FLUX GAP ACTUALLY CLOSES')
print('     R_mu = P_beam / E_mu. so muons/s rises by:')
print('        raising P_beam (extensive, capital, cooling-limited)')
print('        lowering E_mu  (intensive, the same 16.7x headroom)')
print('     the SAME 16.7x that buys Q also buys 16.7x of flux.')
print('     it is one lever appearing in both gaps, worth 16.7x in each.')
print('     after spending it: Q = 16.6 and the flux gap is 1e5/16.7 = %.0f x remaining.' % (1.2e5/16.7))