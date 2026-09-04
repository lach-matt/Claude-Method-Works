import math
from itertools import product, permutations
# index, WHAT it indexes, coords, cells, E, closes, CARRIER SET
IX=[("Λ","atoms/transfers",8,976,0,"yes","n,ℓ,k,q,e,f,g,S"),
    ("Λ_spectra","channels",4,328,">0","no","Z,c,ℓ,2S+1"),
    ("Λ_phys","parameters",4,22,57,"no","kind,source,domain,arity"),
    ("Λ_law","laws",2,7,0,"yes","law,carrier"),
    ("Λ_const","constants",2,14,0,"yes","role,carrier"),
    ("Λ_var","variables",3,12,4,"no","body,type,role"),
    ("Λ_ryd","series",3,10,4,"no","order,ℓ,sign")]
print("  THE SEVEN INDEXES AS ONE OBJECT\n")
print(f"      {'index':<12}{'indexes':<18}{'coords':>7}{'cells':>7}{'E':>6}{'closes':>8}")
for n,w,c,ce,e,cl,car in IX:
    print(f"      {n:<12}{w:<18}{c:>7}{ce:>7}{str(e):>6}{cl:>8}")
print()
print("  THE CYPHER QUESTION — do the six languages agree across all seven?\n")
print("      ORDER       : does the index close?  Λ, Λ_law, Λ_const — YES")
print("                    Λ_spectra, Λ_phys, Λ_var, Λ_ryd — NO")
print("      ANALYSIS    : is there a continuous law on it?")
print("                    Λ_spectra yes (δ), Λ_law yes (the laws), others no")
print("      ALGEBRA     : is it a lattice under ℛ?  all seven, by construction")
print("      GEOMETRY    : does it embed in a product?  all seven, by construction")
print("      INFORMATION : does a coordinate add join-irreducibles?")
print("                    tested on Λ_spectra (δ costs 45%), Λ_var, Λ_const")
print("      STATISTICS  : are the cells drawn from a distribution?")
print("                    Λ_spectra yes, the rest are enumerations\n")
print("  WHAT THE FOUR NON-CLOSING INDEXES HAVE IN COMMON\n")
BAD=[x for x in IX if x[5]=="no"]
for n,w,c,ce,e,cl,car in BAD:
    print(f"      {n:<12}{car}")
print()
print("      Λ_phys : coordinates are kind/source/domain — SOURCE is the observer")
print("      Λ_var  : had 'origin' — given/read/derived — the observer again")
print("      Λ_ryd  : indexed by ℓ where the carrier is p — WRONG CARRIER")
print("      Λ_spectra: (Z, c, ℓ, 2S+1) — but c appears in THREE positions\n")
print("  THE THREE FAULTS, NAMED\n")
print("      1 · OBSERVER ON AN OBJECT AXIS   Λ_phys (source), Λ_var (origin),")
print("          Λ_const (standing, removed).  removing it closed Λ_const and Λ_var")
print("          went from E=6 to E=4.")
print()
print("      2 · WRONG CARRIER                Λ_ryd indexed by ℓ; its law sorts by p.")
print("          the same fault took law 2 from r² 0.868 (fake) to 0.356 (real).")
print()
print("      3 · ONE SYMBOL, THREE POSITIONS  Λ_spectra's c is in u, in c^(−x),")
print("          and inside x itself. no monotone envelope can hold that.")
print()
print("  AND THE PREDICTION\n")
print("      if the three faults are the whole story, then:")
print("        Λ_phys closes when 'source' is dropped")
print("        Λ_var  closes when the remaining observer trace is found")
print("        Λ_ryd  closes when re-indexed on p")
print("        Λ_spectra closes when c is split into its three roles")
print()
print("      three are testable now. the fourth is the Löwdin problem itself.")