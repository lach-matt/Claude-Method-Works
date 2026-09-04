import sys; sys.path.insert(0,"/tmp")
import li_mod as li, random
from itertools import product

def trial(n, dims, seed):
    """random n-cell set on `dims` grid with axis 0 INJECTIVE (a key)."""
    rnd = random.Random(seed)
    rows = rnd.sample(range(dims[0]), n)
    cells = {(rows[i],) + tuple(rnd.randrange(d) for d in dims[1:]) for i in range(n)}
    return cells if len(cells)==n else None

print(f"{'d':>3}{'cells':>7}{'trials':>8}{'minE>0':>9}   grid")
for dims,n in [([4,5,2],4),([4,5,3],4),([6,4,3],6),([6,4,4],6),([7,4,4],7)]:
    got=tot=0
    for s in range(120):
        c = trial(n,dims,s)
        if not c: continue
        tot+=1
        if li.minE(c,dims)[0] > 0: got+=1
    print(f"{len(dims):>3}{n:>7}{tot:>8}{got:>9}   {dims}")