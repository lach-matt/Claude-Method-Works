import json
T = json.load(open("tower.json"))
L11 = [tuple(c) for c in T["11"]]; L12 = [tuple(c) for c in T["12"]]; L10 = [tuple(c) for c in T["10"]]

# canonical-build extra fingerprint: cells of Λ12 with f below the cap (f=0)
print("Λ12 cells with f < f_max:", sum(1 for c in L12 if c[5] < 1), "(printed: 39,375)")

# Hypothesis for the Index of Indices build: exact triangle, cell's own f, parity step 2
L12t = [c+(K2,) for c in L11 for K2 in range(abs(c[10]-2*c[5]), c[10]+2*c[5]+1, 2)]
L13t = [c+(J2,) for c in L12t for J2 in range(max(0,c[11]-1), c[11]+2)]
print("triangle build: Λ12' =", len(L12t), "(printed 22,275) | Λ13' =", len(L13t), "(printed 64,290)")
print("2K=0 in Λ12' =", sum(1 for c in L12t if c[11]==0), "| |Λ10| =", len(L10))

# B: the two axis-10 variants, restated for the record
L9 = [tuple(c) for c in T["9"]]
bare = sum(c[6]-c[8]+1 for c in L9)
parg = sum(1 for c in L9 for v in range(c[8], c[6]+1) if (v-c[6])%2==0)
print("axis 10: bare interval =", bare, "| parity build =", parg)