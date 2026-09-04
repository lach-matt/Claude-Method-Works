"""t7c_corr_all.py -- s22: GB U/P bracket on all 15 rows; base = t7c_sic row if banked else corr=None run. Appends t7c_corr_all.jsonl. usage: Z"""
import sys, json, os
from t7c_corr import scf_sic_corr
from t5_scf import ground_occ, minus
SH={55:('Cs','6s'),21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),
    57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f')}
B={json.loads(l)['Z']:json.loads(l) for l in open('t7c_sic.jsonl')}
C={json.loads(l)['Z']:json.loads(l) for l in open('t7c_corr.jsonl')}
done={json.loads(l)['Z'] for l in open('t7c_corr_all.jsonl')} if os.path.exists('t7c_corr_all.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); E={}
    if Z in C: E={'base':B[Z]['sr_all'],'U':C[Z]['corrU'],'P':C[Z]['corrP']}; src='banked-s21'
    else:
        src='run-s22'
        for cr,key in ((None,'base'),("U","U"),("P","P")):
            Es,h,s=scf_sic_corr(Z,1,occ=hole,entrant=(n,l),mode="all",corr=cr); E[key]=round(float(Es[(n,l,s,"ent")]),4)
    out=dict(Z=Z,el=el,sh=sh,src=src,sr_sic=E['base'],corrU=E['U'],corrP=E['P'],shiftU=round(E['U']-E['base'],4),shiftP=round(E['P']-E['base'],4))
    open('t7c_corr_all.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)