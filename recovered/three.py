import sys; sys.path.insert(0,"/tmp")
import li_mod as li
from itertools import product, permutations

# ladders: isoelectronic, walk, ionisation, isotopic
FIX  = [0,1,2,3]          # Ne | c | Z | Z,Ne,c   (the existing axis)
SEAT = [3,3,2,0]          # valence | valence | subvalence | nucleus

# candidate THIRD axes. each must be a property of the LADDER, not of our
# progress on it (register 1356) and not derived from the other two (A.derived).
CAND = {
 "relation it lives in  (electronic | nuclear)":      [0,0,0,1],
 "Lambda coordinate the variation moves (c|Ne|both|none)": [0,1,2,3],
 "arity of the fixing   (one observable | three)":     [0,0,0,1],
 "does it cross a block boundary (yes|no)":            [0,1,1,0],
}

def report(name, third, axes):
    cells = {(FIX[i], SEAT[i], third[i]) for i in range(4)}
    E,_ = li.minE(cells, axes)
    # is any axis non-injective?  and does the box exceed the cells?
    box = axes[0]*axes[1]*axes[2]
    ninj = [a for a,vals in enumerate([FIX,SEAT,third]) if len(set(vals))<4]
    return len(cells), box, E, ninj

print(f"{'third axis':<52}{'cells':>6}{'box':>6}{'minE':>6}  non-injective axes")
for nm,t in CAND.items():
    n,box,E,ninj = report(nm,t,[4,5,len(set(t))])
    print(f"{nm:<52}{n:>6}{box:>6}{E:>6}  {ninj}")

print("\nthe obstruction, stated exactly:")
print("  4 ladders, and the `fixes` axis is injective on them by construction —")
print("  a ladder IS named by what it holds fixed. so every candidate third axis")
print("  leaves at most one cell per (fixes) row, and the sort that monotonises")
print("  it always exists. E = 0 is forced at d = 3 for the same reason as d = 2.")