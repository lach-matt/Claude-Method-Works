import sympy as sp, pickle
v,r,th,e,mu=sp.symbols('v r theta e mu',positive=True)
res=pickle.load(open('hlin.pkl','rb'))
a,b,cc,dps,dom=[sp.Function(n)(v,r,th) for n in ('a','b','cc','dps','dom')]
s,c=sp.sin(th),sp.cos(th)
hvr=r**4*s**2*c**2
Phi=sp.Function('Phi')(v)
x=sp.cos(2*th); hx=sp.sqrt(2/(1+x**2))
cases={'F':(s**2*hx*Phi*r**sp.Rational(-3,2)/3, -s**2*hx*Phi*r**sp.Rational(-3,2)/2),
       'G':(c**2*hx*Phi*r**sp.Rational(-3,2)/3,  c**2*hx*Phi*r**sp.Rational(-3,2)/2)}
C=sp.Function('C')(r,th); A_=sp.Function('A')(r,th)
for name,(P,O) in cases.items():
    sub={dps:P, dom:O, b:2*P*hvr, cc:C*Phi, a:A_*Phi}
    Ert=sp.simplify((res[(1,2)][1].subs(sub).doit())/Phi)
    print(name,'rtheta eq:',sp.factor(sp.simplify(Ert)))
