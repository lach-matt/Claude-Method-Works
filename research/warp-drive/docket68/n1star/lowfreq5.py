#!/usr/bin/env python3
"""lowfreq5.py -- [Hin26] section 10.2 in five dimensions: the low-frequency part of the proof of 2-admissibility and
its sf-loss (N1STAR-PROOF.md sections 10.40-10.41; ROUTES-OPEN.md 4.41-4.42; D104-D106).  Labels: computed (exact,
sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) writes the forward solution as u = u_hi + u_reg + g-dot + h_s1 ((10.50)), the last two
the inverse Fourier transforms of the augmentation's columns against b-hat_1, S-hat_1; "Differentiation in t* removes
these poles" and Lemma 10.12 records "d_t* g-dot in H^((s;k),(-1/2-eps,0))_3b;b" (10.51) and "d_t*^2 h_s1 in
H^((s;k),(1/2-eps,0))_3b;b" (10.52) (p. 215).  Its proof takes d_t* g-dot^Ups,aug in A^(1,2,2) ((10.54)) and d_t*^2
h^(<=1),aug_s1 ((10.57)) through (2.25a), "(Fu)|_(sigma in +-[0,1]) in H^(k, min(beta_I,beta_iota)-eps, beta_iota-1,
((0,0),beta_K-1))_b" (p. 60) -- the scf order the least of the I+ and iota+ orders, the tf order the iota+ order less
1, against an unweighted b-density -- and then, by Lemma 2.20 (p. 55: the 3b sf weight alpha' is the tf weight and s' +
alpha' the scf weight), to H^((s';k),(alpha',0)) "provided alpha' < -1/2 and s' + alpha' < -1/2 at R_out" (p. 216):
the tf and scf weights against |dx|, the second -1/2 from his I+ order 1.  With Remark 10.2's margin s + alpha_sf <
-3/2 at R_out (p. 200), two integrations by Lemma 10.13 from the initial weights (10.61)-(10.62) give u in
H^((s-1;k),(-3/2-eps,-2))_3b;b, "This proves (10.3) (since alpha_sf - delta < -3/2)" (p. 217).  In five dimensions the
states are one order faster and the augmentation is chi_K times them, with no I+ term (10.39):

  W1 (computed, exact) The columns at zero frequency.  On 4+1 Minkowski, with aug5.py's gauged states and a piecewise
     cubic chi (1 on [0, 1/4], 0 from 1/2): d_T(chi(r/T) g-dot) is homogeneous of degree -(k+1) and vanishes where r/T
     is outside (1/4, 1/2), and at r = 2 its integral over T >= 1 is 1, so that the column's zero-frequency value is
     g-dot itself; d_T^2(chi(r/T)(T h + h')), h, h' generic, integrates to h there (chi C^1 at its joints).  So the
     zero-frequency values of the derivative columns are the states g-dot and h_s1, and their weights in rho^alpha
     L^2(r^(n-1) dr) = r^-alpha L^2(r^(n-1) dr) are below k - n/2 and k + 1 - n/2, h_s1 one order faster than the mass
     state (section 10.28): for the mass state, from its actual components, 0 and 1 in five dimensions; four
     dimensions -1/2 and 1/2, his (10.51) and (10.52).  Controls: the five-dimensional weight claimed to be the
     four-dimensional -1/2; a ramp chi, C^0 only, under which the second integral is not h.
  W2 (computed, exact) The weights of section 10.2, over the admissible region alpha_sf + n/2 in (0, eps_ind), eps_ind
     in (0, 1], at 598 rational points.  A column of iota+ order q and I+ order beta_I has, by (2.25a) against |dx|,
     tf weight q - 1 - n/2 - eps and scf weight min(beta_I, q) - n/2 - eps; d_t* g-dot's weight is the lesser of its
     tf weight and its scf weight less s at R_out (s' = s; s below -3/2 - alpha_sf there), d_t*^2 h_s1's likewise at
     s' = s - 1, d_t*^2 u_sing's the lesser of the second and the first plus 1, and Lemma 10.13 twice from
     (10.61)-(10.62).  Four dimensions (beta_I = 1): -1/2 - eps, 1/2 - eps, the final -3/2 - eps, loss alpha_sf + 3/2
     + eps -- his.  Five dimensions (no I+ term): -eps, 1 - eps (also at s' = s), the final alpha_sf, loss 0 at every
     point -- the requirement at R_out does not bind, and the initial weights set the bound.  Five dimensions with I+
     terms at the radiative order beta_I = 3/2: alpha_sf + 1 - eps, alpha_sf + 2 - eps, the final alpha_sf - eps,
     loss eps.  Controls: five dimensions with four-dimensional orders and I+ order 1 (a loss); four dimensions
     claimed lossless; five dimensions claimed at alpha_sf + 1 and alpha_sf + 2, the radial threshold binding (D104's
     reading, corrected in D105).
  W3 (computed, exact) [Hin26c] (13.30a)'s shift at n = 4 (D106, D107). On R^n near infinity (|x| >= 1), r^-a lies in
     L^2(|dx|) iff a > n/2 and in L^2(mu_b), mu_b = |dx|/|x|^n, iff a > 0: L^2(|dx|) = rho^(n/2) L^2(mu_b), the shift
     his (13.30a) calls "due to the passage from mu to mu_b" (p. 255), 3/2 at n = 3 (his p. 252) and 2 at n = 4.
     (13.30a)'s rule -- the target's scf order at R_out below the source's less the shift, its tf order the source's
     less the shift -- reproduces his printed instances at n = 3: p. 206's "r + alpha_sf + 1 < 3/2 - eps" for scf order
     3 - eps and "r + alpha_sf < -1/2" for 2 - eps; p. 216's "r < -1/2" for (10.56)'s (1 - eps, 1 - 2eps), tf -1/2 -
     2eps (his -1/2 - eps, eps renamed); and (10.59)'s (1 - eps, 2 - eps), r < -1/2 and 1/2 - eps. At n = 4 it gives
     10.40(b)'s requirements r < 1 - eps and r < 2 - eps and tf weights -eps and 1 - eps. Controls: the shift taken as
     3/2 at n = 4; the rule without the shift.

Run: python3 lowfreq5.py --selftest | --mutants | --only k [--verbose]   (seconds).
"""
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

