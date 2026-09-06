import json
T = json.load(open("tower.json"))
L11 = [tuple(c) for c in T["11"]]
L12t = [c+(K2,) for c in L11 for K2 in range(abs(c[10]-2*c[5]), c[10]+2*c[5]+1, 2)]
L13t = [c+(J2,) for c in L12t for J2 in range(max(0,c[11]-1), c[11]+2)]
def comp(L, tgt, src):
    srcs = set(tuple(c[i] for i in src) for c in L)
    return sum(1 for c in L if tuple(c[i] for i in tgt) in srcs)
b_t, b_s = (4,5,6,8), (0,1,2,7)
n13 = comp(L13t, b_t+(12,), b_s+(10,))
print("Λ13t with 2J->2Jc:", n13, "(recorded 39,772) fraction:", round(n13/len(L13t),4))
# decomposition check per register 627
srcs = set(tuple(c[i] for i in b_s+(10,)) for c in L13t)
nonc = [c for c in L13t if tuple(c[i] for i in b_t+(12,)) not in srcs]
g0 = sum(1 for c in nonc if c[6]==0)
jhigh = sum(1 for c in nonc if c[12] in (6,7,8) and c[6]!=0)
combo = len(nonc)-g0-jhigh
print("non-composable:", len(nonc), "| g=0:", g0, "(rec 11,188) | 2J in 6-8:", jhigh, "(rec 5,116) | combination:", combo, "(rec 8,214)")