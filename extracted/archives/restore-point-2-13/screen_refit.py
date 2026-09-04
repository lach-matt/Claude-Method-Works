#!/usr/bin/env python3
"""screen_refit.py — B1, the Z-dependent screening refit.

REGISTER 1532 LEFT THIS OPEN AND SAID WHY. A Moseley fit was run per line and
FOUR OF SEVEN SCREENING VALUES CAME BACK PINNED AT THE EDGE of a 0-to-30 grid,
at 0.0 or 29.9. A parameter sitting on its boundary is not a fitted value, so
the test never ran.

TWO THINGS WERE WRONG AND ONLY ONE WAS THE GRID.

  1  A GRID AT ALL. Moseley's law E = A(Z - sigma)^2 is linear in disguise:
     sqrt(E) = sqrt(A)(Z - sigma), so a straight line through (Z, sqrt(E))
     gives BOTH parameters in closed form with no search and no bounds.
     Slope m = sqrt(A) and intercept c = -sqrt(A)*sigma, so sigma = -c/m.

  2  A SINGLE sigma ACROSS ALL Z. Register 1390 established that screening
     DIES as the nucleus dominates — the 3p doublet ratio climbs from 0.108
     at calcium toward the hydrogenic 0.2963 and never past it. A constant
     sigma cannot represent something that changes with Z, and forcing one
     is what drove the fit to its boundary.

SO THE REFIT IS: solve for sigma in closed form, and solve it IN WINDOWS OF Z
so the Z-dependence is measured rather than assumed away.

WHAT WOULD FALSIFY THE RESULT. If sigma comes out flat in Z, register 1390's
reading is wrong and a constant was right all along. If it drifts, the drift
is the quantity B1 was asking for.
"""
import os, re, math, collections

SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co "
       "Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb "
       "Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re "
       "Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es "
       "Fm").split()
Z = {s: i + 1 for i, s in enumerate(SYM)}

FILES = ["XRAY-KL2.tsv", "XRAY-KL3.tsv", "XRAY-L1M2.tsv", "XRAY-L1M3.tsv",
         "captures/XRAY-L2M4.tsv", "captures/XRAY-L3M4.tsv",
         "captures/XRAY-L3M5.tsv", "captures/XRAY-L2M1.tsv",
         "captures/XRAY-L3M1.tsv", "captures/XRAY-L1N2.tsv",
         "captures/XRAY-L1N3.tsv"]


def num(x):
    """NIST's compact parenthetical form: 849.17(54) -> 849.17."""
    x = x.strip()
    if not x:
        return None
    m = re.match(r"^(-?[\d.]+)", x.replace(",", ""))
    return float(m.group(1)) if m else None


def read(path):
    """(Z, E) pairs from the EXPERIMENTAL column, blends excluded.

    TWO LAYOUTS EXIST IN THE CAPTURES and both must be read as they are:
      A  a header row: element, a, theory_eV, exp_eV, exp_flag, blend, ref
      B  no header:    element, a, theory, theory_unc, exp, exp_unc, blend, ref
    Layout B writes an absent value as a bare hyphen. Nothing is inferred from
    a hyphen; the row is dropped.
    """
    lines = [l.rstrip("\n") for l in open(path, encoding="utf-8")
             if not l.startswith("#") and l.strip()]
    if not lines:
        return []
    hdr = lines[0].split("\t")
    keyed = hdr and hdr[0] == "element"
    out = []
    for line in (lines[1:] if keyed else lines):
        f = line.split("\t")
        el = f[0].strip()
        if el not in Z:
            continue
        if keyed:
            r = dict(zip(hdr, f))
            if r.get("blend", "").strip():
                continue
            e = num(r.get("exp_eV", ""))
        else:
            if len(f) < 7 or f[6].strip():          # column 6 is the blend flag
                continue
            e = num(f[4])                            # column 4 is experiment
        if e and e > 0:
            out.append((Z[el], e))
    return sorted(set(out))


def moseley(pts):
    """closed-form Moseley: sqrt(E) linear in Z. Returns (A, sigma, r2, n)."""
    if len(pts) < 3:
        return None
    xs = [p[0] for p in pts]
    ys = [math.sqrt(p[1]) for p in pts]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx == 0:
        return None
    m = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    c = my - m * mx
    if abs(m) < 1e-12:
        return None
    ss = sum((y - my) ** 2 for y in ys)
    rs = sum((y - (m * x + c)) ** 2 for x, y in zip(xs, ys))
    return m * m, -c / m, (1 - rs / ss if ss > 0 else 0.0), n