import aug5 as A5
from damping5 import Checklist
from sbar5 import v, eC, gC, eU, gU

HALF = Fr(1, 2)


def chi(s):
    """piecewise cubic step, 1 on [0, 1/4], 0 on [1/2, oo)"""
    u = (s - sp.Rational(1, 4)) * 4
    return sp.Piecewise((1, s <= sp.Rational(1, 4)), (1 - 3 * u**2 + 2 * u**3, s < sp.Rational(1, 2)), (0, True))


# ------------------------------------------------------------------------------------------------- W1
def w1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    T, R = sp.symbols("T R", positive=True)
    h, h1 = sp.symbols("h h1")
    col = sp.diff(chi(R / T), T)                               # d_T chi(r/T): the column's scalar factor
    sv = sp.Symbol("s")
    mid = 1 - 3 * (4 * sv - 1)**2 + 2 * (4 * sv - 1)**3        # chi on [1/4, 1/2]
    if control == 2:
        mid = 2 - 4 * sv                                       # a ramp, C^0 only
    c1 = [mid.subs(sv, sp.Rational(1, 4)), mid.subs(sv, sp.Rational(1, 2)),
          sp.diff(mid, sv).subs(sv, sp.Rational(1, 4)), sp.diff(mid, sv).subs(sv, sp.Rational(1, 2))]
    # at r = 2, chi(2/T) is 0 for T <= 4, mid(2/T) on [4, 8], 1 for T >= 8, and C^1 at the joints (c1 = 1, 0, 0, 0):
    # the integrands vanish off [4, 8] and the second derivative carries no delta there
    one = sp.simplify(sp.integrate(sp.diff(mid.subs(sv, 2 / T), T), (T, 4, 8)))
    two = sp.simplify(sp.integrate(sp.diff(mid.subs(sv, 2 / T) * (T * h + h1), T, 2), (T, 4, 8)))
    zero_tail = c1 == [1, 0, 0, 0]
    outside = all(sp.simplify(col.subs({R: rr, T: tt})) == 0 for rr, tt in ((1, 5), (3, 5), (2, 1))) and zero_tail
    if control == 2:
        zero_tail = outside = True                             # the claim: the ramp's integrals are those of a step
    chk(f"the zero-frequency integrals: d_T chi gives {one}, d_T^2 (chi (T h + h')) gives {two}; d_T chi vanishes "
        f"outside the transition", one == 1 and sp.expand(two - h) == 0 and outside)
    if control == 2:
        return chk.ok
    al = sp.Symbol("alpha", real=True)
    for n in ((4,) if control else (4, 3)):
        C, gauge, L, out = A5.states(n)
        g = out["mass"][0].subs({v: sp.Rational(1, 3), eC: sp.Rational(1, 5), gC: 10, eU: sp.Rational(1, 7),
                                  gU: sp.Rational(3, 2)})
        pt = {C.x[0]: R, **{q: 0 for q in C.x[1:]}}
        nrm2 = sp.simplify(sum(g[i, j].subs(pt)**2 for i in range(C.N) for j in range(C.N)))
        k = -sp.Rational(sp.degree(sp.numer(sp.together(nrm2)), R) - sp.degree(sp.denom(sp.together(nrm2)), R), 2)
        # the T-dependence of chi(r/T) g-dot: homogeneous of degree -(k+1) after d_T
        lam = sp.Symbol("lam", positive=True)
        cg = sp.diff(chi(R / T), T) * R**(-k)
        hom = sp.simplify(cg.subs({R: lam * sp.Rational(3, 10), T: lam}) * lam**(k + 1) -
                          cg.subs({R: sp.Rational(3, 10), T: 1}))
        thr_g = k - sp.Rational(n, 2)               # r^-k in rho^al L^2(r^(n-1) dr) = r^-al L^2 iff al < k - n/2
        conv = sp.integrate(R**(2 * (thr_g - sp.Rational(1, 10)) - 2 * k + n - 1), (R, 1, sp.oo)).is_finite
        div = not sp.integrate(R**(2 * thr_g - 2 * k + n - 1), (R, 1, sp.oo)).is_finite
        want = {4: (0, 1), 3: (-sp.Rational(1, 2), sp.Rational(1, 2))}[n]
        if control == 1:
            want = (-sp.Rational(1, 2), sp.Rational(1, 2))
        good = hom == 0 and conv and div and (thr_g, thr_g + 1) == want
        chk(f"n + 1 = {n + 1}: the mass state of degree -{k}, its column of degree -{k + 1}; weights of g-dot and h_s1 "
            f"(one order faster, section 10.28) {thr_g}, {thr_g + 1}", good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- W2
def chain(n, qg, qh, bi, a, eps):
    """section 10.2's weights: n spatial dimensions, the states' decay orders qg, qh, the columns' I+ order bi (None:
    no I+ term), alpha_sf a, the small eps; s at R_out below smax = -3/2 - a (Remark 10.2's margin)"""
    smax = -Fr(3, 2) - a

    def col(q, drop):
        """a column of iota+ order q at s' = s - drop: (2.25a) against |dx|, then Lemma 2.20 and R_out"""
        tf = q - 1 - Fr(n, 2) - eps                            # tf order q - 1
        scf = (q if bi is None else min(bi, q)) - Fr(n, 2) - eps   # scf order min(beta_I, q)
        return min(tf, scf - (smax - drop))                    # alpha' < tf and s' + alpha' < scf at R_out
    w_dg = col(qg + 1, 0)                                      # d_t* g-dot^aug at iota+ order qg + 1, s' = s
    w_ddh = col(qh + 1, 1)                                     # d_t*^2 h^aug at iota+ order qh + 1, s' = s - 1
    w_dd = min(w_dg + 1, w_ddh)                                # d_t* in rho_sf V_3b
    w_du = min(w_dd, (a + 1) + 1) - 1                          # Lemma 10.13 from (10.62)
    w_u = min(w_du, a + 1) - 1                                 # Lemma 10.13 from (10.61)
    return w_dg, w_ddh, col(qh + 1, 0), min(w_u, a), a - min(w_u, a)


def w2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    pts = [(ei, Fr(j, 11) * ei, Fr(1, 10**m)) for ei in (Fr(1, 100), Fr(1, 10), HALF, Fr(9, 10), Fr(1))
           for j in range(1, 11) for m in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)]
    cases = [(4, 2, 3, None, "five, no I+ term: -eps, 1 - eps, alpha_sf, no loss"),
             (4, 2, 3, Fr(3, 2), "five, I+ order 3/2: alpha_sf + 1 - eps, alpha_sf + 2 - eps, alpha_sf - eps"),
             (3, 1, 2, 1, "four, I+ order 1: his -1/2 - eps, 1/2 - eps, -3/2 - eps and loss")]
    if control:
        cases = cases[:1] if control != 2 else cases[2:]
    for n, qg, qh, bi, what in cases:
        if control == 1:
            qg, qh, bi = 1, 2, 1
        good, used = True, 0
        for ei, x, eps in pts:
            a = x - Fr(n, 2)                                   # alpha_sf + n/2 = x in (0, eps_ind)
            if eps >= x or eps >= ei - x:
                continue
            used += 1
            w_dg, w_ddh, w_ddh0, w, loss = chain(n, qg, qh, bi, a, eps)
            if n == 4 and bi is None:
                want = (-eps, 1 - eps, 1 - eps, a, 0) if control != 3 else (a + 1, a + 2, 1 - eps, a, 0)
                good &= (w_dg, w_ddh, w_ddh0, w, loss) == want
            elif n == 4:
                good &= (w_dg, w_ddh, w, loss) == (a + 1 - eps, a + 2 - eps, a - eps, eps)
            else:
                good &= w_dg == -HALF - eps and w_ddh == HALF - eps and w == -Fr(3, 2) - eps
                good &= (loss == a + Fr(3, 2) + eps) if control != 2 else loss == 0
        chk(f"n + 1 = {n + 1}: section 10.2's weights at {used} points of the admissible region ({what})", good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- W3
def shift(n):
    """the a at which r^-a enters L^2(R^n, |dx|), less the one at which it enters L^2(R^n, |dx|/|x|^n)"""
    R = sp.Symbol("R", positive=True)
    tenth = sp.Rational(1, 10)

    def enters(a0, power):                      # r^-a over r >= 1: in L^2(r^power dr) at a0 + 1/10, not at a0
        return (sp.integrate(R**(-2 * (a0 + tenth) + power), (R, 1, sp.oo)).is_finite and
                not sp.integrate(R**(-2 * a0 + power), (R, 1, sp.oo)).is_finite)
    a_mu, a_mub = sp.Rational(n, 2), 0
    assert enters(a_mu, n - 1) and enters(a_mub, -1)
    return a_mu - a_mub


def w3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    e = sp.Symbol("eps", positive=True)
    sh = {3: shift(3), 4: shift(4)}
    chk(f"the density shift: {sh[3]} at n = 3 (his p. 252), {sh[4]} at n = 4", sh == {3: sp.Rational(3, 2), 4: 2})
    if control == 1:
        sh[4] = sp.Rational(3, 2)
    if control == 2:
        sh = {3: 0, 4: 0}

    def rule(n, scf, tf):                                      # (13.30a): (scf bound at R_out, tf weight) against |dx|
        return sp.expand(scf - sh[n]), sp.expand(tf - sh[n])
    half = sp.Rational(1, 2)
    p206a = rule(3, 3 - e, 0)[0] == half * 3 - e               # r + alpha_sf + 1 < 3/2 - eps
    p206b = rule(3, 2 - e, 0)[0] - 1 == -half - e              # r + alpha_sf < -1/2 (eps arbitrary)
    p216 = rule(3, 1 - e, 1 - 2 * e) == (-half - e, -half - 2 * e)     # r < -1/2; his -1/2 - eps, eps renamed
    p1059 = rule(3, 1 - e, 2 - e) == (-half - e, half - e)     # r < -1/2; 1/2 - eps
    chk("n = 3: his p. 206 (r + alpha_sf + 1 < 3/2 - eps; r + alpha_sf < -1/2), p. 216 ((10.56): r < -1/2, -1/2 - eps) "
        "and (10.59) (r < -1/2, 1/2 - eps)", p206a and p206b and p216 and p1059)
    five = rule(4, 3 - e, 2 - e) == (1 - e, -e) and rule(4, 4 - e, 3 - e) == (2 - e, 1 - e)
    chk("n = 4: 10.40(b)'s columns, (3 - eps, 2 - eps) and (4 - eps, 3 - eps): r < 1 - eps, r < 2 - eps; tf -eps, "
        "1 - eps", five)
    return chk.ok


CHECKS = [("W1 the columns' zero-frequency values are the states; their weights 0 and 1 (four: his -1/2, 1/2)", w1, 2),
          ("W2 section 10.2's weights: five dimensions -eps, 1 - eps, alpha_sf, no loss; I+ terms eps; four his", w2, 3),
          ("W3 (13.30a)'s shift n/2 (3/2, 2): his pp. 206, 216 and (10.59) reproduced; five dimensions 10.40(b)", w3, 2)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"lowfreq5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"lowfreq5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    verbose = "--verbose" in args
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, nc = CHECKS[k - 1]
        print(name, "PASS" if fn(verbose=True) else "FAIL")
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    else:
        sys.exit(0 if selftest(verbose) else 1)
