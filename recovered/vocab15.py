LETTERS={'X_exp','X_spon','Sc','IC','U_open','U_ghost','NEC_pt','NEC_ach',
         'L_dyn','L_kin','SD_obs','SD_field','DNc','DNd','EOM'}
VOC={'V1 laws':LETTERS,
     'V2 theory':{'causal','field content','interacting','d > 2'},
     'V3 geometry':{'flat spacetime','asymptotically flat','simply connected','globally hyperbolic','generic'},
     'V4 algebra':{'determinism','ultralocality','stability','vacuum lowest energy','vacuum not annihilated'},
     'V5 coupling':{'minimal coupling'},
     'V6 solution':{'self-consistent semiclassical'},
     'V7 degeneracy':{'non-degenerate higher-derivative'}}
WHERE={h:v for v,hs in VOC.items() for h in hs}
CH_OLD={'Buniy':['causal','X_exp','2nd-order EOM','field content'],
        'Hartman':['unitary','X_exp','interacting','d > 2','flat spacetime'],
        'Wall':['determinism','ultralocality','X_exp','stability','minimal coupling'],
        'GrahamOlum':['asymptotically flat','simply connected','generic','globally hyperbolic','self-consistent semiclassical'],
        'spin-statistics':['X_exp','microcausality','vacuum lowest energy','positive metric','vacuum not annihilated'],
        'Ostrogradsky':['non-degenerate higher-derivative']}
CH_NEW={'Buniy':['causal','X_exp','EOM','field content'],
        'Hartman':['U_ghost','X_exp','interacting','d > 2','flat spacetime'],
        'Wall':['determinism','ultralocality','X_exp','stability','minimal coupling'],
        'GrahamOlum':['asymptotically flat','simply connected','generic','globally hyperbolic','self-consistent semiclassical'],
        'spin-statistics':['X_exp','SD_obs','vacuum lowest energy','U_ghost','vacuum not annihilated'],
        'Ostrogradsky':['EOM','non-degenerate higher-derivative']}
def analyse(lab,CH,letters):
    print('  %s' % lab)
    tot=0; idx=0
    print('     %-18s %-5s %-5s  span  outside the alphabet' % ('charger','hyps','in V1'))
    for ch,hs in CH.items():
        ins=[h for h in hs if h in letters]
        out=[h for h in hs if h not in letters]
        vocs={WHERE.get(h,'V1 laws') if h in letters else WHERE.get(h,'?') for h in hs}
        tot+=len(hs); idx+=len(ins)
        print('     %-18s %-5d %-5d  %4d  %s' % (ch,len(hs),len(ins),len(vocs),'; '.join(out) or '-'))
    print('     TOTAL hypotheses %d, indexable %d (%.0f%%)' % (tot,idx,100*idx/tot))
    return tot,idx
print()
t1,i1=analyse('NINE-LETTER ALPHABET',CH_OLD,{'X_exp'} | {'Sc','IC','DNc','DNd','NEC_pt'})
print()
t2,i2=analyse('FIFTEEN-LETTER ALPHABET',CH_NEW,LETTERS)
print()
print('  IMPROVEMENT: %d -> %d indexable hypotheses (%.0f%% -> %.0f%%)' % (i1,i2,100*i1/t1,100*i2/t2))
print()
print('  IS ANY CHARGER NOW EXPRESSIBLE IN ONE VOCABULARY?')
for ch,hs in CH_NEW.items():
    vocs={('V1 laws' if h in LETTERS else WHERE.get(h,'?')) for h in hs}
    tag='YES' if len(vocs)==1 else 'no  (spans %d)'%len(vocs)
    print('     %-18s %s   %s' % (ch,tag,', '.join(sorted(vocs))))
print()
print('  A SEVENTH VOCABULARY APPEARED')
print('     V7 degeneracy: {non-degenerate higher-derivative}')
print('     required by Ostrogradsky, which the alphabet now triggers via EOM -> U_ghost.')
print('     the edge is in the index; its jurisdiction is not.')
print()
print('  WHAT REMAINS OUTSIDE, BY VOCABULARY')
from collections import Counter
out=Counter()
for ch,hs in CH_NEW.items():
    for h in hs:
        if h not in LETTERS: out[WHERE.get(h,'?')]+=1
for v,n in sorted(out.items()): print('     %-16s %d hypotheses' % (v,n))