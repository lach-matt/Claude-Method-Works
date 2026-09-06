#!/usr/bin/env python3
"""gap99a89.py -- S99 Item 2: ONE HF reference solve, row-89 ent side, eps(7s)/eps(6d) -> den. usage: gap99a89.py"""
import sys,os,json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','rt')); os.chdir(os.path.join(HERE,'..','rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
core=NC.cfg_from_chain(88,ROWS); ent=NC.add(core,(6,2))
assert any((n,l,q)==(7,0,2) for n,l,q in ent) and any((n,l)==(6,2) for n,l,q in ent)
for beta,maxit in NG.LADDER:
    g=H.HFC(89,[tuple(x) for x in ent],c=C0); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
    if it<maxit: break
else: raise RuntimeError
e7s=eps[(7,0)]; e6d=eps[(6,2)]; den=2*(e7s-e6d)
json.dump({'side':'ent','Z':89,'E':float(E),'eps_7s':float(e7s),'eps_6d':float(e6d),'den':float(den)},open(os.path.join(HERE,'gap99a89-ent.json'),'w'))
print("ent Z=89 E %.5f  eps(7s) %.5f  eps(6d) %.5f  den=2(e7s-e6d) %+.5f"%(E,e7s,e6d,den),flush=True)