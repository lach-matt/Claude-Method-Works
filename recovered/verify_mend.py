import eldata as ed
print("="*74); print("VERIFICATION: is the retrodiction robust to the 1869 list?"); print("="*74)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
def leq(a,b): return all(x<=y for x,y in zip(a,b))

def flagged(known):
    occ=set(ed.E[z] for z in known if z in ed.E)
    cells=set()
    for x in occ:
        for y in L:
            if leq(y,x) and y not in occ: cells.add(y)
    out=[]
    for c in sorted(cells):
        who=[z for z in ed.E if ed.E[z]==c]
        if who and who[0] not in known: out.append(who[0])
    return sorted(set(out))

# Variant A: my list
A={1,3,4,5,6,7,8,9,11,12,13,14,15,16,17,19,20,22,23,24,25,26,27,28,29,30,33,34,35,38,39,40,
   41,42,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,62,63,64,65,66,67,68,73,74,75,76,
   77,78,79,80,81,82,83,90,92}
# Variant B: conservative — drop the rare earths whose 1869 status was murky
B=A-{58,59,60,62,63,64,65,66,67,68}
# Variant C: add Cs, Rb, Tl, In which were known by 1869
C=A|{37,49,81}

for nm,K in [('A: as used',A),('B: minus disputed rare earths',B),('C: plus Rb/In/Tl',C)]:
    f=flagged(K)
    hits=[z for z in f if z in (21,31,32)]
    print(f"\n  {nm}  (|known|={len(K)})")
    print(f"    flagged: {[ed.SYM[z] for z in f]}")
    print(f"    Mendeleev's three among them: {[ed.SYM[z] for z in hits]}  ({len(hits)}/3)")

print()
print("="*74); print("WHAT THE TEST DOES AND DOES NOT SHOW"); print("="*74)
print("""  The down-set property flags every admissible cell lying below an
  occupied cell but itself unoccupied. Applied to the 1869 element set
  it flags 13 cells, including all three of Mendeleev's famous
  predictions — eka-boron (Sc), eka-aluminium (Ga), eka-silicon (Ge).

  BUT the flag is not selective. It also flags the noble gases (He, Ne,
  Ar, Kr, Xe), which Mendeleev did NOT predict and whose existence was
  a genuine surprise in the 1890s. And it flags Rb, Hf, Tc, Pm, Pa.
  So it produces 13 candidates where Mendeleev produced 3, and it does
  not rank them.

  The honest reading: the ideal property is a COMPLETENESS CHECK, not a
  prediction engine. It says 'these cells must be filled if the ideal
  property holds' — a necessary condition, not a targeted forecast.
  Mendeleev did far better with chemical reasoning, and did it in 1869.""")