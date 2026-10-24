#!/usr/bin/env python3
"""cone5.py -- [Hin26] section 11.1 in five dimensions: the structure of the dynamical linearized operator, its
admissibility and the regularity of forward solutions (N1STAR-PROOF.md section 10.42; ROUTES-OPEN.md 4.43; D108).
Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) section 11 studies L_(g,g0) for g = g_(b0,b,-S) + h, g_(b0,b,-S) := (1 - chi_K)
phi*_(-S) g_b0 + chi_K g_b ((11.1), p. 218), with h in index sets E+ at iota+ subject to "(1, 0) in E+, min Re E+ >= 1"
((11.6), p. 220): "The requirement (1, 0) in E+ ensures that smooth decaying perturbations are allowed" (p. 221), since
"the two metrics g_b0 + h and g_b0,b,0 ... differ near (iota+)^o by chi_K (g_b - g_b0) in rho_+ C^oo" (Remark 11.7, p.
224); Corollary 11.9's proof: "Since g_b0,b,-S - g-bar is a smooth section of S^2 T* and of class rho_+ C^oo near
(iota+)^o, we have P(g0, g0) in rho_+^3 C^oo there" (p. 225); Corollary 11.10 takes "l_+ in (delta, 1), and l_K in (2, 2
+ eps_K]" (p. 225); and Theorem 11.12 states [Hin26c] Theorem 11.1 "in the form using unweighted b-densities as in
[Hin26c, (11.5)-(11.6a)]" with "beta_+ in (1/2, 1/2 + eps_ind) and beta_I in (beta_+, 1); fix delta > beta_+ - 1/2", u
in H^(k, beta_I, beta_+ - delta, -3/2)_b (pp. 225-226); [Hin26c] p. 228: "mu_b := rho_I^3 rho_+^4 rho_K |dt dx| ... (in
which case rho_I^3 rho_+^4 rho_K = 1/(t* r^3))" and (11.5) "beta_I = alpha_I + 3/2, beta_+ = alpha_+ + 2".  In five
dimensions:

  C1 (computed, exact) The densities and the weights.  With [Hin26c]'s (11.4), rho_I = t*/(t* + r), rho_+ = (t* +
     r)/(t* r), rho_K = r/(t* + r): 1/(t* r^n) = rho_I^n rho_+^(n+1) rho_K, so the unweighted b-density shifts the
     weights at (I+, iota+, K+) by (n/2, (n+1)/2, 1/2) -- (3/2, 2, 1/2) at n = 3, his (11.5), and (2, 5/2, 1/2) at n = 4.
     So alpha_sf + n/2 in (0, eps_ind) is beta_+ in (1/2, 1/2 + eps_ind) in both dimensions; his delta > beta_+ - 1/2 is
     Theorem 10.1's delta > alpha_sf + 3/2; with section 10.41's sf-loss 0, the five-dimensional forward solution is at
     (beta_I, beta_+, -3/2), the K+ weight 1/2 - aleph with aleph = 2 in both.  A radiation field r^-((n-1)/2) is of
     I+ order (n-1)/2 against mu_b and -1/2 against |dt dx| in both dimensions (rho_I rho_+ = 1/r), so [Hin26c]'s
     threshold alpha_I < -1/2 + S-bar ((10.2), p. 201), read at n = 4, is beta_I < (n-1)/2 + S-bar: his 1 at n = 3
     (S-bar's min 0), 3/2 at n = 4 -- the threshold's value at n = 4 a reading, the radiation field's order computed.
     Control: the shifts claimed dimension-free, caught by the density identity they are read against.
  C2 (computed, exact) The background differences at iota+.  Homogeneity along rays in the cone, in Cartesian
     components: a change of mass, r^-(n-2) k (x) k (Kerr-Schild, k null), of degree -(n - 2); of rotation, r^-n (dt
     (x)_s w), w = x^1 dx^2 - x^2 dx^1, of degree -(n - 1); a boost, L_X of the mass term, X = t d_x1 + x^1 d_t, of
     degree -(n - 2) -- each nonzero.  So iota+ orders 2, 3, 2 in five dimensions; four dimensions 1, 2, 1, his rho_+
     C^oo.  Control: the five-dimensional mass change claimed of order 1.
  C3 (computed, exact) Ric of the cut-off mass interpolation.  For g = eta + M(t, r) r^-(n-2) (dt + dr)^2 on
     R^(1,n), M = mu_0 + d F(r/t), F arbitrary: Ric = 0 for F constant (Tangherlini, Schwarzschild); its part linear in
     the deviation, d F's, is homogeneous of degree -n, nonzero, and vanishes where F is constant; its quadratic part
     (mu_0 d, d^2) is homogeneous of degree -(2n - 2), and there is no cubic part.  So Ric of the cut-off mass
     interpolation is of iota+ order 4 in five dimensions, supported where the cut-off varies; four dimensions 3, his
     Corollary 11.9 (rotation and boost are deduced in section 10.42(c), not computed here).
     Control: the five-dimensional order claimed 3.

Run: python3 cone5.py --selftest | --mutants | --only k [--verbose]   (seconds).
"""
import sys
import time

