# Check for Part VI.B Lemma 1.1: g_KS^{-1}(dr_A, dr_A) = (P(r) - mu r^2)/(r^2 Sigma) for Myers-Perry in III.B's
# Kerr-Schild form, in the rotated frame A = a J12 + b J34, on the spheroidal parametrisation of {r_A = r}.
import sympy as sp
x1,x2,x3,x4,a,b,mu,y=sp.symbols('x1 x2 x3 x4 a b mu y',real=True)
th,ph,ps=sp.symbols('theta phi psi',real=True); rr=sp.Symbol('rr',positive=True)
X=sp.Matrix([x1,x2,x3,x4]); A=sp.zeros(4); A[0,1]=a; A[1,0]=-a; A[2,3]=b; A[3,2]=-b
s=a**2+b**2; p2=a**2*b**2; X2=(X.T*X)[0]; AX2=((A*X).T*(A*X))[0]
Q=y**2+(s-X2)*y+p2-s*X2+AX2                       # III.B Lemma 3.1 (b), y = r^2
grad_r=[-sp.diff(Q,v)/sp.diff(Q,y)/(2*rr) for v in (x1,x2,x3,x4)]
P=(y+a**2)*(y+b**2); Minv=(y*sp.eye(4)-A*A).inv()
ell=Minv*(rr*sp.eye(4)+A)*X                       # M(rI+A)x/P = (r^2-A^2)^{-1}(r+A)x
F=1+((X.T*A*A*(P*Minv)*(P*Minv)*X)[0])/P**2; H=mu*y/(P*F)
ginv=sum(g**2 for g in grad_r)-H*sum(ell[i]*grad_r[i] for i in range(4))**2   # III.B Lemma 3.3 (d)
sub={x1:sp.sqrt(y+a**2)*sp.sin(th)*sp.cos(ph), x2:sp.sqrt(y+a**2)*sp.sin(th)*sp.sin(ph),
     x3:sp.sqrt(y+b**2)*sp.cos(th)*sp.cos(ps), x4:sp.sqrt(y+b**2)*sp.cos(th)*sp.sin(ps)}
assert sp.simplify(Q.subs(sub))==0
e=ginv.subs(sub).subs(y,rr**2)
Sig=rr**2+a**2*sp.cos(th)**2+b**2*sp.sin(th)**2
assert sp.simplify(sp.trigsimp(sp.together(e-(P.subs(y,rr**2)-mu*rr**2)/(rr**2*Sig))))==0
print('horizon5 check passes')
