#!/usr/bin/env python3
"""jsel94.py -- S94 ITEM 3 (V3). First-order j-selection at rows 109-120 from so94.jsonl + sealed nlchain order. No new solve.
usage: jsel94.py [--canfail A|B]   rc=4 on a fired can-fail."""
import sys, os, json
HERE=os.path.dirname(os.path.abspath(__file__))
SO={json.loads(l)['Z']:json.loads(l) for l in open(os.path.join(HERE,'so94.jsonl'))}
NL={json.loads(l)['Z']:json.loads(l) for l in open(os.path.join(HERE,'..','rt','nlchain.jsonl'))}
cf=sys.argv[sys.argv.index('--canfail')+1] if '--canfail' in sys.argv else None
rows=[]
for Z in range(109,121):
    s=SO[Z]; n,l=s['n'],s['l']; z=s['zeta_loc']
    if cf=='A': z=0.0
    if cf=='B' and Z==115: z*=10
    D=NL[Z]['D_ent']; run_tag,D_run=NL[Z]['order'][1]
    lo=D - z*(l+1)/2 if l>0 else D; hi=D + z*l/2 if l>0 else D
    rows.append(dict(Z=Z,ent=s['ent'],run=run_tag,D=D,D_run=D_run,zeta=z,D_lo=lo,D_hi=hi,m_lo=D_run-lo,m_hi=D_run-hi))
    print(" %3d %-3s run %-3s D %8.5f D_run %8.5f zeta %7.5f  j=l-1/2 %8.5f (margin %+8.5f)  j=l+1/2 %8.5f (margin %+8.5f)"%(Z,s['ent'],run_tag,D,D_run,z,lo,D_run-lo,hi,D_run-hi))
J1=sum(1 for r in rows if 109<=r['Z']<=118 and r['D_lo']<r['D_hi'])
J2=sum(1 for r in rows if 113<=r['Z']<=118 and r['m_lo']>0)
J3=sum(1 for r in rows if 115<=r['Z']<=118 and r['m_hi']>0)
J4=sum(1 for r in rows if 109<=r['Z']<=112 and r['m_hi']>0)
print("J1 %d/10  J2 %d/6  J3 %d/4  J4 %d/4"%(J1,J2,J3,J4))
if cf=='A':
    same=all(abs(r['m_hi']-(r['D_run']-r['D']))<1e-12 for r in rows)
    print("CF-A: zeta=0 -> every j-margin equals the sealed margin:",same); sys.exit(4 if same else 1)
if cf=='B':
    r=[r for r in rows if r['Z']==115][0]
    print("CF-B: zeta x10 at 115 -> J3 margin %+.5f"%r['m_hi']); sys.exit(4 if r['m_hi']<0 else 1)
json.dump(rows,open(os.path.join(HERE,'jsel94.json'),'w'),indent=0)