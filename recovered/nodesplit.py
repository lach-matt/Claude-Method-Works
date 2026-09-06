"""nodesplit.py -- s30 PREDICTION-NODESPLIT: split A, B at the entrant's outermost radial node on the f=1 neutral SCF (drow_p path)."""
import sys,os,json,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; from t7c_kernel import C0; from t5_scf import ground_occ; import t7c_cuaudit as T
Zs=[int(a) for a in sys.argv[1:]]; sys.argv=[sys.argv[0]]
exec(open('frachf.py').read().split('def path')[0].split('import t7c_cuaudit as T')[1])
SH={21:('Sc','3d'),39:('Y','4d'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
DP={d['Z']:d for d in map(json.loads,open('drow_p.jsonl'))}
OUT="nodesplit.jsonl"; done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in Zs:
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); ent=(n,l); H.CORR=True; occ=ground_occ(Z)
    h=HFCf(Z,occ,c=C0); h.ent=ent; h.f=1.0; h.frac={ent:(0,1.0)}; E,Ec,it,eps=h.run2()
    r,dr=h.r,h.dr; w=4*np.pi*r*r; P=h.P; ue=P[ent]; nu,nd,_=H.spin_split(occ,P); ntot=nu+nd
    ne=ue*ue; ncore=ntot-ne
    sgn=np.sign(ue); ch=np.where((sgn[:-1]*sgn[1:]<0)&(r[1:]>1e-3))[0]
    r_node=float(r[ch[-1]]) if len(ch) else 0.0; m=r<r_node
    Bfull=-np.sum(ne*H.eps_c(ne/w,0*r)*dr); B_in=-np.sum((ne*H.eps_c(ne/w,0*r)*dr)[m])
    a=ntot*H.eps_c(nu/w,nd/w)-ncore*H.eps_c((nu-ne)/w,nd/w); Afull=float(np.sum(a*dr)); A_in=float(np.sum((a*dr)[m]))
    Q_in=float(np.sum((ne*dr)[m])/np.sum(ne*dr)); ex=DP[Z]['excess']
    o=dict(Z=Z,el=el,sh=sh,it=it,nodes=len(ch),r_node=round(r_node,4),Q_in=round(Q_in,4),B=round(float(Bfull),6),B_in=round(float(B_in),6),
           B_in_over_B=round(float(B_in/Bfull),4),A_frozen=round(Afull,6),A_in=round(A_in,6),A_in_over_A=round(A_in/Afull,4),excess=ex,
           B_in_over_excess=(round(float(B_in)/ex,3) if ex else None))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)