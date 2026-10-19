import sympy as sp
v,r,th,p1,p2=sp.symbols('v r theta phi1 phi2',real=True)
X=[v,r,th,p1,p2]
mu=sp.Function('mu')(v); Fm=1-mu/r**2
g=sp.diag(1,1,1,1,1)*0
g=sp.zeros(5); g[0,0]=-Fm; g[0,1]=g[1,0]=1; g[2,2]=r**2; g[3,3]=r**2*sp.cos(th)**2; g[4,4]=r**2*sp.sin(th)**2
gi=sp.simplify(g.inv())
fv,fr,ft=sp.symbols('f_v f_r f_t',real=True)
df=[fv,fr,ft,0,0]
grad2=sum(gi[a,b]*df[a]*df[b] for a in range(5) for b in range(5))
T=sp.Matrix(5,5,lambda a,b: df[a]*df[b]-sp.Rational(1,2)*g[a,b]*grad2)
Tup=sp.simplify(gi*T*gi)
al=sp.Function('alpha')(v,r); sg=sp.Function('sigma')(v,r)
Xv=[al,-sg,0,0,0]
pi=sp.Matrix(5,5,lambda a,b: sum(Xv[e]*sp.diff(g[a,b],X[e])+g[e,b]*sp.diff(Xv[e],X[a])+g[a,e]*sp.diff(Xv[e],X[b]) for e in range(5)))
K=sp.simplify(sp.Rational(1,2)*sum(Tup[a,b]*pi[a,b] for a in range(5) for b in range(5)))
K=sp.expand(K)
P=sp.Poly(K,fv,fr,ft)
for m,cf in zip(P.monoms(),P.coeffs()): print(m, sp.factor(cf))
