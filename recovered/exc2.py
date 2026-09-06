import eldata as ed
CAP={0:2,1:6,2:10,3:14,4:18}
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP[l]+1)]
def leq(x,y): return all(p<=q for p,q in zip(x,y))
ground=set(ed.E[z] for z in ed.E)

print("="*76)
print("TEST: ADMIT LOW-LYING EXCITED CONFIGURATIONS — DOES STRUCTURE SURVIVE?")
print("="*76)
print("""  Spectroscopically documented low-lying excited configurations that
  populate a subshell the element's ground state does not use. Source:
  standard atomic spectra (NIST ASD level designations).""")
# element -> (n,l) newly populated in a low-lying excited state
EXC = {
 3:(2,1),   # Li  2s->2p
 4:(2,1),   # Be  2s2 -> 2s2p
 11:(3,1),  # Na  3s->3p
 12:(3,1),  # Mg
 19:(4,1),  # K   4s->4p
 20:(4,1),  # Ca  also 4s3d
 20+0:(3,2),
 37:(5,1),  # Rb
 38:(5,1),  # Sr
 55:(6,1),  # Cs
 56:(6,1),  # Ba  also 5d
 56+0:(5,2),
 87:(7,1),  # Fr
 88:(7,1),  # Ra
}
# Build an "excited-augmented" occupied set: add the FULL column for any
# (n,l) reached by a low-lying excited state of a known element.
extra_cols={(2,1),(3,1),(4,1),(3,2),(5,1),(6,1),(5,2),(7,1)}
aug=set(ground)
for (n,l) in extra_cols:
    for k in range(1,CAP[l]+1): aug.add((n,l,k))
print(f"\n  ground-state cells: {len(ground)}")
print(f"  after adding excited-reachable columns: {len(aug)}")
newc=sorted(set((n,l) for (n,l,k) in aug)-set((n,l) for (n,l,k) in ground))
print(f"  columns added: {[f'{n}{chr(115+0) if l==0 else chr(112) if l==1 else chr(100)}' for n,l in newc] if newc else 'none — all already occupied'}")
print()
# do the structural properties survive?
def is_ideal(S):
    return not any(leq(y,x) and y not in S for x in S for y in L)
def allornothing(S):
    cols=set((n,l) for (n,l,k) in S)
    bad=[]
    for (n,l) in cols:
        h=max(k for (nn,ll,k) in S if (nn,ll)==(n,l))
        if h!=CAP[l]: bad.append(((n,l),h,CAP[l]))
    return bad
print(f"  ground set is an order ideal:      {is_ideal(ground)}")
print(f"  augmented set is an order ideal:   {is_ideal(aug)}")
print(f"  ground set all-or-nothing:  {'yes' if not allornothing(ground) else allornothing(ground)}")
print(f"  augmented all-or-nothing:   {'yes' if not allornothing(aug) else allornothing(aug)}")
print()
print("""  All the excited-reachable columns (2p, 3p, 3d, 4p, 5p, 5d, 6p, 7p)
  are ALREADY fully occupied by ground states of other elements. So
  admitting low-lying excitation adds nothing to the occupied set.""")
print()
print("="*76)
print("WHY THAT IS NECESSARILY SO")
print("="*76)
print("""  A low-lying excited configuration of element Z promotes an electron
  into a subshell that the aufbau sequence reaches shortly AFTER Z. But
  by construction the periodic system already contains those later
  elements — so the column is already occupied in the ground-state set.

  The only way excitation could add a column is if it reached a subshell
  BEYOND the end of the known series, i.e. 5g, 6f, 6g, 7d, 7f or 7g. No
  neutral atom up to Z=118 has a documented low-lying state populating
  any of those: they lie above the aufbau frontier.

  Conclusion: the order-ideal and all-or-nothing properties are robust
  to admitting excitation. The six empty columns stay empty. Pauli
  capacity was never the constraint — the constraint is that element
  synthesis has not passed Z=118.""")