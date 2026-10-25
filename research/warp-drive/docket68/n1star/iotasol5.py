#!/usr/bin/env python3
"""iotasol5.py -- the numerals of [Hin26] section 9's iota+ and tf solution theory at n = 4 (N1STAR-PROOF.md 10.82;
the readings census's root RI; D176).
Labels: computed (exact, sympy) where said; arithmetic in n checked against print at n = 3 where said; READ.

[Hin26] (Hintz, arXiv:2606.28253v2) works at n = 3 with the iota+ model (9.11), N_iota+(L-bar, lam) = -2 v (v d_v -
lam)(v d_v - 1 - S-bar) + v^2 L~(0)(omega, v d_v, d_omega), v = t*/r, its conjugate N_sf(lam) (9.10) across v = 0, and
the tf model (9.58), N_tf(L-bar, +-1) = rhat^-2 L~(0)(omega, -rhat d_rhat, d_omega) -+ i rhat^-1 L~_1(-rhat d_rhat),
L~_1(rho d_rho) = -2(rho d_rho - 1 - S-bar), from L-bar = rho^2 L~(0)(omega, rho d_rho, d_omega) + rho L~_1(rho d_rho)
d_t*.  The checks below run at n = 3 and n = 4 (c = (n - 1)/2) with S a complex constant standing for an eigenvalue
of S-bar, on a scalar harmonic of S^(n-1) with eigenvalue kappa of his slashed Delta, the positive Laplacian
(Remark 9.5).

  J1 (computed, exact) The model.  -box of R^(1+n) in (t*, rho), t* = t - r, rho = 1/r, has no d_t*^2 term and is
     rho^2 L~(0)(rho d_rho) + rho L~_1(rho d_rho) d_t* with L~(0)(x) = -x^2 + (n - 2) x + kappa and L~_1(x) = -2(x -
     c): his -2(x - 1) at n = 3, -2(x - 3/2) at n = 4.  For L-bar = rho^2 L~(0) + rho L~_1 d_t* with L~_1(x) = -2(x - c -
     S), t*^lam t*^2 L-bar t*^-lam on functions of (v, omega) is -2 v (v d_v - lam)(v d_v - c - S) + v^2 L~(0)(v d_v):
     (9.11) at every n, with c for his 1.  Control: c = 1 at n = 4.
  J2 (computed, exact) N_sf and its exponents at v = 0 (Proposition 9.2 (1)).  N_sf(lam) = v^(-2-lam) N_iota+ v^lam is
     -2 d_v (v d_v + lam - c - S) + L~(0)(v d_v + lam); the b-normal operator of v N_sf(lam) at v = 0 has the
     characteristic exponents 0 and c + S - lam: his 0 and 1 + alpha - lam at n = 3, 3/2 + alpha - lam at n = 4.  So
     (arithmetic, chi^w_+ in H^(Re w + 1/2 - eps)_loc) the below-threshold condition is s < c + 1/2 + min Re S - Re lam,
     his 3/2 + min spec S-bar - Re lam and 2 - Re lam at n = 4 (min spec S-bar = 0, 10.25); (9.5) needs s > -1/2,
     possible iff Re lam < c + 1 (his 2; 5/2); the extension by zero of (9.6)'s v^(c + min S - Re lam - eps) is in
     L^1_loc iff Re lam < c + 1.  Control: the exponent c - lam with c = 1 at n = 4.
  J3 (computed, exact) The Fourier transform in v and the tf operator (the injectivity step).  With u-hat(rhat) = int
     e^(i rhat v) u dv (d_v -> -i rhat, v d_v -> -d_rhat rhat), N_sf(lam) becomes 2 i rhat (-d_rhat rhat + lam - c - S)
     + L~(0)(-d_rhat rhat + lam), his bracket with c for 1; conjugation by rhat^(lam - 1) -- the exponent free of c --
     gives -2 i rhat (rhat d_rhat + c + S) + L~(0)(-rhat d_rhat) = rhat^2 N_tf(L-bar, +1) of (9.58) (the other sign
     with rhat -> -rhat).  So the weight condition of Proposition 8.6 on w-flat, Re(-lam + 1) > -eps_ind, is Re lam < 1
     + eps_ind at every n.  ((9.7) prints the bracket as rhat^-2 N_tf; against (9.58) it is rhat^2 N_tf, a
     normalisation that does not touch the kernel.)  Control: conjugation by rhat^(lam - c).
  J4 (computed, exact) The outgoing end of tf (Lemma 9.26, Propositions 9.30, 9.35).  On e^(i theta rhat) rhat^-a,
     N_tf(L-bar, +1)'s rhat^0 coefficient is theta (theta + 2): the non-oscillating (outgoing) phase theta = 0 and the
     incoming e^(-2 i rhat); at theta = 0 the rhat^-1 coefficient vanishes iff a = c + S.  Outgoing solutions are
     rhat^-(c + S) (1 + O(rhat^-1)), in H^(oo, l)_b(|d rhat / rhat|) near scf iff l < c + Re S: the condition l_scf <
     c + min spec S-bar, his l_scf < 1 and l_scf < 3/2 at n = 4.  Control: c = 1 at n = 4.
  J5 (computed, exact; arithmetic where said) Proposition 9.4's weights at I+.  From (9.11), N_iota+ h = f is (v d_v -
     lam)(v d_v - c - S) h = -f/(2v) + (v/2) L~(0)(v d_v) h, (9.22); with J2's s = c + 1/2 - Re lam - eps and (9.5)
     (H-dot^s(|dv|) = H^(s, s - 1/2)_b(|dv/v|)), h = v^lam h~ has the I+ b-weight c - eps (arithmetic: his 1 - eps, 3/2
     - eps at n = 4), so (9.22)'s right side has order c + 1 - eps (his 2 - eps, 5/2 - eps); (9.5) holds for Re lam < c
     + 1 and (9.21) for Re lam > c, which overlap; and v^lam is excluded from h's expansion by the bound h = O(v^(c -
     eps)) iff Re lam < c (his 'Re lam < 1', 3/2 at n = 4).  Control: the weight 1 - eps claimed at n = 4.
"""
import sys
import time

