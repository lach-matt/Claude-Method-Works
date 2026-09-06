from itertools import product, combinations

def latclose(gens):
    S = set(gens)
    grew = True
    while grew:
        grew = False
        cur = list(S)
        for a in cur:
            for b in cur:
                for t in (tuple(max(x,y) for x,y in zip(a,b)),
                          tuple(min(x,y) for x,y in zip(a,b))):
                    if t not in S: S.add(t); grew = True
    return S

def minseed(X):
    cells = sorted(X)
    for k in range(1, len(cells)+1):
        hits = [set(G) for G in combinations(cells, k) if latclose(G) == X]
        if hits: return k, len(hits)
    return None

# c=2 witnesses across d: full box (fill=1) vs maximal chain (fill -> 0)
for d in (3,4):
    box = set(product((0,1), repeat=d))
    k_box, n_box = minseed(box)
    # maximal chain: (0..0),(1,0..0),(1,1,0..),...,(1..1)
    chain = set(tuple([1]*i + [0]*(d-i)) for i in range(d+1))
    assert latclose(chain) == chain   # closed sublattice
    k_ch, n_ch = minseed(chain)
    print(f"d={d}: full box |X|={2**d} fill=1.000 seed={k_box} | chain |X|={d+1} fill={(d+1)/2**d:.3f} seed={k_ch}")

# Q2: convex geometry (points on a line), unique seed + empty set closed
def conv(S):
    return frozenset(range(min(S), max(S)+1)) if S else frozenset()
X = frozenset(range(1,6))
mins = []
for k in range(1,6):
    mins = [set(G) for G in combinations(sorted(X), k) if conv(G)==X]
    if mins: break
print("convex geometry [1..5]: min seeds:", mins, "| unique:", len(mins)==1,
      "| conv(∅)=∅ closed:", conv(frozenset())==frozenset())