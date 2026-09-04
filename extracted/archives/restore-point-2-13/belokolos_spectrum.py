#!/usr/bin/env python3
"""belokolos_spectrum.py — GAP 1's test.

His first-order semiclassical spectrum for the Tietz potential (SIGMA 13, 038):

    R    = (9/2Z)^(1/3)
    eta  = 2ZR / (l + 1/2)^2
    M    = n + l
    E    = -8 ( sqrt(2ZR) - M ) (l + 1/2) / ( (3 eta^2 - 8 eta) R^2 )

Rank the admissible subshells by E at each Z -- most bound first -- and compare
that ordering with (a) the observed entrant and (b) ours, nu = n - a*sqrt(p).

WHAT THE COMPARISON DECIDES. If his ordering and ours agree, nu is a
reparametrisation of his spectrum and inherits his derivation, which is the
answer to the guessed-form objection this work cannot otherwise give. If they
disagree, the disagreement locates what nu adds or loses -- and the prediction
from register 1453 is that they should agree where q = 0 and part where q != 0,
because his is a one-electron mean field and cannot carry the occupancy.

The formula is first order in the scaled energy and is stated by its author to
hold in a narrow band starting a few eV below threshold. Applying it as a global
ranking is USING IT OUTSIDE ITS STATED DOMAIN, and any disagreement found may be
that rather than a fact about nu. Declared here rather than discovered later.
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


def E_bel(n, l, Z):
    R = (9 / (2 * Z)) ** (1 / 3)
    h = 2 * Z * R / (l + 0.5) ** 2
    # HIS OWN admissibility condition: the turning points x± are real only for
    # eta > 4. Below it the level does not exist and the first-order formula is
    # meaningless. Without this filter the ranking picks 5g everywhere, which is
    # a domain violation and not a disagreement.
    if h <= 4:
        return None
    den = (3 * h * h - 8 * h) * R * R
    if abs(den) < 1e-15:
        return None
    return -8 * (math.sqrt(2 * Z * R) - (n + l)) * (l + 0.5) / den


def pick_bel(prev, Z):
    s = [(E_bel(n, l, Z), n, l) for n, l in cands(prev)]
    s = [t for t in s if t[0] is not None]
    return min(s)[1:] if s else None


def pick_nu(prev, a):
    s = [(n - a * math.sqrt((n - l - 1) + prev.get((n, l), 0) / cap(l)), n, l)
         for n, l in cands(prev)]
    b = min(x[0] for x in s)
    t = [(n, l) for v, n, l in s if v - b < EPS]
    return max(t, key=lambda x: x[0])


def a_track():
    a, lo, hi, out = None, -1e9, 1e9, {}
    for Z in STEPS:
        Lo, Up = IV[Z][4], IV[Z][5]
        nlo, nhi = max(lo, Lo), min(hi, Up)
        if nlo >= nhi or a is None:
            lo, hi = Lo, Up
        else:
            lo, hi = nlo, nhi
        w = lo if (lo > EPS and lo < 1e8) else (hi if hi < 1e8 else None)
        a = w if w is not None else (a if a is not None else 1.0)
        out[Z] = a
    return out


A = a_track()
hb = hn = agree = 0
disagree, bel_miss = [], []
for Z in STEPS:
    prev = occ(Z - 1)
    b = pick_bel(prev, Z)
    u = pick_nu(prev, A[Z])
    o = OBS[Z]
    hb += b == o
    hn += u == o
    if b == u:
        agree += 1
    else:
        q = prev.get(o, 0)
        disagree.append((Z, o, b, u, q))
    if b != o:
        bel_miss.append(Z)

n = len(STEPS)
print(f"  BELOKOLOS'S SPECTRUM AS AN ORDERING, {n} steps\n")
print(f"    his ranking matches the observed entrant : {hb} of {n}")
print(f"    ours (nu, corridor-placed a)             : {hn} of {n}")
print(f"    the two rankings AGREE WITH EACH OTHER   : {agree} of {n}")
print(f"\n    Madelung null, conditional: 96 of {n}\n")

if disagree:
    print(f"  WHERE THEY PART ({len(disagree)}), with the target's occupancy q before the step\n")
    print(f"    {'':4}{'Z':>4}{'observed':>10}{'his':>7}{'ours':>7}{'q':>4}")
    for Z, o, b, u, q in disagree[:28]:
        print(f"    {SYM[Z-1]:<4}{Z:>4}{f'{o[0]}{L[o[1]]}':>10}"
              f"{f'{b[0]}{L[b[1]]}':>7}{f'{u[0]}{L[u[1]]}':>7}{q:>4}")
    z0 = sum(1 for *_, q in disagree if q == 0)
    print(f"\n    of the {len(disagree)} disagreements, {z0} have q = 0 and "
          f"{len(disagree)-z0} have q > 0")
    print(f"    R 1453 predicted agreement at q = 0 and parting at q > 0.")
