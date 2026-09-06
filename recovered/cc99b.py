#!/usr/bin/env python3
"""cc99b.py -- S99 Item 2: row 89 through the filed remainder rule + ent-side own-slot block.
V^2 candidates: (a) COMPUTED piece x sealed-eps den (instrument-source-consistent), (b) s97 declared 2.13e-2 (E_PT x 0.47, provenance under F99.3), (c) 0 (can-fail lever).
usage: cc99b.py"""
import json,os,math
HERE=os.path.dirname(os.path.abspath(__file__)); P=os.path.join(HERE,'..','pack96')
def ck(s): return json.load(open(os.path.join(P,'v5d-89-%s.e2w-ck-20-l6.json'%s)))
def parts(s,r): return json.load(open(os.path.join(P,'v5d-89-%s.e2%s-20.json'%(s,r))))['parts']
def twostate(D,V2): return (D-math.sqrt(D*D+4*V2))/2
S={s:ck(s) for s in ('core','ent','run')}
exw=parts('ent','w'); exx=parts('ent','')
E2w_ent=S['ent']['70-70']; excl_ent=exx['70-70']
assert abs(exw['70-70']-E2w_ent)<1e-9, (exw['70-70'],E2w_ent)   # ck vs parts consistency
piece=E2w_ent-excl_ent
den=json.load(open(os.path.join(HERE,'gap99a89-ent.json')))['den']
Dcfg=0.12668; dD2,m=0.04121,0.03233
print("E2w(ent,70-70) %+.5f  excl %+.5f  piece(E_PT) %+.5f  [s97 -0.04538]"%(E2w_ent,excl_ent,piece))
print("den(sealed-eps rule) %+.5f -> V^2 computed %+.4e ; s97 declared 2.13e-2 (piece x 0.47, F99.3)"%(den,piece*den))
def rem(side,excl,entblock):
    t=0.0
    for k,v in S[side].items():
        if any(x in excl for x in k.split('-')): continue
        c=S['core'].get(k,0.0)
        if side=='ent' and k=='70-70' and entblock is not None: v=entblock
        t+=v-c
    return t
r=rem('run',{'71'},None)
dcc_pt=r-rem('ent',{'62'},None)
print("PR1 dcc_PT (no resummation) %+.5f  [s96/s97 +0.06616]"%dcc_pt)
for tag,V2 in (('computed',piece*den),('s97-declared',2.13e-2),('canfail-0',0.0)):
    b=excl_ent+twostate(Dcfg,V2)
    dcc=r-rem('ent',{'62'},b)
    print("%-12s V2 %.3e two-state %+.5f block %+.5f  dcc %+.5f  dm2 %+.5f = %.2fx margin %s"%(
        tag,V2,twostate(Dcfg,V2),b,dcc,dD2+dcc,(dD2+dcc)/m,'NO FLIP' if dD2+dcc>0 else 'FLIP'))