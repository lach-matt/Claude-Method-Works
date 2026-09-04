from collections import Counter
A=[
 ('n','principal quantum number',
  'CONFLATED','hydrogenic eigenvalue vs configuration label',
  'in hydrogen n = n_r + l + 1 is exact. in a many-electron atom no operator has '
  'eigenvalue n; it labels a configuration in the central-field approximation.'),
 ('l','orbital angular momentum, single electron',
  'CONFLATED','exact quantum number vs central-field label',
  'l is good only in the central field. and it is SINGLE-electron; the total L is '
  'a different quantity, which Lambda does not carry at all.'),
 ('k','occupancy of the (n,l) subshell',
  'clean','-','a counting number; unambiguous in any scheme'),
 ('q','the number available to transfer',
  'UNGROUNDED','no referent located in the spectroscopic literature',
  'q appears only in this construction, as 0 <= q <= k feeding g <= min(4f+2, q). '
  'it is transition-specific bookkeeping, not a spectroscopic label.'),
 ('e','target principal quantum number',
  'CONFLATED','as n','same defect as n, on the target'),
 ('f','target orbital angular momentum',
  'CONFLATED','as l','same defect as l, on the target'),
 ('g','occupancy of the target subshell',
  'clean','-','as k'),
 ('2S','total spin',
  'CONFLATED','subshell S vs atomic S',
  'Condon-Shortley S is the total spin of the ATOM in LS coupling. here it is the '
  'spin of one subshell. the two coincide only for a single open subshell.'),
 ("2S'",'target multiplicity',
  'CONFLATED','as 2S','same defect, on the target'),
 ('2J','total angular momentum',
  'clean','-','the final coupled J; unambiguous once the scheme is fixed'),
]
DONE=[
 ('2K','intermediate coupling',
  'CONFLATED','scheme-specific: Jc + l_outer (jK) vs L_tot + S_core (LK); jj has no K',
  'confirmed against the IVOA/NIST scheme definitions'),
 ('v','seniority',
  'clean','-','Racah: the number of particles not in J=0 pairs. matches.'),
 ('L','total orbital angular momentum',
  'MISSING','used and never indexed',
  "Racah's v is a label ADDITIONAL to L, S and J. Lambda reads L when computing the "
  "axis-11 bound and carries no L coordinate."),
]
print('  LAMBDA CONFLATION AUDIT -- all thirteen coordinates')
print()
print('  %-5s %-38s %-12s %s' % ('letter','meaning as built','status','merges / note'))
for a,b,c,d,e in A+DONE:
    print('  %-5s %-38s %-12s %s' % (a,b,c,d))
    print('  %-5s %-38s %-12s %s' % ('','','',e))
print()
cnt=Counter(c for _,_,c,_,_ in A+DONE)
print('  TALLY')
for k,v in sorted(cnt.items()): print('     %-12s %d' % (k,v))
tot=len(A)+len(DONE)
conf=cnt.get('CONFLATED',0)
print('     of %d coordinates: %d conflated (%.0f%%)' % (tot,conf,100*conf/tot))
print()
print('  COMPARISON')
print('     %-24s %8s %10s %8s' % ('index','letters','conflated','rate'))
print('     %-24s %8d %10d %7.0f%%' % ('violation index V1',9,5,100*5/9))
print('     %-24s %8d %10d %7.0f%%' % ('Lambda',tot,conf,100*conf/tot))
print()
print('  THE INVERSION')
print('     the paper presents Lambda as the CLEAN case and the violation index as the')
print('     contested one. proportionally Lambda is WORSE: %.0f%% against %.0f%%.' % (100*conf/tot,100*5/9))
print()
print('     and the causes are different in kind:')
print('        V1 conflated because two literatures used one word (unitarity, linearity).')
print('        Lambda conflates because an APPROXIMATION is not a coordinate:')
print('           n and l are exact in hydrogen and labels in everything else,')
print('           and the central-field approximation is nowhere in the index.')
print()
print('  A NEW CATEGORY: UNGROUNDED')
print('     q has no referent in the literature. it is not conflated - there is nothing')
print('     to conflate WITH. it is an index-internal construct that the paper presents')
print('     alongside n, l, k as though all four had the same provenance.')
print()
print('     audit 22 cannot detect this. it compares a rung to a theorem\'s meaning;')
print('     if no theorem names the term, the pair never appears in the table.')
print('     -> a FOURTH audit blind spot: coordinates with no external referent at all.')