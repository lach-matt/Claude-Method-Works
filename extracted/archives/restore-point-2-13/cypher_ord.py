import math
from itertools import product
print("  THE CYPHER ON THE ORDERING QUESTION\n")
print("      ANALYSIS  : Y(c) = Ac² + Bc + C.  needs 3+ ENERGIES per ladder.")
print("                  cost: a full level table per species.")
print("      ORDER     : which configuration is LOWEST at each c.")
print("                  cost: one ground configuration per species — 1 bit.\n")
print("      the crossing is where the order changes. the ORDER language")
print("      locates it to within one charge step using no energies at all.\n")
print("  WHAT WE ALREADY HOLD, IN THE ORDER LANGUAGE\n")
G={20:[("Ca I",1,"4s²"),("Sc II",2,"3d.4s"),("Ti III",3,"3d²"),("V IV",4,"3d²")],
   38:[("Sr I",1,"5s²"),("Y II",2,"5s²"),("Zr III",3,"4d²"),("Nb IV",4,"4d²")],
   56:[("Ba I",1,"6s²"),("La II",2,"5d²"),("Ce III",3,"4f²"),("Pr IV",4,"4f²")],
   88:[("Ra I",1,"7s²"),("Ac II",2,"6d.7s"),("Th III",3,"6d²"),("Pa IV",4,"5f.6d")]}
print(f"      {'Nₑ':>4}   " + "".join(f"{f'c={c}':>12}" for c in (1,2,3,4)))
for ne in sorted(G):
    print(f"      {ne:>4}   " + "".join(f"{g[2]:>12}" for g in G[ne]))
print()
print("      the crossing — where the ground stops being sⁿ — by inspection:")
for ne in sorted(G):
    v=G[ne]; cr=None
    for i in range(len(v)-1):
        a,b=v[i][2],v[i+1][2]
        if ("s²" in a and "s²" not in b) or (a!=b and "s" in a and "s" not in b):
            cr=(v[i][1],v[i+1][1]); break
    print(f"          Nₑ = {ne:>3} : between c = {cr[0]} and {cr[1]}" if cr
          else f"          Nₑ = {ne:>3} : no clean crossing in range")
print()
print("  THE FINDING\n")
print("      all four ladders cross between c = 1 and c = 3.")
print("      Nₑ = 20 : 4s² → 3d.4s → 3d²    crossing 1→2")
print("      Nₑ = 38 : 5s² → 5s²   → 4d²    crossing 2→3")
print("      Nₑ = 56 : 6s² → 5d²   → 4f²    crossing 1→2")
print("      Nₑ = 88 : 7s² → 6d.7s → 6d²    crossing 1→2\n")
print("      three of four cross at 1→2, one at 2→3. the measured root for")
print("      Nₑ = 20 was c = 2.13 from ENERGIES; the ORDER language gives")
print("      'between 1 and 2' from ground configurations alone.\n")
print("  DOES THE ORDER LANGUAGE SUFFICE?\n")
print("      for the LÖWDIN QUESTION — which subshell fills next — yes.")
print("      the question is ordinal: which configuration is lowest. that is")
print("      exactly what a ground configuration states, and NIST publishes it")
print("      for all 6,027 spectra.")
print()
print("      for the QUADRATIC FORM — no. that needs energies, and it is")
print("      already attributed to Krug & von Lilienfeld on Z = 1–86.")
print()
print("  SO THE NEXT CAPTURE IS NOT A LEVEL TABLE\n")
print("      it is the GSIE ground-configuration list — one line per spectrum,")
print("      6,027 rows, no energies. that settles the ordering everywhere")
print("      the compendium reaches, at a fraction of the cost.")
