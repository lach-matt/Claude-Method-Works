#!/usr/bin/env python3
"""lowenergy5.py -- the five-dimensional inputs of [Hin26c]'s low-energy theory for the gauge potential operator on
Tangherlini: the transition face model, its Bessel reduction and the weights (N1STAR-PROOF.md section 10.20;
ROUTES-OPEN.md 4.21; D64).  Labels: computed (exact, sympy; numerical, mpmath, where said), deduced, READ.

[Hin26c] (arXiv:2606.28008v1) section 9.5 is stated for X a neighbourhood of the boundary of R^n: the transition face
normal operator N_tf(P_0, sigma^) = 2i sigma^ rho^ (rho^ d_rho^ - (n - 1)/2 - S) + rho^^2 P^(0)(0, w, rho^ d_rho^, d_w)
((9.110)); for the wave operator, conjugated by e^(i sigma^ r^), it is Delta_e - sigma^^2, and his Proposition 9.40 --
"Suppose the spatial dimension satisfies n >= 3" -- makes the scalar and every tensor wave operator tf-admissible with
all weights beta in (0, n - 2), by a Bessel argument: on degree-l harmonics the solutions are r^^(-(n-2)/2) H^(j)_nu
(sigma^ r^), nu = (n - 2)/2 + l; outgoing forces j = 1, whose size r^^(-(n-2)-l) near r^ = 0 is not O(r^^-beta).
Theorems 9.36 and 9.41 and Corollary 9.43 write the weight shift of Lemma 3.11 at n = 3, alpha + 3/2.  [Hin26]
Proposition 6.12's Step 1 needs the augmentation f = box_gam(sigma)(lambda^-1 omega_(0)) to lie in the target space,
which his (6.25) secures in four dimensions through a cancellation at infinity.

  L1 (computed, exact) On 4+1 Minkowski in t* = t - r and the Cartesian frame, thresh5.py's 2 (delta + E) G delta* at gam
     = 0, applied to e^(-i sigma t*) e^(-i sigma r) w(x) and multiplied back, is (Delta_e - sigma^2) w on every
     component: the 1-form wave operator acts componentwise, and conjugated by e^(i sigma r) its spectral family is the
     Helmholtz operator (his p. 197 display, at n = 4).  Four-dimensional control: n = 3, the same.  Controls: gam =
     1, where the modification does not act componentwise; and the conjugation by e^(-i sigma r).
  L2 (computed; exact, and numerical where said) The Bessel reduction at n = 4: for u = r^-1 w, -u'' - (3/r) u' + l (l
     + 2) u/r^2 - u = -r^-3 (r^2 w'' + r w' + (r^2 - (l + 1)^2) w), Bessel's equation of order nu = l + 1 = (n - 2)/2 +
     l; the exponents at r = 0 are l and -(l + 2) -- in rho^ = 1/r^ the zero energy indicial roots -l and l + 2 of the
     unmodified operator (10.15's vl roots), the gap (0, 2) at l = 0; and, numerically (mpmath, 30 digits, l = 0, ...,
     4): x^nu H^(1)_nu(x) -> -(i/pi) Gamma(nu) 2^nu as x -> 0, e^(-ix) x^(1/2) H^(1)_nu(x) -> (2/pi)^(1/2) e^(-i (nu
     pi/2 + pi/4)) as x -> oo, and on the ray x = i t, H^(1) decays and H^(2) grows.  So the outgoing solution r^^-1
     H^(1)_(l+1) is c r^^-(l+2) near 0 with c != 0: excluded from O(r^^-beta) for beta < 2 at every l, and admitted at l
     = 0 for beta > 2 -- the range (0, n - 2) is sharp.  Four-dimensional control: u = r^(-1/2) w, nu = l + 1/2, the
     exponents l and -(l + 1), the range (0, 1).  Control: the range (0, 3) claimed.
  L3 (computed, exact) The weights at n = 4.  rho^a lies in rho^alpha L^2(r^3 dr) near infinity iff a > alpha + 2: the
     shift of his Lemma 3.11 is n/2 = 2 (his 3/2), so Theorem 9.36's alpha + 3/2 reads alpha + 2, 10.15's shifted weight.
     On Tangherlini with t* = t - r, d_sigma^2 of the spectral family is 2 g00 Id, g00 = g^-1(dt*, dt*) in rho^2 C^oo
     (thresh5.py U4), so the third summand of f, (lambda sigma^^2/2) d_sigma^2 box(0) W*, is -2 mu rho^4 dt + O(rho^5):
     with 10.15's rho^3 for the first summand, f lies in the target space H_b^(oo, alpha + 2) iff alpha + 2 < 1.
     Four-dimensional control: n = 3, the shift 3/2.  Control: the Coulomb fall-off rho of four dimensions put on W*,
     where the third summand is rho^3.

Deduced, not computed here: with 10.18-10.19 (thresholds, dynamics, Theorems 9.5 and 9.16 on the reading of [Hin26c]
section 9 for n = 4): Theorem 9.36 at n = 4 with alpha + 2 in an indicial gap; Proposition 9.40 (READ, n >= 3) at n = 4
for the unmodified operator, weights (0, 2); his Lemma 6.8 there, box^Ups tf-admissible on (0, lam_s1,2) for small gam
and e, by his perturbation and Corollary 9.39; Corollary 9.43, index 0, so the cokernel of box(0) is spanned by 10.15's
delta(r - r_h) dr functional; and [Hin26] Proposition 6.12's Steps 1-2 in five dimensions, with alpha + 2 in (0, 1).

READ.  [Hin26c] pp. 61 (Lemma 3.11, Definition 3.12, (3.47)), 104 (Definition 5.10), 193-195 (Theorem 9.36 and its
proof, (9.107)-(9.109), section 9.5: (9.110), Theorem 9.38, (9.111)-(9.115)), 197-198 (Corollary 9.39, Proposition
9.40 and its proof), 198-200 (Theorem 9.41 and its proof, (9.119)-(9.122), Remark 9.42, Corollary 9.43 and its proof);
[Hin26] pp. 117-119 (Lemma 6.6, (6.17b), Lemma 6.8 and its proof), 121-124 (Proposition 6.12 and its proof, (6.24)-
(6.28)); alphaXiv, 2026-10-22.

sympy, mpmath.  python3 lowenergy5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import mpmath as mp
import sympy as sp

import thresh5 as T
from damping5 import Checklist

D = sp.diff
mu = T.mu
gam = T.gam


# ------------------------------------------------------------------------------------------------- L1
def l1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    sg = sp.Symbol("sigma", positive=True)
    for n in ((4,) if control else (4, 3)):
        Mk = T.minkowski(n, sp.Rational(2, n - 1))
        P, W, Tt, x, r, N = Mk["P"], Mk["W"], Mk["T"], Mk["x"], Mk["r"], Mk["N"]
        g0 = 1 if control == 1 else 0
        s = -1 if control == 2 else 1
        w = [sp.Function("w%d" % a)(*x) for a in range(N)]
        sub = {W[b]: sp.exp(-sp.I*sg*(Tt + s*r))*w[b] for b in range(N)}
        ok = True
        for a in range(N):
            Q = sp.expand(sp.powsimp(sp.expand(P[a].subs(gam, g0).subs(sub).doit()*sp.exp(sp.I*sg*(Tt + s*r)))))
            tgt = -sum(D(w[a], xi, 2) for xi in x) - sg**2*w[a]
            d = sp.expand(Q - tgt)
            atoms = sorted(d.atoms(sp.Derivative), key=str) + w
            syms = sp.symbols("q0:%d" % len(atoms))
            dl = d.subs(dict(zip(atoms, syms)))
            rest = dl.subs({q: 0 for q in syms})
            ok &= T.exact0(rest, x) and all(T.exact0(sp.expand(dl.coeff(q)), x) for q in syms)
        chk(f"n + 1 = {n + 1}: e^(i sigma r) (box(sigma) e^(-i sigma r) w) = (Delta_e - sigma^2) w on every component",
            ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- L2
def l2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    r, l = sp.symbols("r l", positive=True)
    p = sp.Symbol("p")
    w = sp.Function("w")(r)
    mp.mp.dps = 30
    for n in ((4,) if control else (4, 3)):
        nu = l + sp.Rational(n - 2, 2)
        u = r**(-sp.Rational(n - 2, 2))*w
        lhs = -D(u, r, 2) - (n - 1)/r*D(u, r) + l*(l + n - 2)*u/r**2 - u
        rhs = -r**(-sp.Rational(n - 2, 2) - 2)*(r**2*D(w, r, 2) + r*D(w, r) + (r**2 - nu**2)*w)
        bessel = sp.simplify(lhs - rhs) == 0
        ex = set(sp.solve(sp.expand(-p*(p - 1) - (n - 1)*p + l*(l + n - 2)), p))
        expo = ex == {l, -l - (n - 2)}
        num = True
        for ll in range(5):
            v = mp.mpf(ll) + mp.mpf(n - 2)/2
            small = mp.mpf("1e-12")**v*mp.hankel1(v, mp.mpf("1e-12"))
            want0 = -1j/mp.pi*mp.gamma(v)*2**v
            big = mp.mpf(10)**6
            far = mp.exp(-1j*big)*mp.sqrt(big)*mp.hankel1(v, big)
            want1 = mp.sqrt(2/mp.pi)*mp.exp(-1j*(v*mp.pi/2 + mp.pi/4))
            ray = abs(mp.hankel1(v, 1j*40)) < mp.exp(-30) and abs(mp.hankel2(v, 1j*40)) > mp.exp(30)
            num &= abs(small/want0 - 1) < mp.mpf("1e-6") and abs(far/want1 - 1) < mp.mpf("1e-3") and ray
        top = (n - 2) if control != 1 else (n - 1)
        # the outgoing solution is c r^-(l + n - 2) near 0 with c != 0, so it is O(r^-beta) iff beta >= l + n - 2:
        # excluded for every l and every beta in (0, top) iff min_l (l + n - 2) = n - 2 >= top, with equality (sharp)
        sharp = (n - 2) == top
        chk(f"n + 1 = {n + 1}: u = r^-{sp.Rational(n - 2, 2)} w gives Bessel's equation of order l + "
            f"{sp.Rational(n - 2, 2)}; exponents l, -(l + {n - 2}); Hankel asymptotics (mpmath); the outgoing solution "
            f"excluded exactly for beta in (0, {top})", bessel and expo and num and sharp)
    return chk.ok


# ------------------------------------------------------------------------------------------------- L3
def l3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    rho, a, al = sp.symbols("rho a alpha", real=True)
    for n in ((4,) if control else (4, 3)):
        e = 2*(a - al) - n - 1                                     # rho^(2(a - alpha)) rho^(-n-1) d rho near rho = 0
        thr = sp.solve(sp.Eq(e, -1), a)[0]
        chk(f"n + 1 = {n + 1}: rho^a in rho^alpha L^2(r^{n - 1} dr) iff a > {thr} (shift n/2)",
            sp.simplify(thr - (al + sp.Rational(n, 2))) == 0)
    if control:
        pass
    rs = sp.Symbol("rho", positive=True)
    g00 = -(2*mu*rs**2 - mu**2*rs**4)/(1 - mu*rs**2)             # thresh5.py U4, t* = t - r
    Wdt = rs**2 if control != 1 else rs                          # W* = dt/r^2 + ...; the control puts on rho
    third = sp.series(2*g00*Wdt, rs, 0, 6).removeO()
    lead = sp.Poly(third, rs).monoms()[-1][0]
    first = 3                                                    # 10.15 (vi): d_sigma box(0) W* = i r^-3 dt + O(r^-4)
    # rho^k lies in H_b^(oo, alpha + 2) (Euclidean density, n = 4) iff k > (alpha + 2) + 2, i.e. alpha + 2 < k - 2
    bound = min(first, lead) - 2
    chk(f"n + 1 = 5: (1/2) d_sigma^2 box(0) W* = g00 W*: 2 g00 W* = {sp.factor(third.as_leading_term(rs))} + ..., order "
        f"rho^{lead}; with 10.15's rho^3, f in H_b^(oo, alpha + 2) iff alpha + 2 < {bound}",
        lead == 4 and sp.simplify(third.coeff(rs, 4) + 4*mu) == 0 and bound == 1)
    return chk.ok


CHECKS = [("L1 the 1-form wave operator on 4+1 Minkowski: conjugated spectral family = Delta_e - sigma^2 per component",
           l1, 2),
          ("L2 Bessel at n = 4: order l + 1, exponents l and -(l + 2); outgoing excluded exactly for beta < 2", l2, 1),
          ("L3 weights at n = 4: shift alpha + 2; f's terms rho^3 and rho^4, in the target iff alpha + 2 < 1", l3, 1)]


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
    print(f"lowenergy5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"lowenergy5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
