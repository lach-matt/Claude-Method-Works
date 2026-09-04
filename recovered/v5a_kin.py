import sys,os,numpy as np,scipy.linalg as sla
sys.argv=['v5a.py','ent','--lmax','-1']; exec(open('v5a.py').read().split("out={}")[0])
a=(7,0); n,l=a; Vl=-Z/r+sum((Q[b] if b!=a else g._ceff(a,Q))*Y0[b]/r for b in keys)
u,e_sh,nd,res=g.solve_one(l,n,Vl,np.zeros(N),eps[a],P[a])      # sealed shooter, X=0
for tag,E0 in (("Eref=e_sh",e_sh),):
    Vp_,Vpp_=_derivs(x,Vl); M=1+(E0-Vl)/(2*c*c); Mp=-Vp_/(2*c*c); Mpp=-Vpp_/(2*c*c); Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
    for kin,KIN in (("3pt",D2),("numerov",FD2)):
        A=-KIN+np.diag((l+0.5)**2+r*r*(2*M*Vl+Dref)); Bi=1/np.sqrt(2*r*r*M); C=A*Bi[:,None]*Bi[None,:]; C=0.5*(C+C.T)
        w=sla.eigvalsh(C); j=np.argmin(abs(w-e_sh)); print("KIN",kin,"shooter %.7f lin %.7f dE %+.2e rel %.1e"%(e_sh,w[j],w[j]-e_sh,(w[j]-e_sh)/abs(e_sh)),flush=True)