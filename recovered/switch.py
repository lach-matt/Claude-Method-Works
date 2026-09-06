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
    return (gn,gl),lo,hi,bhi,pr
REC={3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104}
print("  THE BINDING RIVAL SWITCHES WHEN THE s SHELL DROPS TO ONE.")
print("  Pauli (R 1397): a FULL subshell is not admissible and cannot be a rival.\n")
print(f"  {'Z':>4}{'el':>4}{'enters':>7}{'ns occ before':>15}{'binding rival':>15}"
      f"{'upper':>10}{'  reset?'}")
for row,(ns) in ((( 3,2),(4,0)),((4,2),(5,0)),((5,2),(6,0))):
    for Z in range(3,109):
        c=corr(Z)
        if not c or c[0]!=row: continue
        pr=c[4]; occ=pr.get(ns,0)
        r=f"{c[3][0]}{LS[c[3][1]]}" if c[3] else "—"
        print(f"  {Z:>4}{G.GROUND[Z][0]:>4}{f'{row[0]}{LS[row[1]]}':>7}"
              f"{f'{occ}/2':>15}{r:>15}{c[2]:>10.4f}"
              f"   {'RESET' if Z in REC else ''}")
    print()
print("  THE CLAIM: within a d row, the rival is the np while ns is FULL,")
print("  and the ns once it has dropped to one. Count it.\n")
hit=tot=0
for row,ns,npx in (((3,2),(4,0),(4,1)),((4,2),(5,0),(5,1)),((5,2),(6,0),(6,1))):
    for Z in range(3,109):
        c=corr(Z)
        if not c or c[0]!=row or not c[3]: continue
        pr=c[4]; occ=pr.get(ns,0); tot+=1
        pred = ns if occ<2 else npx
        # the 7s cases at Os/Ir/Pt are neither; count them separately
        hit += (c[3]==pred)
print(f"      rival == (ns if ns<2 else np): {hit} of {tot}")