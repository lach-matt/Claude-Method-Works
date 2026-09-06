import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1)
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
    return gn,gl,lo,hi
B={Z:bracket(Z) for Z in range(3,109) if bracket(Z)}
REC=[3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104]
print("  THE ENDPOINT RULE — a is placed AT L or AT U, never between.")
print("  test: walk with a := L at every reset, and with the L/U choice made")
print("  by which endpoint the PREVIOUS a is nearer. count and compare.\n")
C=lambda x: max(-5.0,min(5.0,x))
def walk(pick):
    a=None; moves=[]; where=[]
    for Z in sorted(B):
        gn,gl,lo,hi=B[Z]
        if a is None or not (lo-1e-12<=a<=hi+1e-12):
            a=pick(C(lo),C(hi),a,gl); moves.append(Z)
            where.append('L' if abs(a-C(lo))<1e-9 else 'U')
    return moves, where
RULES={
 "always L":        lambda L,U,a,l: L,
 "always U":        lambda L,U,a,l: U,
 "nearest endpoint":lambda L,U,a,l: L if (a is None or abs(a-L)<=abs(a-U)) else U,
 "L for s, U else": lambda L,U,a,l: L if l==0 else U,
 "L unless L=-inf": lambda L,U,a,l: L if L>-4.99 else U,
}
print(f"  {'rule':<22}{'resets':>8}{'match rec':>11}{'  L/U pattern'}")
for nm,f in RULES.items():
    m,w=walk(f); s=set(m)&set(REC)
    print(f"  {nm:<22}{len(m):>8}{f'{len(s)}/{len(REC)}':>11}   "
          f"{''.join(w)[:26]}")
print("\n  and where do the RECORDED resets' brackets put L and U?")
print(f"  {'Z':>4}{'el':>4}{'opens':>7}{'L':>10}{'U':>10}{'one-sided?'}")
for Z in REC:
    if Z not in B: print(f"  {Z:>4}  (no bracket — step not single-gain)"); continue
    gn,gl,lo,hi=B[Z]
    f=lambda x:("-inf" if x<-1e8 else "inf" if x>1e8 else f"{x:.4f}")
    print(f"  {Z:>4}{G.GROUND[Z][0]:>4}{f'{gn}{LS[gl]}':>7}{f(lo):>10}{f(hi):>10}"
          f"   {'YES' if (lo<-1e8 or hi>1e8) else ''}")