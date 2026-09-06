import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def corr(Z,use_q=True):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]
    rad=lambda n,l:(n-l-1)+(pr.get((n,l),0)/cap(l) if use_q else 0)
    rg=rad(gn,gl); cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    lo,hi=-INF,INF; bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(rad(n,l))-math.sqrt(rg); r=n-gn
        if abs(d)<1e-12: continue
        if d>0 and r/d<hi: hi,bhi=r/d,(n,l)
        if d<0 and r/d>lo: lo=r/d
    return (gn,gl),lo,hi,bhi
REC={3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104}
print("  THE CONTRACTION — how far does the ceiling fall when s takes over?\n")
print(f"  {'Z':>4}{'el':>4}{'prev ceiling':>14}{'own ceiling':>13}{'drop':>9}"
      f"{'held a still inside?':>22}{'  reset?'}")
prev=None; a=None
for Z in range(3,109):
    c=corr(Z)
    if not c: continue
    if Z in (41,42,44,45,46,78,79):
        pc = prev[2] if prev else float('nan')
        drop = pc-c[2] if prev else float('nan')
        print(f"  {Z:>4}{G.GROUND[Z][0]:>4}{pc:>14.4f}{c[2]:>13.4f}{drop:>9.4f}"
              f"{'':>22}   {'RESET' if Z in REC else ''}")
    prev=c
print("\n  THE HELD VALUE — walk with the endpoint rule on the q=0 corridor,")
print("  then ask at Mo, Rh, Pd whether a lies inside the q-RESTORED corridor.\n")
a=None
for Z in range(3,109):
    c0=corr(Z,False)
    if not c0: continue
    lo,hi=c0[1],c0[2]
    if a is None or not (lo-1e-9<=a<=hi+1e-9):
        a = lo if (lo>-INF/2 and abs(lo)>1e-9) else (hi if hi<INF/2 else lo)
    if Z in (42,45,46):
        cq=corr(Z,True)
        inside = cq[1]-1e-9 <= a <= cq[2]+1e-9
        print(f"      {G.GROUND[Z][0]:>3} {Z}: a = {a:.4f}   q-corridor "
              f"({cq[1]:+.4f}, {cq[2]:.4f})   a is {'INSIDE' if inside else 'OUTSIDE'}"
              f"   {'RESET' if Z in REC else 'no reset'}")
print("\n  and the ceilings of the three, ordered:")
for Z in (42,45,46):
    c=corr(Z)
    print(f"      {G.GROUND[Z][0]:>3} {Z}  ceiling {c[2]:.4f}   "
          f"{'RESET' if Z in REC else 'NO RESET'}")