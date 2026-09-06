# The string partition function index: Z(q) = prod_{n>=1} (1 - q^n)^{-24} = sum_N d(N) q^N.
# d(N) = number of ways to write N as a sum of parts, each part n available in 24 colours
#      = p_24(N), the 24-coloured partitions of N (transverse oscillator states at level N).
# The INDEX: a string state is a choice of occupation numbers for oscillators (n, i),
#   n>=1 the mode, i in 1..24 the transverse dimension; total level N = sum n * occ(n,i).
# "An index with multiplicity": level N carries a COUNT d(N), not a boolean.
# It CLOSES (E=0) because the modes are INDEPENDENT — the admissible set of occupation vectors is
# a full product (each oscillator occupancy free in Z>=0), and a product/box closes trivially (§31.2.3,
# §11.7 independence case). We verify: (a) compute d(N) from the product; (b) confirm the closure of
# the occupation-vector index is the full box => E=0.

# (a) d(N) via the generating function prod (1-q^n)^{-24}, series to level M.
M = 14  # the source notes V~147 at N~14; compute d(N) up to here
coeff = [0]*(M+1); coeff[0]=1
for n in range(1, M+1):
    # multiply current series by (1-q^n)^{-24} = sum_{k>=0} C(k+23,23) q^{n k}
    from math import comb
    factor = [0]*(M+1)
    k=0
    while n*k <= M:
        factor[n*k] = comb(k+23,23)
        k+=1
    new=[0]*(M+1)
    for a in range(M+1):
        if coeff[a]==0: continue
        for b in range(M+1-a):
            if factor[b]==0: continue
            new[a+b]+=coeff[a]*factor[b]
    coeff=new
print("d(N) = 24-coloured partition counts (string level degeneracies):")
for N in range(0, M+1):
    print(f"  d({N}) = {coeff[N]}")

# (b) The closure of the occupation index. Take a TRUNCATED version we can enumerate exactly:
# oscillators (n,i) for n in 1..nmax, i in 1..ncol, occupancy 0..occmax; the admissible set is the
# FULL product (independence). R of a full product box is itself => E=0. Demonstrate on a small case
# and confirm the count factorises (the partition function is the product = the box's generating fn).
from itertools import product as prod
def E_of_box(dims):
    # dims: list of coordinate sizes; admissible = full box; R(box)=box; E=0 by construction.
    # verify via join/meet closure that a full box is closed.
    import itertools
    axes=[range(d) for d in dims]
    box=set(itertools.product(*axes))
    # join/meet closure
    S=set(box); 
    # a full product is a lattice already; check closed:
    closed=True
    L=list(S)
    for a in L:
        for b in L:
            jn=tuple(max(x,y) for x,y in zip(a,b)); mt=tuple(min(x,y) for x,y in zip(a,b))
            if jn not in S or mt not in S: closed=False; break
        if not closed: break
    return len(box), closed

sz, closed = E_of_box([3,3,3])  # 3 oscillators, occupancy 0..2 each (toy)
print(f"\ntoy occupation box 3x3x3: |box|={sz}, closed under join/meet = {closed}, E=0 = {closed}")
print("independence => admissible set is the full product => E=0 (a box always closes).")