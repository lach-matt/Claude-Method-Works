#!/usr/bin/env python3
"""derive_P3.py -- Session 7, donor-step refinement of route (ii). STATED AFTER Tb WAS SEEN TO FAIL (flag).
Three of the ten class steps are DONOR steps (ground.py): Ru 4d5 5s2 -> 4d7 5s ; Tb 4f7 5d 6s2 -> 4f9 6s2 ;
Bk 5f7 6d 7s2 -> 5f9 7s2. Two electrons enter the half-full shell (entrant + the moved runner-up electron).
Exchange bookkeeping per entering electron, averaged over the two (Hund):
  1st paired electron: loses (2l+1)J_H, forgoes (2l+1)K in n'l'
  2nd paired electron: parallel to the 1st -> loses (2l+1)J_H - J_H ; alternative n'l'^2 forgoes (2l+1)K + J_H(n'l')
  P_iii = (2l+1)(J_H - K) - [J_H(nl) + J_H(n'l')]/2      (single-entrant steps: P_iii = P_ii)
J_H(n'l') for s = 0; for d = (F2+F4)/14 of the runner-up shell in the same object."""
import json, numpy as np, tfd, warnings; warnings.filterwarnings("ignore")
from derive_P import numerov_wf, slater_Fk, J_H
rows=json.load(open("derive_P2.json")); DONOR={"Ru":(5,0),"Tb":(5,2),"Bk":(6,2)}
WIN={"3d":(0.0108,0.2978),"4d":(0.0262,0.2245),"4f":(0.0569,0.2180),"5d":(0.0,0.3766),"5f":(0.1250,0.2145),"6d":(0.0,0.3261)}
out=[]
for r in rows:
    el=r['el']; P=r['P_ii']; note=""
    if el in DONOR:
        n2,l2=DONOR[el]; JH2=0.0
        if l2==2:
            V,x0=tfd.potential(r['Z'],1); rr,dr,u,E,_=numerov_wf(V,l2,n2,1.0,r['Z'])
            F=slater_Fk(rr,dr,u,(0,2,4)); JH2=J_H(2,F)
        P=r['P_ii']-(r['J_H']+JH2)/2; note=f"donor: J_H(nl)={r['J_H']:.4f} J_H(n'l')={JH2:.4f}"
    lo,hi=WIN[r['shell']]; v="IN" if lo<P<hi else("ABOVE" if P>=hi else "BELOW")
    out.append(dict(el=el,shell=r['shell'],P_ii=r['P_ii'],P_iii=round(P,4),verdict=v,note=note))
    print(f"{el:3s} {r['shell']}  P_ii={r['P_ii']:.4f}  P_iii={P:.4f}  win {lo}-{hi}  {v}  {note}")
json.dump(out,open("derive_P3.json","w"),indent=1)