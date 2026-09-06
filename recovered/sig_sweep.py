import json
from itertools import combinations
T = json.load(open("tower.json"))
L11 = [tuple(c) for c in T["11"]]
# rebuild triangle objects
L12t = [c+(K2,) for c in L11 for K2 in range(abs(c[10]-2*c[5]), c[10]+2*c[5]+1, 2)]
L13t = [c+(J2,) for c in L12t for J2 in range(max(0,c[11]-1), c[11]+2)]
# idx: 0n 1l 2k 3q 4e 5f 6g 7S2 8S2p 9v 10Jc2 11K2 12J2

def comp(L, tgt, src):
    srcs = set(tuple(c[i] for i in src) for c in L)
    return sum(1 for c in L if tuple(c[i] for i in tgt) in srcs)

base_t, base_s = (4,5,6,8), (0,1,2,7)
# L11: which single extra (tgt_i, src_j) pair gives 9450?
print("Λ11 sweep (target 9,450):")
for ti in range(11):
    for sj in range(11):
        n = comp(L11, base_t+(ti,), base_s+(sj,))
        if n == 9450:
            print("  HIT extra pair: tgt idx", ti, "-> src idx", sj, "=", n)
# also base alone and v->v style
print("  base4:", comp(L11, base_t, base_s))