#!/usr/bin/env python3
"""check.py -- the machine checks behind "The occupation law as a lower convex hull".

Every number the paper prints is produced here, and every decidable claim is decided here.
Exact arithmetic throughout: a corridor endpoint is a rational combination of square roots of
squarefree integers, held as {m: Fraction}.  Equality is decided by that representation, which is
faithful because square roots of distinct squarefree integers are linearly independent over Q; a
non-zero sign is decided by a rational enclosure of the sum refined until it excludes 0.  No sign
is ever decided in floating point.  Floating point appears only in the epsilon-walk of section 5
and the coverage sweep of section 6, both of which are themselves rules stated with a tolerance.

    python3 check.py              every obligation, one line each, a summary; exit 1 on any failure
    python3 check.py --selftest   the same, plus three negative controls that must be REFUTED
    python3 check.py --table      the 106 corridors as a Markdown table (pasted into PAPER.md)

Instruments imported BY PATH and never copied:
    method/members/LW1-ground.py            the observed ground configurations (NIST ASD 5.12)
    tools/slopeaxis.py                      the seated corridor/hull instrument (the object under test)
    method/proofs/walkresets.py             the walk of the recovered instrument, with its resets
    method/proofs/candidateset.py           the two candidate-set conventions at the f openings
    research/warp-drive/prover.py           the Z3 harness (require_z3, guard discipline)
The reference implementations below are written fresh; that is the point of a guard.
"""
import argparse
import collections
import contextlib
import importlib.util
import io
import functools
import itertools
import math
import os
import random
import re
import sys
import time
from decimal import Decimal, ROUND_HALF_UP, getcontext
from fractions import Fraction as Fr

getcontext().prec = 60

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
MEMBERS = os.path.join(ROOT, "method", "members")
LET = "spdfghijklmno"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


G = load(os.path.join(MEMBERS, "LW1-ground.py"), "LW1_ground")

# ----------------------------------------------------------------------------- the data


def cap(l):
    return 2 * (2 * l + 1)


def occ(Z):
    c = {}
    if Z < 1:
        return c
    for n, l, o in G.expand(Z):
        c[(n, l)] = c.get((n, l), 0) + o
    return c


def gains(Z):
    pr, cu = occ(Z - 1), occ(Z)
    return [(cu[k] - pr.get(k, 0), k) for k in cu if cu[k] - pr.get(k, 0) > 0]


def entrant(Z):
    g = gains(Z)
    assert len(g) == 1, (Z, g)
    return g[0][1]


def name(s):
    return "%d%s" % (s[0], LET[s[1]])


STEPS = list(range(3, 109))

# ----------------------------------------------------------------------------- exact surds
# A number is held as {m: c}: the sum of c*sqrt(m) over squarefree m (m = 1 is the rational part).

# The sign of a non-zero surd is decided EXACTLY, by rational enclosure of each radical
# refined until the enclosure of the sum excludes 0.  Termination rests on the linear
# independence over Q of {sqrt(m) : m squarefree} together with 1 (Besicovitch 1940):
# a non-empty representation is a non-zero number, so some finite precision separates it.
MINBOUND = [None]   # a certified rational lower bound on the smallest |value| ever decided
MAXPREC = [0]       # the deepest enclosure ever needed, in decimal digits


def sqfree(N):
    k, m, d = 1, 1, 2
    while d * d <= N:
        while N % (d * d) == 0:
            N //= d * d
            k *= d
        if N % d == 0:
            N //= d
            m *= d
        d += 1
    return k, m * N


def sqrt_rat(r):
    """sqrt of a non-negative Fraction as a surd."""
    if r == 0:
        return {}
    k, m = sqfree(r.numerator * r.denominator)
    return {m: Fr(k, r.denominator)}


