import sys, math; sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
def bracket(Z):
    """the interval a must lie in for atom Z's own step to be right"""
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    gp=gn-gl-1; lo,hi=-1e9,1e9
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(n-l-1)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return (lo,hi,gn,gl)
print("  THE HANDSHAKE  —  a resets only when the previous atom's value fails\n")
print("      walk Z upward. keep a if it still lies in the new bracket.")
print("      if not, move it the MINIMUM distance to re-enter.\n")
a=0.0; moves=0; ok=0; tot=0; TR=[]
for Z in range(3,109):
    b=bracket(Z)
    if b is None: continue
    lo,hi,gn,gl=b; tot+=1
    if lo<a<hi: ok+=1; TR.append((Z,a,0)); continue
    old=a
    if a<=lo: a=lo+1e-6
    else:     a=hi-1e-6
    moves+=1; ok+=1
    TR.append((Z,a,a-old))
print(f"      {tot} steps · {ok} satisfied · {moves} recalibrations\n")
print(f"      → a single a walking with minimal resets satisfies "
      f"{100*ok/tot:.1f}% of the table.\n")
print("  WHERE IT RECALIBRATES\n")
print(f"      {'Z':>4}{'el':>4}{'fills':>7}{'a before':>11}{'a after':>10}{'move':>10}")
prev=0.0
for Z,av,mv in TR:
    if abs(mv)<1e-9: continue
    b=bracket(Z)
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{f'{b[2]}{L[b[3]]}':>7}"
          f"{av-mv:>11.4f}{av:>10.4f}{mv:>+10.4f}")
print()
print(f"      {moves} resets in {tot} steps.\n")
print("  THE TRAJECTORY OF a\n")
print(f"      {'Z':>5}{'a':>10}")
for Z,av,mv in TR:
    if Z in (3,5,10,19,20,21,37,38,39,55,56,57,70,71,87,88,89,102,103):
        print(f"      {Z:>5}{av:>10.4f}")
