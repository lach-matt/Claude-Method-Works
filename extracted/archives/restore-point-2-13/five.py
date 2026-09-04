import math, statistics as st
import numpy as np
from scipy import stats as SS
print("  ALL ELEVEN LADDERS\n")
# Ne, occupied (n,l), rival (n,l), crossing charge (None = never)
LAD=[(4,(2,0),(2,1),None),(12,(3,0),(3,2),None),(20,(4,0),(3,2),2),
     (30,(4,0),(4,2),None),(38,(5,0),(4,2),2),(48,(5,0),(5,2),None),
     (56,(6,0),(5,2),2),(70,(6,0),(5,2),3),(80,(6,0),(6,2),None),
     (88,(7,0),(6,2),3),(102,(7,0),(6,2),None)]
L="spdfg"
print(f"      {'Nₑ':>4}{'occ':>6}{'rival':>7}{'Δn':>4}{'a_cross':>10}{'crosses at c':>14}")
PTS=[]
for ne,(gn,gl),(rn,rl),cc in LAD:
    gp=gn-gl-1; rp=rn-rl-1; dn=rn-gn
    if abs(math.sqrt(rp)-math.sqrt(gp))<1e-12: ac=float("nan")
    else: ac=dn/(math.sqrt(rp)-math.sqrt(gp))
    s=f"{ac:.4f}" if ac==ac and dn!=0 else "—"
    print(f"      {ne:>4}{f'{gn}{L[gl]}':>6}{f'{rn}{L[rl]}':>7}{dn:>4}{s:>10}"
          f"{(cc if cc else 'never'):>14}")
    if cc and dn!=0: PTS.append((ne,ac,cc))
print()
print("  THE CONSTRAINT FROM Nₑ = 102  —  Δn = −1 BUT NO CROSSING\n")
gp=7-0-1; rp=6-2-1; ac=(6-7)/(math.sqrt(rp)-math.sqrt(gp))
print(f"      7s: p = {gp}, 6d: p = {rp}, Δn = −1")
print(f"      a_cross = −1/(√{rp} − √{gp}) = {ac:.4f}")
print(f"      No crosses at NO charge up to 4, so a > {ac:.4f} at every c ≤ 4.")
print(f"      → the descent has NOT fallen below {ac:.4f} by charge 4 at Nₑ = 102.\n")
print("  THE FIVE CROSSING POINTS\n")
NE=np.array([p[0] for p in PTS],float); AC=np.array([p[1] for p in PTS])
print(f"      {'Nₑ':>4}{'a_cross':>10}{'at c':>7}")
for ne,ac,cc in PTS: print(f"      {ne:>4}{ac:>10.4f}{cc:>7}")
print()
print("  THE STATISTICS, NOW WITH FIVE POINTS\n")
print(f"      {'model':<28}{'r²':>9}{'rms':>9}{'  form'}")
for nm,X in (("ln Nₑ",np.log(NE)),("Nₑ^(1/3)",NE**(1/3)),("Nₑ^(2/3)",NE**(2/3)),
             ("√Nₑ",np.sqrt(NE)),("Nₑ",NE),("1 − Nₑ^(−1/3)",1-NE**(-1/3)),
             ("1 − Nₑ^(−1/2)",1-NE**(-0.5)),("Nₑ/(Nₑ+k), k=20",NE/(NE+20))):
    r=SS.linregress(X,AC); res=AC-(r.intercept+r.slope*X)
    print(f"      {nm:<28}{r.rvalue**2:>9.4f}{float(np.sqrt(np.mean(res**2))):>9.5f}"
          f"   {r.intercept:+.4f} {r.slope:+.4f}x")
print()
print("  AND THE TRANSITION CHARGE\n")
print("      crosses at 1→2 : Nₑ = 20, 38, 56")
print("      crosses at 2→3 : Nₑ = 70, 88")
print("      never by c = 4 : Nₑ = 102")
print()
print("      so the charge at which the descent reaches a_cross RISES with Nₑ,")
print("      and by Nₑ = 102 it has not arrived by charge 4.")
