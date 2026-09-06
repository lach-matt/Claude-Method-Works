import math
print("  THE CROSSING VALUES, EXACT\n")
print("      at each Nₑ, a descends through a specific value as c rises,")
print("      and the ladder's ordering flips there.\n")
X=[(20,"4s→3d",(4,0),(3,2),0.5773503),
   (38,"5s→4d",(5,0),(4,2),1.0000000),
   (56,"6s→5d",(6,0),(5,2),1.2167),
   (56,"5d→4f",(5,2),(4,3),0.7071068),
   (88,"7s→6d",(7,0),(6,2),1.3938)]
print(f"      {'Nₑ':>4}{'transition':>10}{'crossing a':>13}{'  exact form'}")
for ne,nm,(gn,gl),(rn,rl),v in X:
    gp=gn-gl-1; rp=rn-rl-1
    ex=f"({rn}−{gn})/(√{rp}−√{gp})"
    calc=(rn-gn)/(math.sqrt(rp)-math.sqrt(gp))
    print(f"      {ne:>4}{nm:>10}{v:>13.5f}   {ex} = {calc:+.5f}")
print()
print("  → the crossing value is exactly (Δn)/(√pᵣ − √p_g).")
print("    it is fixed by the two subshells alone, and NOT by Nₑ or c.\n")
print("  SO THE LAW SEPARATES\n")
print("      the CROSSING VALUE is arithmetic: two subshells, one surd.")
print("      the CHARGE at which a reaches it is physics.\n")
print(f"      {'transition':>10}{'crossing a':>13}{'crosses at c':>14}")
for nm,v,c in (("4s→3d",0.5774,"1→3"),("5s→4d",1.0000,"1→3"),
               ("6s→5d",1.2167,"1→2"),("5d→4f",0.7071,"2→3"),
               ("7s→6d",1.3938,"2→3")):
    print(f"      {nm:>10}{v:>13.4f}{c:>14}")
print()
print("  AND a(c) IS NOW BRACKETED AT EACH CHARGE, ACROSS ALL FOUR LADDERS\n")
B={1:[(20,0.577,1e9),(38,1.000,1e9),(56,1.217,1e9),(88,1.394,1e9)],
   2:[(20,-0.0,0.707),(38,-0.0,1.366),(56,0.707,1.217),(88,1.394,1e9)],
   3:[(20,-1e9,0.577),(38,-1e9,1.000),(56,-1e9,0.707),(88,-1e9,1.380)],
   4:[(20,-1e9,0.577),(38,-1e9,1.000)]}
print(f"      {'c':>3}{'Nₑ=20':>16}{'Nₑ=38':>16}{'Nₑ=56':>16}{'Nₑ=88':>16}")
for c in (1,2,3,4):
    row=f"      {c:>3}"
    d={n:(a,b) for n,a,b in B[c]}
    for ne in (20,38,56,88):
        if ne in d:
            a,b=d[ne]
            s=f"({a if a>-1e8 else float('-inf'):.2f},{b if b<1e8 else float('inf'):.2f})"
        else: s="—"
        row+=f"{s:>16}"
    print(row)
print()
print("  READING\n")
print("      c = 1 : every lower bound, no upper. a is LARGE and unbounded above.")
print("      c = 3 : every upper bound, no lower. a is SMALL and unbounded below.")
print("      c = 2 : two-sided at three of four ladders — the ONLY charge where")
print("              a is pinned from both directions.")
print()
print("      so the charge dependence is a DESCENT: a(c=1) > crossing > a(c=3),")
print("      and c = 2 is where it passes through. the brackets do not measure")
print("      a's value — they measure WHERE IT CROSSES, and that is a surd.")