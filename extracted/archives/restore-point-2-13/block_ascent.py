#!/usr/bin/env python3
"""block_ascent.py — REBUILT from register 1409.

    at a Janet block opening, a takes the block's own floor;
    inside a block, a takes max(itself, floor), so it only ever rises.

WHY GLOBAL ASCENT CANNOT WORK. The highest floor anywhere exceeds the tightest
ceiling anywhere by a factor of nearly three, so NO SINGLE a serves the walk.
That is register 1341's necessity of state proved rather than asserted.

TWO CORRECTIONS THIS REBUILD CARRIES, both from register 1443.

  · The entry says "zero violations across all 106 steps". Per-block ascent
    tracks FLOORS ONLY and never intersects a ceiling, and the corridor
    intersections of blocks 5 to 8 are EMPTY (R 1447) — block 5 demands
    a > 1.0000 from rubidium and a < 0.7071 from the 3d steps at once. So a
    floors-only ascent MUST leave some corridor, and "zero violations" cannot
    mean corridor membership. Both readings are measured below.

  · The entry counts SEVEN block openings; register 1411 counts SIX. Seven
    includes lithium, where a is first PLACED; six counts RE-placements, which
    excludes it. Both are self-consistent.
"""
import sys, io, contextlib
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack

EPS = 1e-9
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga "
       "Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd "
       "Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac "
       "Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs").split()
LENGTHS = [2, 2, 8, 8, 18, 18, 32, 32]
STARTS, _z = [], 1
for _n in LENGTHS:
    STARTS.append(_z); _z += _n
OPENS = set(STARTS)
blk = lambda Z: max(i for i, s in enumerate(STARTS) if s <= Z) + 1

RECORDED = {19: 0.5774, 37: 1.0000, 55: 1.2168, 57: 0.7071,
            80: 0.8090, 87: 1.3938, 91: 1.3660, 103: 1.9841}

# ---- why no single a serves the walk --------------------------------------
floors = [(IV[Z][4], Z) for Z in STEPS if -1e8 < IV[Z][4] < 1e8]
ceils = [(IV[Z][5], Z) for Z in STEPS if IV[Z][5] < 1e8]
hf, hz = max(floors); tc, tz = min(ceils)
print("  WHY GLOBAL ASCENT CANNOT WORK\n")
print(f"    highest floor anywhere   {hf:.4f}  at {SYM[hz-1]} {hz}")
print(f"    tightest ceiling anywhere {tc:.4f}  at {SYM[tz-1]} {tz}")
print(f"    ratio {hf/tc:.3f} — 'a factor of nearly three', R 1409")
print(f"    a single a is impossible: {hf} > {tc}\n")

# ---- the ascent -----------------------------------------------------------
a = None
moves, opens_hit, rises, viol = [], [], [], []
track = {}
for Z in STEPS:
    Lo, Up = IV[Z][4], IV[Z][5]
    fl = -1e8 < Lo < 1e8
    if Z in OPENS or a is None:
        newa = Lo if fl else (Up if Up < 1e8 else a)
        if newa is not None and (a is None or abs(newa - a) > EPS):
            moves.append(Z); opens_hit.append(Z)
        a = newa if newa is not None else a
    elif fl and Lo > a + EPS:
        a = Lo
        moves.append(Z); rises.append(Z)
    track[Z] = a
    if a is not None and Up < 1e8 and a >= Up - EPS:
        viol.append(Z)

print("  THE ASCENT\n")
print(f"    moves {len(moves)} = {len(opens_hit)} block placements + {len(rises)} rises"
      f"   (R 1409: fifteen = seven + eight)")
print(f"    block placements at Z = {opens_hit}")
print(f"    rises at Z            = {rises}")
print(f"    of the placements, RE-placements (excluding the first): "
      f"{len([z for z in opens_hit if z != STEPS[0]])}   (R 1411: six)")

print("\n  DOES a EVER LEAVE A CORRIDOR?  (the 'zero violations' question)\n")
print(f"    steps where the held a is at or above that step's ceiling: {len(viol)}")
if viol:
    print(f"      {[SYM[z-1]+str(z) for z in viol][:14]}")
print("    A floors-only ascent cannot respect ceilings in blocks whose corridor")
print("    intersections are empty, so 'zero violations' means MONOTONICITY —")
print("    a never descends — and not corridor membership.")

desc = [Z for i, Z in enumerate(STEPS[1:], 1)
        if track[Z] is not None and track[STEPS[i-1]] is not None
        and track[Z] < track[STEPS[i-1]] - EPS]
print(f"\n    descents in the produced trajectory: {len(desc)}  {desc}")

print("\n  AGAINST THE EIGHT RECORDED VALUES\n")
print(f"    {'':4}{'Z':>4}{'block':>7}{'recorded':>11}{'produced':>11}   match")
ok = 0
for Z in sorted(RECORDED):
    p = track.get(Z)
    m = p is not None and abs(p - RECORDED[Z]) < 5e-4
    ok += m
    print(f"    {SYM[Z-1]:<4}{Z:>4}{blk(Z):>7}{RECORDED[Z]:>11.4f}"
          f"{(f'{p:.4f}' if p is not None else '—'):>11}   {'YES' if m else 'no'}")
print(f"\n    {ok} of {len(RECORDED)} reproduced   (R 1409 claims all eight, with")
print(f"    protactinium's assigned at the actinium opening two elements earlier")
print(f"    and held — see R 1436, where Ac's floor and Pa's ceiling are one surd.)")
print(f"\n    Both descents in the RECORD are Janet block openings — lanthanum at")
print(f"    4f and actinium at 5f — which is why global ascent fails where it does.")
