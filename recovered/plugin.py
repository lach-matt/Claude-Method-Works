import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
def run(af):
    ok=bad=0; BAD=[]
    for Z in range(3,109):
        pr={(n,l):o for n,l,o in G.expand(Z-1)}
        cu={(n,l):o for n,l,o in G.expand(Z)}
        got=[k for k in cu if cu[k]>pr.get(k,0)]
        if len(got)!=1: continue
        got=got[0]; av=af(Z-1); cand=[]
        for l in range(5):
            for n in range(l+1,9):
                if pr.get((n,l),0)>=cap(l): continue
                cand.append((n,l,n-av*math.sqrt(n-l-1)))
                if pr.get((n,l),0)==0: break
        if len(cand)<2 or got not in [(a,b) for a,b,_ in cand]: continue
        pick=min(cand,key=lambda x:x[2])
        if (pick[0],pick[1])==got: ok+=1
        else: bad+=1; BAD.append((Z,got,(pick[0],pick[1])))
    return ok,bad,BAD
print("  PLUGGING IN a(Nₑ) FROM THE LADDER BRACKETS\n")
print("      the six group-2 lower bounds at c = 1:\n")
LB=[(20,0.5774),(38,1.0000),(56,1.2168),(70,1.2168),(88,1.3938),(102,1.3938)]
for ne,v in LB: print(f"          Nₑ = {ne:>3} : a > {v:.4f}")
print()
print("  a(Nₑ) = −1.0631 + 0.5576·ln Nₑ   (r² 0.9867 on those bounds)\n")
def a_log(ne):
    return max(-1.0631+0.5576*math.log(max(ne,2)),0.0)
ok,bad,BAD=run(a_log)
print(f"      {ok}/{ok+bad} = {100*ok/(ok+bad):.1f}%\n")
print("  AND WITH THE BOUND ITSELF — piecewise, using each ladder's value\n")
def a_step(ne):
    v=0.5774
    for n0,x in LB:
        if ne>=n0: v=x
    if ne<20: v=0.5774*ne/20
    return v
ok2,bad2,B2=run(a_step)
print(f"      {ok2}/{ok2+bad2} = {100*ok2/(ok2+bad2):.1f}%\n")
print("  AND A PURE POWER  a = k·Nₑ^m FITTED TO THE SIX BOUNDS\n")
import numpy as np
NE=np.array([x[0] for x in LB],float); AV=np.array([x[1] for x in LB])
b=np.polyfit(np.log(NE),np.log(AV),1)
print(f"      a = {math.exp(b[1]):.4f}·Nₑ^{b[0]:.4f}")
def a_pow(ne): return math.exp(b[1])*max(ne,2)**b[0]
ok3,bad3,B3=run(a_pow)
print(f"      {ok3}/{ok3+bad3} = {100*ok3/(ok3+bad3):.1f}%\n")
print("  COMPARISON\n")
print(f"      constant a = 0.60          86/106 = 81.1%")
print(f"      a = −1.063 + 0.558·lnNₑ    {ok}/{ok+bad} = {100*ok/(ok+bad):.1f}%")
print(f"      a = step through bounds    {ok2}/{ok2+bad2} = {100*ok2/(ok2+bad2):.1f}%")
print(f"      a = {math.exp(b[1]):.3f}·Nₑ^{b[0]:.3f}         {ok3}/{ok3+bad3} = {100*ok3/(ok3+bad3):.1f}%")
print()
best=max([(ok,'log',BAD),(ok2,'step',B2),(ok3,'power',B3)])
print(f"  FAILURES OF THE BEST ({best[1]})\n")
from collections import Counter
c=Counter(f"{g[0]}{L[g[1]]}→{p[0]}{L[p[1]]}" for _,g,p in best[2])
for k,v in c.most_common(8): print(f"      {k:<12}{v:>4}")
print(f"\n      at Z = {sorted(Z for Z,_,_ in best[2])[:20]}")