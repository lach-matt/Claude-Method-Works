#!/usr/bin/env python3
"""rival_pull.py — REBUILT from register 1406. Pauli chooses the rival, the cap
sets its pull.

The ceiling is  U = dn / ( sqrt(r_r) - sqrt(r_g) ),  where a radicand is the node
count plus the occupancy over the cap, r = p + q/2(2l+1). The rival's occupancy
enters ONLY through its own radicand, so every electron in the rival grows the
gap and lowers the ceiling. Differentiating:

    dU/dq_r  =  - dn / ( 2 * cap(l_r) * sqrt(r_r) * GAP^2 ),   GAP = sqrt(r_r) - sqrt(r_g)

Two things sit in that denominator and each says something.

  THE CAP -- 2, 6, 10, 14 -- so the pull scales as 1/cap and an s rival's single
  electron moves the ceiling most. That is the algebra of a charge of two: an s
  shell divides by two, so each electron carries the largest share.

  THE GAP, SQUARED -- an inverse-square in the separation between the radicands,
  so the pull grows as the two approach. THE SHAPE IS A FACT ABOUT THIS ALGEBRA;
  identifying it with the Coulomb law is a FURTHER claim and is not tested here,
  since the radicands are node counts and not distances (R 1444).

The 4d row is the worked case: 5s at two is inadmissible by Pauli so 5p binds;
5s at one is admissible and binds instead, contracting the ceiling at molybdenum
and rhodium while palladium's rises. No fitted parameter -- cap, node count and
occupancy are all counts.
"""
import sys, io, contextlib, math
sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack
import ground as G

L = "spdfg"
cap = lambda l: 2 * (2 * l + 1)
IV = {r[0]: r for r in brack.IV}
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga "
       "Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd "
       "Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac "
       "Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs").split()


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


rad = lambda nl, o: (nl[0] - nl[1] - 1) + o.get(nl, 0) / cap(nl[1])


def ceiling_and_rival(Z):
    """the binding upper rival and the ceiling it sets"""
    _, gn, gl, gp, lo, hi, blo, bhi = IV[Z]
    prev = occ(Z - 1)
    g = (gn, gl)
    rg = rad(g, prev)
    best = None
    for c in cands(prev):
        if c == g:
            continue
        rr = rad(c, prev)
        gap = math.sqrt(rr) - math.sqrt(rg)
        if gap <= 1e-12:
            continue
        U = (c[0] - gn) / gap
        if best is None or U < best[0]:
            best = (U, c, rr, gap)
    return g, rg, best


def sensitivity(dn, lr, rr, gap):
    return -dn / (2 * cap(lr) * math.sqrt(rr) * gap * gap)


print("  THE PULL SCALES AS 1/cap — an s rival's single electron moves most\n")
print(f"    {'ℓ':>2}{'cap':>5}{'1/cap':>9}")
for l in range(4):
    print(f"    {L[l]:>2}{cap(l):>5}{1/cap(l):>9.4f}")

print("\n  THE 4d ROW, WHERE PAULI SWITCHES THE BINDING RIVAL (R 1406)\n")
print(f"    {'':4}{'Z':>4}{'entrant':>9}{'rival':>8}{'5s occ':>8}{'ceiling':>10}{'Δ ceiling':>11}")
prevU = None
for Z in range(39, 49):
    if Z not in IV:
        continue
    g, rg, best = ceiling_and_rival(Z)
    if best is None:
        continue
    U, riv, rr, gap = best
    o5s = occ(Z - 1).get((5, 0), 0)
    d = "" if prevU is None else f"{U-prevU:+11.3f}"
    print(f"    {SYM[Z-1]:<4}{Z:>4}{f'{g[0]}{L[g[1]]}':>9}{f'{riv[0]}{L[riv[1]]}':>8}"
          f"{o5s:>8}{U:>10.3f}{d:>11}")
    prevU = U
print("\n    R 1406: the ceiling contracts by 0.505 at molybdenum and 0.748 at")
print("    rhodium while palladium's RISES by 0.059 — the two that contract")
print("    reset, the one that does not, does not.")

print("\n  SENSITIVITY OF THE CEILING TO ONE MORE ELECTRON IN THE RIVAL\n")
print(f"    {'':4}{'Z':>4}{'rival':>8}{'cap':>5}{'gap':>9}{'dU/dq':>12}")
for Z in (42, 43, 45, 46, 24, 29, 64, 96):
    if Z not in IV:
        continue
    g, rg, best = ceiling_and_rival(Z)
    if best is None:
        continue
    U, riv, rr, gap = best
    s = sensitivity(riv[0] - g[0], riv[1], rr, gap)
    print(f"    {SYM[Z-1]:<4}{Z:>4}{f'{riv[0]}{L[riv[1]]}':>8}{cap(riv[1]):>5}"
          f"{gap:>9.4f}{s:>12.4f}")
print("\n    Monotone in 1/cap and in 1/gap² by construction; both are counts,")
print("    and no parameter is fitted anywhere above.")
