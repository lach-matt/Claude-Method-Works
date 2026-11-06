#!/usr/bin/env python3
"""tame5.py -- the tame clause of Lemma 6.4 (N1STAR-PROOF.md section 6.3), D619: which energy inequality the proof gives.

D26 stated, for the squared energy Z at an index s'' > s,
    d_r Z + c0 ||a||^2_(H^(s''+2)) <= omega_0 Z + C ||F||^2_(H^(s'')) + C m_(s'') omega_s Z^(1/2),
with omega_0, C depending only on the low norms (M_s).  The section 6 reader of 2026-11-06 (m1) found that false: the
lower-order coefficients b, c, e of the first equation of (6.4) lie in H^(s'') only, so pairing that equation at index
s'' + 1 moves one derivative onto a, |<a, c a>_(s''+1)| <= ||a||_(s''+2) ||c a||_(s''), and Young's inequality against
the gain c0 ||a||^2_(s''+2) leaves C m_(s'')^2 omega_inf^2 (omega_inf a low norm of the solution).  The model here is
the first equation on S^1, alpha = 1, Delta_alpha = d_th^2, F = 0:
    (row c)  d_r a = a_thth - c a;          (row e)  d_r a = a_thth - e w, d_r w = 0
(row e is the coupling e . (w, q) with w frozen).  Norms ||f||^2_sig := sum_n (1 + n^2)^sig |f_n|^2 over the Fourier
coefficients, s = 4, s'' = 8; the instantaneous quantities at a state (a, c) are computed in exact rational arithmetic:
    LHS := d_r Z + c0 ||a||^2_(s''+2) = 2 <a, a_thth - c a>_(s''+1) + c0 ||a||^2_(s''+2),  Z := ||a||^2_(s''+1),
    m := ||c||_(s''),  L := sum |c_n| (>= sup |c|),  omega := sum |a_n| (>= sup |a|; for row e, + sum |w_n|).
The family (the reader's tame_ctrex): k = 2^j, M := k^(s''-s)/10, a = 1 - M k^-(s''+2) cos(k th),
c = M k^-(s'') cos(k th); then ||c||_(H^s), L, ||a||_(H^(s+1)) and omega stay bounded while m, Z grow.

  T1 (exact) D26's inequality fails on the family for every pair of constants: LHS > (c0 k/16) (Z + m omega Z^(1/2))
     at every k = 2^2, ..., 2^17, for c0 = 1 and c0 = 1/100, both rows, while the low norms stay below fixed bounds; so
     no omega_0, C depending only on the low norms give LHS <= omega_0 Z + C m omega Z^(1/2).  LHS/(m^2 omega^2) stays
     of order c0: the scale of the missing term.  (The family's k-mode is stationary, -k^2 a_k = (c a)_k, so d_r Z is
     tiny and LHS is essentially the gain c0 ||a||^2_(s''+2): it is the gain D26's right side cannot pay for.)
     Control: the same family with the lower-order term removed (c = 0 in the equation) does not grow (LHS <= 2 Z).
  T2 (exact) The corrected inequality holds, with the explicit constants of its proof (c0 = 1, sig := s''):
         LHS <= (2 + 2 * 4^(sig-1) L^2) Z + 2 * 4^(sig-1) m^2 omega^2,
     from LHS = -||a||^2_(sig+2) + 2 Z - 2 <a, c a>_(sig+1) <= 2 Z + ||c a||^2_sig and the product bound
     ||c a||_sig <= 2^(sig-1) (||c||_sig sum|a_n| + sum|c_n| ||a||_sig) (<n + m'> <= <n> + <m'>, convexity, Young
     l^2 * l^1), on the family (both rows, every k) and on 300 random trigonometric polynomials (random frequencies up to
     48 with a high-frequency spike in c, random rational coefficients), and each of the proof's two steps separately
     at every state ((i) LHS <= 2 Z + ||c a||^2_sig, (ii) the product bound, squared).  T1 also computes d_r Z by a
     second route, Z along a + h d_r a (a quadratic in h, so the central difference is exact), and requires the two to
     agree (on the family the k-mode is stationary, so the agreement is tested at the random states too), and T2
     computes the lower-order term c a (or e w) a second way, as a product of Laurent polynomials in sympy.  Control:
     the test with the term 2 * 4^(sig-1) m^2 omega^2 replaced by D26's 2 * 4^(sig-1) m omega Z^(1/2)
     fails on the family.
  T3 (computed, floating point) Proposition 6.5's induction: the extremal recursion E_(i+1)(r) = A + W (int_a^r
     E_i^2)^(1/2), E_0 = 0, A = 1, W = 3 on [0, 2] (4000 trapezoid steps, 60 iterates) stays below A sum_k W^k
     ((r - a)^k / k!)^(1/2) (ratio <= 1 + 1e-9); the bound is the fixed point of the Minkowski step, exact by
     int_a^r (r' - a)^k / k! dr' = (r - a)^(k+1) / (k+1)!.  Control: W_i = W + i (not uniform in i) exceeds it tenfold.

Labels: T1, T2 computed (exact, a scalar model on S^1); T3 computed (floating point).  The model is the first
equation of (6.4) with its lower-order term; it shows the mechanism, not the full system.
Run: python3 checks/tame5.py   (a few seconds)
"""
import math
import random
import sys
import textwrap
from fractions import Fraction as Fr

