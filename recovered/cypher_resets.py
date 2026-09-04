import sys, math, re; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def anat(Z):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]
    lost=[k for k in pr if pr[k]>cu.get(k,0)]
    q=cu[(gn,gl)]-pr.get((gn,gl),0)
    gp=gn-gl-1; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    lo,hi=-INF,INF; blo=bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0 and r/d<hi: hi,bhi=r/d,(n,l)
        if d<0 and r/d>lo: lo,blo=r/d,(n,l)
    return dict(g=(gn,gl),q=q,lost=lost,lo=lo,hi=hi,blo=blo,bhi=bhi,
                cand=cand,occ=pr.get((gn,gl),0),
                mult=int(re.match(r"(\d+)",G.GROUND[Z][2]).group(1))
                     if re.match(r"(\d+)",G.GROUND[Z][2]) else None)
REC=[3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104]
f=lambda x:("-inf" if x<-INF/2 else "inf" if x>INF/2 else f"{x:.4f}")
print("  THE EIGHTEEN RESETS THROUGH THE CYPHER\n")
print("  ORDER    the corridor            ALGEBRA  the binding pair (which rivals)")
print("  GEOMETRY width                   ANALYSIS q, the transfer count")
print("  INFO     candidate count         STATS    the ground term's 2S+1\n")
print(f"  {'Z':>4}{'el':>3}{'opens':>6}{'ORDER: corridor':>22}{'GEOM':>7}"
      f"{'ALGEBRA: lo/hi rivals':>24}{'ANA q':>6}{'INFO':>5}{'STAT':>5}")
rows={}
for Z in REC:
    d=anat(Z)
    if not d: print(f"  {Z:>4}{G.GROUND[Z][0]:>3}  no single-gain bracket"); continue
    rows[Z]=d
    lo_r=f"{d['blo'][0]}{LS[d['blo'][1]]}" if d['blo'] else "—"
    hi_r=f"{d['bhi'][0]}{LS[d['bhi'][1]]}" if d['bhi'] else "—"
    w = d['hi']-d['lo'] if (d['lo']>-INF/2 and d['hi']<INF/2) else float('inf')
    print(f"  {Z:>4}{G.GROUND[Z][0]:>3}{f'{d[chr(103)][0]}{LS[d[chr(103)][1]]}':>6}"
          f"{'('+f(d['lo'])+', '+f(d['hi'])+')':>22}{w:>7.3f}"
          f"{lo_r+' / '+hi_r:>24}{d['q']:>6}{len(d['cand']):>5}{d['mult']:>5}")
print("\n  THE ALGEBRA — which rival pair binds each reset, tallied:")
from collections import Counter
pairs=Counter()
for Z,d in rows.items():
    lo_r=f"{d['blo'][0]}{LS[d['blo'][1]]}" if d['blo'] else "—"
    hi_r=f"{d['bhi'][0]}{LS[d['bhi'][1]]}" if d['bhi'] else "—"
    pairs[(lo_r,hi_r)]+=1
for (a,b),n in pairs.most_common():
    zs=[Z for Z,d in rows.items()
        if (f"{d['blo'][0]}{LS[d['blo'][1]]}" if d['blo'] else "—")==a
        and (f"{d['bhi'][0]}{LS[d['bhi'][1]]}" if d['bhi'] else "—")==b]
    print(f"      {a:>4} / {b:<4}  {n:>2}   {[G.GROUND[z][0] for z in zs]}")