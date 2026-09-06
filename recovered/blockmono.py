import sys, math; sys.path.insert(0,"/home/claude/work")
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
    if (gn,gl) not in cand or len(cand)<2: return None
    lo,hi=-INF,INF
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return (gn,gl),lo,hi
B=[(Z,)+corr(Z) for Z in range(3,109) if corr(Z)]
JANET=[(1,2),(3,4),(5,12),(13,20),(21,38),(39,56),(57,88),(89,118)]
def block(Z):
    for i,(a,b) in enumerate(JANET):
        if a<=Z<=b: return i
    return None
f=lambda x:("-inf" if x<-INF/2 else "inf" if x>INF/2 else f"{x:.4f}")
print("  MONOTONE WITHIN A JANET BLOCK, free to descend AT a block boundary\n")
print("  rule: inside a block a := max(a, L); at a boundary a := L (or U).\n")
a=None; cur=None; fails=[]; moves=[]
for Z,g,lo,hi in B:
    bl=block(Z)
    if bl!=cur:                      # a block opening: free re-placement
        a = lo if lo>-INF/2 and abs(lo)>1e-9 else (hi if hi<INF/2 else 0.0)
        moves.append((Z,'open',a)); cur=bl; continue
    na = max(a, lo) if lo>-INF/2 else a
    if na > hi+1e-9:
        fails.append((Z,na,lo,hi))
        a = lo if lo>-INF/2 and abs(lo)>1e-9 else hi
        moves.append((Z,'forced',a))
    else:
        if na!=a: moves.append((Z,'rise',na))
        a=na
print(f"  violations INSIDE a block: {len(fails)}")
for Z,na,lo,hi in fails:
    print(f"      {G.GROUND[Z][0]:>3} {Z:<4} block {block(Z)}  a={na:.4f} vs "
          f"({f(lo)}, {f(hi)})")
print(f"\n  moves: {len(moves)}  — {sum(1 for _,k,_ in moves if k=='open')} at boundaries,"
      f" {sum(1 for _,k,_ in moves if k=='rise')} rises, "
      f"{sum(1 for _,k,_ in moves if k=='forced')} forced inside")
REC={3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104}
mz={Z for Z,_,_ in moves}
print(f"  matching the recorded eighteen: {len(mz&REC)}   false positives {len(mz-REC)}")
print(f"\n  the trajectory:")
for Z,k,v in moves:
    print(f"      {G.GROUND[Z][0]:>3} {Z:<4} {k:<7} a = {v:.4f}"
          f"   {'RECORDED' if Z in REC else ''}")