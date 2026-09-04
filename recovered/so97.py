#!/usr/bin/env python3
"""so97.py -- S97 Item 5 scope: first-order spin-orbit parameter xi_nl on the sealed KH scalar-relativistic field, no new kernel.
xi = (1/2c^2) < P | (1/(r M^2)) dV/dr | P >,  M = 1 + (eps - V)/(2c^2)  (Koelling-Harmon; V = direct potential as v5c).
usage: so97.py Z CFG SHELLS [--c 1e6 (can-fail)]   CFG like 'Cn+71' ; SHELLS like 71,61"""
import sys,os,json,time,numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','rt')); os.chdir(os.path.join(HERE,'..','rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0,_derivs
Z=int(sys.argv[1]); cfgs=sys.argv[2]; shells=[(int(s[0]),int(s[1])) for s in sys.argv[3].split(',')]
c=float(sys.argv[sys.argv.index('--c')+1]) if '--c' in sys.argv else C0
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
cfg=NC.cfg_from_chain(108,ROWS)   # Hs row cfg(108)? use chain's last sealed object as base
base,adds=cfgs.split('+')
for a in adds.split('/'):
    n,l,q=int(a[0]),int(a[1]),int(a[2:] or 1); cfg=NC.add(cfg,(n,l)) if q==1 else cfg
    for _ in range(q-1): cfg=NC.add(cfg,(n,l))
print("cfg",cfg,flush=True)
t0=time.time()
for rung,(beta,maxit) in enumerate(NG.LADDER):
    g=H.HFC(Z,[tuple(x) for x in cfg],c=c); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
    if it<maxit: break
print("solved Z=%d E=%.5f rung %d it %d (%.0fs)"%(Z,E,rung,it,time.time()-t0),flush=True)
r,dr=g.r,g.dr; P=g.P; keys=[(n,l) for n,l,q in g.occ]; Q={(n,l):q for n,l,q in g.occ}
Vdir=-Z/r+sum(Q[b]*g.Yk(P[b],P[b],0)/r for b in keys); Vp,_=_derivs(g.x,Vdir)
for s in shells:
    M=1+(eps[s]-Vdir)/(2*c*c); xi=np.sum(P[s]**2*Vp/(r*M*M)*dr)/(2*c*c)
    print("xi(%d%s) = %.5f Ha   eps %.5f   j-split(l+1/2 - l-1/2) = %.5f"%(s[0],'spdfg'[s[1]],xi,eps[s],xi*(2*s[1]+1)/2),flush=True)