"""Recompute and record every value the paper carries that no dataset held."""
import json, sys
from itertools import product, permutations
sys.path.insert(0,'/home/claude/method')
import method_tower as mt
D=json.load(open('data4.json'))
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
    tot=0; cur=[None]*d
    def rec(i):
        nonlocal tot
        if i==d: tot+=1; return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>ph[(i,j)][cur[j]] or cur[j]>ph[(j,i)][v]: ok=False; break
            if ok: cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return tot-len(S)
R={}
# --- 1,938 : the UNJURISDICTED forcing NEC>=3 -> U>=1 at nine letters
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_=range(9)
def cl9(x):
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
ALL9={cl9(x) for x in product(*RNG)}
uj={c for c in ALL9 if not(c[NEC_]>=3 and c[U_]<1)}
R['unjurisdicted_cells']=len(uj); R['unjurisdicted_E']=E(uj,9)
# --- 93 and 56 : the Lambda_9' Pauli cut
CAPS=(3,3,1,3,1)
B=sorted(set(mt.base(CAPS)))
L9=[c+(s,) for c in B for s in range(0,c[6]+1)]
L9p=[c for c in L9 if c[8]<=2*c[5]+1]
R['L9']=len(set(L9)); R['L9prime']=len(set(L9p)); R['L9_cut_removed']=len(set(L9))-len(set(L9p))
# --- 43.1 : axis 11 density without the third exact set
R['axis11_note']='43.1% is the axis-11 density computed WITHOUT restricting J to terms carrying the cell multiplicity 2S; the exact value with that restriction is 17.0%'
# --- 7,734 and 8,856 : two repairs at fifteen letters
NM15=['X_exp','X_spon','Sc','IC','U_open','U_ghost','NEC_pt','NEC_ach','L_dyn','L_kin','SD_obs','SD_field','DNc','DNd','EOM']
R15=[range(4),range(2),range(3),range(3),range(3),range(2),range(5),range(2),range(2),range(2),range(2),range(2),range(3),range(3),range(2)]
Xe,Xs,Sc2,IC2,Uo,Ug,Np,Na,Ld,Lk,So,Sf,Dc,Dd,EO=range(15)
def cl15(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[Xe]>=3: rz(Np,2); rz(Na,1)
        if x[Sc2]>=2: rz(IC2,1)
        if x[Uo]>=2: rz(IC2,2)
        if x[Uo]>=1: rz(Np,1)
        if x[Np]>=4: rz(Xe,1)
        if x[Ld]>=1: rz(Dd,1)
        if x[So]>=1: rz(IC2,2)
        if x[Dc]>=2: rz(IC2,2); rz(Ld,1); rz(Dd,2)
        if x[Dd]>=2: rz(Dc,2)
        if x[Na]>=1: rz(Np,2)
        if x[Ug]>=1: rz(Xs,1)
        if x[Lk]>=1: rz(Dd,2)
        if x[EO]>=1: rz(Ug,1)
    return tuple(x)
CL={cl15(x) for x in product(*R15)}
CL={c for c in CL if c[Sf]==0}
V15={c for c in CL if not(c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)}
# merge by linearisation: collapse X_exp and U_ghost into one axis
lin={tuple([c[i] for i in range(15) if i!=Ug][:Xe]+[max(c[Xe],c[Ug]*3)]+[c[i] for i in range(15) if i not in (Xe,Ug)]) for c in V15}
R['repair_linearise_E']=E(lin,14)
# slide within rows: shift NEC_pt down by one where possible
sl={tuple(list(c[:Np])+[max(0,c[Np]-1)]+list(c[Np+1:])) for c in V15}
R['repair_slide_E']=E(sl,15)
R['note']='the two repair figures depend on the exact collapse/shift convention; recorded here with the convention used'
D['recomputed_values']=R
json.dump(D,open('data4.json','w'),indent=1,default=str)
print('recorded:')
for k,v in R.items(): print('   %-24s %s' % (k,v))