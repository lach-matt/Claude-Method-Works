import math, statistics as st
import numpy as np
print("  THE RADIAL RATIO  R^ℓ(ns,n'ℓ) / R^0(ns,n'ℓ)  —  CAN IT BE COUNTED?\n")
print("      hydrogenic radial functions are polynomials in r times e^(−Zr/n).")
print("      every Slater integral over them is a RATIONAL FUNCTION of n, n', ℓ")
print("      and Z — no transcendentals survive. so the ratio is a rational")
print("      number when Z cancels, which it does in a ratio of same-pair")
print("      integrals.\n")
print("      the exact hydrogenic result for R^k(ns, n'ℓ) with n' = n−1 and")
print("      ℓ = 2 is a finite sum of binomials. rather than derive it, TEST")
print("      whether the measured crossing values ARE such rationals.\n")
D=[(20,(4,0),(3,2),0.577350269),(38,(5,0),(4,2),1.0),
   (56,(6,0),(5,2),1.216845),(88,(7,0),(6,2),1.393831)]
L="spdfg"
print(f"      {'pair':>8}{'a_cross':>12}{'(2ℓ+1)·a':>12}{'a²':>10}{'a²·(2ℓ+1)':>12}")
for ne,(gn,gl),(rn,rl),ac in D:
    print(f"      {f'{gn}{L[gl]}/{rn}{L[rl]}':>8}{ac:>12.6f}"
          f"{ac*(2*rl+1):>12.6f}{ac*ac:>10.6f}{ac*ac*(2*rl+1):>12.6f}")
print()
print("  BUT a_cross IS ALREADY EXACT — (Δn)/(√pᵣ − √p_g)\n")
print("      so the question is not what a_cross is. it is whether the")
print("      DESCENT a(c) reaching it can be counted.\n")
print("      the descent is bracketed by the crossing charges:\n")
CR=[(20,2),(38,2),(56,2),(70,3),(88,3),(102,5)]
print(f"      {'Nₑ':>5}{'crosses at c':>14}{'p_occ':>7}{'shells outside':>16}")
NOB=[0,2,10,18,36,54,86]
for ne,cc in CR:
    per=1+sum(1 for b in NOB[1:] if ne>b)
    p=per-1
    out=ne-max([b for b in NOB if b<ne])
    print(f"      {ne:>5}{cc:>14}{p:>7}{out:>16}")
print()
print("  THE COUNT THAT WORKS\n")
print("      Nₑ = 20, 38, 56 : two electrons outside a noble gas, cross at c=2")
print("      Nₑ = 70, 102    : sixteen outside (4f¹⁴6s² / 5f¹⁴7s²), cross later")
print("      Nₑ = 88         : two outside, but crosses at c=3\n")
print("      so 'electrons outside the closure' separates 70 and 102 from the")
print("      rest — but 88 breaks it. 88 has 2 outside and crosses at 3.\n")
print("  WHAT SEPARATES 88 FROM 20, 38, 56 ?\n")
print(f"      {'Nₑ':>5}{'occupied':>10}{'rival':>8}{'n_occ':>7}{'n_riv':>7}"
      f"{'Δn':>5}{'p_riv':>7}{'c':>4}")
for ne,(gn,gl),(rn,rl),cc in ((20,(4,0),(3,2),2),(38,(5,0),(4,2),2),
                              (56,(6,0),(5,2),2),(70,(6,0),(5,2),3),
                              (88,(7,0),(6,2),3),(102,(7,0),(6,2),5)):
    print(f"      {ne:>5}{f'{gn}{L[gl]}':>10}{f'{rn}{L[rl]}':>8}{gn:>7}{rn:>7}"
          f"{rn-gn:>5}{rn-rl-1:>7}{cc:>4}")
print()
print("      p_riv runs 0,1,2,2,3,3 and c runs 2,2,2,3,3,5.")
print("      → c rises with p_riv, but not as a function of it: p_riv = 2")
print("        gives c = 2 and 3; p_riv = 3 gives c = 3 and 5.")
print()
print("      the SECOND of each pair is always later. and the second of each")
print("      pair is the one with more electrons outside the closure.")
print()
print("  SO THE COUNT NEEDS TWO NUMBERS\n")
print(f"      {'Nₑ':>5}{'p_riv':>7}{'outside':>9}{'c observed':>12}{'p_riv+outside/8':>17}")
for ne,pr,out,cc in ((20,0,2,2),(38,1,2,2),(56,2,2,2),(70,2,16,3),
                     (88,3,2,3),(102,3,16,5)):
    print(f"      {ne:>5}{pr:>7}{out:>9}{cc:>12}{pr+out/8:>17.2f}")
print()
print("      p_riv + outside/8 gives 0.25, 1.25, 2.25, 4, 3.25, 5 against")
print("      c = 2, 2, 2, 3, 3, 5. monotone but not equal.")
