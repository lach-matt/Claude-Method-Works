#!/usr/bin/env python3
"""gap98.py -- S98: relaxed configuration gap Delta_cfg = E(cfg 7s^2->6d^2) - E(cfg) at row 105, three sides, rung 0. 6d present on every side (F97.5 class safe); electron count asserted. usage: gap98.py"""
import sys,os,json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','rt')); os.chdir(os.path.join(HERE,'..','rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
core=NC.cfg_from_chain(104,ROWS); ent=NC.add(core,(6,2)); run=NC.add(core,(7,1))
def swap(cfg):
    assert any((n,l)==(6,2) for n,l,q in cfg) and any((n,l,q)==(7,0,2) for n,l,q in cfg)
    out=[(n,l,(q-2 if (n,l)==(7,0) else q+2 if (n,l)==(6,2) else q)) for n,l,q in cfg]
    out=[x for x in out if x[2]>0]; assert sum(q for _,_,q in out)==sum(q for _,_,q in cfg); return out
def solve(Z,cfg):
    for beta,maxit in NG.LADDER:
        g=H.HFC(Z,[tuple(x) for x in cfg],c=C0); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
        if it<maxit: return float(E),eps
    raise RuntimeError
for name,Z,cfg in (('core',104,core),('ent',105,ent),('run',105,run)):
    (E0,eps),(E1,_)=solve(Z,cfg),solve(Z,swap(cfg))
    print("%-4s Z=%d N=%d E(ref) %.5f E(7s2->6d2) %.5f Delta %+.5f  eps(6d) %.4f eps(7s) %.4f"%(name,Z,sum(q for _,_,q in cfg),E0,E1,E1-E0,eps.get((6,2),float('nan')) if isinstance(eps,dict) else float('nan'),eps.get((7,0),float('nan')) if isinstance(eps,dict) else float('nan')),flush=True)