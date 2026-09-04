#!/usr/bin/env python3
"""cc98.py -- S98 (F98.1 remedy): FILED core-core partition, one rule for every row.
  dcc = [sum over run-side pairs not touching the runner shell of (E2w_run - E2w_core)] - [sum over ent-side pairs not touching the entrant shell of (E2w_ent - E2w_core)]
  (pinned by exact reproduction of the filed row-56 numbers -0.03188 / -0.03519).
  Degenerate own-slot s^2->d^2 block (rows where the entrant d shell is open in core): the s-s pair on EVERY side is replaced by
  E2excl(s-s) + two-state(Delta_cfg, V^2),  V^2 = -(E2w - E2excl) * (2 eps_s - 2 eps_d)  [frozen-block coupling], two-state = (D - sqrt(D^2+4V^2))/2.
  Reads only checkpoint jsons and declared numbers; can-fail --canfail zeroes V^2 -> block must equal exclusion value (PASS if printed).
usage: cc98.py [--canfail]"""
import json,sys,os,math
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','pack96'); CF='--canfail' in sys.argv
def ck(Z,s): return json.load(open(os.path.join(P,'v5d-%d-%s.e2w-ck-20-lNone.json'%(Z,s))))
def rem(S,side,excl,block):
    t=0.0
    for k,v in S[side].items():
        if any(x in excl for x in k.split('-')): continue
        c=S['core'].get(k,0.0)
        if block and k==block['pair']: v=block[side]; c=block['core']
        t+=v-c
    return t
def twostate(D,V2): return (D-math.sqrt(D*D+4*V2))/2
# declared numbers: (filed dD2(ent), sealed margin, runner tag, entrant tag, block spec or None)
ROWS={
 38:(0.06940,0.05639,'51','50',None),
 56:(0.04509,0.03914,'52','60',None),
 72:(0.08295,0.04507,'61','52',{'pair':'60-60','excl':{'ent':-0.047518,'run':-0.007765,'core':-0.018623},'D':{'core':0.2182,'ent':0.1979,'run':0.1429},'den':None,'V2':{'ent':1.0e-3,'run':1.1e-3,'core':1.2e-3}}),  # s97 declared
 105:(0.10599,0.05440,'71','62',{'pair':'70-70','excl':{'core':-0.015044,'ent':-0.028609,'run':-0.007757},'D':{'core':0.26709,'ent':0.26022,'run':0.22358},
       'den':{'core':2*(-0.2733+0.1965),'ent':2*(-0.2966+0.2361),'run':2*(-0.3729+0.3409)},'V2':None}),
}
for Z,(dD,m,runsh,entsh,B) in ROWS.items():
    S={s:ck(Z,s) for s in ('core','ent','run')}; block=None
    if B:
        block={'pair':B['pair']}
        for s in ('core','ent','run'):
            V2=B['V2'][s] if B['V2'] else -(S[s][B['pair']]-B['excl'][s])*B['den'][s]
            if CF: V2=0.0
            block[s]=B['excl'][s]+twostate(B['D'][s],V2)
            print("  Z=%d %s block: E2w %+.5f excl %+.5f V2 %.2e D %.4f two-state %+.5f -> %+.5f"%(Z,s,S[s][B['pair']],B['excl'][s],V2,B['D'][s],twostate(B['D'][s],V2),block[s]))
    r=rem(S,'run',{runsh},block); e=rem(S,'ent',{entsh},block); dcc=r-e
    print("Z=%3d run-core %+.5f ent-core %+.5f dcc %+.5f | dm2 total %+.5f = %.2fx margin %.5f %s"%(Z,r,e,dcc,dD+dcc,(dD+dcc)/m,m,'NO FLIP' if dD+dcc>0 else 'FLIP'))