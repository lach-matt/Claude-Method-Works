#!/usr/bin/env python3
"""tab95.py -- S95 ITEM 2. Tabulation only: exchange-projected zeta (zeta_x) as a second full column for so94 (r_x) and jsel94 (J1-J4 under zeta_x).
Consumes pack94/so94.jsonl + rt/nlchain.jsonl. NO solve. usage: tab95.py [--canfail A|B]  rc=4 on a fired can-fail."""
import sys,os,json
HERE=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(HERE,'..')
SO={json.loads(l)['Z']:json.loads(l) for l in open(os.path.join(R,'pack94','so94.jsonl'))}
NL={json.loads(l)['Z']:json.loads(l) for l in open(os.path.join(R,'rt','nlchain.jsonl'))}
cf=sys.argv[sys.argv.index('--canfail')+1] if '--canfail' in sys.argv else None
def jsel(key):
    out={}
    for Z in range(109,121):
        s=SO[Z]; l=s['l']; z=s[key]
        if cf=='B' and key=='zeta_x' and Z==115: z*=10
        D=NL[Z]['D_ent']; run,Dr=NL[Z]['order'][1]
        lo=D-z*(l+1)/2 if l>0 else D; hi=D+z*l/2 if l>0 else D
        out[Z]=dict(run=run,z=z,m_lo=Dr-lo,m_hi=Dr-hi,lo=lo,hi=hi)
    J1=sum(1 for Z in range(109,119) if out[Z]['lo']<out[Z]['hi'])
    J2=sum(1 for Z in range(113,119) if out[Z]['m_lo']>0)
    J3=sum(1 for Z in range(115,119) if out[Z]['m_hi']>0)
    J4=sum(1 for Z in range(109,113) if out[Z]['m_hi']>0)
    return out,(J1,J2,J3,J4)
# Table 1: so94 two-column r
print("# so94 two-column: Z ent l  zeta_loc  zeta_x  ratio  r_loc  r_x  m(Z)")
nscored=0; maxr=[0,0]; cross=[None,None]; diff=0.0
for Z in sorted(SO):
    s=SO[Z]; l=s['l']
    zl,zx=s['zeta_loc'],s['zeta_x']
    if cf=='A': zx=zl
    m=s['margin']; rl=zl*(2*l+1)/2/m if l>0 else 0.0; rx=zx*(2*l+1)/2/m if l>0 else 0.0
    diff=max(diff,abs(rl-rx))
    if l>0 and Z<=108:
        nscored+=1; maxr=[max(maxr[0],rl),max(maxr[1],rx)]
    for i,r in enumerate((rl,rx)):
        if l>0 and r>=1 and cross[i] is None: cross[i]=Z
    print(" %3d %-3s %d  %.5f %.5f %.3f  %.3f %.3f  %.5f"%(Z,s['ent'],l,zl,zx,(zx/zl if zl else 1),rl,rx,m))
print("SCORED l>0 rows Z<=108: %d  max r_loc %.3f  max r_x %.3f  first r>=1: loc %s  x %s"%(nscored,maxr[0],maxr[1],cross[0],cross[1]))
# Table 2: jsel under both
jl,Jl=jsel('zeta_loc'); jx,Jx=jsel('zeta_x')
print("# jsel two-column: Z ent run | loc: m_lo m_hi | x: m_lo m_hi")
for Z in range(109,121):
    print(" %3d %-3s %-3s | %+.5f %+.5f | %+.5f %+.5f"%(Z,SO[Z]['ent'],jl[Z]['run'],jl[Z]['m_lo'],jl[Z]['m_hi'],jx[Z]['m_lo'],jx[Z]['m_hi']))
print("J1-J4 loc %s  x %s"%(Jl,Jx))
# 7p block r uniformity (open question, not residue)
blk=[SO[Z] for Z in range(113,119)]
rs=[b['zeta_loc']*3/2/b['margin'] for b in blk]
print("7p block r_loc 113-118: "+" ".join("%.3f"%r for r in rs)+"  spread %.3f  zeta ratio 118/113 %.2f  m ratio 118/113 %.2f"%(max(rs)-min(rs),blk[-1]['zeta_loc']/blk[0]['zeta_loc'],blk[-1]['margin']/blk[0]['margin']))
if cf=='A':
    print("CF-A: zeta_x := zeta_loc -> max|r_loc-r_x| = %.2e (column dead)"%diff); sys.exit(4 if diff<1e-12 else 1)
if cf=='B':
    print("CF-B: zeta_x x10 at 115 -> J3_x = %d (J3_loc %d)"%(Jx[2],Jl[2])); sys.exit(4 if Jx[2]<Jl[2] else 1)
json.dump(dict(J_loc=Jl,J_x=Jx,maxr=maxr,cross=cross,r7p=rs),open(os.path.join(HERE,'tab95.json'),'w'))