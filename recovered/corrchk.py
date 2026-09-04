import os, sys, json, time
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
sys.path.insert(0,'.')
import hfc2 as H
from t7c_kernel import C0
cfg=[tuple(x) for x in json.load(open('/home/claude/s84/pack82/conf82_ref.json'))['cfg']]
TARGET=-25694.541630577907
for corr in (True,False):
    H.CORR=corr
    t=time.time(); E,_,it,eps=H.HFC(89,cfg,c=C0).run2()
    print(f"CORR={corr}  E={float(E):.9f}  it={it}  d_vs_conf82={(float(E)-TARGET)*1000:+.6f} mHa  {time.time()-t:.1f}s")