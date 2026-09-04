import math
import numpy as np
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
config,core_p,thresh,ORDER,ROWS=g["config"],g["core_p"],g["thresh"],g["ORDER"],g["ROWS"]
a,b,h,w,k=np.load("/tmp/eqgs2.npy")
L="spdfg"
def outer(ne):
    cfg=config(ne); return cfg[-1] if cfg else (0,0,0)
def delta(Z,c,l):
    ne=Z-c+1; p=core_p(ne-1,l); t=math.log(c+1)/c
    n_,l_,o_=outer(ne-1)
    if p>=1: return (a+b*l_)*math.sqrt(p)*ne**k*t
    D=Z-thresh(ne-1,l); x=max(-60.,min(60.,D/w))
    return h*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
# observed neutral and ion ground configurations, transition metals — NIST
# (Z, charge) -> the subshell the OUTERMOST electron occupies, i.e. what ionises next
OBS = {
 (21,1):(4,0),(21,2):(4,0),(21,3):(3,2),
 (22,1):(4,0),(22,2):(4,0),(22,3):(3,2),(22,4):(3,2),
 (23,1):(4,0),(23,2):(3,2),(23,3):(3,2),
 (24,1):(4,0),(24,2):(3,2),(24,3):(3,2),
 (25,1):(4,0),(25,2):(3,2),(25,3):(3,2),
 (26,1):(4,0),(26,2):(3,2),(26,3):(3,2),(26,4):(3,2),
 (27,1):(4,0),(27,2):(3,2),(27,3):(3,2),
 (28,1):(4,0),(28,2):(3,2),(28,3):(3,2),
 (29,1):(4,0),(29,2):(3,2),(29,3):(3,2),
 (30,1):(4,0),(30,2):(3,2),(30,3):(3,2),
 (39,1):(5,0),(39,2):(5,0),(39,3):(4,2),
 (40,1):(5,0),(40,2):(5,0),(40,3):(4,2),(40,4):(4,2),
 (57,1):(6,0),(57,2):(6,0),(57,3):(5,2),
 (20,1):(4,0),(20,2):(4,0),(19,1):(4,0),
 (12,1):(3,0),(12,2):(3,0),(13,1):(3,1),(13,2):(3,0),
 (14,1):(3,1),(14,2):(3,1),(15,1):(3,1),(16,1):(3,1),(17,1):(3,1),(18,1):(3,1),
}
print("  THE IONISATION ORDER — a test the equation has never been shown\n")
print("      For each species, which subshell holds the electron that leaves next?")
print("      The equation says: the one with the LARGEST n* among occupied ones.\n")
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for A,B,O in cfg:
        if A==n and B==l: return O
    return 0
ok=bad=0; BAD=[]
for (Z,c),got in sorted(OBS.items()):
    ne=Z-c+1
    cfg=config(ne)                       # this species' own ground configuration
    cand=[(n,l,o) for n,l,o in cfg if o>0]
    if len(cand)<2: continue
    scored=[]
    for n,l,o in cand:
        # n* of the OCCUPIED orbital, as the equation would give it for this ion
        d=delta(Z,c,l)
        scored.append((n,l,n-d))
    pick=max(scored,key=lambda x:x[2])   # largest n* = least bound = leaves first
    if (pick[0],pick[1])==got: ok+=1
    else: bad+=1; BAD.append((Z,c,got,pick,scored))
print(f"      species tested : {ok+bad}")
print(f"      correct        : {ok}  ({100*ok/max(ok+bad,1):.1f}%)")
print(f"      wrong          : {bad}")
print()
if BAD:
    print(f"      {'Z':>4}{'chg':>5}{'observed':>10}{'equation':>10}{'n* obs':>9}{'n* eq':>8}")
    for Z,c,got,pick,sc in BAD[:18]:
        no=[x for x in sc if (x[0],x[1])==got]
        print(f"      {Z:>4}{c:>5}{f'{got[0]}{L[got[1]]}':>10}"
              f"{f'{pick[0]}{L[pick[1]]}':>10}"
              f"{(no[0][2] if no else float('nan')):>9.3f}{pick[2]:>8.3f}")
print()
print("  SPLIT AT Z = 21\n")
lo=[(Z,c) for (Z,c) in OBS if Z<21]; hi=[(Z,c) for (Z,c) in OBS if Z>=21]
for lab,sel in (("Z < 21",lo),("Z ≥ 21",hi)):
    n=sum(1 for x in sel)
    wrong=sum(1 for Z,c,_,_,_ in BAD if (Z,c) in sel)
    print(f"      {lab:<10}{n-wrong:>4}/{n:<4} correct   ({100*(n-wrong)/max(n,1):.0f}%)")
