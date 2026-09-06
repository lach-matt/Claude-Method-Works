import numpy as np, re, json
from tfd import potential
from rad import defect
src=open('gate.py').read()
M=eval(re.search(r"M = (\{.*?\n\})",src,re.S).group(1)); core_n=eval(re.search(r"core_n = (\{.*?\n\})",src,re.S).group(1).replace('\n',''))
res=[];out={}
for sp,(Z,ch,md) in M.items():
    V,x0=potential(Z,ch); row=[]
    for l,dm in md.items():
        n0=core_n[Z][l]; d2,_=defect(V,l,n0+4,ch,Z); row.append((l,dm,d2)); res.append(d2-dm)
    out[sp]=row
    print(f"{sp:7s}"+"  ".join(f"l{l}: meas {dm:6.3f} TFD {d2:6.3f}" for l,dm,d2 in row))
res=np.array(res); print(f"\nrms(TFD - measured) over {len(res)} channels = {np.sqrt((res**2).mean()):.3f}; mean signed = {res.mean():+.3f}")
json.dump(out,open('gate2.json','w'))