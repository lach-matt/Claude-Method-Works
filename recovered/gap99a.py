#!/usr/bin/env python3
"""gap99a.py -- S99: row-72 eps re-read for the 6s^2->5d^2 block dens. ONE reference solve per call (Zeno).
Prints eps(6s), eps(5d), den = 2(eps_6s - eps_5d). Delta_cfg NOT re-solved (filed s97). usage: gap99a.py {core|ent|run}"""
import sys,os,json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','rt')); os.chdir(os.path.join(HERE,'..','rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
core=NC.cfg_from_chain(71,ROWS); ent=NC.add(core,(5,2)); run=NC.add(core,(6,1))
side=sys.argv[1]; Z,cfg={'core':(71,core),'ent':(72,ent),'run':(72,run)}[side]
assert any((n,l)==(5,2) for n,l,q in cfg) and any((n,l,q)==(6,0,2) for n,l,q in cfg)  # 5d and 6s^2 present (F97.5 class)
for beta,maxit in NG.LADDER:
    g=H.HFC(Z,[tuple(x) for x in cfg],c=C0); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
    if it<maxit: break
else: raise RuntimeError
e6s=eps[(6,0)]; e5d=eps[(5,2)]; den=2*(e6s-e5d)
out={'side':side,'Z':Z,'E':float(E),'eps_6s':float(e6s),'eps_5d':float(e5d),'den':float(den)}
json.dump(out,open(os.path.join(HERE,'gap99a-%s.json'%side),'w'))
print("%-4s Z=%d E %.5f  eps(6s) %.5f  eps(5d) %.5f  den=2(e6s-e5d) %+.5f"%(side,Z,E,e6s,e5d,den),flush=True)
