import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def corr(Z):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]
    rad=lambda n,l:(n-l-1)+pr.get((n,l),0)/cap(l)
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
print("  WHY DOES d DRIFT NEGATIVE?  the upper bound is r/(√p_r − √p_g).")
print("  as the ENTERING shell fills, p_g rises, so √p_r − √p_g SHRINKS and the")
print("  bound GROWS — that is the p and f behaviour. For d it falls, so the")
print("  BINDING RIVAL must be changing as the shell fills.\n")
for target in ((4,2),(5,2),(3,2)):
    print(f"  {target[0]}{LS[target[1]]} filling:")
    print(f"      {'Z':>4}{'el':>4}{'occ before':>12}{'upper':>10}{'binding rival':>15}")
    for Z in range(3,109):
        c=corr(Z)
        if not c or c[0]!=target: continue
        pr={(n,l):o for n,l,o in G.expand(Z-1)}
        occ=pr.get(target,0)
        r=f"{c[3][0]}{LS[c[3][1]]}" if c[3] else "—"
        print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{occ:>12}{c[2]:>10.4f}{r:>15}")
    print()
print("  the s shells drift EXACTLY zero — why?")
for Z in (19,20,37,38):
    c=corr(Z)
    if not c: continue
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    print(f"      {G.GROUND[Z][0]:>3} {Z} enters {c[0][0]}{LS[c[0][1]]}"
          f" occ before {pr.get(c[0],0)}  upper {c[2]:.4f}"
          f"  rival {c[3][0]}{LS[c[3][1]] if c[3] else '—'}")