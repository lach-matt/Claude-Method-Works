#!/usr/bin/env python3
"""scorer.py — the walk, end to end, with nothing fitted.

REBUILT from register 1413 and the specification recovered from the 1.6.1
transcript. The original was lost; this is a reconstruction and every figure it
prints is RECOMPUTED, not reproduced. See PROVENANCE.md.

    nu(n, l) = n - a * sqrt( (n - l - 1) + q / (2(2l+1)) )

with q the subshell's occupancy BEFORE the step, so the second term is the Pauli
fraction. The incoming electron takes the admissible subshell of least nu.

CANDIDATES are generated exactly as brack.py does: for each l, walk n upward,
skip any subshell already at capacity, and stop after the first empty one. A full
subshell has nowhere to put an electron, so it cannot be a rival in anyone's
bracket -- including its own (R 1397).

THE TIE-BREAK is the whole of the s-block question. At a = L the entrant and its
binding rival are exactly degenerate -- at potassium both 4s and 3d score 3.000000
-- so the corridor's endpoint IS a crossing and a is placed on it. The rule is to
take the HIGHER n, the larger and more diffuse orbital. That is the Madelung
preference appearing as the resolution of an exact degeneracy rather than as a
rule imposed on top; taking the lower n instead should cost about eight steps.

TWO PLACEMENT RULES, both of which must be run because R 1413 scores them
differently and the difference is the point:

  HANDSHAKE (R 1403)  a takes the tightest finite non-zero bound -- L where it
                      exists as a real surd, U where it does not -- and moves
                      only when the held a leaves the corridor. Ten moves.

  PER-BLOCK ASCENT    at a Janet block opening a takes the block's own floor;
  (R 1409)            inside a block a takes max(itself, floor), so it only ever
                      rises. Fifteen moves, and it re-places at openings where
                      nothing requires it.

EXPECTED, from R 1413: handshake 99 of 106, missing Mn 25, Tc 43, Ce 58, Gd 64,
Pa 91, Cm 96, Rf 104. Per-block ascent 97, those seven plus B 5 and Sc 21.
Lower-n tie-break 91.
"""
import sys, io, contextlib, math
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
EPS = 1e-9

LENGTHS = [2, 2, 8, 8, 18, 18, 32, 32]
STARTS, _z = [], 1
for _n in LENGTHS:
    STARTS.append(_z); _z += _n
OPENS = set(STARTS)


def occ(Z):
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


def candidates(prev):
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
    q = prev.get((n, l), 0)
    return n - a * math.sqrt((n - l - 1) + q / cap(l))


def choose(cands, prev, a, higher_n=True):
    scored = [(nu(n, l, prev, a), n, l) for n, l in cands]
    best = min(s for s, _, _ in scored)
    tied = [(n, l) for s, n, l in scored if s - best < EPS]
    return max(tied, key=lambda t: t[0]) if higher_n else min(tied, key=lambda t: t[0])


# corridor per element, from brack.py's exact intervals
IVL = {r[0]: (r[4], r[5]) for r in brack.IV}
OBS = {r[0]: (r[1], r[2]) for r in brack.IV}
STEPS = sorted(IVL)


def run(placement, higher_n=True, a0=1.0):
    """a is placed on the RUNNING INTERSECTION, not on the current element's own
    corridor. That is the structure that reproduces R 1401's fourteen forced
    moves exactly (balance.py); placing against each element separately makes a
    leave its bracket constantly and is not what the record describes."""
    a, moves, hits, misses = None, [], 0, []
    lo, hi = -1e9, 1e9
    for Z in STEPS:
        Lo, Up = IVL[Z]

        if placement == "handshake":
            nlo, nhi = max(lo, Lo), min(hi, Up)
            if nlo >= nhi or a is None:                  # the intersection empties
                lo, hi = Lo, Up
            else:
                lo, hi = nlo, nhi
        else:                                            # per-block ascent
            # R 1409 exactly: at a block opening a takes the block's OWN floor;
            # inside a block a takes max(itself, floor). Floors only — no
            # ceiling is intersected, so a only ever rises within a block.
            if Z in OPENS or a is None:
                lo, hi = Lo, Up
            else:
                lo, hi = max(lo, Lo), 1e9

        # the tightest finite non-zero bound: L where it is a real surd, U where
        # it is not. Lithium's window is (0, +inf) and determines nothing, so a0
        # is declared arbitrary there and its effect is measured below.
        want = lo if (lo > EPS and lo < 1e8) else (hi if hi < 1e8 else None)
        newa = want if want is not None else (a if a is not None else a0)
        if a is None or abs(newa - a) > EPS:
            moves.append(Z)
        a = newa

        prev = occ(Z - 1)
        pick = choose(candidates(prev), prev, a, higher_n)
        if pick == OBS[Z]:
            hits += 1
        else:
            misses.append((Z, OBS[Z], pick))
    return hits, moves, misses


print(f"  scored over {len(STEPS)} steps, Z = {min(STEPS)} to {max(STEPS)}\n")
print(f"    {'placement':<22}{'tie-break':<12}{'score':>10}{'moves':>8}")
results = {}
for pl in ("handshake", "per-block ascent"):
    for hi in (True, False):
        h, m, ms = run(pl, hi)
        results[(pl, hi)] = (h, m, ms)
        print(f"    {pl:<22}{'higher n' if hi else 'lower n':<12}"
              f"{h:>6} / {len(STEPS)}{len(m):>8}")

print("\n  EXPECTED from R 1413: handshake 99 with 10 moves, per-block 97 with 15,")
print("                        lower-n tie-break 91.\n")

for pl in ("handshake", "per-block ascent"):
    h, m, ms = results[(pl, True)]
    print(f"  {pl.upper()} — {h} of {len(STEPS)}, {len(m)} moves")
    print("    misses: " + ", ".join(
        f"{SYM[Z-1]}{Z} (obs {o[0]}{L[o[1]]}, said {p[0]}{L[p[1]]})" for Z, o, p in ms))
    print()

exp7 = {25, 43, 58, 64, 91, 96, 104}
got_h = {Z for Z, _, _ in results[("handshake", True)][2]}
got_b = {Z for Z, _, _ in results[("per-block ascent", True)][2]}
print(f"  R 1413's seven                 : {sorted(exp7)}")
print(f"  handshake misses here          : {sorted(got_h)}   match: {got_h == exp7}")
print(f"  per-block adds B 5 and Sc 21?  : {sorted(got_b - got_h)}")
print("\n  NOTE: a REBUILD. Where this disagrees with R 1413, neither is")
print("        privileged until the disagreement is examined.")

print("\n  IS THE ARBITRARY INITIALISATION IMMATERIAL?")
for a0 in (0.05, 0.2, 0.5, 1.0, 2.0, 5.0):
    print(f"    a0 = {a0:<5} handshake {run('handshake', True, a0)[0]} / {len(STEPS)}"
          f"   per-block {run('per-block ascent', True, a0)[0]} / {len(STEPS)}")