import sympy as sp

from damping5 import Checklist


# ------------------------------------------------------------------------------------------------- C1
def c1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    t, r = sp.symbols("t r", positive=True)
    rI, rP, rK = t / (t + r), (t + r) / (t * r), r / (t + r)
    shift = {}
    for n in (3, 4):
        sh = (sp.Rational(n, 2), sp.Rational(n + 1, 2), sp.Rational(1, 2))
        if control == 1:
            sh = (sp.Rational(3, 2), 2, sp.Rational(1, 2))
        # an L^2 weight moves by half the density's exponent: the shifts are read against the identity itself
        ok = sp.simplify(rI**(2 * sh[0]) * rP**(2 * sh[1]) * rK**(2 * sh[2]) - 1 / (t * r**n)) == 0
        shift[n] = sh
        chk(f"n = {n}: 1/(t* r^{n}) = rho_I^{n} rho_+^{n + 1} rho_K; shifts {sh}", ok)
    chk("n = 3: his (11.5), beta_I = alpha_I + 3/2, beta_+ = alpha_+ + 2, and K+ 1/2",
        shift[3] == (sp.Rational(3, 2), 2, sp.Rational(1, 2)))
    chk("n = 4: (2, 5/2, 1/2)", shift[4] == (2, sp.Rational(5, 2), sp.Rational(1, 2)))
    good = True
    for ei in (sp.Rational(1, 100), sp.Rational(1, 10), sp.Rational(1, 2), 1):
        for j in range(1, 10):
            x = ei * sp.Rational(j, 10)                        # alpha_sf + n/2 in (0, eps_ind)
            for n in (3, 4):
                a = x - sp.Rational(n, 2)
                bp = a + shift[n][1]
                good &= sp.Rational(1, 2) < bp < sp.Rational(1, 2) + ei
                if n == 3:
                    good &= bp - sp.Rational(1, 2) == a + sp.Rational(3, 2)        # his delta threshold
    chk("beta_+ = alpha_sf + (n + 1)/2 in (1/2, 1/2 + eps_ind) at n = 3 and 4; his delta > beta_+ - 1/2 is "
        "delta > alpha_sf + 3/2 (Theorem 10.1)", good)
    aleph = 2
    chk("the K+ weight 1/2 - aleph = -3/2, his (11.22)", sp.Rational(1, 2) - aleph == -sp.Rational(3, 2))
    # the radiation field r^-((n-1)/2) at I+: rho_I rho_+ = 1/r, so its I+ order is (n-1)/2 against mu_b and
    # (n-1)/2 - n/2 = -1/2 against |dt dx| in both dimensions; his threshold alpha_I < -1/2 + S-bar ([Hin26c] (10.2))
    # is then beta_I < (n-1)/2 + S-bar, with min spec S-bar = 0 (section 10.25): 1 at n = 3, his (11.22), 3/2 at n = 4
    # -- on the reading that (10.2)'s -1/2 stands at n = 4; only the radiation field's order is computed here
    one_over_r = sp.simplify(rI * rP - 1 / r) == 0
    rad = {n: (sp.Rational(n - 1, 2), sp.Rational(n - 1, 2) - shift[n][0]) for n in (3, 4)}
    top = {n: rad[n][1] + shift[n][0] for n in (3, 4)}            # alpha_I < -1/2, S-bar's min 0, shifted by n/2
    chk(f"the radiation field's I+ order (n-1)/2 against mu_b, -1/2 against |dt dx| ({rad}); the top of beta_I: "
        f"{top[3]} at n = 3 (his beta_I < 1), {top[4]} at n = 4 (reading (10.2) there)",
        one_over_r and rad[3][1] == rad[4][1] == -sp.Rational(1, 2) and top == {3: 1, 4: sp.Rational(3, 2)})
    return chk.ok


