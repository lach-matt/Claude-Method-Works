import sympy as sp, pickle
v,r,th=sp.symbols('v r theta',positive=True)
d=pickle.load(open('hsolve6.pkl','rb'))
Phi=sp.Function('Phi')(v); p1,p2=sp.Function('p1')(th),sp.Function('p2')(th)
K=sp.Function('K')(v,th); M=sp.Function('M')(v,th)
for name,dd in d['sup'].items():
    print('==',name)
    for pw in sorted(dd,key=lambda x: float(x)):
        c=dd[pw]
        has=[str(f) for f in (K,M) if c.has(f)]
        cs=sp.simplify(c)
        print(' r^%s'%pw, 'involves',has, ':', str(cs)[:600])
print('Apart:',str(sp.simplify(d['Apart']))[:900])