S_LOW, SIG = 4, 8


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def norm2(f, sig):
    return sum((1 + n * n) ** sig * c * c for n, c in f.items())


def inner(f, g, sig):
    return sum((1 + n * n) ** sig * f[n] * g.get(n, 0) for n in f)


def mul(f, g):
    h = {}
    for n, c in f.items():
        for m_, d in g.items():
            h[n + m_] = h.get(n + m_, 0) + c * d
    return h


def wiener(f):
    return sum(abs(c) for c in f.values())


def lap(f):
    return {n: -n * n * c for n, c in f.items()}


def rhs(row, a, coef, w=None):
    """d_r a of the model, and the lower-order term c a (row c) or e w (row e)"""
    low = mul(coef, a) if row == 'c' else mul(coef, w)
    la = lap(a)
    return {n: la.get(n, 0) - low.get(n, 0) for n in set(la) | set(low)}, low


def state(row, a, coef, w=None):
    """the instantaneous quantities of the model at the state: LHS(c0) as a function, Z, m^2, L, omega"""
    dra, _ = rhs(row, a, coef, w)
    dZ = 2 * inner(a, dra, SIG + 1)
    top = norm2(a, SIG + 2)
    Z = norm2(a, SIG + 1) + (norm2(w, SIG) if row == 'e' else 0)
    omega = wiener(a) + (wiener(w) if row == 'e' else 0)
    return (lambda c0: dZ + c0 * top), Z, norm2(coef, SIG), wiener(coef), omega


def dZ_independent(row, a, coef, w=None):
    """d_r Z by a second route: Z(a + h d_r a) = Z + h dZ + h^2 ||d_r a||^2 is a quadratic in h, so
    dZ = (Z(a + h d_r a) - Z(a - h d_r a)) / (2 h) exactly, for any h (h = 1/7 here); w is frozen (d_r w = 0)"""
    dra, _ = rhs(row, a, coef, w)
    h = Fr(1, 7)
    ap = {n: a.get(n, 0) + h * dra.get(n, 0) for n in set(a) | set(dra)}
    am = {n: a.get(n, 0) - h * dra.get(n, 0) for n in set(a) | set(dra)}
    return (norm2(ap, SIG + 1) - norm2(am, SIG + 1)) / (2 * h)


def family_state(k, row, drop=False):
    M = Fr(k ** (SIG - S_LOW), 10)
    a = {0: Fr(1), k: -M * Fr(1, k ** (SIG + 2)) / 2, -k: -M * Fr(1, k ** (SIG + 2)) / 2}
    coef = {k: M * Fr(1, k ** SIG) / 2, -k: M * Fr(1, k ** SIG) / 2}
    if drop:
        coef = {k: Fr(0), -k: Fr(0)}
    w = {0: Fr(1)} if row == 'e' else None
    return a, coef, w


def family(k, row, drop=False):
    a, coef, w = family_state(k, row, drop)
    low = (norm2(coef, S_LOW), wiener(coef), norm2(a, S_LOW + 1), wiener(a))
    return state(row, a, coef, w), low