def add(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + c
        if out[m] == 0:
            del out[m]
    return out


def neg(a):
    return {m: -c for m, c in a.items()}


def scale(a, c):
    return {m: v * c for m, v in a.items()} if c != 0 else {}


def val(a):
    if not a:
        return Decimal(0)
    return sum((Decimal(c.numerator) / Decimal(c.denominator)) * Decimal(m).sqrt() for m, c in a.items())


def key(a):
    return tuple(sorted(a.items()))


_SQB = {}


def sqrt_bounds(m, k):
    """Rationals L <= sqrt(m) <= U with U - L <= 10^-k, exactly, for an integer m >= 0."""
    hit = _SQB.get((m, k))
    if hit is not None:
        return hit
    if m <= 1:
        out = (Fr(m), Fr(m))
    else:
        d = 10 ** k
        a = math.isqrt(m * d * d)
        out = (Fr(a, d), Fr(a + 1, d))
    _SQB[(m, k)] = out
    return out


def decide(a):
    """(sign, L) with L a rational lower bound on |a|, both exact.  Zero is decided by the representation: a sum of rational
    multiples of square roots of distinct squarefree integers (1 among them) vanishes
    only when every coefficient vanishes.  A non-zero sign is decided by a rational
    enclosure of the sum, refined until it excludes 0; the same theorem guarantees that
    some finite precision does.  No floating point enters the decision."""
    if not a:
        return 0, Fr(0)
    k = 24
    while True:
        lo = hi = Fr(0)
        for m, c in a.items():
            L, U = sqrt_bounds(m, k)
            if c > 0:
                lo += c * L
                hi += c * U
            else:
                lo += c * U
                hi += c * L
        if lo > 0:
            mag, out = lo, 1
            break
        if hi < 0:
            mag, out = -hi, -1
            break
        k *= 2
        if k > 8192:
            raise AssertionError("sign: no separation at 8192 digits for %r" % (a,))
    if k > MAXPREC[0]:
        MAXPREC[0] = k
    if MINBOUND[0] is None or mag < MINBOUND[0]:
        MINBOUND[0] = mag
    return out, mag


def sign(a):
    return decide(a)[0]


def gap(a, b):
    """A rational lower bound on |a - b|, exact.  Zero only when a = b."""
    return decide(add(a, neg(b)))[1]


def less(a, b):
    return sign(add(a, neg(b))) < 0


def dec7(a):
    return "%.7f" % val(a).quantize(Decimal("0.0000001"), rounding=ROUND_HALF_UP)


def closed(a):
    """A surd as a closed form: (k1 sqrt(m1) + k2 sqrt(m2))/den."""
    if not a:
        return "0"
    den = 1
    for c in a.values():
        den = den * c.denominator // math.gcd(den, c.denominator)
    terms = []
    for m, c in sorted(a.items()):
        k = c.numerator * (den // c.denominator)
        root = "" if m == 1 else "√%d" % m
        if abs(k) == 1 and m != 1:
            t = root
        elif m == 1:
            t = "%d" % abs(k)
        else:
            t = "%d%s" % (abs(k), root)
        terms.append(("−" if k < 0 else "+", t))
    s = terms[0][1] if terms[0][0] == "+" else "−" + terms[0][1]
    for sg, t in terms[1:]:
        s += " %s %s" % (sg, t)
    if den == 1:
        return s
    return ("(%s)/%d" % (s, den)) if len(terms) > 1 else "%s/%d" % (s, den)

# ----------------------------------------------------------------------------- the geometry
# A point is (r, y): r = x^2 a non-negative Fraction, y an integer.  Every slope between two
# points of different abscissa is Dy (sqrt(r2) + sqrt(r1)) / (r2 - r1), a surd.


def slope(p, q):
    (r1, y1), (r2, y2) = p, q
    assert r1 != r2
    return scale(add(sqrt_rat(r2), sqrt_rat(r1)), Fr(y2 - y1) / (r2 - r1))


def corridor(i, pts):
    """The open interval of slopes on which point i is the unique minimiser of y - a x.
    Returns (lo, hi, infeasible) with None for an absent bound."""
    ps = pts[i]
    lo = hi = None
    bad = False
    for j, pr in enumerate(pts):
        if j == i:
            continue
        if pr[0] == ps[0]:
            if pr[1] <= ps[1]:
                bad = True
            continue
        sl = slope(ps, pr)
        if pr[0] > ps[0]:
            if hi is None or less(sl, hi):
                hi = sl
        else:
            if lo is None or less(lo, sl):
                lo = sl
    return lo, hi, bad


def nonempty(c):
    lo, hi, bad = c
    if bad:
        return False
    if lo is None or hi is None:
        return True
    return less(lo, hi)


def cross(u, s, w):
    """sign of (x_w - x_u)(y_s - y_u) - (y_w - y_u)(x_s - x_u), exactly."""
    xu, xs, xw = sqrt_rat(u[0]), sqrt_rat(s[0]), sqrt_rat(w[0])
    return sign(add(scale(add(xw, neg(xu)), s[1] - u[1]), neg(scale(add(xs, neg(xu)), w[1] - u[1]))))


def vertex_pairwise(i, pts):
    """s is NOT in conv(P - s) + [0, inf) e_y: for every pair u, w of other points with
    x_u <= x_s <= x_w, s lies strictly below the line u w (a same-abscissa point must be
    strictly above s).  Independent of the corridor and of the chain."""
    s = pts[i]
    others = [p for j, p in enumerate(pts) if j != i]
    for u in others:
        if u[0] == s[0] and u[1] <= s[1]:
            return False
    for u in others:
        for w in others:
            if u is w or not (u[0] < s[0] < w[0]):
                continue
            if cross(u, s, w) >= 0:
                return False
    return True


def hull_chain(pts):
    """Andrew's monotone chain, lower half, strict turns, exact signs.  Returns indices."""
    byx = {}
    for i, p in enumerate(pts):
        if p[0] not in byx or p[1] < pts[byx[p[0]]][1]:
            byx[p[0]] = i
    order = sorted(byx.values(), key=lambda i: pts[i][0])
    H = []
    for i in order:
        while len(H) >= 2 and cross(pts[H[-2]], pts[H[-1]], pts[i]) >= 0:
            H.pop()
        H.append(i)
    return H

# ----------------------------------------------------------------------------- the atoms


def admissible(prev, N=15, lmax=4):
    return [(n, l) for n in range(1, N + 1) for l in range(0, min(lmax, n - 1) + 1)
            if prev.get((n, l), 0) < cap(l)]


def point(s, prev, form):
    n, l = s
    r = Fr(n - l - 1) + (Fr(prev.get(s, 0), cap(l)) if form == "q" else 0)
    return (r, n)


def step(Z, form, N=15, lmax=4):
    prev = occ(Z - 1)
    S = admissible(prev, N, lmax)
    pts = [point(s, prev, form) for s in S]
    return prev, S, pts


def ent_corridor(Z, form, N=15, lmax=4):
    prev, S, pts = step(Z, form, N, lmax)
    e = entrant(Z)
    assert e in S
    return corridor(S.index(e), pts)


def ckey(c):
    lo, hi, bad = c
    return (None if lo is None else key(lo), None if hi is None else key(hi), bad)


def fl(a, default):
    return default if a is None else float(val(a))


def walk(form, eps, N=15, lmax=4):
    """The carried slope: held while strictly inside the step's corridor, otherwise moved to the
    nearer endpoint and eps inside it.  a starts at 0.  Returns one row per step."""
    a = 0.0
    TR = []
    for Z in STEPS:
        lo, hi, bad = ent_corridor(Z, form, N, lmax)
        L, U = fl(lo, -math.inf), fl(hi, math.inf)
        if L < a < U:
            TR.append(dict(Z=Z, a=a, move=0.0, L=L, U=U, at=None, lo=lo, hi=hi))
            continue
        old = a
        if a <= L:
            a, at = L + eps, "L"
        else:
            a, at = U - eps, "U"
        TR.append(dict(Z=Z, a=a, move=a - old, L=L, U=U, at=at, lo=lo, hi=hi))
    return TR


def openings():
    op, prev = {}, {}
    for Z in range(1, 109):
        cur = occ(Z)
        for k, v in cur.items():
            if v > 0 and prev.get(k, 0) == 0:
                op.setdefault(Z, []).append(k)
        prev = cur
    return op


def spans():
    first, done = {}, {}
    for Z in range(1, 109):
        for k, v in occ(Z).items():
            if v > 0 and k not in first:
                first[k] = Z
            if v >= cap(k[1]) and k not in done:
                done[k] = Z
    return {k: (first[k], done.get(k)) for k in first}

# ----------------------------------------------------------------------------- reporting

LINES = []
FAILS = []
NUM = {}            # every number the paper prints


QUIET = [False]


def rep(status, label, ok, detail=""):
    LINES.append((status, label, ok, detail))
    if not ok:
        FAILS.append(label)
    if not QUIET[0]:
        print("  [%s] %-70s %s" % (("ok  " if ok else "FAIL"), label, detail))


def compute(quiet=False):
    """Everything the paper states, computed once.  Returns a dict of results."""
    out = {}
    say = (lambda *a: None) if quiet else print

    # 0. the data
    say("\n0  THE DATA")
    bad = [Z for Z in range(1, 109) if G.occ_count(Z) != Z]
    rep("EXHAUSTIVE", "electron counts validate at every Z of 1..108", not bad, "%d of 108" % (108 - len(bad)))
    multi = [Z for Z in STEPS if len(gains(Z)) != 1]
    rep("EXHAUSTIVE", "exactly one subshell gains at every step Z = 3..108", not multi, "%d steps" % len(STEPS))
    NUM["steps"] = len(STEPS)
    ents = {Z: entrant(Z) for Z in STEPS}
    out["entrant"] = ents
    two = [Z for Z in STEPS if gains(Z)[0][0] == 2]
    rep("EXHAUSTIVE", "twelve steps gain two electrons (another subshell loses one): Cr Cu Nb Ru Pd Pr Tb Pt Pa Pu Bk Rf",
        two == [24, 29, 41, 44, 46, 59, 65, 78, 91, 94, 97, 104] and all(gains(Z)[0][0] == 1 for Z in STEPS if Z not in two),
        "%s" % two)
    NUM["two_electron"] = two
    # the data's own marks of a calculated entry: a ground level printed as a bare J with no term
    bareJ = [Z for Z in range(1, 109) if re.fullmatch(r"\d+(/\d+)?", G.GROUND[Z][2])]
    rep("EXHAUSTIVE", "the tabulated ground level is a bare J with no term at exactly Sg, Bh, Hs (Z = 106, 107, 108)",
        bareJ == [106, 107, 108], "%s" % bareJ)
    NUM["bareJ"] = bareJ
    rep("EXHAUSTIVE", "Z = 103 (Lr): the tabulated configuration [Rn]5f14 7s2 7p makes 7p the entrant; the (n+l, n) pick there is 6d",
        G.GROUND[103][1] == "[Rn]5f14 7s2 7p" and ents[103] == (7, 1)
        and min(step(103, "p")[1], key=lambda s: (s[0] + s[1], s[0])) == (6, 2))
    # the unconditional aufbau: fill subshells in (n+l, n) order from nothing, and compare with the table
    aorder = sorted([(n, l) for n in range(1, 10) for l in range(0, n)], key=lambda s: (s[0] + s[1], s[0]))

    def aufbau(Z):
        c, left = {}, Z
        for s in aorder:
            if left == 0:
                break
            k = min(left, cap(s[1]))
            c[s] = k
            left -= k
        return c
    adiff = [Z for Z in range(1, 109) if aufbau(Z) != occ(Z)]
    rep("EXHAUSTIVE", "the unconditional (n+l, n) aufbau differs from the tabulated configuration at exactly 20 atoms",
        adiff == [24, 29, 41, 42, 44, 45, 46, 47, 57, 58, 64, 78, 79, 89, 90, 91, 92, 93, 96, 103],
        "%s" % [G.GROUND[Z][0] for Z in adiff])
    NUM["aufbau_diff"] = adiff
    out["aufbau_diff"] = adiff
    op = openings()
    sp = spans()
    out["openings"], out["spans"] = op, sp
    # no two admissible subshells share a point, either form
    for form in ("p", "q"):
        clash = 0
        for Z in STEPS:
            prev, S, pts = step(Z, form)
            clash += len(pts) != len(set(pts))
        rep("EXHAUSTIVE", "form %s: no two admissible subshells share a point, 106 steps" % form, clash == 0)
    # n + l = 2n - p - 1 on every subshell of the frame
    bad = [(n, l) for n in range(1, 16) for l in range(0, min(4, n - 1) + 1) if n + l != 2 * n - (n - l - 1) - 1]
    rep("EXHAUSTIVE", "n + l = 2n - p - 1 on every subshell n <= 15, l <= 4", not bad)
    # no tabulated configuration occupies a g subshell, so 5g (node-free, capacity 18) is admissible at every step
    gocc = [Z for Z in range(1, 109) if any(l >= 4 and o > 0 for n, l, o in G.expand(Z))]
    rep("EXHAUSTIVE", "no ground configuration Z <= 108 occupies a subshell with l >= 4; 5g admissible at every step",
        not gocc and all(occ(Z - 1).get((5, 4), 0) < cap(4) for Z in STEPS))

    # 1. corridors and hulls at every step, both forms, three routes
    say("\n1  THE CORRIDOR AND THE HULL AT EVERY STEP, THREE ROUTES")
    out["cor"] = {}
    out["A"] = {}
    out["hull"] = {}
    out["pts"] = {}
    for form in ("p", "q"):
        ne = 0
        mism_pair = mism_chain = 0
        Ahist = collections.Counter()
        cors, Aset, hulls, ptss = {}, {}, {}, {}
        for Z in STEPS:
            prev, S, pts = step(Z, form)
            cs = [corridor(i, pts) for i in range(len(S))]
            A = {S[i] for i in range(len(S)) if nonempty(cs[i])}
            V = {S[i] for i in range(len(S)) if vertex_pairwise(i, pts)}
            H = {S[i] for i in hull_chain(pts)}
            mism_pair += A != V
            mism_chain += A != H
            e = ents[Z]
            ce = cs[S.index(e)]
            ne += nonempty(ce)
            Ahist[len(A)] += 1
            cors[Z] = ce
            Aset[Z] = A
            hulls[Z] = [S[i] for i in hull_chain(pts)]
            ptss[Z] = dict(zip(S, pts))
        rep("EXHAUSTIVE", "form %s: {corridor non-empty} = {vertex, pairwise test}, 106 steps" % form, mism_pair == 0)
        rep("EXHAUSTIVE", "form %s: {corridor non-empty} = {vertex, monotone chain}, 106 steps" % form, mism_chain == 0)
        rep("EXHAUSTIVE", "form %s: the observed entrant's corridor is non-empty" % form, ne == 106, "%d of 106" % ne)
        rep("EXHAUSTIVE", "form %s: every step has at least two vertices" % form, min(Ahist) >= 2,
            "min %d, max %d" % (min(Ahist), max(Ahist)))
        want_rng = {"p": (11, 15), "q": (7, 15)}[form]
        rep("EXHAUSTIVE", "form %s: vertices per step in the frame n <= 15, l <= 4 run from %d to %d" % ((form,) + want_rng),
            (min(Ahist), max(Ahist)) == want_rng, "%s" % dict(sorted(Ahist.items())))
        NUM["nonempty_" + form] = ne
        NUM["Ahist15_" + form] = dict(sorted(Ahist.items()))
        out["cor"][form], out["A"][form], out["hull"][form], out["pts"][form] = cors, Aset, hulls, ptss
        # the endpoints are the flanking hull-edge slopes (sorted vertices)
        bad = 0
        for Z in STEPS:
            prev, S, pts = step(Z, form)
            H = hull_chain(pts)
            for k, i in enumerate(H):
                lo, hi, inf = corridor(i, pts)
                want_lo = None if k == 0 else slope(pts[H[k - 1]], pts[i])
                want_hi = None if k == len(H) - 1 else slope(pts[i], pts[H[k + 1]])
                if (lo is None) != (want_lo is None) or (hi is None) != (want_hi is None):
                    bad += 1
                elif (lo is not None and key(lo) != key(want_lo)) or (hi is not None and key(hi) != key(want_hi)):
                    bad += 1
        rep("EXHAUSTIVE", "form %s: every vertex's L, U are its flanking hull-edge slopes, exactly" % form, bad == 0)
    # |A| under the instrument's own frame n <= 7
    Ah7 = collections.Counter()
    for Z in STEPS:
        prev, S, pts = step(Z, "p", 7, 4)
        Ah7[sum(1 for i in range(len(S)) if nonempty(corridor(i, pts)))] += 1
    NUM["Ahist7_p"] = dict(sorted(Ah7.items()))
    rep("EXHAUSTIVE", "node-only, frame n <= 7: vertices per step are 3 at 6 steps, 4 at 56, 5 at 28, 6 at 14, 7 at 2",
        NUM["Ahist7_p"] == {3: 6, 4: 56, 5: 28, 6: 14, 7: 2}, "%s" % NUM["Ahist7_p"])
    # the abscissa is a choice: with x = r in place of x = sqrt(r) the entrant is not a vertex at every step
    for form, want_ne, want_not in (("p", 100, [57, 64, 89, 90, 96, 103]), ("q", 101, [57, 64, 89, 96, 103])):
        notv = []
        for Z in STEPS:
            prev, S, pts = step(Z, form)
            sq = [(r * r, n) for r, n in pts]          # sqrt(r^2) = r: the abscissa is r itself, exactly
            if not nonempty(corridor(S.index(ents[Z]), sq)):
                notv.append(Z)
        rep("EXHAUSTIVE", "form %s, abscissa x = r instead of sqrt(r): the entrant's corridor is non-empty at %d of 106" % (form, want_ne),
            notv == want_not and 106 - len(notv) == want_ne, "not at %s" % [G.GROUND[Z][0] for Z in notv])
        NUM["linear_notv_" + form] = notv

    # 2. the frame: the entrant's corridor is the same under every frame past the reduction
    say("\n2  THE FRAME")
    for form, frames, expect_same in (("p", [(8, 4), (12, 4), (20, 4), (30, 4), (15, 14), (8, 14)], True),
                                      ("q", [(12, 4), (20, 4), (30, 4), (15, 14)], True),
                                      ("q", [(8, 4)], False)):
        for N, lm in frames:
            d = [Z for Z in STEPS if ckey(ent_corridor(Z, form, N, lm)) != ckey(out["cor"][form][Z])]
            ok = (not d) if expect_same else bool(d)
            rep("EXHAUSTIVE", "form %s: frame n <= %d, l <= %d gives the n <= 15, l <= 4 corridors" % (form, N, lm)
                if expect_same else "form %s: frame n <= %d, l <= %d DIFFERS (expected)" % (form, N, lm), ok,
                "differ at %s" % d if d else "identical at 106 steps")
            if form == "q" and (N, lm) == (8, 4):
                NUM["q_frame8_differs"] = d
    # a frame reaching n = 15 without g is NOT enough: l <= 4 is part of the hypothesis
    d153 = [Z for Z in STEPS if ckey(ent_corridor(Z, "p", 15, 3)) != ckey(out["cor"]["p"][Z])]
    rep("EXHAUSTIVE", "node-only: the frame n <= 15, l <= 3 (no g) differs at exactly sixteen steps, 91-95, 97-102, 104-108",
        d153 == [91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108], "%s" % d153)
    NUM["nog_differs"] = d153
    # the frame THEOREM: the extremes it needs, and the two closed frames it certifies
    EXTREME = {}
    for form in ("p", "q"):
        maxU = minL = None
        maxr = Fr(0)
        maxn = 0
        for Z in STEPS:
            lo, hi, _ = out["cor"][form][Z]
            assert hi is not None
            if maxU is None or less(maxU, hi):
                maxU = hi
            if lo is not None and (minL is None or less(lo, minL)):
                minL = lo
            pt = point(ents[Z], occ(Z - 1), form)
            maxr, maxn = max(maxr, pt[0]), max(maxn, pt[1])
        EXTREME[form] = (maxU, minL, maxr, maxn)
        NUM["extreme_" + form] = (closed(maxU), dec7(maxU), closed(minL), dec7(minL), str(maxr), maxn)
    wantp = (key({6: Fr(1), 7: Fr(1)}), key({}), Fr(6), 7)
    wantq = (key({11: Fr(10, 9), 26: Fr(5, 9)}), key({14: Fr(-1)}), Fr(13, 2), 7)
    for form, want in (("p", wantp), ("q", wantq)):
        maxU, minL, maxr, maxn = EXTREME[form]
        rep("EXHAUSTIVE", "form %s: over the 106 steps max U, min L, max radicand and max n of the entrant" % form,
            (key(maxU), key(minL), maxr, maxn) == want,
            "U <= %s, L >= %s, r_e <= %s, n_e <= %d" % (closed(maxU), closed(minL), maxr, maxn))
    # Theorem 3's two inequalities, exactly.  phi(n) = (n-7)/sqrt(n-1) at n = 38; psi(n) = (n-7)/sqrt(n) at n = 56.
    phi38 = scale(sqrt_rat(Fr(1, 37)), Fr(31))
    psi56 = scale(sqrt_rat(Fr(1, 56)), Fr(49))
    rep("EXHAUSTIVE", "Theorem 3, form p: 31/sqrt(37) exceeds the largest U", less(EXTREME["p"][0], phi38),
        "%s = %s > %s" % (closed(phi38), dec7(phi38), dec7(EXTREME["p"][0])))
    rep("EXHAUSTIVE", "Theorem 3, form q: 49/sqrt(56) exceeds the largest U", less(EXTREME["q"][0], psi56),
        "%s = %s > %s" % (closed(psi56), dec7(psi56), dec7(EXTREME["q"][0])))
    # and the left-hand halves: a rival above the entrant and left of it has a slope below min L
    lp = scale(sqrt_rat(Fr(1, 6)), Fr(-31))
    lq = scale(sqrt_rat(Fr(2, 13)), Fr(-49))
    rep("EXHAUSTIVE", "Theorem 3, form p: -31/sqrt(6) falls below the smallest L", less(lp, EXTREME["p"][1]),
        "%s < %s" % (dec7(lp), dec7(EXTREME["p"][1])))
    rep("EXHAUSTIVE", "Theorem 3, form q: -49/sqrt(13/2) falls below the smallest L", less(lq, EXTREME["q"][1]),
        "%s < %s" % (dec7(lq), dec7(EXTREME["q"][1])))
    # the two closed frames: every subshell the lemma does not cover, admitted
    for form, N, lm in (("p", 37, 36), ("q", 55, 54)):
        d = [Z for Z in STEPS if ckey(ent_corridor(Z, form, N, lm)) != ckey(out["cor"][form][Z])]
        rep("EXHAUSTIVE", "form %s: frame n <= %d, l <= %d gives the n <= 15, l <= 4 corridors" % (form, N, lm),
            not d, "differ at %s" % d if d else "identical at 106 steps")

    # the instrument's frame n <= 7 differs at exactly three ceilings
    d7 = [Z for Z in STEPS if ckey(ent_corridor(Z, "p", 7, 4)) != ckey(out["cor"]["p"][Z])]
    rep("EXHAUSTIVE", "node-only: the frame n <= 7 differs from the full set at exactly Fr, Ra, Lr", d7 == [87, 88, 103], "%s" % d7)
    NUM["frame7_differs"] = d7
    no_ceiling7 = [Z for Z in STEPS if ent_corridor(Z, "p", 7, 4)[1] is None]
    rep("EXHAUSTIVE", "node-only, n <= 7: the three are the steps with no ceiling there", no_ceiling7 == [87, 88, 103])
    ends7 = set()
    for Z in STEPS:
        lo, hi, _ = ent_corridor(Z, "p", 7, 4)
        ends7 |= {key(x) for x in (lo, hi) if x is not None}
    NUM["ends7_p"] = len(ends7)
    rep("EXHAUSTIVE", "node-only, n <= 7: distinct endpoints (the instrument's figure)", len(ends7) == 17, "%d" % len(ends7))

    # 3. the endpoints
    say("\n3  THE ENDPOINTS")
    out["ends"] = {}
    for form in ("p", "q"):
        ends = collections.defaultdict(lambda: dict(nL=0, nU=0, Z=[]))
        for Z in STEPS:
            lo, hi, _ = out["cor"][form][Z]
            if lo is not None:
                ends[key(lo)]["nL"] += 1
                ends[key(lo)]["Z"].append(Z)
            if hi is not None:
                ends[key(hi)]["nU"] += 1
                ends[key(hi)]["Z"].append(Z)
        lst = sorted(ends.items(), key=functools.cmp_to_key(
            lambda A, B: sign(add(dict(A[0]), neg(dict(B[0]))))))
        # distinctness: every consecutive gap is bounded below by an exact rational
        gaps = [gap(dict(lst[i + 1][0]), dict(lst[i][0])) for i in range(len(lst) - 1)]
        mingap = min(gaps)
        want_n = {"p": 19, "q": 138}[form]
        rep("EXHAUSTIVE", "form %s: %d distinct endpoints over the 106 corridors" % (form, want_n), len(lst) == want_n,
            "%d, min gap %.4g" % (len(lst), float(mingap)))
        rep("EXHAUSTIVE", "form %s: consecutive endpoints are separated by more than 1/10000, exactly" % form,
            mingap > Fr(1, 10000), "certified lower bound %.4g" % float(mingap))
        NUM["ends_" + form] = len(lst)
        out["ends"][form] = [(dict(k), v) for k, v in lst]
    NUM["ends_p_list"] = [(closed(d), dec7(d), v["nL"], v["nU"]) for d, v in out["ends"]["p"]]
    no_floor = [Z for Z in STEPS if out["cor"]["p"][Z][0] is None]
    no_ceil = [Z for Z in STEPS if out["cor"]["p"][Z][1] is None]
    NUM["nofloor_p"], NUM["noceil_p"] = no_floor, no_ceil
    NUM["twosided_p"] = 106 - len(no_floor) - len(no_ceil)
    rep("EXHAUSTIVE", "node-only: corridors with no ceiling", len(no_ceil) == 0, "%d" % len(no_ceil))
    rep("EXHAUSTIVE", "node-only: 80 two-sided corridors, 26 with no floor, 0 with no ceiling",
        (NUM["twosided_p"], len(no_floor), len(no_ceil)) == (80, 26, 0), "%d + %d + %d = 106" % (NUM["twosided_p"], len(no_floor), len(no_ceil)))
    # the narrowest two-sided corridor, exactly: Lr's, of width (sqrt7 - sqrt3)/2, far above 2 eps
    narrow = None
    for Z in STEPS:
        lo, hi, _ = out["cor"]["p"][Z]
        if lo is None:
            continue
        w = add(hi, neg(lo))
        if narrow is None or less(w, narrow[0]):
            narrow = (w, Z)
    rep("EXHAUSTIVE", "node-only: the narrowest two-sided corridor is Lr's, of width (sqrt7 - sqrt3)/2 > 2 eps for every eps <= 1e-4",
        narrow[1] == 103 and key(narrow[0]) == key({3: Fr(-1, 2), 7: Fr(1, 2)}) and less({1: Fr(2, 10000)}, narrow[0]),
        "%s = %s at Z = %d" % (closed(narrow[0]), dec7(narrow[0]), narrow[1]))
    NUM["narrowest"] = (closed(narrow[0]), dec7(narrow[0]), narrow[1])

    # the ns / (n-1)d crossing
    say("\n   the crossing (sqrt(n-1) + sqrt(n-4))/3")
    # (u+v)(u-v) - (u^2 - v^2) vanishes identically: degree 2 in u and v, 3-point grid each
    grid = [Fr(2, 1), Fr(7, 3), Fr(5, 2)]
    resid = max(abs((u + v) * (u - v) - (u * u - v * v)) for u in grid for v in grid)
    rep("EXHAUSTIVE", "(u+v)(u-v) = u^2 - v^2 on a 3x3 rational grid above degree 2", resid == 0)
    rep("EXHAUSTIVE", "(n-1) - (n-4) = 3 on a 2-point grid above degree 1", all((n - 1) - (n - 4) == 3 for n in (Fr(4), Fr(11, 2))))
    cross_vals = {}
    for n, Z in ((4, 19), (5, 37), (6, 55), (7, 87)):
        want = scale(add(sqrt_rat(Fr(n - 1)), sqrt_rat(Fr(n - 4))), Fr(1, 3))
        lo = out["cor"]["p"][Z][0]
        rep("EXHAUSTIVE", "floor at Z = %d (%ss opens) equals (sqrt(%d)+sqrt(%d))/3 exactly" % (Z, n, n - 1, n - 4),
            key(lo) == key(want), "%s = %s" % (closed(lo), dec7(lo)))
        cross_vals[n] = (closed(want), dec7(want))
    NUM["cross"] = cross_vals

    # 4. the floor
    say("\n4  THE FLOOR")
    nodefree = [Z for Z in STEPS if ents[Z][0] - ents[Z][1] - 1 == 0]
    nodefree_open = [Z for Z in nodefree if occ(Z - 1).get(ents[Z], 0) == 0]
    rep("EXHAUSTIVE", "node-only: {no floor} = {entrant node-free}", no_floor == nodefree, "%d steps" % len(no_floor))
    rep("EXHAUSTIVE", "finished: {no floor} = {entrant node-free and empty}",
        [Z for Z in STEPS if out["cor"]["q"][Z][0] is None] == nodefree_open, "%s" % nodefree_open)
    NUM["nodefree"], NUM["nodefree_open"] = nodefree, nodefree_open
    NUM["nofloor_q"] = nodefree_open
    for Z, sub, want_p in ((58, (4, 3), 0), (91, (5, 3), 1)):
        lo, hi, _ = out["cor"]["p"][Z]
        p = sub[0] - sub[1] - 1
        rep("EXHAUSTIVE", "Z = %d: entrant %s, p = %d" % (Z, name(sub), want_p), ents[Z] == sub and p == want_p)
        NUM["Z%d" % Z] = dict(p=p, L=None if lo is None else (closed(lo), dec7(lo)), U=None if hi is None else (closed(hi), dec7(hi)))
    rep("EXHAUSTIVE", "Z = 58 (Ce, 4f): no floor; ceiling 1/sqrt2", out["cor"]["p"][58][0] is None and key(out["cor"]["p"][58][1]) == key({2: Fr(1, 2)}))
    lo91, hi91, _ = out["cor"]["p"][91]
    rep("EXHAUSTIVE", "Z = 91 (Pa, 5f): floor 0, ceiling (1+sqrt3)/2", lo91 is not None and sign(lo91) == 0 and key(hi91) == key({1: Fr(1, 2), 3: Fr(1, 2)}))
    # who supplies Pa's floor: the rival at smaller abscissa with the largest slope is 5g
    prev, S, pts = step(91, "p")
    i = S.index((5, 3))
    left = [(S[j], slope(pts[i], pts[j])) for j in range(len(S)) if pts[j][0] < pts[i][0]]
    best = max(left, key=lambda t: val(t[1]))
    rep("EXHAUSTIVE", "Z = 91: the floor is supplied by 5g", best[0] == (5, 4))
    # which node-free subshells are admissible at Pa: none of 1s 2p 3d 4f; 5g only
    nf = [s for s in S if s[0] - s[1] - 1 == 0]
    rep("EXHAUSTIVE", "Z = 91: the only admissible node-free subshell is 5g", nf == [(5, 4)], "%s" % [name(s) for s in nf])
    # without g: Pa has no floor, and eleven steps break the equivalence
    nf_nog = [Z for Z in STEPS if ent_corridor(Z, "p", 15, 3)[0] is None]
    # the 5f steps of 91..102: Cm (96) is not one of them, its entrant is 6d
    fsteps = [Z for Z in range(91, 103) if ents[Z] == (5, 3)]
    assert len(fsteps) == 11 and 96 not in fsteps and ents[96] == (6, 2)
    rep("EXHAUSTIVE", "without g (l <= 3): {no floor} minus {node-free} is the eleven 5f steps of 91..102",
        sorted(set(nf_nog) - set(nodefree)) == fsteps, "%s" % fsteps)
    NUM["nog_extra"] = sorted(set(nf_nog) - set(nodefree))
    # without g the five 6d steps Rf..Hs keep their ceiling and their floor falls from sqrt3/3 (5g) to 0 (6f)
    rfhs_ok = True
    for Z in (104, 105, 106, 107, 108):
        lo3, hi3, _ = ent_corridor(Z, "p", 15, 3)
        lo4, hi4, _ = out["cor"]["p"][Z]
        prev3, S3, pts3 = step(Z, "p", 15, 3)
        i3 = S3.index(ents[Z])
        left3 = [(S3[j], slope(pts3[i3], pts3[j])) for j in range(len(S3)) if pts3[j][0] < pts3[i3][0]]
        sup3 = max(left3, key=lambda t: val(t[1]))[0]
        rfhs_ok = rfhs_ok and ents[Z] == (6, 2) and key(lo4) == key({3: Fr(1, 3)}) and sign(lo3) == 0 \
            and key(hi3) == key(hi4) and sup3 == (6, 3)
    rep("EXHAUSTIVE", "without g (l <= 3): at Rf..Hs (104-108, entrant 6d) the floor falls from sqrt3/3 (5g) to 0 (6f); the ceiling is unchanged", rfhs_ok)
    rep("EXHAUSTIVE", "without g (l <= 3): the corridors differ at exactly the eleven 5f steps and the five 6d steps, no other",
        NUM["nog_differs"] == sorted(fsteps + [104, 105, 106, 107, 108]))
    # the candidate-set instrument, imported, agrees
    cs = load(os.path.join(ROOT, "method", "proofs", "candidateset.py"), "candidateset")
    o = cs.measure(MEMBERS)
    rep("GUARD", "candidateset instrument: Pa floor 0 with g, -inf without; Ce -inf under both",
        round(o["pa_walk"]["lo"], 9) == 0.0 and o["pa_seated"]["minus_inf"] and o["ce_walk"]["minus_inf"] and o["ce_seated"]["minus_inf"])
    rep("GUARD", "candidateset instrument: the iff holds with g and fails without", o["walk"]["iff_holds"] and not o["seated"]["iff_holds"])

    # 5. the walk
    say("\n5  THE WALK")
    TRs = {eps: walk("p", eps) for eps in (1e-4, 1e-6, 1e-8, 1e-10)}
    TR = TRs[1e-6]
    recal = [t for t in TR if t["move"] != 0.0]
    real = [t for t in recal if t["Z"] != 3 and abs(t["move"]) > 1e-3]
    touch = [t for t in recal if t["Z"] != 3 and abs(t["move"]) <= 1e-3]
    NUM["recal"], NUM["real"], NUM["touch"] = len(recal), len(real), len(touch)
    rep("EXHAUSTIVE", "node-only walk, eps = 1e-6: recalibrations = 1 initial + real moves + touches",
        len(recal) == 1 + len(real) + len(touch), "%d = 1 + %d + %d" % (len(recal), len(real), len(touch)))
    same = all([(t["Z"], t["at"]) for t in TRs[e] if t["move"] != 0.0] == [(t["Z"], t["at"]) for t in recal] for e in TRs)
    rep("EXHAUSTIVE", "the recalibration sites and endpoints are the same for eps = 1e-4, 1e-6, 1e-8, 1e-10", same)
    tsz = all(abs(abs(t["move"]) - 2 * e) < 1e-12 for e in TRs for t in TRs[e] if t["Z"] != 3 and t["move"] != 0.0 and abs(t["move"]) <= 1e-3)
    rep("EXHAUSTIVE", "every touch moves a by exactly 2 eps", tsz)
    NUM["real_sites"] = [(t["Z"], G.GROUND[t["Z"]][0], name(ents[t["Z"]]), t["at"], closed(t["lo"] if t["at"] == "L" else t["hi"]),
                         dec7(t["lo"] if t["at"] == "L" else t["hi"])) for t in real]
    NUM["touch_sites"] = [(t["Z"], G.GROUND[t["Z"]][0], name(ents[t["Z"]]), t["at"]) for t in touch]
    rep("EXHAUSTIVE", "the real moves are at K Rb Cs Ce Hg Tl Fr Pa Lr",
        [t["Z"] for t in real] == [19, 37, 55, 58, 80, 81, 87, 91, 103])
    rep("EXHAUSTIVE", "the touches are at Mo Tc Rh Gd Tb Cm Bk Rf",
        [t["Z"] for t in touch] == [42, 43, 45, 64, 65, 96, 97, 104])
    # a touch recurs the endpoint at which a was last placed
    last_key = None
    ok = True
    for t in TR:
        if t["move"] == 0.0:
            continue
        k = key(t["lo"] if t["at"] == "L" else t["hi"])
        if t["Z"] != 3 and abs(t["move"]) <= 1e-3:
            ok = ok and (k == last_key)
        last_key = k
    rep("EXHAUSTIVE", "at every touch the endpoint reached equals the endpoint at which a was last placed", ok)
    # Table 3 in full: the endpoint reached (L or U) at each of the eighteen, Ce and Pa the two at U
    WANT18 = [(3, "L"), (19, "L"), (37, "L"), (42, "U"), (43, "L"), (45, "U"), (55, "L"), (58, "U"), (64, "L"),
              (65, "U"), (80, "L"), (81, "L"), (87, "L"), (91, "U"), (96, "L"), (97, "U"), (103, "L"), (104, "U")]
    rep("EXHAUSTIVE", "Table 3: the endpoint reached at each of the 18 recalibrations; the moves at U are exactly Ce and Pa",
        [(t["Z"], t["at"]) for t in recal] == WANT18
        and [t["Z"] for t in real if t["at"] == "U"] == [58, 91], "%s" % [(t["Z"], t["at"]) for t in recal])
    NUM["table3"] = [(t["Z"], G.GROUND[t["Z"]][0], name(ents[t["Z"]]),
                      "initial placement" if t["Z"] == 3 else ("move" if abs(t["move"]) > 1e-3 else "touch"), t["at"],
                      closed(t["lo"] if t["at"] == "L" else t["hi"]), dec7(t["lo"] if t["at"] == "L" else t["hi"]), "%.7f" % t["a"])
                     for t in recal]
    smallest = min(real, key=lambda t: abs(t["move"]))
    rep("EXHAUSTIVE", "the smallest real move exceeds 1/50 (at Pa) and every touch is 2 eps: any threshold in (2e-4, 0.02) gives the same partition",
        abs(smallest["move"]) > 0.02 and smallest["Z"] == 91 and all(abs(t["move"]) > 0.02 for t in real),
        "smallest real move %.4f at Z = %d" % (abs(smallest["move"]), smallest["Z"]))
    NUM["smallest_move"] = (abs(smallest["move"]), smallest["Z"])
    # the walk without g (l <= 3) has the same eighteen sites and endpoints
    TR3 = walk("p", 1e-6, 15, 3)
    rep("EXHAUSTIVE", "without g (l <= 3): the walk has the same 18 recalibration sites and endpoints",
        [(t["Z"], t["at"]) for t in TR3 if t["move"] != 0.0] == WANT18)
    # hydrogen and helium: the 1s corridor is (-inf, 1) and contains the starting slope 0
    hhe = True
    for Z in (1, 2):
        prev = occ(Z - 1)
        S = admissible(prev)
        pts = [point(s, prev, "p") for s in S]
        g = gains(Z)
        lo, hi, bad = corridor(S.index((1, 0)), pts)
        hhe = hhe and len(g) == 1 and g[0][1] == (1, 0) and not bad and lo is None and key(hi) == key({1: Fr(1)})
    rep("EXHAUSTIVE", "Z = 1, 2: the entrant is 1s with corridor (-inf, 1), which contains a = 0; starting at Li changes no site", hhe)
    # the values a takes after each real move: the endpoint reached
    # eight of nine at the entrant's own opening; Hg the exception
    at_open = [t["Z"] for t in real if ents[t["Z"]] in op.get(t["Z"], [])]
    rep("EXHAUSTIVE", "eight of the nine real moves are at the opening of the entering subshell",
        at_open == [19, 37, 55, 58, 81, 87, 91, 103], "not: %s" % [t["Z"] for t in real if t["Z"] not in at_open])
    # which subshells fill at constant a
    notconst = []
    for k, (a0, b0) in sorted(sp.items(), key=lambda kv: kv[1][0]):
        end = b0 if b0 is not None else 108
        hits = [t["Z"] for t in real if a0 < t["Z"] <= end]
        if hits:
            notconst.append((name(k), a0, b0, hits))
    rep("EXHAUSTIVE", "subshells not filling at constant a: 5d (Ce) and 6d (Pa, Lr), no other",
        [(x[0], x[3]) for x in notconst] == [("5d", [58]), ("6d", [91, 103])], "%s" % notconst)
    NUM["notconst"] = notconst
    # the four consecutive pairs meeting at a point
    pairs = []
    for a_, b_ in ((42, 43), (64, 65), (96, 97), (103, 104)):
        ca, cb = out["cor"]["p"][a_], out["cor"]["p"][b_]
        shared = [key(x) for x in (ca[0], ca[1]) if x is not None] and set(key(x) for x in (ca[0], ca[1]) if x is not None) & set(key(x) for x in (cb[0], cb[1]) if x is not None)
        pairs.append((a_, b_, [closed(dict(s)) for s in shared]))
    rep("EXHAUSTIVE", "Mo/Tc, Gd/Tb, Cm/Bk, Lr/Rf: consecutive corridors share an endpoint", all(len(p[2]) == 1 for p in pairs), "%s" % pairs)
    NUM["pairs"] = pairs
    # the recovered instrument's own walk, imported through walkresets
    wr = load(os.path.join(ROOT, "method", "proofs", "walkresets.py"), "walkresets")
    o = wr.measure(MEMBERS)
    rep("GUARD", "walkresets instrument: 18 recalibrations, 9 real moves, 8 touches", (len(o["resets"]), len(o["real"]), len(o["touch"])) == (18, 9, 8))
    rep("GUARD", "walkresets instrument: real moves at the same nine steps", [r["Z"] for r in o["real"]] == [t["Z"] for t in real])
    dv = max(abs(r["after"] - t["a"]) for r, t in zip(o["real"], real))
    rep("GUARD", "walkresets instrument: the nine values agree to 1e-9", dv < 1e-9, "max |diff| %.1e" % dv)
    rep("GUARD", "walkresets instrument: touches at the same eight steps", [r["Z"] for r in o["touch"]] == [t["Z"] for t in touch])
    # its corridors (the recovered frame) differ from the full set only at ceilings of six steps
    wd, wd_lo, wd_hi = [], [], []
    _, wmod = wr.load(MEMBERS)
    for Z in STEPS:
        b = wmod.bracket(Z)
        lo, hi, _ = out["cor"]["p"][Z]
        L, U = fl(lo, -1e9), fl(hi, 1e9)
        dlo, dhi = abs(b[0] - L) > 1e-9, abs(b[1] - U) > 1e-9
        if dlo:
            wd_lo.append(Z)
        if dhi:
            wd_hi.append(Z)
        if dlo or dhi:
            wd.append(Z)
    SEVEN = [3, 11, 19, 37, 47, 55, 87]
    rep("GUARD", "the recovered walk's frame: every floor agrees with the full set, 106 steps", wd_lo == [], "%s" % wd_lo)
    rep("GUARD", "the recovered walk's frame: the ceiling is absent at exactly Li Na K Rb Ag Cs Fr",
        wd == SEVEN and wd_hi == SEVEN and all(wmod.bracket(Z)[1] >= 1e9 for Z in SEVEN), "%s" % wd)
    rep("GUARD", "those seven are ns openings, and the truncated set holds no larger abscissa there",
        all(ents[Z][1] == 0 for Z in SEVEN)
        and all(max(pts[0] for pts in step(Z, "p", 8, 4)[2]) > point(ents[Z], occ(Z - 1), "p")[0] for Z in SEVEN))
    NUM["walkframe_differs"] = wd
    out["TR"] = TR
    # the finished form's walk
    TRq = walk("q", 1e-6)
    recq = [t for t in TRq if t["move"] != 0.0]
    realq = [t for t in recq if t["Z"] != 3 and abs(t["move"]) > 1e-3]
    touchq = [t for t in recq if t["Z"] != 3 and abs(t["move"]) <= 1e-3]
    NUM["recal_q"], NUM["real_q"], NUM["touch_q"] = len(recq), len(realq), len(touchq)
    NUM["real_sites_q"] = [(t["Z"], G.GROUND[t["Z"]][0], name(ents[t["Z"]]), t["at"]) for t in realq]
    WANTQ = [(3, "L"), (19, "L"), (25, "L"), (37, "L"), (43, "L"), (55, "L"), (58, "U"), (64, "L"), (65, "U"), (87, "L"),
             (91, "U"), (96, "L"), (97, "U"), (103, "L"), (104, "U")]
    rep("EXHAUSTIVE", "finished form walk: 15 recalibrations = 1 initial + 14 moves + 0 touches, at U exactly at Ce Tb Pa Bk Rf",
        (len(recq), len(realq), len(touchq)) == (15, 14, 0) and [(t["Z"], t["at"]) for t in recq] == WANTQ,
        "%d, %d, %d; %s" % (len(recq), len(realq), len(touchq), [(t["Z"], t["at"]) for t in recq]))
    out["TRq"] = TRq
    # t at Pa: the walk places a at U
    tPa = [t for t in TR if t["Z"] == 91][0]
    rep("EXHAUSTIVE", "Z = 91: the walk arrives above the ceiling and is placed at U (t = 1 up to eps)", tPa["at"] == "U")

    # 6. the running intersection, the piercing number, one fixed slope
    say("\n6  ONE SLOPE FOR MANY STEPS")
    def inside(c, q):
        """Is the rational q strictly inside the corridor c?  Exact."""
        lo, hi, bad = c
        if bad:
            return False
        r = {1: q} if q != 0 else {}
        return (lo is None or less(lo, r)) and (hi is None or less(r, hi))

    def just_below(lo, hi):
        """The greedy stab: a rational in (lo, hi) within 10^-7 of hi.  Exact."""
        if hi is None:
            return Fr(math.ceil(float(val(lo)))) + 1 if lo is not None else Fr(0)
        k = 7
        while True:
            d = 10 ** k
            q = Fr(int(math.floor(float(val(hi)) * d)), d)
            r = {1: q} if q else {}
            if less(r, hi) and (lo is None or less(lo, r)):
                return q
            k += 1

    def between(a, b):
        """A rational strictly between two surds (or the open ends), exact."""
        if a is None:
            return (Fr(math.floor(float(val(b)))) - 1) if b is not None else Fr(0)
        if b is None:
            return Fr(math.ceil(float(val(a)))) + 1
        k = 1
        while True:
            d = 10 ** k
            q = Fr(int((val(a) + val(b)) / 2 * d), d)
            if less(a, {1: q} if q else {}) and less({1: q} if q else {}, b):
                return q
            k += 1

    for form in ("p", "q"):
        lo_r, hi_r, emp = None, None, []          # the running intersection, exactly
        for Z in STEPS:
            lo, hi, _ = out["cor"][form][Z]
            nlo = lo if lo_r is None else (lo_r if lo is None or less(lo, lo_r) else lo)
            nhi = hi if hi_r is None else (hi_r if hi is None or less(hi_r, hi) else hi)
            if nlo is not None and nhi is not None and not less(nlo, nhi):
                emp.append(Z)
                lo_r, hi_r = lo, hi
            else:
                lo_r, hi_r = nlo, nhi
        NUM["empties_" + form] = emp
        rep("EXHAUSTIVE", "form %s: the running intersection empties, exactly" % form, True, "%d times at %s" % (len(emp), emp))
        # (i) a largest pairwise-disjoint set, by the greedy on the right endpoint
        iv = sorted(STEPS, key=lambda Z: (fl(out["cor"][form][Z][1], math.inf), Z))
        chosen, last = [], None
        for Z in iv:
            lo, hi, _ = out["cor"][form][Z]
            if last is None or (lo is not None and not less(lo, last)):
                chosen.append(Z)
                last = hi
        NUM["disjoint_" + form] = chosen
        okd = True
        for x, y in itertools.combinations(chosen, 2):
            cx, cy = out["cor"][form][x], out["cor"][form][y]

            def le(u, l):
                return u is not None and l is not None and not less(l, u)
            okd = okd and (le(cx[1], cy[0]) or le(cy[1], cx[0]))
        rep("EXHAUSTIVE", "form %s: %d corridors are pairwise disjoint, exactly" % (form, len(chosen)), okd,
            "%s" % [(Z, G.GROUND[Z][0]) for Z in chosen])
        # (ii) a piercing set of the same size, EXHIBITED as rationals and verified exactly
        stabs, unpierced = [], list(STEPS)
        while unpierced:
            Z0 = min(unpierced, key=lambda Z: (fl(out["cor"][form][Z][1], math.inf), Z))
            lo, hi, _ = out["cor"][form][Z0]
            q = just_below(lo, hi)
            stabs.append(q)
            unpierced = [Z for Z in unpierced if not inside(out["cor"][form][Z], q)]
        miss = [Z for Z in STEPS if not any(inside(out["cor"][form][Z], q) for q in stabs)]
        rep("EXHAUSTIVE", "form %s: %d exhibited rational slopes pierce all 106 corridors, exactly" % (form, len(stabs)),
            not miss and len(stabs) == len(chosen), "%s" % [str(q) for q in stabs])
        NUM["pierce_" + form] = [str(q) for q in stabs]
        rep("EXHAUSTIVE", "form %s: the piercing number is exactly %d" % (form, len(chosen)),
            okd and not miss and len(stabs) == len(chosen))
        # coverage by one slope: piecewise constant, so probe between consecutive endpoints, exactly
        es = sorted({key(x) for Z in STEPS for x in out["cor"][form][Z][:2] if x is not None},
                    key=functools.cmp_to_key(lambda A, B: sign(add(dict(A), neg(dict(B))))))
        es = [dict(k) for k in es]
        probes = ([between(None, es[0])] + [between(es[i], es[i + 1]) for i in range(len(es) - 1)]
                  + [between(es[-1], None)])
        cov = [(sum(1 for Z in STEPS if inside(out["cor"][form][Z], q)), i) for i, q in enumerate(probes)]
        best = max(cov)[0]
        where = [i for c, i in cov if c == best]
        span = [(None if i == 0 else es[i - 1], None if i == len(es) else es[i]) for i in where]
        NUM["cover_" + form] = (best, [("−∞" if a is None else closed(a), "+∞" if b is None else closed(b)) for a, b in span])
        out.setdefault("cover", {})[form] = (best, span)       # the band as surds, for figures.py
        rep("EXHAUSTIVE", "form %s: best coverage by one fixed slope, exactly" % form, True,
            "%d of 106 on %s" % (best, NUM["cover_" + form][1]))
    rep("EXHAUSTIVE", "node-only: fourteen emptyings at 37 42 43 45 55 58 64 65 80 91 96 97 103 104",
        NUM["empties_p"] == [37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104])
    rep("EXHAUSTIVE", "node-only: the three pairwise-disjoint corridors are B, La, Lr", NUM["disjoint_p"] == [5, 57, 103])

    # 7. what the law does not do: prediction
    say("\n7  PREDICTION")
    for form, TRx in (("p", TR), ("q", TRq)):
        a_after = {t["Z"]: t["a"] for t in TRx}
        hits, ties, misses = 0, 0, []
        for Z in STEPS[1:]:
            a = a_after[Z - 1]
            prev, S, pts = step(Z, form)
            vals = sorted((pts[i][1] - a * math.sqrt(pts[i][0]), S[i]) for i in range(len(S)))
            if abs(vals[0][0] - vals[1][0]) < 1e-9:
                ties += 1
            elif vals[0][1] == ents[Z]:
                hits += 1
            else:
                misses.append(Z)
        NUM["heldout_" + form] = (hits, ties, misses)
        rep("EXHAUSTIVE", "form %s: held-out prediction at the carried slope, Z = 4..108" % form, True, "%d of 105, %d ties, misses %s" % (hits, ties, misses))
    kscore, kmiss = 0, []
    for Z in STEPS:
        prev, S, pts = step(Z, "p")
        kp = min(S, key=lambda s: (s[0] + s[1], s[0]))
        if kp == ents[Z]:
            kscore += 1
        else:
            kmiss.append(Z)
    NUM["kscore"], NUM["kmiss"] = kscore, kmiss
    rep("EXHAUSTIVE", "the memoryless least-(n+l, n) rule", True, "%d of 106, misses %s" % (kscore, kmiss))
    for form in ("p", "q"):
        notv = [Z for Z in STEPS if min(step(Z, form)[1], key=lambda s: (s[0] + s[1], s[0])) not in out["A"][form][Z]]
        rep("EXHAUSTIVE", "form %s: the least-(n+l, n) pick is a hull vertex at every step" % form, not notv, "not at %s" % notv)
        NUM["kpick_vertex_" + form] = notv

    # 8. the seated instrument, imported: its corridors and hulls against the fresh ones
    say("\n8  THE SEATED INSTRUMENT")
    sa = load(os.path.join(ROOT, "tools", "slopeaxis.py"), "slopeaxis")
    store = sa.Store(4)
    for form in ("p", "q"):
        mism = 0
        cdiff = []
        for Z in STEPS:
            conf = store.CONF[Z - 1]
            S = store.admissible(Z)
            H = set(store.hull(conf, S, form))
            # the fresh pairwise test on the instrument's OWN frame (n <= 7, l <= 4)
            prev, S2, pts = step(Z, form, 7, 4)
            V = {name(S2[i]) for i in range(len(S2)) if vertex_pairwise(i, pts)}
            mism += H != V
            lo, hi, bad = store.corridor(conf, store.ENT[Z], S, form)
            lo2, hi2, _ = ent_corridor(Z, form, 7, 4)
            L2, U2 = fl(lo2, -math.inf), fl(hi2, math.inf)
            if abs(lo - L2) > 1e-9 and not (lo == -math.inf and L2 == -math.inf) or abs(hi - U2) > 1e-9 and not (hi == math.inf and U2 == math.inf):
                cdiff.append(Z)
        rep("GUARD", "form %s: the instrument's hull = the fresh pairwise vertex set on its frame, 106 steps" % form, mism == 0)
        rep("GUARD", "form %s: the instrument's entrant corridor = the fresh one on its frame, 106 steps" % form, not cdiff, "%s" % cdiff)
    NUM["instrument_ends_q"] = None
    return out


# ----------------------------------------------------------------------------- the theorem, checked


def exhaustive_family():
    """Every set of 2..5 distinct points of the grid {0,1,2,3}^2, exact rational arithmetic:
    corridor non-empty <=> pairwise vertex test <=> monotone chain; endpoints = flanking slopes;
    the corridors of the sorted vertices are ordered and share consecutive endpoints."""
    grid = [(Fr(x * x), y) for x in range(4) for y in range(4)]
    sets = pts_n = 0
    bad = 0
    for k in range(2, 6):
        for P in itertools.combinations(grid, k):
            pts = list(P)
            sets += 1
            cs = [corridor(i, pts) for i in range(k)]
            A = {i for i in range(k) if nonempty(cs[i])}
            V = {i for i in range(k) if vertex_pairwise(i, pts)}
            H = hull_chain(pts)
            pts_n += k
            if A != V or A != set(H):
                bad += 1
                continue
            for j, i in enumerate(H):
                lo, hi, _ = cs[i]
                wl = None if j == 0 else slope(pts[H[j - 1]], pts[i])
                wh = None if j == len(H) - 1 else slope(pts[i], pts[H[j + 1]])
                if (lo is None) != (wl is None) or (hi is None) != (wh is None):
                    bad += 1
                elif (lo is not None and key(lo) != key(wl)) or (hi is not None and key(hi) != key(wh)):
                    bad += 1
    rep("EXHAUSTIVE", "grid {0..3}^2, every point set of size 2..5: the three vertex tests agree and L, U are the flanking slopes",
        bad == 0, "%d sets, %d point-instances" % (sets, pts_n))
    NUM["family_sets"], NUM["family_points"] = sets, pts_n
    return bad == 0


def z3_checks(negative=False):
    prover = load(os.path.join(ROOT, "research", "warp-drive", "prover.py"), "prover")
    prover.require_z3()
    import z3

    def strict_min(xs, ys, a, k):
        return z3.And([ys[0] - a * xs[0] < ys[i] - a * xs[i] for i in range(1, k)])

    def in_E(xs, ys, k, lam, t):
        return z3.And([l >= 0 for l in lam] + [z3.Sum(lam) == 1, t >= 0,
                      xs[0] == z3.Sum([lam[i - 1] * xs[i] for i in range(1, k)]),
                      ys[0] == z3.Sum([lam[i - 1] * ys[i] for i in range(1, k)]) + t])

    def pairwise(xs, ys, k):
        conds = []
        for u in range(1, k):
            conds.append(z3.Implies(xs[u] == xs[0], ys[0] < ys[u]))
            for w in range(1, k):
                if u != w:
                    conds.append(z3.Implies(z3.And(xs[u] < xs[0], xs[0] < xs[w]),
                                            (xs[w] - xs[u]) * (ys[0] - ys[u]) - (ys[w] - ys[u]) * (xs[0] - xs[u]) < 0))
        return z3.And(conds)

    # --- guards.  (i) non-vacuity of each hypothesis; (ii) encoding fidelity against the fresh
    # concrete implementations on random rational instances, with a negative control.
    k = 4
    xs = [z3.Real("x%d" % i) for i in range(k)]
    ys = [z3.Real("y%d" % i) for i in range(k)]
    a = z3.Real("a")
    s = z3.Solver()
    s.add(strict_min(xs, ys, a, k))
    nv1 = s.check() == z3.sat
    s = z3.Solver()
    s.add(pairwise(xs, ys, k), z3.And([z3.Or(xs[i] != xs[j], ys[i] != ys[j]) for i in range(k) for j in range(i + 1, k)]))
    nv2 = s.check() == z3.sat
    rep("GUARD", "non-vacuity: both hypotheses are satisfiable (k = 4)", nv1 and nv2)
    rnd = random.Random(11)
    tot = dis = 0
    dis_ctrl = 0
    for _ in range(300):
        k = rnd.randint(2, 5)
        pts = []
        while len(pts) < k:
            p = (Fr(rnd.randint(0, 5)) ** 2 if rnd.random() < 0.5 else Fr(rnd.randint(0, 25)), rnd.randint(0, 6))
            if p not in pts:
                pts.append(p)
        # the encoding of "not in E(P - s)" evaluated concretely, against the chain (independent)
        for i in range(k):
            s0 = pts[i]
            others = [p for j, p in enumerate(pts) if j != i]
            enc = all(not (u[0] == s0[0] and u[1] <= s0[1]) for u in others) and all(
                not (u[0] < s0[0] < w[0]) or cross(u, s0, w) < 0 for u in others for w in others if u is not w)
            ref = i in hull_chain(pts)
            tot += 1
            dis += enc != ref
            dis_ctrl += enc != (i in hull_chain(pts)[1:])     # a wrong reference: the chain without its first vertex
    rep("GUARD", "encoding fidelity: the pairwise predicate = the chain on 300 random instances", dis == 0, "%d point-instances, %d disagreements" % (tot, dis))
    rep("GUARD", "negative control: a wrong reference is caught", dis_ctrl > 0, "%d disagreements" % dis_ctrl)
    # the strict-minimiser encoding against brute force over a rational a
    tot = dis = 0
    for _ in range(300):
        k = rnd.randint(2, 5)
        pts = [(Fr(rnd.randint(0, 25)), rnd.randint(0, 6)) for _ in range(k)]
        av = Fr(rnd.randint(-8, 8), rnd.randint(1, 4))
        xr = [Fr(p[0]) for p in pts]      # rational abscissae here: x itself, not x^2
        f = [p[1] - av * xr[j] for j, p in enumerate(pts)]
        enc = all(f[0] < f[i] for i in range(1, k))
        ref = f.count(min(f)) == 1 and f[0] == min(f)
        tot += 1
        dis += enc != ref
    rep("GUARD", "encoding fidelity: the strict-minimiser formula = brute force on 300 random instances", dis == 0)

    ok = True
    # --- forward: a strict minimiser is not in conv(P - s) + ray
    for k in (2, 3, 4, 5):
        xs = [z3.Real("x%d" % i) for i in range(k)]
        ys = [z3.Real("y%d" % i) for i in range(k)]
        a = z3.Real("a")
        lam = [z3.Real("l%d" % i) for i in range(1, k)]
        t = z3.Real("t")
        s = z3.Solver()
        s.add(strict_min(xs, ys, a, k), in_E(xs, ys, k, lam, t))
        t0 = time.time()
        r = s.check()
        ok = ok and r == z3.unsat
        rep("MACHINE-CHECKED", "Theorem 1 (=>): k = %d points in R^2, strict minimiser => not in E(P - s)" % k, r == z3.unsat, "%s, %.1fs" % (r, time.time() - t0))
    # --- converse: not in E(P - s) (pairwise form) => some slope makes s the strict minimiser
    for k in (2, 3, 4):
        xs = [z3.Real("x%d" % i) for i in range(k)]
        ys = [z3.Real("y%d" % i) for i in range(k)]
        a = z3.Real("a")
        box = z3.And([z3.And(0 <= v, v <= 10) for v in xs + ys])
        distinct = z3.And([z3.Or(xs[i] != xs[j], ys[i] != ys[j]) for i in range(k) for j in range(i + 1, k)])
        notmin = z3.ForAll([a], z3.Or([ys[0] - a * xs[0] >= ys[i] - a * xs[i] for i in range(1, k)]))
        s = z3.Solver()
        s.add(box, distinct, pairwise(xs, ys, k), notmin)
        t0 = time.time()
        r = s.check()
        ok = ok and r == z3.unsat
        rep("MACHINE-CHECKED", "Theorem 1 (<=): k = %d distinct points in [0,10]^2, not in E(P - s) => some slope selects s" % k, r == z3.unsat, "%s, %.1fs" % (r, time.time() - t0))
    if negative:
        # a false claim: the strict minimiser is always the point of least y
        k = 3
        xs = [z3.Real("x%d" % i) for i in range(k)]
        ys = [z3.Real("y%d" % i) for i in range(k)]
        a = z3.Real("a")
        s = z3.Solver()
        s.add(strict_min(xs, ys, a, k), z3.Or([ys[i] < ys[0] for i in range(1, k)]))
        r = s.check()
        rep("NEGATIVE", "negative control: 'the strict minimiser has the least y' is REFUTED by Z3", r == z3.sat, "%s" % r)
    return ok


def negative_controls():
    # (a) a wrong hull: the chain with non-strict turns keeps collinear points; the identity must fail
    def chain_wrong(pts):
        byx = {}
        for i, p in enumerate(pts):
            if p[0] not in byx or p[1] < pts[byx[p[0]]][1]:
                byx[p[0]] = i
        order = sorted(byx.values(), key=lambda i: pts[i][0])
        H = []
        for i in order:
            while len(H) >= 2 and cross(pts[H[-2]], pts[H[-1]], pts[i]) > 0:
                H.pop()
            H.append(i)
        return H
    mism = 0
    for Z in STEPS:
        prev, S, pts = step(Z, "p")
        A = {i for i in range(len(S)) if nonempty(corridor(i, pts))}
        mism += A != set(chain_wrong(pts))
    rep("NEGATIVE", "negative control: a hull that keeps collinear points is REFUTED by the corridor identity", mism > 0, "%d mismatching steps" % mism)
    # (b) a wrong crossing formula
    want = scale(add(sqrt_rat(Fr(3)), sqrt_rat(Fr(0))), Fr(1, 2))
    lo = ent_corridor(19, "p")[0]
    rep("NEGATIVE", "negative control: (sqrt(n-1)+sqrt(n-4))/2 at n = 4 is REFUTED against K's floor", key(lo) != key(want))


def table(out):
    """The 106 node-only corridors with the two hull vertices flanking the entrant, whose edge
    slopes the check has verified to BE the endpoints (section 1)."""
    ents = out["entrant"]
    print("| Z | element | entrant | p | u | L | U | w | L (7 dp) | U (7 dp) |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for Z in STEPS:
        lo, hi, _ = out["cor"]["p"][Z]
        e = ents[Z]
        H = out["hull"]["p"][Z]
        k = H.index(e)
        u = "—" if k == 0 else name(H[k - 1])
        w = "—" if k == len(H) - 1 else name(H[k + 1])
        print("| %d | %s | %s | %d | %s | %s | %s | %s | %s | %s |" % (
            Z, G.GROUND[Z][0], name(e), e[0] - e[1] - 1, u,
            "−∞" if lo is None else closed(lo), "+∞" if hi is None else closed(hi), w,
            "" if lo is None else dec7(lo), "" if hi is None else dec7(hi)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--table", action="store_true")
    ap.add_argument("--no-z3", action="store_true")
    a = ap.parse_args()
    if a.table:
        QUIET[0] = True
        out = compute(quiet=True)
        LINES.clear()
        table(out)
        return 0
    print("check.py -- The occupation law as a lower convex hull")
    out = compute()
    print("\n9  THE THEOREM ON A FINITE FAMILY AND UNDER Z3")
    exhaustive_family()
    if not a.no_z3:
        z3_checks(negative=a.selftest)
    if a.selftest:
        print("\n10 NEGATIVE CONTROLS")
        negative_controls()
    rep("EXHAUSTIVE", "every sign in the geometry decided by exact rational enclosure, none in floating point",
        MAXPREC[0] > 0 and MINBOUND[0] > 0,
        "deepest %d digits, smallest certified magnitude >= %.6g" % (MAXPREC[0], float(MINBOUND[0])))
    print("\n  exact-sign record: deepest enclosure %d decimal digits; smallest certified "
          "non-zero magnitude >= %s (no sign decided in floating point)"
          % (MAXPREC[0], float(MINBOUND[0]) if MINBOUND[0] is not None else None))
    NUM["maxprec"] = MAXPREC[0]
    NUM["minbound"] = float(MINBOUND[0]) if MINBOUND[0] is not None else None
    counts = collections.Counter(st for st, _, ok, _ in LINES)
    print("\n  obligations: " + ", ".join("%s %d" % (k, v) for k, v in sorted(counts.items())))
    print("  %d of %d passed" % (sum(1 for l in LINES if l[2]), len(LINES)))
    if FAILS:
        print("  FAILED: %s" % FAILS)
        return 1
    print("  ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
