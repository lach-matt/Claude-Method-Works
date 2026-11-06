"""order5.py -- SETTLE-GLAM5 round 4, (Pr): Propositions 9.8 and 9.9 of N1STAR-PROOF.md (as of 82a7e95) read at
every order k, the places where k enters computed.

Setting. On P the scaled norms |f|_(j,P) = sum_(i + |beta| <= j) lam^i ||d^i Omega^beta f|| (9.2); Lemma 9.3(a):
||d^i f||_inf <= C lam^(-3-i) t^(-3/2) |f|_(i+3,P) (the cost of three: H^3 in L^inf on four-dimensional slices);
Lemma 9.3(b): ||f|| <= C ||d_r f|| for f vanishing on {v = v_start}. E(tau) of (9.8) controls the w-derivatives of
orders 1 .. k + 1 (and order 0 through 9.3(b)); "w-order" of a factor = the number of derivatives on w.

  O1 (exact, enumeration) the product split at order k. Every source monomial of Proposition 9.8's commuted equation
     at level j <= k (nonlinear terms of N(w): at least two factors w-or-dw, total w-order <= j + 2, no factor of
     w-order j + 2, which would be the principal part; the quasilinear commutators d^i g . d^(j-i+1) d w, i >= 1)
     is estimated with its factor of highest w-order in L^2 (needs w-order <= k + 1) and every other factor in sup
     (needs w-order + 3 <= k + 1, Lemma 9.3(a)). This works for every k >= 5 (checked k = 5..200), the minimal k
     being 5; so k = 6 (the record's) and every larger k are covered with constants C_k. Controls (the code under
     test mutated): with the Sobolev cost 4 in place of 3 the minimal k becomes 7, so the claim "k = 6 suffices"
     fails; with the split reversed (highest factor in sup) no k works.
  O2 (exact) the far region's closing at order k (Proposition 9.8): with the kernels C_k t^(-3/2) (B.dw, C.w, the
     commutators, d g_n) and C_k lam^-1 t^(-3/2) (the 1/lam coupling s G2), whose integrals over t >= lam^-2 are
     2 C_k lam and 2 C_k: the Gronwall factor exp(2 C_k (1 + lam)) is lam-free and k enters only through C_k; the
     nonlinear term C_k lam^-5 t^(-3/2) E^2 with E <= 2 M lam^K' t^(-1/2) returns C_k M^2 lam^(2K'-5) t^(-1/2),
     below M lam^K' / 2 for lam small exactly when K' > 5 (independent of k). Control: K' = 5 does not close.
  O3 (exact, sympy) the near region's bootstrap at order k (Proposition 9.9): for beta > 1, a > -beta,
     int_t^T t'^(-1-a) (T/t')^beta dt' <= t^-a (T/t)^beta / (beta + a), and log(T/t) <= (T/t)^beta / beta (control:
     without the factor (T/t)^beta the log is unbounded); with
     beta0(k) = max(2, 4 C(k) + 1) each integral of (9.9) returns C/(beta0 - 1) <= 1/4 of its bound; the nonlinear
     terms C B^2 lam^(-8 - 4 beta0) are below B/2 for lam small once K' > 8 + 4 beta0, which N = K + 4 +
     ceil(4 beta0(k)) gives for every K >= 6; and (P-iii)'s absorption K' - 2 beta0 >= K holds. Control (the order
     rule mutated): N = K + 4 + ceil(2 beta0) fails the closing at K = 6, beta0 = 4.
  O4 (exact, sympy) the commutation facts behind "every line holds at every order j <= k with c0 unchanged":
     [Z, L0] = 0 for Z in {d_tau, d_r, Omega_ab} (L0 = d_tau - xhat.d_x), [d_r, r^-c] = -c r^(-c-1) (the factor
     r^(-c-1)), [Omega, r^-c] = [d_tau, r^-c] = 0; and [Omega_12, box~] = 0 for g0 = eta + mu(v) r^-2 dv dv on every
     function (P6 of past5.py, recomputed). Controls: the Cartesian d_1 does not commute with L0; x1 d_2 + x2 d_1
     does not commute with box~.
  O5 (exact) Theorem P at order k: N(k) = K + 4 + ceil(4 beta0(k)) grows with k, so the approximant changes with k;
     g_app^(N(k)) - g_app^(N(6)) = sum_(j > N(6)) lam^j [g_j] is O(lam^N(6) t^(-3/2)) in C^1, inside (P-v)'s
     uniqueness class, so the solution built at order k is the g_lam built at order 6. And the orders used later:
     (P-iii) at order k gives d^i e for i <= k - 3; Proposition R3.1 at n derivatives needs k = n + 4.
Round 5 (SETTLE-GLAM5 R5.0, the round-4 verifier's reading): checks marked [arithmetic] compute a consequence of
rules or exponents entered by hand (the bootstrap's closing condition, the order rule, the growth of N(k)), and their
controls cannot fail under a mutation of the operator: they check the arithmetic of the deduction, not the deduction.
Labels: computed (exact; sympy and integer enumeration).

    python3 checks/order5.py
"""
import sys

