"""hfcorr.py -- s26 (a'): exact-exchange (HFSR 'hf', c=C0) TS entrant eps(1/2) + first-order chain-Z correlation on the HF orbitals.
usage: python3 hfcorr.py Z ...  Appends hfcorr.jsonl. No constant beyond c."""
import sys,os,json,time,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1")
from t7c_hfsr import HFSR
from t7c_kernel import C0
from t5_scf import ground_occ,minus
import t7c_cuaudit as T
from hfs import L
OUT="hfcorr.jsonl"
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),
    64:('Gd','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f'),71:('Lu','5d')}
done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); occ=minus(ground_occ(Z),n,l,0.5); t0=time.time()
    h=HFSR(Z,occ,c=C0); eps,E,it,hist=h.run('hf',qtail=1)
    r,dr=h.r,h.dr; w=4*np.pi*r*r; P=h.P; Q={(a,b):q for a,b,q in occ}
    ne=P[(n,l)]**2; f=0.5
    nu=np.zeros_like(r); nd=np.zeros_like(r)
    for (a,b),q in Q.items():
        cap=2*(2*b+1); dens=P[(a,b)]**2
        if (a,b)==(n,l): nu+=f*dens; q_s=q-f
        else: q_s=q
        if q_s>=cap/2: nu+=(cap/2)*dens; nd+=(q_s-cap/2)*dens   # closed part even, excess... (open siblings: fill spin up first)
        else: nu+=q_s*dens
    # note: for closed shells q_s=cap -> up cap/2, down cap/2. For open other-shell (Gd 4f7): all up.
    vu,vd=T.v_gbz(nu/w,nd/w); vsic=T.v_gbz(f*ne/w,0*ne)[0]
    Dc=float(np.sum(ne*(vu-vsic)*dr))
    o=dict(Z=Z,el=el,sh=sh,eps_hf_half=round(float(eps[(n,l)]),5),it=it,Delta_c=round(Dc,5),eps_hfc=round(float(eps[(n,l)])+Dc,5),
           Etot=round(float(E),4),sec=int(time.time()-t0))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)