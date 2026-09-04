#!/usr/bin/env python3
"""per_run.py — one a per subshell-filling run, placed WITHOUT observation.

The unit is the filling run, not the Janet block: within a run the corridors
intersect in 31 of 31 cases, because while q walks 0 -> cap the entrant's
radicand steps by 1/cap and its rivals sit still. Blocks 5 to 8 have empty
intersections and cannot serve as the unit.

THE QUESTION THIS ASKS. A run's corridor is computable from node counts and
capacities alone. But knowing WHICH subshell is filling is itself an observation
unless the walk generates it. So the honest test is a closed loop:

    at each step, with the held a, the law names an entrant;
    if that entrant differs from the one currently filling, a RUN BOUNDARY is
    declared and a is re-placed on the NEW run's corridor -- which is computed
    from the law's own choice, not from the record;
    the step is then scored against the record it never saw.

Nothing here reads the observed entrant before predicting. The record is used
only to score afterwards. Contrast the in-sample scorer, which placed a on a
corridor brack.py had built FROM the observed entrant at that same step.

FOUR PLACEMENTS ARE TRIED inside each run's own window, because R 1402 says the
count is rule-dependent and R 1440 measured a seven-step spread across placements
on identical constraints. Reporting one would be choosing.
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


def nu(n, l, prev, a):
    return n - a * math.sqrt((n - l - 1) + prev.get((n, l), 0) / cap(l))


def pick(prev, a):
    s = [(nu(n, l, prev, a), n, l) for n, l in cands(prev)]
    b = min(x[0] for x in s)
    t = [(n, l) for v, n, l in s if v - b < EPS]
    return max(t, key=lambda x: x[0])


def corridor_for(prev, entrant):
    """The window of a making `entrant` the least-nu choice. Node counts and
    capacities only — no observation of what was actually entered."""
    gn, gl = entrant
    rg = (gn - gl - 1) + prev.get(entrant, 0) / cap(gl)
    lo, hi = -1e9, 1e9
    for n, l in cands(prev):
        if (n, l) == entrant:
            continue
        r = (n - l - 1) + prev.get((n, l), 0) / cap(l)
        d = math.sqrt(r) - math.sqrt(rg)
        if abs(d) < 1e-12:
            continue
        x = (n - gn) / d
        if d > 0:
            hi = min(hi, x)
        else:
            lo = max(lo, x)
    return lo, hi


def place(lo, hi, how, a_prev):
    fl, fu = lo > EPS and lo < 1e8, hi < 1e8
    if how == "floor":
        w = lo if fl else (hi if fu else None)
    elif how == "ceiling":
        w = hi if fu else (lo if fl else None)
    elif how == "midpoint":
        w = (lo + hi) / 2 if (fl and fu) else (lo if fl else (hi if fu else None))
    else:                                    # "hold" — move only if forced out
        if a_prev is not None and lo < a_prev < hi:
            return a_prev
        w = lo if fl else (hi if fu else None)
    return w if w is not None else (a_prev if a_prev is not None else 1.0)


def run_walk(how, a0=1.0):
    a, filling, hits, misses, boundaries = None, None, 0, [], []
    for Z in STEPS:
        prev = occ(Z - 1)
        # --- predict, using only a and the previous configuration -----------
        if a is None:
            a = a0
        guess = pick(prev, a)
        # --- has the run changed under the law's OWN choice? ----------------
        if guess != filling:
            lo, hi = corridor_for(prev, guess)      # the NEW run's own window
            a = place(lo, hi, how, a)
            guess = pick(prev, a)                   # re-read at the placed a
            if guess != filling:
                filling = guess
                boundaries.append(Z)
        # --- score against the record, which was never consulted above ------
        if guess == OBS[Z]:
            hits += 1
        else:
            misses.append(Z)
    return hits, misses, boundaries


print(f"  PER-RUN PLACEMENT, OUT OF SAMPLE — the record is used only to score\n")
print(f"    {'placement':<12}{'score':>12}{'run boundaries':>17}")
best = None
for how in ("floor", "midpoint", "ceiling", "hold"):
    h, m, b = run_walk(how)
    print(f"    {how:<12}{h:>6} / {len(STEPS)}{len(b):>17}")
    if best is None or h > best[0]:
        best = (h, m, b, how)

h, m, b, how = best
print(f"\n  BEST: {how} — {h} of {len(STEPS)}")
print(f"    misses: " + ", ".join(f"{SYM[Z-1]}{Z}" for Z in m))
print(f"\n  BENCHMARKS, all on the same 106 steps")
print(f"    plain Madelung, conditional, no free parameter   96")
print(f"    per-step placement using each step's OWN corridor (in-sample) 99")
print(f"    per-step placement, held out                      90")
print(f"    per-run placement, held out                       {h}")
