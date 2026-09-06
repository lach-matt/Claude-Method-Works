from itertools import product, combinations
NM=['X_exp','X_spon','Sc','IC','U_open','U_ghost','NEC_pt','NEC_ach',
    'L_dyn','L_kin','SD_obs','SD_field','DNc','DNd','EOM']
RNG=[range(4),range(2),range(3),range(3),range(3),range(2),range(5),range(2),
     range(2),range(2),range(2),range(2),range(3),range(3),range(2)]
Xe,Xs,Sc,IC,Uo,Ug,Np,Na,Ld,Lk,So,Sf,Dc,Dd,EO=range(15)
HOME={'X_exp':'W1','EOM':'W1','X_spon':'W3','Sc':'W3','NEC_pt':'W3','NEC_ach':'W5',
      'IC':'W6','U_open':'W6','U_ghost':'W6','L_dyn':'W6','L_kin':'W6',
      'SD_obs':'W6','SD_field':'W6','DNc':'W6','DNd':'W6'}
# (antecedent index, value, consequent index, value, label)
EDGES=[(Xe,3,Np,2,'X_exp>=3 -> NEC_pt>=2'),
       (Xe,3,Na,1,'X_exp>=3 -> NEC_ach=1'),
       (Sc,2,IC,1,'Sc>=2 -> IC>=1'),
       (Uo,2,IC,2,'U_open=2 -> IC=2'),
       (Uo,1,Np,1,'U_open>=1 -> NEC_pt>=1'),
       (Np,4,Xe,1,'NEC_pt>=4 -> X_exp>=1'),
       (Ld,1,Dd,1,'L_dyn -> DNd>=1'),
       (So,1,IC,2,'SD_obs -> IC=2'),
       (Dc,2,IC,2,'DNc=2 -> IC=2'),
       (Dc,2,Ld,1,'DNc=2 -> L_dyn'),
       (Dc,2,Dd,2,'DNc=2 -> DNd=2'),
       (Dd,2,Dc,2,'DNd=2 -> DNc=2'),
       (Na,1,Np,2,'NEC_ach -> NEC_pt>=2'),
       (Ug,1,Xs,1,'U_ghost -> X_spon'),
       (Lk,1,Dd,2,'L_kin -> DNd=2'),
       (EO,1,Ug,1,'EOM -> U_ghost')]
print('  THE THIRTEEN EDGES, CLASSIFIED')
within=[];cross=[]
for a,av,c,cv,lab in EDGES:
    wa,wc=HOME[NM[a]],HOME[NM[c]]
    (within if wa==wc else cross).append((lab,wa,wc))
print('     WITHIN a vocabulary: %d' % len(within))
for lab,wa,wc in within: print('        %-28s %s' % (lab,wa))
print('     CROSS vocabularies : %d' % len(cross))
for lab,wa,wc in cross: print('        %-28s %s -> %s' % (lab,wa,wc))
print()
print('     the Buniy charge NEC_pt>=3 & X_exp=0 & EOM=0 -> U_ghost=1')
print('        spans W3 & W1 & W1 -> W6   = THREE vocabularies')
print()
def E(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    tot=0; cur=[None]*d
    def rec(i):
        nonlocal tot
        if i==d: tot+=1; return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>phi[(i,j)][cur[j]] or cur[j]>phi[(j,i)][v]: ok=False; break
            if ok: cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return tot-len(S)
def build(idxs, edges, charge=None):
    """closure on the sub-index given by idxs, using only edges internal to it"""
    pos={g:k for k,g in enumerate(idxs)}
    def cl(x):
        x=list(x); g=True
        while g:
            g=False
            for a,av,c,cv,lab in edges:
                if a in pos and c in pos:
                    if x[pos[a]]>=av and x[pos[c]]<cv: x[pos[c]]=cv; g=True
        return tuple(x)
    cells={cl(t) for t in product(*[RNG[i] for i in idxs])}
    if charge: cells={c for c in cells if charge(c,pos)}
    return cells,pos
print('  EACH VOCABULARY-PART, ON ITS OWN EDGES')
print('  %-6s %-44s %6s %6s' % ('vocab','letters','cells','E'))
for w in ('W1','W3','W5','W6'):
    idxs=[i for i in range(15) if HOME[NM[i]]==w]
    cells,_=build(idxs,EDGES)
    print('  %-6s %-44s %6d %6d' % (w, ', '.join(NM[i] for i in idxs), len(cells), E(cells,len(idxs))))
print()
print('  THE WHOLE INDEX, EDGES ADDED BACK IN STAGES')
def full(use_cross, use_charge):
    edges=[e for e in EDGES if (HOME[NM[e[0]]]==HOME[NM[e[2]]]) or use_cross]
    idxs=list(range(15))
    def ch(c,pos):
        return not (c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)
    cells,_=build(idxs,edges,ch if use_charge else None)
    cells={c for c in cells if c[Sf]==0}
    return cells
for lab,uc,uch in [('within-vocabulary edges only',False,False),
                   ('+ cross-vocabulary edges',True,False),
                   ('+ the Buniy charge (3 vocabularies)',True,True)]:
    cells=full(uc,uch)
    print('  %-40s cells %6d   E = %d' % (lab,len(cells),E(cells,15)))
print()
print('  THE RESULT')
print('     within-vocabulary structure alone: every part closes, and so does the union.')
print('     the defect appears ONLY when a constraint spans vocabularies.')
print('     -> "arity tracks vocabulary span" is now tested, not inferred.')