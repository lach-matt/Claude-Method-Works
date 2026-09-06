import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
JANET=[(1,2),(3,4),(5,12),(13,20),(21,38),(39,56),(57,88),(89,118)]
block=lambda Z: next(i for i,(a,b) in enumerate(JANET) if a<=Z<=b)
def nu_full(n,l,q,a):
    """the law of record: nu = n - a*sqrt(n-l-1 + q/2(2l+1)), q the CURRENT
    occupancy of that subshell before the electron enters."""
    return n - a*math.sqrt(max(0.0,(n-l-1) + q/cap(l)))
def state(Z):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    tgt=got[0]; gn,gl=tgt; gp=gn-gl-1; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if tgt not in cand or len(cand)<2: return None
    lo,hi=-INF,INF
    for n,l in cand:
        if (n,l)==tgt: continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return tgt,lo,hi,cand,pr
print("  THE FULL LAW — q RESTORED IN THE SCORER, corridor unchanged.\n")
for lab,scorer in (("q = 0 (what I had been using)", lambda k,pr,a: (k[0]-a*math.sqrt(max(0.0,k[0]-k[1]-1)), k[0], k[1])),
                   ("q = current occupancy (the law of record)",
                    lambda k,pr,a: (nu_full(k[0],k[1],pr.get(k,0),a), k[0], k[1]))):
    a=None; cur=None; right=0; tot=0; wrong=[]
    for Z in range(3,109):
        s=state(Z)
        if not s: continue
        tgt,lo,hi,cand,pr=s; b=block(Z)
        if a is None or b!=cur:
            a = lo if lo>-INF/2 and abs(lo)>1e-9 else (0.0 if lo>-INF/2 else min(hi,1.0))
            cur=b
        elif not (lo-1e-9 <= a <= hi+1e-9):
            a = max(a, lo) if lo>-INF/2 else min(a,hi)
            if a>hi+1e-9: a=hi
        pick=min(cand,key=lambda k: scorer(k,pr,a))
        tot+=1
        if pick==tgt: right+=1
        else: wrong.append((Z,G.GROUND[Z][0],tgt,pick,a))
    print(f"  {lab}")
    print(f"      correct {right} of {tot}")
    if wrong:
        print("      misses: " + ", ".join(
            f"{s_}{Z}({t[0]}{LS[t[1]]}->{p[0]}{LS[p[1]]})" for Z,s_,t,p,_ in wrong[:14]))
        if len(wrong)>14: print(f"              ... +{len(wrong)-14}")
    print()