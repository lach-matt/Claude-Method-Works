import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
IV=[]
for Z in range(3,109):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: continue
    gp=gn-gl-1; lo,hi=-math.inf,math.inf; blo=bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0:
            if r/d<hi: hi,bhi=r/d,(n,l,rp,r)
        else:
            if r/d>lo: lo,blo=r/d,(n,l,rp,r)
    IV.append((Z,gn,gl,gp,lo,hi,blo,bhi))
print("corridors:",len(IV))
# ROUTE 1 — greedy by right endpoint: maximum pairwise-disjoint set
S=sorted(IV,key=lambda t:t[5])
sel=[];last=-math.inf
for t in S:
    if t[4]>=last: sel.append(t); last=t[5]
print("ROUTE1 max pairwise-disjoint =",len(sel),
      [(t[0],G.GROUND[t[0]][0],round(t[4],4),round(t[5],4)) for t in sel])
# ROUTE 2 — brute-force max clique on the conflict graph
import itertools
n=len(IV); adj=[[False]*n for _ in range(n)]; E=0
for i in range(n):
    for j in range(i+1,n):
        a,b=IV[i],IV[j]
        if a[5]<=b[4] or b[5]<=a[4]:
            adj[i][j]=adj[j][i]=True; E+=1
best=[]
def ext(R,P):
    global best
    if not P:
        if len(R)>len(best): best=R[:]
        return
    if len(R)+len(P)<=len(best): return
    for k,v in enumerate(P):
        ext(R+[v],[u for u in P[k+1:] if adj[v][u]])
ext([],list(range(n)))
print("edges:",E,"density:",round(2*E/(n*(n-1)),3))
print("ROUTE2 max clique =",len(best),
      [(IV[i][0],G.GROUND[IV[i][0]][0]) for i in best])
iso=sum(1 for i in range(n) if not any(adj[i]))
print("isolated vertices:",iso)
# Gallai: minimum stabbing points
S=sorted(IV,key=lambda t:t[5]); pts=[];last=-math.inf
for t in S:
    if t[4]>=last: last=t[5]; pts.append(last)
print("min stabbing points:",len(pts),[round(p,4) for p in pts])

print("\n--- THE THREE, WITH THEIR GENERATING RIVALS ---")
tri={5,57,103}
for Z,gn,gl,gp,lo,hi,blo,bhi in IV:
    if Z not in tri: continue
    def f(b):
        if b is None: return "—"
        n,l,rp,r=b; return f"{r}/(√{rp}−√{gp}) [rival {n}{L[l]}]"
    print(f"  Z={Z:>3} {G.GROUND[Z][0]:<3} enters {gn}{L[gl]} p={gp} "
          f"lo={lo:+.4f} {f(blo)}  hi={hi:+.4f} {f(bhi)}")
print("\n--- IS THE FAMILY DRIFTING? ---")
fin=[(Z,lo,hi) for Z,gn,gl,gp,lo,hi,blo,bhi in IV if lo>-math.inf and hi<math.inf]
print("  corridors with two finite ends:",len(fin))
import statistics as st
for a,b in ((3,20),(21,40),(41,60),(61,80),(81,108)):
    seg=[(lo+hi)/2 for Z,lo,hi in fin if a<=Z<=b]
    w=[hi-lo for Z,lo,hi in fin if a<=Z<=b]
    if seg: print(f"  Z {a:>3}-{b:<3} n={len(seg):>3} midpoint median={st.median(seg):.4f}  width median={st.median(w):.4f}")
print("\n--- WIDTH VS ENTRANT p ---")
byp={}
for Z,gn,gl,gp,lo,hi,blo,bhi in IV:
    if lo>-math.inf and hi<math.inf: byp.setdefault(gp,[]).append(hi-lo)
for p in sorted(byp): print(f"  p_entrant={p}  n={len(byp[p]):>3}  median width={st.median(byp[p]):.4f}")

print("\n--- THE CANONICAL FORM: is each bound Δn=±1 against a rival at Δp=±2? ---")
def g(p): return 1/(math.sqrt(p+2)-math.sqrt(p))
canon=[]
for Z,gn,gl,gp,lo,hi,blo,bhi in IV:
    okl = blo is None or (blo[2]==gp-2 and blo[3]==-1)
    okh = bhi is None or (bhi[2]==gp+2 and bhi[3]==1)
    if okl and okh: canon.append((Z,gp,lo,hi))
