#!/usr/bin/env python3
"""group_rule.py — the placement rule that comes out of register 1453.

    a = the MINIMUM intra-group crossing among the Pauli-admissible members
        of the current Madelung group,  crossing = (√p_A + √p_B)/2

Three layers, from the join: Belokolos supplies the group (E = E(n_r+2ℓ), all
members degenerate at E = 0); Pauli removes members as they fill; a orders what
survives, and sits on the binding ceiling.

WHAT MAKES THIS DIFFERENT FROM THE FIVE RULES THAT FAILED TONIGHT. It reads only
node counts, capacities and the current configuration -- no corridor built from
the observed entrant, no value carried across species, no self-consistency test
that cannot fail. And it comes from a derivation rather than from guessing.

WHAT IT STILL RISKS. Knowing WHICH group is current is close to knowing the
answer. Two ways of deciding it are tried and reported separately:

    strict   the current group is the lowest M with an admissible member --
             which IS Madelung's first rule, so this variant assumes half the
             thing being tested and its score means only that the second half
             works. Reported, and labelled.

    carried  the group is whichever the previous step's entrant belonged to,
             advancing only when that group has no admissible member left.
             This assumes only the starting group.

Scored out of sample against Madelung's 96 of 106 conditional.
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
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga "
       "Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd "
       "Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac "
       "Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf").split()
SUBS = [(n, l) for n in range(1, 9) for l in range(min(n, 5))]
pn = lambda s: s[0] - s[1] - 1
Mof = lambda s: s[0] + s[1]


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


def open_in(M, prev):
    return [s for s in SUBS if Mof(s) == M and prev.get(s, 0) < cap(s[1])]


def ceiling(M, prev):
    o = open_in(M, prev)
    cs = [(math.sqrt(pn(A)) + math.sqrt(pn(B))) / 2
          for A, B in itertools.combinations(o, 2)]
    return min(cs) if cs else None


def run(mode, a0=1.0):
    a, cur, hits, miss = a0, None, 0, []
    for Z in STEPS:
        prev = occ(Z - 1)
        if mode == "strict":
            cur = min(Mof(s) for s in cands(prev))
        else:
            if cur is None or not open_in(cur, prev):
                cur = min(Mof(s) for s in SUBS
                          if prev.get(s, 0) < cap(s[1]) and Mof(s) >= (cur or 0)) \
                      if cur is not None else min(Mof(s) for s in cands(prev))
        c = ceiling(cur, prev)
        if c is not None:
            a = c                       # sit on the binding ceiling
        g = pick(prev, a)
        if g == OBS[Z]:
            hits += 1
        else:
            miss.append(Z)
        if mode != "strict" and g not in open_in(cur, prev):
            cur = Mof(g)                # the walk itself says the group moved
    return hits, miss


print(f"  THE GROUP RULE, OUT OF SAMPLE — {len(STEPS)} steps\n")
for mode in ("strict", "carried"):
    h, m = run(mode)
    note = " (assumes Madelung's FIRST rule — see the docstring)" if mode == "strict" else ""
    print(f"    {mode:<9} {h:>4} of {len(STEPS)}{note}")
    print(f"      misses: " + ", ".join(f"{SYM[Z-1]}{Z}" for Z in m[:22])
          + (" …" if len(m) > 22 else ""))
print(f"\n  BENCHMARKS on the same steps")
print(f"    plain Madelung, conditional, no free parameter      96")
print(f"    corridor placement, held out                        90")
print(f"    per-run / per-atom / transition, held out           90 / 0 / 54")