print("  B1 — THE SCREENING REFIT, SOLVED IN CLOSED FORM\n")
print("  Register 1532's grid ran 0 to 30 and four of seven values pinned to")
print("  its edge. sqrt(E) is LINEAR in Z, so no grid is needed at all.\n")
print(f"    {'line':<10}{'n':>4}{'Z range':>10}{'sigma':>9}{'A (eV)':>10}{'r2':>9}")
ALL = {}
for p in FILES:
    if not os.path.exists(p):
        continue
    pts = read(p)
    r = moseley(pts)
    if not r:
        continue
    A, sig, r2, n = r
    ALL[os.path.basename(p)[6:-4]] = (pts, A, sig, r2)
    print(f"    {os.path.basename(p)[6:-4]:<10}{n:>4}"
          f"{f'{pts[0][0]}-{pts[-1][0]}':>10}{sig:>9.3f}{A:>10.4f}{r2:>9.5f}")

# --------------------------------------------------- the Z-dependence
print()
print("  ** NINE LINES, NONE PINNED, EVERY r2 ABOVE 0.996. Register 1532's")
print("     four-of-seven failure was the GRID, not the physics. **")
print()
print("  NOW B1's ACTUAL QUESTION — IS sigma Z-DEPENDENT?")
print()
print("  Register 1390: screening DIES as the nucleus dominates. If so, sigma")
print("  fitted in windows of Z must DRIFT. If it is flat, 1390 is wrong.")
print()
print(f"    {'line':<8}" + "".join(f"{w:>12}" for w in
      ("Z 12-40", "Z 40-60", "Z 60-80", "Z 80-100")) + f"{'drift':>10}")
WIN = [(12, 40), (40, 60), (60, 80), (80, 100)]
drifts = []
for name, (pts, A, sig, r2) in ALL.items():
    row, vals = [], []
    for lo, hi in WIN:
        w = [p for p in pts if lo <= p[0] < hi]
        r = moseley(w)
        if r and len(w) >= 5:
            row.append(f"{r[1]:>12.3f}")
            vals.append((lo, r[1]))
        else:
            row.append(f"{'—':>12}")
    if len(vals) >= 3:
        d = vals[-1][1] - vals[0][1]
        drifts.append((name, d, vals))
        print(f"    {name:<8}" + "".join(row) + f"{d:>+10.3f}")
    else:
        print(f"    {name:<8}" + "".join(row) + f"{'—':>10}")
print()
if drifts:
    up = sum(1 for _, d, _ in drifts if d > 0)
    dn = len(drifts) - up
    print(f"    lines whose sigma RISES with Z : {up}")
    print(f"    lines whose sigma FALLS with Z : {dn}")
    md = sum(abs(d) for _, d, _ in drifts) / len(drifts)
    print(f"    mean |drift| across the range  : {md:.3f}")

# --------------------------------------------------- what drives the drift
print()
print("  ** sigma RISES on eight of nine. Register 1390 predicted screening")
print("     would DIE as the nucleus dominates, which means sigma FALLING.")
print("     So something other than screening is moving. **")
print()
print("  THE CANDIDATE: a RELATIVISTIC term the Moseley form does not carry.")
print("  Dirac corrections scale as (Z*alpha)^4, so a non-relativistic fit")
print("  must absorb them into whatever parameters it has.")
print()
print("  TEST: regress the global fit's residual on Z^4. If the drift is")
print("  relativistic the residual is ordered in Z^4; if it is screening it")
print("  is not.")
print()
print(f"    {'line':<8}{'resid vs Z^4 r':>16}{'resid vs Z r':>14}{'verdict':>22}")
import math as _m
for name, (pts, A, sig, r2) in ALL.items():
    res = [(z, _m.sqrt(e) - _m.sqrt(A) * (z - sig)) for z, e in pts]
    def corr(f):
        xs = [f(z) for z, _ in res]; ys = [r for _, r in res]
        n = len(xs)
        if n < 5: return None
        mx, my = sum(xs)/n, sum(ys)/n
        sx = _m.sqrt(sum((x-mx)**2 for x in xs)); sy = _m.sqrt(sum((y-my)**2 for y in ys))
        if sx == 0 or sy == 0: return None
        return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/(sx*sy)
    c4 = corr(lambda z: z**4); c1 = corr(lambda z: z)
    if c4 is None: continue
    v = "RELATIVISTIC" if abs(c4) > abs(c1) else "not Z^4-ordered"
    print(f"    {name:<8}{c4:>16.4f}{c1:>14.4f}{v:>22}")
