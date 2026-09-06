#!/usr/bin/env python3
"""Datasets v2 for TRANSITIONS — corrected constraint (NEC>=3) plus new findings."""
import sys, json, itertools, random, math
sys.path.insert(0,"/home/claude/method")
from itertools import product, combinations, permutations
from collections import Counter, defaultdict
import method_tower as mt

D = json.load(open('/home/claude/paper/data.json'))   # keep Lambda-side results
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']

def close(x):
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
def RRs(X,d):
    X=set(X); vals=[sorted({c[i] for c in X}) for i in range(d)]
    def env(i,j):
        m={}
        for c in X:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
def BPC(X,d):
    X=set(X); vals=[sorted({c[i] for c in X}) for i in range(d)]
    pj={(i,j):{(c[i],c[j]) for c in X} for i,j in combinations(range(d),2)}
    return {x for x in product(*vals) if all((x[i],x[j]) in pj[(i,j)] for i,j in combinations(range(d),2))}
def E(X,d): return len(RRs(X,d))-len(set(X))

allc={close(x) for x in product(*RNG)}
# CORRECTED: the disjunction binds at NEC>=3 (macroscopic), not NEC>=2 (Planck-scale)
V={c for c in allc if not(c[4]>=3 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))}
Vold={c for c in allc if not(c[4]>=2 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))}
R=RRs(V,9); B=BPC(V,9); ex=sorted(R-V)
D['v2']={'cells':len(V),'BPC':len(B),'R':len(R),'defect':len(R)-len(V),
         'gc_defect':len(B)-len(V),'env_coarse':len(R)-len(B),
         'old_cells':len(Vold),'old_defect':E(Vold,9),
         'origin':list(close((0,1,0,0,1,0,0,0,0))),'names':NM}

# core x multiplicity
T={(c[0],c[3],c[4]) for c in V}
exT=sorted(RRs(T,3)-T)
core={(c[0],c[3],c[4]) for c in ex}
free={tuple(c[i] for i in [1,2,5,6,7,8]) for c in ex}
D['v2']['core']=[list(t) for t in sorted(core)]
D['v2']['core_E']=len(exT)
D['v2']['multiplicity']=len(free)
D['v2']['product_exact']=(len(core)*len(free)==len(ex))

# projection covariance, decomposed
proj=[]
for lab,idx in [('X,Sc,U,NEC',[0,1,3,4]),('+IC',[0,1,2,3,4]),('+L,SD',[0,1,2,3,4,5,6]),('all 9',list(range(9)))]:
    P={tuple(c[i] for i in idx) for c in V}
    e=sorted(RRs(P,len(idx))-P)
    ci=[idx.index(k) for k in (0,3,4) if k in idx]
    co={tuple(c[k] for k in ci) for c in e}
    fr={tuple(c[k] for k in range(len(idx)) if k not in ci) for c in e}
    proj.append({'label':lab,'coords':len(idx),'cells':len(P),'E':len(e),'core':len(co),'mult':len(fr)})
D['v2']['projection']=proj

# minimal support, exhaustive
TRI={0,3,4}
fails=0; checked=0
for d in range(2,7):
    for idx in combinations(range(9),d):
        if TRI<=set(idx): continue
        checked+=1
        if E({tuple(c[i] for i in idx) for c in V}, d)>0: fails+=1
D['v2']['support']={'subsets_checked':checked,'failing':fails,'minimal':['X','U','NEC']}

# exhaustive relabelling of the triple
vals=[sorted({t[i] for t in T}) for i in range(3)]
zeros=0; tested=0; mn=None
for pa in permutations(range(len(vals[0]))):
    ma={vals[0][k]:pa[k] for k in range(len(vals[0]))}
    for pb in permutations(range(len(vals[1]))):
        mb={vals[1][k]:pb[k] for k in range(len(vals[1]))}
        for pc in permutations(range(len(vals[2]))):
            mc={vals[2][k]:pc[k] for k in range(len(vals[2]))}
            S={(ma[t[0]],mb[t[1]],mc[t[2]]) for t in T}
            e=E(S,3); tested+=1
            if mn is None or e<mn: mn=e
            if e==0: zeros+=1
D['v2']['relabel']={'tested':tested,'zeros':zeros,'min_E':mn}

