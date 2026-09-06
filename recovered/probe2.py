import sys, os, math, numpy as np
R='/home/claude/s88'
for p in ('pack87','pack86','pack85','pack84','pack83','pack81','rt'): sys.path.insert(0, os.path.join(R,p))
import semi87 as S87, semi85 as S85, semi84 as S84, gtest83 as G
from scipy.integrate import cumulative_trapezoid as ct
def screen(r, shells):
    s=np.zeros_like(r)
    for (P,occ) in shells:
        P2=np.asarray(P)**2
        inner=ct(P2, r, initial=0.0)
        outer=ct((P2/r)[::-1], -r[::-1], initial=0.0)[::-1]
        s+=occ*(inner + r*outer)
    return s
for Z in (24, 56):
    h,cfg,ent,eps,row,E=S84.field_of(Z); r=np.asarray(h.r,float)
    rr,q=S85.q_native(h,3,2)
    sc=screen(r,[(h.cP[k],h.cQ[k]) for k in h.cQ])
    qq=Z-sc
    print(Z, 'Z-screen vs q_native: max|diff|=%.3e  q[0]=%.4f q[-1]=%.4f  N=%.1f'%(np.abs(qq-q).max(), q[0], q[-1], sum(h.cQ.values())))
    rr2,q2=S85.q_native(h,5,0); print('   q depends on channel? max|q(3,2)-q(5,0)|=%.2e'%np.abs(q-q2).max())