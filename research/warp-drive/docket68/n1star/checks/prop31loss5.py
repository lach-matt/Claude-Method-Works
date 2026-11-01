#!/usr/bin/env python3
"""prop31loss5: III.I' Proposition 3.1's fixed loss, counted (LOSS-D LD16, D573).

LD16 charges an iota+ round III.G'' Corollary 4.3 (loss d_G + 2) and III.I' Proposition 3.1 (proof5/PART-III-I2-SCRI.md:
165-238), the latter "a fixed loss through L~ (loss 2)". III.J'' (g) (proof5/PART-III-J3-TAME.md:173-176) makes
Proposition 3.1 a composition of the face integrations (d) (III.A Lemma 1.2: loss 0, J3:139-141), of (z - 3/2 -
Abar)^-1 ((c), bounded, loss 0, J3:124-128) and of L~ ((b), loss 2), "in finitely many steps whose number is fixed by
l_I, l_+ and the index sets". The proof's steps: Step 1 removes the exceptional slot-7 term (I2:198-212) and leaves f -
L_b v; Step 2 removes, window by window [mu, mu + 1) (mu the least real part left), the terms (z, k) of the I+-expansion
with Re z <= l_I (I2:216-235). Within a window the z's are solved from the same f (L~ shifts by integers >= 1, beyond
the window, I2:226-229), so one window is one application of L_b; the log orders of one z, k, k - 1, ..., 0, are taken
in turn (I2:230-232), each through f - L_b(...). So the chain has 1 + J + Lg applications of L_b, J the windows that
meet {Re z <= l_I}, Lg the log steps, and the remainder (3.1) is 2(1 + J + Lg) derivatives below f (u, 2 less).

E^C_I is an index set of III.C Definition 3.1 (proof5/PART-III-C-EXTERIOR.md:149-158): min Re > 3/2 + 2 gamma_Ups and
E^tot + (E^tot - 1) in E^C_I, E^tot := E^C_I u {3/2 + s : s in sigma_Ups}, sigma_Ups = {0, (1 - e_Ups) gamma_Ups,
gamma_Ups, 2 gamma_Ups}; III.C Lemma 3.2 (e) gives a least one containing any admissible seed.

  Q1 (exact) the least E^C_I (empty seed) below 3.6 at e_Ups = gamma_Ups = 1/100: its points are 1 + sum n_i (1/2 + s_i)
     over sum n_i >= 2, all of log order 0: 9, 16, 25 points about 2, 2.5 and 3, 36 about 3.5; (2, 0), (3, 0) in it and
     E^C_I + 1/2 in E^C_I below 3.6 (III.C Lemma 3.2 (a)).
  Q2 (exact) for every l_I in (3, 3.5099), off the exclusion set: the windows meeting {Re z <= l_I} are [2, 3) and
     [3, 4), J = 2, no log steps: 1 + J = 3 applications of L_b, loss 6 for the remainder (3.1), 4 for u. The same J = 2
     for every admissible seed with min Re E^C_I in (3/2 + 2 gamma_Ups, 2] and no log term below l_I.
  Q3 (control) a seed with a log term below l_I, (2.3, 1): its two log orders are taken in turn, one more step.

Labels: computed (exact rationals) for Q1-Q3; deduced (the reading of I2's proof and J3 (g) above) for the step count.

    python3 checks/prop31loss5.py
"""
import sys
from fractions import Fraction as Fr

E_UPS = G_UPS = Fr(1, 100)
SIGMA = [Fr(0), (1 - E_UPS) * G_UPS, G_UPS, 2 * G_UPS]
TOP = Fr(36, 10)


def least_ECI(seed=(), top=TOP):
    """the least index set of III.C Definition 3.1 (2)-(3) containing seed, below top: {(z, k)} with index-set sums
    (z, k) + (w, j) = (z + w, k + j), and the larger log order kept at a repeated z"""
    E = {}
    for z, k in seed:
        E[z] = max(E.get(z, -1), k)
    base = {Fr(3, 2) + s: 0 for s in SIGMA}
    while True:
        tot = dict(base)
        for z, k in E.items():
            tot[z] = max(tot.get(z, -1), k)
        new = dict(E)
        for a, ka in tot.items():
            for b, kb in tot.items():
                z = a + b - 1
                if z <= top:
                    new[z] = max(new.get(z, -1), ka + kb)
        if new == E:
            return E
        E = new


def chain(E, lI):
    """the L_b applications of Proposition 3.1's proof below l_I: Step 1, one per window, one per extra log order"""
    left = sorted(z for z in E if z <= lI)
    J, logs = 0, 0
    while left:
        mu = left[0]
        win = [z for z in left if z < mu + 1]
        J += 1
        logs += sum(E[z] for z in win)
        left = [z for z in left if z >= mu + 1]
    return J, logs, 1 + J + logs


def main():
    ok = {}
    E = least_ECI()
    pts = sorted(E)
    groups = {}
    for z in pts:
        groups.setdefault(int(2 * z), []).append(z)
    sizes = [len(groups.get(m, [])) for m in (4, 5, 6, 7)]
    half = all(z + Fr(1, 2) in E for z in pts if z + Fr(1, 2) <= TOP)
    nolog = all(k == 0 for k in E.values())
    ok['Q1'] = (sizes == [9, 16, 25, 36] and nolog and Fr(2) in E and Fr(3) in E and half
                and min(pts) > Fr(3, 2) + 2 * G_UPS)
    print('  Q1: the least E^C_I below 3.6: %d points, %s about 2, 2.5, 3, 3.5; all of log order 0: %s; min %s; '
          '(2,0), (3,0) in it; E + 1/2 in E: %s' % (len(pts), sizes, nolog, min(pts), half))
    excl = set(E) | {Fr(3, 2) + s for s in SIGMA}
    lIs = [Fr(3) + Fr(k, 10**4) for k in range(1, 5099) if Fr(3) + Fr(k, 10**4) not in excl]
    res = {chain(E, l) for l in lIs}
    ok['Q2a'] = res == {(2, 0, 3)}
    print('  Q2: over %d values of l_I in (3, 3.5099) off the exclusion set, (J, log steps, L_b applications) = %s: '
          'loss 6 for (3.1), 4 for u' % (len(lIs), sorted(res)))
    seeds = [((Fr(152, 100) + Fr(1, 10**6), 0),), ((Fr(17, 10), 0),), ((Fr(2), 0),), ((Fr(199, 100), 0), (Fr(23, 10), 0))]
    Js = set()
    for sd in seeds:
        Es = least_ECI(sd)
        for l in (Fr(30001, 10**4), Fr(34, 10), Fr(35098, 10**4)):
            if l not in Es:
                Js.add(chain(Es, l)[0])
    ok['Q2b'] = Js == {2}
    print('  Q2: seeds with min Re in (1.52, 2] (%d seeds, l_I = 3.0001, 3.4, 3.5098): J = %s' % (len(seeds), sorted(Js)))
    El = least_ECI(((Fr(23, 10), 1),))
    ok['Q3'] = chain(El, Fr(34, 10))[1] > 0 and chain(El, Fr(34, 10))[2] > 3
    print('  Q3 (control): a seed (2.3, 1): (J, log steps, applications) at l_I = 3.4: %s' % (chain(El, Fr(34, 10)),))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
