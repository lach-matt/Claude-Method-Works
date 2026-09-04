#!/usr/bin/env python3
"""class_hfs.py -- Session 8 T1'. The ten class species under the self-consistent orbital-density kernel
(hfs.scf), charge 1. Per species: SCF; then in the FINAL potential the candidate eigenvalues (step-3
candidate list), F^k of the entrant, G^k/K with the runner-up, P_i/P_ii/P_iii; windows REBUILT from the new
gaps (P4). Resumable: class_hfs.jsonl."""
import json, os, sys, numpy as np, tfd, warnings; warnings.filterwarnings("ignore")
from sympy.physics.wigner import wigner_3j
from hfs import scf, numerov_wf, L
from derive_P import slater_Fk, J_H
from derive_P2 import Gk
CLASS=[("Mn",25,3,2,4,0),("Fe",26,3,2,4,1),("Tc",43,4,2,5,0),("Ru",44,4,2,5,1),("Gd",64,4,3,5,2),
       ("Tb",65,4,3,5,2),("Os",76,5,2,6,1),("Cm",96,5,3,6,2),("Bk",97,5,3,6,2),("Hs",108,6,2,7,1)]
DONOR={"Ru":(5,0),"Tb":(5,2),"Bk":(6,2)}
cand={}
for line in open("../step3B_fixed.jsonl"):
    r=json.loads(line); cand[r['el']]=(r['cand'] if 'cand' in r else list(r['EB'].keys()), r['obs'])
done={}
if os.path.exists("class_hfs.jsonl"):
    for line in open("class_hfs.jsonl"): r=json.loads(line); done[r['el']]=r
for el,Z,n,l,n2,l2 in CLASS:
    if el in done: continue
    Vf,Es,hist,_=scf(Z,1)
    cs,obs=cand[el]; EB={}
    for c in cs:
        nn=int(c[0]); ll=L.index(c[1]); EB[c]=round(float(numerov_wf(Vf,ll,nn,1.0,Z)[3]),5)
    sh=f"{n}{L[l]}"; ru=f"{n2}{L[l2]}"
    r,dr,ua,Ea,_=numerov_wf(Vf,l,n,1.0,Z); r2,dr2,ub,Eb,_=numerov_wf(Vf,l2,n2,1.0,Z)
    ub=np.interp(r,r2,ub,left=0,right=0); ub/=np.sqrt(np.sum(ub*ub*dr))
    F=slater_Fk(r,dr,ua,(0,2,4) if l==2 else (0,2,4,6)); JH=J_H(l,F)
    ks=[k for k in range(abs(l-l2),l+l2+1) if (l+l2+k)%2==0]
    Gd=Gk(r,dr,ua,ub,ks); K=sum(float(wigner_3j(l,k,l2,0,0,0)**2)*Gd[k] for k in ks)
    Pi=(2*l+1)*JH; Pii=(2*l+1)*(JH-K); Piii=Pii; JH2=0.0
    if el in DONOR:
        nd_,ld_=DONOR[el]
        if ld_==2:
            rr,drr,ud,_,_=numerov_wf(Vf,ld_,nd_,1.0,Z); JH2=J_H(2,slater_Fk(rr,drr,ud,(0,2,4)))
        Piii=Pii-(JH+JH2)/2
    gap=min(v for k,v in EB.items() if k!=sh)-EB[sh]
    argmin=min(EB,key=EB.get)
    row=dict(el=el,Z=Z,shell=sh,runner=ru,obs=obs,iters=len(hist),dV=hist[-1],EB=EB,argminB=argmin,gap=round(gap,4),
             J_H=round(JH,5),K=round(K,5),J_H2=round(JH2,5),P_i=round(Pi,4),P_ii=round(Pii,4),P_iii=round(Piii,4))
    open("class_hfs.jsonl","a").write(json.dumps(row)+"\n")
    print(f"{el:3s} it{len(hist):2d} EB {EB} argmin {argmin} obs {obs} gap {gap:.4f}  J_H {JH:.4f} K {K:.4f}  P_i {Pi:.4f} P_ii {Pii:.4f} P_iii {Piii:.4f}",flush=True)