# ------------------------------------------------------------------------------------------------- C2
def degree(comps, X, p):
    """the common homogeneity degree of the nonzero components at the point p along the ray lam p, or None"""
    lam = sp.Symbol("lam", positive=True)
    at1 = {x: v for x, v in zip(X, p)}
    atl = {x: lam * v for x, v in zip(X, p)}
    degs = set()
    for c in comps:
        c1v = sp.nsimplify(sp.simplify(c.subs(at1)))
        if c1v == 0:
            continue
        ratio = sp.simplify(c.subs(atl) / c1v)
        d = sp.simplify(sp.log(ratio) / sp.log(lam))
        if not d.is_number:
            return None
        degs.add(sp.nsimplify(d))
    return degs.pop() if len(degs) == 1 else None


def c2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    want = {4: (-2, -3, -2), 3: (-1, -2, -1)}
    if control == 1:
        want[4] = (-1, -3, -2)
    for n in (4, 3):
        t = sp.Symbol("t", positive=True)
        xs = sp.symbols("x1:%d" % (n + 1), real=True)
        X = [t, *xs]
        N = n + 1
        r = sp.sqrt(sum(x**2 for x in xs))
        k = sp.Matrix([1, *[x / r for x in xs]])                # dt + x-hat . dx, null for eta = diag(-1, 1, ...)
        mass = r**(-(n - 2)) * k * k.T
        dt = sp.Matrix([1] + [0] * n)
        w = sp.Matrix([0, -xs[1], xs[0]] + [0] * (n - 2))       # x^1 dx^2 - x^2 dx^1
        rot = r**(-n) * (dt * w.T + w * dt.T)
        Xv = [xs[0]] + [t] + [0] * (n - 1)                      # X = x^1 d_t + t d_x1, Killing for eta
        boost = sp.zeros(N, N)
        for a in range(N):
            for b in range(N):
                boost[a, b] = (sum(Xv[c] * sp.diff(mass[a, b], X[c]) for c in range(N)) +
                               sum(mass[c, b] * sp.diff(Xv[c], X[a]) + mass[a, c] * sp.diff(Xv[c], X[b])
                                   for c in range(N)))
        p = [sp.Rational(7)] + [sp.Rational(j + 1, 2) for j in range(n)]
        got = tuple(degree(list(T), X, p) for T in (mass, rot, boost))
        chk(f"n + 1 = {n + 1}: the mass change, rotation and boost of degrees {got}, iota+ orders "
            f"{tuple(-g if g is not None else None for g in got)}", got == want[n])
    return chk.ok


