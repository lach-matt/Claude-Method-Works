"""nlwalk.py -- s36 PREDICTION-NLWALK: the full-table n+l walk. lwalk.py generalised: entrant derived from ground.expand (ground(Z)-ground(Z-1)),
channels by rule (N,0) (N,1) (N-1,2) (N-2,3 if N>=6) with N = max n of ground(Z); swap = each OCCUPIED frontier partner (s,d,f channels) removed from the neutral.
Energetics VERBATIM lwalk.py (t5 non-rel local field; frozen HFS + relaxed E path; xseam_relax functional; SIC per electron on P^2 -- stated).
usage: python3 nlwalk.py Z ...  appends nlwalk.jsonl (key Z,tag). No constant; no measured input; channels enumerated."""
import sys,os,json,time,numpy as np
sys.argv,_a=[sys.argv[0]],sys.argv; exec(open('xseam_relax.py').read().split('for Z in map')[0]); sys.argv=_a
import ground as G
EL={13:'Al',19:'K',20:'Ca',21:'Sc',31:'Ga',37:'Rb',38:'Sr',39:'Y',49:'In',55:'Cs',56:'Ba',57:'La',58:'Ce',64:'Gd',71:'Lu',72:'Hf',81:'Tl',87:'Fr',88:'Ra',89:'Ac',90:'Th',91:'Pa',92:'U',96:'Cm',103:'Lr',104:'Rf'}
def entrant(Z):
    a={(n,l):k for n,l,k in G.expand(Z)}; b={(n,l):k for n,l,k in G.expand(Z-1)}
    d=[(nl,a[nl]-b.get(nl,0)) for nl in a if abs(a[nl]-b.get(nl,0))>1e-9]
    up=[nl for nl,x in d if x>0]; assert len(up)==1, (Z,d); return up[0], d
def channels(Z):
    N=max(n for n,l,k in G.expand(Z)); ch=[(N,0),(N,1),(N-1,2)]
    if N>=6: ch.append((N-2,3))
    return ch
OUT='nlwalk.jsonl'; done={(d['Z'],d['tag']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
def add(occ,n,l,k):
    o=[list(t) for t in occ]; f=False
    for t in o:
        if t[0]==n and t[1]==l: t[2]+=k; f=True
    if not f: o.append([n,l,k])
    return [tuple(t) for t in o]
def tagof(c): return f"{c[0]}{'spdf'[c[1]]}"
for Z in map(int,_a[1:]):
    el=EL.get(Z,str(Z)); g,dd=entrant(Z); occ0=ground_occ(Z); occ1=minus(occ0,g[0],g[1],1.0); occ1d={(n,l):k for n,l,k in occ1}
    Vf0,Es0,_,_=scf_occ(Z,occ0,1)
    r,dr,P0,it0,T0=orbs(Z,occ0,1); w=4*np.pi*r*r; V0=Vf0(r)
    r,dr,P1,it1,T1=orbs(Z,occ1,2); E1r,_,_=e_tot(Z,occ1,P1,T1,g,r,w,dr); E1f,_,_=e_tot(Z,occ1,P0,T0,g,r,w,dr)
    for c in channels(Z):
        tag=tagof(c)
        if (Z,tag) in done: print("SKIP",Z,tag); continue
        if occ1d.get(c,0)>=2*(2*c[1]+1)-1e-9:
            o=dict(Z=Z,el=el,tag=tag,kind='chan',ent=tagof(g),full=True); open(OUT,'a').write(json.dumps(o)+'\n'); print(o); continue
        t0=time.time(); occc=add(occ1,c[0],c[1],1.0)
        try:
            Pf=dict(P0); Tf=dict(T0)
            if c not in Pf:
                rr,drr,u,E,nd=numerov_wf(Vf0,c[1],c[0],1.0,Z); ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); Pf[c]=ui; Tf[c]=float(E-np.sum(ui*ui*V0*dr))
            E0f,_,_=e_tot(Z,occc,Pf,Tf,c,r,w,dr); D_frz=E0f-E1f
            r_,dr_,Pc,itc,Tc=orbs(Z,occc,1); E0r,_,_=e_tot(Z,occc,Pc,Tc,c,r,w,dr); D_rel=E0r-E1r
            eps=float(numerov_wf(Vf0,c[1],c[0],1.0,Z)[3])
            o=dict(Z=Z,el=el,tag=tag,kind='chan',ent=tagof(g),eps_frz=round(eps,5),D_frz=round(D_frz,5),D_rel=round(D_rel,5),relax=round(D_rel-D_frz,5),it=itc,sec=int(time.time()-t0))
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
            if E0r0 is None: E0r0,_,_=e_tot(Z,occ0,P0,T0,g,r,w,dr)
            occs=minus(occ0,s[0],s[1],1.0)
            Es_f,_,_=e_tot(Z,occs,P0,T0,g,r,w,dr); r_,dr_,Ps,its,Ts=orbs(Z,occs,2); Es_r,_,_=e_tot(Z,occs,Ps,Ts,g,r,w,dr)
            o=dict(Z=Z,el=el,tag=tag,kind='remove '+tagof(s),ent=tagof(g),D_frz=round(E0r0-Es_f,5),D_rel=round(E0r0-Es_r,5),relax=round((E0r0-Es_r)-(E0r0-Es_f),5),it=its,sec=int(time.time()-t0))
        except Exception as e:
            o=dict(Z=Z,el=el,tag=tag,kind='remove '+tagof(s),ent=tagof(g),err=str(e)[:80])
        open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)