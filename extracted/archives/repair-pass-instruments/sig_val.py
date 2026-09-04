import json
from itertools import combinations
T = json.load(open("tower.json"))
L11 = [tuple(c) for c in T["11"]]
L12t = [c+(K2,) for c in L11 for K2 in range(abs(c[10]-2*c[5]), c[10]+2*c[5]+1, 2)]
L13t = [c+(J2,) for c in L12t for J2 in range(max(0,c[11]-1), c[11]+2)]

def comp(L, tgt, src):
    srcs = set(tuple(c[i] for i in src) for c in L)
    return sum(1 for c in L if tuple(c[i] for i in tgt) in srcs)

b_t, b_s = (4,5,6,8), (0,1,2,7)
# Λ12 triangle: expect 14,242 — sweep extras on top of nothing/Jc->Jc
print("Λ12t base4:", comp(L12t, b_t, b_s), "| +Jc->Jc:", comp(L12t, b_t+(10,), b_s+(10,)))
print("Λ12t sweep for 14,242:")
for extra in combinations(range(12),0): pass
for t1 in range(12):
    for s1 in range(12):
        if comp(L12t, b_t+(t1,), b_s+(s1,)) == 14242:
            print("  HIT 1-extra:", t1, "->", s1)
for t1 in range(12):
    for s1 in range(12):
        for t2 in range(t1+1,12):
            for s2 in range(12):
                if s2==s1: continue
                n = comp(L12t, b_t+(t1,t2), b_s+(s1,s2))
                if n == 14242:
                    print("  HIT 2-extra:", (t1,"->",s1), (t2,"->",s2))
