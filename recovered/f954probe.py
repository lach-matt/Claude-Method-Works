#!/usr/bin/env python3
"""f954probe.py -- S99 Item 3 (F95.4 locus test). v5a build copied VERBATIM; one flag restores sqrt(M_i/M_j).
Row-89 core side, outermost shell of one l per call (Zeno). Sealed v5a untouched. usage: f954probe.py L"""
import sys,os,json,time,numpy as np,scipy.linalg as sla
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','rt')); os.chdir(os.path.join(HERE,'..','rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0, _derivs
from t7b_hf import _c3j0sq
ltest=int(sys.argv[1])
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
Z=88; cfg=NC.cfg_from_chain(88,ROWS)   # core side, row 89
def solve(Z,cfg):
    for beta,maxit in NG.LADDER:
        g=H.HFC(Z,[tuple(x) for x in cfg],c=C0); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
        if it<maxit: return g,E
    raise RuntimeError
t0=time.time(); g,E=solve(Z,cfg); print("solved core E=%.5f (%.1fs)"%(E,time.time()-t0),flush=True)
r,x,h,dr,N=g.r,g.x,g.h,g.dr,g.npts; P=g.P; eps=g.eps; keys=[(n,l) for n,l,q in g.occ]; Q={(n,l):q for n,l,q in g.occ}; c=C0
print("grid: N=%d  max|dr/(r*h)-1| = %.3e"%(N,float(np.max(np.abs(dr/(r*h)-1)))),flush=True)
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
def build(l,Eref,S,unsym):
    M=1+(Eref-Vdir)/(2*c*c); Mp=-Vp/(2*c*c); Mpp=-Vpp/(2*c*c)
    Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
    A=-FD2+np.diag((l+0.5)**2+r*r*(2*M*Vdir+Dref)); Bd=2*r*r*M; Bi=1/np.sqrt(Bd)
    C=A*Bi[:,None]*Bi[None,:]
    X=np.sqrt(r)[:,None]*S*np.sqrt(r)[None,:]*h
    if unsym:
        sm=np.sqrt(M); C=0.5*(C+C.T)-sm[:,None]*X/sm[None,:]      # exact sqrt(M_i/M_j) factor; direct part symmetrised as filed
    else:
        C-=X; C=0.5*(C+C.T)
    return C,Bi
S=exch_S(ltest)
a=[k for k in keys if k[1]==ltest][-1]
for tag,unsym in (('sym',False),('unsym',True)):
    t1=time.time(); C,Bi=build(ltest,eps[a],S,unsym)
    if unsym: w=sla.eigvals(C); w=np.sort(np.real(w))
    else: w=sla.eigvalsh(C)
    j=int(np.argmin(np.abs(w-eps[a]))); dE=w[j]-eps[a]
    print("l=%d %s %-6s: sealed %.6f  lin %.6f  dE %+.3e  rel %.3e  (%.1fs)"%(ltest,a,tag,eps[a],w[j],dE,abs(dE/eps[a]),time.time()-t1),flush=True)
