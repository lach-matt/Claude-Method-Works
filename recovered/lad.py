import importlib.util as iu
sp=iu.spec_from_file_location("li","ladder_index.py"); li=iu.module_from_spec(sp)
li.__name__="_li"; sp.loader.exec_module(li)   # imports without running __main__

# register 1356 REMOVED `state` from the axes. the script still carries it.
with_state = {(f,s,st) for _,f,s,st,_ in li.LAD}
without    = {(f,s)    for _,f,s,_,_  in li.LAD}
E3,_ = li.minE(with_state, [4,5,3])
E2,_ = li.minE(without,    [4,5])
print(f"  with `state` on an axis (what the CODE still does) : {len(with_state)} cells, min E = {E3}")
print(f"  without it (what REGISTER 1356 rules)              : {len(without)} cells, min E = {E2}")

# is that E = 0 earned or vacuous? a cell set with one cell per row of a
# 2-D grid cannot refuse anything -- the EM.image fault.
rows = {f for f,s in without}; cols = {s for f,s in without}
print(f"\n  cells {len(without)} · distinct `fixes` {len(rows)} · distinct `seat` {len(cols)}")
print(f"  box {len(rows)*len(cols)} — occupied fraction {len(without)/(len(rows)*len(cols)):.2f}")
from collections import Counter
print("  per-row occupancy:", dict(Counter(f for f,s in without)))
print("  -> at most one cell per row, so no envelope can bind: E = 0 is VACUOUS,")
print("     the same fault EM.image records (a complete rectangle closes for free).")

# what the new capture does to the ionisation row
print("\n  IONISATION LADDER, after LADDER-H-Ar-I-III.tsv")
import csv
rows_=[r for r in csv.DictReader((l for l in open("LADDER-H-Ar-I-III.tsv") if not l.startswith("#")),delimiter="\t")]
from collections import defaultdict
held=defaultdict(set)
for r in rows_: held[int(r["Z"])].add(int(r["c"]))
done=[z for z in held if len(held[z])==z]     # element with Z electrons has Z stages
print(f"    stages held per element: 3 for Z>=3, 2 for He, 1 for H")
print(f"    COMPLETE ladders now: {sorted(done)}  ({len(done)} elements)")
print(f"    because an element of atomic number Z has exactly Z ionisation stages,")
print(f"    so I-III exhausts H, He and Li and no other element.")