"""corepol.py -- s29 mechanism A: adiabatic, cutoff-free dipole core polarisation of the entrant (PREDICTION-COREPOL-SESSION-29). No constant."""
import sys,os,json,numpy as np
from scipy.linalg import solve_banded
from t5_scf import scf_occ,ground_occ,minus
from hfs import numerov_wf
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
def mesh(Z,npts=4000):
    x=np.linspace(np.log(1e-6/Z),np.log(300.0),npts); r=np.exp(x); h=x[1]-x[0]; return x,r,h,r*h
def orbitals(Z,occ,qtail,Vf=None):
    x,r,h,dr=mesh(Z)
    if Vf is None: Vf,Es,_,_=scf_occ(Z,occ,qtail)
    P={}
    for n,l,k in occ:
        rr,drr,u,E,nd=numerov_wf(Vf,l,n,1.0,Z); ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); P[(n,l)]=(ui,E,k)
    return Vf,P
def sternheimer(x,r,h,V,eps,lp,rhs):
    """solve (-1/2 d2/dr2 + lp(lp+1)/2r^2 + V - eps) y = rhs on the log mesh; y=0 at ends. y=r^{1/2} g removes first-derivative term."""
    # d2y/dr2 = r^{-3/2}( g'' - g/4 ) with ' = d/dx
    g_rhs=rhs*r**1.5
    diag=(1.0/h**2)+0.125+ (lp*(lp+1)/2.0+ (V-eps)*r*r)      # from: -1/2 r^{-2}(g''-g/4)+... multiply eq by r^2: -1/2 g''+ g/8 + [lp(lp+1)/2 + (V-eps) r^2] g = r^2 rhs r^{-1/2}=rhs r^{1.5}
    off=-0.5/h**2*np.ones(len(r))
    ab=np.zeros((3,len(r))); ab[0,1:]=off[:-1]; ab[1]=diag; ab[2,:-1]=off[1:]
    g=solve_banded((1,1),ab,g_rhs); return g/np.sqrt(r)
def E2_of_re(Z,occ_core,P,V,x,r,h,dr,re_list):
    """E2(r_e) for a unit point charge at r_e, closed-core orbitals in P (dict (n,l)->(u,eps,N))."""
    Vr=V(r); out=np.zeros(len(re_list))
    occ_by_l={}
    for (n,l),(u,e,N) in P.items(): occ_by_l.setdefault(l,[]).append(u)
    for k,re in enumerate(re_list):
        v=np.where(r<re,r/re**2,re/r**2); s=0.0
        for (n,l),(u,e,N) in P.items():
            for lp in (l-1,l+1):
                if lp<0: continue
                fac=max(l,lp)/(2*l+1)
                rhs=v*u
                for uo in occ_by_l.get(lp,[]): rhs=rhs-uo*np.sum(uo*rhs*dr)
                y=sternheimer(x,r,h,Vr,e,lp,rhs)
                for uo in occ_by_l.get(lp,[]): y=y-uo*np.sum(uo*y*dr)
                s+=N*fac*np.sum(u*v*y*dr)
        out[k]=-s/3.0
    return out
def alpha(Z,occ,qtail,Vf=None):
    x,r,h,dr=mesh(Z); Vf,P=orbitals(Z,occ,qtail,Vf); Vr=Vf(r); s=0.0
    occ_by_l={}
    for (n,l),(u,e,N) in P.items(): occ_by_l.setdefault(l,[]).append(u)
    for (n,l),(u,e,N) in P.items():
        for lp in (l-1,l+1):
            if lp<0: continue
            rhs=r*u
            for uo in occ_by_l.get(lp,[]): rhs=rhs-uo*np.sum(uo*rhs*dr)
            y=sternheimer(x,r,h,Vr,e,lp,rhs)
            for uo in occ_by_l.get(lp,[]): y=y-uo*np.sum(uo*y*dr)
            s+=N*max(l,lp)/(2*l+1)*np.sum(u*r*y*dr)
    return 2.0*s/3.0,Vf,P
if __name__=="__main__":
    if sys.argv[1]=="gate":
        x,r,h,dr=mesh(1); Vh=lambda rr:-1.0/np.asarray(rr,float); a,_,_=alpha(1,[(1,0,1)],1,Vf=Vh); print(f"H 1s alpha {a:.4f} (exact 4.5)")
        a,_,_=alpha(2,[(1,0,2)],1); print(f"He HFS alpha {a:.4f} (exact 1.383)"); sys.exit()
    OUT="corepol.jsonl"; done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
    for Z in map(int,sys.argv[1:]):
        if Z in done: print("SKIP",Z); continue
        el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); occ=ground_occ(Z); ion=minus(occ,n,l,1.0)
        x,r,h,dr=mesh(Z); Vf,P=orbitals(Z,occ,1)      # neutral HFS potential + orbitals (entrant P_e taken from here)
        Pe=P[(n,l)][0]
        ns=[(a,b,q) for a,b,q in ion if b==0 and a==n]  # the ns2 pair (n = entrant n for d rows; none for Cs 6s)
        closed=[t for t in ion if t not in ns]
        Vi,Pi=orbitals(Z,ion,1)                            # ion HFS potential + orbitals for the response
        Pc={k:v for k,v in Pi.items() if k in {(a,b) for a,b,q in closed}}; Pn={k:v for k,v in Pi.items() if k in {(a,b) for a,b,q in ns}}
        a_c,_,_=alpha(Z,closed,1,Vf=Vi)
        # E_A: integrate over entrant density on a coarse r_e ladder (Simpson in x), E2 evaluated by Sternheimer at each r_e
        sel=np.arange(0,len(r),40); re=r[sel]; E2c=E2_of_re(Z,closed,Pc,Vi,x,r,h,dr,re)
        E2n=E2_of_re(Z,ns,Pn,Vi,x,r,h,dr,re) if Pn else np.zeros(len(re))
        w=Pe**2*dr; wsel=np.interp(r,re,E2c); EA=float(np.sum(w*wsel)); EAn=float(np.sum(w*np.interp(r,re,E2n)))
        alim=-2*E2c[-1]*re[-1]**4
        o=dict(Z=Z,el=el,sh=sh,alpha_closed=round(a_c,3),alpha_from_E2_tail=round(float(alim),3),E_A_closed=round(EA,5),A_ns=round(EAn,5),n_re=len(re))
        open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)