import sympy as sp

from damping5 import Checklist

lam, z, y, a, th, S, kap = sp.symbols("lambda z y a theta S kappa")
eps = sp.Symbol("epsilon", positive=True)
ts, r, rho, v, rh, t = sp.symbols("tstar r rho v rhat t", positive=True)


def c_of(n):
    return sp.Rational(n - 1, 2)


def L0(x, n):
    return -x**2 + (n - 2) * x + kap                    # kappa >= 0: his slashed Delta is the positive Laplacian


def L1(x, n, S_=S, c=None):
    c = c_of(n) if c is None else c
    return -2 * (x - c - S_)


def minus_box(U, n):
    """-box of R^(1+n) on U(t*, r) Y_l, computed from u(t, r) = U(t - r, r)."""
    u = U.subs(ts, t - r)
    box = -sp.diff(u, t, 2) + sp.diff(u, r, 2) + (n - 1) / r * sp.diff(u, r) - kap / r**2 * u
    return sp.simplify(-box.subs(t, ts + r))


def j1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        c = sp.Integer(1) if (control and n == 4) else c_of(n)
        # -box on t*^-lam rho^y, rho = 1/r: rho^2 L~(0)(y) + rho L~_1(y) (-lam/t*)
        U = ts**(-lam) * r**(-y)
        mb = sp.expand(sp.simplify(minus_box(U, n) / U))
        target = sp.expand(r**-2 * L0(y, n) + r**-1 * (-2) * (y - c) * (-lam / ts))
        chk(f"n = {n}: -box = rho^2 L~(0)(rho d_rho) + rho L~_1(rho d_rho) d_t*, L~_1(x) = -2(x - {c})",
            sp.simplify(mb - target) == 0)
        chk(f"n = {n}: no d_t*^2 term (-box t*^2 -> 0 as r -> oo)", sp.limit(minus_box(ts**2, n), r, sp.oo) == 0)
        # (9.11): t*^lam t*^2 Lbar t*^-lam on v^z, v = t* rho, Lbar = rho^2 L~(0)(rho d_rho) + rho L~_1(rho d_rho) d_t*;
        # on G = (t* rho)^z t*^-lam, rho d_rho is z and d_t* is (z - lam)/t*
        E1 = sp.expand(ts**2 * (rho**2 * L0(z, n) + rho * L1(z, n) * (z - lam) / ts))
        E2 = sp.expand((-2 * v * (z - lam) * (z - c - S) + v**2 * L0(z, n)).subs(v, ts * rho))
        chk(f"n = {n}: t*^lam t*^2 Lbar t*^-lam = -2 v (v d_v - lam)(v d_v - {c} - S) + v^2 L~(0)(v d_v)",
            sp.simplify(E1 - E2) == 0)
    return chk.ok


