#!/usr/bin/env python3
"""audit_tfd_floor.py -- Session 8. Scan COMPUTED-TFD.tsv (pack-5) for cells solved at the -0.6*zeta^2 floor.
Result: 0 of 103,545 at floor; max E/floor = 0.027 (Ne, ch 1, l 0, n 7). Step 2 solves at n0+4 (Rydberg)."""
import csv, sys
F=sys.argv[1] if len(sys.argv)>1 else "COMPUTED-TFD.tsv"; n=at=0; rmax=0; worst=None
for r in csv.DictReader(open(F),delimiter='\t'):
    n+=1; Z=int(r['Z']); ch=int(r['charge']); E=float(r['E'])
    if ch==Z: continue
    fl=-0.6*ch*ch
    if abs(E-fl)<1e-6*abs(fl)+1e-9: at+=1
    if E/fl>rmax: rmax=E/fl; worst=(Z,ch,r['l'],r['n_used'],E,fl)
print("cells",n,"AT floor",at,"max E/floor",round(rmax,4),worst)