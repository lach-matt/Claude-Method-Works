"""epsind5.py -- LOSS-D LD10 (D420): eps_ind as III.D'' D4:54-57 defines it, at the record's point.

D4:54-57 lets M be "the finite set of real numbers in [-10, 10] of the form Re lam + j", lam an indicial root of
box^Ups (III.D Lemma 4.1 = PART-III-D-GAUGEPOT.md:197-211), j in Z, and fixes eps_ind below half the least distance
between distinct points of M. The roots (GAUGEPOT:200-206): s0: 0, 3 and 1/2 +- (9/4 + z)^(1/2); sl (l >= 1): l + 3,
1 - l and 1/2 +- (1/4 + s_(l,j))^(1/2), s_(l,j) the roots of Q_l(s) = s^2 - (2 + 2 kappa + z) s + kappa (kappa + 1) +
z kappa, kappa = l (l + 2); vl: -l, l + 2. z = 4 e gam^2 = 4e-6 at the record's point (gam = e = 1/100).

  E1 (exact, 50 digits) the non-integer roots sit delta above or below an integer, with delta_l = z l/(2(l + 1)(2l +
     1)) + O(z^2) for l + 1 + delta_l, so delta_l -> 0: read literally (every l), M is not finite and has no positive
     least distance, and no eps_ind > 0 exists. delta_12 = 7.3846e-8 is N1STAR-PROOF.md:4071's "least distance from
     Z" over l <= 12, a cutoff value, not a minimum.
  E2 (exact) the finite reading, roots with real part in [-10, 10]: the least distance between distinct points of M,
     and the least distance of a point of M from Z; so eps_ind < half the former.
  Control: at z = 0 every root is an integer and M = Z cap [-10, 10], least distance 1.
Labels: computed (exact arithmetic, mpmath at 50 digits). Which reading the record intends is not decided here.

    python3 checks/epsind5.py [--selftest]
"""
import sys

from mpmath import floor, mp, mpf, sqrt

mp.dps = 50


def roots(z, lmax):
    out = [(mpf(0), "s0"), (mpf(3), "s0")]
    out += [(mpf(1)/2 + sg*sqrt(mpf(9)/4 + z), "s0") for sg in (1, -1)]
    for l in range(1, lmax + 1):
        k = mpf(l*(l + 2))
        b, c = 2 + 2*k + z, k*(k + 1) + z*k
        disc = sqrt(b*b - 4*c)
        for j, s in ((1, (b - disc)/2), (2, (b + disc)/2)):
            for sg in (1, -1):
                out.append((mpf(1)/2 + sg*sqrt(mpf(1)/4 + s), "s%d,%d%s" % (l, j, "+" if sg > 0 else "-")))
        out += [(mpf(l + 3), "s%d" % l), (mpf(1 - l), "s%d" % l), (mpf(-l), "v%d" % l), (mpf(l + 2), "v%d" % l)]
    return out


def fracs(rs, window=10, tol=mpf(10)**-40):
    """the distinct fractional parts of the points of M from roots with real part in [-window, window]"""
    fr = []
    for lam, name in rs:
        if -window <= lam <= window:
            f = lam - floor(lam)
            if f > 1 - tol:
                f = mpf(0)
            fr.append((f, name))
    fr.sort(key=lambda q: q[0])
    uniq = []
    for f, name in fr:
        if not uniq or f - uniq[-1][0] > tol:
            uniq.append((f, name))
    return uniq


def least(uniq):
    """least distance between distinct points of M (fractional parts on the circle) and least distance from Z"""
    best, arg = mpf(1), None
    n = len(uniq)
    for i in range(n):
        f, a = uniq[i]
        g, b = uniq[(i + 1) % n]
        d = (g - f) if i + 1 < n else (1 + g - f)
        if n > 1 and d < best:
            best, arg = d, (a, b)
    fromZ = min((min(f, 1 - f), name) for f, name in uniq if f > 0)
    return best, arg, fromZ


def main():
    ok = {}
    z = 4*mpf(1)/100*(mpf(1)/100)**2
    rs = roots(z, 200)
    deltas = {l: [lam for lam, name in rs if name == "s%d,1+" % l][0] - (l + 1) for l in (1, 9, 12, 20, 50, 100, 200)}
    print("  E1: delta_l (root l + 1 + delta_l):", ", ".join("l=%d %s" % (l, mp.nstr(d, 6)) for l, d in deltas.items()))
    ok["E1"] = abs(deltas[12] - mpf("7.3846e-8")) < mpf("5e-13") and deltas[200] < deltas[100] < deltas[50] < deltas[12]
    uniq = fracs(rs)
    best, arg, fromZ = least(uniq)
    print("  E2: finite reading (real parts in [-10, 10]): %d distinct fractional parts; least distance between points"
          " of M %s (%s, %s), so eps_ind < %s; least distance from Z %s (%s)"
          % (len(uniq), mp.nstr(best, 6), arg[0], arg[1], mp.nstr(best/2, 6), mp.nstr(fromZ[0], 6), fromZ[1]))
    ok["E2"] = abs(best - mpf("2.9243e-10")) < mpf("1e-13") and abs(fromZ[0] - mpf("9.4737e-8")) < mpf("1e-12")
    u0 = fracs(roots(mpf(0), 200))
    b0, _, _ = least(u0) if len(u0) > 1 else (mpf(1), None, None)
    ok["control"] = len(u0) == 1 and u0[0][0] == 0
    print("  control: z = 0, distinct fractional parts %d (all integers): %s" % (len(u0), ok["control"]))
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
