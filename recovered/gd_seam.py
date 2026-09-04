"""gd_seam.py -- s33 PREDICTION-GDSEAM: hfterm machinery on Gd (Z=64), entrant 5d; prints D_avg, D_term, seam, closed-form check."""
import os,sys,json,numpy as np; os.environ.setdefault("SIC_NOCLAMP","1")
import hfterm as H; from t5_scf import ground_occ,minus; from t7c_hfsr import HFSR; from t7c_kernel import C0
Z=64; n,l=5,2; occ0=ground_occ(Z); occ1=[(a,b,q) for a,b,q in minus(occ0,n,l,1.0) if q>0]
print("occ0 open:",[(a,b,q) for a,b,q in occ0 if 0<q<2*(2*b+1)])
res={}
for tag,occ in (("neu",occ0),("ion",occ1)):
    h=HFSR(Z,occ,c=C0); e,E,it,_=h.run('hf',qtail=1)
    openk=[(a,b) for a,b,q in occ if 0<q<2*(2*b+1)]; shells=[(b,int(round(q))) for a,b,q in occ if 0<q<2*(2*b+1)]
    Fk,Gk=H.radial(h,openk); so=H.hund_det(shells); dE=H.E_open(shells,so,Fk,Gk)-H.E_avg(shells,Fk,Gk)
    res[tag]=dict(E=float(E),it=it,dE=dE,openk=openk,Gk=Gk,shells=shells)
    print(tag,"E",round(float(E),5),"it",it,"open",shells,"dE_term",round(dE,5),flush=True)
D_avg=res["ion"]["E"]-res["neu"]["E"]; seam=res["ion"]["dE"]-res["neu"]["dE"]
# closed form on the neutral orbitals: +1/2 sum_k G^k(4f,5d) Q_k, Q_k = sum_m c^k(2 md;3 m)^2 (md=0)
ok=res["neu"]["openk"]; i,j=ok.index((4,3)),ok.index((5,2)); G=res["neu"]["Gk"][(min(i,j),max(i,j))]
Q={k:sum(H.ck(2,0,3,m,k)**2 for m in range(-3,4)) for k in G}
cf=0.5*sum(G[k]*Q[k] for k in G)
out=dict(Z=64,el="Gd",D_avg=round(D_avg,5),D_term=round(D_avg+seam,5),seam=round(seam,5),closed_form=round(cf,5),Gk_fd={k:round(v,5) for k,v in G.items()},Qk={k:round(v,4) for k,v in Q.items()},dE_neu=round(res["neu"]["dE"],5),dE_ion=round(res["ion"]["dE"],5))
print(out); open("gd_seam.json","w").write(json.dumps(out))