KS = [2 ** j for j in range(2, 18)]


def gt_sqrt(lhs, X, Z, m2, om):
    """exact test of lhs > X (Z + m omega Z^(1/2)), m^2 = m2"""
    d = lhs - X * Z
    return d > 0 and d * d > X * X * m2 * om * om * Z


def t1(control=False):
    ok, rows = True, []
    for row in ('c', 'e'):
        for c0 in (Fr(1), Fr(1, 100)):
            lowmax, grow, ratios, route = [0, 0, 0, 0], True, [], True
            for k in KS:
                (LHS, Z, m2, L, om), low = family(k, row, drop=control)
                lowmax = [max(x, float(y)) for x, y in zip(lowmax, low)]
                lhs = LHS(c0)
                route &= LHS(Fr(0)) == dZ_independent(row, *family_state(k, row, drop=control))
                grow &= gt_sqrt(lhs, c0 * k / 16, Z, m2, om)
                if not control and k in (4, 64, 2 ** 17):
                    ratios.append("k = %d: LHS/(Z + m omega Z^1/2) = %.4g, LHS/(m^2 omega^2) = %.4g" % (
                        k, float(lhs) / (float(Z) + math.sqrt(float(m2) * float(Z)) * float(om)),
                        float(lhs) / (float(m2) * float(om) ** 2)))
            bounded = lowmax[0] < 0.01 and lowmax[1] < 0.01 and lowmax[2] < 2 and lowmax[3] < 2
            ok &= grow and (bounded or control) and route
            if not control:
                rows.append("row %s, c0 = %s: LHS > (c0 k/16)(Z + m omega Z^1/2) at every k: %s; d_r Z equal to the"
                            " second route's (Z along a + h d_r a): %s; low norms (max over k: ||c||^2_(H^4) %.3g,"
                            " sum|c_n| %.3g, ||a||^2_(H^5) %.4g, omega_a %.4g) bounded: %s; %s" % (
                                row, c0, grow, route, lowmax[0], lowmax[1], lowmax[2], lowmax[3], bounded,
                                "; ".join(ratios)))
    if not control:
        out("  T1 " + " || ".join(rows))
    return ok


def corrected(LHS, Z, m2, L, om, d26=False):
    B = 2 * 4 ** (SIG - 1)
    lhs = LHS(Fr(1))
    base = (2 + B * L * L) * Z
    if d26:   # lhs <= base + B m omega Z^(1/2), exact
        d = lhs - base
        return d <= 0 or d * d <= B * B * m2 * om * om * Z
    return lhs <= base + B * m2 * om * om


def steps(row, a, coef, w=None):
    """the proof's two steps, each exact: (i) LHS(1) <= 2 Z + ||low||^2_sig (Cauchy-Schwarz and Young against the
    gain); (ii) the product bound ||low||_sig <= 2^(sig-1) (m ||f||_l1 + L ||f||_sig), f = a (row c) or w (row e),
    tested in the squared form the corrected inequality uses, ||low||^2_sig <= 2 * 4^(sig-1) (m^2 ||f||_l1^2 +
    L^2 ||f||^2_sig) (it follows from the product bound by (x + y)^2 <= 2 x^2 + 2 y^2; exact, no square roots)"""
    LHS, Z, m2, L, om = state(row, a, coef, w)
    _, low = rhs(row, a, coef, w)
    f = a if row == 'c' else w
    i_ok = LHS(Fr(1)) <= 2 * Z + norm2(low, SIG)
    lhs2 = norm2(low, SIG)
    x2, y = m2 * wiener(f) ** 2, L * L * norm2(f, SIG)
    ii_ok = lhs2 <= 4 ** (SIG - 1) * 2 * (x2 + y)
    return i_ok, ii_ok


