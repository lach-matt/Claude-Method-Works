from itertools import product, combinations

def latclose(gens, dims):
    """sublattice closure under coordinatewise min/max"""
    S = set(gens)
    grew = True
    while grew:
        grew = False
        cur = list(S)
        for a in cur:
            for b in cur:
                j = tuple(max(x,y) for x,y in zip(a,b))
                m = tuple(min(x,y) for x,y in zip(a,b))
                for t in (j,m):
                    if t not in S:
                        S.add(t); grew = True
    return S

# --- Q3 witness: full box c=3,d=3 (fill=100%) ---
box = set(product(range(3), repeat=3))
target_seed = None
cells = sorted(box)
found = False
for k in range(2, 6):
    for G in combinations(cells, k):
        if latclose(G, 3) == box:
            target_seed = k; found = True; break
    if found: break
print("full box 3^3: |X|=27, fill=1.000, seed =", target_seed, "(law d+c-2 =", 3+3-2, ")")

# --- Q3 witness: a sparse down-set, same d,c, much lower fill ---
# down-set: x+y+z <= 2  (a small corner)
ds = set(t for t in box if sum(t) <= 2)
found = False
for k in range(2, 8):
    for G in combinations(sorted(ds), k):
        if latclose(G, 3) == ds:
            seed_ds = k; found = True; break
    if found: break
print("down-set sum<=2: |X|=%d, fill=%.3f, seed = %d (law d+c-1 = %d)" % (len(ds), len(ds)/27, seed_ds, 3+3-1))

# --- Q2 witness: an Edelman convex geometry where the seed IS unique ---
# ground set 1..5 on a line; closure = interval hull conv(S)=[min,max]
# closed set X=[1,5]: minimal generating sets under conv
import itertools
X = frozenset(range(1,6))
def conv(S):
    if not S: return frozenset()
    return frozenset(range(min(S), max(S)+1))
mins = []
for k in range(1,6):
    for G in itertools.combinations(sorted(X), k):
        if conv(G) == X: mins.append(set(G))
    if mins: break
print("convex geometry [1..5]: minimal seeds of size %d:" % len(mins[0]), mins,
      "| unique =", len(mins)==1, "| extreme points = {1,5}")
print("and conv(empty)=empty is closed:", conv(frozenset())==frozenset())