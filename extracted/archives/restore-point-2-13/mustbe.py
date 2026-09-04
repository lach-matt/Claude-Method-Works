import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
def brack(Z):
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
    gp=gn-gl-1; lo,hi=-1e9,1e9; bh=bl=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(n-l-1)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0:
            if r/d<hi: hi,bh=r/d,(n,l)
        else:
            if r/d>lo: lo,bl=r/d,(n,l)
    return lo,hi,gn,gl,bl,bh
print("  IS U AT AN OPENING THE CROSSING WITH THE PREVIOUS SUBSHELL?\n")
print("      a subshell opens when it becomes favourable. at that instant it")
print("      has just overtaken whatever was filling before. 'just overtaken'")
print("      means AT the crossing. so a = U must hold at every opening —")
print("      provided U's rival IS the previously-filling subshell.\n")
prev=None; OPEN={}
for Z in range(1,109):
    cur={(n,l) for n,l,o in G.expand(Z) if o>0}
    if prev is not None:
        for k in cur-prev: OPEN[Z]=k
    prev=cur
print(f"      {'Z':>4}{'el':>4}{'opens':>7}{'previously filling':>20}"
      f"{'U set by':>10}{'  same?'}")
same=diff=0
for Z in sorted(OPEN):
    if Z<4: continue
    b=brack(Z)
    if b is None: continue
    lo,hi,gn,gl,bl,bh=b
    # what was filling at Z-1?
    p2={(n,l):o for n,l,o in G.expand(Z-2)} if Z>=5 else {}
    p1={(n,l):o for n,l,o in G.expand(Z-1)}
    pg=[k for k in p1 if p1[k]>p2.get(k,0)]
    pv=pg[0] if len(pg)==1 else None
    s = (pv is not None and bh is not None and pv==bh)
    same+=s; diff+= (not s)
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{f'{gn}{L[gl]}':>7}"
          f"{(f'{pv[0]}{L[pv[1]]}' if pv else '—'):>20}"
          f"{(f'{bh[0]}{L[bh[1]]}' if bh else '—'):>10}"
          f"{'  YES' if s else '  no'}")
print(f"\n      U's rival IS the previously-filling subshell : {same}")
print(f"      it is not                                    : {diff}")