def j2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        c = c_of(n)
        # N_sf(lam) = v^(-2-lam) N_iota+ v^lam on v^z, from (9.11)
        Nio = (-2 * v * z * (z + lam - c - S) + v**2 * L0(z + lam, n)) * v**(z + lam)
        nsf = sp.expand(sp.powsimp(v**(-2 - lam) * Nio / v**(z - 1), force=True))
        chk(f"n = {n}: N_sf(lam) = -2 d_v (v d_v + lam - c - S) + L~(0)(v d_v + lam)",
            sp.simplify(nsf - sp.expand(-2 * z * (z + lam - c - S) + v * L0(z + lam, n))) == 0)
        roots = set(sp.roots(sp.Poly(nsf.coeff(v, 0), z)).keys())
        claim = {sp.Integer(0), (1 if (control and n == 4) else c) + S - lam}
        chk(f"n = {n}: exponents of v N_sf at v = 0: {sorted(map(str, roots))}",
            {sp.simplify(q) for q in roots} == {sp.simplify(q) for q in claim})
        # arithmetic: the thresholds at min spec S-bar = 0
        Re_lam = sp.Symbol("Re_lam")
        s_top = c + sp.Rational(1, 2)
        lam_max = sp.solve(sp.Eq(s_top - Re_lam, -sp.Rational(1, 2)), Re_lam)[0]
        printed = {3: (sp.Rational(3, 2), 2), 4: (2, sp.Rational(5, 2))}[n]
        chk(f"n = {n}: s < {s_top} - Re lam; s > -1/2 possible iff Re lam < {lam_max} (arithmetic)",
            (s_top, lam_max) == printed)
    return chk.ok


def j3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    w, e = sp.symbols("w e")
    for n in (3, 4):
        c = c_of(n)
        # Fourier side on rhat^w: d_v -> -i rhat, v d_v -> -d_rhat rhat (on rhat^w: -(w + 1))
        F = 2 * sp.I * rh * (-(w + 1) + lam - c - S) + L0(-(w + 1) + lam, n)
        Ntf = sp.expand(L0(-y, n) - sp.I * rh * L1(-y, n))                       # rhat^2 N_tf(+1) on rhat^y
        diff = sp.Poly(sp.expand(F.subs(w, y + lam + e) - Ntf), y, rh)
        es = sp.solve(diff.coeffs(), e, dict=True)
        chk(f"n = {n}: rhat^(lam + e) carries F[N_sf] onto rhat^2 N_tf(+1) only for e = {es}: free of c",
            len(es) == 1 and es[0][e] == -1)
        shift = (c - 1) if control else 0
        Fc = sp.expand(F.subs(w, y + lam - 1 + shift))
        chk(f"n = {n}: rhat^-(lam-1) F[N_sf] rhat^(lam-1) = -2 i rhat (rhat d + c + S) + L~(0)(-rhat d) "
            f"= rhat^2 N_tf(+1)",
            sp.simplify(Fc - Ntf) == 0)
    return chk.ok