# ------------------------------------------------------------------------------------------------- C3
def ricci_ks(n):
    """Ric of g = eta + H (dt + dr)^2, H = M(t, r) r^-(n-2), on R^(1,n) in polar coordinates, frame components"""
    t, r = sp.symbols("t r", positive=True)
    M = sp.Function("M")(t, r)
    H = M * r**(-(n - 2))
    if n == 3:
        th, ph = sp.symbols("theta phi")
        ang, sph = [th, ph], [1, sp.sin(th)**2]
    else:
        th, p1, p2 = sp.symbols("theta p1 p2")
        ang, sph = [th, p1, p2], [1, sp.cos(th)**2, sp.sin(th)**2]
    X = [t, r, *ang]
    N = len(X)
    g = sp.diag(-1, 1, *[r**2 * s for s in sph])
    g[0, 0] += H
    g[0, 1] += H
    g[1, 0] += H
    g[1, 1] += H
    gi = sp.diag(-1, 1, *[1 / (r**2 * s) for s in sph])        # Kerr-Schild: g^-1 = eta^-1 - H k# k#, k# = (-1, 1)
    gi[0, 0] -= H
    gi[0, 1] += H
    gi[1, 0] += H
    gi[1, 1] -= H
    D = sp.diff
    Gam = [[[sp.expand(sum(gi[a, e] * (D(g[e, b], X[c]) + D(g[e, c], X[b]) - D(g[b, c], X[e])) for e in range(N)) / 2)
             for c in range(N)] for b in range(N)] for a in range(N)]
    Ric = sp.zeros(N, N)
    for b in range(N):
        for d in range(b, N):
            v = sum(D(Gam[a][b][d], X[a]) - D(Gam[a][b][a], X[d]) for a in range(N))
            v += sum(Gam[a][a][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][a] for a in range(N) for e in range(N))
            Ric[b, d] = Ric[d, b] = sp.simplify(v)
    frame = [1, 1] + [r * sp.sqrt(s) for s in sph]
    comps = [sp.simplify(Ric[a, b] / (frame[a] * frame[b])) for a in range(N) for b in range(a, N)]
    return comps, t, r, M


def c3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    lam, d, mu0, eps = sp.symbols("lam d mu0 eps", positive=True)
    F = sp.Function("F")
    for n in ((4,) if control else (4, 3)):
        comps, t, r, M = ricci_ks(n)
        # M = eps (mu0 + d F(r/t)); the eps^k piece is of order k in the metric's deviation r^-(n-2) (mu0 + d F)
        full = [c.subs(M, eps * (mu0 + d * F(r / t))).doit() for c in comps]
        piece = lambda k: [sp.simplify(sp.diff(e, eps, k).subs(eps, 0) / sp.factorial(k)) for e in full]
        p0, p1, p2, p3 = piece(0), piece(1), piece(2), piece(3)
        flat = all(c == 0 for c in p0)
        vac = all(sp.simplify(c.subs(d, 0)) == 0 for c in p1 + p2)          # Tangherlini (F constant) is vacuum
        lead = [sp.simplify(c.coeff(d, 1)) for c in p1]                       # the d-linear, mu0-free piece
        want_lin = n if control != 1 else 3

        def hom(cs, k):
            return all(sp.simplify(c.subs({t: lam * t, r: lam * r}, simultaneous=True) * lam**k - c) == 0 for c in cs)
        hom1 = hom(lead, want_lin)
        hom2 = hom(p2, 2 * n - 2)
        nothree = all(c == 0 for c in p3)
        nonzero = any(c != 0 for c in lead)
        s = sp.Symbol("s")
        const = all(sp.simplify(c.replace(F, sp.Lambda(s, 1)).doit()) == 0 for c in lead)
        if verbose:
            print(f"      n = {n}: flat {flat}, vacuum {vac}, lead homogeneous {hom1}, quadratic {hom2}, no cubic "
                  f"{nothree}, nonzero {nonzero}, zero where F is constant {const}")
        chk(f"n + 1 = {n + 1}: Ric = 0 for F constant; its part linear in the deviation homogeneous of degree "
            f"-{want_lin}, nonzero, zero where F is constant; the quadratic part of degree -{2 * n - 2}, no cubic",
            flat and vac and hom1 and hom2 and nothree and nonzero and const)
    return chk.ok


CHECKS = [("C1 the b-density shifts (n/2, (n+1)/2, 1/2): his (11.5) at n = 3, (2, 5/2, 1/2) at n = 4; weights", c1, 1),
          ("C2 the background differences at iota+: mass, rotation, boost of orders 2, 3, 2 (four: his 1, 2, 1)", c2, 1),
          ("C3 Ric of the cut-off mass interpolation: iota+ order 4, where the cut-off varies (four: his 3)", c3, 1)]


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
    print(f"cone5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"cone5.py mutants: {caught}/{total}")
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
