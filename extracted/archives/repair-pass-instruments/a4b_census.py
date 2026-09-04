import json
from itertools import product
T = json.load(open("tower.json"))
L11 = [tuple(c) for c in T["11"]]
L12t = [c+(K2,) for c in L11 for K2 in range(abs(c[10]-2*c[5]), c[10]+2*c[5]+1, 2)]
alph = [sorted(set(c[i] for c in L12t)) for i in range(12)]
Xs = set(L12t); d = 12
pairs = [(i,j) for i in range(d) for j in range(i+1,d)]
# staircase bounds: for each pair, per value of coord i, the [min,max] of coord j (and vice versa)
bnd = {}
for (i,j) in pairs:
    mi, ma = {}, {}
    mj, mb = {}, {}
    for x in Xs:
        a, b = x[i], x[j]
        if a not in mi or b < mi[a]: mi[a] = b
        if a not in ma or b > ma[a]: ma[a] = b
        if b not in mj or a < mj[b]: mj[b] = a
        if b not in mb or a > mb[b]: mb[b] = a
    bnd[(i,j)] = (mi, ma, mj, mb)
R = 0
for y in product(*alph):
    ok = True
    for (i,j) in pairs:
        mi, ma, mj, mb = bnd[(i,j)]
        a, b = y[i], y[j]
        if a not in mi or b < mi[a] or b > ma[a] or a < mj[b] or a > mb[b]:
            ok = False; break
    if ok: R += 1
print("staircase-bound R =", R, "| E =", R - len(Xs), "(MC 1515: E = 35,570)")
