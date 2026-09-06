import math
from itertools import product, combinations
print("="*88)
print("  THE REFORMULATION FROM THE d = 2 THEOREM")
print("="*88)
print("""
  **Lemmas 1–2:** a closed set has every row an interval [lo(i), hi(i)] with
  lo and hi both non-decreasing. **So counting closed sets = counting PAIRS
  OF MONOTONE SEQUENCES** — and that is a non-intersecting lattice-path
  count, which has a determinant formula (Lindström–Gessel–Viennot).

     N(r,c) = #{(lo,hi) : monotone, length r, values in [0,c-1] ∪ {empty},
                          lo_i ≤ hi_i where non-empty}
     a(r,c) = the same, requiring every row non-empty and every column used
""")
def monoseq(r,vals):
    """non-decreasing sequences of length r over vals"""
    out=[]
    def rec(i,last,acc):
        if i==r: out.append(tuple(acc)); return
        for v in vals:
            if v>=last: acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-10**9,[])
    return out
def count_pairs(r,c,require_all_rows,require_all_cols):
    E=-1   # empty marker, sorts below everything
    vals=list(range(c))
    tot=0
    LO=monoseq(r,vals+[E] if not require_all_rows else vals)
    HI=monoseq(r,vals+[E] if not require_all_rows else vals)
    for lo in LO:
        for hi in HI:
            ok=True; cover=set(); nonempty=0
            for i in range(r):
                if lo[i]==E or hi[i]==E:
                    if lo[i]!=E or hi[i]!=E: ok=False; break
                    continue
                if lo[i]>hi[i]: ok=False; break
                nonempty+=1
                cover|=set(range(lo[i],hi[i]+1))
            if not ok: continue
            if nonempty==0: continue
            if require_all_rows and nonempty<r: continue
            if require_all_cols and len(cover)<c: continue
            tot+=1
    return tot
KN_N={(1,1):1,(1,2):3,(1,3):7,(2,2):12,(2,3):37,(3,3):146,(2,4):103,(3,4):505,(4,4):2102}
KN_a={(1,1):1,(1,2):1,(2,2):4,(2,3):8,(3,3):29,(2,4):13,(3,4):73,(4,4):266,(2,5):19,(3,5):151}
print("="*88)
print("  DOES THE PATH COUNT REPRODUCE N AND a?")
print("="*88)
print("\n  %10s%14s%14s%10s%14s%14s%10s"%("(r,c)","paths -> N","known N","match","paths -> a","known a","match"))
print("  "+"-"*86)
okN=badN=oka=bada=0
for (r,c) in sorted(set(list(KN_N)+list(KN_a))):
    if r*c>16: continue
    pn=count_pairs(r,c,False,False)
    pa=count_pairs(r,c,True,True)
    sN=KN_N.get((r,c)); sa=KN_a.get((r,c))
    m1=("YES" if pn==sN else "no") if sN else "—"
    m2=("YES" if pa==sa else "no") if sa else "—"
    if sN: okN+= (pn==sN); badN+= (pn!=sN)
    if sa: oka+= (pa==sa); bada+= (pa!=sa)
    print("  %10s%14d%14s%10s%14d%14s%10s"%("(%d,%d)"%(r,c),pn,str(sN or "—"),m1,pa,str(sa or "—"),m2))
print("\n     N : %d correct, %d wrong        a : %d correct, %d wrong"%(okN,badN,oka,bada))
print("="*88)
print("  IF IT MATCHES — THE DETERMINANT")
print("="*88)
print("""
  **A pair of non-crossing monotone sequences is a pair of non-intersecting
  lattice paths.** By Lindström–Gessel–Viennot the count is a 2×2 determinant
  of binomials:

      #pairs = C(r+c-1, r)² − C(r+c-1, r-1)·C(r+c-1, r+1)

  **which is a Catalan-like (ballot) number.** Test it against the counts
  above.
""")
print("  %10s%18s%18s%10s"%("(r,c)","LGV determinant","paths -> N","match"))
print("  "+"-"*58)
for (r,c) in sorted(KN_N):
    if r*c>16: continue
    n1=math.comb(r+c-1,r); n2=math.comb(r+c-1,r-1); n3=math.comb(r+c-1,r+1)
    det=n1*n1-n2*n3
    pn=count_pairs(r,c,False,False)
    print("  %10s%18d%18d%10s"%("(%d,%d)"%(r,c),det,pn,"YES" if det==pn else "no"))