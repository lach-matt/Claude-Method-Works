import sympy as sp
t,x,y,z,M=sp.symbols('t x y z M',real=True)
Y=[t,x,y,z]; r=sp.sqrt(x**2+y**2+z**2)
def ricci(g):
    gi=g.inv()
    G=[[[sum(gi[a,e]*(sp.diff(g[e,b],Y[c])+sp.diff(g[e,c],Y[b])-sp.diff(g[b,c],Y[e])) for e in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
    def R(b,d):
        s=0
        for a in range(4):
            s+=sp.diff(G[a][b][d],Y[a])-sp.diff(G[a][b][a],Y[d])
            s+=sum(G[a][a][e]*G[e][b][d]-G[a][d][e]*G[e][b][a] for e in range(4))
        return s
    return [[R(b,d) for d in range(4)] for b in range(4)]
# exact isotropic Schwarzschild: must be Ricci-flat
A=((1-M/(2*r))/(1+M/(2*r)))**2; Bf=(1+M/(2*r))**4
Rx=ricci(sp.diag(-A,Bf,Bf,Bf))
pt={x:sp.Rational(3,10),y:sp.Rational(3,10),z:sp.Rational(1,10),M:sp.Rational(1,50)}
print("isotropic exact Ricci at a point (should be 0):", max(abs(sp.N(Rx[i][j].subs(pt))) for i in range(4) for j in range(4)))
Phi=-M/r
gl=sp.diag(-(1+2*Phi),1-2*Phi,1-2*Phi,1-2*Phi)
Rl=ricci(gl)
for Mv in (2e-3,-2e-3,-4e-3):
    p={x:0,y:0.3,z:0,M:Mv}
    ph=-Mv/0.3; s=((1+2*ph)/(1-2*ph))**0.5
    k=[1,s,0,0]
    Rkk=sum(float(Rl[a][b].subs(p))*k[a]*k[b] for a in range(2) for b in range(2))
    w=3*Mv/0.3**3
    print("M=%+.0e  R_kk(true null k) at closest approach = %.4e ; -4M^2/b^4 = %.4e ; |R_kk|/|w| = %.2e" % (Mv,Rkk,-4*Mv**2/0.3**4,abs(Rkk/w)))
