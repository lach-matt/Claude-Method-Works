import sympy as sp, pickle, time
t0=time.time()
v,r,th,mu=sp.symbols('v r theta mu',positive=True)
res=pickle.load(open('hlin.pkl','rb')); cp=pickle.load(open('hsolve3.pkl','rb'))['cp']
a,b,cc,dps,dom=[sp.Function(n)(v,r,th) for n in ('a','b','cc','dps','dom')]
Phi=sp.Function('Phi')(v); p1,p2=sp.Function('p1')(th),sp.Function('p2')(th)
K=sp.Function('K')(v,th); A=sp.Function('A')(v,r,th)
k=sp.Rational(-3,2)
sub={dps:p1*Phi*r**k, dom:p2*Phi*r**k, b:2*p1*Phi*r**k*r**4*sp.sin(th)**2*sp.cos(th)**2, cc:Phi*cp*r**sp.Rational(7,2)+K*r**2, a:A}
E=sp.numer(sp.together(res[(2,2)][1].subs(sub).doit()))
E=sp.expand(E)
cAr=sp.factor(E.coeff(sp.Derivative(A,r))); cA=sp.factor(sp.expand(E.subs(sp.Derivative(A,r),0)).coeff(A))
rest=sp.expand(E.subs(sp.Derivative(A,r),0).subs(A,0))
print('A_r coeff',cAr); print('A coeff',cA); print(round(time.time()-t0,1))
# ODE A_r + (cA/cAr) A = -rest/cAr
P=sp.simplify(cA/cAr); Q=sp.simplify(-rest/cAr)
print('P',P)
pickle.dump(dict(P=P,Q=Q),open('hsolve4.pkl','wb'))
