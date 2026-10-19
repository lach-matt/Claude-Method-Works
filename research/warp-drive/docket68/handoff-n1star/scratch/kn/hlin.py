import sympy as sp, time
t0=time.time()
v,r,th,e,mu=sp.symbols('v r theta e mu',positive=True)
X=[v,r,th]
s,c=sp.sin(th),sp.cos(th)
rho=r**2*s*c; Fm=1-mu/r**2
a,b,cc,dps,dom=[sp.Function(n)(v,r,th) for n in ('a','b','cc','dps','dom')]
hb=rho**2*sp.Matrix([[-Fm,1,0],[1,0,0],[0,0,r**2]])
dh=sp.Matrix([[a,b,cc],[b,0,0],[cc,0,0]])
h=hb+e*dh
gi=h.inv().applyfunc(lambda x: sp.series(x,e,0,2).removeO())
n=3
G=[[[sp.expand(sp.series(sum(gi[i,d]*(sp.diff(h[d,j],X[k])+sp.diff(h[d,k],X[j])-sp.diff(h[j,k],X[d])) for d in range(n))/2,e,0,2).removeO()) for k in range(n)] for j in range(n)] for i in range(n)]
def Ric(j,k):
    ex=0
    for i in range(n):
        ex+=sp.diff(G[i][j][k],X[i])-sp.diff(G[i][j][i],X[k])
        for d in range(n):
            ex+=G[i][i][d]*G[d][j][k]-G[i][k][d]*G[d][j][i]
    return sp.expand(ex)
psib=sp.log(rho); omb=sp.log(c/s)/2
src=lambda j,k,p,o: sp.Rational(3,2)*sp.diff(p,X[j])*sp.diff(p,X[k])+2*sp.diff(o,X[j])*sp.diff(o,X[k])
ps=psib+e*dps; om=omb+e*dom
res={}
for jk in [(1,1),(1,2),(2,2),(0,1),(0,2),(0,0)]:
    R=Ric(*jk); S=sp.expand(src(*jk,ps,om))
    res[jk]=(sp.simplify(R.coeff(e,0)-S.coeff(e,0)), sp.simplify(R.coeff(e,1)-S.coeff(e,1)))
    print(jk,'bg residual',res[jk][0],' t',round(time.time()-t0,1),flush=True)
import pickle; pickle.dump(res,open('hlin.pkl','wb'))
for jk in [(1,1),(1,2),(2,2)]: print(jk,'linear:',res[jk][1])
