from itertools import product

def E_defect(X, dims):
    """double-projection closure defect on a product of chains"""
    X = set(X)
    box = set(product(*[range(c) for c in dims]))
    pairs = [(i,j) for i in range(len(dims)) for j in range(len(dims)) if i<j]
    proj = {p: set((x[p[0]], x[p[1]]) for x in X) for p in pairs}
    R = set(y for y in box if all((y[i],y[j]) in proj[(i,j)] for (i,j) in pairs))
    return len(R) - len(X)

# a closed staircase in 4x4x4: x<=y<=z  (single-argument monotone bounds -> sublattice)
dims = (4,4,4)
X = [t for t in product(range(4),repeat=3) if t[0]<=t[1]<=t[2]]
print("staircase x<=y<=z in 4^3: |X| =", len(X), " E =", E_defect(X, dims))

# reading A: at-EITHER-extreme -> 1  (M's stated bit)
def bitA(v,c): return 1 if v in (0,c-1) else 0
XA = set(tuple(bitA(v,4) for v in t) for t in X)
print("at-either-extreme image: |X| =", len(XA), " E =", E_defect(XA,(2,2,2)),
      "| monotone? min->%d, mid->%d, max->%d" % (bitA(0,4),bitA(1,4),bitA(3,4)))

# reading B: at-TOP threshold -> 1  (a lattice homomorphism)
def bitB(v,c): return 1 if v==c-1 else 0
XB = set(tuple(bitB(v,4) for v in t) for t in X)
print("at-top threshold image:  |X| =", len(XB), " E =", E_defect(XB,(2,2,2)))

# reading C: at-BOTTOM threshold (also a homomorphism, dual)
def bitC(v,c): return 1 if v==0 else 0
XC = set(tuple(1-bitC(v,4) for v in t) for t in X)   # complement to keep monotone orientation
print("at-bottom threshold image:|X| =", len(XC), " E =", E_defect(XC,(2,2,2)))

# collapse idempotence: rank-chain of a rank-chain is itself
# graded object: the staircase X, rank = sum of coords; chain = set of rank values
ranks = sorted(set(sum(t) for t in X))
chain1 = [(r,) for r in range(len(ranks))]        # its rank chain, relabelled 0..m
ranks2 = sorted(set(t[0] for t in chain1))
chain2 = [(r,) for r in range(len(ranks2))]
print("collapse: |chain(X)| =", len(chain1), "| chain(chain(X)) == chain(X):", chain1==chain2)

# fill at D=1: a one-coordinate index over its own alphabet
alpha = sorted(set(t[0] for t in X))
print("D=1 projection: alphabet", alpha, "-> fill =", len(alpha), "/", len(alpha), "= 1.000 (forced: alphabet = values appearing)")