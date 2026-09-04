"""t7c_so.py -- session 19 (bridge-18 s3(2), smallest scale): FIRST-ORDER spin-orbit level term on the SR-pol TS object.
zeta_nl = (alpha^2/2) <P| (1/r) dV/dr |P> on the converged self-consistent potential of the TS SCF (own channel), c=137.035999.
Level shifts: j=l+1/2: +zeta*l/2 ; j=l-1/2: -zeta*(l+1)/2. Predictions PL1/PL2 stated in chat before the run. No constant, no measured input.
usage: python3 t7c_so.py lr            (Lr I 7p vs 6d, TS on Lr core 102, tail 1)
       python3 t7c_so.py 5d 57 64 71   (neutral 5d TS, as t7c_pol rows)"""
import sys, json, numpy as np, warnings; warnings.filterwarnings("ignore")
from t5_scf import ground_occ, minus
from t7c_pol import scf_pol_sr
from t7c_kernel import numerov_wf_sr, C0
def zeta(Z,q,occ,n,l):
    probe,Es,h=scf_pol_sr(Z,q,occ=occ,c=C0)
    cells={nm:c.cell_contents for nm,c in zip(probe.__code__.co_freevars,probe.__closure__)}
    Vf=cells['Vf']; occd={(a,b):k for a,b,k in occ}; s="d" if occd.get((n,l),0)>=2*l+1 else "u"
    rr,drr,u,E,nd=numerov_wf_sr(Vf[s][0],l,n,1.0,Z,C0,Vp=Vf[s][1],Vpp=Vf[s][2]); u=u/np.sqrt(np.sum(u*u*drr))
    z=float((1.0/C0**2)/2*np.sum(u*u*Vf[s][1](rr)/rr*drr))
    return E,z,len(h)
out=[]
if sys.argv[1]=='lr':
    Z,N=103,102; g=ground_occ(N)
    E7p,zp,i1=zeta(Z,1,g+[(7,1,0.5)],7,1); E6d,zd,i2=zeta(Z,1,g+[(6,2,0.5)],6,2)
    d0=E7p-E6d; sh_p=-zp*1.0; sh_d=-zd*1.5; d1=d0+sh_p-sh_d
    row=dict(obj='LrI 7p-6d TS-SR-pol',E7p=round(E7p,5),E6d=round(E6d,5),zeta_7p=round(zp,5),zeta_6d=round(zd,5),shift_7p12=round(sh_p,5),shift_6d32=round(sh_d,5),d0=round(d0,5),d1=round(d1,5),it=[i1,i2])
    print(row); out.append(row)
else:
    T5={json.loads(l)['Z']:json.loads(l) for l in open('t5.jsonl')}; P={json.loads(l)['Z']:json.loads(l) for l in open('t7c_pol.jsonl')}
    for Z in map(int,sys.argv[2:]):
        occ=minus(ground_occ(Z),5,2,0.5); E,z,it=zeta(Z,1,occ,5,2); sh=-1.5*z; m=T5[Z]['meas']; e0=P[Z]['t7c_pol']; e1=e0+sh
        row=dict(Z=Z,el=T5[Z]['el'],E_ts=round(E,4),t7c_pol=e0,zeta_5d=round(z,5),shift_5d32=round(sh,5),corr=round(e1,4),meas=m,dev0=P[Z]['dev_pct'],dev1=round(100*(e1-m)/abs(m),1),it=it)
        print(row,flush=True); out.append(row)
for r in out: open('t7c_so.jsonl','a').write(json.dumps(r)+'\n')