import sympy as sp

import builtins as _builtins
import textwrap as _textwrap

_raw_print = _builtins.print


def print(*args, **kw):  # output lines are kept to 121 characters (wrapped, continuation indented)
    text = kw.pop("sep", " ").join(str(x) for x in args)
    for line in text.split("\n"):
        for piece in (_textwrap.wrap(line, 121, subsequent_indent="        ", break_long_words=True,
                                     replace_whitespace=False, drop_whitespace=True) or [""]):
            _raw_print(piece, **kw)


FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------- O1: the product split at order k

MCAP = 40  # triples and quadruples are enumerated for k <= MCAP; above it pairs dominate (see o1)


def monomials(k):
    """w-orders of the factors of every source monomial at levels j <= k (nonlinear terms and the quasilinear
    commutator terms of Proposition 9.8's commuted equation).  A monomial at level j has total w-order <= j + 2
    <= k + 2, so the union over j <= k is the set of tuples of total <= k + 2; w-order k + 2 occurs only in the
    principal part and is excluded."""
    out = set()
    for o1_ in range(0, k + 3):          # pairs (the quasilinear commutators (i, j - i + 2) are among them)
        for o2_ in range(0, min(o1_, k + 2 - o1_) + 1):
            out.add((o2_, o1_))
    if k <= MCAP:
        for m in (3, 4):
            def rec(rem, parts, lo):
                if len(parts) == m:
                    out.add(tuple(sorted(parts)))
                    return
                for o in range(lo, rem + 1):
                    rec(rem - o, parts + [o], o)
            for tot in range(0, k + 3):
                rec(tot, [], 0)
    return {mono for mono in out if max(mono) <= k + 1}


def split_ok(k, sob=3, reverse=False):
    """True when every monomial at order k has a split: highest factor in L^2 (w-order <= k + 1), the others in
    sup (w-order + sob <= k + 1)."""
    for mono in monomials(k):
        mono = sorted(mono)
        if reverse:
            l2, sups = mono[0], mono[1:]
        else:
            l2, sups = mono[-1], mono[:-1]
        if l2 > k + 1 or any(o + sob > k + 1 for o in sups):
            return False
    return True


def min_k(sob=3, reverse=False, kmax=200):
    ok = [split_ok(k, sob, reverse) for k in range(0, kmax + 1)]
    for k in range(1, kmax + 1):
        if all(ok[k:]):
            return k
    return None


def dominated(k):
    """every triple or quadruple of total <= k + 2 has its second-largest entry <= that of a pair of total
    <= k + 2 (the pair (k + 2 - o2, o2)), so pairs decide the split condition"""
    for m in (3, 4):
        def rec(rem, parts, lo):
            if len(parts) == m:
                ps = sorted(parts)
                if ps[-2] > (k + 2)//2:
                    return False
                return True
            return all(rec(rem - o, parts + [o], o) for o in range(lo, rem + 1))
        if not all(rec(tot, [], 0) for tot in range(0, k + 3)):
            return False
    return True


