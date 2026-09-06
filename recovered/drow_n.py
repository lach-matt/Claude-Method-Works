"""drow_n.py -- s30 Route N (PREDICTION-DROW-SESSION-30). Non-adiabatic second-order entrant-core correlation, dipole (k=1) direct term,
in the ion HFS local potential of the chain (corepol.orbitals). Basis = box eigenstates of h_l on the log mesh (symmetric tridiagonal, phi = r g),
same discretisation as corepol.sternheimer. E2 = -(1/3) sum_i N_i sum_{a,b} f_ia f_eb R1(ie;ab)^2 / (eps_a+eps_b-eps_i-eps_e).
a excludes ion-occupied shells of l_a (entrant shell allowed: empty in the ion); b excludes ion-occupied shells of l_b. Box cut eps < ECUT (3 Ha) stated.
Adiabatic gate: drop (eps_b-eps_e), close over b -> must reproduce corepol E_A_closed (Sternheimer, exact a-sum) on Cs within 10 %.
usage: python3 drow_n.py Z [Z ...]  -> drow_n.jsonl (done-set)."""
import sys,os,json,numpy as np,time
from scipy.linalg import eigh_tridiagonal
from t5_scf import ground_occ,minus
import corepol as CP
SH=CP.SH; ECUT=3.0; LMAX=4
def box(Vr,r,h,l):
    d=(1.0/h**2+0.125+l*(l+1)/2.0+Vr*r*r)/(r*r); e=(-0.5/h**2)/(r[:-1]*r[1:])
    w,phi=eigh_tridiagonal(d,e); U=(phi/np.sqrt(h*r)[:,None]).T   # rows = states, u normalised: int u^2 dr = 1
    return w,U
def Y1(rho,r,dr):
    """Y1[rho](r) = r^-2 int_0^r rho r' dr' + r int_r^inf rho r'^-2 dr'  (rows of rho)."""
    a=np.cumsum(rho*(r*dr),axis=1); b=np.cumsum((rho*(dr/(r*r)))[:,::-1],axis=1)[:,::-1]
    return a/(r*r)+b*r
def fac(l,lp): return max(l,lp)/(2*l+1)
def run(Z):
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); occ=ground_occ(Z); ion=minus(occ,n,l,1.0)
    x,r,h,dr=CP.mesh(Z); Vn,Pn=CP.orbitals(Z,occ,1); ue=Pn[(n,l)][0]
    Vi,Pi=CP.orbitals(Z,ion,1); Vr=Vi(r)
    amax=max(a for a,b,q in ion if b==0); ns={(a,b) for a,b,q in ion if b==0 and a==amax and a>n}
    nocc={}                                                             # ion-occupied shells per l -> count (lowest box states excluded)
    for a,b,q in ion: nocc[b]=nocc.get(b,0)+1
    B={}                                                                # box per l: (eps, U) with occupied removed, and full for gate
    for lb in range(LMAX+1):
        w,U=box(Vr,r,h,lb); k=nocc.get(lb,0); B[lb]=dict(full=(w,U),free=(w[k:],U[k:]),occ_e=w[:k])
    # entrant energy in the ion potential
    d=(1.0/h**2+0.125+l*(l+1)/2.0+Vr*r*r)/(r*r); e=(-0.5/h**2)/(r[:-1]*r[1:]); phi=ue*np.sqrt(h*r)
    eps_e=float(np.sum(d*phi*phi)+2*np.sum(e*phi[:-1]*phi[1:]))
    # eigenvalue check: box bound states vs numerov ion orbitals
    dev=max(abs(B[b]['occ_e'][ [aa for aa,bb,qq in ion if bb==b].index(a) if False else 0 ]-0) for a,b,q in ion) if False else 0.0
    chk=[]
    for a,b,q in ion:
        idx=sorted(aa for aa,bb,qq in ion if bb==b).index(a); chk.append(abs(B[b]['occ_e'][idx]-Pi[(a,b)][1]))
    dev=float(max(chk))
    out=dict(Z=Z,el=el,sh=sh,eps_e_ion=round(eps_e,5),eps_e_neu=round(float(Pn[(n,l)][1]),5),box_dev_max=round(dev,5),ecut=ECUT,npts=len(r))
    tot={'closed':0.0,'ns':0.0}; ad_full={'closed':0.0,'ns':0.0}; ad_cut={'closed':0.0,'ns':0.0}; nb={}
    ue2=ue*ue
    for (ni,li,Ni) in ion:
        ui,ei,_=Pi[(ni,li)]; grp='ns' if (ni,li) in ns else 'closed'
        for la in (li-1,li+1):
            if la<0 or la>LMAX: continue
            fia=fac(li,la)
            for tag,(wa,Ua) in (('full',B[la]['full']),('cut',None)):
                pass
            wa,Ua=B[la]['free']; sel=wa<ECUT
            rho=ui[None,:]*Ua; Ya=Y1(rho,r,dr)                    # all free a (for the full adiabatic closure)
            Da=wa-ei
            # adiabatic closure over b (sum_lb f_eb = 1): sum_a (1/Da) int ue^2 Ya^2 dr
            I=(Ya*Ya)@(ue2*dr)
            ad_full[grp]+=-(1.0/3.0)*Ni*fia*float(np.sum(I/Da)); ad_cut[grp]+=-(1.0/3.0)*Ni*fia*float(np.sum((I/Da)[sel]))
            Ya=Ya[sel]; Da=Da[sel]
            for lb in (l-1,l+1):
                if lb<0 or lb>LMAX: continue
                feb=fac(l,lb); wb,Ub=B[lb]['free']; sb=wb<ECUT; wb=wb[sb]; Ub=Ub[sb]; nb[lb]=int(sb.sum())
                W=(ue[None,:]*Ub)*dr[None,:]; R1=Ya@W.T                                     # (n_a x n_b)
                D=Da[:,None]+(wb-eps_e)[None,:]
                tot[grp]+=-(1.0/3.0)*Ni*fia*feb*float(np.sum(R1*R1/D))
    out.update(E2_closed=round(tot['closed'],5),E2_ns=round(tot['ns'],5),adiab_closed_full=round(ad_full['closed'],5),adiab_closed_cut=round(ad_cut['closed'],5),
               adiab_ns_full=round(ad_full['ns'],5),n_b=nb,ns_shells=sorted(ns))
    return out
if __name__=="__main__":
    OUT="drow_n.jsonl"; done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
    for Z in map(int,sys.argv[1:]):
        if Z in done: print("SKIP",Z); continue
        t0=time.time(); o=run(Z); o['sec']=int(time.time()-t0)
        open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)
