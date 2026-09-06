import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def corr(Z,use_q):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]
    rad=lambda n,l:(n-l-1)+(pr.get((n,l),0)/cap(l) if use_q else 0)
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
    return (gn,gl),lo,hi
runs={}
for Z in range(3,109):
    c=corr(Z,True)
    if not c: continue
    runs.setdefault(c[0],[]).append((Z,c[1],c[2]))
print("  WHAT q BUYS — the corridor MOVES as a subshell fills. q=0 gives one")
print("  interval per subshell; q gives a sequence. measure the DRIFT.\n")
print(f"  {'subshell':>9}{'n fills':>9}{'upper: first -> last':>26}{'drift':>9}{'per e-':>9}")
rows=[]
for (n,l),v in sorted(runs.items()):
    if len(v)<3: continue
    his=[h for _,_,h in v if h<INF/2]
    if len(his)<3: continue
    d=his[-1]-his[0]; per=d/(len(his)-1)
    rows.append(((n,l),len(v),his[0],his[-1],d,per))
    print(f"  {f'{n}{LS[l]}':>9}{len(v):>9}{f'{his[0]:.4f} -> {his[-1]:.4f}':>26}"
          f"{d:>9.4f}{per:>9.4f}")
print(f"\n  chem_index records an OCCUPANCY SLOPE of 0.021 to 0.243, one per")
print(f"  subshell, property = subshell radius, class = one subshell.")
per=[r[5] for r in rows]
print(f"  the q-corridor's drift per electron: min {min(per):.4f}  max {max(per):.4f}")
print(f"  chem_index's range                 : 0.0210        0.2430")
print(f"\n  do they order the same way? subshells ranked by drift per electron:")
for (nl,cnt,a,b,d,p) in sorted(rows,key=lambda r:r[5]):
    print(f"      {nl[0]}{LS[nl[1]]}  {p:.4f}")