import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def corridor(Z, use_q):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]
    rad=lambda n,l: (n-l-1) + (pr.get((n,l),0)/cap(l) if use_q else 0)
    rg=rad(gn,gl); cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    lo,hi=-INF,INF
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(rad(n,l))-math.sqrt(rg); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return gn,gl,lo,hi
REC=set([3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104])
def run(use_q, per_subshell):
    """per_subshell: resets.py records that a NEVER resets mid-subshell — every
    subshell is filled at constant a. So hold a across a subshell and re-place
    only at a subshell OPENING."""
    a=None; moves=[]; cur=None
    for Z in range(3,109):
        c=corridor(Z,use_q)
        if not c: continue
        gn,gl,lo,hi=c
        opening = (gn,gl)!=cur
        cur=(gn,gl)
        need = a is None or not (lo-1e-9<=a<=hi+1e-9)
        if need and (opening or not per_subshell):
            a = lo if (lo>-INF/2 and abs(lo)>1e-9) else (hi if hi<INF/2 else lo)
            moves.append(Z)
        elif need:
            moves.append(Z)          # forced mid-subshell: record it, hold a
    return moves
print("  RESTATING THE PLACEMENT WITH q — resets.py says a is CONSTANT")
print("  across a subshell, so re-place only at a subshell OPENING.\n")
print(f"  {'variant':<40}{'resets':>8}{'match':>8}{'false +':>9}")
for uq in (False,True):
    for ps in (False,True):
        m=run(uq,ps); s=set(m)
        lab=f"q {'restored' if uq else 'dropped '} · {'per-subshell' if ps else 'every step '}"
        print(f"  {lab:<40}{len(m):>8}{len(s&REC):>8}{len(s-REC):>9}")
print("\n  the per-subshell variant with q, in full:")
m=run(True,True)
print(f"      {m}")
print(f"      recorded  {sorted(REC)}")
print(f"      false positives {sorted(set(m)-REC)}")
print(f"      missed          {sorted(REC-set(m))}")