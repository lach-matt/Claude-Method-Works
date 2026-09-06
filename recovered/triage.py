print("="*76)
print("TRIAGE: what could Λ plausibly speak to, and what can it not?")
print("="*76)
print("""
Λ supplies: a poset structure, an order ideal, fibres, a boundary diagonal,
            a linear functional (Madelung), and dimensionless coordinates.
Λ cannot supply: any dimensional quantity, any rate, any energy scale.

So the test for a candidate application is:
  (a) is the target quantity ORDINAL or STRUCTURAL rather than metric?
  (b) does the answer depend on lattice POSITION rather than lattice DISTANCE?
  (c) is there an established baseline to benchmark against?
""")
cands = [
 ("Superheavy element configuration prediction (Z>118)",
  "ordinal — which cell, not what energy", "YES", "Pyykkö 2011 relativistic calcs", "STRONG"),
 ("Predicting anomalous ground-state configurations",
  "ordinal — which cell is occupied", "YES", "measured configs (Cr, Cu, Pd...)", "STRONG"),
 ("Chemical similarity / group assignment",
  "ordinal — fibre membership", "YES", "Restrepo similarity studies", "MODERATE"),
 ("Ordering elements by any measured property",
  "METRIC — needs real numbers", "NO", "Pettifor, Miedema", "WEAK (already lost)"),
 ("Crystal-structure prediction",
  "METRIC — energies", "NO", "DFT, Miedema", "WEAK"),
 ("Reaction thermochemistry",
  "METRIC — kJ/mol", "NO", "vast literature", "VERY WEAK"),
 ("Isoelectronic series / valence-isoelectronic sets",
  "ordinal — same (l,k) different n", "YES", "standard chemistry", "MODERATE"),
 ("Missing-element prediction in historical periodic tables",
  "structural — which cells were gaps", "YES", "Mendeleev's predictions", "STRONG"),
 ("Chemical space navigation / materials screening",
  "ordinal ranking of candidates", "PARTIAL", "Pettifor maps", "MODERATE"),
]
print(f"{'candidate':<52}{'kind':<34}{'fits?':<8}{'verdict'}")
print("-"*76)
for nm,kind,fits,base,verd in cands:
    print(f"{nm:<52}{kind:<34}{fits:<8}{verd}")
    print(f"{'':52}baseline: {base}")