import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np
from collections import Counter
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
print("  THE LÖWDIN EQUATION REBUILT\n")
print("      Pauli  : an electron may enter any subshell with occ < 2(2ℓ+1)")
print("      nodes  : p = n − ℓ − 1  for ANY subshell, open or not")
print("      so     : n* = n − a·√(n−ℓ−1)   and the lowest n* receives\n")
def run(af,lmax=4,nmax=8):
    ok=bad=0; BAD=[]
    for Z in range(3,109):
        pr={(n,l):o for n,l,o in G.expand(Z-1)}
        cu={(n,l):o for n,l,o in G.expand(Z)}
        got=[k for k in cu if cu[k]>pr.get(k,0)]
        if len(got)!=1: continue
        got=got[0]
        a=af(Z-1); cand=[]
        for l in range(lmax+1):
            for n in range(l+1,nmax+1):
                if pr.get((n,l),0)>=cap(l): continue
                p=n-l-1
                cand.append((n,l,n-a*math.sqrt(p)))
                break_after=False
                if pr.get((n,l),0)==0: break   # only the first unopened at this l
        if len(cand)<2: continue
        pick=min(cand,key=lambda x:x[2])
        if (pick[0],pick[1])==got: ok+=1
        else: bad+=1; BAD.append((Z,got,(pick[0],pick[1])))
    return ok,bad,BAD
print(f"      {'a':>6}{'correct':>9}{'of':>5}{'  rate':>8}")
best=None
for av in np.arange(0.0,2.01,0.05):
    ok,bad,BAD=run(lambda ne,A=float(av): A)
    if best is None or ok>best[0]: best=(ok,bad,BAD,float(av))
    if round(av*10)==av*10 and round(av*5)==av*5:
        print(f"      {av:>6.2f}{ok:>9}{ok+bad:>5}{100*ok/max(ok+bad,1):>7.1f}%")
ok,bad,BAD,av=best
print(f"\n      best constant a = {av:.2f} : {ok}/{ok+bad} = {100*ok/(ok+bad):.1f}%\n")
b0,b1,b2=-2.2402,1.3250,-0.1602
def am(ne):
    if ne<2: return 0.0
    u=math.log(ne); return math.exp(b0+b1*u+b2*u*u)
ok2,bad2,BAD2=run(am)
print(f"      with the measured a(u) : {ok2}/{ok2+bad2} = {100*ok2/(ok2+bad2):.1f}%\n")
print("  WHERE THE BEST VERSION FAILS\n")
use=BAD if ok>=ok2 else BAD2
c=Counter(f"{g[0]}{L[g[1]]}→{p[0]}{L[p[1]]}" for _,g,p in use)
for k,v in c.most_common(8): print(f"          {k:<12}{v:>4}")
print()
EXC={24,29,41,42,44,45,46,47,57,58,64,78,79,89,90,91,92,93,96,103}
ine=sum(1 for Z,_,_ in use if Z in EXC)
print(f"      at a known aufbau exception : {ine} of {len(use)}")
print(f"      elsewhere                   : {len(use)-ine}")
zz=sorted(Z for Z,_,_ in use if Z not in EXC)
print(f"      Z : {zz[:24]}")
