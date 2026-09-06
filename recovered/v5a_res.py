import sys,os,numpy as np,scipy.linalg as sla
sys.argv=['v5a.py','ent','--lmax','-1']; exec(open('v5a.py').read().split("out={}")[0])
sys.path.insert(0,os.path.join(HERE,"..","pack94")); import so94
a=(7,0); n,l=a; Vl,Xs=so94.pot(g,a)
u,e_re,nd,res=g.solve_one(l,n,Vl,Xs,eps[a],P[a]); print("RESOLVE shooter with converged source: e %.7f vs eps %.7f  d %+.1e  |u-P| %.1e"%(e_re,eps[a],e_re-eps[a],np.max(abs(u-P[a]))))
Vp_,Vpp_=_derivs(x,Vl); E0=eps[a]; M=1+(E0-Vl)/(2*c*c); Mp=-Vp_/(2*c*c); Mpp=-Vpp_/(2*c*c); Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
q=(l+0.5)**2+r*r*(2*M*(Vl-E0)+Dref); y=P[a]/np.sqrt(r); s=-2*M*r**1.5*Xs
# discrete residual of the sealed P in the Numerov equation: D2 y - f(q y + s)
f=np.eye(N)+h*h*D2/12.0; R=D2@y-f@(q*y+s); R3=D2@y-(q*y+s)
# where is the residual?  energy-weighted: <y| R>/<y|B y>
Bd=2*r*r*M; print("residual norms: numerov %.2e  3pt %.2e ; |y| %.2e"%(np.max(abs(R[5:-5])),np.max(abs(R3[5:-5])),np.max(abs(y))))
print("implied dE (numerov) = -<y,R>/<y,B y> = %+.2e"%(-np.sum(y*R)/np.sum(y*Bd*y)))
for lo,hi in ((1e-6,1e-3),(1e-3,1e-1),(1e-1,1),(1,10),(10,300)):
    m=(r>lo)&(r<hi); print("  r in [%g,%g): sum y*R = %+.2e"%(lo,hi,np.sum((y*R)[m])))