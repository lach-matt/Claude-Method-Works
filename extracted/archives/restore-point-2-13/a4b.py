#!/usr/bin/env python3
"""a4b.py — the four unforced resets. Queue item A4b, from 1.6.1.

THE STATE OF THE QUESTION. Eighteen resets are recorded. Fourteen are forced by
the running intersection emptying (R 1401, reproduced exactly by balance.py).
FOUR are not: Li 3, K 19, Tl 81, Fr 87.

WHAT HAS BEEN TRIED AND FAILED.
  · R 1401 calls them "the first element of a new period". THALLIUM IS NOT ONE
    (R 1443) — period six opens at caesium.
  · "Opens a subshell" is true of all four but ALSO of eight of the fourteen
    forced (Rb, Cs, Ce, Gd, Pa, Cm, Lr, Rf), so it is necessary and not
    sufficient (R 1443).
  · R 1403's endpoint rule produces ten of the eighteen, a different ten.

SPACE, DECLARED BEFORE ANY COMPUTATION BELOW (R 1383 question 2). The admissible
set is the 106 walk steps. A candidate property is tested by asking how many of
the four it covers AND how many of the other 102 it also covers. A property
covering all four and few others separates; one covering all four and many
others is the "opens a subshell" failure repeated. The null for each is the
hypergeometric probability of covering all four by chance given its own size.
Nothing below chooses a property after seeing its rate.
"""
import sys, io, contextlib, math
from math import comb
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack
import ground as G

L = "spdfg"
cap = lambda l: 2 * (2 * l + 1)
EPS = 1e-9
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)
N = len(STEPS)
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se "
       "Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy "
       "Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf "
       "Es Fm Md No Lr Rf Db Sg Bh Hs").split()
FOUR = [3, 19, 81, 87]
FORCED = {37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104}
STARTS = [1, 3, 5, 13, 21, 39, 57, 89]
PERIOD = {1, 3, 11, 19, 37, 55, 87}
blk = lambda Z: max(i for i, s in enumerate(STARTS) if s <= Z) + 1


def occ(Z):
    if Z < 1:
        return {}
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


def facts(Z):
    _, gn, gl, gp, lo, hi, blo, bhi = IV[Z]
    prev, cur = occ(Z - 1), occ(Z)
    t = (gn, gl)
    lost = [k for k in prev if prev[k] > cur.get(k, 0)]
    return {
        "Z": Z, "t": t, "n": gn, "l": gl, "p": gp, "M": gn + gl,
        "q": cur[t] - prev.get(t, 0),
        "opens_subshell": prev.get(t, 0) == 0,
        "opens_shell": all(prev.get((gn, x), 0) == 0 for x in range(min(gn, 5))),
        "opens_block": Z in STARTS,
        "opens_period": Z in PERIOD,
        "l_is_s": gl == 0,
        "floor_finite": lo > -1e8,
        "ceiling_finite": hi < 1e8,
        "sides": int(lo > -1e8) + int(hi < 1e8),
        "has_source": bool(lost),
        "ncands": len(cands(prev)),
        "block": blk(Z),
        "prev_l": None,
    }


F = {Z: facts(Z) for Z in STEPS}
prev_entrant = None
for Z in STEPS:
    F[Z]["prev_l"] = prev_entrant[1] if prev_entrant else None
    F[Z]["l_rises"] = (prev_entrant is not None and F[Z]["l"] > prev_entrant[1])
    F[Z]["l_falls"] = (prev_entrant is not None and F[Z]["l"] < prev_entrant[1])
    prev_entrant = F[Z]["t"]

print("  THE FOUR, WITH EVERYTHING THE TREE KNOWS ABOUT THEM\n")
cols = ["t", "n", "l", "p", "M", "q", "block", "sides", "opens_subshell",
        "opens_shell", "opens_block", "opens_period", "l_falls"]
print("    " + f"{'':6}" + "".join(f"{c[:9]:>11}" for c in cols))
for Z in FOUR:
    f = F[Z]
    v = [f"{f['t'][0]}{L[f['t'][1]]}" if c == "t" else str(f[c]) for c in cols]
    print(f"    {SYM[Z-1]+str(Z):<6}" + "".join(f"{x:>11}" for x in v))

print("\n  CANDIDATE PROPERTIES, EACH SCORED ON ALL 106 STEPS\n")
PROPS = {
    "opens a subshell":            lambda f: f["opens_subshell"],
    "opens a whole SHELL (new n)": lambda f: f["opens_shell"],
    "opens a Janet block":         lambda f: f["opens_block"],
    "opens a period":              lambda f: f["opens_period"],
    "entrant is s":                lambda f: f["l_is_s"],
    "entrant is s AND opens it":   lambda f: f["l_is_s"] and f["opens_subshell"],
    "no finite floor":             lambda f: not f["floor_finite"],
    "no finite ceiling":           lambda f: not f["ceiling_finite"],
    "one-sided corridor":          lambda f: f["sides"] == 1,
    "ℓ falls from the last step":  lambda f: f["l_falls"],
    "ℓ falls to s":                lambda f: f["l_falls"] and f["l_is_s"],
    "opens shell AND ℓ falls":     lambda f: f["opens_shell"] and f["l_falls"],
}
print(f"    {'property':<30}{'covers the 4':>13}{'other steps':>13}{'P(all 4)':>11}")
res = []
for name, fn in PROPS.items():
    S = [Z for Z in STEPS if fn(F[Z])]
    k = len(set(S) & set(FOUR))
    others = len(S) - k
    p = comb(len(S), 4) / comb(N, 4) if len(S) >= 4 else 0.0
    res.append((k, others, name, S, p))
    print(f"    {name:<30}{k:>10} / 4{others:>13}{(p if k==4 else float('nan')):>11.5f}")

print("\n  THE SEPARATING PROPERTIES — all four, fewest others\n")
best = sorted([r for r in res if r[0] == 4], key=lambda r: r[1])
for k, others, name, S, p in best[:4]:
    extra = [SYM[z-1]+str(z) for z in S if z not in FOUR]
    print(f"    {name:<30} covers all four, plus {others}: {extra}")
    print(f"      P(a random {len(S)}-set covering all four) = {p:.5f}")
if not best:
    print("    NONE. No single property on this list covers all four.")
