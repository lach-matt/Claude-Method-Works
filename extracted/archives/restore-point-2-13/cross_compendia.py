#!/usr/bin/env python3
"""cross_compendia.py -- what one compendium says that the other can test.

Register 829. The Mathematical Compendium holds 213 objects; the Spectra Compendium
holds 413 channels across 38 spectra. Everything in both rests on the periodic table
and its atomic index as real measured numbers, so the two are answerable to the same
ground truth and to each other.

This asks three questions:

  1  Of the mathematical objects, how many are ANSWERABLE to atomic data at all —
     that is, how many make a claim a measured spectrum could contradict?
  2  Of those, how many have actually been checked against it?
  3  Where the two compendia speak about the same thing, do they agree?

The grades already carry part of the answer. DEFINITIONAL objects cannot be
contradicted by data — they are constructions. MEASURED objects must be. The
interesting class is anything graded COMPUTED or ASSERTED that touches a physical
coordinate, because those are claims about the world made without a measurement.
"""
import re, importlib.util as iu
from collections import Counter, defaultdict
from zeno import State, step

def load_math():
    sp = iu.spec_from_file_location("_m", "mathreg.py"); m = iu.module_from_spec(sp)
    try: sp.loader.exec_module(m)
    except SystemExit: pass
    return m.REG

# the coordinates the lattice is built from, and their physical meaning
PHYS = {"n":"principal quantum number", "l":"orbital angular momentum", "ℓ":"orbital angular momentum",
        "k":"valence occupancy", "q":"", "2S":"multiplicity", "2J":"total angular momentum",
        "Z":"nuclear charge", "delta":"quantum defect", "δ":"quantum defect",
        "Rydberg":"", "spectr":"", "atomic":"", "element":"", "level":"", "channel":""}

def analyse(REG):
    by_grade = Counter(v["grade"] for v in REG.values())
    touches = {}
    for k, v in REG.items():
        blob = " ".join(str(v.get(f) or "") for f in ("stmt","hyp","named","check"))
        hits = [t for t in PHYS if re.search(re.escape(t), blob)]
        touches[k] = hits
    physical = {k for k, h in touches.items() if h}
    # of the physical ones, which are graded as though data settled them?
    checked = {k for k in physical if REG[k]["grade"] in ("MEASURED","COMPUTED")
               and REG[k].get("check")}
    unchecked = {k for k in physical
                 if REG[k]["grade"] not in ("DEFINITIONAL","OPEN") and not REG[k].get("check")}
    fam = Counter(k.split(".")[0] for k in physical)
    return by_grade, physical, checked, unchecked, fam, touches

with State("cross_compendia") as s:
    REG = step(s, "load the mathematics register", load_math, budget=120)
    by_grade, physical, checked, unchecked, fam, touches = step(
        s, "cross-reference against the physical coordinates", lambda: analyse(REG), budget=300)

print(f"  THE MATHEMATICAL COMPENDIUM — {len(REG)} objects\n")
print(f"  by grade:")
for g, c in by_grade.most_common(): print(f"      {g:<16}{c:>5}")
print()
print(f"  ANSWERABLE TO ATOMIC DATA — the object names a physical coordinate")
print(f"      {len(physical)} of {len(REG)}   ({100*len(physical)//len(REG)}%)")
print(f"      by family: {dict(fam.most_common())}")
print()
print(f"      of those, carrying an explicit check : {len(checked)}")
print(f"      of those, carrying NONE             : {len(unchecked)}")
print()
if unchecked:
    print(f"  GRADED AS SETTLED, TOUCHING PHYSICS, NO CHECK RECORDED:")
    for k in sorted(unchecked)[:16]:
        print(f"      {k:<16}{REG[k]['grade']:<14}{(REG[k].get('named') or REG[k]['stmt'])[:60]}")
