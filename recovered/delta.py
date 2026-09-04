import sys, math, csv; sys.path.insert(0,"/home/claude/work")
import ground as G
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def bracket(Z):
    if Z<3 or Z>108: return None
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]; gp=gn-gl-1; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    lo,hi=-INF,INF
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return (gn,gl),gp,lo,hi
# the handshake trajectory: hold a, move to the nearest endpoint when forced
A={}
a=None
for Z in range(3,109):
    b=bracket(Z)
    if not b: continue
    (gn,gl),gp,lo,hi=b
    if a is None or not (lo-1e-9<=a<=hi+1e-9):
        cands=[x for x in (lo,hi) if -INF/2<x<INF/2]
        a = (min(cands,key=lambda x:abs(x-a)) if (a is not None and cands)
             else (lo if lo>-INF/2 else hi))
    A[Z]=(a,gn,gl,gp)
# measured defects for the neutrals
M={}
for r in csv.DictReader(open("COORDINATES.tsv"),delimiter="\t"):
    if r["grade"]!="measured": continue
    if r["charge"]!="1": continue
    M.setdefault((int(r["Z"]),int(r["l"])),[]).append(float(r["delta"]))
print("  a = δ/√p  ->  δ = a·√p.  the walk's a, the entered subshell's p,")
print("  against the MEASURED defect for that (Z, ℓ) at charge 1.\n")
print(f"  {'Z':>4}{'el':>4}{'enters':>8}{'p':>4}{'a':>9}{'δ pred':>9}"
      f"{'δ measured':>12}{'ratio':>8}")
rows=[]
for Z in sorted(A):
    a,gn,gl,gp=A[Z]
    if gp==0: continue                       # sqrt(0) -> delta 0, no information
    key=(Z,gl)
    if key not in M: continue
    dm=sum(M[key])/len(M[key])
    dp=a*math.sqrt(gp)
    rows.append((Z,gn,gl,gp,a,dp,dm))
for Z,gn,gl,gp,a,dp,dm in rows[:22]:
    r = dp/dm if abs(dm)>1e-6 else float('nan')
    print(f"  {Z:>4}{G.GROUND[Z][0]:>4}{f'{gn}{LS[gl]}':>8}{gp:>4}{a:>9.4f}"
          f"{dp:>9.4f}{dm:>12.4f}{r:>8.3f}")
import statistics as st
rr=[dp/dm for _,_,_,_,_,dp,dm in rows if abs(dm)>1e-6]
print(f"\n  {len(rows)} elements comparable.  ratio predicted/measured:")
print(f"      median {st.median(rr):.4f}   mean {sum(rr)/len(rr):.4f}"
      f"   sd {st.pstdev(rr):.4f}")