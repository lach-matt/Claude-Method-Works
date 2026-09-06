import math
print("  Sc I   Z = 21, Nₑ = 21   —  the element where 3d is OCCUPIED\n")
print("      ground : 3d.4s²  ²D₃/₂  at 0.0000   (not 4s²4p or 4s²3d excited)")
print("      so scandium's ground configuration is [Ar] 3d¹ 4s².\n")
print("  WHAT THE LEVEL LIST SHOWS — the low-lying structure\n")
LV=[("3d.4s²","2D",1.5,0.0000),("3d.4s²","2D",2.5,168.3371),
    ("3d².(3F).4s","4F",1.5,11519.9611),("3d².(3F).4s","4F",4.5,11677.3121),
    ("3d².(3F).4s","2F",2.5,14926.061),
    ("3d.4s.(3D).4p","4F*",1.5,15672.5595),
    ("3d.4s.(1D).4p","2D*",2.5,16022.7219),
    ("3d².(1D).4s","2D",2.5,17012.753),
    ("3d².(3P).4s","4P",0.5,17226.025),
    ("4s².4p","2P*",0.5,18711.029),
    ("3d².(1G).4s","2G",4.5,20236.877),
    ("3d³","4F",1.5,33763.534)]
print(f"      {'configuration':<16}{'term':>6}{'J':>5}{'level':>13}")
for c,t,j,e in LV: print(f"      {c:<16}{t:>6}{j:>5}{e:>13.4f}")
print()
print("  THE ORDERING SCANDIUM ITSELF DECLARES\n")
print("      3d.4s²      0        the ground state — ONE 3d, TWO 4s")
print("      3d².4s   11520        move a 4s electron into 3d : COSTS 11520 cm⁻¹")
print("      4s².4p   18711        move it into 4p instead    : COSTS 18711 cm⁻¹")
print("      3d³      33764        move both                  : COSTS 33764 cm⁻¹\n")
print("      so at Sc: 3d < 4p, and 4s is filled before either.")
print("      the cost of 4s → 3d is 11520 cm⁻¹ = 1.43 eV.\n")
print("  WHY THE RYDBERG DEFECT CANNOT SETTLE THIS\n")
print("      a Rydberg δ measures ONE electron outside a fixed core.")
print("      the 4s²/3d question is about TWO electrons in the same shell,")
print("      where the 3d-3d and 4s-4s repulsions differ by more than the")
print("      one-electron energies do.")
print()
print("      Sc has no 3d Rydberg SERIES at all in this list — 3d is a")
print("      ground-configuration orbital here, not a Rydberg one. the")
print("      series that exist are 3d.4s.np, 3d².np, and so on: they")
print("      measure an electron outside a 3d-containing core.\n")
print("  WHAT THIS SETTLES\n")
print("      K I's spectrum says n*(3d) < n*(4s), and K fills 4s.")
print("      Sc I's ground state says 3d.4s² beats 3d².4s by 11520 cm⁻¹.")
print("      both are true, and they are about different quantities:")
print("        · the Rydberg defect  — one electron, fixed core")
print("        · the ground configuration — several electrons, mutual repulsion")
print()
print("      the Löwdin ordering is the SECOND. the compendium measures the FIRST.")
print("      that is the gap, stated exactly, and no capture of Rydberg series")
print("      will close it.")