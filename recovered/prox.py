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
    lo,hi=-INF,INF
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(rad(n,l))-math.sqrt(rg); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return (gn,gl),lo,hi
REC={3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104}
# walk on the q=0 corridor with the endpoint rule; record the MARGIN to the
# q-restored ceiling at every step.
a=None; rows=[]
for Z in range(3,109):
    c0=corr(Z,False); cq=corr(Z,True)
    if not c0 or not cq: continue
    lo,hi=c0[1],c0[2]
    if a is None or not (lo-1e-9<=a<=hi+1e-9):
        a = lo if (lo>-INF/2 and abs(lo)>1e-9) else (hi if hi<INF/2 else lo)
    if cq[2]<INF/2:
        rows.append((Z, cq[2]-a, Z in REC))
res=[m for _,m,r in rows if r]; non=[m for _,m,r in rows if not r]
print(f"  MARGIN (q-ceiling − held a) at {len(rows)} two-sided steps\n")
print(f"      resets     n={len(res):>3}  median {st.median(res):+.4f}"
      f"  min {min(res):+.4f}  max {max(res):+.4f}")
print(f"      non-resets n={len(non):>3}  median {st.median(non):+.4f}"
      f"  min {min(non):+.4f}  max {max(non):+.4f}")
print("\n  DOES A THRESHOLD SEPARATE THEM?  scan every cut, score by accuracy.")
best=None
for t in [x/200 for x in range(-100,400)]:
    tp=sum(1 for _,m,r in rows if r and m< t); fn=sum(1 for _,m,r in rows if r and m>=t)
    fp=sum(1 for _,m,r in rows if not r and m< t); tn=sum(1 for _,m,r in rows if not r and m>=t)
    acc=(tp+tn)/len(rows)
    if best is None or acc>best[0]: best=(acc,t,tp,fp,fn,tn)
acc,t,tp,fp,fn,tn=best
print(f"      best cut margin < {t:+.3f}: accuracy {100*acc:.0f}%"
      f"   TP {tp}  FP {fp}  FN {fn}  TN {tn}")
base=max(len(res),len(non))/len(rows)
print(f"      always-guess-majority baseline: {100*base:.0f}%")
print(f"\n  the ten SMALLEST margins, and whether each is a reset:")
for Z,m,r in sorted(rows,key=lambda x:x[1])[:10]:
    print(f"      {G.GROUND[Z][0]:>3} {Z:<4} margin {m:+.4f}   {'RESET' if r else ''}")