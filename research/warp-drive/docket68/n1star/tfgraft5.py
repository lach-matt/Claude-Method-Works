#!/usr/bin/env python3
"""tfgraft5.py -- [Hin26] section 9.2 at n = 4 (proof5/PART-III-G5-TF.md): the tf-normal operator on the formal
solutions, the pairing of indicial roots with source exponents behind the functions l_beta, the order bookkeeping of
Lemma 9.26 and Propositions 9.30 and 9.35 at n = 4, and the counterexample to the source's pointwise construction in
the proof of Proposition 9.35.  Labels: computed (exact, sympy; exact rational arithmetic and interval grids).

  T1 (Lemma 2.2, the source's (9.60) at n = 4, exactly) Scalar model: L-bar = -d_t* rho (rho d_rho - 3/2 - s) +
     rho^2 N(rho d_rho), N(lam) = (lam - mu)(lam - c), and a tower N(mu - m) phi_m = (mu - m - 1/2 - s) phi_(m-1),
     phi_0 = 1.  (a) |sigma|^-2 L-bar^(sigma) is N_tf = r^-2 N(-r d_r) +- i r^-1 (-r d_r - 3/2 - s) in r = |sigma|/rho
     (on monomials, sigma = +-|sigma|).  (b) N_tf sum_(j<=k) (-+ i r)^j r^-mu phi_j = (-+ i)^(k+1) r^(k-1-mu) psi_k,
     psi_k = -(mu - k - 3/2 - s) phi_k, for k = 0..3, mu, s, c symbolic.  Control: the sign of the r^-1 term flipped.
  T2 (the pairing behind l_beta) For Re(2 - alpha) in (-eps_ind, 1) and every root -mu of the window (integer, or with
     fractional part in [eps_ind, 1 - eps_ind]), 2 - alpha + j = -mu has a solution only for j = floor(-mu), and then
     beta_mu = 2 - alpha - {-mu} = 0: on a grid, |2 - alpha + j + mu| >= min(1 - x, x + eps_ind), x = Re(2 - alpha),
     for every other j.  And (r^z - r^-mu)/(z + mu)
     = r^-mu l_(z+mu)(r), with limit r^-mu log r as z + mu -> 0.  Control: a fractional part 1 - eps_ind/2.
  T3 (the n = 4 bookkeeping) For sample parameters, the window roots of III.G'' Table 1.1 (class roots from III.D
     Lemma 4.1's formulas), c_mu := 2 - floor(-mu) companions with c_mu <= K_mu, floor(-mu) + c_mu + 1 = 3, and on a
     grid of (Re alpha_0, w = l_zf - Re alpha_0 + 2) with -eps_ind < w < 3 and l_zf < 3: (i) the remainder order
     c_mu + 1 - mu + min(0, Re beta_mu) of Lemma 3.3 exceeds w; (ii) the zf-orders of Proposition 4.4's
     Step 1.2 (iii) exceed l_zf (generic, s1 with k = 3, v1 with k = 2); (iii) those of Proposition 5.1 exceed l_zf.
     Controls: l_zf allowed up to 3 + eps_ind/2 (the source's range); one companion fewer.
  T4 (Proposition 5.1, Step 1) Scalar model N(lam) = (lam - a)(lam - b): for f = rho^(i eta), the source's pointwise
     choice u = N(alpha - 2)^-1 f leaves rho^-alpha (rho^2 N(rho d_rho))(rho^(alpha-2) u) - f = (N(alpha - 2 + i eta) /
     N(alpha - 2) - 1) f, of the size of f (no factor rho); the dilation-invariant inverse u = N(alpha - 2 + i eta)^-1 f
     leaves 0; for smooth f = 1 + rho the pointwise error is O(rho).  Control: eta = 0.

sympy, fractions.  python3 tfgraft5.py [--selftest | --mutants | --only k]
"""
import math
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

from damping5 import Checklist

r, mu, s, c, lam = sp.symbols("r mu s c lam")


