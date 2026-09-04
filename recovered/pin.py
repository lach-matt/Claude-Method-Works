import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
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
    gp=gn-gl-1; lo,hi=-INF,INF
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp)
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,(n-gn)/d)
        else:   lo=max(lo,(n-gn)/d)
    return gn,gl,lo,hi
B={Z:bracket(Z) for Z in range(3,109) if bracket(Z)}
REC=set([3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104])
RECA={19:0.5774,37:1.0000,55:1.2168,57:0.7071,80:0.8090,87:1.3938,91:1.3660,103:1.9841}
# NO CLAMPING. an infinite endpoint is not a place; a degenerate L at 0 is the
# absence of a real lower surd. The rule: take the tightest FINITE, NON-ZERO
# bound — L if it exists, else U.
def pick(lo,hi):
    if lo>-INF/2 and abs(lo)>1e-9: return lo,'L'
    if hi< INF/2: return hi,'U'
    if lo>-INF/2: return lo,'L'
    return 0.0,'0'
a=None; moves=[]; where={}
for Z in sorted(B):
    gn,gl,lo,hi=B[Z]
    if a is None or not (lo-1e-9<=a<=hi+1e-9):
        a,w=pick(lo,hi); moves.append(Z); where[Z]=(a,w)
print("  THE RULE, UNCLAMPED: a := the tightest FINITE NON-ZERO bound")
print("                        L if it exists as a real surd, else U\n")
print(f"      resets {len(moves)}   recorded {len(REC)}   "
      f"matching {len(set(moves)&REC)}")
print(f"      false positives (forced but not recorded): {sorted(set(moves)-REC)}")
print(f"      recorded but not produced:                 {sorted(REC-set(moves))}")
print(f"\n  {'Z':>4}{'el':>4}{'a placed':>11}{'end':>5}{'recorded a':>12}   agree")
ok=0; tot=0
for Z in sorted(moves):
    v,w=where[Z]
    r=RECA.get(Z)
    ag=""
    if r is not None:
        tot+=1; ag = "YES" if abs(v-r)<2e-3 else "no"
        ok += ag=="YES"
    print(f"  {Z:>4}{G.GROUND[Z][0]:>4}{v:>11.4f}{w:>5}"
          f"{(f'{r:.4f}' if r is not None else '—'):>12}   {ag}")
print(f"\n      of the {tot} recorded a-values reproduced: {ok}")