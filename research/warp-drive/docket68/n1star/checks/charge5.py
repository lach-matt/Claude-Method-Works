#!/usr/bin/env python3
"""charge5.py -- the charge of a round for larger l_I (verifier 259's item 2, D605), counted by prop31loss5.py's rules.

prop31loss5.py counts, for l_I in (3, 3.5099), the applications of L_b in III.I' Proposition 3.1's proof (Q2: 1 + J +
log steps, J the windows [mu, mu + 1) that meet {Re z <= l_I}) and in the iota+ round's own application (Q4: its error
class 5/2 + sigma_Ups + N_0, no Step 1, no logs), so that a round is charged (d_G + 2) + 2 x (applications) = 15 on (3,
3.5) and 17 on [3.5, 3.5099), d_G = 11. The paper says "more for larger l_I". Here the same rules, with the index sets
continued to Re z <= 7.6, are run for l_I in (3, 7.5), off the exclusion set, on a grid of 10^-3, with d_G taken per l_I
from dg5.py's d25 (LOSS-D (2.5), imported): d_G(l_I) = max over the iota+ window [1.5099, 2 - eps) of d25, which with
delta < eps is 7 + 2 ceil(l_I - Re lam), largest at Re lam = 1.5099 (deduced: the other two ceilings are constant, 0 and
1, on the window), so 7 + 2 ceil(l_I - 1.5099); each call also checks that max over 40 sampled Re lam.

  G1 (exact rationals) On (3, 3.5099) the counts are prop31loss5.py's (Q2: J = 2, no logs, 3 applications; Q4: 1 and 2
     applications, a round 15 and 17, d_G = 11). For larger l_I the least E^C_I stays free of logs (its points are sums
     of log-free points), the window count J of Proposition 3.1 is the number of unit windows from 2 that meet {Re z <=
     l_I}, and the round's count is the number from 5/2: n(l_I) = 1 + floor(l_I - 5/2). The round is charged (d_G + 2) +
     2 n = 11 + 2 ceil(l_I - 1.5099) + 2 floor(l_I - 5/2): 15 on (3, 3.5), 17 on [3.5, 3.5099], then 2 more at each
     later crossing of l_I - 1/2 or l_I - 0.5099 through an integer (19 at l_I = 3.6 and 4, 23 at 4.55 and 5, 27 at 6,
     31 at 7 and 7.4). So the charge grows by 4 for each unit of l_I (2 from d_G, 2 from the round's applications), not
     2 as an earlier version of this program said with d_G frozen at 11; Proposition 3.1's remainder loss is 2 (1 + J).
     A sufficient charge by the proof's own count, not a shown minimum.
  G2 (exact rationals) d_G per l_I reproduces LOSS-D's own points (LOSS-D.md:895-896, 913-915): 9 at l_I = 2.2, 11 on
     the grid in (3, 3.5099], 13 at 3.6, 15 at 4.55 (its eps_I = 1.6 point).
  Controls: G1, windows of width 1/2 in place of 1 (not the proof's) must give exactly J = 3 on (3, 3.5), not
     prop31loss5.py's 2; G2, d_G frozen at 11 must fail to reproduce LOSS-D's points.

Reach: whether the write-out admits l_I above 3.5099 is not decided here (its choice of l_I is among the weights the
paper lists as open); the count says what such an l_I would cost. Labels: computed (exact rationals) on the rules; the
rules are prop31loss5.py's and dg5.py's readings of the proofs; d_G's maximiser on the window is deduced and sampled.

Run: python3 checks/charge5.py   (under a minute)
"""
import math
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prop31loss5 as P                                                         # noqa: E402
from dg5 import d25                                                             # noqa: E402

TOP = Fr(76, 10)
LS, EPS, DELTA = Fr(15099, 10000), Fr(1, 10**6), Fr(1, 10**7)                  # dg5.py's window and delta < eps
LAMS = [LS + (2 - EPS - LS) * Fr(k, 40) for k in range(40)]


