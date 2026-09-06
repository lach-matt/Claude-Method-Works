import sys, time, pickle
from itertools import product, permutations, combinations
DIMS=tuple(int(x) for x in sys.argv[1].split(','))
STEP=int(sys.argv[2])
d=len(DIMS); cells=list(product(*[range(x) for x in DIMS])); n=len(cells)
CIDX={c:i for i,c in enumerate(cells)}
JO=[[CIDX[tuple(max(x[k],y[k]) for k in range(d))] for y in cells] for x in cells]
ME=[[CIDX[tuple(min(x[k],y[k]) for k in range(d))] for y in cells] for x in cells]
PERM=[[CIDX[tuple(ps[k][c[k]] for k in range(d))] for c in cells]
      for ps in product(*[list(permutations(range(x))) for x in DIMS])]
def sublat(mask):
    idx=[i for i in range(n) if mask>>i & 1]
    for a in range(len(idx)):
        ia=idx[a]
        for b in range(a+1,len(idx)):
            ib=idx[b]
            if not (mask>>JO[ia][ib] & 1): return False
            if not (mask>>ME[ia][ib] & 1): return False
    return True
def used(mask):
    for k in range(d):
        s=set()
        for i in range(n):
            if mask>>i & 1: s.add(cells[i][k])
        if len(s)<2: return False
    return True
CACHE={}
def reord(mask):
    if mask in CACHE: return CACHE[mask]
    r=False
    for m in PERM:
        nm=0
        for i in range(n):
            if mask>>i & 1: nm|=1<<m[i]
        if sublat(nm): r=True; break
    CACHE[mask]=r; return r
t0=time.time()
# base: all reorderable sets of size 3 with >=2 values per axis
base=set()
for T in combinations(range(n),3):
    m=0
    for i in T: m|=1<<i
    if used(m) and reord(m): base.add(m)
tb=time.time()-t0
print("  box %-12s step %d   base(size 3) %d   %.1fs"%("×".join(map(str,DIMS)),STEP,len(base),tb))
table=set(base); frontier=set(base); rounds=0
while frontier:
    rounds+=1
    new=set()
    for m in frontier:
        off=[i for i in range(n) if not (m>>i & 1)]
        for k in range(1,STEP+1):
            for T in combinations(off,k):
                p=m
                for i in T: p|=1<<i
                if p in table or p in new: continue
                if reord(p): new.add(p)
    frontier=new; table|=new
    print("     round %2d : +%-7d  total %-8d  %.1fs"%(rounds,len(new),len(table),time.time()-t0))
    if rounds>40: break
print("  **table size %d      time %.1fs**"%(len(table),time.time()-t0))
pickle.dump({'dims':DIMS,'step':STEP,'table':sorted(table)},
            open('/home/claude/stage/tbl_%s_%d.pkl'%("x".join(map(str,DIMS)),STEP),'wb'))