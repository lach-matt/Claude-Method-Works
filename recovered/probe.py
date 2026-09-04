import sys, os, math, numpy as np
R='/home/claude/s88'
for p in ('pack87','pack86','pack85','pack84','pack83','pack81','rt'): sys.path.insert(0, os.path.join(R,p))
import semi87 as S87, semi85 as S85, semi84 as S84, gtest83 as G
Z=24
h,cfg,ent,eps,row,E=S84.field_of(Z); core=S87.core_numbers(h); r=core['r']; rho=core['rho_r']
print('shells', {k:(v, round(float(np.trapezoid(r*np.asarray(h.cP[k])**2, r)/core['norms'][k]),3)) for k,v in h.cQ.items()})
for c in sorted(G.channels(row,lmax=3), key=lambda c:c['nu'])[:3]:
    n,l,Ec=c['n'],c['l'],float(c['D']); rr,q=S85.q_native(h,n,l); Rw=S85.channel_row(Ec,l,rr,q)
    if Rw is None: continue
    L=l+0.5; u1,u2=1/Rw['r_out'],1/Rw['r_in']; a=u2-u1
    t=np.linspace(0,1,20001); u=u1+a*t; rt=1/u
    sig=2*np.interp(np.log(rt), np.log(r), r*r*rho)/L**2
    print(c['tag'], 'K=%.5f  int sigma=%.5f  b0=%.4f b1=%.4f  min sig=%.4f max %.3f'%(Rw['K'], np.trapezoid(sig,t), Rw['b0'],Rw['b1'],sig.min(),sig.max()))