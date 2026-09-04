import math
print("  Sc II   Z = 21, c = 2, Nₑ = 20   —  same electron count as Ca I\n")
print("      ground : 3d.4s  ³D₁  at 0.00\n")
print("  THE LOW-LYING CONFIGURATIONS, AND WHAT EACH COSTS\n")
LV=[("3d.4s","3D",0.00),("3d.4s","1D",2540.95),
    ("3d²","3F",4802.87),("3d²","1D",10944.56),
    ("4s²","1S",11736.36),("3d²","3P",12074.10),
    ("3d²","1G",14261.32),("3d²","1S",25955.2),
    ("3d.4p","1D*",26081.34),("3d.4p","3F*",27443.71),
    ("4s.4p","3P*",39002.20),("4s.4p","1P*",55715.36)]
print(f"      {'configuration':<10}{'term':>6}{'level':>12}")
for c,t,e in LV: print(f"      {c:<10}{t:>6}{e:>12.2f}")
print()
print("  THE ORDERING SC II DECLARES\n")
print("      3d.4s      0        one 3d, one 4s")
print("      3d²     4803        BOTH in 3d  — costs 4803 cm⁻¹")
print("      4s²    11736        BOTH in 4s  — costs 11736 cm⁻¹\n")
print("      → 3d² beats 4s² by 6933 cm⁻¹. at charge 2, 3d is ALREADY favoured.\n")
print("  AND THE SAME THREE ACROSS THE Nₑ = 20 LADDER\n")
print(f"      {'species':<9}{'c':>3}{'3d.4s':>10}{'3d²':>10}{'4s²':>10}"
      f"{'  ground':>12}")
print(f"      {'Ca I':<9}{1:>3}{20335:>10}{'—':>10}{0:>10}{'  4s²':>12}")
print(f"      {'Sc II':<9}{2:>3}{0:>10}{4803:>10}{11736:>10}{'  3d.4s':>12}")
print(f"      {'Ti III':<9}{3:>3}{38064:>10}{0:>10}{102665:>10}{'  3d²':>12}")
print()
print("      the three configurations reorder COMPLETELY across three charges:")
print("          c = 1 :  4s²  <  3d.4s  <  3d²")
print("          c = 2 :  3d.4s  <  3d²  <  4s²")
print("          c = 3 :  3d²  <  3d.4s  <  4s²")
print()
print("      a full reversal — 4s² goes from lowest to highest in two steps.\n")
print("  THE SPLITTING, IN cm⁻¹\n")
print(f"      {'':<9}{'E(3d²) − E(4s²)':>20}")
for nm,v in (("Ca I",20335*2-0),("Sc II",4803-11736),("Ti III",0-102665)):
    print(f"      {nm:<9}{v:>20,}")
print()
print("      Ca I : +40670   (3d² far above 4s², estimated from 2×3d.4s)")
print("      Sc II:  −6933")
print("      Ti III: −102665")
print()
print("      the gap swings by ~143,000 cm⁻¹ over two charge steps — 17 eV.")
print("      THAT is the quantity the aufbau order is about, and it is a")
print("      two-electron energy, not a quantum defect.")
