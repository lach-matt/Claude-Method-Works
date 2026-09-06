import eldata as ed
print("="*74)
print("TEST 2: WOULD Λ HAVE PREDICTED THE ELEMENTS MISSING IN 1869?")
print("="*74)
# Elements known by 1869 (Mendeleev's table). 63 elements.
KNOWN1869 = {1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,
 33,34,35,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,62,63,64,65,66,
 67,68,73,74,75,76,77,78,79,80,81,82,83,90,92}
# (approximate; He/Ne/Ar not isolated until 1890s, Sc/Ga/Ge predicted by Mendeleev)
KNOWN1869 = KNOWN1869 - {2,21,31,32}   # remove noble gases not yet found + Mendeleev's 3 predictions
print(f"  elements known in 1869: {len(KNOWN1869)}")

occ_then = set(ed.E[z] for z in KNOWN1869 if z in ed.E)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
def leq(a,b): return all(x<=y for x,y in zip(a,b))

# Was the 1869 set an order ideal?
viol=[(y,x) for x in occ_then for y in L if leq(y,x) and y not in occ_then]
print(f"  down-set violations in the 1869 set: {len(viol)}")
print()
if viol:
    print("  The cells that were 'missing' — admissible, below an occupied cell,")
    print("  but unoccupied in 1869. These are the gaps the ideal property flags:")
    seen=set()
    for y,x in sorted(viol):
        if y in seen: continue
        seen.add(y)
        # which element actually occupies it now?
        who=[z for z in ed.E if ed.E[z]==y]
        nm=ed.SYM[who[0]] if who else '—'
        zz=who[0] if who else None
        print(f"    {str(y):>12}  now held by {nm:>3} (Z={zz})")
    print()
    print(f"  {len(seen)} distinct cells flagged")
    disc=[z for z in ed.E if ed.E[z] in seen and z not in KNOWN1869]
    print(f"  of which subsequently filled by: {sorted(ed.SYM[z] for z in disc)}")
    print()
    print("  Mendeleev predicted eka-boron (Sc), eka-aluminium (Ga), eka-silicon (Ge).")
    hit=[ed.SYM[z] for z in disc if z in (21,31,32)]
    print(f"  Of those three, the ideal property flags: {hit or 'none'}")