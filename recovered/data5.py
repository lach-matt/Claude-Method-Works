import json
from itertools import combinations
from collections import defaultdict
D=json.load(open('data4.json'))
N=['T','M','A','S']
CH={'Buniy-Hsu-Murray':(['S'],['T'],['A'],'fires'),
    'Hartman-Kundu-Tajdini':(['S'],['T','M'],['A','T'],'fires in flat space only'),
    'Wall (GSL)':(['M','S'],['T','A'],['A','T'],'fires'),
    'Graham-Olum':(['M','S'],['M'],['T'],'CONJECTURE, not a theorem'),
    'spin-statistics':(['A'],['T','A','S'],['A'],'fires'),
    'Ostrogradsky':(['T'],['T'],['A'],'fires')}
def spans(c):
    t,j,cu,f=CH[c]; return sorted(set(t)|set(j)|set(cu))
E=set()
for c in CH:
    for a,b in combinations(spans(c),2): E.add(tuple(sorted((a,b))))
adj=defaultdict(set)
for a,b in E: adj[a].add(b); adj[b].add(a)
seen=set(); comps=0
for v in N:
    if v in seen: continue
    comps+=1; st=[v]; seen.add(v)
    while st:
        u=st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
D['system_tmas']={'nodes':N,'edges':len(E),'components':comps,'cycles':len(E)-len(N)+comps,
 'complete':len(E)==len(N)*(len(N)-1)//2,
 'chargers':{k:{'trigger':v[0],'jurisdiction':v[1],'currency':v[2],'spans':spans(k),'status':v[3]}
             for k,v in CH.items()},
 'withdrawn':'the severance. V6 was never a node - self-consistency is a RELATION between M and S, '
             'and treating it as a vocabulary created a leaf only Graham-Olum touched. M stays '
             'reachable without Hartman because Wall spans T, A and M and fires.',
 'restated':'Graham-Olum is reachable and its trigger is not met: its trigger is ACHRONAL ANEC '
            'violation, and the core cell has NEC_ach = 0. A long wormhole violates the ANEC and '
            'satisfies the achronal ANEC.'}
D['graham_olum']={'status':'CONJECTURE with a sufficiency proof attached',
 'what_is_proved':'that the condition, IF it holds, rules out wormholes and closed timelike curves',
 'what_is_not':'the condition itself. "We indicate why such a condition might be expected to hold."',
 'age':'19 years, no proof, no counterexample',
 'function':'a filter, not a derivation: used to disqualify counterexamples',
 'why_violation_free':'by construction. the three known violation classes - chronal geodesics, '
                      'non-self-consistent solutions, Planck scale - are excluded by its own clauses.',
 'curved_cases':'a proof exists for near-horizon extremal black holes: another Killing horizon, '
                'the sixth independent instance of the same restriction',
 'correction':'the charger index listed FIRE = 1. a conjecture with a sufficiency proof is a third '
              'category the index does not have.'}
D['theorem_chain']=[
 ('T0','Reeh-Schlieder','the vacuum is cyclic and separating for local algebras',
  'the physical input that makes the rest applicable'),
 ('T1','Tomita-Takesaki','for (M, Omega) there exist Delta and J with Delta^it M Delta^-it = M',
  'supplies the modular flow sigma_t'),
 ('T2','Borchers / Wiesbrock','half-sided modular inclusion is CHARACTERISED by the existence of a '
  'one-parameter unitary group with positive Hermitian generator',
  'supplies the translation. an iff, not an implication. gap filled and extended to weights by '
  'Araki-Zsido 2004'),
 ('T3','Takesaki, Acta Math 131 (1973); Theory of Operator Algebras XII.1.1',
  'N = M crossed sigma^phi R is type II_infinity with a faithful semifinite normal trace tau, '
  'tau . theta_s = e^-s tau, and M = N crossed theta R, uniquely',
  'FLIPS THE BIT: type III_1 -> type II_infinity. an involution up to stabilisation.'),
 ('T4','semifiniteness','a semifinite factor carries a trace, hence a von Neumann entropy',
  'type III carries none'),
]
D['chain_caveats']=[
 ('T2 is the open problem','HSMI holds for cuts of KILLING horizons (Wall; Casini-Teste-Torroba; '
  'Witten). on an isolated horizon it is unproved - and because T2 is a characterisation, proving '
  'it is exactly equivalent to producing the positive-generator translation.'),
 ('T3 is stated for R','a 2024 result shows the generalisation to arbitrary locally compact groups '
  'is NOT automatic: it needs an invariant weight, KMS on a subgroup, and centrality of the modular '
  'automorphism group.'),
 ('the physical group is not R','Chandrasekaran-Flanagan cross by C-infinity(S^{d-2}), one generator '
  'per angle. their Appendix F reaches Takesaki through an ANGULAR MODE CUTOFF and an inductive '
  'limit. whether the limit satisfies the 2024 conditions is not settled here.'),
 ('the trace is not invariant','tau . theta_s = e^-s tau. this is why entropy in these constructions '
  'is defined only up to an additive constant.')]
D['repairs']={'kinds':[
 ('SPLIT','two unit vectors mistaken for one','no bit changes; the merge was the error',
  'U, L, SD, X - all four done here'),
 ('DICTIONARY','one unit vector, two bases','no bit changes; a rotation inside a vocabulary',
  '2K: Racah recoupling coefficients translate between LS, LK, jK and jj exactly'),
 ('TRANSLATOR','weight 0 -> weight 1','one bit, and it must be manufactured',
  'supertranslation: gravitational dressing, with corner edge modes as the output')],
 'no_dictionary':'n and l have none. exact hydrogenic eigenvalues and central-field labels are '
                 'related by a LIMIT, not an isomorphism, and a limit is not invertible.',
 'one_hot':{'terms_tested':40,'weight_0':2,'weight_1':35,'weight_2':3,
   'patterns_used':5,'patterns_available':16,
   'finding':'every term is physical in exactly one vocabulary, or in none. one-hot IS the partition.',
   'limit':'weight 2 means RELATION or CONFLATION and the test cannot tell them apart; '
           'weight 0 means UNGROUNDED or CONSTRUCTIBLE and likewise.',
   'new_findings':0},
 'functor':'A : Loc -> Alg is the geometry-to-algebra translator. it is well-defined on whole '
           'spacetimes and does not extend to subregions, because specifying a subregion requires '
           'dressing. the edge modes are what restores it.'}
D['withdrawals_2'].append(('the severance of the system graph',
  'an artefact of the seven-vocabulary partition. on T/M/A/S the graph is complete: 4 nodes, '
  '6 edges, 1 component. the six repairs failed on ARITY, which was always the explanation.'))
D['withdrawals_2'].append(('Graham-Olum listed as a charger that fires',
  'it is a conjecture with a sufficiency proof, not a theorem'))
D['error_class_2']['instances']=26
json.dump(D,open('data4.json','w'),indent=1,default=str)
print('data4.json extended')
print('  system_tmas:',{k:v for k,v in D['system_tmas'].items() if k in ('edges','components','cycles','complete')})
print('  chain steps:',len(D['theorem_chain']),' caveats:',len(D['chain_caveats']))
print('  withdrawals_2:',len(D['withdrawals_2']))