def laurent_product(f, g):
    """f g by a second route: the two as Laurent polynomials in z = e^(i th), multiplied by sympy"""
    import sympy as sp
    z = sp.Symbol('z')
    sh = max(abs(n) for n in list(f) + list(g))
    pf = sp.Poly(sum(sp.Rational(c.numerator, c.denominator) * z**(n + sh) for n, c in f.items()), z)
    pg = sp.Poly(sum(sp.Rational(c.numerator, c.denominator) * z**(n + sh) for n, c in g.items()), z)
    res = {}
    for (e,), c in (pf * pg).terms():
        if c != 0:
            res[e - 2 * sh] = Fr(int(c.p), int(c.q))
    return res


def rand_poly(rng, kmax, spike=None):
    f = {}
    for n in rng.sample(range(0, kmax + 1), 5):
        v = Fr(rng.randint(-30, 30), rng.randint(1, 9))
        f[n] = f.get(n, 0) + (v if n == 0 else v / 2)
        if n:
            f[-n] = f[n]
    if spike:
        k, amp = spike
        f[k] = f.get(k, 0) + amp / 2
        f[-k] = f.get(-k, 0) + amp / 2
    return f


def t2(control=False):
    fam_ok, n_fam = True, 0
    for row in ('c', 'e'):
        for k in KS:
            (LHS, Z, m2, L, om), _ = family(k, row)
            fam_ok &= corrected(LHS, Z, m2, L, om, d26=control)
            n_fam += 1
    if control:
        return fam_ok
    rng = random.Random(619)
    rnd_ok, step_ok, route_ok, prod_ok, n_rnd = True, True, True, True, 0
    for k in KS:
        for row in ('c', 'e'):
            step_ok &= all(steps(row, *family_state(k, row)))
    for i in range(300):
        row = 'c' if i % 2 == 0 else 'e'
        a = rand_poly(rng, 48)
        k = rng.randint(30, 48)
        coef = rand_poly(rng, 12, spike=(k, Fr(rng.randint(1, 50) * k ** (SIG - S_LOW), k ** SIG)))
        w = rand_poly(rng, 48) if row == 'e' else None
        rnd_ok &= corrected(*state(row, a, coef, w))
        step_ok &= all(steps(row, a, coef, w))
        route_ok &= state(row, a, coef, w)[0](Fr(0)) == dZ_independent(row, a, coef, w)
        if i < 40:
            low = {n_: c for n_, c in rhs(row, a, coef, w)[1].items() if c != 0}
            prod_ok &= low == laurent_product(coef, a if row == 'c' else w)
        n_rnd += 1
    out("  T2 corrected inequality LHS <= (2 + 2 4^7 L^2) Z + 2 4^7 m^2 omega^2 (c0 = 1): family (%d states, rows c and"
        " e) %s; random trigonometric polynomials (%d states) %s; the proof's two steps, (i) LHS <= 2 Z + ||c a||^2_8"
        " and (ii) the product bound, at every state: %s; d_r Z equal to the second route's at the random states: %s;"
        " the lower-order term equal to the product as Laurent polynomials (sympy, 40 states): %s"
        % (n_fam, fam_ok, n_rnd, rnd_ok, step_ok, route_ok, prod_ok))
    return fam_ok and rnd_ok and step_ok and route_ok and prod_ok


def t3(control=False):
    A, W, Lr, n = 1.0, 3.0, 2.0, 4000
    h = Lr / n
    bound = [A * sum(W ** k * math.sqrt((i * h) ** k / math.factorial(k)) for k in range(90)) for i in range(n + 1)]
    E, worst = [0.0] * (n + 1), 0.0
    for it in range(60):
        Wi = W + it if control else W
        acc, new = 0.0, [A]
        try:
            for i in range(1, n + 1):
                acc += h * (E[i - 1] ** 2 + E[i] ** 2) / 2
                new.append(A + Wi * math.sqrt(acc))
        except OverflowError:
            return control
        E = new
        worst = max(worst, max(e / b for e, b in zip(E, bound)))
    if control:
        return worst <= 10
    out("  T3 max over 60 iterates and 4001 points of E_i / (A sum W^k ((r-a)^k/k!)^(1/2)) = %.12f; E_60(2) = %.6f,"
        " bound(2) = %.6f" % (worst, E[-1], bound[-1]))
    return worst <= 1 + 1e-9


def main():
    ok = True
    for name, f in (("T1", t1), ("T2", t2), ("T3", t3)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("tame5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
