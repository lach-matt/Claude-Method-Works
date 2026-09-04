import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np, statistics as st
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
IV=[]
for Z in range(3,109):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: continue
    gp=gn-gl-1; lo,hi=-1e9,1e9
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(n-l-1)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    IV.append((Z,gn,gl,lo,hi))
PER=[(3,10,2),(11,18,3),(19,36,4),(37,54,5),(55,86,6),(87,108,7)]
print("  CAN a BE CONSTANT WITHIN A PERIOD?\n")
print(f"      {'period':>7}{'Z range':>10}{'n':>4}{'a >':>9}{'a <':>9}{'  verdict'}")
OK=[]
for lo_,hi_,per in PER:
    v=[x for x in IV if lo_<=x[0]<=hi_]
    if not v: continue
    LO=max(x[3] for x in v); HI=min(x[4] for x in v)
    f="feasible" if LO<HI else "EMPTY"
    print(f"      {per:>7}{f'{lo_}–{hi_}':>10}{len(v):>4}"
          f"{(LO if LO>-1e8 else float('-inf')):>9.3f}"
          f"{(HI if HI<1e8 else float('inf')):>9.3f}   {f}")
    OK.append((per,LO,HI,v))
print()
print("  WHERE A PERIOD FAILS, SPLIT IT BY BLOCK\n")
BL={0:"s",1:"p",2:"d",3:"f"}
for per,LO,HI,v in OK:
    if LO<HI: continue
    print(f"      period {per}:")
    for b in range(4):
        w=[x for x in v if x[2]==b]
        if not w: continue
        L2=max(x[3] for x in w); H2=min(x[4] for x in w)
        print(f"          {BL[b]}-block : {len(w):>3} atoms   a ∈ "
              f"({L2 if L2>-1e8 else float('-inf'):.3f}, "
              f"{H2 if H2<1e8 else float('inf'):.3f})   "
              f"{'feasible' if L2<H2 else 'EMPTY'}")
    print()
print("  AND BY BLOCK ACROSS THE WHOLE TABLE\n")
print(f"      {'block':>7}{'n':>5}{'a >':>9}{'a <':>9}{'  verdict'}")
for b in range(4):
    w=[x for x in IV if x[2]==b]
    if not w: continue
    L2=max(x[3] for x in w); H2=min(x[4] for x in w)
    print(f"      {BL[b]:>7}{len(w):>5}"
          f"{(L2 if L2>-1e8 else float('-inf')):>9.3f}"
          f"{(H2 if H2<1e8 else float('inf')):>9.3f}"
          f"   {'feasible' if L2<H2 else 'EMPTY'}")
