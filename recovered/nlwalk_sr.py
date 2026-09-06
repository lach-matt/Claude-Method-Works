"""nlwalk_sr.py -- s37 Stage 3 of the n+l walk: nlwalk.py energetics with the KH scalar-relativistic kernel (t7c_kernel.numerov_wf_sr) in BOTH the t5 SCF and
the orbital build; SIC in the ENERGY only (as Stage 1), computed in TWO conventions on ONE orbital set: per-electron on P^2 (Stage 1) and f_orb
(spin channel f = k_s/(2l+1); SIC = (2l+1)[E_H+E_x+E_c](f P^2); core shells k/2 per spin, entrant shell all up -- the xseam spin convention).
D_rel_fo = D_rel + (SIC_pe - SIC_fo)(neu+c) - (SIC_pe - SIC_fo)(ion). C=1e6 reproduces Stage 1 (build gate). usage: [CLIGHT=1e6] python3 nlwalk_sr.py Z ...
appends nlwalk_sr.jsonl (key Z,tag). No constant; no measured input; channels enumerated as nlwalk.py."""
import sys,os,json,time,numpy as np
CL=float(os.environ.get("CLIGHT","0")) or None
sys.argv,_a=[sys.argv[0]],sys.argv; exec(open('xseam_relax.py').read().split('for Z in map')[0]); sys.argv=_a
import ground as G, tfd
from t7c_kernel import numerov_wf_sr, C0
CC=CL if CL else C0
def nw(Vf,l,n,zeta,Z): return numerov_wf_sr(Vf,l,n,zeta,Z,c=CC)
def scf_occ_sr(Z, occ, qtail, npts=4000, beta=0.3, tol=2e-5, maxit=80):
    N=sum(k for _,_,k in occ)
    x=np.linspace(np.log(1e-6/Z),np.log(300.0),npts); r=np.exp(x); h=x[1]-x[0]; dr=r*h
    Vt,_=tfd.potential(Z,max(int(round(Z-N)),1)); Vg=Vt(r); Vf=lambda rr,Vg=Vg: np.interp(np.log(np.asarray(rr,float)),x,Vg)
    for it in range(maxit):
        n_r=np.zeros(npts); Es={}
        for n,l,k in occ:
            rr,drr,u,E,nd=nw(Vf,l,n,1.0,Z)
            if nd!=n-l-1: raise RuntimeError(f"Z={Z} {n}{'spdf'[l]} nodes {nd}")
            ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); n_r+=k*ui*ui; Es[(n,l)]=E
        cum=np.cumsum(n_r*dr)-0.5*n_r*dr; outer=np.cumsum((n_r/r*dr)[::-1])[::-1]-0.5*n_r/r*dr; VH=cum/r+outer
        rho=n_r/(4*np.pi*r*r); Vx=-(3.0*rho/np.pi)**(1.0/3.0)
        Vn=np.minimum(-Z/r+VH+Vx,-qtail/r); d=float(np.max(np.abs(r*(Vn-Vg))[r<60]))
        Vg=(1-beta)*Vg+beta*Vn; Vf=lambda rr,Vg=Vg: np.interp(np.log(np.asarray(rr,float)),x,Vg)
        if d<tol: break
    return Vf,Es,None,it+1
def orbs_sr(Z,occ,qtail):
    Vf,Es,Et,it=scf_occ_sr(Z,occ,qtail)
    x=np.linspace(np.log(1e-6/Z),np.log(300.0),4000); r=np.exp(x); h=x[1]-x[0]; dr=r*h; P={}; T={}; V=Vf(r)
    for n,l,k in occ:
        rr,drr,u,E,nd=nw(Vf,l,n,1.0,Z); ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); P[(n,l)]=ui
        T[(n,l)]=float(E-np.sum(ui*ui*V*dr))
    return r,dr,P,it,T,Vf
def sic_shift(occ,P,ent,r,w,dr):
    """SIC_pe - SIC_fo (>0 when f_orb removes SIC). Adding it to E_pe gives E_fo."""
    tot=0.0
    for n,l,k in occ:
        p2=P[(n,l)]**2
        pe=k*(0.5*float(np.sum(p2*HF.hartree(p2,r,dr)*dr))+Ex(p2,0*p2,w,dr)+Ec(p2,0*p2,w,dr))
        chans=[k] if (n,l)==ent else [k/2,k/2]
        fo=0.0
        for ks in chans:
            if ks<=1e-9: continue
            f=ks/(2*l+1); q=f*p2
            fo+=(2*l+1)*(0.5*float(np.sum(q*HF.hartree(q,r,dr)*dr))+Ex(q,0*q,w,dr)+Ec(q,0*q,w,dr))
        tot+=pe-fo
    return float(tot)
EL={13:'Al',19:'K',20:'Ca',21:'Sc',31:'Ga',37:'Rb',38:'Sr',39:'Y',49:'In',55:'Cs',56:'Ba',57:'La',58:'Ce',64:'Gd',71:'Lu',72:'Hf',81:'Tl',87:'Fr',88:'Ra',89:'Ac',90:'Th',91:'Pa',92:'U',96:'Cm',103:'Lr',104:'Rf'}
def entrant(Z):
    a={(n,l):k for n,l,k in G.expand(Z)}; b={(n,l):k for n,l,k in G.expand(Z-1)}
    up=[nl for nl in a if a[nl]-b.get(nl,0)>1e-9]; assert len(up)==1,(Z,up); return up[0]
