import math
import numpy as np
src=open("/tmp/final2.py",encoding="utf-8").read()
src=src[:src.index('print("  THE EQUATION WITH THE MEASURED SWITCH')]
g={}; exec(src,g)
cfg_c,cp,out_,n0_,thr_=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["thr_"]
a,q,k=0.4751,-0.0403,0.4666
RY=109737.316
L="spdfg"
print("  THE THREE THRESHOLD CAPTURES — orbital orderings read directly\n")
print("  Y II   Z=39 c=2   5s² ground · 4d.5s at 840.198 · 4d² at 8003.126")
print("         → one electron moved 5s→4d costs +840 cm⁻¹.  5s BELOW 4d.\n")
print("  La II  Z=57 c=2   5d² ground · 5d.6s at 1895.15 · 6s² at 7394.57")
print("                    · 4f.5d at 16599.17")
print("         → 5d BELOW 6s by 1895.  4f ABOVE 5d by 16599.\n")
print("  Ce III Z=58 c=3   4f² ground · 4f.5d at 3276.66 · 5d² at 40440.20")
print("         → 4f BELOW 5d by 3277.  THE ORDERING HAS FLIPPED.\n")
print("  ── the 4f/5d crossing happens between Z = 57 and Z = 58 ──\n")
OBS=[("Y II",39,2,(5,0),(4,2), 840.198),
     ("La II",57,2,(5,2),(6,0), 1895.15),
     ("La II",57,2,(5,2),(4,3), 16599.17),
     ("Ce III",58,3,(4,3),(5,2), 3276.66)]
def delta(Z,c,l):
    ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
    n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
    if p>=1: return (a+q*(n0-n_))*math.sqrt(p)*ne**k*t
    T=thr_(ne-1,l,c); x=max(-60.,min(60.,(Z-T+1.5)/0.40))
    return 0.37*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
def E(Z,c,n,l):
    d=delta(Z,c,l); ns=n-d
    return -(c**2)*RY/max(ns,0.2)**2
print(f"  {'species':<8}{'lower':>7}{'upper':>7}{'measured Δ':>13}{'equation Δ':>13}{'sign':>7}")
for nm,Z,c,lo,hi,dE in OBS:
    e1=E(Z,c,lo[0],lo[1]); e2=E(Z,c,hi[0],hi[1])
    pred=e2-e1
    ok="OK" if pred>0 else "WRONG"
    print(f"  {nm:<8}{f'{lo[0]}{L[lo[1]]}':>7}{f'{hi[0]}{L[hi[1]]}':>7}"
          f"{dE:>13.0f}{pred:>13.0f}{ok:>7}")
print()
print("  WHAT THE EQUATION NEEDS AT EACH THRESHOLD\n")
print("      solve for δ of the collapsing orbital that reproduces the measured Δ\n")
print(f"      {'species':<8}{'orbital':>9}{'δ required':>12}{'δ equation':>12}{'ratio':>8}")
for nm,Z,c,lo,hi,dE in OBS:
    n_h,l_h=hi
    e_lo=E(Z,c,lo[0],lo[1])
    target=e_lo+dE                       # the upper orbital's energy
    ns=c*math.sqrt(RY/max(-target,1e-9))
    need=n_h-ns
    have=delta(Z,c,l_h)
    print(f"      {nm:<8}{f'{n_h}{L[l_h]}':>9}{need:>12.4f}{have:>12.4f}"
          f"{(need/have if have>1e-6 else float('nan')):>8.2f}")
