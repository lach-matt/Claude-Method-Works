#!/usr/bin/env python3
"""Session-2 datasets. Recomputes the cheap results; records provenance for the rest."""
import json, sys, itertools
from itertools import product, combinations
from collections import Counter, defaultdict
sys.path.insert(0,'/home/claude/method')
import method_tower as mt

O={}
def E(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in S:
                if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
            b,o=-99,{}
            for t in sorted(m): b=max(b,m[t]); o[t]=b
            ph[(i,j)]=o
    n=sum(1 for x in product(*vals) if all(x[i]<=ph[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))
    box=1
    for v in vals: box*=len(v)
    return n-len(S), box
def nonmono(S,d):
    bad=0
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in S: m[c[j]]=max(m.get(c[j],-99),c[i])
            s=[m[v] for v in sorted(m)]
            if s!=sorted(s) and s!=sorted(s,reverse=True): bad+=1
    return bad

# ---------------- the four vocabularies, derived from BFV
O['bfv']={'source':'Brunetti-Fredenhagen-Verch 2003, a functor A: Loc -> Alg',
 'parts':[('T THEORY','the functor itself, what the Lagrangian determines',
           ['X_exp','CPT','causality','field content','EOM derivative order','degeneracy',
            'interacting','dimension','xi coupling to curvature']),
          ('M SPACETIME','the source objects: globally hyperbolic spacetimes',
           ['flat / asymptotically flat / curved','simply connected','globally hyperbolic',
            'generic condition','spatially compact','achronality of a geodesic']),
          ('A ALGEBRA','the target objects: unital *-algebras',
           ['U_open','U_ghost','SD_obs','SD_field','L_dyn','L_kin','IC','DNc','DNd',
            'determinism','ultralocality','stability']),
          ('S STATE','functionals on the algebra',
           ['X_spon','Sc','NEC_pt','Hadamard','vacuum is lowest energy','vacuum not annihilated'])],
 'relations':['self-consistent semiclassical: a relation between M and S',
              'within the semiclassical regime: a relation on the pair',
              'backreaction included: the same relation as a modelling choice',
              'state-independent QEI availability: a relation between T and S'],
 'collapsed':[('V5 coupling','xi is a parameter of the theory -> T'),
              ('V6 solution','a relation between spacetime and state, not a vocabulary'),
              ('V7 degeneracy','a parameter of the theory -> T'),
              ('V2 theory','the functor itself, described by properties rather than graded')],
 'V1_spans':4}

# ---------------- V3 geometry, built and closed
NM3=['FLAT','CONN','HYP','GEN','ASYM']
R3=[range(3),range(2),range(2),range(2),range(2)]
FLAT,CONN,HYP,GEN,ASYM=range(5)
def cl3(x):
    x=list(x); g=True
    while g:
        g=False
        def up(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        def dn(i,v):
            nonlocal g
            if x[i]>v: x[i]=v; g=True
        if x[FLAT]==0: dn(CONN,0); dn(HYP,0); dn(GEN,0); dn(ASYM,0)
        if x[CONN]>=1: up(FLAT,1)
        if x[HYP]>=1:  up(FLAT,1)
        if x[ASYM]>=1: up(FLAT,2)
    return tuple(x)
V3={cl3(c) for c in {cl3(x) for x in product(*R3)}}
e3,b3=E(V3,5)
O['V3']={'letters':NM3,'cells':len(V3),'box':b3,'E':e3,'nonmono':nonmono(V3,5),
 'go_jurisdiction':len([c for c in V3 if c[FLAT]<=1 and c[CONN]==0 and c[ASYM]==0 and c[GEN]==0]),
 'clean':True,'source':'every letter has an exact Hawking-Ellis definition'}

# ---------------- V6 solution, built and closed
NM6=['SC','HAD','REG','ACH']
R6=[range(3),range(2),range(2),range(2)]
SC,HAD,REG,ACH=range(4)
def cl6(x):
    x=list(x); g=True
    while g:
        g=False
        def up(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[REG]>=1: up(SC,1)
        if x[HAD]>=1: up(REG,1)
    return tuple(x)
V6={cl6(c) for c in {cl6(x) for x in product(*R6)}}
e6,b6=E(V6,4)
O['V6']={'letters':NM6,'cells':len(V6),'box':b6,'E':e6,'nonmono':nonmono(V6,4),
 'admissible_for_GO':len([c for c in V6 if c[SC]==0 and c[REG]==0 and c[HAD]==0 and c[ACH]==0]),
 'violations_out_of_scope':4,'violations_total':5,
 'note':'REG "within the semiclassical regime" is itself conflated: no sharp definition'}

# ---------------- the local null-surface index
NMn=['THETA','SIGMA','STAT','COMP','ACH','TOP']
Rn=[range(2)]*6
TH,SG,ST,CM,AC,TP=range(6)
def cln(x):
    x=list(x)
    if x[ST]==0: x[TH]=0; x[SG]=0
    if x[TH]==0: x[SG]=0          # Raychaudhuri: non-expanding implies shear-free
    return tuple(x)
Vn={cln(c) for c in {cln(x) for x in product(*Rn)}}
en,bn=E(Vn,6)
O['null_surface']={'letters':NMn,'cells':len(Vn),'box':bn,'E':en,'nonmono':nonmono(Vn,6),
 'killing_cells':len([c for c in Vn if c[ST]==0]),
 'nonexpanding_cells':len([c for c in Vn if c[TH]==0]),
 'target':'HSMI on isolated horizons: non-expanding without a Killing field'}

# ---------------- the ANEC proof index
PROOFS={'Klinkhammer / Wald-Yurtsever':[(0,0,0,0)],
 'Faulkner-Leigh-Parrikar-Wang':[(0,0,0,0),(0,1,0,0)],
 'Hartman-Kundu-Tajdini':[(0,1,0,0)],'Kelly-Wall':[(0,1,0,0)],
 'Rosso (dS/AdS)':[(1,0,0,0),(1,1,0,0)],'Kontou-Olum':[(2,0,0,0)],
 'Wall (GSL)':[(2,0,0,1),(2,1,0,1)],'Iizuka-Ishibashi-Maeda':[(2,1,0,0)]}
COV=set()
for v in PROOFS.values(): COV|=set(v)
BOX=set(product(range(3),range(2),range(2),range(2)))
ea,ba=E(COV,4)
O['anec_index']={'axes':['GEOM','FIELD','COUP','BACK'],'cases':len(BOX),'covered':len(COV),
 'E':ea,'box':ba,'nonmono':nonmono(COV,4),'closed':ea==0,
 'coup1_covered':len([c for c in COV if c[2]==1]),
 'coup1_total':len([c for c in BOX if c[2]==1]),
 'withdrawn':['the 30-of-48 coverage figure','every curved proof crosses at free AND minimally coupled'],
 'finding':'COUP=1 is a wall, not an articulation point: the ANEC is FALSE there (Urban-Olum)'}

# ---------------- the measure index over Lambda
L8=sorted(set(mt.base((3,3,1,3,1))))
le=lambda a,b: all(a[i]<=b[i] for i in range(8))
pairs=[]
for i,a in enumerate(L8):
    for b in L8[i+1:]:
        if le(a,b): pairs.append((a,b))
        elif le(b,a): pairs.append((b,a))
def resolves(mu):
    unf=sum(1 for a,b in pairs if str(mu(a))==str(mu(b)))
    return 100*(len(pairs)-unf)/len(pairs), len({str(mu(c)) for c in L8})
MEAS=[('Coulomb  -1/n^2',lambda c:-1.0/c[0]**2),
      ('shell occupancy k',lambda c:c[2]),
      ('Madelung  n+l then n',lambda c:(c[0]+c[1])*100+c[0]),
      ('n, l, k',lambda c:(c[0]*100+c[1])*100+c[2]),
      ('grade  sum of coordinates',lambda c:sum(c)),
      ('the cell itself',lambda c:c)]
O['measure_index']={'ordered_pairs':len(pairs),'of':len(L8)*(len(L8)-1)//2,
 'measures':[{'name':n,'resolves':round(r,1),'values':v,'faithful':r==100.0}
             for n,f in MEAS for r,v in [resolves(f)]],
 'finding':'a faithful measure exists and compresses 976 cells to 18 values; '
           'physics does not use it. the Coulomb measure resolves 47.7% of the order.',
 'impossible_cell':'unfaithful bijection - impossible by definition, not by physics'}

# ---------------- the charger index
P=['TRIG','CUR','JUR','VOC','V1','FIRE']
CH={'Buniy-Hsu-Murray':(1,1,4,2,2,1),'Hartman-Kundu-Tajdini':(1,3,3,3,2,0),
    'Wall (GSL)':(1,2,5,3,1,1),'Graham-Olum':(1,1,5,2,0,1),
    'spin-statistics':(1,1,5,2,3,1),'Ostrogradsky':(1,1,1,2,1,1)}
Xc=set(CH.values()); ec,bc=E(Xc,6)
O['charger_index']={'properties':P,'cells':len(Xc),'box':bc,'E':ec,
 'density':round(100*len(Xc)/bc,1),'nonmono':nonmono(Xc,6),
 'absences':{'TRIG':'every charger has trigger arity 1; none is triggered by a conjunction',
             'JUR':'every charger has at least one jurisdiction condition; NONE is universal'},
 'convergence':'the empty JUR=0 direction is exactly the charger shape that would close '
               'the law index (an unjurisdicted forcing gives E=0 at 1,938 cells)',
 'pair_completion':'produces nothing here: all ten pairs empty, every charger inside the box'}

# ---------------- Lambda's conflation audit
O['lambda_audit']={'total':13,'conflated':7,'clean':4,'ungrounded':1,'missing':1,
 'rate':round(100*7/13),'v1_rate':round(100*5/9),
 'entries':[('n','hydrogenic eigenvalue vs configuration label','CONFLATED'),
            ('l','exact quantum number vs central-field label; single-electron, not total L','CONFLATED'),
            ('k','a counting number','clean'),
            ('q','no referent in the spectroscopic literature','UNGROUNDED'),
            ('e','as n','CONFLATED'),('f','as l','CONFLATED'),('g','as k','clean'),
            ('2S','subshell S vs atomic S','CONFLATED'),("2S'",'as 2S','CONFLATED'),
            ('2J','the final coupled J','clean'),
            ('2K','scheme-specific: Jc+l (jK) vs Ltot+Score (LK); jj has no K','CONFLATED'),
            ('v','Racah seniority: matches','clean'),
            ('L','used in the axis-11 bound and never indexed','MISSING')],
 'cause':'an approximation is not a coordinate. n and l are exact in hydrogen and labels '
         'everywhere else, and the central-field approximation is nowhere in the index.'}

# ---------------- coupling schemes
O['schemes']={'tested':['jK (as built)','LS','jj','LK'],
 'E_all_levels':0,'note':'uniform one-parameter looseness convention',
 'cells_L13':{'jK':199130,'LS':431050,'jj':206520,'LK':341150},
 'finding':'closure is NOT scheme-contingent. what IS scheme-contingent is what the letters MEAN.',
 'error':'a first run applied two-parent bounds to the alternatives and one-parent to jK, '
         'and reported the difference as a finding'}

# ---------------- the 2x2
O['closure_vs_conflation']={
 'closed_clean':['V3 geometry: 5 letters, E=0, 0 conflated'],
 'closed_conflated':['Lambda: 13 letters, E=0, 7 conflated, 1 ungrounded, 1 missing',
                     'V6 solution: 4 letters, E=0, 1 conflated'],
 'open_conflated':['V1 laws: 15 letters, E=816'],
 'open_clean':[],
 'finding':'CLOSURE DOES NOT CERTIFY THE LETTERS. an index can be globally consistent '
           'and still not mean what it says.',
 'null_case':'transfers from Lambda to V3'}

# ---------------- audits 23 and 24
O['audits']={'suite':21,'blind_spots':4,
 'list':[('22 term match','external + judgement','IDENTIFIED, unfillable by code',
          'debt 32 of 48 pairs'),
         ('23 published values','external + mechanical','BUILT',
          '10 of 10 LS term tables reproduced; 0 microstate mismatches'),
         ('24 unbacked claims','internal + debt','BUILT',
          '14 of 105 numeric claims unbacked; 5 false positives, 6 substantive, 0 wrong'),
         ('25 ungrounded coordinates','no external referent at all','IDENTIFIED',
          "audit 22 cannot see it: if no theorem names the term, the pair never appears")],
 'note':'audit 23 is the only external validation in the construction'}

# ---------------- the shape, and its one test
O['shape']={'statement':'a term whose status is scope-dependent, carried by an index that '
                        'does not carry the scope',
 'instances':[('Buniy','a hypothesis operative in one scope and not another'),
              ('U, L, SD, X','a word meaning one thing in one literature and another elsewhere'),
              ('2K','a label meaning different things in different coupling schemes'),
              ('n, l','exact in hydrogen, approximate everywhere else'),
              ('supertranslation','gauge in geometry, physical in the algebra')],
 'test':'where an anchor exists (null infinity) supertranslations carry nonvanishing charges '
        'and are physical in BOTH vocabularies; where it is absent (a bare NEH) the NEH free '
        'data is provably supertranslation-invariant. the reversal is present exactly where '
        'the anchor is absent.',
 'provenance':'the shape came from the NEH invariance result and the algebra region-dependence; '
              'the test facts came from BMS charges and the memory effect, an untouched literature',
 'status':'one directed test, passed; one directed search for a counterexample, none found'}

# ---------------- the modular-theory relocation
O['modular']={'finding':'the ANEC gap in curved spacetime is a MODULAR THEORY gap',
 'evidence':'five of six curved-space routes require a Killing field or a horizon generated '
            'by one; the sixth replaces it with a holographic dual and yields a weighted bound',
 'boundary':'Sorce 2024: any geometric modular flow must be generated by a conformal Killing '
            'field. so the near-horizon-boost extension is EXCLUDED, not merely unproved.',
 'route':'half-sided modular inclusion gives K in terms of T without geometric flow',
 'target':'HSMI on isolated horizons - one cell from where it is proved',
 'literature':'Chandrasekaran-Flanagan Jan 2026: corner edge modes supply both the dressing '
              'anchor and the half-sided translation generator; the two-sidedness enters only '
              'through the expansion and vanishes on a non-expanding horizon'}

O['withdrawals_2']=[
 ('arity tracks vocabulary span','falsified: eight binary cross-vocabulary edges give E=0, '
  'and a two-vocabulary ternary constraint gives E=176. arity determines arity.'),
 ('the 30-of-48 ANEC coverage figure','superseded: 8 of 24, and half the box is a region '
  'where the statement is false'),
 ('every curved proof crosses at free, minimally coupled','only minimally coupled is shared'),
 ('Lambda as the clean control','7 of 13 letters conflated; the null case transfers to V3'),
 ('the seven-vocabulary partition','derived down to four from the BFV functor'),
 ('Hartman is vacuous','it fires in flat space and excludes 2 cells; the earlier computation '
  'was circular, having built Hartman-plus-more into the cross-edge'),
 ('the nine-letter density of 3.99%','the box is 19,440; the density is 12.19%'),
 ('the bilingual equation is arity 3','it is arity 2, and the script printed a pre-written '
  'conclusion contradicting its own output'),
 ('promotion as an ordering repair','made E worse, 8 to 16'),
 ('the observer resolves the reversal','the encoding forced ST constant; E=0 was trivial'),
 ('the curved-space extension needs a near-horizon boost theorem','excluded by Sorce'),
 ('the coupling-scheme comparison','an unfair convention applied to the alternatives'),
]
O['error_class_2']={'instances':24,'dominant_subtype':'the encoding carries the conclusion',
 'note':'four consecutive attempts at the bilingual repair each embedded the answer in the setup'}

json.dump(O,open('/home/claude/paper/data4.json','w'),indent=1,default=str)
print('data4.json written')
for k,v in O.items():
    print('  %-22s %s' % (k, len(v) if isinstance(v,(dict,list)) else ''))
