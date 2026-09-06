from itertools import product, permutations
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
def minE(cells,axes):
    best=None; arg=None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        if best is None or E<best: best,arg=E,p
    return best,arg

FIXN=["Ne","c","Z","N","A"]; SEATN=["nucleus","subvalence","valence"]; RELN=["electronic","nuclear"]
# ladder : fixes, seat, relation
LAD=[("isoelectronic",0,2,0),("the walk",1,2,0),("ionisation",2,1,0),
     ("isotopic",2,0,1),("isotonic",3,0,1),("isobaric",4,0,1)]

for label, sub in (("FOUR ladders (as held)",[0,1,2,3]),("SIX ladders (arithmetic)",[0,1,2,3,4,5])):
    cells={(LAD[i][1],LAD[i][2],LAD[i][3]) for i in sub}
    nf=len({LAD[i][1] for i in sub}); ns=len({LAD[i][2] for i in sub}); nr=len({LAD[i][3] for i in sub})
    E,_=minE(cells,[nf,ns,nr])
    print(f"{label:<26} cells {len(cells)}  box {nf*ns*nr:>3}  min E = {E}")
    from collections import Counter
    print(f"{'':<26} fixes injective on ladders: {len({LAD[i][1] for i in sub})==len(sub)}")