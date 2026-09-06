#!/usr/bin/env python3
"""All datasets produced in the fifteen-letter session. Writes data3.json."""
import json, math, sys, random
from itertools import product, combinations, permutations
from collections import Counter, defaultdict
sys.path.insert(0, '/home/claude/method')
import method_tower as mt

OUT = {}

# ----------------------------------------------------------------- nine letters
RNG9 = [range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
NM9  = ['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_ = range(9)

def close9(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[0]>=3: rz(4,2)
        if x[1]>=2: rz(2,1)
        if x[2]>=2: rz(0,1)
        if x[3]>=2: rz(2,2)
        if x[3]>=1: rz(4,1)
        if x[4]>=4: rz(0,1)
        if x[5]>=1: rz(8,1)
        if x[6]>=1: rz(2,2)
        if x[7]>=2: rz(2,2); rz(5,1); rz(8,2)
        if x[8]>=2: rz(7,2)
    return tuple(x)

def envelopes(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in S:
                if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
            b,o=-99,{}
            for t in sorted(m): b=max(b,m[t]); o[t]=b
            phi[(i,j)]=o
    return vals,phi

def closure(S,d,want_excess=False):
    """Backtracking count of R(S); returns (E, excess list or None, box)."""
    S=set(S); vals,phi=envelopes(S,d)
    box=1
    for v in vals: box*=len(v)
    tot=0; ex=[]; cur=[None]*d
    def rec(i):
        nonlocal tot
        if i==d:
            tot+=1
            if want_excess:
                t=tuple(cur)
                if t not in S: ex.append(t)
            return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>phi[(i,j)][cur[j]] or cur[j]>phi[(j,i)][v]: ok=False; break
            if ok: cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return tot-len(S), (ex if want_excess else None), box

ALL9={close9(x) for x in product(*RNG9)}
V9=sorted({c for c in ALL9 if not(c[4]>=3 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))})
e9,ex9,box9=closure(V9,9,True)
O9=close9((0,1,0,0,1,0,0,0,0))
OUT['nine']={'cells':len(V9),'E':e9,'box':box9,'density':round(100*len(V9)/box9,2),
             'origin':list(O9),'core':[list(t) for t in sorted({(c[X_],c[U_],c[NEC_]) for c in ex9})]}

# --------------------------------------------------------------- fifteen letters
NM15=['X_exp','X_spon','Sc','IC','U_open','U_ghost','NEC_pt','NEC_ach',
      'L_dyn','L_kin','SD_obs','SD_field','DNc','DNd','EOM']
RNG15=[range(4),range(2),range(3),range(3),range(3),range(2),range(5),range(2),
       range(2),range(2),range(2),range(2),range(3),range(3),range(2)]
Xe,Xs,Sc,IC,Uo,Ug,Np,Na,Ld,Lk,So,Sf,Dc,Dd,EO = range(15)

MEANING=[
 ('X_exp','explicit Lorentz violation in the Lagrangian',4,'split from X'),
 ('X_spon','spontaneous Lorentz breaking (a VEV picks a frame)',2,'split from X'),
 ('Sc','CHSH correlation strength',3,'unchanged, clean'),
 ('IC','information causality',3,'unchanged, clean'),
 ('U_open','open-system non-unitarity (CPTP, Lindblad)',3,'split from U'),
 ('U_ghost','indefinite metric, ghosts',2,'split from U'),
 ('NEC_pt','null energy violation, graded by scale',5,'split from NEC'),
 ('NEC_ach','achronal ANEC violated',2,'split from NEC'),
 ('L_dyn','nonlinear evolution, state space linear (Weinberg)',2,'split from L'),
 ('L_kin','nonlinear state space, superposition fails',2,'split from L'),
 ('SD_obs','spacelike commutativity of observables',2,'split from SD'),
 ('SD_field','spacelike commutativity of fields',2,'split from SD'),
 ('DNc','cloning fidelity',3,'unchanged, partial conflation noted'),
 ('DNd','state discrimination',3,'unchanged, partial conflation noted'),
 ('EOM','derivative order of the equations of motion',2,'NEW'),
]
OUT['alphabet']=[{'letter':a,'meaning':b,'rungs':r,'provenance':p} for a,b,r,p in MEANING]

def close15(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[Xe]>=3: rz(Np,2); rz(Na,1)
        if x[Sc]>=2: rz(IC,1)
        if x[Uo]>=2: rz(IC,2)
        if x[Uo]>=1: rz(Np,1)
        if x[Np]>=4: rz(Xe,1)
        if x[Ld]>=1: rz(Dd,1)
        if x[So]>=1: rz(IC,2)
        if x[Dc]>=2: rz(IC,2); rz(Ld,1); rz(Dd,2)
        if x[Dd]>=2: rz(Dc,2)
        if x[Na]>=1: rz(Np,2)
        if x[Ug]>=1: rz(Xs,1)
        if x[Lk]>=1: rz(Dd,2)
        if x[EO]>=1: rz(Ug,1)
    return tuple(x)

CL15={close15(x) for x in product(*RNG15)}
NOTHEORY=len([c for c in CL15 if c[Sf]==1])
CL15={c for c in CL15 if c[Sf]==0}
V15={c for c in CL15 if not(c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)}
e15,ex15,box15=closure(V15,15,True)
O15=close15(tuple([0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]))
PIN=[Xe,Ug,Np,EO]; FREE=[i for i in range(15) if i not in PIN]
core15=sorted({tuple(c[i] for i in PIN) for c in ex15})
pat15=sorted({tuple(c[i] for i in FREE) for c in ex15})
OUT['fifteen']={'closed_before_charge':len(CL15)+NOTHEORY,'removed_no_theory':NOTHEORY,
  'cells':len(V15),'E':e15,'box':box15,'density':round(100*len(V15)/box15,2),
  'origin':list(O15),'core':[list(t) for t in core15],'patterns':len(pat15),
  'collapse_exact':len(core15)*len(pat15)==len(ex15),
  'pinned':[NM15[i] for i in PIN]}

# minimal failing subsets
mins=[]
for r in (2,3):
    found=[]
    for idx in combinations(range(15),r):
        if any(set(m)<=set(idx) for m in mins): continue
        P={tuple(c[i] for i in idx) for c in V15}
        if closure(P,r)[0]>0: found.append(idx)
    for idx in found:
        if not any(set(m)<set(idx) for m in mins): mins.append(idx)
    if found: break
OUT['fifteen']['minimal_supports']=[[NM15[i] for i in m] for m in mins]
OUT['fifteen']['arity']=len(mins[0]) if mins else None

# repairs at fifteen
T3={(c[Xe],c[Ug],c[Np]) for c in V15}
vals3=[sorted({t[i] for t in T3}) for i in range(3)]
zeros=0; tested=0; mn=None
for pa in permutations(range(len(vals3[0]))):
    ma={vals3[0][k]:pa[k] for k in range(len(vals3[0]))}
    for pb in permutations(range(len(vals3[1]))):
        mb={vals3[1][k]:pb[k] for k in range(len(vals3[1]))}
        for pc in permutations(range(len(vals3[2]))):
            mc={vals3[2][k]:pc[k] for k in range(len(vals3[2]))}
            S={(ma[t[0]],mb[t[1]],mc[t[2]]) for t in T3}
            v=closure(S,3)[0]; tested+=1
            if mn is None or v<mn: mn=v
            if v==0: zeros+=1
OUT['repairs15']={'relabel_tested':tested,'relabel_zeros':zeros,'relabel_min':mn,
                  'triple_cells':len(T3),'triple_E':closure(T3,3)[0]}
def phiv(S,i,j,v): return max([c[i] for c in S if c[j]<=v] or [-99])
OUT['repairs15']['phi_NEC_given_Xexp0']=phiv(V15,Np,Xe,0)
OUT['repairs15']['phi_NEC_given_Ughost0']=phiv(V15,Np,Ug,0)

# frontier formulas at fifteen (sampled verification)
def dP(c):
    v=tuple(c[i] for i in FREE)
    return min(sum(abs(v[k]-p[k]) for k in range(len(FREE))) for p in pat15)
def sP(c):
    v=tuple(c[i] for i in FREE)
    return min(sum(1 for k in range(len(FREE)) if v[k]!=p[k]) for p in pat15)
d_f=lambda c: c[Xe]+c[Ug]+abs(c[Np]-3)+c[EO]+dP(c)
s_f=lambda c: (1 if c[Xe]>0 else 0)+(1 if c[Ug]>0 else 0)+(1 if c[Np]!=3 else 0)+(1 if c[EO]>0 else 0)+sP(c)
rng=random.Random(0); samp=rng.sample(sorted(V15),1500)
bd=bs=0
for c in samp:
    bt=min(sum(abs(e[i]-c[i]) for i in range(15)) for e in ex15)
    bk=min(sum(1 for i in range(15) if e[i]!=c[i]) for e in ex15)
    if d_f(c)!=bt: bd+=1
    if s_f(c)!=bk: bs+=1
OUT['frontier15']={'sampled':len(samp),'d_mismatch':bd,'s_mismatch':bs,
  'our_d':d_f(O15),'our_s':s_f(O15),
  'mean_s':round(sum(s_f(c) for c in samp)/len(samp),2),
  'mean_d':round(sum(d_f(c) for c in samp)/len(samp),2),
  'single_letter_pct':round(100*sum(1 for c in samp if s_f(c)==1)/len(samp),1)}

# lattice map
guar=[c for c in V15 if c[Xe]==0 and c[So]==0 and c[Ug]==0]
OUT['lattice_map']={'guaranteed':len(guar),'of':len(V15),
  'pct':round(100*len(guar)/len(V15),1),'ours_included':O15 in guar,
  'acting':['X_exp','Sc','SD_obs','U_ghost'],
  'hypotheses':[('Lorentz invariance','X_exp = 0','indexable'),
                ('spacelike commutativity of observables','SD_obs = 0','indexable'),
                ('positive-definite metric','U_ghost = 0','indexable'),
                ('vacuum is lowest energy','-','not a letter'),
                ('vacuum not annihilated','-','not a letter')]}

# ------------------------------------------------------------- conflation audit
OUT['conflations']=[
 ('X','causal ladder','CONFLATED','spontaneous vs explicit Lorentz breaking; stated vs operative hypothesis',
  'the ghost condensate is a Lorentz-invariant THEORY with a Lorentz-violating VACUUM'),
 ('Sc','CHSH strength','clean','graded by a measured number',''),
 ('IC','information causality','clean','m>0 vs m=0 explicit in the grading',''),
 ('U','unitarity','CONFLATED','open-system (CPTP, metric intact) vs ghosts (indefinite metric)',
  'the spin-statistics postulate concerns the METRIC, which Lindblad preserves'),
 ('NEC','null energy','CONFLATED','ANEC vs ACHRONAL ANEC',
  'MMP violates ANEC and satisfies achronal ANEC; different theorems apply'),
 ('L','linearity','CONFLATED','dynamical (Weinberg) vs kinematical (state space)',
  'Lambda uses state-space structure only, never the evolution law'),
 ('SD','microcausality','CONFLATED','commutativity of OBSERVABLES vs of FIELDS',
  'wrong field choice gives identically vanishing fields, so no theory exists (Burgoyne)'),
 ('DNc','cloning','partial','deterministic vs probabilistic at rungs 0-1',
  'Rastegin: the cloning-discrimination equivalence is deterministic only'),
 ('DNd','discrimination','partial','as DNc',''),
]
OUT['conflation_counts']={'full':5,'partial':2,'clean':2}

# vocabulary debt
THMS={'Buniy-Hsu-Murray':['X','NEC','U'],'Hartman-Kundu-Tajdini':['U','X','SD','NEC'],
 'Wall (GSL)':['X','U','NEC'],'Graham-Olum':['NEC'],
 'spin-statistics (Luders-Zumino)':['X','SD','U','Sc'],'Burgoyne':['SD'],'Tsirelson':['Sc'],
 'Popescu-Rohrlich':['Sc','IC'],'Pawlowski':['IC','Sc'],'Banks-Susskind-Peskin':['U','IC'],
 'Nikolic':['U'],'Polchinski / Gisin':['L','IC'],'Abrams-Lloyd':['L'],'Weinberg':['L'],
 'Wootters-Zurek / Dieks':['DNc'],'Rastegin':['DNc','DNd'],'Simon-Buzek-Gisin':['DNc','IC'],
 'Soulas':['SD','IC'],'Sorkin':['SD'],'Creminelli et al':['NEC','X'],'Ford-Roman':['NEC'],
 'Dubovsky-Sibiryakov':['X','U'],'Deutsch / Lloyd (CTC)':['X','U','L','DNc','DNd'],
 'Ishibashi-Maeda-Mefford':['NEC','X']}
pairs=[(c,t) for t,cs in THMS.items() for c in cs]
CHECKED=16; CONF=7; PART=2
OUT['audit22']={'coordinates':9,'theorems':len(THMS),'pairs':len(pairs),
  'checked':CHECKED,'conflations':CONF,'partial':PART,'matches':CHECKED-CONF-PART,
  'unchecked':len(pairs)-CHECKED,
  'by_coord':{c:sum(1 for a,b in pairs if a==c) for c in NM9}}

# ------------------------------------------------------------ system of indices
IDXN=['V1 laws','V2 theory','V3 geometry','V4 algebra','V5 coupling','V6 solution','V7 degeneracy']
CH={'Buniy':(['V1 laws','V2 theory'],True),
    'Hartman':(['V1 laws','V2 theory','V3 geometry'],False),
    'Wall':(['V1 laws','V4 algebra','V5 coupling'],True),
    'Graham-Olum':(['V3 geometry','V6 solution'],True),
    'spin-statistics':(['V1 laws','V4 algebra'],True),
    'Ostrogradsky':(['V1 laws','V7 degeneracy'],True)}
def graph(active):
    E=set()
    for ch,(vs,fires) in CH.items():
        if ch not in active: continue
        for a,b in combinations(sorted(vs),2): E.add((a,b))
    adj=defaultdict(set)
    for a,b in E: adj[a].add(b); adj[b].add(a)
    seen=set(); comps=[]
    for v in IDXN:
        if v in seen: continue
        st=[v]; seen.add(v); g=[]
        while st:
            u=st.pop(); g.append(u)
            for w in adj[u]:
                if w not in seen: seen.add(w); st.append(w)
        comps.append(sorted(g))
    return E,comps,len(E)-len(IDXN)+len(comps),adj
Eall,Call,cycall,adjall=graph(set(CH))
live={ch for ch,(vs,f) in CH.items() if f}
Elive,Clive,cyclive,_=graph(live)
OUT['system']={'nodes':IDXN,'edges_all':len(Eall),'components_all':len(Call),'cycles_all':cycall,
  'edges_live':len(Elive),'components_live':len(Clive),'cycles_live':cyclive,
  'components_live_detail':Clive,
  'degrees':{v:sum(1 for a,b in Eall if a==v or b==v) for v in IDXN},
  'spans':{ch:len(vs) for ch,(vs,f) in CH.items()},
  'vacuous':[ch for ch,(vs,f) in CH.items() if not f],
  'unreachable':[v for c in Clive if 'V1 laws' not in c for v in c]}

# hypothesis coverage, nine vs fifteen
LETTERS15=set(NM15)
CH_OLD={'Buniy':4,'Hartman':5,'Wall':5,'GrahamOlum':5,'spin-statistics':5,'Ostrogradsky':1}
OUT['hyp_coverage']={'total_old':25,'indexable_old':4,'total_new':26,'indexable_new':9,
  'pct_old':16,'pct_new':35,'single_vocab_chargers':0,'min_span':2}

# ------------------------------------------------------- tower under parastatistics
def cap(l,m): return m*(4*l+2)
def base_m(caps,m):
    nn,ee,ll,kk,ff=caps; cells=[]
    for n in range(1,nn+1):
      for l in range(0,min(n-1,ll)+1):
        for k in range(1,min(cap(l,m),kk)+1):
          for q in range(0,k+1):
            for S2 in range(0,k+1):
              for e in range(1,ee+1):
                for f in range(0,min(e-1,ff)+1):
                  for g in range(0,min(cap(f,m),q)+1):
                    cells.append((n,l,k,q,e,f,g,S2))
    return cells
import itertools as _it
from functools import lru_cache
@lru_cache(maxsize=None)
def terms_m(l,k,m):
    orbs=[(ml,ms) for ml in range(-l,l+1) for ms in (1,-1)]
    cnt=Counter()
    for combo in _it.combinations_with_replacement(range(len(orbs)),k):
        c=Counter(combo)
        if any(v>m for v in c.values()): continue
        ML=sum(orbs[i][0]*n for i,n in c.items()); MS2=sum(orbs[i][1]*n for i,n in c.items())
        cnt[(2*ML,MS2)]+=1
    out=[]
    while cnt:
        L2=max(a for (a,b) in cnt); S2=max(b for (a,b) in cnt if a==L2)
        for a in range(-L2,L2+1,2):
            for b in range(-S2,S2+1,2):
                if (a,b) in cnt:
                    cnt[(a,b)]-=1
                    if cnt[(a,b)]==0: del cnt[(a,b)]
        out.append((S2,L2))
    return tuple(out)
@lru_cache(maxsize=None)
def max2J(l,k,m):
    js=set()
    for S2,L2 in terms_m(l,k,m):
        for j2 in range(abs(L2-S2),L2+S2+1,2): js.add(j2)
    return max(js) if js else 0
def phihat(k,lcap,m):
    best=0
    for kk in range(0,k+1):
        best=max(best,max((max2J(l,kkk,m) for l in range(0,lcap+1)
                           for kkk in range(1,min(cap(l,m),kk)+1)),default=0))
    return best
CAPS=(3,3,1,3,1); n_,e_,l_,k_,f_=CAPS
tower={}
for m in (1,2,3):
    B=base_m(CAPS,m); ph={k:phihat(k,l_,m) for k in range(0,k_+1)}
    L9=[c+(s,) for c in B for s in range(0,c[6]+1)]
    L10=[c+(v,) for c in L9 for v in range(c[8],c[6]+1)]
    L11=[c+(j,) for c in L10 for j in range(0,ph[c[2]]+1)]
    L12=[c+(K,) for c in L11 for K in range(0,c[10]+2*f_+1)]
    L13=[c+(J,) for c in L12 for J in range(max(0,c[11]-1),c[11]+2)]
    sizes=[]; Es=[]; boxes=[]
    for Xs_,d in [(B,8),(L9,9),(L10,10),(L11,11),(L12,12),(L13,13)]:
        S=set(Xs_); sizes.append(len(S))
        E,_,bx=closure(S,d); Es.append(E); boxes.append(bx)
    tower[m]={'sizes':sizes,'E':Es,'boxes':boxes}
OUT['tower_para']=tower

# ------------------------------------------------------ periodic table monotonicity
occ=set()
for g in (1,18): occ.add((1,g))
for p in (2,3):
    for g in [1,2,13,14,15,16,17,18]: occ.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): occ.add((p,g))
def block18(g):
    if g in (1,2): return 0
    if 3<=g<=12: return 2
    return 1
seq18=[block18(g) for g in range(1,19)]
byp=defaultdict(list)
for p,g in occ: byp[p].append(g)
contig={(p,i+1) for p,gs in byp.items() for i in range(len(gs))}
W=[2,2,8,8,18,18,32,32]
janet={(r+1,i+1) for r,w in enumerate(W) for i in range(w)}
P3={(p,g,block18(g)) for p,g in occ}
OUT['ptable_mono']={'l_by_group':seq18,
  'monotone_up':seq18==sorted(seq18),'monotone_down':seq18==sorted(seq18,reverse=True),
  'E_18col':closure(occ,2)[0],'E_contig':closure(contig,2)[0],'E_janet':closure(janet,2)[0],
  'E_with_l':closure(P3,3)[0],
  'E_period_l':closure({(p,block18(g)) for p,g in occ},2)[0],
  'E_group_l':closure({(g,block18(g)) for p,g in occ},2)[0]}
# non-monotone relation counts
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
OUT['failure_modes']=[
 {'object':'Lambda_8','nonmono':nonmono(set(mt.base(CAPS)),8),'arity':2,'E':0,
  'verdict':'null case'},
 {'object':'periodic table','nonmono':nonmono(P3,3),'arity':2,'E':36,
  'verdict':'sub-case A, ordering, REPAIRED by re-placement'},
 {'object':'violation index (9)','nonmono':nonmono(set(V9),9),'arity':3,'E':e9,
  'verdict':'sub-case B, arity, six repairs failed'},
 {'object':'violation index (15)','nonmono':nonmono(V15,15),'arity':3,'E':e15,
  'verdict':'sub-case B, survives the alphabet doubling'},
]

# ------------------------------------------------------------------- axis index
AXP=['rungs','exposure','lattice','conflation','measured','in-deg','out-deg']
NINE={'X':(4,8,2,2,2,2,1),'Sc':(3,4,2,0,2,0,1),'IC':(3,6,0,0,2,4,1),'U':(3,8,0,2,1,0,2),
 'NEC':(5,7,1,2,1,2,1),'L':(2,4,0,2,2,1,1),'SD':(2,5,2,2,2,0,1),
 'DNc':(3,4,0,1,2,1,3),'DNd':(3,2,0,1,2,2,1)}
SIXM={'CPT':(2,2,2,0,2,0,1),'E-p conservation':(2,1,0,0,2,1,0),'GSL':(2,3,0,0,0,1,1),
 'EOM order':(2,2,0,0,2,0,1),'equivalence principle':(2,1,0,0,2,0,0),
 'global symmetry':(2,1,0,0,1,0,0)}
Xax=set(NINE.values()); eax,_,bax=closure(Xax,7)
OUT['axis_index']={'cells':len(Xax),'E':eax,'box':bax,'density':round(100*len(Xax)/bax,2),
  'nonmono':nonmono(Xax,7),'open':eax>0,'properties':AXP}
v9ax=[sorted({c[i] for c in Xax}) for i in range(7)]
full=[range(2,6),range(1,9),range(0,3),range(0,3),range(0,3),range(0,5),range(0,4)]
UNOCC={AXP[i]:[v for v in full[i] if v not in v9ax[i]] for i in range(7)
       if [v for v in full[i] if v not in v9ax[i]]}
OUT['axis_index']['unoccupied']=UNOCC
def dirs(p): return tuple(a for a in UNOCC if p[AXP.index(a)] in UNOCC[a])
occd=defaultdict(list)
for n,p in SIXM.items(): occd[dirs(p)].append(n)
prs=[]
for a,b in combinations(UNOCC,2):
    got=[n for d,ns in occd.items() if set(d)=={a,b} for n in ns]
    prs.append({'pair':[a,b],'occupied_by':got})
OUT['axis_index']['pairs']=prs
OUT['axis_index']['predictions']=[
 {'pair':['exposure','in-deg'],'description':'rarely theorised, forced by three other coordinates','candidate':None},
 {'pair':['measured','in-deg'],'description':'unmeasured, forced by three others','candidate':'the holographic / Bekenstein bound'},
 {'pair':['measured','out-deg'],'description':'unmeasured and terminal, heavily theorised','candidate':'weak cosmic censorship'},
 {'pair':['in-deg','out-deg'],'description':'a pure sink: three things force it, it forces nothing','candidate':'black-hole information recovery'},
]

# --------------------------------------------------------------- density ladder
def dens(n,b): return round(100*n/b,2)
OUT['density_ladder']=[
 {'object':'periodic table','cells':90,'box':126,'pct':dens(90,126),'E_informative':True},
 {'object':'Lambda_8','cells':976,'box':6912,'pct':dens(976,6912),'E_informative':True},
 {'object':'violation index (15)','cells':len(V15),'box':box15,'pct':dens(len(V15),box15),'E_informative':True},
 {'object':'violation index (9)','cells':len(V9),'box':box9,'pct':dens(len(V9),box9),'E_informative':True},
 {'object':'Lambda_13','cells':199130,'box':47775744,'pct':dens(199130,47775744),'E_informative':False},
 {'object':'axis index','cells':9,'box':bax,'pct':dens(9,bax),'E_informative':False},
]

# ------------------------------------------------------------------ propositions
OUT['propositions']=[
 ('P1','X >= 1 -> U >= 1','REFUTED','the ordinary second law survives Lorentz violation (Eling et al)'),
 ('P2','NEC >= 3 -> X >= 1','REFUTED','Buniy is scoped to Lorentz-invariant theories'),
 ('P3','U >= 1 -> IC = 2','REFUTED','the U=1 rung is occupied; Lindblad operators computed (Nikolic)'),
 ('P4','U >= 1 -> X >= 1','FALSE ON THIS AXIS','true for ghosts, which were not a rung until the split'),
 ('P5','NEC >= 3 -> U >= 1','CONDITIONAL','flat space proven; curved rests on Graham-Olum'),
 ('P6','NEC >= 3 -> SD','NOT ASSERTABLE','a single disjunct of Hartman'),
 ('P7','NEC >= 3 -> IC = 2','NOT ASSERTABLE','a single disjunct of Hartman'),
]

# ------------------------------------------------------------------- the ledger
OUT['promotions']=[
 ('the two failure modes: ordering and arity','PROMOTE','four objects, each demonstrated computationally'),
 ('E requires density to be informative (asymmetric)','PROMOTE','measured on six objects; E=0 informative at any density'),
 ('audit 22 is necessary and cannot be automated','PROMOTE','21 audits passed on a document containing five conflations'),
 ('five of nine coordinates are conflated','PROMOTE','each shown against a named theorem with a quoted hypothesis'),
 ('the axis set is open','PROMOTE','computed at nine and at fifteen axes; E > 0 both times'),
 ('B.3.1 as a general law about all indices','HOLD','three instances, all built here, all in one session'),
 ('pair-completion predicts missing axes','HOLD','one confirmation from six hand-chosen cases'),
 ('the four predicted axes','HOLD','candidates; three have plausible occupants, none verified'),
 ('the vocabulary partition','HOLD','mine; no source draws those lines'),
 ('defect 30 / core 1 as physical numbers','HOLD','computed over a coordinate set that is demonstrably incomplete'),
]

OUT['withdrawals']=[
 ('defect 60, disjunction at NEC >= 2','the constraint is about scale; macroscopic wormholes are excluded, Planck-scale are not'),
 ('Helly number unbounded','a falling joint-given-pairwise ratio measures how often random families intersect, not the Helly number'),
 ('projection-covariance as a scaling law','the defect does not scale; the core is one cell at every resolution'),
 ('X >= 1 -> U >= 1','severed at its second link by the authors of its first'),
 ('instability routed to a disjunction','Buniy gives instability, not a preferred frame; the second disjunct was mine'),
 ('NEC is the unique family-A-preserving axis','it is one of eight'),
 ('the defect grows with jurisdiction count','it shrinks; narrower jurisdiction charges fewer cells'),
 ('MMP escapes the ANEC','it violates the ANEC and escapes the ACHRONAL ANEC'),
 ('a dropped edge in the exclusion classifier','DNc = 2 -> IC = 2 was omitted when transcribing the edge list'),
 ('the same-axis tautology, twice','the ANEC as a preservation is the NEC axis excluding itself; logged at nine letters and repeated at fifteen'),
 ('three obstructions, one theorem','reviving Hartman connects the system and CREATES a cycle; two obstructions, traded'),
 ('no curved-space extension exists (withdrawn, then restored)','withdrawn on an abstract whose scope-phrase modified the regulator, not the QNEC; restored on the full text'),
]

OUT['error_class']={'instances':12,'description':
 'a conclusion drawn from a comparison that was not licensed',
 'subtypes':['matching a rung to a theorem by the word rather than the content (U, L, X, SD)',
             'searching by the name of a result rather than by what implies it',
             'attaching a scope-phrase to the nearest noun rather than to what it modifies',
             'repeating a logged correction (the same-axis tautology)']}

with open('/home/claude/paper/data3.json','w') as f:
    json.dump(OUT,f,indent=1,default=str)
print('data3.json written')
for k in OUT:
    v=OUT[k]
    n=len(v) if isinstance(v,(list,dict)) else 1
    print('  %-20s %s' % (k, n))
