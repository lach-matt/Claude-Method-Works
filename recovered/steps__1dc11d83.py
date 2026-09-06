import math, statistics as st
import numpy as np
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
cfg=g["cfg"]; cp_=g["cp_"]; L="spdfg"
print("  THE STRUCTURAL STEP FROM Z TO Z+1  —  neutrals\n")
print("      each species' structure is the staircase n₀(ℓ) = p(ℓ) + ℓ + 1.")
print("      the step to the next element changes ONE p by ONE.\n")
print(f"      {'Z':>4}{'element':>4}{'n₀(s)':>7}{'n₀(p)':>7}{'n₀(d)':>7}{'n₀(f)':>7}"
      f"{'  which p rose'}")
EL={1:"H",2:"He",3:"Li",4:"Be",5:"B",6:"C",7:"N",8:"O",9:"F",10:"Ne",11:"Na",12:"Mg",
13:"Al",14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",19:"K",20:"Ca",21:"Sc",22:"Ti",23:"V",
24:"Cr",25:"Mn",26:"Fe",27:"Co",28:"Ni",29:"Cu",30:"Zn",31:"Ga",36:"Kr",37:"Rb",
38:"Sr",39:"Y",48:"Cd",49:"In",54:"Xe",55:"Cs",56:"Ba",57:"La",86:"Rn",87:"Fr"}
prev=None; steps=[]
for Z in range(2,90):
    n0=[cp_(Z-1,l,1)+l+1 for l in range(4)]
    if prev is not None:
        ch=[l for l in range(4) if n0[l]!=prev[l]]
        w=",".join(L[l] for l in ch) if ch else "—"
        steps.append((Z,tuple(n0),w))
        if Z in EL or ch:
            print(f"      {Z:>4}{EL.get(Z,''):>4}" + "".join(f"{v:>7}" for v in n0)
                  + f"   {w}")
    prev=n0
print()
from collections import Counter
c=Counter(w for _,_,w in steps)
print("      steps by which ℓ's n₀ rose:")
for k,v in c.most_common(): print(f"          {k:<6}{v:>4} steps of {len(steps)}")
print()
print("  THE STATEMENT\n")
print("      going from Z to Z+1, the core gains one electron. n₀(ℓ) rises by one")
print("      for exactly ONE ℓ — the ℓ whose subshell just CLOSED — and is")
print("      unchanged for every other ℓ.")
print()
print("      so the structural difference between adjacent species is a single")
print("      integer step in a single coordinate. the staircase moves one tread.")
print()
print("  AND THE STEP IN u\n")
print(f"      {'Z':>4}{'u = ln Nₑ':>12}{'Δu':>9}{'Δa predicted':>14}")
b0,b1,b2=-2.2402,1.3250,-0.1602
for Z in (2,5,10,20,36,54,86):
    u=math.log(Z); up=math.log(Z+1)
    a=math.exp(b0+b1*u+b2*u*u); ap=math.exp(b0+b1*up+b2*up*up)
    print(f"      {Z:>4}{u:>12.4f}{up-u:>9.4f}{ap-a:>14.4f}")
print()
print("      Δu = ln(1 + 1/Nₑ) ≈ 1/Nₑ — the step SHRINKS as the table grows.")
print("      so the amplitude changes fast at the top of the table and slowly")
print("      at the bottom, which is the periodicity's own envelope.")