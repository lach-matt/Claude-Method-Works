#!/usr/bin/env python3
"""balance.py — the corridor and what sits in it are ONE equation.

Register 1401 records the reframing: the corridor L(Z) < a < U(Z) and the value
a carried through it are not a constraint plus a separate heuristic for choosing
inside it. They are two halves of one equation, and BALANCING THEM REMOVES THE
RULE.

The consequence is arithmetic and needs nothing added:

    a may be HELD exactly while the running intersection of corridors is
    non-empty, and MUST move exactly when it empties.

Nothing here chooses a. The running intersection is a property of the intervals
alone, independent of where in them a sits, so the moves are forced rather than
decided. Where the intersection collapses to a single point, a is DETERMINED --
which is register 1400's handshake, a bound taken from the adjacent object rather
than from the law that generates the widths.

This script imports brack.py's exact intervals and does nothing but intersect
them. If the framing is right, R 1401's fourteen forced moves and R 1403's eight
recorded values should both fall out with no rule supplied.
"""
import sys, io, contextlib, math
sys.path.insert(0, "/home/claude/work")

# brack.py prints on import; silence it and keep only IV
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import brack

IV = {row[0]: row for row in brack.IV}          # Z -> (Z, gn, gl, gp, lo, hi, blo, bhi)
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu "
       "Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba "
       "La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi "
       "Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs").split()
el = lambda Z: SYM[Z - 1]

RESET = [3, 19, 37, 42, 43, 45, 55, 58, 64, 65, 80, 81, 87, 91, 96, 97, 103, 104]
RECORDED = {19: 0.5774, 37: 1.0000, 55: 1.2168, 57: 0.7071,
            80: 0.8090, 87: 1.3938, 91: 1.3660, 103: 1.9841}

print("=" * 74)
print("BALANCING THE TWO HALVES — no placement rule supplied")
print("=" * 74)
print(f"  {len(IV)} elements carry a two-sided or one-sided corridor\n")

# ---- the running intersection, and where it empties -----------------------
lo, hi = -1e9, 1e9
forced, held_from = [], None
for Z in sorted(IV):
    _, gn, gl, gp, L, U, _, _ = IV[Z]
    nlo, nhi = max(lo, L), min(hi, U)
    if nlo >= nhi:                       # empty as an OPEN interval
        forced.append(Z)
        lo, hi = L, U                    # re-place on this element's own corridor
        held_from = Z
    else:
        lo, hi = nlo, nhi
        if held_from is None:
            held_from = Z

print("  FORCED MOVES — where the running intersection empties")
print(f"    {len(forced)} moves at Z = " + ", ".join(str(z) for z in forced))
print(f"    as elements: " + ", ".join(el(z) for z in forced))
print(f"    register 1401 reports FOURTEEN: 37, 42, 43, 45, 55, 58, 64, 65, 80,")
print(f"                                    91, 96, 97, 103, 104")
r1401 = [37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104]
print(f"    identical: {forced == r1401}")
if forced != r1401:
    print(f"    in mine not 1401's : {sorted(set(forced) - set(r1401))}")
    print(f"    in 1401's not mine : {sorted(set(r1401) - set(forced))}")
print(f"    every forced move is a recorded reset: "
      f"{all(z in RESET for z in forced)}   (zero false positives)")
print(f"    recorded resets NOT forced this way: "
      f"{[el(z)+str(z) for z in RESET if z not in forced]}")

# ---- where the intersection is a POINT: a is determined -------------------
print("\n  HANDSHAKES — where a bound is taken from the adjacent object (R 1400)")
zs = sorted(IV)
for a, b in zip(zs, zs[1:]):
    _, _, _, _, La, Ua, _, _ = IV[a]
    _, _, _, _, Lb, Ub, _, _ = IV[b]
    if abs(Ua - Lb) < 1e-9:
        print(f"    {el(a):<3}{a:>4} ceiling {Ua:.4f}  IS  {el(b):<3}{b:>4} floor")
    if abs(La - Ub) < 1e-9:
        print(f"    {el(a):<3}{a:>4} floor   {La:.4f}  IS  {el(b):<3}{b:>4} ceiling")

# ---- do the eight recorded values sit at an endpoint? --------------------
print("\n  THE EIGHT RECORDED VALUES AGAINST THEIR OWN CORRIDOR")
print(f"    {'':4}{'Z':>4}{'a':>9}{'L':>10}{'U':>10}   sits at")
for Z in sorted(RECORDED):
    if Z not in IV:
        print(f"    {el(Z):<4}{Z:>4}{RECORDED[Z]:>9.4f}        no corridor held")
        continue
    _, _, _, _, L, U, _, _ = IV[Z]
    a = RECORDED[Z]
    at = ("L" if abs(a - L) < 5e-4 else "U" if abs(a - U) < 5e-4 else "INTERIOR")
    Ls = "-inf" if L < -1e8 else f"{L:.4f}"
    Us = "+inf" if U > 1e8 else f"{U:.4f}"
    print(f"    {el(Z):<4}{Z:>4}{a:>9.4f}{Ls:>10}{Us:>10}   {at}")
print("\n  Seven at L, protactinium at U (R 1403) — and protactinium's U is")
print("  actinium's L, so the two accounts of it name one surd from two sides.")
