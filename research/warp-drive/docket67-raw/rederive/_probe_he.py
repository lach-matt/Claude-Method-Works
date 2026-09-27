import sympy as sp, time
t,x,y,z,v=sp.symbols('t x y z v',real=True)
F0,F1,F2=sp.symbols('F0 F1 F2',real=True)  # f, f', f'' at R
X=[t,x,y,z]
def einstein_mixed(shift_of, R):
    f=sp.Function('f')
    fR=f(R)
    beta=shift_of(fR)
    g=sp.Matrix([[-1+beta**2,-beta,0,0],[-beta,1,0,0],[0,0,1,0],[0,0,0,1]])
    gi=sp.simplify(g.inv())
    Gam=[[[sum(gi[a,e]*(sp.diff(g[e,b],X[c])+sp.diff(g[e,c],X[b])-sp.diff(g[b,c],X[e])) for e in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
    Ric=sp.zeros(4)
    for b in range(4):
        for d in range(4):
            s=0
            for a in range(4):
                s+=sp.diff(Gam[a][b][d],X[a])-sp.diff(Gam[a][b][a],X[d])
                for e in range(4):
                    s+=Gam[a][a][e]*Gam[e][b][d]-Gam[a][d][e]*Gam[e][b][a]
            Ric[b,d]=s
    Rs=sum(gi[b,d]*Ric[b,d] for b in range(4) for d in range(4))
    Gd=Ric-Rs*g/2
    Gm=gi*Gd
    # replace f and its derivatives by symbols
    rep={}
    Gm=Gm.applyfunc(lambda e: e.doit())
    d2=sp.Derivative(f(R),R) # placeholder
    def sub(e):
        e=e.subs(sp.Subs(sp.Derivative(f(sp.Symbol('_x')),sp.Symbol('_x'),2),sp.Symbol('_x'),R),F2)
        return e
    return Gm, f
t0=time.time()
Rlab=sp.sqrt((x-v*t)**2+y**2+z**2)
Gm,f=einstein_mixed(lambda fR: v*fR, Rlab)
print('built',time.time()-t0)
e=Gm[0,1]
print(e.atoms(sp.Derivative), e.atoms(sp.Subs))
