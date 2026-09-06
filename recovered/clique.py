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