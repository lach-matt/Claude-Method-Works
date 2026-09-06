import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
def zstar(Z, cfg, n, l):
    """Slater's rules for an electron in (n,l) added to configuration cfg"""
    s=0.0
    for nn,ll,o in cfg:
        if l<=1:                       # s or p
            if nn==n and ll<=1: s+=0.35*o
            elif nn==n-1:       s+=0.85*o
            elif nn<n-1:        s+=1.00*o
            elif nn==n and ll>1: s+=1.00*o
        else:                          # d or f
            if nn==n and ll==l: s+=0.35*o
            else:               s+=1.00*o
    if n==1: s=0.30*sum(o for nn,ll,o in cfg if nn==1)
    return Z-s
print("  STEP 4 · SLATER SCREENING AS ν = n / Z*   —  NO free parameter\n")
ok=bad=0; BAD=[]
for Z in range(3,109):
    pr=G.expand(Z-1); prd={(n,l):o for n,l,o in pr}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>prd.get(k,0)]
    if len(got)!=1: continue
    got=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if prd.get((n,l),0)>=cap(l): continue
            zs=zstar(Z,pr,n,l)
            if zs<=0.05: continue
            cand.append((n,l,n/zs))
            if prd.get((n,l),0)==0: break
    if len(cand)<2 or got not in [(a,b) for a,b,_ in cand]: continue
    pick=min(cand,key=lambda x:x[2])
    if (pick[0],pick[1])==got: ok+=1
    else: bad+=1; BAD.append((Z,got,(pick[0],pick[1])))
print(f"      elements tested : {ok+bad}")
print(f"      correct         : {ok}  ({100*ok/max(ok+bad,1):.1f}%)")
print(f"      wrong           : {bad}\n")
from collections import Counter
c=Counter(f"{g[0]}{L[g[1]]}→{p[0]}{L[p[1]]}" for _,g,p in BAD)
print("      failures by pair:")
for k,v in c.most_common(8): print(f"          {k:<12}{v:>4}")
print()
print("  AND THE IMPLIED a — solving n − a√p = n/Z*  for the OBSERVED subshell\n")
print(f"      {'period':>7}{'block':>7}{'n':>4}{'a implied':>12}{'bracket':>22}{'  in?'}")
BR={(2,0):(-0.0,3.146),(2,1):(-9e9,0.707),(3,0):(-0.0,3.146),(3,1):(-0.0,1.366),
    (4,0):(0.577,3.732),(4,1):(-0.0,1.707),(4,2):(-9e9,0.707),
    (5,0):(1.000,4.236),(5,1):(0.577,1.984),(5,2):(-0.0,1.000),
    (6,0):(1.217,4.686),(6,1):(1.000,2.225),(6,2):(0.707,1.217),(6,3):(-9e9,0.707),
    (7,0):(1.394,5.095),(7,1):(1.984,2.441),(7,2):(1.366,1.984),(7,3):(-0.0,1.366)}
import statistics as st
from collections import defaultdict
A=defaultdict(list)
for Z in range(3,109):
    pr=G.expand(Z-1); prd={(n,l):o for n,l,o in pr}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>prd.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; p=gn-gl-1
    if p<=0: continue
    zs=zstar(Z,pr,gn,gl)
    if zs<=0.05: continue
    per=1+sum(1 for b in (2,10,18,36,54,86) if Z>b)
    A[(per,gl)].append((gn-gn/zs)/math.sqrt(p))
hit=tot=0
for k in sorted(A):
    v=st.median(A[k]); lo,hi=BR.get(k,(-9e9,9e9))
    ins = lo<v<hi; tot+=1; hit+=ins
    print(f"      {k[0]:>7}{L[k[1]]:>7}{len(A[k]):>4}{v:>12.4f}"
          f"{f'({lo if lo>-1e8 else float(chr(45)+chr(105)+chr(110)+chr(102)):.3f}, {hi:.3f})':>22}"
          f"   {'YES' if ins else 'no'}")
print(f"\n      {hit} of {tot} cells inside their bracket")