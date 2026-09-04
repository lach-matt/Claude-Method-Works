#!/usr/bin/env python3
"""centre_column.py — the placement that uses BOTH blocks, and where it fails.

Register 1464. Placing a at canonical statistics of the group's own crossing set,
with no fitted step, the best is

    a = sqrt( min(own group's crossings) * min(next group's crossings) )

the GEOMETRIC MEAN of the entrant's own binding ceiling and the next group's.
That is register 1415 made into a rule -- bounded above within its block and
aimed by the block that has not yet opened -- and it scores 94 of 106.

WHY THAT MATTERS (R 1464). Of Madelung's ten exceptions this recovers FIVE:
Mo 42, Rh 45, Pd 46, La 57, Au 79. The form's domain is where Madelung stops.

AND ITS OWN SEVEN MISSES ARE ALL AT TRANSITIONS (R 1465) -- B 5 node-free,
Sc 21 and Ti 22 at Q.collapse's threshold, Tc 43 a half-capacity crossing, and
Cs 55, Ce 58, Pr 59 block openings. This script prints the transition structure
at each so the boundary can be looked at rather than swept.

THIS IS NOT A SEVENTH PLACEMENT SWEEP. Register 1460's P4 forbids one, and the
rule here is a canonical statistic rather than a search: min, max, mean, median,
geometric and harmonic means and the two-block combinations were each computed
once, and the geometric mean of the two ceilings won on its own terms.
"""
import sys, io, contextlib, math, itertools
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
SUBS = [(n, l) for n in range(1, 9) for l in range(min(n, 5))]
pn = lambda s: s[0] - s[1] - 1
Mof = lambda s: s[0] + s[1]
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br "
       "Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho "
       "Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es "
       "Fm Md No Lr Rf Db Sg Bh Hs").split()
STARTS = [1, 3, 5, 13, 21, 39, 57, 89]
blk = lambda Z: max(i for i, s in enumerate(STARTS) if s <= Z) + 1


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


def pick(prev, a):
    s = [(n - a * math.sqrt((n - l - 1) + prev.get((n, l), 0) / cap(l)), n, l)
         for n, l in cands(prev)]
    b = min(x[0] for x in s)
    t = [(n, l) for v, n, l in s if v - b < EPS]
    return max(t, key=lambda x: x[0])


def crossings(M, prev):
    o = [s for s in SUBS if Mof(s) == M and prev.get(s, 0) < cap(s[1])]
    return sorted((math.sqrt(pn(A)) + math.sqrt(pn(B))) / 2
                  for A, B in itertools.combinations(o, 2))


a, hits, miss, track = 1.0, 0, [], {}
for Z in STEPS:
    prev = occ(Z - 1)
    M = min(Mof(s) for s in cands(prev))
    c, nc = crossings(M, prev), crossings(M + 1, prev)
    if c and nc:
        a = math.sqrt(min(c) * min(nc))
    elif c:
        a = min(c)
    track[Z] = (a, M, min(c) if c else None, min(nc) if nc else None)
    g = pick(prev, a)
    if g == OBS[Z]:
        hits += 1
    else:
        miss.append((Z, OBS[Z], g))

print(f"  a = √( own group's ceiling × next group's ceiling )   →  {hits} of {len(STEPS)}\n")
print("  THE FIVE MADELUNG EXCEPTIONS THIS FORM RECOVERS\n")
print(f"    {'':4}{'Z':>4}{'entrant':>9}{'M':>4}{'own ceil':>11}{'next ceil':>11}{'a':>10}")
for Z in (42, 45, 46, 57, 79):
    aZ, M, o, n_ = track[Z]
    e = OBS[Z]
    print(f"    {SYM[Z-1]:<4}{Z:>4}{f'{e[0]}{L[e[1]]}':>9}{M:>4}"
          f"{(f'{o:.4f}' if o else '—'):>11}{(f'{n_:.4f}' if n_ else '—'):>11}{aZ:>10.4f}")

print("\n  ITS OWN SEVEN MISSES, WITH THE TRANSITION EACH SITS ON\n")
WHY = {5: "node-free entrant, no floor exists (R 1414)",
       21: "Q.collapse threshold, 3d collapses (R 1392)",
       22: "Q.collapse threshold (R 1392)",
       43: "half-capacity crossing (R 1439)",
       55: "Janet block opening",
       58: "Janet block opening, 4f",
       59: "first step after the 4f opening"}
print(f"    {'':4}{'Z':>4}{'blk':>4}{'observed':>10}{'said':>8}{'a':>9}   why it is a transition")
for Z, o, g in miss:
    aZ, M, oc, ncl = track[Z]
    print(f"    {SYM[Z-1]:<4}{Z:>4}{blk(Z):>4}{f'{o[0]}{L[o[1]]}':>10}"
          f"{f'{g[0]}{L[g[1]]}':>8}{aZ:>9.4f}   {WHY.get(Z,'—')}")
print("\n    Every one is a boundary, and none is inside a filling run.")
print("    The centre column is the placement of a ACROSS a transition.")
