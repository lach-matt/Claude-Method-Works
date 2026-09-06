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
JAN=[(1,2),(3,4),(5,12),(13,20),(21,38),(39,56),(57,88),(89,118)]
blk=lambda Z: next(i for i,(a,b) in enumerate(JAN) if a<=Z<=b)
print("  PER-BLOCK MONOTONE ASCENT, boundary handled correctly.")
print("  at a Janet opening a := L (the block's own floor); inside, a := max(a,L).\n")
a=None; cur=None; viol=[]; moves=[]
for Z,g,lo,hi in B:
    b=blk(Z)
    if b!=cur:
        a = lo if lo>-INF/2 and abs(lo)>1e-9 else (0.0 if lo>-INF/2 else (hi if hi<INF/2 else 0.0))
        cur=b; moves.append((Z,'open',a)); continue
    na = max(a,lo) if lo>-INF/2 else a
    if na > hi+1e-9:
        viol.append((Z,na,lo,hi))
        na = lo if lo>-INF/2 and abs(lo)>1e-9 else hi
        moves.append((Z,'forced',na))
    elif na!=a:
        moves.append((Z,'rise',na))
    a=na
f=lambda x:("-inf" if x<-INF/2 else "inf" if x>INF/2 else f"{x:.4f}")
print(f"  VIOLATIONS inside a block: {len(viol)}")
for Z,na,lo,hi in viol:
    print(f"      {G.GROUND[Z][0]:>3} {Z:<4} block {blk(Z)}  a={na:.4f} vs ({f(lo)}, {f(hi)})")
REC={3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104}
mz={Z for Z,_,_ in moves}
print(f"\n  moves {len(moves)}: {sum(1 for _,k,_ in moves if k=='open')} openings,"
      f" {sum(1 for _,k,_ in moves if k=='rise')} rises,"
      f" {sum(1 for _,k,_ in moves if k=='forced')} forced")
print(f"  vs the recorded eighteen: matching {len(mz&REC)}  extra {sorted(mz-REC)}"
      f"  missing {sorted(REC-mz)}")
print("\n  the full trajectory:")
RECA={19:0.5774,37:1.0000,55:1.2168,57:0.7071,80:0.8090,87:1.3938,91:1.3660,103:1.9841}
for Z,k,v in moves:
    r=RECA.get(Z)
    tag = f"   recorded {r:.4f} {'MATCH' if r and abs(v-r)<2e-3 else ('differs' if r else '')}"
    print(f"      {G.GROUND[Z][0]:>3} {Z:<4} blk{blk(Z)} {k:<7} a = {v:.4f}{tag}")