#!/usr/bin/env python3
"""tfnorm5.py -- [Hin26c] sections 9.5-9.6 at n = 4: every place the dimension enters Theorem 9.38's proof, Corollary
9.39 and Theorem 9.41, computed at general n against his printed lines and at n = 4 (N1STAR-PROOF.md 10.80; the
readings census's root RL; D173).  Labels: computed (exact, sympy).

[Hin26c] (Hintz, arXiv:2606.28008) states section 9.5 for X in R^n -- the transition face normal operator (9.110),
N_tf(P_0, sigma^) = 2i sigma^ rho^(rho^ d_rho^ - (n - 1)/2 - S) + rho^^2 P^(0)(0, omega, rho^ d_rho^, d_omega), Theorem
9.38 with -q + n/2 in an indicial gap and (9.114)-(9.115), Corollary 9.39 with -n + 2 + beta -- and writes section 9.6's
Theorem 9.41 with Lemma 3.11's shift at n = 3, alpha + 3/2.  Operators x^a p(X), X = x d_x, are composed with
iplusnorm5.py's algebra, adjoints for x^m |dx/x|.

  R1 (computed, exact) (9.117): e^(2i/rho^) N_tf(P_0, 1)^(*, mu_e) e^(-2i/rho^), mu_e = rho^^-n mu_b, for the
     asymptotically Minkowski model, P^(0) = -X^2 + (n - 2) X + kappa on the degree-l harmonics, is -2i rho^(rho^ d -
     (n - 1)/2 - S-bar) + rho^^2 P^(0): N_tf(P_0, -1)'s structure with S~ = S-bar, at every n.  His first line, 2i
     rho^(rho^ d - (n - 1)/2 + S-bar) - 4, is reproduced; his second, for (rho^ D)^2, prints -2i rho^(rho^ d - n + 1)
     where the conjugation gives -2i rho^(2 rho^ d - 2n + 3): a misprint at every n, the printed term leaving no rho^
     rho^ d term at all, against (9.117) itself.  Control: e^(-2i/rho^), which leaves a rho^^0 term.
  R2 (computed, exact) the indicial roots: at ztf (rho^ -> oo) N_tf's leading part is rho^^2 P^(0), so its roots in r^
     = 1/rho^ are -lambda for lambda those of P^(0) -- -l and l + n - 2 -- and the adjoint's for mu_e are -n + 2 +
     lambda-bar, as he concludes: {l, -(l + n - 2)}, at n = 4 {l, -(l + 2)}.  The gap of P^(0) at l = 0 is (0, n - 2),
     so q = -beta + n/2 runs over (n/2 - beta_+, n/2 - beta_-) = (0, 2) at n = 4, and Corollary 9.39's adjoint space
     carries -n + 2 + beta = -2 + beta.  Control: the adjoint for rho^^-(n-1) mu_b.
  R3 (computed, exact) the densities: mu_e = r^^(n-1) |dr^| = rho^^-n |drho^/rho^|; at ztf, r^^a lies in r^^q
     L^2(r^^(n-1) |dr^|) near r^ = 0 iff a > q - n/2, so the Sobolev embedding loses n/2 = 2 (the source's '[0, 1)_rho^'
     in that sentence read as r^, the sixty-ninth verifier); r^(n-1) |dr| = |sigma|^-n r^^(n-1) |dr^|, r^ = r |sigma|, so
     the norm factor of (3.46) is |sigma|^(-n/2 - alpha): the print's |sigma|^(3/2 - alpha) reverses the sign of n/2, as
     its density line does ((xviii)), harmless, the factor standing on both sides of Theorem 9.41's chain; at n = 4 the
     window (-2 + beta_-, -2 + beta_+) and the weight alpha + 2. Control: 3/2 at n = 4.
  R4 (computed, exact) (9.122): with rho = |sigma| rho^, |sigma|^2 N_tf(P_0, e^(i theta)) is 2i sigma rho(rho d_rho -
     (n - 1)/2 - S) + rho^2 P^(0)(0, omega, rho d_rho, d_omega), (9.4)'s leading part, at every n, so P-hat_0(sigma)
     minus it is rho^2 (P^(0)(rho, .) - P^(0)(0, .)) + 2i sigma rho (S(0, omega) - S(rho, omega)) - i sigma Q + g00
     sigma^2 (the S term the sixty-ninth verifier added, of the same class), in rho_scf rho_tf^3 Diff^2_sc-b by
     Definition 9.4's memberships, which five-dimensional Tangherlini satisfies (10.21 (a)). Control: rho = rho^.

Mutants: R1 with e^(-2i/rho^); R2 with the density rho^^-(n-1) mu_b; R3 with 3/2 at n = 4; R4 with no rescaling.
sympy.  python3 tfnorm5.py [--selftest | --mutants]   (seconds)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist
from iplusnorm5 import I, X, add, adj, mul, op, si, sr

S = sr + I * si
nS = sp.Symbol("n", positive=True)
kap = sp.Symbol("kappa", real=True)
lv = sp.Symbol("l", nonnegative=True, integer=True)


def conj_exp(A, sgn=1):
    """e^(2i sgn/x) A e^(-2i sgn/x): X -> X + 2i sgn x^-1."""
    Xc = op({0: X, -1: sgn * 2 * I})
    out = {}
    for a, p in A.items():
        acc = {}
        for (k,), cf in sp.Poly(p, X).terms():
            T = op({0: cf})
            for _ in range(k):
                T = mul(T, Xc)
            acc = add(acc, T)
        out = add(out, mul(op({a: 1}), acc))
    return out


def Ntf(n, P=None):
    c = (n - 1) / sp.Integer(2)
    return op({1: 2 * I * (X - c - S), 2: (P if P is not None else -X**2 + (n - 2) * X + kap)})


# ------------------------------------------------------------------ R1
def r1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    sg = -1 if control else 1
    for n in (nS, 3, 4):
        c = (n - 1) / sp.Integer(2)
        R = conj_exp(adj(Ntf(n), -n), sg)
        want = op({1: -2 * I * (X - c - sp.conjugate(S)), 2: -X**2 + (n - 2) * X + kap})
        chk(f"n = {n}: (9.117) with S~ = S-bar, P~ = P^(0): N_tf(P_0, -1)'s structure",
            set(R) == set(want) and all(sp.simplify(R[a] - want[a]) == 0 for a in want))
        first = conj_exp(adj(op({1: 2 * I * (X - c - S)}), -n), sg)
        pr1 = op({1: 2 * I * (X - c + sp.conjugate(S)), 0: -4})
        chk(f"n = {n}: his first line 2i rho^(rho^ d - (n-1)/2 + S-bar) - 4",
            set(first) == set(pr1) and all(sp.simplify(first[a] - pr1[a]) == 0 for a in pr1))
        sec = conj_exp(adj(op({2: -X**2}), -n), sg)
        got = op({2: -(X - n + 2)**2, 1: -2 * I * (2 * X - 2 * n + 3), 0: 4})
        printed = op({2: -(X - n + 2)**2, 1: -2 * I * (X - n + 1), 0: 4})
        chk(f"n = {n}: (rho^ D)^2 gives -rho^^2 (X - n + 2)^2 - 2i rho^(2X - 2n + 3) + 4",
            set(sec) == set(got) and all(sp.simplify(sec[a] - got[a]) == 0 for a in got))
        chk(f"n = {n}: his printed -2i rho^(X - n + 1) differs (a misprint)",
            any(sp.simplify(sec.get(a, 0) - printed.get(a, 0)) != 0 for a in set(sec) | set(printed)))
    return chk.ok


# ------------------------------------------------------------------ R2
def r2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    y = sp.Symbol("y")
    for n in (3, 4):
        kl = lv * (lv + n - 2)
        P = -X**2 + (n - 2) * X + kl
        lam = sorted(sp.solve(P.subs(X, y), y), key=lambda z: sp.N(z.subs(lv, 1)))
        chk(f"n = {n}: P^(0)'s roots -l, l + {n - 2}", sp.simplify(lam[0] + lv) == 0
            and sp.simplify(lam[1] - lv - n + 2) == 0)
        N = Ntf(n, P)
        dens = -(n - 1) if control else -n
        A = adj(N, dens)
        mu = sp.solve(A[2].subs(X, y), y)                     # rho^^mu roots of the adjoint's ztf part
        rhat = sorted([sp.simplify(-m) for m in mu], key=lambda z: sp.N(z.subs(lv, 1)))
        want = sorted([sp.simplify(-n + 2 + sp.conjugate(L)) for L in lam], key=lambda z: sp.N(z.subs(lv, 1)))
        chk(f"n = {n}: the adjoint's roots in r^ are -n + 2 + lambda-bar = {rhat}",
            all(sp.simplify(a - b) == 0 for a, b in zip(rhat, want)))
        mu0 = sorted([sp.simplify(-m) for m in sp.solve(N[2].subs(X, y), y)], key=lambda z: sp.N(z.subs(lv, 1)))
        chk(f"n = {n}: N_tf's own roots in r^ are -lambda", all(sp.simplify(a + b) == 0
                                                                 for a, b in zip(mu0, reversed(lam))))
        gap = (lam[0].subs(lv, 0), lam[1].subs(lv, 0))
        chk(f"n = {n}: the gap at l = 0 is {gap}; q in ({sp.Rational(n, 2) - gap[1]}, {sp.Rational(n, 2) - gap[0]})",
            gap == (0, n - 2) and (sp.Rational(n, 2) - gap[1], sp.Rational(n, 2) - gap[0]) ==
            {3: (sp.Rational(1, 2), sp.Rational(3, 2)), 4: (0, 2)}[n])
    return chk.ok


# ------------------------------------------------------------------ R3
def r3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    rh, s_, a_ = sp.symbols("rhat sigma a", positive=True)
    q_ = sp.Symbol("q")
    for n in (3, 4):
        rho = sp.Symbol("rho", positive=True)
        mue = sp.simplify((1 / rho)**(n - 1) * sp.Abs(sp.diff(1 / rho, rho)))
        chk(f"n = {n}: r^^{n - 1} |dr^| = rho^^-{n} |drho^/rho^|", sp.simplify(mue - rho**(-n) / rho) == 0)
        shift = sp.Rational(3, 2) if (control and n == 4) else sp.Rational(n, 2)
        # at ztf: int_0^1 r^^(2(a - q)) r^^(n-1) dr^ converges iff 2(a - q) + n > 0
        # r^^a in L^2(r^^(n-1) |dr^|) near 0 (q = 0): integrate |r^^a|^2 r^^(n-1) on (0, 1) just above and below the
        # claimed borderline a = -shift; it must converge above and diverge below
        above = sp.integrate(rh**(2 * (-shift + sp.Rational(1, 10)) + n - 1), (rh, 0, 1))
        below = sp.integrate(rh**(2 * (-shift - sp.Rational(1, 10)) + n - 1), (rh, 0, 1))
        chk(f"n = {n}: at ztf r^^a in r^^q L^2(r^^(n-1) |dr^|) iff a > q - {shift}: the embedding loses n/2 "
            f"(integrals {above}, {below})", above.is_finite and below == sp.oo)
        dmeas = sp.simplify((rh / s_)**(n - 1) / s_)                       # r^(n-1) dr with r = r^/|sigma|
        ratio = sp.simplify(dmeas / rh**(n - 1))
        e_norm = sp.simplify(sp.log(ratio) / sp.log(s_) / 2)
        chk(f"n = {n}: r^{n - 1} |dr| = |sigma|^{sp.log(ratio) / sp.log(s_)} r^^{n - 1} |dr^|: (3.46)'s norm factor "
            f"|sigma|^({e_norm} - alpha)", sp.simplify(e_norm + shift) == 0)
    return chk.ok

# ------------------------------------------------------------------ R4
def r4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    vs, th_ = sp.symbols("varsigma theta", positive=True)
    for n in (3, 4, nS):
        c = (n - 1) / sp.Integer(2)
        Pc = -X**2 + (n - 2) * X + kap
        # N_tf in rho^ = rho / varsigma: x^a p(X) -> varsigma^-a x^a p(X) (X is scale-free)
        sc = 1 if control else vs
        Nrho = op({1: 2 * I * sp.exp(I * th_) * (X - c - S) / sc, 2: Pc / sc**2})
        lhs = op({a: vs**2 * p for a, p in Nrho.items()})
        want = op({1: 2 * I * vs * sp.exp(I * th_) * (X - c - S), 2: Pc})          # sigma = varsigma e^(i theta)
        chk(f"n = {n}: |sigma|^2 N_tf(P_0, e^(i theta)) is (9.4)'s leading part in rho",
            set(lhs) == set(want) and all(sp.simplify(lhs[a] - want[a]) == 0 for a in want))
    return chk.ok


CHECKS = [("R1 (9.117) at every n: S~ = S-bar; his first line; the (rho D)^2 line's misprint", r1),
          ("R2 the indicial roots -lambda and -n + 2 + lambda-bar; the gap (0, n - 2); q in (0, 2) at n = 4", r2),
          ("R3 the densities: mu_e = rho^^-n mu_b, the embedding's n/2 at ztf, (3.46)'s |sigma|^(-n/2 - alpha)", r3),
          ("R4 (9.122): |sigma|^2 N_tf is (9.4)'s leading part at every n", r4)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"tfnorm5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"tfnorm5.py mutants: {caught}/{total}")
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