print(f"  canonical corridors: {len(canon)} of {len(IV)}")
from collections import Counter
print("  by entrant p:",dict(sorted(Counter(p for Z,p,lo,hi in canon).items())))
print("  distinct canonical intervals:",
      sorted({(round(lo,4),round(hi,4)) for Z,p,lo,hi in canon}))
print("\n  predicted band edges g(p) = 1/(√(p+2)−√p):")
print("   ",[f"g({p})={g(p):.4f}" for p in range(0,7)])
print("\n--- DO THE CANONICAL BANDS TILE? ---")
ps=sorted({p for Z,p,lo,hi in canon})
print("  p present:",ps)
for p in ps:
    lo,hi=[(lo,hi) for Z,q,lo,hi in canon if q==p][0]
    print(f"    p={p}: ({lo:+.4f}, {hi:+.4f})   predicted (g({p-2})={g(p-2) if p>=2 else float('-inf'):+.4f}, g({p})={g(p):+.4f})")
print("\n--- WHY NOT MORE: non-canonical corridors at each p ---")
nc=Counter()
for Z,gn,gl,gp,lo,hi,blo,bhi in IV:
    if (Z,gp,lo,hi) not in [(a,b,c,d) for a,b,c,d in canon]: nc[gp]+=1
print("  non-canonical by p:",dict(sorted(nc.items())))

print("\n--- THE FOUR CANONICAL CLASSES AND THEIR MEMBERS ---")
cls={}
for Z,p,lo,hi in canon: cls.setdefault((round(lo,4),round(hi,4),p),[]).append(Z)
for k in sorted(cls,key=lambda t:t[1]):
    m=cls[k]; syms=[G.GROUND[z][0] for z in m]
    print(f"  p={k[2]} ({k[0]:+.4f},{k[1]:+.4f})  n={len(m):>2}  "
          f"{' '.join(syms[:9])}{' ...' if len(syms)>9 else ''}")
print("\n--- IS THE CLIQUE'S CERTIFICATE UNIQUE? ---")
import itertools
reps=[cls[k] for k in sorted(cls,key=lambda t:t[1])]
iv={ (round(lo,4),round(hi,4),p):(lo,hi) for Z,p,lo,hi in canon }
keys=sorted(cls,key=lambda t:t[1])
ok=[]
for combo in itertools.combinations(range(len(keys)),3):
    I=[iv[keys[c]] for c in combo]
    if all(I[i][1]<=I[j][0] or I[j][1]<=I[i][0] for i,j in itertools.combinations(range(3),2)):
        ok.append([keys[c][2] for c in combo])
print("  disjoint triples of canonical CLASSES (by entrant p):",ok)
tot=1
for c in ok[0] if ok else []: pass
if ok:
    sizes=[len(cls[k]) for k in keys if k[2] in ok[0]]
    print("  class sizes for that triple:",sizes,"→ distinct certificates:",
          sizes[0]*sizes[1]*sizes[2])

print("\n--- ALL MAXIMUM CLIQUES IN THE FULL 106-VERTEX GRAPH ---")
allc=[]
for c in itertools.combinations(range(n),3):
    if all(adj[i][j] for i,j in itertools.combinations(c,2)): allc.append(c)
print("  maximum cliques (size 3):",len(allc))
from collections import Counter
pos=[Counter(),Counter(),Counter()]
for c in allc:
    t=sorted(c,key=lambda i:IV[i][5])
    for s,i in enumerate(t): pos[s][G.GROUND[IV[i][0]][0]]+=1
for s in range(3):
    print(f"   slot {s+1}: {len(pos[s])} distinct elements  {dict(list(sorted(pos[s].items(),key=lambda kv:-kv[1]))[:8])}")
verts=sorted({i for c in allc for i in c},key=lambda i:IV[i][0])
print("  vertices appearing in ANY maximum clique:",len(verts))
print("  ",[f"{G.GROUND[IV[i][0]][0]}{IV[i][0]}" for i in verts])
