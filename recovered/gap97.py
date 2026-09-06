#!/usr/bin/env python3
"""gap97.py -- S97: relaxed configuration gap for the 6s^2 -> 5d^2 block at row 72. Solves cfg and cfg(6s^2->5d^2) on each side; prints Delta = E(d2) - E(ref). usage: gap97.py"""
import sys,os,json,time
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','rt')); os.chdir(os.path.join(HERE,'..','rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
core=NC.cfg_from_chain(71,ROWS); ent=NC.add(core,(5,2)); run=NC.add(core,(6,1))
def swap(cfg): return [(n,l,(q-2 if (n,l)==(6,0) else q+2 if (n,l)==(5,2) else q)) for n,l,q in cfg if not((n,l)==(6,0) and q==2)]
def solve(Z,cfg):
    for beta,maxit in NG.LADDER:
        g=H.HFC(Z,[tuple(x) for x in cfg],c=C0); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
        if it<maxit: return float(E)
    raise RuntimeError
for name,Z,cfg in (('core',71,core),('ent',72,ent),('run',72,run)):
    E0=solve(Z,cfg); E1=solve(Z,swap(cfg)); print("%-4s Z=%d  E(ref) %.5f  E(6s2->5d2) %.5f  Delta %+.5f"%(name,Z,E0,E1,E1-E0),flush=True)