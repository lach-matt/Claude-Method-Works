import sympy as sp, mpmath as mp, time
mp.mp.dps=30
t,x,y,z=sp.symbols('t x y z',real=True)
X=[t,x,y,z]; VS=sp.Rational(1,2); SIG=8; RAD=1
def prof(r): return (sp.tanh(SIG*(r+RAD))-sp.tanh(SIG*(r-RAD)))/(2*sp.tanh(SIG*RAD))
def Gmixed(beta):
    g=sp.Matrix([[-1+beta**2,-beta,0,0],[-beta,1,0,0],[0,0,1,0],[0,0,0,1]])
    gi=sp.Matrix([[-1,-beta,0,0],[-beta,1-beta**2,0,0],[0,0,1,0],[0,0,0,1]])
    assert sp.simplify(g*gi-sp.eye(4))==sp.zeros(4)
    dg=[[[sp.diff(g[i,j],X[c]) for c in range(4)] for j in range(4)] for i in range(4)]
    Gam=[[[sum(gi[a,e]*(dg[e][b][c]+dg[e][c][b]-dg[b][c][e]) for e in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
    Ric=sp.zeros(4)
    for b in range(4):
        for d in range(b,4):
            s=0
            for a in range(4):
                s+=sp.diff(Gam[a][b][d],X[a])-sp.diff(Gam[a][b][a],X[d])
                for e in range(4):
                    s+=Gam[a][a][e]*Gam[e][b][d]-Gam[a][d][e]*Gam[e][b][a]
            Ric[b,d]=s; Ric[d,b]=s
    Rs=sum(gi[b,d]*Ric[b,d] for b in range(4) for d in range(4))
    Gd=Ric-Rs*g/2
    return gi*Gd
t0=time.time()
lab=Gmixed(VS*prof(sp.sqrt((x-VS*t)**2+y**2+z**2)))
print('lab built',time.time()-t0)
fl=sp.lambdify((t,x,y,z),lab,'mpmath')
print('lambdified',time.time()-t0)
T=fl(0,mp.mpf('0.9'),mp.mpf('0.3'),0)
print('eval',time.time()-t0)
M=mp.matrix(T)/(8*mp.pi)
print(mp.eig(M)[0])
