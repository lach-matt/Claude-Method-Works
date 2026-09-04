#!/usr/bin/env python3
"""per_atom.py — a calibrated per atom, with nothing carried across species.

THE CALIBRATION ERROR THIS CORRECTS. Every placement rule tried so far carries a
single a ACROSS elements — endpoints, block floors, handshakes, per-run windows.
That pools a constant across species, which Lambda_phys forbids: no parameter of
this work is universal, and a result conditioned on a coordinate holds exactly
where that coordinate separates. If a must be calibrated to the atom, then "the
trajectory of a" is a category error. There is no trajectory. There are 106
per-atom values, each fixed by that atom's own arithmetic.

THE RULE, with no observation and nothing carried:

    for each admissible candidate c at this atom
        compute c's OWN corridor (L_c, U_c) from node counts and capacities
        a_c = L_c + t(l_c) * (U_c - L_c)        the entry point, R Lambda_t
        c is SELF-CONSISTENT if argmin nu at a_c is c itself

    t(l) = sqrt( l(l+1) / 2 )     the centrifugal term: 0, 1, sqrt3, sqrt6

Nothing above reads the record. The corridor of a candidate is what its node
counts say; the entry point is what its angular momentum says. The record is
consulted only to score afterwards.

A DETERMINED step is one where exactly one candidate is self-consistent. Steps
with none or several are reported as such rather than resolved by a tie-break,
because a tie-break carried across atoms would reintroduce the pooling.
"""
import sys, io, contextlib, math
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack
import ground as G

L = "spdfg"
cap = lambda l: 2 * (2 * l + 1)
EPS = 1e-9
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)
OBS = {Z: (IV[Z][1], IV[Z][2]) for Z in STEPS}
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga "
       "Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd "
       "Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac "
       "Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf").split()

t_entry = lambda l: math.sqrt(l * (l + 1) / 2)


def occ(Z):
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


def cands(prev):
    c = []
    for l in range(5):
        for n in range(l + 1, 9):
            if prev.get((n, l), 0) >= cap(l):
                continue
            c.append((n, l))
            if prev.get((n, l), 0) == 0:
                break
    return c


def rad(nl, prev):
    n, l = nl
    return (n - l - 1) + prev.get(nl, 0) / cap(l)


def nu(nl, prev, a):
    return nl[0] - a * math.sqrt(rad(nl, prev))


def pick(prev, a):
    s = [(nu(c, prev, a), c[0], c[1]) for c in cands(prev)]
    b = min(x[0] for x in s)
    tied = [(n, l) for v, n, l in s if v - b < EPS]
    return max(tied, key=lambda x: x[0])


def corridor_for(prev, entrant):
    """Node counts and capacities only. No observation."""
    rg = rad(entrant, prev)
    lo, hi = -1e9, 1e9
    for c in cands(prev):
        if c == entrant:
            continue
        d = math.sqrt(rad(c, prev)) - math.sqrt(rg)
        if abs(d) < 1e-12:
            continue
        x = (c[0] - entrant[0]) / d
        if d > 0:
            hi = min(hi, x)
        else:
            lo = max(lo, x)
    return lo, hi


def a_of(prev, c, span):
    lo, hi = corridor_for(prev, c)
    fl, fu = lo > EPS and lo < 1e8, hi < 1e8
    t = t_entry(c[1])
    if fl and fu:
        return lo + t * (hi - lo)
    if fl:
        return lo * (1 + t)          # one-sided below: scale off the only bound
    if fu:
        return hi / (1 + t) if t > 0 else hi
    return None


det = hit = amb = non = 0
misses, ambiguous, none_ = [], [], []
for Z in STEPS:
    prev = occ(Z - 1)
    ok = []
    for c in cands(prev):
        a = a_of(prev, c, None)
        if a is None or a <= 0:
            continue
        if pick(prev, a) == c:
            ok.append(c)
    if len(ok) == 1:
        det += 1
        if ok[0] == OBS[Z]:
            hit += 1
        else:
            misses.append((Z, OBS[Z], ok[0]))
    elif len(ok) == 0:
        non += 1
        none_.append(Z)
    else:
        amb += 1
        ambiguous.append((Z, len(ok), OBS[Z] in ok))

print("  PER-ATOM CALIBRATION — a from this atom's own corridor and its own l\n")
print(f"    determined (exactly one self-consistent candidate) : {det} of {len(STEPS)}")
print(f"      of those, correct                                : {hit}"
      f"  = {100*hit/det:.0f}% of determined, {100*hit/len(STEPS):.0f}% of all steps")
print(f"    ambiguous (several self-consistent)                : {amb}"
      f"   observed among them: {sum(1 for _,_,o in ambiguous if o)}")
print(f"    none self-consistent                               : {non}")
if misses:
    print("\n    determined but WRONG:")
    for Z, o, g in misses:
        print(f"      {SYM[Z-1]}{Z}  observed {o[0]}{L[o[1]]}  said {g[0]}{L[g[1]]}")
print(f"\n  BENCHMARKS on the same 106 steps")
print(f"    plain Madelung, no free parameter, conditional   96")
print(f"    per-step placement carried across atoms, held out 90")
print(f"    per-run placement carried across atoms, held out  90")
print(f"    per-atom, nothing carried                        {hit}"
      f"   (+{amb} ambiguous, {non} undetermined)")