def d_G(lI, frozen=False):
    """III.G' Theorem 3.1 (2)'s loss on the iota+ window at l_I (dg5.d25 maximised; 11 if frozen, the old reading)."""
    if frozen:
        return 11
    d = d25(LS, lI, DELTA)
    assert d == max(d25(lam, lI, DELTA) for lam in LAMS)
    return d


def round_class(top=TOP):
    return {Fr(5, 2) + s + n: 0 for s in P.SIGMA for n in range(12) if Fr(5, 2) + s + n <= top}


def chain_w(E, lI, width, step1=True):
    left = sorted(z for z in E if z <= lI)
    J, logs = 0, 0
    while left:
        mu = left[0]
        win = [z for z in left if z < mu + width]
        J += 1
        logs += max(E[z] for z in win)
        left = [z for z in left if z >= mu + width]
    return J, logs, int(step1) + J + logs


def g1(control=False):
    width = Fr(1, 2) if control else Fr(1)
    E = P.least_ECI(top=TOP)
    Er = round_class()
    excl = set(E) | set(Er) | {Fr(3, 2) + s for s in P.SIGMA}
    grid = [Fr(3) + Fr(k, 1000) for k in range(1, 4500) if Fr(3) + Fr(k, 1000) not in excl]
    if control:
        Js = {chain_w(E, l, width)[0] for l in grid if l < Fr(35, 10)}
        print("  G1 control: width-1/2 windows give J = %s on (3, 3.5)" % sorted(Js), flush=True)
        return Js == {2} or Js != {3}
    nolog = all(k == 0 for k in E.values())
    rows, ok = {}, nolog
    for l in grid:
        J, lg, apps = chain_w(E, l, width)
        Jr, lgr, appr = chain_w(Er, l, width, step1=False)
        n = 1 + math.floor(l - Fr(5, 2))
        ok &= appr == n and lgr == 0 and lg == 0
        key = (n, J, d_G(l))
        lo, hi = rows.get(key, (l, l))
        rows[key] = (min(lo, l), max(hi, l))
    small = [l for l in grid if l < Fr(35099, 10**4)]
    base = {chain_w(E, l, width) for l in small} == {(2, 0, 3)}
    rnd = {(d_G(l) + 2) + 2*chain_w(Er, l, width, step1=False)[2] for l in small}
    ok &= base and rnd == {15, 17}
    pts = {Fr(36, 10): 19, Fr(4): 19, Fr(455, 100): 23, Fr(5): 23, Fr(6): 27, Fr(7): 31, Fr(74, 10): 31}
    got = {l: d_G(l) + 2 + 2*chain_w(Er, l, width, step1=False)[2] for l in pts}
    ok &= got == pts
    print("  G1: E^C_I below %s has %d points, all log-free: %s; on (3, 3.5099) prop31loss5.py's counts: %s, rounds %s"
          % (float(TOP), len(E), nolog, base, sorted(rnd)), flush=True)
    for (n, J, d), (lo, hi) in sorted(rows.items(), key=lambda kv: kv[1][0]):
        print("      l_I in [%.3f, %.3f]: d_G %d, round applications %d, charge %d; Proposition 3.1's J = %d, remainder "
              "loss %d" % (lo, hi, d, n, (d + 2) + 2*n, J, 2*(1 + J)), flush=True)
    print("      charges at l_I = %s: %s (growth 4 per unit of l_I)"
          % (", ".join(str(float(l)) for l in pts), ", ".join(str(got[l]) for l in pts)), flush=True)
    return ok


def g2(control=False):
    want = {Fr(22, 10): 9, Fr(36, 10): 13, Fr(455, 100): 15}
    got = {l: d_G(l, frozen=control) for l in want}
    mid = {d_G(Fr(3) + Fr(k, 1000), frozen=control) for k in range(1, 510)}
    ok = got == want and mid == {11}
    print("  G2%s: d_G at l_I = 2.2, 3.6, 4.55: %s (LOSS-D: 9, 13, 15); on (3, 3.5099]: %s (LOSS-D: 11)"
          % (" control (d_G frozen at 11)" if control else "", [got[l] for l in want], sorted(mid)), flush=True)
    return ok


CHECKS = [("G1", g1), ("G2", g2)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
