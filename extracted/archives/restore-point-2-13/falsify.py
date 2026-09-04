import sys, math, random; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
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
        d=math.sqrt(n-l-1)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return lo,hi
BR=[(Z,bracket(Z)) for Z in range(3,109)]
BR=[(Z,b) for Z,b in BR if b]
def walk(rule,a0=0.0,seed=0):
    rnd=random.Random(seed); a=a0; ok=0; mv=0
    for Z,(lo,hi) in BR:
        if lo<a<hi: ok+=1; continue
        na=rule(a,lo,hi,rnd)
        if na is None or not (lo<na<hi): continue
        a=na; ok+=1; mv+=1
    return ok,mv
E=1e-9
RULES=[
 ("keep unless excluded, nearest endpoint",
  lambda a,lo,hi,r: (lo+E) if a<=lo else (hi-E)),
 ("always the LOWER endpoint",
  lambda a,lo,hi,r: (lo+E) if lo>-1e8 else (hi-E)),
 ("always the UPPER endpoint",
  lambda a,lo,hi,r: (hi-E) if hi<1e8 else (lo+E)),
 ("the FARTHER endpoint",
  lambda a,lo,hi,r: (hi-E) if a<=lo else (lo+E)),
 ("the midpoint (finite side)",
  lambda a,lo,hi,r: ((lo+hi)/2 if lo>-1e8 and hi<1e8 else
                     (lo+1 if lo>-1e8 else hi-1))),
 ("reset to 0 then nearest",
  lambda a,lo,hi,r: (lo+E) if 0<=lo else ((hi-E) if 0>=hi else 0.0)),
 ("a random interior point",
  lambda a,lo,hi,r: r.uniform(max(lo,-5)+E,min(hi,5)-E)),
 ("nearest endpoint, but overshoot by 10%",
  lambda a,lo,hi,r: (lo+0.1*max(hi-lo,0.01)) if a<=lo else (hi-0.1*max(hi-lo,0.01))),
]
print(f"  FALSIFYING THE SELECTION RULE  —  {len(BR)} steps\n")
print(f"      {'rule':<44}{'satisfied':>11}{'moves':>8}")
for nm,f in RULES:
    ok,mv=walk(f)
    print(f"      {nm:<44}{ok:>7}/{len(BR)}{mv:>8}")
print()
print("  RANDOM INTERIOR POINT — 200 seeds\n")
res=[walk(RULES[6][1],seed=s)[0] for s in range(200)]
print(f"      satisfied: min {min(res)} · median {sorted(res)[100]} · max {max(res)}")
print(f"      reached {len(BR)}/{len(BR)} on {sum(1 for x in res if x==len(BR))} of 200 seeds")
print()
print("  READING\n")
print("      every rule that lands INSIDE the new interval satisfies every step,")
print("      because the walk's only requirement is that a lie in the interval.")
print("      the interval is what constrains; the rule choosing where inside it")
print("      is unconstrained by the ORDERING data.")
print()
print("      → the selection rule is NOT falsifiable from the filling order.")
print("        it cannot be promoted. what IS forced is the interval.")
