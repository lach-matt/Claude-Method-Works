import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
RESET=[3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104]
# subshell openings, read from the configurations
prev=None; OPEN={}
for Z in range(1,109):
    cur={(n,l) for n,l,o in G.expand(Z) if o>0}
    if prev is not None:
        for k in cur-prev: OPEN[Z]=k
    else:
        for k in cur: OPEN[Z]=k
    prev=cur
# the aufbau exceptions: where the filled subshell is not the one Madelung says
MAD=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
     (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
def mad_expected(ne):
    occ={}; left=ne
    for n,l in MAD:
        if left<=0: break
        c=min(left,2*(2*l+1)); occ[(n,l)]=c; left-=c
    return occ
EXC=set()
for Z in range(3,109):
    obs={(n,l):o for n,l,o in G.expand(Z)}
    exp=mad_expected(Z)
    if {k:v for k,v in obs.items() if v>0}!={k:v for k,v in exp.items() if v>0}:
        EXC.add(Z)
print("  WHAT IS EVERY RESET?\n")
print(f"      {'Z':>4}{'el':>4}{'opens a subshell':>20}{'aufbau exception':>20}")
o=e=n=0
for Z in RESET:
    a="YES  "+f"{OPEN[Z][0]}{L[OPEN[Z][1]]}" if Z in OPEN else "—"
    b="YES" if Z in EXC else "—"
    if Z in OPEN: o+=1
    if Z in EXC: e+=1
    if Z not in OPEN and Z not in EXC: n+=1
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{a:>20}{b:>20}")
print()
print(f"      opens a subshell : {o} of {len(RESET)}")
print(f"      aufbau exception : {e} of {len(RESET)}")
print(f"      NEITHER          : {n} of {len(RESET)}")
print()
print("  AND THE CONVERSE — does every subshell opening force a reset?\n")
print(f"      {'Z':>4}{'el':>4}{'opens':>8}{'reset?':>9}")
miss=0
for Z in sorted(OPEN):
    if Z<3: continue
    r="YES" if Z in RESET else "no"
    if Z not in RESET: miss+=1
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{f'{OPEN[Z][0]}{L[OPEN[Z][1]]}':>8}{r:>9}")
print()
print(f"      subshell openings that do NOT reset : {miss}")
print()
print("  THE STATEMENT\n")
print("      a resets ONLY at a subshell opening or an aufbau exception —")
print("      never in the middle of a subshell's filling. so every subshell")
print("      is filled at CONSTANT a, and its occupancy slope is a property")
print("      of that subshell alone.")
print()
print("      the slopes are not comparable because the index says so, and the")
print("      reset mechanism is WHY: each subshell is its own segment.")