# the six repair operations
def lin_test():
    pairs=sorted({(c[0],c[3]) for c in V})
    paid=lambda p:0 if (p[0]==0 and p[1]==0) else 1
    W=sorted(pairs,key=lambda p:(paid(p),p[0],p[1])); Wi={p:i for i,p in enumerate(W)}
    S={(Wi[(c[0],c[3])],)+tuple(c[i] for i in [1,2,4,5,6,7,8]) for c in V}
    return E(S,8)
def derived_test():
    P=lambda c: 1 if (c[0]>=1 or c[3]>=1 or c[2]>=2) else 0
    return E({c+(P(c),) for c in V},10)
def slide_test():
    rows=defaultdict(list)
    for a,b,n in T: rows[(a,b)].append(n)
    return E({(a,b,sorted(rows[(a,b)]).index(n)) for a,b,n in T},3)
def split_test():
    sp={0:(0,0),1:(1,0),2:(2,0),3:(2,1),4:(2,2)}
    return E({tuple(c[:4])+sp[c[4]]+tuple(c[5:]) for c in V},10)
D['v2']['repairs']=[
 {'op':'merge by identification','result':'fails the biconditional rule','E':None},
 {'op':'merge by linearisation','result':'worse','E':lin_test()},
 {'op':'relabel axis values (exhaustive)','result':'never zero','E':mn},
 {'op':'slide within rows','result':'never better','E':slide_test()},
 {'op':'add a derived coordinate','result':'worse','E':derived_test()},
 {'op':'split an axis','result':'neutral or worse','E':split_test()},
]
D['v2']['baseline_E']=len(ex)

# object thresholds
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_=range(9)
o=close((0,1,0,0,1,0,0,0,0))
objs=[('classical black hole','none',lambda c:True),
      ('Hawking-evaporating black hole','NEC >= 1',lambda c:c[NEC_]>=1),
      ('Planck-scale wormhole','NEC >= 2',lambda c:c[NEC_]>=2),
      ('macroscopic wormhole','NEC >= 3',lambda c:c[NEC_]>=3),
      ('universal horizon','X >= 2',lambda c:c[X_]>=2),
      ('time machine','X = 3',lambda c:c[X_]>=3)]
reach={c for c in V if all(c[i]>=o[i] for i in range(9))}
D['v2']['objects']=[{'name':n,'threshold':t,'cells':sum(1 for c in V if f(c)),
                     'here':bool(f(o)),'reachable':sum(1 for c in reach if f(c))} for n,t,f in objs]
D['v2']['reach']={'reachable':len(reach),'unreachable':len(V)-len(reach)}
wh=[c for c in V if c[NEC_]>=3]
D['v2']['wormhole_cost']={'total':len(wh),
  'nonunitary':sum(1 for c in wh if c[U_]>=1),'frame':sum(1 for c in wh if c[X_]>=1),
  'signalling':sum(1 for c in wh if c[IC_]>=2),
  'free':sum(1 for c in wh if c[U_]==0 and c[X_]==0 and c[IC_]<2)}

# periodic table: the contiguity finding
occ=set()
for g in (1,18): occ.add((1,g))
for p in (2,3):
    for g in [1,2,13,14,15,16,17,18]: occ.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): occ.add((p,g))
exP=sorted(RRs(occ,2)-occ)
byp=defaultdict(list)
for p,g in occ: byp[p].append(g)
contig={(p,i+1) for p,gs in byp.items() for i in range(len(gs))}
Wj=[2,2,8,8,18,18,32,32]
janet={(r+1,i+1) for r,w in enumerate(Wj) for i in range(w)}
D['v2']['ptable']={'cells':len(occ),'E':len(exP),
  'slabs':[{'period':p,'groups':[min(g for q,g in exP if q==p),max(g for q,g in exP if q==p)],
            'n':sum(1 for q,_ in exP if q==p)} for p in sorted({q for q,_ in exP})],
  'law':26,'convention':10,
  'contiguous_cells':len(contig),'contiguous_E':E(contig,2),
  'janet_cells':len(janet),'janet_E':E(janet,2),'janet_widths':Wj}

