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
print("  CAN a ASCEND MONOTONICALLY THROUGH ALL 106 CORRIDORS?\n")
print("  rule: a := max(a, L)  — never decrease, rise only when forced.")
print("  feasible iff that a is always <= U.\n")
a=-INF; fail=[]; moves=[]
for Z,g,lo,hi in B:
    newa = max(a, lo if lo>-INF/2 else a)
    if newa==-INF: newa = lo if lo>-INF/2 else 0.0
    if newa > hi+1e-9:
        fail.append((Z,newa,lo,hi))
    else:
        if newa!=a: moves.append(Z)
        a=newa
print(f"  steps where the ascending a EXCEEDS the ceiling: {len(fail)}")
for Z,na,lo,hi in fail[:14]:
    f=lambda x:("-inf" if x<-INF/2 else "inf" if x>INF/2 else f"{x:.4f}")
    print(f"      {G.GROUND[Z][0]:>3} {Z:<4} a would be {na:.4f}, corridor "
          f"({f(lo)}, {f(hi)})")
print(f"\n  -> monotone ascent is {'FEASIBLE' if not fail else 'IMPOSSIBLE'}")
if fail:
    print(f"\n  the first failure is at Z = {fail[0][0]} ({G.GROUND[fail[0][0]][0]}).")
    print("  what is the highest a can reach and still clear every later ceiling?")
    ceil=min(hi for Z,g,lo,hi in B if hi<INF/2)
    print(f"      the tightest ceiling anywhere: {ceil:.4f}")
    print(f"      the highest floor anywhere   : {max(lo for Z,g,lo,hi in B if lo>-INF/2):.4f}")
    print("      floor exceeds ceiling, so NO single a serves the whole walk —")
    print("      which is why a must be a STATE and not a constant (R 1341's")
    print("      'necessity of state').")