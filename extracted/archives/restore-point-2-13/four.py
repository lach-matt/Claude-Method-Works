import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
RESET=[3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104]
prev=None; OPEN={}
for Z in range(1,109):
    cur={(n,l) for n,l,o in G.expand(Z) if o>0}
    if prev is not None:
        for k in cur-prev: OPEN[Z]=k
    prev=cur
MAD=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
     (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
def mad(ne):
    occ={}; left=ne
    for n,l in MAD:
        if left<=0: break
        c=min(left,2*(2*l+1)); occ[(n,l)]=c; left-=c
    return {k:v for k,v in occ.items() if v>0}
EXC={Z for Z in range(3,109)
     if {(n,l):o for n,l,o in G.expand(Z) if o>0}!=mad(Z)}
UN=[Z for Z in RESET if Z not in OPEN and Z not in EXC]
print("  THE FOUR UNACCOUNTED RESETS\n")
print(f"      Z = {UN}\n")
for Z in UN:
    print(f"      Z = {Z}  {G.GROUND[Z][0]}")
    print(f"          {Z-1}: {G.GROUND[Z-1][0]:<3} {G.GROUND[Z-1][1]}")
    print(f"          {Z}: {G.GROUND[Z][0]:<3} {G.GROUND[Z][1]}")
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    gain=[(k,cu[k]-pr.get(k,0)) for k in cu if cu[k]>pr.get(k,0)]
    lose=[(k,pr[k]-cu.get(k,0)) for k in pr if pr[k]>cu.get(k,0)]
    print(f"          gains : {[(f'{n}{L[l]}',d) for (n,l),d in gain]}")
    print(f"          loses : {[(f'{n}{L[l]}',d) for (n,l),d in lose]}")
    print(f"          in OPEN? {Z in OPEN}   in EXC? {Z in EXC}")
    print(f"          Madelung says: {sorted(mad(Z).items())[-3:]}")
    print(f"          observed     : "
          f"{sorted([(k,v) for k,v in cu.items() if v>0])[-3:]}")
    print()
print("  ALL EIGHTEEN, CLASSIFIED\n")
print(f"      {'Z':>4}{'el':>4}{'class':>26}")
for Z in RESET:
    if Z in OPEN and Z in EXC: c=f"opening {OPEN[Z][0]}{L[OPEN[Z][1]]} + exception"
    elif Z in OPEN: c=f"opening {OPEN[Z][0]}{L[OPEN[Z][1]]}"
    elif Z in EXC: c="aufbau exception"
    else: c="*** UNACCOUNTED ***"
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{c:>26}")
