import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
cap=lambda l:2*(2*l+1)
def bracket(Z):
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
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp)
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,(n-gn)/d)
        else:   lo=max(lo,(n-gn)/d)
    return (gn,gl,lo,hi)
B={}
for Z in range(3,109):
    b=bracket(Z)
    if b: B[Z]=b
REC=set([3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104])
C=lambda x: max(-5.0,min(5.0,x))
def walk(tfun):
    a=None; moves=[]
    for Z in sorted(B):
        gn,gl,lo,hi=B[Z]; L,U=C(lo),C(hi)
        if a is None or not (lo-1e-12<=a<=hi+1e-12):
            t=tfun(gl); a=L+t*(U-L); moves.append(Z)
    return set(moves)
print("  DOES AN ℓ-RANKED PLACEMENT REPRODUCE THE RESET SET?\n")
ENTRY=lambda l: math.sqrt(l*(l+1)/2)
print("  Λ_t's entry point t(ℓ) = √(ℓ(ℓ+1)/2):",
      ", ".join(f"ℓ={l}:{ENTRY(l):.4f}" for l in range(4)))
print("  (t > 1 puts a ABOVE the upper endpoint, so the raw entry point cannot")
print("   be a position WITHIN a two-sided corridor. clamped for the scan.)\n")
best=[]
import itertools
grid=[i/20 for i in range(21)]
for ts in itertools.product(grid,repeat=3):        # t for l=0,1,2 ; l=3 = t[2]
    tf=lambda l,ts=ts: ts[min(l,2)]
    m=walk(tf)
    score=len(m&REC)-abs(len(m)-len(REC))*0.5
    best.append((score,len(m),len(m&REC),ts))
best.sort(reverse=True)
print(f"  {'t(s)':>6}{'t(p)':>6}{'t(d+)':>7}{'resets':>8}{'match':>7}")
for sc,n,mt,ts in best[:8]:
    print(f"  {ts[0]:>6.2f}{ts[1]:>6.2f}{ts[2]:>7.2f}{n:>8}{mt:>7}")
print(f"\n  recorded: 18 resets. best match found: {best[0][2]} of 18"
      f" at {best[0][1]} resets")