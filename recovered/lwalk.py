"""lwalk.py -- s35 PREDICTION-LWALK: the l-walk with n. Row Z: ion of record (ground minus the ground entrant); entrant placed in each enumerated empty channel c=(n,l).
D_frz(c): frozen on the ground-neutral HFS field (t5 orbitals; empty channels by Numerov on the same field). D_rel(c): relaxed E path (t5 SCF of ion+c, qtail 1; ion qtail 2),
energy functional of xseam_relax (T+V_ne+H+LSD-x+PZ-SIC per electron+S). SWAP row: the frontier partner removed from the ground neutral instead (e.g. Sc 4s from 3d1 4s2).
usage: python3 lwalk.py Z ...  appends lwalk.jsonl (key Z,tag). No constant; no measured input; channels enumerated, not searched."""
import sys,os,json,time,numpy as np
sys.argv,_a=[sys.argv[0]],sys.argv; exec(open('xseam_relax.py').read().split('for Z in map')[0]); sys.argv=_a
CH={21:[(3,2),(4,1),(5,0),(4,2),(4,3)], 39:[(4,2),(5,1),(6,0),(5,2),(4,3)], 57:[(5,2),(4,3),(6,1),(7,0),(6,2)], 71:[(5,2),(6,1),(7,0),(5,3),(6,2)], 55:[(6,0),(5,2),(4,3),(6,1),(7,0)]}
SWAP={21:(4,0),39:(5,0),57:(6,0),71:(6,0),55:None}
OUT='lwalk.jsonl'; done={(d['Z'],d['tag']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
def add(occ,n,l,k):
    o=[list(t) for t in occ]; f=False
    for t in o:
        if t[0]==n and t[1]==l: t[2]+=k; f=True
    if not f: o.append([n,l,k])
    return [tuple(t) for t in o]
for Z in map(int,_a[1:]):
    el,sh=SH[Z]; g=(int(sh[0]),"spdf".index(sh[1])); occ0=ground_occ(Z); occ1=minus(occ0,g[0],g[1],1.0)
    Vf0,Es0,_,_=scf_occ(Z,occ0,1)
    r,dr,P0,it0,T0=orbs(Z,occ0,1); w=4*np.pi*r*r; x=np.log(r); V0=Vf0(r)
    r,dr,P1,it1,T1=orbs(Z,occ1,2); E1r,_,_=e_tot(Z,occ1,P1,T1,g,r,w,dr); E1f,_,_=e_tot(Z,occ1,P0,T0,g,r,w,dr)
    for c in CH[Z]:
        tag=f"{c[0]}{'spdf'[c[1]]}"
        if (Z,tag) in done: print("SKIP",Z,tag); continue
        t0=time.time(); occc=add(occ1,c[0],c[1],1.0)
        try:
            Pf=dict(P0); Tf=dict(T0)
            if c not in Pf:
                rr,drr,u,E,nd=numerov_wf(Vf0,c[1],c[0],1.0,Z); ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); Pf[c]=ui; Tf[c]=float(E-np.sum(ui*ui*V0*dr))
            E0f,_,_=e_tot(Z,occc,Pf,Tf,c,r,w,dr); D_frz=E0f-E1f
            r_,dr_,Pc,itc,Tc=orbs(Z,occc,1); E0r,_,_=e_tot(Z,occc,Pc,Tc,c,r,w,dr); D_rel=E0r-E1r
            eps=float(numerov_wf(Vf0,c[1],c[0],1.0,Z)[3])
            o=dict(Z=Z,el=el,tag=tag,kind='chan',eps_frz=round(eps,5),D_frz=round(D_frz,5),D_rel=round(D_rel,5),relax=round(D_rel-D_frz,5),it=itc,sec=int(time.time()-t0))
        except Exception as e:
            o=dict(Z=Z,el=el,tag=tag,kind='chan',err=str(e)[:80])
        open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)
    s=SWAP[Z]
    if s and (Z,'swap') not in done:
        t0=time.time(); occs=minus(occ0,s[0],s[1],1.0); E0r0,_,_=e_tot(Z,occ0,P0,T0,g,r,w,dr)
        Es_f,_,_=e_tot(Z,occs,P0,T0,g,r,w,dr); r_,dr_,Ps,its,Ts=orbs(Z,occs,2); Es_r,_,_=e_tot(Z,occs,Ps,Ts,g,r,w,dr)
        # note: functional treats the GROUND entrant g as the polarised/SIC'd one in both neutral and s-hole ion (consistent, stated)
        o=dict(Z=Z,el=el,tag='swap',kind='remove '+f"{s[0]}{'spdf'[s[1]]}",D_frz=round(E0r0-Es_f,5),D_rel=round(E0r0-Es_r,5),relax=round((E0r0-Es_r)-(E0r0-Es_f),5),it=its,sec=int(time.time()-t0))
        open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)