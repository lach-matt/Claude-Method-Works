#!/usr/bin/env python3
"""cc99.py -- S99: row-72 dcc re-read. cc98 filed rule, with V^2(ent) COMPUTED (piece x den from gap99a eps),
core/run V^2 BRACKETED {0, s97 declared} (both sign-inconsistent under piece x den; F99.2).
Can-fails: --canfail-ent zeroes V^2(ent) -> dcc must MOVE (lever alive). --canfail-core perturbs the core block by +0.01 -> dcc must NOT move (exact cancellation of the shared 60-60 core value).
usage: cc99.py [--canfail-ent] [--canfail-core]"""
import json,sys,os,math
HERE=os.path.dirname(os.path.abspath(__file__)); P=os.path.join(HERE,'..','pack96')
CFE='--canfail-ent' in sys.argv; CFC='--canfail-core' in sys.argv
def ck(s): return json.load(open(os.path.join(P,'v5d-72-%s.e2w-ck-20-lNone.json'%s)))
def gp(s): return json.load(open(os.path.join(HERE,'gap99a-%s.json'%s)))
def twostate(D,V2): return (D-math.sqrt(D*D+4*V2))/2
S={s:ck(s) for s in ('core','ent','run')}
EXCL={'ent':-0.047518,'run':-0.007765,'core':-0.018623}
D={'core':0.2182,'ent':0.1979,'run':0.1429}
dD2,m=0.08295,0.04507
piece={s:S[s]['60-60']-EXCL[s] for s in ('core','ent','run')}
den={s:gp(s)['den'] for s in ('core','ent','run')}
V2ent=0.0 if CFE else piece['ent']*den['ent']
print("pieces: core %+.5f ent %+.5f run %+.5f | dens: core %+.5f ent %+.5f run %+.5f"%(piece['core'],piece['ent'],piece['run'],den['core'],den['ent'],den['run']))
print("V2(ent) computed = %+.3e  [s97 declared 1.0e-3]"%(piece['ent']*den['ent']))
print("V2(core) piece x den = %+.3e SIGN-INCONSISTENT (F99.2); V2(run) = %+.3e SIGN-INCONSISTENT (s97 -6.5e-4 attributed)"%(piece['core']*den['core'],piece['run']*den['run']))
def rem(side,excl,blockval,coreblock):
    t=0.0
    for k,v in S[side].items():
        if any(x in excl for x in k.split('-')): continue
        c=S['core'].get(k,0.0)
        if k=='60-60': v=blockval; c=coreblock
        t+=v-c
    return t
for V2c in (0.0,1.2e-3):
    for V2r in (0.0,1.1e-3):
        bc=EXCL['core']+twostate(D['core'],V2c)+(0.01 if CFC else 0.0)
        be=EXCL['ent']+twostate(D['ent'],V2ent)
        br=EXCL['run']+twostate(D['run'],V2r)
        dcc=rem('run',{'61'},br,bc)-rem('ent',{'52'},be,bc)
        print("corner V2(core)=%.1e V2(run)=%.1e: block c/e/r %+.5f/%+.5f/%+.5f  dcc %+.5f  dm2 %+.5f = %.2fx margin %s"%(
            V2c,V2r,bc,be,br,dcc,dD2+dcc,(dD2+dcc)/m,'NO FLIP' if dD2+dcc>0 else 'FLIP'))
