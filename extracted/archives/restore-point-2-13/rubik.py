from itertools import product, permutations
LAW=["1 amp","2 spread","3 chg-exp","4 floor","5 gate","6 switch","7 regimes"]
CAR=["u","p","l-lc","Z-T"]
# (law, carrier) pairs actually held
HELD=[(0,"u"),(1,"p"),(2,"u"),(3,"p"),(4,"l-lc"),(5,"Z-T"),(6,"p")]
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(d) for j in range(d) if i!=j)}
print("  THE REARRANGEMENT — E depends on the ORDER of both axes\n")
best=[]
for lp in permutations(range(7)):
    for cp in permutations(CAR):
        ci={c:i for i,c in enumerate(cp)}
        cells={(lp.index(a),ci[b]) for a,b in HELD}
        R=opR(cells,2)
        best.append((len(R)-len(cells),lp,cp))
best.sort(key=lambda z:z[0])
print(f"      {len(best)} orderings tested (7! × 4!)")
print(f"      E ranges {best[0][0]} to {best[-1][0]}   ·   my arbitrary choice gave 7\n")
E0,lp,cp=best[0]
print(f"  THE MINIMUM:  E = {E0}\n")
print(f"      carrier order : {' < '.join(cp)}")
print(f"      law order     : {' < '.join(LAW[i] for i in lp)}\n")
ci={c:i for i,c in enumerate(cp)}
cells={(lp.index(a),ci[b]):(LAW[a],b) for a,b in HELD}
print(f"      {'':<12}" + "".join(f"{c:>10}" for c in cp))
for r in range(7):
    row=f"      {LAW[lp[r]]:<12}"
    for c in range(4):
        row+=f"{('X' if (r,c) in cells else '.'):>10}"
    print(row)
print()
n0=sum(1 for e,_,_ in best if e==E0)
print(f"      {n0} orderings reach E = {E0}\n")
print("  HOW MANY REACH ZERO?\n")
z=[b for b in best if b[0]==0]
print(f"      {len(z)} of {len(best)}   ({100*len(z)/len(best):.2f}%)")
if z:
    print("\n      one of them:")
    E0,lp,cp=z[0]
    ci={c:i for i,c in enumerate(cp)}
    cells={(lp.index(a),ci[b]) for a,b in HELD}
    print(f"          carrier : {' < '.join(cp)}")
    print(f"          law     : {' < '.join(LAW[i] for i in lp)}")
    print(f"\n      {'':<12}" + "".join(f"{c:>10}" for c in cp))
    for r in range(7):
        row=f"      {LAW[lp[r]]:<12}"
        for c in range(4):
            row+=f"{('X' if (r,c) in cells else '.'):>10}"
        print(row)
