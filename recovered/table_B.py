"""table_B.py -- s34: DE_J^S = int eps_S(f) df vs eps_S(1/2) (janak_S.jsonl), against the chain-Z record (janak_table logic verbatim) and the E-path seam of s33."""
import json,numpy as np
from scipy.integrate import trapezoid
def janak(rows):
    f=np.array([float(x['f'] if 'f' in x else x['par']) for x in rows]); E=np.array([x['E'] for x in rows]); o=np.argsort(f); f=f[o];E=E[o]
    x=f**(1/3); xs=np.linspace(0,1,20001); Ei=np.interp(xs,x,E); I=float(trapezoid(Ei,xs**3)); e5=float(E[list(f).index(0.5)])
    return E[0],e5,E[-1],I
S={}; 
for l in open('janak_S.jsonl'):
    d=json.loads(l); S.setdefault(d['Z'],[]).append(d)
Zr={}
for l in open('t7c_ownshell.jsonl'):
    d=json.loads(l)
    if d['test']=='D': Zr.setdefault(d['Z'],[]).append(d)
SEAM={21:-0.0324,39:-0.0088,57:-0.0071,64:-0.0052,71:-0.0090,55:-0.0035}   # E path resid (IE_E vs T), FINDING-SEAM s33, chain S
out=["s34 B: Janak integral vs TS eigenvalue on the E path under S (janak_S.jsonl) and chain Z (t7c_ownshell.jsonl D). SIC_NOCLAMP=1 SUBCELL=1.",
     "el sh | S: eps(f->0) eps(1/2) eps(1) DE_J | DE_J-eps(1/2) [S] | [Z record] | S-Z | E resid(S) | E resid if DSCF"]
for Z in (21,39,57,64,71,55):
    a0,a5,a1,aI=janak(S[Z]); b0,b5,b1,bI=janak(Zr[Z]); kS=aI-a5; kZ=bI-b5
    out.append(f"{S[Z][0]['el']:2s} {S[Z][0]['sh']} | {a0:+.4f} {a5:+.4f} {a1:+.4f} {aI:+.4f} | {kS:+.4f} | {kZ:+.4f} | {kS-kZ:+.4f} | {SEAM[Z]:+.4f} | {SEAM[Z]+kS:+.4f}")
k3=None
open('TABLE-B-SESSION-34.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))