import numpy as np, sys, os, json
from t7c_corrz import scf_sic_corr
from t5_scf import ground_occ, minus
import corr_ring as CR, corr_sosex as CS
SH={39:('Y','4d'),57:('La','5d'),21:('Sc','3d')}
for Z in map(int,sys.argv[1:]):
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0)
    Es,h,s=scf_sic_corr(Z,1,occ=hole,entrant=(n,l),mode="all",corr="S"); L=scf_sic_corr.last; r,dr=L['r'],L['dr']
    nsig={'u':np.zeros_like(r),'d':np.zeros_like(r)}; nent=None
    for c in L['chans']:
        nn,ll,k,ss,f,tag=c; nsig[ss]+=k*L['dens'][c]
        if tag=='ent': nent=L['dens'][c]
    w=4*np.pi*r*r; nu,nd=nsig['u']/w,nsig['d']/w; ntot=nu+nd
    dloc=float(np.sum(nent*dr*(CS.eps_S(nu,nd)-CR.eps_R(nu,nd))))            # entrant-weighted local S-R on the TOTAL density
    ne=nent/w; dsic=float(np.sum(nent*dr*(CS.eps_S(ne,0*ne)-CR.eps_R(ne,0*ne))))  # same on the one-orbital (zeta=1) density: what SIC subtracts
    # potential-level: entrant expectation of v_S - v_R (spin of entrant)
    vSu,vSd=CS.v_S(nu,nd); vRu,vRd=CR.v_R(nu,nd); dv=float(np.sum(nent*dr*(vSu-vRu)))
    vSe,_=CS.v_S(ne,0*ne); vRe,_=CR.v_R(ne,0*ne); dvs=float(np.sum(nent*dr*(vSe-vRe)))
    print(dict(Z=Z,el=el,dloc_eps=round(dloc,5),dloc_eps_oneorb=round(dsic,5),net_eps=round(dloc-dsic,5),dv_tot=round(dv,5),dv_oneorb=round(dvs,5),net_v=round(dv-dvs,5)))