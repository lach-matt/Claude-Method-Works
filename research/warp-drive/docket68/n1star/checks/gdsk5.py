#!/usr/bin/env python3
"""gdsk5.py -- GAUGEDECAY5.md Round 3, task 2: the hypothesis (S_K) of Theorem R2.12, from the iota+- and K+-orders of
h' (III.J''' Proposition 5.4) and of D vartheta_tot(p') (III.I'''''''-III.I'''''''''''''' rows).  Computed.

Notation: near the corner of iota+ and K+, rho_+ = 1/r and rho_K = r/t_* (III.J''' section 0), so a function with
|b-derivatives| <= C rho_+^a rho_K^b = C r^-a (r/t_*)^b has iota+-order a and K+-order b, Lemma R2.11's (a_iota, b_K).

  K1 (exact) Corner conormality of products.  With t = 1/(rho_+ rho_K), r = 1/rho_+: t d_t = -rho_K d_rhoK and
     r d_r|_t = -rho_+ d_rho+ + rho_K d_rhoK; for F = t^-c (log t)^k r^-m (k = 0, 1, 2), every (t d_t)^i (r d_r)^j F
     (i + j <= 3) is rho_+^(c+m) rho_K^c times a polynomial of degree <= k in log rho_+, log rho_K, so F has orders
     (c + m, c), exactly for k = 0 and minus for k > 0 (rho_+^-(c+m-eta) rho_K^-(c-eta) |.| -> 0 along every path
     (s, s^a) into the corner, eta > 0).  Control: with -eta in place of eta the quotient is unbounded.
  K2 (exact) The rows of III.I''''''''' Definition 2.1 and III.I'''''''''''''' Definition 1.3 near K+, where chi_K = 1
     and vartheta_{nu,#}(W) = (1/2) Box^Ups omega_nu(W) = (1/2)[a^(K+1) (A1 w^K + A2 w^(K-1)) + a^(K+2) A2 w^K]
     (III.I''''''''' (2.2), Lemma 2.2 (d)).  With w^i of spatial order sigma - i ((2.1)), a^(j) of rate rate0 + j, and
     A1, A2 gaining 1 and 2 spatial orders (K3), every type (s1, v1, s0, s2, c0, c1 and the rotation rows) has joint
     orders (iota+, K+) = (lambda + 1, kappa_nu) with kappa_nu = lambda + 4 (s1, v1, s0, s2, rot) and lambda + d + 3
     (c0, c1): the values of Lemma 2.2 (b) and (d), now at the corner jointly.  Control: A1 without its gain gives
     iota+-order lambda, contradicting Lemma 2.2 (b).
  K3 (exact) The gains of K2 on five-dimensional Tangherlini.  In the outgoing chart of III.B (3.4), (3.6) (as admbox5
     B1), for Box^Ups := 2 (delta + E^Ups) G delta^*, E^Ups k := -gam (2 iota_{g^-1 c} k - (2/3)(1 - e) c tr_g k),
     c = |x|^-1 dt (III.B (6.1)), and a stationary class 1-form U of spatial order q (q = 3, 7/2, general angular
     profiles), Box^Ups(phi(t_*) U) = phi A0 U + phi' A1 U + phi'' A2 U with A1 U = O(r^-(q+1)) and A2 U = O(r^-(q+2))
     in an orthonormal frame.  Control: with c = dt (no |x|^-1) A1 U is only O(r^-q).
  K4 (exact, rational samples) The inequalities of (S_K) and Lemma R2.11.  For gam in (0, 1/4), e in (0, 1),
     delta_# = (1 - e) gam, lambda_# = 3/2 + delta_#, alpha = 4 + eps_K with eps_K < delta_#, every beta in (0, delta_#)
     and a loss eta = delta_#/8 for the orders written "w-": h' (iota+ lambda_#, K+ alpha), h_rem (lambda_#-,
     (alpha - 2)-), the rows (lambda_# + 1-, kappa > lambda_# + 3) and J_h = E G h + D vartheta (|x|^-1 gains one
     iota+-order) meet (S_K) and Lemma R2.11 (a_iota > beta + 5/2, b_K > 1/2), with beta = alpha_sf + 2 in (0, 1).
     Controls: beta = delta_# fails (h' has iota+-order exactly lambda_#), and gam = 0 leaves no beta > 0.
  K5 (exact) The class.  G = O(2) x O(2) acting on R^4: the G-fixed subspaces of the row coefficient spaces have
     dimensions S_0: 1, S_1: 0, S_2 (harmonic quadratics): 1 (spanned by x1^2 + x2^2 - x3^2 - x4^2), so(4): 0 (the
     rotation rows and v1), the black-hole parameters R x so(4): 1.  So in the class only the rows s0, s2, c0 carry
     parameters.  Control: the torus T^2 alone fixes a 2-dimensional subspace of so(4) (R_12, R_34) -- the reflections
     are what remove the rotation rows.

Labels: computed (exact, sympy).  Run: python3 checks/gdsk5.py   (a few minutes)
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

# ---------------------------------------------------------------- K1


def k1(control=False):
    rp, rk, t, r, s = sp.symbols('rho_p rho_K t r s', positive=True)
    to = {t: 1/(rp*rk), r: 1/rp}
    ok_chain = True
    al, be = sp.symbols('alpha beta')
    F = t**al*r**be
    Fr_ = F.subs(to)
    ok_chain &= sp.simplify(sp.powsimp((-rk*sp.diff(Fr_, rk) - al*Fr_), force=True)) == 0
    ok_chain &= sp.simplify(sp.powsimp((-rp*sp.diff(Fr_, rp) + rk*sp.diff(Fr_, rk) - be*Fr_), force=True)) == 0
    eta = sp.Rational(1, 10)*(-1 if control else 1)
    ok = ok_chain
    for (c, m, k) in [(sp.Rational(5, 2), sp.Rational(1, 2), 0), (sp.Rational(9, 2), 2, 1), (3, sp.Rational(3, 2), 2)]:
        F = t**(-c)*sp.log(t)**k*r**(-m)
        for i, j in [(a, b) for a in range(4) for b in range(4) if a + b <= 3]:
            G = F
            for _ in range(i):
                G = t*sp.diff(G, t)
            for _ in range(j):
                G = r*sp.diff(G, r)
            Q = sp.expand(sp.simplify(G/(t**(-c)*r**(-m))))
            Lt = sp.Symbol('Lt')
            Qp = sp.Poly(Q.subs(sp.log(t), Lt), Lt) if Q.has(t) or Q.has(Lt) else None
            if Q.free_symbols - {t}:
                ok = False
            if Qp is not None and Qp.degree() > k:
                ok = False
            Gc = sp.expand_log((G*rp**(-(c + m) + eta)*rk**(-c + eta)).subs(to), force=True)
            for a in (1, 2, sp.Rational(1, 2)):
                lim = sp.limit(Gc.subs({rp: s, rk: s**a}), s, 0, '+')
                if lim != 0:
                    ok = False
    print("  K1%s: chain rule for t d_t, r d_r in (rho_+, rho_K): %s; products t^-c log^k t r^-m have orders "
          "(c + m, c) (the weighted quotient -> 0 into the corner): %s" % (" control (-eta in place of eta)"
                                                                           if control else "", ok_chain, ok),
          flush=True)
    return ok

# ---------------------------------------------------------------- K2


LAM, MU0, MU1 = sp.symbols('lambda mu_c0 mu_c1', real=True)
TYPES = {   # K_tau, sigma_tau, rate of a (= e_nu except s0, where a = A_nu ~ t^(1 - lambda)), kappa read (I10:204-205)
    's1': (4, 0, LAM - 1, LAM + 4),
    'v1': (3, -1, LAM, LAM + 4),
    's0': (4, 0, LAM - 1, LAM + 4),
    's2': (3, -1, LAM, LAM + 4),
    'c0': (2, MU0 - 1, LAM - MU0, LAM - MU0 + 3),
    'c1': (2, MU1 - 1, LAM - MU1, LAM - MU1 + 3),
    'rot': (3, -1, LAM, LAM + 4),
}


def k2(control=False):
    g1 = 0 if control else 1
    ok = True
    rows = []
    for name, (K, sig, rate0, kap) in TYPES.items():
        terms = [(K + 1, g1, K), (K + 1, 2, K - 1), (K + 2, 2, K)]          # (j: a^(j), gain of A, tower index i)
        iota = [rate0 + j + (sig - i + gain) for j, gain, i in terms]
        kplus = [rate0 + j for j, gain, i in terms]
        # the minimum over terms, read off the coefficient of 1 (all differ by integer constants)
        imin = min(iota, key=lambda e: sp.simplify(e - LAM - 10))
        kmin = min(kplus, key=lambda e: sp.simplify(e - LAM - 10))
        good = sp.simplify(imin - (LAM + 1)) == 0 and sp.simplify(kmin - kap) == 0
        rows.append((name, sp.simplify(imin), sp.simplify(kmin), good))
        ok &= good
    print("  K2%s: (type, iota+-order, K+-order, = (lambda + 1, kappa_nu) of III.I''''''''' Lemma 2.2 (b), (d)): %s"
          % (" control (A1 without its gain)" if control else "", rows), flush=True)
    return ok

# ---------------------------------------------------------------- K3


def k3(control=False):
    from admbox5 import outgoing_geo
    from hgauge5 import theta
    from rwgauge5 import N, X, r, s, th
    T = X[0]
    G, p = outgoing_geo()
    gam_, e_ = sp.symbols('gamma_Ups e_Ups', positive=True)
    cU = [1, p, 0, 0, 0] if control else [1/r, p/r, 0, 0, 0]          # c_Ups = |x|^-1 dt, dt = dT + p dr
    cvec = [sum(G.gi[a, b]*cU[b] for b in range(N)) for a in range(N)]

    def Eups(k):
        trk = G.tr(k)
        iota = [sum(cvec[a]*k[a][m] for a in range(N)) for m in range(N)]
        return [-gam_*(2*iota[m] - sp.Rational(2, 3)*(1 - e_)*cU[m]*trk) for m in range(N)]

    def boxU(w):
        L = G.lie(w)
        trL = G.tr(L)
        GL = [[L[a][b] - G.g[a, b]*trL/2 for b in range(N)] for a in range(N)]
        th_ = theta(G, L)
        E_ = Eups(GL)
        return [th_[m] + E_[m] for m in range(N)]
    phi = sp.Function('phi')(T)
    P0, P1, P2 = sp.symbols('P0 P1 P2')
    a, b, c = [sp.Function(n)(th) for n in ('a', 'b', 'c')]
    ok = True
    report = []
    for q in (3, sp.Rational(7, 2)):
        U = [r**(-q)*a, r**(-q)*b, r**(1 - q)*c, 0, 0]
        E = boxU([phi*u for u in U])
        rep = {sp.Derivative(phi, (T, 2)): P2, sp.Derivative(phi, T): P1}
        E = [sp.expand(e.subs(rep).subs(phi, P0)) for e in E]
        jets = {}
        for fn in (a, b, c):
            for k in range(3):
                jets[sp.diff(fn, th, k) if k else fn] = sp.Symbol('%s%d' % (fn.func.__name__, k))
        frame = [1, 1, 1/r, 1, 1]                                   # orthonormal-frame scaling of the components
        for coef, order in ((P1, q + 1), (P2, q + 2)):
            lims = []
            for m in range(3):
                ex = sp.diff(E[m], coef)*frame[m]
                ex = ex.subs({sp.Derivative(fn, (th, k)): jets[sp.diff(fn, th, k)] for fn in (a, b, c)
                              for k in (2, 1)}).subs({fn: jets[fn] for fn in (a, b, c)})
                lims.append(sp.limit(sp.simplify(ex*r**order), r, sp.oo))
            fin = all(l.is_finite for l in lims)
            report.append((str(q), 'A1' if coef == P1 else 'A2', fin))
            ok &= fin
    print("  K3%s: Box^Ups(phi(t_*) U), U of spatial order q: (q, coefficient, r^(q+1) A1 U resp. r^(q+2) A2 U "
          "finite in an orthonormal frame): %s" % (" control (c_Ups = dt)" if control else "", report), flush=True)
    return ok

# ---------------------------------------------------------------- K4


def sk_inequalities(gam, e, beta, eta):
    d = (1 - e)*gam
    lam = Fr(3, 2) + d
    epsK = d/2
    alpha = 4 + epsK
    kappa_min = lam + 3                       # every kappa_nu exceeds lambda_# + 3 (I10:206)
    h_prime = (lam, alpha)                    # iota+, K+ (exact, simple pole at lambda_#)
    h_rem = (lam - eta, alpha - 2 - eta)
    rows = (lam + 1 - eta, kappa_min)
    h_io = min(h_prime[0], h_rem[0])
    h_k = min(h_prime[1], h_rem[1])
    J = (min(h_io + 1, rows[0]), min(h_k, rows[1]))
    conds = [0 < beta < 1,
             h_io > Fr(3, 2) + beta, h_k > Fr(1, 2),
             rows[0] > Fr(5, 2) + beta, rows[1] > Fr(1, 2),
             J[0] > beta + Fr(5, 2), J[1] > Fr(1, 2)]
    return all(conds)


def k4(control=False):
    gams = [Fr(1, 100), Fr(1, 20), Fr(1, 8), Fr(1, 5), Fr(249, 1000)]
    es = [Fr(1, 100), Fr(1, 3), Fr(1, 2), Fr(9, 10), Fr(99, 100)]
    ok = True
    n = 0
    if control:
        # the claim that fails: (S_K) holds at the edge beta = delta_#, or with no damping (gam = 0) for some beta > 0
        edge = any(sk_inequalities(gam, e, (1 - e)*gam, (1 - e)*gam/8) for gam, e in itertools.product(gams, es))
        undamped = any(sk_inequalities(Fr(0), e, b, Fr(1, 1000)) for e in es for b in (Fr(1, 10**6), Fr(1, 100)))
        print("  K4 control: (S_K) holds at beta = delta_# for some sample: %s; with gam = 0 for some beta > 0: %s"
              % (edge, undamped), flush=True)
        return edge or undamped
    for gam, e in itertools.product(gams, es):
        d = (1 - e)*gam
        eta = d/8
        for frac in (Fr(1, 100), Fr(1, 2), Fr(3, 4)):
            ok &= sk_inequalities(gam, e, frac*d, frac*d/8 if frac < Fr(1, 2) else eta)
            n += 1
    print("  K4: (S_K) and Lemma R2.11 hold at %d samples (gam, e, beta in (0, delta_#)): %s" % (n, ok), flush=True)
    return ok

# ---------------------------------------------------------------- K5


def k5(control=False):
    x = sp.symbols('x1:5')
    rot1 = lambda P: x[0]*sp.diff(P, x[1]) - x[1]*sp.diff(P, x[0])
    rot2 = lambda P: x[2]*sp.diff(P, x[3]) - x[3]*sp.diff(P, x[2])
    ref1 = lambda P: P.subs(x[1], -x[1])
    ref2 = lambda P: P.subs(x[3], -x[3])

    def harmonic_basis(l):
        mons = [sp.Mul(*c) for c in itertools.combinations_with_replacement(x, l)] if l else [sp.Integer(1)]
        cs = sp.symbols('c0:%d' % len(mons))
        P = sum(ci*mi for ci, mi in zip(cs, mons))
        lap = sp.expand(sum(sp.diff(P, xi, 2) for xi in x))
        eqs = sp.Poly(lap, *x).coeffs() if lap != 0 else []
        sol = sp.solve(eqs, cs, dict=True)
        P = P.subs(sol[0]) if sol else P
        free = sorted(P.free_symbols & set(cs), key=str)
        return [sp.expand(P.subs({f: (1 if f == g else 0) for f in free})) for g in free], mons

    def fixed_dim(basis, ops):
        cs = sp.symbols('d0:%d' % len(basis))
        P = sum(ci*bi for ci, bi in zip(cs, basis))
        eqs = []
        for op in ops:
            ex = sp.expand(op(P))
            if ex != 0:
                eqs += sp.Poly(ex, *x).coeffs()
        M = sp.Matrix([[sp.diff(eq, ci) for ci in cs] for eq in eqs]) if eqs else sp.zeros(0, len(cs))
        return len(cs) - (M.rank() if eqs else 0)
    full = [rot1, rot2, lambda P: ref1(P) - P, lambda P: ref2(P) - P]
    torus = [rot1, rot2]
    ops = torus if control else full
    dims = {}
    for l in (0, 1, 2):
        B, _ = harmonic_basis(l)
        dims['S_%d (dim %d)' % (l, len(B))] = fixed_dim(B, ops)
    # so(4) by conjugation: generators E_ij, A -> [J, A] for the torus generators, S A S for the reflections
    J1 = sp.zeros(4); J1[0, 1], J1[1, 0] = -1, 1
    J2 = sp.zeros(4); J2[2, 3], J2[3, 2] = -1, 1
    S1 = sp.diag(1, -1, 1, 1)
    S2 = sp.diag(1, 1, 1, -1)
    cs = sp.symbols('a0:6')
    A = sp.zeros(4)
    for k_, (i, j) in enumerate(itertools.combinations(range(4), 2)):
        A[i, j], A[j, i] = cs[k_], -cs[k_]
    eqs = list(J1*A - A*J1) + list(J2*A - A*J2)
    if not control:
        eqs += list(S1*A*S1 - A) + list(S2*A*S2 - A)
    M = sp.Matrix([[sp.diff(eq, c_) for c_ in cs] for eq in eqs])
    dims['so(4) (dim 6)'] = 6 - M.rank()
    cos2 = x[0]**2 + x[1]**2 - x[2]**2 - x[3]**2
    inv_cos2 = all(sp.expand(op(cos2)) == 0 for op in full)
    want = {'S_0 (dim 1)': 1, 'S_1 (dim 4)': 0, 'S_2 (dim 9)': 1, 'so(4) (dim 6)': 0}
    if control:
        res = dims['so(4) (dim 6)'] == 0
        print("  K5 control (torus only): fixed dimensions %s; so(4) fixed = 0: %s" % (dims, res), flush=True)
        return res
    ok = dims == want and inv_cos2
    print("  K5: G-fixed dimensions %s (expected %s); x1^2 + x2^2 - x3^2 - x4^2 is G-fixed: %s; so the black-hole "
          "parameters R x so(4) have a 1-dimensional fixed space: %s" % (dims, want, inv_cos2, ok), flush=True)
    return ok


CHECKS = [("K1", k1), ("K2", k2), ("K3", k3), ("K4", k4), ("K5", k5)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
