import sys, os, json, numpy as np, scipy.linalg as sla
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt')); os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0, _derivs
from t7b_hf import _c3j0sq
npts=int(sys.argv[1])
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
Z=88; cfg=NC.cfg_from_chain(88,ROWS)
for beta,maxit in NG.LADDER:
    g=H.HFC(Z,[tuple(x) for x in cfg],npts=npts,c=C0); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
    if it<maxit: break
r,x,h,dr,N=g.r,g.x,g.h,g.dr,g.npts; P=g.P; keys=[(n,l) for n,l,q in g.occ]; Q={(n,l):q for n,l,q in g.occ}; c=C0
Y0={k:g.Yk(P[k],P[k],0) for k in keys}; Vdir=-Z/r+sum(Q[b]*Y0[b]/r for b in keys)
a=[k for k in keys if k[1]==0][-1]; l=0
def Gk(k):
    ri=r[:,None]; rj=r[None,:]; lo=np.minimum(ri,rj); hi=np.maximum(ri,rj); return lo**k/hi**(k+1)
S=np.zeros((N,N))
for b in keys:
    nb,lb=b
    for k in range(abs(l-lb),l+lb+1,2):
        coef=0.5*Q[b]*_c3j0sq(l,k,lb)
        if coef>1e-14: S+=coef*(P[b][:,None]*Gk(k)*P[b][None,:])
D2=(np.diag(-2*np.ones(N))+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1))/(h*h)
FD2=np.linalg.solve(np.eye(N)+h*h*D2/12.0,D2); FD2=0.5*(FD2+FD2.T)
Vp,Vpp=_derivs(x,Vdir); Eref=eps[a]
M=1+(Eref-Vdir)/(2*c*c); Mp=-Vp/(2*c*c); Mpp=-Vpp/(2*c*c)
Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
A=-FD2+np.diag((l+0.5)**2+r*r*(2*M*Vdir+Dref)); Bi=1/np.sqrt(2*r*r*M)
X=np.sqrt(r)[:,None]*S*np.sqrt(r)[None,:]*h; C0m=A*Bi[:,None]*Bi[None,:]
sm=np.sqrt(M); Cw=C0m-sm[:,None]*X
lam=None
Aop=Cw-eps[a]*np.eye(N); lu,piv=sla.lu_factor(Aop,overwrite_a=True); v=np.ones(N)/np.sqrt(N); lam=eps[a]
for _ in range(80):
    wv=sla.lu_solve((lu,piv),v); wv/=np.linalg.norm(wv)
    ln=float(wv@(Cw@wv))
    if abs(ln-lam)<1e-14: lam=ln; break
    lam=ln; v=wv
out=dict(npts=N,h=h,eps=float(eps[a]),lam=float(lam),dE=float(lam-eps[a]))
print("npts=%d h=%.4e dE_weighted=%+.6e"%(N,h,out['dE']),flush=True)
json.dump(out,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'g1w-%d.json'%N),'w'),indent=1)