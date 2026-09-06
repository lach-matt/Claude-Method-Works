"""t7c_corrz_run.py -- s23: corr="Z" on the 15 rows (SIC_NOCLAMP=1). Appends t7c_corrz.jsonl; resumable. usage: Z..."""
import sys, json, os, time
assert os.environ.get("SIC_NOCLAMP")=="1"
from t7c_corrz import scf_sic_corr
from t5_scf import ground_occ, minus
SH={55:('Cs','6s'),21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),
    57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f')}
R={json.loads(l)['Z']:json.loads(l) for l in open('t7c_regen.jsonl')}
done={json.loads(l)['Z'] for l in open('t7c_corrz.jsonl')} if os.path.exists('t7c_corrz.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); t0=time.time()
    Es,h,s=scf_sic_corr(Z,1,occ=hole,entrant=(n,l),mode="all",corr="Z"); EZ=round(float(Es[(n,l,s,"ent")]),4)
    b=R[Z]['noclamp']
    out=dict(Z=Z,el=el,sh=sh,EZ=EZ,base=b['base'],U=b['U'],P=b['P'],shiftZ=round(EZ-b['base'],4),inside=bool(b['U']-1e-9<=EZ<=b['P']+1e-9),
             closerP=bool(abs(EZ-b['P'])<abs(EZ-b['U'])),sec=int(time.time()-t0))
    open('t7c_corrz.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)