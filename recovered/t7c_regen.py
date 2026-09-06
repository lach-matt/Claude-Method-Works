"""t7c_regen.py -- s23 item (1): regenerate 15-row chain under F22.1 repair (SIC_NOCLAMP=1 must be set in env). Appends t7c_regen.jsonl; resumable. usage: Z..."""
import sys, json, os, time
assert os.environ.get("SIC_NOCLAMP")=="1", "set SIC_NOCLAMP=1"
from t7c_corr2 import scf_sic_corr
from t5_scf import ground_occ, minus
SH={55:('Cs','6s'),21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),
    57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f')}
A={json.loads(l)['Z']:json.loads(l) for l in open('t7c_corr_all.jsonl')}
done={json.loads(l)['Z'] for l in open('t7c_regen.jsonl')} if os.path.exists('t7c_regen.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); E={}; t0=time.time()
    for cr,key in ((None,'base'),("U","U"),("P","P")):
        Es,h,s=scf_sic_corr(Z,1,occ=hole,entrant=(n,l),mode="all",corr=cr); E[key]=round(float(Es[(n,l,s,"ent")]),4)
    b=A[Z]
    out=dict(Z=Z,el=el,sh=sh,noclamp=E,banked=dict(base=b['sr_sic'],U=b['corrU'],P=b['corrP']),
             dbase=round(E['base']-b['sr_sic'],4),shiftU=round(E['U']-E['base'],4),shiftP=round(E['P']-E['base'],4),
             dshiftU=round(E['U']-E['base']-b['shiftU'],4),dshiftP=round(E['P']-E['base']-b['shiftP'],4),sec=int(time.time()-t0))
    open('t7c_regen.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)