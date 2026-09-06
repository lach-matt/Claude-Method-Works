# RULING S77.1 — M RULES OPTION B ON F77.1. RECORDED.

**No s76 row is written to LINEAGE.** The ladder reads ... 74, 75, 77. The 13 files
new at s76 are sealed at s77 close, inside the s77 root.

**`python3 pack58/condense.py 76 --check` WILL FAIL FOREVER. THAT IS THE INTENDED
STATE, NOT A DEFECT** — it is F77.1 made permanently visible from the tooling. Any
future session meeting that failure should read pack77/FAULT-F77.1-UNSEALED-HANDOFF.md
and stop, not seal.

**The integrity of s76 rests on the subset verification recorded in F77.1:** the 1215
paths sealed at s75 recompute to root ff11fa8d…bd62e, MATCH, with s76 adding 13,
changing 0, removing 0. That is the evidence, and it is stronger than a row would be.

**STANDING, FROM THIS RULING:** a session is not closed until `condense.py N --seal`
has run and the LINEAGE row exists. Tarring is not sealing.