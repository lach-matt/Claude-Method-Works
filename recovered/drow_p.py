"""drow_p.py -- s30 Route P (PREDICTION-DROW-SESSION-30). Decompose DEc_sc = A + B + R on the s28 sc path (frachf.HFCf), f=1 (neutral) vs f=0 (ion).
A = Δ∫ n_tot eps_c(n_tot); B = -Δ q_e ∫ P_e² eps_c(P_e²/w,0) (entrant PZ self-correlation); R = same over non-entrant shells. Also Q_mid for P2.
usage: python3 drow_p.py Z [Z ...]   -> appends drow_p.jsonl (done-set), one SCF pair per Z."""
import sys,os,json,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; from t7c_kernel import C0; from t5_scf import ground_occ; import t7c_cuaudit as T
Zs=[int(a) for a in sys.argv[1:]]; sys.argv=[sys.argv[0]]
exec(open('frachf.py').read().split('def path')[0].split('import t7c_cuaudit as T')[1])   # HFCf class only
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
FR={d['Z']:d for d in map(json.loads,open('frachf.jsonl'))}; CF={d['Z']:d for d in map(json.loads,open('cutfrac.jsonl'))}
OUT="drow_p.jsonl"; done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
def pieces(h,ent,f):
    r,dr=h.r,h.dr; w=4*np.pi*r*r; nu,nd,_=H.spin_split(h.occ,h.P)
    A=float(np.sum((nu+nd)*H.eps_c(nu/w,nd/w)*dr)); B=0.0; R=0.0
    for a,b,q in h.occ:
        ff=f if (a,b)==ent else 1.0
        t=-q*float(np.sum(h.P[(a,b)]**2*H.eps_c(ff*h.P[(a,b)]**2/w,0*r)*dr))
        if (a,b)==ent: B+=t
        else: R+=t
    return A,B,R
for Z in Zs:
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); ent=(n,l); H.CORR=True; occ0=ground_occ(Z)
    res={}
    for f in (1.0,0.0):
        occ=[(a,b,(f if (a,b)==ent else q)) for a,b,q in occ0 if not ((a,b)==ent and f==0.0)]
        h=HFCf(Z,occ,c=C0); h.ent=ent; h.f=f
        if f>0: h.frac={ent:(0,f)}
        E,Ec,it,eps=h.run2(); A,B,R=pieces(h,ent,f); res[f]=dict(E=float(E),Ec=float(Ec),A=A,B=B,R=R,it=it)
        if f==1.0:
            r,dr=h.r,h.dr; w=4*np.pi*r*r; nu,nd,_=H.spin_split(occ,h.P); e_tot=H.eps_c(nu/w,nd/w)
            qe=h.P[ent]**2*dr; Q=qe.sum(); idx=np.where(e_tot<0)[0]; r_cut=float(r[idx[-1]]) if len(idx) else 0.0
            pd=h.P[(n-1,1)]**2; r_peak=float(r[int(np.argmax(pd))])
            Q_mid=float(qe[(r<r_cut)&(r>r_peak)].sum()/Q); Q_in=float(qe[r<r_cut].sum()/Q)
    dA=res[1.0]['A']-res[0.0]['A']; dB=res[1.0]['B']-res[0.0]['B']; dR=res[1.0]['R']-res[0.0]['R']; DEc=res[1.0]['Ec']-res[0.0]['Ec']
    c=CF.get(Z,{}); excess=(c.get('missing_over_req',0)-c.get('F_out',0))*c.get('required',0) if c else None
    o=dict(Z=Z,el=el,sh=sh,it=[res[1.0]['it'],res[0.0]['it']],DEc=round(DEc,6),DEc_frachf=FR[Z]['DEc_sc'],A=round(dA,6),B=round(dB,6),R=round(dR,6),
           sum_minus_DEc=round(dA+dB+dR-DEc,7),r_cut=round(r_cut,3),r_peak_p=round(r_peak,3),Q_in=round(Q_in,4),Q_mid=round(Q_mid,4),
           excess=(round(excess,5) if excess is not None else None),g=(round(excess/Q_mid,5) if excess is not None else None))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)
