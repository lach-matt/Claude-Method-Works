import sys, math, random; sys.path.insert(0,"/home/claude/work")
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
    return lo,hi
B={Z:bracket(Z) for Z in range(3,109) if bracket(Z)}
CLIP=lambda x: max(-5.0,min(5.0,x))
def walk(place):
    """place(lo,hi,a) -> new a when the held a leaves [lo,hi]. count the moves."""
    a=None; moves=[]
    for Z in sorted(B):
        lo,hi=B[Z]
        if a is None or not (lo-1e-12 <= a <= hi+1e-12):
            a=place(lo,hi,a); moves.append(Z)
    return moves
RULES={
 "nearest endpoint (the record's rule)":
    lambda lo,hi,a: (CLIP(lo) if a is None else (lo if abs(a-lo)<=abs(a-hi) else hi)),
 "always the lower endpoint":  lambda lo,hi,a: CLIP(lo),
 "always the upper endpoint":  lambda lo,hi,a: CLIP(hi),
 "midpoint of the interval":   lambda lo,hi,a: (CLIP(lo)+CLIP(hi))/2,
 "farther endpoint":           lambda lo,hi,a: (CLIP(hi) if a is None else (hi if abs(a-lo)<=abs(a-hi) else lo)),
}
REC=[3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104]
print("  IS THE RESET SET A PROPERTY OF THE CORRIDOR, OR OF ONE TRAJECTORY?\n")
print(f"  {'placement rule':<38}{'resets':>8}{'matches record':>16}")
for nm,f in RULES.items():
    m=walk(f); s=set(m)&set(REC)
    print(f"  {nm:<38}{len(m):>8}{f'{len(s)} of {len(REC)}':>16}")
print()
rnd=[]
for seed in range(200):
    r=random.Random(seed)
    m=walk(lambda lo,hi,a,r=r: CLIP(lo)+r.random()*(CLIP(hi)-CLIP(lo)))
    rnd.append(len(m))
import statistics as st
print(f"  200 random interior placements: resets min {min(rnd)} max {max(rnd)}"
      f"  median {st.median(rnd)}")
print(f"\n  recorded: {len(REC)} resets")