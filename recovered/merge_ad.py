import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
print("  WHERE DO a AND δ EACH SIT?\n")
print("      δ  lives in Λ_spectra : (Z, c, ℓ, 2S+1) → one δ per channel")
print("      a  lives in Λ_var     : the single output, per element\n")
print("      and a = δ/√p, so they are one object under a change of scale.\n")
print("  THE AXES OF EACH\n")
A=[("Λ_spectra","Z","the nucleus","shared"),
   ("Λ_spectra","c","the charge","shared"),
   ("Λ_spectra","ℓ","the Rydberg electron's angular momentum","shared"),
   ("Λ_spectra","2S+1","the coupling","δ only"),
   ("Λ_var","body","nucleus/core/rydberg and pairs","shared as (Z,c,ℓ)"),
   ("Λ_var","role","input/intermediate/output","a only"),
   ("Λ_walk","Z","the element","shared with Λ_spectra's Z"),
   ("Λ_walk","the carried state","a itself","a only")]
print(f"      {'index':<12}{'axis':<18}{'what it is':<40}{'status'}")
for i,ax,w,s in A: print(f"      {i:<12}{ax:<18}{w:<40}{s}")
print()
print("  THE MERGE\n")
print("      shared: Z, c, ℓ.  δ adds 2S+1.  a adds the carried state.")
print("      so the merged index is  (Z, c, ℓ, 2S+1, n)  where n is the")
print("      PRINCIPAL NUMBER of the channel — which Λ_spectra never had")
print("      (register: 'Λ_spectra has no principal quantum number') and")
print("      which the walk supplies, because a is defined per subshell.\n")
print("      MERGED AXES : (Z, c, n, ℓ, 2S+1)\n")
print("      and the object in each cell is a = δ/√(n−ℓ−1), one number.\n")
print("  WHICH RESOLVES THE OLD DEFECT\n")
print("      Λ_spectra on (Z,c,ℓ,2S+1) gave E = 1929, and on (u,ℓ,2S+1) E = 9")
print("      mostly binning. neither had n. the walk's index has n and no c.")
print("      the merge has both — and it is the FIRST index in this work whose")
print("      cells are (species, subshell) rather than (species) or (channel).")
print()
print("  THE COUNT\n")
ns=0
for Z in range(1,109):
    ns+=len([1 for n,l,o in G.expand(Z) if o>0])
print(f"      (species, subshell) cells for the 108 neutrals : {ns}")
print(f"      channels held in Λ_spectra                     : 328")
print(f"      elements in the walk                           : 106")
print()
print("      → the merged index is larger than either parent and contains")
print("        both as projections: drop n and 2S+1 → the walk; drop the")
print("        carried state → Λ_spectra.")