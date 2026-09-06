import sys, math, statistics as st; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def corr(Z,use_q=True):
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
    lo,hi=-INF,INF; bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(rad(n,l))-math.sqrt(rg); r=n-gn
        if abs(d)<1e-12: continue
        if d>0 and r/d<hi: hi,bhi=r/d,(n,l)
        if d<0 and r/d>lo: lo=r/d
    return (gn,gl),lo,hi,bhi,pr
REC={3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104}
print("  THE TRIGGER — not proximity to the ceiling, but the CHANGE in it.")
print("  R 1406: the ceiling contracts when an occupied rival takes over.")
print("  Test the CONTRACTION itself as the trigger, not the margin.\n")
a=None; rows=[]; prev=None
for Z in range(3,109):
    c0=corr(Z,False); cq=corr(Z,True)
    if not c0 or not cq: continue
    lo,hi=c0[1],c0[2]
    if a is None or not (lo-1e-9<=a<=hi+1e-9):
        a = lo if (lo>-INF/2 and abs(lo)>1e-9) else (hi if hi<INF/2 else lo)
    if prev is not None and cq[2]<INF/2 and prev<INF/2:
        rows.append((Z, prev-cq[2], cq[2]-a, Z in REC))
    prev=cq[2] if cq[2]<INF/2 else prev
d_res=[d for _,d,_,r in rows if r]; d_non=[d for _,d,_,r in rows if not r]
print(f"  CONTRACTION (previous ceiling − this one), {len(rows)} steps")
print(f"      resets     n={len(d_res):>3}  median {st.median(d_res):+.4f}")
print(f"      non-resets n={len(d_non):>3}  median {st.median(d_non):+.4f}")
best=None
for t in [x/200 for x in range(-100,300)]:
    tp=sum(1 for _,d,_,r in rows if r and d> t); fp=sum(1 for _,d,_,r in rows if not r and d> t)
    fn=sum(1 for _,d,_,r in rows if r and d<=t); tn=sum(1 for _,d,_,r in rows if not r and d<=t)
    acc=(tp+tn)/len(rows)
    if best is None or acc>best[0]: best=(acc,t,tp,fp,fn,tn)
acc,t,tp,fp,fn,tn=best
base=max(len(d_res),len(d_non))/len(rows)
print(f"      best cut contraction > {t:+.3f}: accuracy {100*acc:.0f}%"
      f"  (baseline {100*base:.0f}%)   TP {tp} FP {fp} FN {fn} TN {tn}")
print(f"\n  the ten LARGEST contractions:")
for Z,d,m,r in sorted(rows,key=lambda x:-x[1])[:10]:
    print(f"      {G.GROUND[Z][0]:>3} {Z:<4} contraction {d:+.4f}  margin {m:+.4f}"
          f"   {'RESET' if r else ''}")