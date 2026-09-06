import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
JANET=[(1,2),(3,4),(5,12),(13,20),(21,38),(39,56),(57,88),(89,118)]
block=lambda Z: next(i for i,(a,b) in enumerate(JANET) if a<=Z<=b)
def nu(n,l,a): return n - a*math.sqrt(max(0.0,n-l-1))
def observed_entry(Z):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    return (got[0] if len(got)==1 else None), pr
def corridor(Z):
    tgt,pr=observed_entry(Z)
    if tgt is None: return None
    gn,gl=tgt; gp=gn-gl-1; cand=[]
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
print("  END TO END — does the DERIVED a reproduce the ORDERING?\n")
print("  a from per-block ascent (no choice). at each Z, take the")
print("  Pauli-admissible subshell of least nu and compare to the observed one.\n")
a=None; cur=None; right=0; tot=0; wrong=[]
for Z in range(3,109):
    c=corridor(Z)
    if not c: continue
    tgt,lo,hi,cand,pr=c
    b=block(Z)
    if b!=cur:
        a = lo if lo>-INF/2 and abs(lo)>1e-9 else (0.0 if lo>-INF/2 else hi)
        cur=b
    else:
        a = max(a,lo) if lo>-INF/2 else a
    pick=min(cand,key=lambda k:(nu(k[0],k[1],a), k[0], k[1]))
    tot+=1
    if pick==tgt: right+=1
    else: wrong.append((Z,G.GROUND[Z][0],tgt,pick,a))
print(f"      steps predicted correctly: {right} of {tot}")
if wrong:
    print(f"\n      {'Z':>4}{'el':>4}{'observed':>10}{'predicted':>11}{'a':>9}")
    for Z,s,t,p,aa in wrong:
        print(f"      {Z:>4}{s:>4}{f'{t[0]}{LS[t[1]]}':>10}{f'{p[0]}{LS[p[1]]}':>11}{aa:>9.4f}")
print(f"\n  NULL (contingency R 1383): plain Madelung order scores 28 of 108.")