import json
T = json.load(open("tower.json"))
L12 = [tuple(c) for c in T["12"]]   # canonical envelope, 70,905
L13 = [tuple(c) for c in T["13"]]   # canonical envelope, 199,130
def comp(L, tgt, src):
    srcs = set(tuple(c[i] for i in src) for c in L)
    return sum(1 for c in L if tuple(c[i] for i in tgt) in srcs)
b_t, b_s = (4,5,6,8), (0,1,2,7)
n12 = comp(L12, b_t+(11,), b_s+(10,))   # 2K -> 2Jc
n13 = comp(L13, b_t+(12,), b_s+(10,))   # 2J -> 2Jc
print("CANONICAL Λ12: composable =", n12, "of", len(L12), "fraction = %.4f" % (n12/len(L12)))
print("CANONICAL Λ13: composable =", n13, "of", len(L13), "fraction = %.4f" % (n13/len(L13)))
# dichotomy check: does the fraction still FALL at each coupling axis on the canonical build?
print("sequence: 0.0000, 0.7068, 0.8087, 0.6956, %.4f, %.4f" % (n12/len(L12), n13/len(L13)))
# non-composable decomposition at canonical Λ13 (for the record)
srcs = set(tuple(c[i] for i in b_s+(10,)) for c in L13)
nonc = [c for c in L13 if tuple(c[i] for i in b_t+(12,)) not in srcs]
g0 = sum(1 for c in nonc if c[6]==0)
jhigh = sum(1 for c in nonc if c[12] in (6,7,8) and c[6]!=0)
jmax = max(c[12] for c in L13)
print("canonical Λ13 non-composable:", len(nonc), "| g=0:", g0, "| 2J in {6,7,8} (g≠0):", jhigh, "| combination:", len(nonc)-g0-jhigh, "| max 2J =", jmax)
