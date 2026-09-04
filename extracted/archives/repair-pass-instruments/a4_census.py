import json
from itertools import product
T = json.load(open("tower.json"))
L11 = [tuple(c) for c in T["11"]]
L12t = [c+(K2,) for c in L11 for K2 in range(abs(c[10]-2*c[5]), c[10]+2*c[5]+1, 2)]
alph = [sorted(set(c[i] for c in L12t)) for i in range(12)]
box = 1
for a in alph: box *= len(a)
print("triangle Λ12: cells =", len(L12t), "| box =", box)
Xs = set(L12t)
d = 12
pairs = [(i,j) for i in range(d) for j in range(i+1,d)]
proj = {p: set((x[p[0]], x[p[1]]) for x in Xs) for p in pairs}
R = 0
for y in product(*alph):
    ok = True
    for (i,j) in pairs:
        if (y[i], y[j]) not in proj[(i,j)]:
            ok = False; break
    if ok: R += 1
print("R =", R, "| E =", R - len(Xs), "(MC 1515 states E = 35,570)")