# ------------------------------------------------------------------------------------------------- T1
def t1(control=0, verbose=False):
    """coefficient algebra: a monomial r^e is mapped by N_tf to N(-e) r^(e-2) + sgn i (-e - 3/2 - s) r^(e-1)"""
    chk = Checklist(verbose, quiet=control != 0)
    N = lambda x: (x - mu) * (x - c)
    ok = True
    a = sp.symbols("a")
    for eps in (1, -1):
        sgn = -eps if control == 1 else eps
        # (a) on rho^a = |sigma|^a r^-a: |sigma|^-2 L-bar^(sigma) gives |sigma|^a [N(a) r^(-a-2) + eps i (a - 3/2 - s)
        # r^(-a-1)] (from i sigma = eps i |sigma|); N_tf on |sigma|^a r^-a gives the coefficients below
        lhs = (N(a), eps * sp.I * (a - sp.Rational(3, 2) - s))
        rhs = (N(a), sgn * sp.I * (a - sp.Rational(3, 2) - s))          # -r d_r r^-a = a r^-a
        good = all(sp.cancel(x - y) == 0 for x, y in zip(lhs, rhs))
        chk(f"sigma = {'+' if eps == 1 else '-'}|sigma|: |sigma|^-2 L-bar^(sigma) = N_tf on rho^a", good)
        ok &= good
        # (b) the formal solutions: H = sum_j cj r^(j - mu), cj = (-eps i)^j phi_j
        phi = [sp.Integer(1)]
        for m in range(1, 5):
            phi.append(sp.cancel((mu - m - sp.Rational(1, 2) - s) * phi[m - 1] / N(mu - m)))
        for k in range(4):
            cj = [(-eps * sp.I)**j * phi[j] for j in range(k + 1)] + [0]
            # coefficient of r^(m - mu - 2): cj[m] N(mu - m) + sgn i cj[m-1] (mu - m + 1 - 3/2 - s)
            C = [sp.cancel(cj[m] * N(mu - m) + (sgn * sp.I * cj[m - 1] * (mu - m + 1 - sp.Rational(3, 2) - s)
                                                 if m >= 1 else 0)) for m in range(k + 2)]
            psi = -(mu - k - sp.Rational(3, 2) - s) * phi[k]
            good = all(x == 0 for x in C[:k + 1]) and sp.cancel(C[k + 1] - (-eps * sp.I)**(k + 1) * psi) == 0
            chk(f"sigma = {'+' if eps == 1 else '-'}|sigma|, k = {k}: N_tf h^(<=k) = (-+i)^(k+1) r^(k-1-mu) psi_k", good)
            ok &= good
    return ok


# ------------------------------------------------------------------------------------------------- T2
def t2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    epsi = Fr(1, 20)
    roots = [Fr(0), Fr(1), Fr(2), Fr(1, 20), Fr(1, 5), Fr(21, 20), Fr(6, 5), Fr(41, 20), Fr(11, 5)]
    if control == 1:
        roots = roots + [Fr(1) - epsi / 2]
    grid = [Fr(-1, 25) + Fr(k, 200) * (1 + Fr(1, 25)) for k in range(200)]          # Re(2 - alpha) in (-eps, 1)
    for m in roots:                                                                  # m = -mu
        fl, fr = math.floor(m), m - math.floor(m)
        if fr != 0 and not (epsi <= fr <= 1 - epsi) and control == 0:
            continue
        worst = min(abs(x + j - m) - min(1 - x, x + epsi) for x in grid for j in range(0, 6) if j != fl)
        good = worst >= 0
        chk(f"-mu = {m}: for j != floor(-mu) = {fl}, |2 - alpha + j + mu| >= min(1 - x, x + eps_ind), x = Re(2 - alpha)"
            f" (min slack {float(worst):.4f})", good)
        ok &= good
    z, m_, b = sp.symbols("z m b")
    l = lambda bb, x: (x**bb - 1) / bb
    good = sp.simplify((r**z - r**m_) / (z - m_) - r**m_ * l(z - m_, r)) == 0
    good &= sp.simplify(sp.limit(l(b, r), b, 0) - sp.log(r)) == 0
    chk("(r^z - r^-mu)/(z + mu) = r^-mu l_(z+mu)(r), and l_b -> log r as b -> 0", good)
    return ok and good


# ------------------------------------------------------------------------------------------------- T3
def class_roots(zU):
    """2 - lambda^Ups_(sl,l+j) for l + j <= 4 (III.D Lemma 4.1), as floats, with (type, (l, l+j))"""
    out = []
    lam0 = 0.5 + math.sqrt(2.25 + zU)
    out.append((2 - lam0, "s0c", (0, 2)))
    for l in (1, 2, 3):
        kap = l * (l + 2)
        A, B = 2 + 2 * kap + zU, kap * (kap + 1) + zU * kap
        d = math.sqrt(A * A - 4 * B)
        for j, sv in ((1, (A - d) / 2), (2, (A + d) / 2)):
            if l + j <= 4:
                out.append((2 - (0.5 + math.sqrt(0.25 + sv)), f"s{l}c", (l, l + j)))
    return out


def window(zU, ctl_fewer=False):
    """(mu, type, K, c) for the window (-3, 0] of III.G'' Table 1.1"""
    W = [(0, "s0", 3), (0, "s2", 3), (-1, "s1", 4), (-1, "v1", 3), (-1, "s3", 2), (-1, "v2", 2), (-2, "s4", 1),
         (-2, "v3", 1), (-2, "s2p", 0), (-2, "v2p", 0), (-2, "t2p", 0)]
    W += [(m, t, 2) for (m, t, _) in class_roots(zU)]
    out = []
    for (m, t, K) in W:
        cc = 2 - math.floor(-m + 1e-12)
        if ctl_fewer:
            cc -= 1
        out.append((m, t, K, cc))
    return out


