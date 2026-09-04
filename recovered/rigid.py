import numpy as np, eldata as ed, itertools
occ=set(ed.E[z] for z in ed.E)
CAP={0:2,1:6,2:10,3:14,4:18}
def leq(x,y): return all(p<=q for p,q in zip(x,y))

print("="*76); print("RIGIDITY OF EACH AXIS"); print("="*76)

# --- l-axis (already done) ---
def test_l(perm):
    cap={i:CAP[perm[i]] for i in range(5)}
    Lx=[(n,i,k) for n in range(1,8) for i in range(0,min(n,5)) for k in range(1,cap[i]+1)]
    pos={perm[i]:i for i in range(5)}
    Ox=set()
    for (n,l,k) in occ:
        i=pos[l]
        if i>n-1 or k>cap[i]: return False
        Ox.add((n,i,k))
    return not any(leq(y,x) and y not in Ox for x in Ox for y in Lx)
gl=[p for p in itertools.permutations(range(5)) if test_l(p)]
print(f"  ℓ-axis: {len(gl)}/120 subshell orderings admissible → {'FORCED' if len(gl)==1 else 'not forced'}")

# --- n-axis: permute shell labels 1..7 ---
def test_n(perm):
    pos={perm[i]:i+1 for i in range(7)}   # perm[i]=which shell sits at position i+1
    Lx=[(i+1,l,k) for i in range(7) for l in range(0,min(i+1,5)) for k in range(1,CAP[l]+1)]
    Ox=set()
    for (n,l,k) in occ:
        i=pos[n]
        if l>i-1: return False
        Ox.add((i,l,k))
    return not any(leq(y,x) and y not in Ox for x in Ox for y in Lx)
gn=[p for p in itertools.permutations(range(1,8)) if test_n(p)]
print(f"  n-axis: {len(gn)}/5040 shell orderings admissible → {'FORCED' if len(gn)==1 else 'not forced'}")

# --- k-axis: reverse it? k -> cap+1-k ---
def test_k_rev():
    Lx=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP[l]+1)]
    Ox=set((n,l,CAP[l]+1-k) for (n,l,k) in occ)
    return not any(leq(y,x) and y not in Ox for x in Ox for y in Lx)
print(f"  k-axis reversed (k → cap+1−k): down-set preserved? {test_k_rev()}")

print()
print("="*76); print("WHAT THIS MEANS"); print("="*76)
print("""  All three axis orientations are forced by the requirement that the
  118 occupied cells form a down-set:

    • the subshell order must be s < p < d < f < g   (1 of 120)
    • the shell order must be 1 < 2 < ... < 7        (1 of 5040)
    • the occupancy axis cannot be reversed

  So the lattice admits no relabelling that preserves its central
  structural property. The orientation is not a presentational choice
  — it is determined, given the elements.

  This is a rigidity result: it says the coordinate system is unique up
  to nothing at all, which is a stronger statement than the origin-
  independence of §10 (where translations WERE free).""")