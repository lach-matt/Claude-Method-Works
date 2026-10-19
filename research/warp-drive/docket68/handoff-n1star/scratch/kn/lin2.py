import sympy as sp, time
t0=time.time()
exec(open('red.py').read().split("gi5,G5,R5=")[0])
e,mu=sp.symbols('e mu')
w,bb,u,q1,q2=[sp.Function(n)(v,r,th) for n in ('w','bb','u','q1','q2')]
sub={b:e*bb, W:1-mu/r**2+e*w, U:e*u, gam:r**2*sp.exp(-2*e*(q1+q2)), U1:sp.log(r*sp.cos(th))+e*q1, U2:sp.log(r*sp.sin(th))+e*q2}
g5s=g5.subs(sub).doit()
n=5
def ser(x): return sp.expand(sp.series(x,e,0,2).removeO())
gi=g5s.inv().applyfunc(lambda x: ser(sp.simplify(x)))
print('inv',time.time()-t0)
G=[[[ser(sum(gi[a,d]*(sp.diff(g5s[d,b_],X[c])+sp.diff(g5s[d,c],X[b_])-sp.diff(g5s[b_,c],X[d])) for d in range(n))/2) for c in range(n)] for b_ in range(n)] for a in range(n)]
print('christ',time.time()-t0)
def Ric(b_,c):
    ex=0
    for a in range(n):
        ex+=sp.diff(G[a][b_][c],X[a])-sp.diff(G[a][b_][a],X[c])
        for d in range(n):
            ex+=G[a][a][d]*G[d][b_][c]-G[a][c][d]*G[d][b_][a]
    return sp.simplify(sp.expand(ex).coeff(e,1))
out={}
for k in [(1,1),(1,2),(2,2),(3,3),(4,4),(0,1),(0,2)]:
    out[k]=Ric(*k); print(k,time.time()-t0,flush=True)
import pickle; pickle.dump(out,open('lin2.pkl','wb'))
print('Rrr',sp.factor(out[(1,1)]))
print('Rrt',out[(1,2)])
