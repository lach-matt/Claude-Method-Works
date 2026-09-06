# check with the SHELL'S OWN sealed operator (hfc2.run2 form): Vloc_a (ceff, local self-exchange) in M and in 2MV; nonlocal exchange b != a only.
import sys,os,numpy as np,scipy.linalg as sla
sys.argv=['v5a.py','ent','--lmax','-1']; exec(open('v5a.py').read().split("out={}")[0])
def own(a):
    n,l=a; Vloc=-Z/r+sum((Q[b] if b!=a else g._ceff(a,Q))*Y0[b]/r for b in keys)
    cc=g._ceff(a,Q)*(2*l+1)/(4*l+1)
    for k in range(2,2*l+1,2): Vloc=Vloc-cc*_c3j0sq(l,k,l)*g.Yk(P[a],P[a],k)/r
    S=np.zeros((N,N))
    for b in keys:
        if b==a: continue
        nb,lb=b
        for k in range(abs(l-lb),l+lb+1,2):
            coef=0.5*Q[b]*_c3j0sq(l,k,lb)
            if coef>1e-14: S+=coef*(P[b][:,None]*Gk(k)*P[b][None,:])
    return Vloc,S
for a in [(1,0),(4,0),(7,0),(2,1),(6,2)]:
    n,l=a; Vl,S=own(a); Vp_,Vpp_=_derivs(x,Vl); Eref=eps[a]
    M=1+(Eref-Vl)/(2*c*c); Mp=-Vp_/(2*c*c); Mpp=-Vpp_/(2*c*c); Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
    A=-FD2+np.diag((l+0.5)**2+r*r*(2*M*Vl+Dref)); Bd=2*r*r*M; Bi=1/np.sqrt(Bd)
    C=A*Bi[:,None]*Bi[None,:]; C-=np.sqrt(r)[:,None]*S*np.sqrt(r)[None,:]*h; C=0.5*(C+C.T)
    w,v=sla.eigh(C); j=np.argmin(abs(w-eps[a])); y=v[:,j]*Bi; F=np.sqrt(r)*y; F/=np.sqrt(np.sum(F*F*dr)); ov=abs(np.sum(F*P[a]*dr))
    print("OWN",a,"sealed %.6f lin %.6f dE %+.2e rel %.1e overlap %.7f"%(eps[a],w[j],w[j]-eps[a],(w[j]-eps[a])/abs(eps[a]),ov),flush=True)