def t3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    for zU in (0.01, 0.1, 0.3):
        cr = class_roots(zU)
        fr = [(-m) - math.floor(-m) for (m, _, _) in cr]
        good = all(0 < f < 0.25 for f in fr) and all(lj < 2 - m < lj + 0.25 for (m, _, (l, lj)) in cr)
        chk(f"z = {zU}: class roots lam^Ups in (l+j, l+j+1/4), fractional parts of -mu in (0, 1/4)", good)
        ok &= good
        epsi = min(min(f, 1 - f) for f in fr)
        W = window(zU, ctl_fewer=control == 2)
        good = all(cc <= (K - 2 if t == "s1" else K - 1 if t == "v1" else K) for (m, t, K, cc) in W) or control == 2
        good &= all(math.floor(-m + 1e-12) + cc + 1 == 3 for (m, t, K, cc) in W) or control == 2
        chk(f"z = {zU}: c_mu <= K_mu (s1: c + 2 <= 4, v1: c + 1 <= 3) and floor(-mu) + c_mu + 1 = 3", good)
        ok &= good
        top = 3 + epsi / 2 if control == 1 else 3
        bad = []
        # Re alpha_0 in (1, 2 + eps), w in (-eps, 3), refined where l_zf can reach 3
        agrid = [1 + ia / 60 for ia in range(1, 60)] + [2 + epsi * m / 6 for m in range(1, 6)]
        wgrid = [-epsi + (3 + epsi) * iw / 80 for iw in range(1, 80)] + [3 - epsi * m / 6 for m in range(1, 6)]
        for a in agrid:
            for w in wgrid:
                lz = w + a - 2
                if lz >= top:
                    continue
                for (m, t, K, cc) in W:
                    if -m >= w:
                        continue
                    frac = (-m) - math.floor(-m + 1e-12)
                    beta = 2 - a - frac
                    if cc + 1 - m + min(0, beta) <= w + 1e-12:
                        bad.append(("rem", a, w, m, t))
                    if t == "s1":
                        zf = min(a - 2, 0) + (cc + 2)
                    elif t == "v1":
                        zf = min(a - 2, 0) + (cc + 1) + 1
                    else:
                        zf = min(a - 2 - m, math.floor(-m + 1e-12)) + cc + 1
                    if zf <= lz + 1e-12:
                        bad.append(("zf", a, w, m, t))
                    if a < 2 and a + 1 + frac <= lz + 1e-12 and frac > 0:
                        bad.append(("conormal", a, w, m, t))
        good = not bad
        chk(f"z = {zU}, eps_ind = {epsi:.4f}: remainder orders > w and zf-orders > l_zf on the grid"
            + ("" if good else f" (first failure {bad[0]})"), good)
        ok &= good
    return ok


# ------------------------------------------------------------------------------------------------- T4
def t4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    rho = sp.symbols("rho", positive=True)
    aa, bb = sp.Rational(-1, 7), sp.Integer(-2)                        # two roots, neither at alpha - 2
    N = lambda x: (x - aa) * (x - bb)
    for al in (sp.Rational(5, 4), sp.Rational(3, 2), sp.Rational(9, 5)):
        for eta in ((sp.Integer(0),) if control == 1 else (sp.Integer(1), sp.Integer(3))):
            f = rho**(sp.I * eta)
            # rho^-alpha * rho^2 N(rho d_rho)(rho^(alpha-2) u), u = C rho^(i eta): = C N(alpha - 2 + i eta) rho^(i eta)
            pointwise = N(al - 2 + sp.I * eta) / N(al - 2) - 1
            invariant = N(al - 2 + sp.I * eta) / N(al - 2 + sp.I * eta) - 1
            good = sp.Abs(sp.N(pointwise)) > sp.Rational(1, 100) and sp.simplify(invariant) == 0
            chk(f"alpha = {al}, eta = {eta}: pointwise error ratio {sp.N(sp.Abs(pointwise), 4)} (no factor rho); "
                f"dilation-invariant inverse exact", good)
            ok &= good
        # smooth f = 1 + rho: pointwise u = 1/N(al-2) + rho/N(al-2): error coefficient of rho^1 is N(al-1)/N(al-2) - 1
        e1 = N(al - 1) / N(al - 2) - 1
        good = sp.simplify(e1) != 0
        chk(f"alpha = {al}: for smooth f = 1 + rho the pointwise error starts at rho^1 (coefficient {sp.N(e1, 4)})",
            good)
        ok &= good
    return ok


CHECKS = [("T1 (9.60) at n = 4: N_tf on the formal solutions, exactly (scalar model, mu, s, c symbolic)", t1, 1),
          ("T2 the pairing of roots with source exponents; (r^z - r^-mu)/(z + mu) = r^-mu l_(z+mu)", t2, 1),
          ("T3 the n = 4 bookkeeping: companions, remainder orders, zf-orders on a grid", t3, 2),
          ("T4 Proposition 9.35 Step 1: the pointwise choice leaves an error of the size of a conormal f", t4, 1)]


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
    print(f"tfgraft5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"tfgraft5.py mutants: {caught}/{total}")
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
