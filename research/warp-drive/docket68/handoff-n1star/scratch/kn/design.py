import numpy as np, sympy as sp
z=sp.symbols('z',positive=True)
def check(q,zc,c=1,gfac=1.0,zb=1.15):
    zs=c*z**q*(zc**2-z**2)**2; sg=sp.simplify(zs/z)
    ap=3*c*z**q*(zc**2-z**2)**2*gfac
    al=sp.integrate(ap,(z,0,z))
    Fm=1-1/z**2
    qvv=ap; qvr=ap*Fm+3*sg/z; qrr=sp.Rational(1,2)*(-Fm*sp.diff(sg,z)+3*sg/z-sg/z**3); qtt=sp.diff(z*sg,z)/(2*z**3)
    tl=al*Fm+2*sg
    f=sp.lambdify(z,[qvv,qvr,qrr,qtt,tl,al,sg,4*qvv*qrr-qvr**2],'numpy')
    Z=np.linspace(1e-3,zc-1e-6,20000); V=f(Z)
    inner=Z<=zb
    ok=dict(timelike=bool(np.all(V[4]>0)), qvv=bool(np.all(V[0]>0)), qtt_inner=bool(np.all(V[3][inner]>0)), det=bool(np.all(V[7]>=0)), det_min_inner=float(np.min((V[7]/np.maximum(V[0],1e-300))[inner&(Z>0.05)])))
    zqtt=Z[np.argmax(V[3]<0)] if np.any(V[3]<0) else None
    return ok, zqtt, float(sp.N(al.subs(z,zc)))
for q in (2.5,3,4):
    for zc in (1.4,1.6,2.0):
        print(q,zc,check(q,zc))
