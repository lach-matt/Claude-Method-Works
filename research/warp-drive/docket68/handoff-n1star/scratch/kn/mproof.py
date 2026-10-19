import sympy as sp, numpy as np
v,r,th,p1,p2=sp.symbols('v r theta phi1 phi2',real=True)
z,eps=sp.symbols('z epsilon',positive=True)
X=[v,r,th,p1,p2]
mu=sp.Function('mu')(v); Fm=1-mu/r**2
g=sp.zeros(5); g[0,0]=-Fm; g[0,1]=g[1,0]=1; g[2,2]=r**2; g[3,3]=r**2*sp.cos(th)**2; g[4,4]=r**2*sp.sin(th)**2
gi=sp.simplify(g.inv())
fv,fr,ft=sp.symbols('f_v f_r f_t',real=True); df=[fv,fr,ft,0,0]
grad2=sum(gi[a,b]*df[a]*df[b] for a in range(5) for b in range(5))
T=sp.Matrix(5,5,lambda a,b: df[a]*df[b]-sp.Rational(1,2)*g[a,b]*grad2); Tup=gi*T*gi
Z=sp.symbols('Z',positive=True)
alz=12*Z**4-4*Z**6+sp.Rational(3,8)*Z**8; sgz=Z**2*(4-Z**2)**2
zz=r/sp.sqrt(mu)
al=alz.subs(Z,zz); sg=sgz.subs(Z,zz)
Xv=[al,-sg,0,0,0]
pi=sp.Matrix(5,5,lambda a,b: sum(Xv[e]*sp.diff(g[a,b],X[e])+g[e,b]*sp.diff(Xv[e],X[a])+g[a,e]*sp.diff(Xv[e],X[b]) for e in range(5)))
K=sp.Rational(1,2)*sum(Tup[a,b]*pi[a,b] for a in range(5) for b in range(5))
m=sp.Symbol('m',positive=True); mp=sp.Symbol('mp',real=True)
K=K.subs(sp.Derivative(mu,v),mp).subs(mu,m)
K=sp.expand(sp.simplify(K.subs({r:z*sp.sqrt(m)}).subs(mp,eps*sp.sqrt(m))*sp.sqrt(m)))   # units sqrt(mu)=1
K=sp.expand(K.subs(m,1))
P=sp.Poly(K,fv,fr,ft); C={mo:sp.simplify(c) for mo,c in zip(P.monoms(),P.coeffs())}
qvv=C.get((2,0,0),0); qvr=C.get((1,1,0),0); qrr=C.get((0,2,0),0); qtt=C.get((0,0,2),0)
print('qvv',sp.factor(qvv)); print('qvr',sp.factor(qvr)); print('qrr',sp.factor(qrr)); print('qtt',sp.factor(qtt))
Fz=1-1/z**2
tl=sp.factor(alz.subs(Z,z)*Fz+2*sgz.subs(Z,z)); print('timelike',tl)
det=sp.factor(sp.together(4*qvv*qrr-qvr**2)); print('det',det)
import pickle; pickle.dump(dict(qvv=qvv,qvr=qvr,qrr=qrr,qtt=qtt,det=det,tl=tl),open('mq.pkl','wb'))
