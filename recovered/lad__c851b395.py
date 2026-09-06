import sys; sys.path.insert(0,"/tmp")
import li_mod as li
with_state = {(f,s,st) for _,f,s,st,_ in li.LAD}
without    = {(f,s)    for _,f,s,_,_  in li.LAD}
E3,_ = li.minE(with_state, [4,5,3]); E2,_ = li.minE(without, [4,5])
print(f"  with `state` on an axis (what the CODE still does) : {len(with_state)} cells, min E = {E3}")
print(f"  without it (what REGISTER 1356 rules)              : {len(without)} cells, min E = {E2}")
from collections import Counter
rows={f for f,s in without}; cols={s for f,s in without}
print(f"\n  cells {len(without)} · distinct fixes {len(rows)} · distinct seat {len(cols)} · box {len(rows)*len(cols)}")
print("  per-row occupancy:", dict(Counter(f for f,s in without)))
print("  -> one cell per row, so no envelope can bind. E = 0 is VACUOUS —")
print("     the EM.image fault: a shape that closes for free certifies nothing.")
print("\n  IONISATION LADDER after LADDER-H-Ar-I-III.tsv")
import csv
from collections import defaultdict
rr=[r for r in csv.DictReader((l for l in open("/home/claude/work/LADDER-H-Ar-I-III.tsv") if not l.startswith("#")),delimiter="\t")]
held=defaultdict(set)
for r in rr: held[int(r["Z"])].add(int(r["c"]))
done=sorted(z for z in held if len(held[z])==z)
print(f"    an element of atomic number Z has exactly Z ionisation stages.")
print(f"    COMPLETE ladders now: Z = {done} -> {len(done)} elements")
print(f"    partial: Z = 4..18 at 3 of Z stages")