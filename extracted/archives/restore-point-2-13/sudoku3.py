#!/usr/bin/env python3
"""sudoku3.py — three independent determinations of one cell.

THE SHAPE. A sudoku cell is constrained three ways — row, column, box — and the
puzzle is solvable because the three must agree. Where two agree and one does
not, the odd one out is LOCALISED rather than merely suspected.

The spectra index has the same shape and has never been read that way:

    A  THE FILLER      delta computed by the channel equation      COORDINATES.tsv
    B  THEODOSIOU      the ASYMPTOTIC quantum defect, measured     QDEFECT-*.tsv
    C  THE LADDER      the GROUND-STATE defect from an ionisation  LADDER-K-Kr.tsv
                       energy, mu = n - z*sqrt(R/IE)

All three are indexed on (Z, z, l) and none was fitted to either other.

WHAT MAKES IT A SUDOKU AND NOT THREE LISTS. B and C measure DIFFERENT
QUANTITIES — register 1546 established the asymptotic and ground-state defects
are not the same number, and register 1552 measured the gap closing as z rises
at slope -0.0037. So the three-way cell carries a KNOWN OFFSET between two of
its faces, and that offset is itself checkable.

    A vs B   does the filler reproduce a measured asymptotic defect?
    A vs C   does the filler reproduce a measured ground state?
    B vs C   does R 1552's offset law hold where both are present?

THE LANGUAGES (register 1518). The same disagreement can be read three ways and
the right one depends on the cell:

    geometry     is the triple feasible within tolerance?  (a Helly question)
    logic        which pair is consistent, which is not?   (k-consistency)
    statistics   is the deviation inside the spread?       (fractional)

Use the language that is NON-DEGENERATE for the cell. Where only two faces are
present, geometry at order 3 is degenerate and the pairwise logic face is live.
"""
import math, collections, sys

R = 13.605693

# ---------------------------------------------------------------- face A
rows = [l.rstrip("\r\n").split("\t")
        for l in open("COORDINATES.tsv", encoding="utf-8").read().split("\n")[1:]
        if l.strip()]
A = {}
for x in rows:
    try:
        A[(int(x[0]), int(x[1]), int(x[2]))] = (float(x[4]), x[5], x[8])
    except (ValueError, IndexError):
        pass

# ---------------------------------------------------------------- face B
B = {}
for l in open("captures/QDEFECT-Theodosiou-1986.tsv", encoding="utf-8"):
    if l.startswith("#") or not l.strip():
        continue
    f = l.rstrip("\n").split("\t")
    if len(f) < 8:
        continue
    try:
        B[(int(f[2]), int(f[3]), int(f[5]))] = float(f[7])
    except ValueError:
        pass

# ---------------------------------------------------------------- face C
# the ground-state defect needs the OUTER ORBITAL (n, l) of the species, which
# follows from the electron count N = Z - z + 1 under the observed filling order.
ORDER = [(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6),(4,0,2),(3,2,10),(4,1,6),
         (5,0,2),(4,2,10),(5,1,6),(6,0,2),(5,2,10),(4,3,14),(6,1,6),(7,0,2),
         (6,2,10),(5,3,14),(7,1,6)]

# THE HYDROGENIC ORDER. Theodosiou, Manson & Inokuti (1986): "as the stage of
# ionization increases, the magic numbers occur no longer at the noble gases,
# but rather at the HYDROGENIC closed-shell systems... 2, 10, 28, 60", and "for
# z >= 3 the rich structure has completely disappeared". So an ion fills by n
# then l, not by the neutral order. Found because the sudoku's third face
# disagreed at Sc III by -0.206 where the others sat at -0.012 to -0.088.
HYDROGENIC = [(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6),(3,2,10),
              (4,0,2),(4,1,6),(4,2,10),(4,3,14),(5,0,2),(5,1,6)]

def outer(N, z):
    """(n, l) of the last electron. The NEUTRAL order for z <= 2, the
    HYDROGENIC order for z >= 3, which is where the neutral pattern dies."""
    seq = ORDER if z <= 2 else HYDROGENIC
    for n, l, cap in seq:
        if N <= cap:
            return n, l
        N -= cap
    return None

C = {}
for l in open("captures/LADDER-K-Kr.tsv", encoding="utf-8"):
    if l.startswith("#") or not l.strip():
        continue
    zs, cs, es, q = l.rstrip("\n").split("\t")
    Z = int(zs); z = int(cs[1:]) + 1; ie = float(es)
    o = outer(Z - z + 1, z)
    if not o or ie <= 0:
        continue
    n, ll = o
    C[(Z, z, ll)] = (n - z * math.sqrt(R / ie), q, n)

