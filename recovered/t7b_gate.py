"""t7b_gate.py -- session 18 audit gates for the adopted t7b_hf.py: (B) mode='hfs' switch regenerates T5 HFS-TS;
(C) Janak identity: E0-E1 (av-config HF) vs eps(N-1/2)+J~/2 on a nodeless-entrant species."""
import sys, json, io, contextlib, numpy as np, warnings; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
from t5_scf import ground_occ, minus
from t7b_hf import HF, _c3j0sq
T5={json.loads(l)['Z']:json.loads(l) for l in open('t5.jsonl')}
which=sys.argv[1]
if which=='B':
    for Z in (21,26):
        t=T5[Z]; n,l=int(t['sh'][0]),"spdf".index(t['sh'][1]); g=ground_occ(Z)
        h=HF(Z,minus(g,n,l,0.5)); eps,E,it,_=h.run('hfs',qtail=1)
        print(f"GATE B  Z={Z} {t['sh']} hfs-switch eps {eps[(n,l)]:.4f}  T5 hfs_ts {t['hfs_ts']:.4f}  it {it}")
if which=='C':
    Z=int(sys.argv[2]); t=T5[Z]; n,l=int(t['sh'][0]),"spdf".index(t['sh'][1]); g=ground_occ(Z); w=(2*l+1)/(4*l+1)
    h=HF(Z,minus(g,n,l,0.5)); eps,_,_,_=h.run('hf',qtail=1); P=h.P[(n,l)]; r,dr=h.r,h.dr
    Fk=lambda k: float(np.sum(P*P*h.Yk(P,P,k)/r*dr)); J=Fk(0)-w*sum(_c3j0sq(l,k,l)*Fk(k) for k in range(2,2*l+1,2))
    h0=HF(Z,g); _,E0,_,_=h0.run('hf',qtail=1); h1=HF(Z,minus(g,n,l,1.0)); _,E1,_,_=h1.run('hf',qtail=2)
    print(f"GATE C  Z={Z} {t['sh']} eps_half {eps[(n,l)]:.4f} J~ {J:.4f} eps+J/2 {eps[(n,l)]+0.5*J:.4f}  E0-E1 {E0-E1:.4f}")