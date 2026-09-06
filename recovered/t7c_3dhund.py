"""t7c_3dhund.py -- s25 item (3): 3d SO/Hund column. zeta_3d from t7c_so.zeta (SR-pol TS potential, half hole); F^k from the same 3d orbital;
Hund-II stab by exact CI over all-parallel-spin d determinants (t7c_mult.ci with L=2); Lande level term A=+-zeta/(2S). No constant, no measured input.
usage: python3 t7c_3dhund.py Z ... ; appends t7c_3dhund.jsonl"""
import sys, json, itertools, numpy as np, warnings; warnings.filterwarnings("ignore")
from sympy.physics.wigner import gaunt
from t5_scf import ground_occ, minus
from t7c_pol import scf_pol_sr
from t7c_kernel import numerov_wf_sr, C0
import t7c_mult as M
L=2; MS=list(range(-L,L+1)); M.L=L; M.MS=MS
M.G={k:{(a,b):float(gaunt(L,k,L,-a,a-b,b))*(-1)**a for a in MS for b in MS if abs(a-b)<=k} for k in (0,2,4)}
def V2(a,b,c,d,F):
    if a+b!=c+d: return 0.0
    return sum(F[k]*4*np.pi/(2*k+1)*M.G[k].get((a,c),0.0)*M.G[k].get((d,b),0.0) for k in (2,4) if abs(a-c)<=k)
M.V2=V2
def stab(nd,F):   # nd = number of d electrons; all-parallel manifold: electrons if nd<=5 else holes
    k=nd if nd<=5 else 10-nd
    return M.ci(k,F) if k>=2 else 0.0
def so(L_,S,nd,z):
    if L_==0 or S==0 or nd in (0,5,10): return 0.0
    A=z/(2*S)*(1 if nd<5 else -1); J=abs(L_-S) if nd<5 else L_+S
    return 0.5*A*(J*(J+1)-L_*(L_+1)-S*(S+1))
# (el, nd_neutral, (L,S) neutral, nd_ion, (L,S) ion) -- 3d-hole channel, ground terms of those configurations
ROWS={21:('Sc',1,(2,.5),0,(0,0)),22:('Ti',2,(3,1),1,(2,.5)),24:('Cr',5,(0,3),4,(2,2.5)),26:('Fe',6,(2,2),5,(0,2.5)),28:('Ni',8,(3,1),7,(3,1.5)),29:('Cu',10,(0,.5),9,(2,1))}
for Z in map(int,sys.argv[1:]):
    el,nn,(Ln,Sn),ni,(Li,Si)=ROWS[Z]; occ=minus(ground_occ(Z),3,2,0.5)
    probe,Es,h=scf_pol_sr(Z,1,occ=occ,c=C0)
    cells={nm:c.cell_contents for nm,c in zip(probe.__code__.co_freevars,probe.__closure__)}; Vf=cells['Vf']
    occd={(a,b):k for a,b,k in occ}; s="d" if occd.get((3,2),0)>=5 else "u"
    rr,drr,u,E,nd=numerov_wf_sr(Vf[s][0],2,3,1.0,Z,C0,Vp=Vf[s][1],Vpp=Vf[s][2]); u=u/np.sqrt(np.sum(u*u*drr))
    z=float((1.0/C0**2)/2*np.sum(u*u*Vf[s][1](rr)/rr*drr)); F=M.Fk(u,rr,drr)
    sn,si=stab(nn,F),stab(ni,F); son,soi=so(Ln,Sn,nn,z),so(Li,Si,ni,z)
    col=(sn+son)-(si+soi); col_qavg=(sn+son)-(0.0+soi)
    row=dict(Z=Z,el=el,zeta_3d=round(z,5),F2=round(F[2],4),F4=round(F[4],4),stab_n=round(sn,4),stab_i=round(si,4),so_n=round(son,5),so_i=round(soi,5),
             col=round(col,4),col_ion_avg=round(col_qavg,4),it=len(h))
    print(row,flush=True); open('t7c_3dhund.jsonl','a').write(json.dumps(row)+'\n')