import eldata as ed
CAP={0:2,1:6,2:10,3:14,4:18}
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP[l]+1)]
ground=set(ed.E[z] for z in ed.E)
def leq(x,y): return all(p<=q for p,q in zip(x,y))

print("="*78)
print("D2: THE VALENCE CELL OF DOCUMENTED EXCITED STATES")
print("="*78)
print("""  For each element, take the subshell into which the valence electron is
  promoted in its lowest documented excited configuration, and record the
  resulting (n,ℓ,k) valence cell. Representative cases from standard
  atomic spectra:""")
# element: (excited valence subshell, resulting k)
EXC = {
 1:(2,1,1),   # H  1s->2p
 2:(2,0,1),   # He 1s2 -> 1s2s
 3:(2,1,1),   # Li 2s->2p
 4:(2,1,1),   # Be 2s2->2s2p
 5:(3,0,1),   # B  2p->3s
 6:(3,0,1),   # C
 11:(3,1,1),  # Na 3s->3p
 12:(3,1,1),  # Mg
 19:(3,2,1),  # K  4s->3d
 20:(3,2,1),  # Ca 4s2->4s3d
 26:(4,1,1),  # Fe 3d->4p
 29:(4,1,1),  # Cu
 37:(5,1,1),  # Rb
 38:(4,2,1),  # Sr 5s2->5s4d
 55:(6,1,1),  # Cs
 56:(5,2,1),  # Ba 6s2->6s5d
 57:(4,3,1),  # La 5d->4f
 79:(6,1,1),  # Au
 87:(7,1,1),  # Fr
 88:(6,2,1),  # Ra 7s2->7s6d
 89:(5,3,1),  # Ac 6d->5f
}
D2=set(EXC.values())
print(f"\n  documented excited valence cells: {len(D2)} distinct")
new=sorted(D2-ground)
print(f"  of which NOT already in the ground-state set: {len(new)}")
if new:
    for c in new: print(f"    {c}")
else:
    print("    none")
print()
cols_g=set((n,l) for (n,l,k) in ground)
cols_e=set((n,l) for (n,l,k) in D2)
print(f"  columns touched by excited states: {sorted(cols_e)}")
print(f"  columns NOT already occupied:      {sorted(cols_e-cols_g) or 'none'}")

print()
print("="*78)
print("THE UNION Λ_g ∪ Λ_exc — DOES IT DIFFER FROM Λ_g?")
print("="*78)
U=ground|D2
print(f"  |Λ_g| = {len(ground)},  |Λ_g ∪ Λ_exc| = {len(U)},  identical? {U==ground}")
def is_ideal(S): return not any(leq(y,x) and y not in S for x in S for y in L)
def partial_cols(S):
    cols=set((n,l) for (n,l,k) in S); out=[]
    for (n,l) in cols:
        h=max(k for (nn,ll,k) in S if (nn,ll)==(n,l))
        if h!=CAP[l]: out.append(((n,l),h,CAP[l]))
    return out
print(f"  union is an order ideal: {is_ideal(U)}")
print(f"  union all-or-nothing:    {'yes' if not partial_cols(U) else partial_cols(U)}")

print()
print("="*78)
print("CONCLUSION")
print("="*78)
print("""  Every documented excited valence cell already lies in the ground-state
  set. The union is the ground-state set. Both structural properties are
  therefore unchanged, trivially.

  The reason is the same as for D1 and for the low-lying test earlier:
  excitation promotes an electron into a subshell that the aufbau
  sequence reaches at slightly higher Z, and the periodic system already
  contains those elements. Excitation moves an atom to a cell some OTHER
  element already occupies as its ground state.

  For an excited state to reach a genuinely new cell it would have to
  populate 5g, 6f, 6g, 7d, 7f or 7g — the six empty columns. Those lie
  above the aufbau frontier and no neutral atom to Z=118 reaches them.""")