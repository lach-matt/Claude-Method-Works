import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
JANET=[(1,2),(3,4),(5,12),(13,20),(21,38),(39,56),(57,88),(89,118)]
block=lambda Z: next(i for i,(a,b) in enumerate(JANET) if a<=Z<=b)
def nu(n,l,a): return n - a*math.sqrt(max(0.0,n-l-1))
def state(Z):
    """everything about step Z, derived from the configuration BEFORE it."""
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    tgt=got[0]; gn,gl=tgt; gp=gn-gl-1
    cand=[]
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
    return tgt,lo,hi,cand
print("  CORRECTED SEQUENCING — a entering step Z is CARRIED from Z-1.")
print("  the corridor at Z says which a would have chosen correctly; the law")
print("  is asked with the CARRIED value, and a moves only if that value is")
print("  outside [lo, hi].  the move is to the nearest admissible point.\n")
for policy in ("carry, clip into [lo,hi] when outside",
               "carry, per-block ascent (max with lo) when outside"):
    a=None; cur=None; right=0; tot=0; wrong=[]; moves=0
    for Z in range(3,109):
        s=state(Z)
        if not s: continue
        tgt,lo,hi,cand=s; b=block(Z)
        if a is None or b!=cur:
            a = lo if lo>-INF/2 and abs(lo)>1e-9 else (0.0 if lo>-INF/2 else min(hi,1.0))
            cur=b; moves+=1
        elif not (lo-1e-9 <= a <= hi+1e-9):
            if policy.startswith("carry, clip"):
                a = min(max(a, lo if lo>-INF/2 else a), hi if hi<INF/2 else a)
            else:
                a = max(a, lo) if lo>-INF/2 else min(a, hi)
                if a>hi+1e-9: a=hi
            moves+=1
        pick=min(cand,key=lambda k:(nu(k[0],k[1],a), k[0], k[1]))
        tot+=1
        if pick==tgt: right+=1
        else: wrong.append((Z,G.GROUND[Z][0],tgt,pick,a))
    print(f"  {policy}")
    print(f"      correct {right} of {tot}   moves {moves}")
    if wrong and len(wrong)<=12:
        for Z,s_,t,p,aa in wrong:
            print(f"         {Z:>4}{s_:>4} observed {t[0]}{LS[t[1]]}"
                  f"  predicted {p[0]}{LS[p[1]]}   a={aa:.4f}")
    elif wrong:
        print(f"         first misses: "
              + ", ".join(f"{s_}{Z}" for Z,s_,_,_,_ in wrong[:12]))
    print()