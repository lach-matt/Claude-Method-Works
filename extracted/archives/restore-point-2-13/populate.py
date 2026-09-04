import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np, statistics as st
from collections import defaultdict
import ground as G
L="spdfg"
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]
print("  POPULATING THE MERGED INDEX  (Z, c, n, ℓ, 2S+1) → a = δ/√(n−ℓ−1)\n")
print("      Λ_spectra's δ is measured at the SERIES LIMIT — it is δ for the")
print("      channel, not for one n. so the channel's n is n₀ = p+ℓ+1, the")
print("      first member. that is the cell the walk also occupies.\n")
CELLS={}
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    if p<1: continue
    n0=p+l+1
    CELLS[(Z,c,n0,l,S)]=d/math.sqrt(p)
print(f"      {len(CELLS)} cells populated from Λ_spectra\n")
print("  AND THE WALK'S CELLS — from the ionisation energies, c = 1\n")
R=13.605693122994
IE={5:8.298019,6:11.2602880,13:5.985769,14:8.15168,19:4.34066373,20:6.1131549210,
31:5.9993020,32:7.899435,37:4.1771281,38:5.69486745,39:6.21726,49:5.7863558,
50:7.343918,55:3.89390572743,56:5.2116646,81:6.1082873}
W={}
for Z in sorted(IE):
    prd={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>prd.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; gp=gn-gl-1
    if gp<1: continue
    nu=math.sqrt(R/IE[Z]); W[(Z,1,gn,gl)]=(gn-nu)/math.sqrt(gp)
print(f"      {len(W)} cells populated from ionisation energies\n")
print("  WHERE BOTH SOURCES OCCUPY THE SAME (Z, c, n, ℓ)\n")
both=[]
for (Z,c,n,l),aw in sorted(W.items()):
    ms=[(S,v) for (Z2,c2,n2,l2,S),v in CELLS.items()
        if (Z2,c2,n2,l2)==(Z,c,n,l)]
    if ms: both.append((Z,c,n,l,aw,ms))
print(f"      {'Z':>4}{'el':>4}{'shell':>7}{'a from IE':>12}{'a from δ':>22}")
for Z,c,n,l,aw,ms in both:
    s=" ".join(f"{S}:{v:.4f}" for S,v in sorted(ms))
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{f'{n}{L[l]}':>7}{aw:>12.4f}   {s}")
if not both:
    print("      NONE — Λ_spectra's channels are the subshells ABOVE the ground")
    print("      configuration; the ionisation energy is the ground one. the two")
    print("      sources populate DISJOINT cells of the merged index.\n")
    print("      → the merge is real and the sources are complementary, not")
    print("        redundant. that is why they never contradicted before:")
    print("        they were never in the same cell.")
