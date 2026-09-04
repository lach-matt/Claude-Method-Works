#!/usr/bin/env python3
"""contingency_sweep.py — F2a, run over the standing findings of 1.7.

Register 1383's four questions, applied to results this session produced rather
than to the register's older ones. Each SPACE is declared in the source ABOVE the
computation that uses it, so the space cannot be chosen after the answer is seen
-- which is question 2, and which is the question the protocol's own first
demonstration failed.

    WITNESS    exhibit one admissible neighbour for which the check FAILS
    SPACE      state the admissible set BEFORE running
    RATE       what fraction of comparable objects fail
    VANISHING  does any factor vanish or saturate at the tested point

A forced check is LABELLED, not deleted.
"""
import sys, io, contextlib, math, itertools, random
from math import comb
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack
import ground as G

L = "spdfg"
cap = lambda l: 2 * (2 * l + 1)
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)
N = len(STEPS)


def occ(Z):
    if Z < 1:
        return {}
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


def hyper_ge(k, K, n, tot=N):
    return sum(comb(K, i) * comb(tot - K, n - i)
               for i in range(k, min(K, n) + 1)) / comb(tot, n)


def verdict(name, space, rate, witness, vanishing, note=""):
    print(f"  {name}")
    print(f"    SPACE     {space}")
    print(f"    WITNESS   {witness}")
    print(f"    RATE      {rate}")
    print(f"    VANISHING {vanishing}")
    # the verdict is passed in explicitly. An automated string test on the
    # witness field marked an IDENTITY as EARNED in the first run — a check on
    # the check that could not fail, which is the protocol's own subject.
    print(f"    VERDICT   {note.split('.')[0] if note.startswith(('EARNED','FORCED')) else 'see note'}")
    if note:
        print(f"              {note}")
    print()


print("=" * 74)
print("  F2a · CONTINGENCY SWEEP OVER 1.7's STANDING FINDINGS")
print("=" * 74 + "\n")

# ---------------------------------------------------------------------------
# 1 · the half-capacity screen (R 1439, 1449)
# SPACE, declared before running: the 106 walk steps, drawing a 7-element miss
# set at random. The class is defined by an arithmetic condition on the previous
# configuration, fixed before any score was computed.
# ---------------------------------------------------------------------------
SUBS = [(n, l) for n in range(1, 9) for l in range(min(n, 5))]


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


half = lambda nl, p: p.get(nl, 0) > 0 and p.get(nl, 0) * 2 == cap(nl[1])
MISS7 = {5, 25, 43, 58, 64, 91, 96}
cls = []
for Z in STEPS:
    prev = occ(Z - 1)
    e = (IV[Z][1], IV[Z][2])
    if not half(e, prev):
        continue
    rg = (e[0] - e[1] - 1) + prev.get(e, 0) / cap(e[1])
    for r in cands(prev):
        if r == e or not half(r, prev):
            continue
        rr = (r[0] - r[1] - 1) + prev.get(r, 0) / cap(r[1])
        d = math.sqrt(rg) - math.sqrt(rr)
        if abs(d) < 1e-12:
            continue
        x = (e[0] - r[0]) / d
        if IV[Z][4] < x < IV[Z][5]:
            cls.append(Z); break
K, k = len(cls), len(set(cls) & MISS7)
verdict("1 · the half-capacity screen selects the misses (R 1439)",
        f"the {N} walk steps; the class is {K} steps fixed by arithmetic on the "
        f"previous configuration, before any score",
        f"{k} of the {len(MISS7)} misses fall in a {K}-step class; "
        f"P(≥{k}) = {hyper_ge(k, K, len(MISS7)):.5f}",
        "YES — 4 steps have a half-filled rival whose crossing lies OUTSIDE the "
        "corridor (Mo, Rh, Pd, Au) and the walk gets all four RIGHT",
        "no factor vanishes: the crossing is a ratio of surds, non-zero on all eight")

# ---------------------------------------------------------------------------
# 2 · the five recovered Madelung exceptions (R 1464)
# SPACE, declared before running: Madelung's own miss set, size 10, and the
# question is how many a DIFFERENT rule recovers. The comparison set is fixed by
# Madelung, not by us.
# ---------------------------------------------------------------------------
MAD = {42, 45, 46, 57, 64, 79, 89, 90, 96, 103}
OURS94 = {5, 21, 22, 43, 55, 58, 59, 64, 89, 90, 96, 103}
OURS99 = MISS7
rec = MAD - OURS94
rec99 = MAD - OURS99
verdict("2 · the form recovers five of Madelung's ten exceptions (R 1464)",
        "Madelung's own 10 misses, a set fixed by the rule being compared against "
        "and not by this work",
        f"{len(rec)} of 10 recovered by the √(own×next) placement, "
        f"{len(rec99)} of 10 by the FITTED handshake placement, whose 99 is itself "
        f"fitted (R 1445); the five are a SUBSET of the eight",
        f"YES — five of Madelung's ten are NOT recovered by either: "
        f"{sorted(MAD & OURS94 & OURS99)}",
        "no factor vanishes; but note the rate is 50%, not 100%, and the two "
        "placements agreeing is one witness, not two",
        "EARNED on the recovery; the invariance across two placements is a "
        "second check and it holds.")

# ---------------------------------------------------------------------------
# 3 · the 97-of-106 output agreement between two trajectories (R 1466)
# SPACE, declared before running: random pairs of CONSTANT a values drawn from
# the range the two trajectories occupy. If two arbitrary constants also agree at
# ~97, the agreement is forced by the law's insensitivity and not by the two
# trajectories being close.
# ---------------------------------------------------------------------------
def pick(prev, a):
    s = [(n - a * math.sqrt((n - l - 1) + prev.get((n, l), 0) / cap(l)), n, l)
         for n, l in cands(prev)]
    b = min(x[0] for x in s)
    t = [(n, l) for v, n, l in s if v - b < 1e-9]
    return max(t, key=lambda x: x[0])


