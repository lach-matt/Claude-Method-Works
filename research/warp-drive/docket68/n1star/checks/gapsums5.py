"""gapsums5.py -- LOSS-D LD9 (D408): how close the sums of two near-commensurate increments come above an integer.

Lambda (I11 Definition 1.1) contains every g + sum n_i w_i, n_i in N_0, g a generator and w_i in pi_1(E_ind cup
E^iota_ind) cup {1}. E_ind is the index set of III.D'' Proposition 3.1 and III.F''' Proposition 2.2 at b_0 (I5:190,
I8:35); its exponents are indicial roots plus integers (D4:52-60), and the record does not list them. box^Ups(0)'s
s0 and s1 roots through 2 are (III.D (4.1); N1STAR-PROOF.md:4575-4576)

    lam_s0 = (1 + (9 + 4z)^(1/2))/2 = 2 + z/3 + O(z^2),
    lam_s1,2 = (1 + (17 + 2z - 2(z^2 + 4z + 16)^(1/2))^(1/2))/2 = 2 + z/12 + O(z^2),

z = 4 e_Ups gam_Ups^2, = 4 x 10^-6 at the record's point (e_Ups = gam_Ups = 1/100). If E_ind contains the offsets
d0 := lam_s0 - 2 and d1 := lam_s1,2 - 2 (as the expansions of Proposition 3.1's s1 state and of the mass state's gauge
part generically carry), then 2 + n0 d0 + n1 d1 is in Lambda, and (G) needs eps_K below its distance above 3.

  G1 (exact, 50 digits) d0, d1 at the record's point and their first-order forms; e2 := d0 - 4 d1 = O(z^2).
  G2 the least positive n0 d0 + n1 d1 - 1 over n0, n1 >= 0 (every n0 up to 1/d0, n1 the least making the sum exceed
     1): an upper bound for delta_G under that hypothesis, against the record's least distance 7.3846 x 10^-8 of a
     non-integer root from Z (N1STAR-PROOF.md:4071), which bounds eps_ind.
  G3 the same from the generator lambda_sharp = 3/2 + (1 - e_Ups) gam_Ups to just above 2.
  Control: with d0 alone (n1 = 0) the least gap above 1 is of the order of d0 itself, far larger: the near-
     commensurability d0 ~ 4 d1 is what brings the sums close.
Labels: computed (exact arithmetic at 50 digits); the hypothesis on E_ind is not checked here.

    python3 checks/gapsums5.py [--selftest]
"""
import sys

from mpmath import ceil, mp, mpf, sqrt

mp.dps = 50
EU = GU = mpf(1)/100
Z = 4*EU*GU**2
D0 = (1 + sqrt(9 + 4*Z))/2 - 2
D1 = (1 + sqrt(17 + 2*Z - 2*sqrt(Z**2 + 4*Z + 16)))/2 - 2
LSHARP = mpf(3)/2 + (1 - EU)*GU
EPS_REC = mpf("7.3846e-8")


def least_above(target, a, b, nmax):
    """least positive n0 a + n1 b - target over 0 <= n0 <= nmax, n1 >= 0"""
    best, arg = None, None
    for n0 in range(nmax + 1):
        rest = target - n0*a
        if rest < 0:
            val = -rest
            n1 = 0
        else:
            n1 = int(ceil(rest/b))
            val = n0*a + n1*b - target
            if val == 0:
                n1 += 1
                val = n0*a + n1*b - target
        if best is None or val < best:
            best, arg = val, (n0, n1)
        if rest < 0:
            break
    return best, arg


def main():
    ok = {}
    e2 = D0 - 4*D1
    print("  G1: z = %s; d0 = %s (z/3 = %s); d1 = %s (z/12 = %s); e2 = d0 - 4 d1 = %s"
          % (mp.nstr(Z, 6), mp.nstr(D0, 12), mp.nstr(Z/3, 12), mp.nstr(D1, 12), mp.nstr(Z/12, 12), mp.nstr(e2, 6)))
    ok["G1"] = abs(D0 - Z/3) < Z**2 and abs(D1 - Z/12) < Z**2 and 0 < abs(e2) < Z**2
    nmax = int(1/D0) + 1
    g2, a2 = least_above(mpf(1), D0, D1, nmax)
    print("  G2: least n0 d0 + n1 d1 above 1: %s at (n0, n1) = %s; against eps_ind <= %s: %s times smaller"
          % (mp.nstr(g2, 6), a2, mp.nstr(EPS_REC, 6), mp.nstr(EPS_REC/g2, 4)), flush=True)
    ok["G2"] = 0 < g2 < EPS_REC
    g3, a3 = least_above(2 - LSHARP, D0, D1, int((2 - LSHARP)/D0) + 1)
    print("  G3: least lambda_sharp + n0 d0 + n1 d1 above 2: %s at %s" % (mp.nstr(g3, 6), a3), flush=True)
    ok["G3"] = 0 < g3 < EPS_REC
    n = int(ceil(1/D0))
    gc = n*D0 - 1
    if gc == 0:
        gc = D0
    print("  control: d0 alone, least n d0 above 1: %s (n = %d)" % (mp.nstr(gc, 6), n))
    ok["control"] = gc > 100*g2
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
