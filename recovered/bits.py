from collections import Counter
from itertools import product
V=['T','M','A','S']
# status of each term in each vocabulary: 1 physical, 0 gauge/absent, None not applicable
T={
 'X_exp   explicit Lorentz violation'    :(1,0,0,0),
 'X_spon  a VEV picks a frame'           :(0,0,0,1),
 'EOM     derivative order'              :(1,0,0,0),
 'xi      curvature coupling'            :(1,0,0,0),
 'CPT'                                   :(1,0,0,0),
 'FLAT    curvature'                     :(0,1,0,0),
 'CONN    connectedness'                 :(0,1,0,0),
 'HYP     global hyperbolicity'          :(0,1,0,0),
 'U_ghost indefinite metric'             :(0,0,1,0),
 'U_open  CPTP non-unitarity'            :(0,0,1,0),
 'SD_obs  observable commutativity'      :(0,0,1,0),
 'IC      information causality'         :(0,0,1,0),
 'NEC_pt  <T_kk> in this state'          :(0,0,0,1),
 'Sc      CHSH value realised'           :(0,0,0,1),
 'Hadamard'                              :(0,0,0,1),
 'supertranslation (whole horizon)'      :(0,0,0,0),
 'supertranslation (subregion)'          :(0,0,1,0),
}
print('  STATUS VECTORS OVER T / M / A / S')
print('  %-38s %s' % ('term',' '.join(V)))
for k,v in T.items(): print('  %-38s %s' % (k,'  '.join(str(x) for x in v)))
print()
c=Counter(T.values())
print('  distinct patterns used : %d of %d available' % (len(c),2**4))
print('  patterns:')
for p,n in sorted(c.items(), key=lambda kv:-kv[1]):
    print('     %-14s x%-2d  %s' % (str(p),n,
      'single-vocabulary' if sum(p)==1 else ('ABSENT everywhere' if sum(p)==0 else 'MIXED')))
print()
single=[k for k,v in T.items() if sum(v)==1]
mixed =[k for k,v in T.items() if sum(v)>1]
zero  =[k for k,v in T.items() if sum(v)==0]
print('  single-vocabulary terms : %d' % len(single))
print('  mixed (physical in >1)  : %d  %s' % (len(mixed),mixed))
print('  physical nowhere        : %d  %s' % (len(zero),zero))
print()
print('  THE FINDING')
print('     every term is physical in EXACTLY ONE vocabulary, or in none.')
print('     the status vector is a ONE-HOT code, not an arbitrary 4-bit word.')
print('     %d of 16 patterns occur, and all of them have weight 0 or 1.' % len(c))
print()
print('  WHICH IS WHAT THE BFV PARTITION MEANS')
print('     a term predicates on exactly one of: the functor, the source objects,')
print('     the target objects, or a functional on the target.')
print('     one-hot IS the partition. the bits are not free.')
print()
print('  AND THE REVERSAL IS A ONE-BIT MOVE')
a=T['supertranslation (whole horizon)']; b=T['supertranslation (subregion)']
d=[i for i in range(4) if a[i]!=b[i]]
print('     whole horizon : %s   weight %d - physical nowhere' % (str(a),sum(a)))
print('     subregion     : %s   weight %d - physical in %s' % (str(b),sum(b),V[b.index(1)]))
print('     Hamming distance: %d  (bit %s)' % (len(d),[V[i] for i in d]))
print()
print('     the translator supplies ONE BIT: it moves a term from weight 0 to weight 1.')
print('     that is what gravitational dressing does - it makes an operator that was')
print('     an element of nothing into an element of the subregion algebra.')
print()
print('  SO: YES, BINARY, AND CONSTRAINED')
print('     status is one bit per vocabulary -> 16 words.')
print('     the partition forces one-hot -> 5 admissible words (four unit vectors and zero).')
print('     a term needing a translator is one at ZERO that must be moved to a unit vector.')
print('     a term needing a SPLIT was two terms at different unit vectors all along.')
print('     a term needing a DICTIONARY sits at one unit vector under two different')
print('        labellings of that vocabulary - the scheme choice - and the dictionary')
print('        is a change of basis WITHIN a vocabulary, not between them.')
print()
print('  THE THREE REPAIRS, IN BITS')
R=[('SPLIT','two unit vectors mistaken for one','no bit changes; the merge was the error'),
   ('DICTIONARY','one unit vector, two bases','no bit changes; a rotation inside the vocabulary'),
   ('TRANSLATOR','weight 0 -> weight 1','one bit, manufactured by dressing')]
print('  %-12s %-38s %s' % ('repair','in bits','cost'))
for a2,b2,c2 in R: print('  %-12s %-38s %s' % (a2,b2,c2))