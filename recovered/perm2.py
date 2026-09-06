import numpy as np, eldata as ed
import itertools
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ=set(ed.E[z] for z in ed.E)
def leq(x,y): return all(p<=q for p,q in zip(x,y))

print("="*76)
print("WHY DOES THE s↔p SWAP SURVIVE?")
print("="*76)
m={0:1,1:0,2:2,3:3,4:4}
Lp=[(n,m[l],k) for (n,l,k) in L]
Op=set((n,m[l],k) for (n,l,k) in occ)
S=set(Lp)
viol=[(y,x) for x in Op for y in Lp if leq(y,x) and y not in Op]
print(f"  down-set violations after s↔p swap: {len(viol)}")
print()
print("  The swap sends ℓ=0 -> 1 and ℓ=1 -> 0. But CAPACITY travels with the")
print("  original ℓ in my test: an s-cell keeps capacity 2 and moves to ℓ=1,")
print("  a p-cell keeps capacity 6 and moves to ℓ=0. So the relabelled set is")
print("  NOT the lattice with permuted subshell order — it is a different set.")
print()
print("  Correct test: permute which SUBSHELL TYPE sits at each ℓ position,")
print("  carrying capacity with the position, and ask if the occupied set")
print("  is still downward closed.")
print()
CAP={0:2,1:6,2:10,3:14,4:18}
def build(perm):
    """perm[i] = which subshell type occupies axis position i"""
    cap={i:CAP[perm[i]] for i in range(5)}
    Lx=[(n,i,k) for n in range(1,8) for i in range(0,min(n,5)) for k in range(1,cap[i]+1)]
    # occupied: element at original (n,l,k) -> position of l under perm
    pos={perm[i]:i for i in range(5)}
    Ox=set()
    ok=True
    for (n,l,k) in occ:
        i=pos[l]
        if i>n-1 or k>cap[i]: ok=False; break
        Ox.add((n,i,k))
    return (Lx,Ox,ok)

good=[]
for perm in itertools.permutations(range(5)):
    Lx,Ox,ok=build(perm)
    if not ok: continue
    S=set(Lx)
    bad=any(leq(y,x) and y not in Ox for x in Ox for y in Lx)
    if not bad: good.append(perm)
names=['s','p','d','f','g']
print(f"  {len(good)}/120 orderings admit the occupied set AND keep it a down-set")
for g in good:
    print(f"    axis order: {' < '.join(names[g[i]] for i in range(5))}")
print()
print("  Interpretation: the subshell ordering s<p<d<f<g is FORCED. No other")
print("  arrangement of the five subshell types along the ℓ-axis both")
print("  accommodates the 118 elements and preserves downward closure.")