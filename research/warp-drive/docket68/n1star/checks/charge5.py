#!/usr/bin/env python3
"""charge5.py -- the charge of a round for larger l_I (verifier 259's item 2, D605), counted by prop31loss5.py's rules.

prop31loss5.py counts, for l_I in (3, 3.5099), the applications of L_b in III.I' Proposition 3.1's proof (Q2: 1 + J +
log steps, J the windows [mu, mu + 1) that meet {Re z <= l_I}) and in the iota+ round's own application (Q4: its error
class 5/2 + sigma_Ups + N_0, no Step 1, no logs), so that a round is charged (d_G + 2) + 2 x (applications) = 15 on (3,
3.5) and 17 on [3.5, 3.5099), d_G = 11. The paper says "more for larger l_I". Here the same rules, with the index sets
continued to Re z <= 7.6, are run for l_I in (3, 7.5), off the exclusion set, on a grid of 10^-3.

  G1 (exact rationals) On (3, 3.5099) the counts are prop31loss5.py's (Q2: J = 2, no logs, 3 applications; Q4: 1 and 2
     applications, a round 15 and 17). For larger l_I the least E^C_I stays free of logs (its points are sums of log-free
     points), the window count J of Proposition 3.1 is the number of unit windows from 2 that meet {Re z <= l_I}, and the
     round's count is the number from 5/2: the round is charged 13 + 2 n(l_I), n(l_I) = 1 + floor(l_I - 5/2), so 15,
     17, 19, 21, 23 on the unit intervals from 5/2 (above 3), and Proposition 3.1's remainder loss 2 (1 + J). So the
     charge grows by 2 for each unit of l_I, a sufficient charge by the proof's own count, not a shown minimum.
  Control: windows of width 1/2 in place of 1 (not the proof's) give J = 3 on (3, 3.5), not prop31loss5.py's 2.

Reach: whether the write-out admits l_I above 3.5099 is not decided here (its choice of l_I is among the weights the
paper lists as open); the count says what such an l_I would cost. d_G = 11 is taken as LD16 has it, the same for every
l_I. Labels: computed (exact rationals) on the rules; the rules are prop31loss5.py's reading of the proofs.

Run: python3 checks/charge5.py   (under a minute)
"""
import math
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prop31loss5 as P                                                         # noqa: E402

TOP = Fr(76, 10)
D_G = 11


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
        return {chain_w(E, l, width)[0] for l in grid if l < Fr(35, 10)} == {2}
    nolog = all(k == 0 for k in E.values())
    rows, ok = {}, nolog
    for l in grid:
        J, lg, apps = chain_w(E, l, width)
        Jr, lgr, appr = chain_w(Er, l, width, step1=False)
        n = 1 + math.floor(l - Fr(5, 2))
        ok &= appr == n and lgr == 0 and lg == 0
        key = (n, J)
        lo, hi = rows.get(key, (l, l))
        rows[key] = (min(lo, l), max(hi, l))
    small = [l for l in grid if l < Fr(35099, 10**4)]
    base = {chain_w(E, l, width) for l in small} == {(2, 0, 3)}
    rnd = {(D_G + 2) + 2*chain_w(Er, l, width, step1=False)[2] for l in small}
    ok &= base and rnd == {15, 17}
    print("  G1: E^C_I below %s has %d points, all log-free: %s; on (3, 3.5099) prop31loss5.py's counts: %s, rounds %s"
          % (float(TOP), len(E), nolog, base, sorted(rnd)), flush=True)
    for (n, J), (lo, hi) in sorted(rows.items(), key=lambda kv: kv[1][0]):
        print("      l_I in [%.3f, %.3f]: round applications %d, charge %d; Proposition 3.1's J = %d, remainder loss %d"
              % (lo, hi, n, (D_G + 2) + 2*n, J, 2*(1 + J)), flush=True)
    return ok


CHECKS = [("G1", g1)]


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
