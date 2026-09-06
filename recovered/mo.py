import sys, math, re; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def corr(Z):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]; gp=gn-gl-1; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    lo,hi=-INF,INF; bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0 and r/d<hi: hi,bhi=r/d,(n,l)
        if d<0 and r/d>lo: lo=r/d
    return (gn,gl),lo,hi,bhi,pr
print("  BLOCK 5 (n+l = 5, Z 21-38) AND BLOCK 6 (Z 39-56) — where a ascends.\n")
print("  the rule fails at Mo because a had risen to 1.3660. WHERE did it rise?\n")
a=None
print(f"  {'Z':>4}{'el':>4}{'enters':>7}{'floor L':>10}{'ceiling U':>11}"
      f"{'a after':>10}{'  note'}")
for Z in range(39,49):
    c=corr(Z)
    if not c: continue
    g,lo,hi,bhi,pr=c
    if a is None or Z==39: a = lo if lo>-INF/2 and abs(lo)>1e-9 else 0.0
    na = max(a,lo) if lo>-INF/2 else a
    note=""
    if na>hi+1e-9: note="VIOLATION"; na = lo if lo>-INF/2 and abs(lo)>1e-9 else hi
    elif na!=a: note="rise"
    a=na
    f=lambda x:("-inf" if x<-INF/2 else "inf" if x>INF/2 else f"{x:.4f}")
    print(f"  {Z:>4}{G.GROUND[Z][0]:>4}{f'{g[0]}{LS[g[1]]}':>7}{f(lo):>10}{f(hi):>11}"
          f"{a:>10.4f}   {note}")
print("\n  PCAX ON Mo — what does each letter say?\n")
for Z in (41,42,43):
    sym,cfg,term=G.GROUND[Z]
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    c=corr(Z)
    print(f"  {sym} {Z}  {cfg:<18} term {term}")
    print(f"      P  corridor ({c[1]:+.4f}, {c[2]:.4f})  binding rival "
          f"{c[3][0]}{LS[c[3][1]]}  occ {pr.get(c[3],0)}")
    print(f"      C  c = 1 (neutral) — a defining letter across the walk")
    print(f"      A  entering 4d vs rival {c[3][0]}{LS[c[3][1]]}: "
          f"l = 2 and {c[3][1]}  -> Slater F0"
          + (", G2" if c[3][1]==0 else ", G1 G3"))
    print(f"      X  2S+1 = {re.match(r'(\\d+)',term).group(1)}"
          f"   4d occ after = {cu.get((4,2),0)}")
    print()
print("  THE ONE THING Mo HAS THAT Nb AND Tc DO NOT:")
print("      Nb 4d4 5s1  — 4d below half")
print("      Mo 4d5 5s1  — 4d EXACTLY HALF FILLED, 2S+1 = 7, the table's maximum")
print("      Tc 4d5 5s2  — 4d half, but the electron went to 5s")
print("\n  Mo is the ONLY element where the entering electron completes a")
print("  half-filled d shell AND the s shell is already at one.")