import sys, math; sys.path.insert(0,"/home/claude/work")
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
print("  THE EIGHTH RULE, EXAMINED  —  'nearest endpoint, overshoot 10%'\n")
E=1e-9
def rule8(a,lo,hi):
    w=hi-lo
    if w>1e8:  # one-sided
        return (lo+1.0) if a<=lo else (hi-1.0)
    return (lo+0.1*w) if a<=lo else (hi-0.1*w)
a=0.0; ok=0; fail=[]; moves=[]
for Z,(lo,hi) in BR:
    if lo<a<hi: ok+=1; continue
    na=rule8(a,lo,hi)
    if not (lo<na<hi):
        fail.append((Z,a,lo,hi,na)); continue
    moves.append((Z,a,na,lo,hi)); a=na; ok+=1
print(f"      satisfied {ok}/{len(BR)} · moves {len(moves)} · failed {len(fail)}\n")
if fail:
    print("      FAILURES:")
    for Z,a0,lo,hi,na in fail[:10]:
        print(f"          Z={Z:>3} a={a0:.4f} interval ({lo:.4f},{hi:.4f}) → {na:.4f}")
print()
print("  ITS TRAJECTORY vs THE MINIMAL RULE\n")
def walk_min():
    a=0.0; T=[]
    for Z,(lo,hi) in BR:
        if lo<a<hi: continue
        a=(lo+E) if a<=lo else (hi-E); T.append((Z,a))
    return T
Tm=walk_min()
print(f"      minimal rule : {len(Tm)} moves")
print(f"      rule 8       : {len(moves)} moves\n")
print(f"      {'Z':>4}{'minimal a':>12}{'rule-8 a':>12}{'same?':>8}")
dm={Z:a for Z,a in Tm}; d8={Z:na for Z,_,na,_,_ in moves}
for Z in sorted(set(dm)|set(d8)):
    m=dm.get(Z); e=d8.get(Z)
    s = "yes" if (m is not None and e is not None and abs(m-e)<1e-6) else "—"
    print(f"      {Z:>4}{(f'{m:.6f}' if m is not None else '—'):>12}"
          f"{(f'{e:.6f}' if e is not None else '—'):>12}{s:>8}")
print()
print("  READING\n")
print("      rule 8 reproduces the table but its trajectory is different and")
print("      its reset values are NOT the crossing surds. so it confirms the")
print("      falsification: the ordering does not select the trajectory.")