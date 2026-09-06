from itertools import combinations, product

def closed(cells):
    S=set(cells)
    jn=lambda a,b: tuple(max(x,y) for x,y in zip(a,b))
    mt=lambda a,b: tuple(min(x,y) for x,y in zip(a,b))
    return all(jn(a,b) in S and mt(a,b) in S for a,b in combinations(cells,2))

BOX=list(product(range(6),repeat=3))

print("="*74)
print("VERIFY: are the atomic constraint types individually sublattices,")
print("and is their intersection a sublattice?")
print("="*74)
atoms = {
 'x0 ≤ x1'      : [c for c in BOX if c[0]<=c[1]],
 'x1 ≤ x2'      : [c for c in BOX if c[1]<=c[2]],
 'x0 ≤ 3'       : [c for c in BOX if c[0]<=3],
 'x2 ≥ 2'       : [c for c in BOX if c[2]>=2],
 'x0 ≤ 2·x1'    : [c for c in BOX if c[0]<=2*c[1]],
 'x0 ≤ x1 + 1'  : [c for c in BOX if c[0]<=c[1]+1],
}
for nm,S in atoms.items():
    print(f"  {nm:<16} |S|={len(S):4d}  sublattice: {closed(S)}")

print("\n  pairwise and triple intersections:")
names=list(atoms)
for a,b in combinations(names,2):
    I=[c for c in atoms[a] if c in set(atoms[b])]
    if I: print(f"    {a} ∧ {b:<14} |I|={len(I):4d}  sublattice: {closed(I)}")
tri=[c for c in atoms['x0 ≤ x1'] if c in set(atoms['x1 ≤ x2']) and c in set(atoms['x2 ≥ 2'])]
print(f"    triple                        |I|={len(tri):4d}  sublattice: {closed(tri)}")

print()
print("="*74)
print("COUNTEREXAMPLE CLASS: negated coordinate breaks it")
print("="*74)
neg = {
 '−x0 ≤ x1  (i.e. x0 ≥ −x1)' : [c for c in BOX if -c[0]<=c[1]],   # trivially all
 '|x0−2| ≤ x1'               : [c for c in BOX if abs(c[0]-2)<=c[1]],
 'x0 + x1 ≤ 4'               : [c for c in BOX if c[0]+c[1]<=4],
}
for nm,S in neg.items():
    print(f"  {nm:<28} |S|={len(S):4d}  sublattice: {closed(S)}")

print()
print("="*74)
print("APPLY TO Λ AND Λ′ AS INTERSECTIONS OF ATOMS")
print("="*74)
L=[(n,l,k) for n in range(1,8) for l in range(0,5) for k in range(1,19)]
c1=[c for c in L if c[1]<=c[0]-1]
c2=[c for c in c1 if c[2]<=2*(2*c[1]+1)]
print(f"  full box (n≤7, ℓ≤4, k≤18)          |S|={len(L):4d}  sublattice: {closed(L)}")
print(f"  + constraint ℓ ≤ n−1                |S|={len(c1):4d}  sublattice: {closed(c1)}")
print(f"  + constraint k ≤ 2(2ℓ+1)  = Λ       |S|={len(c2):4d}  sublattice: {closed(c2)}")
print("   → Λ is built by intersecting sublattices; closure is inherited.")
print()
H=[(n,l,m,s) for n in range(1,8) for l in range(0,5) for m in range(-4,5) for s in (-1,1)]
h1=[c for c in H if c[1]<=c[0]-1]
h2=[c for c in h1 if c[2]<=c[1]]
h3=[c for c in h2 if -c[2]<=c[1]]
print(f"  hydrogenic box                      |S|={len(H):4d}  sublattice: {closed(H)}")
print(f"  + ℓ ≤ n−1                           |S|={len(h1):4d}  sublattice: {closed(h1)}")
print(f"  + m ≤ ℓ                             |S|={len(h2):4d}  sublattice: {closed(h2)}")
print(f"  + −m ≤ ℓ   = Λ′                     |S|={len(h3):4d}  sublattice: {closed(h3)}")
print("   → the failure enters at exactly the last step: the negated m.")