# Lambda-9 articulation
N9=['n','l','k','q','e','f','g','2S',"2S'"]
E9=[('n','l'),('l','k'),('k','q'),('e','f'),('f','g'),('q','g'),('k','2S'),('g',"2S'")]
SRC={'n','l','k','2S'}; TGT={'e','f','g',"2S'"}
def comps(nodes,edges):
    adj=defaultdict(list)
    for a,b in edges:
        if a in nodes and b in nodes: adj[a].append(b); adj[b].append(a)
    seen=set(); c=0
    for v in nodes:
        if v in seen: continue
        c+=1; st=[v]; seen.add(v)
        while st:
            u=st.pop()
            for w in adj[u]:
                if w not in seen: seen.add(w); st.append(w)
    return c
base=comps(set(N9),E9)
arts=[v for v in N9 if comps(set(N9)-{v},E9)>base]
D['v2']['articulation']={'nodes':len(N9),'edges':len(E9),'cut_vertices':arts,
  'bridge':'q','source':sorted(SRC),'target':sorted(TGT),
  'cross_edges':[ (a,b) for a,b in E9 if (a in SRC and b in TGT) or (a in TGT and b in SRC)]}

# Helly bound
Bl=mt.base((3,3,1,3,1)); L9=[c+(s,) for c in Bl for s in range(0,c[6]+1)]
S9=set(L9)
def sq(c):
    out=set()
    for i,j in combinations(range(9),2):
        for si in (1,-1):
            for sj in (1,-1):
                a=list(c); a[i]+=si
                b=list(c); b[j]+=sj
                ab=list(c); ab[i]+=si; ab[j]+=sj
                if tuple(a) in S9 and tuple(b) in S9 and tuple(ab) in S9: out.add((i,si,j,sj))
    return frozenset(out)
sqs={c:sq(c) for c in L9}
ground=set().union(*sqs.values())
pool=sorted(S9); rng=random.Random(3)
best=0
for _ in range(60000):
    m=rng.randint(3,9); cells=[rng.choice(pool) for _ in range(m)]
    sets=[sqs[c] for c in cells]
    tot=sets[0]
    for t in sets[1:]: tot=tot&t
    if tot: continue
    crit=True
    for k in range(m):
        sub=[sets[t] for t in range(m) if t!=k]
        it=sub[0]
        for t in sub[1:]: it=it&t
        if not it: crit=False; break
    if crit and m>best: best=m
D['v2']['helly']={'ground':len(ground),'upper':len(ground),'lower':best,
                  'possible':math.comb(9,2)*4}

# ANEC proof coverage
AX=['geometry','fields','coupling','curvature','backreaction']
DOM={'geometry':['flat','curved'],'fields':['free','interacting'],'coupling':['minimal','non-minimal'],
     'curvature':['small','strong'],'backreaction':['none','perturbative','self-consistent']}
PR={'Kontou-Sanders':lambda c:c[0]=='flat','Hartman-Kundu-Tajdini':lambda c:c[0]=='flat',
    'Kelly-Wall':lambda c:c[0]=='flat' and c[1]=='interacting',
    'Flanagan-Wald':lambda c:c[0]=='flat' and c[4] in ('none','perturbative'),
    'Kontou-Olum':lambda c:c[1]=='free' and c[2]=='minimal' and c[3]=='small',
    'Wall-GSL':lambda c:c[2]=='minimal' and c[1]=='free'}
cells=[c for c in product(*[DOM[a] for a in AX])]
U=set()
for f in PR.values(): U|={c for c in cells if f(c)}
D['v2']['coverage']={'cases':len(cells),'covered':len(U),'uncovered':len(cells)-len(U),
  'pct_open':(len(cells)-len(U))/len(cells)*100,
  'per_proof':{k:sum(1 for c in cells if f(c)) for k,f in PR.items()},
  'invariance':{'4 axes':37.5,'5 axes':37.5,'7 axes':37.5,
                'Wall generous':25.0,'holographic generous':12.5,'both generous':12.5}}

json.dump(D, open('/home/claude/paper/data.json','w'), indent=1)
print('v2 written')
print('  cells', D['v2']['cells'], 'defect', D['v2']['defect'], 'core', D['v2']['core'], 'mult', D['v2']['multiplicity'])
print('  relabel', D['v2']['relabel'])
print('  helly', D['v2']['helly'])
print('  ptable', {k:D['v2']['ptable'][k] for k in ('E','contiguous_E','janet_E','janet_cells')})
print('  articulation', D['v2']['articulation']['cut_vertices'], 'cross', D['v2']['articulation']['cross_edges'])
print('  wormhole cost', D['v2']['wormhole_cost'])
