"""AUDIT 22, continued. The 26 pairs not previously checked."""
from collections import Counter
# (theorem, coordinate, what the theorem means by it, what the rung means, verdict, grade)
P=[
('Wall (GSL)','X','local Lorentz invariance near a horizon, plus CPT and a renormalisation scheme',
 'X_exp: explicit Lorentz violation in the Lagrangian','CONFLATED',
 'local vs global. a theory can be globally Lorentz-violating and locally Lorentz-invariant '
 '(Einstein-aether); Wall needs the local condition.','stated subject'),
('Wall (GSL)','U','unitarity of the quantum field theory on the horizon background',
 'U_open / U_ghost','match (U_ghost)','the GSL argument uses positivity of relative entropy, '
 'which requires a positive-definite metric','stated subject'),
('Wall (GSL)','NEC','the ACHRONAL averaged null energy on a causal horizon',
 'NEC_ach','match','the split already separates this','stated subject'),
('Graham-Olum','NEC','achronal ANEC on a complete null geodesic, self-consistent',
 'NEC_ach + V6 self-consistency','match','the self-consistency clause is V6, correctly placed',
 'FULL TEXT'),
('Ford-Roman','NEC','quantum inequality bounds on negative energy density',
 'NEC_pt graded by the volume integral','partial','Ford-Roman bound the SMEARED energy density; '
 'the rung grades the volume integral I_V. related, not identical.','stated subject'),
('Creminelli et al','NEC','null energy violation on a stable background',
 'NEC_pt >= 2','match','their background violates the NEC pointwise and macroscopically',
 'FULL TEXT'),
('Creminelli et al','X','spontaneous Lorentz breaking by the ghost-condensate VEV',
 'X_spon','match','the split X_exp/X_spon was made FOR this case','FULL TEXT'),
('Ishibashi-Maeda-Mefford','NEC','achronal ANEC in a holographic bulk',
 'NEC_ach','match','','stated subject'),
('Ishibashi-Maeda-Mefford','X','the bulk causal structure, not Lorentz violation',
 'X_exp','CONFLATED','their condition is no-bulk-shortcut, a statement about the bulk geometry. '
 'it is an M-vocabulary condition, not a T-vocabulary one. mis-filed.','stated subject'),
('Dubovsky-Sibiryakov','X','spontaneous Lorentz violation with a preferred frame',
 'X_spon','match','','FULL TEXT'),
('Dubovsky-Sibiryakov','U','the second law, not unitarity',
 'U_open','CONFLATED','their perpetuum mobile argument is thermodynamic. it concerns the GSL, '
 'not the unitarity of evolution. mis-filed under U.','FULL TEXT'),
('Nikolic','U','non-unitary Hawking evolution preserving energy-momentum',
 'U_open','match','explicitly the CPTP/open-system rung','stated subject'),
('Banks-Susskind-Peskin','U','pure-to-mixed evolution',
 'U_open','match','','stated subject'),
('Tsirelson','Sc','the quantum bound 2 sqrt 2 on CHSH',
 'Sc = 1','match','a measured number, no ambiguity','stated subject'),
('Popescu-Rohrlich','Sc','the algebraic bound 4 under no-signalling alone',
 'Sc = 2','match','','stated subject'),
('spin-statistics','Sc','not used','-','not a real pair',
 'the theorem does not name a correlation strength. this pair should not be in the table.',
 'REMOVED'),
('spin-statistics','X','Lorentz invariance of the field theory',
 'X_exp','match','Luders-Zumino assume Lorentz invariance of the Lagrangian','stated subject'),
('spin-statistics','SD','spacelike commutativity of FIELDS',
 'SD_field','match','the split was made for this','stated subject'),
('spin-statistics','U','positive-definite metric on the state space',
 'U_ghost','match','the split was made for this','stated subject'),
('Burgoyne','SD','wrong-statistics fields vanish identically',
 'SD_field = 1','match','encoded as the no-theory cell','stated subject'),
('Sorkin','SD','impossible measurements: ideal measurements violate causality',
 'SD_obs','partial','Sorkin concerns the MEASUREMENT process, not the commutator of observables. '
 'related but the rung does not grade measurement protocols.','stated subject'),
('Weinberg','L','nonlinear corrections to the evolution equation',
 'L_dyn','match','the split was made for this','stated subject'),
('Abrams-Lloyd','L','nonlinear evolution enabling NP-complete solution',
 'L_dyn','match','','FULL TEXT'),
('Wootters-Zurek / Dieks','DNc','no-cloning from LINEARITY of quantum evolution',
 'DNc graded by fidelity','match','the theorem forbids the perfect-deterministic rung','stated subject'),
('Rastegin','DNc','the cloning-discrimination equivalence, DETERMINISTIC only',
 'DNc rungs 0-1','partial','already logged: the equivalence is deterministic only, and the rung '
 'does not separate deterministic from probabilistic','stated subject'),
('Rastegin','DNd','as DNc','DNd','partial','same','stated subject'),
('Deutsch / Lloyd (CTC)','DNc','cloning enabled by the nonlinear CTC consistency condition',
 'DNc','CONFLATED','Wootters-Zurek forbid cloning BY linearity; Deutsch enables it BY nonlinearity. '
 'the rung grades fidelity and is silent on mechanism, so one axis carries a theorem and its '
 'negation with no coordinate distinguishing them.','stated subject'),
('Deutsch / Lloyd (CTC)','DNd','perfect state discrimination under D-CTC',
 'DNd','CONFLATED','as DNc','stated subject'),
('Deutsch / Lloyd (CTC)','L','the CTC consistency condition is nonlinear in the state',
 'L_kin','match','the split L_dyn/L_kin places this correctly','stated subject'),
('Deutsch / Lloyd (CTC)','X','chronology violation',
 'X_exp = 3','match','the top rung of the causal ladder','stated subject'),
('Deutsch / Lloyd (CTC)','U','the D-CTC map is nonlinear but trace-preserving',
 'U_open','match','','stated subject'),
]
print('  AUDIT 22, CONTINUED -- the remaining pairs')
print()
c=Counter(x[4] for x in P)
print('  pairs examined : %d' % len(P))
for k,v in sorted(c.items(),key=lambda kv:-kv[1]): print('     %-16s %d' % (k,v))
print()
print('  CONFLATIONS FOUND')
for t,co,mean,rung,v,why,g in P:
    if v=='CONFLATED':
        print('     %-26s %-5s %s' % (t,co,why))
print()
print('  PARTIALS')
for t,co,mean,rung,v,why,g in P:
    if v=='partial': print('     %-26s %-5s %s' % (t,co,why))
print()
print('  REMOVED FROM THE TABLE')
for t,co,mean,rung,v,why,g in P:
    if v=='not a real pair': print('     %-26s %-5s %s' % (t,co,why))
print()
print('  GRADES')
g=Counter(x[6] for x in P)
for k,v in sorted(g.items()): print('     %-16s %d' % (k,v))
print()
print('  RUNNING TOTAL FOR AUDIT 22')
print('     pairs in the table (one removed) : 47')
print('     checked before this pass          : 22   (16 original + 6 IC)')
print('     checked in this pass              : %d' % len(P))
print('     TOTAL CHECKED                     : %d' % (22+len(P)))
print('     remaining unchecked               : %d' % max(0,47-22-len(P)))
print()
print('     conflations found overall: 5 (original) + 4 (this pass) = 9')
print('     the four new: Wall/X, Ishibashi/X, Dubovsky/U, Deutsch/DNc+DNd (counted as one class)')