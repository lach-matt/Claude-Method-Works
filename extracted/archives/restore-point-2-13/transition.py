#!/usr/bin/env python3
"""transition.py — the walk with the cell read as a MOVE rather than a target.

Register 1420: Λ's cell is a transition — a source triple, a target triple, and a
count between them — and the walk's cell carries only the target, because the
bracket construction asks solely which subshell was GAINED. So the machinery has
never attempted to predict the twelve donor steps at all; it predicts the target
and is silent on whether anything departs.

THE EXTENSION TESTED HERE, stated plainly as an extension and not a derivation:

    1. the arriving electron takes the admissible subshell of least nu, as now
    2. THEN, with that arrival in place, an electron RELOCATES from an occupied
       subshell s to the same target t if nu(s) > nu(t) -- the move is downhill

Step 1 alone reproduces the current walk. Step 2 is the only new content, it uses
no new parameter, and it is the transition reading taken literally: a cell is a
move, and a move happens when it lowers nu.

WHAT IT MUST DO TO EARN ITS PLACE. It must predict the twelve donor steps, and it
must not break the ninety-four that arrive from the notional outside. A rule that
buys the twelve by spoiling the ninety-four is not an improvement, and the base
rate matters: predicting "no relocation" everywhere already scores 94 of 106.
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


def nu(nl, o, a):
    n, l = nl
    return n - a * math.sqrt((n - l - 1) + o / cap(l))


def truth(Z):
    """(target, source or None, q) as observed."""
    a, b = occ(Z - 1), occ(Z)
    tgt = (IV[Z][1], IV[Z][2])
    lost = [k for k in a if a[k] > b.get(k, 0)]
    return tgt, (lost[0] if lost else None), b[tgt] - a.get(tgt, 0)


def predict(prev, a):
    t = min(((nu(c, prev.get(c, 0), a), c) for c in cands(prev)))[1]
    after = dict(prev)
    after[t] = after.get(t, 0) + 1
    # step 2 — does an occupied subshell want to move an electron into t?
    best, src = None, None
    for s, o in prev.items():
        if s == t or o == 0 or after.get(t, 0) >= cap(t[1]):
            continue
        gain = nu(s, o, a) - nu(t, after[t], a)          # downhill if positive
        if gain > EPS and (best is None or gain > best):
            best, src = gain, s
    return t, src, (2 if src else 1)


# a placed as in scorer.py's handshake run, so the comparison is like for like
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
tt = ts = tq = full = 0
donor_hit, donor_miss, broke = [], [], []
for Z in STEPS:
    prev = occ(Z - 1)
    pt, ps, pq = predict(prev, A[Z])
    ot, os_, oq = truth(Z)
    tt += pt == ot
    ts += ps == os_
    tq += pq == oq
    ok = (pt, ps, pq) == (ot, os_, oq)
    full += ok
    if os_ is not None:
        (donor_hit if ok else donor_miss).append((Z, ot, os_, ps))
    elif ps is not None:
        broke.append((Z, ps))

print(f"  THE WALK AS A TRANSITION — {len(STEPS)} steps\n")
print(f"    target correct                  {tt:>4} of {len(STEPS)}")
print(f"    source correct                  {ts:>4} of {len(STEPS)}")
print(f"    q correct                       {tq:>4} of {len(STEPS)}")
print(f"    FULL triple correct             {full:>4} of {len(STEPS)}")
print(f"\n    baseline — predict 'no relocation' everywhere: 94 of {len(STEPS)}")
print(f"\n    of the twelve donor steps, fully right: {len(donor_hit)}")
for Z, ot, os_, ps in donor_hit:
    print(f"      {SYM[Z-1]}{Z}  {os_[0]}{L[os_[1]]} -> {ot[0]}{L[ot[1]]}")
print(f"    donor steps missed: {len(donor_miss)}")
for Z, ot, os_, ps in donor_miss:
    p = f"{ps[0]}{L[ps[1]]}" if ps else "none"
    print(f"      {SYM[Z-1]}{Z}  observed {os_[0]}{L[os_[1]]} -> {ot[0]}{L[ot[1]]}   said source {p}")
print(f"\n    FALSE relocations invented on outside-arrival steps: {len(broke)}")
if broke:
    print("      " + ", ".join(f"{SYM[Z-1]}{Z}({s[0]}{L[s[1]]})" for Z, s in broke[:16]))
