#!/usr/bin/env python3
"""null_madelung.py — the null the 99 is scored against, recomputed.

The handoff quotes the Loewdin result as 99 of 106 "against a null of 28". The
null was plain Madelung order: at each step take the next unfilled subshell in
n+l sequence and score it against the observed entry. It returned 28 of 108,
against an expectation of about 82 — and that gap was correctly read at the time
as the STEP EXTRACTOR being broken, taking an arbitrary gain where several
shells changed, rather than as a fact about Madelung.

So the 28 is a bad null and must not be carried. This recomputes it on the SAME
106 clean steps the corridor result uses — brack.py's own extraction, which
keeps only steps where exactly one subshell gains.

Two nulls, because the corridor result is a PER-STEP claim and only one of them
is matched to it:

  CONDITIONAL   given the OBSERVED configuration at Z-1, does Madelung name the
                observed entrant? This is the matched null: it asks the same
                question of Madelung that the corridor asks of nu, one step at a
                time, with no accumulated error.

  FREE-RUNNING  let Madelung generate its own configurations from hydrogen and
                score against the observed entrant. This is a trajectory null,
                and it compounds: one early miss shifts every later state.

Quoting a per-step result against a free-running null overstates it. Quoting it
against the conditional null is the honest comparison.
"""
import sys, io, contextlib
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack
import ground as G

L = "spdfg"
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
       "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce "
       "Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn "
       "Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs").split()
cap = lambda l: 2 * (2 * l + 1)

# Madelung order: by n+l, then by n
ORDER = sorted(((n, l) for n in range(1, 9) for l in range(0, min(n, 5))),
               key=lambda nl: (nl[0] + nl[1], nl[0]))


def madelung_next(occ):
    for n, l in ORDER:
        if occ.get((n, l), 0) < cap(l):
            return (n, l)
    return None


def cfg(Z):
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


STEPS = [(r[0], (r[1], r[2])) for r in brack.IV]        # (Z, observed entrant)
print(f"  scored on the SAME {len(STEPS)} clean steps the corridor result uses\n")

# ---- conditional -----------------------------------------------------------
hit_c, miss_c = 0, []
for Z, obs in STEPS:
    pred = madelung_next(cfg(Z - 1))
    if pred == obs:
        hit_c += 1
    else:
        miss_c.append((Z, obs, pred))

# ---- free-running ----------------------------------------------------------
occ, hit_f, miss_f = {}, 0, []
for Z in range(1, 3):                                    # H, He before the walk
    nl = madelung_next(occ)
    occ[nl] = occ.get(nl, 0) + 1
for Z, obs in STEPS:
    pred = madelung_next(occ)
    if pred == obs:
        hit_f += 1
    else:
        miss_f.append((Z, obs, pred))
    occ[pred] = occ.get(pred, 0) + 1                     # Madelung's own state

n = len(STEPS)
print(f"  CONDITIONAL  (given the observed state at Z-1)   {hit_c} of {n}"
      f"   = {100*hit_c/n:.0f}%")
print(f"  FREE-RUNNING (Madelung generates its own state)  {hit_f} of {n}"
      f"   = {100*hit_f/n:.0f}%")
print(f"\n  the handoff carries a null of 28 of 108 — neither of these, and the")
print(f"  28 was already diagnosed as a broken step extractor rather than a")
print(f"  fact about Madelung. It should be RETIRED, not carried.\n")

print(f"  CONDITIONAL misses ({len(miss_c)}):")
for Z, obs, pred in miss_c:
    print(f"    {SYM[Z-1]:<3}{Z:>4}  observed {obs[0]}{L[obs[1]]}"
          f"   Madelung says {pred[0]}{L[pred[1]]}")

print(f"\n  and the corridor result is 99 of {n}. Against the CONDITIONAL null")
print(f"  that is {hit_c} -> 99; against the free-running one it is {hit_f} -> 99.")
print(f"  The conditional is the matched comparison, because both it and the")
print(f"  corridor are asked one step at a time from the observed state.")
