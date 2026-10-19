import sympy as sp, pickle, time
t0=time.time()
v,r,th,mu=sp.symbols('v r theta mu',positive=True)
res=pickle.load(open('hlin.pkl','rb')); cp=pickle.load(open('hsolve3.pkl','rb'))['cp']
d4=pickle.load(open('hsolve4.pkl','rb')); Q=d4['Q']
a,b,cc,dps,dom=[sp.Function(n)(v,r,th) for n in ('a','b','cc','dps','dom')]
Phi=sp.Function('Phi')(v); p1,p2=sp.Function('p1')(th),sp.Function('p2')(th)
K=sp.Function('K')(v,th); M=sp.Function('M')(v,th)
k=sp.Rational(-3,2)
# A particular: r^2 * int Q/r^2 dr
Qe=sp.expand(sp.simplify(Q))
terms=sp.Add.make_args(Qe)
Ip=0
for t in terms:
    Ip+=sp.integrate(t/r**2,r)
Apart=sp.simplify(r**2*Ip)
print('A particular:',Apart, round(time.time()-t0,1))
Afull=Apart+M*r**2
sub={dps:p1*Phi*r**k, dom:p2*Phi*r**k, b:2*p1*Phi*r**k*r**4*sp.sin(th)**2*sp.cos(th)**2, cc:Phi*cp*r**sp.Rational(7,2)+K*r**2, a:Afull}
for jk,name in [((0,2),'vtheta'),((0,1),'vr')]:
    E=sp.expand(sp.simplify(res[jk][1].subs(sub).doit()))
    lead=sp.limit(E*r**0,r,sp.oo) if False else None
    # collect powers of r
    Ec=sp.collect(sp.expand(E),r,evaluate=False)
    print(name,'powers:',{p:sp.simplify(cf) for p,cf in Ec.items()})
    print(round(time.time()-t0,1),flush=True)
pickle.dump(dict(Apart=Apart),open('hsolve5.pkl','wb'))