def channels(Z):
    N=max(n for n,l,k in G.expand(Z)); ch=[(N,0),(N,1),(N-1,2)]
    if N>=6: ch.append((N-2,3))
    return ch
OUT=os.environ.get("OUT",'nlwalk_sr.jsonl'); done={(d['Z'],d['tag']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
def add(occ,n,l,k):
    o=[list(t) for t in occ]; f=False
    for t in o:
        if t[0]==n and t[1]==l: t[2]+=k; f=True
    if not f: o.append([n,l,k])
    return [tuple(t) for t in o]
def tagof(c): return f"{c[0]}{'spdf'[c[1]]}"
for Z in map(int,_a[1:]):
    el=EL.get(Z,str(Z)); g=entrant(Z); occ0=ground_occ(Z); occ1=minus(occ0,g[0],g[1],1.0); occ1d={(n,l):k for n,l,k in occ1}
    r,dr,P0,it0,T0,Vf0=orbs_sr(Z,occ0,1); w=4*np.pi*r*r; V0=Vf0(r)
    r,dr,P1,it1,T1,_=orbs_sr(Z,occ1,2); E1r,_,_=e_tot(Z,occ1,P1,T1,g,r,w,dr); E1f,_,_=e_tot(Z,occ1,P0,T0,g,r,w,dr)
    S1r=sic_shift(occ1,P1,g,r,w,dr); S1f=sic_shift(occ1,P0,g,r,w,dr)
    for c in channels(Z):
        tag=tagof(c)
        if (Z,tag) in done: print("SKIP",Z,tag); continue
        if occ1d.get(c,0)>=2*(2*c[1]+1)-1e-9:
            o=dict(Z=Z,el=el,tag=tag,kind='chan',ent=tagof(g),full=True); open(OUT,'a').write(json.dumps(o)+'\n'); print(o); continue
        t0=time.time(); occc=add(occ1,c[0],c[1],1.0)
        try:
            Pf=dict(P0); Tf=dict(T0)
            if c not in Pf:
                rr,drr,u,E,nd=nw(Vf0,c[1],c[0],1.0,Z); ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); Pf[c]=ui; Tf[c]=float(E-np.sum(ui*ui*V0*dr))
            E0f,_,_=e_tot(Z,occc,Pf,Tf,c,r,w,dr); D_frz=E0f-E1f; Sf=sic_shift(occc,Pf,c,r,w,dr)
            r_,dr_,Pc,itc,Tc,_=orbs_sr(Z,occc,1); E0r,_,_=e_tot(Z,occc,Pc,Tc,c,r,w,dr); D_rel=E0r-E1r; Sr=sic_shift(occc,Pc,c,r,w,dr)
            eps=float(nw(Vf0,c[1],c[0],1.0,Z)[3])
            o=dict(Z=Z,el=el,tag=tag,kind='chan',ent=tagof(g),eps_frz=round(eps,5),D_frz=round(D_frz,5),D_rel=round(D_rel,5),relax=round(D_rel-D_frz,5),
                   D_frz_fo=round(D_frz+Sf-S1f,5),D_rel_fo=round(D_rel+Sr-S1r,5),c=CC,it=itc,sec=int(time.time()-t0))
        except Exception as e:
            o=dict(Z=Z,el=el,tag=tag,kind='chan',ent=tagof(g),err=str(e)[:80])
        open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)
    E0r0=None
    for s in channels(Z):
        if s==g or s[1]==1 or occ1d.get(s,0)<=1e-9: continue
        tag='swap'+tagof(s)
        if (Z,tag) in done: print("SKIP",Z,tag); continue
        t0=time.time()
        try:
            if E0r0 is None: E0r0,_,_=e_tot(Z,occ0,P0,T0,g,r,w,dr); S00=sic_shift(occ0,P0,g,r,w,dr)
            occs=minus(occ0,s[0],s[1],1.0)
            Es_f,_,_=e_tot(Z,occs,P0,T0,g,r,w,dr); Ssf=sic_shift(occs,P0,g,r,w,dr)
            r_,dr_,Ps,its,Ts,_=orbs_sr(Z,occs,2); Es_r,_,_=e_tot(Z,occs,Ps,Ts,g,r,w,dr); Ssr=sic_shift(occs,Ps,g,r,w,dr)
            o=dict(Z=Z,el=el,tag=tag,kind='remove '+tagof(s),ent=tagof(g),D_frz=round(E0r0-Es_f,5),D_rel=round(E0r0-Es_r,5),relax=round((E0r0-Es_r)-(E0r0-Es_f),5),
                   D_frz_fo=round((E0r0+S00)-(Es_f+Ssf),5),D_rel_fo=round((E0r0+S00)-(Es_r+Ssr),5),c=CC,it=its,sec=int(time.time()-t0))
        except Exception as e:
            o=dict(Z=Z,el=el,tag=tag,kind='remove '+tagof(s),ent=tagof(g),err=str(e)[:80])
        open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)
