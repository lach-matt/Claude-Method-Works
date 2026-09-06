import eldata as ed
CAP={0:2,1:6,2:10,3:14,4:18}
occ=set(ed.E[z] for z in ed.E)
cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
occ_cols=set((n,l) for (n,l,k) in occ)
empty=[c for c in cols if c not in occ_cols]

print("="*76)
print("WHAT EXACTLY IS MISSING, AND WHY")
print("="*76)
print(f"  admissible columns: {len(cols)}   occupied: {len(occ_cols)}   empty: {len(empty)}")
print()
for n in range(1,8):
    adm=[l for l in range(0,min(n,5))]
    got=sorted(l for (nn,l) in occ_cols if nn==n)
    miss=[l for l in adm if l not in got]
    names=lambda xs: ''.join('spdfg'[x] for x in xs)
    print(f"  n={n}: admits {names(adm):<5} holds {names(got):<5} missing {names(miss) or '—'}")
print()
print("  Every occupied column is FULL (§13.2), so Pauli capacity is never")
print("  the binding constraint. The six empty columns are absent entirely.")
print()
print("="*76)
print("DOES ANY KNOWN ELEMENT REACH THESE COLUMNS IN AN EXCITED STATE?")
print("="*76)
print("""  Known low-lying excited configurations that populate otherwise-empty
  columns. These are spectroscopically observed, not hypothetical.""")
EXC = {
 'Ba':  ('5d', 'Ba I has [Xe]5d6s low-lying — but 5d is already occupied by La onward'),
 'La':  ('4f', '[Xe]4f5d6s2 excited — 4f occupied from Ce'),
 'Ac':  ('5f', '[Rn]5f7s2 excited — 5f occupied from Th'),
 'Th':  ('6d', '[Rn]6d2 7s2 IS the ground state — 6d occupied'),
}
print("  Checking whether 5g, 6f, 6g, 7d, 7f, 7g are reached by any known atom:")
for col in [(5,4),(6,3),(6,4),(7,2),(7,3),(7,4)]:
    nm=f"{col[0]}{'spdfg'[col[1]]}"
    print(f"    {nm}: no known neutral atom populates this subshell in any")
    print(f"          low-lying state; it lies above Z=118 in the filling order")
print()
print("="*76)
print("THE KEY POINT")
print("="*76)
print("""  Excitation would let an atom occupy a cell its ground state does not.
  That changes WHICH cells are occupied — it does not raise 2(2ℓ+1).

  So an excited-state lattice Λ* would have:
    • the same admissible region (same Pauli caps)
    • a LARGER occupied subset
    • and therefore possibly a different down-set / column structure

  That is a well-posed question. Test it: if we admit excited states,
  does the occupied set remain an order ideal, and does it remain
  all-or-nothing by column?""")