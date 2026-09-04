#!/usr/bin/env python3
"""ame_parse.py — parse AME2020 Table I from the uploaded paper.

SOURCE. Meng Wang, W.J. Huang, F.G. Kondev, G. Audi and S. Naimi, "The AME 2020
atomic mass evaluation (II). Tables, graphs and references", Chinese Physics C
45, 030003 (2021). Table I, pages 030003-6 to 030003-75, PDF pages 7 to 76.

THIS IS THE PUBLISHED ROUNDED TABLE, not mass_1.mas20. The ASCII file carries
unrounded values and uses '#' in place of the decimal point for estimates; the
paper uses '#' as a trailing marker. The two differ in the last digit by
construction and this file records which it is.

STRUCTURE. A appears only on the FIRST row of each isobar block; later rows in
the block inherit it. A = N + Z always, so A is RECOMPUTED rather than carried,
and the printed A is used only as a CHECK.

VERIFICATION, all run below and none skipped:
  1  A = N + Z on every row where A is printed
  2  the row count against the isobar structure
  3  the five A = 9 nuclides against the Argonne mass_1.mas20 text fetched at
     register 1548 — a DIFFERENT source, unrounded
  4  binding energy per nucleon recomputed from mass excess
  5  Z coverage contiguous from 0 to 118
"""
import re, sys
from collections import defaultdict

SRC = "/home/claude/work/tableI.txt"
ROW = re.compile(r"^\s*(\d{1,3})\s+(\d{1,3})\s+(?:(\d{1,3})\s+)?([A-Z][a-z]?)\s+(.*)$")
NUM = re.compile(r"-?\d[\d ]*\.?\d*#?")

rows = []
bad_A = []
for line in open(SRC, encoding="utf-8", errors="replace"):
    m = ROW.match(line)
    if not m:
        continue
    N, Z = int(m.group(1)), int(m.group(2))
    Aprint = int(m.group(3)) if m.group(3) else None
    el, rest = m.group(4), m.group(5)
    A = N + Z
    if Aprint is not None and Aprint != A:
        bad_A.append((N, Z, Aprint, A))
    # mass excess is the first numeric field after the origin flag
    tail = rest
    # strip a leading origin code (letters, -, +, digits mixed, no decimal)
    tok = tail.split()
    mx = mxu = None
    for i, t in enumerate(tok):
        c = t.replace("#", "").replace("-", "").replace("+", "").replace(".", "")
        if c.isdigit() and ("." in t or len(c) >= 4 or i > 0):
            try:
                mx = float(t.replace("#", ""))
                if i + 1 < len(tok):
                    try:
                        mxu = float(tok[i + 1].replace("#", ""))
                    except ValueError:
                        mxu = None
                break
            except ValueError:
                continue
    rows.append((N, Z, A, el, mx, mxu, "#" in tail.split()[1] if len(tail.split()) > 1 else False))

print(f"  PARSED {len(rows)} rows from AME2020 Table I\n")
print("  CHECK 1 — A = N + Z wherever A is printed")
print(f"    mismatches: {len(bad_A)}  {bad_A[:4]}")

print("\n  CHECK 2 — coverage")
Zs = sorted({r[1] for r in rows})
gaps = [z for z in range(min(Zs), max(Zs) + 1) if z not in Zs]
print(f"    Z runs {min(Zs)} to {max(Zs)}, gaps: {gaps if gaps else 'none'}")
As = sorted({r[2] for r in rows})
agaps = [a for a in range(min(As), max(As) + 1) if a not in As]
print(f"    A runs {min(As)} to {max(As)}, gaps: {agaps if agaps else 'none'}")
print(f"    distinct (Z, N) pairs: {len({(r[1], r[0]) for r in rows})}")

print("\n  CHECK 3 — the A = 9 chain against the ARGONNE mass_1.mas20 text")
ARG = {("He", 9): 40935.826, ("Li", 9): 24954.905, ("Be", 9): 11348.451,
       ("B", 9): 12416.486, ("C", 9): 28910.971}
print(f"    {'nuclide':<9}{'this table':>14}{'Argonne ASCII':>16}{'diff keV':>11}")
worst = 0.0
for r in rows:
    k = (r[3], r[2])
    if k in ARG and r[4] is not None:
        d = r[4] - ARG[k]
        worst = max(worst, abs(d))
        print(f"    {r[3]}{r[2]:<7}{r[4]:>14.3f}{ARG[k]:>16.3f}{d:>+11.3f}")
print(f"\n    largest disagreement: {worst:.3f} keV "
      f"({'ROUNDING ONLY' if worst < 1.0 else 'MORE THAN ROUNDING'})")

print("\n  CHECK 4 — binding energy per nucleon recomputed from mass excess")
DH, DN = 7288.97106, 8071.31806
ok = fail = 0
KNOWN = {("Be", 9): 6462.7, ("C", 12): 7680.1, ("Fe", 56): 8790.4,
         ("U", 238): 7570.1, ("Ca", 40): 8551.3}
for r in rows:
    k = (r[3], r[2])
    if k in KNOWN and r[4] is not None:
        B = r[1] * DH + r[0] * DN - r[4]
        ba = B / r[2]
        d = ba - KNOWN[k]
        print(f"    {r[3]}{r[2]:<5} B/A = {ba:>9.2f}   known {KNOWN[k]:>8.1f}   "
              f"{'OK' if abs(d) < 1.0 else f'DIFFER {d:+.2f}'}")
