import math
import numpy as np
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
ROWS=g["ROWS"]; thresh0=g["thresh"]; ORDER=g["ORDER"]; OPEN=g["OPEN"]
a,b,h,w,k=np.load("/tmp/eqgs2.npy")
L="spdfg"
# --- the two orderings
MAD=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
     (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
HYD=sorted(MAD,key=lambda t:(t[0],t[1]))          # n first, then l — hydrogenic
def build(ne,order):
    left,out=ne,[]
    for n,l in order:
        if left<=0: break
        cap=2*(2*l+1); o=min(left,cap); out.append((n,l,o)); left-=o
    return out
def config_c(ne,c):
    """the ground configuration, with the ordering set by CHARGE.

    Theodosiou, Manson & Inokuti 1986: the closed shells are the noble-gas numbers
    at z = 1 and the HYDROGENIC ones at z >= 3. So the filling order is Madelung
    for the neutral and hydrogenic for the multiply charged."""
    return build(ne, MAD if c<=1 else HYD)
def cp(ne,l,c): return sum(1 for n,ll,o in config_c(ne,c) if ll==l and o>0)
def out_(ne,c):
    cfg=config_c(ne,c); return cfg[-1] if cfg else (0,0,0)
def n0_(ne,l,c):
    v=[n for n,ll,o in config_c(ne,c) if ll==l and o>0]
    return (max(v)+1) if v else l+1
def thr_(ne,l,c): return OPEN.get((n0_(ne,l,c),l),9999)
def delta(Z,c,l):
    ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
    n_,l_,o_=out_(ne-1,c)
    if p>=1: return (a+b*l_)*math.sqrt(p)*ne**k*t
    D=Z-thr_(ne-1,l,c); x=max(-60.,min(60.,D/w))
    return h*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
print("  THE CHARGE-DEPENDENT ORDERING\n")
print("      neutral (c = 1) : Madelung, n+ℓ then n")
print("      ion (c ≥ 2)     : hydrogenic, n then ℓ")
print("      — Theodosiou, Manson & Inokuti 1986, applied as a rule not a fit\n")
for ne,c in ((19,1),(19,3),(21,1),(26,2)):
    print(f"      Nₑ={ne:>3} c={c}:  " +
          " ".join(f"{n}{L[l]}{o}" for n,l,o in config_c(ne,c) if o>0))
print()
print("  DOES IT FIX THE IONISATION ORDER?\n")
OBS={(21,1):(4,0),(21,2):(4,0),(21,3):(3,2),(22,1):(4,0),(22,2):(4,0),(22,3):(3,2),
     (23,1):(4,0),(23,2):(3,2),(23,3):(3,2),(24,1):(4,0),(24,2):(3,2),(24,3):(3,2),
     (25,1):(4,0),(25,2):(3,2),(25,3):(3,2),(26,1):(4,0),(26,2):(3,2),(26,3):(3,2),
     (27,1):(4,0),(27,2):(3,2),(28,1):(4,0),(28,2):(3,2),(29,1):(4,0),(29,2):(3,2),
     (30,1):(4,0),(30,2):(3,2),(39,1):(5,0),(39,3):(4,2),(40,1):(5,0),(40,3):(4,2),
     (57,1):(6,0),(57,3):(5,2),(20,1):(4,0),(20,2):(4,0),(19,1):(4,0),
     (12,1):(3,0),(12,2):(3,0),(13,1):(3,1),(14,1):(3,1),(15,1):(3,1),(16,1):(3,1),
     (17,1):(3,1),(18,1):(3,1)}
for lab,cfgfn in (("aufbau only",lambda ne,c: build(ne,MAD)),
                  ("charge-dependent",config_c)):
    ok=bad=0; miss=0
    for (Z,c),got in sorted(OBS.items()):
        ne=Z-c+1; cfg=cfgfn(ne,c)
        cand=[(n,l,o) for n,l,o in cfg if o>0]
        if len(cand)<2: continue
        sc=[(n,l,n-delta(Z,c,l)) for n,l,o in cand]
        if not any((x[0],x[1])==got for x in sc): miss+=1
        pick=max(sc,key=lambda x:x[2])
        if (pick[0],pick[1])==got: ok+=1
        else: bad+=1
    print(f"      {lab:<20}{ok:>4}/{ok+bad:<5}({100*ok/max(ok+bad,1):>5.1f}%)   "
          f"observed subshell absent from the configuration: {miss}")
print()
lo=[(Z,c) for (Z,c) in OBS if Z<21]; hi=[(Z,c) for (Z,c) in OBS if Z>=21]
for lab,sel in (("Z < 21",lo),("Z ≥ 21",hi)):
    ok=bad=0
    for (Z,c) in sel:
        got=OBS[(Z,c)]; ne=Z-c+1; cfg=config_c(ne,c)
        cand=[(n,l,o) for n,l,o in cfg if o>0]
        if len(cand)<2: continue
        sc=[(n,l,n-delta(Z,c,l)) for n,l,o in cand]
        pick=max(sc,key=lambda x:x[2])
        if (pick[0],pick[1])==got: ok+=1
        else: bad+=1
    print(f"      {lab:<10}{ok:>4}/{ok+bad:<4}({100*ok/max(ok+bad,1):>5.0f}%)")