"""janak_table.py -- s24: Janak-integrated removal energy from t7c_ownshell.jsonl test D rows; TABLE-JANAK-SESSION-24.txt"""
import json,numpy as np
from scipy.integrate import trapezoid
T5={json.loads(l)['Z']:json.loads(l) for l in open('t5.jsonl')}
Z_={json.loads(l)['Z']:json.loads(l) for l in open('t7c_corrz.jsonl')}
SOH={57:-0.0046,68:+0.0534}   # so/hund column of TABLE-CHAIN-15 (Er: -0.2802 -> -0.2268 = +0.0534; La: -0.0046), carried, stated
rows=[json.loads(l) for l in open('t7c_ownshell.jsonl') if '"D"' in l]
out=["Janak integral DE_J = int_0^1 eps(f) df (grid in f, interpolated in f^(1/3)) vs TS eps(1/2), chain Z, SIC_NOCLAMP=1, s24.",
     "el sh | eps(f->0) eps(1/2) eps(1) | DE_J | DE_J-eps(1/2) | so/hund | resid_TS resid_J (chain - meas)"]
for Z in sorted({r['Z'] for r in rows}):
    d=[r for r in rows if r['Z']==Z]; f=np.array([float(x['par']) for x in d]); E=np.array([x['E'] for x in d]); o=np.argsort(f); f=f[o];E=E[o]
    x=f**(1/3); xs=np.linspace(0,1,20001); Ei=np.interp(xs,x,E); I=float(trapezoid(Ei,xs**3)); e5=float(E[list(f).index(0.5)])
    m=T5[Z]['meas']; sh=SOH.get(Z,0.0)
    out.append(f"{d[0]['el']:2s} {d[0]['sh']} | {E[0]:+.4f} {e5:+.4f} {E[-1]:+.4f} | {I:+.4f} | {I-e5:+.4f} | {sh:+.4f} | {e5+sh-m:+.4f} {I+sh-m:+.4f}")
open('TABLE-JANAK-SESSION-24.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))