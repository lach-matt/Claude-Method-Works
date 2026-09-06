import sys; sys.path.insert(0,"/tmp")
import li
SEAT,KIND,ZC = li.SEAT, li.KIND, li.ZCROSS
base = {(s,k,z) for _,_,s,k,z,_ in li.LAD}
axes = [len(SEAT),len(KIND),len(ZCROSS)] if False else [len(SEAT),len(KIND),len(ZC)]

def show(label, cells):
    E,defects = li.minE(cells, axes, want_defects=True)
    print(f"  {label:<44} {len(cells)} cells · E = {E}")
    for d in defects:
        print(f"        DEFECT ({SEAT[d[0]]}, {KIND[d[1]]}, {ZC[d[2]]})")
    return E

print("  ITEM 5 — Λ_ladder WITH THE X-RAY LADDERS IN\n")
E0 = show("12 ladders, as held", base)

# reading A: the X-ray ladders reach THE CORE (Lambda_chem's seat for K/L shells)
core = base | {(1,0,1), (1,1,0)}
print()
EA = show("+ X-ray at THE CORE (seats 1)", core)

# reading B: they reach SUBVALENCE, i.e. they fill the defect cells directly
sub = base | {(2,0,1), (2,1,0)}
print()
EB = show("+ X-ray at SUBVALENCE (seats 2)", sub)

print("\n  WHICH LADDERS SHARE A CELL UNDER READING A")
occ={}
for nm,_,s,k,z,_ in li.LAD: occ.setdefault((s,k,z),[]).append(nm)
occ.setdefault((1,0,1),[]).append("Moseley (X-ray, counting)")
occ.setdefault((1,1,0),[]).append("the Kα doublet (X-ray, coupling)")
for key,v in sorted(occ.items()):
    if len(v)>1:
        print(f"      ({SEAT[key[0]]}, {KIND[key[1]]}, {ZC[key[2]]}): {', '.join(v)}")