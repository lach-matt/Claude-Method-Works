import eldata as ed
CAP={0:2,1:6,2:10,3:14,4:18}
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP[l]+1)]
ground=set(ed.E[z] for z in ed.E)
def leq(x,y): return all(p<=q for p,q in zip(x,y))

print("="*78)
print("READING A, VARIANT: HIGHER EXCITATIONS")
print("="*78)
print("""  Previous tests used the LOWEST excited configuration. Atomic spectra
  document Rydberg series extending to high n. Sodium alone has documented
  levels up to n≈60. So the question is whether high excitations reach
  cells no ground state occupies.

  A hydrogen atom excited to n=7 has valence (7,ℓ,1) for ℓ up to 6.
  Within Λ's ceiling ℓ≤4, that gives (7,0,1) ... (7,4,1).""")
print()
# Rydberg reachable cells for a one-electron-excited atom: (n, l, 1) any admissible n,l
rydberg=set((n,l,1) for n in range(1,8) for l in range(0,min(n,5)))
print(f"  singly-excited Rydberg cells (n,ℓ,1): {len(rydberg)}")
new=sorted(rydberg-ground)
print(f"  NOT in the ground-state set: {len(new)}")
for c in new: print(f"    {c}   = {c[0]}{'spdfg'[c[1]]}¹")
print()
U=ground|rydberg
print(f"  |Λ_g| = {len(ground)}   |Λ_g ∪ Rydberg| = {len(U)}")
def is_ideal(S): return not any(leq(y,x) and y not in S for x in S for y in L)
def partial(S):
    cols=set((n,l) for (n,l,k) in S); out=[]
    for (n,l) in cols:
        h=max(k for (nn,ll,k) in S if (nn,ll)==(n,l))
        if h!=CAP[l]: out.append(((n,l),h,CAP[l]))
    return out
print(f"  union is an order ideal:  {is_ideal(U)}")
p=partial(U)
print(f"  union all-or-nothing:     {'yes' if not p else 'NO'}")
if p:
    print("    partially-filled columns introduced:")
    for c,h,cap in p: print(f"      {c[0]}{'spdfg'[c[1]]}: height {h} of {cap}")
print()
print("="*78)
print("THIS IS THE FIRST CONSTRUCTION THAT CHANGES ANYTHING")
print("="*78)
print("""  Rydberg excitation DOES reach the six empty columns — a hydrogen atom
  promoted to 5g occupies (5,4,1). So Λ_exc ⊋ Λ_g under this definition.

  But note what it costs: the resulting set has partially-filled columns
  (height 1 of 18 for 5g, etc.), so the ALL-OR-NOTHING property fails.
  And whether it remains an order ideal is reported above.""")