def o1():
    print("O1  the product split at order k (Proposition 9.8's commuted equation)")
    ks = list(range(5, 201))
    allok = all(split_ok(k) for k in ks)
    mk = min_k()
    check("O1a every source monomial has a split (highest w-order in L^2, the rest in sup with Lemma 9.3(a)) at "
          "every k = 5..200; minimal k = 5", allok and mk == 5, f"minimal k = {mk}")
    check("O1b [first clause arithmetic] the record's k = 6 and every larger k are covered (10.51(a)'s split at k - "
          "2: the sup factor has "
          "w-order <= (k + 2)/2 <= k - 2); and for every k the second-largest w-order of a monomial with 3 or 4 "
          "factors is at most that of a pair (checked k <= 40), so pairs decide the split above 40",
          all((k + 2)//2 <= k - 2 for k in range(6, 201)) and all(dominated(k) for k in range(1, MCAP + 1)))
    mk4 = min_k(sob=4)
    check("O1c control (Sobolev cost mutated 3 -> 4): the minimal k becomes 7, so 'k = 6 suffices' fails",
          mk4 == 7 and not split_ok(6, sob=4), f"minimal k with cost 4 = {mk4}")
    rk = min_k(reverse=True)
    check("O1d [arithmetic] control (split reversed: highest factor in sup): no k <= 200 works", rk is None)


# ---------------------------------------------------------------- O2: Proposition 9.8's closing at order k

lam, t, Ck, M, CR, Kp = sp.symbols("lambda t C_k M C_R Kp", positive=True)


def o2():
    print("O2  Proposition 9.8 at order k: the kernels and the closing")
    k1 = sp.integrate(Ck*t**sp.Rational(-3, 2), (t, lam**-2, sp.oo))
    k2 = sp.integrate(Ck/lam*t**sp.Rational(-3, 2), (t, lam**-2, sp.oo))
    check("O2a far-region kernels: int_(lam^-2)^oo C_k t^(-3/2) = 2 C_k lam, int C_k lam^-1 t^(-3/2) = 2 C_k: the "
          "Gronwall factor exp(2 C_k (1 + lam)) is lam-free; k enters only through C_k",
          sp.simplify(k1 - 2*Ck*lam) == 0 and sp.simplify(k2 - 2*Ck) == 0)
    # the closing: G := exp(2 C_k (1 + lam)) C_k ( 2 C_R lam^K' + 4 C_k M^2 lam^(2K' - 5) ) <= M lam^K' / ... ?
    def closes(Kpv):
        expr = (Ck*M**2*lam**(2*Kpv - 5))/(M*lam**Kpv)
        return sp.limit(expr.subs({Ck: 7, M: 11}), lam, 0, "+") == 0
    check("O2b [arithmetic] the nonlinear return C_k M^2 lam^(2K'-5) is o(M lam^K') as lam -> 0 exactly when K' > 5 "
          "(K' = 6, 9, 30 "
          "close; independent of k)", closes(6) and closes(9) and closes(30))
    check("O2c [arithmetic] control: K' = 5 does not close (the ratio tends to C_k M, not 0)", not closes(5))
    # M_F(k) := 4 C e^(6C) C_R + 1 returns E <= M_F lam^K' t^(-1/2) once lam is small
    Mf = 4*Ck*sp.exp(6*Ck)*CR + 1
    lhs = Ck*sp.exp(2*Ck*(1 + lam))*2*CR
    check("O2d [arithmetic] the data-and-residual part C_k e^(2 C_k (1 + lam)) 2 C_R is at most M_F(k)/2 for lam <= 1 "
          "(M_F(k) := 4 C_k e^(6 C_k) C_R + 1, the record's choice with C = C_k)",
          sp.simplify(sp.expand(Mf/2 - lhs.subs(lam, 1))) .subs({Ck: 1, CR: 1}) > 0
          and all((Mf/2 - lhs.subs(lam, 1)).subs({Ck: c, CR: r}) > 0 for c in (sp.Rational(1, 10), 1, 5)
                  for r in (sp.Rational(1, 10), 1, 50)))


# ---------------------------------------------------------------- O3: Proposition 9.9 at order k

def o3():
    print("O3  Proposition 9.9 at order k: the bootstrap integrals and the order of the approximant")
    tp, T, a, beta, C = sp.symbols("tp T a beta C", positive=True)
    # int_t^T tp^(-1-a) (T/tp)^beta dtp = T^beta (t^(-a-beta) - T^(-a-beta)) / (a + beta)
    exact = T**beta*(t**(-a - beta) - T**(-a - beta))/(a + beta)
    integrand = tp**(-1 - a)*(T/tp)**beta
    ok = True
    for av, bv in ((sp.Rational(1, 2), 2), (sp.Rational(-1, 2), 3), (1, sp.Rational(5, 2)), (-1, 2)):
        val = sp.integrate(integrand.subs({a: av, beta: bv}), (tp, t, T))
        ok = ok and sp.simplify(val - exact.subs({a: av, beta: bv})) == 0
    bound_ok = sp.simplify(t**(-a)*(T/t)**beta/(beta + a) - exact - T**beta*T**(-a - beta)/(a + beta)) == 0
    check("O3a int_t^T t'^(-1-a) (T/t')^beta dt' = T^beta (t^(-a-beta) - T^(-a-beta))/(a + beta) <= t^-a (T/t)^beta"
          " / (beta + a) (beta + a > 0; four exact cases and the symbolic bound)", ok and bound_ok)
    x = sp.Symbol("x", positive=True)  # x = T/t >= 1
    ok2 = True
    for bv in (sp.Rational(3, 2), 2, 3, sp.Rational(9, 4)):
        g = x**bv/bv - sp.log(x)
        ok2 = ok2 and sp.simplify(sp.diff(g, x) - (x**bv - 1)/x) == 0 and g.subs(x, 1) > 0
    check("O3b log(T/t) <= (T/t)^beta / beta for beta > 1: g(x) := x^beta/beta - log x has g(1) = 1/beta > 0 and "
          "g'(x) = (x^beta - 1)/x >= 0 on x >= 1 (four beta)", ok2)
    ctlb = sp.limit(sp.log(x)/x**0, x, sp.oo)
    check("O3b' control (the growth factor removed, beta = 0): log(T/t) is not bounded by (T/t)^0 = 1 as T/t -> oo, "
          "so the bootstrap's weight (T/t)^beta is what absorbs the Q'-line's t^-1 H term", ctlb == sp.oo)
    b0 = sp.Max(2, 4*C + 1)
    ret = [(C/(b0 - 1)).subs(C, cv) for cv in (sp.Rational(1, 10), sp.Rational(1, 4), 1, 3, 40)]
    check("O3c [arithmetic] beta0(k) := max(2, 4 C(k) + 1): each integral of (9.9) returns C/(beta0 - 1) <= 1/4 of "
          "its bound, "
          "at every C = C(k)", all(r <= sp.Rational(1, 4) for r in ret), str(ret))
    Kv = sp.Symbol("K", integer=True, positive=True)

    def closing(Krule, Kval, b0v):
        N = Krule(Kval, b0v)
        Kpv = N - 1
        return Kpv > 8 + 4*b0v and Kpv - 2*b0v >= Kval

    rule = lambda K, b: K + 4 + sp.ceiling(4*b)
    ok3 = all(closing(rule, K, b) for K in range(6, 30) for b in
              (2, sp.Rational(9, 4), 3, 7, sp.Rational(101, 3), 1000))
    check("O3d N = K + 4 + ceil(4 beta0(k)): K' = N - 1 > 8 + 4 beta0 (the nonlinear terms C B^2 lam^(-8-4beta0) "
          "small against B) and K' - 2 beta0 >= K ((P-iii)'s absorption), for every K >= 6 and every beta0", ok3)
    bad = lambda K, b: K + 4 + sp.ceiling(2*b)
    check("O3e [arithmetic] control (the order rule mutated to K + 4 + ceil(2 beta0)): the closing fails at K = 6, "
          "beta0 = 4",
          not closing(bad, 6, 4))


# ---------------------------------------------------------------- O4: the commutation facts

def o4():
    print("O4  the commutation facts (Lemma 9.6 transports, the Z's of N_P, the rotations)")
    tau = sp.Symbol("tau", real=True)
    X = sp.symbols("x1 x2 x3 x4", real=True)
    r = sp.sqrt(sum(c**2 for c in X))
    f = sp.Function("f")(tau, *X)

    def L0(u):
        return sp.diff(u, tau) - sum(c/r*sp.diff(u, c) for c in X)

    def dr(u):
        return sum(c/r*sp.diff(u, c) for c in X)

    def Om(u, i=0, j=1):
        return X[i]*sp.diff(u, X[j]) - X[j]*sp.diff(u, X[i])

    def comm(A, B, u):
        return sp.simplify(A(B(u)) - B(A(u)))

    ok = (comm(lambda u: sp.diff(u, tau), L0, f) == 0 and comm(dr, L0, f) == 0 and comm(Om, L0, f) == 0
          and comm(lambda u: Om(u, 1, 3), L0, f) == 0)
    check("O4a [Z, L0] = 0 for Z = d_tau, d_r, Omega_12, Omega_24 on a generic function", ok)
    c = sp.Symbol("c", positive=True)
    ok2 = (sp.simplify(dr(r**-c*f) - r**-c*dr(f) + c*r**(-c - 1)*f) == 0 and
           sp.simplify(Om(r**-c*f) - r**-c*Om(f)) == 0 and sp.simplify(sp.diff(r**-c*f, tau) - r**-c*sp.diff(f, tau))
           == 0)
    check("O4b [d_r, r^-c] = -c r^(-c-1), [Omega, r^-c] = [d_tau, r^-c] = 0 (the transports keep c0 at every order)",
          ok2)
    ctl = comm(lambda u: sp.diff(u, X[0]), L0, f) != 0
    check("O4c control: the Cartesian d_1 does not commute with L0 (hence N_P's Z are d_tau, d_r, Omega)", ctl)
    # [Omega_12, box~] = 0 for g0 = eta + mu(v)/r^2 dv dv, v = tau + r, componentwise on functions
    mu = sp.Function("mu")
    v = tau + r
    XS = (tau,) + X
    k = [sp.Integer(1)] + [cc/r for cc in X]
    eta = sp.diag(-1, 1, 1, 1, 1)
    L = [eta[i, i]*k[i] for i in range(5)]
    gi = sp.Matrix(5, 5, lambda i, j: eta[i, j] - mu(v)/r**2*L[i]*L[j])
    u = sp.Function("u")(*XS)

    def box(w):
        return sum(gi[i, j]*sp.diff(w, XS[i], XS[j]) for i in range(5) for j in range(5))

    def Om5(w, i=1, j=2):
        return XS[i]*sp.diff(w, XS[j]) - XS[j]*sp.diff(w, XS[i])

    val = sp.simplify(sp.expand(Om5(box(u)) - box(Om5(u))))
    check("O4d [Omega_12, box~] = 0 on every function, g0 = eta + mu(v) r^-2 dv dv (P6 of past5.py, recomputed)",
          val == 0)

    def Bad(w):
        return XS[1]*sp.diff(w, XS[2]) + XS[2]*sp.diff(w, XS[1])

    ctl2 = sp.simplify(sp.expand(Bad(box(u)) - box(Bad(u)))) != 0
    check("O4e control: x1 d_2 + x2 d_1 does not commute with box~", ctl2)


# ---------------------------------------------------------------- O5: Theorem P at order k

def o5():
    print("O5  Theorem P at order k: the same g_lam, and the orders used later")
    b0 = lambda Cv: max(2, 4*Cv + 1)
    Ns = [6 + 4 + sp.ceiling(4*b0(Cv)) for Cv in (sp.Rational(1, 2), 1, 3, 10)]
    check("O5a [arithmetic] N(k) = K + 4 + ceil(4 beta0(k)) grows with C(k) (K = 6; C = 1/2, 1, 3, 10)",
          all(Ns[i] < Ns[i + 1] for i in range(len(Ns) - 1)), str(Ns))
    # g_app^(N(k)) - g_app^(N(6)) = sum_(j = N6 + 1)^(Nk) lam^j [g_j]: C^1 size lam^N6 t^(-3/2) (d [g_j] costs lam^-1)
    N6, Nk = 18, 30
    size = sum(lam**j*lam**-1 for j in range(N6 + 1, Nk + 1))
    lead = sp.limit(size/lam**N6, lam, 0, "+")
    check("O5b [arithmetic] g_app^(N(k)) - g_app^(N(6)) is lam^N(6) (1 + O(lam)) t^(-3/2) in C^1: inside (P-v)'s class "
          "|g - g_app| + |d(g - g_app)| <= eps_P t^(-3/2) for lam small, so the order-k solution is g_lam", lead == 1)
    check("O5c [arithmetic] (P-iii) at order k bounds d^i e for i <= k - 3; Proposition R3.1 at n derivatives needs "
          "k = n + 4: "
          "both finite for every n", all((n + 4) - 3 >= n + 1 for n in range(0, 100)))


def main():
    for f in (o1, o2, o3, o4, o5):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
