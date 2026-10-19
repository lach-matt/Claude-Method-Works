import sympy as sp, pickle, time
t0=time.time()
v,r,th,mu=sp.symbols('v r theta mu',positive=True)
res=pickle.load(open('hlin.pkl','rb')); cp=pickle.load(open('hsolve3.pkl','rb'))['cp']
Q=pickle.load(open('hsolve4.pkl','rb'))['Q']
a,b,cc,dps,dom=[sp.Function(n)(v,r,th) for n in ('a','b','cc','dps','dom')]
Phi=sp.Function('Phi')(v); p1,p2=sp.Function('p1')(th),sp.Function('p2')(th)
K=sp.Function('K')(v,th); M=sp.Function('M')(v,th)
k=sp.Rational(-3,2)
# Q is a sum of r-powers times theta-functions: integrate Q/r^2 termwise via as_coefficients in r
Qe=sp.expand(Q)
def rpow_split(ex):
    d={}
    for t in sp.Add.make_args(sp.expand(ex)):
        c,pw=t.as_independent(r)[0], t.as_independent(r)[1]
        pe=sp.Poly(pw.subs(r,sp.Symbol('R')),sp.Symbol('R')) if False else None
        ex_r=sp.powsimp(pw)
        n_=sp.degree(ex_r,r) if ex_r.is_polynomial(r) else None
        e_=sp.simplify(sp.log(ex_r).expand(force=True).coeff(sp.log(r))) if ex_r!=1 else 0
        d[e_]=d.get(e_,0)+c
    return d
dQ=rpow_split(Qe)
print('Q powers',{kk:sp.count_ops(vv) for kk,vv in dQ.items()}, round(time.time()-t0,1))
Ip=0
for e_,cf in dQ.items():
    m=e_-2
    Ip+= cf*(sp.log(r) if m==-1 else r**(m+1)/(m+1))
Apart=sp.expand(r**2*Ip)
print('A part powers',list(rpow_split(Apart).keys()), round(time.time()-t0,1),flush=True)
Afull=Apart+M*r**2
sub={dps:p1*Phi*r**k, dom:p2*Phi*r**k, b:2*p1*Phi*r**k*r**4*sp.sin(th)**2*sp.cos(th)**2, cc:Phi*cp*r**sp.Rational(7,2)+K*r**2, a:Afull}
outd={}
for jk,name in [((0,2),'vtheta'),((0,1),'vr')]:
    E=res[jk][1].subs(sub).doit()
    E=sp.expand(sp.numer(sp.together(E)))
    d=rpow_split(E)
    outd[name]=d
    print(name,'r powers:',sorted(d.keys(),key=lambda x: float(x)), round(time.time()-t0,1),flush=True)
pickle.dump(dict(Apart=Apart,sup=outd),open('hsolve6.pkl','wb'))