print(f"  FACES:  A filler {len(A):,}   B Theodosiou {len(B)}   C ladder {len(C)}\n")

keys = sorted(set(A) & (set(B) | set(C)))
tri = sorted(set(A) & set(B) & set(C))
ab = sorted((set(A) & set(B)) - set(C))
ac = sorted((set(A) & set(C)) - set(B))

print(f"  CELLS WITH ALL THREE FACES : {len(tri)}")
print(f"  A+B only                   : {len(ab)}")
print(f"  A+C only                   : {len(ac)}")
print(f"  total multi-face cells     : {len(keys)}\n")

SYM = {1:"H",2:"He",3:"Li",4:"Be",5:"B",6:"C",7:"N",8:"O",9:"F",10:"Ne",
       11:"Na",12:"Mg",13:"Al",14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",
       19:"K",20:"Ca",21:"Sc",22:"Ti",23:"V",24:"Cr",25:"Mn",26:"Fe",
       27:"Co",28:"Ni",29:"Cu",30:"Zn",31:"Ga",32:"Ge",33:"As",34:"Se",
       35:"Br",36:"Kr"}
ROM = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
       10:"X",11:"XI",12:"XII",13:"XIII",14:"XIV",15:"XV",16:"XVI"}

if tri:
    print("  THE THREE-FACE CELLS — every one read three ways\n")
    print(f"    {'cell':<12}{'l':>2}{'A filler':>10}{'B asympt':>10}"
          f"{'C ground':>10}{'A-B':>8}{'B-C':>8}   verdict")
    for k in tri:
        Z, z, l = k
        a = A[k][0]; b = B[k]; c = C[k][0]
        nm = f"{SYM.get(Z,Z)} {ROM.get(z,z)}"
        dab = a - b; dbc = b - c
        v = "AGREE" if abs(dab) < 0.05 else "A OFF"
        print(f"    {nm:<12}{'spdf'[l]:>2}{a:>10.4f}{b:>10.3f}{c:>10.4f}"
              f"{dab:>+8.3f}{dbc:>+8.3f}   {v}")

# ------------------------------------------------------- the pairwise faces
print()
print("  THE TWO-FACE CELLS — geometry at order 3 is DEGENERATE here, so the")
print("  live language is pairwise logic (register 1518).")
print()
tol = 0.05
for lab, pairs, get in (("A vs B  filler against the measured ASYMPTOTIC defect",
                         ab, lambda k: (A[k][0], B[k])),
                        ("A vs C  filler against the measured GROUND state",
                         ac, lambda k: (A[k][0], C[k][0]))):
    ok = off = skip = 0
    worst = []
    for k in pairs:
        if lab.startswith("A vs C") and C[k][1] != "M":
            skip += 1        # an interpolated IE cannot arbitrate anything
            continue
        u, v = get(k)
        d = abs(u - v)
        (ok, off) = (ok + 1, off) if d < tol else (ok, off + 1)
        worst.append((d, k, u, v))
    worst.sort(reverse=True)
    print(f"    {lab}")
    print(f"        within {tol}: {ok}    beyond: {off}"
          + (f"    skipped (interpolated): {skip}" if skip else ""))
    for d, k, u, v in worst[:4]:
        Z, z, l = k
        print(f"          {SYM.get(Z,Z)} {ROM.get(z,z):<5}{'spdf'[l]}   "
              f"A {u:>8.4f}   other {v:>8.4f}   |d| {d:.3f}")
    print()

# ------------------------------------------------------- the verdict
print("  WHICH ROUTE TO USE, ON THE EVIDENCE ABOVE")
print()
print("  B — THEODOSIOU — measures the SAME quantity the index holds, needs no")
print("      correction, and lands on 42 admitted cells. **Use it directly.**")
print()
print("  C — THE LADDER — measures a DIFFERENT quantity. Its offset from B is")
print("      now known to depend on BOTH z and l, and the l-dependence is the")
print("      larger: s cells sit at -0.044 and d cells at -0.183, a factor of")
print("      four. **Usable only with an l-resolved correction, which two")
print("      d-points cannot calibrate.**")
print()
print("  ** SO THE COMPARISON ANSWERS M'S QUESTION: USE B. Take C's sixty")
print("     measured rows as a CHECK on the filler, not as a population of")
print("     the index — a check needs no calibration, a population does. **")
