#!/usr/bin/env python3
"""derive_P2.py -- Session 7, route (ii): penalty as an exchange DIFFERENCE.
Entrant into half-full nl (forced antiparallel): exchange with the 2l+1 shell electrons = 0.
Entrant into runner-up n'l' (Hund, parallel): exchange with them = (2l+1) K(nl,n'l'),
   K = sum_k C_k G^k(nl,n'l'), C_k = (l k l'; 0 0 0)^2.
Hypothetical parallel placement into nl would give (2l+1) J_H(nl).
P_ii = (2l+1) [ J_H(nl,nl) - K(nl,n'l') ]   -- exchange lost in nl MINUS exchange gained in n'l'.
Both radial functions from the same charge-1 TFD object at the pack-5 kernel's E. Nothing written."""
import json, numpy as np, tfd, warnings; warnings.filterwarnings("ignore")
from sympy.physics.wigner import wigner_3j
from derive_P import numerov_wf, slater_Fk, J_H
def Gk(r,dr,ua,ub,ks):
    w=ua*ub*dr; out={}
    for k in ks:
        A=np.cumsum(w*r**k)-0.5*w*r**k
        out[k]=2*np.sum(w*A/r**(k+1))
    return out
CLASS=[("Mn",25,3,2,4,0),("Fe",26,3,2,4,1),("Tc",43,4,2,5,0),("Ru",44,4,2,5,1),("Gd",64,4,3,5,2),
       ("Tb",65,4,3,5,2),("Os",76,5,2,6,1),("Cm",96,5,3,6,2),("Bk",97,5,3,6,2),("Hs",108,6,2,7,1)]
WIN={"3d":(0.0108,0.2978),"4d":(0.0262,0.2245),"4f":(0.0569,0.2180),"5d":(0.0,0.3766),"5f":(0.1250,0.2145),"6d":(0.0,0.3261)}
L="spdfg"; rows=[]
for el,Z,n,l,n2,l2 in CLASS:
    V,x0=tfd.potential(Z,1)
    r,dr,ua,Ea,_=numerov_wf(V,l,n,1.0,Z); r2,dr2,ub,Eb,_=numerov_wf(V,l2,n2,1.0,Z)
    ub=np.interp(r,r2,ub)  # meshes differ in rmax; interpolate runner-up onto entrant mesh
    ub/=np.sqrt(np.sum(ub*ub*dr))
    F=slater_Fk(r,dr,ua,(0,2,4) if l==2 else (0,2,4,6)); JH=J_H(l,F)
    ks=[k for k in range(abs(l-l2),l+l2+1) if (l+l2+k)%2==0]
    G=Gk(r,dr,ua,ub,ks); C={k:float(wigner_3j(l,k,l2,0,0,0)**2) for k in ks}
    K=sum(C[k]*G[k] for k in ks); Pi=(2*l+1)*JH; Pii=(2*l+1)*(JH-K)
    sh=f"{n}{L[l]}"; lo,hi=WIN[sh]; v=lambda P:"IN" if lo<P<hi else("ABOVE" if P>=hi else "BELOW")
    rows.append(dict(el=el,Z=Z,shell=sh,runner=f"{n2}{L[l2]}",E_nl=round(Ea,5),E_run=round(Eb,5),J_H=round(JH,5),
                     G={k:round(v_,5) for k,v_ in G.items()},C=C,K=round(K,5),P_i=round(Pi,4),P_ii=round(Pii,4),
                     P_ii_half=round(Pii/2,4),window=(lo,hi),verdict_i=v(Pi),verdict_ii=v(Pii),verdict_ii_half=v(Pii/2)))
    print(f"{el:3s} {sh}/{n2}{L[l2]}  J_H={JH:.4f} K={K:.4f}  "+" ".join(f"G{k}={G[k]:.4f}" for k in ks)+
          f"  P_i={Pi:.4f} {v(Pi)}  P_ii={Pii:.4f} {v(Pii)} ({Pii*27.211:.2f} eV)  ½P_ii={Pii/2:.4f} {v(Pii/2)}  win {lo}-{hi}",flush=True)
json.dump(rows,open("derive_P2.json","w"),indent=1)