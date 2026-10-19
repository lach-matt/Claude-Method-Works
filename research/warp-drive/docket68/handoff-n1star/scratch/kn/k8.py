import sympy as sp, numpy as np, pickle
v,r,th=sp.symbols('v r theta',positive=True)
Apart=pickle.load(open('hsolve6.pkl','rb'))['Apart']; cp=pickle.load(open('hsolve3.pkl','rb'))['cp']
Phi=sp.Function('Phi')(v); p1f,p2f=sp.Function('p1')(th),sp.Function('p2')(th)
mu=sp.Symbol('mu',positive=True)
s,c=sp.sin(th),sp.cos(th); hx=sp.sqrt(2/(1+sp.cos(2*th)**2))
pol={'F':(s**2*hx/3,-s**2*hx/2),'G':(c**2*hx/3,c**2*hx/2)}
fr,ft=sp.symbols('f_r f_t',real=True)
Fm=1-1/r**2; rhob=r**2*s*c
z=sp.Symbol('z',positive=True)
al=12*z**4-4*z**6+sp.Rational(3,8)*z**8
E={}
for name,(P1,P2) in pol.items():
    rep={p1f:P1,p2f:P2}
    Kf=sp.Function('K')(v,th); A_=(Apart.subs(Kf,0).doit()/Phi).subs(rep).doit().subs(mu,1)
    C_=(cp*r**sp.Rational(7,2)).subs(rep).doit()     # dh_vtheta per unit Phi
    B_=2*P1*r**sp.Rational(-3,2)*rhob**2             # dh_vr per unit Phi
    Tvv=fr**2; Tvr=Fm*fr**2/2-ft**2/(2*r**2); Tvt=fr*ft/r**2
    err=sp.Rational(1,2)*rhob**(-2)*(Tvv*A_+2*Tvr*B_+2*Tvt*C_)   # per unit alpha * Phi'
    E[name]=sp.lambdify((r,th),[sp.expand(err).coeff(fr,2).subs(ft,0),sp.expand(err).coeff(fr,1).coeff(ft,1),sp.expand(err).coeff(ft,2).subs(fr,0)],'numpy')
q=pickle.load(open('mq.pkl','rb')); e_=sp.Symbol('epsilon',positive=True)
Dq=sp.lambdify(z,sp.cancel(q['det'].subs(e_,0)/(4*q['qvv'])),'numpy'); qt=sp.lambdify(z,q['qtt'].subs(e_,0),'numpy'); alf=sp.lambdify(z,al,'numpy')
Z=np.linspace(0.005,1.2,600); TH=np.linspace(0.02,np.pi/2-0.02,181); PH=np.linspace(0,2*np.pi,73)
lam=np.zeros_like(Z)
for i,zz in enumerate(Z):
    worst=0
    for t in TH:
        eF=np.array(E['F'](zz,t)); eG=np.array(E['G'](zz,t))
        for ph in PH:
            e=alf(zz)*(np.cos(ph)*eF-np.sin(ph)*eG)       # Phi'_F = A env cos, Phi'_G = -A env sin  (A' = 1)
            # generalized eigen: max t s.t. err <= t Qmin; Qmin = diag(Dq, qt)
            Mq=np.array([[Dq(zz),0],[0,qt(zz)]]); Me=np.array([[abs(e[0]),abs(e[1])/2],[abs(e[1])/2,abs(e[2])]])
            L=np.linalg.cholesky(Mq); Li=np.linalg.inv(L)
            w=np.linalg.eigvalsh(Li@Me@Li.T).max()
            worst=max(worst,w)
    lam[i]=worst
print('max lambda (per unit A env mu^-1/4) on (0,1.2]:',lam.max(),'at z',Z[lam.argmax()])
print('absorption ratio at A env mu^-1/4 = 0.314:',0.314*lam.max())
for zz in (0.01,0.05,0.2,0.5,0.8,1.0,1.1,1.2): print(zz, float(np.interp(zz,Z,lam)))
pickle.dump(dict(Z=Z,lam=lam),open('k8.pkl','wb'))
