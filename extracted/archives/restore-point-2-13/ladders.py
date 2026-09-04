import math
L="spdfg"
# (Ne, c, Z, [(n,l,occ)...]) — valence only, the [core] is closed
LAD={
20:[(1,20,[(4,0,2)]),(2,21,[(3,2,1),(4,0,1)]),(3,22,[(3,2,2)]),(4,23,[(3,2,2)])],
38:[(1,38,[(5,0,2)]),(2,39,[(4,2,1),(5,0,1)]),(3,40,[(4,2,2)]),(4,41,[(4,2,2)])],
56:[(1,56,[(6,0,2)]),(2,57,[(5,2,2)]),(3,58,[(4,3,2)])],
88:[(1,88,[(7,0,2)]),(2,89,[(7,0,2)]),(3,90,[(5,3,1),(6,2,1)])]}
# p = n - l - 1 for each candidate; rivals are the other valence options
RIV={20:[(4,0),(3,2),(4,1)],38:[(5,0),(4,2),(5,1)],
     56:[(6,0),(5,2),(4,3),(6,1)],88:[(7,0),(6,2),(5,3),(7,1)]}
print("  THE BRACKETS ON a, PER CHARGE  —  ν = n − a√(n−ℓ−1)\n")
print("      the OCCUPIED subshell must have least ν among the rivals.\n")
print(f"      {'Nₑ':>4}{'c':>3}{'Z':>4}{'occupied':>12}{'a >':>10}{'a <':>10}{'  feasible'}")
OUT={}
for ne in sorted(LAD):
    for c,Z,cfg in LAD[ne]:
        occ=[(n,l) for n,l,o in cfg]
        lo,hi=-1e9,1e9
        for gn,gl in occ:
            gp=gn-gl-1
            for rn,rl in RIV[ne]:
                if (rn,rl) in occ: continue
                rp=rn-rl-1
                d=math.sqrt(rp)-math.sqrt(gp); r=rn-gn
                if abs(d)<1e-12: continue
                if d>0: hi=min(hi,r/d)
                else:   lo=max(lo,r/d)
        s="+".join(f"{n}{L[l]}{o}" for n,l,o in cfg)
        f="yes" if lo<hi else "NO"
        print(f"      {ne:>4}{c:>3}{Z:>4}{s:>12}"
              f"{(lo if lo>-1e8 else float('-inf')):>10.3f}"
              f"{(hi if hi<1e8 else float('inf')):>10.3f}   {f}")
        OUT[(ne,c)]=(lo,hi)
    print()
print("  DOES a DEPEND ON c AT FIXED Nₑ?\n")
for ne in sorted(LAD):
    v=[(c,OUT[(ne,c)]) for c,_,_ in LAD[ne]]
    LO=max(x[1][0] for x in v); HI=min(x[1][1] for x in v)
    print(f"      Nₑ = {ne:>3} : intersection over all charges = "
          f"({LO if LO>-1e8 else float('-inf'):.3f}, {HI if HI<1e8 else float('inf'):.3f})"
          f"   {'ONE a serves the ladder' if LO<HI else 'EMPTY — a MUST vary with c'}")
print()
print("  AND AT FIXED c ACROSS Nₑ?\n")
for c in (1,2,3,4):
    v=[OUT[(ne,c)] for ne in sorted(LAD) if (ne,c) in OUT]
    if len(v)<2: continue
    LO=max(x[0] for x in v); HI=min(x[1] for x in v)
    print(f"      c = {c} : {len(v)} ladders · "
          f"({LO if LO>-1e8 else float('-inf'):.3f}, {HI if HI<1e8 else float('inf'):.3f})"
          f"   {'feasible' if LO<HI else 'EMPTY'}")
