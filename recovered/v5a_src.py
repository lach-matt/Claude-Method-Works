import sys,os,numpy as np,scipy.linalg as sla
sys.argv=['v5a.py','ent','--lmax','-1']; exec(open('v5a.py').read().split("out={}")[0])
Finv=np.linalg.inv(np.eye(N)+h*h*D2/12.0)
for a in [(7,0),(6,2)]:
    n,l=a; Vl=-Z/r+sum((Q[b] if b!=a else g._ceff(a,Q))*Y0[b]/r for b in keys); cc=g._ceff(a,Q)*(2*l+1)/(4*l+1)
    for k in range(2,2*l+1,2): Vl=Vl-cc*_c3j0sq(l,k,l)*g.Yk(P[a],P[a],k)/r
    S=np.zeros((N,N))
    for b in keys:
        if b==a: continue
        nb,lb=b
        for k in range(abs(l-lb),l+lb+1,2):
            coef=0.5*Q[b]*_c3j0sq(l,k,lb)
            if coef>1e-14: S+=coef*(P[b][:,None]*Gk(k)*P[b][None,:])
    Vp_,Vpp_=_derivs(x,Vl); E0=eps[a]; M=1+(E0-Vl)/(2*c*c); Mp=-Vp_/(2*c*c); Mpp=-Vpp_/(2*c*c); Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
    A=-FD2+np.diag((l+0.5)**2+r*r*(2*M*Vl+Dref)); Bi=1/np.sqrt(2*r*r*M)
    EX=2*M[:,None]*r[:,None]**1.5*S*np.sqrt(r)[None,:]*r[None,:]*h      # exchange in y-space (unscaled): 2 M r^1.5 S r^0.5 dr
    for tag,EXm in (("f on source",EX),("NO f on source -> f^-1 EX",Finv@EX)):
        C=(A-EXm)*Bi[:,None]*Bi[None,:]; C=0.5*(C+C.T); w=sla.eigvalsh(C); j=np.argmin(abs(w-E0))
        print("SRC",a,tag,": sealed %.7f lin %.7f dE %+.2e"%(E0,w[j],w[j]-E0),flush=True)