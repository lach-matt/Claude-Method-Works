import sympy as sp, pickle, time
t0=time.time()
v,r,th,e,mu=sp.symbols('v r theta e mu',positive=True)
S,Cc=sp.symbols('S Cc',positive=True)   # sin, cos of theta
res=pickle.load(open('hlin.pkl','rb'))
a,b,cc,dps,dom=[sp.Function(n)(v,r,th) for n in ('a','b','cc','dps','dom')]
def tri(ex):
    ex=sp.expand_trig(ex)
    return ex.subs({sp.sin(th):S,sp.cos(th):Cc})
# generic separated forms: P-profile r^-3/2 * p(theta) * Phi(v); unknown radial-angular functions
Phi=sp.Function('Phi')(v)
p1,p2=sp.Function('p1')(th),sp.Function('p2')(th)   # psi- and omega- angular profiles
k=sp.Rational(-3,2)
Cf=sp.Function('C')(r,th); Af=sp.Function('A')(r,th)
sub={dps:p1*r**k*Phi, dom:p2*r**k*Phi, b:2*p1*r**k*Phi*r**4*sp.sin(th)**2*sp.cos(th)**2, cc:Cf*Phi, a:Af*Phi}
out={}
for jk in [(1,2),(2,2),(0,2),(0,1)]:
    ex=res[jk][1].subs(sub).doit()
    out[jk]=sp.simplify(ex)
    print(jk,round(time.time()-t0,1),flush=True)
pickle.dump(out,open('hsolve2.pkl','wb'))
# r-theta: collect C derivatives
E=sp.expand(sp.numer(sp.together(out[(1,2)])))
print('rt C_rr coeff',sp.factor(E.coeff(sp.Derivative(Cf,(r,2)))))
print('rt C_r coeff',sp.factor(E.coeff(sp.Derivative(Cf,r))))
