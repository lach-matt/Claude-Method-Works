import eldata as ed, itertools
occ=set(ed.E[z] for z in ed.E)
CAP={0:2,1:6,2:10,3:14,4:18}
def leq(x,y): return all(p<=q for p,q in zip(x,y))

def test_n(perm):
    pos={perm[i]:i+1 for i in range(7)}
    Lx=[(i+1,l,k) for i in range(7) for l in range(0,min(i+1,5)) for k in range(1,CAP[l]+1)]
    Ox=set()
    for (n,l,k) in occ:
        i=pos[n]
        if l>i-1: return None
        Ox.add((i,l,k))
    ok=not any(leq(y,x) and y not in Ox for x in Ox for y in Lx)
    return ok

good=[p for p in itertools.permutations(range(1,8)) if test_n(p)]
print("="*76); print("STEP 1: CHARACTERISE THE 8 PERMUTATIONS"); print("="*76)
for p in good:
    # express as a permutation in cycle notation
    pos={p[i]:i+1 for i in range(7)}
    cyc=[]; seen=set()
    for s in range(1,8):
        if s in seen: continue
        c=[s]; x=pos[s]; seen.add(s)
        while x!=s:
            c.append(x); seen.add(x); x=pos[x]
        if len(c)>1: cyc.append(tuple(c))
    print(f"  {p}   cycles: {cyc if cyc else 'identity'}")

print()
print("="*76); print("STEP 2: DO THEY FORM A GROUP?"); print("="*76)
# represent each as a mapping shell -> position
maps=[]
for p in good:
    maps.append(tuple(p))   # p[i] = shell at position i+1
S=set(maps)
def compose(a,b):
    # a,b as tuples: position i holds shell a[i]
    # composition: apply b then a
    posb={b[i]:i+1 for i in range(7)}
    return tuple(a[posb[s]-1] for s in range(1,8))
closed=all(compose(a,b) in S for a in maps for b in maps)
ident=tuple(range(1,8))
print(f"  identity present: {ident in S}")
print(f"  closed under composition: {closed}")
inv_ok=True
for a in maps:
    posa={a[i]:i+1 for i in range(7)}
    inv=tuple(posa[s] for s in range(1,8))
    if inv not in S: inv_ok=False
print(f"  closed under inverse: {inv_ok}")
print(f"  |G| = {len(S)}")
if closed and inv_ok:
    print("  → the 8 permutations form a GROUP of order 8")