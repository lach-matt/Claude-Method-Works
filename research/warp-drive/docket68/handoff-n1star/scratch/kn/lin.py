import sympy as sp, time
t0=time.time()
v,r,th,p1,p2,e,mu=sp.symbols('v r theta phi1 phi2 e mu')
X=[v,r,th,p1,p2]
w,bb,u,q1,q2=[sp.Function(n)(v,r,th) for n in ('w','bb','u','q1','q2')]
W=1-mu/r**2+e*w; b=e*bb; U=e*u; P1=e*q1; P2=e*q2
S=sp.exp(-2*(P1+P2))
g=sp.zeros(5)
g[0,0]=-sp.exp(2*b)*W+r**2*S*U**2; g[0,1]=g[1,0]=sp.exp(2*b); g[0,2]=g[2,0]=-r**2*S*U; g[2,2]=r**2*S
g[3,3]=r**2*sp.cos(th)**2*sp.exp(2*P1); g[4,4]=r**2*sp.sin(th)**2*sp.exp(2*P2)
def lin(expr): return sp.simplify(sp.diff(expr,e).subs(e,0))
# first-order metric and inverse
g0=g.subs(e,0); g1=g.applyfunc(lambda x: sp.diff(x,e).subs(e,0))
gi0=sp.simplify(g0.inv()); gi1=-gi0*g1*gi0
n=5
def Gam(gi,gd):
    return [[[sum(gi[a,d]*(sp.diff(gd[d,b_],X[c])+sp.diff(gd[d,c],X[b_])-sp.diff(gd[b_,c],X[d])) for d in range(n))/2 for c in range(n)] for b_ in range(n)] for a in range(n)]
G0=Gam(gi0,g0)
G1=[[[sp.simplify(sum(gi1[a,d]*(sp.diff(g0[d,b_],X[c])+sp.diff(g0[d,c],X[b_])-sp.diff(g0[b_,c],X[d]))/2+gi0[a,d]*(sp.diff(g1[d,b_],X[c])+sp.diff(g1[d,c],X[b_])-sp.diff(g1[b_,c],X[d]))/2 for d in range(n))) for c in range(n)] for b_ in range(n)] for a in range(n)]
def R1(b_,c):
    ex=0
    for a in range(n):
        ex+=sp.diff(G1[a][b_][c],X[a])-sp.diff(G1[a][b_][a],X[c])
        for d in range(n):
            ex+=G1[a][a][d]*G0[d][b_][c]+G0[a][a][d]*G1[d][b_][c]-G1[a][c][d]*G0[d][b_][a]-G0[a][c][d]*G1[d][b_][a]
    return sp.simplify(ex)
Rrr=R1(1,1); Rrt=R1(1,2)
trace=sp.simplify(gi0[2,2]*R1(2,2)+gi0[3,3]*R1(3,3)+gi0[4,4]*R1(4,4))
print('Rrr',sp.factor(Rrr)); print('Rrt',sp.collect(sp.expand(Rrt),[u])); print('trace',sp.collect(sp.expand(trace),[w]))
print(time.time()-t0)
import pickle; pickle.dump(dict(Rrr=Rrr,Rrt=Rrt,trace=trace,R33=R1(3,3),R44=R1(4,4),Rvr=R1(0,1),Rvt=R1(0,2)),open('lin.pkl','wb'))