def j4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    q = sp.Symbol("q", positive=True)
    for n in (3, 4):
        c = sp.Integer(1) if (control and n == 4) else c_of(n)
        u = sp.exp(sp.I * th * rh) * rh**(-a)
        X = lambda f: -rh * sp.diff(f, rh)                                       # -rhat d_rhat
        L0u = -X(X(u)) + (n - 2) * X(u) - kap * u
        L1u = -2 * (X(u) - (c_of(n) + S) * u)
        N = sp.expand(sp.simplify((rh**-2 * L0u - sp.I / rh * L1u) / u).subs(rh, 1 / q))
        P = sp.Poly(N, q)
        c0, c1 = P.coeff_monomial(1), P.coeff_monomial(q)
        chk(f"n = {n}: rhat^0 coefficient theta (theta + 2)", sp.simplify(c0 - th * (th + 2)) == 0)
        asol = sp.solve(sp.Eq(c1.subs(th, 0), 0), a)
        chk(f"n = {n}: outgoing (theta = 0) decay rhat^-a, a = {asol}; l_scf < c + min spec S-bar = {c}",
            len(asol) == 1 and sp.simplify(asol[0] - (c + S)) == 0)
        ain = sp.solve(sp.Eq(c1.subs(th, -2), 0), a)
        chk(f"n = {n}: incoming e^(-2 i rhat) rhat^-a, a = {ain}", len(ain) == 1)
    return chk.ok


def j5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    w = sp.Symbol("w")
    Re_lam = sp.Symbol("Re_lam")
    for n in (3, 4):
        c = c_of(n)
        # (9.22) from (9.11) on v^w: N_iota+ h = f  <=>  (w - lam)(w - c - S) h = -f/(2v) + (v/2) L~(0)(w) h
        Nio = -2 * v * (w - lam) * (w - c - S) + v**2 * L0(w, n)
        chk(f"n = {n}: (9.22): (v d_v - lam)(v d_v - c - S) h = -f/(2v) + (v/2) L~(0)(v d_v) h",
            sp.simplify(-Nio / (2 * v) + (v / 2) * L0(w, n) - (w - lam) * (w - c - S)) == 0)
        s = c + sp.Rational(1, 2) - Re_lam - eps
        wI = sp.simplify(s - sp.Rational(1, 2) + Re_lam)                       # (9.5), then times v^lam
        claim = (sp.Integer(1) if (control and n == 4) else c) - eps
        printed = {3: 1 - eps, 4: sp.Rational(3, 2) - eps}[n]
        chk(f"n = {n}: h's I+ b-weight {wI}, (9.22)'s right side {wI + 1}; (9.5) for Re lam < {c + 1}, (9.21) for "
            f"Re lam > {c}; no v^lam term iff Re lam < {c} (arithmetic)",
            sp.simplify(wI - claim) == 0 and sp.simplify(claim - printed) == 0)
    return chk.ok


CHECKS = [("J1 -box = rho^2 L~(0) + rho L~_1 d_t*, L~_1 = -2(x - c); (9.11) with c for 1 (n = 3, 4)", j1),
          ("J2 N_sf at v = 0: exponents 0, c + S - lam; s < c + 1/2 - Re lam, Re lam < c + 1", j2),
          ("J3 Fourier in v: conjugation by rhat^(lam - 1) gives rhat^2 N_tf(L-bar, +1) at every c", j3),
          ("J4 N_tf at scf: phases 0 and -2; outgoing rhat^-(c + S); l_scf < c + min spec S-bar", j4),
          ("J5 (9.22) at every c; h's I+ weight c - eps; Re lam < c for the expansion", j5)]


def run(only=None, verbose=False):
    ok = True
    for q, (name, fn) in enumerate(CHECKS, 1):
        if only and q != only:
            continue
        t0 = time.time()
        res = fn(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"iotasol5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, fn in CHECKS:
        total += 1
        res = fn(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"iotasol5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
