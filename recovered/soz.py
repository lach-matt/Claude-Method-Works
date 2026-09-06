"""soz.py -- s38 item 1a: SO gap contribution on the walk's pair, first-order Lande, PREDICTION-SO-SIGN filed first.
zeta from t7c_so.zeta on the TS object (half hole in the channel), the s19 convention. No constant, no measured input.
gap_SO - gap_LS = so(ion_s) - so(ion_d)   [the neutral cancels, FINDING-TERMS section 2]
class A: ion_d closed (0) ; ion_s d^1 s^1 3D_1, A=zeta/2 -> -1.5 zeta            -> diff = -1.5 zeta
class B: ion_d d^1 2D_3/2 -> -1.5 zeta    ; ion_s d^2 s^1 4F_3/2, A=zeta/3 -> -2 zeta -> diff = -0.5 zeta
class C: f^n common to both ions; the s-removed ion additionally holds d^1 -> diff = -1.5 zeta_d
usage: python3 soz.py Z ...   appends soz.jsonl
"""
import sys,json,os,time
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
from t5_scf import ground_occ,minus
from t7c_so import zeta
import ground as G
NAME={21:'Sc',39:'Y',57:'La',58:'Ce',64:'Gd',71:'Lu',72:'Hf',89:'Ac',90:'Th',91:'Pa',92:'U',96:'Cm',104:'Rf'}
CLS={21:'A',39:'A',57:'A',71:'A',89:'A',72:'B',90:'B',104:'B',58:'C',64:'C',91:'C',92:'C',96:'C'}
COEF={'A':-1.5,'B':-0.5,'C':-1.5}
OUT='soz.jsonl'
done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    t0=time.time(); N=max(n for n,l,k in G.expand(Z)); n,l=N-1,2
    occ=minus(ground_occ(Z),n,l,0.5)
    E,z,it=zeta(Z,1,occ,n,l)
    c=COEF[CLS[Z]]; o=dict(Z=Z,el=NAME[Z],cls=CLS[Z],ch=f"{n}d",zeta_d=round(z,5),coef=c,so_gap=round(c*z,5),E_ts=round(E,5),it=it,sec=int(time.time()-t0))
    open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)