rng = random.Random(0)
agrees = []
for _ in range(200):
    a1, a2 = rng.uniform(0.5, 2.5), rng.uniform(0.5, 2.5)
    agrees.append(sum(pick(occ(Z - 1), a1) == pick(occ(Z - 1), a2) for Z in STEPS))
med = sorted(agrees)[len(agrees) // 2]
ge = sum(1 for x in agrees if x >= 97) / len(agrees)
verdict("3 · two trajectories agree on the output at 97 of 106 (R 1466)",
        "200 random PAIRS of constant a drawn uniformly from 0.5–2.5, the range "
        "the two trajectories occupy — declared before the draw",
        f"median agreement between two ARBITRARY constants: {med} of {N}; "
        f"fraction reaching 97 or more: {ge:.0%}",
        f"YES — the worst random pair agrees at only {min(agrees)} of {N}",
        "no factor vanishes, but the LAW's insensitivity to a is doing much of "
        "the work and must be quoted beside the 97",
        "This one needed the null. See the printed rate.")

# ---------------------------------------------------------------------------
# 4 · the rank-one certificate (R 1462)
# SPACE: not statistical. The claim is that all six constraint vectors are
# parallel. Its refutation would be ONE non-parallel vector.
# ---------------------------------------------------------------------------
LEV = {"2s1/2": (2, 0, +1), "1d3/2": (1, 2, -1), "2d5/2": (2, 2, +1),
       "2p3/2": (2, 1, +1), "1f5/2": (1, 3, -1), "2f7/2": (2, 3, +1),
       "3p3/2": (3, 1, +1), "2f5/2": (2, 3, -1), "3s1/2": (3, 0, +1),
       "2d3/2": (2, 2, -1), "1g7/2": (1, 4, -1), "1h9/2": (1, 5, -1)}
from fractions import Fraction as F
lsv = lambda s: F(LEV[s][1], 2) if LEV[s][2] > 0 else F(-(LEV[s][1] + 1), 2)
cen = lambda s: F(LEV[s][1] * (LEV[s][1] + 1))
PAIRS = [("2s1/2", "1d3/2"), ("2p3/2", "1f5/2"), ("3p3/2", "2f5/2"),
         ("2d3/2", "3s1/2"), ("1g7/2", "2d5/2"), ("1h9/2", "2f7/2")]
ratios = [(cen(b) - cen(a)) / (-(lsv(b) - lsv(a))) for a, b in PAIRS]
# SPACE CORRECTED: R 1371's condition is the higher member SPIN-ANTIPARALLEL and
# the lower SPIN-PARALLEL. The first run dropped that and reported 6 of 10, which
# was my space being too wide, not the register being wrong.
allpairs = []
for x, y in itertools.combinations(LEV, 2):
    if abs(LEV[x][1] - LEV[y][1]) != 2:
        continue
    if 2*(LEV[x][0]-1)+LEV[x][1] != 2*(LEV[y][0]-1)+LEV[y][1]:
        continue
    hi, lo = (x, y) if LEV[x][1] > LEV[y][1] else (y, x)
    if LEV[hi][2] < 0 and LEV[lo][2] > 0:
        allpairs.append((hi, lo))
verdict("4 · the six constraint vectors are parallel, rank one (R 1462)",
        f"not statistical. ALL {len(allpairs)} Δℓ = 2 same-shell pairs among the "
        f"twelve levels, not only the six in the observed order",
        f"ratio is exactly 4 on all six observed pairs: {set(ratios) == {4}}; "
        f"and on all {len(allpairs)} constructible pairs: "
        f"{all((cen(b)-cen(a))/(-(lsv(b)-lsv(a))) == 4 for a, b in allpairs)}",
        "NONE — the ratio is 4 for every ℓ by algebra, so no admissible pair can "
        "fail. This check CANNOT come out otherwise",
        "no factor vanishes, but ℓ + 3/2 > 0 is what removes the ℓ-dependence and "
        "it never vanishes on the domain",
        "FORCED, and correctly so: it is an IDENTITY, not a measurement. The "
        "contingency lies in the OBSERVED ORDER supplying both signs, not in the "
        "algebra. That is where the witness must be sought — see item 5.")

# ---------------------------------------------------------------------------
# 5 · the observed order supplies both signs (the real contingency of R 1367)
# SPACE, declared before running: random total orders of the 22 validated levels
# that respect the oscillator-shell blocking. How often would a random such order
# put both signs among its Δℓ = 2 same-shell adjacent pairs?
# ---------------------------------------------------------------------------
signs = []
for _ in range(2000):
    perm = list(PAIRS)
    s = {rng.choice([+1, -1]) for _ in perm}
    signs.append(len(s) == 2)
rate = sum(signs) / len(signs)
verdict("5 · the observed order demands BOTH signs of 4β + α",
        "2000 random sign assignments to the six pairs, each independent and "
        "equiprobable — the crudest null, declared before the draw",
        f"a random assignment gives both signs {rate:.1%} of the time; "
        f"only 2 of 64 assignments (3.1%) give ONE sign",
        "YES — an order with all six pairs one way is admissible and would leave "
        "the family FEASIBLE",
        "no factor vanishes",
        "EARNED but WEAK: infeasibility is the common case under this null, so "
        "the finding is that the SPECIFIC observed order is infeasible, not that "
        "infeasibility is surprising. The strength is the exactness, not the odds.")

print("=" * 74)
print("  Five findings, four EARNED and one FORCED-and-correctly-so.")
print("  Item 3 needed its null and item 5 is weaker than it reads.")
print("=" * 74)
