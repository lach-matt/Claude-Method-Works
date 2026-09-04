import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def rad(n,l,q):
    """the FULL radicand of the law: p + q/2(2l+1). brack.py uses q = 0."""
    return (n-l-1) + q/cap(l)
def bracket(Z, use_q):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]
    qg = (cu[(gn,gl)]-pr.get((gn,gl),0)) if use_q else 0
    # the entering subshell's own occupancy AFTER the step is what the law scores
    rg = rad(gn,gl, pr.get((gn,gl),0) if use_q else 0)
    cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    lo,hi=-INF,INF
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rr = rad(n,l, pr.get((n,l),0) if use_q else 0)
        d=math.sqrt(rr)-math.sqrt(rg); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return gn,gl,lo,hi
f=lambda x:("-inf" if x<-INF/2 else "inf" if x>INF/2 else f"{x:.4f}")
print("  THE CORRIDOR WITH q RESTORED — does it separate Mo, Rh and Pd?\n")
print(f"  {'Z':>4}{'el':>4}{'q=0 corridor (brack.py)':>28}{'with q':>28}")
for Z in (42,45,46):
    b0=bracket(Z,False); b1=bracket(Z,True)
    print(f"  {Z:>4}{G.GROUND[Z][0]:>4}"
          f"{'('+f(b0[2])+', '+f(b0[3])+')':>28}{'('+f(b1[2])+', '+f(b1[3])+')':>28}")
print("\n  and across the whole walk — is the system still consistent?")
ok=0; tot=0; empt=[]
for Z in range(3,109):
    b=bracket(Z,True)
    if not b: continue
    tot+=1
    if b[2] < b[3]-1e-12: ok+=1
    else: empt.append(Z)
print(f"      non-empty corridors with q restored: {ok} of {tot}")
if empt: print(f"      EMPTY at: {[(z,G.GROUND[z][0]) for z in empt]}")
print("\n  the resets that follow, with q restored:")
a=None; moves=[]
for Z in range(3,109):
    b=bracket(Z,True)
    if not b: continue
    lo,hi=b[2],b[3]
    if a is None or not (lo-1e-9<=a<=hi+1e-9):
        a = lo if (lo>-INF/2 and abs(lo)>1e-9) else (hi if hi<INF/2 else lo)
        moves.append(Z)
REC=[3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104]
print(f"      {len(moves)} resets: {moves}")
print(f"      recorded {len(REC)}: {REC}")
print(f"      matching {len(set(moves)&set(REC))}   false positives "
      f"{sorted(set(moves)-set(REC))}")