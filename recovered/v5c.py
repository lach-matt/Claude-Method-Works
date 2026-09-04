#!/usr/bin/env python3
"""v5c.py -- S96 ITEM 1: v5a.py generalised to any chain row, Zeno-segmented per l. Construction IDENTICAL to pack95/v5a.py (stencil read, not memory).
usage: v5c.py Z SIDE --l L [--lmax 6]     SIDE in {core, ent, run}: core = cfg(Z-1) from the sealed chain; ent/run = core + the sealed order[0]/order[1] shell.
  --l L   : compute the spectrum for one l only (one eigensolve 4000^2 per call; ~30-50 s) -> pack96/v5c-Z-SIDE-lL.npz
  --occ   : solve only, write occupied P/eps -> pack96/v5c-Z-SIDE-occ.npz (used by the V^{N-1} assembly v5d.py)
Spectrum operator: V^N of the SIDE object (all occupied shells at full Q), E_ref = 0, roots kept < 150 Ha, as v5a."""
import sys, os, json, time, numpy as np, scipy.linalg as sla
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','rt')); os.chdir(os.path.join(HERE,'..','rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0, _derivs
from t7b_hf import _c3j0sq
assert H.CORR is False
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
Z=int(sys.argv[1]); side=sys.argv[2]
lsel=int(sys.argv[sys.argv.index('--l')+1]) if '--l' in sys.argv else None
occonly='--occ' in sys.argv
cfg=NC.cfg_from_chain(Z-1,ROWS); row=ROWS[Z]
def nl(s): return (int(s[0]),'spdf'.index(s[1]))
if side=='ent': cfg=NC.add(cfg,nl(row['order'][0][0]))
if side=='run': cfg=NC.add(cfg,nl(row['order'][1][0]))
assert side in ('core','ent','run')
def solve(Z,cfg):
    for rung,(beta,maxit) in enumerate(NG.LADDER):
        g=H.HFC(Z,[tuple(x) for x in cfg],c=C0); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
        if it<maxit: return g,float(E),rung,it
    raise RuntimeError
t0=time.time(); g,E,rung,it=solve(Z,cfg); print("solved Z=%d %s E=%.5f rung %d it %d (%.1fs) occ=%s"%(Z,side,E,rung,it,time.time()-t0,g.occ),flush=True)
r,x,h,dr,N=g.r,g.x,g.h,g.dr,g.npts; P=g.P; eps=g.eps; keys=[(n,l) for n,l,q in g.occ]; Q={(n,l):q for n,l,q in g.occ}; c=C0
tag='v5c-%d-%s'%(Z,side)
if occonly:
    np.savez(os.path.join(HERE,tag+'-occ.npz'),r=r,dr=dr,eps=json.dumps({str(k):v for k,v in eps.items()}),occ=json.dumps(g.occ),E=E,**{('P%d%d'%k):P[k] for k in keys})
    print("wrote",tag+'-occ.npz'); sys.exit(0)
Y0={k:g.Yk(P[k],P[k],0) for k in keys}; Vdir=-Z/r+sum(Q[b]*Y0[b]/r for b in keys)
def Gk(k):
    ri=r[:,None]; rj=r[None,:]; lo=np.minimum(ri,rj); hi=np.maximum(ri,rj); return lo**k/hi**(k+1)
def exch_S(l):
    S=np.zeros((N,N))
    for b in keys:
        nb,lb=b
        for k in range(abs(l-lb),l+lb+1,2):
            coef=0.5*Q[b]*_c3j0sq(l,k,lb)
            if coef>1e-14: S+=coef*(P[b][:,None]*Gk(k)*P[b][None,:])
    return S
D2=(np.diag(-2*np.ones(N))+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1))/(h*h)
FD2=np.linalg.solve(np.eye(N)+h*h*D2/12.0,D2); FD2=0.5*(FD2+FD2.T)
Vp,Vpp=_derivs(x,Vdir)
def build(l,Eref,S):
    M=1+(Eref-Vdir)/(2*c*c); Mp=-Vp/(2*c*c); Mpp=-Vpp/(2*c*c)
    Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
    A=-FD2+np.diag((l+0.5)**2+r*r*(2*M*Vdir+Dref)); Bd=2*r*r*M; Bi=1/np.sqrt(Bd)
    C=A*Bi[:,None]*Bi[None,:]; C-=np.sqrt(r)[:,None]*S*np.sqrt(r)[None,:]*h
    C=0.5*(C+C.T); return C,Bi
l=lsel; t1=time.time(); S=exch_S(l)
occ_l=[a for a in keys if a[1]==l]
for a in occ_l[-1:]:
    C,Bi=build(l,eps[a],S); w,v=sla.eigh(C); j=np.argmin(abs(w-eps[a]))
    y=v[:,j]*Bi; F=np.sqrt(r)*y; F/=np.sqrt(np.sum(F*F*dr)); ov=abs(np.sum(F*P[a]*dr))
    print("  check l=%d %s: sealed eps %.6f  lin %.6f  dE %+.2e  overlap %.6f  (aoc=%s)"%(l,a,eps[a],w[j],w[j]-eps[a],ov,"OPEN" if Q[a]<2*(2*l+1) else "closed"),flush=True)
C,Bi=build(l,0.0,S); w,v=sla.eigh(C)
print(" l=%d E_ref 0: %d neg, %d < 20 Ha, %d < 100 Ha; lowest %s  (%.1fs)"%(l,int(np.sum(w<0)),int(np.sum(w<20)),int(np.sum(w<100)),np.round(w[:4],4),time.time()-t1),flush=True)
keep=w<150; F=(np.sqrt(r)[:,None]*(v[:,keep]*Bi[:,None])); F/=np.sqrt(np.sum(F*F*dr[:,None],0))
np.savez(os.path.join(HERE,'%s-l%d.npz'%(tag,l)),w=w[keep],F=F)
print("wrote %s-l%d.npz"%(tag,l),flush=True)