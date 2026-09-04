import sys; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def group(Z):
    """the periodic-table group, from the observed configuration"""
    cfg=G.expand(Z)
    v=[(n,l,o) for n,l,o in cfg]
    nmax=max(n for n,l,o in v)
    val=[(n,l,o) for n,l,o in v if n==nmax or (l>=2 and o<2*(2*l+1))]
    # count valence electrons above the last noble gas
    NOB=[0,2,10,18,36,54,86]
    core=max([b for b in NOB if b<Z])
    return Z-core
NOB=[0,2,10,18,36,54,86]
print("  THE 24 ELEMENTS WITH A CLOSED f SHELL INSIDE THE VALENCE\n")
print(f"      {'Z':>4}{'el':>4}{'period':>8}{'block':>7}{'group':>7}   ground shells")
R=[]
for Z in range(1,109):
    cfg=G.expand(Z)
    if not any(l==3 and o==14 for n,l,o in cfg): continue
    per=1+sum(1 for b in NOB[1:] if Z>b)
    n_,l_,o_=cfg[-1]
    blk=L[l_]
    core=max([b for b in NOB if b<Z])
    # standard group: for d-block, 2 + d-count; for p-block, 12 + p-count
    dcount=sum(o for n,l,o in cfg if l==2 and n==per-1)
    pcount=sum(o for n,l,o in cfg if l==1 and n==per)
    scount=sum(o for n,l,o in cfg if l==0 and n==per)
    if blk=="s": grp=scount
    elif blk=="d": grp=2+dcount
    elif blk=="p": grp=12+pcount
    else: grp=0
    R.append((Z,G.GROUND[Z][0],per,blk,grp))
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{per:>8}{blk:>7}{grp:>7}   {G.GROUND[Z][1]}")
print(f"\n      {len(R)} elements\n")
from collections import Counter
print("  BY PERIOD  : " + " · ".join(f"period {k}: {v}"
      for k,v in sorted(Counter(r[2] for r in R).items())))
print("  BY BLOCK   : " + " · ".join(f"{k}: {v}"
      for k,v in sorted(Counter(r[3] for r in R).items())))
print("  BY GROUP   : " + " · ".join(f"{k}: {v}"
      for k,v in sorted(Counter(r[4] for r in R).items())))
print()
print("  AND THE THREE LADDER NEUTRALS AMONG THEM\n")
for ne in (70,88,102):
    if ne in [r[0] for r in R]:
        r=[x for x in R if x[0]==ne][0]
        print(f"      Nₑ = {ne:>3} : {r[1]} — period {r[2]}, {r[3]}-block, group {r[4]}")
    else:
        cfg=G.expand(ne)
        nf=sum(o for n,l,o in cfg if l==3)
        per=1+sum(1 for b in NOB[1:] if ne>b)
        print(f"      Nₑ = {ne:>3} : {G.GROUND[ne][0]} — period {per}, "
              f"f electrons = {nf}  (NOT in the f14 list)")
