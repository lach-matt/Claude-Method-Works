import sympy as sp, time
t0=time.time()
v,r,th,p1,p2=sp.symbols('v r theta phi1 phi2')
X3=[v,r,th]; X=[v,r,th,p1,p2]
b,W,U,gam,U1,U2=[sp.Function(n)(v,r,th) for n in ('b','W','U','gam','U1','U2')]
g3=sp.Matrix([[-sp.exp(2*b)*W+gam*U**2, sp.exp(2*b), -gam*U],[sp.exp(2*b),0,0],[-gam*U,0,gam]])
def christ(g,X):
    gi=sp.simplify(g.inv()); n=len(X)
    G=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b_],X[c])+sp.diff(g[d,c],X[b_])-sp.diff(g[b_,c],X[d])) for d in range(n))/2) for c in range(n)] for b_ in range(n)] for a in range(n)]
    return gi,G
def ricci(g,X):
    gi,G=christ(g,X); n=len(X)
    R=sp.zeros(n)
    for b_ in range(n):
        for c in range(b_,n):
            e=0
            for a in range(n):
                e+=sp.diff(G[a][b_][c],X[a])-sp.diff(G[a][b_][a],X[c])
                for d in range(n):
                    e+=G[a][a][d]*G[d][b_][c]-G[a][c][d]*G[d][b_][a]
            R[b_,c]=R[c,b_]=e
    return gi,G,R
g5=sp.zeros(5); g5[:3,:3]=g3; g5[3,3]=sp.exp(2*U1); g5[4,4]=sp.exp(2*U2)
gi5,G5,R5=ricci(g5,X); print('R5',time.time()-t0)
gi3,G3,R3=ricci(g3,X3); print('R3',time.time()-t0)
sq5=sp.exp(U1+U2)*sp.sqrt(-g3.det())  # sqrt(-g5)
det3=sp.simplify(-g3.det()); print('det3',det3)
s3=sp.exp(2*b)*sp.sqrt(gam)
def box5(f):
    return sp.simplify(sum(sp.diff(sp.exp(U1+U2)*s3*gi3[a,c]*sp.diff(f,X3[c]),X3[a]) for a in range(3) for c in range(3))/(sp.exp(U1+U2)*s3))
def hess3(f,a,c):
    return sp.diff(f,X3[a],X3[c])-sum(G3[d][a][c]*sp.diff(f,X3[d]) for d in range(3))
I1=[sp.simplify(R5[3,3]+sp.exp(2*U1)*box5(U1)), sp.simplify(R5[4,4]+sp.exp(2*U2)*box5(U2)), sp.simplify(R5[3,4])]+[sp.simplify(R5[a,k]) for a in range(3) for k in (3,4)]
print('I1',I1,time.time()-t0)
I2=[sp.simplify(R5[a,c]-(R3[a,c]-sum(hess3(Ui,a,c)+sp.diff(Ui,X3[a])*sp.diff(Ui,X3[c]) for Ui in (U1,U2)))) for a in range(3) for c in range(a,3)]
print('I2',I2,time.time()-t0)
