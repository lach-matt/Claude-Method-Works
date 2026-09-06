from itertools import product, permutations, combinations
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
    b=None;arg=None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        if b is None or E<b: b,arg=E,p
    return b,arg

LADDERS=["isoelectronic","the walk","ionisation","isotopic","isotonic","isobaric",
         "Rydberg series","l-ladder","term ladder","outer-j","parent-term","isomeric"]

# EVERY axis below is a coordinate the work already holds and proves.
AX={
 # Lambda_chem's seats
 "seat  (Lambda_chem)": (["nucleus","core","subvalence","valence"],
      [3,3,2,0,0,0,3,3,3,3,1,0]),
 # T.dich: counting coordinates close exactly, coupling close as envelopes
 "kind  (T.dich)": (["counting","coupling"],
      [0,0,0,0,0,0,0,0,1,1,1,0]),
 # K.zcross: composability within one element vs across the 118
 "Zcross (K.zcross)": (["within one element","across elements"],
      [1,1,0,0,1,1,0,0,0,0,0,0]),
 # the relation the ladder's constraint lives in — both already indexed objects
 "relation (Lambda | nuclide)": (["Lambda","nuclide chart"],
      [0,0,0,1,1,1,0,0,0,0,0,1]),
 # Lambda_phys's domain axis
 "domain (Lambda_phys)": (["all elements","a region","one species"],
      [0,0,0,1,1,1,2,2,2,2,2,1]),
}

names=list(AX)
print(f"{'axes':<62}{'cells':>6}{'box':>6}{'minE':>6}")
best=[]
for tri in combinations(names,3):
    vals=[AX[t][0] for t in tri]; asg=[AX[t][1] for t in tri]
    cells={tuple(asg[i][k] for i in range(3)) for k in range(len(LADDERS))}
    axes=[len(v) for v in vals]
    E,_=minE(cells,axes)
    box=axes[0]*axes[1]*axes[2]
    best.append((E,len(cells),box,tri))
    print(f"{' x '.join(t.split('  ')[0].split(' (')[0] for t in tri):<62}"
          f"{len(cells):>6}{box:>6}{E:>6}")
print()
for E,n,box,tri in sorted(best)[:3]:
    print(f"  min E = {E}  on {n} cells in a box of {box}:  {' x '.join(tri)}")